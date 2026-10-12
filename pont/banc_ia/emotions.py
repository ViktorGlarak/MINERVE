"""Choix d'une nuance du dictionnaire des émotions (PSYCHOLOGUE/DICTIONNAIRE_EMOTIONS.json, règles 1 à 5).
Prototype pour le banc ; le portage dans app-ia reviendra à PLEIADE."""
import hashlib, json, os, re

ici = os.path.dirname(os.path.abspath(__file__))
D = json.load(open(os.path.join(ici, "..", "..", "PSYCHOLOGUE", "DICTIONNAIRE_EMOTIONS.json"), encoding="utf-8"))
PAR_ID = {n["id"]: n for n in D["nuances"]}


def _tirage(*cles):  # déterministe, entre 0 et 1 (rejouable)
    return int(hashlib.sha256("|".join(map(str, cles)).encode()).hexdigest()[:8], 16) / 0xFFFFFFFF


def temperament(invite_sys):
    # Caractère + métier seulement : la ligne « Tempérament » est standard (« ni crédule ni méfiant ») et fausserait les affinités
    t = " ".join(m.group(1) for m in re.finditer(r"(?:Caractère|Activité) : ([^\n]*)", invite_sys)).lower()
    return t


def famille_depuis(reaction, humeur):
    """Famille d'émotion : celle du décideur pour une réaction ; d'après l'humeur pour une publication spontanée."""
    if reaction:
        return reaction.get("emotion") or "neutre", int(reaction.get("intensite") or 1)
    h = humeur.lower()
    for mot, fam in (("colère", "colere"), ("à cran", "colere"), ("peur", "peur"), ("inquiet", "peur"),
                     ("triste", "tristesse"), ("abattu", "tristesse"), ("bonne humeur", "joie"), ("content", "joie")):
        if mot in h:
            return fam, 1
    return "neutre", 1


def choisir(reaction, humeur, invite_sys, avatar, cle, deja=()):
    fam, inten = famille_depuis(reaction, humeur)
    temp = temperament(invite_sys)
    # règle 5 : le ressenti du décideur corrige la famille
    if reaction:
        fond, forme = reaction.get("ressenti_fond"), reaction.get("ressenti_forme")
        if fond == "doute" or (fond == "d_accord" and any(m in temp for m in ("sceptique", "râleu", "méfian", "prudent"))):
            if fam in ("joie", "tendresse", "fierte"):
                return PAR_ID["approbation_reservee"], "règle 5 (accord avec réserve)"
        if forme in ("mefiante", "en_desaccord"):
            return PAR_ID["mepris" if any(m in temp for m in ("moqu", "direct", "fier")) else "mefiance"], "règle 5 (méfiance)"
    # règle 3 : émotion secondaire selon le tempérament
    for s in D["secondaires"]:
        if fam in s["primaire"] and any(m in temp for m in s["si_temperament"]) and _tirage(avatar, cle, "sec") < s["proba"]:
            cands = [PAR_ID[i] for i in s["devient"] if i not in deja] or [PAR_ID[i] for i in s["devient"]]
            return cands[int(_tirage(avatar, cle, "s2") * len(cands))], "règle 3 (secondaire : " + s["pourquoi"] + ")"
    # règles 1, 2, 4 : famille, intensité la plus proche, affinités, rotation
    cands = [n for n in D["nuances"] if n["famille"] == fam and "contexte" not in n] or [PAR_ID["constat"]]  # règle 2bis
    if fam == "neutre" and not reaction:  # publication spontanée sans humeur marquée : nuances du quotidien
        cands = [PAR_ID[i] for i in ("constat", "contentement", "lassitude", "inquietude", "amusement", "melancolie", "fierte_personnelle")]
    ecart = min(abs(n["intensite"] - inten) for n in cands)
    cands = [n for n in cands if abs(n["intensite"] - inten) == ecart]
    cands = [n for n in cands if n["id"] not in deja] or cands
    poids = [2 if any(a in temp for a in n["affinites"]) else 1 for n in cands]
    x, cumul = _tirage(avatar, cle, "n") * sum(poids), 0
    for n, p in zip(cands, poids):
        cumul += p
        if x <= cumul:
            return n, "règles 1-2-4 (famille " + fam + ", intensité " + str(inten) + ")"
    return cands[-1], "règles 1-2-4"


def consigne(n):
    return (f"TON ÉMOTION, à faire SENTIR sans la nommer : {n['id'].replace('_', ' ')} — {n['def']}.\n"
            f"Ça se voit à : {' ; '.join(n['ecrit'][:3])}.\n"
            f"À éviter : {' ; '.join(n['eviter'])}.")
