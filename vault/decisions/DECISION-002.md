---
id: DECISION-002
type: decision
title: Pipeline « inject as code »
tags: [mastaurige, injects, pipeline]
source: ../../MASTAURIGE/MEMOIRE.md
linkedTo: [DECISION-003, TOOL-007, DECISION-004]
relevantFor: [mastaurige, injects]
tier: 2
created: 2026-06-12
updated: 2026-06-12
---

# DECISION-002 — Pipeline « inject as code »

## Contexte / problème
Construire les injects d'un exercice de façon reproductible et versionnable, pas à la main dans l'outil.

## Décision
Plan JSON → `generer_injects.py` → session importable dans MELMIL. Les injects deviennent du code généré, rejouable.

## Pourquoi
Traçabilité, diff git, regénération en masse, cohérence avec `lo_config.js`. Évite la saisie manuelle source d'erreurs.

## Conséquences / à respecter
Le plan JSON est la matière éditable ; ne pas éditer la session générée à la main si on veut garder la regénération.

## 🔗 Source de vérité
[[../../MASTAURIGE/MEMOIRE.md]]. Voir aussi [[TOOL-007]].
