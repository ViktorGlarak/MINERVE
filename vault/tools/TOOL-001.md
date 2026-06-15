---
id: TOOL-001
type: tool
title: generer_trombino_bios.py
tags: [mastaurige, trombinoscope, python, parser]
source: ../../MASTAURIGE/MEMOIRE.md
linkedTo: [DECISION-006, LESSON-002, LESSON-007]
relevantFor: [mastaurige, trombino]
tier: 2
created: 2026-06-12
updated: 2026-06-12
---

# TOOL-001 — generer_trombino_bios.py

## Rôle
Parse 3 fiches bio (docx Arnland + docx/odt Bothnia) → écrit `Sites/Trombinoscope/bios.js` (`window.TROMBI_BIOS`, 45 fiches) → injecte un bloc idempotent `<!-- BIOS:START/END -->` (CSS + pop-up + cartes cliquables) dans `ACTEURS_A3_model.html`.

## Emplacement
`D:\CECPC\MASTAURIGE\LOCALSTORAGE_WEB_VERSION\OUTILS\` (+ copie dans l'instance 7BB).

## Points de vigilance (cf. leçons)
Formats Word/ODT irréguliers : espaces insécables dans les labels, en-têtes manquants, blocs non bornés → voir [[LESSON-002]] et [[LESSON-007]]. **Après tout changement : auditer fusion** (Forces>5/Faiblesses>6/Objectifs>6) + réconcilier sources↔bios.js + `node --check` du pop-up.

## 🔗 Source de vérité
[[../../MASTAURIGE/MEMOIRE.md]] § trombino.
