# Plan — app `app-ia` : le moteur des avatars IA, une instance par zone

> ✅ **Réponses de l'utilisateur (2026-10-11, ~17 h 20)** : (1) le serveur peut joindre le PC (nœud de calcul via VPN) ; (2) nom **`app-ia`**, avec un **dépôt GitHub propre** dans l'organisation, branches **`main`** et **`prod`** comme les autres apps ; (3) **base dédiée** (journal, cycles, réglages, bail ; eho garde fiches, état et interrupteur) ; (4) rôles : **l'Administration** dans un premier temps ; (5) **une seule instance par zone** (sinon doubles lectures, doubles réponses, états écrasés) : interdiction par l'orchestrateur + bail en base ; (6) **mode « validation humaine » supprimé** ; l'interrupteur garde **une seule valeur de référence dans eho**, avec **un bouton dans les deux apps** (celui d'app-ia écrit dans eho) ; écran d'app-ia conçu avec **DESIGNER**.

*Préparé le 2026-10-11 par PLEIADE, sur décision de Xavier : la configuration des avatars reste dans eho, le moteur devient une app dédiée par zone, « presque une extension de l'admin ». À relire par l'utilisateur, puis par Xavier et CYBERSECU, avant tout code. Réalisation et tests d'abord en local.*

## 1. Répartition, arborescence, stack

| Où | Quoi |
|---|---|
| **app-ia** | Le moteur (boucle, psychologie, appels au modèle, contrôles de texte, publication), ses réglages d'exercice (coefficient de crise, campagnes, contexte fictif), son journal, l'historique des cycles, un écran de pilotage, `/api/sante` |
| **eho** (inchangé, en prod) | Fiches de comportement, état de chaque avatar (`etat-ia`), **interrupteur**, témoin du moteur, page Population IA |
| **Social** (inchangé, en prod) | Publication (`/api/service/publish`, `like`, `chat`, marquée « IA ») et lecture (`/api/service/retex`) |

**Arborescence :**
- `Dockerfile`, `docker-entrypoint.sh`, `prisma/schema.prisma`, `src/instrumentation.ts`
- `src/lib/` : `auth`, `kc-token`, `session`, `deconnexion`, `db`, `discovery` (copiés de app-admin) ; `zone.ts`
- `src/moteur/` : `esprit.mjs` (ex-moteur.mjs) ; `boucle`, `cycle`, `population`, `interrupteur`, `social`, `reglages`, `journal` (ex-pont.mjs découpé)
- `src/app/` : `page.tsx`, `journal/`, `reglages/`, `api/sante`, `api/bff/*`
- `scripts/test-*.mts`

**Stack : la même que app-admin** (Next 16, Auth.js + Keycloak, Prisma 7 + MariaDB, image node:22-alpine). Raisons :
- l'authentification et les gardes de l'admin sont éprouvées ;
- `instrumentation.ts` sait déjà démarrer une boucle dans le serveur ;
- la découverte des apps voisines est réutilisable ;
- le Dockerfile est rodé ;
- la maintenance est la même que l'admin.

Le moteur reste en JavaScript (environ 1 000 lignes portées telles quelles, sans réécriture en TypeScript à ce stade).

## 2. Portage du moteur

**Ce qui se garde tel quel :**
- la psychologie (`Esprit`), les appels au modèle, l'extraction des faits, les contrôles et reformulations ;
- les voix de cohorte et les campagnes ;
- la logique du cycle, les plafonds × crise, l'anti-tic, l'anti-chœur, la sélection des lecteurs.

**Ce qui change :**

| Prototype | app-ia |
|---|---|
| `zone.mjs` / `zones.json`, clé lue par `docker inspect` | Variables injectées par l'orchestrateur (`PLEIADE_URL/ZONE/API_KEY`) ; eho et Social trouvés par découverte |
| `etat.json` (propositions, journal) | Tables `Journal`, `Cycle`, `Reglage` |
| `crise.json`, `campagnes.json`, `contexte.md` | Réglages en base, relus à chaque cycle, avec qui/quand |
| Mémoire de secours en fichiers | eho seulement |
| Options de ligne de commande | Variables : `IA_GROUPE`, `OLLAMA_URL`, `OLLAMA_MODELE`, `CYCLE_PAUSE_S` (90) |
| Page localhost:3875 | Écran de l'app |

