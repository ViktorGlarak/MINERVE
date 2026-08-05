# MÉMOIRE — MASTORION (état durable)

> **Convention 2 fichiers** : ce fichier = état durable (règles, connaissance plateforme, capacités, roadmap) — doit rester lisible d'un bloc (< 100 Ko). Historique daté → `JOURNAL.md`.
> Dernière mise à jour : 2026-07-27.

---

## Identité & périmètre

- **MASTORION** = plateforme de réseaux sociaux fictifs **nouvelle génération**, travaillée **en parallèle** de l'outillage MASTAURIGE, destinée principalement aux exercices de niveau **division / corps d'armée**.
- Racine : `D:\CECPC\MASTORION\` · Repo cloné GitHub : `D:\CECPC\MASTORION\mastorion-v0` (possède son propre `CLAUDE.md`).
- Raison d'être de l'agent : **transposer le savoir MINERVE/MASTAURIGE** (avatars-camps, matrices LO/GLM26, calendriers D+ avec GELEX, vérificateurs de cohérence, baking d'articles, chartes médias, doctrine ILI, RETEX) **dans l'amélioration de la plateforme**.

## ⚠ Règles en vigueur

1. **LECTURE SEULE sur `D:\CECPC\MASTORION`** (consigne utilisateur du 2026-07-27) : aucune modification, création de fichier, build ou installation dans ce dossier sans autorisation explicite. Analyses, specs et propositions se consignent ici (côté MINERVE).
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
9. Divers : porter Margaret (assistant IA de veille du vanilla-cockpit) en Angular, threads > 1 niveau, rôle « entraîné » explicite, requalification à la demande (seul TODO du repo).
