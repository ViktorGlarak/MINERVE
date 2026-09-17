---
id: DECISION-022
aliases: ["DECISION-022"]
type: decision
title: LEAC — le « drapeau » devient un choix explicite et un filtre réel, il ne dépend plus d'un ordre de clic
tags: [leac, metier, observations, tableau-de-bord, ergonomie]
source: ../../LEAC/MEMOIRE.md
linkedTo: [ARCH-014, DECISION-021, LESSON-034]
relevantFor: [leac]
tier: 2
created: 2026-09-17
updated: 2026-09-17
---

# DECISION-022 — Une conséquence lourde ne peut pas dépendre de l'ordre dans lequel on a coché des cases

## Contexte / problème
Memento utilisateur § V.A.3 : sur un domaine transverse, *« la première personne
cochée aura un petit drapeau ; seuls ses commentaires seront vus dans le tableau
de bord »*.

Deux défauts, et le second est le plus grave :
1. La désignation dépend d'un **ordre de clic** — invisible, non rejouable, et
   que personne ne se rappelle une semaine plus tard.
2. C'était un **avertissement écrit dans un manuel**, donc une règle que le
   logiciel **n'appliquait pas**. Le tableau de bord montrait tout.

## Décision
- Le porteur du drapeau se **désigne explicitement** (un bouton « donner le
  drapeau »), et l'écran **nomme la conséquence** au lieu de la cacher.
- Le tableau de bord **filtre réellement** sur l'**auteur** des observations.
- Les remarques des autres sont **écartées du bilan, jamais supprimées** — et
  l'écran l'écrit en clair.
- Retirer le droit d'observer au porteur **déplace** le drapeau au lieu de le
  laisser orphelin.
- Si personne ne le porte, l'écran le signale : sans cela, un tableau de bord
  vide se lit comme « rien à dire » au lieu de « mal paramétré ».

## Pourquoi (alternatives écartées)
Garder « la première cochée » aurait été fidèle au memento — mais fidèle à un
**défaut**. Tout le sens de la v3 est de traduire en propriétés du logiciel ce
que la v2.5 confiait à la mémoire de l'utilisateur.

## Conséquences / à respecter
- ⚠ Appliquer ce filtre **exige de connaître l'auteur de chaque valeur** : d'où
  `lireEtatDetaille`, qui rend `{valeur, auteurId, horloge}` et non la seule
  valeur. Toute règle métier portant sur « qui a écrit » en dépend.
- Le lien auteur ↔ membre d'équipe passe par `MembreEquipe.identityId`
  (UUID eho / `sub` Keycloak), **nullable** : un renfort créé la veille en local
  (§ V.B.3) n'en a pas encore.

## 🔗 Source de vérité
Détail complet : voir `source:` ci-dessus. **Cette note ne recopie pas — elle pointe.**
