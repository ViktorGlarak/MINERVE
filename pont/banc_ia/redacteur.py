"""Essai « décideur 26B + rédacteur » sur les vraies invites du moteur (pont/banc_ia).

Le 26B a déjà décidé (resultats_gemma4_26b-a4b-it-qat.json). Pour chaque message qu'il a choisi
d'écrire (réponse, commentaire de partage, publication spontanée), on construit une invite COURTE
(fiche + règles absolues + la publication concernée + l'état de l'avatar + sa décision et sa pensée)
et on fait rédiger le texte seul par chaque modèle passé en argument.

Usage : python3 -I redacteur.py [--v2] gemma4:26b-a4b-it-qat gemma4:31b-mlx  → redacteur_resultats[_v2].json
--v2 (2026-10-12, après le 1er essai) : longueur cible selon la disponibilité, règles de réalisme remises,
interdiction d'inventer, souvenirs sous la publication limités à 2 (invite plus courte).
"""
import json, os, re, sys, time, urllib.request

ici = os.path.dirname(os.path.abspath(__file__))
V3 = "--v3" in sys.argv
V2 = "--v2" in sys.argv or V3
if V3:
    sys.path.insert(0, ici)
    import emotions
MODELES = [a for a in sys.argv[1:] if not a.startswith("--")]


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
    court = avant + "RÈGLES ABSOLUES :" + "\n".join(absolues).rstrip() + "\n- Ne recopie pas les exemples ; varie les émojis et les tournures."
    if V2:
        court += ("\n\nRÉALISME :\n- Une vraie personne écrit court, surtout quand elle est occupée. Pas de formule d'encouragement générique "
                  "(« Bravo pour l'initiative », « Courage à tous », « On lâche rien »).\n- Respecte ton registre et ton nombre d'émojis habituel (voir tes exemples).\n"
                  "- N'invente AUCUN lieu, métier, proche, activité ou fait qui ne figure pas dans ta fiche, dans TA VIE ou dans ce que tu viens de lire.\n"
                  "- Si tu parles de ce que tu fais en ce moment, ça doit coller à ton métier et à l'heure.")
    return court


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
    if V2 and lu:  # au plus 2 souvenirs sous la publication
        tete, sep, souv = lu.partition("Ce que tu as déjà vu ou dit sur ce sujet :")
        lu = tete + sep + "\n" + "\n".join(souv.strip().split("\n")[:2]) if sep else lu
    lu = f"CE QUE TU VIENS DE LIRE :\n{lu}\n\n" if lu else ""
    return (f"{moment}\n\n{lu}{etat.strip()}\n\n"
            f"TA DÉCISION : {CONSIGNE[cas['action']]}\nCe que tu en penses vraiment : « {cas['pensee']} »\n\n"
            + (("LONGUEUR : " + ("tu es au travail ou occupé(e) : UNE phrase courte, 120 caractères au plus, 0 ou 1 émoji. "
                if ("au travail" in moment or "occup" in moment) else "une ou deux phrases, 200 caractères au plus. ")) if V2 else "")
            + "Écris maintenant ce texte, et seulement lui : naturel, à ta façon, " + ("" if V2 else "280 caractères au plus, ") +
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
                             "v1_26b_un_appel": r.get("texte") or r.get("commentaire"), "sys": sys_long, "user": user, "reaction": r})
    p = j.get("publication")
    if p and p.get("texte"):
        cas_tous.append({"fichier": res["fichier"], "n": p.get("source") or 0, "action": "publication", "pensee": p.get("pensee", ""),
                         "v1_26b_un_appel": p["texte"], "sys": sys_long, "user": user, "reaction": None})

deja_par_avatar = {}
for cas in cas_tous:
    cas["invite_sys"], cas["invite_user"] = systeme_court(cas.pop("sys")), invite_utilisateur(cas.pop("user"), cas)
    reaction = cas.pop("reaction")
    if V3:
        humeur = re.search(r"Ton humeur du moment : ([^\n]*)", cas["invite_user"])
        n, raison = emotions.choisir(reaction, humeur.group(1) if humeur else "", cas["invite_sys"], cas["fichier"], cas["n"],
                                     deja_par_avatar.get(cas["fichier"], [])[-2:])
        deja_par_avatar.setdefault(cas["fichier"], []).append(n["id"])
        cas["emotion_decideur"] = (reaction or {}).get("emotion", "(publication)")
        cas["nuance"], cas["raison"] = n["id"], raison
        cas["invite_user"] = cas["invite_user"].replace("LONGUEUR :", emotions.consigne(n) + "\n\nLONGUEUR :", 1)

for modele in MODELES:
    appel(modele, "Réponds ok.", "ok")  # chargement
    for cas in cas_tous:
        duree, ji, jr, texte = appel(modele, cas["invite_sys"], cas["invite_user"])
        cas[modele] = {"duree_s": duree, "jetons_invite": ji, "jetons_reponse": jr, "texte": texte}
        print(f"{modele:24} {cas['fichier'][:30]:30} n={cas['n']} {cas['action']:11} {duree:5.1f} s ({ji} → {jr} jetons)", flush=True)
    urllib.request.urlopen(urllib.request.Request("http://localhost:11434/api/generate", json.dumps({"model": modele, "keep_alive": 0}).encode()))

json.dump(cas_tous, open(os.path.join(ici, "redacteur_resultats_v3.json" if V3 else "redacteur_resultats_v2.json" if V2 else "redacteur_resultats.json"), "w"), ensure_ascii=False, indent=1)
