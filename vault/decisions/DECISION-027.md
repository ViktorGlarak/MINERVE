---
id: DECISION-027
aliases: ["DECISION-027"]
type: decision
title: LEAC — Keycloak dit QUI VOUS ÊTES, LEAC dit CE QUE VOUS AVEZ LE DROIT D'Y FAIRE
tags: [leac, pleiade, keycloak, habilitation, architecture, securite]
source: ../../LEAC/MEMOIRE.md
linkedTo: [DECISION-026, ARCH-014, LESSON-036]
relevantFor: [leac, pleiade]
tier: 1
created: 2026-09-18
updated: 2026-09-18
---

# DECISION-027 — L'administration appartient à LEAC, pas à Keycloak

## Contexte / problème
Il fallait cloisonner : un administrateur crée des contrôles et voit tout, un
contrôleur n'entre que dans les contrôles où il est affecté et n'ouvre que ses
grilles. Premier réflexe : un rôle Keycloak `admin`. **Repris par l'utilisateur**
le 2026-09-18 : *« Axel ne doit pas être admin “sur” Keycloak, il doit être admin
“sur” LEAC »*.

## Décision
- **Pléiade / Keycloak** répond à *qui êtes-vous ?* — compte de zone, identité.
- **LEAC** répond à *qu'avez-vous le droit d'y faire ?* — table
  `administrateurs_entite` dans la base `leac`, et fonction dans un contrôle
  (`membres_equipe`) qui décide **quelles grilles s'ouvrent**.
- Amorçage par `LEAC_ADMINISTRATEURS` (variable d'instance, valeur par défaut
  de l'image) : elle **inscrit**, ne révoque jamais ; le dernier administrateur
  ne peut pas être révoqué.

## Pourquoi (alternatives écartées)
- Rôle Keycloak : Pléiade attribue les rôles **par groupe** alors que c'est
  nominatif ; un rôle de royaume **suit la personne dans toutes les apps** ; deux
  endroits où la même vérité s'écrit = deux vérités.
- Ne rien enregistrer (« tout le monde admin ») : impossible dès qu'un
  contrôleur ne doit pas voir les autres contrôles.

## Conséquences / à respecter
- Le cloisonnement **se rejoue côté serveur** (`/api/sync`, actions serveur) :
  un garde d'affichage ne protège rien. **404, jamais 403.**
- Une fonction **inconnue** n'ouvre **que les transverses** — se tromper doit fermer.
- Les comptes de la zone se **choisissent** (route de service sans mot de
  passe), l'identité choisie est relue auprès de Pléiade côté serveur.
- Ne pas retirer le bloc `roles:` du catalogue sans le vouloir (cf.
  [[LESSON-036]]).

## 🔗 Source de vérité
Détail complet : voir `source:` ci-dessus (Règle 24). **Cette note ne recopie pas — elle pointe.**
