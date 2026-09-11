# -*- coding: utf-8 -*-
"""
generer_annuaire_visuel.py — MINERVE / agent MASTORION
Produit un classeur Excel de CONSULTATION (≠ import MASTORION) : un annuaire
des 248 personas mis en forme pour la lecture humaine — filtres natifs,
code couleur par camp et par pays, tableau de bord avec graphiques.

Reutilise EXACTEMENT les donnees de generer_bibliotheque.construire() (meme
audit, memes corrections des 4 agents-experts, Titane deja ramene sous MER)
-> les deux fichiers restent rigoureusement coherents, aucune double saisie.

Usage :  python generer_annuaire_visuel.py
"""
import os
import sys
from collections import Counter

sys.path.insert(0, os.path.dirname(__file__))
import generer_bibliotheque as G

SORTIE = r"D:\CECPC\PRODUCTION\IA\MINERVE\MASTORION\RECAPS\ANNUAIRE_PERSONAS.xlsx"

CAMP_STYLE = {
    "rouge":  {"nom": "Rouge",  "fill": "F8D7DA", "font": "842029"},
    "bleu":   {"nom": "Bleu",   "fill": "CFE2FF", "font": "084298"},
    "neutre": {"nom": "Neutre", "fill": "E2E3E5", "font": "41464B"},
}

# Palette par pays — clin d'oeil aux chartes graphiques MINERVE existantes
# (Mercure = rouge sovietique, Arnland/DR = bleu nordique)
PAYS_STYLE = {
    "Mercure":  {"fill": "F5C2C7", "font": "58151C"},
    "Arnland":  {"fill": "B6D4F0", "font": "0A3866"},
    "France":   {"fill": "D6C6EC", "font": "3B1E6B"},
    "Bothnia":  {"fill": "B8E2DA", "font": "0F5C4E"},
    "":         {"fill": "E9ECEF", "font": "495057"},   # transverse (ONG, UE, animation...)
}

TRANSVERSE = {"ONG", "INSTITUTION INTERNATIONALE", "MEDIA INTERNATIONAL",
              "OTAN", "UE", "ANIMATION EXERCICE"}


def preparer(lignes):
    """Deplie chaque persona en une ligne d'annuaire lisible."""
    out = []
    for l in lignes:
        tous = [g for g in str(l["groups"]).split(";") if g]
        exercices = [g.replace("EXERCICE ", "") for g in tous if g.startswith("EXERCICE ")]
        fonctions = [g for g in tous if not g.startswith("EXERCICE ")]
        out.append({
            "camp": l["camp"],
            "pays": l["pays"] or "",
            "handle": "@" + l["username"],
            "nom": l["display_name"],
            "groupes": ", ".join(fonctions),
            "exercices": ", ".join(sorted(exercices)) if exercices else "—",
            "age": l["age"] or "",
            "genre": l["genre"] or "",
            "role": l["activite"] or l["label"] or "",
            "source_bio": str(l["qualifications"]).replace("Source bio : ", ""),
            "bio": (l["bio"] or "")[:220],
        })
    out.sort(key=lambda d: (d["pays"] or "\uffff", d["camp"], d["nom"]))
    return out


