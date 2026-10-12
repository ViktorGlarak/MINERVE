---
name: feedback-tester-en-local-avant-push
description: "Avant tout push d'une app PLÉIADE, faire TOURNER l'image en local (base + volume réels) et rejouer l'opération de bout en bout — exigence absolue de l'utilisateur"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 699185de-99a6-4263-a321-d605be7e2b29
  modified: 2026-10-01T14:48:18.111Z
---

Règle imposée par l'utilisateur le 2026-10-01 : **tout doit être testé en local avant d'être poussé sur le serveur.**

**Why:** le 2026-10-01, après le push de l'eho `6451f97` (portraits intégrés à l'import), l'EHO de DE LATTRE 26 n'a plus répondu (404 pendant plus de 20 min). Les autres apps de la zone fonctionnaient. Ce qui avait été vérifié : la fonction seule (tsx), `tsc`, `npm test` et `docker build`. L'image n'avait **jamais été démarrée**, ni avec une base de données, ni avec un volume de données réaliste. Aucun import n'avait été rejoué dans l'app. En plus, j'ai écrit « l'image démarre » alors que je l'avais seulement construite : c'était faux. Xavier a dû prendre l'incident en main, et l'utilisateur a demandé de ne plus toucher à l'eho.

**How to apply:**
- Le build ne suffit pas. Avant tout push, faire `docker run` de l'image construite :
  - avec une base de données de test ;
  - avec un volume de données monté comme en prod (`/app/data`, propriétaire root, avec beaucoup de fichiers si l'app en a) ;
  - avec les variables d'environnement de la zone.
- Attendre que `/api/sante` (ou le healthcheck du catalogue) réponde **200**, et chronométrer le démarrage.
- **Rejouer l'opération réelle** dans l'app locale : l'import, l'export ou le clic concerné, avec le vrai fichier.
- Rendre compte exactement de ce qui a été testé et de ce qui ne l'a pas été. Ne jamais écrire « démarre » ou « fonctionne » sans l'avoir vu. Voir [[feedback-indicateur-etat]].
- Si l'environnement ne permet pas le test local, le dire et **demander** avant de pousser.
- **La règle a prouvé son utilité le jour même.** Le test local a montré que l'image eho `6451f97` ne démarrait pas : un accès disque à chemin dynamique sans `/* turbopackIgnore: true */` faisait embarquer tout le projet dans le standalone, dont `prisma7.config.ts`, et le `db push` de démarrage échouait.
- **Réflexe Next.js** : après tout ajout de `fs` ou `path` dans `src/`, lancer `docker run --rm --entrypoint sh IMAGE -c 'ls /app/*.config.* /app/src'`. Les deux doivent être absents.
- **Avant de pousser, toujours `git fetch`** et vérifier l'avance rapide sur `main` ET `prod`.
  - Le 2026-10-01, Xavier avait poussé un correctif **sur `prod` seulement** (`NODE_PATH` et CLI Prisma épinglé).
  - J'ai remis mes commits par-dessus les siens (rebase), puis refait le test local de l'image combinée **avant** de pousser.
  - Ne jamais forcer un push.
- Dans le test local, inclure un **`docker restart`** : la panne du 01/10 était une boucle au redémarrage.
- **Procédure eho locale** :
  - base de test : `docker exec eho-eho-db-1 mariadb …` (le client s'appelle `mariadb`, pas `mysql`) ;
  - lancement : `docker run -p 3910:3000 -v <scratch>/eho_data:/app/data -e DATABASE_URL=…host.docker.internal:3307/<base> -e PLEIADE_API_KEY=cle-essai -e AUTH_SECRET=… -e AUTH_TRUST_HOST=true` ;
  - appels : en-tête `X-API-Key: cle-essai` sur `/api/import`.
