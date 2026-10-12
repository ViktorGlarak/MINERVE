---
name: feedback-release-notes-pleiade
description: "Toute mise à jour poussée sur PLÉIADE doit avoir ses notes de version (demande de Xavier, 2026-10-03)"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 699185de-99a6-4263-a321-d605be7e2b29
  modified: 2026-10-03T10:25:41.284Z
---

Chaque mise à jour poussée sur un dépôt PLÉIADE (`cecpc-pleiade`) doit laisser des **notes de version** (release notes), pour garder l'historique des mises à jour.

**Why:** demande de Xavier, relayée par l'utilisateur le 2026-10-03. Constat ce jour-là : aucun dépôt n'avait de CHANGELOG ni de notes de version ; l'étape « tag immuable prod-* » du workflow de déploiement échoue en silence (`continue-on-error`) → aucun tag `prod-*` sur GitHub. L'historique n'existait que dans les messages de commit et dans `PLEIADE\JOURNAL.md` (dépôt MINERVE, invisible pour Xavier).

**How to apply:** à chaque push PLÉIADE, rédiger/mettre à jour les notes de version du dépôt dans le même commit (format retenu avec l'utilisateur, à confirmer), en langage clair pour les utilisateurs + une ligne technique. Voir aussi [[feedback-tester-en-local-avant-push]].
