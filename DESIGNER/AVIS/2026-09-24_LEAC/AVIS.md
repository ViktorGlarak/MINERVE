# Avis DESIGNER n°2 — app-leac (version 2026-09-22.1)

- **Demande de l'utilisateur** : « LEAC est vraiment compliqué à assimiler visuellement ; travailler le responsive — une version tablette, une version téléphone, une version ordinateur ».
- **Méthode** (MEMOIRE §3.6) :
  - captures de 8 écrans à 4 tailles (ordinateur 1440 × 900, tablette 820 × 1180 et 1180 × 820, téléphone 390 × 844), dans ce dossier ;
  - mesures relevées dans la page : débordement horizontal, cibles de moins de 44 px, tailles de texte ;
  - grilles de lecture : Nielsen (REF-14), WCAG (REF-13), Fitts (REF-06), APG (REF-19).
- ⚠ **Contrainte de référence** : le parti pris de LEAC **validé par l'utilisateur le 2026-09-17** (`LEAC\MEMOIRE.md` §7) est conservé. Tablette tenue à la main dehors · contraste élevé · cibles de 48 px · clair par défaut · mention en un seul appui · état de synchronisation permanent · système PLEIADE. L'avis **s'y ajoute**, il ne le rediscute pas.
- Ce qui est **déjà bien**, à garder :
  - les mentions en 48 px avec leur liseré de famille ;
  - la mention choisie en **inversion franche** ;
  - le mode « un par un » ;
  - la pastille de synchronisation ;
  - le carnet de terrain en entrée.

## Diagnostic

| # | Problème | Mesure / où | Règle | Gravité |
|---|---|---|---|---|
| D1 | **Pas de navigation commune.** Chaque écran porte sa propre rangée de 3 à 6 boutons, **dans un ordre différent** (le carnet affiche Bilan, Fin de cycle, Mandat, Paramétrage, Synchroniser ; le bilan affiche Fin de cycle, Paramétrage, CRF, Mandat, Grilles…). Aucun bouton ne dit **où l'on est**. On ne peut pas apprendre l'application par cœur. | 8 écrans | Nielsen 4 (cohérence) et 6 (reconnaître) ; Jakob | **4** |
| D2 | **Téléphone : l'écran de travail commence sous la ligne de flottaison.** Sur la grille, bandeau, en-tête, sélecteur, 6 boutons et barre d'outils sur 4 lignes occupent **540 px sur 844**. La rangée de boutons **déborde de 83 px**, ce qui fait défiler toute la page de côté. | téléphone, grilles et bilan | WCAG 1.4.10 (recomposition) ; Fitts | **4** |
| D3 | **Aucune adaptation à la taille d'écran.** La tablette et l'ordinateur affichent la **même colonne de 768 px**, avec des pages de même hauteur. L'ordinateur laisse les deux tiers de l'écran vides, la tablette paysage aussi. | toutes | « un service, pas un site » (REF-10) ; REF-07 | 3 |
| D4 | **La grille est centrée, alors qu'elle devrait être alignée à gauche.** Code, intitulé et compteur sont regroupés au milieu de la ligne : on ne balaie pas une colonne de codes. *Cause technique : `.frappe { justify-content: center }` l'emporte sur `justify-between`.* | grilles | REF-07 (alignement) ; Proximité | 3 |
| D5 | **Les boutons de navigation sont petits et nombreux** (12 px de texte), alors que les mentions sont confortables. Dehors, avec des gants, ce sont eux qu'on rate. | tous les écrans | Parti pris §7 (48 px), Fitts | 2 |
| D6 | **Des mots différents pour la même chose** : « Bilan » ouvre « Réunion quotidienne », « CRF » ouvre « Compte rendu ». | navigation | Nielsen 2 et 4 | 2 |
| D7 | **Accueil** : le pictogramme est collé **après** le libellé (« Créer un contrôle+ », « Administrateurs⚙ ») ; les cartes de contrôle n'ont pas toutes la même largeur ; l'administration a le même poids que « Ouvrir ». | accueil | REF-07 (hiérarchie), REF-08 | 1 |

## Recommandations

| # | Proposition | Traite | Effort |
|---|---|---|---|
| **R1** | **Une seule barre de navigation**, identique sur tous les écrans d'un contrôle, où la destination **courante est enfoncée** : **Carnet · Grilles · Bilan · Synchro · Plus** (Fin de cycle, Mandat, Compte rendu, Paramétrage). Les libellés reprennent les titres des pages. | D1, D5, D6 | M |
| **R2** | **Trois mises en page selon l'écran** : **téléphone et tablette en portrait**, barre **en bas** (sous le pouce, cibles de 56 px, zone de sécurité iOS) ; **tablette paysage et ordinateur** (≥ 1024 px), barre **latérale gauche** avec toutes les destinations visibles et une colonne de contenu élargie (jusqu'à 1 000 px). | D2, D3 | M |
| **R3** | **Supprimer les rangées de boutons propres à chaque écran**, remplacées par R1. Sur téléphone, cela supprime le débordement et fait remonter le contenu d'environ 110 px. | D1, D2 | S |
| **R4** | **Barre d'outils de la grille sur téléphone** : la recherche sur toute la largeur, puis les filtres sur une ligne qui défile horizontalement, au lieu d'un empilement de 4 lignes. | D2 | S |
| **R5** | **Grille alignée à gauche** : code et intitulé à gauche, compteur et note à droite (correctif CSS). | D4 | S |
| **R6** | **Accueil** : le pictogramme avant le libellé, et les cartes de contrôle en pleine largeur uniforme. | D7 | S |

**Non retenu** : une grille en deux colonnes sur ordinateur (arbre des domaines à gauche, critères à droite). C'est pertinent, mais c'est un chantier en soi, à proposer une fois R1 à R6 validés.
