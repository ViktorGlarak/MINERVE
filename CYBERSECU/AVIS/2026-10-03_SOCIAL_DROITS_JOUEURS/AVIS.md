# AVIS CYBERSECU — Droits d'écriture des JOUEURS sur le réseau social (app-social)

- **Date** : 2026-10-03 (préparé le 2026-10-02)
- **Demande** : décision utilisateur du 2026-10-03 — les joueurs (comptes Keycloak de zone sans rôle ANIMATEUR, ex. groupe DIV1) peuvent (1) suivre / ne plus suivre avatars et hashtags, marquer leurs notifications lues ; (2) publier au nom des avatars de leur camp (groupe eho « CAMP DIV1 », 7 avatars).
- **Code lu** (état `app-social` `13f1776`, eho local) : `apps/api/src/auth.ts`, `garde-ecriture.ts`, `audit.ts`, `upload.ts`, `index.ts`, `social/{posts,users,hashtags,notifications,link-preview}.ts` ; `eho/src/lib/impersonation.ts`, `eho/src/app/api/impersonation/route.ts`.
- **Statut** : CONSEIL. Rien n'est modifié ni poussé. Mise en œuvre : PLEIADE / ARCHITECTE, règle « tester en local avant de pousser ».
- **Doctrine** : REF-03 (zero trust : moindre privilège, refus par défaut, décision à chaque accès), REF-11 (R6/R10 contenus téléversés, R13-R18 en-têtes), REF-01 M11 (secrets), règles §4 « les règles s'appliquent côté serveur » et « au nom de : refus si un maillon manque ».

## Verdict

**Les règles proposées sont VALIDÉES sur le fond**, avec **7 corrections** (R2, R4, R5, R6, R7, R8, R9) et **4 préalables bloquants** (R10 à R13). Ces préalables sont des failles **aujourd'hui sans gravité**, parce que seuls des animateurs de confiance écrivent. Elles deviennent exploitables dès qu'un joueur écrit.

## Règles

**R1 — ANIMATEUR inchangé.** Validé. eho décide (`avatarIds` = camp + « autres comptes », ou `master`).

**R2 — Le garde d'écriture devient une LISTE BLANCHE par route (refus par défaut).** On ne retire pas des interdits à un joueur : on lui accorde des routes précises. C'est l'esprit de `garde-ecriture.ts` (« la quinzième route ne peut pas être oubliée ») : une route ajoutée demain reste fermée aux joueurs.
- **Joueur, sans `X-Act-As`** : `POST /users/:u/follow`, `POST /hashtags/:t/follow`, `PATCH /notifications/:id/read`, `POST /notifications/read-all`. Rien d'autre.
- **Joueur avec un `X-Act-As` valide (R3)** : les routes ci-dessus, plus `POST /posts` (sans `scheduled_at`), `POST /posts/:id/like`, `POST /posts/:id/boost` et `POST /posts/:id/comments`. `POST /posts/preview-link` seulement après R11.
- **Toujours refusés** : `PATCH`/`DELETE` des posts et commentaires (v1, voir R6), `turbo-boost`, `/api/admin/*`, `/api/zone`, `/api/service`, tout le reste.

**R3 — « Au nom de » pour un joueur = groupes de SON camp uniquement.** Validé, avec trois précisions.
- eho renvoie un champ séparé **`avatarIdsCamp`** (union des groupes liés aux camps du joueur, **sans** les « autres comptes »). `avatarIds` reste inchangé pour la messagerie et les animateurs.
- **Fail closed sur l'absence du champ.** Pour un non-animateur, un `avatarIdsCamp` absent (eho pas encore à jour) vaut une liste vide : surtout **ne jamais retomber sur `avatarIds`**, sinon un joueur incarnerait d'un coup ≈ 3 400 comptes. Ordre de déploiement : eho d'abord, social ensuite.
- **`master` est ignoré pour un non-animateur.** Un organisateur qui joue prend le rôle ANIMATEUR. C'est plus strict que « sauf masteradmin » : un seul chemin donne tous les avatars.

