# Avis n°98 — 2026-10-11 — app-ia : l'écran du moteur des avatars IA d'une zone

> DESIGNER contribue, il ne tranche pas. Maquette statique : `index.html` (ce dossier), en local seulement, sans toucher aux dépôts. Données de démonstration fictives (villes en H…, « GET », aucune personne réelle).
> Lu avant : `PLEIADE\PLAN_APP_IA.md` (réponses de l'utilisateur du 11/10 ~17 h 20 en tête), page Population IA d'eho (`eho\src\app\(admin)\population-ia\page.tsx`, son interrupteur), coquille de la Console d'animation (`app-admin` : `Shell.tsx`, `Dashboard.tsx`, `globals.css`, `pleiade-theme*.css`, `barre-zone.css`), avis n°69/71 (navigation, barre de zone), n°77 (cohérence de la Console), n°97 (tutoriel). Données réelles du prototype consultées en lecture : `dev\prototype-ia\pont\etat.json` (journal), `campagnes.json`, `pont.mjs` (calcul du coefficient de crise).
> Contrôle : Playwright à 1280 px (clair et sombre) et 820 px (tablette), sur les trois pages. Aucune erreur JS, pas de défilement horizontal. La fenêtre de confirmation se ferme au clic sur le fond, le volet de détail se ferme par Échap. Captures `capture_*.png` dans ce dossier.

## Ce que montre la maquette

**Deux étages, comme partout** : la barre de zone PLÉIADE (sombre, identique, « Avatars IA — vous êtes ici » dans « Apps de la zone »), puis la coquille de la Console, à l'identique : wordmark espacé, onglets à soulignement craie, « Exercice · non classifié », Auto/Clair/Sombre, initiales, « Se déconnecter ». À la place du logo constellation, le **✦** : c'est déjà le signe de l'IA dans eho (Population IA, couche ✦ IA de la fiche d'un avatar, avis n°91).

**Trois destinations** : Tableau de bord · Journal · Réglages. Le titre de chaque page reprend le libellé de son onglet, et chaque page a un « ? » (À quoi sert · Par quoi commencer · Ensuite).

