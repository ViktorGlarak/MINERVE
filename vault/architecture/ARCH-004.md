---
id: ARCH-004
type: architecture
title: Registre des agents (renvoi)
tags: [architecture, agents, registre]
source: ../../CLAUDE.md
linkedTo: [ARCH-001, ARCH-002]
relevantFor: [systeme, noyau]
tier: 1
created: 2026-06-12
updated: 2026-06-12
---

# ARCH-004 — Registre des agents

## Principe
Le registre (agent, modèle Ollama, collaborations, rôle) a **un seul lieu canonique** : le tableau de [[../../CLAUDE.md]]. Les autres fichiers (CONFIG, ROUTAGE, DOSSIER_POSTE, MINERVE_HOME) **renvoient**, ne dupliquent pas.

## Maintenance
Ajout/suppression/changement de modèle d'un agent → checklist dans CLAUDE.md (registre + compteur NOYAU/MEMOIRE + ROUTAGE + prompt système + dossier agent). Compteur d'agents = nombre de lignes du registre.

## 🔗 Source de vérité
[[../../CLAUDE.md]] § Registre des agents.
