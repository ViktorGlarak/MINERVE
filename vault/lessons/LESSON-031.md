---
id: LESSON-031
aliases: ["LESSON-031"]
type: lesson
title: exFAT (D:) n'exécute aucun binaire natif — clone d'exécution sur NTFS obligatoire
tags: [exfat, environnement, npm, prisma, nextjs, piege]
source: ../../PLEIADE/MEMOIRE.md
linkedTo: [ARCH-012, DECISION-015]
relevantFor: [pleiade, mastorion, outillage]
tier: 2
created: 2026-09-11
updated: 2026-09-11
---

# LESSON-031 — D: est en exFAT : les binaires natifs n'y tournent pas

## Symptôme observé
Sur `D:\CECPC\…`, trois échecs de familles différentes mais de même origine :
- `npm install` d'un **monorepo** → `EISDIR` (les symlinks d'espaces de travail) ;
- `next build` → *« Attempted to load @next/swc-win32-x64-msvc … Accès refusé »* ;
- `prisma db push` → *« Schema engine exited. Command failed with EPERM »*.

## Cause racine
**exFAT ne porte ni les liens symboliques ni le bit d'exécution.** Tout ce qui
doit *s'exécuter* (moteur Prisma, binding SWC) ou *se lier* (workspaces npm)
échoue. Le code TypeScript, lui, se vérifie sans problème (`tsc` est du JS pur).

## Correctif / règle à appliquer
**Deux clones, rôles distincts** — le schéma éprouvé :
- `D:\…` = **copie de référence** (git, lecture, édition) ;
- `C:\…` (NTFS) = **clone d'exécution** : npm, Prisma, build, serveur de dev ;
- **GitHub fait foi** : les deux clones s'y synchronisent, jamais de copie de
  fichiers à la main.
⚠ Un paquet **unique** (sans workspaces) accepte `npm install` sur exFAT — mais
ses binaires natifs resteront inexécutables : l'illusion de fonctionner s'arrête
au premier build.

## 🔗 Source de vérité
Détail / trace : voir `source:`. **Pointeur, pas copie.**
