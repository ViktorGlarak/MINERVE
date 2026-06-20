---
id: DECISION-009
type: decision
title: Cartographie des injects ILI — « Piste C » (storyline = structure JEMM, LO = étiquette)
tags: [jemm, melmil, mastaurige, ili, lo, storyline, methodo]
source: ../../MASTAURIGE/MEMOIRE.md
linkedTo: [PROJ-AURIGE-7BB, TOOL-013]
relevantFor: [mastaurige, minautore, expert-influence]
tier: 2
created: 2026-06-20
updated: 2026-06-20
---

# DECISION-009 — Cartographie des injects ILI « Piste C »

## Contexte / problème
Modèle de conception à **4 axes** (Thème ILI ▸ Ligne d'Opération ▸ Storyline ▸ Inject) mais **JEMM ne range que sur 3 colonnes** (`EE.SS.Inn`). En forçant la LO comme niveau (12 « thématiques » 07.01-07.12), une storyline narrative (ex. « Vorin ») se retrouve **éclatée** sur plusieurs codes → incohérent. Cause profonde : **LO et Storyline sont des axes CROISÉS** (une storyline sert plusieurs LO ; une LO est servie par plusieurs storylines), pas une hiérarchie.

## Décision
**Le code d'inject `EE.SS.Inn` est le contrat partagé. On structure JEMM par STORYLINE (le récit), la LO devient une ÉTIQUETTE par inject** (pas une colonne). JEMM = exécution (récit + dates) ; MASTAURIGE / synchromatrice = planification (vue par LO, lue dans l'étiquette). Mécanisme déjà présent : `lo_config.incidents` (LO par inject). ⚠ **Proposition validée comme logique** (vitrine = la [[TOOL-013]]) ; **re-cartographie effective des codes JEMM à acter** avec l'utilisateur.

## Pourquoi (alternatives écartées)
- **B — LO encodée dans la dizaine du numéro** (07.2x = LO2…) : garde la LO lisible dans JEMM mais **plafonne à ~9 storylines/LO** → écartée.
- **LO = niveau (état actuel)** : déchire les storylines → le problème lui-même.
- **Piste C (découplage total)** retenue : storylines illimitées, JEMM intact, LO préservée comme attribut + secondaire possible (inject multi-LO).

## Conséquences / à respecter
- En **début d'exercice** : on PART des LO (lignes directrices) pour **bâtir les storylines**, puis on numérote librement.
- Chaque inject porte sa **LO** (étiquette) → la synchromatrice/synchro-effets reste une **vue dérivée**.
- Les LO **ne disparaissent pas** : elles vivent à travers MASTAURIGE.

## 🔗 Source de vérité
Détail + artefacts : `MASTAURIGE/MEMOIRE.md` (synchromatrice) et [[TOOL-013]]. Doctrine LO transverse : `EXPERT_INFLUENCE/MEMOIRE.md`. **Pointeur, pas copie.**
