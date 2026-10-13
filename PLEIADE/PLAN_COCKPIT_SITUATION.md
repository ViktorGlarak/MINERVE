# Plan — Refonte de la vue principale du Cockpit (Situation · À traiter · Projection)

> Rédigé le 2026-10-13. Sources :
> - avis DESIGNER n°105 et ses arbitrages (`DESIGNER\AVIS\2026-10-13_COCKPIT_VUE_PRINCIPALE\AVIS.md` §8) ;
> - avis CYBERSECU du 2026-10-13, conditions **K1 à K13** (`CYBERSECU\MEMOIRE.md` §4 et §9) ;
> - relevé du code de `app-cockpit`, `app-social`, `app-press`, `app-messagerie`, `eho` et `app-admin`.
>
> Maquettes de référence : `C:\CECPC\pleiade\dev\maquettes-cockpit\` (`node serveur.mjs`, http://127.0.0.1:4100/).
>
> Règles de chaque lot : essai en local, puis feu vert de l'utilisateur **pour chaque dépôt** avant le push sur `prod`, puis vérification de `/api/sante` ou de la page.

---

## 1. Point de départ (ce que le code montre)

| Constat | Conséquence |
|---|---|
| Catégories, sources, non-lus et disposition sont **dans le stockage du navigateur** (`ck_*`). Le Cockpit n'a **ni base de données ni tests**. | Impossible de partager une catégorie avec la cellule, ou de noter un « dernier passage » par animateur, sans persistance serveur. |
| Un groupe eho est **copié membre par membre** en sources (FORAD = 1 889 cartes). | Les membres ajoutés plus tard ne sont pas suivis. L'écran est illisible. |
| Le navigateur relance `poll` **toutes les 10 s**, et le serveur fait alors **un appel `accounts/lookup` par avatar**. | Des milliers d'appels toutes les 10 s : la nouvelle vue ne peut pas reposer sur ce mécanisme. |
| Seul le **réseau social public** est lu. Le type de contenu (`Toot`) est propre au social. | Il faut un type de contenu générique et des connecteurs par canal. |
| Social : les réactions sont **horodatées en base mais jamais exposées** ; les partages sont **désactivés** ; aucune route ne donne les abonnés. | « Qui pèse » demande une nouvelle route. Le poids s'écrit **réponse ×3 + j'aime ×1** (partage ×2 dès qu'ils seront réactivés). |
| Le **Chat** du social : le schéma dit « rien n'en sort (fil, Cockpit, reporting) ». La route existante pour le moteur IA rend le contenu, sans journal. | Décision de l'utilisateur à prendre (§5) ; la route existante est à borner (K8). |
| **Presse** : `retex` donne les articles ; `viewCount` n'est jamais incrémenté. | On compte les articles et les commentaires. Les lectures ne sont pas disponibles. |
| **Messagerie** : de type Telegram (canaux, groupes, conversations privées), **pas de courriels**. Elle a déjà les rôles `animateur` et `superviseur` ; seul le superviseur lit le privé. | Les maquettes disent « courriels » : à remplacer par « messages ». La règle du superviseur est conservée. |
| eho : pas de résolution en lot ; pas de notion de cellule (la cellule vient des groupes Keycloak, via `app-admin`). | Il faut une route de résolution en lot dans eho. La cellule est lue chez `app-admin`. |

---

## 2. Architecture cible

```
 navigateur (Situation / À traiter / Projection)
      │  1 requête toutes les 15 s, déjà agrégée
      ▼
 app-cockpit — BFF + base propre (MariaDB de la plateforme, Prisma)
   ├─ Categorie       règle (groupe eho par id, camp, cellule, compte, hashtag ; exclusions ; canaux ; alerte ; partage)
   ├─ Passage         dernier passage par animateur (sub Keycloak)
   ├─ Evenement       index de MÉTADONNÉES : app, canal, id, auteur (identity_id), heure, hashtags, réponse_à, privé o/n
   ├─ Reaction        réaction reçue : auteur visé, type, heure (pour « qui pèse »)
   ├─ Resolution      cache identity_id → groupes, camp, cellule, comptes (5 min)
   └─ Collecteur      toutes les 30 à 60 s, appelle chaque app : evenements?depuis=dernier_curseur
      │  clé de zone, métadonnées seulement (K7)
      ▼
 app-social · app-press · app-messagerie   (nouvelles routes de service evenements / reactions)
 eho (resolution en lot) · app-admin (cellules)
