# Avis DESIGNER n°114 — 2026-10-15 — La carte de situation dans la Projection grand écran

> **Demande utilisateur** : « insérer une sorte de recopie de la carte de situation dans la vue plein écran qu'on utilise sur la console d'animation ». La vue plein écran est la **Projection grand écran du Cockpit** (`app-cockpit`, `ProjectionView.tsx`, avis n°108) ; la carte vit dans le **Moteur IA** (`app-ia`, `/carte`, avis n°111 à 113).
> **Statut** : propositions, rien n'est codé. Le besoin de l'utilisateur, les choix de PLEIADE et les règles CYBERSECU priment.

## Ce que la projection impose (repris de l'avis n°108)
- Lue de **4 à 8 m**, sans souris ni molette : ce qui dépasse ou demande un survol n'existe pas. Plancher de **18 px** pour tout ce que la salle lit.
- La page **tient dans l'écran** (1920 × 1080), sans défilement.
- **Dire quand ce n'est plus en direct** (bandeau « Liaison perdue depuis… »).
- CYBERSECU K10 : contenus **publics** et **agrégats** seulement.

## Ce que la carte doit devenir pour une salle (quelle que soit la piste)
Une **carte de projection**, pas la carte de travail recopiée :
1. **Aucun panneau, aucune infobulle, aucun mode Animation** : rien qui se commande.
2. **Cadrage fixe** sur la zone d'exercice ; recadrage doux sur une zone qui vient d'être transmise (et retour après 2 min).
3. Ne garder que ce qui se lit de loin : **les zones d'événement** (contour épais, nom en 22 px : « Bombardement · HToul · 14:05 »), **les points des avatars** groupés par ville (anneaux), **les flèches d'évacuation**. Pas de liens entre avatars (illisibles à 6 m), pas de noms d'avatars.
4. Un **encart de chiffres** (28-40 px) : zones actives, évacués, en route, à l'abri.
5. Fond **Nuit** (hors ligne, sans noms réels) par défaut ; animation lente ou coupée (pas de scintillement sur un grand écran).
6. Une ligne de fraîcheur « Carte relue à 14:07 » et le même bandeau de liaison perdue que le reste de la projection.

## Les quatre pistes de mise en page
| Piste | Principe | Pour | Contre |
|---|---|---|---|
| **A. Deux vues au choix de l'opérateur** | La projection a deux vues : « Fil » (celle d'aujourd'hui) et « Carte » (carte en grand + colonne de droite gardée : volumes, privé). L'opérateur bascule (touche C ou bouton du pied de page). | Chaque vue garde ses tailles de salle ; la carte a la place d'être lue ; personne n'est coupé en pleine lecture | Il faut un geste de l'opérateur |
| **B. Alternance automatique** | Même chose, mais bascule seule toutes les 45 s, avec une barre de progression. | Rien à faire | La salle est coupée en pleine lecture ; un événement important peut tomber pendant l'autre vue. Déconseillé seul ; acceptable en option de A |
| **C. Écran partagé** | Fil réduit à gauche (3 cartes), carte au centre, colonne de droite. | Tout est visible en permanence | Le fil perd ses 5 cartes lisibles (n°108 §1) ; la carte fait ~900 px de large : juste lisible |
| **D. Vignette** | Une petite carte (440 × 400) remplace « Hashtags du moment » dans la colonne de droite. | Le plus simple, rien ne bouge | À 6 m, on ne voit que des taches : sert à dire « où », pas « quoi » |

**Recommandation : A**, avec l'alternance de B en **option** (désactivée par défaut). D seulement si l'on veut « juste un repère ».

## Technique (à confirmer par PLEIADE et CYBERSECU)
- **Une seule carte, pas de copie du code** : `app-ia` sert une vue dédiée `/carte/projection` (lecture seule, gabarit ci-dessus), que la projection du Cockpit **intègre** (cadre `iframe`). La carte reste maintenue à un seul endroit.
- Il faut autoriser l'intégration **depuis le seul Cockpit de la zone** (en-tête `frame-ancestors`), et le poste de projection doit avoir le rôle « Carte de situation ».
- Variante sans intégration : la vue `/carte/projection` ouverte sur un second écran. Aucun changement de sécurité, mais deux écrans.

## Sources
Avis n°108 (projection, tailles de salle, liaison perdue) ; avis n°111 à 113 (carte) ; Nielsen 1 et 8 (REF-14) ; règle 38 (flux).
