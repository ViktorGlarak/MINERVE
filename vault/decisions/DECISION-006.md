---
id: DECISION-006
type: decision
title: Trombino — pages A3 auto + bande bio + cache-buster
tags: [mastaurige, trombinoscope]
source: ../../MASTAURIGE/MEMOIRE.md
linkedTo: [TOOL-001, LESSON-002]
relevantFor: [mastaurige, trombino]
tier: 2
created: 2026-06-12
updated: 2026-06-12
---

# DECISION-006 — Trombinoscope : pages A3 auto + bande bio

## Contexte / problème
Les fiches bio manquantes déversées en bloc cassaient la mise en page A3 ; cache navigateur servait l'ancien `bios.js`.

## Décision
Pages pays **intactes** (cartes existantes rendues cliquables) + fiches manquantes en **bande `.bio-band`** au bas de la page pays, groupée par rôle. `.page` en **hauteur auto** (plus de `height:283mm; overflow:hidden`). Cache-buster `bios.js?v=<timestamp>`.

## Pourquoi
Garder la présentation Mercure-style + ajouter le clic→pop-up bio sans casser le layout.

## Conséquences / à respecter
Après régénération : **hard-refresh Ctrl+Shift+R**. Rename « Dacie Romanie → Arnland » appliqué (DR = Arnland).

## 🔗 Source de vérité
[[../../MASTAURIGE/MEMOIRE.md]]. Outil : [[TOOL-001]].
