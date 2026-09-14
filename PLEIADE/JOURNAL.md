# JOURNAL — PLEIADE (historique chronologique, append-only)

> Comptes rendus datés des travaux sur le système PLEIADE. Les règles et l'état durable sont dans `MEMOIRE.md`.

---

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
