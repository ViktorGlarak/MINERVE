# MÉMOIRE — DELATTRE (exercice DELATTRE 26)

> **Source de vérité détaillée de l'exercice DELATTRE 26.** Créée le **2026-07-22**.
> ⭐ **RÉFLEXE : CONSULTER cette mémoire AVANT toute production · y CONSIGNER APRÈS chaque avancée**, sans attendre de rappel utilisateur.
> Successeur de MINAUTORE (AURIGE 7BB / MINOTAURE 26), lui-même successeur de GUILLAUME (AURIGE 2BB).

---

## 1. ⚠️ IDENTITÉ DE L'EXERCICE — À RENSEIGNER

> **Rien n'est encore connu de DELATTRE 26 au 2026-07-22** hormis son nom. Demander ces éléments à l'utilisateur
> avant toute production, puis remplir ce tableau — **il conditionne tout le reste** (surtout le **niveau**, qui
> détermine la calibration des injects).

| Champ | Valeur | Impact |
|---|---|---|
| Nom complet / cadre OTAN | **DELATTRE 26** (usage courant : « DELATTRE ») | — |
| Organisateur | ⚠️ *à renseigner* | — |
| **Unité(s) entraînée(s)** | **1re DIV** (1 DIV), avec **27e BIM** et **9e BIMa** *(PPT GREY CELL v4, 2026-09-23 — cohérent avec le diagramme RZO)* | Destinataires des injects |
| **Niveau** (brigade / division / CA) | **Division** (1 DIV), puis brigades 27 BIM / 9 BIMa en phase AURIGE ; échelon sup. = **1CA** *(déduit du PPT : « amener la 1DIV puis les brigades… », FRAGO du 1CA)* | **⭐ Détermine la calibration — le point n°1 du RETEX** |
| Lieu + dates réelles | ⚠️ *à renseigner* | Calendrier |
| Temps de jeu (D+ → dates) | ✅ **D+27 = mar 06/10/2026 → D+41 = mar 20/10/2026** (page 2 du PPT ; D0 = 09/09/2026). Phases : **Warm up tactique** D+27-28 · **BST DE LATTRE 26** D+29-31 · **3A** D+32 · **AURIGE 27e BIM** D+33-36 · **3A** D+37 · **AURIGE 9e BIMa** D+38-41 | `DAY_MAP` MELMIL + `dayorder` |
| Zone d'opérations + H-codes | ⚠️ *à renseigner* | Cohérence géographique |
| **Camps** (qui attaque / défend) | ⚠️ *à renseigner* | ⚠ **Vérifier le sens : le 7BB était INVERSÉ vs le 2BB** |
| Pays fictifs impliqués | ⚠️ *à renseigner* | Quels ANALYSTES mobiliser |
| Sources de montage | ✅ **`EXER\DELATTRE 26\01_Montage exercice\20260909 - GREY CELL_MAIN v4.pptx`** (events, storylines, incidents — voir §1ter) + diagramme RZO (§1bis) ; **JEMM** en cible | Pipeline d'ingestion |
| Storylines → LO | ⚠️ *à renseigner* (7 storylines connues, §1ter) | `lo_config.js` |

---

## 1bis. ⭐ PREMIER ÉLÉMENT CONCRET — Réseau RENS/RZO (diagramme SITCEN, ingéré 2026-09-10)

> **Source autoritaire** : `EXER\DELATTRE 26_Montage exercice\RENS60904_NP_DLT26_SITCEN_RENS_Diagramme RZO.pptx` (le `.pdf` homonyme est identique — 1 diapositive, 0 note, vérifié fragment par fragment).

### Ce que le document révèle de l'exercice
- **Insignes d'unités : `1 DIV` (sur HETTA) · `27 BIM` (sur CIRKOF) · `9 BIMa` (sur MICHEL)** → unités visées/infiltrées par le réseau — indice fort d'un exercice **niveau division** (1re DIV) avec la 27e BIM et le 9e BIMa. ⚠ À confirmer par l'utilisateur avant d'en faire une base de calibration (point n°1 du RETEX).
- **Continuité MINOTAURE → DELATTRE** : 28 des 30 acteurs sont la reprise du réseau RENS/RZO du 7BB (mêmes noms, mêmes photos). Zone toujours HLorraine (maires HSARREBOURG, HNANCY, HLUNÉVILLE, HCHATEAU-SALINS, HSARRE-UNION) + « Gouverneur GET ».

