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
| **Unité(s) entraînée(s)** | ⚠️ *à renseigner* | Destinataires des injects |
| **Niveau** (brigade / division / CA) | ⚠️ *à renseigner* | **⭐ Détermine la calibration — le point n°1 du RETEX** |
| Lieu + dates réelles | ⚠️ *à renseigner* | Calendrier |
| Temps de jeu (D+ → dates) | ⚠️ *à renseigner* | `DAY_MAP` MELMIL + `dayorder` |
| Zone d'opérations + H-codes | ⚠️ *à renseigner* | Cohérence géographique |
| **Camps** (qui attaque / défend) | ⚠️ *à renseigner* | ⚠ **Vérifier le sens : le 7BB était INVERSÉ vs le 2BB** |
| Pays fictifs impliqués | ⚠️ *à renseigner* | Quels ANALYSTES mobiliser |
| Sources de montage | ⚠️ *à renseigner* (JEMM ? Event List ? synchromatrice ? OPORD ?) | Pipeline d'ingestion |
| Storylines → LO | ⚠️ *à renseigner* | `lo_config.js` |

---

## 1bis. ⭐ PREMIER ÉLÉMENT CONCRET — Réseau RENS/RZO (diagramme SITCEN, ingéré 2026-09-10)

> **Source autoritaire** : `EXER\DELATTRE 26_Montage exercice\RENS60904_NP_DLT26_SITCEN_RENS_Diagramme RZO.pptx` (le `.pdf` homonyme est identique — 1 diapositive, 0 note, vérifié fragment par fragment).

### Ce que le document révèle de l'exercice
- **Insignes d'unités : `1 DIV` (sur HETTA) · `27 BIM` (sur CIRKOF) · `9 BIMa` (sur MICHEL)** → unités visées/infiltrées par le réseau — indice fort d'un exercice **niveau division** (1re DIV) avec la 27e BIM et le 9e BIMa. ⚠ À confirmer par l'utilisateur avant d'en faire une base de calibration (point n°1 du RETEX).
- **Continuité MINOTAURE → DELATTRE** : 28 des 30 acteurs sont la reprise du réseau RENS/RZO du 7BB (mêmes noms, mêmes photos). Zone toujours HLorraine (maires HSARREBOURG, HNANCY, HLUNÉVILLE, HCHATEAU-SALINS, HSARRE-UNION) + « Gouverneur GET ».

### Structure du réseau (30 acteurs, 7 types de liens)
- **Tête** : `Patrick HETTA` — « ARN-ProMER, CDT RÉGION », **visage NON identifié (silhouette — voulu)**, insigne 1 DIV. **Commande** (liens noirs) 2 cellules : `Jules CIRKOF (27 BIM)` ↔ `Thomas MICHEL (9 BIMa)` · `Louis YARBOT (adjoint)`–`Bernard LECONE (geek-cyber)`–`Firmin LAPOTRE (instructeur guérilla)`–`Éric HERVOUET (artificier)`. **Ex-relation intime** avec `Cathy POMMEROND` (commerçante pro-MER).
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

### [2026-07-22] Création de l'agent
Agent **DELATTRE** créé (20ᵉ du système MINERVE) à la demande de l'utilisateur, en préparation de l'exercice **DELATTRE 26**.
Enregistré au registre `CLAUDE.md`, dans `SYSTEME\ROUTAGE.md`, compteur `NOYAU\MEMOIRE.md` porté à 20.
Prompt système `SYSTEME\PROMPTS\delattre.md` créé depuis le modèle MINAUTORE + gabarit `aurige.md`, **enrichi du RETEX MINOTAURE**.
⚠ **Identité de l'exercice non encore communiquée** — à recueillir auprès de l'utilisateur.