def construire_dashboard(ws, lignes):
    from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
    from openpyxl.chart import BarChart, Reference
    from openpyxl.chart.label import DataLabelList

    ws.sheet_view.showGridLines = False
    ws.column_dimensions["A"].width = 3

    titre = ws.cell(row=2, column=2, value="ANNUAIRE DES PERSONAS — MINERVE / MASTORION")
    titre.font = Font(size=20, bold=True, color="1B1B1B")
    sous = ws.cell(row=3, column=2,
                    value="Fusion GUILLAUME 2BB · MINOTAURE 26 · ORION 26 — audité par les agents MINERVE le 2026-07-28")
    sous.font = Font(size=11, italic=True, color="6C757D")

    # ── tuiles KPI ──
    total = len(lignes)
    par_camp = Counter(l["camp"] for l in lignes)
    par_pays = Counter(l["pays"] for l in lignes if l["pays"])
    nb_pays = len(par_pays)
    nb_groupes = len({g for l in lignes for g in str(l["groups"]).split(";")
                      if g and not g.startswith("EXERCICE")})

    tuiles = [
        ("PERSONAS", str(total), "212529", "E9ECEF"),
        ("PAYS REPRÉSENTÉS", str(nb_pays), "0A3866", "B6D4F0"),
        ("GROUPES", str(nb_groupes), "3B1E6B", "D6C6EC"),
        ("🔴 ROUGE", str(par_camp.get("rouge", 0)), "842029", "F8D7DA"),
        ("🔵 BLEU", str(par_camp.get("bleu", 0)), "084298", "CFE2FF"),
        ("⚪ NEUTRE", str(par_camp.get("neutre", 0)), "41464B", "E2E3E5"),
    ]
    col = 2
    for label, valeur, fcol, bgcol in tuiles:
        for r in (5, 6):
            c = ws.cell(row=r, column=col)
            c.fill = PatternFill("solid", fgColor=bgcol)
        vc = ws.cell(row=5, column=col, value=valeur)
        vc.font = Font(size=22, bold=True, color=fcol)
        vc.alignment = Alignment(horizontal="center", vertical="center")
        lc = ws.cell(row=6, column=col, value=label)
        lc.font = Font(size=9, bold=True, color=fcol)
        lc.alignment = Alignment(horizontal="center", vertical="center")
        ws.merge_cells(start_row=5, start_column=col, end_row=5, end_column=col + 1)
        ws.merge_cells(start_row=6, start_column=col, end_row=6, end_column=col + 1)
        col += 2

    # ── tableaux de donnees (source des graphiques), pousses hors vue ──
    ws.cell(row=9, column=2, value="Répartition par pays").font = Font(bold=True, size=12)
    r0 = 10
    for i, (pays, n) in enumerate(sorted(par_pays.items(), key=lambda x: -x[1])):
        ws.cell(row=r0 + i, column=2, value=pays)
        ws.cell(row=r0 + i, column=3, value=n)
    fin_pays = r0 + len(par_pays)

    ws.cell(row=9, column=6, value="Répartition par exercice").font = Font(bold=True, size=12)
    par_exo = Counter(g.replace("EXERCICE ", "") for l in lignes
                       for g in str(l["groups"]).split(";") if g.startswith("EXERCICE "))
    for i, (exo, n) in enumerate(sorted(par_exo.items(), key=lambda x: -x[1])):
        ws.cell(row=r0 + i, column=6, value=exo)
        ws.cell(row=r0 + i, column=7, value=n)
    fin_exo = r0 + len(par_exo)

    chart1 = BarChart()
    chart1.type, chart1.style = "col", 10
    chart1.title = "Personas par pays"
    chart1.y_axis.title, chart1.x_axis.title = "Nombre", None
    data = Reference(ws, min_col=3, min_row=r0, max_row=fin_pays - 1)
    cats = Reference(ws, min_col=2, min_row=r0, max_row=fin_pays - 1)
    chart1.add_data(data, titles_from_data=False)
    chart1.set_categories(cats)
    chart1.legend = None
    chart1.dLbls = DataLabelList(); chart1.dLbls.showVal = True
    chart1.width, chart1.height = 13, 8
    ws.add_chart(chart1, "B18")

    chart2 = BarChart()
    chart2.type, chart2.style = "col", 11
    chart2.title = "Personas par exercice"
    data2 = Reference(ws, min_col=7, min_row=r0, max_row=fin_exo - 1)
    cats2 = Reference(ws, min_col=6, min_row=r0, max_row=fin_exo - 1)
    chart2.add_data(data2, titles_from_data=False)
    chart2.set_categories(cats2)
    chart2.legend = None
    chart2.dLbls = DataLabelList(); chart2.dLbls.showVal = True
    chart2.width, chart2.height = 13, 8
    ws.add_chart(chart2, "J18")

    note = ws.cell(row=36, column=2,
                    value="→ Onglet « Annuaire » : cliquer les flèches d'en-tête pour filtrer "
                          "(ex. Pays = Mercure, ou Exercice contient MINOTAURE).")
    note.font = Font(italic=True, size=10, color="6C757D")


def construire_annuaire(ws, rows):
    from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
    from openpyxl.worksheet.table import Table, TableStyleInfo
    from openpyxl.formatting.rule import FormulaRule
    from openpyxl.utils import get_column_letter

    entetes = ["Camp", "Pays", "Handle", "Nom affiché", "Groupe(s)", "Exercice(s)",
               "Âge", "Genre", "Rôle / activité", "Source bio", "Aperçu biographie"]
    ws.append(entetes)
    for l in rows:
        ws.append([CAMP_STYLE[l["camp"]]["nom"], l["pays"] or "—", l["handle"], l["nom"],
                   l["groupes"], l["exercices"], l["age"], l["genre"], l["role"],
                   l["source_bio"], l["bio"]])

    n = ws.max_row
    largeurs = {1: 10, 2: 11, 3: 22, 4: 24, 5: 34, 6: 22, 7: 7, 8: 10,
                9: 20, 10: 24, 11: 65}
    for i, w in largeurs.items():
        ws.column_dimensions[get_column_letter(i)].width = w

    tbl = Table(displayName="Annuaire", ref="A1:K%d" % n)
    tbl.tableStyleInfo = TableStyleInfo(name="TableStyleMedium2", showRowStripes=True,
                                        showFirstColumn=False, showLastColumn=False)
    ws.add_table(tbl)

    ws.freeze_panes = "C2"
    for c in range(1, 12):
        cel = ws.cell(row=1, column=c)
        cel.font = Font(bold=True, color="FFFFFF")
        cel.fill = PatternFill("solid", fgColor="343A40")
        cel.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    ws.row_dimensions[1].height = 30
    for r in range(2, n + 1):
        ws.cell(row=r, column=11).alignment = Alignment(wrap_text=True, vertical="top")
        ws.cell(row=r, column=5).alignment = Alignment(wrap_text=True, vertical="top")
        ws.row_dimensions[r].height = 30

    # code couleur : Camp (colonne A) et Pays (colonne B)
    for camp, style in CAMP_STYLE.items():
        ws.conditional_formatting.add(
            "A2:A%d" % n,
            FormulaRule(formula=['$A2="%s"' % style["nom"]],
                       fill=PatternFill("solid", fgColor=style["fill"]),
                       font=Font(color=style["font"], bold=True)))
    for pays, style in PAYS_STYLE.items():
        if not pays:
            continue
        ws.conditional_formatting.add(
            "B2:B%d" % n,
            FormulaRule(formula=['$B2="%s"' % pays],
                       fill=PatternFill("solid", fgColor=style["fill"]),
                       font=Font(color=style["font"], bold=True)))
    fin_style = PatternFill("solid", fgColor=PAYS_STYLE[""]["fill"])
    ws.conditional_formatting.add(
        "B2:B%d" % n, FormulaRule(formula=['$B2="—"'], fill=fin_style))


