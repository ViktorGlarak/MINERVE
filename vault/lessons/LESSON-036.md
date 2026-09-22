---
id: LESSON-036
aliases: ["LESSON-036"]
type: lesson
title: Retirer un rôle du catalogue Pléiade le SUPPRIME de Keycloak — le déclaratif efface, il n'ignore pas
tags: [leac, pleiade, keycloak, catalogue, deploiement]
source: ../../LEAC/JOURNAL.md
relevantFor: [leac, pleiade, mastorion]
linkedTo: [DECISION-027, LESSON-035]
tier: 2
created: 2026-09-18
updated: 2026-09-18
---

# LESSON-036 — Un catalogue déclaratif efface ce qu'on cesse d'y écrire

## Ce qui s'est passé
En rendant l'administration à LEAC ([[DECISION-027]]), le rôle Keycloak `admin`
de `catalog/leac.yml` devenait inutile. Premier mouvement : le retirer du
catalogue. Relecture de `ensureClientRoles` dans `pleiade-platform` : **tout
rôle absent du catalogue est supprimé du client Keycloak** à la promotion
suivante — avec ses attributions, dans une zone que Xavier administre.

## Leçon
Dans Pléiade, le catalogue n'est pas une liste d'ajouts : c'est **l'état
voulu**. Ce qu'on n'y écrit plus **disparaît**. Avant de retirer une ligne
(rôle, variable, chemin), lire la réconciliation qui la consomme et se demander
ce qu'elle détruit.

## Appliqué
Le rôle `admin` est **conservé, marqué obsolète et inerte** ; à retirer un jour
**délibérément**, pas au passage. Même prudence pour les variables d'instance :
le `.env` n'est généré qu'à la création, seules les `PLEIADE_*` sont repatchées
— d'où la valeur par défaut posée dans l'image (`ENV LEAC_ADMINISTRATEURS`).
