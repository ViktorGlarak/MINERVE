"""
Génère deux exports JEMM FICTIFS (Event 06 ILI, Event 08 GREY CELL) à partir de
« 20260909 - GREY CELL_MAIN v4.pptx » (exercice DELATTRE 26).

Pourquoi un générateur plutôt qu'un fichier écrit à la main : le PPT va encore
bouger ; relancer ce script refait les deux JSON à l'identique.

Règles validées par l'utilisateur le 2026-09-23 :
  - Source = pages 3 à 10 SEULEMENT (numérotation du tableau des pages 1-2).
    Les pages 11 à 21 (ancienne numérotation 08.06, 08.07, 08.08, 08.10…) sont
    des brouillons et ne sont pas importées.
  - Un incident répété sur plusieurs jours = UN inject par jour.
  - Pas d'heure dans le PPT = 09h00. Les 3 incidents 08.02 (sans jour) sont
    répartis sur les jours de ses barres en page 2 : D+27, D+28, D+31.
  - Narratifs 06.02 et 08.03 : chaque « CRQ » (09h00 / 15h00) = un inject distinct.
  - Codes au format JEMM « EE.SS.Inn » ; le code d'origine du PPT est rappelé
    dans la description de chaque inject.

Calendrier (page 2) : D+27 = mardi 06/10/2026 … D+41 = mardi 20/10/2026.

Usage :  python generer_jemm_greycell.py
"""
import base64
import datetime as dt
import json
import os
import re
import uuid

from pptx import Presentation

PPTX = r"D:\CECPC\PRODUCTION\EXER\DELATTRE 26\01_Montage exercice\20260909 - GREY CELL_MAIN v4.pptx"
SORTIE = r"D:\CECPC\PRODUCTION\EXER\DELATTRE 26\01_Montage exercice\JEMM"

D27 = dt.date(2026, 10, 6)  # page 2 : D+27 = MAR 06/10


def jour(dplus: int) -> dt.date:
    return D27 + dt.timedelta(days=dplus - 27)


def iso(d: dt.date, h: int = 9, m: int = 0) -> str:
    return f"{d.isoformat()}T{h:02d}:{m:02d}:00"


# Identifiants stables : relancer le script donne les mêmes Id (JEMM les garde d'un export à l'autre).
NS = uuid.UUID("5d3c1b8e-7a2f-4c11-9e0a-0000000d1726")


def uid(*parts: str) -> str:
    return str(uuid.uuid5(NS, "|".join(parts)))


def propre(t: str) -> str:
    t = t.replace("\u00a0", " ").replace("\x0b", "\n")
    t = re.sub(r"[ \t]+", " ", t)
    t = re.sub(r"\s*/\s*$", "", t.strip())
    return t.strip()


def sans_jours(t: str) -> str:
    """Le libellé sans ses mentions de jours (« D+36;D+37 », « D+28 – »), pour le nom de l'inject."""
    t = re.sub(r"\(?\s*D\+\d+[^A-Za-zÀ-ÿ]*?(?:,|;|et)?\s*", " ", t)
    t = re.sub(r"\bIVO\b", "", t)
    t = re.sub(r"\s*[–-]\s*$", "", t)
    t = re.sub(r"\s{2,}", " ", t).strip(" .,;–-")
    return t


def nom_court(t: str, n: int = 110) -> str:
    t = sans_jours(t).replace("\n", " ")
    return t if len(t) <= n else t[: n - 1].rstrip() + "…"


# --------------------------------------------------------------------------- lecture du PPT

prs = Presentation(PPTX)
slides = list(prs.slides)


def tables(i: int):
    return [sh.table for sh in slides[i - 1].shapes if sh.has_table]


def textes(i: int):
    return [sh.text_frame.text for sh in slides[i - 1].shapes if getattr(sh, "has_text_frame", False) and sh.text_frame.text.strip()]


def bloc(i: int, entete: str) -> str:
    """Le texte d'un encadré de la diapositive, sans son titre (« DESCRIPTION… », « EFFET… »)."""
    for t in textes(i):
        if t.strip().upper().startswith(entete):
            lignes = t.replace("\x0b", "\n").split("\n")
            corps = [l for l in lignes[1:] if l.strip() and not l.strip().upper().startswith("(STORY LINE)")]
            return propre("\n".join(corps))
    return ""


