---
id: DECISION-007
type: decision
title: Starter Package — code réservé 00.00.00i (carte ghost MELMIL)
tags: [mastaurige, melmil, starter, convention, 7bb]
source: ../../MASTAURIGE/MEMOIRE.md
linkedTo: [PROJ-AURIGE-7BB, PROJ-MASTAURIGE, ARCH-008]
relevantFor: [mastaurige, exercices, minautore]
tier: 2
created: 2026-06-18
updated: 2026-06-18
---

# DECISION-007 — Starter Package : code réservé `00.00.00i`

## Décision
Un **« Starter Package »** = lot d'articles donné aux joueurs au **démarrage** d'un exercice (7BB : le 23 juin / D+33) pour poser la **ligne de conduite / structure politique**. Ces injects **n'ont pas de vrai numéro** → on leur réserve le code **`00.00.00i`**.

## Comportement (convention moteur, intégrée vierge + collab + 7BB)
- La série `00` étant inconnue du plan, MELMIL place l'incident sur la **ligne r7 GHOST** automatiquement ; `melmil.js` l'**étiquette « 📦 STARTER PACKAGE »** (sinon `inj.sujet`).
- Les cartes se colorent **par camp** (autorité qui parle) : 🔴 / 🔵 / ⚪.
- Articles déjà rédigés (`.html` riches) = créations **`external:true` + `file`** → `CR_previewArticle` ouvre le **vrai `.html` en iframe** (pas de re-rendu). Auto-injectées (idempotent) par `moteur/starter_package.js`.

## Pourquoi
Donner aux joueurs un cadrage politique commun **sans polluer la numérotation** des injects ILI/HN, tout en restant visible et rangé (ghost) dans la synchromatrice.

## Source (vérité)
[[../../MASTAURIGE/MEMOIRE.md]] § « STARTER PACKAGE ». Exercice : [[PROJ-AURIGE-7BB]] ; collaboratif : [[ARCH-008]].
