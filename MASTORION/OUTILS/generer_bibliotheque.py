# -*- coding: utf-8 -*-
"""
generer_bibliotheque.py — MINERVE / agent MASTORION
Construit le classeur XLSX d'import MASTORION (bibliotheque de personas)
a partir des sources MINERVE existantes.

Sources (lecture seule) :
  1. AURIGE 7BB (MINOTAURE 26) : moteur/avatars.js  + Sites/Trombinoscope/bios.js (EHO)
  2. AURIGE 2BB (GUILLAUME)    : WEB/avatars.js     + MASTAURIGE/MEMOIRE.md (registre)
  3. ORION 26 (CASW)           : avatars_casw_ia_usable.md (222 personas, champs complets)

PRIORITE demandee par l'utilisateur (2026-07-27) en cas de conflit sur une fiche
(age, orientation politique/camp, bio...) :   MINOTAURE  >  GUILLAUME  >  ORION 26

Format de sortie = format d'import MASTORION :
  - 1 ONGLET = 1 GROUPE cree automatiquement a l'import (camp)
  - colonne `groups` = groupes additionnels (pays, exercices, faction CASW), separes par ';'
Usage :  python generer_bibliotheque.py
"""
import io, os, re, json, unicodedata
from collections import OrderedDict

EXER = r"D:\CECPC\PRODUCTION\EXER"
MINERVE = r"D:\CECPC\PRODUCTION\IA\MINERVE"
A7_AVA = os.path.join(EXER, r"AURIGE 7BB\00_Boites à outils\MASTAURIGE\LOCALSTORAGE_WEB_VERSION\moteur\avatars.js")
A7_BIO = os.path.join(EXER, r"AURIGE 7BB\00_Boites à outils\MASTAURIGE\LOCALSTORAGE_WEB_VERSION\Sites\Trombinoscope\bios.js")
A2_AVA = os.path.join(EXER, r"AURIGE 2BB\00_Boites à outils\MASTAURIGE\WEB\avatars.js")
CASW = os.path.join(EXER, r"01 ORION 26\01 - O41 - ARCHIVAGE - DOCUMENTS TRIES\01 - ORIGINE WORKING FIELDO41\99-TOOLS\setup\orion26-stobo\avatars_casw_ia_usable.md")
REGISTRE = os.path.join(MINERVE, r"MASTAURIGE\MEMOIRE.md")
SORTIE = os.path.join(MINERVE, r"MASTORION\BIBLIOTHEQUES\BIBLIOTHEQUE_TEST_3_EXERCICES.xlsx")

# Colonnes reconnues par l'import MASTORION (cf. import-users.ts KNOWN_COLS)
COLS = ["masto_id", "username", "display_name", "email", "password", "bio", "groups", "avatar",
        "age", "genre", "pays", "label", "origine", "religion", "situation",
        "caractere", "langage", "activite", "observations", "qualifications", "aime", "deteste"]

CAMP_LABEL = {"rouge": "CAMP ROUGE", "bleu": "CAMP BLEU", "neutre": "CAMP NEUTRE"}


def norm(s):
    s = unicodedata.normalize("NFD", str(s or "")).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]", "", s.lower())


def lire(p):
    return io.open(p, encoding="utf-8", errors="replace").read()


# ---------------------------------------------------------------- avatars.js
def charger_avatars(path):
    """Lit avatars.js. Recupere aussi le COMMENTAIRE curateur qui precede un bloc
    d'avatars (`// ── ... ──`) : il decrit precisement le role du/des persona(s)."""
    raw = lire(path)
    out = []
    commentaire = ""

    def utilisable(txt):
        """Un vrai commentaire descriptif : assez de lettres, pas un separateur."""
        lettres = sum(ch.isalpha() for ch in txt)
        return lettres >= 20 and not re.match(r"^[=\-─\s]+$", txt)

    dans_tableau = False
    for ligne in raw.splitlines():
        if "MASTAURIGE_AVATARS" in ligne:      # debut du tableau : on ignore l'en-tete du fichier
            dans_tableau, commentaire = True, ""
            continue
        if not dans_tableau:
            continue
        c = re.match(r"\s*//\s*[─-]{2,}\s*(.+?)\s*[─-]{2,}\s*$", ligne)
        if c and utilisable(c.group(1)):
            commentaire = re.sub(r"\s+", " ", c.group(1)).strip()
            continue
        c2 = re.match(r"\s*//\s*(\S.{20,})$", ligne)      # commentaire libre (sans tirets)
        if c2 and utilisable(c2.group(1)) and "avatars.js" not in ligne and "handle" not in ligne:
            commentaire = re.sub(r"\s+", " ", c2.group(1)).strip()
            continue
        m = re.search(r'\{\s*handle:\s*"([^"]+)"\s*,\s*nom:\s*"([^"]+)"\s*,\s*camp:\s*"([^"]+)"([^}]*)\}', ligne)
        if m:
            handle, nom, camp, reste = m.groups()
            img = re.search(r'img:\s*"([^"]+)"', reste)
            out.append({"handle": handle, "nom": nom, "camp": camp,
                        "img": img.group(1) if img else "",
                        "note": commentaire})
    return out


