# Avis DESIGNER n°77 — Animation (`app-admin`) : un même menu, une même charte sur toutes les pages

> **Date** : 2026-10-07 · **Apps** : `app-admin` (et, pour les règles, les autres apps de la zone) · **Demande utilisateur** : « toutes les pages devraient avoir le même menu et une charte de style cohérente, pour que l'utilisateur ne se perde pas. Tu me proposes quoi ? (analyse les autres pages également) ».
> **Matière** : 2 captures en production (`52.png` liste, `53.png` éditeur) et 13 captures en local (`scratchpad\coherence\p01` à `p14`), confrontées au code en lecture seule (`globals.css`, `pleiade-theme.css`, `editor\editor.css`, `Shell.tsx`, `ScenariosList.tsx`, `Dashboard.tsx`, `Monitoring.tsx`, `editor\*.tsx`, `EtatTag.tsx`, `lib\etats.ts`, `app\*\page.tsx`).
> **Maquette interactive** : `index.html` (même dossier), servie en local sur `http://127.0.0.1:3852/`. Elle montre la liste, l'éditeur et la Supervision, avec un interrupteur « actuel / proposé » par décision du §5. ★ = recommandation. Montrée à l'utilisateur le 2026-10-07.
> **Statut** : proposition. L'utilisateur décide. La mise en œuvre revient à PLEIADE et ARCHITECTE, avec un test en local avant tout push, et les scénarios mis en pause avant le push en production (mise à jour automatique de DELATTRE 26).

---

## 0. Le constat en une phrase

**Le menu est le même partout, mais pas ce qu'il y a dessous.** `Shell` (barre de zone, menu « Tableau de bord · Scénarios · Supervision », pied de page) entoure bien les 5 pages (`app\page.tsx`, `scenarios\page.tsx`, `scenarios\[id]\page.tsx`, `monitoring\page.tsx`, `aide\page.tsx`) et l'en-tête est collant (`Shell.tsx:33`, `sticky top-0`). Ce qui change d'une page à l'autre, c'est le **contenu sous le menu** : en-tête de page, filtres, étiquettes, mots, largeur. Chaque écran a été refait à son tour, par un avis différent (n°27, 47, 56, 70, 71, 76), **sans socle commun**. Résultat : **3 styles de filtres, 3 styles d'étiquettes d'état, 3 rendus du journal, 2 largeurs de page, 2 genres pour « publication »**.

⚠ **À vérifier en production** : sur `52.png` et `53.png`, on ne voit ni la barre de zone ni le menu. En local, ils sont présents sur toutes les pages, éditeur compris (`p05` à `p12`). Il s'agit soit d'un **cadrage de la capture**, soit d'une version en production **antérieure à l'avis n°71 (R3)**. Il suffit d'ouvrir l'éditeur en production et de remonter en haut de page pour le savoir.

---

## 1. Inventaire des incohérences

Gravité de 0 à 4 (Nielsen, REF-14). « 4. Cohérence » = heuristique 4 (cohérence et standards).

### 1.1 En-tête de page : sur-titre, titre, « ? », actions

| # | Constat | Captures | Code | Gravité |
|---|---|---|---|---|
| E1 | **Le sur-titre ne veut pas dire la même chose d'une page à l'autre.** Tableau de bord : « Théâtre d'entraînement » (rien à voir avec la page). Scénarios : « Scénarios de la zone » (redit le titre). Supervision : « Supervision » au-dessus de « Supervision » (doublon). Aide : « Aide » au-dessus de « Premiers pas ». Éditeur : « SCÉNARIO » à côté d'une flèche de retour. On ne retient aucune règle, ce n'est donc pas un repère (règle 30). | p01, p02, p03, p04, p05 | `Dashboard.tsx:51`, `ScenariosList.tsx:371`, `Monitoring.tsx:68`, `aide\page.tsx:80`, `ScenarioEditor.tsx:269` | 2 |
| E2 | **Deux en-têtes différents.** Tableau de bord, Scénarios et Supervision utilisent `PageHeader` (titre de 27 px, « ? » collé au titre, action principale à droite). L'**éditeur** refait son propre en-tête : le « ? » tombe **seul sur une ligne, sous le titre**, et les actions (Vérifier · Lancer · Plus) passent **à droite** (53, p12) ou **à gauche sous les dates** (p05) selon la longueur du titre. L'**Aide** refait aussi son titre, en `text-[26px]` au lieu du jeton `text-page` (27 px). | 53, p05, p12, p04 | `Shell.tsx:68` (`PageHeader`) ; `ScenarioEditor.tsx:262-296` ; `aide\page.tsx:81` | 3 |
| E3 | **Pas de fil d'Ariane ni de retour nommé.** Le retour de l'éditeur est une flèche seule (icône sans mot) ; « où suis-je ? » ne se lit que par l'onglet « Scénarios » souligné dans le menu. | 53, p05 | `ScenarioEditor.tsx:268` | 2 |
| E4 | **Les actions changent de place et de poids.** « + Nouveau scénario » est en crème plein à droite (p01, p02). Dans l'éditeur, « Vérifier » est en crème plein (brouillon, p05) ou encadré (terminé, 53). Dans Supervision, « Suivre » est un **interrupteur** dessiné comme un bouton principal crème (p03). Le crème plein sert donc **à la fois** à l'action principale, au filtre actif et à l'interrupteur (voir E7). | p01, p02, p03, p05, 53 | `Monitoring.tsx:87` (`pl-btn-primary` sur un `aria-pressed`) | 2 |

