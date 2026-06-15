---
id: LESSON-012
type: lesson
title: Auditer le vault contre les countbooks SOURCES, pas seulement les mémoires
tags: [vault, countbook, audit, coherence, analystes]
source: ../../CLAUDE.md
linkedTo: [LESSON-001, ENT-karpovitch, ENT-bothnia]
relevantFor: [analystes, exercices, vault]
tier: 2
created: 2026-06-15
updated: 2026-06-15
---

# LESSON-012 — Auditer le vault contre les countbooks sources

## Symptôme observé
Le vault (sourcé sur les `ANALYSTE/<pays>/MEMOIRE.md`) couvrait tout le **principal**, mais en comparant aux **countbooks ORION originaux** (`D:\CECPC\DOC REF\COUNTRY BOOK\*.docx`), il manquait des figures profondes (députés, sous-chefs police, porte-parole de partis, présidents régionaux, commissions…) — **71 oublis**. Et une **divergence de nom** : Bothnia « chef de la Police » = **Karpovitch** (countbook) vs **Richter** (mémoire/vault) → [[ENT-karpovitch]].

## Cause racine
Les `MEMOIRE.md` des analystes sont des **synthèses** du countbook : elles omettent du détail et peuvent **diverger** (transcription, version exercice). Auditer la mémoire ≠ auditer la source.

## Correctif / règle à appliquer
- Pour une **complétude** réelle d'un pays : comparer le vault aux **countbooks .docx sources** (annexes « Leading Figures / Personalities »), pas seulement à la mémoire.
- Une **divergence de nom** countbook↔mémoire ne se corrige PAS en silence : créer la fiche en **annotant la divergence** et laisser l'analyste/utilisateur arbitrer (cf. [[LESSON-001]] : un seul propriétaire, mais l'arbitrage est humain).
- Méthode : extraire le texte du `.docx` (zip → `word/document.xml`), localiser les annexes nominatives, diff par nom de famille contre `vault/entities/`.

## 🔗 Source
[[../../CLAUDE.md]] (règle propriétaire unique) ; countbooks `DOC REF\COUNTRY BOOK`.
