---
id: DECISION-003
type: decision
title: lo_config.js — source unique séries→LO
tags: [mastaurige, melmil, lo, source-unique]
source: ../../MASTAURIGE/MEMOIRE.md
linkedTo: [DECISION-004, LESSON-001, ARCH-001]
relevantFor: [mastaurige, melmil]
tier: 2
created: 2026-06-12
updated: 2026-06-12
---

# DECISION-003 — lo_config.js, source unique séries→LO

## Contexte / problème
Le mapping série d'inject → ligne d'objectif (LO) était dupliqué, risque de divergence.

## Décision
`lo_config.js` = **source unique** du routage séries→LO, consommée par MELMIL et les générateurs.

## Pourquoi
Applique la règle « propriétaire unique » au code : un seul endroit fait foi (cf. [[LESSON-001]], [[ARCH-001]]).

## Conséquences / à respecter
Tout nouveau routage série→LO se déclare ici, jamais en dur ailleurs.

## 🔗 Source de vérité
[[../../MASTAURIGE/MEMOIRE.md]] § MELMIL v0.2.
