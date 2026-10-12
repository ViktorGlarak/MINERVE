"""Essai « décideur 26B + rédacteur » sur les vraies invites du moteur (pont/banc_ia).

Le 26B a déjà décidé (resultats_gemma4_26b-a4b-it-qat.json). Pour chaque message qu'il a choisi
d'écrire (réponse, commentaire de partage, publication spontanée), on construit une invite COURTE
(fiche + règles absolues + la publication concernée + l'état de l'avatar + sa décision et sa pensée)
et on fait rédiger le texte seul par chaque modèle passé en argument.

Usage : python3 -I redacteur.py gemma4:26b-a4b-it-qat gemma4:31b-mlx  → redacteur_resultats.json
"""
import json, os, re, sys, time, urllib.request

ici = os.path.dirname(os.path.abspath(__file__))


def appel(modele, systeme, utilisateur):
    corps = {"model": modele, "stream": False, "think": False, "format": "json",
             "options": {"temperature": 0.8, "num_ctx": 8192},
             "messages": [{"role": "system", "content": systeme}, {"role": "user", "content": utilisateur}]}
    req = urllib.request.Request("http://localhost:11434/api/chat", json.dumps(corps).encode(), {"Content-Type": "application/json"})
    t = time.time(); r = json.load(urllib.request.urlopen(req, timeout=900))
    try: texte = json.loads(r["message"]["content"]).get("texte", "")
    except Exception: texte = "ILLISIBLE : " + r["message"]["content"][:200]
    return round(time.time() - t, 1), r.get("prompt_eval_count"), r.get("eval_count"), texte


def systeme_court(sys_long):
    """Fiche + situation + exemples + règles ABSOLUES seulement (sans les règles de décision ni le format)."""
    avant, _, regles = sys_long.partition("RÈGLES ABSOLUES :")
    absolues = []
    for ligne in regles.split("\n"):
        if ligne.startswith("- Elle ne réagit PAS") or ligne.startswith("- Il ne réagit PAS") or ligne.startswith("FORMAT"):
            break
        absolues.append(ligne)
    return avant + "RÈGLES ABSOLUES :" + "\n".join(absolues).rstrip() + "\n- Ne recopie pas les exemples ; varie les émojis et les tournures."


def bloc_publication(user, n):
    m = re.search(rf"\n{n}\) Publication de .*?(?=\n\d+\) Publication de |\nTON ÉTAT :)", user, re.S)
    return m.group(0).strip() if m else ""


CONSIGNE = {
    "repondre": "Tu as décidé de RÉPONDRE en commentaire à cette publication.",
    "partager": "Tu as décidé de PARTAGER cette publication à tes abonnés, avec un mot d'accompagnement.",
    "publication": "Tu as décidé de PUBLIER un message spontané de toi-même.",
}


def invite_utilisateur(user, cas):
    moment = user.split("\n", 1)[0]
    etat = "TON ÉTAT :" + user.split("TON ÉTAT :", 1)[1].rsplit("\nQue fait ", 1)[0]
    lu = bloc_publication(user, cas["n"]) if cas["n"] else ""
    lu = f"CE QUE TU VIENS DE LIRE :\n{lu}\n\n" if lu else ""
    return (f"{moment}\n\n{lu}{etat.strip()}\n\n"
            f"TA DÉCISION : {CONSIGNE[cas['action']]}\nCe que tu en penses vraiment : « {cas['pensee']} »\n\n"
            "Écris maintenant ce texte, et seulement lui : naturel, à ta façon, 280 caractères au plus, "
            "sans recopier ta pensée mot pour mot. Réponds UNIQUEMENT par un objet JSON : {\"texte\": \"<ton message>\"}")


cas_tous = []
for res in json.load(open(os.path.join(ici, "resultats_gemma4_26b-a4b-it-qat.json"))):
    if res["type"] not in ("lecture", "publication"):
        continue
    d = json.load(open(os.path.join(ici, res["fichier"])))
    sys_long, user = d["messages"][0]["content"], d["messages"][1]["content"]
    j = json.loads(res["reponse"])
    for r in j.get("reactions", []):
        if r.get("action") in ("repondre", "partager") and (r.get("texte") or r.get("commentaire")):
            cas_tous.append({"fichier": res["fichier"], "n": r["n"], "action": r["action"], "pensee": r.get("pensee", ""),
                             "v1_26b_un_appel": r.get("texte") or r.get("commentaire"), "sys": sys_long, "user": user})
    p = j.get("publication")
    if p and p.get("texte"):
        cas_tous.append({"fichier": res["fichier"], "n": p.get("source") or 0, "action": "publication", "pensee": p.get("pensee", ""),
                         "v1_26b_un_appel": p["texte"], "sys": sys_long, "user": user})

for cas in cas_tous:
    cas["invite_sys"], cas["invite_user"] = systeme_court(cas.pop("sys")), invite_utilisateur(cas.pop("user"), cas)

for modele in sys.argv[1:]:
    appel(modele, "Réponds ok.", "ok")  # chargement
    for cas in cas_tous:
        duree, ji, jr, texte = appel(modele, cas["invite_sys"], cas["invite_user"])
        cas[modele] = {"duree_s": duree, "jetons_invite": ji, "jetons_reponse": jr, "texte": texte}
        print(f"{modele:24} {cas['fichier'][:30]:30} n={cas['n']} {cas['action']:11} {duree:5.1f} s ({ji} → {jr} jetons)", flush=True)
    urllib.request.urlopen(urllib.request.Request("http://localhost:11434/api/generate", json.dumps({"model": modele, "keep_alive": 0}).encode()))

json.dump(cas_tous, open(os.path.join(ici, "redacteur_resultats.json"), "w"), ensure_ascii=False, indent=1)
