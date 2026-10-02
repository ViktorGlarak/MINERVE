# Avis DESIGNER n°21 — MELMIL : des comptes rendus partagés par jour et par ETIM, en direct (2026-10-01)

**Demande utilisateur.** Les PSYREP et CIMICREP doivent être **les mêmes pour tous les incidents d'un même jour qui ont la même ETIM**. Par exemple, à D+27, si 08.02.I01 et 08.03.I01 ont l'ETIM 7, ils partagent le PSYREP et le CIMICREP de l'ETIM 7. Si l'un d'eux a aussi l'ETIM 27, celle-ci a ses propres comptes rendus. Ils doivent se modifier **à plusieurs, en temps réel**. DESIGNER était invité à redisposer la fiche d'incident pour que ce soit compréhensible.

**Décisions de l'utilisateur** : **un seul** PSYREP et **un seul** CIMICREP par jour et par ETIM. Les anciens comptes rendus sont **convertis automatiquement** quand il n'y a pas d'ambiguïté.

| # | Recommandation | Source |
|---|---|---|
| R1 | **La rubrique « Comptes rendus du jour (D+x) » remonte juste sous « ETIM concernées »** : elle en dépend, on doit voir la cause et l'effet ensemble. | Proximité (REF-06) ; Nielsen 4 |
| R2 | **Un tableau ETIM × type** : une ligne par ETIM cochée, une colonne PSYREP, une colonne CIMICREP. La structure (jour × ETIM × type) se lit sans explication. | La forme de la donnée parle (règle 7) |
| R3 | **Chaque case dit avec qui le compte rendu est partagé** : « Commun avec 08.03.I01 », ou « Sera commun avec… » avant sa création, ou « Seul incident de ce jour avec cette ETIM ». On sait qu'une modification vaut pour plusieurs incidents. | État du système visible (Nielsen 1, règle 25) |
| R4 | **Ouvrir** quand le compte rendu existe, sinon **+ Créer** ou **Importer** (.docx). L'en-tête de la fiche ouverte affiche « PSYREP · ETIM 7 · D+27 — commun à 08.02.I01, 08.03.I01 · modifié en direct par tous ». | Reconnaissance plutôt que rappel (Nielsen 6) |
| R5 | **Temps réel sans perte** : une case s'enregistre aussi après **une seconde sans frappe**, pas seulement en la quittant. Les autres postes voient le texte arriver. La case où l'on écrit n'est **jamais** écrasée par un autre poste ; elle se remet à jour quand on la quitte. | Doherty, réponse rapide (règle 13) ; ne jamais perdre une saisie (REF-14) |
| R6 | **États vides qui guident** : « Placez l'incident sur un jour (D+) » ou « Cochez les ETIM concernées ci-dessus », plutôt qu'un tableau vide. | États vides soignés (règle 18) |
| R7 | **Les anciens comptes rendus restent visibles**, sous « Anciens comptes rendus de cet incident », avec l'explication de pourquoi ils n'ont pas été convertis (plusieurs ETIM, ou compte rendu du jour déjà existant). | Ne rien perdre en silence (principe MELMIL) |

**Règles de gestion** (code `app-melmil` `db46d4b`) :
- un compte rendu partagé = `{ jour, etim, type }`, avec `incident = ""` ;
- il est **unique** : une création concurrente ou rejouée rend celui qui existe ;
- il **survit** à la suppression d'un incident, et réapparaît si l'ETIM est recochée ;
- **valeurs de départ** : GDH du jour, à l'heure du premier incident concerné ; pour le CIMICREP, l'exercice et les codes des incidents couverts.

**Vérifié en local** (données fictives, Playwright, **deux navigateurs séparés**) :
- le poste A crée le PSYREP de « ETIM ESSAI » à D+33 depuis 06.01.I01 ;
- le poste B, sur 08.01.I01, le voit apparaître sans recharger (« Commun avec 06.01.I01 ») et l'ouvre ;
- A tape dans une case **sans la quitter** : B voit « Texte tape par le poste A » s'afficher ;
- 301 tests, dont 12 sur les comptes rendus partagés et la conversion.

Captures : `cr_1_tableau.png`, `cr_2_poste_A.png`, `cr_3_poste_B.png`.
