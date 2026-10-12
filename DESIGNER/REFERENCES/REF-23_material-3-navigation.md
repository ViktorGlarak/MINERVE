# REF-23 — Material Design 3 : navigation, mises en page et vocabulaire

- **Fournie par l'utilisateur le** 2026-10-06 (deux fois).
- **Nature** : système de design de Google. Doc Android Apache 2.0, site CC-BY.
- **Lu** : ⚠ `m3.material.io` ne rend que ses titres (site JavaScript) ; lu à la place `material-components-android/docs/components/` (NavigationRail, BottomNavigation, NavigationDrawer, Tabs, TopAppBar, Dialog, SideSheet, BottomSheet, Menu, Card) et developer.android.com (navigation adaptative, mises en page canoniques, classes de largeur).

## À retenir
1. **Barre de navigation** : 3 à 5 destinations (petits écrans). **Rail** : 3 à **7 destinations au plus**, tablette et bureau. **Le tiroir est déprécié** (M3 Expressive) au profit du **rail étendu**, non modal, qui se replie en rail.
2. **Choix selon la largeur** : < 600 dp compact, 600-840 moyen, 840-1200 étendu, 1200-1600 grand, ≥ 1600 très grand. Nos postes d'animation sont « grands » ou « très grands » : rail étendu permanent.
3. **Onglets primaires** (sous la barre d'app, destinations de contenu) et **secondaires** (subdivisions dans un contenu) ; fixes (tous visibles) ou défilants.
4. **Barre d'application** qui devient **barre d'actions contextuelles** pendant une sélection.
5. **Trois mises en page canoniques** : **liste-détail** (deux volets côte à côte), **volet d'appui** (~70/30, contenu qui n'a de sens que par rapport au principal), **flux** (grille de cartes ≥ 180 dp).
6. **Vocabulaire des surfaces** : boîte de dialogue = décision ou information critique ; volet latéral / inférieur = contenu secondaire ; menu = choix sur surface temporaire ; carte = un sujet et ses actions.

## Ce que ça change pour nos projets
- **Au plus 7 destinations primaires par app** ; le reste en onglets secondaires, menus ou volets.
- **Liste-détail** pour planches d'injects, scénarios, messagerie ; **volet d'appui** pour l'aide ou le contexte d'un objet ; **flux** pour la veille.
- Un **vocabulaire commun** pour nommer les éléments quand DESIGNER explique un écran (rail, onglet, volet, menu, carte, dialogue).
