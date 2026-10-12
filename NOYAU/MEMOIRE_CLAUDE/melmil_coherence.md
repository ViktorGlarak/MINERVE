---
name: melmil-coherence
description: "Résolution cohérence MELMIL.xls vs index_master.html — règles dates, codes doublons corrigés, convention extensions éditoriales, trou narratif 08.02"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 73fcca0d-c040-42d3-9859-fa36df54c216
---

# MELMIL — Résolution cohérence codes & convention extensions (2026-05-28)

Analyse conjointe NOYAU × GUILLAUME. Ces règles s'appliquent à tous les agents produisant des injects pour index_master.html.

## Règle de vérité des dates

> **Les dates dans MELMIL.xls peuvent être fausses si modifiées manuellement.**
> **La date affichée dans index_master.html = vérité animateur = source de foi.**

Le XLS est la vérité des **codes** et des **sujets/contenus**, pas toujours des **dates**.

**Cas documenté :** 07.02.06i (STEP 2) — MELMIL.xls indique 28/05, index_master affiche 27 Mai. Le XLS a été modifié manuellement ; la date index_master est correcte. Ne pas corriger index_master sur la foi du XLS seul.

**Règle de conduite :** en cas de divergence date XLS / index_master → demander confirmation à l'utilisateur avant toute correction.

**Why:** règle validée lors d'une analyse croisée NOYAU × GUILLAUME le 28/05/2026.
**How to apply:** quand une correction de date index_master est envisagée suite à un écart MELMIL.xls, vérifier d'abord si la date XLS n'est pas une modification manuelle erronée.

---

## Règle injects multi-canaux

> Un même inject MELMIL peut se décliner sur N cartes dans index_master (BC1 article + tweet EastWatch).
> Le `num` ANIM_DATA est **identique** — intentionnel.
> La **clé ANIM_DATA** porte le suffixe canal pour les distinguer.
> MELMIL compte 1 inject ; index_master peut afficher N cartes.

**Exemple :** 07.05.07i (Marchuk Level Alpha) → `BCI_Article_CemaBR` + `@EastWatch_marchuk_alpha` — même `num:"07.05.07"`, deux cartes distinctes.

---

## Convention de codage des extensions éditoriales

Les injects hors MELMIL (enrichissement narratif) suivent les suffixes :

| Suffixe | Signification | LO héritée |
|---|---|---|
| `.00` | Tweet d'amorce pré-série | LO de la série |
| `Ai` | Amplification civile organique (blanchiment source) | LO 1 + LO parent |
| `Bi` | Amplification SMS/numérique | LO 1 + LO parent |
| ~~`P-xx`~~ | *Migré 2026-05-29 vers séries 07.07/07.08/07.05* | — |
| ~~`R-x`~~ | *Migré 2026-05-29 vers 08.03/07.01/07.05/08.01.xxAi.Rx* | — |
| `CIVIL-xx` | Témoin civil neutre | LO 3 |
| `TV4-xx` | Succès tactique camp bleu (point de repère) | LO 2/3 |

Ces extensions ne figurent pas dans MELMIL.xls. Elles héritent de la LO de l'inject racine.

---

## ⚠ RÈGLE MASTAURIGE — Synchronisation bidirectionnelle MELMIL ↔ index_master (2026-05-29)

### Codes d'injects immuables

Ne jamais renommer un code inject pour résoudre un problème de placement MELMIL. Utiliser `MELMIL_SUBINJECT_DAYS` à la place.

### Architecture sync (melmil.js)

| Sens | Mécanisme | Clé localStorage |
|---|---|---|
| index_master → MELMIL | `syncDayOverrides()` Sync 2 lit `card-day-KEY` → `applySubInjectPosition()` (sans persistence) | `card-day-KEY` |
| MELMIL → index_master | `saveSubInjectPositions()` écrit `card-day-KEY` → index_master lit à son chargement | `card-day-KEY` |
| Defaults | `buildSubInjectDefaultSplits()` lit `MELMIL_SUBINJECT_DAYS` → `applySubInjectPosition()` | *(aucune)* |

