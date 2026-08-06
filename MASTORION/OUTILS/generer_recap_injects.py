# -*- coding: utf-8 -*-
"""
generer_recap_injects.py — MINERVE / agent MASTORION
Produit un classeur Excel recapitulatif des INJECTS JOUES, un onglet par exercice :
   - onglet GUILLAUME  (AURIGE 2BB)
   - onglet MINOTAURE  (AURIGE 7BB)

Pour chaque inject : numero, nom (sujet), TYPE(S) DE PRODUIT (tweet, article,
tract, courrier...), description, date de jeu, etat, destinataires, LO, et le
detail des produits rattaches.

Sources (lecture seule) — outillage MASTAURIGE de chaque exercice :
  MELMIL/melmil_data.js         -> liste de reference des injects (code + sujet + desc + date + etat)
  MELMIL/melmil_inject_index.js -> 2BB : correspondance inject -> produits TYPES
  tweets_data.js                -> tweets (champ `num` = code inject)
  moteur/articles_data.js       -> 7BB : articles / tracts / courriers (champs `num`, `type`, `site`)

Usage :  python generer_recap_injects.py
"""
import io, os, re, json
from collections import OrderedDict, Counter

EXER = r"D:\CECPC\PRODUCTION\EXER"
A2 = os.path.join(EXER, r"AURIGE 2BB\00_Boites à outils\MASTAURIGE\WEB")
A7 = os.path.join(EXER, r"AURIGE 7BB\00_Boites à outils\MASTAURIGE\LOCALSTORAGE_WEB_VERSION")
SORTIE = r"D:\CECPC\PRODUCTION\IA\MINERVE\MASTORION\RECAPS\RECAP_INJECTS_GUILLAUME_MINOTAURE.xlsx"

COLS = ["numero", "nom", "types_de_produit", "nb_produits", "description",
        "date_de_jeu", "etat", "destinataires", "lo", "detail_des_produits"]

LIB_TYPE = {"tweet": "Tweet", "article": "Article", "tract": "Tract",
            "courrier": "Courrier", "document": "Document", "image": "Image",
            "communique": "Communiqué", "video": "Vidéo"}


def lire(p):
    return io.open(p, encoding="utf-8", errors="replace").read()


def sans_commentaires(txt):
    """Retire les commentaires JS (// et /* */) en preservant le contenu des chaines."""
    out, i, n = [], 0, len(txt)
    chaine = None
    while i < n:
        c = txt[i]
        if chaine:
            out.append(c)
            if c == "\\" and i + 1 < n:
                out.append(txt[i + 1]); i += 2; continue
            if c == chaine:
                chaine = None
            i += 1; continue
        if c in "\"'":
            chaine = c; out.append(c); i += 1; continue
        if c == "/" and i + 1 < n and txt[i + 1] == "/":
            while i < n and txt[i] != "\n":
                i += 1
            continue
        if c == "/" and i + 1 < n and txt[i + 1] == "*":
            fin = txt.find("*/", i + 2)
            i = n if fin < 0 else fin + 2
            continue
        out.append(c); i += 1
    return "".join(out)


def quoter_cles(txt):
    """Met des guillemets autour des clefs d'objet non quotees (2BB : {code: "..."}).
    Les chaines sont preservees telles quelles."""
    out, i, n = [], 0, len(txt)
    chaine = None
    while i < n:
        c = txt[i]
        if chaine:
            out.append(c)
            if c == "\\" and i + 1 < n:
                out.append(txt[i + 1]); i += 2; continue
            if c == chaine:
                chaine = None
            i += 1; continue
        if c in "\"'":
            chaine = c; out.append('"' if c == "'" else c); i += 1; continue
        m = re.match(r"([A-Za-z_$][\w$]*)(\s*):", txt[i:])
        if m and out and re.search(r"[{,]\s*$", "".join(out[-40:])):
            out.append('"%s"%s:' % (m.group(1), m.group(2)))
            i += m.end(); continue
        out.append(c); i += 1
    return "".join(out)


def charger_js(path, variable, ouvrant):
    """Charge la valeur JSON affectee a `variable` dans un fichier .js."""
    txt = quoter_cles(sans_commentaires(lire(path)))
    m = re.search(r"\b(?:var|let|const)\s+%s\s*=\s*" % re.escape(variable), txt)
    if not m:
        return None
    debut = txt.index(ouvrant, m.end())
    valeur, _ = json.JSONDecoder().raw_decode(txt[debut:])
    return valeur


def melmil(path):
    d = charger_js(path, "MELMIL_DATA", "{")
    return (d or {}).get("injections", [])


def tweets(path):
    return charger_js(path, "MASTAURIGE_TWEETS", "[") or []


def articles(path):
    return charger_js(path, "MASTAURIGE_ARTICLES", "[") or []


