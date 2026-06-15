---
id: TOOL-004
type: tool
title: GENERER_KIT_JOUEURS.py
tags: [mastaurige, generateur, joueurs]
source: ../../MASTAURIGE/MEMOIRE.md
linkedTo: [DECISION-001, TOOL-005]
relevantFor: [mastaurige]
tier: 2
created: 2026-06-12
updated: 2026-06-12
---

# TOOL-004 — GENERER_KIT_JOUEURS.py

## Rôle
Génère le dossier JOUEURS_WEB_VERSION (kit joueurs) : `joueur.js` importe les actus, contenu nettoyé/effacé.

## Détail technique
Détection via sentinelle `moteur/joueur.js` (au lieu d'un fichier marqueur) ; boucle de retry sur `rmtree` (Windows « delete pending »).

## Emplacement
`OUTILS\GENERER_KIT_JOUEURS.py`.

## 🔗 Source de vérité
[[../../MASTAURIGE/MEMOIRE.md]]. Console de fusion : [[TOOL-005]].
