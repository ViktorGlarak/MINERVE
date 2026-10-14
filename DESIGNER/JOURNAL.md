# JOURNAL — DESIGNER

## Avis n°108 — 2026-10-14 — Cockpit : projection grand écran (contrôle demandé par l'utilisateur après codage)
- La projection (lot 5) avait été codée **sans avis** ; l'utilisateur a demandé le contrôle. Verdict : **VALIDÉ AVEC RÉSERVES** (`AVIS\2026-10-14_COCKPIT_PROJECTION.md`).
- Appliqué le jour même : page sans défilement (cartes entières, « + n plus anciens »), échelle de tailles pour la salle (plancher 18 px, message 30 px sur 2 lignes), état « plus en direct » (bandeau après 40 s, canal en panne « — »), couleur pleine réservée à la bande des catégories (étiquettes neutres dans l'en-tête, 3 au plus), mot « RÉSEAU »/« PRESSE » en plus de la couleur, ligne de réponse « ↳ Répond à … », bouton Retirer visible seulement si la souris vient de bouger + « Annuler » 10 s.
- **Addendum (demande utilisateur)** : l'étiquette « NOUVEAU » (2 min, puis 0,7 s) jugée inadaptée → **animation d'arrivée** : poussée FLIP 700 ms, entrée en fondu 500 ms décalée, liseré craie ~3 s, gros lot (≥ 3) en fondu, `prefers-reduced-motion` respecté, Web Animations API sans Motion. Le §7 initial (« pas de glissement ») est remplacé. Écart assumé à la règle 150-250 ms pour un écran sans geste vu à 6-8 m (avis, pas une source).
- Restent : palette fermée de couleurs de catégories (à remonter à PLEIADE : pas de bleu ciel, jaune, rouge ni gris) ; ingérer ISO 9241-303 / AVIXA (distances de lecture) ; test sur le vrai écran avec 3 animateurs au fond de la salle.

## Avis n°106 — 2026-10-13 — Console d'animation, Supervision : télécharger en .md les contenus de sa cellule
- **Demande utilisateur** : un bouton dans Supervision pour que l'animateur télécharge en .md ce que SA cellule a publié (scénarios et direct) + les réactions des autres comptes, filtré par Event / Storyline / Incident / Scénario et par types (publications, commentaires, citations, articles, reprises de hashtags), rangé Event > Storyline > Incident. Arbitrages déjà pris par l'utilisateur, repris tels quels.
- Code lu sans rien modifier (`app-admin`) : `Monitoring.tsx`, `Shell.tsx` (`PageHeader` a une prop `action`), `dialogs\Modal.tsx`, `IncidentPicker.tsx`.
- Avis : bouton secondaire en en-tête ; formulaire unique à 4 blocs (cellule en lecture, périmètre arbre/scénarios avec recherche, types, période) ; aperçu chiffré vivant + nom de fichier ; 4 états (rien, long, erreur, app injoignable sans partiel silencieux) ; structure du fichier avec bandeau de diffusion en tête et en pied, exemple de 20 lignes. `AVIS\2026-10-13_EXPORT_MD_SUPERVISION\AVIS.md`. Aucun commit.
- Remontées : PLEIADE (export serveur, cellule de la session, aperçu, rattachement du direct, hashtags lancés), CYBERSECU (libellé de diffusion, journalisation, plafond).

## Avis n°101 — 2026-10-12 — Console d'animation : avatars animés par l'IA (« CAMP IA ») traités comme réservés (avant commit)
- **Demande** (décision utilisateur du 12/10) : les avatars membres du groupe eho « CAMP IA », qui ne sont pas jouables sur le social, doivent être traités dans la Console comme un avatar réservé par un autre compte. Il faut **alerter** l'animateur, pas le bloquer. Cinq avatars de scénarios sont concernés, dont ManFredK et GREYCELL. Lu sans rien modifier (`wt-app-admin-likes`, branche `avatars-ia`, `git diff origin/main`) : `lib/avatars-ia.ts`, `lib/avatars-ia-serveur.ts`, `lib/scheduler.ts`, `PersonaPicker.tsx`, `ScenarioEditor.tsx`, `lib/kit-ia.ts`, `api/bff/scenarios/[id]/kit-ia/route.ts`, `globals.css` (`.pa-res*`), `KitIaDialog.tsx`. Comparé avec eho (`population-ia`, `dashboard` : ✦ `#c026d3`) et avec l'origine « IA » du social (`pi-sparkles`, MASTORION).
- **Ce qui va** : l'avis n°29 est bien repris.
  - L'étiquette est faite d'une icône et d'un mot, et ✦ est en `aria-hidden`.
  - La confirmation se fait dans la liste (pas de fenêtre) et le focus va sur « L'utiliser ». Le cas « réservé ET IA » est traité dans une seule phrase.
  - L'encadré est séparé de « À savoir » et ne bloque pas, avec `role="status"`. La liste compacte porte le préfixe ✦, le pendant de 🔒.
  - Les items publiés sont ignorés.
  - Si eho ne répond pas ou si le groupe n'existe pas, rien n'est affirmé.
  - Le kit écarte ces avatars et dit pourquoi. Le 409 « tous animés par l'IA » donne une issue.
  - L'écart avec les 🔒, qui restent dans le kit, est voulu par la décision et cohérent : un avatar réservé peut être utilisé avec une demande nominative, un avatar IA non.
- **Indispensable avant commit** :
  1. **Phrase ambiguë.** « @x est animé par le Moteur IA : il parle aussi de lui-même » peut se lire « il parle aussi de sa propre personne ». De même, « Le Moteur IA fait aussi parler ces avatars de lui-même » peut se lire « parler du Moteur ». Proposition :
     - confirmation : « @x est animé par le Moteur IA : il publie déjà de son côté. L'utiliser quand même ? » ;
     - `avertissementIa` : « … — items #a, #b. Il publie déjà de son côté : vérifiez que c'est voulu. » ;
     - pied de l'encadré : « Le lancement reste possible. Ces avatars publient déjà de leur côté (Moteur IA) : deux voix pour un même avatar peuvent se contredire. Si ce n'est pas voulu, changez l'avatar de ces items… ».
     « Lit et publie de lui-même » (`title`, kit) n'est pas ambigu et peut rester.
  2. **Remède hors de portée.** « Mettez l'avatar en pause dans eho › Population IA » : cette page est réservée à l'Administration (garde serveur), alors que l'animateur ne l'est pas. Écrire « ou demandez à l'Administration de le mettre en pause (eho › Population IA) », dans l'encadré et dans le 409 du kit.
  3. **Consigne du kit impossible à suivre.** « Ne les fais jamais publier, même si la demande les nomme » : leurs noms ne figurent pas dans le kit, l'IA ne peut donc pas les reconnaître. Écrire au minimum : « Si la demande nomme un avatar absent de cette liste, ne l'invente pas : signale-le. » Autre solution : lister leurs @ sur une ligne (au plus une centaine, c'est léger).
  4. **Avertissement absent côté humain.** `KitIaDialog` annonce les 🔒, mais pas les ✦ écartés, et l'animateur découvre l'absence de ManFredK au retour de l'IA. Ajouter une ligne fixe dans l'encadré `role="status"` : « Les avatars animés par l'IA (✦) ne sont pas dans le kit. » Le nombre exact n'est connu qu'au serveur, la phrase fixe suffit (règle R4 du n°29 : écartés **et annoncés**).
- **Différable** :
  - `title` du bouton quand l'avatar est à la fois réservé et IA : nommer les deux.
  - Fusionner les deux encadrés orange voisins (🔒 et ✦) en un seul « À vérifier » à deux sous-listes : une seule zone d'attention plutôt que deux boîtes identiques.
  - Dans l'encadré, la ligne répète l'en-tête et le pied : « @x — items #a, #b » suffit (le message serveur peut rester complet pour les autres usages). Même allègement à faire, à terme, pour 🔒.
  - Ranger les ✦ en fin de liste dans le sélecteur.
  - Si les lignes d'items portent un 🔒, faire de même pour ✦.
  - Remontée PLEIADE : un avatar qui passe en « CAMP IA » après « Vérifier » ne change pas l'empreinte, donc l'alerte n'apparaît qu'à la prochaine vérification. C'est acceptable puisque rien n'est bloqué.
- **Points tranchés (proposition)** :
  - **`pa-res-autre`** : c'est une **forme** (bordure en tirets, texte gris), pas une couleur, et elle veut dire « tenu ailleurs, une confirmation sera demandée ». C'est la décision de l'utilisateur, il est donc juste de la reprendre. La différence avec « Réservé » tient à l'icône (🔒 / ✦) et au mot, et non à la couleur (doctrine : jamais la couleur seule, n°29 R2 « partout pareil »). Il n'y a pas de risque de confusion, car le mot est toujours affiché.
  - **Icône** : ✦ est cohérent avec eho (titre « ✦ Population IA », tableau de bord, fiche « ✦ IA : non activée »). Pour reprendre le signal commun, teinter **seulement le glyphe** avec un jeton `--color-ia` (`#c026d3` en clair, environ `#e879f9` en sombre ; une icône demande un contraste de 3:1). Ne teinter ni la bordure ni le fond : l'étiquette crierait plus que « Réservé » et se heurterait à l'orange `dev`. Le `pi-sparkles` (✨) du bandeau d'origine du social est de la même famille. Il reste acceptable, faute de ✦ dans PrimeIcons, mais un même signe dans toutes les apps serait l'idéal à terme.
- **Point de doctrine** : un état « tenu ailleurs » garde **une seule forme**, quel que soit le titulaire (un compte ou le Moteur IA). Le titulaire se dit par l'icône et le mot. Un remède proposé dans un message doit être à la portée de celui qui le lit, sinon il faut dire à qui le demander.

## Avis n°100 — 2026-10-12 — eho, Population IA : « Installer la population IA » (avant push)
- **Demande** (décision utilisateur) : relire avant push un nouveau bloc d'eho (branche `installer-population`, non commitée). L'administrateur de DELATTRE 26 (production) y dépose le fichier « Télécharger les fiches » de la zone locale. La vérification s'affiche dans la page, il confirme, et 105 avatars entrent en pause. Constat de départ : zone vide, curseurs grisés, et l'administrateur croyait qu'il fallait d'abord activer les avatars. Lu sans rien modifier : `installation-ia.tsx`, `population-ia/page.tsx` (diff), `fiches-ia-import.tsx`, `lib/installation-ia.ts`.
- **Ce qui va** : même parcours que l'avis n°99 (dépôt, vérification lancée d'office et affichée dans la page, bandeau « rien n'a encore été installé » qui prend le focus, `confirmer` seule fenêtre, empreinte et 409 « Vérifier à nouveau »). Statuts forme + mot (+ ✕ = –), refusés dépliés, le reste replié, compteurs-liens, répartition par cohorte avant de confirmer, bouton qui dit l'effet (« Installer 105 avatars (en pause) »), blocage CAMP IA expliqué avec la marche à suivre, bilan avec lien vers les effectifs. Le fichier venant d'une autre zone est ici normal : il est mentionné sans alerte, c'est juste. Pas de « Admin ».
- **Indispensable avant push** :
  1. **Le bilan disparaît aussitôt** : `onInstalle` → `charger` → `pop.total` passe de 0 à 105, le bloc du haut (`!pop.total`) est démonté et celui du bas est monté vierge. Le message « 105 installés… » et le focus sont perdus. Il faut figer la place du bloc au premier chargement (état posé une fois), pas la recalculer à chaque rechargement.
  2. **Ordre quand la zone est vide** : le bloc d'installation doit passer AVANT `<Interrupteur />` (page.tsx l. 88-90). Aujourd'hui, le gros bouton vert « Activer les avatars IA » est la première action visible, et c'est lui qui a induit l'erreur. Ajouter une phrase dans l'interrupteur quand il n'y a aucun avatar : « Aucun avatar à animer pour l'instant : installez d'abord la population IA. »
  3. **En-tête contradictoire quand la zone est vide** (l. 83) : « 0 avatar animé sur 0 … on ne crée rien ici » se trouve juste au-dessus d'un bloc « Installer ». Si `!pop.total`, le remplacer par trois étapes : « Cette zone n'a encore aucun avatar IA. 1. Installez la population (fichier d'une autre zone). 2. Réglez les effectifs par cohorte. 3. Activez les avatars IA. »
  4. **Explication des curseurs grisés** (l. 94 ; voir ci-dessous).
  5. **Contresens dans la confirmation** (installation-ia.tsx l. 53) : « en pause : ni lus ni animés » veut dire qu'on ne les lit pas. Écrire : « en pause : ils ne lisent rien et ne publient rien, et restent jouables par l'animation et les joueurs. » « Jouable » est le mot de la liste (« en pause · jouable »), c'est donc lui qu'il faut employer.
  6. **Deux zones de dépôt sur une page vide** : masquer `FichesIaImport` quand `!pop.total` (export grisé, import inutile, risque de déposer le fichier dans la mauvaise zone et d'obtenir « 105 ignorés »).
  7. **Dépôt pendant l'application** : `onDrop` reste actif en état `verification` ou `application`, et un second dépôt relance `verifier`, qui remet `v` à zéro en pleine installation. Ignorer le dépôt dans ces deux états (le bouton est déjà désactivé).
  8. **Les 5 avatars déjà utilisés dans des scénarios** : en attendant la décision de l'utilisateur, ils ne doivent pas se fondre dans « + à installer ». Proposition pour le push : **A** = « – ignoré », avec la raison « Utilisé dans n scénario(s) de l'animation : à installer plus tard s'il le faut ». C'est réversible et ne demande aucun nouvel état. **B** (à terme) = « + à installer · réservé », hors des curseurs, réintégrable seulement à la ligne par « Réintégrer ». Ce n'est pas à DESIGNER de trancher.
- **Différable** : retour visuel au survol de la zone de dépôt (`survol`, comme dans n°99) ; près du bouton, « Les n refusés ne seront pas installés » (parité n°99) ; intro raccourcie à 3 phrases ; titre « Ajouter des avatars à la population IA » quand `total > 0` ; tableau vide « Aucun avatar installé : voir “Installer la population IA” ci-dessus » ; dans la raison « déjà installé », nommer le bloc (« Fiches de comportement », plus bas) plutôt que « l'import de corrections » ; dans le bilan, lien « Voir les avatars installés » vers la liste filtrée « En pause ».
- **Curseurs grisés, zone vide** : « Chaque curseur est borné par ce qui existe » dit la règle, pas la cause, et ne dit pas quoi faire (heuristique de Nielsen 9 et règle « un contrôle désactivé dit pourquoi »). Garder les curseurs visibles, puisqu'ils montrent l'étape suivante, mais remplacer la phrase par « Les curseurs s'ouvrent quand des avatars sont installés : installez d'abord la population IA (ci-dessus). », avec un lien vers `#titre-installation`. Dans chaque carte, « 0 actif sur 0 existant » devient « aucun avatar installé ». Quand la zone n'est pas vide, garder la règle sous une forme plus claire : « Chaque curseur va de 0 au nombre d'avatars installés dans la cohorte. » Une cohorte vide affiche « aucun avatar dans cette cohorte ».
- **Point de doctrine** : un écran vide montre d'abord le premier geste à faire, et jamais un interrupteur qui n'a rien à commander. Un contrôle désactivé dit pourquoi, et ce qui l'activera.

## Avis n°99 — 2026-10-11 — eho, Population IA : exporter / importer les fiches IA
- **Demande** (décision utilisateur) : ajouter à la page Population IA d'eho un bloc pour exporter les fiches (identifiant, nom, groupes, fiche, état IA, lieu) et les réimporter. Le serveur vérifie d'abord sans rien écrire et classe chaque avatar en modifié, inchangé, ignoré ou refusé. `cohorte` et `orientation_initiale` sont protégées, la mémoire n'est jamais importée, une sauvegarde est faite avant. Lu sans rien modifier : `population-ia\page.tsx`, `confirmer.tsx`.
- **Produit** : `AVIS\2026-10-11_EXPORT_IMPORT_IA.md` (R1 emplacement, R2 export, R3 dépôt et vérification, R4 confirmation et sauvegarde, R5 après application).
- **Point de doctrine** : un résultat qu'il faut relire (105 lignes) s'affiche dans la page, pas dans une fenêtre. La règle « fermer au clic extérieur » ferait perdre la relecture. Dans l'écran, on écrit « Vérification » plutôt qu'« essai à blanc ».
- **Remontées** :
  - PLEIADE : en-tête de format dans le fichier ; empreinte d'état entre la vérification et l'application (409) ; dictionnaire de libellés des champs partagé avec la fiche de l'avatar ; si possible, version des fiches chargée par le moteur.
  - CYBERSECU : bornes de taille et de nombre d'entrées ; copie de sauvegarde côté serveur ; journal de l'import ; le fichier exporté contient la mémoire d'exercice et ne doit pas aller aux joueurs.

## Avis n°98 — 2026-10-11 — app-ia : écran du moteur des avatars IA (maquette)
- **Demande** (sur le plan `PLEIADE\PLAN_APP_IA.md`, réponses utilisateur du 11/10 ~17 h 20) : écran de la nouvelle app `app-ia`, réservée à l'Administration, « presque une extension » de la Console. Contenu : interrupteur à double bouton (eho fait foi), état du moteur, journal filtrable, réglages journalisés. Ni validation humaine, ni « lancer un cycle », ni clé ou adresse. Lu sans rien modifier : page Population IA d'eho, `Shell.tsx`, `Dashboard.tsx`, `globals.css`, `pleiade-theme*.css`, `barre-zone.css` d'app-admin ; données du prototype (`etat.json` : 7 417 lignes de journal, `campagnes.json`, formules de crise dans `pont.mjs`).
- **Produit** : `AVIS\2026-10-11_APP_IA\index.html` (autonome, jetons de la Console, clair/sombre `prefers-color-scheme` + bascule) + `AVIS.md` + 11 captures.
- **Contrôle** : Playwright à 1280 px (clair et sombre) et 820 px sur les 3 pages. 0 erreur JS, pas de défilement horizontal. La confirmation se ferme au clic sur le fond, le volet de détail par Échap. Corrigé en cours de route : durée moyenne affichée avec 15 décimales, pastille « nouvelles actions » visible malgré `hidden` (règle `[hidden]` ajoutée), repères du curseur sortant à gauche, barre de 8 types + garde-fous trop chargée (remplacée par un segment de 3 vues et un menu « Types ▾ », règle 37).
- **Point de doctrine** : **un état partagé entre deux apps s'affiche relu** (provenance, fraîcheur, refus en cas de conflit), jamais tel qu'on l'a demandé ; **un réglage s'exprime dans son effet concret** (« 80 messages par heure au plus »), dans la lignée de l'avis n°70.
- **Remontées** : précondition `attendu` (409) et provenance `depuis` pour l'interrupteur d'eho (PLEIADE, CYBERSECU) ; API de journal paginée côté serveur, avec `garde` et `hash/mode` en attributs ; texte d'invite borné (contexte, campagnes). 6 points à trancher (voir l'AVIS).

## Avis n°97 — 2026-10-11 — Tutoriel PLÉIADE : panneau du guide (maquette)
- **Demande** (reprise du chantier tutoriel, décisions utilisateur du 11/10) : maquette statique du panneau de guide hors fiction, ouvert depuis la barre de zone. Contenu attendu : coche au geste détecté, progression par compte, et écran de suivi pour l'animation. Lu : avis n°81 et n°71, `PLEIADE\MEMOIRE.md` § Tutoriel, `PARCOURS.md`, fiches J0-J7 et A1, `DECOR.md`.
- **Produit** : `AVIS\2026-10-11_TUTO_PANNEAU\index.html` (autonome : Archivo depuis Google Fonts, couleurs en oklch, clair et sombre) + `AVIS.md`.
- **Contrôle** : Playwright à 1280 px (clair et sombre) et 820 px. 0 erreur, pas de défilement horizontal. Échap et clic extérieur ferment le guide quand il n'est pas épinglé, la coche part au vrai clic sur l'heure de la publication, le parcours va jusqu'à la fin. Un défaut a été corrigé : une virgule restait dans le résumé du mode Aide.
- **Point de doctrine** : la règle « fermer au clic extérieur » entre en conflit avec un guide qu'on lit pendant qu'on clique dans l'app. **Résolution** : un volet épinglable. Épinglé, il se range à côté de l'app : ce n'est plus une fenêtre.
- **Remontées** : les fiches J0 et J7 parlent d'un « ? du guide » et d'une liste « Premiers pas », à reformuler. La barre de zone n'est montrée aux joueurs ni sur le Social ni sur la presse publique (avis n°71), alors que le guide en a besoin. 6 points à trancher (voir l'AVIS).

## Avis n°96 — 2026-10-10 — Cockpit, Reporting : graphique « par hashtag »
- **Demande** (décision utilisateur) : dans Reporting, un graphique par hashtag. Il reprend les mêmes séries, avec une courbe « Hors séries » en plus. On peut choisir un hashtag ou en additionner plusieurs, et lire en nombres ou en parts (aires empilées à 100 %). Le sélecteur Contenu s'applique aussi. Code lu sans rien modifier : `ReportingView.tsx`, `GrapheTemps.tsx`, `CellulesVues.tsx`, `globals.css`, `api/bff/trending`.
- **Points préalables** :
  - écrire « contenus » et jamais « messages », qui désigne le Chat (avis n°92) ;
  - l'empilement à 100 % reste compatible avec la doctrine du n°75 (lignes en nombres) ;
  - si des séries se recouvrent, les parts dépassent 100 % : elles sont calculées sur la somme des attributions, et une mention le dit (règle de calcul à trancher par PLEIADE/ARCHITECTE).
- **Produit** : `AVIS\2026-10-10_COCKPIT_REPORTING_HASHTAG\AVIS.md`.
  - R1 : un `pl-panel` « Par hashtag » entre Activité et Cellules, ni onglet ni section repliée ; titre qui suit Contenu et la lecture ; Contenu devient un réglage unique pour la page.
  - R2 : saisie (« # » facultatif, tolérante), 12 puces « Tendances du moment » cochables, « Choisis » avec ✕, « n hashtags additionnés — un contenu qui en emploie plusieurs compte une fois », plafond 10, état vide guidé, choix mémorisé par poste.
  - R3 : `ck-vues` « Nombres · Parts (%) ». En Parts : première série sur la ligne de base, Hors séries en haut, en gris hachuré ; la légende met en avant au lieu de masquer ; heure vide = aire interrompue, sans 0 ; bande de volume de 28 px. Alternative à étudier : colonnes à 100 %.
  - R4 : bulle « 15 · 60 % » dans les deux lectures, avec le total de l'heure.
  - R5 : tableau `ck-totaux` Série · Contenus · Part, avec Hors séries et Total distinct.
  - R6 : `<details>` « Voir heure par heure », et navigation au clavier ← → dans `GrapheTemps`, au profit des deux graphiques.
- **Suite** : mise en œuvre par PLEIADE.

## Avis n°95 — 2026-10-10 — eho, planche des joueurs : zones repliables sans casser le glisser-déposer
- **Demande** : reprendre sur la planche des joueurs (`planche.tsx`) le repli des bandeaux de pays fait dans le trombinoscope. Un dépôt sur un bandeau replié range la carte dans la zone. Un survol prolongé ouvre la zone, comme les dossiers à ressort du Finder. Code lu sans rien modifier.
- **Pièges relevés** :
  - glisser-déposer HTML5 natif : replier pendant un glissement démonte la source, et Chrome n'émet alors plus `dragend` ;
  - `dragleave` scintille à cause des boutons contenus dans le bandeau ;
  - pas de bouton dans un bouton, d'où un titre-bouton étendu par un pseudo-élément ;
  - pagination à 60 : un dépôt en fin de bloc serait invisible.
- **Vocabulaire** : on garde « Sans rubrique » (`HORS_RUBRIQUE`), qui existe déjà, au lieu d'introduire « Non classé ».
- **Produit** : `AVIS\2026-10-10_PLANCHE_REPLIABLE\AVIS.md`.
  - R1 : codes du trombinoscope (▶, « · replié », « Tout replier / Tout déplier »), clé `localStorage` par planche.
  - R2 : ouverture après **700 ms**, le liseré de 3 px servant de barre de progression.
  - R3 : anneau ambre, voile, « Lâcher ici → Sans rubrique » ; curseur « interdit » pour une autorité STARTEX vers une autre zone.
  - R4 : la carte se pose en **tête** du bloc « Sans rubrique », et la zone reste repliée.
  - R5 : compteur ×1,15, message de 4 s « Rangé dans Mercure › Sans rubrique · Afficher ».
  - R6 : aucun repli au départ du glissement ; une zone ouverte au survol se referme à la fin si rien n'y a été posé.
  - R7 : le mode sélection reste l'alternative au glisser ; bandeau avec `aria-expanded`.

## Avis n°94 — 2026-10-10 — Social : programmer une publication sans ambiguïté
- **Demande** : avec l'icône horloge, on ne sait pas si « Publier » va programmer ou publier ; l'utilisateur propose un bouton « valider » dans la fenêtre. Le bug serveur (post publié immédiatement) est traité par PLEIADE. Code lu sans rien modifier : `compose.ts` (l. 229-244, 293-300, 949-978), `sidebar.ts`, `pages\scheduled\scheduled.ts`.
- **Constats** (gravité 3) : le calendrier en ligne est lié directement à `scheduledAt`, donc un clic sur un jour programme déjà ; le clic sur le fond ferme la fenêtre en gardant la date et `Échap` n'est pas géré ; le seul signal est la couleur de l'horloge avec une infobulle ; le bouton reste « Publier » avec l'icône d'envoi ; `minScheduleDate` est figé au chargement ; le fuseau n'est pas nommé.
- **Produit** : `AVIS\2026-10-10_SOCIAL_PROGRAMMER\AVIS.md`, modèle X pour tous les habillages (Mastodon web ne propose pas la programmation, son API impose au moins 5 min).
  - R1 : fenêtre avec Date et Heure (24 h, pas de 5 min), phrase « Sera publié le … (heure de Paris) », valeur proposée au prochain quart d'heure, raccourcis facultatifs, boutons **Confirmer** et Annuler. Le clic extérieur et Échap valent Annuler. Refus du passé et de moins de 2 min, minimum recalculé à l'ouverture et à la confirmation, contrôle aussi côté serveur.
  - R2 : bandeau « 🕑 Sera publié le … · Modifier · ✕ », le bouton principal devient **« Programmer »** avec une icône horloge.
  - R3 : annulation par le ✕ du bandeau ou par « Retirer la programmation », sans confirmation ; après l'envoi, depuis Programmés.
  - R4 : notification « Programmé pour le … » avec le lien « Voir dans Programmés » ; la publication n'apparaît pas dans le fil ; si l'heure est passée au moment de l'envoi, on demande « Publier maintenant / Changer l'heure ».
  - R5 : affichage en `Europe/Paris` avec la mention « (heure de Paris) », stockage en UTC.
- **Question ouverte** : heure réelle ou heure d'exercice (D+, JEMM) ?

## Avis n°93 — 2026-10-10 — eho, fiche d'un avatar : relecture de conformité des lots L1-L3 (avis n°91)
- **Demande** : relecture courte de la mise en œuvre locale par PLEIADE (sans schéma). Captures de la fiche d'Isabella Orchkova vue par l'animateur GREYCELL gc10 (1440 px, 390 px, gros plan « Affiché ») ; code lu sans rien modifier : `eho\…\users\[id]\page.tsx` et `api\users\[id]\reel\route.ts`.
- **Produit** : `AVIS\2026-10-10_EHO_FICHE_RELECTURE\AVIS.md`. **Conforme pour l'essentiel** : ordre des couches, étiquettes « qui voit », en-tête (camp lu, bandeau des trois couches, Enregistrer seul, état non enregistré, alerte au départ), Réel en lecture refusé aux joueurs, libellés renommés, champs vides repliés, aperçu du profil, IA à l'état vide, Rangement par famille avec 🔒 avant le refus, Supprimer relégué.
- **5 corrections retenues avant mise en ligne** : (1) sélecteur de fichier natif en anglais et tronqué → bouton « Choisir une image… » (gravité 2) ; (2) téléphone : sommaire absent et en-tête collant trop haut → seule la ligne nom + Enregistrer reste collante, sommaire horizontal défilant (2) ; (3) Catégorie restée en texte libre → liste fermée tirée de `lib/trombinoscope.ts`, une valeur hors liste reste affichée comme telle (2) ; (4) « se change dans Rangement » → « (Administration seulement) 🔒 » quand c'est verrouillé (1) ; (5) biographie interne à hauteur automatique, de 5 à environ 15 lignes (1).
- **Non retenus** (gravité 1) : « Voir sur le réseau ↗ » et menu « ⋯ » absents, liste Certification trop large, bouton Enregistrer désactivé peu contrasté, segment « Affiché » du bandeau redondant jusqu'au lot 4.

## Avis n°92 — 2026-10-10 — Hashtags dans les commentaires : page d'un hashtag (Social) et Tendances (Cockpit)
- **Demande** : décision utilisateur du 10/10, un commentaire compte autant qu'une publication pour les tendances et le compteur d'un hashtag ; dans le Cockpit, afficher « #X : 120, dont 45 en commentaires ». Code lu sans rien modifier : `hashtag.ts`, `profile.ts` (carte Réponse), `right-panel.ts`, `Sections.tsx` (`TrendingSection`), `TootItem.tsx`.
- **Produit** : `AVIS\2026-10-10_HASHTAGS_COMMENTAIRES\AVIS.md`.
  - **Social** : liste unique mêlée par date, comme le fil de hashtag de Mastodon et la recherche « Récent » de X (règles 15, 34). Les commentaires reprennent la carte « Réponse » du profil, avec trois retouches : extrait du post parent sur 2 lignes, #hashtags et @mentions rendus en liens (aujourd'hui texte brut), gabarit aligné sur `post-card`. Libellé gardé : **« N publications »**, pas « messages » (confusion avec le Chat, règle 36). Même total dans le panneau Tendances de droite. Aucun détail côté joueurs. Plus tard : « N publications · M participants ».
  - **Cockpit** : juste après le total, un second nombre atténué « ↩45 » (icône `MessageCircle` ou `Reply` en 11 px, mono 0,68 rem `ink-faint`), séparé des compteurs par réseau par un filet d'1 px, masqué à 0. `aria-label` et `title` « #X : 120 publications, dont 45 en commentaires ». Légende ajoutée une fois sur la ligne « Depuis le… ». La somme par réseau doit inclure les commentaires. Colonnes de veille : étiquette « commentaire » et bandeau « en réponse à » suffisants ; facultatif, surligner le #tag ; pas de filtre supplémentaire.

## Avis n°91 — 2026-10-10 — eho, fiche d'un avatar : architecture de l'information (réel / personnage / affiché / IA)
- **Demande** : la fiche d'un avatar « n'est pas claire, on ne sait pas quelle partie correspond à quoi » ; distinguer la réalité physique (qui tient le compte, où), l'identité déclarée sur le réseau social, le persona, une future section « Comportement IA » (projet `PLEIADE\PROJET_AVATARS_IA.md`) et les groupes. Captures 93-94 (@LoloAnna) ; code eho lu sans rien modifier (`users\[id]\page.tsx`, `schema.prisma`, `eho-joueur.ts`, `droits-avatars.ts`, `usage-avatars.ts`, `rangement-groupes.ts`), plus `app-social\…\auth.ts` et `app-admin\…\kit-ia.ts`.
- **Produit** : `AVIS\2026-10-10_EHO_FICHE_AVATAR\AVIS.md` — 10 constats ; 3e couche « Personnage » **confirmée** ; ordre réel → personnage → affiché → IA → rangement → technique, page longue à sommaire collant (pas d'onglets : on compare les couches, règle 34) ; couleur + pictogramme par couche (ardoise `Fingerprint` / sarcelle `Lock` / ambre `Eye`, déjà utilisé pour « visible des joueurs » / fuchsia `Bot`), rouge-bleu réservés au camp ; en-tête : nom, @ copiable, camp lu par `campDepuisGroupes` (alerte 0 ou 2+ camps), statut IA, **bandeau des trois couches**, Enregistrer seul, e-mail et UUID relégués ; section affichée avec **aperçu du profil joueur** ; groupes : membres seuls, par famille (Allégeance en choix unique / Cellules 🔒 / Exercices / Classement / Archivés).
- **Champs ambigus** : `pays` = vérité de la fiction (comparaison, trombinoscope, STARTEX) → renommé à l'écran, **nouveau « Lieu affiché »** sans déduction ; `label` → « Catégorie (trombinoscope) » en liste fermée ; `langage` → « Registre et ton » + **nouvelle « Langue de publication »** ; `qualifications` → nouvelle « Source de la fiche » ; aucune colonne renommée.
- **Constats transmis** : M9 CYBERSECU toujours ouvert (API complète aux participants) ; le réseau social recopie tous les champs du personnage dans sa base (`auth.ts` l. 66-80) ; **bug probable** `campDe` (kit IA) qui prend le 1er groupe « CAMP … » (peut rendre « div1 ») → ARCHITECTE. « CAMP » a 3 sens (allégeance / cellule / partage).
- **11 questions** à l'utilisateur ; plan L1-L6 (L1-L3 sans changement de schéma).

## Avis n°90 — 2026-10-09 — Social, Chat : séparer les conversations de la liste
- **Demande** : « un petit trait entre les conversations ? » + capture 92 (liste `.conv` padding 12×16, aucun séparateur ; sous-liste `.sous-boite` 7×6 déjà groupée par un rail gauche de 2 px). Code lu sans rien modifier.
- **Avis** : **oui, pour la liste des conversations seulement** — 6 lignes de même gris se lisent comme un bloc. Trait `1px solid var(--masto-border)` **en retrait aligné sur le texte** (`.conv { position: relative }` + `::after { left: 68px; right: 0; bottom: 0 }`, 68 = 16 padding + 42 avatar + 10 gap), absent sur la dernière ligne, masqué sous la ligne active et survolée (le fond suffit). Pas de trait pleine largeur (bruit), pas d'espacement supplémentaire (la liste s'allonge). **Sous-liste des Boîtes : ne rien ajouter** — le rail et le padding serré suffisent (proximité). Inchangés : survol, fond actif + bord droit accent, pastilles, gras non-lu — règles 9, 5, 23 ; REF-07, REF-06 (Jakob : X/Messenger), REF-12.

## Avis n°89 — 2026-10-09 — Social : rendre la lecture des messages du Chat plus agréable
- **Demande** : « est-ce qu'on ne peut pas faire un truc pour que l'affichage des messages soit plus agréable à lire esthétiquement ? » + capture (habillage par défaut « mastodon »). Code lu sans rien modifier : `pages\chat\chat.ts`, `components\boites-animation\boites-animation.ts`, `components\layout\mastodon-layout.ts` (grille `240px 1fr 300px`, max 1200 px) et `twitter-layout.ts` (colonne centrale **figée à 600 px**), `components\right-panel\right-panel.ts`, jetons `styles.scss`.
- **Diagnostic chiffré** : colonne centrale ≈ 660 px − liste 340 px = **≈ 320 px de conversation** (X : 600 px − 340 = 260 px). Bulle reçue `--masto-panel-light` **#f0f3f7** posée sur `.masto-main` = `--masto-bg` **#f2f5f9** → contraste bulle/fond **≈ 1,01 : 1** (la bulle n'existe pas visuellement ; règle 23 couches). Texte blanc sur `--masto-accent` #6364ff = **4,4 : 1** (< 4,5 AA, règle 21) ; X #1d9bf0 = 3,0 : 1, Facebook #1877f2 = 4,2 : 1. L'image hérite de `.bulle` (padding 9×14 + fond accent) → cadre violet épais. Heure `.72rem` ≈ 11,5 px en « timeago » (« 1h ») sous **chaque** message ; aucun séparateur de jour ; aucun avatar côté reçu ; « Boîtes de mes avatars » ≈ 95 px de haut même vide.
- **Recommandations, par effet sur le confort de lecture** :
  1. **Largeur** (gain n°1) — sur `/chat`, **masquer le panneau de droite** comme X sur Messages : grille `240px 1fr` (classe posée par le layout selon la route) → conversation ≈ 620 px. « Au nom de » ne doit pas disparaître pour l'animation : le reprendre en **pastille compacte « Au nom de @avatar ▾ »** dans `.liste-tete`, qui ouvre l'`impersonation-switcher` existant en menu déroulant (fermeture clic extérieur + Échap, règle du 09/10). Repli moins coûteux : sur `/chat`, ne garder que la carte « Au nom de » et ramener le panneau à **260 px**. Habillage X : libérer la colonne figée de 600 px sur `/chat` (`275px 1fr`). Liste ramenée à `minmax(240px, 300px)`. Bulles : `max-width: min(70%, 520px)` (≈ 60-65 caractères à 15 px) — Jakob REF-06, règle 8/26 REF-07/REF-17, règle 38 (liste-détail) REF-23.
  2. **Fond et bulles** — `.conversation { background: var(--masto-panel) }` (blanc) pour que la bulle reçue se détache ; bulle reçue `background: color-mix(in srgb, var(--masto-text) 7%, var(--masto-panel))` (≈ #ececed, lisible dans les 5 habillages) ; bulle envoyée sur `--masto-accent-hover` (#5253e0 → **5,7 : 1**, AA) dans l'habillage mastodon. Habillages X/Facebook : la couleur de marque prime (illusion, §1) — **tension à trancher par l'utilisateur**. Texte 15 px, interligne 1,4, padding 8×12, rayon 18 px — règles 21, 23, 26 ; REF-13, REF-12, REF-07.
  3. **Regroupement** — messages consécutifs du même auteur à moins de 5 min : écart **2 px** dans le groupe, **12 px** entre groupes ; coins « queue » (rayon 4 px) seulement sur le **dernier** message du groupe, coins intérieurs 6 px pour les autres ; **avatar 28 px** devant le dernier message reçu du groupe (espace réservé de 28 + 8 px pour aligner les autres) — proximité règle 9, REF-06/REF-07 ; Jakob (Messenger/X).
  4. **Images** — sortir l'image de la bulle colorée : `padding: 0; background: none` quand le message est une image seule ; `border-radius: 16px`, `max-width: min(100%, 320px)`, `max-height: 360px`, `object-fit: cover`, fine bordure `1px solid var(--masto-border)` ; légende éventuelle dans une bulle séparée dessous ; agrandissement déjà en place (ajouter Échap + focus, règle 11) — REF-07 (atténuer le cadre), REF-19.
  5. **Horodatage** — séparateurs de jour centrés « Aujourd'hui » / « Hier » / « jeudi 8 octobre » (12 px, `--masto-text-secondary`, marge 16 px) ; heure **HH:MM** (pas « 1h ») **sous le dernier message d'un groupe seulement**, **12 px** (`.75rem`, plancher de lisibilité) ; date et heure complètes en `title` au survol (élément `<time datetime>`) ; côté envoyé, « Vu » éventuel au même endroit — règle 25 (état visible) REF-14, règle 26.
  6. **En-tête de conversation** — nom + @ de l'interlocuteur à gauche ; **en animation seulement**, rappel discret « vous écrivez au nom de @OlamaoOfficiel » (12 px, sous le nom ou à droite, avec photo 20 px) : le risque n°1 est d'écrire sous le mauvais avatar — Nielsen 1 et 5 (REF-14), règle 25.
  7. **Zone de saisie** — `<textarea>` qui grandit de 1 à **5 lignes** (puis défile), **Entrée envoie, Maj+Entrée** saut de ligne, rayon 20 px, compteur seulement au-delà de 1 800/2 000 ; fond `--masto-panel` — Jakob REF-06, REF-13 (3.3.2 étiquette conservée).
  8. **« Boîtes de mes avatars » vide → une seule ligne** (≈ 36 px) : « Boîtes de mes avatars · aucun message à traiter » + interrupteur Alertes ; la note explicative passe dans un « ? » ou un `title`. Dépliée seulement s'il y a des non-lus — règle 37 (Hick), règle 5 (atténuer), REF-21 révélation progressive.
  9. **États vides** — garder « Commencer une conversation » ; dans une conversation sans message, carte centrée avec photo 64 px + nom + @ de l'interlocuteur au-dessus de « Début de votre conversation » (modèle X) — règle 18 Peak-End, REF-06.
- **Complément (même jour, question « rabattre le menu comme X »)** : **oui**. Sur `/chat`, menu de gauche en **rail de 64 px** (on réutilise l'état déjà prévu sous 960 px dans `mastodon-layout`) : icônes 24 px dans des cibles 48 px, **infobulle avec le libellé** (et `aria-label`), **pastilles conservées**, bloc compte réduit à l'avatar 32 px en bas (« Animation · au nom de @… » dans son infobulle). **Retour automatique** au menu complet quand on quitte `/chat`, **sans bouton manuel** (un seul comportement à mémoriser ; règle 28, Jakob REF-06). Combiné à la R1 : rail 64 + liste 300 + conversation, sans panneau de droite, « Au nom de » en pastille dans l'en-tête de la liste. Conversation ≈ **836 px** à 1366 comme à 1920 px (grille plafonnée à 1200 px ; avec la R1 seule : ≈ 660 px). Les bulles restent plafonnées à 520 px.
- **Effort** : 1-2 (CSS + layout) ; 3 (regroupement, séparateurs : calcul côté composant) ; 5 et 7 faibles ; 6 et 8 faibles. Rien poussé, rien modifié dans `app-social`.

## Avis n°88 — 2026-10-09 — Social : avertir l'animateur qu'un de ses avatars a reçu un message privé
- **Demande** : « que l'animateur puisse avoir une notif, peut-être dans l'onglet Chat, pour l'avertir que tel avatar a reçu un message », pour tous les avatars qu'il peut incarner (des dizaines, parfois 100+, partagés entre animateurs ; « lu » partagé). Code lu sans rien modifier : `app-social\apps\web\src\app\pages\chat\chat.ts` (liste | conversation, modèle X ; sans avatar incarné, page vide « Choisissez un avatar dans « Au nom de »… »), `components\sidebar\sidebar.ts` (pastille `chat.nonLus()` = avatar incarné seul, relue toutes les 30 s par `services\chat.service.ts`), `components\impersonation-switcher` (« Au nom de » / « Redevenir moi »). Les joueurs incarnent aussi (avatars de leur camp, `peutIncarner`).
- **(1) Combinaison recommandée, trois étages de force croissante** (Nielsen 1, Hick, Von Restorff règle 20) : **a. pastille cumulée sur « Chat »** = total des non-lus des boîtes signalées (filtre ci-dessous), plafonnée à « 99+ » ; **b. section « Boîtes de mes avatars » en tête de la colonne de gauche de Chat**, au-dessus des conversations de l'avatar incarné, ne listant **que les boîtes avec des non-lus**, triées du plus récent au plus ancien, 8 lignes puis « Voir les {n} autres boîtes » ; une ligne = photo + nom + @avatar + pastille du nombre, 2e ligne « @expéditeur : extrait » + « il y a 2 min ». Sans avatar incarné, cette section **remplace** l'état vide actuel (elle devient le point d'entrée naturel). **c. toast** seulement pour un message **arrivé depuis le dernier relevé**, hors page Chat (là, la section se met à jour seule), jamais pour un message envoyé depuis son propre compte, **au plus un toast toutes les 30 s, regroupé** au-delà d'un message ; désactivable. Pas de son.
- **(2) Clic** (ligne de la section ou bouton du toast) : **incarner @X et ouvrir `/chat/@Y` en un geste**, en le disant : annonce « Vous agissez maintenant au nom de @X. » et rappel permanent **« Au nom de @X »** dans l'en-tête de la conversation (le risque n°1 est de répondre avec le mauvais avatar). Si un message est en cours de saisie dans une autre conversation : confirmation « Abandonner le message en cours ? » (Nielsen 5). Ouvrir la conversation la marque lue pour toute l'animation, donc le dire une fois dans la section : « Ouvrir une conversation la marque lue pour toute l'animation. »
- **(3) Bruit** : un segmenté **« Signaler : Mes avatars du jour · Toute ma cellule »**, qui gouverne la pastille, la section et les toasts ensemble (un seul réglage, règle 33). Défaut **« Mes avatars du jour »** (avatars incarnés par ce compte depuis 0 h) : à 100 avatars, « toute la cellule » donnerait une pastille toujours haute, donc ignorée. État vide qui renvoie à l'autre choix (règle 18). Le « lu » partagé dédoublonne déjà entre animateurs : une boîte ouverte par un collègue disparaît chez tous. Mémorisation du choix par compte. Interrupteur « Alertes de messages : Activées / Désactivées » à côté du segmenté (toasts seulement ; pastille et section restent).
- **(4) Libellés exacts** : pastille, nom accessible « Chat, {n} messages non lus pour {k} de vos avatars » ; section « Boîtes de mes avatars » ; segmenté « Mes avatars du jour » · « Toute ma cellule » (joueur : « Tous mes avatars », sans segmenté s'ils sont peu nombreux) ; ligne « {Nom} @{x} » / « @{y} : {extrait} » ; « Voir les {n} autres boîtes » ; vide : « Aucun message en attente pour vos avatars du jour. » + lien « Voir toute la cellule » ; toast simple « @{x} a reçu un message de @{y} » + extrait sur une ligne + bouton « Répondre au nom de @{x} » ; toast groupé « {n} nouveaux messages pour {k} de vos avatars » + bouton « Voir les boîtes » ; sans avatar incarné, sous-titre « Choisissez une boîte, ou un avatar dans « Au nom de ». »
- **(5) Joueur** : le même mécanisme, limité aux avatars de son camp (il peut déjà les incarner : aucune information nouvelle), libellés « Tous mes avatars ». Rien de propre à l'animation (pas d'autre cellule, pas d'origine). Lecture seule et Modération : rien.
- **(6) Accessibilité** : toast dans une région `role="status"` `aria-live="polite"` présente dans le DOM dès le chargement, **sans prise de focus**, affichée au moins 8 s, en pause au survol et au focus, fermable (« Fermer » + Échap), sans animation si « réduire les animations ». **Pas d'`aria-live` sur la pastille** (une annonce toutes les 30 s = bavardage, cf. n°87) ; pastille doublée par le nom accessible (règle 10). Lignes de la section = liens au nom complet « Ouvrir la boîte de @{x} : {n} non lus, dernier message de @{y} ». Cibles ≥ 24 px.
- **Hors du champ de DESIGNER** : point d'API agrégé (non-lus par avatar incarnable, relevé 30 s, 100 avatars × plusieurs animateurs) et trace « incarnés aujourd'hui » (serveur plutôt que localStorage, pour suivre l'animateur d'un poste à l'autre) → ARCHITECTE/PLEIADE ; filtrage strict par avatars réellement incarnables (aucune fuite entre cellules ou camps) → CYBERSECU.

## Avis n°87 — 2026-10-09 — Cockpit Reporting : mode « En direct » sans clic
- **Demande** : avec « jusqu'à maintenant », le graphique et « Publications par cellule » doivent se mettre à jour seuls ; renommer « Actualiser » (l'utilisateur suggère « Synchroniser »). Animateurs, écran laissé ouvert. Code lu sans rien modifier (`app-cockpit\src\components\ReportingView.tsx` : lien « jusqu'à maintenant » visible seulement quand la fin est figée, `run()` déjà calé sur `toMaintenant`).
- **(1) Contrôle** : remplacer le lien par un segmenté `.ck-vues` (radiogroup, `aria-label="Fin de la période"`) placé juste après le champ « À » : **« En direct » · « Figée »**, défaut En direct. Infobulles : En direct → « La fin suit l'heure actuelle ; le graphique se met à jour tout seul chaque minute. » ; Figée → « La fin reste à la date choisie ; le graphique ne change plus. » Le lien caché/affiché viole la stabilité (règle 28) et ne dit pas l'état (règle 25). **Modifier « À » fait passer en Figée** sans confirmation (geste explicite, réversible d'un clic). Modifier « De » en direct reste en direct et recalcule après la saisie (au `blur` ou 800 ms sans frappe).
- **(2) Cadence** : **60 s** (barres horaires : plus fin n'apporte rien et charge les BFF ; 30 s au plus bas). Ne pas lancer un appel si le précédent tourne. Mise à jour **en arrière-plan** : anciennes données affichées jusqu'à l'arrivée des nouvelles, remplacement d'un coup, **pas d'animation Recharts** au rafraîchissement (`isAnimationActive={false}`), séries masquées et survol conservés, pas de spinner ni de grisé. Indicateur à côté du segmenté : **● « En direct · mis à jour à 13:42 »** (point vert doublé du texte, règle 10). Échec : **« ⚠ Mise à jour impossible (13:43) — nouvel essai dans 1 min »** en ambre, dernières données gardées ; après 3 échecs : « Dernière mise à jour réussie : 13:40 ». Figée : « Période figée ».
- **(3) Bouton** : il sert surtout à appliquer De / À / groupes → **« Recalculer »** (icône refresh) en Figée, bouton secondaire. « Synchroniser » déconseillé : rien n'est synchronisé entre systèmes, le mot promet autre chose (Nielsen 2). En direct : remplacé par une **icône seule** refresh, `aria-label` et infobulle « Mettre à jour maintenant », à côté de l'indicateur (garde le contrôle sans concurrencer, règles 6 et 37).
- **(4) Onglet caché** : pause sur `visibilitychange` ; au retour, mise à jour immédiate si la dernière date de plus de 60 s, puis reprise de la cadence.
- **(5) Accessibilité** : **pas d'`aria-live` sur l'heure** (une annonce par minute = bavardage) ; `aria-live="polite"` seulement sur le passage En direct ↔ Figée et sur l'apparition/disparition d'une erreur. Heure dans un `<time>`. Segmenté au clavier (flèches, REF-19).
- **Hors du champ de DESIGNER** : charge réelle des BFF (`stats-cellules`, `reporting`, membres eho à chaque passage) à 60 s avec plusieurs animateurs → ARCHITECTE/PLEIADE ; la mémorisation localStorage de `toMaintenant` existe déjà et reste valable.

## Avis n°86 — 2026-10-09 — Cockpit Reporting : sélecteur de contenu du graphique par série
- **Demande** : le graphique « Publications par heure, par série » (`app-cockpit\src\components\ReportingView.tsx`) ne compte que les posts ; il doit compter aussi commentaires et reposts (y compris ceux des scénarios). Vocabulaire Social : publication / commentaire / repost / J'aime. Code lu sans rien modifier.
- **(1) Sélecteur** « Contenu », même composant `.ck-vues/.ck-vue` (radiogroup) que « Dans le temps » : **Tout · Publications · Commentaires · Reposts**, défaut **Tout** (la demande est justement de tout compter ; ordre = du contenu d'origine vers ses dérivés). Pas de « J'aime » en v1 (un J'aime n'est pas une prise de parole ; à ajouter seulement si demandé, après les reposts).
- **(2) CellulesVues** : oui, aligner (« Tweets » → « Publications », « Réponses » → « Commentaires » ; aussi la vue « Par type » et le commentaire d'en-tête « Tweets, pas Posts » qui devient « Publications »). **Maintenant, dans le même lot** : deux sélecteurs voisins sur la même page avec deux vocabulaires = incohérence directe (règle de cohérence, Jakob/consistance). « Reposts » à y ajouter si la donnée existe ; sinon libellés seuls.
- **(3) Titre** (« Publications » devient ambigu : c'est aussi un type) : Tout → « Activité par heure, par série » ; Publications → « Publications par heure, par série » ; Commentaires → « Commentaires par heure, par série » ; Reposts → « Reposts par heure, par série ». Sur-titre `pl-eyebrow` : « Activité par heure ». **Aide** : Tout → « Publications, commentaires et reposts des avatars de chaque série, sur tous les réseaux de la zone, du {début} au {fin}. Les J'aime ne sont pas comptés. Survolez pour lire les valeurs ; cliquez une série pour la masquer. » ; type seul → « {Publications | Commentaires | Reposts} des avatars de chaque série, sur tous les réseaux de la zone, du {début} au {fin}. Survolez… masquer. »
- **(4) Tableau** : une colonne par type **+ Total** (Série · Publications · Commentaires · Reposts · Total), quel que soit le choix ; la colonne du type choisi (ou Total si « Tout ») en gras. Le tableau sert la comparaison exacte que le graphique ne donne pas ; 4 nombres restent lisibles. Repli si la largeur manque (mobile) : seulement la colonne du choix.
- **(5) Reposts des scénarios** : oui, une phrase ajoutée à l'aide quand Tout ou Reposts est choisi : « Les reposts comprennent ceux joués par les scénarios de l'animation. » (vocabulaire « animation », jamais « Admin »).

## Avis n°85 — 2026-10-09 — Social : repère d'origine des publications (animation seulement)
- **Décision utilisateur : variante A**, couleurs posées sur PLÉIADE (palette fermée de 10 + « Aucune »), repère masqué par défaut. **Appliqué en local** (Social `9ab1106`, PLÉIADE `d03f232`, MELMIL `7682d40`, Console `7548295`), maquette `index.html` + captures `captures\` (social_affiche.png, pleiade_groupes_palette.png, melmil_incident_*.png). Écarts : interrupteur placé sous « Au nom de » (présent dans tous les habillages) ; rappel « visible de l'animation seulement » sous l'interrupteur plutôt qu'en tête du fil.
- **Demande** : repère activable montrant d'où vient un post, un commentaire ou un repost (groupe + compte réel pour un joueur ; cellule + compte pour un animateur ; scénario → console et incident → MELMIL, cliquables). Avis : `AVIS\2026-10-09_SOCIAL_ORIGINE\AVIS.md`. Code lu sans rien modifier.
- **Constat** : `SocialPost` n'a que `parAnimation` : ni compte réel, ni groupe, ni scénario, ni incident stockés → préalable PLEIADE/MASTORION ; données servies à l'animation et l'administration seulement (CYBERSECU), jamais masquées en CSS.
- **3 variantes** : A ligne d'origine de 24 px au-dessus de la carte + trait gauche de 4 px (même signe que MELMIL, avis n°43) ; B cadre coloré + étiquette ; C pastille + détail au clic. **Recommandée : A** (lisible sans clic, carte habillée intacte). Textes : `Joueur · DIV 1 · dv01`, `Animation · GREYCELL · anim03`, `Scénario · GREYCELL · <scénario ↗> · Incident 07.01.I03 ↗`, `… · Storyline 07-02`, `… · Bruit de fond`, `Origine inconnue` (repli ardoise en pointillés).
- **Interrupteur** « Origine des publications » (Affichée / Masquée), barre animation de Social, mémorisé par poste, masqué par défaut, absent en vue « comme un joueur » ; couleurs dans une liste ▾ ; pas de filtre en v1 (cockpit, règle 33). 8 questions ouvertes.

## Avis n°84 — 2026-10-09 — Console : message privé, lieu, sondage, qui peut répondre
- **Appliqué et poussé le 2026-10-09** (`app-admin` `cc1de4c` + `5a236bf` : fond opaque de la liste des lieux, défaut signalé par l'utilisateur) : segmenté de type, Destinataire, Média/Sondage en barre (l'un grise l'autre + raison), sections repliables « Options de la publication » et « Engagement simulé » avec résumé, Lieu en combobox à recherche obligatoire (Échap ferme la liste sans fermer la fenêtre), résumé d'erreurs GOV.UK relié aux champs, marques ✉ 📊 📍 🔒 doublées d'un mot (2 + « +n ») dans l'arbre et la table. Écart : durée du sondage en champs j/h/min (pas de liste) ; marques en emoji + mot plutôt qu'icônes Lucide (cohérent avec les ♥ ↻ existants de l'arbre). Captures : `scratchpad\console\`.
- **Demande** : intégrer dans la fenêtre « Nouvelle publication » (`app-admin`, `ItemDialog.tsx`, lu sans rien modifier) un type « Message privé » et, sur une publication, Lieu (≈ 2 300 communes en « H… »), Sondage (2 à 4 choix, 25 car., 5 min à 7 j, exclusif du média) et « Qui peut répondre » ; libellés Likes / Reposts. Avis rendu en session, sans dossier d'avis.
- **Constat** : l'ordre actuel (App cible, Persona, Titre, Message, Répond à, Cite, Likes/Retweets, Média) déroule déjà 8 blocs ; en ajouter 4 de plus à plat noie le geste principal (persona + texte) — Hick (REF-06), règles 6, 32 et 37.
- **Recommandé** : (1) un **segmenté de type en tête** « Publication · Réponse · Message privé » (3 options exclusives et visibles, Jakob REF-06), qui fait apparaître seulement les champs du type ; « Réponse » rend « Répond à » obligatoire en 2ᵉ position, « Message privé » remplace la cible par « Destinataire » (avatar, recherche) et retire Lieu, Sondage, Qui peut répondre, Likes/Reposts ; (2) ordre : Type → App → Persona (expéditeur) → [Destinataire / Répond à] → Message → Média ou Sondage → section repliable **« Options de la publication »** (Lieu, Qui peut répondre, Cite) → section repliable **« Engagement simulé »** (Likes ♥, Reposts) ; chaque section repliée affiche son résumé (« 📍 Hxxx · Comptes suivis ») et s'ouvre d'office si elle contient une valeur ou une erreur (2 niveaux de révélation, règle 32, REF-21) ; (3) Média et Sondage = **deux boutons d'une même barre d'outils** sous le message, à la manière de X (Jakob) : ajouter l'un grise l'autre avec la raison en infobulle et en texte (« Retirez le média pour ajouter un sondage »), plutôt qu'une erreur après coup (Nielsen 5, REF-14) ; (4) Lieu = **combobox avec recherche obligatoire** (modèle Combobox APG, REF-19), 20 résultats au plus, aucune saisie libre acceptée : la valeur ne peut être que dans la liste, erreur « Choisissez une commune de la liste » si le texte tapé ne correspond à rien ; « Qui peut répondre » = liste à 4 valeurs, défaut « Tout le monde » affiché ; (5) sondage : compteur « 12/25 » par choix, bouton « + Ajouter un choix » masqué à 4, durée en jours/heures/minutes bornée ; résumé d'erreurs GOV.UK en tête de fenêtre au clic sur Enregistrer, chaque erreur reliée à son champ (règle 24, REF-10) ; (6) arbre et timeline : une **icône Lucide doublée d'un mot ou d'une infobulle** (règle 10) : `Mail` message privé, `MapPin` lieu, `ChartBar`/`ListChecks` sondage, `MessageSquareLock` réponses restreintes ; au plus 2 pictos par ligne + « +1 » pour ne pas saturer la ligne. Toutes les listes (combobox, groupes, sélecteurs) se ferment au clic extérieur et à Échap (règle maison, règle 11).
- **Hors du champ de DESIGNER, à trancher** : le comportement réel côté Social (le message privé apparaît-il au joueur destinataire seulement ?), la durée minimale du sondage par rapport au rythme de l'exercice, et la visibilité des Likes en vue joueurs (rappel en cours).

## Avis n°83 — 2026-10-08 — Social : fil de réponses infini

## 2026-10-08 — Avis n°82 — Social : qui a réagi
- **Demande** : sur `app-social`, voir qui a liké, qui a partagé, et la liste des citations avec leur contenu (joueurs et animateurs). Avis rendu en session, aucun code ni dossier d'avis.
- **Constat** : les compteurs sont collés aux boutons d'action. Si le même clic sert tantôt à agir, tantôt à voir la liste, l'action devient ambiguë et on like par erreur (Nielsen 4 cohérence et 5 prévention, REF-14 ; Fitts, REF-06).
- **Recommandé** : (1) la barre d'actions reste « clic = action » ; (2) sur la page Publication, une **ligne de statistiques** au-dessus de la barre (« 12 partages · 3 citations · 40 favoris »), chaque segment étant un vrai `<button>` qui ouvre la liste (Jakob, REF-06 : c'est le geste de X/Twitter et de Mastodon) ; (3) une **fenêtre à 3 onglets** « Favoris (n) / Partages (n) / Citations (n) », ouverte sur l'onglet cliqué, qui réutilise la fenêtre « Partagé par » existante (règles 33 et 34 : un seul chemin, 3 sections bien nommées) ; elle devient plein écran sous 600 px ; (4) les profils en lignes avatar · nom · @ cliquables vers le profil, les citations en cartes compactes (texte en entier, sans barre d'actions) ; (5) pour les longues listes, le total en tête, une pagination par « Afficher plus » (20 à 40) plutôt qu'un défilement infini, une recherche par nom au-delà d'environ 50 ; (6) un état vide qui dit les choses (« Aucune citation pour l'instant », règle 18) ; un onglet à 0 reste visible mais grisé (règle 28, stabilité). Pour l'accessibilité : un `aria-label` explicite sur chaque compteur, le modèle Dialog + Tabs de l'APG (REF-19, règle 11) et des cibles de 44 px en tactile (règle 12).
- **Hors du champ de DESIGNER, à trancher** : l'emplacement exact de la ligne selon chaque habillage (charte fidèle), le bandeau « Partagé par » du fil, et la visibilité des favoris pour les joueurs (voir le rappel « likes invisibles en vue joueurs » ; CYBERSECU E8).

## 2026-10-08 — Avis n°81 : Tutoriel guidé PLÉIADE — conception
- Avis oral (aucun code, aucun fichier d'avis). Recommandation : aide tirée par rôle et par zone (checklist « Premiers pas » générée depuis les instances déployées + « ? » contextuel + états vides) ; **zone d'entraînement** sur données fictives pour la formation avant exercice ; guide incarné **optionnel**, cantonné à l'accueil du portail, jamais dans le flux d'animation. Rejetés : visite imposée, modales bloquantes, leviers ludiques. Sources : REF-25, REF-24, REF-21, règles 28, 35, 39, 40. 6 questions ouvertes remises à l'utilisateur.

## 2026-10-08 — Avis n°79 : orchestrateur PLÉIADE, page « Zones » (maquette)
- **Demande** : refondre le rangement de la page Zones (instances mêlées, presse éparpillée, exercices annuels et éditions successives, recherche par nom ou année, LEAC = prototype). Maquette à garder en localhost.
- **Produit** : `AVIS\2026-10-08_PLEIADE_ZONES\AVIS.md` (13 constats, R1-R9, modèle de données `famille` / `exercice` / `annee` + `archivee_le`, plan, 5 questions) et `index.html` (maquette interactive, port 3853 via `python -m http.server 3853 --bind 127.0.0.1` depuis le dossier). Captures avant/après dans `captures\`.
- **Contrôle** : Playwright à 1440 et 390 px, recherche « lattre », « 2026 », « tf1 », création d'une zone, erreurs, menus, archivage : 0 erreur JS, 0 image cassée. 3 défauts vus aux captures et corrigés (choix de famille sans marge intérieure, segmenté DEV/PROD écrasé par `.champ label`, identifiant proposé `de-lattre-28` au lieu de `delattre-28`).
- Code `pleiade-platform` lu en lecture seule ; rien modifié dans `C:\CECPC\pleiade\`.

## 2026-10-07 (suite) — Avis n°77 : relecture avant push (branche `coherence-77`)
- 7 décisions conformes (c01 à c08). 2 points bloquants : le titre de l'éditeur disparaît à 390 px (`PageHeader` en `flex-1`, une régression) ; 3 fichiers du socle non suivis par git. 3 retouches pour plus tard : la date dans le journal, l'accent de « supprimé », le journal vide en démo. Détail : AVIS.md §7.

## 2026-10-07 — Avis n°77 : app-admin, cohérence de toutes les pages (menu et charte)

- **Demande** : l'utilisateur, devant la liste et l'éditeur en production, demande que toutes les pages aient le même menu et une charte cohérente ; analyser aussi les autres pages.
- **Matière** : captures 52 et 53 (production), p01 à p14 (local : tableau de bord, scénarios, supervision, aide, 4 onglets de l'éditeur, dialogue, nouveau scénario, scénario terminé, mobile 390 px) ; code lu sans rien modifier (`globals.css`, `pleiade-theme.css`, `editor.css`, `Shell.tsx`, `ScenariosList`, `Dashboard`, `Monitoring`, `ScenarioEditor`, `TreeView`, `ConfigPanel`, `EtatTag`, `lib/etats.ts`, pages).
- **Constat** : le menu est commun aux 5 pages (`Shell`) ; ce qui diverge, c'est le contenu. 26 incohérences inventoriées : filtres en 3 styles (dont 2 classes recopiées et 3 segmentés identiques), crème plein partagé entre action principale et filtre actif, 3 familles d'étiquettes, « non partie » dit de 6 façons, « publication » au masculin, en-tête de l'éditeur à part, 2 largeurs (le bord saute de 26 px), journal mono/sans, débordement mobile de l'éditeur.
- **Proposé** : socle commun (gabarit `PageHeader` étendu, `BarreFiltres`, `Etiquette` unique, règle de vocabulaire, fusion de classes) ; plan en 7 étapes, les étapes 1 et 2 (mots, étiquettes) faisables pendant DELATTRE 26 ; 6 décisions soumises à l'utilisateur.
- **À vérifier** : la barre de zone et le menu n'apparaissent pas sur les captures de production (cadrage, ou version antérieure à l'avis n°71).
- **Doctrine dégagée** : un composant par geste, une table par vocabulaire ; l'aplat de l'action principale ne sert jamais à un état sélectionné.

## 2026-10-06 (suite) — Avis n°71 : mise en œuvre de R1 à R7 dans les 8 apps (local, non poussé)

- **Demande** : travailler tous les R de l'avis n°69 avec DESIGNER, contrôler, montrer le rendu en localhost ; décision de déploiement remise à l'utilisateur (de suite ou après l'exercice).
- **Fait** : barre de plateforme commune (R3, 8 apps), MELMIL ramené à 7 destinations (R4), menus « Plus ▾ » / « Affichage ▾ » de l'éditeur admin et en-tête du cockpit (R5), corrections immédiates (R1), lexique de zone + « publication » dans l'Admin (R2), aide « ? » et page « Premiers pas » (R6), protocole d'observation (R7). Détail : `AVIS\2026-10-06_NAVIGATION_PLEIADE\AVIS_71_MISE_EN_OEUVRE.md`.
- **Contrôles** : compilation des 8 apps, captures `apres\` (Admin, MELMIL, presse, cockpit), images Docker. Un défaut trouvé par la capture et corrigé (bulle d'aide MELMIL hors écran).
- **Limites** : eho, messagerie, LEAC et social non vus à l'écran (pas de session locale) ; filtrage de la barre par groupe impossible sans extension de l'API de découverte (Xavier).
- **En attente de l'utilisateur** : déployer maintenant ou après DELATTRE 26 ; 5 arbitrages du lexique ; lancer l'observation de 5 animateurs.

## 2026-10-06 — Formation « orientation et surcharge d'outils » + avis n°69 (navigation de PLÉIADE)

- **Demande** : les animateurs de DELATTRE 26 sont perdus (trop d'apps, d'onglets, d'outils) ; former DESIGNER avec 10 liens fournis et l'appliquer aux apps existantes et futures.
- **Ingéré** : REF-21 NN/g (architecture, navigation, onglets, révélation progressive, aide ; lien fourni en 404), REF-22 GOV.UK navigation, REF-23 Material 3 (site illisible → doc Android officielle), REF-24 NN/g utilisabilité et analyse de tâches, REF-25 onboarding (UX Collective via Wayback + NN/g), REF-26 **hors doctrine** (RAG-Anything, UXAgent, Pydantic AI : outillage d'agents IA ; UXAgent = avis CYBERSECU obligatoire).
- **Doctrine** : §3.7, règles 27 à 40, avec les tensions entre sources notées.
- **Avis n°69** : inventaire de la navigation des 9 apps (lu dans le code), 10 constats, 7 recommandations classées (R1 corrections immédiates → R3 barre de plateforme commune → R7 test avec 5 animateurs). Rien d'appliqué, en attente du choix de l'utilisateur.

## 2026-10-06 — Avis n°68 : app-admin, corps d'article « Mise en forme | HTML »

- **Demande** : écrire le corps d'un article de presse en HTML ou avec des boutons (gras, italique…), comme sur un forum ; prototype à montrer en local.
- **Recommandations** : R1 segment mémorisé par poste · R2 barre d'outils en groupes (Toolbar APG, raccourcis en infobulle) · R3 lien en barre en ligne · R4 rien que le journal jette · R5 jamais de perte silencieuse (encadrés de maquette → ouverture en HTML + encart qui nomme les pertes) · R6 HTML aéré · R7 compteur.
- **Statut** : appliqué en local (branche `editeur-article`), 5 captures dans le dossier de l'avis ; défaut `setEditable` trouvé et corrigé à l'essai ; en attente de l'avis de l'utilisateur.

## 2026-10-05 — Avis n°65 : app-admin, fenêtre de choix de l'incident

- **Demande** : la fenêtre de choix de l'incident (création d'un scénario, « Changer… ») est trop petite, on choisit mal.
- **Constats** : « Changer… » rogne la liste à une ligne (gravité 4) ; à la création, fenêtre de 620 px et liste flottante de 320 px qui masque le formulaire (3) ; 89 incidents sur une colonne (3) ; un clic de trop dans « Changer… » (2) ; mode storyline en menu + liste de 280 px (2).
- **Recommandations** : R1 liste intégrée à hauteur fixe · R2 960 px en deux colonnes storylines | incidents · R3 intitulé entier, coche « actuel » · R4 « Changer… » ouvre la liste · R5 même gabarit en mode storyline.
- **Statut** : appliqué (`70cdc56`), captures avant/après dans le dossier de l'avis, en attente du feu vert.

## 2026-10-05 — Avis n°64 : app-admin, arbre d'un scénario — « Tout sélectionner » par partie

- **Demande** : en mode Sélection, pouvoir tout cocher **par partie** (tous les tweets sans la presse), et remettre de l'ordre dans les boutons de la zone.
- **Constats** (Nielsen) : pas de « tout cocher » (gravité 3) ; la partie d'app, unité naturelle, sans case (3) ; mode Sélection muet tant que rien n'est coché (2) ; Supprimer noyé au milieu (2) ; barre du haut sans groupes (1) ; pas d'Échap (1).
- **Recommandations** : R1 case « Tout » tri-état par app · R2 barre de sélection toujours visible · R3 quoi → comment → danger → sortie · R4 trois groupes en haut · R5 Échap.
- **Statut** : appliqué dans app-admin (`972b348`), testé, en attente du feu vert de l'utilisateur.

## 2026-10-05 — Avis n°63 : MELMIL, déroulé des incidents en temps réel

- **Demande** : voir pour chaque incident son déroulé (FAM JEMM → tweets / presse de l'admin → CRQ) et où l'on en est à l'heure près ; emplacement libre.
- **Propositions** (prototype interactif `AVIS\2026-10-05_MELMIL_DEROULE\prototype.html`, données fictives, curseur « heure simulée ») : **B** nouvel onglet « Déroulé », chronogramme avec ligne MAINTENANT (recommandé) ; **A** 4 étapes par incident dans la Synthèse ; **C** « Maintenant » (joué 3 h / à venir 6 h / à corriger). Reco : B + étapes de A dans le tiroir + compteurs de C en tête.
- **Faits relevés** : FAM présent dans les exports mais non lu ; pas d'état « joué » dans JEMM ; l'admin doit exposer ses éléments datés ; CRQ rapproché par date + cellule + « CRQ-UTMC ». Exports du 05/10 marqués NATO RESTRICTED → exclus du prototype.
- **Statut** : montré en local, en attente du choix de l'utilisateur (3 questions dans l'AVIS).
- **Suite (même jour)** : icônes refaites (pictogrammes Lucide, plein + ✓ / contour / « ! » / ✕, regroupement « +N » au-dessus) ; lien « Ouvrir le scénario dans l'admin » ; **B retenue** et codée dans app-melmil (branche `deroule`) avec les étapes de A dans le détail et « À corriger » de C en tête ; le détail reprend **le même bloc CRQ** que la fiche (demande utilisateur). Décisions : CRQ du jour de l'incident, joué = heure (FAM) / statut admin, FAM en entier. ⚠ Leçon technique : une règle `display:inline-flex` sur les `span` de la légende écrasait la grille des icônes (pictogramme réduit à 2 px) — cibler `> span`, et `box-sizing: content-box` pour une pastille à bordure.

## 2026-10-04 — Avis n°60 : MELMIL, en-tête de la planche de préparation

- **Demande** : l'utilisateur « n'est pas fan » de la zone au-dessus de la planche (capture) ; propositions demandées.
- **Constat** : grille à 303 px du haut ; réglages éparpillés sur 3 lignes à droite ; 7 pastilles de même poids sur la ligne du titre ; « Exporter en PPT » plus visible que tout ; phrase d'aide permanente entre réglages et grille.
- **Propositions** (maquette `AVIS6-10-04_MELMIL_ENTETE_PLANCHE\maquette-entete.html`) : A barre d'outils unique (½ j, 217 px) ; B en-tête compact, recommandé (1 j, 202 px) ; C planche agrandie collante (+½ j, 106 px).
- **Statut** : proposé, puis **B retenue** (comparaison locale `comparer.html`) et appliquée le 2026-10-04 (app-melmil `fe17050`, 2026-10-04.15) ; grille à 200 px au lieu de 303.

## 2026-10-03 — Avis n°40 : MELMIL, deux groupes d'animation (GA1, GA2) et la source de chaque event

- **Demande** : mettre en écran 7 décisions de l'utilisateur : rôles GA1/GA2 (fin du rôle « Animation »), chaque GA ne modifie que ses events et ce qui en dépend, lit ceux de l'autre, demande des produits partout ; propriétaire + source par event (« Synchronisé avec JEMM », un export = un event, mise à jour limitée à cet event ; « Créé dans MELMIL », jamais touché) ; codes MELMIL ≥ 20 ; statut arrêté à « Validé » pour les events MELMIL ; Écarts limités aux events JEMM ; choix d'afficher ou non l'autre GA ; events existants au GA1.
- **Constat** (code lu le 2026-10-03, `app-melmil` `1ea2e0c` + travail non commité) : la planche JEMM **n'a pas de filtre d'events** (seulement le style, mémorisé par poste) ; « Aligner sur JEMM » supprime les events absents des exports ; le modèle `ga`/`source`, `groupes.ts` (`prochainCodeMelmil`, `codeMelmilInvalide` qui **bloque** < 20, `modificationsHorsPerimetre`, `idsDuGroupe`) et `alignerPerimetre` sont déjà en cours ; le mode lecture n°35 est un contexte React réutilisable par élément.
- **Avis** : `AVIS\2026-10-03_MELMIL_GROUPES_ANIMATION\AVIS.md`, R1 à R13. Points clés : pastille de mode après le titre ; un seul segment « GA1 seul | Tous les groupes » mémorisé par poste, ce qui est caché toujours compté ; marquage par mot + forme (pointillé), jamais par couleur ni opacité ; `LectureContexte` imbriqué par event ; formulaire de création avec la source d'abord ; « Mettre à jour depuis JEMM… » avec bilan de l'event ; stepper à 3 segments ; « Verser » retiré, « Aligner » sans suppression d'event ; Synthèse qui nomme son périmètre.
- **Questions** : 6, avec réponses par défaut (affichage « Tous » au premier passage ; code < 20 bloqué ; liste des events classés MELMIL montrée à l'Admin ; GA1+GA2 choisit ; Prod inchangé ; source non modifiable).
- **Statut** : proposé, à arbitrer ; aucun code modifié. CYBERSECU à consulter sur le contrôle d'accès serveur par GA.

## 2026-10-03 — Avis n°39 : app-social, joindre et écouter un MP3 sur un post principal

- **Demande** : joindre des .mp3 aux posts principaux (pas aux réponses), avec un visuel correct de lecture ; usages : messages audio, interceptions radio, discours, podcasts d'avatars. Le serveur (modifications en cours, non commitées) accepte `audio/mpeg` avec signature vérifiée, 20 Mo par défaut, `media_type = "audio"`, et refuse l'audio en réponse.
- **Constat** (web `e9aed18`) : partout, ce qui n'est pas une vidéo est rendu en `<img>` (post-card, grille Instagram, et `app-cockpit` `TootItem`) → image cassée ; bouton trombone (`label` + `input hidden`) inatteignable au clavier ; limites inconnues du client, toast 413 sans accents ; aperçus d'édition et de réponse toujours en `<img>` ; info-bulle « Ajouter une image » fausse ; pas de `duration_seconds` pour l'audio (ffprobe réservé aux vidéos) ; input non remis à zéro ; **aucun thème sombre** dans le code (`darkModeSelector: false`) ; pas d'onglet « Médias » au profil.
- **Avis** : `AVIS\2026-10-03_SOCIAL_MP3\AVIS.md`, R1 à R15. Points clés : lecteur natif dans un bandeau aux jetons `--masto-*` (variante maison sur `button` + `input range` seulement si le natif déçoit) ; un seul son à la fois par un écouteur global ; aucune lecture automatique ; pas de nom de fichier publié ; erreurs avant l'envoi et sur place ; vignette « AUDIO » dans les grilles.
- **Limite signalée** : le modèle Slider (et Disclosure) de l'APG n'est pas encore ingéré en fiche détaillée (REF-19 = Dialog, Tabs).
- **Statut** : proposé, à arbitrer par l'utilisateur (4 questions avec réponses par défaut) ; aucun code modifié.

## 2026-10-03 — Avis n°38 : MELMIL, un CR appartient à l'incident depuis lequel il a été créé

- **Demande** : un CR rempli depuis la fiche de 07.01.I03 doit se voir sur 07.01.I03 seulement (agrafe de la planche, section CR de la fiche), pas sur tous les incidents du même jour et de la même ETIM ; dans une fiche, seul CE CR est visible et modifiable, avec éventuellement un indicateur « un autre CR du même type existe via un autre incident » ; le .docx qui télécharge toute la colonne est à garder.
- **Constat** (code lu le 2026-10-03, `app-melmil` `1aa2354`) : `creerCompteRenduPartage` n'enregistre pas l'origine ; `piecesDeLIncident` compte toute la colonne (agrafe partout, Synthèse faussée) ; la fiche ouvre tous les exemplaires ; « + Créer » rend l'existant ; valeurs de départ prises sur la colonne ; la conversion du 2026-10-01 a effacé l'incident des anciens CR.
- **Avis** : `AVIS\2026-10-03_MELMIL_CR_PAR_INCIDENT\AVIS.md`, R1 à R14. Points clés : champ `depuisIncident` distinct de `incident` ; colonne = numérotation + lot, origine = affichage ; ligne « Aussi / Déjà ce jour pour l'ETIM 7 : n°1, créé depuis 08.02.I01 › » avec lien vers la fiche ; rien sur la planche ; anciens CR « à attribuer » en un clic, jamais devinés ; changement d'origine dans la fiche du CR.
- **Statut** : proposé, à arbitrer par l'utilisateur (4 questions avec réponses par défaut) ; aucun code modifié.

## 2026-10-03 — Avis n°37 : admin, changer la cible d'un scénario existant

- **Demande** : l'ancien scénario « 08.01 STARTEX » (créé avant la fonction storyline) n'est relié à rien ; sur sa fiche on ne peut choisir qu'UN incident dans une liste déroulante. L'utilisateur veut en cocher plusieurs (le rattacher à la storyline) et juge la liste déroulante inadaptée. La liste ne se fermait pas au clic extérieur (correctif en cours à part, présent non commité dans `IncidentPicker.tsx`).
- **Constat** (code lu le 2026-10-03) : 3 cibles à la création, 1 seule sur la fiche, alors que le PATCH accepte déjà la storyline ; bandeau de storyline figé ; ⚠ le commentaire « l'édition du périmètre reste MELMIL » est faux (MELMIL `api/zone/scenarios` = GET seul) ; un bouton dans le `listbox` (n°36 R14) ; `Modal` sans piège du focus ni `aria-labelledby`.
- **Avis** : `AVIS\2026-10-03_ADMIN_CIBLE_MULTI_INCIDENTS\AVIS.md`, R1 à R10. Points clés : une fenêtre « Cible du scénario » qui réutilise le bloc de la création (composant partagé), ouverte par un seul bouton du bandeau ; segment « Un incident | Une storyline | Bruit de fond » ; pré-rempli par la cible actuelle ou par le nom ; « Changer… » sur le scénario de storyline avec les codes couverts visibles ; combobox conforme au modèle APG.
- **Limite signalée** : les modèles APG Combobox, Listbox, Radio Group et Checkbox ne sont pas encore ingérés en fiche (REF-19 = Dialog, Tabs).
- **Statut** : proposé, à arbitrer par l'utilisateur ; aucun code modifié.

## 2026-10-03 — Avis n°36 : admin, scénarios de bruit de fond

- **Demande** : créer dans l'admin des scénarios nommés reliés à aucun incident ni storyline MELMIL (posts ordinaires, ambiance), bien rangés dans « Scénarios ». L'utilisateur proposait une 3e option dans « Cible du scénario » ou une case.
- **Constat** (code lu le 2026-10-03) : incident obligatoire côté formulaire et serveur dès qu'il y a un MELMIL ; « sans incident » = « Non classés » (à ranger) ; le bandeau invite à rattacher ; le segment n'a ni rôle ni état ARIA.
- **Avis** : `AVIS\2026-10-03_ADMIN_SCENARIOS_BRUIT\AVIS.md`, R1 à R15. Points clés : 3e segment « Bruit de fond » plutôt qu'une case (choix exclusifs, pas de mode caché) ; drapeau explicite côté données ; section « Bruit de fond » distincte, entre l'arborescence et « Non classés », sous-groupée par jour ; conversions dans les deux sens par le bandeau.
- **Statut** : proposé, à arbitrer par l'utilisateur ; aucun code modifié.

## 2026-10-02 — Avis n°34 : MELMIL, synthèse de planification

- **Demande** : voir d'un coup d'œil où en est la planification (incidents, en prépa, sans pièce jointe ni scénario…), nouvel onglet possible, ergonomie soignée ; à voir en local d'abord.
- **Constat** : tout est déjà calculable (statuts, `piecesDeLIncident`, `scenariosDe`, `ecarts`, demandes) mais éparpillé sur 4 onglets.
- **Avis** : `AVIS\2026-10-02_MELMIL_SYNTHESE_PLANIFICATION\AVIS.md`, R1 à R9 + maquette textuelle. Points clés : onglet « Synthèse » en tête de *Visualiser* sans changer l'arrivée ; phrase + barre empilée (Validé hachuré / Dans JEMM plein, car même vert) ; chaque manque = un lien vers Incidents filtré par un nouveau paramètre `manque` (non mémorisé), calculé par une seule fonction pure ; jamais de 0 quand les scénarios ou JEMM sont indisponibles.
- **Limite signalée** : pas encore de source dédiée aux tableaux de bord (Few, NN/g) dans nos fiches.
- **Statut** : à appliquer par PLEIADE / ARCHITECTE, en local d'abord.

## 2026-10-02 — Avis n°27 : admin, retrouver ses scénarios dans la masse

- Demande de l'utilisateur : on ne retrouve plus ses scénarios dans l'app-admin. On cherche par incident MELMIL, et les noms commencent en général par le code.
- Constat : liste plate triée par dernière modification (l'ordre change sans cesse), grandes cartes (environ 5 par écran), aucun regroupement.
- Proposé : rangement par event › storyline › incident lu dans le nom, une ligne par scénario, recherche qui comprend les codes, affichage mémorisé, modèle de nom à la création.
- Signalé au passage : le `createdById` aléatoire des scénarios créés avant la correction d'identité.
- Statut : proposé, en attente de la décision de l'utilisateur. Détail dans `AVIS\2026-10-02_ADMIN_RANGER_SCENARIOS\AVIS.md`.

## 2026-10-01 — Avis n°19 : MELMIL, demande de produit sans incident + cellule demandeuse

- **Demande** : la FORAD ne crée pas d'incident. Il faut un bouton dans l'onglet « Demandes de produit », et chaque demande doit indiquer GREY CELL ou FORAD. DESIGNER a été associé à la mise en place.
- **Avis** : `AVIS\2026-10-01_MELMIL_DEMANDE_SANS_INCIDENT\AVIS.md`, R1 à R6. Les deux décisions clés : une **cellule obligatoire pré-choisie, en choix visibles** ; une **demande directe qui porte elle-même ses fichiers**.
- **Appliqué** dans `app-melmil` `533e548` (`2026-10-01.1`). Vérifié avec Playwright en local.

## 2026-10-01 — Avis n°18 : portail de zone, page « Presse », la carte entière ouvre le site

- **Demande** : supprimer le bouton « Ouvrir », faire ouvrir le site par un clic sur la carte, garder « Espace de rédaction ».
- **Avis** : `AVIS\2026-10-01_PORTAIL_CARTES_PRESSE\AVIS.md`, R1 à R7. Le point clé est le **lien étiré** : il ne faut jamais mettre un lien dans un lien, et le survol du bouton secondaire ne doit pas animer la carte.
- **Appliqué** dans `pleiade-platform` `4995efc` (`portail.ts`, `pageChoix`). Vérifié avec Playwright : zones de clic, survols, focus, téléphone.
- **Leçon technique** : une capture prise juste après un `mouse.move` saisit la transition en cours. Attendre ~400 ms avant de capturer un état de survol.

## 2026-09-30 — Avis n°15 : MELMIL, médias des incidents et demandes de produit complexe

- **Demande** : un bouton « Demande de produit complexe » sur chaque incident (FORAD, GreyCell vers la cellule Prod), et les fichiers de l'incident visibles, avec un import. Le formulaire InfoG d'ORION 26 est à remanier.
- En cours de route, l'utilisateur a renoncé à la fiche Word : « un seul outil ». Elle a été retirée.
- **Avis** : `AVIS\2026-09-30_MELMIL_PRODUITS\AVIS.md` (R1–R8), captures `captures\`.
- **Appliqué** : `app-melmil` `e5fcf86`, et le catalogue de `pleiade-platform` `7de590f`.

## 2026-09-29 — Avis n°14 : maquettes existantes d'app-press (TM, HEX, TV4, BC1)

- **Demande** : optimiser le rendu et l'architecture des 4 maquettes de médias fictifs, en respectant les chartes des pays (Today Mercure = média d'État « russe », en anglais). Les 6 reprises de sites réels sont exclues.
- **Avis** : `AVIS\2026-09-29_PRESSE_MAQUETTES\AVIS.md`, 9 constats et R1–R8, captures `avant\` / `apres\`.
- **Appliqué** : `app-press` branche `design-maquettes` `48b1072` ; image reconstruite comme sur le serveur, tests OK. En attente de validation et de mise en ligne.
- **Leçons** :
  - un banc d'essai de maquette de presse doit contenir des articles **sans photo** ;
  - les images différées ne sont pas chargées dans une capture pleine page : faire défiler la page avant.

## 2026-09-28 — Avis n°13 : MELMIL, « Confié à » par groupes

- **Avis** : `AVIS\2026-09-28_MELMIL_CONFIE\AVIS.md`, R1–R6 : le choix suit la hiérarchie, des pastilles d'un clic, dire ce que signifie « rien de coché », un état vide qui guide, ne rien perdre, montrer le résultat partout.
- **Appliqué** : `app-melmil` `a65d6f2`.

## 2026-09-28 — Avis n°12 : organigramme, placer les groupes reliés côte à côte

- **Avis** : `AVIS\2026-09-28_MELMIL_PLACEMENT\AVIS.md`, R1–R3 : supprimer l'information vide, la proximité suit la relation (chaînes de colonnes, sous-groupe du côté de son partenaire), un placement stable.
- **Appliqué** : `app-melmil` `04b3a15`.

## 2026-09-28 — Avis n°11 : MELMIL, Équipe, de l'araignée à l'organigramme

- **Déclencheur** : trois remarques de l'utilisateur sur l'avis n°10 (niveaux masqués, un seul rattachement, exercice au centre trompeur).
- **Avis** : `AVIS\2026-09-28_MELMIL_ORGANIGRAMME\AVIS.md`, R1–R5.
- **Leçon de doctrine** : une mise en page radiale fixe un nombre de couronnes et confond « contenir » avec « être au centre ». Pour une structure militaire, l'organigramme (Jakob) ; deux relations différentes = deux traits différents, ET un texte.
- **Appliqué** : `app-melmil` `84294f7`.

## 2026-09-28 — Avis n°10 : MELMIL, onglet Équipe (araignée)

- **Avis** : `AVIS\2026-09-28_MELMIL_EQUIPE\AVIS.md`, R1–R7 : lire d'abord et modifier dans le panneau, deux vues (araignée, liste), des choix plutôt que de la saisie, couleur doublée du nom, une seule action principale, état vide, rien de perdu.
- **Appliqué** : `app-melmil` `f9f72b6` (branche `equipe-organigramme`).

## 2026-09-28 — Avis n°9 : eho, ranger 235 groupes

- **Avis** : `AVIS\2026-09-28_EHO_RANGER_GROUPES\AVIS.md`, R1–R5 : masquer sans supprimer, assistant qui propose par famille, résultat avant d'appliquer, aucune supposition invisible, archives à portée.
- **Appliqué** : `eho` `8bb7084` (branche `groupes-archives`), 235 → 6 visibles en local.

## 2026-09-27 — Avis n°8 : LEAC, la pastille d'état du réseau

- **Demande** : voir si l'écran vient du serveur (« direct », en vert) ou de la copie du service worker.
- **Avis** : `AVIS\2026-09-27_LEAC_PASTILLE_RESEAU\AVIS.md`, R1–R5.
- **Appliqué** sur `etat-reseau` (`a4639f3`), puis mis en ligne le même jour (`2026-09-27.1`).

## 2026-09-25 — Avis n°7 : MELMIL, choisir les ETIM d'un incident

- **Demande** : cocher les ETIM concernées à la création d'un incident, et voir leurs noms sur la carte dans la planification.
- **Avis** : `AVIS\2026-09-25_MELMIL_ETIM\AVIS.md`, R1–R5 (voir §6 de la mémoire).
- **Appliqué** : `app-melmil` `5b4d76a`, version `2026-09-25.1`, sur la branche `etim-incidents`. Testé en local au téléphone et sur ordinateur.

## 2026-09-25 — Avis n°6 : eho, onglet Groupes (liste des membres)

- **Demande** : cliquer sur un groupe pour voir ses avatars — @compte du réseau social et nom/prénom, sans la fiche complète. « Très beau et fluide », mis en ligne directement.
- **Avis** : `AVIS\2026-09-25_EHO_GROUPES\AVIS.md`, R1–R6 (voir §6 de la mémoire).
- **Relevé en préparant** : `GET /api/groups/[id]/members` était lisible par tout joueur. Or un nom de groupe révèle ce que le joueur doit découvrir. La route est désormais réservée à l'animation et à la clé de service.
- **Mis en ligne** : `eho` `124679a`, `2026-09-25.4`.

## 2026-09-25 — Avis n°5 : l'écran Avatars d'eho (rail, préchargement, retour)

- **Demande** :
  - voir images et fiches bio des cartes affichées, grâce à un préchargement qui ne fait pas planter ;
  - pouvoir refermer ce qu'on a déplié ;
  - faire défiler plutôt que cliquer, sans agrandir la fenêtre.
- **Défaut trouvé** : si sa lecture échouait, une fiche restait sur « Chargement… » pour toujours.
- **Solution** : `AVIS\2026-09-25_EHO_AVATARS\AVIS.md`, R1 à R5, appliquée sur `eho` `avatars-rail` (`a3bf90a`).
- **Vérifié**, avec 3 500 avatars en CPU ×4 :
  - sur un bloc de 625 cartes, le défilement charge 60 → 420 et la page reste à la même hauteur ;
  - « Revenir au début » ramène à 60 ;
  - la fiche s'ouvre avec sa bio sans chargement ;
  - les portraits à l'écran sont chargés (4/4) ;
  - aucun débordement au téléphone.

## 2026-09-24 (nuit) — Avis n°4 appliqué en local sur eho, + chargement par groupe

- **Demande** : tout mettre en œuvre en local ; en plus, à ~3 500 avatars (DE LATTRE 26), faire charger les avatars « par groupe », les pages buguant sous la charge.
- **Banc d'essai** : copie locale de la base `eho` → **`eho_charge`**, plus 3 050 avatars générés (3 503 au total). Mesure faite en CPU ×4 et réseau 10 Mbit/s, 60 ms.
- **Fait** : l'état complet est dans `AVIS\2026-09-24_EHO\AVIS.md` § « Suite donnée ».
- **Corrigé dans l'avis** :
  - P4 : l'alternative clavier existait déjà pour la zone ;
  - la confirmation de modèle demandait déjà de taper le code.
- **Vérifié** :
  - 0 page plus large que l'écran ;
  - le contenu démarre à 0 px au téléphone et à 68 px sur tablette ;
  - rangement de 3 cartes en une action ;
  - confirmation : focus sur « Annuler », Échap ferme ;
  - mode sombre lisible ;
  - aucune fuite de données officielles vers un joueur (liste et fiche) ;
  - la nouvelle route `/api/avatars/planche` renvoie 403 à un joueur.

## 2026-09-24 (soir) — Avis n°4 : eho, propositions sans code

- **Demande** : analyser eho et dire, **sans coder**, ce qu'il faudrait changer pour le rendre plus fluide et utilisable par tous (téléphone, tablette, ordinateur).
- **Examiné** : `eho` `aa791a4`, en local sur le port 3001, 10 écrans animateur + 3 écrans joueur + la connexion, sur iPhone 13, iPad Mini et 1440 px, plus un passage en mode sombre du système.
- **Constats majeurs** :
  - mode sombre blanc sur blanc (seul `--background` est redéfini) ;
  - menu de 256 px fixe au téléphone ;
  - tableaux Avatars et Modèles coupés sans défilement sous 1024 px ;
  - rangement uniquement par glisser-déposer natif (`draggable`), sans alternative ;
  - JSON brut au tableau de bord ;
  - 8 `confirm()` natifs ;
  - 29 textes à 8-11 px.
- **Rendu** : `AVIS\2026-09-24_EHO\AVIS.md` (12 problèmes, 11 recommandations en 3 lots, ordre conseillé, critère de réussite) et 13 captures.

## 2026-09-24 (soir) — Avis n°3 : MELMIL v2, appliqué en local

- **Demande** : repenser toute l'architecture de MELMIL pour la lisibilité et l'accessibilité, comme pour LEAC, du téléphone à l'ordinateur.
- **Audit de départ** (`2026-09-24.4`, iPhone 13) : sélecteur d'espace poussé hors écran, tableau des incidents débordant de 220 px, contenu à 370 px du haut, 5 boutons en barre, grille illisible au téléphone. Tablette et ordinateur corrects.
- **Proposition** : `AVIS\2026-09-24_MELMIL_V2\PROPOSITION.md` (R1–R8), toute appliquée sur `app-melmil` branche `refonte-v2` (`03e3363`).
- **Corrections trouvées en vérifiant** : « Afficher » cassé lettre par lettre (select trop large), codes coupés « 06.0 / 1 », éditeur à 280 px minimum, menus « Plus » et « Changer d'étape » hors écran, bandeau trop large à 150 %.
- **Résultat** : 0 débordement sur iPhone SE, 13, 13 Pro Max, Pixel 7 (100 et 150 %), iPad Mini, 1440 px ; 166/166 tests ; captures dans le scratchpad de session.

## 2026-09-24 (suite) — 11 sources de plus + premier audit (MELMIL)

- **Décisions de l'utilisateur** :
  1. le gaver de sources fiables et gratuites, en lui laissant proposer les siennes ;
  2. Refactoring UI : pas de livre, on s'en tient aux extraits gratuits ;
  3. pas de thème PLÉIADE unifié.
- **Ingérés** (REF-10 à REF-20) : GOV.UK (principes et Design System), DSFR (⛔ réservé aux sites `.gouv.fr` : inspiration seulement), IBM Carbon (couches, tableau de données), WCAG 2.2 AA (seuils), 10 heuristiques de Nielsen, Radix Colors (12 crans), A11Y Project, Practical Typography, Inclusive Components (index), WAI-ARIA APG (Dialog, Tabs), ressources libres (bradtraversy). Ajout à REF-07 du chapitre gratuit « Building Your Color Palette ».
- **Refus de lecture automatique** : systeme-de-design.gouv.fr et Medium (403) → contournés par le README GitHub du DSFR. L'article Medium de Refactoring UI reste à lire.
- **Correction** : une lecture automatique attribuait 44 × 44 px au critère WCAG 2.5.8. La vraie valeur est 24 × 24 (AA), et 44 × 44 relève du critère 2.5.5 (AAA). Règle 12 corrigée.
- **Doctrine** portée à 26 règles, avec une grille d'audit (§3.6) et une liste de sources à ingérer ensuite (§5 bis).
- **Avis n°1 — MELMIL** : `AVIS\2026-09-24_MELMIL\AVIS.md`. 8 problèmes relevés, dont 1 de gravité 4 (on ne voit pas dans quel espace on est) et 4 de gravité 3. 8 recommandations, dont 5 retouches légères à faire d'abord.

## 2026-09-24 — Création de l'agent + première ingestion (9 sources)

- **Demande de l'utilisateur** : un agent « DESIGNER » qui maîtrise les documents de design fournis petit à petit, pour conseiller sur le design de nos sites et applicatifs. Il n'a pas forcément la vérité sur nos projets, mais il y contribue pour rendre le design plus agréable à l'humain.
- **Ingérés** (une fiche chacun dans `REFERENCES\`) : shadcn/ui, Radix Primitives, HyperUI, Awesome Design Systems (klaufel), Awesome React Design Systems (jbranchaud), Laws of UX, Refactoring UI, Lucide, Motion.
  - Pages GitHub complétées par la documentation : thème shadcn, introduction Radix, accessibilité Motion, fiches Fitts, Hick et Jakob de Laws of UX.
  - Les liens fournis portaient `?utm_source=gemini` : ce paramètre de suivi a été retiré.
- **Terrain relevé dans le code** : deux familles de jetons (thème PLÉIADE pour admin et press, graphite/craie pour MELMIL et LEAC), Tailwind 4 partout, lucide-react dans admin et press, eho non habillé.
- **Doctrine** : 20 règles sourcées dans `MEMOIRE.md` §3.
- **Premier constat utile** : la fiche de compte rendu de MELMIL (livrée le même jour) ferme bien sur `Échap`, mais elle **ne piège pas le focus** et **ne le rend pas** au bouton d'origine (règle 11, REF-02). À proposer à la prochaine intervention sur MELMIL.
- **Questions ouvertes** : DSFR, GOV.UK et Carbon à ingérer ? PDF de Refactoring UI disponible ? Thème PLÉIADE unifié ?
- **Prochaine étape** : ingérer les documents suivants de l'utilisateur ; rendre un premier avis sur un écran réel dès qu'on en sollicite un.

## 2026-10-11 (~20 h 20) — Avis n°99 mis en œuvre (eho 2026-10-11.7, local)
- Bloc « Fiches de comportement : exporter, corriger, réimporter » en bas de la page Population IA, conforme à R1-R5 : boutons secondaires, vérification lancée au dépôt, résultat dans la page (bandeau qui prend le focus, compteurs forme + mot, groupes repliables refusés / modifiés dépliés, ignorés / inchangés repliés, puces « Exemples +1 », « Tempérament · anxiété 40 → 55 », « Voir le détail » avant barré / après), case de sauvegarde cochée, `confirmer` sans style danger, bandeau vert « 1 fiche mise à jour à 20:13. Le moteur les prendra en compte d'ici 20:23 », sauvegarde nommée.
- **Écart à l'avis** : l'export ne contient PAS la mémoire d'exercice (choix CYBERSECU : format fermé, la mémoire va dans l'export d'analyse du Moteur IA) → mention adaptée ; une tentative sur un champ protégé fait **refuser** l'entrée (CYBERSECU) au lieu d'un marqueur orange ; limites 8 Mo / 500.
- Non fait (option R5) : « en attente du moteur / prises en compte à… ». Captures : `C:\CECPC\pleiade\dev\prototype-ia\pont\essai-fiches\`.

## 2026-10-13 — Avis n°105 : vue principale du Cockpit
- Demande utilisateur : vue principale « incompréhensible » (capture DELATTRE 26 : 4 025 sources, mosaïque « Nouveaux messages 149 ») ; besoin de catégories de suivi et d'un contrôle général multi-canaux (social, Chat, presse, messagerie).
- Code lu (lecture seule, `app-cockpit` `dea51d1`). Cause racine : un groupe eho est copié membre par membre en sources ; les compteurs de catégorie comptent des sources, pas de l'activité ; le Cockpit ne lit que les réseaux sociaux.
- Trois concepts (A canaux, B situation catégories × canaux, C boîte de réception) avec ASCII et listes de zones à maquetter ; recommandation B + C. Avis : `AVIS\2026-10-13_COCKPIT_VUE_PRINCIPALE\AVIS.md`. Aucun commit.
- Maquettes cliquables réalisées (données de synthèse, hors dépôt) : `C:\CECPC\pleiade\dev\maquettes-cockpit\` (`node serveur.mjs`, http://127.0.0.1:4100/) : sommaire, A, B, C, fenêtre « Nouvelle catégorie de suivi », volet non modal, états simulés (rien de neuf, messagerie injoignable, premier écran sans catégorie). Correction en cours de maquettage : seuil de flambée relevé (≥ 6 nouveaux et × 3), sinon le rouge envahissait la grille B. En attente des arbitrages de l'utilisateur (dernier passage par animateur ou par cellule, mesure du poids, noms d'onglets) et de CYBERSECU (contenu du Chat et de la messagerie).
- Arbitrages utilisateur consignés (avis 105 §8) : dernier passage par animateur ; poids = réactions de l'heure, abonnés hors calcul ; onglets validés ; B accueil + C onglet + A en projection grand écran via le menu ⋯ (aucun contenu privé projeté). Maquettes mises à jour.

## 2026-10-13 — Avis n°107 : diaporama de présentation de PLÉIADE (officier, décideurs)
- **Demande** : avis design sur un deck de 10 diapos 16:9 (PDF) présentant PLÉIADE à des décideurs de la Défense ; l'utilisateur veut « beaucoup plus propre ». Chiffres vérifiés en parallèle par une autre analyse.
- **Mesures** : texte vectorisé « Glyphless » (polices identifiées à l'œil) ; corps 13-15 pt (interlignes mesurés à 144 dpi), 92 à 139 mots par diapo ; palette relevée par échantillonnage (marine `#14213D`, cartes `#1D2D52`, or `#E8A93A`, sarcelle `#5CC2AD`, rose `#EF8A96`, rouge `#9B2D3A`) ; contrastes 3,5:1 à 14,2:1.
- **Avis** : `AVIS\2026-10-13_PPT_PRESENTATION_PLEIADE\AVIS.md`. Piste A recommandée (charte PLÉIADE graphite/craie, Archivo + JetBrains Mono, angles vifs), clair = contenu / sombre = moments, corps 24 pt, 40 mots max, grille 12 colonnes, 4 schémas, plan en 11 diapos.
- **Constat annexe** (remontée PLEIADE) : les icônes d'apps du portail (`pleiade-platform\public\img\apps\`) sont hétérogènes et **social, messagerie, cockpit et admin ont la même image**.
- **En attente** : piste A/B, demande aux décideurs, données de la courbe d'opinion, capture, outil de fabrication.
