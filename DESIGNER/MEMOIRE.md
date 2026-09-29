# MÉMOIRE — DESIGNER

> **Agent n°24 du système MINERVE** — créé le **2026-09-24** à la demande de l'utilisateur.
> Rôle : **conseiller en design** des sites et applicatifs que nous créons (PLÉIADE, sites d'exercice, outils MINERVE).
> ⭐ **RÉFLEXE : CONSULTER cette mémoire AVANT tout conseil de design · CONSIGNER APRÈS chaque document ingéré ou avis rendu** (compte rendu daté dans `JOURNAL.md`).

---

## 1. Mission et limites (décision utilisateur, 2026-09-24)

- **Maîtriser tous les documents** que l'utilisateur fournit, au fil du temps : les **analyser**, les **comprendre**, les **ingérer** (une fiche par source dans `REFERENCES\`, la synthèse au §3).
- **Conseiller** sur le design : ce qui rend un écran plus agréable et plus efficace **pour l'humain** qui l'utilise.
- ⚠ **DESIGNER n'a pas la VÉRITÉ sur nos projets.** Il **contribue**, il ne tranche pas. Ce qui fait foi :
  - le **besoin exprimé par l'utilisateur** ;
  - les **chartes des médias fictifs** (MASTAURIGE, maquettes press : reproduction **fidèle**, un conseil de « beauté » ne les modifie pas) ;
  - les **modèles officiels** (comptes rendus PSYREP / CIMICREP, documents d'ordres : reproduits **à l'identique**) ;
  - les choix d'architecture de **PLEIADE / ARCHITECTE**.
  → Un conseil de DESIGNER est toujours **formulé comme une proposition argumentée** (quelle loi, quelle source), jamais comme une correction imposée.
- Il **améliore les compétences** de l'assistant : les principes ci-dessous s'appliquent à tout écran produit, même sans que DESIGNER soit explicitement sollicité.

## 2. Terrain : ce que nous construisons (relevé le 2026-09-24)

| Famille | Apps | Habillage actuel |
|---|---|---|
| **Thème « PLÉIADE » sombre** | `app-admin`, rédaction d'`app-press` | jetons `--color-shell / panel / sunken / field / line* / ink*` (`pleiade-theme.css`), police **Archivo**, icônes **lucide-react** |
| **Thème « graphite / craie »** | `app-melmil`, `app-leac` | échelle `--color-graphite-50…900` + `--color-craie`, **Archivo** + **JetBrains Mono** pour les codes, **pas d'icônes** |
| **Sites d'exercice** | `app-press` (10 maquettes : TV4, BC1, ONU, OTAN, TF1…), `app-social`, sites MASTAURIGE | **chartes de médias à reproduire** (hors du champ des conseils esthétiques) |
| Orchestrateur | `pleiade-platform` | Tailwind 4 compilé, police système |
| Non habillé | `eho` | gabarit Next.js par défaut (Arial) → **candidat n°1 à un habillage PLÉIADE** |

Toutes les apps sont en **Tailwind CSS 4**. Aucune n'utilise Radix, shadcn ou Motion.

**Publics** : des **animateurs d'exercice** qui travaillent vite et sous pression, sur ordinateur (MELMIL, admin, cockpit), des **contrôleurs de terrain** sur tablette hors ligne (LEAC), et des **joueurs** qui doivent croire aux médias fictifs.

## 3. ⭐ Doctrine de design (synthèse des sources ingérées)

> Chaque règle renvoie à sa source. Une règle sans source est un avis, et doit être présentée comme tel.

### 3.1 Système avant écran
1. **Des jetons sémantiques, en paires surface / texte** (`background/foreground`, `card`, `muted`, `primary`, `destructive`, `border`, `ring`…), un mode sombre obtenu en **redéfinissant les mêmes noms** — REF-01.
2. **Couleurs en `oklch`** : la clarté est régulière d'une teinte à l'autre, ce qui rend le contraste prévisible — REF-01, REF-07.
3. **Limiter les choix à l'avance** : une échelle d'espacements, une échelle typographique, 9 à 10 nuances par teinte — REF-07.
4. **Des gris teintés**, jamais neutres ; **pas de texte gris sur un fond coloré** — REF-07.

### 3.2 Hiérarchie et lisibilité
5. **Mettre en valeur en atténuant le reste**. La taille n'est qu'un des moyens, avec le poids et la couleur — REF-07.
6. **Une seule action principale par écran** (`primary`) ; les autres en secondaire ou discrètes — REF-01, Hick REF-06.
7. **L'étiquette est un dernier recours** : la forme de la donnée doit parler d'elle-même — REF-07.
8. Lignes de **45 à 75 caractères** ; **interligne plus grand pour le texte courant, plus serré pour les titres** — REF-07.
9. **Pas d'espacement ambigu** : l'écart à l'intérieur d'un groupe est nettement plus petit que l'écart entre les groupes (proximité) — REF-07, REF-06.

### 3.3 Comportement et accessibilité
10. **Ne jamais transmettre une information par la couleur seule** : doubler par un texte, une icône ou une forme — REF-07. *(Appliqué : les feux TLS du CIMICREP portent la lettre G, A ou R en plus de la couleur.)*
11. **Clavier et focus** : fenêtre modale avec piège du focus, `Échap` pour fermer, **retour du focus au déclencheur**, fond inerte ; onglets au clavier avec les flèches ; anneau de focus visible (`ring`) — REF-02, REF-19, REF-13 (2.1.2, 2.4.7).
12. **Cibles assez grandes et espacées** : **24 × 24 px au minimum** (WCAG 2.5.8 AA), **44 × 44 en tactile** (2.5.5 AAA, retenu pour LEAC) — Fitts REF-06, REF-13.
13. **Réponse à l'écran en moins de 400 ms**, même si l'enregistrement suit — Doherty REF-06.
14. **Respecter « réduire les animations »** ; animer seulement `transform` et `opacity`, sur 150 à 250 ms ; une animation doit expliquer, pas décorer — REF-09.

### 3.3 bis Couleur et contraste, en chiffres
21. **Contraste** : texte **4,5 : 1**, grand texte **3 : 1**, **bords de champs, icônes et focus 3 : 1** — REF-13, REF-16.
22. **Une échelle à usages fixés** (12 crans à la Radix : 1-2 fonds, 3-5 états d'un composant, 6-8 bordures, 9-10 aplats, 11-12 textes). Personne n'a plus à « choisir une nuance » — REF-15, REF-07.
23. **Des couches qui alternent** : page → panneau → carte, chacune distincte de celle qui la porte ; un champ prend la teinte de la couche où il est posé — Carbon REF-12.

### 3.4 Parcours
15. **Faire comme les autres** là où l'utilisateur a déjà ses habitudes (Jakob) ; innover seulement là où ça apporte quelque chose — REF-06.
16. **Moins de choix quand le temps presse** ; **mettre en avant l'option recommandée** ; découper les tâches longues — Hick REF-06.
17. **Tolérant en entrée, strict en sortie** (Postel) : c'est déjà la règle des imports JEMM et CR — REF-06.
18. **Soigner les états vides et la fin des parcours** (Peak-End) : premier écran vide qui dit quoi faire, confirmation nette à la fin — REF-06, REF-07.
19. **La complexité incompressible est portée par le système** (Tesler) : pré-remplir ce que l'app sait déjà (exemple : GDH et n° de message des comptes rendus) — REF-06.
20. **Une seule couleur d'alerte, rare** (Von Restorff) — REF-06.
24. **Erreurs à la GOV.UK** : un résumé en haut, qui reçoit le focus, chaque erreur reliée à son champ, un texte qui dit **comment corriger** ; les champs facultatifs sont marqués « (facultatif) », pas d'astérisque — REF-10, REF-14 (heuristique 9).
25. **L'état du système toujours visible** : enregistré, en cours, en direct, en conflit — Nielsen 1, REF-14.
26. **Texte courant de 14 à 16 px dans les outils, interligne de 1,35 à 1,45, lignes de 45 à 90 caractères** pour les textes longs — REF-17, REF-07.

### 3.6 Grille d'audit d'un écran
1. Passer l'écran au crible des **10 heuristiques de Nielsen** (REF-14), en notant chaque problème de **0 à 4** selon sa gravité.
2. Passer la **liste A11Y Project** (REF-16) et les seuils **WCAG** (REF-13).
3. Vérifier la **hiérarchie** : une seule action principale ? le regard va-t-il d'abord à l'essentiel ? (REF-07)
4. Rendre **3 à 5 recommandations** classées par gain pour l'utilisateur, chacune sourcée, avec une **estimation de l'effort**.

### 3.5 Outils de référence (à recommander, sans les imposer)
- ⛔ **DSFR, Marianne, GDS Transport** : réservés aux sites de l'État français et de GOV.UK. On s'inspire de leurs **méthodes**, jamais de leur **identité**, y compris sur les sites d'exercice (REF-10, REF-11).
- **Comportement accessible** : Radix Primitives (REF-02) ; **composants à posséder** : shadcn/ui (REF-01) ; **motifs HTML/Tailwind** : HyperUI (REF-03) ; **icônes** : Lucide (REF-08, déjà en place) ; **animation** : Motion (REF-09), et seulement quand le CSS ne suffit pas.
- **Systèmes de comparaison** : **Carbon** (IBM) et **Blueprint** (Palantir) pour nos outils de données denses ; Polaris pour la rédaction des interfaces ; Material comme référence de ce que les joueurs connaissent — REF-04, REF-05.

## 4. Index des sources ingérées

| N° | Source | Fiche | Date |
|---|---|---|---|
| REF-01 | shadcn/ui | `REFERENCES\REF-01_shadcn-ui.md` | 2026-09-24 |
| REF-02 | Radix Primitives | `REFERENCES\REF-02_radix-primitives.md` | 2026-09-24 |
| REF-03 | HyperUI | `REFERENCES\REF-03_hyperui.md` | 2026-09-24 |
| REF-04 | Awesome Design Systems (klaufel) | `REFERENCES\REF-04_awesome-design-systems.md` | 2026-09-24 |
| REF-05 | Awesome React Design Systems (jbranchaud) | `REFERENCES\REF-05_awesome-react-design-systems.md` | 2026-09-24 |
| REF-06 | Laws of UX | `REFERENCES\REF-06_laws-of-ux.md` | 2026-09-24 |
| REF-07 | Refactoring UI | `REFERENCES\REF-07_refactoring-ui.md` ⚠ page publique + 1 chapitre gratuit (palette) | 2026-09-24 |
| REF-08 | Lucide | `REFERENCES\REF-08_lucide.md` | 2026-09-24 |
| REF-09 | Motion | `REFERENCES\REF-09_motion.md` | 2026-09-24 |
| REF-10 | GOV.UK (principes + Design System) | `REFERENCES\REF-10_gov-uk.md` | 2026-09-24 |
| REF-11 | DSFR ⛔ inspiration seulement | `REFERENCES\REF-11_dsfr.md` | 2026-09-24 |
| REF-12 | IBM Carbon | `REFERENCES\REF-12_ibm-carbon.md` | 2026-09-24 |
| REF-13 | WCAG 2.2 A/AA | `REFERENCES\REF-13_wcag-2-2.md` | 2026-09-24 |
| REF-14 | 10 heuristiques de Nielsen | `REFERENCES\REF-14_nielsen-heuristiques.md` | 2026-09-24 |
| REF-15 | Radix Colors (12 crans) | `REFERENCES\REF-15_radix-colors.md` | 2026-09-24 |
| REF-16 | A11Y Project checklist | `REFERENCES\REF-16_a11y-project-checklist.md` | 2026-09-24 |
| REF-17 | Practical Typography | `REFERENCES\REF-17_practical-typography.md` | 2026-09-24 |
| REF-18 | Inclusive Components (index) | `REFERENCES\REF-18_inclusive-components.md` | 2026-09-24 |
| REF-19 | WAI-ARIA APG (Dialog, Tabs) | `REFERENCES\REF-19_wai-aria-apg.md` | 2026-09-24 |
| REF-20 | Ressources libres (bradtraversy) | `REFERENCES\REF-20_ressources-libres.md` | 2026-09-24 |

**Méthode d'ingestion** (pour chaque nouveau document) :
1. Lire la source entière, y compris sa documentation quand la page d'accueil est trop mince.
2. Écrire la fiche `REF-NN_nom.md` : source, date, licence, nature, ce qu'il faut retenir, et ce que ça change pour nos projets.
3. Ajouter ou affiner les règles du §3, avec le renvoi à la fiche.
4. Mettre l'index à jour et consigner au `JOURNAL.md`.
5. Signaler les **contradictions** entre sources au lieu de les trancher en silence.

## 5. Décisions et questions

- ✅ **Décision utilisateur (2026-09-24)** : **le gaver de sources fiables**, publiques et gratuites, pour qu'il devienne vraiment expert. DESIGNER **propose lui-même** les sources à lire (§5 bis).
- ✅ **Refactoring UI** : l'utilisateur n'a pas le livre. On s'en tient aux **extraits gratuits publiés par les auteurs**, sans aucune copie piratée.
- ✅ **Pas de thème PLÉIADE unifié** pour l'instant (décision utilisateur) : chaque app garde sa famille, et DESIGNER conseille à l'intérieur de chacune.

## 5 bis. Sources à ingérer ensuite (libres et gratuites, par priorité)
1. **Inclusive Components**, articles complets : onglets, repliables, notifications, boutons bascule (REF-18).
2. **WAI-ARIA APG**, autres modèles : Disclosure, Menu Button, Grid/Treegrid, Toolbar, Tooltip (REF-19).
3. **Apple Human Interface Guidelines** (developer.apple.com/design) : référence du **tactile** (LEAC sur tablette).
4. **Material Design 3** (m3.material.io) : ce que les joueurs connaissent (Android), mouvement, états.
5. **GitHub Primer** (primer.style) et **Atlassian Design** (atlassian.design) : outils denses, rédaction des interfaces.
6. **web.dev — Learn Design** et **Learn Accessibility** (Google, cours gratuits).
7. **Open Props** (github.com/argyleink/open-props) et **Utopia** (utopia.fyi) : échelles de jetons et typographie fluide.
8. **APCA** (git.apcacontrast.com) : le futur modèle de contraste, déjà utilisé par Radix Colors.
9. Les autres articles de NN/g sur les tableaux de bord, les tableaux de données et les formulaires.

## 6. Avis rendus

| Date | Écran | Recommandations | Suite |
|---|---|---|---|
| 2026-09-24 | **app-melmil** (planche JEMM, atelier, 8 onglets) : `AVIS\2026-09-24_MELMIL\AVIS.md` avec les captures | R1 emplacement évident (bande et étiquette par espace) · R2 haut de page compacté · R3 onglets groupés en Construire / Visualiser / Organiser · R4 échelle typographique d'outil · R5 planche claire, rouge réservé aux alertes · R6 incidents en tableau · R7 fiches structurées · R8 lot accessibilité | ✅ **tout appliqué**, **validé par l'utilisateur** et **en production** le 2026-09-24 à 15:04 (`app-melmil` `2026-09-24.3`). Reste : découper les fiches storylines en sections |
| 2026-09-24 | **app-leac** (8 écrans × 4 tailles) : `AVIS\2026-09-24_LEAC\AVIS.md`, captures `avant\` et `apres\` | R1 une barre de navigation unique (en bas < 1024 px, latérale au-delà) · R2 trois mises en page · R3 rangées de boutons par écran retirées · R4 filtres de la grille sur téléphone · R5 grille alignée à gauche (piège `.frappe`) · R6 accueil. **Contrainte respectée** : parti pris LEAC validé le 17/09 (48 px, contraste, clair, mention en un appui) | ✅ appliqué, **validé** (« c'est parfait ») et **en production** le 2026-09-24 à 15:56 (`app-leac` `2026-09-24.1`) |
| 2026-09-24 (soir) | **app-leac v2**, carte blanche **architecture comprise** : `AVIS\2026-09-24_LEAC\PROPOSITION_V2.md`, captures `v2\` | système visuel (rayons, ombres, 3 rôles de bouton, segmenté, progression, encarts) + en-tête compact, accueil, carnet, grille, bilan, paramétrage. ⭐ **Leçon** : mesurer le mobile avec l'émulation d'appareil et le texte agrandi (débordement réel manqué sinon) | ✅ **validé et en production** le 2026-09-24 à 16:54 (`app-leac` `2026-09-24.2`) |
| 2026-09-24 (soir) | **app-melmil v2**, architecture comprise : `AVIS\2026-09-24_MELMIL_V2\PROPOSITION.md` | R1 système visuel v2 · R2 bandeau (espace toujours visible, menu compte < 900 px, 2 lignes si texte agrandi) · R3 « Plus ▾ » · R4 vue **Liste par jour** (défaut téléphone) · R5 parcours GT compact · R6 onglets défilants · R7 incidents en cartes, fiches plein écran · R8 filet anti-débordement. ⭐ **Leçons** : sur téléphone, menus en **feuille basse** (un menu ancré sort de l'écran quand la barre passe à la ligne) ; un **code ne se coupe jamais** (`overflow-wrap: normal` sur le mono) ; mesurer aussi ce qui sort **à gauche** | 🟡 **local**, branche `refonte-v2` `03e3363` (`2026-09-24.5`) — 0 débordement sur 4 téléphones × 100/150 %, iPad, 1440 px ; **en attente de validation** |
| 2026-09-24 (soir) | **eho** (13 écrans × 3 tailles, animateur + joueur), **propositions seules, sans code** : `AVIS\2026-09-24_EHO\AVIS.md`, captures `captures\` | 12 problèmes, dont **2 de gravité 4** : **mode sombre à moitié fait** (blanc sur blanc sur un poste en sombre) et **menu de 256 px au téléphone** (134 px de contenu). 11 recommandations en 3 lots : R1 mode sombre · R2 navigation par taille (onglets en bas pour le joueur) · R3 tableaux en cartes · R4 **ranger sans glisser** (WCAG 2.5.7) + sélection multiple · R5 planche relationnelle (aide « ? », zoom lisible, état « Enregistré », consultation au téléphone) · R6 actions destructrices · R7 tableau de bord en phrases · R8 couleur = pays/camp · R9 petit système · R10 pastilles pays · R11 connexion. ⭐ **Leçon** : toujours tester le **mode sombre du système** (`colorScheme: "dark"`) | 🟡 **appliqué en local** le soir même (`eho` `refonte-v2` : `7263464` charge, `f3bece5` R1–R11, `f67be82`), **+ chargement par groupe** exigé par l'utilisateur (3 500 avatars). ⭐ **Leçons** : (1) vérifier dans le CODE avant d'affirmer un manque (P4 : la fiche offrait déjà la zone au clavier) ; (2) Tailwind 4 = bordures `currentColor` par défaut → cadres noirs ; (3) une liste de milliers d'éléments = **paginer l'affichage + mémoïser les cartes + recherche différée**, et ne charger le détail qu'à l'ouverture. ✅ **En ligne le 2026-09-25** (`2026-09-24.2`). |
| 2026-09-25 | **eho, écran Avatars** : défilement, préchargement, retour à l'état initial — `AVIS\2026-09-25_EHO_AVATARS\AVIS.md` | R1 un gros bloc (> 16) devient un **rail borné** (`min(60vh, 34rem)`) qui défile en lui-même, tranche suivante préchargée **avant** la fin, `overscroll-behavior: contain`, fondu d'affordance · R2 compteur + **« Revenir au début »** (décharge et remonte) · R3 cartes d'un bloc **complètes** (fiche instantanée) ; recherche : préchargement au survol, échec dit + « Réessayer » · R4 portraits `lazy` + `async` · R5 même règle sur tous les écrans. ⭐ **Doctrine ajoutée** : **pas de défilement infini de page** (on perd ses repères, Nielsen 6) → rail borné ; la **virtualisation** seulement au-delà de ~1 500 cartes par bloc | ✅ **en ligne le 2026-09-25 à 08:59** (`eho` `a3bf90a`, `2026-09-25.1`) : 60 → 420 cartes au défilement sans que la page grandisse, retour à 60, fiche ouverte avec bio sans attente, 0 débordement au téléphone |
| 2026-09-29 | **app-press, maquettes existantes** Today Mercure, HEXAGONE, TV4, Bothnia Channel 1 (les 6 reprises de sites réels exclues) — `AVIS\2026-09-29_PRESSE_MAQUETTES\AVIS.md`, captures `avant\` et `apres\` | R1 vignette à la marque au lieu d'un pavé vide · R2 une hiérarchisée (principal + 2 secondaires ; HEX premier en 2 × 2) · R3 grilles en rangées complètes · R4 plus de doublons (Latest hors une, slogan, triple titre HEX) · R5 bandeaux en boucle + réduire les animations · R6 contrastes et tailles · R7 téléphone (TM 4 356 → 3 437 px) · R8 TM : « 18+ » et mention d'enregistrement (sites d'État russes). ⭐ **Doctrine** : une maquette de média fictif s'**optimise dans sa charte** (structure, hiérarchie, lisibilité), jamais dans son identité ; tester avec **des articles sans photo** et **des images différées** (défiler avant la capture) | 🟡 **local**, `app-press` branche `design-maquettes` `48b1072`, image reconstruite et tests OK ; **en attente de validation** |
| 2026-09-28 | **MELMIL, « Confié à »** par groupes — `AVIS\2026-09-28_MELMIL_CONFIE\AVIS.md` | R1 le choix suit la hiérarchie (event → groupe, storyline → sous-groupe, incident → personnes) · R2 pastilles d'un clic, ✓ + couleur · R3 « rien de coché » écrit en clair (« tout le sous-groupe gère ») · R4 état vide qui dit où agir · R5 l'ancienne attribution gardée · R6 résultat visible (colonne, en-tête, fiche personne) | ✅ **en ligne le 2026-09-28** (`app-melmil` `a65d6f2`) |
| 2026-09-28 | **MELMIL, organigramme** : placer les groupes reliés — `AVIS\2026-09-28_MELMIL_PLACEMENT\AVIS.md` | R1 retirer « Aucune personne » (le 0 le dit) · R2 la proximité suit la relation : colonnes reliées côte à côte, sous-groupe du côté de son partenaire · R3 placement déterministe (même dessin partout) | ✅ **en ligne le 2026-09-28** (`app-melmil` `04b3a15`) |
| 2026-09-28 | **MELMIL, Équipe v2** : l'organigramme — `AVIS\2026-09-28_MELMIL_ORGANIGRAMME\AVIS.md` | R1 l'exercice est le cadre, pas le centre · R2 organigramme à toute profondeur, personnes dans chaque carte · R3 un seul parent + liens « travaille aussi avec » (pointillé ET « ↔ X » écrit) · R4 légende · R5 défilement dans le cadre, jamais la page. ⭐ **Doctrine** : une mise en page radiale plafonne la profondeur et confond « contenir » avec « être au centre » → organigramme pour une structure militaire | ✅ **en ligne le 2026-09-28** (`app-melmil` `84294f7`) |
| 2026-09-28 | **MELMIL, onglet Équipe** : l'architecture de l'exercice — `AVIS\2026-09-28_MELMIL_EQUIPE\AVIS.md` | R1 lire d'abord (GRADE Nom), modifier dans le panneau · R2 araignée à 2 couronnes + liste (téléphone) · R3 grade, groupe, fonction et compte choisis, pas tapés · R4 couleur de groupe toujours doublée du nom · R5 une seule action principale (« + Groupe ») · R6 état vide qui guide · R7 rien de l'existant perdu (groupes implicites, grade séparé du nom) | ✅ **en ligne le 2026-09-28** (`app-melmil` `f9f72b6`, `2026-09-28.1`) |
| 2026-09-28 | **eho, groupes** : ranger 235 groupes — `AVIS\2026-09-28_EHO_RANGER_GROUPES\AVIS.md` | R1 masquer, ne pas supprimer (les autres apps tiennent les groupes par id) · R2 un assistant qui propose par famille, l'humain valide · R3 le résultat avant d'appliquer · R4 aucune supposition invisible (exercice en cours à choisir) · R5 archives repliées, « Ressortir » d'un clic | ✅ **en ligne le 2026-09-28** (`eho` `8bb7084`, `2026-09-28.1`) |
| 2026-09-27 | **LEAC, bandeau** : pastille d'état du réseau — `AVIS\2026-09-27_LEAC_PASTILLE_RESEAU\AVIS.md` | R1 état permanent au même endroit · R2 trois états, texte + forme (rond plein / demi-rond / croix) · R3 ne dire que le mesuré (marque du worker + `/api/sante`, jamais `navigator.onLine`) · R4 un appui explique et propose l'action · R5 « copie + serveur qui répond » = certificat suspect, dit en clair | ✅ **en ligne le 2026-09-27** (`app-leac` `a4639f3`, `2026-09-27.1`) |
| 2026-09-25 | **MELMIL, planification** : choisir les ETIM d'un incident — `AVIS\2026-09-25_MELMIL_ETIM\AVIS.md` | R1 une **liste d'ETIM par exercice** (Réglages), pas de saisie libre : les variantes ne se regroupent plus · R2 dans la fiche, des **pastilles cochées d'un toucher** (pleine + ✓ / cerclée + « + », 32 px, `aria-pressed`) · R3 « Autre ETIM… » sur place, arrive cochée · R4 le nom en clair sur la carte de la planche (étiquette sombre), dans le tableau et dans la liste par jour · R5 état vide qui dit quoi faire. Écarté : une couleur par ETIM (la couleur porte déjà la storyline) | ✅ **en ligne le 2026-09-25** (`app-melmil` `5b4d76a`, `2026-09-25.1`) |
| 2026-09-25 | **eho, onglet Groupes** : voir les membres d'un groupe — `AVIS\2026-09-25_EHO_GROUPES\AVIS.md` | R1 toute la ligne ouvre (chevron `›`), le menu « ⋯ » reste à part · R2 fenêtre commune d'eho (Échap, focus piégé, retour) · R3 en-tête pastille + nom + effectif, recherche instantanée · R4 une ligne par membre : portrait 32 px (initiales si absent ou cassé), **Prénom Nom** + `@compte` (écrit une seule fois s'ils sont identiques), badge Inactif, lien « Fiche › » · R5 « Copier les @ » · R6 squelettes + `content-visibility`. ⚠ Sécurité : la route des membres était ouverte aux joueurs → réservée à l'animation | ✅ **en ligne le 2026-09-25** (`eho` `124679a`, `2026-09-25.4`) : groupe de 396 membres ouvert en 0,2 s, recherche « 286 sur 396 », 0 débordement au téléphone, joueur 403, anonyme 401 |
