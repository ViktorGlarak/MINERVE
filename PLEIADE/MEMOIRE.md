# MÉMOIRE — PLEIADE (système global d'exercice)

> **Source de vérité durable de l'agent PLEIADE.** Créée le **2026-09-11**.
> ⭐ **RÉFLEXE NON NÉGOCIABLE : CONSULTER cette mémoire AVANT toute intervention · y CONSIGNER APRÈS chaque avancée**, sans attendre de rappel utilisateur.
> CR daté → `PLEIADE\JOURNAL.md` · règle / capacité durable → **ce fichier**.
> 🔒 **Sécurité (⭐ 2026-10-01)** : la doctrine, les règles de sécurité décidées et le **plan de durcissement** de la plateforme vivent chez l'agent **CYBERSECU** (`CYBERSECU\MEMOIRE.md`). Le consulter avant toute intervention qui touche l'authentification, les secrets, TLS, VPN, en-têtes, droits ou anonymat, et l'y consigner après.

---

## 1. Ce qu'est PLEIADE — en une phrase

**PLEIADE est l'écosystème logiciel complet d'entraînement du CECPC** : un **orchestrateur de zones d'exercice** qui déploie, dans des espaces isolés, des instances d'applications (réseau social, gestion d'avatars, sites web…) avec une **authentification centralisée Keycloak**.

⚠ **Changement de nom mené à son terme** — deux étapes, la seconde constatée le **2026-09-16** :
1. *(2026-09-11)* le programme entier s'appelait **MASTORION** → il devient **PLEIADE** (la plateforme, l'orchestrateur, l'ensemble), et « MASTORION » se réduit au **réseau social** seul.
2. ⭐ *(constaté le 2026-09-16)* le réseau social a **lui aussi** été renommé : c'est **`social`**, dépôt **`app-social`**.

👉 **Le mot « MASTORION » ne désigne plus rien de vivant.** Il ne subsiste que comme nom de l'ancêtre du réseau social (dépôt `mastorion`, figé) et comme nom de l'**agent MINERVE** qui en tient l'expertise. **Ne plus l'employer dans les productions durables.**

---

## 2. Organisation GitHub — `cecpc-pleiade`

⭐ **12 dépôts, TOUS clonés dans `C:\CECPC\pleiade\`** *(relevé et complété le 2026-09-16 — les 7 `app-*` manquaient)*. Un dépôt = une brique déployable ; **les 8 apps du catalogue ont chacune le sien**.

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
| ⭐ **`app-leac`** | **Contrôle des PC** — préparation, notation **terrain sur tablette hors ligne**, concaténation par VPN, 3A et compte rendu *(créé 2026-09-17, 12ᵉ dépôt)* | Next.js 16 + Prisma 7 + IndexedDB | **3700** |

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
| `eho` · `app-social` · `app-admin` · `app-cockpit` · `app-press` · `app-messagerie` · ⭐ `app-leac` · ⭐ `app-melmil` | **`prod`** |
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

### ⭐⭐ Domaine et adressage — **relevé SUR LE SERVEUR** le 2026-09-17

> ⚠ La mémoire annonçait `*.mastorion.internal`. **C'était faux.** Ce qui suit
> n'est pas déduit des dépôts : c'est mesuré sur le serveur, par VPN.

| Ce qu'on veut joindre | Adresse réelle | Comment on le sait |
|---|---|---|
| Tableau de bord de l'orchestrateur | **`pleiade.cecpc.internal`** | répond 302 → `/auth/login` |
| Keycloak | **`auth.cecpc.internal`** | route en dur dans `docker-compose.prod.yml` |
| Registre d'images | ⭐ **`registry.cecpc.internal`** | `/v2/_catalog` répond ; `registry.mastorion.internal` est **mort** |
| **Portail d'une zone** | **`{zone}.pleiade.internal`** | tout `{x}.pleiade.internal` répond 302 |
| ⭐ **Instance d'application** | **`{instance}.{zone}.pleiade.internal`** | `eho.exercice.pleiade.internal` répond 307 |

⭐⭐ **`BASE_DOMAIN` = `pleiade.internal`** — et non `cecpc.internal`, qui ne sert
qu'aux hôtes d'infrastructure. **Déterminé par l'épreuve** : `{x}.pleiade.internal`
est capté par le routeur de portail (302), `{x}.cecpc.internal` ne l'est pas (404
Traefik). ⚠ **Ne pas déduire cette valeur des dépôts** : elle vit dans le `.env`
du serveur, et les trois candidats qu'on y lit se contredisent.

⭐ **Certificats : il y en a un PAR ZONE, et c'est nécessaire.** Un wildcard TLS
ne couvre **qu'un seul niveau** — `*.pleiade.internal` matche
`exercice.pleiade.internal` mais **pas** `leac.exercice.pleiade.internal`. Traefik
présente donc, selon le SNI demandé :
- `*.cecpc.internal` (+ `*.pleiade.internal`) pour l'infrastructure ;
- ⭐ **`*.exercice.pleiade.internal`** pour les instances de la zone `exercice`.

👉 **Créer une zone impose donc un certificat pour elle.** Une zone dont le
certificat manque servira ses instances sous un certificat qui ne les couvre pas
— avertissement de sécurité **devant les participants**.

⚠ **`pleiade-infra` NE REFLÈTE PLUS LE SERVEUR** : `make-cert.sh` et
`traefik/dynamic/` y parlent encore de `mastorion.internal`, domaine qui ne
répond plus. Le dépôt a dérivé de la réalité — ne pas s'y fier pour l'adressage.

### ⭐ Zone `cecpc-div-eval` — LEAC en production (2026-09-17)

**Première mise en production de LEAC réussie.** L'instance répond à
`https://leac.cecpc-div-eval.pleiade.internal` — 307 vers `/connexion`,
`/api/sante` en 200, `/api/service/health` en 401 sans clé.

⭐ **Le certificat par zone est bien créé automatiquement** :
`*.cecpc-div-eval.pleiade.internal`. Le mécanisme décrit plus haut fonctionne
pour une zone neuve.

⚠ **Traefik rend 404 tant que le conteneur n'est pas prêt** — le temps de tirer
l'image, de pousser le schéma et de démarrer. Ça ressemble à une erreur de
configuration et n'en est pas : attendre une minute et recharger.

⚠⚠ **`pleiade-promouvoir` ne connaît PAS `leac`.** La dernière étape du workflow
échoue donc, et le job apparaît en rouge alors que l'image est bien au registre.
Sans conséquence pour une PREMIÈRE instance (la promotion ne met à jour que des
instances existantes), mais **bloquant dès la deuxième mise à jour** : il
faudrait recréer l'instance à la main. À faire ajouter côté serveur (script
`/usr/local/sbin/pleiade-promouvoir` + sudoers du compte `runner`).

### Zone `exercice` — ce qui tourne (2026-09-17)
`eho.exercice.pleiade.internal` répond. Registre : `admin`, `cockpit`, `eho`,
`messagerie`, `pleiade-orchestrator`, `presse`, `social` et ✅ **`leac`**
(étiquettes `latest` et `a747d4f`).

⚠ Ce registre publie des manifestes au format **OCI**, pas Docker v2 : une
requête avec le mauvais en-tête `Accept` rend 404 sur un manifeste qui existe.

### Chemins sur le serveur
`~/mastorion/pleiade/` (orchestrateur) · `~/mastorion/mastorion-v0/` · `~/mastorion/infra/` · `~/mastorion/pleiade/data/zones/` (instances déployées)

⚠ **PKI** : certificat wildcard `*.mastorion.internal` + `*.cecpc.mastorion.internal` géré dans `pleiade-infra`. Les clients VPN doivent installer `pki/ca.crt`.
- ⭐ **Vécu le 2026-09-25 sur iPhone** : les zones (`*.cecpc-div-eval.pleiade.internal`…) sont signées par **« Mastorion Internal CA »**.
  - **Symptômes** si l'autorité n'est pas approuvée sur l'appareil : un **⊗** « non sécurisé » dans Safari, puis, dans LEAC, la page « **Sans réseau — Cette page n'est pas sur l'appareil** ». Le service worker n'hérite pas de l'exception acceptée dans Safari. Pourtant le VPN est actif et le PC marche.
  - **Correctif iOS** :
    1. installer `pleiade-infra\pki\ca.crt` (profil) ;
    2. ⚠ *Réglages → Général → Informations → Réglages de confiance des certificats* → activer l'autorité ;
    3. supprimer les données du site dans Safari ;
    4. rouvrir.
  - **À faire sur chaque tablette de terrain AVANT l'exercice.**

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
- une **route Traefik** : `{instanceId}.{zoneName}.pleiade.internal` *(voir §3 — relevé sur le serveur)*

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

