# Avis DESIGNER n°5 — eho, écran « Avatars » : défilement, préchargement, retour à l'état initial

> **Date** : 2026-09-25 · **Demande de l'utilisateur** :
> 1. voir les **images** et les **fiches bio complètes** des cartes affichées, grâce à un **préchargement** qui ne fait pas planter l'application ;
> 2. un moyen de **refermer** ce qu'on a déplié avec « Afficher 60 de plus », pour revenir à l'affichage de départ ;
> 3. **faire défiler** plutôt que cliquer, pour charger petit à petit **sans agrandir la fenêtre**.
>
> Contexte : DE LATTRE 26, ≈ 3 500 avatars (version en ligne `2026-09-24.2`).

## 1. Le constat

- Un bloc de fonction (ex. « ARN — Citoyen », 139 cartes) **grandit à chaque « Afficher plus »**. La page s'allonge, on perd le pays suivant, et aucun geste ne ramène à l'état de départ *(Nielsen 3, contrôle et liberté)*.
- La carte ne porte qu'un **résumé**. La fiche complète (bio, état civil, observations) est demandée **au clic**. Sur un réseau lent, la fiche s'ouvre sur « Chargement… », et si la requête échoue, elle y **reste**. C'est un défaut *(Nielsen 1, état du système ; Doherty, réponse en moins de 400 ms)*.

## 2. La solution retenue

**R1 · Chaque gros bloc devient un « rail » à hauteur bornée, qui défile en lui-même.**
- Au-delà de deux rangées de cartes, le bloc garde une **hauteur fixe** : environ 3 rangées sur ordinateur, `min(60vh, 34rem)`, et 60 % de la hauteur d'écran au téléphone. On y **fait défiler** les cartes. La page ne grandit plus, et le pays suivant reste à sa place.
- **Chargement au défilement** : un repère invisible, placé avant la fin du rail, déclenche la tranche suivante (60 cartes) **avant** qu'on arrive au bout. C'est le préchargement : on ne voit jamais le vide.
- `overscroll-behavior: contain` : arrivé en bas du rail, le doigt ne fait pas défiler la page par surprise. Un **dégradé** en bas du rail signale qu'il y a une suite *(REF-07 : montrer l'affordance plutôt que l'écrire)*.
- ⚠ Les **petits blocs** (moins de deux rangées) restent tels quels : un rail pour 8 cartes serait une complication gratuite *(Hick)*.

**R2 · Un compteur et « Revenir au début » dans l'en-tête du bloc.**
- « 180 / 480 affichés · **Revenir au début** » : le bouton **décharge** les tranches supplémentaires (le navigateur récupère la mémoire) et remonte le rail. On retrouve l'affichage de départ en un geste *(Nielsen 3)*.
- Le compteur est annoncé aux lecteurs d'écran (`aria-live`).

**R3 · Des cartes COMPLÈTES dès leur arrivée : la fiche s'ouvre instantanément.**
- La tranche d'un bloc transporte **tout ce que montre la fiche** : bio, état civil, observations, source, groupes. C'est raisonnable, car ce sont 60 cartes à la fois, pas 3 500.
- La fiche s'ouvre donc **sans requête et sans attente**.
- Pour les résultats de **recherche** (jusqu'à 400), on garde des cartes légères. Leur fiche se **précharge au survol ou au focus**, et s'affiche en moins de 400 ms au clic. Si la requête échoue, la fiche le **dit** et propose de réessayer, au lieu de rester sur « Chargement… ».

**R4 · Des images qui ne bloquent rien.**
- `loading="lazy"` et `decoding="async"` sur les portraits, avec une taille fixe (pas de saut de mise en page).
- Le rail ne demande l'image qu'à l'approche de l'écran : 480 portraits chargés à l'avance feraient ramer une tablette.

**R5 · Responsive.**
- **Téléphone** : 2 cartes par rangée, rail à 60 % de la hauteur, pastilles pays collantes en haut (déjà en place).
- **Tablette** : 4 à 5 cartes.
- **Ordinateur** : 8 à 10 cartes.
- Le rail garde la même règle partout. Seule sa hauteur suit l'écran.

## 3. Ce qui n'est pas retenu, et pourquoi

- **Un défilement infini de la page entière** : il reprend le problème de départ. La page s'allonge sans fin et l'on perd ses repères *(Nielsen 6)*.
- **La virtualisation** (dessiner seulement les cartes visibles) : c'est efficace, mais elle ajoute une bibliothèque. Avec des tranches de 60 et un rail borné, l'écran reste fluide sans elle. **À reconsidérer** si un bloc dépasse ~1 500 cartes.

## 4. Critère de réussite

- Ouvrir un bloc de 480 cartes et le faire défiler jusqu'en bas sans gel perceptible (tâches longues < 200 ms en CPU ×4). « Revenir au début » ramène l'état initial.
- Une fiche ouverte depuis un bloc s'affiche **tout de suite**, bio comprise.
- Aucune page plus large que l'écran, sur téléphone, tablette et ordinateur.
