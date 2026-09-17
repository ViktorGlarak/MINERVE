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

## À quoi sert le drapeau (le memento ne le dit jamais)
Un **domaine transverse** — fonctionnement général du PC, travail collectif —
**n'appartient à aucune fonction** : plusieurs contrôleurs l'observent, chacun
depuis son poste. Les **notes** se moyennent, pondérées par membre. Les
**observations**, elles, sont du **texte libre** : on ne fait pas la moyenne de
quatre paragraphes. **Il faut donc une voix**, et le drapeau la désigne — c'est
son bilan que projette la réunion du soir (memento p. 27).

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
- ⚠ **Écart assumé** : la v2.5 écrit *« SEULS ses commentaires seront vus »* —
  le travail écrit de trois contrôleurs disparaît de la réunion sans que
  personne le sache. En v3 le bilan du porteur reste la **parole officielle,
  seule affichée par défaut** (l'intention est tenue : une seule voix), mais les
  autres observations sont **dépliables**, nommées, « hors bilan officiel ».
  Le drapeau existe parce qu'on ne peut pas moyenner du texte ; ce problème est
  réglé dès qu'une seule voix s'affiche par défaut. Effacer les autres n'y
  ajoute rien et coûte une remarque juste de temps en temps.
  **Réversible en une ligne** si le CECPC préfère la règle stricte.
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
