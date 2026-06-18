---
id: LESSON-015
type: lesson
title: Outillage multi-exercice — zéro calendrier (ou contenu) d'exercice codé en dur
tags: [melmil, calendrier, generation, mastaurige, multi-exercice]
source: ../../MASTAURIGE/MEMOIRE.md
linkedTo: [PROJ-MASTAURIGE, PROJ-AURIGE-7BB]
relevantFor: [mastaurige, technique]
tier: 2
created: 2026-06-18
updated: 2026-06-18
---

# LESSON-015 — Ne jamais coder le calendrier d'un exercice en dur dans le moteur

## Symptôme observé
Dans MELMIL 7BB, **tout inject créé tombait en « À placer »** (overflow) au lieu de sa colonne jour. Pas seulement le STARTEX — **tous** les injects datés.

## Cause racine
`dayorderToISO()` (melmil.js) **convertissait le n° de jour en date avec un calendrier 2BB codé en dur** (D+26→35 = fin mai/début juin). En 7BB (D+33→41 = 23 juin→1 juil), la date calculée tombait hors `DAY_MAP` → overflow. Même cause pour la garde `d<=40` (excluait D+41) et la liste de colonnes `['d31'…'d40']` de `ensureDynRow`.

## Correctif / règle à appliquer
- **Le moteur ne contient AUCUNE valeur d'exercice en dur.** Tout ce qui dépend de l'exercice (calendrier, jours, séries→LO) est **dérivé d'une config générée** (`DAY_MAP`/`COL_TO_ISO` issus de `exercice_config.json`).
- Fix : `dayorderToISO(d)` retourne `COL_TO_ISO['d'+d]` ; gardes de plage remplacées par « le jour existe-t-il dans CE calendrier ? » ; colonnes dérivées de `DAY_MAP`.
- **Réflexe** : devant un bug « tout en À placer / hors colonne » après changement d'exercice → chercher une **borne de dates en dur** dans le moteur.
- Corollaire (même session) : pour réécrire un fichier de données JS, **échapper via `json.dumps` par objet** — un `esc()` maison qui oublie les `\n` (descriptions multi-lignes) casse le JS. Toujours `node --check` après génération.

## 🔗 Source de vérité
[[../../MASTAURIGE/MEMOIRE.md]] § « SOCLE MELMIL 7BB » + « 4 bugs STARTEX ». Voir [[PROJ-MASTAURIGE]].