**R4 — Valider `X-Act-As` strictement.** Il doit correspondre à `^\d+$`, sinon 400. Aujourd'hui `Number("abc")` donne `NaN` puis une exception Prisma, rattrapée en 401 : le refus tient, mais par accident. La décision se prend **à chaque requête** (lecture comprise, via `optionalAuth`), jamais d'après ce que le client affiche. Le filtre `?impersonables=1` de `users/search` doit utiliser `avatarIdsCamp` pour un joueur, mais il reste cosmétique. `impersonateMiddleware` n'est pas utilisé : le supprimer.

**R5 — Messages programmés (correction de E8).** L'exception « auteur » de E8 compare `post.userId` à `req.userId`. Sous `X-Act-As`, `req.userId` désigne **l'avatar** : un joueur qui incarne un avatar de son camp verrait donc les injects que l'animation y a programmés. Le trou passe par `GET /posts/scheduled`, la page profil et `GET /posts/:id`. Corrections :
- l'exception « auteur » ne vaut **que pour un ANIMATEUR** ;
- `scheduled_at` est **refusé** (403) dans une écriture de joueur ;
- `GET /posts/scheduled` est **réservé aux ANIMATEURS**.

**R6 — « Supprimer ou modifier ce que l'avatar incarné a publié » : NON en v1.** Le contenu d'un avatar partagé ne porte pas trace de qui l'a écrit. Un joueur pourrait donc effacer ou réécrire un inject publié par l'animation sur ce même avatar, ou le message d'un autre joueur. En v2, ajouter `operatorId` aux posts et commentaires, et n'autoriser `PATCH`/`DELETE` que si `operatorId` désigne le joueur appelant. Même logique pour les bascules like/boost : elles peuvent annuler un like posé par l'animation. C'est acceptable (effet mineur, journalisé), mais il faut le savoir.

