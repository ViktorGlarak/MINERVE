# JOURNAL — CYBERSECU (historique chronologique, append-only)

> Comptes rendus datés : ingestions, audits, décisions, corrections, incidents. L'état durable est dans `MEMOIRE.md`.

---

## 2026-10-01 — Création de l'agent, ingestion des 11 guides ANSSI, inventaire de la posture de PLÉIADE

- **Demande de l'utilisateur** : créer l'agent « CYBERSECU ». Il doit contenir tout ce que l'assistant sait de la cybersécurité, et ses mises à jour futures. Il doit ingérer et maîtriser la documentation PDF déposée dans `D:\CECPC\PLEIADE\DOC\CYBER SECU\`, pour bien connaître la cybersécurité de PLÉIADE.
- **Marquages vérifiés avant ingestion** : les 11 documents sont **publics** (ANSSI, Licence ouverte ; la note de 2013 est « NP, diffusable sans restriction »). La mention « Diffusion Restreinte » de REF-04 décrit le champ d'application du guide : ce n'est pas un marquage.
- **Ingestion** par 4 sous-agents en parallèle, avec lecture intégrale page par page (PyMuPDF) des 388 pages. On obtient 11 fiches `REFERENCES\REF-01` à `REF-11` (2 178 lignes), qui listent toutes les recommandations avec leur numérotation d'origine. Nombre de recommandations par fiche :

  | Fiche | Recommandations |
  |---|---|
  | REF-01 | 42 mesures |
  | REF-02 | 6 principes, 7 barrières et 3 barrières génériques |
  | REF-03 | 55 (numérotation ZT-01 à ZT-55 ajoutée) |
  | REF-04 | 78 |
  | REF-05 | 50 |
  | REF-06 | 46 |
  | REF-07 | 11 |
  | REF-08 | 7 |
  | REF-09 | 10 |
  | REF-10 | 29 |
  | REF-11 | 71 |

  Erreurs du guide REF-11 relevées dans la fiche, pour ne pas les recopier : exemples de CSP avec des deux-points parasites, `Set-Cookie` mal ordonné, contradiction sur le téléversement multipart.
  - ⚠ Écart signalé par un sous-agent : son script a extrait le texte de **tous** les PDF du dossier dans le scratchpad de session, pas seulement des siens. Ce sont les mêmes documents publics, tous à ingérer : sans conséquence.
- **Inventaire de la posture** par un 5e sous-agent, en lecture seule :
  - mémoires MINERVE et code des 13 dépôts ;
  - aucune clé privée ni aucun profil VPN ouverts, aucun secret recopié ;
  - seuls les certificats **publics** de la CA et le wildcard ont été lus ;
  - un `npm audit --package-lock-only` a été lancé, sans modification.

  Résultat : 20 règles déjà décidées, les incidents, la posture par thème, **7 écarts de risque élevé, 11 moyens et 8 faibles**, et les questions ouvertes.
- **Vérification directe par l'agent principal** des deux écarts les plus graves :
  - **E1** : `pleiade-platform/src/index.ts`, le gestionnaire `server.on("upgrade")` passe `/ws/terminal` à `handleTerminalWs` sans contrôle de session, de rôle ni d'`Origin` ;
  - **E2** : `app-social/apps/api/src/auth.ts`, `JWT_SECRET` a une valeur par défaut codée en dur, un jeton local est essayé en premier, et sur ce chemin « au nom de » ne vérifie que le rôle `ANIMATEUR`, sans `actAsAutorise`. `JWT_SECRET` est absent de `catalog/social.yml`.
  - **Les deux sont confirmés dans le code** ; leur exposition réelle reste à vérifier sur le serveur.
- **Rédigé** : `MEMOIRE.md`, avec les 9 parties suivantes :
  1. mission ;
  2. terrain ;
  3. doctrine de 32 règles sourcées ;
  4. 20 règles décidées ;
  5. plan de durcissement E1–E7, M1–M11, faibles, et calendrier post-quantique ;
  6. index ;
  7. questions ;
  8. incidents ;
  9. avis.

  S'y ajoutent `README.md` et le prompt `SYSTEME\PROMPTS\cybersecu.md`.
