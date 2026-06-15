---
id: TOOL-006
type: tool
title: CONFIGURER_EXERCICE.py + exercice_config.json
tags: [mastaurige, config, exercice]
source: ../../MASTAURIGE/MEMOIRE.md
linkedTo: [TOOL-003, ARCH-003]
relevantFor: [mastaurige, exercices]
tier: 2
created: 2026-06-12
updated: 2026-06-12
---

# TOOL-006 — CONFIGURER_EXERCICE.py

## Rôle
À partir de `exercice_config.json`, régénère pour un exercice donné : `lo_config.js`, `melmil.js` (DAY_MAP), `melmil_ili.html` (thead/tbody/colgroup), `index_master.html` (onglets jours / DAY_OPTIONS / titre).

## Propriété
Idempotent ; détection d'ancre via `re.search` (évite les faux avertissements d'idempotence sur DAY_MAP / onglets).

## 🔗 Source de vérité
[[../../MASTAURIGE/MEMOIRE.md]]. Structure exercices : [[ARCH-003]].