def index_2bb(path):
    """MASTAURIGE_INDEX du 2BB : { "07.01.04Bi": [ {key,type,label}, ... ] }
    Ecrit en JS (clefs non quotees dans les objets) -> extraction par regex."""
    txt = sans_commentaires(lire(path))
    res = OrderedDict()
    for mcode in re.finditer(r'"([0-9]{2}\.[0-9]{2}\.[^"]+)"\s*:\s*\[', txt):
        code = mcode.group(1)
        prof, i, n = 1, mcode.end(), len(txt)
        while i < n and prof:
            prof += (txt[i] == "[") - (txt[i] == "]")
            i += 1
        bloc = txt[mcode.end():i - 1]
        produits = []
        for mo in re.finditer(r"\{[^{}]*\}", bloc):
            o = mo.group(0)
            t = re.search(r'type\s*:\s*"([^"]*)"', o)
            l = re.search(r'label\s*:\s*"([^"]*)"', o)
            k = re.search(r'key\s*:\s*"([^"]*)"', o)
            produits.append({"type": (t.group(1) if t else "").lower(),
                             "label": l.group(1) if l else (k.group(1) if k else "")})
        res.setdefault(code, []).extend(produits)
    return res


def noms_depuis_commentaires(path):
    """index_master.html porte des commentaires  <!-- 07.04.07Ci — libelle — date -->
    qui nomment les injects. Sert de secours quand le code manque dans MELMIL."""
    noms = {}
    if not os.path.exists(path):
        return noms
    for m in re.finditer(r"<!--\s*(\d{2}\.\d{2}\.[^\s—–-]+)\s*[—–-]\s*(.+?)\s*-->", lire(path)):
        code, libelle = m.group(1).strip(), re.sub(r"\s+", " ", m.group(2)).strip()
        libelle = re.sub(r"\s*[—–-]\s*\d{1,2}\s*(Jun|Jan|mai|juin|Juin|h\d).*$", "", libelle).strip()
        # retire un prefixe de type/source : "ARTICLE TM — ", "TWEET — ", "ZUBRRADIO.FM — "
        sans_prefixe = re.sub(r"^(ARTICLE|TWEET|TRACT|COURRIER|DOCUMENT|VIDEO|[A-Z0-9\.]{2,12})\s*"
                              r"(?:[A-Z0-9]{1,10}\s*)?[—–-]\s*", "", libelle)
        if len(sans_prefixe) > 12:
            libelle = sans_prefixe.strip()
        for cle in (code, racine(code)):
            if libelle and len(libelle) > len(noms.get(cle, "")):
                noms[cle] = libelle
    return noms


def racine(code):
    """Code d'inject parent : 07.01.04Bi -> 07.01.04i ; 07.02.I08B -> 07.02.I08."""
    c = (code or "").strip()
    m = re.match(r"^(\d{2}\.\d{2}\.\d{2,3})[A-Za-z]?i$", c)          # ancien format
    if m:
        return m.group(1) + "i"
    m = re.match(r"^(\d{2}\.\d{2}\.[Ii]\d{1,3})[A-Za-z]?$", c)        # format JEMM
    if m:
        return m.group(1)
    return c


def collecter(nom_exercice, chemin, mode):
    injects = OrderedDict()
    noms_secours = noms_depuis_commentaires(os.path.join(chemin, "index_master.html"))

    for inj in melmil(os.path.join(chemin, "MELMIL", "melmil_data.js")):
        code = (inj.get("code") or "").strip()
        if not code:
            continue
        injects[code] = {"numero": code, "nom": inj.get("sujet", ""),
                         "description": re.sub(r"\s+", " ", inj.get("desc", "") or "").strip(),
                         "date_de_jeu": (inj.get("date") or "").replace("T", " "),
                         "etat": inj.get("etat", ""), "destinataires": inj.get("dest", ""),
                         "produits": [], "lo": set()}

    def rattacher(code, type_produit, libelle, lo=None):
        cible = code if code in injects else racine(code)
        fiche = injects.get(cible)
        if fiche is None:
            fiche = injects.setdefault(cible, {
                "numero": cible,
                "nom": noms_secours.get(cible) or noms_secours.get(code) or "(nom non renseigné)",
                "description": "", "date_de_jeu": "", "etat": "",
                "destinataires": "⚠ hors matrice MELMIL",
                "produits": [], "lo": set()})
        fiche["produits"].append((type_produit, libelle, code))
        for x in (lo or []):
            fiche["lo"].add(str(x))

    # --- tweets (les deux exercices)
    f_tweets = os.path.join(chemin, "tweets_data.js")
    if not os.path.exists(f_tweets):
        f_tweets = os.path.join(chemin, "moteur", "tweets_data.js")
    for t in tweets(f_tweets):
        libelle = "%s — %s" % (t.get("handle", ""), re.sub(r"\s+", " ", (t.get("text") or ""))[:90])
        rattacher((t.get("num") or "").strip(), "tweet", libelle.strip(" —"), t.get("lo"))

    if mode == "7bb":
        # --- articles / tracts / courriers portes par articles_data.js
        for a in articles(os.path.join(chemin, "moteur", "articles_data.js")):
            t = (a.get("type") or a.get("site") or "article").lower()
            if t not in LIB_TYPE:
                t = {"tract": "tract", "courrier": "courrier"}.get((a.get("site") or "").lower(), "article")
            rattacher((a.get("num") or "").strip(), t,
                      re.sub(r"\s+", " ", a.get("title") or a.get("file") or ""), a.get("lo"))
    else:
        # --- 2BB : produits types par l'index MELMIL -> cards
        for code, produits in index_2bb(os.path.join(chemin, "MELMIL", "melmil_inject_index.js")).items():
            for p in produits:
                if p["type"] == "tweet":
                    continue           # deja couvert par tweets_data.js (evite les doublons)
                rattacher(code, p["type"] or "article", p["label"])

    # dernier recours : nommer l'inject par le libelle de son 1er produit
    for f in injects.values():
        if f["nom"] in ("", "(nom non renseigné)") and f["produits"]:
            libelle = f["produits"][0][1]
            if len(libelle) > 12:
                f["nom"] = libelle[:90]

    lignes = []
    for code, f in injects.items():
        compte = Counter(t for t, _, _ in f["produits"])
        types = " + ".join("%s%s" % (LIB_TYPE.get(t, t.capitalize()),
                                     " x%d" % n if n > 1 else "")
                           for t, n in compte.most_common())
        detail = " | ".join("[%s] %s%s" % (LIB_TYPE.get(t, t), lib,
                                           "" if c == code else " (%s)" % c)
                            for t, lib, c in f["produits"])
        lignes.append({
            "numero": code, "nom": f["nom"],
            "types_de_produit": types or "— aucun produit —",
            "nb_produits": len(f["produits"]),
            "description": f["description"][:900],
            "date_de_jeu": f["date_de_jeu"], "etat": f["etat"],
            "destinataires": f["destinataires"],
            "lo": ", ".join("LO%s" % x for x in sorted(f["lo"])),
            "detail_des_produits": detail[:1200],
        })

    def cle(l):
        m = re.match(r"(\d{2})\.(\d{2})\.[Ii]?(\d+)", l["numero"])
        return (int(m.group(1)), int(m.group(2)), int(m.group(3)), l["numero"]) if m else (99, 99, 99, l["numero"])
    lignes.sort(key=cle)
    return lignes


