# Avis DESIGNER n°19 — MELMIL : une demande de produit sans incident, et la cellule demandeuse (2026-10-01)

**Demande utilisateur.** La FORAD ne crée pas d'incident dans MELMIL. Elle doit pourtant pouvoir demander un produit à la cellule Prod. Il faut donc un bouton dans l'onglet « Demandes de produit », et chaque demande doit dire si elle vient de la GREY CELL ou de la FORAD. DESIGNER a été associé à la mise en place.

| # | Recommandation | Source |
|---|---|---|
| R1 | **« + Nouvelle demande sans incident »**, bouton principal en haut à droite de l'onglet, ouvert à tous. C'est la seule action principale de l'écran : les filtres restent discrets. Le libellé dit pour quel cas il est fait, pour qu'on ne l'utilise pas à la place de la demande depuis un incident. | Une action principale par écran (règle 6) ; l'étiquette dit l'usage (REF-07) |
| R2 | **« Cellule demandeuse » obligatoire sur TOUTE demande**, en tête du formulaire, sous forme de **deux choix visibles** (FORAD / GREY CELL, `role="radio"`) plutôt qu'une liste déroulante. Elle est **pré-choisie** d'après la fiche Équipe de la personne, sinon d'après l'event de l'incident. | Hick, peu de choix tous visibles (REF-06) ; Tesler, le système pré-remplit (règle 19) |
| R3 | **« Rempli par MELMIL » dit l'absence d'incident** : « Incident : *Aucun — demande directe* ». La ligne « Joué le » disparaît, et l'en-tête de la fenêtre porte « sans incident · demande directe ». | État du système visible (Nielsen 1, règle 25) |
| R4 | **Dans la file, une colonne et un filtre « Cellule »**. Une demande directe affiche « *sans incident* » en italique, et non un tiret qui ferait croire à un incident supprimé. | Ne pas laisser d'ambiguïté (REF-07) ; Nielsen 6 |
| R5 | **Une demande directe reçoit elle-même ses fichiers.** Le demandeur y joint ses fichiers de base après l'envoi (bouton « Joindre des fichiers »), cochés d'office dans « Fichiers fournis ». La cellule Prod y dépose sa livraison. Avant l'envoi, le formulaire dit qu'on pourra les joindre juste après. | Fin de parcours soignée (Peak-End, règle 18) ; Tesler |
| R6 | **La cellule DÉCLARÉE fait foi** pour le nommage des pièces jointes (`AAAAMMJJ_MR_DL26_SITCEN-CELLULE-Titre`), avant la fiche Équipe du demandeur. | Cohérence (Nielsen 4) |

**Règles de gestion qui en découlent** (code `app-melmil` `533e548`) :
- une demande directe a `incident = ""`. Elle **survit** au ménage des orphelins ; la **supprimer emporte ses fichiers** (ils n'ont pas d'incident où rester) ;
- la retirer une fois **prise en charge** reste **réservé à la cellule Prod**, comme pour les autres demandes ;
- les demandes d'avant le 2026-10-01 n'ont pas de cellule déclarée : la file affiche celle de la fiche Équipe de leur demandeur.

**Vérifié en local** (données fictives, Playwright) :
- le bouton ouvre le formulaire, avec la cellule pré-choisie (FORAD, d'après la fiche Équipe) ;
- une fois envoyée, la demande DP-03 apparaît « *sans incident* » avec la cellule FORAD ;
- la demande ouverte propose « Joindre des fichiers » ;
- au téléphone (390 px), aucun débordement ; aucune erreur de page ;
- 281 tests, dont 9 nouveaux.

Captures : `dp_2_formulaire.png`, `dp_3_demande_ouverte.png`, `dp_4_liste.png`, `dp_5_tel.png`.
