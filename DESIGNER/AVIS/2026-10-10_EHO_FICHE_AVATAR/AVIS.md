# Avis DESIGNER n°91 — eho, fiche d'un avatar : refonte de l'architecture de l'information

- **Date** : 2026-10-10
- **Demande de l'utilisateur** : la fiche d'un avatar dans eho « n'est pas claire, on ne sait pas quelle partie correspond à quoi ». Il faut distinguer la **réalité physique** (qui tient réellement le compte, et où : « on est tous libres de mentir sur l'identité affichée, mais pas sur la réelle possession du compte, qui est physique »), l'**identité déclarée sur le réseau social** (« ce qu'on fait croire »), le **persona** (la vérité dans la fiction, à confirmer), une future section **« Comportement IA »** (projet `PLEIADE\PROJET_AVATARS_IA.md`, décision du 2026-10-10) et les **groupes**.
- **Matière** : captures 93 et 94 (fiche de @LoloAnna, « Lolo-Anna Voryn »), code lu **sans rien modifier** : `eho\src\app\(admin)\users\[id]\page.tsx`, `prisma\schema.prisma` (`User`, `Group`, `GroupeCamp`, `CampComptesLibres`, `Appropriation`, `EhoLecture`), `src\lib\eho-joueur.ts`, `droits-avatars.ts`, `usage-avatars.ts`, `rangement-groupes.ts`, `camp.ts`, `api\eho\mon-eho`, `api\avatars\planche`, `(player)\avatars-autorises\page.tsx` ; côté apps voisines : `app-social\apps\api\src\auth.ts` (provisionnement depuis eho), `app-admin\src\lib\kit-ia.ts` (`campDe`).
- **Statut** : proposition. DESIGNER contribue, il ne tranche pas. La mise en œuvre revient à PLEIADE / ARCHITECTE, avec CYBERSECU pour les points de fuite (§5) et MASTORION pour ce que le réseau social affiche.

---

## 0. Ce que montre la fiche actuelle (constats)

| # | Constat | Gravité (0-4) | Règle |
|---|---|---|---|
| C1 | **Les titres de section ne disent ni à quoi sert la section ni qui la voit.** « Identité » contient le **compte technique** (username, e-mail), pas l'identité de l'avatar ; « Profil / Persona » mélange la vérité du personnage (bio interne) et des champs que d'autres écrans montrent aux joueurs (pays, label, âge). Seule la section « Réseau social » (cadre ambre) dit qu'elle est **visible des joueurs**. | 4 | Nielsen 2 et 6 (REF-14), règle 30 |
| C2 | **Ce que voient les joueurs est éclaté en deux sections** : « Portraits » (portrait, bannière) et « Réseau social » (description publique, certification), alors que nom affiché et @ sont dans « Identité ». Pour savoir à quoi ressemble le profil, l'animateur reconstitue mentalement 3 sections. | 3 | Proximité, règle 9 |
| C3 | **Le camp n'est lisible que dans le mur des groupes**, par une pastille pleine parmi 15. L'appartenance est dite **par la couleur seule** (pleine = membre, cerclée = non-membre), et la couleur change d'un groupe à l'autre. | 3 | Règle 10, REF-13 1.4.1 |
| C4 | **Le mot « CAMP » a trois sens dans les groupes** : l'**allégeance fictive** (`CAMP ROUGE / BLEU / NEUTRE`, lue par `campDepuisGroupes`), la **cellule de joueurs** qui l'incarne (`CAMP DIV1`, `Camp 27BIM` ; et dans eho, « Camps autorisés… » = groupes Keycloak de joueurs) et le **partage d'animation** (`PACK FORAD`, `PACK GREYCELL`). Les trois sont des pastilles identiques. | 4 | Règle 36 (une notion par mot) |
| C5 | **Le mur montre tous les groupes, membres ou non**, comme des interrupteurs (15 actifs + 229 archivés à la demande). Un clic de travers retire l'avatar d'un camp. Les groupes **protégés** (CAMP, PACK, exclusifs), qu'un animateur ne peut pas modifier (`droits-avatars.ts`), ne sont pas signalés : on l'apprend au refus du serveur. | 3 | Nielsen 5, règle 25 |
| C6 | **« Pays » est la vérité de la fiction, pas une façade** : la comparaison joueurs (`paysEstime` contre `pays`), le trombinoscope, les cartes STARTEX et le kit IA (« rangement par pays ») le lisent comme tel. Mais rien ne le dit, et il n'existe **aucun champ pour le pays ou le lieu affichés**. L'animateur est tenté d'y écrire la façade, ce qui fausserait la comparaison. | 4 | — |
| C7 | **La couche réelle existe dans les données, mais pas sur la fiche** : titulaire (`Appropriation` : compte gc05, cellule GREYCELL, depuis), cellules autorisées (`GroupeCamp` + groupes exclusifs + « autres comptes »), relevé d'usage (`usage-avatars.ts` : comptes fdXX / gcXX réellement connectés au réseau social, scénarios, presse). Elle vit dans « Qui utilise quoi » et l'export. | 3 | Règle 33 (un chemin évident) |
| C8 | **L'en-tête montre l'e-mail et l'UUID** (données techniques, jamais utiles en animation) ; « Supprimer » rouge plein, **aussi saillant que « Sauvegarder »** ; aucun état « modifications non enregistrées ». | 2 | Règles 6, 20, 25 |
| C9 | **Champs détournés ou vides** : « Qualifications » contient « Source bio : CASW ORION 26 » ; « Aime / Déteste », « Observations », « Origine » souvent vides, mais prennent autant de place que les remplis ; la bio interne est en **anglais** (source CASW) sans que ce soit signalé. | 2 | Règle 5 (atténuer) |
| C10 | **Fiche non habillée PLÉIADE** (indigo, blanc, police par défaut) ; pas de barre de section ni de sommaire sur une page de ~2 écrans de haut. | 1 | §2 de la mémoire DESIGNER |

