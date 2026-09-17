---
id: ARCH-013
aliases: ["ARCH-013"]
type: architecture
title: Une zone PLEIADE — 11 dépôts, 1 app = 1 dépôt, et 4 mécanismes qui les font parler
tags: [pleiade, architecture, zones, eho, keycloak, depots]
source: ../../PLEIADE/MEMOIRE.md
linkedTo: [ARCH-012, DECISION-013, DECISION-014, DECISION-017]
relevantFor: [pleiade, mastorion, exercices]
tier: 1
created: 2026-09-16
updated: 2026-09-16
---

# ARCH-013 — Comment une zone d'exercice est découpée, et comment ses apps se parlent

## Le découpage : 1 app du catalogue = 1 dépôt

L'organisation GitHub `cecpc-pleiade` compte **11 dépôts** : deux briques de
plateforme (`pleiade-platform` l'orchestrateur, `pleiade-infra` l'infra), **les
8 apps du catalogue** — `eho`, `app-social`, `app-admin`, `app-cockpit`,
`app-press`, `app-messagerie`, `app-webserver`, `app-wordpress` — et `mastorion`,
**ancêtre figé** du réseau social.

⚠ **`app-social` contient tout `mastorion` plus 19 commits** : le renommage
annoncé dans [[DECISION-014]] a eu lieu. Travailler dans `app-social`.

⭐ **L'admin embarquée dans mastorion a été démantelée** : les comptes sont
partis chez **eho**, les scénarios chez **app-admin**, la veille chez
**app-cockpit**, les rôles chez **Keycloak**. Il ne reste au social qu'un seul
rôle, `animateur`. C'est l'aboutissement de [[DECISION-013]].

## Les 4 mécanismes (le modèle à avoir en tête)

1. **L'identité est UNE et vient d'eho.** `identity_id` = UUID eho = `sub`
   Keycloak, **identique sur toutes les apps**. Une app ne stocke pas de
   comptes. ⚠ Un persona reçoit un `user.id` **différent dans chaque instance**
   sociale : seul `identity_id` fait le pont — **sans lui, aucune vue transverse
   n'existe**.
2. **Découverte à l'exécution**, jamais en dur : chaque app interroge
   l'orchestrateur pour connaître ses voisines, et **conserve la dernière liste
   si celui-ci tombe** (application de [[LESSON-032]]).
3. **Clé de service de la zone** (`X-API-Key`) pour l'app-à-app — *parce que
   personne n'est en ligne quand le scheduler publie à T+37 min*. La session de
   l'opérateur ne sert alors qu'à signer le journal.
4. **Contrat `/api/service/*` identique** sur social, presse et messagerie :
   `app-admin` vise n'importe quelle app **sans rien savoir d'elle**. Un item de
   scénario cible **une instance**, jamais un type de réseau.

## Ce que ça implique pour nous
👉 **eho n'est pas une app parmi d'autres : c'est la source d'identité de toute
la zone.** Tout travail dessus engage la presse, la messagerie, le cockpit et
les scénarios.

## 🔗 Source de vérité
Détail complet — tableau des dépôts, rôles Keycloak par app, design system,
conventions de code : `PLEIADE/MEMOIRE.md` §2 et §6bis. **Cette note pointe, elle
ne recopie pas.**
