# -*- coding: utf-8 -*-
# ============================================================
#  generer_etat_exercice.py — Carte de référence de l'exercice MINOTAURE 7BB
#  -----------------------------------------------------------
#  MINAUTORE = référent de l'exercice : il doit TOUT maîtriser
#  (quel inject joue quand, quelle storyline, quel persona, quelle LO).
#  Ce script LIT les données réelles de l'instance de travail (collab)
#  et REGENERE  MINAUTORE/ETAT_EXERCICE_7BB.md  → toujours à jour.
#
#  À relancer après TOUTE modification de l'exercice (dates, injects,
#  personas, renumérotation…) :  py MINAUTORE/generer_etat_exercice.py
# ============================================================
import json, re, os, sys, datetime
try: sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception: pass

COLLAB = r"D:/CECPC/PRODUCTION/EXER/AURIGE 7BB/00_Boites à outils/MASTAURIGE/SERVEUR_COLLABORATIF/mastaurige"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ETAT_EXERCICE_7BB.md")

# Calendrier de jeu (GELEX = 29 juin, sans D+)
ISO2D = {"2026-06-21":31,"2026-06-22":32,"2026-06-23":33,"2026-06-24":34,"2026-06-25":35,
         "2026-06-26":36,"2026-06-27":37,"2026-06-28":38,"2026-06-30":39,"2026-07-01":40,"2026-07-02":41}
D2LABEL = {31:"21 juin",32:"22 juin",33:"23 juin",34:"24 juin",35:"25 juin",36:"26 juin",
           37:"27 juin",38:"28 juin",39:"30 juin",40:"01 juil.",41:"02 juil."}
PHASES = {31:"CONVEX",32:"CONVEX",33:"WU TECH",34:"WU TECH",35:"WU TAC",36:"WU TAC",
          37:"CAX 1",38:"CAX 1",39:"CAX 2",40:"CAX 2",41:"CAX 2"}

def jsarr(path):
    t = open(path, encoding="utf-8").read()
    m = re.search(r"=\s*(\[.*\])\s*;?\s*$", t, re.S)
    return json.loads(m.group(1)) if m else []

def lo_cfg():
    t = open(os.path.join(COLLAB, "moteur/lo_config.js"), encoding="utf-8").read()
    return json.loads(re.search(r"storylines:\s*(\{.*?\}\})", t, re.S).group(1))

def d_of_dayorder(v):
    try: return int(v)
    except: return None

def d_of_isodate(s):
    return ISO2D.get((s or "")[:10])

# ---- socle (cards JEMM) ----
def socle_cards():
    t = open(os.path.join(COLLAB, "MELMIL/melmil_data.js"), encoding="utf-8").read()
    m = re.search(r"=\s*(\{.*\})\s*;?\s*$", t, re.S)
    return json.loads(m.group(1)).get("injections", []) if m else []
socle = socle_cards()
cards = {}
for c in socle:
    code = c.get("code")
    if not code: continue
    cards[code] = {"sujet": c.get("sujet",""), "d": d_of_isodate(c.get("date")), "etat": c.get("etat","")}

# ---- bakés (tweets + articles) ----
baked = {}
for o in jsarr(os.path.join(COLLAB, "moteur/tweets_data.js")):
    num = o.get("num")
    if num: baked.setdefault(num, []).append(("tweet", o.get("handle") or o.get("nom") or "?", d_of_dayorder(o.get("dayorder")), (o.get("text") or "")[:50], (o.get("lo") or [""])[0]))
for o in jsarr(os.path.join(COLLAB, "moteur/articles_data.js")):
    num = o.get("num")
    if num: baked.setdefault(num, []).append((o.get("type") or "article", (o.get("site") or "?").upper(), d_of_dayorder(o.get("dayorder")), (o.get("title") or o.get("deck") or "")[:50], (o.get("lo") or [""])[0]))