---

## 1. Architecture proposée, section par section

### 1.1 Le principe : quatre couches, de la plus vraie à la plus fausse, plus le rangement

Je **confirme la troisième couche** (persona) : elle existe déjà dans les données, et sans elle la phrase de l'utilisateur ne tient pas. L'exemple « un joueur en France (réel) incarne un agent mercurien (persona) qui se fait passer pour un Arnlandais (affiché) » a **trois réponses différentes** à la question « d'où vient-il ? ». Les écrans qui comparent les lectures des joueurs mesurent justement l'écart entre l'affiché et le persona : il faut donc pouvoir les saisir séparément.

L'ordre suit **la vérité, puis la fiction, puis le masque**. C'est aussi l'ordre dans lequel on crée un avatar (qui le tient → qui il est → ce qu'il fait croire → comment il se comporte). Le rangement technique et les données de compte viennent en dernier.

```
┌ EN-TÊTE ─────────────────────────────────────────────────────────────────────┐
│ (portrait) Lolo-Anna Voryn  @LoloAnna [Copier]   🔴 Rouge   ✓ Bleu   Actif   │
│            IA : non activée                [Voir sur le réseau ↗] [⋯] [Enregistrer] │
│ ┌ Bandeau des trois couches ─────────────────────────────────────────────┐   │
│ │ ◆ RÉEL  Tenu par GREYCELL (gc05) · France   ● PERSONNAGE Mercure ·     │   │
│ │ influenceuse · 26 ans   ◐ AFFICHÉ Mercure · « Hmunich »                │   │
│ └────────────────────────────────────────────────────────────────────────┘   │
├──────────────┬───────────────────────────────────────────────────────────────┤
│ Sommaire     │ 1 ◆ Qui tient le compte (réel)                                 │
│ (collant)    │ 2 ● Le personnage (vérité dans la fiction)                     │
│ ◆ Réel       │ 3 ◐ Ce que voient les joueurs (réseau social)                  │
│ ● Personnage │ 4 ✦ Comportement IA                                            │
│ ◐ Affiché    │ 5 ▦ Rangement (groupes)                                        │
│ ✦ IA         │ 6 ⚙ Compte technique                                           │
│ ▦ Groupes    │                                                               │
│ ⚙ Technique  │                                                               │
└──────────────┴───────────────────────────────────────────────────────────────┘
```

**Une page longue avec sommaire collant, pas des onglets.** L'animateur doit **comparer** le personnage et l'affiché (pays réel contre lieu affiché, bio interne contre description publique) ; or un onglet cache ce qu'on compare (règle 34 : jamais d'onglets pour comparer, REF-21, REF-22). Le sommaire répond à « où suis-je ? » (règle 30) et ses ancres permettent d'aller droit à une couche. Au téléphone, le sommaire devient une barre horizontale défilante sous l'en-tête.

### 1.2 Code couleur et pictogramme des couches

