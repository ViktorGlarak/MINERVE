---
name: mastaurige-instance-7bb
description: "Outillage MASTAURIGE AURIGE 7BB / MINOTAURE 26 créé le 2026-06-10 (3 dossiers, MELMIL configuré D+33-41, storylines 07-01..04)"
metadata: 
  node_type: memory
  type: project
  originSessionId: 08c749e1-d2a0-4ea6-ab1e-0268dec9e9b0
---

Instance MASTAURIGE propre à **AURIGE 7BB / MINOTAURE 26** créée dans `D:\CECPC\PRODUCTION\EXER\AURIGE 7BB\00_Boites à outils\MASTAURIGE\` = 3 dossiers **LOCALSTORAGE_WEB_VERSION** (traitants) + **JOUEURS_WEB_VERSION** + **EXE_MASTER_VERSION**, noms identiques à la vierge globale (chemins relatifs des scripts → marchent sans modif).

**Config 7BB** (≠ 2BB) : `lo_config.js` 07-01→LO2 · 07-02→LO3 · 07-03→LO4 · 07-04→LO5, `paysDelegitime:"ARN"` · MELMIL `DAY_MAP` 9 jours **D+33→D+41 = 23 Jun→01 Jul 2026** (dayorder = D+) · thead/tbody/onglets régénérés · socle `melmil_data.js` = 18 incidents Event List 13/03. ⚠ **Camps INVERSÉS** (entraînés 7BB/27BIM/BFA = BLEU). Source des injects : `01_Montage exercice\` (synchromatrice V5 + Event List + Brainstorming + Main Body).

**⭐ Config par exercice (2026-06-10)** : nouveau système `exercice_config.json` (1 fichier à éditer : nom, dates, premierDPlus, nbJours, series→LO, lignes, phases, paysDelegitime, campsInverses) + `OUTILS\CONFIGURER_EXERCICE.bat` qui régénère automatiquement onglets jours + MELMIL (dates/phases/lignes LO) + lo_config.js + titres. **Plus d'édition manuelle de melmil.js/melmil_ili.html/index_master.** La **vierge globale est désormais NEUTRE** (0 trace 2BB : D+1-10, séries vides, socle vide). 7BB a son propre exercice_config.json. Détail : `MASTAURIGE\MEMOIRE.md` § système de config.

**Why:** la synchromatrice 7BB enfin reçue → MELMIL propre à MINAUTORE possible ; et la vierge contenait encore les données 2BB de GUILLAUME → fallait un vrai découplage config/contenu.
**How to apply:** pour toute prod 7BB, travailler dans cette instance (pas la vierge globale ni le 2BB). Détails techniques : `MASTAURIGE\MEMOIRE.md` § instance 7BB ; inventaire injects + dates : `MINAUTORE\MEMOIRE.md` (ingestion 2026-06-10). Sous-injects 07.02/03.1x-3x et codes 07-04 restent à créer. Voir [[aurige7bb_minotaure]], [[mastaurige_pipeline_injects]].
