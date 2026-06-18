---
id: ARCH-008
type: architecture
title: MASTAURIGE collaboratif temps réel (serveur central + collab.js)
tags: [mastaurige, collaboratif, serveur, temps-reel, sse]
source: ../../MASTAURIGE/MEMOIRE.md
linkedTo: [PROJ-MASTAURIGE, DECISION-001, LESSON-013]
relevantFor: [mastaurige, exercices]
tier: 2
created: 2026-06-17
updated: 2026-06-17
---

# ARCH-008 — MASTAURIGE collaboratif temps réel

## En une phrase
Faire travailler 6-15 traitants **en même temps** sur **un seul** MASTAURIGE commun, hébergé sur un PC (« PC Admin »), au lieu que chacun modifie son fichier local (état `localStorage` isolé).

## Principe (ne réécrit pas MASTAURIGE)
- **Serveur** (`SERVEUR_COLLABORATIF\serveur.py`, Python stdlib) : sert l'instance MASTAURIGE en HTTP + détient l'état partagé = le **« mod layer »** + pousse chaque changement en **SSE** + persiste/sauvegarde/relance.
- **Client** (`collab.js`, 1ᵉʳ script de `index_master.html` + `melmil_ili.html`) : amorce localStorage depuis le serveur, **enveloppe `setItem/removeItem`** → POST, écoute `/flux` → applique + rafraîchit.
- **Pivot** : on **réutilise le modèle Export/Import existant** (`isModKey` / `COLLECTION_KEYS` / `mergeCollection`) — collections **fusionnées par id** (pas d'écrasement). `mast-traitant` (identité du poste) **reste local**.

## État
Phases 1 (serveur) & 2 (`collab.js`) faites et testées (hors navigateur). Reste : validation navigateur 2 machines, **Phase 3** (rafraîchissement sans reload), **Phase 4** (présence « qui édite quoi », verrou par card, restauration sauvegarde). Hébergement : Python portable embarqué si le PC Admin n'a pas Python.

## Source (vérité)
[[../../MASTAURIGE/MEMOIRE.md]] § « INTÉGRATION MASTAURIGE → COLLABORATIF ». Voir [[PROJ-MASTAURIGE]], [[DECISION-001]], perf → [[LESSON-013]].
