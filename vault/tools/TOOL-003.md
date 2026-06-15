---
id: TOOL-003
type: tool
title: GENERER_VIERGE.py
tags: [mastaurige, generateur, vierge]
source: ../../MASTAURIGE/MEMOIRE.md
linkedTo: [DECISION-001, TOOL-006]
relevantFor: [mastaurige]
tier: 2
created: 2026-06-12
updated: 2026-06-12
---

# TOOL-003 — GENERER_VIERGE.py

## Rôle
Produit le gabarit MASTAURIGE vierge (instance LOCALSTORAGE) à partir de la référence vivante.

## Garde-fou
Verrou **anti-rollback** (`--force-rollback`) : la vierge est la référence vivante ; la source 2BB est périmée → on ne régresse pas par mégarde.

## Emplacement
`OUTILS\GENERER_VIERGE.py` ; DST = `D:\CECPC\MASTAURIGE\LOCALSTORAGE_WEB_VERSION`.

## 🔗 Source de vérité
[[../../MASTAURIGE/MEMOIRE.md]]. Voir [[DECISION-001]].
