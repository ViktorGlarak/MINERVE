---
id: DECISION-021
aliases: ["DECISION-021"]
type: decision
title: LEAC — on écrit un CHAMP par cible, jamais un objet entier ; c'est la granularité qui achète l'absence de conflit
tags: [leac, synchronisation, hors-ligne, conception]
source: ../../LEAC/MEMOIRE.md
linkedTo: [ARCH-014, DECISION-022]
relevantFor: [leac, pleiade]
tier: 2
created: 2026-09-17
updated: 2026-09-17
---

# DECISION-021 — La granularité d'écriture est une décision de conception, pas un détail

## Contexte / problème
Plusieurs contrôleurs travaillent **en parallèle et hors ligne** sur le même
contrôle, puis leurs journaux se fondent au retour. La question n'est pas *si*
deux écritures vont se croiser, mais **sur quoi** elles se croisent.

## Décision
**Une opération porte un champ, et un seul.** Jamais un objet agrégé.

- Équipe : `MembreEquipe#<id>#nom`, `…#poids`, `…#peutObserver` — **jamais** un
  objet « équipe ».
- Observations : **une cartouche = un champ** (`pointsPositifs`,
  `pointsAAmeliorer`, `pointsDeVigilance`, `propositions`,
  `observationGenerale`).
- Notation : une feuille = une cible.

## Pourquoi (alternatives écartées)
Écrire l'équipe **en bloc** ferait qu'un officier de marque modifiant un **poids**
écraserait le **nom** qu'un collègue vient de corriger sur une autre ligne —
alors que les deux gestes n'ont **rien à voir**. Le moteur de fusion ne peut pas
le savoir : pour lui, deux écritures sur la même cible sont un conflit.

⭐ Champ par champ, les cibles sont **disjointes** : la propriété « ils ne
peuvent pas se recouvrir » est obtenue **gratuitement**, sans arbitrage et sans
demander quoi que ce soit à l'utilisateur.

## Conséquences / à respecter
- Tout nouvel écran qui persiste doit **décomposer** son état en champs avant
  d'écrire. Un `JSON.stringify` d'un formulaire entier dans une seule opération
  annulerait la propriété.
- Corollaire pour la saisie libre : écriture **différée** (repos de frappe) *et*
  **sortie de champ**. La v2.5 n'écrivait qu'à la sortie de case (§ II.B) —
  insuffisant sur tablette : écran verrouillé, bascule d'application ou batterie
  à plat, et la sortie n'arrive jamais. On perdrait le **dernier** paragraphe,
  donc le plus récent.
- À l'inverse, un **clic** (poids, case à cocher) s'écrit **immédiatement** :
  différer un geste unique n'apporte rien et retarde sa remontée.

## 🔗 Source de vérité
Détail complet : voir `source:` ci-dessus. **Cette note ne recopie pas — elle pointe.**
