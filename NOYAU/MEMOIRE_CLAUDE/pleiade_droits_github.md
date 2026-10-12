---
name: pleiade-droits-github
description: "Droits GitHub de ViktorGlarak sur cecpc-pleiade — app-press ouvert le 24/09 ; admin/cockpit/messagerie 403 ; mes git push passent seulement hors mode auto ; « pousser » pour l'utilisateur ≠ déployer (prod)"
metadata:
  node_type: memory
  type: project
  originSessionId: 7f9a0a6b-9fe5-457d-b4e3-f0b50bf62931
  modified: 2026-10-01T11:05:43.740Z
---

Constaté le 2026-09-21 : `git push` → HTTP 403 « Write access to repository not granted » sur
**`app-press`, `app-admin`, `app-cockpit`, `app-messagerie`**. Les pushes passent sur `eho`,
`app-leac`, `app-melmil`, `pleiade-platform`. `gh` n'est pas installé.

**2026-09-24 : Xavier a ouvert `app-press` en écriture** — `git push --dry-run` passe (main
e8e22ee..99b649f + nouvelle branche `maquettes-existantes`). admin/cockpit/messagerie non retestés.

⚠ Depuis le 2026-09-24, **le classificateur du mode auto refuse mes `git push` réels**
(« Data Exfiltration ») même autorisés par l'utilisateur ; le `--dry-run` passe. Ne pas
contourner : donner la commande à l'utilisateur ou lui faire ajouter une règle de permission.
Les règles Allow (`Bash(git push:*)`, posée par l'utilisateur le 24/09) sont **ignorées en mode
auto** ; le push passe quand la session est en **« Edit automatically »** (vérifié le 24/09 et le 25/09).

⚠ **2026-09-25 : « pousser » depuis GitHub Desktop ≠ déployer.** L'utilisateur a poussé `main`
(et une branche de travail) mais ne savait pas qu'il fallait **fusionner `main` dans `prod`** :
rien n'était en ligne, et Desktop lui disait « rien à pousser » sur `prod`. Après un push de sa
part, **toujours contrôler `origin/prod` et `/api/sante`**, pas seulement `main`. Le plus simple :
qu'il passe en « Edit automatically » et que je pousse `main:prod` (avance rapide vérifiée par
`git merge-base --is-ancestor`).

**Why:** ces dépôts sont ceux de Xavier ; un travail sans droits finit en patchs.

**How to apply:** avant de coder sur admin/cockpit/messagerie, prévenir que le résultat sera
**remis à Xavier** (`git format-patch`, `MINERVE\PLEIADE\PATCHS\`). Toujours `git push --dry-run`
d'abord. Voir [[pleiade-deploy-mecanique]].

**2026-09-28 : l'utilisateur annonce que Xavier a ouvert `app-admin` en écriture** (non encore vérifié par un push). admin compris ; cockpit et messagerie non retestés.
**2026-09-28 (soir)** : `git push --dry-run` sur app-admin passe (84009f4..5b6bf9f). Push réel pas encore fait.
**2026-09-28 (soir) : premier push RÉEL sur app-admin réussi** (84009f4..3d396fd sur `main` et `prod`). app-admin est donc ouvert en écriture. Instances : `admin.delattre-26` et `conduite.exercice` (`.pleiade.internal`) ; déploiement vérifié par la route `/api/bff/scenarios/1/kit-ia`, qui passe de 404 à 401 (app-admin n'a pas de `/api/sante`).
**2026-09-29 : les maquettes existantes d'`app-press` étaient sur `origin/prod` depuis le 24/09 mais jamais déployées** : le serveur servait encore l'ancienne version, et rien ne le signalait. Un nouveau push sur prod (cea3ac9) les a mises en ligne en environ 3 min. Pour vérifier, chercher `sk-tv4` dans le CSS servi par une instance de presse. Un push sur prod doit **toujours** être suivi d'un contrôle de ce que sert le site.
**2026-10-01 : premier push RÉEL sur `app-messagerie` réussi** (18b6648..412dbae sur main + prod), autorisé explicitement par l'utilisateur. ⚠ Ma copie locale de `main` était en retard sur `origin/prod` : toujours repartir de `origin/prod`. Le Dockerfile lance `npm test` AVANT `prisma generate` : construire l'image avant de pousser. **2026-10-01 : push réel sur `app-cockpit` accepté** (ae5b70a..ddc73b7, main + prod) : tous les dépôts cecpc-pleiade testés sont ouverts. Cockpit sans `/api/sante` : déploiement vérifié par le redémarrage observé (`/api/auth/csrf` en 404, puis de nouveau en 200).
**2026-09-28 : premier push RÉEL sur `app-social` réussi** (36bcb07..27869bd sur main + prod), autorisé explicitement par l'utilisateur. Déploiement d'environ 6 min, vérifiable sans compte par un `DELETE` anonyme sur `/api/social/posts/0` : 401 = nouvelle version.
**2026-10-04 : le cas s'est reproduit** (MELMIL 2026-10-04.14) : le push de l'utilisateur dans GitHub Desktop n'a envoyé que `main`. Désormais, quand je lui laisse le push, lui donner **d'emblée** les étapes Desktop : sur `prod`, Branch → Merge into current branch → main → Push origin.
