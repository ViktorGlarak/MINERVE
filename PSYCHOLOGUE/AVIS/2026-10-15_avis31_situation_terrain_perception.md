# Avis PSYCHOLOGUE n°31 et CYBERSECU — Situation terrain sur la carte : ce que perçoivent les civils

**Date** : 2026-10-15 · **Demandeur** : utilisateur (« placer de vraies actions sur le terrain avec de la symbologie militaire — une attaque NRBC ici, des combats là — et que ce soit repris automatiquement par le moteur IA ») · **Décisions utilisateur** : symbologie APP-6 (générée) et images fournies par l'utilisateur ; perception automatique selon la distance ; maquette locale qui produit un fichier, à déposer dans les Réglages du moteur. · **Mise en œuvre** : PLEIADE (`dev\carte`, `app-ia`)

## Principe
La carte devient l'outil de l'animation pour poser la **vérité du terrain** de l'exercice : des symboles militaires et des zones d'action. Le moteur n'en reçoit **que ce qu'un civil peut percevoir**. C'est de la fiction d'exercice : aucune unité, aucun lieu ni aucune donnée réels.

## Perception (PSYCHOLOGUE)
Un civil sait d'un événement militaire ce qu'il **vit**, ce qu'il **voit ou entend**, et ce qu'on lui **raconte**. Rien d'autre : il ignore les unités, leurs positions et les intentions.

| Distance de la ville à la zone | Ce qu'il vit | Effets dans le moteur |
|---|---|---|
| **Dans la zone** | l'événement lui-même | Événement de zone complet : choc d'humeur, activité, travail. Départs spontanés pour les combats, bombardements et attaques NRBC ; confinement « fenêtres fermées » pour le NRBC. |
| **À proximité** (rayon réglable par type) | ce qui se voit et s'entend : détonations, fumée, sirènes, colonnes de véhicules, odeur | Bloc « ce que tu as vu ou entendu », choc d'humeur ×0,4, inquiétude, envie d'en parler. **Pas** de décision de départ. |
| **Au-delà** | rien de direct | Il l'apprend seulement par le réseau social (annonces, messages lus), comme aujourd'hui. |

- **Rayons de proximité par défaut** (modifiables par action) : bombardement 15 km, combats 10 km, attaque NRBC 8 km (fumée, sirènes), zone contaminée 3 km, présence militaire visible 2 km. Les autres types : 5 km.
- **NRBC.** C'est la peur la plus forte et la plus diffuse : menace invisible, rumeurs, symptômes réels ou imaginés, ruée sur les pharmacies. Dans la zone : choc de −50, confinement « reste chez toi, fenêtres fermées, n'utilise pas l'eau du robinet », départ spontané pour les plus anxieux. À proximité : inquiétude marquée, et l'avatar demande ce qui se passe.
- **La perception se décrit avec les mots d'un civil**, écrits par l'animation pour chaque action. Par exemple : « fumée jaunâtre au-dessus de la zone industrielle, odeur âcre, des gens qui toussent ». Si l'animation n'écrit rien, une phrase type est utilisée selon le type, sans aucun détail militaire.

## Séparation (CYBERSECU)
1. **Ce que le moteur reçoit** : des événements de zone, c'est-à-dire un type, les villes touchées et les villes proches, des dates et une description civile. **Jamais** les symboles, leurs codes APP-6, l'identité ou l'échelon d'une unité, ni une position précise : seules des villes.
2. **La carte est un outil d'animation**, en local pour l'instant. Le fichier « situation » (symboles et zones) est un document d'animation : il ne va pas aux joueurs, et il se supprime en fin d'exercice comme les exports.
3. **Le passage au moteur** se fait par le réglage `evenements` existant : schéma fermé, journal, empreinte. Le dépôt du fichier dans les Réglages montre les lignes **avant** l'enregistrement.
4. **Images fournies par l'utilisateur** : formats PNG et SVG seulement. Un SVG est affiché comme image (`<img>`), jamais inséré dans la page, puisqu'il peut porter du script. Elles restent dans le navigateur.
5. **Les fuites** restent le seul chemin par lequel un détail militaire peut sortir, et seulement s'il a été écrit par l'animation (avis n°29).

## Mise en œuvre
- **Moteur** :
  - nouveaux types : `nrbc` (attaque NRBC), `zone_contaminee` et `presence_militaire` (perception seule) ;
  - champ `villesProches`, qui donne le niveau « proximité » ;
  - effets selon l'avis ;
  - bouton « Importer un fichier… » dans le panneau Événements de zone.
- **Carte** : mode Animation, avec une palette de symboles (APP-6 générés, images importées), un outil « zone » (cercle : centre et rayon) et une fiche par élément (type, libellé, dates, perception civile, rayons). Calcul des villes touchées et proches. Le travail en cours est gardé dans le navigateur. Export du fichier `situation`, qui contient les éléments et les événements pour le moteur.

## À mesurer
- les avatars proches disent ce qu'ils ont vu ou entendu, sans jamais un détail militaire ;
- les habitants d'une zone NRBC se confinent ou partent ;
- les villes au-delà de la proximité restent dans l'ignorance jusqu'à une annonce.