**R7 — Profil : `PATCH /api/auth/profile` est HORS du garde** (monté sur `/api/auth`, pas sur `/api/social`).
- **Aujourd'hui déjà**, un joueur peut renommer son propre compte et lui donner le nom et la photo d'un ministre fictif. Avec les abonnements, ce compte devient visible (listes d'abonnés).
- **Demain**, un joueur qui incarne un avatar pourrait changer son nom, sa bio et son portrait : c'est l'usurpation de l'avatar.

Correction : route réservée à l'ANIMATEUR. L'identité des avatars appartient à eho.

**R8 — Visibilité des abonnements des joueurs : risque réel, à traiter.** Aujourd'hui, `GET /users/:u/followers` et `/following` sont publics, sans authentification. Trois conséquences :
- le camp adverse voit **quels comptes surveillent quels avatars** (contre-renseignement, en contradiction avec la mission « repérer les bonnes sources ») ;
- les comptes d'opérateurs gonflent l'audience des avatars et faussent la mesure de leur portée ;
- le nom affiché vient de la claim Keycloak `name` : il peut contenir un nom réel, contre la règle d'anonymat des comptes du 2026-09-29 / 2026-10-01.

Correction : marquer à l'authentification Keycloak les comptes d'**opérateurs** (joueur ou animateur), par opposition aux avatars venus d'eho. Les exclure des listes publiques (abonnés, abonnements, retweeteurs) et des compteurs. Ils restent visibles d'eux-mêmes et de l'ANIMATEUR. Corollaire : un abonnement pris **au nom d'un avatar** est, lui, public et visible de l'adversaire. Le joueur doit le savoir ; par défaut, il suit avec son propre compte.

**R9 — Journalisation de l'opérateur réel.** `audit.ts` enregistre déjà `operatorId` et `avatarId`, mais seulement quand la route renseigne `res.locals.audit`. Trois écritures n'y passent pas : `hashtags/:t/follow`, `notifications/*` et `auth/profile`. Il faut l'ajouter. Le journal ne relie que gw01, l'IP VPN et l'agent utilisateur, sans nom : c'est conforme à la règle d'anonymat, et cela doit le rester. L'échec d'écriture du journal n'est que consigné ; c'est acceptable.

## Préalables BLOQUANTS (avant d'ouvrir l'écriture aux joueurs)

**R10 — E2 d'abord : jetons locaux.** Un jeton HS256 signé avec le secret par défaut `social-dev-secret` passe **avant** Keycloak. Quand le secret par défaut est en place, n'importe qui forge `roles:["ANIMATEUR"]` et agit au nom de n'importe quel avatar, **sans contrôle de camp**. Ouvrir l'écriture fait venir des joueurs actifs et curieux sur cette API. Correction : supprimer ce chemin (le login local renvoie déjà 410), ou imposer un `JWT_SECRET` `{auto}`. Validé : il ne doit en aucun cas être élargi aux joueurs.

**R11 — SSRF de l'aperçu de lien.** `link-preview.ts` suit toute URL, redirections comprises, **sans aucun filtre d'hôte ni d'IP**. Le déclenchement est automatique (`processLinkPreview`) à chaque post qui contient une URL, et aussi via `POST /posts/preview-link`. Un joueur pourrait faire interroger par le serveur les services internes de la zone (eho, Keycloak, conteneurs, `169.254.x`). Le titre et la description de la page visée seraient ensuite affichés dans le fil. Correction :
- résoudre le DNS, puis refuser les adresses loopback, privées, link-local et les noms de conteneurs ;
- revérifier à chaque redirection, ou désactiver les redirections ;
- à défaut, n'accepter qu'une liste blanche des domaines d'exercice.

**R12 — XSS stockée par téléversement (social, analogue à M3).** `upload.ts` se fie au type MIME déclaré par le client (`image/*`, qui accepte donc `image/svg+xml`). L'extension est reprise de `originalname` : un fichier `x.html` déclaré `image/png` est accepté. `express.static("/api/uploads")` le sert ensuite **sur l'origine du réseau social**. Un joueur pourrait piéger un animateur qui ouvre le média, voler son jeton et agir au nom de n'importe quel avatar : c'est une élévation complète. Correction :
- vérifier les octets magiques, refuser le SVG, imposer l'extension d'après le type réel ;
- servir les médias avec `X-Content-Type-Options: nosniff` et `Content-Security-Policy: sandbox` (ou `Content-Disposition` pour les types non affichables).

**R13 — Limites de débit par opérateur.** Il faut des quotas, par exemple 10 posts, 60 likes ou boosts et 60 abonnements par minute et par `operatorId`, avec réponse 429. Sans eux, un script muni d'un jeton de joueur reproduit le turbo-boost à la main (fermes de likes) ou noie le fil. Revoir aussi la limite de corps JSON (100 Mo, risque faible de §5).

## Points d'attention (non bloquants)

- **Cache de décision de 10 s.** Acceptable : une révocation de groupe prend effet en ≤ 10 s, puisqu'eho résout les groupes en direct auprès de Pléiade. Le retrait du rôle ANIMATEUR, lui, suit la durée de vie du jeton d'accès (≈ 5 min). Deux corrections : purger la `Map` (elle croît sans limite) et ne pas mettre en cache plus de 2 s une décision `ok:false` due à une panne, pour qu'un retour d'eho soit pris en compte vite.
- **Groupes = camps par leur nom.** Tout groupe Keycloak du joueur lié dans eho compte comme un camp. Vérifier que **DIV1 n'est lié qu'à « CAMP DIV1 »**, et que l'animation ne programme pas d'injects sur ces 7 avatars, sinon R5 et R6 deviennent critiques.
- **Avatar partagé** entre plusieurs joueurs du camp : les notifications marquées lues par l'un le sont pour tous, et chacun voit ce que les autres publient. C'est un comportement attendu, à expliquer aux joueurs.
- **Lecture anonyme (REQUIRE_AUTH).** Recommandation : la **fermer** (`REQUIRE_AUTH=true`) dès que tous les lecteurs légitimes ont un compte de zone. C'est le principe zero trust « chaque accès est authentifié » (REF-03). Aujourd'hui, tout porteur d'un profil VPN, y compris les profils d'exercice non révoqués (§7), lit les injects et les listes d'abonnés. Trois réserves :
  - l'API cockpit passe par la clé de service, hors `/api/social` : non concernée ;
  - `/api/uploads` resterait public (accès statique) ;
  - vérifier que le front gère la redirection vers la connexion.

  La décision revient à l'utilisateur.

## Tests à faire en LOCAL avant tout push (image démarrée, base, Keycloak et eho locaux)

Comptes de test : `anim` (ANIMATEUR), `j1` (groupe DIV1, sans rôle), `j2` (autre camp), anonyme. Avatars de test : A (CAMP DIV1), B (autre groupe réservé), C (« autres comptes »).

| # | Cas | Attendu |
|---|---|---|
| T1 | j1 suit puis ne suit plus un avatar et un hashtag (sans `X-Act-As`) | 200 / 200 ; journal avec `operatorId=j1` |
| T2 | j1 marque une notification lue, puis toutes | 200 ; seulement les siennes |
| T3 | j1 publie **sans** `X-Act-As` | 403 |
| T4 | j1 publie, aime, partage, commente au nom de A | 201/200 ; `avatarId=A`, `operatorId=j1` |
| T5 | j1 au nom de **B** et au nom de **C** | 403 / 403 (C : la preuve que les « autres comptes » sont exclus) |
| T6 | `X-Act-As: abc`, `1e3`, `-1`, vide | 400 (ou 403), jamais 500 ni 401 accidentel |
| T7 | eho arrêté, puis eho sans le champ `avatarIdsCamp` | j1 au nom de A refusé dans les deux cas ; anim inchangé |
| T8 | j1 au nom de A : `scheduled_at`, `GET /posts/scheduled`, profil A et `GET /posts/:id` d'un post programmé par anim sur A | 403 / 403 / programmé invisible / 404 |
| T9 | j1 au nom de A : `PATCH`/`DELETE` d'un post de A publié par anim, `turbo-boost`, `/api/admin/groups` | 403 partout |
| T10 | j1 : `PATCH /api/auth/profile`, avec et sans `X-Act-As: A` | 403 |
| T11 | Retrait de j1 du groupe DIV1 dans Keycloak | refus en ≤ 10 s, sans reconnexion |
| T12 | Jeton HS256 forgé avec `social-dev-secret` et `roles:["ANIMATEUR"]` | 401 (preuve de R10) |
| T13 | j1 publie au nom de A un post contenant `http://127.0.0.1:3000`, `http://<conteneur-eho>:3000`, `http://169.254.169.254` et une URL publique qui redirige vers une IP privée | aucun appel sortant interne, aucun aperçu |
| T14 | j1 téléverse un SVG, un `.html` déclaré `image/png` et un vrai PNG | refusé / refusé / accepté, servi avec `nosniff` + CSP `sandbox` |
| T15 | j1 : 100 likes en 10 s | 429 au-delà du quota |
| T16 | Anonyme : `GET /users/A/followers` | j1 et anim absents de la liste et du compteur |
| T17 | Non-régression : anim au nom de B et de C, suppression d'un post sans avatar ; messagerie au nom de (champ `avatarIds` inchangé) | inchangé |
| T18 | `npx tsx --test src/garde-ecriture.test.ts`, complété des cas joueur (liste blanche) ; `docker restart`, puis `/api/sante` 200 | vert |
