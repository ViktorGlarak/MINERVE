"""Modèle eho « TUTO PLÉIADE » : ~100 avatars tirés du modèle intégré SKOLKAN PERSONA 21.09.26
(politiques, militaires, médias, autorités, institutions, société civile ; Mercure, Arnland, Bothnia, France,
international). Même format qu'un modèle eho : manifest.json + payload.json + portraits/."""
import json, os, shutil, collections, pathlib, datetime
SRC = pathlib.Path(r"C:\CECPC\pleiade\eho\modeles\skolkan-persona-21-09-26")
DST = pathlib.Path(r"D:\CECPC\PRODUCTION\IA\MINERVE\PLEIADE\GUIDE\DONNEES\modele-tuto-pleiade")
p = json.load(open(SRC / "payload.json", encoding="utf-8"))
U = p["users"]
pays = lambda u: (u.get("pays") or "").strip().capitalize() or "International"
lab = lambda u: (u.get("label") or "").strip().upper()
def score(u):  # portrait d'abord, puis fiche la plus fournie
    texte = sum(len(str(u.get(k) or "")) for k in ("bio", "qualifications", "observations", "activite", "caractere"))
    return (bool(u.get("avatar_url")), bool(u.get("bio")), texte)

# ⛔ Règle « jamais de personne ni d'organisation RÉELLE incarnée » : écartés même s'ils sont dans le modèle source.
EXCLUS = {"markrutte", "antonioguterres", "IAEA_AIEA_off", "Amnesty_International", "UNHCR_off", "UNOCHA_off",
          "compteofficielCICR", "boriskalugintatianavelkova", "arn_kalugin"}
QUOTAS = [  # (pays, label, nombre)
    ("Mercure", "POLITICIEN", 8), ("Arnland", "POLITICIEN", 8), ("Bothnia", "POLITICIEN", 9),
    ("Mercure", "MILITAIRE", 14), ("Arnland", "MILITAIRE", 10), ("Bothnia", "MILITAIRE", 6), ("France", "MILITAIRE", 8),
    ("France", "JOURNALISTE", 5), ("Arnland", "JOURNALISTE", 4), ("Mercure", "JOURNALISTE", 3), ("Bothnia", "JOURNALISTE", 2),
    ("International", "MEDIA INTERNATIONAL", 2),
    ("Arnland", "AUTORITE LOCALE", 6), ("International", "INSTITUTION INTERNATIONALE", 5), ("International", "UE", 1),
    ("Arnland", "CITOYEN", 2), ("Mercure", "INFLUENCEUR", 2), ("Arnland", "INFLUENCEUR", 1),
    ("Bothnia", "OPPOSITION", 2), ("Mercure", "OPPOSITION", 1), ("Arnland", "ONG", 1),
    ("Arnland", "JUSTICE", 1), ("Bothnia", "RELIGIEUX", 1),
]
choisis = []
for pa, la, n in QUOTAS:
    cand = sorted([u for u in U if pays(u) == pa and lab(u) == la and u["username"] not in EXCLUS], key=score, reverse=True)
    if len(cand) < n: print(f"⚠ {pa}/{la} : {len(cand)} disponibles pour {n} demandés")
    choisis += cand[:n]

# Groupes : on retire les marques d'exercices passés, on pose la marque du tutoriel.
TUTO = "EXERCICE TUTORIEL PLEIADE"
sortie = []
for u in choisis:
    v = dict(u)
    v["groups"] = [g for g in u["groups"] if not g.startswith("EXERCICE ")] + [TUTO]
    sortie.append(v)
utilises = {g for u in sortie for g in u["groups"]}
groupes = [g for g in p["groups"] if g["name"] in utilises]
groupes.append({"name": TUTO, "color": "#6364ff", "description": "Population du tutoriel guidé PLÉIADE (zone d'entraînement)."})

# Planche : seulement les avatars retenus et les liens entre eux.
ids = {u["id"] for u in sortie}
noeuds = [dict(n, parent=None) for n in p["graphe"]["noeuds"] if n.get("type") == "avatar" and n["id"] in ids]
for n in noeuds: n.pop("parent", None)
liens = [l for l in p["graphe"]["liens"] if l.get("source") in ids and l.get("cible", l.get("target")) in ids]

if DST.exists(): shutil.rmtree(DST)
(DST / "portraits").mkdir(parents=True)
for u in sortie:
    a = u.get("avatar_url") or ""
    if a.startswith("/api/uploads/"):
        shutil.copy2(SRC / "portraits" / a.rsplit("/", 1)[1], DST / "portraits")
json.dump({"graphe": {"noeuds": noeuds, "liens": liens}, "users": sortie, "groups": groupes},
          open(DST / "payload.json", "w", encoding="utf-8"), ensure_ascii=False)
json.dump({"code": "TUTO-PLEIADE", "name": "TUTO PLÉIADE",
           "description": f"Population du tutoriel guidé PLÉIADE : {len(sortie)} avatars Skolkan tirés de SKOLKAN PERSONA 21.09.26 (politiques, militaires, médias, autorités, institutions, société civile — Mercure, Arnland, Bothnia, France, international).",
           "created_at": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
           "counts": {"users": len(sortie), "groups": len(groupes)}},
          open(DST / "manifest.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)

# Récapitulatif lisible pour l'utilisateur
camp = lambda u: next((g.replace("CAMP ", "") for g in u["groups"] if g.startswith("CAMP ")), "?")
lignes = ["| Pays | Catégorie | Nb | Avec portrait |", "|---|---|---|---|"]
for pa, la, n in QUOTAS:
    s = [u for u in sortie if pays(u) == pa and lab(u) == la]
    lignes.append(f"| {pa} | {la.capitalize()} | {len(s)} | {sum(1 for u in s if u.get('avatar_url'))} |")
liste = ["| Identifiant | Nom affiché | Pays | Catégorie | Camp |", "|---|---|---|---|---|"]
liste += [f"| {u['username']} | {u['display_name']} | {pays(u)} | {lab(u).capitalize()} | {camp(u)} |" for u in sortie]
(DST.parent / "SELECTION_AVATARS.md").write_text(
    "# Sélection d'avatars — tutoriel PLÉIADE\n\n"
    f"Source : modèle eho intégré **SKOLKAN PERSONA 21.09.26**. Modèle produit : `modele-tuto-pleiade/` (code `TUTO-PLEIADE`). "
    f"{len(sortie)} avatars, {sum(1 for u in sortie if u.get('avatar_url'))} avec portrait, {len(groupes)} groupes, "
    f"{len(liens)} liens de planche conservés. Camps : " + ", ".join(f"{k} {v}" for k, v in collections.Counter(camp(u) for u in sortie).items()) +
    ".\n\n> Camps lus dans le modèle eho ; le registre MASTAURIGE fait foi en cas de doute.\n\n## Répartition\n\n" + "\n".join(lignes) +
    "\n\n## Liste\n\n" + "\n".join(liste) + "\n", encoding="utf-8")
print(len(sortie), "avatars ;", sum(1 for u in sortie if u.get("avatar_url")), "portraits ;", len(groupes), "groupes ;", len(liens), "liens")
print(collections.Counter(camp(u) for u in sortie))
