---
id: TOOL-016
type: tool
title: EHO éditable côté joueur — fiches bio + 4 familles de cartes + curseur de position + admin caché
tags: [mastaurige, trombino, eho, joueurs, edition, localstorage, vierge]
source: ../../MASTAURIGE/MEMOIRE.md
linkedTo: [TOOL-001, TOOL-004, DECISION-006, ARCH-010, LESSON-023, LESSON-024, PROJ-MASTAURIGE, AGENT-MASTAURIGE]
relevantFor: [mastaurige, exercices]
tier: 2
created: 2026-06-25
updated: 2026-09-09
---

# TOOL-016 — Édition joueur de l'EHO (trombino)

## Rôle
Permettre aux **joueurs** d'éditer le contenu de l'EHO et de faire varier la **position politique** (curseur bleu↔gris↔rouge, % affiché « 30 % rouge ») — fiches **bio** + les **4 familles de cartes** (avatars RS, médias, ONG/OI, localités), y compris **créer une fiche vierge** sur une carte sans bio.

## Mécanique (dans [[TOOL-001]] `generer_trombino_bios.py`, bloc `BIOS_BLOCK`)
- **Éditeur générique d'entités** `ENT_REG`/`entOpen`/`entEdit`/`entSave` + curseur partagé (`pctOf`/`reopenCard`/`pctColor`/`pctLabel`, 0=100 % bleu · 50=neutre · 100=100 % rouge).
- **Persistance** : une seule clé `localStorage['EHO_EDITS']` = `{id:{fields,campPct}}`, qui **se superpose** au baked à chaque nouveau kit.
- **Gate `window.EHO_EDITABLE`** : actif **uniquement dans le kit JOUEURS** (flag injecté par [[TOOL-004]]) → l'animateur reste **lecture seule** (popup bio d'origine, `tbOpenLoc`).
- **Admin caché** (index joueur) : **Alt+clic sur le logo MASTAURIGE** → exporter `.json` / vider EHO / **réinitialiser le fil** (cf. [[LESSON-024]]). Conserve les repères « NEW » (`aurige2bb_viewed`).

## À retenir
Câbler une nouvelle famille = lire ses champs (DOM pour statiques, data pour générées) + `entRegister({fields, refresh})`. Ré-injecter le flag via `.replace()` **simple** (cf. [[LESSON-023]]). Principe base/évolution : [[ARCH-010]].

## ✅ Porté dans la vierge (2026-09-09)
`BIOS_BLOCK` répliqué à l'identique dans `D:\CECPC\MASTAURIGE\LOCALSTORAGE_WEB_VERSION\OUTILS\generer_trombino_bios.py` (`Edit` littéral, pas de regex — évite le piège [[LESSON-023]]). `ORGS_ARNLAND`/`LOCALITES_ARNLAND` portés **vides** (base propre, [[ARCH-010]]) ; `BIO_PATCH_MINOTAURE` **non** porté (spécifique 7BB). Vérifié : 55 fiches inchangées, `node --check` + `py_compile` OK, 0 octet `\x01`. **Reste hors périmètre** : `GENERER_KIT_JOUEURS.py` (admin caché) et `index_master.html` (`_consoIsModKey`/`EHO_EDITS`, consolidation traitants) — non portés, à faire sur demande. Détail : `MASTAURIGE/JOURNAL.md` (2026-09-09).

## 🔗 Source de vérité
Détail : `MASTAURIGE/MEMOIRE.md` (entrées 2026-06-25). **Pointeur, pas copie.**
