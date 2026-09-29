# Avis DESIGNER n°1 — app-melmil (version 2026-09-24.2)

- **Demande de l'utilisateur** : « visuellement il n'est pas très esthétique et j'ai du mal à me repérer ».
- **Méthode** (grille MEMOIRE §3.6) : captures des écrans réels sur la copie locale (données DE LATTRE 26, 1440 × 900, dans ce dossier) · 10 heuristiques de Nielsen (REF-14) · A11Y / WCAG (REF-13, REF-16) · hiérarchie (REF-07). Tailles relevées dans la page : texte courant 16 px, **étiquettes 10,4 px**, **boutons 11,2 px sur 26 px de haut**, résumés de groupe 12 px, onglets 14 px.
- ⚠ **Avis, pas verdict** : les choix de fond de MELMIL (deux planches séparées, enregistrement en quittant le champ, codes JEMM) sont conservés. L'avis porte sur la **présentation**.

## Diagnostic : pourquoi on s'y perd

| # | Problème | Où | Règle / source | Gravité (0-4) |
|---|---|---|---|---|
| D1 | **Les deux espaces se ressemblent** : « Création d'exercice » et « Planche JEMM » ont le même en-tête, la même planche et les mêmes couleurs. Seul un petit bouton clair dans le bandeau dit où l'on est, et il ressemble à un bouton, pas à un emplacement. | bandeau, en-têtes | Nielsen 1 (où suis-je ?), Similarity (REF-06) | **4** |
| D2 | **Trois étages de navigation empilés** avant le contenu : le bandeau, puis les cartes GT1/GT2/GT3 (état et actions mélangés), puis 8 onglets. **Le contenu commence à 390 px du haut**, soit plus de 40 % de l'écran. | haut de toutes les pages de l'atelier | Hick, Cognitive Load (REF-06) ; « ne pas remplir l'écran » (REF-07) | **3** |
| D3 | **8 onglets à plat**, de natures différentes : construire (Events, Storylines, Incidents), voir (Planche, Écarts), organiser (Équipe, Journal, Réglages). | onglets | Chunking, Hick (REF-06) | 2 |
| D4 | **Texte trop petit pour un outil de travail** : étiquettes à 10,4 px en capitales espacées, boutons à 11,2 px, cartes de la planche à environ 8-9 px avec des « … » partout. | partout | REF-17 (14 px minimum en outil), REF-07 | **3** |
| D5 | **Planche saturée** : aplats très vifs (rouge foncé, bleu, vert, violet) sous du texte blanc minuscule ; le **rouge sert de couleur de storyline** alors qu'il signifie « alerte » ; des cases vides à côté d'une case qui déborde (06.01, 13 incidents entassés). | planche JEMM et planche de préparation | Von Restorff, une seule couleur d'alerte (MEMOIRE r.20) ; Refactoring UI « atténuer pour mettre en valeur » | **3** |
| D6 | **Liste d'incidents** : 46 boîtes bordées les unes sous les autres, dont on ne lit bien que le code ; **le statut n'est porté que par un petit carré de couleur**. | onglet Incidents | WCAG 1.4.1 (couleur seule, REF-13) ; « moins de bordures » (REF-07) ; tableau de données (REF-12) | **3** |
| D7 | **Fiches très longues, sur toute la largeur** : les descriptions courent sur 1 400 px (plus de 180 caractères par ligne), et tous les champs ont le même poids, qu'ils soient essentiels ou secondaires. | fiches storyline et incident | REF-17 (45 à 90 caractères), REF-07 (hiérarchie) | 2 |
| D8 | **Accessibilité** : la fenêtre de compte rendu ne garde pas le focus et ne le rend pas ; onglets sans navigation par flèches ; petites cibles (26 px). | fiche CR, onglets | REF-19, REF-13 (2.1.2, 2.5.8) | 2 |

Ce qui marche et **doit rester** : la pastille « EN DIRECT · nom » (Nielsen 1) · les codes en police à chasse fixe (lecture rapide) · le pré-remplissage (Tesler) · la grille EXCON et le CR à l'identique des modèles · la planche en colonnes par jour.

## Recommandations, classées par gain pour l'utilisateur

