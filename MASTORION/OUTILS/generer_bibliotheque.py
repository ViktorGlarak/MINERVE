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
A7_RZO = os.path.join(EXER, r"AURIGE 7BB\00_Boites à outils\MASTAURIGE\LOCALSTORAGE_WEB_VERSION\Sites\Trombinoscope\rzo_data.js")
A2_AVA = os.path.join(EXER, r"AURIGE 2BB\00_Boites à outils\MASTAURIGE\WEB\avatars.js")
CASW = os.path.join(EXER, r"01 ORION 26\01 - O41 - ARCHIVAGE - DOCUMENTS TRIES\01 - ORIGINE WORKING FIELDO41\99-TOOLS\setup\orion26-stobo\avatars_casw_ia_usable.md")
REGISTRE = os.path.join(MINERVE, r"MASTAURIGE\MEMOIRE.md")
SORTIE = os.path.join(MINERVE, r"MASTORION\BIBLIOTHEQUES\BIBLIOTHEQUE_TEST_3_EXERCICES.xlsx")

# Colonnes reconnues par l'import MASTORION (cf. import-users.ts KNOWN_COLS)
COLS = ["masto_id", "username", "display_name", "email", "password", "bio", "groups", "avatar",
        "age", "genre", "pays", "label", "origine", "religion", "situation",
        "caractere", "langage", "activite", "observations", "qualifications", "aime", "deteste"]

CAMP_LABEL = {"rouge": "CAMP ROUGE", "bleu": "CAMP BLEU", "neutre": "CAMP NEUTRE"}

# ══════════════════════════════════════════════════════════════════════
#  TAXONOMIE DES GROUPES  —  format « PAYS - FONCTION »
#  (refonte 2026-07-28 : les groupes CASW d'origine etaient trop nombreux,
#   heterogenes et souvent a un seul membre)
# ══════════════════════════════════════════════════════════════════════
# ⚠ DECISION UTILISATEUR 2026-07-28 : « Titane » n'est PAS une nation distincte —
#   c'est le nom de la force FORAD de l'armee mercurienne (toutes les fiches CASW
#   marquees TITAN ont Pays = Mercure). Le code TIT est supprime, tout revient a MER.
PAYS_CODE = {
    "mercure": "MER", "mer": "MER", "titane": "MER", "titan": "MER",
    "arnland": "ARN", "arn": "ARN", "arnish": "ARN",
    "france": "FR", "francaise": "FR", "français": "FR",
    "bothnia": "BOT", "bot": "BOT",
}
PAYS_NOM = {"MER": "Mercure", "ARN": "Arnland", "FR": "France", "BOT": "Bothnia"}

# Personas ecartes de la bibliotheque (doublons d'identite tranches par l'utilisateur)
EXCLUSIONS = {
    "@kozi_aus",   # « Andrei Kolesnikov » apprenti, homonyme exact du sergent
                   # @KolesnikovAndrei (employe dans les 2 exercices) -> un seul conserve
}

# Groupes transverses, SANS prefixe pays
TRANSVERSE = ("ONG", "INSTITUTION INTERNATIONALE", "OTAN", "UE",
              "MEDIA INTERNATIONAL", "ANIMATION EXERCICE")

