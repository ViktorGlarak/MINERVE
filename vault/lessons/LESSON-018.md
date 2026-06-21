---
id: LESSON-018
type: lesson
title: Modifier un inject = entrer dans le document + cohérence des dates (dateline=card D+, renvoi=article visé)
tags: [aurige, minautore, dates, coherence, methodo, jemm]
source: ../../AURIGE/MEMOIRE.md
linkedTo: [PROJ-AURIGE-7BB, LESSON-017]
relevantFor: [minautore, exercices, mastaurige]
tier: 2
created: 2026-06-21
updated: 2026-06-21
---

# LESSON-018 — Modifier un inject = corriger TOUT le document, dates cohérentes

## Symptôme observé
Demandé de « changer la date d'un article », je ne changeais que la card/dayorder (ou je déclarais un inject « absent » faute de card) — alors que la date apparaît **dans le document** (dateline, corps, encarts, renvois). Articles résiduels restés en mai alors que leur card était en juin.

## Cause racine
Confusion entre la **card** (placement MELMIL) et le **contenu du document** (HTML article / objet tweet). Un inject peut exister en HTML autonome **sans card bakée**.

## Correctif / règle à appliquer
1. **« Modifier un inject » = entrer DANS le document** (article/tweet/courrier) et corriger TOUT (dateline + corps + encarts + renvois), pas seulement la card.
2. **Cohérence des dates** : dateline d'un article = **date D+ de sa card** ; date d'un **renvoi/related** = date de l'**article visé** ; dates internes/décoratives (timelines, listes « recent », liens morts) = **+1 mois** (convention 2BB→7BB) ; **refs backstory en body** (ex. vote UNSC fondateur) **préservées**.
3. Si la valeur exacte manque → consulter le chef ([[LESSON-017]]), ne pas inventer.

## 🔗 Source de vérité
Détail + traces (xlsx MODIF_PRODUITS, balayage cohérence) : `MINAUTORE/MEMOIRE.md` (2026-06-21) + `AURIGE/MEMOIRE.md` § Méthodologie. **Pointeur, pas copie.**
