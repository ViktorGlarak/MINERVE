# Avis CYBERSECU (et DESIGNER n°113) — Intégration de la carte de situation au moteur IA

**Date** : 2026-10-15 · **Décisions utilisateur** : la carte devient un onglet du moteur IA (app-ia), avec un lien depuis la console d'animation ; les animateurs **voient**, l'Administration **pose** les actions. · **Mise en œuvre** : PLEIADE (`app-ia`, `pleiade-platform/catalog/ia.yml`, `app-admin`)

## Constat
- Le moteur ne déclare qu'un rôle, `admin`. Toutes ses pages et routes exigent ce rôle, ce qui a été vérifié dans le code.
- Les animateurs des cellules n'y ont donc aujourd'hui aucun accès.

## Règles (CYBERSECU)
1. **Un nouveau rôle de client** : `carte` (« Carte de situation, consultation »), déclaré dans le catalogue de PLÉIADE. Il est attribué dans Keycloak aux animateurs (groupes GREYCELL et FORAD) par l'Administration. **Il n'ouvre que la page Carte et sa route de lecture** : toutes les autres pages et routes restent réservées au rôle `admin`, sans changement. Un compte ayant seulement ce rôle est envoyé sur la Carte s'il ouvre l'accueil.
2. **La lecture est minimisée.** La route de la carte ne renvoie que ce qu'elle affiche :
   - **par avatar** : identifiant, nom affiché, compte, cohorte, statut de lecteur ;
   - **sa vie** : ville, ville de travail, métier, âge, ville de ses proches ;
   - **son état** : situation (évacué…), deux axes d'opinion, humeur, relations marquées (chiffres seulement) ;
   - **ses 3 derniers messages publiés**, textes d'avatars seulement.
   - **Jamais** les souvenirs, les croyances, la mémoire détaillée ni aucun message de joueur.
   - Le résumé est gardé 60 s en cache pour ne pas solliciter eho à chaque rafraîchissement.
3. **L'écriture est réservée à l'Administration**, avec une session navigateur, une origine identique et un corps JSON borné :
   - la **situation** (symboles et zones) a un schéma fermé : position dans la zone, code APP-6 contrôlé, textes bornés, 200 éléments au plus ;
   - les **images personnelles** : PNG ou SVG, 150 Ko au plus chacune, 20 au plus, affichées comme images ;
   - **« Transmettre au moteur »** passe par `validerEvenements` et remplace seulement les événements issus de la carte (préfixe `carte-`), sans toucher à ceux saisis à la main ;
   - **chaque écriture est journalisée** (auteur, nombre d'éléments, empreinte).
4. **Les symboles ne sortent jamais vers les avatars** (avis n°31) : le moteur ne lit que les événements de zone.
5. **Les fonds de carte externes** (IGN, OSM) sont chargés par le navigateur de l'animateur. Le serveur n'en relaie aucun, et il n'y a donc aucune nouvelle sortie réseau depuis la zone. Un cache local des tuiles est à prévoir pour le réseau sans Internet.

## Insertion (DESIGNER n°113)
- Dans le moteur, l'onglet **« Carte »** est placé en premier pour un compte qui n'a que ce rôle, après « Réglages » pour l'Administration. La carte occupe tout l'écran sous la barre de zone, avec un retour « ‹ Moteur IA » pour l'Administration.
- Dans la console d'animation, un lien **« Carte de situation ↗ »** est ajouté à la navigation. Il ouvre la carte dans un nouvel onglet : on garde sa console, et la connexion unique évite toute nouvelle connexion.
- En consultation, la bascule « Animation (situation) » est **absente**, et non grisée (un contrôle sans objet ne s'affiche pas). Une ligne « Consultation : la situation est posée par l'Administration » l'explique.
- À la place de l'export de fichier, l'Administration dispose de **« Transmettre au moteur »**, qui affiche le compte des événements et une confirmation, puis la date de la dernière transmission.
