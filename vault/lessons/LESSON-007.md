---
id: LESSON-007
type: lesson
title: Bloc parseur non borné → record poubelle
tags: [parser, python, mastaurige, regex]
source: ../../MASTAURIGE/MEMOIRE.md
linkedTo: [TOOL-001, LESSON-002]
relevantFor: [mastaurige, trombino, parser]
tier: 2
created: 2026-06-12
updated: 2026-06-12
---

# LESSON-007 — Bloc non borné → fiche poubelle

## Symptôme observé
Fiche « Andrei Saniki » gonflée (Objectifs 17, Faiblesses 18) contenant le parcours de Koho ; 3 officiers (Kosmannen/Koho/Groop) absents.

## Cause racine
Le dernier bloc militaire « 3. » n'avait pas d'en-tête suivant → il **avalait tout le document** ; `re.search` du Nom sautait le « Nom : » qui échoue et s'accrochait au 1er couple Nom/Prénom valide en aval (SANIKI). En-têtes irréguliers (« Nom : » suivi direct de « Parcours », pas d'en-tête du tout).

## Correctif / règle à appliquer
**Borner** le scan d'une section à son marqueur de fin (ici « OPPOSITION POLITIQUE »). Pour les enregistrements à format cassé : extraction ciblée par marqueurs uniques (`sub_lines`). Toujours réconcilier sources↔sortie après coup.

## 🔗 Source de vérité
[[../../MASTAURIGE/MEMOIRE.md]]. Outil : [[TOOL-001]]. Voir aussi [[LESSON-002]].
