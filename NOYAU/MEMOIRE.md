# MÉMOIRE — NOYAU (Orchestrateur)

## Format d'entrée
```
### [YYYY-MM-DD] Catégorie : Titre
Contenu de la connaissance acquise.
```

---

## Contexte du projet — CE QUE FAIT L'UTILISATEUR
Mercure est un assistant de production d'exercices militaires et civils de gestion de crise.
L'utilisateur crée des exercices complets incluant : scénarios, personnages fictifs, documents, images IA, vidéos IA, montage Premiere Pro.
Exercices de référence : ORION 26 (grand exercice multi-cellules, Vienne/Poitiers) et AURIGE 2BB (production média, Lorraine).

## Préférences utilisateur

### [2026-05-06] Init : Création du système Mercure
Système multi-agents créé. L'utilisateur souhaite un orchestrateur (Claude) qui délègue aux agents Ollama locaux.
Préférence : réponses en français, annonce toujours de l'agent qui répond.

### [2026-05-06] Règle de mémoire proactive
L'utilisateur veut que Claude mette à jour automatiquement les fichiers MEMOIRE.md des agents concernés après chaque apprentissage, correction ou avancée significative. Objectif : ne jamais avoir à répéter un sujet déjà traité. Appliquer après chaque session productive.

### [2026-05-06 — mis à jour 2026-05-23] Règle QC — Principe de compétence
Claude (NOYAU) est plus performant que les agents Ollama locaux. En conséquence :
- **Tout output d'agent est systématiquement relu par NOYAU** avant livraison à l'utilisateur
- Si le contenu est perfectible (fond, forme, cohérence géopolitique, ton), NOYAU ne rejette pas — il **utilise le travail de l'agent comme base** et le raffine directement
- L'agent fournit la matière première (ancrage countrybook, structure narrative) ; NOYAU élève la qualité finale
- L'utilisateur ne reçoit que la version finale contrôlée — jamais un draft brut d'agent Ollama
Ce principe s'applique à tous les agents sans exception : ANALYSTE, ANALYSTE_ARN, SCÉNARISTE, IMAGIER, etc.

### [2026-05-06] Texte dans les images
Quand l'utilisateur fournit un texte précis à afficher dans une image générée, ce texte doit être intégré mot pour mot dans le prompt, entre guillemets, avec "legible word for word". Jamais résumer ou paraphraser.

---

## Table de routage canonique — À consulter AVANT toute production (2026-05-29)

> **Principe :** NOYAU applique automatiquement le routage ci-dessous sans attendre que l'utilisateur le demande. Consulter la mémoire des agents concernés AVANT de produire. NOYAU assure le contrôle qualité final dans tous les cas.

### ⚠ Règle automatique — Trombinoscope RS mis à jour à chaque nouvel avatar

> **Dès qu'un nouvel avatar RS fictif est créé pour AURIGE 2BB, NOYAU déclenche automatiquement la mise à jour de la section "Avatars RS" correspondante dans le trombinoscope** — sans attendre que l'utilisateur le demande.

La mise à jour du trombinoscope fait partie de la **checklist création avatar** (étape 5) :
1. Card HTML dans index_master.html
2. ANIM_DATA + LO_BY_KEY
3. melmil_inject_index.js
4. MASTAURIGE/MEMOIRE.md (registre)
5. **Trombinoscope `Trombinoscope\ACTEURS_A3_AURIGE2BB.html` — section RS du pays concerné**

Page à mettre à jour selon le camp :
- Rouge/pro-MER → Page 1 Mercure
- Bleu/OTAN/civil neutre → Page 2 Dacie Romanie
- BR → Page 3 Bella Russia

---

### Trombinoscope (`Trombinoscope\ACTEURS_A3_AURIGE2BB.html`)

