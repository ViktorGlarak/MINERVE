---
id: TOOL-005
type: tool
title: Console MASTER (fusion / renumérotation / actus)
tags: [mastaurige, master, base]
source: ../../MASTAURIGE/MEMOIRE.md
linkedTo: [DECISION-001, TOOL-004]
relevantFor: [mastaurige, base]
tier: 2
created: 2026-06-12
updated: 2026-06-12
---

# TOOL-005 — Console MASTER (EXE_MASTER_VERSION)

## Rôle
Poste BASE : consolide les exports traitants, renumérote, fabrique les **packages actus** à envoyer aux joueurs, compresse les images, gère mode fichier / sélection à publier / ledger.

## Workflow
Exporter modifs traitants → récupérer fichiers → `MASTER.bat` → packages actus → diffusion joueurs + introduction BASE/traitants.

## Détail technique
Stamp `%Y%m%d%H%M%S` (évite collision même minute qui fusionnait les dossiers actus).

## 🔗 Source de vérité
[[../../MASTAURIGE/MEMOIRE.md]]. Voir [[DECISION-001]], [[TOOL-004]].