### Structure du réseau (30 acteurs, 7 types de liens)
- **Tête** : `Patrick HETTA` — « ARN-ProMER, CDT RÉGION », **visage NON identifié (silhouette — voulu)**, insigne 1 DIV.
  - 🔴 **CORRECTION du 2026-09-15** : la version précédente affirmait que HETTA « commande (liens noirs) » deux cellules. **C'est faux.** Le fichier a été dépouillé trait par trait (63 traits) : **l'unique trait noir est celui de la LÉGENDE**. Aucun lien « commande » n'est tracé dans le diagramme — la légende en définit un, le dessin n'en contient aucun. La lecture de 2026-09-10 confondait la **mise en page** (une ellipse autour de HETTA, un rectangle autour des quatre cadres) avec un **lien dessiné**.
  - Ce qui part **réellement** de HETTA : `relation RZO` → `Pascal DEGARDIN` · `ex-relation intime` → `Cathy POMMEROND` · un `lien suspecté` vers un individu non identifié. **Rien d'autre.**
  - La cellule `YARBOT`–`LECONE`–`LAPOTRE`–`HERVOUET` est bien une chaîne, mais en **`relation HFM/NOM` (rouge pointillé)**, et elle est reliée au reste par `Капитан Хэдок` → `YARBOT`. Son appartenance commune est portée par un **rectangle de mise en page**, pas par des liens.
  - ⚠ **Leçon** : lire un diagramme « à l'œil » depuis un PDF fait confondre proximité et relation. La géométrie du `.pptx` (couleur, pointillés, extrémités attachées) est la seule source fiable.
- **Sphère clandestine HFM/NOM** (liens rouges pointillés) : masques anonymes + agitateurs `The flying fly`, `Le Padupe`, `Léon-Philippe THELY` ; symboles HFM (tête de mort ▽) et NOM (étoile rouge).
- **Maillage civil RZO** (liens bleus) : les 5 maires (`PROMESY`, `ADRIANE`, `MORDVIDCHEV`, `DANEVOIS`, `MARTIN`) + `Rémi LAFFIN (Gouverneur GET)` + `José PERNOD (journaliste régional)` + `Antoine BOURGUIGNON (pdt des Agriculteurs)` + `Pascal DEGARDIN (ancien militaire)` + `Thomas CRUSADIER (militaire ARN)`.
- **Sphère MER** : `Armin KRASNI (43e DIV)`, `Gennady YEREMIN (42e DIV)`, influenceurs `Капитан Хэдок`, `Marie NASSAH`, `Béa_HVT (complotiste)`, célébrités `Алексей Аксёненко`, `Сюзанна Светличная`, `Katia CHAPMAN`. `HERVOUET` **en relation intime** avec `Béa_HVT` ; `Хэдок` avec `NASSAH`.
- **Liens familiaux** (verts) : `Kimberley (« Fille de… », identité incomplète)` ↔ `Nathalie MARTIN` et ↔ `Pascal DEGARDIN` ; Kimberley **en relation intime** avec `CRUSADIER`.
- **Liens suspectés** (orange) : LAFFIN↔symboles NOM/HFM, THELY↔DANEVOIS, CHAPMAN↔СВЕТЛИЧНАЯ/NASSAH, KRASNI↔étoile NOM, CRUSADIER↔masque central, etc.
- Légende complète : noir=commande · rouge pointillé=HFM/NOM · vert=familial · bleu=RZO · violet pointillé=ex-intime · violet plein=intime · orange=suspecté.

