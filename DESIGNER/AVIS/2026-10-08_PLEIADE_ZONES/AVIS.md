# Avis DESIGNER n°79 — Orchestrateur PLÉIADE, page « Zones » : familles, années, éditions, instances groupées

> **Date** : 2026-10-08 · **Demandeur** : utilisateur (organisateur) · **Écran** : `pleiade-platform`, page « Zones » (`public/app.js`, `zoneCard()` et `instanceRow()`)
> **Statut** : **proposé**. Maquette interactive à valider avant toute mise en œuvre. Rien n'a été modifié dans `C:\CECPC\pleiade\`.
> **Maquette** : `index.html` dans ce dossier, servie en local par
> `& "C:\Users\MTR\AppData\Local\Python\pythoncore-3.14-64\python.exe" -m http.server 3853 --bind 127.0.0.1` (lancé depuis ce dossier) → **http://127.0.0.1:3853/**
> **Captures** : `captures\avant_61` à `avant_64` (écran actuel), `captures\maquette_*` (maquette, 1440 px et 390 px).

---

## 0. La demande, en une phrase

Les zones s'empilent dans une seule liste et leurs instances se mélangent. Il faut **ranger** les zones (exercices par année, éditions successives d'un même exercice, prototype LEAC à part), les **retrouver** par leur nom ou leur année, et **naviguer** sans dérouler 30 lignes d'instances.

---

## 1. Constat sur l'écran actuel (captures 61 à 64)

Gravité de 0 à 4, selon la grille §3.6 de la doctrine (Nielsen, REF-14).

