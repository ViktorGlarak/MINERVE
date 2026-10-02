# JOURNAL — LEAC (historique chronologique, append-only)

> Comptes rendus datés des travaux sur le système LEAC. Les règles et l'état durable sont dans `MEMOIRE.md`.

---

## 2026-10-02 — Identité aléatoire à chaque connexion : correction et recollage (`db7738c` + `da5c4f6`, branche `identite-sub`, version `2026-10-02.1`) — ✅ EN LIGNE le 2026-10-02 (`/api/sante` = `2026-10-02.1` sur cecpc-div-eval)

- **Défaut** (le même que dans la messagerie) : `auth.ts` prenait `user.id` d'Auth.js, qui est un UUID aléatoire à chaque connexion Keycloak, et non le `sub`. La première connexion liait affectation, administration ou référence à cet id ; à la connexion suivante, la personne pouvait **perdre son contrôle ou ses droits**.
- **Correction** :
  - `jwt` prend le `sub` (`profile.sub` / `providerAccountId`) ; le fournisseur « jeton » (type credentials) garde `user.id`.
  - Les sessions d'avant la correction sont closes une fois (`idv: 2`).
- **Recollage** : `src/lib/zone/recoller.ts` (`recollerIdentite`), appelé avant la lecture des droits (`profilDe`) et dans les réclamations (affectations, références).
  - Repassent au vrai sub les lignes `MembreEquipe`, `AdministrateurEntite` et `ReferentUnite` désignées à l'adresse de la personne mais tenues par un autre id, ainsi que ses `Appareil` et l'`auteurId` de ses `Operation`.
  - Le journal d'audit n'est pas réécrit. Une fois par processus et par identité.
  - L'adresse suffit car le royaume refuse les adresses en double.
