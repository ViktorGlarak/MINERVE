---
id: LESSON-026
aliases: ["LESSON-026"]
type: lesson
title: Placement card MELMIL (date ↔ standby) — exclusif ET appliqué au RENDU (bug card socle JEMM)
tags: [mastaurige, melmil, standby, jemm, rendu]
source: "../../MASTAURIGE/MEMOIRE.md"
linkedTo: [PROJ-MASTAURIGE, AGENT-MASTAURIGE]
relevantFor: [mastaurige, melmil, minautore]
tier: 2
created: 2026-06-29
updated: 2026-06-29
---

# LESSON-026 — Placement MELMIL (date ↔ standby) : exclusif + appliqué au rendu

## Symptôme observé
Une card glissée en « À placer » (standby, ex. **05.10.I05** = card socle **JEMM**, à garder hors du 30 Jun) **revenait sur sa date** après cuisson **et** au rechargement — alors que le `card-attente-<key>=1` était bien présent (export + seed + localStorage).

## Cause racine
**Deux bugs distincts, même symptôme :**
1. **Seed** : glisser vers « À placer » retire `card-day`/`card-time` côté traitant, mais `baker_collab` n'**ajoutait** que les clés de l'export sans **retirer** l'ancienne `card-day` du seed → le seed avait **date + standby en même temps** (conflit).
2. **Rendu** : le placement d'une card **socle (JEMM compris)** dans `melmil.js` se faisait **uniquement par `inj.date`** (date JEMM) **sans lire le calque** `card-attente`/`card-day` → l'overlay était capté au drag mais jamais affiché au reload.

## Correctif / règle à appliquer
- **`card-day` et `card-attente` sont EXCLUSIFS** (une card est sur un jour OU en standby) : à l'import comme au render, poser l'un **retire** l'autre.
- **Un calque de placement (overlay localStorage) doit être appliqué AU RENDU, pas seulement capté au drag.** Le rendu socle lit désormais l'overlay des cards liées (`MASTAURIGE_INDEX[code]`) — **priorité attente > card-day > inj.date**. Le socle JEMM reste la vérité (on ne touche QUE l'affichage ; ré-import inchangé).
- Le **feed index_master gérait déjà** `card-attente` (`tweets_engine.withOverrides`) → toujours vérifier les **deux** rendus (MELMIL **et** feed) quand une clé de placement est partagée.
- ⚠ Un calque ne se propage aux postes qu'au **reseed** (même SEED_VERSION = seed sauté) : recharge forcée ou « 🧹 Vider ».

## 🔗 Source de vérité
Trace technique (baker_collab.js + melmil.js, 2026-06-29) : `source:`. Voir aussi désync de date [[LESSON-025]]. **Pointeur, pas copie.**
