# MASTORION — Rapport d'analyse initiale du repo (lecture seule)

> **Rapport intégral** de la première analyse de `D:\CECPC\MASTORION\mastorion-v0`, réalisée le 2026-07-27 sans aucune modification du dossier. La synthèse condensée et la roadmap sont dans `MEMOIRE.md` ; ce fichier est la **référence détaillée** (chemins `fichier:ligne`) à consulter au `grep` pour tout travail futur sur la plateforme.

**Périmètre** : `D:\CECPC\MASTORION\` ne contient qu'un seul élément : le repo cloné `mastorion-v0`.
**Repo** : `https://github.com/XTalandier/mastorion-v0.git`, branche `main`, **un seul commit** (`b7c6332` — "first commit", Xavier TALANDIER). Pas d'historique exploitable, 276 fichiers versionnés, ~28 000 lignes de TS/Python. Arbre de travail propre au moment de l'analyse.

⚠️ Tous les chemins ci-dessous sont **relatifs à `mastorion-v0/`**.

---

## 1. Objet et vision

### Ce que disent les docs

- `README.md:3` : « Plateforme de type Mastodon comprenant un réseau social, un panneau d'administration et un cockpit de veille. »
- `CLAUDE.md:3` : « Plateforme de type Mastodon **pour exercice militaire** — réseau social, administration, cockpit de veille. »
- `docs/cockpit-spec.md:5` : « application web de veille Mastodon… Conçue pour un **contexte d'exercice militaire (type ORION 26)**, elle permet à un ou plusieurs veilleurs de suivre l'activité, être alertés des nouvelles publications, analyser les tendances et exporter les données. »
- `docs/sentinel-spec.md:3` : « **Exercice d'influence red/blue team** sur un réseau social simulant un pays envahi (parallèle Ukraine : narratifs d'un envahisseur qui "libère pour la bonne cause" vs force qui se défend avec cohabitation OTAN). »

### Fonctionnalités effectivement présentes

1. **Réseau social fictif complet** (clone Mastodon/Twitter) : posts, médias, likes, boosts (retweets), commentaires, follows, hashtags, mentions, notifications, link preview Open Graph, posts programmés (`apps/api/src/social/`, `apps/web/`).
2. **Moteur de scénarios/injects** : matrices d'injects planifiées en minutes relatives, publiées automatiquement par un scheduler cron (`apps/api/src/scheduler.ts`, `apps/api/src/admin/scenario-items.ts`).
3. **Back-office animation (admin)** : gestion des comptes/personas, groupes (camps), génération en masse, import/export XLSX, timeline visuelle des injects, monitoring système (`apps/admin/`).
4. **Cockpit de veille** (successeur du prototype HTML `vanilla-cockpit/`) : dashboard de suivi de sources (comptes + hashtags), alertes sonores, workspaces, reporting horaire par groupe (`apps/cockpit/`, `apps/api/src/cockpit/index.ts`).
5. **Sentinel / "Orion"** : outil d'analyse **neutre** red/blue par NLP (embeddings + BERTopic + LLM Ollama) qui fait émerger les narratifs et calcule des « rapports de force » (`apps/sentinel-*`, `docs/sentinel-spec.md`).
6. **Migrator Mastodon** : import d'une vraie instance Mastodon (PostgreSQL via tunnel SSH) vers Mastorion (`apps/api/src/migrator.ts`, `migrator/`).

### Publics

| Public | Interface | Rôle technique |
|---|---|---|
| Animateurs / white cell | `/admin/` (port 4201) | `APP_ADMIN` |
| Veilleurs / analystes (red & blue) | `/cockpit/` (4202) + sentinel-ui | `COCKPIT` ou `APP_ADMIN` |
| Joueurs / entraînés | `/social/` (4200) | aucun rôle |

Cf. `README.md:204-214` et `apps/api/src/auth.ts:77-93`.

---

## 2. Architecture technique

### 2.1 Monorepo

`package.json` (racine) : workspaces npm `apps/*` + Turborepo (`turbo.json` : tâches `dev`, `dev:debug`, `build`). npm 10.9.2, Node 22.

| App | Chemin | Rôle | Port dev | Version |
|---|---|---|---|---|
| **api** | `apps/api/` | Backend Express 5 + Prisma + scheduler + CLI | 3000 | **0.2.49** (`apps/api/package.json:3`) |
| **web** | `apps/web/` | Front social (Angular 21 + PrimeNG 21) | 4200 | 0.0.0 |
| **admin** | `apps/admin/` | Front animation/back-office | 4201 | 0.0.0 |
| **cockpit** | `apps/cockpit/` | Front veille | 4202 | 0.0.0 |
| **sentinel-api** | `apps/sentinel-api/` | API analyse (Express 5 + pg brut, **pas NestJS** malgré la spec) | 3100 | 0.1.0 |
| **sentinel-ui** | `apps/sentinel-ui/` | Front analyse (Angular + **d3**) | 4200 (ng serve) | 0.0.0 |
| **sentinel-worker** | `apps/sentinel-worker/` | Worker Python 3.12 (BERTopic/embeddings) | — | — |

> ⚠️ **Docs périmées** : `README.md:14-26` et `CLAUDE.md:22-92` ne décrivent que **3 frontends** et ignorent totalement les 3 apps `sentinel-*`, `apps/admin/src/app/pages/monitoring/`, `scenario-create/`, `apps/cockpit/src/app/pages/reporting/` et `components/workspace-dialog/`. Le code est en avance sur la doc.

Pas de dossier `packages/` : **aucun code partagé** entre apps (les types sont dupliqués côté front/back).

### 2.2 Stack

