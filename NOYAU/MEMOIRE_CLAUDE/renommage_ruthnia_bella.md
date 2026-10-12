---
name: renommage-ruthnia-bella
description: Le pays fictif Bella Russia a été renommé Ruthnia Bella (BR→RB) le 2026-05-31. Action MELMIL.xls encore en attente côté utilisateur.
metadata: 
  node_type: memory
  type: project
  originSessionId: 410ff7ab-cce4-44f7-9471-211855cef197
---

Le **2026-05-31**, correction d'une erreur de nom : le pays fictif **« Bella Russia » est renommé « Ruthnia Bella »** pour tous les exercices (en cours et à venir).

**Règles du renommage appliquées :**
- `Bella Russia` → `Ruthnia Bella` (et `BELLA RUSSIA` → `RUTHNIA BELLA`)
- Abréviation `BR` → `RB` (agent `ANALYSTE_BR` → `ANALYSTE_RB`, dossier `ANALYSTE\RUTHNIA_BELLA\`, prompt `analyste_rb.md`)
- Média : le **code `BC1` est conservé**, mais son nom complet devient **« Bella Channel 1 »** (avant : « Bella Russia Channel 1 »). Dossiers de site renommés `Site Bella Channel 1`.
- Hashtags renommés (`#BellaRussia` → `#RuthniaBella`, etc.).
- Fichiers/clés avec token `_BR_` renommés en `_RB_` (ex : `TV4_Article_Frontiere_RB_01`, `BCI_Article_CemaRB`, clé `@GromovaYelena_r1_RB_signals`, images `07.05.05_RB_...`).
- Dossier source **`CREATION\07 - RUTHNIA BELLA\`** (renommé depuis `07 - BELLA RUSSIA`).

**Portée traitée :** `IA\MINERVE` (+ dossier ANALYSTE + prompt), `EXER\AURIGE 2BB` (articles, trombinoscope, index_master, melmil_inject_index, snapshots D+, RTF), auto-mémoire, dossier CREATION.

**⚠ Préservé volontairement :** le fichier source `Opposition BellaRussia.docx` garde son nom (non renommé).

**⚠ ACTION UTILISATEUR EN ATTENTE :** `MELMIL.xls` (Excel binaire) et `melmil_data.js` (régénéré depuis le .xls) contiennent ENCORE « Bella Russia ». L'utilisateur doit : (1) rechercher-remplacer « Bella Russia »→« Ruthnia Bella » dans `MELMIL.xls`, puis (2) double-cliquer `Actualiser_MELMIL.bat` pour régénérer `melmil_data.js`. Tant que ce n'est pas fait, le tableau MELMIL affichera l'ancien nom. Voir [[melmil_coherence]].