| N° | Constat | Où | Gravité |
|---|---|---|---|
| E1 | **Une seule liste à plat**, sans famille : l'essai `essai-partage` arrive **en tête**, avant l'exercice en cours ; le prototype LEAC (`cecpc-div-eval`) est rangé comme un exercice. | 62 | 3 |
| E2 | **Rien ne dit l'année ni l'édition.** DELATTRE 2027 deviendra une zone de plus dans la même liste, sans lien avec DELATTRE 2026. Pas d'archives : un exercice terminé reste mêlé aux zones vivantes, ou doit être supprimé. | 62, 63 | 3 |
| E3 | **Toutes les zones sont dépliées** : `delattre-26` occupe à elle seule plus d'un écran (14 lignes). Trouver `orion26` demande de faire défiler toute la page. | 61, 63 | 3 |
| E4 | **La recherche ne cherche que l'identifiant** (`Filtrer les zones…`), pas l'année, ni l'exercice, ni une application (« où est TF1 ? »). | 62 | 2 |
| E5 | **Le filtre mélange deux questions** dans un seul choix exclusif : l'environnement (PROD, DEV) et l'état (ARRÊTÉES). On ne peut pas demander « les zones DEV arrêtées ». | 62 | 2 |
| E6 | **Instances triées par identifiant**, donc **la presse est éparpillée** : HEXAGONE et CICR entre le Partage et MELMIL, OCHA et Préfectures entre la Messagerie et le Réseau social, TF1 à la fin. | 61 | 3 |
| E7 | **7 à 8 boutons de zone**, en 4 styles (crème plein, vert, encadré, texte), **répétés sous chaque zone**. « Supprimer zone » est sur la même ligne que les gestes courants. | 62, 63 | 2 |
| E8 | **Une ligne d'instance = 6 à 7 icônes sans mot** (curseurs, image, œil, engrenage, bouclier, terminal), lisibles seulement au survol. L'icône « curseurs » (administration de l'app) **n'existe que pour certaines apps**, si bien que les autres icônes **changent de place** d'une ligne à l'autre. | 61 | 3 |
| E9 | **« Stop » en orange plein, 14 fois** : c'est l'élément le plus voyant de la page, alors qu'on s'en sert rarement. La **croix rouge de suppression est collée** à « Stop » (risque de clic à côté, loi de Fitts). L'instance arrêtée affiche « **Deploy** », en anglais. | 61 | 3 |
| E10 | **Le nom affiché n'est pas utilisé** : la base a une colonne `label` (`orch_zones`), mais la carte montre l'identifiant technique (`delattre-26`). Les instances ont des noms en casse libre (« cockpit », « melmil », « ocha » à côté de « EHO DE LATTRE 26 »). | 61, 62 | 1 |
| E11 | **Étiquettes en CAPITALES espacées** (PRESSE, ADMIN, LATEST, PORTAIL : 3 GROUPES) et **filtre actif en crème plein**, le même aplat que « + Nouvelle zone » : c'est ce que le socle n°77 a corrigé dans l'animation. « LATEST » est affiché partout et ne dit rien. | 61, 62 | 1 |
| E12 | **« Choisir une application »** : 12 cartes **par ordre alphabétique**, avec des descriptions de 1 à 7 lignes. L'app s'y appelle « **Admin** », mais l'instance « **Console d'animation** » (règle de vocabulaire n°77 : « animation », jamais « Admin »). | 64 | 1 |
| E13 | La zone **`exercice`** est en **PROD** alors qu'elle sert visiblement de démonstration (Agora, La Gazette, Veille) : elle se lit comme un vrai exercice. | 63 | 1 |

**Ce qui est déjà bon, et que la maquette garde** : le thème graphite et crème, Archivo et JetBrains Mono, les icônes d'instance (pupitre, radar, bulles, journal), l'adresse cliquable de chaque instance, l'indication « portail : n groupes », la date de création.

---

## 2. Recommandations

| R | Recommandation | Sources (doctrine) | Effort |
|---|---|---|---|
| **R1** | **Trois familles de zones**, dans un ordre fixe : **Exercices** → **Prototypes et outils** → **Essais**, plus des **Archives** masquées par défaut. Chaque bloc a un titre, un compte et une phrase qui dit ce qu'il contient. | Règle 27 (l'architecture avant la navigation, REF-21) ; 28 (stabilité, mémorisation, REF-24) ; 9 (proximité, REF-07) | ½ j |
| **R2** | **Les exercices sont rangés par année** (2027, puis 2026), **une zone par édition**. Les éditions d'un même exercice sont reliées par leur **nom d'exercice** : vue « **par exercice** » à l'accueil (DE LATTRE : 2026, 2027), et une barre « **Éditions de DE LATTRE** » sur la page de la zone, qui sert d'**historique**. Le choix « par année / par exercice » est mémorisé par poste. | Règles 27, 30 (« où suis-je ? »), 36 (un mot par notion) ; REF-21 | 1 j |
| **R3** | **Barre de recherche et de filtres** du socle n°77 : recherche (nom, identifiant, exercice, année **et noms des applications** ; sans accents ni casse ; « Contient : TF1 INFO » sur la carte trouvée par une instance) → segmenté **Famille** avec effectifs → listes **Année**, **Environnement**, **État** (deux questions séparées, E5) → bascule **Archives (n)**. Un résultat vide le dit, et signale les **zones archivées qui correspondent** (« les afficher »). | Avis n°77 §3.2 ; n°72 (un résultat vide dit ce qu'il cache) ; règle 37 | 1 j |
| **R4** | **Cartes de zone repliées** à l'accueil : nom affiché, identifiant, état en mot (« En ligne 14/14 », « En partie 13/14 », « Arrêtée », « Sans instance »), PROD / DEV, icônes des apps, édition, nombre d'instances (« dont 7 médias »), date. **Un clic ouvre la page de la zone**, qui commence par le **retour nommé « ← Zones »**. L'adresse change (`#zone/delattre-26`) : le bouton Précédent du navigateur marche, on peut envoyer le lien. | Règle 38 (liste-détail, REF-23) ; GOV.UK *back link* (REF-22) ; n°77 §3.1 ; règle 10 (jamais la couleur seule) | 1 j |
| **R5** | **Instances groupées par fonction**, dans un ordre fixe : **Animation** (Console d'animation, MELMIL, Cockpit) · **Réseaux et messagerie** · **Presse** · **Identités** (eho) · **Fichiers et web** (Partage, serveur web, WordPress) · **Contrôle des PC** (LEAC). La **presse est repliable** : repliée, elle montre ses logos et « 7/7 en ligne » sur une ligne ; l'état ouvert / fermé est mémorisé. La fonction est **portée par le catalogue** (`catalog.ts`, un champ `fonction` par app) : aucune saisie, et la fenêtre « Ajouter une instance » est rangée de la même façon (E12). | Règles 9, 31, 32 (2 niveaux de révélation) ; Tesler (19) | ½ j |
| **R6** | **En-tête de zone** : à gauche le nom, l'état, PROD / DEV, l'édition, l'adresse, la version, la date ; à droite **une seule action principale, « + Instance »** (crème plein), « Utilisateurs » en secondaire (geste fréquent), et un **menu « ⋯ »** : Déployer toute la zone, Sauvegardes, Storybook, Modifier la zone, Passer en DEV / PROD, Changer de version (DEV seulement), **Archiver l'exercice**, puis, séparé et **en rouge**, **Supprimer la zone**. La suppression demande de **taper l'identifiant** et propose d'archiver à la place. | Règles 6, 37 (Hick) ; 20 (une seule couleur d'alerte) ; 24 (erreurs GOV.UK) ; n°76 (Supprimer dans « ⋯ ») | ½ j |
| **R7** | **Ligne d'instance compacte**, colonnes alignées : icône · nom (+ type s'il diffère, + « portail : 3 groupes ») · adresse · **état en mot** · **« Arrêter » / « Démarrer » en bouton secondaire** · « ⋯ » (Ouvrir l'administration de l'app, Configuration, Droits, Visibilité sur le portail, Icône, Renommer, Terminal, puis **Supprimer l'instance** en rouge). Plus d'orange plein répété, plus de croix collée au bouton, plus d'icônes qui changent de place. Sous 760 px, la ligne passe sur 3 rangs. | Règles 6, 12 (Fitts), 33 (un chemin par geste) ; n°71 R5 ; n°77 §3.3 | ½ j |
| **R8** | **Trois champs nouveaux** sur la zone (famille, exercice, année), **saisis à la création et modifiables** dans « Modifier la zone ». Le **nom affiché** (déjà en base) et l'**identifiant** sont **proposés** à partir de l'exercice et de l'année (DE LATTRE + 2027 → « DE LATTRE 27 », `delattre-27`) ; l'identifiant est figé après création (il est dans toutes les adresses). Un **aperçu** dit où la zone sera rangée (« Exercices › 2027 › DE LATTRE — 2ᵉ édition, avec 2026 »). | Tesler (19) ; règle 24 (erreurs à la GOV.UK) ; 25 (état visible) | 1 j (base + API + fenêtre) |
| **R9** | **Socle commun n°77** appliqué à l'orchestrateur : segmenté en casse normale, actif en **crème pâle**, crème plein réservé à l'action principale, étiquettes **icône + mot** en sans, verbes français (« Arrêter », « Démarrer », jamais « Stop » ni « Deploy »), « Console d'animation » partout (fenêtre d'ajout comprise), « latest » rangé dans la méta. | Avis n°77 §3.2-3.4 ; règle 36 ; mémoire « animation, jamais Admin » | ½ j |

**Ce que la maquette ne change pas** : les fenêtres existantes (Utilisateurs, Sauvegardes, Storybook, Configuration, Droits, Visibilité, Icône, Terminal) sont **reprises telles quelles**, simplement ouvertes depuis les menus.

---

## 3. Modèle de données proposé

### 3.1 Trois colonnes dans `orch_zones` (migration dans `src/db.ts`, comme `zone_type` et `label`)

| Colonne | Type | Valeur par défaut | Règle |
|---|---|---|---|
| `famille` | `ENUM('exercice','prototype','essai')` | `'essai'` | Obligatoire. Une zone non classée tombe en Essais : rien ne se perd, rien ne se présente à tort comme un exercice. |
| `exercice` | `VARCHAR(64) NULL` | `NULL` | Obligatoire si `famille = 'exercice'`. Nom de la **série** (« DE LATTRE », « ORION ») : même nom = même exercice, ses éditions se rangent ensemble. Comparaison sans accents ni casse. |
| `annee` | `SMALLINT NULL` | `NULL` | Obligatoire si `famille = 'exercice'` (année de jeu, 4 chiffres). L'**édition** se déduit : nom de l'exercice + année. Pas de colonne « édition » en plus. |

**Pour les archives (R1)**, une quatrième colonne est nécessaire : `archivee_le DATETIME NULL` (vide = zone active). *À confirmer avec la question Q3 ; sans elle, pas d'archives, et le reste fonctionne.*

`PATCH /api/zones/:zone` accepte aujourd'hui `zoneType` et `imageVersion` : il faut y ajouter `label`, `famille`, `exercice`, `annee` (et `archivee`). `POST /api/zones` accepte les mêmes champs à la création. **Aucun changement** pour les instances : leur fonction vient du catalogue (R5).

### 3.2 Valeurs pour les zones existantes (proposées, à confirmer)

| Identifiant (inchangé) | Nom affiché proposé | Famille | Exercice | Année | Remarque |
|---|---|---|---|---|---|
| `delattre-26` | DE LATTRE 26 | exercice | DE LATTRE | 2026 | Exercice en cours, PROD |
| `orion26` | ORION 26 | exercice | ORION | 2026 | Exercice joué : candidat à l'archivage (Q3) |
| `cecpc-div-eval` | CECPC DIV EVAL | prototype | — | — | Prototype LEAC, pas un exercice (demande de l'utilisateur) |
| `essai-partage` | essai-partage | essai | — | — | DEV |
| `exercice` | Démonstration (exercice) | essai | — | — | Zone de démonstration en PROD (E13) : Q2 |
| *(futur)* `delattre-27` | DE LATTRE 27 | exercice | DE LATTRE | 2027 | **Exemple de la maquette**, n'existe pas |

Dans la maquette, la date de création d'`orion26` n'apparaissait pas sur les captures : elle est notée « date non relevée ».

---

## 4. Plan par étapes

1. **Maquette** (fait) : `index.html`, port 3853. Accueil, recherche et filtres qui marchent pour de vrai (« lattre », « 2026 », « tf1 »), vues par année et par exercice, page de zone, presse repliable, menus « ⋯ », Nouvelle zone et Modifier la zone avec contrôle des erreurs, Ajouter une instance rangée par fonction, archivage et réactivation, suppression confirmée par la saisie. Contrôlée à 1440 et 390 px : 0 erreur JS, 0 image cassée, pas de défilement horizontal.
2. **Accord de l'utilisateur** sur les questions du §5, puis **accord de Xavier** (propriétaire de l'orchestrateur) : la page Zones est l'écran des organisateurs, et le modèle de données change.
3. **Mise en œuvre par PLEIADE / ARCHITECTE**, dans cet ordre, **après la fin de DELATTRE 26** (l'orchestrateur gère la zone en jeu) :
   - a. Migration des 3 colonnes (+ `archivee_le`) et API (`POST` / `PATCH /api/zones`), valeurs initiales du §3.2. *(½ j)*
   - b. Champ `fonction` dans `catalog.ts` ; fenêtre « Ajouter une instance » rangée par fonction et renommée (« Console d'animation »). *(½ j)*
   - c. Accueil : familles, cartes repliées, recherche et filtres, page de zone avec `#zone/<id>`. *(1,5 j)*
   - d. Page de zone : en-tête, menu « ⋯ », lignes d'instance, presse repliable. *(1 j)*
   - e. Archivage (si Q3 = oui). *(½ j)*
   - f. **Essai en local avant tout push** (règle de la plateforme) ; relecture de conformité DESIGNER sur captures, comme pour le n°77 ; **CYBERSECU** consulté sur la confirmation de suppression et sur l'archivage (arrêt des instances, conservation des données).

---

## 5. Questions pour l'utilisateur (réponses fermées)

| N° | Question | Choix | **Recommandation** |
|---|---|---|---|
| **Q1** | Les **trois familles** (Exercices · Prototypes et outils · Essais) vous conviennent-elles, avec ces noms ? | Oui · Autres noms · Deux familles seulement | **Oui** : elles répondent à vos trois cas (exercice annuel, LEAC, zones de test), et une zone non classée tombe en Essais sans se faire passer pour un exercice. |
| **Q2** | La zone **`exercice`** (Agora, La Gazette, Veille) : on la range en **Essais** ? | En Essais · En Exercices · La supprimer après DELATTRE 26 | **En Essais**, renommée « Démonstration (exercice) ». Elle reste utile pour montrer la plateforme ; sa suppression pourra se décider après l'exercice. |
| **Q3** | **Archiver** un exercice terminé = arrêter ses instances, **tout conserver** (données, sauvegardes, storybook), le sortir de la liste, avec un geste « Réactiver » ? | Oui · Non, on supprime comme aujourd'hui | **Oui** : on garde la trace pour le RETEX sans encombrer la liste. ORION 26 serait le premier candidat. *(Un avis de CYBERSECU est à prendre sur la durée de conservation.)* |
| **Q4** | Les exercices s'affichent d'abord **par année** ou **par exercice** ? (l'autre vue reste à un clic) | Par année · Par exercice | **Par année** : c'est votre demande, et l'exercice de l'année est celui qu'on cherche le plus souvent. La vue par exercice sert l'historique. |
| **Q5** | La **presse** est-elle **repliée** par défaut sur la page de la zone ? | Repliée · Dépliée | **Repliée** : 7 médias sur 14 instances ; repliée, la ligne montre les logos et l'état « 7/7 en ligne », ce qui suffit le plus souvent. Le choix est mémorisé par poste. |

---

## 6. Sources mobilisées

- Doctrine DESIGNER, `MEMOIRE.md` §3 : règles 6, 9, 10, 12, 19, 20, 24, 25, 27 à 38.
- **REF-21** (NN/g, architecture de l'information et navigation), **REF-22** (GOV.UK, lien de retour, un seul mécanisme), **REF-23** (Material 3, liste-détail), **REF-24** (NN/g, mémorisation et fréquence des tâches), REF-06 (Hick, Fitts, Tesler, Jakob), REF-07, REF-14, REF-19 (menus et fenêtres au clavier).
- Avis **n°69** et **n°71** (deux étages de navigation, 1 action principale + « Plus »), **n°72** (un résultat vide dit ce qu'il cache), **n°76** (Supprimer dans « ⋯ »), **n°77** (socle commun : en-tête, barre de filtres, étiquettes, vocabulaire).
- Code relu en lecture seule : `pleiade-platform\public\app.js` (`zoneCard`, `instanceRow`, `openModal`), `src\index.ts` (routes `/api/zones`), `src\db.ts` (`orch_zones` : `name`, `zone_type`, `image_version`, `service_key`, `label`).
