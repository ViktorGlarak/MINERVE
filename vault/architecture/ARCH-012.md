---
id: ARCH-012
aliases: ["ARCH-012"]
type: architecture
title: PLEIADE — orchestrateur de zones d'exercice (instances, Keycloak, Traefik)
tags: [pleiade, architecture, zones, instances, keycloak, traefik, podman]
source: ../../PLEIADE/MEMOIRE.md
linkedTo: [DECISION-014, DECISION-015, LESSON-031]
relevantFor: [pleiade, mastorion, exercices]
tier: 1
created: 2026-09-11
updated: 2026-09-11
---

# ARCH-012 — Architecture du système PLEIADE

## En une phrase
Un **orchestrateur** déploie, dans des **zones** isolées (une par exercice), des
**instances** d'applications (réseau social, eho, WordPress, webserver), chacune
avec sa base, son client **Keycloak** et sa route **Traefik** — le tout sur un
serveur **Podman rootful** joint par **VPN**.

## Les 5 repères
1. **Zone** = un exercice : slug immuable + label + type (dev/prod) + **1 realm
   Keycloak** créé automatiquement.
2. **Instance** = une app dans une zone : compose **généré** depuis un template
   du catalogue, `.env` injecté, client Keycloak, route
   `{instance}.{zone}.mastorion.internal`.
3. **Nommage** : base `mast_{zone}_{instance}` · projet compose
   `zone-{zone}-{instance}` · conteneur `zone-{zone}-{instance}-app-1`.
4. **Keycloak, 2 URLs à ne pas confondre** : `KEYCLOAK_URL` (interne Docker,
   backend) vs `KEYCLOAK_PUBLIC_URL` (navigateur). Clients **public** (sans
   secret) ou **confidential** (secret + credentials admin).
5. **Catalogue = données** : ajouter une app déployable = déposer un YAML dans
   `pleiade-platform/catalog/`.

## Liaison inter-instances
Quand **eho et le réseau social coexistent** dans une zone, `EHO_URL` est injecté
dans le second, qui **résout ses comptes de scénario auprès de l'EHO** →
**l'EHO est la source d'identité des personas**, le réseau social le consommateur.

## ⚠ Production
Serveur Podman **rootful** : toujours `sudo`. Aucune action sur la prod sans
autorisation explicite. Les dépôts sont **partagés avec le développeur** :
jamais de commit/push sans demande.

## 🔗 Source de vérité
État durable : `PLEIADE/MEMOIRE.md` ; chronologie : `PLEIADE/JOURNAL.md`. **Pointeur, pas copie.**