# ── Corrections manuelles, issues de la connaissance MINERVE (registre MASTAURIGE,
#    mémoires MINAUTORE / GUILLAUME / ANALYSTE_ARN). Priment sur la deduction.
#    ⚠ Piege corrige ici : la Lorraine « H-prefixe » du 7BB est ARNLANDAISE (fiction),
#    alors que la Lorraine du 2BB est la vraie France -> les handles en 57/67 ne sont
#    PAS des departements francais cote MINOTAURE.
OVERRIDES = {
    "@stepan_roubek":    ["ARN - PRO-MERCURE", "ARN - CITOYEN"],   # temoin mercurianophone HSarrebourg
    "@j_vasseur":        ["ARN - MILITAIRE"],                      # veteran DAC (=ARN) amputé
    "@makarovsid":       ["ARN - PRO-MERCURE"],                    # habitant HBlamont, diaspora MER
    "@gavrilovborislav": ["ARN - PRO-MERCURE"],                    # habitant HDieuze, diaspora MER
    "@eastwatch_intl":   ["MEDIA INTERNATIONAL"],                  # relais OSINT, blanchiment MER
    "@temoignagearn":    ["ARN - PRO-MERCURE"],                    # compte « temoignage » pilote MER
    "@voixarnland":      ["ARN - PRO-MERCURE"],
    "@temoignagedac":    ["ARN - PRO-MERCURE"],
    "@voixdacia":        ["ARN - PRO-MERCURE"],
    "@bernardlutz67":    ["ARN - CITOYEN"],                        # habitant HSaverne (7BB)
    "@julienholveck57":  ["ARN - CITOYEN"],                        # habitant arnlandais (7BB)
    "@sylviebrucker57":  ["ARN - CITOYEN"],                        # commercante HMittersheim (7BB)
    "@brigitteschmitt67": ["ARN - PRO-MERCURE", "ARN - CITOYEN"],  # HSarre-Union, penchant MER
    "@marcweber67":      ["ARN - PRO-MERCURE", "ARN - CITOYEN"],
    "@marionkessler57":  ["ARN - CITOYEN"],                        # 7BB, zone H-prefixe
    "@veilleosint_est":  ["MER - SOCK-PUPPET"],                    # facade pro-FR, operation MER
    "@t_reynaud_fr":     ["MER - SOCK-PUPPET"],
    "@sophie_moselle":   ["MER - SOCK-PUPPET"],
    "@novusordomundi":   ["ARN - GROUPE CLANDESTIN"],              # organisation clandestine pro-MER
    "@arnlandlovepeace": ["ARN - PACIFISTE", "ARN - PRO-MERCURE"], # facade eco-pacifiste, manoeuvre rouge
    "@clambroise55":     ["FR - CITOYEN"],                         # 2BB : vraie Lorraine francaise

    # ── Audit ANALYSTE (Mercure), 2026-07-28 — corrections fondées sur
    #    ANALYSTE\MERCURE\MEMOIRE.md + registre MASTAURIGE + fiches CASW
    "@home_mum":         ["MER - FAMILLE DE MILITAIRE"],           # mere d'un soldat du 5e bat. artillerie
    "@1aia":             ["MER - MILITAIRE"],                      # 1ere Armee Blindee de la Garde (unite)
    "@titancom":         ["MER - MILITAIRE"],                      # compte du COM FORAD (Lt-Gen Kissel)
    "@2divinfmec":       ["MER - MILITAIRE"],                      # CASW pays=Mercure (TITAN = force FORAD)
    "@4divbld":          ["MER - MILITAIRE"],
    "@mpaleksanvorynofficial": ["MER - POLITICIEN"],               # depute MUP, proche d'Olamao
    "@loloanna":         ["MER - INFLUENCEUR"],                    # influenceuse / tele-realite
    "@viktorslade":      ["ARN - GROUPE CLANDESTIN", "ARN - PRO-MERCURE"],  # 2IC milice TANTALE
    "@natogohome":       ["MER - GROUPE CLANDESTIN", "MER - PATRIOTE"],     # collecteur de fonds Tantale
    "@mamamia":          ["MER - REFUGIE", "MER - PATRIOTE"],       # refugie MER en Haquitaine
    "@meihoffrudolf":    ["MER - REFUGIE", "MER - PATRIOTE"],
    "@petrovaferapont":  ["MER - PATRIOTE", "MER - FAMILLE DE MILITAIRE", "MER - INFLUENCEUR"],
    "@mercurerealnews":  ["MER - PATRIOTE", "MER - INFLUENCEUR"],
    "@calgarmarneus":    ["MER - RELIGIEUX", "MER - PACIFISTE"],    # pope orthodoxe anti-guerre
    "@gotmituns":        ["MER - RELIGIEUX", "MER - PACIFISTE"],
    "@love_our_soldiers": ["MER - PACIFISTE", "MER - OPPOSITION", "MER - INFLUENCEUR"],
    "@temoignagedac":    ["ARN - PRO-MERCURE", "MER - SOCK-PUPPET"],  # rouge camoufle civil (Storm-1516)
    "@voixdacia":        ["ARN - PRO-MERCURE", "MER - SOCK-PUPPET"],
    "@temoignagearn":    ["ARN - PRO-MERCURE", "MER - SOCK-PUPPET"],  # equivalents 7BB
    "@voixarnland":      ["ARN - PRO-MERCURE", "MER - SOCK-PUPPET"],
    "@siegumjedenpreis": ["ARN - PRO-MERCURE"],                     # diaspora MER residant en ARN
    "@hmunikvoice":      ["ARN - PRO-MERCURE", "ARN - JOURNALISTE"], # propagandiste radio
    "@maiakovalenko":    ["ARN - PRO-MERCURE", "ARN - JOURNALISTE"],
    "@karidovmichel":    ["BOT - CITOYEN"],                         # CASW pays=Bothnia
    "@svetlovirina":     ["BOT - CITOYEN"],
    "@swifttaylor":      ["ANIMATION EXERCICE"],                    # CASW pays=ANIMATION

    # ── Audit ANALYSTE_ARN (Arnland), 2026-07-28
    "@timesarnish":      ["ARN - JOURNALISTE"],                     # organe de presse, pas un citoyen
    "@officialskolkan":  ["ARN - PRO-MERCURE", "ARN - JOURNALISTE"],  # station Skolkan FM, pro-MER
    "@asps_officiel":    ["ARN - AUTORITE LOCALE"],                 # Arnland State Police Services
    "@acquarnland":      ["ARN - ACTEUR ECONOMIQUE"],               # PME eau potable pres de HLa Rochelle
    "@ionescupetr_ceo_artc": ["ARN - ACTEUR ECONOMIQUE"],           # CEO Arnland Rail Transportation Co
    "@ivanhorvat_artc":  ["ARN - ACTEUR ECONOMIQUE"],               # ingenieur maintenance ARTC
    "@dragovic_novak_eda": ["ARN - ACTEUR ECONOMIQUE"],             # reseau electrique EDA
    "@kovalenkoandrei_eda": ["ARN - ACTEUR ECONOMIQUE"],
    "@pavelkov_novak_eda": ["ARN - ACTEUR ECONOMIQUE"],
    "@petrenko_dnepr_eda": ["ARN - ACTEUR ECONOMIQUE"],
    "@freunderolf":      ["ARN - CITOYEN"],                         # etudiant refractaire, refuse de se battre
    "@giselam":          ["ARN - CITOYEN"],
    "@keypof":           ["ARN - CITOYEN"],                         # adolescente a HParis
    "@togwewin":         ["ARN - MILITAIRE", "ARN - PATRIOTE"],     # soldat logistique ARN
    "@kevdu13":          ["FR - MILITAIRE"],                        # CASW pays=France, CCH de la SDCO
    "@arnwillwin":       ["FR - INFLUENCEUR", "FR - REFUGIE"],      # influenceuse FR refugiee dans la Loire
    "@manfredk":         ["ARN - CITOYEN"],                         # franco-ARN vivant en ARN, non deplace
    "@faahcharentemaritime": ["ARN - MILITAIRE", "ARN - AUTORITE LOCALE"],  # DMD HCharente-Maritime
    "@pasteurvolkonsky": ["ARN - PRO-MERCURE", "ARN - RELIGIEUX"],  # leader protestant pro-MER
    "@shootarnland":     ["ARN - PRO-MERCURE", "ARN - PACIFISTE"],  # collectif anti-guerre MAIS pro-MER
    "@correspondantest": ["MEDIA INTERNATIONAL", "MER - SOCK-PUPPET"],  # couche 2 piege retroactif

    # ── Audit MINAUTORE + GUILLAUME (emploi editorial reel dans les injects), 2026-07-28
    #    Regle degagee : un compte a FAÇADE est classe selon sa NATURE (sock-puppet MER),
    #    la façade restant lisible en 2e groupe.
    "@temoignagedac_":   [],                                         # (placeholder, voir ci-dessous)
    "@j_vasseur":        ["MER - SOCK-PUPPET", "ARN - MILITAIRE"],   # veteran ARN/DAC = relais rouge (08.03.04Gi)
    "@eastwatch_intl":   ["MEDIA INTERNATIONAL", "MER - SOCK-PUPPET"],  # think-tank de blanchiment MER
    "@arnlandlovepeace": ["ARN - PRO-MERCURE", "ARN - PACIFISTE"],   # manoeuvre rouge sous façade verte (05.09.I04)
    "@s_tikhanov":       ["BOT - POLITICIEN", "BOT - OPPOSITION", "BOT - PRO-MERCURE"],
    "@a_saniki":         ["BOT - POLITICIEN", "BOT - OPPOSITION", "BOT - PRO-MERCURE"],
    "@h_hansen":         ["BOT - POLITICIEN", "BOT - OPPOSITION"],   # cheffe opposition BPP pro-UE (Bothnia)
    "@eurotendency_b":   ["UE", "BOT - ACTEUR ECONOMIQUE"],          # groupe de pression pro-UE en Bothnia
    "@gavrilovborislav": ["ARN - PRO-MERCURE", "ARN - CITOYEN"],     # habitant HDieuze, diaspora (revue 06-21)
    "@makarovsid":       ["ARN - PRO-MERCURE", "ARN - CITOYEN"],     # habitant HBlamont, diaspora
    "@novusordomundi":   ["ARN - GROUPE CLANDESTIN", "ARN - PRO-MERCURE"],
    "@sylviebrucker57":  ["ARN - CITOYEN", "ARN - ACTEUR ECONOMIQUE"],  # epiciere ruinee de HMittersheim
    "@pasteurvolkonsky": ["ARN - RELIGIEUX", "ARN - PRO-MERCURE"],   # pasteur de HLuneville
}
# Comptes « temoignage / voix » : façade civile, outil rouge (Storm-1516 couche 1)
for _h in ("@temoignagedac", "@voixdacia", "@temoignagearn", "@voixarnland"):
    OVERRIDES[_h] = ["MER - SOCK-PUPPET", "ARN - PRO-MERCURE"]
