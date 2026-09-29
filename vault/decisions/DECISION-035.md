---
id: DECISION-035
aliases: ["DECISION-035"]
type: decision
title: MELMIL est un document d'animation — le rôle du bouclier conditionne l'accès, pas la discrétion de la carte
tags: [melmil, pleiade, keycloak, habilitations, cloisonnement, exercices, influence]
source: ../../PLEIADE/JOURNAL.md
linkedTo: [DECISION-033, LESSON-042, DECISION-031, ARCH-013]
relevantFor: [pleiade, melmil, exercices, delattre]
tier: 1
created: 2026-09-23
updated: 2026-09-23
---

# DECISION-035 — Une planche d'injects ne se montre pas à ceux qui la subissent

## Contexte / problème
Mise à disposition de MELMIL sur le serveur, avec une consigne explicite de
l'utilisateur : seuls les **groupes d'animation** doivent y accéder, *« car si
les joueurs ont accès à cette application ils peuvent voir le déroulé et le
montage de l'exercice pour la partie Influence »*.

Or le catalogue de MELMIL déclarait **`roles: []`** — hérité du premier essai,
justifié alors par « l'état vit dans le navigateur, rien n'est partagé, donc
rien à protéger ». Le raisonnement portait sur les **données saisies** et
oubliait le **contenu affiché** : la planche montre le montage de l'exercice,
incident par incident, avec dates, heures, émetteurs et destinataires.

Sans rôle déclaré, **rien à cocher sur le bouclier**, et **tout compte du
royaume** — donc tout entraîné — entrait.

## Décision
1. Le catalogue déclare le rôle **`admin`** (libellé « Animation »), qui
   devient cochable groupe par groupe sur le **bouclier de l'instance**.
2. **MELMIL refuse côté serveur** quiconque ne le porte pas : le sas pose deux
   questions, « qui êtes-vous » puis « avez-vous le droit d'être ici ». Sans le
   rôle, la planche n'est pas masquée, elle **n'est jamais rendue**.
3. Le refus est **expliqué** et nomme l'endroit où le rôle se donne — un
   « accès refusé » sec fait chercher une panne, et finit par faire ouvrir
   l'accès à tout le monde pour s'en débarrasser.

## Pourquoi (alternatives écartées)
- **Compter sur la discrétion de la carte** : impossible, le portail de zone
  est public ([[LESSON-042]]).
- **Tenir une liste d'autorisés dans MELMIL** : une seconde vérité finirait par
  contredire le bouclier. Même raison que pour les fonctions de LEAC.
- **Un rôle nommé `animateur`** : `admin` est ce que le bouclier présente déjà
  pour les autres apps ; l'utilisateur raisonne en « groupes cochés admin ».

## Conséquences / à respecter
- ⚠ **Ne cocher QUE les groupes d'animation.** Un groupe d'entraînés coché voit
  tout le montage — c'est l'exercice qui est éventé, pas seulement une page.
- ⚠ Le rôle est **lu à la connexion** : cocher un groupe ne vaut qu'à la
  connexion suivante de ses membres.
- ⚠ Le nom du rôle doit rester **identique** entre `catalog/melmil.yml` et
  `src/lib/zone/habilitation.ts` — le changer d'un seul côté ferme l'app à tous.
- ⭐ Règle générale à retenir : **ce qu'une app AFFICHE peut être sensible même
  quand elle n'enregistre rien.** « Pas de données partagées » ne vaut pas
  « rien à protéger ».

## 🔗 Source de vérité
Détail complet : `source:` (2026-09-23) et `app-melmil/README.md`.
**Cette note ne recopie pas — elle pointe.**
