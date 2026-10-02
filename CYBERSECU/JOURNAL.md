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
