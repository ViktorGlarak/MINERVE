---
name: jemm-melmil-import
description: JEMM remplace GESTIM ; MELMIL exportée en JSON ; importateur unifié generer_melmil.py (fusion GESTIM+JEMM)
metadata: 
  node_type: memory
  type: project
  originSessionId: 08c749e1-d2a0-4ea6-ab1e-0268dec9e9b0
---

**JEMM** est le nouveau logiciel de scénarisation (remplace **GESTIM**). Il exporte la MELMIL en **JSON** (1 fichier = 1 *Event* ; `Data.Events / Storylines / Injections`), contrairement à GESTIM qui sortait du `.xls`.

**Outil livré le 2026-06-16** : `…\MASTAURIGE\…\MELMIL\generer_melmil.py` = importateur **unifié adaptatif** (Python stdlib) qui lit `.xls` (GESTIM) OU `.json` (JEMM) et produit le même `melmil_data.js`.
- `--source auto|gestim|jemm|both` (auto = JEMM si `MELMIL\JEMM\*.json` présents, sinon GESTIM).
- `--mode fusion|remplacer` (défaut : gestim→remplacer historique ; jemm→**fusion** = ajoute sans perdre le socle ILI fait main, dédup par `code`).
- Conversion code JEMM `EE.SS.Innn` → MELMIL `EE.SS.nni` (ex. `08.01.I01` → `08.01.01i`).
- Boîte d'arrivée : déposer les `.json` (ou dossiers EVENT extraits) dans `MELMIL\JEMM\`, puis `Actualiser_MELMIL.bat` (auto) ou `Actualiser_MELMIL_JEMM.bat`. `generate_data.py` (GESTIM seul) gardé en secours → **GESTIM jamais cassé**.

**Why:** le CECPC bascule de GESTIM à JEMM ; il fallait pouvoir importer la nouvelle MELMIL sans casser l'existant et sans perdre la trame ILI construite à la main.

**How to apply:** déployé dans la **vierge** (`D:\CECPC\MASTAURIGE\LOCALSTORAGE_WEB_VERSION\MELMIL`) et l'**instance 7BB**. EVENT_07 (ILI) sort vide de JEMM → contenu rouge à produire par MINAUTORE ; EVENT_08 (HOST NATION, 8 injects 08.01/08.02) ingéré. ⚠ Routage : 08.xx hors lo_config → ligne r7 « autres » (à trancher : ligne HN dédiée). Détail exhaustif : `MASTAURIGE\MEMOIRE.md` § « IMPORTATEUR MELMIL UNIFIÉ » + `MINAUTORE\MEMOIRE.md` § « MELMIL via JEMM ». Voir [[mastaurige_pipeline_injects]], [[mastaurige_instance_7bb]], [[aurige7bb_actif]].
