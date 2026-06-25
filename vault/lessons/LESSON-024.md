---
id: LESSON-024
type: lesson
title: Fil joueur = baked (fichiers) + localStorage (AW.merged) — un navigateur sale gonfle le compte
tags: [mastaurige, joueurs, localstorage, articles, reset, piege]
source: ../../MASTAURIGE/MEMOIRE.md
linkedTo: [LESSON-019, ARCH-009, TOOL-016, TOOL-004, PROJ-MASTAURIGE]
relevantFor: [mastaurige, exercices]
tier: 2
created: 2026-06-25
updated: 2026-06-25
---

# LESSON-024 — Le fil joueur fusionne baked + localStorage (penser au reset)

## Symptôme
« 11 médias » affichés alors que les fichiers du kit n'en ont que **6** (4 dans `articles_data.js` + 2 du `starter_package.js`).

## Cause racine
`AW.renderHTML()` rend `effective()` = **baked (`MASTAURIGE_ARTICLES`) + TOUT `localStorage['mastaurige-articles']`** (merge par id, `articles.js`). Un navigateur de **test** garde des articles résiduels d'anciennes versions / d'imports ACTUS passés → le compte gonfle. Un navigateur **vierge** affiche bien 6 (le starter recrée ses 2 via `AW.create`). **Ce n'est pas un bug des fichiers.**

## Règle / correctif
- Réflexe diag : compter `articles_data.js` + `starter_package.js` AVANT d'incriminer le rendu ; le surplus = localStorage.
- **Reset** : `removeItem('mastaurige-articles')` + `removeItem('mastaurige-creations')` + reload → les fichiers font foi (bouton « Réinitialiser le fil » de l'admin caché, cf. [[TOOL-016]]).
- Même esprit que [[LESSON-019]] : la vérité = le contenu effectif / les fichiers, pas le localStorage. S'inscrit dans la diffusion [[ARCH-009]].
- ⏭ option distribution : auto-purge **versionné** (style SEED `collab.js`) au changement de version de kit, pour que les navigateurs joueurs se nettoient seuls.

## 🔗 Source de vérité
Détail : `MASTAURIGE/MEMOIRE.md` (2026-06-25). **Pointeur, pas copie.**
