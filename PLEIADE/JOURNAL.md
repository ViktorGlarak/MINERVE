# JOURNAL — PLEIADE (historique chronologique, append-only)

> Comptes rendus datés des travaux sur le système PLEIADE. Les règles et l'état durable sont dans `MEMOIRE.md`.

---

## 2026-09-16 — Fusion de `MEYTRE` dans `main` : notre EHO de jeu rejoint la mise en production de Xavier

**Demande utilisateur** : « tout le travail réalisé dans la branche MEYTRE, peux-tu le commiter dans main pour qu'on soit bien à jour ? » — avec la consigne explicite de **résoudre les conflits sans casser ce qui a été fait sur main**, et de **retenir les évolutions de MEYTRE** là où la mise à jour vient bien de MEYTRE.

### Ce que chaque branche apportait (séparées depuis `830a0eb`)
- **MEYTRE — 4 commits, nous** : STARTEX, planche joueur, comparaison animateur, cloisonnement des rôles, groupes de travail, verrous, versement granulaire, planche relationnelle, planche officielle.
- **`main` — 8 commits, Xavier** : image Docker et `docker-entrypoint.sh`, Prisma 7 (client dans `src/generated`, `prisma.config.ts`), Keycloak derrière Traefik + thème Pléiade, mise en production automatique depuis la branche `prod`, et ⭐ **« Fermer l'annuaire des avatars »** — les gardes `exigerLecture` / `exigerEcriture` / clé de service `PLEIADE_API_KEY` sur toutes les routes.
- ⭐ **Les deux branches avaient attaqué le MÊME problème** (fermer l'application aux non-autorisés) **sans se voir**. D'où exactement deux conflits, tous deux sur des gardes d'autorisation.

### Résolution des deux conflits — on garde les DEUX apports, jamais « la version d'un camp »
| Fichier | Retenu de MEYTRE | Retenu de `main` |
|---|---|---|
| `(admin)/layout.tsx` | Le garde complet : `auth()` + **traitement de `session.error`** (rôles vides ≠ joueur → reconnexion, leçon du 2026-09-14), `estRoleAdmin` (`lib/roles.ts` = source unique), redirection vers `/mon-eho`, padding responsive | `export const dynamic = "force-dynamic"` + la doctrine du rôle « Administration » déclaré au catalogue Pléiade (commentaire) |
| `(player)/layout.tsx` | La **coque** (Sidebar + `min-w-0 … p-4 sm:p-6 lg:p-8`) dont dépend toute la refonte visuelle | Le garde `operateurCourant()` + `force-dynamic` |

- **Arbitrage assumé** : un opérateur sans le rôle admin est **redirigé vers `/mon-eho`** (décision du 2026-09-14) plutôt que de recevoir l'écran « Accès refusé » de Xavier — un joueur n'a rien à faire sur une page d'erreur. ⏳ **À signaler à Xavier** : c'est le seul endroit où son comportement a été écarté au profit du nôtre.

### ⚠ Ce que la fusion automatique a fait dans notre dos — et qu'il a fallu contrôler un par un
- `lib/api-auth.ts` (touché des deux côtés) : git a gardé **les rôles de CLIENT** lus par Xavier (`resource_access[eho]` — sans eux, **aucun administrateur n'est vu dans une zone Pléiade**, les rôles y sont créés comme rôles de client) **et** notre source unique `lib/roles.ts`. Le `const ROLES_ADMIN` local de `main` a disparu au profit du module partagé : **plus de liste dupliquée**, exactement ce qu'on voulait.
- `lib/auth.ts` (touché par `main` seul) : vérifié que le **contrat dont dépend notre garde tient toujours** — la session expose bien `roles`, `error` et `username`. Xavier y a même corrigé la lecture des rôles de client.
- Routes API : les gardes de `main` se sont posés **sans effacer nos ajouts** (planche officielle dans l'import, `PORTEUR_OFFICIEL` dans l'export, `purgerEstimations` sur la fiche d'avatar).
- 🔧 **Corrigé à la main** : `api/import/route.ts` se retrouvait avec **deux `import` du même module** `@/lib/api-auth` (une ligne de chaque branche) — refondus en un seul.

### 🔒 Conséquence majeure : la faille des 10 routes est FERMÉE
Le travail de Xavier, en arrivant par la fusion, referme le trou décrit au § 8bis de `MEMOIRE.md`. **Vérifié en anonyme sur la version fusionnée réellement démarrée** : `/api/users`, `/api/users/[id]`, `/api/groups*`, `/api/import`, `/api/uploads`, `/api/activity`, `/api/avatars/export` → **401**. Les pages `/mon-eho`, `/eho-gt`, `/graphe`, `/avatars`, `/trombinoscope`, `/users`, `/comparaison`, `/planche-officielle` → **307**.
- **10ᵉ route, `uploads/[nom]` : délibérément publique**, ce n'est pas un oubli — les portraits sont affichés par mastorion, c'est écrit dans le code.
- ⏳ **Ce qui RESTE ouvert** : `GET /api/users` est gardé par `exigerLecture` (n'importe quelle session de la zone) et renvoie la **charge utile complète**. Un **joueur connecté** peut donc y lire `pays`, `label`, `activite`, `observations` — ce que la planche joueur lui cache. Le dépouillement reste contournable **par un participant**, plus par un anonyme. C'est l'arbitrage encore en attente (charge utile réduite pour les non-admins).

### Contrôles de la fusion — dans un arbre de travail isolé sur `C:` (jamais sur l'arbre de travail de l'utilisateur)
`npx tsc --noEmit` **0 erreur** · `npx eslint` **0 erreur** (1 avertissement `<img>` préexistant) · `npm run test` **71/71** · `npm run test:bio` **538/538** · `npm run build` **réussi**, toutes les routes des deux branches présentes · serveur de production démarré sur le **port 3002** pour tester les gardes en anonyme.
- ⚠ **Piège d'outillage rencontré** : un `node_modules` monté en **jonction** fait **planter Turbopack** (`Symlink [project]/node_modules is invalid, it points out of the filesystem root`). Il faut une **vraie copie** (0,7 Go, ~30 s en `robocopy /MT:16`). Ce n'était pas un défaut de la fusion.
- ⚠ **Non vérifié** : le comportement **connecté** par rôle (animateur → trombinoscope, joueur → renvoyé sur `/mon-eho`). Le flux Keycloak n'aboutit pas sur un autre port que 3001 (le client `eho` n'autorise que celui-là) et je n'ai pas modifié la configuration Keycloak pour un essai. Le code de ce garde est **repris mot pour mot de MEYTRE**, que l'utilisateur fait tourner depuis deux jours.
- ⚠ **Découvert au passage** : Prisma charge `prisma7.config.ts` (notre fichier, présent depuis le commit initial) **et non** `prisma.config.ts` (celui de Xavier). Les deux existent sur `main` — la duplication **préexiste à la fusion**, je n'y ai pas touché. Ils déclarent le même schéma et la même URL, donc le comportement est identique aujourd'hui, mais **lequel gagne n'est pas évident** : à trancher avec Xavier.

### État des dépôts en fin de séance
- **`main` POUSSÉ** sur `origin` (`e3e2acc..ff1c63a`) — décision de l'utilisateur. `prod` n'a pas été touchée, **aucun déploiement automatique n'a été déclenché**. Point de retour conservé : tag **`avant-fusion-MEYTRE`** (= `e3e2acc`, l'état de `main` avant fusion).
- `D:\CECPC\PLEIADE\eho` — branche `main`, à jour avec `origin/main`.
- `C:\CECPC\PLEIADE\eho` (clone d'exécution) — **basculé de `MEYTRE` sur `main`** à la demande de l'utilisateur. Le travail y est désormais fait sur une base qui contient **aussi le durcissement de Xavier**.
  - ⚠ **Vérifié AVANT de toucher à quoi que ce soit** : le travail vivant non commité y était **identique au commit `15d8b25`** (`diff -r` sur `src/`, `prisma/`, `scripts/`, `package.json` — seul `src/generated`, ignoré par git, différait). Rien ne pouvait être perdu.
  - **Filet conservé** : `stash@{0}` — « etat MEYTRE avant bascule sur main (2026-09-16) ». À supprimer quand l'utilisateur le décidera (`git stash drop`).
  - `npm install` (ajout de `dotenv` par `main`) + `prisma generate` refaits ; **aucun `db push`** — le schéma de `main` est identique à celui de `MEYTRE`, la base était déjà en phase.
  - Serveur de dev **relancé sur 3001**, gardes vérifiés en anonyme : `/mon-eho`, `/graphe`, `/trombinoscope`, `/planche-officielle` → **307** ; `/api/users`, `/api/avatars/export` → **401**.

### Dans la foulée — l'utilisateur réaligne `MEYTRE` sur `main` (vérifié)
Pour repartir d'une base commune et commiter proprement ses prochains travaux, l'utilisateur a reporté `main` dans `MEYTRE` et poussé. **Contrôlé** : `origin/MEYTRE` et `origin/main` sont au **même commit `ff1c63a`** et au **même arbre** (`ecfa6a6`) — `0` commit d'écart **dans les deux sens**. `prod` n'a pas bougé (`e3e2acc`).
- ⚠ **Une seule chose n'était pas en ordre, en local** : le clone d'exécution `C:` était resté sur `main`, et sa branche **`MEYTRE` locale traînait 10 commits en arrière**. Commiter là-dessus aurait **reconstruit une divergence** dès le premier travail. Remis d'aplomb (`checkout MEYTRE` + `merge --ff-only`) : comme l'arbre est identique à celui de `main`, **aucun fichier n'a bougé** et le serveur de dev n'a pas bronché (`/login` 200, `/mon-eho` 307, `/api/users` 401).
- **Les deux clones sont maintenant sur `MEYTRE`**, propres, à jour, base strictement identique à `main`.
- Le filet `stash@{0}` de C: est devenu **redondant** (l'état qu'il conserve est entièrement contenu dans `ff1c63a`) — conservé tant que l'utilisateur ne dit pas de le supprimer.

### Suppression de l'onglet « Choix d'avatar » (section joueur)
**Question de l'utilisateur** : « à quoi sert l'onglet *Choix d'avatar* dans la partie joueur ? » — puis, à la lecture de la réponse : « supprime-le, il ne convient plus aux décisions qu'on a prises aujourd'hui ».

**Ce que la lecture du code a montré** :
- La page annonçait « Sélectionnez votre personnage » mais **ne sélectionnait rien** : aucun `onClick` sur les cartes, aucun `POST`, aucune persistance. Les seuls boutons actifs étaient les filtres par groupe.
- `git log --follow` : elle date du **commit initial** `a071eed` — vestige de l'échafaudage d'origine, quand **un avatar était un compte Keycloak**. La prémisse est morte avec `0720ab1` (« fin du lien avatar/Keycloak ») ; l'écran, lui, était resté. Même famille que les 20 avatars de démonstration supprimés le 2026-09-14.
- ⚠ **Elle contredisait frontalement la règle n°1 du jeu.** `lib/eho-joueur.ts` dit : « le dépouillement est la règle : hors STARTEX, un joueur ne doit RIEN savoir d'officiel ». Or la page appelait `/api/users` en simple joueur connecté et **affichait la bio et les groupes** des 453 avatars (le reste de la ligne `User` étant dans la réponse réseau). **`Mon EHO` cachait ce que `Choix d'avatar` distribuait, dans le même menu, au même joueur.**

**Fait** : entrée retirée de `components/Sidebar.tsx` (menu JOUEUR = `Mon EHO` · `EHO GT` · `Planche relationnelle`), page `(player)/avatars/page.tsx` **effacée**, commentaire d'en-tête du Sidebar corrigé et daté. Aucune autre référence dans le code (`grep` sur `"/avatars"` : la ligne du menu était la seule).
**Vérifié** : `tsc` **0 erreur** · `eslint` **0 erreur** (l'avertissement `<img>` disparaît, il venait de cette page) · `npm run test` **71/71** · `/avatars` renvoie **404** sur le serveur de dev, `/login` toujours 200.
**⭐ Effet de bord utile** : cette page était **le seul écran joueur à consommer `/api/users`** — c'est elle qui bloquait la réduction de charge utile réclamée depuis le 2026-09-14. **Le verrou a sauté.**

#### 🔎 Défaut trouvé au passage — `npm run test:bio` mentait depuis la fusion (CORRIGÉ le jour même)
**Le défaut** : `scripts/test-bio.mts` lisait les vraies bios via `fetch("http://localhost:3001/api/users")` **sans session**. Depuis que la route est gardée, il recevait **401**, tombait dans sa branche `!reponse?.ok`, annonçait « **serveur injoignable sur :3001** » — **faux : le serveur avait répondu, il avait refusé** — puis passait de **538 contrôles à 13** en affichant toujours « **TOUT PASSE** », code de sortie **0**.
⚠ Exactement le travers que le projet s'interdit : « un échec de lecture ne doit jamais être présenté comme un résultat valide » · « contrôler le code HTTP dans tout script d'essai ». `!reponse?.ok` confondait **trois** situations : serveur éteint, serveur qui refuse (401/403), serveur qui plante (500).

**Le correctif retenu — supprimer la cause, pas le symptôme** : le script **lit désormais les bios DIRECTEMENT en base** (`PrismaClient` + `PrismaMariaDb`, helper `urlBase()` repris tel quel de `backfill-curseur.mts`). ⭐ **La couche HTTP n'a jamais été le sujet** : ce qu'on éprouve, c'est le découpage d'un texte. En allant à la source, **la question de l'autorisation disparaît**, et le script ne dépend plus du tout du serveur de dev.
**Et le diagnostic devient honnête** :
- échec de lecture → message qui **nomme la cause réelle** (l'enrobage Prisma — ligne vide, « Invalid `prisma.x.y()` invocation: », extrait de code annoté — est écarté pour garder la ligne qui renseigne, tronquée à 110 caractères) ;
- ⭐ **un contrôle sauté n'est plus un contrôle réussi** : la conclusion affiche « **INCOMPLET** » au lieu de « TOUT PASSE » et le script **sort en code 1**, avec le remède à faire (`docker compose up -d eho-db`) ;
- une base **vide** est également traitée comme incomplet — il n'y avait rien à éprouver, ce n'est pas un succès.
- ⚠ Piège évité de justesse : `e.message.split("\n")[0]` donnait « base inaccessible **()** » — un motif vide, soit le défaut qu'on corrigeait, en plus petit.

**Vérifié sur les trois chemins** : cas normal **538/538**, code 0 (mêmes chiffres qu'avant la fusion : 262 bios, 57 fiches structurées, 59/59 aérées) · base éteinte → INCOMPLET, code **1** · mauvais mot de passe → INCOMPLET, code **1**. `tsc` et `eslint` 0 erreur, `npm run test` 71/71.

---

## 2026-09-15 — EHO PLEIADE : groupes de travail, verrous, versement granulaire, planche relationnelle (branche `MEYTRE`)

**Demande utilisateur, en cinq temps** : (1) affilier un joueur à un **groupe de travail** et lui donner, en plus de « Mon EHO », un **« EHO GT »** commun où le groupe travaille ensemble ; (2) **avertir et bloquer** quand une carte est déjà ouverte par quelqu'un d'autre ; (3) pouvoir **importer** l'EHO GT dans son EHO personnel ; (4) **verser** l'inverse — une carte, une rubrique ou un pays — par une **icône**, avec **retour arrière** ; (5) une **planche relationnelle** en onglet séparé, inspirée de *Board* d'Adobe : poser des cartes, tirer des liens, canevas infini.

### Groupes de travail — la convention qui tient tout
- Les groupes de travail sont les **sous-groupes du groupe Keycloak `GT`** (chemin `/GT/<nom>`). Rien d'autre n'est un GT. Cette convention évite d'ajouter une table et de dupliquer une appartenance qui existe déjà dans Keycloak.
- ⚠ **Les groupes ne sont PAS dans le jeton** : ils sont résolus **côté serveur** par l'API d'administration Keycloak (`lib/keycloak-admin.ts` → `groupesDeTravail(sub)`).
- ⚠ **`groupesDeTravail` renvoie `null` en cas d'échec, jamais `[]`** — application directe de la leçon du 2026-09-14 : « un échec de lecture n'est pas un résultat valide ». `lib/porteur.ts` traduit `null` en **503**, et un non-membre en **403**. Sans cela, une panne Keycloak aurait ouvert tous les GT à tout le monde.
- Un **porteur** (`playerId` ou `gt:<id>`) paramètre désormais toutes les routes EHO : `components/planche.tsx` est la **même planche** pour « Mon EHO » et « EHO GT », un `?gt=` près.

### Concurrence — verrou par carte, pas par écran
- `eho_verrous` : un verrou **par carte et par porteur**, avec **TTL** et battement de cœur. Ouvrir une carte déjà ouverte affiche **qui** la tient et **bloque la saisie** — le lecteur voit tout, n'écrit rien.
- Portée volontairement limitée : le verrou protège la **fiche**, pas le rangement. Deux joueurs peuvent réordonner en même temps sans se gêner.

### Versement `Mon EHO` → `EHO GT` (et retour)
- **Icône unique** (jamais de bouton texte), reprise à l'identique dans le bouton d'import : le geste se reconnaît avant de se lire.
- Trois grains : **carte** (le bouton vit *dans* la fiche), **rubrique**, **pays**.
- ⚠ **Deux listes, pas une** : `aVerser` (les cartes qui ont une lecture à copier) et `aPlacer` (toutes les cartes demandées). Symptôme corrigé : *Ribiki restait dans « sans rubrique »* — il n'avait pas de lecture, donc il n'était ni versé **ni placé**.
- ⚠ **`parRubrique: [{nom, ids}]`** et non une liste plate : verser un **pays** avec une seule rubrique cible **écrasait toutes les rubriques** du GT. Symptôme constaté par l'utilisateur, réparé **avec son propre bouton d'annulation**.
- **Annulation** (`verser-gt/annuler`) : restaure l'instantané `eho_versements`, mais **épargne** les cartes qu'un tiers a modifiées depuis (`modifiePar` différent) ou qui sont verrouillées ; la disposition n'est restaurée que **si rien n'a été épargné**. Annuler ne doit jamais détruire le travail d'un autre.
- L'**import GT → personnel** écrit d'abord une **sauvegarde restaurable** (`eho_sauvegardes`).

### ⭐ Planche relationnelle (`(player)/graphe`) — nouveau concept
- **Bibliothèque retenue : `@xyflow/react` (React Flow) 12.11.6** — MIT, **3 dépendances**, canevas infini, zoom, nœuds et liens sur mesure. Proposée puis validée par l'utilisateur.
- Persistance : **un seul modèle**, `eho_graphes` (une ligne JSON par porteur). Assainissement côté serveur : 600 nœuds, 2 000 liens, coordonnées bornées, couleurs `#RRGGBB`, **auto-liens refusés**, liens vers un nœud absent supprimés.
- **Gestes construits sur demande, dans l'ordre** : lien cliquable pour être supprimé → auto-lien interdit → **libellé éditable** → **geste d'étirement/rupture** (clic maintenu, le trait s'étire et **casse**, à la manière de ComfyUI) → suppression des pointes de flèche → **barre d'inspection en pied de planche** (couleur, texte, supprimer) plutôt que des pastilles sur le tracé → **libellé posé AU-DESSUS du trait et orienté comme lui** (`<textPath>` sur un rail inversé, halo `paintOrder="stroke"`).
- ⚠ **Les liens ne se connectaient pas** : toutes les accroches étaient `type="source"`. Correctif : une accroche **cible + source** par côté, plus `ConnectionMode.Loose`.
- **Point de jonction** (« connecteur ») : un **lien ne peut pas être la cible d'un autre lien**. Pour rattacher une troisième carte à une relation, il faut un point matériel. Deux apparences :
  - **sans nom**, une pastille de 16 px — les accroches se confondent avec elle, il n'y a rien à viser ;
  - **avec un nom**, un **rectangle blanc bordé de sa couleur, à l'image des cartes**, le texte à l'intérieur *(demande du 2026-09-15)*.
  - ⚠ **Deux pièges à ne pas réintroduire** : (1) mettre le texte **dans** une pastille agrandit la boîte et React Flow **repousse les accroches très loin** du point — d'où le nom hors flux pour la pastille, et le rectangle qui *est* la boîte pour la version nommée ; (2) une accroche qui **recouvre** le nœud capte l'appui et le rend **impossible à déplacer** — d'où quatre accroches de bord (`j-<côté>` / `s-j-<côté>`).
  - Les liens partant d'une jonction sont **rectilignes** (`getStraightPath`) et non courbes : ils filent **droit vers la carte**, dans sa direction réelle.
- ↩️ **Revenu en arrière à la demande de l'utilisateur** : la disparition automatique d'une jonction tombée sous 3 liens a été **annulée** (« remet la version d'avant c'était bien »).

### Accroches invisibles au repos (demande de fin de séance)
- **Constat utilisateur** : « je trouve ça hyper moche, j'aimerai qu'on ne les voit pas, et que quand on place la souris sur le bord d'une card le connecteur apparaisse ». Les points de départ étaient en effet **visibles en permanence** (`opacity-60`), soit quatre pastilles indigo par carte.
- **Livré** : un composant unique **`Accroches`** (cartes *et* jonctions — un seul geste à apprendre) + un bloc CSS dans `globals.css`. Rien au repos ; les points se posent **au survol du nœud**, grossissent au survol d'une accroche précise, et **tout le plan les montre en retrait pendant qu'un lien est tracé** (pour désigner les arrivées possibles).
- **Teinte du camp** : la pastille reprend la couleur de la carte — le point qu'on tire annonce déjà de qui part la relation.
- ⚠ **La zone de préhension n'est pas le dessin** : boîte de 18 px pour une pastille de 10 px — on attrape un bord, on ne vise pas un point. La jonction **nue** garde des accroches de 10 px : plus grandes, elles recouvriraient ses 16 px et la rendraient indéplaçable (React Flow pose `nodrag` sur chaque accroche). Elle signale le survol par une **auréole**, pas par des pastilles : elle **est** son propre point d'accroche.
- ⚠ **`useConnection` doit être appelé AVEC un sélecteur** (`(c) => c.inProgress`) : sans lui, le composant se redessine à chaque pixel parcouru pendant tout le tracé.
- **Identifiants d'accroche inchangés** (`<côté>` / `s-<côté>`, `j-<côté>` / `s-j-<côté>`) — les plans déjà enregistrés continuent de se recharger (vérifié : 5 nœuds / 5 liens intacts).

### Menu du plan — ajouter là où l'on clique (⭐ registre extensible)
- **Demande** : « quand on clique sur la planche, un clic gauche, on a les options possibles de création qui s'affichent » — en commençant par « Point de jonction », **le bouton de la réserve étant supprimé**. L'utilisateur annonce qu'il **en demandera d'autres**.
- **Livré** : un **registre `MODULES`** dans `components/graphe.tsx` — une entrée `{cle, nom, aide, apercu, creer}` = un module de plus dans le menu, **sans toucher au menu ni au plan**. `creer` reçoit le point cliqué et rend un nœud **centré** dessus (React Flow positionne par le coin haut-gauche : au module de retrancher sa demi-taille, lui seul sait ce qu'il mesure).
- **Pourquoi c'est mieux qu'un bouton** : le bouton posait toujours au centre de l'écran, il fallait ensuite traîner le module au bon endroit. Le clic **désigne le point ET ouvre le choix** — un geste au lieu de deux.
- ⚠ **Un clic sur le fond sert d'abord à REFERMER** : si une barre d'édition est ouverte, le premier clic ne fait que désélectionner, c'est le suivant qui ouvre le menu. Sans cette règle, fermer une barre faisait surgir un panneau.
- ⚠ **Le navigateur émet un `click` même après un glissement** (appui et relâchement sur le même élément) : sans mesure, **chaque panoramique** se terminait par l'ouverture du menu à l'endroit lâché. Corrigé en mémorisant le point d'appui (`onPointerDownCapture`) et en ignorant tout clic ayant parcouru plus de 4 px. React Flow, lui, neutralise déjà le clic qui suit un lien lâché dans le vide.

### Encadrés — une mini-planche dans la planche
- **Demande** : « un encadré / une rubrique où on pourrait placer les cards dedans… faire comprendre visuellement que ces personnes font partie d'un même groupe », **sans empêcher** de relier une carte du dedans à une carte du dehors ou d'un autre encadré. Accessible par le **menu du plan**.
- **Choix de conception** : un vrai **contenant**, pas un rectangle décoratif — une carte lâchée dedans lui **appartient** (`parentId` de React Flow), donc déplacer l'encadré emporte son contenu. Redimensionnable (`NodeResizer`), titré, coloré par la même barre du bas que la jonction.
- **C'est le CENTRE de la carte qui décide** du rattachement, pas un chevauchement : une carte à cheval sur un bord serait sinon happée alors qu'elle est visiblement dehors.
- ⚠ **Les coordonnées d'un nœud rattaché sont RELATIVES à son encadré** (convention React Flow) — conversion dans les deux sens au rattachement/détachement, et à l'enregistrement. Sans elle, la carte saute à l'autre bout du plan.
- ⚠ **React Flow exige que le parent PRÉCÈDE ses enfants** dans la liste des nœuds → `trierNoeuds` (tri stable : les encadrés d'abord, donc rendus **derrière** les cartes libres).
- ⚠⚠ **Supprimer un encadré ne doit PAS supprimer son contenu.** React Flow, laissé à lui-même, emporte les enfants avec le parent — on perdrait d'un coup toutes les cartes rangées dedans. Traité dans `onBeforeDelete` : on détache, on retire le seul encadré, et on répond `false` pour qu'il ne rejoue pas la suppression.
- ⚠ **Un `parent` introuvable détache le nœud** côté serveur au lieu de le garder : React Flow le positionnerait relativement à un parent inexistant et la carte **disparaîtrait de l'écran**. *Perdre un rangement est réparable ; perdre une carte de vue ne l'est pas.*
- **Barre du bas généralisée** : `BarreConnecteur` → **`BarreNoeud`** (marque, titre, invite, aide paramétrés) — jonction et encadré partagent la même, au même endroit.
- **Serveur** : `assainir` accepte `groupe`, `largeur`/`hauteur` (bornées 140–8000) et `parent`. **Aller-retour vérifié** : titre, couleur, taille et appartenance restitués ; `parent` fantôme détaché ; taille 10×99999 ramenée à 140×8000.
- 🔴 **Incident de la séance** : mon plan d'essai a été envoyé sur la planche de `joueur_test` **pendant que l'utilisateur travaillait dessus** → son plan a été écrasé (`eho_graphes` = une ligne par porteur, **sans historique**). Reconstruit au plus près (jonction « conseil » + 3 avatars + 3 liens), positions approximatives. **Règle : ne jamais écrire sur la planche d'un porteur vivant — créer un porteur d'essai dédié.**

### Transfert d'un encadré entre planches relationnelles (`POST /api/eho/graphe/transferer`)
- **Demande** : verser un encadré **avec toutes ses cartes** vers la planche relationnelle du GT, et **inversement** rapatrier un encadré du GT dans sa planche personnelle « pour y apporter des modifications perso ».
- **Le sens est donné par l'endroit**, jamais par un réglage : sur ma planche le bouton verse vers un GT (`vers-gt`), sur celle d'un groupe il rapatrie chez moi (`depuis-gt`). Même icône que le versement de l'EHO (`ICONE_TRANSFERT`), **retournée** selon le sens.
- ⭐ **Ce transfert n'efface JAMAIS rien chez le destinataire** : il n'ajoute ou ne remplace que l'encadré visé, son contenu et les liens **dont les deux bouts sont dedans**. C'est ce qui le rend sûr sur une planche partagée — et **c'est pourquoi il n'a pas de bouton « annuler »**, contrairement au versement de l'EHO : il n'y a rien à restaurer. **Vérifié** : un nœud et un lien préexistants du GT ont survécu au versement.
- **Les identifiants sont conservés** → reverser deux fois **met à jour** au lieu de dupliquer, et le rapatriement reconnaît l'encadré (essai : `remplaces: 5`, planche personnelle intacte — 2 encadrés, 6 avatars, 2 jonctions, 6 liens).
- **Un lien vers l'extérieur ne suit pas** : il désignerait une carte que le destinataire n'a peut-être pas, et emporterait au passage des cartes que personne n'a demandées.
- **Refus vérifiés** : sans `?gt=` → 400 · encadré inconnu (ou nœud qui n'est pas un encadré) → 404 · GT dont on n'est pas membre → 403 · sens invalide → 400 · sans session → 401.
- **Barre du bas** : `BarreNoeud` reçoit un emplacement `extra` — les actions propres à un genre de nœud s'y posent sans polluer la barre générique.

### ⭐ Planche relationnelle OFFICIELLE (animation), enregistrée avec le modèle d'EHO
- **Demande** : « il faut forcément qu'on ait la planche relationnelle officielle dans la vue admin […] liée et enregistrée au modèle d'EHO utilisé ». Un PDF de relations entre avatars sera fourni pour la remplir.
- **Porteur `officiel`** (`lib/porteur.ts`, id réservé `PORTEUR_OFFICIEL = "officiel"`) : troisième nature à côté de `joueur` et `gt`. Aucune collision possible — les `sub` Keycloak sont des UUID. **Réservé aux animateurs, vérifié côté serveur** ; `?officiel=1` sur une route d'un non-admin → **403**. Tout l'existant (GET/PUT, historique/versions) marche sans modification.
- ⭐ **Les cartes n'y sont PAS dépouillées** : `composerCarte(..., { officiel })` révèle pays, camp, fonction et bio pour tous, pas seulement les STARTEX. C'est la seule vue où l'on regarde la vérité. Le drapeau est **déduit du porteur déjà vérifié**, jamais réclamé par le client. **Vérifié** : 381 cartes hors STARTEX renseignées côté animation, **0 fuite** côté joueur.
- ⭐ **La planche voyage avec le modèle** (`Payload.graphe` dans `lib/eho-templates.ts`) : ses nœuds portent les identifiants des avatars, elle n'a de sens qu'avec la population qui va avec. **Vérifié de bout en bout** : capture d'un modèle → `payload.json` contient `graphe` (4 nœuds, 2 liens) ; planche vidée → application du modèle → planche restituée à l'identique.
- ⚠ **Absent ≠ vide** : un modèle capturé avant cette fonctionnalité (SKOLKAN) n'a pas la clé `graphe` → l'appliquer **laisse la planche en place** au lieu de l'effacer (vérifié). Le modèle **VIERGE** porte une planche vide **explicite** : lui, il efface — sinon une remise à zéro laisserait un schéma reliant des avatars disparus.
- **Pas de bouton de transfert** sur cette planche : elle n'est ni celle d'un joueur ni celle d'un groupe, elle voyage par le modèle.
- Écran `(admin)/planche-officielle` + entrée de menu « Planche officielle » (même icône que celle du joueur : même outil, autre vue). Cloisonnement vérifié : joueur et anonyme → **307**, animateur → 200.

### ⭐ Le diagramme RZO de DELATTRE 26 porté sur la planche officielle
- **Demande** : reproduire le schéma relationnel de `EXER\DELATTRE 26\01_Montage exercice\RENS\…Diagramme RZO.pptx` sur la planche officielle, **avec les avatars existants**, sans en créer aucun.
- **Méthode — la géométrie du `.pptx`, pas l'œil** : `python-pptx` + lecture XML. Chaque trait porte sa **couleur** et son **pointillé** (= le type de relation, via la légende du document) et, quand il est attaché, les **identifiants** de ses deux extrémités (`a:stCxn` / `a:endCxn`). Pour les traits non attachés, résolution par **distance au bord** des nœuds (jamais au centre : une carte large fausse tout), avec un seuil de rejet.
- **Livré** : **30 cartes d'avatars + 8 points de jonction + 54 liens** sur la planche officielle. Positions reprises du diagramme (pouces × 200), couleurs et libellés repris de la légende.
- ⭐ **Les 8 nœuds anonymes sont des JONCTIONS, pas des avatars** : cinq silhouettes du réseau HFM/NOM — identifiées comme anonymes parce que **les cinq images ont le même SHA-1**, c'est le même fichier répété — et trois badges « ? ». Les représenter en jonctions préserve la structure **sans inventer d'avatar**.
- **Appariement 30/30**, dont 4 orthographes divergentes (`Rémi LAFFIN`→`Rémy Laffin`, `MORDVIDCHEV`→`Mordidchev`) et le trio cyrillique (`@rzo_x`, `@rzo_x_2`, `@rzo_x_3`).
- **1 lien sur 56 reste douteux** : `The flying fly` ↔ `Le Padupe` (lien suspecté), extrémités à plus d'un pouce de toute carte. Non posé — signalé à l'utilisateur.
- **Non porté** : les deux rectangles de mise en page (`27 BIM / 9 BIMa` ; le cadre des quatre cadres HFM/NOM). Ils se rendraient en **encadrés**, à valider.

### ⭐ La planche officielle voyage aussi dans le classeur Excel
- **Demande** : que « Exporter en .xlsx » emporte le schéma de la planche officielle, et que le réimport soit **fonctionnel**.
- **Format** : deux onglets, parce qu'un graphe ne tient pas dans un tableau — **`# Planche officielle - noeuds`** (cle, type, x, y, libelle, couleur, largeur, hauteur, **parent**) et **`# Planche officielle - liens`** (id, source, cible, libelle, couleur, depuis, vers).
- ⚠⚠ **LA décision qui rend l'aller-retour possible : les cartes y sont désignées par leur `username`, pas par leur identifiant.** L'import apparie les avatars par `username` et leur donne de **nouveaux** UUID ; un plan qui aurait retenu les identifiants d'origine ne retrouverait personne dans la base d'arrivée et reviendrait **vide**. Jonctions et encadrés, eux, n'existent que dans le plan et gardent leur propre id.
- ⚠ **Le plan se relit APRÈS les avatars**, jamais avant : il faut que les avatars existent pour avoir un identifiant à lui donner. D'où un classeur conservé en mémoire entre les deux étapes (`lignesDuClasseurCharge` séparé du chargement).
- ⚠ Le préfixe **`#`** garde ces onglets invisibles pour les imports qui ne les connaissent pas (dont celui de l'EHO mastorion) : un classeur exporté ici y reste lisible, la planche en moins.
- ⚠⚠ **Réservé à l'animation** : `/api/import` n'exige toujours aucune authentification (dette connue). On ne fait donc pas entrer une capacité nouvelle par une porte ouverte — sans rôle admin, **les avatars sont importés, la planche est ignorée, et le résultat le DIT** (`ignores: ["rôle admin requis…"]`). Vérifié sans session et avec un compte joueur.
- Le **filet** s'applique aussi : instantané de la planche avant l'écriture par import.
- **Aller-retour vérifié EXACT** : planche vidée → import du classeur → **43 nœuds / 56 liens / 42 nœuds imbriqués**, nœuds **et** liens strictement identiques à l'original, imbrication des encadrés comprise. Un classeur **sans** onglet de planche ne touche à rien (`planche: null`).

### 🔴🔴 L'imbrication se perdait au rechargement — et l'enregistrement automatique achevait le travail
- **Symptôme utilisateur** : « pendant que je travaille ça fonctionne, mais si je change d'onglet et que je reviens, les encadrés ont changé d'emplacement et ne sont plus à l'intérieur ».
- **Cause, en une ligne** : au chargement, la branche qui reconstruit un **encadré** ne lisait pas `parent`. Les branches `avatar` et `connecteur` le faisaient ; celle des groupes avait été écrite **avant** que les encadrés puissent s'imbriquer, et n'avait pas été reprise.
- ⚠⚠ **Pourquoi c'était bien pire qu'un oubli d'affichage** : la position d'un nœud imbriqué est **relative à son parent**. Sans `parentId`, elle est relue comme **absolue** → l'encadré saute ailleurs sur le plan. Puis **l'enregistrement différé réécrit aussitôt cet état aplati**. Le simple fait de revenir sur l'onglet **détruisait** le travail.
- ✅ **Récupéré** : la version **18** de `eho_graphe_versions` portait encore l'imbrication (42 nœuds imbriqués, 2 encadrés dans « RENS ») — capturée juste avant l'aplatissement. Restaurée. **Deuxième sauvetage réel du filet.**
- **Vérifié après correctif** : aller-retour écriture → relecture → réécriture, les 42 nœuds imbriqués et les 2 encadrés enfants tiennent.
- ⚠ **Leçon** : quand un champ devient valable pour un nouveau type de nœud, **relire TOUTES les branches** du chargement et de l'enregistrement. Ici l'écriture était correcte (le `parent` partait bien au serveur), le serveur le gardait, et seule la lecture le jetait — le genre d'asymétrie qu'aucun test d'API ne voit, parce que l'API, elle, répondait juste.

### ⭐ Encadrés imbriqués (une cellule dans un état-major)
- **Demande** : « un encadré ne peut pas être dans un autre encadré, pourtant il faut que ce soit réalisable, avec les cartes bien présentes dans l'encadré ».
- **Deux verrous levés** : le **serveur** retirait purement le `parent` des nœuds de type `groupe` (`est !== "groupe" ? … : undefined`), et l'**écran** sortait de `surFinDeplacement` dès que le nœud déplacé était un encadré.
- ⚠⚠ **Le tri « les encadrés d'abord » ne suffit plus.** React Flow exige qu'un parent précède ses enfants ; dès qu'un encadré en contient un autre, seul un tri **par profondeur d'imbrication** le garantit. Second critère à profondeur égale : l'encadré avant le reste, pour rester **derrière** les cartes.
- ⭐ **Le PLUS PETIT encadré contenant le centre l'emporte.** Avec l'imbrication, un centre tombe dans deux boîtes à la fois : prendre la dernière de la liste rangeait au hasard. La plus petite est toujours la plus intérieure — c'est celle que l'œil désigne.
- ⚠⚠ **Boucles d'appartenance** (A dans B, B dans A) : React Flow chercherait indéfiniment la position d'un nœud par rapport à lui-même et **l'écran se fige**. Trois gardes : le déplacement écarte le nœud et **toute sa descendance** ; le serveur **remonte la chaîne** de chaque nœud et détache au premier déjà-vu ; les remontées de parent portent toutes une garde `vus`. **Vérifié** : un cycle A↔B envoyé volontairement est cassé (B détaché), sans blocage.
- ⚠ **Supprimer un encadré n'emporte plus les encadrés qu'il contient** : la règle « ne partent que les nœuds visés pour eux-mêmes » vaut maintenant pour tout ce qui a **un ancêtre** dans la liste de suppression, pas seulement un parent direct. Idem pour l'interdiction de relier un encadré à son contenu, étendue à **tout ancêtre** : un lien vers le grand-parent serait tout aussi enfermé dans la boîte.
- ⚠ Le détachement calcule les positions absolues **avant** le retrait, imbrications résolues (`absolus`) : une fois le parent parti, la position d'un enfant ne veut plus rien dire.
- **Vérifié** : encadré dans encadré, **jonction au troisième niveau**, lien d'une carte vers la cellule imbriquée — tout persiste. État de l'utilisateur (43 nœuds / 58 liens) relu avant et remis après, sans résidu d'essai.

### ⭐ Les encadrés se relient, comme les jonctions
- **Demande** : relier une carte ou une jonction **à un encadré**, « en gardant le même système de placement du lien que les points de jonction ».
- **Livré** : l'encadré reçoit quatre accroches de bord (`g-<côté>` / `s-g-<côté>`) et surtout l'**ancrage géométrique** — `ancrable(type)` couvre désormais `connecteur` **et** `groupe`. Le lien touche le point du bord qui regarde l'autre extrémité, recalculé à chaque rendu : il glisse le long de l'encadré quand on déplace la carte, sans espace. Même geste, même rendu.
- **Ce que ça permet de dire** : « l'état-major finance cette cellule » se trace d'un trait vers le GROUPE, sans avoir à désigner un représentant arbitraire dans la boîte.
- ⚠ **Un encadré ne se relie pas à ce qu'il contient** (`lienValide`) : le trait serait tracé À L'INTÉRIEUR de la boîte — invisible, impossible à attraper — et il ne dirait rien, l'appartenance étant déjà écrite par le fait d'être dedans.
- ⚠ `boiteDe` prend `measured?.width ?? width` : `measured` n'existe qu'après le premier rendu, alors qu'un encadré porte sa taille dès sa création. Sans ce repli, il passait pour une pastille de 16 px le temps d'un rendu et le lien partait de son coin.
- **Vérifié de bout en bout** : aller-retour serveur d'un encadré relié à une carte (`s-left` → `g-right`) et à une jonction (`s-j-left` → `g-bottom`), puis **état exact de l'utilisateur remis en place** (42 nœuds / 56 liens — il avait continué à travailler pendant l'essai).

### Palette fermée + attaches des liens réparties
- **Constat utilisateur** : « tu as utilisé des couleurs que je ne peux pas sélectionner » et « tu as encore placé des liens au même endroit alors qu'on peut les mettre sur les côtés ou en bas ».
- ⭐ **Règle posée** : **toute couleur portée par un lien doit figurer dans la palette.** Une couleur absente s'affiche mais ne peut plus être ni retrouvée ni reproduite à la main — le joueur voit un trait qu'il lui est impossible de refaire.
- **Palette étendue de 7 à 13**, en deux familles : les couleurs de l'application (camps, STARTEX…) et ⭐ **le code couleur des diagrammes de réseau du SITCEN**, repris de leur légende et nommé par sa SIGNIFICATION — « Réseau (RZO) », « Clandestin (HFM/NOM) », « Lien suspecté », « Relation intime », « Lien familial », « Commande ». Un analyste qui a lu un diagramme RZO les reconnaît ; une planche reproduite depuis un tel document reste fidèle. Pastilles passées en 16 px et rangée `flex-wrap` pour loger les 13.
- **Attaches réparties** : chaque lien part désormais du **côté qui regarde l'autre carte** (horizontal si |dx|≥|dy|, sinon vertical), avec **bascule sur le côté suivant au-delà de 3 liens** sur un même côté. Résultat : 37 liens avec leurs deux accroches, 10 avec une seule (jonction à l'autre bout), 7 entre deux jonctions — ces dernières s'ancrant toutes seules par géométrie.
- ⚠ **L'utilisateur éditait la planche pendant l'opération.** J'ai **lu avant d'écrire** (règle du jour) : ses 3 modifications de couleur ont donc survécu. Mais ses éventuels choix d'accroche manuels ont été remplacés par le calcul. Son état exact reste restaurable — version `id=12`, auteur `thomas`, dans l'historique.

### 🔴 Erreur de ma fiche DELATTRE du 2026-09-10, corrigée
- `DELATTRE\MEMOIRE.md` affirmait que HETTA « **commande** (liens noirs) deux cellules ». **Faux** : sur les **63 traits** du fichier, **le seul trait noir est celui de la légende**. La légende définit un lien « commande » ; **le dessin n'en contient aucun**.
- HETTA n'a en réalité que trois liens : `relation RZO`→DEGARDIN, `ex-relation intime`→POMMEROND, un `lien suspecté`. La cellule YARBOT–LECONE–LAPOTRE–HERVOUET est une chaîne **HFM/NOM**, son unité n'étant portée que par un **rectangle de mise en page**.
- ⚠ **Cause** : la lecture de 2026-09-10 s'était faite **à l'œil sur le PDF** — elle a pris la proximité et les cadres pour des liens. Fiche corrigée, avec la leçon.

### Les GT apparaissent dans « EHO joueurs », même vides
- **Constat utilisateur** : « dans EHO joueurs je ne vois pas la possibilité de voir l'EHO des GT ».
- **Diagnostic** : la section existait déjà (et la route de détail savait déjà servir un GT — elle calcule `estGroupe` et les contributeurs). Mais la liste était bâtie **uniquement à partir des GT ayant des lectures** → un groupe sans travail était **purement introuvable**. Les lectures des GT versées plus tôt avaient été effacées par mes applications de modèle : la section était donc vide.
- **Corrigé** : la liste part de **tous** les GT (Keycloak) **union** ceux qui portent des lectures. Un groupe neuf, ou remis à zéro, s'affiche **à zéro** au lieu de disparaître ; un groupe supprimé de Keycloak mais porteur de travail reste visible — sa trace ne doit pas s'évaporer.
- ⚠ Et dans la route de détail : `estGroupe` ne peut pas se déduire des seules lectures. Sans lecture, un GT passait pour **un joueur anonyme sans nom**. Il est désormais reconnu par Keycloak. *Ne rien savoir n'est pas la même chose que savoir que c'est un joueur.*
- **Vérifié** : « 1re Division » et « 27e Brigade » listées à 0 ; ouverture d'un GT vide → nom correct, `estGroupe = true`, 62 lignes STARTEX. Garde-fous intacts : planche d'animateur par URL directe → **404**, joueur sur la liste → **403**.

### Rangement des deux planches admin + supervision des planches joueurs
- **Demande** : « Planche officielle » **dans ANIMATION** (c'est la vérité de l'exercice, pas une production de joueur), et un nouvel onglet **dans JOUEURS** pour voir les planches relationnelles **des joueurs et des GT**.
- **Menu réorganisé** : ANIMATION = Tableau de bord · Avatars · Groupes · **Planche officielle** · Modèles d'EHO · Import/Export — la planche officielle est **posée juste avant les Modèles**, parce qu'elle voyage avec eux. JOUEURS = EHO joueurs · Comparatif · **Planches relationnelles**.
- ⭐ **Porteur `observateur`** (`lib/porteur.ts`) : `?joueur=<sub>` (admin seul) et `?gt=<id>` pour un animateur **non membre** rendent un porteur marqué **lecture seule**.
- ⚠⚠ **Le vrai danger était l'enregistrement automatique** : la planche s'enregistre après une seconde de repos — **il suffisait d'OUVRIR le travail d'un joueur pour que l'écran de l'animateur le réécrive**. Verrou posé à trois niveaux : (1) **toute route d'écriture refuse un porteur observé** — `refusObservateur()` dans les 7 routes concernées, vérifié **403** sur planche, restauration, rangement, lecture et verrou ; (2) l'enregistrement différé **ne part pas** ; (3) les gestes d'édition sont neutralisés (classe `.lecture-seule` dans `globals.css` : liens inertes, boutons des cartes masqués, accroches cachées), plutôt que de faire descendre un drapeau dans chaque composant.
- ⚠ Un joueur qui tente `?joueur=<autre>` → **403** (« réservé à l'animation »).

### 🔴 Bug antérieur trouvé au passage — `tousLesGroupesDeTravail` rendait TOUJOURS une liste vide
- **Keycloak 26 ne remplit plus `subGroups`** : la recherche de groupes rend la racine `GT` avec `subGroups: []` et un `subGroupCount: 2`. Les enfants se demandent séparément, sur **`/groups/{id}/children`**.
- Conséquence : **aucun groupe de travail n'apparaissait dans les écrans d'animation**, sans la moindre erreur — le piège du « résultat vide » qui cache une lecture ratée, exactement celui qu'on avait déjà corrigé ailleurs. Touchait aussi le champ `groupes` de `/api/eho/comparaison`.
- **Corrigé et vérifié** : `['1re Division', '27e Brigade']` remontent.
- Le `[]` en cas d'échec est **conservé ici seulement**, et commenté : cette liste ne remplit qu'un choix à l'écran, elle ne décide **jamais** d'un accès — le contrôle d'appartenance passe par `groupesDeTravail`, qui rend `null`.
- `/api/eho/gt?tous=1` ajouté (admin seul) : un animateur supervise des groupes dont il n'est pas membre.

### 🔴 Encore un écrasement de test — planche du GT vidée, puis récupérée par le filet
- En testant « l'écriture doit être refusée », j'ai lancé un `PUT` vide sur le GT **1re Division** en supposant que l'animateur n'en était pas membre. **Il l'était** → écriture acceptée, planche vidée (l'encadré MERCURE et ses 3 liens).
- ✅ **Le filet posé une heure plus tôt a tenu** : `eho_graphe_versions` contenait l'état, restauré en un appel. **Premier sauvetage réel du dispositif.**
- ⚠ **Règle** : un essai « ceci doit être refusé » se fait sur une cible dont on a **vérifié** qu'elle déclenche le refus — sinon c'est un essai « ceci doit réussir », mené sans le savoir.

### Sauvegardes d'avant-application : complètes, plafonnées à 3, jamais pour rien
- **Arbitrage utilisateur** : « changer de modèle supprime tous les travaux des joueurs, **c'est normal** » → **aucune restitution automatique** après une application. Un nouveau modèle est un nouvel exercice. Et : « je ne veux pas qu'on se retrouve avec énormément de sauvegardes qui servent à rien ».
- **Constat chiffré** : ~400 Ko par sauvegarde et **aucune purge** — le dossier grossissait sans fin. Le problème existait déjà, indépendamment du reste.
- **Trois règles livrées** :
  1. ⭐ **Complète, ou pas du tout** — la sauvegarde embarque désormais `travail` : lectures, rangements (`eho_dispositions`) et planches des joueurs et des GT. Sans cela, « restaurer » rendait une population sans son exercice : du théâtre.
  2. ⭐ **Trois gardées** (`SAUVEGARDES_GARDEES`), purge à chaque écriture, tri par nom (l'horodatage ISO EST l'ordre chronologique, inutile d'ouvrir les fichiers). Plafond ~5 Mo. Le seul cas d'usage réel — « je viens de cliquer sur le mauvais modèle » — se voit dans la minute.
  3. **Rien à sauver → aucun fichier** : base vide et aucun travail = pas d'écriture. `ResultatApplication.sauvegarde` devient `string | null`.
- ⚠ **`travail` est dans les SAUVEGARDES, jamais dans les MODÈLES.** Un modèle est une population réutilisable : y embarquer les analyses d'un exercice passé les ferait ressurgir chez les joueurs du suivant. **Vérifié** : un modèle capturé contient `users`, `groups`, `graphe` — et **pas** `travail`.
- ⚠ **Les verrous et les instantanés de versement ne sont PAS sauvegardés** : les uns expirent seuls, les autres n'ont de sens que dans la minute. Les restaurer ressusciterait des verrous fantômes.
- ⚠ La restauration fait **table rase d'abord** sur rangements et planches joueurs : sinon une planche que la sauvegarde ignore survivrait à la restauration.
- **Aller-retour vérifié** : 2 lectures posées → application (lectures à 0, sauvegarde contenant 2 lectures) → restauration → **les 2 lectures reviennent, nommément**, planches et rangements intacts. Purge vérifiée : 4 applications d'affilée → **3 fichiers**.
- ⚠ Conséquence assumée du plafond : **4 applications successives effacent l'état d'origine**. C'est le prix du choix, et il est explicite.
- 💡 Piste écartée à raison : garder *volontairement* un exercice, c'est **capturer un modèle** — le geste explicite. La sauvegarde automatique est un filet, pas une archive.

### 🔴🔴 DÉCOUVERT EN TESTANT — appliquer un modèle DÉTRUIT toutes les lectures des joueurs
- **Le fait** : `eho_lectures.avatar` porte `onDelete: Cascade`. `remplacer()` fait `tx.user.deleteMany({})` → **toutes les analyses de tous les joueurs disparaissent**, silencieusement, à chaque application de modèle. Constaté en direct : les 6 lectures de `joueur_test` sont passées à 0.
- ⚠ **La sauvegarde automatique ne les couvre pas** : le fichier `data/eho/backups/*.json` contient `users`, `groups` et désormais `graphe` — **jamais `lectures`, `dispositions` ni les planches des joueurs**. Il n'y a donc rien à restaurer.
- ⚠ **C'est ANTÉRIEUR à ce travail** (le cascade et `remplacer` existaient), mais je l'ai déclenché : 6 lectures d'essai perdues. Ce qui a **survécu** : `eho_graphes` et `eho_dispositions` (aucune clé étrangère vers `users`).
- 💡 **Correctif proposé à l'utilisateur, non appliqué** : inclure `lectures` + `dispositions` + planches des joueurs dans la sauvegarde d'avant-application, et les **réattacher après** (les identifiants d'avatars sont conservés par le modèle, la réattache est donc exacte). À défaut, au minimum **avertir** dans l'écran « Modèles d'EHO ».
- 🔁 **État remis d'aplomb** : modèle `SKOLKAN` ré-appliqué (étiquette du modèle actif correcte, 453 avatars), modèle d'essai `ESSAI_PLANCHE` supprimé, planche officielle conservée (4 nœuds, 2 liens).

### Liens des jonctions : attache géométrique, recalculée à chaque rendu
- **Constat utilisateur** : « ça part dans tous les sens, une card est en haut alors qu'elle se connecte au point à droite » + « je ne veux plus d'espace entre le lien et le point/encadré ».
- **Cause** : une jonction portait **quatre accroches fixes**, et l'accroche choisie au moment du tracé était figée dans le plan. Un lien déclaré « en haut » repartait vers le haut même une fois la carte déplacée à droite — et rien ne suivait le mouvement.
- **Livré** : `ancrer(boite, vers)` — le point du **bord** qui regarde l'autre extrémité, **recalculé à chaque rendu**, donc il glisse le long de la jonction quand on déplace la carte. Deux formes : **disque** pour la jonction nue (≤ 20 px), **rectangle** pour la jonction nommée (on pousse le vecteur jusqu'au premier bord). Le point tombe **exactement sur le bord** → plus d'espace.
- ⭐ **Les DEUX bouts s'ancrent** dès qu'une jonction est en jeu, carte comprise : une jonction n'a pas de côté, garder l'accroche manuelle côté carte reproduisait le défaut. **Entre deux cartes, rien ne change** — les côtés choisis sont un choix du joueur.
- ⚠ **C'est le NŒUD qui fait foi, plus l'accroche** (`type === "connecteur"` via `useInternalNode`) : les plans enregistrés avant les quatre accroches se comportent comme les autres.
- Chaque bout vise le **centre** de l'autre, jamais son ancrage : sinon les deux se poursuivraient sans se fixer.

### ⭐ Filet de sécurité des planches relationnelles (`eho_graphe_versions`) — suite directe de l'incident
- **Déclencheur** : les deux écrasements ci-dessous. `eho_graphes` ne gardait **qu'une ligne par porteur, réécrite en bloc, sans historique**. Proposé à l'utilisateur, accepté (« oui tu peux le rajouter »).
- **Schéma — additif uniquement** : nouveau modèle **`EhoGrapheVersion`** (`eho_graphe_versions`) — `playerId`, `contenu` (l'état complet d'avant), `auteur` (**celui dont on sauve le travail**, pas celui qui écrit), `motif`, `creeLe`, index `(playerId, creeLe)`. `prisma db push` → « in sync », rien de supprimé.
- ⚠ **Surtout PAS un instantané par enregistrement** : la planche s'enregistre après chaque seconde de repos — on noierait la table et la seule version utile serait introuvable. `lib/graphe-versions.ts` ne retient qu'aux moments qui veulent dire quelque chose :
  1. **`force`** — acte délibéré et lourd (transfert d'encadré, restauration) : toujours ;
  2. ⭐ **quelqu'un d'autre a écrit en dernier** — LE cas à protéger sur une planche collective : je m'apprête à recouvrir le travail d'un voisin ;
  3. le dernier instantané date de **plus de 3 minutes** — on jalonne une longue séance sans la hacher.
  Au-delà de **20 versions** par porteur, les plus anciennes s'effacent.
- ⚠ **`conserverEtat` ne lève jamais** (try/catch silencieux, commenté comme tel) : un filet qui empêcherait d'enregistrer ferait perdre le travail qu'il prétend sauver.
- **Restaurer conserve d'abord l'état courant** → on peut **annuler l'annulation** (vérifié : motif `avant restauration`). Exception voulue : un état **vide** n'est pas conservé, il n'y a rien à sauver.
- ⚠ **Après restauration, l'écran RECHARGE la page.** Sans cela, le client garde l'ancien plan en mémoire et son enregistrement différé le réécrit une seconde plus tard — la restauration serait annulée toute seule.
- ⚠ **L'appartenance de la version au porteur est revérifiée** : l'identifiant est un entier, il se devine. Sans ce contrôle on lirait — et on écrirait — la planche d'un autre groupe.
- **UI** : bouton **« Historique »** en tête de planche → liste des 20 derniers états (quand, combien de cartes/liens, **de qui**, pourquoi), bouton « Restaurer » avec confirmation.
- **Vérifié de bout en bout** : planche du GT vidée d'un `PUT` → l'état de 5 nœuds/3 liens apparaît dans l'historique au nom de `joueur_test` → restauration → planche revenue (MERCURE + conseil). Refus : version d'une autre planche → 404 · version inexistante → 404 · sans session → 401 · GT dont on n'est pas membre → 403.
- ⚠ **`prisma generate` → redémarrage du serveur de dev** (4ᵉ rencontre du même piège).

### 🔴 Deux écrasements de la planche de l'utilisateur, le même jour
- **Ce qui s'est passé** : deux fois, j'ai écrit un plan d'essai sur une planche relationnelle **en production d'usage** — celle de `joueur_test` pendant qu'il travaillait dessus, puis celle du **GT 1re Division** sans l'avoir lue au préalable. `eho_graphes` = **une ligne par porteur, écrasée en bloc, sans historique**.
- ⚠⚠ **Règles à tenir désormais** : (1) **lire avant d'écrire** toute planche d'un porteur, systématiquement ; (2) ne jamais poser un plan d'essai sur un porteur vivant ; (3) pour vérifier une API d'écriture, **partir de l'état lu et n'y ajouter que le strict nécessaire**, puis retirer ses propres artefacts (fait pour le GT : nœud « travail du GT » et son lien supprimés, le versement de l'utilisateur conservé).
- 💡 **Piste** : `eho_graphes` gagnerait le même filet que l'EHO (`eho_sauvegardes` / `eho_versements`) — un instantané avant écriture. À proposer.

### 🔒 Trou de garde trouvé en vérifiant — section JOUEUR ouverte aux anonymes
- **Constat** : `(player)/layout.tsx` **n'avait aucun garde**. Sans le moindre cookie, `/mon-eho`, `/eho-gt`, `/graphe` et `/avatars` répondaient **200** — pages vides (les routes `/api` répondent bien 401) mais coque, navigation et libellés servis à un inconnu. La section **animation**, elle, était gardée depuis le 2026-09-14.
- **Corrigé** : garde côté serveur, sur le modèle de `(admin)/layout.tsx`. On n'y vérifie **qu'une chose — être connecté** : il n'existe pas de rôle « joueur », et un animateur doit pouvoir ouvrir ces écrans (c'est ainsi qu'il contrôle ce que voit un joueur).
- **Vérifié** : anonyme → **307** sur les quatre pages ; joueur → 200 ; animateur → 200 partout.
- ⚠ **Règle** : *une page qui répond 200 à un inconnu est une page ouverte, même vide.* Chaque groupe de routes doit porter son garde — ne pas supposer qu'un groupe voisin protège.

### Contrôles de la séance
- `npm run test` **71/71** · `npm run test:bio` **538/538** · `npx tsc --noEmit` et `npx eslint` **sans erreur**.
- ⚠ **Lancer `tsc` dans le clone d'exécution `C:`**, jamais dans `D:` : sur D: (exFAT) le client Prisma ne peut pas être généré, et `tsc` y crache 40 erreurs fantômes sur des modèles pourtant présents.
- Pages vérifiées en conditions réelles (cookies de session forgés) : `/graphe`, `/mon-eho`, `/eho-gt` **200** côté joueur, `/eho-joueurs` **200** côté animateur ; plan d'essai à deux jonctions (une nommée, une anonyme) rechargé depuis l'API.
- ⚠ **Troisième rencontre du même piège** : client Prisma périmé après `prisma generate` → **redémarrer le serveur de dev**.

### ⏭️ Reste à faire
- **Concurrence sur la planche relationnelle collective** : aujourd'hui **dernière écriture gagnante**, sans verrou (à trancher — le grain « carte » du verrou EHO ne s'y transpose pas).
- Remplacer les GT d'essai « 1re Division » / « 27e Brigade » par les **vrais groupes**.
- Toujours en attente : arbitrage des **10 routes API sans autorisation** (§ 8bis de `MEMOIRE.md`).

## 2026-09-14 — EHO PLEIADE : sécurité des écrans, rangement du joueur, refonte visuelle (branche `MEYTRE`)

Séance longue, entièrement dans `cecpc-pleiade/eho`, branche `MEYTRE`. Rien sur le serveur : tout en local (`C:\CECPC\PLEIADE\eho`, port 3001).

### 1. Cloisonnement animateur / joueur

- **La navigation suit le rôle** : rubrique « Animation » (configurer l'EHO) + « Joueurs » (ce qu'ils en ont fait) pour l'animateur ; rubrique « Joueur » seule pour l'entraîné. `lib/roles.ts` centralise les rôles admissibles (`admin`, `realm-admin`), partagé par le garde d'API, le garde de layout et la barre.
- ⚠ **Découverte : toute la partie animation était OUVERTE sans authentification** (`/dashboard` répondait 200 sans session). Verrou posé **côté serveur** dans `(admin)/layout.tsx` : anonyme → `/login`, opérateur sans rôle → `/mon-eho`. Vérifié 14/14 (anonyme, joueur, animateur × 9 pages).
- **Panne latente révélée** : `KEYCLOAK_CLIENT_SECRET` du `.env` (`eho-secret`) ne correspondait pas au client Keycloak (`eho-dev-secret`). Keycloak validait l'identité puis refusait l'échange du code — « Server error » générique. Personne ne l'avait vu **parce qu'on ne se connectait jamais** : les écrans étaient ouverts et mes vérifications passaient par des jetons obtenus directement.
- **Filtrage des planches** : `lib/keycloak-admin.ts` demande au realm qui porte un rôle d'animation ; ces comptes sont exclus de la liste des joueurs ET du classement des avatars mal lus. Un animateur qui essaie le dispositif ne fausse plus les statistiques de ses entraînés. Échec Keycloak → filtre désactivé (jamais un écran vide).

### 2. 🔴 Bug de conception grave : la dégradation silencieuse

Deux incidents de la même famille, remontés par l'utilisateur :

- **« Je suis en vue joueur »** alors qu'il était `thomas` (animateur). Cause : quand le rafraîchissement du jeton échoue, `auth.ts` **vide les rôles** ; la barre en déduisait « pas admin, donc joueur » et repliait le menu **sans rien dire**. L'interface annonçait un rôle faux. Corrigé : bandeau « Session expirée — ce menu ne reflète pas votre rôle réel » + bouton de reconnexion, pastille « rôle inconnu », et les écrans d'animation renvoient vers `/login` au lieu de déposer l'animateur sur la planche joueur. La barre est en outre devenue **collante** : le compte connecté était auparavant en bas d'une page de 4 000 px, donc invisible.
- **« Appliquer a vidé tout le package STARTEX »** : la lecture du package renvoyait 401 (session expirée) et le code traitait cet échec comme **un package vide**. Aucune donnée perdue (journal d'activité vierge), mais avec un autre enchaînement le retrait des 62 aurait été réellement envoyé.

> ⚠ **Règle tirée de ces deux incidents : un échec de lecture ne doit JAMAIS être présenté comme un résultat valide.** Lever, afficher, désactiver l'action — mais ne pas rendre « vide » ou « sans rôle » ce qu'on n'a pas pu lire.

Durcissements appliqués au package : la lecture lève au lieu de rendre un ensemble vide ; le bouton reste désactivé tant que le package n'est pas connu ; **« Appliquer » relit le serveur** avant de calculer l'écart (au lieu de se fier à une copie locale vieillie) ; un retrait de plus de 5 avatars représentant la moitié du package demande confirmation ; l'état est **relu** après application au lieu d'être supposé.

### 3. Package STARTEX — l'écran manquant

L'API existait depuis le portage, **sans aucune interface** : il n'y avait donc aucun endroit correct pour modifier le package. Mode sélection ajouté au trombinoscope (★ pleine / ☆ creuse, pastilles `+`/`−` de ce qui va changer, barre d'action collante, rien d'écrit avant « Appliquer »).

⚠ **Faille trouvée en chemin** : cocher le groupe STARTEX depuis la fiche d'un avatar **n'appliquait pas la purge des estimations** — exactement le symptôme « Lena Peters mal placée » du 10 septembre. La règle est désormais écrite une fois (`purgerEstimations`) et appliquée sur **tous** les chemins.

### 4. Ce que le joueur peut faire de sa planche

- **Curseur d'alignement** (−100 bleu · 0 neutre · +100 rouge) : porte le camp ET la force de conviction d'un seul geste. ⭐ Le curseur est la **valeur de référence**, `campEstime` en est **déduit côté serveur** — deux champs disant la même chose finissent toujours par se contredire, et c'est sur le camp que la comparaison marque les écarts. Colonne `camp_curseur` ajoutée, script de reprise idempotent `npm run backfill:curseur` pour les lectures antérieures.
- **Ordre libre des cartes** dans une zone, puis **rubriques créées par le joueur** (« Politique » dans MERCURE…), avec renommage et suppression sans perte.
- ⭐ **Choix de stockage** : une **seule ligne par joueur** (`eho_dispositions`, JSON zone → rubriques + listes). Une colonne par carte aurait écrit 391 lignes pour remonter un avatar d'un cran. Les listes sont **partielles** : seul ce qui a été déplacé à la main est enregistré. Le format initial (liste simple par zone) est relu sans perte par `normaliserDisposition`.
- L'ordre enregistré est calculé sur la zone **complète**, recherche ignorée : filtrer puis déplacer aurait effacé la position des cartes masquées.
- **La vue animateur reproduit la planche à l'identique** — mêmes rubriques, même ordre, même ordre de repli (les deux écrans appellent la même fonction de répartition).

### 5. Fiches et lisibilité

- **La fiche du trombinoscope ne s'ouvrait pas** : `<dialog>` natif + `showModal()`, cause exacte non identifiée (pas de navigateur pilotable sur le poste). Remplacé par la surcouche qui fonctionne partout → **les trois fiches de l'application partagent une seule mécanique** (`components/fiche.tsx` : Modale, Biographie, Champs, Rubrique, LiseréCouleur).
- **Les bios ne sont pas des pavés** : 57 des 262 sont des **fiches structurées de countrybook** (`Parcours : … | Objectifs : … ; … ; …`), une est en **Markdown**, le reste en prose continue **sans un seul saut de ligne** (la plus longue : 3 006 caractères). `lib/bio.ts` reconnaît la structure et la restitue en rubriques et listes ; la prose est aérée en paragraphes. **Aucun mot n'est modifié.** Test sur les 262 bios réelles : `npm run test:bio`, **538/538**, le plus long bloc passe de 1 411 à 612 caractères.
- Fiche sur **deux colonnes** (état civil en rail, biographie à droite), champs `aime`/`deteste`/`email` qui n'arrivaient jamais à l'écran.

### 6. Ergonomie et design

- **Barre repliable** (68 px en icônes), choix retenu et synchronisé entre onglets via `useSyncExternalStore`.
- **Planches en pleine largeur** (le trombinoscope était bridé à 1 600 px) ; le Comparatif reste borné à 1 500 px — c'est un écran de lecture.
- **Fusion « Avatars » + « Trombinoscope » en une seule entrée**, avec bascule **Planche | Liste** ; la planche est la vue par défaut. Bouton « + Nouvel avatar » sur les deux vues, **un seul formulaire** (`components/nouvel-avatar.tsx`).
- Libellés corrigés : ce bouton crée un **avatar**, pas un « utilisateur » — plus aucune occurrence du mot dans les écrans d'animation.
- **Trombinoscope aligné sur la planche joueur** : bandeau pays + panneau attaché, catégories en filet de couleur + libellé + effectif. Le gris est réservé au panneau ; les cartes restent sur blanc (les fiches non dirigeantes sont en #fafafa et s'y fondraient).
- Indicateur de dev Next déplacé en bas à droite : il recouvrait la déconnexion de la barre repliée.

### 7. Vérifications de la séance

Aller-retour Excel prouvé : export (453 avatars, 22 colonnes, onglet groupes) → modification d'une fiche → ré-export (la modification y est) → **réimport : `created 0, updated 453, refused 0`**, 58 groupes, 1 643 appartenances, 62 STARTEX, portraits et lectures intacts. Appariement **par `username` uniquement**.

⚠ Rappel : le **modèle SKOLKAN n'est pas un fichier Excel** mais un instantané JSON (`data/eho/templates/skolkan/`) capturé depuis la base — il conserve les identifiants, ce que le classeur ne fait pas.

### 8. Pièges d'environnement rencontrés (à ne pas réapprendre)

- **Après `prisma generate`, REDÉMARRER le serveur de dev** : il garde l'ancien client en mémoire et les écritures échouent en 500. Vu deux fois.
- **Toujours contrôler le code HTTP** dans les scripts d'essai : un script qui parse la réponse sans regarder le statut avale les 500 et fait croire que tout marche.
- Les sessions de test expirent au bout d'une heure : un 401 en cours d'essai n'est pas un bug de l'application.

### 9. État final

Base : **453 avatars · 58 groupes · 1 643 appartenances · 62 STARTEX · 6 lectures · 1 disposition**. `tsc` et ESLint propres (hors avertissement `<img>` préexistant), **71/71** tests trombinoscope, **538/538** tests bios.

⚠⚠ **Toujours ouvert** : les **10 routes API sans contrôle d'autorisation** (`/api/users`, `/api/groups*`, `/api/import`, `/api/uploads*`, `/api/activity`, `/api/avatars/export`). `GET /api/avatars/export` télécharge **toute la bibliothèque sans authentification**. Le dépouillement de la planche joueur reste contournable par `GET /api/users`.


## 2026-09-11 (suite 2) — Modèle SKOLKAN créé · 🔴 incident : suppression accidentelle des 63 groupes

- **Question utilisateur « pourquoi 473 avatars ? »** — décompte établi : **453 à nous** (451 de la bibliothèque après retrait du doublon Gavrilov **+ HETTA et Kimberley**, créés la veille depuis le diagramme RENS DELATTRE 26) **+ 20 avatars de démonstration** préexistants dans le nouvel EHO (noms français génériques, groupes « Journalistes / Population civile / Autorites locales / Groupe hostile / Influenceurs » — données de Xavier, pas les nôtres). Les 20 ont été supprimés → **453**.
- 🔴 **INCIDENT — ma faute, réparé.** En voulant purger les groupes de démonstration devenus vides, j'ai jugé « vide » tout groupe dont le compteur ne portait pas le nom que j'avais **supposé** (`_count.users` / `userCount` / `nbAvatars`) — or `/api/groups` n'expose aucun de ces champs. **Les 63 groupes ont donc été supprimés**, CAMP ROUGE / STARTEX / EXERCICE * compris, et le modèle capturé dans la foulée était vide de groupes.
  - **Dégâts** : 0 appartenance, 0 groupe. **Avatars, fiches et 118 portraits INTACTS.**
  - **Réparation** : réimport du classeur → `created 0, updated 453, refused 0` → **58 groupes, 1 643 appartenances, STARTEX à 62** ; modèle erroné supprimé puis **recapturé correctement (453 avatars / 58 groupes)**.
  - ⚠ **Leçon à appliquer partout : ne JAMAIS déduire un champ d'API par supposition avant une suppression de masse.** Lire la réponse réelle d'abord (un simple `GET` l'aurait montré), et pour toute opération destructive, vérifier sur UN élément avant de boucler.
- ✅ **Modèle `SKOLKAN` disponible** dans « Modèles d'EHO » (453 avatars, 58 groupes, package STARTEX inclus) aux côtés de `VIERGE`.

## 2026-09-11 (suite) — EHO PLEIADE : STARTEX, planche joueur et comparaison portés (branche `MEYTRE`)

- **Demande utilisateur** : porter STARTEX + comparaison vers le nouvel EHO, **sans la notion de cellule** (mise de côté), avoir **tous les avatars** dans l'EHO de PLEIADE, une **vue joueur** où il range les cartes (sauf les STARTEX) et la **comparaison** animateur/joueur. Travail exigé dans le dépôt **`cecpc-pleiade/eho`**, branche **`MEYTRE`**.
- **Base retenue (validée par l'utilisateur)** : `origin/feat/avatars-sans-keycloak` — 3 commits de nos sessions précédentes (compte `ViktorGlarak`) qui avaient déjà porté **l'affranchissement Keycloak des avatars**, le **trombinoscope** (`src/lib/trombinoscope.ts` : thèmes, rangs, regroupement) et les **modèles d'EHO** (catalogue, capture, application verrouillée, sauvegardes). `MEYTRE` créée depuis cette branche pour ne rien casser.
- **Livré (commit `8c10b87`, poussé sur `origin/MEYTRE`)** :
  - schéma : **un seul modèle ajouté**, `EhoLecture` (`eho_lectures`) — la lecture d'UN joueur (`playerId` = `sub` Keycloak, sans clé étrangère) sur UN avatar ; séparée de `users` par construction ;
  - **STARTEX = un GROUPE** nommé « STARTEX » → rien de plus au schéma, et **le package voyage dans les classeurs** (vérifié : les 62 autorités sont arrivées par l'import Excel) ; entrer au package **purge** les rangements déjà posés, conserve les notes ;
  - API : `/api/eho/startex` (GET+POST, admin), `/api/eho/mon-eho` (GET, tout opérateur), `/api/eho/mon-eho/[avatarId]` (PUT), `/api/eho/comparaison` + `/[playerId]` (admin) ;
  - UI : page joueur **`(player)/mon-eho`** (glisser-déposer natif HTML5, aucune dépendance ajoutée, équivalent clavier par la fiche) et **`(admin)/comparaison`** (tuiles par joueur, avatars les plus mal lus, détail officiel/joueur avec verdicts ✓/✗) ; entrées ajoutées à la Sidebar.
- ⚠ **Écart de zone calculé sur la ZONE attendue, pas sur le pays brut** : un avatar sans pays (ONU, CICR) est attendu en « Autre / International » — sinon un rangement juste compterait pour faux.
- ✅ **Vérifié 8/8 en conditions réelles** (comptes Keycloak `joueur_test` / `anim_test` créés dans le realm `cecpc`, jetons par flux mot de passe sur le client `eho`) : 62 au package · 403 joueur sur `/startex` et `/comparaison` · **473 cartes dont 0 champ officiel sur un non-STARTEX** · Olamao pré-placé Mercure/rouge avec sa bio · rangement d'un non-STARTEX OK · **re-rangement d'un STARTEX ignoré mais note conservée** · zone inventée refusée (400) · comparaison : 63 lignes, STARTEX jamais en écart, note visible.
- **Avatars chargés** : **453 importés** depuis `BIBLIOTHEQUE_TEST_3_EXERCICES.xlsx` (0 refus — le contrat d'import de la branche accepte nos classeurs tels quels) + 20 de test = **473** ; **118 portraits transférés** depuis l'ancienne base MASTORION via `/api/uploads` (total 138 avec photo), servis en HTTP 200.
- ⚠⚠ **FAILLE DE SÉCURITÉ SUR LA BRANCHE DE BASE, À TRANCHER** : **10 routes API n'ont AUCUN contrôle d'autorisation** (`/api/users`, `/api/users/[id]`, `/api/groups*`, `/api/import`, `/api/uploads*`, `/api/activity`, `/api/avatars/export`). **Démontré** : sans aucune authentification, `GET /api/users?limit=2` renvoie les 473 avatars avec `pays`, `label`, `activite`, `observations`. **Cela annule le dépouillement de la planche joueur** — un joueur n'a qu'à appeler cette route. ⚠ Tension produit à arbitrer : la page `(player)/avatars` (choix d'avatar) consomme `/api/users` et a besoin des identifiants — la fermer telle quelle casserait cette page. Piste recommandée : **charge utile réduite pour les non-admins** sur `/api/users` + `exigerAdmin` sur import/export/activity/uploads.
- ⚠ Contrainte d'environnement : **D: est en exFAT → aucun binaire natif ne s'exécute** (`next build` et `prisma db push` échouent en EPERM). D'où un **clone d'exécution `C:\CECPC\PLEIADE\eho`** (NTFS) où tournent npm, Prisma et le serveur de dev (port **3001**) ; le dépôt D: reste la copie de référence. Même schéma que pour mastorion.

## 2026-09-11 — Création de l'agent + première analyse de `D:\CECPC\PLEIADE`

- **Déclencheur utilisateur** : « le programme devait s'appeler MASTORION, maintenant MASTORION devient simplement un réseau social et à terme on lui changera de nom » → créer un agent **PLEIADE** qui comprenne le **système global**, et mettre à jour l'agent MASTORION en conséquence.
- **Analyse en lecture seule de `D:\CECPC\PLEIADE`** : 3 dépôts git clonés (`pleiade-platform`, `mastorion`, `eho`), organisation GitHub **`cecpc-pleiade`** (l'ancien `XTalandier/mastorion-v0` est dépassé). Un 4ᵉ dépôt, `pleiade-infra`, est référencé mais **non cloné** sur ce poste.
- **Sources lues** : les `CLAUDE.md` de `pleiade-platform` (187 l., très complet — architecture serveur, zones, instances, Keycloak, catalogue, conventions, PKI) et de `mastorion` (242 l.) ; le `CLAUDE.md` de `eho` ne contient qu'un renvoi vers `AGENTS.md` (gabarit Next.js) → **l'EHO n'a pas encore de documentation propre**, sa connaissance vient de la lecture du code.
- **Architecture retenue en mémoire** : orchestrateur de **zones** (1 realm Keycloak par zone) contenant des **instances** d'apps (compose + .env + client KC + route Traefik générés) ; serveur 192.168.10.10 sous **Podman rootful** (toujours `sudo`), accès **VPN Pritunl**, Traefik en `*.mastorion.internal`, catalogue de 4 apps (`mastorion`, `eho`, `wordpress`, `webserver`).
- ⭐ **Liaison inter-instances comprise** : quand eho et mastorion coexistent dans une zone, `EHO_URL` est injecté dans mastorion, qui **résout les comptes de scénario auprès de l'EHO** (`admin/scenario-items.ts`). **L'EHO devient la source d'identité des personas.**
- ⚠ **EHO RÉÉCRIT** : ce n'est plus notre app Angular mais un dépôt **Next.js 16 + next-auth v5 + Keycloak** autonome (3 commits, stade précoce). `User.id` = **UUID Keycloak**. **Bonne nouvelle vérifiée : les champs de persona sont exactement ceux de MASTORION** (`pays`, `label`, `activite`, `observations`…) → **les bibliothèques MINERVE restent exploitables**. Import attendu en **CSV** (`csv-parse`), l'export Excel vivant côté orchestrateur.
- ⚠ **Sort de notre travail EHO Angular** : la branche **`origin/feat/eho`** (8 commits, `b2e91ec`…`89ad382`) **existe toujours** mais n'a **jamais été fusionnée** dans `main`, et `main` a divergé (Keycloak, layouts sociaux, impersonation auditée). Les fonctionnalités développées (modèles d'EHO, cellules joueurs, fiches d'analyse, **package STARTEX**, trombinoscope, vue comparative) sont **absentes du nouvel EHO** → **point à trancher avec l'utilisateur** (abandonner ou porter). Le savoir de conception reste capitalisé dans `MASTORION\MEMOIRE.md` et `MASTORION\JOURNAL.md` (09–10 sept.).
- **Créations MINERVE** : dossier `PLEIADE\` (README + MEMOIRE + JOURNAL), prompt système `SYSTEME\PROMPTS\pleiade.md`, entrée au registre `CLAUDE.md` (**21 → 22 agents**), branche de routage dans `SYSTEME\ROUTAGE.md`, compteur `NOYAU\MEMOIRE.md` mis à jour.
- **Agent MASTORION recadré** : son périmètre devient **le réseau social seul** ; chemins, organisation GitHub et statut de l'EHO corrigés dans ses fichiers.
