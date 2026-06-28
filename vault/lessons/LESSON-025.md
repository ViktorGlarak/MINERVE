---
id: LESSON-025
type: lesson
title: Désync de date MELMIL ↔ feed — clé card-day des articles (id vs basename) + piège GELEX
tags: [mastaurige, dates, melmil, articles, sync, gelex]
source: "../../MASTAURIGE/MEMOIRE.md"
linkedTo: [REF-calendrier-7bb-gelex]
relevantFor: [mastaurige, exercices]
tier: 2
created: 2026-06-27
updated: 2026-06-27
---

# LESSON-025 — Dates qui divergent entre MELMIL et le fil (index_master)

## Symptôme observé
Un inject affiché à une date sur `melmil_ili.html` et à une autre sur `index_master.html` (ex. **08.02.I01** : MELMIL 27 Jun / feed 28 Jun). Plus tôt : injects du 30 juin placés à tort en « D+40 ».

## Cause racine
1. **GELEX** : le 29 juin est gelé (pas de D+) → **30 Jun = D+39, pas D+40**. Supposer un calendrier linéaire = erreur. Cf. [[REF-calendrier-7bb-gelex]].
2. **Clé `card-day` des ARTICLES incohérente** : MELMIL et le bouton « Modifier » écrivent/lisent `card-day-<id_article>`, mais l'éditeur de date **inline du feed** (`initDateTimeEditors`) ne testait que `markTweet`/`openCard`. Or les articles AW ont `onclick="CR_previewArticle(id)"` + `data-artid` → le feed tombait sur une clé **aléatoire** et **ignorait** la surcharge `card-day-<id>`. Les tweets (clé = id partagée) marchaient ; pas les articles.

## Correctif / règle à appliquer
- **La date de la card MELMIL fait foi** ; aligner le `dayorder` baké du feed dessus (audit : comparer `inj.date` ↔ `dayorder`).
- Fix code (1 ligne, `index_master.html`) : `_key = … : (card.getAttribute('data-artid') || null)` → feed et MELMIL partagent la même clé `card-day-<id>` pour les articles → **sync bidirectionnelle OK** (le split/fusion multi-injects existait déjà).
- Réflexe dates 7BB : toujours passer par le mapping GELEX [[REF-calendrier-7bb-gelex]].

## 🔗 Source de vérité
Détail / trace : `MASTAURIGE/MEMOIRE.md` (§ FIX SYNC DATE des ARTICLES + statut permanent). **Pointeur, pas copie.**
