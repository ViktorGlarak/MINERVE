# -*- coding: utf-8 -*-
"""
_seed_countbook_complements.py — comble les OUBLIS détectés en comparant les
countbooks sources (D:\\CECPC\\DOC REF\\COUNTRY BOOK) aux entités du vault.
Bothnia : MP + sous-chefs police + DIA Kavalenka. Arnland : porte-parole partis,
associations, OI. Mercure : présidents régionaux, sous-dir Intérieur, Deema,
groupes d'influence, commissions, reps OIG (filler différé).
Camps par doctrine. IDEMPOTENT. tier 3.
"""
import os, datetime
VAULT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DST = os.path.join(VAULT, "entities", "personas")
TODAY = datetime.date.today().isoformat()
EMOJI = {"rouge": "🔴", "bleu": "🔵", "neutre": "⚪"}
SRC = {"bothnia": "BOTHNIA", "arnland": "ARNLAND", "mercure": "MERCURE"}

# (slug, nom, role, camp, pays, cat)
FIG = [
    # ---------- BOTHNIA ----------
    ("dziadok-natallia", "Natallia Dziadok", "Députée (MP) — Bothnian Unity Party (BUP)", "neutre", "bothnia", "parlement"),
    ("hurski", "Andrej Hurski", "Député (MP) — Bothnian National Party (BNP)", "neutre", "bothnia", "parlement"),
    ("makarevich", "Ulyana Makarevich", "Députée (MP) — Bothnian Prosperity Party (BPP)", "neutre", "bothnia", "parlement"),
    ("zhuk", "Michal Zhuk", "Député (MP) — Liberal Party of Bothnia (LPB)", "neutre", "bothnia", "parlement"),
    ("karpovitch", "Artsiom Karpovitch", "Chef de la Police (countbook ORION). ⚠ DIVERGENCE : la mémoire ANALYSTE_BOT / le vault listent « Ann Richter » au même poste — à arbitrer.", "neutre", "bothnia", "police"),
    ("shymanovich", "Paval Shymanovich", "Chef du NCID (National Criminal Investigations Department)", "neutre", "bothnia", "police"),
    ("radzivil-aliaksandr", "Aliaksandr Radzivil", "Chef du NTF (National Task Force)", "neutre", "bothnia", "police"),
    ("vasilevich", "Raman Vasilevich", "Chef du NSWAT (anti-terroriste)", "neutre", "bothnia", "police"),
    ("dziadok-maryia", "Maryia Dziadok", "Cheffe du NECB (National Economic Crimes Bureau)", "neutre", "bothnia", "police"),
    ("marozau", "Tatsiana Marozau", "Cheffe du Police Air Service", "neutre", "bothnia", "police"),
    ("kavalenka", "Yury Kavalenka", "Directeur de la DIA (Defence Intelligence Agency) — countbook", "neutre", "bothnia", "renseignement"),
    ("rasmussen", "Emil Rasmussen", "Porte-parole de la CBE (Confederation of Bothnian Enterprise)", "neutre", "bothnia", "societe"),
    # ---------- ARNLAND ----------
    ("zhivkovic", "Irina Zhivković", "Porte-parole de l'APP (Arnland Prosperity Party)", "bleu", "arnland", "partis"),
    ("durova", "Katarina Durova", "Porte-parole de l'ASP (Arnland Socialist Party)", "neutre", "arnland", "partis"),
    ("petrovic-radmila", "Radmila Petrović", "Porte-parole de l'ARP (Arnland Republican Party)", "bleu", "arnland", "partis"),
    ("kostova", "Natalya Kostova", "Porte-parole du SDP (Social Democratic Party)", "neutre", "arnland", "partis"),
    ("savchenko-anya", "Anya Savchenko", "Porte-parole de l'ALP (Arnland Liberal Party). ⚠ distincte de Nataliya Savchenko (leader pro-MER, rouge)", "bleu", "arnland", "partis"),
    ("milenkovic", "Zoya Milenković", "Porte-parole de l'ACP (Arnland Communist Party)", "neutre", "arnland", "partis"),
    ("vrenko", "Tomaš Vrenko", "Président d'association (société civile)", "neutre", "arnland", "societe"),
    ("novik-lidija", "Lidija Novik", "Porte-parole d'association (société civile)", "neutre", "arnland", "societe"),
    ("jaksic", "Radovan Jakšić", "Président d'association (société civile)", "neutre", "arnland", "societe"),
    ("blazic", "Vesna Blazic", "Porte-parole d'association (société civile)", "neutre", "arnland", "societe"),
    ("borovic", "Tanja Borović", "Porte-parole du Dushman (allié-partenaire)", "neutre", "arnland", "international"),
    ("radojevic", "Svetlana Radojević", "Porte-parole UNICEF (Arnland)", "neutre", "arnland", "ong"),
    # ---------- MERCURE — présidents régionaux ----------
    ("mancini", "Alla Mancini", "Présidente régionale de Bavemberg", "rouge", "mercure", "regions"),
    ("konig-markus", "Markus König", "Président régional de Bernino", "rouge", "mercure", "regions"),
    ("caruso", "Ksenia Caruso", "Présidente régionale de Bohême", "rouge", "mercure", "regions"),
    ("ebner", "Artem Ebner", "Président régional de Doluskie", "rouge", "mercure", "regions"),
    ("auer-georg", "Georg Auer", "Président régional de Lombmont", "rouge", "mercure", "regions"),
    ("antonova", "Zoya Antonova", "Présidente régionale de Nieva", "rouge", "mercure", "regions"),
    ("zaitsev", "Konstantin Zaitsev", "Président régional de Saxinga", "rouge", "mercure", "regions"),
    ("pichler", "Jakob Pichler", "Président régional de Tyrie", "rouge", "mercure", "regions"),
    ("bogdanov", "Stanislav Bogdanov", "Président régional de Vormaia", "rouge", "mercure", "regions"),
    ("tapeur", "Peter Tapeur", "Président de l'enclave HAquitaine", "rouge", "mercure", "regions"),
    # ---------- MERCURE — sous-directions Intérieur ----------
    ("auer-tobias", "Tobias Auer", "Service des poursuites de l'État (SPS) — Min. Intérieur", "rouge", "mercure", "interieur"),
    ("wallner", "Niklas Wallner", "Police régionale — Min. Intérieur", "rouge", "mercure", "interieur"),
    ("moser", "Heidi Moser", "Comité d'enquête — Min. Intérieur", "rouge", "mercure", "interieur"),
    ("konig-lorenz", "Lorenz König", "Département des enquêtes criminelles — Min. Intérieur", "rouge", "mercure", "interieur"),
    ("fuchs", "Verena Fuchs", "Département de l'ordre public — Min. Intérieur", "rouge", "mercure", "interieur"),
    ("winkler", "Sarah Winkler", "Service logistique — Min. Intérieur", "rouge", "mercure", "interieur"),
    ("tarasov", "Emanuele Tarasov", "Sécurité économique — Min. Intérieur", "rouge", "mercure", "interieur"),
    ("palmieri", "Dmitri Palmieri", "Organisation & Inspection — Min. Intérieur", "rouge", "mercure", "interieur"),
    ("seidl", "Benedikt Seidl", "Transports & Sécurité routière — Min. Intérieur", "rouge", "mercure", "interieur"),
    ("reither", "Theresa Reither", "Département financier & économique — Min. Intérieur", "rouge", "mercure", "interieur"),
    # ---------- MERCURE — Deema + Banque ----------
    ("muller-viktoria", "Viktoria Müller", "Tête de la Deema (chambre)", "rouge", "mercure", "institutions"),
    ("leitgeb", "Magdalena Leitgeb", "Députée (Deema)", "rouge", "mercure", "institutions"),
    ("majewski", "Patryk Majewski", "Député (Deema)", "rouge", "mercure", "institutions"),
    ("haider", "Agnieszka Haider", "Députée (Deema)", "rouge", "mercure", "institutions"),
    ("pawlak", "Petra Pawlak", "Présidente de la Banque fédérale", "rouge", "mercure", "institutions"),
    # ---------- MERCURE — groupes d'influence ----------
    ("kuznetsov", "Roman Kuznetsov", "Co-président — Fraternité des anciens combattants", "rouge", "mercure", "influence"),
    ("vassiliev", "Sergueï Vassiliev", "Co-président — Fraternité des anciens combattants", "rouge", "mercure", "influence"),
    ("kozlov", "Maksim Kozlov", "Porte-parole — Fraternité des anciens combattants", "rouge", "mercure", "influence"),
    ("hofer", "Margarita Hofer", "Présidente — Les Racines du Peuple", "rouge", "mercure", "influence"),
    ("franke", "Sebastian Franke", "Porte-parole — Les Racines du Peuple", "rouge", "mercure", "influence"),
    ("zupan", "Jasna Zupan", "Présidente — La Voie Économique Libre", "rouge", "mercure", "influence"),
    ("rupnik", "Jure Rupnik", "Porte-parole — La Voie Économique Libre", "rouge", "mercure", "influence"),
    ("zimmerman", "Henrik Zimmerman", "Président — Les Gardiens du Peuple", "rouge", "mercure", "influence"),
    ("schwarz", "Antonia Schwarz", "Porte-parole — Les Gardiens du Peuple", "rouge", "mercure", "influence"),
    # ---------- MERCURE — commissions ----------
    ("neumann", "Alexei Neumann", "Président — Commission électorale populaire (PECC)", "rouge", "mercure", "commissions"),
    ("vogel", "Alexandre Vogel", "Membre — PECC", "rouge", "mercure", "commissions"),
    ("gunther", "Greta Günther", "Porte-parole — PECC", "rouge", "mercure", "commissions"),
    ("jerman", "Maja Jerman", "Présidente — Commission intégrité & anticorruption (PICC)", "rouge", "mercure", "commissions"),
    ("schmid", "Zala Schmid", "Membre — PICC", "rouge", "mercure", "commissions"),
    ("fredotov", "Anatoli Fredotov", "Porte-parole — PICC", "rouge", "mercure", "commissions"),
    ("kiselev", "Timur Kiselev", "Président — Commission judiciaire populaire (PJC)", "rouge", "mercure", "commissions"),
    ("frolov", "Piotr Frolov", "Membre — PJC", "rouge", "mercure", "commissions"),
    ("urban-franziska", "Franziska Urban", "Porte-parole — PJC", "rouge", "mercure", "commissions"),
    # ---------- MERCURE — reps OIG Skolkan ----------
    ("conti", "Federico Conti", "Représentant MER au SCO", "rouge", "mercure", "oig"),
    ("wagner-natalia", "Natalia Wagner", "Représentante MER au SFTA", "rouge", "mercure", "oig"),
    ("gallo", "Pavel Gallo", "Représentant MER au SIA", "rouge", "mercure", "oig"),
    ("bauer-yuri", "Yuri Bauer", "Représentant MER à l'ONU", "rouge", "mercure", "oig"),
]


