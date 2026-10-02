# Avis DESIGNER n°23 — MELMIL : l'agrafe des pièces jointes

**Date** : 2026-10-02 · **App** : `app-melmil`, planche de préparation (cartes d'incident), tableau des incidents, liste par jour.
**Demande de l'utilisateur** : voir d'un coup d'œil qu'un incident a une ou plusieurs pièces jointes. Il veut une icône d'agrafe **en bas à droite de la carte** de l'incident sur la planche de préparation, avec le **nombre à partir de 2**. Il a demandé de consulter DESIGNER « pour faire quelque chose de propre et ergonomique ».

## Contraintes du terrain
- Les cartes d'incident de la planche sont **minuscules** : texte de 7,5 px, une colonne par jour d'environ 118 px. Chaque ligne en plus allonge tout le mur.
- Les cartes prennent la **couleur de leur storyline**, en style « Clair » et en style « Classique » (sombre). Une couleur fixe pour l'icône serait illisible sur une partie d'entre elles.
- MELMIL n'a pas de bibliothèque d'icônes (thème graphite / craie) : il faut une icône dessinée, sans dépendance.

## Recommandations retenues

| # | Recommandation | Source |
|---|---|---|
| R1 | **L'agrafe se cale en bas à droite, sur la dernière ligne de la carte**, celle des ETIM s'il y en a. La carte ne s'allonge pas. | proximité, densité (REF-07 Refactoring UI) |
| R2 | **Une seule forme, la même partout** : tableau des incidents (après le sujet), carte de la planche, liste par jour du téléphone. C'est un composant commun, `Agrafe`. | cohérence (Jakob, REF-06) |
| R3 | **Le nombre seulement à partir de 2** : l'agrafe seule dit « il y en a une ». Le chiffre est en gras, collé à l'icône. | demande utilisateur ; « mettre en valeur en atténuant le reste » (REF-07) |
| R4 | **Couleur héritée de la carte** (`currentColor`) : blanc sur les cartes sombres, foncé sur les claires. Elle est lisible sur toutes les storylines, et la couleur reste réservée à la storyline. | contraste 3 : 1 pour une icône (REF-13 1.4.11) |
| R5 | **Jamais l'icône seule** : « n pièces jointes » est lu par les lecteurs d'écran (texte masqué) et ajouté à l'infobulle de la carte. | information jamais portée par une icône seule (doctrine n°10, REF-13 1.1.1) |
| R6 | **Pas de cible cliquable à part** sur la carte : la carte entière ouvre déjà l'incident et ses pièces jointes. Un bouton de 9 px serait sous le minimum de 24 px. | taille des cibles (REF-13 2.5.8) |

## Vérification (en local, atelier fictif « EXERCICE DEMO AGRAFE »)
- Avec 1, 2, 3 puis 0 pièce jointe, on obtient l'agrafe seule, l'agrafe et « 2 », l'agrafe et « 3 », puis rien. C'est vérifié dans le tableau, sur les cartes de la planche (styles Clair et Classique) et dans la liste par jour au téléphone.
- Captures : `tableau.png`, `planche_clair.png`, `planche_classique.png`, `liste_telephone.png`.