### 1.2 Barres d'outils, filtres, recherche

| # | Constat | Captures | Code | Gravité |
|---|---|---|---|---|
| E5 | **Trois dessins pour « choisir un filtre ».** (a) Liste : **puces encadrées en CAPITALES espacées**, « TOUS 59 · BROUILLON 5 · LANCÉ 27 » (`.pa-filter-btn`). (b) Éditeur, arbre et chronogramme : **contrôle segmenté en casse normale**, « Tous 35 \| Brouillons 0 \| Publiés 35 \| Erreurs 0 » (`.tv-seg`, `.tc-seg`, `.ag-seg`). (c) Fenêtre « Nouveau scénario » : un **troisième segmenté**, au fond crème plein (« Un incident \| Une storyline \| Bruit de fond »). Et dans Réglages, les puces CAPITALES reviennent (« AUCUNE GREFFE · SOCIAL »). Le même geste (« je ne veux voir que… ») a trois apparences (règle 15, Jakob ; heuristique 4). | 52, 53, p02, p05, p06, p07, p11 | `globals.css` `.pa-filter-btn` ; `editor.css:146` `.ed-filter` (**copie** de `.pa-filter-btn`) ; `editor.css:325` `.ag-seg`, `:355` `.tv-seg`, `:435` `.tc-seg` (**trois copies identiques**) ; `ChoixCible.tsx` | 3 |
| E6 | **Les capitales espacées sont difficiles à lire en 11 px** : « MES SCÉNARIOS 2 », « À CORRIGER 2 », « TERMINÉ 26 ». Les capitales se lisent bien pour un mot court qui sert de **titre de zone** (sur-titre), mal pour un **libellé qu'on compare** à ses voisins (REF-17). | 52, p02, p13 | `.pa-filter-btn` (`text-transform: uppercase; letter-spacing: .12em`) | 2 |
| E7 | **Le filtre actif a le même aplat crème que le bouton principal.** Sur la liste, on compte jusqu'à **4 aplats crème** (« + Nouveau scénario », « TOUS », « TOUS » de l'état, « TOUTES » de la cellule). L'œil ne sait plus où est l'action (règles 5 et 6, Von Restorff règle 20). L'éditeur, lui, marque le filtre actif en crème **pâle** (`--color-craie-soft`) : c'est la bonne solution, mais elle n'est pas la même que celle de la liste. | 52, p02 | `.pa-filter-btn[aria-pressed=true]` contre `.tv-seg [aria-checked=true]` | 3 |
| E8 | **Trois champs de recherche.** Liste : grand champ de 300 px, à gauche, placeholder « Rechercher : code (08.01, I04…) ou nom ». Arbre : petit champ dans la barre, « Rechercher #id, @avatar, texte… ». Chronogramme : « **Filtrer** #id, @avatar, texte… ». Hauteurs différentes, verbes différents (« Rechercher » / « Filtrer ») pour le même geste. | 52, 53, p05, p06 | `ScenariosList.tsx:378` ; `TreeView.tsx` ; `Timeline.tsx` | 1 |
| E9 | **« Tout déplier · Tout replier »** : **liens texte** rangés à droite de la ligne de filtres dans la liste, **paire de boutons encadrés** collée aux filtres dans l'arbre. L'ordre est le même (corrigé par l'avis n°71), mais pas la forme ni la place. | 52, 53, p02, p05 | `ScenariosList.tsx:390-391` ; `TreeView.tsx:269-270` | 1 |
| E10 | **Le libellé de zone dans le panneau redit l'onglet** (« ARBRE », « TIMELINE », « JOURNAL ») ou le **contredit** : l'onglet s'appelle « **Réglages** » (renommé par l'avis n°71) et son panneau s'intitule encore « **CONFIGURATION** » (règle 30 : titre = libellé du menu). | p05, p06, p07, p08 | `ConfigPanel.tsx` (titre de `Panel`) | 2 |
| E11 | **« SÉLECTIONNER »** : le seul bouton en capitales espacées de l'app ; tous les autres boutons sont en casse normale (« Ajouter sur Social », « Changer… », « Vérifier »). | p05, p14 | `TreeView.tsx` | 1 |

