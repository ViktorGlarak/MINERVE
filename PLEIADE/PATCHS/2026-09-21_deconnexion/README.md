# Patchs « déconnexion complète » — 2026-09-21

Pour Xavier. Quatre commits prêts, un par dépôt, que je n'ai pas pu pousser :
GitHub refuse l'écriture au compte `ViktorGlarak` sur `app-press`, `app-admin`,
`app-cockpit` et `app-messagerie` (HTTP 403 « Write access to repository not
granted »). Le même correctif est **déjà en production sur `eho`** (`af91f31`,
`main` + `prod`).

## Le problème

`signOut` NextAuth ne ferme que la session de l'application. La session du
**royaume Keycloak** reste ouverte : « Se connecter » rouvre le même compte sans
rien demander, et il est impossible de changer de compte — sur un poste partagé
entre plusieurs joueurs, c'est bloquant. Pléiade (`/auth/logout`), LEAC et le
social (keycloak-js) faisaient déjà la déconnexion complète ; ces quatre apps
et eho, non.

## Le correctif (identique dans les quatre)

- `src/lib/deconnexion.ts` (nouveau, action serveur) : `signOut({ redirect:
  false })` puis redirection vers `PUBLIC_ISSUER/protocol/openid-connect/logout`
  avec `id_token_hint`, `client_id`, `post_logout_redirect_uri` (page de
  connexion, origine lue dans `X-Forwarded-*`).
- `src/lib/auth.ts` : le jeton d'identité est **gardé** dans le `jwt`
  (`token.idToken = account.id_token`) et exposé en `session.idToken` ;
  `PUBLIC_ISSUER` et `KC_CLIENT_ID` sont exportés.
- Boutons « Déconnexion » → `deconnexion()`.
- Rien d'autre : les variantes « Changer de compte » / « Se connecter avec un
  autre compte » ont existé quelques heures le 21/09 puis ont été retirées à la
  demande de l'utilisateur — un seul geste, « Se déconnecter », qui fonctionne
  vraiment.

## Vérifications faites

- eho : test navigateur de bout en bout (Playwright, Keycloak local,
  `joueur_test` / `anim_test`) — 10 contrôles sur 10, dont la session Keycloak
  orpheline (onglet fermé sans déconnexion).
- Les quatre apps : `tsc --noEmit` → compte d'erreurs **identique à la
  référence** (press 48 · admin 20 · cockpit 0 · messagerie 48, aucune dans les
  fichiers touchés) ; `next build` → **OK** pour les quatre.
- Serveur : `GET …/realms/delattre-26/protocol/openid-connect/logout?client_id=
  eho-eho-delattre26&post_logout_redirect_uri=https://…/login` → 302 vers
  `/login` : le motif `https://<app>/*` des clients couvre le retour.
- ⚠ `npm run lint` est cassé **à la référence** dans ces quatre dépôts (pas
  d'`eslint.config.*`, ESLint 9 renvoie son guide de migration). Pas touché.

## Application

```bash
cd app-press      && git am  ../PATCHS/2026-09-21_deconnexion/app-press.patch
cd app-admin      && git am  ../PATCHS/2026-09-21_deconnexion/app-admin.patch
cd app-cockpit    && git am  ../PATCHS/2026-09-21_deconnexion/app-cockpit.patch
cd app-messagerie && git am  ../PATCHS/2026-09-21_deconnexion/app-messagerie.patch
```

Bases inchangées : `app-press` `e8e22ee` · `app-admin` `036817b` · `app-cockpit` `ae5b70a`
· `app-messagerie` `082c095` (= `origin/main` du 2026-09-21).

⚠ **`app-messagerie` : `prod` a un commit absent de `main`** (`18b6648`,
« brider « au nom de » au camp du joueur », 2026-09-17). Le patch s'applique
sur `main` ; à toi de voir si `main` doit d'abord rattraper `prod`.

## Effet à connaître

Fermer la session de royaume déconnecte de **toutes** les apps de la zone en
même temps. Sur un poste partagé c'est l'effet voulu, et le social le faisait
déjà. Elle ne remonte **pas** à la session d'organisateur : Pléiade pose
désormais le fournisseur « cecpc » sans adresse de fin de session
(`b79cd5f`), et déclare l'adresse de retour de déconnexion sur le client
broker (`b8853e7`, `23f4f55`) — sans quoi la déconnexion finissait sur
« Invalid redirect uri » pour un compte entré par cecpc Connect.
