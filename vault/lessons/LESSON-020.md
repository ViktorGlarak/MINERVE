---
id: LESSON-020
type: lesson
title: Les éditions « Modifier » du socle (collab) ne persistent pas dans le fichier — baker avant de copier
tags: [mastaurige, collab, overlay, localstorage, tweets, durabilite]
source: ../../MASTAURIGE/MEMOIRE.md
linkedTo: [PROJ-MASTAURIGE, TOOL-015, AGENT-MASTAURIGE]
relevantFor: [mastaurige, exercices]
tier: 2
created: 2026-06-23
updated: 2026-06-23
---

# LESSON-020 — « Modifier » en collab n'écrit pas dans tweets_data.js

## Symptôme observé
Un tweet du socle édité via le bouton « ✎ Modifier » d'index_master change bien **sur la card**, mais après **copie du dossier `mastaurige/`** vers un autre poste, le texte **retombe à l'ancienne version**.

## Cause racine
« Modifier » sur un tweet **baked** crée un **overlay localStorage `mastaurige-edits`** (clé = id), persisté côté serveur dans **`etat_mastaurige.json`** (racine de `SERVEUR_COLLABORATIF\`, **hors** du dossier `mastaurige/`). Cet overlay est lié à l'instance/navigateur → il **ne voyage pas** quand on copie `mastaurige/`. Seul `tweets_data.js` voyage, et lui garde l'ancien texte. *(Idem pour les overrides de date `card-day-`/`card-time-`.)*

## Correctif / règle à appliquer
- **Avant toute copie/redistribution** du collab : **replier l'overlay dans le fichier source** avec [[TOOL-015]] (`BAKER_EDITIONS.py`, `--dry-run` pour aperçu) → une seule vérité durable.
- Pour les gros contenus pré-rédigés, **éditer directement le `.html` / le fichier de données** plutôt que « Modifier ».
- Ne **jamais** baker un overlay aveuglément : relire chaque champ (un changement non voulu peut s'y cacher).

## 🔗 Source de vérité
Détail / trace : `MASTAURIGE/MEMOIRE.md` (2026-06-23). **Pointeur, pas copie.**
