---
id: DECISION-023
aliases: ["DECISION-023"]
type: decision
title: LEAC — figer un cycle est un état métier, jamais un verrou d'écriture sur le journal
tags: [leac, metier, synchronisation, hors-ligne, cycle]
source: ../../LEAC/MEMOIRE.md
linkedTo: [ARCH-014, DECISION-021, DECISION-022, LESSON-034]
relevantFor: [leac]
tier: 2
created: 2026-09-17
updated: 2026-09-17
---

# DECISION-023 — Figer un cycle n'empêche personne d'écrire

## Contexte / problème
En fin de journée, le chef de contrôle **fige** le cycle : ce qui s'y trouve
fait foi pour la réunion. La tentation évidente est d'en faire un **verrou** :
plus rien n'entre après.

⚠ Ce serait reconstruire de nos mains le défaut de la v2.5, annoncé en toutes
lettres au § V.B.8 du memento utilisateur : *« toute modification effectuée
durant la synchronisation sera perdue »*. Car une note posée **hors ligne avant
le figeage** peut très bien ne **remonter qu'après** — c'est même le cas normal
quand un contrôleur rentre au bureau en fin de soirée.

## Décision
- **Figer est un état MÉTIER**, pas un verrou technique. Le journal reste ouvert.
- Une saisie postérieure est **acceptée et conservée**, puis **signalée** à
  l'écran : le chef de contrôle voit ce qui est arrivé après sa décision et
  tranche s'il rouvre.
- **Rouvrir n'efface rien** : c'est une opération de plus, la trace du figeage
  reste au journal.
- La comparaison « avant / après » se fait sur l'**horloge de Lamport**, **jamais
  sur une date** : deux tablettes n'ont pas la même heure, et une tablette
  éteinte trois jours revient avec une horloge murale fausse.
- ⚠ L'horloge de référence est lue **avant** d'écrire le figeage, sinon le
  figeage se signalerait lui-même comme une saisie tardive.

## Pourquoi (alternatives écartées)
**Refuser les opérations tardives** : simple, et faux — c'est exactement la perte
silencieuse que la v3 existe pour supprimer.
**Les accepter en silence** : le chef de contrôle croirait que le cycle figé est
ce qu'il a vu. La conservation sans signalement est un mensonge par omission.

## Conséquences / à respecter
- Corollaire d'ergonomie : **une seule réserve empêche de figer** — l'absence de
  porteur du drapeau (sinon le cycle est figé sur un bilan sans auteur). Toutes
  les autres **informent sans bloquer** : exiger la complétude produit le piège
  classique où un contrôleur absent bloque un cycle indéfiniment.
- L'écran doit **dire pourquoi** un avertissement ne bloque pas — sinon il se
  lit comme un bug.
- Même raisonnement à tenir pour tout futur état « validé / clôturé / archivé ».

## 🔗 Source de vérité
Détail complet : voir `source:` ci-dessus. **Cette note ne recopie pas — elle pointe.**
