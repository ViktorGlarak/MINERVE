# CLAUDE.md — Source de vérité du système Mercure

> Ce fichier est **la référence canonique** du projet. Toute valeur définie ici prime sur les autres fichiers.
> Quand une information change ici, mettre à jour les fichiers listés dans la section correspondante.

---

## Chemin racine du projet

```
D:\CECPC\PRODUCTION\IA\Mercure\
```

**Fichiers à mettre à jour si ce chemin change :**
- `SYSTEME\CONFIG.md` — section "Répertoire Mercure"
- `SYSTEME\DOSSIER_POSTE.md` — section "7. SYSTÈME MERCURE"
- `.claude\settings.local.json` — toute permission contenant ce chemin

---

## Registre des agents (source de vérité)

> **Ce tableau est l'UNIQUE source de vérité du registre des agents.** Les autres fichiers (CONFIG, ROUTAGE, DOSSIER_POSTE, NOYAU/MEMOIRE) **ne dupliquent pas** cette liste : ils y renvoient.
> - Colonne **« Collabore avec »** = partenaires de travail **thématiques** (qui travaille avec qui sur le contenu) — ce n'est PAS le partage de VRAM.
> - **Co-résidence VRAM** = déductible de la colonne **Modèle** : deux agents avec le même modèle Ollama sont co-résidents en mémoire (pas besoin de la lister).

