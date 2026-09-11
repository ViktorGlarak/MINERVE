---
id: DECISION-015
aliases: ["DECISION-015"]
type: decision
title: L'EHO devient un dépôt autonome — STARTEX et comparaison portés, cellules écartées
tags: [pleiade, eho, startex, joueurs, comparaison, nextjs]
source: ../../PLEIADE/MEMOIRE.md
linkedTo: [DECISION-014, ARCH-012, ARCH-011, LESSON-030, LESSON-031]
relevantFor: [pleiade, exercices]
tier: 1
created: 2026-09-11
updated: 2026-09-11
---

# DECISION-015 — L'EHO autonome : ce qu'on porte, ce qu'on laisse

## Contexte / problème
L'EHO avait été développé en **Angular dans le monorepo mastorion**
(branche `feat/eho`, 8 commits) : modèles d'EHO, cellules joueurs, package
STARTEX, trombinoscope, vue comparative. Il a été **réécrit ailleurs** — dépôt
autonome **`cecpc-pleiade/eho`** en **Next.js + Keycloak** — qui n'en reprenait
aucune de ces fonctions.

## Décision
Décision utilisateur (2026-09-11) : **porter STARTEX et la comparaison** vers le
nouvel EHO, **sans la notion de cellule/équipe** (mise de côté). Un **joueur =
un compte Keycloak**, avec **sa** planche personnelle. Tous les avatars de la
bibliothèque MINERVE doivent y être présents.
→ La branche `origin/feat/eho` de mastorion **n'a plus vocation à être fusionnée**.

## Pourquoi (alternatives écartées)
- Fusionner l'ancien `apps/eho` dans mastorion : `main` a divergé profondément
  (Keycloak, layouts, impersonation) et l'EHO n'a plus sa place dans ce dépôt.
- Repartir de zéro : le savoir de conception (invariants, pièges) restait valable
  et a été réutilisé tel quel.

## Conséquences / à respecter
- Travail sur la branche **`MEYTRE`**, partie de `feat/avatars-sans-keycloak`.
- **STARTEX = un GROUPE nommé `STARTEX`** → aucun ajout de schéma, et le package
  **voyage dans les classeurs, exports et modèles d'EHO**.
- **Un seul modèle ajouté** : `EhoLecture` (une lecture de joueur sur un avatar),
  séparée de `users` pour que l'animateur puisse comparer.
- Les 3 règles du jeu (dépouillement, verrou STARTEX, validation des zones) sont
  appliquées **côté serveur**, jamais par masquage d'interface.

## 🔗 Source de vérité
Détail complet — règles, données en place, comptes de test : `PLEIADE/MEMOIRE.md` § 8bis. **Pointeur, pas copie.**
