---
id: DECISION-007
type: decision
title: STARTEX Package — sous-injects 00.00.00Ai…Ei (cartes ghost par camp, MELMIL)
tags: [mastaurige, melmil, startex, convention, 7bb]
source: ../../MASTAURIGE/MEMOIRE.md
linkedTo: [PROJ-AURIGE-7BB, PROJ-MASTAURIGE, ARCH-008]
relevantFor: [mastaurige, exercices, minautore]
tier: 2
created: 2026-06-18
updated: 2026-06-18
---

# DECISION-007 — STARTEX Package : sous-injects `00.00.00Ai…Ei` (incident `00.00.00i`)

## Décision
Un **« STARTEX Package »** (*Start of Exercise* — nommage corrigé de « Starter », 2026-06-18) = lot d'articles donné aux joueurs au **démarrage** d'un exercice (7BB : le 23 juin / D+33) pour poser la **ligne de conduite / structure politique**. Ces injects **n'ont pas de vrai numéro** → incident réservé **`00.00.00i`**, et **chaque article = un sous-inject** `00.00.00Ai`, `Bi`, `Ci`… (respecte la logique de codage MASTAURIGE : nom propre, draggable, statut).

## Comportement (convention moteur — instance 7BB + copie collab ; vierge alignée en fin de MINAUTORE)
- La série `00` étant inconnue du plan, MELMIL traite chaque sous-inject via le **CAS 1.5** de `buildGhostInjects` → **une carte GHOST par camp** sur la **ligne r7 GHOST** au D+33, libellée **« 📦 STARTEX PACKAGE »**. Chaque carte ne montre au clic **que les injects de son camp** (sous-items cliquables individuellement).
- Les cartes se colorent **par camp** (autorité qui parle) : 🔴 Olamao `Ai` · 🔵 Pallesson `Bi` / Rutte `Ci` · ⚪ Guterres ONU `Di` / TV4 `Ei`.
- Articles déjà rédigés (`.html` riches) = créations **`external:true` + `file`** → `CR_previewArticle` **navigue vers le vrai `.html` dans le même onglet** (`saveMasterState()` + `?from=master`, comme `openCard`) ; bouton **« ← MASTAURIGE »** via `shared/back-btn.js` + scroll restauré au retour. Auto-injectées (idempotent) par `moteur/starter_package.js`, qui **réconcilie `num` + `file`** d'une ancienne instance localStorage (corrige aussi un 404 si l'ancien `file` était périmé). ⚠ chemin 7BB du script = `../../shared/back-btn.js` (`shared/` racine instance), pas `../shared/`.

## Portée — convention PERMANENTE (tous exercices futurs)
**Décision utilisateur (2026-06-18) :** `00.00.00i` est un **code réservé standard**, pas un bricolage 7BB. Le **mécanisme** STARTEX (code réservé + label CAS 1.5 + nav `external` créateur + `back-btn.js` + correctifs calendrier-agnostiques) doit être **intégré au gabarit VIERGE en fin de MINAUTORE**, pour que **tout futur exercice** dispose nativement d'un emplacement STARTEX. ⚠ D'ici là **vierge intacte** ; on ne porte QUE le mécanisme (squelette `starter_package.js` vide), **jamais** les 5 articles 7BB (contenu spécifique). Checklist détaillée : `MASTAURIGE/MEMOIRE.md` § « STARTEX = fonctionnalité PERMANENTE de la vierge ».

## Pourquoi
Donner aux joueurs un cadrage politique commun **sans polluer la numérotation** des injects ILI/HN, tout en restant visible, rangé (ghost) et **nommé inject par inject** dans la synchromatrice — une carte par camp évite d'entasser rouge/bleu/neutre dans une seule carte. Réservé `00.00.00i` = **valable pour tous les exercices**, donc à inscrire dans le gabarit.

## Source (vérité)
[[../../MASTAURIGE/MEMOIRE.md]] § « STARTEX PACKAGE ». Exercice : [[PROJ-AURIGE-7BB]] ; collaboratif : [[ARCH-008]].
