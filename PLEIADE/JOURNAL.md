# JOURNAL — PLEIADE (historique chronologique, append-only)

> Comptes rendus datés des travaux sur le système PLEIADE. Les règles et l'état durable sont dans `MEMOIRE.md`.

---

## 2026-10-03 (matin) — ⚠ Déploiements bloqués : MariaDB partagée saturée (« Too many connections »)

- **Constat** : MELMIL run #50 (`cd8222f`) et Admin run #20 (`233d0df`) échouent tous deux à l'étape `pleiade-promouvoir` (image construite et poussée au registre, promotion refusée).
- **Cause probable (lecture du code)** : UN seul conteneur `pleiade-db` (`mariadb:11`, `docker-compose.prod.yml`) sert l'orchestrateur ET toutes les instances de toutes les zones ; `max_connections` non réglé → défaut **151** ; chaque instance Prisma (`PrismaMariaDb`) garde jusqu'à **10** connexions → saturation dès ~15 instances. L'orchestrateur, lui, est limité à 5 (`src/db.ts`).
- **Contournement fait par l’utilisateur** : arrêt des instances inutiles des autres zones (connexions libérées) ; message de diagnostic transmis à Xavier.
- **Déblocage proposé (serveur, utilisateur/Xavier)** : `SHOW PROCESSLIST` groupé par base, puis `SET GLOBAL max_connections = 500;` (non persistant), puis « Re-run failed jobs » sur les deux runs.
- ⭐ **Cause RACINE mesurée en local** : le pilote `mariadb` (via `@prisma/adapter-mariadb`) a par défaut `minimumIdle = connectionLimit = 10` → dès la 1re requête, **chaque instance garde 10 connexions ouvertes EN PERMANENCE**, même sans utilisateur (essai : pool sans réglage = 10 au repos). ~15 instances ≈ 151 = plafond. Les 3 postes ajoutés n'ont fait que réveiller des réserves.
- **Correctif préparé (branches `reserve-connexions`, NON POUSSÉ, accord Xavier attendu)** : `avecReserve(url)` ajoute `connectionLimit` (`DB_POOL_MAX`, défaut 3 ; **5 pour eho**), `minimumIdle=1`, `idleTimeout=60` à DATABASE_URL (une valeur déjà présente l'emporte) dans les 7 apps à base : app-admin `7b20134`, app-messagerie `587cb1d`, app-press `1b807b0`, eho `e398d9a`, app-melmil `cbf246b`, app-leac `436d85b`, app-social `28a1f46` (API). tsc OK partout ; tests : admin 31, messagerie 9, press 8, eho 112, leac 468, melmil 375 — tous verts. Mesure image MELMIL, 30 requêtes simultanées : **10 connexions gardées avant → 3 après**, toutes servies (200). Reste à faire avant push : essai d'image des 6 autres apps.
- **Correctifs durables proposés, non engagés** : (1) `command: --max-connections=500` sur le service `db` (recréation du conteneur = courte coupure de toutes les apps) ; (2) réserve Prisma réduite par instance (ex. 3). À décider avec Xavier ; à tester en local d'abord.

## 2026-10-03 (suite 3) — Admin : scénarios de BRUIT DE FOND (app-admin `233d0df`) — POUSSÉ sur main + prod le 2026-10-03 vers 10:57 ; ⚠ mise en ligne non constatée à 09:06 (même cause probable que MELMIL : promotion « Too many connections »)

- **Besoin (utilisateur)** : créer des scénarios de bruit (ambiance des réseaux), reliés à aucun incident ni storyline, mais nommés et bien rangés ; travail avec DESIGNER (avis n°36).
- **Serveur** : champ `Scenario.bruit` (booléen, défaut faux → ajout sans risque par le `db push` du démarrage). POST : `bruit: true` = pas de cible MELMIL exigée ; sans le drapeau, l'incident reste obligatoire. PATCH : `bruit: true` retire la cible ; poser un incident/storyline retire le drapeau. `rattacherAuxIncidents` ignore le bruit. La route lue par MELMIL ne liste que les scénarios avec incident → le bruit n'apparaît pas dans MELMIL.
- **Écran** : 3e cible « Bruit de fond » (radiogroup accessible), section « Bruit de fond » sous-groupée par jour avant « Non classés », colonne « bruit », lien « + Bruit de fond », bandeau dédié sur la fiche, conversions bruit ↔ incident sans renommer, « C'est du bruit de fond » pour un non-classé, case dédiée en zone sans MELMIL. Corrigé au passage : segment sélectionné illisible en thème sombre.
- **Vérifié** : tsc, 31/31 tests, Playwright 16/16 (refus serveur sans cible, création, fiche, conversions dans les deux sens, liste, recherche, 0 erreur JS) ; image Docker : base vide + base ancienne (scénario existant gardé, `bruit` = 0), redémarrage, 0 erreur.

## 2026-10-03 (suite 2) — MELMIL : statut des incidents à l'import JEMM (app-melmil `cd8222f`) — ✅ EN LIGNE le 2026-10-03 (`/api/sante` 2026-10-03.3) après relance, une fois des instances inutiles arrêtées ; d’abord ÉCHOUÉ (run #50) : image construite et poussée, mais `pleiade-promouvoir` → « echec de la promotion : Too many connections » (MariaDB saturée côté serveur). À relancer (« Re-run failed jobs ») ; si récurrent : `SHOW PROCESSLIST` / `max_connections` sur le serveur (pools Prisma des instances)

- **Question utilisateur** : les statuts saisis dans MELMIL survivent-ils à l'import des exports JEMM ? Et un incident créé dans JEMM, absent de MELMIL ?
- **Constaté dans le code** : (1) l'import de la **Planche JEMM** n'écrit que la planche JEMM, jamais l'atelier → statuts intacts ; (2) **Réglages → verser un export** n'ajoute que ce qui manque (code inconnu), sans toucher l'existant ; (3) **Réglages → aligner sur JEMM** remplace code, sujet, description, D+/heure, moyen, émetteur, destinataires, résultat attendu, et **garde** statut, ETIM, effets attendus, QUI/OÙ, EXCON, responsables, traitants (`...ancien`). ⚠ Limite : l'alignement apparie par ressemblance du sujet puis par numéro ; un incident **trop transformé** dans JEMM (sujet ET numéro changés) n'est pas reconnu → recréé, et l'ancien est supprimé s'il n'a pas de pièces jointes (sinon gardé et listé au bilan) — le statut est alors perdu.
- **Corrigé (décision utilisateur)** : un incident nouveau venu de JEMM entrait au statut « Dans JEMM » → désormais **« En préparation »** (verser + aligner). 4 tests, 375/375, image Docker base vide + redémarrage → `2026-10-03.3`, 0 erreur.

## 2026-10-03 (suite) — MELMIL : rôles « Admin » et « Lecture et demandes », Animation recentrée (app-melmil `955cf8c`, pleiade-platform `4844ee0`) — POUSSÉ, EN LIGNE (`/api/sante` 2026-10-03.2)

- **Décision utilisateur** : un groupe « Admin » a accès à tout ; l'**Animation** crée events, storylines, incidents et demandes ; **toute la gestion technique** passe à l'Admin.
- **Catalogue** : rôle `gestion` libellé **« Admin »** (⚠ la clé `admin` reste celle d'« Animation », historique — ne pas la renommer, les cases cochées seraient perdues). Se suffit à lui-même (entrer, écrire, droits Prod).
- **Réservé à l'Admin** : onglet **Réglages** (nom, ETIM de l'exercice, calendrier, verser un export JEMM, aligner, sauvegarde/restauration), **« Changer d'étape »**, et **toute écriture de la planche JEMM** (import, réglages, remplacer, restaurer, déplacer, purger, vider). L'Animation garde Journal, Écarts, Équipe, l'export PPT et peut encore **ajouter** une ETIM depuis une fiche d'incident (pas la renommer ni la retirer).
- **Serveur** : `reglagesModifiesSansDroit` (`src/lib/atelier/gestion.ts` : nom, calendrier, GT, ETIM perdues) → 403 « Réservé au rôle « Admin » » ; PUT `/api/planche` → Admin seul. Même règle côté écran (geste annulé + message).
- **Vérifié** : 371/371, tsc, Playwright Animation et Admin (onglets, Changer d'étape, création d'event, 403/200 serveur, planche JEMM, 0 erreur JS), image Docker base vide + redémarrage → `2026-10-03.2`, 0 erreur ; plateforme 24/25 (échec Windows connu).
- **Après mise en ligne** : bouclier MELMIL → cocher **Admin** sur le groupe des gestionnaires (⚠ sinon plus personne n'a les Réglages) ; GREY CELL garde Animation ; FORAD → Lecture et demandes ; reconnexion.

## 2026-10-03 — MELMIL : rôle « Lecture et demandes » pour la FORAD (app-melmil `c3a1446` branche `role-lecture-demandes`, pleiade-platform `da09694` branche `role-lecture-melmil`) — VÉRIFIÉ EN LOCAL, NON POUSSÉ

- **Besoin (utilisateur)** : seule GREY CELL crée storylines et incidents ; la FORAD lit la planche et fait des demandes de produit → colonne dédiée dans le bouclier, à cocher **à la place** d'« Animation ».
- **Catalogue** : `catalog/melmil.yml` + rôle `lecteur` « Lecture et demandes ».
- **Serveur** : `peutEcrire` = Animation seule ; `estLecteur` = lecteur sans Animation. PUT `/api/atelier` d'un lecteur : version obligatoirement à jour (sinon 409), puis `modificationsInterditesAuLecteur` (`src/lib/atelier/lecture-demandes.ts`) → 403 si autre chose que les demandes **de sa cellule** encore « envoyées », leurs fichiers fournis, sa ligne `cellulesDesComptes` et le journal. `/api/medias` : lecteur limité aux fichiers fournis à une demande de sa cellule.
- **Écran** (avis DESIGNER n°35) : pastille « Lecture et demandes », champs en texte, boutons de modification masqués, Écarts/Journal/Réglages masqués, planche non déplaçable, « Demander un produit » en tête de fiche, cellule fixée.
- **Vérifié** : 363/363 tests, tsc OK, Playwright en `for01`/lecteur (tout OK, 403 serveur sur incident et fichier d'incident, 0 erreur JS), image Docker sur base vide + redémarrage → `/api/sante` 200 `2026-10-03.1`, 0 erreur. Tests plateforme 24/25 (l'échec `test-deploiement` existe déjà sur la base : chemin Windows).
- **Après mise en ligne** : bouclier MELMIL → FORAD : décocher Animation, cocher **Lecture et demandes** ; les comptes FORAD se reconnectent.

## 2026-10-03 — Diagnostic plateforme (demande utilisateur) → `PLEIADE\DIAGNOSTIC_2026-10-03.md`

- Contrôle des 12 dépôts + relevé des besoins (RETEX, DELATTRE, journal depuis le 20/09, CYBERSECU, DESIGNER, LEAC, MASTAURIGE) + sondage de la zone `delattre-26` (6 instances au portail + 4 titres de presse ; webserver/wordpress non déployés). 9 constats, 8 axes (A fiabilité de mise en ligne → H hygiène), ordre proposé : A, puis TF1 Info + E1/E4, puis onglet « Conduite » MELMIL (boucle d'entraînement), puis multi-réseaux + cockpit joueur + socle partagé.
- Vérifié : toutes les branches sont fusionnées dans `origin/main` (sauf `feat/eho-data-volume` dans platform) ; les « non fusionnées » du relevé étaient des `main` locaux périmés.

## 2026-10-03 — Réseau social : rôles « Joueurs » et « Modération » dans le bouclier, joueurs autorisés à suivre et à publier avec les avatars de leur camp (social `9350ddc`, eho `afa4766`, pleiade-platform `9714719`) — POUSSÉ, EN LIGNE (eho 23:27, social 23:32)

- **Bouclier de Pléiade (social)** : colonnes **Animation · Joueurs · Modération** + une **légende** sous le tableau (le survol ne suffisait pas), dont « Aucune case » (champ `sansRole` du catalogue). Maquette validée par l'utilisateur.
- **eho** : la décision « au nom de » renvoie aussi `avatarIdsCamp` (groupes du camp seuls), rétrocompatible (messagerie inchangée).
- **Réseau social** : 4 niveaux + Modération, garde-fous CYBERSECU — détail dans `MASTORION\JOURNAL.md` ; 46/46 tests de bout en bout.
- **Ordre de mise en ligne** : eho → Pléiade → social. **Après** : (1) bouclier social : DIV1 → décocher Animation, cocher **Joueurs** ; (2) eho : cocher le camp **DIV1** sur le groupe « CAMP DIV1 » ; (3) les joueurs se reconnectent (rôles relus dans le jeton).

## 2026-10-02 (suite 18) — Cockpit joueur : étude + fuite des messages programmés corrigée dans `app-social` (`cf0f5ee`, `13f1776`) — POUSSÉ, EN LIGNE le 2026-10-02 à 22:26

- **Demande** : un cockpit pour les joueurs (sans la partie admin), pour suivre comptes et hashtags. **Étude** : le cockpit est fermé aux joueurs (rôle analyste) car l'API de veille expose `identity_id` (lien eho entre les comptes d'un même avatar), les groupes (camps) et les **messages programmés**. Sur le réseau social, **suivre est une écriture → réservé à l'animation** (règle de lecture seule du 2026-09-28) : pas de doublon pour les joueurs.
- **Fuite (CYBERSECU E8)** corrigée avec l'autorisation de l'utilisateur — détail dans `MASTORION\JOURNAL.md`. Vérifié sur image : 14 cas conformes, publication à l'heure OK.
- **Captures comparatives** social ↔ cockpit remises à l'utilisateur (`scratchpad\suivi-*.png`).
- 💡 Le réseau social n'expose aucun numéro de version (`/api/config` dit toujours `0.3.0`) : impossible de lire la version en service — à ajouter comme dans MELMIL.
- ❓ En attente : décision sur le mode joueur du cockpit (rôle « joueur » attribué ou automatique ; lire les abonnements du joueur avec son propre compte).

## 2026-10-02 (suite 17) — MELMIL : onglet « Synthèse » de la planification (avis DESIGNER n°34) (`app-melmil` `e743ed5`, `2026-10-02.11`) — POUSSÉ sur main et prod, EN LIGNE

- **Demande de l'utilisateur** : voir en un coup d'œil où en est la planification (nombre d'incidents, en préparation, sans pièce jointe et sans scénario, etc.), nouvel onglet si nécessaire, ergonomie soignée, montré en local.
- **Avis DESIGNER n°34** : onglet **« Synthèse »** en tête de la famille **Visualiser** (l'arrivée reste la planche, décision n°25) ; titre « Où en est la planification ? » ; 4 blocs **Avancement → À traiter → Par storyline → Charge par jour** ; chaque chiffre mène à l'endroit où l'on agit ; jamais un 0 inconnu ; ni jauge, ni camembert, ni score.
- **Calcul** : `lib/atelier/synthese.ts` (pur, testé) — répartition par statut, `partValidee`, manques avec la LISTE des incidents (`non-place`, `fiche-incomplete` [sujet/moyen/émetteur/destinataire, description facultative], `sans-etim`, `sans-piece`, `sans-scenario`, `sans-piece-ni-scenario`), JEMM (`aMarquer`, `horsExport`), storylines (période, à traiter, EXCON), demandes (en cours / en retard / livrées), charge par jour par statut sur toute la période. `idsDuFiltre()` = **le même calcul** pour la synthèse et le filtre de l'onglet Incidents. Scénarios : `codesScenarioDe()` (`lib/ui/scenarios-admin.ts`) → `ok` / `cache` (« d'après la dernière lecture ») / `inconnu` (« scénarios non vérifiés », pas de « sans scénario ») / `chargement` (« … »).
- **Écran** : `components/atelier/synthese.tsx` (`OngletSynthese`, `BarreStatuts` — Validé hachuré, Dans JEMM plein, `role=img` + phrase). Onglet Incidents : nouveau **filtre `manque`** (et `statut`, `storyline`) venu de la synthèse, **non mémorisé**, bandeau « Filtré depuis la synthèse : … · Retirer le filtre · ‹ Retour à la synthèse » ; lien direct `?onglet=gt3&manque=…`. `ecran-atelier.tsx` : onglet `synthese`, état `filtreIncidents`, `ouvrir(cible)`.
- **Testé** (Playwright, données de dev) : « 2 incidents sur 19 sont validés ou dans JEMM (11 %) » ; « 12 sans pièce jointe ni scénario » → **12 lignes** dans Incidents ; légende « Validé » → 08.01.I07 ; ligne 08.01 → ses 7 incidents ; Retirer / Retour OK ; charge : 15 jours dont 9 vides, « Jour le plus chargé : D+28 (5) » ; thème sombre (bouton ☾ réel) ; téléphone 360 px sans défilement horizontal (jours en lignes, colonne Période masquée). 0 erreur JS. 12 tests ajoutés (352/352). Image (base vide) démarrage/redémarrage 200, 0 erreur.
- ❓ **À confirmer par l'utilisateur** (choix par défaut appliqués) : description obligatoire pour une fiche complète ? Synthèse comme onglet d'arrivée ?

## 2026-10-02 (suite 16) — MELMIL : statut d'incident en 4 étapes, repère visuel (avis DESIGNER n°33) (`app-melmil` `ae0304d` + `444dcf4`, `2026-10-02.10`) — POUSSÉ sur main et prod, EN LIGNE

- **Demande de l'utilisateur** : la colonne « Statut » devient un repère visuel de l'avancement : 🟠 **En préparation** (à la création) → 🟡 **En validation** (le rédacteur) → 🟢 **Validé** (chef greycell) → 🟢 « J » **Dans JEMM** (validé et saisi dans JEMM). Modifiable dans la fiche ; **ouvert à tous** (pas de rôle chef/rédacteur dans l'app). Exigence forte : **ne pas alourdir la fiche**.
- **Modèle** (`modele.ts`) : `StatutIncident` = `preparation | validation | valide | jemm`, `lireStatut()` relit les anciens (idée → préparation, à coordonner → validation, coordonné → validé), `ORDRE_STATUT`. Nouveaux champs facultatifs `statutPar` / `statutLe`, posés **seulement** quand le statut change (et à la création) — la `trace` bouge à chaque champ, elle ne dit pas qui a validé. Imports et alignement JEMM créent en « Dans JEMM ».
- **Gestes** (`gestes.ts`) : `modifierIncident` retient qui/quand au changement de statut + journal « passe l'incident X « Validé » » ; `marquerDansJemm(a, ids, par)` (groupé, idempotent).
- **Écran** : composant unique `components/atelier/statut.tsx` — `PastilleStatut` (SVG : quart orange, moitié jaune, disque vert ✓, pastille verte « J »), `StepperStatut` (4 segments en tête de fiche, groupe radio, flèches, un clic, sans confirmation — remplace la liste déroulante de « Quand »), `LigneStatut` (« Validé le 02/10 à 14:32 par gc05 » ; **« Présent dans JEMM — Marquer « Dans JEMM » »** quand le code est dans la planche JEMM ; « ⚠ Absent du dernier export JEMM »), `BandeauJemm` (proposition groupée), `FiltreStatut` (effectifs, mémorisé par poste). Tableau : pastille + mot, colonne triable **dans l'ordre de progression**. Planche de préparation : ⭐ **décision utilisateur** — la pastille de statut **remplace le rond de couleur du moyen d'injection** en haut à gauche de la carte (l'utilisateur ne savait pas ce qu'il signifiait ; en préparation le moyen est presque toujours vide → rond gris). La planche JEMM garde le rond du moyen. Tenu dans une colonne de 103 px : écart 2 px, marge de carte 3 px en style Clair, « Dans JEMM » en rond vert « J » sur la carte (`app-melmil` `444dcf4`). Mesuré : 0 débordement en Clair et Classique (`statutAtelier` transmis par `versPlanche`). Couleurs en jetons `oklch` clair/sombre (`--st-*`).
- ⚠ **JEMM jamais automatique** (doctrine `ecarts.ts` : la vue constate) : MELMIL propose, l'humain décide. `codesJemm` calculé une fois dans `ecran-atelier.tsx`, `null` sans export JEMM.
- **Testé** : 12 tests ajoutés (340/340) ; Playwright : passage par les 4 statuts, ligne qui/quand, flèches clavier, tri, filtre « Validé » → 2 lignes, 17 pastilles sur la planche **sans aucune coupée ni heure tronquée** (mesuré), thème sombre, téléphone 360 px en 2 × 2 sans débordement ; démonstration JEMM (export d'essai `jemm-essai-08` chargé + incidents 08.01.I01/I02 créés **dans l'atelier de dev**) → bandeau « 2 incidents sont présents dans JEMM sans être marqués » et proposition dans la fiche. 0 erreur JS. Image (base vide) démarrage/redémarrage 200, 0 erreur. ESLint : seule l'erreur préexistante du tri reste.
- 🧪 Données de dev laissées en démonstration ; sauvegardes : `scratchpad\at_avant_statut.json` (atelier), `planche_avant_statut.json` (planche JEMM vide).
- 💡 Constat à part (préexistant, non traité) : fiche ouverte, la colonne « Sujet » du tableau est écrasée à quelques lettres par ligne.

## 2026-10-02 (suite 15) — MELMIL : comptes rendus — télécharger l'exemplaire ouvert, garder « Importer… » (avis DESIGNER n°32) (`app-melmil` `eb8dc4f`, `2026-10-02.9`) — POUSSÉ sur main et prod, EN LIGNE

- **Constat de l'utilisateur** : avec plusieurs CR d'un même type pour une ETIM (ex. CIMICREP n°1, n°2), ouvrir n°2 puis « Télécharger » sortait le **n°1**. Et le bouton « Importer » **disparaissait** dès le premier CR de la colonne.
- **Causes** (`compte-rendu.tsx`) : (1) le `onTelecharger` de la fiche ré-étendait à `crsPartages(...)` = **tout le lot**, nommé et commencé par n°1 ; (2) « Importer » n'existait que dans l'état « aucun CR », et `importer()` n'passait pas `exemplaireSuivant` → un 2ᵉ import aurait été **ignoré** (il rendait le CR existant).
- **Correctifs** : la fiche télécharge `[courant]` (l'exemplaire ouvert) ; « .docx (n) » du tableau reste l'export du lot. « Importer… » ajouté après « +1 » dans la cellule quand un CR existe ; `importer()` passe `exemplaireSuivant: true` (crée toujours un exemplaire ; garde d'idempotence par id inchangée). Nom de fichier proposé avec le rang (« CIMICREP n°2 ») pour ne pas écraser n°1. aria-labels avec l'ETIM, « +1 » dit « vide », « Importer… » (points de suspension) dans les deux états. Pas de bouton de téléchargement par exemplaire dans le tableau (R3 : cellule déjà dense).
- **Testé en local** (Playwright, ETIM-7 posée sur 08.01.I04 puis atelier restauré) : créer n°1 (« CONTENU-UN ») → la cellule garde « Importer… » ; +1 → n°2 (« CONTENU-DEUX ») ; fiche n°2 → dialogue « Télécharger le CIMICREP n°2 · ETIM-7 · D+31 », fichier `…-CIMICREP-n°2.docx` qui **contient CONTENU-DEUX et pas CONTENU-UN** ; import de ce fichier avec 2 CR → **n°3** créé. 0 erreur JS. `tsc` OK ; image (base vide) démarrage/redémarrage 200, 0 erreur.

## 2026-10-02 (suite 14) — admin + MELMIL : un scénario peut cibler toute une STORYLINE (avis DESIGNER n°31) (admin `913b992`, MELMIL `f3ee5c0` / `2026-10-02.8`) — POUSSÉ sur main et prod

> ✅ **Mise en ligne** : MELMIL confirmé `2026-10-02.8` sur `melmil.delattre-26.pleiade.internal`. Admin (pas de `/api/sante`) : app up (401 sur service sans clé, 307 sur `/scenarios`), déployée par le même runner et la **même image dont l'entrypoint `db push` crée `storyline_code` + `incident_ids`** (prouvé en local sur base vide ET sur base peuplée). **Compat de l'ancien scénario `08.01`** (créé avant la feature, sans storylineCode/incidentIds) : colonnes nullables ajoutées sans perte ; `incidentIds` retombe sur `[incidentId]` ou `[]`, `codeAffiche`/`scenariosDe` gèrent le null → aucune régression. Vérif end-to-end authentifiée du picto en prod = à faire côté utilisateur (session requise).

- **Constat de l'utilisateur** : un animateur a nommé un scénario `08.01` (toute une storyline, pas un incident). Non anticipé : sur la planche de préparation, l'icône de scénario ne s'affichait alors sur aucun incident. Besoin : **forcer la sélection de l'ensemble d'injects** couverts pour que le picto ▶ apparaisse sur **chacun**. **Ne rien casser.**
- **Avis DESIGNER n°31** (`DESIGNER\AVIS\2026-10-02_ADMIN_SCENARIO_STORYLINE\`) : R1 segment « Cet incident / Toute une storyline » ; R2 storyline → ses incidents en cases à cocher, **tous cochés** par défaut, ≥1 requis ; R3 même picto ▶, sur chaque incident couvert ; R4 fiche « Storyline 08.01 — N incidents », badge « storyline · N » dans la liste ; R5 mode incident unique inchangé.
- **Modèle** (admin, `schema.prisma`) : ajout `storylineCode` + `incidentIds` (Text, liste d'ids internes) au `Scenario`, à côté de `incidentId`/`incidentCode`. Appliqué par **`db push` au démarrage** (admin, comme eho). L'**incident primaire** (= 1er coché) reste dans `incidentId`/`incidentCode` pour toute la compat existante.
- **Admin back** : `lib/melmil.ts` → `incidentsDeStoryline()` + `resoudreCible()` (mode incident OU storyline : filtre les incidentIds sur la storyline, ≥1, primaire = retenus[0]) ; POST et PATCH `bff/scenarios` passent par `resoudreCible` ; `service/scenarios` expose `storylineCode` + `incidentIds`. DTO (`scenario-logic.ts`, `types.ts`) étendus.
- **Admin UI** : `NewScenarioDialog` → segment + sélecteur de storyline + liste à cocher (tous cochés, « Tout cocher/décocher ») ; `ScenarioEditor` montre un bandeau storyline ; `ScenariosList` range sous le code de storyline + badge.
- **MELMIL** : `zone/scenarios/route.ts` calcule l'ensemble `codes` (codes ACTUELS des incidentIds) ; `ui/scenarios-admin.ts` → `scenariosDe` affiche le scénario sur **chaque** code de l'ensemble (sinon le code unique). Picto et bloc inchangés. Version `2026-10-02.8`.
- **Testé en local** (admin+MELMIL+fake Pléiade, Playwright) : storyline 08.01 → **5 incidents, 5 cochés par défaut** ; décoche I12 → 4 ; nom pré-rempli ; créé ; service `storylineCode=08.01`, `incidentIds=4` ; API zone MELMIL `codes=[I03,I04,I07,I15]` ; **planche : picto ▶ 1 sur I03/I04/I07/I15, ABSENT sur I12 décoché** ; badge « storyline · 4 » dans la liste admin ; `tsc` OK les deux ; **0 erreur JS**.

## 2026-10-02 (suite 13) — MELMIL : ergonomie des fichiers fournis (avis DESIGNER n°30) (`app-melmil` `3e0da58`, `2026-10-02.7`) — POUSSÉ sur main et prod

- **Constat de l'utilisateur** : les fichiers fournis d'une demande (ajoutés en suite 12) s'affichaient en **lignes pleine largeur** avec des **liens bleus** — bizarre face à la grille de cartes des médias.
- **Avis DESIGNER n°30** : deux écarts (le bleu `--anneau` banalisé ; la pleine largeur). Corrigé : **grille de cartes compactes** (`minmax(240px,1fr)`, comme `.media-grille`), **boutons neutres** `frappe frappe-mini`, nom en couleur de texte, l'**accent réservé à la sélection** « sert de base » (bordure + coche pleine).
- Version `2026-10-02.7`. Testé en local (3 fichiers → 3 cartes, Ouvrir/Télécharger OK) ; image démarrage/redémarrage 200, 0 erreur.

## 2026-10-02 (suite 12) — MELMIL : les fichiers « fournis » d'une demande se récupèrent (`app-melmil` `482b762`, `2026-10-02.6`, branche `lien-admin`) — POUSSÉ sur main et prod

- **Constat de l'utilisateur** : dans une demande de produit, on peut déposer des fichiers « fournis » (fichiers de base), mais pas les **récupérer**.
- **Cause** : le champ « Fichiers fournis » (genre `fichiers`) ne s'affichait qu'en **pastilles de nom** (sélection), **désactivées en lecture** — aucun lien pour ouvrir/télécharger. La cellule Prod ne pouvait donc pas récupérer les fichiers de base.
- **Correctif** (`produits.tsx`, composant `Champ`) : le champ `fichiers` est séparé de `multi`. Chaque fichier a un lien **« Ouvrir »** (aperçu `inline`) et **« Télécharger »** (pièce jointe), via la route existante `/api/medias/[id]`. En lecture, on montre les fichiers fournis en **liste de liens** (plus de pastilles mortes) ; en édition, la pastille de sélection reste, plus Ouvrir/Télécharger. Styles `.liste-fournis` / `.fourni-*`.
- Version `2026-10-02.6`.
- **Testé en local** : fichier déposé (nom conforme) puis rattaché en « fourni » à une demande directe → la demande montre « Ouvrir » + « Télécharger » ; le téléchargement renvoie le fichier (HTTP 200, `Content-Disposition: attachment`). `tsc` OK ; image (base vide → migrate deploy) démarrage/redémarrage 200, 0 erreur.

## 2026-10-02 (suite 11) — EHO : la fiche de la planche se relit à l'ouverture (`eho` `059a001`, `2026-10-02.3`, branche `fiche-planche-live`) — POUSSÉ sur main et prod

- **Constat de l'utilisateur** : après avoir modifié une bio (ex. @UNOCHA_off) via « Modifier la fiche », la **fenêtre de la fiche dans la planche** (trombinoscope) montrait encore l'ancien texte ; un **rafraîchissement du navigateur** corrigeait. Diagnostic prouvé : la bio ÉTAIT bien enregistrée (écran d'édition + base OK) ; la base et le kit IA étaient à jour. Seule la fiche en lecture de la planche affichait les données du bloc chargées à l'ouverture de la page.
- **Correctif** : `FicheChargee` (trombinoscope) relit **toujours** `/api/users/[id]` à l'ouverture (vide d'abord `fichesEnCache` pour ne pas resservir une copie périmée). La carte du bloc s'affiche aussitôt (ouverture instantanée), la version fraîche la remplace. Plus besoin de recharger la page.
- Version `2026-10-02.3`.
- **Testé en local** : planche chargée, bio modifiée en arrière-plan (sans reload), réouverture de la fiche → nouveau texte affiché (avant le correctif : ancien). `tsc` OK ; image démarrage/redémarrage 200, 0 erreur.
- ⭐ Pour mémoire (réponse à l'animateur) : la **modification d'une bio est bien prise en compte instantanément** par le kit IA (lecture live d'eho). Les cas « pas pris en compte » = kit non re-téléchargé/redéposé dans l'IA, ou cette fiche de planche non rafraîchie (corrigé ici).

## 2026-10-02 (suite 10) — EHO : création d'avatar — email facultatif, fenêtre qui tient avec les groupes archivés (`eho` `79f52d9`, `2026-10-02.2`, branche `creation-avatar`) — POUSSÉ sur main et prod

- **Constats de l'utilisateur** (écran « Nouvel avatar ») : (1) l'email était obligatoire, sans raison — un avatar est une fiche, pas un compte ; (2) « Afficher aussi les groupes archivés » cassait l'affichage de la fenêtre.
- **Corrections** :
  - **Email facultatif**. L'API `POST /api/users` n'exige plus que `username` + `displayName` ; si l'email est vide, repli `username@exercise.local`, exactement comme l'import. Le champ du formulaire perd `required`, placeholder « Email (facultatif — identifiant technique, généré sinon) ».
  - **Plantage de l'affichage** : c'était un débordement. Avec les ~235 groupes de DE LATTRE 26, afficher les archivés faisait sortir la fenêtre de l'écran et rendait « Créer » inatteignable. La fenêtre est désormais à **hauteur bornée** (`max-h-90vh`), **corps défilant**, **liste des groupes** en `max-h-30vh`, et **pied (Annuler / Créer) fixe**.
  - Version `2026-10-02.2`.
- **Testé en local** : création sans email → 201, email `username@exercise.local` (API et via le formulaire) ; avec Playwright (session admin, groupes archivés présents) : email non requis, « Créer » reste visible et dans l'écran après affichage des archivés, 0 erreur ; image sur copie de base → démarrage/redémarrage 200, création sans email 201.

## 2026-10-02 (suite 9) — MELMIL : tableau des incidents triable par colonne (`app-melmil` `b14fa08`, `2026-10-02.5`) — POUSSÉ sur main et prod ; image testée (base vide → migrate deploy OK, redémarrage OK)

- **Demande de l'utilisateur** : dans l'onglet « Incidents », pouvoir ranger le tableau en cliquant sur un en-tête de colonne (Code, Quand, Destinataire, Pièces jointes), avec croissant/décroissant, en gardant « Quand » croissant par défaut.
- **Livré** :
  - `lib/atelier/tri-incidents.ts` : `trierIncidents(incidents, atelier, colonne, sens)`, pur ; défaut `quand`/`asc` (= l'ordre actuel, D+ puis heure) ; « Destinataire » trie sur les ETIM, les incidents sans ETIM toujours en fin ; « Pièces jointes » trie sur le nombre (fichiers + comptes rendus).
  - `onglets-gt.tsx` : composant `ThTri` (en-tête bouton, `aria-sort`, flèche ▲/▼ sur la colonne active) ; état de tri mémorisé par poste (`localStorage` `melmil-incidents-tri`) ; le tri s'applique à chaque storyline. Colonnes Sujet et Statut non triables.
  - Style `.th-tri` / `.th-fleche` dans `globals.css`.
  - Version `2026-10-02.5`.
- **Testé en local** (base jetable, atelier fictif) : 328/328 ; avec Playwright, défaut = Quand croissant (D+27→D+32), clic Code = I03→I15, re-clic = I15→I03, `aria-sort` correct, choix conservé après rechargement, 0 erreur.
- ⚠ Le tri s'applique **à l'intérieur de chaque storyline** (le tableau est groupé par storyline) : c'est le cadre où l'utilisateur lit ses incidents.

## 2026-10-02 (suite 8) — MESSAGERIE : gc01 encore en double dans l’annuaire en ligne (`app-messagerie` `d767342`, branche `doublons-annuaire` partie de `f9a9a45`) — POUSSÉ sur main et prod à la demande de l’utilisateur

- **Constat de l'utilisateur** : sur DE LATTRE 26, gc01 apparaît toujours deux fois dans la liste des comptes, à la création d'une conversation.
- **Cause** : la fusion des fantômes (`f9a9a45`) ne se déclenche qu'à la **connexion** du compte concerné (`noterCompte`). Tant que gc01 ne revient pas sur la messagerie, ses entrées fantômes (identifiants aléatoires d'avant la correction) restent visibles pour tout le monde.
- **Correctif** (`lib/comptes.ts`) :
  - `nettoyerDoublons` : pour chaque nom en double, Pléiade (`resoudre-identite`) indique lequel est un **vrai** compte. Pléiade répond « aucun groupe » pour un identifiant inconnu, et un compte de zone a toujours au moins un groupe. S'il n'y a qu'un vrai compte, les fantômes lui sont rattachés, conversations comprises (`fusionnerDoublons`). Au plus toutes les 5 minutes, depuis la recherche de l'annuaire ; si Pléiade est injoignable, rien n'est touché.
  - `dedoublonner` : l'annuaire n'affiche qu'**une entrée par nom** (la plus récemment vue), et jamais ses propres anciens fantômes (`personas/route.ts`).
  - On n'utilise **pas** `/api/internal/zones/{zone}/users`, qui renvoie les mots de passe en clair.
- **Testé en local** (base jetable, faux Pléiade) :
  - un vrai gc01 et deux fantômes : la liste n'affiche qu'un gc01 ; en base, les fantômes sont fusionnés, et le groupe et le message du fantôme passent au vrai compte ;
  - gc02 avec seulement deux fantômes (jamais revenu) : la liste n'en affiche qu'un, les deux lignes restent en base jusqu'à son retour ;
  - tests 9/9 ; image : `/api/sante` 200, déclarée saine, redémarrage 200, 0 erreur ; avance rapide possible sur main et prod.

## 2026-10-02 (suite 7) — S’approprier des avatars, « Qui utilise quoi », vérification obligatoire (avis DESIGNER n°29) — POUSSÉS : `eho` `e344a19` (`2026-10-02.1`), `app-admin` `d656148`, sur `main` et `prod` — ✅ **EN LIGNE vérifié** : eho `2026-10-02.1` à 13h03 (`/api/appropriations` 401 sans clé, page « Qui utilise quoi » derrière la connexion) ; admin à 13h05 (`/api/bff/appropriations` 401 sans session, `/login` 200, `/avatars` 404 comme voulu)

- **Besoin** : à l'intérieur d'un camp (GREYCELL, FORAD, DIV1…), un compte de zone (gc05, div1…) s'approprie un ou plusieurs avatars que son camp peut déjà utiliser. L'appropriation est facultative. Les animateurs doivent voir qui tient quoi.
- **Existant** : la réservation se fait par **groupe d'avatars** coché pour un camp (`GroupeCamp` dans eho ; « comptes libres » via `CampComptesLibres`). Le kit IA choisit le périmètre par groupes (`KitIaDialog`) et ignore toute notion de titulaire.
- **Décisions de l'utilisateur** :
  - **bloquer** : seul le titulaire, et les animateurs, utilise un avatar réservé ;
  - libération par le titulaire ou par les **animateurs** (rôle admin), avec « Tout libérer » ;
  - **eho et kit IA d'abord**, les sélecteurs du réseau social, de la presse et de la messagerie ensuite.
- **Proposition** :
  - stockage dans eho (un titulaire au plus par avatar : compte de zone, camp, date) ;
  - API lue par les apps ;
  - bouton ☆/★ et filtre « Mes avatars » dans eho ;
  - vue animateur par camp, avec Libérer et Tout libérer ;
  - kit IA : les avatars réservés par d'autres sont écartés et annoncés, ceux du compte en tête ;
  - blocage vérifié par le serveur.
- ⚠ **Le blocage ne sera réel qu'à l'étape 2.** C'est au moment de l'incarnation, dans le social, la presse et la messagerie, qu'on utilise un avatar. L'étape 1 ne bloque que dans le kit IA.
- 🔒 Le lien est compte ↔ avatar, jamais personne réelle ↔ avatar.
- **Préalable** : faire valider par Xavier le stockage dans eho (et, plus tard, le contrôle dans le réseau social).
- **Réalisé en local le même jour** (branches `appropriation-avatars` dans `eho`, partie de `2209b45`, et dans `app-admin`, partie de `7d6d96f` ; ⏳ non commité, non poussé). L'utilisateur a demandé de tester en local, et rappelé que **les joueurs ne doivent rien voir**.
  - ⭐ **Recadrage par DESIGNER** : la donnée vit dans eho, l'**écran est dans l'admin**.
    - L'admin est réservée à l'animation : l'invisibilité pour les joueurs est garantie par construction.
    - C'est là que travaillent les comptes gc. Ils n'ont peut-être pas accès aux écrans d'administration d'eho.
    - Le blocage devient réel dès l'étape 1, puisque l'admin publie au nom des avatars.
  - **eho** :
    - modèle `Appropriation` (avatarId en clé primaire : un seul titulaire ; compteId = `sub`, compte, camp, depuis) ;
    - `lib/appropriation.ts` (`approprier` : 404 si l'avatar n'existe pas, 409 s'il est déjà réservé, 403 hors camp via `avatarsImpersonables`, 503 si Pléiade est injoignable ; `liberer`, `libererTout`, journal `ActivityLog`) ;
    - `resoudreAupresDePleiade` exporté ;
    - routes `/api/appropriations` (GET : clé ou administrateur d'eho ; POST et DELETE : clé seulement) et `/api/appropriations/[avatarId]` ;
    - ⛔ **rien dans `/api/users`**, lisible de toute session (vérifié).
  - **admin** :
    - `lib/appropriations.ts` (`refusDUtilisation` = le blocage : l'avatar d'un autre est refusé sauf animateur ; `avatarsOuverts` pour prévenir l'erreur) ;
    - BFF `/api/bff/appropriations` (GET, `?ouverts` ; POST ; DELETE `?camp=` ou `?tout=1`, animateurs) et `/[avatarId]` (le titulaire ou un animateur) ;
    - **blocage serveur** à l'ajout ou au changement d'avatar d'un item et à l'import (ligne refusée) ;
    - **kit IA** : `appliquerReservations` (avatars des autres retirés, « ★ Tes avatars » en tête, nombre de retirés annoncé) et résumé avant le téléchargement ;
    - nouvel onglet **Avatars** (`/avatars`) : « Mes avatars », « S'approprier un avatar » (chaque résultat dit son état : ☆ à prendre, ★ à moi, 🔒 réservé par un autre et grisé, « Hors de votre camp »), « Qui utilise quoi » par camp et par compte, avec recherche dans les deux sens, Libérer et Tout libérer avec confirmation ;
    - sélecteur d'avatar des scénarios : les miens en tête, ceux des autres grisés et non cliquables ;
    - mode local : `ADMIN_DEV_ROLES` et `ADMIN_DEV_ID`.
  - **Testé en local** : MariaDB jetable, eho (3913) avec un faux Pléiade (3990) pour les camps, admin (3400) en gc05 opérateur puis en anim01 animateur ; 12 avatars et 3 camps fictifs.
    - Tests : admin 30/30, eho 112/112 ; `tsc` sans erreur dans les deux apps.
    - API : 401 sans clé, 409 si déjà réservé, 403 hors camp, rien dans `/api/users`.
    - Avec Playwright :
      - gc05 : appropriation, avatar de gc03 grisé et sans bouton, hors camp annoncé d'emblée, item avec l'avatar de gc03 refusé (403), résumé du kit (« 2 retirés, vos 2 en tête ») ;
      - animateur : Libérer un avatar, Tout libérer un camp avec confirmation ;
      - aucun débordement au téléphone (corrigé).
  - ⭐ **Même jour, demande de l'utilisateur : s'approprier DEPUIS eho.** Les animateurs consultent la planche « Avatars » d'eho : devoir changer d'application pour s'approprier un avatar était dommage. Réalisé, l'admin gardant sa section ; une seule donnée, visible des deux côtés.
    - **Planche** (`trombinoscope`) : un **marque-page** (l'étoile ★ appartient déjà au package STARTEX) en **languette centrée sous la carte**, posé à côté du bouton de la carte et non dedans. Libre : visible au survol ou au clavier (toujours sur écran tactile) ; « À moi » plein ; « gc03 » en pointillé pour l'avatar d'un autre ; rien hors du camp ; masqué pendant la sélection STARTEX. La grille des cartes a été retouchée (`flex`, `gap-y-4`).
    - **Fiche** : ligne d'état (« Libre pour votre camp » et « Me l'approprier », « À moi depuis… » et « Libérer », « Réservé par gc03… — demandez à un organisateur », « Hors de votre camp »).
    - **Liste** : l'étiquette après le @compte.
    - **Menu Animation** : « **Qui utilise quoi** » (`/appropriations`), par camp et par compte, avec recherche dans les deux sens, Libérer et Tout libérer pour les organisateurs.
    - **Routes eho** :
      - POST par un animateur connecté (pour lui-même) ou par la clé ;
      - DELETE d'un avatar par son titulaire, par un **organisateur** (masteradmin via Pléiade, `estOrganisateur`) ou par la clé ;
      - Tout libérer par un organisateur ou par la clé ;
      - GET renvoie aussi `moi` et `ouverts` (avatars du camp) pour une session.
    - Composant partagé `components/appropriation.tsx` : une seule interrogation pour la page ; messages par `role=alert`, jamais `alert()`.
    - ⚠ **Différence assumée** : dans eho, libérer l'avatar d'un autre est réservé aux **organisateurs** (masteradmin). eho ne distingue pas un compte gc d'un chef d'animation : tous ont le rôle admin d'eho. Dans l'admin de zone, c'est le **rôle admin** de l'admin.
    - **Testé en local**, avec des sessions d'essai signées par la clé locale (gc05 animateur, org01 organisateur, div1 joueur) :
      - gc05 : 12 cartes ; marque-page au survol, un clic donne « À moi » ; aucun marque-page sur une carte hors camp ; la fiche affiche l'état ; la liste montre les étiquettes ; libérer l'avatar de gc03 est refusé (403) ;
      - org01 : « Tout libérer » visible ; libérer l'avatar de gc03 fonctionne ;
      - **div1, joueur** : `/api/appropriations` en 403, renvoyé hors des pages Animation, aucun marque-page ni le mot « Réservé » dans « Mon EHO » ;
      - eho 112/112 ; `tsc` sans erreur ; 0 erreur dans le navigateur.
  - ⭐ **Même jour : l'onglet « Avatars » de l'admin est RETIRÉ** (décision de l'utilisateur, après confirmation que **tous** les comptes qui préparent des scénarios ont accès à la planche d'eho). Un seul écran pour un même geste, une seule règle de libération (celle d'eho).
    - **Restent dans l'admin, en lecture** : le **kit IA** (avatars des autres retirés, les miens en tête, résumé avant le téléchargement), le **sélecteur d'avatar** des scénarios (étiquettes, avatars des autres grisés, lien « Gérer mes avatars dans eho ↗ » vers `/trombinoscope`) et le **blocage serveur** (items et import).
    - **Supprimés** : `src/app/avatars`, `AvatarsAppropriation.tsx`, les routes BFF d'écriture (POST, DELETE et `/[avatarId]` ; un POST répond maintenant 405), `approprier`, `liberer`, `libererTout` et `avatarsOuverts` côté admin, et les styles `.pa-av-*`.
    - **Ajout** : `ehoPublicUrl()` (discovery) ; le GET BFF renvoie `ehoUrl`.
    - Admin 30/30, `tsc` sans erreur ; `/avatars` répond 404 et l'onglet a disparu.
  - ⭐ **Même jour : le blocage dur est remplacé par une consigne et un avertissement** (décision de l'utilisateur).
    - **Kit IA** : les avatars réservés par d'autres comptes **restent**, marqués « 🔒 RÉSERVÉ (gc03) — seulement si la demande le nomme ». La consigne `CONSIGNE_RESERVES` figure dans `1_AVATARS.md`, dans `2_MODE_EMPLOI.md` et dans `5_MODELE_DE_PROMPT.txt` (« n'en utilise AUCUN, sauf ceux que je nomme ici : [@compte… ou « aucun »] »). Les miens restent en tête (★). Le résumé du dialogue : « n avatars signalés 🔒 : l'IA ne les utilisera que si vous les nommez ». `appliquerReservations(appropriations, moiId)` renvoie `{ aMoi, autres }`.
    - **« Vérifier »** : `avertissementsReserves` (lib/appropriations) ajoute un message par avatar réservé par un **autre** compte que l'opérateur, animateurs compris, avec les items concernés. Il n'est **pas bloquant** et s'affiche dans un **encadré orange à part** (« n avatars réservés par un autre compte — vérifiez que c'est voulu », `estAvatarReserve` dans `verification.ts`). `validateScenario(id, op)`.
    - **Plus de refus** à l'ajout, au changement d'avatar ou à l'import : `refusDUtilisation` est supprimée. **Sélecteur** : l'avatar d'un autre compte demande une confirmation sur place (« réservé par gc03. L'utiliser quand même ? »).
    - Tests admin 31/31 (kit : avatar gardé et signalé, consigne présente dans les trois documents) ; `tsc` sans erreur. Kit téléchargé et vérifié ; encadré de « Vérifier » vérifié avec Playwright (Brenz/gc03 pour les items #1 et #3, Mira/gc05 pour le #2 ; un avatar libre ne donne aucun message).
  - ⭐ **Même jour : « Vérifier » devient OBLIGATOIRE avant « Lancer »** (décision de l'utilisateur). Constat : on pouvait lancer sans vérifier. Au lancement, le serveur relançait bien la vérification, mais ne refusait que les erreurs bloquantes ; les avertissements n'étaient jamais montrés.
    - Base : `Scenario.verifieLe` et `verifieEmpreinte` (facultatifs). `lib/empreinte.ts` calcule `empreinteScenario` = SHA-256 des items (qui, où, quoi, délai, réponse, likes et boosts, média) et de la greffe ; le **début n'en fait pas partie** (« Maintenant » le décale). `validateScenario` enregistre l'empreinte vérifiée.
    - **Serveur** : `start` répond **409 `aVerifier`** si le scénario n'a jamais été vérifié, ou si son contenu a changé depuis (« Le scénario a changé depuis la dernière vérification… »). Le DTO de la fiche expose `verifie` et `verifieLe`.
    - **Écran** :
      - tant que ce n'est pas fait, « Vérifier » devient l'action principale et « Lancer » est **grisé** ;
      - un message orange au-dessus des boutons (« Vérifiez le scénario avant de le lancer » ou « Modifié depuis la vérification : vérifiez à nouveau ») ;
      - la **fenêtre « Lancer » rappelle les avertissements** (avatars réservés 🔒 compris), et la case « J'ai pris connaissance de ces avertissements » est **obligatoire** pour lancer.
    - **Testé** : API sans vérification → 409 ; avec Playwright, Lancer est grisé, puis actif après vérification, puis de nouveau grisé après une modification d'item ; dans la fenêtre, Lancer reste grisé tant que la case n'est pas cochée. Admin 31/31, `tsc` sans erreur.
  - ⚠ **À trancher à l'étape 2** : si un **joueur** s'approprie un compte « libre », il bloque l'animation dans l'admin. Il faudra sans doute limiter le blocage au camp du titulaire. Aujourd'hui, les joueurs n'ont aucun accès à l'admin.

## 2026-10-02 (suite 6) — ADMIN ↔ MELMIL : un scénario est lié à un incident MELMIL (avis DESIGNER n°27 et n°28) — POUSSÉS : `app-admin` `7d6d96f`, `app-melmil` `c27d368` (`2026-10-02.4`) sur `main` et `prod`

- **Demande de l'utilisateur** : l'admin récupère les incidents de MELMIL, on choisit l'incident à la création, et MELMIL a un bouton vers les scénarios.
- **Décisions** :
  - incident **obligatoire** (sauf dans une zone sans MELMIL) ;
  - bouton MELMIL **avec le nombre et l'état** ;
  - **rattachement automatique** des anciens scénarios dont le nom porte un code connu.
- **MELMIL** :
  - `lib/atelier/service-incidents.ts` (`incidentsPourService`, **anonyme** : code, sujet, storyline, event, D+, heure, jour ; testé) ;
  - `GET /api/service/incidents`, protégée par la clé de la zone (`lib/zone/cle-service.ts`, comparaison à temps constant) ;
  - `lib/zone/scenarios-admin.ts` : découverte de l'admin auprès de Pléiade, appel serveur à serveur ; en local, `MELMIL_DEV_ADMIN_URL` ;
  - `GET /api/zone/scenarios`, réservée aux sessions MELMIL, qui ajoute le **code actuel** retrouvé par l'identifiant ;
  - `lib/ui/scenarios-admin.ts` : une seule interrogation toutes les 30 s pour toute la page ;
  - `components/scenarios-incident.tsx` : `PictoScenarios` (« ▶ n » au pied de la carte, vert si un scénario est en lecture) et `BlocScenarios` (fiche d'incident et détail d'une carte : état, nom, créneau, « Ouvrir ↗ », « + Créer un scénario pour cet incident ↗ ») ;
  - jeton CSS `--direct`.
- **Admin** :
  - base : `Scenario.incidentId` et `incidentCode` (facultatifs, avec index) ;
  - `lib/melmil.ts` : `incidentsMelmil` (cache de 20 s, dernière liste gardée), `trouverIncident` (par identifiant ou par code normalisé), `rattacherAuxIncidents` (rattachement automatique et mise à jour du code recodé, seulement si MELMIL a répondu) ;
  - `GET /api/bff/incidents`, qui donne aussi le nombre de scénarios par incident ;
  - POST `/api/bff/scenarios` : incident obligatoire, 503 si MELMIL est injoignable ; PATCH : on peut changer d'incident, pas le retirer ;
  - `GET /api/service/scenarios` (clé de la zone, `lib/service-auth.ts`) : ni auteur, ni contenu ;
  - `components/IncidentPicker.tsx` : `IncidentPicker` (combobox avec recherche « 08.01.04 », groupes par storyline titrée, « n scénarios », clavier), `EtiquetteIncident`, `BandeauIncident` (fiche du scénario : MELMIL ↗, Changer, rattacher un ancien) ;
  - formulaire de création : l'incident d'abord ; nom (« code — sujet ») et début (jour et heure de l'incident) pré-remplis ; `?nouveau=<id|code>` ouvre le formulaire pré-rempli ;
  - liste : rangée par l'incident lié ; titres MELMIL dans les en-têtes ; une relance garde son code sous son incident ; un code seulement deviné est en pointillés.
- **Testé en local** : MariaDB jetable, MELMIL (port 3801) et admin (3400) reliés par une clé de zone d'essai, 17 incidents et 27 scénarios fictifs.
  - Tests : MELMIL 322/322, admin 27/27 ; `tsc` sans erreur dans les deux apps.
  - Sécurité : la route de service MELMIL répond 401 sans clé ou avec une mauvaise clé, celle de l'admin 401 sans clé.
  - Rattachement automatique : 22 scénarios rattachés.
  - Avec Playwright :
    - « Créer » est désactivé sans incident ; « 08.01.15 » trouve I15, « pont » trouve I07 ;
    - le choix se fait au clavier, nom et début sont pré-remplis, la création aboutit, la fiche affiche le bandeau ;
    - l'API refuse un scénario sans incident (400) ;
    - un ancien scénario se rattache depuis sa fiche ;
    - MELMIL : 16 cartes portent « ▶ », dont 3 en direct, avec l'infobulle « 3 scénarios · 1 en lecture » ; le bloc de la fiche s'affiche ; « Créer un scénario pour cet incident » ouvre l'admin pré-remplie ;
    - aucun débordement au téléphone.
- **Test d'image avant le push** :
  - admin, sur une base à l'**ancien format** contenant des données : démarrage 200, les colonnes `incident_id` et `incident_code` sont ajoutées par le `db push` de démarrage (sans `--accept-data-loss`), les données sont conservées ; redémarrage 200 ; 0 erreur ;
  - MELMIL : `/api/sante` = `2026-10-02.4` au démarrage et au redémarrage ; les routes de service répondent 401 sans clé et 200 avec la clé ; 0 erreur.
- ⚠ **À vérifier en zone** : l'admin découvre MELMIL et MELMIL découvre l'admin auprès de Pléiade, par les `appType` « melmil » et « admin » du catalogue. Cette découverte n'a pas pu être rejouée hors zone : en local, le lien a été testé avec `ADMIN_DEV_INSTANCES` et `MELMIL_DEV_ADMIN_URL`.

## 2026-10-02 (suite 5) — ADMIN : scénarios rangés par code MELMIL (avis DESIGNER n°27) — POUSSÉ avec la suite 6 (`app-admin` `7d6d96f`)

- **Besoin** : on ne retrouve plus ses scénarios dans la masse ; on les cherche par incident MELMIL, et les noms commencent par le code.
- **Livré en local** :
  - `src/lib/codes-melmil.ts` : `lireCode`, `ranger`, `comparerCodes`, `estRelance`, avec 7 tests (`scripts/test-codes-melmil.mts`) ;
  - `ScenariosList.tsx` réécrit : groupes Event › Storyline repliables, avec effectif, nombre en lecture et en erreur ; une ligne par scénario (code, nom, statut, créneau, publiés, auteur, corbeille) ; lien étiré, toute la ligne ouvre ; relances décalées sous leur incident ; « Non classés » à la fin, avec la consigne ;
  - recherche « Code (08.01, I04…) ou nom », qui cherche aussi l'auteur ; effectifs sur les filtres ; « Tout déplier / Tout replier » ;
  - affichage mémorisé par poste (`localStorage` `admin.scenarios.affichage`) ;
  - dialogue de création : modèle « 08.01.I04 — … » et remarque « Rangé sous 08.01.I15 » ou « ira dans Non classés » ;
  - styles `.pa-scn-*` dans `globals.css`.
- **Testé en local** :
  - MariaDB jetable et 25 scénarios fictifs ; `tsc` sans erreur ; 25 tests sur 25 ;
  - avec Playwright : la recherche « 07.02 » donne 5 lignes ; un groupe replié le reste après rechargement ; un clic sur la ligne ouvre `/scenarios/14` ; aucun débordement horizontal au téléphone ; 0 erreur dans la console.
- Aucun changement de base de données.
- **Demande de l'utilisateur (même session)** : « 08.01.04 », « 08.01.i04 » et « 08.01.I04 » doivent se ranger au même endroit, pour qu'un « I » oublié ne crée pas de doublon.
  - `lireCode` rajoute le `I` et redresse la minuscule ; le code affiché est toujours la forme normalisée.
  - À code égal, le tri se fait par titre.
  - `normaliserRecherche` : taper « 08.01.04 » trouve aussi « 08.01.I04 ».
  - ⚠ Effet de bord accepté : l'ancien format « 07.05.02i » se lit désormais « 07.05.I02i », toujours rangé sous son incident.
  - 27 tests sur 27 ; vérifié à l'écran : « 08.01.04 — … » se range sous 08.01.I04, et « 08.01.i07 — … » sous 08.01.I07.

## 2026-10-02 (suite 4) — Identité aléatoire : messagerie, admin, LEAC, MELMIL et press POUSSÉS sur `main` et `prod` (branches `identite-sub`) — ✅ MELMIL `2026-10-02.3` et LEAC `2026-10-02.1` vérifiés EN LIGNE vers 09h50 ; admin `/login` 200 ; press non vérifiable (pas de marque de version)

- **Messagerie** : `f9a9a45` poussé sur `main` et `prod` à la demande de l'utilisateur.
- **Correction des 4 autres apps** : même correctif du callback `jwt` (sub Keycloak, sessions d'avant closes une fois, fournisseur de type credentials inchangé).
  - `app-admin` `e3c24f8`, sur `origin/main` ;
  - `app-melmil` `deb7ff3` + `282836a` (version `2026-10-02.3`) ;
  - `app-press` `42dbb9a`, sur `origin/main` ;
  - `app-leac` `db7738c` + `da5c4f6` (`2026-10-02.1`), avec en plus le **recollage** des affectations, administrations, références, appareils et opérations (voir `LEAC\JOURNAL.md`).
- ⚠ Pour admin et press, `origin/main` a **1 commit de Xavier pas encore sur `prod`** (« Épingler le CLI Prisma du build ») : pousser sur `prod` le mettra aussi en ligne.
- **Tests locaux** :
  - `tsc` sans erreur ; tests : admin 18/18, press 8/8, MELMIL 320/320, LEAC 468/468 ;
  - callback `jwt` simulé, par un module bouchon de `next-auth` : 5/5 dans chaque app. Contre-épreuve : l'ancien code de press échoue à 4 sur 5 ;
  - recollage LEAC sur la base locale avec des données fictives : 6/6 ;
  - images lancées avec une MariaDB jetable : `/api/sante` 200 au démarrage et au redémarrage pour LEAC, MELMIL et press ; admin n'a pas de `/api/sante`, mais `/login` et `/api/auth/*` répondent 200 avant et après redémarrage ; 0 erreur dans les journaux.
- **Non testé** : la vraie connexion Keycloak de bout en bout dans ces 4 apps. La messagerie l'a validée pour le même motif. Pour ces 4 apps, le garde-fou refuse de manipuler les identifiants d'administration du Keycloak local.
- Constat sans lien avec la correction : `/app/src` (admin, LEAC, press) et des `*.config.*` (MELMIL) sont présents dans le standalone ; ils l'étaient déjà avant, et les images démarrent.

## 2026-10-02 (suite 3) — MESSAGERIE : le même compte (gc01) apparaît deux fois, ouvert sur Chrome et sur Edge (`app-messagerie` `f9a9a45`, branche `compte-double` partie de `origin/main` `cedbb47`, ⏳ non poussé)

- **Cause** : `auth.ts` prenait pour identité `user.id`. Or Auth.js v5, sans base de comptes, donne à `user.id` un **UUID aléatoire à chaque connexion OAuth**. Résultat : chaque connexion créait une nouvelle identité. Les conversations ne suivaient pas d'un navigateur à l'autre, et l'annuaire montrait des doublons.
- **Correctif** :
  - `jwt` prend `profile.sub` ou `account.providerAccountId`, c'est-à-dire le `sub` Keycloak. Le fournisseur « token » garde `user.id`, qui porte déjà le sub.
  - Marqueur `idv: 2` : une session antérieure est close une fois, puis l'authentification unique de Keycloak reconnecte sans mot de passe.
  - `comptes.ts` : `fusionnerDoublons` rattache au vrai compte, en une transaction par fantôme, les identités fantômes de même nom (membres en gardant la lecture la plus avancée, messages, réactions, médias, invitations). La ligne fantôme est ensuite supprimée.
- **Test local** :
  - avec le vrai Keycloak local (client et compte d'essai, supprimés ensuite) : l'ancien code donne 2 entrées aléatoires ;
  - avec le nouveau : 1 seule entrée au vrai sub, et le groupe comme le message du fantôme sont rattachés et visibles des deux navigateurs ;
  - 9 tests sur 9 ; image : démarrage 200, redémarrage 200.
- ⚠ **Même défaut dans 4 autres apps** (`token.sub = user.id` après `profile.sub`) : `app-admin/src/lib/auth.ts:62-63`, `app-leac/src/lib/zone/auth.ts:55-56`, `app-melmil/src/lib/zone/auth.ts:43-44`, `app-press/src/lib/auth.ts:57-58`. Aucune n'est corrigée pour l'instant ; c'est signalé à l'utilisateur et consigné chez CYBERSECU.

## 2026-10-02 (suite 2) — MESSAGERIE : le bouton « Activer » des notifications paraissait figé (`app-messagerie` `cedbb47`, branche `notifications-bouton` partie de `origin/main`, ⏳ non poussé)

- **Constat des utilisateurs** : on ne peut pas cliquer sur « Activer », le bouton semble figé.
- **Diagnostic, reproduit en local** avec Chromium, Chrome et Edge en vrai :
  - le bouton est **cliquable** (`elementFromPoint` atteint le bouton) et le clic lance bien `Notification.requestPermission()` ;
  - **le défaut est ce qui suit** : l'écran n'affichait aucune réaction. La fenêtre « Autoriser » s'ouvre en haut à gauche, loin du bouton. Si on la ferme sans répondre, le résultat est `default` et le bandeau reste inchangé. Chrome et Edge peuvent aussi **masquer** la demande (cloche barrée dans la barre d'adresse), et la promesse reste alors en suspens.
  - Hypothèse supplémentaire, non vérifiable d'ici : un poste sans le certificat de la zone peut se voir refuser les notifications.
- **Correctif** (avis DESIGNER n°26) dans `useAlertes.ts` et `ConversationList.tsx` :
  - nouveaux états `en-cours` et `ignoree` ;
  - un message dit où cliquer ; **après 4 s**, il ajoute la piste de la demande masquée (cloche barrée ou cadenas, puis Autoriser) ;
  - « fermée sans réponse » est annoncé, et le bouton reste disponible ;
  - en cas de refus, la marche à suivre pour réautoriser s'affiche ;
  - l'état réel est relu au focus, au retour sur l'onglet et à chaque changement signalé par `navigator.permissions` : autoriser depuis la barre d'adresse suffit ;
  - l'ancienne forme à rappel de `requestPermission` (Safari) est prise en charge.
- **Testé** :
  - Playwright, avec 4 cas simulés : masquée (message, puis piste à 4 s), fermée (message et bouton), autorisée (le bandeau disparaît), refusée (marche à suivre) ;
  - 9 sur 9 ;
  - image : démarrage et redémarrage OK.
- ⚠ La branche `main` locale de la messagerie porte toujours `b322f54` (déconnexion), jamais poussé : le travail repart d'`origin/main`.
- ✅ **En ligne le 2026-10-02 à 08h58** : push en avance rapide (`main` et `prod` `9fd56cf..cedbb47`).
  - Le redémarrage a été observé, l'application est stable. Le nouveau texte est présent dans un chunk servi (`2wluclildhlzg.js`).
  - L'environnement local est arrêté (dev, faux EHO) et la base `msg_essai` supprimée.
  - **L'utilisateur teste lui-même sur les comptes qui n'avaient pas réussi** : résultat à consigner.

## 2026-10-02 (suite) — MELMIL : l'accueil ouvre la planification, sur la planche de préparation (`app-melmil` `b3b74af`, branche `accueil-planification`, `2026-10-02.2`, ⏳ non poussé)

- **Constat de l'utilisateur** : la vue de travail principale est la **planche de préparation**, mais MELMIL s'ouvrait sur la **planche JEMM**. Vérifié dans le code : la planification ouvrait ensuite l'onglet du GT courant, c'est-à-dire Incidents pendant l'exercice. Cela faisait **deux clics à chaque arrivée**.
- **Décisions de l'utilisateur** : la planification ouvre **toujours** la planche, et l'accueil devient la planification.
- **Code** :
  - `(planche)/page.tsx` est déplacé en `(planche)/jemm/page.tsx` ;
  - le nouveau `(planche)/page.tsx` redirige vers `/preparation` **en conservant les paramètres**, pour que le lien `?onglet=demandes` du bandeau marche toujours ;
  - `nav-app.tsx` : JEMM pointe vers `/jemm`, et `espaceDe` repère `/jemm` ;
  - `ecran-atelier.tsx` : l'onglet par défaut est `"planche"`, et `?onglet=` accepte tous les onglets (`ONGLETS_VALIDES`). L'ordre et la place des onglets ne changent pas.
- **Testé** :
  - redirections : `/` donne 307 vers `/preparation` ; `/?onglet=demandes&demande=abc` est redirigé avec ses paramètres ;
  - Playwright : arrivée sur la planche ; « Planche JEMM » mène à `/jemm` ; « Planification » ramène sur la planche ; lien demandes ; `?onglet=gt3` ouvre Incidents ; le logo ramène sur la planche ;
  - 320 sur 320 ;
  - image : démarrage et redémarrage OK ; sans session, `/` et `/jemm` envoient vers `/connexion`, ce qui est attendu.
- Démonstration ouverte pour l'utilisateur sur `localhost:3801` (base `melmil_demo_accueil`), validée par l'utilisateur.
- ✅ **En ligne le 2026-10-02 à 08h45** : push en avance rapide (`main` et `prod` `189f4a3..b3b74af`), `/api/sante` renvoie `2026-10-02.2`, stable. Sans session, `/` envoie vers `/connexion`, puis la connexion ramène vers `/`, donc vers la planification. La démonstration locale est arrêtée et la base supprimée.

## 2026-10-02 — MELMIL : agrafe des pièces jointes dans la liste des incidents (`app-melmil` `01f5bd4`, branche `agrafe-pieces-jointes`, `2026-10-02.1`, ⏳ non poussé)

- **Demande** : dans le tableau des incidents, afficher une agrafe sur l'incident qui a une pièce jointe, avec le nombre à partir de 2.
- **Code** : `onglets-gt.tsx`. Le composant `Agrafe` (SVG dessiné, sans dépendance) se place **après le sujet**, ce qui le garde visible sur tablette et sur téléphone, où les dernières colonnes se masquent.
  - Le compte porte sur les `medias` dont l'incident est celui de la ligne.
  - Le texte « n pièces jointes » est fourni en `aria-label` et au survol : l'icône n'est jamais seule (doctrine DESIGNER n°10).
  - CSS : `.agrafe` et `.agrafe-nombre`.
- **Testé** :
  - 317 sur 317 ;
  - Playwright sur un atelier fictif « EXERCICE DEMO AGRAFE » : 1 pièce jointe donne l'agrafe seule, 2 donnent « 2 », 3 donnent « 3 », 0 ne montre rien ;
  - image : démarrage et redémarrage OK, aucune erreur.
  - ⚠ Au premier essai, mes identifiants de démonstration faisaient moins de 8 caractères et MELMIL écartait les pièces jointes (comportement voulu) ; c'est corrigé dans le jeu d'essai.
- Démonstration ouverte pour l'utilisateur sur `localhost:3801` (base `melmil_demo_pj`).
- **Précision de l'utilisateur** : il voulait l'agrafe **sur la planche de préparation, en bas à droite de la carte de l'incident**, mais garde aussi celle du tableau. Il demande de consulter DESIGNER (avis n°23).
- **Ajout** (`9e377a6`) :
  - `Inject.pieces` est posé par `versPlanche`, comme `etims` : planification seulement, jamais enregistré sur la planche JEMM ;
  - composant commun `components/agrafe.tsx` (SVG, nombre à partir de 2, texte `sr-only`) ;
  - carte : dernière ligne `i-pied`, avec les ETIM à gauche et l'agrafe calée à droite ; infobulle complétée ;
  - même agrafe dans la liste par jour du téléphone ; le tableau utilise le composant commun.
  - ⚠ La couleur du nombre définie pour le tableau s'appliquait aux cartes colorées : corrigé en `color: inherit`.
- **Testé** :
  - Playwright, styles Clair et Classique et téléphone : agrafes sur 08.01.I01, I02 (« 2 ») et I03 (« 3 »), rien sur I04 ;
  - 317 sur 317 ;
  - image : démarrage et redémarrage OK.
- **Suite, même journée** (`189f4a3`, avis DESIGNER n°24) :
  - **Constat de l'utilisateur** : un compte rendu créé n'apparaissait pas dans la colonne « CR ». **Défaut réel** : elle ne comptait que les anciens comptes rendus (`incident` = id), pas les comptes rendus partagés par jour et par ETIM.
  - **Décision de l'utilisateur** : un compte rendu est une pièce jointe. La colonne devient **« Pièces jointes »**, avec l'agrafe en en-tête. Elle compte les fichiers et les comptes rendus (`lib/atelier/pieces-jointes.ts` : `piecesDeLIncident`, `detailPieces`, testé). Le détail s'affiche au survol, et la colonne reste visible sur téléphone.
  - L'agrafe placée après le sujet **quitte le tableau** : une seule indication par ligne. La carte de la planche compte de la même façon.
  - Testé : 320 sur 320. Avec Playwright, la création d'un PSYREP sur 08.01.I04 fait aussitôt apparaître l'agrafe (« 1 pièce jointe : 1 compte rendu »), et la planche suit. Image : démarrage et redémarrage OK.
- ✅ **En ligne le 2026-10-02 à 08h30** : push en avance rapide (`main` et `prod` `d9d5187..189f4a3`, qui emporte `01f5bd4`, `9e377a6` et `189f4a3`). `/api/sante` renvoie `2026-10-02.1`, stable. La démonstration locale est arrêtée et la base supprimée.

## 2026-10-01 (suite 21) — MELMIL : alignement JEMM sans perte (sauvegarde, dates, pièces jointes de l'export) (`app-melmil` `d9d5187`, branche `alignement-sur-et-pieces`, `2026-10-01.13`, ⏳ non poussé)

- **Demande** : un nouvel export JEMM (`EXER\DELATTRE 26\01_Montage exercice\JEMM\01.10.26`, events 07 et 08, 66 injects, 4 PDF sur l'event 08) doit mettre à jour la planification **sans perdre** les déplacements, les ETIM, les pièces jointes et les comptes rendus. Les pièces jointes JEMM doivent être ajoutées aux bons incidents si MELMIL ne les a pas.
- **Analyse** :
  - l'alignement garde déjà ETIM, comptes rendus, pièces jointes et demandes (renumérotation, même identifiant) ;
  - **il écrase en revanche le jour et l'heure**. L'utilisateur confirme que les déplacements sont **aussi dans JEMM**, donc JEMM fait foi ;
  - il supprime les events absents des fichiers choisis ;
  - il n'importait pas les pièces jointes.
- **Ajouts** :
  1. **Sauvegarde et restauration** de l'atelier dans Réglages (`SauvegardeAtelier`, JSON `melmil-sauvegarde-atelier`, confirmation qui dit ce qui revient ; les pièces jointes restent sur le serveur ; le fichier contient les noms de l'Équipe, à garder en lieu sûr).
  2. `alignerSurJemm` : option `garderDates` (défaut JEMM) et `bilan.datesChangees` ; les suppressions s'affichent en alerte rouge.
  3. **Pièces jointes JEMM** (`lib/melmil/pieces-jemm.ts`) :
     - `piecesJointesJemm` lit `Injections[].Attachments` ;
     - `repartirPieces` place chaque pièce sur l'incident du même code, sauf si elle y est déjà (même nom, une fois mis en règle ou non, ou même taille et même type) ;
     - `nomConforme` insère le NMR, parce que le serveur **impose la règle de nommage** (refus en 400 constaté au premier essai) ; une cellule inconnue donne une pièce « à nommer à la main » ;
     - `fichierDeLaPiece` va chercher le fichier dans `attachments/<Id>/` ;
     - le dépôt se fait après l'application (`envoyerFichier`, désormais exporté), suivi d'un `ajouterMedia`.
  4. On choisit le **dossier** de l'export (`webkitdirectory`), ou des fichiers.
- **Tests** : 317 sur 317, dont 13 nouveaux (dates, pièces jointes, noms conformes).
- **Essai complet sur l'export RÉEL du 01.10.26**, avec un atelier **fictif** construit depuis cet export (ETIM, un compte rendu, 1 PDF déjà présent, un ancien event 05 fictif) :
  - bilan : 66 incidents inchangés, event 05 supprimé (en alerte), « 3 à ajouter, 1 déjà dans MELMIL » ;
  - après « Appliquer » : **3 PDF déposés sur 08.01.I02, I03 et I07** sous un nom conforme (`…-GYC-0801I02-UNOCHA-LETTER-(08-01-01).pdf`), avec les bonnes tailles ; le PDF déjà présent n'est pas dupliqué ; ETIM et comptes rendus intacts ;
  - **restauration** de la sauvegarde : on revient exactement à 3 events et 68 incidents ;
  - image : démarrage et redémarrage OK, aucune erreur.
  - ⚠ Incident de test sans conséquence : le chargement SQL de mon atelier de démonstration cassait le JSON, car MariaDB interprète les barres obliques inverses ; c'est corrigé dans le script de chargement.
- Démonstration ouverte pour l'utilisateur sur `localhost:3801` (base `melmil_demo_align`).
- Questions de l'utilisateur, réponses vérifiées :
  - les textes viennent bien de JEMM : sujet, description, effet attendu, émetteur, moyen et destinataires (66 sur 66) ; récit (8 sur 8) ; description d'event (2 sur 2). Les effets attendus, QUI / OÙ et la coordination des storylines restent ceux de MELMIL. Seule exception : l'objectif principal d'une storyline, gardé si JEMM est vide ;
  - le retour en arrière passe par la sauvegarde, à télécharger **avant**. La restauration remplace tout pour tous les postes ; les PDF ne sont pas dans le fichier ; la Planche JEMM est hors champ.
- ✅ **En ligne à 18h55** : push en avance rapide (`main` et `prod` `507164c..d9d5187`), `/api/sante` renvoie `2026-10-01.13`, stable. La démonstration locale est arrêtée, la base et les fichiers de test supprimés.

## 2026-10-01 (suite 20) — MELMIL : supprimer un compte rendu, et plusieurs exemplaires par jour et par ETIM (`app-melmil` `507164c`, branche `cr-plusieurs-et-suppression`, `2026-10-01.12`, ⏳ non poussé)

- **Demande** :
  - pouvoir **supprimer** un compte rendu créé par erreur (un PSYREP au lieu d'un CIMICREP) ;
  - pouvoir faire **plusieurs** comptes rendus dans la journée pour une même ETIM (« +1 »), téléchargés dans **un seul fichier**.
- **Décisions de l'utilisateur** : un **seul fichier Word** (un exemplaire par page, sans LibreOffice) ; le « +1 » vaut pour les **trois types**.
- **Code** :
  - `gestes.ts` : `crsPartages` (les exemplaires dans l'ordre de création), option `exemplaireSuivant` de `creerCompteRenduPartage`, et `nomCompteRendu` numérote « n°k » dès qu'il y a deux exemplaires ;
  - `docx.ts` : `exporterDocxPlusieurs` remplit le modèle par exemplaire, recopie les corps avant le `w:sectPr` avec un saut de page, et retire les signets des copies ; `exporterDocx` le délègue ;
  - `compte-rendu.tsx` : la case affiche « Ouvrir », ou « n°1 n°2… » ; boutons « +1 » et « .docx (n) » ; un bouton **Supprimer** dans la fiche, avec une confirmation qui cite les incidents qui partagent le compte rendu ; le téléchargement depuis la fiche emporte tous les exemplaires du jour.
- **Testé** :
  - 304 sur 304, dont 6 nouveaux : « +1 », numérotation, exemplaire vierge, pas de doublon sans « +1 », suppression, trace au journal ;
  - Playwright sur un atelier fictif « EXERCICE DEMO CR », avec 2 CIMICREP pour ETIM 9 BIMa à D+33 :
    - « .docx (2) » produit `20261012_MR_DL26_SITCEN-GYC-0801I01-CIMICREP.docx` ;
    - **ouvert dans Word (COM)** : 4 pages (le modèle vierge en fait 2), 2 tableaux, les deux contenus distincts présents, export PDF propre ;
    - « +1 » sur le PSYREP ouvre « PSYREP n°3 », puis Supprimer, confirmation et retour à 2 ;
  - image : démarrage et redémarrage OK, aucune erreur.
- Démonstration ouverte pour l'utilisateur sur `localhost:3801` (base `melmil_demo_cr`, fictive), validée par l'utilisateur.
- ✅ **En ligne à 18h26** : push en avance rapide (`main` et `prod` `d6c1fe3..507164c`), `/api/sante` renvoie `2026-10-01.12`, stable. La démonstration locale est arrêtée et la base supprimée.

## 2026-10-01 (suite 19) — MELMIL : colonne « Destinataire » dans la liste des incidents (`app-melmil` `d6c1fe3`, branche `colonne-destinataire`, `2026-10-01.11`, ⏳ non poussé)

- **Demande** : ajouter une colonne « DESTINATAIRE » aux colonnes Code, Quand et Sujet, qui reçoit les ETIM cochées, lesquelles quittent la colonne « Sujet ».
- **Code** :
  - `onglets-gt.tsx` : un `<th>` Destinataire et une cellule `col-destinataire` avec `EtiquettesEtims`, ou « — » quand il n'y a pas d'ETIM ; le sujet est seul dans sa cellule ;
  - CSS `.col-destinataire` de 13rem.
- **Testé** :
  - 298 sur 298 ;
  - Playwright sur un atelier fictif « EXERCICE DEMO DESTINATAIRE » : les en-têtes sont Code · Quand · Sujet · Destinataire · Statut · CR, et les étiquettes ETIM sont bien dans la colonne ;
  - image : démarrage et redémarrage OK, aucune erreur.
- Démonstration ouverte pour l'utilisateur sur `localhost:3801` (base `melmil_demo_dest`, fictive), validée par l'utilisateur.
- ✅ **En ligne à 18h09** : push en avance rapide (`main` et `prod` `be43962..d6c1fe3`), `/api/sante` renvoie `2026-10-01.11`, stable. La démonstration locale est arrêtée et la base supprimée.

## 2026-10-01 (suite 18) — MELMIL : anonymat des comptes, option A (`app-melmil` `be43962`, branche `anonymat-comptes`, `2026-10-01.10`, ⏳ non poussé)

- **Demande (sécurité)** : MELMIL reliait les comptes anonymes (gc01) à « CNE X » dans l'Équipe, et les demandes stockaient le compte à côté du nom. L'utilisateur a choisi l'**option A** : couper le lien. Le signal se fait par **cellule**, comme je l'avais recommandé.
- **Code** :
  - `modele.ts` : `Membre` sans `compte` ni `compteId` ; ajout de `cellulesDesComptes` et de `contientLiensComptes` ; suppression de `membreDuCompte` ;
  - `produits/modele.ts` : `Demandeur` sans `compteId`, et `demandeurChoisi(nom, cellule)` remplace `demandeurDe` ;
  - `creerDemande` retient la cellule du compte ;
  - `nommage.ts` : `celluleDuCompte` remplace `celluleDuMembre` ;
  - `signaux.ts` : `miennes` est calculé par cellule ;
  - `lireAtelier` purge la base ;
  - Équipe : la section « Compte Pléiade » et l'appel à `/api/zone/comptes` sont retirés ;
  - formulaire de demande : champ « Demandeur » avec une `datalist` alimentée par l'Équipe ;
  - le nommage et l'export de compte rendu retiennent la cellule (`retenirCelluleDuCompte`).
- **Tests** : 298 sur 298, dont 9 nouveaux « anonymat » : détection, effacement, conservation du reste, demande sans compte, cellule retenue sans nom, signal par cellule.
- **Test local complet** :
  - **purge sur une vraie base** avec un atelier **fictif** (« gc99 ↔ CNE FICTIF Alpha ») : la base passe de la version 5 à la 6, `gc99` et `compteId` disparaissent, et les noms, grades, notes et demandes restent intacts ;
  - Playwright : la fiche Équipe n'a plus de section compte ; le champ « Demandeur » propose les noms de l'Équipe ; une demande envoyée est enregistrée sous la forme `{"nom":"LTN FICTIF Bravo","cellule":"GREY CELL"}`, **sans `compteId` en base**, avec `cellulesDesComptes` = `{dev → GREYCELL}` ; le nom n'est retenu que dans le navigateur ;
  - image : démarrage en 2 s, migrations appliquées, redémarrage OK, aucune erreur.
- ⚠ **Aucune donnée réelle lue.** La purge des données réelles se fera **sur le serveur, à la première lecture après la mise en ligne**.
- L'utilisateur a vu la démonstration locale (atelier fictif « EXERCICE DEMO ANONYMAT ») et l'a validée.
- ✅ **En ligne à 18h00** : push autorisé, en avance rapide (`main` et `prod` `4a1af66..be43962`). `/api/sante` renvoie `2026-10-01.10` avec `medias: ok`, stable.
  - La purge des liens réels se fait **sur le serveur, à la première lecture de l'atelier**. Je ne l'ai pas vérifiée moi-même : il aurait fallu lire des données réelles et confidentielles.
  - L'environnement de démonstration local est arrêté et la base `melmil_demo_anon` supprimée.

## 2026-10-01 (suite 17) — MESSAGERIE : liste en direct, « on me parle » en orange, titre des conversations privées, alertes hors de l'onglet (`app-messagerie` `d69df60` + `c47a3bf` + `9fd56cf`, branche `liste-en-direct` partie de `origin/main` `90207e2`) — ✅ **EN LIGNE à 17h19**

- ✅ **Push autorisé par l'utilisateur** : avance rapide, `main` `90207e2..9fd56cf` et `prod` `412dbae..9fd56cf`.
  - Redémarrage observé sur `messagerie.delattre-26` : 404 de 17h19 à 17h19m33, puis 200, stable.
  - La messagerie n'expose pas de version. La mise en ligne est confirmée par le **contenu servi** : le texte des alertes est présent dans un chunk public (`/_next/static/chunks/22kj73uwczou7.js`).
  - L'environnement de démonstration local est arrêté (dev, faux EHO, robot) et la base `msg_essai` supprimée.
  - Le commit de déconnexion `b322f54` **n'est pas inclus** : il n'a pas été demandé.

- **Cause** : `/api/flux` abonne le flux aux conversations qui existent **à son ouverture**. Une nouvelle conversation, celle du premier message de quelqu'un, n'y figurait pas, et rien n'arrivait avant de recharger la page.
- **Correctif** :
  - `lib/bus.ts` : un **canal personnel** par identité (`prevenirIdentite`, `abonnerIdentite`) ;
  - `ensureMember` envoie `added` à la personne ajoutée, et `/api/flux` abonne aussi ce canal ;
  - côté client, sur `added` ou sur `hello` (chaque reconnexion), la liste est relue ; `useFlux` prend une clé `abonnement` (les ids de la liste), et le flux se rouvre abonné au nouveau fil ;
  - un filet de sécurité relit la liste toutes les 30 s, même quand le flux est vivant.
- **Orange (avis DESIGNER n°22)** :
  - `ms-conv-nouveau` : voile orange et liseré pulsé, pastille orange à texte sombre ;
  - point orange sur l'onglet Canaux ou Discussions ;
  - « (n) » dans le titre du navigateur ;
  - « réduire les animations » respecté.
- **Bug trouvé pendant le test** : le titre d'un direct, choisi par le créateur, est **le nom du destinataire**. Le destinataire voyait donc son propre nom. `titresDesDirects` donne maintenant le nom de l'autre membre, dans la liste et dans la fiche.
- **Tests** :
  - 9 sur 9, dont 3 nouveaux dans `scripts/test-bus.mts` ;
  - `tsc` sans erreur ; eslint est sans configuration dans ce dépôt, c'était déjà le cas avant.
- **Test local complet** :
  - image sans `*.config.*` ; démarrage en 2 s ; `docker restart` OK ; aucune erreur dans les journaux ;
  - Playwright sur un dev local, avec un **faux EHO** (deux personas, « au nom de » autorisé) : Paul ouvre une conversation privée et écrit. Chez moi, sans rechargement, le fil apparaît en moins d'une seconde, en orange, avec la pastille 1, puis 2, et « (1) Messagerie ». À l'ouverture, l'orange disparaît. En mouvement réduit, l'animation est à `none`. Le titre affiché est « Paul ESSAI ».
- **Ajout dans la même session : alertes hors de l'onglet** (`9fd56cf`, `components/chat/useAlertes.ts`) :
  - **notification du système** quand un fil (ni muet, ni archivé) gagne des non-lus et que l'onglet est caché ou sans focus ; un clic ramène sur l'onglet et ouvre le fil ;
  - bandeau « **Activer** » tant que l'autorisation n'est pas donnée (elle ne s'obtient que sur un clic), et une ligne d'aide si elle a été refusée ;
  - **clignotement de l'onglet** : le titre alterne entre « 💬 X vous écrit » et « (n) Messagerie », et l'icône SVG prend un point orange, chaque seconde, jusqu'au retour. Hors clignotement, l'onglet garde « (n) » et le point orange tant qu'il reste des non-lus ;
  - ⚠ **un fil ouvert dans un onglet caché ne se marque plus lu tout seul** (`useVisible`). Sinon aucune alerte ne partait ; le fil se marque lu au retour.
  - Tests :
    - Playwright invisible : le titre alterne bien, l'icône a son point orange, et au retour le fil est marqué lu, le titre redevient « Messagerie » et le point disparaît ;
    - ⚠ le **Chromium invisible refuse toujours les notifications** (`permission: denied`). La notification a donc été testée avec un **navigateur visible** hors écran : la notification « Paul ESSAI : … » part bien, et le bandeau disparaît une fois l'autorisation donnée ;
    - image : démarrage, redémarrage, aucune erreur.
  - **Démonstration locale** pour l'utilisateur : dev sur `localhost:3930`, faux EHO sur 3913, et un robot (`scratchpad/robot-messages.mjs`) où Paul écrit en privé toutes les 45 s et Julie dans le groupe « Cellule ILI (essai) » tous les 3 messages, 20 envois en tout.
- **À noter** :
  - les résultats de recherche affichent encore le titre enregistré pour un direct (`recherche/route.ts`) ;
  - le commit local de déconnexion `b322f54` (branche `main` locale) n'est toujours pas poussé.

## 2026-10-01 (suite 16) — EHO : « Erreur lors de la sauvegarde » sur une fiche d'avatar (`eho` `a64c565`, `2026-10-01.2`, branche `import-portraits-integres`, ⏳ non poussé)

- **Reproduit en local** : la page `users/[id]` renvoie la fiche ENTIÈRE servie par GET, dont `groups`, qui est un tableau d'objets groupe. `prisma.user.update` refuse alors l'argument (`Argument groups: Invalid value… UserGroupUpdateManyWithoutUserNestedInput`), d'où une erreur 500. **Toute sauvegarde échouait.**
- **Correctif** dans `api/users/[id]/route.ts` :
  - liste blanche `CHAMPS_MODIFIABLES` (les colonnes de `User`), les groupes passant par `groupIds` ;
  - `avatarUrl` rangé en chemin avec `cheminPortrait` (GET le sert en adresse absolue) ;
  - erreur P2000 : réponse 400 « Texte trop long… (191 caractères au plus) » ;
  - la page affiche le message du serveur.
- **Test local complet** :
  - 112 tests, `tsc` et `eslint` sans erreur ;
  - l'image construite depuis la branche (qui contient aussi `243b72e`) ne contient ni `*.config.*` ni `src/` complet ;
  - démarrage en 2 s ;
  - avec 24 commandants importés, les PATCH reproduisent exactement la page : sauvegarde 200 et vérifiée en base (bio, caractère, portrait en chemin, 3 groupes), retrait d'un groupe 200, texte trop long 400.
- **Push à valider** par l'utilisateur ou Xavier. Il emportera `243b72e` et `a64c565`.
- ✅ **Feu vert de l'utilisateur, mis en ligne à 16h47.**
  - Au `fetch`, Xavier avait poussé **sur `prod` seulement** deux commits : `303fefd`, qui ajoute `NODE_PATH=/app/prisma-cli/node_modules` au `db push`, et `9f177b6`, qui épingle `prisma@7.10.0` et `dotenv@18.0.3`. **C'était la vraie correction de la boucle de redémarrage** (dérive de dotenv 17 vers 18 au rebuild).
  - J'ai remis mes deux commits par-dessus (rebase) : ils deviennent `eb633b3` et `2209b45`.
  - L'image combinée a été retestée en local : démarrage en 2 s, **`docker restart`** OK, aucune erreur dans les journaux, imports OK, sauvegarde 200.
  - Push en avance rapide : `main` `6451f97..2209b45`, `prod` `9f177b6..2209b45`.
  - Sur le serveur, `2026-10-01.2` répond à 16h47, et l'EHO, le réseau social et MELMIL restent à 200 au fil des contrôles.

## 2026-10-01 (suite 15) — MELMIL : retrait du « confié à » (`app-melmil` `c44ffbc` + `4a1af66`, branche `retrait-confie-a`, `2026-10-01.9`, ⏳ non poussé)

- **Demande** : supprimer le fonctionnement « confié à » : la cellule de l'event, le « confié à » de la storyline et celui de l'incident. **Garder les ETIM concernées et le système de comptes rendus.**
- **Écrans** :
  - `onglets-gt.tsx` : le bloc Cellule de l'event, le « Confiée à » de la storyline, le « non confiée » du résumé (ce résumé est réécrit avec des séparateurs « · »), la colonne et la section « Confié à » de l'incident, et le texte d'aide de GT1 ;
  - `equipe.tsx` : les rubriques « Confié » et « Events portés » ;
  - `champs.tsx` : `ChoixGroupes`, `ChoixPersonnes` et `AncienConfie` sont supprimés ;
  - le CSS `col-confie`.
- **Logique** :
  - `equipe.ts` : `choixPourEvent/Storyline/Incident`, `gestionnairesDeLIncident`, `confieA`, `celluleDeLEvent`, `groupesDeLEvent/LaStoryline` sont supprimés ;
  - `nommage.ts` : `celluleDeLIncident` est supprimé (et retiré de `celluleExport` dans `produits.tsx`) ;
  - `versPlanche` : `cellule: ""` ;
  - `aligner.ts` et `importer.ts` : `groupes: []`.
- **Modèle inchangé**, pour relire les anciens ateliers sans perte.
- **Tests** : 290 sur 290. Le bloc « confié » est remplacé par 4 tests de retrait : planche sans cellule, ETIM conservées, JEMM sans coche, ancien atelier relu.
- **Test local complet (règle du jour)** :
  - `tsc` et `eslint` sans erreur ;
  - image construite, de même contenu que la version en ligne `c67edc6` (MELMIL charge `prisma.config.mjs` explicitement, donc il n'est pas exposé au défaut de l'EHO) ;
  - démarrage réel avec base et volume de médias : `/api/sante` répond 200 en 3 s, et le conteneur est « healthy » ;
  - **Playwright** sur le MELMIL local, avec des données fictives :
    - Events sans « Cellule » ;
    - Storylines et tableau des incidents sans « Confié à » ;
    - fiche d'incident avec les **ETIM concernées** et le tableau « **Comptes rendus du jour** » (PSYREP, CIMICREP, SCAMR) intacts.
- ✅ **En ligne à 16h31** : push autorisé (`c67edc6..4a1af66` sur `main` et `prod`), et `/api/sante` renvoie `2026-10-01.9` avec `medias: ok`.

## 2026-10-01 (suite 14) — EHO : 26 commandants de Mercure à ajouter (Profils HVI), import avec portraits intégrés (`eho` `6451f97`, `2026-10-01.1`, branche `import-portraits-integres`, ⏳ non poussé)

- **Demande** : ajouter à l'EHO de PLÉIADE les chefs militaires de Mercure du PDF `CREATION\02 - MERCURE\Portraits\20260303_NP_GLM26_SITCEN_RENS_Profils-HVI-MER.pdf` (UNCLASSIFIED, 30 profils) qui n'y sont pas encore. L'utilisateur capturera ensuite la base courante.
- **Comparaison** avec la copie locale du modèle SKOLKAN FULL PERSONA du 25/09 (3 983 avatars) : 4 présents (PRUNIERE, ZHUKOV, KALEVA, MILANOV) et **26 absents**. Détail chez l'Analyste Mercure (§ 1.5.ter).
- **Décisions de l'utilisateur** : portraits **repris tels quels**, bien que ce soient probablement de vraies photos et des noms proches de vrais généraux (risque signalé) ; portraits **intégrés au fichier d'import**.
- **`eho`** : `lib/portrait-integre.ts`. Une cellule `avatar_url` en `data:image/png|jpeg|webp;base64` est enregistrée comme un dépôt (uuid, `UPLOADS_DIR`, 5 Mo au plus). Le SVG est refusé, et une image refusée fait échouer la ligne. L'appel est branché dans `api/import` avant `versPrisma`.
- **Fichier** : `IMPORT_EHO_26_commandants_MER_HVI.xlsx`, avec une planche de contrôle `…_planche.png`, rangé à côté du PDF.
  - Portraits réduits à 240 px en JPEG, environ 8 à 16 Ko par cellule.
  - Le portrait est choisi par sa **position** sous le cartouche du nom : sur certaines pages, la plus grande image est l'**emblème au griffon**, et le premier essai l'avait prise pour 9 pages. La correction a été vérifiée : 26 portraits distincts.
- **Vérifié** : la cellule relue par ExcelJS est enregistrée (`/api/uploads/….jpg`), une adresse ordinaire reste une adresse, le SVG est refusé ; 112 tests ; `tsc` ; build Docker.
- **Suite** : push de l'eho (à valider), puis l'utilisateur fait **EHO → Importer** du fichier, puis capture la base.
- ⛔ **INCIDENT (15h00)** : push sur `main` et `prod` autorisé (`c0a3ea2..6451f97`). Ensuite, l'EHO de DE LATTRE répond **404 pendant plus de 20 minutes** ; MELMIL et le réseau social fonctionnent.
  - La cause n'est pas établie : je n'ai pas accès aux journaux du serveur.
  - **Xavier a pris l'incident en main.** Consigne de l'utilisateur : **ne plus toucher à l'eho**.
  - **Faute de méthode reconnue** : l'image avait été construite mais **jamais démarrée** en local, ni avec une base, ni avec un volume, et aucun import n'avait été rejoué. J'avais écrit à tort « elle démarre ».
  - **Nouvelle règle** : tout est testé en local avant un push (mémoire auto `feedback_tester_en_local_avant_push.md`).
  - Le fichier d'import des 26 commandants reste prêt, **en attente**.
  - ✅ **Résolu** par Xavier : c'était un **problème de cache**, pas le changement de code. L'EHO répond de nouveau ; `/api/sante` renvoie `2026-10-01.1`, donc les portraits intégrés sont en ligne. La règle « tester en local avant de pousser » reste en vigueur.
- **Import sur le serveur (utilisateur)** : 24 créés, **2 refusés** (`coldimitrimikhailovic`, `bgkristianmikhelev`). Motif : `caractere` dépasse 191 caractères (VarChar par défaut).
  - Cause : l'extraction du PDF avait aspiré du texte de mise en page (« 410 TANK BN ASSESSMENT PRO: 70 % … COMBATIVENESS … ») dans les vulnérabilités, et dans 4 autres fiches.
  - Correctif de données : `IMPORT_EHO_HVI_2a_CORRECTIF_24.xlsx` est une mise à jour des 24 **sans la colonne `avatar_url`** (la photo reste intacte, puisque `versPrisma` ignore une colonne absente). `IMPORT_EHO_HVI_2b_COMPLEMENT_2.xlsx` contient les 2 refusés, complets.
  - Il reste 2 fichiers photo orphelins sur le serveur : le portrait est enregistré avant l'échec de la ligne. C'est sans gravité.
- ⭐ **TEST LOCAL (première application de la nouvelle règle)** : l'image `6451f97` **NE DÉMARRE PAS** en local. Message : `Failed to load config file "/app/prisma7.config.ts" … Cannot find module 'dotenv/config'`.
  - Cause : l'accès disque à chemin dynamique de `lib/portrait-integre.ts`, **sans `turbopackIgnore`**, fait embarquer **tout le projet** dans la sortie standalone, dont `prisma7.config.ts` et `src/`. Le `db push` de démarrage charge alors ce fichier, échoue, et le conteneur s'arrête.
  - L'image de `c0a3ea2` n'a pas ce défaut.
  - ⇒ C'est **très probablement la vraie cause du 404 de 15h**. Le « cache » a pu masquer le problème.
  - **Correctif local `243b72e`** (branche `import-portraits-integres`, **NON poussé** : consigne de ne plus toucher à l'eho) : annotation `turbopackIgnore` sur le `mkdir` et le `writeFile`.
  - Validé en local :
    - l'image ne contient plus de `*.config.*` ;
    - `/api/sante` répond 200 en 2 s ;
    - les 3 imports rejoués donnent 24 créés + 2 refusés (reproduction exacte), puis 24 mis à jour, puis 2 créés ;
    - en base : 26 avatars, 26 portraits servis en `image/jpeg`, aucun résidu de mise en page, les 3 groupes × 26.
  - **Risque** : si l'image qui tourne en prod contient `/app/prisma7.config.ts`, le prochain redémarrage de l'EHO échouera. À vérifier par Xavier (`ls /app/prisma7.config.ts` dans le conteneur).
  - **Décision de l'utilisateur** : garder `243b72e` en réserve et **l'intégrer à la prochaine mise à jour de l'EHO**. C'est noté dans la mémoire auto `project_eho_correctif_en_attente.md`.

## 2026-10-01 (suite 13) — MELMIL : les comptes rendus téléchargés suivent le nommage des pièces jointes (`c67edc6`, `2026-10-01.8`, ✅ en ligne à 14:26)

- **Décision de l'utilisateur** : `AAAAMMJJ_MR_DL26_SITCEN-GYC|FOR-<code incident>-<Titre>.docx`.
  - **Date** : celle de l'incident, modifiable.
  - **NMR** : code de l'incident. Pour un compte rendu partagé, c'est **l'incident de la fiche ouverte**.
  - **Titre** : le nom du compte rendu (« PSYREP », « CIMICREP », « SCAMR »), modifiable.
- **Écran** : `DialogueExportCr` (date, cellule « nom (code) », titre, nom final en direct) s'ouvre sur **tous** les téléchargements : tableau du jour, fiche ouverte, anciens comptes rendus. `useQui` est maintenant exporté par `produits.tsx`.
- **Vérifié** : Playwright (06.01.I01 à D+33 donne `20261012_MR_DL26_SITCEN-FOR-0601I01-PSYREP.docx` ; titre modifié repris ; fichier téléchargé sous ce nom) ; 302 tests ; build Docker.
- Mise en ligne autorisée dans le même message que celle du SCAMR.

## 2026-10-01 (suite 12) — MELMIL : PROTOTYPE du compte rendu SCAMR (CRI propagande) (`1feb372` + `736f544`, `2026-10-01.7`, ✅ validé par l utilisateur et en ligne à 14:21 ; le modèle `/modeles-cr/scamr.docx` est servi)

- **Demande** : intégrer `EXER\DELATTRE 26\01_Montage exercice\SCAMR.png` comme nouveau compte rendu « SCAMR » pour les ETIM, **au format exactement identique**, avec un prototype à tester d'abord.
- **Fait** :
  - le **modèle Word est reconstruit à l'identique** par `scripts/modele-scamr.py` (`public/modeles-cr/scamr.docx`, un seul tableau, police Arial). Il n'existait pas de `.docx` ;
  - `scripts/gabarits-cr.py` lit désormais les cellules **sans bordure** (`nb`) et le **centrage vertical** (`va`). PSYREP et CIMICREP gagnent ainsi le centrage de leurs modèles, avec le même nombre de cases (21 et 167) ;
  - type `scamr` (8 cases) ajouté dans `TYPES_CR`, la relecture, l'import (reconnu par « PROPAGANDE ») et `CelluleFiche` ;
  - comme PSYREP et CIMICREP : un SCAMR **par jour et par ETIM**, l'unité pré-remplie avec le nom de l'ETIM, le GDH de la découverte à saisir.
- **Vérifié en local** :
  - rendu Word du modèle, comparé à l'image ;
  - fiche MELMIL à l'écran ;
  - export `.docx` rempli puis rendu par Word, avec les valeurs aux bonnes cases ;
  - 302 tests.
- ⚠ **`Modèle SCAMR.pptx`** contient en diapo 3 le même formulaire que l'image, mais **en diapo 1 un AUTRE modèle** (« SUJET OBSERVATION » : source, métriques, contenu, analyse, liste d'adressage CRINF). **Consigne de l'utilisateur : ne prendre en compte QUE l'image SCAMR.png, pas le PPT.** Le prototype en est tiré uniquement.
- Copie de test : `EXER\DELATTRE 26\01_Montage exercice\SCAMR_prototype_vierge.docx`.

## 2026-10-01 (suite 11) — Cockpit vide : il ne trouvait aucun réseau social (`app-cockpit` `58a11c7` + `a5e8cce`, `app-social` `b7851c0`, ✅ en ligne : social redémarré à 13:33, cockpit à 13:35)

- **Choix de l'utilisateur** : un **filtre « À partir du »**.
- **Fait dans `app-cockpit`, `a5e8cce`** : réglage dans le pied de page, mémorisé dans le navigateur (`ck_depuis`, comme les autres réglages du cockpit) ; `debutDepuis()`.
  - Les posts antérieurs n'entrent ni dans les sources ni dans les non-lus (`addToots`), et ceux déjà stockés sont retirés à la saisie de la date ;
  - le fil en direct les écarte ;
  - les **totaux** transmettent `?since=` au réseau ;
  - le rapport part par défaut de cette date ;
  - les tendances portent déjà sur les 3 dernières heures, sans changement.
- **Fait dans `app-social`, `b7851c0`** : `GET /api/cockpit/stats?since=` compte les posts et commentaires postérieurs ; sans paramètre, rien ne change.
- `tsc` et builds Docker OK pour les deux.

- **Question de l'utilisateur** : le cockpit est-il relié à admin ou aux apps ? Il ne voit rien, alors que le réseau social contient les anciennes publications d'ORION : est-ce un bug ?
- **Réponse** :
  - le cockpit n'est relié **ni à admin ni à la presse**. Il lit **les réseaux sociaux** de la zone (API `/api/cockpit/*` du social, clé de service de la zone), découverts auprès de PLÉIADE (`/api/internal/zones/:zone/instances`) ;
  - le vide était un **BUG** : la découverte ne gardait que `appType === "mastorion"`, alors que le catalogue nomme le réseau `social` depuis le renommage du 16/09. Aucune instance n'était trouvée et aucune erreur ne s'affichait.
- **Correctif** : les types `social` et `mastorion` sont acceptés. `tsc` et build Docker OK.
- ⚠ **Conséquence à annoncer** : une fois corrigé, le fil en direct et les statistiques afficheront les publications **les plus récentes** du réseau, donc les anciennes d'ORION tant que DE LATTRE n'a rien publié. L'utilisateur préfère ne voir que DE LATTRE : un filtre « à partir du » lui est proposé.

## 2026-10-01 (suite 10) — Cockpit : « There is a problem with the server configuration » (`app-cockpit` `ddc73b7`, ✅ poussé sur main + prod ; l instance a redémarré entre 13:05:03 et 13:05:34)

- **Constat** : instance cockpit ajoutée à DE LATTRE 26, page d'erreur Auth.js « Server error / problem with the server configuration ».
- **Diagnostic sans compte** :
  - `/api/auth/csrf` répond 200 ;
  - la connexion simulée redirige bien vers Keycloak (`client_id=cockpit-cockpit`) ;
  - c'est donc le **retour** qui échoue : **défaut connu, noté dans la règle du 21/09 mais jamais corrigé sur cockpit**. `auth.ts` déclarait `issuer: ISSUER` (adresse interne), alors que Keycloak signe avec l'émetteur public.
- **Correctif** : `issuer: PUBLIC_ISSUER`. Token, userinfo et JWKS restent sur l'adresse interne, comme la presse. `tsc` et build Docker OK.
- Parti de **`origin/main`** : ma copie locale de `main` porte `9dab9da` (« Se déconnecter ferme aussi la session Keycloak »), jamais publié et non inclus ici.
- **Après mise en ligne** : il faut le rôle **`analyste`** (« Veille ») sur l'instance cockpit, à cocher dans PLÉIADE. Sans lui, la connexion aboutit mais l'accès est refusé.
- **Droits GitHub** sur `app-cockpit` : push réel **accepté** le 01/10. Tous les dépôts testés sont ouverts.

## 2026-10-01 (suite 9) — MELMIL : le NMR du nommage devient le code de l'incident (`dea3dd6`, `2026-10-01.6`, ✅ en ligne à 12:54 — `/api/sante` vérifié)

- **Décision de l'utilisateur**, qui remplace le NNN par incident du matin :
  - NMR = **code de l'incident sans points** (`08.01.I01` donne `0801I01`) ;
  - **code seul**, sans numéro de pièce, choix assumé : deux fichiers de même titre sur un incident ont le même nom ;
  - pour une demande **sans incident**, le numéro de pièce (`001`…).
- **`nommage.ts`** : `MOTIF` accepte un NMR alphanumérique ; ajout de `nmrIncident`, `nmrPiece`, `nmrDepuisNom`, `nmrAttendu` ; `nomDeFichier({…, nmr})`. **`nomExport` corrige le NMR** d'un nom conforme mais faux (par exemple « -001- » sur un incident) en gardant la date, la cellule et le titre. `contexteNommage` renvoie `nmrIncident`.
- **Écran** : aperçu `…-FOR-0602I01-…` ; l'étiquette « Pièce n° » ne reste que pour les demandes sans incident.
- **Vérifié** : 302 tests ; `tsc`, eslint et build Docker ; Playwright (incident 06.02.I01 donne `20261013_MR_DL26_SITCEN-FOR-0602I01-…`).

## 2026-10-01 (suite 8) — MELMIL : comptes rendus PARTAGÉS par jour et par ETIM, en direct (`db46d4b`, `2026-10-01.5`, ✅ en ligne à 11:33 — `/api/sante` vérifié)

- **Demande** : PSYREP et CIMICREP communs à tous les incidents d'un même jour qui ont la même ETIM, chaque autre ETIM ayant les siens ; modifiables à plusieurs en temps réel. Avis DESIGNER n°21.
- **Décisions de l'utilisateur** : un seul compte rendu par type, jour et ETIM ; conversion automatique des anciens quand il n'y a pas d'ambiguïté.
- **Modèle** :
  - `CompteRendu` reçoit `jour` (D+) et `etim`, avec `incident = ""` pour un compte rendu partagé ;
  - `convertirAnciensComptesRendus()`, appelé par `normaliserAtelier` (pur, idempotent) : un compte rendu d'un incident placé sur un jour, à une seule ETIM et sans compte rendu du jour déjà existant, devient partagé ;
  - `sansOrphelins` garde les comptes rendus partagés.
- **Gestes** : `crPartage`, `incidentsDuCr`, `creerCompteRenduPartage` (unique, rejouable ; GDH à l'heure du premier incident ; CIMICREP n° de message = codes couverts) ; journal « de ETIM x à D+y ».
- **Écran** :
  - rubrique « Comptes rendus du jour » placée sous « ETIM concernées », en tableau ETIM × type (Ouvrir / + Créer / Importer, « Commun avec … ») ;
  - « Anciens comptes rendus de cet incident » pour ce qui n'a pas été converti ;
  - **`CaseTexte` enregistre après 1 s sans frappe**, en plus de l'enregistrement en quittant la case.
- **Vérifié** :
  - 301 tests, dont 12 nouveaux ; `tsc`, eslint et build Docker ;
  - **Playwright avec deux navigateurs séparés** : le compte rendu créé par A apparaît chez B sans recharger, et la frappe de A, faite sans quitter la case, s'affiche chez B.
- ⚠ **En ligne**, la conversion des anciens comptes rendus se fera à la première écriture de l'atelier après la mise en ligne. Le nom de fichier `.docx` d'un compte rendu partagé est `PSYREP_ETIM-7_D+27.docx`.

## 2026-10-01 (suite 7) — MELMIL : un PDF accepté mais jamais enregistré, même pour le déposant (`app-melmil` `f42ceb1` `2026-10-01.4`, `pleiade-platform` `b946897`, ✅ en ligne : plateforme à 11:11, MELMIL à 11:14)

- ✅ **Cause CONFIRMÉE** par le message reçu par l'utilisateur : « Dépôt impossible : EACCES: permission denied, open '/data/medias/…' ».
- Après la mise en ligne, la sonde renvoie **`medias: "ok"`**, **sans redéploiement manuel** : la promotion de MELMIL, arrivée après la plateforme, est passée par `deployZone`, donc par `preparerVolumes`.
- ⚠ **À retenir** : toute app qui écrit dans un volume « ./… » sous un utilisateur restreint avait le même défaut. La presse (`./data/media`) est couverte au prochain redéploiement de ses instances.

- **Constat** : avec `2026-10-01.3`, un PDF renommé puis déposé n'apparaît **ni chez le déposant ni ailleurs**. Le problème est donc en amont du rattachement : c'est l'**écriture du fichier sur le disque** qui échoue.
- **Hypothèse principale, non vérifiable d'ici** : le volume `./data/medias:/data/medias` est un **montage de dossier du serveur**, qui masque `/data/medias` préparé dans l'image. Si le moteur de conteneurs crée lui-même ce dossier au premier démarrage, il appartient à l'utilisateur du serveur, et `nextjs` (le conteneur MELMIL, `USER nextjs`) ne peut pas y écrire (`EACCES`). La route répond alors 500 « Dépôt impossible ». `addInstance` ne crée que `data/`, jamais ses sous-dossiers.
- **Fait** :
  - `pleiade-platform` : **`preparerVolumes()`** crée les dossiers des volumes « ./… » et les passe en **0777** avant `up -d`, dans `deployInstance` et dans `deployZone` ;
  - `app-melmil` : **`/api/sante`** renvoie aussi `medias: "ok"` ou `"ecriture impossible (CODE)"`, lisible sans compte, sans rien écrire.
- **Vérifié en local** : sonde à `medias: "ok"` ; 289 tests ; build Docker ; plateforme `tsc` et 24 tests sur 25, avec le même échec Windows préexistant.
- **À faire après le push** : lire `https://melmil.delattre-26.pleiade.internal/api/sante`. Si on y lit `ecriture impossible`, l'hypothèse est confirmée : **« Déployer » l'instance melmil** (elle passe par `preparerVolumes`), puis relire la sonde.

## 2026-10-01 (suite 6) — MELMIL : nommage `AAAAMMJJ_MR_DL26_SITCEN-GYC|FOR-NNN-Titre` (`4ca8bdf`, `2026-10-01.3`, ✅ en ligne à 10:53 — `/api/sante` vérifié)

- **Décisions de l'utilisateur** (questions posées avant de coder) : GYC est le code court de la cellule, avec **GYC = GREY CELL** et **FOR = FORAD** ; **NNN se compte par incident** ; la date est **celle de l'incident**, modifiable ; le titre est saisi, proposé d'après celui de l'incident. Avis DESIGNER n°20.
- **`nommage.ts`** :
  - `CODE_CELLULE` ; `MOTIF` = nouvelle règle, `ANCIEN` = règle du 30/09, seulement relue pour en tirer le titre ;
  - `numeroDepuisNom`, `prochainNumeroPiece` (après le plus grand, jamais sous le nombre de fichiers), `dateDepuisJour` et `jourDepuisDate` ;
  - `contexteNommage` (date de l'incident, sinon échéance de la demande, sinon aujourd'hui ; numéro suivant ; titre de l'incident ou du produit), `lotDeFichiers`, `rangDansLot` ;
  - `nomDeFichier({…, numero})`, `nomExport(nom, cellule, {date, numero})`.
- **Écran** : la fenêtre de nommage a un champ **Date**, la cellule affichée « nom (code) », « Pièce n°NNN — titre » et l'aperçu en direct. L'export renomme les noms libres ou anciens.
- **Serveur** : `PUT /api/medias` n'accepte plus que la nouvelle règle ; le message d'erreur la cite.
- **Vérifié** : 289 tests, dont 11 sur le nommage ; `tsc`, eslint et build Docker ; Playwright (D+34 donne 20261013, puis 003 et 004 à la suite de 2 fichiers déjà présents).
- ⚠ Les fichiers déjà déposés gardent leur nom stocké. Ils sont renommés au **téléchargement**.

## 2026-10-01 (suite 5) — MELMIL : un fichier d'incident visible du seul poste qui l'a déposé (`d1c0f89`, `2026-10-01.2`, ✅ en ligne à 10:34 — `/api/sante` vérifié, `/api/medias/orphelins` répond 401 sans compte)

- **Constat de l'utilisateur** : un PDF importé sur **08.01.I01** n'est pas visible depuis un autre compte, même dans Planification → Incidents.
- **Cause**, l'architecture et non les droits : la route `PUT /api/medias` écrivait seulement le fichier sur le disque. C'était au **poste** de l'ajouter à l'atelier partagé (`ajouterMedia` + `PUT /api/atelier`). Si cet enregistrement échoue :
  - en cas de coupure, l'état local garde le fichier, qui reste visible sur ce seul poste ;
  - en cas de refus ou de conflits répétés, l'écran recharge l'état et le fichier disparaît.
  - Le fichier reste sur le disque, mais n'est **rattaché à rien**.
  - Reproduit à l'identique en local en bloquant le `PUT /api/atelier` du poste.
- **Correctif** :
  - le dépôt envoie sa **destination** (`incident`, `demande`, `fourniPour`) ;
  - **le serveur rattache lui-même** le fichier (`lib/serveur/rattacher.ts`, relecture et rejeu en cas de conflit, 6 essais) ; le geste du poste n'est plus qu'un écho, ignoré s'il est déjà rattaché ;
  - la **fiche disque** garde l'incident, le déposant et la date ;
  - si le serveur n'a pas pu rattacher, le poste le **dit** ;
  - **Réglages → « Fichiers non rattachés »** (`GET` et `POST /api/medias/orphelins`) liste les fichiers du disque rattachés à rien et permet de les rattacher. Rien n'est effacé automatiquement.
- **Récupération du PDF de 08.01.I01** : après la mise en ligne, il apparaîtra dans « Fichiers non rattachés ». Il n'aura **ni incident ni déposant connus**, car il a été écrit avant ce correctif : il faudra choisir 08.01.I01 à la main puis cliquer « Rattacher ».
- **Vérifié en local** :
  - poste bloqué, le fichier arrive quand même dans l'atelier sur le bon incident ;
  - un fichier orphelin est listé (avec son déposant), puis rattaché ;
  - un orphelin ancien, de la veille, est aussi retrouvé ;
  - 281 tests, `tsc`, eslint et build Docker OK.

## 2026-10-01 (suite 4) — Messagerie : écrire à un collègue sans passer par un avatar (`app-messagerie` `412dbae`, poussé sur `main` + `prod`)

- **Question** : un animateur (gc04) peut-il discuter avec un autre compte (gc05) sans choisir d'avatar ? Il écrit bien en son nom par défaut, mais **l'annuaire des participants ne listait que les avatars d'eho**. Les comptes Keycloak n'y figurent pas : pas de privé possible, et pas moyen de cocher un collègue dans un groupe. Le serveur, lui, l'acceptait.
- **Autorisation de l'utilisateur** : « je t'autorise à corriger cela directement sur le serveur ».
- **Fait** :
  - table **`comptes_zone`** (`CompteZone`, créée par `db push` au démarrage) et `lib/comptes.ts` ;
  - chaque compte **réel** connecté est noté, au plus une écriture toutes les 10 min, jamais un avatar endossé ni le compte de développement ;
  - `/api/bff/personas` renvoie **les comptes ET les avatars** pour la composition, chacun avec sa `nature` ; jamais de comptes dans le sélecteur « au nom de » ;
  - `ensureMember` et le titre du privé prennent le nom du compte ;
  - à l'écran, la mention « Compte de la zone » ou « @x · avatar », et l'aide « les comptes apparaissent après leur première connexion ».
- ⚠ **Ma copie locale de `main` était en retard sur `prod`** (le bridage « au nom de » par camp, `18b6648`, n'y était pas). Je suis reparti de `origin/prod`. Le correctif « Se déconnecter ferme aussi la session Keycloak » (`b322f54`, local) **n'est toujours pas en ligne** : il n'a pas été inclus, faute d'accord explicite.
- ⚠ **Piège du Dockerfile** : `npm test` y tourne **avant** `prisma generate`. Un import de `db.ts` dans `auth.ts` cassait donc l'image (« Cannot find module @/generated/prisma/client »). Le correctif est un import **différé** de `comptes.ts`. Toujours construire l'image avant de pousser.
- **Vérifié** :
  - `tsc` ; 6 tests sur 6 ; build Docker OK ;
  - sur une base jetable (`messagerie_essai`, supprimée ensuite) : la table est créée ; « gc05 » est noté, trouvé par « gc0 » et ajouté comme membre sous son nom ; le compte de développement est ignoré.
- **Droits GitHub** : le push sur `app-messagerie` est **accepté**.
- **Mise en ligne** : `delattre-26` n'est pas une zone `prod`. Il faut **« Déployer » l'instance `messagerie`** dans PLÉIADE une fois le CI terminé, ce qui tire la nouvelle image depuis `f020b4e`.

## 2026-10-01 (suite 3) — MELMIL : demande de produit SANS incident (FORAD) et cellule demandeuse (`533e548`, `2026-10-01.1`, ✅ en ligne à 09:12 — `/api/sante` vérifié)

- **Demande** : la FORAD ne crée pas d'incident. Il faut un bouton dans l'onglet « Demandes de produit », et chaque demande doit dire GREY CELL ou FORAD. Fait avec DESIGNER (avis n°19).
- **Modèle** :
  - `DemandeProduit.incident` peut être `""` (demande directe) ;
  - nouveau champ de formulaire **`cellule`** (genre `segment`, `CELLULES_DEMANDE` FORAD / GREYCELL), **obligatoire** ;
  - `MediaIncident.fourniPour` : fichier de base joint à une demande directe ; `fichiersDeLaDemande()`.
- **Gestes** :
  - `creerDemande("")` crée une demande directe ;
  - `ajouterMedia` accepte une demande directe, pour une livraison (`demande`) ou un fichier de base (`fourniPour`) ;
  - `sansOrphelinsProduits` garde les demandes directes et leurs fichiers ;
  - `supprimerDemande` emporte les fichiers d'une demande directe ;
  - `demandesModifieesSansDroit` : retirer une demande directe prise en charge reste réservé à Prod (corrige un trou : le test sur l'incident aurait laissé passer).
- **Nommage** : `celluleProposee` prend d'abord la cellule déclarée de la demande.
- **Écran** (`produits.tsx`) :
  - bouton « + Nouvelle demande sans incident » ;
  - cellule pré-choisie (Équipe, sinon event) ;
  - « Aucun — demande directe » ;
  - « Joindre des fichiers » ;
  - colonne et filtre Cellule.
- **Vérifié** :
  - 281 tests, dont 9 nouveaux, et une ancienne attente mise à jour (la cellule est désormais obligatoire) ; `tsc`, eslint et build Docker OK ;
  - Playwright sur le MELMIL local (données fictives) : formulaire, envoi (DP-03 « sans incident », FORAD), bouton « Joindre », liste, téléphone, aucune erreur.
- ⚠ Les demandes déjà en ligne n'ont pas de cellule déclarée : la file montre celle de la fiche Équipe du demandeur. Les compléter si besoin, en ouvrant la demande.

## 2026-10-01 (suite 2) — Le logo de chaque titre de presse sur le portail (`app-press` `8c7f400`, `pleiade-platform` `139098a`, ✅ en ligne le 2026-10-01 à 08:47 — les 4 titres de DE LATTRE servent leur logo : Today Mercure et TV4 en SVG, Hexagone et TF1 Info par redirection vers le fichier de la maquette)

- **Demande** : récupérer le logo des médias (site ou thème) et l'afficher sur `delattre-26.pleiade.internal/presse`.
- **app-press** : `lib/logo.ts` (`logoDuSite`) et la route **publique** `GET /api/public/logo`.
  - **Ordre de choix**, le même que les en-têtes des maquettes :
    1. le logo téléversé (« Identité ») ;
    2. le fichier de la maquette (`/skins/hexagone|omerta|otan|tf1-…`) ;
    3. le logo **dessiné en CSS**, redessiné en SVG carré avec les mêmes lettres et les couleurs du thème : TV4 (« TV » sur orange, « 4 » cerclé), Today Mercure (T blanc ★ or M rouge sur noir), BC1 (lettres marine, chiffre rouge, cadre rouge) ;
    4. un monogramme.
  - Une image renvoie une redirection 302 vers le fichier ; un dessin renvoie un SVG sans script (CSP fermée). Cache de 5 min.
  - Tests : 3 nouveaux (noms injectés, couleurs douteuses), 8 sur 8 ; build OK.
- **pleiade-platform** : champ de catalogue **`logoPath`** (`presse.yml` : `/api/public/logo`). `logoOuIcone()` dans `portail.ts` sert la page d'accueil (carte d'instance) et la page de choix.
  - En cas d'erreur, l'image retombe sur `/api/icone/…` via `data-repli` : une instance muette ou ancienne, sans la route, ne montre jamais d'image cassée.
- **Vérifié** avec Playwright : rendu de la page avec les SVG générés (TV4, TM, BC1, monogramme), le PNG Hexagone et un site absent (repli) ; tout est affiché, rien de cassé.
- ⚠ **Mise en ligne** : `delattre-26` n'est **pas** une zone `prod`, donc la promotion ne met pas à jour ses instances de presse. Après le push d'app-press, il faut **« Déployer »** chaque instance de presse de DE LATTRE, ou la zone limitée à la presse. Depuis `f020b4e`, cela tire la nouvelle image. Tant que ce n'est pas fait, la carte garde l'icone habituelle.

## 2026-10-01 (suite) — Une instance neuve naît à jour : démarrer TIRE l'image (`pleiade-platform` `f020b4e`, ✅ en ligne le 2026-10-01 à 08:21 — `/api/version` renvoie `f020b4e`)

- **Constat de l'utilisateur** : la nouvelle instance de presse `tv4-international` (DE LATTRE) n'a pas les « maquettes existantes » dans Réglages → Maquette et thème. Il pensait le problème réglé.
- **Cause**, déjà décrite le 2026-09-21 mais **jamais corrigée** : `deployInstance` (« démarrer », appelé après la création) faisait `up -d` sur l'image `presse:latest` déjà présente sur le serveur. Le CI pousse bien `latest` au registre, mais rien ne le retirait pour une instance neuve. La promotion ne vise que les zones `prod`, et `delattre-26` n'en est pas une.
- **Correctif** : `pull` (délai de 5 min, `dockerCompose` reçoit un délai) puis `up -d`. Si le pull échoue, l'instance démarre quand même sur l'image locale et la sortie le signale.
- **Pour l'instance déjà créée** : après la mise en ligne, la **redémarrer** (« Déployer » sur l'instance) suffit, puisqu'elle tirera la dernière image. « Déployer » la zone pour l'app presse le faisait déjà.
- `tsc` OK ; tests 24 sur 25, avec le même échec Windows préexistant.

## 2026-10-01 — Portail de zone : sur la page « Presse », toute la carte ouvre le site (`pleiade-platform` `4995efc`, ✅ en ligne le 2026-10-01 à 08:15 — la page `/presse` sert 8 cartes cliquables, 0 bouton « Ouvrir »)

- **Demande** : sur `delattre-26.pleiade.internal/presse`, supprimer le bouton « Ouvrir », faire ouvrir le site par un clic sur la carte et garder « Espace de rédaction ». DESIGNER a été consulté (avis n°18).
- **Fait** dans `src/portail.ts`, `pageChoix` (la page de choix de tout type d'app à plusieurs instances, pas seulement la presse) :
  - le titre devient un **lien étiré** sur toute la carte (`::after`) ;
  - le bouton de rédaction passe au-dessus (`z-index`), et le survoler n'anime pas la carte (`:has(.titre-liens:hover)`) ;
  - ajouts : chevron « › », focus visible sur la carte, réduction des animations respectée.
- **Vérifié** avec Playwright sur une page rendue avec des données fictives : clic au centre ou dans un coin, le site ; clic sur le bouton, l'espace de rédaction ; aucun « Ouvrir » restant ; pas de débordement au téléphone.
- ⚠ **Tests de la plateforme** : 24 sur 25. Le test « un volume relatif devient un chemin absolu d'hôte » échoue **aussi sur `main` non modifié** : c'est un problème de chemin Windows, préexistant.
- ⚠ Sous Windows, `npm test` échoue à cause du préfixe `REGISTRY_HOST=…` (syntaxe Unix) : lancer `REGISTRY_HOST=registry.cecpc.internal npx tsx --test scripts/test-*.mts` depuis bash.
- Rappel : `pleiade-platform` se déploie **dès le push sur `main`**.

## 2026-09-30 (suite 9) — app-admin : Kit IA, un modèle de prompt à copier-coller (`b66c8dd`, `fd7cd89`, `1b6cdda`, ✅ en ligne le 2026-09-30 à 18:43 : les deux instances ont redémarré — 404 de 18:42:51 à 18:43:12 — puis sont revenues en 401)

- ⭐ **Correction de l'utilisateur, intégrée dans `fd7cd89`** : « le prompt doit être court, le KIT IA contient déjà du contexte ; il doit dire à l'IA de consulter les pièces jointes ». La première version (8 sections, environ 170 lignes, ci-dessous) est **remplacée**.
  - Le prompt tient maintenant en **environ 30 lignes** : lire D'ABORD les pièces jointes, puis Excel · SCÉNARIO · TEMPS (pré-rempli, heure de Paris) · RYTHME · AVATARS / apps · PRESSE (règle absolue) · trame à valider.
  - La **rédaction de chaque média** passe dans **`2_MODE_EMPLOI.md`**, section de chaque site de presse, avec la règle du journaliste ; la règle 6 est complétée.
  - **Règle retenue** : un prompt de kit **renvoie** au contexte des pièces jointes, il ne le recopie pas.
- ⭐ **Deuxième correction de l'utilisateur, intégrée dans le commit « recruté parmi les avatars sans biographie »** : un journaliste manquant n'est plus « à créer ». On le **recrute parmi les avatars SKOLKAN sans fiche bio**.
  - Nouveau fichier du kit : **`6_AVATARS_SANS_BIO.md`**, tiré de **tous** les avatars de l'EHO et non du périmètre de la cartographie ; les membres d'une rédaction en sont exclus.
  - L'onglet demandé à l'IA devient **`JOURNALISTES_A_AJOUTER`** (username, media, fonction, biographie_proposee) ; le prompt, le mode d'emploi (règle 6, section de chaque site) et le guide sont alignés.
  - 18 tests et le build OK.
  - ⚠ La taille du fichier dépend du nombre d'avatars sans bio : environ 70 caractères par avatar, donc au pire environ 270 Ko pour 3 900.
- *Première version (`b66c8dd`), remplacée :*

- **Demande** : ajouter au « Kit IA » un `.txt` que l'utilisateur copie dans son IA et adapte. Il doit contenir :
  - la création d'un **fichier Excel** ;
  - le choix des avatars d'après les pièces jointes ;
  - la **règle absolue de la presse** : un journaliste **du média**, sinon un nouveau journaliste, jamais celui d'un autre titre ;
  - le **temps** : début et fin, date et heure ;
  - le **rythme** des posts et des articles ;
  - le **scénario, le thème et le contexte**.
- **Livré** : `5_MODELE_DE_PROMPT.txt` dans le zip (`txtModelePrompt`, `lib/kit-ia.ts`), en UTF-8 avec BOM et fins de ligne CRLF, pour le Bloc-notes.
  - **Structure** : un mode d'emploi, puis le texte à coller entre « ✂ DÉBUT » et « ✂ FIN », avec des champs `[À COMPLÉTER]`, en 8 sections : scénario · temps · rythme · avatars · presse · apps · livrable · méthode avec liste de vérification.
  - **Pré-rempli** avec les dates du scénario (heure de Paris), les apps et la **rédaction actuelle de chaque site de presse**.
  - **La rédaction est demandée au site** : `checkAccounts` sur tous les avatars, **par paquets de 150**, car 500 identifiants dépassent les 16 Ko d'en-têtes de Node. Si le site est injoignable, le modèle écrit « rédaction non lue ».
  - **Journaliste manquant** : l'IA le décrit dans un onglet `JOURNALISTES_A_CREER` (username, nom affiché, média, pays, langue, camp, biographie). **Le traitant le crée dans l'EHO et dans la rédaction du média AVANT l'import**, sinon l'import signale un persona introuvable.
- **Vérifié** : 17 tests (dont le nouveau : heure de Paris, rythme, rédaction citée, média sans journaliste), `tsc` et `next build` OK ; aperçu généré avec des données fictives.
- ⚠ Non éprouvé contre un vrai site de presse en local : le repli « rédaction non lue » couvre l'échec.

## 2026-09-30 (suite 8) — MELMIL : aligner la planification et la planche sur les exports JEMM réels (`50255e7`, `2026-09-30.7`, ✅ en ligne à 18:12 — `/api/sante` vérifié)

- **Demande** : la saisie JEMM de DE LATTRE 26 est terminée (exports 07 ILI et 08 HN, 62 incidents). La planche JEMM **et** la planification doivent être « à 100 % identiques » aux fichiers, sans un incident de plus. Les manques (effets attendus…) sont pris dans les diapos. Plan validé par l'utilisateur avant le code. Données : `DELATTRE\MEMOIRE.md` § « JEMM RÉEL ».
- **Planification** : `lib/atelier/aligner.ts` (`alignerSurJemm`) et l'écran `components/atelier/aligner-jemm.tsx` (Réglages → « Aligner l'atelier sur JEMM »). On voit d'abord un bilan, puis on clique sur « Appliquer » ; l'alignement est **recalculé au moment d'appliquer**, sur l'atelier du moment.
  - **Renuméroter plutôt que recréer** : médias, demandes, comptes rendus, ETIM et traitants restent attachés par identifiant.
  - **Appariement** :
    - events : même code et même nom, puis même nom, puis même code ;
    - storylines et incidents : ressemblance du titre **ou** de la description (seuil 0,5), à égalité le même jour puis le même numéro ;
    - par numéro, seulement si les textes se ressemblent un peu (≥ 0,3) ;
    - en dessous de 0,5, l'appariement est « douteux » et signalé dans le bilan.
  - **Remplacé par JEMM** : code, nom / sujet, description, période ou D+ et heure, objectif principal (`PrimaryTrainingObjective`, désormais lu par `jemm.ts`), moyen, émetteur, destinataires, résultat attendu.
  - **Gardé** : effets attendus, QUI / OÙ, EXCON, objectifs secondaires, groupes, **cellule de l'event** (elle nomme les pièces jointes), ETIM, statut.
  - **Compléments** : fichier `{"type":"melmil-complements"}` ; il ne remplit que le vide.
  - **Absent de JEMM** : supprimé, sauf un incident qui porte des pièces jointes. Celui-ci est gardé et listé, tant que la case « les supprimer aussi » n'est pas cochée.
- **Planche** : `remplacerParExports` dans `fusion.ts`, menu **Plus → « Remplacer par des exports JEMM… »**. Un import ordinaire ne touche qu'à ses propres events, donc l'ancien 06 serait resté. Ici les réglages sont gardés et les déplacements annulés.
- ⚠ **Leçon, trouvée par l'essai** : apparier **au numéro** est faux dès que JEMM découpe un fait en occurrences datées ou réordonne les numéros. Le premier essai rattachait un média au mauvais incident (l'ancien I02 « Carte Mercure » tombait sur le nouvel I02 « Pylône HS D+35 »). Il faut apparier sur le **texte**, puis sur la date.
- **Vérifié** : `scripts/essai-aligner.mts`, sur un atelier « comme sur le serveur » (les 2 JEMM fictifs du 23/09 versés, 46 incidents) aligné sur les 2 exports réels.
  - **Résultat** : 07 ILI et 08 HN ; 8 storylines ; **62 incidents** identiques champ à champ aux injects ; aucun sans D+.
  - **Ce qui a survécu** : le média, ses ETIM, les effets attendus saisis à la main ; le vide est rempli depuis les diapos ; la 07.03 reste vide.
  - **Rejouer** l'alignement ne change plus rien ; une pièce jointe hors JEMM est gardée, ou supprimée si la case est cochée ; la planche est une copie exacte (aucun 06).
  - **Bilan de l'essai** : 23 incidents renumérotés, 15 mis à jour, 24 créés, 8 supprimés, 1 douteux (08.04.I01 « FRAGO… » devient « Création d'un couloir humanitaire »).
  - 273 tests, `tsc`, eslint et build Docker OK.

## 2026-09-30 (suite 7) — eho : les « autres comptes » pour l'incarnation (`c0a3ea2`, `2026-09-30.2`, ✅ en ligne à 17:09 — `/api/sante` vérifié, nouvelle route en 401 sans compte)

- **Premier constat** : gc05 ne pouvait choisir aucun compte, parce que son groupe n'était coché dans aucun « Camps ». L'utilisateur l'a réglé.
- **Deuxième constat** : même avec les camps réglés, les animateurs n'ont accès qu'à ≈ 500 des 3 900 comptes d'eho. Seuls les avatars d'un groupe visible et coché sont incarnables ; les autres sont dans les 229 groupes archivés le 28/09, ou dans aucun groupe.
- **Règle retenue**, avec l'accord de l'utilisateur (« je te laisse voir ce qu'il y a de mieux ») :
  - un groupe d'avatars avec des camps cochés est **réservé** ;
  - tous les autres avatars forment les **« autres comptes »**, un ensemble calculé ;
  - y ont droit **d'office** les camps d'au moins un groupe réservé, et **en plus** ceux cochés dans le nouvel encart « Autres comptes » (écran Groupes, en tête de page, avec le nombre d'avatars et la liste des camps).
- **Technique** :
  - table `camps_comptes_libres` (créée par `db push` au démarrage) ;
  - `comptesLibres()` et `avatarsImpersonables()` dans `lib/impersonation.ts` ;
  - route `GET`/`PUT /api/camps/comptes-libres` ;
  - `CampsModal` rendue générique : les camps attribués d'office y sont cochés et grisés.
  - **Aucun changement** dans le social ni dans la messagerie : eho leur renvoie simplement la liste d'identifiants.
- **Vérifié** :
  - sur une copie jetable de la base locale (`eho_essai_camps`, 453 avatars), 5 scénarios OK : un camp voit ses avatars réservés et les autres comptes, jamais ceux réservés à un autre camp ; un groupe sans camp ne voit rien tant qu'il n'est pas ajouté à la main, puis exactement les autres comptes ;
  - 112 tests, `tsc` et build Docker OK.
- ⚠ **Garde Prisma** : `db push --accept-data-loss` est refusé aux IA sans consentement explicite de l'utilisateur. Ne pas contourner.

## 2026-09-30 (suite 6) — MELMIL : export PPT, plus de doublon rouge de l'effet dans les incidents (`a0af1d8`, `2026-09-30.6`, ✅ en ligne à 15:02)

- Constat de l'utilisateur : le texte rouge de chaque incident (son `resultatAttendu`) répétait l'encadré « Effets attendus » de la storyline.
- Analyse de l'export réel, **corrigée à 15:10** : sur 36 textes rouges, **22 sont des copies** de l'encadré. Les **14 autres** appartiennent à des storylines dont l'encadré « Effets attendus » est **vide** : ils sont le seul effet affiché, donc conservés. Le premier comptage (« 36 sur 36 ») était faux : en Python, une chaîne vide est toujours « contenue » dans une autre.
- Vérifié en passant `effetPropre()` sur les textes réels de l'export `(2)` : 22 sur 36 filtrés.
- L'export de 15:03, encore avec doublons, a la même taille à l'octet près que celui de 14:55 : il a été produit par l'**ancien code resté dans le navigateur**. Il faut recharger la page après un déploiement.
- `effetPropre()` (dans `modele.ts`) n'affiche plus l'effet d'un incident quand il répète celui de la storyline (comparaison sans casse, espaces ni puces, dans un sens comme dans l'autre). Un effet **propre à l'incident** (par exemple des hypothèses H1/H2) reste affiché. On gagne de la place : plus d'incidents par diapositive.
- 272 tests OK.

## 2026-09-30 (suite 5) — MELMIL : export PPT en A4 paysage, pagination mesurée (`2b74c23`, `2026-09-30.5`, ✅ en ligne à 14:54)

- Constat de l'utilisateur sur le serveur : avec les vraies descriptions (plusieurs paragraphes), le tableau des incidents **débordait** de la diapositive. Il faut respecter le format A4.
- Diapositives en **A4 paysage** (29,7 × 21 cm, mise en page propre `A4_PAYSAGE`). Toutes les positions sont dérivées de la largeur et de la hauteur.
- La pagination se fait selon la **hauteur mesurée** de chaque ligne : `GABARIT_A4` (colonnes, taille 8 pt, 4,75 pouces de lignes) est partagé entre `modele.ts` (mesure) et `ppt.ts` (dessin). La storyline continue sur (1/n), (2/n)…
- Un incident trop long pour une page entière est raccourci, avec la mention « […] (suite dans MELMIL) ».
- Vérifications :
  - rendu PowerPoint COM : aucun tableau ne descend sous la légende (bas maxi 474 pt pour une limite de 536 pt) ;
  - 271 tests OK, build Docker OK.

## 2026-09-30 (suite 4) — MELMIL : export PowerPoint au format du PPT de montage (`4ef3232`, `2026-09-30.4`, ✅ en ligne à 14:30)

- Le bouton « Exporter en PPT » (en-tête de l'atelier) produit, au format de `20260909 - GREY CELL_MAIN v4.pptx` (DE LATTRE 26) :
  - la synthèse ;
  - la chronologie D+ ;
  - le récapitulatif des changements depuis une date ;
  - une fiche par storyline, continuée sur plusieurs diapositives si besoin.
- Les nouveautés et modifications sont marquées en rouge.
- `pptxgenjs` (MIT) ; `src/lib/export-ppt/` (modèle pur testé + dessin). Avis DESIGNER n°17.
- ⚠ **Piège** : un morceau de texte vide rend le `.pptx` « endommagé » pour PowerPoint. Valider dans PowerPoint (rendu COM), pas seulement avec python-pptx.

## 2026-09-30 (suite 3) — MELMIL : onglet Incidents, storylines repliées (`1242213`, `2026-09-30.3`, ✅ en ligne à 14:03)

- Repliées à l'arrivée, avec un en-tête qui résume : incidents, cellule, période D+, statuts accordés, médias, demandes en cours. Un intertitre par event, « Tout déplier / replier », et chacun retrouve ce qu'il avait déplié (`localStorage`).
- Dépliées d'office : la storyline d'un incident ouvert depuis la planche, ou celle choisie dans le filtre. Avis DESIGNER n°16.

## 2026-09-30 (suite 2) — Portraits cassés sur le réseau social (Olamao…) : ✅ corrigé en ligne (eho `7f1abe2` = `2026-09-30.1` à 13:41, social `4b3ec9c` à 13:46)

- ⚠ **Le premier correctif d'eho (`c4f249a`) n'a rien changé** : le serveur Next pose **lui-même** des `x-forwarded-*` sur un appel direct, avec le nom du conteneur. Le repli sur `NEXTAUTH_URL`, placé après ces en-têtes, n'était jamais atteint. Le test unitaire ne l'a pas vu, parce qu'il construisait un `Request` sans en-têtes.
- `7f1abe2` fait passer l'adresse annoncée **avant** les en-têtes, et teste le cas réel.
- **Vérifié en ligne** : le profil `OlamaoOfficiel` porte `https://eho-delattre26.delattre-26.pleiade.internal/api/uploads/eb04e5a3….jpg`, et l'image est servie en 200 `image/jpeg`. Les 114 portraits du fil sont publics.
- ⭐ **Leçon** : sous Next, les en-têtes `x-forwarded-*` ne prouvent **pas** qu'on est passé par Traefik. Vérifier un correctif « d'appel interne » sur le serveur, et relever la version pour pouvoir constater la mise en ligne.

### Diagnostic initial

- **Constat en ligne**, `GET /api/social/users/search?q=olamao` (lecture ouverte) : `avatar_url` valait `http://zone-delattre-26-eho-delattre26-app-1:3000/api/uploads/eb04e5a3….jpg`, c'est-à-dire le **nom interne du conteneur eho**. Aucun navigateur ne le joint. Le même fichier est servi en 200 à `https://eho-delattre26.delattre-26.pleiade.internal/api/uploads/…`.
- **Cause** (`eho/src/lib/uploads.ts`, `originePublique`) : le social appelle eho **par le réseau interne**, sans Traefik, donc sans `x-forwarded-*`. eho prenait alors `req.url`, le conteneur. Le social recopie ce portrait dans ses profils à chaque recherche.
- **Correctifs** :
  - `eho` `c4f249a` (branche `portraits-origine`) : repli sur `NEXTAUTH_URL` / `AUTH_URL`, l'adresse publique posée par la plateforme. 3 tests, 111/111.
  - `app-social` `4b3ec9c` (branche `portraits-publics`) : `reparerPortraitsInternes()` au démarrage, puis toutes les 30 min, redemande à eho les profils dont le portrait commence par `EHO_URL`.
- **Ordre de mise en ligne** : eho d'abord (`main` + `prod`), puis le social (`main` + `prod`). La réparation du social n'a d'effet qu'une fois eho corrigé.

## 2026-09-30 (suite) — MELMIL : nommage des pièces jointes (`2da39bd`, `2026-09-30.2`, ✅ en ligne à 10:47, poussé à la demande de l’utilisateur)

- **Règle de l'utilisateur** : `AAAAMMJJ_MR_DL26_SITCEN-CELLULE-Titre.ext`.
  - La date est celle du jour, **heure de Paris** : le 01/10, on passe à `20261001`.
  - `MR_DL26_SITCEN` est fixe ; la CELLULE est `FORAD` ou `GREYCELL`.
  - Dans le titre, les espaces deviennent des « - ».
- **Import** : une fenêtre de nommage où l'on ne tape que le titre, avec le nom final affiché en direct. La cellule vient, dans l'ordre, de :
  1. la demande, pour une livraison Prod ;
  2. la fiche Équipe de l'importeur, en remontant les groupes (un sous-groupe de GREY CELL donne `GREYCELL`) ;
  3. l'event de l'incident ;
  4. sinon, un choix.
- **Export** : un nom conforme sort tel quel ; sinon il est renommé au jour de l'export (`?nom=` sur `GET /api/medias/:id`).
- **Serveur** : un dépôt au nom non conforme est refusé (400).
- `src/lib/produits/nommage.ts`, pur, 13 tests.
- ⚠ Les fichiers déposés **avant** gardent leur ancien nom dans MELMIL, mais **sortent renommés** au téléchargement.

## 2026-09-30 — MELMIL : médias des incidents + demandes de produit complexe à la cellule Prod (✅ en ligne : plateforme `7de590f` à 10:15, MELMIL `4d11796` = `2026-09-30.1` à 10:17)

- **Ajout demandé en cours de route** (`4d11796`) : Prod est averti des demandes, et le demandeur de leur suite. Cela passe par un signal dans le bandeau, sur toutes les pages, une alerte à l'arrivée et « (n) » dans le titre de l'onglet. `/api/demandes/signaux` est relu toutes les 20 s.
- **Vérifié en ligne sans compte** : `/api/sante` renvoie `2026-09-30.1`, et `/api/demandes/signaux` comme `PUT /api/medias` répondent 401 (les routes existent).
- 🔴 **Défaut de plateforme découvert** : cocher sur le bouclier un rôle qui n'existe pas encore dans Keycloak ne faisait **rien**, sans le dire. `setGroupClientRoles` écartait le rôle inconnu. L'utilisateur avait coché « Prod » pour `cecpc` avant toute synchronisation, et cela n'a donc pas été enregistré.
- ✅ **Corrigé et en ligne** (`pleiade-platform` `b85e2e2`, 10:29) :
  - la route du bouclier crée d'abord les rôles manquants ;
  - le démarrage de la plateforme crée ceux de toutes les zones (`creerRolesManquants`) ;
  - dans les deux cas, **création seulement, rien n'est retiré** ;
  - un rôle introuvable renvoie désormais une erreur.
  - Testé contre Keycloak 26 (`scripts/essai-roles.mts`). **Plus besoin de la commande `synchroniser-roles`** pour un rôle ajouté au catalogue.
- ⏳ **Reste pour l'utilisateur** : recocher « Prod » pour `cecpc` sur le bouclier MELMIL (la première coche n'a pas été enregistrée), se reconnecter, puis faire un premier dépôt réel pour vérifier le volume.

- **Besoin** : voir et déposer les fichiers d'un incident. FORAD et GreyCell demandent à « Prod » (l'utilisateur) les produits que les IA en ligne ne savent pas faire.
- **Décisions de l'utilisateur** : rôle « Prod » sur le bouclier, import ouvert à tous les animateurs, 500 Mo par fichier, **pas de fiche Word** (tout dans MELMIL).
- **`app-melmil` `e5fcf86`** (branche `produits-complexes`, version `2026-09-30.1`) :
  - dans l'atelier : `medias[]` et `demandes[]` ;
  - `src/lib/produits/` (modèle, gestes, dates) et le composant `produits.tsx` : rubrique de la fiche incident, fiche de demande, onglet « Demandes de produit » ;
  - `/api/medias` : PUT en flux avec coupure à 500 Mo, GET par tranche, DELETE ;
  - garde « Prod » dans `PUT /api/atelier` ;
  - dossier `/data/medias` créé dans l'image, appartenant à `nextjs`.
- **Vérifié en local** (base `melmil_produits` sur le port 3307, données fictives) : le parcours complet, un 403 sans le rôle, la coupure à 500 Mo, 241 tests, l'image reconstruite.
  - Un **bug a été trouvé et corrigé** : un second dépôt au même id effaçait le fichier du premier.
- **`pleiade-platform` `7de590f`** (branche `melmil-prod`) : catalogue `melmil.yml`, avec le rôle `prod` et le volume `./data/medias:/data/medias`.
- **Ordre de mise en ligne** :
  1. pousser la plateforme (`main` déploie aussitôt) ;
  2. `POST /api/zones/delattre-26/synchroniser-roles` (depuis la console du tableau de bord, sans bouton) ;
  3. cocher « Prod » sur le bouclier MELMIL, pour le groupe de l'utilisateur et `cecpc` ;
  4. pousser MELMIL `main` + `prod` (le compose est régénéré, et le volume monté) ;
  5. vérifier `/api/sante` → `2026-09-30.1`.
- ⚠ Le rôle est lu **à la connexion** : se déconnecter puis se reconnecter après avoir coché.

## 2026-09-29 (suite 2) — pleiade-platform : identifiants sans adresse mail + bouton « Modifier l'identifiant » (`56f0576`, ✅ en ligne)

- **Demande utilisateur, pour la sécurité** : des identifiants simples (`gw01`), sans adresse, ni nom, ni prénom. Il faut conserver Xavier et Thomas, qui administrent la zone.
- **Livré** :
  - création sans adresse ;
  - import et export avec une colonne « Identifiant » ;
  - bouton crayon qui renomme **sans recréer** : le `sub` est gardé, et rien n'est perdu dans les apps ;
  - l'option « retirer adresse, prénom et nom » ;
  - le refus de renommer un compte d'organisateur (connexion « cecpc »).
- **Essais contre Keycloak 26.0** (conteneur jetable sur le port 8181, `scripts/essai-identifiants.mts`) : tout passe. Deux blocages de Keycloak ont été découverts et contournés : l'adresse est obligatoire tant que la zone la prend pour identifiant, et l'identifiant est en lecture seule tant que `editUsernameAllowed` est faux.
- **Mise en ligne** : poussé sur `main` pendant la planification, avec l'accord de l'utilisateur, puis vérifié par `/api/version` (commit `56f0576`).
- ⚠ **Écran non essayé en local** : pas de plateforme complète sur le poste. Premier essai réel à faire par l'utilisateur, sur un seul compte.
- ⏳ Un test unitaire déjà cassé sous Windows (`test-deploiement.mts`, « un volume relatif devient un chemin absolu d'hôte ») échoue aussi sur `main`, sans lien avec ce travail.

## 2026-09-29 (suite) — app-press : revue DESIGNER de 4 maquettes (`48b1072`, ✅ en ligne le 2026-09-29, poussé sur main + prod à la demande de l'utilisateur)

- **Vérifié en ligne** vers 08:35 :
  - `today-mercure` et `hexagone` servent le nouveau CSS (`sk-vide`, `sk-boucle`) ;
  - leurs maquettes sont bien `sk-todaymercure` et `sk-hexagone`, choisies à la main par l'utilisateur ;
  - le nouveau pied de Today Mercure est servi (`tm-age`, `tm-registre`, « Official state news service »).
- ⚠ **Les instances ont été renommées** : `mercure-today` n'existe plus (404 Traefik), elle s'appelle désormais **`today-mercure`**. L'instance `hexagone` est nouvelle.
- ⚠ **Aucun article publié** sur ces deux instances : la une hiérarchisée, les vignettes et les grilles n'apparaîtront qu'avec des articles. Cela explique l'impression d'« ancienne version » chez l'utilisateur, avec en plus le cache du navigateur.
- La maquette ne peut se changer que depuis les réglages, par un directeur connecté : il n'existe **pas de route de service** pour le faire.

- Today Mercure, HEXAGONE, TV4 et Bothnia Channel 1 : une hiérarchisée, vignettes à la marque, rangées complètes, doublons retirés, bandeaux en boucle, contrastes, téléphone. « 18+ » et mention d'enregistrement pour Today Mercure. **Chartes inchangées.** Détail : `DESIGNER\AVIS\2026-09-29_PRESSE_MAQUETTES\AVIS.md`.
- Nouveaux éléments partagés dans `src/skins/` : `Visuel` et `rangees()` (`shared.tsx`), `HorsAccueil` (`client.tsx`), `.sk-vide` et `.sk-boucle` (`skins.css`).
- Banc d'essai local : base `presse_design` sur le MySQL du port 3307 (l'utilisateur `presse` du 3320 n'a pas le droit de créer une base) ; `scripts/essai-skin.mts <cle>` (non versionné) change de maquette.

## 2026-09-29 — app-press : les « maquettes existantes » (TV4, Today Mercure, TF1…) n'ont jamais été mises en ligne

- **Symptôme** : sur la nouvelle instance `mercure-today` (zone DE LATTRE 26), « Réglages du site → Maquette et thème » ne propose pas les maquettes existantes.
- **Constat** :
  - le code est sur `origin/prod` (`1a40aa1`, `5c43ffe`, `aeda6d5`, du 23 au 24/09) ;
  - une image reconstruite à l'identique (`git archive origin/prod | docker build`, `npm test` compris) compile et contient les styles `.sk-tv4` (184 occurrences) ;
  - **le CSS servi par `mercure-today` n'en contient aucun** : le serveur tourne sur une version d'avant le 23/09. La mise en production du 24/09 ne s'est donc jamais faite, sans qu'on puisse dire si le workflow ne s'est pas déclenché ou s'il a échoué après le build.
  - Le dépôt n'a **aucun tag** de mise en production : l'étape de tag du workflow n'a jamais abouti, et ne permet donc pas de dater les déploiements.
- **Correctif** : pousser sur `main` + `prod` l'unique commit en attente, `cea3ac9` (« Update CLAUDE.md », de l'utilisateur, le 24/09), pour relancer `deployer-prod.yml`. Le premier essai a été bloqué par le classificateur. ✅ **Poussé le 2026-09-29 sur demande explicite** (« pousse app-press en prod »).
- ✅ **Vérifié en ligne** : 07:56:55, `sk-tv4` est présent (184 occurrences) dans le CSS servi par `mercure-today`. Les maquettes existantes sont en ligne pour toutes les instances de presse.
- ⭐ **Leçon** : un push sur `prod` d'`app-press` peut ne rien déployer, sans que rien ne le signale. Après chaque mise en production, **contrôler la présence d'un marqueur de la nouvelle version dans ce que sert le site** (ici une classe CSS), et non la seule branche `origin/prod`.
- `gazette.delattre-26` : instance **supprimée par l'utilisateur** (confirmé).

## 2026-09-28 (suite 12) — app-social : 🔴 toute écriture depuis l'écran du réseau social était refusée (403) → ✅ corrigé (`27869bd`, en ligne sur delattre-26 à 17:00:54)

- **Correctif** (autorisé par l'utilisateur, poussé sur main + prod) :
  - `apps/api/src/garde-ecriture.ts` : le garde authentifie lui-même les écritures, puis contrôle le rôle. La règle ne change pas : écrire demande le rôle ANIMATEUR, la lecture reste libre. Testé dans `garde-ecriture.test.ts` : animateur 200, sans rôle 403, sans jeton 401, GET libre.
  - Front : un message d'erreur s'affiche quand une suppression (post ou commentaire) est refusée ; le profil et la page hashtag retirent la carte supprimée.
  - Build API (tsc) et build web (ng) OK.
- **Vérification en ligne** : un `DELETE` anonyme est passé de 403 (ancien garde) à 401 (« Token manquant »), la preuve que l'authentification passe désormais avant le rôle.
- **Précision de l'utilisateur** : on écrit « in the name of » un avatar, mais un animateur doit pouvoir supprimer sans avatar. La route `DELETE /posts/:id` le permettait déjà (`isAdmin`), seul le garde bloquait.

### Diagnostic initial

- **Symptôme** : l'utilisateur, animateur, ne peut pas supprimer le post #114101 (@arn_krauss) sur `social.delattre-26`. La console affiche `DELETE /api/social/posts/114101 403`, et l'écran ne dit rien, car `deletePost()` n'a aucun traitement d'erreur.
- **Cause** (`apps/api/src/index.ts`, commit `9a86b38` du 2026-09-14, Xavier, en prod) :
  - le garde « écrire demande le rôle animateur » est monté sur `/api/social` et lit `req.userRoles` ;
  - or l'authentification ne passe **avant** lui que si `REQUIRE_AUTH=true`. Sinon, chaque route l'applique elle-même, mais **après** le garde ;
  - avec `REQUIRE_AUTH=false`, la valeur par défaut du catalogue, vérifiée sur `delattre-26` via `/api/config`, `userRoles` est donc toujours vide au moment du garde. **Toutes les écritures de l'écran sont refusées**, animateurs compris : publier, supprimer, liker, modifier.
  - L'admin n'est pas touchée : elle passe par `/api/service` avec la clé de zone.
- **Correctif proposé (pas fait, dépôt en lecture seule sans autorisation)** : dans le garde, authentifier d'abord (`authMiddleware`) pour les méthodes d'écriture, puis contrôler le rôle. Côté écran, afficher les erreurs de suppression, et retirer la carte après suppression sur le profil et sur la page hashtag.

## 2026-09-28 (suite 11) — app-admin : supprimer aussi les publications (branche `suppression-publications`, `e827ab5`, ✅ en ligne le 2026-09-28 : les deux instances ont redémarré à 16:36, puis sont revenues en 401)

- **Retour utilisateur** : après la suppression de scénarios, leurs articles et leurs messages restaient sur les apps.
- ⚠ **Les numéros de ces publications sont perdus** : ils disparaissent avec le scénario, journal compris. Ces publications-là ne peuvent donc pas être retirées par l'admin : il faut les enlever à la main dans chaque app.
- **Suppression d'un scénario** :
  - la case « Supprimer aussi les publications déjà parties » est cochée par défaut (`?publications=retirer`) ;
  - si un seul retrait échoue, le scénario n'est **pas** supprimé (502), puisque c'est lui qui garde les numéros.
- **Suppression d'un inject publié** :
  - la poubelle est désormais visible sur un inject publié, avec la même case ;
  - l'inject part avec son fil, car ses réponses n'ont plus de support sur l'app ;
  - rien n'est supprimé si un retrait échoue.
- `retirerPublications()` est commun avec la remise à zéro. `fil()` et `estEnLigne()` sont purs (`src/lib/suppression.ts`) et testés.
- **Vérifié en local contre une fausse app** :
  - la fausse app a reçu les `DELETE /posts/<n>` : pour l'inject seul, pour la racine et sa réponse, et pour le scénario ;
  - avec l'app arrêtée, la suppression répond 502 et le scénario est gardé ;
  - 16 tests et le build sont OK.
- **Piège** : `next build` pendant qu'un `next dev` tourne casse ce dernier (« Jest worker… »). Libérer le port et supprimer `.next` avant de relancer.

## 2026-09-28 (suite 10) — app-admin : les horaires d'un scénario respectés (branche `horaires-lancement`, `9416628`, ✅ en ligne le 2026-09-28 : poussé sur main + prod ; les deux instances ont redémarré, en 404 de 16:22:30 à 16:23:03, puis sont revenues en 401)

- **Retour utilisateur** : tous les items d'un scénario sont publiés d'un coup, sans respecter les horaires.
- **Cause 1** : lancé alors que son début était passé, un scénario partait **sans fenêtre** et gardait l'ancien début. Au premier tick, le temps écoulé était énorme et tout ce qui était échu partait d'un coup : c'est le rattrapage du planificateur.
- **Cause 2** : Pause → Reprendre produisait le même effet, car la durée de la pause comptait comme du temps écoulé.
- **Correctifs** :
  1. La fenêtre de lancement s'ouvre toujours. Quand le début est passé, elle propose « Maintenant (décaler) » par défaut, ou « Rattraper » avec le nombre d'items qui partiront d'un coup.
  2. Le serveur refuse (409) un lancement à début passé sans choix explicite (`now` / `rattraper`).
  3. Nouvelle colonne `paused_at` (ajout, `db push` au démarrage). À la reprise, début et fin sont décalés de la durée de la pause. Le journal indique « décalé de N min ».
- **Vérifié en local contre une fausse app** :
  - les items à 0, 1 et 2 min sont publiés à 14:11:12, 14:12:12 et 14:13:12 ;
  - après une pause de 70 s, le début est décalé de 70 s ;
  - la fenêtre compte juste : 3 items échus pour un début passé de 30 min.
  - `tsc`, 13 tests et le build sont OK.
- ⚠ **Scénarios déjà partis** : les remettre à zéro, puis les relancer avec « Maintenant ».

## 2026-09-28 (suite 9) — app-admin : les liens des anciennes publications de la Gazette (`1775cca`, ✅ en ligne le 2026-09-28 : la route `/api/bff/lien` répond 401 aux anonymes sur les deux instances)

- **Retour utilisateur** : les liens fonctionnent sur le réseau social, pas sur la Gazette.
- **Cause** : les publications de la Gazette avaient été faites AVANT la mise en ligne des liens, donc sans adresse gardée. Le réseau social se reconstituait d'après le numéro du post, la presse non. Les pages d'articles du serveur répondent bien : la route `/article/<slug>` est vérifiée en 200 sur `gazette.delattre-26`.
- **Correctif** : `/api/bff/lien?instance=&post=` redemande l'adresse à l'app au clic (`/api/service/posts/:id`, présent dans la presse en production) et redirige. Le journal et l'arbre passent par cette route quand l'adresse manque. Vérifié en local.

## 2026-09-28 (suite 8) — app-admin : le lien vers chaque publication (`5a9de73`, en ligne)

- **Demande** : en Supervision, rendre « Gazette publication #1 » cliquable, vers l'article ou le post.
- **Principe** : l'app renvoie déjà l'adresse de ce qu'elle publie (presse : `/article/<slug>`, messagerie : `/c/<fil>#m<id>`), mais l'admin la jetait. Le réseau social ne la renvoie pas ; elle se déduit : `/social/post/<id>`.
- **Livré** :
  - `ScenarioItem.remoteUrl` (nouvelle colonne, `db push` au démarrage) et `meta.lien` du journal ;
  - `MessageJournal` rend cliquable, en Supervision, au tableau de bord et dans le journal du scénario, ce qui suit « → » ;
  - « voir ↗ » sur chaque item publié de l'arbre ;
  - `lib/liens.ts` pur et testé (13 tests).
- ⚠ Les publications **antérieures** : le réseau social se reconstitue par le numéro du post, la presse non (pas de faux lien).
- **Vérifié en local** : article publié sur TV4, lien ouvert (« Coupure d'eau dans le secteur — TV4 International »). **En ligne** : redémarrage du conteneur observé, puis retour en 401 sur `admin.delattre-26` et `conduite.exercice`.

## 2026-09-28 (suite 7) — app-admin : « Vérifier » ne crie plus au loup (`78d7141`, en ligne)

- **Retour utilisateur** : « 8 points à corriger », tous du type « persona @x inconnu (sera provisionné depuis eho…) » sur la Gazette et le réseau social.
- **Diagnostic** : ces messages n'étaient **pas bloquants** (le code les classait déjà comme avertissements), mais l'écran les annonçait tous comme « à corriger ». Or :
  - le réseau social crée le compte depuis eho à la première publication ;
  - pour la presse, « inconnu » voulait seulement dire « hors de la rédaction du site », et l'article paraît quand même.
- **Correctif** :
  - pré-vol exact : un avatar absent d'eho est **bloquant**, un avatar présent ne produit plus de message sur le réseau social ; sur un site de presse, seul l'auteur d'un article hors rédaction reçoit un avertissement ;
  - l'écran sépare « à corriger avant de lancer » et « à savoir » ;
  - `lib/verification.ts` est la règle partagée.
- ⚠ **Défaut ancien corrigé** : le motif « cycle de reponses » (sans accent) ne bloquait jamais un cycle.
- **En ligne** : `main` = `prod` = `78d7141`. Le redémarrage du conteneur a été observé environ 100 s après le push, et la route du kit est revenue en 401. ⚠ app-admin n'a **pas de `/api/sante`** : la version servie ne peut pas être lue directement (à ajouter).

## 2026-09-28 (suite 6) — app-admin : le Kit IA et l'import fiabilisé, branche `kit-ia`

- **Demande** : un seul bouton pour les fichiers de préparation par IA ; examiner l'import pour que tout fonctionne entre les sites.
- **Examen de l'import** : titre, rubrique et champs de maquette n'y passaient pas ; une rubrique presse inconnue est créée sur le site ; les réponses entre apps et les articles sans titre n'étaient vus qu'à la publication ; seul le `.xlsx` était accepté.
- **Livré** : `3d396fd` (voir MEMOIRE, section Kit IA). ✅ **En ligne** sur demande. La route du kit répond 401 aux anonymes sur les deux instances : `admin.delattre-26.pleiade.internal` et `conduite.exercice.pleiade.internal`. Les 2 commits de septembre en attente sont partis avec (`5a5fbd1`, `5b6bf9f`).

## 2026-09-28 (suite 5) — MELMIL : la « Cellule » d'un event devient la sélection des groupes, branche `cellule-groupes`

- **Question de l'utilisateur** : à quoi sert « Cellule » ? Réponse : c'est l'héritage du `CoordinatingCell` de JEMM, un texte libre qui n'était plus qu'un affichage, et qui créait des groupes fantômes dans l'Équipe.
- **Décision de l'utilisateur** : fusionner les deux, la sélection des groupes vivant dans « Cellule ».
- **Livré** : `1e2adf8`, `2026-09-28.6`, 220 tests ; vérifié à l'écran ; ✅ en ligne sur demande (`/api/sante` vérifié).

## 2026-09-28 (suite 4) — MELMIL : « Confié à » par groupes, branche `confie-par-groupes`

- **Demande** : pour « confié à », l'event prend un groupe de premier niveau (GREYCELL, FORAD, le troisième), la storyline un sous-groupe de ce groupe, l'incident une personne du sous-groupe, ou tout le sous-groupe si personne n'est coché.
- **Livré** : `a65d6f2`, `2026-09-28.5`, ✅ en ligne sur demande (`/api/sante` vérifié). Essai local sur des données fictives : event 08 → GREYCELL, 08.01 → DEV / PROD ; incident « tout le sous-groupe », puis une personne ; la fiche d'une autre personne du sous-groupe ne voit plus l'incident. 0 erreur, 0 débordement.

## 2026-09-28 (suite 3) — MELMIL : placer les groupes reliés côte à côte, branche `equipe-placement`

- **Demande** : retirer « Aucune personne » ; que les groupes reliés changent de place pour un dessin harmonieux. L'utilisateur voulait que je regarde le serveur : **impossible** (session requise, et ses données sont confidentielles). Le cas a été reproduit sur une structure fictive, et une capture masquée lui a été proposée.
- **Livré** : `04b3a15`, `2026-09-28.4`, ✅ en ligne sur demande (`/api/sante` vérifié). 205 tests. Essai local : FORAD à côté de GREYCELL, HN BOTHNIA du côté d'ILI, pointillés courts.

## 2026-09-28 (suite 2) — MELMIL : Équipe v2, l'organigramme, branche `equipe-organigramme-v2`

- **Remarques utilisateur** (après saisie de ses vraies données, **que je n'ai pas lues à sa demande**) : HOSTNATION ne montrait que des noms de sous-groupes ; DEV / PROD (dans GREYCELL) doit aussi être relié à FORAD ; l'exercice au centre n'aide pas à comprendre.
- **Réponse** (avec DESIGNER, avis n°11) : organigramme à toute profondeur dans le cadre de l'exercice + liens « travaille aussi avec ». `84294f7`, `2026-09-28.3`, ✅ en ligne sur demande (`/api/sante` vérifié). 201 tests. Essai sur une structure fictive du même genre : 0 erreur, 0 débordement (1440, 1024, téléphone).

## 2026-09-28 (suite) — MELMIL : l'onglet Équipe refait (araignée), branche `equipe-organigramme`

- **Demande** : l'onglet Équipe ne servait pas (« mal pensé ») ; on veut créer des groupes (GREY CELL…), y mettre des personnes avec leur grade, rattacher au besoin un compte Pléiade de la zone, et voir l'architecture de l'exercice « comme une araignée ». Avec l'avis de DESIGNER. « On commence comme ça et on peaufine. »
- **Livré** : `f9f72b6`, `2026-09-28.1`, ✅ **en ligne** sur demande (`melmil.delattre-26` `/api/sante` vérifié ; `/api/zone/comptes` renvoie 401 aux anonymes). L'utilisateur fait ses essais sur le serveur. Détail : MEMOIRE § MELMIL atelier.
- **Corrigé en essayant** : les sous-groupes n'étaient que des étiquettes, sans leurs personnes → passage à une araignée à 2 couronnes ; un grand vide en haut → hauteur calculée sur le contenu ; les grades saisis dans le nom → séparés à la relecture.

## 2026-09-28 — eho : ranger les groupes (235 → 6 visibles), branche `groupes-archives`

- **Demande** : 235 groupes sur le modèle DE LATTRE 26, incompréhensible. Les diminuer au maximum **sans rien casser dans les autres applicatifs**.
- **Analyse** : 49 groupes de classement pays × catégorie, doublons des champs `pays` et `label` ; 180 groupes d'autres exercices (ORION 26 phases 2 et 4 : `O2…`, `O4…`, `02…`, `001-tweeter…`) ; seuls ≈ 6 servent à DE LATTRE.
- **Qui consomme les groupes d'eho** (vérifié dans le code) :
  - l'**incarnation** (camps de joueurs ↔ groupes, `lib/impersonation.ts`) ;
  - **app-admin** (groupes de likes et partages, stockés par **id** dans les items) ;
  - **app-press** (la « rédaction » d'un journal, par id) ;
  - **app-messagerie**.

  app-social, cockpit, MELMIL et LEAC ne les lisent pas ; `pleiade-platform` gère ses propres groupes Keycloak. ⇒ **Règle : ne jamais supprimer ni renommer un groupe, seulement le masquer.**
- **Livré** (`8bb7084`, `2026-09-28.1`, ✅ **en ligne le 2026-09-28** : `main` = `prod`, `/api/sante` vérifié ; l'assistant reste à lancer sur le serveur par l'utilisateur) : champ `Group.archive` (masqué dans eho, toujours renvoyé par `/api/groups`), assistant « Ranger les groupes » (admin), archives repliées, pickers filtrés, drapeau transporté par les modèles, `PATCH /api/groups/[id]` restreint aux champs d'un groupe. Avis DESIGNER n°9.
- **Vérifié en local** (base DE LATTRE fusionnée) : 235 → 6 visibles ; 235 groupes et 5 297 appartenances intacts ; `/api/groups` renvoie 235 groupes (229 marqués archivés) ; un joueur reçoit 403 sur l'assistant ; 0 débordement au téléphone ; 108 tests.
- ⚠ **Erreur corrigée en essayant** : l'exercice en cours était deviné au « groupe EXERCICE le plus récent ». Or la fusion recrée tous les groupes à la même date, et ce critère a désigné ORION 26. Désormais, on ne devine que par le nom de la zone, et le choix est obligatoire sinon.
- ⚠ **Point de vigilance, préexistant** : **appliquer un modèle d'EHO recrée les groupes avec de NOUVEAUX identifiants** (`eho-templates.ts`, `tx.group.create`). Les liens par id d'app-admin et d'app-press ne survivent donc pas à l'application d'un modèle. Ranger, lui, ne change aucun id.

## 2026-09-25 (suite 5) — MELMIL : les ETIM d'un incident, dans la planification

- **Demande** : pouvoir choisir les ETIM liées à un incident (« ETIM 27 », « ETIM 9 » pour les régiments ou les brigades) à sa création, et voir leurs noms sur l'incident dans le tableau de planification.
- **Constat préalable** : dans les JEMM fictifs de DE LATTRE 26, 36 incidents sur 46 citent une ETIM comme acteur, mais avec des libellés qui varient (« ETIM 27 », « ETIM 27 BIM ou 9 BIMa »). D'où **une liste par exercice** plutôt qu'une saisie libre.
- **Livré en local** : `app-melmil` `5b4d76a` (branche `etim-incidents`), version `2026-09-25.1`. 178/178 tests, tsc, lint et build OK. Essai à l'écran au téléphone et sur ordinateur : 0 débordement, 0 erreur de page. Détail : MEMOIRE § MELMIL atelier.
- ✅ **En ligne** sur demande : `main` et `prod` = `5b4d76a`, `melmil.delattre-26` `/api/sante` = `2026-09-25.1`.
- ⏳ **Suite demandée** : dès les premiers exports JEMM réels de l'exercice, récupérer les ETIM pour les afficher sur la planche JEMM (voir MEMOIRE).

## 2026-09-25 (suite 4) — eho : l'onglet Groupes montre les membres d'un groupe

- Un clic sur un groupe ouvre une fenêtre : portrait, Prénom Nom, @compte, recherche, « Copier les @ », lien vers la fiche (avis DESIGNER n°6).
- ⚠ **Sécurité** : `/api/groups/[id]/members` passe de `exigerLecture` à `exigerEcriture`. Les joueurs reçoivent 403. La clé de service d'`app-admin` fonctionne toujours. La liste est triée par nom, avec les portraits sur l'origine publique.
- **Testé en local** sur `eho_delattre` (groupe de 396 membres : ouverture en 0,2 s, 0 débordement au téléphone). **En ligne** : `124679a`, `/api/sante` = `2026-09-25.4`, et un anonyme reçoit 401 sur la route.

## 2026-09-25 (suite 3) — eho : fusionner SKOLKAN PERSONA dans la base DE LATTRE (≈ 3 750)

- **Contexte** : Xavier a mis à jour le réseau social de DE LATTRE en important une base, ce qui a remplacé l'eho de la zone par ≈ 3 750 avatars. SKOLKAN PERSONA a disparu de la base. L'utilisateur garde les 3 750 et veut y ajouter SKOLKAN PERSONA 21.09.26. En cas de doublon, la fiche SKOLKAN est gardée, sans casser le lien avec le réseau social. Le résultat devient un nouveau modèle.
- ⭐ **Le lien social ↔ eho** : `app-social` relie chaque compte par `identityId` = **id eho de l'avatar** (`provisionFromEho`), puis recopie les champs d'eho (username compris). L'export Excel d'eho n'a **pas** d'id. Un modèle bâti depuis le classeur aurait donc donné de nouveaux ids et coupé TOUS les comptes → la fusion se fait **dans eho**, sur la base en place.
- **Réalisé** : `eho` `fda2a17`, `2026-09-25.3` — ✅ **en ligne le 2026-09-25 à 10:36** (vérifié sur `eho.exercice`). La fusion elle-même reste à lancer par l'utilisateur, depuis l'écran.
  - Le bouton « **Fusionner dans la base…** » (Modèles d'EHO) montre un aperçu, puis demande la confirmation `FUSION-<code>`.
  - **Doublon** : même @, sinon même email, sinon même nom normalisé (signalé à part).
  - La fiche du modèle est **gardée avec l'id de la base**. Les groupes des deux fiches sont réunis, car ceux de la base portent les camps du social.
  - La planche officielle est reprise et ses ids sont renommés. Une sauvegarde est prise dans la transaction, et le travail des joueurs est remis.
  - Le résultat peut être enregistré comme modèle ; nom proposé : **SKOLKAN FULL PERSONA 25.09.26**.
- ⚠⚠ **Défaut de fond trouvé en testant** : MariaDB plafonne une requête à **65 535 paramètres**. Avec 3 983 avatars × 26 colonnes (≈ 103 000), `createMany` ne partait jamais. La promesse restait pendante, la transaction SERIALIZABLE restait **ouverte avec ses verrous** et le drapeau « application en cours » restait levé jusqu'au redémarrage. Sur le serveur, cela aurait figé eho pour tous.
  - ✅ Corrigé par des écritures **par lots** (1 000 avatars, 5 000 appartenances, 2 000 lectures). Le correctif vaut aussi pour « Appliquer » et « Restaurer ».
- **Vérifié en local**, sur une base `eho_delattre` remplie par l'import du vrai export du serveur (`avatars-eho-2026-09-25.xlsx`, 3 750 avatars, 177 groupes) :

  | Contrôle | Résultat |
  |---|---|
  | Total | 3 983 = 3 750 + 453 − 220 doublons (212 par @, 8 par email, 0 par nom) |
  | Ids de la base | les **3 750 conservés** |
  | @ changés | 8 (accents perdus côté social, ex. `LaVrit_de_lIntrieure` → `LaVerite_de_lInterieure`) |
  | STARTEX | 62 |
  | Planche officielle | 30 cartes, aucune orpheline, 56 liens |
  | Modèle créé | 3 983 avatars · 235 groupes |
  | Durée | 23 s |

  Tests 95/95, `next build` OK.
- **Vue joueur vérifiée** sur la base fusionnée (ordinateur et iPhone) :
  - Mon EHO et EHO GT : 3 921 avatars à classer + 62 STARTEX, 2,5 à 3,3 s ;
  - planche relationnelle OK ;
  - aucune erreur JS, aucun débordement ;
  - **0 donnée officielle** hors STARTEX ; trombinoscope et planche officielle refusés au joueur.
- **Travail des joueurs conservé** à travers une fusion : deux rangements avec notes, dont un sur un doublon, sont intacts.
- ⭐ **Fusion idempotente** : la relancer donne toujours 3 983 avatars (453 doublons, 0 ajout). Un double clic ne fait pas de dégât.
- ⚠ Observé : l'**import Excel** d'eho est lent, ≈ 5 lignes/s, soit ~12 min pour 3 750, car il traite ligne à ligne. Non traité.

## 2026-09-25 (suite 2) — eho : les portraits ne s'affichaient pas sur le serveur

- **Signalement** : pas de photos sur « Avatars » ni sur la « Planche officielle », seulement des initiales.
- **Cause** : les avatars portent des adresses ABSOLUES vers le poste de préparation, `http://localhost:3001/api/uploads/…`. C'est le cas des 118 portraits du modèle intégré, et de même pour un classeur exporté d'un poste local. Sur le serveur, le navigateur cherchait l'image sur **son propre ordinateur**. Les fichiers sont pourtant bien sur le serveur : `/api/uploads/<nom>` répond 200 sur `eho.exercice`.
- **Correctif** (`eho` `2b7a563`, `2026-09-25.2` — ✅ **en ligne à 09:19**) : `lib/portraits.ts` introduit deux fonctions.
  - `cheminPortrait` (écrans d'eho) : rend le chemin relatif `/api/uploads/<nom>`, quel que soit l'hôte écrit.
  - `portraitPourOrigine` (`/api/users`, consommé par mastorion) : rend l'adresse complète sur l'origine publique de l'instance.
  - L'import et l'export Excel et l'application d'un modèle écrivent désormais une adresse portable.
- **Vérifié** : en local, avec des adresses réécrites vers un autre hôte, les portraits s'affichent (Avatars 10/10, planche officielle 32/32, EHO joueurs 16/18, dont 2 hors écran en chargement paresseux) et `/api/users` rend l'origine de l'instance. Tests 86/86, `next build` OK.
- ⭐ **Leçon** : une adresse de fichier servi par l'app ne doit **jamais** dépendre de l'hôte où elle a été écrite. On stocke le chemin, et l'on compose l'adresse complète à la sortie seulement.

## 2026-09-25 (suite) — eho : écran Avatars en rails (avis DESIGNER n°5), en local

- Branche `avatars-rail` (`a3bf90a`, `2026-09-25.1`) — ✅ **en ligne le 2026-09-25 à 08:59** (poussée sur `main` et `prod`, avance rapide).
- `GET /api/avatars/planche?section=…` rend désormais les cartes d'un bloc **complètes** : toute la ligne `User` moins `rawPassword`, plus `groups`, `aBio` et `complet`. C'est toujours réservé à l'animation (`exigerEcriture`). La recherche reste légère.
- Écran :
  - rail borné qui défile ;
  - préchargement de la tranche suivante ;
  - « Revenir au début » ;
  - fiche instantanée ;
  - correctif de la fiche bloquée sur « Chargement… ».
- Vérifié : tests 80/80, lint et `next build` OK. Le serveur de dev tourne de nouveau sur `eho_charge` (:3001).

## 2026-09-25 — MELMIL v2, eho v2 et LEAC profils : EN LIGNE

- L'utilisateur avait poussé depuis GitHub Desktop, mais seulement **`main`** (MELMIL, eho) et la branche **`profils`** (LEAC). **Aucune `prod`** n'avait bougé, et rien n'était donc déployé. Dans GitHub Desktop, il ne voyait « rien à pousser » sur `prod`.
- ⭐ **Leçon** : pour lui, « pousser » ne suffit pas. Il faut **fusionner `main` dans `prod`** (et, pour LEAC, `profils` dans `main`). Contrôler chaque fois `origin/prod` et `/api/sante`, jamais le seul `main`.
- En mode « Edit automatically », j'ai poussé moi-même, en avance rapide contrôlée (`merge-base --is-ancestor`) :

  | Dépôt | Poussé | Commits |
  |---|---|---|
  | app-melmil | `main → prod` | `4ef018b..03e3363` |
  | eho | `main → prod` | `aa791a4..f67be82` |
  | app-leac | `profils → main` et `prod` | `f13d167..2b8d539` |

- ✅ **Vérifié sur le serveur** à 08:08 :
  - MELMIL `2026-09-24.5` ;
  - eho `2026-09-24.2` ;
  - LEAC `2026-09-25.1`, base remise à niveau et administrateurs conservés (`amorce: true`) ;
  - `/api/avatars/planche` d'eho → 401 pour un anonyme.
- Copies locales remises sur `main` à jour dans les trois dépôts.

## 2026-09-24 (suite 9) — eho : charge à 3 500 avatars + refonte DESIGNER, en local

- **Demande** : appliquer l'avis n°4 en local et faire charger les avatars par groupe. Dans DE LATTRE, avec ≈ 3 500 avatars, la plupart des pages buguaient.
- **Branche locale `refonte-v2`** d'eho (partie de `main` `aa791a4`), version `2026-09-24.2`, trois commits :
  - `7263464` : la charge ;
  - `f3bece5` : les recommandations R1 à R11 ;
  - `f67be82` : la garde de `/api/avatars/planche`, réservée à l'animation.
  - ⏸ **Rien n'est poussé.**
- **Banc local** : base **`eho_charge`**, copie de `eho` enrichie de 3 050 avatars `charge_XXXX`, sur le même conteneur `eho-eho-db-1`. Le serveur de dev sur **:3001 tourne sur cette copie** (`DATABASE_URL=…/eho_charge`). La base `eho` habituelle n'est pas touchée. Pour revenir à la normale : relancer `npm run dev -- -p 3001` sans la variable.
- **Mesures** (CPU ×4, réseau type VPN) :

  | Écran | Avant | Après |
  |---|---|---|
  | Trombinoscope | 9,1 s · 8,4 Mo · saisie 3,4 s | 2,2 s · 44 Ko · saisie 0,37 s |
  | Mon EHO | gel 2,0 s | gel 0,2 s |
  | Planche relationnelle | tâches longues 291 ms par frappe | 50 ms |

- **Sécurité vérifiée** :
  - aucune donnée officielle ne part vers un joueur, ni dans la liste, ni dans la nouvelle fiche ;
  - `/api/avatars/planche` renvoie 403 à un joueur et 401 à un anonyme.
- **Non fait** : le test d'intégration `test-modeles-integration.mjs`, qui applique des modèles et aurait écrasé le banc. Le `next build` non plus, pour ne pas perturber le serveur de dev. **À faire avant la mise en production.**

## 2026-09-24 (suite 8) — eho : avis DESIGNER n°4 (propositions, aucun code)

- Analyse d'eho (`aa791a4`) demandée par l'utilisateur, **sans modification du dépôt**. Avis : `DESIGNER\AVIS\2026-09-24_EHO\AVIS.md`.
- ⚠ **Défaut à signaler en priorité** : sur un poste en **mode sombre**, eho devient illisible (texte blanc sur cartes blanches). La cause est dans `src/app/globals.css`, où le bloc `prefers-color-scheme: dark` ne redéfinit que `--background` et `--foreground`. Correctif de quelques minutes, pas encore fait.
- 🟡 **MELMIL v2** : `main` local de `app-melmil` = `03e3363`, en avance d'un commit ; l'utilisateur le pousse lui-même depuis le travail (main + prod).

## 2026-09-24 (suite 7) — MELMIL v2 : refonte responsive en local (non poussée)

- **app-melmil**, branche locale `refonte-v2` (`03e3363`, version `2026-09-24.5`), partie de `prod` `4ef018b`. Avis DESIGNER n°3 appliqué : système visuel v2, bandeau à espace toujours visible, menu « Plus ▾ », **vue Liste par jour** (nouveau composant `src/components/planche-liste.tsx`, style `liste` ajouté à `style-planche.tsx`, par défaut < 768 px), onglets et incidents adaptés au téléphone, fiches plein écran, menus en feuille basse.
- **Données** : aucune modification du modèle ni de l'API — affichage seul. Le choix Liste / Clair / Classique reste par poste (`localStorage`).
- **Vérifié** : `tsc`, eslint, 166/166 tests, 0 débordement sur 6 appareils. ⏸ **Pas de push** avant validation par l'utilisateur sur http://localhost:3800.

## 2026-09-24 (suite 6) — eho : amélioration des liens en ligne · LEAC : refonte locale

- **eho** : l'utilisateur a demandé de pousser l'amélioration en attendant son diagnostic. `aa791a4` (version `2026-09-24.1`) a été poussé sur `main` et `prod` par moi. **En ligne sur `eho.exercice` à 15:39.**
- **LEAC** : avis DESIGNER n°2 appliqué, validé, puis ✅ **en production** à 15:56 (`6701831`, `2026-09-24.1`). Aucune donnée perdue : l'affichage seul est touché. Détail dans `LEAC\JOURNAL.md` et `LEAC\MEMOIRE.md` §7.

## 2026-09-24 (suite 5) — eho : liens invisibles sur la planche relationnelle (signalement, non reproduit)

- **Symptôme** : pendant une démonstration en vue joueur et en vue admin, les cartes étaient bien placées, mais **aucun trait de lien** n'apparaissait.
- **Non reproduit en local**, avec la même version que le serveur (`eho.exercice` → `2026-09-22.1`, `prod` = `main` = `ee15253`). Les liens s'affichent :
  - en **dev** comme en **build de production** (essai dans un worktree, `next start` sur 3001) ;
  - dans la vue joueur `/graphe`, dans l'admin qui observe `joueur_test` (6/6 liens) et sur la planche officielle (56/56).
  - ⇒ Ni le code ni la construction : **les données du serveur ou les conditions d'affichage** sont en cause.
- **Pistes écartées** :
  - `.lecture-seule .accroche { display:none }` : les liens restent dessinés, parce que React Flow est en `ConnectionMode.Loose` ;
  - l'hypothèse du trait trop fin au zoom 0,23 : Chrome dessine déjà un trait d'environ 1 px (écart de pixels mesuré : 1 960 contre 2 019).
- **Fait quand même** (commit `1037433`, ✅ **poussé et en ligne le 2026-09-24 à 15:39**, version `2026-09-24.1`) : `vector-effect="non-scaling-stroke"` et 2 px au repos. Le trait et la zone de préhension gardent leur taille à l'écran, quel que soit le zoom. C'est une amélioration, **pas le correctif démontré**.
- **Informations demandées à l'utilisateur** : quelle planche, sur quelle instance ; les traits reviennent-ils en zoomant ; quel navigateur ; y a-t-il des erreurs dans la console F12. Piste restante : des identifiants d'accroche (`depuis`/`vers`) incompatibles avec le type du nœud, auquel cas React Flow abandonne le lien (erreur 008).

## 2026-09-24 (suite 4) — MELMIL : « Planification » et étape « Exercice en cours »

- **Demande de l'utilisateur** : « Création d'exercice » décrivait mal l'outil. On s'en sert pour planifier la MELMIL **avant ET pendant** l'exercice, jusqu'à la fin, pour créer et modifier des incidents. Il fallait aussi retirer « brouillon de la cellule » : ce n'est pas un brouillon, c'est l'outil de **conception de la partie ILI**. Enfin, le mot « Préparation » doit devenir « en cours » une fois l'exercice lancé.
- **Fait** (commit `4ef018b`, version `2026-09-24.4`) ✅ **poussé et en ligne sur `melmil.delattre-26` à 15:15** :
  - le bouton du bandeau devient **« Planification »** ;
  - une **4ᵉ étape « Exercice »** s'ajoute après le GT3 (`NumeroGt` 1 à 4, relue par `normaliserAtelier`) ;
  - l'étiquette passe de **« Préparation »** à **« Exercice en cours »**, avec un point, dès l'étape 4 ;
  - à l'étape 4, on arrive sur l'onglet Incidents ;
  - le menu devient « Changer d'étape » (Passer / Revenir, Déclarer l'exercice en cours) ;
  - le journal écrit « déclare l'exercice en cours ».
  - 166 tests passent.

## 2026-09-24 (suite 3) — MELMIL : refonte visuelle (avis DESIGNER n°1), en local

- Avis du nouvel agent **DESIGNER** sur MELMIL (`DESIGNER\AVIS\2026-09-24_MELMIL\AVIS.md`). L'utilisateur a demandé d'appliquer les 8 recommandations en localhost pour les voir.
- **Branche `refonte-design`** d'app-melmil, commit `aeaa796`. ✅ **Validée par l'utilisateur** (« j'aime beaucoup les modifs »), fusionnée par avance rapide et **poussée sur `main` et `prod`** (`ea43edc`, version `2026-09-24.3`). **En ligne sur `melmil.delattre-26` à 15:04.** (Cette fois, mon push est passé.)
- **Contenu** : sélecteur d'espace et bande de couleur (préparation ambre, JEMM bleu) ; en-tête d'une ligne ; onglets groupés et navigables au clavier ; échelle de texte ; planche « Clair » (par défaut) ou « Classique » au choix, mémorisé par poste ; incidents en tableau avec fiche en panneau latéral ; focus conforme WAI-ARIA. La palette des storylines ne contient plus de rouge (Bordeaux → Cuivre, Rouge → Olive), et les couleurs choisies dans les réglages restent prioritaires.
- ⚠ Un sélecteur d'e2e a changé : les onglets sont désormais `role="tab"` dans un `role="tablist"` (avec la même `aria-label`), et les incidents sont des `tr` de `table.table-incidents`, plus des `details.carte-ui`.

## 2026-09-24 (suite 2) — Pushes de l'utilisateur (GitHub Desktop)

- ✅ **pleiade-platform `2ffa941`** (œil « Masquée aux joueurs » réservé à la Presse) : en ligne à 13:46 (`/api/version` commit `2ffa941`). ⭐ L'orchestrateur répond sur `https://pleiade.pleiade.internal/api/version` (aussi `orchestrateur.`, `admin.`…).
- ✅ **app-press `aeda6d5`** poussé sur `main` + `prod` (item_fields, chapô, eho). Déploiement **non vérifiable de l'extérieur** (press n'expose pas sa version en public).
- ⏳ En attente de Xavier (403) : **app-admin** (2 commits, **rebasés le 24/09 sur son `84009f4`** « type social publiable », patchs régénérés dans `PATCHS\2026-09-24_admin-champs-maquette\`), **app-cockpit** et **app-messagerie** (déconnexion, `PATCHS\2026-09-21_deconnexion\`).

## 2026-09-24 (suite) — MELMIL : comptes rendus PSYREP / CIMICREP

- Demande : les deux modèles de `DELATTRE 26\00_Boites à outils` dans l'atelier, à l'identique, complétables, exportables à l'identique ; accès en bas de chaque incident (GT3), cumulables ; + (message en cours de route) **import** d'un modèle rempli dans Word. Marquages : aucun sur les modèles (le CIMICREP a une case « Classification » à remplir).
- Livré : `app-melmil` `6f77eb6` (`2026-09-24.2`) — détail dans MEMOIRE (§ atelier). ✅ **Poussé par l'utilisateur via GitHub Desktop** (mon push bloqué en mode auto) → **en ligne sur `melmil.delattre-26` à 13:14** ; les deux modèles `.docx` y sont servis (200). ⭐ Nouvelle façon de faire retenue : je prépare les branches, l'utilisateur pousse dans GitHub Desktop, je vérifie `/api/sante`.
- Piège évité : « Location CP » du CIMICREP est dans un **tableau imbriqué** dans la cellule → le générateur lit `tc.iter(p)` et non les seuls enfants directs.

## 2026-09-24 — MELMIL atelier : versement JEMM expliqué + grille EXCON cliquable

- L'utilisateur trouvait « Création d'exercice » vide : la fonction existait (Réglages ▸ calendrier ▸ « Verser un export JEMM »), elle était simplement cachée derrière le calendrier. Marche à suivre donnée. L'atelier vide s'affichait sans l'alerte « pas de base de données » → **la base de `melmil.delattre-26` existe**, pas de recréation à faire.
- Demande : le tableau « EXCON COORDINATION REQUIRED » du PPT, cliquable dans les storylines (blanc → jaune → vert → blanc). Livré en local, commit `d55688d` (`2026-09-24.1`) ; détail dans MEMOIRE. Couleurs relevées dans le PPT (python-pptx) : jaune `FFFF00`, vert `92D050`. **Non poussé : en attente de l'accord de l'utilisateur.** Accord donné ; mon `git push` a été **bloqué par le classificateur de permissions** → commande laissée à l'utilisateur. Ensuite `origin/main` contenait `d55688d`, mais **`origin/prod` restait sur `cc6d5b2`** (donc pas encore déployé).
- **Point des 12 dépôts (fetch)** : **rien à tirer**, tous les `main` locaux contiennent déjà les travaux de Xavier (derniers en date : press 20/09, trois thèmes Le Monde/Figaro/20 Minutes ; social 19/09 ; messagerie 17/09). En attente de push : 1 commit « Se déconnecter ferme aussi la session Keycloak » sur **admin, cockpit, messagerie, press** (403, patchs `PATCHS\2026-09-21_deconnexion`) + la branche `maquettes-existantes` d'app-press (patchs `2026-09-23_…`, elle contient bien le `main` de Xavier). ⚠ **app-messagerie : `origin/prod` a un commit de Xavier (`18b6648`, « brider au nom de au camp du joueur ») absent de `origin/main`** — à lui de le reporter sur main. Branches locales `atelier-preparation`, `catalogue-melmil`, `libelle-masquee-aux-joueurs` : déjà fusionnées. `app-press\CLAUDE.md` modifié = bloc réécrit par `next dev`, sans importance.
- **Push app-press FAIT** (Xavier a ouvert les droits) : `main` e8e22ee..99b649f (déconnexion Keycloak) + nouvelle branche distante **`maquettes-existantes`** (pas sur prod → pas en ligne, à fusionner). Passé une fois hors mode auto ; le push suivant (`app-melmil main:prod`) a de nouveau été refusé dès le retour du mode auto → **grille EXCON toujours pas en ligne**.
- ✅ **Mode « Edit automatically » (hors auto) → push passés** : `app-melmil main:prod` (cc6d5b2..d55688d) → **`melmil.delattre-26` sert `2026-09-24.1` depuis 08:44** ; **`app-press` `maquettes-existantes` → `main` ET `prod`** (avance rapide, 5c43ffe) sur demande « tout à jour et sur le serveur » → les 10 maquettes partent en production. ⚠ press n'expose pas sa version (`/api/sante` = `{ok, app}` seulement) : vérification à faire dans une instance press (Réglages ▸ Maquette ▸ onglet « Maquettes existantes »). **Prévenir Xavier** : son `main` d'app-press contient désormais nos 3 commits.
- Orchestrateur : le bouton œil « Masquée aux joueurs » **n'apparaît plus que sur les instances `presse`** (demande utilisateur : les autres ne se cachent jamais). Exception : une instance d'une autre app déjà masquée garde le bouton, pour pouvoir la réafficher. Commit `2ffa941` sur `pleiade-platform`, **local, en attente de push**.
- **Vérif admin → press sur les 10 maquettes** (press local + clé de service d'essai + eho simulé, requêtes = exactement celles de `app-admin/src/lib/mastorion.ts publish`) : pour chaque habillage, article texte brut, article avec photo (multipart) et réaction de lecteur → **201, accueil et page 200, habillage `sk-<clé>` appliqué, corps en paragraphes, réaction affichée, photo servie**. 10/10. Données d'essai supprimées, site remis sur `tv4`.
  - ⚠ Limites du contrat admin : l'admin n'envoie que `title`, `content`, `category`, `functional_id`, média → **pas de chapô, pas de champs de maquette** (lieu TV4/BC1…, « L'essentiel » TF1, référence/signataire ONU, émission ZubrRadio, bouton EFS : tous retombent sur leur valeur par défaut), **ni urgent/à la une/direct** (le fil en direct n'est pas alimentable depuis l'admin).
  - 🐛 `autoStandfirst`/`plainText` (lib/sanitize.ts) collent les paragraphes (« jour.Les Etats ») et, sur un article court, le chapô **répète tout le corps**. Visible sur chaque article publié par l'admin. Correctif simple proposé, non appliqué.
  - ⚠ press rend une **500** si eho est injoignable (`fetch` non rattrapé dans `lib/eho.ts`) : une publication de scénario échoue au lieu de signer « Rédaction ».
- ✅ **Corrigé + champs de maquette dans l'admin** (demande utilisateur) :
  - **press `aeda6d5`** (local, à pousser) : `plainText` espace les blocs ; chapô par défaut vide sous 220 car. ; eho injoignable → `null` ; `/api/service/health` annonce **`item_fields`** (chapô, urgent, à la une + champs de la maquette active, groupés) ; `/api/service/publish` accepte **`fields`** (standfirst/urgent/pinned, le reste → `skinFields`).
  - **admin `69728f5`** (local, **403 → patch** `PATCHS\2026-09-24_admin-champs-maquette\`, avec 0001 déconnexion) : `DescribedApp.itemFields`, colonne `scenario_items.fields` (JSON, db push additif), formulaire dynamique sous la rubrique, envoi `fields` au publish. Aucune maquette connue côté admin (contrat générique, style `needs_title`).
  - Essai bout en bout local (admin 3400 + press 3500 + eho simulé 3599) : formulaire ONU → item → publication → page ONU avec référence, signataire, fonction ; chapô non dupliqué ; TF1 `fields` → chapô, urgent, `skinFields`. Données d'essai et base `admin_essai` supprimées.

## 2026-09-23 (suite 9) — MELMIL : l'atelier de préparation (création d'exercice GT1 → GT3)

- Concept validé avec l'utilisateur (deux planches jamais mélangées ; GT = étapes ; tout le monde modifie, trace visible ; écarts plutôt qu'export ; annuaire d'équipe).
- Développé sur `app-melmil` branche `atelier-preparation`, commit `cc6d5b2`, version `2026-09-23.3` : modèle pur + gestes + planche dérivée + écarts + versement JEMM ; table `atelier` + migration additive ; `/api/atelier` ; canal SSE par document ; écran `/preparation` et bascule dans le bandeau.
- Vérifié : 139 tests, essai deux navigateurs 16/16, montée de base simulée, image de production lancée (healthy, 401 sans session).
- En route : un ancien `next dev` d'`app-melmil` (session précédente, sans base) occupait le port 3800 → arrêté ; piège CRLF de l'essai d'image local noté en MEMOIRE.
- ✅ **Déployé** avec l'accord explicite de l'utilisateur : `main` et `prod` d'`app-melmil` avancés en avance rapide `aa141a6..cc6d5b2`. `melmil.delattre-26` sert `2026-09-23.3` à 17:41 (≈ 2 min, dont 40 s de Bad Gateway/404 pendant le redémarrage) ; `/api/atelier` = 401 sans session, `/preparation` → `/connexion`.
- ⚠ L'utilisateur indique que l'instance `melmil.delattre-26` **n'a pas été recréée** depuis le constat « sans base » du 23/09 : si l'écran affiche « Cette instance n'a pas de base de données », la supprimer/recréer dans Pléiade reste nécessaire (puis recocher les groupes d'animation sur le bouclier).

## 2026-09-23 (suite 8) — Orchestrateur : « Masquée aux joueurs » en production

- Demande utilisateur : garder la case de visibilité du portail mais la nommer clairement. Comportement vérifié dans le code avant de renommer (seul `getPortalData` filtre ; tableau de bord et découverte voient tout ; adresse joignable ; portail identique pour tous → masque aussi aux animateurs qui passent par lui).
- `public/app.js` : étiquette « Masquée aux joueurs » sur la ligne, infobulle et message réécrits. Commit `839d389`, intégré à `main` en avance rapide et **poussé avec l'accord explicite de l'utilisateur** (déploiement immédiat de l'orchestrateur).
- ✅ Vérifié sur le serveur par la marque de version : `https://pleiade.cecpc.internal/api/version` → `commit 839d389`, construit à 14:03:23Z.
- 💡 Pour vérifier un déploiement de l'orchestrateur : `/api/version` est public ; `/app.js` est derrière la connexion (302).

## 2026-09-23 (suite 7) — Mise sur serveur des maquettes : bloquée, livraison préparée

- L'utilisateur autorise la mise sur le serveur. Deux blocages constatés : `git push` sur `app-press` renvoie toujours **403**, et l'accès SSH au serveur de production est **refusé par la protection de l'environnement Claude** (lecture de production), que je n'ai pas contournée.
- Livraison préparée pour Xavier : `PLEIADE\PATCHS\2026-09-23_maquettes-existantes\` (3 patchs, paquet git, README).
- Voie isolée repérée dans le code (`promoteVersion(version, { zones, appType })`) : publier l'image sous une étiquette dédiée (pas `latest`) et ne la promouvoir que sur une zone de test, sans toucher aux instances `presse` des zones de production.

## 2026-09-23 (suite 6) — `app-press` : onglets de maquettes + vagues 2 et 3 (les 10 sites)

- Demande utilisateur : deux onglets dans « Maquette du site » (génériques / existantes), un seul visible à la fois — fait.
- Habillages ajoutés : Hexagone, TF1 Info, Omerta Média, Nations Unies, OTAN, ZubrRadio.FM, EFS. Commit `5c43ffe` (local, non poussé).
- Vérifié : captures des 7 nouveaux sites (articles avec photo de démonstration et champs de maquette renseignés), 40 pages (une, rubrique, recherche, direct × 10) en 200 sans erreur navigateur, onglets des réglages, `tsc` OK, 5 tests OK.
- Corrigé en route : collision `.wrap` EFS / mention d'exercice ; `h2` EFS qui touchait le titre des réactions.
- Détail : MEMOIRE § « Chantier — Templates MASTAURIGE ».

## 2026-09-23 (suite 5) — `app-press` : vague 1 des maquettes existantes réalisée (local)

- Branche locale `maquettes-existantes`, commit `1a40aa1` (non poussé) : habillages **TV4**, **Today Mercure**, **Bothnia Channel 1** — une, article, rubrique, direct, recherche, page fixe ; réglages (groupe « Maquettes existantes », charte verrouillée, « Retoucher les couleurs », reprise d'identité, aperçu réel en miniature) ; champ « Lieu de la dépêche » (TV4, BC1).
- Vérifié : captures Chrome des 3 chartes comparées au template d'origine (logo TV4 identique) ; parcours Playwright réglages → Retoucher → éditeur ; lieu affiché sur le site ; `tsc` OK, 5 tests OK ; site générique inchangé.
- Constat : sauvegarde d'article impossible en local sans eho (contrôle de signature par camp, préexistant).
- Détail et architecture : MEMOIRE § « Chantier — Templates MASTAURIGE ».

## 2026-09-23 (suite 4) — `app-press` : templates MASTAURIGE en « maquettes existantes » — cadrage

- Lu `app-wordpress` (WordPress officiel + OIDC, hors contrat de zone) et `app-webserver` (fichiers statiques publics + explorateur `/_admin`) pour situer `press` ; rôles des deux apps corrigés dans MEMOIRE.
- Analysé les 10 `_TEMPLATE.html` de `Sites\` 7BB et le système de maquettes d'`app-press` (`theme.ts`, `(site)/layout.tsx`, `SiteHeader`, modèles `Site`/`Article`).
- ⚠ `git push --dry-run` sur `app-press` → **403** (confirmé) ; commit local `99b649f` toujours non remonté.
- Décisions utilisateur consignées dans MEMOIRE § « Chantier — Templates MASTAURIGE » : habillages fidèles par vagues, 10 sites dont EFS, branche locale seulement, charte verrouillée + « Retoucher ». Rien codé.

## 2026-09-23 (suite 3) — Portail de zone : cartes regroupées, pastille « nouveau », case de visibilité

**Point de départ** : l'utilisateur, en découvrant le fonctionnement de la presse (1 instance = 1 titre), objecte que **vingt titres feraient vingt cartes** sur `delattre-26.pleiade.internal`, à côté du social et de MELMIL. Il imaginait d'abord un **kiosque** : une seule instance presse gérant tous les titres.

### Ce que j'ai conseillé, et pourquoi (discussion sans code, à sa demande)
- **Ne pas fusionner les instances de presse.** Le kiosque perdrait les **adresses propres** de chaque titre (crédibilité d'un média fictif pour l'influence), mettrait **vingt titres dans un seul conteneur** (une panne = toute la presse), et exigerait de refondre la presse — **dépôt de Xavier, sans droits d'écriture**. Surtout, les droits par titre y deviendraient un problème : un rôle du bouclier vaut pour l'instance entière.
- **Regrouper dans le portail à la place** : petit, dans la plateforme (où j'écris), et utile à **tous** les types d'apps.
- Sur sa question « peut-on demander de se connecter sur le portail, avec un bouton *invité* ? » : **déconseillé**. (1) Le SSO de royaume existe déjà : connecté à une app, on ne retape pas son mot de passe dans la suivante — **à mesurer avant de construire** ; (2) un « invité » sur le portail serait **décoratif** : c'est chaque app qui décide ce qu'un anonyme peut faire, et la presse le fait déjà ; (3) une connexion devant le kiosque **coûte du réalisme** (un vrai site ne demande pas de s'identifier pour lire) et crée une panne nouvelle ; (4) coût réel : l'orchestrateur n'authentifie que les **opérateurs**, contre un client unique — authentifier les **joueurs de zone** est un chemin d'authentification **par zone** à construire. **Chantier séparé, décidé séparément** ; l'utilisateur a accepté.
- ⭐ **Trois niveaux d'identité dans la presse**, clarifiés pour lui : le **lecteur** (aucun compte) · le **rédacteur** (session Keycloak + rôle du client du titre) · la **signature** (un **avatar eho**, parmi les groupes cochés par le directeur, et parmi ceux qu'eho autorise **selon le camp** — fermé si eho ne répond pas).

### Fait — `pleiade-platform` `4b1ddea`, poussé sur `main` (déploie)
1. **Regroupement** : les instances d'un même type se replient en **une carte** (compte affiché) qui ouvre **`/<type>`**, page de choix listant chaque instance avec **le site** et, si le catalogue déclare un `adminPath`, **son espace d'administration** (la presse déclare `/redaction`). Un type à une seule instance garde sa carte directe.
2. **Pastille « nouveau »** : la page de choix lit, par le **contrat de service que le storybook utilise déjà** (`health` → `supports: retex`, puis `retex?depuis=`), la **dernière parution** de chaque instance — le retex ne rend **que le publié**, à la date de **parution**. Le navigateur retient ce qu'il a vu et allume la pastille quand c'est plus récent ; la carte groupée de l'accueil s'allume si **un** de ses membres est neuf. ⚠ **Par appareil** (les lecteurs n'ont pas de compte). Les **commentaires n'allument rien**. Fenêtre 30 j, cache 60 s, délai 4 s, échec silencieux : une app éteinte ne retarde ni ne casse le portail.
3. **Case « visible sur le portail »** par instance (`portail_visible`, œil / œil barré dans l'interface opérateur, `PATCH /api/zones/:z/instances/:id/portail`). ⚠ **Pas une protection** — le portail est public et l'adresse se devine ; le rôle protège. L'infobulle le dit. La **découverte entre apps** continue de tout voir.
- Le rendu sort d'`index.ts` pour vivre dans **`src/portail.ts` (pur)** et `src/portail-fraicheur.ts` (les appels) : **10 tests Node** (regroupement sans perte, ordre, **échappement d'un libellé hostile**, liens, règle du neuf, commentaires ignorés). Les deux pages **rendues et éprouvées dans un navigateur, 15/15** : carte groupée et compte, pastille qui **s'éteint à l'ouverture** et **reste allumée** pour un autre titre, **autre appareil** qui revoit tout neuf.
- ⚠ Relevé en passant : sur l'hôte d'une zone, **seul le middleware placé avant le garde de session est public** (`portailDeZone` n'exempte que `/img` et `/icones`). La page de choix devait donc vivre dans ce même middleware, sinon elle aurait renvoyé vers la connexion.
- 🐛 Attrapé par la relecture d'un test, pas par le produit : j'assertais `!html.includes("lien-admin")` alors que la **feuille de style embarquée** contient toujours cette chaîne — le test aurait passé à côté du défaut. Corrigé sur le balisage.

## 2026-09-23 (suite 2) — MELMIL v1 : la planche devient PARTAGÉE et vivante

**Demande utilisateur**, après avoir vérifié avec moi que la v0 ne partageait rien : *« je veux que melmil soit interactif avec tous les utilisateurs qui y ont accès… que lorsque quelqu'un apporte une modification la modification s'effectue en live sur les autres ordis »*, **« en respectant la documentation de Pléiade »**.

⚠ **Lecture de la demande, à confirmer** : « tous les joueurs » est compris comme **tous les utilisateurs AYANT ACCÈS**, c'est-à-dire les groupes cochés sur le bouclier. L'interdit du matin **tient** : un entraîné n'entre pas dans MELMIL.

### Ce que « respecter la documentation Pléiade » a voulu dire concrètement
Rien n'a été inventé — chaque pièce copie un modèle existant :
| Besoin | Modèle suivi |
|---|---|
| Base de l'instance | `requires: mariadb` + `DATABASE_URL`, **comme `leac` et `eho`** |
| Client Prisma | `src/lib/serveur/prisma.ts`, **copie de celui de LEAC** (pool sur `globalThis`, message clair si l'URL manque) |
| Temps réel | **SSE**, `GET /api/flux` + bus en mémoire — **exactement le montage d'`app-messagerie`** (`api/flux/route.ts`, `lib/bus.ts`, `useFlux.ts`) : `retry`, battement de cœur, `X-Accel-Buffering: no`, reconnexion à attente croissante |

### Les trois décisions qui portent la v1
1. **Une instance = UNE planche** (`Planche.id = 1`). L'instance est déployée pour un exercice : rien à choisir, rien à nommer, et un seul objet à suivre.
2. ⭐⭐ **La concurrence se tient par un NUMÉRO DE VERSION, pas par un verrou.** Toute écriture dit sur quelle version elle s'appuie ; le serveur n'accepte que si c'est encore la courante (`updateMany where version = …`, donc **atomique en base**). Sinon **409 + l'état frais**, et l'écran **rejoue son geste dessus**.
   ⚠ **C'est pour cela que `modifier` prend une FONCTION et non un état.** Envoyer un état calculé d'avance aurait effacé le travail de l'autre **sans que personne ne le voie** — la perte silencieuse que ce projet refuse partout. L'import JEMM a dû être réécrit pour fusionner **dans** la transformation, pour la même raison.
3. ⭐ **Le flux ne transporte JAMAIS la planche**, seulement son numéro de version. Un écran en retard **relit**. Événement perdu, reconnexion, redémarrage : on retombe juste, parce que la vérité est en base.

### ⚠ Un point où je m'écarte de LEAC, délibérément
LEAC démarre sur `prisma db push --accept-data-loss`, et son propre commentaire dit pourquoi c'est acceptable : *« chaque tablette garde son journal complet, la base du serveur est un point de rassemblement, pas la mémoire du contrôle »*. **MELMIL est l'inverse** — la base est la **seule** mémoire de la planche. MELMIL utilise donc des **migrations versionnées** (`prisma/migrations/`, `migrate deploy`).
⚠ Conséquence technique : `migrate deploy` **n'accepte pas `--url`** (contrairement à `db push`) et exige un fichier de configuration. D'où un **`prisma.config.mjs`** — en JavaScript, l'image n'embarquant ni TypeScript ni `dotenv` ; LEAC, lui, supprime sa configuration TypeScript de l'image.

### Vérifié — le seul contrôle qui prouve un partage : DEUX navigateurs
`e2e_melmil_partage.cjs`, **9/9**, deux contextes indépendants (donc deux `localStorage` distincts), base MariaDB réelle :
- les deux écrans sont **« en direct »** ;
- A importe un export JEMM → ⭐ **B voit les cartes sans rien faire** ;
- B renomme l'exercice → ⭐ **A le voit en direct** ;
- **écritures simultanées** (A clique une carte pendant que B renomme) → les deux convergent, **et aucune carte ne disparaît** ;
- la planche **survit au rechargement** (elle est en base) ;
- **un troisième navigateur, jamais venu, la trouve déjà remplie**.
96 tests unitaires (dont 9 nouveaux sur la relecture d'un état enregistré, désormais partagée entre serveur et navigateur), lint et `tsc` propres.

### Ce que l'écran dit maintenant
Un **voyant permanent** : *en direct* · *enregistrement…* · *hors direct* (le flux est coupé, la planche est relue toutes les 10 s, **les modifications partent quand même**). ⚠ « Vider » et « Restaurer » préviennent désormais que cela vaut **pour tout le monde**.

### L'IMAGE éprouvée, pas seulement le code
⭐ Leçon appliquée ([[LESSON-035]] : *« un build applicatif qui passe ne prouve RIEN pour un déploiement conteneurisé »*) — l'image a été **construite et exécutée** sur une **base neuve** :
- l'entrypoint applique la migration (`1 migration found` → `successfully applied`) ;
- conteneur **`healthy`** ; `/api/sante` rend `2026-09-23.2` ;
- ⭐ `/api/planche` et `/api/flux` rendent **401 sans session** — en `NODE_ENV=production` l'échappatoire de développement n'existe pas, et le cloisonnement tient **aussi sur les routes d'API**, pas seulement sur l'écran ;
- table `planche` conforme (`longtext`, `version`, `majPar`).
Conteneur et base d'essai **supprimés** après contrôle.

⚠ Le client Prisma **généré** n'est pas versionné (`.gitignore`, comme LEAC) : le `Dockerfile` le régénère à la construction.

### 🔴 Un défaut que la bascule aurait créé — réparé AVANT de pousser
L'utilisateur signale qu'il a **déjà créé l'instance** sur `delattre-26`. Deux conséquences, vérifiées dans le code :

1. ⚠⚠ **Cette instance n'a PAS de base.** `createInstance` provisionne la base **à la création**, d'après `tpl.requires` (`zone-manager.ts` ~911) ; elle a donc été créée quand le catalogue disait `requires: []`. **Aucun chemin de réparation n'existe** dans l'orchestrateur : ajouter `requires` au catalogue ne lui en donnera pas. ⇒ **Il faut la supprimer et la recréer.**
2. 🔴 **La bascule aurait orpheliné la planche déjà faite dans le navigateur.** L'état v0 vit dans `localStorage` ; après la mise à jour, l'application lit le serveur — la planche locale **existe toujours**, mais **plus rien ne la montre et aucun bouton ne l'atteint**. C'est exactement la perte silencieuse que ce projet refuse partout, et je m'apprêtais à la créer.
   ⇒ **`components/reprise-locale.tsx`** : l'écran **signale** la planche locale, **dit ce qu'elle contient** (events / storylines / incidents), et propose les trois seules issues — *publier pour tout le monde*, *télécharger d'abord*, *ne plus proposer*. ⚠ Proposé **uniquement quand la planche partagée est encore vide** : publier par-dessus le travail d'une équipe serait pire que le défaut réparé.
   Vérifié en navigateur, **7/7** : signalement avec le compte exact, publication effective **sur le serveur**, bandeau qui disparaît, **un autre poste la voit**, et lui n'a **aucune** proposition puisque la planche n'est plus vide.

### Poussé, et mesuré sur le serveur
1. **`pleiade-platform` `main` `bca926f`** — catalogue avec `requires: mariadb`. ⚠ **En premier**, délibérément. ✅ `/api/version` rend `bca926f` **60 s** après.
2. **`app-melmil` `prod` `aa141a6`** — version `2026-09-23.2`. ✅ **7 étapes sur 7**, promotion et tag compris. `melmil.delattre-26` rend `{"ok":true,"app":"melmil","version":"2026-09-23.2"}`.

⚠⚠ **L'instance sert la nouvelle version, mais elle n'a toujours PAS de base.** Vérifié en lisant `promoteVersion` : elle ne fait que mettre à jour `image_version` et redéployer — **elle n'appelle jamais `createInstanceDb`**, qui n'existe que dans `createInstance`. Une promotion ne rattrape donc pas un `requires` ajouté après coup. ⇒ **la suppression/recréation reste obligatoire**, et l'application le dira franchement à la connexion (« cette instance n'a pas de base de données : la planche ne peut pas être partagée ») au lieu de rendre une page blanche.

### ⏭️ Reste — geste d'OPÉRATEUR
1. ⚠⚠ **SUPPRIMER puis RECRÉER l'instance melmil de `delattre-26`** — sans cela, pas de base, et MELMIL dira « cette instance n'a pas de base de données : la planche ne peut pas être partagée ».
2. **Recocher les groupes d'animation** sur le bouclier de la nouvelle instance.
3. Si une planche a été construite dans un navigateur, l'écran proposera de **la publier** à la première ouverture.
- ⏳ Un rôle de **lecture seule** n'existe pas : qui entre peut modifier (`peutEcrire` est le point unique à changer).
- ⏳ Une planche déjà faite dans un navigateur ne remonte pas toute seule : « Exporter l'état » puis « Restaurer » sur l'instance partagée.
- ⏳ Un rôle de **lecture seule** n'existe pas : qui entre peut modifier (`peutEcrire` est le point unique à changer).
- ⏳ Les planches déjà faites dans un navigateur ne remontent pas toutes seules : « Exporter l'état » puis « Restaurer » sur l'instance partagée.

## 2026-09-23 (suite) — 🔴 « Failed to create client role "admin" : 500 » — une description de 295 caractères

**Signalement utilisateur**, en créant l'instance melmil dans `delattre-26` :

```
Failed to create client role "admin": 500 {"error":"unknown_error",
"error_description":"For more on this error consult the server log."
```

### Cause — mesurée, pas devinée
`KEYCLOAK_ROLE.DESCRIPTION` est un **VARCHAR(255)**. La description que j'avais
écrite pour le rôle de melmil faisait **295 caractères** : l'insertion échoue en
base et Keycloak rend **500 `unknown_error`**, un message qui ne dit rien.
Mesure des 15 rôles du catalogue — **melmil était le seul à dépasser** :

| app | rôle | longueur |
|---|---|---|
| leac | admin | 221 |
| messagerie | animateur | 125 |
| social | animateur | 105 |
| **melmil** | **admin** | **295** ⛔ |
| *(les 11 autres)* | | ≤ 94 |

⚠ **C'est mon défaut**, introduit le matin même en écrivant une description
trop bavarde. Le catalogue avait été validé sur sa **syntaxe** (le « : » non
quoté), jamais sur les **limites du système qui le consomme**.

### Corrigé — deux fois, pour ne pas laisser le piège
1. La description de melmil passe à **195 caractères**, sans rien perdre de
   l'essentiel (« ne cocher QUE des groupes d'animation »).
2. ⭐ `descriptionDeRole()` (`keycloak-manager.ts`) **tronque au-delà de 255
   AVANT l'appel**, et **le dit dans le journal**. Une description est de la
   **documentation** : en perdre la fin est sans gravité, un 500 bloque un
   déploiement. ⚠ Et une troncature silencieuse ferait croire le catalogue
   servi tel qu'il est écrit — d'où l'avertissement.

### Et des tests, sur les DEUX défauts du jour
Nouveau `scripts/test-catalogue.mts` (4 contrôles, verts) : toute description
de rôle **sous 255**, la **troncature** effective, chaque fichier du catalogue
**YAML-lisible** *(le « : » non quoté du matin, qui aurait fait tomber **tout**
le catalogue)*, et tout rôle portant clé et libellé.
⇒ Les deux fautes de la journée sont désormais **impossibles à refaire en
silence**. Commit `b76870a`, poussé sur `main`.

### État après l'échec, et ce qu'il faut faire
- `createClient` s'exécute **avant** `ensureClientRoles` : le client Keycloak
  `melmil-delattre26` **existe** probablement déjà, sans son rôle. L'instance,
  elle, **n'a pas été créée** (l'erreur coupe avant l'écriture du dossier et de
  la ligne en base).
- ⭐ **Rien à nettoyer à la main** : `createClient` gère le 409 (il reprend le
  client existant et récupère son secret). **Refaire simplement la création**
  une fois l'orchestrateur redéployé.

### ⚠ Relevé en passant, sans rapport et NON corrigé
`scripts/test-deploiement.mts` — « un volume relatif devient un chemin absolu
d'hôte » **échoue sur Windows** : `config.hostDataDir` y vaut
`C:\CECPC\pleiade\pleiade-platform\data`, qui ne commence pas par `/`.
Le test est **juste sur le serveur** (Linux) et faux seulement sur ce poste ;
antérieur à mes changements, laissé tel quel.

## 2026-09-23 — MELMIL mis à disposition sur le serveur, derrière le rôle du bouclier

**Demande utilisateur** : *« tu peux pousser l'application sur le serveur »*, avec une consigne explicite — MELMIL ne doit être accessible **qu'aux groupes cochés « admin » sur le bouclier de l'instance**, *« car si les joueurs ont accès à cette application ils peuvent voir le déroulé et le montage de l'exercice pour la partie Influence »*.

### ⚠⚠ Ce que j'ai trouvé avant de pousser — la consigne ne pouvait pas être tenue telle quelle

1. **Le catalogue de MELMIL ne déclarait AUCUN rôle** (`roles: []`, hérité du premier essai « rien n'est partagé, donc rien à protéger »). Sans rôle déclaré, **il n'y a rien à cocher sur le bouclier** : Pléiade ne crée aucun rôle Keycloak, et **tout compte du royaume** — donc tout joueur — entrait dans la planche.
2. **Le portail d'une zone est PUBLIC.** Relevé dans `pleiade-platform/src/index.ts` : le middleware du portail est placé **avant** `requireAuth`, et il affiche `getPortalData(zone)`, un `SELECT` de **toutes** les instances. Aucune authentification, aucun filtrage. ⭐ **Ne pas cocher un groupe ne cache donc pas la carte** — cela retire l'accès à l'app. La carte reste visible et l'adresse devinable. *(Vérifié aussi que la branche `durcissement-acces-et-portail` est déjà fusionnée dans `main` et ne traite pas ce point : elle exige un rôle sur l'**orchestrateur**, pas sur le portail de zone.)*

**Conséquence assumée et dite à l'utilisateur** : la barrière qui protège réellement le montage de l'exercice, c'est **l'application elle-même**, pas la visibilité de la carte.

### Fait
- **`app-melmil`** — `src/lib/zone/habilitation.ts` : `ROLE_ACCES = "admin"`, `peutEntrer(roles)`, comparaison **exacte** (Keycloak distingue la casse). Le sas `(planche)/layout.tsx` pose **deux** questions : qui êtes-vous (Keycloak) puis avez-vous le rôle. Sans lui, la planche **n'est jamais rendue** (composant serveur) et un **refus expliqué** dit où le rôle se donne et qu'il est **lu à la connexion**.
- Les rôles du compte de développement se règlent (`MELMIL_DEV_ROLES`) — ⭐ un chemin de test qui ne sait qu'**ouvrir** ne prouve rien sur la **fermeture**, et c'est la fermeture qui protège l'exercice.
- **`catalog/melmil.yml`** — rôle `admin` (libellé « Animation ») avec une description qui dit en toutes lettres de **ne cocher que les groupes d'animation**.
- ⚠ **Défaut attrapé par la validation, pas par la relecture** : ma description de l'app contenait `ANIMATION : reserve…` — un `:` suivi d'une espace dans un scalaire **non quoté** casse le YAML. `js-yaml` refusait le fichier ; sur le serveur, c'est **tout le catalogue** qui n'aurait plus chargé. Corrigé (guillemets) et **les 10 entrées revalidées une par une**.
- **Poussé** : `app-melmil` `main` puis `prod` (`bbf72f5`, version `2026-09-23.1`) ; `pleiade-platform` `main` (`67ad82b`, fusion de `catalogue-melmil`) — ⚠ `main` **déploie sans sas**.

### Vérifié
- 87 tests (dont 6 sur l'habilitation : porteur, non-porteur, liste vide, casse).
- **Dans un navigateur, les deux côtés** : `MELMIL_DEV_ROLES=` (sans rôle) → page de refus, et le HTML servi **ne contient aucune donnée de planche** ; avec le rôle → la planche s'ouvre.

### Mise en service — mesurée, pas supposée
- **Orchestrateur à jour en 80 s** : `/api/version` rend `67ad82b` (il servait `b79cd5f` du 21/09). Le catalogue est donc sur le serveur.
- **Déploiement de l'app du 06:05, examiné pas à pas** (API GitHub, jeton jamais affiché) : `Construire l'image (tests + compilation)` ✅ · `Pousser au registre interne` ✅ · `Promouvoir` ❌ · tag sauté. ⭐ **L'image `localhost:5000/melmil:latest` et `:bbf72f5` sont donc bien au registre** — l'app EST sur le serveur.
- ⭐⭐ **Le motif exact du refus, lu dans le journal du runner, corrige une hypothèse de la mémoire** :

  ```
  app inconnue : « melmil »
  connues : admin, cockpit, eho, leac, messagerie, presse, social, webserver, wordpress
  ```

  Ce message vient de **`src/promouvoir.ts` lui-même**, pas de `sudo` ni du script `/usr/local/sbin/pleiade-promouvoir` : l'appel **a bien été autorisé** et a atteint le programme Node, qui a refusé parce que **son catalogue embarqué** ignorait melmil. La liste « connues » est `getCatalog()`, pas une liste en dur.
  ⇒ **Il n'y a jamais eu de préalable `sudoers` à faire pour melmil.** Le seul manquant était le catalogue. *(La note du `README`/workflow qui annonce ce préalable est à corriger.)*
  ⚠ La promotion tournait à **06:06:42**, l'orchestrateur n'a été reconstruit qu'à **06:07:08** : c'est une question d'**ordre**, pas de droits.
- **Déploiement relancé** (`workflow_dispatch` sur `prod`, HTTP 204) une fois l'orchestrateur à jour → ✅ **les 7 étapes en succès**, promotion comprise, et la version marquée d'un tag. Sortie de la promotion :

  ```
  melmil → bbf72f5 : 0 zone(s) redeployee(s) sur 4 visitee(s)
  ```

  **4 zones visitées** : la chaîne fonctionne de bout en bout. **0 redéployée** parce qu'**aucune instance melmil n'existe encore** — c'est le comportement attendu, la promotion ne met à jour que l'existant.
- **Corrigé dans la foulée, parce que la doc mentait** : `docs/DEPLOIEMENT.md` et l'en-tête du workflow annonçaient un préalable `sudoers`. La mesure prouve le contraire ; les deux portent désormais le message d'erreur et son explication. Le `README` dit en tête ce qu'est MELMIL du point de vue de la confidentialité (document d'animation, rôle obligatoire, portail de zone public). Commit `a3482f1`.

### ⏭️ Reste — un geste d'OPÉRATEUR, dans Pléiade
1. **Créer l'instance** `melmil` dans la zone voulue (ex. `delattre-26`) : l'app est au catalogue, son image est au registre.
2. Sur le **bouclier de l'instance**, **cocher UNIQUEMENT les groupes d'animation** pour le rôle « Animation » (`admin`). ⚠ Un groupe d'entraînés qu'on coche voit tout le montage.
3. Prévenir les personnes concernées : le rôle est **lu à la connexion** — cocher un groupe ne vaut qu'à la connexion suivante de ses membres.

*(Je n'ai pas de session d'opérateur sur l'orchestrateur et n'en fabrique pas ; SSH au serveur — port 2222 — n'est pas joignable depuis ce poste, seuls les services derrière Traefik le sont.)*
- ⏳ **À décider avec l'utilisateur et Xavier** : faut-il **authentifier et filtrer le portail de zone** ? Cela change le comportement de **toutes** les zones et **toutes** les apps — pas à glisser dans une livraison.

## 2026-09-22 (suite 11) — MELMIL : un chevauchement de phases se RAYE

- **Constat utilisateur, sur un cas réel** : 3A INTER jusqu'au 30/06 et CAX 2 dès le 25/06 — la première phase prenait le dessus et **la seconde disparaissait de la planche**, alors qu'elle était bien saisie. Demande : une zone rayée, automatique, esthétique.
- ⭐ **Revirement assumé d'une décision de ce matin.** La suite 5 disait : « on tranche par l'ordre de la liste ». C'était le mauvais arbitrage — il **cache une information** au lieu de la montrer. Un jour peut appartenir à deux périodes ; la planche doit le dire, et laisser l'animateur juger si c'est voulu ou si c'est une faute de saisie.
- **Mise en œuvre** : `phasesCouvrant` rend **toutes** les phases d'un jour ; les bandes se regroupent sur le **jeu** de phases (« WU TEC + 3A INTER » fait sa bande, « 3A INTER + CAX 2 » la sienne, « CAX 2 » seule reprend après) — on voit où le chevauchement commence **et où il s'arrête**. `fondDePhases` rend un aplat à une couleur, des **rayures à 135°** au-delà.
- **Pourquoi des rayures et pas un mélange** : mélanger deux teintes en donnerait une troisième, qui ne veut rien dire ; en choisir une ment. Les rayures montrent les deux, et se lisent d'un coup d'œil. ⚠ 135° pour les phases, −45° pour la hachure d'un jour gelé : **deux trames distinctes pour deux notions distinctes**.
- L'en-tête nomme les deux (chasse réduite, ombre de texte pour rester lisible sur les rayures), l'infobulle dit « Chevauchement : … ». La colonne reçoit la même trame, en discret.
- **Vérifié** : **81** tests de logique pure, **5** contrôles navigateur sur le cas exact de l'utilisateur (bande `— CONVEX | WU TEC + 3A INTER | 3A INTER + CAX 2 | CAX 2`, fond rayé mesuré, aplat conservé pour une phase seule). Commit `5f9ed76`, poussé sur **`main` seulement**.

## 2026-09-22 (suite 10) — MELMIL : un nom de couleur porte sa teinte

- **Demande utilisateur** : voir la couleur à côté de son nom, en cas de doute.
- **Fait** : chaque `<option>` du menu porte sa teinte en fond — dans la liste déroulée, le nom et la couleur se lisent ensemble.
- ⚠⚠ **Ce fond n'est rendu que par certains navigateurs** (Chromium le fait, d'autres l'ignorent). **L'information ne repose donc pas sur lui** : le `<select>` fermé porte un **liseré de 6 px** de la couleur effective, qui s'affiche partout ; la pastille de gauche la montre aussi, et son infobulle la nomme. Le confort d'un côté, la garantie de l'autre — on ne fait pas dépendre une information d'un rendu optionnel.
- Bénéfice de bord : même en mode « auto », le liseré et la pastille montrent la teinte **réellement appliquée** par la palette, ce que l'écran ne disait pas.
- **Vérifié** : 75 tests de logique pure, **13** contrôles navigateur (12 options colorées ; liseré mesuré à `rgb(0,105,92)` après un choix « Sarcelle »). Commit `8410456`, poussé sur **`main` seulement**.

## 2026-09-22 (suite 9) — MELMIL : storylines repliables par Event, couleurs nommées

- **Demande utilisateur** : une flèche qui ouvre le sous-menu d'un Event (droite → bas), appliquée à tous les events ; et des **noms de couleurs** au lieu de « teinte 1 ».
- ⭐ **`<details>` natif plutôt qu'un état à tenir** : la flèche, l'ouverture au clic, le clavier et l'accessibilité viennent avec, sans une ligne d'état. **Replié par défaut** — c'est le but : les 14 storylines du 7BB occupaient tout le panneau, il ne reste que deux lignes. Chaque groupe s'ouvre indépendamment.
- **Palette nommée** (Bordeaux, Bleu roi, Violet, Vert forêt, Rouge, Sarcelle, Framboise, Indigo, Orange, Brun, Ardoise, Pourpre) : un menu « teinte 1, teinte 2… » oblige à essayer chaque option pour savoir de quoi on parle. `PALETTE_NOMMEE` est la source, `PALETTE` en dérive pour la logique. La pastille de gauche montre toujours la couleur effective.
- **Vérifié** : 75 tests de logique pure, **11** contrôles navigateur (replié par défaut, la flèche pivote, un groupe s'ouvre sans l'autre, plus aucune « teinte N », et choisir « Sarcelle » applique bien `#00695C`). Commit `bec9fd7`, poussé sur **`main` seulement**.

## 2026-09-22 (suite 8) — MELMIL : une phase tient sur UNE ligne

- **Demande utilisateur** : couleur, nom et plage sur la même ligne, champs de date rétrécis, « plage à poser » supprimé — *« quelque chose d'épuré et fluide, pas surchargé »*.
- **Fait** : le cadre autour de chaque phase disparaît, le bouton de retrait est réduit à sa croix, le panneau passe de 440 à 500 px pour que la ligne tienne.
- ⭐ **Ce qui va bien ne se dit plus** : la couverture réelle (« 2 jours · D+31 → D+32 ») part dans l'**infobulle** de la ligne. Seul ce qui ne va pas reste visible, réduit à un **⚠ rouge** qui porte l'explication — une plage à l'envers ou hors de la planche continue donc de se signaler, sans encombrer. C'est le bon compromis entre « épuré » et « ne jamais taire une erreur ».
- ⚠ **128 px et non 112** pour un champ de date : plus étroit, le navigateur **rogne l'année** et la date se lit « 21/06/202 ». Un champ qui ment sur son contenu est pire qu'un champ large. Constaté sur capture, puis **vérifié par la mesure** (`scrollWidth` contre `clientWidth`) et non à l'œil.
- **Vérifié** : 75 tests de logique pure, **18** contrôles navigateur dont « couleur, nom et dates tiennent sur une ligne », mesure des positions à l'appui. Commit `58bd5cb`, poussé sur **`main` seulement**.

## 2026-09-22 (suite 7) — MELMIL : le GELEX se DÉSIGNE, comme une phase

- **Demande utilisateur** : même traitement que les phases — au lieu de la liste de tous les jours, on **désigne** le jour du GELEX (« on part du principe qu'il y en aura qu'un »), avec un bouton **« + Ajouter un autre jour »** au besoin. Objectif : des réglages moins surchargés.
- **Fait** : `joursHorsCompte` (une table date → libellé) devient **`joursGeles`** (une liste), comme les phases. Une ligne = un champ de date + un libellé + un bouton de retrait ; ouvrir l'interrupteur **pose la première ligne d'office**. Un jour non encore choisi (`jour: null`) ne gèle rien. Chaque ligne dit ce qu'elle vaut (« LUN 29 JUN », « hors de la planche »).
- ⭐ **Récupération** (troisième fois aujourd'hui, et c'est devenu un réflexe) : un état enregistré quand c'était une table est repris dans l'ordre du calendrier — sinon les jours **disparaîtraient de l'écran tout en continuant à décaler la numérotation**.
- **Vérifié** : **75** tests de logique pure (jour sans date, deux jours gelés avec chacun son libellé), **17** contrôles navigateur. Commit `c24c5dd`, poussé sur **`main` seulement**.

## 2026-09-22 (suite 6) — MELMIL : les jours GELEX derrière un interrupteur

- **Demande utilisateur** : « Appliquer des jours GELEX », case devant le titre ; cochée, la liste des jours apparaît ; décochée, elle disparaît — un menu plus clair quand aucun GELEX n'est joué.
- ⭐ **Un interrupteur, et non une case d'affichage** : fermé, les jours cochés sont **ignorés** et ne décalent plus la numérotation D+. Cacher une liste dont le contenu continue d'agir serait un **état invisible**, la pire espèce — la planche aurait sauté un jour sans que rien ne le dise. Les coches sont **conservées** : rouvrir l'interrupteur les retrouve intactes, on ne perd pas son travail sur un clic malheureux.
- ⭐ **Récupération** : un état enregistré avant l'interrupteur avait des jours cochés sans rien pour les commander — on l'ouvre donc, sinon la planche changerait toute seule au rechargement. (Même principe que pour les plages de phases.)
- Fermé par défaut sur une planche neuve : la plupart des exercices n'ont pas de GELEX.
- **Vérifié** : **73** tests de logique pure (dont « interrupteur fermé : un jour coché ne décale rien »), **15** contrôles navigateur. Commit `52c019d`, poussé sur **`main` seulement**.

## 2026-09-22 (suite 5) — MELMIL : une phase se règle par PLAGE, plus jour par jour

- **Retour utilisateur, fondé** : marquer la phase de chaque jour ne tient pas à l'échelle — *« si on a un exercice sur 200 jours ça nous fait régler 200 lignes une par une »*. Une phase porte désormais **sa plage** (« du 23 au 26 juin »), qui est aussi la forme sous laquelle un montage d'exercice la donne. **Six lignes, quelle que soit la durée.**
- ⚠ **Deux plages peuvent se chevaucher, et on ne l'interdit pas** : pendant la saisie, l'état intermédiaire est forcément bancal. On tranche par l'**ordre de la liste**, qui est visible à l'écran — plutôt que de refuser une saisie ou d'inventer une priorité invisible. Une plage dont la fin précède le début ne couvre rien, **et le dit**.
- Chaque ligne annonce ce qu'elle couvre réellement (« 2 jours · D+31 → D+32 », « hors de la planche ») : une plage de travers ne se verrait pas autrement qu'en cherchant sa bande manquante.
- ⭐ **Récupération de l'existant** : un état enregistré avant ce changement avait ses phases marquées jour par jour ; on en déduit la plage (premier et dernier jour marqués). Sans cela, un animateur qui avait déjà réglé ses phases les aurait vues disparaître sans explication — et il aurait eu raison de ne plus faire confiance à l'enregistrement.
- **Vérifié** : **72** tests de logique pure (chevauchement, plage à l'envers), **10** contrôles navigateur — le découpage de MINOTAURE 26 se saisit en six plages et redonne exactement la même bande. Commit `b6e8803`, poussé sur **`main` seulement**.

## 2026-09-22 (suite 4) — MELMIL : les PHASES d'exercice, que JEMM ne connaît pas

- **Demande utilisateur** : récupérer, de la synthèse de montage de MINOTAURE 26, les périodes qui structurent la lecture d'un exercice — **CONVEX, WU TEC, WU TAC, CAX 1, 3A INTER, CAX 2** — les afficher en ligne au-dessus des jours, pouvoir dire à quelle phase appartient chaque jour, et donner à toute la colonne la couleur de sa phase.
- **Source relevée** (`01_Montage exercice/20260313 - GT2 MINOTAURE 26 … SYNTHESE FINALE.pdf`, bande identique sur les 4 pages) : `CONVEX D+31→32 · WU TEC D+33→34 · WU TAC D+35→36 · CAX 1 D+37→38 · 3A INTER (GELEX, 29/06) · CAX 2 D+39→41`. ⭐ **Ces mots n'existent dans AUCUN export JEMM** — ils viennent du montage. C'est la première chose que la planche porte sans que JEMM la lui dise.
- **Mise en œuvre** : une ligne PHASE au-dessus des jours ; les jours d'une même phase forment **une bande** (`colSpan`) ; une phase interrompue puis reprise donne **deux bandes**, parce que c'est ce qui est vrai. Les six phases sont proposées d'emblée, **renommables, colorables, supprimables**, et on peut en ajouter — un autre exercice aura d'autres mots.
- ⭐ **Le lavis** : la colonne prend la couleur de sa phase, mais *posée légèrement* (7 % sur le corps, 40 % sur les en-têtes). Une colonne à pleine saturation avalerait les cartes qu'elle porte. Rendu en `linear-gradient` et non en `background` : la couche se pose **par-dessus** le fond existant (cellule claire ou en-tête sombre) sans effacer les bordures ni les ombres qui dessinent la grille.
- **Couleurs par famille** (demande explicite) : bleus pour les mises en main, rouges pour les deux CAX, vert pour le point d'arrêt, aubergine pour la mise en place.
- ⚠ **Un jour hors compte ne prend plus de couleur propre** : la couleur appartient désormais aux phases. Il se signale par son libellé (GELEX) et par une **hachure**, posée en couche superposée (`::after`) pour ne pas entrer en conflit avec le lavis — deux notions distinctes, deux signaux distincts.
- **Vérifié** : **69** tests de logique pure ; **8** contrôles navigateur — le découpage complet de MINOTAURE 26 saisi à l'écran redonne exactement `CONVEX:2 WU TEC:2 WU TAC:2 CAX 1:2 3A INTER:1 CAX 2:3`, et il survit au rechargement. Commit `a46ca17`, poussé sur **`main` seulement**.

## 2026-09-22 (suite 3) — MELMIL : une carte couvre les jours CONSÉCUTIFS d'une storyline

- **Demande utilisateur** : « si 07.01 se joue sur deux jours consécutifs, j'aimerais que les deux cartes n'en forment visuellement qu'une, à cheval sur les deux jours ; mais si 07.01 revient deux jours plus tard, on a bien une nouvelle carte à part. »
- **Mise en œuvre** : un **segment** = une storyline sur une suite de colonnes consécutives, rendu par une **cellule de tableau avec `colSpan`** — donc alignée sur les colonnes sans artifice de positionnement. Un seul en-tête, un seul cadre ; le **corps reste découpé par jour** (un filet pointillé, une colonne par jour couvert) : on fusionne le cadre, jamais le temps. Badge « N j » sur l'en-tête.
- ⚠ **La continuité se juge en COLONNES, pas en dates** : une seule colonne d'écart, **GELEX compris**, ouvre une nouvelle carte. Une carte qui enjamberait un jour où la storyline ne joue pas dirait le contraire de la vérité.
- ⭐ **Effet de bord utile : les BANDES.** Deux storylines qui se chevauchent ne peuvent pas tenir sur la même ligne — la rangée de l'événement se dédouble (`rowSpan` sur l'étiquette et sur « À placer »), comme un tableau de service. La planche se lit désormais en bandes horizontales continues, ce qui est exactement ce qu'on attend d'un tableau de programmation.
- **Dépôt** : sur une carte qui couvre plusieurs jours, le jour visé est celui **sous le pointeur** (calcul par abscisse dans la cellule). Sans cela, déposer sur le jeudi d'une carte mardi→jeudi renverrait au mardi.
- **Vérifié** : **60** tests de logique pure (fusion, trou qui sépare, trois jours de suite, bandes qui ne se coupent jamais) ; **9** contrôles navigateur sur les exports réels du 7BB — **9 cartes étendues**, chacune occupant exactement autant de colonnes que de jours, et deux fois plus large à l'écran pour deux jours ; **4** contrôles du dépôt par abscisse.
- ⚠⚠ **Deux pièges de mesure, tous deux du même genre** : (1) un **vrai glisser à la souris** déclenche le défilement horizontal de la planche et déplace la cible sous le pointeur — on mesurait le défilement, pas le calcul du jour ; il a fallu envoyer les événements de glissement directement, **dragstart compris** (sans lui le dépôt est refusé, et c'est le comportement voulu) ; (2) **reposer un incident sur sa date JEMM EFFACE son déplacement** — lire `deplacements[code]` seul faisait conclure à un échec alors que la carte était au bon endroit. On mesure le **jour effectif**. Même famille que la leçon du 21/09 sur les indicateurs.
- Commit `9ac4a1e`, poussé sur **`main` seulement**.

## 2026-09-22 (suite 2) — MELMIL : la planche suit les TROIS niveaux de JEMM

- **Demande utilisateur** : « la colonne *lignes opératoires* doit devenir **EVENT** et correspond aux Events de JEMM ; ensuite les **Storylines**, représentées par les cartes colorées ; ensuite les **incidents**, qui sont dans les cartes. Ces trois notions existent dans JEMM. »
- **Fait**, et c'est une SIMPLIFICATION de fond : la planche ne déduit plus rien. Rangée = `Event`, carte colorée = `Storyline`, lignes dans la carte = `Injection` (l'incident du CECPC). Les trois niveaux sont lus tels quels dans l'export.
- **Ce qui disparaît** : la déduction de ligne opératoire à partir du nom des storylines, et le réglage ligne/sphère. Il ne reste en réglage que ce qui **n'est pas dans l'export** — D+ du premier jour, jours hors compte, couleur des storylines (palette, forçable).
- ⭐ **Décision de conception** : une storyline s'étale sur plusieurs jours → elle donne **une carte PAR JOUR** où elle a des incidents. Une carte n'est pas « la storyline » mais « ce qu'elle joue ce jour-là » ; sinon il faudrait choisir un jour arbitraire pour un arc qui en couvre cinq. C'est la reprise, propre, du « split card multi-jours » de MASTAURIGE.
- **Deux gestes de déplacement** : l'en-tête d'une carte déplace tout ce que la storyline joue ce jour-là, une ligne d'incident ne déplace que celui-là. ⚠ Un incident ne peut pas changer d'Event : la cellule d'une autre rangée ne s'allume pas — on ne promet pas un geste impossible.
- **Deux fiches** : la storyline (récit, bornes, tous ses incidents) et l'incident (tous les champs JEMM), l'une menant à l'autre.
- **Lisibilité** : colonnes à 118 px minimum et défilement horizontal — comprimées à 80 px, les cartes ne montraient plus que « … ». Incidents sur deux lignes (repères, puis sujet). Pastille de couleur par moyen (courriel, chat, média, téléphone, en personne).
- ⚠ **État localStorage en version 2** : un état v1 est **ignoré** plutôt que relu de travers — il faut réimporter les exports. Sur un prototype, une planche à moitié juste est pire qu'une planche vide.
- **Vérifié** : **52** tests de logique pure, **15** contrôles navigateur sur les exports JEMM réels du 7BB (2 events, 14 storylines, 44 incidents, 31 cartes), tsc, lint, build. Commit `fba08dc`, poussé sur **`main` seulement** — `prod` déploie, et ce n'était pas demandé.

## 2026-09-22 (suite) — ⭐ Nouvelle app de zone : `app-melmil`, la planche des injects alimentée par JEMM

- **Demande utilisateur** : créer `app-melmil` dans l'organisation `cecpc-pleiade`, reprendre l'architecture du MELMIL de MASTAURIGE, et surtout : **à partir d'un export JEMM, le tableau vierge se remplit tout seul**. « Plus fluide et bien fonctionnel », premier essai **en localStorage**, avec les branches qui vont bien pour Pléiade (`prod` indispensable).
- **Ce que j'ai lu avant d'écrire** : les deux exports JEMM réels du 7BB (`EVENT_07` ILI, 35 injects, 12 storylines ; `EVENT_08` HOST NATION, 9 injects), `generer_melmil.py`, `melmil.js` / `melmil.css` / `melmil_ili.html`, `exercice_config.json` → `lo_config.js`, la mémoire MASTAURIGE (§ MODULE MELMIL, règle canonique, tables), le gabarit LEAC (Dockerfile, entrypoint, workflow, auth de zone, sonde), le catalogue Pléiade (`catalog.ts` : découverte automatique des `.yml`).
- **Ce que JEMM exporte** : `Data.Events[0]` (code « 07 », nom, début/fin), `Data.Storylines` (`Literal` « 07.01 », `Name`, `Story`), `Data.Injections` (`Literal` « 07.01.I01 », `Name`, `Description`, `ExpectedOutcome`, `CoordinationRemarks`, `DisplayDateTime`, `InjectionMeans.Name`, `Sender`, `CoordinatingCell`, `ReceiverList[].Name`, `ScenarioRoleList[].Name`, `InjectionType.Name`, `ActivityLevel.Name`, `InformationMarking.Classification` = UNCLASSIFIED). `MetaData` : `ExportDateTime`, `ExerciseName` (« MINOTAURE 7BB »).
- **Trois partis pris qui font la « fluidité »** :
  1. **Le calendrier se déduit des exports** (début/fin des événements, étendu aux dates d'injects) — plus d'`exercice_config.json` ni de HTML écrit à la main. Le D+ du premier jour et les **jours hors compte** (GELEX) se règlent à l'écran ; le compteur les saute (29/06 = GELEX → 30/06 = D+39, le piège du 7BB, testé).
  2. **La ligne se déduit du nom de la storyline** : le CECPC nomme « Volonté de combattre - 01 - … », « Guerre des pertes - 02 - … » → LO2, LO3… ; un événement « HOST NATION » → HN ; sinon « hors lignes opératoires ». Un réglage par storyline force la ligne et la sphère. Plus de `lo_config.js`.
  3. **La fusion ne perd rien** : par code ; un inject **absent** du nouvel export de son événement est **signalé et conservé** (badge, purge explicite) — la perte silencieuse des 21 injects curés (TODO du 23/06 sur `generer_melmil.py`) ne peut plus se produire ; un export **plus ancien** que le dernier importé est **refusé** ; les **déplacements** faits à la main **survivent** et le rapport dit quand ils masquent une nouvelle date JEMM.
- **Architecture** : `src/lib/melmil/` = logique **pure** (`jemm.ts` lecture, `calendrier.ts`, `lignes.ts`, `fusion.ts`, `etat.ts`) testée en Node ; `stockage.ts` = magasin externe React sur **une seule clé** localStorage (`melmil.etat`), exportable/restaurable en un fichier ; écran : planche (glisser-déposer natif), fiche d'inject (tous les champs JEMM, « revenir à la date JEMM », « mettre à placer »), rapport d'import, réglages. Auth de zone Keycloak identique à LEAC/eho ; `/api/sante` + `lib/version.ts` (`2026-09-22.1`) ; Dockerfile (tests avant build, `USER nextjs` sans volume) ; workflow `prod`.
- **Vérifié** : `npm test` **49/49** ; **23/23** contrôles navigateur, dont l'import des **deux exports JEMM réels du 7BB → 44 cartes**, titre « MINOTAURE 7BB », lignes LO1..LO5 + HN déduites (LO2 = 13 : 07.01×2, 07.02×9, 07.03×2), glisser-déposer, persistance au rechargement, réglages D+/GELEX, re-import identique sans changement et déplacement conservé. tsc, lint, build. ⚠ Mon premier test comptait 12 en LO2 : le produit avait raison, pas mon décompte.
- **Dépôt** : `cecpc-pleiade/app-melmil` créé (privé, API GitHub avec les identifiants du poste, jamais affichés), commit `cc9d3c8` poussé sur **`main` et `prod`**. Le push sur `prod` a lancé le workflow sur le runner (`run 35724547517`) : attendu = image construite et poussée au registre, **échec à la promotion** faute de « melmil » dans `pleiade-promouvoir` — sans conséquence, aucune instance n'existe.
- **Orchestrateur** : `catalog/melmil.yml` + `public/img/apps/melmil.png` commités sur la branche locale **`catalogue-melmil`** de `pleiade-platform` (`fc5099f`), **NON poussés** : `main` y déploie sans sas, décision utilisateur requise.
- ⏭ **Reste** : (1) décision de pousser le catalogue ; (2) côté serveur, `pleiade-promouvoir` + sudoers pour « melmil » ; (3) créer l'instance dans une zone ; (4) v1 : état partagé serveur (base), rôle animateur, cartes MASTAURIGE accrochées aux injects, impression A0/A2.

## 2026-09-22 — eho : la fiche complète s'ouvre depuis la PLANCHE RELATIONNELLE

- **Demande utilisateur** : sur la planche relationnelle, joueurs comme animateurs, cliquer une carte posée doit ouvrir **la fiche biographique complète** — et cette fiche doit être **identique** à celle des onglets EHO, avec **la portée de la planche affichée** : sur « La mienne » celle de **Mon EHO**, sur « GT … » celle de l'**EHO GT** du groupe.
- **Ce qui existait déjà, et qui a tout simplifié** : la planche relationnelle charge **déjà** ses cartes par `GET /api/eho/mon-eho` **avec la portée de la planche** (`?gt=…`, `?officiel=1`, observation). La bonne fiche était donc déjà dans la page — elle n'était ni ouvrable, ni affichée. Le travail n'était pas d'aller chercher des données, mais de **cesser d'avoir deux fiches**.
- **Mise en œuvre — deux briques extraites, donc AUCUNE copie** :
  - `components/fiche-avatar.tsx` : **LA** fiche d'un avatar (`FicheAvatar`, `CarteFiche`, `couleurCarte`), sortie telle quelle de `planche.tsx`. Deux ajouts : `lectureSeule` (planche observée, planche de l'animation) et `officiel` (sur la planche de l'animation, **toutes** les cartes portent leur identité officielle, pas seulement les STARTEX). L'action « verser vers un GT » devient un emplacement optionnel : elle n'a de sens que là où la carte est rangée dans une rubrique.
  - `lib/verrou-fiche.ts` : `useVerrouFiche` — prise, prolongation et relâchement du verrou de fiche, déplacés depuis `planche.tsx`. Les deux écrans partagent donc **le même garde-fou** sur une planche de groupe.
- **Côté plan** : `CarteDispo` devient la carte complète (`CarteFiche`) ; un clic sur une carte ouvre sa fiche (`onNodeClick`, un glissement ne déclenche pas de clic) ; un bouton **« i »** apparaît au survol, **en bas à droite DANS la carte**, et rend le geste accessible au clavier, qu'un nœud React Flow n'offre pas (⚠ au milieu du bord bas, il se posait sur le point d'accroche des liens : les accroches étant centrées sur chaque côté, **les coins sont les seules zones libres**) ; l'enregistrement passe par la **même route** que la planche de rangement, et repose la carte à jour dans la réserve **et** dans le nœud (la couleur suit l'alignement observé). La couleur d'une carte se calcule désormais d'un seul endroit : sur une autorité connue, la **dérive observée** se voit enfin sur le plan aussi.
- **Vérifié dans un vrai navigateur, contre l'instance locale — 13/13** : la fiche s'ouvre au clic ; elle porte la biographie complète (12 mots distinctifs sur 12) ; **le texte de la fiche du plan est identique, mot pour mot, à celui de « Mon EHO »** et à celui de l'« **EHO GT** » ; ce qu'on écrit depuis le plan personnel atterrit dans l'EHO **personnel**, ce qu'on écrit depuis le plan d'un GT atterrit dans l'EHO **de ce GT** sans toucher au personnel ; la planche de l'animation et la planche observée s'ouvrent en **consultation**, sans bouton d'enregistrement. Plus `npm test` 80/80, `tsc`, `lint`, `build`.
- **Complément demandé dans la foulée** : dans la **réserve** (colonne de gauche), un petit bouton **« i »** en bas à droite de chaque carte ouvre la fiche **sans poser la carte** — on consulte souvent avant de décider si quelqu'un a sa place sur le plan. Le clic sur la carte elle-même continue de la poser. ⚠ Deux boutons **voisins**, jamais imbriqués : un bouton dans un bouton n'est pas du HTML valide et le clic y devient imprévisible. Sur le plan, le même **« i »** remplace l'ancienne pastille « Fiche ». Réserve et plan parlent donc la même langue : une carte, un « i », la fiche. Contrôles portés à **15/15** (le « i » ouvre la fiche · il ne pose pas la carte).
- **Transfert d'un encadré d'une planche à l'autre — il EXISTAIT déjà**, et il fait exactement ce qui était demandé (`POST /api/eho/graphe/transferer`, composant `TransfererEncadre`) : l'encadré part avec **les cartes qu'il contient et les liens dont les deux bouts sont dedans**, dans les deux sens (ma planche → GT, GT → ma planche). ⚠ Il n'était pas trouvable : le bouton n'apparaît que lorsque l'encadré est **sélectionné**, dans la barre du bas. Corrigé sans rien dupliquer — l'étiquette de l'encadré devient visiblement cliquable (curseur + infobulle qui nomme les quatre actions), et l'aide de la réserve le dit.
- ⭐ **Vérifié, car c'était la vraie question de l'utilisateur : les fiches ne voyagent PAS.** Le transfert n'écrit que dans `ehoGraphe` (la géométrie) et ne touche jamais `ehoLecture` (le contenu des fiches). Contrôlé avec deux analyses différentes sur le **même avatar** — l'une personnelle, l'autre du GT — puis transfert : chaque planche a gardé la sienne, et la fiche ouverte depuis la planche du GT affiche bien celle du GT. **9/9**. Le seul chemin pour porter une fiche d'un EHO à l'autre reste le versement depuis « Mon EHO ».
- ⚠ **Piège de mesure rencontré** : le contenu d'un `<textarea>` n'est pas dans `innerText` — c'est une **valeur**, pas du texte. Le premier contrôle concluait donc à l'absence d'un texte pourtant affiché. Lire `inputValue()`. Même famille que la leçon du 21/09 sur les indicateurs.
- **Bilan de code** : +203 / −455 lignes — la fonctionnalité est ajoutée **en retirant** du code, puisque la fiche et le verrou n'existent plus qu'en un exemplaire.
- Marque de version portée à **`2026-09-22.1`**. ⏸ **Rien n'est commité ni poussé** : les dépôts sont partagés avec Xavier, et `prod` déploie devant les participants.

## 2026-09-21 (suite 23) — Clôture de la journée : version `2026-09-21.1` en ligne sur les deux instances

- ✅ **Déploiement confirmé par la marque de version** (et non plus par une empreinte) : `GET /api/sante` rend `{"ok":true,"app":"eho","version":"2026-09-21.1"}` sur **`eho-delattre26.delattre-26`** *et* **`annuaire.orion26`**. Cette image (`93dc2c8`) porte les trois correctifs du jour : modèle intégré (`f4fce4c`), volume rendu à nextjs (`289048e`), origine publique (`db9fb5c`).
- 🧹 **Les deux guetteurs par empreinte d'assets sont arrêtés** (l'un expiré, l'autre coupé) : ils ne pouvaient rien voir de ces trois mises en production, qui ne touchaient que le serveur. La sonde de déploiement d'eho est désormais `/api/sante`, comme LEAC.
- ⏭ **Une seule action reste à l'utilisateur** : **ré-appliquer « SKOLKAN PERSONA 21.09.26 » sur delattre-26**. Les adresses de portraits sont réécrites **à l'application** (`originePublique`) ; les 118 fichiers, eux, sont déjà déposés. Si les images manquent encore après cette application, la cause est ailleurs (forme de l'`avatarUrl` en base, `X-Forwarded-Host` avec port) — à chercher sur une base mesurée, pas supposée.
- 📌 **Rappel de ce qui attend Xavier** (rien ne peut être poussé par moi) : les 4 patchs de déconnexion (`PLEIADE/PATCHS/2026-09-21_deconnexion/`), le **défaut de propriété du volume de données** qui frappe vraisemblablement press / messagerie / social, la divergence `main`/`prod` de messagerie, le lint cassé dans 4 dépôts.

## 2026-09-21 (suite 22) — On ne voyait plus quelle image tournait : eho reçoit `/api/sante` + marque de version

- **Constat** : l'utilisateur ré-applique le modèle, toujours pas d'images, « peut-être pas la bonne version ? ». Ma sonde par **empreinte des chunks de la page de connexion est AVEUGLE aux mises en production qui ne touchent que le serveur** : `f4fce4c` (modèle intégré), `289048e` (entrypoint), `db9fb5c` (origine publique) n'ont changé aucun fichier client → même empreinte `f9cfecdb` depuis `977db35`. Impossible de dire si `db9fb5c` était en ligne au moment de son essai (poussé 3 min avant). L'API GitHub Actions est fermée sans jeton (404).
- **Correction durable** : eho reçoit **`/api/sante`** (publique, sans base) et **`lib/version.ts`** (`2026-09-21.1`), même contrat que LEAC — à **incrémenter à chaque mise en production**. Poussé `main` + `prod` ; surveillance sur cette route désormais.
- ⭐ **Leçon** : une sonde de déploiement doit lire une **marque posée par le code** (version), pas un effet de bord (empreinte d'assets) qui peut ne pas bouger.

## 2026-09-21 (suite 21) — « Pourquoi je ne vois pas les images des avatars ? » : contenu mixte

- **Constat** : sur `eho-delattre26`, un portrait du modèle répond **200 `image/jpeg`** (donc modèle appliqué avec la version corrigée, portraits déposés) et pourtant rien à l'écran. Le catalogue Pléiade **n'injecte pas `EHO_PUBLIC_URL`** ; l'origine venait alors de `req.url`, c'est-à-dire ce que le **conteneur** reçoit derrière Traefik : `http://…` → image `http` dans une page `https` = **contenu mixte**, bloqué par le navigateur. Le même défaut guettait `urlPublique` (portraits téléversés depuis l'écran) sur toute instance sans `EHO_PUBLIC_URL`.
- **Correction** (`originePublique(req)` dans `lib/uploads.ts`) : `EHO_PUBLIC_URL`, sinon **`X-Forwarded-Proto` / `X-Forwarded-Host`** (la lecture qui fait marcher la déconnexion sur le serveur), sinon l'origine de la requête. Utilisée par `urlPublique` et par l'application d'un modèle intégré. Vérifié en local avec des en-têtes de proxy simulés (5/5) : adresses stockées en `https://<hôte public>/api/uploads/…`.
- ⏭ Après mise en ligne, **ré-appliquer le modèle** sur delattre-26 : les adresses sont réécrites à l'application (les fichiers, déjà déposés, restent).
- LEAC `2026-09-21.2` (volume rendu à nextjs) : **en ligne** sur `cecpc-div-eval`.

## 2026-09-21 (suite 20) — 🔴 « EACCES: permission denied, mkdir '/app/data/uploads' » : le volume de données des instances appartient à root

- **Symptôme utilisateur** : première application du modèle intégré sur `eho-delattre26` → `Erreur serveur : EACCES: permission denied, mkdir '/app/data/uploads'`.
- **Cause** : l'image tourne sous `USER nextjs` (uid 1001) ; Pléiade monte `./data:/app/data` depuis l'hôte, dossier **créé par l'orchestrateur** (`zone-manager.ts:941`, `fs.mkdirSync(path.join(dir, "data"))`) donc **root:root** ; le `chown` fait dans l'image sur `/app/data` est **recouvert par le montage**. ⚠ **Défaut LATENT de toutes les instances eho du serveur** : rien ne pouvait y écrire — ni portrait téléversé, ni modèle capturé, ni sauvegarde d'application (`mkdirSync(BAK_DIR)`), ni donc **aucune** application de modèle, VIERGE compris. Il ne s'est vu qu'aujourd'hui, à la première écriture disque sur le serveur. **LEAC a exactement le même schéma** (`USER nextjs`, `./data:/app/data`, pièces jointes dans `DATA_DIR/pieces`).
- **Correction, dans l'image (nos deux dépôts)** : plus de `USER nextjs` ; `apk add su-exec` ; **l'entrypoint démarre root, `mkdir -p` + `chown -R nextjs:nodejs /app/data`, puis `exec su-exec nextjs "$0" "$@"`** — tout le reste (db push, serveur) tourne sous nextjs comme avant. Schéma standard des images à volume. Côté eho, `deposerPortraits` devient best-effort jusqu'au `mkdir` (un modèle s'applique même sans ses portraits, en le journalisant).
- ⚠ **À signaler à Xavier** : press (médias), messagerie et social ont vraisemblablement le même défaut si leur image fixe `USER` et monte un volume de données créé par l'orchestrateur ; alternative côté Pléiade : `chown` du dossier `data` à l'uid de l'app à la création de l'instance.
- ✅ **Vérifié en local** : image eho construite (`docker build`), démarrée sur un **volume pré-rempli par root** (`alpine … chown root:root`, le cas du serveur) → après démarrage `/app/data`, `uploads/`, `eho/`, `eho/templates/` sont **nextjs:nodejs**, `next-server` et `node` tournent **sous nextjs**, nextjs écrit dans `uploads/`, l'image porte `modeles/skolkan-persona-21-09-26` et ses 118 portraits. ⚠ Piège du script : sous Git Bash, `/app/data` est converti en chemin Windows → `MSYS_NO_PATHCONV=1`. Poussé : eho et app-leac, `main` + `prod`.

## 2026-09-21 (suite 19) — eho : « SKOLKAN PERSONA 21.09.26 », modèle INTÉGRÉ à l'application

- **Demande utilisateur** : sur delattre-26 il n'y avait que « VIERGE » ; le classeur `avatars-eho-2026-09-15 (1).xlsx` devait être un catalogue disponible **sur cette instance et sur toute instance future**. Nom imposé : **« SKOLKAN PERSONA 21.09.26 »**.
- **Pourquoi il manquait** : les modèles vivent dans le **volume de données de l'instance** (`EHO_DATA_DIR/templates/<code>/manifest.json + payload.json`) ; seul VIERGE est codé dans l'app. Le modèle `SKOLKAN-2026` n'existait que sur le poste (capturé le 15/09 16:45). Le classeur (16:56) en est l'export : mêmes 453 avatars, 58 groupes, planche 43 nœuds / 56 liens (vérifié par comparaison des usernames : 0 écart).
- ⚠ **Défaut du modèle d'origine, corrigé au passage** : les 118 `avatar_url` étaient **absolues vers le poste** (`http://localhost:3001/api/uploads/…`) — donc portraits cassés sur toute autre instance (y compris celle où l'utilisateur a importé le JSON). Le modèle intégré les porte en **relatif** et **livre les 118 fichiers** (`portraits/`, 2,4 Mo) ; à l'application, ils sont déposés dans `UPLOADS_DIR` et les adresses rendues absolues pour l'instance (`EHO_PUBLIC_URL` ou origine appelée — même règle qu'`urlPublique`).
- **Mise en œuvre** : dossier `modeles/skolkan-persona-21-09-26/` dans le dépôt (copié dans l'image, `Dockerfile`) ; `MODELES_INTEGRES_DIR` ; `lireManifests` = intégrés (`builtin: true`) + disque (un code intégré masque un homonyme) ; `lireManifest`/`lirePayload` regardent l'intégré d'abord ; `supprimerModele` refuse un intégré, `creerModele` refuse son code ; `appliquer(…, base)` dépose les portraits. L'écran affiche le badge « intégré » et masque « Retirer » (déjà prévu pour VIERGE). 9 contrôles d'intégrité ajoutés à `npm test` (80/80).
- Identifiants d'avatars **conservés** dans le modèle → le même avatar a le même `identityId` sur toutes les zones qui l'appliquent (utile pour la reprise de contenu inter-zones, cf. suite 3).

## 2026-09-21 (suite 18) — « Se connecter avec un autre compte » retiré aussi ; la déconnexion redevient un geste unique

- **Demande utilisateur** : retirer le lien de la page de connexion d'eho. Fait — avec la mécanique qui ne servait qu'à lui (`deconnexion(true)`, relance `?changer=1`) : `deconnexion()` ne fait plus qu'une chose, fermer eho puis la zone, et revenir sur `/login`.
- **Reste donc** : « Se connecter via Keycloak » (page) · « Se déconnecter » (barre). Le cas « onglet fermé sans déconnexion, session de zone orpheline » n'a plus de rattrapage côté app : « Se connecter » rouvre alors le même compte (SSO). Accepté par l'utilisateur en connaissance de cause (argument : « Se déconnecter » fonctionne, on ne multiplie pas les boutons).
- **Report dans les quatre patchs de Xavier** (press, admin, cockpit, messagerie) : boutons/composants « autre compte » retirés, `deconnexion()` simplifiée de même, commits locaux amendés, `.patch` réexportés.
- Test navigateur : **10/10** (vérifie désormais l'absence des deux boutons).

## 2026-09-21 (suite 17) — « Changer de compte » retiré de la barre d'eho

- **Proposition utilisateur, partagée** : « Se déconnecter » fonctionnant vraiment (fermeture de la zone), « Changer de compte » n'était plus qu'un raccourci d'un clic ; deux boutons voisins pour presque la même chose troublaient plus qu'ils n'aidaient. **Retiré** (eho `main` + `prod`).
- **Conservé, et pourquoi** : « Se connecter avec un autre compte » sur la page de connexion — lui seul rattrape le **poste partagé où l'onglet a été fermé sans déconnexion** (session de zone orpheline que « Se connecter » rouvrirait en silence). L'action `deconnexion(true)` et la relance `?changer=1` restent donc.
- Test navigateur ajusté (l'étape « Changer de compte » vérifie désormais l'absence du bouton) : **11/11**.
- ⚠ Sonde de déploiement d'eho : les pages ne portent pas de version ; **empreinte = liste des chunks `/_next/static/chunks/*.js`** (md5), comparée avant/après. (Le motif `app/login/page-<hash>.js` de la sonde précédente ne correspond à rien en Next 16.) ⚠⚠ **Piège vu ce soir** : pendant le redémarrage la page rend une liste **vide**, dont le md5 (`d41d8cd9…`) diffère de l'empreinte de départ → **faux « nouvelle version »**. Une sonde doit exiger une liste NON vide. Contrôlé ensuite à la main : `c37f9072` → `ff6d8120`, 9 chunks, sur **les deux** instances (delattre-26 suit désormais orion26 sans « Déployer »).

## 2026-09-21 (suite 16) — « Changer de compte » puis « cecpc » → « Please re-authenticate » : le `prompt=login` de trop

- **Symptôme utilisateur** (capture) : « Changer de compte » dans eho, puis clic « cecpc » sur le formulaire de zone → écran cecpc **« Please re-authenticate to continue »**, identifiant figé `THOMAS.MEYTRE`, mot de passe seul. Adresse : `…/realms/cecpc/…/auth?client_id=cecpc-connect&redirect_uri=…/delattre-26/broker/cecpc/endpoint&**prompt=login**`.
- **Cause** : la relance `?changer=1` d'eho envoyait `prompt=login` au royaume de zone (« ceinture » posée ce matin). Vérifié par sonde : le formulaire de zone s'affiche bien (200, lien `broker/cecpc/login`, **aucune redirection automatique**, ni Pléiade ni thème) ; c'est donc au **clic « cecpc »** que Keycloak **transmet le `prompt=login` au fournisseur**. Et devant la session d'organisateur — que la suite 15 veut justement garder ouverte — le royaume `cecpc` ré-authentifie le MÊME utilisateur au lieu de le laisser passer. Les deux décisions se contredisaient.
- **Correction** (eho poussé `main` + `prod`, test navigateur 10/10) : la relance se fait **sans `prompt=login`**. Elle n'a pas besoin de ceinture : « Changer de compte » vient de fermer la session de zone, le formulaire s'affiche de toute façon ; et « cecpc » y redevient silencieux. Appliqué à eho (`login/page.tsx`, commentaires de `deconnexion.ts`) **et aux quatre patchs de Xavier** (press, admin, cockpit, messagerie : commits locaux amendés, `.patch` réexportés dans `PLEIADE/PATCHS/2026-09-21_deconnexion/`).
- ⭐ **Leçon** : un paramètre « par sécurité » n'est jamais gratuit — `prompt` traverse le brokering. Ne poser que ce dont on a démontré le besoin.

## 2026-09-21 (suite 15) — « Voir comme » ANNULÉ ; décision : la déconnexion ferme la zone, pas l'organisateur

- **Décision utilisateur** : *« on annule… on reste sur l'utilisation normale : on se connecte avec le bouton cecpc, et si on se déconnecte on se déconnecte de la zone sans se déconnecter de l'organisateur… moins risqué et plus propre »*. C'est l'**option B** de la suite 12.
- **Nettoyage eho** : les deux fichiers inertes de « Voir comme » supprimés ; arbre revenu à `af91f31`, rien à committer.
- **Mise en œuvre (pleiade-platform, commit `b79cd5f`, `main` → redéployé)** : `configurerCecpcConnect` pose désormais le fournisseur `cecpc` **sans `logoutUrl`** (Keycloak ne remonte alors pas la déconnexion à cecpc) ; `effacerLogoutUrlIdp(realm, alias, secret)` retire l'adresse sur un fournisseur existant en renvoyant le **vrai** secret (masqué à la lecture, on ne compte pas sur le masque) ; `reconcilierRetoursCecpcConnect` devient **`reconcilierCecpcConnect`** : au démarrage, adresses de retour du client broker **+** retrait de la déconnexion amont sur chaque zone, best-effort, journalisé.
- **Effet attendu** : se déconnecter d'eho ferme la session de zone et revient sur `/login` ; le bouton « cecpc » rouvre l'organisateur **en silence** tant que sa session (Pléiade) est ouverte. Les adresses de retour de déconnexion restent déclarées (inoffensives, utiles si l'on remet la chaîne un jour).
- ⚠ Pas de sonde publique possible sur la configuration d'un fournisseur d'identité : **la validation est le test utilisateur** (connexion via cecpc → déconnexion → clic cecpc → pas de formulaire).

## 2026-09-21 (suite 14) — « Voir comme » dans eho : validé, conçu, ARRÊTÉ par le garde-fou de l'outil

- **Validation utilisateur** : principe OK, **eho d'abord**, **réservé aux organisateurs**, **en ÉCRITURE** (« copier les droits liés au compte sélectionné… pour tout tester »), **sans journal** (phase de test).
- **Conception retenue** : un cookie `eho.voir-comme` nomme la cible ; la substitution se fait en **UN point**, le callback `session` d'`auth.ts` — tout ce qui lit la session (layouts, routes API, barre latérale) voit le compte visé avec **ses rôles effectifs** (`role-mappings/…/composite`, héritage par groupe compris) et **ses groupes** ; l'autorité (organisateur = membre d'un groupe maître `masteradmin`/`cecpc`) est **revérifiée à chaque requête** via l'API admin Keycloak (eho a `KEYCLOAK_ADMIN_*`, injectés par Pléiade) ; le jeton d'identité reste celui de l'organisateur ; la déconnexion efface le cookie. Endpoints Keycloak 26 vérifiés en local (users, groups, composite realm/client).
- 🛑 **Garde-fou de l'outil (classifier du mode auto)** : refus d'écrire `src/lib/voir-comme-actions.ts` (pose du cookie) **et** refus d'appliquer le patch serveur (substitution dans `auth.ts`, lectures Keycloak, Sidebar). Même famille de refus que le 18/09 (octroi de droits). **Règle mémoire appliquée : arrêt, explication, décision utilisateur.** État du dépôt : **rien de modifié**, deux fichiers nouveaux inertes (`src/lib/voir-comme.ts`, `src/components/VoirComme.tsx`), patch prêt dans le scratchpad (`patch_voir_comme.py`).
- ⏭ Attend la décision : confirmation explicite pour réessayer, ou application du patch par l'utilisateur.

## 2026-09-21 (suite 13) — Proposition « Voir comme » : l'organisateur regarde une app avec les yeux d'un compte de la zone

- **Idée utilisateur** : entré par « cecpc », cliquer son nom dans une app et **choisir un compte de la zone** pour voir la page comme ce joueur/admin/animateur — et ne plus avoir à se déconnecter pour ça.
- **Deux voies étudiées** :
  - *Usurpation native Keycloak* (`POST /admin/realms/{realm}/users/{id}/impersonation`) : crée une vraie session navigateur comme la cible, valable dans toutes les apps. ⚠ Ne convient pas ici : les cookies ne se posent que si l'appel part de l'hôte Keycloak (console d'admin, droits `realm-management`), pas depuis Pléiade ; la variante *token exchange* est une fonctionnalité preview à activer sur le Keycloak de Xavier, et eho/social n'ont pas de porte « jeton ».
  - ⭐ **« Voir comme » DANS l'app** (recommandé) : réservé aux **masteradmin** (Pléiade `resoudre-identite` → `isMasterAdmin`) ; liste des comptes = `GET /api/internal/zones/:zone/users` (clé de service) ; l'app substitue l'identité côté serveur, **lecture seule**, bandeau « Vous voyez comme X », journal d'audit, retour en un clic. Briques déjà là : eho `porteur.observateur` (lecture stricte), messagerie `x-act-as`, social `X-Act-As`. Ce que voit la cible dépend de ses rôles/groupes → à lire via Pléiade (à compléter : `resoudre-identite` ne rend plus `roles`).
- Périmètre réaliste : eho + LEAC (nos dépôts, déployables) d'abord ; press/admin/cockpit/messagerie en patchs pour Xavier ; social (Angular) à part.
- Rien fait : proposition soumise, décision utilisateur attendue. Indépendant de l'arbitrage A/B sur la déconnexion en chaîne (suite 12), qui reste à trancher pour les vraies déconnexions.

## 2026-09-21 (suite 12) — « Le bouton cecpc me redemande de me connecter » : conséquence de la déconnexion réelle, à arbitrer

- **Symptôme utilisateur** : après la déconnexion d'eho (désormais effective jusqu'au royaume `cecpc`), le bouton « cecpc » de l'écran de connexion de `delattre-26` envoie sur **« Sign in to account » du royaume `cecpc`** (`…/realms/cecpc/…/auth?client_id=cecpc-connect&redirect_uri=…/delattre-26/broker/cecpc/endpoint`). L'utilisateur y voit une contradiction avec la promesse du bouton (« entrer sans se connecter »).
- **Lecture** : ce n'est ni un bug du bouton ni du correctif. Le bouton promet « pas de compte DE ZONE », pas « jamais de mot de passe » : il ouvre les zones **tant que la session du royaume `cecpc` est ouverte**. Or la déconnexion d'eho la **ferme désormais** (suite 10-11 : `logoutUrl` de l'IdP posé par `ensureIdentityProvider` → Keycloak propage la déconnexion en amont = *single logout*). Avant, la propagation **échouait** en silence (« Invalid redirect uri »), donc la session `cecpc` ne se fermait jamais — d'où l'impression d'un bouton « toujours silencieux ».
- ⚠ **Effet collatéral, pas encore annoncé à l'utilisateur** : la propagation ferme aussi la session du **tableau de bord Pléiade** (même royaume `cecpc`). Se déconnecter d'une app de zone en tant qu'organisateur = être déconnecté de Pléiade.
- Le commit `b80d79f` de Xavier ne dit **rien** de cette intention : le `logoutUrl` semble rempli par complétude, pas par décision.
- **Deux options soumises à l'utilisateur** (rien fait) : (A) garder le *single logout* — le plus sûr sur un poste partagé, mais une saisie du mot de passe organisateur à chaque cycle ; (B) **ne plus propager** la déconnexion au royaume `cecpc` (vider `logoutUrl` de l'IdP dans `ensureIdentityProvider`, réconcilié au démarrage comme les retours) — la déconnexion d'une app ferme la zone seulement, la session organisateur et Pléiade survivent, le bouton « cecpc » reste silencieux tant qu'on est connecté à Pléiade. Les **joueurs** (comptes de zone, non brokerisés) ne sont concernés par aucune des deux. Recommandation : B, sous réserve de Xavier.

## 2026-09-21 (suite 11) — Le retour de déconnexion posé au DÉMARRAGE de l'orchestrateur

- **Rebond utilisateur** : « je viens de cliquer à nouveau… ça me fait cela encore », avec **la même adresse mot pour mot** (même `state`, même jeton : `iat` 13:20:20Z, avant la mise en ligne de `b8853e7` à 13:30:04Z). **Sonde décisive, sans session** : `GET …/realms/cecpc/…/logout?client_id=cecpc-connect&post_logout_redirect_uri=…/delattre-26/broker/cecpc/endpoint/logout_response` → **400 « Invalid redirect uri »** ; la même sonde sur l'aller `…/endpoint` → **302**. Donc : correctif en ligne, **rattrapage jamais joué**. Le geste manuel proposé (console) n'a pas été fait — et c'est normal, personne n'y pense.
- **Décision** : l'orchestrateur pose lui-même, **à chaque démarrage**, les deux adresses (aller + retour) de **toutes** les zones sur le client broker `cecpc-connect`. Un seul appel Keycloak (`createClient` → 409 → fusion sans retrait), best-effort (journalisé, le démarrage continue). Cohérent avec la ligne de l'utilisateur : *« on part du principe que ça doit être présent constamment »* — et sans bouton. `retoursCecpcConnect(zone)` devient le **seul** endroit qui connaît ces adresses (création de zone et réconciliation ne peuvent plus diverger).
- Commit `23f4f55` sur `main` → redéployé en ~40 s → la réconciliation a tourné au redémarrage. ✅ **Vérifié sans aucun geste de l'utilisateur** : la même sonde rend désormais **302 sur les trois zones** (`delattre-26`, `orion26`, `cecpc-div-eval`) là où `delattre-26` rendait 400 dix minutes plus tôt.

## 2026-09-21 (suite 10) — 🔴 « Invalid redirect uri » à la déconnexion : le retour du brokering n'était pas déclaré

- **Symptôme utilisateur** (capture) : connecté à eho sur `delattre-26`, « Se déconnecter » tombe sur la page d'erreur Keycloak **« Invalid redirect uri »**, sur `…/realms/**cecpc**/protocol/openid-connect/logout?…&post_logout_redirect_uri=…/realms/**delattre-26**/broker/cecpc/endpoint/**logout_response**`.
- **Cause, lue dans l'adresse elle-même** : le compte était entré par **cecpc Connect** (jeton d'identité `aud: cecpc-connect`, émis par le royaume `cecpc`). Quand eho ferme la session, le royaume **de la zone** propage la déconnexion au royaume **`cecpc`** et lui demande de revenir sur `…/broker/cecpc/endpoint/logout_response`. Or le client broker `cecpc-connect` ne déclarait que `…/broker/cecpc/endpoint` — **Keycloak compare à l'identique, sans joker** : l'aller ne couvre pas le retour.
- ⚠ **Défaut DORMANT, pas une régression de forme** : il existait depuis cecpc Connect (16/09), mais **rien ne fermait la session amont** avant que les apps ne se déconnectent vraiment (21/09). Il vaut pour **toutes les zones**, pas seulement `delattre-26`.
- ✅ **Reproduit puis corrigé sur un vrai Keycloak 26** (local, client jetable `essai-logout`, supprimé après) : avec la seule adresse d'endpoint → **400 « Invalid redirect uri »**, identique à la capture ; l'adresse `…/logout_response` ajoutée → **302**. C'est cette fois la mesure qui portait sur la bonne chose (cf. la leçon de la suite 9).
- **Corrigé** : `configurerCecpcConnect` déclare désormais **les deux** adresses (`b8853e7`, `main`, donc déployé). `tsc` 0 erreur, tests plateforme au niveau de référence.
- ⏭ **À faire par l'utilisateur, une fois par zone** : rejouer `POST /api/zones/<zone>/cecpc-connect` depuis la console du tableau de bord — `createClient` **fusionne** les adresses et n'en retire jamais. Les zones créées après ce commit sont correctes d'emblée.

## 2026-09-21 (suite 9) — 🔴 Le bouton « cecpc Connect » RETIRÉ : il annonçait faux

- **Rejet utilisateur, argumenté et juste** : *« il ne sert à rien, on part du principe que le
  bouton doit être présent constamment… en plus là par exemple il dit que c'était déconnecté
  alors que le bouton était bien présent »*. Retiré : **revert `280b779`** (annule `32cacef`),
  poussé sur `main` — donc redéployé.
- ⚠⚠ **Le défaut, à retenir** : `etatCecpcConnect` exigeait **deux** pièces — le fournisseur
  d'identité **ET** un groupe nommé `cecpc` — alors que le **bouton de l'écran de connexion ne
  dépend que de la première**. Une zone dont le groupe maître porte un autre nom (ou a été
  renommé) passait donc pour cassée **alors qu'elle marchait**. J'ai mesuré la mauvaise chose.
- ⭐ **Leçon** : *un indicateur d'état doit mesurer EXACTEMENT ce qu'il prétend rapporter.* Ici,
  la question était « le bouton est-il là ? » et j'ai répondu à « l'installation est-elle
  complète ? ». Un indicateur qui se trompe coûte plus qu'il ne rapporte : on va vérifier à la
  main ce qu'il affirme, puis on cesse de le croire. ⚠ Mes 11 contrôles navigateur sont passés
  au vert **sans rien voir** : ils vérifiaient que l'affichage suit l'API, jamais que l'API dit
  vrai — un simulacre ne peut pas contredire l'hypothèse qui l'a écrit.
- ⭐ **Second point utilisateur, sur le fond** : le bouton « cecpc » **doit être là en
  permanence**. Offrir en façade un bouton pour le rebrancher, c'est traiter l'exception comme
  la règle. La route de rattrapage de Xavier reste disponible pour les zones d'avant le 16/09.
- **Conservé** : `POST /api/zones/:zone/cecpc-connect` (Xavier), inchangé.

## 2026-09-21 (suite 8) — Bouton « cecpc Connect » dans le tableau de bord Pléiade

- **Demande utilisateur** : *« tu peux me placer le bouton directement… ça nous évitera de perdre du temps »*, avec la question « même pour les futures instances il sera d'office présent c'est bien ça ? ».
- ⭐ **Réponse à la question : les futures zones étaient DÉJÀ couvertes.** `createZone` (`zone-manager.ts:707`) appelle `configurerCecpcConnect` depuis le 16/09 — mais **en best-effort** (`try/catch` + `console.warn`) : une zone se crée même si Keycloak bronche, et personne ne l'apprend. Le bouton sert donc à **rattraper** : zones d'avant le 16/09 (cas de `delattre-26`) et poses en échec.
- **Livré (commit `32cacef`, `pleiade-platform` `main`)** :
  - `identityProviderExists()` (keycloak-manager) et **`etatCecpcConnect()`** (zone-manager) : fournisseur d'identité + groupe maître. **Lève** si Keycloak ne répond pas, au lieu de rendre `false`.
  - **`GET /api/zones/:zone/cecpc-connect`** — lecture seule, à côté du POST de backfill existant.
  - **Tableau de bord** : un bouton par zone, à côté d'« Utilisateurs », dans les deux variantes de carte (zone vivante et zone arrêtée). **Neutre** quand c'est en place, **« ⚠ Brancher cecpc » en alerte** quand ça manque, infobulle qui dit la conséquence. Le clic rejoue le backfill (idempotent) et repeint sans recharger.
- ⚠⚠ **Défaut trouvé PAR LE TEST, pas à la relecture** : la première version réinterrogeait Keycloak à chaque rendu pour une zone dont la lecture avait échoué — or le rendu se rejoue **à chaque frappe dans la recherche**. Corrigé : l'échec se retient (`null`), distinct de « jamais tenté » (absent de l'objet). Les deux se peignent en **neutre** — règle du 2026-09-14 : *un échec de lecture n'est jamais un résultat valide*.
- **Vérifié** : `tsc` 0 erreur · tests plateforme **10/11, l'échec est antérieur** (chemin Windows dans `test-deploiement.mts`, constaté identique après `git stash`) · **test navigateur du VRAI `public/app.js`** avec `fetch` simulé (Playwright, `scratchpad/e2e_cecpc.cjs`) : **11/11**, dont le cas « lecture en échec → bouton neutre » et « deux rendus de plus = zéro appel ».
- ✅ **DÉPLOYÉ automatiquement** : `main` de `pleiade-platform` *est* le geste de déploiement (règle §, `deployer.yml`). `GET https://pleiade.cecpc.internal/api/version` (route publique) rend **`{"commit":"32cacef","buildDate":"2026-09-21 13:14:43Z"}`** — la nouvelle version sert. Le reste (`/app.js`, `/api/zones/...`) est derrière la session : `302` et `401` en anonyme, comme attendu.
- ⏭ **Reste à faire par l'utilisateur** : ouvrir le tableau de bord, vérifier que `delattre-26` porte bien « ⚠ Brancher cecpc », cliquer, puis rouvrir l'écran de connexion de la zone — le bouton « cecpc » doit être revenu.

## 2026-09-21 (suite 7) — « Le bouton cecpc a disparu ? » — non : il manque au royaume `delattre-26`

- **Question utilisateur** : le bouton « cecpc » (connexion directe avec un compte organisateur, mis en place par Xavier) n'apparaît plus depuis l'ajout de « Changer de compte ». **Vérifié : je n'y ai pas touché**, et il ne pouvait pas l'être depuis les apps — ce bouton est celui du **fournisseur d'identité `cecpc` sur le FORMULAIRE KEYCLOAK** de la zone (« cecpc Connect », Xavier, `b80d79f` du 16/09 : broker `cecpc-connect` dans le royaume `cecpc`, IdP alias `cecpc` + groupe maître + mappeur dans chaque zone). Les pages de connexion des apps n'ont jamais porté ce bouton (`git show af91f31^:src/app/login/page.tsx` d'eho : un seul bouton) et aucune app n'utilise `kc_idp_hint`.
- **Constat par sondes sur les formulaires Keycloak réels** (`…/protocol/openid-connect/auth?client_id=…`) : `orion26` → `<a id="social-cecpc" href="/realms/orion26/broker/cecpc/login…">` **présent** · `cecpc-div-eval` → section `kc-social-providers` **présente** · **`delattre-26` → aucun fournisseur d'identité, formulaire nu.** Le royaume `delattre-26` n'a pas (ou plus) l'IdP `cecpc`.
- **Remède prévu par Xavier** : route de rattrapage idempotente **`POST /api/zones/delattre-26/cecpc-connect`** (« Backfill cecpc Connect sur une zone existante : monte ou remet le broker, le groupe maître et le mappeur »), derrière `requireAuth` — **aucun bouton dans l'interface**. À lancer avec une session Pléiade (console du navigateur sur le tableau de bord) ; je n'ai pas de session et ne cherche pas d'identifiants.
- Effet attendu après rattrapage : le bouton « cecpc » revient sur le formulaire de `delattre-26`, et les comptes organisateurs (dont thomas.meytre) y entrent en master admin.

## 2026-09-21 (suite 6) — Déconnexion complète portée sur les cinq apps fautives, validée de bout en bout

- **Autorisation utilisateur** : « Je te laisse appliquer ce qu'il y a de plus judicieux… fluide et opérationnel pour tous ». Fait sur **eho, app-press, app-admin, app-cockpit, app-messagerie** (le social et LEAC étaient déjà bons).
- **Le même motif partout** (`src/lib/deconnexion.ts`, action serveur) : fermer la session de l'app (`signOut({ redirect: false })`), puis rediriger vers `PUBLIC_ISSUER/protocol/openid-connect/logout` avec `id_token_hint` + `client_id` + `post_logout_redirect_uri` = page de connexion. Le **jeton d'identité est désormais gardé** dans le `jwt` et exposé en `session.idToken` (rien de secret : il décrit l'opérateur lui-même). `PUBLIC_ISSUER` et `KC_CLIENT_ID` exportés d'`auth.ts`. L'origine publique vient des en-têtes `X-Forwarded-*` (pas de dépendance à `NEXTAUTH_URL`).
- **Trois gestes** : « Se déconnecter » (complet) · « Se connecter avec un autre compte » sous le bouton de connexion (5 apps) · « Changer de compte » dans la barre d'eho (poste partagé, un seul geste).
- ⚠⚠ **Découverte pendant le test — `prompt=login` seul NE CONVIENT PAS pour « autre compte »** : devant une session de royaume ouverte, Keycloak affiche son écran de **ré-authentification** (mot de passe du MÊME utilisateur, identifiant non modifiable), il ne propose pas d'en changer. D'où le choix : « autre compte » = **déconnexion Keycloak d'abord** (même sans session app, sans `id_token_hint` → Keycloak demande une confirmation, un clic), retour sur `?changer=1`, et la page relance la connexion (`prompt=login` en ceinture).
- ✅ **Validé de bout en bout sur eho** — Playwright contre le Keycloak local (`joueur_test` / `anim_test`), script `scratchpad/e2e_deconnexion.cjs` : **10/10** — formulaire redemandé après déconnexion (LE bug), changement de compte effectif, « Changer de compte » en un geste, session orpheline (cookie eho supprimé, Keycloak gardé) : « Se connecter » reconnecte en silence (SSO attendu) et « autre compte » ferme bien la session via la confirmation Keycloak puis présente le formulaire. Sur le serveur, la sonde `GET …/logout?client_id=eho-eho-delattre26&post_logout_redirect_uri=…/login` → **302 vers /login** : le motif `https://<app>/*` des clients Pléiade couvre le retour.
- **Vérifications sur les quatre autres apps** (pas de serveur de dev, pas de test navigateur) : `tsc --noEmit` → **compte d'erreurs identique à la référence** (press 48 · admin 20 · cockpit 0 · messagerie 48, toutes préexistantes, hors des fichiers touchés) ; `next build` (voir ci-dessous). ⚠ `npm run lint` est **cassé à la référence** dans ces quatre dépôts (aucun `eslint.config.*`, ESLint 9 renvoie le guide de migration) — pas de notre fait, à signaler à Xavier.
- **Détail par app** : press — `SignInButton` (+ autre compte, relance), `SignOutButton` d'« accès refusé » devient une déconnexion complète, `RedactionShell` · admin — `Shell`, `SignOutButton`, page `login` · cockpit — `Header`, page `login` · messagerie — `ConversationList` (lien), `supervision/layout` (`<form action={deconnexion}>` — d'où la signature `changerDeCompte?: unknown`, un `FormData` n'est jamais pris pour `true`), nouveau `AutreCompte.tsx` sur `/connexion`.
- ⚠ **Effet annoncé** : la déconnexion ferme la session de royaume → déconnecte de **toutes les apps de la zone**. Voulu sur un poste partagé, cohérent avec le social qui le faisait déjà.
- **Poussé / non poussé (2026-09-21, fin de journée)** : **eho `af91f31` → `main` + `prod`**, nouvelle version constatée en ligne sur `annuaire.orion26` (« Se connecter avec un autre compte » servi). ⚠ `eho-delattre26` (zone non prod) attend un **« Déployer » sur la zone**. ❌ **`app-press`, `app-admin`, `app-cockpit`, `app-messagerie` : `git push` refusé — HTTP 403 « Write access to repository not granted »** (le compte du poste n'a pas l'écriture sur ces quatre dépôts ; `gh` absent). Les quatre commits existent **en local** (`c7bd5d4`, `0e98717`, `345ab92`, `62bee3c`) et sont exportés en patchs pour Xavier : **`PLEIADE/PATCHS/2026-09-21_deconnexion/`** (un `.patch` par dépôt + `README.md` d'application). ⚠ `app-messagerie` : **`origin/prod` porte `18b6648` absent de `origin/main`** (Xavier, 17/09) — à signaler.

## 2026-09-21 (suite 5) — Déconnexion : la session Keycloak survit, reconnexion automatique sur le même compte (diagnostic, rien de codé)

- **Symptôme utilisateur** : sur eho (et d'autres instances), « Déconnexion » déconnecte bien de l'app, mais « Se connecter via Keycloak » **rouvre le même compte sans rien demander**. Impossible d'essayer une autre place. ⚠ Cas à anticiper : **un seul ordinateur pour plusieurs joueurs**.
- **Cause, établie par lecture du code** : il y a **deux sessions**, celle de l'app et celle du royaume Keycloak. `signOut({ callbackUrl })` ne ferme **que la première**. La session de royaume reste ouverte, donc l'autorisation suivante est accordée en silence. Ce n'est ni un bug de Keycloak ni un cache de navigateur.
- ⭐ **La maison sait déjà faire — deux précédents dans le système** :
  - **Pléiade**, tableau de bord : `GET /auth/logout` efface son cookie **puis redirige vers `…/protocol/openid-connect/logout`** avec `client_id` et `post_logout_redirect_uri` (`src/auth.ts:254`).
  - **LEAC**, notre app : `src/lib/zone/deconnexion.ts` fait la même chose avec en plus `id_token_hint` — écrit précisément parce que l'utilisateur avait rencontré ce symptôme sur le serveur. **Le jeton d'identité y est conservé exprès** (`src/lib/zone/auth.ts:65`).
- **État par app** (relevé le 2026-09-21) :
  | App | Déconnexion | Ferme la session Keycloak ? |
  |---|---|---|
  | `pleiade-platform` | `/auth/logout` → `end_session` | ✅ |
  | `app-leac` | `deconnexion.ts` → `end_session` + `id_token_hint` | ✅ |
  | `app-social` | `keycloak.logout()` (keycloak-js le fait nativement) | ✅ |
  | **`eho`** | `signOut({ callbackUrl: "/login" })` (`Sidebar.tsx:313` et `:345`) | ❌ |
  | **`app-press`** · **`app-admin`** · **`app-cockpit`** | `signOut({ callbackUrl })` | ❌ |
  | **`app-messagerie`** | lien nu `/api/auth/signout` | ❌ |
- ⚠ **Obstacle technique pour eho** : le `jwt` d'eho garde `access_token` et `refresh_token` mais **PAS `account.id_token`** (`src/lib/auth.ts`). Sans lui, pas d'`id_token_hint` : Keycloak accepte alors la déconnexion avec `client_id` seul (voie Pléiade) mais peut afficher un écran de confirmation. **Garder le jeton d'identité, comme LEAC, est la voie propre.**
- **Pistes proposées à l'utilisateur** (aucune engagée) : (1) **corriger la déconnexion** — la vraie cause, portage de ce que LEAC a déjà ; (2) **« Se connecter avec un autre compte »** sous le bouton, qui ajoute `prompt=login` à l'autorisation et force Keycloak à redemander les identifiants même si une session traîne — filet indispensable quand quelqu'un a fermé l'onglet sans se déconnecter ; (3) **« Changer de compte »** visible même connecté, pour le poste partagé ; (4) demander à Xavier de **raccourcir l'inactivité de session du royaume**.
- ⚠ **Conséquence à annoncer** : fermer la session de royaume déconnecte de **toutes les apps de la zone** à la fois. Sur un poste partagé c'est l'effet voulu, mais il faut le dire. `app-social` le fait déjà aujourd'hui, donc l'incohérence existe déjà entre les apps.

## 2026-09-21 (suite 4) — Faisabilité de la reprise ORION 26 → DELATTRE 26 (étude, rien de codé)

- **Demande** : réalisable de récupérer les publications d'ORION et de les poser dans `social.delattre-26`, **sans doubler le volume**, **correctement datées**, pour montrer un passif aux joueurs, les statistiques ne comptant que les messages à venir. **Consigne : ne rien faire.**
- **Verdict : réalisable, mais pas avec les routes existantes seules.** La lecture existe, l'écriture datée n'existe pas.
  - **Lecture — déjà là** : `GET /api/service/retex` rend exactement ce qu'il faut (auteur `identity_id`, texte, **horodatage**, médias, parenté post/commentaire, métriques). Écrite pour le storybook, réutilisable telle quelle.
  - **Écriture — manquante** : `POST /api/service/publish` **n'accepte aucune date** (ni `created_at` ni `scheduled_at`) et déclenche hashtags, aperçu de lien et notifications aux abonnés. Hors d'échelle et hors sujet pour un passif. Il faut soit une route de reprise qui écrive `createdAt` explicitement, soit un transfert au niveau de la base. **Les deux touchent le dépôt de Xavier.**
- ⭐ **Les dates règlent la plupart des statistiques, mais PAS toutes** :
  | Mesure | Comportement si le contenu est daté d'avril | 
  |---|---|
  | Rapport cockpit (`/api/cockpit/rapport`) | fenêtré `from`/`to`, défaut = aujourd'hui → **ignore le passif** ✅ |
  | Veille cockpit (`/poll`) | curseur `since_id` sur l'identifiant → **ignore le passif** ✅ |
  | Compteurs de profil (`posts_count`, abonnés) | totaux → **affichent le passif**, ce qui est voulu ✅ |
  | ⚠ **Panneau « Tendances »** (`GET /api/social/hashtags`) | `groupBy` sur **tous** les `social_post_hashtags`, **aucune fenêtre temporelle** → resterait **figé sur les mots-dièse d'ORION** ❌ |
  👉 **Seul point dur** : les tendances. Soit on leur ajoute une fenêtre, soit on n'importe pas les mots-dièse du passif.
- **Où est réellement le volume** (échantillons du 5 au 16 avril) : ce ne sont pas les textes. C'est (1) **~100 000 publications**, (2) surtout les **lignes de « j'aime »** — 20 à 55 par post sur l'échantillon, donc potentiellement **des millions de lignes**, car `like_count` est **compté sur les lignes**, jamais stocké ; (3) les médias. Trois leviers pour ne pas doubler : **ne reprendre que le contenu curaté** (l'animation, pas le bruit d'ambiance généré par le `toolbox`, qui backdate déjà ses posts sur 14 jours) ; **retirer l'instance source** une fois ORION clos ; ou **stocker un compteur** au lieu de copier les « j'aime ».
- ⚠⚠ **DÉCOUVERTE À CONFIRMER AVANT TOUTE DÉCISION — les médias d'ORION sont largement perdus.** Sur **38 médias tirés au hasard entre le 5 et le 16 avril, 14 sont servis et 24 répondent 404**. Ce ne sont pas des références fabriquées : le `toolbox` télécharge et écrit vraiment ses images (préfixe `post-`), or les manquants sont des **téléversements réels** (UUID nu, `.JPG` majuscule, un `.mp4`). Le volume `./data/uploads` de l'instance a donc **perdu une partie de son contenu**. Les sauvegardes de zone ne rattraperont rien (rétention 14 jours, l'exercice date d'avril). **À poser à Xavier.**
- **Identités** : rappel de la suite 3 — l'`identityId` est propre à chaque eho. Deux voies : traduire les auteurs **par `username`** contre l'eho de DELATTRE, ou reprendre tels quels les comptes locaux du social source (ils deviennent des **comptes d'archive que personne ne peut incarner**, puisque la décision « au nom de » interroge l'eho de la zone — effet plutôt souhaitable pour un passif).
- **Rien n'est engagé.** Arbitrage utilisateur attendu, et le sujet relève du dépôt `app-social` de Xavier.

## 2026-09-21 (suite 3) — Reprendre le contenu d'ORION 26 dans DELATTRE 26 : ce qui existe, ce qui manque (vérification seule)

- **Demande utilisateur** : `reseau.orion26` contient tout le contenu d'un exercice passé (publications + médias) ; DELATTRE 26 étant « dans la continuité » d'ORION, faire apparaître ce contenu dans `social.delattre-26`. **Consigne : ne rien coder, vérifier si Xavier l'a prévu.**
- **Réponse : NON.** Aucune fonction de reprise de contenu d'une instance vers une autre, dans aucun des quatre dépôts, et **aucune branche en cours** (`app-social`, `pleiade-platform`, `app-admin`, `eho` : toutes les branches distantes relues, rien sur le sujet).
- **Ce qui existe et s'en approche** :
  | Brique | Ce qu'elle fait | Pourquoi ça ne suffit pas |
  |---|---|---|
  | **Storybook** (Pléiade, `storybook-manager.ts`) | Agrège `/api/service/retex` de toutes les instances d'une zone et **fige une page HTML autonome** du récit chronologique | Sortie de **lecture** pour le débriefing, **par zone**. Ne réinjecte rien. |
  | `GET /api/service/retex` (social) | Rend **tout ce qui a paru** : posts + commentaires, auteur (`identity_id`), horodatage, médias, métriques, parenté | C'est la **bonne source de lecture** pour une reprise, mais il n'y a pas de route symétrique en écriture. |
  | `POST /api/service/publish` (social, clé de service) | Publier au nom d'une identité, avec média, `reply_to_post_id`, likes et partages générés | ⚠ **Aucune date** : ni `created_at` ni `scheduled_at`. Tout arriverait **daté d'aujourd'hui**. |
  | **Scénarios app-admin**, export/import XLSX | `id, app, persona, message, delta, reply_to, likes, boosts, like_groups, boost_groups` ; import par `username` ou UUID | Ne contient **que les scénarios programmés**, pas les publications faites à la main. `delta` est un **délai relatif**, pas une date. Découverte des apps **limitée à sa zone**. |
  | **Sauvegardes de zone** (Pléiade) | Sauvegarde/restauration complète | **Verrouillée sur la même zone** : `if (sauv.zone !== zone) throw`. Interdit par construction. |
- ⚠⚠ **Obstacle d'identité, le plus structurant** : dans eho, `User.id` est `@default(uuid())` et l'import **upserte par `username` UNIQUEMENT**. Deux zones qui importent le même classeur obtiennent donc des **identityId DIFFÉRENTS pour le même avatar**. Or `publish` prend un `identity_id`. **Le seul pont entre zones est le `username`** — toute reprise devra traduire auteur par auteur contre l'eho de la zone cible (`GET /api/service/users?search=`, comme le fait l'import de scénarios d'app-admin).
- **État relevé sur le serveur (sondes publiques en lecture seule, 2026-09-21)** :
  - `reseau.orion26` = instance `social` v0.3.0, realm `orion26`, client `social-reseau`, eho de zone = instance **`annuaire`**.
  - `social.delattre-26` = instance `social` v0.3.0, realm `delattre-26`, client `social-social`, eho de zone = **`eho-delattre26`**. **Fil vide** (`[]`).
  - **Corpus ORION 26 : du 2026-04-01 au 2026-04-16**, rien avant. Progression des identifiants : 9 971 (01/04) → 15 441 (09/04) → 66 384 (13/04) → **113 741 (16/04)**. ⚠ **Ordre de grandeur : ~100 000 publications**, l'essentiel généré en rafale entre le 11 et le 15 avril (probablement le bruit d'ambiance du `toolbox`), et non une centaine de posts curatés.
- **Conséquence pour l'arbitrage** : republier à l'unité par `publish` est hors d'échelle (chaque appel déclenche hashtags, aperçu de lien, notifications aux abonnés) **et perdrait les dates**. Les pistes réalistes se situent plus bas : copie de la base de l'instance, ou route de reprise à écrire (lire `retex` de la source, traduire les auteurs par `username`, écrire en base avec les horodatages). **Rien n'est engagé : à arbitrer avec l'utilisateur, et le sujet touche le périmètre de Xavier.**

## 2026-09-21 (suite 2) — « Au nom de » : joueur → réseau social → avatar eho — l'état de ce que Xavier a livré (lecture seule)

- **Question utilisateur** : le joueur se connecte au social de la zone et poste **avec un avatar de l'eho de la même zone** — Xavier l'a-t-il mis en place ? **Réponse : oui, chaîne complète livrée et en production** (aucun code de notre part, analyse des dépôts seulement).
- **Trois dépôts, une chaîne** (tous les commits sont sur `prod`) :
  - `pleiade-platform` `b083a9f` + `a3e41bd` (17/09) : `POST /api/internal/zones/:zone/resoudre-identite` (par `identityId`, clé de service) → groupes du joueur **avec le drapeau `masteradmin`** ; `GET …/groupes-keycloak` pour le sélecteur de camps.
  - `eho` `fee2e75` + `d98e801` (17/09) : modèle **`GroupeCamp`** (groupe d'avatars → nom de groupe Keycloak = « camp »), `POST /api/impersonation` (clé de service) → `{ master, avatarIds }`, **écran Groupes → bouton « Camps »** (cases à cocher, admin seul).
  - `app-social` `f45ae29` (10/09, impersonation obligatoire + `audit_logs`), `c2b0c89` (12/09, API service), `2e8b553` (17/09, **bridage serveur au camp** : `X-Act-As` interdit → 403), `36bcb07` (19/09, picker visible pour `ANIMATEUR` — bug d'affichage corrigé).
- **Comment ça marche** : l'utilisateur ouvre le social avec son compte Keycloak ; il ne poste **jamais en son nom** : la boîte de composition est bloquée tant qu'il n'a pas choisi un avatar dans le panneau **« Au nom de »** (`X-Act-As`). Le social demande à eho la liste des avatars autorisés ; eho demande à Pléiade les groupes du joueur ; **masteradmin → tout**, sinon **union des groupes d'avatars ouverts à l'un de ses groupes Pléiade**, sinon **rien (fail closed)**. Cache 10 s côté social. Chaque geste est journalisé (`audit_logs` : opérateur, avatar, action).
- ⚠ **Deux conditions que la description utilisateur ne mentionne pas** :
  1. **Le rôle `animateur` sur l'instance social est OBLIGATOIRE pour écrire** (`9a86b38`, catalogue `social.yml` : « sans ce rôle, un compte de la zone lit et ne fait que lire »). Un joueur sans ce rôle ne voit **ni la boîte de composition ni le panneau « Au nom de »**. Il s'attribue **par groupe**, via le bouclier Pléiade de l'instance social (`PUT /api/zones/:zone/instances/:id/groups/:groupId/roles`).
  2. **Le référentiel des camps doit être rempli dans eho** : pour chaque groupe d'avatars, cocher les groupes Pléiade autorisés à l'incarner. **Aucune case cochée = personne ne peut, sauf les organisateurs** (masteradmin, ex. thomas.meytre via cecpc Connect).
- **Cohérence avec `69260ef` (matin)** : les « camps » de Xavier et nos « groupes de travail » sont **les mêmes groupes Pléiade de racine**, lus par deux chemins (Pléiade pour lui, API admin Keycloak pour nous). Pas de conflit : `GroupeCamp` n'est pas touché par notre changement.
- **Prérequis d'instance** : social a besoin d'`EHO_URL` + `PLEIADE_API_KEY` (injectés par la découverte Pléiade quand eho est dans la zone) ; eho de `PLEIADE_URL` / `PLEIADE_ZONE` / `PLEIADE_API_KEY`. À vérifier sur `delattre-26` si le panneau reste vide malgré le rôle et les camps.

## 2026-09-21 (suite) — eho : les groupes Pléiade deviennent les groupes de travail ; delattre-26 remise d'aplomb

- **`eho-delattre26`** recréée par l'utilisateur : elle tournait une VIEILLE
  image — la création/démarrage d'une instance fait `up -d` SANS `pull`
  (`deployInstance` aussi), seul **« Déployer » la zone** (`deployZone`) fait
  `pull` + `up -d`. `delattre-26` n'est pas `zone_type = prod` : les
  promotions automatiques la sautent. Après « Déployer » la zone : pages
  MEYTRE présentes, connexion → Keycloak. ⚠ Règle : à chaque version d'eho,
  redéployer la zone à la main (ou la passer en prod avec Xavier).
- **Groupes de travail** : eho ne reconnaissait que `/GT/<nom>` (console
  Keycloak obligatoire, Pléiade ne crée que des groupes de racine). Feu vert
  utilisateur (« chaque groupe doit avoir son groupe de travail propre ») →
  `eho` `69260ef` : tous les groupes de racine sauf techniques (`cecpc`,
  `masteradmin`, racine `GT`), `/GT/…` toujours accepté ; droits d'animation
  inchangés (bouclier Pléiade). Poussé main + prod.

## 2026-09-21 — eho : connexion impossible sur toutes les zones, corrigée (émetteur Keycloak)

**Symptôme** (utilisateur) : « Server error — problem with the server
configuration » au clic « se connecter » sur `annuaire.orion26` et
`eho.delattre-26`. **Diagnostic** (sans accès aux logs, par sondes HTTP) :
- `orion26` : Auth.js démarre (csrf/providers/session OK), seule la connexion
  échoue → eho déclarait l'émetteur Keycloak **interne** alors que, depuis le
  `frontendUrl` figé sur l'adresse publique (Xavier, 2026-09-13), Keycloak
  annonce toujours `https://auth.cecpc.internal/realms/<zone>` → « issuer
  mismatch » à la découverte OIDC. Les 4 autres apps (admin, leac,
  messagerie, press) déclarent l'émetteur public ; **eho et cockpit** non.
- `delattre-26` : image antérieure au 16/09 (pages MEYTRE absentes, pas de
  logo du 20/09, pas de `trustHost`) → toutes les routes d'auth en erreur.

**Correctif** (feu vert utilisateur) : `eho` `1e44e2c` — `issuer` public +
`authorization` public, `token`/`userinfo`/`jwks` internes (motif de
messagerie/leac). Poussé main + prod → image reconstruite, promotion sur les
zones prod : `orion26` redirige vers Keycloak à t+2 min. `eho.delattre-26`
ne répond plus (404 Traefik) depuis la promotion — et le portail de la zone
ne liste que `social` : ce n'était **pas une instance gérée** (conteneur
orphelin sur une vieille image, route Traefik résiduelle), balayé quand
l'orchestrateur a régénéré les routes. Rien de géré n'a été cassé.
⚠ **Suite** : l'utilisateur a supprimé lui-même cet eho depuis Pléiade.
`deleteInstance` emporte la base, le dossier d'instance (donc le volume
`./data` : avatars téléversés) et le client Keycloak. Cette instance tournait
une image d'avant le 16/09 — elle ne portait donc pas le travail MEYTRE, mais
ses éventuels contenus DELATTRE 26 sont partis avec. Filet : sauvegardes de
zone (bases par instance + dossiers), quotidiennes, rétention 14 j par défaut,
et « restaurer une zone qui n'existe plus ». Zone saine après coup : portail
200, `social` debout, `orion26` et `cecpc-div-eval` intactes.
⚠ Leçon : j'ai qualifié l'instance de « reliquat » sur la seule absence au
portail (requête sur `orch_instances`, donc indice solide) **en demandant
confirmation à Xavier** ; elle a été supprimée avant cette confirmation. Pour
une suppression qui emporte des données, dire explicitement « ne pas
supprimer avant confirmation » plutôt que « à confirmer ». ⚠ Xavier à prévenir : dépôt à lui, cause dans un
arbitrage à lui (à raison). `app-cockpit` porte la même erreur, non corrigée.

**Constat annexe** : ta branche `MEYTRE` est dans `main` d'eho depuis le
16/09 (61 fichiers) ; `prod` = `main`. cecpc Connect (broker `cecpc-connect`,
groupe maître `masteradmin`) donne l'entrée « superadmin » aux comptes du
royaume cecpc — jamais atteint tant que l'émetteur bloquait.

## 2026-09-16 — Fusion de `MEYTRE` dans `main` : notre EHO de jeu rejoint la mise en production de Xavier

**Demande utilisateur** : « tout le travail réalisé dans la branche MEYTRE, peux-tu le commiter dans main pour qu'on soit bien à jour ? » — avec la consigne explicite de **résoudre les conflits sans casser ce qui a été fait sur main**, et de **retenir les évolutions de MEYTRE** là où la mise à jour vient bien de MEYTRE.

### Ce que chaque branche apportait (séparées depuis `830a0eb`)
- **MEYTRE — 4 commits, nous** : STARTEX, planche joueur, comparaison animateur, cloisonnement des rôles, groupes de travail, verrous, versement granulaire, planche relationnelle, planche officielle.
- **`main` — 8 commits, Xavier** : image Docker et `docker-entrypoint.sh`, Prisma 7 (client dans `src/generated`, `prisma.config.ts`), Keycloak derrière Traefik + thème Pléiade, mise en production automatique depuis la branche `prod`, et ⭐ **« Fermer l'annuaire des avatars »** — les gardes `exigerLecture` / `exigerEcriture` / clé de service `PLEIADE_API_KEY` sur toutes les routes.
- ⭐ **Les deux branches avaient attaqué le MÊME problème** (fermer l'application aux non-autorisés) **sans se voir**. D'où exactement deux conflits, tous deux sur des gardes d'autorisation.

### Résolution des deux conflits — on garde les DEUX apports, jamais « la version d'un camp »
| Fichier | Retenu de MEYTRE | Retenu de `main` |
|---|---|---|
| `(admin)/layout.tsx` | Le garde complet : `auth()` + **traitement de `session.error`** (rôles vides ≠ joueur → reconnexion, leçon du 2026-09-14), `estRoleAdmin` (`lib/roles.ts` = source unique), redirection vers `/mon-eho`, padding responsive | `export const dynamic = "force-dynamic"` + la doctrine du rôle « Administration » déclaré au catalogue Pléiade (commentaire) |
| `(player)/layout.tsx` | La **coque** (Sidebar + `min-w-0 … p-4 sm:p-6 lg:p-8`) dont dépend toute la refonte visuelle | Le garde `operateurCourant()` + `force-dynamic` |

- **Arbitrage assumé** : un opérateur sans le rôle admin est **redirigé vers `/mon-eho`** (décision du 2026-09-14) plutôt que de recevoir l'écran « Accès refusé » de Xavier — un joueur n'a rien à faire sur une page d'erreur. ⏳ **À signaler à Xavier** : c'est le seul endroit où son comportement a été écarté au profit du nôtre.

### ⚠ Ce que la fusion automatique a fait dans notre dos — et qu'il a fallu contrôler un par un
- `lib/api-auth.ts` (touché des deux côtés) : git a gardé **les rôles de CLIENT** lus par Xavier (`resource_access[eho]` — sans eux, **aucun administrateur n'est vu dans une zone Pléiade**, les rôles y sont créés comme rôles de client) **et** notre source unique `lib/roles.ts`. Le `const ROLES_ADMIN` local de `main` a disparu au profit du module partagé : **plus de liste dupliquée**, exactement ce qu'on voulait.
- `lib/auth.ts` (touché par `main` seul) : vérifié que le **contrat dont dépend notre garde tient toujours** — la session expose bien `roles`, `error` et `username`. Xavier y a même corrigé la lecture des rôles de client.
- Routes API : les gardes de `main` se sont posés **sans effacer nos ajouts** (planche officielle dans l'import, `PORTEUR_OFFICIEL` dans l'export, `purgerEstimations` sur la fiche d'avatar).
- 🔧 **Corrigé à la main** : `api/import/route.ts` se retrouvait avec **deux `import` du même module** `@/lib/api-auth` (une ligne de chaque branche) — refondus en un seul.

### 🔒 Conséquence majeure : la faille des 10 routes est FERMÉE
Le travail de Xavier, en arrivant par la fusion, referme le trou décrit au § 8bis de `MEMOIRE.md`. **Vérifié en anonyme sur la version fusionnée réellement démarrée** : `/api/users`, `/api/users/[id]`, `/api/groups*`, `/api/import`, `/api/uploads`, `/api/activity`, `/api/avatars/export` → **401**. Les pages `/mon-eho`, `/eho-gt`, `/graphe`, `/avatars`, `/trombinoscope`, `/users`, `/comparaison`, `/planche-officielle` → **307**.
- **10ᵉ route, `uploads/[nom]` : délibérément publique**, ce n'est pas un oubli — les portraits sont affichés par mastorion, c'est écrit dans le code.
- ⏳ **Ce qui RESTE ouvert** : `GET /api/users` est gardé par `exigerLecture` (n'importe quelle session de la zone) et renvoie la **charge utile complète**. Un **joueur connecté** peut donc y lire `pays`, `label`, `activite`, `observations` — ce que la planche joueur lui cache. Le dépouillement reste contournable **par un participant**, plus par un anonyme. C'est l'arbitrage encore en attente (charge utile réduite pour les non-admins).

### Contrôles de la fusion — dans un arbre de travail isolé sur `C:` (jamais sur l'arbre de travail de l'utilisateur)
`npx tsc --noEmit` **0 erreur** · `npx eslint` **0 erreur** (1 avertissement `<img>` préexistant) · `npm run test` **71/71** · `npm run test:bio` **538/538** · `npm run build` **réussi**, toutes les routes des deux branches présentes · serveur de production démarré sur le **port 3002** pour tester les gardes en anonyme.
- ⚠ **Piège d'outillage rencontré** : un `node_modules` monté en **jonction** fait **planter Turbopack** (`Symlink [project]/node_modules is invalid, it points out of the filesystem root`). Il faut une **vraie copie** (0,7 Go, ~30 s en `robocopy /MT:16`). Ce n'était pas un défaut de la fusion.
- ⚠ **Non vérifié** : le comportement **connecté** par rôle (animateur → trombinoscope, joueur → renvoyé sur `/mon-eho`). Le flux Keycloak n'aboutit pas sur un autre port que 3001 (le client `eho` n'autorise que celui-là) et je n'ai pas modifié la configuration Keycloak pour un essai. Le code de ce garde est **repris mot pour mot de MEYTRE**, que l'utilisateur fait tourner depuis deux jours.
- ⚠ **Découvert au passage** : Prisma charge `prisma7.config.ts` (notre fichier, présent depuis le commit initial) **et non** `prisma.config.ts` (celui de Xavier). Les deux existent sur `main` — la duplication **préexiste à la fusion**, je n'y ai pas touché. Ils déclarent le même schéma et la même URL, donc le comportement est identique aujourd'hui, mais **lequel gagne n'est pas évident** : à trancher avec Xavier.

### État des dépôts en fin de séance
- **`main` POUSSÉ** sur `origin` (`e3e2acc..ff1c63a`) — décision de l'utilisateur. `prod` n'a pas été touchée, **aucun déploiement automatique n'a été déclenché**. Point de retour conservé : tag **`avant-fusion-MEYTRE`** (= `e3e2acc`, l'état de `main` avant fusion).
- `D:\CECPC\PLEIADE\eho` — branche `main`, à jour avec `origin/main`.
- `C:\CECPC\PLEIADE\eho` (clone d'exécution) — **basculé de `MEYTRE` sur `main`** à la demande de l'utilisateur. Le travail y est désormais fait sur une base qui contient **aussi le durcissement de Xavier**.
  - ⚠ **Vérifié AVANT de toucher à quoi que ce soit** : le travail vivant non commité y était **identique au commit `15d8b25`** (`diff -r` sur `src/`, `prisma/`, `scripts/`, `package.json` — seul `src/generated`, ignoré par git, différait). Rien ne pouvait être perdu.
  - **Filet conservé** : `stash@{0}` — « etat MEYTRE avant bascule sur main (2026-09-16) ». À supprimer quand l'utilisateur le décidera (`git stash drop`).
  - `npm install` (ajout de `dotenv` par `main`) + `prisma generate` refaits ; **aucun `db push`** — le schéma de `main` est identique à celui de `MEYTRE`, la base était déjà en phase.
  - Serveur de dev **relancé sur 3001**, gardes vérifiés en anonyme : `/mon-eho`, `/graphe`, `/trombinoscope`, `/planche-officielle` → **307** ; `/api/users`, `/api/avatars/export` → **401**.

### Dans la foulée — l'utilisateur réaligne `MEYTRE` sur `main` (vérifié)
Pour repartir d'une base commune et commiter proprement ses prochains travaux, l'utilisateur a reporté `main` dans `MEYTRE` et poussé. **Contrôlé** : `origin/MEYTRE` et `origin/main` sont au **même commit `ff1c63a`** et au **même arbre** (`ecfa6a6`) — `0` commit d'écart **dans les deux sens**. `prod` n'a pas bougé (`e3e2acc`).
- ⚠ **Une seule chose n'était pas en ordre, en local** : le clone d'exécution `C:` était resté sur `main`, et sa branche **`MEYTRE` locale traînait 10 commits en arrière**. Commiter là-dessus aurait **reconstruit une divergence** dès le premier travail. Remis d'aplomb (`checkout MEYTRE` + `merge --ff-only`) : comme l'arbre est identique à celui de `main`, **aucun fichier n'a bougé** et le serveur de dev n'a pas bronché (`/login` 200, `/mon-eho` 307, `/api/users` 401).
- **Les deux clones sont maintenant sur `MEYTRE`**, propres, à jour, base strictement identique à `main`.
- Le filet `stash@{0}` de C: est devenu **redondant** (l'état qu'il conserve est entièrement contenu dans `ff1c63a`) — conservé tant que l'utilisateur ne dit pas de le supprimer.

### Suppression de l'onglet « Choix d'avatar » (section joueur)
**Question de l'utilisateur** : « à quoi sert l'onglet *Choix d'avatar* dans la partie joueur ? » — puis, à la lecture de la réponse : « supprime-le, il ne convient plus aux décisions qu'on a prises aujourd'hui ».

**Ce que la lecture du code a montré** :
- La page annonçait « Sélectionnez votre personnage » mais **ne sélectionnait rien** : aucun `onClick` sur les cartes, aucun `POST`, aucune persistance. Les seuls boutons actifs étaient les filtres par groupe.
- `git log --follow` : elle date du **commit initial** `a071eed` — vestige de l'échafaudage d'origine, quand **un avatar était un compte Keycloak**. La prémisse est morte avec `0720ab1` (« fin du lien avatar/Keycloak ») ; l'écran, lui, était resté. Même famille que les 20 avatars de démonstration supprimés le 2026-09-14.
- ⚠ **Elle contredisait frontalement la règle n°1 du jeu.** `lib/eho-joueur.ts` dit : « le dépouillement est la règle : hors STARTEX, un joueur ne doit RIEN savoir d'officiel ». Or la page appelait `/api/users` en simple joueur connecté et **affichait la bio et les groupes** des 453 avatars (le reste de la ligne `User` étant dans la réponse réseau). **`Mon EHO` cachait ce que `Choix d'avatar` distribuait, dans le même menu, au même joueur.**

**Fait** : entrée retirée de `components/Sidebar.tsx` (menu JOUEUR = `Mon EHO` · `EHO GT` · `Planche relationnelle`), page `(player)/avatars/page.tsx` **effacée**, commentaire d'en-tête du Sidebar corrigé et daté. Aucune autre référence dans le code (`grep` sur `"/avatars"` : la ligne du menu était la seule).
**Vérifié** : `tsc` **0 erreur** · `eslint` **0 erreur** (l'avertissement `<img>` disparaît, il venait de cette page) · `npm run test` **71/71** · `/avatars` renvoie **404** sur le serveur de dev, `/login` toujours 200.
**⭐ Effet de bord utile** : cette page était **le seul écran joueur à consommer `/api/users`** — c'est elle qui bloquait la réduction de charge utile réclamée depuis le 2026-09-14. **Le verrou a sauté.**

#### 🔎 Défaut trouvé au passage — `npm run test:bio` mentait depuis la fusion (CORRIGÉ le jour même)
**Le défaut** : `scripts/test-bio.mts` lisait les vraies bios via `fetch("http://localhost:3001/api/users")` **sans session**. Depuis que la route est gardée, il recevait **401**, tombait dans sa branche `!reponse?.ok`, annonçait « **serveur injoignable sur :3001** » — **faux : le serveur avait répondu, il avait refusé** — puis passait de **538 contrôles à 13** en affichant toujours « **TOUT PASSE** », code de sortie **0**.
⚠ Exactement le travers que le projet s'interdit : « un échec de lecture ne doit jamais être présenté comme un résultat valide » · « contrôler le code HTTP dans tout script d'essai ». `!reponse?.ok` confondait **trois** situations : serveur éteint, serveur qui refuse (401/403), serveur qui plante (500).

**Le correctif retenu — supprimer la cause, pas le symptôme** : le script **lit désormais les bios DIRECTEMENT en base** (`PrismaClient` + `PrismaMariaDb`, helper `urlBase()` repris tel quel de `backfill-curseur.mts`). ⭐ **La couche HTTP n'a jamais été le sujet** : ce qu'on éprouve, c'est le découpage d'un texte. En allant à la source, **la question de l'autorisation disparaît**, et le script ne dépend plus du tout du serveur de dev.
**Et le diagnostic devient honnête** :
- échec de lecture → message qui **nomme la cause réelle** (l'enrobage Prisma — ligne vide, « Invalid `prisma.x.y()` invocation: », extrait de code annoté — est écarté pour garder la ligne qui renseigne, tronquée à 110 caractères) ;
- ⭐ **un contrôle sauté n'est plus un contrôle réussi** : la conclusion affiche « **INCOMPLET** » au lieu de « TOUT PASSE » et le script **sort en code 1**, avec le remède à faire (`docker compose up -d eho-db`) ;
- une base **vide** est également traitée comme incomplet — il n'y avait rien à éprouver, ce n'est pas un succès.
- ⚠ Piège évité de justesse : `e.message.split("\n")[0]` donnait « base inaccessible **()** » — un motif vide, soit le défaut qu'on corrigeait, en plus petit.

**Vérifié sur les trois chemins** : cas normal **538/538**, code 0 (mêmes chiffres qu'avant la fusion : 262 bios, 57 fiches structurées, 59/59 aérées) · base éteinte → INCOMPLET, code **1** · mauvais mot de passe → INCOMPLET, code **1**. `tsc` et `eslint` 0 erreur, `npm run test` 71/71.

### 🗑️ Consolidation sur `C:` — le doublon `D:\CECPC\PLEIADE` supprimé
**Question de l'utilisateur** : « on ne peut pas tout synchroniser sur le C: plutôt que de l'avoir sur D: ? Car le D: apparemment ne sert à rien. »

**Ce que l'inventaire a montré — c'était déjà fait à 95 %, sans que personne le sache** :
| | `C:\CECPC\pleiade` | `D:\CECPC\PLEIADE` |
|---|---|---|
| `eho` | MEYTRE, nos commits du jour | ff1c63a, figé |
| `mastorion` | branche `fix/keycloak-issuer-public-url` | `main`, figé au 11/09 |
| `pleiade-platform` | 2 fichiers en cours | figé au 11/09 |
| `pleiade-infra` | ✅ **présent** | ❌ absent |
| `dev/` (up/down.ps1, seeds, bootstrap KC) | ✅ | ❌ |

- ⭐ **Deux faits périmés corrigés au passage** : `pleiade-infra` **EST cloné** (la mémoire le disait absent depuis le 2026-09-11) ; et le dossier **`dev/`** — scripts d'environnement local **non versionnés**, donc présents nulle part ailleurs — n'était documenté nulle part. Il l'est désormais.
- ⚠⚠ **La vraie raison, à ne jamais redécouvrir** : **D: est formaté en exFAT → aucun binaire natif ne s'y exécute** (`npm`, `next build`, `prisma generate`). Un dépôt de code sur D: **ne peut ni se construire, ni se lancer, ni se tester** : c'est une archive morte qui ne peut que vieillir. C: est en NTFS.
- **Vérifié avant suppression** (pas seulement la branche courante) : sur les 3 dépôts D:, **0 commit non poussé toutes branches confondues**, **0 remise (stash)**, toutes les branches locales contenues dans `origin`, **aucun `.env` ni dossier `data/`** — uniquement `src/generated` et `tsbuildinfo`, régénérables. Le tag de retour `avant-fusion-MEYTRE` a été confirmé **présent sur C:** avant d'effacer.
- **Fait** : `D:\CECPC\PLEIADE` supprimé, **0,8 Go libérés**.
- ⭐ **Fin de la doctrine « clone d'exécution + copie de référence »**. Elle entretenait deux vérités qui divergeaient — le matin même, la `MEYTRE` locale de C: traînait 10 commits en arrière. Désormais : **une seule copie de travail, sur C:, GitHub fait foi.**
- ✅ **`D:\CECPC\PRODUCTION` n'est PAS concerné** (17,9 Go : MINERVE, EXER, BDA, CREATION, DOC REF). Ce sont des **documents**, pas du code : exFAT ne les gêne pas, et les déplacer casserait les chemins de `CLAUDE.md`, les hooks et les permissions `.claude`. La distinction a été posée explicitement à l'utilisateur avant d'agir.

**Documentation rebasculée sur `C:\CECPC\pleiade`** : `CLAUDE.md` (table des chemins permanents + registre des agents MASTORION/PLEIADE, avec une note expliquant **pourquoi** C: et pas D:), `SYSTEME\ROUTAGE.md`, `SYSTEME\PROMPTS\pleiade.md`, `SYSTEME\PROMPTS\mastorion.md`, `PLEIADE\MEMOIRE.md`, `PLEIADE\README.md`, `PLEIADE\REFERENCES\README.md`, `MASTORION\MEMOIRE.md`, `MASTORION\README.md`, `NOYAU\MEMOIRE.md`, `vault\decisions\DECISION-014.md` (consigne permanente, `updated` bumpé).
- Les `JOURNAL.md` et `vault\daily\` **gardent leurs mentions de D:** — c'est de l'historique, on ne le réécrit pas.
- `.claude\settings.local.json` : **aucune permission** ne référençait ce chemin, rien à faire.
- ⚠ Le dossier réel s'écrit en **minuscules** : `C:\CECPC\pleiade`.
- **Vault revalidé** : 449 notes, 0 erreur bloquante (l'avertissement `bios.js` est antérieur et sans rapport).

### ⭐ Le curseur d'alignement ouvert sur les autorités STARTEX — suivre une ATTITUDE, pas deviner une identité
**Constat utilisateur** (vue joueur, compte `joueur_test`) : « quand je clique sur une card qui est en startex package, il m'est impossible d'avoir le même rendu qu'une card qui n'est pas dans le startex package ; ce qui m'intéresserait c'est d'avoir le curseur du camp estimé, car selon les actions que vont mener les joueurs sur le terrain et réseaux sociaux, un avatar va mal réagir ou bien réagir — il faudrait que les joueurs puissent modifier la position de ce curseur pour **un maire** par exemple ».

#### ⭐ La clé : ce n'est pas la même question
Ce n'est **pas** un relâchement du dépouillement, c'est une **autre question posée au même widget** :
| Carte | Question | Départ | Écart ? |
|---|---|---|---|
| Avatar inconnu | « **qui est-il ?** » — identification | « je ne me prononce pas » | **oui** |
| Autorité STARTEX | « **où en est-il avec nous ?** » — attitude | **la position officielle** | **jamais** |

Sur une autorité connue, la première question n'a pas lieu d'être : le countrybook y a répondu. La seconde, elle, **bouge avec l'exercice**.

#### Fait
- **Serveur** (`PUT /api/eho/mon-eho/[avatarId]`) : le verrou STARTEX portait sur *« les champs de rangement »* ; il porte désormais explicitement sur l'**IDENTITÉ** — `paysEstime` et `fonctionEstimee` restent ignorés, le **curseur passe**. Un **seul chemin d'écriture** pour le curseur, commun aux deux cas : la validation ne vaut jamais « ici mais pas là ».
- **`components/curseur-camp.tsx`** : `CurseurCamp` gagne `titre`, `aide` et surtout **`officiel`** — un **repère noir fixe** sur la piste, motif repris de `JaugeCamp` côté animateur. ⚠ `pointer-events-none` dessus : un trait qui intercepterait le clic empêcherait de saisir la poignée juste à cet endroit. Avec un repère, le bouton devient « **Revenir à la position officielle** » — « je ne me prononce pas » n'a plus de sens quand on connaît le départ.
- **`components/planche.tsx`** : le curseur apparaît dans l'encadré ambre de la fiche STARTEX, sous la bio, titré « **Alignement observé — évolue avec vos actions** ». ⭐ Il **part de la position officielle** (`curseurDepuisCamp(campOfficiel)`), pas de zéro : **sans point de départ, il n'y a pas de dérive à lire**. La carte de la planche suit l'alignement **observé** dès qu'il existe — un maire qui bascule doit se voir sur la planche, pas au fond de sa fiche.

#### Vérifié en conditions réelles (jeton Keycloak de `joueur_test`, pas une simulation)
- `PUT` d'un curseur à **+40** sur une autorité STARTEX bleue → accepté, `campEstime` **déduit côté serveur** à `rouge`, `campOfficiel` **inchangé** (`bleu`).
- ⭐ **Le dépouillement tient** : le même appel tentait de forcer `paysEstime: "Mercure"` et `fonctionEstimee: "espion infiltré"` → **les deux écartés**, seul le curseur a pris.
- **Aucun faux écart** : la comparaison animateur rend `"ecarts": null` sur cette ligne, tout en affichant les deux positions côte à côte (officiel −70 / observé +40). C'est de la matière d'animation, pas une faute.
- `tsc` 0 erreur · `eslint` 0 erreur · `npm run test` 71/71 · `test:bio` 538/538 · le serveur de dev recompile et sert `/mon-eho` en 200.
- ⚠ **Essai mené sur la planche VIVANTE de `joueur_test`** (celle que l'utilisateur avait sous les yeux), donc selon la règle du 2026-09-15 : cible **vierge** choisie exprès, état **lu avant**, **restauré après**, et la **ligne `eho_lectures` créée par l'essai supprimée** (suppression gardée par une condition sur chacun de ses champs). Zéro trace.

### ⭐⭐ Les 11 dépôts de `cecpc-pleiade` clonés et compris — l'agent PLEIADE remis à niveau
**Demande utilisateur** : cloner tous les dépôts de `github.com/cecpc-pleiade` dans `C:\CECPC\pleiade`, **lire leurs `.md` pour comprendre qui fait quoi**, et mettre à jour l'agent PLEIADE en conséquence. ⚠ Consigne expresse : *« le répertoire EHO doit exactement correspondre à l'EHO sur lequel on travaillait — assure-toi que rien n'est supprimé »*.

- **L'organisation compte 11 dépôts, le poste n'en avait que 4.** Les 7 manquants sont tous des **applications du catalogue** : `app-admin`, `app-cockpit`, `app-messagerie`, `app-press`, `app-social`, `app-webserver`, `app-wordpress`. Clonés. ⭐ **Règle découverte : 1 app du catalogue = 1 dépôt** (correspondance 1:1 vérifiée avec `pleiade-platform/catalog/*.yml`).
- ⚠ **Dépôts privés** : l'API anonyme rend une liste vide. Énumérés avec les identifiants **déjà enregistrés sur le poste** (`git credential fill`), jamais affichés.
- ✅ **`eho` garanti intact** : je n'y ai pas touché. Vérifié avant et après — même branche `MEYTRE`, mêmes **3 fichiers modifiés** (le travail sur le curseur), rien de perdu. L'utilisateur avait poussé entre-temps : `origin/main` **et** `origin/MEYTRE` sont sur `f8ba88a`, donc GitHub = notre local, **au travail en cours près**.

#### ⭐⭐ Ce que la lecture des documents a révélé — deux faits que la mémoire ignorait
1. **Le renommage du réseau social a EU LIEU.** `app-social` contient **tout `mastorion` plus 19 commits** (même commit initial `b7c6332`), dont « *Devenir social : renommage et mise en production automatique* ». Le point ouvert « nouveau nom du réseau social » est **tranché** : c'est **`social`**. Le clone `mastorion` est un **ancêtre figé**.
2. ⭐ **L'admin embarquée dans mastorion a été DÉMANTELÉE** (commits « Retirer l'administration et le cockpit embarqués », « Retirer la gestion des comptes… ») et répartie : **comptes → `eho`** · **scénarios → `app-admin`** · **veille → `app-cockpit`** · **rôles → Keycloak**. Il ne reste au social **qu'un seul rôle, `animateur`**, et **lecture seule sans lui**.
   👉 **Conséquence directe pour nous : `eho` n'est pas une app parmi d'autres, c'est la source d'identité de toute la zone.** Notre chantier est la pierre angulaire.

#### Les 4 mécanismes d'une zone, désormais écrits dans la mémoire (§6bis)
1. **L'identité est UNE** : `identity_id` = UUID eho = `sub` Keycloak, **le même sur toutes les apps**. Une app ne stocke pas de comptes — `app-press` compose sa rédaction en **cochant des groupes eho**. ⚠ Un persona a un `user.id` **différent dans chaque instance** sociale : seul `identity_id` fait le pont, et **sans lui aucune vue transverse n'existe**.
2. **Découverte à l'exécution**, jamais en dur : `GET {PLEIADE_URL}/api/internal/zones/{zone}/instances`, rafraîchi 30 s, **dernière liste conservée si l'orchestrateur tombe**. Une app ajoutée à une zone est vue **sans redéploiement**.
3. **Clé de service `X-API-Key`** (clé de zone) pour l'app-à-app — ⭐ *parce que personne n'est en ligne quand le scheduler publie à T+37 min* ; la session de l'opérateur ne sert qu'à **signer le journal**. Une app compromise ne voit que sa zone.
4. **Contrat `/api/service/*` identique** sur social, presse et messagerie → `app-admin` **vise n'importe quelle app sans rien savoir d'elle**. ⚠ Un item cible **une instance**, jamais un type de réseau (*« s'il y a trois YouTube, ce sont trois cibles »*), et un message de scénario doit être **indiscernable** d'un message de joueur (`source="scenario"` n'apparaît qu'en supervision).

**Aussi consigné** : les leçons du BFF cockpit (pas de CORS, ids désambiguïsés `{instance}:{id}`, curseur par réseau, une instance en panne n'en fait pas échouer d'autres), le **design system Pléiade** (`pleiade-theme.css` = copie conforme, **ne jamais l'éditer sur place**), et les **conventions de code des apps** (texte FR accentué / commentaires FR sans accents expliquant le *pourquoi* ; jamais de `prompt`/`confirm`/`alert` ; polices auto-hébergées *« un exercice tourne sur réseau fermé, rien ne sort »*).

**Fichiers mis à jour** : `PLEIADE\MEMOIRE.md` (§1 renommage achevé, §2 les 11 dépôts, §6 catalogue↔dépôts↔rôles, **§6bis nouveau**, §7 recadré, points ouverts), `CLAUDE.md` (chemins + registre MASTORION/PLEIADE), `SYSTEME\PROMPTS\pleiade.md` (table des dépôts + les 4 mécanismes), `SYSTEME\PROMPTS\mastorion.md`, `SYSTEME\ROUTAGE.md`, `PLEIADE\README.md`, `MASTORION\README.md` + `MASTORION\MEMOIRE.md`.

- ⚠ **Incident d'outillage, corrigé** : une substitution Python a interprété `\a` de `…\app-social` comme le caractère **BEL** (0x07), écrivant `pleiade<BEL>pp-social` dans `CLAUDE.md`. Détecté par un balayage des caractères de contrôle sur tous les `.md`, réparé, **plus aucun caractère parasite**. 👉 **Règle : ne jamais écrire un chemin Windows en littéral dans un script de substitution** — composer l'antislash (`chr(92)`), ou passer par l'outil d'édition.
- 🔎 **Trouvé au passage, non corrigé** : `DELATTRE\MEMOIRE.md` contient un caractère de contrôle **0x01** — antérieur à cette séance, signalé à l'utilisateur.

#### ⭐⭐ Dans la foulée — le modèle de branches enfin écrit (§2bis)
**Question de l'utilisateur** : *« as-tu compris que `main` est la branche principale où l'on importe nos travaux depuis une branche provisoire, et que `prod` est reliée au serveur où tourne réellement PLEIADE ? ça devrait être écrit dans un des .md »*.

**Vérifié dans les workflows plutôt qu'acquiescé — et il avait raison sur les deux points** :
- Le modèle est **exact** : `.github/workflows/deployer-prod.yml` se déclenche sur `push: branches: [prod]`, sur un **runner auto-hébergé sur le serveur d'exercice**, et **promeut la version sur les zones de production**. L'en-tête du workflow d'`eho` l'énonce mot pour mot : *« Le geste de déploiement, c'est de pousser sur `prod` — jamais sur `main`. […] une app cassée se voit en salle, pas seulement par nous. »*
- ⚠ **Et ce n'était écrit dans AUCUN `.md`** — uniquement dans les en-têtes de workflow. C'est désormais **§2bis de la mémoire**, la **règle 2bis** des règles de travail, et le **prompt de l'agent**.

**⚠ Deux nuances trouvées en vérifiant dépôt par dépôt, que le modèle général ne dit pas** :
1. ⚠⚠ **`pleiade-platform` n'a pas de branche `prod`** : son workflow se déclenche sur **`main`** — **y pousser déploie immédiatement**, sans sas (seul garde-fou : `paths-ignore: '**.md'`). Le workflow d'`eho` assume l'asymétrie : *« le sas se justifie ici bien plus que pour l'orchestrateur »*.
2. **`pleiade-infra`, `app-webserver`, `app-wordpress`** n'ont ni `prod` ni workflow de déploiement.

**Aussi retenu** : la promotion **ne touche QUE les instances de l'app concernée** — *« une correction urgente ne doit pas couper les autres apps d'un exercice en cours »* — et le `concurrency` fait **attendre** un second déploiement **sans annuler le premier**, un déploiement interrompu laissant la pile dans un état bâtard.

---

## 2026-09-15 — EHO PLEIADE : groupes de travail, verrous, versement granulaire, planche relationnelle (branche `MEYTRE`)

**Demande utilisateur, en cinq temps** : (1) affilier un joueur à un **groupe de travail** et lui donner, en plus de « Mon EHO », un **« EHO GT »** commun où le groupe travaille ensemble ; (2) **avertir et bloquer** quand une carte est déjà ouverte par quelqu'un d'autre ; (3) pouvoir **importer** l'EHO GT dans son EHO personnel ; (4) **verser** l'inverse — une carte, une rubrique ou un pays — par une **icône**, avec **retour arrière** ; (5) une **planche relationnelle** en onglet séparé, inspirée de *Board* d'Adobe : poser des cartes, tirer des liens, canevas infini.

### Groupes de travail — la convention qui tient tout
- Les groupes de travail sont les **sous-groupes du groupe Keycloak `GT`** (chemin `/GT/<nom>`). Rien d'autre n'est un GT. Cette convention évite d'ajouter une table et de dupliquer une appartenance qui existe déjà dans Keycloak.
- ⚠ **Les groupes ne sont PAS dans le jeton** : ils sont résolus **côté serveur** par l'API d'administration Keycloak (`lib/keycloak-admin.ts` → `groupesDeTravail(sub)`).
- ⚠ **`groupesDeTravail` renvoie `null` en cas d'échec, jamais `[]`** — application directe de la leçon du 2026-09-14 : « un échec de lecture n'est pas un résultat valide ». `lib/porteur.ts` traduit `null` en **503**, et un non-membre en **403**. Sans cela, une panne Keycloak aurait ouvert tous les GT à tout le monde.
- Un **porteur** (`playerId` ou `gt:<id>`) paramètre désormais toutes les routes EHO : `components/planche.tsx` est la **même planche** pour « Mon EHO » et « EHO GT », un `?gt=` près.

### Concurrence — verrou par carte, pas par écran
- `eho_verrous` : un verrou **par carte et par porteur**, avec **TTL** et battement de cœur. Ouvrir une carte déjà ouverte affiche **qui** la tient et **bloque la saisie** — le lecteur voit tout, n'écrit rien.
- Portée volontairement limitée : le verrou protège la **fiche**, pas le rangement. Deux joueurs peuvent réordonner en même temps sans se gêner.

### Versement `Mon EHO` → `EHO GT` (et retour)
- **Icône unique** (jamais de bouton texte), reprise à l'identique dans le bouton d'import : le geste se reconnaît avant de se lire.
- Trois grains : **carte** (le bouton vit *dans* la fiche), **rubrique**, **pays**.
- ⚠ **Deux listes, pas une** : `aVerser` (les cartes qui ont une lecture à copier) et `aPlacer` (toutes les cartes demandées). Symptôme corrigé : *Ribiki restait dans « sans rubrique »* — il n'avait pas de lecture, donc il n'était ni versé **ni placé**.
- ⚠ **`parRubrique: [{nom, ids}]`** et non une liste plate : verser un **pays** avec une seule rubrique cible **écrasait toutes les rubriques** du GT. Symptôme constaté par l'utilisateur, réparé **avec son propre bouton d'annulation**.
- **Annulation** (`verser-gt/annuler`) : restaure l'instantané `eho_versements`, mais **épargne** les cartes qu'un tiers a modifiées depuis (`modifiePar` différent) ou qui sont verrouillées ; la disposition n'est restaurée que **si rien n'a été épargné**. Annuler ne doit jamais détruire le travail d'un autre.
- L'**import GT → personnel** écrit d'abord une **sauvegarde restaurable** (`eho_sauvegardes`).

### ⭐ Planche relationnelle (`(player)/graphe`) — nouveau concept
- **Bibliothèque retenue : `@xyflow/react` (React Flow) 12.11.6** — MIT, **3 dépendances**, canevas infini, zoom, nœuds et liens sur mesure. Proposée puis validée par l'utilisateur.
- Persistance : **un seul modèle**, `eho_graphes` (une ligne JSON par porteur). Assainissement côté serveur : 600 nœuds, 2 000 liens, coordonnées bornées, couleurs `#RRGGBB`, **auto-liens refusés**, liens vers un nœud absent supprimés.
- **Gestes construits sur demande, dans l'ordre** : lien cliquable pour être supprimé → auto-lien interdit → **libellé éditable** → **geste d'étirement/rupture** (clic maintenu, le trait s'étire et **casse**, à la manière de ComfyUI) → suppression des pointes de flèche → **barre d'inspection en pied de planche** (couleur, texte, supprimer) plutôt que des pastilles sur le tracé → **libellé posé AU-DESSUS du trait et orienté comme lui** (`<textPath>` sur un rail inversé, halo `paintOrder="stroke"`).
- ⚠ **Les liens ne se connectaient pas** : toutes les accroches étaient `type="source"`. Correctif : une accroche **cible + source** par côté, plus `ConnectionMode.Loose`.
- **Point de jonction** (« connecteur ») : un **lien ne peut pas être la cible d'un autre lien**. Pour rattacher une troisième carte à une relation, il faut un point matériel. Deux apparences :
  - **sans nom**, une pastille de 16 px — les accroches se confondent avec elle, il n'y a rien à viser ;
  - **avec un nom**, un **rectangle blanc bordé de sa couleur, à l'image des cartes**, le texte à l'intérieur *(demande du 2026-09-15)*.
  - ⚠ **Deux pièges à ne pas réintroduire** : (1) mettre le texte **dans** une pastille agrandit la boîte et React Flow **repousse les accroches très loin** du point — d'où le nom hors flux pour la pastille, et le rectangle qui *est* la boîte pour la version nommée ; (2) une accroche qui **recouvre** le nœud capte l'appui et le rend **impossible à déplacer** — d'où quatre accroches de bord (`j-<côté>` / `s-j-<côté>`).
  - Les liens partant d'une jonction sont **rectilignes** (`getStraightPath`) et non courbes : ils filent **droit vers la carte**, dans sa direction réelle.
- ↩️ **Revenu en arrière à la demande de l'utilisateur** : la disparition automatique d'une jonction tombée sous 3 liens a été **annulée** (« remet la version d'avant c'était bien »).

### Accroches invisibles au repos (demande de fin de séance)
- **Constat utilisateur** : « je trouve ça hyper moche, j'aimerai qu'on ne les voit pas, et que quand on place la souris sur le bord d'une card le connecteur apparaisse ». Les points de départ étaient en effet **visibles en permanence** (`opacity-60`), soit quatre pastilles indigo par carte.
- **Livré** : un composant unique **`Accroches`** (cartes *et* jonctions — un seul geste à apprendre) + un bloc CSS dans `globals.css`. Rien au repos ; les points se posent **au survol du nœud**, grossissent au survol d'une accroche précise, et **tout le plan les montre en retrait pendant qu'un lien est tracé** (pour désigner les arrivées possibles).
- **Teinte du camp** : la pastille reprend la couleur de la carte — le point qu'on tire annonce déjà de qui part la relation.
- ⚠ **La zone de préhension n'est pas le dessin** : boîte de 18 px pour une pastille de 10 px — on attrape un bord, on ne vise pas un point. La jonction **nue** garde des accroches de 10 px : plus grandes, elles recouvriraient ses 16 px et la rendraient indéplaçable (React Flow pose `nodrag` sur chaque accroche). Elle signale le survol par une **auréole**, pas par des pastilles : elle **est** son propre point d'accroche.
- ⚠ **`useConnection` doit être appelé AVEC un sélecteur** (`(c) => c.inProgress`) : sans lui, le composant se redessine à chaque pixel parcouru pendant tout le tracé.
- **Identifiants d'accroche inchangés** (`<côté>` / `s-<côté>`, `j-<côté>` / `s-j-<côté>`) — les plans déjà enregistrés continuent de se recharger (vérifié : 5 nœuds / 5 liens intacts).

### Menu du plan — ajouter là où l'on clique (⭐ registre extensible)
- **Demande** : « quand on clique sur la planche, un clic gauche, on a les options possibles de création qui s'affichent » — en commençant par « Point de jonction », **le bouton de la réserve étant supprimé**. L'utilisateur annonce qu'il **en demandera d'autres**.
- **Livré** : un **registre `MODULES`** dans `components/graphe.tsx` — une entrée `{cle, nom, aide, apercu, creer}` = un module de plus dans le menu, **sans toucher au menu ni au plan**. `creer` reçoit le point cliqué et rend un nœud **centré** dessus (React Flow positionne par le coin haut-gauche : au module de retrancher sa demi-taille, lui seul sait ce qu'il mesure).
- **Pourquoi c'est mieux qu'un bouton** : le bouton posait toujours au centre de l'écran, il fallait ensuite traîner le module au bon endroit. Le clic **désigne le point ET ouvre le choix** — un geste au lieu de deux.
- ⚠ **Un clic sur le fond sert d'abord à REFERMER** : si une barre d'édition est ouverte, le premier clic ne fait que désélectionner, c'est le suivant qui ouvre le menu. Sans cette règle, fermer une barre faisait surgir un panneau.
- ⚠ **Le navigateur émet un `click` même après un glissement** (appui et relâchement sur le même élément) : sans mesure, **chaque panoramique** se terminait par l'ouverture du menu à l'endroit lâché. Corrigé en mémorisant le point d'appui (`onPointerDownCapture`) et en ignorant tout clic ayant parcouru plus de 4 px. React Flow, lui, neutralise déjà le clic qui suit un lien lâché dans le vide.

### Encadrés — une mini-planche dans la planche
- **Demande** : « un encadré / une rubrique où on pourrait placer les cards dedans… faire comprendre visuellement que ces personnes font partie d'un même groupe », **sans empêcher** de relier une carte du dedans à une carte du dehors ou d'un autre encadré. Accessible par le **menu du plan**.
- **Choix de conception** : un vrai **contenant**, pas un rectangle décoratif — une carte lâchée dedans lui **appartient** (`parentId` de React Flow), donc déplacer l'encadré emporte son contenu. Redimensionnable (`NodeResizer`), titré, coloré par la même barre du bas que la jonction.
- **C'est le CENTRE de la carte qui décide** du rattachement, pas un chevauchement : une carte à cheval sur un bord serait sinon happée alors qu'elle est visiblement dehors.
- ⚠ **Les coordonnées d'un nœud rattaché sont RELATIVES à son encadré** (convention React Flow) — conversion dans les deux sens au rattachement/détachement, et à l'enregistrement. Sans elle, la carte saute à l'autre bout du plan.
- ⚠ **React Flow exige que le parent PRÉCÈDE ses enfants** dans la liste des nœuds → `trierNoeuds` (tri stable : les encadrés d'abord, donc rendus **derrière** les cartes libres).
- ⚠⚠ **Supprimer un encadré ne doit PAS supprimer son contenu.** React Flow, laissé à lui-même, emporte les enfants avec le parent — on perdrait d'un coup toutes les cartes rangées dedans. Traité dans `onBeforeDelete` : on détache, on retire le seul encadré, et on répond `false` pour qu'il ne rejoue pas la suppression.
- ⚠ **Un `parent` introuvable détache le nœud** côté serveur au lieu de le garder : React Flow le positionnerait relativement à un parent inexistant et la carte **disparaîtrait de l'écran**. *Perdre un rangement est réparable ; perdre une carte de vue ne l'est pas.*
- **Barre du bas généralisée** : `BarreConnecteur` → **`BarreNoeud`** (marque, titre, invite, aide paramétrés) — jonction et encadré partagent la même, au même endroit.
- **Serveur** : `assainir` accepte `groupe`, `largeur`/`hauteur` (bornées 140–8000) et `parent`. **Aller-retour vérifié** : titre, couleur, taille et appartenance restitués ; `parent` fantôme détaché ; taille 10×99999 ramenée à 140×8000.
- 🔴 **Incident de la séance** : mon plan d'essai a été envoyé sur la planche de `joueur_test` **pendant que l'utilisateur travaillait dessus** → son plan a été écrasé (`eho_graphes` = une ligne par porteur, **sans historique**). Reconstruit au plus près (jonction « conseil » + 3 avatars + 3 liens), positions approximatives. **Règle : ne jamais écrire sur la planche d'un porteur vivant — créer un porteur d'essai dédié.**

### Transfert d'un encadré entre planches relationnelles (`POST /api/eho/graphe/transferer`)
- **Demande** : verser un encadré **avec toutes ses cartes** vers la planche relationnelle du GT, et **inversement** rapatrier un encadré du GT dans sa planche personnelle « pour y apporter des modifications perso ».
- **Le sens est donné par l'endroit**, jamais par un réglage : sur ma planche le bouton verse vers un GT (`vers-gt`), sur celle d'un groupe il rapatrie chez moi (`depuis-gt`). Même icône que le versement de l'EHO (`ICONE_TRANSFERT`), **retournée** selon le sens.
- ⭐ **Ce transfert n'efface JAMAIS rien chez le destinataire** : il n'ajoute ou ne remplace que l'encadré visé, son contenu et les liens **dont les deux bouts sont dedans**. C'est ce qui le rend sûr sur une planche partagée — et **c'est pourquoi il n'a pas de bouton « annuler »**, contrairement au versement de l'EHO : il n'y a rien à restaurer. **Vérifié** : un nœud et un lien préexistants du GT ont survécu au versement.
- **Les identifiants sont conservés** → reverser deux fois **met à jour** au lieu de dupliquer, et le rapatriement reconnaît l'encadré (essai : `remplaces: 5`, planche personnelle intacte — 2 encadrés, 6 avatars, 2 jonctions, 6 liens).
- **Un lien vers l'extérieur ne suit pas** : il désignerait une carte que le destinataire n'a peut-être pas, et emporterait au passage des cartes que personne n'a demandées.
- **Refus vérifiés** : sans `?gt=` → 400 · encadré inconnu (ou nœud qui n'est pas un encadré) → 404 · GT dont on n'est pas membre → 403 · sens invalide → 400 · sans session → 401.
- **Barre du bas** : `BarreNoeud` reçoit un emplacement `extra` — les actions propres à un genre de nœud s'y posent sans polluer la barre générique.

### ⭐ Planche relationnelle OFFICIELLE (animation), enregistrée avec le modèle d'EHO
- **Demande** : « il faut forcément qu'on ait la planche relationnelle officielle dans la vue admin […] liée et enregistrée au modèle d'EHO utilisé ». Un PDF de relations entre avatars sera fourni pour la remplir.
- **Porteur `officiel`** (`lib/porteur.ts`, id réservé `PORTEUR_OFFICIEL = "officiel"`) : troisième nature à côté de `joueur` et `gt`. Aucune collision possible — les `sub` Keycloak sont des UUID. **Réservé aux animateurs, vérifié côté serveur** ; `?officiel=1` sur une route d'un non-admin → **403**. Tout l'existant (GET/PUT, historique/versions) marche sans modification.
- ⭐ **Les cartes n'y sont PAS dépouillées** : `composerCarte(..., { officiel })` révèle pays, camp, fonction et bio pour tous, pas seulement les STARTEX. C'est la seule vue où l'on regarde la vérité. Le drapeau est **déduit du porteur déjà vérifié**, jamais réclamé par le client. **Vérifié** : 381 cartes hors STARTEX renseignées côté animation, **0 fuite** côté joueur.
- ⭐ **La planche voyage avec le modèle** (`Payload.graphe` dans `lib/eho-templates.ts`) : ses nœuds portent les identifiants des avatars, elle n'a de sens qu'avec la population qui va avec. **Vérifié de bout en bout** : capture d'un modèle → `payload.json` contient `graphe` (4 nœuds, 2 liens) ; planche vidée → application du modèle → planche restituée à l'identique.
- ⚠ **Absent ≠ vide** : un modèle capturé avant cette fonctionnalité (SKOLKAN) n'a pas la clé `graphe` → l'appliquer **laisse la planche en place** au lieu de l'effacer (vérifié). Le modèle **VIERGE** porte une planche vide **explicite** : lui, il efface — sinon une remise à zéro laisserait un schéma reliant des avatars disparus.
- **Pas de bouton de transfert** sur cette planche : elle n'est ni celle d'un joueur ni celle d'un groupe, elle voyage par le modèle.
- Écran `(admin)/planche-officielle` + entrée de menu « Planche officielle » (même icône que celle du joueur : même outil, autre vue). Cloisonnement vérifié : joueur et anonyme → **307**, animateur → 200.

### ⭐ Le diagramme RZO de DELATTRE 26 porté sur la planche officielle
- **Demande** : reproduire le schéma relationnel de `EXER\DELATTRE 26\01_Montage exercice\RENS\…Diagramme RZO.pptx` sur la planche officielle, **avec les avatars existants**, sans en créer aucun.
- **Méthode — la géométrie du `.pptx`, pas l'œil** : `python-pptx` + lecture XML. Chaque trait porte sa **couleur** et son **pointillé** (= le type de relation, via la légende du document) et, quand il est attaché, les **identifiants** de ses deux extrémités (`a:stCxn` / `a:endCxn`). Pour les traits non attachés, résolution par **distance au bord** des nœuds (jamais au centre : une carte large fausse tout), avec un seuil de rejet.
- **Livré** : **30 cartes d'avatars + 8 points de jonction + 54 liens** sur la planche officielle. Positions reprises du diagramme (pouces × 200), couleurs et libellés repris de la légende.
- ⭐ **Les 8 nœuds anonymes sont des JONCTIONS, pas des avatars** : cinq silhouettes du réseau HFM/NOM — identifiées comme anonymes parce que **les cinq images ont le même SHA-1**, c'est le même fichier répété — et trois badges « ? ». Les représenter en jonctions préserve la structure **sans inventer d'avatar**.
- **Appariement 30/30**, dont 4 orthographes divergentes (`Rémi LAFFIN`→`Rémy Laffin`, `MORDVIDCHEV`→`Mordidchev`) et le trio cyrillique (`@rzo_x`, `@rzo_x_2`, `@rzo_x_3`).
- **1 lien sur 56 reste douteux** : `The flying fly` ↔ `Le Padupe` (lien suspecté), extrémités à plus d'un pouce de toute carte. Non posé — signalé à l'utilisateur.
- **Non porté** : les deux rectangles de mise en page (`27 BIM / 9 BIMa` ; le cadre des quatre cadres HFM/NOM). Ils se rendraient en **encadrés**, à valider.

### ⭐ La planche officielle voyage aussi dans le classeur Excel
- **Demande** : que « Exporter en .xlsx » emporte le schéma de la planche officielle, et que le réimport soit **fonctionnel**.
- **Format** : deux onglets, parce qu'un graphe ne tient pas dans un tableau — **`# Planche officielle - noeuds`** (cle, type, x, y, libelle, couleur, largeur, hauteur, **parent**) et **`# Planche officielle - liens`** (id, source, cible, libelle, couleur, depuis, vers).
- ⚠⚠ **LA décision qui rend l'aller-retour possible : les cartes y sont désignées par leur `username`, pas par leur identifiant.** L'import apparie les avatars par `username` et leur donne de **nouveaux** UUID ; un plan qui aurait retenu les identifiants d'origine ne retrouverait personne dans la base d'arrivée et reviendrait **vide**. Jonctions et encadrés, eux, n'existent que dans le plan et gardent leur propre id.
- ⚠ **Le plan se relit APRÈS les avatars**, jamais avant : il faut que les avatars existent pour avoir un identifiant à lui donner. D'où un classeur conservé en mémoire entre les deux étapes (`lignesDuClasseurCharge` séparé du chargement).
- ⚠ Le préfixe **`#`** garde ces onglets invisibles pour les imports qui ne les connaissent pas (dont celui de l'EHO mastorion) : un classeur exporté ici y reste lisible, la planche en moins.
- ⚠⚠ **Réservé à l'animation** : `/api/import` n'exige toujours aucune authentification (dette connue). On ne fait donc pas entrer une capacité nouvelle par une porte ouverte — sans rôle admin, **les avatars sont importés, la planche est ignorée, et le résultat le DIT** (`ignores: ["rôle admin requis…"]`). Vérifié sans session et avec un compte joueur.
- Le **filet** s'applique aussi : instantané de la planche avant l'écriture par import.
- **Aller-retour vérifié EXACT** : planche vidée → import du classeur → **43 nœuds / 56 liens / 42 nœuds imbriqués**, nœuds **et** liens strictement identiques à l'original, imbrication des encadrés comprise. Un classeur **sans** onglet de planche ne touche à rien (`planche: null`).

### 🔴🔴 L'imbrication se perdait au rechargement — et l'enregistrement automatique achevait le travail
- **Symptôme utilisateur** : « pendant que je travaille ça fonctionne, mais si je change d'onglet et que je reviens, les encadrés ont changé d'emplacement et ne sont plus à l'intérieur ».
- **Cause, en une ligne** : au chargement, la branche qui reconstruit un **encadré** ne lisait pas `parent`. Les branches `avatar` et `connecteur` le faisaient ; celle des groupes avait été écrite **avant** que les encadrés puissent s'imbriquer, et n'avait pas été reprise.
- ⚠⚠ **Pourquoi c'était bien pire qu'un oubli d'affichage** : la position d'un nœud imbriqué est **relative à son parent**. Sans `parentId`, elle est relue comme **absolue** → l'encadré saute ailleurs sur le plan. Puis **l'enregistrement différé réécrit aussitôt cet état aplati**. Le simple fait de revenir sur l'onglet **détruisait** le travail.
- ✅ **Récupéré** : la version **18** de `eho_graphe_versions` portait encore l'imbrication (42 nœuds imbriqués, 2 encadrés dans « RENS ») — capturée juste avant l'aplatissement. Restaurée. **Deuxième sauvetage réel du filet.**
- **Vérifié après correctif** : aller-retour écriture → relecture → réécriture, les 42 nœuds imbriqués et les 2 encadrés enfants tiennent.
- ⚠ **Leçon** : quand un champ devient valable pour un nouveau type de nœud, **relire TOUTES les branches** du chargement et de l'enregistrement. Ici l'écriture était correcte (le `parent` partait bien au serveur), le serveur le gardait, et seule la lecture le jetait — le genre d'asymétrie qu'aucun test d'API ne voit, parce que l'API, elle, répondait juste.

### ⭐ Encadrés imbriqués (une cellule dans un état-major)
- **Demande** : « un encadré ne peut pas être dans un autre encadré, pourtant il faut que ce soit réalisable, avec les cartes bien présentes dans l'encadré ».
- **Deux verrous levés** : le **serveur** retirait purement le `parent` des nœuds de type `groupe` (`est !== "groupe" ? … : undefined`), et l'**écran** sortait de `surFinDeplacement` dès que le nœud déplacé était un encadré.
- ⚠⚠ **Le tri « les encadrés d'abord » ne suffit plus.** React Flow exige qu'un parent précède ses enfants ; dès qu'un encadré en contient un autre, seul un tri **par profondeur d'imbrication** le garantit. Second critère à profondeur égale : l'encadré avant le reste, pour rester **derrière** les cartes.
- ⭐ **Le PLUS PETIT encadré contenant le centre l'emporte.** Avec l'imbrication, un centre tombe dans deux boîtes à la fois : prendre la dernière de la liste rangeait au hasard. La plus petite est toujours la plus intérieure — c'est celle que l'œil désigne.
- ⚠⚠ **Boucles d'appartenance** (A dans B, B dans A) : React Flow chercherait indéfiniment la position d'un nœud par rapport à lui-même et **l'écran se fige**. Trois gardes : le déplacement écarte le nœud et **toute sa descendance** ; le serveur **remonte la chaîne** de chaque nœud et détache au premier déjà-vu ; les remontées de parent portent toutes une garde `vus`. **Vérifié** : un cycle A↔B envoyé volontairement est cassé (B détaché), sans blocage.
- ⚠ **Supprimer un encadré n'emporte plus les encadrés qu'il contient** : la règle « ne partent que les nœuds visés pour eux-mêmes » vaut maintenant pour tout ce qui a **un ancêtre** dans la liste de suppression, pas seulement un parent direct. Idem pour l'interdiction de relier un encadré à son contenu, étendue à **tout ancêtre** : un lien vers le grand-parent serait tout aussi enfermé dans la boîte.
- ⚠ Le détachement calcule les positions absolues **avant** le retrait, imbrications résolues (`absolus`) : une fois le parent parti, la position d'un enfant ne veut plus rien dire.
- **Vérifié** : encadré dans encadré, **jonction au troisième niveau**, lien d'une carte vers la cellule imbriquée — tout persiste. État de l'utilisateur (43 nœuds / 58 liens) relu avant et remis après, sans résidu d'essai.

### ⭐ Les encadrés se relient, comme les jonctions
- **Demande** : relier une carte ou une jonction **à un encadré**, « en gardant le même système de placement du lien que les points de jonction ».
- **Livré** : l'encadré reçoit quatre accroches de bord (`g-<côté>` / `s-g-<côté>`) et surtout l'**ancrage géométrique** — `ancrable(type)` couvre désormais `connecteur` **et** `groupe`. Le lien touche le point du bord qui regarde l'autre extrémité, recalculé à chaque rendu : il glisse le long de l'encadré quand on déplace la carte, sans espace. Même geste, même rendu.
- **Ce que ça permet de dire** : « l'état-major finance cette cellule » se trace d'un trait vers le GROUPE, sans avoir à désigner un représentant arbitraire dans la boîte.
- ⚠ **Un encadré ne se relie pas à ce qu'il contient** (`lienValide`) : le trait serait tracé À L'INTÉRIEUR de la boîte — invisible, impossible à attraper — et il ne dirait rien, l'appartenance étant déjà écrite par le fait d'être dedans.
- ⚠ `boiteDe` prend `measured?.width ?? width` : `measured` n'existe qu'après le premier rendu, alors qu'un encadré porte sa taille dès sa création. Sans ce repli, il passait pour une pastille de 16 px le temps d'un rendu et le lien partait de son coin.
- **Vérifié de bout en bout** : aller-retour serveur d'un encadré relié à une carte (`s-left` → `g-right`) et à une jonction (`s-j-left` → `g-bottom`), puis **état exact de l'utilisateur remis en place** (42 nœuds / 56 liens — il avait continué à travailler pendant l'essai).

### Palette fermée + attaches des liens réparties
- **Constat utilisateur** : « tu as utilisé des couleurs que je ne peux pas sélectionner » et « tu as encore placé des liens au même endroit alors qu'on peut les mettre sur les côtés ou en bas ».
- ⭐ **Règle posée** : **toute couleur portée par un lien doit figurer dans la palette.** Une couleur absente s'affiche mais ne peut plus être ni retrouvée ni reproduite à la main — le joueur voit un trait qu'il lui est impossible de refaire.
- **Palette étendue de 7 à 13**, en deux familles : les couleurs de l'application (camps, STARTEX…) et ⭐ **le code couleur des diagrammes de réseau du SITCEN**, repris de leur légende et nommé par sa SIGNIFICATION — « Réseau (RZO) », « Clandestin (HFM/NOM) », « Lien suspecté », « Relation intime », « Lien familial », « Commande ». Un analyste qui a lu un diagramme RZO les reconnaît ; une planche reproduite depuis un tel document reste fidèle. Pastilles passées en 16 px et rangée `flex-wrap` pour loger les 13.
- **Attaches réparties** : chaque lien part désormais du **côté qui regarde l'autre carte** (horizontal si |dx|≥|dy|, sinon vertical), avec **bascule sur le côté suivant au-delà de 3 liens** sur un même côté. Résultat : 37 liens avec leurs deux accroches, 10 avec une seule (jonction à l'autre bout), 7 entre deux jonctions — ces dernières s'ancrant toutes seules par géométrie.
- ⚠ **L'utilisateur éditait la planche pendant l'opération.** J'ai **lu avant d'écrire** (règle du jour) : ses 3 modifications de couleur ont donc survécu. Mais ses éventuels choix d'accroche manuels ont été remplacés par le calcul. Son état exact reste restaurable — version `id=12`, auteur `thomas`, dans l'historique.

### 🔴 Erreur de ma fiche DELATTRE du 2026-09-10, corrigée
- `DELATTRE\MEMOIRE.md` affirmait que HETTA « **commande** (liens noirs) deux cellules ». **Faux** : sur les **63 traits** du fichier, **le seul trait noir est celui de la légende**. La légende définit un lien « commande » ; **le dessin n'en contient aucun**.
- HETTA n'a en réalité que trois liens : `relation RZO`→DEGARDIN, `ex-relation intime`→POMMEROND, un `lien suspecté`. La cellule YARBOT–LECONE–LAPOTRE–HERVOUET est une chaîne **HFM/NOM**, son unité n'étant portée que par un **rectangle de mise en page**.
- ⚠ **Cause** : la lecture de 2026-09-10 s'était faite **à l'œil sur le PDF** — elle a pris la proximité et les cadres pour des liens. Fiche corrigée, avec la leçon.

### Les GT apparaissent dans « EHO joueurs », même vides
- **Constat utilisateur** : « dans EHO joueurs je ne vois pas la possibilité de voir l'EHO des GT ».
- **Diagnostic** : la section existait déjà (et la route de détail savait déjà servir un GT — elle calcule `estGroupe` et les contributeurs). Mais la liste était bâtie **uniquement à partir des GT ayant des lectures** → un groupe sans travail était **purement introuvable**. Les lectures des GT versées plus tôt avaient été effacées par mes applications de modèle : la section était donc vide.
- **Corrigé** : la liste part de **tous** les GT (Keycloak) **union** ceux qui portent des lectures. Un groupe neuf, ou remis à zéro, s'affiche **à zéro** au lieu de disparaître ; un groupe supprimé de Keycloak mais porteur de travail reste visible — sa trace ne doit pas s'évaporer.
- ⚠ Et dans la route de détail : `estGroupe` ne peut pas se déduire des seules lectures. Sans lecture, un GT passait pour **un joueur anonyme sans nom**. Il est désormais reconnu par Keycloak. *Ne rien savoir n'est pas la même chose que savoir que c'est un joueur.*
- **Vérifié** : « 1re Division » et « 27e Brigade » listées à 0 ; ouverture d'un GT vide → nom correct, `estGroupe = true`, 62 lignes STARTEX. Garde-fous intacts : planche d'animateur par URL directe → **404**, joueur sur la liste → **403**.

### Rangement des deux planches admin + supervision des planches joueurs
- **Demande** : « Planche officielle » **dans ANIMATION** (c'est la vérité de l'exercice, pas une production de joueur), et un nouvel onglet **dans JOUEURS** pour voir les planches relationnelles **des joueurs et des GT**.
- **Menu réorganisé** : ANIMATION = Tableau de bord · Avatars · Groupes · **Planche officielle** · Modèles d'EHO · Import/Export — la planche officielle est **posée juste avant les Modèles**, parce qu'elle voyage avec eux. JOUEURS = EHO joueurs · Comparatif · **Planches relationnelles**.
- ⭐ **Porteur `observateur`** (`lib/porteur.ts`) : `?joueur=<sub>` (admin seul) et `?gt=<id>` pour un animateur **non membre** rendent un porteur marqué **lecture seule**.
- ⚠⚠ **Le vrai danger était l'enregistrement automatique** : la planche s'enregistre après une seconde de repos — **il suffisait d'OUVRIR le travail d'un joueur pour que l'écran de l'animateur le réécrive**. Verrou posé à trois niveaux : (1) **toute route d'écriture refuse un porteur observé** — `refusObservateur()` dans les 7 routes concernées, vérifié **403** sur planche, restauration, rangement, lecture et verrou ; (2) l'enregistrement différé **ne part pas** ; (3) les gestes d'édition sont neutralisés (classe `.lecture-seule` dans `globals.css` : liens inertes, boutons des cartes masqués, accroches cachées), plutôt que de faire descendre un drapeau dans chaque composant.
- ⚠ Un joueur qui tente `?joueur=<autre>` → **403** (« réservé à l'animation »).

### 🔴 Bug antérieur trouvé au passage — `tousLesGroupesDeTravail` rendait TOUJOURS une liste vide
- **Keycloak 26 ne remplit plus `subGroups`** : la recherche de groupes rend la racine `GT` avec `subGroups: []` et un `subGroupCount: 2`. Les enfants se demandent séparément, sur **`/groups/{id}/children`**.
- Conséquence : **aucun groupe de travail n'apparaissait dans les écrans d'animation**, sans la moindre erreur — le piège du « résultat vide » qui cache une lecture ratée, exactement celui qu'on avait déjà corrigé ailleurs. Touchait aussi le champ `groupes` de `/api/eho/comparaison`.
- **Corrigé et vérifié** : `['1re Division', '27e Brigade']` remontent.
- Le `[]` en cas d'échec est **conservé ici seulement**, et commenté : cette liste ne remplit qu'un choix à l'écran, elle ne décide **jamais** d'un accès — le contrôle d'appartenance passe par `groupesDeTravail`, qui rend `null`.
- `/api/eho/gt?tous=1` ajouté (admin seul) : un animateur supervise des groupes dont il n'est pas membre.

### 🔴 Encore un écrasement de test — planche du GT vidée, puis récupérée par le filet
- En testant « l'écriture doit être refusée », j'ai lancé un `PUT` vide sur le GT **1re Division** en supposant que l'animateur n'en était pas membre. **Il l'était** → écriture acceptée, planche vidée (l'encadré MERCURE et ses 3 liens).
- ✅ **Le filet posé une heure plus tôt a tenu** : `eho_graphe_versions` contenait l'état, restauré en un appel. **Premier sauvetage réel du dispositif.**
- ⚠ **Règle** : un essai « ceci doit être refusé » se fait sur une cible dont on a **vérifié** qu'elle déclenche le refus — sinon c'est un essai « ceci doit réussir », mené sans le savoir.

### Sauvegardes d'avant-application : complètes, plafonnées à 3, jamais pour rien
- **Arbitrage utilisateur** : « changer de modèle supprime tous les travaux des joueurs, **c'est normal** » → **aucune restitution automatique** après une application. Un nouveau modèle est un nouvel exercice. Et : « je ne veux pas qu'on se retrouve avec énormément de sauvegardes qui servent à rien ».
- **Constat chiffré** : ~400 Ko par sauvegarde et **aucune purge** — le dossier grossissait sans fin. Le problème existait déjà, indépendamment du reste.
- **Trois règles livrées** :
  1. ⭐ **Complète, ou pas du tout** — la sauvegarde embarque désormais `travail` : lectures, rangements (`eho_dispositions`) et planches des joueurs et des GT. Sans cela, « restaurer » rendait une population sans son exercice : du théâtre.
  2. ⭐ **Trois gardées** (`SAUVEGARDES_GARDEES`), purge à chaque écriture, tri par nom (l'horodatage ISO EST l'ordre chronologique, inutile d'ouvrir les fichiers). Plafond ~5 Mo. Le seul cas d'usage réel — « je viens de cliquer sur le mauvais modèle » — se voit dans la minute.
  3. **Rien à sauver → aucun fichier** : base vide et aucun travail = pas d'écriture. `ResultatApplication.sauvegarde` devient `string | null`.
- ⚠ **`travail` est dans les SAUVEGARDES, jamais dans les MODÈLES.** Un modèle est une population réutilisable : y embarquer les analyses d'un exercice passé les ferait ressurgir chez les joueurs du suivant. **Vérifié** : un modèle capturé contient `users`, `groups`, `graphe` — et **pas** `travail`.
- ⚠ **Les verrous et les instantanés de versement ne sont PAS sauvegardés** : les uns expirent seuls, les autres n'ont de sens que dans la minute. Les restaurer ressusciterait des verrous fantômes.
- ⚠ La restauration fait **table rase d'abord** sur rangements et planches joueurs : sinon une planche que la sauvegarde ignore survivrait à la restauration.
- **Aller-retour vérifié** : 2 lectures posées → application (lectures à 0, sauvegarde contenant 2 lectures) → restauration → **les 2 lectures reviennent, nommément**, planches et rangements intacts. Purge vérifiée : 4 applications d'affilée → **3 fichiers**.
- ⚠ Conséquence assumée du plafond : **4 applications successives effacent l'état d'origine**. C'est le prix du choix, et il est explicite.
- 💡 Piste écartée à raison : garder *volontairement* un exercice, c'est **capturer un modèle** — le geste explicite. La sauvegarde automatique est un filet, pas une archive.

### 🔴🔴 DÉCOUVERT EN TESTANT — appliquer un modèle DÉTRUIT toutes les lectures des joueurs
- **Le fait** : `eho_lectures.avatar` porte `onDelete: Cascade`. `remplacer()` fait `tx.user.deleteMany({})` → **toutes les analyses de tous les joueurs disparaissent**, silencieusement, à chaque application de modèle. Constaté en direct : les 6 lectures de `joueur_test` sont passées à 0.
- ⚠ **La sauvegarde automatique ne les couvre pas** : le fichier `data/eho/backups/*.json` contient `users`, `groups` et désormais `graphe` — **jamais `lectures`, `dispositions` ni les planches des joueurs**. Il n'y a donc rien à restaurer.
- ⚠ **C'est ANTÉRIEUR à ce travail** (le cascade et `remplacer` existaient), mais je l'ai déclenché : 6 lectures d'essai perdues. Ce qui a **survécu** : `eho_graphes` et `eho_dispositions` (aucune clé étrangère vers `users`).
- 💡 **Correctif proposé à l'utilisateur, non appliqué** : inclure `lectures` + `dispositions` + planches des joueurs dans la sauvegarde d'avant-application, et les **réattacher après** (les identifiants d'avatars sont conservés par le modèle, la réattache est donc exacte). À défaut, au minimum **avertir** dans l'écran « Modèles d'EHO ».
- 🔁 **État remis d'aplomb** : modèle `SKOLKAN` ré-appliqué (étiquette du modèle actif correcte, 453 avatars), modèle d'essai `ESSAI_PLANCHE` supprimé, planche officielle conservée (4 nœuds, 2 liens).

### Liens des jonctions : attache géométrique, recalculée à chaque rendu
- **Constat utilisateur** : « ça part dans tous les sens, une card est en haut alors qu'elle se connecte au point à droite » + « je ne veux plus d'espace entre le lien et le point/encadré ».
- **Cause** : une jonction portait **quatre accroches fixes**, et l'accroche choisie au moment du tracé était figée dans le plan. Un lien déclaré « en haut » repartait vers le haut même une fois la carte déplacée à droite — et rien ne suivait le mouvement.
- **Livré** : `ancrer(boite, vers)` — le point du **bord** qui regarde l'autre extrémité, **recalculé à chaque rendu**, donc il glisse le long de la jonction quand on déplace la carte. Deux formes : **disque** pour la jonction nue (≤ 20 px), **rectangle** pour la jonction nommée (on pousse le vecteur jusqu'au premier bord). Le point tombe **exactement sur le bord** → plus d'espace.
- ⭐ **Les DEUX bouts s'ancrent** dès qu'une jonction est en jeu, carte comprise : une jonction n'a pas de côté, garder l'accroche manuelle côté carte reproduisait le défaut. **Entre deux cartes, rien ne change** — les côtés choisis sont un choix du joueur.
- ⚠ **C'est le NŒUD qui fait foi, plus l'accroche** (`type === "connecteur"` via `useInternalNode`) : les plans enregistrés avant les quatre accroches se comportent comme les autres.
- Chaque bout vise le **centre** de l'autre, jamais son ancrage : sinon les deux se poursuivraient sans se fixer.

### ⭐ Filet de sécurité des planches relationnelles (`eho_graphe_versions`) — suite directe de l'incident
- **Déclencheur** : les deux écrasements ci-dessous. `eho_graphes` ne gardait **qu'une ligne par porteur, réécrite en bloc, sans historique**. Proposé à l'utilisateur, accepté (« oui tu peux le rajouter »).
- **Schéma — additif uniquement** : nouveau modèle **`EhoGrapheVersion`** (`eho_graphe_versions`) — `playerId`, `contenu` (l'état complet d'avant), `auteur` (**celui dont on sauve le travail**, pas celui qui écrit), `motif`, `creeLe`, index `(playerId, creeLe)`. `prisma db push` → « in sync », rien de supprimé.
- ⚠ **Surtout PAS un instantané par enregistrement** : la planche s'enregistre après chaque seconde de repos — on noierait la table et la seule version utile serait introuvable. `lib/graphe-versions.ts` ne retient qu'aux moments qui veulent dire quelque chose :
  1. **`force`** — acte délibéré et lourd (transfert d'encadré, restauration) : toujours ;
  2. ⭐ **quelqu'un d'autre a écrit en dernier** — LE cas à protéger sur une planche collective : je m'apprête à recouvrir le travail d'un voisin ;
  3. le dernier instantané date de **plus de 3 minutes** — on jalonne une longue séance sans la hacher.
  Au-delà de **20 versions** par porteur, les plus anciennes s'effacent.
- ⚠ **`conserverEtat` ne lève jamais** (try/catch silencieux, commenté comme tel) : un filet qui empêcherait d'enregistrer ferait perdre le travail qu'il prétend sauver.
- **Restaurer conserve d'abord l'état courant** → on peut **annuler l'annulation** (vérifié : motif `avant restauration`). Exception voulue : un état **vide** n'est pas conservé, il n'y a rien à sauver.
- ⚠ **Après restauration, l'écran RECHARGE la page.** Sans cela, le client garde l'ancien plan en mémoire et son enregistrement différé le réécrit une seconde plus tard — la restauration serait annulée toute seule.
- ⚠ **L'appartenance de la version au porteur est revérifiée** : l'identifiant est un entier, il se devine. Sans ce contrôle on lirait — et on écrirait — la planche d'un autre groupe.
- **UI** : bouton **« Historique »** en tête de planche → liste des 20 derniers états (quand, combien de cartes/liens, **de qui**, pourquoi), bouton « Restaurer » avec confirmation.
- **Vérifié de bout en bout** : planche du GT vidée d'un `PUT` → l'état de 5 nœuds/3 liens apparaît dans l'historique au nom de `joueur_test` → restauration → planche revenue (MERCURE + conseil). Refus : version d'une autre planche → 404 · version inexistante → 404 · sans session → 401 · GT dont on n'est pas membre → 403.
- ⚠ **`prisma generate` → redémarrage du serveur de dev** (4ᵉ rencontre du même piège).

### 🔴 Deux écrasements de la planche de l'utilisateur, le même jour
- **Ce qui s'est passé** : deux fois, j'ai écrit un plan d'essai sur une planche relationnelle **en production d'usage** — celle de `joueur_test` pendant qu'il travaillait dessus, puis celle du **GT 1re Division** sans l'avoir lue au préalable. `eho_graphes` = **une ligne par porteur, écrasée en bloc, sans historique**.
- ⚠⚠ **Règles à tenir désormais** : (1) **lire avant d'écrire** toute planche d'un porteur, systématiquement ; (2) ne jamais poser un plan d'essai sur un porteur vivant ; (3) pour vérifier une API d'écriture, **partir de l'état lu et n'y ajouter que le strict nécessaire**, puis retirer ses propres artefacts (fait pour le GT : nœud « travail du GT » et son lien supprimés, le versement de l'utilisateur conservé).
- 💡 **Piste** : `eho_graphes` gagnerait le même filet que l'EHO (`eho_sauvegardes` / `eho_versements`) — un instantané avant écriture. À proposer.

### 🔒 Trou de garde trouvé en vérifiant — section JOUEUR ouverte aux anonymes
- **Constat** : `(player)/layout.tsx` **n'avait aucun garde**. Sans le moindre cookie, `/mon-eho`, `/eho-gt`, `/graphe` et `/avatars` répondaient **200** — pages vides (les routes `/api` répondent bien 401) mais coque, navigation et libellés servis à un inconnu. La section **animation**, elle, était gardée depuis le 2026-09-14.
- **Corrigé** : garde côté serveur, sur le modèle de `(admin)/layout.tsx`. On n'y vérifie **qu'une chose — être connecté** : il n'existe pas de rôle « joueur », et un animateur doit pouvoir ouvrir ces écrans (c'est ainsi qu'il contrôle ce que voit un joueur).
- **Vérifié** : anonyme → **307** sur les quatre pages ; joueur → 200 ; animateur → 200 partout.
- ⚠ **Règle** : *une page qui répond 200 à un inconnu est une page ouverte, même vide.* Chaque groupe de routes doit porter son garde — ne pas supposer qu'un groupe voisin protège.

### Contrôles de la séance
- `npm run test` **71/71** · `npm run test:bio` **538/538** · `npx tsc --noEmit` et `npx eslint` **sans erreur**.
- ⚠ **Lancer `tsc` dans le clone d'exécution `C:`**, jamais dans `D:` : sur D: (exFAT) le client Prisma ne peut pas être généré, et `tsc` y crache 40 erreurs fantômes sur des modèles pourtant présents.
- Pages vérifiées en conditions réelles (cookies de session forgés) : `/graphe`, `/mon-eho`, `/eho-gt` **200** côté joueur, `/eho-joueurs` **200** côté animateur ; plan d'essai à deux jonctions (une nommée, une anonyme) rechargé depuis l'API.
- ⚠ **Troisième rencontre du même piège** : client Prisma périmé après `prisma generate` → **redémarrer le serveur de dev**.

### ⏭️ Reste à faire
- **Concurrence sur la planche relationnelle collective** : aujourd'hui **dernière écriture gagnante**, sans verrou (à trancher — le grain « carte » du verrou EHO ne s'y transpose pas).
- Remplacer les GT d'essai « 1re Division » / « 27e Brigade » par les **vrais groupes**.
- Toujours en attente : arbitrage des **10 routes API sans autorisation** (§ 8bis de `MEMOIRE.md`).

## 2026-09-14 — EHO PLEIADE : sécurité des écrans, rangement du joueur, refonte visuelle (branche `MEYTRE`)

Séance longue, entièrement dans `cecpc-pleiade/eho`, branche `MEYTRE`. Rien sur le serveur : tout en local (`C:\CECPC\PLEIADE\eho`, port 3001).

### 1. Cloisonnement animateur / joueur

- **La navigation suit le rôle** : rubrique « Animation » (configurer l'EHO) + « Joueurs » (ce qu'ils en ont fait) pour l'animateur ; rubrique « Joueur » seule pour l'entraîné. `lib/roles.ts` centralise les rôles admissibles (`admin`, `realm-admin`), partagé par le garde d'API, le garde de layout et la barre.
- ⚠ **Découverte : toute la partie animation était OUVERTE sans authentification** (`/dashboard` répondait 200 sans session). Verrou posé **côté serveur** dans `(admin)/layout.tsx` : anonyme → `/login`, opérateur sans rôle → `/mon-eho`. Vérifié 14/14 (anonyme, joueur, animateur × 9 pages).
- **Panne latente révélée** : `KEYCLOAK_CLIENT_SECRET` du `.env` (`eho-secret`) ne correspondait pas au client Keycloak (`eho-dev-secret`). Keycloak validait l'identité puis refusait l'échange du code — « Server error » générique. Personne ne l'avait vu **parce qu'on ne se connectait jamais** : les écrans étaient ouverts et mes vérifications passaient par des jetons obtenus directement.
- **Filtrage des planches** : `lib/keycloak-admin.ts` demande au realm qui porte un rôle d'animation ; ces comptes sont exclus de la liste des joueurs ET du classement des avatars mal lus. Un animateur qui essaie le dispositif ne fausse plus les statistiques de ses entraînés. Échec Keycloak → filtre désactivé (jamais un écran vide).

### 2. 🔴 Bug de conception grave : la dégradation silencieuse

Deux incidents de la même famille, remontés par l'utilisateur :

- **« Je suis en vue joueur »** alors qu'il était `thomas` (animateur). Cause : quand le rafraîchissement du jeton échoue, `auth.ts` **vide les rôles** ; la barre en déduisait « pas admin, donc joueur » et repliait le menu **sans rien dire**. L'interface annonçait un rôle faux. Corrigé : bandeau « Session expirée — ce menu ne reflète pas votre rôle réel » + bouton de reconnexion, pastille « rôle inconnu », et les écrans d'animation renvoient vers `/login` au lieu de déposer l'animateur sur la planche joueur. La barre est en outre devenue **collante** : le compte connecté était auparavant en bas d'une page de 4 000 px, donc invisible.
- **« Appliquer a vidé tout le package STARTEX »** : la lecture du package renvoyait 401 (session expirée) et le code traitait cet échec comme **un package vide**. Aucune donnée perdue (journal d'activité vierge), mais avec un autre enchaînement le retrait des 62 aurait été réellement envoyé.

> ⚠ **Règle tirée de ces deux incidents : un échec de lecture ne doit JAMAIS être présenté comme un résultat valide.** Lever, afficher, désactiver l'action — mais ne pas rendre « vide » ou « sans rôle » ce qu'on n'a pas pu lire.

Durcissements appliqués au package : la lecture lève au lieu de rendre un ensemble vide ; le bouton reste désactivé tant que le package n'est pas connu ; **« Appliquer » relit le serveur** avant de calculer l'écart (au lieu de se fier à une copie locale vieillie) ; un retrait de plus de 5 avatars représentant la moitié du package demande confirmation ; l'état est **relu** après application au lieu d'être supposé.

### 3. Package STARTEX — l'écran manquant

L'API existait depuis le portage, **sans aucune interface** : il n'y avait donc aucun endroit correct pour modifier le package. Mode sélection ajouté au trombinoscope (★ pleine / ☆ creuse, pastilles `+`/`−` de ce qui va changer, barre d'action collante, rien d'écrit avant « Appliquer »).

⚠ **Faille trouvée en chemin** : cocher le groupe STARTEX depuis la fiche d'un avatar **n'appliquait pas la purge des estimations** — exactement le symptôme « Lena Peters mal placée » du 10 septembre. La règle est désormais écrite une fois (`purgerEstimations`) et appliquée sur **tous** les chemins.

### 4. Ce que le joueur peut faire de sa planche

- **Curseur d'alignement** (−100 bleu · 0 neutre · +100 rouge) : porte le camp ET la force de conviction d'un seul geste. ⭐ Le curseur est la **valeur de référence**, `campEstime` en est **déduit côté serveur** — deux champs disant la même chose finissent toujours par se contredire, et c'est sur le camp que la comparaison marque les écarts. Colonne `camp_curseur` ajoutée, script de reprise idempotent `npm run backfill:curseur` pour les lectures antérieures.
- **Ordre libre des cartes** dans une zone, puis **rubriques créées par le joueur** (« Politique » dans MERCURE…), avec renommage et suppression sans perte.
- ⭐ **Choix de stockage** : une **seule ligne par joueur** (`eho_dispositions`, JSON zone → rubriques + listes). Une colonne par carte aurait écrit 391 lignes pour remonter un avatar d'un cran. Les listes sont **partielles** : seul ce qui a été déplacé à la main est enregistré. Le format initial (liste simple par zone) est relu sans perte par `normaliserDisposition`.
- L'ordre enregistré est calculé sur la zone **complète**, recherche ignorée : filtrer puis déplacer aurait effacé la position des cartes masquées.
- **La vue animateur reproduit la planche à l'identique** — mêmes rubriques, même ordre, même ordre de repli (les deux écrans appellent la même fonction de répartition).

### 5. Fiches et lisibilité

- **La fiche du trombinoscope ne s'ouvrait pas** : `<dialog>` natif + `showModal()`, cause exacte non identifiée (pas de navigateur pilotable sur le poste). Remplacé par la surcouche qui fonctionne partout → **les trois fiches de l'application partagent une seule mécanique** (`components/fiche.tsx` : Modale, Biographie, Champs, Rubrique, LiseréCouleur).
- **Les bios ne sont pas des pavés** : 57 des 262 sont des **fiches structurées de countrybook** (`Parcours : … | Objectifs : … ; … ; …`), une est en **Markdown**, le reste en prose continue **sans un seul saut de ligne** (la plus longue : 3 006 caractères). `lib/bio.ts` reconnaît la structure et la restitue en rubriques et listes ; la prose est aérée en paragraphes. **Aucun mot n'est modifié.** Test sur les 262 bios réelles : `npm run test:bio`, **538/538**, le plus long bloc passe de 1 411 à 612 caractères.
- Fiche sur **deux colonnes** (état civil en rail, biographie à droite), champs `aime`/`deteste`/`email` qui n'arrivaient jamais à l'écran.

### 6. Ergonomie et design

- **Barre repliable** (68 px en icônes), choix retenu et synchronisé entre onglets via `useSyncExternalStore`.
- **Planches en pleine largeur** (le trombinoscope était bridé à 1 600 px) ; le Comparatif reste borné à 1 500 px — c'est un écran de lecture.
- **Fusion « Avatars » + « Trombinoscope » en une seule entrée**, avec bascule **Planche | Liste** ; la planche est la vue par défaut. Bouton « + Nouvel avatar » sur les deux vues, **un seul formulaire** (`components/nouvel-avatar.tsx`).
- Libellés corrigés : ce bouton crée un **avatar**, pas un « utilisateur » — plus aucune occurrence du mot dans les écrans d'animation.
- **Trombinoscope aligné sur la planche joueur** : bandeau pays + panneau attaché, catégories en filet de couleur + libellé + effectif. Le gris est réservé au panneau ; les cartes restent sur blanc (les fiches non dirigeantes sont en #fafafa et s'y fondraient).
- Indicateur de dev Next déplacé en bas à droite : il recouvrait la déconnexion de la barre repliée.

### 7. Vérifications de la séance

Aller-retour Excel prouvé : export (453 avatars, 22 colonnes, onglet groupes) → modification d'une fiche → ré-export (la modification y est) → **réimport : `created 0, updated 453, refused 0`**, 58 groupes, 1 643 appartenances, 62 STARTEX, portraits et lectures intacts. Appariement **par `username` uniquement**.

⚠ Rappel : le **modèle SKOLKAN n'est pas un fichier Excel** mais un instantané JSON (`data/eho/templates/skolkan/`) capturé depuis la base — il conserve les identifiants, ce que le classeur ne fait pas.

### 8. Pièges d'environnement rencontrés (à ne pas réapprendre)

- **Après `prisma generate`, REDÉMARRER le serveur de dev** : il garde l'ancien client en mémoire et les écritures échouent en 500. Vu deux fois.
- **Toujours contrôler le code HTTP** dans les scripts d'essai : un script qui parse la réponse sans regarder le statut avale les 500 et fait croire que tout marche.
- Les sessions de test expirent au bout d'une heure : un 401 en cours d'essai n'est pas un bug de l'application.

### 9. État final

Base : **453 avatars · 58 groupes · 1 643 appartenances · 62 STARTEX · 6 lectures · 1 disposition**. `tsc` et ESLint propres (hors avertissement `<img>` préexistant), **71/71** tests trombinoscope, **538/538** tests bios.

⚠⚠ **Toujours ouvert** : les **10 routes API sans contrôle d'autorisation** (`/api/users`, `/api/groups*`, `/api/import`, `/api/uploads*`, `/api/activity`, `/api/avatars/export`). `GET /api/avatars/export` télécharge **toute la bibliothèque sans authentification**. Le dépouillement de la planche joueur reste contournable par `GET /api/users`.


## 2026-09-11 (suite 2) — Modèle SKOLKAN créé · 🔴 incident : suppression accidentelle des 63 groupes

- **Question utilisateur « pourquoi 473 avatars ? »** — décompte établi : **453 à nous** (451 de la bibliothèque après retrait du doublon Gavrilov **+ HETTA et Kimberley**, créés la veille depuis le diagramme RENS DELATTRE 26) **+ 20 avatars de démonstration** préexistants dans le nouvel EHO (noms français génériques, groupes « Journalistes / Population civile / Autorites locales / Groupe hostile / Influenceurs » — données de Xavier, pas les nôtres). Les 20 ont été supprimés → **453**.
- 🔴 **INCIDENT — ma faute, réparé.** En voulant purger les groupes de démonstration devenus vides, j'ai jugé « vide » tout groupe dont le compteur ne portait pas le nom que j'avais **supposé** (`_count.users` / `userCount` / `nbAvatars`) — or `/api/groups` n'expose aucun de ces champs. **Les 63 groupes ont donc été supprimés**, CAMP ROUGE / STARTEX / EXERCICE * compris, et le modèle capturé dans la foulée était vide de groupes.
  - **Dégâts** : 0 appartenance, 0 groupe. **Avatars, fiches et 118 portraits INTACTS.**
  - **Réparation** : réimport du classeur → `created 0, updated 453, refused 0` → **58 groupes, 1 643 appartenances, STARTEX à 62** ; modèle erroné supprimé puis **recapturé correctement (453 avatars / 58 groupes)**.
  - ⚠ **Leçon à appliquer partout : ne JAMAIS déduire un champ d'API par supposition avant une suppression de masse.** Lire la réponse réelle d'abord (un simple `GET` l'aurait montré), et pour toute opération destructive, vérifier sur UN élément avant de boucler.
- ✅ **Modèle `SKOLKAN` disponible** dans « Modèles d'EHO » (453 avatars, 58 groupes, package STARTEX inclus) aux côtés de `VIERGE`.

## 2026-09-11 (suite) — EHO PLEIADE : STARTEX, planche joueur et comparaison portés (branche `MEYTRE`)

- **Demande utilisateur** : porter STARTEX + comparaison vers le nouvel EHO, **sans la notion de cellule** (mise de côté), avoir **tous les avatars** dans l'EHO de PLEIADE, une **vue joueur** où il range les cartes (sauf les STARTEX) et la **comparaison** animateur/joueur. Travail exigé dans le dépôt **`cecpc-pleiade/eho`**, branche **`MEYTRE`**.
- **Base retenue (validée par l'utilisateur)** : `origin/feat/avatars-sans-keycloak` — 3 commits de nos sessions précédentes (compte `ViktorGlarak`) qui avaient déjà porté **l'affranchissement Keycloak des avatars**, le **trombinoscope** (`src/lib/trombinoscope.ts` : thèmes, rangs, regroupement) et les **modèles d'EHO** (catalogue, capture, application verrouillée, sauvegardes). `MEYTRE` créée depuis cette branche pour ne rien casser.
- **Livré (commit `8c10b87`, poussé sur `origin/MEYTRE`)** :
  - schéma : **un seul modèle ajouté**, `EhoLecture` (`eho_lectures`) — la lecture d'UN joueur (`playerId` = `sub` Keycloak, sans clé étrangère) sur UN avatar ; séparée de `users` par construction ;
  - **STARTEX = un GROUPE** nommé « STARTEX » → rien de plus au schéma, et **le package voyage dans les classeurs** (vérifié : les 62 autorités sont arrivées par l'import Excel) ; entrer au package **purge** les rangements déjà posés, conserve les notes ;
  - API : `/api/eho/startex` (GET+POST, admin), `/api/eho/mon-eho` (GET, tout opérateur), `/api/eho/mon-eho/[avatarId]` (PUT), `/api/eho/comparaison` + `/[playerId]` (admin) ;
  - UI : page joueur **`(player)/mon-eho`** (glisser-déposer natif HTML5, aucune dépendance ajoutée, équivalent clavier par la fiche) et **`(admin)/comparaison`** (tuiles par joueur, avatars les plus mal lus, détail officiel/joueur avec verdicts ✓/✗) ; entrées ajoutées à la Sidebar.
- ⚠ **Écart de zone calculé sur la ZONE attendue, pas sur le pays brut** : un avatar sans pays (ONU, CICR) est attendu en « Autre / International » — sinon un rangement juste compterait pour faux.
- ✅ **Vérifié 8/8 en conditions réelles** (comptes Keycloak `joueur_test` / `anim_test` créés dans le realm `cecpc`, jetons par flux mot de passe sur le client `eho`) : 62 au package · 403 joueur sur `/startex` et `/comparaison` · **473 cartes dont 0 champ officiel sur un non-STARTEX** · Olamao pré-placé Mercure/rouge avec sa bio · rangement d'un non-STARTEX OK · **re-rangement d'un STARTEX ignoré mais note conservée** · zone inventée refusée (400) · comparaison : 63 lignes, STARTEX jamais en écart, note visible.
- **Avatars chargés** : **453 importés** depuis `BIBLIOTHEQUE_TEST_3_EXERCICES.xlsx` (0 refus — le contrat d'import de la branche accepte nos classeurs tels quels) + 20 de test = **473** ; **118 portraits transférés** depuis l'ancienne base MASTORION via `/api/uploads` (total 138 avec photo), servis en HTTP 200.
- ⚠⚠ **FAILLE DE SÉCURITÉ SUR LA BRANCHE DE BASE, À TRANCHER** : **10 routes API n'ont AUCUN contrôle d'autorisation** (`/api/users`, `/api/users/[id]`, `/api/groups*`, `/api/import`, `/api/uploads*`, `/api/activity`, `/api/avatars/export`). **Démontré** : sans aucune authentification, `GET /api/users?limit=2` renvoie les 473 avatars avec `pays`, `label`, `activite`, `observations`. **Cela annule le dépouillement de la planche joueur** — un joueur n'a qu'à appeler cette route. ⚠ Tension produit à arbitrer : la page `(player)/avatars` (choix d'avatar) consomme `/api/users` et a besoin des identifiants — la fermer telle quelle casserait cette page. Piste recommandée : **charge utile réduite pour les non-admins** sur `/api/users` + `exigerAdmin` sur import/export/activity/uploads.
- ⚠ Contrainte d'environnement : **D: est en exFAT → aucun binaire natif ne s'exécute** (`next build` et `prisma db push` échouent en EPERM). D'où un **clone d'exécution `C:\CECPC\PLEIADE\eho`** (NTFS) où tournent npm, Prisma et le serveur de dev (port **3001**) ; le dépôt D: reste la copie de référence. Même schéma que pour mastorion.

## 2026-09-11 — Création de l'agent + première analyse de `D:\CECPC\PLEIADE`

- **Déclencheur utilisateur** : « le programme devait s'appeler MASTORION, maintenant MASTORION devient simplement un réseau social et à terme on lui changera de nom » → créer un agent **PLEIADE** qui comprenne le **système global**, et mettre à jour l'agent MASTORION en conséquence.
- **Analyse en lecture seule de `D:\CECPC\PLEIADE`** : 3 dépôts git clonés (`pleiade-platform`, `mastorion`, `eho`), organisation GitHub **`cecpc-pleiade`** (l'ancien `XTalandier/mastorion-v0` est dépassé). Un 4ᵉ dépôt, `pleiade-infra`, est référencé mais **non cloné** sur ce poste.
- **Sources lues** : les `CLAUDE.md` de `pleiade-platform` (187 l., très complet — architecture serveur, zones, instances, Keycloak, catalogue, conventions, PKI) et de `mastorion` (242 l.) ; le `CLAUDE.md` de `eho` ne contient qu'un renvoi vers `AGENTS.md` (gabarit Next.js) → **l'EHO n'a pas encore de documentation propre**, sa connaissance vient de la lecture du code.
- **Architecture retenue en mémoire** : orchestrateur de **zones** (1 realm Keycloak par zone) contenant des **instances** d'apps (compose + .env + client KC + route Traefik générés) ; serveur 192.168.10.10 sous **Podman rootful** (toujours `sudo`), accès **VPN Pritunl**, Traefik en `*.mastorion.internal`, catalogue de 4 apps (`mastorion`, `eho`, `wordpress`, `webserver`).
- ⭐ **Liaison inter-instances comprise** : quand eho et mastorion coexistent dans une zone, `EHO_URL` est injecté dans mastorion, qui **résout les comptes de scénario auprès de l'EHO** (`admin/scenario-items.ts`). **L'EHO devient la source d'identité des personas.**
- ⚠ **EHO RÉÉCRIT** : ce n'est plus notre app Angular mais un dépôt **Next.js 16 + next-auth v5 + Keycloak** autonome (3 commits, stade précoce). `User.id` = **UUID Keycloak**. **Bonne nouvelle vérifiée : les champs de persona sont exactement ceux de MASTORION** (`pays`, `label`, `activite`, `observations`…) → **les bibliothèques MINERVE restent exploitables**. Import attendu en **CSV** (`csv-parse`), l'export Excel vivant côté orchestrateur.
- ⚠ **Sort de notre travail EHO Angular** : la branche **`origin/feat/eho`** (8 commits, `b2e91ec`…`89ad382`) **existe toujours** mais n'a **jamais été fusionnée** dans `main`, et `main` a divergé (Keycloak, layouts sociaux, impersonation auditée). Les fonctionnalités développées (modèles d'EHO, cellules joueurs, fiches d'analyse, **package STARTEX**, trombinoscope, vue comparative) sont **absentes du nouvel EHO** → **point à trancher avec l'utilisateur** (abandonner ou porter). Le savoir de conception reste capitalisé dans `MASTORION\MEMOIRE.md` et `MASTORION\JOURNAL.md` (09–10 sept.).
- **Créations MINERVE** : dossier `PLEIADE\` (README + MEMOIRE + JOURNAL), prompt système `SYSTEME\PROMPTS\pleiade.md`, entrée au registre `CLAUDE.md` (**21 → 22 agents**), branche de routage dans `SYSTEME\ROUTAGE.md`, compteur `NOYAU\MEMOIRE.md` mis à jour.
- **Agent MASTORION recadré** : son périmètre devient **le réseau social seul** ; chemins, organisation GitHub et statut de l'EHO corrigés dans ses fichiers.
