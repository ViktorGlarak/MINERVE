---
id: LESSON-017
type: lesson
title: Le chef d'orchestre de l'exercice est LE référent — le consulter en premier, jamais grep aveugle
tags: [minautore, guillaume, aurige, agents, methodo, exercices]
source: ../../AURIGE/MEMOIRE.md
linkedTo: [PROJ-AURIGE-7BB, AGENT-MINAUTORE, AGENT-GUILLAUME, TOOL-014, LESSON-018]
relevantFor: [minautore, exercices, mastaurige, analystes]
tier: 1
created: 2026-06-21
updated: 2026-06-21
---

# LESSON-017 — Le chef d'exercice est le référent : le consulter en premier

## Symptôme observé
Sur l'exercice MINOTAURE/7BB, je travaillais « à l'aveugle » (greps globaux pour savoir si un article est utilisé, quelle date, etc.) et j'exécutais les consignes mécaniquement sans piloter via l'agent **MINAUTORE** ni faire relire par les agents compétents. Demande **répétée** de l'utilisateur, non tenue.

## Cause racine
S'appuyer sur ma mémoire/ma bonne volonté pour « penser à utiliser l'agent » échoue. Et l'agent chef n'était pas exploité comme **oracle de l'exercice** (il doit savoir quel inject joue quand, quelle storyline/LO, quel persona, quel jour).

## Correctif / règle à appliquer
- **Réflexe n°1** : pour toute question « quel inject / date / persona / jour / cet article est-il utilisé ? » → consulter D'ABORD le **chef de l'exercice** (GUILLAUME 2BB · MINAUTORE 7BB) et sa **carte générée** ([[TOOL-014]] `MINAUTORE/ETAT_EXERCICE_7BB.md`), JAMAIS un grep aveugle.
- **Le chef pilote, ne décide pas seul** : faire relire/corriger par l'agent compétent — camp/persona → **ANALYSTE** du pays · ILI/PSYOPS/LO → **EXPERT_INFLUENCE** · rédaction → **SCÉNARISTE** · format → **MASTAURIGE**. Rapporter « validé/corrigé par X ».
- **Imposé par le système** (pas par ma mémoire) : hooks PostToolUse `minautore_agent_reminder.py` (7BB) + `aurige_methodo_reminder.py` (tout AURIGE). Capitalisé dans [[LESSON-018]] et `AURIGE/MEMOIRE.md`.

## 🔗 Source de vérité
Détail : `AURIGE/MEMOIRE.md` (§ Méthodologie de travail) + `MINAUTORE/MEMOIRE.md` + mémoire harness `feedback_agent_minautore_pilote_7bb`. **Pointeur, pas copie.**
