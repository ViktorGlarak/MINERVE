# Avis n°97 — 2026-10-11 — Tutoriel PLÉIADE : le panneau du guide et l'écran de suivi

> DESIGNER contribue, il ne tranche pas. Maquette statique : `index.html` (ce dossier), en local seulement, sans toucher aux dépôts.
> Lu avant : avis n°81 (conception du tutoriel), n°71 (barre de zone commune), `PLEIADE\MEMOIRE.md` § « Chantier — Tutoriel guidé » (reprise du 11/10), `PLEIADE\GUIDE\PARCOURS.md`, fiches J0 à J7 et A1.
> Contrôle : Playwright à 1280 px (clair et sombre) et 820 px (tablette). Aucune erreur JS, pas de défilement horizontal. Échap ferme le guide, un clic à l'extérieur aussi quand il n'est pas épinglé, la coche se fait au vrai clic sur la publication, et le parcours se termine.

## Ce que montre la maquette
- **(a) Barre de zone** (toujours sombre, avis n°71) : à droite, le bouton **Guide**. Il affiche le numéro de l'étape (« Étape 3 sur 7 »), 7 segments de progression et, à partir de 1180 px, le titre de l'étape. Le bouton s'allume un instant quand un geste est détecté.
- **(b) Volet du guide**, sur la fiche J2 (Social) : consigne, état « En attente du geste : ouvrir la publication de @rzo_katia_chapman », le pas-à-pas de la fiche, et « Bon à savoir » replié. Quand le geste est détecté, un bandeau vert annonce « Étape 3 faite — geste détecté » et la fiche suivante s'affiche aussitôt (J3 eho), avec le lien « Ouvrir eho ». Le stagiaire n'a rien à cliquer de plus.
- **(c) Le parcours** : les étapes faites (on peut cliquer pour les relire), l'étape en cours, les étapes à venir. Chaque état est donné par une **forme et un mot** (« fait », « en cours », « à venir »), pas seulement par une couleur.
- **(d) Écran de suivi de l'animation**, en lecture seule : une ligne par stagiaire, une colonne par étape. On y distingue le geste détecté (pastille pleine) du « J'ai terminé » (carré cerclé). Une seule alerte : « sur la même étape depuis plus de 10 min ».
- **Contexte « Exercice réel »** : le bouton devient **Aide**, sans progression. Le volet liste les gestes de l'app ouverte comme un aide-mémoire : rien ne s'y coche.

## Choix principaux et leurs sources
1. **Un volet d'appui non modal, épinglable.** L'utilisateur a fixé deux règles : la fenêtre se ferme au clic extérieur, et le stagiaire doit cliquer dans l'app pour faire le geste. Une fenêtre flottante se fermerait donc au premier geste. D'où deux modes :
   - **non épinglé**, la règle s'applique telle quelle (clic extérieur, Échap) ;
   - **épinglé**, le guide se range à côté de l'app au lieu de la recouvrir : ce n'est plus une fenêtre. Échap ferme toujours.

   Sur tablette, il se superpose toujours. Sources : mise en page canonique « volet d'appui » (REF-23, règle 38) ; Dialog non modal, Échap et retour du focus au déclencheur (REF-19, règle 11).