- **Enregistrement** : registre `CLAUDE.md` (et règle générale « sécurité → CYBERSECU »), `SYSTEME\ROUTAGE.md`, `MINERVE_HOME.md`, compteur `NOYAU\MEMOIRE.md` porté à 25 agents, mémoire automatique.
- **Aucune correction engagée** : le plan attend les choix de l'utilisateur. Les risques élevés lui ont été présentés.

## 2026-10-02 — Plan transmis à Xavier, mis en attente

- L'assistant a rédigé un récapitulatif à l'intention de Xavier : l'origine (11 guides ANSSI et lecture du code, sans le serveur), les priorités E1 et E2, les points E3 à E7 à décider ensemble, les risques moyens, la méthode (tests en local, accord avant tout push) et les questions sur ce qui est déjà protégé côté serveur.
- L'utilisateur l'a **transmis à Xavier**. Il demande de **garder tous ces éléments de côté** et de poursuivre l'exercice. On reprendra plus tard, avec la réponse de Xavier.
- **État** : plan en attente, aucune correction engagée.

## 2026-10-02 — Défaut d'identité trouvé (messagerie, puis 4 autres apps)

- En cherchant pourquoi gc01 apparaissait deux fois dans la messagerie (Chrome et Edge), l'assistant a trouvé que `user.id` d'Auth.js (aléatoire à chaque connexion) remplaçait le `sub` Keycloak comme identité.
- La correction de la messagerie, `f9a9a45`, est faite et testée en local, mais pas poussée. Le même défaut est relevé dans admin, LEAC, MELMIL et press, sans correction pour l'instant.
- Le détail est dans `MEMOIRE.md` § 8.

## 2026-10-02 — Nouvelles routes entre apps : MELMIL ↔ admin (avis DESIGNER n°28)

- Deux routes de service nouvelles :
  - `GET /api/service/incidents` (MELMIL) ;
  - `GET /api/service/scenarios` (admin).
- Les deux exigent la clé de la zone (`X-API-Key`, comparaison à temps constant). Vérifié en local : 401 sans clé ou avec une mauvaise clé.
- La liste des incidents est **anonyme**, conformément à l'option A : code, sujet, storyline, event, D+, heure, jour. Ni « confié à », ni ETIM, ni émetteur, ni destinataires. Un test le garantit (`service : ANONYME`).
- La liste des scénarios ne contient ni auteur ni contenu.
- Le navigateur ne parle qu'au serveur de son app (`/api/zone/scenarios` est réservée aux sessions MELMIL) ; aucune clé n'est exposée.
- État : poussé le 2026-10-02 (admin `7d6d96f`, MELMIL `c27d368`).

## 2026-10-02 — Avis sur le projet « appropriation des avatars » (cadré, pas codé)

- Le lien stocké est **compte de zone ↔ avatar** (gc05 → @avatar), jamais **personne réelle ↔ avatar**. Il est donc compatible avec l'anonymat des comptes (option A).
- Le **blocage**, choisi par l'utilisateur, devra être **vérifié par le serveur** :
  - kit IA (étape 1) ;
  - incarnation dans le réseau social, la presse et la messagerie (étape 2).

  Un blocage seulement affiché à l'écran ne protège rien.
- Les animateurs passent outre et libèrent, comme les masteradmin pour les camps. Chaque appropriation et chaque libération est journalisée.

## 2026-10-02 — Appropriation des avatars : étape 1 en local

- Invisibilité pour les joueurs, vérifiée :
  - la donnée ne sort **jamais** par `/api/users` d'eho, lisible de toute session ;
  - `/api/appropriations` exige la clé de la zone ou le rôle administrateur d'eho ;
  - l'écran est dans l'admin, réservée à l'animation.
- Blocage vérifié par le serveur de l'admin (items et import) : 403 pour l'avatar d'un autre compte, sauf animateur.
- Le mode local de l'admin accepte `ADMIN_DEV_ROLES` et `ADMIN_DEV_ID`, ignorés en production comme `ADMIN_DEV_USER`.
- Non poussé.

## 2026-10-02 — Appropriation des avatars et vérification obligatoire : mise en ligne

- eho `e344a19` et admin `d656148` poussés sur main et prod, après le test des images sur des bases à l'ancien format.
- Vérifié sur l'image :
  - `/api/appropriations` répond 401 sans clé ;
  - rien dans `/api/users` ;
  - un joueur est refusé (403) et renvoyé hors des pages Animation (testé en local avec une session de joueur).
