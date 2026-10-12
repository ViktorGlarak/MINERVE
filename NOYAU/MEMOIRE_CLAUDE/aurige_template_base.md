---
name: aurige-template-base
description: "AURIGE sert de base d'initialisation pour tout nouvel agent éditorial d'exercice — template SYSTEME\\PROMPTS\\aurige.md contient la doctrine neutre transférable"
metadata: 
  node_type: memory
  type: project
  originSessionId: 4a1937f0-0fee-4e67-a37d-d5d8338f7301
---

**AURIGE = base d'initialisation pour les agents exercice CECPC**

Le fichier `SYSTEME\PROMPTS\aurige.md` est le **template de référence** : copier pour initialiser tout nouvel agent éditorial d'exercice (MINAUTORE pour 7BB, futurs agents).

**Éléments universels dans ce template (ne pas modifier sans validation) :**
- Univers Skolkan : acteurs permanents GET (Olamao, Pallesson, Youkachenko), citations canoniques, règle Ruthnia Bella, règle GET
- Camps BLEU/ROUGE/GRIS + médias fictifs (Today Mercure, BC1, TV4, HEXAGONE)
- 5 LO GLM26 (LO1→LO5, source GLM26_Matrice ILI-FORAD.pptx)
- Règles cohérence narrative : CLIMAX, noyau de vérité 80/20, équilibre camps, neutralité visuelle tweets, règle LO
- Steps PSYOPS (Step 1→2→3, ne jamais sauter)
- Catalogue séries ILI 07.01→08.03
- Règle H-préfixe (ville réelle → H+nom)
- Doctrine calibration brigade : max 1-2 stratégiques/semaine + catalogue 15 types injects locaux
- Architecture dossier exercice : 6 dossiers numérotés 00→05, nommage D+XX_JJ_MOIS
- Framework agents (MASTAURIGE + agent exercice + ANALYSTE pays = 90% des cas)

**Sections ⚠️ à compléter pour chaque exercice :**
- H-codes spécifiques de la ZO
- Brigade/unité entraînée
- Game Plan / synchromatrice / dates réelles
- Acteurs locaux fictifs

**Procédure de création d'un nouvel agent exercice :**
1. Copier `SYSTEME\PROMPTS\aurige.md` → `SYSTEME\PROMPTS\[agent].md`
2. Compléter les sections ⚠️ avec les données de l'exercice
3. Créer `[AGENT]\README.md` et `[AGENT]\MEMOIRE.md` avec la doctrine AURIGE héritée
4. Enregistrer dans CLAUDE.md, CONFIG.md, ROUTAGE.md, NOYAU\MEMOIRE.md
5. Créer `AURIGE\AURIGE_[UNITE]\MEMOIRE.md`

**Why:** L'utilisateur a demandé que AURIGE conserve les éléments transférables et serve de base neutre pour les futurs agents exercice — formalisé le 2026-05-31 lors de la création de MINAUTORE.

**How to apply:** À chaque création d'un agent exercice type GUILLAUME/MINAUTORE, partir de ce template. Ne jamais créer un agent exercice de zéro.

Voir aussi : [[minautore-agent]] [[expert_influence]]
