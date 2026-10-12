---
name: reference-essai-image-crlf
description: "Essai local d'une image Docker PLEIADE sous Windows — construire depuis git sans conversion CRLF, sinon l'entrypoint « n'existe pas »"
metadata:
  node_type: memory
  type: reference
  originSessionId: 699185de-99a6-4263-a321-d605be7e2b29
  modified: 2026-09-23T15:12:42.992Z
---

Sur ce poste, `core.autocrlf=true` : la copie de travail des dépôts `C:\CECPC\pleiade\*` est en **CRLF** alors que le dépôt est en LF. Construire une image depuis la copie de travail donne un conteneur qui meurt aussitôt : `exec ./docker-entrypoint.sh: no such file or directory`.

Ce n'est **pas** un défaut du dépôt : le runner du serveur (Linux) construit depuis git, en LF.

Pour un essai local fidèle : `git -c core.autocrlf=false archive --format=tar HEAD | docker build -t <nom> -` — ⚠ `git archive` sans l'option convertit **aussi**. Constaté le 2026-09-23 sur `app-melmil`. Voir [[feedback_indicateur_etat]] (tester contre le vrai système).