def lignes_injects(i: int):
    """Les lignes « code | texte » du tableau INJECTS d'une diapositive."""
    for t in tables(i):
        if t.cell(0, 0).text.strip().upper() == "INJECTS":
            for r in list(t.rows)[1:]:
                code, txt = propre(r.cells[0].text), propre(r.cells[1].text)
                if txt:
                    yield code, txt


def narratifs(i: int):
    """Les lignes du tableau NARRATIFS (06.02, 08.03)."""
    for t in tables(i):
        if t.cell(0, 0).text.strip().upper() == "NARRATIFS":
            for r in list(t.rows)[1:]:
                c = [propre(x.text) for x in r.cells]
                yield {"qui_ligne": c[0], "narratif": c[1], "quand": c[2], "qui": c[3], "par_qui": c[4], "quoi": c[5]}


def coordination(i: int) -> list[str]:
    for t in tables(i):
        if t.cell(0, 0).text.strip().upper().startswith("EXCON"):
            return [propre(c.text) for c in t.rows[1].cells if propre(c.text)]
    return []


def quand_ou_qui(i: int) -> dict:
    for t in tables(i):
        if t.cell(0, 0).text.strip().upper() == "QUOI":
            return {propre(r.cells[0].text).upper(): propre(r.cells[1].text) for r in t.rows}
    return {}


# Coordination de la page 1 (colonne COORDINATION du tableau des storylines)
COORD_P1 = {}
for t in tables(1):
    for r in list(t.rows)[1:]:
        code = re.match(r"\d{2}\.\d{2}", propre(r.cells[0].text))
        if code:
            COORD_P1[code.group(0)] = propre(r.cells[1].text)

# --------------------------------------------------------------------------- les storylines

# Nom, période (page 2), diapositives sources, destinataire par défaut
STORYLINES = {
    "06.01": dict(event="06", nom="Signaux faibles captés par les ETIM", debut=33, fin=40, slides=[3, 4]),
    "06.02": dict(event="06", nom="Rumeurs contre la FORCE", debut=27, fin=39, slides=[5]),
    "08.01": dict(event="08", nom="Dégradation des services essentiels de la nation hôte (STARTEX)", debut=27, fin=39, slides=[6]),
    "08.02": dict(event="08", nom="Risques sur les sites sensibles", debut=27, fin=32, slides=[7]),
    "08.03": dict(event="08", nom="Actions perfides", debut=27, fin=40, slides=[8]),
    "08.04": dict(event="08", nom="Mouvements de populations", debut=27, fin=40, slides=[9]),
    "08.05": dict(event="08", nom="Sécurisation des IDPs et appui à la HN", debut=29, fin=40, slides=[10]),
}

EVENTS = {
    "06": dict(nom="ILI", description="DE LATTRE 26 — Event 06 ILI (storylines 06.01, 06.02)"),
    "08": dict(nom="GREY CELL", description="DE LATTRE 26 — Event 08 GREY CELL (storylines 08.01 à 08.05)"),
}

# Jours d'occurrence des incidents, lus dans leurs libellés (une entrée par jour).
# 06.01.08 n'a aucun jour dans le PPT : placé au premier jour de la storyline (D+33) — À CONFIRMER.
JOURS_0601 = {
    "06.01.01": [33, 35, 36, 37], "06.01.02": [38], "06.01.03": [37], "06.01.04": [36, 37],
    "06.01.05": [37, 38], "06.01.06": [36, 38, 39], "06.01.07": [38, 39], "06.01.08": [33],
    "06.01.09": [36, 37], "06.01.10": [37, 38, 39], "06.01.11": [38],
}
JOURS_0802 = {"08.02.01": 27, "08.02.02": 28, "08.02.03": 31}  # répartis sur les barres de la page 2
JOURS_0804 = [27, 28, 29, 33, 38]   # dans l'ordre des lignes (le PPT numérote deux fois 08.04.04)
JOURS_0805 = [28, 29, 31, 33, 38]

