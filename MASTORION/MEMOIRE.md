# MÉMOIRE — MASTORION (état durable)

> **Convention 2 fichiers** : ce fichier = état durable (règles, connaissance plateforme, capacités, roadmap) — doit rester lisible d'un bloc (< 100 Ko). Historique daté → `JOURNAL.md`.
> Dernière mise à jour : 2026-07-27.

---

## Identité & périmètre

- **MASTORION** = plateforme de réseaux sociaux fictifs **nouvelle génération**, travaillée **en parallèle** de l'outillage MASTAURIGE, destinée principalement aux exercices de niveau **division / corps d'armée**.
- Racine : `D:\CECPC\MASTORION\` · Repo cloné GitHub : `D:\CECPC\MASTORION\mastorion-v0` (possède son propre `CLAUDE.md`).
- Raison d'être de l'agent : **transposer le savoir MINERVE/MASTAURIGE** (avatars-camps, matrices LO/GLM26, calendriers D+ avec GELEX, vérificateurs de cohérence, baking d'articles, chartes médias, doctrine ILI, RETEX) **dans l'amélioration de la plateforme**.

## ⚠ Règles en vigueur

1. **Périmètre d'écriture — état au 2026-07-27 (amendé en cours de journée) :**
   - `D:\CECPC\MASTORION\mastorion-v0` (copie de référence GitHub Desktop) → **LECTURE SEULE stricte**, on n'y exécute et n'y modifie rien *(seule exception faite : le `apps/api/.env`, non versionné, tenu en miroir du clone C:)*.
   - `C:\CECPC\MASTORION\mastorion-v0` (clone d'exécution) → **installation/lancement/test AUTORISÉS** (consigne levée par l'utilisateur pour les fichiers **non versionnés** : `node_modules`, `.env`, données). ⚠ **Modifier le CODE SOURCE suivi par git reste soumis à autorisation explicite** — aucune modification de code n'a été faite à ce jour.
   - Analyses, specs et propositions se consignent **côté MINERVE** (ici), pas dans le repo.
2. Clone Git : avant toute intervention future autorisée → `git status` / branche / remote d'abord ; jamais de commit/push sans demande explicite.
   **Convention de branches (utilisateur, 2026-07-27)** : dans `mastorion-v0`, tout le travail se fait sur la branche **`MEYTRE`** (créée par l'utilisateur via GitHub Desktop) — **jamais directement sur `main`** ; `main` reste le miroir du dépôt d'origine (XTalandier). Le repo MINERVE, lui, continue sur `main` (dépôt personnel de l'utilisateur). ⚠ Vérifier la branche active (`git branch --show-current`) avant toute édition future dans le repo.
3. Distinction stricte MASTAURIGE (HTML statique, brigade) / MASTORION (plateforme applicative, division-corps).
4. Règles transverses MINERVE applicables aux contenus : camp d'un persona = registre MASTAURIGE fait foi ; GET ; numéros fictifs ; langue de l'avatar ; pas de détails opérationnels réels.

## Connaissance de la plateforme (analyse initiale — lecture seule)

> Chemins ci-dessous **relatifs à `mastorion-v0/`**. Repo : `https://github.com/XTalandier/mastorion-v0.git`, branche `main`, **1 seul commit** (Xavier TALANDIER — pas d'historique exploitable), arbre propre. ~276 fichiers, ~28 000 lignes TS/Python. Version applicative : **0.2.49** (`apps/api/package.json`).

### Objet
Plateforme type **Mastodon pour exercice militaire** (contexte ORION 26, red/blue team) : réseau social fictif complet + back-office animation + cockpit de veille + module d'analyse NLP. Trois publics : animateurs (`/admin/`, rôle `APP_ADMIN`), veilleurs (`/cockpit/` + sentinel-ui, rôle `COCKPIT`), joueurs (`/social/`, sans rôle — **pas de rôle « entraîné » explicite**).

### Architecture (monorepo npm workspaces + Turborepo, Node 22)
| App | Rôle | Stack |
|---|---|---|
| `apps/api` (port 3000) | Backend + scheduler + CLI | Express 5, Prisma 7 (multi-provider MySQL/SQLite/PG via driver adapters), JWT, node-cron, Winston/Seq, ExcelJS |
| `apps/web` (4200) | Front social joueurs | Angular 21 + PrimeNG 21, signals |
| `apps/admin` (4201) | Back-office animation | Angular 21, Chart.js, xlsx, faker |
| `apps/cockpit` (4202) | Veille | Angular 21 |
| `apps/sentinel-api` (3100) + `sentinel-ui` + `sentinel-worker` | Analyse « Orion » : topics/narratifs par NLP | Express + pg · Angular + d3 · Python 3.12 (BERTopic, embeddings pgvector 768, LLM **Ollama** qwen2.5:3b) |
| `migrator/` + `apps/api/src/migrator.ts` | Import instance Mastodon réelle (SSH+PG) | Node |
| `vanilla-cockpit/` | Prototype HTML du cockpit — code de référence, non déployé ; contient **Margaret** (assistant IA de veille, non porté en Angular) | JS vanilla |

