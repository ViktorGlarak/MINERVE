# MÉMOIRE — PLEIADE (système global d'exercice)

> **Source de vérité durable de l'agent PLEIADE.** Créée le **2026-09-11**.
> ⭐ **RÉFLEXE NON NÉGOCIABLE : CONSULTER cette mémoire AVANT toute intervention · y CONSIGNER APRÈS chaque avancée**, sans attendre de rappel utilisateur.
> CR daté → `PLEIADE\JOURNAL.md` · règle / capacité durable → **ce fichier**.

---

## 1. Ce qu'est PLEIADE — en une phrase

**PLEIADE est l'écosystème logiciel complet d'entraînement du CECPC** : un **orchestrateur de zones d'exercice** qui déploie, dans des espaces isolés, des instances d'applications (réseau social, gestion d'avatars, sites web…) avec une **authentification centralisée Keycloak**.

⚠ **Changement de nom mené à son terme** — deux étapes, la seconde constatée le **2026-09-16** :
1. *(2026-09-11)* le programme entier s'appelait **MASTORION** → il devient **PLEIADE** (la plateforme, l'orchestrateur, l'ensemble), et « MASTORION » se réduit au **réseau social** seul.
2. ⭐ *(constaté le 2026-09-16)* le réseau social a **lui aussi** été renommé : c'est **`social`**, dépôt **`app-social`**.

👉 **Le mot « MASTORION » ne désigne plus rien de vivant.** Il ne subsiste que comme nom de l'ancêtre du réseau social (dépôt `mastorion`, figé) et comme nom de l'**agent MINERVE** qui en tient l'expertise. **Ne plus l'employer dans les productions durables.**

---

## 2. Organisation GitHub — `cecpc-pleiade`

⭐ **11 dépôts, TOUS clonés dans `C:\CECPC\pleiade\`** *(relevé et complété le 2026-09-16 — les 7 `app-*` manquaient)*. Un dépôt = une brique déployable ; **les 8 apps du catalogue ont chacune le sien**.

### Les deux briques de plateforme
| Dépôt | Rôle | Stack |
|---|---|---|
| **`pleiade-platform`** | **Orchestrateur** — zones, instances, catalogue, builds, Keycloak, `/api/internal` | Node.js 22 + Express + TypeScript |
| **`pleiade-infra`** | Infra serveur : Traefik, PKI, monitoring, VPN | Docker Compose |

### Les 8 apps déployables (1 app du catalogue = 1 dépôt)
| Dépôt | Ce qu'elle fait | Stack | Port dev |
|---|---|---|---|
| ⭐ **`eho`** | **Identités de la zone** — avatars, groupes, EHO de jeu. **Source d'identité de TOUTES les autres apps.** | Next.js 16 + next-auth v5 + Prisma 7 | **3001** |
| **`app-social`** | **Réseau social** (ex-`mastorion`) — Mastodon-like, apparences configurables (mastodon / twitter / facebook / instagram / youtube) | Node 22 + Express 5 + Angular 21 + PrimeNG + Prisma 7 | 3000 / 4200 |
| **`app-admin`** | **Administration centrale de zone** — scénarios **multi-apps** + **scheduler** qui publie | Next.js + Prisma | 3400 |
| **`app-cockpit`** | **Veille multi-réseaux** de la zone — BFF en éventail sur toutes les instances | Next.js 16 (BFF, sans Prisma en phase 1) | 3000 |
| **`app-press`** | **Site de presse** — 1 instance = 1 titre ; site public + rédaction | Next.js + Prisma | 3500 |
| **`app-messagerie`** | **Messagerie** esprit Telegram — canaux, groupes, privés, transferts, envois programmés. ⚠ **Fondations seules : l'interface reste à écrire** | Next.js 16 + Prisma | 3600 |
| **`app-webserver`** | Fichiers statiques + explorateur admin | Node + `server.js` | — |
| **`app-wordpress`** | Image WordPress OIDC (Dockerfile + `mu-plugins`) | Docker | — |

### ⚠⚠ `mastorion` est un ANCÊTRE, plus une brique vivante
**`app-social` contient tout `mastorion` PLUS 19 commits** (même commit initial `b7c6332`, `mastorion` s'arrête à `61d1a5f`). Le renommage annoncé le 2026-09-11 **a eu lieu** — commit « *Devenir social : renommage et mise en production automatique* ».
👉 **Travailler dans `app-social`. Ne plus toucher au clone `mastorion`**, conservé comme repère historique. *(Les très anciens clones `D:\CECPC\MASTORION\mastorion-v0` et `C:\CECPC\MASTORION\mastorion-v0`, organisation `XTalandier`, sont dépassés depuis plus longtemps encore.)*

> 📁 **`C:\CECPC\pleiade\dev\`** — scripts d'environnement local, hors dépôts : `up.ps1` / `down.ps1` (monter et descendre la pile), `bootstrap-keycloak.mjs`, `seed-eho.mjs`, `seed-mastorion-posts.mjs`, `purge-comptes-avatars.mjs`, `README.md`. ⚠ **Non versionnés** — ils n'existent que sur ce poste.

Chaque dépôt possède **son propre `CLAUDE.md` / `README.md`** : le lire et le respecter quand on travaille dedans. Le `CLAUDE.md` de MINERVE reste la source de vérité côté MINERVE.

### 📄 Documents de référence — `PLEIADE/REFERENCES/`

| Document | Ce que c'est |
|---|---|
| **`Pleiade-presentation.pdf`** | ⭐ **La présentation de PLEIADE par Xavier** (draft, 19 pages, 2026-09-14). La vision d'ensemble : zones étanches, catalogue d'applications, scénarios orchestrés, cockpit de veille, réseau fermé sous VPN. **À lire avant toute discussion d'architecture avec Xavier.** |

`REFERENCES/README.md` en donne le sommaire page par page **et les écarts** avec la présente
mémoire. ⚠ C'est un **draft de présentation** : quand il contredit le code des dépôts, **le
code fait foi**.

---

## 2bis. ⭐⭐ Le modèle de branches — `main` on travaille, `prod` on déploie

> ⚠⚠ **RÈGLE DE SÉCURITÉ, pas une convention de confort.** *(Écrit le 2026-09-16 à la demande de l'utilisateur ; jusque-là la doctrine n'existait QUE dans l'en-tête des workflows, dans aucun `.md`.)*

### Les trois étages
| Branche | Ce que c'est | Qui la touche |
|---|---|---|
| **branche provisoire** *(nommée librement)* | Là où l'on **fait** le travail, dans le dépôt concerné | nous, librement |
| **`main`** | La branche **principale d'intégration** — on y **importe** le travail depuis la branche provisoire | sur décision |
| ⚠ **`prod`** | **Ce qui tourne réellement** sur le serveur d'exercice, **devant des participants** | ⚠ **jamais sans décision explicite de l'utilisateur** |

**Branches provisoires réellement observées** (2026-09-16) : `MEYTRE` (la nôtre), `cle-de-service-eho`, `exiger-un-role`, `editeur-et-cle-de-service`, `feat/eho-data-volume`, `fix/keycloak-issuer-public-url`, `infra/traefik-prod-compose`, `durcissement-acces-et-portail`.

### ⭐ Pousser sur `prod` N'EST PAS un enregistrement : c'est LE geste de déploiement
`.github/workflows/deployer-prod.yml` se déclenche sur `push: branches: [prod]`, sur un **runner auto-hébergé sur le serveur d'exercice** (donc ni clé SSH ni secret à stocker) : il construit l'image en rootless, la pousse au registre interne, puis demande à Pléiade de **promouvoir la version sur les zones de production**.

Mot pour mot, l'en-tête du workflow d'`eho` :
> *« Le geste de déploiement, c'est de pousser sur `prod` — jamais sur `main`. `main` est là où l'on travaille ; `prod` est ce qui tourne devant des participants. […] **une app cassée se voit en salle**, pas seulement par nous. »*

- ✅ **Bonne nouvelle** : la promotion **ne touche QUE les instances de l'app concernée** — *« une correction urgente ne doit pas couper les autres apps d'un exercice en cours »*. Un `concurrency` par app empêche deux déploiements simultanés, **sans annuler le premier** (un déploiement interrompu à mi-chemin laisserait la pile dans un état bâtard).

### ⚠ Deux nuances que le modèle général ne dit pas — vérifiées dépôt par dépôt
1. ⚠⚠ **`pleiade-platform` n'a PAS de branche `prod`** : son workflow (`deployer.yml`) se déclenche sur **`main`**. **Pousser sur `main` de l'orchestrateur DÉPLOIE**, immédiatement. *(Le workflow d'`eho` assume l'asymétrie : « le sas se justifie ici bien plus que pour l'orchestrateur ».)* Seul garde-fou : `paths-ignore: '**.md'` — *« un changement de documentation ne justifie pas un redéploiement »*.
2. **Trois dépôts n'ont ni `prod` ni workflow de déploiement** : `pleiade-infra`, `app-webserver`, `app-wordpress`.

| Dépôt | Branche qui déploie |
|---|---|
| `eho` · `app-social` · `app-admin` · `app-cockpit` · `app-press` · `app-messagerie` | **`prod`** |
| ⚠ `pleiade-platform` | **`main`** *(pas de sas !)* |
| `pleiade-infra` · `app-webserver` · `app-wordpress` | aucune (déploiement manuel) |

### Ce que cela m'impose
1. **Travailler sur une branche provisoire**, jamais directement sur `main`.
2. **Ne jamais pousser sur `prod`** — ni sur le `main` de `pleiade-platform` — **sans que l'utilisateur l'ait explicitement demandé pour CE dépôt**. Une autorisation donnée une fois ne vaut pas pour la suivante.
3. **Toujours annoncer l'effet** avant de pousser : « ceci déploiera sur le serveur d'exercice » n'est pas la même phrase que « ceci enregistre le travail ».
4. Ces dépôts sont **partagés avec Xavier** : vérifier `git status`, la branche et le remote avant toute intervention.

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

`pleiade-platform/catalog/*.yml` — **8 apps** (relevé le 2026-09-15) :

⭐ **Chaque entrée du catalogue a SON dépôt** (correspondance 1:1 vérifiée le 2026-09-16) :

| App (YAML) | Dépôt | Ce qu'elle fait | Rôles Keycloak |
|---|---|---|---|
| `social` | **`app-social`** | Réseau social d'exercice — **remplace `mastorion`** | `animateur` (seul ; lecture seule sans lui) |
| `presse` | **`app-press`** | Site de presse — 1 instance = 1 titre | `journaliste` · `redacteurchef` · `directeur` |
| `messagerie` | **`app-messagerie`** | Messagerie instantanée — canaux, groupes, privés, programmés | `admin` · `moderateur` *(outil de JOUEUR : tout compte du royaume entre ; les rôles ne servent qu'à la supervision)* |
| ⭐ `admin` | **`app-admin`** | **Administration de la zone** : scénarios multi-apps, publication orchestrée | Administration · Conduite d'exercice |
| ⭐ `cockpit` | **`app-cockpit`** | **Veille multi-réseaux** de la zone | Veille · Environnement |
| `eho` | **`eho`** | Identités de la zone — **notre chantier**, et **source d'identité de toutes les autres** | Administration · Environnement |
| `wordpress` | **`app-wordpress`** | CMS (OIDC Keycloak pré-configuré) | Administrateur · Éditeur |
| `webserver` | **`app-webserver`** | Fichiers statiques avec explorateur admin | Administration · Environnement |

⚠ **`admin` et `cockpit` sont nouveaux et recoupent directement le savoir MINERVE** — l'un
orchestre des déroulés heure par heure avec import XLSX (cf. MELMIL / synchromatrice), l'autre
fait de la veille et du reporting comparatif. Voir `REFERENCES/README.md`.

Un template déclare : `image`, `port`, `healthcheck`, `icon` · `keycloak` (clientId + clientType) · `requires` (DB + mapping d'env) · `env` (variables typées : select, couleur, nombre, `secret`, `editable`, défauts avec substitution `{instance}` / `{domain}` / `{auto}`) · `volumes`.

> **Ajouter une app au catalogue = déposer un YAML** — c'est une opération de contenu, pas de code.

### ⭐ Liaison inter-instances (cross-instance linking)
Quand **eho et mastorion coexistent dans une zone**, `EHO_URL` est **automatiquement injecté** dans le `.env` de mastorion. Mastorion s'en sert pour **résoudre un compte par username auprès de l'EHO** quand il ne le trouve pas chez lui (`apps/api/src/admin/scenario-items.ts` → `GET {EHO_URL}/api/users?search=…`). **L'EHO devient donc la source d'identité des personas, mastorion le consommateur.**

---

## 6bis. ⭐⭐ Comment les apps d'une zone se parlent — les 4 mécanismes à connaître

*(Établi le 2026-09-16 à la lecture des `README`/`CLAUDE` des 7 dépôts `app-*`. C'est LE modèle à avoir en tête avant toute discussion d'architecture.)*

### 1. L'identité est UNE, et elle vient d'eho
`identity_id` = **UUID eho** = `sub` Keycloak = **le même identifiant sur toutes les apps de la zone**. Un avatar déclaré une fois dans eho agit partout : il signe un article dans `app-press`, poste dans `app-social`, écrit dans `app-messagerie`.
- ⚠ Une app **n'a pas de comptes à elle** : elle ne stocke qu'un `identityId`. `app-press` compose sa rédaction en **cochant des groupes eho** — un avatar ajouté au groupe « Journalistes » devient signataire sans ressaisie.
- ⚠ Un persona reçoit un `user.id` **différent dans chaque instance** de `app-social`. C'est `identity_id` qui fait le pont, et `/accounts/lookup?identity=` qui le résout. **Sans lui, aucune vue transverse n'est possible** — c'est la clé du cockpit.
- 👉 **Conséquence pour nous : notre chantier eho est la pierre angulaire de la zone**, pas une app parmi d'autres.

### 2. La découverte se fait à l'EXÉCUTION, jamais en dur
Aucune app ne connaît ses voisines par configuration. Chacune interroge l'orchestrateur :
`GET {PLEIADE_URL}/api/internal/zones/{PLEIADE_ZONE}/instances` avec `PLEIADE_API_KEY` → `{id, label, appType, url, publicUrl}`.
- Rafraîchi ~30 s ; **dernière liste conservée si l'orchestrateur est injoignable** (application de « un échec de lecture n'est pas un résultat valide »).
- `url` = adresse interne (nom de conteneur, pour le serveur) · `publicUrl` = pour rendre **absolus les médias**, que les apps renvoient relatifs à *leur* origine.
- 👉 **Une app ajoutée ou retirée d'une zone est vue sans redéploiement.**

### 3. La clé de service `X-API-Key` — parce que personne n'est en ligne
C'est **la clé de la zone**, injectée par Pléiade dans toutes ses apps.
- ⭐ **Pourquoi pas le jeton de l'opérateur** : le scheduler de `app-admin` publie un inject à **T+37 min**, quand plus personne n'est devant l'écran. La session Keycloak de l'opérateur ne sert alors qu'à **signer le journal**.
- **Cloisonnement** : une app compromise ne voit que **sa** zone.

### 4. Le contrat `/api/service/*` est le MÊME partout
`app-social`, `app-press` et `app-messagerie` exposent le même contrat (`health`, `accounts?identity=`, `users?search=`, `groups`, `publish`, `posts/[id]`…).
- 👉 **`app-admin` vise n'importe quelle app sans rien savoir d'elle.** C'est ce qui rend les scénarios multi-apps possibles.
- ⚠ Un item de scénario cible **une INSTANCE (`instanceId`), jamais un type de réseau** : *« s'il y a trois YouTube, ce sont trois cibles »*.
- ⚠ **Un message publié par le scénario doit être strictement indiscernable d'un message tapé par un joueur** : `source = "scenario"` n'apparaît **jamais** côté joueur, seulement en supervision.

### ⭐ Le démantèlement de l'admin embarquée — à connaître pour ne pas chercher au mauvais endroit
L'administration et le cockpit vivaient **dans** mastorion (`apps/admin`, `apps/cockpit`). Ils en ont été **retirés** (commits « Retirer l'administration et le cockpit embarqués », « Retirer la gestion des comptes… ») et répartis :

| Ce qui était dans mastorion | Vit désormais dans |
|---|---|
| Comptes, utilisateurs, groupes | ⭐ **`eho`** |
| Scénarios, publication programmée | **`app-admin`** (multi-apps) |
| Veille, tendances, reporting | **`app-cockpit`** (multi-réseaux) |
| Rôles | **Keycloak**, via Pléiade |

Il ne reste au social **qu'un seul rôle : `animateur`** — et **lecture seule sans lui**.

### Ce que `app-cockpit` a appris (utile au-delà du cockpit)
- **BFF dans le même processus** : le navigateur ne parle qu'au BFF, qui fait l'éventail en serveur-à-serveur. → **pas de CORS**, pas de *web origins* Keycloak à configurer, **un seul jeton** (toutes les instances d'une zone partagent le realm et le client).
- ⚠ **Les ids sont désambiguïsés** : `key = "{instance}:{id}"` — *« le post 42 n'est pas le même d'une base à l'autre »*, d'où aussi un **curseur de polling par réseau**.
- ⚠ **Une instance en panne ne fait jamais échouer les autres** : chaque réponse porte ses `errors` par réseau.
- **Persona = 3ᵉ type de source**, transverse : un `identity_id` résolu sur chaque réseau, non-lus cumulés.

### Le design system Pléiade (toutes les apps)
Graphite + **craie comme seule couleur de marque**, angles vifs, **Archivo + JetBrains Mono**, aucune ombre ni *scale*, mention « **Exercice · non classifié** » sur toute surface. Mode clair par **inversion** (la craie devient le support), jetons inchangés sous `html[data-theme="light"]`.
⚠ **`pleiade-theme.css` est une COPIE CONFORME dans chaque app — ne jamais l'éditer sur place**, le recopier quand le thème évolue à la source.

### Conventions de code des apps (relevées dans `app-messagerie`)
- Texte affiché **en français avec accents** ; **commentaires de code en français sans accents**, qui expliquent le **pourquoi**.
- **Jamais** de `prompt` / `confirm` / `alert` du navigateur — un `ConfirmDialog` maison.
- **Deux mondes dans une seule feuille de style** : l'app crédible pour les joueurs, le thème Pléiade pour la supervision.
- Polices **auto-hébergées** (`next/font`) : *« un exercice tourne sur réseau fermé, rien ne sort »*.

---

## 7. État des briques principales

> ⚠ Section écrite le **2026-09-11**, quand le poste ne connaissait que 3 dépôts. **Le paysage a changé** : voir §2 (11 dépôts) et §6bis (comment ils se parlent). Ce qui suit reste vrai pour `pleiade-platform` ; **7.2 est à lire à la lumière du démantèlement** de l'admin embarquée ; **7.3 est largement dépassé** — l'état réel d'eho est au §8.

### 7.1 `pleiade-platform` — l'orchestrateur
`src/` : `index.ts` (Express, routes API, portail dynamique) · `config.ts` · `db.ts` (pool MySQL + migrations) · `catalog.ts` (chargement YAML) · `zone-manager.ts` (CRUD zones/instances, compose, .env) · `keycloak-manager.ts` (API Admin KC).
Dev local : `docker compose -f docker-compose.platform.yml up -d` puis `npm run dev` → **http://localhost:4204**.
Acquis récents : design system Pléiade + thème de login Keycloak · **import/export Excel des utilisateurs**, mot de passe auto, gestion des groupes · variables d'env typées · rôles de client KC + matrice groupes×rôles · app `webserver` au catalogue.

### 7.2 le réseau social — ⚠ désormais `app-social`, et amputé de l'admin et du cockpit
⭐ **Lire `app-social`, pas `mastorion`** (cf. §2). Le turborepo comptait 8 apps : `api` · `web` · `admin` · `cockpit` · `docs` · `sentinel-api` · `sentinel-ui` · `sentinel-worker`. **`admin` et `cockpit` en ont été RETIRÉS** et sont devenus les dépôts `app-admin` et `app-cockpit` ; la gestion des comptes est partie chez `eho` (cf. §6bis). Restent l'API, le front social et la lignée sentinel.
Docs internes du dépôt : `docs/deploiement.md`, `docs/cockpit-spec.md` (746 l.), `docs/sentinel-spec.md` (Orion — embeddings, BERTopic, Ollama).
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
2. **Verrou STARTEX — porte sur l'IDENTITÉ, pas sur l'alignement** *(précisé le 2026-09-16)* : sur un avatar du package, `PUT /api/eho/mon-eho/[id]` **ignore `paysEstime` et `fonctionEstimee`** (faits du countrybook) et ne retient que **la note et le CURSEUR**. Entrer au package **purge** les rangements déjà posés (les notes sont conservées).
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
- ⭐⭐ **UN SEUL emplacement : `C:\CECPC\pleiade\` — il n'y a plus de second clone** *(consolidé le 2026-09-16)*.
  - ⚠⚠ **Pourquoi C: et pas D:** : **D: est formaté en exFAT → AUCUN binaire natif ne s'y exécute** (`npm`, `next build`, `prisma generate`/`db push` échouent en **EPERM**). **C: est en NTFS.** Un dépôt de code sur D: n'est donc qu'une **archive morte** — il ne peut ni se construire, ni se lancer, ni se tester.
  - 🗑️ Le doublon **`D:\CECPC\PLEIADE` a été SUPPRIMÉ** le 2026-09-16 (0,8 Go, figé au 2026-09-11) après vérification : 0 commit non poussé, 0 remise, toutes les branches sur `origin`, aucun `.env` ni dossier `data/` — rien que des artefacts régénérables. **Ne pas le recréer.**
  - ⚠ **Fin de la doctrine « clone d'exécution + copie de référence »** : elle entretenait deux vérités qui divergeaient (le matin même, la `MEYTRE` locale de C: traînait 10 commits en arrière). Désormais : **une seule copie de travail, sur C:, et GitHub fait foi.**
  - ✅ En revanche **`D:\CECPC\PRODUCTION\` reste sur D:** (MINERVE, EXER, BDA, CREATION, DOC REF — 17,9 Go) : ce sont des **documents**, pas du code, exFAT ne les gêne pas.
  - ⚠ Le dossier réel s'écrit en **minuscules** (`C:\CECPC\pleiade`). Windows est insensible à la casse, mais `git` affiche le chemin tel qu'il est.
- Pile locale (conteneurs) : `eho-eho-db-1` (MariaDB, port **3307**), `eho-keycloak-1` (**8180**, realm `cecpc`, admin/admin sur le realm *master*), `eho-keycloak-db-1`.
- **Comptes de test créés dans le realm `cecpc`** : `joueur_test` / `test123` (aucun rôle → vue joueur) · `anim_test` / `test123` (rôle `admin` → trombinoscope, STARTEX, comparaison). `thomas` = compte utilisateur (rôles `admin` + `cockpit`).
- Pour obtenir un jeton en script : flux mot de passe sur le client `eho` (secret lu via l'API admin KC). ⚠ Keycloak 26 exige un **profil complet** (prénom, nom, email vérifié) et le rôle `default-roles-cecpc`, sinon « Account is not fully set up ».

#### ▶️ Relancer l'environnement de dev EHO (procédure)
1. **Conteneurs** : `docker compose -f C:\CECPC\pleiade\eho\docker-compose.yml up -d eho-db keycloak keycloak-db` — en pratique **Docker Desktop les remonte tout seul** au démarrage du poste (`restart: unless-stopped`). ⚠ Ne PAS monter le service `eho` du compose : le serveur de dev tient ce rôle.
2. **Attendre Keycloak** : `curl -o /dev/null -w "%{http_code}" http://localhost:8180/realms/cecpc/.well-known/openid-configuration` doit rendre **200**.
3. **Serveur de dev** (seul emplacement, il n'y a plus de second clone) : `cd C:\CECPC\pleiade\eho && npm run dev -- -p 3001` — ⚠ le `-p 3001` est **obligatoire** (`package.json` ne le porte pas, et `.env` déclare `NEXTAUTH_URL=http://localhost:3001` : sur 3000 la connexion Keycloak casse). Prêt en ~1,5 s → **http://localhost:3001**.
4. **Contrôle en 10 s** : `/login` répond 200, et la base rend `avatars=453 · groupes=58 · appartenances=1643` (`docker exec eho-eho-db-1 mariadb -uroot -peho2026 -N -e "select count(*) from users" eho`).
- ⭐ **Branches (au 2026-09-16, après la fusion ET le réalignement fait par l'utilisateur)** : **`MEYTRE` et `main` sont au MÊME commit `ff1c63a`, au même arbre — zéro divergence dans les deux sens.** `MEYTRE` redevient la **branche de travail** (repartie d'une base commune propre), `main` l'intégration. La copie de travail `C:\CECPC\pleiade\eho` est sur `MEYTRE`, propre et à jour (le doublon D: a été supprimé le 2026-09-16). Point de retour de la fusion : tag `avant-fusion-MEYTRE`. `prod` reste à `e3e2acc` — **c'est la branche de DÉPLOIEMENT, voir §2bis** : y pousser met en production devant les participants, jamais sans décision explicite.
- ⚠ **Après un réalignement de branches fait hors session, vérifier la branche LOCALE de la copie de travail** : `origin/MEYTRE` était à jour mais la `MEYTRE` locale de C: était restée **10 commits en arrière** — commiter là aurait reconstruit une divergence. `git checkout MEYTRE && git merge --ff-only origin/MEYTRE` (arbre identique à `main`, donc aucun fichier ne bouge et le serveur de dev n'est pas perturbé).
- **Filet gardé dans C:** : `stash@{0}` « etat MEYTRE avant bascule sur main (2026-09-16) » — l'état non commité d'avant la bascule, à supprimer quand l'utilisateur le dira.
- ⚠ **Avant toute bascule de branche dans C:, comparer d'abord** (`diff -r` sur `src/`, `prisma/`, `scripts/`, `package.json`) l'arbre vivant avec le commit visé : le travail y vit souvent **non commité**. Puis `git stash push -u` plutôt qu'un `reset --hard` — un filet récupérable, jamais une destruction.
- ⚙️ **Vérifier une fusion / une branche sans toucher au travail en cours** : `git worktree add` dans le répertoire temporaire, puis `tsc` + `eslint` + `npm run test` + `npm run build`. ⚠ **`node_modules` doit être une VRAIE copie** (`robocopy /E /MT:16`, 0,7 Go, ~30 s) : monté en **jonction**, Turbopack plante (`Symlink [project]/node_modules is invalid, it points out of the filesystem root`).
- ⚠ **Le flux Keycloak n'aboutit que sur le port 3001** : le client `eho` n'autorise que cette URL de retour. Démarrer une version d'essai sur un autre port permet de tester l'anonyme (307/401), **pas** le comportement connecté par rôle.
- Conteneur `mastorion-mastorion-1` en **boucle de redémarrage** (sa base `mastorion-mariadb-1` est tombée) — **sans effet sur l'EHO**, à ignorer ou arrêter.

### Acquis du 2026-09-14 — ce que l'EHO sait faire de plus

| Capacité | Où | Règle à retenir |
|---|---|---|
| **Cloisonnement des rôles** | `lib/roles.ts` · `(admin)/layout.tsx` | La section animation est **refusée côté serveur** (anonyme → `/login`, sans rôle → `/mon-eho`). Masquer une entrée de menu ne protège rien. |
| **Écran de sélection STARTEX** | `(admin)/trombinoscope` | Rien n'est écrit avant « Appliquer » ; un retrait massif demande confirmation ; l'état est **relu** avant et après. |
| **Curseur d'alignement** | `lib/camp.ts` · `camp_curseur` | ⭐ Le curseur (−100 bleu → +100 rouge) est la **valeur de référence** ; `campEstime` en est **déduit côté serveur**. ⭐⭐ **Depuis le 2026-09-16 il est ouvert AUSSI sur les STARTEX** — voir la règle ci-dessous. |

#### ⭐⭐ Le curseur pose DEUX questions différentes selon la carte *(2026-09-16)*

C'est la clé pour ne pas défaire ce réglage par mégarde :

| Carte | Question posée | Départ du curseur | Compté en écart ? |
|---|---|---|---|
| Avatar **inconnu** | « **qui est-il ?** » — une identification | « je ne me prononce pas » | **Oui** — juste ou faux face au countrybook |
| Autorité **STARTEX** | « **où en est-il avec nous ?** » — une **attitude** | **la position officielle**, marquée d'un repère noir | **Jamais** (`calculerEcarts` rend `null` sur un STARTEX) |

**Pourquoi** (demande utilisateur du 2026-09-16) : sur une autorité connue, la première question n'a pas lieu d'être — le countrybook y a répondu. Mais son attitude, elle, **bouge avec ce que les joueurs font** sur le terrain et sur les réseaux : *« un maire ménagé se rapproche, un maire humilié bascule »*. Les joueurs doivent pouvoir l'enregistrer.

- ⚠ **Le dépouillement n'est PAS relâché** : `paysEstime` et `fonctionEstimee` restent **ignorés côté serveur** sur un STARTEX. Vérifié par un appel forgé qui tentait de les poser en même temps que le curseur — les deux ont été écartés, seul le curseur a pris.
- ⚠ **Le curseur part de la position officielle, pas de zéro** : sans point de départ visible, il n'y a **pas de dérive à lire**. Le repère noir (motif repris de `JaugeCamp`) montre d'où l'on vient, et le bouton devient « **Revenir à la position officielle** » au lieu de « je ne me prononce pas ».
- **La carte de la planche suit l'alignement observé** dès qu'il existe (`couleurCamp`) : un maire qui bascule doit se voir **sur la planche**, pas seulement au fond de sa fiche. Tant que rien n'a bougé, la couleur est identique à avant.
- **Côté animateur, c'est de la matière d'animation, pas une faute** : la comparaison affiche officiel et observé côte à côte (`officiel.campCurseur` vs `joueur.campCurseur`) avec `ecarts: null`.
- ⚠ **Un seul chemin d'écriture** pour le curseur, commun aux deux cas : la validation ne doit jamais valoir « ici mais pas là ».
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
- **Menu JOUEUR (au 2026-09-16)** : `Mon EHO` · `EHO GT` · `Planche relationnelle`. **Rien d'autre.** ↩️ L'onglet **« Choix d'avatar » a été SUPPRIMÉ** (page `(player)/avatars` effacée) : vestige de l'échafaudage d'origine, il **ne choisissait rien** (aucun `onClick`, aucun enregistrement — reliquat de l'époque « un avatar = un compte Keycloak », close par `0720ab1`) et servait à tout joueur la **bio et les groupes** des 453 avatars, soit **exactement ce que `composerCarte` s'applique à lui cacher**. ⚠ **Ne pas le réintroduire** : un écran qui liste les avatars n'a de sens que côté animation.

#### ⚠ Pièges d'environnement (vérifiés deux fois chacun)

- **Après `prisma generate`, REDÉMARRER le serveur de dev** : il conserve l'ancien client en mémoire et les écritures échouent en **500**.
- **Contrôler le code HTTP** dans tout script d'essai : un script qui parse la réponse sans regarder le statut avale les 500 et fait croire que tout fonctionne.
- ⭐⭐ **Un contrôle SAUTÉ n'est pas un contrôle RÉUSSI** *(règle née du défaut de `test:bio`, 2026-09-16)*. Un test qui n'a pas pu lire ses données doit **sortir en échec** et **nommer la cause**, jamais afficher « TOUT PASSE » sur ce qui reste. Trois exigences :
  1. **Ne pas confondre les causes** — `!reponse?.ok` mélangeait serveur éteint, serveur qui **refuse** (401/403) et serveur qui plante (500), tous annoncés « injoignable ». Les distinguer, et le dire.
  2. ⭐ **Un script d'essai qui éprouve une LOGIQUE lit la base directement** (`PrismaClient` + `PrismaMariaDb`, helper `urlBase()` de `backfill-curseur.mts`), **pas l'API** : la couche HTTP n'est pas le sujet, et la question de l'autorisation disparaît avec elle. Ne passer par l'API que pour éprouver l'API elle-même — et alors, se présenter avec la **clé de service `X-API-Key`** (`PLEIADE_API_KEY`).
  3. **Une base vide est un « incomplet »**, pas un succès : il n'y avait rien à éprouver.
  ⚠ En remontant la cause d'une erreur Prisma, ne pas prendre `e.message.split("\n")[0]` : le message **s'ouvre par une ligne vide**, puis « Invalid `prisma.x.y()` invocation: », puis un extrait de code — la cause réelle vient **après**.
- Les **sessions expirent** : un 401 en cours d'essai n'est pas un bug de l'application (et se voit désormais à la pastille de la barre).
- Le **modèle SKOLKAN n'est pas un fichier Excel** mais un instantané JSON (`data/eho/templates/skolkan/`) capturé depuis la base : il conserve les **identifiants**, ce que le classeur ne fait pas.
- **Aller-retour Excel prouvé** (2026-09-14) : export → modification → ré-export → réimport = `created 0, updated 453, refused 0`, groupes, appartenances, STARTEX, portraits et lectures intacts. Appariement **par `username` uniquement**.

### Acquis du 2026-09-15 — travail collectif et planche relationnelle

| Capacité | Où | Règle à retenir |
|---|---|---|
| **Groupes de travail (GT)** | `lib/keycloak-admin.ts` · `lib/porteur.ts` | ⭐ **Un GT = un sous-groupe du groupe Keycloak `GT`** (`/GT/<nom>`), rien d'autre. Les groupes **ne sont pas dans le jeton** : résolution serveur par l'API d'admin. `groupesDeTravail` renvoie **`null` en cas d'échec, jamais `[]`** → **503**, jamais « pas membre ». |
| **Une planche, deux porteurs** | `components/planche.tsx` | « Mon EHO » et « EHO GT » sont **le même composant**, paramétré par `gt`. Toute route EHO accepte `?gt=` et **revérifie l'appartenance côté serveur**. |
| **Verrou d'édition** | `eho_verrous` | Verrou **par carte et par porteur**, TTL + battement de cœur. Carte déjà ouverte → **on voit qui la tient, on ne peut pas écrire**. Le verrou protège la **fiche**, pas le rangement. |
| **Import GT → personnel** | `/api/eho/importer-gt` | Écrit d'abord une **sauvegarde restaurable** (`eho_sauvegardes`). |
| **Versement personnel → GT** | `/api/eho/verser-gt` (+ `/annuler`) | Trois grains (carte / rubrique / pays), déclenché par une **icône** — le bouton de carte vit **dans la fiche**. Instantané `eho_versements` avant écriture. |
| **⭐ Planche relationnelle** | `(player)/graphe` · `components/graphe.tsx` · `eho_graphes` | **React Flow** (`@xyflow/react`, MIT, 3 dépendances). Une **ligne JSON par porteur**. Assainissement serveur : 600 nœuds, 2 000 liens, coordonnées bornées, `#RRGGBB`, **auto-liens refusés**. |

#### ⭐ Règles de conception nées de cette séance

1. **Verser, c'est deux listes, pas une** : `aVerser` (cartes qui ont une lecture à copier) et `aPlacer` (toutes les cartes demandées). Une carte sans lecture doit quand même être **placée** — sinon elle reste « sans rubrique ».
2. **Un versement porte sa STRUCTURE** (`parRubrique: [{nom, ids}]`). Une liste plate + une rubrique cible **aplatit tout le GT**.
3. **Annuler ne doit jamais détruire le travail d'un autre** : l'annulation **épargne** les cartes modifiées depuis par un tiers ou verrouillées, et ne restaure la disposition **que si rien n'a été épargné**.
4. **Toute action collective doit être réversible** — import comme versement écrivent leur instantané **avant** d'écrire.
5. **Sur la planche relationnelle, une accroche ne doit jamais recouvrir son nœud** : elle capte l'appui et rend le nœud **impossible à déplacer**.
6. **Un texte placé DANS un nœud en change la taille** — et React Flow pose les accroches sur les **bords** de cette boîte. D'où : la pastille porte son nom **hors flux**, et la version nommée est **un vrai rectangle** dont le texte est légitimement l'intérieur.

7. **Une page qui répond 200 à un inconnu est une page ouverte, même vide.** La section **joueur** n'avait aucun garde : `/mon-eho`, `/eho-gt`, `/graphe`, `/avatars` étaient servis à un anonyme (coque et navigation comprises), alors que seules les routes `/api` refusaient. Corrigé le 2026-09-15. **Chaque groupe de routes porte son propre garde** — `(player)` vérifie seulement **être connecté** (il n'y a pas de rôle « joueur », et un animateur doit pouvoir ouvrir ces écrans).
8. **Les accroches sont invisibles au repos** (`components/graphe.tsx` → `Accroches`, + § accroches de `globals.css`). Elles se posent au survol du nœud, et **tout le plan les montre en retrait pendant qu'un lien est tracé**. La **zone de préhension n'est pas le dessin** : boîte de 18 px, pastille de 10 px. ⚠ `useConnection` **toujours avec un sélecteur**, sinon redessin à chaque pixel du tracé.

9. **Une écriture « en bloc » sur une ressource partagée exige un filet.** `eho_graphes` ne garde qu'une ligne par porteur, réécrite entièrement : une fausse manœuvre effaçait le travail de tout un groupe, sans recours. D'où **`eho_graphe_versions`** (`lib/graphe-versions.ts`) — mais **pas un instantané par enregistrement** (la planche s'enregistre chaque seconde de repos) : on retient sur **acte délibéré**, quand **un autre a écrit en dernier**, ou après **3 min**. 20 versions par porteur. Le filet **ne lève jamais** : il ne doit pas empêcher d'enregistrer. Restaurer conserve l'état courant, et **l'écran recharge** — sinon l'enregistrement différé du client réécrit l'ancien plan par-dessus.
10. **Lire avant d'écrire, toujours** — et ne jamais poser un plan d'essai sur un porteur vivant : c'est de là que sont venus les deux écrasements du 2026-09-15.
11. **Transférer sans jamais effacer** : le transfert d'encadré entre planches (`/api/eho/graphe/transferer`) n'ajoute ou ne remplace que l'encadré visé, son contenu et les liens **dont les deux bouts sont dedans** — d'où l'absence de bouton « annuler » : il n'y a rien à restaurer. Les identifiants sont conservés, donc reverser **met à jour** au lieu de dupliquer.

12. ⭐ **Trois porteurs de planche, pas deux** : `joueur`, `gt`, et **`officiel`** (id réservé `"officiel"`, animation seule, vérifié serveur). La planche officielle est la **seule vue non dépouillée** — `composerCarte(..., { officiel })` — et le drapeau est **déduit du porteur**, jamais réclamé par le client.
13. ⭐ **La planche officielle voyage avec le modèle d'EHO** (`Payload.graphe`) : ses nœuds portent des identifiants d'avatars, elle n'a de sens qu'avec eux. ⚠ **Absent ≠ vide** — un modèle sans la clé `graphe` la **laisse en place** ; seul le VIERGE, qui porte une planche vide explicite, l'efface.
14. ⭐ **Appliquer un modèle efface le travail des joueurs — et c'est VOULU** (arbitrage utilisateur du 2026-09-15 : « un nouveau modèle est un nouvel exercice »). Rien n'est restitué automatiquement. Le filet est ailleurs : la **sauvegarde d'avant-application est désormais complète** (lectures + rangements + planches) et **plafonnée à 3**, purgée à chaque écriture ; aucune écriture s'il n'y a rien à sauver. ⚠ **`travail` va dans les SAUVEGARDES, jamais dans les MODÈLES** — sinon les analyses d'un exercice passé ressurgiraient chez les joueurs du suivant. ⚠ 4 applications d'affilée effacent l'état d'origine : c'est le prix assumé du plafond. Pour garder un exercice **volontairement**, on **capture un modèle** — la sauvegarde est un filet, pas une archive.

15. ⭐ **Porteur `observateur` = lecture stricte.** `?joueur=<sub>` (admin) et `?gt=<id>` pour un non-membre admin rendent un porteur **observé** ; **toute route d'écriture le refuse** (`refusObservateur()`). ⚠ Le danger n'était pas l'UI mais **l'enregistrement automatique** : ouvrir la planche d'un joueur suffisait à l'écraser. Trois verrous : serveur (403), enregistrement différé désarmé, gestes neutralisés par la classe `.lecture-seule`.
16. 🔴 **Keycloak 26 ne remplit plus `subGroups`** — les sous-groupes se lisent sur **`/groups/{id}/children`**. `tousLesGroupesDeTravail` rendait donc **toujours `[]`**, silencieusement (corrigé le 2026-09-15). Réflexe : devant une liste vide venant de Keycloak, **vérifier la forme réelle de la réponse** avant de conclure qu'il n'y a rien.

#### Où vivent les écrans (ne pas les déplacer sans raison)

- **ANIMATION** : Tableau de bord · Avatars · Groupes · **Planche officielle** · Modèles d'EHO · Import/Export. La planche officielle est là, **juste avant les Modèles**, parce qu'elle est la **vérité de l'exercice** et qu'elle **voyage avec le modèle**.
- **JOUEURS** (ce que les entraînés ont produit) : EHO joueurs · Comparatif · **Planches relationnelles** (celles des joueurs ET des GT, en lecture seule).
- **JOUEUR** : Mon EHO · EHO GT · Planche relationnelle · Choix d'avatar.

#### Vocabulaire et gestes de la planche relationnelle

- **Jonction** (dite « connecteur ») : le point matériel où converger, **parce qu'un lien ne peut pas être la cible d'un autre lien**. Deux apparences — **pastille de 16 px** sans nom, **rectangle blanc bordé de sa couleur, à l'image des cartes**, dès qu'on la nomme *(2026-09-15)*. Accroches `j-<côté>` / `s-j-<côté>` sur les quatre bords ; liens **rectilignes** depuis une jonction, pour filer **droit vers la carte**.
- **Casser un lien** : clic maintenu puis tirer — le trait s'étire et **rompt** (geste de ComfyUI). ⚠ Ne pas poser de pastilles sur le tracé : elles gênent ce geste. Les options du lien vivent dans la **barre d'inspection en pied de planche** (couleur, texte, supprimer).
- **Libellé** : **au-dessus** du trait et **orienté comme lui** (`<textPath>` sur un rail inversé). Pas de pointe de flèche — la relation n'est pas orientée.
- ↩️ **N'a PAS été retenu** : la disparition automatique d'une jonction tombée sous 3 liens (**annulé sur demande** de l'utilisateur, « remet la version d'avant c'était bien »).
- ⏳ **Concurrence non traitée** sur la planche relationnelle collective : **dernière écriture gagnante**, sans verrou. Le grain « carte » du verrou EHO ne s'y transpose pas.

### ✅ Faille des 10 routes API — FERMÉE le 2026-09-16 (par la fusion de `MEYTRE` dans `main`)
**L'ancien état** (constaté les 2026-09-11/14, sur `MEYTRE` seule) : 10 routes sans aucun contrôle — `GET /api/users` rendait les 453 avatars avec `pays`, `label`, `activite`, `observations` **sans authentification**, et `GET /api/avatars/export` téléchargeait toute la bibliothèque en classeur Excel de la même façon.
**Ce qui l'a refermée** : le commit `4b11a0d` « Fermer l'annuaire des avatars » de **Xavier** sur `main` — `exigerLecture` (toute session de la zone) / `exigerEcriture` (rôle admin) / clé de service `PLEIADE_API_KEY` en en-tête `X-API-Key` pour les appels app-à-app. Arrivé chez nous par la fusion du 2026-09-16.
**Vérifié en anonyme sur la version fusionnée démarrée** : les 9 routes → **401** ; les 8 pages joueur et animation → **307**.
- `uploads/[nom]` (servir un portrait) reste **volontairement publique** — mastorion affiche les portraits. Ce n'est pas un oubli, c'est écrit dans le code.
- ⏳ **Ce qui reste ouvert** : `GET /api/users` est gardé par `exigerLecture` et renvoie la **charge utile complète** (toute la ligne `User` moins `rawPassword` : `age, genre, pays, label, origine, religion, situation, caractere, langage, activite, observations, qualifications, aime, deteste`). Un **joueur connecté** peut donc lire ce que sa planche lui cache. Le dépouillement n'est plus contournable par un anonyme, mais l'est encore **par un participant**.
  - ⭐ **Le verrou produit qui bloquait la correction a sauté le 2026-09-16** : la page `(player)/avatars`, seul écran joueur à consommer `/api/users`, **a été supprimée**. Plus rien côté joueur n'a besoin de cette route → la **charge utile réduite pour les non-admins** (ou `exigerEcriture` pur et simple sur `GET /api/users`) est désormais applicable **sans rien casser**. ⚠ Vérifier auparavant les consommateurs restants : **MASTORION** (`admin/scenario-items.ts`, recherche par `username`) passe par la **clé de service `X-API-Key`**, pas par une session — il n'est donc pas concerné par une réduction visant les sessions non-admin.

### 🔴 Leçon durement apprise (2026-09-11)
**Ne JAMAIS déduire un nom de champ d'API par supposition avant une opération destructive.** En cherchant les groupes vides, j'ai testé `_count.users` / `userCount` / `nbAvatars` — aucun n'existe dans la réponse de `/api/groups` → **tous les groupes ont été jugés vides et les 63 ont été supprimés**. Réparé par réimport du classeur (`updated 453`, groupes et appartenances reconstruits), mais la règle vaut pour tout : **lire la réponse réelle d'abord, et vérifier sur UN élément avant de boucler.**

## 9. Règles de travail de l'agent PLEIADE

1. **Périmètre** : PLEIADE = le **système global** (orchestrateur, zones, Keycloak, infra, articulation entre apps). Le détail interne du réseau social reste chez l'agent **MASTORION** ; le contenu d'exercice chez les agents d'exercice (DELATTRE, MINAUTORE, GUILLAUME) ; l'outillage HTML brigade chez **MASTAURIGE**.
2. **Les dépôts sont partagés avec le développeur (Xavier)** : ne jamais committer/pousser sans demande explicite ; vérifier `git status`, branche et remote avant toute intervention.
2bis. ⚠⚠ **Modèle de branches — voir §2bis, c'est une règle de sécurité.** Travailler sur une **branche provisoire**, l'importer dans **`main`**, et ne **JAMAIS** pousser sur **`prod`** — ni sur le **`main` de `pleiade-platform`**, qui déploie sans sas — sans demande explicite **pour ce dépôt-là**. Pousser sur `prod` n'enregistre pas : **cela met en production devant les participants**. Toujours annoncer l'effet avant de pousser.
3. **Sur le serveur, toujours `sudo`** pour Docker/Podman (mode rootful). Ne jamais toucher à la production sans autorisation.
4. **Ne pas figer le nom « MASTORION »** dans les productions durables : le réseau social sera renommé.
5. **CONSULTER avant / CONSIGNER après** — cette mémoire + `JOURNAL.md`.
6. Règles transverses MINERVE applicables aux contenus : camps (registre MASTAURIGE fait foi), GET, numéros fictifs, langue de l'avatar, pas de détail opérationnel réel.

---

## 10. Points ouverts / à trancher avec l'utilisateur

- ✅ **Sort du travail EHO Angular — TRANCHÉ (2026-09-11)** : porté vers le nouvel EHO (trombinoscope, modèles, STARTEX, planche joueur, comparaison) ; **les cellules/équipes sont écartées**. La branche `origin/feat/eho` de mastorion n'a plus vocation à être fusionnée.
- ✅ **Faille d'autorisation des 10 routes API — FERMÉE** le 2026-09-16 par la fusion (cf. § 8bis). ⏳ **Reste à trancher** : la charge utile réduite de `GET /api/users` pour les non-admins — un joueur connecté lit encore ce que sa planche lui cache.
- ✅ **`main` poussé** le 2026-09-16 (`e3e2acc..ff1c63a`) — Xavier voit la fusion. `prod` non touchée, aucun déploiement déclenché.
- ⏳ **Deux configs Prisma sur `main`** : `prisma.config.ts` (Xavier) et `prisma7.config.ts` (nous, depuis le commit initial). Prisma charge **`prisma7.config.ts`**. Même schéma et même URL des deux côtés, donc sans effet aujourd'hui — mais à unifier avec Xavier.
- ⏳ **Un comportement de `main` écarté par la fusion** : un opérateur sans le rôle admin est **redirigé vers `/mon-eho`** (notre décision du 2026-09-14) au lieu de l'écran « Accès refusé » de Xavier. À lui signaler.
- ⏳ **Modèle DELATTRE 26 à part ?** HETTA et Kimberley sont aujourd'hui DANS le modèle `SKOLKAN` ; l'utilisateur peut vouloir un modèle distinct pour l'exercice.
- ✅ **Nom du réseau social — TRANCHÉ** : c'est **`social`** (dépôt `app-social`, commit « Devenir social : renommage et mise en production automatique »). « MASTORION » n'est plus qu'un nom d'ancêtre — **ne plus l'employer** dans les productions durables.
- ✅ `pleiade-infra` **est cloné** (`C:\CECPC\pleiade\pleiade-infra`) — constaté le 2026-09-16 ; la mémoire l'affirmait absent à tort depuis le 2026-09-11.
- ⏳ Le **package STARTEX**, les **452 personas** et les classeurs MINERVE (`MASTORION\BIBLIOTHEQUES\`) visent le schéma MASTORION ; vérifier leur import dans le **nouvel EHO** (format CSV attendu, `id` = UUID Keycloak).
- ⏳ **Groupes de travail réels** : les sous-groupes `/GT/1re Division` et `/GT/27e Brigade` sont des **groupes d'essai** — à remplacer par les vrais GT de l'exercice.
- ⏳ **Concurrence sur la planche relationnelle collective** (`eho_graphes` d'un GT) : aujourd'hui **dernière écriture gagnante**. Le verrou par carte ne s'y transpose pas — décider du modèle (verrou de planche, fusion, ou statu quo assumé).