### 1.3 Étiquettes d'état

| # | Constat | Captures | Code | Gravité |
|---|---|---|---|---|
| E12 | **Deux familles d'étiquettes pour deux objets voisins.** Un **scénario** porte `EtatTag` : icône cerclée + mot, en sans (avis n°76). Une **publication** porte un **cadre en police mono, vert ou rouge** (« Publié », « Erreur »), et « Brouillon » en gris **sans cadre**. Sur 53, « Terminé » (cerclé) et « Publié » (mono vert) se côtoient : deux grammaires sur un même écran. | 53, p05, p12 | `EtatTag.tsx` + `.pa-etat-*` ; `editor.css:341-345` `.tv-st`, `.tv-st-pub`, `.tv-st-err`, `.tv-st-draft` | 3 |
| E13 | **Une troisième famille dans les journaux** : type de ligne en **aplat de couleur, en capitales et en anglais** (« ACTION », « PUBLISH », « ERROR », « TICK », « SKIP »), et les boutons de filtre de Supervision en anglais minuscule (« publish · error · skip · tick · action »). La table de couleurs est **recopiée trois fois**. | p01, p03, p08 | `Dashboard.tsx:104`, `Monitoring.tsx:10,83,94`, `ScenarioLog.tsx:8` (`LOG_TAG` / `TYPE_TAG`) | 2 |
| E14 | **« Brouillon » d'une publication en `--ink-faint`** : environ 3,5 : 1, sous le seuil de 4,5 : 1 pour du texte de 10,5 px. C'est le même défaut que celui corrigé sur la liste (avis n°76, §1.3). | p05, p14 | `.tv-st-draft { color: var(--color-ink-faint) }` | 2 |
| E15 | **« Brouillon » ment pour une publication d'un scénario lancé** : elle attend son heure, elle n'est plus un brouillon. Le lexique de zone dit déjà « **programmées / en direct** » (décision du 06/10). | p05 (et tout scénario Lancé) | `TreeView.tsx:240` (`draft → "Brouillon"`) | 2 |

### 1.4 Vocabulaire

