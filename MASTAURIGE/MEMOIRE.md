# MÉMOIRE — MASTAURIGE

> 🗂️ **Vue méta** (notes atomiques qui *lient* cette mémoire, ne la dupliquent pas) : [vault/projects/MASTAURIGE.md](../vault/projects/MASTAURIGE.md) + [vault/INDEX.md](../vault/INDEX.md). **Ce fichier (outillage) + le registre avatars (`avatars.js`) restent la source de vérité.** *(Vault créé le 2026-06-15 — couche méta, ne modifie pas l'outillage.)*
> ⚙️ **Camps** : le registre des avatars (`avatars.js` / `bios.js`) fait foi, **miroir** dans `vault/entities/` ; `vault/_tools/valider.py` **bloque** toute contradiction de camp entre `bios.js` et les notes entité.

## Création
Agent créé le **2026-05-24** pour la génération de contenus RS fictifs dans les exercices de type AURIGE (entraînement PC niveau brigade). MASTAURIGE est INDÉPENDANT de Mastorion — pas de lien avec la plateforme fictive ORION 26.

---

## Distribution par exercice

| Exercice | Mode de distribution | Statut |
|---|---|---|
| AURIGE 2BB | HTML statique ZIP offline (`WEB/index_master.html`) | Actif |
| Exercices AURIGE futurs | HTML statique ZIP offline (même format) | Extensible |

## Architecture dossiers AURIGE 2BB — Chemins de production

> Chemin racine exercice : `D:\CECPC\PRODUCTION\EXER\AURIGE 2BB\`

**Fichier maître animateur :** `D:\CECPC\PRODUCTION\EXER\AURIGE 2BB\00_Boites à outils\MASTAURIGE\WEB\index_master.html`

**Trombinoscope :** `D:\CECPC\PRODUCTION\EXER\AURIGE 2BB\00_Boites à outils\MASTAURIGE\WEB\Trombinoscope\ACTEURS_A3_AURIGE2BB.html` *(déplacé le 2026-05-28 depuis la racine WEB\)*

**Productions MASTAURIGE par jour :**
```
03_Productions\
├── D+31_26_MAI\WEB_20260526_1338\WEB\
├── D+32_27_MAI\MASTAURIGE_D32_27_MAI\WEB\
├── D+33_28_MAI\MASTAURIGE_D+33_28_MAI\WEB\
├── D+34_29_MAI\MASTAURIGE_D+34_29_MAI\WEB\
├── D+35_30_MAI\MASTAURIGE_D+35_30_MAI\WEB\
├── D+36_31_MAI\MASTAURIGE_D+36_31_MAI\WEB\
├── D+37_01_JUIN\MASTAURIGE_D+37_01_JUIN\WEB\
├── D+38_02_JUIN\MASTAURIGE_D+38_02_JUIN\WEB\
├── D+39_03_JUIN\MASTAURIGE_D+39_03_JUIN\WEB\
└── D+40_04_JUIN\MASTAURIGE_D+40_04_JUIN\WEB\
```

**Séries 07.05 à 07.10** : Dossiers de production vidéo/Premiere Pro, localisés dans `03_Productions\`. Non utilisés par MASTAURIGE — référence uniquement.

⚠ **Doublon D+31 :** deux dossiers coexistent (`D+31_26_MAI` underscore et `D+31_26-MAI` tiret) — à nettoyer manuellement.

---

## ⚠ RÈGLE OBLIGATOIRE — Consultation MASTAURIGE avant toute création d'avatar

> **Tout nouvel avatar RS fictif pour un exercice Mercure doit être déclaré ici AVANT production.**
> S'applique à TOUS les agents : NOYAU, GUILLAUME, EXPERT_INFLUENCE, ANALYSTE, SCÉNARISTE, et tout futur agent.
> Processus : (1) vérifier si l'avatar existe dans CASW ORION 26 → (2) si non, créer une fiche dans `avatars_casw_aurige2bb.md` → (3) mettre à jour ce registre.
> Créer sans consulter = doublon possible, contradiction de profil, perte de traçabilité.

---

## Avatars utilisés — AURIGE 2BB (registre au 26 mai 2026)

> ## ⭐ REGISTRE CANONIQUE DES PERSONAS — SOURCE DE VÉRITÉ UNIQUE *(décidé 2026-06-01)*
> **Ce registre (MASTAURIGE) est l'UNIQUE propriétaire de l'identité d'un avatar/persona : handle, nom affiché, image/initiales, et surtout le CAMP (🔴 rouge / 🔵 bleu / ⚪ neutre).** Les autres IA (Analystes pays, GUILLAUME, MINAUTORE, EXPERT_INFLUENCE…) **citent** ce registre — elles ne redéfinissent JAMAIS le camp d'un persona ailleurs.
> - **Qui décide le camp ?** L'Analyste du pays reste l'**autorité de décision** (expertise politique) ; mais le camp n'est **stocké qu'ici**, et l'Analyste apporte la *doctrine* (LO, éléments de langage, emploi) en renvoyant à ce registre.
> - **Miroir machine** = `…\MASTAURIGE\WEB\avatars.js` (handle → camp), lu par le créateur de tweets. Toute correction de camp se fait **ici + dans avatars.js**, puis se propage.
> - **Garde-fou automatique** : `OUTILS\verifier_mastaurige.py` (CONTROLE G) alerte si un tweet porte un camp en **contradiction dure** (rouge↔bleu) avec son avatar. *(Un avatar « neutre » qui penche — ex. @EastWatch_Intl en façade de blanchiment — n'est PAS une divergence.)*
> - **Pourquoi cette règle** : la dérive Svetlana Tikhanov (camp recopié « bleu » dans 7 fichiers, faux) — voir `melmil_coherence` mémoire. Désormais : un seul endroit fait foi.

> ⚠ **Lecture de la colonne « Injects »** : elle peut contenir deux types de références —
> - des **codes d'injects canoniques** (`07.05.03Ai`, `08.02.02Bi`…) = cartes réelles dans index_master.html ;
> - des **identifiants d'arcs/propositions `P-xx`** (P-01 à P-28, ex : P-05c, P-27) = convention éditoriale Storm-1516 / bascule politique (cf. `GUILLAUME\MEMOIRE.md` § « Convention de codage des extensions éditoriales » + `PROPOSITIONS_ILI_DOCTRINERUSSE.md`).
>
> Les `P-xx` **ne sont pas des codes périmés à renommer** : ils désignent des arcs narratifs, pas des injects précis. Seuls les arcs devenus séries officielles sont mappés 1:1 (P.01→07.07, P.02→07.08, P.03→07.05, P-25/26→08.03 — voir tableau de migration plus bas). Pour la correspondance fine P-xx → carte, se référer à GUILLAUME.

### Avatars issus de la base CASW ORION 26
→ Fiches complètes dans `CASW/avatars_casw_orion26.md`
→ Avatars recommandés par camp dans `CASW/PROCESS_TWEETS_AURIGE.md` section 7

| Handle | Nom | ID CASW | Camp | Injects AURIGE 2BB |
|---|---|---|---|---|
| @HmunikVoice | Pavlus Juri Gautoreif | 3727 | 🔴 Rouge | 07.01, 07.02, P-02, P-05c, P-07a, P-11, P-15, P-17, P-18 |
| @NOVUSORDOMUNDI | NOVUS ORDO MUNDI | 3691 | 🔴 Rouge | 07.02 |
| @ArnlandLovePeace | Clémence Gavaloff | 1392 | 🔴 Rouge | 07.05 |
| @MaiaKovalenko | Maïa Sokhaguvka | 3726 | 🔴 Rouge | 07.04 |
| @BelovDimitri | Dimitri Belov | 1851 | 🔵 Bleu | 07.05, **07.05.04Di** |
| @GromovaYelena | Yelena Gromova | 1845 | 🔵 Bleu | 07.01 |
| @IndependentArnish | Arnish Independent | 3510 | 🔵 Bleu | 07.02 |
| @BelikovaMarina | Marina Belikova | 1825 | 🔵 Bleu | **07.05.04Ei** — 1ère apparition AURIGE 2BB (2026-05-30) — pigiste DAC 24 ans, réaction civile au sommet Olamao-Youkachenko |

### Avatars nouveaux — spécifiques AURIGE 2BB
→ Fiches complètes dans `CASW/avatars_casw_aurige2bb.md`
→ Créés le 26 mai 2026 **sans consultation préalable** (corrigé rétroactivement)

| Handle | Nom affiché | Initiales | Camp | Rôle | Injects |
|---|---|---|---|---|---|
| @EastWatch_Intl | EastWatch International | EW | 🟡 Pseudo-neutre | Relais analytique — blanchiment progressif MER | P-03, P-04, P-08, P-09, P-12, P-20 |
| @CorrespondantEst | Correspondant Est | CE | 🟡 Pseudo-neutre | Correspondant terrain — couche 2 piège rétroactif | P-14, P-16 |
| @TemoignageDAC | Témoignage DAC | TD | 🔴 Rouge (camouflé civil) | Couche 1 flou architecture déni Storm-1516 | P-05a |
| @VoixDACia | Voix DACia | VD | 🔴 Rouge (camouflé civil) | Voix anti-guerre / anti-mobilisation DAC | P-06 |
| @clambroise55 | Claire Ambroise | CA | ⚪ Témoin civil neutre | Témoignage civil D+33 — blocage N4 Void-Vacon (impact conflit sur population) | CIVIL-01 |
| @J_Vasseur | Jérôme Vasseur | JV | 🔴 Rouge (camouflé civil) | **Vétéran DAC amputé** — grief corruption chefs DAC/polonais : « pendant que je m'achète de nouvelles jambes, les chefs s'achètent des voitures et des montres ». Levier LO5 (rupture alliance). Créé **2026-06-02**, sans portrait (initiales JV). Déclaré `avatars.js` + trombinoscope p.1 | 07.04.07Ci |

### Avatar media social — BC1 Ruthnia Bella (ajouté 2026-05-28)

| Handle | Nom affiché | Camp | Avatar | Rôle | Injects |
|---|---|---|---|---|---|
| @BC1_News | BC1 Ruthnia Bella | 🔴 Rouge | Initiales "BC1" — background `#12125A` (navy BC1), texte blanc, `font-size: 0.6em`, `font-weight: 900` | Compte social officiel de BC1 — dépêches et témoignages en temps réel | 07.05.03i (Ci, Di) |

> Pas de photo portrait — avatar stylisé avec la charte graphique BC1 (navy + blanc). Aucun fichier image à créer.

### Avatars avec photo portrait réelle — spécifiques AURIGE 2BB
Créés le 27 mai 2026 à partir de portraits Firefly générés.

| Handle | Nom affiché | Camp | Photo portrait | Rôle | Injects |
|---|---|---|---|---|---|
| @S_Tikhanov | Svetlana Tikhanov | 🔴 **Rouge — pro-MER** *(corrigé 2026-06-01, était à tort bleu)* | `avatars tweet/Svetlana Tikhanov - Nouvelle pahonie - photo avatar.png` | Dirigeante **Nouvelle Pahonie** — opposition RB **pro-guerre / pro-Mercure** : soutient la guerre de MER contre la DR, opposée à l'appel à la paix de Youkachenko (= capitulation), alliée de **Saniki (Bison Libre)**. ⚠ PAS bleue, PAS pro-OTAN. Fiche source : `ANALYSTE\BOTHNIA\MEMOIRE.md` | **07.05.03Ai**, **07.05.04Ci** |
| @A_Saniki | Andrei Saniki | 🔴 Rouge (pro-MER, bi-national) | `avatars tweet/Andrei Saniki_bison_libre - photo avatar.png` | Soutien MER en DR — levier LO 5 | P-28, **07.05.03Bi** |

> **Dossier avatars photo :** `D:\CECPC\PRODUCTION\EXER\AURIGE 2BB\00_Boites à outils\MASTAURIGE\WEB\images\avatars tweet\`

---

## Hashtags actifs — AURIGE 2BB

| Hashtag | Camp | Thème |
|---|---|---|
| #NATOInvaders | Rouge | Convois OTAN Lorraine |
| #FuckNato | Rouge | Anti-OTAN radical |
| #ALERTE | Rouge | N.O.M — événement urgent |
| #NATOBetrayDAC | Rouge | Trahison OTAN sur troupes DAC |
| #NATOIllegitimate | Rouge | Délégitimation juridique OTAN |
| #StopWar | Rouge | Antiwar / voix civiles |
| #NonALaGuerre | Rouge | Anti-mobilisation @VoixDACia |
| #ContraOffensive | Rouge | Contre-offensive MER D+38 |
| #LePiège | Rouge | Révélation narrative piège rétroactif |
| #StratégieGagnante | Rouge | Supériorité stratégique MER |
| #TémoignagesDAC | Rouge | Architecture déni couche 3 |
| #CrimesDeGuerre | Rouge | Amplification accusations 2BB |
| #HSARREBOURG | Gris/tous | Ville événement clé D+35 |
| #HSARREGUEMINES | Gris/tous | Axe contre-offensive D+38 |
| #ZURB | Gris/tous | Zone urbaine résidentielle |
| #EastWatch | Gris/neutre | Marque @EastWatch_Intl |
| #FinOffensive | Gris/neutre | Fin offensive US DIV D+36 |
| #StrongerTogether | Bleu | Soutien OTAN |
| #StandWithArnland | Bleu | Solidarité Dacie Romanie |
| #StandWithDaciaRomania | Bleu | Solidarité DAC (variante) |
| #NATOForFreedom | Bleu | Pro-OTAN @BelovDimitri |
| #Lorraine | Gris/tous | Ancrage géographique |
| #Sarrebourg | Gris/tous | Ville événement |

---

## ⚠ Point ouvert — badges camp dans index_master.html

La règle du 2026-05-25 stipule : pas de badge camp visible sur les cartes tweet (les stagiaires doivent classifier eux-mêmes).
En pratique, tous les tweets de index_master.html ont `<div class="camp-badge rouge/bleu">` visible.
**Hypothèse validée :** index_master.html est l'outil animateur — badge acceptable pour le tri. Ne pas reproduire dans une éventuelle vue stagiaire.
**À confirmer par l'utilisateur.**

---

## Lignes Opératoires — Référence obligatoire pour la production MASTAURIGE

> **Source :** `D:\CECPC\DOC REF\CECPC\20260421_GLM26_Matrice ILI-FORAD.pptx`

Chaque tweet card produit par MASTAURIGE doit pouvoir être rattaché à une LO. La LO est indiquée dans la description ANIM_DATA de l'inject (champ `desc` dans index_master.html).

### LO — mémo production tweet

| LO | Ce que le tweet doit faire percevoir | Handles principaux AURIGE 2BB |
|---|---|---|
| **LO 1** | Tromper, fictionnaliser, saturer cognitivement | @TemoignageDAC (couche 1 flou), @HmunikVoice (amplification), @EastWatch_Intl (blanchiment) |
| **LO 2** | MER fort et déterminé · OTAN fragile et hésitant | @HmunikVoice (valorisation MER), @GromovaYelena (fragilité OTAN) |
| **LO 3** | MER résilient · coût humain insupportable pour OTAN | @HmunikVoice (tracts + bilan pertes), @IndependentArnish (insoutenabilité) |
| **LO 4** | MER légitime et accueilli · DAC/ARN État failli | @HmunikVoice (libération), @CorrespondantEst (population hostile DAC) |
| **LO 5** | Alliance fracturée · RB nouveau partenaire MER | @EastWatch_Intl (doute OTAN), @BelovDimitri (08.03.03 contremesures OTAN), signaux RB |

### Règle de marquage tweet
> Quand MASTAURIGE produit un nouveau tweet card, indiquer dans la description (commentaire ou champ `desc` ANIM_DATA) : `LO X — [titre]`. Si tweet réactif (condition), indiquer aussi `Réactif : [condition]`.

---

## Figures politiques et médias AURIGE 2BB — Référence MASTAURIGE

> Mis à jour le 26 mai 2026.

### Chefs d'État mentionnables dans les tweets

| Personnage | Camp | Rôle | Règle tweet |
|---|---|---|---|
| **Olamao** | 🔴 Rouge | Président MER | Citations officielles — ton autoritaire, déni propagandiste |
| **Youkachenko** | 🔴 Rouge | Président RB | Soutien MER — discours anti-OTAN souveraniste |
| **Pallesson** | 🔵 Bleu | **Président DAC** (civil) | Cible discrédit LO 4 — attaque crédibilité politique, jamais rôle militaire |

### Médias à mentionner dans les tweets

| Média | Code | Camp | Comment l'utiliser dans un tweet |
|---|---|---|---|
| Today Mercure | TM | 🔴 | `#TodayMercure` — source officielle MER |
| BC1 | BC1 | 🔴 | `#BC1` — source RB — Youkachenko parle via BC1 |
| HEXAGONE | HEX | 🔵 | Presse française fictive — ex : "d'après HEXAGONE..." dans tweet blanchiment |
| TV4 | TV4 | 🔵 | Média occidental — Pallesson interviewé sur TV4 |
| EastWatch | EW | 🟡 | Blanchiment — @EastWatch_Intl citant des sources HEX ou TV4 |

---

## Commandants FORAD AURIGE 2BB — Référence pour tweets

> **Source données :** ANALYSTE MERCURE (section 1.5.bis) — interroger pour tout détail profil
> **Source primaire :** `D:\CECPC\PRODUCTION\EXER\AURIGE 2BB\MERCURE\G26_PROFIL 41 et 43 MER FORCES.pptx`

MASTAURIGE peut être amené à produire des tweets mentionnant ou attribués à des figures HVI MER. Références de base :

| Commandant | Unité | Traits pour tweet | LO |
|---|---|---|---|
| **MG PRUNIERE** | 41e DIV CHARS | Dirige depuis l'avant, Héros de la Nation 2019, impulsif | LO 2 (valorisation) |
| **MG ZHUKOV** | 43e DIV ABN | Parachutiste aguerri, affaire fiscale (vulnérabilité), conscrits 30% | LO 4 (discrédit), LO 2 (valorisation para) |

**Règle MASTAURIGE :** Avant tout tweet citant un HVI par son nom, vérifier la cohérence profil avec ANALYSTE MERCURE. Un tweet qui contredit le profil psychologique d'un personnage dégrade la crédibilité de la série.

**Référentiel HVI complet GLM26 :** `D:\CECPC\PRODUCTION\CREATION\02 - MERCURE\Portraits\20260303_NP_GLM26_SITCEN_RENS_Profils-HVI-MER.pdf` — ANALYSTE MERCURE détient la référence.

---

## MODULE MELMIL ILI — Architecture et emplacement

> Mis à jour le 2026-05-28. Intégré dans l'arborescence MASTAURIGE.

**Chemin :** `D:\CECPC\PRODUCTION\EXER\AURIGE 2BB\00_Boites à outils\MASTAURIGE\WEB\MELMIL\`

### Fichiers du module

| Fichier | Rôle |
|---|---|
| `MELMIL_ILI_GUILLAUME.html` | Tableau MELMIL visualisation (10 jours D+31→D+40, 6 lignes acteurs) |
| `melmil.css` | Feuille de style dédiée (charte sombre, couleurs séries 07/08, ghost cards) |
| `melmil.js` | Logique : chargement données, ghost cards, drag-and-drop, persistance localStorage |
| `melmil_inject_index.js` | Correspondance codes MELMIL → cards index_master + MELMIL_EDITORIAL_DAYS (ghost) |
| `melmil_data.js` | Auto-généré — NE PAS MODIFIER manuellement |
| `generate_data.py` | **(principal, 2026-05-31)** Lit `MELMIL.xls` (format XML Tableur 2003) **sans Excel** via Python stdlib → génère `melmil_data.js`. Sortie validée identique à l'ancien PS1 (47/47 injects, diff vide). |
| `generate_data.ps1` | *(secours)* Ancienne méthode Excel COM — conservée si Python absent |
| `Actualiser_MELMIL.bat` | Double-clic : essaie Python d'abord, bascule sur le PS1 Excel en secours |
| `MELMIL.xls` | Source de vérité des injects officiels (3 feuilles : Events, Incidents, Injections) |

### Architecture incident / injects MELMIL — RÈGLE CANONIQUE

> **Applicable par TOUS les agents. Mis à jour 2026-05-28.**

| Niveau | Convention de code | Exemple | Rendu dans MELMIL |
|---|---|---|---|
| **Incident** | `XX.YY.ZZi` | `07.05.03i` | Card principale dans le tableau (vient du XLS) |
| **Inject A** | `XX.YY.ZZAi` | `07.05.03Ai` | Ligne compacte cliquable **à l'intérieur** de la card `07.05.03i` |
| **Inject B** | `XX.YY.ZZBi` | `07.05.03Bi` | Idem |
| **Inject C…** | `XX.YY.ZZCi` | `07.05.03Ci` | Idem |

**Règle de lettre :** Vérifier dans `melmil_data.js` que la lettre n'est pas déjà prise pour cet incident dans le XLS. Si A est libre → `Ai`, sinon B, C…

### Format d'affichage unifié — cards MASTAURIGE dans MELMIL

**Toutes** les cards MASTAURIGE liées à un incident s'affichent dans un format unique à l'intérieur de la card incident :

```
[●] identifiant_card    Début du titre de la card...
[●] autre_card          Début du titre...
```

- **Dot** coloré par type (bleu tweet, violet article, orange tract, vert courrier)
- **Identifiant** : clé ANIM_DATA de la card (ex: `@HmunikVoice_sniper`, `BCI_Article_Manifestations`)
- **Titre** : label MASTAURIGE_INDEX tronqué par CSS overflow

**Pour les sous-injects** (`07.05.03Ai`, `07.05.03Bi`) : même format, l'identifiant est le code inject lui-même.

**Comportement clic :**
- Cliquer sur une ligne de card → ouvre le popup MASTAURIGE de l'inject parent
- Cliquer sur une ligne de sous-inject → ouvre le popup MASTAURIGE de ce sous-inject spécifiquement

**Ghost standalone :** Un code MASTAURIGE sans parent dans MELMIL.xls ET sans motif `XX.YY.ZZLi` (lettre finale) peut apparaître en card fantôme indépendante si un dayorder est défini dans `MELMIL_EDITORIAL_DAYS`.

### Ghost actifs (2026-05-28)

| Code | Type | Compte | Statut |
|---|---|---|---|
| `07.05.03Ai` | tweet | @S_Tikhanov_newpahonia | Sous-inject de `07.05.03i` — affiché à l'intérieur |
| `07.05.03Bi` | tweet | @A_Saniki_freebison | Sous-inject de `07.05.03i` — affiché à l'intérieur |

Pour les "promouvoir" en injects officiels : ajouter `07.05.03Ai` et `07.05.03Bi` dans MELMIL.xls, relancer `Actualiser_MELMIL.bat`. Le sous-inject disparaît et une card indépendante prend le relais.

### Sync localStorage index_master ↔ MELMIL

Quand l'animateur déplace une card dans `index_master.html` vers un autre jour via le sélecteur de jour, MELMIL relit cette position au chargement via `syncDayOverrides()` (lecture des clés `card-day-*` en localStorage). Les positions de drag MELMIL ont toujours la priorité sur le localStorage index_master.

### Architecture data-driven

```
MELMIL.xls  →  [Actualiser_MELMIL.bat]  →  generate_data.ps1  →  melmil_data.js
                                                                         ↓
                                                        MELMIL_ILI_GUILLAUME.html  ←  melmil.js
```
Le fichier `melmil_data.js` est la **seule interface** entre le XLS et le HTML. Après chaque mise à jour du XLS, relancer le .bat pour régénérer ce fichier.

### Colonnes "À PLACER" (overflow)

Les injects sans date dans le XLS (`"date":""`) sont placés automatiquement dans la colonne **"À PLACER"** (fond sombre, bordure pointillée) de chaque ligne acteur. Ils peuvent ensuite être **glissés-déposés** vers le bon jour. Les positions sont sauvegardées en `localStorage` (clé `melmil-gg-positions`).

### Tables de correspondance melmil.js

| Constante | Rôle |
|---|---|
| `ROW_MAP` | Code incident (`07.01`, `08.02`…) → ID ligne acteur (`r1`…`r6`) |
| `CLASS_MAP` | Code incident → classe couleur CSS (`c01`…`c83`) |
| `DAY_MAP` | Date ISO (`2026-05-26`…) → ID colonne jour (`d31`…`d40`) |
| `BADGE_MAP` | Statut (`Ended`, `Started`, `Draft`, `Validated`) → badge affiché |

### Intégration dans index_master.html

Deux boutons animateur dans la barre de navigation, entre la barre de recherche et le badge ANIMATEUR :

| Bouton | Classe CSS | Couleur | Cible | onclick |
|---|---|---|---|---|
| ⚡ MELMIL ILI | `.btn-melmil` | Gold `#FFD700` | `MELMIL/MELMIL_ILI_GUILLAUME.html` | `saveMasterState()` |
| 🗂 TROMBINOSCOPE | `.btn-acteurs` | Navy `#2c3e50` | `Trombinoscope/ACTEURS_A3_AURIGE2BB.html` | `saveMasterState()` |

Les deux boutons sont **supprimés automatiquement** dans tous les exports stagiaires (ajoutés à la liste de nettoyage des 3 fonctions d'export — classes `.btn-melmil` et `.btn-acteurs`).

**Règle :** Tout nouveau bouton de navigation ajouté à l'en-tête de `index_master.html` doit : (1) appeler `saveMasterState()` en `onclick`, (2) être ajouté aux **3 listes de nettoyage** des fonctions `generateIndexMedia`, `generateIndexRzo`, `generateComplet`. *(NB : `generateSplit` n'a pas de liste propre — il appelle `generateIndexMedia` + `generateIndexRzo`. La fonction `generateIntegral` n'existe pas.)*

---

## FICHIER ACTEURS_A3_AURIGE2BB.html — Trombinoscope 3 pays

> Créé le 2026-05-28. Déplacé le 2026-05-28 dans le sous-dossier `Trombinoscope\`. Chemin actuel : `D:\CECPC\PRODUCTION\EXER\AURIGE 2BB\00_Boites à outils\MASTAURIGE\WEB\Trombinoscope\ACTEURS_A3_AURIGE2BB.html`

Fichier HTML autonome — format A3 paysage, 3 pages imprimables. **Usage animateur uniquement — ne pas inclure dans les exports stagiaires.**

### Contenu par page

| Page | Pays | Sections |
|---|---|---|
| 1 | 🔴 Mercure | Politique (Olamao + ministres + opposition) · Commandement MAF · Entités para-étatiques (TANTALE, N.O.M.) · Médias MER |
| 2 | 🔵 Dacie Romanie | Politique + opposition ASP + judiciaire · Commandement ADF (VONG + DJOBOVIC 8e DAC) · Acteurs internationaux (Rutte, Guterres, CICR) · Médias camp bleu |
| 3 | 🟡 Ruthnia Bella *(onglet jaune)* | Régime Youkachenko + appareil sécuritaire · Opposition (Tikhanov, Saniki) · CEMA RB · Médias RB + arcs narratifs |

> ⚠ **Le 🟡 est la couleur d'ONGLET de la page trombinoscope RB — pas un camp narratif.** Le camp de Ruthnia Bella (régime Youkachenko, BC1) reste **🔴 Rouge (allié MER)**. L'opposition Tikhanov **et** Saniki sont **🔴 rouge — pro-MER** *(corrigé 2026-06-01 ; Tikhanov n'est PAS bleue)*. Camp = ce registre + `avatars.js` ; fiches doctrine → `ANALYSTE\BOTHNIA`.

### Photos intégrées

| Personnage | Source |
|---|---|
| Olamao, Pallesson, Youkachenko, Rutte, Guterres | `WEB/images/` |
| Tikhanov, Saniki | `WEB/images/` (avatars existants) |
| Junker, Stoph, Ribiki | `CREATION/02 - MERCURE/Portraits/Ministres/` |
| PRUNIERE (MG 41e DIV) | `WEB/images/MER_PRUNIERE_Thierry_41DIV.jpg` — portrait officiel JPG (2026-05-28) |
| ZHUKOV (MG 43e DIV) | `WEB/images/MER_ZHUKOV_Mikhail_43DIV.png` — extrait PPTX |

### Accès et navigation

- **Depuis MASTAURIGE** : bouton **🗂 ACTEURS A3** (navy) dans l'en-tête de `index_master.html`
- **Retour MASTAURIGE** : bouton fixe bas-gauche `← MASTAURIGE` (même style que le retour MELMIL) — état complet restauré (scroll, filtres, onglets)
- **À l'impression** : le bouton retour est masqué (`@media print { display:none }`)

---

## Règles apprises

### [2026-05-28] Convention de codage des extensions éditoriales (injects hors MELMIL)

Quand MASTAURIGE produit un inject qui enrichit narrativement un inject MELMIL sans en être le calque exact, utiliser les suffixes ci-dessous. **Ces codes ne figurent PAS dans MELMIL.xls** — ils vivent uniquement dans index_master.html.

| Suffixe | Signification | LO héritée | Exemple |
|---|---|---|---|
| `.00` | Tweet d'amorce pré-série (avant le premier inject MELMIL numéroté) | LO de la série | `07.02.00` = 1er tweet @HmunikVoice (amorce campagne) |
| `Ai` | Amplification civile organique (couche blanchiment) | LO 1 + LO parent | `07.02.05Ai` = @TemoignageDAC photo tract NEUFCHATEAU |
| `Bi` | Amplification SMS/numérique | LO 1 + LO parent | `07.02.05Bi` = @MarionKessler57 SMS psyops |
| `Ci`, `Di`… | Extensions supplémentaires si nécessaire | LO 1 + LO parent | — |
| ~~`P-xx`~~ | Absorbé dans 07.07, 07.08, 07.05 *(migration terminée 2026-05-29)* | — | — |
| ~~`R-x`~~ | Absorbé dans 08.03, 07.01, 07.05, 08.01.xxAi.Rx *(migration terminée 2026-05-29)* | — | — |
| `CIVIL-xx` | Témoin civil neutre (ni rouge ni bleu) | LO 3 | CIVIL-01 = @clambroise55 |
| `TV4-xx` | Succès tactique camp bleu (point de repère neutre) | LO 2/3 | TV4-01 = capture 104 MER DJOBOVIC |

**Règle de vérité des dates MELMIL :** Les dates dans MELMIL.xls peuvent être modifiées manuellement et être inexactes.

#### ✅ Migration P-xx / R-x terminée (2026-05-29)

Tous les codes P-xx et R-x ont été migrés vers le format canonique `XX.YY.ZZAi` ou `XX.YY.ZZAi.Rx`. Résumé :

| Ancienne série | Nouveaux codes | Nouvelle série |
|---|---|---|
| P.01 (Architecture déni Storm-1516) | 07.07.01Ai/Bi/Ci · 07.07.02Ai · 07.07.03Ai→Ei · 07.07.04Ai | **07.07** |
| P.02 (Piège narratif rétroactif) | 07.08.01Ai→Ei · 07.08.02Ai · 07.08.03Ai→Di | **07.08** |
| P.03 (Bascule politique RB) | 07.05.01Ci/Di · 07.05.05Bi · 07.05.09Bi · 07.05.10Bi→Gi | **07.05** (absorbé) |
| R1 (Contremesures OTAN) | 08.03.03Ai→Ei | **08.03** |
| R3 (Relances courriers) | 08.01.01Ai.R1 + 08.01.01Ai.R2 | **08.01** (format .Rx) |
| R4 (BC1 blanchiment) | 07.05.05Bi | **07.05** |
| R5 (Signaux D+39 nuit) | 07.05.10Fi + 07.05.10Gi | **07.05** |
| R6 (Renforcements 07.01) | 07.01.05Ai + 07.01.06Ai | **07.01** |
| P-25/P-26 (Guterres) | 08.03.02Ai + 08.03.02Bi | **08.03** |

**Fichiers mis à jour :** `index_master.html` (ANIM_DATA `num` + `series` + LO_BY_KEY) + `melmil_inject_index.js` (nouvelles entrées).

> ⚠ **Périmètre exact de la migration (clarifié 2026-05-31) :** la migration ne couvre que les **fichiers de production** (`index_master.html`, `melmil_inject_index.js`). Des **labels P-xx historiques subsistent volontairement dans les mémoires** (chronologies et registres d'avatars de `MASTAURIGE/MEMOIRE.md`, `GUILLAUME/MEMOIRE.md`, `ANALYSTE/BOTHNIA/MEMOIRE.md`) comme repères d'**arcs narratifs**, pas comme codes d'injects.
> - Les **arcs** (P.01, P.02, P.03, P-25/26) se résolvent via le tableau de mapping ci-dessus.
> - Les **P-xx individuels** des registres d'avatars (P-02, P-04…P-20) n'ont **pas** de table de correspondance 1:1 complète → ne **pas** les renommer à l'aveugle. Avant tout renommage de registre, demander à GUILLAUME la correspondance P-xx → code canonique, ou laisser le label d'arc.

**⚠ RÈGLE CRITIQUE — Virgule finale dans `melmil_inject_index.js` (bug détecté 2026-05-29) :**
> Lors de l'ajout de nouvelles sections dans `MASTAURIGE_INDEX`, la **dernière entrée de chaque bloc précédent** doit se terminer par une virgule `,` avant le commentaire de la nouvelle section.
> Sans cette virgule, JavaScript lève une SyntaxError silencieuse et `MASTAURIGE_INDEX` devient `undefined` — tous les injects disparaissent de MELMIL et les popups ne fonctionnent plus.
> **Toujours vérifier** que la structure se lit : `],` (virgule) + saut de ligne + `// commentaire` + nouvelle entrée.

**Règle injects multi-canaux :** Un même code MELMIL peut apparaître sur deux cartes différentes (article BC1 + tweet EastWatch) — c'est intentionnel. Le `num` est identique, la **clé ANIM_DATA** porte le suffixe canal.

---

### [2026-05-29] Convention injects de relance — format `XX.YY.ZZAi.Rx`

Un inject de relance est joué si les entraînés ne réagissent pas à l'inject parent dans un délai donné.

**Format :** `XX.YY.ZZAi.Rx` — ex : `07.05.02Ai.R1`

| Élément | Rôle |
|---|---|
| `07.05.02Ai` | Inject parent auquel la relance se raccroche |
| `.R1` | Relance numéro 1 (`.R2` si une 2e est nécessaire) |

**Workflow de création d'une relance :**
1. Créer la card dans `index_master.html` (tweet / article) avec clé unique dans `markTweet` ou `openCard`
2. Ajouter dans `ANIM_DATA` : `num:"07.05.02Ai.R1"` 
3. Ajouter dans `LO_BY_KEY` : même LO que l'inject parent
4. Ajouter dans `melmil_inject_index.js` : `"07.05.02Ai.R1": [{key:"...", type:"...", label:"[RELANCE R1] — condition d'activation — contenu"}]`
5. **Pas de ligne XLS** — la relance s'insère automatiquement dans la card MELMIL de l'incident parent `07.05.02i`

**Ce qui est automatique (melmil.js modifié le 2026-05-29) :**
- `getParentInjectCode("07.05.02Ai.R1")` → retourne `"07.05.02i"` → s'insère dans la card MELMIL de l'incident
- Drag indépendant : la relance peut être glissée vers un autre jour sans déplacer les autres sous-injects
- Sync date : le déplacement MELMIL met à jour `card-day-KEY` en localStorage → `index_master.html` repositionne la card

**Visuel MELMIL :** bord gauche orange `#F57C00` + badge **"R1"** en orange.

**Label convention :** `"[RELANCE R1] — <condition d'activation> — <contenu résumé (date heure)>"`

---

### [2026-05-26] ⚠ RÈGLE OBLIGATOIRE — Attribution LO dans LO_BY_KEY à chaque nouvel inject

**Tout tweet card créé pour AURIGE 2BB doit inclure une entrée dans la table `LO_BY_KEY`** du JavaScript de `index_master.html`. Cette étape est non négociable — sans elle, le bouton ℹ animateur n'affiche pas la Ligne Opératoire.

**Processus de création d'un tweet card (ordre obligatoire) :**
1. HTML tweet card avec clé unique dans `markTweet(this, 'clé')`
2. Entrée ANIM_DATA `"clé": { num, series, desc }`
3. **Entrée `LO_BY_KEY` : `"clé": ["X"]`** — LO principale obligatoire, secondaire si deux axes distincts activés
4. Si inject réactif : noter la condition dans ANIM_DATA et en MEMOIRE GUILLAUME

**Référence LO par type de contenu tweet :**
- Tweet dénigrement forces bleues → **LO 2**
- Tweet valorisation MER / comm offensive → **LO 2**
- Tweet MER libérateur / DAC discrédité → **LO 4**
- Tweet délégitimation OTAN/ONU → **LO 4**
- Tweet escalade RB / rupture coalition → **LO 5**
- Tweet blanchiment / déni / graine → **LO 1**
- Tweet anti-mobilisation civile → **LO 2**
- Tweet insoutenabilité humanitaire → **LO 3**

**Localisation `LO_BY_KEY` :** chercher `var LO_BY_KEY` dans le `<script>` de `index_master.html`.

---

### [2026-05-25] Neutralité visuelle des tweets — AURIGE 2BB
Les tweets produits pour AURIGE 2BB ne doivent comporter **aucun indicateur visuel de camp** :
- Pas de bordure colorée (rouge/bleu) sur les cartes tweet
- Pas de badge "PRO-MERCURE" / "PRO-OTAN"
- Pas de couleur de camp sur les avatars — tous gris neutres (#80868b)
- Tous les tweets doivent être visuellement identiques

**Raison :** la cellule stagiaire doit classifier elle-même les comptes selon son analyse. L'IA ne doit pas orienter cette classification par des codes visuels.

**Conséquence pour la production :** ne jamais ajouter de classe `camp-rouge`, `camp-bleu`, `tweet-camp` ou `tweet-avatar.rouge/bleu` dans les nouvelles cartes tweet.

### [2026-05-27] Widget éditeur date/heure — animateur uniquement

Chaque card (article ET tweet) dispose d'un widget flottant à droite permettant à l'animateur de modifier le jour et l'heure de publication sans toucher au HTML.

**Comportement :**
- **Jour** : sélecteur `DAY_OPTIONS` (26 Mai → 04 Jun + "En attente") — modifie `data-dayorder` et repositionne la card dans le DOM en ordre chronologique décroissant
- **Heure** : champ `<input type="time">` — met à jour le texte affiché (`.card-meta span:first-child` pour les articles, `.tweet-time` pour les tweets)
- **Persistance "En attente" :** sauvegardé en `localStorage` (clé `card-attente-KEY`) — survit au rechargement de la page
- **Persistance changement de jour :** sauvegardé en `localStorage` (clé `card-day-KEY`) — survit au rechargement de la page *(corrigé 2026-05-28)*
- **Invisible dans les exports stagiaire :** supprimé automatiquement par les 3 fonctions generate (media/rzo/complet)

**Implémentation :** `initDateTimeEditors()` dans `index_master.html` — s'exécute uniquement si `data-master="1"` sur `<body>`.

#### ⚠ Bug corrigé (2026-05-28) — Changement de jour non persisté

**Symptôme :** Quand l'animateur bascule un article du 27 mai au 28 mai via le sélecteur de jour, le changement est appliqué dans le DOM mais **disparaît au rechargement** de la page. La card revient à son `data-dayorder` HTML d'origine.

**Cause :** Dans `applyChange()` de `initDateTimeEditors()`, le cas `dayVal !== 'attente'` ne sauvegardait rien en localStorage — seule la clé `card-attente-KEY` (booléen) était persistée. À chaque init, `daySel.value = card.dataset.dayorder` relisait le HTML, ignorant le changement.

**Correction :**
- Ajout d'une clé `card-day-KEY` en localStorage
- Dans `applyChange()` : `localStorage.setItem(_dayKey, String(newDay))` quand le jour est modifié ; `localStorage.removeItem(_dayKey)` quand "attente" est sélectionné
- Dans `initDateTimeEditors()` au chargement : si `_savedDay = localStorage.getItem(_dayKey)` est présent, `card.dataset.dayorder = _savedDay` avant de lire `daySel.value`

**Clés localStorage pour une card donnée :**
| Clé | Valeur | Cas d'usage |
|---|---|---|
| `card-attente-KEY` | `"1"` | Card basculée en "En attente" |
| `card-day-KEY` | `"28"` (numéro du jour) | Card dont le jour a été modifié par l'animateur |
| `card-time-KEY` | `"07:00"` (HH:MM) | Card dont l'heure a été modifiée par l'animateur |

**Règle de production :** `card-attente-KEY` et `card-day-KEY` sont mutuellement exclusives. `card-time-KEY` est conservé même en mode "attente" (l'heure est préservée quand la card est réactivée).

#### ⚠ Bug corrigé (2026-05-28) — Texte affiché dans la card non mis à jour au rechargement

**Symptôme :** Après avoir déplacé une card du 27 mai au 28 mai via le sélecteur, la date affichée dans la card (`.card-meta > span:first-child` ou `.tweet-time`) restait "27 Mai" après rechargement, même si le sélecteur affichait bien "28 Mai". De plus, les modifications d'heure n'étaient pas du tout persistées.

**Cause :** Deux problèmes distincts :
1. Au rechargement, `_savedDay` était appliqué sur `card.dataset.dayorder` et `daySel.value`, mais `updateCardTimeDisplay()` n'était **jamais appelé** → le texte HTML de la card restait celui d'origine.
2. `localStorage.setItem(_timeKey, ...)` **n'existait pas** → les changements d'heure disparaissaient au rechargement.

**Correction :**
- Ajout de `var _timeKey = 'card-time-' + _fallbackKey` et `var _savedTime = localStorage.getItem(_timeKey)`
- `timeInp.value` utilise maintenant `_savedTime || extractCardTime(card)` (préfère la valeur sauvée)
- Bloc de synchronisation au chargement : si `_savedDay` ou `_savedTime` existe et que la card n'est pas en "attente", appel immédiat de `updateCardTimeDisplay()` pour mettre à jour le texte affiché
- Dans `applyChange()` : ajout de `localStorage.setItem(_timeKey, newTime)` pour persister chaque changement d'heure

---

### [2026-05-27] Feature "En attente" — filtre jour orange

Option **"En attente"** disponible dans le sélecteur de jour de chaque widget éditeur. Quand sélectionnée :
- La card reçoit `data-dayorder="attente"`
- Elle devient **invisible dans tous les filtres de jour normaux** (TOUT, 26 Mai… 04 Jun)
- Elle n'apparaît que quand le bouton **"En attente"** (orange) est actif dans la barre de filtres

**Utilité animateur :** stocker les injects non encore programmés, les activer au bon moment en leur assignant un jour réel.

**Bouton HTML :** `<button class="day-btn day-btn-attente" data-dayorder="attente" onclick="setDay(this)">En attente</button>` — à droite de la barre de filtres de jours, CSS couleur `#E65100`.

**Persistance :** `localStorage` clé `card-attente-KEY` (KEY = identifiant unique de la card, dérivé du `onclick`).

**Actuellement en attente (27 mai 2026) :** `@NOVUSORDOMUNDI` — tweet pillages Héming — attendait l'activation du scénario ressortissants RB. Voir `rappel_novusordomundi_attente.md`.

---

### [2026-05-27] Panneau droit cards — .card-right-panel

Les deux widgets animateur (statut + date/heure) sont regroupés dans un **panneau unique `.card-right-panel`** centré verticalement à droite de chaque card :

```css
.card-right-panel {
    position: absolute;
    left: calc(100% + 10px);
    top: 50%;
    transform: translateY(-50%);
    display: flex;
    flex-direction: column;
    gap: 8px;
    align-items: stretch;
    z-index: 30;
}
@media (max-width: 960px) { .card-right-panel { display: none; } }
```

**Ordre vertical dans le panel :**
1. `.card-status-wrap` — sélecteur statut (⬜ En cours / 🟠 Finalisé / ✅ Envoyé)
2. `.card-datetime-wrap` — éditeur Jour + Heure

**Construction :** `initDateTimeEditors()` retire le `.card-status-wrap` existant de la card, le déplace dans le panel, ajoute le `.card-datetime-wrap` en dessous, puis appende le panel à la card.

**Bug corrigé (2026-05-27) :** `updateCounts()` contenait deux références à des variables non déclarées (`attente`, `elAttente`) provenant d'un revert partiel — causait un `ReferenceError` bloquant `filterArticles()` au chargement. Supprimé.

---

### [2026-05-27] Avatar avec photo portrait — format CSS background-image
Quand un personnage dispose d'une photo réelle (portrait Firefly ou autre), utiliser le style CSS sur le `div.tweet-avatar` plutôt que des initiales :
```html
<div class="tweet-avatar" style="background: url('./images/avatars%20tweet/NOM_FICHIER.png') center/cover; color: transparent;"></div>
```
Les espaces dans le nom de fichier doivent être encodés en `%20` dans l'URL CSS.
Les initiales texte (ex : `EW`, `PG`) restent la norme pour les avatars sans photo.

### [2026-05-27] Persistance état animateur — sessionStorage
`index_master.html` mémorise automatiquement dans `sessionStorage` l'état des filtres avant chaque navigation sortante :
- Onglet actif (média / RS)
- Jour sélectionné (TOUT / 27 mai / etc.)
- Mode cumul / exact
- Texte de recherche
- Position de défilement (scrollY)
- État classification camps

Au retour (par lien retour ou bouton précédent), tout est restauré instantanément.

**Implémentation :** fonction `saveMasterState()` appelée dans `openCard()` (articles) ET via `onclick` sur le bouton MELMIL.

#### ⚠ Règle — Toute navigation sortante depuis index_master.html doit appeler saveMasterState()

> **Tout nouveau bouton ou lien qui fait quitter `index_master.html` doit déclencher `saveMasterState()` avant la navigation** — sinon l'état n'est pas restauré au retour.

**Implémentation correcte pour un lien sortant :**
```html
<a href="chemin/vers/page.html" onclick="saveMasterState()">Libellé</a>
```

**Pourquoi les articles fonctionnent** : ils passent par `openCard()` qui appelle `saveMasterState()` en interne.
**Pourquoi MELMIL ne fonctionnait pas** : c'était un `<a href>` sans `onclick` — corrigé le 2026-05-28.

**Ne PAS utiliser `openCard()` pour MELMIL** : cette fonction ajoute `?from=master` dans l'URL et appelle `markViewed()`, ce qui est inutile pour MELMIL (pas un article à marquer comme lu).

### [2026-05-29] RÈGLE CANONIQUE — Langues des médias fictifs AURIGE 2BB

> **Today Mercure publie EXCLUSIVEMENT en anglais.**
> **Bella Channel 1 publie en anglais** (audience internationale fictive).
> **⚠ TV4 International publie en FRANÇAIS** *(corrigé 2026-06-02 — TV4 est un média basé en Dacie Romanie, pays francophone fictif ; ligne éditoriale = français par défaut, chrome compris).* L'ancienne règle « TV4 en anglais » est **abrogée**.
> Today Mercure et Bella Channel 1 publient en anglais (audience internationale fictive). La langue française apparaît dans **TV4**, dans les tweets de civils francophones (@clambroise55, @MarionKessler57…) et dans les tracts/courriers institutionnels MAF/maires.
> ✅ **Décision utilisateur (2026-06-02) :** les articles TV4 **déjà créés** (dont ceux en anglais, ex. `TV4_Article_Corruption_Rebuttal_01` 07.04.07Ei) sont **conservés tels quels — NE PAS retraduire**. La règle « TV4 en français » s'applique uniquement aux **nouveaux** articles à partir de cette date.

**Règle complémentaire — Vorin, tireur d'élite MER :**
> Aleksander Vorin est un **tueur de commandants de compagnie (capitaines)**. Il ne cible PAS les colonels ou lieutenants-colonels. Sa réputation est bâtie sur la décapitation des cadres de contact (capitaines, chefs de section), pas des états-majors. Toute production future sur Vorin doit respecter ce profil.
> Portrait disponible : `D:\CECPC\PRODUCTION\CREATION\02 - MERCURE\Portraits\MER_Aleksander VORIN_sniper_tueur_de_CDU.png`

---

---

---

## ⚠ RÈGLE AUTOMATIQUE — Mise à jour trombinoscope à chaque nouvel avatar (2026-05-29)

> **À chaque création d'un nouvel avatar RS fictif pour AURIGE 2BB, MASTAURIGE met automatiquement à jour la section "Avatars RS" correspondante dans le trombinoscope.**
> Fichier : `WEB\Trombinoscope\ACTEURS_A3_AURIGE2BB.html`

### Quelle section mettre à jour selon le camp de l'avatar

| Camp de l'avatar | Page trombinoscope | Section |
|---|---|---|
| 🔴 Rouge (pro-MER) | Page 1 — Mercure | `Avatars RS FORAD — AURIGE 2BB` |
| 🔴 Rouge camouflé civil / pseudo-neutre | Page 1 — Mercure | `Avatars RS FORAD — AURIGE 2BB` |
| 🔵 Bleu (OTAN/DAC) | Page 2 — Dacie Romanie | `Avatars RS — Camp Bleu + Civils ZO` |
| ⚪ Civil neutre (Lorraine) | Page 2 — Dacie Romanie | `Avatars RS — Camp Bleu + Civils ZO` |
| 🟡 RB (Ruthnia Bella) | Page 3 — Ruthnia Bella | `Avatars RS — Ruthnia Bella` |

### Format d'entrée à ajouter

```html
<div class="avatar-rs-item" style="border-left-color:#C41E3A;">
  <div class="avatar-rs-handle">@NouvelAvatar</div>
  <div class="avatar-rs-name">Prénom Nom — Rôle/Description courte</div>
  <div class="avatar-rs-footer">
    <span class="avatar-rs-lo">LO X</span>
    <span class="avatar-rs-camp rouge">ROUGE</span>
  </div>
</div>
```

Couleurs border-left et camp badge :
- Rouge : `#C41E3A` / classe `rouge`
- Bleu : `#2B5BA0` / classe `bleu`
- Neutre/pseudo : `#888` / classe `neutre`
- En attente : `#aaa` / classe `attente` + `opacity:0.65`

### Déclencheur : checklist création avatar complète

Quand MASTAURIGE crée un nouvel avatar :
1. ✅ Card HTML tweet dans `index_master.html`
2. ✅ Entrée `ANIM_DATA` + `LO_BY_KEY`
3. ✅ Entrée `melmil_inject_index.js`
4. ✅ Fiche dans `MASTAURIGE/MEMOIRE.md` (registre avatars)
5. **✅ Nouveau : entrée dans la section RS du trombinoscope** (`Trombinoscope\ACTEURS_A3_AURIGE2BB.html`)

---

## ⚠ RÈGLE ABSOLUE — MASTAURIGE est consulté sur TOUTE modification de ces fichiers (2026-05-29)

> **MASTAURIGE est l'agent expert de l'outil MASTAURIGE.**
> Toute modification de `index_master.html` ou de `MELMIL_ILI_GUILLAUME.html` requiert la consultation de MASTAURIGE, sans exception et quel que soit le type de modification.

**Périmètre de responsabilité MASTAURIGE = tout fichier sous :**
```
D:\CECPC\PRODUCTION\EXER\AURIGE 2BB\00_Boites à outils\MASTAURIGE\
```

Sans restriction de type — HTML, JS, CSS, PS1, BAT, XLS, images, scripts partagés.
**Cela s'applique à toute modification, quel qu'en soit le type.**

**Ce que MASTAURIGE vérifie systématiquement :**
1. Cohérence du code inject (format `XX.YY.ZZAi`, lettre libre, MELMIL_EDITORIAL_DAYS si nécessaire)
2. Présence des 4 éléments obligatoires pour tout nouvel inject : HTML card + ANIM_DATA + LO_BY_KEY + melmil_inject_index
3. MELMIL_SUBINJECT_DAYS si date sous-inject ≠ date parent XLS
4. Virgule finale dans melmil_inject_index.js (bug critique documenté)
5. Template HTML correct par site (BC1/TM/TV4/HEX ont chacun leur template obligatoire)
6. back-btn.js présent en dernière ligne des articles HTML

---

## ⚠ DOCTRINE CALIBRATION BRIGADE — Guide de production MASTAURIGE (2026-05-29)

> **Référence complète :** `AURIGE/MEMOIRE.md` + auto-mémoire `aurige_brigade_calibration.md`
> D+31→D+34 trop stratégique. À partir de D+35 et pour tout exercice AURIGE futur, **calibrer pour le PC brigade**.

### Formats prioritaires pour le niveau brigade

| Format | Contenu | Clé de réalisme |
|---|---|---|
| **Tweet civil local** (@clambroise55 type) | Tag vu, tract reçu, présence suspecte dans une ville ZO | Ville précise H-préfixe, numéro 03 72 67 XX XX |
| **Courrier HTML** | Plainte du maire au commandant brigade | Charte mairie fictive locale |
| **Article journal local** | L'Est Républicain fictif hostile à la brigade | Ton local, pas national |
| **Transcript radio** | Ce qui se dit sur Radio Moselle fictive | Court, neutre, rapporte |
| **RS humiliant** | Mème, montage, tweet moqueur sur la brigade | Impact émotionnel, minimaliste |
| **Photo tweet** | Vandalisme, drapeau, graffiti, tract collé | Image + légende civile |

### Villes ZO brigade AURIGE 2BB (cibles injects locaux)
- **Priorité haute :** HCHATEAU-SALINS · HLUNEVILLE · HSARREBOURG · HToul · HHéming
- **Éviter comme cible principale :** HNANCY (niveau division) 

### Roadmap formats à créer
- [ ] Pages LinkedIn HTML (criblage OSINT)
- [ ] Pages Wikipedia HTML (crédibilisation personnages)
- [ ] Journal local HTML (L'Est Républicain fictif)
- [ ] Radio locale (retranscription / clip audio)

### Chaîne Storm-1516 adaptée brigade
Phase 1 tweet civil → Phase 2 journal local → Phase 3 RS humiliants → Phase 4 courrier maire

---

## ⚠ RÈGLE CANONIQUE — Placement MELMIL des sous-injects multi-jours (2026-05-29)

> **Les codes d'injects ne changent JAMAIS pour des raisons de placement MELMIL.**
> Si un sous-inject est joué un jour différent de son incident parent XLS, on utilise `MELMIL_SUBINJECT_DAYS` — pas un nouveau code.

### Principe fondamental — split automatique

Un incident MELMIL peut s'étendre sur plusieurs jours. Dans ce cas :
- La card principale reste à la date du parent dans le XLS (ex : `07.01.02i` à D+32)
- Les sous-injects joués à une date différente créent automatiquement une **card split** à leur date de jeu
- Le split est identique au glisser-déposer manuel : la card parent est clonée, le sous-inject seul s'y trouve

### Architecture complète de synchronisation MELMIL ↔ index_master

```
index_master change date
        │ écrit card-day-KEY (localStorage)
        ▼
MELMIL reload → syncDayOverrides() Sync 2
        │ lit card-day-KEY → trouve le sous-inject XLS
        │ applySubInjectPosition() — SPLIT sans persistence
        │ (SUBINJ_KEY non modifié)
        ▼
buildSubInjectDefaultSplits()
        │ skip si SUBINJ_KEY set (drag MELMIL)
        │ skip si card-day-KEY set (index_master)
        │ sinon → applySubInjectPosition() depuis MELMIL_SUBINJECT_DAYS
        ▼
MELMIL drag sous-inject
        │ handleSubInjectDrop() → saveSubInjectPositions()
        │ écrit SUBINJ_KEY + card-day-KEY
        ▼
index_master reload → initDateTimeEditors()
        lit card-day-KEY → repositionne la card
```

**Règle clé :** `SUBINJ_KEY` (melmil-subinj) est écrit UNIQUEMENT par les drags manuels de l'animateur dans MELMIL. Les positions automatiques (Sync 2 + defaults) n'y touchent pas → priorité claire.

### Priorité des positions (du plus fort au plus faible)

| Priorité | Source | Clé localStorage | Écrit par |
|---|---|---|---|
| 1 | Drag MELMIL sous-inject | `melmil-subinj` | `saveSubInjectPositions()` |
| 2 | Date selector index_master | `card-day-KEY` | `initDateTimeEditors()` dans index_master |
| 3 | Default `MELMIL_SUBINJECT_DAYS` | *(aucune — visuel seul)* | `applySubInjectPosition()` |

### `MELMIL_SUBINJECT_DAYS` (melmil_inject_index.js)

```javascript
var MELMIL_SUBINJECT_DAYS = {
    "07.01.02Ci": 29,   // TM Vorin — D+34 — parent 07.01.02i est à D+32
    "07.05.03Fi": 29,   // BC1 Manifestations J4 — D+34 — parent 07.05.03i est à D+33
};
```

### Règle de production — quand utiliser MELMIL_SUBINJECT_DAYS

| Situation | Action |
|---|---|
| Sous-inject joué le **même jour** que le parent XLS | Coder `XX.YY.ZZAi` normalement — apparaît dans la card du parent ✅ |
| Sous-inject joué un **autre jour** que le parent XLS | Garder le code + `MELMIL_SUBINJECT_DAYS[code] = dayorder` |
| Incident thématiquement nouveau, pas de parent existant | Code libre `XX.YY.VVi` + `MELMIL_EDITORIAL_DAYS[XX.YY.VVi] = dayorder` |

### ⚠ NE JAMAIS changer un code d'inject pour résoudre un problème de placement

> Les codes (`07.01.02Ci`, `07.05.03Fi`…) sont des identifiants narratifs permanents présents dans index_master.html, ANIM_DATA, LO_BY_KEY, melmil_inject_index.js, GUILLAUME/MEMOIRE.md et les rapports exercice. Les renommer crée des incohérences en cascade.

### Cas de référence (2026-05-29)

| Inject | Code (conservé) | Parent XLS | Date parent | Date jeu | Solution |
|---|---|---|---|---|---|
| TM Portrait Vorin | `07.01.02Ci` | `07.01.02i` | D+32 | D+34 | `MELMIL_SUBINJECT_DAYS["07.01.02Ci"] = 29` |
| BC1 Manifestations J4 | `07.05.03Fi` | `07.05.03i` | D+33 | D+34 | `MELMIL_SUBINJECT_DAYS["07.05.03Fi"] = 29` |

### Responsabilité inter-agents

| Agent | Rôle |
|---|---|
| **GUILLAUME** | Fournit la date de jeu + contexte scénario |
| **NOYAU** | Valide la cohérence avec la synchromatrice |
| **MASTAURIGE** | Code l'inject, vérifie `melmil_data.js`, ajoute dans `MELMIL_SUBINJECT_DAYS` si nécessaire |

---

### [2026-05-30] Comportement "En attente" — Corrections synchronisation (2026-05-30)

**Problème identifié :** Quand une card est basculée "En attente" dans index_master.html :
1. Sa date HTML restait affichée (ex: "03 Juin 08h00") au lieu de montrer un statut "En attente"
2. MELMIL ne déplaçait pas le sous-inject vers la colonne "À placer" — il restait à sa date d'origine

**Corrections apportées :**

| Fichier | Correction |
|---|---|
| `index_master.html` | `applyChange()` : quand "attente" sélectionné → affiche `⏳ En attente` dans l'élément date de la card |
| `index_master.html` | `initDateTimeEditors()` au chargement : si `card-attente-KEY = "1"` → affiche immédiatement `⏳ En attente` |
| `melmil.js` | `syncDayOverrides()` Sync 2 : lit `card-attente-KEY`, déplace le sous-inject vers `cell-RX-overflow` (= "À placer") |
| `melmil.js` | `buildSubInjectDefaultSplits()` : skip si `card-attente-KEY = "1"` pour ne pas appliquer le default et écraser le statut attente |
| `melmil.js` | `saveSubInjectPositions()` : drag vers jour → efface `card-attente-KEY` + écrit `card-day-KEY` ; drag vers overflow → écrit `card-attente-KEY` + efface `card-day-KEY` |
| `melmil.js` | `savePositions()` (drag incident entier) : même logique bidirectionnelle via `propagateToCard()` |
| `melmil.js` | Drop ghost r7 : même logique bidirectionnelle jour ↔ overflow |

**Priorité de positionnement MELMIL (mise à jour) :**
1. Drag manuel MELMIL (`SUBINJ_KEY`) — priorité absolue
2. **"En attente" index_master** (`card-attente-KEY = "1"`) → overflow "À placer"
3. Date modifiée index_master (`card-day-KEY`) → colonne de la date
4. Default `MELMIL_SUBINJECT_DAYS` → colonne par défaut si rien d'autre

---

### [2026-05-30] ⚠ RÈGLE CRITIQUE — Attributs obligatoires sur toute article-card (audit 2026-05-30)

**Problème découvert :** 37 cards dans index_master.html manquaient l'attribut `data-camp`, créées avant que la règle devienne obligatoire (cards P-xx, cards anciennes).

**Impact :** Classification visuelle absente (pas de border-color rouge/bleu). La card `BCI_Article_MinskConseildUrgence` (07.05.10Bi) semblait invisible car son `data-camp` manquant empêchait l'affichage correct dans certains contextes. → Corrigé le 2026-05-30 par correction en masse.

**Règle canonique — 5 attributs obligatoires sur toute nouvelle article-card :**

```html
<div class="article-card"
     data-source="[bc1|tm|tv4|hex|inst]"
     data-category="[media|social]"
     data-camp="[rouge|bleu|neutre|gris]"
     data-dayorder="[26-35|attente]"
     onclick="openCard(this, '...')  ou  markTweet(this, 'KEY')">
```

| `data-source` | `data-camp` attendu |
|---|---|
| `bc1`, `tm` | `rouge` |
| `tv4`, `hex` | `bleu` |
| `inst` (courriers maires/préfet DAC) | `bleu` |
| tweet `data-camp` déjà présent | selon camp avatar |
| `neutre` (civils locaux) | `neutre` |

**Correction highlightCardFromUrl() (2026-05-30) :** La fonction basculait toujours sur filtre TOUT, rendant les cards "En attente" invisibles même via navigation MELMIL. Désormais, si la card cible est en `data-dayorder="attente"`, le filtre bascule automatiquement sur "En attente" avant de scroller.

**Checklist création nouvelle card (mise à jour) :**
1. HTML card dans index_master.html avec les 5 attributs ci-dessus
2. Entrée ANIM_DATA
3. Entrée LO_BY_KEY
4. Entrée melmil_inject_index.js
5. MELMIL_SUBINJECT_DAYS si date ≠ parent XLS
6. Trombinoscope RS si nouvel avatar
**+ Vérifier que `data-camp` est bien présent**

---

### [2026-05-29] ⚠ Template HTML obligatoire — Sites fictifs TV4, BC1, TM

> **Tout nouvel article HTML pour un site fictif AURIGE 2BB doit utiliser le template complet de référence — jamais un template simplifié ad hoc.**

**Référence par site :**

| Site | Article de référence | Chemin |
|---|---|---|
| TV4 International | TV4_Article_Panique_01.html | `WEB/Site TV4/TV4_Article_Panique_01.html` |
| Bella Channel 1 | BCI_Article_Rencontre.html | `WEB/Site Bella Channel 1/BCI_Article_Rencontre.html` |
| Today Mercure | TM_Article_CEMA_01.html | `WEB/Site Today Mercure/TM_Article_CEMA_01.html` |

**Blocs obligatoires TV4 (dans l'ordre) :**
1. `.top-bar` — barre noire avec recherche + nav + X/f/YT/TG + sélecteur langue
2. `.logo-band` — logo TV4 bicolore avec classe `tv4-logo-wrap`
3. `.ticker-bar` — bande orange défilante
4. `.page-wrap` — grid `210px 1fr`
5. `.left-nav` — nav gauche + live dot + bloc on-air
6. `.breadcrumb` — fil d'Ariane
7. `.article-card` — hero + article-head + article-body + article-tags
8. `.more-section` — "More on This Story" 3 cartes (liens ≤ même date)
9. `.site-footer` — footer complet avec logo, tagline, social, liens
10. `<script src="../shared/back-btn.js"></script>` — OBLIGATOIRE, dernière ligne avant `</body>`

**Interdictions :**
- PAS de `#backBtn{display:none;}` dans le CSS
- PAS de template simplifié sans nav gauche
- PAS de footer réduit à une ligne
- PAS de lien "More on This Story" vers un article futur

**Contexte de la règle :** TV4_Article_SF_HCHATEAU_01.html avait été créé avec un template incomplet (sans nav gauche, sans breadcrumb, sans More section, sans footer complet, sans back-btn). Corrigé le 2026-05-29.

---

### [2026-05-24] Distribution AURIGE 2BB
Les tweets AURIGE ne passent pas par MASSTALK V3 — ils sont intégrés directement en HTML dans `WEB/index.html` (section `data-category="social"`). Le système NEW badge + localStorage track les tweets lus via leur @handle.

### [2026-05-24] Avatars ORION 26 réutilisables pour AURIGE 2BB
Les avatars de la base ORION 26 sont génériques (journalistes, militants, ONG) et fonctionnent pour AURIGE 2BB. Adapter le contenu des posts au contexte Lorraine sans modifier les profils.

---

## Série 04.01 — NRBC / Site Seveso HToul

> Ajoutée le 2026-05-29 — D+34

### Nouvelle série dans MELMIL
- `ROW_MAP['04.01'] = 'r1'` — ligne ILI EHO MER (r1, avec 07.01 et 07.02)
- `CLASS_MAP['04.01'] = 'c41'` — couleur CSS `.c41 { background: #BF360C }` (orange brûlé hazmat)

### Avatars utilisés pour cette série
| Handle | Nom | Initiales | Camp | Injects |
|---|---|---|---|---|
| @HmunikVoice | Pavlus Juri Gautoreif | **PG** | 🔴 Rouge | 04.01.01Ci — SEVESO OTAN accusation |
| @clambroise55 | Claire Ambroise | **CA** | ⚪ Neutre civil LO3 | 04.01.01Di — panique civile HToul masques gaz |

### Production 2026-05-29 — Série 04.01
| Inject | Clé | Canal | Contenu résumé |
|---|---|---|---|
| 04.01.01Ai | `TV4_Article_Seveso_HToul_01` | TV4 article | Pompiers DAC héroïques — incendie chimique BRENNTAG HToul — 08h30 CET — **"dans la banlieue de HToul"**, horaire vague "Thursday morning" |
| 04.01.01Bi | `TM_Article_Seveso_OTAN_01` | TM article | OTAN accusé tir SEVESO, nuage toxique, 12 000 civils — 11h00 MSK |
| 04.01.01Ci | `@HmunikVoice_Seveso_NRBC` | Tweet rouge | OTAN incompétent, site décadent, nuage toxique — 09h00 |
| 04.01.01Di | `@clambroise55_HToul_masques` | Tweet neutre | Panique civile, fumée noire, besoin masques à gaz — 09h15 |
| **04.01.01Ei** | `@clambroise55_commercy_fumees` | Tweet neutre | Nuage dérive vers HCommercy — odeur âcre signalée — silence préfectoral — 14h00 — LO 3 |

### Avatars série 04.01 (ajout 04.01.01Ei)
@clambroise55 réutilisée pour 04.01.01Ei — même civile, deuxième tweet dans la journée — cohérence éditoriale.

---

## Mapping 08.02 → éléments index_master (mis à jour 2026-05-29)

| Inject MELMIL | Code MASTAURIGE | Fichier | Date | Statut |
|---|---|---|---|---|
| **08.02.02i** | **08.02.02Ai** | `TV4_Article_8DAC_HNANCY_01.html` | 28 Mai D+33 | ✅ Intégré |
| **08.02.02i** | **08.02.02Bi** | tweet `@KolesnikovAndrei_POW_maltraitance` | 29 Mai D+34 | ✅ Intégré |
| 08.02.01i | — | — | 31 Mai D+36 | ❌ Non créé |
| 08.02.03i | — | — | 31 Mai D+36 | ❌ Non créé |
| 08.02.04i | — | — | 31 Mai D+36 | ❌ Non créé |

**08.02.02Ai :** TV4 — 104 soldats MER capturés à HNANCY par la 8e DAC, commandant DJOBOVIC (28 Mai 06h45). Rupture narrative MER : "repli calculé" ← contredit par la capture de 104 hommes. Force un inject de blanchiment MER côté 07.08. LO 2 + LO 3.

**08.02.02Bi :** @KolesnikovAndrei — 29 Mai 16h00 — Rumeurs maltraitance POW MER en garde 8e DAC. Appel CICR pour accès immédiat. Discrédit DAC vs troupes FR (même coalition, pas mêmes standards). Avatar @KolesnikovAndrei choisi pour profil IHL/DICA déjà établi (07.06). `MELMIL_SUBINJECT_DAYS["08.02.02Bi"] = 29`. LO 2 + LO 3.

---

## Sessions de production
<!-- À compléter au fil des sessions -->
| Date | Exercice | Thème animé | Avatars | Nombre de posts |
|---|---|---|---|---|
| 2026-05-24 | AURIGE 2BB | Convois OTAN Lorraine + N.O.M | 4 avatars | 4 cards HTML |
| 2026-05-26 | AURIGE 2BB | Tractage D+31 + amplification civile NEUFCHATEAU | @TemoignageDAC | 1 tweet avec image |
| 2026-05-27 | AURIGE 2BB | Opposition RB réaction Youkachenko — P-27/P-28 | @S_Tikhanov (photo), @A_Saniki (photo) | 2 tweets avec avatar photo portrait |
| 2026-05-28 | AURIGE 2BB | Témoin civil D+33 — blocage N4 Void-Vacon | @clambroise55 (initiales CA) | 1 tweet civil NEUTRE — LO 3 |
| 2026-05-28 | AURIGE 2BB | Article Today Mercure — MG PRUNIERE CO 41e DIV CHARS (07.02.02i) | Today Mercure (TM) | TM_Article_CEMA_01.html réécrit — profil Héros de la Nation, 3 citations, front Moselle — LO 2 |
| 2026-05-29 | AURIGE 2BB | 6 nouveaux injects D+34 (29 Mai) — 07.01/07.02/07.05/07.06/04.01 | @clambroise55 (2e tweet), @KolesnikovAndrei, @GavrilovBorislav, BC1, TM×2 | 3 articles HTML créés + 3 tweets + ANIM_DATA + LO_BY_KEY + melmil_inject_index mis à jour |
| 2026-05-29 | AURIGE 2BB | Intégration image base64 dans BCI_Article_Manifestations_NP_BL.html | BC1 | Photo `manifestation BelleRussia 29 mai.jpg` encodée en base64 (172 Ko) — hero section remplace le placeholder texte "DAY 4" par l'image réelle — fichier HTML : 193 Ko |
| 2026-05-30 | AURIGE 2BB | 07.05.05 — Fermeture frontière RB (D+35, 30 Mai) : correction BCI_Article_Frontiere + création TV4_Article_Frontiere_BR_01 | BC1 + TV4 | BC1 corrigé : source → Min. Int. Ivan Lubrakov (au lieu de Marchuk), horaires vagues ; TV4 créé (07.05.05Ci) : perspective externe, logistique OTAN, 09h15 CET — melmil_inject_index + ANIM_DATA + LO_BY_KEY mis à jour |
| 2026-05-30 | AURIGE 2BB | 07.05.04 — Révision tweets sommet secret Olamao-Youkachenko (D+34, 29 Mai) | @EastWatch_Intl (clé renommée), @A_Saniki, @S_Tikhanov, @BelovDimitri, @BelikovaMarina (1ère app.) | 1 tweet corrigé (clé → @EastWatch_olamao_summit) + 4 nouveaux tweets Bi/Ci/Di/Ei — @BelikovaMarina intégrée dans trombinoscope |

## ⚠ RÈGLE ÉDITORIALE — Liens croisés entre articles (ajout 2026-05-29)

> **Un article ne doit JAMAIS contenir un lien ("Related articles", "À lire aussi") vers un article publié à une date ULTÉRIEURE.**

### Règle de production
Lors de la création ou de la mise à jour d'un article HTML (TM, BC1, TV4, HEX...) :
1. Identifier la date de l'article en cours
2. Pour chaque entrée de la section "Related articles" : **vérifier que la date de l'article lié ≤ date de l'article en cours**
3. Liens vers des articles du même jour : acceptables
4. **Liens vers des articles futurs : interdits** — ils spoilent les événements et brisent la cohérence de simulation pour les stagiaires

### Pourquoi c'est critique
Les articles sont consultés par les stagiaires dans le cadre de la simulation en temps réel. Si un article du 30 Mai contient un lien vers un article du 4 Juin, les stagiaires découvrent un événement futur avant qu'il soit "joué" par l'animateur, brisant l'immersion et l'effet pédagogique de l'exercice.

### Correction effectuée le 2026-05-29
8 liens chronologiquement incohérents supprimés de 8 articles. Voir GUILLAUME\MEMOIRE.md section "Règle éditoriale — Liens croisés" pour la liste complète et la chronologie de référence des articles.

---

## Numéros de téléphone fictifs — Règle de réalisme

**⚠ RÈGLE OBLIGATOIRE** : Ne jamais écrire `XX XX XX XX`. Utiliser les plages fictives ci-dessous.

| Région / Zone | Format | Exemple |
|---|---|---|
| 01 — Île-de-France | `01 99 00 XX XX` | 01 99 00 47 23 |
| 02 — Nord-Ouest / Outre-mer | `02 61 91 XX XX` | 02 61 91 08 54 |
| **03 — Nord-Est (Lorraine)** | **`03 72 67 XX XX`** | **03 72 67 14 89** |
| 04 — Sud-Est | `04 51 08 XX XX` | 04 51 08 37 62 |
| 05 — Sud-Ouest | `05 36 49 XX XX` | 05 36 49 91 05 |

**AURIGE 2BB (théâtre Lorraine) → préfixe `03 72 67` systématique.**
S'applique à : SMS psyops, tweets avec numéros, bio d'avatars, captures d'écran fictives.

### Numéros canoniques — attributions permanentes (tous exercices)

| Institution | Numéro fixe |
|---|---|
| **Palais présidentiel DAC / HPARIS** | **01 99 00 01 00** |

Fixe et permanent — ne jamais changer ce numéro entre les exercices.

---

### Timing injects D+31 (26 mai) — référence production

| Heure | Inject | Avatar / Canal | Camp | Référence canonique |
|---|---|---|---|---|
| 14h00 | Tract MAF STEP 1 — image jpg | MAF (média) | ROUGE | **07.02.05i** |
| 15h00 | Photo tract NEUFCHATEAU — tweet image | @TemoignageDAC | ROUGE | **07.02.05Ai** (ext. civile Step 1) |
| 18h00 | SMS bombing — @MarionKessler57 partage capture SMS psyops reçu | @MarionKessler57 | **BLEU** ⚠ | **07.02.05Bi** (ext. SMS Step 1) |

> **Historique correction (2026-05-28) :** @TemoignageDAC était codé `07.02.06i` (collision avec STEP 2) et @MarionKessler57 était codé `07.02.05i_bis` (doublon avec STEP 1). Codes corrigés dans ANIM_DATA de index_master.html. Les codes `07.02.05Ai` et `07.02.05Bi` sont des **extensions éditoriales** de 07.02.05i — ils ne figurent pas dans MELMIL.xls (normal).

**@MarionKessler57 :** Marion Kessler — civile Moselle (57), initiales MK. Compte BLEU = civile non-suspecte qui amplifie involontairement le psyops. Inject pédagogiquement clé : force les stagiaires à analyser même les sources "friendly". Image : `./images/SMS2 Dacia ROMANIA tombeau.jpg`.

### Timing injects D+32 (27 mai) — complément

| Heure | Inject | Avatar / Canal | Référence |
|---|---|---|---|
| 07h00 | Héros sniper VORIN — tweet décalé de D+31 au matin D+32 | @HmunikVoice | 07.01.02i |

### Injects EN ATTENTE (bouton dédié dans index_master.html)

Trois courriers 08.01 retirés du 27 mai et placés dans le filtre **EN ATTENTE** (bouton orange) — disponibles quand l'animateur décide de les activer :

| Inject | Sujet | Référence |
|---|---|---|
| 08.01.01i | Corridors humanitaires — collectif des maires | `courrier_maires_corridors.html` |
| 08.01.05i | Musées — Convention de La Haye 1954 | `courrier_prefet_musees.html` |
| 08.01.06i | Lieux de culte — art. 53 Protocole additionnel I | `courrier_prefet_cultes.html` |

**Actifs le 27 mai :** uniquement 08.01.03i (écoles) + 08.01.04i (hôpitaux/EHPAD).

---

## [2026-05-28] FONCTIONNALITÉS MELMIL ↔ index_master.html — Session technique

> Ensemble de fonctionnalités ajoutées lors de la session du 28 mai 2026. À connaître pour tout travail futur sur MELMIL ou index_master.

### 1. Navigation MELMIL → MASTAURIGE (click-to-popup)

**Concept :** Cliquer sur un inject card dans `MELMIL_ILI_GUILLAUME.html` ouvre un popup listant toutes les cards MASTAURIGE associées à cet inject. Cliquer sur un bouton du popup navigue vers `index_master.html` sur la bonne card, avec animation visuelle de ciblage.

**Fichiers impliqués :**

| Fichier | Rôle |
|---|---|
| `MELMIL/melmil_inject_index.js` | Données : `var MASTAURIGE_INDEX = { "07.02.05i": [{key, type, label}...] }` — 27 entrées couvrant toutes les séries 07.01 à 08.01 |
| `MELMIL/melmil.js` | Logique popup : `openInjectPopup()`, `closeInjectPopup()`, `initClickPopup()` |
| `MELMIL/MELMIL_ILI_GUILLAUME.html` | HTML du popup + CSS + `<script src="melmil_inject_index.js">` chargé AVANT `melmil.js` |

**Structure de `melmil_inject_index.js` :**
```javascript
var MASTAURIGE_INDEX = {
    "07.02.05i": [
        {key:"tract1-daciaromania-votre-tombeau-D+31-26-mai", type:"tract",   label:"Tract MAF STEP 1 — (26 Mai 14h00)"},
        {key:"@TemoignageDAC_tract_neufchateau",              type:"tweet",   label:"@TemoignageDAC — Photo tract NEUFCHATEAU (26 Mai 15h00)"},
        {key:"@MarionKessler57_sms",                          type:"tweet",   label:"@MarionKessler57 — SMS en masse (26 Mai 18h00)"}
    ],
    // ... (27 codes total)
};
```
Types possibles : `"tweet"`, `"article"`, `"tract"`, `"courrier"`.

**URL de navigation :** `../index_master.html?card=KEY` (encodeURIComponent de la clé ANIM_DATA).

**Protection drag vs click :** Le flag `isDragging` (avec `setTimeout(50ms)` au dragend) empêche l'ouverture du popup lors d'un glisser-déposer. La propriété `isDragging` existe déjà dans `melmil.js`.

**Popup CSS — charte graphique :**
- Fond : `#1a1a2e` (sombre)
- Bordure : or `#FFD700`
- Couleurs type badge : tweet `#1DA1F2` · article `#7B1FA2` · tract `#F57C00` · courrier `#2E7D32`
- Fermeture : clic overlay, bouton ✕, touche Échap

---

### 2. Navigation entrante ?card=KEY — highlightCardFromUrl()

**Concept :** Quand `index_master.html` est ouvert avec `?card=KEY` en paramètre URL, la fonction `highlightCardFromUrl()` localise automatiquement la card, bascule le bon onglet, réinitialise les filtres, défile jusqu'à la card et applique deux animations visuelles.

**Localisation de la card :** Parcours de tous les `.article-card` — recherche `'KEY'` dans l'attribut `onclick` (fonctionne pour `markTweet(this,'KEY')` et `openCard(this,'.../KEY.html')`).

**Comportement automatique à l'arrivée :**
1. Bascule l'onglet correct (media / social) selon `card.dataset.category`
2. Réinitialise le filtre jour → TOUT (dayorder 0) + mode cumulatif
3. Appelle `filterArticles()` pour afficher la card
4. Efface le `?card=KEY` de l'URL (`history.replaceState`)
5. Flash or 3× (animation `.melmil-link-highlight`, 2.7s)
6. Icône `▶` animée dans la marge gauche (classe `.melmil-link-active`, 10s ou jusqu'au clic)
7. Défilement centré dans la fenêtre visible (calcul dynamique `scrollMarginTop` dans `setTimeout(120ms)`)

**Classes CSS :**
```css
/* Flash 3× or */
.melmil-link-highlight { animation: melmilFlash 0.9s ease-in-out 3; }
@keyframes melmilFlash {
    0%, 100% { box-shadow: none; }
    33%, 66% { box-shadow: 0 0 0 3px #FFD700, 0 0 20px rgba(255,215,0,0.45); }
}

/* Icône ▶ rebondissante en marge gauche */
.melmil-link-active::before {
    content: '▶'; position: absolute; left: -20px; top: 50%;
    transform: translateY(-50%); font-size: 12px; color: #FFD700;
    animation: melmilBounce 0.65s ease-in-out infinite;
}
```

**Règle de centrage scroll :**
```javascript
var stickyH  = 160;  // hauteur cumulée des 3 headers sticky
var visibleH = window.innerHeight - stickyH;
card.style.scrollMarginTop = Math.max(stickyH, stickyH + (visibleH - card.offsetHeight) / 2) + 'px';
card.scrollIntoView({ behavior: 'smooth', block: 'start' });
```
Le `setTimeout(120ms)` est **indispensable** — donne le temps au navigateur de recalculer le layout après `filterArticles()` avant de mesurer `card.offsetHeight`.

---

### 3. Headers sticky — hiérarchie z-index (correction)

**Problème corrigé :** Les boutons ⚡ MELMIL et 🗂 ACTEURS A3 dans `.g-header` étaient inaccessibles en bas de page parce que `.cat-tabs` avait le même `z-index: 100` et `top: 0` → le navigateur peignait les onglets par-dessus le header.

**Solution — Variables CSS + hiérarchie z-index :**

```css
:root { --header-h: 57px; --cattabs-h: 62px; }

.g-header      { position: sticky; top: 0;                                    z-index: 120; }
.cat-tabs      { position: sticky; top: var(--header-h);                      z-index: 100; }
.day-filter-bar{ position: sticky; top: calc(var(--header-h) + var(--cattabs-h)); z-index: 90; }
```

**Règle de production :** Si un 4e niveau sticky est ajouté, utiliser `z-index: 80` et `top: calc(var(--header-h) + var(--cattabs-h) + var(--daybar-h))` avec une nouvelle variable CSS `--daybar-h`.

---

### 4. Bouton "Afficher la classification" — déplacé dans la barre des jours

**Avant :** Deux boutons séparés, un dans l'onglet media et un dans l'onglet social (dans les `[data-show]`).
**Après :** Un seul bouton `.classify-btn` dans `.day-filter-inner` de la `.day-filter-bar`, poussé à l'extrême droite par `margin-left: auto`.

**CSS :**
```css
.classify-btn { margin-left: auto; /* pousse à droite, hors du flux des boutons de jours */ }
```

**Contrainte importante :** Pour que `margin-left: auto` fonctionne dans un flex container, le conteneur `.day-filter-inner` ne doit pas avoir `max-width` avec `margin: auto` — ceux-ci ont été supprimés pour permettre la largeur totale de la barre.

**HTML (dans `.day-filter-inner`) :**
```html
<div class="day-mode-toggle">
    <button class="mode-btn active" id="modeCumul" onclick="setMode('cumul')">Cumulatif</button>
    <button class="mode-btn" id="modeExact" onclick="setMode('exact')">Exact</button>
</div>
<button class="classify-btn" id="classifyBtn" onclick="toggleClassification()">
    <span class="classify-dot"></span>Afficher la classification
</button>
```

---

### 5. Intégration d'images dans les articles BC1/TM/TV4

**Règle :** Quand une image est disponible pour un inject, elle doit être intégrée dans **deux endroits** :

| Endroit | Chemin relatif | Balise |
|---|---|---|
| Card-thumb dans `index_master.html` | `./images/FICHIER.jpg` | `<div class="card-thumb"><img src="./images/FICHIER.jpg" alt="..."></div>` |
| Hero section dans l'article HTML | `../images/FICHIER.jpg` | `<img src="../images/FICHIER.jpg" alt="..." style="width:100%; height:auto; display:block;">` |

**Exemple appliqué (07.05.03i) :**
- Image : `images/07.05.03_Manifestation_opposition_Pro_MER_BR_BC1.jpg`
- Card-thumb dans index_master : `./images/07.05.03_Manifestation_opposition_Pro_MER_BR_BC1.jpg`
- Hero dans BCI_Article_Manifestations.html : `../images/07.05.03_Manifestation_opposition_Pro_MER_BR_BC1.jpg`

---

### 7. Dots indicateurs MASTAURIGE dans les cards MELMIL (ajout 2026-05-28)

Chaque card inject dans MELMIL affiche une rangée de petits points colorés en bas, indiquant le nombre et le type de cards MASTAURIGE liées.

**Couleurs (identiques au popup) :**
| Type | Couleur | Code |
|---|---|---|
| Tweet | Bleu | `#1DA1F2` |
| Article | Violet | `#7B1FA2` |
| Tract | Orange | `#F57C00` |
| Courrier | Vert | `#2E7D32` |

**Comportement :** 1 point = 1 card dans `MASTAURIGE_INDEX[code]`. Tooltip au survol = libellé complet de la card. Les dots n'apparaissent que si `MASTAURIGE_INDEX` est chargé ET que le code a des entrées.

**Implémentation :** Dans `buildInjects()` de `melmil.js` — génère les dots avant d'appender la card au DOM. CSS dans `melmil.css` (`.inj-dots` + `.inj-dot`). Légende ajoutée en bas de `MELMIL_ILI_GUILLAUME.html`.

**Règle de maintenance :** Quand une nouvelle card est ajoutée à `melmil_inject_index.js`, le dot apparaît automatiquement sans intervention sur le HTML MELMIL.

### 6. Règle de vérification des descriptions visuelles

> **RÈGLE OBLIGATOIRE** — Avant toute publication, les descriptions textuelles d'une image doivent être vérifiées contre l'image réelle.

**Cas d'erreur corrigé (2026-05-28) :** `BCI_Article_Manifestations.html` décrivait des "drapeaux de Ruthnia Bella et de la République de Mercure" alors que l'image montrait le drapeau Pahonia (symbole nationaliste biélorusse, drapeau blanc-rouge-blanc avec cavalier). **Trois occurrences** ont été corrigées : caption, deck, et corps de l'article.

**Processus de vérification :**
1. Ouvrir l'image avant de rédiger tout texte descriptif
2. Décrire exactement ce que montre l'image (pas ce qu'on suppose)
3. Chercher TOUTES les occurrences de la description dans l'article (caption + deck + corps)
4. Pour les symboles géopolitiques (drapeaux, insignes) : utiliser une formulation générique ("symboles nationalistes", "drapeaux de la résistance") en cas de doute plutôt que de nommer un pays spécifique

---

## ⚙️ OUTILS D'OPTIMISATION MASTAURIGE (2026-05-31)

> 5 optimisations livrées et validées le 2026-05-31. Aucune ne touche au format des injects ni au scénario.

### 1. Contrôleur automatique — `WEB\OUTILS\verifier_mastaurige.py` (+ `VERIFIER.bat`)
**Lecture seule.** Double-clic → vérifie la « règle des 4 éléments » sur toute la production et signale les oublis :
- tweet/article sans `ANIM_DATA` ou sans `LO_BY_KEY` ;
- `melmil_inject_index.js` cassé (virgule manquante → `MASTAURIGE_INDEX = undefined`, MELMIL vide) ;
- clé `MASTAURIGE_INDEX` sans card correspondante ; article `openCard` dont le fichier manque ;
- `article-card` sans `data-camp` ; article sans `shared/back-btn.js`.
Filtre les placeholders (`KEY`, `...`). **À lancer avant chaque export.** *(A déjà détecté un vrai oubli : `@EastWatch_contraoff_blanchiment` sans LO.)*

### 2. Export en 1 clic — `WEB\PS1\CREER_ZIP_AUTO.ps1` (+ `.bat`)
Récupère **tout seul** `index_media/rzo/complet.html` depuis Téléchargements **ou** WEB, les rapatrie, crée le(s) ZIP(s), puis supprime le HTML transitoire. Supprime l'étape « déplacer le fichier à la main ». Les 3 anciens scripts (`CREER_MEDIA/RZO/COMPLET_ZIP.ps1`) restent en secours manuel.

### 3. MELMIL sans Excel — `generate_data.py` (voir table MELMIL ci-dessus)
`MELMIL.xls` est en réalité du **XML (Tableur 2003)** → lu en Python stdlib, plus besoin d'Excel installé, pas de process EXCEL.EXE fantôme. Sortie validée **identique** à l'ancien PS1.

> ⚠ **Source = logiciel GESTIM** (le `.xls` AURIGE 2BB en est l'export). Les **futurs exercices utiliseront d'autres logiciels → d'autres formats**. `generate_data.py` devra donc évoluer en **lecteur adaptatif par type de fichier** (détecter le format en entrée et router vers le bon parseur), tout en produisant toujours le même `melmil_data.js`. À prévoir avant le 1er exercice sur un nouveau logiciel.

### 4. Sauvegarde du rangement — boutons dans `MELMIL_ILI_GUILLAUME.html`
**💾 Sauvegarder le rangement** / **📂 Charger** dans la **barre d'outils MELMIL** (à côté de « ↺ Réinitialiser les positions »). *(Placés ici et non dans index_master : MELMIL est la surface de planification visuelle où l'animateur déplace les cards par glisser-déposer.)* Exporte/réimporte les clés `localStorage` (`card-day-*`, `card-attente-*`, `card-time-*`, `melmil-*`) dans un `.json` portable → l'agencement (jours/heures/en attente/drags) survit à un vidage de cache ou à un changement de PC. `localStorage` est **partagé** entre MELMIL et index_master, donc la sauvegarde couvre les deux. Fonctions `saveArrangement()` / `loadArrangement()` inline en fin de `MELMIL_ILI_GUILLAUME.html` ; styles `.btn-save` dans `melmil.css`. MELMIL étant une page animateur (jamais exportée stagiaire), aucune liste de nettoyage à gérer.

### 5. Ménage
3 fichiers résidus de la migration P-xx/R-x déplacés dans `WEB\MELMIL\_archive\` (`_mapping_final.txt`, `_pr_full.txt`, `_pr_nums.txt`).

> **Idée 6 (reportée après AURIGE 2BB) :** externaliser `ANIM_DATA` + `LO_BY_KEY` hors du monolithe `index_master.html` (447 Ko) vers un `injects_data.js` — diffs Git lisibles, édition plus sûre. À ne faire **qu'entre deux exercices**.

### 6. Gabarit vierge réutilisable (2026-05-31)
**Cible :** `D:\CECPC\PRODUCTION\CREATION\08 - MASTAURIGE VIERGE` — copie de l'outil **vide** (0 card, ANIM_DATA/LO_BY_KEY/MASTAURIGE_INDEX/ROW_MAP/CLASS_MAP/DAY_MAP vides, `MELMIL.xls` = structure 3 feuilles sans données) avec squelette **génériqué** (calendrier J+1…J+10, lignes Acteur 1…7, phases neutres). `index_master` 447 Ko → 82 Ko. Mode d'emploi : `LISEZ-MOI_GABARIT.md` à la racine du gabarit.
**Générateur :** `WEB\OUTILS\creer_gabarit_vierge.py` — reconstruit le gabarit depuis la prod (copie machinerie + vide contenu + généricise + nettoie les commentaires de scénario en gardant les séparateurs `=====`). Réexécutable. ⚠ Strip de `MELMIL.xls` en **texte** (pas ElementTree, qui casse les namespaces SpreadsheetML et rend le `.xls` illisible par `generate_data.py`).
**Pour un nouvel exercice :** copier le dossier, déposer le nouvel export GESTIM `MELMIL.xls`, lancer `Actualiser_MELMIL.bat`, puis reparamétrer 3 fichiers (libellés MELMIL html ; `ROW_MAP`/`CLASS_MAP`/`DAY_MAP` dans melmil.js ; boutons jours + `DAY_OPTIONS` dans index_master).

### 7. Système de versions (2026-05-31)
**Convention `vX.Y`** (`.Y` = petit ajout, `X` = majeur). **On démarre à `v0.1`** ; ⚠ **la `v1.0` sera posée seulement quand l'utilisateur jugera l'outil abouti** — ne pas l'attribuer de soi-même. Au 2026-05-31 : vierge ET AURIGE 2BB = **v0.1**.
**Fichiers :** `MASTAURIGE_VERSION.txt` (racine de chaque instance, = source autoritaire lue par les outils) ; `CHANGELOG.md` (racine du vierge = historique maître) ; version affichée en pied de `index_master.html` + barre `MELMIL_ILI_GUILLAUME.html`.
**Modèle :** le **vierge = référence, porte toujours le dernier numéro** ; chaque exercice est **figé** à sa version de départ. Quand la machinerie évolue → reporter dans le vierge + **bump 3 endroits** (CHANGELOG, VERSION.txt, affichage pied/barre) + ligne de version.
**Outil `OUTILS\COMPARER.bat` (`comparer_au_gabarit.py`, lecture seule) :** compare la machinerie d'un exercice au vierge — affiche les 2 versions, liste les fichiers-moteur identiques/différents/absents (compare à l'octet les fichiers « purs » : OUTILS, PS1, generate_data, melmil.css, back-btn.js ; compare le moteur `melmil.js` en ignorant `ROW_MAP`/`CLASS_MAP`/`DAY_MAP`), et imprime le carnet → indique quoi reporter. Chemin du vierge codé en tête du script (`VIERGE = …08 - MASTAURIGE VIERGE`). Généré dans le gabarit par `creer_gabarit_vierge.py` (qui écrit aussi VERSION/CHANGELOG/LISEZ-MOI).

---

## ⭐ v0.2 — état & évolutions (au 2026-06-04) — FAIT FOI

> Version courante = **v0.2** (`MASTAURIGE_VERSION.txt`). Cette section **fait foi** et **corrige les références périmées plus haut**.

**Chemins / nommage à jour :**
- **Vierge** = `D:\CECPC\MASTAURIGE\LOCALSTORAGE_WEB_VERSION` *(déplacée 2026-06-04 ; ex `D:\CECPC\MASTAURIGE`, ex `…\CREATION\08 - MASTAURIGE VIERGE`)*. Structure : racine `index_master.html` + `Sites/ moteur/ MELMIL/ assets/ shared/ OUTILS/ PS1/`. Cf. [[mastaurige-vierge-chemin]].
- **Générateur** = `OUTILS\GENERER_VIERGE.py` (et **non** `creer_gabarit_vierge.py`). Reset + copie + réécriture `../../` + blanking. ⚠ `empty_obj` **corrigé 2026-06-04** (commentaire-aware) : un `//` avec apostrophe seule faisait déborder le vidage de `LO_BY_KEY` et **supprimait le bloc d'appels d'init** de la vierge (classification/statuts inactifs).
- **MELMIL dans la vierge** = `MELMIL/melmil_ili.html` *(renommé ; reste `MELMIL_ILI_GUILLAUME.html` côté 2BB)*. Le générateur renomme + réécrit le bouton.
- ⚠ Outils à **chemin vierge codé en dur** (ex. COMPARER) : vérifier qu'ils pointent sur le nouveau chemin avant usage.

**MELMIL (melmil.js) — injects CRÉÉS (index_master → localStorage) :**
- Placés à **LEUR propre date** ; si l'incident parent est dans le `.xls` mais à un autre jour → **card-incident créée à la date du sous-inject**.
- **Split par camp** : 1 card par camp présent (🔴/🔵/⚪).
- **Ghost (couleur claire) UNIQUEMENT si l'incident est absent du `.xls`** ; s'il y est → **couleur pleine + nom (sujet) repris du `.xls`**.
- **LO déduite de la série** via `ROW_MAP` (07.05→LO1 · 07.01→LO2 · 07.02→LO3 · 07.03/07.06→LO4 · 07.04→LO5 + overrides incident). ⚠ **Miroir** dans `index_master.html` (`_LO_BY_SERIES`/`_LO_BY_INCIDENT`) — **GARDER SYNCHRONISÉ** si les séries→LO changent (MINAUTORE).
- Bandeau classification (index_master) : le contenu créé affiche **num + LO** (repli `AW/TW.get` / `data-num` quand `ANIM_DATA` vide).

**Vider MELMIL — 2 niveaux :**
- Bouton **ANIMATEUR → « 🗑 Tout vider (session + tableau MELMIL) »** : vide le localStorage (créations/positions/statuts) **et** masque le socle (`melmil-socle-masque` = `updated` du socle ; `socleInjections()` → `[]`). **Réversible** (un nouvel import réaffiche). Navigateur seulement ; localStorage partagé sur **Edge/Chrome**, **isolé sur Firefox** → utiliser Edge/Chrome.
- **`MELMIL/Vider_MELMIL.bat`** : **vrai reset disque** — réécrit `melmil_data.js` à vide + retire `MELMIL.xls` (+ verrou).

**Trombinoscope :** photos centralisées dans **`Trombinoscope/img/`** (auto-contenu `src="img/…"`, fini les `../../../../../../CREATION/…`) — cf. [[trombino-img-convention]]. Page **Bothnia** : drapeau image (dégradé vert→rouge « penchant MER ») + **Tikhanov (Nouvelle Pahonie) / Saniki (Bison Libre)** en opposition pro-MER (camp = ce registre). Layout : région gauche 2/3 (pol+mil) + bande avatars 4 col ; anti-chevauchement (`flex:0 0 auto` + base `flex-shrink:0`).

**Sites médias (templates `_TEMPLATE.html`) :** **TF1 INFO** (logo réel base64 ; hero option « vidéo » avec **bouton play FUYANT** qui revient au centre au `mouseleave`), **Omerta Média** (logo base64), **ZubrRadio.FM** (radio, transcription IA). Garde-fou commun : placeholder `.ph` masqué dès qu'une image est présente.

**Pont statut ↔ ronds MELMIL :** via `card-status-<key>` (même clé index_master ↔ MELMIL). Export/Import session sur MELMIL (`exportSession`/`importSession`) embarque les `card-*` (dont statuts).

**Chaîne « Créer un article » → fichier .html (vérifiée 2026-06-09) :**
Pipeline : créateur (`moteur/createur.js`, bouton FAB `#fabCreerArt` « ➕ Créer un article », onglet **média** uniquement, exige `window.AW`) → `AW.create` (`moteur/articles.js`) → `localStorage["mastaurige-articles"]` → carte injectée au reload (`index_master.html` : `AW.renderHTML()`), clic = **aperçu in-app** (`CR_previewArticle`). Le **.html autonome** (pour Outlook) est produit **côté BASE** par `OUTILS\generer_articles.py` (via `GENERER_ARTICLES.bat`) : lit le `creations_MASTAURIGE_*.json` exporté (bouton **💾 Exporter mes modifs** sur MELMIL), fusionne dans `Sites/<site>/_TEMPLATE.html`, **embarque l'image en base64** + archive l'image décodée dans `Sites/images/`.
- ⚠ **Bug trouvé + corrigé 2026-06-09 (régression v0.2)** : `generer_articles.py` cherchait les gabarits à `racine/Site X/` alors que v0.2 les a déplacés sous `racine/Sites/Site X/` → **0 article généré, même TV4**. Corrigé : `SITES_DIR = WEB/Sites` pour gabarit + sortie + `IMAGES = Sites/images`.
- ⚠ **Sites manquants** : le dict `SITES` ne listait que tv4/bc1/tm/hex (le créateur en propose 8). **Étendu à 9** (tv4, bc1, tm, hex, efs, tf1, omerta, zubr, onu) — **doit rester aligné avec `moteur/articles.js` (mêmes clés + dossiers)**.
- ⚠ **Tokens des gabarits riches** : EFS/TF1/Omerta/ZubrRadio/ONU utilisent des tokens non alimentés par le créateur (`{{AUTHOR}}`, `{{TRANSCRIPT}}`, `{{RUBRIQUE}}`, `{{SIGNATAIRE}}`, `{{ESSENTIEL}}`, `{{PLACEHOLDERS}}`…). Ajout d'un **nettoyage final** `re.sub(r"\{\{[A-Z_]+\}\}", "", out)` → plus aucun `{{…}}` visible. **Limite connue :** ces champs riches restent **vides** tant que le créateur n'est pas enrichi (champs par site) — TODO « créateur enrichi ». TV4/BC1/Today Mercure/Hexagone rendent parfaitement (n'utilisent que les 10 tokens gérés : TITLE/HEADLINE/DECK/KICKER/LOCATION/DATE/HERO/HERO_CAPTION/BODY/TAGS).
- ✅ **Test E2E 2026-06-09** : JSON synthétique (TV4 avec image base64 + TF1 riche) → 2/2 générés, image archivée, échappement HTML OK, 0 token résiduel. Artefacts de test supprimés (vierge laissée pristine).
- ⚠ **2 formats d'export — corrigé 2026-06-09** : le bouton **« 💾 Exporter mes modifs » de MELMIL** produit un fichier **`session_<traitant>_*.json`** (`type:"mastaurige-session"`, clés localStorage brutes dans `data{}`, dont `mastaurige-articles` = **string JSON**), PAS le format plat `creations_MASTAURIGE_*.json` (export du créateur, plus exposé dans l'UI). `generer_articles.py` ne lisait que le format plat → « aucun fichier trouvé ». **Fix** : `find_json` globe aussi `session_*.json` ; fonction `extract_articles(data)` accepte **les 2 formats** (plat → `data["articles"]` ; session → parse `data["data"]["mastaurige-articles"]` + `mastaurige-creations`, dédup par `id`). ✅ Validé sur le vrai `session_BASE_202606091323.json` de l'utilisateur (1 article TV4, image base64, 4 paragraphes, 0 token résiduel).
- ⚠ **`GENERER_ARTICLES.bat`** : `chcp 65001 >/dev/null` (syntaxe Unix) → provoquait « Le chemin d'accès spécifié est introuvable ». Corrigé en `>nul`.
- ⚠ **NE PAS lancer le .bat « en tant qu'admin »** : en élévation, `%USERPROFILE%` peut pointer ailleurs que `C:\Users\MTR` → le script scrute le mauvais dossier Téléchargements. Double-clic **normal** (aucun droit admin requis).

**Créateur enrichi — champs par site (2026-06-09) :**
Les gabarits riches (EFS, TF1, Omerta, ZubrRadio, ONU) ont des tokens que le créateur de base ne remplissait pas. Solution **data-driven** : config **`SITE_FIELDS`** dans `moteur/articles.js` (exposée `AW.SITE_FIELDS`) = `{ site: [ {key,label,type,ph} ] }`. **La clé du champ EST le nom du token `{{KEY}}`** (mapping 1:1). Sites de base (tv4/bc1/tm/hex) = aucun champ extra.
- **createur.js** : modale article → conteneur `#caExtraWrap`/`#caExtra` ; `renderExtra(site, values)` peuple les champs au changement de `#caSite` et à l'ouverture (préremplit en édition depuis `a.extra`) ; `onSaveArt` collecte les `#caX_<KEY>` non vides dans **`f.extra = {KEY: val}`** (stocké tel quel par `AW.create/update`). ⚠ Au passage, **bug latent corrigé** : `set("#caImage",…)` visait un champ inexistant (aurait planté l'édition).
- **generer_articles.py** : après les reps de base, applique `a["extra"]` → tokens, avec **transformations** : `ESSENTIEL` (1 ligne→`<li>`), `CATEGORIES` (mots→`<a href="#">`), `TRANSCRIPT` (paragraphes→blocs `.z-seg`) ; reste = `esc(v)` direct. **Défauts dérivés** : `READ_TIME` auto (~200 mots/min, EFS), `CHAPO`=deck (Omerta), `TRANSCRIPT`←corps si vide + `PLAYER_TITLE`←titre (ZubrRadio), `SIGNATURE`←`SIGNATAIRE` (ONU). `KICKER` extra (Zubr/ONU) **écrase** le KICKER générique ville·date. `{{PLACEHOLDERS}}` n'est pas un champ (mot dans les commentaires des gabarits) — neutralisé par le nettoyage final.
- ⚠ **À garder aligné** : `SITE_FIELDS` (articles.js) ↔ transformations/défauts (generer_articles.py) ↔ tokens réels des `_TEMPLATE.html`. Ajouter un champ = clé dans `SITE_FIELDS` + (si transformation/défaut) handler Python + token dans le gabarit.
- ✅ **Test E2E 2026-06-09** : 1 article par site riche (5/5 générés, 0 token résiduel) — puces TF1, liens catégories Omerta, transcript Zubr depuis le corps, player/signature par défaut, CTA+read_time EFS, réf/signataire ONU. Artefacts supprimés (vierge pristine).
- **TODO restant** : `HERO_CAPTION` Omerta = ville (crédit photo générique) ; transcript Zubr en blocs `.z-seg` sans timecode/locuteur par segment (acceptable v1). Dérive d'étiquette **v0.2/v0.3** (en-têtes createur.js/index_master.html disent v0.3) toujours non tranchée.

**Créateur d'articles — wizard 2 étapes + APERÇU LIVE du gabarit (2026-06-09) :**
Le bouton « ➕ Créer un article » ouvre désormais un **assistant en 2 étapes** :
- **Étape 1 — informations de base** : média/site, camp, incident (+ code auto), jour, heure → bouton **« Suivant → »** (valide le format incident).
- **Étape 2 — contenu + aperçu** : formulaire à gauche (titre, chapô, corps, champs spécifiques au site, image, ville, tags) + **aperçu LIVE du vrai gabarit du média à droite**, qui se met à jour à chaque frappe. Boutons **« ← Retour »** / **« Créer l'article »**.

**Comment l'aperçu fonctionne (contrainte file://) :** impossible de `fetch` un `_TEMPLATE.html` local en `file://`. Donc :
- `OUTILS\generer_templates_js.py` (+ `GENERER_TEMPLATES.bat`) **embarque les 9 gabarits** dans **`moteur/templates.js`** (`window.MASTAURIGE_TEMPLATES = {site: html}`, ~287 Ko).
- **`moteur/render.js`** (`window.AWRender.render(site, article)`) = **port JS de `generer_articles.py`** (mêmes tokens / transforms ESSENTIEL·CATEGORIES·TRANSCRIPT / défauts / cleanup). L'aperçu = `iframe.srcdoc = AWRender.render(...)` (srcdoc = même origine, accessible, pas de fetch ; le `<style>` inline de chaque gabarit rend l'aperçu fidèle).
- `index_master.html` charge **`templates.js` puis `render.js` AVANT `createur.js`** ; les deux sont **ajoutés aux 3 listes de strip export** (`script[src*="templates"]`, `[src*="render"]`) — animateur only, hors exports stagiaires.
- `createur.js` : `readArtForm()` (lit étapes 1+2 → objet article, utilisé par aperçu ET sauvegarde), `setStep()/goNext()`, `refreshPreview()` (debounce 280 ms, délégation `input` sur `#caStep2` → couvre les champs extra dynamiques). CSS wizard dans `createur.css` (`.cr-box-wide`, `.ca-split/.ca-form/.ca-preview iframe`).
- ⚠⚠ **BUILD STEP** : si un `_TEMPLATE.html` change → **relancer `GENERER_TEMPLATES.bat`** sinon l'aperçu est périmé. ⚠ **DEUX moteurs de rendu à garder synchronisés** : `render.js` (aperçu JS) ↔ `generer_articles.py` (.html final côté BASE). Dette acceptée ; convergence future possible = génération du `.html` directement côté client (téléchargement) pour retirer l'étape Python.
- ✅ **Tests 2026-06-09** : `node --check` OK sur articles.js/render.js/createur.js/templates.js ; rendu des **9 sites → 0 token résiduel**. Reste à valider en navigateur (UX wizard + aperçu visuel).

**Génération du .html côté NAVIGATEUR (2026-06-09) :**
Le `.html` autonome peut désormais être produit **directement dans le navigateur** via `render.js` (plus besoin de l'étape Python pour un article unique). `createur.js` : `downloadArticleHtml(a)` (Blob → `<a download>`), `articleFileName(a)` (= basename de `AW.fileFor`, le dossier cible se range à la main car le navigateur télécharge dans *Téléchargements*), `window.CR_downloadArticle(id)`.
- **Boutons fusionnés (2026-06-09)** : le bouton primaire de l'étape 2 fait **les deux** — « ✅ Créer l'article + .html » (création) / « Enregistrer + .html » (édition) : `onSaveArt` enregistre la carte (`AW.create/update`) **puis** `downloadArticleHtml(...)`, avec `location.reload()` **différé de 600 ms** pour laisser le téléchargement démarrer. *(Raison : créer un article implique toujours d'en vouloir le .html — pas de bouton de téléchargement séparé dans la modale.)* **Bouton « 📄 .html »** conservé sur `artTools` (cartes d'articles créés) → re-télécharger à tout moment sans re-enregistrer.
- ✅ **Test d'équivalence 2026-06-09** : même article (TF1, champs riches) généré par `render.js` (navigateur) **vs** `generer_articles.py` (BASE) → **contenu identique ligne à ligne** (seul écart = fins de ligne LF vs CRLF, sans incidence).
- **`generer_articles.py` reste utile** pour le **batch** (générer tous les articles d'un export `session_*.json`/`creations_*.json` d'un coup) et l'**archivage image** dans `Sites/images/`. Les deux chemins doivent rester synchronisés (cf. règle render.js ↔ generer_articles.py).

**Créateur d'articles — plus de téléchargement .html automatique (2026-06-10, demande utilisateur) :**
Le clic « Créer » ne télécharge PLUS le `.html` dans Téléchargements (source de confusion : ce fichier ne sert à RIEN dans la chaîne MASTER, qui régénère elle-même les `.html` des paquets joueurs depuis les données du session export). Boutons renommés : **« ✅ Créer l'article »** / **« Enregistrer »** (sans « + .html ») ; `onSaveArt` → `AW.create/update` + `location.reload()` direct (plus de setTimeout 600 ms qui attendait le téléchargement). **Conservé** : `downloadArticleHtml()` + bouton **« 📄 .html »** sur les cards (`CR_downloadArticle`) = obtention du fichier À LA DEMANDE (usage : envoi Outlook direct d'un article isolé, hors circuit joueurs).

**WYSIWYG hybride — édition dans l'aperçu (2026-06-09) — ❌ ABANDONNÉ le 2026-06-10 (préférence utilisateur) :**
> **Retour au modèle « formulaire complet à gauche / aperçu LECTURE SEULE à droite ».** `createur.js` : champs Titre/Chapô/Corps restaurés dans le formulaire (`#caTitle`/`#caDeck`/`#caBody`), `renderExtra` remontre TOUS les champs du site (plus de filtre STRUCTURED/TEXT_EXTRA), `readArtForm()` relit tout le formulaire, aperçu rendu en mode **plain** (`AWRender.render(site, article)` sans `{editable:true}`) ; supprimés : `buildArticle`/`readZones`/`previewDoc`/`artInitial`/`_artZonesReady`/constantes EXTRA. **Le mode `{editable:true}` de `render.js` reste dans le code mais n'est plus appelé nulle part** (inerte — le retirer si un jour on nettoie render.js). Préremplissage édition = via les champs du formulaire. ✅ node --check + rendu plain testé (0 contenteditable/data-tok/token). Le § ci-dessous est conservé pour HISTORIQUE uniquement :
À l'étape 2, les **textes s'éditent directement dans la maquette** (aperçu), le formulaire de gauche ne garde que l'**image**, la **ville**, les **tags** et les **champs structurés** du site.
- `render.js` a un **mode `{editable:true}`** (aperçu uniquement) : il enveloppe la **1ʳᵉ occurrence** des tokens TEXTE dans `<span class="awz" data-tok="KEY" contenteditable>` (et BODY dans un `<div>`), + un `<style>` de surbrillance. Tokens texte = `WRAP_INLINE` (HEADLINE, DECK, CHAPO, INTERTITLE, AUTHOR, CTA, HERO_TEXT, SOURCE, CATEGORY, SHOW, DURATION, TIMECODE, RUBRIQUE, PLAYER_TITLE, KICKER, REF, SIGNATAIRE, FONCTION, SIGNATURE) + BODY. **Le mode plain (téléchargement / Python) est inchangé** → le `.html` final ne contient aucun `awz`/`data-tok`. ⚠ Pas d'annotation des gabarits : le wrap est auto-injecté au rendu.
- `createur.js` : `STRUCTURED_EXTRA` (ESSENTIEL, CATEGORIES, TRANSCRIPT, PREV_TITLE, NEXT_TITLE) restent au formulaire (`renderExtra` les filtre) ; `TEXT_EXTRA` édités in-place. `readZones(iframeDoc)` relit les `[data-tok]` (BODY → `<p>` joints en paragraphes) ; `buildArticle()` = `readArtForm()` (base) **+** zones (ou `artInitial` si l'aperçu pas encore prêt). `doRenderPreview()` rend en `{editable:true}` ; `_artZonesReady` passe à true au 1ᵉʳ `iframe.onload`.
- **Astuce architecture** : l'aperçu est un **iframe = document séparé** → éditer dedans **ne bulle pas** vers le listener `input` de `#caStep2` (donc pas de re-rendu / pas de saut de curseur en frappe in-place) ; seules les modifs du **formulaire** déclenchent un re-rendu, qui lit d'abord les zones (préserve les éditions) puis reconstruit. Sauvegarde/téléchargement passent par `buildArticle()`.
- ✅ **Tests 2026-06-09** : `node --check` OK ; rendu editable = 0 token résiduel + zones `data-tok` éditables ; rendu plain = 0 `data-tok`/`awz` (final propre). ⚠ **Interactif (contenteditable, relecture iframe, seed/ready) à valider en NAVIGATEUR.**

**⭐ PIPELINE « INJECT AS CODE » — production de masse par plan déclaratif (2026-06-10) :**
Nouveau chemin BATCH pour la chaîne IA (complète le wizard unitaire, ne remplace rien) : un **plan JSON** décrivant N injects → `OUTILS\generer_injects.py` (+ `GENERER_INJECTS.bat`, modèle `PLAN_INJECTS_EXEMPLE.json`) → produit un **`session_<traitant>_*.json`** au format EXACT de « 💾 Exporter mes modifs » → import en 1 clic via **« Importer » de MELMIL** (fusion par id, non destructif) ; les `.html` Outlook des articles sortent ensuite par `GENERER_ARTICLES.bat` sur ce même fichier (testé : il lit les sessions du pipeline).
- **Validations en amont** (remplacent la checklist 4+1) : avatar ∈ `avatars.js` + **camp rouge↔bleu contradictoire = ERREUR bloquante** (CONTROLE G amont, façade neutre = warning) · site ∈ SITES + champs `extra` ∈ SITE_FIELDS · incident `XX.YY.ZZ[Z]` (tirets 7BB `07-01-10` normalisés en points) · **lettre de code auto** (port Python de `TW.nextCode`, scan tweets_data + melmil_inject_index + melmil_data + index_master + le plan) ou `code` explicite (collision = erreur) · dayorder ∈ onglets index_master (libellé `time` lu des onglets, ex. `04 Jun — 07h30`) · heure `HHhMM` · LO ∈ 1..5 **ou déduite de lo_config.js** (incident > série ; séries HN → pas de LO) · image embarquée base64 (`imageData`) · langue avatar si propriété `langue` posée dans avatars.js (optionnelle). Erreurs → exit 1, **aucun fichier produit**.
- Objets générés conformes au moteur : tweets → `mastaurige-creations.tweets` (forme canonique TW, id `IA_tw_*`, avatar résolu du registre) ; articles → `mastaurige-articles.articles` (forme AW, `file` via port de `fileFor`/`slug`).
- ⚠ **Limite connue** : les créations vivant uniquement dans le localStorage d'un navigateur ne sont pas visibles du scan de lettres → fixer `"code"` explicite en cas de doute ; CONTROLE H reste le filet aval.
- ✅ **Tests E2E 2026-06-10** : 3 tweets + 2 articles (dont ONU + image base64 + champs riches) → bundle conforme `isModKey`/COLLECTION_KEYS, lettres partagées par incident (Ai/Bi), ids uniques, `GENERER_ARTICLES.bat` 2/2 .html 0 token ; 6 cas d'erreur tous bloqués. Artefacts supprimés, vierge pristine (VERIFIER ✅).

**⭐ lo_config.js — SOURCE UNIQUE séries→LO (2026-06-10) — fin du miroir flaggé « GARDER SYNCHRONISÉ » :**
- Nouveau **`moteur/lo_config.js`** (`window.MASTAURIGE_LO = { series, incidents, sphereBlue, paysDelegitime }`, valeur `"HN"` = ligne Host Nation r6 sans badge LO).
- **`MELMIL/melmil.js`** : `ROW_MAP`/`INCIDENT_LO`/`SPHERE_BLUE`/`PAYS_DELEGITIME` désormais **dérivés** de la config (repli console.warn + Ghost si script absent). **`index_master.html`** : `_LO_BY_SERIES`/`_LO_BY_INCIDENT` supprimés, `loFromNum()` lit la config. `generer_injects.py` la lit aussi (LO par défaut).
- Chargement : `index_master.html` (`moteur/lo_config.js` avant tweets_data) + `melmil_ili.html` (`../moteur/lo_config.js` avant melmil.js). **Pas dans les listes de strip export** (donnée neutre, les exports la gardent).
- ✅ Corrige une **divergence avérée** du miroir : l'override `08.03.04→LO4` existait dans melmil.js mais pas dans index_master. **Pour MINAUTORE/7BB : adapter le mapping séries→LO = éditer UNIQUEMENT lo_config.js.**

**Correctifs 2026-06-10 :**
- `moteur/articles.js` : **site `onu` ajouté à SITES** (code ONU, dossier `Site ONU`, prefix `ONU_`) — le créateur le proposait mais `fileFor` retombait en silence sur TV4 (mauvais dossier/logo). Aligné avec `generer_articles.py` (9 sites partout).
- `GENERER_VIERGE.py` (côté 2BB) : **GARDE-FOU anti-rollback** — refuse de tourner sans `--force-rollback`. Raison : la vierge est la **référence vivante** (templates.js/render.js, articles.js v0.3, createur wizard, outils 09-10/06 **absents du 2BB source** — `MOTEUR` ne liste même pas templates/render) ; une régénération écraserait tout cela avec les versions périmées du 2BB.
- **⭐ INSTANCE MASTAURIGE AURIGE 7BB / MINOTAURE 26 (créée 2026-06-10)** : 3 dossiers dans `D:\CECPC\PRODUCTION\EXER\AURIGE 7BB\00_Boites à outils\MASTAURIGE\` = **`LOCALSTORAGE_WEB_VERSION`** (traitants) + **`JOUEURS_WEB_VERSION`** (kit généré) + **`EXE_MASTER_VERSION`** (console). **Noms identiques à la vierge globale** → les chemins RELATIFS de `MASTER.py` (RACINE=parent, WEB=RACINE/LOCALSTORAGE_WEB_VERSION) et `GENERER_KIT_JOUEURS.py` (DST=sibling) fonctionnent **sans modif de code**. `EXERCICE.txt` = « MINOTAURE 26 — AURIGE 7BB ». Copié depuis la vierge globale puis configuré 7BB.
  - **Config 7BB appliquée** : `moteur/lo_config.js` (07-01→LO2, 07-02→LO3, 07-03→LO4, 07-04→LO5 ; `paysDelegitime:"ARN"` ; sphereBlue vide) · `MELMIL/melmil.js` **DAY_MAP** réécrit (9 jours **D+33→D+41 = 23 Jun→01 Jul 2026**, dayorder = valeur D+, COL_TO_DAY explicite) · `MELMIL/melmil_ili.html` **thead + colgroup + tbody régénérés** (9 colonnes, phases CAX1 franchissement / CAX1 ATK MDL / CAX2 reconquête, libellés LO 7BB, `group-sep colspan=11`) · **onglets jours index_master + DAY_OPTIONS** = D+33→D+41 · `melmil_data.js` **socle = 18 incidents** de l'Event List 13/03 (07.01.01-11, 07.02.01-03, 07.03.01-03, 07.04.01, etat Draft, repères de phase à affiner par drag). Titres/headers « AURIGE 7BB / MINOTAURE 26 ». ⚠ **Camps INVERSÉS** (entraînés = BLEU).
  - ✅ Vérifié : syntaxe JS OK, **dayorder 33..41 aligné partout** (onglets ↔ DAY_MAP ↔ cellules tbody), VERIFIER « TOUT EST BON », console MASTER 7BB tourne sur son instance. ⚠ Validation NAVIGATEUR du MELMIL 7BB (rendu tableau 9 colonnes, drag) à faire.
  - **Sous-injects à créer** : 07.02.10-13/20-23/30-33, 07.03.10-13/20-22/30-35, codes 07-04 à numéroter (cf. MINAUTORE/MEMOIRE § inventaire injects). Production = 0 inject (cards apparaîtront via le créateur).

- **Correctifs créateur d'articles (2026-06-10, demandes utilisateur)** : voir § « Créateur d'articles » plus bas (retour formulaire/aperçu lecture seule ; suppression du téléchargement .html auto ; rangement .json des actus dans `ACTUS\` ; bouton Publier réservé BASE + auto-statut Envoyé). Ces évolutions sont dans la **vierge globale** ET héritées par l'instance 7BB (copie postérieure).

- **⭐ SYSTÈME DE CONFIG PAR EXERCICE — `exercice_config.json` + `CONFIGURER_EXERCICE.py` (2026-06-10, demande utilisateur)** : auparavant la vierge contenait les données 2BB de GUILLAUME (LO, storylines, dates, socle) — **pas vraiment vierge**. Désormais **un seul fichier éditable** `exercice_config.json` (racine de l'instance) décrit tout ce qui change par exercice : `nom, sousTitre, dateDebut, premierDPlus, nbJours, campsInverses, paysDelegitime, series{serie→LO}, incidents, sphereBlue, lignes{r1..r7 sous-libellés}, phases[{span,cls,titre,sub}]`. Le script **`OUTILS\CONFIGURER_EXERCICE.py` (+ .bat)** en dérive **automatiquement** : `moteur/lo_config.js` (généré, ne plus éditer à la main), `MELMIL/melmil.js` DAY_MAP, `MELMIL/melmil_ili.html` (colgroup + thead phases/dates/D+ + tbody lignes LO + titres), `index_master.html` (onglets jours + DAY_OPTIONS + title). **Idempotent**, relançable. Les **titres de lignes LO sont canoniques GLM26** (fixés dans le script) ; seul le sous-libellé varie. Jours générés depuis dateDebut+premierDPlus+nbJours (dow/dates/D+ calculés). **Ne touche PAS** au contenu produit ni au socle `melmil_data.js`.
  - **Vierge globale NEUTRALISÉE** : `exercice_config.json` neutre (D+1→D+10, séries vides, phases « À CONFIGURER », `paysDelegitime XXX`) appliqué → **0 trace 2BB** (vérifié : plus de Ruthnia/HSARREBOURG/GUILLAUME/07.05/DAC). Socle `melmil_data.js` vidé (`injections: []`).
  - **Workflow nouvel exercice** : éditer `exercice_config.json` → `CONFIGURER_EXERCICE.bat` → (option) `GENERER_KIT_JOUEURS.py`. Plus aucune édition manuelle de melmil.js/melmil_ili.html/index_master.
  - L'instance **7BB** a son propre `exercice_config.json` (D+33-41, 07-01..04→LO2..5, ARN, camps inversés, phases CAX1/CAX2) — régénérable à l'identique par le script. ✅ Testé E2E sur les 2 instances (vierge + 7BB), syntaxe JS OK, dayorder aligné, kits régénérés.
  - ⚠ Les **ancres regex** du script dépendent de la structure de melmil.js/melmil_ili.html/index_master — si on refactore ces fichiers, vérifier que CONFIGURER retrouve ses blocs (warnings `!` explicites sinon).

- **Allègement images (2026-06-10)** : (1) **trombinoscope** — l'utilisateur a recompressé `Sites/Trombinoscope/img/` en `.jpg` ; les 10 références `.png`/`.jpeg` cassées dans `ACTEURS_A3_model.html` ont été réalignées sur les `.jpg` présents (18 refs, 0 cassé, 0 orphelin, 2 instances). (2) **avatars tweet** — `assets/images/avatars tweet/` recompressé en JPG 200 px q82 : **2,6 Mo → 28 Ko** par instance. Seuls 2 des 5 avatars étaient câblés dans `avatars.js` (Saniki, Tikhanov, déjà petits) ; les 3 lourds (Gavrilov/Kolesnikov/Makarov ~2,5 Mo) n'étaient référencés nulle part (ajoutés en prévision) — gardés mais allégés. `avatars.js` mis à jour (`img: ....png` → `.jpg`). **Choix retenu = recompression dédiée (Option A), PAS réutilisation des images trombino (Option B écartée : couplerait moteur tweets + MASTER + kit pour économiser 5 petits fichiers).** Les avatars restent affichés via `./images/avatars tweet/<fichier>` (chemin moteur inchangé). Kits joueurs régénérés.

- **Guide joueur PowerPoint (2026-06-10)** : `GUIDE_JOUEUR_MASTAURIGE.pptx` (7 slides, 16:9, ~39 Ko) produit dans chaque kit JOUEURS — explique aux joueurs ce qu'est MASTAURIGE (fil actu média + tweets), l'ouverture (double-clic index_master.html), et les **2 étapes à chaque paquet reçu** : (1) extraire le `ACTUS_*.zip` dans le dossier du kit, (2) « 📥 Importer les actus » → dernier fichier de `ACTUS\`. Généré par `OUTILS\generer_guide_joueur.py` (fonction `make(out_dir)`, python-pptx requis — installé poste BASE v1.0.2). **Câblé dans `GENERER_KIT_JOUEURS.py`** (try/except : régénéré à chaque kit puisque le dossier JOUEURS est recréé ; si python-pptx absent → skip sans erreur).
  - **Kit joueur ÉPURÉ (2026-06-10, demande utilisateur)** : suppression du `LISEZ-MOI_JOUEURS.md` (remplacé par le PPTX) ET du marqueur `GENERE_PAR_GENERER_KIT_JOUEURS.txt` (parasites côté joueur). Le garde-fou anti-écrasement du générateur n'utilise plus de fichier marqueur visible mais la **sentinelle `moteur/joueur.js`** (fichier unique au kit) — même sécurité, dossier propre. Contenu final du kit : `index_master.html` + `GUIDE_JOUEUR_MASTAURIGE.pptx` + `ACTUS/` + `Sites/ images/ assets/ moteur/`.

- **Guide ANIMATEUR/TRAITANT PowerPoint (2026-06-10)** : `GUIDE_ANIMATEUR_MASTAURIGE.pptx` (14 slides, 16:9) à la racine de chaque instance traitant (`LOCALSTORAGE_WEB_VERSION`), produit par `OUTILS\generer_guide_animateur.py` (`make(out_dir)`, lancé manuellement — le dossier traitant n'est pas auto-régénéré). Documente chaque bouton réel : header (⚡ MELMIL ILI · 🗂 TROMBINOSCOPE · 🔍 recherche · ANIMATEUR), barre jours (onglets · Cumulatif/Exact · Afficher la classification · En attente · Corbeille), création (➕ Créer un tweet / un article), card (statut En cours/Finalisé/Envoyé · date/heure · Modifier/Supprimer · 📄 .html · ➕ Publier=BASE), MELMIL (drag · Valider/Réinitialiser positions · Exporter mes modifs · Importer fusion), menu ANIMATEUR (🔧 Poste · 🗑 Tout vider), choix du poste **BASE vs T1-T6** au démarrage, cycle complet T→BASE→joueurs. **Slide « Règles d'or »** : ne pas déplacer/renommer le dossier + même navigateur (localStorage).
- **Guide JOUEUR enrichi (2026-06-10)** : slide « Comment ouvrir » complétée des 2 avertissements localStorage (ne pas déplacer/renommer le dossier → sinon tout repasse « NEW » ; rester sur le même navigateur Edge↔Chrome). Mêmes règles d'or dans les DEUX guides (demande utilisateur). Les deux générateurs (`generer_guide_joueur.py` + `generer_guide_animateur.py`) sont dans `OUTILS\` des deux instances ; python-pptx requis (poste BASE v1.0.2).

- **⭐ TROMBINOSCOPE — fiches bio cliquables (pop-up) (2026-06-11)** : `OUTILS\generer_trombino_bios.py` parse 3 fiches bio (`CREATION\06 - Arnland\...20260611...docx` + `CREATION\07 - RUTHNIA BELLA\FICHES BIO\Fiches bio BOTHNIA.docx` + `...Fiche Bio - RUTHNIA BELLA.odt` = en fait **Bothnia** : militaires/opposition/religieux) → **41 fiches** dans `Sites\Trombinoscope\bios.js` (`window.TROMBI_BIOS`, champs nom/role/pays/camp/age/initiales/bio{Parcours,Objectifs,Forces,Faiblesses,Réseaux sociaux}). Puis **injecte un bloc idempotent** (marqueurs `<!-- BIOS:START/END -->`) dans `ACTEURS_A3_model.html` : CSS + overlay pop-up + `bios.js` + script `init()`. Au chargement : les **cartes existantes** deviennent cliquables par **correspondance de nom** (Tikhanov, Saniki, Pallesson… → `tbOpen(id)`), et les **personnes manquantes** sont rendues en cartes dans des sections « addendum » ajoutées à `.page-dr` (Arnland HN : 20) et `.page-br` (Bothnia : 21). Clic = pop-up fiche complète (header coloré par camp, sections). Échap/clic-hors = ferme ; `@media print` masque le pop-up.
  - **Camps = autorité ANALYSTE/registre** : Arnland officiel 🔵, leaders pro-MER 🔴 ; Bothnia état 🟢 neutre ; **Tikhanov/Saniki figés 🔴** (registre MASTAURIGE, post-traitement). Dédup par nom normalisé (bio la plus riche gagne).
  - Appliqué aux **2 instances** (vierge + 7BB). ✅ Testé : bios.js JSON valide, popup JS `node --check` OK, idempotent (1 bloc après 2 runs). ⚠ Validation NAVIGATEUR du rendu pop-up à faire.
  - Bios consignées chez les **propriétaires** : `ANALYSTE_ARN` (§ MAJ 06-11 : 4 maires HTOUL/HMORANGE/HSARRE-UNION/HALBERSTROFF + Volkonsky/Savchenko pro-MER) · `ANALYSTE_BOT` (§ MAJ 06-11 : 12 officiers + Diniz/Schmit/Boerck/Holm + religieux Nyberg/Viklund/Eklund).
  - **⚠ Correction 2026-06-12 (demande utilisateur)** : la 1ʳᵉ version déversait toutes les fiches manquantes dans un **bloc gris « addendum » full-width** ajouté en JS aux pages existantes → cassait la mise en page A3 et donnait l'impression que les sections riches (médias par camp, avatars RS) étaient perdues (elles étaient juste poussées/débordées ; le HTML source n'a JAMAIS été altéré). Corrigé : pages existantes **intactes** (présentation Mercure-style préservée), cartes existantes rendues cliquables ; **matching de nom amélioré** (`stripTitle` retire « Gén./Dr/Lt-général… ») → 15 cartes existantes matchées (Palmquetil/Brrouette/Diniz/Meyer…), plus de doublons. Holm (Nortek) reclassé en institutions (« général » dans « directeur général » captait le militaire). `groupe` ajouté au parseur.
  - **⚠ MAJ 2026-06-12 (2e demande) — TOUT sur la MÊME page A3 par pays + rename Arnland** : abandon des pages dédiées séparées → les fiches manquantes sont intégrées en **bande `.bio-band` en bas de la page pays** (`.page-dr` Arnland, `.page-br` Bothnia, avant le footer), organisée par groupe (`bandFor()`). Pour éviter le clip : `.page` passe de **`height:283mm; overflow:hidden`** à **hauteur AUTO + `overflow:visible`**.
  - **⚠ Bug rendu corrigé 2026-06-12 (vérifié jsdom)** : avec `min-height:283mm` + `.page-content{flex:1}`, la zone colonnes remplissait toute l'A3 → la **bande bio était enterrée tout en bas après un grand vide** (≈ une hauteur A3 de scroll) → impression « fiches manquantes ». **Données OK** (audit : 41 fiches toutes placées = 15 cartes existantes cliquables + 26-27 en bandes, 0 perdue, 0 bio vide ; jsdom : 2 bandes, 27 cartes rendues). Fix = `.page` hauteur **auto** (retrait du `height/min-height` 283mm, idempotent 2 états) → la bande suit immédiatement les colonnes. **+ cache-buster `bios.js?v=<timestamp>`** (le navigateur gardait l'ancienne version en cache → cause probable de la perception). ⚠ Conseil utilisateur : **hard-refresh (Ctrl+Shift+R)** après régénération. **Rename « Dacie Romanie/Dacia Romania → Arnland »** dans le trombino des 2 instances (header « Arnland (ARN) », drapeau, rôle CHOD, footer, commentaire) — DR = Arnland (renommé pour Guillaume/2BB). ✅ 0 « Dacie Romanie » restant, sections médias/avatars intactes, node --check OK, idempotent, vierge + 7BB.
  - **⚠ Bug parseur corrigé 2026-06-12 (signalé : « GROOP introuvable »)** : `parse_bothnia_odt()` **sautait 3 officiers** de la 2ᵉ série « haute direction Armée de terre » du `.odt` — **Teemu Kosmannen, Harri Koho, Tyko Groop**. Causes : (1) leur « Nom : X » est suivi **directement de « Parcours »** sans Prénom/Fonction/Intitulé → regex `mn` (« Parcours » absent de ses stops) échouait → `continue` ; (2) **GROOP n'a NI en-tête numéroté NI « Nom : »** (débute par « Parcours :Tyko Groop »). Fix = extraction ciblée par marqueurs uniques (`sub_lines`, normalisation des espaces insécables) → `rec()` complet. **bios.js 41 → 44 fiches**, bande Bothnia 12 → 15. Doctrine ANALYSTE_BOT **déjà correcte** (12 officiers) — seul le trombino les perdait. ✅
  - **⚠ 4 bugs parseur en cascade corrigés 2026-06-12 (signalés : « faiblesses LINDQUIST manquantes »)** — tous des **fuites/fusions de sections** dans `grab()`/`parse_*` :
    1. **Label `Faiblesses` non reconnu** : le `.odt` écrit « Faiblesses **\xa0**/ défis / préoccupations : » (espace **insécable** DANS le label) → la classe `[A-Za-zÉéÀ-ÿ /]` du regex de `grab()` ne le matchait pas → la section n'était pas détectée → **les faiblesses étaient avalées dans « Forces »** (LINDQUIST : Forces 8 au lieu de 4, Faiblesses absentes). Fix : `l = l.replace("\xa0"," ")` en tête de `grab()`. → +10 fiches avec faiblesses (30→40, puis 42/45).
    2. **Record poubelle « bot_mil_saniki »** : le bloc militaire « 3. » (Koho) n'avait pas d'en-tête suivant → il avalait tout le doc ; `mn` (re.search) sautait « Nom : KOHO » et s'accrochait au 1er « Nom:/Prénom: » en aval = SANIKI → fiche Saniki gonflée (Objectifs 17, Faiblesses 18) gardée par le dédup. Fix : **borner le scan militaire à « OPPOSITION POLITIQUE »**.
    3. **Tikhanov/Saniki** : extraits désormais en **bio complète** (`sub_lines`+`rec()`, Parcours/Objectifs/Forces/Faiblesses/RS) au lieu de Parcours+RS via `block_after`. Camp **rouge** forcé (registre).
    4. **Elena Petrovna polluée (12 faiblesses)** : dans le docx Arnland, l'en-tête **« PATRON DE BORCHENKO TRANSPORTS… »** (Maksym Borchenko) n'était pas dans `heads` → son bloc fusionnait dans Petrovna. Fix : ajout de `"PATRON DE "` aux `heads` → **Borchenko devient sa propre carte** (neutre, groupe « Acteurs économiques », double-jeu) + Petrovna nettoyée (Faiblesses 4). Label **« Identité numérique »** ajouté aux `FIELD_LABELS` + fallback RS dans `rec()` (sinon fuyait dans Faiblesses).
    **Résultat : 45 fiches**, 0 suspect de fusion (audit Forces>5/Faiblesses>6/Objectifs>6 = vide), 42/45 avec faiblesses (3 sans = religieux, structure source sans labels). Bandes : Arnland 15 (dont Borchenko), Bothnia 15. node --check OK, idempotent, vierge + 7BB.

- **TODO livrable 3 (axe 1, à faire)** : génération du trombinoscope RS depuis `avatars.js` (ajouter champs pays/bio au registre + script `generer_trombino.py`) — la checklist avatar passerait à « éditer avatars.js + lancer le script ».

**⭐ ARCHITECTURE 3 DOSSIERS `D:\CECPC\MASTAURIGE\` — multi-traitants + joueurs (2026-06-10) :**
| Dossier | Pour qui | Rôle |
|---|---|---|
| `LOCALSTORAGE_WEB_VERSION\` | Traitants | MASTAURIGE animateur complet (référence vivante) |
| `JOUEURS_WEB_VERSION\` | Joueurs (kit jour 0) | Fil d'actus SANS animateur — **GÉNÉRÉ, ne jamais éditer à la main** |
| `EXE_MASTER_VERSION\` | BASE | Console de consolidation (`MASTER.bat`, `_DEPOT\`, `SORTIES\`) |

- **Kit joueurs** : généré par `OUTILS\GENERER_KIT_JOUEURS.py` (marqueur `GENERE_PAR_*.txt`, refus d'écraser un dossier non marqué). Transformations : body sans `data-master` (toute l'init animateur est gatée dessus, vérifié L1987 index_master) ; ancres MELMIL/TROMBINO, badge ANIMATEUR, publish-bar retirés ; **bandeau `day-filter-bar` ENTIER retiré** (demande utilisateur 2026-06-10 : onglets jours + Cumulatif/Exact + bouton « Afficher la classification » — le fil joueur affiche TOUT, mode dayorder 0 par défaut, comme les exports stagiaires ; regex ancrée par lookahead sur `<!-- ===== CONTENU` pour ne pas avaler la page) ; scripts createur/avatars/templates/render/**lo_config** (réponse pédagogique !) déchargés ; garde-fous post-génération sur les ÉLÉMENTS (le CSS/JS conserve des chaînes mortes — ex. libellé « Afficher la classification » dans `toggleClassification`, inerte car le bouton n'existe plus). Conserve : moteurs TW/AW + tweets_data.
- **`moteur/joueur.js`** (nouveau, chargé UNIQUEMENT par le kit joueurs) : bouton « 📥 Importer les actus » **inséré dans `.g-header-right` du header, à gauche de la date** (`insertBefore(firstChild)` — demande utilisateur 2026-06-10 ; repli sous le header si le bloc n'existe pas) ; import = fusion par id/ts dans localStorage, ré-import sans doublon ; **shim `CR_previewArticle`** = viewer iframe `srcdoc` depuis le HTML embarqué (clé LS `joueur-html`) ; post-render : suppression `.camp-badge`/`data-camp` + application avatars/médias base64 (clé LS `joueur-imgs`, préfixes `av:`/`md:` par id de tweet). `GENERER_KIT_JOUEURS.py` : retry anti-verrou Windows sur la recréation du dossier (rmtree « delete pending » quand Explorer/IDE a le dossier ouvert).
- **Console MASTER** (`EXE_MASTER_VERSION\MASTER.py`) : déposer les `session_*.json` traitants dans `_DEPOT\` → fusion par id (ts gagne, conflits signalés) → **RENUMÉROTATION des collisions de codes** (2 traitants créant chacun `07.01.10Ai` dans LEUR navigateur : le plus ancien garde, l'autre reçoit la lettre libre suivante — comble la limite « localStorage invisible » du pipeline) → contrôles camps/LO → sorties : `CONSOLIDE_BASE_*.json` (session à réimporter par chaque traitant) + `actus_J<N>_*.json` (joueurs, filtre jour effectif card-day ≤ N, attente exclu, **épuré camp/lo**, HTML articles + images en base64). `EXERCICE.txt` optionnel = nom affiché. **Importe les briques** `generer_injects` + `generer_articles` (sys.path → vierge OUTILS) — ne pas séparer les dossiers.
- **`generer_articles.py` rendu importable** (refactor sans changement de comportement .bat) : logique de rendu extraite dans **`render_article(a, write_file=True, archive_image=True)`** + `main()` gardé par `__name__`. La console MASTER l'appelle avec `write_file=False` (rend sans toucher au disque de la vierge).
- ✅ **Test E2E cycle complet 2026-06-10** : 2 sessions (ALPHA/BRAVO) en collision volontaire → fusion 3 tweets + 1 article, renumérotation `07.01.10Ai(BRAVO)→Bi`, actus J35 : tweet jour 36 exclu, camp/lo vidés, HTML autonome 0 token avec image base64. Artefacts nettoyés.
- ⚠ Limites v1 actées : épuration camp/lo = valeurs vidées dans le JSON (un joueur outillé dev-tools ne voit rien de plus que dans les exports ZIP) ; statuts de production non filtrés (filtre = jour uniquement) ; packaging `.exe` (PyInstaller) = étape ultérieure optionnelle, la console tourne en `.bat`.
- **🗜 Compression des images (actus joueurs, 2026-06-10)** : `MASTER.py compresser_data_uri()` via **Pillow** (poste BASE v12.2 ; absent → pas de compression + avertissement, rien ne casse). Heros 1200 px JPEG q72 (PNG si transparence), compressé AVANT `render_article` ; avatars 128 px ; médias 1000 px ; jamais plus lourd que l'original. **Le CONSOLIDE traitants garde toujours l'original pleine qualité.** Bilan `🗜` affiché. ✅ Test : PNG 4 732 Ko → JPEG 62 Ko.
- **⭐ MODE FICHIERS des actus joueurs (2026-06-10, demande utilisateur — remplace le tout-embarqué)** : à ~10 articles/jour le json cumulatif embarqué aurait crevé le quota localStorage ET Outlook. Désormais la console produit un **paquet `SORTIES\ACTUS_J<N>_<stamp>\` + son `.zip`** : **`actus_J<N>.json` LÉGER** (cards avec **vignette 320 px q60** ~2 Ko + tweets, épuré camp/LO, `mode:"fichiers"`, `html`/`imgs` vides, **toujours cumulatif**) + **fichiers** `Sites\<Site>\<article>.html` (autonomes, hero 1200 px embarqué) et `images\` (+ `images\avatars tweet\`) aux **chemins natifs du moteur TW**. Routine joueur : **dézipper DANS le dossier du kit (fusionner) → importer le .json** — le localStorage ne stocke plus que les cards (~quelques Ko/jour), les fichiers vivent sur disque, quota réglé à la racine (l'idée IndexedDB abandonnée car inutile).
  - **`joueur.js` viewer** : `Sites/<a.file>` en `iframe.src` (via `AW.get(id).file`) ; **repli** HTML embarqué (`joueur-html`) pour compat anciens paquets ; message d'erreur guidant vers la copie du paquet.
  - **Option `--depuis J`** : fichiers du paquet limités aux jours ≥ J (le .json reste cumulatif) → envois quotidiens légers ; un joueur qui a raté un envoi reçoit un paquet complet (sans `--depuis`). Avertissement « paquet partiel » imprimé.
  - **`compresser_fichier_image()`** : images fichiers recompressées DANS LEUR FORMAT (le nom référencé par `tweet.media`/`avatar.value` ne change pas).
  - ✅ Test E2E : 2 articles (J34/J35, hero 1018 Ko→fichier autonome) + 1 tweet média → json 4 Ko, zip 609 Ko, vignette card 2 Ko, 0 token ; `--depuis 35` = seuls les fichiers J35 dans le paquet, json toujours complet. Projection fin d'exercice (100 articles) : json ~300-400 Ko, html sur disque ~8-10 Mo (hors quota), envois quotidiens deltas de quelques centaines de Ko.
- **⭐ DIFFUSION PAR SÉLECTION « Publié » — envois intra-journée (2026-06-10) :** le filtre par jour était trop grossier (l'animateur envoie 3 injects le matin, 2 plus tard). Le bouton **« + Publier »** d'index_master (qui alimentait « Extraction complète ») est désormais **persisté en localStorage** (`card-pub-<clé>`, clé = `data-twid`/`data-artid`/`data-num` ; `togglePublish`+`initPublishToggles`+`resetPublish` lisent/écrivent) → la sélection **voyage dans « Exporter mes modifs »** (préfixe `card-` déjà collecté). Côté joueur la persistance est **inerte** (init Publier sous le gate `data-master`).
  - **MASTER `--publies`** : sélection = injects dont `card-pub-<clé>='1'` (id OU code) dans le dépôt ; détection auto + prompt « Diffuser cette sélection ? » si des publiés sont présents et pas de `--jour`. **Registre `SORTIES\_DEJA_ENVOYE_<exercice>.json`** = ids déjà expédiés → seuls les **fichiers NEUFS** partent au lot suivant ; le **.json reste cumulatif** (le directeur **ne réinitialise pas** « Publié » entre lots — publié = tout l'envoyé). Le `--depuis` met aussi à jour le registre.
  - **Flux** : (A) consolider traitants → CONSOLIDE, l'importer dans SON animateur ; (B) « + Publier » les injects du lot → « Exporter mes modifs » → `_DEPOT` → `MASTER.bat` (mode publiés) → `ACTUS_J*_PUBLIES_*.zip` ; lot suivant = publier les nouveaux, ré-exporter, relancer. Le **CONSOLIDE traitants est nettoyé des `card-pub-*`** (la sélection de diffusion est une décision BASE, pas une donnée traitant).
  - Horodatage paquets passé à la **seconde** (`%Y%m%d%H%M%S`) — évitait la collision de dossiers entre 2 lots de la même minute.
  - **Rangement des .json d'actus dans `ACTUS\` (2026-06-10, demande utilisateur après test réel)** : le `.json` du paquet va dans un sous-dossier **`ACTUS\`** (nom horodaté `actus_J<N>_<stamp>.json`) au lieu de la racine — chez le joueur les lots successifs s'y rangent au lieu de s'empiler à côté d'index_master.html. Kit joueurs : dossier `ACTUS\` pré-créé vide par le générateur. Réimporter un ancien fichier = sans danger (fusion par id/ts). Dans `SORTIES\`, le dossier non zippé à côté du `.zip` = dossier de construction (vérification/copie USB), supprimable après envoi.
  - **« + Publier » RÉSERVÉ AU PROFIL BASE (2026-06-10)** : `initPublishToggles()` n'est appelé que si `mast-traitant === 'BASE'` (gate dans le bloc data-master) — les traitants T1..T6 ne voient plus le bouton (leur sélection ne peut plus polluer celle du directeur à la consolidation). `CR_pickPoste` fait désormais **`location.reload()`** après changement de poste (l'UI dépendante du profil suit immédiatement).
  - **AUTO-STATUT « ✅ Envoyé » à la publication (2026-06-10)** : `togglePublish` ON → `setStatutEnvoye(card)` écrit `card-status-<k>='envoye'` sur **toutes les clés possibles** (id `data-twid`/`data-artid` = clé MELMIL/panneau créateur · nom de fichier openCard = cards socle · repli titre 30 car. = clé du sélecteur des articles créés — ces 3 systèmes de clés coexistent, hérité) + met à jour le `.card-status-select` visible (`applyStatusStyle`). Résultat : **rond VERT dans MELMIL + « ✅ Envoyé » dans index_master = repère « parti aux joueurs »**. Dépublier ne rétrograde PAS le statut (correction de sélection ≠ rappel de contenu).
  - **Chaîne « Split » SUPPRIMÉE (2026-06-10, validé utilisateur)** : bouton « ✂ Split » + fonctions `generateSplit`/`generateIndexMedia`/`generateIndexRzo` retirés d'index_master (−7 Ko, appariement d'accolades) + `PS1\CREER_MEDIA_ZIP.ps1`/`CREER_RZO_ZIP.ps1` supprimés (orphelins ; récupérables via git). Restent : « 🗂 Extraction complète » (`generateComplet`) + `CREER_COMPLET_ZIP.ps1` + `CREER_ZIP_AUTO` (auto-détecte, branches media/rzo inertes). ⚠ **La règle « 3 listes de nettoyage export » devient « 1 liste »** : tout nouveau bouton animateur ne doit plus être ajouté qu'à la liste de strip de `generateComplet`.
  - ✅ Test E2E 2 lots : lot1 publie art.1-2 → 2 fichiers, registre 0→2 ; lot2 ajoute art.3-4 (1-2 restent publiés) → json **cumulatif 4 articles** mais paquet **= seulement fichiers 3-4**, registre 2→4. Conforme.

**⭐ PISTE « MASTAURIGE COLLABORATIF » — serveur temps réel multi-traitants (PROTOTYPE, 2026-06-16) :**
> Question utilisateur : au lieu que chaque traitant ouvre SON MASTAURIGE et modifie dans son coin (état isolé en `localStorage`), avoir **UN** MASTAURIGE commun, ouvert par tous, **co-édité en temps réel**. Contexte : PC traitants verrouillés (**partage de fichiers seulement**), un **PC Admin** peut héberger une app ; **6–15** traitants simultanés ; besoin = **temps réel**.
- **Constat d'architecture (le verrou)** : MASTAURIGE est 100 % statique, tout l'état vit dans le **`localStorage` du navigateur** (isolé par machine) → **un simple partage de dossier ne partage RIEN** (c'est le symptôme « chacun dans son coin »). Pour du commun+simultané il faut un **serveur** qui détient l'état au centre et le **pousse** aux clients.
- **Modèle retenu** : le **PC Admin fait tourner un serveur** ; les traitants ouvrent juste `http://<IP-Admin>:8765` dans leur navigateur (rien à installer côté traitant). Tout en **LAN, zéro internet**.
- **Stack** : **Python bibliothèque standard uniquement** (aucun pip) — `http.server` + **SSE** (Server-Sent Events) pour le push temps réel + **POST** pour les écritures + **état central `etat.json`** (écriture atomique). Choix SSE (pas WebSocket) car natif navigateur sans dépendance, robuste pour 6–15 éditeurs. Python car déjà l'outillage du projet (Python 3.14 sur le poste).
- **Livrable = PROTOTYPE de faisabilité** dans **`D:\CECPC\MASTAURIGE\SERVEUR_COLLABORATIF\`** (4ᵉ version à côté de LOCALSTORAGE/JOUEURS/EXE_MASTER) : `serveur.py` (~190 l.) + `client_test.html` (compteur + note partagés en direct + présence « N traitants connectés ») + `LANCER_SERVEUR.bat` (auto `py`/`python`, affiche les URL LAN) + `README.md` (test décisif) + `etat.json`. **Ne contient PAS encore MASTAURIGE** — il sert à **prouver d'abord** que le réseau autorise le temps réel.
- **⚠ POINT BLOQUANT À VALIDER AVANT TOUT** : les navigateurs des PC verrouillés doivent pouvoir **joindre un port TCP** (8765) du PC Admin, pas seulement un partage SMB. Le test = ouvrir l'URL depuis un PC traitant ; si le compteur/texte se synchronise entre 2 machines → temps réel validé, on porte MASTAURIGE. Sinon (pare-feu/verrouillage) → temps réel impossible, repli synchro par fichier partagé (non temps réel).
- ✅ **Smoke-test 2026-06-16** : endpoints `/etat`, `/maj` (compteur+note), `/` (client servi 4615 o), persistance `etat.json` OK. SSE non testé en batch (mécanisme standard). Reste : **test 2 machines** (utilisateur) + si OK, **feuille de route portage** (schéma central SQLite par card, remplacer les lectures/écritures `localStorage` du client par appels serveur + abonnement `/flux`, gestion conflit même-card, présence « qui édite quoi », conserver export ZIP stagiaire). Cf. README du dossier.
**⭐ IMPORTATEUR MELMIL UNIFIÉ — GESTIM (.xls) + JEMM (.json) (2026-06-16, demande utilisateur) :**
> Contexte : **JEMM** (nouveau logiciel remplaçant **GESTIM**) exporte la MELMIL en **JSON** (1 fichier = 1 *Event* ; `Data.Events / Storylines / Injections`). Réalise enfin l'évolution « lecteur adaptatif » prévue ligne ~1237. Source réelle 7BB = `E:\09_MTR\D+30_20_Juin\NU_*_JEMM_WUG0N_EVENT_07/08`.
- **Format JEMM** : EVENT_07 = **ILI** (storylines 07.01-07.04, **0 inject** : le rouge ILI reste produit par MINAUTORE) ; EVENT_08 = **HOST NATION** (storylines **08.01** Arnland civil authorities + **08.02** Captured Personnel, **8 injects réels** : requêtes maires HSARREBOURG/HMORHANGE/HTOUL/HSARRE-UNION + redditions MER/CPERS HNANCY/HLUNEVILLE/HALBERSDORF). Champs utiles d'un `Injection` : `Literal` (code), `Name` (sujet), `Description`, `FixedDateTime`, `InjectionMeans.StateOnDelivered.Name` (état), `ReceiverList[].Name` (dest), `Storyline.Literal`.
- **Conversion code** : JEMM `EE.SS.Innn` → MELMIL `EE.SS.nni` (ex. `08.01.I01` → **`08.01.01i`** ; le « I » devient le suffixe « i »). État JEMM `Injected` → `Validated`.
- **Nouvel outil = `MELMIL/generer_melmil.py`** (importateur unifié, stdlib) : `--source auto|gestim|jemm|both` (auto = JEMM si `JEMM/*.json` présents, sinon GESTIM) · `--mode fusion|remplacer` (défaut : **gestim→remplacer** = historique, **jemm→fusion** = additif). **Fusion** : relit le `melmil_data.js` existant, fusionne par `code` (la source gagne) → **le socle ILI fait main n'est jamais perdu**. Chaque inject taggé `"src":"jemm|gestim"`. **Boîte d'arrivée `MELMIL/JEMM/`** (scan récursif des `.json`, dossiers `checksums`/non-JEMM ignorés ; on peut y déposer les dossiers EVENT extraits tels quels). `generate_data.py` (GESTIM seul) **conservé en secours**.
- **Bats** : `Actualiser_MELMIL.bat` réécrit = appelle `generer_melmil.py` (auto) → repli `generate_data.py` → repli `generate_data.ps1` (**GESTIM jamais cassé**) ; nouveau **`Actualiser_MELMIL_JEMM.bat`** force `--source jemm`. `JEMM/LISEZMOI.txt` explique le dépôt.
- **Déployé** vierge globale (`D:\CECPC\MASTAURIGE\LOCALSTORAGE_WEB_VERSION\MELMIL`) **+ instance 7BB** ; les 2 exports JEMM déposés dans la boîte 7BB. Backup `melmil_data.AVANT_JEMM.bak.js` créé côté 7BB.
- ✅ **Tests 2026-06-16** : 7BB `--source jemm` → **18 ILI (socle préservé) + 8 HN = 26 injects**, tous datés, codes/dest corrects. Non-régression GESTIM : `generer_melmil.py --source gestim` vs ancien `generate_data.py` sur le même `.xls` = **48 = 48, 0 différence de contenu**. ⚠ **À valider en NAVIGATEUR** (rendu des cards 08.xx).
- ✅ **ROUTAGE TRANCHÉ (2026-06-16) — ligne HOST NATION dédiée (r6)** : choix utilisateur = r6 devient une vraie ligne **HOST NATION** (les opportunités EXCON, pas encore des injects, passent sur r7). Implémenté : **titre canonique r6** dans `OUTILS\CONFIGURER_EXERCICE.py` `LIGNES` = `("r6","#1B5E20","HN","HOST NATION")` (était `OPP / "OPPORTUNITÉS / HN"`) ; r7 = `("✦","GHOST / OPP")`. **7BB `exercice_config.json`** : `series` += `08-01/08.01/08-02/08.02 → "HN"` (→ ROW_MAP `HN`→r6, sans badge LO) ; sous-libellés r6 = « Autorités civiles ARN (08.01) · CPERS (08.02) », r7 = opportunités EXCON + hors-plan. **Régénéré** via `CONFIGURER_EXERCICE.py` (lo_config.js + melmil_ili.html + index_master) sur **7BB + vierge**. ✅ Vérifié : melmil_ili 7BB affiche « HOST NATION », 0 label « OPPORTUNITÉS / HN » résiduel, lo_config route 08.xx→HN. Codes melmil_data inchangés (08.01.01i…) → atterrissent sur r6.

**⭐ ACCÈS SANS IP — raccourci cliquable (2026-06-16, demande utilisateur)** : les traitants ne doivent ni taper ni connaître d'adresse IP. Solution = le serveur **génère au démarrage un raccourci Windows `OUVRIR_MASTAURIGE.url`** (`ecrire_raccourci()`) pointant sur le **NOM du PC Admin** (`http://<hostname>:8765`, stable même si l'IP DHCP change), à **copier dans le dossier partagé** ; le traitant **double-clique** → navigateur ouvert sur le MASTAURIGE commun. ⚠ **Le dossier partagé porte le RACCOURCI, pas l'appli qui tourne** : la co-édition exige le serveur en marche sur le PC Admin ; « accès au partage SMB » ≠ « joindre le port réseau » → le test 2 machines reste le juge. Confort possible : démarrage auto du serveur (tâche planifiée / dossier Démarrage). `.bat` : `chcp 65001` ajouté ; `serveur.py` : `sys.stdout.reconfigure(utf-8)` + marqueurs ASCII `>>` (le `►` plantait la console cp1252). ✅ Raccourci généré OK (`URL=http://LAPTOP-TLLASRTF:8765`), bannière sans crash.

**⭐ PC ADMIN SANS PYTHON → Python PORTABLE embarqué (2026-06-17, test terrain) :** 1er essai sur le **PC Admin** du réseau traitants (≠ poste dev VSCode ; copié par clé USB) → `.bat` échoue « **Python absent** ». Solution = **Python embeddable** (python.org `python-3.12.7-embed-amd64.zip`, ~11 Mo, stdlib complet en `.pyc` dans `python312.zip` — http.server/socketserver/json/queue/threading/urllib/socket vérifiés présents, **aucun pip/aucune install**) **dézippé dans `SERVEUR_COLLABORATIF\python\`**. `LANCER_SERVEUR.bat` réécrit : ordre = **(1) `%~dp0python\python.exe`** (portable livré) → (2) `py` → (3) `python`. → copier tout le dossier (avec `python\`) par USB sur le PC Admin, double-clic, **rien à installer**.
- ⚠ **Non testable sur le poste dev** : sa **politique de sécurité bloque l'exécution de tout `.exe` non approuvé** (AppLocker/WDAC/AV) — `python\python.exe` y donne « Accès refusé » **même après `Unblock-File`** (≠ MOTW). Le `py` système y marche car installé/approuvé. **Le test réel se fait sur le PC Admin.** Comme un **`.exe` PyInstaller serait bloqué pareil** (binaire non approuvé) + risque faux positif AV, le portable est préféré.
- **Plan B si le PC Admin REFUSE aussi `python\python.exe`** (erreur « Accès refusé » ≠ « Python absent ») : (1) IT installe/autorise Python ; ou (2) **héberger sur un autre poste du réseau traitants ayant déjà un Python approuvé** + allumé (le raccourci `.url` se régénère au nom du poste hôte). Documenté dans `SERVEUR_COLLABORATIF\README.md`.

**⭐⭐ INTÉGRATION MASTAURIGE → COLLABORATIF TEMPS RÉEL (2026-06-17) — Phases 1 & 2 faites :**
> Objectif utilisateur : **100 % de l'état MASTAURIGE partagé en temps réel** entre 6-15 traitants, sans bug, avec relance/sauvegarde anti-plantage. Instance choisie : **AURIGE 7BB**, copiée dans `SERVEUR_COLLABORATIF\mastaurige\` (l'originale 7BB n'est pas touchée).
- **Pivot — réutilisation du modèle Export/Import existant** (`melmil_ili.html` § sync) : ce qui se partage = le **« mod layer »** = `isModKey(k)` = clés `card-*` + **`COLLECTION_KEYS`** (`mastaurige-articles/creations/edits/art-edits`, `melmil-subinj`, `melmil-gg-positions`, fusion **par id** via `mergeCollection`/`mergeById`). **LOCAL par machine, jamais partagé** : `mast-traitant` (identité du poste !), `mast-sync-base`, `aurige2bb_viewed`, `melmil-gg-version-2`, `melmil-valide`. → la couche collab ne réinvente rien, elle synchronise ce mod layer.
- **PHASE 1 — `SERVEUR_COLLABORATIF\serveur.py` réécrit** (stdlib) : (1) **sert** le dossier `mastaurige\` en HTTP (les traitants ouvrent `http://<PC-Admin>:8765/` = index_master, **plus le fichier local** — obligatoire pour temps réel : même origine + état central) ; (2) **magasin clé-valeur** du mod layer, **fusion collections par id côté serveur** (port Python de `mergeCollection`) ; (3) **SSE `/flux`** pousse chaque `maj` à tous ; (4) **persistance atomique `etat_mastaurige.json` à chaque écriture + sauvegardes horodatées `backups\` (thread, 5 min, 60 gardées) + restauration auto** si le store est corrompu. Endpoints : `GET /` (+ statiques), `GET /etat`, `POST /maj` {key,value,op,clientId} (refuse les clés non-mod), `GET /flux`, `GET /sante`. `LANCER_SERVEUR.bat` = **boucle de relance auto** (replante → relance 3 s ; fermer la fenêtre pour arrêter) + python portable prioritaire.
- **PHASE 2 — `mastaurige\collab.js`** (chargé **en TOUT PREMIER** par `index_master.html` et `MELMIL\melmil_ili.html` via `../collab.js`) : (1) **amorce synchrone** (XHR `/etat`) → localStorage avant que l'appli lise ; (2) **enveloppe `localStorage.setItem/removeItem`** → POST `/maj` pour les clés mod (garde `applyingRemote` anti-boucle ; `mast-traitant` reste local) ; (3) **EventSource `/flux`** : applique les `maj` distantes (ignore son propre `clientId`), `etat` à la reconnexion = resync complet ; (4) **rafraîchissement MVP = `location.reload()` différé 1 s, JAMAIS si un éditeur est ouvert** (`.cr-overlay` visible ou focus input/textarea/contenteditable → on repousse) ; (5) **badge bas-gauche** « 🟢 Collaboratif — N connecté(s) / 🔴 Hors-ligne ».
- ✅ **Tests 2026-06-17** (sans navigateur) : serveur sert index_master (83 Ko) + moteur/*.js ; scalaires `card-*` OK ; **fusion 2 traitants art1+art2 sans écrasement** ; `mast-traitant` refusé (reste local) ; persistance disque ; **chaîne SSE temps réel prouvée** (Viewer reçoit la `maj` d'un autre client) ; `collab.js` `node --check` OK.
- ⏳ **RESTE À FAIRE** : (a) **valider en NAVIGATEUR** sur 2 machines (amorce, écriture↔écriture, reload, badge) ; (b) **Phase 3** = rafraîchissement **fin sans reload** (re-rendu ciblé cards/MELMIL) ; (c) **Phase 4** = présence « qui édite quoi » + verrou visuel par card + bouton « restaurer une sauvegarde » + doc. ⚠ Le prérequis réseau (navigateurs traitants qui joignent le port du PC Admin) reste à confirmer.
- **🐛 Correctif 2026-06-17 — « le serveur redémarre en boucle »** : le `.bat` prioritisait le `python\` portable ; sur un poste qui **refuse** ce binaire (politique de sécu → « Accès refusé »), lancement instantanément raté → relance → boucle. **Fix `LANCER_SERVEUR.bat`** : (1) ordre **py système → python système → portable**, chacun **testé `-c "pass"`** avant d'être retenu (on ne choisit qu'un Python qui s'exécute vraiment) ; (2) si aucun → message clair + `pause` (plus de boucle) ; (3) après arrêt du serveur, **`choice /C RQ /T 15 /D R`** = 15 s pour lire l'erreur, **Q pour quitter** (fin de la boucle aveugle). **`serveur.py`** : bind du port dans un `try/except OSError` → message clair « port déjà utilisé » au lieu d'un crash. + docstring `python\ ` → SyntaxWarning Python 3.14 corrigé.
- **🐛 Correctif 2026-06-17 — comptage des connectés faux** (cliquer « MELMIL » incrémentait le compte) : **chaque page = 1 flux SSE**, et l'ancien flux d'`index_master` traînait jusqu'au battement avant nettoyage → compte gonflé. **Fix** : identifiant **par FENÊTRE** via `sessionStorage` (`collab-tab-id`, stable quand on navigue index↔MELMIL dans la même fenêtre, distinct entre fenêtres), passé en `/flux?...&id=TAB` ; **`presence()` compte les `id` DISTINCTS** (pas les flux bruts) → `{count, noms, flux}`. Battement SSE **15 s → 5 s** (détection plus rapide des fenêtres fermées). ✅ Testé : 2 flux même id = count 1 (+observateur = 2). **Port configurable** : `PORT = MAST_PORT env` (défaut 8765). ⚠ Le compte retombe avec ~5 s de latence (normal = délai de battement).
- **⚡ Correctif 2026-06-17 — LENTEUR de chargement des pages** (signalée même sur poste puissant). Diagnostic chiffré : `/` via **`127.0.0.1` = 16 ms** mais via **`localhost` = 2033 ms**. **Cause racine = double pile IP** : `localhost` (et les noms de machine) résolus en **IPv6 `::1` d'abord**, or le serveur n'écoutait qu'en **IPv4 `0.0.0.0`** → tentative IPv6 qui échoue (~2 s) puis repli IPv4, **à chaque nouvelle connexion**. **Fix principal = `ServeurDualStack`** (écoute `::` avec `IPV6_V6ONLY=0` → IPv6 **et** IPv4 ; repli IPv4 pur si IPv6 indispo) → **2033 ms → 29 ms**. Corrections de perf complémentaires : `protocol_version="HTTP/1.1"` (**keep-alive**), `wbufsize=64K` + **`TCP_NODELAY`** dans `setup()` (supprime les pauses Nagle/ACK différé — `templates.js` 287 Ko : ~690 ms → **2 ms**), **`Last-Modified` + 304** (revalidation conditionnelle → on ne re-télécharge que ce qui a changé, crucial vu le refresh-par-reload), **table MIME fixe** (évite l'init lente de `mimetypes` lisant le registre Windows). ✅ Mesuré : page principale ~15-30 ms, fichiers en cache → 304. ⚠ La lenteur n'était PAS un problème de machines (ce serait pareil/pire sur le LAN) ; le refresh-par-reload reste lourd → **Phase 3** (re-rendu sans reload) l'éliminera.
- **📄 Déploiement / IT (2026-06-18)** : `SERVEUR_COLLABORATIF\NOTE_IT.md` = note de réassurance pour l'administration système (à transmettre avant déploiement) — prouve que l'outil est **local, autonome, sans installation, sans Internet, sans droits admin, limité à son dossier + 1 port (8765)**, auditable (serveur.py ~300 lignes lisibles, seul `.exe` = Python officiel python.org vérifiable au SHA-256). `.gitignore` ajouté (exclut `python\`, `etat_mastaurige.json`, `backups\`, `OUVRIR_MASTAURIGE.url`). **En attente des accords admin avant déploiement sur le serveur.**

**⭐ PHASE 3 — rafraîchissement FIN (sans reload) + PHASE 4 — présence d'édition & sauvegardes (2026-06-18) :**
- **Phase 3 (`collab.js`)** : sur une `maj` distante, **mise à jour EN PLACE sans reload** pour les actions fréquentes — `card-status-*` (met à jour le `<select>` + style via dérivation de clé identique à index_master : `markTweet`/`openCard`/titre) et `card-pub-*` (bouton Publier). **Repli automatique sur un reload DOUX** (jour/attente/heure, collections, ou card non trouvée) qui **préserve le scroll** (`sessionStorage['collab-scrollY']` → `restaurerScroll()` au `load`). Petit **flash** jaune sur la card modifiée à distance. ⚠ Le repli garantit la correction : si l'optim en place rate, on retombe sur le reload (toujours juste).
- **Phase 4 serveur (`serveur.py`)** : (a) **éditions éphémères** `_editions{cardKey→{traitant,tab,ts}}` (NON persistées) — `POST /edition {key,op:start|end,traitant,clientId=tab}` → diffuse `editions` à tous ; snapshot envoyé à la connexion SSE ; **purge auto** (thread 10 s, TTL 35 s) + libération à la **déconnexion** de la fenêtre (par `tab`). (b) **Sauvegardes** : `GET /sauvegardes` (liste fichier/date/taille/clés), `POST /sauvegarder` (sauvegarde horodatée immédiate), `POST /restaurer {fichier}` (valide le nom = `etat_*.json` dans `backups\`, remplace le store, persiste, **rediffuse `etat`** → tous les postes resync). `do_POST` routé (`/maj /edition /restaurer /sauvegarder`).
- **Phase 4 client (`collab.js`)** : écoute `editions` → **badge « ✏ <traitant> »** sur la card concernée (finder multi-clés data-twid/artid/num/cleStatut/pubKey) ; **verrou ADVISORY** = enveloppe `CR_editArticle`/`CR_editTweet`/`CR_editExArt` → `confirm` si la card est déjà éditée par un autre, puis signale mon édition ; **détection ouverture/fermeture** du modal via `.cr-overlay.open` (interval 1 s) + **heartbeat** 15 s ; `window.MAST_COLLAB.edit/endEdit`. **Page d'admin** servie : `…:8765/_collab_admin.html` (lister/restaurer/sauvegarder, réservée à l'animateur).
- ✅ **Tests 2026-06-18** : `node --check` collab.js + `ast.parse` serveur.py OK ; fonctionnel — `/edition` reçu en direct par un Viewer, `/sauvegarder`+`/sauvegardes` OK, **`/restaurer` ramène bien l'état** + rediffuse `etat`, purge/déconnexion OK. ⏳ **Reste la validation NAVIGATEUR** (badges, flash, verrou advisory, reload doux) sur 2 machines.
- **🐛 Diagnostic 2026-06-18 — « impossible d'ouvrir MASTAURIGE depuis le fichier HTML »** : ce n'est PAS un bug serveur (vérifié : `/`, `/collab.js`, `/etat`, MELMIL, créateur, `/_collab_admin.html` tous servis en 200, collab.js chargé avant `<title>`, 0 erreur). **Cause = ouverture du FICHIER en `file://` au lieu de l'URL du serveur.** En collaboratif, MASTAURIGE s'ouvre **uniquement via `http://<hôte>:8765/`** (ou le raccourci `OUVRIR_MASTAURIGE.url`) : un fichier `file://` ne peut pas, par sécurité navigateur, joindre l'origine du serveur. **Garde-fou ajouté dans `collab.js`** : si `location.protocol === 'file:'` → **bandeau rouge** « ouvre l'adresse du serveur… » + on n'amorce ni SSE ni éditions (mode local). Rien d'autre à corriger côté serveur.

**🌍 ADAPTATION CONTENU 7BB — Arnland + Bothnia (instance `EXER\AURIGE 7BB\…\LOCALSTORAGE_WEB_VERSION`, 2026-06-18) :** 5 articles `.html` (TV4 ×2, HEXAGONE, ONU, Today Mercure) ré-employés de 2BB → corrigés : **Dacie Romanie/Dacia Romania/Dacian → Arnland** (élisions FR), **Ruthnia Bella → Bothnia**, **dates → mardi 23 juin 2026** (D+33), géo **H-préfixe** (HNancy, HLorraine), domaine TV4 `.dr→.arn`. Puis **casting Bothnia** (décision utilisateur) : **Tikhanov/Saniki conservés** (canon, 🔴) · **Youkachenko → Présidente Lena Peters** · **Bella Channel 1 → Bothnia Channel 1** (sigle BC1 gardé) · **Minsk → Brahea**. Fichiers : site BC1 `_TEMPLATE.html` + **régénération `templates.js`** · libellé `name` (`articles.js`/`generer_articles.py`) + dropdown `createur.js` · `bios.js` + **fix durable dans `generer_trombino_bios.py`** (substitution avant écriture → une régénération ne réintroduit pas Youkachenko). **Clés/dossiers internes inchangés** (`bc1`, `Site Bella Channel 1`) — seul l'affichage devient « Bothnia Channel 1 ». ⚠ **Narratif à réécrire** : le gabarit BC1 garde un sommet « Lena Peters–Olamao » qui contredit la neutralité de Peters. Legacy laissé : `MELMIL.xls` (GESTIM, on est en JEMM). Sauvegardes : `D:\CECPC\_cbtmp\{articles_bak,bothnia_bak}`.

**⭐ STARTEX PACKAGE — sous-injects `00.00.00Ai…Ei` (incident parent `00.00.00i`) (2026-06-18, demande utilisateur ; nommage corrigé « STARTER → STARTEX » + passage en sous-injects) :** lot d'articles « ligne de conduite politique » donné aux joueurs au démarrage (7BB : le 23 juin / D+33), **sans vrai numéro**. Chaque article = **sous-inject distinct** `00.00.00Ai`/`Bi`/… rattaché à l'incident **`00.00.00i`** ⇒ dans MELMIL, le **CAS 1.5** de `buildGhostInjects` crée **une carte GHOST par camp** (série `00` inconnue → ligne **r7 GHOST**), chaque carte ne montrant au clic **que les injects de son camp** (sous-items cliquables individuellement). Couleur **par camp** (🔴/🔵/⚪ = autorité qui parle).
- **Moteur (instance 7BB + copie collab ; PAS la vierge — alignée en fin de MINAUTORE)** : `MELMIL\melmil.js` — (1) CAS 1.5 : si `parentCode` commence par `00.00.00`, libellé **« 📦 STARTEX PACKAGE »** lisible sur chaque carte-camp (au lieu de l'avertissement « hors XLS ») ; (2) ligne socle 188 : même rename STARTEX (cas futur où `00.00.00` serait dans le XLS). `moteur\createur.js` — `CR_previewArticle`, pour `external:true` + `file`, **NAVIGUE vers le vrai `.html` dans le MÊME onglet** (`saveMasterState()` + `location.href = Sites/<file>?from=master`), comme les cards média via `openCard` — **PAS** d'iframe popup ni de nouvel onglet *(itéré 2026-06-18 sur demande utilisateur : iframe → window.open → navigation même onglet)*. Le bouton **« ← MASTAURIGE »** (bas-gauche) vient de `shared/back-btn.js` (chargé en fin d'article), et `index_master` **restaure le scroll** au retour.
- **Articles** : `moteur\starter_package.js` = **5 créations auto-injectées** (idempotent par id, respecte la corbeille), chacune avec **son code sous-inject** — TM/Olamao `00.00.00Ai` 🔴 · TV4/Pallesson `00.00.00Bi` 🔵 · HEX/Rutte `00.00.00Ci` 🔵 · ONU/Guterres `00.00.00Di` ⚪ · TV4/Guterres `00.00.00Ei` ⚪ — `external:true`, `dayorder:"33"` (23 juin). Le loader **réconcilie le `num`** des articles déjà en localStorage (`AW.update(id,{num})`, conserve `file`/contenu) → une instance taguée à l'ancien `00.00.00i` se renumérote seule au prochain chargement.
- ✅ Tests : `node --check` melmil.js + starter_package.js + createur.js OK ; diff net contrôlé. ⏳ **Re-valider en NAVIGATEUR** après les 4 correctifs ci-dessous. ⚠ **Régénérer le kit JOUEURS** pour embarquer `starter_package.js` + les `.html`. Sauvegardes : `D:\CECPC\_cbtmp\starter_bak`.

**🐛 4 bugs corrigés au 1er test navigateur STARTEX (2026-06-18) — instance 7BB + copie collab (PAS la vierge) :**
1. **🔴 Cartes en « À placer » au lieu du D+33 (bug GÉNÉRIQUE, tout le 7BB)** : `dayorderToISO()` (melmil.js) était **codée en dur pour le calendrier 2BB** (D+26→35 = mai/début juin) → un `dayorder` 7BB (33-41 = 23 juin→1 juil) renvoyait une date hors `DAY_MAP` ⇒ overflow. **Tout inject créé en 7BB tombait en « À placer »**, pas que le STARTEX. Fix = `dayorderToISO(d)` retourne `COL_TO_ISO['d'+d]` (piloté par le `DAY_MAP` généré, zéro calendrier en dur). + corollaires même cause : garde `d>=26&&d<=40` → `COL_TO_ISO['d'+d]` (sinon **D+41 exclu**) ; liste de colonnes en dur `['d31'…'d40']` de `ensureDynRow` → dérivée de `DAY_MAP`.
2. **🔴 Cartes rouge/bleu/neutre fusionnées en une seule au drag** : le handler de drop ghost cherchait `existingG` par `[data-code]` **sans le camp** → déposer une carte sur une autre du même incident fusionnait les sous-injects (toutes couleurs) en une carte. Fix = sélecteur `[data-code][data-camp="<camp>"]` (ne fusionne qu'avec le **même camp**).
3. **🔴 404 « Today Mercure » au clic** : `file` **périmé en localStorage** (ancienne création) ; l'idempotence sautait la re-création. Fix = le loader `starter_package.js` **réconcilie aussi `file`** (`AW.update(id,{num,file})`, conserve le contenu) → repointe vers le bon `.html` au prochain chargement.
4. **🔴 Articles ouverts en pop-up iframe au lieu de la vraie page** : `createur.js` `CR_previewArticle` external **navigue dans le même onglet** (`saveMasterState()` + `?from=master`) → bouton **« ← MASTAURIGE »** (`shared/back-btn.js`) + scroll restauré au retour (comme `openCard`).
5. **🔴 Bouton retour absent / 404 du script** : les 5 articles (hérités 2BB) incluaient `../shared/back-btn.js` (1 niveau = `Sites/shared/`, **inexistant**) alors que la convention 7BB des gabarits `_TEMPLATE.html` est **`../../shared/back-btn.js`** (= `shared/` à la **racine** de l'instance, qui existe). Fix = chemin des 5 articles corrigé en `../../shared/` (doublon `Sites/shared/` que j'avais créé par erreur → supprimé). ⚠ profondeur 7BB = `Sites/Site X/page.html` (2 niveaux), pas comme 2BB (`Site X/page.html`, 1 niveau).
> ⚠ **À porter dans la VIERGE en fin de MINAUTORE** : les correctifs #1 (calendrier-agnostique), #2 (fusion par camp) et #4 (navigation même onglet) sont **génériques** — la vierge a les mêmes bugs 2BB en dur.

**📦 RELOCALISATION du serveur collaboratif dans l'exercice 7BB (2026-06-18, demande utilisateur) :** emplacement canonique = **`D:\CECPC\PRODUCTION\EXER\AURIGE 7BB\00_Boites à outils\MASTAURIGE\SERVEUR_COLLABORATIF\`** (serveur.py + python\ portable + infra + `mastaurige\`). `mastaurige\` **reconstruit à neuf** depuis l'instance 7BB à jour (Arnland/Bothnia/Starter Package) + couche collab (collab.js, _collab_admin.html, tags injectés). **Workflow** : toutes les MAJ MINAUTORE se font ICI ; l'utilisateur copie le sous-dossier `mastaurige\` sur le PC Admin (remplace l'ancien) → traitants rafraîchissent. **VIERGE intacte** (MAJ vierge à la fin de MINAUTORE). Ancien `D:\CECPC\MASTAURIGE\SERVEUR_COLLABORATIF\` superseded. ✅ Smoke-test relocalisé : `/`, collab.js, starter_package.js, article Pallesson (272 Ko), _collab_admin, melmil_ili tous servis 200. ⚠ Reste 3 résidus 2BB dans les **gabarits de site `_TEMPLATE.html`** (TV4/Hexagone — contenu d'exemple, génère de futurs articles ; PAS les 5 articles livrés qui sont propres) → à nettoyer si besoin. bios.js 7BB déjà propre. Sauvegardes : `D:\CECPC\_cbtmp\relocate_bak`.
