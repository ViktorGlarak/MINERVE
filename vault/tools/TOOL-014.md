---
id: TOOL-014
type: tool
title: generer_etat_exercice.py — carte de référence générée de l'exercice (MINAUTORE)
tags: [minautore, aurige, etat-exercice, calendrier, synchromatrice, generateur]
source: ../../MINAUTORE/MEMOIRE.md
linkedTo: [PROJ-AURIGE-7BB, AGENT-MINAUTORE, LESSON-017]
relevantFor: [minautore, exercices]
tier: 2
created: 2026-06-21
updated: 2026-06-21
---

# TOOL-014 — generer_etat_exercice.py (carte de référence MINAUTORE)

## Rôle
Donne à **MINAUTORE** (référent de l'exercice) une **carte maîtresse régénérable** : `MINAUTORE/ETAT_EXERCICE_7BB.md`. Permet de répondre « quel inject / date / persona / jour, cet article est-il utilisé ? » **sans grep aveugle** (cf. [[LESSON-017]]).

## Mécanique
- Script `MINAUTORE/generer_etat_exercice.py` — **lit les données réelles** de l'instance collab 7BB : `MELMIL/melmil_data.js` (socle JEMM : code, sujet, date→D+, état) + `moteur/tweets_data.js` + `moteur/articles_data.js` (bakés : num, type, persona, dayorder, LO) + `moteur/lo_config.js` (storylines→LO).
- **Sortie** `ETAT_EXERCICE_7BB.md` : calendrier **D+↔date↔phase** (GELEX=29 juin sans D+), storylines→LO, **registre complet des injects** (code · D+ · LO · type · persona · sujet), **vue par jour** D+31→D+41.
- **À relancer après TOUTE modif** de l'exercice (`py MINAUTORE/generer_etat_exercice.py`) — sinon la carte (et MINAUTORE) n'est plus fiable. *(2026-06-21 : 57 codes, 52 injects bakés, 57 cards socle.)*

## À porter
Même principe recommandé pour **GUILLAUME 2BB** (carte de référence générée propre à l'exercice).

## 🔗 Source de vérité
Détail : `MINAUTORE/MEMOIRE.md` (en-tête « Carte de référence » + journal 2026-06-21). **Pointeur, pas copie.**
