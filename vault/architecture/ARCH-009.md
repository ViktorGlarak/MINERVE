---
id: ARCH-009
type: architecture
title: Diffusion joueurs MASTAURIGE — mode fichiers par lots incrémentaux
tags: [mastaurige, joueurs, diffusion, master, lots, fichiers]
source: ../../MASTAURIGE/MEMOIRE.md
linkedTo: [PROJ-MASTAURIGE, ARCH-008, LESSON-019, DECISION-001]
relevantFor: [mastaurige, exercices]
tier: 2
created: 2026-06-22
updated: 2026-06-22
---

# ARCH-009 — Diffusion joueurs par lots incrémentaux

## En une phrase
Livrer le fil d'actus aux joueurs **par fichiers** (extraire le `.zip` → voir direct, sans import localStorage), et **par lots** qui **s'ajoutent** sans s'écraser, pour ne jamais perdre les anciens injects **ni** faire grossir un fichier au-delà de la limite d'envoi.

## Principe
- **MASTER.py** (poste BASE) : à chaque diffusion, écrit **`moteur/actus/lot_<stamp>.js`** (uniquement la sélection publiée du lot, épurée camp/LO) qui fait un **`push` remplace-par-id** dans `MASTAURIGE_TWEETS`/`MASTAURIGE_ARTICLES`. Régénère le **manifeste** `moteur/actus_index.js` (`var ACTUS_LOTS=[...noms...]` + boucle `document.write` chargeant chaque lot **avant le rendu**). Liste persistée dans `SORTIES/_LOTS_<exercice>.json`. **N'écrit plus** `tweets_data.js`/`articles_data.js` (socle vierge).
- **Kit joueur** (`JOUEURS_WEB_VERSION/index_master.html`) : charge `articles_data.js` (socle vide) puis `actus_index.js` (charge les lots) avant `articles.js`. Le contenu vient **uniquement des lots**.
- **Source d'export (animateur)** : le bouton « 🗂 Extraction complète » (`exporterSessionJoueurs`) produit le `.json` de session **identique au « Exporter mes modifs » de MELMIL**, en y **injectant le contenu complet des publiés** via `TW.effective()`/`AW.effective()` (cf. [[LESSON-019]]), puis commit (publiés → Envoyé + dépubliés).
- **Côté joueur** : extraire **chaque** `.zip` dans le kit → le lot s'ajoute (nom unique, ancien jamais écrasé) → ouvrir → fil cumulé. Un lot manqué = son contenu absent, sans planter. Classification (camp) reste en localStorage par-dessus.

## Pourquoi (vs alternatives écartées)
- **Écrasement mono-fichier** : le joueur perdait les anciens injects. ❌
- **Cumul mono-fichier** : dépasse la limite d'envoi (base64 + volume). ❌
- **Lots** : ajout incrémental, zip petit, pas de perte. ✅

## État
Implémenté + testé hors navigateur (2 lots distincts, manifeste cumulé, `node --check` OK). `GENERER_KIT_JOUEURS.py` reproduit au build. Reste : validation navigateur 2 lots de bout en bout + HTML des « courriers sans gabarit ». ⚠ `document.write` (sync, OK file:// même origine).

## Source (vérité)
[[../../MASTAURIGE/MEMOIRE.md]] §§ « Kit JOUEURS — diffusion par LOTS » + « Publier/statut ». Voir [[ARCH-008]] (collaboratif), [[DECISION-001]] (3 dossiers + console MASTER), [[LESSON-019]].