def main():
    os.makedirs(DST, exist_ok=True)
    created = skipped = 0
    for slug, nom, role, camp, pays, cat in FIG:
        path = os.path.join(DST, "ENT-%s.md" % slug)
        if os.path.exists(path):
            skipped += 1
            continue
        body = (
            "---\n"
            "id: ENT-%s\n" % slug +
            "type: entity\n"
            "title: %s\n" % nom +
            "tags: [%s, persona, countbook, %s]\n" % (pays, cat) +
            "source: ../../../ANALYSTE/%s/MEMOIRE.md\n" % SRC[pays] +
            "linkedTo: [ENT-%s]\n" % pays +
            "relevantFor: [%s]\n" % pays +
            "camp: %s\n" % camp +
            "pays: %s\n" % pays.capitalize() +
            "tier: 3\n"
            "created: %s\n" % TODAY +
            "updated: %s\n" % TODAY +
            "---\n\n"
            "# 👤 %s\n\n" % nom +
            "> camp %s **%s**. Rôle : %s.\n\n" % (EMOJI[camp], camp, role) +
            "> Complément countbook (annexe « Leading Figures / Personalities »).\n\n"
            "## 🔗 Source de vérité\n"
            "[[../../../ANALYSTE/%s/MEMOIRE.md]] + countbook ORION. Pays : [[ENT-%s]].\n" % (SRC[pays], pays)
        )
        open(path, "w", encoding="utf-8").write(body)
        created += 1
    print("seed countbook complements : %d créées, %d déjà présentes" % (created, skipped))


if __name__ == "__main__":
    main()