**Boucle :** démarrée au lancement du serveur (sauf `IA_MOTEUR=off`). Un cycle se termine, il est enregistré, puis le suivant part **90 s après la fin** (`setTimeout` enchaîné, jamais `setInterval`).

**Interrupteur (dans eho) :** lu toutes les 15 s, au début de chaque cycle, avant chaque avatar et juste avant chaque action. S'il est coupé ou si eho ne répond pas, le moteur se tait et annule ce qu'il avait programmé.

**Jamais deux moteurs à la fois :** un drapeau en mémoire, plus un **bail en base** (3 min, renouvelé chaque minute), pour qu'un ancien et un nouveau conteneur ne publient pas ensemble pendant un redéploiement.

**Arrêt propre :** les minuteurs sont arrêtés, l'état de chaque avatar est écrit dans eho, le bail est libéré.

## 3. Écran de l'app (rôles vérifiés côté serveur)

- **Tableau de bord :**
  - état du moteur : en cycle, en pause jusqu'à…, en attente de l'interrupteur, nœud de calcul injoignable ;
  - dernier cycle : durée, actions, erreurs, avec la moyenne des derniers ;
  - nombre d'avatars animés ;
  - interrupteur en lecture seule, avec un lien vers Population IA dans eho.
- **Journal :** cycles et actions par avatar (action, cible, raison, texte, alertes), filtrable.
- **Réglages :** coefficient de crise, campagnes (# → axes et poids), contexte de l'exercice ; chaque changement est journalisé.
- **Ce qui n'y est PAS :** l'interrupteur et les fiches (eho), les clés et adresses internes, un bouton « lancer un cycle maintenant » (sauf demande de Xavier).

## 4. Entrée du catalogue `catalog/ia.yml`

- **Identité :** `name: ia`, `fonction: animation`, `port: 3000`.
- **Santé :** `/api/sante` répond 200 si le serveur et la base vont bien. Le nœud de calcul ou eho absents donnent un état « dégradé », pas une panne, pour éviter que le conteneur redémarre en boucle.
- **Keycloak :** client confidentiel `ia`.
- **Rôles :** `admin` pour les réglages, `animateur` pour la lecture du journal.
- **Base :** une base MariaDB dédiée.
- **Variables :** `OLLAMA_URL` (en local : `http://host.docker.internal:11434`), `OLLAMA_MODELE`, `IA_GROUPE`, `CYCLE_PAUSE_S`, `OLLAMA_TIMEOUT_MS`, `IA_MOTEUR`, `APP_VERSION`.
- ⚠ **Point d'attention :** l'orchestrateur n'ajoute l'accès à `host.docker.internal` que dans certains cas (`zone-manager.ts`, ligne 656 environ). Il faudra un `extraHosts` déclaratif dans le catalogue, ou un vrai nom de nœud de calcul.

## 5. Réalisation en local (zone `ia-locale`), environ 5 à 6 jours

| Lot | Durée | Contenu |
|---|---|---|
| **L0 – squelette** | ½ j | base app-admin, schéma, `/api/sante`, `ia.yml`, déploiement par l'orchestrateur local, connexion et refus sans rôle |
| **L1 – portage du moteur** | 2 j | voir les tests ci-dessous |
| **L2 – écran** | 1 j | tableau de bord, journal, réglages ; matrice des droits testée ; aucune clé dans les réponses |
| **L3 – intégration `ia-locale`** | 1 j | voir les vérifications ci-dessous |
| **L4 – durcissement** | ½ à 1 j | délais d'attente du modèle, nœud de calcul en panne (le cycle échoue proprement, reprise au suivant), purge du journal, notes de version, revue CYBERSECU, présentation à Xavier avant de pousser |

**Tests du lot L1 :**
- cadence : fin + 90 s, même avec un cycle de 7 min, jamais deux cycles à la fois ;
- interrupteur et annulation en moins de 15 s ;
- double démarrage ;
- arrêt propre.

**Vérifications du lot L3 :**
- Ollama de ce PC joint par l'app ;
- le prototype est coupé ;
- témoin, interrupteur, rechargement des fiches, coefficient de crise ;
- 2e instance dans `tuto-locale` : chaque moteur ne voit que sa zone ;
- redéploiement en cours de cycle sans double publication.

## 6. Questions pour Xavier
1. **Nœud de calcul en production :** ce PC (RTX 5070 Ti) via le VPN, ou un serveur à carte graphique ? Qui garantit sa disponibilité ? Faut-il HTTPS ou une authentification devant Ollama, qui n'en a pas ? Faut-il un `extraHosts` dans le catalogue ?
2. **Nom :** `ia`, `avatars-ia` ? Le dépôt s'appelle-t-il `app-ia` ?
3. **Base :** une base dédiée par instance (recommandé), ou tout dans eho ?
4. **Rôles :** `admin` / `animateur`, ou ceux de l'admin ? Qui règle le coefficient de crise ?
5. **Image et versions :** comme les autres apps ?
6. **Une instance par zone :** l'orchestrateur peut-il l'imposer, ou le bail en base suffit-il ?
7. **Mode « validation humaine »** (propositions validées avant publication) : le garder dans l'écran, ou moteur seulement autonome ?
8. **Population :** `IA_GROUPE` par instance, ou toute la population IA de la zone ?

## 7. Présentation à Xavier (état au 2026-10-11 soir, lots L1 à L4 faits en local)
**Ce qui est prêt :** app-ia 2026-10-12.2 (`main` poussé jusqu'à L3 ; L4, l'export d'analyse, la pensée / relecture hybride et la mémoire longue à pousser), eho 2026-10-12.1 (branche `ia-avatars`, non poussée), entrée de catalogue `ia.yml` (branche locale de `pleiade-platform`). Une instance par zone, base dédiée, Administration seulement, cycle suivant 90 s après la fin du précédent, clé de zone injectée par l'orchestrateur, interrupteur dans eho et dans l'app, revue CYBERSECU corrigée. **Analyse et correction sans clé sur le poste** : export pour analyse complet dans le Moteur IA, export / import vérifié des fiches dans eho.

**Décisions à lui demander :**
1. **Nœud de calcul en production** (recommandation CYBERSECU) : Ollama sur ce PC écoute sur 127.0.0.1 seulement ; un proxy TLS (certificat de la CA de zone) l'expose sur l'IP VPN avec un **jeton dédié** (`OLLAMA_CLE`) ; liste blanche `/api/chat` et `/api/tags` ; pare-feu Windows limité à l'IP VPN du serveur. Variante : le PC **tire** le travail depuis le serveur (aucun port ouvert chez nous). Disponibilité : moteur en « nœud injoignable » si le PC dort, sans rien publier.
2. **Entrée `ia` au catalogue du serveur** et variables : `OLLAMA_URL`, `OLLAMA_MODELE`, `IA_GROUPE`, `CYCLE_PAUSE_S`, `IA_T0`.
3. **Clé dédiée `PLEIADE_IA_KEY`** (recommandée par CYBERSECU) : injectée dans eho et le social seulement, liste blanche des routes IA, « au nom de » borné à CAMP IA. Évite qu'une fuite de la clé ouvre toute la zone.
4. **Nœud de calcul, mémoire** : le moteur appelle aussi Ollama pour **bge-m3** (vecteurs de sens, sur le processeur) — le proxy du point 1 doit laisser passer `/api/embed`. Le PC du projet a une carte de **12 Go** (Gemma 26B en occupe ~9) : un serveur à carte plus grande permettrait un modèle plus gros.
5. **Ordre de mise en ligne proposé** : catalogue → eho 2026-10-12.1 → app-ia `prod` → installation de la population dans DELATTRE 26 (interrupteur coupé) → premier essai surveillé.