### État EHO MASTORION (fait le 2026-09-10)
- **30/30 présents** dans le modèle SKOLKAN-PERSONA, tous taggés `EXERCICE DELATTRE 26` ; **29/30 avec portrait conforme au diagramme** (HETTA sans photo = VOULU).
- **2 créés pour DELATTRE** : `@rzo_patrick_hetta` (ARN-GROUPE CLANDESTIN/PRO-MERCURE, rouge) · `@rzo_kimberley` (ARN-CITOYEN, neutre) — inscrits À LA SOURCE dans `MASTORION\OUTILS\generer_bibliotheque.py` (`PERSONAS_DELATTRE` + `RESEAU_DELATTRE`) → classeur Excel 453 personas, annuaire alignés, modèle recapturé.
- **7 portraits récupérés du PPTX même** (les sources 7BB avaient des placeholders `rzo-x*`) : Хэдок, Аксёненко, Светличная, The flying fly, Le Padupe, Kimberley, Mordidchev.
- ⚠ **Divergence d'orthographe À TRANCHER par l'utilisateur** : le diagramme écrit « Serge **MORDVIDCHEV** », l'EHO 7BB « Serge **Mordidchev** » (maire HNancy). Même personne (alias posé dans le générateur) — quelle graphie fait foi pour DELATTRE ?
- ⚠ Trio cyrillique : usernames hérités de placeholders source (`@rzo_x`, `@rzo_x_2`, `@rzo_x_3`) — fonctionnels mais laids ; renommage possible si demandé.

## 1ter. ⭐ EVENTS, STORYLINES, INCIDENTS — PPT « GREY CELL MAIN v4 » (ingéré 2026-09-23)