Chaque section porte **un filet de 3 px en tête** et une **étiquette de couche** (pictogramme + mot + qui voit). La couleur n'est jamais seule : pictogramme et texte la doublent (règle 10).

| Couche | Pictogramme (Lucide, déjà en place) | Étiquette | Teinte (clair → sombre) | Pourquoi cette teinte |
|---|---|---|---|---|
| **Réel** | `Fingerprint` | « RÉEL — ne ment jamais · animation » | ardoise : filet `#64748b`, fond `#f1f5f9`, texte `#334155` → sombre filet `#94a3b8`, fond `#1e293b`, texte `#cbd5e1` | Neutre, minéral : c'est le socle, rien à « jouer » |
| **Personnage** | `Lock` | « PERSONNAGE — interne, jamais montré aux joueurs » | sarcelle : `#0d9488` / `#f0fdfa` / `#115e59` → `#2dd4bf` / `#042f2e` / `#99f6e4` | Ni rouge ni bleu (couleurs de camp), ni ambre (public) |
| **Affiché** | `Eye` | « AFFICHÉ — visible par les joueurs » | ambre : `#d97706` / `#fffbeb` / `#92400e` → `#fbbf24` / `#2a1d05` / `#fde68a` | **Reprend l'ambre déjà utilisé** pour la section « Réseau social » (Jakob, REF-06) : ambre = « attention, public » |
| **IA** | `Bot` | « IA — moteur d'animation · animation / administration » | fuchsia : `#c026d3` / `#fdf4ff` / `#86198f` → `#e879f9` / `#2e0a33` / `#f5d0fe` | Se distingue du violet `#6364ff` du réseau social (identité de l'app, avis n°78) |
| Rangement | `Tags` | « GROUPES — technique » | gris neutre de la page | Pas une couche de vérité : outil de rangement |
| Compte technique | `Settings` | « TECHNIQUE » | gris neutre, replié | — |

- Les **couleurs de camp** (🔴 / 🔵 / ⚪) ne servent **qu'au camp**, jamais à une couche (règle 20 : une couleur, un sens).
- Valeurs à passer au contrasteur avant mise en œuvre (filets ≥ 3 : 1 sur leur fond, textes ≥ 4,5 : 1 — règle 21). À reprendre en jetons sémantiques `--couche-reel / -persona / -affiche / -ia`, paires fond / texte, redéfinis en sombre (règles 1 et 2). Si eho reçoit l'habillage PLÉIADE sombre, seules les valeurs des jetons changent.

### 1.3 Les sections, dans l'ordre

