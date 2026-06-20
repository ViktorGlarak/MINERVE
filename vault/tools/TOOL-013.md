---
id: TOOL-013
type: tool
title: Synchromatrice — planche de travail des storylines (LO × temps de jeu)
tags: [mastaurige, synchromatrice, storyline, lo, melmil, web]
source: ../../MASTAURIGE/MEMOIRE.md
linkedTo: [PROJ-AURIGE-7BB, DECISION-009]
relevantFor: [mastaurige, minautore]
tier: 2
created: 2026-06-20
updated: 2026-06-20
---

# TOOL-013 — Synchromatrice (planche storylines)

## Rôle
Outil web MASTAURIGE (`MELMIL/SYNCHROMATRICE/`) : **planche LO (lignes LO1-5 + HN) × temps de jeu (colonnes D+)** où les storylines sont des **blocs rectangulaires**. Vitrine de [[DECISION-009]] (la LO comme étiquette, la storyline comme unité).

## Mécanique
- 3 fichiers autonomes : `synchromatrice.html` + `.css` + `.js`. **localStorage** (`mastaurige-synchromatrice-v1`).
- **Dynamique** : glisser = change jour + LO (couleur suit) ; poignée droite = durée ; clic = éditeur (titre, code, n° injects, **description/effet attendu**, LO, jours) + supprimer ; ＋Ajouter, ↺ reseed, 🗑 Vider.
- **Export / Import JSON** (sauvegarde/partage/restauration). **PDF** : `@media print` via **`zoom: var(--pscale)`** (PAS `transform:scale` — sinon double-réduction navigateur) → 1 page paysage.
- Couleurs LO lues dans `lo_config.loColors` si présent, sinon palette canonique. Header centré + boutons retour `← MELMIL` / `🏠 MASTAURIGE`.

## Déclinaisons (3 instances, divergence assumée)
- **Vierge localstorage** (`D:\CECPC\MASTAURIGE\LOCALSTORAGE_WEB_VERSION`) — gabarit, seed = 17 threads Piste C, D+1-18.
- **Vierge collab** (`…\SERVEUR_COLLABORATIF\mastaurige`) — **synchro temps réel** : clé ajoutée à `serveur.py` + `collab.js` COLLECTION_KEYS (LWW), `collab.js` chargé, garde anti-boucle dans `save()`. ⚠ nécessite redémarrage serveur.
- **MINOTAURE 7BB** (`EXER\AURIGE 7BB\…\SERVEUR_COLLABORATIF\mastaurige`) — **localStorage pur** (pas de `collab.js`, serveur non touché), seed = **12 storylines JEMM 07.01-07.12**, **D+ RÉELS de la MELMIL** (`START_DP=31`, D+31→D+41 ; `d1/d2` en D+ réels).
- Bouton d'accès `.btn-synchro` dans `index_master.html` + `melmil_ili.html`.

## 🔗 Source de vérité
Détail complet : `MASTAURIGE/MEMOIRE.md` (notes synchromatrice, 2026-06-20). **Pointeur, pas copie.**