# Noms courts (le « sujet » de la carte MELMIL). Écrits à la main : couper le
# libellé du PPT faisait disparaître ce qui distingue deux injects (la ville
# des cinq demandes 08.05, par exemple). Le texte intégral du PPT reste, lui,
# dans la description de chaque inject.
NOMS = {
    "06.01.01": "Pylônes électriques / poteaux téléphoniques systématiquement détruits dans le fuseau (axe D674-D38, SARRALBE)",
    "06.01.02": "Post RS d'un profil militaire Mercure : « Bitche, on revient »",
    "06.01.03": "Civils ARN de Bousseviller et Liederschiedt chassés vers le SO par des « soldats Mercure arrivés depuis peu »",
    "06.01.04": "Drones d'observation décelés par la Force, exfiltrés vers l'E puis le N",
    "06.01.05": "Témoignage de civils ARN fuyant le NE : départ précipité de troupes Mercure vers le Nord",
    "06.01.06": "Câbles téléphoniques / pylônes électriques intacts (conquête O23)",
    "06.01.07": "Mouvement précipité de populations pro-Mercure, à pied et en véhicule, direction NE",
    "06.01.08": "Carte Mercure abandonnée dans une ferme devant notre progression, transmise par la population",
    "06.01.09": "La population signale le survol de drones venant de l'EST",
    "06.01.10": "UN OCHA alerte les ETIM : violences contre les populations ARN à Grosbliederstroff",
    "06.01.11": "Vidéo sur X (compte pro-ARN) d'un convoi Mercure conspué par la population : « #ilsreviennent »",
    ("06.02", "BST"): "Rumeurs RS : comportements irrespectueux de la Force BLEU en zone de combat",
    ("06.02", "27 BIM"): "Rumeur : points de passage payants et trafic de rations imputés à la Force BLEU",
    ("06.02", "9 BIMa"): "Plaintes ARN relayées par les autorités : pillages, vols et recels imputés à la Force",
    ("08.03", "BST"): "Véhicule à l'emblème du CICR utilisé pour des prises d'otages d'enfants",
    ("08.03", "27 BIM"): "Bien protégé (NSL) utilisé comme lieu d'exécution — la Force découvre un charnier",
    ("08.03", "9 BIMa"): "Bouclier humain ARN (manifestation) pour bloquer la progression de la Force",
    "08.02.01": "Mail du G39/1CA : sites sensibles potentiellement vulnérables (deux laboratoires BSL-3 à HNANCY)",
    "08.02.02": "Site de production d'essence : risque de fuite dans la nature faute de maintenance",
    "08.02.03": "Coopérative agricole lorraine (nitrate d'ammonium) touchée par des tirs d'origine inconnue",
    ("08.04", 1): "FRAGO du 1CA : ordre de dégager un axe pour un HUM (D+27 ou startex package)",
    ("08.04", 2): "Flux d'IDPs fuyant HNANCY via HTOUL vers HST-DIZIER et HCHAUMONT (SCRIPT)",
    ("08.04", 3): "UN OCHA demande des couloirs humanitaires : HNANCY → HTOUL, HLUNEVILLE → HCHAUMONT",
    ("08.04", 4): "Mouvements sporadiques d'IDPs fuyant HSARREBOURG vers HLUNEVILLE (SCRIPT)",
    ("08.04", 5): "Mouvements sporadiques d'IDPs fuyant HHAGUENEAU (SCRIPT)",
    ("08.05", 1): "Autorités locales : sécuriser les accès et ravitailler les camps de déplacés de HST-DIZIER",
    ("08.05", 2): "Autorités locales : sécuriser les accès et ravitailler les camps de déplacés de HCHAUMONT / VILIERS-LE-SEC",
    ("08.05", 3): "Autorités locales : sécuriser les accès et ravitailler les camps de déplacés de HJOINVILLE",
    ("08.05", 4): "Autorités locales : sécuriser les accès et ravitailler les camps de déplacés de HNEUFCHÂTEAU",
    ("08.05", 5): "Autorités locales : réapprovisionner HLUNEVILLE en eau et en vivres",
}

RE_CRQ = re.compile(r"(\d{2}\.\d{2}\.I\d{2})\s*:\s*(\d{2})(\d{2})(\d{2})(\d{2})\s*:\s*(CRQ_\d{2})")

