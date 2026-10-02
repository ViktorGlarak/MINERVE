# Avis DESIGNER n°18 — Portail de zone, page « Presse » : la carte entière ouvre le site (2026-10-01)

**Demande utilisateur.** Sur `https://delattre-26.pleiade.internal/presse`, chaque titre de presse a deux boutons, « Ouvrir » et « Espace de rédaction ». L'utilisateur veut que **cliquer sur la carte** ouvre le site, ce qui supprime « Ouvrir ». Le bouton « Espace de rédaction » reste. DESIGNER était consulté pour proposer la meilleure façon de faire.

**Écran concerné** : `pleiade-platform`, `src/portail.ts`, `pageChoix` (la page de choix d'un type d'app quand la zone en compte plusieurs).

| # | Recommandation | Source |
|---|---|---|
| R1 | **Toute la carte ouvre le site.** Elle devient une cible bien plus grande que le petit bouton « Ouvrir », qui disparaît. La page d'accueil du portail fonctionne déjà ainsi : les deux pages se comportent maintenant de la même façon. | Fitts (REF-06, règle 12) ; Jakob, faire comme ailleurs (règle 15) |
| R2 | **Motif du « lien étiré »** : le **titre** du média est le lien, étendu sur toute la carte par un `::after`. Un lien ne peut pas en contenir un autre : on ne peut donc pas faire de la carte un seul `<a>` qui contiendrait aussi le bouton de rédaction. Le lecteur d'écran annonce le **nom du média**, et pas « Ouvrir », un mot vide hors contexte. | REF-02 (Radix), REF-13 (WCAG 2.4.4, but du lien) |
| R3 | **« Espace de rédaction » reste une action secondaire, posée au-dessus de la carte**, avec son propre survol et son propre focus. **Survoler le bouton n'anime pas la carte**, pour ne pas faire croire qu'un clic ouvrira le site. | Une seule action principale (règle 6) ; Nielsen 4, cohérence (REF-14) |
| R4 | **Un chevron « › » à droite** montre que la carte mène quelque part. Il s'éclaire au survol. Il est seulement décoratif (`aria-hidden`), puisque le titre porte le lien. | L'affordance doit se voir sans étiquette (règle 7) |
| R5 | **Un focus clavier visible sur la carte entière** quand le titre reçoit le focus (`:has(:focus-visible)`), et un anneau propre au bouton. L'ordre de tabulation est : carte, puis bouton. | Règle 11 ; WCAG 2.4.7 |
| R6 | **« Réduire les animations » est respecté** : pas de déplacement de la carte au survol si l'utilisateur l'a demandé. | Règle 14 |
| R7 | **« Nouveau » se marque toujours au clic sur la carte** : le marquage « déjà vu » suit le lien du titre. | État du système (Nielsen 1, règle 25) |

**Point laissé en l'état** : le bouton mesure **36 px** de haut. C'est au-dessus du minimum de 24 px (WCAG 2.5.8 AA), mais en dessous des 44 px du tactile. Cette page sert surtout sur ordinateur ; à reprendre si elle est consultée sur tablette.

**Vérifié en local** (page rendue avec 4 titres fictifs, Playwright) :
- un clic au centre de la carte, ou dans un coin vide, mène au site ; un clic sur le bouton mène à l'espace de rédaction ;
- plus aucun bouton « Ouvrir » ;
- au survol du bouton, la carte reste immobile, avec sa bordure d'origine ; au survol de la carte, bordure bleue et déplacement de 2 px ;
- le focus clavier encadre la carte ;
- au téléphone (390 px), aucun débordement.

Captures : `portail_1_survol.png`, `portail_2_survol_bouton.png`, `portail_3_clavier.png`, `portail_4_tel.png`.
