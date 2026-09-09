# MISSION — App EHO de MASTORION : modèles de départ, double vue animateur/joueurs, EHO collaboratif

Tu interviens sur **MASTORION**, une plateforme de réseau social fictif servant à l'entraînement
militaire (exercices d'influence). Je suis le concepteur de l'exercice, pas un développeur : explique
tes choix en français simple, et signale-moi tout ce qui mérite un arbitrage plutôt que de trancher seul.

---

## 0. Où travailler — à vérifier AVANT toute chose

| | |
|---|---|
| Dépôt (clone d'exécution) | `C:\CECPC\MASTORION\mastorion-v0` |
| Branche de travail | `feat/eho` (déjà créée, déjà poussée sur `origin`) |
| ⚠ Ne PAS utiliser | `D:\CECPC\MASTORION\mastorion-v0` — le disque D: est en **exFAT**, `npm install` y échoue (symlinks EISDIR). C'est une copie de référence, on n'y exécute rien. |
| Lancer la stack | `npx turbo dev --filter='!docs'` à la racine |
| ⚠ Pourquoi ce filtre | l'app `docs` réclame le port **4203 en dur**, déjà pris par `sentinel-ui` ; comme **turbo abat tout le pipeline dès qu'une tâche échoue**, sans le filtre c'est TOUTE la stack (API comprise) qui tombe. |
| Base de données | conteneur Docker `mastorion-db` (MariaDB 11, port 3306, user/mdp/base `mastorion`). Doit tourner. |
| Compte de test | `test@test.fr` / `password123` (rôle `APP_ADMIN`) |
| Ports | web 4200 · admin 4201 · cockpit 4202 · docs/sentinel 4203 · **eho 4204** · API 3000 |

⚠ **`prisma migrate` est inutilisable sur ce dépôt** : `migration_lock.toml` déclare `sqlite` alors que
le schéma est `mysql` (défaut présent dès le commit initial). `prisma migrate status` échoue en **P3019**
et Prisma te conseillera de « supprimer le dossier de migrations » — **ne le fais jamais**. Le projet
fonctionne au `db push`. Pour vérifier le schéma sans risque : comparer le nombre de `model` du schéma
au nombre de tables réelles (`SELECT COUNT(*) FROM information_schema.tables WHERE table_schema='mastorion'`).

---

## 1. Ce qui existe déjà (ne pas refaire)

L'app **`apps/eho`** (Angular 21 standalone + PrimeNG/Aura, port 4204) existe et fonctionne. Elle a été
calquée fichier par fichier sur `apps/admin` — respecte les mêmes conventions.

```
apps/eho/src/app/
  app.routes.ts · app.config.ts · app.ts
  guards/auth.guard.ts                  (exige APP_ADMIN)
  services/auth.service.ts              (clés localStorage : eho_token / eho_user)
  services/auth.interceptor.ts
  services/eho.service.ts               (enveloppe les endpoints /api/admin existants)
  pages/login/login.ts
  pages/avatars/avatars.ts              (formulaire de création d'un persona)
  pages/trombinoscope/trombinoscope.ts  (page d'accueil actuelle)
```

**Le trombinoscope** affiche les personas en cartes rondes groupées **par pays** puis **par fonction**,
avec les palettes exactes des planches d'exercice MASTAURIGE (Mercure `#8B0000` · Arnland `#2B5BA0` ·
Bothnia `#1C5E2F` · accents `#C4A000` / `#E8D040` / `#C41E3A`). Chaque carte montre nom, **fonction**
(« Président de la République »), handle et portrait ou initiales. Les cartes d'un bloc sont classées
**hiérarchiquement** (chef d'État → chef de gouvernement → ministres → états-majors → gouverneurs →
justice → unités → porte-parole → **opposition en dernier**), les dirigeants ayant une carte mise en
avant et l'opposition un liseré distinct. Un clic ouvre la fiche complète.

**Conserve tout cela** : c'est validé. Tu le réorganises, tu ne le réécris pas.

### Données actuellement en base

**452 personas** (⚠ pas 404 — le chiffre a changé, ne le code jamais en dur), **112 portraits**,
**56 groupes**. Répartition : Arnland 243 · Mercure 110 · France 55 · Bothnia 37 · sans pays 11.

### Endpoints API déjà disponibles (aucun nouveau n'a été nécessaire jusqu'ici)

```
GET    /api/admin/users            (?search= &limit= &offset= — renvoie {items,total})
POST   /api/admin/users            (identité seule : username, email, password, display_name)
PATCH  /api/admin/users/:id        (champs de fiche + avatar_url)
PATCH  /api/admin/users/:id/groups
DELETE /api/admin/users/:id
GET    /api/admin/groups   ·  POST /api/admin/groups  ·  DELETE /api/admin/groups/:id
POST   /api/admin/users/upload-avatar   → { url: "/api/uploads/users/<fichier>" }
GET    /api/admin/users/field-values?field=pays
POST   /api/admin/users/import          ( { users: [...], groups: [...] } )
GET    /api/admin/users/export
```

⚠ La création se fait **en deux temps** : `POST` n'accepte que l'identité, les champs de fiche
passent ensuite par un `PATCH`. C'est le comportement de l'API, pas une limitation à corriger.

### Champs de fiche EHO (déjà présents sur le modèle `User` — aucune colonne à ajouter)

`age · genre · pays · label · origine · religion · situation · caractere · langage · activite ·
observations · qualifications · aime · deteste · bio · avatar_url`

---

## 2. Contraintes NON NÉGOCIABLES

1. **MASTORION est en production. Sois le moins destructif possible sur le schéma.**
   Tu peux **ajouter** des tables ; tu ne **modifies ni ne supprimes jamais** une table ou une colonne
   existante. Toute migration doit m'être présentée AVANT d'être appliquée.

2. **Les fiches écrites par les joueurs ne doivent JAMAIS modifier les fiches officielles.**
   C'est le point le plus important du projet. L'isolation doit être garantie **côté serveur**
   (les endpoints joueurs n'écrivent que dans les tables joueurs), pas seulement par une UI en lecture seule.

3. **La vue comparative animateur ne doit pas être atteignable par un joueur.**
   À garantir par **l'autorisation d'API**, jamais par un simple masquage de bouton dans l'interface.

4. **Ne jamais laisser deux fiches partager `email` ou `masto_id`.** L'import remonte par `masto_id`
   puis par `email` : deux fiches qui partagent l'un des deux sont **fusionnées en silence**, et l'une
   disparaît sans aucun avertissement. Cela s'est déjà produit et a fait perdre un compte joué en exercice.

5. **`username` : ASCII strict** (`[a-z0-9_]`). Un handle accentué a déjà pollué la base.

6. **Ne change pas le schéma de `username` des personas existants** : les portraits sont rattachés aux
   identifiants en base, un renommage en masse crée des doublons et orpheline les photos.

---

## 3. Ce qu'il faut construire

### 3.1 — Écran d'accueil : choix du modèle d'EHO

Avant toute chose, l'utilisateur choisit un **modèle**. Deux pour l'instant, l'architecture doit en
accepter d'autres sans retouche de code :

| Modèle | Contenu |
|---|---|
| **SKOLKAN PERSONA** | l'EHO complet actuel — les 452 personas avec portraits, fiches bio, pays, fonctions, groupes |
| **VIERGE** | rien. L'administrateur crée ses personas et ses groupes à la main, ou importe un classeur Excel. |

Conçois le catalogue de modèles comme une **donnée**, pas comme du code en dur : ajouter un futur modèle
doit être une opération de contenu.

### 3.2 — Ce que « choisir un modèle » provoque

Le choix **approvisionne MASTORION** : avec VIERGE, le panneau d'administration de MASTORION est vide
d'avatars et de groupes ; avec SKOLKAN PERSONA, il contient les 452 personas.

⚠ **C'est l'opération la plus dangereuse du projet** — elle peut effacer des données réelles. Exigences :

- Elle doit être **explicite, confirmée**, jamais déclenchée par un simple clic de navigation.
- Elle ne doit **jamais supprimer les comptes humains** (administrateurs, animateurs, joueurs) : elle ne
  touche qu'aux personas d'exercice.
- Elle doit être **réversible** : sauvegarde préalable automatique. Un outillage existe déjà dans
  `C:\CECPC\MASTORION\SAUVEGARDES\` (`BASE_VIERGE.sql`, `SAUVEGARDER.bat`, `RESTAURER.bat`) —
  inspire-t'en ou intègre-le.
- Propose-moi le mécanisme **avant** de l'implémenter.

### 3.3 — Deux modes d'ouverture : animateur et joueur

- **Mode animateur/admin** : l'EHO officiel, la création de personas, la vue comparative.
- **Mode joueur** : uniquement *son* EHO, qu'il peut annoter et réorganiser.

Le mode doit découler du **rôle du compte**, pas d'un sélecteur que le joueur pourrait forcer.
Bonne nouvelle : dans le schéma, `role` est une **chaîne libre** (`role String // "APP_ADMIN", etc.`,
table `user_roles`) — introduire un rôle joueur ne demande donc **aucune migration**. Les rôles déjà
utilisés sont `APP_ADMIN` et `COCKPIT`.

### 3.4 — Vue joueur

Le joueur part de l'EHO du modèle choisi, en version **basique** (les personas, sans le renseignement
officiel). Au fil de l'exercice, en observant ce que les personas publient sur MASTORION, il :

