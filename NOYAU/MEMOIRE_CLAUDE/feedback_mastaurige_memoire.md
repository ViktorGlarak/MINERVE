---
name: feedback-mastaurige-memoire
description: "Règle NON négociable : consulter ET mettre à jour MASTAURIGE\\MEMOIRE.md à chaque intervention sur l'outillage MASTAURIGE — sans rappel"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 9cd755be-0651-44f5-8932-5974a21bced9
---

**Quand je touche à l'OUTILLAGE MASTAURIGE** (code WEB : `melmil.js`, `createur.js`, `index_master.html`, `GENERER_VIERGE.py`, la vierge `…\MASTAURIGE\LOCALSTORAGE_WEB_VERSION`, les `.bat`, le trombinoscope, les sites médias, les conventions) :
1. **LIRE `MASTAURIGE\MEMOIRE.md` AVANT** d'intervenir (état/capacités courants).
2. **METTRE À JOUR `MASTAURIGE\MEMOIRE.md` JUSTE APRÈS** (section « v0.2 — FAIT FOI »), **dans la même session**, **sans attendre que l'utilisateur le demande**.

**Why:** lors de la session du 2026-06-04, j'ai fait de nombreuses évolutions MASTAURIGE (Vider_MELMIL.bat, bouton « Tout vider »/masque socle, convention `Trombinoscope/img/`, moteur injects créés, renommage `melmil_ili.html`, fix `empty_obj` du générateur…) **sans les consigner dans `MASTAURIGE\MEMOIRE.md`** — l'utilisateur a dû me le rappeler, ce qui l'a agacé à juste titre. La règle existait déjà dans `CLAUDE.md` (« mise à jour automatique — OBLIGATOIRE ») mais je ne l'ai pas appliquée à cette mémoire pendant une longue session.

**How to apply :** réflexe systématique (renforcé dans `CLAUDE.md` + un **hook** PostToolUse qui me le rappelle à chaque édition d'un fichier MASTAURIGE). Ne jamais clôturer une session ayant touché MASTAURIGE sans avoir mis à jour sa mémoire. Voir [[mastaurige]].