#### Section 1 — « Qui tient le compte » ◆ Réel
- **À quoi elle sert** : dire, sans fiction, quelle cellule et quel compte de zone ont réellement la main sur l'avatar, et où ils se trouvent physiquement.
- **Qui la voit** : **animation et administration** (à confirmer, Q8 : un animateur GREYCELL doit-il voir qu'un avatar est tenu par FORAD ?). **Jamais les joueurs.**
- **Mode** : **lecture seule** pour l'essentiel (ce sont des faits calculés). On modifie à la source (rangement dans les groupes protégés, appropriation, libération), avec un lien « Modifier dans Rangement › » ou « Libérer ».
- **Champs** :

| Champ (libellé à l'écran) | Statut | Source |
|---|---|---|
| **Ouvert à** : « DIV 1 · GREYCELL », chaque cellule avec sa **raison** (« par CAMP DIV1 », « par PACK GREYCELL », « autres comptes ») | à afficher (calcul existant : `avatarsImpersonables`, `GroupeCamp`, `CampComptesLibres`, groupes exclusifs) | eho |
| **Titulaire** : « gc05 (GREYCELL), depuis le 7 oct. 14:02 » + Libérer | à afficher (existe : `Appropriation`) | eho |
| **Localisation réelle** de la cellule : « France — Nancy » | **à créer**, portée par la **cellule**, jamais saisie avatar par avatar (§4) | Keycloak / orchestrateur |
| **Mode de tenue** : Humain · IA (en validation) · IA (autonome) | **à créer**, déduit de la section IA | eho |
| **Utilisé réellement par** : comptes connectés (fd03, gc05), dernière publication par app (réseau social direct, scénario, presse, messagerie) ; une source injoignable est **dite** | à afficher (existe : relevé `usage-avatars.ts`) | apps de la zone |
| ⚠ **Alerte** : « Utilisé par FORAD alors qu'il n'est ouvert qu'à GREYCELL » | à afficher (existe : `alerteCamp`) | eho |

#### Section 2 — « Le personnage » ● Personnage (vérité dans la fiction)
- **À quoi elle sert** : décrire qui est vraiment l'avatar dans l'univers de l'exercice ; c'est la référence de l'analyse (comparaison des lectures joueurs) et de l'IA.
- **Qui la voit** : animation et administration. **Jamais les joueurs** (exceptions voulues : cartes STARTEX, et la fiche du joueur qui incarne l'avatar — Q9).
- **Champs, en trois sous-blocs** (le vide se replie : « Compléter le caractère — 4 champs vides ▸ ») :

**2a. Qui il est**

| Libellé à l'écran | Colonne actuelle | Statut |
|---|---|---|
| Allégeance | (groupe `CAMP ROUGE/BLEU/NEUTRE`) | **lecture seule**, lue des groupes, lien « changer dans Rangement › » — **jamais un champ** (§5) |
| **Pays d'appartenance (fiction)** — aide : « Le vrai pays du personnage. Sert à la comparaison des lectures joueurs et au trombinoscope. Ce que l'avatar prétend va dans « Ce que voient les joueurs ». » | `pays` | **à renommer** (libellé seul), à déplacer ici |
| **Catégorie (trombinoscope)** — liste fermée (POLITICIEN, MILITAIRE, INFLUENCEUR, SOCK-PUPPET…) | `label` | **à renommer**, champ texte → liste |
| Activité (métier en clair) | `activite` | inchangé |
| Âge · Genre | `age`, `genre` | inchangés (vérité du personnage) |
| Origine (lieu de naissance, racines) | `origine` | **à préciser** (Q5) |
| Religion · Situation | `religion`, `situation` | inchangés |

**2b. Comment il pense et s'exprime**

| Libellé | Colonne | Statut |
|---|---|---|
| **Biographie interne** — étiquette de langue automatique « EN » quand le texte est en anglais, et « Source : CASW ORION 26 » sous le champ | `bio` | **à renommer** (« Bio (interne — jamais montrée aux joueurs) » → l'étiquette de couche le dit déjà) |
| Caractère | `caractere` | inchangé |
| **Registre et ton** (ex. « de jeune », « soutenu, juridique ») | `langage` | **à renommer** ; la **langue** de publication part en section 3 (§3) |
| Aime · Déteste | `aime`, `deteste` | inchangés, mention « utile à l'IA » |

**2c. Notes et sources**

| Libellé | Colonne | Statut |
|---|---|---|
| **Source de la fiche** (ex. « CASW ORION 26 ») | — | **à créer** (aujourd'hui dans `qualifications`) |
| Compétences et diplômes | `qualifications` | **à renommer** ; reprise des « Source bio : … » vers le nouveau champ |
| Observations (animation) | `observations` | inchangé |

#### Section 3 — « Ce que voient les joueurs » ◐ Affiché (réseau social)
- **À quoi elle sert** : composer le profil public de l'avatar, ce qu'il **fait croire**. Tout ce qui est ici sort vers le réseau social.
- **Qui la voit** : **les joueurs** (sur le réseau social), saisie par l'animation et l'administration.
- **Disposition** : à gauche les champs, à droite un **aperçu du profil tel que le voit un joueur** (bannière, portrait, nom, @, badge, description, lieu), mis à jour pendant la saisie. L'aperçu est le meilleur antidote à la fuite : on voit ce qu'on publie (Nielsen 1 et 5).
- **Bandeau** (déjà présent, à garder) : « Visible par les joueurs. N'y mettez rien qui trahisse son camp ou son rôle. »
- **Champs** :

| Libellé | Colonne | Statut |
|---|---|---|
| Portrait · Bannière | `avatarUrl`, `bannerUrl` | **à déplacer** depuis « Portraits » |
| Nom affiché | `displayName` | **à déplacer** depuis « Identité » |
| @identifiant (copiable) — aide : « Le changer casse les scénarios qui le citent » | `username` | **à déplacer** depuis « Identité » |
| Description publique (500 car.) | `bioPublique` | inchangé |
| **Lieu affiché** (texte libre : « Strasbourg », « Hmunich ») — vide = rien d'affiché, **jamais déduit du pays du personnage** | — | **à créer** + **affichage par le réseau social** (MASTORION, Q3) |
| **Langue de publication** (fr, en, ru, ro…) | — | **à créer** (règle « langue du tweet = langue de l'avatar » ; aujourd'hui confondue avec `langage`) |
| Certification (aucune / gris / or / bleu) | `certification` | inchangé |
| Âge ou genre affichés | — | **ne pas créer** tant que le réseau social ne les affiche pas (X ne montre pas le genre) ; un champ qui ne sort nulle part induit en erreur (Q4) |
| Mention « Appliqué au réseau social : immédiatement / à la prochaine synchronisation » | — | à afficher (état visible, règle 25) |

#### Section 4 — « Comportement IA » ✦ IA
- **À quoi elle sert** : régler la manière dont le moteur d'animation fait parler l'avatar, et voir ce qu'il a fait.
- **Qui la voit** : animation et administration ; **activation réservée à l'Administration** (proposition, Q10). Jamais les joueurs (« l'origine IA reste visible de l'animation seulement », projet §4).
- **État vide** tant que le moteur n'existe pas : une ligne « Le moteur IA n'est pas encore branché sur cette zone. » plutôt qu'un formulaire mort (règle 18).
- **Champs** (tous **à créer**, à arrêter avec PLEIADE) :

| Libellé | Mode |
|---|---|
| Activation : Non · En validation (chaque texte relu) · Autonome | saisie (Administration) |
| Exemples de messages (5 à 10, dans la langue de publication) | saisie, liste |
| Plages d'activité (heures, jours) | saisie |
| Tempérament : Silencieux ◀────▶ Bavard (et part de réponses / J'aime) | curseur |
| Sujets à éviter | saisie, liste |
| Mémoire de l'avatar | **lecture seule** (du moteur) |
| Journal : ce que l'IA a publié (date, app, texte, validé par) | **lecture seule**, 10 derniers + « tout voir » |

Le moteur **lit** aussi les sections 2 et 3 (persona + affiché) : rien à ressaisir ici.

#### Section 5 — « Rangement » ▦ Groupes
- **À quoi elle sert** : ranger l'avatar dans les groupes qui servent aux autres apps (camp, partage, exercice, classement).
- **Qui la voit** : animation (groupes libres) et administration (tous).
- **Refonte** : on n'affiche **que les groupes dont l'avatar est membre**, rangés par famille (celles de `rangement-groupes.ts`), avec un bouton « + Ajouter à un groupe » qui ouvre la recherche à une colonne de l'avis n°72 (archivés masqués, recherche qui dit si elle cache un archivé).

| Famille (titre à l'écran) | Groupes | Commande |
|---|---|---|
| **Allégeance (camp de la fiction)** | `CAMP ROUGE / BLEU / NEUTRE` | **choix unique** (segmenté 🔴 Rouge · 🔵 Bleu · ⚪ Neutre · Aucun), protégé 🔒 pour l'animateur |
| **Cellules qui l'incarnent** | `CAMP DIV1`, `Camp 27BIM`, `PACK FORAD`, `PACK GREYCELL`, exclusifs (`RESEAU RZO`) | pastilles avec 🔒 et raison (« Seule l'Administration change le partage ») ; renvoi vers la section 1 |
| **Exercices** | `EXERCICE DELATTRE 26`, `STARTEX`… | pastilles retirables |
| **Classement** | `MER - INFLUENCEUR`… | pastilles ; avertissement doux si le classement contredit le pays ou la catégorie du personnage |
| **Archivés (n)** | les 3 groupes archivés de @LoloAnna | replié |

L'appartenance est dite par la **présence** de la pastille (et un « × Retirer »), plus par la couleur pleine ou cerclée (règle 10).

#### Section 6 — « Compte technique » ⚙ (repliée)
- **À quoi elle sert** : les données de fonctionnement, rarement utiles.
- **Qui la voit** : administration (animation en lecture).
- **Champs** : identifiant interne (UUID, copiable), e-mail technique (**à déplacer** depuis l'en-tête et « Identité »), actif / désactivé (`enabled`), créé le, modifié le, journal des modifications (`ActivityLog`).
- **Zone de danger** en bas : « Désactiver l'avatar », puis « Supprimer l'avatar » (confirmation déjà en place).

---

## 2. L'en-tête de fiche

| Élément | Proposition | Règle |
|---|---|---|
| Portrait 56 px | initiales si absent ou cassé (comme les autres écrans d'eho) | cohérence |
| **Nom affiché** (titre de page) | `h1`, identique au libellé de la liste | règle 30 |
| **@identifiant** | gris, bouton « Copier » → « Copié ✓ » | avis n°62 |
| **Allégeance** | pastille « 🔴 Rouge » lue par `campDepuisGroupes` (eho-joueur.ts) ; au survol et au focus : « Lu dans le groupe CAMP ROUGE. Se change dans Rangement. » **Aucun camp** → « ⚪ sans camp » en gris ; **deux camps ou plus** → « ⚠ 2 camps (CAMP ROUGE, CAMP BLEU) — à corriger » | règles 10, 25 ; §5 |
| Certification | badge ✓ gris / or / bleu, comme sur le réseau social | Jakob |
| Statut | « Actif » ou « Désactivé » (texte, pas la couleur seule) | règle 10 |
| **Statut IA** | « IA : non activée » · « IA : en validation » · « IA : autonome » (pictogramme `Bot`) | règle 25 |
| **Bandeau des trois couches** | une ligne : « ◆ RÉEL Tenu par GREYCELL (gc05) · France — ● PERSONNAGE Mercure · influenceuse · 26 ans — ◐ AFFICHÉ Mercure · Hmunich ». C'est la réponse en un coup d'œil à la demande de l'utilisateur ; chaque segment est une ancre vers sa section | règle 5 ; REF-07 |
| **Actions** | **« Enregistrer »** seul en aplat (action principale) + état « 3 modifications non enregistrées » / « Enregistré à 14:02 » ; « Voir sur le réseau social ↗ » en secondaire ; menu « ⋯ » : Copier l'identifiant interne, Exporter la fiche, Désactiver, **Supprimer** (en bas, rouge texte, pas en aplat) | règles 6, 20, 25, 37 |
| Retirés | e-mail, UUID (→ section 6) | règle 5 |
| Comportement | en-tête **collant** au défilement (nom + Enregistrer), alerte si l'on quitte avec des modifications non enregistrées | Nielsen 5 |

---

## 3. Les champs ambigus

| Champ | Ce qu'il est aujourd'hui (lu dans le code) | Proposition |
|---|---|---|
| **Pays** (`pays`) | La **vérité de la fiction** : comparé à `paysEstime` des joueurs, regroupe le trombinoscope, s'affiche sur les cartes STARTEX et dans « Avatars autorisés », range le kit IA. Recopié dans la base du réseau social (`auth.ts`, l. 71), où je ne l'ai vu affiché nulle part. | Le garder **tel quel** en section 2, **renommé à l'écran** « Pays d'appartenance (fiction) », avec l'aide qui renvoie vers la façade. Créer **« Lieu affiché »** en section 3 (et, si l'utilisateur le veut, « Pays affiché »). **Aucune déduction automatique** de l'un vers l'autre : vide = rien d'affiché. On ne renomme **pas** la colonne (d'autres apps la lisent). |
| **Origine** (`origine`) | Souvent vide. La bio de Lolo-Anna dit « originally from Hcosnes-sur-Loire » : c'est la racine du personnage. | Section 2, « Origine (lieu de naissance, racines) ». Si l'utilisateur voulait une **origine prétendue**, c'est un champ de la section 3, pas celui-ci (Q5). |
| **Label** (`label`) | La **catégorie du trombinoscope** (blocs et couleurs, `lib/trombinoscope.ts`) et la « fonction » comparée à `fonctionEstimee` des joueurs. Doublonne en partie « Activité » (INFLUENCEUR / Influenceur). | Renommer « Catégorie (trombinoscope) », passer en **liste fermée** (fautes de frappe = avatar hors bloc). Garder « Activité » pour le métier en clair. Une catégorie comme SOCK-PUPPET révèle la nature de l'avatar : elle reste **interne** (section 2). |
| **Langage** (`langage`) | « De jeune » = un **registre**. Le kit IA l'imprime pourtant comme « langue / ton ». | Renommer « Registre et ton » (section 2) ; créer **« Langue de publication »** (section 3), que l'IA et le vérificateur de langue liront. |
| **Qualifications** (`qualifications`) | Sert de fourre-tout (« Source bio : CASW ORION 26 »). | Créer **« Source de la fiche »** ; « Qualifications » devient « Compétences et diplômes ». Reprise des lignes « Source bio : … » par un script, avec contrôle sur quelques fiches d'abord. |
| **Bio interne** (`bio`) | En anglais (CASW). | Étiquette de langue « EN » visible ; ne pas traduire d'office (la source fait foi) — Q6. |

---

## 4. Données qui manquent pour la couche réelle

| Donnée | Existe ? | D'où elle pourrait venir | Remarque |
|---|---|---|---|
| Cellules autorisées et pourquoi | ✅ calculée | eho (`GroupeCamp`, groupes exclusifs, `CampComptesLibres`) | à afficher, rien à stocker |
| Titulaire (compte qui se l'est approprié) | ✅ | eho `Appropriation` | à afficher |
| Comptes qui l'ont réellement utilisé | ✅ (relevé) | réseau social (journal d'audit, compte connecté), Admin (scénarios), presse, messagerie, via `usage-avatars.ts` | la presse et la messagerie ne gardent pas le compte : le dire, ne pas deviner |
| **Localisation réelle** | ❌ | **portée par la cellule** : un attribut du **groupe Keycloak** de la cellule (DIV 1 → « France — Nancy ») ou la définition de zone de l'orchestrateur `pleiade-platform` | une **seule** source, choisie par PLEIADE / Xavier ; **jamais** saisie avatar par avatar (elle mentirait vite) ; granularité à fixer (Q7) |
| Libellé lisible de la cellule (« Division 1 » pour `DIV1`) | ❌ | même source que la localisation | évite d'afficher des codes Keycloak bruts |
| Mode de tenue (humain / IA) | ❌ | section 4 + relevé d'usage | déduit, pas saisi |
| Historique de possession | partiel | `ActivityLog` (changements de groupes protégés, appropriations, libérations) | à filtrer sur ces événements |

⚠ CYBERSECU : les comptes de zone sont **anonymes** (gc01, fd03). La couche réelle s'arrête au **compte et à la cellule** : jamais le nom d'une personne, et une localisation à la maille de la cellule, pas de l'individu.

---

## 5. Pièges

1. **Rien qui trahisse le camp ou le personnage aux joueurs.**
   - L'écart M9 de CYBERSECU est toujours ouvert : `GET /api/users` d'eho renvoie la **fiche complète** des avatars à tout participant connecté. Une fiche mieux rangée ne protège rien si l'API sert tout ; à fermer **avant** d'ajouter des champs internes (source, mémoire IA…).
   - Le réseau social **recopie tous les champs du personnage** (`age`, `pays`, `religion`, `caractere`, `observations`, `qualifications`…) dans sa propre base (`app-social\apps\api\src\auth.ts`, l. 66-80). Je ne les ai pas vus affichés, mais il faut vérifier qu'aucune route vue des joueurs ne les renvoie (CYBERSECU / MASTORION). Le mieux serait que le réseau social ne reçoive **que** la section 3.
   - « Avatars autorisés » montre au joueur qui incarne l'avatar la **bio interne, le pays et la catégorie**. C'est voulu (se briefer), mais une fois le lieu affiché créé, la fenêtre doit séparer « Qui vous êtes vraiment » et « Ce que vous faites croire » (Q9).
   - L'aperçu de la section 3 ne doit jamais puiser dans la section 2 pour « remplir » un vide.
2. **Ne jamais dupliquer le camp.** Pas de colonne `camp` dans `User`, pas de champ « Camp » à saisir : l'en-tête et la section 2 **lisent** le groupe `CAMP ROUGE / BLEU / NEUTRE`. Pour les avatars qui viennent de MASTAURIGE ou du vault, le **registre MASTAURIGE** (`MASTAURIGE\MEMOIRE.md` + `avatars.js`) et les entités `vault\entities\personas\ENT-*.md` font foi : la concordance eho ↔ registre se vérifie par un **contrôle** (comme `valider.py`), jamais par une recopie dans la fiche. Le « camp estimé » des joueurs reste dans `eho_lectures`, à part (déjà le cas).
3. **« CAMP » a trois sens** (C4). Je ne propose **pas** de renommer les groupes (les apps les lisent par nom), seulement de les **présenter** dans trois familles distinctes et de mettre à jour le lexique de zone (`PLEIADE\LEXIQUE_ZONE.md`) : Allégeance / Cellule / Partage. ⚠ **Bug probable, à vérifier par ARCHITECTE** : `campDe` dans `app-admin\src\lib\kit-ia.ts` (l. 97) prend **le premier groupe qui commence par « CAMP »** : pour un avatar membre de `CAMP DIV1` et de `CAMP ROUGE`, le kit IA peut annoncer « camp : div1 ». eho, lui, utilise une table exacte (`campDepuisGroupes`) : c'est elle qu'il faudrait réutiliser.
4. **Ne pas renommer les colonnes** `pays`, `label`, `langage`, `qualifications` : social, Admin, kit IA, imports et exports les lisent. Les changements de cette refonte sont des **libellés** et des **nouvelles colonnes**.
5. **Droits visibles avant le refus** : les groupes protégés et l'activation IA s'affichent verrouillés 🔒 avec la raison pour l'animateur, en plus du refus serveur (déjà en place).
6. **Changer le @** casse les scénarios et les mentions qui le citent : l'aide le dit, et une confirmation le rappelle.
7. **Champ « Source »** : jamais de lien ni de chemin vers `DOC REF\MERCURE\RENS\01_Fiches bio` (dossier interdit).
8. **Pas de mode « voir comme un joueur »** dans la fiche (abandonné le 2026-09-21, jugé trop risqué par CYBERSECU) : l'aperçu de la section 3 est un rendu local, pas une session joueur.

---

## 6. Plan de mise en œuvre proposé (pour PLEIADE / ARCHITECTE, en local d'abord)

| Lot | Contenu | Schéma | Risque |
|---|---|---|---|
| L1 | Ordre des sections, titres, étiquettes de couche, libellés renommés, en-tête (sans e-mail, camp lu, Enregistrer seul), section technique repliée | aucun | faible |
| L2 | Rangement : membres seuls, par famille, allégeance en choix unique, 🔒 visibles | aucun | faible |
| L3 | Section « Qui tient le compte » en lecture (appropriation, cellules autorisées, usage) | aucun | moyen (appels aux apps : source injoignable dite) |
| L4 | Nouvelles colonnes : lieu affiché, langue de publication, source ; aperçu du profil ; affichage par le réseau social | oui (eho + social) | moyen |
| L5 | Localisation réelle par cellule | oui (Keycloak ou orchestrateur) | à décider par PLEIADE |
| L6 | Section IA | oui | avec le projet IA |
| Préalable | Fermer M9 (API complète aux participants) ; vérifier les routes du réseau social | — | CYBERSECU |

Contrôle avant push (règle du poste) : essai en local Docker, captures à 1440 et 390 px, en clair et en sombre (leçon de l'avis du 2026-09-24).

---

## 7. Questions à l'utilisateur

1. **L'ordre** réel → personnage → affiché → IA → groupes vous convient-il, ou préférez-vous l'affiché en premier (c'est ce que l'on modifie le plus souvent) ?
2. **Confirmez-vous la troisième couche** « Personnage » (vérité dans la fiction), distincte de l'affiché ?
3. **Lieu affiché** (et pays affiché ?) : on le crée, et le réseau social l'affiche sur le profil (comme la localisation sur X) ?
4. **Âge et genre affichés** : utiles, ou la description publique suffit-elle ?
5. **Origine** : la vraie racine du personnage, ou une origine prétendue ?
6. **Bio interne en anglais** : on la garde telle quelle (source CASW), on la traduit, ou les deux (source + résumé français) ?
7. **Localisation réelle** : à quelle maille (pays, ville, emprise) et qui la tient (attribut du groupe Keycloak, orchestrateur) ?
8. **Qui voit la couche réelle** : toute l'animation, ou un animateur ne voit-il que les avatars de sa cellule ?
9. **Joueur qui incarne l'avatar** (« Avatars autorisés ») : doit-il voir la bio interne et le pays réel de son personnage, ou seulement l'affiché ?
10. **Activation de l'IA** : Administration seule, ou aussi l'animation de la cellule qui tient l'avatar ?
11. **Camp** : pour les avatars eho de DELATTRE 26 qui ne sont ni dans le registre MASTAURIGE ni dans le vault, le groupe `CAMP …` d'eho fait-il foi ? Et voulez-vous un contrôle de concordance eho ↔ registre ?

---

**Sources** : Nielsen 1, 2, 5, 6 (REF-14) ; Jakob (REF-06) ; NN/g architecture et onglets (REF-21) ; GOV.UK navigation (REF-22) ; Refactoring UI (REF-07) ; WCAG 1.4.1, 1.4.3, 1.4.11 (REF-13) ; règles 1, 2, 5, 6, 9, 10, 18, 20, 21, 25, 30, 33, 34, 36, 37 de la mémoire DESIGNER ; avis n°29, 62, 72, 77, 78.
