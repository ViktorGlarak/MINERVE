---
id: LESSON-037
aliases: ["LESSON-037"]
type: lesson
title: Un indicateur doit mesurer EXACTEMENT ce qu'il prétend rapporter — deux fois le même jour
tags: [pleiade, eho, deploiement, sonde, methode, tests]
source: ../../PLEIADE/MEMOIRE.md
linkedTo: [DECISION-029, LESSON-038, LESSON-035]
relevantFor: [pleiade, leac, mastorion, noyau]
tier: 1
created: 2026-09-21
updated: 2026-09-21
---

# LESSON-037 — Mesurer la chose même, pas un effet de bord

## Ce qui s'est passé — deux fois, le 2026-09-21
1. **Un voyant qui annonçait faux.** Un indicateur « cecpc Connect » jugeait
   une zone sur **deux** pièces (le fournisseur d'identité **et** un groupe
   nommé `cecpc`), alors que le bouton qu'il prétendait décrire ne dépend que
   de la **première**. Une zone qui marchait passait pour cassée. Retiré à la
   demande de l'utilisateur, à juste titre.
2. **Une sonde de déploiement aveugle.** Pour savoir si une mise en production
   était en ligne, je comparais l'**empreinte des fichiers statiques** de la
   page de connexion. Trois mises en production successives ne touchaient que
   le **serveur** (entrypoint, dépôt de portraits, origine publique) : aucun
   fichier client ne changeait, l'empreinte restait identique — donc « pas
   déployé », trois fois de suite, à tort. Pendant ce temps l'utilisateur
   réessayait et me demandait *« peut-être pas la bonne version ? »*.

## Leçon
Un indicateur qui se trompe **coûte plus qu'il ne rapporte** : on va vérifier à
la main ce qu'il affirme, puis on cesse de le croire. Avant d'en poser un,
écrire la question à laquelle il répond, puis vérifier qu'il mesure **cette
question-là** et rien d'autre.

⚠ **Mes tests n'ont rien vu** : onze contrôles navigateur au vert pendant que
le voyant mentait. Ils vérifiaient que l'affichage suit l'API, jamais que
l'API dit vrai — **un simulacre ne peut pas contredire l'hypothèse qui l'a
écrit**. Ce qui tranche, c'est une mesure contre le **vrai système** (ici :
une requête sur le Keycloak réel, une sonde sur l'instance réelle).

## Appliqué
- eho reçoit `/api/sante` → `{ version }` et `lib/version.ts`, comme LEAC :
  une **marque posée par le code**, à incrémenter à chaque push sur `prod`.
- Les deux guetteurs par empreinte ont été arrêtés le 2026-09-22.
- Règle générale : une sonde de déploiement lit une marque de version, jamais
  un effet de bord.