# ---------------------------------------------------------------- bios.js (EHO)
def charger_eho(path):
    raw = lire(path)
    s = raw.index("{", raw.index("window.TROMBI_BIOS"))
    d, _ = json.JSONDecoder().raw_decode(raw[s:])
    return d


def composer_bio_eho(fiche, max_len=1500):
    """Assemble les sections narratives de l'EHO en un texte de bio."""
    bio = fiche.get("bio") or {}
    morceaux = []
    for section in ("Parcours", "Objectifs", "Forces", "Faiblesses", "Réseaux sociaux"):
        val = bio.get(section)
        if not val:
            continue
        txt = " ".join(v.strip() for v in (val if isinstance(val, list) else [val]) if v)
        txt = re.sub(r"\s+", " ", txt).strip()
        if txt:
            morceaux.append("%s : %s" % (section, txt))
    texte = " | ".join(morceaux)
    return texte[:max_len].rstrip() + ("..." if len(texte) > max_len else "")


# ---------------------------------------------------------------- CASW ORION 26
def charger_casw(path):
    raw = lire(path)
    blocs = [b for b in re.split(r"\n---\n(?=## )", raw) if b.strip().startswith("## ")]
    out = []
    for b in blocs:
        entete = re.match(r"##\s+(.+?)\s+\(id:\s*(\d+)\)", b.strip())
        if not entete:
            continue
        nom_complet, pid = entete.group(1).strip(), entete.group(2)
        champs = {}
        for m in re.finditer(r"^\|\s*\*{0,2}([^|*]+?)\*{0,2}\s*\|\s*`?([^|`]*?)`?\s*\|\s*$", b, re.M):
            champs[m.group(1).strip().lower()] = m.group(2).strip()
        compte = re.search(r"\|\s*Mastodon\s*\|\s*`?(\d*)`?\s*\|\s*(@[A-Za-z0-9_.]+)\s*\|\s*`?([^|`]*)`?\s*\|\s*([^|]*)\|", b)
        groupes = [g.strip("- ").strip() for g in re.findall(r"^-\s+(.+)$", b, re.M)]
        portrait = re.search(r"\*\*Portrait\s*:\*\*\s*(\S+)", b)
        obs = re.search(r"### Observations\s*\n+(.+?)(?:\n#|\Z)", b, re.S)

        def c(k):
            v = champs.get(k, "")
            return "" if v.lower() in ("none", "n/a", "-") else v

        out.append({
            "persona_id": pid,
            "nom": nom_complet,
            "prenom": c("prénom"), "nom_fam": c("nom"),
            "age": re.sub(r"\D", "", c("âge")),
            "genre": c("genre"), "pays": c("pays"), "label": c("label/faction"),
            "origine": c("origine"), "religion": c("religion"), "situation": c("situation"),
            "caractere": c("caractère"), "langage": c("langage"), "activite": c("activité"),
            "masto_id": compte.group(1) if compte else "",
            "handle": compte.group(2) if compte else "",
            "password": compte.group(3).strip() if compte else "",
            "email": compte.group(4).strip() if compte else "",
            "groupes": [g for g in groupes if g and not g.startswith("**")],
            "avatar": portrait.group(1) if portrait else "",
            "observations": re.sub(r"\s+", " ", obs.group(1)).strip() if obs else "",
        })
    return out


