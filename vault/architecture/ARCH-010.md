---
id: ARCH-010
type: architecture
title: Base vs évolution — la vierge/.docx = base, les spécificités exercice vivent dans le générateur (patch/flag)
tags: [mastaurige, vierge, minotaure, trombino, base, evolution]
source: ../../ANALYSTE/ARNLAND/MEMOIRE.md
linkedTo: [TOOL-001, TOOL-003, TOOL-016, PROJ-MASTAURIGE]
relevantFor: [mastaurige, exercices, arnland]
tier: 2
created: 2026-06-25
updated: 2026-06-25
---

# ARCH-010 — Séparer la BASE (vierge) de l'ÉVOLUTION (exercice)

## En une phrase
Tout ce qui est **spécifique à un exercice** (évolution d'une fiche, capacité joueur) vit dans le **générateur**, jamais dans la base : la **vierge** régénère depuis le **`.docx`** et reste **propre** pour le prochain exercice.

## Deux applications (2026-06-25)
- **`BIO_PATCH_MINOTAURE`** (dans [[TOOL-001]] `generer_trombino_bios.py`, MINOTAURE seulement) : fait évoluer une fiche bio **après parsing** du `.docx` (ex. Promesy 20 %→30 % d'origine MER + « cœur des combats » ; Martin → 2 700 hab.). La **VIERGE** (générateur **sans** ce patch) garde la **base** ; le `.docx` n'est **jamais** édité. Vérification : vierge=20 % vs MINOTAURE=30 %.
- **Flag `window.EHO_EDITABLE`** : la capacité d'**édition joueur** ([[TOOL-016]]) n'apparaît **que** dans le kit JOUEURS (flag injecté à la génération par [[TOOL-003]]/[[TOOL-016]]). L'animateur garde le comportement de base (lecture seule).

## Règle
Faire évoluer un contenu en cours d'exo → **patch/flag dans le générateur**. Ne JAMAIS éditer le `.docx` ni la vierge. Toujours **vérifier la séparation** base↔évolution après régénération.

## 🔗 Source de vérité
Détail bio : `ANALYSTE/ARNLAND/MEMOIRE.md` · outillage : `MASTAURIGE/MEMOIRE.md` (2026-06-25). **Pointeur, pas copie.**
