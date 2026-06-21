---
id: LESSON-019
type: lesson
title: Exporter le contenu EFFECTIF (pas le localStorage seul) + jamais de fichier qui accumule
tags: [mastaurige, export, master, joueurs, localstorage, lots]
source: ../../MASTAURIGE/MEMOIRE.md
linkedTo: [ARCH-009, PROJ-MASTAURIGE]
relevantFor: [mastaurige, exercices]
tier: 2
created: 2026-06-22
updated: 2026-06-22
---

# LESSON-019 — Exporter le contenu effectif, diffuser par lots

## Symptôme observé
Après diffusion, le joueur voyait **0 tweet** et des articles manquants ; et chaque nouveau `.zip` **effaçait** les anciens injects (écrasement des bases) — l'alternative (cumuler) menaçait de dépasser la **limite d'envoi**.

## Cause racine
1. **Export incomplet** : l'export de session ne lisait que le **localStorage** (créé/édité + `card-pub-*`). Or l'essentiel des injects publiés est du **socle baké** (`tweets_data.js`/`articles_data.js`), absent du localStorage → MASTER ne le recevait jamais.
2. **Écrasement** : les bases du kit étaient remplacées à chaque envoi → perte des anciens.

## Correctif / règle à appliquer
- **Exporter le contenu EFFECTIF**, pas le brut localStorage : passer par les moteurs (`TW.effective()` / `AW.effective()`) qui exposent **baked socle + créé**, filtrés sur les publiés.
- **Ne jamais accumuler dans un seul fichier** destiné à l'envoi : découper en **lots séparés** qui s'**ajoutent** (noms uniques, `push` remplace-par-id) + un manifeste qui les charge tous (cf. [[ARCH-009]]).
- Réflexe debug kit joueur : contenu = moteurs (pas les fichiers copiés seuls) ; tweets sous l'onglet **social**, articles sous **media** ; bandeau `window.onerror` pour voir les échecs silencieux.

## 🔗 Source de vérité
Détail / trace : [[../../MASTAURIGE/MEMOIRE.md]] (entrées 2026-06-22) + [[ARCH-009]]. **Pointeur, pas copie.**
