---
id: ARCH-001
type: architecture
title: Vault MINERVE — source de vérité unique
tags: [architecture, coherence, source-unique, obsidian]
source: ../../CLAUDE.md
linkedTo: [LESSON-001, ARCH-004]
relevantFor: [systeme, tous]
tier: 1
created: 2026-06-12
updated: 2026-06-12
---

# ARCH-001 — Source de vérité unique + propriétaire unique

## Principe
Le système MINERVE est un vault Obsidian bâti sur **une seule source de vérité par donnée**. Chaque fait a **un propriétaire** ; les autres fichiers **renvoient**, ne recopient pas.

## Application
- Registre des agents → [[../../CLAUDE.md]] (unique).
- Identité + camp d'un avatar → registre MASTAURIGE + `avatars.js`.
- Doctrine pays → l'Analyste du pays. Doctrine ILI → EXPERT_INFLUENCE.
- Le présent **vault atomique** respecte la règle : ses notes **lient** (`source:`), ne dupliquent pas.

## Pourquoi
La duplication a causé des bugs réels ([[LESSON-001]] : camp inversé dans 7 fichiers → effet ILI inverse).

## 🔗 Source de vérité
[[../../CLAUDE.md]] · carte : [[../../MINERVE_HOME.md]].
