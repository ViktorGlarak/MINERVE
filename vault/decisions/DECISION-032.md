---
id: DECISION-032
aliases: ["DECISION-032"]
type: decision
title: LEAC — le carnet de terrain entre avant la grille, et ne quitte jamais l'appareil
tags: [leac, terrain, carnet, vocaux, hors-ligne, indexeddb, classification]
source: ../../LEAC/MEMOIRE.md
linkedTo: [ARCH-014, DECISION-021, LESSON-040, LESSON-041]
relevantFor: [leac, pleiade]
tier: 1
created: 2026-09-22
updated: 2026-09-22
---

# DECISION-032 — Le brouillon d'abord, la copie ensuite

## Contexte / problème
Premier retour d'un contrôleur sur LEAC **déployé** : en entrant dans un
exercice, on tombait droit sur la **grille d'évaluation**. Or sur le terrain,
personne ne retrouve *le bon critère* parmi quatorze domaines et 1 352 lignes
au moment où il faut regarder ailleurs. Ce dont un contrôleur a besoin sur
l'instant, c'est de **noter**, et de trier le soir.

## Décision
1. **L'entrée d'un contrôle est un carnet de terrain** : plusieurs notes
   **texte** et **mémos vocaux**, à traiter / traitées, les plus récentes en
   tête. La grille passe sous `/controle/<id>/grilles`.
2. Une note **mène à la grille** (`?note=`) : elle reste **épinglée** en tête
   d'écran le temps de chercher le critère, puis se marque traitée.
3. ⚠⚠ **Le carnet reste sur l'appareil.** Ni journal d'opérations, ni
   synchronisation, ni téléversement — table IndexedDB à part. C'est la
   **seule** écriture locale qui contourne `depot.ecrire`, et c'est voulu.

## Pourquoi (alternatives écartées)
- **Faire remonter les notes** comme les pièces jointes : rejeté par
  l'utilisateur. Et cela rouvrait la question **non tranchée** de la
  classification d'un enregistrement pris dans un PC en exercice ([[DECISION-021]]
  et la capacité `LEAC_PIECES_JOINTES`, toujours éteinte) — un vocal qui ne
  sort pas de la tablette ne la pose pas.
- **Transcrire les vocaux** : rien sur le serveur ne sait le faire ; un vocal
  se réécoute, il ne se lit pas.
- Garder la grille en premier et ajouter un onglet « notes » : c'est l'ordre
  qui était faux, pas la présence de la grille.

## Conséquences / à respecter
- ⚠ **Le carnet est la seule copie** : une note prise sur la tablette du matin
  n'est pas sur le téléphone du soir, et perdre l'appareil, c'est perdre le
  carnet. **L'écran le dit** — ce n'est pas une propriété à découvrir.
- ⚠ Aucun module de `sync/` ne doit jamais lire cette table.
- Les **mentions**, elles, se synchronisent : le carnet est le brouillon, la
  grille est la copie.
- Voir [[LESSON-041]] : une donnée qui n'existe que sur l'appareil impose de
  demander la **persistance du stockage**.

## 🔗 Source de vérité
Détail complet : voir `source:` (Règle 29) et `LEAC/JOURNAL.md` du 2026-09-22.
**Cette note ne recopie pas — elle pointe.**