injects: dict[str, list[dict]] = {k: [] for k in STORYLINES}


def ajouter(sl: str, *, nom: str, description: str, quand: str, attendu: str = "", coord: str = "",
            destinataires: list[str] | None = None, moyen: str = "À PRÉCISER", roles: list[str] | None = None):
    injects[sl].append(dict(nom=nom, description=description, quand=quand, attendu=attendu, coord=coord,
                            destinataires=destinataires or ["1 DIV"], moyen=moyen, roles=roles or ["ETIM"]))


def moyen_de(txt: str) -> str:
    t = txt.lower()
    if "mail" in t:
        return "E-MAIL"
    if any(k in t for k in ("post rs", "tweet", "vidéo sur x", "vidéo sur x", " rs ")):
        return "RÉSEAU SOCIAL"
    if "frago" in t:
        return "ORDRE (FRAGO)"
    return "À PRÉCISER"


# 06.01 — deux diapositives d'injects, jours multiples
eff = bloc(3, "EFFET ATTENDU")
for i in (3, 4):
    for code, txt in lignes_injects(i):
        code = code.split()[0]
        jours = JOURS_0601[code]
        for k, j in enumerate(jours, 1):
            occ = f" — occurrence {k}/{len(jours)}" if len(jours) > 1 else ""
            ajouter("06.01", nom=NOMS.get(code, nom_court(txt)), quand=iso(jour(j)), attendu=eff, moyen=moyen_de(txt),
                    description=f"{txt}\n\n[PPT {code} — D+{j}{occ}]",
                    coord="Coordination EXCON : " + ", ".join(coordination(i)), roles=["ETIM", "ETEC"])

# 06.02 et 08.03 — narratifs, un inject par CRQ
DEST = {"BST": "1 DIV", "27 BIM": "27 BIM", "9 BIMa": "9 BIMa"}
for sl, i in (("06.02", 5), ("08.03", 8)):
    for n in narratifs(i):
        quoi = n["quoi"]
        desc = re.split(r"\bH1\s*:", quoi)[0]
        desc = RE_CRQ.sub("", desc).strip(" :/\n")
        hyp = "\n".join(l.strip(" /") for l in quoi.split("/") if re.match(r"\s*H\d", l))
        for m in RE_CRQ.finditer(quoi):
            code_ppt, jj, mm, hh, mi, crq = m.groups()
            quand = f"2026-{mm}-{jj}T{hh}:{mi}:00"
            ajouter(sl, nom=f"{n['qui_ligne']} — {NOMS.get((sl, n['qui_ligne']), nom_court(n['narratif'], 90))} ({crq})",
                    description=f"{n['narratif']}\n\n{desc}\n\n[PPT {sl} narratif {n['qui_ligne']} — {n['quand']} — {crq} (codé {code_ppt} dans le PPT)]",
                    quand=quand, attendu=hyp, destinataires=[DEST.get(n["qui_ligne"], n["qui_ligne"])],
                    roles=[n["par_qui"] or "ETIM"], moyen="RÉSEAU SOCIAL" if "tweet" in quoi.lower() or "rs" in quoi.lower() else "À PRÉCISER",
                    coord="Coordination EXCON : " + ", ".join(coordination(i)))

# 08.01 — STARTEX
ajouter("08.01", nom="STARTING PACKAGE — état critique des ressources essentielles entre PL2 et PL3",
        description=f"{bloc(6, 'DESCRIPTION DE L')}\n\n[PPT 08.01.I01 — STARTING PACKAGE — D+27]",
        quand=iso(jour(27)), attendu=bloc(6, "EFFET ATTENDU"),
        coord="Coordination : " + COORD_P1.get("08.01", "") + " · EXCON : " + ", ".join(coordination(6)), moyen="STARTEX PACKAGE")

# 08.02 — sites sensibles, jours répartis
for code, txt in lignes_injects(7):
    code = code.split()[0]
    j = JOURS_0802[code]
    ajouter("08.02", nom=NOMS.get(code, nom_court(txt)), description=f"{txt}\n\n[PPT {code} — D+{j} (réparti sur la période D+27/D+32)]",
            quand=iso(jour(j)), attendu=bloc(7, "EFFET ATTENDU"), moyen=moyen_de(txt),
            destinataires=["1 DIV"], roles=["ETIM", "HN", "AUTORITÉS CIVILES"],
            coord="Coordination : " + COORD_P1.get("08.02", "") + " · EXCON : " + ", ".join(coordination(7)))

