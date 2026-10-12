# Avis DESIGNER n°103 — 2026-10-12 — app-cockpit, Reporting : l'opinion des avatars IA et l'effet des joueurs

> Écran lu : `C:\CECPC\pleiade\app-cockpit\src\components\ReportingView.tsx`, `ReportingHashtag.tsx` et `GrapheTemps.tsx`. Aucun code modifié.
> Demande de l'utilisateur : dans le Reporting (réservé à l'animation, rôle « analyste »), un graphique de **l'état d'influence des avatars IA par rapport à ce que font les joueurs**. Données relevées **chaque heure** par le moteur IA (105 avatars, axes FORCE, Mercure, institutions, N.O.M, au plus 8 axes, positions de −100 « rejette totalement » à +100 « soutient »).
> Suite des avis n°75 (`GrapheTemps` : des lignes, jamais d'aires empilées ; la valeur au survol), n°96 (panneau « Par hashtag » ; une part se donne avec son effectif) et n°102 (axes éditables : libellé, clé figée, **pôles nommés**).
> Ce sont des **propositions** : le besoin de l'utilisateur et les choix de PLEIADE priment. Les définitions du doute, de la bascule et de l'attribution relèvent du **PSYCHOLOGUE**.

---

## Constat

- Le Reporting compte aujourd'hui des **volumes** (contenus par heure, toujours ≥ 0). L'opinion est d'une autre nature : une **position signée** et des **déplacements** dans les deux sens. Il faut donc un **zéro visible** et un **sens lisible sans légende** (« vers soutient » en haut, « vers rejette » en bas).
- `GrapheTemps` suppose des valeurs positives à quatre endroits : le domaine part de 0 (`Math.max(0, …)`), les repères aussi, les points ne s'affichent que si `v > 0`, et l'axe dit « … par heure ». La légende affiche une **somme**, fausse pour une courbe cumulée ou une position. Voir R7.
- Le piège de vocabulaire : dans l'exercice, **« camp »** désigne le camp eho (🔴 / 🔵 / ⚪). Une bascule d'opinion sur un axe n'est pas un changement de camp eho. Écrire **« a basculé »** (passé de « pour » à « contre », ou l'inverse), jamais « a changé de camp ».

---

## R1. Un panneau, cinq blocs, dans l'ordre des questions de l'animateur

Un nouveau panneau **« Opinion de la population IA »**, placé **après « Par hashtag »** et avant « Publications par cellule ». Il suit la période, le mode En direct / Figée et le bouton Recalculer existants (prop `rafraichir`, comme `ReportingHashtag`).

| Ordre | Bloc | Question à laquelle il répond |
|---|---|---|
| 1 | **Vue d'ensemble des axes** (petits multiples, qui servent aussi de sélecteur) | Où en est l'opinion, sur chaque axe ? |
| 2 | **Qui fait bouger l'opinion** (axe choisi) ⭐ | Les joueurs pèsent-ils, et dans quel sens ? |
| 3 | **Position moyenne** (axe choisi) | Où en est la population par rapport à son départ ? |
| 4 | **Avatars ébranlés** (axe choisi) | Combien doutent, combien ont basculé ? |
| 5 | **Comptes qui ont le plus fait bouger**, puis **Avatars** (deux tableaux) | Qui, précisément ? |

Trois graphiques dans le temps pour l'axe choisi, pas plus. Les blocs 3 et 4 peuvent être repliés par défaut si l'écran paraît long : le bloc 2 est la réponse à la demande.

```
┌ OPINION DE LA POPULATION IA ─────────────────────── dernier relevé 14:00 · prochain vers 15:00 ┐
│ — 105 avatars animés par l'IA ; position de −100 (rejette) à +100 (soutient), relevée chaque heure │
│                                                                                                │
│ ┌ FORCE ───────────┐ ┌ Mercure ─────────┐ ┌ Institutions ────┐ ┌ N.O.M ───────────┐            │
│ │ +18  ▲ +6        │ │ −22  ▼ −9        │ │ +4   = 0         │ │ −41  ▼ −3        │            │
│ │ ‾‾‾‾‾‾‾‾‾‾‾╱‾‾‾‾ │ │ ────╲___________ │ │ ──────────────── │ │ ________________ │            │
│ │ ·············0·· │ │ ·············0·· │ │ ·············0·· │ │ ·············0·· │            │
│ │ dont joueurs +4  │ │ dont joueurs −7  │ │ dont joueurs 0   │ │ dont joueurs −1  │            │
│ └══════════════════┘ └──────────────────┘ └──────────────────┘ └──────────────────┘            │
│   (carte choisie : bordure épaisse craie + aria-checked)                                       │
│                                                                                                │
│ QUI FAIT BOUGER L'OPINION SUR « FORCE » — déplacement cumulé de la moyenne, en points          │
│  ▲ vers « soutient »                                                                           │
│ +6 ┤                                         ━━━━━━━━  Joueurs        +4,1                     │
│ +3 ┤                    ━━━━━━━━━━━━━━━━━━━━━          Animation      +1,6                     │
│  0 ┼━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  (zéro : trait plein, plus épais)         │
│ −3 ┤          - - - - - - - - - - - - - - - - - - - -  Avatars IA     −0,8                     │
│  ▼ vers « rejette »                                    Faits injectés +1,1                     │
│     08:00     10:00     12:00     14:00                                                        │
│     lun. 12/10                                                                                 │
└────────────────────────────────────────────────────────────────────────────────────────────────┘
```

