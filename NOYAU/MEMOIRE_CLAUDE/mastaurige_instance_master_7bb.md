---
name: mastaurige-instance-master-7bb
description: Quelle instance MASTAURIGE 7BB est le MASTER éditorial (où éditer) — éviter la confusion des dossiers
metadata: 
  node_type: memory
  type: project
  originSessionId: 4377e89f-f0dd-40af-851d-ddfb523fd276
---

**MASTER éditorial AURIGE 7BB = `D:\CECPC\PRODUCTION\EXER\AURIGE 7BB\00_Boites à outils\MASTAURIGE\LOCALSTORAGE_WEB_VERSION`** (⚠ le `MASTAURIGE\` est dans le chemin). C'est LÀ qu'on édite tweets/articles/MELMIL/trombino/statuts ; c'est la source du rebuild kit JOUEURS.

- `…\MASTAURIGE\JOUEURS_WEB_VERSION` = kit joueurs (régénéré/sync depuis le master).
- `…\MASTAURIGE\SERVEUR_COLLABORATIF\mastaurige` = **HS/obsolète** depuis 2026-06 — NE PAS l'utiliser comme source de vérité.
- ⚠ **2026-06-27** : la carte `MINAUTORE\generer_etat_exercice.py` lisait encore le collab → repointée sur `LOCALSTORAGE_WEB_VERSION` (master). Régénérer la carte la lit donc bien à jour.
- ⚠ **Piège dossiers parasites** : `sync_trombino_joueurs.py` avait un `ROOT` faux → créait `00_Boites à outils\{LOCALSTORAGE,JOUEURS}_WEB_VERSION` (SANS `MASTAURIGE`, dossiers VIDES parasites). Corrigé (`ROOT=dirname(MAST)`). Si tu revois un `…\00_Boites à outils\LOCALSTORAGE_WEB_VERSION` sans `MASTAURIGE` → c'est un parasite, pas le master.

**Why:** confusion répétée entre les instances (et un dossier « vide » alarmant) — perte de temps le 2026-06-27.

**How to apply:** toute édition de contenu/outillage 7BB → cibler le chemin `…\MASTAURIGE\LOCALSTORAGE_WEB_VERSION`. Voir [[mastaurige_instance_7bb]], [[mastaurige_vierge_chemin]], détail dans `MASTAURIGE\MEMOIRE.md`.
