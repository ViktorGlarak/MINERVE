# Avis n°37 — app-admin : changer la cible d'un scénario existant (un incident, une storyline, du bruit)

> **Date** : 2026-10-03 · **Demandeur** : l'utilisateur · **Écrans** : `app-admin`, bandeau en tête de la fiche d'un scénario (`IncidentPicker.tsx` › `BandeauIncident`, appelé par `editor/ScenarioEditor.tsx` l. 201-215), création (`NewScenarioDialog.tsx`), fenêtre commune (`dialogs/Modal.tsx`).
> **Statut** : 🟡 proposé, à arbitrer par l'utilisateur. La mise en œuvre revient à PLEIADE / ARCHITECTE, à tester en local avant tout push.
> Suite des avis n°28 (lien avec l'incident MELMIL), n°31 (scénario de storyline) et n°36 (bruit de fond).
> ⚠ DESIGNER contribue, il ne tranche pas : ce sont des propositions argumentées. Le besoin de l'utilisateur et les choix de PLEIADE / ARCHITECTE font foi.

## Besoin exprimé

Un ancien scénario, « **08.01 STARTEX** », a été créé avant la fonction « storyline ». Il n'est relié à aucun incident. Sur sa fiche, le bandeau n'offre qu'une liste déroulante pour choisir **un** incident. L'utilisateur veut en sélectionner **plusieurs**, c'est-à-dire le rattacher à la storyline 08.01 en cochant ses incidents. Il estime que la liste déroulante n'est pas le bon contrôle. Autre défaut : la liste ne se ferme pas quand on clique à l'extérieur (corrigé à part).

## Constat (lecture du code, 2026-10-03)

| # | Constat | Gravité (Nielsen, 0-4) | Source |
|---|---|---|---|
| C1 | **Deux écrans, deux modèles pour la même notion.** À la création, la cible se choisit parmi 3 options (segment « Cet incident / Toute une storyline / Bruit de fond »). Sur la fiche, on ne peut choisir qu'**un incident** (ou du bruit, en bas de la liste). Un scénario déjà créé ne peut donc **jamais** devenir un scénario de storyline. Le serveur, lui, accepte déjà `{ storylineCode, incidentIds }` en PATCH : seul l'écran manque. | 3 | Heuristique 4 « cohérence », heuristique 7 « souplesse » (REF-14) |
| C2 | **Un scénario de storyline est figé.** Son bandeau (`ScenarioEditor` l. 205-209) est en lecture seule. Le commentaire dit que « l'édition du périmètre reste MELMIL ». **C'est faux** : dans `app-melmil`, la route `api/zone/scenarios` n'a qu'un `GET`. On ne peut ni ajouter ni retirer un incident d'un scénario de storyline, nulle part. Le seul recours est de supprimer et recréer le scénario, ce qui perd ses items. | 3 | Heuristique 3 « contrôle et liberté » (REF-14) |
| C3 | **Le bandeau ne dit pas quels incidents sont couverts** : seulement « n incidents couverts ». Pour savoir si I12 en fait partie, il faut aller dans MELMIL. | 2 | Heuristique 6 « reconnaître plutôt que se rappeler » (REF-14) |
| C4 | **Le choix d'un incident est enregistré dès le clic dans la liste**, sans bouton de validation. Pour un seul incident, cela allait. Pour une sélection en plusieurs gestes (une storyline, puis des cases), il faut un moment où l'on **valide**. | 2 | Heuristique 3 et 5 (REF-14) |
| C5 | **La sortie « bruit de fond » est logée dans la liste déroulante** (n°36, R14/R15, placée au pied de la liste). Un bouton dans un `role="listbox"` n'est pas permis par ARIA : une liste ne contient que des options et des groupes. | 2 | REF-13 4.1.2 ; APG Listbox *(modèle pas encore ingéré en fiche, cf. §5 bis)* |
| C6 | **La fenêtre commune (`Modal`) n'est pas complète** : pas de piège du focus, pas de retour du focus au déclencheur, pas d'`aria-labelledby`. Elle se ferme aussi au moindre clic sur le fond, ce qui ferait perdre des cases cochées. | 2 | Règle 11 ; WAI-ARIA APG Dialog (REF-19) |
| C7 | **Fermeture au clic extérieur** : la correction est présente dans la copie de travail (`pointerdown` sur le document, l. 132-141, non commitée au 2026-10-03). | — | — |

## Recommandations (classées par gain)

### 1. Une seule porte pour changer la cible : la fenêtre « Cible du scénario »

**R1 — Le bandeau garde son rôle (dire ce qu'est le scénario), et un seul bouton ouvre une fenêtre de choix.** Plutôt qu'un panneau qui se déplie dans le bandeau, une **fenêtre modale**.
- *Pourquoi une fenêtre et pas un panneau qui se déplie* :
  1. le bandeau est dans l'**en-tête collant** de la fiche (`ed-sticky`). Une liste de 5 à 15 cases dépliée là ferait grandir l'en-tête et repousserait l'éditeur à chaque ouverture ;
  2. le choix se fait en **plusieurs gestes** puis se **valide** (C4). C'est exactement le cas d'usage d'une fenêtre : une tâche courte, isolée, avec « Annuler » et un bouton de validation (APG Dialog, REF-19) ;
  3. c'est l'occasion de **réutiliser tel quel** le bloc « Cible du scénario » de la création. Un seul composant, un seul comportement, rien à réapprendre (Jakob, REF-06 ; heuristique 4, REF-14).
- **Mise en œuvre** : extraire de `NewScenarioDialog` un composant `ChoixCible` (segment + sélecteur d'incident + storyline et cases + ligne d'aide du bruit), avec une valeur contrôlée `{ mode, incidentId, storylineCode, incidentIds }`. La création et la fiche l'utilisent toutes deux. *Effort : moyen.*

**R2 — Le bouton du bandeau, selon l'état du scénario** (`pl-btn-secondary`, éditeurs seulement ; les points de suspension signalent qu'un choix va s'ouvrir) :

| État | Intitulé du bandeau | Contenu | Bouton |
|---|---|---|---|
| Sans cible (« Non classé ») | **Cible MELMIL** | « *Ce scénario n'est rattaché à rien : choisissez un incident, une storyline, ou déclarez-le bruit de fond.* » | **Rattacher…** |
| Un incident | **Incident MELMIL** | étiquette actuelle (code, intitulé, storyline, moment) + « MELMIL ↗ » | **Changer…** |
| Une storyline | **Storyline MELMIL** | voir R9 | **Changer…** |
| Bruit de fond | **Bruit de fond** (icône `activity`) | phrase actuelle du n°36, R12 | **Rattacher…** (remplace « Rattacher à un incident… », puisqu'on peut aussi viser une storyline) |

Pour un observateur : le même bandeau, **sans bouton** (pas de bouton qui mène à un refus, règle déjà appliquée).
- **Remplace** le sélecteur ouvert d'office pour un « Non classé », le bouton « C'est du bruit de fond » et l'option « Aucun incident : en faire du bruit de fond » au pied de la liste (n°36, R14/R15). Ces trois sorties deviennent les trois choix du segment. Cela règle aussi C5.
- **Proposition par le nom, sans rien enregistrer** (Tesler, REF-06) : pour un « Non classé » dont le nom commence par un code, une ligne discrète sous le texte : « *D'après son nom, ce scénario semble relever de la storyline **08.01**.* » Le bouton « Rattacher… » ouvre alors la fenêtre déjà réglée (R4).

**R3 — La fenêtre « Cible du scénario ».**
- **Titre** : « **Cible du scénario** », suivi du nom du scénario en sous-titre (« 08.01 STARTEX »), pour qu'on sache sur quoi on agit.
- **Segment, libellés alignés partout** : « **Un incident | Une storyline | Bruit de fond** ». Je propose de changer **aussi** ceux de la création :
  - « Cet incident » supposait qu'un incident était déjà en vue (arrivée depuis MELMIL). Ce n'est pas le cas en général ;
  - « Toute une storyline » est inexact, puisqu'on peut décocher des incidents.
  - Le même mot sur les deux écrans (heuristique 4, REF-14). Segment en `radiogroup` comme aujourd'hui (flèches, `aria-checked`), ordre inchangé, « Bruit de fond » en dernier (n°36, R1).
- **Pied de fenêtre** : « Annuler » (bouton texte) et **un seul bouton principal** (règle 6). Son libellé dit ce qui va se passer (GOV.UK, REF-10) :
  - Un incident : « **Rattacher à 08.01.I04** » ;
  - Une storyline : « **Rattacher à 3 incidents** » ;
  - Bruit de fond : « **Classer en bruit de fond** ».
- **Bouton grisé** tant que la sélection est **identique à la cible actuelle** (rien à enregistrer) ou **incomplète** (R6). Dans le second cas, un message dit pourquoi, sous le bloc, au même endroit qu'à la création.
- **Phrase de conséquence** au-dessus du pied dès que la sélection **retire** quelque chose de MELMIL, parce que le geste change ce que voit une **autre cellule** (heuristique 5, REF-14 ; n°36, R14) : « *Le pictogramme ▶ disparaîtra de 08.01.I12 et 08.01.I15 dans MELMIL.* » Pas de seconde confirmation : le bouton suffit, et l'opération est réversible.
- **Après validation** : la fenêtre se ferme, le focus **revient au bouton** du bandeau, et une ligne d'état confirme dans le bandeau (`role="status"`, Peak-End, règle 18) : « *Rattaché à la storyline 08.01 : 3 incidents, le ▶ s'affiche sur chacun dans MELMIL.* »
- **En cas d'échec** (MELMIL injoignable : 503, incident disparu : 400), la fenêtre **reste ouverte**, la sélection est conservée, et l'erreur du serveur s'affiche au-dessus du pied avec quoi faire (« Réessayer »).
- **Fenêtre accessible** (C6, à corriger dans `Modal` pour tous ses usages) : `aria-labelledby` sur le titre, **piège du focus**, focus initial sur le **choix coché du segment**, `Échap` ferme (sauf si une liste déroulante est ouverte : elle se ferme d'abord, comme aujourd'hui), retour du focus au déclencheur (APG Dialog, REF-19 ; règle 11). **Le clic sur le fond ne ferme pas** cette fenêtre dès qu'un choix a été modifié : on ne perd pas des cases cochées par un clic de trop (heuristique 5, REF-14).
- *Effort : moyen* (fenêtre + correction de `Modal`).

**R4 — Ce qui est pré-rempli à l'ouverture : la cible actuelle, sinon ce que dit le nom.**

| Scénario | Mode ouvert | Pré-rempli |
|---|---|---|
| Un incident | Un incident | l'incident actuel, en étiquette + « Changer » (comme à la création) |
| Une storyline | Une storyline | la storyline ; **les incidents actuellement couverts sont cochés**, les autres non |
| Bruit de fond | Bruit de fond | rien |
| Sans cible, nom commençant par un **code d'incident** (« 08.01.I04 — … ») | Un incident | cet incident, s'il existe dans MELMIL |
| Sans cible, nom commençant par un **code de storyline** seul (« **08.01 STARTEX** ») | Une storyline | la storyline 08.01, **tous ses incidents cochés** (même défaut qu'à la création, n°31 R2) |
| Sans cible, rien de reconnu | Un incident | rien |

- Quand la proposition vient du **nom**, une ligne le dit au-dessus du bloc : « *Proposé d'après le nom « 08.01 STARTEX ». Vérifiez les incidents cochés.* » L'humain voit pourquoi c'est pré-rempli et garde la main (Tesler, REF-06 ; heuristique 1, REF-14). On ne pré-remplit que ce que l'on **sait** : un code inconnu de MELMIL ne pré-sélectionne rien.
- **Changer de mode ne perd rien** : passer de « Une storyline » à « Un incident » puis revenir retrouve les cases telles qu'on les a laissées (état gardé par mode tant que la fenêtre est ouverte).
- **Le nom n'est jamais modifié** par un changement de cible, contrairement à la création où il est pré-rempli (n°36, à éviter n°10). Le nom d'un scénario existant appartient à l'humain.

### 2. Le mode « Une storyline »

**R5 — Choisir la storyline : garder le `<select>` natif, en l'enrichissant.**
- *Pourquoi pas une liste filtrable* : un exercice compte de l'ordre de **10 à 20 storylines**. Un `<select>` natif suffit, il est accessible et identique sur tous les navigateurs, et il est déjà celui de la création (Jakob, REF-06). Une combobox à recherche n'apporte quelque chose qu'au-delà de **~25 options** : à reconsidérer si un exercice dépasse ce seuil.
- **Options** : « **08.01 — Startex · 5 incidents** ». Le nombre aide à reconnaître la bonne storyline sans l'ouvrir (heuristique 6, REF-14).
- **Étiquette visible** « Storyline », reliée au `<select>` (`<label for>`), et non le seul placeholder « Choisir une storyline… » (REF-13 1.3.1, 3.3.2).
- **Changer de storyline** coche tous les incidents de la nouvelle (défaut de la création). **Revenir** à la storyline actuelle du scénario rétablit les cases **telles qu'elles étaient enregistrées**, pas « tout coché ».

**R6 — La liste des incidents à cocher : le modèle de la création, avec quatre ajouts.**
1. **Structure accessible** : `<fieldset>` avec `<legend>` « Incidents couverts » (qui peut être visuellement discrète), une vraie case par incident, toute la ligne cliquable (`<label>`), cible d'au moins 24 px de haut (règle 12 ; REF-13 1.3.1, 2.5.8).
2. **Mêmes repères que le sélecteur d'un incident** : code en mono, intitulé, **moment** (« D+31 · 14:00 ») et, à droite, « **2 scénarios** » quand l'incident en a déjà. Le doublon se voit avant d'être créé, comme au n°28 (R2). Le scénario en cours n'est pas compté dans ce nombre.
3. **Compteur annoncé** : « **3 / 5 incidents** : l'icône de scénario s'affichera sur chacun. » Il est placé dans une zone `aria-live="polite"` pour qu'un lecteur d'écran entende le compte changer. « Tout cocher / Tout décocher » reste un seul lien qui bascule, comme aujourd'hui.
4. **Incidents disparus de MELMIL** : un incident couvert qui n'existe plus est affiché **en fin de liste**, case décochée et inactive, avec la mention « *n'existe plus dans MELMIL : il sera retiré* ». Rien ne disparaît sans être dit (heuristique 1, REF-14).

- **Validation impossible tant qu'aucune case n'est cochée.** Le bouton est grisé et un message s'affiche sous la liste (GOV.UK : dire comment corriger, REF-10 ; règle 24) :
  > *Cochez au moins un incident. Pour ne rattacher ce scénario à aucun incident, choisissez « Bruit de fond ».*

  La seconde phrase donne la sortie au lieu de laisser l'utilisateur dans une impasse (Postel, REF-06).
- **Avant de choisir une storyline** : pas de liste vide, mais une ligne d'aide à la même place : « *Choisissez la storyline : ses incidents s'afficheront ici, tous cochés.* » La fenêtre ne saute pas quand la liste apparaît (n°36, R2).
- **Hauteur** : la liste défile en elle-même au-delà de ~8 lignes (`max-height` actuel de 220 px, à porter à ~280 px dans la fenêtre), le reste de la fenêtre ne bouge pas.
- *Effort : faible* (le modèle existe ; ajouts 2 à 4).

**R7 — Côté envoi** : la fenêtre envoie **exactement** l'une de ces trois formes, déjà acceptées par le PATCH : `{ incidentId }`, `{ storylineCode, incidentIds: [...] }`, `{ bruit: true }`. Jamais un mélange, même si un autre mode a laissé un état (n°36, R5). *Effort : nul côté serveur.*

### 3. Le bandeau d'un scénario de storyline

**R8 — Oui, ajouter « Changer… »** (éditeurs seulement). Le n°31 l'avait laissé en lecture seule en supposant que MELMIL gérait le périmètre. Ce n'est pas le cas (C2) : **sans ce bouton, un périmètre faux est définitif**. Le bouton ouvre la même fenêtre (R3), en mode « Une storyline », cases actuelles cochées (R4).
- *Si l'on préfère que MELMIL soit le lieu d'édition* : ce serait une fonction nouvelle à construire dans MELMIL. En attendant, l'admin est le seul endroit possible. Rien n'empêche d'avoir les deux plus tard : les deux apps écrivent alors la même donnée.

**R9 — Le bandeau montre les codes couverts, pas seulement leur nombre** (C3) :

> **STORYLINE MELMIL** `08.01` Startex — 3 incidents sur 5 : `I03` `I04` `I07` · MELMIL ↗ · **Changer…**

- Les codes courts (« I03 ») en mono, dans le style des codes actuels, suivis d'une infobulle (`title` + texte lisible au lecteur d'écran) avec l'intitulé complet.
- « **3 incidents sur 5** » dit d'un coup d'œil si la storyline est couverte en entier ou en partie (reconnaître plutôt que se rappeler, heuristique 6, REF-14).
- Au-delà de **8 codes**, on montre les 8 premiers puis « **+ 4** », qui ouvre la fenêtre en lecture (les observateurs peuvent ainsi tout voir sans pouvoir rien modifier).
- Même structure que le bandeau d'un incident (intitulé `pl-eyebrow` à gauche, contenu, actions à droite), pour que les quatre états se lisent pareil (heuristique 4, REF-14).
- *Effort : faible.*

### 4. La liste déroulante d'un incident (combobox)

**R10 — Comportement attendu, conforme au modèle Combobox du WAI-ARIA APG** *(modèle pas encore ingéré en fiche : la fiche REF-19 ne couvre que Dialog et Tabs, cf. §5 bis ; ce qui suit reprend le modèle publié)* :
- **Clic ou appui hors du sélecteur** : la liste se ferme, **rien n'est choisi**, le texte tapé est conservé. C'est ce que fait la correction en cours (C7). Ajouter le cas du **toucher** (le `pointerdown` le couvre déjà).
- **Échap** : 1er appui, la liste se ferme (le texte reste) ; 2e appui, liste fermée, le texte est effacé ; 3e appui, dans la fenêtre, la fenêtre se ferme. Chaque `Échap` défait **une seule chose** à la fois.
- **Tab** : la liste se ferme et le focus passe au champ suivant **sans choisir** l'option active. Un choix ne doit jamais arriver par accident.
- **Ouverture** : à la frappe, à `↓` / `Alt+↓`, ou au clic dans le champ. **Pas à la prise de focus automatique** : dans la fenêtre, une liste qui s'ouvre toute seule recouvrirait le segment et le pied avant que l'utilisateur ait rien demandé.
- **Option active** : seule l'option sous le clavier ou la souris est marquée, et `aria-selected` ne s'applique qu'à elle, comme aujourd'hui.
- **Contenu de la liste** : uniquement des options et des groupes. **Plus aucun bouton dedans** (C5) : la sortie vers le bruit passe au segment (R2, R3).
- *Effort : faible.*

## À éviter

1. **Un panneau qui se déplie dans l'en-tête collant** : l'en-tête grandit, l'éditeur saute, et l'on ne sait plus où finit la tâche (R1).
2. **Deux contrôles différents pour la même notion** selon qu'on crée ou qu'on modifie (segment d'un côté, liste déroulante de l'autre) : c'est l'origine du constat (C1).
3. **Une liste déroulante à choix multiple** (combobox à plusieurs choix, ou `<select multiple>`) : les choix sont cachés, l'état de la sélection n'est pas visible d'un coup d'œil, et le `<select multiple>` exige Ctrl+clic, que personne ne connaît. Des cases visibles restent le bon contrôle pour « plusieurs parmi quelques-uns ».
4. **Enregistrer à chaque case cochée** : un périmètre en cours de composition s'afficherait à moitié dans MELMIL. On valide une fois (C4).
5. **Une seconde fenêtre de confirmation** après « Rattacher » : la phrase de conséquence dans la fenêtre suffit, l'opération est réversible.
6. **Rattacher automatiquement** un « Non classé » d'après son nom, sans geste humain : on **propose**, l'humain **valide** (doctrine du n°33).
7. **Renommer le scénario** au changement de cible (n°36, à éviter n°10).
8. **Garder « C'est du bruit de fond » et l'option au pied de la liste** à côté du segment : trois portes pour un même geste.
9. **Fermer la fenêtre au clic sur le fond** quand des cases ont été modifiées.
10. **Laisser dans le code le commentaire « l'édition du périmètre reste MELMIL »** : il est faux (C2) et pourrait induire une autre décision en erreur.

## Questions à l'utilisateur (réponse par défaut proposée entre crochets)

- **Libellés de la création** : aligner aussi « Cet incident / Toute une storyline » sur « Un incident / Une storyline » ? [Oui, le même mot partout.]
- **Un scénario en lecture** (`playing`) : peut-on changer sa cible pendant qu'il joue ? [Oui : cela ne change que les pictogrammes de MELMIL, pas les publications. Le statut « terminé » reste en lecture seule, comme aujourd'hui (`canEdit`).]
- **« 08.01 STARTEX »** : couvrir **tous** les incidents de 08.01 ? [Oui par défaut, tous cochés ; l'utilisateur décoche ceux que le STARTEX ne couvre pas.]
- **Édition du périmètre depuis MELMIL** : à prévoir plus tard ? [Non pour l'instant : un seul endroit, l'admin, tant que le besoin n'est pas exprimé.]

## Doctrine retenue

⭐ **Une même notion se choisit avec le même contrôle, partout où on la choisit.** Si la création offre trois cibles, la modification offre les trois mêmes, dans le même composant. Et **un choix composé en plusieurs gestes se valide une fois**, dans une fenêtre qui dit ce qui va changer.