OVERRIDES.pop("@temoignagedac_", None)

# ── Audit ANALYSTE_BOT (Bothnia + France + transverses), 2026-07-28
OVERRIDES.update({
    "@a_saniki":         ["BOT - OPPOSITION", "BOT - PRO-MERCURE", "BOT - POLITICIEN"],
    "@compteofficielcicr": ["INSTITUTION INTERNATIONALE"],          # CICR = OI a mandat DIH, pas une ONG
    "@1fracorpsinarnland": ["FR - MILITAIRE"],                      # compte officiel de corps d'armee
    "@cimic_1div":       ["FR - MILITAIRE"],                        # officier CIMIC 1re DIV
    "@1stdivinarn":      ["FR - MILITAIRE"],                        # 1re division deployee en Arnland
    "@corpswarfighting": ["FR - MILITAIRE"],                        # etat-major de corps
    "@milimothers":      ["FR - PATRIOTE", "FR - FAMILLE DE MILITAIRE"],  # assoc. femmes de militaires
    "@kardashiankim":    ["FR - INFLUENCEUR"],                      # vecteur de notoriete

    # ── Arbitrages utilisateur du 2026-07-28
    #  (2) Pas de region francaise reelle dans les exercices : les civils de la zone
    #      d'operation sont arnlandais (France fictive = Arnland), meme en 2BB.
    "@clambroise55":     ["ARN - CITOYEN"],
    #  (3) Sa BIOGRAPHIE fait foi : sergent senior de la 47e division mercurienne.
    #      ⚠ contredit la revue MINOTAURE du 2026-06-21 qui en faisait un habitant
    #      de HDieuze (diaspora) — les injects 7BB concernes sont a revoir.
    "@gavrilovborislav": ["MER - MILITAIRE"],
})

