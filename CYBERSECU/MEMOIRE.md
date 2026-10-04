# MÉMOIRE — CYBERSECU

> **Agent n°25 du système MINERVE**, créé le **2026-10-01** à la demande de l'utilisateur.
> Rôle : **référent cybersécurité de PLÉIADE**.
> ⭐ **RÉFLEXE IMPOSÉ PAR L'UTILISATEUR : CONSULTER cette mémoire dès qu'un sujet touche la sécurité · la METTRE À JOUR à chaque décision, correction ou incident de sécurité** (compte rendu daté dans `JOURNAL.md`).
> ⚠ Ne jamais recopier ici la valeur d'un secret, ni une adresse IP, un port ou un compte d'administration du serveur.

---

## 1. Mission et limites (décision utilisateur, 2026-10-01)

- **Maîtriser la cybersécurité de PLÉIADE** : la doctrine (les documents fournis, ingérés un par un), le terrain (ce que fait réellement la plateforme), les règles déjà décidées et le plan de durcissement.
- **Contenir tout ce que l'assistant sait de la sécurité de PLÉIADE**, et ses mises à jour futures.
- **Conseiller et vérifier** : il ne pousse rien. La mise en œuvre passe par PLEIADE ou ARCHITECTE, **testée en local** (image démarrée, redémarrage, scénario réel), avec l'**accord explicite** de l'utilisateur pour chaque mise en ligne.
- **Proportionné** : PLÉIADE est une plateforme d'**entraînement** sur un réseau d'exercice derrière VPN, pas un système homologué ou classifié. On classe les mesures par gain réel ; on ne bloque pas un exercice pour un risque théorique, mais on **signale toujours un risque élevé**.
- Les sections « Application à PLÉIADE » des fiches sont des **transpositions** faites par l'agent : ce ne sont pas des avis de l'ANSSI. Aucun des guides ne traite les conteneurs ni l'OIDC en tant que tels.

## 2. Terrain : la posture de PLÉIADE (inventaire du 2026-10-01, code + mémoires, sans le serveur)

