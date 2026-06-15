---
id: ARCH-007
type: architecture
title: Roadmap technique MINERVE (RAG · CONVERGENCE · orchestrateur autonome)
tags: [architecture, roadmap, rag, fine-tuning]
source: ../../SYSTEME/CONFIG.md
linkedTo: [ARCH-001, ARCH-002, PROJ-MINERVE]
relevantFor: [systeme, noyau]
tier: 3
created: 2026-06-15
updated: 2026-06-15
---

# ARCH-007 — Roadmap technique MINERVE

## Prochaines étapes prévues (CONFIG.md)
1. **Orchestrateur autonome** : script Python qui route sans Claude (niveau 2).
2. **RAG mémoires** : `nomic-embed-text` (installé) pour recherche sémantique dans les `MEMOIRE.md`.
3. **Dataset CONVERGENCE** : consolidation transversale → fine-tuning futur (cf. `CONVERGENCE/SYNTHESE.md`, gabarit non actif).

## Lien avec le rework vault
Le vault atomique (notes + `entities/` + context-packs) est un **socle naturel** pour ces 3 axes : embeddings sur des notes atomiques > sur des mémoires monolithiques ; le dataset CONVERGENCE peut se générer depuis les notes.

## 🔗 Source de vérité
[[../../SYSTEME/CONFIG.md]] § Prochaines étapes.
