# -*- coding: utf-8 -*-
"""
_seed_arnland.py — sème (une fois) les entités Arnland du countrybook + théâtre 7BB
(MINOTAURE 26). Camps : bios.js fait foi pour les personas du trombino (HN bleu,
Weber/Lang neutre), doctrine sinon. ORION 26 O41 (théâtre HPoitou) = DIFFÉRÉ.
IDEMPOTENT (ne réécrit jamais une note existante). Source : ANALYSTE/ARNLAND/MEMOIRE.md.
Volkonsky/Savchenko (rouge) + Borchenko (neutre) = écrits à la main (exclus ici).
"""
import os, datetime

VAULT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DST = os.path.join(VAULT, "entities", "personas")
TODAY = datetime.date.today().isoformat()
EMOJI = {"rouge": "🔴", "bleu": "🔵", "neutre": "⚪"}

FIG = [
    # Gouvernement national (APP, pro-OTAN) — bleu
    ("pallesson", "Sture Pallesson", "Président de la République (APP, pro-OTAN) — com > action, coalition fragile", "bleu", "gouvernement"),
    ("karrlson", "Vincent Karrlson", "Premier ministre (APP) — apparatchik loyal, sans base", "bleu", "gouvernement"),
    ("jankovic", "Mira Janković", "Ministre des Affaires étrangères — très active sur X (contre-narratifs, droit international)", "bleu", "gouvernement"),
    ("belov", "Andrei Belov", "Ministre de la Défense — dépendance OTAN, tensions budgétaires", "bleu", "gouvernement"),
    ("radulov", "Dmitri Radulov", "Ministre de l'Intérieur (ex-ASPS) — rhétorique « 5e colonne » anti-diaspora MER", "bleu", "gouvernement"),
    ("dragunov", "Viktor Dragunov", "Ministre des Finances", "bleu", "gouvernement"),
    ("marinov", "Vladislav Marinov", "Chef de l'ASP (opposition, pro-SCO/MER ambiguë, amplifié par MER)", "neutre", "opposition"),
    # Échelon HLorraine (ZO 7BB)
    ("birkmann", "Augustin Birkmann", "Préfet de la région HLorraine — intègre mais dépassé, isolé de HParis", "bleu", "hlorraine"),
    ("weber", "Henri Weber", "Maire de HSarrebourg — pharmacien proche des milieux pro-MER, ville 35% diaspora (relais/cible LO4)", "neutre", "hlorraine"),
    ("gervais", "Émile Gervais", "Maire de HNancy — jeune (gauche), « capitale de résistance », hub logistique/humanitaire", "bleu", "hlorraine"),
    ("thiebaut", "Bernard Thiebaut", "Maire de HChâteau-Salins — liens familiaux mercuriens frontaliers", "bleu", "hlorraine"),
    ("lang", "Dorothée Lang", "Maire de HHaguenau — biculturelle MER/ARN, charnière LO4/LO5, sous surveillance MININT", "neutre", "hlorraine"),
    ("krauss", "Isabelle Krauss", "Maire de HLunéville — patriote arnlandaise (aile sociale APP), base arrière/hôpital", "bleu", "hlorraine"),
    ("voloshyn", "Irina Voloshyn", "Maire de HToul", "bleu", "hlorraine"),
    ("brenner", "Nikolaï Brenner", "Maire de HMorange", "bleu", "hlorraine"),
    ("hartmann", "Grigori Hartmann", "Maire de HSarre-Union (ville saisie par 27BIM en CAX1)", "bleu", "hlorraine"),
    ("kovalev", "Dmitri Kovalev", "Maire de HAlberstroff", "bleu", "hlorraine"),
    # Militaire (ADF) — bleu
    ("djobovic", "Marko Djobović", "Gén. de brigade — CO 8e DAC (capture des 104 soldats MER à HNancy) ; cible nominative de l'ILI MER", "bleu", "militaire"),
    ("vong", "Vong", "CHOD — chef des armées", "bleu", "militaire"),
    ("hus", "Hus", "CGS — état-major terrestre", "bleu", "militaire"),
    ("bystrom", "Bystrom", "Chef de la Marine", "bleu", "militaire"),
    ("fries", "Fries", "Chef de l'Armée de l'air", "bleu", "militaire"),
    ("gradholm-arn", "Gradholm (ARN)", "Chef des forces spéciales (SOF) — homonyme distinct du Gradholm bothnien", "bleu", "militaire"),
    ("arne", "Arne", "Ballistic Missile Force (BMF)", "bleu", "militaire"),
    ("stanev", "Aleksandr Stanev", "Chef de l'ASPS", "bleu", "militaire"),
    # Judiciaire — bleu (institution HN)
    ("vukovic", "Stanislav Vuković", "Président de la Cour suprême", "bleu", "justice"),
    ("stepanenko", "Mariya Stepanenko", "Juge constitutionnel", "bleu", "justice"),
    ("zoric-nikolai", "Nikolai Zoric", "Juge pénal", "bleu", "justice"),
    ("milova", "Ekaterina Milova", "Avocate générale", "bleu", "justice"),
    ("antonov", "Yuri Antonov", "Avocat de la défense (célèbre)", "neutre", "justice"),
    # Internationaux
    ("zoric-kristina", "Kristina Zoric", "Porte-parole de l'OTAN", "bleu", "international"),
    ("andreev-milan", "Milan Andreev", "Porte-parole de l'UE", "bleu", "international"),
    ("malenko", "Yegor Malenko", "Président du Dushman (allié-partenaire)", "neutre", "international"),
    # ONG / humanitaire (présents dans le trombino 7BB)
    ("kalugin", "Boris Kalugin", "Représentant de l'ICRC en Arnland (POW/civils ; humanitaire)", "bleu", "ong"),
    ("velkova", "Tatiana Velkova", "ICRC en Arnland (humanitaire)", "bleu", "ong"),
    ("mishin", "Igor Mishin", "Président de l'Arnish Refugee Council (ARC)", "bleu", "ong"),
    ("petrovna", "Elena Petrovna", "Responsable de Blue Shield en Arnland (patrimoine culturel)", "bleu", "ong"),
    # Cabinet (annexe countrybook, structurel)
    ("novak", "Boris Novak", "Ministre du Développement national/international", "bleu", "cabinet"),
    ("vasilieva", "Elena Vasilieva", "Ministre de la Justice", "bleu", "cabinet"),
    ("pavlenko-natalya", "Natalya Pavlenko", "Ministre de l'Environnement", "bleu", "cabinet"),
    ("petrova-irina", "Irina Petrova", "Ministre de la Santé", "bleu", "cabinet"),
    ("kravtsova", "Anastasia Kravtsova", "Ministre Culture / Jeunesse / Sports", "bleu", "cabinet"),
    ("baranov", "Ivan Baranov", "Ministre Agriculture / Alimentation", "bleu", "cabinet"),
    ("filipovic", "Zoran Filipović", "Ministre des Transports", "bleu", "cabinet"),
    ("zhukova", "Milena Zhukova", "Ministre Éducation / Recherche", "bleu", "cabinet"),
    ("nikitin", "Sergei Nikitin", "Ministre Travail / Protection sociale", "bleu", "cabinet"),
    ("bodrova", "Tatiana Bodrova", "Ministre Économie / Commerce", "bleu", "cabinet"),
    ("morozov", "Alexei Morozov", "Ministre Technologies / Numérisation", "bleu", "cabinet"),
    # Partis (countrybook)
    ("dimitrov", "Oleg Dimitrov", "Président de l'APP (centre-droit, dominant depuis 1991)", "bleu", "partis"),
    ("sidorov", "Mikhail Sidorov", "Président de l'ARP (droite, appui ponctuel à l'APP)", "bleu", "partis"),
    ("karadzic", "Bojan Karadzic", "Président du SDP (centre-gauche)", "neutre", "partis"),
    ("pavlenko-luka", "Luka Pavlenko", "Président de l'ALP (centre, soutient l'APP)", "bleu", "partis"),
    ("volkov-ivan", "Ivan Volkov", "Président de l'ACP (communiste)", "neutre", "partis"),
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
            "tags: [arnland, persona, %s]\n" % cat +
            "source: ../../../ANALYSTE/ARNLAND/MEMOIRE.md\n"
            "linkedTo: [ENT-arnland]\n"
            "relevantFor: [arnland]\n"
            "camp: %s\n" % camp +
            "pays: Arnland\n"
            "tier: 3\n"
            "created: %s\n" % TODAY +
            "updated: %s\n" % TODAY +
            "---\n\n"
            "# 👤 %s\n\n" % nom +
            "> camp %s **%s**. Rôle : %s.\n\n" % (EMOJI[camp], camp, role) +
            "## 🔗 Source de vérité\n"
            "[[../../../ANALYSTE/ARNLAND/MEMOIRE.md]] (countrybook Arnland). Pays : [[ENT-arnland]].\n"
        )
        open(path, "w", encoding="utf-8").write(body)
        created += 1
    print("seed Arnland : %d créées, %d déjà présentes" % (created, skipped))


if __name__ == "__main__":
    main()
