# -*- coding: utf-8 -*-
"""
_seed_bothnia.py — sème (une fois) les entités Bothnia restantes (officiers, cabinet,
gouverneurs, partis, justice/sécurité, Leading Figures). Toutes ⚪ neutre sauf annoté.
IDEMPOTENT : ne réécrit jamais une note existante (préserve les éditions à la main).
Source de vérité : ANALYSTE/BOTHNIA/MEMOIRE.md. Après : lancer build.py.
"""
import os, datetime

VAULT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DST = os.path.join(VAULT, "entities", "personas")
TODAY = datetime.date.today().isoformat()
EMOJI = {"rouge": "🔴", "bleu": "🔵", "neutre": "⚪"}

# (slug, nom, rôle, camp, catégorie)
FIG = [
    # Commandement militaire (BNDF)
    ("palmquetil", "Tony Palmquetil", "Général — CHOD, chef d'état-major des armées (logisticien ; réformes pro-MER, interopérabilité Mercure)", "neutre", "militaire"),
    ("brrouette", "Leonard Brrouette", "Général — Chef du Commandement des opérations (guerre hybride)", "neutre", "militaire"),
    ("breesson", "Josef Breesson", "Général — CEM Armée de terre (blindés, école traditionnelle)", "neutre", "militaire"),
    ("malmsten", "Anders Malmsten", "Vice-amiral — CEM Marine (flotte du Nord, surveillance côtière)", "neutre", "militaire"),
    ("uhlmensch", "Vensel Uhlmensch", "Lt-général — CEM Armée de l'air (drones, DCA, pro-techno)", "neutre", "militaire"),
    ("lindquist", "Kevin Lindquist", "Lt-général — Directeur du renseignement de défense (DIA, cyber offensif)", "neutre", "militaire"),
    ("gradholm", "Malte Gradholm", "Lt-général — Commandant des Gardes-frontières (populaire terrain)", "neutre", "militaire"),
    ("rosenquist", "Wilhelm Rosenquist", "Major-général — Directeur de la Défense civile (résilience)", "neutre", "militaire"),
    ("pierrinen", "Niampsa Pierrinen", "Général — Chef de l'armée de terre (province Kaina)", "neutre", "militaire"),
    ("kosmannen", "Teemu Kosmannen", "Lt-général — Cdt Préparation opérationnelle (innovation, réformateur)", "neutre", "militaire"),
    ("koho", "Harri Koho", "Lt-général — Cdt Défense territoriale (réservistes, défense en profondeur)", "neutre", "militaire"),
    ("groop", "Tyko Groop", "Lt-général — Cdt Soutien (logistique)", "neutre", "militaire"),
    ("koivisto", "Koivisto", "Général — Air Corps Command", "neutre", "militaire"),
    # Cabinet (compléments)
    ("thulin", "Dr Leopold Thulin", "Ministre de l'Éducation", "neutre", "cabinet"),
    ("rylander", "Quirin Rylander", "Ministre des Finances", "neutre", "cabinet"),
    ("buerger", "Dr Cecilia Buerger", "Ministre de la Santé", "neutre", "cabinet"),
    ("bruske", "Sven Bruske", "Ministre des Transports", "neutre", "cabinet"),
    ("zeelen", "Maryam Zeelen", "Ministre du Travail", "neutre", "cabinet"),
    ("weber-dorit", "Dorit Weber", "Ministre de l'Environnement", "neutre", "cabinet"),
    ("thinnes", "Edric Thinnes", "Ministre du Développement national", "neutre", "cabinet"),
    ("amin", "Nero Amin", "Ministre de l'Information & des Communications", "neutre", "cabinet"),
    ("adam", "Lisa Adam", "Ministre du Commerce & de l'Industrie", "neutre", "cabinet"),
    ("muller-aiko", "Dr Aiko Müller", "Ministre de la Culture", "neutre", "cabinet"),
    ("strutz", "Prof. Veronika Strutz", "Ministre de la Justice", "neutre", "cabinet"),
    ("dewaele", "Patrick De Waele", "Ministre Dév. communautaire / Jeunesse / Sports", "neutre", "cabinet"),
    # Gouverneurs régionaux (compléments)
    ("anders-lorentz", "Lorentz Anders", "Gouverneur de Braheland (loyal à Peters)", "neutre", "regions"),
    ("erik-petra", "Petra Erik", "Gouverneur de Belluxa (loyale à Peters)", "neutre", "regions"),
    ("madsen-freja", "Freja Madsen", "Gouverneur de Bområde (loyale à Peters)", "neutre", "regions"),
    # Partis (échiquier domestique)
    ("jansen", "Ingo Jansen", "Chef de l'opposition — BNP (centre-droit conservateur, 52/171)", "neutre", "partis"),
    ("kramer", "Anna Kramer", "Cheffe du LPB (Liberal Party, gauche modérée)", "neutre", "partis"),
    ("bryl", "Palina Bryl", "Cheffe de Green Bothnia (écologiste, non représenté)", "neutre", "partis"),
    ("shauchenka", "Yan Shauchenka", "Chef du BDP (extrême gauche)", "neutre", "partis"),
    ("lapitski", "Marina Lapitski", "Cheffe de l'AFB (Alliance for the Future of Bothnia, extrême droite)", "neutre", "partis"),
    # Justice & contrôle
    ("novik", "Siarhei Novik", "Cour suprême — administratif", "neutre", "justice"),
    ("ivanouski", "Yauhen Ivanouski", "Cour suprême — économique", "neutre", "justice"),
    ("sokal", "Vassilina Sokal", "Central Auditing Office", "neutre", "justice"),
    ("turchyn", "Anton Turchyn", "Ombudsperson (BOB)", "neutre", "justice"),
    ("dubrouski", "Mikalai Dubrouski", "Anti-corruption (CPIB)", "neutre", "justice"),
    ("tsikhanouski", "Ihar Tsikhanouski", "Chancelier de Justice", "neutre", "justice"),
    # Police & renseignement
    ("richter", "Ann Richter", "Commissaire national de la Police", "neutre", "securite"),
    ("rynkevich", "Halina Rynkevich", "NSS — sécurité nationale", "neutre", "securite"),
    ("radzivil", "Valery Radzivil", "NSA — signals intelligence", "neutre", "securite"),
    ("astapenka", "Alyaksei Astapenka", "CCB — cybersécurité", "neutre", "securite"),
    # Annexe « Leading Figures »
    ("nielsen-kasper", "Kasper Nielsen", "SCO — Skolkan Cooperation Organisation", "neutre", "leading"),
    ("pedersen-anders", "Anders Pedersen", "SSTO — Skolkan Security Treaty Organisation", "neutre", "leading"),
    ("madsen-ida", "Ida Madsen", "SFTA", "neutre", "leading"),
    ("andersen-line", "Line Andersen", "SIA", "neutre", "leading"),
    ("rosendaal", "Oliver Rosendaal", "CBE — patronat", "neutre", "leading"),
    ("bohler", "Erika Bohler", "NTUC — syndicats", "neutre", "leading"),
    ("jensen-niels", "Niels Jensen", "Fédération des fermiers", "neutre", "leading"),
    ("maes", "Dries Maes", "RAFB — anti-radicalisation", "neutre", "leading"),
    ("declercq", "Annelies de Clercq", "FARO — patrimoine", "neutre", "leading"),
    ("pavlenko-nikolai", "Nikolai Pavlenko", "AAG — Affirmative Action Group", "neutre", "leading"),
    ("sokolova-natalia", "Natalia Sokolova", "BFR — Bothnian Free Radicals", "neutre", "leading"),
    ("horby", "Tor Horby", "Magnat des médias (Horby Holdings)", "neutre", "leading"),
    ("kalenik", "Dmitri Kalenik", "Juriste — droits humains", "neutre", "leading"),
    ("baradzin", "Sviatlana Baradzin", "Juriste — pro-coopération avec Mercure", "rouge", "leading"),
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
            "tags: [bothnia, persona, %s]\n" % cat +
            "source: ../../../ANALYSTE/BOTHNIA/MEMOIRE.md\n"
            "linkedTo: [ENT-bothnia]\n"
            "relevantFor: [bothnia]\n"
            "camp: %s\n" % camp +
            "pays: Bothnia\n"
            "tier: 3\n"
            "created: %s\n" % TODAY +
            "updated: %s\n" % TODAY +
            "---\n\n"
            "# 👤 %s\n\n" % nom +
            "> camp %s **%s**. Rôle : %s.\n\n" % (EMOJI[camp], camp, role) +
            "## 🔗 Source de vérité\n"
            "[[../../../ANALYSTE/BOTHNIA/MEMOIRE.md]] (countrybook Bothnia). Pays : [[ENT-bothnia]].\n"
        )
        open(path, "w", encoding="utf-8").write(body)
        created += 1
    print("seed Bothnia : %d créées, %d déjà présentes" % (created, skipped))


if __name__ == "__main__":
    main()