> Fichier sous `...\MASTAURIGE\WEB\` → **MASTAURIGE obligatoire** dans tous les cas.

| Type de modification | Agents obligatoires | Agents contextuels |
|---|---|---|
| Personnage Mercure | **MASTAURIGE** | **ANALYSTE MERCURE** (profil, biographie, cohérence Countrybook) |
| Personnage DAC / Arnland | **MASTAURIGE** | **ANALYSTE_ARN** |
| Personnage Bella Russia | **MASTAURIGE** | **ANALYSTE_BR** |
| Ajout portrait manquant | **MASTAURIGE** (intégration) | **IMAGIER** (création portrait) |
| Mise en page / CSS / structure A3 | **MASTAURIGE** + NOYAU | — |

**Réflexe avant édition :** Grep sur le nom du personnage → lire la section → vérifier cohérence avec ANALYSTE concerné → vérifier que le portrait est dans `WEB\images\`.

---

### Exercice AURIGE — Productions contenus

| Demande | Agents primaires | Agents contextuels | Notes |
|---|---|---|---|
| **Tweet exercice AURIGE** | MASTAURIGE (format, avatar, MELMIL) + GUILLAUME (date, LO, cohérence) | ANALYSTE MERCURE si tweet pro-MER · ANALYSTE_BR si tweet BR · SCÉNARISTE si narratif local | Toujours vérifier MELMIL_SUBINJECT_DAYS si date ≠ parent XLS |
| **Article média fictif** (BC1, TM, TV4, HEX) | MASTAURIGE (template HTML, format) + GUILLAUME (date, LO, cohérence) | SCÉNARISTE (narrative) · ANALYSTE pertinent (cohérence pays) | Template obligatoire par site (voir MASTAURIGE/MEMOIRE.md) |
| **Courrier fictif** (maire, préfet, institution) | MASTAURIGE (format HTML) + GUILLAUME (date, LO) | SCÉNARISTE (voix du personnage) | Charte locale + numéro 03 72 67 XX XX |
| **Tract PSYOPS** | MASTAURIGE (format) + GUILLAUME (LO, phase psyops) | ANALYSTE MERCURE (contenu MAF/MER) | Référence 07.02.XXi dans synchromatrice |
| **Inject brigade local** (manifestation, tag, sermon, RS humiliant) | MASTAURIGE + GUILLAUME | SCÉNARISTE (voix locale) | Ancrer dans ville ZO (HCHATEAU-SALINS, HLUNEVILLE...) — voir doctrine brigade |

### Discours de personnages

| Personnage | Agent principal | Agent secondaire |
|---|---|---|
| Olamao / ministre MER / HVI MER | **ANALYSTE MERCURE** | SCÉNARISTE (mise en forme) |
| Pallesson / ministre DAC / figure ARN | **ANALYSTE_ARN** | SCÉNARISTE |
| Youkachenko / figure BR | **ANALYSTE_BR** | SCÉNARISTE |
| Rutte (SG OTAN) / figure réelle OTAN | **NOYAU** directement | — |
| Figure OTAN fictive | **SCÉNARISTE** | NOYAU (QC) |
| Journaliste / notable / civil local | **SCÉNARISTE** | MASTAURIGE si tweet |

### Productions médias (image, voix, vidéo)

| Demande | Agent principal | Notes |
|---|---|---|
| Prompt image ComfyUI / Firefly | **IMAGIER** | NOYAU révise le prompt si trop complexe |
| Prompt vidéo LTX | **CINÉASTE** | Pour vidéos courtes exercice |
| Paramètres OmniVoice | **VOIX** | Clonage vocal personnages |
| Portrait personnage fictif | **IMAGIER** → puis **ARCHIVISTE** (BDA) | Chemin dossier Portraits → BDA |

### Planification / Doctrine ILI

| Demande | Agent principal | Agent secondaire |
|---|---|---|
| Synchromatrice / planning injects | **EXPERT_INFLUENCE** + **GUILLAUME** | ANALYSTE pertinent |
| Calibrage pédagogique exercice | **EXPERT_INFLUENCE** | PENSEUR (raisonnement) |
| PPT / brief animateur | **EXPERT_INFLUENCE** + **ANALYSTE** | PENSEUR |
| Analyse narrative cohérence | **PENSEUR** | ANALYSTE pertinent |
| Question complexe multi-agents | **PENSEUR** + NOYAU | — |

### Code & technique

| Demande | Agent principal | Notes |
|---|---|---|
| Code JS / HTML / PS1 (MELMIL, index_master) | **ARCHITECTE** (ou NOYAU directement si complexe) | NOYAU intervient directement pour logique MELMIL — ARCHITECTE = debug ou refactoring |
| Bug technique système | **ARCHITECTE** | NOYAU diagnose d'abord |
| Script PowerShell | **ARCHITECTE** | |

### Règle absolue — Tout fichier de l'écosystème MASTAURIGE

> **MASTAURIGE est l'expert de son propre système. Dès qu'un fichier appartient à l'écosystème MASTAURIGE, MASTAURIGE est obligatoirement consulté — sans exception, quel que soit le type de modification (contenu, code, CSS, script, config).**

**L'écosystème MASTAURIGE = tout ce qui se trouve sous :**
```
D:\CECPC\PRODUCTION\EXER\AURIGE 2BB\00_Boites à outils\MASTAURIGE\
```

Cela inclut notamment :
- `WEB\index_master.html` — agrégateur maître animateur
- `WEB\MELMIL\` — tous les fichiers : `MELMIL_ILI_GUILLAUME.html`, `melmil.js`, `melmil.css`, `melmil_inject_index.js`, `melmil_data.js`, `generate_data.ps1`, `Actualiser_MELMIL.bat`, `MELMIL.xls`
- `WEB\Site BC1\`, `WEB\Site Today Mercure\`, `WEB\Site TV4\`, `WEB\Site Hexagone\` — tous les articles HTML
- `WEB\TRACTS\` — tous les tracts
- `WEB\shared\` — scripts partagés (`back-btn.js`, etc.)
- `WEB\images\` — images du système
- `WEB\Trombinoscope\` — trombinoscope acteurs
- Tout autre fichier ou script présent dans ce dossier

| Type de modification | Agents **obligatoires** | Agents contextuels |
|---|---|---|
| Nouveau inject (tweet, article, courrier, tract) | **MASTAURIGE** + GUILLAUME | ANALYSTE pertinent |
| Bug JS / logique (`melmil.js`, `index_master`) | **MASTAURIGE** + NOYAU | — |
| Script PS1 / BAT (`generate_data.ps1`, etc.) | **MASTAURIGE** | ARCHITECTE si complexe |
| CSS (`melmil.css`, styles articles) | **MASTAURIGE** | — |
| Article HTML site fictif | **MASTAURIGE** + GUILLAUME | SCÉNARISTE/ANALYSTE (contenu) |
| Config MELMIL (`.xls`, `melmil_data.js`) | **MASTAURIGE** | — |
| Images / assets | **MASTAURIGE** | IMAGIER (création image) |

**Règle des 4+1 modifications simultanées pour tout nouvel inject :**
1. HTML card dans `index_master.html` — **avec les 5 attributs obligatoires** (voir ci-dessous)
2. Entrée `ANIM_DATA`
3. Entrée `LO_BY_KEY`
4. Entrée `melmil_inject_index.js`
5. Trombinoscope RS si nouvel avatar
+ Si date sous-inject ≠ date parent XLS → `MELMIL_SUBINJECT_DAYS`

**5 attributs obligatoires sur toute article-card :**
`data-source` · `data-category` · `data-camp` · `data-dayorder` · `onclick`
— `data-camp` manquant = bug silencieux (classification et redirect MELMIL cassés)

> Toujours lire la section exacte avant d'éditer (Grep pour localiser, Read pour contexte).

### Questions scénario / univers

| Sujet | Agent |
|---|---|
| Mercure (politique, militaire, histoire, personnages) | **ANALYSTE MERCURE** |
| Dacie Romanie / Arnland | **ANALYSTE_ARN** |
| Bella Russia (Youkachenko, opposition, médias BR) | **ANALYSTE_BR** |
| Question transversale plusieurs pays | **PENSEUR** → consultation ANALYSTES |

---

### Règle de consultation automatique

> **NOYAU lit toujours en priorité la mémoire des agents concernés avant de produire** — pas besoin que l'utilisateur le demande. Le routage ci-dessus est automatique dès qu'une demande de production arrive.
>
> **Quand je ne suis pas sûr du routage :** appliquer la règle des 3 agents = GUILLAUME (contexte éditorial AURIGE) + MASTAURIGE (technique/format) + ANALYSTE pertinent (contenu/pays). Ces 3 agents couvrent 90% des demandes de production.

---

### ⚠ RÈGLE OBLIGATOIRE — Enregistrement chez l'Analyste pays à chaque création de personnage ou avatar (ajout 2026-05-30)

> **Toute création ou modification d'un personnage, d'une figure politique, d'un avatar RS ou d'un acteur fictif lié à un pays du GET doit être enregistrée IMMÉDIATEMENT dans la mémoire de l'Analyste du pays concerné.**
> Cette règle s'applique sans exception et sans attendre que l'utilisateur le demande.

#### Correspondance pays → Analyste à mettre à jour

| Pays concerné | Fichier à mettre à jour | Ce qui déclenche la mise à jour |
|---|---|---|
| **Mercure** | `ANALYSTE/MEMOIRE.md` | Tout nouveau personnage MER (politique, militaire, para-étatique, avatar RS) |
| **Arnland / Dacie Romanie** | `ANALYSTE/ARNLAND/MEMOIRE.md` | Tout nouveau personnage ARN/DR (politique, militaire, civil ZO, avatar RS) |
| **Bella Russia** | `ANALYSTE/BELLA_RUSSIA/MEMOIRE.md` | Tout nouveau personnage BR (gouvernement Youkachenko, opposition, militaire, avatar RS) |

#### Ce qui déclenche cette obligation

- Création d'un personnage nommé dans un article HTML (ministre, général, chef d'État, porte-parole…)
- Création d'un avatar RS fictif (nouveau compte Twitter, BC1, TM, EastWatch…)
- Attribution d'un poste ou d'un rôle à un personnage existant mais non encore documenté
- Correction d'une erreur d'attribution (ex : mauvais porte-parole cité dans un article)

#### Ce qu'il faut enregistrer chez l'Analyste

1. Nom complet du personnage
2. Poste / rôle officiel
3. Camp (rouge / bleu / neutre)
4. Règle éditoriale : qui parle de quoi (éviter les confusions futures)
5. Articles ou injects où il apparaît (référence par clé MASTAURIGE ou nom de fichier HTML)

#### Rappel — Erreur corrigée le 2026-05-30

Ivan Lubrakov (Ministre de l'Intérieur BR, créé pour l'inject 07.05.05i) avait été enregistré dans GUILLAUME et MASTAURIGE mais **pas dans ANALYSTE_BR**. Cette règle est instaurée pour éviter ce type d'oubli.

---

---

## Patterns de routage appris

### [2026-05-06] Mockups UI (WhatsApp, interfaces mobiles)
llama3.1:8b insuffisant pour décrire fidèlement des interfaces mobiles.
Claude répond directement pour ce type de demande sans passer par l'IMAGIER.

### [2026-05-23] Discours de personnages politiques
SCÉNARISTE seul est insuffisant — il écrit bien mais sans ancrage géopolitique réel.
Règle validée :
- Personnage mercurien → ANALYSTE rédige le discours
- Personnage DR / Arnland → ANALYSTE_ARN rédige le discours
- Figure réelle (Rutte, Youkachenko) → NOYAU (Claude) directement
- Figure OTAN fictive → SCÉNARISTE
NOYAU assure le contrôle qualité final dans tous les cas.

---

## Règle automatique — Dossier par exercice AURIGE

> **À chaque démarrage d'un nouvel exercice AURIGE, NOYAU crée automatiquement le sous-dossier de l'exercice dans `AURIGE\` sans attendre que l'utilisateur le demande.**

### Procédure automatique au démarrage d'un nouvel exercice AURIGE

1. Créer `D:\CECPC\PRODUCTION\IA\Mercure\AURIGE\AURIGE_[UNITE]\MEMOIRE.md`
2. Y inscrire : identité exercice, unité entraînée, niveau, période, chemins, agents assignés
3. Créer l'agent éditorial dédié (ex : `GUILLAUME_3BB\`) au niveau racine Mercure
4. Mettre à jour `AURIGE\MEMOIRE.md` — tableau des exercices
5. Mettre à jour `CLAUDE.md` — registre agents + checklist

### Convention de nommage dossier exercice
```
AURIGE\AURIGE_[UNITE]\     ex : AURIGE_2BB, AURIGE_3BB, AURIGE_11BP...
```

### Ce que NOYAU stocke dans ce dossier (via agent AURIGE)
- État de production (jours produits / restants / gaps)
- Bilan pédagogique (niveau atteint, erreurs, leçons)
- Décisions d'architecture propres à cet exercice
- Leçons à réinjecter dans l'exercice suivant

### Capitalisation inter-exercices
Avant de démarrer AURIGE_3BB, NOYAU consulte automatiquement `AURIGE\AURIGE_2BB\MEMOIRE.md` pour :
- Ne pas répéter les erreurs de calibrage (D+31→D+34 trop stratégiques)
- Repartir avec le bon ratio dès le montage (4 injects locaux / 1 stratégique)
- Réutiliser les conventions techniques validées (MELMIL_SUBINJECT_DAYS, sync bidirectionnelle, etc.)

### [2026-05-31] AURIGE = Base d'initialisation des agents exercice

> **AURIGE est la source de vérité de la doctrine d'exercice CECPC. Lors de la création de tout nouvel agent éditorial d'exercice, NOYAU part de `SYSTEME\PROMPTS\aurige.md` comme template de base.**

**Ce que AURIGE transmet automatiquement à chaque nouvel agent exercice :**
- Univers Skolkan (acteurs permanents GET, citations canoniques, règle Bella Russia, règle GET)
- Camps narratifs BLEU/ROUGE/GRIS + médias fictifs associés
- 5 LO GLM26 (référence stratégique universelle)
- Règles cohérence narrative (CLIMAX, noyau de vérité, équilibre camps, neutralité visuelle, règle LO)
- Steps PSYOPS (Step 1→2→3, escalade progressive obligatoire)
- Catalogue séries ILI (07.01→08.03, logique thématique)
- Règle H-préfixe (codage géographique)
- Doctrine calibration brigade (ratio 1-2 stratégiques/semaine, catalogue 15 types injects locaux)
- Architecture dossier exercice (6 dossiers numérotés, nommage D+XX_JJ_MOIS)
- Framework agents (qui appeler pour quoi)

**Ce que l'agent exercice complète lui-même (non transférable) :**
- Zone géographique et H-codes de la ZO
- Brigade / unité entraînée
- Game Plan / synchromatrice (dates réelles)
- Acteurs locaux fictifs
- Injects produits et leur statut

**Procédure automatique de création d'un agent exercice :**
1. Copier `SYSTEME\PROMPTS\aurige.md` → créer `SYSTEME\PROMPTS\[agent].md`
2. Compléter les sections ⚠️ avec les données de l'exercice
3. Créer `[AGENT]\README.md` et `[AGENT]\MEMOIRE.md` avec doctrine AURIGE héritée
4. Enregistrer dans CLAUDE.md, CONFIG.md, ROUTAGE.md, NOYAU\MEMOIRE.md

---

## Décisions d'architecture

### [2026-05-06] Claude comme orchestrateur réel
Choix validé : Claude appelle les modèles Ollama via API PowerShell (localhost:11434).
Continue (VSCode) reste disponible pour accès direct aux agents individuels.
Niveau 2 (script Python autonome) prévu pour une prochaine étape.

### [2026-05-27] Règle vocabulaire — GET (Grand East Territory)
**GET** = entité géopolitique fictive de l'univers Skolkan = regroupement des pays fictifs de l'Est (Mercure, Arnland/Dacie Romanie, Bella Russia).

⚠ **Nuance critique :**
- "Europe" (vraie) coexiste avec le GET — ce sont deux entités distinctes
- "Europe" reste valide pour les vrais pays européens, l'OTAN réelle, les institutions réelles
- "GET" s'emploie quand le contexte désigne la zone géopolitique des **pays fictifs** de l'Est
- Ce n'est PAS un remplacement automatique "Europe → GET" — c'est une question de contexte

### [2026-05-25 — mis à jour 2026-05-30] 19 agents au total
4 généralistes (ARCHITECTE, PENSEUR, SECRÉTAIRE, ÉCLAIREUR) +
3 spécialistes exercices (IMAGIER, CINÉASTE, SCÉNARISTE) +
10 agents spécialisés (VOIX, ARCHIVISTE, ANALYSTE, ANALYSTE_ARN, ANALYSTE_BR, MASTODONTE, MASTAURIGE, GUILLAUME, EXPERT_INFLUENCE, MINAUTORE) +
NOYAU (Claude — orchestrateur)

> MINAUTORE ajouté le 2026-05-30 — chef d'orchestre éditorial AURIGE 7BB, claude-opus-4-7 (même modèle que GUILLAUME). Dossier exercice : `D:\CECPC\PRODUCTION\EXER\AURIGE 7BB\`. Synchromatrice à ingérer.
> ANALYSTE_BR ajouté le 2026-05-27 — comptage corrigé de 17 à 18 le 2026-05-29, puis 19 le 2026-05-30.

ANALYSTE_ARN ajouté le 2026-05-23 — expert Arnland/Dacie Romanie, deepseek-r1:14b partagé avec ANALYSTE + PENSEUR.
MASTAURIGE ajouté le 2026-05-24 — contenus RS fictifs pour exercices AURIGE (entraînement PC niveau brigade), avatars CASW, tweet cards HTML offline. mistral-nemo:latest partagé avec MASTODONTE + SCÉNARISTE + SECRÉTAIRE + VOIX. Indépendant de Mastorion (plateforme distincte, IA dédiée future).
GUILLAUME ajouté le 2026-05-25 — chef d'orchestre éditorial AURIGE 2BB. Connaît tous les acteurs, camps, médias fictifs et gère le calendrier de publication (statut publié/à produire/date à définir). **Migration 2026-05-25 : deepseek-r1:14b → claude-opus-4-7 (cloud)** — même modèle qu'EXPERT_INFLUENCE, pour garantir la qualité doctrinale et narrative. Partage avec EXPERT_INFLUENCE, ANALYSTE, ANALYSTE_ARN.
EXPERT_INFLUENCE ajouté le 2026-05-25 — expert doctrine ILI et conception de synchromatrice. Transversal tous exercices. Claude Opus 4.7 (cloud) — modèle susceptible d'évoluer sur décision de l'utilisateur. Partage avec GUILLAUME, ANALYSTE, ANALYSTE_ARN, PENSEUR.
ANALYSTE_BR ajouté le 2026-05-27 — expert Bella Russia (Biélorussie fictive). Couvre le régime Youkachenko, l'opposition démocratique (Tikhanov, Saniki), les médias BR (BC1), la chronologie des injects BR (série 07.05, arc P.03). Transversal tous exercices impliquant BR. deepseek-r1:14b partagé avec ANALYSTE + ANALYSTE_ARN + PENSEUR. Dossier : `ANALYSTE\BELLA_RUSSIA\`.

### [2026-05-25] Dossier GUILLAUME — créé + GAME PLAN AURIGE 2BB ingéré
Dossier `GUILLAUME\` créé à la racine Mercure (manquait). Contient :
- `GUILLAUME\README.md` — rôle, modèle, fichiers de référence
- `GUILLAUME\MEMOIRE.md` — GAME PLAN AURIGE 2BB ingéré (données MAINBODY réelles) + 8 axes lacunaires + 15 propositions ILI doctrine russe

**Données MAINBODY désormais connues de GUILLAUME :**
- D+35 (30 mai) = CLIMAX — RUPTURE LDP, SAISIE HSARREBOURG — GAP CRITIQUE (aucun inject de victoire MER)
- D+32–34 : DPs fuyant HLUNEVILLE N4 → ancrage humanitaire (08.01.02i TV4 Panique)
- D+37 : Arrivée 13e RG DAC — opportunité narrative "OTAN envoie des renforts car elle perd"
- D+37–38 : Population hostile HLUNEVILLE / D+39+ : population hostile HSARREBOURG
- AUTH ARN exactions IRREG confirmées — à nier en architecture 3 couches (P-05)

**15 propositions ILI (P-01 à P-15) soumises à validation :**
`EXER\AURIGE 2BB\00_Boites à outils\MASTAURIGE\PROPOSITIONS_ILI_DOCTRINERUSSE.md`
Couvrent 8 axes manquants (déni plausible, blanchiment, noyau vérité, industrialisation, localisation, opportunisme, saturation, appropriation)

---

### [2026-05-25] Dossier ANALYSTE — structure par pays + Countrybook Mercure ingéré
Dossier `ANALYSTE\` créé à la racine Mercure, centralise tous les analystes par pays :
- `ANALYSTE\MERCURE\` — Expert Mercure (Countrybook complet) + Doctrine OI Storm-1516 (rapport VIGINUM TLP:CLEAR)
- `ANALYSTE\ARNLAND\` — Expert Arnland / Dacie Romanie (migré depuis `ANALYSTE_ARN\`, nom du pays variable selon exercice)
- `ANALYSTE_ARN\` — supprimé le 2026-05-25

**ANALYSTE MERCURE maîtrise désormais :**
1. Countrybook Mercure (943 paragraphes, CB MERCURE FR.docx) — géographie, politique, militaire (607K, triade nuc), économie (PIB 550 Mds$), société (3 ethnies Inen), info (172/180 RSF), infrastructure, tous les personnages
2. Storm-1516 (VIGINUM, 77 opérations) — 16 TTP, 4 phases de diffusion, acteurs (DOUGAN, KOROVINE, KHOROCHENKY)
Prompt système mis à jour : `SYSTEME\PROMPTS\analyste.md`.