- **Tests locaux** :
  - 468/468 ;
  - callback `jwt` simulé 5/5 (l'ancien code échoue) ;
  - recollage sur la base locale avec des données fictives 6/6 (affectation, administration et appareil recollés, appareil d'un autre intact) ;
  - image : `/api/sante` 200 au démarrage et au redémarrage, 0 erreur.
- ⚠ **Terrain** : une tablette doit être en ligne une fois pour se reconnecter par Keycloak après la mise en ligne. Les notes en attente restent sur l'appareil.

## 2026-09-27 (suite) — Pastille réseau dans le bandeau, branche `etat-reseau`

- **Cause des blocages confirmée** : l'autorité de la zone est absente du magasin Windows du poste principal. Le service worker ne peut ni se mettre à jour ni joindre le serveur, d'où l'ancienne version et l'effet « comme déconnecté ».
- **Décision utilisateur** : garder le service worker, ajouter une pastille d'état. Supprimer le worker a été écarté, car on perdrait l'ouverture hors ligne du terrain.
- **Livré** : `a4639f3` sur `etat-reseau`, puis **mis en ligne** sur demande (`main` et `prod` = `a4639f3`, `/api/sante` = `2026-09-27.1`). Deux défauts anciens corrigés au passage (purge de `/hors-ligne`, scripts de tête exportés d'un module client). Détail : MEMOIRE § 8 bis.

## 2026-09-27 — Un utilisateur (Axel) ne change plus de page, « comme déconnecté »

- Le serveur de production est sain (`2026-09-25.1`) ; le problème est local à l'appareil. L'utilisateur l'avait déjà réglé chez lui en effaçant les cookies et les données du site.
- **Consigne** transmise pour Axel : synchroniser d'abord, tester en fenêtre privée, puis effacer les données de ce seul site. Aucun code modifié, l'utilisateur n'étant pas devant son poste.
- Analyse, causes probables et correctifs de code proposés : MEMOIRE § 8 bis, « Incident du 2026-09-27 ».

## 2026-09-25 (matin) — Profils EN LIGNE

- `profils` fusionnée dans `main` et `prod` (`2b8d539`). ✅ Le serveur annonce `2026-09-25.1` depuis 08:08, avec `amorce: true` : la base a pris la colonne `profil` et les administrateurs existants sont conservés.
- À faire côté client : attribuer les profils superviseur et officier de marque depuis **Administration → Profils**. Chaque personne doit se reconnecter pour que son profil prenne effet.

## 2026-09-25 (nuit) — Les quatre profils demandés par le client

- **Demande** : vérifier que LEAC répond à quatre profils (superviseur, utilisateur, officier de marque, administrateur), et sinon le faire.
- **Constat avant travaux** :

  | Profil | État |
  |---|---|
  | Utilisateur | ✅ déjà |
  | Superviseur | ❌ n'existait pas |
  | Officier de marque | ⚠ n'existait que comme fonction dans un contrôle ; créer un contrôle était réservé à l'administrateur |
  | Administrateur | ✅ paramétrage (grilles, unités) et profils ; ❌ correction après clôture (tout était verrouillé) ; ❌ création de comptes (Pléiade) |

- **Fait**, sur la branche `profils` (`2b8d539`, version `2026-09-25.1`) : voir la règle 30 et DECISION-036.
  - Schéma : ajout d'une colonne (valeur par défaut `ADMINISTRATEUR`). `db push` au démarrage ne perd rien.
  - Écran « Profils LEAC » ;
  - pastilles et libellés selon le profil ;
  - « Rouvrir pour correction ».
- **Vérifié** : les 4 profils ont été testés en local, sur 4 serveurs successifs (`LEAC_DEV_EMAIL`). Profils attribués par l'écran ; un contrôle créé par l'ODM ; une correction après clôture tracée au journal. Tests : 459/459. `next build` réussi.
- **Données locales** : les profils `sup.test` et `odm.test` sont conservés. Le siège S2 de la démo est rétabli et le contrôle de test supprimé.
- ✅ **Tranché** : pas de création de comptes depuis LEAC. Les comptes restent dans Pléiade (décision de l'utilisateur).
- ⏳ **Reste** : le push (main et prod), par l'utilisateur.

## 2026-09-24 (soir, suite) — Encore un débordement sur iPhone : le NOM DE ZONE du bandeau

- **Capture de l'utilisateur** (iPhone, 16:56, version 2026-09-24.2) : il faut encore glisser à droite. Le bouton de thème du bandeau est **hors de l'écran**.
- **Cause** : sur le serveur, le bandeau affiche le nom de zone (`PLEIADE_ZONE` = « cecpc-div-eval »), **absent en local**. L'élément flex (`min-width: auto`, `nowrap`) ne rétrécit pas, il élargit la page. En plus, `overflow-x: clip` n'est pas compris par tous les navigateurs d'iPhone.
- **Correctif** : nom tronqué, puis masqué sous 420 px ; bandeau borné à l'écran ; `overflow-x: hidden` avant `clip`. Mesuré avec le nom de zone injecté après l'hydratation : **0 débordement sur 48 cas** (iPhone SE, 13, 13 Pro Max, Pixel 7 ; texte à 100 et 150 % ; 6 écrans). ✅ **En ligne à 17:04** (`f13d167`, `2026-09-24.3`).
- ⭐ **Leçon** : l'environnement local **diffère du serveur** par ses variables d'instance (`PLEIADE_ZONE`, …) qui ajoutent du contenu. Tester l'affichage **avec les valeurs du serveur**.

## 2026-09-24 (soir) — Débordement sur vrai téléphone + LEAC v2 (DESIGNER, locale)

- **Signalement** : sur un vrai téléphone, la page est plus large que l'écran et il faut glisser pour finir les phrases.
- **Cause** (non vue par mes mesures de l'après-midi, faites sans émulation mobile ni texte agrandi) : reproduite en émulant un **Pixel 7 avec le texte système à 150 %**. Six sources :
  - des mots sans espace ;
  - un `<select>` qui prend la largeur de sa plus longue option (son `maxWidth` est en rem et grandit avec le texte) ;
  - `fieldset` et éléments de grille bloqués à leur largeur de contenu ;
  - la barre du bas et le menu « Plus » ;
  - la case `sr-only` (position absolue) des filtres, qui échappait à sa ligne défilante.
- **Correctif** : `67689fb` sur `main`, **local, non poussé**, avec un filet `overflow-x: clip` sous 640 px. Résultat : 22/22 en taille normale et 33/33 avec le texte agrandi, iPhone 13, Pixel 7 et iPhone SE confondus.
- ⭐ **Leçon** : mesurer un rendu mobile **avec `devices[…]` de Playwright** (viewport méta, zoom) **et avec le texte agrandi**. Un simple viewport étroit ne voit pas ces débordements.
- **Demande** : que DESIGNER conseille « sur la totalité de ses capacités, même l'architecture », pour une interface plus fluide, plus esthétique, plus pro. **En local d'abord.** Proposition : `DESIGNER\AVIS\2026-09-24_LEAC\PROPOSITION_V2.md`. Réalisé sur la branche `refonte-v2` (`576de5e`) : détail en MEMOIRE §7.
- ✅ **Validé et mis en production** (« c'est parfait, tu peux publier ») : `ffc8b73`, version `2026-09-24.2`, **en ligne à 16:54** (`/api/sante`, `/connexion` 200, `/controle/x/grilles` 307). Le diff ne touche que l'affichage : aucune donnée, synchronisation ni API.

## 2026-09-24 — Refonte visuelle et responsive avec l'agent DESIGNER (locale, non poussée)

- **Demande** : *« optimiser l'application LEAC qui est vraiment compliquée à assimiler visuellement ; travailler le responsive design : une version tablette, une version téléphone et une version ordinateur »* — en travaillant avec le nouvel agent **DESIGNER**.
- **Audit** (`DESIGNER\AVIS\2026-09-24_LEAC\AVIS.md`, captures `avant\` et `apres\`) : 8 écrans × 4 tailles (1440 × 900, 820 × 1180, 1180 × 820, 390 × 844), mesures relevées dans la page. Le parti pris §7 **validé le 17/09 reste la référence**. Problèmes relevés :
  - D1 : pas de navigation commune (rangées de 3 à 6 boutons dans un ordre différent par écran, sans indication de l'emplacement) — gravité 4 ;
  - D2 : sur téléphone, le contenu commence à 540 px sur 844 et la grille **déborde de 83 px** — gravité 4 ;
  - D3 : aucune adaptation à la taille d'écran (une colonne de 768 px partout) ;
  - D4 : grille **centrée** (piège `.frappe`) ;
  - D5 : boutons de navigation petits ;
  - D6 : vocabulaire incohérent (Bilan / Réunion quotidienne, CRF / Compte rendu) ;
  - D7 : accueil.
- **Réalisé** : R1 à R6 (détail en MEMOIRE §7), commit `b27b171` sur `refonte-design`. Vérifié :
  - tsc et lint propres, 452/452 ;
  - essai au téléphone : « Plus » s'ouvre, se referme au choix et prend le nom de la page ; la destination active suit la page ;
  - 0 px de débordement aux 4 tailles.
- Vu en passant, **déjà connu** : l'erreur de page en dev `Function statements require a function name` (notée le 22/09), sans lien avec la refonte.
- ✅ **Mise en production** (autorisation : « tu peux tout envoyer sur le serveur ») : `6701831`, version `2026-09-24.1`, **en ligne à 15:56** (`/api/sante`, `/connexion` 200, `/controle/x/grilles` 307). **Question posée par l'utilisateur : les données en cours sont-elles perdues ? Non, vérifié avant l'envoi.** Le diff ne touche que 11 fichiers d'écran et de style : ni `prisma`, ni `offline/`, ni `sync/`, ni les API. La base IndexedDB reste en v4. Le service worker ne purge que les caches `leac-*` d'autres versions, jamais IndexedDB. La base serveur est conservée.
- ~~Prochaine étape~~ (faite) : l'utilisateur regarde en local (`http://localhost:3700`, contrôle de démonstration), puis décide de fusionner dans `main` et de pousser `prod`. Idée non réalisée : une grille en **deux colonnes** sur ordinateur (arbre à gauche, critères à droite).

## 2026-09-22 (suite) — Retour du premier utilisateur sur le serveur : « la grille arrive trop tôt »

- **Nouveau besoin, remonté du terrain** (utilisateur ayant testé LEAC déployé) : quand un contrôleur entre dans un exercice, il tombe **directement sur la grille d'évaluation**. Or, sur le terrain, il ne sait pas retrouver *la bonne* grille parmi tout ce qui existe (14 domaines, jusqu'à 1 352 critères). Ce dont il a besoin **d'abord**, c'est d'un **carnet de terrain** : plusieurs **notes texte** et **mémos vocaux** (tablette/téléphone) pris au fil de la journée, comme pense-bêtes ; **le soir**, contrôle terminé, il relit/réécoute ses notes et va noter dans les grilles.
- **Demande exacte** : *« la première fenêtre qui apparaît lorsqu'on entre dans un exercice ne soit pas la grille mais plutôt une fenêtre qui nous permette d'enregistrer plusieurs textes/vocaux — est-ce réalisable ? »*
- **Réponse donnée : OUI, réalisable avec l'existant**, sans nouvelle brique d'infrastructure :
  - une note texte = une **opération de journal** comme une observation (`Carnet#<cycle>|<auteur>#<noteId>`), donc **hors ligne, fusionnée, compactée** par la même mécanique ;
  - un vocal = **`MediaRecorder`** du navigateur (fonctionne sur Android/Chrome et iOS/Safari ≥ 14.5, en HTTPS — ce que Pléiade impose déjà), octets en **IndexedDB** puis remontés **exactement comme les pièces jointes** (table `pieces` + `/api/pieces`, description au journal, octets à part) ;
  - le lien note → grille : la **recherche existante** (`domaine/recherche.ts`) ; depuis une note, un bouton « aller à la grille » ouvre la notation avec la note affichée en bandeau, et une note peut être **rattachée à un critère** une fois la mention posée ;
  - l'écran d'entrée devient le carnet ; la grille devient un onglet/bouton « Grilles ».
- ⚠ **Deux points à faire trancher par le CECPC, dits à l'utilisateur** : (1) **classification** d'un enregistrement audio pris dans un PC en exercice — même question que pour les photos (règle 28, `LEAC_PIECES_JOINTES`) ; le carnet **texte** ne pose pas cette question et peut être livré d'emblée, le **vocal** derrière le même interrupteur ou un `LEAC_VOCAUX` ; (2) **transcription** automatique des vocaux : rien n'existe sur le serveur (Whisper hors ligne serait un chantier à part) — dans un premier temps, la note vocale se **réécoute**, elle ne se lit pas.
- **Volume** : 1 minute d'audio Opus ≈ 0,5 à 1 Mo ; plafond proposé **3 minutes** par mémo (< 5 Mo, sous le plafond actuel des pièces).
- **Décision utilisateur, dans la foulée** : *« les notes textuelles et vocales restent dans l'appareil utilisé et ne vont pas sur le serveur »*. Cela retire le journal et la route des pièces du dessin, et règle la classification : rien ne quitte la tablette.
- **Construit le jour même** (Règle 29 de la mémoire) :
  - `domaine/carnet.ts` (pur : formats, durée, tri « à traiter d'abord », validation, dates) — **17 tests**, 448/448 au total ;
  - base locale **v4** : table `carnet` (`id, [controleId+auteurId], controleId`), octets du vocal dedans, **jamais lue par `sync/`** ; `offline/useCarnet.ts` = la seule écriture locale qui contourne `depot.ecrire`, documentée comme telle ;
  - `controle/[id]/page.tsx` = **le carnet** (nouvelle note, enregistreur, liste à traiter / traitées, « Noter dans la grille », légende d'un vocal, suppression en deux gestes, avertissement « ces notes restent sur cet appareil ») ; `enregistreur.tsx` (`MediaRecorder`, compteur, arrêt à 3 min, repli `<input capture>`, `useSyncExternalStore` pour ne pas rendre différemment serveur/client) ; `lecteur-vocal.tsx` (URL `blob:` locale) ;
  - la grille déplacée sous **`/controle/[id]/grilles`** (`notation.tsx` dans un `Suspense`, `?note=` épingle la note en tête, bouton « Traitée » ferme et marque) ; lien « Carnet » ajouté ; les six écrans qui renvoyaient « Grilles » vers la racine pointent vers `/grilles`.
- **Vérifié dans un navigateur** (Chromium, micro simulé) — **21/21** : entrée = carnet, note texte gardée et brouillon vidé, vocal de 2 s → 28 Ko `audio/webm;codecs=opus` dans la table `carnet`, lecteur sur URL `blob:`, **aucune requête** `/api/pieces` ni `/api/echange` pendant le parcours, survie au rechargement, grille ouverte avec la note épinglée, « Traitée » la fait passer sous les notes à traiter, tableau de bord → `/grilles`.
- ⚠ **Deux choses vues en passant, pas corrigées** : (1) à la **première ouverture** d'un contrôle sur un appareil, `amorcage.tsx` échange puis **recharge la page** — une note tapée ou un vocal lancé dans cette seconde-là serait perdu (comportement existant, le même pour la grille) ; (2) une erreur de page `Function statements require a function name` apparaît en dev dès `/`, avant tout code du carnet — à regarder à part.
- Lint et `tsc` propres. Commit `89122f2` sur `main` ; **`prod` n'est pas poussée** (autorisation par geste).

### Mise en PRODUCTION — `2026-09-22.1` en ligne

- **Autorisation utilisateur** : *« je veux que tu push cette maj sur le serveur de sorte à ce que les utilisateurs puissent y avoir accès »*.
- Version marquée **`2026-09-22.1`** (`src/lib/version.ts`, la même que `/api/sante` et le service worker), commit `71df2fc` ; `prod` avancée **en avance rapide** depuis `main` (elle reprend au passage le bouclier Pléiade et les écrans d'administration restés sur `main`).
- **Mesuré sur le serveur**, ⭐ par la marque de version et non par une empreinte d'assets (leçon du 21) : `/api/sante` rend `{"ok":true,"app":"LEAC","amorce":true,"version":"2026-09-22.1"}` **140 s** après la poussée ; `/connexion` → 200 ; `/controle/<id>` **et** `/controle/<id>/grilles` → 307 vers `/connexion` — la **nouvelle route des grilles existe** (une route inconnue rendrait 404) et le sas fonctionne toujours.
- ⏭️ **À dire aux contrôleurs avant le prochain contrôle** : **installer LEAC sur l'écran d'accueil de la tablette**, faute de quoi le navigateur peut effacer le carnet s'il manque de place — et le carnet est la seule copie.

### Dans la foulée — le plafond de 3 minutes des vocaux est LEVÉ

- **Demande utilisateur** : *« vu que les vocaux ne partent pas sur le serveur, est-ce qu'on peut enlever la limite des 3 min ? »* — fondée : les 3 min et les 5 Mo étaient repris du plafond des **pièces jointes**, qui, elles, remontent au serveur (bande passante, disque, classification). Un vocal du carnet ne remonte nulle part.
- **Fait** : plus aucun plafond, ni de durée, ni de taille. Plus d'arrêt automatique de l'enregistreur.
- ⚠⚠ **Le point qui comptait vraiment** : l'ancien code refusait un vocal trop long/lourd **après** l'enregistrement. Les octets n'existent qu'une fois le micro coupé — ce refus **détruisait** ce que la personne venait de dire. Un vocal n'est désormais refusé que s'il est **vide** (rien capté), le seul cas où il n'y a rien à perdre.
- **Ce qui remplace la limite, puisqu'il en reste une, réelle : la place de l'appareil.**
  - l'écran **affiche** ce que le carnet occupe (« 34 Mo sur l'appareil ») ;
  - `navigator.storage.persist()` est demandé à l'ouverture — sans cela, IndexedDB est « best-effort » et le navigateur peut **évincer** le stockage quand l'appareil manque de place. Pour le reste de LEAC ce serait réparable (le serveur a tout) ; **le carnet n'existe que là** ;
  - un refus de persistance est **dit à l'écran** ; un `QuotaExceededError` rend un motif clair (« supprimez des vocaux déjà traités ») au lieu d'un écran qui n'affiche rien de nouveau ;
  - le compteur de l'enregistreur montre la **durée et la place prise en direct**, et `formatDuree` passe en `h:mm:ss` au-delà de l'heure.
- **Vérifié** : 452 tests (dont 40 min / 2 h acceptés, formats de durée et de taille) ; **parcours navigateur dédié**, mené en temps réel — ⚠ c'était le seul contrôle probant, un essai de 10 s aurait passé avec l'ancien code aussi :

  | à | état | compteur | capté |
  |---|---|---|---|
  | 60 s | enregistre | 1:00 | 940 Ko |
  | 120 s | enregistre | 2:01 | 1,8 Mo |
  | **181 s** | **enregistre** *(l'ancien code coupait ici)* | **3:03** | 2,8 Mo |
  | 200 s | enregistre | 3:21 | 3,1 Mo |

  En base : `dureeS: 201`, 3 228 701 octets, cohérents avec la durée. Soit ~0,95 Mo par minute en webm/opus — une demi-heure de dictée ≈ 29 Mo.
- 🔴 **Ce que la mesure a appris, et que je croyais acquis** : `navigator.storage.persist()` est **REFUSÉ** par un navigateur ordinaire (Chromium le réserve aux sites installés ou très fréquentés). Mon contrôle affirmait l'inverse — **c'est le test qui avait tort, pas le produit** : LEAC ne décide pas, il demande. Corrigé : le test vérifie désormais ce que LEAC **contrôle** (il demande, et il DIT le refus), et un contrôle dédié éprouve la bannière d'alerte.
- ⭐ **Conséquence pratique à faire remonter au terrain** : LEAC a un manifeste et un service worker, donc **installer LEAC sur l'écran d'accueil de la tablette suffit à obtenir la persistance**. C'est ce que la bannière conseille désormais, en toutes lettres. Sans installation, le navigateur peut effacer le carnet s'il manque de place — et le carnet est la seule copie.

## 2026-09-22 — « Je n'arrive pas à me connecter à LEAC » : la chaîne est SAINE de bout en bout (vu du dehors)

- **Signalement utilisateur** (en passant, avant de reprendre MELMIL) : impossible de se connecter à LEAC sur le serveur.
- **Mesuré, sans rien toucher** — tout répond, et correctement :
  - `GET /api/sante` → `{"ok":true,"app":"LEAC","amorce":true,"version":"2026-09-21.2"}` ;
  - `/` → **307** vers `/connexion` ; `/connexion` → **200**, écran « LEAC · Se connecter · compte de la zone » ; `/administration/administrateurs` → **307** vers `/connexion` (le sas fonctionne) ;
  - **certificat** servi : `CN=*.cecpc-div-eval.pleiade.internal`, SAN couvrant l'hôte — valide jusqu'en 2036, même forme que les zones qui marchent ;
  - royaume **`cecpc-div-eval`** présent (découverte OIDC 200, émetteur `https://auth.cecpc.internal/realms/cecpc-div-eval`) ;
  - ⭐ **le client Keycloak de l'instance existe et est le bon** : en faisant parler LEAC lui-même (POST de connexion avec jeton CSRF), il part sur `client_id=**leac-leac**` — c'est le nommage `<type>-<instance>` de `clientDeInstance`, et ce client **accepte** l'adresse de retour `…/api/auth/callback/keycloak` (page de connexion Keycloak rendue, 200) ;
  - **cecpc Connect** est déclaré pour cette zone (`cecpc-connect` accepte `…/realms/cecpc-div-eval/broker/cecpc/endpoint` → 200), et la page de connexion du royaume porte bien le bouton `broker/cecpc/login`.
- ⚠ **Piège de mesure écarté** : `GET /api/auth/signin/keycloak` rend `error=Configuration` sur LEAC… **et sur les deux instances d'eho qui marchent**. C'est Auth.js qui exige un POST avec jeton CSRF, pas un défaut. Sans la comparaison, j'aurais conclu à une mauvaise configuration.
- **Ce que je ne peux pas voir du dehors, et qui reste à vérifier avec l'utilisateur** : (1) ce que l'écran affiche exactement au moment de l'échec (page Keycloak ? erreur LEAC ? boucle vers `/connexion` ?) ; (2) s'il a un **compte dans le royaume `cecpc-div-eval`** ou s'il entre par « cecpc » ; (3) le cas échéant, les journaux du conteneur (`AUTH_SECRET`, `KEYCLOAK_CLIENT_SECRET`) — une boucle de retour à `/connexion` après une connexion réussie pointerait vers le secret de session.

## 2026-09-21 (suite 2) — 🔴 Défaut LATENT réparé : le volume de données d'une instance appartient à root

Trouvé sur eho (« EACCES: permission denied, mkdir '/app/data/uploads' » à la
première écriture disque sur le serveur), **LEAC avait exactement le même
schéma** : image en `USER nextjs`, montage `./data:/app/data` d'un dossier
**créé par l'orchestrateur en root** — le `chown` fait dans l'image est
recouvert par le montage. Personne ne l'avait vu parce que LEAC n'avait encore
rien écrit sur disque en production : les **pièces jointes** (`DATA_DIR/pieces`)
auraient échoué au premier téléversement réel.

- **Correctif, identique dans les deux dépôts** : plus de `USER nextjs` dans le
  `Dockerfile` ; `apk add su-exec` ; l'entrypoint démarre **root**, fait
  `mkdir -p` + `chown -R nextjs:nodejs /app/data`, puis
  `exec su-exec nextjs "$0" "$@"` — tout le reste (migrations, serveur) tourne
  sous `nextjs` comme avant.
- ⚠ **À tester sur un volume pré-rempli par root**, jamais sur un volume neuf :
  un volume neuf est initialisé depuis l'image, donc déjà bien possédé, et le
  cas du serveur ne s'y reproduit pas.
- Version **`2026-09-21.2`**, poussée `main` + `prod`, **en ligne** sur
  `leac.cecpc-div-eval`.
- ⚠ Signalé pour les apps de Xavier (press, messagerie, social) : même schéma
  probable. Alternative côté plateforme : que Pléiade `chown` le dossier `data`
  à l'uid de l'app à la création de l'instance.

## 2026-09-21 (suite) — ⭐ Le bouclier Pléiade administre aussi LEAC

**Déclencheur** : Axel, dans un groupe « admin » sur Pléiade, vu comme simple
utilisateur par LEAC. Vérifié : c'était **le fonctionnement décidé le 18/09**
(LEAC ignore les rôles Pléiade ; administrateurs = `administrateurs_entite`,
amorcés par `LEAC_ADMINISTRATEURS` ou promus à la main). Sur
`leac.cecpc-div-eval`, `/api/sante` → `amorce: true`, version `2026-09-19.1` ;
donc l'adresse amorcée existe et c'est le **rattachement par adresse** qui
échoue (adresse différente, compte recréé, ou autre instance au champ vide —
⚠ Pléiade écrit `LEAC_ADMINISTRATEURS=` vide à la création, ce qui ÉCRASE
l'`ENV` de l'image).

**Décision utilisateur** : *« je veux que LEAC fonctionne également avec le
bouclier Pléiade… comme les autres applis »*. Mise en œuvre sans défaire le
18/09 : la vérité reste dans LEAC, **le bouclier INSCRIT** :

- `lib/zone/bouclier.ts` (pur, testé) : `ROLE_ADMIN_BOUCLIER = "admin"`,
  `porteLeBouclier(roles)`, `PROMU_PAR_BOUCLIER`, `inscritParLeBouclier(promuPar)`.
- `estAdministrateur` : après amorçage et rattachement, si le jeton porte
  `admin` (royaume ou client `leac`) → **création d'une ligne** (adresse,
  identité, `promuPar` = bouclier, journal `administrateur.bouclier`) puis
  `true`. Sans adresse dans le jeton ou ligne déjà tenue : `true` quand même,
  c'est Pléiade qui a donné le rôle.
- `revoquer` **refuse** une ligne du bouclier (elle reviendrait à la connexion
  suivante) : le droit se retire dans Pléiade. Écran : pastille « bouclier
  Pléiade », bouton Révoquer désactivé, texte d'en-tête réécrit.
- `catalog/leac.yml` : rôle `admin` **réhabilité** (« Administration »), bloc
  de commentaire réécrit. Le rôle client existait déjà dans Keycloak (jamais
  retiré) → aucune synchronisation de zone nécessaire.
- ⚠ Les rôles sont lus **à la connexion** : un rôle donné après coup vaut à la
  connexion suivante → dire à l'utilisateur de se déconnecter/reconnecter
  (déconnexion complète en place depuis ce matin).
- Version `2026-09-21.1`. Tests **430/430** (dont 8 sur le bouclier), tsc, lint, build. **Commit `dfae88f`, `main` + `prod`** ; catalogue `pleiade-platform` `32c5f16` (`main`).

## 2026-09-21 — Mise à jour des 12 dépôts Pléiade, sans rien casser

Demande utilisateur : être à jour sur les push/pull par rapport aux travaux
de Xavier, sans conflit. `git fetch` partout. Rapatriés en avance rapide :
`app-press` (2), `app-social` (2), `eho` main (4, branche `MEYTRE`
conservée), `mastorion` main (12), `app-leac` prod local (17).
`pleiade-platform` : 10 commits de Xavier (icônes d'instance, favicon via
Traefik, champs d'env éditables). ⚠ Les « fichiers locaux de Xavier »
(`package-lock.json`, `public/style.css`) que je protégeais depuis le 18/09
**n'étaient pas de lui** : artefacts de MON poste (lock resynchronisé par npm,
Tailwind non minifié écrit par `npm run dev`, tous deux du 18/09 15h03).
Jetés (`git checkout --`), catalogue mis de côté, avance rapide, catalogue
remis : 0 conflit. Rien de Xavier ne touche LEAC. Puis, sur feu vert, le
catalogue (2 variables) commité et poussé : `pleiade-platform` `bbb3d4e`.

---

## 2026-09-19 (suite) — ⭐⭐ Les six lots du comparatif ÉVAL-PC, mis en place EN LOCAL

Feu vert utilisateur : « je t'autorise à mettre en place tous les lots
PROPOSÉS ». Neuf commits sur `app-leac` (`28df915` → `1045719`), **poussés sur feu
vert : main + prod, en ligne à t+4 min, version `2026-09-19.1`** (image
reconstruite, `db push` passé sans perte). 422/422 tests, tsc, lint,
toutes les pages en 200 sur le serveur de dev, vérification mobile
320/375/414 sans débordement.

- **A — saisie** : recherche plein texte + filtres (non notés, par mention,
  complément demandé) sur la grille et l'onglet Critères ; mode « un par un »
  (gros boutons, prochain non noté, sommaire, raccourcis 1-8 / ← → / N / 0) ;
  écran Affichage (taille, contraste, mouvement, densité) appliqué avant le
  premier rendu ; `lib/version.ts` unique.
- **B — lecture** : tableau de bord analytique (radar, forts/faibles avec
  couverture, critères critiques ≤ Défaillant, top/bottom 5, distribution des
  mentions, évolution par CYCLE — l'axe du temps de LEAC, pas la date) en SVG
  sans bibliothèque ; grille physio réelle au journal + 3 lectures ; page
  Mandat lisible par toute l'équipe ; lecture des notes en module pur partagé.
- **C — droits fins** : `MembreEquipe.droits` (écrit / lit / rien par domaine)
  par-dessus la fonction ; grille en lecture affichée sans se noter ; **politique
  de réception côté serveur** (`sync/politique.ts`) : chaque opération jugée
  selon SON auteur ; refus conservé + motif, accusé, non redistribué, dit à la
  tablette. Les verrous d'écran ne sont plus les seuls.
- **D — comparaison** : `Controle.bilanFinal` figé à la clôture ;
  `/administration/comparaison` (2-4 contrôles clôturés, tableau, barres,
  radar superposé, .xlsx navigateur, impression). On compare l'ANNONCÉ.
- **E — socle hors ligne** : service worker versionné servi par `/sw.js`
  (route), navigations réseau→cache, `/hors-ligne`, mise à jour jamais
  silencieuse, manifest + icônes ; **démo** en un clic (1 482 opérations,
  reproductible, DÉMO partout, supprimable) ; `npm run verifier:mobile`
  (Playwright dev-dep, navigateur hors image) ; **amorçage** : première
  ouverture d'un contrôle = échange automatique (défaut vu sur la démo).
- **F — sur décision CECPC** (hypothèses écrites, éteintes par défaut) :
  **grilles importables** (.xlsx via le lecteur des classeurs N4, .json LEAC,
  rapport, activation = second geste, grille FIGÉE par contrôle,
  `useDomaines()` partout) ; **pièces jointes** (`LEAC_PIECES_JOINTES=1`,
  PNG/JPEG/PDF aux octets, 5 Mo, description au journal / octets à part,
  purge avec le contrôle) ; **auto-évaluation** (`LEAC_AUTO_EVALUATION=1`,
  `Controle.mode`, référents d'unité, étanchéité `peutEntrer`).
- ⚠⚠ **Défaut de données révélé** par la relecture des grilles : **9 codes de
  critère en double dans le classeur N4** du CECPC (`2.3.2.x` codés `1.3.2.x`
  dans « Travail collectif », `1.8.3.x` codés `1.8.2.x`). Deux critères
  partageaient une clé de note. Réparé (`~2` sur le second, le premier garde
  son identifiant), affiché à l'administrateur (écran Grilles), **à corriger
  dans le classeur par le CECPC**.
- ⚠ `pleiade-platform/catalog/leac.yml` : deux variables ajoutées EN LOCAL,
  non commitées (dépôt de Xavier, fichiers locaux intacts).
- Reste : pousser sur feu vert (main puis prod, `db push` ajoute 3 tables /
  5 colonnes sans perte) ; commiter le catalogue Pléiade ; arbitrages CECPC.

---

## 2026-09-19 — Comparatif avec ÉVAL-PC (spécification d'un client)

Reçu `REFERENCES/2026-09-19_EVAL-PC_prompt-creation_client.md` : prompt de
création d'une app « ÉVAL-PC » produit par un client avec une IA sur son
téléphone. Demande : **comparer sans rien modifier**, proposer ce qu'on
absorbe. Résultat : `COMPARATIF_EVAL-PC_2026-09-19.md` — 15 idées classées
(droits par domaine réglables, mode un-critère-à-la-fois, recherche/filtres,
tableau de bord analytique, comparaison de contrôles, pièces jointes, grilles
importables, préférences d'affichage, PWA, démo, auto-évaluation…), 8 points à
**ne pas** reprendre (échelle chiffrée, seuils de niveau divergents de la N4,
plafond label B vs C, snapshots, « synchroniser = recharger », mention DR par
défaut, JSON de notes), 5 arbitrages CECPC, 6 lots A→F. ⚠ Constat utile :
ÉVAL-PC révèle un manque de **notre** socle — pas de service worker, l'app
ne s'ouvre pas sans réseau si les pages ne sont pas déjà chargées (lot E).
En attente de la décision de l'utilisateur.

---

## 2026-09-18 (suite 12) — ⚠ Texte perime sur l'ecran de synchronisation

Question de l'utilisateur : « si j'appuie sur Synchroniser, ca ne se synchronise
pas sur le serveur ? ». **Si** : `echanger()` → `POST /api/sync` → operations
rangees en base, celles des autres appareils rapatriees (branche le 2026-09-17
suite 4). Mais le paragraphe au-dessus du bouton disait encore « le serveur de
zone n'est pas encore branche, ce bouton simule… » — texte de la maquette,
oublie quand le tuyau a ete pose. **Lecon** : un texte d'ecran est une promesse ;
quand une simulation devient reelle, relire TOUT ce que l'ecran affirme, pas
seulement le code. Corrige (texte + version 2026-09-18.7), tsc + lint OK.
Pousse sur feu vert : `e2fe00e` main + prod, en ligne a t+2 min (2026-09-18.7).

---

## 2026-09-18 (suite 11) — Supprimer un controle (§ V.A.7)

Demande utilisateur (controle d'essai « antares 21RIMa » a effacer). Fait :
`depot.supprimerControle` — **seulement en INITIALISATION ou EN_PREPARATION**
(un controle parti porte le travail d'une equipe : il se cloture, puis
s'archive), journalise AVANT la suppression ; action serveur gardee par
`peutParametrer` **et** par l'intitule retape, verifie cote serveur ;
section « Supprimer ce controle » en bas de l'onglet Initialisation, avec
confirmation maison (jamais `confirm()`). Cascade **prouvee** sur la base
locale : equipe, appareils, operations, cycles → 0 orphelin. 312/312, tsc,
lint, build. Pousse sur feu vert : main + prod, version 2026-09-18.6.

---

## 2026-09-18 (suite 10) — Composer l'equipe en CHOISISSANT parmi les comptes de la zone

**Demande utilisateur** : au lieu de taper une adresse, selectionner des
personnes deja enregistrees comme utilisateurs de la zone dans Pleiade ; creer
3 comptes de test « controleur 1/2/3 ».

- **Comptes de test** : impossible pour moi (creation = Pleiade, session
  d'operateur) — a faire par l'utilisateur ou Xavier ; ils apparaitront dans la
  liste automatiquement.
- **La liste** : le blocage etait que la seule route de Pleiade listant les
  comptes est reservee a l'operateur ET rend `rawPassword`. Ajoute a Pleiade
  **`GET /api/internal/zones/:zone/users`** (cle de service via `cleZoneValide`,
  que Xavier avait factorisee ; **sans mot de passe** ; comptes de service et
  desactives ecartes ; `?group=<nom>` optionnel). Cote LEAC : `lib/zone/comptes.ts`
  (cache 30 s, repli sur la derniere liste connue, vide hors zone), `Membre`
  affecte avec `identityId` **lie tout de suite** quand le compte est choisi ;
  saisie d'adresse conservee en repli. Les deux formulaires (creation,
  parametrage/Siege). ⚠ L'identite choisie est **relue aupres de Pleiade** cote
  serveur — on ne fait pas confiance au navigateur. Catalogue :
  `LEAC_GROUPE_UTILISATEURS` (vide = tous).
- Verifie : 312/312, tsc (les deux depots), lint, build ; en local (hors zone)
  le formulaire retombe sur la saisie d'adresse. **La route Pleiade n'est pas
  testable d'ici** (pas d'orchestrateur local) : a verifier sur le serveur.

✅ Pousse sur feu vert : `pleiade-platform` `e4b1bb7..069b48d` (catalogue +
route, rebase, fichiers locaux de Xavier intacts) ; `app-leac` `f2e6cde`
main + prod, **en ligne a t+3 min** (version 2026-09-18.5). La route Pleiade
repond 401 sans cle depuis l'exterieur — elle est bien deployee.

---

## 2026-09-18 (suite 9) — Design : polices embarquees, bandeau, mode sombre, mentions compactes

Avis rendu a l'utilisateur (« optimal ou mieux ? ») : socle sain (contraste,
48 px, clair par defaut, couleurs daltonien-compatibles) mais **deux promesses de
la charte non tenues** et une nudite visuelle. Les quatre points, sur son feu vert :

1. **Polices** — Archivo et JetBrains Mono etaient declarees sans jamais etre
   chargees (chacun voyait sa police systeme). Embarquees via
   `@fontsource-variable/*` (OFL), importees au layout racine : aucun CDN,
   compatible reseau ferme. Verifie dans le bundle (`.next/static/media/*.woff2`).
2. **Mode sombre** — les jetons `[data-theme="sombre"]` existaient sans bouton.
   `lib/ui/bascule-theme.tsx` : choix explicite memorise (`localStorage`),
   applique avant le premier rendu par un script dans `<head>` (pas d'eclair
   blanc). ⚠ On ne suit PAS `prefers-color-scheme` : clair par defaut, doctrine.
3. **Bandeau** — `lib/ui/bandeau.tsx` sur toutes les pages : graphite, nom en
   chasse fixe espacee, zone (`PLEIADE_ZONE`), bouton de theme. `.frappe-vide`
   passe au trait fort (un bouton ne doit pas ressembler a un cadre) ;
   `.sur-titre` a 0,1 em (ne passe plus sur deux lignes au telephone).
4. **Mentions compactes** sous 480 px — deux rangees de quatre, mots abreges
   (`Mention.court`, affichage seulement), le mot choisi ecrit en entier sous la
   rangee. Sur tablette, rien ne change.

306/306, tsc, lint, build. **Non commite** — en attente du feu vert.

---

## 2026-09-18 (suite 8) — ⚠ Defaut d'amorcage : sans entite, personne n'etait administrateur

Capture de l'utilisateur : Axel toujours simple utilisateur apres l'amorcage.
Cause : `estAdministrateur` cherchait une **entite existante** avant de semer ;
sur le serveur il n'y en avait **aucune** (l'ancienne version ne la creait qu'a
la premiere synchronisation, jamais faite). Rien n'etait seme, et le refus
etait silencieux. ⚠ Lecon : **le premier administrateur ne peut pas dependre
d'un geste que seul un administrateur peut faire.** Corrige : `entiteCourante()`
(cree si absente) dans `estAdministrateur`, `listerAdministrateurs`,
`promouvoir` ; l'echec de lecture est journalise. Marque `version` sur
`/api/sante`. Commit `97d2c3c`, `main` + `prod`, **en ligne a t+2 min**.

---

## 2026-09-18 (suite 7) — Axel administrateur de LEAC, par defaut de l'image

L'utilisateur n'avait pas ses identifiants Pleiade (en remote depuis son
telephone). Refus de chercher des identifiants ; voie legitime trouvee par le
code : `ensureDiscoveryEnv` ne complete que le bloc `PLEIADE_*`, donc le `.env`
de l'instance (17/09) ne porte pas `LEAC_ADMINISTRATEURS` — une valeur posee
dans l'IMAGE (`ENV` du Dockerfile) s'applique, et la variable d'instance
primera des qu'elle sera reglee.

⚠ Le garde-fou de l'outil a d'abord **refuse** l'edition (octroi de droits) ;
arret, explication, **confirmation explicite** de l'utilisateur (« admin
uniquement sur LEAC, pas sur Pleiade » — exact), puis edition. Commit
`57cd3c9`, `main` + `prod`. `/api/sante` rend desormais `amorce` (booleen) :
**`true` sur le serveur a t+2 min**. Axel sera inscrit a sa prochaine
connexion (liaison par adresse, insensible a la casse).

---

## 2026-09-18 (suite 6) — Mise en production de la version « habilitations »

**Autorisation explicite de l'utilisateur** : *« tu peux faire le 1 et 3, je
m'occupe de 2 et 4 »* (1 = catalogue Pléiade, 3 = `prod` ; 2 = variable
`LEAC_ADMINISTRATEURS`, 4 = second compte de test).

| | Geste | Résultat |
|---|---|---|
| 1 | `pleiade-platform` : **`catalog/leac.yml` seul** commité (`e4b1bb7`), **rebasé** sur 2 commits de Xavier (`b083a9f`, `a3e41bd` — identité de zone, ne touchent pas le catalogue LEAC), `--autostash` pour ses fichiers locaux non miens (`package-lock.json`, `public/style.css`, laissés tels quels), poussé `a3e41bd..e4b1bb7` | Pléiade se redéploie avec `LEAC_ADMINISTRATEURS` déclarée et `adminPath: /administration/administrateurs` |
| 3 | `app-leac` : `origin/main:prod`, avance rapide `a747d4f..74f066e` (2 commits : synchronisation + habilitations/corrections/unités) | Le runner construit l'image (tests dans le build) |

⚠ Vigilance connue : `/usr/local/sbin/pleiade-promouvoir` + sudoers doivent
connaître `leac` pour que la nouvelle image **remplace** l'instance (note du
17/09). Sonde de version : `GET /administration/administrateurs` sans session
→ **404** = ancienne version, **307** = nouvelle. Surveillance lancée. **Résultat : nouvelle version en ligne à t+6 min** (sonde 404 → 307, `/api/sante` 200). Pléiade a rendu 404 une minute à t+1 (son propre redéploiement), puis 302. ✅ La promotion a bien remplacé l'instance : le point « pleiade-promouvoir / leac » est réglé en pratique.

⏭️ Côté utilisateur : renseigner `LEAC_ADMINISTRATEURS` sur l'instance (puis
la **redémarrer** — une variable d'environnement se lit au démarrage du
conteneur), créer un second compte de zone, l'affecter depuis LEAC.

---

## 2026-09-18 (suite 5) — Déconnexion complète, et premier commit de la journée

**Remarque utilisateur** : pas de bouton de déconnexion ; sur le serveur, connecté
en Axel, impossible de changer de compte pour essayer.

⚠ Le manque était double : pas de bouton, et un `signOut` NextAuth seul (ce que
fait eho) **ne clôt pas la session Keycloak** — « se connecter » rouvre le même
compte sans rien demander. Fait : `lib/zone/deconnexion.ts` ferme LEAC puis
redirige vers `end_session_endpoint` avec `id_token_hint` (gardé dans le jeton
NextAuth depuis le `jwt` callback) + `client_id` + `post_logout_redirect_uri`
= `/connexion`. Le motif `https://<app>/*` déclaré par Pléiade sur les clients
d'app couvre ce retour. Bouton sur l'accueil. ⚠ Non éprouvé de bout en bout
en local (le poste passe par `LEAC_DEV_USER`, sans Keycloak) — à vérifier sur
le serveur au prochain déploiement.

**Commit + push `main` d'`app-leac`** autorisés par l'utilisateur, sous
condition de conformité et de non-régression. Vérifié avant : 306 tests, tsc,
lint, build, **image Docker construite localement** (tests exécutés dans le
build). ⚠ `main` **ne déploie pas** : seule `prod` déploie. ⚠ `pleiade-platform`
(`catalog/leac.yml`) **non poussé** : `main` y déploie sans garde-fou, et le
dépôt porte des modifications locales qui ne sont pas de moi
(`package-lock.json`, `public/style.css`) — demande d'autorisation spécifique.

---

## 2026-09-18 (suite 4) — ⭐ Référentiel des unités, insignes, historique par régiment

**Demande utilisateur** : *« que l'administrateur puisse sélectionner un régiment
déjà enregistré dans la base… archiver tous les exercices liés à ce régiment…
récupérer les logos sur internet pour faire quelque chose de propre. »*

### Ce que j'ai répondu sur les logos, et pourquoi

**Je n'ai pas récupéré d'insignes sur internet.** Trois raisons dites à
l'utilisateur : (1) l'application tourne dans une zone **sans internet**, tout
doit être embarqué ; (2) les insignes officiels appartiennent au ministère —
copier Wikipédia dans un outil officiel est une question de **droits** que le
CECPC tranche, pas moi ; (3) le mémento prévoit déjà que l'administrateur
**téléverse** les insignes (§ IV.A, § V.A.1). J'ai construit ce mécanisme-là.
Si l'utilisateur fournit les fichiers ou autorise une source, ils s'intègrent
en une minute par l'écran.

### Fait

| | |
|---|---|
| **Référentiel des unités** `/administration/unites` | créer (libellé court/long, grande unité), désactiver/réactiver (§ IV.A.3 : jamais supprimer), **doublon refusé sur libellé normalisé** (« 152E r.i. » = « 152e RI », inactives comprises → « réactivez plutôt ») |
| **Sélection à la création** | `<select>` des unités actives + option « autre » qui crée à la volée ; `uniteId` prime sur le libellé |
| **Insigne** | téléversement PNG/JPEG ≤ 800 Ko, **format lu dans les octets** (un SVG renommé est refusé — il exécuterait du script), stocké dans `DATA_DIR/insignes/<uuid>.<ext>` (volume Pléiade `./data`), servi par `/api/insignes/<id>` (authentifié, `nosniff`, id validé UUID contre la traversée) |
| **Historique par unité** `/administration/unites/<id>` | tous les contrôles du régiment, niveau + label **annoncés à l'époque** (figés à la clôture), résumé des résultats |
| **Insigne partout** | accueil, bandeau du contrôle, **page de garde du CRF** (`ImageRun`) et **diapo de garde de la 3A** (`addImage`) — chargé au clic, absent hors réseau sans bloquer ; écusson d'initiales à défaut |

### ⚠ Deux défauts trouvés en éprouvant

- `libelleNormalise` remplaçait la ponctuation par une espace : « r.i. » ≠
  « ri ». **Le test l'a relevé** ; corrigé (ponctuation retirée).
- Page d'historique en 500 : le serveur de dev tenait l'**ancien client
  Prisma** en mémoire (démarré avant `prisma generate`). Pas un défaut du code
  — build et tsc passaient. Redémarré.

Éprouvé : couche fichiers (PNG écrit, relu, SVG refusé), route (200
`image/png`, traversée → 404), écrans (200), sélect de création, insigne sur
l'accueil et le bandeau. **306/306 tests**, tsc, lint, build propres.

### ⏭️ Reste

- **Les insignes eux-mêmes** : à fournir par le CECPC, ou source à autoriser.
- Une liste initiale des régiments (import CSV) éviterait de les saisir un par
  un — à proposer quand le CECPC donnera sa liste.

---

## 2026-09-18 (suite 3) — ⭐⭐ Corrections et améliorations de l'analyse, appliquées

**Autorisation utilisateur** : *« Je t'autorise à apporter les améliorations que
tu as repérées et corriger ce qu'il y a à corriger, on reste bien en local. »*
Tout est appliqué, **rien n'est commité ni poussé**. 297/297 tests, tsc, lint,
build de production : propres. Six écrans éprouvés à 200 sur un contrôle réel.

### Corrections

| | Ce qui a été fait | Où |
|---|---|---|
| **C1** ⚠⚠ | **L'auteur fait partie de la cible** des notes et des observations (`<cycle>:<pointId>|<auteurId>`). Deux contrôleurs d'un transverse ne s'écrasent plus. Les deux anciennes formes de clé restent lues — rien ne se perd. | `offline/cibles.ts` (pur, 10 tests), `useNotation`, `useObservations`, `useObservationsControle` |
| **C2** ⚠⚠ | **La pondération par observateur sur un transverse est calculée** : chaque observateur produit sa moyenne du domaine, le domaine est la moyenne pondérée de ces moyennes. Un domaine de fonction retient la valeur la plus récente (remplacement du titulaire). `useNotesDuControle` livre les notes par auteur ET fusionnées. | `domaine/apports.ts` (`noteurDe`, `PoidsDe`), `offline/useNotesDuControle.ts`, 3 écrans |
| **C3** | La case « observe » devient **« retenu dans la moyenne »** et **fait quelque chose** : `useParametrage.poidsDe` traduit case + poids en poids d'auteur. Repli : domaine jamais paramétré → tout le monde pèse 1. Ne restreint pas l'accès (un transverse reste ouvert à tous, par définition). | `useParametrage.ts`, paramétrage |
| **C4** | **Le chef de contrôle valide le label** (diapo 20). `labelFinal(calculé, retenu)` ; décision A/B/C/non validé + justification, **obligatoire si elle s'écarte du calcul** (manque bloquant sinon). Le CRF imprime les deux côte à côte. | `domaine/label.ts`, onglet Label, `crf.ts`, `docx-crf.ts` |
| **C5+P5** | **Annexe III complète** : recommandation générale, appréciation Scorpion (constat + recommandations), bloc structuré exercice (nom, type, EdT, manœuvre, ordres reçus/émis WINGO/OVO/OPO/FRAGO, durée OPO1, APPSIT, structure/protection/SIC des PC, fonctions déployées oui/non, incidents oui/non, recommandations). Saisi hors ligne dans les champs `crf:*`, formulaire sur l'écran CRF. | `restitution/crf.ts` (`AnnexeIII`), `docx-crf.ts`, `compte-rendu/annexe-iii.tsx` |
| **C6** | **L'équipe réunie** : l'onglet Équipe affecte / libère un siège par adresse (actions serveur gardées par `peutParametrer`), liste les **fonctions non pourvues** du référentiel (le « renfort de dernière minute »), montre « en attente de 1re connexion ». `useParametrage` relit l'équipe du serveur quand elle change, sans perdre le journal. `Membre.identityId` est la vraie identité. | `parametrage/actions.ts`, `session.tsx` (`sieges`, `fonctionsVacantes`), layout |
| **C7** | **Restitutions générées dans le navigateur** (`crfEnBlob`, `troisAEnBlob`), bibliothèques chargées au clic. La 3A se produit sans réseau. Les routes API restent. | `docx-crf.ts`, `pptx-3a.ts`, écran CRF |
| **C8** | `tonNote` : borne basse incluse (4,00 = niveau 3, plus rouge) ; seuils du tableau de bord alignés (4,0 / 4,4) ; échafaudage de démo retiré de `contexte.ts` ; défauts `ParametresApplication` alignés 2026 ; commentaire `Horloge.observer` corrigé. | |

### Propositions appliquées

| | | |
|---|---|---|
| **P2** | **Critères retenus non notés**, listés par domaine au tableau de bord ; **demande de complément** du commandement vers un contrôleur (`Demande#<cycle>:<pointId>#texte`), affichée ⚑ sur le critère dans sa grille. | `apports.feuillesNonNotees`, `offline/useDemandes.ts`, tableau de bord, notation |
| **P3** | **Critères retenus par le mandat** : onglet « Critères » (décocher un sous-domaine écarte ce qu'il porte), `Selection#<id>#retenu=false` au journal, `appliquerSelection()` pur. Un critère écarté disparaît des grilles et de la couverture ; ses notes restent au journal. | `domaines.ts`, `useParametrage`, 4 écrans |
| **P6** | **Suivi longitudinal** : unité à la création (find-or-create `Unite`), **clôture** qui fige niveau + label sur le contrôle (`niveauFinal`, `labelFinal`), accueil montrant unité et résultat annoncé ; notation en lecture seule sur un contrôle clos. | schéma, `depot.cloturer`, `compte-rendu/actions.ts`, accueil |
| **P8** | **Descriptions réinjectées** depuis la grille de juin (`npm run grille:descriptions`). ⚠ **Constat honnête** : sur 1 185 descriptions, **969 sont identiques au libellé**. Seules S4 (133), S6 (52), PMO (23) et quelques autres en portent de vraies — **216 copiées**. La « colonne perdue » valait moins que l'analyse ne le laissait entendre. Affichées sous le libellé sur la grille. | `scripts/fusionner-descriptions.mts`, JSON de grille, notation |
| **P9** | **Journal d'audit** des gestes d'administration : création, affectation, libération, clôture, amorçage, promotion, révocation. `JournalAudit` reçoit enfin des lignes. Ne lève jamais. | `serveur/audit.ts` |

### Ce qui n'a PAS été fait, et pourquoi

- **P1** (observation comme fait daté) — [À ARBITRER] par le client. Ne se
  décide pas seul.
- **P4** (mandat comme objet, couverture du mandat) — dépend de P1 pour relier
  objectifs et critères.
- **P10** (preuves), **P11** (tutoriel), **P12** (responsable de domaine) —
  hors périmètre immédiat.

### ⚠ À retenir pour la reprise

- Les tablettes existantes lisent encore leurs anciennes clés ; **aucune
  migration du journal local** n'est nécessaire. Les anciennes formes seront à
  retirer quand plus aucune base de terrain ne datera d'avant.
- `--accept-data-loss` est dans l'entrypoint (voir suite 2) ; les ajouts de
  colonnes de cette session (`niveau_final`, `label_final`) sont additifs.
- Le contrôle local `PARCOURS_2026` (152e RI) existe dans la base de
  développement, avec axel en ODM : c'est un terrain d'essai.

---

## 2026-09-18 (suite 2) — Analyse de conformité : ce qui est juste, ce qui ne l'est pas

Relecture de **tous** les documents sources confrontée au code, sur demande de
l'utilisateur (hors IA). Détail complet : **`LEAC/ANALYSE_2026-09-18.md`**.

**Ce qui tient, prouvé par les FORMULES du classeur NG** : moyenne par niveau
(`AVERAGE(I3,I36,I55)` = moyenne de moyennes), non noté ≠ zéro (`IFERROR → ""`),
échelle 2026-07, barème CFOT (diapo 16), label (annexe II). Le socle de calcul
est conforme.

**⚠⚠ Deux défauts graves trouvés** :
- **C1** — les notes ET les observations sur un domaine **transverse** n'ont pas
  l'auteur dans leur cible (`${cycle}:${pointId}`). Plusieurs contrôleurs y
  notent par définition → **ils s'écrasent**, et la synchronisation le montre
  comme une *collision* alors que c'est le cas nominal. Le drapeau n'a alors
  plus rien à départager.
- **C2** — la pondération par membre sur les transverses (`poidsTransverse`)
  est saisie au paramétrage mais **jamais utilisée dans le calcul**.

Autres : `peutObserver` ne restreint rien (C3) · le jugement du CC sur le label
(diapo 20) n'est pas modélisé (C4) · annexe III du CRF réduite à deux paragraphes,
sans Scorpion ni recommandations — les « pistes de travail » du client (C5) ·
équipe en base vs paramétrage au journal = deux vérités (C6) · restitutions
impossibles hors réseau (C7).

**Propositions** (12, classées) — en tête : l'observation comme **fait daté**
(P1, [À ARBITRER] client), critères non couverts + demande de complément (P2),
critères retenus par le mandat (P3), mandat comme objet (P4), recommandations
comme objets (P5), suivi longitudinal d'une unité (P6).

⏭️ Ordre proposé : C1+C2 (bloquant avant tout pilote) → C6 → C4+C5+P5 → P3+P2 → P1.

---

## 2026-09-18 (suite) — ⚠⚠ Correction d'architecture : c'est LEAC qui dit qui administre LEAC

**Rattrapé par l'utilisateur, et il avait raison.** *« Axel ne doit pas être
admin SUR Keycloak, il doit être admin SUR LEAC. Ce que je veux c'est que quand
je crée une zone dans Pléiade, dedans je crée des utilisateurs avec un mail, nom
et prénom et ça génère un mdp. De ces comptes utilisateurs, LEAC sait quel
utilisateur est admin ou utilisateur. Car ça serait enregistré DANS LEAC. »*

### Ce que j'avais fait de travers, le matin même

`estAdministrateur: roles.includes("admin")` — les rôles sortant du jeton
Keycloak. J'avais pris ce raccourci parce que `catalog/leac.yml` déclarait le
rôle. **Et j'avais vu `AdministrateurEntite` dans le schéma sans m'en servir.**

Trois raisons pour lesquelles c'était faux :
1. **Pléiade attribue ses rôles PAR GROUPE.** « Axel administre LEAC » est
   nominatif ; le passer par un groupe oblige à inventer un groupe par
   responsabilité.
2. Un rôle de royaume **suit la personne dans toutes les apps** de la zone.
   Administrer LEAC n'a aucune raison d'ouvrir quoi que ce soit ailleurs.
3. **Deux endroits où la même vérité s'écrit, c'est deux vérités.**

### ⭐⭐ Le partage, désormais

| | Répond à | Où |
|---|---|---|
| **Pléiade / Keycloak** | *qui êtes-vous ?* — compte de zone (mail, nom, prénom, mdp généré) | royaume |
| **LEAC** | *qu'avez-vous le droit d'y faire ?* | `administrateurs_entite`, base `leac` |

### L'amorçage — le premier administrateur

Si LEAC seul décide qui l'administre, personne ne peut devenir le premier. D'où
`LEAC_ADMINISTRATEURS`, **déclarée dans `catalog/leac.yml` donc saisissable
depuis Pléiade** au moment de créer l'instance. Elle n'ouvre aucun droit par
elle-même : elle **inscrit des lignes en base**, comme une promotion ordinaire.

⚠ Retirer une adresse de la variable **ne révoque pas** : la révocation est un
geste explicite et tracé. Sinon un redéploiement avec un champ oublié
dépouillerait tout le monde en silence.

⚠ Le **dernier** administrateur ne peut pas être révoqué.

### ⚠⚠ Ce que l'utilisateur craignait — vérifié, pas supposé

Il redoutait de casser le travail de Xavier. Vérifications :

| Question | Preuve |
|---|---|
| `administrateurs_entite` est-elle à Pléiade ? | **Non.** Zéro occurrence dans `pleiade-platform`, eho, app-social, app-admin. Définie dans le seul `app-leac/prisma/schema.prisma`, base `leac`. |
| Du code l'a-t-il déjà utilisée ? | **Jamais** — `git log -S` sur tout l'historique : vide. |
| Où Pléiade range-t-elle ses affaires ? | Tables `orch_*`, base séparée. |
| Le SQL du déploiement touche quoi ? | `migrate diff` : **une seule table**, `administrateurs_entite`. Rien d'autre. |

### ⚠ Le piège trouvé en chemin, et évité

`ensureClientRoles` (code de Xavier) **supprime de Keycloak les rôles retirés du
catalogue** — c'est son mécanisme voulu, le catalogue fait autorité. Retirer le
bloc `roles:` aurait donc **effacé le rôle `admin` du client `leac`**.

Décision : **on le laisse en place**, marqué obsolète, inerte. LEAC ne le lit
plus. On le retirera plus tard, en connaissance de cause, quand la nouvelle
mécanique aura fait ses preuves. **Le royaume n'est pas touché.**

### ⚠ Le démarrage du conteneur

`db push` refuse une restructuration de clé primaire → le conteneur ne
démarrerait pas. `--accept-data-loss` ajouté à `docker-entrypoint.sh`, **avec le
marché écrit en toutes lettres** : ce qui le rend acceptable aujourd'hui, c'est
que **chaque tablette garde son journal complet** — la base du serveur est un
point de rassemblement, pas la mémoire du contrôle. ⏭ À rebasculer sur
`prisma migrate` le jour où LEAC portera des contrôles archivés.

### ⚠ Un défaut d'échafaudage qui rendait mes tests faux

`controleurDeDeveloppement()` donnait `identityId = dev-${LEAC_DEV_USER}` :
**le même identifiant quelle que soit l'adresse**. Changer `LEAC_DEV_EMAIL` ne
changeait donc pas de personne, et un test de refus passait en donnant un faux
« autorisé ». Repéré en le voyant échouer. Corrigé : l'identifiant **suit
l'adresse**, comme un `sub` Keycloak distingue deux personnes.

### Éprouvé

| | Outils d'admin | `/administration/*` |
|---|---|---|
| axel (amorcé) | oui, **sans aucun rôle Keycloak** | 200 |
| s2 (ni amorcé ni promu) | aucun | **404** |

Vérifié aussi : promotion **idempotente** (deux fois = une ligne) · l'amorçage se
**rejoue seul** après effacement de la table · une adresse promue reste « en
attente de 1ʳᵉ connexion » tant que personne ne s'est connecté, et **un autre
compte ne peut pas la réclamer**.

**243/243 tests**, lint, build : propres.

### Fichiers

- ✨ `src/lib/controle/administrateurs.ts` — l'autorité
- ✨ `src/app/(controle)/administration/administrateurs/` — l'écran
- 🔁 `src/lib/zone/auth.ts` — **`estAdministrateur` retiré** : ce module
  authentifie, il n'autorise plus
- 🔁 `prisma/schema.prisma` — `AdministrateurEntite` (id, email, nomAffiche,
  promuPar, promuLe ; `identityId` nullable)
- 🔁 `docker-entrypoint.sh`, `catalog/leac.yml` (env `LEAC_ADMINISTRATEURS`,
  `adminPath`, rôle marqué obsolète)

### ⏭️ Reste

- Renseigner `LEAC_ADMINISTRATEURS` sur l'instance, **avant** le déploiement —
  sinon personne n'est administrateur.
- Retirer le rôle Keycloak obsolète, plus tard, délibérément.

---

## 2026-09-18 — ⭐⭐ Habilitations : chacun n'entre que chez lui

**Demande utilisateur.** *« Chaque utilisateur doit arriver sur une page lambda.
Les admins ont accès à la fenêtre "paramétrage du contrôle" et peuvent créer des
contrôles ; les utilisateurs lambda n'ont droit qu'au contrôle dont ils ont été
sélectionnés par un admin, et à l'intérieur aux grilles qui leur sont attribuées. »*

### Ce qui existait, et pourquoi ça ne tenait plus

Se connecter ouvrait **directement une grille de notation**, sur un contrôle de
démonstration écrit en dur (`CONTROLE_DEMO`), avec un **sélecteur de rôle** dans
l'interface (`lib/demo/role.tsx`) : chacun choisissait le personnage qu'il jouait.
C'était un échafaudage assumé, tenable tant qu'il n'y avait ni vrai contrôle ni
vrais comptes. Keycloak étant en place, il tombe.

### Les deux niveaux de droit, à ne pas confondre

| | Où il vit | Ce qu'il décide | Stabilité |
|---|---|---|---|
| **Rôle de zone** `admin` | Keycloak (client `leac`) | Créer des contrôles, tout voir, paramétrer | suit la personne |
| **Fonction** (chef d'équipe, S4…) | `MembreEquipe` du contrôle | **Quelles grilles s'ouvrent** | change à chaque contrôle |

⚠ Les mélanger serait l'erreur classique : déclarer « chef d'équipe » comme rôle
Keycloak obligerait à rejouer le royaume à chaque nouvelle équipe, et les deux
vérités divergeraient au premier oubli. `catalog/leac.yml` ne déclarait déjà
qu'un seul rôle — cette décision est simplement mise en œuvre.

### La règle de cloisonnement, en trois lignes

`domainesOuverts()` dans `src/lib/domaine/domaines.ts` — **fonction pure, testée** :

- **les transverses sont ouverts à tous** les membres (par définition notés par
  plusieurs contrôleurs, § IV.B) ;
- **un domaine de fonction n'est ouvert qu'à son titulaire** ;
- **le commandement voit tout** (il synthétise).

⚠⚠ Une fonction **inconnue** n'ouvre **que les transverses**, jamais tout. C'est
le sens dans lequel il faut se tromper : un renfort mal orthographié voit trop
peu — ce qui se signale — plutôt que trop, ce qui ne se signale pas. Testé.

### ⭐ L'affectation se fait par ADRESSE, et pourquoi

L'officier de marque monte son équipe **avant** que les intéressés ne se
connectent. Il les connaît par leur adresse, pas par leur `sub` Keycloak, qui est
un UUID que personne ne lit. Et LEAC **ne peut pas** aller le chercher : la seule
route de Pléiade qui liste les comptes d'une zone
(`GET /api/zones/:zone/users`) est réservée à l'opérateur — et elle **renvoie les
mots de passe en clair** (`rawPassword`), donc elle n'a rien à faire dans un
appel d'application.

D'où : `MembreEquipe.email` porte l'affectation, et `identityId` se renseigne
**tout seul à la première connexion** (`reclamerSesAffectations`). Ensuite c'est
`identityId` qui fait foi — une adresse qui change ne fait perdre son contrôle à
personne. ⚠ On ne réclame **que** les sièges encore libres (`identityId: null`),
sinon deux comptes portant la même adresse se voleraient leur place.

⚠ Conséquence assumée, écrite à l'écran : une adresse mal saisie ne produit
aucune erreur, elle produit **quelqu'un qui ne voit pas le contrôle**.

### ⚠⚠ Le cloisonnement est rejoué côté SERVEUR

Le layout `/controle/[id]` autorise (composant serveur, incontournable), et
`/api/sync` **revérifie**. Sans cela, n'importe quel compte connecté déversait
des opérations dans le contrôle d'une autre équipe — et en **lisait** le contenu
par la réponse, qui rend tout ce qui suit le curseur. C'était le trou réel.

⭐ Un contrôle qui n'est pas le vôtre rend **404, jamais 403** : « existe mais pas
pour vous » apprendrait à un curieux quels contrôles tournent.

### Éprouvé pour de bon, pas seulement relu

Serveur de dev + MariaDB, un contrôle réel, trois personnes :

| | Accueil | Grilles | Créer | Paramétrage | `/api/sync` étranger |
|---|---|---|---|---|---|
| **Contrôleur S4** | son contrôle seul | **3** (2 transverses + S4) | absent | refusé | **404** |
| **Administrateur** | tous | **14** | oui | oui | — |
| **Étranger** | « aucun contrôle » | — | 404 | 404 | 404 |

Vérifié aussi : un second compte ne peut pas réclamer une adresse déjà liée.
**243/243 tests**, lint propre, build propre.

### Fichiers

- ✨ `src/lib/zone/habilitation.ts` — **l'autorité unique** (`mesControles`,
  `habilitationSur`, `reclamerSesAffectations`)
- ✨ `src/lib/controle/depot.ts` — créer un contrôle, référentiel des fonctions,
  `pourvoir`/`liberer` un siège
- ✨ `src/lib/controle/session.tsx` — remplace `lib/demo/role.tsx` (**supprimé**)
- ✨ `src/app/(controle)/page.tsx` — l'accueil « Mes contrôles »
- ✨ `src/app/(controle)/controle/[id]/layout.tsx` — le sas qui autorise
- ✨ `src/app/(controle)/administration/nouveau-controle/` — création (admin)
- 🔁 Les 6 écrans déplacés sous `/controle/[id]/…` — une URL qui ne dit pas quel
  contrôle elle montre est un piège (signet, bouton retour)
- 🔁 `prisma/schema.prisma` — `MembreEquipe.email` (+ index)
- 🔁 `domaines.ts` — `Domaine.fonction` + `domainesOuverts`

### ⏭️ Ce qu'il reste

- ⚠⚠ **Attribuer le rôle `admin` à axel** — tableau de bord Pléiade → instance
  LEAC → icône bouclier « **Droits** » → cocher `admin` pour son **groupe**.
  ⚠ Les rôles s'attribuent **par groupe**, pas par personne. **Sans cela,
  personne ne peut créer de contrôle** et tout le monde voit « aucun contrôle ».
- L'équipe éditée au paramétrage vit encore dans le journal hors ligne ; le
  serveur décide de l'accès, l'écran décide du reste. À réunir.
- Écran d'administration de l'équipe en cours de contrôle (`pourvoir` existe,
  l'écran non).

---

## 2026-09-17 (suite 4) — ⭐⭐ LEAC tourne sur le serveur

**Première mise en production réussie.** `https://leac.cecpc-div-eval.pleiade.internal`

Vérifié depuis le poste, par VPN : `/` renvoie **307** vers `/connexion`,
`/api/sante` rend `{"ok":true,"app":"LEAC"}`, `/connexion` répond **200**, et
`/api/service/health` refuse bien sans clé (**401**).

### La chaîne, et qui a fait quoi

Je n'ai **jamais touché au serveur** — ni SSH, ni commande à distance. Tout est
passé par Git.

1. J'écris `Dockerfile`, `docker-entrypoint.sh`, le workflow et `catalog/leac.yml`.
2. L'utilisateur pousse `pleiade-platform` sur `main` → l'orchestrateur se
   redéploie **avec le catalogue**.
3. Je pousse `app-leac` sur `prod`, sur son feu vert explicite.
4. Le **runner auto-hébergé, sur le serveur**, construit l'image et la pousse au
   registre interne. ⭐ Les **214 tests tournent dans le `podman build`**, avant
   la compilation : s'ils cassent, aucune image n'est fabriquée.
5. L'utilisateur crée l'instance depuis le tableau de bord.
6. Pléiade fabrique base, client Keycloak, `compose`, `.env`, route Traefik.

### ⚠ Deux échecs avant d'y arriver, tous deux de mon fait

**Exit code 125 au premier essai.** Ma première hypothèse — le runner ne serait
pas disponible pour ce dépôt neuf — était **fausse** : la capture d'écran a
montré un job qui avait tourné 2 min 29 puis échoué.

1. **`public/` absent du dépôt.** J'avais repris le `Dockerfile` de
   `app-messagerie`, qui en a un. ⚠ Et Git n'enregistre pas un dossier vide : il
   a fallu y mettre une vraie favicon.
2. **`docker-entrypoint.sh` extrait en CRLF** → « no such file or directory » sur
   un fichier pourtant présent.

⭐ Trouvés en **reproduisant le build ici** — ce poste a Docker. Clone propre de
`prod`, `docker build`, puis exécution contre une vraie MariaDB. Deux minutes.

⚠ **Vérifié avant de « réparer »** : le blob Git de l'entrypoint était bien en
**LF** (`git show HEAD:… | od -c`). Le serveur n'était donc pas touché par le
second ; c'est la copie de travail Windows qui l'était. Sans ce contrôle,
j'aurais corrigé un problème que le dépôt n'avait pas. → [[LESSON-035]]

### Ce que la mise en production a validé

- `prisma db push` applique **réellement** le schéma : **30 tables** créées,
  `operations` comprise avec sa `sequence` auto-incrémentée.
- Le **certificat par zone** est créé automatiquement pour une zone neuve.
- ⚠ Traefik rend **404 tant que le conteneur n'est pas prêt** — ça ressemble à
  une erreur de configuration et n'en est pas.

### ⚠⚠ Ce que la mise en production ne change PAS

**LEAC déployé est une démonstration, pas encore un outil.** Chaque tablette a sa
base isolée dans son navigateur ; Prisma est généré mais **jamais instancié** ;
l'écran de synchronisation **simule** un échange. Deux contrôleurs sur cette
instance ne verraient pas le travail l'un de l'autre.

Or « concaténer les données de chaque contrôleur » **est** la finalité du projet.

### ⏭️ Prochaine étape
1. ⭐⭐ **La couche de synchronisation serveur.** Le modèle existe (`Appareil`,
   `Operation` et son curseur `sequence`), le moteur de fusion est écrit et
   testé — il manque le tuyau : client Prisma, `POST /api/sync`, et le
   branchement de l'écran qui simule.
2. ⚠ **Côté serveur, chez Xavier** : faire connaître `leac` à
   `pleiade-promouvoir`, sans quoi la prochaine mise à jour ne se propagera pas.
3. Charger un **vrai contrôle** depuis la base, et l'équipe depuis **eho**.

---

## 2026-09-17 (suite 3) — La directive N4 2026 entre dans le logiciel

**Documents reçus** : `D:\Nouveau dossier` — demande client, mémoire de
passation LEAC NG, récapitulatif projet, **deux grilles Excel**, cours sur les
critères (CBA Rubben), **modèle de compte rendu final**. Tous copiés dans
`app-leac\docs\sources\`, avec leurs marquages de diffusion relevés.

### ⭐⭐ Ce que ces documents ont changé, et ce qu'ils ont contredit

**LEAC NG est plus vaste que ce que je construisais.** La mémoire de passation
décrit un système métier complet, en phase de **cadrage**, avec ses marqueurs
`[CONFIRMÉ]` / `[ENVISAGÉ]` / `[À ARBITRER]`. Ce qu'on a bâti correspond à une
**partie de la BETA** décrite au § 17 — pas à tout LEAC NG.

**Ce qu'ils confirment** : le journal d'opérations hors ligne (§ 11), « null n'est
pas zéro », la moyenne qui remonte par niveau, les deux domaines transverses.

**Ce qu'ils contredisent** — et c'est l'essentiel :

1. ⭐⭐ **La notation se fait par des MOTS, chiffres cachés.** Mon écran affichait
   une échelle chiffrée : il contredisait frontalement la méthode. → [[DECISION-025]]
2. **Le barème que j'avais codé était le mauvais** : 4,5 / 4 / 3 (v2.5) contre
   **4,65 / 4,4 / 4** (CFOT 2026). La directive 2026 prime.
3. **La pondération porte sur le DOMAINE**, pas sur la fonction.
4. **Il manquait les LABELS** — toute une dimension. → [[DECISION-026]]
5. La hiérarchie a **5 niveaux**, pas 4.

### Les défauts trouvés dans les documents du CECPC

⭐ Le lecteur de grilles ne convertit pas seulement, il **rend compte**. Trois
défauts réels dans la grille NG, vérifiés cellule par cellule :

- *Fonctionnement général* L142-146 : sous « 1.8.3 RENFORTS AIR », les critères
  sont numérotés **1.8.2.x** — ces cinq codes existent **deux fois** ;
- *Travail collectif* L63-66 : sous « 2.3.2 », les critères sont numérotés
  **1.3.2.x** ;
- *S3-2D* L144 : « 7.7.2 » inséré au milieu du bloc 7.2.

Plus deux formules fausses dans leur « Tableau de Bord » :
`COUNTIF('Travail Collectif du CO'!J:J;…)` pour la ligne *Remarquable* de **S7**,
et `COUNTIF(PMO!I:EI;"N/O")` au lieu de `I:I`.

⭐ Et une **perte** : la grille de juin porte une colonne **« Description »** — le
*but* de chaque critère — que la NG a abandonnée. 132 critères sur 133 pour le
seul Fonctionnement général.

### ⚠ Deux erreurs que j'ai commises, et ce qui les a rattrapées

1. **3 415 fausses anomalies** sur la grille de juin : dans ce format le libellé
   est **intercalé** entre les colonnes de code, et je le comptais comme un code.
   Le code se reconnaît désormais à **sa forme** (`10.1.1.1`). ⭐ C'est
   l'énormité du chiffre qui a rendu l'erreur évidente — un décalage produisant
   *quelques* anomalies plausibles serait passé.
2. **J'ai annoncé à tort** que les cartouches ne correspondaient pas aux
   rubriques du compte rendu : je n'avais lu que l'annexe I. Les **annexes V et
   VI portent les cinq rubriques**, exactement les cinq cartouches. Corrigé.

### Ce qui a été écrit

| | |
|---|---|
| Notation par mentions, le **mot** enregistré | `domaine/echelle.ts` · `f0b69eb` |
| Lecture des grilles Excel, **deux formats** + contrôle | `import/grille.ts` · `aeb9773` |
| **Les vraies grilles branchées** — 14 domaines, 1 352 critères | `165009b` |
| **Label** de l'exercice, 10 exigences | `domaine/label.ts` · `95c7fcb` |
| **Compte rendu final** `.docx`, annexes I à VII | `/compte-rendu` · `16627e3` + `02ca61d` |
| **3A** `.pptx`, une diapo par domaine | `02ca61d` |
| **Pondérations adaptées par le mandat** du N+1 | `e3079f8` |
| Le **classeur NG fait foi** comme référentiel | `476d07f` |

**214 tests** (contre 120 avant cette session).

### ⚠ Deux points de forme qui ne sont pas cosmétiques

- **3A** : le **taux de couverture à côté de chaque camembert**. Un camembert sur
  12 % de critères et un sur 100 % se ressemblent exactement — c'est ainsi qu'une
  salle tire une conclusion d'un domaine à peine observé.
- **CRF** : le document sort marqué **PROJET** et porte **la liste de ce qui lui
  manque**, avant son titre. Un brouillon qui a l'air fini est plus dangereux
  qu'un brouillon vide.

⭐ Et un bénéfice de côté : le CRF est **construit**, pas rempli depuis le modèle
(Word a découpé `$$NUMDOC$$` et `$$SIGNATURE$$` entre plusieurs balises). Il
**n'hérite donc pas** du filigrane « DIFFUSION RESTREINTE » que le modèle porte
par erreur.

### ⏭️ Prochaine étape
1. ⏳ **À faire confirmer par le CECPC** : l'échelle de mentions (elle remonte les
   moyennes), les trois défauts de numérotation, la colonne « Description »
   perdue, le filigrane erroné du modèle de CRF.
2. **Le stockage serveur** — tout vit aujourd'hui dans le navigateur, alors que
   la concaténation entre contrôleurs suppose un serveur qui reçoive les
   journaux. C'est le cœur de la finalité du projet.
3. Bascule **NG ↔ ancienne grille** (le lecteur sait déjà lire les deux).

---

## 2026-09-17 (suite 2) — Paramétrage persisté, tableau de bord de la réunion

**Demande utilisateur** : « ok tu peux avancer » — poursuite du développement
sur la feuille de route annoncée.

### 1. Le paramétrage survit à la fermeture de l'application — commit `86da06d`

L'écran de l'officier de marque était **en mémoire** : fermer l'onglet effaçait
l'équipe, les pondérations et le porteur du drapeau. Il écrit désormais dans le
**même journal d'opérations** que la notation — un paramétrage corrigé *en cours*
de contrôle remonte donc au serveur comme le reste.

- ⭐ **Granularité retenue : un CHAMP par membre** (`MembreEquipe#<id>#nom`),
  jamais un objet « équipe » entier. Écrire l'équipe en bloc ferait qu'un ODM
  modifiant un **poids** écraserait le **nom** qu'un collègue vient de corriger
  sur une autre ligne — alors que les deux gestes n'ont rien à voir. Champ par
  champ, ils se fondent sans conflit. *(Même propriété que les 5 cartouches
  d'observation, obtenue de la même façon.)*
- `useEcritureDifferee` **extrait** — les observations et le paramétrage en
  avaient un besoin identique ; dupliquée, la minuterie aurait divergé au premier
  correctif. **Deux déclencheurs : repos de saisie ET sortie de champ.** La v2.5
  n'écrivait qu'à la sortie de case (§ II.B) — insuffisant sur tablette : écran
  verrouillé, bascule d'application, batterie à plat, et la sortie de champ
  n'arrive jamais. On perdrait le **dernier** paragraphe, donc le plus récent.
- Texte = différé ; **poids et cases à cocher = écrits immédiatement** (différer
  un clic n'apporte rien et retarde sa remontée).
- Le drapeau qui deviendrait **orphelin** (retirer le droit d'observer à son
  porteur) est **déplacé**, pas perdu.

### 2. Tableau de bord de la réunion quotidienne (§ V.B.9) — commit `d352962`

`/tableau-de-bord` + `src/lib/domaine/bilan.ts`. Trois questions, **dans cet
ordre** — et l'ordre est le fond du sujet :

1. ⭐ **Où en est-on** — le taux de remplissage, **avant** toute note. Lire
   « 4,2 » sur 8 % de points saisis fait conclure qu'un PC est au niveau alors
   que personne n'a encore rien vu.
   ⚠ **Le taux se compte en POINTS, pas en moyenne de taux** : un domaine à 60
   critères et un domaine à 6 ne représentent pas le même travail restant. Une
   moyenne de taux dirait « 50 % » là où il reste 59 points sur 66.
2. **Qu'est-ce qui ressort** — note par fonction, puis détail par sous-domaine,
   dépliable. ⚠ Le détail **s'arrête au niveau au-dessus des feuilles** : le
   critère par critère appartient à la grille, pas à une réunion — déplier
   soixante lignes devant une assemblée ne fait lire personne.
3. **Qu'en dit le porteur du drapeau.**

⭐⭐ **Le drapeau devient un vrai filtre.** En v2.5 c'était un *avertissement*
(« la première personne cochée aura un petit drapeau ») : une règle que le
logiciel n'appliquait pas. L'appliquer demandait de connaître l'**auteur** de
chaque observation — d'où `lireEtatDetaille`, qui rend l'auteur de chaque valeur
de l'état dérivé. Les remarques des autres sont **écartées du bilan, jamais
supprimées**, et l'écran l'écrit noir sur blanc.

⚠ **Écran en LECTURE SEULE, à dessein.** On ne corrige pas une note pendant la
réunion : celui qui l'a posée n'est pas forcément là, et une note changée sans
lui est une note que personne n'assume.

### 3. Ce que les tests verrouillent — **78/78** (+27)

13 tests sur le bilan, tous sur des erreurs **invisibles à l'œil** :
- ⭐ Une fonction **non abordée est EXCLUE** de la moyenne, elle **ne compte pas
  zéro**. Sans cette règle, le premier matin d'un contrôle affiche « Inapte
  opérationnel » à un PC dont personne n'a rien vu.
- Une fonction de **poids 0** sort du calcul **mais reste à l'écran**, motif écrit
  en clair — *« pourquoi cette ligne n'est pas dans la moyenne »* est exactement
  la question posée à voix haute en réunion.
- Taux en points et non en moyenne de taux (cas 60/60 + 0/6).
- Contrôle vierge : note `null`, barème `null`, taux `0` — **pas `NaN`**.

### 4. Écran de fin de cycle (§ III.B / § III.C) — commit `edbf801`

`/fin-de-cycle` + `src/lib/domaine/cycle.ts`. Trois gestes dans l'ordre du soir :
lire les réserves, écrire le bilan et les synthèses, figer.

⭐⭐ **La décision centrale — figer est un état MÉTIER, pas un verrou
d'écriture.** Une note posée hors ligne **avant** le figeage peut très bien ne
remonter qu'**après** : c'est même le cas normal d'un contrôleur qui rentre au
bureau en fin de soirée. La refuser reconstruirait de nos mains le défaut annoncé
au § V.B.8. Elle est donc **acceptée, conservée, et signalée** — l'écran liste ce
qui est arrivé depuis la décision, et le chef de contrôle tranche s'il rouvre.
→ [[DECISION-023]]

⚠ La comparaison se fait sur l'**horloge de Lamport**, jamais sur une date : deux
tablettes n'ont pas la même heure, et une tablette éteinte trois jours revient
avec une horloge murale fausse. L'horloge de référence est lue **avant** d'écrire
le figeage, sinon le figeage se signalerait lui-même comme une saisie tardive.

**Une seule réserve est bloquante** — l'absence de porteur du drapeau (le cycle
serait figé sur un bilan sans auteur). Tout le reste informe sans empêcher :
exiger la complétude produit le piège classique où un contrôleur absent bloque un
cycle indéfiniment. ⚠ L'écran **dit pourquoi** les autres ne bloquent pas — sinon
un avertissement qui laisse passer se lit comme un bug.

Le reste :
- § III.C — les **synthèses générales** restent **visibles et verrouillées** hors
  chef de contrôle. Les masquer ferait croire qu'elles n'existent pas, et la
  question reviendrait à chaque contrôle.
- ⚠ Ces verrous sont de **lisibilité**. La règle qui compte s'applique **au
  serveur**, à la réception des opérations — un écran ne protège rien, et le
  fichier le dit pour qu'on ne s'y trompe pas.
- **Confirmation maison, jamais `confirm()`** : sur tablette la boîte système est
  minuscule, hors charte, et se valide par réflexe.
- **Rouvrir n'efface rien** : c'est une opération de plus, la trace reste.
- **Sélecteur de rôle**, marqué comme échafaudage de démonstration : il permet
  d'**éprouver** le cloisonnement au lieu de le croire sur parole. Il disparaît
  avec la session Keycloak.
- Les membres de démonstration ont un `identityId`, **sauf `m6`** : c'est le
  renfort de dernière minute (§ V.B.3), créé en local, sans identité de zone. Les
  écrans doivent le supporter — c'est un cas réel, pas une donnée incomplète.

**14 tests de plus (92/92)**, dont ceux qui verrouillent qu'une saisie **à**
l'horloge du figeage n'est **pas** tardive, et que le figeage ne se signale pas
lui-même.

### 5. Cycles réels, validation de grille, et le drapeau expliqué — commit `7510830`

**Question de l'utilisateur** : *« à quoi sert le système de donner le drapeau
dans LEAC, je ne comprends pas son utilité »*. Elle est justifiée : le memento
dit ce que le drapeau **fait**, jamais **pourquoi** il existe.

#### ⭐ Le drapeau — la réponse, à conserver
Un **domaine transverse** (fonctionnement général du PC, travail collectif)
**n'appartient à aucune fonction** : plusieurs contrôleurs l'observent, chacun
depuis son poste. Pour les **notes**, aucun problème — elles se moyennent,
pondérées par membre (c'est le rôle de `PonderationTransverse`). Pour les
**observations**, qui sont du **texte libre**, on ne peut pas faire la moyenne
de quatre paragraphes. **Il faut une voix.** Le drapeau désigne celle dont le
bilan est projeté le soir *(memento p. 27 : « le bilan de cycle de la personne
désignée par le drapeau »)*.

Ce qui rend la v2.5 incompréhensible : désignation par **ordre de clic**,
porteur **jamais nommé** ensuite, et conséquence annoncée comme un simple
**avertissement dans un manuel**.

⚠ **Écart assumé, documenté** dans `docs/COUVERTURE.md` § « Écarts assumés » :
la v2.5 dit *« SEULS ses commentaires seront vus »* — le travail écrit de trois
contrôleurs disparaît de la réunion sans que personne le sache. En v3, le bilan
du porteur reste la **parole officielle seule affichée par défaut** (l'intention
est tenue : une seule voix), mais les autres sont **dépliables**, nommées, sous
la mention « hors bilan officiel ». **Réversible en une ligne** si le CECPC
préfère la règle stricte — l'utilisateur a été prévenu.

#### § V.B.7 — le cycle entre dans la CLÉ des notes
Le numéro de cycle était une constante : « ouvrir le cycle suivant » ne pouvait
rien vouloir dire. Il devient une valeur du journal (`Controle#…#cycleCourant`),
et surtout les notes portent le cycle dans leur cible :
`Note#<cycle>:<pointId>#valeur`.

⭐ **Ce n'est pas un filtre, c'est la cible.** Chaque cycle **renote les mêmes
critères**, et c'est **l'écart entre cycles** qui dit si le PC progresse. Sans le
cycle dans la clé, la 2ᵉ journée écraserait la 1ʳᵉ.

⚠ Les notes écrites **avant** ce changement sont rattachées au cycle d'origine,
en trois lignes marquées à retirer. Une donnée qui s'évapore parce qu'on a changé
un format de clé est exactement la perte silencieuse que cette application
refuse — **y compris quand la victime est une base de démonstration**.

#### § III.D — chacun valide SA grille
L'état `grilleValidee` s'affichait mais rien ne permettait de le poser. Le bouton
n'apparaît que sur **sa propre** ligne : une validation est un engagement (« ce
que j'ai noté, je l'assume »), elle ne se délègue pas plus qu'une signature.

#### Rôle joué, partagé entre les écrans
Le sélecteur de démonstration passe dans `src/lib/demo/role.tsx` et remonte au
`layout` : le cloisonnement se traverse d'un écran à l'autre, sinon on ne peut
pas l'éprouver. ⚠ Il vit dans `sessionStorage`, **pas dans le journal** — ce
n'est pas une donnée du contrôle, l'y écrire l'enverrait au serveur et le ferait
apparaître dans la revue de synchronisation. Lu via `useSyncExternalStore` :
l'outil prévu pour un magasin extérieur à React, qui traite aussi le rendu
serveur, lequel n'a pas de stockage.

### 6. CORRECTIF — le drapeau ne s'applique qu'aux transverses — commit `eeb64ea`

**Relance de l'utilisateur** : *« un profil qui porte le drapeau met en avant ses
observations sur toutes les grilles ? »* — lecture exacte de ce que faisait mon
code, **et mon code était faux**.

Mon filtre était **global** : il retenait les observations du porteur sur tout le
contrôle. Les remarques du S4 sur **sa propre** grille disparaissaient donc du
tableau de bord dès que le drapeau était ailleurs — alors que personne d'autre
n'écrit sur un domaine de fonction.

**Ce que dit réellement le memento** : le § V.A.3 est situé dans l'onglet
« pondérations », au milieu des domaines transverses. Le drapeau y coche « les
personnes qui pourront mettre des observations **dans les domaines
transverses** ». Il ne concerne qu'eux.

La distinction vit désormais dans `src/lib/domaine/domaines.ts`, avec la règle
`remonteAuTableauDeBord` en **un seul endroit** — elle était auparavant répartie
entre l'écran et le hook, et fausse aux deux.

⚠ **Corollaire** : le drapeau appartient au **domaine**, pas au contrôle. Chaque
transverse a **son propre** porteur. L'onglet Pondérations devient donc un bloc
par transverse — la forme exacte de l'écran du memento p. 15 : poids, « observe »,
drapeau, pour chaque membre.

⭐ **Écrit comme « QUI le porte »**, champ unique par domaine, et non comme un
booléen sur chaque membre. Avec un booléen, deux tablettes hors ligne qui
désignent chacune leur porteur remontent deux `true` sur des **cibles
différentes** : la fusion les garde **tous les deux**, le domaine se retrouve
avec **deux drapeaux**. Champ unique = même cible = l'horloge tranche.

Aussi : un domaine transverse réel rejoint les données de démonstration
(FONCTIONNEMENT GÉNÉRAL ET TRAVAIL COLLECTIF DU PC, § IV.B), et l'écran de
notation permet d'en changer — sans quoi le drapeau restait **invérifiable à
l'usage**. `GRILLES_PAR_MEMBRE` ne contient plus que les domaines de fonction :
un transverse n'appartient à personne.

**11 tests de plus (103/103)**, tous sur la règle qui était fausse.

### 7. Compactage du journal — commit `675cfd3`

**Constat de l'utilisateur à l'usage** : *« si je pose une notation puis que je
la retire, on a quand même X saisies à remonter alors que je ne fais que cliquer
et annuler le clic — ça risque de surcharger les données, non ? »*

⭐⭐ **La question portait sur le volume ; le vrai problème est la JUSTESSE.**

Serveur à « rien ». Tablette A pose 3, se ravise, retire. Tablette B, hors ligne
elle aussi, pose 4 sur le même point.
- **A remonte son retrait** : il porte une horloge **plus récente** que le 4 de
  B. À la fusion, le retrait gagne et **efface le travail de B** — alors que A
  n'a rien changé, il a écrit puis annulé.
- **A ne remonte rien** : le 4 de B tient. Seul résultat correct.

Une opération **nette nulle** n'est donc pas inutile : elle **écrase le travail
d'autrui au nom d'un geste qui n'a pas eu lieu**. → [[DECISION-024]]

**La règle** : pour une cible donnée, tant qu'aucune opération n'est partie, on
ne garde que l'écart net par rapport à ce que le serveur connaît. Écart nul, il
ne reste rien.

⚠⚠ **La limite, absolue** : jamais une opération **déjà remontée**. Elle
appartient à l'histoire commune.

⚠ **Ce qu'on perd, assumé** : les états intermédiaires d'une frappe. Le journal
sert à **synchroniser**, pas à reconstituer les hésitations de quelqu'un.

**Une quatrième table locale : `socle`** — ce que le serveur connaît de chaque
cible. ⚠ Elle se met à jour **même quand une opération distante n'est pas
appliquée à l'écran** : « ce que le serveur détient » et « ce que j'affiche »
sont deux choses différentes.

⚠ **La migration v1 → v2 était dangereuse** et a été traitée : un socle vide
signifie « le serveur ne connaît rien », ce qui aurait **fait taire une
suppression légitime** — retirer une note déjà remontée serait passé pour un
geste annulé, et le serveur l'aurait gardée pour toujours. Le socle est donc
reconstruit depuis les valeurs sans opération en sursis.

**17 tests de plus (120/120)**, dont celui qui verrouille que `0` et `false` ne
sont **pas** vides : un poids à 0 neutralise une fonction, c'est une décision.

### 8. LEAC devient une app de zone PLEIADE déployable — commits `4eccf1f` + `b96fd8b`

**Demande** : configurer `app-leac` comme les autres dépôts, pour pouvoir y
introduire une branche `prod` qui met l'application à jour automatiquement, et
l'introduire comme **instance** assignable à une zone depuis
`https://pleiade.cecpc.internal/`.

LEAC suivait déjà les conventions PLEIADE **dans son code** ; il lui manquait
tout ce qui en fait une app **déployable**.

#### Chaîne de déploiement (`app-leac`)
- `Dockerfile` — sortie standalone, CLI Prisma isolé, schéma poussé au
  démarrage. ⭐ **`npm test` AVANT `npm run build`**, et c'est un choix de fond :
  les tests tiennent les règles de notation et de fusion, dont les erreurs sont
  **invisibles à l'œil**. Les faire échouer là, c'est refuser de fabriquer
  l'image. **Le serveur n'a pas Node** : c'est le seul endroit où ils tournent
  automatiquement.
- `.github/workflows/deployer-prod.yml` — déclenché sur `prod`, runner
  auto-hébergé, promotion limitée aux seules instances de `leac`.
- ⚠ **Port 3000 dans le conteneur** comme toutes les apps ; le 3700 ne sert qu'à
  cohabiter en local avec eho et les autres.

#### Intégration à la zone
- **Deux sondes, à ne pas confondre** : `/api/sante` (Podman, sans
  authentification, ne touche **ni la base ni Pléiade** — sinon une instance qui
  démarre pendant que MariaDB se réveille serait déclarée morte et ne
  reviendrait jamais) et `/api/service/health` (contrat commun, derrière
  `X-API-Key`).
- Découverte des voisines **à l'exécution**, avec conservation de la dernière
  liste si l'orchestrateur est injoignable.
- **Keycloak du royaume de la zone.** Les écrans passent dans un groupe de
  routes `(controle)` dont le layout est le sas : un seul endroit, pas de boucle
  de redirection, la page de connexion reste dehors.
- ⚠ Échappatoire `LEAC_DEV_USER` **fermée en production**. Vérifié : sans elle,
  `/` et `/parametrage` renvoient **307** vers `/connexion`.

#### ⚠ Défaut de schéma révélé par la première construction
`prisma generate` **n'avait jamais été lancé** sur ce schéma : il ne validait
pas. `@@unique([acronyme, definition])` portait sur un `@db.Text`, que MySQL
n'indexe pas sans longueur. Passé en `VarChar(255)`. Garder `Text` aurait obligé
à **renoncer à l'unicité**, donc à accepter deux fois le même couple dans le
glossaire. ⭐ C'est exactement ce que la construction d'image doit attraper.

#### Catalogue (`pleiade-platform`)
`catalog/leac.yml` — opération de **contenu**, aucune ligne de code de
l'orchestrateur touchée. ⚠ Mais le catalogue est **copié dans l'image** de
l'orchestrateur : il faut redéployer `pleiade-platform`, dont le `main`
**déploie sans sas**.

⭐ **Un seul rôle Keycloak, et c'est une décision** : « chef de contrôle »,
« chef d'équipe », « officier de marque » sont des **fonctions tenues dans une
équipe**, qui changent d'un contrôle à l'autre. Les mettre dans le royaume
obligerait à rejouer Keycloak à chaque équipe, et les deux vérités divergeraient
au premier oubli. Le royaume ne tranche que l'accès au **référentiel** (`admin`).

#### ⚠ Ce qui reste à faire, hors de nos dépôts
1. `/usr/local/sbin/pleiade-promouvoir` doit connaître `leac` (script + sudoers
   du compte `runner`) — sinon l'image est construite et poussée, mais **rien
   n'est promu**.
2. Vérifier la valeur réelle de **`BASE_DOMAIN`** dans le `.env` du serveur, et
   que le **certificat wildcard** couvre ce domaine — `pleiade-infra` génère
   encore `*.mastorion.internal`.

#### ✅ Mise en service constatée le 2026-09-17

`app-leac` poussé sur `main`, et `pleiade-platform` poussé par l'utilisateur.
**Vérifié sur le serveur, pas supposé** :

- `https://pleiade.cecpc.internal/api/version` rend **`commit: f7d075a`** — c'est
  le commit du catalogue. ⭐ **LEAC est donc dans le catalogue de PLÉIADE** et
  assignable à une zone.
- ⚠ **L'image `leac` n'est PAS dans le registre** (`registry.cecpc.internal/v2/_catalog` :
  admin, cockpit, eho, messagerie, pleiade-orchestrator, presse, social).
  👉 **Créer une instance LEAC maintenant échouerait au démarrage** : rien à tirer.
  L'image n'est fabriquée que par le workflow `prod`.
- ⭐ **Le premier `push prod` fait l'essentiel même s'il « échoue »** : les étapes
  1 et 2 (construire, pousser au registre) aboutissent ; seule la promotion
  échoue, faute de `leac` dans `pleiade-promouvoir`. Or la promotion ne sert
  qu'à **mettre à jour des instances existantes** — et il n'y en a aucune. Donc
  après ce push, l'image est là et l'instance peut être créée.

**Adressage relevé au passage** *(voir `PLEIADE\MEMOIRE.md` §3, corrigé)* :
`BASE_DOMAIN = pleiade.internal`, donc une instance LEAC vivra à
**`{instance}.{zone}.pleiade.internal`**. La zone `exercice` tourne déjà
(`eho.exercice.pleiade.internal` répond), et Traefik y sert un certificat
**par zone** — la réserve que j'avais émise sur le certificat était infondée.

#### Mise en production engagée — branche `prod` créée le 2026-09-17

À la demande de l'utilisateur, et **après** avoir écrit
`docs/INTEGRATION-PLEIADE.md` pour que la branche l'emporte avec elle :

```
git switch -c prod && git push -u origin prod
```

`prod` part de `main` au commit **`f3e0555`**. Le workflow construit l'image,
lance les **120 tests** (ils sont dans le `Dockerfile`, avant le build), pousse
au registre, puis tente la promotion.

⏳ Attendu : **succès jusqu'au registre, échec à la promotion** faute de `leac`
dans `pleiade-promouvoir`. ⭐ Sans conséquence pour un premier déploiement — la
promotion ne met à jour que des **instances existantes**, et il n'y en a aucune.

⚠ **À partir de la 2ᵉ mise à jour**, ce manque se fera sentir : il faudrait
recréer l'instance à la main au lieu de la promouvoir. C'est le point à faire
traiter côté serveur.

### 📝 Fichiers autoritaires modifiés
- `app-leac` : commits **`86da06d`**, **`d352962`**, **`edbf801`** et
  **`7510830`**, **`eeb64ea`** et **`675cfd3`** — `docs/COUVERTURE.md` passe à
  🟢 **16 faites** / 🟡 52 / ⚪ 21 / 🔵 29, et gagne une section **« Écarts
  assumés avec le memento v2.5 »**. ⭐ Le compactage est la **118ᵉ** fonction :
  elle ne vient pas du memento, la v2.5 n'avait pas lieu de l'avoir.
- `LEAC\MEMOIRE.md` — tableau d'état, règle métier n°4 (drapeau) recadrée.

### ⚠ Rien n'est poussé
✅ **Tout est poussé** : `app-leac` `main` et `prod` au commit `f3e0555`,
`pleiade-platform` `main` au commit `f7d075a` (déployé, vérifié par
`/api/version`). Dépôt partagé avec
Xavier : pas de poussée sans demande explicite.

### ⏭️ Prochaine étape
1. ⏳ **En attente de l'utilisateur** : confirmer l'**écart assumé sur le
   drapeau** (dépliable) ou revenir à la règle stricte du memento.
2. **Génération 3A (.pptx) / CR (.docx)** — ⏳ bloqué sur le **modèle de CR** du
   CECPC (§ X, « en cours de rédaction »), demandé par l'utilisateur.
3. **Import/export Excel des grilles** — ⏳ bloqué de même (§ XII).
4. Trancher la **durée de vie du PIN hors ligne**.

---

## 2026-09-17 (suite) — Documentation ingérée, dépôt créé, socle v3 écrit

**Demande utilisateur** : à partir des deux mementos v2.5, produire une version
« nettement plus optimisée, plus fluide, plus esthétique » ; créer le dépôt privé
`cecpc-pleiade/leac` ; **100 % des fonctionnalités assimilées** ; finalité = les
contrôleurs sur **tablette en extérieur**, puis **synchronisation par VPN** au
retour pour **concaténer les données de chaque contrôleur**.

### Ce que la documentation a révélé
- ⭐⭐ **Le défaut central de la v2.5** est écrit noir sur blanc dans le memento
  utilisateur § V.B.8 : *« toute modification effectuée durant la synchronisation
  sera perdue »*. C'est exactement ce que la demande de l'utilisateur vise.
- ⚠ **Les 5 « erreurs récurrentes » (§ V.D) viennent TOUTES du dispositif
  technique, aucune du métier** : réinstallation complète, `multi-master.info` à
  supprimer, câble réseau à débrancher au démarrage, et — la plus parlante — **une
  apostrophe** dans une grille qui casse la synchronisation (SQL concaténé). Elles
  occupent **un cinquième du memento**. C'est l'argument le plus fort pour la
  réécriture, et il vient du document lui-même.
- ⚠ **Deux sections des mementos sont « en cours de rédaction »** : le **modèle CR**
  (§ X) et le **format des grilles Excel** (§ XII). Ce sont des **trous dans la
  source**, pas des oublis — signalés à l'utilisateur, à demander au CECPC.

### Fait
- **Dépôt privé `cecpc-pleiade/leac` créé** (API GitHub, identifiants du poste,
  jamais affichés), cloné dans `C:\CECPC\pleiade\leac`, **poussé** (`main`).
- ⭐ **`docs/COUVERTURE.md`** — les **117 fonctions** des deux mementos, une par
  une, avec leur état : 🟢 4 faites · 🟡 63 modèle en place · ⚪ 21 spécifiées ·
  🔵 **29 repensées**. Les 29 ne sont pas des abandons : 27 disparaissent parce que
  la contrainte technique qui les imposait (hub, IP fixes, PC maître, clé USB,
  comptes locaux) n'existe plus, chacune justifiée dans sa ligne.
- **`prisma/schema.prisma`** — modèle complet, **annoté paragraphe par paragraphe**
  du memento, pour qu'on puisse vérifier la couverture sans relire les PDF.
- ⭐⭐ **`src/lib/sync/fusion.ts`** — le moteur de concaténation. Journal
  d'opérations, **horloge de Lamport** (jamais l'heure de la tablette, qui dérive
  après 5 jours en campagne), **ordre d'arbitrage total et déterministe**,
  opérations perdantes **conservées avec leur motif**, distinction entre vraie
  collision (deux auteurs) et auto-correction.
- **`src/lib/domaine/notation.ts`** — seules les feuilles se notent, moyenne
  remontante **par niveau**, `null ≠ 0`, pondération par fonction, barèmes
  (`min` incluse / `max` exclue), échelle sans dérive flottante.
- **`src/app/globals.css`** — système visuel PLEIADE **adapté au terrain** :
  contraste élevé, cibles 48 px, clair par défaut, note en un appui, état de
  synchro permanent.
- **`README.md`** + **`docs/ARCHITECTURE.md`**.
- **Vérifié : 51/51** contrôles, dont l'invariant qui compte — *l'ordre d'arrivée
  des opérations ne change pas le résultat*.

### ⚠ Ce qui N'EST PAS fait, et ne doit pas être annoncé autrement
**Aucun écran n'est écrit.** Le socle (modèle, logique, design, doc) est là ; toute
l'interface reste à produire. `docs/COUVERTURE.md` distingue explicitement
*spécifié* de *implémenté*, et fait référence.

### 🔤 Renommage du dépôt — `leac` → **`app-leac`** (même jour)
**Demande utilisateur** : aligner le nom sur la nomenclature des autres apps.
Fait par l'API GitHub (`PATCH /repos`), dossier local renommé
(`C:\CECPC\pleiade\app-leac`), **remote réaligné**, tests repassés **51/51**.
- ℹ️ GitHub laisse une **redirection** depuis l'ancien nom : un clone existant
  continuerait de fonctionner. Le remote a tout de même été mis à jour
  explicitement — une redirection silencieuse finit toujours par surprendre.
- ⚠ **La nomenclature n'est pas universelle** : **`eho`** est une app du catalogue
  et ne porte PAS le préfixe `app-`. À signaler si l'on veut une règle stricte.

### ⭐ Écran de notation terrain écrit et VALIDÉ (même jour)
**Déclencheur** : l'utilisateur a demandé à *voir* dans un navigateur. Il n'y
avait alors **aucun écran** — le socle seul. Plutôt que de le lui dire sèchement,
j'ai construit l'écran de notation, qui était la prochaine étape proposée.

- **Verdict utilisateur** : *« Ça me plaît, on peut partir là-dessus. »*
  👉 **Le parti pris de design fait désormais référence** pour tous les écrans
  suivants (consigné en `MEMOIRE.md` §7).
- **Ce qui a été montré** : grille S4 LOGISTIQUE **réelle** (libellés du memento),
  note en **un appui** sur une rangée de crans, **moyennes remontant en direct**
  par niveau, compteur rempli/attendu, niveau de barème calculé, pastille de
  synchronisation permanente, les 5 cartouches d'observation.
- ⚠ **Réappuyer sur le cran choisi efface la note** — seul moyen de revenir à
  « non noté » sans menu, et « non noté » n'est pas la note la plus basse.
- Commit **`aeceeb8`**. Vérifié : `tsc` 0, `eslint` 0/0, **51/51**, page en 200.
- ⚠ **Toujours une démonstration** : notes en mémoire, IndexedDB et journal
  d'opérations pas branchés. L'écran le dit à l'utilisateur, en toutes lettres.

#### 🔧 Deux pannes d'outillage rencontrées et corrigées
1. ⚠⚠ **Cache npm du poste corrompu** — `npm install` a échoué (entrée `_cacache`
   manquante pour `exceljs`) **en sortant avec un code de succès** : l'échec était
   donc invisible, et seul `next: command not found` l'a révélé. Réparé par
   `npm cache verify` (31 entrées manquantes purgées, 354 Mo récupérés).
   👉 **Peut expliquer d'autres installs bizarres sur ce poste.**
2. **`eslint.config.mjs` passait par `FlatCompat`**, que `eslint-config-next` 16
   ne supporte plus : re-sérialisation d'une **référence circulaire**
   (`plugins.react`) et trace illisible qui ne nomme pas la cause. Remonté sur le
   montage d'`eho`, qui tourne.

### ⭐⭐ Persistance hors ligne + écran de synchronisation (commit `7c640d1`)
**Contexte** : l'utilisateur a demandé les deux documents manquants au CECPC et
m'a dit de « faire le reste en attendant ». J'ai donc traité les deux chantiers
qui ne dépendent d'aucun document.

#### La base locale n'est **pas un cache**
Elle doit tenir **une semaine sans voir le serveur** et savoir exactement ce
qu'il lui reste à remonter. Un cache, on peut le vider ; ceci, jamais — ce serait
jeter le travail d'un contrôleur. Trois tables aux rôles **distincts** :
- `operations` — **le journal**, la vérité de ce qui n'est pas remonté ;
- `valeurs` — l'état courant, **pure commodité de lecture** (se reconstruirait
  depuis le journal) ; rejouer 4 000 opérations à chaque écran serait absurde ;
- `meta` — identité de l'appareil + **horloge persistée**. ⚠ L'identifiant
  d'appareil doit **survivre aux redémarrages** : c'est lui qui départage deux
  saisies d'horloge égale. S'il changeait, l'arbitrage cesserait d'être
  reproductible et deux postes pourraient diverger.

#### ⭐ Un seul chemin d'écriture, sans exception
On n'écrit **jamais** une valeur : on **émet une opération**, l'état dérivé suit
dans la **même transaction**. ⚠ Si un chemin contournait le journal, la saisie
s'afficherait correctement sur la tablette et **ne remonterait jamais** — le
contrôleur croirait son travail enregistré. C'est la perte silencieuse que la v3
doit rendre impossible.

#### Deux exigences de terrain dans le branchement React
1. **L'appui repeint le cran immédiatement**, la base suit en parallèle. ⚠ Sur
   tablette, un retard de 80 ms se lit comme un **appui raté** — l'utilisateur
   réappuie, et pose deux fois la note.
2. **Si l'écriture locale échoue, l'écran REVIENT en arrière et le dit.** Une
   note affichée mais non enregistrée est le pire état possible : le contrôleur
   passe à la suite en confiance.

#### L'écran de synchronisation répond à trois questions, dans cet ordre
Ce qui n'est pas parti · ce qui est arrivé des autres · ⭐ **ce qui a été
recouvert, et par qui**. La troisième est la seule qui compte : une
synchronisation qui annonce « terminée » **cache les désaccords entre
contrôleurs**, alors qu'un désaccord sur une note est une **information
d'animation**, pas un incident à masquer.
- ⚠ **Les opérations ne sont marquées « remontées » qu'APRÈS accusé.** Marquer
  avant perdrait le travail si l'envoi échouait en route ; renvoyer ne coûte rien
  puisque le serveur déduplique sur l'identifiant d'opération.
- La simulation fait tourner **le même code de fusion** que celui du serveur.

**Vérifié** : `tsc` 0 · `eslint` 0/0 · **51/51** · les deux pages en **200**.
Un avertissement React 19 corrigé au passage (`setState` synchrone dans un effet,
cause de rendus en cascade).

⚠ **Restent non persistées : les observations** (les 5 cartouches). L'écran le dit
en toutes lettres à l'utilisateur.

### Observations persistées + écran de paramétrage ODM (commits `a2f1f0c`, `fe90ede`, `8b51061`)

#### Observations — le piège du texte libre
⚠ Une note se pose en un appui ; une observation se tape **caractère par
caractère**. Une opération par frappe = **des centaines d'opérations pour une
phrase**, journal gonflé et revue de synchronisation noyée sous le bruit.
👉 On reprend la règle **déjà posée par v2.5** (§ II.B, « enregistre à chaque
sortie de case ») **plus un filet : écriture après 800 ms de repos**. ⚠ Sortir
d'un champ **n'est pas garanti sur tablette** — on verrouille l'écran, on bascule
d'application, la batterie lâche. Attendre le `blur` seul, c'est accepter de
perdre **le dernier paragraphe**, donc le plus récent.
- ⭐ **Chaque cartouche est un CHAMP distinct** : deux contrôleurs remplissant
  l'un « points positifs » et l'autre « propositions » **ne peuvent pas se
  recouvrir**. La granularité par champ achète cette propriété gratuitement.
- ⚠ Purge des minuteries au démontage : sans elle, quitter l'écran juste après
  une frappe laisse un `setTimeout` écrire dans un composant mort.

#### ⭐⭐ Paramétrage ODM — deux AVERTISSEMENTS du memento devenus des propriétés du formulaire
1. **La règle de nommage** (§ V.A.1) était écrite **en rouge** : un avertissement
   en rouge dans un memento, c'est **une règle qu'on oublie** — elle reposait sur
   la mémoire d'un officier tapant un champ libre une fois tous les six mois. Les
   exemples du memento le prouvent : `VAP_GTD-INF_BARKHANE10_1RI` a **4 segments**,
   `ANTARES_152RI` en a **2**. 👉 On saisit les morceaux, **l'intitulé se compose**.
2. **Le drapeau** (§ V.A.3) : « *la première personne cochée aura un petit
   drapeau* ». ⚠ **Une conséquence aussi lourde ne peut pas dépendre d'un ordre de
   clic.** Il se donne explicitement, il est nommé, retirer le droit d'observer à
   son porteur **le déplace** au lieu de le laisser orphelin, et si personne ne le
   porte l'écran le dit — sinon aucun commentaire ne remonterait à la réunion
   quotidienne sans que personne comprenne pourquoi.

Aussi : alerte sur les **fonctions obligatoires non pourvues**, affichée au
paramétrage plutôt qu'au déploiement quand il est trop tard ; suivi **vert/gris**
des validations de grille (§ V.A.6) ; poids par fonction, **0 neutralisant** une
fonction sans la retirer de l'équipe.

#### 🔎 Un test a tranché une ambiguïté que je n'avais pas vue
J'avais annoncé la normalisation de l'intitulé comme « testée » **sans l'avoir
testée**. En écrivant les 12 contrôles, ils ont immédiatement révélé une question
non tranchée : **un espace disparaît-il ou devient-il un tiret ?**
👉 **Décision assumée : il devient un TIRET.** « 152 RI » → « 152-RI ». Supprimer
l'espace collerait des mots illisibles (« 1ERRI »), et le memento écrit justement
« GTD-INF » **avec son tiret**. Qui veut « 152RI » le tape sans espace.
**63/63.**

### ⏭️ Prochaine étape
1. **Persister le paramétrage** (même journal d'opérations) — aujourd'hui en
   mémoire.
2. **Tableau de bord de la réunion quotidienne** (§ V.B.9) : domaines, taux de
   remplissage, moyennes, bilan de cycle du porte-drapeau.
3. ⏳ **En attente du CECPC** : format Excel des grilles, modèle de CR.
4. Trancher la **durée de vie du PIN hors ligne**.

---

## 2026-09-17 — Création de l'agent

**Demande utilisateur** : créer dans MINERVE un agent **LEAC** qui **stocke toutes
les données `.md` importantes et le suivi du projet**, avec le réflexe de **tout
mettre à jour à chaque avancée, à l'ouverture et à la fermeture de session**, et
d'**être consulté dès que LEAC est évoqué**.

### Fait
- Dossier `LEAC\` créé avec `README.md`, `MEMOIRE.md`, `JOURNAL.md` et
  `REFERENCES\`. ⭐ **Mémoire et journal séparés dès le départ** — leçon de
  MASTAURIGE, dont la mémoire avait atteint 397 Ko avant d'être scindée.
- Agent ajouté au **registre de `CLAUDE.md`** (23ᵉ), au **compteur de
  `NOYAU\MEMOIRE.md`**, à l'**arbre de routage** et au **prompt système**
  `SYSTEME\PROMPTS\leac.md` — la checklist complète du `CLAUDE.md` racine.
- Les quatre réflexes demandés sont écrits **là où ils s'appliquent** : règle
  d'usage du `README.md`, règles de travail du `MEMOIRE.md`, prompt système, et
  branche de routage.

### ⚠ État
**Rien n'est connu du système LEAC hormis son nom.** L'identité (§1 de la mémoire)
est un tableau de champs ⚠️ à renseigner. **La documentation doit être fournie par
l'utilisateur** — annoncée dans le même message.

### ⏭️ Prochaine étape
1. **Recevoir la documentation**, la classer dans `REFERENCES\`, la résumer dans
   `MEMOIRE.md` §1 et §2.
2. Trancher le **rattachement** : LEAC est-il lié à PLEIADE, à un exercice, ou
   autonome ? Cela déterminera les collaborations de l'agent dans le registre.
