---
id: ARCH-002
type: architecture
title: Routage par modèle Ollama / co-résidence VRAM
tags: [architecture, agents, ollama, routage]
source: ../../SYSTEME/ROUTAGE.md
linkedTo: [ARCH-004]
relevantFor: [systeme, noyau]
tier: 2
created: 2026-06-12
updated: 2026-06-12
---

# ARCH-002 — Routage par modèle / co-résidence VRAM

## Principe
NOYAU (Claude cloud) orchestre les agents locaux groupés par **modèle Ollama** : deux agents partageant le même modèle sont **co-résidents en VRAM** (déductible de la colonne Modèle du registre, pas listé séparément).

## Groupes
- deepseek-r1:14b → PENSEUR, ANALYSTE(s), BROUILLON
- mistral-nemo → SECRÉTAIRE, SCÉNARISTE, VOIX, MASTODONTE, MASTAURIGE
- llama3.1:8b → ÉCLAIREUR, IMAGIER, CINÉASTE, ARCHIVISTE
- qwen2.5-coder:14b → ARCHITECTE
- Claude cloud → NOYAU, GUILLAUME, MINAUTORE, EXPERT_INFLUENCE

## Distinction
« Collabore avec » (thématique) ≠ co-résidence VRAM (déduite du modèle).

## 🔗 Source de vérité
[[../../SYSTEME/ROUTAGE.md]] · registre [[ARCH-004]] / [[../../CLAUDE.md]].
