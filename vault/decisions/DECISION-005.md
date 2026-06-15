---
id: DECISION-005
type: decision
title: Format codes incident 2 ou 3 chiffres
tags: [mastaurige, melmil, codes]
source: ../../MASTAURIGE/MEMOIRE.md
linkedTo: [DECISION-002]
relevantFor: [mastaurige, melmil]
tier: 3
created: 2026-06-12
updated: 2026-06-12
---

# DECISION-005 — Codes incident XX.YY.ZZ ou ZZZ

## Contexte / problème
Renumérotation forcée dès qu'un incident dépassait 99 (ex. 01.01.119).

## Décision
Supporter `XX.YY.ZZ` **OU** `XX.YY.ZZZ` partout (`bridgeCode` + `normalizeIncident` assouplis en `\d{2,3}`).

## Pourquoi
Éviter les renumérotations cosmétiques ; 01.01.119 devient valide.

## Conséquences / à respecter
Générateur `.bat` déjà verbatim ; convention suffixes extensions éditoriales conservée.

## 🔗 Source de vérité
[[../../MASTAURIGE/MEMOIRE.md]].
