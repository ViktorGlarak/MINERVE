# Avis DESIGNER — maquettes existantes d'app-press (2026-09-29)

**Demande utilisateur** : analyser et optimiser le rendu et l'architecture des maquettes **Today Mercure, HEXAGONE, TV4 International et Bothnia Channel 1**, en respectant la charte de chaque pays (Today Mercure = média d'État « théoriquement russe »). **Hors champ** : TF1, Omerta, ONU, OTAN, ZubrRadio et EFS, reprises de sites réels qui doivent rester ressemblants.

**Ce qui fait foi** (DESIGNER contribue, ne tranche pas) :
- les chartes MASTAURIGE (couleurs, logos, typographies, langue) ;
- la mémoire de l'Analyste Mercure : **Today Mercure publie exclusivement en anglais**, c'est la source officielle de propagande de Mercure.

**Banc d'essai** : `app-press` en local sur une base à part (`presse_design`), avec le jeu de démonstration (13 articles, fil en direct) et 10 photos d'essai. Deux articles sont volontairement laissés sans photo. Captures à 1440 et 390 px, accueil et article : `avant\` et `apres\`.

## Constats (gravité 0 à 4, Nielsen)

| # | Problème | Où | Gravité |
|---|---|---|---|
| P1 | **Pavé noir ou gris** à la place de la vignette d'un article sans photo (le cadre était posé avant de savoir s'il y avait une image) | les 4 | 3 |
| P2 | **Une sans hiérarchie** : un article principal, puis 9 lignes identiques | TM, BC1 | 3 |
| P3 | **Doublons** : la colonne « Latest » répétait tout le fil de la une ; le slogan était affiché deux fois dans l'en-tête | TM, BC1 | 2 |
| P4 | **Titre répété trois fois** (bandeau, ligne rose, titre) | HEX | 2 |
| P5 | **Carte orpheline** en fin de grille | HEX, TV4 | 1 |
| P6 | **Bandeau défilant vide** au chargement (le texte partait de l'extrême droite) ; aucun arrêt pour « réduire les animations » (WCAG 2.2.2) | TM, BC1, TV4 | 2 |
| P7 | **Textes de 9-10 px** et blancs à 22-40 % d'opacité sur noir : sous 4,5:1 (WCAG 1.4.3) | les 4 (pieds, colonnes, méta) | 2 |
| P8 | Vignettes de cartes en **tranche de 100 px** : on ne voyait pas la photo | TV4 | 1 |
| P9 | **Téléphone** : fil à chapeaux sur une colonne étroite, soit 4 356 px de haut | TM, BC1 | 2 |

## Recommandations appliquées

1. **R1 — Vignette à la marque** (`Visuel`, `skins.css`) : sans photo, la marque du média sur sa couleur (TM : noir et or ★, BC1 : marine « BC1 », TV4 : carré orange « TV4 » en bleu, HEX : bleu « HEXAGONE » condensé). Refactoring UI : un état vide soigné plutôt qu'un trou.
2. **R2 — Une hiérarchisée** : TM et BC1 affichent l'article principal, puis **deux secondaires en cartes avec photo**, puis le fil. Hexagone met le **premier article en grand (2 × 2)**. Hiérarchie par la taille, REF-07.
3. **R3 — Grilles en rangées complètes** (`rangees()`) : on garde le plus grand nombre de cartes qui remplit les rangées ; le reste se trouve dans les rubriques et la recherche.
4. **R4 — Plus de doublons** : la colonne « Latest » est retirée de la une (`HorsAccueil`) et reste sur les pages d'article. La ligne d'or de TM porte le **statut** du média (« Official state news service · English edition · 24/7 »). Le bandeau d'antenne d'Hexagone porte **l'heure** (« HEXAGONE · 05H04 · L'INFORMATION EN CONTINU ») au lieu du titre, et la rubrique n'y est plus doublée.
5. **R5 — Bandeaux** : remplis dès le chargement, en boucle continue, arrêtés sous `prefers-reduced-motion`.
6. **R6 — Lisibilité** : textes portés de 9-10 px à 11-13 px, blancs à 60-80 % sur noir, focus visible dans la couleur de la charte, photo principale plafonnée à 440-460 px en 16/9, colonne latérale qui suit le défilement.
7. **R7 — Téléphone** (< 600 px) : fil sans chapeau (il reste sur la page de l'article), vignette de 96 px. TM passe de **4 356 à 3 437 px**.
8. **R8 — Identité « russe » de Today Mercure**, sans rien inventer hors charte : **« 18+ »** et **mention d'enregistrement** du média en pied de page (« registered by the Federal Service for Media Supervision of the Republic of Mercure · Reg. No. EL FS 77-81024 »), deux marques des sites d'État russes (RT, TASS). VK et Telegram, les langues EN/MR/RU, l'étoile et le noir/rouge/or sont gardés.

## Vérifications
- Aucun débordement horizontal (1440 et 390 px, accueil et article, les 4 maquettes).
- `tsc` OK ; image reconstruite comme sur le serveur (`npm test` + `next build`) OK.
- Commit `48b1072` sur la branche `design-maquettes` (app-press).

## Écarté
- Remonter le direct au-dessus de la une au téléphone : c'est l'article principal qui doit venir en premier.
- Toute modification de couleur, de logo ou de langue : la charte fait foi.