> Constat fait **dans le code** des 13 dépôts de `C:\CECPC\pleiade\` et dans les mémoires. Le **serveur réel n'a pas été inspecté** : tout ce qui dépend de lui est « à vérifier » (§7). La copie locale de `pleiade-infra` est en retard sur le serveur (domaine `mastorion.internal`).

### 2.1 Architecture de confiance
- **Une zone d'exercice = un domaine** `<zone>.pleiade.internal`, une **clé de service de zone** (`X-API-Key`, 32 octets aléatoires) injectée dans toutes ses apps, des **instances d'apps** en conteneurs Podman.
- **Accès réseau** : Traefik n'écoute que sur l'**interface du VPN** Pritunl. Le portail de zone est **public** par décision ; c'est chaque app qui refuse.
- **Identité** : Keycloak (royaume par zone), comptes de zone **anonymes** (gc01…), « au nom de » des avatars contrôlé par eho (camps) et l'orchestrateur.
- **TLS** : CA interne « Mastorion Internal CA », ECDSA P-256 / SHA-256, valable jusqu'en 2036, **sans contrainte de nom**. Certificats de zone en P-256, valables 10 ans. Traefik en TLS ≥ 1.2, redirection 80 → 443, aucune suite imposée.
- **Déploiement** : runner auto-hébergé ; une app se déploie depuis `prod`, l'orchestrateur `pleiade-platform` depuis `main`.

### 2.2 Ce qui est solide
- Toutes les routes API des apps Next.js passent par un garde : `exiger*`, `access()`, `requireBearer`, `checkServiceKey`, `habilitation`. Les exceptions publiques sont voulues : santé, portraits eho, médias.
- Les comptes de développement sont neutralisés quand `NODE_ENV=production`, dans toutes les apps.
- La clé de zone est comparée en temps constant dans l'orchestrateur.
- La déconnexion ferme aussi la session Keycloak de la zone.
- L'émetteur Keycloak public est appliqué partout sauf dans `app-webserver`.
- Les images eho et LEAC démarrent en root uniquement pour le `chown`, puis passent à `nextjs`.
- Les secrets d'instance sont générés (`{auto}`, 32 octets).
- Les journaux d'audit existent dans social, LEAC, messagerie et MELMIL.
- Sauvegarde quotidienne, avec un filet de sécurité avant restauration.

### 2.3 Écarts relevés dans le code
→ Voir le plan de durcissement (§5), où chaque écart a son niveau de risque, son fichier et sa référence ANSSI.

## 3. ⭐ Doctrine (synthèse des 11 guides ANSSI ingérés)

> Chaque règle renvoie à sa fiche (`REF-NN`, recommandation d'origine). Détail exhaustif dans `REFERENCES\`.

### 3.1 Gouvernance et hygiène
1. **Connaître son système** : inventaire des actifs, des comptes à privilèges, des flux (matrice), des dépendances (SBOM par app et par image) — REF-01 M1-M4, REF-04 4.2.2, REF-05 R17.
2. **Comptes nominatifs et séparés** ; un compte d'administration ne sert qu'à administrer. Les comptes de zone anonymes de PLÉIADE sont un **écart assumé**, à compenser : correspondance compte ↔ personne tenue **hors ligne**, administrateurs nominatifs, connexions journalisées — REF-01 M8, REF-02 B6.
3. **Authentification forte pour tous les privilèges** (console Keycloak, admin de zone, GitHub, Pritunl, serveur), idéalement par clé physique — REF-01 M13, REF-05 R29, REF-02 G1.
4. **Aucun mot de passe par défaut, aucun secret dans Git ni dans les images** ; secrets aléatoires, distincts par zone et par app, avec rotation — REF-01 M11-M12, REF-06 RègleTailleCléSym.
5. **Correctifs dans le mois**, veille CERT-FR, Dependabot, versions harmonisées, fins de support suivies — REF-01 M34-M35, REF-04 3.12.
6. **Journaliser** les connexions et actions sensibles (Traefik, Keycloak, apps), horloge commune (NTP), conservation ≥ 1 an, copie hors du serveur — REF-01 M36, REF-02 G2, REF-10.
7. **Sauvegarder** base, volumes, royaumes Keycloak et **clé de la CA**, avec une copie **hors ligne**, et **tester la restauration** au moins une fois par an — REF-01 M37, REF-05 R49-R50.

### 3.2 Architecture : zero trust et défense en profondeur
8. **Plusieurs barrières indépendantes** : la chute d'une seule ne doit pas suffire — REF-02 P1-P6.
9. **Pas de confiance implicite liée au réseau** : être sur le VPN ne donne aucun droit ; chaque app authentifie et autorise — REF-03 ZT-01 à ZT-10.
10. **Chaîne d'administration distincte** de celle des utilisateurs : SSH, console Keycloak, admin, Traefik, Grafana, registre uniquement par un chemin d'administration, jamais exposés aux joueurs — REF-03 ZT-40/ZT-53, REF-05 R21.
11. **Annuaire d'administration séparé** des annuaires de zone (royaume `master` à part, sans chemin d'élévation depuis un gc01) — REF-05 R21.
12. **Un poste non maîtrisé n'administre jamais** la plateforme, même s'il paraît sain — REF-03 ZT-31/37/38, REF-04.
13. **Cloisonner** : une zone = un segment ; pare-feu de l'hôte qui refuse tout par défaut ; MariaDB jamais exposée — REF-01 M19/M23/M28, REF-05 R17/R45.
14. **Savoir révoquer** vite : désactiver un compte et couper ses sessions dans un délai connu ; rotation testée des clés et certificats — REF-03 ZT-20/ZT-21.
15. **Le partage du noyau** entre zones (conteneurs) cloisonne moins qu'une VM : à justifier dans une analyse de risques — REF-03, REF-04.

### 3.3 Cryptographie
16. **RSA et DH ≥ 2048 bits jusqu'à fin 2030, ≥ 3072 à partir de 2031** ; courbes ≥ 256 bits (P-256 conforme) — REF-06.
17. **Symétrique ≥ 128 bits** (192 à 256 pour le post-quantique) ; AES-GCM sans réutiliser d'IV ; **jamais** de mode sans intégrité, de bloc de 64 bits (3DES, Blowfish) ni de SHA-1 — REF-06.
18. **Secrets d'app** (`AUTH_SECRET`, JWT, clés d'API) : ≥ 128 bits d'aléa cryptographique ; HMAC-SHA-256 conforme ; **une clé pré-partagée ne se partage qu'entre deux entités** — REF-06 Annexe A.4.1.
19. **Signatures** : préférer RSA-PSS ou ECDSA à RSA PKCS#1 v1.5 — REF-06 RecoSignature.
20. **Mots de passe** : empreintes non attaquables hors ligne ; un mot de passe ne se stocke **jamais en clair** — REF-06 RègleSecretFaibleEntropie.
21. **Post-quantique** : toute donnée qui doit rester confidentielle au-delà du **1er janvier 2030** demande un échange de clés **hybride** (ECDHE + ML-KEM-768). ML-KEM ou ML-DSA seuls ne sont pas conformes. Confidentialité d'abord, authentification ensuite — REF-06, REF-07, REF-08, REF-09.
22. **TLS 1.3** : hybride ECDHE + ML-KEM dès que la pile le permet (OpenSSL 3.5, Chrome de bureau) ; **0-RTT désactivé** — REF-07. **SSH** : OpenSSH ≥ 10.0 (hybride par défaut) ; pas d'ECDSA pour SSH — REF-08, REF-06. **VPN** : la clé pré-partagée WireGuard n'est qu'une mesure post-quantique temporaire — REF-09.

### 3.4 Applications web (côté navigateur)
23. **TLS partout**, redirection 80 → 443, **HSTS** `max-age=31536000; includeSubDomains`, mais **seulement après installation de la CA** sur tous les appareils : HSTS interdit de passer outre une erreur de certificat — REF-11 R1-R2.
24. **CSP par en-tête**, générée par l'app avec un **nonce par requête**, sans `unsafe-inline`, `unsafe-eval` ni `data:`. Ne pas cumuler avec une CSP statique dans Traefik, qui bloquerait Next.js — REF-11 R13-R16.
25. **Anti-clickjacking** : `frame-ancestors 'none'` et `X-Frame-Options: DENY` par défaut ; seules les origines exactes qui embarquent une app (cockpit, admin) sont autorisées — REF-11 R17-R18, R56.
26. **Cookies de session** : `HttpOnly`, `Secure`, `SameSite=Lax` au minimum, **sans attribut `Domain`** ; l'app doit savoir qu'elle est en HTTPS derrière Traefik — REF-11 R27-R33, REF-10 R21.
27. **Un nom d'hôte par app** : toutes les apps d'une zone sont « same-site », donc `SameSite` ne les protège pas les unes des autres — REF-11 R27, R41.
28. **CSRF** : jeton aléatoire (≥ 128 bits) et contrôle d'`Origin` sur toute route qui modifie, téléversements compris — REF-11 R38, R40, annexe A ; REF-10 R24.
29. **CORS** : jamais `Access-Control-Allow-Origin: *` ; les clés `X-API-Key` restent de serveur à serveur, jamais dans le code envoyé au navigateur — REF-11 R39-R41.
30. **XSS** : jamais de contenu saisi injecté sans assainissement (`dangerouslySetInnerHTML`, `innerHTML`, `eval`) ; fichiers téléversés servis avec leur **vrai type**, `nosniff`, et **SVG refusés ou isolés** (CSP `sandbox`) — REF-11 R4-R10, REF-10 R14/R18.
31. `Referrer-Policy: strict-origin-when-cross-origin` (ou `same-origin`), `Cross-Origin-Opener-Policy: same-origin` — REF-11 R21, R46.
32. **Stockage local** (LEAC hors ligne) : analyse de risques avant d'y mettre des données sensibles ; chiffrer le stockage de la tablette — REF-11 R23-/R24-, REF-01 M30-M33.

## 4. Règles de sécurité déjà décidées (elles s'appliquent toujours)

| Date | Règle | Source |
|---|---|---|
| 2026-06-25 | Interdiction d'accéder à `DOC REF\MERCURE\RENS\01_Fiches bio` sans autorisation | mémoire auto `feedback_dossier_interdit_fiches_bio` |
| 2026-09-15 | **Ne jamais ouvrir** les profils et certificats VPN Pritunl ; ne jamais tester de mot de passe | `feedback_certificats_vpn_interdits` |
| 2026-09-16 | Modèle de branches : `prod` déploie devant les participants (`main` pour l'orchestrateur) ; **rien ne se pousse sans demande explicite** pour le dépôt concerné | PLEIADE §2bis, §9 |
| 2026-09-16 | Les routes eho sont gardées (`exigerLecture` / `exigerEcriture` / clé de zone) ; « une page qui répond 200 à un inconnu est ouverte » | PLEIADE §8bis |
| 2026-09-14 | Les règles du jeu s'appliquent **côté serveur**, jamais en masquant l'interface | PLEIADE §8bis |
| 2026-09-16 | **Une clé de service par zone** ; une app compromise ne voit que sa zone | PLEIADE §6bis.3 |
| 2026-09-17 | **Marquages de diffusion** : vérifier le filigrane réel ; en cas de marquage protecteur, signaler, exclure et laisser l'utilisateur trancher | `feedback_marquages_diffusion` |
| 2026-09-18 | LEAC : « Keycloak dit qui vous êtes, LEAC dit ce que vous avez le droit d'y faire » ; le dernier administrateur ne se révoque pas | LEAC règle 24 |
| 2026-09-21 | Émetteur Keycloak = adresse **publique** ; jeton, userinfo et JWKS en interne | PLEIADE |
| 2026-09-21 | « Au nom de » : rôle `animateur` **et** camp ouvert dans eho ; refus si un maillon manque. « Voir comme » abandonné, jugé trop risqué | PLEIADE |
| 2026-09-21 | La déconnexion ferme aussi la session Keycloak de la zone | PLEIADE |
| 2026-09-23 | Le portail de zone est public : **c'est l'app qui refuse**, masquer n'est pas protéger | PLEIADE §6 |
| 2026-09-23 | MELMIL : rôle `admin` obligatoire pour entrer | PLEIADE §6 |
| 2026-09-29 | Identifiants de zone courts et anonymes (gw01…) ; les apps suivent le `sub` | PLEIADE |
| 2026-10-01 | ⛔ **Anonymat des comptes dans MELMIL** : aucun lien compte ↔ personne stocké ni affiché ; purge automatique | PLEIADE, CYBERSECU §8 |
| 2026-10-01 | **Tester en local avant tout push** (image démarrée, base, volume, `docker restart`, scénario réel) ; vérifier ce que Xavier a pu pousser (`git fetch`) ; jamais de push forcé | mémoire auto `feedback_tester_en_local_avant_push` |
| 2026-09-21 | Un indicateur d'état mesure exactement ce qu'il rapporte ; un déploiement se vérifie par `/api/sante` | `feedback_indicateur_etat` |
| permanent | Ne jamais contourner une protection (classificateur, garde-fou, `--accept-data-loss` sans accord, push forcé) | consignes de session |
| 2026-10-01 | MELMIL : **sauvegarde de l'atelier** avant tout alignement JEMM (seul retour en arrière) ; le fichier contient les noms de l'équipe, à garder en lieu sûr | PLEIADE |

## 5. ⭐ Plan de durcissement (écarts code ↔ doctrine, 2026-10-01)

> Constaté **dans le code** : à confirmer sur le serveur avant toute action. Aucune correction n'est faite tant que l'utilisateur ne l'a pas demandée. Chaque correction suit la règle « tester en local » et s'enregistre ici et au journal.

### Risque ÉLEVÉ
| # | Écart | Où | Doctrine | Piste |
|---|---|---|---|---|
| E1 | **Terminal WebSocket de l'orchestrateur sans authentification** : l'`upgrade` est traité hors d'Express, sans garde ni contrôle d'`Origin`. N'importe quel client VPN, ou une page piégée visitée par un organisateur, pourrait ouvrir un shell dans un conteneur de zone | `pleiade-platform/src/index.ts` (gestionnaire `upgrade`, terminal) | REF-03 ZT-40/53, REF-11 R40 | vérifier le cookie et le rôle dans l'`upgrade`, contrôler `Origin` |
| E2 | **Jetons locaux forgeables dans app-social** : un jeton HS256 local est accepté en premier, avec un secret par défaut codé en dur et non injecté par le catalogue ; sur ce chemin, « au nom de » ne vérifie pas les camps | `app-social/apps/api/src/auth.ts` | REF-01 M11, REF-06 | supprimer ce chemin (le login local renvoie déjà 410), ou `JWT_SECRET` obligatoire et `{auto}` |
| E3 | **Mots de passe des comptes de zone stockés en clair** : attribut Keycloak `rawPassword`, table `orch_user_passwords`, et donc les sauvegardes non chiffrées | `pleiade-platform/src/keycloak-manager.ts`, `index.ts`, `sauvegarde-manager.ts` | REF-06 RègleSecretFaibleEntropie | distribuer une seule fois, puis supprimer ou chiffrer ; chiffrer les sauvegardes |
| E4 | **Registre d'images routé par Traefik sans authentification** : un client VPN pourrait tirer, voire pousser, une image ensuite déployée | `pleiade-infra/docker-compose.infra.yaml` | REF-01 M34, REF-04 3.12 | authentification du registre ou restriction IP ; images épinglées par empreinte |
| E5 | **Surface root de l'orchestrateur** : socket Podman rootful et dossier `.ssh` d'administration montés ; combiné à E1, l'hôte est en jeu | `pleiade-platform/docker-compose.prod.yml` | REF-05 (hyperviseur ↔ hôte), REF-03 | proxy de socket restreint, dossier SSH dédié et minimal |
| E6 | **CA interne sans contrainte de nom, installée sur des appareils personnels** : qui détient la clé de la CA peut intercepter n'importe quel domaine sur ces appareils | `pleiade-infra/pki/` | REF-06, REF-03 | nouvelle CA avec `nameConstraints` (`.internal`), durée plus courte, clé hors ligne |
| E7 | **Secrets versionnés** dans `app-social` (`apps/api/migrator.env`, 3 mots de passe) et une adresse d'administration en dur dans `deploy/` ; même chose dans l'ancêtre `mastorion` | `app-social`, `mastorion` | REF-01 M11 | faire tourner ces secrets, retirer le fichier, purger l'historique (à décider avec Xavier) |
| E8 | ⭐ *(constaté le 2026-10-02)* **Messages PROGRAMMÉS lisibles avant publication dans le réseau social** (`scheduledAt` non nul = pas encore publié). Le fil public `/posts/feed` les exclut, mais **pas** : la **page profil** `/users/:username/posts` (publique, même anonyme), le fil **« Abonnements »** `/posts/following` (comptes suivis), le message par numéro `/posts/:id`, ni l'API cockpit (cf. M12). Un joueur qui suit ou consulte le compte d'un avatar peut lire un inject avant son heure | `app-social/apps/api/src/social/users.ts`, `social/posts.ts`, `cockpit/index.ts` | REF-03 (moindre privilège) | ajouter `scheduledAt: null` à ces requêtes (sauf pour l'auteur et l'animation) ; ✅ **CORRIGÉ en local le 2026-10-02** (autorisé par l'utilisateur) : `app-social` `cf0f5ee` + `13f1776` (le compteur « Publications » comptait aussi les programmés), branche `messages-programmes-caches` ; 14 cas vérifiés sur image (joueur, anonyme, auteur, animateur, cockpit) + publication à l'heure OK ; ✅ **EN LIGNE le 2026-10-02 à 22:26** (poussé sur main + prod, redémarrage observé sur `social.delattre-26`) |

### Risque MOYEN
| # | Écart | Où | Doctrine |
|---|---|---|---|
| M1 | Valeurs par défaut faibles pour le secret de cookie, l'administrateur Keycloak et les mots de passe de base ; aucun refus de démarrer en production avec une valeur par défaut | `pleiade-platform/src/config.ts`, `docker-compose.prod.yml` | REF-01 M11 |
| M2 | **Aucun en-tête de sécurité global** : ni HSTS, ni CSP, ni `frame-ancestors`, ni `nosniff` (ni middleware Traefik, ni `headers()` Next.js) | `pleiade-infra/traefik`, `next.config.ts` des apps | REF-11 R2, R13-R18 |
| M3 | **XSS stockée possible par SVG ou HTML téléversé** : médias de la messagerie (publics, sans CSP), portraits eho (SVG acceptés), MELMIL (type MIME repris du client, servi en ligne) | `app-messagerie/.../media/[name]`, `eho/src/lib/uploads.ts`, `app-melmil/.../medias` | REF-11 R6, R10 |
| M4 | Royaumes Keycloak **sans protection anti-force brute ni politique de mot de passe** ; *password grant* ouvert sur tous les clients | `pleiade-platform/src/keycloak-manager.ts` | REF-01 M10, REF-06 |
| M5 | Tableau de bord Traefik, Grafana et console Keycloak (royaume master) joignables par tout client VPN | `pleiade-infra` | REF-03 ZT-53, REF-05 R21 |
| M6 | Dépendances : `next` 16.3.4 (critique GHSA-vcvr-r3jv-pc5j dans `next/og`, non utilisé ; corrigé en 16.3.8) dans eho et LEAC ; `mysql2`/`mariadb` (élevé) ; app-social 17 élevées (`multer` 1.x) | `package-lock.json` | REF-01 M34 |
| M7 | Volumes passés en **0777** par `preparerVolumes()` | `pleiade-platform/src/zone-manager.ts` | REF-01 M14 |
| M8 | Conteneurs en root : social, webserver, orchestrateur ; `wordpress:latest` non épinglé | Dockerfiles, catalogue | REF-04, REF-05 |
| M9 | eho `GET /api/users` renvoie la fiche complète des avatars à tout participant connecté | `eho/src/app/api/users/route.ts` | REF-03 (moindre privilège) |
| M10 | Service de génération d'images ouvert si sa clé est vide (vide par défaut) | `app-social/generator/app.py` | REF-01 M11 |
| M11 | Mot de passe root MariaDB passé en ligne de commande lors des sauvegardes (visible par `ps`) | `pleiade-platform/src/sauvegarde-manager.ts` | REF-01 M11 |
| M12 | ⭐ *(constaté le 2026-10-02, étude « cockpit joueur »)* L'API de veille du réseau social **ne filtre pas les messages PROGRAMMÉS** (`scheduledAt` non nul = pas encore publiés) sur `/feed`, `/users/:u/statuses`, `/hashtags/:tag/statuses`, `/search`, `/poll` — seuls `/activity` et `/reporting` les excluent ; le fil public (`social/posts.ts`), lui, les exclut. Le cockpit d'analyste voit donc des messages futurs comme s'ils étaient publiés. **Bloquant pour tout accès joueur** : ce serait la fuite des injects à venir. Toutes les réponses portent aussi `identity_id` (le lien eho entre les comptes d'un même avatar sur tous les réseaux) et `/groups` expose les groupes eho (les camps) | `app-social/apps/api/src/cockpit/index.ts` | REF-03 (moindre privilège), REF-11 |
| M13 | ⭐ *(constaté le 2026-10-02, avis droits joueurs)* **SSRF de l'aperçu de lien du réseau social** : toute URL contenue dans un post est suivie par le serveur, redirections comprises, sans filtre d'hôte ni d'IP ; le titre de la page visée est affiché. **Devient ÉLEVÉ si les joueurs publient** | `app-social/apps/api/src/social/link-preview.ts` | REF-03, REF-10 |
| M14 | ⭐ *(constaté le 2026-10-02)* **XSS stockée par téléversement dans le réseau social** : type MIME déclaré par le client (`image/*`, donc SVG accepté), extension reprise du nom d'origine (`.html` accepté), fichiers servis par `express.static` sur l'origine de l'app. **Devient ÉLEVÉ si les joueurs publient** (vol du jeton d'un animateur) | `app-social/apps/api/src/upload.ts`, `index.ts` | REF-11 R6, R10 |

### Risque FAIBLE
- Cookies de l'orchestrateur et du webserver sans `Secure` ; signature de session comparée hors temps constant.
- `app-webserver` : pas de `state` OIDC, pas de limite de téléversement, émetteur interne, contrôle de chemin sans séparateur.
- WordPress sans vérification TLS (`no_sslverify`) ; `KC_HOSTNAME_STRICT=false` ; Traefik `sniStrict: false`, sans suites imposées.
- app-social : route `/api/testfail`, corps JSON de 100 Mo, `db push --accept-data-loss` au démarrage.
- Garde de l'orchestrateur conditionné à la présence de la configuration Keycloak (fail-open).
- Données LEAC hors ligne non chiffrées sur les tablettes (IndexedDB).
- `pleiade-infra` local décalé du serveur : la PKI et le Traefik réels ne sont pas versionnés.
- La mémoire `PLEIADE\MEMOIRE.md` §3 contient des informations d'accès au serveur (adresse, port SSH, compte) : à sortir des mémoires partagées.

### Post-quantique et cryptographie (échéances)
- **D'ici 2030** : passer Traefik et SSH à l'échange de clés hybride (REF-07, REF-08) ; vérifier OpenSSH ≥ 10.0 sur le serveur.
- **Avant 2031** : aucune clé RSA < 3072 bits (la CA actuelle est en P-256 : conforme).
- **Dès maintenant** : 0-RTT désactivé ; secrets ≥ 128 bits (déjà 256) ; RSA-PSS ou ECDSA pour les jetons Keycloak (à vérifier : RS256 par défaut ?).

## 6. Index des sources

| Réf. | Document | Fichier source | Ingéré |
|---|---|---|---|
| REF-01 | Guide d'hygiène informatique, 42 mesures (v2.0, 2017) | `guide_hygiene_informatique_anssi.pdf` | 2026-10-01 |
| REF-02 | Les Essentiels — Défense en profondeur, mise en œuvre (v1.0) | `anssi_essentiels_defense_profondeur_mise_en_oeuvre_1.0.pdf` | 2026-10-01 |
| REF-03 | Modèle Zero Trust — les fondamentaux (ANSSI-PA-111, 2025) | `anssi-fondamentaux-zero-trust-v1.0.pdf` | 2026-10-01 |
| REF-04 | Sécurisation du poste multi-environnements (ANSSI-PA-114, 2026) | `anssi-fondamentaux-securisation-poste-multi-environnements-v1-0.pdf` | 2026-10-01 |
| REF-05 | Sécurisation d'une infrastructure VMware (ANSSI-BP-103, 2024) | `anssi-fondamentaux-securisation_infrastructure_vmware_v1-0.pdf` | 2026-10-01 |
| REF-06 | Mécanismes cryptographiques, règles et recommandations (ANSSI-PG-083 v3.00, 2026) | `anssi-guide-mecanismes-crypto-3.00.pdf` | 2026-10-01 |
| REF-07 | Transition post-quantique de TLS 1.3 (ANSSI-FT-115, 2026) | `transition_post_quantique_tls_1_3.pdf` | 2026-10-01 |
| REF-08 | Transition post-quantique de SSHv2 (ANSSI-FT-116, 2026) | `transition_post_quantique_ssh_v2.pdf` | 2026-10-01 |
| REF-09 | Transition post-quantique d'IPsec (ANSSI-FT-117, 2026) | `transition_post_quantique_ipsec.pdf` | 2026-10-01 |
| REF-10 | Note technique sécurité des sites web (DAT-NT-009, 2013) | `20130422-NP_Securite_Web_NoteTech.pdf` | 2026-10-01 |
| REF-11 | Site web : maîtriser les standards de sécurité côté navigateur (ANSSI-PA-009 v2.0, 2021) | `anssi-guide-recommandations_mise_en_oeuvre_site_web_maitriser_standards_securite_cote_navigateur-v2.0.pdf` | 2026-10-01 |

Dossier source : `D:\CECPC\PLEIADE\DOC\CYBER SECU\`. Les 11 documents sont **publics** (Licence ouverte ; la note de 2013 est « NP, diffusable sans restriction »). La mention « Diffusion Restreinte » de REF-04 décrit son champ d'application, pas un marquage.

**Sources utiles à ingérer ensuite**, citées par les guides et absentes du dossier : Guide de sélection d'algorithmes cryptographiques (ANSSI, 2021), RGS Annexe B2 (gestion des clés), guide ANSSI sur l'authentification multifacteur et les mots de passe, recommandations ANSSI pour un système GNU/Linux, pour TLS, pour l'administration sécurisée des SI, et le document compagnon « Défense en profondeur — principes ».

## 7. Questions ouvertes (à vérifier sur le serveur ou auprès de Xavier)

- Pare-feu de l'hôte : ce qui écoute hors du VPN ; SSH limité au VPN et aux clés ; fail2ban.
- Pritunl : authentification forte, durée et **révocation des profils d'exercice** (FORAD, GREYCELL…) après exercice, cloisonnement des clients VPN.
- `.env` réels : les valeurs par défaut sont-elles surchargées (secret de cookie, administrateur Keycloak, bases, `JWT_SECRET` des instances social, clé du service d'images) ?
- Registre, tableau de bord Traefik, Grafana : protégés côté serveur ?
- Où est la **clé de la CA**, qui y accède, quelle procédure de renouvellement et de révocation ?
- Sauvegardes : disque distinct, copie hors site ou hors ligne, restaurations testées, durée de conservation des dumps qui contiennent des mots de passe.
- Rythme de mise à jour de l'OS, de Podman, Keycloak, Traefik, MariaDB.
- Runner de déploiement : droits sudo, validation des arguments des scripts de promotion.
- Dépôts GitHub : privés ? protection de branche sur `prod` et sur `main` de l'orchestrateur ? scan des secrets ?
- Journaux : Keycloak enregistre-t-il les événements de connexion ? centralisation et conservation ?
- Niveau de sensibilité visé par la plateforme (données réelles hébergées : noms MELMIL, pièces LEAC marquées DR ?) et éventuelle homologation.
- L'ancêtre `mastorion` tourne-t-il encore quelque part avec ses secrets par défaut ?

## 8. Incidents et leçons de sécurité ou de fiabilité

- **2026-09-11** : 63 groupes eho supprimés faute d'avoir lu le vrai nom d'un champ d'API → lire la réponse réelle, essayer sur un élément avant de boucler.
- **2026-09-14/15** : un 401 lu comme « paquet vide » a effacé des données ; un jeton non rafraîchi a fait passer un animateur pour un joueur ; une section joueur répondait 200 aux anonymes → un échec de lecture n'est jamais un résultat valide ; vérifier côté serveur.
- **2026-09-21** : émetteur Keycloak interne (« issuer mismatch ») sur toutes les zones ; `EACCES` sur les volumes possédés par root → schéma `su-exec`.
- **2026-10-01** : panne de l'EHO (boucle de redémarrage) après un push testé sans démarrer l'image ; vraie cause, une dérive de `dotenv` au rebuild, corrigée par Xavier en épinglant le CLI Prisma → règle « tester en local » et épinglage des outils de build.
- **2026-10-01** : MELMIL reliait les comptes anonymes (gc01) aux noms et grades → option A « couper le lien » et purge automatique (`be43962`).
- **2026-10-01** : `EACCES` sur les médias MELMIL → `preparerVolumes()` en 0777 : fonctionne, mais crée l'écart M7.
- **2026-10-02** : **identité aléatoire** dans 5 apps. Auth.js v5 sans adaptateur donne à `user.id` un UUID aléatoire à chaque connexion, et le callback `jwt` l'écrasait par-dessus le `sub` Keycloak. Conséquences :
  - comptes en double (gc01 sur Chrome et Edge dans la messagerie) ;
  - données orphelines ;
  - tout contrôle « au nom de » ou de propriété fondé sur `session.user.id` porte sur un faux identifiant.

  Correction de la messagerie : `f9a9a45` (sub Keycloak + fusion des doublons), testée en local. La messagerie est **en ligne** (2026-10-02). Admin, LEAC, MELMIL et press sont **corrigés et testés en local** sur les branches `identite-sub`, puis **poussés** le même jour (MELMIL et LEAC vérifiés en ligne). LEAC recolle en plus les droits liés à un id aléatoire (voir `PLEIADE\JOURNAL.md` du 2026-10-02, suites 3 et 4). **Règle** : l'identité est toujours le `sub` Keycloak (`profile.sub` / `providerAccountId`), jamais `user.id` d'Auth.js.

## 9. Avis rendus et décisions

| Date | Sujet | Décision / état |
|---|---|---|
| 2026-10-01 | Anonymat des comptes MELMIL (avant la création de l'agent) | Option A choisie et mise en ligne : aucun lien compte ↔ personne |
| 2026-10-01 | Création de l'agent, ingestion des 11 guides ANSSI, inventaire de la posture | Plan de durcissement §5 dressé ; **aucune correction engagée**, en attente des choix de l'utilisateur |
| 2026-10-02 | Récapitulatif du plan **transmis à Xavier** par l'utilisateur (priorités E1 terminal WebSocket, E2 jetons locaux app-social ; E3–E7 à décider avec lui ; risques moyens ensuite) | ⏸️ **EN ATTENTE** : l'utilisateur poursuit l'exercice ; on reprendra plus tard, après le retour de Xavier sur ce qui est déjà protégé côté serveur. **Ne rien corriger d'ici là sans demande.** |
| 2026-10-03 | **Droits d'écriture des JOUEURS sur le réseau social** (suivre avatars et hashtags, notifications lues, publier au nom des avatars de leur camp) — `AVIS\2026-10-03_SOCIAL_DROITS_JOUEURS\AVIS.md` | Règles **validées avec corrections** : garde en **liste blanche** par route ; « au nom de » joueur limité au champ eho `avatarIdsCamp` (sans « autres comptes », `master` ignoré, champ absent = refus) ; pas de `PATCH`/`DELETE` en v1 (pas d'`operatorId` sur les posts) ; **trou E8** sous « au nom de » (l'exception « auteur » doit être réservée à l'animateur, `scheduled_at` refusé aux joueurs) ; `PATCH /api/auth/profile` hors garde, à réserver à l'animateur ; comptes d'opérateurs retirés des listes publiques d'abonnés. **4 préalables bloquants** : E2 (jetons locaux), **SSRF de l'aperçu de lien**, **XSS stockée par téléversement** (SVG/HTML, extension client), limites de débit. Recommandation : fermer la lecture anonyme (`REQUIRE_AUTH`). 18 tests locaux T1-T18. ✅ **APPLIQUÉ en local le 2026-10-03** (`app-social` `6c70d99`→`9350ddc`, `eho` `237a21e`+`afa4766`, `pleiade-platform` `bc7e186`+`9714719`) — **46/46 tests de bout en bout** (Keycloak local + eho + faux Pléiade), montée de version sur base existante OK. ⚠ **Amendé par l'utilisateur** : (1) rôle explicite **« Joueurs »** (clé `joueur`) au lieu de « sans rôle = joueur » ; sans rôle = lire + suivre ; Joueurs l'emporte sur Animation ; (2) les joueurs **modifient / suppriment / programment** leurs propres messages (contre R4 v1) — garde-fou : champ **`parAnimation`** sur posts/commentaires, **vrai par défaut** (tout l'existant), faux seulement pour ce qu'un joueur crée ; un joueur ne touche ni ne voit d'avance un inject de l'animation, même sur un avatar de son camp ; (3) rôle **« Modération »** (clé `moderateur`, se cumule) : modifier/supprimer tout, sans publier ; (4) l'**Animation** ne modifie/supprime que les messages des avatars qu'elle peut incarner (camp + sans groupe). Préalables R10-R13 faits (E2 côté social : jetons locaux refusés en mode Keycloak ; M13 ; M14 ; quota 10 publications / 60 actions par minute). Lecture anonyme : **laissée ouverte** (décision à prendre). ✅ **EN LIGNE le 2026-10-03 à 23:32** (eho `2026-10-03.1`, Pléiade poussé, social redémarré ; `nosniff` constaté sur `/api/uploads`) |
| 2026-10-03 | **MELMIL : rôle « Lecture et demandes »** (clé `lecteur`, FORAD) — décision utilisateur, sans avis CYBERSECU dédié | Moindre privilège appliqué **côté serveur** : `peutEcrire` = Animation seule ; un lecteur peut envoyer l'atelier mais `modificationsInterditesAuLecteur` (comparaison stricte à l'atelier enregistré, version obligatoirement à jour) refuse en 403 tout ce qui n'est pas une demande de **sa** cellule encore « envoyée », ses fichiers fournis et sa propre ligne `cellulesDesComptes` (déclarable une fois, jamais réécrite → pas d'usurpation de cellule). `/api/medias` : jamais de fichier sur un incident ni de produit livré. Anonymat inchangé (demandes = cellule seule). Testé en local (11 tests + Playwright, 403 vérifiés). ✅ **EN LIGNE le 2026-10-03** (2026-10-03.2) |
| 2026-10-03 | **MELMIL : groupes d'animation GA1 / GA2** (rôles `ga1`, `ga2` ; rôle `admin` « Animation » **retiré**) — décision utilisateur | Cloisonnement d'écriture **par propriétaire d'event**, appliqué **côté serveur** : `modificationsHorsPerimetre` (PUT `/api/atelier`, comparaison élément par élément — events, storylines, incidents, comptes rendus, fichiers — avant ET après ; seul l'Admin change le propriétaire d'un event) ; `incidentHorsGroupe` sur dépôt, suppression et rattachement de fichiers. Lecture inchangée pour tous (choix utilisateur : chacun consulte l'autre). Demandes de produit communes. Import JEMM limité à un périmètre (`alignerPerimetre`) : un export ne peut pas remplacer l'event d'un autre groupe. ⚠ Transition : l'ancien rôle `admin` n'ouvre plus MELMIL → cocher GA1/GA2 sur le bouclier aussitôt après la mise en ligne, pousser Pléiade puis MELMIL à la suite. Vérifié en local (403 sur incident et fichier de l'autre groupe, 18 tests). ✅ En ligne le 2026-10-03 à 16:27 (Pléiade `83084af` puis MELMIL `4bb00c9`). **Complément (même jour, `4bb00c9`)** : noms d'usage des groupes (`nomsGa`, « GA1 » → « GREYCELL ») — **simple libellé**, les droits restent portés par les rôles `ga1`/`ga2` ; renommage **réservé à l'Admin côté serveur** (`modificationsHorsPerimetre` → 403 pour un GA, vérifié en local ; les lecteurs sont bloqués par la liste blanche de `lecture-demandes`) ; relecture stricte (clés `GA\d` seulement, ≤ 24 caractères). **Puis (`cf1c8d8`)** : couleur par groupe (`couleursGa`) — **clé d'une palette fermée**, jamais un code couleur libre (pas d'injection de style), relecture qui rejette toute autre valeur ; changement **réservé à l'Admin côté serveur** (403 pour un GA, testé). **Puis (`08ed95c`, CRQ UTMC)** : nouveau champ `crqs`, chaque CRQ appartient à son groupe — la garde `modificationsHorsPerimetre` l'inclut (un GA ne crée/modifie/retire pas le CRQ de l'autre ; refus aussi d'un CRQ sans groupe), les lecteurs restent bloqués (liste blanche) ; relecture stricte (groupe `GA\d`, un seul par jour et groupe, textes bornés). Le modèle Word publié (`public/modeles-cr/crq-utmc.docx`) a été **vidé de tout texte** du document d'origine (nom du signataire, auteur) |
| 2026-10-04 | **MELMIL : déplacer une demande de produit vers un autre incident** — besoin utilisateur, **réservé à la cellule Prod** (rôle `prod`, et `gestion`) | Appliqué **côté serveur** : `demandesModifieesSansDroit` signale tout changement de `incident` d'une demande (« incident de DP-xx ») → 403 pour tout rôle sans Prod (GA, lecteur) ; les lecteurs restent aussi bloqués par `modificationsInterditesAuLecteur` (demande hors « envoyée »/hors cellule). Exemption **étroite** dans `modificationsHorsPerimetre` pour la Prod membre d'un seul GA : seul le **rattachement** (`incident`, `fourniPour`) d'un fichier livré/joint à une demande peut changer — tout autre changement du fichier reste refusé (testé). Aucune donnée de compte ajoutée (anonymat inchangé). 9 tests + Docker. ✅ **Poussé** le 2026-10-04 (`9be0958`, 2026-10-04.3, main + prod) — mise en ligne à confirmer |
| 2026-10-04 | **app-admin : cellule d'un scénario (GREYCELL / FORAD)** — besoin utilisateur | L'admin lit désormais le claim **`groups`** du jeton Keycloak (mapper `group-membership` déjà posé par PLÉIADE sur tous les clients de zone ; seulement les noms courts) pour **déduire la cellule** de l'auteur. ⚠ **Aucun droit nouveau** : `operatorOf` exige toujours un rôle `admin`/`operateur` (un groupe seul n'ouvre rien — testé) ; la cellule n'est qu'un **libellé** d'affichage/filtre. L'API n'accepte que « GREYCELL » / « FORAD » (liste fermée, `celluleNormalisee`, testé contre une injection) ; tout éditeur peut la corriger (comme le nom). Anonymat : une **cellule**, pas une personne — rien de plus que `createdBy` déjà stocké. Colonne `scenarios.cellule` additive (db push), essai de mise à niveau local OK. ✅ Poussé le 2026-10-04 (`e810c73`, main + prod) |
| 2026-10-04 | **MELMIL : ouvrir les pièces jointes sans télécharger (aperçu bureautique)** — besoin utilisateur | ⚠ **Faille corrigée au passage** : `/api/medias/[id]` servait EN LIGNE le type déposé tel quel → un .html/.svg déposé se serait exécuté sur l'origine MELMIL (XSS stockée). Désormais : type effectif (extension si générique), **HTML/XML/JSON/JS servis en `text/plain`**, et **`Content-Security-Policy: sandbox; default-src 'none'…`** sur tout affichage en ligne sauf le PDF (le lecteur PDF de Chrome refuse le bac à sable) et sur les téléchargements ; `nosniff` gardé. Aperçu bureautique côté navigateur : **`docx-preview` 0.4.1** (Apache-2.0, maintenu, seule dépendance jszip) ; xlsx/ods/pptx/odp/odt lus par code maison (jszip + DOMParser, **texte rendu par React, jamais d'innerHTML**, images en `blob:` limitées à png/jpeg/gif/webp/bmp — **SVG exclu**, relations `External` ignorées, plafond 40 Mo décompressés/entrée anti-bombe zip, 80 Mo par fichier). **Refusés** : `xlsx` npm 0.18.5 (failles connues non corrigées sur npm), `pptx-preview` (provenance non vérifiable, sans dépôt). ⚠ **`npm audit` (préexistant, non lié)** : `next` 16.2.0–16.3.5 **critique**, `mysql2`, `mariadb`, `deepmerge-ts`, `image-size` élevés → à traiter (montée de version testée) avec PLEIADE. 13 tests ; Docker OK. ✅ Poussé le 2026-10-04 (`97129ad`, avec `60a791a`, main + prod) |
| 2026-10-04 | **Social / admin : publication MP3** — correctif | Social accepte désormais un `.mp3` annoncé avec un type non standard ou vide (`normaliserTypeMp3`) : la **signature** (ID3 / trame MPEG) reste le seul juge — testé : faux .mp3 → 400. ⚠ La route `POST /api/service/publish` (clé de zone, utilisée par les scénarios de l'admin) **ne vérifiait pas la signature** : ajout de `verifierFichiersTeleverses` (défense en profondeur ; la clé de zone n'est pas une preuve de contenu). Admin : `.mp3` ajouté à la liste FERMÉE des extensions, relu en `audio/mpeg`. ✅ Poussé le 2026-10-04 (`app-social` `ada6088`, `app-admin` `6af7d0a`, main + prod) |
| 2026-10-04 | **MELMIL : avis du demandeur sur un produit livré** — besoin utilisateur | Le statut d'une demande restait **réservé à Prod** côté serveur (`demandesModifieesSansDroit`). Exception **étroite** ajoutée (`avisSeulement`) : un non-Prod peut faire **uniquement** Livrée → Approuvée / À modifier, avec **un avis ajouté** (verdict cohérent avec le statut, texte obligatoire pour « à modifier ») et **rien d'autre** de la demande modifié (mot de Prod, formulaire, historique d'avis antérieur — comparaison stable) ; « Lecture et demandes » : même exception, **sur sa cellule seulement**. Testé : avis légitime accepté ; avis qui change aussi le mot de Prod → refusé ; « Approuvée » sans avis → refusé ; autre cellule → refusé. Anonymat : l'avis retient le nom d'opérateur (comme `statutPar`), pas de compte. ✅ Poussé le 2026-10-04 (`60a791a`, main + prod) |
| 2026-10-03 | **Réseau social : fichiers MP3 acceptés sur les posts principaux** — décision utilisateur | Nouveau type de téléversement, ajouté **dans le cadre de durcissement M14 existant** : liste fermée (`audio/mpeg`, `audio/mp3` → extension `.mp3` imposée), **signature vérifiée** (étiquette ID3 ou trame MPEG, sinon fichier effacé + 400), servi en `audio/mpeg` avec `nosniff` + CSP `sandbox` (le `.mp3` rejoint la liste des extensions affichées en ligne), taille plafonnée (`SOCIAL_UPLOAD_AUDIO_MAX_SIZE`, 20 Mo). Son **refusé sur les réponses** côté serveur (y compris API `service`). ⚠ Constat préexistant : la route `service/publish` n'appelle pas `verifierFichiersTeleverses` (clé de service seule) — à durcir à l'occasion. Vérifié en local (ID3 accepté, faux MP3 refusé, réponse refusée). ✅ En ligne le 2026-10-03 à 15:03 |
| 2026-10-03 | **MELMIL : rôle « Admin »** (clé `gestion`) — décision utilisateur | Séparation des tâches : l'Animation (clé `admin`, historique) ne touche plus aux réglages ni à la planche JEMM. Garde **serveur** : `reglagesModifiesSansDroit` (nom, calendrier, étape GT, retrait/renommage d'ETIM → 403) et PUT `/api/planche` réservé à `gestion`. ⚠ Point d'attention : la restauration d'une sauvegarde reste un remplacement complet de l'atelier, désormais réservé à l'Admin (onglet masqué + garde partielle serveur). ⚠ À la mise en ligne, cocher Admin sur au moins un groupe. ✅ **EN LIGNE le 2026-10-03** (2026-10-03.2) |