| Agent | Modèle Ollama | Collabore avec (thématique) | Rôle |
|---|---|---|---|
| NOYAU | Claude (cloud) | — *(orchestre tous les agents)* | Orchestrateur |
| ARCHITECTE | qwen2.5-coder:14b | PENSEUR | Code & debug |
| PENSEUR | deepseek-r1:14b | ARCHITECTE, ANALYSTE, ANALYSTE_ARN, ANALYSTE_BOT, EXPERT_INFLUENCE, GUILLAUME, MINAUTORE | Raisonnement & stratégie — optimise les productions au profit des entraînés ; **cite** la doctrine d'EXPERT_INFLUENCE (Sun Tzu, Morelli, LO), ne la détient pas *(local ; bref passage Opus 4.8 le 2026-06-02 annulé le même jour — doctrine regroupée chez EXPERT_INFLUENCE)* |
| SECRÉTAIRE | mistral-nemo:latest | SCÉNARISTE, VOIX, MASTODONTE | Rédaction FR |
| ÉCLAIREUR | llama3.1:8b | IMAGIER, CINÉASTE, ARCHIVISTE | Tâches rapides |
| IMAGIER | llama3.1:8b | ÉCLAIREUR, CINÉASTE, ARCHIVISTE | Prompts image |
| CINÉASTE | llama3.1:8b | ÉCLAIREUR, IMAGIER, ARCHIVISTE | Prompts vidéo LTX |
| SCÉNARISTE | mistral-nemo:latest | SECRÉTAIRE, VOIX, MASTODONTE, MASTAURIGE, GUILLAUME, MINAUTORE | Contenu scénario |
| VOIX | mistral-nemo:latest | SECRÉTAIRE, SCÉNARISTE | Paramètres OmniVoice |
| ARCHIVISTE | llama3.1:8b | ÉCLAIREUR, IMAGIER, CINÉASTE | Gestion BDA |
| ANALYSTE | deepseek-r1:14b | PENSEUR, ANALYSTE_ARN, ANALYSTE_BOT, EXPERT_INFLUENCE, GUILLAUME, MINAUTORE | Expert République de Mercure |
| ANALYSTE_ARN | deepseek-r1:14b | PENSEUR, ANALYSTE, ANALYSTE_BOT, EXPERT_INFLUENCE, GUILLAUME, MINAUTORE | Expert Arnland / Dacie Romanie *(dossier : `ANALYSTE\ARNLAND\` — migré 2026-05-25)* |
| MASTODONTE | mistral-nemo:latest | SCÉNARISTE, SECRÉTAIRE, MASTAURIGE | Expert Mastodon / réseaux sociaux fictifs |
| MASTAURIGE | mistral-nemo:latest | GUILLAUME, MINAUTORE, MASTODONTE, SCÉNARISTE | Contenus RS fictifs exercices AURIGE — entraînement PC niveau brigade (avatars CASW, tweet cards HTML) |
| ANALYSTE_BOT | deepseek-r1:14b | ANALYSTE, ANALYSTE_ARN, PENSEUR, EXPERT_INFLUENCE, GUILLAUME, MINAUTORE | Expert **Bothnia** — countrybook ORION 26 (Pr. Lena Peters, BUP, démocratie, allié MER via SCO/SSTO, Den Helder) ; **+ legacy « Ruthnia Bella » (Youkachenko/BC1) pour AURIGE 2BB uniquement** *(dossier : `ANALYSTE\BOTHNIA\` — ex-ANALYSTE_RB, renommé 2026-05-31)* |
| GUILLAUME | Claude (cloud) — claude-opus-4-7 | EXPERT_INFLUENCE, MASTAURIGE, SCÉNARISTE, ANALYSTE, ANALYSTE_ARN, ANALYSTE_BOT | Chef d'orchestre éditorial AURIGE 2BB — calendrier publications, cohérence narrative, programmation des injects |
| EXPERT_INFLUENCE | Claude (cloud) — claude-opus-4-7 | GUILLAUME, MINAUTORE, PENSEUR, ANALYSTE, ANALYSTE_ARN, ANALYSTE_BOT | Expert doctrine ILI & synchromatrice — **dépôt doctrinal unique** (VIGINUM, Storm-1516, L2I, GLM26/LO + **Sun Tzu** & **Morelli 10 principes** dans `EXPERT_INFLUENCE\REFERENCES\`, ajoutés 2026-06-02) ; planification effets informationnels, cohérence inter-camps, transversal tous exercices |
| MINAUTORE | Claude (cloud) — claude-opus-4-7 | EXPERT_INFLUENCE, MASTAURIGE, SCÉNARISTE, ANALYSTE, ANALYSTE_ARN, ANALYSTE_BOT | Chef d'orchestre éditorial AURIGE 7BB — calendrier publications, cohérence narrative, programmation des injects *(dossier : `MINAUTORE\` — créé 2026-05-30)* |
| BROUILLON | deepseek-r1:14b | — *(bac à sable personnel utilisateur)* | Incubateur d'idées non abouties — IA **locale** pour **économiser les tokens** ; stockage d'idées brutes à travailler dans le temps *(dossier : `BROUILLON\` — créé 2026-06-02)* |

**Fichiers à mettre à jour si un agent est ajouté, supprimé ou change de modèle :**
1. **Ce registre ci-dessus** — la seule liste à éditer. ⚠ Mettre à jour le **compteur d'agents** dans `NOYAU\MEMOIRE.md` (= nombre de lignes de ce tableau).
2. `SYSTEME\ROUTAGE.md` — arbre de décision (logique de routage, pas une copie du registre).
3. `SYSTEME\PROMPTS\nom_agent.md` — créer / supprimer le prompt système.
4. Créer le dossier `NOM_AGENT\` avec `README.md` et `MEMOIRE.md`.

> `SYSTEME\CONFIG.md` et `SYSTEME\DOSSIER_POSTE.md` **ne contiennent plus de copie du registre** — ils renvoient ici. Rien à y modifier pour un simple ajout d'agent (sauf info infra spécifique : taille modèle dans CONFIG si nouveau modèle Ollama).

---

## Chemins permanents (ne changent pas)

| Ressource | Chemin |
|---|---|
| Bibliothèque d'assets (BDA) | `D:\CECPC\PRODUCTION\BDA\` |
| Index BDA | `D:\CECPC\PRODUCTION\BDA\_CATALOGUE.md` |
| Exercice AURIGE 2BB | `D:\CECPC\PRODUCTION\EXER\AURIGE 2BB` |
| Exercice ORION 26 | `D:\CECPC\PRODUCTION\EXER\01 ORION 26` |
| ComfyUI | `C:\Users\MTR\Documents\ComfyUI_windows_portable\ComfyUI` |
| Whisper | `..\models\audio_encoders\openai_whisper-large-v3-turbo` |
| Continue config | `C:\Users\MTR\.continue\config.yaml` |
| Portraits Mercure | `D:\CECPC\PRODUCTION\CREATION\02 - MERCURE\Portraits\` |
| Portraits Ruthnia Bella | `D:\CECPC\PRODUCTION\CREATION\07 - RUTHNIA BELLA\Portraits` |
| Politique RB — bios opposition | `D:\CECPC\PRODUCTION\CREATION\07 - RUTHNIA BELLA\POLITIQUE\Opposition BellaRussia.docx` |
| Avatars tweet AURIGE 2BB | `D:\CECPC\PRODUCTION\EXER\AURIGE 2BB\00_Boites à outils\MASTAURIGE\WEB\images\avatars tweet` |

---

## Vocabulaire géographique — GET (Grand East Territory)

**GET = Grand East Territory** — entité géopolitique fictive propre à l'univers Skolkan.

> **Définition :** Le GET est le regroupement régional fictif des pays de l'Est de l'univers Skolkan :
> **Mercure, Arnland / Dacie Romanie, Ruthnia Bella** (et tout futur pays fictif de la zone).
> Ce n'est PAS un remplacement systématique d'"Europe" — c'est une entité distincte.

**Règle d'utilisation :**
- **"Europe"** reste valide quand on parle des pays réels européens (France réelle, Allemagne, OTAN, ONU…)
- **"GET"** s'emploie quand le contexte désigne la zone géopolitique des **pays fictifs** de l'Est (Mercure, Arnland, DR, RB)
- Exemple : *"a scale the Grand East Territory has not seen in decades"* = les pays fictifs de l'Est, pas toute l'Europe réelle

**Fichiers à mettre à jour si le GET évolue (membres, frontières, dénomination) :**
- Ce fichier — section GET
- `GUILLAUME\MEMOIRE.md` — convention géographique
- `ANALYSTE\MERCURE\MEMOIRE.md` + `ANALYSTE\ARNLAND\MEMOIRE.md` + `ANALYSTE\BOTHNIA\MEMOIRE.md`
- `NOYAU\MEMOIRE.md`

---

## Règles de cohérence — checklist à appliquer

### Quand un agent est ajouté
- [ ] **Ajouter au registre ci-dessus** (seule liste à éditer)
- [ ] `NOYAU\MEMOIRE.md` — mettre à jour le compteur d'agents (= nb de lignes du registre)
- [ ] `SYSTEME\ROUTAGE.md` — ajouter la branche de routage de l'agent
- [ ] `SYSTEME\PROMPTS\nom_agent.md` — créer le prompt système
- [ ] `NOM_AGENT\README.md` et `NOM_AGENT\MEMOIRE.md` — créer les fichiers
- [ ] `SYSTEME\CONFIG.md` — **seulement si nouveau modèle Ollama** (ajouter sa taille) ; sinon rien (renvoie au registre)
- [ ] `SYSTEME\DOSSIER_POSTE.md` — rien (renvoie au registre)

### Quand le chemin racine change
- [ ] Mettre à jour ce fichier en premier
- [ ] `SYSTEME\CONFIG.md`
- [ ] `SYSTEME\DOSSIER_POSTE.md`
- [ ] `.claude\settings.local.json`
- [ ] Vérifier toutes les permissions avec `Grep("D:\\CECPC")`

### Propriétaire unique d'une fiche personnage — règle anti-divergence

> **Deux propriétaires complémentaires, jamais de copie ailleurs :**
> - **IDENTITÉ d'un persona/avatar** (handle, nom affiché, image/initiales, **CAMP** 🔴/🔵/⚪, parti) → **UNIQUEMENT le registre MASTAURIGE** : `MASTAURIGE\MEMOIRE.md` § « Avatars utilisés » (+ miroir machine `MASTAURIGE\WEB\avatars.js`).
> - **DOCTRINE narrative d'un personnage pays** (rôle, LO, positionnement, éléments de langage, emploi ILI) → **l'Analyste du pays**, qui **cite** le registre pour le camp (ne le redéfinit jamais).
>
> L'Analyste pays reste l'**autorité de décision** du camp (expertise politique) — mais le camp n'est **stocké qu'une fois**, dans le registre MASTAURIGE. Tous les autres agents (GUILLAUME, MINAUTORE, EXPERT_INFLUENCE, médias…) **citent**, ne recopient pas.

**Source de vérité par type :**
| Donnée | Propriétaire unique |
|---|---|
| Identité + **camp** d'un persona/avatar | `MASTAURIGE\MEMOIRE.md` (+ `avatars.js`) |
| Doctrine narrative — personnage **Mercure** | `ANALYSTE\MERCURE\MEMOIRE.md` *(cite le registre pour le camp)* |
| Doctrine narrative — **Arnland / Dacie Romanie** | `ANALYSTE\ARNLAND\MEMOIRE.md` *(idem)* |
| Doctrine narrative — **Bothnia** *(+ legacy RB AURIGE 2BB)* | `ANALYSTE\BOTHNIA\MEMOIRE.md` *(idem)* |

**Pourquoi :** divergences répétées du camp par recopie — Andrei Saniki (corrigé 2026-05-31) puis Svetlana Tikhanov (camp « bleu » recopié dans **7 fichiers**, faux : elle est 🔴 rouge pro-MER — corrigé 2026-06-01). Un inject construit sur la mauvaise valeur produit l'effet ILI **inverse**. D'où : **un seul endroit fait foi pour le camp**.

**Comment appliquer :**
- Avant d'attribuer un camp à un persona (inject, trombinoscope, mémoire) : **lire d'abord le registre MASTAURIGE** (+ `avatars.js`).
- Tout autre fichier qui mentionne le camp écrit un **renvoi** (« camp : voir registre MASTAURIGE ») — jamais une valeur figée non annotée.
- Décision/changement de camp d'un personnage pays : l'Analyste tranche, puis **met à jour le registre MASTAURIGE + avatars.js** (les deux), et les autres s'alignent.
- **Garde-fou automatique** : `MASTAURIGE\WEB\OUTILS\verifier_mastaurige.py` (CONTROLE G) signale tout tweet dont le camp **contredit durement** (rouge↔bleu) son avatar. Un avatar ⚪ neutre qui penche (façade de blanchiment, ex. @EastWatch_Intl) n'est PAS une divergence.
- Réflexe en cas de doute : `Grep` le nom du personnage sur tout le repo pour détecter les valeurs divergentes avant d'en ajouter une nouvelle.

### Règle de mise à jour automatique — OBLIGATOIRE

> **Après chaque avancée du projet, mettre à jour les fichiers concernés sans attendre que l'utilisateur le demande.**
> C'est un réflexe non négociable : chaque production validée, chaque décision prise, chaque contenu créé doit laisser une trace immédiate.

**Ce qui déclenche une mise à jour :**
- Un discours rédigé ou validé → `SCENARISTE\MEMOIRE.md`
- Un personnage créé ou complété → mémoire auto (`aurige_guillaume.md`) + `SCENARISTE\MEMOIRE.md`
- Un asset produit (portrait, voix, vidéo) → mémoire auto (tableau état de production)
- Une règle de production apprise → `SYSTEME\DOSSIER_POSTE.md`
- Un nouveau pattern de routage → `NOYAU\MEMOIRE.md`
- Un agent ajouté ou modifié → **tous les fichiers du registre** (voir checklist ci-dessus)
- Le chemin racine change → **tous les fichiers de chemin** (voir checklist ci-dessus)

**Fichiers de mémoire à maintenir en priorité :**
- `SCENARISTE\MEMOIRE.md` — narrative, discours, règles par exercice
- `NOYAU\MEMOIRE.md` — patterns de routage, préférences utilisateur
- `SYSTEME\DOSSIER_POSTE.md` — règles de production validées
- Mémoire auto Claude (`memory\aurige_guillaume.md`) — état de production personnages

### Après chaque session productive
- [ ] Mettre à jour `AGENT\MEMOIRE.md` des agents sollicités
- [ ] Mettre à jour `NOYAU\MEMOIRE.md` si nouveau pattern de routage appris
- [ ] Mettre à jour `SYSTEME\DOSSIER_POSTE.md` si nouvelle règle de production validée
- [ ] Mettre à jour `CONVERGENCE\SYNTHESE.md` si connaissance transversale dégagée