# 08.04 et 08.05 — un jour par ligne
for sl, i, jours, roles in (("08.04", 9, JOURS_0804, ["HN", "AUTORITÉS ARN", "POPULATION ARN"]),
                            ("08.05", 10, JOURS_0805, ["HN", "AUTORITÉS LOCALES"])):
    eff = bloc(i, "EFFET ATTENDU") or bloc(i, "EFFETS ATTENDUS")
    for rang, ((code, txt), j) in enumerate(zip(lignes_injects(i), jours), 1):
        ajouter(sl, nom=NOMS.get((sl, rang), nom_court(txt)), description=f"{txt}\n\n[PPT {code.split()[0]} — D+{j}]",
                quand=iso(jour(j)), attendu=eff, moyen=moyen_de(txt), roles=roles,
                coord="Coordination : " + COORD_P1.get(sl, "") + " · EXCON : " + ", ".join(coordination(i)))

# --------------------------------------------------------------------------- écriture au format JEMM

EXPORT = dt.datetime.now(dt.UTC).strftime("%Y-%m-%dT%H:%M:%S.%f0Z")
MARQUAGE = {"Owner": "NATO", "Classification": "UNCLASSIFIED", "Releasability": [], "Rank": 10, "Color": "lightgreen"}
CELLULE = {"06": "ILI", "08": "GREY CELL"}


def ref(nom_: str, *cle: str) -> dict:
    return {"Id": uid("ref", nom_, *cle), "Name": nom_, "Description": ""}


