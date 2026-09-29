---
id: DECISION-036
aliases: ["DECISION-036"]
type: decision
title: LEAC — quatre PROFILS permanents (utilisateur, superviseur, officier de marque, administrateur)
tags: [leac, droits, profils, habilitation]
source: ../../LEAC/MEMOIRE.md
linkedTo: []
relevantFor: [leac]
tier: 1
created: 2026-09-25
updated: 2026-09-25
---

# DECISION-036 — Quatre profils permanents, en plus de la fonction tenue dans chaque contrôle

## Contexte / problème
Remarque recueillie par l'utilisateur auprès du client, le 2026-09-24 :
- **superviseur** : accès à tous les contrôles, toutes les notes, tous les labels et comptes rendus, et au tableau de bord avec ses indicateurs ;
- **utilisateur** : réalise un contrôle en tant que contrôleur quand il y est désigné, et n'a accès qu'à ce contrôle ;
- **officier de marque** : crée des contrôles, avec en plus les droits du superviseur et de l'utilisateur ;
- **administrateur** : crée des comptes et des profils, peut corriger après coup, et accède au paramétrage (grilles, régiments, brigades).

LEAC n'avait qu'**un** profil permanent (administrateur). Tout le reste venait de la **fonction** tenue dans un contrôle.

## Décision
- La colonne **`AdministrateurEntite.profil`** prend les valeurs `SUPERVISEUR`, `OFFICIER_DE_MARQUE` ou `ADMINISTRATEUR`. Sa valeur par défaut est `ADMINISTRATEUR` : les lignes existantes restent des administrateurs. **Pas de ligne = UTILISATEUR.**
- **Une seule table de correspondance** (`lib/controle/profils.ts`, `droitsDuProfil`), avec trois droits :
  - `voitTout` : superviseur et au-delà ;
  - `peutCreerControle` : officier de marque et au-delà ;
  - `estAdministrateur`.
- **Superviseur** : tous les contrôles **officiels**, toutes les grilles en **lecture** (tableau de bord, compte rendu, comparaison compris). Il écrit seulement si sa fonction dans l'équipe le permet. Le serveur refuse ses écritures, car il est un « auteur inconnu » s'il n'est pas de l'équipe.
- **Officier de marque** : crée un contrôle et en devient d'office l'officier de marque (fonction principale), donc il le paramètre.
- **Administrateur** : profils, unités, grilles, et **« Rouvrir pour correction »** d'un contrôle clos.
  - Le contrôle repasse en `COMPTE_RENDU`.
  - Un motif est obligatoire.
  - Le résultat annoncé est inscrit au journal (`controle.reouverture`) avant d'être libéré. Une nouvelle clôture fige le résultat corrigé.
- **Le profil se cumule avec la fonction.** L'**auto-évaluation reste étanche** : aucun profil n'y entre sans être de l'équipe.

## Ce qui reste hors de LEAC
**Créer les comptes** : c'est Pléiade qui les crée (identité de zone, règle 24). LEAC attribue les profils.
✅ **Tranché par l'utilisateur le 2026-09-25** : l'administrateur LEAC **ne crée pas** de comptes. On garde le fonctionnement actuel : les comptes se créent dans Pléiade (« ça fonctionne très bien »). Ne pas le reproposer.

## Vérifié (2026-09-25, en local, 4 profils)

| Profil | Contrôles visibles | Grilles | Administration |
|---|---|---|---|
| Administrateur | 3 | — | 5 entrées, 9 écrans : 200 |
| Superviseur | 3 | 14/14 en lecture | comparer seulement |
| Officier de marque | 3 | lecture | + créer : a créé un contrôle, puis paramétrage OK |
| Utilisateur | 1 (le sien) | 3 | tout en 404 ; un autre contrôle : 404 |

Correction après clôture : `CLOTURE` → `COMPTE_RENDU`, journal avec motif et « B · validé · 7,5 ».