def construire_legende(ws):
    from openpyxl.styles import Font, PatternFill, Alignment
    ws.sheet_view.showGridLines = False
    ws.column_dimensions["A"].width = 3
    ws.column_dimensions["B"].width = 22
    ws.column_dimensions["C"].width = 60
    ws.cell(row=2, column=2, value="LÉGENDE").font = Font(size=16, bold=True)

    ws.cell(row=4, column=2, value="Camps").font = Font(bold=True, size=12)
    r = 5
    for camp, style in CAMP_STYLE.items():
        c = ws.cell(row=r, column=2, value=style["nom"])
        c.fill = PatternFill("solid", fgColor=style["fill"])
        c.font = Font(color=style["font"], bold=True)
        c.alignment = Alignment(horizontal="center")
        desc = {"rouge": "Camp Mercure — sert au ciblage des likes/retweets synthétiques",
                "bleu": "Camp OTAN / Arnland officiel",
                "neutre": "Comptes neutres, ONG, médias non alignés"}[camp]
        ws.cell(row=r, column=3, value=desc).font = Font(italic=True, size=10)
        r += 1

    r += 1
    ws.cell(row=r, column=2, value="Pays").font = Font(bold=True, size=12)
    r += 1
    for pays, style in PAYS_STYLE.items():
        if not pays:
            continue
        c = ws.cell(row=r, column=2, value=pays)
        c.fill = PatternFill("solid", fgColor=style["fill"])
        c.font = Font(color=style["font"], bold=True)
        c.alignment = Alignment(horizontal="center")
        r += 1
    c = ws.cell(row=r, column=2, value="— (transverse)")
    c.fill = PatternFill("solid", fgColor=PAYS_STYLE[""]["fill"])
    c.alignment = Alignment(horizontal="center")
    ws.cell(row=r, column=3, value="ONG, institutions internationales, animation d'exercice…").font = \
        Font(italic=True, size=10)

    r += 3
    ws.cell(row=r, column=2, value="Comment filtrer").font = Font(bold=True, size=12)
    r += 1
    for txt in ["1. Aller dans l'onglet « Annuaire »",
                "2. Cliquer la flèche ▾ en haut de la colonne Pays (ou Exercice(s))",
                "3. Cocher ex. « Mercure » → seuls les comptes mercuriens s'affichent",
                "4. Combiner plusieurs filtres (Pays + Camp) pour croiser les critères"]:
        ws.cell(row=r, column=2, value=txt).font = Font(size=10)
        ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=4)
        r += 1


if __name__ == "__main__":
    from openpyxl import Workbook
    lignes, _ = G.construire()
    G.fusionner_rzo(lignes, G.A7_RZO)
    G.fusionner_planche(lignes, G.A7_PLANCHE)   # cartes ecrites en dur dans la planche EHO
    G.fusionner_delattre(lignes)                # reseau RENS DELATTRE 26
    rows = preparer(lignes)

    os.makedirs(os.path.dirname(SORTIE), exist_ok=True)
    wb = Workbook()
    wb.remove(wb.active)

    ws_dash = wb.create_sheet("Tableau de bord")
    construire_dashboard(ws_dash, lignes)

    ws_ann = wb.create_sheet("Annuaire")
    construire_annuaire(ws_ann, rows)

    ws_leg = wb.create_sheet("Légende")
    construire_legende(ws_leg)

    wb.active = 0
    wb.save(SORTIE)

    print("Fichier : %s" % SORTIE)
    print("Personas : %d" % len(rows))
    print("Onglets : Tableau de bord · Annuaire (avec filtres) · Légende")