**Clé SUBINJ_KEY (melmil-subinj) = UNIQUEMENT les drags manuels MELMIL.** Les positions auto n'y touchent pas.

**Priorité :** drag MELMIL (SUBINJ_KEY) > date selector index_master (card-day-*) > MELMIL_SUBINJECT_DAYS

### `MELMIL_SUBINJECT_DAYS` — cas de référence

```javascript
"07.01.02Ci": 29,   // TM Vorin D+34, parent 07.01.02i à D+32
"07.05.03Fi": 29,   // BC1 Manifestations J4 D+34, parent 07.05.03i à D+33
```

**How to apply:** si date inject ≠ date parent XLS → `MELMIL_SUBINJECT_DAYS[code] = dayorder` dans melmil_inject_index.js — pas de renommage de code.
**Why:** les codes sont présents dans index_master ANIM_DATA, LO_BY_KEY, rapports — les changer crée des incohérences en cascade.

---

## ⚠ RÈGLE CRITIQUE — Virgule finale dans melmil_inject_index.js (bug 2026-05-29)

> Lors de l'ajout de nouvelles sections dans `MASTAURIGE_INDEX`, la **dernière entrée de chaque bloc** doit se terminer par `],` (virgule) avant le commentaire `//` suivant.
> **Symptôme** : si la virgule manque, JavaScript invalide silencieusement `MASTAURIGE_INDEX` → tous les injects disparaissent de MELMIL, les popups ne s'ouvrent plus.
> **Correction appliquée** : virgule ajoutée après `07.06.02Bi` (ligne 195 du fichier).
> **How to apply** : après tout ajout de bloc dans `melmil_inject_index.js`, vérifier que la dernière `]` du bloc précédent est suivie d'une virgule.

---

## Corrections appliquées dans index_master.html (2026-05-28)

| Élément | Avant | Après | Motif |
|---|---|---|---|
| `@HmunikVoice` 1er tweet (27 Mai) | `num:"07.02.03"` | `num:"07.02.00"` | Collision avec 07.02.03i (forces faibles, 29 Mai) |
| `@TemoignageDAC_tract_neufchateau` (26 Mai) | `num:"07.02.06"` | `num:"07.02.05Ai"` | Collision avec tract_step2 (07.02.06i canonique) |
| `@MarionKessler57_sms` (26 Mai) | `num:"07.02.05"` | `num:"07.02.05Bi"` | Collision avec tract_step1 (07.02.05i canonique) |
| Commentaire HTML BCI Youkachenko | `07.02.01i` | `07.05.01i` | Erreur relique d'ancienne version |
| Commentaire HTML @TemoignageDAC | `07.02.06i` | `07.02.05Ai` | Aligné sur la correction ANIM_DATA |

---

## Trou narratif identifié — Série 08.02 (D+35 CLIMAX, non corrigé)

Les 4 injects de redditions/captures MER sont absents d'index_master. À créer en priorité :

| Inject | Date | Sujet | Priorité |
|---|---|---|---|
| **08.02.03i** | 31 Mai | Reddition troupes niveau HSARREBOURG | **HAUTE** |
| **08.02.02i** | 28 Mai | Capture soldats MER (= 104 hommes DJOBOVIC/HNANCY) | **HAUTE** |
| 08.02.01i | 31 Mai | Reddition soldats MER (général) | Importante |
| 08.02.04i | 31 Mai | Capture troupes HSarre-union | Moyenne |

## Mapping 08.03 → éléments existants (mis à jour 2026-05-29)

| Inject MELMIL | Couvert par | Code MASTAURIGE |
|---|---|---|
| 08.03.01i (Discours SG OTAN) | `HEX_Article_Rutte` (num 07.02.08) | — |
| 08.03.02i (Discours SG ONU) | `HEX_Article_Guterres_Statement` + `TV4_Article_Guterres_Statement` | **08.03.02Ai** + **08.03.02Bi** |
| 08.03.03i (Contremesures OTAN) | 5 tweets (@IndependentArnish ×2, @GromovaYelena ×2, @BelovDimitri) | **08.03.03Ai→Ei** |
| 08.03.04i | Draft MELMIL — créer uniquement à la demande | — |

