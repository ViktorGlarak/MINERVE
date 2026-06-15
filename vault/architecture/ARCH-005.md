---
id: ARCH-005
type: architecture
title: Boucle QC — NOYAU évalue chaque réponse agent
tags: [architecture, qc, noyau, agents]
source: ../../SYSTEME/QC.md
linkedTo: [ARCH-001, ARCH-002, PROJ-MINERVE]
relevantFor: [systeme, noyau]
tier: 2
created: 2026-06-15
updated: 2026-06-15
---

# ARCH-005 — Boucle de contrôle qualité (QC)

## Principe
Chaque réponse d'un agent Ollama est **interceptée et évaluée par NOYAU (Claude)** avant d'arriver à l'utilisateur. PASS → transmise + mémoire MAJ. FAIL → relance (max 2) puis Claude complète lui-même, et la **leçon est consignée** dans `AGENT/MEMOIRE.md`.

## 5 critères
Complétude (éliminatoire) · Précision (éliminatoire) · Clarté · Format · Pertinence.

## Enrichissement du prompt (avant appel agent)
NOYAU injecte : prompt système de l'agent + entrées pertinentes de sa mémoire + patterns connus. Après coup : « Patterns efficaces » / « Patterns à éviter ».

## 🔗 Source de vérité
[[../../SYSTEME/QC.md]]. Routage : [[ARCH-002]].