| # | Constat | Où | Gravité |
|---|---|---|---|
| E16 | **Une même chose, plusieurs mots.** Une publication qui n'est pas partie s'appelle : « **Erreur** » (étiquette de l'arbre), « **Erreurs** » (filtre), « **en erreur** » (Réglages, « 1 en erreur »), « **EN ERREUR** » (Supervision), « **ERROR** » (journal), « **non partie** » (bandeau de l'éditeur, liste). L'avis n°76 a fixé « **non partie** » (et « à corriger » pour ce qu'il faut traiter). | 53, p03, p05, p07, p08 | 3 |
| E17 | **Deux genres pour « publication ».** Liste : « 35 / 35 **publiées** » ; éditeur : « 35/35 **publiés** », filtre « **Publiés** 35 », étiquette « **Publié** » ; Réglages : « 1 publié(s) » ; Supervision : « **PUBLIÉS** ». Le mot du lexique est « publication », donc **féminin**. | 52, 53, p03, p07 | 2 |
| E18 | **Singulier ici, pluriel là.** Filtres d'état de la liste au singulier (« Brouillon », décision n°76) ; filtres de l'arbre au pluriel (« Brouillons ») ; chiffres du tableau de bord au pluriel (« BROUILLONS », « TERMINÉS »). | p01, p02, p05 | 1 |
| E19 | **Restes techniques ou anglais** : « item(s) » dans le journal et les messages (« 1 item(s) », « l'item #102 ») alors que le lexique dit « publication » (avis n°71 R2) ; « Tick », « publish » ; « Apps publiables 01 ». | p01, p03 | 2 |
| E20 | **Chiffres : « 00 » ici, « 0 » là.** Tableau de bord : « 00 · 14 · 01 » (zéro ajouté). Supervision : « 0 · 0 · 0 ». | p01, p03 | 1 |

### 1.5 Typographie, mise en page, alertes

| # | Constat | Captures | Code | Gravité |
|---|---|---|---|---|
| E21 | **Deux largeurs de page : le bord gauche saute de 26 px** entre la liste et l'éditeur (liste de 359 à 1547 px sur 52 ; éditeur de 387 à 1523 px sur 53). Cause : l'éditeur ajoute **sa propre marge** (`px-[26px]`) **à l'intérieur** de celle de `Shell`, et déclare `max-w-[1400px]`, ce qui ne sert à rien dans un `main` limité à 1240 px. | 52/53, p02/p05 | `Shell.tsx:57` ; `ScenarioEditor.tsx:233` | 2 |
| E22 | **Mono et sans mélangés sans règle.** Journal du tableau de bord **en sans**, journal de Supervision et de l'éditeur **entièrement en mono**, messages compris. Mono pour « 1/18 publié · 1 non partie » dans l'en-tête de l'éditeur, sans pour le même chiffre dans la liste. Usage sain à généraliser : mono pour **codes, heures, identifiants**, sans pour **les phrases**. | p01, p03, p05, p08 | `.ed-log` (`font-mono`), `Monitoring.tsx` | 2 |
| E23 | **Tailles en dur** au lieu des jetons : `text-[11.5px]`, `text-[12px]`, `fontSize: "10.5px"` (sur-titre de `PageHeader`), `text-[26px]`… Le thème définit pourtant `--text-meta`, `--text-control`, `--text-body`, `--text-page`. | — | `Shell.tsx:72`, `ScenarioEditor.tsx`, `aide\page.tsx` | 1 |
| E24 | **Trois formes d'alerte.** Ligne de texte orange (« Modifié depuis la vérification… »), bandeau rouge encadré (« 1 publication non partie »), texte rouge sous un nom (liste : « 19 à corriger avant de lancer »). Le cadre jaune « INCIDENT MELMIL — MELMIL ne répond pas » est une quatrième forme, pour une panne. Il faut une forme par **niveau** (information, à faire, panne), pas une par écran (règle 24, GOV.UK). | p02, p05 | `ScenarioEditor.tsx`, `NonParties.tsx`, `BandeauCible.tsx`, `ScenariosList.tsx` | 2 |
| E25 | **Mobile (390 px) : l'éditeur déborde à l'horizontale.** La page fait environ 643 px de large alors que la barre et le menu s'arrêtent à 375 px. Les lignes de l'arbre et le bandeau MELMIL sortent de l'écran, ce qui fait défiler toute la page de côté. La liste, elle, se replie correctement (p13). | p14 (et p13 pour comparer) | `editor.css` (`.tv-ligne` en grille à colonnes fixes ; en-tête `min-w-[360px]` du champ de titre) | 2 (usage mobile rare, mais un défilement horizontal de page est un défaut net) |
| E26 | **Le menu sur mobile** occupe 3 lignes (logo, onglets, puis thème · G · Déconnexion), soit environ 200 px avant le contenu. C'est acceptable, mais à faire avec la règle de la barre de plateforme commune. | p13, p14 | `Shell.tsx:33-55` | 1 |

---

## 2. Ce qui est déjà cohérent : à garder

- **Le cadre commun** : barre de zone + menu à 3 rubriques + pied de page sur **toutes** les pages (`Shell`), en-tête collant, onglet actif souligné en crème. C'est le socle de l'avis n°69 (règles 29 et 30) : on le garde.
- **`PageHeader`** (titre 27 px, « ? » collé au titre, action principale à droite) : un bon gabarit, appliqué sur 3 pages sur 5. Il faut **l'étendre**, pas le refaire.
- **`EtatTag` + `lib\etats.ts`** : une seule table de libellés (mot, icône, couleur, aide) pour les états d'un scénario, partagée par la liste et l'éditeur. **C'est exactement le modèle à suivre** pour les publications et le journal.
- **`TagCellule`** et le **liseré de cellule** (avis n°56) : identiques sur la liste, l'éditeur et la fenêtre de création.
- **Les jetons du thème PLÉIADE** (`--color-*`, `--text-*`, `.pl-btn-*`, `.pl-input`, `.pl-panel`) et les polices (Archivo, JetBrains Mono pour les codes et les heures).
- **Le « ? » d'aide (`AideEcran`)** sur chaque écran, et la page « Premiers pas ».
- **Les icônes Lucide**, au même trait partout.
- **L'ordre « Tout déplier · Tout replier »**, unifié par l'avis n°71.
- **Le menu « Plus ▾ »** et une seule action principale dans l'éditeur (avis n°71 R5).

---

## 3. Proposition : un petit socle commun pour l'animation

> Principe : **un composant par geste, une table par vocabulaire**, comme `EtatTag` / `etats.ts` le fait déjà pour les états d'un scénario. On ne refait pas de thème : on **range** ce qui existe (REF-01 : des composants qu'on possède ; règle 3 : limiter les choix à l'avance ; règle 36 : vocabulaire contrôlé).

### 3.1 Gabarit de page — `PageHeader` étendu, utilisé par les 5 pages

```
[← Scénarios]                                   (retour nommé, seulement sur une page de détail)
Titre de la page  (?)   [méta : état · cellule · compteur]          [action principale] [Plus ▾]
```
- **Une seule largeur** : celle de `Shell` (contenu de 1188 px utiles). L'éditeur **retire sa propre marge** et son `max-w-[1400px]` inutile. Le bord gauche ne saute plus (E21).
- **Sur-titre** : on le **retire des pages de rubrique**, parce que le menu et le titre suffisent (règle 30 : titre = libellé du menu). Sur une **page de détail**, il est remplacé par un **lien de retour nommé**, « ← Scénarios » (motif *Back link* de GOV.UK, REF-22 : **un seul mécanisme**, pas de fil d'Ariane en plus du retour ; tension notée au §3.7 de la doctrine). Le titre « Aide / Premiers pas » devient « Premiers pas » seul.
- **Le « ? » toujours collé au titre**, sur la même ligne (E2).
- **Une zone de méta**, sous le titre ou à sa suite, pour l'état, la cellule et les compteurs (l'éditeur y range ce qui est aujourd'hui sur la ligne du sur-titre).
- **Une zone d'actions à droite, toujours au même endroit** : au plus **une** action principale (crème plein), le reste en secondaire ou dans « Plus ▾ » (règles 6 et 37). Sous 900 px, elle passe sous le titre, mais **toujours à droite et dans le même ordre**.
- **Le titre du panneau = le nom de l'onglet**, ou rien. Pas de « ARBRE » sous l'onglet « Arbre », pas de « CONFIGURATION » sous « Réglages » (E10).

### 3.2 Une barre de filtres et de recherche — composant `BarreFiltres`

```
[🔍 Rechercher : …        ]  [Tous 59 | Brouillon 5 | Lancé 27 | Pause 1 | Terminé 26]  [Mes scénarios] [À corriger 2]   ·····   Tout déplier · Tout replier
```
- **Ordre fixe** : recherche → filtres exclusifs → bascules indépendantes → (espace) → gestes d'affichage à droite.
- **Filtre exclusif** (un seul choix à la fois : état, cellule, statut d'une publication) → **contrôle segmenté** en **casse normale**, avec l'effectif, `role="radiogroup"` et flèches au clavier (REF-19). Un seul style CSS, `.pl-seg`, qui remplace `.pa-filter-btn`, `.ed-filter`, `.ag-seg`, `.tv-seg`, `.tc-seg` et le segmenté de `ChoixCible`.
- **Bascule indépendante** (« Mes scénarios », « À corriger », « Suivre ») → bouton à **`aria-pressed`**, de la même hauteur que le segmenté, sous la forme d'une puce encadrée qui se remplit d'une coche quand elle est active.
- **État actif = crème pâle** (`--color-craie-soft` + texte `--color-ink` + graisse 600), **jamais l'aplat crème plein**, qui reste réservé à l'action principale (E7 ; règles 5, 6 et 20).
- **Champ de recherche unique** (`ChampRecherche`) : loupe, même hauteur que les contrôles (32 px), verbe « **Rechercher** » partout, exemples propres à l'écran dans le placeholder, `Échap` efface. La largeur s'adapte à l'écran.
- **Gestes d'affichage** (« Tout déplier · Tout replier », zoom, « Affichage ▾ ») : en **boutons discrets** (texte, souligné au survol), **toujours à droite**.
- **Au-delà de 5 commandes**, ou sur un écran étroit, les filtres se replient derrière « **Filtres (n)** » (règle 37). La recherche reste visible.

### 3.3 Un seul style d'étiquette d'état — `Etiquette` (généralise `EtatTag`)

**Forme unique** : icône Lucide cerclée de 13 px + mot, en **sans**, casse normale, couleur portée par le texte et l'icône (`currentColor`), bulle d'aide au survol et au focus. Le **mono** est réservé aux codes et aux heures. Le **rouge** est réservé à ce qui est **à corriger** (règle 20 ; avis n°76).

| Objet | Technique | **Mot proposé** | Icône | Ton |
|---|---|---|---|---|
| Scénario | draft · playing · paused · done | Brouillon · Lancé · Pause · Terminé *(inchangé, n°76)* | circle-dashed · circle-play · circle-pause · circle-check | gris · vert · ocre · gris |
| Publication, scénario non lancé | draft | **Brouillon** | circle-dashed | gris (`--muted`, pas `--faint` : E14) |
| Publication, scénario lancé | draft (en attente) | **Programmée** | circle-dot (ou clock) | gris |
| Publication | publishing | **En cours d'envoi** | loader-circle (sans rotation si « réduire les animations ») | ocre |
| Publication | published | **Publiée** | circle-check | vert |
| Publication | error | **Non partie** | triangle-alert | **rouge** |
| Publication | error + `priseEnCompte` | **Prise en compte** | circle-check | gris (avis n°76 §5.3) |
| Journal | publish · error · action · tick · skip | **Publiée · Non partie · Action · Cycle · Ignorée** | idem | idem |

- Une table par objet dans `lib\` (`etats.ts` existe ; ajouter `etatsPublication.ts` et `journal.ts`), qui remplace `TreeView.tsx:240`, `ItemsTable.tsx:12`, `LOG_TAG` (×2) et `TYPE_TAG`.
- Le journal adopte une seule ligne, `LigneJournal` : heure en mono, étiquette, **phrase en sans**. Le même composant sert au tableau de bord, à Supervision et à l'onglet Journal de l'éditeur (E13, E22).

### 3.4 Règle de vocabulaire (à verser au `PLEIADE\LEXIQUE_ZONE.md`)
1. **publication** est **féminin** : « publiée(s) », « non partie(s) », « 35 / 35 publiées ».
2. **non partie** pour une publication en échec (jamais « erreur », « en erreur » ni « ERROR ») ; **à corriger** pour ce que l'animateur doit traiter (n°76).
3. **Un filtre porte le même mot que l'étiquette**, au singulier (« Brouillon 5 », pas « Brouillons 5 ») ; les intitulés de chiffres, eux, restent au pluriel (« Brouillons : 14 »).
4. **Titre de page = libellé du menu ; titre de panneau = libellé de l'onglet.**
5. **Pas d'anglais ni de jargon technique à l'écran** : publish, tick, item, error → leur équivalent français.
6. **Chiffres** : pas de zéro ajouté (« 0 », « 14 »), sauf décision contraire de l'utilisateur, alors appliquée partout.
7. **Casse** : CAPITALES espacées **seulement** pour les sur-titres de panneau et les en-têtes de colonnes. Boutons, filtres et étiquettes s'écrivent en casse normale.

### 3.5 Jetons et classes à fusionner

| Aujourd'hui | Demain |
|---|---|
| `.pa-filter-btn` (globals) + `.ed-filter` (editor.css, copie) | `.pl-toggle` (bascule `aria-pressed`) |
| `.ag-seg` + `.tv-seg` + `.tc-seg` (trois copies) + segmenté de `ChoixCible` | `.pl-seg` (une seule définition) |
| `.pa-chip` + `.ed-chip` | `.pl-chip` |
| `.pa-etat-*` + `.tv-st-*` + `pl-tag-prod/halt/app/outline` employés comme types de journal | `.pl-etiquette` + `[data-ton="neutre|ok|attente|alerte"]` |
| `.ed-tab` (onglets de l'éditeur) et `.pl-tab` (menu) | un seul `.pl-tab` (même soulignement crème, déjà quasi identiques) |
| `.ed-log*` + rendu du journal en ligne dans `Dashboard` / `Monitoring` | `LigneJournal` (composant) |
| Tailles en dur (`text-[11.5px]`, `10.5px`, `text-[26px]`…) | jetons `--text-meta / -control / -body / -page` |
| Texte en `--color-ink-faint` | `--color-ink-muted` pour tout texte ; `faint` réservé aux traits et aux décors |

Le tout reste dans le thème PLÉIADE existant (pas de nouvelle dépendance, pas de bibliothèque). On ajoute une **page de référence interne** (`app-admin\docs\SOCLE_UI.md`, ou une route `/socle` réservée à l'Administration) qui montre chaque composant une fois. C'est elle qu'on consulte avant d'écrire un nouvel écran.

### 3.6 Ce qui s'applique aux autres apps de la zone (sans unifier les thèmes)

La décision du 2026-09-24 tient : **pas de thème PLÉIADE unifié**. MELMIL et LEAC gardent graphite/craie, le social garde l'habillage des réseaux imités. On partage des **règles**, pas du CSS :
- **Gabarit d'en-tête** (titre = menu, « ? » collé, une action principale à droite, retour nommé sur une page de détail) → **MELMIL, cockpit, presse (rédaction), eho**.
- **Filtres** : segmenté pour un choix exclusif, bascule pour un choix indépendant, état actif en teinte pâle → **MELMIL** (Demandes, Écarts), **cockpit**.
- **Étiquettes d'état** : icône + mot, rouge = à corriger, mêmes mots pour les mêmes états → **MELMIL** (`scenarios-admin.ts` affiche déjà l'état des scénarios), **presse** (Brouillon · Programmé · Publié d'un article : mêmes icônes), **messagerie**.
- **Vocabulaire** §3.4 → toutes les apps, via le lexique de zone.
- ⛔ **Social et sites de presse publics** : hors champ (chartes des médias à reproduire).

---

## 4. Plan par étapes (priorisé)

| Étape | Contenu | Gain pour l'utilisateur | Risque | Ampleur |
|---|---|---|---|---|
| **1. Mots** | E16-E20 et E10 : « publiée(s) », « non partie », filtres au singulier, « Réglages » dans le panneau, journal en français, « item » → « publication », chiffres sans zéro ajouté. Uniquement des libellés, rassemblés dans des tables `lib\`. | **Fort** : c'est ce qu'on lit en premier | **Faible** (aucune logique touchée) | **½ journée** |
| **2. Étiquettes** | `Etiquette` + tables publication et journal ; « Programmée » dans un scénario lancé ; `LigneJournal` partagé ; `--faint` → `--muted` (E12-E15, E22). | **Fort** sur l'éditeur et Supervision | Faible | **½ journée** |
| **3. Gabarit de page** | `PageHeader` étendu (retour nommé, méta, actions) adopté par l'éditeur et l'Aide ; largeur unique ; « ? » collé au titre (E1-E4, E21). ⚠ L'éditeur a une **barre compacte** au défilement (`ed-compact`), à aligner sur le même gabarit. | Moyen à fort (« où suis-je ? ») | **Moyen** (en-tête de l'éditeur, renommage en place du titre, barre compacte) | **1 journée** |
| **4. Barre de filtres** | `BarreFiltres`, `ChampRecherche`, `.pl-seg`, `.pl-toggle` ; liste, arbre, chronogramme, Supervision, fenêtre de création, Réglages (E5-E9, E11). Garder la mémoire des filtres par navigateur (`CLE_AFFICHAGE`) et le filtre de cellule de l'avis n°56. | Moyen | **Moyen** (filtres mémorisés, clavier, 6 écrans) | **1 à 1,5 journée** |
| **5. Mobile et alertes** | Éditeur à 390 px sans défilement horizontal (arbre en 2 lignes, bandeau MELMIL replié) ; un composant `Alerte` à 3 niveaux (information · à faire · panne) (E24-E26). | Faible à moyen | Faible | **½ à 1 journée** |
| **6. Ménage CSS et référence** | Fusion des classes (§3.5), suppression des copies, jetons de taille, page `SOCLE_UI`. | Invisible pour l'utilisateur, mais **empêche la dérive** de revenir | Faible si fait en dernier | **½ journée** |
| **7. Autres apps** | Appliquer §3.6 **à chaque passage** dans une app (pas de grand chantier). | Durable | Faible | au fil de l'eau |

**Ordre conseillé** : 1 → 2 (faisables pendant DELATTRE 26, à un moment où les scénarios sont en pause) → 3 → 4 (de préférence après l'exercice, ou sur une fenêtre calme) → 5 → 6. Chaque étape : test en local (compilation, `docker run`, `/api/sante` 200, parcours rejoué), captures avant/après, notes de version.

---

## 5. Décisions à soumettre à l'utilisateur

1. **Filtres : segmenté en casse normale (« Tous 59 | Brouillon 5 | … »), ou puces en CAPITALES (« TOUS 59 ») ?**
   → **Recommandé : segmenté en casse normale**, avec l'actif en crème **pâle**. C'est plus lisible (REF-17), le crème plein reste à l'action principale (règle 6), et c'est déjà le style de l'éditeur.
2. **Publications : « Publiée / Non partie », ou « Publié / Erreur » ?**
   → **Recommandé : « Publiée / Non partie »** (féminin de « publication », mot fixé par l'avis n°76, conséquence pour les joueurs plutôt que cause technique).
3. **Une publication qui attend son heure dans un scénario lancé : « Programmée », ou garder « Brouillon » ?**
   → **Recommandé : « Programmée »** (vrai, et cohérent avec « programmées / en direct » du lexique).
4. **Sur-titre de page : le retirer des pages de rubrique et mettre « ← Scénarios » sur l'éditeur, ou garder des sur-titres harmonisés ?**
   → **Recommandé : retirer, avec un retour nommé** (le menu et le titre disent déjà où l'on est ; un seul mécanisme de retour, REF-22).
5. **Largeur : une seule largeur pour toutes les pages, ou un éditeur plus large (environ 1440 px) dont l'en-tête serait aligné sur la même grille ?**
   → **Recommandé : une seule largeur** (le bord gauche ne bouge plus). On ne passe à un éditeur large que si les animateurs manquent de place dans l'arbre.
6. **Calendrier : étapes 1 et 2 pendant DELATTRE 26, étapes 3 et 4 après l'exercice ?**
   → **Recommandé : oui**. Les mots et les étiquettes posent peu de risque et apportent beaucoup ; l'en-tête et les filtres touchent des gestes que les animateurs font en direct.

### 5.1 ✅ Décisions de l'utilisateur (2026-10-07, après la maquette) — « en gros c'est tout proposé »
1. Filtres : **segmenté, casse normale** (actif en crème pâle).
2. Publications : **Publiée / Non partie**.
3. Publication qui attend son heure dans un scénario lancé : **Programmée** (dit « programmé » par l'utilisateur ; accordé au féminin de « publication »).
4. **Retour « ← Scénarios »**, sur-titres retirés.
5. **Une seule largeur**.
6. **Icône + mot partout** (étiquettes).
7. **Animation** : journal en français, nom de l'app « Animation », chiffres sans zéro ajouté.

Calendrier (point 6 du §5) non tranché explicitement : mise en œuvre en local d'abord, montrée avant tout push.

---

## 6. Sources mobilisées
Doctrine `MEMOIRE.md` : règles 3, 5, 6, 10, 15, 20, 21, 24, 28, 29, 30, 36, 37 ; REF-01 (shadcn : composants possédés, jetons sémantiques), REF-06 (Jakob, Von Restorff, Hick), REF-07 (Refactoring UI : limiter les choix, mettre en valeur en atténuant), REF-13 (contraste 4,5 : 1), REF-14 (Nielsen 4 « cohérence et standards »), REF-17 (capitales), REF-19 (radiogroup, disclosure), REF-21 (titre = menu, vocabulaire contrôlé), REF-22 (lien de retour, un seul mécanisme), REF-23 (mises en page canoniques). Avis antérieurs : n°27, 47, 56, 69, 71, 76.

---

## 7. Relecture de la mise en œuvre (2026-10-07)
Branche `coherence-77` d'app-admin, captures locales c01 à c08. **Les 7 décisions sont conformes** : segmenté en casse normale, actif pâle (c02, c03, c07) · Publiée / Non partie (c01, c03, c06) · Programmée (c03) · « ← Scénarios », plus de sur-titre (c01 à c06) · même bord gauche (126 px, c01 = c03) · icône + mot partout (c02, c03, c06) · journal en français, « 3 / 8 publiées », sans zéro ajouté (c01, c03, c06).
**2 points bloquants avant le push.** (1) **Le titre disparaît à 390 px (c08)**, alors qu'il s'affichait avant (p14). Cause : `PageHeader`, bloc titre en `flex-1` (base 0) dans une ligne qui passe à la ligne ; correction : une base réelle, par exemple `flex-[1_1_18rem]`. Le compteur se coupe mot à mot pour la même raison. C'est une régression, distincte de l'étape 5. (2) `Etiquette.tsx`, `LigneJournal.tsx` et `lib/etats-publication.ts` ne sont **pas suivis par git** : les ajouter au commit, sinon l'image ne se construit pas. À noter aussi : la branche emporte 7 commits absents de `main` (n°76, contrôle de cellule, kit IA) et une modification de `schema.prisma`. C'est à confirmer comme voulu.
**Suite donnée** :
- (1) **corrigé** : `flex-[1_1_18rem]`. Titre mesuré à 390 px : 302 px de large, et le bord est inchangé sur ordinateur.
- (2) les 3 fichiers sont dans le commit.
- Les « 7 commits absents de `main` » viennent du `main` LOCAL, qui était en retard. Face à `origin/main`, il n'y a aucun commit en trop ni aucune modification du schéma.
- « supprime » → « supprimé » : corrigé dans `phraseJournal`.
- ✅ **En production** : `af592fb`, tag `prod-20261007-1704-af592fb`.
- Le journal vide d'un scénario lancé (c04) vient bien des données de démo : elles sont insérées en base, sans ligne de journal.

**Pour un lot suivant** : la date dans le journal quand le jour change (c01 et c06 enchaînent plusieurs jours avec l'heure seule) ; « supprime » → « supprimé » dans la traduction des vieilles lignes (c01) ; vérifier que le journal vide d'un scénario lancé (c04) vient bien des données de démo.
