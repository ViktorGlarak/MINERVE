---
id: LESSON-009
type: lesson
title: Prompts image — scènes civiles sans drapeaux + texte verbatim
tags: [image, prompt, realisme, production]
source: ../../SYSTEME/DOSSIER_POSTE.md
linkedTo: [TOOL-010, ARCH-006]
relevantFor: [production, image]
tier: 2
created: 2026-06-15
updated: 2026-06-15
---

# LESSON-009 — Règles de prompt image

## Symptôme observé
« protesters » génère des drapeaux syndicaux (CGT) → casse le réalisme de scènes civiles spontanées. Texte résumé → image incorrecte.

## Correctif / règle à appliquer
- Pour scènes civiles : `local residents`, `ordinary civilians`, `local people` — **jamais** « protesters ».
- **Double verrouillage anti-drapeaux** (positif ET négatif) : `no flags of any kind, people holding only handwritten cardboard signs`.
- Texte fourni par l'utilisateur = copié **mot pour mot** dans le prompt, jamais résumé (Flow gère le texte long).

## 🔗 Source de vérité
[[../../SYSTEME/DOSSIER_POSTE.md]] §5. Outil : [[TOOL-010]].
