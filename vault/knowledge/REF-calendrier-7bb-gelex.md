---
id: REF-calendrier-7bb-gelex
type: reference
title: Calendrier AURIGE 7BB — mapping D+ ↔ date avec GELEX (29 Jun)
tags: [aurige-7bb, calendrier, dates, gelex, exercices]
source: "../../../../EXER/AURIGE 7BB/00_Boites à outils/MASTAURIGE/LOCALSTORAGE_WEB_VERSION/MELMIL/melmil.js"
linkedTo: [LESSON-025]
relevantFor: [exercices, mastaurige]
tier: 2
created: 2026-06-27
updated: 2026-06-27
---

# 🗓️ Calendrier AURIGE 7BB — D+ ↔ date (avec GELEX)

> ⚠ Le calendrier 7BB **n'est PAS linéaire** : la synchromatrice place un **GELEX (jour gelé, pas de jeu) le 29 juin**, qui n'a **pas** de numéro D+. Autorité = `DAY_MAP` dans `MELMIL/melmil.js` (identique à `DAY_OPTIONS` de `index_master.html`).

| D+ (dayorder) | Date | | D+ | Date |
|---|---|---|---|---|
| 31 | 21 Jun | | 37 | 27 Jun |
| 32 | 22 Jun | | 38 | **28 Jun** |
| 33 | 23 Jun | | — | **29 Jun = GELEX** |
| 34 | 24 Jun | | 39 | **30 Jun** |
| 35 | 25 Jun | | 40 | 1 Jul |
| 36 | 26 Jun | | 41 | 2 Jul |

**Piège** : après le 28 Jun (D+38), le jour joué suivant est le **30 Jun = D+39** (le 29 est sauté). Donc **30 Jun = D+39** (≠ D+40), **1 Jul = D+40**, **2 Jul = D+41**.

## À appliquer
- Tout placement de date 7BB : `dayorder = DAY_MAP[date]` ci-dessus ; champ `time` = « `<J Mois>` · D+`<N>` ».
- **La date de la card MELMIL fait foi** ; le `dayorder` baké du feed (`tweets_data`/`articles_data`) doit s'y aligner.
- Sync feed ↔ MELMIL = via `card-day-<key>` (localStorage partagé). Cf. [[LESSON-025]].

## 🔗 Source de vérité
`DAY_MAP` / `DAY_OPTIONS` (instance 7BB, cf. `source:`). Mémoire harness : `calendrier_7bb_gelex`.
