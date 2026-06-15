---
id: DECISION-001
type: decision
title: Architecture 3 dossiers MASTAURIGE
tags: [mastaurige, architecture, livraison]
source: ../../MASTAURIGE/MEMOIRE.md
linkedTo: [DECISION-002, TOOL-003, TOOL-004, TOOL-005, ARCH-003]
relevantFor: [mastaurige, exercices]
tier: 1
created: 2026-06-12
updated: 2026-06-12
---

# DECISION-001 — Architecture 3 dossiers MASTAURIGE

## Contexte / problème
Distribuer l'outil aux traitants, aux joueurs et fusionner tous leurs exports sur un poste BASE — sans Excel ni installation lourde.

## Décision
Trois dossiers à chemins relatifs (mêmes noms réutilisables dans chaque instance) :
- **LOCALSTORAGE_WEB_VERSION** — traitants (référence vivante, gabarit vierge)
- **JOUEURS_WEB_VERSION** — kit joueurs généré/effacé (joueur.js importe les actus)
- **EXE_MASTER_VERSION** — console BASE (fusion / renumérotation / packages actus)

## Pourquoi
Version web pure (localStorage, origine `file://`) → pas d'install ; chemins relatifs → portable sur clé USB / Outlook. Écarté : un `.exe` (inutile, le navigateur suffit).

## Conséquences / à respecter
État lié au navigateur + machine + chemin du dossier : **ne pas renommer/déplacer** le dossier extrait, ne pas changer de navigateur en cours d'exercice (sinon tout réapparaît « NEW »).

## 🔗 Source de vérité
Détail : [[../../MASTAURIGE/MEMOIRE.md]] § v0.2. Pointeur, pas copie.
