---
id: DECISION-025
aliases: ["DECISION-025"]
type: decision
title: LEAC — on pose une MENTION et on enregistre le MOT, jamais le chiffre
tags: [leac, metier, notation, antares, n4]
source: ../../LEAC/MEMOIRE.md
linkedTo: [DECISION-024, DECISION-026, LESSON-034, ARCH-014]
relevantFor: [leac]
tier: 1
created: 2026-09-17
updated: 2026-09-17
---

# DECISION-025 — Le contrôleur choisit un mot, pas une note

## Contexte / problème
La méthode ANTARES N4 l'écrit : *« comme la note n'est pas visible, on empêche
les chiffres de guider le contrôleur »*. Et le cours du CBA Rubben : *« les notes
ne sont pas communiquées, seul le niveau est révélé »*.

L'écran de notation que j'avais écrit affichait une **échelle chiffrée**. Il
contredisait frontalement la méthode.

## Décision
- Le contrôleur choisit une **mention** — *Exceptionnel, Remarquable, Très
  satisfaisant, Satisfaisant, Moyen, Insuffisant, Défaillant, Mauvais esprit*.
- ⭐⭐ **Le journal enregistre le MOT, jamais le chiffre.**

## Pourquoi (alternatives écartées)
Enregistrer la valeur numérique était le réflexe, et c'est faux ici :
**l'échelle est en cours de recalibration** (« Remarquable » passe de 4,5 à
4,75). Un journal rempli de nombres aurait perdu ce que le contrôleur voulait
dire, et tout l'historique serait à relire à la main. Le mot survit à la
recalibration : on recalcule un contrôle de juin avec le barème de juin.

## Conséquences / à respecter
- ⚠ **Un mot retiré de l'échelle ne vaut pas zéro** : il ne compte pas, **et il
  est signalé**. « Bien » existait en juillet, plus en septembre ; le compter
  zéro effondrerait la moyenne d'un domaine sans bruit.
- ⚠ **Où le chiffre a le droit d'apparaître** : sur le tableau de bord de
  l'équipe de contrôle — c'est son outil de travail, et le classeur du CECPC y
  affiche des moyennes. **Jamais** sur l'écran de notation, **jamais** dans le
  compte rendu remis à l'unité, qui reçoit un **niveau** et un **label**.
- La conversion mot → chiffre se fait en **un seul endroit par écran**, pour
  qu'on puisse dire où la note apparaît — et donc garantir qu'elle n'apparaît
  pas ailleurs.
- ⚠ Échelle **à faire confirmer** : le haut passe au quart de point, ce qui
  **remonte mécaniquement les moyennes**. Une grille tout « Remarquable » passe
  du niveau 4 au niveau 5. Signalé au CECPC, maintenu sur sa décision.

## 🔗 Source de vérité
Détail complet : voir `source:` ci-dessus. **Cette note ne recopie pas — elle pointe.**
