---
id: DECISION-017
aliases: ["DECISION-017"]
type: decision
title: Modèle de branches — on travaille sur une provisoire, on intègre dans main, on déploie par prod
tags: [pleiade, git, deploiement, securite, prod]
source: ../../PLEIADE/MEMOIRE.md
linkedTo: [ARCH-013, ARCH-012, DECISION-019]
relevantFor: [pleiade, mastorion, outillage]
tier: 1
created: 2026-09-16
updated: 2026-09-16
---

# DECISION-017 — `main` on travaille, `prod` on DÉPLOIE

## Contexte / problème
La convention existait dans les faits mais **n'était écrite dans aucun `.md`** —
seulement dans l'en-tête des workflows GitHub. Un agent qui pousse « pour
enregistrer » pouvait donc déclencher une mise en production sans le savoir.

## Décision
Trois étages : **branche provisoire** (on y fait le travail) → **`main`**
(branche principale d'intégration) → **`prod`** (ce qui tourne réellement,
devant des participants).

⚠ **Pousser sur `prod` n'est pas un enregistrement : c'est LE geste de
déploiement.** Le workflow construit l'image sur un runner hébergé **sur le
serveur d'exercice** et promeut la version sur les zones de production.

## Pourquoi
Mot pour mot l'en-tête du workflow d'`eho` : *« `main` est là où l'on travaille ;
`prod` est ce qui tourne devant des participants […] **une app cassée se voit en
salle**, pas seulement par nous. »*

## Conséquences / à respecter
- **Ne jamais pousser sur `prod` sans demande explicite pour CE dépôt-là.** Une
  autorisation donnée une fois ne vaut pas pour la suivante.
- **Toujours annoncer l'effet avant de pousser** : « ceci enregistre le travail »
  et « ceci déploie devant les participants » ne sont pas la même phrase.
- ⚠⚠ **Exception `pleiade-platform` : aucune branche `prod`** — son workflow se
  déclenche sur **`main`**. Y pousser **déploie immédiatement** (seul garde-fou :
  les `.md` sont ignorés).
- `pleiade-infra`, `app-webserver`, `app-wordpress` : aucun déploiement
  automatique.
- La promotion **ne touche que les instances de l'app concernée** — une
  correction urgente ne coupe pas les autres apps d'un exercice en cours.

## 🔗 Source de vérité
`PLEIADE/MEMOIRE.md` §2bis (tableau dépôt → branche qui déploie) et règle 2bis
des règles de travail de l'agent.