## ⚠ RÈGLE — Inject créé hors MELMIL.xls = ligne GHOST r7 (2026-06-01)

MELMIL est une **synchromatrice** (lignes incidents `ROW_MAP` × colonnes jours). `buildGhostInjects()` (appelée dans `init()`) affiche les injects produits dans MASTAURIGE mais **absents de MELMIL.xls** dans la ligne **r7 « GHOST — Injects hors XLS »**. Trois conditions pour qu'un orphelin apparaisse au bon jour :

1. **Indexation par SOUS-CODE** dans `MASTAURIGE_INDEX` : une clé par sous-inject (`07.04.07Ai`, `07.04.07Bi`, `07.04.07Ci`), **une carte chacune** — JAMAIS plusieurs cartes groupées sous une clé code-parent (`07.04.07i`). Une clé sans lettre (`…ZZi`) fait échouer `getParentInjectCode()` (retourne null) → l'inject part en CASE 2 et **seule la 1re carte s'affiche**.
2. **Jour éditorial obligatoire** : ajouter le **code parent** (`07.04.07i`) à `MELMIL_EDITORIAL_DAYS = { … : dayorder }` (32 = 01 Jun). Sans cela, CASE 2 fait `return` (jour null) → l'inject **disparaît** ; CASE 1.5 tombe sur l'*overflow* → invisible sous le jour attendu.
3. **Promotion auto** : dès que l'incident est saisi dans MELMIL.xls, CASE 1 prend le relais et la carte r7 disparaît — rien d'autre à faire.

**Ancrage volontaire des arcs** : un arc multi-jours (ex. `07.07.03i` D+28→D+38) est **délibérément ancré à son jour de lancement** dans r7 et y regroupe tous ses sous-injects (même ceux datés plus tard). Ce n'est PAS un bug — c'est pourquoi un sous-inject daté 01 Jun (`07.07.03Di`) apparaît sous le 28 Mai dans MELMIL alors qu'il est au 01 Jun dans index_master.

**Cas documenté (01/06)** : 12 cartes au 01 Jun dans index_master vs ~4 dans MELMIL. Causes : (a) séries entières absentes du XLS (07.04.07i corruption, 07.07.xx, 07.08.xx) ; (b) arcs ancrés au départ ; (c) relances P-xx/R-x sans code. Corrigé pour 07.04.07i (ré-indexé Ai/Bi/Ci + `MELMIL_EDITORIAL_DAYS["07.04.07i"]=32` → ghost r7 au 01 Jun).

**Why:** j'avais créé l'inject corruption sans jour éditorial ni indexation par sous-code → il ne s'affichait nulle part dans MELMIL.
**How to apply:** tout inject créé dans MASTAURIGE et pas encore dans MELMIL.xls → 3 clés sous-code dans `MASTAURIGE_INDEX` + 1 entrée `MELMIL_EDITORIAL_DAYS[code parent]`.

### Répartition d'un arc orphelin sur PLUSIEURS jours (2026-06-01)

Avant : `buildGhostInjects` CASE 1.5 ancrait **tout** un arc orphelin au jour de lancement du parent (`MELMIL_EDITORIAL_DAYS`) → un sous-inject daté 01 Jun apparaissait au 28 Mai. CASE 1.5 a été **enrichie** : le jour est désormais calculé **par sous-inject** (`localStorage card-day-*` > `MELMIL_SUBINJECT_DAYS[sous-inject]` > `MELMIL_EDITORIAL_DAYS[parent]`), et un fantôme r7 est créé **par couple (parent + jour)** (recherche `orphanCell.querySelector` au lieu de `document.querySelector`).