# ------------------------------------------------- registre MASTAURIGE (roles)
def charger_roles_registre(path):
    """Recupere une description de role par handle depuis les tableaux du registre."""
    roles = {}
    for ligne in lire(path).splitlines():
        if not ligne.strip().startswith("| @"):
            continue
        cellules = [c.strip() for c in ligne.strip().strip("|").split("|")]
        handle = cellules[0]
        meilleur = ""
        for cel in cellules[2:]:
            texte = re.sub(r"\*+|`+", "", cel).strip()
            # retire un code d'inject en tete ("07.05.04Ei — ...")
            texte = re.sub(r"^\d{2}\.\d{2}(\.\w+)?\s*[—–-]\s*", "", texte).strip()
            if len(texte) < 30:
                continue
            chiffres = sum(ch.isdigit() for ch in texte)
            if chiffres / max(len(texte), 1) > 0.25:          # liste de codes d'inject
                continue
            if re.match(r"^\d{2}\.\d{2}", texte):             # reste un libelle d'inject
                continue
            if re.search(r"#[0-9A-Fa-f]{6}|font-size|font-weight|background|initiales\s*\"", texte, re.I):
                continue                                       # detail de style, pas une bio
            if len(texte) > len(meilleur):
                meilleur = texte
        if meilleur:
            k = norm(handle)
            if len(meilleur) > len(roles.get(k, "")):
                roles[k] = meilleur
    return roles


# ---------------------------------------------------------------- fusion
def construire():
    a7 = charger_avatars(A7_AVA)
    a2 = charger_avatars(A2_AVA)
    eho = charger_eho(A7_BIO)
    casw = charger_casw(CASW)
    roles = charger_roles_registre(REGISTRE)

    eho_par_nom = {norm(v["nom"]): v for v in eho.values()}
    casw_par_handle = {norm(c["handle"]): c for c in casw if c["handle"]}
    casw_par_nom = {norm(c["nom"]): c for c in casw}

    fiches = OrderedDict()   # cle = norm(handle)

    def ajouter(handle, nom, camp, img, exercice, prio, note=""):
        k = norm(handle)
        f = fiches.get(k)
        if f is None:
            f = {"handle": handle, "nom": nom, "camp": camp, "img": img,
                 "exercices": [], "prio": prio, "note": note}
            fiches[k] = f
        elif prio < f["prio"]:          # priorite plus forte : ecrase identite + camp
            f.update({"handle": handle, "nom": nom, "camp": camp, "img": img, "prio": prio})
            if note:
                f["note"] = note
        elif note and not f.get("note"):
            f["note"] = note
        if exercice not in f["exercices"]:
            f["exercices"].append(exercice)

    # Priorite 1 = MINOTAURE, 2 = GUILLAUME, 3 = ORION 26
    for a in a7:
        ajouter(a["handle"], a["nom"], a["camp"], a["img"], "MINOTAURE 26", 1, a.get("note", ""))
    for a in a2:
        ajouter(a["handle"], a["nom"], a["camp"], a["img"], "GUILLAUME 2BB", 2, a.get("note", ""))
    for c in casw:
        if not c["handle"]:
            continue
        camp = {"rouge": "rouge", "red": "rouge", "bleu": "bleu", "blue": "bleu",
                "gris": "neutre", "grey": "neutre", "gray": "neutre",
                "neutre": "neutre"}.get(c["label"].strip().lower(), "neutre")
        ajouter(c["handle"], c["nom"], camp, "", "ORION 26", 3)

    lignes = []
    stats = {"eho": 0, "note": 0, "casw_bio": 0, "registre": 0, "sans_bio": 0}
    for k, f in fiches.items():
        cw = casw_par_handle.get(k) or casw_par_nom.get(norm(f["nom"])) or {}
        fe = eho_par_nom.get(norm(f["nom"])) or {}

        # --- bio, dans l'ordre de priorite demande :
        #     EHO MINOTAURE > note du registre 7BB (MINOTAURE) > registre MASTAURIGE
        #     (GUILLAUME 2BB) > observations CASW (ORION 26)
        if fe:
            bio, src = composer_bio_eho(fe), "EHO MINOTAURE 26"; stats["eho"] += 1
        elif f.get("note") and "MINOTAURE 26" in f["exercices"]:
            bio, src = f["note"], "registre MINOTAURE 26"; stats["note"] += 1
        elif roles.get(k):
            bio, src = roles[k], "registre MASTAURIGE (GUILLAUME 2BB)"; stats["registre"] += 1
        elif cw.get("observations"):
            bio, src = cw["observations"], "CASW ORION 26"; stats["casw_bio"] += 1
        elif f.get("note"):
            bio, src = f["note"], "registre MASTAURIGE"; stats["registre"] += 1
        else:
            bio, src = "", "aucune"; stats["sans_bio"] += 1

        # --- age : EHO d'abord (priorite MINOTAURE), sinon CASW
        age = re.sub(r"\D", "", fe.get("age", "") or "") or cw.get("age", "") or ""

        groupes = []
        pays = (fe.get("pays") or cw.get("pays") or "").strip()
        if pays:
            groupes.append("PAYS %s" % pays.upper())
        for ex in f["exercices"]:
            groupes.append("EXERCICE %s" % ex)
        if fe.get("groupe"):
            groupes.append(fe["groupe"])
        for g in cw.get("groupes", []):
            groupes.append(g)

        lignes.append({
            "camp": f["camp"],
            "masto_id": cw.get("masto_id", ""),
            "username": f["handle"].lstrip("@"),
            "display_name": f["nom"],
            "email": cw.get("email", "") or "%s@mastorion.local" % norm(f["handle"]),
            "password": cw.get("password", ""),
            "bio": bio,
            "groups": ";".join(OrderedDict.fromkeys(groupes)),
            "avatar": "",                      # portraits non resolus (cf. README)
            "age": age,
            "genre": cw.get("genre", ""),
            "pays": pays,
            "label": cw.get("label", "") or CAMP_LABEL.get(f["camp"], ""),
            "origine": cw.get("origine", ""),
            "religion": cw.get("religion", ""),
            "situation": cw.get("situation", ""),
            "caractere": cw.get("caractere", ""),
            "langage": cw.get("langage", ""),
            "activite": fe.get("role", "") or cw.get("activite", ""),
            "observations": cw.get("observations", "") if src != "CASW ORION 26" else "",
            "qualifications": "Source bio : %s" % src,
            "aime": "", "deteste": "",
        })
    return lignes, stats