- **Backend** : Node 22 ESM, Express 5, JWT (`jsonwebtoken`), bcryptjs, Multer (uploads), node-cron, Winston + winston-daily-rotate-file + winston-seq, ExcelJS, ssh2, commander (`apps/api/package.json`).
- **ORM** : **Prisma 7** avec *driver adapters* dynamiques — `apps/api/src/db.ts` charge `@prisma/adapter-pg`, `@prisma/adapter-mariadb` ou `@prisma/adapter-better-sqlite3` selon `DB_PROVIDER`. Schéma multi-fichiers : `apps/api/prisma/schema/base.prisma` + `social.prisma` (feature `prismaSchemaFolder`).
- **BDD** : MySQL/MariaDB par défaut, SQLite et PostgreSQL supportés. 15 migrations Prisma dans `apps/api/prisma/migrations/` (du `20260405170350_init` au `20260406204126_add_like_retweet_group_ids`) + une migration SQL manuelle hors Prisma : `apps/api/migrations/add-system-logs-columns.sql`.
- **Frontends** : Angular 21 standalone + signals, PrimeNG 21, Chart.js (admin/cockpit), d3 (sentinel-ui), xlsx + jszip + @faker-js/faker (admin), emoji-picker-element (web).
- **Analyse** : Python — torch CPU, `bertopic`, `hdbscan`, `umap-learn`, `sentence-transformers`, `pgvector`, `mysql-connector-python` (`apps/sentinel-worker/requirements.txt`). LLM via **Ollama** (`qwen2.5:3b` par défaut, embeddings `snowflake-arctic-embed:137m`, dim 768 — `apps/sentinel-worker/src/config.py:16-17`).
- **Message broker** : **aucun**. La spec évoquait RabbitMQ (`docs/sentinel-spec.md:40`) mais l'implémentation retenue est un **polling SQL** du worker sur la base MySQL Mastorion (`apps/sentinel-worker/src/ingestion.py`).

### 2.3 Services Docker

**`docker-compose.yml`** (dev/prod mono-nœud) :

| Service | Image | Port hôte→conteneur | Dépendances |
|---|---|---|---|
| `mastorion` | `mastorion:latest` (build `.`) | `${APP_PORT:-3080}`→3000 | `mariadb` (service_healthy), healthcheck sur `/api/config` |
| `mariadb` | `mariadb:11` | `${MARIADB_PORT:-3306}` | healthcheck `healthcheck.sh` |
| `seq` | `datalust/seq` | `${SEQ_PORT:-5380}`→80 | — |
| `postgres` | `postgres:16-alpine` | `${PG_PORT:-5432}` | *(uniquement pour un dump Mastodon importé)* |
| `phpmyadmin` | `phpmyadmin:latest` | `${PHPMYADMIN_PORT:-8080}`→80 | `mariadb` |

Volumes bind sur `${DATA_DIR:-./data}/{uploads,logs,mysql,seq,postgres}`.

**`docker-stack.yml`** (Docker Swarm) : mêmes 4 services (pas de `postgres`), variables passées en clair au lieu de `env_file`, `deploy.update_config.order: start-first`, `restart_policy: on-failure`, 1 réplique. Pas de healthcheck, pas de `depends_on` (non supporté en Swarm).

**`docker-compose.sentinel.yml`** (overlay, à combiner : `docker compose -f docker-compose.yml -f docker-compose.sentinel.yml`) :
- `sentinel-pg` : **`pgvector/pgvector:pg16`**, port `${SENTINEL_PG_PORT:-5433}`→5432, healthcheck `pg_isready`.
- `sentinel-worker` : build `Dockerfile.sentinel` target `sentinel-worker`, monte `./apps/sentinel-worker/src` en volume (hot-reload), lit Mastorion via `MASTORION_DB_*` (souvent `host.docker.internal:3306`) et écrit dans `sentinel-pg`.
- `sentinel-api` : profil `prod` uniquement, port `${SENTINEL_API_PORT:-3100}`.
- `ollama` : `ollama/ollama`, profil `prod`, port 11434, volume `${DATA_DIR}/ollama`.

### 2.4 Dockerfiles