Donc pour aligner MELMIL sur index_master jour par jour :
- **Sous-inject orphelin** (parent absent du XLS, séries sans `ROW_MAP` comme 07.07/07.08) → `MELMIL_SUBINJECT_DAYS[sous-inject] = dayorder` (consommé par CASE 1.5).
- **Sous-inject à parent présent au XLS** mais publié un autre jour (ex. 08.03.03Ci, 08.01.01Ai.R2) → même `MELMIL_SUBINJECT_DAYS[...]`, consommé par `buildSubInjectDefaultSplits` (nécessite que l'incident ait une ligne `ROW_MAP`).

**Cas 01/06 résolu** : 12 cartes index_master ↔ 12 items MELMIL au 01 Jun. Les 5 qui manquaient (07.07.03Ci/Di, 07.08.01Di, 08.03.03Ci, 08.01.01Ai.R2) recodés à `=32`. Les relances/courriers ont bien un code réel (`08.01.01Ai.R2`, `07.08.02Ai`) malgré des commentaires HTML obsolètes « R3-2 / P-10 ».

---

## ✅ NORMALISATION 100% des codes d'injects → XX.YY.ZZ<Lettre>i (2026-06-01)

> **Règle absolue désormais :** tout *inject* (carte index_master : tweet, article, facture, courrier, tract) porte un code **sous-inject** `XX.YY.ZZ<Lettre>i` (ex. `07.01.03Ai`). Le code **sans lettre** `XX.YY.ZZi` est réservé aux *incidents* (melmil.xls). Un code famille (`07.02`) ou illisible (`07.02 / TV4`, `CIVIL-01`) est **interdit**.

**Pourquoi c'était un bug :** un inject codé au niveau incident (`07.01.03`) était traité par MELMIL comme **l'incident lui-même** → changer sa date déplaçait la carte incident (conflit XLS) au lieu de l'inject. D'où « 07.01.03 ne se met pas à jour ». Corrigé en le rendant sous-inject `07.01.03Ai`.

**Le num d'une carte vit à 2 endroits cohérents :** `ANIM_DATA` (index_master, clés `@handle` ET clés article — 122 entrées = master) **et** `tweets_data.js` (`num` des tweets). `LO_BY_KEY` est keyé par **clé carte** (code en commentaire) → non concerné par un renommage de num.

**Source autoritaire du bon code = le pont curé `MASTAURIGE_INDEX`** (maintenu par GUILLAUME) : 46/57 cartes mal formées y avaient déjà le bon code → on aligne le num dessus (pas de devinage). Les 47 déterministes (46 curés + `07.02.00→07.02.00Ai`) renommés par script ; les 10 éditoriaux (arc Pallesson `07.02.09Ai-Ei`, `07.01.07Ai`, `07.02.10Ai`, `07.03.05Ai`, `07.04.06Ai`, `08.01.07Ai`) sur décision utilisateur — ce sont de **nouveaux incidents hors-XLS** (apparaissent en r7 jusqu'à ajout au XLS). Articles **statiques** (Pallesson) ajoutés au pont curé + `MELMIL_SUBINJECT_DAYS` (MELMIL ne lit pas index_master).

**Backups :** `index_master_BACKUP_20260601b.html`, `tweets_data_BACKUP_20260601b.js`, `index_master_BACKUP_20260601c_precomments.html`. **How to apply (futur) :** tout nouvel inject créé doit recevoir un code `XX.YY.ZZ<Lettre>i` ; jamais un code incident nu ni famille.

**Commentaires HTML nettoyés (2026-06-01) :** les 77 commentaires d'index_master ont été recodés sur les vrais codes (69 via clé de carte / handle+heure) ou débarrassés de leur ancien code P-xx/R-x non résolvable (8). Plus aucun marqueur legacy (`P-xx`, `Rx-y`, `CIVIL-xx`, `XX.YY / TV4`) ne subsiste. La nomenclature P-xx/R-x est définitivement morte partout (data + commentaires).

---

## ⚙ Modèle de dates incident vs inject + glisser bidirectionnel MELMIL (2026-06-01)

> **Modèle validé :** la date d'un **incident** vit uniquement dans **melmil.html + melmil.xls**. La date d'un **inject** vit dans **index_master.html + melmil.html** (canal de sync = `card-day-{clé}` en localStorage, partagée file://).

**Deux opérations de glisser dans MELMIL :**
1. **Glisser une CARD d'incident** → seuls **les injects CONTENUS dans cette card** la suivent (comportement DOM naturel : `cell.appendChild(card)` déplace la card + ses enfants). Les injects du **même incident splittés sur d'autres dates** (clones ailleurs) **restent** à leur place. `savePositions()` (cascade par incident) est ensuite **corrigé** par `saveSubInjectPositions()` qui réécrit `card-day` selon la position DOM RÉELLE de chaque sous-inject → les splits gardent leur date.
2. **Glisser un SEUL inject** (la ligne sous-inject) → SPLIT : `handleSubInjectDrop` branche SPLIT clone la card, seul cet inject change de `card-day`.

**⚠ NE PAS réunir tous les sous-injects d'un incident au drop** *(corrigé 2026-06-02)* : une fonction `reuniteIncidentSubInjects` rapatriait TOUS les sous-injects de l'incident dans la card déplacée → déplacer n'importe quelle card ramenait 100% des injects (faux). **Supprimée.** Le comportement voulu = chaque card déplace uniquement son propre contenu ; les autres splits restent indépendants.

**⚠ Sync NON live + cache :** le sens MELMIL→index_master exige de **recharger index_master (Ctrl+F5)** après le glisser (il relit `card-day` au chargement). Et melmil.html charge ses scripts avec `?v=AAAAMMJJx` — **bumper ce suffixe à chaque édition de melmil.js/melmil_inject_index.js** sinon le navigateur sert l'ancienne version en cache (actuel : `v=20260601f`).

---

## ⚙ PONT AUTOMATIQUE index_master → MELMIL + ligne matrice dynamique (2026-06-01)

> **Modèle validé par l'utilisateur :** *incident* = numéro venant de `melmil.xls` (carte `XX.YY.ZZi`). *Inject* = produit créé dans index_master, rattaché à un incident (article TV4/TM, facture, courrier, tweet), codé `XX.YY.ZZAi`. On travaille parfois **en sens inverse** : créer l'inject (et son incident) AVANT que `melmil.xls` ne contienne le numéro. MELMIL doit donc afficher **plus** d'incidents/injects que le XLS, et **promouvoir sans conflit** dès que le XLS est importé.

**Pont auto (`buildAutoBridge()` dans melmil.js, appelé en 1er dans `init()`) :** MELMIL lit désormais directement les injects (`MASTAURIGE_TWEETS` via `<script src="../tweets_data.js">` ajouté à melmil.html, + `localStorage` `mastaurige-creations.tweets` et `mastaurige-articles.articles`) et fabrique **à la volée** les entrées `MASTAURIGE_INDEX` + `MELMIL_SUBINJECT_DAYS` manquantes (clé = id de la carte, jour = `dayorder` de l'inject). **Plus besoin d'éditer `melmil_inject_index.js` à la main.** Le pont curé garde la priorité (`knownKeys` par clé → aucun doublon ; suppressions `mastaurige-edits` respectées).
- `bridgeCode()` normalise : `07.10.01Ai`→`07.10.01Ai`, `07.04.03`→`07.04.03i`. **Un inject doit avoir un code 3-niveaux `XX.YY.ZZ`** pour être ponté ; les codes famille (`07.02`) ou legacy (`CIVIL-01`) ne le sont pas (6 tweets bakés concernés au 01/06 — data hygiene).

**Ligne matrice dynamique (`ensureDynRow()`) :** quand `buildInjects` rencontre un incident XLS dont la famille `XX.YY` n'a pas de ligne fixe (`ROW_MAP`), il **crée une nouvelle ligne** `rdyn{n}` (label « Incident importé / hors plan initial », classe `.cdyn`) insérée avant la ligne GHOST r7, avec les cellules `cell-rdyn{n}-d31..d40` + overflow. → promotion d'une série totalement neuve (ex. `07.10`) hors du holding r7.

**Cycle de vie d'un inject créé en sens inverse :**
1. Créé dans index_master avec code `07.10.01Ai` + jour → **apparaît seul** en r7 (fantôme `07.10.01i` « hors XLS »).
2. `07.10.01i` ajouté à `melmil.xls` → au rechargement, `buildInjects` crée la vraie carte (ligne dynamique si famille neuve), `buildGhostInjects` CASE 1 y rattache l'inject → **le fantôme r7 disparaît, sans doublon** (le changement de timestamp XLS purge aussi les positions sauvegardées).

**Bug date éditée d'un tweet baké (corrigé 02/06) :** le créateur enregistre la date modifiée d'un **tweet** dans `mastaurige-edits[id].dayorder` (via `TW.update`) et **supprime** `card-day`. Le pont auto appliquait les edits pour le `num` mais PAS pour le `dayorder` → il gardait le dayorder baké (ex. `07.01.03Ai` baké « attente ») et l'inject restait collé au jour de son incident parent XLS (04 Jun) au lieu du jour choisi (02 Jun). Corrigé : `buildAutoBridge` calcule le **dayorder effectif = `mastaurige-edits[id].dayorder` › baked** (helper `effDay`) avant de poser `MELMIL_SUBINJECT_DAYS`. Vaut pour TOUT tweet dont la date a été changée via « Modifier ».

**Alignement du JOUR automatique (02/06) :** `buildAutoBridge` pose aussi le jour de **chaque** inject (curé OU auto) à partir de son `dayorder` index_master → `MELMIL_SUBINJECT_DAYS[code]` pour un sous-inject (Ai/Bi…), `MELMIL_EDITORIAL_DAYS[code]` pour un code niveau incident. Sans écraser une valeur déjà posée (priorité : entrée manuelle > `card-day-*` drag > `dayorder`). **Conséquence : un sous-inject publié un autre jour que son incident parent tombe au bon jour sans entrée manuelle** (ex. `08.03.03Di` daté 02 Jun alors que `08.03.03i` est au 30 Mai au XLS). Les entrées manuelles `MELMIL_SUBINJECT_DAYS` ne servent donc plus qu'à **forcer** un jour différent du `dayorder`.

**Why:** le créateur d'index_master n'alimentait pas `MASTAURIGE_INDEX`, et les jours des sous-injects n'étaient pas alignés sur index_master → injects invisibles ou placés au mauvais jour dans MELMIL. **How to apply:** rien — automatique ; il suffit de donner à l'inject un code `XX.YY.ZZAi` + un jour dans index_master.

---

## Migration P-xx / R-x complète (2026-05-29)

Tous les anciens codes P-xx et R-x ont été renommés vers le format canonique :

| Nouvelle série | Description | Incidents |
|---|---|---|
| **07.07** | Architecture déni Storm-1516 (EastWatch blanchiment, TemoignageDAC, VoixDACia, ZURB) | 07.07.01i à 07.07.04i |
| **07.08** | Piège narratif rétroactif (graines, déni, révélation D+38) | 07.08.01i à 07.08.03i |
| **07.05** (extensions) | Bascule politique RB + signaux D+38/D+39 (absorbés dans séquence existante) | .01Ci/Di, .05Bi, .09Bi, .10Bi→Gi |
| **08.03** | HOST NATION : OTAN/ONU (Guterres + contremesures OTAN) | 08.03.02i + 08.03.03i |
| **07.01** (extensions) | Renforcements dénigrement post-HSARREBOURG | 07.01.05Ai, 07.01.06Ai |
| **08.01** (format .Rx) | Relances formelles courriers | 08.01.01Ai.R1, 08.01.01Ai.R2 |