# CASW : groupe d'origine -> (code pays ou None = deduire, FONCTION)
MAP_CASW = {
    "o4 comptes officiels mercure": ("MER", "POLITICIEN"),
    "o4 groupe animation ili mercure": (None, "ANIMATION EXERCICE"),
    "o4 groupe patriote mercure": ("MER", "PATRIOTE"),
    "o4 groupe pacifiste mercure": ("MER", "PACIFISTE"),
    "o4 groupe soldat mercure/titane": ("MER", "MILITAIRE"),
    "o4 heros de guerre mercurien": ("MER", "MILITAIRE"),
    "o4 groupe femmes de militaires forad": ("MER", "FAMILLE DE MILITAIRE"),
    "o4 groupe officiel titan": ("MER", "POLITICIEN"),   # TITAN = force FORAD mercurienne
    "o4 officiel arn": ("ARN", "POLITICIEN"),
    "o4 patriotes arn": ("ARN", "PATRIOTE"),
    "o4 groupe soldats arn": ("ARN", "MILITAIRE"),
    "o4 groupe pro-mercure en arn": ("ARN", "PRO-MERCURE"),
    "o4 refugies arn": ("ARN", "REFUGIE"),
    "o4_autoriteshn": ("ARN", "AUTORITE LOCALE"),
    "o4 groupe officiel francais": ("FR", "POLITICIEN"),
    "o4 groupe soldat francais": ("FR", "MILITAIRE"),
    "o4 groupe patriote francais": ("FR", "PATRIOTE"),
    "o4 groupe anti-militariste francais": ("FR", "PACIFISTE"),
    "o4 medias francais": ("FR", "JOURNALISTE"),
    "o4 mediafrancelarontonde": ("FR", "JOURNALISTE"),
    "o4 media france journal national": ("FR", "JOURNALISTE"),
    "o4 media france hexagone": ("FR", "JOURNALISTE"),
    "o4 media france afg": ("FR", "JOURNALISTE"),
    "02-redteam - presse": (None, "JOURNALISTE"),
    "o4 ong ngos": (None, "ONG"),
    "o2 - ani haute ong": (None, "ONG"),
    "o4 army": (None, "MILITAIRE"),
    "o4animation1ca": (None, "ANIMATION EXERCICE"),
    "o4 animation div1": (None, "ANIMATION EXERCICE"),
}

# EHO (trombinoscope 7BB) : champ `groupe` -> FONCTION
MAP_EHO = {
    "gouvernement": "POLITICIEN",
    "gouvernement & institutions": "POLITICIEN",
    "prefecture & maires (host nation)": "AUTORITE LOCALE",
    "commandement militaire (bndf)": "MILITAIRE",
    "ong & humanitaire": "ONG",
    "acteurs economiques": "ACTEUR ECONOMIQUE",
    "societe civile pro-mercure": "PRO-MERCURE",
    "opposition": "OPPOSITION",
    "religieux": "RELIGIEUX",
}