```

**Principes**
- **Le Cockpit stocke des métadonnées, jamais de texte** (K6). Le texte d'un contenu public est relu à la demande, au clic, par les routes unitaires existantes (`posts/:id`…). Le texte privé n'est **jamais** lu par le Cockpit en v1 : un lien profond ouvre la supervision de l'app source (K5).
- **Tous les compteurs se calculent en SQL sur la table locale.** Cela couvre catégorie × canal depuis T, la flambée (rythme comparé aux 2 h précédentes), les tendances et le poids. Le serveur ne dépend plus du nombre d'avatars. Un contenu présent dans deux catégories est compté une fois par catégorie, et une seule fois dans le total.
- **Une catégorie est une règle**, résolue côté serveur. Un groupe eho est suivi **par son identifiant**.
- **Canal injoignable** : le collecteur note le dernier succès de chaque app. L'écran affiche « ✕ injoignable depuis HH:MM », jamais 0 (K9).
- **Rétention** : 14 jours au plus, purge avec la zone, sauvegardes comprises (K12).

---

## 3. Lots

### Lot 0 — Décisions préalables (utilisateur)
Voir §5. Sans réponse aux questions 1 et 2, le lot 4 ne démarre pas.

### Lot 1 — Socle du Cockpit (dépôt `app-cockpit`, plus le catalogue `pleiade-platform` pour la base)
1. **Base propre** (Prisma, MariaDB de la plateforme, comme `app-ia`) : modèles `Categorie`, `Passage`, `Evenement`, `Reaction`, `Resolution`, `EtatCanal`. Déclaration de la base dans le catalogue (PLEIADE).
2. **Tests** : mise en place de `npm test` (aujourd'hui absent), avec la résolution des règles, les compteurs, la flambée et la validation des catégories (K11 : 50 règles au plus, formats contrôlés, 2 Mo au plus).
3. **BFF** :
   - `requireBearer` + rôle nommé (K9) ;
   - cellule déduite du jeton, jamais d'un paramètre (K11) ;
   - routes `categories` (CRUD, auteur `sub`, modification journalisée), `passage` (lire et « J'ai fait le point »), `situation?depuis=` (grille + bandeau + tendances + qui pèse), `a-traiter` (liste triée, regroupements).
4. **Migration** : à la première ouverture, proposer d'importer les catégories et sources du navigateur (sources `persona` d'un même groupe → **une** règle « groupe eho ») et les espaces partagés de l'Admin.

*Livrable* : socle testé, sans changement visible.

### Lot 2 — Réseau social public (dépôts `app-social` puis `app-cockpit`) — ⭐ premier lot utile
1. `app-social` :
   - route `GET /api/service/evenements?depuis=&curseur=&limite=` : publications et commentaires publics parus (`scheduledAt` passé, programmés exclus), champs explicites sans texte ;
   - route `GET /api/service/reactions?depuis=` : j'aime et réponses reçus, par auteur visé ;
   - index sur `createdAt` (`social_posts`, `social_likes`) ;
   - garde et matrice de tests K7.
2. `eho` : `POST /api/service/resolution` (liste d'`identity_id` → groupes, camp, appropriation). Lu par paquets, mis en cache.
3. `app-cockpit` :
   - collecteur social ;
   - **page Situation** (bandeau « Ce qui a changé », grille catégories × canaux avec une seule colonne active « Réseau social », Tendances, Qui pèse, État des canaux, volet non modal) ;
   - **onglet À traiter** (rail, liste triée par importance, rafales regroupées, panneau de lecture, Vu / À suivre / Signaler) ;
   - fenêtre « Nouvelle catégorie de suivi » avec les modèles et le premier écran.
   - Les colonnes Chat, Presse et Messagerie restent visibles, grisées, avec la mention « bientôt ».
4. **L'ancienne vue reste accessible** pendant la transition, via le menu ⋯ > « Ancienne vue » (à retirer au lot 5).

*Livrable* : on remplace l'écran illisible par la Situation, sur le réseau social. **À essayer en exercice avant la suite.**

### Lot 3 — Presse (dépôts `app-press` puis `app-cockpit`)
- `app-press` : `GET /api/service/evenements?depuis=` (articles publiés, commentaires, entrées de direct ; auteur, heure), sans texte.
- `app-cockpit` : colonne Presse active ; volet de lecture des articles par la route unitaire existante.
- Option : compter réellement les lectures (`viewCount`) si l'on veut cet indicateur.

### Lot 4 — Chat et messagerie, en métadonnées (dépôts `app-social`, `app-messagerie`, `app-cockpit`, Keycloak)
1. `app-messagerie` :
   - `GET /api/service/meta?depuis=` (conversation, type canal/groupe/direct, expéditeur par nom d'avatar, heure, réponse ou transfert), **sans aucun champ de contenu** (K2, K7) ;
   - route `retex` alignée sur le contrat commun.
2. `app-social` :
   - `GET /api/service/chat/meta?depuis=` sur le même modèle, ce qui suppose de lever la règle du schéma (question 1, §5) ;
   - **borner** `chat/messages` aux membres de CAMP IA (K8) ;
   - créer une **page de supervision du Chat** sous le rôle `superviseur`, avec un motif obligatoire et un journal d'accès non modifiable (K3, K4).
3. `app-cockpit` :
   - colonnes Chat et Messagerie actives : volumes, interlocuteurs par nom d'avatar ;
   - au clic, « Ouvrir dans la supervision ↗ », visible seulement pour le rôle `superviseur` (K1, K5) ;
   - aucun texte privé ne passe par le Cockpit.
4. Keycloak : rôle `superviseur` attribué nominativement (question 2).
5. Mention de supervision dans le Chat et la messagerie (K13).

### Lot 5 — Projection, finitions, retrait de l'ancienne vue (dépôt `app-cockpit`)
- **Projection grand écran** : menu ⋯ > « Projection grand écran », nouvel onglet, session Keycloak normale, sans lien à jeton.
  - Uniquement du public et des agrégats ; « Message privé » sans interlocuteurs ; programmés exclus.
  - Bouton « retirer de la projection » (K10).
- Raccourcis clavier J, K et V ; « Tout marquer vu jusqu'ici ».
- Retrait de l'ancienne vue, du `poll` toutes les 10 s et des lookups unitaires.
- Notes de version ; journal PLEIADE ; mémoires DESIGNER et CYBERSECU.

---

## 4. Ce qui est repris de l'existant
- `GrapheTemps` (fiche de catégorie) ;
- Tendances avec ↩ commentaires ;
- `TootItem` (variante panneau) ;
- `SidePanel` (pile d'historique) ;
- `MenuFixe` (Échap, clic extérieur, focus rendu) ;
- les groupes eho portés par le Reporting (`eho: <id>`), déjà relus à chaque calcul : c'est l'embryon de la catégorie-règle, à basculer côté serveur ;
- les espaces de l'Admin (P8), importés au lot 1.

## 5. Questions pour l'utilisateur
1. **Chat du réseau social** : le code dit aujourd'hui « rien n'en sort vers le Cockpit ». Accepte-t-on d'en sortir les **métadonnées seulement** (volumes, interlocuteurs par nom d'avatar, heure) ? *Recommandé : oui.*
2. **Rôle `superviseur`** (seul habilité à lire le contenu privé, avec motif et journal) : à qui l'attribuer ? *Recommandé : 1 ou 2 personnes nommément, pas toute la cellule.*
3. **Joueurs informés** de la supervision des échanges privés (au briefing et par une mention dans les apps), condition K13 : d'accord ?
4. **Mot-clé** dans les règles de catégorie : il oblige à indexer du texte. *Recommandé : plus tard ; la v1 couvre groupe eho, camp, cellule, compte et hashtag.*

### Réponses de l'utilisateur (2026-10-13)
1. **Métadonnées du Chat vers le Cockpit : OUI** (pas le contenu).
2. **Rôle superviseur** : l'utilisateur propose de le lier aux groupes Keycloak, comme la case « Veille » (rôle `analyste` du catalogue `cockpit.yml`, cochée par groupe sur la plateforme). Recommandation : **même mécanisme, mais une seconde case « Supervision »** pour le Cockpit, à côté de « Veille ». Elle suit le modèle de la messagerie (`messagerie.yml` : Animation / Supervision). Sinon, toute personne en veille lirait les messages privés. *En attente de confirmation.*
3. **Information des joueurs** : explication demandée. *En attente.*
4. **Mot-clé : reporté** ; la v1 couvre groupe eho, camp, cellule, compte et hashtag.

## 6. Agents et dépôts concernés
| Lot | Dépôts | Agents |
|---|---|---|
| 1 | `app-cockpit`, `pleiade-platform` (base) | PLEIADE, ARCHITECTE, CYBERSECU (K6, K9, K11) |
| 2 | `app-social`, `eho`, `app-cockpit` | PLEIADE, MASTORION, DESIGNER, CYBERSECU (K7) |
| 3 | `app-press`, `app-cockpit` | PLEIADE, DESIGNER |
| 4 | `app-messagerie`, `app-social`, `app-cockpit`, Keycloak | PLEIADE, MASTORION, CYBERSECU (K1 à K5, K8, K13) |
| 5 | `app-cockpit` | DESIGNER, CYBERSECU (K10) |
