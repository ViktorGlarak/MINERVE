---
name: aurige7bb-actif
description: AURIGE 7BB / MINOTAURE 26 — exercice TERMINÉ (clos le 2026-07-03) ; débloque le portage de la vierge
metadata: 
  node_type: memory
  type: project
  originSessionId: 52feb2ec-047b-438f-b7ad-369a80dbc9a0
  modified: 2026-07-22T11:28:17.241Z
---

L'exercice **AURIGE 7BB / MINOTAURE 26** est **TERMINÉ** (fenêtre 2026-06-16 → **2026-07-03**, jeu in-game des injects D+33→D+41 = 23 juin → 1ᵉʳ juillet 2026). Confirmé par l'utilisateur le **2026-07-22**. Ce n'est plus le contexte métier dominant : on prépare les **exercices suivants** (à préciser par l'utilisateur).

**Why:** la mémoire précédente le décrivait comme *actif* jusqu'au 03/07 — la laisser telle quelle ferait travailler les sessions suivantes sur un exercice clos.

**How to apply:**
- Ne plus produire d'injects 7BB « en jeu ». MINAUTORE reste l'**archive de référence** du 7BB (`MINAUTORE\MEMOIRE.md`, carte générée `MINAUTORE\ETAT_EXERCICE_7BB.md`) — à consulter pour tout RETEX ou réemploi.
- ⭐ **La fin de MINOTAURE DÉBLOQUE le portage de la vierge** (`D:\CECPC\MASTAURIGE\LOCALSTORAGE_WEB_VERSION`), gelé jusqu'ici (« vierge intacte d'ici là »). Backlog générique à porter avant le prochain exercice — voir [[vierge_porting_fin_minautore]] et `MASTAURIGE\MEMOIRE.md` (chercher « À PORTER dans la vierge ») : mécanisme **STARTEX PACKAGE** permanent (`00.00.00i`), les **3 correctifs calendrier** génériques (`dayorderToISO`→`COL_TO_ISO`, fusion drag scopée camp, colonnes dérivées), capacité **store baked articles**, navigation même onglet (`createur.js`), `shared\back-btn.js` à la racine, et le **split de card JEMM** (sous-inject `XX.YY.Izz<Lettre>`, ajouté 2026-06-30).
- Pour un nouvel exercice : partir de [[aurige_template_base]] (`SYSTEME\PROMPTS\aurige.md`) + méthodo transverse `AURIGE\MEMOIRE.md`.

Voir [[transition_minautore]], [[aurige7bb_minotaure]], [[mastaurige_instance_7bb]], [[mastaurige_instance_master_7bb]].
