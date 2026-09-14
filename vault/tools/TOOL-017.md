---
id: TOOL-017
aliases: ["TOOL-017"]
type: tool
title: lib/bio.ts — rendre lisibles les bios de la bibliothèque sans les modifier
tags: [eho, pleiade, bios, countrybook, lisibilite, tests]
source: ../../PLEIADE/MEMOIRE.md
linkedTo: [DECISION-016, LESSON-032]
relevantFor: [pleiade, exercices, mastaurige]
tier: 2
created: 2026-09-14
updated: 2026-09-14
---

# TOOL-017 — Mise en forme des bios (`src/lib/bio.ts`)

## Le constat
Les 262 bios de la bibliothèque ne contiennent **aucun saut de ligne**, et la
plus longue fait **3 006 caractères** d'une seule coulée. Affichées telles
quelles, elles donnent un mur vertical illisible.

Mais beaucoup **portaient déjà une structure** que l'affichage écrasait :

| Famille | Nombre | Forme réelle |
|---|---|---|
| Fiches de countrybook | **57** | `Parcours : … \| Objectifs : … ; … ; … \| Forces : …` |
| Bio en Markdown | 1 | `**Mode opératoire** - … - …` (astérisques affichées telles quelles) |
| Prose continue | ~204 | un seul bloc |

Les 57 premières sont les plus importantes : chefs d'État et figures des
countrybooks (Peters, Danevois, Radulov, Volkonsky, Schmit, Tikhanov, Saniki…).

## Ce que fait l'outil
Il **reconnaît** la structure et la restitue en rubriques et en listes ; la
prose continue est aérée en paragraphes par regroupement de phrases — sans
jamais couper une phrase en deux.

⚠ **Règle absolue : rien n'est réécrit.** Une bio d'exercice est une donnée de
référence ; on n'ajoute, ne retire ni ne déplace un mot.

## Le test est la partie qui compte
`npm run test:bio` passe la mise en forme sur **les 262 bios réelles de la
base**, avec une exigence unique : **le texte recollé doit être identique à
l'original**, aux seules marques de formatage près. **538/538.**

Ce test a attrapé **deux bugs invisibles à l'œil** : une expression régulière
qui appariait les astérisques de travers (fermeture d'un gras avec l'ouverture
du suivant, découpant une fiche en morceaux absurdes), et tout mot en gras
promu au rang de titre de rubrique.

Le plus long bloc affiché est passé de **1 411 à 612 caractères**.
