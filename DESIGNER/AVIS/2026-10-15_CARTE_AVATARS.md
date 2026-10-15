# Avis DESIGNER n°111 — Carte des avatars (maquette locale)

**Date** : 2026-10-15 · **Demandeur** : utilisateur (image de référence : planisphère sombre en points lumineux, réseau d'arcs néon cyan et magenta) · **Décisions utilisateur** : zone d'exercice (Lorraine) ; première maquette avec les quatre couches (avatars et évacuations, liens, événements de zone, opinion par ville) ; maquette locale qui lit un export du moteur. · **Mise en œuvre** : PLEIADE (`C:\CECPC\pleiade\dev\carte`, hors dépôt de zone)

## Intention
Une **vue de situation** que l'on regarde, en salle comme au poste : *où sont les avatars, qui parle à qui, ce qui arrive aux villes, de quel côté penche chaque ville*. Ce n'est pas un SIG : on lit d'un coup d'œil et on n'édite rien.

## Recommandations

- **R1. Le fond.**
  - Nuit profonde (`#060B1A` vers `#0B1530`), sans relief ni routes.
  - Le territoire en **nuée de points** d'environ 1,2 px, cyan à 35 %, avec une densité légèrement plus forte près des frontières. Les limites de départements en filets à 15 %, la frontière avec la zone de Mercure (est) en filet plus marqué.
  - Le nom des villes habitées en petites capitales grises, toujours avec le **H** (« HNANCY »). C'est la convention de l'exercice : jamais le nom réel.
- **R2. Les avatars.**
  - Un point par avatar, dispersé dans un disque autour de sa ville (2 à 6 km selon le nombre d'habitants) pour éviter l'empilement.
  - **Le camp se lit par la couleur et par la forme**, jamais par la couleur seule : rouge corail pro-Mercure (point plein), bleu électrique pro-Arnland (anneau), cyan pâle neutre (petit point).
  - Rayon de 3 à 7 px selon l'activité (messages des dernières 24 h).
  - Halo additif léger, comme dans l'image de référence.
  - Les lecteurs sont plus discrets (50 %).
- **R3. Les évacuations.**
  - Un arc courbe animé de la ville quittée vers la destination, avec une traînée qui avance, en orangé.
  - L'évacué est dessiné à sa destination. Un point « en route » clignote doucement à mi-parcours.
  - Un fantôme à 20 % reste à la ville d'origine : on voit ce qui s'est vidé.
- **R4. Les liens.**
  - Des arcs fins entre avatars qui se répondent ou s'apprécient (familiarité ou affinité marquée). Arcs magenta entre camps opposés, cyan dans le même camp : on voit les **bulles** et les **ponts**.
  - **Par défaut**, seuls les liens de l'avatar survolé ou choisi. Les montrer tous ferait une pelote illisible à 200 avatars. Un interrupteur « tous les liens » reste disponible.
- **R5. Les événements de zone.**
  - Un halo pulsé sur la ville touchée, avec une couleur par famille : rouge pour un bombardement ou des combats, orange pour une évacuation, ambre pour un confinement ou un couvre-feu, violet pour une coupure, gris pour le reste.
  - **Une icône** de type Lucide dans le halo, en plus du libellé, jamais la couleur seule.
  - Le bilan en étiquette (« 6 évacués · 2 refus »).
- **R6. L'opinion par ville.**
  - Un disque translucide sous la ville, de rayon proportionnel au nombre d'habitants. Teinte sur une **échelle divergente** rouge vers gris vers bleu, selon (Mercure − FORCE) / 2 en moyenne.
  - Couche **désactivée par défaut**, parce qu'elle concurrence les points. Une légende de l'échelle avec ses deux pôles écrits : « pro-Mercure » à gauche, « pro-Arnland » à droite.
- **R7. La mise en page, en plein écran.**
  - **À gauche** (280 px, repliable) : le fichier chargé et sa date, les **couches** (cases), les **filtres** (camp, lecteurs, évacués, ville), une recherche par nom, et la légende.
  - **À droite**, à la sélection : la **fiche** de l'avatar (portrait si disponible, nom affiché, métier, ville, camp, humeur, situation, 3 derniers messages, liens principaux).
  - **En haut au centre**, le compteur global : « 205 avatars · 29 villes · 6 évacués · 2 événements ».
  - **À l'état vide**, une grande zone de dépôt « Déposez un export du moteur (.json) ». Le fichier reste dans le navigateur, rien n'est envoyé.
- **R8. Le mouvement.**
  - Animations lentes et continues (traînées, halos à 0,5 Hz). Aucune animation en boucle sur le texte.
  - `prefers-reduced-motion` : tout est fixe, sauf l'état « en route ».
- **R9. La lecture à distance**, pour un usage en salle plus tard : libellés à 12 px au moins, contrastes WCAG AA sur le fond, et des couleurs de camp distinctes aussi pour les daltoniens. Le corail et le bleu restent distincts dans les deutéranopies ; c'est la **forme** qui porte la différence.

## Doctrine
Une carte de situation **montre peu à la fois** : les points d'abord, les liens à la demande, l'opinion en couche optionnelle. Elle dit toujours de **quand** datent les données. Chaque couleur de sens est doublée d'une forme, d'une icône ou d'un mot.
