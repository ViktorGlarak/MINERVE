---
id: LESSON-016
type: lesson
title: Instance de travail 7BB = le serveur collaboratif (pas LOCALSTORAGE) — confirmer l'instance + consulter les agents avant d'écrire
tags: [mastaurige, minautore, instance, collab, reflexe]
source: ../../MASTAURIGE/MEMOIRE.md
linkedTo: [PROJ-AURIGE-7BB, TOOL-012]
relevantFor: [mastaurige, minautore]
tier: 1
created: 2026-06-20
updated: 2026-06-20
---

# LESSON-016 — L'instance de travail 7BB est le SERVEUR COLLABORATIF

## Symptôme observé
J'ai baké les injects LO5 (et préparé tout l'outillage) dans `…\AURIGE 7BB\…\LOCALSTORAGE_WEB_VERSION`, alors que l'utilisateur travaille **toute la journée sur le serveur collaboratif**. Plusieurs allers-retours d'instances erronées (j'ai même ouvert l'ancien proto `D:\CECPC\MASTAURIGE\SERVEUR_COLLABORATIF`, périmé). Travail refait au bon endroit + LOCALSTORAGE restauré.

## Cause racine
Je n'ai pas **consulté MASTAURIGE/MINAUTORE en amont** pour identifier l'instance canonique, et j'ai supposé au lieu de demander. Plusieurs instances coexistent avec des noms quasi identiques (vierge globale, LOCALSTORAGE/JOUEURS/EXE_MASTER 7BB, **SERVEUR_COLLABORATIF**, + un vieux proto homonyme).

## Correctif / règle à appliquer
- **Instance 7BB de travail = `D:\CECPC\PRODUCTION\EXER\AURIGE 7BB\00_Boites à outils\MASTAURIGE\SERVEUR_COLLABORATIF\mastaurige`** (collab.js + serveur.py + état partagé live). C'est LÀ qu'on bake.
- **Avant toute écriture** : confirmer l'instance + **consulter MASTAURIGE & MINAUTORE** (+ l'analyste du pays). Ne jamais conclure « absent » sur une seule source.
- `melmil.js` du collab **n'a aucun code collab** (tout dans `collab.js` séparé) → patches copiables ; **éditer les HTML en place** pour préserver `<script collab.js>`.

## 🔗 Source de vérité
Détail / trace : `MASTAURIGE/MEMOIRE.md` [2026-06-20] + harness `feedback_impliquer_agents_concernes`. **Pointeur, pas copie.**