`pleiade-platform/catalog/*.yml` — **10 apps** *(`leac` ajouté le 2026-09-17, `melmil` le 2026-09-22, **poussé sur `main` le 2026-09-23** avec son rôle d'accès)* :

⭐ **Chaque entrée du catalogue a SON dépôt** (correspondance 1:1 vérifiée le 2026-09-16) :

| App (YAML) | Dépôt | Ce qu'elle fait | Rôles Keycloak |
|---|---|---|---|
| `social` | **`app-social`** | Réseau social d'exercice — **remplace `mastorion`** | `animateur` (seul ; lecture seule sans lui) |
| `presse` | **`app-press`** | Site de presse — 1 instance = 1 titre ; **site public ANONYME** + rédaction | ⚠ **2 rôles** : `journaliste` (écrire et publier) · `directeur` (+ réglages). *« Rédacteur en chef » a été **fusionné** dans `journaliste` le 2026-09-14 (`e985eda`) — « distinguer qui écrit de qui publie ajoutait un réglage à tenir sans rien protéger ». ⚠ Le `README`/`CLAUDE` d'`app-press` le mentionnent encore : **eux** sont périmés, le catalogue fait foi.* |
| `messagerie` | **`app-messagerie`** | Messagerie instantanée — canaux, groupes, privés, programmés | `admin` · `moderateur` *(outil de JOUEUR : tout compte du royaume entre ; les rôles ne servent qu'à la supervision)* |
| ⭐ `admin` | **`app-admin`** | **Administration de la zone** : scénarios multi-apps, publication orchestrée | Administration · Conduite d'exercice |
| ⭐ `cockpit` | **`app-cockpit`** | **Veille multi-réseaux** de la zone | Veille · Environnement |
| `eho` | **`eho`** | Identités de la zone — **notre chantier**, et **source d'identité de toutes les autres** | Administration · Environnement |
| `wordpress` | **`app-wordpress`** | CMS (OIDC Keycloak pré-configuré) — ⚠ **app générique, HORS contrat de zone** *(vérifié 2026-09-23)* : WordPress officiel + plugin OIDC + 1 `mu-plugin` (1 commit, 11/09) ; comptes WP **locaux** créés au 1er login (clé `sub`), **pas** d'identités eho, **pas** d'`/api/service/*` → ni l'admin de zone ni le cockpit ne le pilotent/lisent. Rôle probable : le « site quelconque » (blog, ONG, mairie, parti) que `app-press` ne sait pas faire. Absent de la présentation de Xavier. | `admin` Administrateur · `editor` Éditeur · `author` Auteur *(le mu-plugin mappe aussi `contributor`, non déclaré au catalogue ; sans rôle → `subscriber`)* |
| `webserver` | **`app-webserver`** | Fichiers statiques avec explorateur admin — *(lu 2026-09-23)* Express + 292 lignes, 1 commit (11/09). **Public anonyme** : tout fichier du volume `data/files` est servi tel quel (`/Site TV4/article.html`). **`/_admin`** (rôle KC `admin`) : parcourir, téléverser, créer dossier, renommer, supprimer, télécharger. ⚠ `index:false` → pas d'`index.html` auto (la racine `/` renvoie 404, il faut l'URL exacte du fichier) · ⚠ cookie admin = durée du jeton KC (~5 min) · hors contrat de zone (pas d'`/api/service`, pas d'eho). 👉 **Hôte naturel des `Sites/` HTML de MASTAURIGE, déposés tels quels.** | `admin` Administration *(seul rôle au catalogue)* |
| ⭐ `leac` | **`app-leac`** | **Contrôle des PC** — notation terrain hors ligne, concaténation au retour | `admin` *(référentiel seulement — voir ci-dessous)* |
| ⭐ `melmil` | **`app-melmil`** | **Planche des injects** (EVENT × jours de jeu) alimentée par les **exports JEMM** — reprise du MELMIL de MASTAURIGE ; v0 : état dans le navigateur | ⭐⭐ **`admin`** *(« Animation ») — **obligatoire pour entrer** : la planche révèle le montage de l'exercice, un entraîné qui l'ouvre sait tout d'avance. Ne cocher QUE les groupes d'animation.* |

⚠ **`admin` et `cockpit` sont nouveaux et recoupent directement le savoir MINERVE** — l'un
orchestre des déroulés heure par heure avec import XLSX (cf. MELMIL / synchromatrice), l'autre
fait de la veille et du reporting comparatif. Voir `REFERENCES/README.md`.

Un template déclare : `image`, `port`, `healthcheck`, `icon` · `keycloak` (clientId + clientType) · `requires` (DB + mapping d'env) · `env` (variables typées : select, couleur, nombre, `secret`, `editable`, défauts avec substitution `{instance}` / `{domain}` / `{auto}`) · `volumes`.

> ⚠⚠ **`requires` est lu À LA CRÉATION d'une instance, et une seule fois.**
> `createInstance` provisionne la base d'après `tpl.requires` au moment où
> l'instance naît (`zone-manager.ts`). **Aucun chemin de réparation n'existe** :
> ajouter `requires: mariadb` au catalogue **ne donne pas** de base aux
> instances déjà créées, qui démarrent alors sans `DATABASE_URL`.
> ⇒ **Ordre obligatoire** : pousser le catalogue **d'abord**, créer l'instance
> **ensuite**. Une instance créée trop tôt se **supprime et se recrée**.
> *(Vécu le 2026-09-23 sur l'instance melmil de `delattre-26`.)*

> ⚠⚠ **Deux pièges d'écriture d'un YAML de catalogue, tous deux vécus le 2026-09-23 — et tous deux désormais tenus par `scripts/test-catalogue.mts`** :
> 1. **Un `:` suivi d'une espace dans un scalaire NON quoté** rend le fichier illisible. Le catalogue étant chargé **en bloc**, c'est **tout le catalogue** qui cesse de fonctionner sur le serveur, pas seulement l'app fautive. ⇒ **Quoter** toute description contenant `:`.
> 2. **Une description de rôle de plus de 255 caractères** fait échouer la **création d'instance** : `KEYCLOAK_ROLE.DESCRIPTION` est un VARCHAR(255), Keycloak rend **500 `unknown_error`** et l'interface affiche `Failed to create client role "<role>": 500`. ⇒ Rester **sous 255** ; `descriptionDeRole()` tronque désormais en dernier recours, avec un avertissement au journal.

> **Ajouter une app au catalogue = déposer un YAML** — c'est une opération de contenu, pas de code.
> ⚠ **Mais le catalogue est copié DANS l'image de l'orchestrateur** (`COPY catalog/ catalog/`) : il faut donc **redéployer `pleiade-platform`** pour qu'un nouveau YAML atteigne le serveur — donc pousser sur son `main`, **qui déploie sans sas**.

> ⭐ **Leçon de `leac` sur les rôles Keycloak** *(2026-09-17)* : ne déclarer au royaume que ce qui est **stable**. « Chef de contrôle », « chef d'équipe », « officier de marque » sont des **fonctions tenues dans une équipe**, qui changent d'un contrôle à l'autre — le même officier est chef d'équipe lundi et contrôleur S4 jeudi. Les mettre dans Keycloak obligerait à le rejouer à chaque nouvelle équipe, et **les deux vérités divergeraient au premier oubli**. Elles restent donc dans l'app. Le royaume ne tranche que l'accès au **référentiel**.

### ⭐⭐ 2026-10-05 : le PORTAIL d'une zone EXIGE LA CONNEXION (décision utilisateur) — `pleiade-platform` `f8c7127`

Le portail `<zone>.<domaine>` n'est plus public : connexion au **royaume de la zone** (client confidentiel **`portail`**, créé à la demande par `ensurePortailClient`), flux code + **PKCE S256 + state + nonce**, session = cookie signé 1 h (`src/portail-auth.ts`, routes `/_portail/connexion|retour|deconnexion`). Chaque carte se règle **par groupe Keycloak** pour **toutes** les apps (bouton œil → « Tout le monde / Seulement certains groupes / Personne », `orch_instances.portail_groupes` = JSON d'IDENTIFIANTS de groupe, NULL = tous ; `visiblePour` dans `portail.ts`). Le visiteur porte des NOMS de groupe (claim `groups`) rapprochés des identifiants (relus toutes les 60 s). ⚠ Toujours **pas une protection** : l'adresse de l'app reste joignable, c'est le **bouclier** qui interdit. Remplace la décision du 2026-09-23 ci-dessous (« pas de connexion obligatoire sur le portail ») — la doctrine CYBERSECU (pas de confiance liée au réseau, moindre exposition) va dans ce sens. Conséquence : toute personne qui consulte le portail doit avoir un **compte dans la zone**.

### ⚠⚠ (HISTORIQUE, remplacé le 2026-10-05) Le PORTAIL d'une zone est PUBLIC — relevé dans le code le 2026-09-23

`<zone>.<domaine>` (ex. `delattre-26.pleiade.internal`) est servi par un
middleware d'`index.ts` placé **avant** le garde de session (`requireAuth`,
plus bas dans le même fichier), et il affiche `getPortalData(zone)` — un
`SELECT` de **toutes** les instances de la zone. Donc :

- **aucune authentification** n'est demandée pour voir la page ;
- **aucun filtrage** par utilisateur, groupe ou rôle : toutes les cartes sont
  rendues pour tout le monde, avec le nom et l'adresse de chaque instance.

⭐ **Conséquence à connaître avant de promettre une confidentialité** : ne pas
cocher un groupe sur le **bouclier d'une instance** ne **cache pas** sa carte
du portail — cela lui **retire l'accès à l'application**. La carte reste
visible et l'adresse devinable ; c'est donc **l'app elle-même** qui doit
refuser, côté serveur (c'est ce que fait MELMIL, cf. son `habilitation.ts`).

⏳ Filtrer le portail supposerait de l'authentifier : changement de
comportement pour **toutes** les zones et **toutes** les apps — à décider avec
l'utilisateur et Xavier, pas à glisser dans une livraison.
⭐ **Depuis le 2026-09-23 (`4b1ddea`)**, le portail **regroupe** les instances
d'un même type en une carte → page de choix **`/<type>`** (site + espace
d'administration via `adminPath`), porte une pastille **« nouveau »** (dernière
parution lue sur `retex`, mémoire **par appareil**) et respecte une case
**« visible sur le portail »** par instance (`portail_visible`). ⚠ Cette case
n'est **pas** une protection. Rendu dans `src/portail.ts` (pur, testé).
⭐ **Renommée « Masquée aux joueurs » le 2026-09-23** (demande utilisateur, branche
`libelle-masquee-aux-joueurs`, commit `839d389`, **non poussé**). Comportement
**vérifié dans le code** : seule la requête du portail (`getPortalData`) filtre
`portail_visible = 1` ; le **tableau de bord opérateur** et la **découverte
entre apps** voient toujours l'instance ; son **adresse reste joignable**. ⚠
Nuance : le portail est **le même pour tout le monde** (pas de connexion) —
masquer retire la carte à **quiconque passe par le portail**, animateurs
compris ; ils y accèdent par l'adresse ou par le tableau de bord Pléiade.
⚠ **Décidé avec l'utilisateur** : pas de connexion obligatoire sur le portail,
pas de bouton « invité » (décoratif : c'est chaque app qui décide). Le SSO de
royaume évite déjà de retaper un mot de passe d'une app à l'autre.

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
- ⭐ **Horloge du scheduler (règle du 2026-09-28)** :
  - un item part quand `somme des deltas de sa chaîne ≤ (maintenant − startAt)` ;
  - un **début passé** fait donc partir d'un coup tout ce qui est échu. C'est pourquoi le lancement à début passé exige un choix : « Maintenant » décale le scénario, « Rattraper » est assumé ;
  - la **pause décale** début et fin (`paused_at`).

### 4. Le contrat `/api/service/*` est le MÊME partout
`app-social`, `app-press` et `app-messagerie` exposent le même contrat (`health`, `accounts?identity=`, `users?search=`, `groups`, `publish`, `posts/[id]`…).
- ⭐ **`GET /health` s'annonce** (`kind`, `needs_title`, `supports`) : c'est ainsi que l'admin de zone **adapte son formulaire** sans coder en dur le nom d'une app.
- ⭐ **Un `publish` sans `reply_to_post_id` est un article ; avec, c'est une réaction de lecteur** — ou une entrée de fil si l'article est suivi en direct. Le même verbe sert donc à greffer un emballement sur un article existant.
- 👉 **`app-admin` vise n'importe quelle app sans rien savoir d'elle.** C'est ce qui rend les scénarios multi-apps possibles.
- ⚠ Un item de scénario cible **une INSTANCE (`instanceId`), jamais un type de réseau** : *« s'il y a trois YouTube, ce sont trois cibles »*.
- ⚠ **Un message publié par le scénario doit être strictement indiscernable d'un message tapé par un joueur** : `source = "scenario"` n'apparaît **jamais** côté joueur, seulement en supervision.

### 5. ⭐ Lien admin ↔ MELMIL (2026-10-02, avis DESIGNER n°28)
- **Un scénario de l'admin est rattaché à un incident MELMIL** : `Scenario.incidentId` contient l'identifiant interne de l'incident, qui survit au recodage et à l'alignement JEMM ; `incidentCode` n'en est qu'une copie.
  - L'incident est **obligatoire** à la création, sauf dans une zone sans MELMIL.
  - Les anciens scénarios dont le nom porte un code connu sont rattachés automatiquement.
- **Routes de service** (clé de la zone) : MELMIL `GET /api/service/incidents` (liste **anonyme**) ; admin `GET /api/service/scenarios`.
- **Découverte** : chacune trouve l'autre par son `appType` (« melmil », « admin »). En local : `ADMIN_DEV_INSTANCES` et `MELMIL_DEV_ADMIN_URL`.
- **Côté MELMIL** : « ▶ n » sur la carte et bloc « Scénarios (admin) » dans la fiche. « Créer un scénario pour cet incident » ouvre `admin/scenarios?nouveau=<id|code>`.

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
- ⭐ **Charge à grande échelle — règle depuis le 2026-09-24** *(DE LATTRE 26 ≈ 3 500 avatars ; branche `refonte-v2`, non poussée)* :
  - **Ne plus jamais charger TOUS les avatars complets côté client.** Le trombinoscope passe par **`GET /api/avatars/planche`**. Sans paramètre, il reçoit le **sommaire** (pays → blocs, effectifs). Avec `?section=&fonction=&offset=&limit=`, il reçoit les cartes d'un bloc. Avec `?q=`, il lance une recherche serveur plafonnée à 400. La route est ⚠ **réservée à l'animation** (`exigerEcriture`) : elle porte pays et fonction officiels.
  - La liste **`GET /api/eho/mon-eho`** est **allégée** :
    - elle ne porte plus de bio (drapeau `bioACharger`), et le texte est lu à l'ouverture par le nouveau **`GET /api/eho/mon-eho/[id]`**, avec la même portée `?gt=` et le même dépouillement ;
    - ses **champs vides sont omis** (`compacte`), et le client les remet avec `completerCarte`.
  - **Aucun autre dépôt** ne consomme ces routes (vérifié). Le contrat `/api/users` consommé par MASTORION est **inchangé**.
  - À l'affichage : **60 cartes par bloc** + « Afficher plus », cartes **mémoïsées**, recherche **différée**.
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
7. ⭐ **NOTES DE VERSION à chaque mise à jour poussée** *(demande de Xavier, validée par l'utilisateur le 2026-10-03)* : chaque dépôt `cecpc-pleiade` a un `NOTES-DE-VERSION.md` à sa racine (le plus récent en haut ; une section par jour `## AAAA-MM-JJ — version X` ; « Ce qui change pour les utilisateurs » en langage clair ; « Technique » = commits + « Après la mise en ligne » s'il y a une action + point technique utile à Xavier ; section « Pas encore en ligne » pour ce qui est sur `main` mais pas sur `prod`). **On le met à jour dans le MÊME commit que la modification**, avant le push. Rattrapage fait depuis le 20/09/2026. Constat du 03/10 : aucun CHANGELOG n'existait, et l'étape « tag prod-* » du workflow échoue en silence (aucun tag sur GitHub) — à signaler à Xavier.

---

## 10. Points ouverts / à trancher avec l'utilisateur

> ⭐ **Diagnostic complet du 2026-10-03** — `PLEIADE\DIAGNOSTIC_2026-10-03.md` : contrôle des 12 dépôts (tests, CI, version, dette), carte besoins → outils (RETEX, DE LATTRE, vision Xavier), 9 constats, 8 axes A–H priorisés. **À relire avant tout nouveau chantier.** Points saillants : mise en ligne non prouvable (admin/social/cockpit/platform sans version), tests jamais lancés en CI pour eho et social, 4 outils pour planifier et 4 pour la presse, le besoin n°1 du RETEX (retour sur le traitement des injects) sans outil, « TF1 Info » (média réel) en production.


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


## ⭐⭐ Règle — Émetteur Keycloak : PUBLIC dans `issuer`, INTERNE pour token/userinfo/jwks *(2026-09-21)*

Depuis le `frontendUrl` figé (2026-09-13), Keycloak annonce l'émetteur public
quelle que soit l'URL appelée. Une app Auth.js qui déclare l'émetteur interne
échoue à la découverte (« issuer mismatch ») → page « problem with the server
configuration » au clic « se connecter ». Motif correct : `messagerie`,
`press`, `admin`, `leac`, `eho` (corrigé `1e44e2c`). ⚠ `app-cockpit` portait
encore l'erreur : corrigé le 2026-10-01 (`ddc73b7`), après avoir été constaté
en salle. Leçon : un défaut connu se corrige, il ne reste pas noté en règle. Diagnostic sans logs : `/api/auth/csrf` OK + signin →
`error=Configuration` = émetteur ; csrf KO = `trustHost`/`AUTH_SECRET`
(image ancienne).

## Règle — `pleiade-platform` : `package-lock.json` et `public/style.css` modifiés localement = artefacts de MON poste *(2026-09-21)*

Pas du travail de Xavier (lock resynchronisé par npm, Tailwind non minifié
écrit par `npm run dev`). Se jettent (`git checkout --`) avant un pull.

## Règle — Les volumes « ./… » d'une instance sont préparés INSCRIPTIBLES avant le démarrage *(2026-10-01, `pleiade-platform` `b946897`)*

Un volume de catalogue `./data/x:/data/x` est un montage de dossier du serveur, qui **masque** le dossier préparé dans l'image. Créé par le moteur de conteneurs au premier démarrage, il appartenait à l'utilisateur du serveur. Les apps tournent sous `nextjs` : écriture impossible (`EACCES`). MELMIL refusait ainsi tout dépôt de fichier.

`preparerVolumes()` crée ces dossiers et les passe en 0777, dans `deployInstance` et `deployZone`.

**Diagnostic sans compte** : `/api/sante` de MELMIL renvoie `medias: "ok"` ou `"ecriture impossible (CODE)"`.

## Règle — Démarrer une instance TIRE l'image d'abord *(constaté le 2026-09-21, ✅ corrigé le 2026-10-01, `pleiade-platform` `f020b4e`)*

**Avant** : `deployInstance` faisait `up -d` seul, sur le `latest` déjà présent dans
le magasin podman du serveur (souvent ancien). Seul **« Déployer » la zone**
(`deployZone`) faisait `pull` puis `up -d`. La promotion épingle un tag de commit,
ce qui force le pull, mais ne vise que les zones `zone_type = prod` (`orion26`,
`cecpc-div-eval` ; pas `delattre-26`).
Symptôme : une instance neuve naît en retard (presse sans « maquettes existantes »,
pages récentes en 404). **Revu le 2026-10-01 avec `tv4-international` sur DE LATTRE.**

**Maintenant** : `deployInstance` fait `pull` (5 min au plus) puis `up -d`. Si le
registre est injoignable, l'instance démarre sur l'image locale et la sortie le dit.

⚠ **Leçon** : le 21/09, ce défaut a été **consigné comme règle mais pas corrigé** ;
l'utilisateur l'a cru réglé. Un défaut qui touche l'utilisateur se **corrige**, ou
se **signale explicitement comme non corrigé**. Il ne doit pas rester décrit dans
la mémoire comme une simple règle.

## Règle — Groupes de travail eho = groupes Pléiade de racine *(2026-09-21, `69260ef`)*

Sauf `cecpc`, `masteradmin`, racine `GT` ; `/GT/…` toléré. Un groupe = un
groupe de travail ; les droits restent ceux du bouclier Pléiade.

## Règle — « Au nom de » : poster sur le social = rôle `animateur` + camp ouvert dans eho *(constaté 2026-09-21, livré par Xavier 17–19/09)*

Un compte de zone ne poste **jamais en son nom** sur `app-social` : il choisit un
avatar eho (« Au nom de », `X-Act-As`). Deux verrous, tous deux côté serveur :
1. **rôle `animateur`** sur l'instance social (bouclier Pléiade, par groupe) — sans lui, lecture seule, panneau invisible ;
2. **référentiel des camps dans eho** (écran Groupes → « Camps ») : groupe d'avatars → groupes Pléiade autorisés. Rien de coché = personne, sauf masteradmin.
   - ⭐ **« Autres comptes »** *(2026-09-30, eho `c0a3ea2`)* :
     - Un groupe d'avatars **avec** des camps cochés est **RÉSERVÉ** à ces camps.
     - Tous les autres avatars forment les **« autres comptes »** : un ensemble **calculé**, jamais stocké, où un nouvel avatar entre tout seul.
     - Y ont droit **d'office** les camps cochés sur au moins un groupe réservé, et **en plus** ceux ajoutés dans l'encart « Autres comptes » de l'écran Groupes (joueurs sans camp propre, par exemple GREYCELL).
     - **Pourquoi** : sans cela, à DE LATTRE 26, ≈ 500 avatars sur 3 900 étaient incarnables ; le reste était rangé dans des groupes archivés ou dans aucun groupe.
Chaîne : social → eho `/api/impersonation` → Pléiade `resoudre-identite` (groupes + masteradmin). Fail closed si un maillon manque. Les « camps » sont **les mêmes groupes Pléiade** que nos groupes de travail (`69260ef`). Détail : JOURNAL 2026-09-21 (suite 2).

## Règle — Se déconnecter = fermer AUSSI la session Keycloak *(2026-09-21, toutes les apps Next.js)*

`signOut` NextAuth nu laisse la session de royaume ouverte → « se connecter » rouvre le
même compte en silence. Chaque app porte `src/lib/deconnexion.ts` : `signOut` local puis
`end_session_endpoint` (`id_token_hint` gardé dans le jeton, `client_id`,
`post_logout_redirect_uri`). ⚠ Pour « autre compte » : fermer d'abord, revenir sur `?changer=1`,
relancer **sans `prompt=login`** — Keycloak transmet `prompt` au fournisseur « cecpc », qui
ré-authentifierait l'organisateur (« Please re-authenticate ») au lieu de le laisser passer.
Fermer le royaume de ZONE déconnecte de toutes les apps de la zone (voulu, poste partagé) ;
la session d'organisateur (royaume `cecpc`), elle, survit (règle suivante).
Test de référence : `e2e_deconnexion.cjs` (Playwright, Keycloak local, 10 contrôles).


## ⭐ Rôles d'app : créés automatiquement (règle du 2026-09-30, `b85e2e2`)

- Un rôle **ajouté au catalogue** existe dans Keycloak dès le démarrage de la plateforme. Il est aussi créé au moment où on le coche sur le bouclier. La création ne retire jamais rien.
- ⚠ **Avant ce correctif**, cocher un rôle absent de Keycloak ne faisait **rien**, en silence. Un rôle coché avant le 30/09 à 10:29 est donc à recocher, s'il était nouveau.
- `synchroniser-roles` reste le geste explicite de **ménage** : il retire les rôles disparus du catalogue.

## ⭐ Identifiants de zone sans adresse mail (demande utilisateur du 2026-09-29, analyse, rien de modifié)

L'utilisateur veut des identifiants simples, du type `gw01`, sans adresse mail ni nom/prénom, pour des raisons de sécurité.
- **Les apps suivent le `sub` Keycloak**, jamais l'adresse (eho, admin, presse, messagerie, cockpit, MELMIL, LEAC, social) : un compte sans adresse fonctionne. Le social prend `preferred_username` quand l'adresse manque.
- ⚠ **Supprimer puis recréer = nouveau `sub`**. Ce qui était rattaché à l'ancien est perdu : auteur d'articles et de messages, contrôleurs et administrateurs LEAC, animateur du social (`users.keycloak_id`), créateur d'un scénario admin, comptes liés aux personnes dans MELMIL. En revanche, le « au nom de » vient des **groupes** Keycloak (camps), recalculés à chaque fois.
- ⚠ **Blocages relevés** (`pleiade-platform/src/keycloak-manager.ts`) :
  - `REALM_SETTINGS.registrationEmailAsUsername: true` n'est posé **qu'à la création de la zone**, et non réimposé (correction de l'analyse du 28/09) : les zones anciennes le gardent ;
  - `createUser` exigeait `email`.
- ✅ **Corrigé et EN LIGNE le 2026-09-29** (`56f0576`, poussé sur `main` à la demande de l'utilisateur, pendant la phase de planification de l'exercice) :
  - vérifié par `https://pleiade.cecpc.internal/api/version` → `commit 56f0576`, build 15:17Z ;
  - ⚠ `app.js` et les pages redirigent vers la connexion (302) : ils ne prouvent rien. **Seul `/api/version` fait foi.**
  - identifiant requis, adresse facultative, import et export avec une colonne « Identifiant » ;
  - bouton crayon **« Modifier l'identifiant »** (`PATCH /api/zones/:zone/users/:id`) qui **garde le `sub`**, avec une option pour retirer adresse, prénom et nom ;
  - `ensureIdentifiantsLibres(zone)` corrige la zone au moment de créer ou de renommer, sans toucher aux autres réglages.
- ⭐ **Keycloak 26, constaté sur un vrai conteneur** :
  1. une zone « adresse = identifiant » **refuse** un compte sans adresse (`error-user-attribute-required`) ;
  2. l'identifiant est en **lecture seule, admin compris**, tant que `editUsernameAllowed` est faux : on l'ouvre le temps du renommage, puis on le referme ;
  3. un fournisseur d'identité exige des adresses en HTTPS.
  - Essai rejouable : `scripts/essai-identifiants.mts` (Keycloak jetable sur le port 8181).
- **Xavier et Thomas** entrent par le bouton « cecpc » (royaume `cecpc`) : leurs comptes vivent hors des zones. Il ne faut ni toucher au fournisseur `cecpc` ni au groupe maître, ni supprimer leur compte miroir dans la zone (il serait recréé avec un nouveau `sub`).

## Règle — Le bouton « cecpc » d'une zone vient du ROYAUME, pas des apps *(2026-09-21)*

« cecpc Connect » (Xavier, 16/09) monte un fournisseur d'identité `cecpc` + un groupe
maître dans le royaume de chaque zone : c'est lui qui fait apparaître le bouton « cecpc »
sur l'**écran Keycloak**, par lequel un organisateur entre sans compte propre. Aucune app
n'y touche (aucune n'utilise `kc_idp_hint`). Posé à la création d'une zone, mais en
**best-effort** → une zone peut s'en passer sans que rien ne le dise. Rattrapage :
**`POST /api/zones/:zone/cecpc-connect`** (route de Xavier, idempotente), à appeler depuis la
console du navigateur sur le tableau de bord — **il n'y a pas de bouton**, et c'est voulu
(cf. la leçon du 2026-09-21 : un indicateur d'état retiré parce qu'il annonçait faux).

⚠⚠ **Le bouton « cecpc » de l'écran de connexion ne dépend que du FOURNISSEUR D'IDENTITÉ**,
pas du groupe maître : exiger les deux pour juger l'état fait passer pour cassée une zone qui
marche. Le groupe maître, lui, décide des DROITS de celui qui entre par là.


## Règle — Un client Keycloak doit déclarer l'ALLER **et** le RETOUR *(2026-09-21, `b8853e7`)*

Keycloak compare les adresses de redirection **à l'identique, sans joker** : `…/endpoint` ne
couvre pas `…/endpoint/logout_response`. Le client broker `cecpc-connect` déclare donc les
deux par zone, sinon toute déconnexion d'un compte entré par cecpc Connect finit sur
**« Invalid redirect uri »** — le royaume de la zone propageant la déconnexion au royaume
`cecpc`. ⚠ Défaut resté **dormant** du 16/09 au 21/09 : il ne s'est vu que le jour où les apps
ont commencé à fermer la session amont pour de bon. ⭐ Depuis la suite 11, **l'orchestrateur pose
ces adresses pour toutes les zones à chaque démarrage** (`reconcilierRetoursCecpcConnect`, un appel,
fusion sans retrait) : plus aucun geste manuel. `retoursCecpcConnect(zone)` est la seule source.


## Règle — La déconnexion d'une zone ne remonte PAS à l'organisateur *(décision utilisateur 2026-09-21)*

Le fournisseur `cecpc` de chaque zone est posé **sans `logoutUrl`** : fermer une session de zone
ne ferme pas la session du royaume `cecpc` (organisateur, Pléiade). Le bouton « cecpc » reste
silencieux tant que l'organisateur est connecté à Pléiade. Réconcilié **à chaque démarrage** de
l'orchestrateur (`reconcilierCecpcConnect` : adresses de retour + retrait du `logoutUrl`).
⚠ « Voir comme » (incarner un compte de zone) a été **conçu puis annulé** le même jour : jugé
plus risqué ; le garde-fou de l'outil l'avait d'ailleurs bloqué. Ne pas le relancer sans demande.


## Règle — Modèles d'EHO : « intégrés » (dans l'image) vs « capturés » (volume de l'instance) *(2026-09-21)*

Un modèle capturé depuis l'écran vit dans `EHO_DATA_DIR/templates/` — **le volume de l'instance**,
donc invisible ailleurs. Ce qui doit exister sur **toute** zone se met dans `eho/modeles/<code>/`
(`manifest.json`, `payload.json`, `portraits/`) : c'est copié dans l'image, listé `builtin`, non
supprimable. ⭐ **« SKOLKAN PERSONA 21.09.26 »** (`SKOLKAN-PERSONA-21-09-26`) : 453 avatars, 58 groupes,
STARTEX, planche officielle, 118 portraits. ⚠ Dans un payload, les `avatar_url` doivent être
**relatives** (`/api/uploads/<nom>`) et les fichiers livrés : l'application les rend absolues pour
l'instance. Un modèle capturé embarque des adresses absolues du poste d'origine → portraits cassés ailleurs.


## Règle — Une image avec volume de données ne fixe pas `USER` : l'entrypoint rend le volume puis abandonne root *(2026-09-21)*

Pléiade crée le dossier hôte `data/` d'une instance en **root** ; un `chown` fait dans l'image
est recouvert par le montage. Une image en `USER nextjs` ne peut alors **rien écrire** dans son
volume (eho : « EACCES mkdir /app/data/uploads » ; LEAC : pièces jointes). Schéma retenu (eho,
LEAC) : entrypoint root → `mkdir -p` + `chown -R nextjs:nodejs /app/data` → `exec su-exec nextjs`.
Tester une image sur un **volume pré-rempli par root**, pas sur un volume neuf (initialisé depuis
l'image, donc déjà bien possédé — le cas du serveur ne s'y reproduit pas).


## Règle — Toute adresse absolue rendue au navigateur se construit sur les en-têtes du proxy *(2026-09-21)*

Derrière Traefik, `req.url` est ce que le conteneur reçoit (`http://`, réseau interne). Une
adresse absolue bâtie dessus (portraits eho, retour de déconnexion…) donne du **contenu mixte**
ou un mauvais hôte. Ordre : variable publique explicite (`EHO_PUBLIC_URL`, `NEXTAUTH_URL`) →
`X-Forwarded-Proto`/`X-Forwarded-Host` → origine de la requête. eho : `originePublique(req)`.


## Règle — Vérifier un déploiement d'app par sa MARQUE DE VERSION, jamais par une empreinte d'assets *(2026-09-21)*

`GET /api/sante` → `{ version }` sur **LEAC** (`lib/version.ts`) et **eho** (idem depuis `2026-09-21.1`).
Incrémenter la marque à chaque push sur `prod`. Une empreinte des chunks `/_next/static` ne bouge
pas quand seule la partie serveur change → faux « pas déployé » (constaté sur trois builds de suite).


## Règle — eho : UNE fiche d'avatar, UN verrou, partagés par tous les écrans *(2026-09-22)*

La fiche d'un avatar vit dans **`components/fiche-avatar.tsx`** (`FicheAvatar`, `CarteFiche`,
`couleurCarte`) et son verrou dans **`lib/verrou-fiche.ts`** (`useVerrouFiche`). La planche de
rangement (« Mon EHO », « EHO GT ») **et** la planche relationnelle les utilisent : c'est le même
avatar, ce doit être la même fiche, jusqu'au mot près. ⭐ **La PORTÉE ne vient jamais de la
fiche** : chaque écran interroge `GET /api/eho/mon-eho` avec la sienne (`?gt=…`, `?officiel=1`,
observation), et la fiche affiche la carte qu'on lui donne — donc celle du bon porteur, par
construction. Deux réglages seulement : `lectureSeule` (planche observée, planche de l'animation)
et `officiel` (toutes les cartes portent alors leur identité officielle, pas seulement les
STARTEX). Une action propre à un écran (« verser vers un GT ») se passe en emplacement, elle
n'entre pas dans la fiche.

## ⭐ Chantier — Templates MASTAURIGE en « maquettes existantes » d'`app-press` *(décidé 2026-09-23)*

**Demande utilisateur** : dans *Réglages ▸ Maquette et thème*, à droite des 4 maquettes génériques, un groupe **« Maquettes existantes »** qui reprend les sites de `EXER\AURIGE 7BB\…\LOCALSTORAGE_WEB_VERSION\Sites\` (hors Trombinoscope, TRACTS, images, COURRIERS, Communiqués officiels) ; toute la rédaction (écrire, médiathèque, réactions…) doit fonctionner avec chacun.

**Constat** : les `_TEMPLATE.html` sont des **pages d'article** à balises `{{…}}`, pas des sites (ni une, ni rubrique, ni direct, ni recherche) ; nav / sidebar / « related » / ticker **en dur** ; polices **Google Fonts** (→ à embarquer, réseau fermé) ; logos base64. La rédaction `/redaction` a son propre thème → **indépendante de la maquette** ; le travail est côté site public.

**Décisions utilisateur (2026-09-23)** :
1. **Habillages FIDÈLES, par vagues** — CSS du template repris quasi tel quel, **confiné** à l'habillage ; structure réécrite en composants React (en-tête, pied, article, une, rubrique, direct, recherche) branchés sur les données ; réactions + fil en direct **greffés**. Vagues : ① TV4 · Today Mercure · BC1 ② Hexagone · TF1 · Omerta ③ ONU · OTAN · ZubrRadio · **EFS**.
2. **Les 10 sites, EFS compris** (EFS = site de campagne, champ « appel à l'action »).
3. ⚠ **Branche LOCALE seulement** sur `app-press` — rien livré, rien poussé (pas de droit d'écriture, cf. mémoire auto `pleiade_droits_github`) ; livraison à décider plus tard.
4. **Charte verrouillée par défaut + bouton « Retoucher »** pour la modifier.

**Champs propres à certaines maquettes** (optionnels, visibles dans l'éditeur seulement si la maquette les emploie) : lieu/dateline (TV4, BC1), « l'essentiel » (TF1), signataire/fonction/référence (ONU, OTAN), audio/durée/transcription (ZubrRadio), appel à l'action (EFS). Correspondances directes : TITLE/HEADLINE→`title`, DECK/CHAPO→`standfirst`, BODY→`body`, HERO/HERO_CAPTION→média à la une + légende, KICKER/CATEGORY→rubrique, TAGS, DATE, AUTHOR→avatar eho.

**Source des templates** : propriété MASTAURIGE (règle « template obligatoire par site », `MASTAURIGE\MEMOIRE.md`) — l'habillage doit reproduire le template complet, jamais une version simplifiée.

**✅ Vague 1 LIVRÉE en local le 2026-09-23** — branche **`maquettes-existantes`** d'`app-press` (commit `1a40aa1`, **NON poussée**, base = `99b649f` lui aussi non poussé) : **TV4, Today Mercure, Bothnia Channel 1**. Architecture à réutiliser pour les vagues 2-3 :
- `src/skins/registry.ts` = **données** (clé, identité reprise, charte en jetons, `fields`, `colorLabels`, `swatch`) — importable côté navigateur ; `SKINS_A_VENIR` liste les 7 restants.
- `src/skins/<cle>/<Cle>.tsx` = 5 vues (`Shell`, `Home`, `Article`, `List`, `Page`, contrat `types.ts`) **sans accès base** (les pages chargent, l'habillage met en page → rendu aussi dans l'aperçu des réglages) ; `<cle>.css` = CSS du template **confiné** `.sk-<cle>`, couleurs de marque sur les jetons (`--accent`, `--urgent`…), nuances en `color-mix`.
- Réactions / fil en direct / mention d'exercice = composants génériques posés en **îlots** `.site.sk-island` (`shared.tsx`) aux jetons de la charte.
- Base : `Site.skin` (VarChar 40, null = générique) + `Article.skinFields` (JSON `{cle: texte}`, bornée par `parseSkinFields`). Polices embarquées via `next/font` (PT Serif/Sans, Oswald, Source Sans 3).
- ⚠ Piège rencontré : un composant rendu côté navigateur ne doit rien importer de `lib/site.ts` (tire Prisma/mariadb → « Can't resolve 'fs' ») → `EXERCISE_NOTICE` déplacée dans `lib/notice.ts`.
- ⚠ **Test local** : sans eho, **enregistrer un article échoue** (« Signature inconnue » — contrôle par camp **préexistant**, non modifié) ; les champs de maquette seuls s'enregistrent. Environnement : base `presse-db` (Docker, port 3320), `.env` avec `PRESSE_DEV_USER`, `next dev -p 3500`.
- Limites connues : libellés des îlots (réactions, direct) restent en **français** sur TM/BC1/ONU (sites anglais) ; la une d'un habillage n'applique que le bloc « une » de l'onglet La une (pas les autres blocs).

**✅ LES 10 SITES LIVRÉS en local le 2026-09-23** — commit `5c43ffe` (branche `maquettes-existantes`, non poussée) : vague 2 **Hexagone, TF1 Info, Omerta** + vague 3 **ONU, OTAN, ZubrRadio, EFS**. `SKINS_A_VENIR` est vide.
- **Réglages** : « Maquette du site » a **deux onglets** (demande utilisateur) — *Maquettes génériques (4)* / *Maquettes existantes (10)* ; seul l'onglet actif montre ses vignettes ; il s'ouvre sur la famille en service.
- **Champs par maquette** : `lieu` (TV4, BC1) · `bandeau` (Hexagone) · `essentiel1-3`, `source` (TF1) · `ref`, `signataire`, `fonction`, `signature` (ONU) · `emission`, `duree`, `timecode` (ZubrRadio) · `visuel`, `cta`, `cta_lien` (EFS, lien borné à `/…` ou `http(s)`).
- **Logos** des templates (base64) extraits dans `public/skins/` (hexagone, tf1, omerta, otan) ; ONU/EFS/ZubrRadio/TV4/TM/BC1 = logos en CSS/texte.
- **Corps d'article** : classe commune `.sk-prose` (encadrés, figures de l'éditeur dans toutes les chartes) ; `lib/sanitize.ts` accepte désormais les **classes des templates** (`figures-box`, `ops-box`, `decree-box`, `BodySubTitle`, `z-seg`, `dots`, `band`…) et `class` sur `ul`, `h2`, `blockquote`.
- ⚠ **Piège vérifié** : une classe d'habillage qui porte le nom d'une classe d'îlot (`wrap`, `section-title`, `reaction*`…) déborde sur la mention d'exercice ou les réactions (cas EFS `.wrap` corrigé en `efs-wrap`) ; toute règle sur balise nue (`.sk-x h2`) touche aussi les îlots → toujours préfixer.
- ⚠ **Marques réelles** : TF1 Info et Omerta Média reprennent des médias existants (logo compris) — c'est le choix des templates MASTAURIGE d'origine, reproduit tel quel ; signalé à l'utilisateur.

## ⭐ eho — RANGER LES GROUPES : procédure pour CHAQUE nouvel exercice (validée le 2026-09-28)

**Capacité** : `Group.archive` = masqué dans eho, **jamais supprimé ni renommé** ; `/api/groups` renvoie toujours tout aux autres apps (incarnation, app-admin, app-press, app-messagerie). Assistant « Ranger les groupes… » (admin) : `lib/rangement-groupes.ts` + `/api/groups/rangement`. En ligne depuis `2026-09-28.1`.

**À chaque nouvel exercice** :
1. Appliquer ou fusionner le modèle.
2. Créer le groupe **`EXERCICE <NOM>`** de l'exercice.
3. « Ranger les groupes… » → choisir l'exercice en cours → vérifier → appliquer.
4. « Ressortir » au besoin les groupes d'animation de l'exercice.
5. **Enregistrer en nouveau modèle** : le drapeau archivé voyage avec les groupes, et l'exercice suivant démarre rangé.

**Limites à connaître** :
- un nouveau pays fictif (préfixe autre que ARN / MER / FR / FRA / BOT) doit être ajouté à `PREFIXES_PAYS` (`lib/rangement-groupes.ts`) et à `FAMILLES` (page Groupes) ;
- un groupe d'animation nommé « PAYS - … » sera proposé comme classement : le décocher ;
- l'exercice en cours n'est deviné que si le nom de la zone le contient ;
- ⚠ **appliquer un modèle recrée les groupes avec de nouveaux ids** : les liens par id d'app-admin et d'app-press ne survivent pas (préexistant, à corriger).

## ⭐ app-admin — le KIT IA et l'import fiabilisé (commit `3d396fd`, ✅ EN LIGNE le 2026-09-28 soir : `main` = `prod`)

- **Un bouton « Kit IA »** dans l'éditeur de scénario. Il télécharge un `.zip` fabriqué à l'instant (`GET /api/bff/scenarios/:id/kit-ia`) :
  - `1_AVATARS.md` : par pays puis catégorie, avec @compte, nom, camp, activité, langue, groupes visibles et biographie courte, complète ou absente. Le périmètre est au choix : groupes visibles (défaut), groupes choisis, ou tous ;
  - `2_MODE_EMPLOI.md` : colonnes, apps publiables avec leurs champs annoncés, groupes visibles, règles MINERVE (langue, GET, camp…) et un exemple CSV avec de vrais @comptes ;
  - `3_GUIDE.md` : l'espace permanent, les consignes à coller, la fiche de contexte, la méthode trame → lignes → auto-vérification, la vérification avant import ;
  - `4_MODELE_VIDE.xlsx` ;
  - ⭐ `5_MODELE_DE_PROMPT.txt` *(2026-09-30)* : un prompt **COURT** à copier-coller. Il dit à l'IA de **lire les pièces jointes**, puis fixe scénario, temps (pré-rempli), rythme, avatars et la règle de la presse. **Consigne de l'utilisateur : ne pas y recopier le contexte du kit.**
    - La **rédaction de chaque média** (demandée au site par `checkAccounts`, par paquets de 150) est dans `2_MODE_EMPLOI.md`.
    - Règle : un article est signé par un journaliste **de ce média**.
    - ⭐ **Aucun ne convient** *(décision utilisateur, 2026-09-30)* : on n'invente **jamais** d'avatar. L'IA **recrute** un avatar existant du modèle SKOLKAN **SANS biographie**, pour que rien ne contredise son nouveau métier.
      - Elle le prend dans `6_AVATARS_SANS_BIO.md` : **tous** les avatars de l'EHO sans fiche bio, hors rédactions, rangés par pays, avec langue et camp.
      - Elle le choisit du même pays et de la même langue que le média, et le déclare dans l'onglet `JOURNALISTES_A_AJOUTER` (username, media, fonction, biographie_proposee).
      - Le traitant l'ajoute à la rédaction du média, et peut reprendre la biographie proposée, **avant l'import**.
- ⭐ **`lib/format-scenario.ts` = LA définition du fichier**, partagée par l'import, l'export, la fenêtre d'import et le kit. Ne jamais recopier la liste des colonnes ailleurs.
- **Import** :
  - il lit `title`, `target` et `champ:<clé>` (case à cocher : oui/non) et accepte le **CSV** (séparateur deviné) ;
  - il **contrôle tout le fichier avant d'écrire** et REFUSE : un article sans titre (app `needsTitle`), une réponse vers une autre app, une réponse vers une ligne absente ou refusée (en cascade) ;
  - il signale un champ inconnu de l'app.
- **Export** : `title`, `target` et les colonnes `champ:*`. Aller-retour export → import **identique** (vérifié).
- **Vérifié en local** : app-admin, eho (base DE LATTRE), presse TV4, clé d'essai.
  - Le kit s'obtient en 2 s, avec 653 avatars (groupes visibles) en bio courte, soit 110 Ko ;
  - import d'un CSV « façon IA » avec erreurs volontaires ; 11 tests ; `tsc` et build OK.
  - ⚠ **app-admin n'a PAS de configuration ESLint** : le lint n'y vérifie rien.
- ⚠ Pousser `kit-ia` poussera aussi 2 commits anciens en attente (`5a5fbd1` déconnexion Keycloak, `5b6bf9f` champs d'item).

## 🔄 app-admin — préparer un scénario avec une IA : NOUVELLE ORIENTATION (2026-09-28, soir)

⭐ **Décision de l'utilisateur, après discussion avec Xavier** : on abandonne le « tout en un import / commande de génération ».
- Le traitant reçoit **deux fichiers .md** :
  1. la **cartographie des avatars** de l'EHO ;
  2. le **mode d'emploi du fichier xls d'import** (colonnes, médias présents, champs, règles) ;
- il donne lui-même le **contexte** à l'IA, puis importe le xls produit.
- **Proposition, non codée** : deux boutons dans app-admin (encart « Préparer avec une IA », page scénario), fichiers **générés au clic** depuis eho et la zone, donc toujours à jour.
- **À régler avant de coder** :
  - la taille de la cartographie (3 983 avatars avec bio = plusieurs Mo) → filtres « groupes visibles seulement » (les archivés tombent), groupes cochés, bio oui / courte / non ;
  - l'import ne lit pas encore `title`, `target` ni `fields` ;
  - le mode d'emploi et l'import doivent partager **une seule définition des colonnes** ;
  - une option « sans camp » pour d'autres exercices.
- **Précisions de l'utilisateur (même soir)** :
  - le traitant ne fait ce dépôt **qu'une fois**. Condition à expliquer : déposer les fichiers dans un espace permanent (Projet ChatGPT ou Claude, Gem Gemini, Agent Le Chat) ; les régénérer quand l'EHO change (date de génération en tête de fichier) ;
  - ⭐ **3ᵉ fichier retenu (proposé)** : « Guide de rédaction d'un scénario », qui contient :
    - les consignes à coller dans l'espace de l'IA ;
    - une fiche de contexte à remplir ;
    - une méthode en 3 temps : trame → lignes → auto-vérification ;
    - un exemple complet ;
    - une vérification avant import.

    Il est en grande partie fixe (nom de l'exercice et apps insérés au clic).
  - Dans app-admin : un encart « Kit IA » (3 fichiers, ou un .zip).
- **Xavier a donné les droits d'écriture sur app-admin** (à vérifier au premier push). ⏳ Offert : fabriquer à la main un exemple de chacun des deux .md (base DE LATTRE) pour un essai dans l'IA.

## ⏸️ app-admin — l'export de scénario pour une IA (EN PAUSE le 2026-09-28, en attente des droits d'écriture sur app-admin ; garder le contexte)

**Besoin utilisateur** : générer du contenu en masse (réseau social, presse…) en confiant l'export du scénario à une **IA gratuite en ligne**, avec la liste eho **et les biographies** (l'utilisateur l'accepte, test en .xlsx).
- **Constat du code** (`app-admin` `src/app/api/bff/scenarios/[id]/export|import`) : 10 colonnes seulement (`id, app, persona, message, delta, reply_to, likes, boosts, like_groups, boost_groups`). ⚠ `title`, `target` (rubrique) et `fields` (chapô, champs de maquette, annoncés par l'app dans `item_fields`) **ne passent ni à l'export ni à l'import**, alors que l'éditeur les gère. `delta` = minutes depuis le parent ou le début.
- **Solution retenue avec l'utilisateur** : un **export auto-documenté**, généré depuis l'état réel de la zone. Feuilles : `LISEZ-MOI (IA)` (mode d'emploi, règles MINERVE, prompt), `scenario` (+ titre, rubrique, champs de maquette, menus déroulants), `apps`, `avatars` (+ bios), `groupes`, `exemples`.
- ⭐ **Idée de l'utilisateur** : une **« commande de génération »** remplie DANS l'app avant d'exporter (effet recherché, camp, public, apps cochées, groupes d'avatars, volume et rythme, trame, langue, ton, contraintes). Elle s'écrit dans le fichier, le **filtre** (apps et avatars utiles) et **reste enregistrée** sur le scénario. L'utilisateur n'ouvre plus le fichier.
- Pistes : un import qui accepte aussi un **CSV ou un tableau collé**, avec un aperçu avant d'importer ; plus tard, pré-remplir la commande depuis un **incident MELMIL**.
- **Étape suivante proposée** : fabriquer un `.xlsx` d'exemple (zone DE LATTRE) pour le tester dans l'IA, avant de coder. ⚠ `app-admin` : pas de droits d'écriture (403), et 2 commits locaux non poussés.

## ⭐ MELMIL — l'ATELIER DE PRÉPARATION (« création d'exercice »), 2026-09-23

**Demande utilisateur** : que les traitants se servent de MELMIL pour **créer l'exercice**, GT après GT (GT1 events, GT2 storylines, GT3 incidents), en direct et en parallèle, avec un tableau type MELMIL qui se remplit tout seul — ⚠⚠ **distinct** de la planche JEMM (la vérité des joueurs), et resservant pendant l'exercice pour anticiper ce qu'il faudra ajouter dans JEMM.

**Décisions utilisateur** : tout le monde peut tout modifier, on voit **qui a touché à quoi** ; events (et parfois storylines) **confiés** à des traitants (l'exclusivité par utilisateur n'est pas exclue plus tard) · GT1 = création d'events seulement (pas de référentiel « ordres des chefs ») · **pas d'export JEMM** depuis l'atelier, mais une **vue des écarts** · accès = mêmes groupes d'animation · un **annuaire d'équipe** par cellule (chef, second, traitants).

**Livré** — `app-melmil`, branche `atelier-preparation`, commit `cc6d5b2`, version **`2026-09-23.3`** — ✅ **déployé le 2026-09-23 à 17:41** (`prod` = `cc6d5b2`) :
- Route **`/preparation`** (même sas de rôle que la planche) ; bandeau : bascule **« Création d'exercice » / « Planche JEMM »**.
- `src/lib/atelier/` **pur et testé** : `modele.ts` (Atelier v1 : events, storylines, incidents en **D+ + heure**, membres, journal 300 gestes, calendrier = jour de référence + D+ + **période de jeu**), `gestes.ts` (créer/modifier/supprimer/**recoder en cascade**/dupliquer, chacun pose la **trace** et journalise), `versPlanche.ts` (atelier → `Etat` : **le composant `Planche` existant dessine la planche de préparation**, phases/GELEX/couleurs empruntées à la planche JEMM), `ecarts.ts` (par **code** : prévu absent de JEMM / différent (date, sujet, storyline) / dans JEMM seulement), `importer.ts` (**verser** un export JEMM : **ajoute, ne remplace jamais**, exige le calendrier, pose la période de jeu).
- Serveur : **table `atelier` à part** (migration additive `20260923120000_atelier_preparation`, `planche` intacte), **même concurrence** que la planche (version attendue → 409 → rejeu), `/api/atelier` GET/PUT. **SSE : un canal par document** (`canal: "planche" | "atelier"`) — la planche JEMM ne se relit plus quand l'atelier change.
- Écran : parcours GT (repère, pas verrou ; « passer l'exercice ici » confirmé), onglets Events · Storylines · Incidents · Planche de préparation (**glisser = changer le D+**) · Écarts · Équipe (« C'est moi » rattache la fiche au compte) · Journal · Réglages. ⭐ **Les champs n'enregistrent qu'à la sortie** (pas à chaque frappe : sinon un conflit par lettre et par traitant), brouillon local préservé pendant la frappe.
- **Vérifié** : 139 tests (43 nouveaux) · essai **à deux navigateurs 16/16** (versement des 2 JEMM fictifs DELATTRE → 2/7/46 vus par l'autre poste, écritures simultanées qui survivent toutes deux, équipe, journal, passage GT, planche D+27→D+41, écarts = 1 seul incident retouché, planche JEMM intacte, rechargement) · **montée de base simulée** (planche v5 existante + nouvelle migration → intacte) · **image de production construite et lancée** : migrations appliquées, `healthy`, `/api/sante` = `2026-09-23.3`, **401 sans session** sur `/api/atelier`.
- ⚠ **Piège d'essai d'image sous Windows** : la copie de travail est en **CRLF** (`core.autocrlf=true`) → `exec ./docker-entrypoint.sh: no such file or directory`. Le dépôt est en LF, **le runner Linux n'est pas concerné**. Pour un essai local fidèle : `git -c core.autocrlf=false archive --format=tar HEAD | docker build -t … -` (⚠ `git archive` seul convertit AUSSI).
- ✅ **2026-09-24 — Grille EXCON cliquable** (commit `d55688d`, version `2026-09-24.1`, **local, non poussé**) : dans chaque storyline, le tableau « EXCON COORDINATION REQUIRED » du PPT GREY CELL (légende TO BE COORDINATED / COORDINATED à gauche, cases **OPFOR · LOG · NSE · HN · CAX · ILI**). Un clic fait tourner la case **blanc → jaune `#FFFF00` → vert `#92D050` → blanc** (couleurs relevées dans le PPT). Modèle : `coordination: Record<CelluleExcon, "" | "a-coordonner" | "coordonne">` ; l'ancien texte libre est relu (cellule citée → à coordonner) ; `versPlanche` en tire un texte (« OPFOR (à coordonner), HN (coordonnée) »). Geste pur `basculerCoordination` (tracé, journalisé, rejoué sur l'état frais en cas de conflit). 147 tests + essai à deux navigateurs OK. ⚠ Le PPT a quelques tableaux à cellules différentes (JLSG, LOCON, HICON, LOG / D2) : **la grille reste fixe aux 6 cellules demandées**. JEMM ne porte pas les couleurs → après versement, les cases sont blanches.
- ✅ **2026-09-24 — Comptes rendus PSYREP / CIMICREP sur les incidents** (commit `6f77eb6`, version `2026-09-24.2`, ✅ **en ligne le 2026-09-24 à 13:14**). Modèles = `EXER\DELATTRE 26\00_Boites à outils\APPENDICE 7_ PSYREP.FR.docx` et `APPENDICE 8_ CIMICREP.FR.docx`, copiés dans `app-melmil/public/modeles-cr/`. Décisions utilisateur : export **.docx** (le modèle d'origine rempli), **TLS cliquable** (vide→G→A→R→?, couleurs du modèle `00FF00/FFC000/FF0000`), **pré-remplissage** (GDH `DDHHMM{A|B}MMMYY` heure de Paris, nom d'exercice, n° msg = code incident), bouton **« Importer un CR (.docx) »** (modèle vierge rempli dans Word → nouveau CR ; type reconnu au titre du tableau ; rangées retrouvées par intitulé si le tableau a été retouché).
  - Architecture : `scripts/gabarits-cr.py` **génère** `src/lib/comptes-rendus/gabarits.ts` (cellules, fusions, fonds, hauteurs, runs, numérotation ; cases `r{rangée}c{rang}` genres `texte` / `sous` (on écrit sous l'intitulé, PSYREP) / `tls`) → **à relancer si un modèle change**. `docx.ts` (navigateur, `fflate` + DOMParser) remplit/relit le `word/document.xml` d'origine sans toucher au reste. `Atelier.comptesRendus[]` rattachés par **ID d'incident** (recoder ne détache pas), cascade à la suppression incident/storyline/event, gestes purs une-case-une-écriture.
  - PSYREP 21 cases, CIMICREP 167 (dont « Location CP », dans un tableau imbriqué ; pas de TLS sur DE/A/INFO/REF ; intertitres jaunes non remplissables sauf HNS QUESTIONS). 165 tests + essai navigateur 12/12 (création, cumul 1 CIMICREP + 2 PSYREP, export relu par python-docx et rendu LibreOffice identique au modèle, import de modèles remplis « à la Word », vu par un 2ᵉ poste).
- ✅ **2026-09-25 — ETIM des incidents** (commit `5b4d76a`, branche `etim-incidents`, version `2026-09-25.1`, ✅ **en ligne le 2026-09-25**) : `Atelier.etims` = la liste des ETIM de l'exercice (Réglages : ajouter / renommer / retirer, qui suivent sur les incidents) ; `IncidentAtelier.etims` = celles cochées dans la fiche (pastilles, avis DESIGNER n°7). Affichées sur la carte de la planche de préparation, dans la liste par jour, dans le tableau des incidents et sur la fiche. `Inject.etims?` est posé par `versPlanche` seulement, **jamais enregistré sur la planche JEMM**. Verser un JEMM reprend les acteurs `^ETIM` (`etimsDesRoles`). Relecture rétro-compatible (listes vides). 178 tests.
  - ⏳ **À FAIRE dès les premiers exports JEMM réels de DE LATTRE 26 (demande utilisateur)** : faire apparaître les ETIM sur la **planche JEMM** aussi. Piste : la planche JEMM garde déjà les acteurs JEMM dans `Inject.roles` (`ScenarioRoleList`, lu par `jemm.ts`) ; il suffirait d'en tirer les ETIM (`etimsDesRoles`) à l'affichage de la carte. ⚠ **Vérifier d'abord dans le vrai export** où JEMM porte l'ETIM (acteur, destinataire, émetteur, étiquette `TagList` ?) et sous quels libellés. Les fichiers actuels sont **fictifs**, faits par nous depuis le PPT.
- ✅ **2026-09-28 — Onglet ÉQUIPE refait** (commit `f9f72b6`, branche `equipe-organigramme`, version `2026-09-28.1`, ✅ **en ligne le 2026-09-28**, `main` = `prod`, `/api/sante` vérifié) :
  - modèle : `Atelier.groupes` (`GroupeEquipe` : nom, couleur, parent, rôle), `Membre.grade` et `Membre.compteId`. ⚠ Les personnes et les events citent leur groupe **par son NOM** (`cellule`), comme avant : une cellule citée sans fiche est un **groupe implicite** (id `nom:<NOM>`). Le modifier le rend explicite ;
  - `lib/atelier/equipe.ts` (pur, testé) : renommer suit sur les personnes et les events, un parent circulaire est refusé, supprimer fait remonter les sous-groupes et garde les personnes sans groupe ;
  - écran `components/atelier/equipe.tsx` : vue **Araignée** (2 couronnes, hauteur ajustée au contenu) et vue **Liste** (d'office au téléphone), fiches groupe et personne dans le panneau de droite. Avis DESIGNER n°10 ;
  - **comptes Pléiade de la zone** : `/api/zone/comptes` → route de service de Pléiade `/api/internal/zones/:zone/users` (sans mot de passe, même source que LEAC) ;
  - relecture : un grade saisi dans le nom (« CNE Julie MARTIN ») est séparé (`separerGrade`) ;
  - ⚠ **Abréviations de grade (correction utilisateur)** : sergent-chef = **SCH**, jamais « SGC ». `gradeReglementaire` relit les anciens « SGC » en SCH (commit `018f5dc`, `2026-09-28.2`, ✅ en ligne le 2026-09-28).
  - 192 tests ; essai local ordinateur et téléphone, 0 erreur, 0 débordement.
  - ⚠ Tout utilisateur de MELMIL a le rôle `admin` : « seul un admin crée des groupes » est donc vrai d'office. Un rôle plus fin reste à créer si besoin.
- ✅ **2026-09-28 (après-midi) — Équipe v2 : ORGANIGRAMME + liens transverses** (commit `84294f7`, branche `equipe-organigramme-v2`, `2026-09-28.3`, ✅ **en ligne le 2026-09-28**) : l'araignée est **remplacée**, car elle ne montrait que 2 niveaux et l'exercice au centre trompait. L'exercice devient le **cadre**. Les groupes sont en colonnes et les sous-groupes emboîtés à toute profondeur ; les traits sont tracés d'après la position réelle des cartes (calque SVG). Nouveau champ **`GroupeEquipe.liens`** (« travaille aussi avec ») : stocké d'un côté, lu des deux (`reliesA`, `liensTransverses`, `relierGroupes`), dessiné en pointillé ET écrit « ↔ X » dans les cartes. Avis DESIGNER n°11. ⚠ **Les noms réels saisis par l'utilisateur sont confidentiels : ne pas les lire** ; essais sur des données fictives uniquement.
- ✅ **2026-09-28 (soir) — Organigramme : placement selon les liens** (commit `04b3a15`, branche `equipe-placement`, `2026-09-28.4`, ✅ **en ligne le 2026-09-28**) : `ordonnerOrganigramme` (pur, testé, déterministe) forme une chaîne de colonnes par famille de groupes reliés ; dans un groupe, le sous-groupe relié est placé du côté de son partenaire. Les cartes n'écrivent plus « Aucune personne ». Avis DESIGNER n°12. Piste : un ordre manuel qui primerait.
- ✅ **2026-09-28 (soir) — « Confié à » par GROUPES** (commit `a65d6f2`, branche `confie-par-groupes`, `2026-09-28.5`, ✅ **en ligne le 2026-09-28**) — ⭐ **règle de l'utilisateur** : l'**event** est confié à un groupe de premier niveau (`EventAtelier.groupes`), la **storyline** à un sous-groupe du groupe de son event (`StorylineAtelier.groupes`), l'**incident** à des personnes de ce sous-groupe (`IncidentAtelier.confieA`). **Liste vide = tout le sous-groupe gère l'incident.** Logique pure dans `equipe.ts` (`choixPour*`, `gestionnairesDeLIncident`, `confieA`). L'ancien `responsables` (par personnes) est gardé et affiché avec « Effacer ». Avis DESIGNER n°13. 216 tests.
- ✅ **2026-09-28 (soir) — Event : « Cellule » = la sélection des groupes** (commit `1e2adf8`, branche `cellule-groupes`, `2026-09-28.6`, ✅ **en ligne le 2026-09-28**) — ⭐ **décision utilisateur** : fusion de la « Cellule » (texte libre) et du « Confié à (groupe) », une seule rubrique « Cellule » à pastilles, parce que c'est plus parlant. `celluleDeLEvent` affiche les groupes cochés, sinon l'ancien texte (planche, en-têtes) ; le texte libre ne crée plus de groupe fantôme ; à l'import JEMM, le groupe du même nom que l'event est coché d'office. Storylines et incidents inchangés. 220 tests.
- ⛔ **2026-10-01 — « CONFIÉ À » SUPPRIMÉ** (décision de l'utilisateur ; les deux entrées ci-dessus sont **caduques**). Commits `c44ffbc` + `4a1af66`, branche `retrait-confie-a`, `2026-10-01.9`, ✅ **en ligne le 2026-10-01 à 16h31**.
  - Ce qui disparaît :
    - **Event** : plus de « Cellule » ;
    - **Storyline** : plus de « Confiée à » ;
    - **Incident** : plus de « Confié à », ni dans la fiche ni en colonne du tableau ;
    - **Équipe** : plus de rubriques « Confié » (fiche personne) ni « Events portés » (fiche groupe) ;
    - l'import JEMM ne coche plus de groupe ;
    - la planche ne reçoit plus de cellule venue de l'atelier.
  - **Nommage** : la cellule (GYC / FOR) n'est plus déduite de l'event. On prend celle de la demande, sinon celle de la personne (Équipe), sinon on la choisit à l'export.
  - ⭐ **CONSERVÉS, car essentiels pour l'utilisateur** : les **« ETIM concernées »** et le système de **comptes rendus** (un compte rendu par ETIM, par jour et par type).
  - Les anciennes données (`groupes`, `confieA`, `responsables`) restent relues et conservées, mais sont sans effet.
  - **Ne pas réintroduire** une attribution sans demande explicite.
- ⛔🔒 **2026-10-01 — ANONYMAT DES COMPTES dans MELMIL** (décision de l'utilisateur pour la sécurité, option A « couper le lien » ; commit `be43962`, branche `anonymat-comptes`, `2026-10-01.10`, ✅ **en ligne le 2026-10-01 à 18h00**).
  - **Règle durable** : **aucun lien entre un compte de la zone (gc01…) et une personne (grade et nom) ne doit être stocké ni affiché dans MELMIL**, ni dans l'Équipe, ni dans les demandes, ni ailleurs. Les comptes ont été anonymisés exprès.
  - **Équipe** : plus de rattachement de compte, ni « C'est moi », ni liste des comptes de la zone. Les noms, grades et groupes restent.
  - **Demandes de produit** : le demandeur (grade et nom) est **choisi à l'envoi**, dans la liste de l'Équipe ou en saisie libre. Ce choix est mémorisé **dans le navigateur seulement** (`localStorage` `melmil_demandeur`). La demande garde le nom et la cellule, **jamais le compte**.
  - **Cellule d'un compte, sans nom** : `Atelier.cellulesDesComptes` associe le `sub` Keycloak à GREYCELL ou FORAD. Elle est apprise à l'envoi d'une demande et au choix de la cellule au nommage, et sert au nommage des fichiers et au signal.
  - **Signal** : « les demandes de **votre cellule** ont avancé », et non plus « vos demandes ».
  - **Purge** : `contientLiensComptes`. La relecture efface `compte` et `compteId` des fiches et des demandes, et `lireAtelier` réécrit la base aussitôt, avec `majPar` « purge anonymat des comptes ». Tout le reste est conservé (tests « anonymat »).
  - **Limites dites à l'utilisateur** : les traces « créé par gc01 » restent, mais sans nom réel ; un utilisateur connecté voit qui a fait une demande si le nom est saisi dedans.
- ✅ **2026-10-01 — Comptes rendus : supprimer, et plusieurs exemplaires** (`507164c`, `2026-10-01.12`, en ligne à 18h26).
  - Plusieurs exemplaires d'un même type, pour la même ETIM et le même jour, sont possibles avec « +1 » pour PSYREP, CIMICREP et SCAMR. Ils sont numérotés n°1, n°2…
  - « .docx (n) » produit **un seul fichier Word, un exemplaire par page** (`exporterDocxPlusieurs`). Choix de l'utilisateur : du Word et non du PDF ; le PDF se fait depuis Word.
  - Un compte rendu se supprime depuis sa fiche, avec une confirmation qui cite les incidents qui le partagent.
- ✅ **2026-10-02 — Navigation de MELMIL** (`b3b74af`, `2026-10-02.2`, en ligne à 08h45).
  - **L'accueil ouvre la planification**, et la planification ouvre **toujours la planche de préparation**, qui est la vue de travail principale.
  - La planche JEMM est à `/jemm`, à un clic dans le sélecteur.
  - Tout onglet s'ouvre par lien direct `/preparation?onglet=…` (`planche`, `gt1`, `gt2`, `gt3`, `ecarts`, `demandes`, `equipe`, `journal`, `reglages`).
- ✅ **2026-10-02 — Pièces jointes d'un incident = fichiers + comptes rendus** (`189f4a3`).
  - La colonne du tableau des incidents (en-tête agrafe) et l'agrafe en bas à droite des cartes de la planche comptent les deux. Calcul unique : `piecesDeLIncident`.
- ✅ **2026-10-01 — Alignement JEMM sans perte** (`d9d5187`, `2026-10-01.13`, en ligne à 18h55).
  - **Sauvegarde et restauration** de l'atelier dans Réglages (JSON `melmil-sauvegarde-atelier`). C'est le seul retour en arrière : à faire **avant** chaque alignement.
  - Option « garder le jour et l'heure de MELMIL » (par défaut JEMM fait foi) ; le bilan liste les dates qui changent ; les suppressions s'affichent en alerte.
  - **Pièces jointes de l'export** : on choisit le dossier ; chaque pièce va à l'incident du même code si elle n'y est pas déjà, sous un **nom conforme**, avec le NMR inséré, car le serveur impose la règle de nommage.
  - Ce que JEMM remplace : sujet, description, effet attendu, émetteur, moyen, destinataires, date ; récit, nom et période de storyline ; description d'event. Ce qui reste à MELMIL : effets attendus, QUI / OÙ, coordination et objectifs secondaires de storyline ; ETIM, statut, comptes rendus et pièces jointes des incidents.
- ✅ **2026-10-01 — Liste des incidents : colonne « Destinataire »** (les ETIM cochées, sorties de la colonne « Sujet » ; `d6c1fe3`, en ligne à 18h09).
- ⏳ Limites connues : pas de rôle lecture seule ; pas d'exclusivité d'écriture par traitant ; le journal ne garde que 300 gestes ; les storylines versées depuis JEMM n'ont ni effets attendus ni coordination séparés (JEMM les mêle au récit).