# Metier declare (champ CASW `activite`) -> FONCTION, en dernier recours
MAP_ACTIVITE = {
    "militaire": "MILITAIRE", "journaliste": "JOURNALISTE", "chroniqueur": "JOURNALISTE",
    "politicien": "POLITICIEN", "influenceur": "INFLUENCEUR", "procureur": "AUTORITE LOCALE",
    "professeur": "CITOYEN", "etudiant": "CITOYEN", "artiste": "CITOYEN",
    "chanteur": "CITOYEN", "retraite": "CITOYEN",
}


def _cle(s):
    return norm2(s)


def norm2(s):
    """Normalisation souple pour comparer des libelles (accents, casse, ponctuation)."""
    s = unicodedata.normalize("NFD", str(s or "")).encode("ascii", "ignore").decode()
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9&\-_/ ]", " ", s.lower())).strip()


def deduire_pays(cw, fe, nom, handle, note=""):
    """Code pays : champ `pays` (CASW/EHO) > pays porte par le groupe CASW
    d'origine > indice explicite dans le nom / le handle / la note."""
    for source in (cw.get("pays"), fe.get("pays")):
        c = PAYS_CODE.get(norm2(source))
        if c:
            return c
    for g in cw.get("groupes", []):                      # ex. « O4 Patriotes ARN » -> ARN
        cible = MAP_CASW.get(norm2(g))
        if cible and cible[0]:
            return cible[0]
    txt = norm2(" ".join([nom, handle, note or ""]))
    for motif, code in ((r"titan", "TIT"), (r"mercur|\bmer\b|hmunik", "MER"),
                        (r"arnland|arnish|\barn\b|dacia|\bdac\b", "ARN"),
                        (r"bothnia|\bbot\b|\bbc1\b|pahonie", "BOT"),
                        (r"franc|\bfr\b|lorrain|moselle|\d{2}\b", "FR")):
        if re.search(motif, txt):
            return code
    return None


# Institutions reconnaissables — cherchees UNIQUEMENT dans le nom et le handle
# (⚠ ne jamais chercher dans les bios : « ONU », « OTAN », « UE » y sont des SUJETS,
#  pas l'appartenance du persona ; et « un »/« eu » sont des mots francais courants)
MOTIFS_INSTITUTION = (
    (r"\bonu\b|\bunhcr\b|\bunocha\b|\baiea\b|\biaea\b|nations unies|united nations",
     "INSTITUTION INTERNATIONALE"),
    (r"\botan\b|\bnato\b|\bshape\b|\bsaceur\b", "OTAN"),
    (r"amnesty|croix[- ]rouge|\bcicr\b|\bicrc\b|humanitaire|medecins sans|\bmsf\b|\bhrw\b",
     "ONG"),
    (r"union europeenne|\bue\b|european union|\beuropean commission\b", "UE"),
)


def deduire_fonction(cw, fe, nom, handle, note):
    """FONCTION d'un persona, par ordre de fiabilite decroissante."""
    identite = norm2(nom + " " + handle)

    # 1. institution internationale identifiee par le NOM (pas par la bio)
    for motif, fonction in MOTIFS_INSTITUTION:
        if re.search(motif, identite):
            return fonction

    # 2. groupes CASW d'origine
    for g in cw.get("groupes", []):
        cible = MAP_CASW.get(norm2(g))
        if cible:
            return cible[1]

    # 3. groupe EHO (trombinoscope)
    f = MAP_EHO.get(norm2(fe.get("groupe", "")))
    if f:
        return f

    # 4. role EHO / metier declare
    role = norm2(fe.get("role", ""))
    if role:
        if re.search(r"president|ministre|depute|secretaire|gouverneur|porte.parole|ambassad", role):
            return "POLITICIEN"
        if re.search(r"general|colonel|commandant|chef d.etat.major|militaire|armee", role):
            return "MILITAIRE"
        if re.search(r"maire|prefet|prefecture", role):
            return "AUTORITE LOCALE"
        if re.search(r"journalist|redacteur|correspondant|presse", role):
            return "JOURNALISTE"
        if re.search(r"eveque|pasteur|imam|rabbin|eglise", role):
            return "RELIGIEUX"
    f = MAP_ACTIVITE.get(norm2(cw.get("activite", "")))
    if f:
        return f

    # 5. indices textuels — sur l'identite ET la note de registre (jamais la bio complete)
    txt = norm2(" ".join([nom, handle, note or ""]))
    if re.search(r"pacifis|anti.?guerre|anti.?militar|love.?peace|stop.?war", txt):
        return "PACIFISTE"
    if re.search(r"refugie|deplace|exil", txt):
        return "REFUGIE"
    if re.search(r"osint|veille|analyst", txt):
        return "INFLUENCEUR"
    if re.search(r"media|news|tv\d|radio|channel|\binfo\b|journal|presse|temoignage|voix|watch",
                 txt):
        return "JOURNALISTE"
    if re.search(r"pro.?mercure|patriot|ordo mundi|\bnom\b", txt):
        return "PATRIOTE"
    if re.search(r"maire|prefet|mairie", txt):
        return "AUTORITE LOCALE"
    return "CITOYEN"