- **`Dockerfile`** (image principale, multi-stage) : stage build → `npm ci` + `npx turbo build` ; puis **astuce clé** — il génère et compile le client Prisma **trois fois** (sqlite, mysql, postgresql) via `sed` sur `provider = "..."` dans `base.prisma`, et copie les 3 clients dans `/app/prisma-clients/{sqlite,mysql,postgresql}`. Stage prod = `node:22-alpine`, entrypoint `entrypoint.sh`, expose 3000.
- **`entrypoint.sh`** : au démarrage, mappe `DB_PROVIDER` → provider Prisma, **remplace `/app/dist/generated/prisma` par le client pré-compilé correspondant**, patche le schéma (`sed` provider + réinjection des `@db.Text` que SQLite ne supporte pas, lignes 25-36), lance `prisma db push --accept-data-loss`, puis `node dist/index.js`. → **pas de migrations versionnées en prod, c'est du `db push`**.
- **`Dockerfile.builder`** + `prepare.sh` + `deploy/1-build-builder-image.sh` : image avec `node_modules` pré-installés, exportée en tar.gz — conçue pour **déployer sur un serveur sans accès Internet**.
- **`Dockerfile.sentinel`** : 4 stages — `ui-build` (Angular), `api-build` (tsc), `sentinel-api` (sert l'UI en statique depuis `./public`), `sentinel-deps`/`sentinel-worker` (python:3.12-slim + gcc/g++/libpq + cython/numpy puis requirements).

### 2.5 `migrator/` (racine) vs `apps/api/src/migrator.ts`

Deux choses distinctes :
- **`migrator/`** (racine) : mini-projet standalone Node (`pg` + `xlsx`). `migrator/dump_users.js` exporte les comptes d'une instance Mastodon réelle (SQL sur `accounts`/`users`, reconstruction du chemin d'avatar `/system/accounts/avatars/xxx/yyy/zzz/original/…`, strip HTML de la bio) vers un XLSX ré-importable dans l'admin (colonnes `masto_id, username, display_name, email, password, bio, groups, avatar`). `migrator/mastodon_users_mapping.json` est une **table de correspondance `masto_id → id Mastorion`** déjà remplie (~ID Mastorion à partir de 1000).
- **`apps/api/src/migrator.ts`** (820 lignes) : le vrai migrateur applicatif — tunnel SSH (ssh2), connexion PG Mastodon, sous-commandes `--init`, `--dry-run`, `--users`, `--follows`, `--posts`, `--comments`, `--reset-social`, `--rehash`, `--all`, `--date=`. Résolution de la chaîne de réponses (`resolveParentPost`, ligne 732), téléchargement des médias (HTTP depuis l'instance ou copie locale via `MASTO_SYSTEM_PATH`). Config : `apps/api/migrator.env`.

### 2.6 `vanilla-cockpit/`

Le **prototype v0 du cockpit en HTML/JS vanilla** (`index.html` + `res/app.js`, 3455 lignes, sans build). `docs/cockpit-spec.md:7` : « La première version est disponible dans le dossier vanilla-cockip. L'objectif est de refondre toute l'application en angular. » Il reste dans le repo comme **référence fonctionnelle** de `apps/cockpit/`.

Il contient une fonctionnalité **non portée en Angular** : **Margaret**, un assistant IA de veille (`vanilla-cockpit/res/app.js:2455-2530`) — prompt par défaut « Tu es Margaret, analyste de veille sur un Mastodon militaire… une seule phrase de synthèse (max 200 caractères) », appel `POST {margaretUrl}/analysis` toutes les 60 s avec les 30 derniers toots, GIF `margaret-thinking.gif`, prompt personnalisable en localStorage. Serveur Margaret par défaut : `http://2.2.2.23:3333` (ligne 233) — **service externe absent du repo**.

---

## 3. Modèle de données / concepts métier

Sources : `apps/api/prisma/schema/base.prisma` et `apps/api/prisma/schema/social.prisma`.

### 3.1 Comptes / avatars / personas — `User` (`base.prisma:11-56`, table `users`)

Bien au-delà d'un simple compte : c'est une **fiche persona**.

- Identité : `username` (unique), `displayName`, `email`, `passwordHash`, **`rawPassword`** (mot de passe en clair, volontairement conservé pour que les animateurs distribuent les comptes ; nettoyé pour les `APP_ADMIN` — `apps/api/src/admin/users.ts:463-465`).
- Visuel : `avatarUrl`, `bannerUrl`, `bio` (`@db.Text`).
- Mapping externe : **`mastoId` BigInt unique** (`masto_id`) pour la réconciliation Mastodon, **`masstalkUsername`** (`masstalk_username`, unique) pour la réconciliation MASSTALK — écrit uniquement par `apps/api/src/toolbox.ts:659`.
- **Attributs de persona** : `age`, `genre`, `pays`, `label`, `origine`, `religion`, `situation`, `caractere`, `langage`, `activite`, `observations` (Text), `qualifications` (Text), **`aime`** et **`deteste`** (Text contenant un **tableau JSON de strings**).
- `enabled` (désactivation d'un compte, contrôlé au login — `apps/api/src/auth.ts:163-166`).

Ces champs sont exposés/édités par `apps/api/src/admin/users.ts` (listing, `PATCH /:id`, `POST /import`, `GET /field-values` pour l'autocomplétion) et exportés en XLSX avec **data-validation Excel** par `apps/api/src/excel-export.ts` (feuille `Utilisateurs` + feuille `_data` contenant les valeurs de référence, listes déroulantes générées, multi-valeurs séparées par `" ; "`).

### 3.2 Camps / factions — `Group` + `UserGroup` (`base.prisma:69-89`)

Modèle **volontairement générique** : `Group { name unique, color (#6364ff par défaut) }` et table de jonction `user_groups`. C'est le seul mécanisme de « camp » : il sert à
- filtrer/segmenter les utilisateurs dans l'admin,
- **cibler les likes et retweets synthétiques** (`likeGroupIds`/`retweetGroupIds` sur les injects, `apps/api/src/social/post-service.ts:94-142`),
- constituer les listes de sources du cockpit (`GET /api/cockpit/groups`),
- agréger le reporting horaire (`POST /api/cockpit/reporting`).

**Pas de notion native de "camp red/blue", ni de hiérarchie de groupes, ni d'appartenance pondérée.**

### 3.3 Exercices / scénarios / injects — `Scenario` + `ScenarioItem` (`base.prisma:91-131`)

C'est **l'équivalent Mastorion de la matrice d'injects**.

`Scenario` : `name`, `startDate`, `endDate`, `status` ∈ {`draft`, `playing`, `paused`, `ended`, `error`} (`apps/api/src/admin/scenarios.ts:89`), **`replyToPostId`** (mode « ShitStorm » : tous les items racine commentent un post cible existant), `errors` (tableau JSON d'erreurs de publication), `createdAt`.

`ScenarioItem` (un inject) :
- **`functionalId`** — identifiant fonctionnel textuel, unique par scénario (`@@unique([scenarioId, functionalId])`) : l'équivalent du n° d'inject.
- `accountId`/`username` — le compte émetteur (résolu par username, nullable si non résolu).
- `message` (Text), `mediaUrl`/`mediaType`.
- **`delta`** — décalage **en minutes relatif au parent** (défaut 1).
- **`replyTo`** — `functionalId` du parent → arborescence de fils de discussion.
- `nbLikes`, `nbRetweets`, `likeGroupIds`, `retweetGroupIds` (**CSV d'IDs de groupes**, pas de relation) → engagement synthétique ciblé.
- `status` ∈ {`draft`, `publishing`, `published`, `error`}, `socialPostId` (lien vers le post réellement créé), `sortOrder`.

**Calendrier D+** : il n'y a **pas** de date absolue par inject. L'heure de publication est calculée par remontée récursive de la chaîne `replyTo` en cumulant les `delta` : `computeAbsoluteMin()` (`apps/api/src/scheduler.ts:148-170`), comparé à `elapsedMin = now - scenario.startDate`. La timeline admin (`apps/admin/src/app/components/timeline/timeline.ts`) rend cette arborescence avec des lignes de grille **heure et jour** (`grid-hour`, `grid-day`, `tick-day`) — c'est le plus proche d'un calendrier D+.

**Pas d'entité "Exercice"** au-dessus du scénario : un scénario = une campagne d'injects datée. Plusieurs scénarios peuvent tourner en parallèle.

### 3.4 Posts / fils / médias (`social.prisma`)

- `SocialPost` : `content` (Text), `mediaUrl`/`mediaType`, **`repostOf`** (auto-relation = boost/retweet ; un boost est un post avec contenu vide), `linkPreview{Url,Title,Desc,Image,Domain}`, **`mastoId`** BigInt unique, **`scheduledAt`** (post programmé), `createdAt`/`updatedAt` (l'`updatedAt` est bumpé par les boosts pour remonter dans le feed — `post-service.ts:137-141`).
- `SocialComment` — les **réponses sont des commentaires plats sur un post**, pas des posts. Conséquence : **pas de thread récursif à la Mastodon**, la profondeur est de 1 niveau (un inject `replyTo` devient un commentaire sur le post du parent — `scheduler.ts:189-208`).
- `SocialLike`, `SocialFollow`, `SocialNotification` (types : `follow`, `like`, `boost`, `comment`, `mention`, `fav_comment`, `new_post`), `SocialPostHashtag`, `SocialPostMention`, `SocialHashtagFollow`.
- **Médias** : simple chemin fichier, un média par post/commentaire. Stockage `uploads/users/{userId}.ext` et `uploads/social/{postId}.ext` (`apps/api/src/upload.ts`, `CLAUDE.md:237`).

### 3.5 Exploitation / observabilité

- `SystemLog` (`base.prisma:133-147`) : journal métier en base, types `tick`/`publish`/`error`/`scheduler`, avec `scenarioId` + `functionalId` indexés → **traçabilité inject par inject**.
- `SystemMetric` (`base.prisma:149-160`) : RAM/disque/CPU échantillonnés par `apps/api/src/metrics-collector.ts`.
- `CockpitDashboard` (`base.prisma:162-174`) : workspaces cockpit persistés en base (JSON `data` = layout/zoom/collapsed, JSON `config` = sources/catégories), par utilisateur.

### 3.6 Modèle Sentinel (PostgreSQL séparé)

Créé impérativement par le worker : `apps/sentinel-worker/src/db.py:30-140`.
`sentinel_authors`, `sentinel_posts` (embedding `vector(768)`, `topic_id`), `sentinel_topics` (`label`, `thesis`, `entities` JSONB, `tone`, `keywords[]`, `centroid vector(768)`, `x2d`/`y2d`, **`relevance`**, `post_count`, `author_count`, `is_active`), `sentinel_topic_metrics` (fenêtres `10m/1h/6h/24h`, `volume`, `velocity`, `distinct_authors`, `ewma_mean/std`, `is_spike`), `sentinel_topic_relations` (`entity_overlap`, `author_overlap`, `temporal_correlation`), `sentinel_state`, et surtout :
- **`sentinel_analysis_grids`** (`name`, `poles` JSONB, `pole_embeddings` JSONB) et **`sentinel_topic_pole_affinities`** (`affinities` JSONB, `dominant_pole`) — c'est-à-dire des **grilles d'analyse à pôles définis par l'utilisateur**, avec affectation des topics par similarité d'embedding (`apps/sentinel-api/src/grids/grids.routes.ts`).

### 3.7 Rôles utilisateurs

`UserRole` (`base.prisma:58-67`) : chaîne libre, **seules deux valeurs utilisées** : `APP_ADMIN` et `COCKPIT` (`apps/api/src/auth.ts:77-93`). Il **n'existe pas de rôle "joueur"/"entraîné"** : l'entraîné est un `User` sans rôle. Le JWT (7 j) porte `{id, email, roles[]}`.

**Impersonation** : header `X-Act-As: <userId>`, honoré par `authMiddleware` et `optionalAuth` **uniquement si le JWT contient `APP_ADMIN`** (`apps/api/src/auth.ts:38-42` et `59-62`). Widget « In the name of » dans `apps/web/src/app/components/right-panel/right-panel.ts`.

---

## 4. API et intégrations

### 4.1 Routes montées — `apps/api/src/index.ts:54-75`

| Préfixe | Fichier | Protection |
|---|---|---|
| `/api/auth` | `src/auth.ts` | public (register/login), JWT (me/profile) |
| `/api/config` | `index.ts:44` | public : `version`, `create_account`, `require_auth`, `social_post_max_length`, `admin_url` |
| `/api/social/posts|users|notifications|hashtags` | `src/social/*.ts` | `optionalAuth` par défaut ; **global** si `REQUIRE_AUTH=true` (`index.ts:59`) |
| `/api/admin/groups|users|scenarios|scenarios/:id/items|monitoring` | `src/admin/*.ts` | `authMiddleware` + `requireRole("APP_ADMIN")` |
| `/api/cockpit` | `src/cockpit/index.ts` | `authMiddleware` + `requireCockpit` |
| `/api/uploads/**` | statique | public |
| `/api/testfail` | `index.ts:78` | endpoint de test d'erreur (renvoie une erreur aléatoire) — **exposé même en prod** |

### 4.2 Endpoints notables

**Social** (`src/social/posts.ts`) : `GET /feed`, `/following`, `/scheduled`, `/favorites`, `POST /preview-link`, `GET /:id/retweeters`, `/:id/comments`, `POST /` (multipart, champ `scheduled_at`), `PATCH/DELETE /:id`, `POST /:id/like`, `/:id/boost`, `/:id/comments`, et **`POST /:id/turbo-boost`** (`posts.ts:541`, `APP_ADMIN` only) : injecte à la demande N likes + N boosts sur un post existant, ciblés par groupes → **outil d'amplification manuelle en cours d'exercice**.

**Admin scénarios** (`src/admin/scenario-items.ts`) :
- `POST /import` (remplacement complet optionnel, mapping souple `id|functional_id`, `username|compte`),
- **`POST /validate`** — *dry-run* : vérifie l'existence des comptes, l'auto-référence, et l'existence du parent `reply_to` → **vérificateur de cohérence déjà présent** (lignes 334-365),
- **`POST /auto-organize`** (lignes 246-331) : répartit automatiquement les injects sur la durée du scénario, shuffle des racines, gap moyen ± jitter 50-150 %, enfants à 1 min puis 2-10 min,
- `POST /:itemId/publish` (publication forcée, bypass scheduler), `POST/DELETE /:itemId/media`.

**Cockpit** (`src/cockpit/index.ts`) — API *pensée pour ressembler à l'API Mastodon* (cf. `docs/cockpit-spec.md:17`) : `GET /feed` (`since_id`/`max_id`), `/users/:username/statuses`, **`/users/:username/activity`** (posts + commentaires fusionnés), `/hashtags/:tag/statuses`, `/accounts/lookup?acct=`, `/stats`, `/trending`, `/search`, **`POST /poll`** (batch : toutes les sources en **une seule requête** — remplace le polling N-requêtes du prototype vanilla), `GET /groups`, **`POST /reporting`** (comptage horaire dédupliqué par groupe de sources), CRUD `/dashboards`.

**Sentinel API** (`apps/sentinel-api/src/`) : `/api/health` (public), puis JWT+`COCKPIT|APP_ADMIN` (`apps/sentinel-api/src/auth.ts`) sur `/api/topics` (+ `/map`, `/map/playback`, `/:id`), `/api/relations`, `/api/timeline`, `/api/metrics/summary`, `/api/sentinel-health`, `/api/users-map` (+ `/playback`), `/api/grids` (+ `POST /:id/compute`, `GET /:id/map`). **Le JWT est celui de Mastorion** (même `JWT_SECRET`) → SSO de fait ; le proxy dev `apps/sentinel-ui/proxy.conf.json` route `/api/auth` vers 3000 et le reste vers 3100.

### 4.3 Mécanisme d'injection de contenu (équivalent MASSTALK)

**Deux voies distinctes :**

1. **Le scheduler** (`apps/api/src/scheduler.ts`) — le cœur. Cron `* * * * *`, verrou global `running` (ligne 8). À chaque tick : publication des posts programmés (`publishScheduledPosts`), puis requête unique de tous les `ScenarioItem` `draft` dont le scénario est `playing` et `startDate <= now`. Pour chaque item : calcul de `absoluteMin` par remontée des parents, vérification que le parent est `published`, **verrou atomique optimiste** (`updateMany where status:"draft" → "publishing"`, ligne 178), création post OU commentaire (ou double écriture en mode ShitStorm, ligne 211-226), génération des likes/boosts par groupes, passage à `published` + `socialPostId`. Toute erreur → item `error` + push dans `scenario.errors` JSON + `SystemLog`. Fin : `checkCompletion()` bascule le scénario en `ended`/`error`.
2. **Réconciliation MASSTALK** (`apps/api/src/toolbox.ts:454-727`) : `node dist/toolbox.js --reconcile --username|--password|--groups|--profile`, lit `uploads/reconcile.json`, un **tableau de personas MASSTALK** typé lignes 456-472 : `{ id, prenom, nom, comptes: [{id, username, password, email, platform}], groupes: [{name, type}], portrait_url, … }`. Il repère le compte `platform === "Mastodon"`, retrouve l'utilisateur Mastorion **par email**, et propose interactivement d'aligner username (`sanitizeUsername`), mot de passe, groupes ou profil. Script d'exploitation : `apps/api/deploy-reconcile.sh`.
   > Note terminologique : `docs/cockpit-spec.md:15` pose « Toute notion de **masstalk correspond à admin** ; toute notion de **mastodon correspond à social** ».

### 4.4 Import / export

| Flux | Format | Où |
|---|---|---|
| Import utilisateurs (upsert par `masto_id` → `id` → `username` → `email`) | JSON depuis XLSX parsé côté front | `POST /api/admin/users/import` (`admin/users.ts:180`) |
| Export utilisateurs | **XLSX** avec feuille `_data` + listes déroulantes | `GET /api/admin/users/export` + `src/excel-export.ts` ; aussi CLI `mastorion dump` (`src/cli.ts:93`) |
| Import injects | XLSX → JSON (`xlsx` côté admin, `apps/admin/src/app/pages/scenario-edit/scenario-edit.ts:24,466-478`) | `POST .../items/import` + `/validate` |
| Export injects | XLSX (`exportXlsx()`) | scenario-edit |
| Export veille | JSON / CSV (`;`) | `vanilla-cockpit/res/app.js`, cf. `docs/cockpit-spec.md:491-501` |
| Workspaces cockpit | `.orionworkspace` (JSON) | spec §12.2 ; en Angular désormais persistés en base (`cockpit_dashboards`) |
| Import Mastodon | SQL/SSH + XLSX | `apps/api/src/migrator.ts`, `migrator/dump_users.js` |

### 4.5 Temps réel

**Aucun WebSocket, aucun SSE** — recherche exhaustive : **0 résultat**. Tout est du **polling HTTP** :

| Où | Intervalle |
|---|---|
| `apps/web/.../feed/feed.ts:134` | 60 s (nouveaux posts) |
| `apps/web/.../right-panel.ts:193` | 30 s |
| `apps/web/.../sidebar.ts:291` (notifs) | 30 s |
| `apps/web/.../following.ts:73`, `notifications.ts:152` | 15 s |
| `apps/web/services/config.service.ts:29` | 60 s (détection de nouvelle version → bandeau de refresh) |
| `apps/admin/.../monitoring.ts:411-413` | 30 s logs, **5 s métriques** |
| `apps/admin/.../scenario-edit.ts:1058` | polling de l'état des items |
| `apps/cockpit` | intervalle configurable 10-60 s (`layout.ts:64`, `PollingService`) |

Choix assumé : `docs/sentinel-spec.md:132` « Rafraîchissement par polling (10-30 s), pas besoin de WebSocket vu le différé ».

---

## 5. Déploiement et exploitation

### 5.1 Dev

```
npm install
cp apps/api/.env.example apps/api/.env      # ⚠ ce fichier .env.example n'existe PAS dans le repo
cd apps/api && npx prisma db push
npm run dev                                  # turbo dev : api + web + admin + cockpit
npm run dev:debug                            # idem + --inspect (9229)
```
(`README.md:28-41`) — l'API est démarrée par `prisma db push && prisma generate && tsx watch src/index.ts` (`apps/api/package.json:8`). Les fronts passent par `proxy.conf.json` vers `localhost:3000`.
Sentinel se lance à la main en dev (commentaire en tête de `docker-compose.sentinel.yml`).

Prérequis : Node 22, npm, Docker + buildx, Docker ≥ 24 / Compose v2 côté serveur (`docs/deploiement.md:5-9`).

### 5.2 Build

`build.sh` : lit la version dans `apps/api/package.json`, `npm run build` (turbo → les 3 fronts Angular buildent **directement dans `apps/api/public/{social,admin,cockpit}`** avec `--base-href /xxx/`), puis `docker buildx build` (`--platform linux/amd64` par défaut, `--arm64`, `--multi`) et export `dist/mastorion-<version>.tar.gz`. Option `--no-export`.

### 5.3 Prod

- **Compose** : `cp .env.prod.example .env.prod` puis `docker compose --env-file .env.prod up -d` (`docs/deploiement.md:61-83`). Au 1er lancement : MariaDB crée la base → entrypoint fait `db push` → `ensureAdmin()` (`apps/api/src/index.ts:138-174`) crée le compte `APP_ADMIN` (mot de passe aléatoire affiché dans les logs si `ADMIN_PASSWORD` absent).
- **Swarm** : `deploy.sh`, menu interactif 4 options — **1 Setup** (mkdir data, `docker swarm init`, `docker load` du dernier tar.gz de `dist/`, `docker stack deploy -c docker-stack.yml mastorion`), **2 Update** (load + `docker service update --image … --force`), **3 Status**, **4 Destroy** (`docker stack rm`, volumes conservés).
- **Déploiement par git push** : `deploy/2-setup-server.sh` installe sur `root@2.2.2.40` un **bare repo `/opt/mastorion.git`** avec un hook `post-receive` qui ne se déclenche que sur la branche **`cockpit`** : checkout → `docker run mastorion-builder npx turbo build --concurrency=1` → `docker cp` de `dist/`, `prisma/`, `package.json`, `entrypoint.sh` et des `public/{social,admin,cockpit}/browser` dans le conteneur **`orion26-mastorion-1`** → `docker restart`. Usage : `git push deploy cockpit`.
- **Sauvegardes** : `deploy/backup-db.sh` — `mariadb-dump --all-databases` gzippé toutes les 4 h via cron, rétention 3 jours, conteneur `orion26-mariadb-1`.
- **Migrator en prod** : `apps/api/build-migrator.sh` (prisma generate + tsc) puis `apps/api/deploy-migrator.sh` (bundle tar.gz minimal → scp → `docker cp` → `docker exec -it … node dist/migrator.js "$@"`). `apps/api/deploy-reconcile.sh` fait de même pour `reconcile.json`.
- **Exploitation courante** : `docker compose exec -it mastorion node dist/toolbox.js --new-user | --full N`, `node dist/migrator.js`, `docker compose logs -f mastorion` (`README.md:188-202`).

### 5.4 Configuration

`.env.prod.example` + `README.md:82-133` : `DB_PROVIDER`, `DATABASE_URL`, `MARIADB_*`, `PG_*`, `DATA_DIR`, ports (`APP_PORT` 3080, `PHPMYADMIN_PORT` 8080, `SEQ_PORT` 5380, `MARIADB_PORT` 3306), `ADMIN_*`, `REQUIRE_AUTH`, `CREATE_ACCOUNT`, `SOCIAL_POST_MAX_LENGTH` (500), `SOCIAL_UPLOAD_{PHOTO,VIDEO}_MAX_SIZE` (10/50 Mo), `LOG_TARGETS` (`console,file,seq`), `LOG_LEVEL`, `SEQ_URL`/`SEQ_API_KEY`. Non documentées : `JWT_SECRET` (défaut **`"mastorion-dev-secret"`** — `apps/api/src/auth.ts:7`), `ADMIN_URL`, `UPLOADS_DIR`, `LOG_DIR`, `SENTINEL_*`, `OLLAMA_*`, `MASTORION_DB_*`, `BOOTSTRAP_THRESHOLD`, `EWMA_ALPHA`, `SPIKE_SIGMA`.

---

## 6. État de maturité

**Version** : `0.2.49` (`apps/api/package.json:3`) — versionnage piloté par l'API, exposé via `/api/config`, utilisé pour le tag Docker et la détection de mise à jour côté client.

**Points forts** : le cœur (social + injects + scheduler + cockpit) est complet, cohérent et manifestement éprouvé en exercice réel (traces de production : conteneurs `orion26-*`, `migrator.env` rempli avec de vraies IP, `mastodon_users_mapping.json` peuplé, migration SQL manuelle rétro-appliquée).

**Faiblesses / zones incomplètes :**

1. **Zéro test.** Aucun `.spec.ts`, `.test.ts` ni `test_*.py` dans tout le repo, alors que les `tsconfig.spec.json` existent et que les `package.json` déclarent `"test": "ng test"`. Pas de CI (`.github/` absent), pas de lint configuré.
2. **Un seul TODO** dans tout le code : `apps/sentinel-ui/src/app/pages/settings/settings.ts:157` — `// TODO: API endpoint to trigger requalification`.
3. **Documentation en retard** : ni `README.md` ni `CLAUDE.md` ne mentionnent Sentinel, le monitoring admin, le reporting cockpit, les dashboards persistés, `turbo-boost`, `auto-organize`, `cli.ts`. `README.md:32` référence `apps/api/.env.example` **qui n'existe pas**. `README.md:227` référence `src/seed.ts` (renommé `toolbox.ts`). `CLAUDE.md:194` liste `social_hashtag_follows` mais oublie `system_logs`, `system_metrics`, `cockpit_dashboards`.
4. **Divergence spec/implémentation Sentinel** : la spec annonce NestJS + RabbitMQ + phi4-mini + nomic-embed-text (`docs/sentinel-spec.md:36-42`) ; le code fait Express + polling SQL + `qwen2.5:3b` + `snowflake-arctic-embed:137m` (`apps/sentinel-worker/src/config.py`). Sentinel n'est pas dans `docker-compose.yml` principal.
5. **Secrets committés** ⚠️ : `apps/api/migrator.env` contient des **mots de passe et IP réels** (`MASTO_SSH_PASSWORD`, `MASTO_PG_PASSWORD`, `2.2.2.20`). Les scripts `deploy/2-setup-server.sh`, `apps/api/deploy-migrator.sh`, `deploy-reconcile.sh` codent en dur `root@2.2.2.40`. `JWT_SECRET` a un défaut faible. `rawPassword` stocke les mots de passe en clair en base (choix fonctionnel assumé mais à connaître).
6. **Limites structurelles** : commentaires à **1 seul niveau** (pas de thread récursif) ; `likeGroupIds`/`retweetGroupIds` en CSV de chaînes (pas de FK) ; `errors` et `aime`/`deteste` en JSON dans des colonnes Text ; `db push --accept-data-loss` en prod ; `entrypoint.sh` patche le schéma par `sed`/regex (fragile aux renommages de champs) ; `generateLikes` prend les N **premiers** utilisateurs (`take: count`) — pas d'aléa réel (`post-service.ts:104`) ; `/api/testfail` exposé en prod ; CORS limité en dur à `localhost:4200-4202` (`index.ts:30`).
7. **`vanilla-cockpit/`** : code mort/référence, non buildé, non déployé ; Margaret n'a **pas** été portée en Angular.
8. **`masstalkUsername`** n'est écrit qu'à un seul endroit (`toolbox.ts:659`) et jamais lu — mapping MASSTALK inexploité côté API.

---

## 7. Le `CLAUDE.md` du repo — synthèse

Fichier de **385 lignes de contexte, sans aucune instruction impérative** (pas de « do/don't », pas de règles de commit, pas de commandes de test). C'est une **carte du territoire**, pas une charte. Contenu :

1. **Stack** (l.5-12) : Node 22 / Express 5, Angular 21 + PrimeNG 21, Prisma 7, Turborepo, Docker Compose/Swarm, Winston.
2. **Pointeurs docs** (l.14-18) vers `docs/deploiement.md`, `docs/cockpit-spec.md`, `docs/sentinel-spec.md`.
3. **Arborescence commentée fichier par fichier** (l.22-92) : rôle de chaque module API et de chaque dossier front.
4. **Commandes** (l.94-142) : dev, toolbox, migrator, build/deploy, prod Docker.
5. **Compte admin auto** (l.144-148).
6. **Architecture API** (l.150-178) : routes partagées / social / cockpit / admin, et **impersonation `X-Act-As`**.
7. **Tables DB** (l.180-198).
8. **Scheduler** (l.199-205).
9. **Config `.env`** (l.207-218) et **services Docker** (l.220-230).
10. **Conventions** (l.232-243) — la partie la plus utile pour un agent : modèles Prisma `Social*` → tables `social_*` ; champs longs en `@db.Text` ; JWT `{id, email, roles[]}` ; uploads `uploads/users/{userId}.ext` et `uploads/social/{postId}.ext` ; dates en timeago ; erreurs via Toast PrimeNG ; suppressions via ConfirmDialog ; post-cards en cartes ; `emoji-picker-element` ; zoom + intervalle de polling en localStorage ; version via `/api/config` + polling 60 s.

**Pour l'agent** : ce CLAUDE.md est un bon socle de conventions mais **il ment par omission** (rien sur Sentinel, monitoring, reporting, `cli.ts`, `excel-export.ts`). Le compléter, pas s'y fier seul.

---

## 8. Points d'accroche pour un savoir type MASTAURIGE

### 8.1 Avatars / personas / camps

- **Le modèle est déjà là** : `User` porte 14 champs de persona (`base.prisma:24-36`) + `aime`/`deteste`. Le savoir MASTAURIGE (cohérence d'une légende, sociotypes, densité par camp) se branche sur `GET /api/admin/users/field-values` (vocabulaire contrôlé existant) et sur `apps/api/src/excel-export.ts` (feuille `_data` = **taxonomie de référence**). Enrichir cette feuille = enrichir les listes déroulantes de l'animateur, sans toucher au code.
- **Camps** : `Group` est nu (`name` + `color`). Un `type` de groupe (camp / affiliation / sociotype / OSINT), une hiérarchie, ou une convention de nommage MASTAURIGE se poseraient là (`base.prisma:69-77`). MASSTALK envoie déjà `groupes: [{name, type}]` (`toolbox.ts:469`) mais **le `type` est jeté** (`toolbox.ts:561` ne garde que `.name`) → accroche immédiate.
- **Génération** : `apps/admin/src/app/pages/groups-users/groups-users.ts:1034+` fait du bulk-generate avec `@faker-js/faker/locale/fr`. Un générateur de persona MASTAURIGE (cohérent camp/âge/origine/langage) remplacerait ce faker.

### 8.2 Matrices d'injects LO / calendriers D+

- `ScenarioItem` = ligne de matrice d'injects. Il **manque** les colonnes classiques d'une matrice LO : objectif/effet visé, thème/narratif, LO, cible/audience, indicateur de succès, responsable. Colonnes à ajouter dans `base.prisma:106-131` + `formatItem()` (`admin/scenario-items.ts:10-36`) + import/export XLSX (`scenario-edit.ts`).
- **Calendrier D+** : la timeline `apps/admin/src/app/components/timeline/timeline.ts` gère déjà zoom px/min, lignes de grille heure **et jour**, filtre par `#id`/`@user`. Ajouter un axe explicite « J+n / H+n » et des jalons d'exercice (phases, MSEL) se fait là.
- **`POST .../items/auto-organize`** (`scenario-items.ts:246`) répartit aujourd'hui **au hasard** (jitter 50-150 %). Point d'entrée idéal pour une répartition **doctrinale** (courbes d'intensité par phase, pics sur événements, tempo différencié par camp).

### 8.3 Vérificateurs de cohérence

- **Point d'accroche n°1** : `POST /api/admin/scenarios/:id/items/validate` (`scenario-items.ts:334-365`). Ne vérifie que 3 choses (compte existant, pas d'auto-référence, parent présent). Y greffer les contrôles MASTAURIGE : cohérence émetteur↔camp↔narratif, langage/registre vs persona, plausibilité chronologique, collision de hashtags entre camps, densité d'injects par tranche horaire, médias manquants, longueur > `SOCIAL_POST_MAX_LENGTH`, mentions vers comptes inexistants (`src/social/content-parser.ts` extrait déjà `#tags` et `@mentions`).
- **N°2** : `scenario.errors` (JSON) + `SystemLog` indexé par `scenarioId`/`functionalId` = infrastructure de restitution des anomalies déjà en place — la page `apps/admin/src/app/pages/monitoring/monitoring.ts` les affiche.
- **N°3** : `toolbox.ts --reconcile` (`toolbox.ts:478`) est **déjà un vérificateur de cohérence MASSTALK↔Mastorion** interactif. L'étendre (nouveaux sous-modes, mode non-interactif/rapport) est le chemin le plus court.

### 8.4 Baking d'articles / contenus

- Rien pour les faux articles de presse : `SocialPost` n'a qu'un `linkPreview{Url,Title,Desc,Image,Domain}` **rempli par scraping Open Graph d'une vraie URL** (`apps/api/src/social/link-preview.ts`). Or `createSocialPost` est appelé avec `fetchLinkPreview: false` par le scheduler (`scheduler.ts:206`) → **les injects n'ont aujourd'hui aucune preview**.
- **Accroche naturelle** : permettre de *forger* les 5 champs `linkPreview*` depuis l'inject (colonnes XLSX + champs `ScenarioItem`) → « faux article » crédible sans hébergement externe. Étape suivante : générateur d'articles statiques (à la MASTAURIGE, chartes BC1/TV4/OTAN) dont l'URL alimente ces champs.
- Médias : `POST .../items/:itemId/media` + `socialUpload` (`src/upload.ts`) existent ; un pipeline de baking (génération d'images/vignettes) s'y brancherait.

### 8.5 Doctrine d'analyse (Sentinel) — l'accroche la plus riche

- **`sentinel_analysis_grids` / `poles`** (`apps/sentinel-worker/src/db.py:113-133`, `apps/sentinel-api/src/grids/grids.routes.ts`) : une grille = une liste de pôles textuels, embeddés, contre lesquels chaque topic est positionné. **Réceptacle exact d'une matrice de narratifs/LO MASTAURIGE** : encoder les LO et narratifs comme pôles, la plateforme classe automatiquement ce qui émerge.
- **Le prompt de qualification** (`apps/sentinel-worker/src/qualifier.py:7-27`) contient déjà la doctrine en dur (« exercice militaire d'influence red team vs blue team », `relevance` 0-10). Le savoir EXPERT_INFLUENCE s'y injecte directement (typologie de tons, taxonomie d'entités, catégories de narratifs).
- **Rapports de force** (`apps/sentinel-worker/src/relations.py`, page `apps/sentinel-ui/src/app/pages/forces/forces.ts`) : trois signaux non fusionnés — entités communes, séparation des auteurs, anti-corrélation temporelle. Croiser `author_overlap` avec les **`Group` Mastorion** donnerait une mesure de « fuite » entre camps, absente aujourd'hui (le worker ne lit ni `groups` ni `user_groups`, cf. `ingestion.py`).

### 8.6 Autres manques exploitables

| Manque | Où l'ajouter |
|---|---|
| Entité **Exercice** au-dessus des scénarios (phases, D-day, MSEL) | `base.prisma:91` |
| Rôle explicite joueur/entraîné/observateur | `UserRole` (`base.prisma:58`) + `requireRole` (`auth.ts:77`) |
| Threads > 1 niveau | `SocialComment` (`social.prisma:60`) |
| Temps réel | aucun WS/SSE — tout est polling ; `apps/api/src/index.ts` est le point d'insertion |
| Webhook sortant vers Sentinel (prévu par `docs/sentinel-spec.md:68,177`) | jamais implémenté — le worker fait du pull SQL |
| Re-qualification à la demande d'un topic | `apps/sentinel-ui/.../settings.ts:157` (seul TODO du repo) |
| Portage de **Margaret** (assistant IA de veille) en Angular | `vanilla-cockpit/res/app.js:2455-2530` → `apps/cockpit/` |

---

### Fichiers à lire en priorité pour travailler sur la plateforme

`CLAUDE.md` · `README.md` · `docs/cockpit-spec.md` · `docs/sentinel-spec.md` · `docs/deploiement.md` · `apps/api/prisma/schema/base.prisma` · `apps/api/prisma/schema/social.prisma` · `apps/api/src/index.ts` · `apps/api/src/scheduler.ts` · `apps/api/src/auth.ts` · `apps/api/src/admin/scenario-items.ts` · `apps/api/src/admin/users.ts` · `apps/api/src/cockpit/index.ts` · `apps/api/src/social/post-service.ts` · `apps/api/src/excel-export.ts` · `apps/api/src/toolbox.ts` (§ reconcile) · `apps/sentinel-worker/src/{db,config,qualifier,relations}.py` · `apps/sentinel-api/src/grids/grids.routes.ts` · `apps/admin/src/app/components/timeline/timeline.ts` · `entrypoint.sh` · `deploy/2-setup-server.sh`.