2. **L'étage de la plateforme, jamais celui de l'app.** Le guide part de la barre de zone. Il porte « hors exercice » en en-tête et une teinte propre (bleu-vert), absente de toute app et de tout média fictif. Le stagiaire ne le confond pas avec un message de la fiction. Sources : deux étages jamais confondus (règle 29, REF-22) ; Von Restorff (REF-06).
3. **L'état du système toujours visible.** Il y a deux états : « En attente du geste : … L'étape se coche toute seule », puis le bandeau « geste détecté » qui rappelle **ce qui a été fait** (« Vous avez ouvert la publication de… »). La barre garde le numéro et la progression quand le volet est fermé. Le passage d'étape est annoncé aux lecteurs d'écran (`aria-live`). Sources : Nielsen 1 (règle 25) ; Peak-End (règle 18) ; « prochaine étape après chaque geste » (règle 39).
4. **Une seule action par fiche, et un recours discret.** Une étape à coche automatique n'a pas de bouton principal : seulement « Ouvrir *app* » et un lien discret « Geste non reconnu ? Marquer comme fait ». Une étape « bouton » (J4 presse, J5 fichiers) a **une** action principale, « J'ai terminé cette étape », et le volet dit pourquoi (« le site ne signale pas votre lecture »). Sources : une action principale (règles 6, 37) ; Nielsen 3, contrôle et liberté (REF-14) ; Hick (REF-06).
5. **Lire peu à la fois.** Dans l'ordre : la consigne en 16 px, l'état, le pas-à-pas numéroté (les libellés de l'app en gras, repris tels quels des fiches), puis « Bon à savoir » replié. Pas de « Ce que vous allez apprendre » dans le volet : ce bloc reste dans la fiche. Le parcours entier n'est visible qu'en bas du volet. Sources : révélation progressive à 2 niveaux (règle 32, REF-21) ; lignes de 45 à 75 caractères, interligne 1,45 (règles 8, 26).
6. **Un suivi qui se lit sans légende, et une seule alerte.** La forme seule distingue fait, déclaré, en cours, bloqué et à venir, avec un mot ou un nombre de minutes dans les cas utiles. Le rouge est réservé à « depuis plus de 10 min ». Le résumé en tête donne effectifs, terminés et bloqués. L'animateur n'a aucun bouton : il suit, il ne pilote pas (décision du 11/10). Sources : jamais la couleur seule (règle 10) ; une seule couleur d'alerte, rare (règle 20) ; « une part se donne avec son effectif » (avis n°96).

Hors de ces choix : pas de chronomètre côté stagiaire, puisque les étapes avancent au geste et pas à l'horloge. La durée (1 h au plus) n'est montrée qu'à l'animateur. Pas de question de contrôle, pas de levier ludique (avis n°81, règle 39).

## Ce que la maquette fait remonter (à corriger ailleurs)
- **Fiches J0 et J7** : elles parlent d'un « bouton **?** du guide » et d'une « liste **Premiers pas** du portail ». Avec ce volet, le guide est le bouton **Guide** de la barre (qui devient **Aide** en exercice), et le « ? » reste l'aide de l'écran (avis n°71, R6). Il faut reformuler ces deux fiches (PLEIADE).
- **Numérotation** : le parcours compte 8 fiches (J0 à J7), mais J7 est un écran de fin, pas un geste. La maquette affiche donc « Étape n sur 7 », avec J0 en étape 1. Les fiches restent numérotées à partir de 0 en interne.
- **J3** : la consigne « notez votre estimation » est un geste (enregistrer une fiche), pas une question de contrôle. Elle reste conforme à la règle du 08/10.

## Points à trancher par l'utilisateur
1. **Volet épinglé par défaut** dans la zone d'entraînement, non épinglé en exercice réel ? C'est la recommandation de DESIGNER : pendant le tutoriel, on lit en faisant.
2. **Barre de zone pour les joueurs sur le Social et la Presse.** Aujourd'hui, l'avis n°71 ne montre la barre qu'à l'animation sur le Social, et jamais sur le site public d'un média. Or le guide part de cette barre.
   - **Proposition** : une barre réduite pour les joueurs (portail + Guide, sans « Apps de la zone »).
   - **Sur la presse publique**, pas de barre : les étapes J4 et J5 se valident par « J'ai terminé » depuis l'onglet précédent. C'est déjà le cas dans les fiches.
3. **Lien « Geste non reconnu ? Marquer comme fait »** sur les étapes automatiques : à garder (filet de sécurité si un signal manque, recommandé), ou à retirer pour forcer le vrai geste ?
4. **Seuil d'alerte du suivi** : 10 min sur une même étape, ou un seuil par étape ?
5. **Emplacement de l'écran de suivi** : une rubrique « Tutoriel » de la Console d'animation, ou une page de l'orchestrateur à côté de la zone ? Cela dépend de l'endroit où PLEIADE range la progression par compte.
6. **Fil rouge** : `@veille_hlun_04` et `#PontSud` ne sont que des exemples. Le contenu (un hashtag ou un fait par stagiaire) est à écrire avec ANALYSTE_ARN. La maquette ne l'utilise qu'à l'étape J6, en le glissant dans le message à publier.

## Suite
Mise en œuvre par PLEIADE après ces arbitrages, en local seulement. Côté plateforme : progression par compte et lecture des signaux des fiches. Côté apps : composant volet dans la `BarreZone` des 7 apps Next et dans `app-barre-zone` du Social. ⛔ Localhost uniquement jusqu'au feu vert de l'utilisateur. CYBERSECU à consulter sur la lecture des journaux d'actions par la plateforme, puisque le guide lit ce que **le stagiaire** a fait.