def groupes_final(cw, fe, nom, handle, note):
    """Liste des groupes d'un persona (il peut en cumuler plusieurs :
    p.ex. « ARN - JOURNALISTE » + « ARN - PRO-MERCURE »).
    Retourne (liste_de_groupes, code_pays, fonction_principale)."""
    forces = OVERRIDES.get((handle or "").lower())
    if forces:
        pays = forces[0].split(" - ")[0] if " - " in forces[0] else None
        fonction = forces[0].split(" - ")[-1]
        return list(forces), (pays if pays in PAYS_NOM else None), fonction

    pays = deduire_pays(cw, fe, nom, handle, note)

    # institution internationale reconnue au NOM : prime sur le pays « ANIMATION »
    identite = norm2(nom + " " + handle)
    for motif, fonction in MOTIFS_INSTITUTION:
        if re.search(motif, identite):
            return [fonction], None, fonction

    def nommer(f):
        if f in TRANSVERSE:
            return f
        return "%s - %s" % (pays, f) if pays else "NON CLASSE - %s" % f

    # Les groupes « officiels » (comptes institutionnels) ne disent PAS le metier :
    # un compte d'unite (@6e_Army, @27BgdInfMec) y figure aussi. On affine avec
    # le metier declare (`activite`) — sinon tout finit en POLITICIEN.
    GROUPES_OFFICIELS = {"o4 comptes officiels mercure", "o4 officiel arn",
                         "o4 groupe officiel francais", "o4 groupe officiel titan"}
    metier = MAP_ACTIVITE.get(norm2(cw.get("activite", "")))

    groupes = []
    # toutes les appartenances declarees dans la base CASW
    for g in cw.get("groupes", []):
        cible = MAP_CASW.get(norm2(g))
        if not cible:
            continue
        fonction = cible[1]
        if norm2(g) in GROUPES_OFFICIELS and metier and metier != "POLITICIEN":
            fonction = metier            # ex. compte officiel MER + metier Militaire -> MILITAIRE
        code = cible[0] or pays
        nom_g = fonction if fonction in TRANSVERSE else (
            "%s - %s" % (code, fonction) if code else "NON CLASSE - %s" % fonction)
        if nom_g not in groupes:
            groupes.append(nom_g)
    # appartenance issue du trombinoscope EHO
    f_eho = MAP_EHO.get(norm2(fe.get("groupe", "")))
    if f_eho and nommer(f_eho) not in groupes:
        groupes.append(nommer(f_eho))
    # comptes d'animation de l'exercice (pays « ANIMATION » dans la base CASW)
    if not groupes and norm2(cw.get("pays")) == "animation":
        groupes.append("ANIMATION EXERCICE")
    # a defaut, deduction complete
    if not groupes:
        groupes.append(nommer(deduire_fonction(cw, fe, nom, handle, note)))

    principal = groupes[0]
    return groupes, pays, principal.split(" - ")[-1]


def norm(s):
    s = unicodedata.normalize("NFD", str(s or "")).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]", "", s.lower())


def lire(p):
    return io.open(p, encoding="utf-8", errors="replace").read()


def assainir_pseudo(p):
    """Rend un pseudo utilisable comme `username` MASTORION (equivalent du
    sanitizeUsername de toolbox.ts) : accents retires, apostrophes/espaces
    supprimes, seuls [A-Za-z0-9_.] conserves."""
    p = unicodedata.normalize("NFD", str(p or "")).encode("ascii", "ignore").decode()
    p = p.replace("'", "").replace("`", "").replace(" ", "_")
    return re.sub(r"[^A-Za-z0-9_.]", "", p).strip("_")


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


# ---------------------------------------------------------------- rzo_data.js (reseau RENS/RZO)
def charger_rzo(path):
    raw = lire(path)
    s = raw.index("[", raw.index("window.TROMBI_RZO"))
    d, _ = json.JSONDecoder().raw_decode(raw[s:])
    return d


# reseaux consideres clandestins (mecanique paramilitaire/subversive) -> GROUPE CLANDESTIN
NETS_CLANDESTINS = {"hfm", "nom", "nom (relais/enablers)", "redskulls"}


