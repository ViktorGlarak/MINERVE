---
id: DECISION-031
aliases: ["DECISION-031"]
type: decision
title: LEAC — le bouclier Pléiade INSCRIT un administrateur, il ne remplace pas le registre
tags: [leac, pleiade, keycloak, habilitations, administration]
source: ../../LEAC/MEMOIRE.md
linkedTo: [DECISION-027, LESSON-036, DECISION-029]
relevantFor: [leac, pleiade]
tier: 1
created: 2026-09-21
updated: 2026-09-21
---

# DECISION-031 — Deux sources d'administrateurs, une seule vérité

## Contexte / problème
Axel, membre d'un groupe **admin** sur Pléiade, était vu par LEAC comme un
simple utilisateur. Ce n'était pas un bug : la décision du 18/09
([[DECISION-027]]) avait rendu l'administration à LEAC — les administrateurs
sont des lignes en base (`administrateurs_entite`), amorcées par
`LEAC_ADMINISTRATEURS` ou promues à la main, et les rôles Pléiade étaient
ignorés. L'utilisateur a tranché : *« je veux que LEAC fonctionne également
avec le bouclier Pléiade, comme les autres applis »*.

## Décision
Le bouclier **inscrit**, il ne se substitue pas :
- un jeton portant le rôle `admin` (royaume ou client `leac`) fait **créer une
  ligne** d'administrateur (`promuPar` = bouclier, journal
  `administrateur.bouclier`), puis l'accès est accordé ;
- la **vérité reste dans LEAC** : le registre des administrateurs est toujours
  le même, il gagne une source d'alimentation ;
- LEAC **refuse de révoquer** une ligne posée par le bouclier — elle
  reviendrait à la connexion suivante. Ce droit-là se retire **dans Pléiade**.
  L'écran le dit (pastille « bouclier Pléiade », bouton désactivé).

## Pourquoi (alternatives écartées)
- Lire les rôles Pléiade **sans** inscrire : l'écran d'administration
  n'aurait pas su qui sont les administrateurs, et l'audit non plus.
- Revenir sur le 18/09 : la raison d'alors tient toujours — le contrôle
  fonctionne **hors ligne**, il lui faut son propre registre.

## Conséquences / à respecter
- ⚠ **Les rôles sont lus à la connexion** : un rôle donné après coup ne vaut
  qu'à la connexion suivante. Le dire à l'utilisateur (« déconnectez-vous puis
  reconnectez-vous »).
- ⚠ Le rôle Keycloak `admin` de `catalog/leac.yml` **n'est plus obsolète** :
  le retirer le supprimerait de Keycloak avec ses attributions ([[LESSON-036]]).
- ⚠ Pléiade écrit `LEAC_ADMINISTRATEURS=` **vide** à la création d'une
  instance, ce qui écrase la valeur posée dans l'image : l'amorçage seul ne
  suffit pas à garantir un premier administrateur.

## 🔗 Source de vérité
Détail complet : voir `source:` ci-dessus (Règle 24). **Cette note ne recopie pas — elle pointe.**
