---
name: mastaurige-pipeline-injects
description: Pipeline batch « inject as code » livré le 2026-06-10 (axe 1) — plan JSON → session importable MELMIL ; lo_config.js source unique ; livrable 3 (trombino auto) restant
metadata: 
  node_type: memory
  type: project
  originSessionId: 08c749e1-d2a0-4ea6-ab1e-0268dec9e9b0
---

**Axe 1 (automatisation 4+1) — état au 2026-06-10 :**
- ✅ **Livrable 1** : `OUTILS\generer_injects.py` + `GENERER_INJECTS.bat` + `PLAN_INJECTS_EXEMPLE.json` dans la vierge (`D:\CECPC\MASTAURIGE\LOCALSTORAGE_WEB_VERSION`). Plan JSON déclaratif → validations (camp vs avatars.js = CONTROLE G amont, codes auto port de TW.nextCode, LO, jours, langue, images base64) → `session_*.json` au format « Exporter mes modifs » → bouton **Importer** de MELMIL. Testé E2E (5 injects + 6 cas d'erreur + chaîne GENERER_ARTICLES).
- ✅ **Livrable 2** : `moteur/lo_config.js` = source unique séries→LO (`window.MASTAURIGE_LO`, valeur `"HN"` = ligne Host Nation) ; melmil.js (ROW_MAP/INCIDENT_LO/SPHERE_BLUE/PAYS_DELEGITIME) et index_master (`loFromNum`) dérivent de la config ; divergence avérée 08.03.04 corrigée. **7BB : adapter UNIQUEMENT lo_config.js.**
- ❌ **Livrable 3 restant** : trombinoscope RS généré depuis `avatars.js` (ajouter champs pays/bio + `generer_trombino.py`).

**Architecture 3 dossiers (2026-06-10 après-midi)** : `D:\CECPC\MASTAURIGE\` = `LOCALSTORAGE_WEB_VERSION` (traitants) + `JOUEURS_WEB_VERSION` (kit joueurs GÉNÉRÉ par `OUTILS\GENERER_KIT_JOUEURS.py` — sans animateur, avec `moteur/joueur.js` bouton « Importer les actus ») + `EXE_MASTER_VERSION` (console BASE `MASTER.bat` : fusion multi-traitants par id, **renumérotation des collisions de codes**, contrôles, sorties `CONSOLIDE_BASE_*.json` pour traitants + `actus_J<N>_*.json` épurées camp/LO pour joueurs). Cycle : traitants → Outlook → `_DEPOT\` → MASTER → Outlook → réimport 1 clic. `generer_articles.py` rendu importable (`render_article`). Le `.exe` (PyInstaller) reste optionnel — tout tourne en `.bat`. Testé E2E (collision ALPHA/BRAVO renumérotée, filtre jour, épuration).

**Why:** la cause racine des bugs MASTAURIGE était la vérité dupliquée + checklists manuelles ; le batch est le prérequis du volume « firehose » exigé par l'audit doctrinal pour 7BB ; la renumérotation BASE comble la seule limite du pipeline (codes attribués localement par navigateur).
**How to apply:** pour produire en masse → écrire PLAN_INJECTS.json (modèle dans OUTILS), jamais d'édition manuelle multi-fichiers. ⚠ `GENERER_VIERGE.py` (2BB) verrouillé anti-rollback (`--force-rollback`) : la vierge est la référence vivante, le 2BB source est périmé (templates.js/render.js/articles.js v0.3 absents côté 2BB). Détail canonique : `MASTAURIGE\MEMOIRE.md` § v0.2. Voir [[mastaurige-vierge-chemin]], [[mastaurige_outils_optim]].