- **rédige ses propres fiches** — son analyse, forcément différente de la fiche officielle. Ces fiches
  lui appartiennent et **n'altèrent jamais** les données officielles ;
- **déplace les cartes** — s'il estime qu'un persona penche davantage vers l'Arnland que vers Mercure,
  il le range là. Ce déplacement ne modifie **ni** les données officielles, **ni** la vue animateur,
  **ni** l'EHO des autres joueurs.

Le joueur **ne voit aucune comparaison** : il n'a accès qu'à son propre EHO.

Décide, et explique-moi ton choix : un EHO **par joueur** ou **par équipe** ? (l'entraînement se fait
en cellules, plusieurs analystes travaillent souvent ensemble — je penche pour l'équipe, tranche et dis-moi).

### 3.5 — Vue animateur : la comparaison

C'est la valeur pédagogique du dispositif. L'animateur doit voir **où les joueurs se trompent** :

- fiche officielle et fiche joueur **côte à côte**, écarts mis en évidence ;
- les **déplacements de cartes** : quel persona a été rattaché au mauvais camp ou au mauvais pays ;
- une **vue d'ensemble** : quels personas sont les plus mal lus, quelles manœuvres d'influence ont
  fonctionné. C'est ce qui permet de dire si les entraînés « sont dans le bon ou non ».

Conçois cette synthèse pour qu'elle se lise **d'un coup d'œil**, pas comme un tableau à éplucher.

### 3.6 — À terme, l'app EHO devient propriétaire des personas

À terme, ce n'est plus le panneau d'administration de MASTORION qui gérera la création des avatars et
des groupes, mais **cette application**. Conçois-la dans cet esprit dès maintenant, pour éviter que les
deux outils ne se marchent dessus plus tard. Tu n'as pas à retirer les fonctions de l'admin aujourd'hui,
mais l'app EHO doit pouvoir tout faire : créer, modifier, grouper, importer, exporter, photographier.

---

## 4. Exigences de design

Je veux un **niveau professionnel**, moderne, fluide et performant. L'outil sera projeté devant des
officiers et manipulé sous pression pendant un exercice.

- L'esthétique existante des planches d'exercice est la référence : palettes par pays, cartes rondes,
  hiérarchie visuelle claire entre dirigeants, cadres et opposition. **Ne la dilue pas.**
- La lisibilité prime sur l'effet : on doit distinguer instantanément un pays, une fonction, un camp.
- **452 cartes doivent défiler sans saccade** — soigne les performances (virtualisation, `trackBy`,
  images dimensionnées). Le glisser-déposer doit être fluide, avec un retour visuel net.
- Pense les états vides : le modèle VIERGE affiche un EHO sans aucune carte, il doit guider l'utilisateur
  vers la création ou l'import plutôt que de présenter une page morte.
- Accessibilité au clavier pour le glisser-déposer (tout le monde n'aura pas une souris confortable).

---

## 5. La vraie question d'architecture : où stocker le travail des joueurs

Les fiches et les placements des joueurs doivent être **côté serveur** — sinon l'animateur ne peut rien
comparer, et un simple changement de navigateur effacerait le travail d'une cellule. `localStorage` ne
convient donc pas comme stockage principal.

Cela implique des **tables nouvelles**. C'est acceptable au regard de la contrainte 2.1 — ajouter est
non destructif — mais :

- **uniquement de l'ajout** : aucune table ni colonne existante n'est modifiée ;
- **présente-moi le schéma proposé avant de l'appliquer**, avec ce que chaque table stocke et pourquoi ;
- une fiche joueur doit référencer le persona officiel **sans jamais pouvoir l'écraser**.

Si tu vois une solution plus légère qui satisfait la comparaison animateur, propose-la : je préfère
l'option la plus simple qui fasse le travail.

---

## 6. Méthode attendue

1. **Commence par explorer** le dépôt et l'app `apps/eho` existante avant d'écrire quoi que ce soit.
2. **Présente-moi ton plan** — architecture, migration éventuelle, découpage des écrans — et attends
   mon accord sur les points signalés « à m'arbitrer ». Ne pars pas tête baissée.
3. Implémente par étapes vérifiables. Après chaque étape : `npx ng build` doit passer **sans erreur**,
   et tu vérifies le rendu réel, pas seulement la compilation.
4. **Vérifie sur les données réelles** : 452 personas, 5 pays, portraits présents ou absents. Un
   « ça compile » ne prouve rien.
5. Commits clairs sur `feat/eho`, poussés sur `origin`. Termine chaque message de commit par :
   `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>`
6. **Signale-moi tout ce que tu n'as pas pu faire** plutôt que de réduire le périmètre en silence.

---

## 7. Points sur lesquels je veux ton avis avant que tu codes

1. **EHO joueur : individuel ou par équipe ?** (je penche pour l'équipe — tranche et argumente)
2. **Le schéma de stockage** des fiches et placements joueurs.
3. **Le mécanisme d'application d'un modèle** : comment garantir qu'il n'efface jamais rien d'important.
4. **Le rôle joueur** : nom retenu, et comment un joueur obtient son compte.
5. Ce que doit contenir l'EHO joueur « basique » au départ : nom et portrait seulement ? la fonction
   aussi ? (attention : trop d'information officielle offerte d'emblée ruine l'exercice d'analyse)

---

## 8. Deux précisions à ne pas manquer

- Le chiffre **404 personas** que j'ai pu citer est **périmé** : il y en a **452**. Ne code aucun total en dur.
- Une de mes phrases était incomplète : « je souhaite que si le model vierge. » Je voulais dire que
  **si le modèle VIERGE est choisi, l'EHO s'affiche vide** et que tout se crée depuis l'application.
  Confirme que c'est bien ainsi que tu l'as compris.