def classer_rzo_fonction(role):
    r = norm2(role)
    # ⚠ « Pro-MER » = sympathie politique d'un resident ARN (schema ARN-PRO-MERCURE
    #   deja etabli lors de l'audit) — a checker AVANT les autres motifs, sinon un
    #   « Complotiste Pro-MER » finirait classe INFLUENCEUR sans le tag politique.
    if re.search(r"pro-?mer\b", r): return "PRO-MERCURE"
    if re.search(r"maire|prefet", r): return "AUTORITE LOCALE"
    if re.search(r"militaire|instructeur|guerilla|\bdiv\b|regiment|bataillon|adjoint", r): return "MILITAIRE"
    if re.search(r"journalist|radio|animateur|redacteur", r): return "JOURNALISTE"
    if re.search(r"complotiste|influenceu|chanteu|celebrite|agitateur", r): return "INFLUENCEUR"
    if re.search(r"commerc", r): return "ACTEUR ECONOMIQUE"
    if re.search(r"gouverneur|president|depute|ministre", r): return "POLITICIEN"
    if re.search(r"agriculteur", r): return "ACTEUR ECONOMIQUE"
    return "CITOYEN"


def classer_rzo_pays(role):
    # ⚠ « Pro-MER » ≠ nationalite mercurienne (reside en Arnland, sympathie politique).
    #   Seuls des marqueurs d'identite EXPLICITES (« Chanteur MER », « Celebrite MER »)
    #   indiquent une nationalite/appartenance mercurienne reelle.
    r = norm2(role)
    if re.search(r"pro-?mer\b", r): return "ARN"
    if re.search(r"chanteu[a-z]*\s*mer\b|celebrite\s*mer\b", r): return "MER"
    return "ARN"


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
    # ⚠ le separateur precedant la 1re fiche comporte une ligne vide (les autres non)
    #   -> sans le \s*, la fiche AIEA restait collee a l'en-tete du fichier et etait perdue.
    blocs = [b for b in re.split(r"\n---\n\s*(?=## )", raw) if b.strip().startswith("## ")]
    out = []
    for b in blocs:
        entete = re.match(r"##\s+(.+?)\s+\(id:\s*(\d+)\)", b.strip())
        if not entete:
            continue
        nom_complet, pid = entete.group(1).strip(), entete.group(2)
        champs = {}
        for m in re.finditer(r"^\|\s*\*{0,2}([^|*]+?)\*{0,2}\s*\|\s*`?([^|`]*?)`?\s*\|\s*$", b, re.M):
            champs[m.group(1).strip().lower()] = m.group(2).strip()
        # ⚠ certains pseudos contiennent une apostrophe typographique (@Let’sgoMercure)
        #   ou des espaces (@Honneur et Patrie) -> capturer large PUIS assainir,
        #   sinon 28 fiches etaient silencieusement perdues.
        compte = re.search(r"\|\s*Mastodon\s*\|\s*`?(\d*)`?\s*\|\s*@?([^|]+?)\s*\|\s*`?([^|`]*)`?\s*\|\s*([^|]*)\|", b)
        # ⚠ ne prendre QUE les puces de la section "### Groupes" (sinon on capture
        #    les puces de biographie -> faux groupes a rallonge)
        sec_g = re.search(r"###\s*Groupes\s*\n(.*?)(?=\n\s*(?:###|\*\*|\Z))", b, re.S)
        groupes = [g.strip() for g in re.findall(r"^\s*-\s+(.+)$", sec_g.group(1), re.M)] if sec_g else []
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
            "handle": ("@" + assainir_pseudo(compte.group(2))) if compte else "",
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

    # ── fiches EHO (bios.js) SANS handle avatars.js : jamais couvertes jusqu'ici
    #    (presidents, ministres, prefets, maires, generaux, eveques...). Handle
    #    synthetique "@<id_eho>" (deja unique/propre) pour rester dans le meme pipeline.
    noms_couverts = {norm(f["nom"]) for f in fiches.values()}
    for v in eho.values():
        if norm(v["nom"]) in noms_couverts:
            continue
        fiches[v["id"]] = {"handle": "@" + v["id"], "nom": v["nom"], "camp": v.get("camp", "neutre"),
                           "img": "", "exercices": ["MINOTAURE 26"], "prio": 1, "note": ""}
        noms_couverts.add(norm(v["nom"]))

    lignes = []
    stats = {"eho": 0, "note": 0, "casw_bio": 0, "registre": 0, "sans_bio": 0, "exclus": 0}
    for k, f in fiches.items():
        if (f["handle"] or "").lower() in EXCLUSIONS:
            stats["exclus"] += 1
            continue
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

        # ── groupes : taxonomie « PAYS - FONCTION » + appartenance aux exercices
        g_pays, code_pays, fonction = groupes_final(cw, fe, f["nom"], f["handle"], f.get("note"))
        groupes = g_pays + ["EXERCICE %s" % ex for ex in f["exercices"]]
        # ⚠ pour un groupe transverse (code_pays=None : ONG, INSTITUTION INTERNATIONALE,
        #   ANIMATION EXERCICE...), le pays doit rester VIDE, jamais un artefact CASW
        #   du type "Animation" (le champ `pays` de la fiche brute, pas une vraie nation).
        pays = PAYS_NOM.get(code_pays, "")

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
            "label": fonction,
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


