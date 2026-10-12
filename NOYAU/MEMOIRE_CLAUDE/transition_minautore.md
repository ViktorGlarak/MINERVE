---
name: transition-minautore
description: AURIGE 2BB (GUILLAUME) terminé — prochaine phase = créer MASTAURIGE MINAUTORE depuis la vierge (sur top utilisateur)
metadata: 
  node_type: memory
  type: project
  originSessionId: 9cd755be-0651-44f5-8932-5974a21bced9
---

**Bascule de phase (annoncée le 2026-06-04) :** l'exercice **GUILLAUME / AURIGE 2BB est TERMINÉ**.

- **Ne plus travailler** dans le dossier MASTAURIGE dédié à Guillaume : `D:\CECPC\PRODUCTION\EXER\AURIGE 2BB\00_Boites à outils\MASTAURIGE\WEB` (figé/archivé).
- **Prochaine étape** : créer une nouvelle version **« MASTAURIGE MINAUTORE »** pour l'exercice **MINAUTORE** (= AURIGE 7BB / MINOTAURE 26, cf. [[aurige7bb-minotaure]]) **à partir de la VIERGE** `D:\CECPC\MASTAURIGE\LOCALSTORAGE_WEB_VERSION` (cf. [[mastaurige-vierge-chemin]]) — par copie de la vierge, puis remplissage du contenu MINAUTORE.
- ⚠ **À FAIRE UNIQUEMENT SUR TOP EXPLICITE de l'utilisateur** — il a dit « je le dirai ». Ne rien créer/copier avant son signal. Il donnera l'emplacement cible et les détails à ce moment-là.

Rappel agent : **MINAUTORE** = chef d'orchestre éditorial AURIGE 7BB (équivalent de GUILLAUME pour le 7BB). ⚠ camps INVERSÉS en 7BB (entraînés = BLEU attaquent ; MER = ROUGE défend) — voir [[aurige7bb-minotaure]].

**À prévoir au lancement MINAUTORE (dit par l'utilisateur le 2026-06-04) :**
- Le **`.xls` MELMIL** de MINAUTORE pourra avoir un **autre format / d'autres séries** que le 2BB. Le moteur web actuel fonctionne très bien tel quel — **on ne le retouche pas** pour l'instant.
- ⚠ Si les **séries→LO changent**, mettre à jour **les DEUX** tables série→LO (un commentaire « GARDER SYNCHRONISÉ » est posé dans chaque) : `ROW_MAP` dans `MELMIL/melmil.js` **et** `_LO_BY_SERIES`/`_LO_BY_INCIDENT` dans `index_master.html`.
- **Régénérer la vierge** avec le générateur corrigé (`OUTILS\GENERER_VIERGE.py`, `empty_obj` désormais commentaire-aware) avant de bâtir MINAUTORE — la vierge embarquera tous les correctifs moteur de juin 2026 (injects créés : date propre · split camp · LO série · nom repris du `.xls` · ghost clair seulement hors-`.xls`).
