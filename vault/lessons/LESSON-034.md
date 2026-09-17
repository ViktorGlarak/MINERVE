---
id: LESSON-034
aliases: ["LESSON-034"]
type: lesson
title: « Pas de note » n'est pas « zéro » — la confusion est invisible à l'œil et fait déclarer un PC inapte
tags: [leac, metier, notation, tests, tableau-de-bord]
source: ../../LEAC/MEMOIRE.md
linkedTo: [ARCH-014, DECISION-022]
relevantFor: [leac]
tier: 2
created: 2026-09-17
updated: 2026-09-17
---

# LESSON-034 — L'absence de donnée n'est pas une valeur basse

## Symptôme observé
Règle du memento administrateur § VI.B.1 : *« la notation se fait uniquement par
les derniers sous-niveaux ; les niveaux supérieurs ne font que la moyenne des
niveaux inférieurs. »*

Si un nœud sans aucune feuille notée valait **0** au lieu de **rien**, le premier
matin d'un contrôle — une grille entamée sur six — le tableau de bord de la
réunion quotidienne annoncerait **« Inapte opérationnel »** à un PC dont personne
n'a encore rien vu. Et **personne ne le verrait** : la moyenne est un chiffre
plausible, pas un plantage.

## Cause racine
Trois endroits où `null` se transforme en `0` sans bruit :
1. la moyenne d'un nœud (moyenner sur **tous** les enfants au lieu des enfants
   **notés**) ;
2. la note finale (inclure une fonction non abordée dans la moyenne pondérée) ;
3. l'affichage (`note ?? 0` au lieu de `note === null ? "—" : …`).

Deux pièges voisins, de la même famille :
- ⚠ **La moyenne remonte par NIVEAU, jamais à plat** sur toutes les feuilles —
  sinon un sous-domaine à 3 critères pèse plus qu'un sous-domaine à 2.
- ⚠ **Le taux de remplissage se compte en POINTS**, pas en moyenne de taux : un
  domaine à 60 critères et un domaine à 6 ne représentent pas le même travail
  restant (60/60 + 0/6 fait **91 %**, pas 50 %).

## Correctif / règle à appliquer
- `null` traverse **toute** la chaîne de calcul jusqu'à l'affichage, où il
  devient « — ».
- Une fonction **non abordée** ou de **poids 0** est **exclue** de la moyenne
  pondérée — mais **reste affichée**, avec le **motif écrit en clair** :
  « pourquoi cette ligne n'est pas dans la moyenne » est exactement la question
  posée à voix haute en réunion.
- Un contrôle vierge rend note `null`, barème `null`, taux `0` — **jamais `NaN`**.
- ⭐ **Ces règles sont sous tests** (`scripts/test-domaine.mts`), parce qu'une
  moyenne fausse ne se voit pas à la relecture.
- Corollaire d'écran : afficher le **taux de remplissage AVANT la note**. Lire
  « 4,2 » sur 8 % de points saisis fait conclure qu'un PC est au niveau.

## 🔗 Source de vérité
Détail / trace : voir `source:`. **Pointeur, pas copie.**