def fusionner_rzo(lignes, path):
    """Integre le reseau RENS/RZO (rzo_data.js) dans `lignes` (in place) :
    - un acteur RZO qui correspond (par nom) a une fiche DEJA presente est
      FUSIONNE (ajout d'un tag de groupe, jamais de doublon de ligne) ;
    - sinon une nouvelle ligne (legere) est creee."""
    rzo = charger_rzo(path)
    par_nom = {}
    for l in lignes:
        k = norm(l["display_name"]) or l["display_name"].strip().lower()  # garde-fou noms non-latins (norm() les vide -> collision)
        par_nom[k] = l
    ajouts, fusions = 0, 0
    for p in rzo:
        k = norm(p["nom"]) or p["nom"].strip().lower()
        clandestin = norm2(p.get("net", "")) in NETS_CLANDESTINS
        if k in par_nom:
            l = par_nom[k]
            g = [x for x in l["groups"].split(";") if x]
            if "RESEAU RZO" not in g:
                g.append("RESEAU RZO")
            if clandestin:
                pays_code = next((x.split(" - ")[0] for x in g if " - " in x and x.split(" - ")[0] in PAYS_NOM), "ARN")
                tag = "%s - GROUPE CLANDESTIN" % pays_code
                if tag not in g:
                    g.append(tag)
            l["groups"] = ";".join(g)
            fusions += 1
            continue
        pays_code = classer_rzo_pays(p.get("role", ""))
        fonction = "GROUPE CLANDESTIN" if clandestin else classer_rzo_fonction(p.get("role", ""))
        username = re.sub(r"[^a-z0-9_]", "_", p["id"].replace("-", "_")).strip("_") or ("rzo_%d" % ajouts)
        groupes = ["%s - %s" % (pays_code, fonction), "RESEAU RZO", "EXERCICE MINOTAURE 26"]
        ligne = {
            "camp": p.get("camp", "neutre"), "masto_id": "", "username": username,
            "display_name": p["nom"], "email": "%s@mastorion.local" % username,
            "password": "", "bio": "",
            "groups": ";".join(OrderedDict.fromkeys(groupes)), "avatar": "",
            "age": "", "genre": "", "pays": PAYS_NOM.get(pays_code, ""), "label": fonction,
            "origine": "", "religion": "", "situation": "", "caractere": "", "langage": "",
            "activite": p.get("role", ""), "observations": "",
            "qualifications": "Source bio : Réseau RZO (MINOTAURE 26)",
            "aime": "", "deteste": "",
        }
        lignes.append(ligne)
        par_nom[k] = ligne
        ajouts += 1
    return ajouts, fusions


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
    from collections import Counter
    lignes, stats = construire()
    ajouts_rzo, fusions_rzo = fusionner_rzo(lignes, A7_RZO)
    ecrire(lignes)
    print("Fichier : %s" % SORTIE)
    print("Reseau RZO : %d fusionnes (deja presents) | %d nouvelles fiches" % (fusions_rzo, ajouts_rzo))
    print("Personas : %d" % len(lignes))
    for camp in ("rouge", "bleu", "neutre"):
        print("   %-12s %d" % (CAMP_LABEL[camp], sum(1 for l in lignes if l["camp"] == camp)))
    grp = Counter(g for l in lignes for g in l["groups"].split(";")
                  if g and not g.startswith("EXERCICE"))
    exo = Counter(g for l in lignes for g in l["groups"].split(";") if g.startswith("EXERCICE"))
    print("\nGroupes « PAYS - FONCTION » (%d) — un persona peut en cumuler plusieurs :" % len(grp))
    for k, v in sorted(grp.items(), key=lambda x: (-x[1], x[0])):
        print("   %-34s %3d" % (k, v))
    print("\nGroupes d'exercice :")
    for k, v in exo.most_common():
        print("   %-34s %3d" % (k, v))
    seuls = [k for k, v in grp.items() if v == 1]
    print("\nTotal groupes : %d | a 1 seul persona : %d %s"
          % (len(grp) + len(exo), len(seuls), seuls))
    print("moyenne de groupes par persona : %.1f"
          % (sum(len(l["groups"].split(";")) for l in lignes) / len(lignes)))
    print("Bios — EHO MINOTAURE : %(eho)d | registre MINOTAURE : %(note)d | "
          "registre MASTAURIGE/GUILLAUME : %(registre)d | CASW ORION : %(casw_bio)d | "
          "sans bio : %(sans_bio)d" % stats)
