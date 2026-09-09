---
id: ARCH-011
aliases: ["ARCH-011"]
type: architecture
title: EHO v2 (MASTORION) — modèles d'EHO, double vue anim/joueurs, tables additives
tags: [mastorion, eho, architecture, roles, templates, cellules]
source: ../../MASTORION/MEMOIRE.md
linkedTo: [DECISION-013, LESSON-027, LESSON-028, ARCH-010]
relevantFor: [mastorion, exercices]
tier: 2
created: 2026-09-09
updated: 2026-09-09
---

# ARCH-011 — Architecture EHO v2 sur MASTORION

## En une phrase
Une app `apps/eho` (port 4204, branche `feat/eho`) donne à l'exercice ses
**modèles d'EHO** (SKOLKAN PERSONA / VIERGE), une **vue animateur** (officiel,
gestion, comparaison) et une **vue joueur par cellule** (EHO dépouillé,
drag & drop, fiches) — **sans toucher une seule table existante** de la
plateforme en production.

## Les 5 principes
1. **Additif uniquement** : 4 tables `eho_*` dans un fichier `eho.prisma`
   séparé (`db push`) ; références vers `users` par entier **sans relation
   Prisma** (la relation imposerait le champ inverse sur `User`).
2. **Persona = compte sans rôle** : critère structurel qui protège les humains
   de toute opération d'exercice (application de modèle, import, suppression).
3. **Autorisation côté serveur** : `EHO_ANIM`/`EHO_PLAYER` (chaîne `role`
   libre, 0 migration) ; l'UI ne fait que router, l'API re-vérifie tout.
4. **Le travail joueur ne touche jamais l'officiel** : fiches et placements
   dans `eho_assessments` (une ligne par cellule×persona), l'officiel reste
   sur `users` ; la comparaison animateur croise les deux.
5. **Modèles = données hors git** (`data/eho/templates/`) ; application
   verrouillée : rôle + code retapé + **sauvegarde auto réimportable** +
   uploads jamais supprimés ; capture de la base courante = nouveau modèle.

## 🔗 Source de vérité
État durable : `MASTORION/MEMOIRE.md` § « App EHO » ; chronologie et
vérifications : `MASTORION/JOURNAL.md`. **Pointeur, pas copie.**
