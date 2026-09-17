---
id: ARCH-014
aliases: ["ARCH-014"]
type: architecture
title: LEAC v3 — journal d'opérations et horloge de Lamport remplacent le PC maître, la clé USB et la réplication MariaDB
tags: [leac, pleiade, synchronisation, hors-ligne, tablette, crdt]
source: ../../LEAC/MEMOIRE.md
linkedTo: [ARCH-013, DECISION-021, DECISION-022, LESSON-034]
relevantFor: [leac, pleiade]
tier: 1
created: 2026-09-17
updated: 2026-09-17
---

# ARCH-014 — Comment LEAC concatène le travail de contrôleurs qui ne se voient jamais

## Le problème posé par la v2.5
Le memento utilisateur v2.5 § V.B.8 avertit noir sur blanc : *« toute
modification effectuée durant la synchronisation sera perdue. »* Le dispositif
imposait un **hub réseau**, **16 postes en IP fixes**, un **« PC maître »**, des
**fichiers JSON sur clé USB** et une **réplication MariaDB multi-maître**.

⚠ **Les 5 « erreurs récurrentes » du memento (§ V.D) venaient TOUTES de ce
dispositif, aucune du métier** — dont une **apostrophe** dans une grille qui
cassait la synchronisation (SQL concaténé). Elles occupaient un cinquième du
memento.

## Le mécanisme retenu en v3
**Une saisie n'écrit pas une ligne : elle ajoute un ÉVÉNEMENT daté**
`(cible, champ, valeur, auteur, horloge)`.

- **Horloge de Lamport** persistée sur l'appareil — elle ne recule jamais, et
  s'aligne sur `max(locale, reçue)` à chaque synchronisation.
- **Ordre total déterministe** : horloge → appareil → identifiant d'opération.
  Les deux côtés (tablette et serveur) aboutissent au **même état** sans se
  parler.
- Les opérations **perdantes sont conservées** avec un `motifRejet` : rien n'est
  effacé, la revue de synchronisation les montre.
- Une **vraie collision** n'existe qu'entre **deux auteurs différents** sur la
  même cible.

## Ce que ça supprime
Plus de PC maître, plus de clé USB, plus d'IP fixes, plus de SQL concaténé —
donc plus l'apostrophe qui cassait tout. Et surtout : **on écrit PENDANT la
synchronisation**, ce que la v2.5 interdisait.

## Conséquences / à respecter
- ⚠ **Un seul chemin d'écriture** : `src/lib/offline/depot.ts`. Une écriture qui
  contournerait le journal s'afficherait correctement sur la tablette et
  **disparaîtrait à la synchronisation** — la perte silencieuse que la v3 doit
  rendre impossible.
- L'écriture du journal et celle de l'état dérivé sont dans la **même
  transaction** : une tablette éteinte au mauvais moment ne peut pas garder une
  valeur affichée sans l'opération qui la porte.
- Une opération n'est marquée « remontée » qu'**après accusé du serveur**. Dans
  le doute on renvoie — le serveur déduplique sur l'identifiant d'opération.
- La granularité d'écriture est un sujet à part entière → [[DECISION-021]].

## 🔗 Source de vérité
Détail complet : voir `source:` ci-dessus. **Cette note ne recopie pas — elle pointe.**
