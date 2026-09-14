---
id: DECISION-016
aliases: ["DECISION-016"]
type: decision
title: Le rangement du joueur (rubriques + ordre) est une préférence d'affichage, stockée à part
tags: [eho, pleiade, joueur, schema, design]
source: ../../PLEIADE/MEMOIRE.md
linkedTo: [DECISION-015, LESSON-032, ARCH-012]
relevantFor: [pleiade, exercices]
tier: 2
created: 2026-09-14
updated: 2026-09-14
---

# DECISION-016 — Ranger n'est pas répondre

## La décision
Dans la planche du joueur, **la zone où se trouve une carte est une RÉPONSE**
(mesurée par le Comparatif) ; **la rubrique et la position ne sont qu'un
rangement personnel**. Les deux sont donc stockées séparément :

| | Où | Entre dans le calcul d'écart ? |
|---|---|---|
| Zone, camp, fonction, note | `eho_lectures` (une ligne par carte lue) | **oui** |
| Rubriques et ordre | `eho_dispositions` (**une ligne par joueur**, JSON) | **non** |

## Pourquoi une seule ligne par joueur
Une colonne d'ordre par carte aurait écrit **391 lignes** pour remonter un
avatar d'un cran dans le bac « à classer ». La disposition est donc un objet
JSON `zone → { rubriques, cartes }`, avec des listes **partielles** : seul ce
que le joueur a déplacé à la main y figure, le reste suit l'ordre par défaut.

## Conséquences utiles
- Réordonner ou créer une rubrique **ne touche jamais à l'analyse** du joueur.
- Entrer au package STARTEX **purge les estimations** mais **conserve** le
  rangement et les notes.
- **L'animateur voit la planche à l'identique** : les deux écrans appellent la
  même fonction de répartition, la divergence est impossible par construction.
- Un écran filtré **n'enregistre pas ce qu'il affiche** : l'ordre est calculé
  sur la zone complète, sinon une recherche en cours amputerait le rangement
  des cartes masquées.

## Règle générale qui s'en dégage
**Deux champs qui disent la même chose finissent par se contredire.** Même
raison pour laquelle le camp estimé est *déduit* du curseur d'alignement au lieu
d'être saisi en parallèle — et c'est sur le camp que la comparaison marque les
écarts.
