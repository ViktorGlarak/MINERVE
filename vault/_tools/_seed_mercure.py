# -*- coding: utf-8 -*-
"""
_seed_mercure.py — sème (une fois) le roster Mercure : gouvernement, haut commandement,
FGF-4 (= IV(MER)CORPS, l'adversaire de MINOTAURE 26), renseignement/justice, TANTALE,
opposition interne. Régime/militaire/TANTALE = 🔴 rouge ; opposition tolérée = ⚪ neutre.
DIFFÉRÉ : présidents régionaux, sous-directions Intérieur, reps OIG, groupes d'influence.
IDEMPOTENT. Source : ANALYSTE/MERCURE/MEMOIRE.md. (Olamao/Kaleva/Milanov = à la main.)
"""
import os, datetime

VAULT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DST = os.path.join(VAULT, "entities", "personas")
TODAY = datetime.date.today().isoformat()
EMOJI = {"rouge": "🔴", "bleu": "🔵", "neutre": "⚪"}

FIG = [
    # Gouvernement (Commissariat) — rouge
    ("junker", "Jonas Junker", "Ministre de la Défense — ex-maréchal de l'air + ex-chef d'EM, cercle intime Olamao", "rouge", "gouvernement"),
    ("ribiki", "Voichek Ribiki", "Ministre de l'Intérieur — ordre public, sécurité, infrastructure maritime", "rouge", "gouvernement"),
    ("stoph", "Dominic Stoph", "Ministre des Affaires étrangères — légitimation internationale", "rouge", "gouvernement"),
    ("erickson", "Josef Erickson", "Ministre de l'Économie / Finances — modèle d'économie dirigée", "rouge", "gouvernement"),
    ("muller-angela", "Angela Muller", "Ministre de l'Éducation — endoctrinement militaro-patriotique", "rouge", "gouvernement"),
    ("maizieree", "Sasha Maizierèe", "Ministre de la Santé — tutelle hôpitaux d'État", "rouge", "gouvernement"),
    ("vydra", "Marta Vydra", "Ministre de la Culture + Transport — MERCULT, patrimoine", "rouge", "gouvernement"),
    ("baumgartner", "Marc Baumgartner", "Ministre de l'Environnement", "rouge", "gouvernement"),
    ("gerlach", "Sabine Gerlach", "Ministre de la Justice", "rouge", "gouvernement"),
    ("grun", "Louise Grun", "Ministre de l'Information", "rouge", "gouvernement"),
    ("soucek", "Walter Soucek", "Ministre du Travail", "rouge", "gouvernement"),
    ("druey", "Ursula Druey", "Ministre de la Sécurité d'État", "rouge", "gouvernement"),
    # Haut commandement militaire — rouge
    ("numelin", "Fred Numelin", "Chef d'EM général (5 étoiles) — capacitaire & préparation opérationnelle", "rouge", "militaire"),
    ("rozman", "Rok Rozman", "Chef du Commandement des opérations", "rouge", "militaire"),
    ("sikorski", "Andrzej Sikorski", "Chef d'EM des forces terrestres", "rouge", "militaire"),
    ("lennartsson", "Sixten Lennartsson", "Chef d'EM de la Marine (amiral) — capacité expéditionnaire", "rouge", "militaire"),
    ("grabowski", "Rafal Grabowski", "Chef d'EM de la Force aérienne", "rouge", "militaire"),
    ("majcen", "Miha Majcen", "Chef des forces stratégiques (nucléaire)", "rouge", "militaire"),
    ("oblak", "Nik Oblak", "Chef du commandement SOF", "rouge", "militaire"),
    ("horvat", "Gregor Horvat", "Chef du service de santé des forces armées", "rouge", "militaire"),
    ("vostrikov", "Alexei Vostrikov", "Vice-amiral — chef flotte du Nord (Baltique)", "rouge", "militaire"),
    ("toti", "Paolo Toti", "Vice-amiral — chef flotte du Sud (Méditerranée)", "rouge", "militaire"),
    # FGF-L / FGF-4 — HVI (adversaire MINOTAURE 26) — rouge
    ("guierassimov", "Igor Guierassimov", "Général — cdt suprême FGF-L ; bras droit du Président ; instigateur de la doctrine InfoOps & déception MER", "rouge", "hvi"),
    ("andreev-boris", "Boris Andreev", "Lt-Général — cdt FGF-1 ; offensive blindée ; « InfoOps & deception freak » ; leads from the front", "rouge", "hvi"),
    ("abdoulaiev", "Sliman Abdoulaïev", "Lt-Général — cdt FGF-3 ; « tank tactics freak » ; surnommé « butcher of Syria » ; ex-conseiller du Président", "rouge", "hvi"),
    ("mizintsev", "Vladimir Mizintsev", "Lt-Général — cdt FGF-4 (IV(MER)CORPS, adversaire 7BB) ; pressenti futur cdt FGF-L ; « butcher of Syria » ; show off", "rouge", "hvi"),
    ("pruniere", "Thierry Prunière", "MG — CO 41 TANK DIV ; ⚠ cible 3I/HAUTE ; ambition politique, rivalité avec le cdt 42 MECH ; leads from the front ; lien familial avec le cdt 415 ARTY", "rouge", "hvi"),
    ("zhukov", "Mikhail Zhukov", "MG — CO 43 ABN DIV ; perte de popularité après une affaire fiscale (levier LO4) ; 30% non-PRO", "rouge", "hvi"),
    ("koulikov", "Gueorgy Koulikov", "MG — CO 42 MECH DIV ; très populaire ; rival de Prunière ; ascension rapide = jalousies", "rouge", "hvi"),
    ("sanders", "Ragnar Sanders", "BG — CO 415 ARTY BDE ; lien familial avec Prunière ; veuf (décès récent de son épouse — facteur déstabilisant)", "rouge", "hvi"),
    ("dvornikov", "Sergueï Dvornikov", "BG — CO 411 TANK BDE ; « golden card of the Corps » ; tactics freak", "rouge", "hvi"),
    ("matovnikov", "Aleksandr Matovnikov", "BG — CO 412 TANK BDE ; « POPOV's right-hand man » ; InfoOps freak ; trop sûr de lui", "rouge", "hvi"),
    ("kirillov", "Aleksandr Kirillov", "BG — CO 413 TANK BDE ; ne délègue pas ; harcèlement de son ex-femme (levier perso)", "rouge", "hvi"),
    ("popov", "Vladimir Popov", "BG — CO 414 MECH BDE ; co-auteur de la dernière doctrine MECH MER ; leads from the front", "rouge", "hvi"),
    ("mikhailovic", "Dimitri Mikhailovic", "Colonel — CO 410 TANK BN ; liens avec la milice TAN ; ex-officier de rens. en Bothnia ; tensions avec ses subordonnés", "rouge", "hvi"),
    ("maximov", "Pavel Maximov", "BG — CO 422 MECH BDE ; liens avec les autorités bothniennes (ex-LNO) ; PRO 40% seulement (point faible moral)", "rouge", "hvi"),
    ("gourka", "Sergueï Gourka", "BG — CO 421 MECH BDE ; champion d'échecs ; WIA 2007", "rouge", "hvi"),
    ("mikhelev", "Kristian Mikhelev", "BG — CO 423 TANK BDE ; OPSEC/rens. fort ; prudent ; peu réactif aux changements de plan", "rouge", "hvi"),
    ("kievov", "Slava Kievov", "BG — CO 425 ARTY BDE ; populaire ; veuf", "rouge", "hvi"),
    ("bielski", "Anton Bielski", "BG — CO 431 ABN BDE ; très résilient ; InfoOps & deception freak ; WIA 2008", "rouge", "hvi"),
    ("viktorovitch", "Vladimir Viktorovitch", "BG — CO 432 ABN BDE ; planification ABN détaillée ; soupçonné d'activités illégales (black business) ; a entraîné Kaleva (TANTALE)", "rouge", "hvi"),
    ("vassielvski", "Piotr Vassielvski", "BG — CO 433 ABN BDE ; chasse les technologies récentes ; veuf ; leads from the front", "rouge", "hvi"),
    ("julius", "Peter Julius", "MG — CO 11 TANK DIV (FGF-1) ; fidèle au régime ; imprudent avec ses hommes", "rouge", "hvi"),
    ("rasof", "Sergueï Rasof", "MG — CO 12 MECH DIV (FGF-1) ; très populaire ; leads from the front ; rivalité avec ses pairs", "rouge", "hvi"),
    ("gratchev", "Ievgueni Gratchev", "MG — CO 13 INF DIV (FGF-1) ; blessures multiples → condition médicale", "rouge", "hvi"),
    ("ivazov", "Ivan Ivazov", "MG — CO 31 MECH DIV (FGF-3) ; très populaire, résilient ; rivalité entre pairs", "rouge", "hvi"),
    # TANTALE (direction politique) — rouge
    ("werner", "Elias Werner", "Président de la milice TANTALE (paramilitaire pro-Olamao)", "rouge", "tantale"),
    ("vinogradov", "Moritz Vinogradov", "Porte-parole de TANTALE", "rouge", "tantale"),
    # Renseignement & justice — rouge (sauf critique du régime)
    ("soloviev", "Igor Soloviev", "MSS (Mercure Security Service) — renseignement intérieur", "rouge", "renseignement"),
    ("gusev", "Leonid Gusev", "FIS (Foreign Intelligence Service) — renseignement extérieur", "rouge", "renseignement"),
    ("denisov", "Ilya Denisov", "MIA (Military Intelligence Agency) — renseignement militaire", "rouge", "renseignement"),
    ("kaczmarek", "Bartosz Kaczmarek", "Avocat pro-régime", "rouge", "justice"),
    ("michalski", "Iwona Michalski", "Avocate de droit public — critique du régime", "neutre", "justice"),
    ("zajac", "Mateusz Zajac", "Juge à la Cour suprême (affaires administratives)", "rouge", "justice"),
    ("urban", "Wiktoria Urban", "Juge à la Cour suprême (affaires économiques)", "rouge", "justice"),
    # Opposition interne (tolérée, marginalisée) — neutre
    ("rossi", "Mikhaïl Rossi", "Président du Mercure Freedom Party (MFP)", "neutre", "opposition"),
    ("volkov-alessia", "Alessia Volkov", "Porte-parole du MFP", "neutre", "opposition"),
    ("sokolova-iouri", "Iouri Sokolova", "Président de l'Union pour la Souveraineté Populaire (UPS)", "neutre", "opposition"),
    ("makarova-francesco", "Francesco Makarova", "Porte-parole de l'UPS", "neutre", "opposition"),
    ("orlov-irina", "Irina Orlov", "Présidente de Justice et Solidarité (JS)", "neutre", "opposition"),
    ("petrov-marco", "Marco Petrov", "Porte-parole de JS", "neutre", "opposition"),
    ("morozov-nikolai", "Nikolaï Morozov", "Président de l'Union pour la Concorde Civique (UCH)", "neutre", "opposition"),
    ("sanna-oleg", "Oleg Sanna", "Porte-parole de l'UCH", "neutre", "opposition"),
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
            "tags: [mercure, persona, %s]\n" % cat +
            "source: ../../../ANALYSTE/MERCURE/MEMOIRE.md\n"
            "linkedTo: [ENT-mercure]\n"
            "relevantFor: [mercure]\n"
            "camp: %s\n" % camp +
            "pays: Mercure\n"
            "tier: 3\n"
            "created: %s\n" % TODAY +
            "updated: %s\n" % TODAY +
            "---\n\n"
            "# 👤 %s\n\n" % nom +
            "> camp %s **%s**. Rôle : %s.\n\n" % (EMOJI[camp], camp, role) +
            "## 🔗 Source de vérité\n"
            "[[../../../ANALYSTE/MERCURE/MEMOIRE.md]] (countrybook Mercure). Pays : [[ENT-mercure]].\n"
        )
        open(path, "w", encoding="utf-8").write(body)
        created += 1
    print("seed Mercure : %d créées, %d déjà présentes" % (created, skipped))


if __name__ == "__main__":
    main()
