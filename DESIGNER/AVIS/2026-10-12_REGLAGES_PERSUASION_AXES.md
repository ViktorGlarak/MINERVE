# Avis DESIGNER n°102 — 2026-10-12 — app-ia, Réglages : coefficient de persuasion et éditeur des axes d'opinion

> Écran lu : `C:\CECPC\pleiade\app-ia\src\components\ReglagesMoteur.tsx` (Réglages du Moteur IA) et `src\app\api\bff\reglages\route.ts`. Vu aussi : `src\moteur\esprit.mjs` (où les axes sont définis et cités). Aucun code modifié.
> Demande de l'utilisateur : (1) un coefficient « persuasion » qui fonctionne comme le coefficient de crise ; (2) pouvoir ajouter, modifier et retirer les **axes d'opinion**, figés aujourd'hui (FORCE, Mercure, institutions, N.O.M).
> Suite de l'avis n°98 (`AVIS\2026-10-11_APP_IA\`), dont les recommandations restent valables. Les bornes et paliers de la persuasion relèvent du **PSYCHOLOGUE** : les valeurs ci-dessous servent d'exemple.
> Ce sont des **propositions** : le besoin de l'utilisateur et les choix de PLEIADE priment.

---

## Constat sur l'écran actuel

- Six panneaux empilés, dans un ordre qui ne suit pas l'usage : la **crise** (geste de conduite) est en tête, la **qualité** (réglage technique à l'essai) vient ensuite, et les **campagnes** (geste d'animation) sont plus bas.
- Les campagnes se saisissent en **JSON brut**. Pour un animateur militaire, c'est la principale source d'erreurs : accolades, guillemets, axe mal orthographié (« Force » au lieu de « FORCE »). Le serveur refuse avec « axe inconnu : Force », mais l'écran ne dit pas où corriger.
- La liste des axes vit à **deux endroits** dans le code : `AXES` dans la route (4 clés) et `AXES` dans `esprit.mjs` (clé → libellé donné au modèle). On les rend modifiables : il faut **une seule source**, en base, relue par les deux. C'est une remontée PLEIADE (R-API-1).
- Quatre confirmations passent par `window.confirm`. Ce n'est pas une faute grave, mais leur texte n'est pas mis en forme, le focus par défaut n'est pas maîtrisé, et elles ne suivent pas la règle « fermeture au clic extérieur et par Échap ». Pour les nouveaux gestes, utiliser la fenêtre de confirmation de la famille (avis n°98).

---

## R1. Disposition : trois groupes dans l'ordre de l'usage (gain fort, effort faible)

On regroupe sous des intertitres h2 sobres (`text-[13px] uppercase tracking-wide text-ink-muted`), sans nouveaux onglets. L'écran reste lisible d'un trait, et un animateur trouve d'abord ce qu'il touche pendant l'exercice.

```
Réglages                                   Effet au début du prochain cycle · Chaque modification est journalisée
[message d'état role=status]

── CONDUITE DE L'EXERCICE ───────────────────────────────────────────────
 ┌ Coefficient de crise ────────────┐ ┌ Coefficient de persuasion ───────┐
 │ (inchangé, avis n°98)            │ │ (R2)                             │
 └──────────────────────────────────┘ └──────────────────────────────────┘
 ┌ Campagnes de mots-dièse (R4) ────────────────────────────────────────┐
 └──────────────────────────────────────────────────────────────────────┘

── PRÉPARATION DE L'EXERCICE ────────────────────────────────────────────
 ┌ Axes d'opinion (R3) ─────────────────────────────────────────────────┐
 ┌ Contexte de l'exercice (inchangé) ───────────────────────────────────┐

── MOTEUR ET DONNÉES ────────────────────────────────────────────────────
 ┌ Qualité des messages (essai) ┐  ┌ Journal et archives ┐
 ┌ Historique des réglages (R6) ────────────────────────────────────────┐
```

- **Crise et persuasion côte à côte** au-dessus de 1100 px, empilées en dessous. Ce sont deux « boutons de volume » de même nature : la même forme les fait lire comme une paire (proximité et similarité, Laws of UX, REF-06).
- **Axes avant contexte** : on définit les axes une fois, à la préparation. Ils sont rarement modifiés en cours d'exercice, donc on ne les met pas en tête. Mais les campagnes en dépendent : le panneau Campagnes porte un lien « Gérer les axes ↓ ».
- Un seul « Enregistrer » principal par panneau (règle 37, avis n°98).

---

## R2. Coefficient de persuasion : le jumeau du coefficient de crise (gain fort, effort faible)

**Même composant que la crise**, pour qu'un geste appris serve deux fois. On factorise un composant `CoefficientEffet` (titre, curseur, champ numérique, repères, encadré « Concrètement », bouton, ligne « Actuel »).

```
┌ Coefficient de persuasion ─────────────────────────────────────────────┐
│ À quel point les campagnes des joueurs font changer d'avis la population│
│                                                                        │
│ 0,5 ├────────────●──────────────────────────────┤ 3,0     [ 1,0 ]       │
│     difficile   normale    facile      très facile                     │
│     (0,5)       (1,0)      (1,5)       (2,0)    maximum (3,0)          │
│                                                                        │
│ ┌ Concrètement, à 1,0 : comportement de référence ────────────────────┐ │
│ │ Un avatar ouvert, exposé à une campagne crédible, bouge d'environ   │ │
│ │ 8 points par lecture. Un avatar bien ancré bouge peu.               │ │
│ │ Bascule d'un camp à l'autre : rare, en général après plusieurs jours│ │
│ └─────────────────────────────────────────────────────────────────────┘ │
│ Non enregistré : 1,0 → 2,0                         [ Enregistrer ]      │
│ Actuel : 1,0 · par cdt.martin le 12/10 à 09:14                         │
└────────────────────────────────────────────────────────────────────────┘
```

- **Titre** : « Coefficient de persuasion ». **Sous-titre en une phrase qui dit l'effet** : « À quel point les campagnes des joueurs font changer d'avis la population ». On évite « crédulité » ou « suggestibilité », qui jugent la population.
- **Curseur + champ numérique liés** (pas de 0,1). Le curseur seul est imprécis, et la saisie au clavier doit rester possible (WCAG 2.5.7, mouvements de glissement).
- **Repères cliquables sous le curseur** (comme les 5 repères de la crise dans l'avis n°98), avec un mot par palier. À faire fixer par le PSYCHOLOGUE, par exemple :
  - 0,5 **difficile à convaincre** · 1,0 **normale** · 1,5 **facile** · 2,0 **très facile** · 3,0 **maximum (démonstration)**.
- **Encadré « Concrètement, à x »** qui change avec la valeur. C'est la doctrine de l'avis n°98 : *un réglage s'exprime dans son effet*. Trois lignes au plus, dans les mots de l'animation : de combien bouge un avatar ouvert, ce que devient un avatar ancré, à quel rythme se fait une bascule. Les chiffres viennent des formules du moteur (`s·8·k·c·(1−ancrage)` aujourd'hui × coefficient) et non d'un texte figé. Une **remontée PLEIADE** suit (R-API-2) : la route GET renvoie ces exemples calculés, pour que l'écran ne recopie pas une formule.
- Le mot « bascule » apparaît dans l'encadré, puisque c'est l'effet que l'animateur surveille.
- **Confirmation au-delà d'un seuil** : oui, avec la même règle que pour la crise, mais dans les deux sens, car les deux extrêmes faussent l'exercice.
  - **Au-dessus de 2,0** : *« Persuasion 2,5 : une campagne peut faire basculer un avatar ouvert en quelques heures. Les résultats de l'exercice ne refléteront plus une population réaliste. »* Boutons **[Annuler]** (focus) et **[Appliquer 2,5]**.
  - **En dessous de 0,7** : *« Persuasion 0,5 : les campagnes des joueurs n'auront presque aucun effet visible. Les joueurs risquent de conclure que leurs actions ne servent à rien. »* Mêmes boutons.
  - Le focus va sur **Annuler**, car ces valeurs changent ce que les joueurs constatent (avis n°98, confirmation asymétrique).
- **Effet au prochain cycle** : la ligne « Pris en compte au prochain cycle (vers 17:48) » s'affiche après l'enregistrement, comme pour la crise.
- **Dire aussi ce que la persuasion ne change pas** (une ligne discrète) : *« Ne change ni le nombre de messages (voir Crise), ni les positions déjà acquises : seulement la vitesse à laquelle elles bougent désormais. »* L'animateur ne confond pas les deux coefficients, et ne croit pas que baisser la valeur ramène les avatars en arrière.
- **Accessibilité** : `aria-valuetext` sur le curseur, de la forme « 1,5, facile » (et non « 1.5 »). Le mot de palier est écrit, jamais la couleur seule. Les valeurs sont affichées avec la virgule française partout, y compris dans la confirmation (l'écran actuel écrit `crise.toFixed(1)`, donc « 2.5 » : à corriger au passage).

---

## R3. Éditeur des axes : une liste de cartes, une fenêtre d'édition, l'archivage au lieu de la suppression (gain fort, effort moyen)

### 3.1 Liste

Un axe a cinq champs, dont deux longs (description, règle de départ). Ils ne tiennent pas dans un tableau éditable en ligne, et un tableau éditable invite à modifier par mégarde. On choisit donc une **liste de cartes compactes en lecture**, et l'édition dans une **fenêtre**.

```
┌ Axes d'opinion ──────────────────────────────────────── [ + Nouvel axe ] ┐
│ Chaque avatar a une position sur chaque axe, de −100 (contre) à +100     │
│ (pour). Les campagnes poussent sur ces axes.                             │
│                                                                          │
│ ┌──────────────────────────────────────────────────────────────────────┐ │
│ │ La FORCE                                          clé : FORCE        │ │
│ │ contre : « hostile à la FORCE » ◄──────┼──────► pour : « soutient… » │ │
│ │ Position moyenne : +18 · 105 avatars · 3 campagnes  [Modifier] [⋯]  │ │
│ └──────────────────────────────────────────────────────────────────────┘ │
│ ┌──────────────────────────────────────────────────────────────────────┐ │
│ │ Le N.O.M                                          clé : N.O.M        │ │
│ │ …                                                                    │ │
│ └──────────────────────────────────────────────────────────────────────┘ │
│ ▸ Axes archivés (1)                                                      │
└──────────────────────────────────────────────────────────────────────────┘
```

- **Chaque carte** : le **libellé** en titre, la **clé** à droite en `font-mono text-ink-muted` (l'animateur n'a pas à la retenir), les **deux pôles** de part et d'autre d'un trait gradué, et une ligne de **conséquences** : position moyenne, nombre d'avatars, nombre de campagnes qui l'utilisent. Cette ligne sert à décider avant de toucher (R3.4).
- La **position moyenne** se lit sur le trait gradué par un repère, doublé par le nombre signé (« +18 »). C'est un aperçu utile, mais il n'est pas indispensable au premier lot.
- **Actions** : « Modifier » en bouton secondaire. Le menu « ⋯ » contient « Archiver » (et « Restaurer » pour un axe archivé). Un menu bouton suit l'APG Menu Button (REF-19) : flèches, Échap, focus rendu au bouton.
- **Axes archivés** : un `<details>` replié en bas de la liste, avec le nombre dans le titre.
- **État vide** (aucun axe, cas d'une zone neuve) : *« Aucun axe d'opinion. Les avatars n'auront pas de position politique, et les campagnes n'auront pas d'effet. Commencez par « + Nouvel axe », ou reprenez les 4 axes de référence (FORCE, Mercure, institutions, N.O.M). »* Le bouton **« Reprendre les axes de référence »** est utile pour une nouvelle zone.

### 3.2 Fenêtre « Nouvel axe » / « Modifier l'axe »

```
┌ Nouvel axe d'opinion ────────────────────────────────────────── ✕ ┐
│ Libellé *                                                          │
│ [ La coalition Bothnia                                     ]       │
│ Ce que voient les animateurs dans les écrans.                     │
│                                                                    │
│ Clé technique *                                                    │
│ [ bothnia                ]  proposée d'après le libellé            │
│ Lettres, chiffres, point, tiret. Ne change plus une fois créée.   │
│                                                                    │
│ Ce que le modèle doit comprendre *                    142 / 300    │
│ [ la coalition menée par Bothnia (gouvernement, armée,     ]       │
│ [ alliés SCO/SSTO)                                         ]       │
│ Écrit tel quel dans les instructions des avatars. Faits de la      │
│ fiction seulement, sans consigne de camp.                          │
│                                                                    │
│ Pôle « contre » *            Pôle « pour » *                       │
│ [ hostile à Bothnia    ]     [ favorable à Bothnia     ]           │
│                                                                    │
│ Position de départ des avatars                                     │
│ (●) Neutre pour tous (0)                                           │
│ ( ) Selon le camp eho                                              │
│      🔴 rouge  [ +40 ]   🔵 bleu  [ −40 ]   ⚪ neutre  [ 0 ]        │
│ ( ) Copier un axe existant  [ Mercure ▾ ]  × [ 1 ] (ou × −1)       │
│ Aperçu : 34 avatars à +40 · 41 à −40 · 30 à 0                      │
│                                                                    │
│                               [ Annuler ]  [ Créer l'axe ]         │
└────────────────────────────────────────────────────────────────────┘
```

- **Fenêtre modale**, conforme à l'APG Dialog (REF-19) : focus sur le premier champ, focus piégé, Échap et clic sur le fond la ferment, et le focus revient au bouton qui l'a ouverte. **Exception à la fermeture au clic extérieur** : si un champ a été modifié, le clic extérieur ou Échap demande *« Abandonner les modifications de cet axe ? [Continuer la saisie] [Abandonner] »*. Cela évite de perdre une description de 300 caractères sur un clic de travers. Une fenêtre non modifiée se ferme sans rien demander.
- **Clé technique proposée automatiquement** d'après le libellé (minuscules, sans accent), modifiable à la création seulement, puis **figée** (affichée en lecture avec un cadenas). La clé est ce qui relie les fiches, les campagnes, le journal et les exports. La changer casserait tous ces liens, donc on ne propose pas ce geste (Tesler : la complexité reste dans le système, REF-06). Refus si la clé existe déjà, archivés compris : *« La clé « force » est déjà prise par l'axe « La FORCE ». Choisissez-en une autre. »*
- **Description donnée au modèle** : bornée (300 caractères proposés, à valider par CYBERSECU), avec compteur et consigne d'écriture sous le champ. C'est du texte injecté dans les invites, comme le contexte (remontée CYBERSECU de l'avis n°98).
- **Pôles** : deux champs courts côte à côte (empilés sous 640 px). Ils servent aux écrans (barres divergentes, export des opinions) et sans doute au modèle.
- **Position de départ** : trois choix exclusifs en boutons radio, le plus simple d'abord. Le choix « selon le camp eho » affiche les trois camps avec **émoji + mot**, conformément au registre des camps (MASTAURIGE / vault), jamais la couleur seule. La ligne **« Aperçu »** compte les avatars concernés : l'animateur voit l'effet avant de créer (Nielsen 1, REF-14). Les valeurs sont bornées à −100…+100 avec un message GOV.UK : *« Position de départ : un nombre de −100 à +100. »*
- **La règle « selon le camp » ou « copier un axe » est un choix à faire valider par le PSYCHOLOGUE** (ancrage, dispersion autour de la valeur, part d'avatars sans avis). L'écran ne doit proposer que ce que le moteur sait faire. Si le PSYCHOLOGUE veut une dispersion, on ajoute une seule ligne « Dispersion : faible · moyenne · forte » et rien de plus.
- **Modifier un axe existant** : même fenêtre, sans la position de départ, qui est déjà appliquée. Une note la remplace : *« Les positions des avatars ne sont pas modifiées. »* Si l'on change le **libellé** ou la **description**, un encadré l'annonce avant d'enregistrer : *« Le modèle lira la nouvelle description dès le prochain cycle. Les 105 positions actuelles sont conservées. »*
- **Validation** : erreurs affichées à la GOV.UK (REF-10), avec un résumé en tête de fenêtre qui reçoit le focus et un message sous chaque champ, qui dit comment corriger.

### 3.3 Archiver plutôt que supprimer

- **Pas de suppression définitive** dans l'écran. Un axe porte des positions, un historique et des lignes du journal et des exports : on l'**archive**. Un axe archivé n'est plus donné au modèle, plus proposé dans les campagnes, et les positions sont **gelées et conservées**. **Restaurer** le remet en service avec ses positions.
- La suppression définitive, si elle est utile, rejoint « Supprimer les archives (fin d'exercice) », qui est déjà le geste de fin d'exercice.

### 3.4 Conséquences visibles avant d'archiver

```
┌ Archiver l'axe « Le N.O.M » ? ───────────────────────────── ✕ ┐
│ À partir du prochain cycle :                                   │
│  • les avatars ne liront plus cet axe dans leurs instructions ;│
│  • 2 campagnes perdent leur effet sur cet axe :                │
│      #paixmaintenant (contre · 0,3)  #nomdehors (contre · 1,0) │
│    #nomdehors n'a pas d'autre axe : elle n'aura plus d'effet.  │
│  • les 105 positions sont conservées et gelées.                │
│ Vous pourrez restaurer l'axe plus tard.                        │
│                                  [ Annuler ]  [ Archiver ]     │
└────────────────────────────────────────────────────────────────┘
```

- **Fenêtre de confirmation qui liste les conséquences concrètes**, avec les noms des campagnes touchées, et signale celles qui n'auront **plus aucun effet**. Le focus va sur **Annuler** : ce geste change ce que font les avatars devant les joueurs.
- Le bouton dit le geste (« Archiver »), jamais « OK » ou « Oui ».
- **Avertissement pour les axes cités dans le code du moteur** : aujourd'hui, `esprit.mjs` contient des comportements propres au N.O.M (« message N.O.M », « N.O.M ou militant adverse ») et une règle par défaut sur FORCE et Mercure (un mot-dièse non déclaré n'est rattaché qu'à ces deux axes). Archiver l'un de ces axes ne désactive pas ces comportements. Deux solutions, à trancher par PLEIADE (R-API-3) : soit ces axes sont marqués **« axe de référence »** et ne s'archivent pas (le menu affiche « Archiver » grisé avec la raison : *« Utilisé par le moteur : ne peut pas être archivé »*), soit le moteur ne doit plus rien coder en dur. Dans les deux cas, **l'écran ne doit pas laisser croire qu'un geste a un effet qu'il n'a pas.**
- **Pendant un exercice en cours** (moteur actif) : créer, archiver ou modifier un axe reste permis, mais la fenêtre ajoute une ligne : *« Le moteur tourne : l'effet sera visible devant les joueurs dès le prochain cycle (vers 17:48). »*

---

## R4. Campagnes : remplacer le JSON par un petit éditeur lié aux axes (gain fort, effort moyen)

Oui, c'est le bon moment : les axes deviennent variables, et un JSON qui cite des clés que l'animateur ne voit pas devient encore plus fragile. On reprend le tableau proposé dans l'avis n°98.

```
┌ Campagnes de mots-dièse ───────────────── Gérer les axes ↓  [ + Nouvelle campagne ] ┐
│ Ce qu'une campagne fait aux avatars qui la lisent et la reprennent.                │
│                                                                                    │
│ Mot-dièse         Effet par axe                                  Modifiée     │    │
│ #paixmaintenant   La FORCE      contre ███▌│        1,0          cdt.martin   ✎ ✕ │
│                   institutions  contre    ▌│        0,3          12/10 09:14      │
│ #nomdehors        Le N.O.M      contre ███▌│        1,0          …            ✎ ✕ │
│ ⚠ #vieilletag     Le N.O.M (axe archivé : sans effet)                         ✎ ✕ │
└────────────────────────────────────────────────────────────────────────────────────┘
```

- **Tableau en lecture** : un mot-dièse par ligne, et sous lui **seulement les axes sur lesquels il pousse** (pas de ligne « sans effet » pour chaque axe, qui encombrerait dès 6 axes). Barre divergente autour d'un zéro central, **doublée par le mot et la valeur** (« contre · 1,0 »).
- **Fenêtre « Nouvelle campagne » / « Modifier »** : un champ mot-dièse (le « # » est affiché devant le champ et retiré s'il est tapé), puis **une ligne par axe actif**, avec le libellé de l'axe, un curseur de −1 à +1 (pas de 0,1), un champ numérique, et les **pôles de l'axe** aux deux extrémités (« hostile à la FORCE » … « soutient la FORCE ») plutôt que « −1 » et « +1 ». Le zéro, valeur par défaut, est marqué « sans effet ».
  - Au-delà de 8 axes, les lignes à zéro sont repliées sous « Ajouter un effet sur un autre axe ▾ ».
  - **Phrase de résumé** sous les curseurs, mise à jour en direct : *« Ceux qui lisent #paixmaintenant s'éloignent de la FORCE (fort) et un peu des institutions. »* C'est ce que l'animateur veut vérifier.
  - Refus si tous les axes sont à zéro : *« Cette campagne n'a aucun effet. Donnez un sens sur au moins un axe, ou annulez. »*
  - Doublon : *« #paixmaintenant existe déjà. Modifiez-la depuis le tableau. »*
- **Suppression d'une campagne (✕)** : confirmation simple, focus sur Annuler (*« Supprimer #paixmaintenant ? Les avatars ne seront plus poussés par ce mot-dièse à partir du prochain cycle. »*).
- **Campagne qui ne pousse plus que sur des axes archivés** : la ligne reste, marquée ⚠ avec le mot « sans effet » et l'explication.
- **Rappel de la règle par défaut** (« un mot-dièse absent d'ici n'est rattaché qu'aux axes FORCE et Mercure ») : à reformuler en tête de panneau dans les mots de l'animation, et à revoir si ces axes deviennent archivables (R-API-3).
- **Garder le JSON pour les experts ?** Oui, mais caché : un `<details>` « Saisie avancée (JSON) » en bas du panneau, avec erreur à la ligne près. Il reste utile pour coller d'un coup 20 campagnes préparées hors ligne. Il ne doit pas être la voie normale.
- **Limite de 30 campagnes** (déjà dans la route) : l'afficher (« 12 / 30 ») et désactiver « + Nouvelle campagne » à 30, avec la raison écrite.

---

## R5. États, erreurs et messages (gain moyen, effort faible)

- **Message d'état** : aujourd'hui une seule ligne en tête de page, souvent hors de vue quand on enregistre en bas. On l'affiche **dans le panneau concerné**, sous son bouton (`role="status"`), et on garde l'en-tête pour les erreurs de chargement.
- **Refus du serveur** : écrire le message du serveur en clair, mais dans les mots de l'écran. « axe inconnu : Force » devient *« La campagne #x cite un axe qui n'existe pas (« Force »). »* La route doit renvoyer un champ `champ` en plus de `error` pour placer le message au bon endroit (R-API-4).
- **Chargement** : remplacer « Chargement… » par la structure grisée des panneaux, pour éviter le saut de mise en page.
- **Échec du chargement** (moteur ou base injoignable) : *« Les réglages n'ont pas pu être lus. Rien n'a été modifié. [Réessayer] »*. Ne jamais afficher des valeurs par défaut comme si elles étaient les valeurs actuelles (doctrine de l'avis n°98 : un état s'affiche relu).
- **Modification concurrente** (deux animateurs sur l'écran) : à l'enregistrement, si la valeur a changé depuis la lecture (précondition, comme pour l'interrupteur de l'avis n°98), *« cdt.durand a changé ce réglage à 09:20 (1,0 → 1,5). Votre valeur n'a pas été enregistrée. [Voir la valeur actuelle] »*. Indispensable pour les axes et les campagnes, qui s'écrivent d'un bloc (R-API-5).

---

## R6. Historique des réglages : lisible sans JSON (gain moyen, effort faible)

- Aujourd'hui, une ligne affiche le JSON brut tronqué à 160 caractères. Pour les axes et les campagnes, ce sera illisible.
- On écrit **une phrase par changement**, à partir d'un type et d'un avant → après fournis par la route :
  - `12/10 09:14 · cdt.martin · Persuasion 1,0 → 1,5 (facile)`
  - `12/10 09:20 · cdt.martin · Axe créé : « La coalition Bothnia » (départ selon le camp : 🔴 +40 · 🔵 −40 · ⚪ 0)`
  - `12/10 09:31 · cdt.durand · Axe archivé : « Le N.O.M » (2 campagnes touchées)`
  - `12/10 09:40 · cdt.durand · Campagne #paixmaintenant : La FORCE contre 1,0 → contre 0,6`
- Un filtre par type (Crise · Persuasion · Axes · Campagnes · Contexte · Qualité) en `pl-seg`, utile quand l'historique s'allonge.
- L'auteur est celui de la **session** (déjà le cas avec `g.op.name`, à garder).

---

## R7. Accessibilité, en bref

- Chaque curseur a un champ numérique lié, un `aria-valuetext` en français (« contre, 0,6 ») et des pas au clavier (flèches 0,1 ; Page haut/bas 0,5).
- Fenêtres : APG Dialog (titre relié par `aria-labelledby`, focus initial, focus piégé, Échap, retour du focus). Fermeture au clic extérieur et par Échap, sauf saisie en cours (R3.2), qui demande confirmation.
- Menu « ⋯ » : APG Menu Button, avec un nom accessible qui contient l'axe (« Actions pour l'axe La FORCE »).
- Camps et sens : émoji ou forme **et** mot, jamais la couleur seule (REF-07).
- Cibles de 24 × 24 px au moins (WCAG 2.5.8), 44 px si l'écran doit servir sur tablette.
- Les messages d'enregistrement et d'erreur sont annoncés (`role="status"` ou `role="alert"`).

---

## Remontées PLEIADE, PSYCHOLOGUE et CYBERSECU

- **R-API-1 (PLEIADE)** : une **seule liste d'axes**, en base (clé, libellé, description, pôle contre, pôle pour, ordre, statut actif/archivé, règle de départ), relue par la route **et** par `esprit.mjs`. Aujourd'hui il y en a deux copies.
- **R-API-2 (PLEIADE)** : la route GET renvoie, pour la persuasion, les **exemples d'effet calculés** (déplacement typique d'un avatar ouvert ou ancré, rythme de bascule) pour la valeur actuelle et pour chaque palier, afin que l'écran n'ait pas à recopier une formule.
- **R-API-3 (PLEIADE)** : décider du sort des axes **cités en dur** dans le moteur (N.O.M, et FORCE/Mercure dans la règle par défaut) : axes de référence non archivables, ou moteur sans axe en dur.
- **R-API-4 (PLEIADE)** : erreurs de validation avec `{ error, champ }` pour les placer sous le bon champ.
- **R-API-5 (PLEIADE / CYBERSECU)** : précondition à l'écriture (valeur attendue ou version), refus 409 si elle a changé.
- **PSYCHOLOGUE** : bornes, paliers et mots de la persuasion ; règle de position de départ d'un nouvel axe (par camp, copie d'un axe, dispersion, ancrage) ; effet de l'archivage sur les positions (gel proposé ici).
- **CYBERSECU** : la description d'axe et les pôles sont du **texte injecté dans les invites**. Il faut les borner (300 et 60 caractères proposés), réserver l'écriture au rôle Administration côté serveur (déjà le cas avec `requireAdmin`) et tracer l'auteur réel. Le nombre d'axes doit aussi être borné (12 proposés), pour la taille de l'invite comme pour la lisibilité de l'écran.

---

## Points à trancher par l'utilisateur

1. **Archivage seul**, sans suppression définitive dans l'écran (proposé), ou suppression possible d'un axe jamais utilisé ?
2. Les **axes de référence** (FORCE, Mercure, institutions, N.O.M) sont-ils archivables ? Cela dépend de R-API-3.
3. **Seuils de confirmation** de la persuasion : au-dessus de 2,0 et en dessous de 0,7 (proposé), ou dans un seul sens ?
4. **JSON des campagnes** : gardé en « saisie avancée » repliée (proposé), ou retiré ?
5. **Nombre maximal d'axes** : 12 proposé.

Mise en œuvre : PLEIADE, en local d'abord (règle « tester en local avant de pousser »), après l'avis du PSYCHOLOGUE sur les bornes et la règle de départ.