Docker : `docker-compose.yml` (mastorion + mariadb 11 + seq + phpmyadmin + postgres) · `docker-stack.yml` (Swarm) · `docker-compose.sentinel.yml` (overlay pgvector + worker + ollama). `entrypoint.sh` fait `prisma db push` en prod (pas de migrations rejouées) et échange le client Prisma pré-compilé selon `DB_PROVIDER`. Déploiement « réel » : bare repo git + hook post-receive sur branche `cockpit` (`deploy/2-setup-server.sh`). **Aucun WebSocket/SSE — tout est polling HTTP** (choix assumé, 10-60 s).

### Modèle de données (Prisma : `apps/api/prisma/schema/{base,social}.prisma`)
- **`User` = fiche persona** : identité + 14 champs de persona (age, genre, pays, origine, religion, caractere, langage, activite, observations, qualifications, `aime`/`deteste` en JSON…), `rawPassword` en clair (assumé : distribution des comptes), `mastoId` (réconciliation Mastodon), `masstalkUsername` (réconciliation MASSTALK — écrit mais jamais lu).
- **`Group` = seul mécanisme de camp** : `name` + `color`, sans type ni hiérarchie. Sert au ciblage des likes/boosts synthétiques, aux sources cockpit, au reporting.
- **`Scenario` + `ScenarioItem` = la matrice d'injects** : `functionalId` (n° d'inject), `delta` (minutes relatives au parent), `replyTo` (chaînage), `nbLikes`/`nbRetweets` + groupes cibles, statuts draft→publishing→published/error. **Pas de date absolue par inject** (cumul récursif des deltas depuis `scenario.startDate`, `scheduler.ts:148-170`). **Pas d'entité Exercice** au-dessus. Mode « ShitStorm » (`replyToPostId`).
- **Social** : `SocialPost` (boost = post à contenu vide via `repostOf`, linkPreview 5 champs, `scheduledAt`), `SocialComment` **plat à 1 seul niveau** (pas de thread récursif), likes/follows/notifications/hashtags/mentions.
- **Sentinel (PG séparé)** : topics avec embeddings + `sentinel_analysis_grids` à **pôles** définis par l'utilisateur (affinités topic↔pôle par similarité) + métriques spike/EWMA + relations entre topics (recouvrement d'entités/auteurs, corrélation temporelle).
- Observabilité : `SystemLog` indexé par `scenarioId`/`functionalId` (traçabilité par inject), `SystemMetric`, `CockpitDashboard`.