## R2. Le choix de l'axe : les petits multiples SONT le sélecteur

- Une **carte par axe actif** (4 aujourd'hui, 8 au plus : 4 par ligne, 2 lignes), en `role="radiogroup"` ; chaque carte est un `role="radio"`. Cliquer une carte choisit l'axe des blocs 2 à 5. L'axe choisi est mémorisé par poste (`localStorage`, comme les hashtags).
- Contenu d'une carte, dans cet ordre : **libellé de l'axe** · **position moyenne actuelle**, signée (`+18`, `−22`, `0`, avec le vrai signe moins U+2212) · **variation sur la période** (`▲ +6`, `▼ −9`, `= 0` : flèche **et** signe, jamais la couleur seule) · **mini-courbe** de la position moyenne · **« dont joueurs +4 »** (la part des joueurs dans cette variation).
- Les mini-courbes ont **toutes le même domaine fixe −100..+100** et un zéro en pointillé : on compare les axes d'un coup d'œil, sans qu'un petit mouvement paraisse énorme. C'est un petit composant à part (`MiniCourbe`, SVG ~220×56, sans texte d'axe), pas `GrapheTemps`.
- Pourquoi pas une liste déroulante : elle cache les autres axes. Pourquoi pas 8 grands graphiques : l'écran devient illisible. Les petits multiples donnent la vue d'ensemble, le grand graphique donne le détail.

## R3. « Qui fait bouger l'opinion » : la réponse à la demande ⭐

- **Une courbe par type de source** : **Joueurs**, **Animation**, **Avatars IA**, **Faits injectés**. Valeur = **déplacement cumulé depuis le début de la période**, signé. Au-dessus de zéro, la source a poussé la population **vers « soutient »** ; en dessous, **vers « rejette »**.
- **Unité commune avec la position moyenne** : exprimer chaque déplacement en **points de moyenne** (contribution au déplacement de la position moyenne des 105 avatars). Alors la lecture devient arithmétique : « la moyenne a gagné 6 points, dont 4,1 par les joueurs ». C'est une remontée PLEIADE (R-API-2). Si la somme des quatre ne fait pas la variation de la moyenne (oubli, retour vers la fiche), ajouter une 5e courbe grise fine **« Retour vers la fiche (oubli) »** plutôt que de laisser un écart inexpliqué : à faire préciser par le PSYCHOLOGUE.
- **Faire ressortir les joueurs sans couleur de camp** : les joueurs ont la **seule couleur d'accent** (`--color-craie`, trait de 3,5 px) ; les trois autres sont des **neutres** distingués par le trait, doublé par le libellé : Animation `--color-ink-body` plein, Avatars IA `--color-ink-muted` tirets, Faits injectés `--color-ink-faint` pointillés. Pas de rouge, de bleu ni de vert : ils évoquent les camps eho ou un « bien / mal ». L'œil va droit sur la courbe des joueurs (attention préattentive : une seule couleur saturée).
- **Pôles écrits sur le graphique**, repris des pôles de l'axe (avis n°102) : `▲ vers « soutient la FORCE »` en haut à gauche de la zone, `▼ vers « rejette la FORCE »` en bas. Le titre dit l'axe : « Qui fait bouger l'opinion sur « FORCE » ».
- **Légende** : la valeur affichée est le **cumul à la fin de la période**, signé (`Joueurs +4,1`), pas une somme. **Bulle de survol** : l'heure, puis pour chaque source « cumul +3,2 (cette heure +0,7) », dans l'**ordre fixe** de la légende (un tri par valeur signée ferait sauter les lignes d'une heure à l'autre).
- **Phrase « quoi lire »** générée, en clair : « Sur la période, la moyenne « FORCE » est passée de +12 à +18 (+6). Les joueurs y ont contribué pour +4,1, l'animation +1,6, les faits injectés +1,1, les avatars IA entre eux −0,8. »
- **Joueurs et animation séparés** : c'est indispensable à la demande (« par rapport à ce que font les joueurs »). Les données décrites les regroupent en « comptes des joueurs et de l'animation » : il faut que le moteur les distingue (R-API-1). En attendant, une seule courbe **« Comptes humains (joueurs et animation) »** en craie, et l'écart est dit dans la phrase d'aide.
- Pas de case « par heure » en plus : le cumul montre la tendance, la bulle donne l'heure. Une option « Par heure » en barres divergentes pourra venir plus tard si l'animation la demande.

## R4. Position moyenne et avatars ébranlés (blocs 3 et 4)

- **Position moyenne** : une courbe, plus une **ligne de référence en tirets « départ (fiches) : +12 »**. Domaine automatique qui **contient toujours 0 et la valeur de départ**, arrondi au pas, borné à ±100 (le domaine fixe −100..+100 écraserait un mouvement de 6 points ; il reste celui des mini-courbes et de la courbe d'un avatar). Pôles écrits comme en R3.
- **Avatars ébranlés** (valeurs ≥ 0, `GrapheTemps` actuel suffit) : « **En doute** » (nombre d'avatars à chaque relevé, trait plein) et « **Ont basculé** » (cumul des bascules depuis le début de la période, tirets). Axe : « avatars (sur 105) ». L'**écart moyen depuis la fiche** va dans la carte de l'axe et dans l'aide de ce bloc (« écart moyen 9 points »), pas sur une 3e courbe : ce n'est pas la même unité.

## R5. Tableau « Comptes qui ont le plus fait bouger » (axe choisi)

| Compte | Type | Vers « soutient » | Vers « rejette » | Bilan |
|---|---|---|---|---|
| @capitaine_dupont · Cne Dupont | Joueur | +3,0 | −0,4 | ▲ +2,6 `──█▌` |
| Fait : « Explosion au dépôt de Kel » | Fait injecté | — | −1,9 | ▼ −1,9 `▐██──` |

- **Bilan** avec une petite **barre divergente** centrée sur zéro (vers la droite = soutient, vers la gauche = rejette), plus le signe et la flèche. Les colonnes « vers soutient » et « vers rejette » montrent qu'un compte peut pousser dans les deux sens.
- **Tri par défaut : |bilan| décroissant** (ceux qui ont le plus bougé l'opinion, quel que soit le sens). En-têtes triables (`aria-sort`).
- **Puces de filtre par type** (Joueurs · Animation · Avatars IA · Faits injectés), **Joueurs cochés par défaut** : c'est la question posée. 10 lignes, puis « Voir les 37 comptes ».
- Les « faits crus » du moteur s'appellent **« Faits injectés »** à l'écran (à confirmer par PLEIADE : un fait sans compte, venu de l'animation).

## R6. Tableau des avatars, et la courbe d'un avatar au clic

| Avatar | Camp eho | Départ → actuel | Écart | État |
|---|---|---|---|---|
| Ivana Rostova · @ivana_r | 🔵 bleu | `−100 ──○━━━●── +100` −30 → +5 | ▲ +35 | ⚠ a basculé à 11:00 |
| Piet Maes · @pmaes | ⚪ neutre | `−100 ────●○─── +100` +20 → +12 | ▼ −8 | ? en doute |

- **Départ → actuel** en « haltère » sur une piste −100..+100 avec repère zéro : rond creux = départ, rond plein = actuel, trait entre les deux. Les deux nombres sont écrits à côté.
- **Camp eho en colonne de texte** (émoji **et** mot, lu chez eho), **jamais en couleur de ligne** : le camp est une donnée de lecture, pas un codage du graphique.
- **État** : icône **et** mot (« en doute », « a basculé à 11:00 ») ; une bascule l'emporte sur le doute.
- **Tri par défaut : |écart| décroissant.** Filtres : « En doute », « A basculé », recherche par nom ou identifiant.
- **Clic sur une ligne** (bouton de toute la ligne, `aria-expanded`) : la ligne s'ouvre en dessous (motif Disclosure, pas de fenêtre) sur un `GrapheTemps` de l'avatar, **domaine fixe −100..+100**, ligne de référence « sa fiche : −30 », point marqué à l'heure de la bascule. Bouton « Tous les axes » pour afficher ses 4 à 8 courbes (couleurs neutres + libellés). Une seule ligne ouverte à la fois ; Échap la referme.
- Si le moteur sait dire **qui a fait bouger cet avatar**, ajouter sous sa courbe les 3 premiers comptes (même format que R5). Sinon, ne rien laisser croire.

## R7. Extension de `GrapheTemps` (rétrocompatible : par défaut, rien ne change)

| Prop nouvelle | Rôle |
|---|---|
| `domaine?: "zero" \| "auto" \| [min, max]` | `"zero"` (défaut actuel : 0..max) · `"auto"` : de min à max, **contient toujours 0**, arrondi au pas 1-2-5 · `[−100, 100]` : fixe |
| `reference?: { valeur: number; libelle: string }` | ligne en tirets étiquetée (« départ (fiches) : +12 ») |
| `poles?: { haut: string; bas: string }` | « ▲ vers soutient… » / « ▼ vers rejette… » dans les coins gauches de la zone |
| `libelleAxe?: string` | remplace « {unite} par heure », codé en dur (une position n'est pas « par heure ») |
| `legende?: "somme" \| "dernier"` | total de la période (défaut) ou dernière valeur, signée |
| `format?: (v) => string` | signe explicite (`+4,1`, `−0,8`, U+2212), virgule française |
| `bulle?: "tri" \| "fixe"` | ordre de la bulle : par valeur (défaut) ou ordre de la légende |
| `epaisseur` et `pointilles` par série | trait de l'accent (joueurs) et 3e style de trait, en plus des tirets |
| `valeurs: (number \| null)[]` | **`null` = pas de relevé** : la courbe s'interrompt, la bulle écrit « pas de relevé ». Une absence n'est jamais un zéro |

Et trois corrections internes : les repères partent de `floor(min / pas) × pas` ; le **zéro est un trait plein plus marqué** (`--color-line`, 1,5 px) même quand il est au milieu ; les points s'affichent pour `v !== null` (aujourd'hui `v > 0` efface les valeurs négatives et le zéro).

## R8. États vides et dégradés : chacun sa phrase

| Situation | Ce que montre le panneau |
|---|---|
| Pas de moteur IA dans la zone | Le panneau **n'apparaît pas** (rien à lire, rien à configurer ici). |
| Moteur déployé, **aucun relevé encore** | « Le moteur IA relève l'opinion chaque heure : premier relevé vers 15:00. » Les cartes montrent la position des fiches de départ ; le tableau des avatars est déjà lisible (départ = actuel). |
| Moteur **à l'arrêt** | Bandeau `role="status"` : « Moteur IA à l'arrêt depuis 14:00 : les courbes s'arrêtent au dernier relevé. » Les courbes s'interrompent (`null`), sans retomber à zéro. |
| Période **sans relevé** | « Aucun relevé du 12/10 08:00 au 12/10 10:00. Relevés disponibles du 11/10 16:00 au 12/10 14:00. » + bouton **« Caler la période sur les relevés »**. |
| Aucun déplacement sur la période | Les courbes restent à zéro, et la phrase le dit : « Aucun déplacement d'opinion attribué sur la période. » |
| Moteur injoignable | Même ligne d'erreur que « Publications par cellule » : « Indisponible : le moteur IA ne répond pas. » Le reste du Reporting continue. |

En mode **En direct**, le graphique se recalcule à la minute comme le reste, mais l'en-tête dit la vraie fraîcheur : « **dernier relevé 14:00 · prochain vers 15:00** ». Sinon l'animateur croit voir du temps réel.

---

## Doctrine dégagée

⭐ **Une grandeur signée se lit sur un zéro marqué et des pôles écrits.** Le sens (« vers soutient » / « vers rejette ») se dit par la position et par des mots, jamais par une couleur qui rappelle un camp. **Pour montrer l'effet d'un acteur, on lui donne la seule couleur d'accent et on met les autres en neutres.** Une absence de relevé interrompt la courbe : ce n'est jamais un zéro.

## Remontées

- **PLEIADE** — R-API-1 : distinguer **joueurs** et **animation** dans l'attribution (rôle ou groupe eho du compte) · R-API-2 : exprimer l'attribution en **points de moyenne**, pour qu'elle s'additionne à la variation de la position moyenne · R-API-3 : renvoyer les **pôles** et libellés des axes actifs (avis n°102), les heures sans relevé en `null`, l'heure du dernier relevé et l'état du moteur · R-API-4 : une route BFF du cockpit (`/api/bff/opinion?axe=&from=&to=`) qui lit le moteur côté serveur.
- **PSYCHOLOGUE** — définition affichable du **doute** et de la **bascule** (franchissement de zéro ? seuil ?) ; existence d'un « retour vers la fiche » à montrer comme 5e courbe.
- **CYBERSECU** — lecture serveur à serveur cockpit → moteur IA, réservée au rôle « analyste » ; aucune donnée d'opinion exposée aux joueurs.

## Points à trancher par l'utilisateur

1. Bloc 2 avec **Joueurs et Animation séparés** dès la première version, ou une courbe « Comptes humains » en attendant R-API-1 ?
2. Blocs 3 et 4 **ouverts** ou **repliés** par défaut ?
3. Tableau des comptes filtré sur **Joueurs par défaut**, ou tous les types ?
4. Le mot à l'écran pour les « faits crus » : « Faits injectés » convient-il ?