- Le blocage dur a été remplacé, à la demande de l'utilisateur, par une consigne au kit IA et par un avertissement de « Vérifier ». Le serveur rend « Vérifier » obligatoire avant tout lancement (empreinte du contenu vérifié).
- **2026-10-11** — eho (branche locale `ia-avatars`) : nouvelles routes de la couche IA `GET/PUT /api/population-ia`, `POST /api/users/[id]/ia-actif`, page `(admin)/population-ia` — toutes sous `exigerEcriture` (Administration ou clé de service) + `GardeAdmin`/`PAGES_ADMIN` ; vérifié : un animateur (gc10) est renvoyé sur le trombinoscope. Même périmètre que `etat-ia` / `comportement-ia` (11/10 matin) : la gestion des avatars IA n'est ni pour les joueurs ni pour l'animation.
- **2026-10-11** — Avis sécurité sur le **tutoriel guidé** (panneau de guide, progression par compte, coche automatique, barre réduite joueurs, écran de suivi ; avis DESIGNER n°97) : détection serveur seulement (clé de zone jamais au navigateur), signal par `sub` de session réduit à des booléens, « déclaré » tracé à part, mode tutoriel = drapeau de zone serveur (404 en zone réelle), suivi réservé à l'animation + zone d'entraînement, purge de la progression à la suppression de la zone. Règles détaillées : MEMOIRE §9. Aucun dépôt touché.
- **2026-10-11** — Tutoriel guidé codé en local (branches `tutoriel`) selon R1-R6 : détection serveur seulement (eho lit ses tables, interroge le social avec la clé de zone ; le navigateur ne reçoit que fait/en attente), compte tiré de la session (ou d'un serveur de la zone via `x-tuto-compte`), Origin vérifiée sur les écritures de session, drapeau de ZONE `PLEIADE_TUTORIEL` posé par l'orchestrateur d'après la famille `entrainement` (vérifié : 404 dans ia-locale), écran de suivi à rôle vérifié serveur (stagiaire → acces-refuse / 401), comptes anonymes, remise à zéro par l'animation. Le social n'audite `post.view` qu'en zone d'entraînement. Non poussé.
- **2026-10-11** — Avatars IA : décision utilisateur de les intégrer à DELATTRE 26 avec un interrupteur général dans eho (Administration seulement, coupés par défaut, journalisé ; route moteur sous clé de service). Avis CYBERSECU attendu AVANT le push sur : la clé de zone du serveur détenue par le PC du moteur (VPN), son stockage local, et la purge des états IA en fin d'exercice.
- **2026-10-11 (après déploiement eho 2026-10-11.4 dans DELATTRE 26)** — Avis rendu sur le moteur IA distant (PC portable, Gemma locale, VPN Pritunl). (1) Clé : la clé de zone ouvre toutes les apps **et** la découverte interne de l'orchestrateur, et elle n'est révocable qu'en la régénérant pour toute la zone → cible = **clé dédiée `PLEIADE_IA_KEY`** injectée dans eho et le social seulement, acceptée sur la seule liste blanche des routes IA, « au nom de » borné aux membres de CAMP IA, journal signé `moteur-ia`. **Pas bloquant** pour une première session **surveillée** si les compensations sont tenues ; **bloquant** avant tout fonctionnement autonome sans surveillance (nuit) ou si le disque du portable n'est pas chiffré (BitLocker). (2) Fichier de clé hors dépôt et hors dossier synchronisé, ACL au seul compte de l'utilisateur, posé par l'utilisateur lui-même (l'IA ne le lit pas), les scripts reçoivent un chemin, jamais la clé. (3) VPN ouvert seulement pendant les sessions, pas de mise en veille pendant un fonctionnement autonome, Ollama et la page de validation sur 127.0.0.1. (4) Déjà couvert : interrupteur coupé par défaut et relu, journalisation, garde Administration, CAMP IA injouable, origine IA masquée aux joueurs. (5) Règles des scripts : TLS vérifié (`NODE_EXTRA_CA_CERTS`), jamais de désactivation, adresses limitées à la zone, délais d'expiration, 401/403 = arrêt, pas de repli local en mode distant, purge en fin d'exercice (états IA, publications IA, fichiers locaux, fichier de clé, rotation). Règles détaillées : MEMOIRE §9. Aucun dépôt touché.
- **2026-10-11 (soir)** — Revue de sécurité de la nouvelle app **`app-ia`** (`ac6faf9`), du catalogue `ia.yml` et de l'interrupteur eho (`ia-avatars` `8d18450`). Aucun bloquant pour la présentation à Xavier. La clé de zone est conforme : injectée, lue côté serveur seulement, jamais envoyée au navigateur ni écrite au journal. Les gardes Administration et le contrôle d'Origin sont en place, et les archives n'offrent pas de chemin traversant. À corriger avant prod : exposition d'Ollama (proxy TLS + jeton dédié + pare-feu limité au serveur), `r.ok` manquant dans `appelerModele`, suppression des archives en fin d'exercice (elles contiennent des extraits de messages privés de joueurs), test de la matrice des droits. Améliorations : bail atomique, stdout sans textes privés, `/tmp/memoire`, repli du client Keycloak, `azp`, `Origin: null`, provenance eho. Détail : MEMOIRE §9. Aucun dépôt touché.
- **2026-10-11 (~19 h 30)** — Corrections de la revue `app-ia` **appliquées et vérifiées en local** (app-ia 2026-10-11.9, eho 2026-10-11.6, rien poussé). Faits : `r.ok` dans `appelerModele` ; suppression des archives (Administration + Origin + journal) ; test de la matrice des droits dans `npm test` (bloque l'image) ; Origin absente / nulle / illisible → 403 (vérifié avec session : 4 × 403) ; Keycloak exigé en production ; bail atomique ; stdout sans texte de message privé ; plus d'écriture `/tmp/memoire` ; rôles du client `ia` seuls + contrôle `azp` ; eho : `depuis` seulement avec la clé de service. **Restent ouverts** : exposition d'Ollama en production (proxy TLS + jeton + pare-feu, décision Xavier), clé dédiée `PLEIADE_IA_KEY`, Origin sur le PUT de l'interrupteur eho, délimitation du contenu des joueurs dans les invites.
- **2026-10-11 (~20 h)** — Avis sur l'**export / import des fiches de comportement IA** (eho, page Population IA : export JSON fiches + états + groupes + lieu ; import en essai à blanc puis application, fiches seulement), l'**export pour analyse d'app-ia enrichi du `retex` du Social** et les **scripts locaux**. Lu : `comportement-ia/route.ts`, `api-auth.ts`, `population-ia.ts`, export Excel d'eho, `archives/route.ts` et `session.ts` d'app-ia, route `retex` du Social. Constats : `exigerEcriture` accepte la clé de service et le Bearer → nouvelle garde « session Administration » pour import et export ; `User.rawPassword` au schéma → `select` explicite obligatoire ; la route `retex` du Social n'est pas bornée ; les téléchargements d'app-ia n'ont pas `no-store`. 9 BLOQUANTS (garde + Origin, bornes 8 Mo / 500 entrées / 256 Ko, schéma fermé et champs protégés, liaison essai → application par empreintes SHA-256 + transaction, journal, en-têtes et minimisation des exports, refus des caractères invisibles, lecture bornée du `retex`, matrice de tests), 5 À FAIRE (pagination `retex`, stockage sur C: hors dépôt, purge fin d'exercice, analyse des messages de joueurs par modèle local seulement, délimitation de la fiche dans l'invite), 4 améliorations. Détail : MEMOIRE §9. Aucun code modifié.
- **2026-10-11 (~20 h 20)** — Avis export / import **mis en œuvre et vérifié en local** (eho 2026-10-11.7, app-ia 2026-10-11.10, rien poussé). **B1** garde `exigerSessionAdmin` (clé, Bearer → 403 ; Origin) ✓ ; **B2** bornes 8 Mo (Content-Length + octets lus), 500 et ≤ fiches existantes, 256 Ko, profondeur 8, chaînes 8 000, listes 200 ✓ ; **B3** format fermé ✓ — *écart assumé* : l'entrée admet aussi des repères en lecture seule ignorés (`displayName`, `pays`, `lieu`, `groupes`, `cohorte`, `actif`, `ficheMajLe`) pour que le fichier exporté soit réimportable tel quel (sauvegarde) ; toute clé `etat*` ou inconnue → entrée refusée ; base ancrée élargie à `opinions_initiales` et `eho_id` ; **B4** empreinte du fichier + SHA-256 de chaque fiche visée, 409, transaction ✓ ; **B5** journal par avatar (`ia_fiche_importee`, champs changés, empreinte courte) + global (`ia_import`), `ecritPar import:<compte>`, export journalisé (`ia_export`) ✓ ; **B6** `select` explicite (jamais `rawPassword`), `no-store` + `nosniff` + nom serveur ✓ — l'export d'eho ne contient **pas** la mémoire (elle est dans l'export d'analyse du Moteur IA), donc pas de risque de 64 Mo ; **B7** invisibles et contrôles refusés, texte avant-après affiché ✓ ; **B8** `retex` côté serveur, 30 s, champs réduits, aucun compte réel (vérifié sur l'export), 20 000 / 20 Mo, erreur ≠ vide, `no-store` ✓ — *écart* : `depuis` n'est pas obligatoire, il vaut par défaut le début du journal en ligne, plafonné à 14 jours ; **B9** : règles pures dans `npm test` d'eho, contrôles vivants par `dev/prototype-ia/test-fiches-import.cjs` (clé 403, sans session 401, Origin étrangère 403, 9 Mo 413, cohorte refusée, empreinte périmée 409, sur avatar jetable) — le refus d'un **animateur** n'a pas été rejoué faute de compte animateur dans la zone locale (la garde exige le rôle Administration, comme les autres routes IA). **F2** appliqué : fichiers du poste dans `%USERPROFILE%\.pleiade\analyses-ia\`. **Ouverts** : F1 pagination `retex`, F3 purge fin d'exercice, **F4 décision utilisateur** (analyse des messages de joueurs par un agent cloud), F5 délimitation dans l'invite.
- **2026-10-12 (~1 h 45)** — Mémoire longue des avatars IA (app-ia 2026-10-12.2, eho 2026-10-12.1, local) : deux nouvelles tables dans la base du moteur, `variation` (variations d'humeur, d'opinion, de confiance… avec leur cause) et `vecteur` (vecteurs de sens des souvenirs, qui dérivent des messages lus, joueurs compris). Calcul des vecteurs par Ollama **local** (bge-m3, sur le processeur), aucune donnée ne sort. **Purge** : « Supprimer les archives (fin d'exercice) » efface aussi ces deux tables (Administration, Origin, journalisé). eho : `GET /api/etat-ia?versions=1` (clé de service ou Administration, comme avant) ne renvoie que version et date — moins de données en transit sur le VPN. Bloc `vie` des fiches : validé par l'import (11 clés, format fermé). Rien poussé.
- **2026-10-12** — Avis sur le **nœud de calcul Ollama de production** : app-ia (poussé, catalogue `ia`) sur le serveur DELATTRE 26 appelle Ollama (Gemma 4 26B + bge-m3) sur le PC de l'utilisateur par le VPN Pritunl (PC = 10.8.0.3, aussi sur le LAN 192.168.10.104). Option utilisateur : « VPN seulement + jeton ». Montage NOYAU : proxy Node sans dépendance sur 10.8.0.3:11435, jeton `OLLAMA_CLE`, liste blanche 3 routes, modèles imposés, corps et délais bornés, journal sans contenu, pare-feu limité au serveur, pas de TLS au départ. **Verdict : VALIDÉ AVEC RÉSERVES.** Obligatoire avant l'essai (O1-O8) : proxy durci (pas de repli `0.0.0.0`, cible fixe, chemin exact, en-têtes reconstruits, `Origin` refusé et pas de CORS, contrôle de l'IP source en plus du pare-feu, concurrence bornée, compte non privilégié) ; jeton 32 octets comparé sur empreintes SHA-256, fichier sur C: à ACL restreinte, valeur jamais dans un dépôt ni dans une conversation IA ; pare-feu : purger les règles larges `node.exe`, règle unique vers l'IP **observée** du serveur depuis le conteneur ; Ollama vérifié sur 127.0.0.1, sans `OLLAMA_DEBUG`, à jour ; journal sans corps ni jeton ; app-ia : règle « pas de `http://` » amendée pour la seule adresse tunnel ; Pritunl constaté en tun, sans client-to-client, profil nominatif, route du serveur par le tunnel ; matrice de refus rejouée sur le vrai système. **TLS (point 4)** : non exigé pour l'essai surveillé si Pritunl est constaté conforme ; exigé immédiatement sinon, et avant tout autonome / usage durable — certificat **auto-signé dédié, généré sur le PC, épinglé dans app-ia**, sans toucher à la CA de zone. Différable : bornage de `options`/`keep_alive`, `PLEIADE_IA_KEY` (bloquante avant autonome), BitLocker, proxy à la demande, stabilité de l'IP (Pritunl : IP stable par utilisateur, échec fermé si elle change), périmètre des données (messages de joueurs traités sur le PC → purge F3). Détail : MEMOIRE §9. Aucun code modifié.
- **2026-10-12** — Revue avant push d'eho **« Installer la population IA »** (branche `installer-population`, non commitée : `src/lib/installation-ia.ts`, `mode: "installer"` du POST `src/app/api/population-ia/fiches/route.ts`, `src/components/installation-ia.tsx`, bloc de `population-ia/page.tsx`). But : installer dans DELATTRE 26 les fiches de la zone locale sans clé de zone sur le poste. **Verdict : VALIDÉ AVEC RÉSERVES.** Vérifié conforme : garde `exigerSessionAdmin(req, true)` (clé et Bearer refusés, session Administration, Origin = hôte) ; corps borné (Content-Length et octets lus) ; schéma d'entrée fermé, clés `etat*` refusées, `validerFiche` réutilisé (invisibles, bornes, liste blanche) ; correspondance **par username exacte** : le `IN` SQL (collation MariaDB insensible à la casse et aux espaces de fin) peut ramener une ligne, mais la recherche `Map` JS est exacte → casse, espaces, caractères invisibles ou formes Unicode différentes donnent « ignoré », jamais un autre avatar ; doublon refusé ; `displayName` et `groupes` du fichier non utilisés (valeurs de la zone) ; noms et propriétés des groupes **fixés par le code** (`GROUPES_IA_A_PREPARER`) ; empreinte fichier + cibles (fiche oui/non + groupes ; un avatar apparu entre-temps change l'empreinte) ; blocage CAMP IA revérifié dans la transaction ; tout ou rien ; journal par avatar (`ia_installe`) + bilan (`ia_installation`), opérateur Keycloak ; pas de mémoire, pas de compte, pas d'écrasement ; rendu React échappé (pas de `dangerouslySetInnerHTML`). **Obligatoire avant push** : (I1) `x.cohorte in COHORTES` (installation-ia.ts:79) et `c in COHORTES` (population-ia.ts:30) acceptent les clés du prototype (`toString`, `constructor`, `__proto__`…) : cohorte fantôme stockée, puis `reintegrer` plante après avoir mis l'avatar dans CAMP IA → `Object.hasOwn` ; (I2) la `cohorte` de l'entrée écrase `comportement.cohorte` (l.82) sans contrôle → refuser si elle contredit la fiche ou l'orientation de départ ; (I3) « IA EN PAUSE » préexistant non contrôlé (l.38-45, 108-111) : ouvert à des camps → avatars rendus jouables par ces camps (élévation) ; exclusif → avatars de packs rendus injouables → blocage (non exclusif ET sans camp exigés) ; (I4) fiche créée entre la revérification et la transaction → P2002 sur `create` (l.110), transaction annulée (sûr) mais 500 → 409 explicite. **Usage en prod** (I5, décision utilisateur en attente) : installer ne change pas la jouabilité des 5 avatars en scénario (Anastasia, ManFredK, Mar1na, MercureRealNews, Untergang), mais le réglage des effectifs les réintégrerait dans CAMP IA (exclusif) → injouables en plein scénario : les retirer du fichier tant qu'aucune protection n'est codée. Différable : alerte d'homonymie (`displayName` fichier ≠ zone), `eho_id` réécrit avec l'id de la zone, affichage de la zone d'origine et du nombre de membres touchés par « rendre exclusif », revérification fiche/`enabled` dans la transaction, état des groupes IA dans l'empreinte. Aucun code modifié.
