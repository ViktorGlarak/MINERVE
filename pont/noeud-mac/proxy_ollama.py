#!/usr/bin/env python3
"""Proxy Ollama du nœud de calcul MAC — même contrat que le proxy du PC (avis CYBERSECU du 2026-10-12, réserves O1-O8).

Le serveur PLÉIADE (app-ia) joint Ollama du Mac PAR LE VPN SEULEMENT, avec un jeton. Ollama reste sur 127.0.0.1:11434.

    python3 -I proxy_ollama.py --ecoute 10.8.0.X --sources 10.8.0.1
    python3 -I proxy_ollama.py --essai          (127.0.0.1, jeton jetable, pour essai_proxy.py)

O1  écoute sur l'IP VPN donnée SEULEMENT (absente d'une interface → arrêt, jamais 0.0.0.0) ; cible FIXE 127.0.0.1:11434 ;
    méthode + chemin EXACTS (POST /api/chat, POST /api/embed, GET /api/tags ; le reste 404, `?` compris) ;
    `model` ∈ liste blanche sinon 403 ; corps compté en octets lus ≤ plafond sinon 413 ; en-têtes reconstruits
    (Content-Type seul vers Ollama) ; en-tête Origin → 403, aucun CORS ; adresse source ∈ --sources sinon 403 ;
    2 requêtes simultanées au plus (503 au-delà) ; délais bornés ; tourne sous le compte utilisateur.
O2  jeton 32 octets aléatoires dans ~/.pleiade/ollama-cle.txt (0600, hors dépôt), créé s'il manque, JAMAIS affiché ;
    comparaison à temps constant des empreintes SHA-256 ; 401 sans détail ; 10 échecs → blocage 10 min de la source.
O5  journal ~/.pleiade/proxy-ollama.log : heure, source, méthode, route, modèle, statut, durée, taille — jamais le corps,
    la réponse ni l'en-tête Authorization.
D1  corps reconstruit depuis une liste blanche de champs ; options numériques seulement (400 sinon), bornées
    (num_ctx 1-16384, num_predict 1-2048) ; keep_alive forcé à "30m".
A9  1 image par requête au plus ; 1 Mo sans image, --plafond-ko (≤ 2 048) avec image.
"""
import argparse, hashlib, hmac, http.client, http.server, json, os, secrets, socket, subprocess, sys, threading, time

DOSSIER = os.path.expanduser("~/.pleiade")
FICHIER_CLE = os.path.join(DOSSIER, "ollama-cle.txt")
JOURNAL = os.path.join(DOSSIER, "proxy-ollama.log")
PORT = 11435
CIBLE = ("127.0.0.1", 11434)
MODELES = {"gemma4:26b-a4b-it-qat", "gemma4:31b-it-qat", "bge-m3"}
ROUTES = {("POST", "/api/chat"), ("POST", "/api/embed"), ("GET", "/api/tags")}
CHAMPS = {"/api/chat": {"model", "messages", "stream", "format", "think", "options", "tools"},
          "/api/embed": {"model", "input", "truncate", "options"}}
OPTIONS = {"temperature", "top_p", "top_k", "num_ctx", "num_predict", "num_gpu", "seed", "repeat_penalty", "stop"}
BORNES = {"num_ctx": 16384, "num_predict": 2048}
PLAFOND_TEXTE = 1024 * 1024  # 1 Mo sans image ; --plafond-ko (2 048 au plus) ne vaut que pour une requête avec image
SIMULTANES = threading.BoundedSemaphore(2)
echecs, bloques, verrou = {}, {}, threading.Lock()