| # | Proposition | Gain | Effort |
|---|---|---|---|
| **R1** | **Rendre l'emplacement évident.** Une **bande de couleur et une étiquette permanentes** différentes pour les deux espaces, par exemple « PRÉPARATION · brouillon de la cellule » (teinte chaude) et « PLANCHE JEMM · ce que reçoivent les joueurs » (teinte froide). Dans le bandeau, un **sélecteur segmenté** dont l'état actif est sans ambiguïté. | règle D1 | **S** |
| **R2** | **Compacter le haut de page** : titre et avancement des GT **sur une seule ligne** (« DE LATTRE 26 · GT1 ✓ → GT2 ✓ → **GT3 en cours** »), l'action « passer l'exercice ici » rangée dans un petit menu, la phrase d'explication affichée seulement sur l'atelier vide. Le contenu remonte d'environ 200 px. | D2 | **S** |
| **R3** | **Grouper les onglets** en trois familles séparées visuellement : **Construire** (Events · Storylines · Incidents) · **Visualiser** (Planche · Écarts) · **Organiser** (Équipe · Journal · Réglages). Même nombre de clics, beaucoup moins à lire. | D3 | **S** |
| **R4** | **Une échelle typographique d'outil** : 12 px au minimum pour les étiquettes (en casse normale), 13-14 px pour les boutons avec une hauteur de 32 px, 14 px pour le texte courant, 11-12 px sur la planche avec 2 lignes avant la coupure. | D4, D8 | **S** (CSS) |
| **R5** | **Planche lisible** : des cartes à **fond clair teinté** et **bordure gauche** à la couleur de la storyline au lieu d'aplats saturés ; texte foncé ; le **rouge réservé aux alertes** ; au-delà de 3 incidents par case, afficher « + 8 » avec un dépliage. | D5 | **M** |
| **R6** | **Liste d'incidents en vrai tableau** (à la Carbon) : colonnes Code · Jour · Heure · Sujet · **Statut en texte et en couleur** · nombre de CR ; lignes zébrées au lieu de boîtes ; tri par colonne ; la fiche s'ouvre dans un panneau latéral. | D6 | **M** |
| **R7** | **Fiches structurées** : largeur de lecture limitée à environ 860 px ; des sections (**Quand · Quoi · Qui · Effet attendu · Comptes rendus**) avec plus d'espace entre les sections qu'entre les champs ; les champs rarement utiles repliés. | D7 | **M** |
| **R8** | **Lot accessibilité** : statut en toutes lettres, focus gardé et rendu dans la fenêtre de CR, flèches dans les onglets, anneau de focus visible partout. | D6, D8 | **S** |

**Suggestion d'ordre** : R1 + R2 + R3 + R4 + R8 d'abord. Ce sont des retouches légères, qui traitent directement « j'ai du mal à me repérer ». Viennent ensuite R5, R6 et R7, les chantiers visuels, à valider d'abord sur une **maquette**.

**Suite donnée** : appliqué en local à la demande de l'utilisateur (branche `refonte-design`, `aeaa796`), **validé** (« j'aime beaucoup les modifs ») puis **mis en production** le 2026-09-24 à 15:04 (version `2026-09-24.3`). Captures « après » dans `apres\`.

| # | Ce qui a été fait |
|---|---|
| R1 | Un sélecteur segmenté dans le bandeau : l'espace actif est enfoncé, en ambre pour la préparation et en bleu pour JEMM. Sous le bandeau, une bande de 4 px de la teinte de l'espace ; en tête de page, l'étiquette « Préparation · brouillon de la cellule » ou « Planche JEMM · ce que reçoivent les joueurs ». |
| R2 | L'en-tête tient sur une ligne : étiquette, titre, parcours GT1 ✓ → GT2 ✓ → GT3 en cours (chaque étape est cliquable), menu « Changer de GT », pastille « en direct ». La phrase d'explication ne s'affiche que sur un atelier vide. Le contenu remonte d'environ 200 px. |
| R3 | Les onglets sont groupés en Construire / Visualiser / Organiser, sur le modèle WAI-ARIA : flèches gauche et droite, Début, Fin. |
| R4 | Les étiquettes passent à 12 px en casse normale, les champs à 14 px, les résumés de groupe à 14 px. |
| R5 | Nouveau style **« Clair »** de la planche (par défaut) : fond teinté à 11 %, liseré de 4 px à la couleur de la storyline, texte foncé à 10-10,5 px, repli « + N » au-delà de 3 incidents par jour. Le bouton « Classique » garde les aplats de MASTAURIGE : choix mémorisé par poste, en application de la loi de Jakob. Les deux rouges de la palette (Bordeaux, Rouge) sont remplacés par Cuivre et Olive. |
| R6 | Incidents en tableau : Code · Quand · Sujet · **Statut en toutes lettres** · nombre de CR ; lignes zébrées ; ouverture au clavier (Entrée). |
| R7 | Fiche incident dans un panneau latéral de 640 px, découpée en sections Quand / Quoi / Qui / Effet attendu / Comptes rendus / actions. Focus sur le titre à l'ouverture ; Échap ferme et **rend le focus à la ligne**. *(Storylines : seules les étiquettes ont changé ; leur découpage en sections reste à faire.)* |
| R8 | Anneau de focus visible partout. La fiche de CR garde le focus (Tab en boucle) et le rend à la fermeture. La fenêtre de confirmation met le focus sur **Annuler**, l'action la moins dangereuse. |

Vérifications : 165 tests OK · `tsc` et lint propres · essai au clavier (flèches dans les onglets, Échap sur la fiche, 40 Tab dans la fiche CR sans en sortir) · thème sombre vérifié, et le contraste du segment ambre corrigé.