SL = lo_cfg()
def storyline_of(code):
    sl = ".".join(code.split(".")[:2])  # 07.11.I02 -> 07.11
    return sl, SL.get(sl, {})

# ---- toutes les entrées (union codes socle + bakés) ----
allcodes = sorted(set(list(cards) + list(baked)))
rows = []
for code in allcodes:
    sl, meta = storyline_of(code)
    d = cards.get(code, {}).get("d")
    if d is None:
        for it in baked.get(code, []):
            if it[2] is not None: d = it[2]; break
    rows.append((code, sl, meta.get("lo",""), d, cards.get(code,{}), baked.get(code, [])))

now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
L = []
L.append("# 🗺️ ÉTAT DE L'EXERCICE — MINOTAURE 26 / AURIGE 7BB")
L.append("")
L.append(f"> ⚙️ **FICHIER GÉNÉRÉ** par `MINAUTORE/generer_etat_exercice.py` — ne pas éditer à la main.")
L.append(f"> Carte de référence de MINAUTORE (référent de l'exercice). Régénéré le **{now}**.")
L.append(f"> Source = instance de travail collab (`melmil_data.js` socle + `tweets_data.js`/`articles_data.js` bakés).")
L.append("> Détail doctrinal / narratif : `MINAUTORE/MEMOIRE.md`.")
L.append("")
L.append("## 📅 Calendrier de jeu (D+ ↔ date ↔ phase)")
L.append("| D+ | Date | Phase | DOW |")
L.append("|---|---|---|---|")
DOW = {31:"DIM",32:"LUN",33:"MAR",34:"MER",35:"JEU",36:"VEN",37:"SAM",38:"DIM",39:"MAR",40:"MER",41:"JEU"}
for d in range(31,42):
    L.append(f"| D+{d} | {D2LABEL[d]} | {PHASES[d]} | {DOW[d]} |")
L.append("> ⚠ **GELEX = 29 juin** (gel/évaluation, sans D+, entre D+38 et D+39).")
L.append("")
L.append("## 🎭 Storylines (07.xx) → LO")
L.append("| Storyline | LO | Nom |")
L.append("|---|---|---|")
for sl in sorted(SL):
    L.append(f"| {sl} | LO{SL[sl]['lo']} | {SL[sl]['name']} |")
L.append("| 08.01 | HN | Autorités civiles ARN |")
L.append("| 08.02 | HN | Gestion des CPERS |")
L.append("")
L.append("## 🗂️ Registre complet des injects (code · D+ · LO · type · persona/média · sujet)")
L.append("| Code | D+ | LO | Contenu MASTAURIGE (type · persona · extrait) | Socle (sujet · état) |")
L.append("|---|---|---|---|---|")
for code, sl, lo, d, card, items in rows:
    dlabel = f"D+{d}" if d else "—"
    lol = f"LO{lo}" if lo else ("HN" if sl.startswith("08") else "—")
    bk = "<br>".join(f"{t} · {who} · {sn}" for (t,who,dd,sn,llo) in items) if items else "—"
    sc = (card.get("sujet","")[:45] + (f" · {card.get('etat')}" if card.get('etat') else "")) if card else "—"
    L.append(f"| {code} | {dlabel} | {lol} | {bk} | {sc or '—'} |")
L.append("")
L.append("## 📆 Vue par jour (injects bakés MASTAURIGE)")
byday = {}
for code, sl, lo, d, card, items in rows:
    for (t,who,dd,sn,llo) in items:
        if dd: byday.setdefault(dd, []).append(f"{code} ({t} {who})")
for d in range(31,42):
    lst = byday.get(d, [])
    L.append(f"- **D+{d} ({D2LABEL[d]}, {PHASES[d]})** : " + (" · ".join(lst) if lst else "—"))
L.append("")
open(OUT, "w", encoding="utf-8").write("\n".join(L))
print("Généré :", OUT)
print(f"  {len(allcodes)} codes · {sum(len(b) for b in baked.values())} injects bakés · {len(cards)} cards socle")
