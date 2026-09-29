---
id: LESSON-042
aliases: ["LESSON-042"]
type: lesson
title: Le portail d'une zone est PUBLIC — cocher un groupe donne l'accès, décocher ne cache pas la carte
tags: [pleiade, portail, cloisonnement, habilitations, melmil, traefik]
source: ../../PLEIADE/MEMOIRE.md
linkedTo: [DECISION-035, ARCH-012, ARCH-013, LESSON-037]
relevantFor: [pleiade, melmil, leac, mastorion, exercices]
tier: 1
created: 2026-09-23
updated: 2026-09-23
---

# LESSON-042 — Ce que le bouclier fait, et ce qu'il ne fait pas

## Symptôme observé
Consigne reçue : *« cette application est visible dans le lien de l'instance,
uniquement pour les groupes cochés admin sur le bouclier »*. C'est ainsi qu'on
croit — raisonnablement — que le portail d'une zone se comporte.

**Il ne se comporte pas ainsi.** Lu dans `pleiade-platform/src/index.ts` :
le middleware qui sert `<zone>.<domaine>` est placé **avant** `requireAuth`, et
il affiche `getPortalData(zone)`, un `SELECT` de **toutes** les instances de la
zone. Donc **aucune authentification**, **aucun filtrage** : n'importe qui
atteignant l'adresse voit le nom et l'URL de chaque application déployée.

## Cause racine
Deux mécanismes distincts qu'on confond facilement :

| | ce que ça fait |
|---|---|
| **Bouclier de l'instance** | attribue un **rôle Keycloak** à un groupe → décide **qui entre dans l'app** |
| **Portail de zone** | **liste publique** des instances → décide de rien du tout |

Décocher un groupe **retire l'accès**. Cela **ne retire pas la carte**, et
l'adresse d'une instance est de toute façon devinable
(`<instance>.<zone>.<domaine>`).

## Correctif / règle à appliquer
1. ⭐ **La seule barrière qui tienne est dans l'application**, côté serveur.
   Une app dont le contenu est sensible **déclare un rôle** au catalogue et
   **refuse** qui ne le porte pas ([[DECISION-035]]).
2. Ne **jamais** promettre qu'une app « ne sera pas visible » parce qu'un
   groupe n'est pas coché : dire qu'elle ne sera pas **accessible**.
3. ⏳ Filtrer le portail supposerait de l'**authentifier** — changement de
   comportement pour **toutes** les zones et **toutes** les apps. À décider
   avec l'utilisateur et Xavier, pas à glisser dans une livraison.
4. ⚠ Corollaire de méthode, encore : **lire le code avant de confirmer un
   mécanisme**. La consigne décrivait un comportement plausible qui n'existait
   pas ; l'accepter aurait laissé le montage d'exercice ouvert aux entraînés.

## 🔗 Source de vérité
Détail : `source:` (§6, « Le PORTAIL d'une zone est PUBLIC »).
**Pointeur, pas copie.**
