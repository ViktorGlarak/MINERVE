---
name: calendrier-7bb-gelex
description: "Calendrier AURIGE 7BB/MINOTAURE : mapping D+ ↔ date AVEC un GELEX le 29 Jun (29 Jun n'est PAS un D+)"
metadata: 
  node_type: memory
  type: project
  originSessionId: 4377e89f-f0dd-40af-851d-ddfb523fd276
---

**⚠ Le calendrier 7BB n'est PAS linéaire : il y a un GELEX (jour gelé, pas de jeu) le 29 juin.** Mapping `dayorder` (D+) ↔ date — source de vérité = `MELMIL/melmil.js` `DAY_MAP` (et `index_master.html` DAY_OPTIONS, identiques) :

| D+ (dayorder) | Date |
|---|---|
| 31 | 21 Jun |
| 32 | 22 Jun |
| 33 | 23 Jun |
| 34 | 24 Jun |
| 35 | 25 Jun |
| 36 | 26 Jun |
| 37 | 27 Jun |
| 38 | **28 Jun** |
| — | **29 Jun = GELEX** (colonne `gelex`, PAS de D+) |
| 39 | **30 Jun** |
| 40 | **1 Jul** |
| 41 | **2 Jul** |

**Piège** : après le 28 Jun (D+38), le jour suivant **joué** est le 30 Jun = **D+39** (le 29 est sauté). Donc **30 Jun = D+39** (et NON D+40), **1 Jul = D+40**, **2 Jul = D+41**.

**Why:** j'ai placé par erreur des injects du 30 juin en « D+40 » (erreur faite ≥2× : artillerie 07.03.I11). Le GELEX vient de la synchromatrice.

**How to apply:** pour TOUT placement de date 7BB, utiliser `dayorder = DAY_MAP[date]` ci-dessus (champ `time` = « `<J Mois>` · D+`<N>` »). La **date de la card MELMIL = la vérité** ; le `dayorder` baké du feed (`tweets_data`/`articles_data`) doit s'y aligner. Sync feed↔MELMIL = déjà gérée par `card-day-<key>` (localStorage partagé ; drag MELMIL et « Modifier » du feed l'écrivent tous deux). ⚠ La note [[aurige7bb_actif]] (« D+33→D+41 = 23 juin→1er juillet ») est **imprécise** : D+41 = **2 Jul** et il y a le GELEX.
