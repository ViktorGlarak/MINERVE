---
id: TOOL-015
type: tool
title: BAKER_EDITIONS.py — replie les éditions « Modifier » de l'overlay collab dans tweets_data.js
tags: [mastaurige, collab, overlay, baker, tweets, durabilite]
source: ../../MASTAURIGE/MEMOIRE.md
linkedTo: [PROJ-MASTAURIGE, AGENT-MASTAURIGE, LESSON-020]
relevantFor: [mastaurige, exercices]
tier: 2
created: 2026-06-23
updated: 2026-06-23
---

# TOOL-015 — BAKER_EDITIONS.py (durabiliser les éditions « Modifier »)

## Rôle
Sur la **variante COLLAB** de MASTAURIGE, éditer un tweet **du socle** via « ✎ Modifier » ne touche **pas** `tweets_data.js` : la modif vit dans un overlay `mastaurige-edits` persisté dans `etat_mastaurige.json` (cf. [[LESSON-020]]). Cet outil **replie** cet overlay dans le fichier source (vérité durable qui voyage avec le dossier), puis nettoie l'overlay → une seule vérité.

## Mécanique
- Emplacement : `…\SERVEUR_COLLABORATIF\mastaurige\OUTILS\BAKER_EDITIONS.py`.
- Lit `etat_mastaurige.json` (clé `mastaurige-edits`), applique par `id` les champs **text/hashtags/camp/likes/retweets/nom/handle/avatar** dans `moteur/tweets_data.js` ; **ignore** `time`/`dayorder` salis par le formulaire.
- Retire de l'overlay les clés repliées ; **sauvegardes** dans `D:\CECPC\_cbtmp` ; **`--dry-run`** pour aperçu.
- **Réflexe** : lancer `py OUTILS\BAKER_EDITIONS.py` **AVANT toute copie/redistribution** du dossier `mastaurige/`.

## À retenir
Spécifique COLLAB (seule variante avec `etat_mastaurige.json`) → à **porter dans la vierge collab**.

## 🔗 Source de vérité
Détail : `MASTAURIGE/MEMOIRE.md` (entrées 2026-06-23). **Pointeur, pas copie.**
