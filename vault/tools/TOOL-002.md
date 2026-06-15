---
id: TOOL-002
type: tool
title: verifier_mastaurige.py (contrôles A-I)
tags: [mastaurige, lint, qualite]
source: ../../MASTAURIGE/MEMOIRE.md
linkedTo: [LESSON-008, LESSON-001]
relevantFor: [mastaurige, qualite]
tier: 1
created: 2026-06-12
updated: 2026-06-12
---

# TOOL-002 — verifier_mastaurige.py

## Rôle
Lint de cohérence MASTAURIGE (contrôles A→I). Notamment **CONTROLE G** : tweet dont le camp contredit durement (rouge↔bleu) son avatar ; **H** : num/LO `tweets_data`↔`index_master` ; **I** : avatar↔trombino.

## Emplacement
`MASTAURIGE\WEB\OUTILS\verifier_mastaurige.py`.

## Réflexe
**Lancer en fin de session** avant de clôturer (cf. [[LESSON-008]]). Cause racine des alertes = vérité dupliquée → corriger à la source ([[LESSON-001]]).

## 🔗 Source de vérité
[[../../MASTAURIGE/MEMOIRE.md]].