def lire_ou_creer_cle(essai):
    if essai:
        return secrets.token_hex(32)
    os.makedirs(DOSSIER, mode=0o700, exist_ok=True)
    if not os.path.exists(FICHIER_CLE):
        fd = os.open(FICHIER_CLE, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
        with os.fdopen(fd, "w") as f:
            f.write(secrets.token_hex(32))
        print(f"Jeton créé dans {FICHIER_CLE} (droits 600). Il n'est pas affiché.", flush=True)
    os.chmod(FICHIER_CLE, 0o600)
    return open(FICHIER_CLE).read().strip()


def ip_presente(ip):
    sortie = subprocess.run(["ifconfig"], capture_output=True, text=True).stdout
    return f"inet {ip} " in sortie


def journal(ligne):
    fd = os.open(JOURNAL, os.O_WRONLY | os.O_CREAT | os.O_APPEND, 0o600)
    with os.fdopen(fd, "a") as f:
        f.write(time.strftime("%Y-%m-%dT%H:%M:%S ") + ligne + "\n")


class Relais(http.server.BaseHTTPRequestHandler):
    server_version, sys_version = "noeud", ""
    timeout = 10  # en-têtes et corps : 10 s

    def log_message(self, *a):  # pas de journal par défaut (il contiendrait la requête)
        pass

    def repondre(self, statut, corps=b"", modele="-", t0=None):
        self.send_response(statut)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(corps)))
        self.end_headers()
        if corps:
            self.wfile.write(corps)
        duree = f"{time.time() - t0:.1f}s" if t0 else "-"
        journal(f"{self.client_address[0]} {self.command} {self.path[:60]!r} {modele} {statut} {duree} {len(corps)}o")

    def traiter(self):
        t0, src = time.time(), self.client_address[0]
        if src not in self.server.sources:
            return self.repondre(403, t0=t0)
        with verrou:
            if bloques.get(src, 0) > time.time():
                return self.repondre(429, t0=t0)
        if self.headers.get("Origin") is not None:
            return self.repondre(403, t0=t0)
        if (self.command, self.path) not in ROUTES:
            return self.repondre(404, t0=t0)
        recu = (self.headers.get("Authorization") or "").removeprefix("Bearer ").strip().encode()
        if not hmac.compare_digest(hashlib.sha256(recu).digest(), self.server.empreinte):
            with verrou:
                echecs[src] = echecs.get(src, 0) + 1
                if echecs[src] >= 10:
                    bloques[src], echecs[src] = time.time() + 600, 0
                    journal(f"{src} BLOQUÉ 10 min après 10 échecs de jeton")
            return self.repondre(401, t0=t0)
        with verrou:
            echecs.pop(src, None)
        corps, modele = None, "-"
        if self.command == "POST":
            try:
                attendu = int(self.headers.get("Content-Length", "-1"))
            except ValueError:
                return self.repondre(411, t0=t0)
            if attendu < 0:
                return self.repondre(411, t0=t0)
            if attendu > self.server.plafond:
                return self.repondre(413, t0=t0)
            brut = self.rfile.read(attendu)
            if len(brut) != attendu or len(brut) > self.server.plafond:
                return self.repondre(413, t0=t0)
            try:
                donnees = json.loads(brut)
                assert isinstance(donnees, dict)
            except Exception:
                return self.repondre(400, t0=t0)
            modele = str(donnees.get("model", "-"))[:40]
            if modele not in MODELES:
                return self.repondre(403, modele=modele, t0=t0)
            propre = {k: v for k, v in donnees.items() if k in CHAMPS[self.path]}
            if "options" in propre:
                if not isinstance(propre["options"], dict):
                    return self.repondre(400, modele=modele, t0=t0)
                opts = {k: v for k, v in propre["options"].items() if k in OPTIONS}
                for k, v in opts.items():  # options numériques seulement (sauf stop : liste de chaînes)
                    if k == "stop":
                        if not (isinstance(v, list) and all(isinstance(x, str) for x in v)):
                            return self.repondre(400, modele=modele, t0=t0)
                    elif isinstance(v, bool) or not isinstance(v, (int, float)):
                        return self.repondre(400, modele=modele, t0=t0)
                for k, maxi in BORNES.items():  # bornes basses aussi : num_predict -1/-2 = génération sans fin
                    if k in opts and not 1 <= opts[k] <= maxi:
                        opts[k] = min(max(opts[k], 1), maxi)
                propre["options"] = opts
            images = [i for m in propre.get("messages", []) if isinstance(m, dict) for i in (m.get("images") or [])]
            if len(images) > 1:  # 1 image par requête au plus (avis CYBERSECU A9)
                return self.repondre(413, modele=modele, t0=t0)
            if not images and len(brut) > PLAFOND_TEXTE:  # le plafond large n'est admis qu'avec une image
                return self.repondre(413, modele=modele, t0=t0)
            propre["keep_alive"] = "30m"
            corps = json.dumps(propre).encode()
        if not SIMULTANES.acquire(blocking=False):
            return self.repondre(503, modele=modele, t0=t0)
        try:
            cnx = http.client.HTTPConnection(*CIBLE, timeout=180)
            cnx.request(self.command, self.path, body=corps, headers={"Content-Type": "application/json"} if corps else {})
            rep = cnx.getresponse()
            contenu = rep.read()
            statut = rep.status
            cnx.close()
        except Exception:
            return self.repondre(504, modele=modele, t0=t0)
        finally:
            SIMULTANES.release()
        return self.repondre(statut, contenu, modele, t0)

    def do_GET(self):
        self.traiter()

    def do_POST(self):
        self.traiter()

    def __getattr__(self, nom):  # PUT, DELETE, HEAD, OPTIONS… → 404
        if nom.startswith("do_"):
            return lambda: self.repondre(404)
        raise AttributeError(nom)


