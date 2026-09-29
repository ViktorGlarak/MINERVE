---
id: LESSON-040
aliases: ["LESSON-040"]
type: lesson
title: Un contrôle qui arrive APRÈS coup ne protège rien — il détruit ce qu'il refuse
tags: [leac, carnet, vocaux, validation, conception, perte-silencieuse]
source: ../../LEAC/JOURNAL.md
linkedTo: [DECISION-032, LESSON-041, ARCH-014]
relevantFor: [leac, pleiade, mastorion]
tier: 1
created: 2026-09-22
updated: 2026-09-22
---

# LESSON-040 — Refuser trop tard, c'est jeter le travail

## Symptôme observé
Le carnet plafonnait un mémo vocal à **3 minutes / 5 Mo**, et refusait
poliment ce qui dépassait. Sauf que les octets d'un enregistrement **n'existent
qu'une fois le micro coupé** : répondre « trop long » à cet instant-là, c'est
**détruire ce que la personne vient de dire**, sans recours. Le message avait
l'air d'un garde-fou ; c'était une perte.

## Cause racine
Le plafond avait été **repris d'un autre contexte** sans que sa raison d'être
soit vérifiée : les 3 min / 5 Mo venaient des **pièces jointes**, qui, elles,
remontent au serveur (bande passante, disque, classification). Le carnet ne
remonte nulle part — la contrainte n'avait plus d'objet, mais son coût, lui,
était bien réel.

## Correctif / règle à appliquer
1. ⭐ **Un refus doit tomber AVANT que quoi que ce soit puisse être perdu.**
   Après capture, il ne reste que trois attitudes honnêtes : accepter,
   dégrader, ou prévenir — jamais jeter.
2. ⭐ **Une limite héritée se re-justifie dans son nouveau contexte**, sinon
   elle se supprime. Demander « qu'est-ce qui la rendait nécessaire, et
   est-ce encore vrai ici ? ».
3. Le seul refus resté possible sur un vocal : **il est vide** — le seul cas
   où il n'y a rien à perdre.
4. Quand une limite réelle subsiste (ici la place de l'appareil), on
   l'**affiche** au lieu de la faire deviner : place occupée par le carnet,
   durée et octets qui montent pendant l'enregistrement.

## 🔗 Source de vérité
Trace datée : `source:` (2026-09-22, « le plafond de 3 minutes est LEVÉ »).
**Pointeur, pas copie.**
