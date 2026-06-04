# DOSSIER DE POSTE — Production Médias Exercices de Crise
*Maintenu par Claude (NOYAU) après chaque session productive — dernière mise à jour : 2026-05-31*

---

## 1. MISSION ET CONTEXTE

Le titulaire du poste produit des **contenus médias réalistes** (images, vidéos, voix off, documents fictifs) pour des **exercices militaires et civils de gestion de crise**. Ces contenus servent à immerger les participants dans un scénario fictif crédible : reportages JT, tracts, messages de propagande, vidéos de terrain, etc.

Structure de rattachement : **CECPC**
Répertoire de travail principal : `D:\CECPC\PRODUCTION\`

---

## 2. EXERCICES EN COURS

### AURIGE 2BB — Scénario : GUILLAUME
- **Nature :** Exercice de production média IA — entraînement PC niveau **brigade** (2e Brigade Blindée)
- **Zone géographique :** Lorraine (HChâteau-Salins, HLunéville, HSarrebourg, HToul, HNancy)
- **Période scénario :** D+31 → D+41 (26 mai → 4 juin 2026)
- **Séries d'injects actives :** 04.01 (NRBC) · 07.01 → 07.08 · 08.01 → 08.03 (~45 injects)
- **Dossier :** `D:\CECPC\PRODUCTION\EXER\AURIGE 2BB`
- **Contexte scénario :** Présence de convois OTAN en Lorraine, accusations de pillages par des soldats, blocages routiers spontanés par des habitants, activité du groupe fictif N.O.M
- **Approche personnages :** Chaque personnage a un package complet — portrait (IMAGIER), voix (VOIX/OmniVoice), discours écrit selon sa personnalité (SCÉNARISTE)
- **Agents dédiés :** GUILLAUME (éditorial) · MASTAURIGE (tweets/RS) · EXPERT_INFLUENCE (doctrine ILI)

### AURIGE 7BB — Scénario : MINAUTORE
- **Nature :** Exercice de production média IA — entraînement PC niveau **brigade** (7e Brigade Blindée)
- **Statut :** En préparation — synchromatrice à ingérer (agent MINAUTORE initialisé le 2026-05-30)
- **Dossier :** `D:\CECPC\PRODUCTION\EXER\AURIGE 7BB`

### ORION 26 (O41)
- **Nature :** Grand exercice militaire multi-cellules
- **Zone géographique :** Vienne / Poitiers
- **Nations fictives :** Titane, Ostland, Bothnia
- **Outils spécifiques :** Plateforme sociale fictive Mastorion, outil MASSTALK V3
- **Dossier :** `D:\CECPC\PRODUCTION\EXER\01 ORION 26`

---

## 3. OUTILS ET STACK TECHNIQUE

### Génération d'images
| Outil | Usage | Priorité |
|---|---|---|
| **Adobe Firefly** | Images photorealistic (licence Adobe) | 1er choix |
| **Flow (Google)** | Images + texte intégré dans l'image | 2ème choix |
| **Gemini (Google)** | Itérations rapides, coques UI | 3ème choix |

**Règle Flow :** Flow gère très bien le texte long dans les images — toujours inclure le texte verbatim dans le prompt.
**Règle Gemini :** Gemini ne rend pas bien le texte long — utiliser overlay Premiere Pro pour le texte exact.

### Génération vidéo
| Outil | Usage |
|---|---|
| **ComfyUI + LTX 2.3** | Animation image→vidéo (i2v) et image+audio→vidéo (ia2v) |
| **Adobe Premiere Pro** | Montage final, overlays logos, assemblage clips |

**Workflow vidéo validé :**
1. Générer l'image source (Firefly > Flow > Gemini)
2. Animer avec LTX 2.3 dans ComfyUI (i2v ou ia2v selon besoin audio)
3. Assembler dans Premiere Pro + overlays logos (mode Multiply)

**LTX ia2v (image + audio → vidéo) :** utilisé quand il y a une piste son (voix off, synchro labiale). La durée du clip = durée exacte de l'audio.

### Génération de voix
| Outil | Usage |
|---|---|
| **OmniVoice TTS** (dans ComfyUI) | Génération et clonage de voix pour voix off |

**Deux modes :**
- **Voice Clone** : clonage depuis audio de référence (nécessite Whisper ASR)
- **Voice Design** : création depuis attributs (genre, âge, ton, accent)

**Profils voix validés :**
- Journaliste FR féminine : Voice Clone, réf. Claire Chazal, steps=64, speed=0.95
- Expert sécurité : Voice Clone (si audio dispo) ou Voice Design male/middle-aged/low pitch, steps=64, speed=0.90
- Citoyen FR : Voice Design, steps=32, class_temperature=1.0

**Modèle Whisper installé :** `openai/whisper-large-v3-turbo`
Chemin : `C:\Users\MTR\Documents\ComfyUI_windows_portable\ComfyUI\models\audio_encoders\openai_whisper-large-v3-turbo`

### Modèles IA locaux (Ollama) et agents

> **Registre complet des agents (modèle, collaborations, rôle) → `IA\MINERVE\CLAUDE.md`, section « Registre des agents ».** Source unique, à jour. Ne pas recopier la liste ici.
>
> Arbre de décision « quel agent pour quelle tâche » → `IA\MINERVE\SYSTEME\ROUTAGE.md`.

---

## 4. IDENTITÉS FICTIVES RÉCURRENTES

### Groupe N.O.M (Novus Ordo Mundi)
- **Nature :** Groupe fictif d'extrême-gauche violent, antifasciste radical
- **Logo :** Crâne dans triangle pointe en bas + flèche horizontale traversante
- **Palette :** Noir, rouge, orange — style stencil street art
- **Porte-parole :** Wilma SMASTEN
- **Activités dans les exercices :** Tags, tracts, menaces, propagande
- **Assets BDA :** `D:\CECPC\PRODUCTION\BDA\02 - MERCURE\N.O.M\`
- **Règle Premiere Pro :** Logo N.O.M en overlay PNG mode Multiply (noir sur fond = transparent)

---

## 5. RÈGLES DE PRODUCTION IMPORTANTES

### Prompts image
- Texte fourni par l'utilisateur = copié **mot pour mot** dans le prompt (jamais résumé)
- Ne jamais utiliser "protesters" pour des scènes civiles → génère drapeaux syndicaux (CGT)
- Remplacer par : `local residents`, `ordinary civilians`, `local people`
- Double verrouillage anti-drapeaux : positif ET négatif simultanément
- Pour les scènes de blocage : préciser `no flags of any kind, people holding only handwritten cardboard signs`

### Prompts LTX 2.3
- Format : paragraphe unique fluide, verbes au présent, 4-8 phrases
- Mouvement uniquement (le contenu visuel est dans l'image source)
- ia2v = synchro labiale TOUJOURS dans le prompt
- Logos et texte précis → overlay Premiere Pro (pas LTX)
- Paramètres par défaut : force=0.70, LoRA strength=0.50, fps=24
- Talking head : force=0.65, LoRA=0.60

### Texte TTS OmniVoice
- "HSarrebourg" → "Sarrebourg" (H = préfixe exercice, non prononcé)
- "HNancy" → "Nancy"
- "N.O.M." avec points → diction lettre par lettre
- Ponctuation soignée = intonation correcte

---

## 6. BIBLIOTHÈQUE D'ASSETS (BDA)
Chemin : `D:\CECPC\PRODUCTION\BDA`
Index central : `D:\CECPC\PRODUCTION\BDA\_CATALOGUE.md`
Tout asset réutilisable (image, audio, vidéo) doit être archivé ici avec fiche d'identité.

---

## 7. SYSTÈME MINERVE
Chemin : `D:\CECPC\PRODUCTION\IA\MINERVE`
Interface principale : **Claude Code** (VSCode)
Interface agents locaux : **Continue** (VSCode, config `C:\Users\MTR\.continue\config.yaml`)

---
*Ce fichier est mis à jour par Claude (NOYAU) après chaque session productive.*
