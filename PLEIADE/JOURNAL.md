# JOURNAL — PLEIADE (historique chronologique, append-only)

> Comptes rendus datés des travaux sur le système PLEIADE. Les règles et l'état durable sont dans `MEMOIRE.md`.

---

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