### Mécanismes clés
- **Scheduler** (`apps/api/src/scheduler.ts`) : cron chaque minute, verrou atomique optimiste par item, publication auto des injects + likes/boosts par groupes, erreurs → `scenario.errors` + SystemLog.
- **`POST …/items/validate`** : dry-run de matrice (3 contrôles seulement : compte existe, pas d'auto-référence, parent présent) — **LE point de greffe des vérificateurs type MASTAURIGE**.
- **`POST …/items/auto-organize`** : répartition automatique **aléatoire** (jitter) des injects sur la durée du scénario.
- **`POST /api/social/posts/:id/turbo-boost`** (admin) : amplification manuelle en cours d'exercice (N likes+boosts ciblés par groupes).
- **Import/export XLSX** partout (users avec feuille `_data` = taxonomie + listes déroulantes ; injects via `scenario-edit.ts`) ; réconciliation MASSTALK interactive (`toolbox.ts --reconcile`, lit `uploads/reconcile.json`).
- **Impersonation** : header `X-Act-As` réservé `APP_ADMIN` (« In the name of »).

### État de maturité — points de vigilance
- **Zéro test, pas de CI, pas de lint** ; un seul TODO dans le code.
- **Docs en retard sur le code** : README/CLAUDE.md du repo ignorent Sentinel, monitoring, reporting, turbo-boost, auto-organize ; réfèrent un `.env.example` inexistant. → **compléter, ne pas s'y fier seuls**.
- **⚠ Secrets committés** : `apps/api/migrator.env` (mots de passe + IP réels), `root@2.2.2.40` en dur dans les scripts deploy, `JWT_SECRET` défaut faible (`mastorion-dev-secret`). À signaler au mainteneur.
- Fragilités structurelles : `db push --accept-data-loss` en prod, patch de schéma par `sed` dans `entrypoint.sh`, `likeGroupIds` en CSV sans FK, `generateLikes` prend les N premiers users (pas d'aléa), `/api/testfail` exposé, CORS en dur localhost.
- Traces d'exploitation réelle ORION 26 (conteneurs `orion26-*`, mapping Mastodon peuplé).

### Fichiers à lire en priorité
`CLAUDE.md` · `docs/{cockpit-spec,sentinel-spec,deploiement}.md` · `prisma/schema/{base,social}.prisma` · `src/{index,scheduler,auth,toolbox}.ts` · `src/admin/{scenario-items,users}.ts` · `src/cockpit/index.ts` · `src/social/post-service.ts` · `src/excel-export.ts` · `sentinel-worker/src/{db,config,qualifier,relations}.py` · `sentinel-api/src/grids/grids.routes.ts` · `admin/.../timeline.ts` · `entrypoint.sh`.

## Procédure de test local (dev) — établie 2026-07-27

Poste : Node v24 ✅ · npm 11 ✅ · Docker Desktop ✅ (installé + WSL2 le 2026-07-27 ; CLI : `%LOCALAPPDATA%\Programs\DockerDesktop\resources\bin\docker.exe`, pas dans le PATH). Contraintes découvertes :
- ⚠⚠ **D: est en exFAT → `npm install` IMPOSSIBLE sur D:** (les symlinks des workspaces npm échouent en EISDIR, non convertible en NTFS). D'où **DEUX clones** :
  - `D:\CECPC\MASTORION\mastorion-v0` = copie de **référence** (GitHub Desktop de l'utilisateur) — on n'y exécute RIEN ;
  - **`C:\CECPC\MASTORION\mastorion-v0` = clone d'EXÉCUTION** (NTFS ; branche MEYTRE, origin repointé sur GitHub) — c'est là qu'on installe/lance/teste. ⚠ Risque de divergence entre les deux copies : synchroniser via commits/push (jamais de copie de fichiers à la main), et à terme ne garder qu'une seule copie de travail (à trancher avec l'utilisateur).
  - Prérequis d'accès git au repo D: : `git config --global --add safe.directory` (fait — l'exFAT déclenche « dubious ownership »).
- Base : conteneur `mastorion-db` (mariadb:11, port 3306, user/mdp/db `mastorion`, `--restart unless-stopped` → survit aux reboots ; `docker start mastorion-db` si arrêté).
  ⚠ **Créé sans volume nommé** → les données vivent dans un volume **anonyme** (nom = hash). Elles survivent aux arrêts/redémarrages et aux reboots, mais **`docker rm mastorion-db` les rendrait quasi irrécupérables** (volume orphelin). Ne jamais supprimer ce conteneur. Si les données de test deviennent précieuses : migrer vers un volume nommé ou vers `docker-compose.yml` (qui monte `./data/mysql`) + s'appuyer sur `deploy/backup-db.sh`.
- `apps/api/.env.example` **n'existe pas** (README menteur) → créer `apps/api/.env` à la main (`dotenv/config` chargé par l'API, Prisma CLI le lit aussi).
- `base.prisma:8` = `provider = "mysql"` **en dur** → le dev exige MariaDB/MySQL (SQLite n'est viable qu'en prod Docker via le patch `sed` d'`entrypoint.sh`).
- Compte admin : `ensureAdmin()` crée TOUJOURS un admin au 1er démarrage (défaut `admin@mastorion.local`, mdp aléatoire **affiché dans les logs** si `ADMIN_PASSWORD` absent) → fixer `ADMIN_EMAIL`/`ADMIN_PASSWORD` dans le .env pour maîtriser le login.
- Étapes : MariaDB 11 (conteneur Docker seul, sans le service `mastorion`) → `.env` (DB_PROVIDER=mysql, DATABASE_URL=mysql://…@localhost:3306/mastorion, ADMIN_*, JWT_SECRET) → `npm install` racine → `npm run dev` (turbo : api 3000 + web 4200 + admin 4201 + cockpit 4202).
- ⚠ `npm run seed:full` dans `apps/api` (= `toolbox.ts --full`) **RESET toute la base + uploads** et ne crée QU'UN utilisateur : `test@test.fr` / `password123` (APP_ADMIN) — il **supprime** l'admin du `.env` (recréé par `ensureAdmin()` seulement au prochain redémarrage de l'API). Ne jamais le lancer sur une base qu'on veut garder.
- **Démarrage quotidien** : Docker Desktop lancé → conteneurs `mastorion-db` + `sentinel-pg` + `sentinel-worker` repartent seuls (restart policy) → `cd C:\CECPC\MASTORION\mastorion-v0 && npm run dev` → attendre les builds Angular. Arrêt : Ctrl+C (les conteneurs peuvent rester up).
- **Sentinel en dev (monté 2026-07-27)** : `npm run dev` lance DÉJÀ sentinel-api (:3100) et sentinel-ui (→ **:4203**, repli auto car :4200 pris par web). S'y ajoutent : conteneurs `mastorion-v0-sentinel-pg-1` (pgvector:pg16, :5433) + `mastorion-v0-sentinel-worker-1` (build `Dockerfile.sentinel` target sentinel-worker — Python en conteneur car le poste a Python 3.14, trop récent pour BERTopic/torch), lancés par `docker compose -f docker-compose.sentinel.yml up -d --build sentinel-pg sentinel-worker` avec `MARIADB_PASSWORD=mastorion MARIADB_USER=mastorion MARIADB_DATABASE=mastorion` en env. Modèles Ollama **natifs** requis (pullés) : `qwen2.5:3b` (qualification) + `snowflake-arctic-embed:137m` (embeddings 768d). ⚠ **JWT partagé** : sentinel-api ne lit pas `apps/api/.env` et utilise le défaut `mastorion-dev-secret` → le `.env` de l'API principale a été aligné sur ce même secret (sinon « Token invalide » sur :3100). Le worker ne loggue rien (stdout Python bufferisé) : preuve de vie = ses 8 tables `sentinel_*` dans pgvector (`docker exec … psql -U sentinel -d sentinel -c "\dt"`). Clustering à partir de **50 posts** (`BOOTSTRAP_THRESHOLD`), cycle 10-120 s.
- **Ports dev complets** : API 3000 · social 4200 · admin 4201 · cockpit 4202 · **sentinel-ui 4203** · sentinel-api 3100 · MariaDB 3306 · pgvector 5433 · Ollama natif 11434.
- ⚠ **Piège « Token invalide » partout dans l'IHM** : le JWT est stocké côté navigateur (localStorage) et signé avec `JWT_SECRET`. **Tout changement de `JWT_SECRET` invalide instantanément toutes les sessions ouvertes** — l'IHM reste affichée (elle croit l'utilisateur connecté) mais chaque appel API renvoie 401 « Token invalide », donnant des listes vides + toasts rouges. **Remède : se déconnecter / se reconnecter** (jeton neuf). Vécu le 2026-07-27 après l'alignement du secret pour Sentinel. Même symptôme attendu à l'expiration naturelle (JWT valable **7 jours**) → réflexe n°1 devant « Token invalide » : reconnexion, pas de débogage serveur.
- ⚠⚠ **DETTE À SOLDER AVANT TOUT DÉPLOIEMENT SERVEUR** : notre `.env` local utilise `JWT_SECRET=mastorion-dev-secret` (le **défaut du code**, aligné le 2026-07-27 pour faire dialoguer api et sentinel-api). Sur un serveur multi-postes, ce secret connu permettrait à quiconque de **forger un jeton APP_ADMIN**. À la mise en production : générer un secret aléatoire et le poser dans `.env.prod` (il est lu par les deux API via `env_file`). Même vigilance pour `apps/api/migrator.env` (mots de passe réels commités) et `ADMIN_PASSWORD`.

## Modèle de déploiement cible (confirmé avec l'utilisateur le 2026-07-27)

MASTORION est une **application client-serveur** : installée sur **un serveur**, tous les postes y accèdent par le réseau via un navigateur (rien à installer côté client). C'est LA rupture avec MASTAURIGE (HTML statique distribué en ZIP, une copie par poste, fusions manuelles offline↔réseau, localStorage comme 2ᵉ canal) — une seule base fait foi, tout le monde travaille simultanément dessus. C'est ce qui rend le niveau **division/corps** tenable.

- **En prod, un seul port** : `build.sh` compile les 3 fronts Angular **dans `apps/api/public/{social,admin,cockpit}`** (`--base-href`), servis par le conteneur API unique → `http://<serveur>:${APP_PORT:-3080}/social/` · `/admin/` · `/cockpit/`. Les ports 4200-4203 sont un **artefact du mode dev** (serveurs Angular séparés), ils n'existent pas en production.
- Deux voies de déploiement outillées : `deploy.sh` (Docker **Swarm** — menu Setup/Update/Status/Destroy, image chargée depuis un `.tar.gz`) ou `docker compose --env-file .env.prod up -d`. Mise à jour « à chaud » possible par `git push deploy cockpit` (bare repo + hook post-receive, cf. `deploy/2-setup-server.sh`).
- **Conçu pour un réseau isolé/sans Internet** : `Dockerfile.builder` + `prepare.sh` produisent une image avec les `node_modules` embarqués, exportable en archive → c'est bien un déploiement en enceinte militaire fermée qui est prévu. Sauvegardes : `deploy/backup-db.sh` (dump toutes les 4 h, rétention 3 j).
- Traces d'un déploiement réel ORION 26 : conteneurs `orion26-mastorion-1` / `orion26-mariadb-1`, serveur cible `2.2.2.40` en dur dans les scripts.
- À prévoir côté serveur si Sentinel est voulu : overlay `docker-compose.sentinel.yml` + un **Ollama** (CPU suffisant mais lent — dimensionner la machine).
- Cockpit accessible avec le compte admin (`requireCockpit` accepte APP_ADMIN).
- ⚠ Lancer l'appli crée des fichiers NON versionnés (node_modules, .env, data MariaDB) — le code suivi par git reste intact ; ne jamais commiter le `.env`.

## ⭐ Bibliothèques d'univers (personas/groupes par exercice) — besoin utilisateur + proposition 2026-07-27

**Besoin exprimé** : pouvoir charger *un ensemble cohérent* de personas + groupes selon l'exercice (Skolkan/GET : Arnland-Mercure-Bothnia pour GUILLAUME & MINOTAURE · jeu ORION 26 · futurs univers avec d'autres pays), **sans que les personas des autres univers existent** dans la base (pays différents → risque d'incohérence). Demande d'options **sans modification** de la plateforme à ce stade.

**Capacités d'import vérifiées** (`admin/users.ts:180-265` + `admin/components/import-users/import-users.ts`) — très favorables :
- **1 classeur XLSX = 1 univers ; 1 ONGLET = 1 groupe** (`import-users.ts:556` : `groupsSet.add(row._sheet)`) — les groupes/camps sont **créés automatiquement** s'ils n'existent pas ; colonne `groups` multi-valeurs séparée par `;` cumulable.
- Colonnes reconnues : `id, username, display_name, email, password, bio, groups, avatar` + **les 14 champs de persona** (age, genre, pays, label, origine, religion, situation, caractere, langage, activite, observations, qualifications, `aime`/`deteste` en `;`).
- **Upsert** (masto_id → id → username → email) : réimporter mto à jour, ne duplique pas. Écran de **prévisualisation éditable** avant import.
- ⚠ L'import **n'efface jamais** → charger un univers sur un autre les MÉLANGE : toujours **partir d'une base vierge** (`RESTAURER.bat`).
- ⚠ `avatar` = **URL**, pas de fichier téléversé → les portraits doivent être joignables : déposer les images dans `apps/api/uploads/users/` et pointer `avatar` sur `/api/uploads/users/<fichier>` (c'est pourquoi l'instantané `.sql` + dossier `uploads` est le complément naturel du XLSX).

**Architecture proposée (recommandée)** : **MINERVE = la bibliothèque (source de vérité, versionnée git) · MASTORION = base d'exécution jetable, rechargée au montage de l'exercice.** Cohérent avec la doctrine anti-divergence (leçon Tikhanov) et tranche la question ouverte de la roadmap n°3 : **le camp fait foi côté MINERVE**, MASTORION n'en est qu'une projection.
- *Niveau 1 (0 modif, faisable tout de suite)* : `MASTORION\BIBLIOTHEQUES\<UNIVERS>\` = `personas.xlsx` (1 onglet par camp) + `avatars\` + `README.md`. Montage = base vierge → import.
- *Niveau 2 (0 modif, confort)* : après import + dépôt des avatars, un `SAUVEGARDER.bat` → `UNIVERS_<NOM>.sql` (+ images) = bascule d'univers en un double-clic. **Discipline : le XLSX reste le maître, l'instantané n'est qu'un cache** (ne pas rejouer le piège MASTAURIGE du « quelle copie fait foi »).
- *Niveau 3 (nécessite du code — à spécifier puis négocier avec le mainteneur)* : notion d'`Univers`/`Library` sur `Group`+`User`, filtre d'univers actif dans l'Admin → l'éditeur d'injects ne proposerait QUE les comptes de l'univers actif (supprime le risque d'erreur à la racine).
- ❌ *Option écartée* : préfixer les noms de groupes (`SKOLKAN/…`, `ORION26/…`) et tout laisser cohabiter — gratuit, mais les personas étrangers restent sélectionnables dans l'éditeur d'injects = exactement l'erreur de cohérence à éviter.

### ✅ 1ʳᵉ bibliothèque produite (2026-07-27) — `BIBLIOTHEQUE_TEST_3_EXERCICES.xlsx`

`MASTORION\BIBLIOTHEQUES\BIBLIOTHEQUE_TEST_3_EXERCICES.xlsx` (+ `README.md`) — **220 personas** dédoublonnés : 3 onglets = 3 groupes (CAMP ROUGE 107 · CAMP BLEU 61 · CAMP NEUTRE 52), colonne `groups` = PAYS/EXERCICE/faction CASW. Généré par **`MASTORION\OUTILS\generer_bibliotheque.py`** (versionné, relançable, lecture seule sur les sources).

**Sources et priorité appliquée** (demande utilisateur : **MINOTAURE > GUILLAUME > ORION**) :
| Source | Chemin | Apport |
|---|---|---|
| Avatars 7BB | `AURIGE 7BB\…\LOCALSTORAGE_WEB_VERSION\moteur\avatars.js` | 35 avatars + camps + **commentaires curatés** (réutilisés en bio) |
| EHO 7BB | `…\Sites\Trombinoscope\bios.js` | 59 fiches narratives (Parcours/Objectifs/Forces/Faiblesses/RS) — 5 correspondent à des avatars |
| Avatars 2BB | `AURIGE 2BB\00_Boites à outils\MASTAURIGE\WEB\avatars.js` | 13 avatars (11 déjà en 7BB) |
| Registre | `MASTAURIGE\MEMOIRE.md` (tableaux `\| @handle \|`) | rôles éditoriaux 2BB |
| **CASW ORION 26** | `01 ORION 26\…\99-TOOLS\setup\orion26-stobo\avatars_casw_ia_usable.md` | ⭐ **222 personas avec TOUS les champs MASTORION** (âge, genre, pays, label, origine, religion, situation, caractère, langage, activité) + comptes Mastodon (id/pseudo/mdp/email) + bios |

⭐ **Découverte structurante** : le fichier CASW ORION 26 est **déjà au modèle de données de MASTORION** (la plateforme a été bâtie sur le modèle MASSTALK/CASW) → conversion quasi 1:1, aucune invention de données.
**Chiffres de recouvrement** : 11 avatars communs 7BB↔2BB · seulement 9/35 (7BB) et 6/13 (2BB) présents dans CASW → **la majorité des avatars AURIGE ont été créés hors base ORION**. Remplissage obtenu : bio 83 %, âge 90 %, pays 90 %, caractère 67 %. Contrôlé : **0 doublon** username/email, 0 champ obligatoire vide, colonnes toutes reconnues par l'import.
**Limites** : ~17 % sans bio (avatars AURIGE sans fiche nulle part) · **portraits non résolus** (colonne `avatar` = URL ; ORION pointe vers `masstalk-api.orion.fr` hors ligne, AURIGE = fichiers locaux → MASTORION affiche les initiales) · mots de passe repris de CASW sinon générés par la plateforme.

**Point clé** : le contenu des bibliothèques **existe déjà dans MINERVE** (registre avatars MASTAURIGE + `avatars.js` + `bios.js` du trombinoscope pour Skolkan ; 222 avatars CASW pour ORION 26) → c'est un travail de **conversion vers le format XLSX MASTORION**, pas de création. Débouché : un pipeline unique MINERVE → MASTORION.

## Repartir sur une base vierge / sauvegarder (outillage créé 2026-07-27)

**Outillage MINERVE ajouté** — ⚠ **écrit par nous, ne fait PAS partie du dépôt `mastorion-v0`** (vérifié : 0 `.bat` versionné dans le projet, `git status` propre). Le projet ne fournit que `deploy/backup-db.sh` (script **Linux** pour le **serveur** : cron 4 h, conteneur `orion26-mariadb-1`) — sans équivalent poste Windows, d'où ces scripts.
**Deux emplacements** : copie **de référence versionnée** dans `MINERVE\MASTORION\OUTILS\` (+ son `README.md`) · copie **d'exploitation** dans `C:\CECPC\MASTORION\SAUVEGARDES\` (à côté des `.sql`). Toute modification doit être reportée dans les deux.
Testé et validé (groupe témoin inséré → restauré → disparu) :
- `BASE_VIERGE.sql` — instantané de l'**état vierge de référence** (1 user `test@test.fr`, 0 groupe/scénario/inject/post), figé le 2026-07-27.
- `SAUVEGARDER.bat` — **demande un NOM** (ex. `UNIVERS SKOLKAN`) ; Entrée = nom daté automatique. Produit `<NOM>.sql` + `<NOM>_uploads\` (images). Propose d'écraser si le nom existe.
- `RESTAURER.bat` — liste les sauvegardes/univers par leur nom, sélection par numéro, confirmation « OUI », recharge base **et** images. ⚠ Rappelle de se **reconnecter** après (les comptes changent → jeton invalide).
- **Bascule d'univers = `RESTAURER.bat` + numéro + OUI + reconnexion** (~10 s). D'où l'importance de **nommer** les sauvegardes.
- 🛠 Pièges batch rencontrés lors de l'écriture de ces scripts (à réutiliser pour tout futur `.bat` MINERVE) : ne pas invoquer `docker.exe` par chemin entre guillemets dans un `for /f` (préférer **ajouter son dossier au `PATH`** en tête de script) · éviter `find`/`wmic` (absents ou détournés selon l'environnement — utiliser `for /f` + `powershell Get-Date`) · **toujours quoter les deux côtés d'un `if "%A%"=="%B%"`** · le bloc `set "V=%V:x=%"` de nettoyage de caractères casse sur `::` → préférer vérifier le résultat (`if not exist … goto erreur`). ⚠ **Tester un `.bat` interactif en pipant plusieurs lignes fausse le test** : `set /p` avale tout le tampon (faux « syntaxe incorrecte ») — piper **une seule** valeur à la fois.
- Commandes sous-jacentes : `docker exec mastorion-db mariadb-dump -umastorion -pmastorion --databases mastorion > f.sql` et `docker exec -i mastorion-db mariadb -umastorion -pmastorion < f.sql`.

**Moyens natifs de la plateforme (pour mémoire) :**
- `npm run seed:full` (= `toolbox.ts --full`) → `resetDb()` (`toolbox.ts:69-92`) **vide** : scenario_items, scenarios, tout le social (posts/commentaires/likes/follows/notifs/hashtags/mentions), user_groups, user_roles, users, **+ les fichiers de `uploads/`** ; puis recrée `test@test.fr`/`password123`. ⚠ **Ne supprime PAS la table `groups`** (les camps survivent), ni `system_logs`/`system_metrics`/`cockpit_dashboards`. Un argument numérique (`--full 50`) génère N personas + posts de démo.
- Suppression ciblée dans l'IHM Admin (un scénario, un persona) — le bon geste au quotidien.
- Table rase totale : supprimer le conteneur + son volume et relancer (`prisma db push` au démarrage recrée le schéma, `ensureAdmin()` recrée l'admin) — ⚠ voir la mise en garde sur le volume anonyme.

**Conseil donné à l'utilisateur** : préférer **sauvegarder avant d'expérimenter** plutôt que remettre à zéro après — car une fois un jeu de personas construit, on veut effacer les scénarios sans perdre les personas, ce que `seed:full` ne sait pas faire.

## 📊 Récap des injects joués (2026-07-27) — `RECAPS\RECAP_INJECTS_GUILLAUME_MINOTAURE.xlsx`

Vue « qu'a-t-on joué ? », **1 onglet par exercice**, générée par `OUTILS\generer_recap_injects.py` (lecture seule sur l'outillage MASTAURIGE) : **GUILLAUME 2BB = 70 injects / 176 produits** (Tweet 105 · Article 60 · Courrier 8 · Tract 3) · **MINOTAURE 7BB = 84 injects / 105 produits** (Tweet 60 · Article 28 · Courrier 9 · Tract 8). Colonnes : n°, nom, **types de produit**, nb, description, date, état, destinataires, LO, détail des produits. Sous-injects rattachés à leur parent (fonction `racine()` : gère `07.01.04Bi` → `07.01.04i` ET `07.02.I08B` → `07.02.I08`).

**Où vivent les produits — diffère par exercice** (à retenir pour tout futur outil) :
| | 2BB / GUILLAUME | 7BB / MINOTAURE |
|---|---|---|
| Articles/tracts/courriers | `MELMIL\melmil_inject_index.js` (`MASTAURIGE_INDEX` : code → `{key,type,label}`, types tweet/article/tract/courrier) + cards en dur dans `index_master.html` | `moteur\articles_data.js` (champs `num`, **`type`**, `site` où site ∈ …/tract/courrier) — `MASTAURIGE_INDEX` y est **vide** (passage au pilotage par données) |
| Tweets | `tweets_data.js` (racine) | `moteur\tweets_data.js` |
| Format des clés JS | **non quotées** (`{code: "..."}`) | quotées (JSON strict) |
→ tout lecteur de ces fichiers doit **retirer les commentaires JS** ET **quoter les clés nues** (fonctions `sans_commentaires()` + `quoter_cles()` du script).

**⚠ Écarts de source constatés (pas des bugs) :** (1) **22 injects 2BB joués mais ABSENTS du socle MELMIL** (`04.01.*`, `07.07.*`, `07.08.*`, `01.01.119i`, `08.01.01Ai.R1/R2`…) — `melmil_data.js` 2BB figé au 2026-06-02, jamais régénéré ; ils figurent quand même dans l'onglet, marqués « ⚠ hors matrice MELMIL », nommés depuis les commentaires `<!-- code — libellé -->` d'`index_master.html`. (2) **4 injects sans produit** : 08.02.03i, 08.03.01i (2BB) · 05.09.I06, 05.11.I04 (7BB). (3) **9 produits HTML 7BB non déclarés dans `articles_data.js`** (Olamao_Declaration_Officielle, HEX/ONU/OTAN/TV4 Guterres, TV4_Panique, TM_POW_Morhange…) → invisibles du récap ; les 9 autres fichiers orphelins sont des `_TEMPLATE.html`.

**Convention de rangement** : `MASTORION\BIBLIOTHEQUES\` = fichiers **à importer** dans la plateforme · `MASTORION\RECAPS\` = classeurs **de consultation** (chacun avec son `README.md`).

## Où vivent les données — carte de stockage (vérifiée 2026-07-27)

Question récurrente de l'utilisateur (« les fichiers exportés sont-ils stockés dans Docker ? ») → **non**. Trois emplacements distincts, à ne pas confondre :

| Quoi | Où | Remarque |
|---|---|---|
| **Fichiers d'import/export** (Admin → Exporter/Importer) | **PC de la personne qui utilise le navigateur** (dossier Téléchargements) | Fichiers de **transit uniquement**, la plateforme n'en garde aucune copie. Format réel = **XLSX**, pas JSON (`groups-users.ts:1196` : `a.download = mastorion-export-<date>.xlsx`) |
| **Les données elles-mêmes** (personas, groupes, scénarios, injects, posts) | **Base MySQL → conteneur `mastorion-db`** | C'est LA source de vérité |
| **Médias téléversés** (avatars, images de posts) | **Disque Windows** en dev : `C:\CECPC\MASTORION\mastorion-v0\apps\api\uploads\{users,social}` (`upload.ts:10`, `UPLOADS_DIR`) | ⚠ **PAS dans Docker** en dev, car l'API tourne nativement. En **prod** l'API est conteneurisée → `${DATA_DIR}/uploads` monté sur le serveur |

⚠ **Différence conceptuelle majeure avec MASTAURIGE** : là-bas, l'export JSON **ÉTAIT** la donnée (vidage du localStorage — d'où les fusions manuelles, les instances master, les divergences). Ici l'export n'est qu'une **copie de travail** ; la vérité reste en base. Ne jamais raisonner « le fichier fait foi » sur MASTORION.

Traces de JSON dans la plateforme (pour mémoire) : conversion interne XLSX→JSON par le front avant POST · workspaces cockpit `.orionworkspace` (désormais persistés en base, table `cockpit_dashboards`) · `uploads/reconcile.json` pour la CLI MASSTALK · colonnes JSON en base (`errors`, `aime`/`deteste`, `likeGroupIds`).

## Ce que la plateforme NE fait PAS (vérifié — ne pas le promettre à l'utilisateur)

- **MASSTALK n'existe plus en tant qu'outil.** Le **panneau Admin remplace intégralement** l'ancien outil d'injection externe d'ORION 26 (`docs/cockpit-spec.md:15` : « toute notion de masstalk correspond à admin ; toute notion de mastodon correspond à social »). Correspondances : tableau d'injects → items de scénario (import/export XLSX) · injection programmée → scheduler auto · amplification → likes/RT par camp + `turbo-boost`. Vestiges MASSTALK : champ `masstalkUsername` (écrit, jamais lu) + CLI `toolbox.ts --reconcile` (import d'un `reconcile.json` de personas MASSTALK).
- **AUCUNE messagerie type RocketChat / Mattermost / Signal** — vérifié le 2026-07-27 par `grep` sur tout le repo (0 occurrence) et sur le schéma Prisma : ni conversation, ni message privé, ni salon. Le seul registre conversationnel est **public** (posts + commentaires **à 1 seul niveau** + mentions). Si l'utilisateur cherche RocketChat, c'est soit un outil **externe** du dispositif CECPC, soit un **besoin non couvert** → voir roadmap n°10.
- **Margaret** (chatbot analyste de veille) : existe **seulement** dans `vanilla-cockpit/res/app.js:2455-2530`, jamais portée en Angular, et dépendait d'un serveur externe absent du repo (`http://2.2.2.23:3333`).
- Pas d'entité **Exercice** au-dessus des scénarios, pas de rôle « entraîné » explicite, pas de temps réel (WS/SSE), pas de threads > 1 niveau.

## Capacités / travaux

- **2026-07-27 — Analyse initiale complète du repo** (lecture seule) : synthèse ci-dessus ; **rapport intégral avec toutes les références `fichier:ligne` → `MASTORION\ANALYSE_REPO_2026-07-27.md`** (à consulter au `grep` pour tout travail sur la plateforme).

## Roadmap / idées de transposition du savoir MINERVE (issues de l'analyse initiale)

1. **Vérificateurs de cohérence** (équivalent CONTROLES A-I de `verifier_mastaurige.py`) → greffer sur `POST …/items/validate` : émetteur↔camp↔narratif, langue/registre vs persona, plausibilité chronologique, collisions hashtags inter-camps, mentions vers comptes inexistants, longueur max, médias manquants.
2. **Colonnes de matrice LO** manquantes sur `ScenarioItem` : LO/effet visé, narratif, audience cible, indicateur de succès — + import/export XLSX correspondant. (Équivalent MELMIL/GLM26.)
3. **Camps typés** : `Group` n'a ni type ni hiérarchie ; MASSTALK envoie déjà `groupes[{name, type}]` mais le `type` est jeté (`toolbox.ts:561`) → accroche immédiate. Trancher un jour : **qui fait foi pour le camp** (registre MASTAURIGE vs base plateforme) — question ouverte anti-divergence (leçon Tikhanov).
4. **Auto-organize doctrinal** : remplacer la répartition aléatoire par des courbes d'intensité par phase / tempo par camp (savoir synchromatrice EXPERT_INFLUENCE).
5. **Faux articles de presse** : forger les 5 champs `linkPreview*` depuis l'inject (aujourd'hui les injects n'ont AUCUNE preview) puis générateur d'articles statiques type MASTAURIGE (chartes BC1/TV4/OTAN réutilisables).
6. **Grilles Sentinel à pôles = réceptacle naturel des LO/narratifs GLM26** ; enrichir le prompt de qualification (`qualifier.py`) avec la doctrine EXPERT_INFLUENCE ; croiser `author_overlap` avec les `Group` déclarés (mesure de « fuite » entre camps).
7. **Entité Exercice** (phases, D-day, jalons MSEL) au-dessus de `Scenario` ; axe « J+n » explicite dans la timeline admin (attention leçon GELEX : jours sautés).
8. **Générateur de personas** cohérents camp/âge/origine/langage (remplacer faker) ; enrichir la feuille `_data` XLSX = taxonomie animateur sans toucher au code.
9. Divers : porter Margaret (assistant IA de veille du vanilla-cockpit) en Angular — **d'autant que le poste a déjà Ollama en natif** —, threads > 1 niveau, rôle « entraîné » explicite, requalification à la demande (seul TODO du repo).
10. **Canal messagerie fictive** (question ouverte soulevée par l'utilisateur le 2026-07-27 : « où est RocketChat ? ») : la plateforme n'offre qu'un réseau social **public**. Un canal privé (messagerie type RocketChat/Signal : conversations fermées, groupes, captures d'écran fuitées) est un vecteur d'inject **structurellement différent**, très pertinent au niveau division/corps. À clarifier avec l'utilisateur : outil externe déjà en place au CECPC (→ articulation à étudier) ou brique à concevoir (→ spec à écrire).