def ecrire(feuilles):
    from openpyxl import Workbook
    from openpyxl.styles import Font, PatternFill, Alignment
    from openpyxl.utils import get_column_letter
    os.makedirs(os.path.dirname(SORTIE), exist_ok=True)
    wb = Workbook(); wb.remove(wb.active)
    couleurs = {"GUILLAUME": "1565C0", "MINOTAURE": "6A1B9A"}
    for nom, lignes in feuilles.items():
        ws = wb.create_sheet(nom)
        ws.append([c.replace("_", " ").upper() for c in COLS])
        for i in range(1, len(COLS) + 1):
            cel = ws.cell(row=1, column=i)
            cel.font = Font(bold=True, color="FFFFFF")
            cel.fill = PatternFill("solid", fgColor=couleurs.get(nom, "37474F"))
            cel.alignment = Alignment(horizontal="center", vertical="center")
        for l in lignes:
            ws.append([l[c] for c in COLS])
        ws.freeze_panes = "C2"
        ws.auto_filter.ref = "A1:%s%d" % (get_column_letter(len(COLS)), ws.max_row)
        largeurs = {"numero": 14, "nom": 46, "types_de_produit": 26, "nb_produits": 8,
                    "description": 70, "date_de_jeu": 17, "etat": 12,
                    "destinataires": 24, "lo": 12, "detail_des_produits": 80}
        for i, c in enumerate(COLS, 1):
            ws.column_dimensions[get_column_letter(i)].width = largeurs[c]
        for r in range(2, ws.max_row + 1):
            ws.cell(row=r, column=5).alignment = Alignment(wrap_text=False, vertical="top")
    wb.save(SORTIE)


if __name__ == "__main__":
    feuilles = OrderedDict()
    feuilles["GUILLAUME"] = collecter("GUILLAUME (AURIGE 2BB)", A2, "2bb")
    feuilles["MINOTAURE"] = collecter("MINOTAURE (AURIGE 7BB)", A7, "7bb")
    ecrire(feuilles)
    print("Fichier : %s\n" % SORTIE)
    for nom, lignes in feuilles.items():
        avec = [l for l in lignes if l["nb_produits"]]
        print("Onglet %-10s %3d injects | %3d avec produit | %3d sans | %3d produits au total"
              % (nom, len(lignes), len(avec), len(lignes) - len(avec),
                 sum(l["nb_produits"] for l in lignes)))
        c = Counter()
        for l in lignes:
            for t in re.findall(r"([A-Za-zé]+)(?: x(\d+))?", l["types_de_produit"]):
                if t[0] in LIB_TYPE.values():
                    c[t[0]] += int(t[1] or 1)
        print("        produits : " + ", ".join("%s %d" % (k, v) for k, v in c.most_common()))
        hors = [l["numero"] for l in lignes if "hors matrice" in l["destinataires"]]
        if hors:
            print("        ⚠ %d injects joues mais ABSENTS du socle MELMIL : %s"
                  % (len(hors), ", ".join(hors)))
        vides = [l["numero"] for l in lignes if not l["nb_produits"]]
        if vides:
            print("        ⓘ injects MELMIL sans produit MASTAURIGE : %s" % ", ".join(vides))
