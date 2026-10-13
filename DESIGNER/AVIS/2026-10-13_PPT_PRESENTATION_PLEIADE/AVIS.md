# Avis DESIGNER n°107 — 2026-10-13 — Diaporama de présentation de PLÉIADE (10 diapositives, 16:9)

> **Lu** : `original.pdf` (10 pages, 960 × 540 pt = format PowerPoint 16:9 de 13,33 × 7,5 po, texte vectorisé « Glyphless », donc polices identifiées à l'œil), rendu à 72 et 144 dpi pour mesurer ; `PLEIADE\PRESENTATION\PLEIADE_DOSSIER_DE_PRESENTATION.md` (§13 plan, §14 précautions) ; charte PLÉIADE (`PLEIADE\MEMOIRE.md` « Le design system Pléiade », jetons réels de `app-cockpit\src\app\pleiade-theme.css` et `pleiade-theme-light.css`) ; logo du portail (`pleiade-platform\public\index.html`, constellation en craie) ; icônes d'apps du portail (`public\img\apps\`).
> **Besoin** : un officier présente PLÉIADE à des décideurs et cadres de la Défense. L'utilisateur veut « quelque chose de beaucoup plus propre ».
> **Hors champ** : la justesse des chiffres (analyse parallèle). Je signale seulement les chiffres dont le **dossier lui-même** interdit l'usage comme preuve (§6.5), parce que cela change la mise en page de la diapo 8.
> Ce sont des **propositions** : le besoin de l'utilisateur et les choix de PLEIADE priment.

---

## 1. Diagnostic global

**En une phrase** : le deck est propre au sens « soigné », mais c'est un **document à lire** (92 à 139 mots par diapo, texte à 13-15 pt) habillé d'une **identité qui n'est pas celle de PLÉIADE** (marine, or, empattements), sans **un seul visuel** pour présenter un produit visuel.

| # | Constat | Mesure | Règle | Gravité |
|---|---|---|---|---|
| G1 | **Texte trop petit pour une salle.** Corps des cartes à ~13 pt (p. 4, 5, 7 : interligne 17 pt), ~14-15 pt (p. 2, 9), pied de page ~11 pt. | Sur un écran de 2 m de base, 13 pt donne une capitale de ~19 mm, soit **8 minutes d'arc vues à 8 m**. Le seuil de lecture confortable est de 16 à 22 minutes d'arc (norme ergonomique ANSI/HFES 100, *source externe à ma doctrine, à vérifier*). Il faut **24 pt** pour atteindre ~15' à 8 m sur 2 m, ~23' sur 3 m. | Lisibilité (priorité 2 de la knowledge) ; corps « 16 px minimum, plus pour un public large » (principes-ui §2) transposé à la distance | **Bloquant** |
| G2 | **Trop de mots.** 92 (p. 2) à 139 (p. 9) mots par diapo de contenu. Le public lit au lieu d'écouter l'officier. | 9 diapos sur 10 au-delà de 90 mots | Charge cognitive : « une idée par section, un titre qui dit la conclusion » (ux-psychologie §1) ; principe de redondance (Mayer, *externe*) | **Bloquant** |
| G3 | **Aucun visuel.** Zéro schéma, zéro capture, zéro icône. Le dossier §13 demande pourtant une frise, un schéma « zone », un tableau programme/IA, une courbe d'opinion, une capture du réseau social. | 0 / 10 | « L'étiquette est un dernier recours : la forme de la donnée doit parler » (règle 7, REF-07) | **Majeur** |
| G4 | **Ce n'est pas l'identité PLÉIADE.** Marine `#14213D` + or `#E8A93A`, titres à empattements (type Garamond) + sans-serif type IBM Plex, cartes à coins arrondis (~8 px). La charte PLÉIADE : **graphite + craie seule couleur de marque, angles vifs, Archivo + JetBrains Mono, aucune ombre**, mention « Exercice · non classifié ». | 0 jeton de la charte repris | Cohérence et standards (Nielsen 4) ; Jakob (règle 15) : le public verra ensuite les vrais écrans | **Majeur** |
| G5 | **Six couleurs d'accent sans signification.** Or, sarcelle `#5CC2AD`, rose `#EF8A96`, rouge `#9B2D3A`, vert (p. 6), brun (chiffres p. 4). Sur la p. 4, chaque numéro d'étape a sa couleur ; p. 3, chaque colonne la sienne ; p. 9, or et sarcelle alternent sans raison. | 6 teintes | « Un seul accent » (principes-ui §3) ; Von Restorff (règle 20) : si tout ressort, rien ne ressort | **Majeur** |
| G6 | **Alternance clair / sombre mécanique** (impaire sombre, paire claire). Elle ne dit rien (pas de chapitres) et fait « pomper » la luminosité de l'écran à chaque clic : l'œil se réadapte. En salle éclairée, un projecteur ne sait pas faire de noir : le marine devient gris bleuté et le contraste réel s'effondre. | 5 bascules sur 10 diapos | Leçon « séquence de fonds alternés » (lessons §4) : l'alternance doit être un choix de structure, pas un réflexe | **Majeur** |
| G7 | **Le tiers bas des diapos est vide** alors que le texte est à 13 pt : p. 4 (~35 %), p. 6 (~30 %), p. 10 (~40 %), p. 2, 5, 7, 8, 9 (~25 %). On a la place de **doubler** le corps. | Mesuré sur rendu | Espacement : contenu calé sur la grille, pas collé en haut | **Majeur** |
| G8 | **Titres descriptifs, pas des messages.** « Une zone par exercice », « Sous le capot… », « Ce que PLÉIADE permet » : le décideur doit déduire la conclusion lui-même. | 7 titres sur 9 | « Un titre qui dit la conclusion » (ux-psychologie §1) | Mineur à majeur |
| G9 | **Typographie française** : « > 1 / 000 » et « ≈ 37 / % » coupés sur deux lignes (p. 8) faute d'**espace insécable** ; tiret cadratin visible p. 1 (« non classifié — pays… »). | p. 1, p. 8 | Leçon « tiret cadratin proscrit » (lessons §6) ; règle typographique française | Majeur (p. 8) |
| G10 | **Contrastes** : corrects en théorie, fragiles en projection. Or sur marine 7,7:1, sarcelle sur carte 6,3:1, rose 5,6:1, gris `#7A8294` sur carte **3,5:1** (p. 9, méta). Un projecteur fait perdre facilement la moitié du contraste. | Calculé (WCAG 2.x) | 1.4.3 ; pour la projection je vise **7:1 pour tout texte à lire** (avis, marge de sécurité) | Mineur |

**Ce qui va** : 16:9 natif, marges latérales régulières (~64 pt), mention « Exercice · non classifié » en pied, numérotation « n / 10 », titres tous à gauche au même endroit, contenu fidèle au dossier, deux formules imposées (« SaaS modulaire », « Digital workspace ») bien reprises.

**Faut-il aligner sur la charte PLÉIADE ?** Je le **recommande** (piste A ci-dessous), pour trois raisons : (1) on présente le produit, le deck doit ressembler aux écrans que le public verra ensuite (Jakob) ; (2) la charte est déjà sobre et « militaire » (graphite, angles vifs), donc adaptée au public ; (3) le logo existe déjà (constellation craie du portail). C'est à l'utilisateur de trancher (identité = choix client).

---

## 2. Défauts diapositive par diapositive

| Diapo | Défauts | Gravité |
|---|---|---|
| **1. Titre** | Identité hors charte (or + empattements). Sous-titre orienté technique (« six mois d'avancées techniques ») alors que le public est décideur : il attend la valeur. Tiret cadratin dans la mention. Pas de logo PLÉIADE alors qu'il existe. Le grand vide à droite n'est pas un choix (rien ne l'habite). | Majeur |
| **2. Terrain crédible** | 4 cartes 100 % texte, corps ~14 pt, chapô de 2 lignes en gris. Le quart bas est vide. Aucune icône pour ancrer les 4 mots. Le titre n'est pas un message. | Majeur |
| **3. Une zone par exercice** | Le **concept central** (zone étanche + apps + identité unique) est rendu par 3 colonnes de texte en 3 couleurs (or, sarcelle, rose) qui ne codent rien. La 3e colonne est à moitié vide. Le bandeau du bas mélange deux anglicismes en gras dans un paragraphe à ~13 pt. Ni l'étanchéité ni l'identité qui circule ne se **voient**. | Bloquant (c'est le cœur du discours) |
| **4. Du scénario à l'écran** | 6 cartes étroites (texte ~13 pt, 4 lignes chacune), numéros à empattements en **6 couleurs différentes**. Pas de flèches : un flux sans direction visible. La phrase clé (« les avatars viennent de l'EHO ») est reléguée en paragraphe sous les cartes. Tiers bas vide. | Majeur |
| **5. Quatre exercices** | Une frise rendue en 5 cartes de texte : ~134 mots, ~13 pt. Étiquettes « CONSTAT / RÉPONSE » répétées 5 fois (le lecteur le comprend dès la 1re). Les dates ne sont pas sur un axe : la durée n'est pas visible. La rupture qui compte (ZIP par mail → serveur unique) n'apparaît pas. Titre sur 2 lignes. | Majeur |
| **6. Avant / après** | Bon contenu, mauvaise forme : tableau de 130 mots à ~13 pt, colonne « après » en **vert** (couleur seule pour dire « mieux »), en-tête marine + or. 30 % bas vide. | Majeur |
| **7. Population simulée** | Bon point focal (« 105 » cerclé). Mais : chiffre en empattements or, 4e et 5e couleurs (sarcelle, or) pour les titres de cartes, puces à ~13 pt, la répartition « 15 / 15 / 70 % » est une ligne de texte alors que c'est une donnée à **montrer**. L'idée forte (« le programme décide, l'IA formule ») est éclatée en deux cartes au lieu d'un schéma. Garde-fous en bandeau de texte. | Majeur |
| **8. Mesurer l'effet** | **Chiffres coupés** : « > 1 / 000 » et « ≈ 37 / % » (boîte trop étroite + espace sécable). Trois styles de texte concurrents (citation à empattements, puces, titre de carte en **rouge**, 6e accent). Surtout : le dossier §6.5 dit de **ne pas utiliser ces deux chiffres comme preuves de succès** (fenêtre de 24 min ; diagnostic d'un défaut). Ces deux encarts doivent partir : la diapo n'a alors plus de visuel, il faut la **courbe d'opinion**. | Bloquant |
| **9. Sous le capot** | 4 cartes, 139 mots, ~14 pt, titres alternés or / sarcelle sans logique. Un schéma (périmètre VPN, serveur, nœuds de calcul) dirait tout en 20 mots. *(Contenu, pour l'analyse des chiffres : « libre de droits » contredit le dossier §8.2, « licence libre Apache 2.0, ce qui n'est pas libre de droits ».)* | Majeur |
| **10. Ce que PLÉIADE permet** | Liste de 5 verbes en gras à ~15 pt + encart sombre de 3 paragraphes. 40 % bas vide. **Pas de demande aux décideurs** : on termine sur « à suivre » sans dire ce qu'on attend d'eux. | Majeur |

---

## 3. Direction de refonte

### 3.1 Deux pistes

| | **Piste A — Charte PLÉIADE (recommandée)** | **Piste B — Garder l'habillage actuel, corrigé** |
|---|---|---|
| Identité | Graphite / craie, Archivo + JetBrains Mono, angles vifs, logo constellation | Marine / or, empattements + sans-serif |
| Gain | Le deck et les écrans parlent la même langue ; sobriété militaire ; une seule couleur à gérer | Moins de travail |
| Compromis | Plus austère : l'emphase passe par l'inversion (bloc graphite plein) et le poids, pas par la couleur. Polices à installer ou incorporer. | Reste étranger au produit ; il faut quand même tout réduire à **un** accent (l'or) et retirer l'empattement des chiffres |

Le reste de l'avis décrit la **piste A**. Toutes les règles de taille, de grille et de plan valent aussi pour B.

### 3.2 Palette (jetons réels de la charte, valeurs de `pleiade-theme*.css`)

**Règle de rythme** : **clair = contenu** (robuste en salle éclairée, où le projecteur ne fait pas de noir), **sombre = moment** (couverture, bascule « Nouveauté DELATTRE 26 », conclusion). 3 diapos sombres sur 11, jamais deux bascules de suite sans raison.

| Rôle | Diapo claire (papier craie) | Diapo sombre (tableau noir) |
|---|---|---|
| Fond | `#F3F0E7` (shell clair) | `#161719` (shell) |
| Surface (cadre, carte) | `#FBFAF6` + trait 1 pt `#C8C2B2` | `#1B1C1F` + trait 1 pt `#35373B` |
| Titre | `#14140F` — **14,5:1** | `#FAFAF7` |
| Corps | `#1C1E21` — **14,7:1** | `#EDEEF2` — **15,5:1** |
| Texte secondaire | `#3B3E46` — **9,4:1** | `#C3C8D8` — **10,2:1** |
| Méta, pied de page seulement | `#5B5F69` — 5,6:1 *(proposé : `#6A7189` = 4,25:1, trop juste en projection)* | `#9AA0B4` — 6,9:1 |
| **Signal / emphase (un seul)** | **bloc graphite plein `#1B1C1F` + texte craie `#EDE3C8`** (inversion, 13,3:1) ; trait de courbe graphite 4 pt | **craie `#EDE3C8`** — 14,0:1 |
| Données secondaires (courbes, flèches neutres) | `#5B5F69` en tirets / pointillés | `#9AA0B4` en tirets |

- **Aucune autre teinte.** Ni or, ni sarcelle, ni rouge, ni vert. Les couleurs de statut de la charte (`online`, `dev`, `halt`) ne servent pas dans un deck : elles disent « en ligne / en travaux / arrêté ».
- **Pas de rouge / bleu de camp** en décoration : dans l'univers d'exercice, ils veulent dire « camp ». Uniquement si une diapo montre des camps, et alors **doublés du mot** (règle 10).
- « En essai », « À l'étude » : **symbole + mot**, pas de couleur (◌ En essai · ○ À l'étude · → Ensuite), comme l'avis n°104.

### 3.3 Typographies

| Usage | Police | Graisse | Repli si non installée |
|---|---|---|---|
| Titres, corps, chiffres clés | **Archivo** (SIL OFL, incorporable) | 400 / 500 / 700 / 800 | **Arial** (Arial Black pour les chiffres clés) |
| Repères courts : dates de la frise, noms de zone, « J+3 », étiquettes d'état | **JetBrains Mono** (SIL OFL) | 500 / 700, **jamais sous 18 pt** | **Consolas** |

- **Aucune police à empattements** (absente de la charte, utilisée de façon incohérente dans l'original).
- Chiffres : Archivo ExtraBold, chiffres tabulaires (déjà la règle de la charte, `tabular-nums`).
- **Livraison PowerPoint** : installer les TTF statiques (Archivo Regular, Medium, Bold, ExtraBold ; JetBrains Mono Medium, Bold) sur le poste de fabrication, puis **Fichier › Options › Enregistrer › Incorporer les polices › Tous les caractères**. Le poste de présentation (souvent un poste de la Défense, sans droits d'installation) affichera alors les bonnes polices. **Toujours emporter aussi le PDF** et tester sur l'ordinateur et le projecteur de la salle (leçon de l'avis du 2026-09-30, export PowerPoint de MELMIL : « valider dans PowerPoint », pas seulement dans l'outil qui fabrique).
- Typographie française : **espace fine insécable** (U+202F) dans « 4 000 », avant « % », « : », « ? » ; dans PowerPoint, à défaut, **Ctrl + Maj + Espace** (insécable). Pas de tiret cadratin : virgule, deux-points ou deux phrases.

### 3.4 Échelle typographique (pt PowerPoint, diapo 13,33 × 7,5 po)

| Niveau | Taille | Interligne | Usage |
|---|---|---|---|
| Couverture | 72 pt, 800, capitales espacées 0,08 em | 1,0 | « PLÉIADE » |
| Chiffre clé | 96 à 120 pt, 800 | 0,95 | « 105 », « 4 000 » |
| **Titre-message** | **32 pt, 700** | 1,1 | une phrase, **2 lignes max, ~70 caractères** |
| Chapô / sous-titre | 24 pt, 500 | 1,25 | une ligne sous le titre, facultatif |
| **Corps** | **24 pt, 400** (plancher **20 pt**) | 1,3 | texte des schémas, listes courtes |
| Légendes de schéma | **18 pt** minimum, 500 | 1,2 | étiquettes, axes |
| Pied de page | 12 pt | — | mention, numéro (pas destiné à être lu du fond) |

Ratio ~1,33 (quarte, principes-ui §2). **Plafond : 40 mots par diapo hors titre** (avis DESIGNER : au-delà, le public lit au lieu d'écouter ; le détail va dans les notes de l'orateur).

### 3.5 Grille 16:9 (960 × 540 pt)

- **Marges** : 48 pt à gauche et à droite (5 %), 40 pt en haut, 32 pt en bas. Rien d'important à moins de 48 pt d'un bord (certains projecteurs rognent).
- **12 colonnes** de 50 pt, **gouttières de 24 pt** (largeur utile 864 pt). Divisions utiles : 6 + 6, 4 + 4 + 4, 8 + 4, 3 × 4.
- **Pas vertical de 8 pt.**
- **Zones fixes** (mêmes sur toutes les diapos claires) :
  - titre-message : y 40 → 120 ;
  - contenu : y 144 → 476 (332 pt de haut) ; **le visuel principal occupe au moins la moitié** de cette zone ;
  - pied : ligne de base à y 516 : à gauche logo constellation 12 pt + « PLÉIADE · Exercice · non classifié », à droite « n / 11 ».
- **Angles vifs** (rayon 0), **aucune ombre**, traits 1 pt (cadres) ou 2 pt (périmètres, flèches). Flèches à pointe pleine, une seule forme dans tout le deck.

### 3.6 Iconographie

- **Lucide** (licence ISC, déjà utilisée dans les apps), en SVG inséré dans PowerPoint (recolorable), **une seule épaisseur** : trait 2 à 2,5 pt pour une icône de 40 à 48 pt.
- **Ne pas reprendre les icônes du portail** (`public\img\apps\`) : styles hétérogènes (clip-art couleur, carré violet, grille) et **la même image pour social, messagerie, cockpit et admin**. En salle, quatre apps identiques = confusion. *(Remontée PLEIADE, hors de cet avis.)*
- Correspondance proposée (noms à vérifier sur lucide.dev) : EHO `id-card` · Réseau social `message-square-text` · Presse `newspaper` · Messagerie `send` · MELMIL `kanban` · Console d'animation `calendar-clock` · COCKPIT `gauge` · Moteur IA `cpu` · LEAC `clipboard-check` · Serveur de fichiers `folder` · WordPress `globe` · VPN `lock` · Connexion unique `key-round` · Zone `square-dashed` ou cadre dessiné.
- **Une icône est toujours accompagnée de son nom** (jamais seule).

### 3.7 Les quatre schémas

**S1 — Schéma « zone »** (diapo 5)
- Un **grand cadre graphite 2 pt** = la zone, titré en mono « ZONE DELATTRE 26 ». À l'extérieur, à gauche, une seule porte : icône `lock` « Accès VPN nominatif » puis `key-round` « Une connexion ».
- Dans le cadre, **trois groupes** (Préparer · Jouer · Observer), libellés en capitales 18 pt, chacun 2 à 3 tuiles (icône + nom, 24 pt). Pas de couleur par groupe : c'est l'espace (proximité) qui groupe.
- En bas du cadre, sur toute la largeur, une **barre pleine graphite** « EHO · une fiche par personnage ».
- **Le fil rouge, qui est le seul élément en emphase** : un même avatar fictif (initiales dans un rond, `@nom_fictif`) part de la barre EHO et monte, par trois traits graphite 3 pt, vers Réseau social, Presse et Messagerie, où on le retrouve à l'identique. Légende 18 pt : « Le même personnage, partout ».
- Option : une 2e zone grisée, en arrière-plan décalé, « ZONE D'ESSAI », pour faire comprendre l'étanchéité sans un mot de plus.
- Animation (seulement si l'officier le souhaite) : apparition en 3 temps (cadre, apps, fil de l'avatar), fondu 200 ms. Une animation doit **expliquer**, pas décorer (règle 14).

**S2 — Frise chronologique** (diapo 3)
- Un **axe horizontal** d'avril à octobre, **mois proportionnels** (graduations mono 18 pt).
- 5 jalons ronds (ORION 26, AURIGE 2BB, MINOTAURE 26, Fusion + serveur, DELATTRE 26) ; **DELATTRE plein**, les autres évidés.
- Au-dessus de chaque jalon : le nom (mono 20 pt). En dessous : **« manque → outil » en 6 à 8 mots** (24 pt).
- **L'axe change d'aspect** à la fusion : **pointillé** d'avril à juillet (« fichiers HTML par mail »), **trait plein** d'août à octobre (« plateforme serveur unique »). La rupture se voit sans légende de couleur.

**S3 — « Le programme fait la psychologie, l'IA fait l'expression »** (diapo 8)
- Un **sandwich** de gauche à droite : `Publication du fil` → **[IA · lire]** → **[PROGRAMME]** → **[IA · formuler]** → `Message publié`.
- Le bloc PROGRAMME est **deux fois plus grand** et **plein graphite** (emphase par inversion) : 5 mots empilés, humeur · mémoire · relations · opinions · bascules.
- Les deux blocs IA sont **en trait seul**, plus petits : visuellement, l'IA est à l'entrée et à la sortie, elle ne décide pas.
- Juste avant `Message publié`, une **barrière** (trait épais vertical) « Garde-fous : relecture, interdits, plafonds » et, au-dessus de tout le schéma, un interrupteur `power` « L'animation peut geler, imposer, arrêter ».

**S4 — Courbe d'opinion** (diapo 9)
- Axe vertical **−100 à +100**, zéro marqué, **pôles écrits** (« rejette » en bas, « soutient » en haut) ; axe horizontal = jours ou heures de jeu.
- **Une seule courbe en emphase** (graphite 4 pt) : l'effet des joueurs ; les autres sources (animation, avatars IA, faits) en gris, tirets ou pointillés, **étiquetées directement en bout de courbe** (pas de légende séparée). Reprend la grammaire de l'avis n°103 (Reporting), inversée pour le fond clair.
- 2 ou 3 annotations au plus (« publication des joueurs », « démenti »).
- ⚠ **Données** : soit un **export réel** du Reporting de DELATTRE 26 (anonymisé, §14 du dossier), soit une courbe **explicitement marquée « illustration »**. Je n'invente pas de données présentées comme réelles. *(Question à l'utilisateur.)*

### 3.8 Accessibilité et règles de fabrication

1. Tout texte à lire : **≥ 7:1** (marge pour la projection) ; pied de page ≥ 4,5:1 ; traits porteurs de sens ≥ 3:1 (1.4.11).
2. **Jamais la couleur seule** : avant/après par la position et le mot, états par symbole + mot, courbes par le trait et l'étiquette (1.4.1).
3. Corps ≥ 20 pt, légendes ≥ 18 pt ; **test du fond de salle** : afficher la diapo à 25 % sur un écran d'ordinateur vu à 1 m simule grossièrement une lecture à 8-10 m.
4. Une idée par diapo, **titre = conclusion**, 40 mots maximum, le reste dans les **notes de l'orateur** (l'officier n'a pas à lire l'écran).
5. Texte alternatif sur chaque schéma et capture, ordre de lecture vérifié (le PDF circulera après la séance).
6. Insécables et pas de tiret cadratin (§3.3).
7. Captures d'écran : **données fictives uniquement**, aucune adresse, aucun nom de machine (dossier §14).

---

## 4. Plan de refonte (11 diapositives)

| # | Fond | **Titre-message** (proposition) | Visuel principal | Ce qu'on retire / déplace |
|---|---|---|---|---|
| 1 | Sombre | **PLÉIADE** · « L'espace informationnel d'entraînement du CECPC » | Logo constellation craie agrandi (~120 pt), titre 72 pt, une ligne « D'ORION 26 à DELATTRE 26 » en mono 20 pt | « six mois d'avancées techniques » ; tiret cadratin → « Exercice · non classifié. Pays, personnages, médias et villes : fictifs. » |
| 2 | Clair | « La lutte informationnelle se joue en ligne : PLÉIADE la reproduit en vase clos » | Bandeau de 3 icônes (réseau social, presse, messagerie) dans un périmètre fermé + 4 piliers en ligne : icône, **un mot** (Réalisme, Rapidité, Isolation, Reproductibilité), **6 mots** de preuve chacun | Les 4 cartes et le chapô de 2 lignes (→ notes) |
| 3 | Clair | « Six mois, quatre exercices : chaque manque a produit un outil » | **S2 frise** | Étiquettes CONSTAT / RÉPONSE ×5 ; phrases complètes (→ notes) |
| 4 | Clair | « D'un ZIP envoyé par mail à une plateforme unique, mise à jour en direct » | Avant / après en 2 colonnes, 5 lignes (Déploiement, Identité, Population, Injects, Mesure) avec icône, **≤ 6 mots par case**, colonne « Avec PLÉIADE » en bloc graphite inversé | Le vert ; l'en-tête marine/or ; les phrases longues |
| 5 | Clair | « Une zone par exercice : les applications à la carte, une seule identité partout » | **S1 schéma zone** | Les 3 colonnes colorées ; « SaaS modulaire » et « Digital workspace » passent en **légendes du schéma** (sur le cadre et sur la porte d'entrée), pas en paragraphe |
| 6 | Clair | « Du plan JEMM à l'écran des joueurs, sans ressaisie » | Flux horizontal de 6 étapes : **icône + nom de l'app + 3 à 5 mots**, reliées par des flèches ; sous le flux, la barre EHO qui court sous toutes les étapes | Les 6 couleurs de numéros ; les cartes ; le paragraphe sous les cartes (devenu la barre) |
| 7 | **Sombre** (bascule) | « Nouveauté DELATTRE 26 : un espace qui réagit » | **« 105 »** en chiffre clé craie 120 pt, « avatars animés par IA, citoyens de l'Arnland » ; une **barre empilée** 15 / 70 / 15 % étiquetée en clair (pro-Mercure · neutres · pro-Arnland), en niveaux de craie et motifs, pas en couleurs de camp | Les deux cartes de texte (→ diapo 8) ; l'empattement et l'or |
| 8 | Clair | « Le programme tient la psychologie ; l'IA ne fait que lire et formuler » | **S3 sandwich** + barrière des garde-fous | Les listes à puces ; le bandeau « Garde-fous » en texte ; « 36 nuances » passe en mention ◌ En essai sous le schéma |
| 9 | Clair | « Pour la première fois, on voit l'effet d'une action de joueur sur l'opinion » | **S4 courbe d'opinion** (pleine largeur) ; à droite, 3 questions auxquelles répond le Reporting (≤ 6 mots chacune) | **Les encarts « > 1 000 » et « ≈ 37 % »** (dossier §6.5 : à ne pas présenter comme preuves) ; la citation à empattements ; le titre rouge. S'ils sont gardés pour illustrer la **boucle d'amélioration** (relevé, diagnostic, correction en quelques heures), le faire dans les notes de l'orateur ou en une ligne, jamais en chiffre héros |
| 10 | Clair | « Fermé, local, réparti : rien ne sort de la salle » | Schéma : périmètre VPN (cadre), serveur CECPC au centre, 2 nœuds de calcul (PC, Mac) reliés, flèche de reprise automatique ; 4 légendes de 4 à 6 mots ; mention « Doctrine : 11 guides de l'ANSSI » | Les 4 cartes de 35 mots ; « libre de droits » (à corriger, cf. analyse des chiffres) ; aucun détail réseau (dossier §14) |
| 11 | Sombre | « PLÉIADE permet d'entraîner, mesurer et réutiliser : [la décision attendue] » | 5 verbes en colonne (24 pt, verbe en 700) à gauche ; à droite une **mini-feuille de route** sur un axe : ◌ En essai → ○ À l'étude → Ensuite ; en bas, **la demande aux décideurs** en bloc craie | Les paragraphes de l'encart ; le vide du bas |
| *(annexe)* | Clair | « Chiffres clés au 13 octobre 2026 » | 6 chiffres en grille 3 × 2 (chiffre 60 pt + libellé 18 pt), seulement ceux validés par l'analyse des chiffres | Facultative, à montrer seulement sur question |

**Titres-messages** : ce sont des propositions de forme ; la formulation finale revient à l'utilisateur et à l'officier.

---

## 5. Questions ouvertes (à l'utilisateur)

1. **Piste A (charte PLÉIADE) ou piste B (habillage actuel corrigé) ?** Réponse attendue : « A » ou « B ».
2. **Que demande-t-on aux décideurs** en diapo 11 (moyens, généralisation aux écoles et régiments, poursuite de l'essai IA…) ? Je ne l'invente pas.
3. **Courbe d'opinion** : export réel anonymisé du Reporting, ou courbe marquée « illustration » ?
4. **Captures d'écran** : en veut-on une (réseau social façon X, données fictives) ? Elle remplacerait avantageusement le bandeau d'icônes de la diapo 2.
5. **Outil de fabrication** : le deck est-il produit en PowerPoint (incorporation des polices à prévoir) ou en HTML/PDF ? Quel poste projettera ?
