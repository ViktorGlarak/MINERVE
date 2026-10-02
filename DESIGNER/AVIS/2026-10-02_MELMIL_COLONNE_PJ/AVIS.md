# Avis DESIGNER n°24 — MELMIL : une colonne « Pièces jointes » (fichiers et comptes rendus)

**Date** : 2026-10-02 · **App** : `app-melmil`, tableau des incidents (onglet Incidents) et cartes de la planche.
**Constat de l'utilisateur** : un compte rendu qu'on vient de créer n'apparaissait pas dans la colonne « CR ». C'était un défaut : la colonne ne comptait que les anciens comptes rendus propres à un incident, pas les comptes rendus **partagés** par jour et par ETIM.
**Décision de l'utilisateur** : « un CR est considéré comme une pièce jointe ». La colonne doit donc signaler le nombre de pièces jointes de l'incident, comptes rendus compris.

## Recommandations retenues

| # | Recommandation | Source |
|---|---|---|
| R1 | **Une seule indication par ligne** : la colonne « CR » devient la colonne « Pièces jointes », et l'agrafe ajoutée après le sujet quitte le tableau. Afficher deux fois le même nombre sur une ligne oblige à se demander s'ils diffèrent. | limiter le bruit (REF-07), Hick (REF-06) |
| R2 | **L'en-tête est l'agrafe**, la même forme que dans les cellules et sur les cartes. Son nom complet (« Pièces jointes (fichiers et comptes rendus) ») est donné au lecteur d'écran et à l'infobulle. | cohérence (Jakob, REF-06) ; REF-13 1.1.1 |
| R3 | **Même règle d'affichage partout** : l'agrafe seule pour 1, l'agrafe et le nombre à partir de 2, rien pour 0. | avis n°23 |
| R4 | **Le détail au survol** : « 2 pièces jointes : 1 fichier et 1 compte rendu ». La cellule reste sobre, et l'information complète est à un survol, lue aussi par les lecteurs d'écran. | « mettre en valeur en atténuant le reste » (REF-07) |
| R5 | **Un seul calcul** pour le tableau et la planche (`piecesDeLIncident`) : fichiers, comptes rendus partagés de son jour et de ses ETIM (chaque exemplaire « +1 » compte) et anciens comptes rendus. Les deux vues ne peuvent pas se contredire. | état du système fiable (Nielsen 1, REF-14) |
| R6 | **Visible sur téléphone** : en vue cartes, l'indication passe sous le statut au lieu d'être masquée comme l'ancienne colonne « CR ». | REF-13 1.4.10 |

## Vérification (en local, atelier fictif)
- Création d'un PSYREP sur 08.01.I04, qui n'avait aucune pièce jointe : **la colonne affiche aussitôt l'agrafe**, avec « 1 pièce jointe : 1 compte rendu », et la carte de la planche suit.
- 08.01.I01, avec 1 fichier et 1 compte rendu partagé, affiche « 2 ».
- Captures : `avant_creation_cr.png`, `apres_creation_cr.png`.
