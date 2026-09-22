---
id: DECISION-028
aliases: ["DECISION-028"]
type: decision
title: LEAC — l'AUTEUR fait partie de la cible d'une note ; un transverse noté par plusieurs n'est pas une collision
tags: [leac, journal, synchronisation, notation, transverse]
source: ../../LEAC/MEMOIRE.md
linkedTo: [DECISION-021, DECISION-024, DECISION-027, ARCH-014]
relevantFor: [leac]
tier: 1
created: 2026-09-18
updated: 2026-09-18
---

# DECISION-028 — `Note#<cycle>:<pointId>|<auteurId>`

## Contexte / problème
Deux contrôleurs d'un domaine **transverse** — noté par plusieurs, par
définition — écrivaient la même clé de journal et **s'écrasaient**. La
synchronisation le montrait comme une *collision* alors que c'était le cas
nominal. Défaut réel, révélé par l'analyse de conformité du 2026-09-18.

## Décision
- L'auteur entre dans la **cible** : `Note#<cycle>:<pointId>|<auteurId>#valeur`,
  `Observation#<cycle>:<domaineId>|<auteurId>#<champ>`.
- **Calcul** (`domaine/apports.ts`) : domaine de **fonction** → valeur la plus
  récente tous auteurs ; domaine **transverse** → moyenne des moyennes de
  chaque observateur, **pondérée** par le paramétrage (`poidsDe`) ; domaine non
  paramétré → tout le monde pèse 1.
- La case « retenu dans la moyenne » décide qui **pèse**, jamais qui **voit**.

## Pourquoi (alternatives écartées)
- Fusionner par « dernier écrit gagne » : perd une notation légitime sans le dire.
- Une cible par appareil plutôt que par auteur : le même officier change de
  tablette ; c'est la personne qui note.

## Conséquences / à respecter
- Le label **proposé** par le calcul est **validé par le chef de contrôle** ;
  s'en écarter sans justification = manque **bloquant** du CRF.
- Un critère écarté par le mandat (`Selection#<id>#retenu=false`) sort des
  grilles, ses notes restent au journal.

## 🔗 Source de vérité
Détail complet : voir `source:` ci-dessus (Règle 25). **Cette note ne recopie pas — elle pointe.**