1. **Tableau de bord**
   - **Interrupteur** en tête, sur toute la largeur. On y lit :
     - l'état, donné par une forme et un mot (● ACTIFS / ○ COUPÉS / ? ÉTAT INCONNU) ;
     - une phrase qui dit ce que cela veut dire ;
     - qui a basculé, quand, et **depuis quelle app** (eho ou Avatars IA) ;
     - la fraîcheur de la relecture : « Relu dans eho il y a 4 s ». Le témoin passe à l'orange au-delà de 30 s.

     Un seul bouton : « Activer les avatars IA » (vert) ou « Couper les avatars IA » (rouge, en contour). En dessous : « Le même interrupteur que dans eho › Population IA ».
   - **Moteur** : une phrase d'état en gros (voir R3), la progression du cycle (avatar n sur N, commencé à, depuis), une frise « Cycle → Pause 90 s → Cycle suivant » qui allume l'étape en cours, puis « 61 avatars animés sur 105 qui ont une fiche · Population IA dans eho ↗ ».
   - **Dernier cycle** : 6 chiffres sur une grille de 3 × 2 (durée, lectures, réponses, J'aime, publications dont partages, erreurs) ; sous chacun, la moyenne des 12 cycles précédents. Les erreurs ne sont en rouge que si elles sont > 0.
   - **Tendance des 12 derniers cycles** : 4 petits graphiques en barres, une seule série chacun, avec la moyenne en pointillé : durée, écrits, J'aime, erreurs. Le dernier cycle est en craie, les erreurs en rouge. Une bulle au survol, et une bascule « Graphiques | Tableau » qui donne aussi les garde-fous et les partages.
   - **Derniers écrits et garde-fous** : les 5 dernières lignes du journal, avec « Tout le journal → ».
2. **Journal**
   - Lignes regroupées **par cycle**. Chaque groupe a un bandeau de synthèse : durée, lectures, écrits, J'aime, garde-fous, erreurs.
   - Chaque ligne donne : l'heure, l'avatar avec sa cohorte (pastille et mot), l'action (glyphe et verbe), et le contenu sur 4 étages :
     - la cible (↳ auteur : « extrait ») ;
     - le texte publié, avec une puce « reprend #X » ou « conteste #X » ;
     - « ▲ Garde-fou : … », en orange ;
     - « Pourquoi : … », en italique atténué.
   - Filtres :
     - un avatar, par une recherche avec liste ;
     - un segment **« Écrits et garde-fous (10) · Garde-fous seulement (4) · Tout (20) »** ;
     - un menu « Types ▾ » pour le réglage fin (8 cases avec leur nombre) ; il devient « Types : 5 sur 8 ▾ » dès qu'on le personnalise ;
     - la période.
   - En bas de chaque cycle : « 7 autres actions de ce cycle (J'aime, lectures…) · Afficher tout ».
   - Les nouvelles lignes n'arrivent pas sous les yeux du lecteur : une pastille « 3 nouvelles actions — Afficher » les annonce.
   - Un clic sur une ligne ouvre un **volet de détail** à droite : texte complet, **version écartée** barrée pour un texte reformulé, garde-fou, effet sur l'opinion, lien vers l'avatar dans eho. Il se ferme au clic extérieur, par Échap, et le focus revient à la ligne.
3. **Réglages** (Administration)
   - **Coefficient de crise** :
     - un curseur de 0,2 à 3 et un champ numérique ;
     - 5 repères cliquables : 0,2 quasi-silence · 0,5 accalmie · 1,0 normal · 2,0 soir de crise · 3,0 maximum ;
     - un encadré **« Concrètement, à 2,0 »** : **80 messages par heure au plus** pour toute la population (40 × coefficient), puis le plafond horaire d'un avatar réservé, d'un avatar très extraverti et d'un relais (formules de `pont.mjs`) ;
     - « Enregistrer » ne s'active que s'il y a une modification, avec la ligne « Non enregistré : 1,0 → 2,0 ». Après l'enregistrement : « Pris en compte au prochain cycle (vers 17:48) ».
   - **Campagnes de hashtags** : un tableau # · Sens · Modifié (qui, quand) · ✎ ✕. Le sens se lit en **barres divergentes** autour d'un zéro central, une par axe (FORCE, Mercure, institutions), doublées par les mots « contre · 1,0 », « pour · 0,6 » ou « sans effet ». La fenêtre « Nouvelle campagne » a un curseur de −1 à +1 par axe. Une erreur de saisie s'affiche à la GOV.UK : elle dit comment corriger.
   - **Contexte de l'exercice** : une zone de texte, un compteur de caractères et de mots, et la consigne d'écriture (faits de la fiction, sans consigne de camp, aucune personne réelle).
   - **Historique des réglages** : date, qui, quoi, avec la valeur avant → après. Chaque enregistrement y ajoute une ligne et affiche un message de confirmation.

**Ce qui n'y est pas, par décision utilisateur** : la validation humaine, « Lancer un cycle maintenant », les clés et les adresses internes (le texte dit « nœud de calcul », jamais une URL), les fiches des avatars et le choix de qui est animé (tout cela reste dans eho, accessible par un lien).

**Commandes de démonstration** (encadré pointillé en bas à gauche, hors de l'app) : changer l'état du moteur, simuler une bascule depuis eho, un conflit pendant la confirmation, eho injoignable, l'arrivée de nouvelles actions.

## Choix principaux et leurs sources

1. **L'interrupteur affiche l'état relu, jamais l'état supposé.**
   - Au clic, la réponse est immédiate (« Bascule demandée… relecture dans eho », bouton désactivé). L'état ne change qu'**après relecture** dans eho : aucune mise à jour optimiste.
   - La confirmation rappelle l'état relu et dit que la bascule sera refusée si quelqu'un l'a changé entre-temps (précondition « état attendu » : voir R-API).
   - Si eho a basculé de son côté, la relecture suivante (≤ 15 s) fait clignoter le bloc et affiche « Avatars IA activés par lt.orsini depuis eho (17:44) ».
   - Si eho ne répond pas : « ÉTAT INCONNU » sur fond hachuré, bouton inactif avec sa raison, et rappel que le moteur se tait.

   Sources : Nielsen 1, l'état du système toujours visible (REF-14, règle 25) ; Doherty, une réponse en moins de 400 ms (REF-06, règle 13) ; règle MINERVE « indicateur d'état : mesurer exactement ce qu'on rapporte » ; information jamais portée par la couleur seule (REF-07, règle 10).
2. **Même famille que la Console, au composant près.** Mêmes jetons (`shell / panel / sunken / line / ink / craie`, statuts `online / dev / halt`), angles vifs, Archivo et JetBrains Mono. On reprend `pl-panel` avec son sur-titre, `pa-stat`, `pl-seg`, `pl-bascule`, `pl-etiquette`, la ligne de journal en grille (`pl-journal-ligne`), la barre de zone commune. Seul ajout : le ✦, déjà employé par eho. L'utilisateur passe de la Console à Avatars IA sans rien réapprendre. Sources : Jakob (REF-06) ; deux étages de navigation (règle 29) ; vocabulaire contrôlé (règle 36) ; avis n°71 et n°77.
3. **Un état du moteur = une forme, un mot, une phrase et l'heure du prochain événement.**
   - ● En cycle — avatar 23 sur 61 ;
   - ❚❚ En pause jusqu'à 17:47:04, avec « le suivant part 90 s après la fin du précédent (dans 41 s) » ;
   - ○ En attente — interrupteur coupé ;
   - ? En attente — eho ne répond pas ;
   - ✕ Nœud de calcul injoignable, avec depuis quand, la garantie « rien publié à moitié » et l'heure du prochain essai.

   La frise Cycle → Pause 90 s rend visible la règle « fin + 90 s », qui surprendrait sinon (des cycles qui ne tombent pas à heure fixe). Le rouge est réservé à la panne. Sources : Nielsen 1 et 2 (REF-14) ; règles 10 et 25 ; Von Restorff, une seule couleur d'alerte (REF-06, règle 20).
4. **Le journal montre d'abord ce qui compte : écrits et garde-fous.** Sur le prototype, **7 417 lignes en une journée, dont 61 % de J'aime et 29 % de « ignorer »**. Ouvert sur « tout », le journal serait illisible pendant un exercice. Par défaut, il montre donc réponses, publications, partages, reformulations et blocages, plus toute ligne qui porte un garde-fou. J'aime et lectures restent **comptés**, au bandeau du cycle et dans « n autres actions ».
   - Le garde-fou est un **marqueur orthogonal** à l'action : un « ignorer » peut porter un garde-fou, comme dans les données réelles.
   - Il est en orange (`dev`, ▲), pas en rouge : c'est le système qui fonctionne, pas une panne.
   - Au-delà de 5 commandes, les types passent dans un menu.

   Sources : Hick (REF-06, règle 16) ; Nielsen 8, minimalisme ; mettre en valeur en atténuant le reste (REF-07, règle 5) ; barre de filtres repliée au-delà de ~5 commandes (règle 37).
5. **La lecture n'est jamais déplacée sous les yeux.** Les nouvelles lignes sont annoncées par une pastille, sans saut de la liste. Le détail s'ouvre dans un **volet d'appui** (le journal reste visible). Fenêtres et menus se ferment au clic extérieur (un vrai clic, moins de 10 px entre l'appui et le relâché) et par Échap, avec retour du focus. Sources : règle 28, une navigation stable ; Nielsen 3, contrôle ; volet d'appui (REF-23, règle 38) ; APG Dialog (REF-19, règle 11) ; règle utilisateur « fermer au clic extérieur » ; leçon de l'avis n°54.
6. **Un réglage s'exprime dans son effet concret, et chaque modification laisse une trace.** On ne demande pas à l'Administration ce que « 2,0 » veut dire : l'écran répond « 80 messages par heure au plus ». Les campagnes se lisent en barres et en mots, pas en nombres signés seuls. Chaque enregistrement dit **quand il prend effet** (au prochain cycle, vers hh:mm) et s'inscrit dans l'historique (qui, quand, avant → après). Sources : Tesler, la complexité portée par le système (REF-06, règle 19), sur le précédent de la « ligne de conséquence » de l'avis n°70 ; Nielsen 1 ; Peak-End, une confirmation nette (règle 18) ; erreurs à la GOV.UK (REF-10, règle 24).

Choix secondaires :
- **Confirmations asymétriques** : pour « Couper », le focus va sur **Couper**, parce que c'est un geste d'urgence qui doit pouvoir se valider par Entrée. Pour « Activer », il va sur **Annuler**, parce que cela fait publier des avatars devant les joueurs. Source : APG Dialog (REF-19), « focus sur l'action la moins destructrice ». Ici, la moins risquée en exercice est de couper.
- **Une seule action principale par zone** (règle 37) : l'interrupteur sur le Tableau de bord, « Enregistrer » par panneau dans les Réglages.

## Remontées techniques (pour PLEIADE / CYBERSECU)

- **R-API, précondition à la bascule** : le `PUT` de l'interrupteur, dans eho, devrait porter l'**état attendu** (`{ actif: true, attendu: false }`) et répondre 409 si l'état a changé. Sans cela, deux bascules croisées (eho et app-ia) s'annulent en silence. Il faut aussi tracer la **provenance** (`depuis: "eho" | "app-ia"`) : la page d'eho ne la connaît pas aujourd'hui (elle affiche « par X », pas « depuis où »).
- **eho, Population IA** : pour que les deux boutons disent la même chose, l'interrupteur d'eho devrait reprendre les mêmes éléments : relecture affichée (« relu il y a n s »), provenance, refus en cas de conflit, état inconnu si le moteur ne lit plus. Aujourd'hui, la page d'eho se recharge après le `PUT`, ce qui est correct, mais elle n'affiche ni la provenance ni le conflit.
- **Journal** : il faut une API paginée et filtrée côté serveur (avatar, types, garde-fou, période), car le volume est de l'ordre de 7 000 lignes par jour. Il faut aussi le compte des lignes masquées par cycle, et un champ `garde` distinct de `action`. La reprise ou la contestation d'un # devrait être un **attribut** de l'action (`hash`, `mode`), et non une action à part (« reprend #paixmaintenant » dans le prototype).
- **Sécurité** (CYBERSECU) : le contexte de l'exercice et les campagnes sont du **texte injecté dans les invites** du modèle. Il faut une longueur bornée et un rôle Administration vérifié côté serveur. L'historique des réglages doit tracer l'auteur réel (session), pas une valeur envoyée par le client.

## Points à trancher par l'utilisateur

1. **Nom à l'écran** : « Avatars IA » (proposé : c'est déjà le mot de l'interrupteur et de « Population IA » dans eho) ou « Moteur IA » ?
2. **Focus asymétrique** des confirmations (Couper → focus sur Couper, Activer → focus sur Annuler) : d'accord ?
3. **Journal par défaut sur « Écrits et garde-fous »**, avec J'aime et lectures comptés et repliés : d'accord, ou ouvrir sur « Tout » ?
4. **Coefficient de crise** : enregistrement direct avec trace dans l'historique (proposé), ou confirmation au-delà de 2,0 ?
5. **Durée de conservation du journal** affichée (« Conservé 7 jours » dans la maquette) : quelle valeur ? C'est lié à la purge du lot L4.
6. **Plus tard, rôle d'animation en lecture** : les animateurs voient-ils le Journal (utile pour comprendre pourquoi un avatar a répondu à un joueur) ? Si oui, les Réglages restent masqués et une pastille « Lecture seule » s'affiche, comme dans la Console.

## Suite
Mise en œuvre au lot L2 du plan (PLEIADE), en local. La remontée R-API est à voir avec PLEIADE et CYBERSECU avant le code de l'interrupteur.