def main():
    a = argparse.ArgumentParser()
    a.add_argument("--ecoute", help="adresse VPN du Mac (10.8.0.X)")
    a.add_argument("--sources", default="", help="adresses autorisées, séparées par des virgules (l'IP du serveur observée)")
    a.add_argument("--plafond-ko", type=int, default=1024, help="taille max d'une requête AVEC image (Ko, 2 048 au plus, avis A9) ; sans image : 1 Mo")
    a.add_argument("--essai", action="store_true", help="127.0.0.1, jeton jetable écrit dans ~/.pleiade/essai-cle.txt")
    o = a.parse_args()
    os.makedirs(DOSSIER, mode=0o700, exist_ok=True)
    if not 1 <= o.plafond_ko <= 2048:
        sys.exit("Arrêt : --plafond-ko doit être compris entre 1 et 2 048 (avis CYBERSECU A9).")
    if o.essai:
        ecoute, sources = "127.0.0.1", {"127.0.0.1"}
    else:
        if not o.ecoute or not o.ecoute.startswith("10.8.0.") or not ip_presente(o.ecoute):
            sys.exit(f"Arrêt : l'adresse VPN {o.ecoute!r} n'est portée par aucune interface (VPN connecté ?). Aucune liaison large.")
        ecoute, sources = o.ecoute, {s.strip() for s in o.sources.split(",") if s.strip()}
        if not sources:
            sys.exit("Arrêt : --sources est obligatoire (l'adresse du serveur observée dans le journal).")
    cle = lire_ou_creer_cle(o.essai)
    if o.essai:
        f = os.path.join(DOSSIER, "essai-cle.txt")
        fd = os.open(f, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
        with os.fdopen(fd, "w") as h:
            h.write(cle)
    if os.geteuid() == 0:
        sys.exit("Arrêt : ne jamais lancer le proxy en administrateur (root).")
    serveur = http.server.ThreadingHTTPServer((ecoute, PORT), Relais)
    serveur.empreinte = hashlib.sha256(cle.encode()).digest()
    serveur.sources, serveur.plafond = sources, o.plafond_ko * 1024
    serveur.daemon_threads = True
    journal(f"DÉMARRAGE écoute {ecoute}:{PORT} sources {sorted(sources)} plafond {o.plafond_ko} Ko essai={o.essai}")
    print(f"Proxy Ollama : {ecoute}:{PORT} → 127.0.0.1:11434 · sources {sorted(sources)} · Ctrl+C pour arrêter.", flush=True)
    try:
        serveur.serve_forever()
    except KeyboardInterrupt:
        journal("ARRÊT")


if __name__ == "__main__":
    main()
