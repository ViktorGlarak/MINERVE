---
id: LESSON-002
type: lesson
title: Espace insécable dans les labels → fusion de sections
tags: [parser, python, odt, docx, mastaurige]
source: ../../MASTAURIGE/MEMOIRE.md
linkedTo: [TOOL-001, LESSON-007]
relevantFor: [mastaurige, trombino, parser]
tier: 2
created: 2026-06-12
updated: 2026-06-12
---

# LESSON-002 — Espace insécable (\xa0) dans les labels de bio

## Symptôme observé
Faiblesses de LINDQUIST absentes du trombino ; section « Forces » à 8 items au lieu de 4.

## Cause racine
Le `.odt` écrit « Faiblesses **\xa0**/ défis / préoccupations : » (espace **insécable** DANS le label). La classe de caractères `[A-Za-zÉéÀ-ÿ /]` du regex ne le matchait pas → label non reconnu → ses lignes **avalées dans la section précédente**.

## Correctif / règle à appliquer
Normaliser `l = l.replace("\xa0", " ")` avant toute détection de label. **Réflexe** : après modif parseur, auditer la fusion (Forces>5 / Faiblesses>6 / Objectifs>6 = suspect).

## 🔗 Source de vérité
[[../../MASTAURIGE/MEMOIRE.md]]. Outil : [[TOOL-001]].
