---
id: DECISION-019
aliases: ["DECISION-019"]
type: decision
title: Une seule copie de travail des dépôts PLEIADE, sur C: — le doublon D: supprimé
tags: [pleiade, environnement, exfat, depots, git]
source: ../../PLEIADE/MEMOIRE.md
linkedTo: [LESSON-031, ARCH-013, DECISION-017]
relevantFor: [pleiade, mastorion, outillage]
tier: 1
created: 2026-09-16
updated: 2026-09-16
---

# DECISION-019 — Une seule copie de travail, sur C:, et GitHub fait foi

## Contexte / problème
Le poste portait **deux copies** des dépôts PLEIADE : `C:\CECPC\pleiade` (où tout
tournait) et `D:\CECPC\PLEIADE` (figée depuis cinq jours). La doctrine d'alors —
« clone d'exécution sur C:, copie de référence sur D: » — entretenait **deux
vérités qui divergeaient** : le matin même, la branche locale du clone C: traînait
**10 commits en arrière**.

## Décision
**`D:\CECPC\PLEIADE` supprimé.** Une seule copie de travail, dans
**`C:\CECPC\pleiade`**, et **GitHub fait foi**. Fin de la doctrine
« clone d'exécution + copie de référence ».

## Pourquoi
Un dépôt de code sur D: **ne pouvait rien faire d'autre que vieillir** : D: est en
exFAT, aucun binaire natif ne s'y exécute (voir [[LESSON-031]]). Ni construction,
ni lancement, ni test. C'était une archive morte, pas une sauvegarde.

Vérifié avant de supprimer, sur les trois dépôts et **toutes branches
confondues** : 0 commit non poussé, 0 remise, aucune branche locale absente
d'`origin`, aucun `.env` ni dossier de données — uniquement des artefacts
régénérables.

## Conséquences / à respecter
- **Ne pas recréer** `D:\CECPC\PLEIADE`.
- ✅ **`D:\CECPC\PRODUCTION` reste sur D:** (MINERVE, EXER, BDA, CREATION,
  DOC REF) : ce sont des **documents**, pas du code — exFAT ne les gêne pas, et
  les déplacer casserait les chemins de `CLAUDE.md`, les hooks et les permissions.
- ⚠ **Avant toute bascule de branche dans C:, comparer d'abord** l'arbre vivant au
  commit visé : le travail y vit souvent **non commité**. Puis `git stash push -u`
  plutôt qu'un `reset --hard` — un filet récupérable, jamais une destruction.

## 🔗 Source de vérité
`PLEIADE/MEMOIRE.md` § Environnement de travail, et `CLAUDE.md` (note « Pourquoi
PLEIADE vit sur C: et non sur D: »).
