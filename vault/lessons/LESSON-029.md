---
id: LESSON-029
aliases: ["LESSON-029"]
type: lesson
title: Clé dupliquée dans un literal dict Python — la dernière écrase les autres EN SILENCE
tags: [python, overrides, generateur, piege, validation]
source: ../../MASTORION/OUTILS/generer_bibliotheque.py
linkedTo: [LESSON-027, TOOL-016]
relevantFor: [mastorion, bibliotheques, outillage]
tier: 2
created: 2026-09-09
updated: 2026-09-09
---

# LESSON-029 — Le dict literal qui ment : 12 clés OVERRIDES en double

## Symptôme observé
`OVERRIDES` affichait `"@gavrilovborislav": ["ARN - PRO-MERCURE"]` à la ligne
79… et la sortie donnait `MER - MILITAIRE`. **12 clés existaient en double
dans le même literal** (3 fois pour Gavrilov) : le fichier mentait au lecteur.

## Cause racine
Python garde la DERNIÈRE occurrence d'une clé dupliquée dans un literal,
sans avertissement. Les couches d'audit successives ont été collées DANS le
même `{...}` au lieu de blocs `OVERRIDES.update({...})` (légitimes, lisibles).

## Correctif / règle à appliquer
- 17 entrées mortes purgées — sortie prouvée identique (empreinte avant/après).
- **Garde-fou `verifier_overrides_uniques()`** : la génération ÉCHOUE si une
  clé apparaît deux fois dans un même bloc (les couches `.update()` restent
  autorisées — vérification PAR bloc). Testé sur doublon simulé.
- Réflexe transposable : tout gros dict de configuration maintenu à la main
  mérite un contrôle d'unicité des clés à l'exécution.

## 🔗 Source de vérité
Détail / trace : voir `source:`. **Pointeur, pas copie.**
