# Plan — Refonte de la vue principale du Cockpit (Situation · À traiter · Projection)

> Rédigé le 2026-10-13. Sources :
> - avis DESIGNER n°105 et ses arbitrages (`DESIGNER\AVIS\2026-10-13_COCKPIT_VUE_PRINCIPALE\AVIS.md` §8) ;
> - avis CYBERSECU du 2026-10-13, conditions **K1 à K13** (`CYBERSECU\MEMOIRE.md` §4 et §9) ;
> - relevé du code de `app-cockpit`, `app-social`, `app-press`, `app-messagerie`, `eho` et `app-admin`.
>
> Maquettes de référence : `C:\CECPC\pleiade\dev\maquettes-cockpit\` (`node serveur.mjs`, http://127.0.0.1:4100/).
>
> Règles de chaque lot : essai en local, puis feu vert de l'utilisateur **pour chaque dépôt** avant le push sur `prod`, puis vérification de `/api/sante` ou de la page.


> ▶️ **CHANTIER REPRIS le 2026-10-14** (demande de l'utilisateur). Réponses : **vues enregistrées = oui, intéressant** (basculer entre plusieurs configurations de catégories) ; **go pour le lot 3**.
> **Lot 3 (presse) PRÊT EN LOCAL, non poussé** : `app-press` `93b3ae1` (routes `evenements`, `reactions`, `contenus`), `app-cockpit` `abe6a8e` (collecte social + presse, volet et À traiter). Ordre de mise en production : **presse d'abord, puis Cockpit** (push refusé en mode auto : à lancer par l'utilisateur).
> **Vues enregistrées FAITES en local** (`app-cockpit` branche `vues` `ed3794b` + `9a8558d`) ; **Reporting** : « Groupes comparatifs » retirés (demande utilisateur), une courbe par catégorie de la vue active. Prochain : lot 4.
>
> *(Historique)* ⏸️ Chantier en pause du 2026-10-13 au soir au 2026-10-14.
> **En production** (DELATTRE 26) : lots 1 et 2 ; partage « Toute l'animation de la zone » ; même en-tête pour le Reporting ; Reporting branché sur les catégories de suivi (`app-cockpit` `b0dbfa0`, vérifié par `/api/bff/situation/series-reporting` → 401) ; plateforme `b6f128f` ; réseau social `0e35443` ; eho `2026-10-13.1`.
> **À la reprise, dans l'ordre proposé** :
> 1. Vérifier avec l'utilisateur ce qu'il a vu à l'écran (catégories créées, collecteur « lu à l'instant »).
> 2. Les « vues enregistrées » (équivalent des espaces de travail) : question posée, sans réponse — partager (déjà couvert) ou basculer entre configurations ?
> 3. Lot 3 (presse) ; lot 4 (Chat et messagerie en métadonnées + supervision, case « Supervision » à côté de « Veille ») ; lot 5 (projection, retrait de l'ancien écran).
> 4. Conversations privées entre joueurs (après le lot 4 ; question : un avatar incarné par l'animation est-il humain ?).
> 5. Reporting : règles camp et cellule pas encore comptées (signalées en orange).
> **État technique à connaître** : branches `situation` dans `app-cockpit`, `app-social`, `eho` (toutes fusionnées dans main/prod) ; copie de travail `C:\CECPC\pleiade\wt-platform-situation` (branche `situation` = main de la plateforme) ; la zone locale `ia-locale` tourne sur les images `situation-essai` du social, d'eho et du Cockpit ; scripts d'essai dans le dossier temporaire de session (non conservés).


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
3. **Information des joueurs : OUI** (2026-10-13). Une phrase au briefing ou dans les consignes d'exercice (« tous les échanges sur les outils de l'exercice, y compris privés, peuvent être lus par l'animation et servir au RETEX »), plus une mention discrète dans le Chat et la messagerie au lot 4 (K13).
4. **Mot-clé : reporté** ; la v1 couvre groupe eho, camp, cellule, compte et hashtag.

### Idée de l'utilisateur à instruire (2026-10-13) — « conversation entre joueurs uniquement »
Les joueurs pourraient rendre **privée** une conversation (à deux, en groupe, ou un canal) **dès lors que 100 % des membres sont humains** (aucun avatar animé, IA ou animateur). Le contenu n'est alors lisible par personne côté animation, superviseur compris.
- **À trancher** :
  - « humain » = compte de joueur, pas un avatar incarné par l'animation ni un avatar IA (critère fiable à définir avec eho : appropriation, groupe de camp) ;
  - que se passe-t-il si un avatar ou un animateur est ajouté ensuite (refus d'ajout, ou fin de la protection annoncée à tous les membres) ;
  - garde-t-on les **volumes** dans le Cockpit (recommandé : oui, sans interlocuteurs) ;
  - l'animation accepte-t-elle de perdre la vue sur ces échanges (risque de coordination hors jeu) ;
  - la supervision reste-t-elle possible sur décision de l'Administration ?
- **Précision de l'utilisateur (2026-10-13)** :
  - un compte venant de Keycloak est **d'office humain**, donc une conversation entre de tels comptes peut être rendue privée ;
  - **dès qu'un avatar IA est membre**, la conversation ne peut pas être rendue privée, même avec des humains dedans.
  - Reste à préciser : dans les apps, on écrit **sous un avatar** (identité eho). Un avatar **incarné par un joueur** (appropriation eho) compte comme humain. Mais un avatar **incarné par l'animation** est-il humain lui aussi ? (Proposition : non, sinon l'animation pourrait se cacher d'elle-même.)
- **Agents** : CYBERSECU (cela réduit l'exposition du privé : avis favorable probable), MASTORION (Chat social), PLEIADE (messagerie), DESIGNER (geste « rendre privée » et indicateur visible par tous les membres).
- **Placement** : après le lot 4, puisqu'il suppose la supervision et les métadonnées en place.

### Point de déploiement découvert (2026-10-13) — la base d'une instance existante
La plateforme ne crée la base d'une app **qu'à la création de l'instance** (`zone-manager.ts`, `createInstanceDb` au déploiement initial). Ajouter `requires: mariadb` au catalogue du Cockpit **ne donne pas de base au Cockpit déjà déployé** sur DELATTRE 26. Options :
1. **Recréer l'instance Cockpit.** Le Cockpit ne garde rien côté serveur aujourd'hui. Il faut recocher « Veille » sur les groupes, et les espaces de l'Admin sont conservés.
2. **Faire créer par la plateforme la base manquante au redéploiement** (`pleiade-platform`, à voir avec PLEIADE et Xavier).

Dans tous les cas, le Cockpit doit **tourner sans base** : ancienne vue intacte, et la nouvelle annonce « base non fournie ».

✅ **Tranché et fait le 2026-10-13 : option 2.** L'utilisateur voulait une mise à jour sans recréer l'instance. `assurerBaseInstance` (pleiade-platform `b6f128f`) crée la base au déploiement. Lots 1 et 2 **en production** le 13/10.

## 6. Agents et dépôts concernés
| Lot | Dépôts | Agents |
|---|---|---|
| 1 | `app-cockpit`, `pleiade-platform` (base) | PLEIADE, ARCHITECTE, CYBERSECU (K6, K9, K11) |
| 2 | `app-social`, `eho`, `app-cockpit` | PLEIADE, MASTORION, DESIGNER, CYBERSECU (K7) |
| 3 | `app-press`, `app-cockpit` | PLEIADE, DESIGNER |
| 4 | `app-messagerie`, `app-social`, `app-cockpit`, Keycloak | PLEIADE, MASTORION, CYBERSECU (K1 à K5, K8, K13) |
| 5 | `app-cockpit` | DESIGNER, CYBERSECU (K10) |
