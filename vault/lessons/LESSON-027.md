---
id: LESSON-027
aliases: ["LESSON-027"]
type: lesson
title: Import MASTORION — deux fiches partageant email ou masto_id fusionnent EN SILENCE
tags: [mastorion, import, personas, gavrilov, integrite]
source: ../../MASTORION/JOURNAL.md
linkedTo: [DECISION-013, ARCH-011, TOOL-016]
relevantFor: [mastorion, bibliotheques]
tier: 2
created: 2026-09-09
updated: 2026-09-09
---

# LESSON-027 — La fusion silencieuse à l'import (leçon Gavrilov)

## Symptôme observé
Le classeur contenait 2 lignes Gavrilov (`@GavrilovBorislav` AURIGE et
`@The_Grass_hopper` ORION) ; après import, la base n'en avait qu'UNE.
Le compte joué dans les injects AURIGE avait disparu sans aucun message.

## Cause racine
L'upsert d'import remonte par `masto_id` PUIS par `email` avant le username :
deux fiches distinctes partageant l'un des deux sont considérées comme le
même compte — la seconde écrase/absorbe la première, en silence.

## Correctif / règle à appliquer
- **Deux fiches distinctes DOIVENT avoir `email` et `masto_id` distincts** —
  garanti côté générateur (`clarifier_comptes_multiples()`) ET codé dans le
  nouvel import EHO : upsert par **username seul**, collision email/masto_id
  → **ligne refusée avec message** ; compte humain → refusé.
- Comptes joueurs en domaine dédié `@eho.mastorion.local` (jamais
  `@mastorion.local`, réservé aux personas).
- Réflexe : après tout import, comparer compte attendu / compte en base.

## 🔗 Source de vérité
Détail / trace : voir `source:`. **Pointeur, pas copie.**
