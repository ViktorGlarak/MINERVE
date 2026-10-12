---
name: todo_durcir_import_jemm
description: TODO différé — fiabiliser generer_melmil.py lire_existant() pour que la fusion JEMM ne détruise pas les injects curatés
metadata: 
  node_type: memory
  type: project
  originSessionId: a68d232b-0e67-4473-8fe3-3260ee347b9f
---

TODO (différé, demandé 2026-06-23 « on le fera peut-être plus tard ») — **durcir l'import JEMM manuel** de MASTAURIGE.

**Problème :** `MELMIL\generer_melmil.py` → `lire_existant()` attend un `melmil_data.js` à clés NON quotées (`injections:`), mais le socle actuel a été synchronisé à la main avec clés **quotées** (`"injections":`). Du coup la regex échoue → `lire_existant()` renvoie `[]` → le mode **fusion bascule en REMPLACEMENT total**. Un run `Actualiser_MELMIL_JEMM.bat` aujourd'hui **supprimerait 21 injects curatés** absents des exports JEMM (07.03.I03→I10, 07.05.I02/I03, 07.06.I02/I03, 07.08.I02, 07.09.I02, 07.11.I06/I07, 07.12.I01→I05).

**À faire quand demandé :**
1. Rendre `lire_existant()` robuste (lire aussi clés quotées — ou parser `var MELMIL_DATA = {...}` en JSON tolérant) sur les **4 instances** (collab + traitant + 2 vierges).
2. Ajouter un **mode rapport / dry-run** : lister AVANT écriture ce qui bouge / s'ajoute / disparaît.
3. Avertir quand un **contenu baké** (article/tweet) a un `dayorder` qui ne colle plus à la nouvelle date JEMM (l'import JEMM déplace la card MELMIL socle mais PAS le dayorder du contenu baké — 2 couches distinctes).

Rappel mécanique : fusion = `par_code[code]=jemm` (JEMM écrase par code → déplace la card MELMIL à la date JEMM) ; `updated` change → cards supprimées à la main réapparaissent ; bumper `?v=` melmil_data.js après. Détail conversation : `MASTAURIGE\MEMOIRE.md` / synchro ligne 08 [[project_mercure]].