def ecrire(lignes):
    from openpyxl import Workbook
    from openpyxl.styles import Font, PatternFill, Alignment
    os.makedirs(os.path.dirname(SORTIE), exist_ok=True)
    wb = Workbook(); wb.remove(wb.active)
    couleur = {"CAMP ROUGE": "C62828", "CAMP BLEU": "1565C0", "CAMP NEUTRE": "616161"}
    for camp in ("rouge", "bleu", "neutre"):
        nom_onglet = CAMP_LABEL[camp]
        ws = wb.create_sheet(nom_onglet)
        ws.append(COLS)
        for c in range(1, len(COLS) + 1):
            cel = ws.cell(row=1, column=c)
            cel.font = Font(bold=True, color="FFFFFF")
            cel.fill = PatternFill("solid", fgColor=couleur[nom_onglet])
            cel.alignment = Alignment(horizontal="center")
        for l in [x for x in lignes if x["camp"] == camp]:
            ws.append([l.get(c, "") for c in COLS])
        ws.freeze_panes = "C2"
        for i, c in enumerate(COLS, 1):
            larg = {"bio": 60, "groups": 38, "display_name": 26, "username": 22,
                    "email": 28, "qualifications": 24, "observations": 30}.get(c, 13)
            ws.column_dimensions[ws.cell(row=1, column=i).column_letter].width = larg
    wb.save(SORTIE)


if __name__ == "__main__":
    lignes, stats = construire()
    ecrire(lignes)
    print("Fichier : %s" % SORTIE)
    print("Personas : %d" % len(lignes))
    for camp in ("rouge", "bleu", "neutre"):
        print("   %-12s %d" % (CAMP_LABEL[camp], sum(1 for l in lignes if l["camp"] == camp)))
    print("Bios — EHO MINOTAURE : %(eho)d | registre MINOTAURE : %(note)d | "
          "registre MASTAURIGE/GUILLAUME : %(registre)d | CASW ORION : %(casw_bio)d | "
          "sans bio : %(sans_bio)d" % stats)
