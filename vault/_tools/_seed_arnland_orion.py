# -*- coding: utf-8 -*-
"""
_seed_arnland_orion.py — sème le roster ARNLAND du théâtre ORION 26 O41 (HPoitou/HVienne).
Complète le seed principal (MINOTAURE/7BB). Tous HN = 🔵 bleu ; ONG/OI internationales = ⚪ neutre.
Kalugin/Mishin/Petrovna déjà créés (seed principal) → ignorés (idempotent).
Source : ANALYSTE/ARNLAND/MEMOIRE.md §B (ORION 26 O41). relevantFor : [arnland, orion].
"""
import os, datetime

VAULT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DST = os.path.join(VAULT, "entities", "personas")
TODAY = datetime.date.today().isoformat()
EMOJI = {"rouge": "🔴", "bleu": "🔵", "neutre": "⚪"}

FIG = [
    # Gouvernement (théâtre ORION)
    ("schmidt", "Daniel Schmidt", "Ministre de la Défense (ORION 26 O41)", "bleu", "orion-gouvernement"),
    ("fischer", "Aleksandr Fischer", "Ministre des Affaires étrangères (ORION 26 O41)", "bleu", "orion-gouvernement"),
    # Préfets
    ("karlson-erik", "Erik Karlson", "Préfet de la région HPoitou-Charente", "bleu", "orion-prefets"),
    ("ivanov-sergey", "Sergey Ivanov", "Préfet du département HVienne", "bleu", "orion-prefets"),
    ("lebedev", "Alexei Lebedev", "Préfet du département HCharente-Maritime", "bleu", "orion-prefets"),
    ("kulis", "Kulis", "Préfet du département HDeux-Sèvres", "bleu", "orion-prefets"),
    # Maires
    ("hoffmann", "Olena Hoffmann", "Maire de HPoitiers", "bleu", "orion-maires"),
    ("steiner", "Dimitri Steiner", "Maire de HSaint-Maixent", "bleu", "orion-maires"),
    # Militaires (secteurs / DMD)
    ("alvarez", "Erik Alvarez", "Commandant du 5e Secteur HPoitiers", "bleu", "orion-militaire"),
    ("kellerov", "Anton Kellerov", "Commandant de la 5e Brigade HAngoulême", "bleu", "orion-militaire"),
    ("bold", "Baltzar Bold", "Commandant de la Légion de Gendarmerie", "bleu", "orion-militaire"),
    ("kravchenko", "Nikolai Kravchenko", "DMD HVienne", "bleu", "orion-militaire"),
    ("chareyron", "Chareyron", "DMD HDeux-Sèvres (adjoint : Depoire)", "bleu", "orion-militaire"),
    ("depoire", "Depoire", "Adjoint DMD HDeux-Sèvres", "bleu", "orion-militaire"),
    ("fluxa", "Fluxa", "DMD HCharente-Maritime (adjoint : Laporte)", "bleu", "orion-militaire"),
    ("laporte", "Laporte", "Adjoint DMD HCharente-Maritime", "bleu", "orion-militaire"),
    # Police / Gendarmerie
    ("weiss", "Aleksandr Weiss", "Commandant Régional de Police", "bleu", "orion-police"),
    ("vogelnyk", "Katerina Vogelnyk", "Police HVienne", "bleu", "orion-police"),
    ("brandtsev", "Serhiy Brandtsev", "Police HDeux-Sèvres", "bleu", "orion-police"),
    ("steinbeck", "Konrad Steinbeck", "Gendarmeria Poitou", "bleu", "orion-police"),
    ("havrylenko", "Lukas Havrylenko", "Gendarmerie HVienne", "bleu", "orion-police"),
    ("kermovant", "Kermovant", "Gendarmerie HDeux-Sèvres", "bleu", "orion-police"),
    ("kostich", "Jannik Kostich", "ALC HCharente-Maritime", "bleu", "orion-police"),
    ("kovalenko-viktor", "Viktor Kovalenko", "Responsable de prison", "bleu", "orion-police"),
    # ONG / OI
    ("sokolova-anastasia", "Anastasia Sokolova", "UNOCHA (coordination humanitaire ONU)", "neutre", "orion-ong"),
    ("iliev", "Marko Iliev", "Porte-parole UNHCR (réfugiés ONU)", "neutre", "orion-ong"),
    ("korolev", "Alexandr Korolev", "NGO ISC", "neutre", "orion-ong"),
    ("ivanovitch", "Viktor Ivanovitch", "CultarNGO (biens culturels)", "neutre", "orion-ong"),
    ("steinbach-viktor", "Viktor Steinbach", "ACDA — Arnland Civil Defence Agency (HN)", "bleu", "orion-ong"),
    ("voldyski", "Markus Voldyski", "AISA — agence de sécurité arnish (HN ; examen 5G Dushman)", "bleu", "orion-ong"),
]


def main():
    os.makedirs(DST, exist_ok=True)
    created = skipped = 0
    for slug, nom, role, camp, cat in FIG:
        path = os.path.join(DST, "ENT-%s.md" % slug)
        if os.path.exists(path):
            skipped += 1
            continue
        body = (
            "---\n"
            "id: ENT-%s\n" % slug +
            "type: entity\n"
            "title: %s\n" % nom +
            "tags: [arnland, persona, orion, %s]\n" % cat +
            "source: ../../../ANALYSTE/ARNLAND/MEMOIRE.md\n"
            "linkedTo: [ENT-arnland]\n"
            "relevantFor: [arnland, orion]\n"
            "camp: %s\n" % camp +
            "pays: Arnland\n"
            "tier: 3\n"
            "created: %s\n" % TODAY +
            "updated: %s\n" % TODAY +
            "---\n\n"
            "# 👤 %s\n\n" % nom +
            "> camp %s **%s**. Rôle : %s.\n\n" % (EMOJI[camp], camp, role) +
            "> Théâtre **ORION 26 O41** (HPoitou/HVienne) — distinct du théâtre AURIGE 7BB (HLorraine).\n\n"
            "## 🔗 Source de vérité\n"
            "[[../../../ANALYSTE/ARNLAND/MEMOIRE.md]] §B (ORION 26 O41). Pays : [[ENT-arnland]].\n"
        )
        open(path, "w", encoding="utf-8").write(body)
        created += 1
    print("seed Arnland ORION O41 : %d créées, %d déjà présentes" % (created, skipped))


if __name__ == "__main__":
    main()
