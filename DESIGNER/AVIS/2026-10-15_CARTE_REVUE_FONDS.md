# Avis DESIGNER n°112 — Revue de la carte des avatars, et fonds de carte réels

**Date** : 2026-10-15 · **Demandeur** : utilisateur (« analyser ce qu'on a fait, être sûr d'être sur la bonne piste ; pouvoir basculer entre plusieurs vues — routes, relief… — avec des données réelles ») · **Matière** : captures de la maquette (`dev\carte`), avis n°111 · **Mise en œuvre** : PLEIADE

## 1. Verdict : la piste est bonne
- **L'intention est tenue.** C'est une vue de situation lisible d'un coup d'œil : la population, ses camps, ce qui arrive aux villes. Le fond de nuit en nuée de points donne l'identité voulue, sans bruit.
- **Les choix structurants sont justes** :
  - le camp lu par la couleur **et** la forme ;
  - les liens à la demande ;
  - l'opinion en couche optionnelle, avec une légende à deux pôles écrits ;
  - la date des données toujours visible ;
  - le mode Animation séparé du mode Lecture, avec l'avertissement « document d'animation ».
- **Le pari géographique est le bon** : les villes en H sont placées sur les communes réelles. C'est cela qui ouvre la porte aux fonds réels.

## 2. Ce qui gêne déjà la lecture, par priorité

**P1, la lisibilité**
1. **Les villes denses sont illisibles à l'échelle régionale.** HNancy, HLaxou et HVandœuvre font 55 avatars dans un pouce carré : on ne peut ni compter ni voir le rapport des camps. → **Agrégats par ville en dessous du zoom 9** : un anneau par ville, partagé en secteurs rouge, bleu et cyan au prorata des camps, avec l'effectif au centre. Au-delà, les points individuels. C'est le passage classique de « l'ensemble » au « détail ».
2. **L'infobulle est en bas au centre**, loin du pointeur : l'œil fait l'aller-retour. → La placer **à côté du pointeur**.
3. **Le panneau de gauche est trop long en mode Animation** : outils, couches, filtres et légende font plus d'un écran. → **Des sections repliables** (Situation, Couches, Filtres), qui restent ouvertes d'une visite à l'autre, et la **légende en encart compact en bas à droite** de la carte, où on la cherche.

**P2, l'orientation**
4. **L'Est est un vide noir.** On ne sait pas où commence Mercure. → Un libellé discret « MERCURE », en petites capitales grises à 40 %, au-delà de la frontière orientale. Avec un fond réel, la frontière se voit d'elle-même.
5. **Les évacuations courtes se voient mal** (HToul vers HNancy fait 20 km). → Épaissir l'arc à l'arrivée et ajouter un point d'arrivée orangé.

**P3, plus tard**
6. Le **curseur de temps**, déjà prévu, pour rejouer la journée.
7. Une **échelle kilométrique**. Elle devient utile dès qu'on pose des zones avec un rayon en kilomètres.

## 3. Les fonds de carte réels : oui, avec quatre règles

### Les fonds proposés (sources testées depuis le poste)
| Fond | Source | Usage | Noms réels affichés |
|---|---|---|---|
| **Nuit (points)** — par défaut | maquette actuelle | identité, salle, projection | non : les noms en H |
| **Nuit avec routes** | CARTO *dark, sans libellés* | même esprit, avec le réseau routier réel | non |
| **Relief** | IGN, ombrage (estompage), posé sur la nuit | lire les vallées, les crêtes, les axes naturels (utile aux combats et au NRBC) | non |
| **Photos aériennes** | IGN, orthophotographies | voir le terrain réel d'une zone posée | non |
| **Plan** | IGN, Plan IGN v2 | routes, lieux-dits, détail | **oui** (« Nancy ») |
| **OpenStreetMap** | OSM | alternative au Plan | **oui** |

### Les quatre règles
1. **Un voile pour garder les données lisibles.** Les couleurs néon sont faites pour la nuit. Sur un fond clair (Plan, OSM, photos), un curseur « Assombrir le fond » (45 % par défaut) pose un voile nuit par-dessus les tuiles, et les points gardent leur contour sombre.
2. **Les noms réels contre la convention H.** Le Plan et OSM écrivent « Nancy », pas « HNancy ». C'est acceptable dans un **outil d'animation**, mais **pas en projection devant les joueurs**. La carte le signale (« ce fond affiche les noms réels : à ne pas projeter aux joueurs »), et les fonds **sans noms** (Nuit, Nuit avec routes, Relief, Photos) sont ceux recommandés en salle.
3. **L'attribution toujours visible**, obligation des licences : « © IGN – Géoplateforme », « © contributeurs OpenStreetMap », « © CARTO ».
4. **Le réseau de l'exercice.** Ces fonds sont chargés depuis Internet. Sur le réseau de la zone, sans accès à Internet, il faudra **télécharger à l'avance les tuiles de la zone d'exercice** (Lorraine, zooms 6 à 13), servies par l'application. Le fond « Nuit (points) » reste le **fond de secours** qui marche toujours.
   - **Remarque CYBERSECU** : chaque tuile demandée indique au serveur la zone regardée. C'est sans conséquence pour une maquette locale, mais un argument de plus pour un cache local en exercice.
   - La politique d'usage d'OSM interdit le téléchargement massif. Pour un cache, on prendra **l'IGN** (licence ouverte Etalab).

### La forme du sélecteur
- Un **sélecteur compact en haut à droite** de la carte, avec les six fonds en liste, chacun avec une vignette ou une icône.
- Le choix est mémorisé dans le navigateur.
- Le curseur « Assombrir le fond » n'apparaît que pour les fonds clairs.

## Doctrine
Un fond de carte sert les données, pas l'inverse : on garde la nuit par défaut, on offre le réel à la demande, et on ne montre jamais aux joueurs un nom réel que l'exercice remplace.
