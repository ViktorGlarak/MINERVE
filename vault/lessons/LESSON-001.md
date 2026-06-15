---
id: LESSON-001
type: lesson
title: Anti-divergence camp — propriétaire unique
tags: [coherence, camp, source-unique, ili]
source: ../../CLAUDE.md
linkedTo: [ARCH-001, TOOL-002, DECISION-003]
relevantFor: [mastaurige, analystes, exercices]
tier: 1
created: 2026-06-12
updated: 2026-06-12
---

# LESSON-001 — Anti-divergence du camp (propriétaire unique)

## Symptôme observé
Camp d'un persona recopié faux dans plusieurs fichiers : Svetlana Tikhanov marquée « bleu » dans **7 fichiers** alors qu'elle est 🔴 rouge pro-MER → un inject bâti dessus produit l'effet ILI **inverse**.

## Cause racine
Vérité **dupliquée** : le camp était recopié au lieu d'être référencé.

## Correctif / règle à appliquer
**Un seul endroit fait foi** : identité + camp d'un avatar = registre MASTAURIGE (+ `avatars.js`). Tous les autres fichiers **citent** (« camp : voir registre MASTAURIGE »), ne recopient pas. Avant d'attribuer un camp : lire le registre. En cas de doute : `Grep` le nom sur tout le repo.

## 🔗 Source de vérité
[[../../CLAUDE.md]] § « Propriétaire unique ». Garde-fou : [[TOOL-002]] (CONTROLE G). Principe : [[ARCH-001]].
