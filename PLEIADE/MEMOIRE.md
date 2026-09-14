# MÉMOIRE — PLEIADE (système global d'exercice)

> **Source de vérité durable de l'agent PLEIADE.** Créée le **2026-09-11**.
> ⭐ **RÉFLEXE NON NÉGOCIABLE : CONSULTER cette mémoire AVANT toute intervention · y CONSIGNER APRÈS chaque avancée**, sans attendre de rappel utilisateur.
> CR daté → `PLEIADE\JOURNAL.md` · règle / capacité durable → **ce fichier**.

---

## 1. Ce qu'est PLEIADE — en une phrase

**PLEIADE est l'écosystème logiciel complet d'entraînement du CECPC** : un **orchestrateur de zones d'exercice** qui déploie, dans des espaces isolés, des instances d'applications (réseau social, gestion d'avatars, sites web…) avec une **authentification centralisée Keycloak**.

⚠ **Changement de nom majeur (2026-09-11)** : le programme s'appelait **MASTORION**. Désormais :
- **PLEIADE** = le **système global** (la plateforme, l'orchestrateur, l'ensemble).
- **MASTORION** = **seulement le réseau social**, une app parmi d'autres du catalogue — **son nom changera à terme** (à surveiller, ne pas le figer dans les productions).

---

## 2. Organisation GitHub — `cecpc-pleiade`

| Dépôt | Rôle | Stack | Cloné en local ? |
|---|---|---|---|
| **`pleiade-platform`** | **Orchestrateur** — zones, instances, catalogue, builds, Keycloak | Node.js 22 + Express + TypeScript | ✅ `D:\CECPC\PLEIADE\pleiade-platform` |
| **`mastorion`** | **Réseau social** d'exercice (+ admin, cockpit, sentinel) | Node 22 + Express 5 + Angular 21 + PrimeNG + Prisma 7 | ✅ `D:\CECPC\PLEIADE\mastorion` |
| **`eho`** | **Gestion avatars / utilisateurs** (Environnement Humain d'Opération) | **Next.js 16** + next-auth v5 + Keycloak + Prisma 7 | ✅ `D:\CECPC\PLEIADE\eho` |
| **`pleiade-infra`** | Infra serveur : Traefik, PKI, monitoring, VPN | Docker Compose | ❌ **non cloné** sur ce poste |

> ⚠ **Ancienne organisation** : le dépôt mastorion vivait sous `github.com/XTalandier/mastorion-v0`. Il est désormais sous **`github.com/cecpc-pleiade/mastorion`**. Les anciens clones (`D:\CECPC\MASTORION\mastorion-v0`, `C:\CECPC\MASTORION\mastorion-v0`) pointent encore sur l'ancien remote — **travailler désormais dans `D:\CECPC\PLEIADE\`**.

Chaque dépôt possède **son propre `CLAUDE.md`** : le respecter quand on travaille dedans. Le `CLAUDE.md` de MINERVE reste la source de vérité côté MINERVE.

---

## 3. Architecture serveur (production)

```
Serveur    : 192.168.10.10 — Ubuntu 24.04, Podman 5 (ROOTFUL → toujours `sudo`)
SSH        : port 2222, user `administrator` (sudo sans mot de passe)
VPN        : Pritunl sur TCP 443 — IP publique 77.129.180.156
Interface  : 10.9.0.1

Client VPN ──> 10.9.0.1:443 ──> Traefik ──> conteneurs
```

### Services exposés via Traefik (HTTPS, `*.mastorion.internal`)
| URL | Service |
|---|---|
| `pleiade.mastorion.internal` | Dashboard orchestrateur |
| `auth.mastorion.internal` | Keycloak (admin/admin) |
| `{instance}.{zone}.mastorion.internal` | Instances d'applications |
| `traefik.mastorion.internal` | Dashboard Traefik |
| `metrics.cecpc.mastorion.internal` | Grafana |
| `vpn.cecpc.mastorion.internal` | Console Pritunl |

### Chemins sur le serveur
`~/mastorion/pleiade/` (orchestrateur) · `~/mastorion/mastorion-v0/` · `~/mastorion/infra/` · `~/mastorion/pleiade/data/zones/` (instances déployées)

⚠ **PKI** : certificat wildcard `*.mastorion.internal` + `*.cecpc.mastorion.internal` géré dans `pleiade-infra`. Les clients VPN doivent installer `pki/ca.crt`.

---

## 4. Les 2 concepts fondateurs

### Zone = un espace isolé pour UN exercice
- **slug** (clé immuable, auto-générée du nom : NFD, sans diacritiques, minuscules, 32 car. max)
- **label** (nom d'affichage libre) · **type** (dev/prod) · **version d'image**
- **1 realm Keycloak** portant le nom du slug, créé automatiquement

### Instance = un déploiement d'une app DANS une zone
Chaque instance reçoit automatiquement :
- un `docker-compose.yml` **généré** depuis le template du catalogue
- un `.env` avec les variables injectées (DB, Keycloak…)
- un **client Keycloak** (public ou confidential selon l'app)
- une **route Traefik** : `{instanceId}.{zoneName}.mastorion.internal`

### Conventions de nommage (à respecter scrupuleusement)
| Objet | Forme |
|---|---|
| ID d'instance | minuscules alphanum + tirets, 2–32 car. |
| Nom de base | `mast_{zone}_{instance}` (64 car. max) |
| Projet Docker Compose | `zone-{zone}-{instance}` |
| Conteneur d'instance | `zone-{zone}-{instance}-app-1` |

---

## 5. Keycloak — l'authentification centralisée

- **1 realm par zone**, créé à la création de la zone.
- **Clients créés à l'ajout d'instances**, redirect URIs = URL de l'instance. Si le client existe déjà (2ᵉ instance mastorion), **les redirect URIs sont fusionnées**.
- **2 URLs distinctes, ne pas les confondre** : `KEYCLOAK_URL` (interne Docker, pour le backend) · `KEYCLOAK_PUBLIC_URL` (pour le navigateur).
- Type de client → ce qui est injecté :
  - **public** (frontend mastorion) : pas de secret ;
  - **confidential** (eho, wordpress) : secret + credentials admin KC.
- **Rôles de client Keycloak → rôles applicatifs** : mastorion mappe désormais les rôles de client KC sur ses propres rôles (commit `bd5d659`) ; l'orchestrateur offre une **matrice groupes × rôles** (commit `bab28a5`).

---

## 6. Catalogue d'applications déployables

`pleiade-platform/catalog/*.yml` — **4 apps** : `mastorion.yml`, `eho.yml`, `wordpress.yml`, `webserver.yml`.

Un template déclare : `image`, `port`, `healthcheck`, `icon` · `keycloak` (clientId + clientType) · `requires` (DB + mapping d'env) · `env` (variables typées : select, couleur, nombre, `secret`, `editable`, défauts avec substitution `{instance}` / `{domain}` / `{auto}`) · `volumes`.

> **Ajouter une app au catalogue = déposer un YAML** — c'est une opération de contenu, pas de code.

### ⭐ Liaison inter-instances (cross-instance linking)
Quand **eho et mastorion coexistent dans une zone**, `EHO_URL` est **automatiquement injecté** dans le `.env` de mastorion. Mastorion s'en sert pour **résoudre un compte par username auprès de l'EHO** quand il ne le trouve pas chez lui (`apps/api/src/admin/scenario-items.ts` → `GET {EHO_URL}/api/users?search=…`). **L'EHO devient donc la source d'identité des personas, mastorion le consommateur.**

---

## 7. État des trois applications (au 2026-09-11)

### 7.1 `pleiade-platform` — l'orchestrateur
`src/` : `index.ts` (Express, routes API, portail dynamique) · `config.ts` · `db.ts` (pool MySQL + migrations) · `catalog.ts` (chargement YAML) · `zone-manager.ts` (CRUD zones/instances, compose, .env) · `keycloak-manager.ts` (API Admin KC).
Dev local : `docker compose -f docker-compose.platform.yml up -d` puis `npm run dev` → **http://localhost:4204**.
Acquis récents : design system Pléiade + thème de login Keycloak · **import/export Excel des utilisateurs**, mot de passe auto, gestion des groupes · variables d'env typées · rôles de client KC + matrice groupes×rôles · app `webserver` au catalogue.

### 7.2 `mastorion` — le réseau social
8 apps dans le turborepo : `api` · `web` · `admin` · `cockpit` · `docs` · `sentinel-api` · `sentinel-ui` · `sentinel-worker`.
Acquis récents : **Keycloak câblé au démarrage** (web + admin), `KEYCLOAK_PUBLIC_URL` pour le frontend, **rôles de client KC → rôles Mastorion**, **layouts sociaux configurables** (mastodon / twitter / facebook / instagram), **impersonation imposée pour toute interaction + journal d'audit**, **fallback EHO** pour résoudre les comptes de scénario.
Détail exhaustif de la plateforme : `MASTORION\MEMOIRE.md` (agent dédié) et le `CLAUDE.md` du dépôt.

### 7.3 `eho` — gestion des avatars (⚠ RÉÉCRIT)
**Next.js 16** (App Router) + **next-auth v5 beta** + Keycloak + Prisma 7 / MariaDB. 3 commits seulement — **stade précoce**.
- Écrans : `(admin)` → `dashboard`, `users`, `users/[id]`, `groups`, `import` · `(player)` → `avatars` · `login`.
- API : `/api/users`, `/api/groups`, `/api/groups/[id]/members`, `/api/import`, `/api/activity`, `/api/auth/[...nextauth]`.
- `src/lib/` : `auth.ts`, `api-auth.ts`, `db.ts`, `keycloak-admin.ts`.
- **Modèle de données** : `User.id = UUID Keycloak (String)` — l'identité vient de Keycloak, plus d'auto-incrément. Groupes avec `keycloakId`. Table `activity_logs` (traçabilité).
- ⭐ **Les champs de persona sont EXACTEMENT ceux de MASTORION** : `age, genre, pays, label, origine, religion, situation, caractere, langage, activite, observations, qualifications, aime, deteste` (+ `bio`, `avatarUrl`, `bannerUrl`, `rawPassword`, `enabled`). **Les bibliothèques MINERVE restent donc directement exploitables.**
- Import : dépendance **`csv-parse`** → format **CSV**, pas XLSX (l'export Excel vit côté orchestrateur).

---

## 8. ⚠ Ce qu'il faut savoir sur notre travail EHO antérieur (Angular)

Entre le 2026-09-09 et le 2026-09-10, une app EHO complète a été développée **en Angular, DANS le monorepo mastorion** (`apps/eho`, port 4204), sur la branche **`feat/eho`** — 8 commits, de `b2e91ec` à `89ad382`.

**Cette branche existe toujours sur `origin/feat/eho`** (vérifié le 2026-09-11) mais **n'a jamais été fusionnée dans `main`**, et `main` a divergé profondément (Keycloak, layouts, impersonation…). **L'EHO a été réécrit ailleurs, en Next.js, comme dépôt autonome.**

Fonctionnalités développées côté Angular et **ABSENTES du nouvel EHO Next.js** (à re-proposer si l'utilisateur les veut) :
- **Modèles d'EHO** (SKOLKAN PERSONA / VIERGE) avec application verrouillée + sauvegarde automatique ;
- **Cellules joueurs** (`eho_teams`, `eho_team_members`) et **fiches d'analyse** (`eho_assessments`) ;
- **Package STARTEX** — autorités countrybook pré-placées et verrouillées chez les joueurs ;
- **Trombinoscope** par pays/fonction avec hiérarchie et palettes des planches MASTAURIGE ;
- **Vue comparative animateur** (officiel vs cellule, écarts, personas mal lus) ;
- glisser-déposer des cartes, import/export Excel, garde anti-fusion à l'import.

> 🧠 **Tout le savoir de conception reste valable** (spécifications, pièges, invariants d'étanchéité) : voir `MASTORION\MEMOIRE.md` § App EHO et `MASTORION\JOURNAL.md` des 09 et 10 septembre. **C'est un capital réutilisable pour le nouvel EHO**, pas du travail perdu.

---

## 8bis. ⭐ L'EHO de PLEIADE — état durable (branche `MEYTRE`)

> Chantier en cours, **branche `MEYTRE` du dépôt `cecpc-pleiade/eho`**, partie de
> `feat/avatars-sans-keycloak`. C'est LÀ que vit l'EHO désormais — plus dans mastorion.

### Ce qui est en place
| Brique | Où | État |
|---|---|---|
| Avatars affranchis de Keycloak | `feat/avatars-sans-keycloak` | ✅ (un avatar n'est plus un compte KC) |
| **Trombinoscope** (thèmes pays, rangs, regroupement) | `src/lib/trombinoscope.ts` + `(admin)/trombinoscope` | ✅ porté depuis l'EHO Angular |
| **Modèles d'EHO** (catalogue, capture, application verrouillée, sauvegardes restaurables) | `src/lib/eho-templates.ts` + `(admin)/modeles` | ✅ |
| **Package STARTEX** | `src/lib/eho-joueur.ts` + `/api/eho/startex` | ✅ (2026-09-11) |
| **Planche joueur** (rangement) | `(player)/mon-eho` + `/api/eho/mon-eho` | ✅ (2026-09-11) |
| **Comparaison animateur** | `(admin)/comparaison` + `/api/eho/comparaison` | ✅ (2026-09-11) |
| Cellules / équipes | — | ❌ **écarté volontairement** (décision utilisateur) : un joueur = un compte Keycloak |

### Les 3 règles du jeu — appliquées CÔTÉ SERVEUR, jamais par masquage d'UI
1. **Dépouillement** : `/api/eho/mon-eho` ne transmet que nom, handle, portrait. Pays, camp, fonction et bio officiels **ne sortent QUE pour les avatars STARTEX** (`composerCarte`).
2. **Verrou STARTEX** : sur un avatar du package, `PUT /api/eho/mon-eho/[id]` **ignore** zone/camp/fonction et ne retient que la note. Entrer au package **purge** les rangements déjà posés (les notes sont conservées).
3. **Validation** : toute zone ou tout camp hors liste est refusé (400) — un appel forgé ne peut pas semer de valeurs qui fausseraient la comparaison.

### Choix de conception à connaître
- **STARTEX = un GROUPE nommé `STARTEX`** → aucun ajout au schéma, et **le package voyage dans les classeurs Excel, les exports et les modèles d'EHO** (vérifié : les 62 autorités arrivent par l'import).
- **Un seul modèle Prisma ajouté** : `EhoLecture` (`eho_lectures`) — la lecture d'UN joueur (`playerId` = `sub` Keycloak, **sans clé étrangère** : le joueur est un compte du realm, pas un avatar) sur UN avatar. Séparée de `users` par construction, pour que l'animateur puisse comparer.
- **L'écart de zone se calcule sur la ZONE ATTENDUE, pas sur le pays brut** : un avatar sans pays (ONU, CICR) est attendu en « Autre / International » — sinon un rangement juste compterait pour faux (`zoneAttendue()`).
- **Un STARTEX n'est jamais en écart**, mais reste affiché en comparaison dès qu'il porte une note.

### Données en place (à jour 2026-09-14)
**453 avatars** = 451 de la bibliothèque MINERVE (après retrait du doublon Gavrilov) **+ Patrick HETTA et Kimberley** (créés depuis le diagramme RENS DELATTRE 26). **58 groupes · 1 643 appartenances · 118 portraits · STARTEX = 62.**
Au 2026-09-14 s'y ajoutent les tables de jeu : **`eho_lectures`** (lectures des joueurs, dont le curseur) et **`eho_dispositions`** (rangement personnel : rubriques + ordre).
⚠ Les **20 avatars de démonstration** livrés avec le nouvel EHO (noms génériques français, groupes « Population civile », « Journalistes »…) ont été **supprimés** — ils n'étaient pas à nous.
**Modèles disponibles** : `SKOLKAN` (453 avatars / 58 groupes, STARTEX inclus) et `VIERGE`.

### Environnement de travail
- ⚠⚠ **D: est en exFAT → AUCUN binaire natif ne s'y exécute** : `next build` et `prisma db push` échouent en **EPERM**. D'où un **clone d'exécution `C:\CECPC\PLEIADE\eho`** (NTFS) — npm, Prisma et le serveur de dev y tournent (**port 3001**). Le dépôt `D:\CECPC\PLEIADE\eho` reste la copie de référence ; **GitHub fait foi**, les deux clones s'y synchronisent.
- Pile locale (conteneurs) : `eho-eho-db-1` (MariaDB, port **3307**), `eho-keycloak-1` (**8180**, realm `cecpc`, admin/admin sur le realm *master*), `eho-keycloak-db-1`.
- **Comptes de test créés dans le realm `cecpc`** : `joueur_test` / `test123` (aucun rôle → vue joueur) · `anim_test` / `test123` (rôle `admin` → trombinoscope, STARTEX, comparaison). `thomas` = compte utilisateur (rôles `admin` + `cockpit`).
- Pour obtenir un jeton en script : flux mot de passe sur le client `eho` (secret lu via l'API admin KC). ⚠ Keycloak 26 exige un **profil complet** (prénom, nom, email vérifié) et le rôle `default-roles-cecpc`, sinon « Account is not fully set up ».

### Acquis du 2026-09-14 — ce que l'EHO sait faire de plus

| Capacité | Où | Règle à retenir |
|---|---|---|
| **Cloisonnement des rôles** | `lib/roles.ts` · `(admin)/layout.tsx` | La section animation est **refusée côté serveur** (anonyme → `/login`, sans rôle → `/mon-eho`). Masquer une entrée de menu ne protège rien. |
| **Écran de sélection STARTEX** | `(admin)/trombinoscope` | Rien n'est écrit avant « Appliquer » ; un retrait massif demande confirmation ; l'état est **relu** avant et après. |
| **Curseur d'alignement** | `lib/camp.ts` · `camp_curseur` | ⭐ Le curseur (−100 bleu → +100 rouge) est la **valeur de référence** ; `campEstime` en est **déduit côté serveur**. |
| **Rangement personnel du joueur** | `eho_dispositions` · `lib/zones-planche.ts` | Ordre libre + **rubriques créées par le joueur** dans chaque pays. Purement **affichage** : n'entre dans aucun calcul d'écart. |
| **Mise en forme des bios** | `lib/bio.ts` | Reconnaît les fiches structurées de countrybook et le Markdown. **Aucun mot n'est modifié** — seulement la mise en forme. |
| **Fiches unifiées** | `components/fiche.tsx` | Une seule coquille pour les **trois** fiches de l'application. |
| **Filtrage des animateurs** | `lib/keycloak-admin.ts` | Les planches des porteurs du rôle admin sont exclues des écrans « joueurs » et des statistiques. Échec Keycloak → filtre désactivé, jamais d'écran vide. |

#### ⭐ Règles de conception nées de cette séance

1. **Un échec de lecture ne doit JAMAIS être présenté comme un résultat valide.** Deux incidents de la même famille le même jour : un 401 traité comme « package vide » a fait disparaître les 62 étoiles ; des rôles vidés après un jeton non rafraîchi ont fait passer un animateur pour un joueur, **menu à l'appui**. Lever, afficher, désactiver l'action — mais ne pas rendre « vide » ou « sans rôle » ce qu'on n'a pas pu lire.
2. **Une action destructive se calcule sur l'état RELU du serveur**, jamais sur une copie locale qui a pu vieillir (session expirée, rechargement à chaud, autre animateur).
3. **Deux champs qui disent la même chose finissent par se contredire.** D'où : le camp est *déduit* du curseur, jamais saisi en parallèle ; les zones de la planche sont déclarées une seule fois ; les trois fiches partagent une coquille ; le formulaire de création est unique.
4. **Une règle métier doit valoir sur TOUS les chemins.** La purge des estimations à l'entrée au STARTEX manquait sur la case à cocher de la fiche d'avatar — exactement le symptôme « Lena Peters mal placée ». Elle est désormais écrite une fois (`purgerEstimations`).
5. **Stocker au bon grain** : le rangement d'un joueur tient en **une ligne JSON** par joueur, avec des listes **partielles**. Une colonne par carte aurait écrit 391 lignes pour remonter un avatar d'un cran.
6. **Un écran filtré n'enregistre pas ce qu'il affiche** : l'ordre est calculé sur la zone complète, sinon une recherche en cours amputerait le rangement des cartes masquées.

#### Vocabulaire d'interface (à respecter)

- Dans l'EHO, il n'y a **que des avatars** — plus aucune occurrence du mot « utilisateur » dans les écrans d'animation (« utilisateur » désigne un compte humain, et ceux-là vivent dans Keycloak / MASTORION).
- **Une seule entrée « Avatars »**, deux vues : **Planche** (le trombinoscope, vue par défaut) et **Liste** (le registre : email, statut, création, suppression).
- Côté animateur, « **EHO joueurs** » = la planche d'un joueur telle qu'il l'a rangée ; « **Comparatif** » = le même travail champ par champ face à l'officiel. L'animateur n'a **pas** de planche personnelle : son EHO, c'est le trombinoscope.
- La **planche joueur est la référence esthétique** : bandeau de zone plein + liseré d'accent + panneau attaché, sous-blocs titrés par un filet de couleur. Le trombinoscope s'y est aligné le 2026-09-14.

#### ⚠ Pièges d'environnement (vérifiés deux fois chacun)

- **Après `prisma generate`, REDÉMARRER le serveur de dev** : il conserve l'ancien client en mémoire et les écritures échouent en **500**.
- **Contrôler le code HTTP** dans tout script d'essai : un script qui parse la réponse sans regarder le statut avale les 500 et fait croire que tout fonctionne.
- Les **sessions expirent** : un 401 en cours d'essai n'est pas un bug de l'application (et se voit désormais à la pastille de la barre).
- Le **modèle SKOLKAN n'est pas un fichier Excel** mais un instantané JSON (`data/eho/templates/skolkan/`) capturé depuis la base : il conserve les **identifiants**, ce que le classeur ne fait pas.
- **Aller-retour Excel prouvé** (2026-09-14) : export → modification → ré-export → réimport = `created 0, updated 453, refused 0`, groupes, appartenances, STARTEX, portraits et lectures intacts. Appariement **par `username` uniquement**.


### ⚠⚠ Faille de sécurité connue, NON corrigée (arbitrage utilisateur en attente)
**10 routes API n'ont aucun contrôle d'autorisation** : `/api/users`, `/api/users/[id]`, `/api/groups*`, `/api/import`, `/api/uploads*`, `/api/activity`, `/api/avatars/export`.
**Démontré** : sans aucune authentification, `GET /api/users` renvoie les 453 avatars avec `pays`, `label`, `activite`, `observations` → **cela annule le dépouillement de la planche joueur**.
⚠ **Le cas le plus exposé** : `GET /api/avatars/export` télécharge **toute la bibliothèque en classeur Excel, sans session** (vérifié le 2026-09-14).
⚠ Tension produit : la page `(player)/avatars` (choix d'avatar) consomme `/api/users` et a besoin des identifiants — la fermer telle quelle la casserait. **Piste recommandée** : charge utile réduite pour les non-admins sur `/api/users`, + `exigerAdmin` sur import/export/activity/uploads.

### 🔴 Leçon durement apprise (2026-09-11)
**Ne JAMAIS déduire un nom de champ d'API par supposition avant une opération destructive.** En cherchant les groupes vides, j'ai testé `_count.users` / `userCount` / `nbAvatars` — aucun n'existe dans la réponse de `/api/groups` → **tous les groupes ont été jugés vides et les 63 ont été supprimés**. Réparé par réimport du classeur (`updated 453`, groupes et appartenances reconstruits), mais la règle vaut pour tout : **lire la réponse réelle d'abord, et vérifier sur UN élément avant de boucler.**

## 9. Règles de travail de l'agent PLEIADE

1. **Périmètre** : PLEIADE = le **système global** (orchestrateur, zones, Keycloak, infra, articulation entre apps). Le détail interne du réseau social reste chez l'agent **MASTORION** ; le contenu d'exercice chez les agents d'exercice (DELATTRE, MINAUTORE, GUILLAUME) ; l'outillage HTML brigade chez **MASTAURIGE**.
2. **Les dépôts sont partagés avec le développeur (Xavier)** : ne jamais committer/pousser sans demande explicite ; vérifier `git status`, branche et remote avant toute intervention.
3. **Sur le serveur, toujours `sudo`** pour Docker/Podman (mode rootful). Ne jamais toucher à la production sans autorisation.
4. **Ne pas figer le nom « MASTORION »** dans les productions durables : le réseau social sera renommé.
5. **CONSULTER avant / CONSIGNER après** — cette mémoire + `JOURNAL.md`.
6. Règles transverses MINERVE applicables aux contenus : camps (registre MASTAURIGE fait foi), GET, numéros fictifs, langue de l'avatar, pas de détail opérationnel réel.

---

## 10. Points ouverts / à trancher avec l'utilisateur

- ✅ **Sort du travail EHO Angular — TRANCHÉ (2026-09-11)** : porté vers le nouvel EHO (trombinoscope, modèles, STARTEX, planche joueur, comparaison) ; **les cellules/équipes sont écartées**. La branche `origin/feat/eho` de mastorion n'a plus vocation à être fusionnée.
- ⏳ **Faille d'autorisation des 10 routes API** de l'EHO (cf. § 8bis) — décision attendue sur la charge utile réduite pour les non-admins.
- ⏳ **Modèle DELATTRE 26 à part ?** HETTA et Kimberley sont aujourd'hui DANS le modèle `SKOLKAN` ; l'utilisateur peut vouloir un modèle distinct pour l'exercice.
- ⏳ **Nouveau nom du réseau social** (« MASTORION » est transitoire).
- ⏳ `pleiade-infra` **non cloné** sur ce poste — le cloner si l'on doit travailler l'infra.
- ⏳ Le **package STARTEX**, les **452 personas** et les classeurs MINERVE (`MASTORION\BIBLIOTHEQUES\`) visent le schéma MASTORION ; vérifier leur import dans le **nouvel EHO** (format CSV attendu, `id` = UUID Keycloak).
