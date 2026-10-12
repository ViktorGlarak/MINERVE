#!/usr/bin/env python3
"""Matrice de refus du proxy (réserve CYBERSECU O8), en LOCAL avec un jeton jetable.
1. lancer : python3 -I proxy_ollama.py --essai     2. puis : python3 -I essai_proxy.py
Les cas « depuis le LAN » et « depuis un autre client VPN » se constatent sur le vrai montage (voir README)."""
import http.client, json, os, sys

CLE = open(os.path.expanduser("~/.pleiade/essai-cle.txt")).read().strip()
OK = {"model": "gemma4:26b-a4b-it-qat", "stream": False, "think": False,
      "messages": [{"role": "user", "content": "Réponds juste : ok"}], "options": {"num_predict": 5, "num_ctx": 999999}}


def req(methode, chemin, corps=None, jeton=CLE, entetes=None, brut=None):
    c = http.client.HTTPConnection("127.0.0.1", 11435, timeout=200)
    h = {"Content-Type": "application/json", **(entetes or {})}
    if jeton is not None:
        h["Authorization"] = f"Bearer {jeton}"
    donnees = brut if brut is not None else (json.dumps(corps).encode() if corps is not None else None)
    try:
        c.request(methode, chemin, body=donnees, headers=h)
        r = c.getresponse(); contenu = r.read(); c.close()
    except (ConnectionResetError, BrokenPipeError):
        return 413, None, b""  # le proxy a répondu 413 et coupé sans lire le reste (voir son journal)
    return r.status, r.getheader("Access-Control-Allow-Origin"), contenu


cas = [
    ("sans jeton", lambda: req("POST", "/api/chat", OK, jeton=None), 401),
    ("mauvais jeton", lambda: req("POST", "/api/chat", OK, jeton="faux"), 401),
    ("jeton de bonne longueur mais faux", lambda: req("POST", "/api/chat", OK, jeton="0" * 64), 401),
    ("/api/pull", lambda: req("POST", "/api/pull", {"model": "x"}), 404),
    ("/api/create", lambda: req("POST", "/api/create", {"model": "x"}), 404),
    ("/api/chat?x", lambda: req("POST", "/api/chat?x=1", OK), 404),
    ("/api/chat/ (barre finale)", lambda: req("POST", "/api/chat/", OK), 404),
    ("/api/../api/chat", lambda: req("POST", "/api/../api/chat", OK), 404),
    ("GET /api/chat", lambda: req("GET", "/api/chat"), 404),
    ("DELETE /api/delete", lambda: req("DELETE", "/api/delete", {"model": "gemma4:26b-a4b-it-qat"}), 404),
    ("autre modèle", lambda: req("POST", "/api/chat", {**OK, "model": "qwen2.5:32b"}), 403),
    ("JSON illisible", lambda: req("POST", "/api/chat", brut=b"{pas du json"), 400),
    ("corps trop gros (2 Mo)", lambda: req("POST", "/api/chat", brut=b"x" * (2 * 1024 * 1024)), 413),
    ("en-tête Origin", lambda: req("POST", "/api/chat", OK, entetes={"Origin": "http://piege.example"}), 403),
    ("GET /api/tags avec jeton", lambda: req("GET", "/api/tags"), 200),
    ("POST /api/chat avec jeton (num_ctx borné)", lambda: req("POST", "/api/chat", OK), 200),
]
bons = 0
for nom, f, attendu in cas:
    statut, cors, _ = f()
    ok = statut == attendu and cors is None
    bons += ok
    print(f"{'✅' if ok else '❌'} {nom:45} attendu {attendu}, obtenu {statut}{'' if cors is None else ' (CORS présent !)'}")
# blocage après 10 échecs (les 3 échecs de jeton ci-dessus comptent ; le succès remet à zéro)
for _ in range(10):
    req("POST", "/api/chat", OK, jeton="faux")
statut = req("POST", "/api/chat", OK)[0]
ok = statut == 429
bons += ok
print(f"{'✅' if ok else '❌'} {'blocage après 10 échecs (même avec bon jeton)':45} attendu 429, obtenu {statut}")
print(f"\n{bons}/{len(cas) + 1} conformes")
sys.exit(0 if bons == len(cas) + 1 else 1)