def export_event(ev: str) -> dict:
    e = EVENTS[ev]
    ev_id = uid("event", ev)
    debut, fin = jour(27), jour(41)
    event_min = {"Id": ev_id, "Number": int(ev), "Literal": ev, "Name": e["nom"], "Mode": 0, "IsLocked": False, "IsLockedInMode": False}
    cell = ref(CELLULE[ev], "cellule")
    storylines, injections = [], []
    for sl, s in STORYLINES.items():
        if s["event"] != ev:
            continue
        sl_id = uid("storyline", sl)
        num = int(sl.split(".")[1])
        story = bloc(s["slides"][0], "DESCRIPTION DE L") or bloc(s["slides"][0], "DESCRIPTION DE LA")
        qoq = quand_ou_qui(s["slides"][0])
        storylines.append({
            "Event": event_min, "Number": num,
            "StartDate": iso(jour(s["debut"]), 0), "EndDate": f"{jour(s['fin']).isoformat()}T23:59:59.999",
            "CalculatedPlannedDateTime": iso(jour(s["debut"]), 0),
            "Duration": f"{s['fin'] - s['debut']}.23:59:59.9990000",
            "IsTimeDependent": False, "DependingOn": None, "TimeDependencyLeadTime": "00:00:00", "TimeDependencyReference": 0,
            "CoordinatingCell": cell,
            "TrainingAudienceList": [{**ref("1 DIV", "ta"), "EmailAddresses": [], "ChatAddresses": []}],
            "PrimaryTrainingObjective": {"Id": uid("to", "8.1"), "Name": "8.1", "Code": "DLT26-8.1"},
            "IncludeAllSupportingTasks": True, "SupportingTaskList": [], "SecondaryTrainingObjectiveList": [],
            "TagList": [], "AssociatedMeetingList": [],
            "Story": story + (f"\n\nQUI : {qoq.get('QUI', '')} · OÙ : {qoq.get('OU', '')} · QUAND : {qoq.get('QUAND', '')}" if qoq else ""),
            "Attachments": [], "FeatureCollectionGeoJSON": None,
            "Id": sl_id, "Literal": sl, "Name": s["nom"], "Type": 1,
        })
        sl_min = {"Id": sl_id, "Number": num, "Literal": sl, "Name": s["nom"], "EventId": ev_id, "Event": event_min}
        for n, inj in enumerate(sorted(injects[sl], key=lambda x: x["quand"]), 1):
            lit = f"{sl}.I{n:02d}"
            injections.append({
                "Description": inj["description"],
                "FunctionalAreaMessage": "*** EXERCISE EXERCISE EXERCISE ***\n",
                "ExpectedOutcome": inj["attendu"], "CoordinationRemarks": inj["coord"], "RelayFrom": "",
                "IsAutomatic": False, "IsTriggering": False, "Attachments": [], "AssociatedStorylineElements": [], "TagList": [],
                "Storyline": sl_min, "IsTimeDependent": False,
                "FixedDateTime": inj["quand"], "ActualDateTime": None,
                "CalculatedPlannedDateTime": inj["quand"], "DisplayDateTime": inj["quand"],
                "TimeDependencyLeadTime": "00:00:00", "DependingOn": None, "TimeDependencyReference": 0,
                "InjectionMeans": {"Id": uid("moyen", inj["moyen"]), "Name": inj["moyen"], "DeliveryType": 0,
                                   "StateOnDelivered": {"Id": uid("etat", "Injected"), "Name": "Injected", "Color": "#98FB98", "IsProtected": False}},
                "Sender": cell, "CoordinatingCell": cell,
                "ReceiverList": [{**ref(d, "ta"), "EmailAddresses": [], "ChatAddresses": []} for d in inj["destinataires"]],
                "ActivityLevel": {"Id": uid("activite", "Low"), "Name": "Low", "Level": 25},
                "ScenarioRoleList": [{"Name": r, "UniqueId": f"fictif:DLT26:Actor:{r}", "Source": "JEMM.MelMil.Actors", "Side": ""} for r in inj["roles"]],
                "InformationMarking": {**MARQUAGE, "Id": uid("marquage")},
                "Id": uid("inject", lit), "Number": n, "Literal": lit, "Name": inj["nom"],
                "InjectionType": {"Id": uid("type", "Inject"), "Type": 1, "Name": "Lead in" if n == 1 else "Main event"},
            })
    data = {
        "Events": [{"Attachments": [], "Mode": 0, "Description": e["description"], "Id": ev_id, "Literal": ev,
                    "Name": e["nom"], "Code": str(int(ev)), "StartDate": iso(debut, 0),
                    "EndDate": f"{fin.isoformat()}T23:59:59.999", "Duration": f"{(fin - debut).days}.23:59:59.9990000"}],
        "Storylines": storylines, "Injections": injections,
        "Actions": [], "Returns": [], "IntendedStorylineOutcomes": [], "ExternalDependencies": [], "StorylineObservationTasks": [],
    }
    meta = {"TenantType": 1, "ExportDateTime": EXPORT, "ExportedBy": "MINERVE — DELATTRE (export FICTIF, généré depuis le PPT GREY CELL v4)",
            "ExerciseName": "DE LATTRE 26", "OrganizationName": None, "OrganizationIdentifier": None,
            "WorkspaceIdentifier": "DLT26", "InformationMarking": MARQUAGE, "ExportFileVersion": "1.0.1"}
    corps = {"Data": data, "MetaData": meta}
    corps["EncodedData"] = base64.b64encode(json.dumps({"Data": data, "MetaData": meta}, ensure_ascii=False, indent=2).encode("utf-8")).decode("ascii")
    return corps


os.makedirs(SORTIE, exist_ok=True)
horo = dt.datetime.now().strftime("%Y%m%d_%H%M%S")
for ev in EVENTS:
    chemin = os.path.join(SORTIE, f"FICTIF_{horo}_JEMM_DLT26_EVENT_{ev}.json")
    contenu = export_event(ev)
    with open(chemin, "w", encoding="utf-8") as f:
        json.dump(contenu, f, ensure_ascii=False, indent=2)
    n_sl = len(contenu["Data"]["Storylines"])
    n_inj = len(contenu["Data"]["Injections"])
    print(f"{os.path.basename(chemin)} : {n_sl} storylines, {n_inj} injects")
    for inj in contenu["Data"]["Injections"]:
        print(f"   {inj['Literal']:11} {inj['DisplayDateTime'][:16]}  {inj['Name'][:80]}")
