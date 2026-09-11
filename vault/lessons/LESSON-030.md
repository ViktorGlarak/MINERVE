---
id: LESSON-030
aliases: ["LESSON-030"]
type: lesson
title: Ne jamais déduire un champ d'API par supposition avant une suppression de masse
tags: [api, destructif, methode, garde-fou, eho]
source: ../../PLEIADE/JOURNAL.md
linkedTo: [DECISION-015, LESSON-029]
relevantFor: [pleiade, mastorion, outillage]
tier: 2
created: 2026-09-11
updated: 2026-09-11
---

# LESSON-030 — La suppression de masse fondée sur un champ supposé

## Symptôme observé
En voulant purger les groupes **vides** d'un EHO, **les 63 groupes ont été
supprimés** — CAMP ROUGE, STARTEX et les groupes d'exercice compris — vidant
1 600 appartenances d'un coup.

## Cause racine
Le filtre « groupe vide » testait `_count.users`, puis `userCount`, puis
`nbAvatars` — **trois noms supposés**, aucun n'existant dans la réponse réelle de
`/api/groups`. Tous les compteurs valant `undefined`, **tout groupe paraissait
vide**. La boucle a ensuite appliqué la suppression sans jamais vérifier.

## Correctif / règle à appliquer
- **Lire la réponse réelle de l'API avant de filtrer dessus** — un simple `GET`
  affiché l'aurait montré en deux secondes.
- **Pour toute opération destructive : vérifier sur UN élément avant de boucler**
  (le premier `DELETE` aurait révélé l'erreur de sélection).
- Se méfier des `?.` et des `|| 0` : ils transforment une **clé absente** en
  valeur « légitime » et font disparaître l'erreur au lieu de la signaler.
- Réparation ici : réimport du classeur (`updated 453`) — possible **parce que la
  source de vérité vivait hors de l'application**. C'est un argument de plus
  pour garder les bibliothèques MINERVE comme référence.

## 🔗 Source de vérité
Détail / trace : voir `source:`. **Pointeur, pas copie.**