> **Source** : `EXER\DELATTRE 26\01_Montage exercice\20260909 - GREY CELL_MAIN v4.pptx` (21 diapositives, daté 10/09/2026, **aucun marquage de diffusion réel** — seul un modèle inutilisé porte « NATO CLASSIFICATION »).
> ⚠ **Décision utilisateur** : font foi les **pages 3 à 10** (numérotation du tableau des pages 1-2). Les **pages 11 à 21** sont des **brouillons** (ancienne numérotation 08.06 rumeurs, 08.07 mouvements, 08.08 IDPs, 08.10 sabotage HFM, + saturation santé, exactions, manifestations, communications) — **non importées**. ⚠ Piège : dans le fichier, les pages 3-10 sont **masquées** et les pages 11-13 **visibles** (l'export PDF ne sort que 1, 2, 11, 12, 13).

**2 events, 7 storylines** (page 2 = chronologie D+27 → D+41) :
| Event | Storyline | Période (page 2) | Coordination (page 1) | Incidents |
|---|---|---|---|---|
| **06 — ILI** | **06.01** Signaux faibles captés par les ETIM (FZO 9 BIMa) | D+33 → D+40 | OPFOR + RENS | 11 (06.01.01-11), la plupart sur plusieurs jours |
| | **06.02** Rumeurs contre la FORCE | 3 temps : D+27-28 · D+33-34 · D+38-39 | OPFOR | 3 narratifs (BST / 27 BIM / 9 BIMa), CRQ_01 09h + CRQ_02 15h |
| **08 — GREY CELL** | **08.01** Dégradation des services essentiels de la HN — **STARTEX package** | D+27 | LOG | 1 (starting package) |
| | **08.02** Risques sur les sites sensibles | D+27-28 · D+31-32 | 2D/3D/ciblage | 3 (mail G39/1CA BSL-3 HNANCY, site essence, coopérative nitrate) |
| | **08.03** Actions perfides | D+27-28 · D+34-35 · D+39-40 | — | 3 narratifs (CICR détourné / charnier NSL / bouclier humain) |
| | **08.04** Mouvements de populations (IDPs) | D+27-30 · D+33-35 · D+38-40 | LOG/2D | 5 (FRAGO 1CA, flux HNANCY→HTOUL, UN OCHA couloirs, HSARREBOURG, HHAGUENEAU) |
| | **08.05** Sécurisation des IDPs et appui à la HN | D+29-31 · D+32-34 · D+38-40 | — | 5 (camps HST-DIZIER, HCHAUMONT, HJOINVILLE, HNEUFCHÂTEAU ; eau/vivres HLUNEVILLE) |

- ⭐ **2026-09-30 — le retour vers ce format** : MELMIL exporte l'atelier **au format de ce PPT**, avec le bouton « Exporter en PPT ». L'export contient la synthèse, la chronologie, une fiche par storyline (sur plusieurs diapositives si besoin) et les changements depuis une date, marqués en rouge, pour transmission aux autorités. Voir `DESIGNER\AVIS\2026-09-30_MELMIL_EXPORT_PPT\`.
  - ⚠ **Format A4 paysage** (29,7 × 21 cm) demandé par l'utilisateur, à la place du 16:9 d'origine. Les incidents sont paginés selon leur hauteur réelle, donc aucun débordement. Un incident trop long est raccourci avec la mention « suite dans MELMIL ». *(Version `2026-09-30.5`.)*

Objectif d'entraînement principal : **8.1** — « Étudier les données d'environnement multidomaines de la nation hôte pouvant avoir des conséquences sur la manœuvre ». Acteurs d'injection : **ETIM** / ETEC, HN, autorités ARN, UN OCHA, 1CA.

### ⭐ Export JEMM FICTIF (fait le 2026-09-23)
- **Générateur** : `DELATTRE\OUTILS\generer_jemm_greycell.py` (lit le PPT, **relançable** si le PPT évolue ; Id stables).
- **Sortie** : `EXER\DELATTRE 26\01_Montage exercice\JEMM\FICTIF_<horodatage>_JEMM_DLT26_EVENT_06.json` (**27 injects**) et `…_EVENT_08.json` (**19 injects**) — **46 au total**, 1 fichier par Event (format JEMM réel : `Data.Events/Storylines/Injections`, `MetaData`, `EncodedData`).
- **Vérifié** avec l'importateur d'`app-melmil` (`src/lib/melmil/jemm.ts`) : 0 échec, codes uniques, 0 sans date, 0 orphelin.
- **Règles validées par l'utilisateur** : un inject **par jour** d'occurrence · **09h00** par défaut · 08.02 réparti sur **D+27, D+28, D+31** · chaque **CRQ = un inject** · codes JEMM `EE.SS.Inn` numérotés **par ordre chronologique** dans la storyline, le code PPT d'origine rappelé en fin de description `[PPT 06.01.04 — D+36 — occurrence 1/2]`.
- Champs non fournis par le PPT, posés par défaut : moyen d'injection « À PRÉCISER » (sauf mail / RS / FRAGO / startex), destinataire « 1 DIV » (ou 27 BIM / 9 BIMa pour les narratifs), cellule = ILI / GREY CELL, marquage UNCLASSIFIED.
- ⚠ **Points ouverts** : **06.01.08** (carte Mercure abandonnée) n'a **aucun jour** dans le PPT → placé à D+33, à confirmer · le PPT numérote **deux fois 08.04.04** (D+33 et D+38) → le second est devenu **08.04.I05** · les narratifs 06.02 sont codés **08.06.Ixx** dans le PPT (reliquat de l'ancienne numérotation) → recodés **06.02.Ixx**.
- ⏭ **Suite annoncée par l'utilisateur** : modifications de **MELMIL** (`app-melmil`) pour optimiser le travail.
- ✅ **Fait le 2026-09-23 — l'ATELIER DE PRÉPARATION de MELMIL** (`/preparation`, « Création d'exercice ») : les traitants y créent events (GT1), storylines (GT2) et incidents (GT3) en direct, avec équipe par cellule, journal, planche de préparation et **écarts avec la planche JEMM**. Les deux JEMM fictifs ci-dessus s'y **versent** pour démarrer (réglages : D+27 = 06/10/2026 ; période D+27 → D+41). Détail technique : `PLEIADE\MEMOIRE.md` § « MELMIL — l'ATELIER DE PRÉPARATION ». ✅ Déployé sur `melmil.delattre-26` le 2026-09-23 (17:41, version 2026-09-23.3).
- ✅ **2026-09-24** : grille EXCON cliquable sur les storylines (déployée, `2026-09-24.1`) ; **comptes rendus PSYREP / CIMICREP** sur chaque incident (créer, cumuler, remplir à l'identique du modèle, télécharger en .docx, **importer** un modèle rempli dans Word) — modèles de référence : `EXER\DELATTRE 26\00_Boites à outils\APPENDICE 7_ PSYREP.FR.docx` et `APPENDICE 8_ CIMICREP.FR.docx`. ✅ En ligne sur `melmil.delattre-26` depuis le 2026-09-24 13:14 (`2026-09-24.2`).
- 🟡 **2026-09-24 (soir) — MELMIL v2 responsive** (avis DESIGNER n°3) prêt **en local** (`refonte-v2`, `2026-09-24.5`) : lisible au téléphone (vue **Liste par jour**, fiches plein écran), à la tablette et à l'ordinateur. En attente de validation avant mise en ligne. Détail : `PLEIADE\JOURNAL.md`.
- 🟡 **2026-09-24 (nuit) — eho tient les ~3 500 avatars de DE LATTRE** *(en local, branche `refonte-v2`, non poussé)*. Les pages chargent désormais les avatars **par groupe** : le trombinoscope reçoit d'abord un sommaire par pays, puis les cartes de chaque bloc. S'y ajoute la refonte DESIGNER n°4 : téléphone et tablette, rangement de plusieurs cartes d'un coup, confirmations lisibles. Détail : `PLEIADE\JOURNAL.md` (suite 9). ✅ En ligne le 2026-09-25.
- 🟡 **2026-09-25 — eho de la zone : ≈ 3 750 avatars (import du réseau social par Xavier) + SKOLKAN PERSONA 21.09.26** :
  - Fusion prête **en local** (bouton « Fusionner dans la base… ») : **3 983 avatars** après retrait de **220 doublons**, au profit de la fiche SKOLKAN, **ids conservés** pour ne pas casser le réseau social. Nouveau modèle : **SKOLKAN FULL PERSONA 25.09.26**.
  - Export de référence : `C:\Users\MTR\Downloads\avatars-eho-2026-09-25.xlsx`.
  - Code en ligne le 2026-09-25 à 10:36 ; la fusion reste à lancer depuis l'écran. Détail : `PLEIADE\JOURNAL.md` (2026-09-25, suite 3).

### ⭐ Règle de nommage des pièces jointes (décision utilisateur du 2026-10-01, appliquée par MELMIL)
`AAAAMMJJ_MR_DL26_SITCEN-<CODE>-<NMR>-<Titre>` :
- **AAAAMMJJ** : le jour où l'**incident** est joué (par exemple 20261010), modifiable ;
- **CODE** : **GYC** (GREY CELL) ou **FOR** (FORAD) ;
- **NMR** : *(2e décision du 01/10)* le **code de l'incident sans les points**, par exemple 08.01.I01 donne **0801I01**. Pour une demande **sans incident**, c'est le numéro de pièce (001, 002…) ;
  - choix assumé : deux fichiers du même incident avec le même titre portent le **même nom**, il faut les distinguer par le titre ;
- **Titre** : celui de l'incident par défaut.
- À l'**export**, un fichier nommé « -001- » sur un incident sort avec le code de l'incident.
- **Comptes rendus** (PSYREP, CIMICREP, SCAMR) : même règle au téléchargement. Le titre par défaut est le nom du compte rendu, et le NMR le code de l'incident de la fiche ouverte. La date et le titre sont modifiables *(01/10)*.
- **SCAMR** (CRI propagande) : nouveau compte rendu par jour et par ETIM, reproduit à l'identique de `01_Montage exercice\SCAMR.png`. **Consigne de l'utilisateur : l'image seule fait foi, pas « Modèle SCAMR.pptx »** *(en ligne le 01/10)*.
- ⭐ **SCAMER** *(04/10, version MELMIL 2026-10-04.14)* : le compte rendu **SCAMR est remplacé par le « SCAMER »** (colonne renommée), modèle **`01_Montage exercice5-Modèle Fiche SCAMER - Copie.odt`** (« Le SCAME-R » : Source, Contenu, Auditoire, Média, Effets, Recommandations). Les SCAMR déjà remplis gardent l'ancien modèle « CRI propagande ». ⭐ **2026-10-04.17 : reproduit À L'IDENTIQUE** (6 cadres, réponses à la suite des intitulés, cases à cocher Word ; export = le vierge rempli ; réimport). ⚠ L'exemplaire **rempli** `…Copie.docx` porte **DIFFUSION RESTREINTE** : jamais versé dans PLÉIADE.

Remplace la règle du 30/09 (`AAAAMMJJ_MR_DL26_SITCEN-FORAD|GREYCELL-Titre`, avec la date du jour). Détail : `PLEIADE\JOURNAL.md` (2026-10-01, suite 6).

### ⭐⭐ JEMM RÉEL — la saisie fait foi (exports du 2026-09-30)
- **Fichiers** (marqués **NATO UNCLASSIFIED**, exportés le 30/09 à 14:39) : `EXER\DELATTRE 26\01_Montage exercice\JEMM\30.09.26\NU_20260930_143929_JEMM_WDDPR_EVENT_07\…json` et `…_143920_…_EVENT_08\…json`. Espace JEMM **WDDPR**, exercice « De LATTRE ». Chaque export a un zip et une somme de contrôle.
- ⚠ **Numérotation JEMM, qui remplace celle du PPT et des fictifs** :
  - **Event 07 = ILI** (ex-06). Storylines : **07.01** Signaux faibles captés par les ETIM (22 incidents) · **07.02** Rumeurs sur la Force (3) · **07.03** CRQ ETIM PSYREP+CIMICREP (15, **nouvelle, sans diapo**).
  - **Event 08 = HN** (ex-« GREY CELL »). Storylines : **08.01** Dégradation des services essentiels (6) · **08.02** Risques sites sensibles (3) · **08.03** Actions perfides (3) · **08.04** Mouvement de population (5) · **08.05** Sécurisation des IDPs et appui à la HN (5).
  - **Total : 2 events, 8 storylines, 62 incidents.** Objectif principal de toutes les storylines : « 8-1 — ILI - Etudier les données d'environnement multidomaines… ».
- ⚠ **JEMM a découpé et renuméroté** des incidents du PPT : un fait sur plusieurs jours devient une occurrence datée par jour (« Pylône électrique HS » D+33, D+35, D+36, D+37). Les 07.01.Ixx ne correspondent donc plus aux 06.01.Ixx.
- **Compléments tirés des diapos** (effets attendus, QUI / OÙ, pour ce que JEMM ne tient pas) : `…\JEMM\30.09.26\COMPLEMENTS_DIAPOS_GREY-CELL-v4.json` (diapos 4 à 10 : 06-01 devient 07.01, 06-02 devient 07.02, 08-0x reste 08.0x). Ils ne remplissent que le vide.
  - **Décision utilisateur** : les effets attendus de la **07.03** restent **vides**.
  - Restent aussi sans QUI / OÙ : 07.02 et 08.03, dont les diapos n'ont qu'un tableau de narratifs.
- **Décisions utilisateur du 30/09** :
  - la planche JEMM **et** la planification sont **à 100 % identiques** aux exports, sans un incident de plus ;
  - les noms JEMM sont retenus (« 07 ILI », « 08 HN ») ;
  - un incident absent de JEMM est supprimé, mais on liste d'abord ceux qui portent des pièces jointes.
- **Outil** : MELMIL `2026-09-30.7`, avec « Aligner l'atelier sur JEMM » (Réglages) et « Remplacer par des exports JEMM » (planche, menu Plus). Détail : `PLEIADE\JOURNAL.md` (2026-09-30, suite 8).

## 2. Socle hérité — acquis valables dès maintenant

### Lignes Opératoires GLM26 (référence permanente)
**LO1** Appui hybride à la manœuvre (effort permanent) · **LO2** Volonté de combattre · **LO3** Guerre des pertes ·
**LO4** Vent de libération · **LO5** Rupture des alliances.
→ Tout inject a une **LO principale** ; sans LO il est orphelin. Les LO sont **une aide, pas une contrainte**.

### Règles narratives permanentes
Équilibre des camps · **règle du CLIMAX** (pic informationnel sur le moment tactique majeur) · **noyau de vérité 80/20** ·
neutralité visuelle des camps pour les entraînés · **Steps PSYOPS 1→2→3 sans saut** · pas de renvoi vers un contenu futur ·
**GET** et non « Europe » pour la zone fictive · codage **H-préfixe** · numéros de téléphone fictifs cohérents.

### Propriété des données (anti-divergence)
- **Camp d'un persona** : fait foi **uniquement** dans le registre MASTAURIGE (+ `avatars.js`) et les entités `vault\entities\personas\`.
  L'Analyste du pays **tranche**, tout le monde **cite** — on ne recopie jamais une valeur de camp.
- Doctrine narrative d'un personnage pays → l'**ANALYSTE** du pays. Format/HTML → **MASTAURIGE**. Effets ILI → **EXPERT_INFLUENCE**.

---

## 3. ⭐ RETEX MINOTAURE 26 — à appliquer dès le montage
> Fiche complète : `MINAUTORE\RETEX_MINOTAURE_26.md` (points forts / erreurs / recommandations, sourcés).

**Les 5 leçons :**
1. **Calibrer TACTIQUE** — trop d'injects stratégiques pour une cible brigade = aucun effet (constat unanime des 3 documents).
2. **Fermer la boucle de retour** — sans retour sur le traitement des injects : « travailler dans le vent », démotivation. **Mesure la plus rentable.**
3. **Les GT produisent des scénarios**, pas des débats d'objectifs (sur MINOTAURE, injects décidés dans les 2 derniers jours).
4. **Casser les silos** RENS / FORAD / DIV (fiches bio faites **deux fois**).
5. **Reconduire ce qui a marché** : MASTAURIGE + EHO matérialisé + **1 traitant par LO**.

**À porter en amont (prérequis de montage, pas des erreurs de production) :** internet ouvert au poste (ou 2 postes),
postes de la cellule regroupés, carte de la ZO affichée, traitants en copie des mails chef/adjoint, **formation aux logiciels**,
ratio expert image/opérateurs équilibré (1 pour 7 = goulot), **abonnements outils financés par le CECPC**,
**synthèse des country books**, **annuaire des avatars**.

**⚠ JEMM** : jugé dispersant, non modifiable, à faible apport vs MASTAURIGE et **inadapté au niveau brigade** ;
droits traitants bloquants en l'absence du chef/adjoint. → MASTAURIGE reste l'outil de travail réel.

---

## 4. Actifs réutilisables — ne pas refaire ce qui existe

| Actif | Où | Statut |
|---|---|---|
| **EHO 7BB** — profond, « réutilisable pour de futurs exercices » (RETEX) | `MINAUTORE\MEMOIRE.md` + trombinoscope 7BB | ✅ disponible |
| **Gabarit MASTAURIGE v0.3** (portage post-MINOTAURE du 2026-07-22) | `D:\CECPC\MASTAURIGE\LOCALSTORAGE_WEB_VERSION` | ✅ à jour (format JEMM, split de card, correctifs calendrier, STARTEX + statuts permanents) |
| **Registre des avatars** (base CASW ORION 26, réutilisée 2BB puis 7BB) | `MASTAURIGE\MEMOIRE.md` + `moteur\avatars.js` | ⚠ **à consulter AVANT tout nouveau compte fictif** |
| **Chartes médias** : Today Mercure, TV4 International, BC1, HEXAGONE, Site OTAN, EFS | `MASTAURIGE\MEMOIRE.md` | ✅ cloner, ne pas recréer |
| **Doctrine ILI** : Storm-1516/VIGINUM, Morelli, Sun Tzu, mentalité russe, lawfare | `EXPERT_INFLUENCE\REFERENCES\` | ✅ |
| **Catalogue d'injects niveau brigade** + doctrine de calibration | `AURIGE\MEMOIRE.md` | ✅ anti-« trop stratégique » |
| **Méthodologie transverse AURIGE** (11 points) | `AURIGE\MEMOIRE.md` § méthodologie | ✅ |
| **Générateur de carte d'état** | `MINAUTORE\generer_etat_exercice.py` | 🔁 à adapter pour DELATTRE |

⚠ **Vérifier la transposabilité** de tout actif 7BB : les **camps** et la **zone** peuvent différer sur DELATTRE 26.

---

## 5. Chantiers d'ouverture (dès que l'identité est connue)

- [ ] Renseigner le tableau §1 (identité) — **bloquant pour le reste**
- [ ] Créer l'instance outillage depuis la **vierge v0.3** + configurer le calendrier (`OUTILS\CONFIGURER_EXERCICE.py` → `DAY_MAP`)
- [ ] Établir la table **H-préfixe** de la ZO
- [ ] Définir les **storylines → LO** (`lo_config.js`)
- [ ] Constituer l'EHO (réutiliser le 7BB si la zone/les camps le permettent)
- [ ] Adapter le générateur de **carte d'état** (`DELATTRE\ETAT_EXERCICE.md`)
- [ ] **Poser d'emblée les demandes RETEX** : responsable du retour sur injects, référent inter-cellules, prérequis SIC

---

## 6. Journal de l'exercice

> *(À alimenter à chaque avancée : décisions, injects produits, validations d'agents, corrections.)*

### [2026-09-25] ETIM dans les JEMM fictifs
Vérification demandée par l'utilisateur : dans les deux JEMM FICTIF, les ETIM sont portées comme **acteurs** (`ScenarioRoleList`, repris de la colonne « QUI » du PPT). Aucune n'est dans l'émetteur ni dans les destinataires.
- **36 incidents sur 46** citent une ETIM :
  - Event 06 : les 27 incidents (22 « Signaux faibles » avec ETIM + ETEC, 5 « Rumeurs contre la FORCE ») ;
  - Event 08 : 4 incidents avec « ETIM » (Dégradation services essentiels, Risques sites sensibles) et 5 « Actions perfides » avec un libellé **non normalisé** (« ETIM 27 », « ETIM 9 », « ETIM 27 BIM ou 9 BIMa »).
- Les 10 incidents restants (Mouvements de populations, Sécurisation des IDPs) n'ont pas d'ETIM.
- ⚠ Ce sont des fichiers générés depuis le PPT, **pas un export JEMM réel**.
- Dans `app-melmil`, ces acteurs sont importés dans `roles` et affichés sur la fiche (« Rôles du scénario »). Il n'existe aucun filtre ETIM, et un incident créé dans l'atelier n'a pas de rôles (`versPlanche` → `roles: []`).
- ✅ **Suite le même jour, à la demande de l'utilisateur** : la Planification de MELMIL permet de **cocher les ETIM de chaque incident**, dans une liste propre à l'exercice (Réglages). Leur nom s'affiche sur la carte de l'incident. ✅ En ligne le 2026-09-25 (`app-melmil` `5b4d76a`, `2026-09-25.1`). ⏳ **Suite demandée** : quand les premiers exports JEMM réels de l'exercice arriveront, récupérer leurs ETIM pour les afficher sur la **planche JEMM** (piste et vérifications : `PLEIADE\MEMOIRE.md` § MELMIL atelier). ⚠ Sur le serveur, l'atelier DE LATTRE 26 a été versé **avant** cette fonction : sa liste d'ETIM sera **vide**, et il faudra la remplir dans Réglages (ETIM 27 BIM, ETIM 9 BIMa… — noms exacts à confirmer par l'utilisateur).

### [2026-09-23] PPT GREY CELL v4 ingéré — premier export JEMM fictif
PPT analysé (21 diapositives, pages 1-2 = tableau de synthèse et chronologie, 3-10 = incidents retenus, 11-21 = brouillons écartés). Identité enrichie : **1 DIV + 27 BIM + 9 BIMa**, calendrier **D+27 = 06/10/2026 → D+41 = 20/10/2026** et ses phases. Deux fichiers JEMM fictifs générés (Event 06 ILI : 27 injects ; Event 08 GREY CELL : 19 injects), validés par l'importateur d'`app-melmil`. Détail et points ouverts : §1ter.

### [2026-07-22] Création de l'agent
Agent **DELATTRE** créé (20ᵉ du système MINERVE) à la demande de l'utilisateur, en préparation de l'exercice **DELATTRE 26**.
Enregistré au registre `CLAUDE.md`, dans `SYSTEME\ROUTAGE.md`, compteur `NOYAU\MEMOIRE.md` porté à 20.
Prompt système `SYSTEME\PROMPTS\delattre.md` créé depuis le modèle MINAUTORE + gabarit `aurige.md`, **enrichi du RETEX MINOTAURE**.
⚠ **Identité de l'exercice non encore communiquée** — à recueillir auprès de l'utilisateur.

- **2026-10-02 — Avatars de la DIV 1 : 7 comptes préparés pour eho.**
  - Source : `01_Montage exercice\DIV 1\avatars_DL26 v2.docx`.
  - Comptes : 5 d'Arnland (@elmircaunity, @fertileground, @arnverifiedconflict, @staysafe_stayalive, @donk_pedro) et 2 de Mercure (@el-salsichino, @NO_MERcy).
  - Groupe eho **« CAMP DIV1 »**. Portraits intégrés au fichier d'import, et biographie composée à partir des seuls champs de la fiche, pour le kit IA.
  - Testé dans l'eho local : 7 créés, 0 refusé.
  - Détail chez ANALYSTE_ARN et ANALYSTE (Mercure).
  - ⚠ Pour réserver ces avatars à la DIV 1, il faut cocher le camp DIV1 sur le groupe dans eho (écran Groupes, puis Camps).
