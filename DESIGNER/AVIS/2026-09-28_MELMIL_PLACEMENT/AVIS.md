# Avis DESIGNER n°12 — MELMIL, organigramme : placer les groupes reliés côte à côte

> **Date** : 2026-09-28 (soir) · **Suite des avis n°10 et n°11**, après les liaisons faites par l'utilisateur sur ses vraies données. L'assistant ne les a pas lues : elles sont confidentielles ; l'essai s'est fait sur une structure fictive du même genre.

## Remarques de l'utilisateur
1. Dans HOSTNATION, « Aucune personne » est écrit : **ça ne sert à rien**.
2. Les groupes reliés doivent **changer de place**, pour que ce soit plus harmonieux et logique : rangés par ordre alphabétique, les pointillés traversaient l'organigramme.

## Solution retenue

**R1 · Supprimer l'information vide** *(règle 5 : mettre en valeur en atténuant ; heuristique 8 : minimalisme)* : le « 0 » de l'en-tête dit déjà qu'il n'y a personne en direct, et les sous-groupes montrent où sont les gens.

**R2 · La proximité suit la relation** *(loi de proximité, règle 9 ; Gestalt)* : deux groupes qui travaillent ensemble sont dessinés côte à côte.
- **Les colonnes** : une chaîne par famille de groupes reliés. On part de la colonne la plus liée, et chaque nouvelle colonne s'accroche au bout de la chaîne avec lequel elle est le plus liée. Les colonnes sans aucun lien viennent ensuite, par nom.
- **Les sous-groupes** : celui qui est relié à une colonne de gauche passe à gauche, celui qui est relié à droite passe à droite. Le pointillé part donc du côté de son partenaire.

**R3 · Un placement stable** *(heuristique 4 : constance)* : le calcul est déterministe. La même équipe donne le même dessin sur tous les postes, et rien ne bouge tant que les liens ne changent pas.

## Vérifié (structure fictive, en local)
Liens DEV / PROD ↔ FORAD et HN BOTHNIA ↔ ILI : FORAD vient à côté de GREYCELL, HN BOTHNIA passe du côté d'ILI, et les deux pointillés sont courts, sans croisement ; « Aucune personne » n'apparaît plus ; 0 erreur, 0 débordement.

## Pistes pour la suite
- Un ordre **choisi à la main** (flèches ← →, ou glisser une colonne), qui prime sur le calcul si l'utilisateur le souhaite.
- Un libellé sur le lien (« appui », « coordination »…).
