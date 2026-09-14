---
id: LESSON-032
aliases: ["LESSON-032"]
type: lesson
title: Un échec de lecture ne doit jamais être présenté comme un résultat valide
tags: [eho, pleiade, securite, ux, piege, keycloak]
source: ../../PLEIADE/MEMOIRE.md
linkedTo: [DECISION-016, LESSON-030, ARCH-012]
relevantFor: [pleiade, mastorion, outillage]
tier: 1
created: 2026-09-14
updated: 2026-09-14
---

# LESSON-032 — Un échec de lecture n'est pas un résultat

## Ce qui s'est passé
Deux incidents le même jour, de la même famille, tous deux remontés par
l'utilisateur et tous deux **invisibles depuis le code** :

1. Le rafraîchissement d'un jeton Keycloak échoue → l'authentification **vide
   les rôles** par précaution. La barre de navigation en a déduit « pas admin,
   donc joueur » et a replié le menu **sans rien dire**. L'utilisateur, à qui
   l'interface annonçait une session joueur, a travaillé pendant une demi-heure
   sous son compte d'animateur.
2. La lecture du package STARTEX renvoie **401** (session expirée) ; le code
   traitait cet échec comme **un package vide**. Les 62 étoiles ont disparu de
   l'écran, et le calcul d'écart concluait « rien à enregistrer ».

Aucune donnée n'a été perdue dans les deux cas. Mais dans le second, un
enchaînement inverse — lecture réussie *puis* sélection perdue — aurait
réellement envoyé le retrait des 62 autorités.

## La règle
**Lever, afficher, désactiver l'action — mais ne jamais rendre « vide », « zéro »
ou « sans rôle » ce qu'on n'a pas pu lire.** Un ensemble vide et un échec de
lecture se ressemblent dans le code et n'ont rien à voir pour l'utilisateur.

Trois corollaires appliqués dans l'EHO :
- une action reste **désactivée** tant que l'état dont elle dépend n'est pas
  réellement connu ;
- une **action destructive se calcule sur l'état RELU du serveur**, jamais sur
  une copie locale qui a pu vieillir (session expirée, rechargement à chaud,
  autre opérateur) ;
- un volume de destruction anormal (ici : la moitié du package) **demande
  confirmation**, en disant à l'utilisateur ce qu'il est probablement en train
  de subir plutôt que de vouloir.

## À retenir au-delà de l'EHO
Voir aussi [[LESSON-030]] — supposer un nom de champ d'API avant une suppression
de masse. Même famille : **l'outil se tait, l'utilisateur paie**.

⚠ Pièges d'environnement de la même séance, à ne pas réapprendre :
**après `prisma generate`, redémarrer le serveur de dev** (il garde l'ancien
client, les écritures échouent en 500), et **toujours contrôler le code HTTP**
dans un script d'essai — un script qui parse la réponse sans regarder le statut
avale les 500 et fait croire que tout fonctionne.
