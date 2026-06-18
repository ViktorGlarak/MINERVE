---
id: TOOL-011
type: tool
title: generer_melmil.py (import MELMIL unifié GESTIM + JEMM)
tags: [mastaurige, melmil, jemm, gestim, import]
source: ../../MASTAURIGE/MEMOIRE.md
linkedTo: [PROJ-AURIGE-7BB, DECISION-002]
relevantFor: [mastaurige, exercices, minautore]
tier: 2
created: 2026-06-17
updated: 2026-06-17
---

# TOOL-011 — generer_melmil.py

## Rôle
Importer la MELMIL dans MASTAURIGE depuis **GESTIM** (`.xls`) **ou** **JEMM** (`.json`, le nouveau logiciel), en produisant le même `melmil_data.js`. Réalise l'évolution « lecteur adaptatif » prévue de longue date.

## Usage
- Déposer les exports JEMM (`.json` ou dossiers EVENT extraits) dans `MELMIL\JEMM\`, puis `Actualiser_MELMIL.bat` (auto-détecte) ou `Actualiser_MELMIL_JEMM.bat`.
- `--source auto|gestim|jemm|both` · `--mode fusion|remplacer` (JEMM = **fusion** par défaut → préserve le socle ILI fait main ; dédup par `code`).
- Conversion code JEMM `EE.SS.Innn` → MELMIL `EE.SS.nni` (ex. `08.01.I01` → `08.01.01i`).
- `generate_data.py` (GESTIM seul) conservé en secours → **GESTIM jamais cassé**.

## Notes
EVENT_07 (ILI) sort vide de JEMM (contenu rouge produit par MINAUTORE) ; EVENT_08 (HOST NATION) = 8 injects ingérés (série 08.xx → ligne **HOST NATION** r6 du MELMIL).

## Source (vérité)
[[../../MASTAURIGE/MEMOIRE.md]] § « IMPORTATEUR MELMIL UNIFIÉ ». Exercice : [[PROJ-AURIGE-7BB]] ; pipeline injects : [[DECISION-002]].
