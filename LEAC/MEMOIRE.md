# MÉMOIRE — LEAC

> **Source de vérité durable du système LEAC.** Créée le **2026-09-17**.
> ⭐ **RÉFLEXE NON NÉGOCIABLE : CONSULTER cette mémoire DÈS QUE LEAC EST ÉVOQUÉ · y CONSIGNER APRÈS chaque avancée**, sans attendre de rappel utilisateur.
> CR daté → `LEAC\JOURNAL.md` · règle / décision / capacité durable → **ce fichier**.

---

## 1. Identité du système

**LEAC = Logiciel d'Élaboration et d'Appui au Contrôle.**

| Champ | Valeur |
|---|---|
| Objet | **Contrôler un poste de commandement** : préparer, noter sur le terrain, concaténer le travail de l'équipe, produire la **3A** puis le **compte rendu** |
| Nature | Application web — **réécriture v3** d'un logiciel existant (v2.5 du 2022-05-19) |
| Origine | Développé par le **CDAD-R** (Rambouillet). Concrétise la fiche de besoin **CNCIA 2015**, validée **EMAT 2017** |
| Administration générale | **CECPC** |
| Finalité doctrinale | **Standardiser les procédures au niveau armée de terre** ; référentiels adaptables selon le niveau du PC, les évolutions doctrinales et le RETEX |
| Utilisateurs | 4 profils : **chef de contrôle**, **chef d'équipe**, **officier de marque (ODM)**, **contrôleur** |
| Périmètre v3 | Localhost d'abord, puis **app de zone PLEIADE** |
| Dépôt | **`cecpc-pleiade/app-leac`** (privé) · local `C:\CECPC\pleiade\app-leac` · port dev **3700** |
| Documents sources | `LEAC\REFERENCES\` — les deux mementos v2.5 (utilisateur 44 p., administrateur 34 p.) |

### ⭐ La finalité v3, telle que l'utilisateur l'a formulée
> *« Les contrôleurs se retrouvent avec LEAC sur leur tablette en extérieur, et
> lorsqu'ils reviennent au bureau, grâce au VPN et à une connexion internet, ils
> peuvent synchroniser leurs données dans le LEAC du serveur pour bien concaténer
> toutes les données de chaque contrôleur. »*

C'est **la** exigence structurante. Tout le reste en découle.

---

## 2. Les 4 acteurs et leurs rôles *(memento utilisateur § I)*

| Acteur | Grade type | Ce qu'il fait |
|---|---|---|
| **Chef de contrôle** | colonel | Lien avec la direction d'exercice. **Valide** le paramétrage (pondérations), les observations de fin de cycle, la note finale. **Seul** à tenir la synthèse générale (2 cartouches : sur le PC / sur l'exercice) |
| **Chef d'équipe** | lieutenant-colonel | Commande et coordonne l'équipe. Porte la **synthèse du fonctionnement général et du travail collectif du PC** |
| **Officier de marque (ODM)** | officier d'active | **Référent du contrôle.** Seul à pouvoir l'initialiser. Responsable du paramétrage, de la **concaténation des données** et des productions. **Clôture** le contrôle |
| **Contrôleur** | officier, expert de son domaine | Maîtrise son référentiel, note, **étaye ses observations**, fait des propositions |

⚠ **Tout membre de l'équipe, chef de contrôle inclus, est potentiellement contrôleur.**

---

## 3. Le cycle de vie d'un contrôle — 8 statuts

`INITIALISATION → EN_PREPARATION → EXPORT → EN_CONTROLE → 3A → COMPTE_RENDU → CLOTURE → ARCHIVE`

Verrous portés par les statuts :
- **3A** → les **notations** se verrouillent ; la 3A reste modifiable.
- **COMPTE_RENDU** → seuls les **commentaires** des contrôleurs restent modifiables.
- Suppression d'un contrôle possible **uniquement** en initialisation ou préparation.

---

## 4. ⭐⭐ Les règles métier à ne jamais perdre

1. **Seules les FEUILLES se notent.** *(admin § VI.B.1)* Les niveaux supérieurs
   ne font que **la moyenne des niveaux inférieurs**. ⚠ La moyenne remonte **par
   niveau**, jamais à plat sur toutes les feuilles — sinon un sous-domaine à 3
   critères pèse plus qu'un sous-domaine à 2.
2. ⚠ **Un nœud sans feuille notée n'a PAS de note — il n'a pas zéro.** Confondre
   les deux fausse toutes les moyennes au-dessus et fait croire, à la réunion
   quotidienne, que le PC est en difficulté alors qu'on n'a simplement pas encore
   noté.
3. **Pondération à deux étages** : par **fonction** (note finale) et, sur les
   domaines **transverses**, par **membre**.
4. ⭐⭐ **Le drapeau** *(§ V.A.3)* — **à quoi il sert**, car le memento ne le dit
   jamais. Il y a **DEUX sortes de domaines** :
   - **Domaine de FONCTION** (S4 Logistique, S2…) — `fonctionId` renseigné.
     **Un seul** contrôleur le note et l'observe. ⚠ **Le drapeau n'y a rien à
     faire** : il n'y a qu'une voix, celle du titulaire.
   - **Domaine TRANSVERSE** (fonctionnement général du PC, travail collectif) —
     `fonctionId = null`, `transverse = true`. **Plusieurs** contrôleurs le
     notent *(memento § IV.B : le chef d'équipe « a notamment en charge la
     synthèse du fonctionnement général et du travail collectif du PC »)*.

   Sur un transverse, les **notes** se moyennent (pondération par membre), mais
   les **observations sont du texte** : trois paragraphes ne donnent pas un
   paragraphe, aucune opération ne les fusionne. **Le drapeau désigne la voix
   reprise à la réunion** *(memento p. 27 : « le bilan de cycle de la personne
   désignée par le drapeau »)*.

   ⚠⚠ **Le drapeau appartient au DOMAINE, pas au contrôle.** Chaque transverse a
   **son propre** porteur, qui peut être quelqu'un d'autre. Un drapeau unique
   pour tout le contrôle est une **faute** : il fait disparaître du tableau de
   bord les observations du S4 sur **sa propre** grille. *(Erreur effectivement
   commise le 2026-09-17, corrigée le même jour — commit `eeb64ea`.)*

   ⭐ **Écrit comme « QUI le porte »** (`Domaine#<id>#porteDrapeau`), champ
   unique par domaine — **pas** un booléen sur chaque membre. Avec un booléen,
   deux tablettes hors ligne désignant chacune leur porteur remontent deux
   `true` sur des **cibles différentes** : la fusion les garde **tous les deux**
   et le domaine se retrouve avec **deux drapeaux**. Champ unique = même cible =
   l'horloge tranche = **un seul porteur par construction**.

   ⚠ **Écart assumé avec le memento** *(voir `app-leac\docs\COUVERTURE.md`,
   § « Écarts assumés »)* : la v2.5 dit *« SEULS ses commentaires seront vus »*.
   Appliqué à la lettre, le travail écrit des autres **disparaît** de la réunion.
   En v3 le bilan du porteur reste la **parole officielle, seule affichée par
   défaut** — l'intention est tenue — mais les autres sont **consultables d'un
   geste**, nommées. **Réversible en une ligne** si le CECPC préfère la règle
   stricte.
5. **Barème** *(admin § VI.E.7)* : note finale → tranche, niveau, label.
   ⚠ **Convention de bornes : `min` incluse, `max` exclue.** Sans elle, une note
   pile sur une borne tombe dans deux tranches ou aucune, selon l'ordre des lignes.
6. **Échelle de notation** paramétrable (note min, note max, **pas**). ⚠ La
   construire par **multiplication**, jamais par additions successives : `2 + 0,5
   + 0,5` dérive et sort « 3.4999999 ».
7. **Intitulé d'un contrôle** *(§ V.A.1)* : `TYPE_UNITÉ-EN-PROJECTION_UNITÉ-EN-MÉTRO`
   (ex. `VAP_GTD-INF_BARKHANE10_1RI`, `ANTARES_152RI`).
8. **Une unité n'est jamais supprimée, seulement désactivée** *(admin § IV.A.3)*.
9. **Un contrôleur ne modifie que les lignes physio de SON domaine** ; seul l'ODM
   change l'affectation de domaine.
10. **On ne consulte un contrôle archivé que si l'on y a contribué** *(§ VI.B.8)*.
11. **Rubrique physio** : `valeurs` vide = **saisie libre** ; sinon **liste de choix**.
12. **Import Excel complet des grilles = ÉCRASE tout l'existant** *(admin § VI.B.1)*.
13. ⭐⭐ **Figer un cycle est un état MÉTIER, pas un verrou d'écriture** *(§ III.B)*.
    Une saisie émise hors ligne **avant** le figeage et remontée **après** est
    **acceptée**, puis **signalée**. La refuser reconstruirait le défaut annoncé
    en § V.B.8 (*« toute modification durant la synchronisation sera perdue »*).
    ⚠ La comparaison se fait sur l'**horloge de Lamport**, jamais sur une date :
    deux tablettes n'ont pas la même heure. Voir `vault\decisions\DECISION-023`.
14. **Une seule réserve empêche de figer** : l'absence de porteur du drapeau.
    Tout le reste **informe sans bloquer** — sinon un contrôleur absent bloque un
    cycle indéfiniment. Le chef de contrôle est l'autorité, on l'informe.
15. ⭐ **Le cycle fait partie de la CIBLE d'une note**, pas d'un filtre :
    `Note#<cycle>:<pointId>`. Chaque cycle **renote les mêmes critères**, et
    c'est **l'écart entre cycles** qui dit si le PC progresse. Sans le cycle dans
    la clé, la 2ᵉ journée écrase la 1ʳᵉ et le découpage perd sa raison d'être.

16. **Chacun valide SA grille** *(§ III.D)* — jamais celle d'un autre. Une
    validation est un engagement sur ce qu'on a noté ; elle ne se délègue pas
    plus qu'une signature.
17. ⭐⭐ **Une saisie annulée ne remonte pas.** Tant qu'aucune opération n'est
    partie, on ne garde que l'**écart net** par rapport à ce que le serveur
    connaît (table `socle`). ⚠ Ce n'est **pas** une économie de volume : un
    retrait remonté porte une horloge récente et **écraserait la note qu'un
    collègue vient de poser hors ligne**, au nom d'un geste qui n'a pas eu lieu.
    ⚠⚠ **Jamais une opération déjà remontée** — elle appartient à l'histoire
    commune. Voir `vault\decisions\DECISION-024`.

18. ⭐⭐ **On pose une MENTION, pas une note — et on ENREGISTRE LE MOT.**
    *« Comme la note n'est pas visible, on empêche les chiffres de guider le
    contrôleur »* (CECPC) ; *« les notes ne sont pas communiquées, seul le niveau
    est révélé »* (cours CBA Rubben). Le journal garde `"Remarquable"`, jamais
    `4,75` : l'échelle est en cours de recalibration, et un journal de nombres
    aurait perdu ce que le contrôleur voulait dire.
    ⚠ **Un mot retiré de l'échelle ne vaut pas zéro** — il ne compte pas, et il
    est **signalé**. Voir `vault\decisions\DECISION-025`.
    ⚠ **Où le chiffre a le droit d'apparaître** : tableau de bord de l'équipe
    (outil de travail interne), **jamais** l'écran de notation ni le compte rendu.
19. **Échelle N4 retenue** *(à faire confirmer)* : Exceptionnel 5 · Remarquable
    **4,75** · **Très satisfaisant 4,5** · **Satisfaisant 4** · Moyen 3,5 ·
    Insuffisant 3 · Défaillant 2,5 · Mauvais esprit 2. Le haut passe au **quart
    de point**, le bas reste au demi : c'est en haut que les seuils sont serrés.
    ⚠ **Effet de bord assumé** : remonter Remarquable de 4,50 à 4,75 remonte les
    moyennes — une grille tout « Remarquable » passe du niveau 4 au niveau 5.
20. **Barème CFOT 2026** — ≥ 4,65 niveau 5 · 4,4–4,65 niveau 4 · 4–4,4 niveau 3 ·
    < 4 niveau 2. ⚠ **Remplace** celui du memento v2.5 (4,5 / 4 / 3). Le
    **niveau 1 = « non observé »** : ce n'est pas une tranche de note.
21. ⭐⭐ **Le LABEL qualifie l'EXERCICE, pas l'unité.** Les critères mesurent la
    production → un **niveau** ; les 10 exigences mesurent les conditions du
    contrôle → une **lettre**. 9-10 = A · 7-8 = B · 5-6 = C.
    ⚠⚠ **« ≤ 4 exigences OU exigences obligatoires non réalisées = contrôle non
    validé »** : neuf exigences sur dix ne donnent **pas** le label A si une des
    **cinq obligatoires** manque. Et cela peut entraîner la **rétrogradation de
    l'ANTARES en observation**.
    ⚠ « Sans ses appuis » est un **plafond** (label C max), pas une note : il ne
    peut que faire baisser. Voir `vault\decisions\DECISION-026`.
22. **La pondération porte sur le DOMAINE**, pas sur le membre qui l'observe —
    le classeur NG donne Fonctionnement général 8, Travail collectif 6, … total
    54. ✅ **Le classeur NG fait foi** ; l'annexe VII du modèle de CRF porte
    d'autres valeurs, elle est d'une autre époque.
    ⭐ **Le mandat du N+1 les adapte** : seules les valeurs *changées* sont
    enregistrées, et le compte rendu dit lesquelles s'écartent du référentiel.
23. ⭐ **Les CINQ cartouches du logiciel = les cinq rubriques des annexes V et
    VI** du compte rendu (observation générale · points forts · points faibles ·
    points à confirmer · proposition). Correspondance **exacte**. L'annexe I n'en
    reprend que trois : c'est un **résumé**, pas une perte.

### ⭐⭐ Règle 24 — Qui décide quoi *(2026-09-18)*

⚠⚠ **Keycloak dit QUI VOUS ÊTES. LEAC dit CE QUE VOUS AVEZ LE DROIT D'Y FAIRE.**
*(corrigé le 2026-09-18 sur reprise de l'utilisateur — j'avais d'abord mis
l'administration dans un rôle Keycloak, c'était faux)*

| | Répond à | Où c'est enregistré |
|---|---|---|
| **Pléiade / Keycloak** | *qui êtes-vous ?* — compte de zone (mail, nom, prénom, mdp généré) | royaume |
| **Administrateur de LEAC** | créer des contrôles, tout voir, paramétrer | **`administrateurs_entite`, base `leac`** |
| **Fonction dans un contrôle** | **quelles grilles s'ouvrent** | `membres_equipe` |

**⭐ Le bouclier Pléiade compte aussi** *(2026-09-21, demande utilisateur)* : le
rôle `admin` du client `leac`, donné par groupe depuis Pléiade, **inscrit** la
personne dans `administrateurs_entite` à sa connexion suivante (ligne
`promuPar` = bouclier, journal `administrateur.bouclier`). La vérité reste dans
LEAC ; le bouclier est une **source de plus** avec l'amorçage et la promotion.
⚠ Une ligne du bouclier **se retire dans Pléiade**, LEAC refuse de la révoquer.
⚠ Rôles lus **à la connexion** → se reconnecter après attribution.
*(Le 18/09 on avait écarté la lecture nue du jeton — « deux vérités » ;
l'inscription en base règle ce point.)* Module pur : `lib/zone/bouclier.ts`.

**Amorçage** : `LEAC_ADMINISTRATEURS` (variable d'instance, réglée depuis
Pléiade) **inscrit** des administrateurs en base au démarrage. Elle n'autorise
rien par elle-même. ⚠ En retirer une adresse **ne révoque pas** · le **dernier**
administrateur ne peut pas être révoqué.

⚠ **Ne pas retirer le bloc `roles:` de `catalog/leac.yml`** sans le vouloir :
`ensureClientRoles` **supprime de Keycloak** tout rôle absent du catalogue. Le
rôle `admin` y est laissé, marqué obsolète et **inerte**.

- **Fonction dans un contrôle** (`MembreEquipe`) → **quelles grilles s'ouvrent**.
  **Change à chaque contrôle** : le même officier est chef d'équipe lundi et
  contrôleur S2 jeudi.

**Cloisonnement des grilles** — `domainesOuverts()` dans `domaine/domaines.ts` :
transverses ouverts à tous · domaine de fonction réservé à son titulaire ·
commandement voit tout. ⚠ Une fonction **inconnue** n'ouvre **que les
transverses**, jamais tout : se tromper doit FERMER.

**Affectation en CHOISISSANT un compte de la zone** *(depuis le 2026-09-18,
suite 10)* : `lib/zone/comptes.ts` lit `GET /api/internal/zones/:zone/users`
de Pléiade (clé de service, **sans mot de passe**, `LEAC_GROUPE_UTILISATEURS`
pour restreindre à un groupe ; vide = tous) et le siège est lié à
l'`identityId` **tout de suite**. Repli : affectation par ADRESSE
(`MembreEquipe.email`), `identityId` renseigné à la première connexion. ⚠ Le
compte choisi est **relu auprès de Pléiade** côté serveur — jamais de confiance
au navigateur. ⚠ La route d'opérateur (`/api/zones/:zone/users`) reste
interdite aux apps : elle rend `rawPassword`.

**Suppression d'un contrôle** (§ V.A.7) : **seulement** en INITIALISATION ou
EN_PREPARATION — un contrôle parti porte le travail d'une équipe, il se clôture
puis s'archive. ODM ou administrateur, intitulé retapé et vérifié côté serveur,
journalisé AVANT l'effacement (`depot.supprimerControle`).

**Déconnexion** : `signOut` NextAuth **puis** `end_session_endpoint` Keycloak
avec `id_token_hint` — sans le second, Keycloak reconnecte la même personne en
silence et changer de compte est impossible.

⚠⚠ **Le cloisonnement se rejoue côté serveur** : `/api/sync` revérifie
l'habilitation. Un garde d'affichage ne protège rien. **404, jamais 403.**

### ⭐⭐ Règle 26 — La grille est une DONNÉE, figée par contrôle *(2026-09-19)*

`GrilleReferentiel` (import .xlsx/.json, rapport, activation = second geste) ;
`Controle.grilleId` fige la grille active à la création — un contrôle en cours
ne change jamais de grille. Écrans : `useDomaines()` (jamais `DOMAINES`) ;
serveur : `grilleDuControle()`. Grille embarquée = défaut et forme de toute
grille (`domaine/grille.ts`, réglage N4 par nom de feuille).
⚠⚠ **Le classeur N4 du CECPC porte 9 codes en double** (2.3.2.x codés 1.3.2.x,
1.8.3.x codés 1.8.2.x) : réparés (`~2`), affichés, **à corriger par le CECPC**.

### ⭐⭐ Règle 27 — Le serveur JUGE chaque opération selon son auteur *(2026-09-19)*

`sync/politique.ts` : note/observation ⇒ l'auteur ÉCRIT sur le domaine (droits
par domaine `MembreEquipe.droits` par-dessus la fonction) ; demande ⇒
commandement ; paramétrage ⇒ ODM ; chacun valide SA grille ; cycle suivant et
synthèses ⇒ commandement ; entité inconnue ⇒ refus. Un refus est **conservé
avec son motif, accusé, non redistribué, dit à la tablette**. Les verrous
d'écran ne protègent rien — c'est ici que la règle compte.

### ⭐ Règle 28 — Deux capacités ÉTEINTES par défaut, en attente du CECPC *(2026-09-19)*

`LEAC_PIECES_JOINTES=1` (photos/PDF par critère — classification des photos ?)
et `LEAC_AUTO_EVALUATION=1` (référents d'unité, `Controle.mode = AUTO`,
étanchéité `peutEntrer` : l'administrateur n'entre jamais dans une
auto-évaluation dont il n'est pas membre). Construites, testées, hypothèses
écrites dans le code ; déclarées dans `catalog/leac.yml` (local, non commité).

### ⭐⭐ Règle 25 — L'AUTEUR fait partie de la cible d'une note et d'une observation *(2026-09-18)*

`Note#<cycle>:<pointId>|<auteurId>#valeur` · `Observation#<cycle>:<domaineId>|<auteurId>#<champ>`.
⚠ Sans l'auteur, deux contrôleurs d'un **transverse** — noté par plusieurs,
par définition — écrivaient la même clé et **s'écrasaient** ; la synchronisation
le montrait comme une *collision* alors que c'était le cas nominal. *(Défaut
réel, corrigé le 2026-09-18.)*

**Calcul** (`domaine/apports.ts`) : domaine de **fonction** → valeur la plus
récente tous auteurs (remplacement du titulaire) · domaine **transverse** →
moyenne des moyennes de chaque observateur, **pondérée** par le paramétrage
(`poidsDe`) ; si le domaine n'est pas paramétré, tout le monde pèse 1. La case
« retenu dans la moyenne » décide qui **pèse**, jamais qui **voit**.

**Label** : le calcul propose, **le chef de contrôle valide** (diapo 20) ;
s'écarter du calcul sans justification = manque **bloquant** du CRF.

**Critères retenus** : `Selection#<id>#retenu=false` ; un critère écarté sort
des grilles et de la couverture, ses notes restent au journal.

---

## 5. ⭐⭐ Le défaut de la v2.5 que la v3 corrige

Le memento utilisateur § V.B.8 avertit :
> *« **ATTENTION** : toute modification effectuée durant la synchronisation sera
> perdue. »*

Le dispositif v2.5 imposait : **hub réseau**, **16 postes en IP fixes**, un
**« PC maître »**, des **fichiers JSON sur clé USB**, et une **réplication MariaDB
multi-maître** sur les postes.

⚠ **Les 5 « erreurs récurrentes » du memento (§ V.D) venaient TOUTES de ce
dispositif, aucune du métier** — dont la plus parlante : **une apostrophe** dans
une grille cassait la synchronisation (SQL concaténé). Elles occupaient **un
cinquième du memento utilisateur**. C'est le meilleur argument de la réécriture.

---

## 6. ⭐⭐ Le mécanisme de concaténation retenu (v3)

**Une saisie n'écrit pas une ligne : elle ajoute un ÉVÉNEMENT daté.**
`(cible, champ, valeur, auteur, horloge)` — on transporte des **intentions**, pas
des états, et on les rejoue. Code : `src/lib/sync/fusion.ts`.

| Point | Règle |
|---|---|
| Domaines disjoints | Deux contrôleurs sur deux domaines **ne peuvent pas** entrer en conflit — cibles disjointes. **99 % des retours de terrain.** |
| Horloge | ⚠ **Horloge de Lamport**, jamais l'heure de la tablette : une tablette partie 5 jours **dérive**, et l'heure murale ferait gagner la plus en retard. Lamport ne dit pas *quand*, il dit *après quoi*. |
| Ordre d'arbitrage | **Total et déterministe** : horloge → appareil → id d'opération. ⚠ Sans ordre total, deux postes synchronisés divergent **en se croyant tous deux à jour** — le pire des bugs, parce qu'il est silencieux. |
| Perdantes | **Jamais jetées** (`appliquee=false` + `motifRejet`). ⚠ *Une valeur qui disparaît sans explication est un bug perçu, même quand le calcul est juste.* |
| Vraie collision | Seulement si **deux auteurs différents** sur la même cible. Une auto-correction n'en est pas une — les confondre noie l'ODM ou lui cache un vrai désaccord. |
| Idempotence | L'UUID d'opération est généré par la **tablette** → renvoyer deux fois ne joue qu'une fois. |

---

## 7. Parti pris de design — ✅ **VALIDÉ par l'utilisateur le 2026-09-17**

> Validé sur maquette vivante (écran de notation servi en local, essayé par
> l'utilisateur) : *« Ça me plaît, on peut partir là-dessus. »*
> 👉 **Ce parti pris fait désormais référence pour tous les écrans suivants.**
> Ne pas le rediscuter sans raison ; s'en écarter demande une justification.

**La cible est une tablette tenue à la main, dehors, parfois au soleil, parfois
avec des gants.**

- **Contraste élevé** — pas de gris pâle : dehors, ça disparaît.
- **Cibles de 48 px** — les 44 px recommandés supposent un doigt nu et une main stable.
- **Clair par défaut**, sombre en option — l'inverse de l'habitude, parce que le
  sombre est illisible au soleil.
- **La note se saisit en UN appui** (rangée de crans, pas de menu déroulant) : un
  menu impose 3 gestes et masque la valeur ; sur 300 critères, **900 gestes**.
- **L'état de synchronisation est permanent**, jamais une notification fugace :
  elle arrive toujours quand l'utilisateur regarde ailleurs.
- Système **PLEIADE** : graphite + craie, angles vifs, Archivo + JetBrains Mono,
  mention `EXERCICE · NON CLASSIFIÉ`.

**Complété le 2026-09-18** (« tu peux partir sur les 4 », en production) :
- **Polices embarquées** (`@fontsource-variable`, OFL) — aucun CDN, réseau fermé.
- **Mode sombre** en option : `data-theme="sombre"`, posé par un script de tête
  avant le premier rendu (pas de flash), bascule dans l'accueil.
- **Bandeau** commun (`ui/bandeau.tsx`) : contrôle, unité + insigne, fonction.
- **Mentions compactes** sous 480 px (`Mention.court`) — la tablette en portrait.

---

## 8. État d'avancement

| Volet | État |
|---|---|
| Dépôt privé `cecpc-pleiade/app-leac` créé et poussé | ✅ 2026-09-17 |
| **Inventaire des 117 fonctions** des 2 mementos | ✅ `docs/COUVERTURE.md` |
| Schéma de données complet (annoté § par §) | ✅ `prisma/schema.prisma` |
| Moteur de fusion terrain | ✅ `src/lib/sync/fusion.ts` |
| Calcul de notation + barèmes | ✅ `src/lib/domaine/notation.ts` |
| Système visuel | ✅ `src/app/globals.css` |
| Tests de logique métier | ✅ **214/214** |
| ⭐ **Écran de notation terrain** | ✅ **écrit et validé** 2026-09-17 (`src/app/page.tsx`) — commit `aeceeb8` |
| ⭐ **Persistance hors ligne** (IndexedDB + journal d'opérations) | ✅ 2026-09-17 — `src/lib/offline/` — commit `7c640d1` |
| ⭐ **Écran de synchronisation** + revue des collisions | ✅ 2026-09-17 — `src/app/synchronisation/` |
| **Observations** (5 cartouches) persistées | ✅ 2026-09-17 — commit `a2f1f0c` |
| ⭐ **Écran de paramétrage ODM** (4 onglets § V.A) | ✅ 2026-09-17 — `src/app/parametrage/` — commits `fe90ede` puis `86da06d` (**persisté** au journal d'opérations, un champ par membre) |
| Règle de nommage de l'intitulé, **assistée et testée** | ✅ `src/lib/domaine/intitule.ts` — commit `8b51061` |
| ⭐ **Tableau de bord de la réunion quotidienne** (§ V.B.9) | ✅ 2026-09-17 — `src/app/tableau-de-bord/` + `src/lib/domaine/bilan.ts` — commit `d352962` |
| ⭐ **Écran de fin de cycle** (§ III.B / III.C) | ✅ 2026-09-17 — `src/app/fin-de-cycle/` + `src/lib/domaine/cycle.ts` — commit `edbf801` |
| **Cycles réels** (§ V.B.7) + **validation de grille** (§ III.D) | ✅ 2026-09-17 — commit `7510830` · le cycle entre dans la clé des notes |
| ⭐ **Domaines transverses** (§ V.A.3) — pondération, observateurs, drapeau **par domaine** | ✅ 2026-09-17 — `src/lib/domaine/domaines.ts` — commit `eeb64ea` |
| ⭐ **Compactage du journal** — une saisie annulée ne remonte pas | ✅ 2026-09-17 — `src/lib/sync/compactage.ts` + table `socle` — commit `675cfd3` |
| ⭐⭐ **App de zone PLEIADE déployable** — Dockerfile, workflow `prod`, sondes, Keycloak | ✅ 2026-09-17 — commit `4eccf1f` + `catalog/leac.yml` · voir `docs/DEPLOIEMENT.md` |
| ⭐⭐ **Notation par MENTIONS** — chiffres invisibles, le mot enregistré | ✅ 2026-09-17 — `domaine/echelle.ts` — commit `f0b69eb` |
| ⭐ **Lecture des grilles Excel** du CECPC, deux formats + contrôle qualité | ✅ 2026-09-17 — `import/grille.ts` · `npm run grille:lire` — commit `aeb9773` |
| ⭐⭐ **Les VRAIES grilles branchées** — 14 domaines, 1 352 critères, 5 niveaux | ✅ 2026-09-17 — commit `165009b` |
| ⭐ **LABEL de l'exercice** — 10 exigences, A/B/C, plafond « sans appuis » | ✅ 2026-09-17 — `domaine/label.ts` — commit `95c7fcb` |
| ⭐ **Compte rendu final (.docx)** — lettre + annexes I à VII | ✅ 2026-09-17 — `/compte-rendu` — commits `16627e3` et `02ca61d` |
| ⭐ **3A (.pptx)** — une diapo par domaine, taux à côté du camembert | ✅ 2026-09-17 — commit `02ca61d` |
| **Pondérations adaptables par le mandat du N+1** | ✅ 2026-09-17 — commit `e3079f8` |
| ⭐ **Branches `main` et `prod` en place sur GitHub** | ✅ 2026-09-17 |
| ⭐⭐ **EN PRODUCTION** — `https://leac.cecpc-div-eval.pleiade.internal` | ✅ 2026-09-17 au commit `a747d4f` · image au registre, 30 tables créées, sonde à 200 |
| ⭐⭐ **Synchronisation SERVEUR** — le cœur de la finalité | ✅ 2026-09-17 — `api/sync` + `lib/sync/protocole.ts` + `lib/offline/echange.ts` |
| ⭐⭐ **Habilitations** — accueil, admin vs contrôleur, cloisonnement des grilles | ✅ 2026-09-18 — `lib/zone/habilitation.ts` · règle pure testée dans `domaines.ts` |
| ⭐⭐ **L'administration appartient à LEAC**, pas à Keycloak | ✅ 2026-09-18 — `lib/controle/administrateurs.ts` + écran · amorçage par `LEAC_ADMINISTRATEURS` |
| ⭐⭐ **L'auteur dans la cible** — transverses sans écrasement, pondération par observateur calculée | ✅ 2026-09-18 — `offline/cibles.ts`, `apports.noteurDe`, `useNotesDuControle` |
| ⭐ **Label validé par le CC** · **Annexe III complète** (Scorpion, recommandations, exercice structuré) | ✅ 2026-09-18 — `label.labelFinal`, `crf.AnnexeIII`, écran CRF |
| ⭐ **Équipe réunie** (affecter / libérer depuis le paramétrage, fonctions non pourvues) · **journal d'audit** | ✅ 2026-09-18 — `parametrage/actions.ts`, `serveur/audit.ts` |
| ⭐ **Critères retenus par le mandat** · **non couverts + demande de complément** | ✅ 2026-09-18 — onglet Critères, `useDemandes`, tableau de bord |
| ⭐ **Restitutions hors ligne** (navigateur) · **unité + clôture + historique** · descriptions réinjectées (216) | ✅ 2026-09-18 |
| ⭐ **Référentiel des unités** — sélection à la création, insigne téléversé (PNG/JPEG, octets vérifiés), historique par régiment, insigne sur CRF/3A | ✅ 2026-09-18 — `lib/controle/unites.ts`, `/administration/unites`, `/api/insignes/[id]` · ⚠ insignes à fournir par le CECPC, pas récupérés sur internet |
| ⭐ **Déconnexion complète** (NextAuth + `end_session` Keycloak) · **bouton sur l'accueil** | ✅ 2026-09-18 — `lib/zone/deconnexion.ts` |
| ⭐ **Axel administrateur par défaut de l'image** (`ENV LEAC_ADMINISTRATEURS`, l'instance peut surcharger) · **amorçage corrigé** (entité créée au premier passage) | ✅ 2026-09-18 — `Dockerfile`, `administrateurs.ts` |
| ⭐ **Design complété** — polices embarquées, mode sombre, bandeau, mentions compactes | ✅ 2026-09-18 — `ui/bandeau.tsx`, `ui/bascule-theme.tsx` |
| ⭐ **Équipe composée parmi les comptes de la zone** — route Pléiade `GET /api/internal/zones/:zone/users` (sans mot de passe) + sélecteurs | ✅ 2026-09-18 — `pleiade-platform` `069b48d` · `lib/zone/comptes.ts` |
| ⭐ **Supprimer un contrôle** (INITIALISATION / EN_PREPARATION, intitulé retapé, journalisé) | ✅ 2026-09-18 — `depot.supprimerControle`, onglet Initialisation |
| ⭐⭐ **EN PRODUCTION — version `2026-09-18.7`** (`/api/sante` la rend) | ✅ 2026-09-18 — commit `e2fe00e` sur `prod` |
| ⭐⭐ **Six lots du comparatif ÉVAL-PC** (A saisie · B lecture · C droits fins + politique serveur · D comparaison · E hors ligne/démo/mobile · F grilles/pièces/auto-éval) | ✅ 2026-09-19 — 9 commits `28df915`→`1045719`, **EN PRODUCTION** version `2026-09-19.1`, 422 tests |
| ⭐⭐ **Le bouclier Pléiade INSCRIT les administrateurs** (rôle `admin` du jeton → ligne créée, `promuPar` = bouclier ; révocation refusée côté LEAC) | ✅ 2026-09-21 — `lib/zone/bouclier.ts`, commit `dfae88f`, **EN PRODUCTION** version `2026-09-21.1`, 430 tests |
| 🔴 **Volume de données rendu à `nextjs`** (défaut latent : `./data` créé root par l'orchestrateur → pièces jointes impossibles) | ✅ 2026-09-21 — `Dockerfile` sans `USER` + entrypoint `su-exec`, **EN PRODUCTION** version `2026-09-21.2` |
| **Note d'intégration pour la plateforme** | ✅ `docs/INTEGRATION-PLEIADE.md` — écrite pour qui devra comprendre sans avoir écrit |
| Glossaire, écrans d'administration | ❌ à écrire |
| Génération 3A (.pptx) / CR (.docx) | ❌ balises inventoriées, génération à écrire |
| Import/export Excel | ❌ spécifié |

**Répartition de la couverture** : 🟢 **~25 faites** · 🟡 ~48 modèle en place · ⚪ ~18
spécifiées · 🔵 **29 repensées** (le dispositif technique qui les imposait
disparaît — chacune justifiée dans `docs/COUVERTURE.md`).

---

## 9. Points ouverts / à trancher avec l'utilisateur

- ⏳ **Format d'import Excel des grilles** — memento admin § XII : *« en cours de
  rédaction »*. **Trou dans la doc source**, pas un oubli de notre part. Il faut
  un fichier réel du CECPC.
- ⏳ **Modèle de compte rendu** — § X : *« en cours de rédaction »*. Idem.
- ⏳ **Durée de vie du PIN hors ligne** : combien de jours une tablette reste-t-elle
  utilisable sans revoir le serveur ? Arbitrage sécurité / terrain.
- ⏳ **Reprise de l'existant** : importer les contrôles archivés de la v2.5, ou
  repartir à blanc ?
- ✅ ~~Ordre des écrans~~ — tous construits (notation, synchronisation,
  paramétrage, CRF, administration).
- ⏳ **P1 / P4 de l'analyse du 2026-09-18** (`ANALYSE_2026-09-18.md`) — arbitrage
  CECPC attendu.
- ⏳ **Insignes des unités** : à fournir par le CECPC (pas de récupération sur
  internet — réseau fermé, droits MinArm) ; liste des régiments (CSV) si dispo.
- ⏳ **Côté utilisateur** : créer les comptes de zone de test dans Pléiade ;
  confirmer que la déconnexion retombe sur `/connexion` (non testable en local).
- ✅ 2026-09-21 : `catalog/leac.yml` poussé (`pleiade-platform` `bbb3d4e`) —
  `LEAC_PIECES_JOINTES` / `LEAC_AUTO_EVALUATION` réglables depuis Pléiade, vides.
- ✅ 2026-09-21 : tous les dépôts Pléiade à jour sur Xavier. `package-lock.json`
  et `public/style.css` de `pleiade-platform` étaient des artefacts de mon poste,
  pas du travail de Xavier — plus rien à protéger là ; `--autostash` inutile.
- ⏳ **CECPC** : corriger les 9 codes en double du classeur N4 ; trancher
  pièces jointes (classification) et auto-évaluation (public, comptes).
- ✅ 2026-09-21 : **le rôle Keycloak `admin` reprend du service** — il porte le
  bouclier Pléiade (cf. Règle 24, « Le bouclier Pléiade compte aussi »). Il n'est
  plus obsolète : **ne pas le retirer** de `catalog/leac.yml`, `ensureClientRoles`
  le supprimerait de Keycloak avec ses attributions (leçon du 2026-09-18).

---

## 10. Règles de travail de l'agent LEAC

1. **Propriété unique** : LEAC est le **seul propriétaire** des informations du
   système LEAC dans MINERVE. Les autres agents **citent**, ne recopient pas.
2. **Consulter avant, consigner après** — y compris quand LEAC n'est qu'évoqué en
   passant.
3. ⚠ **Ne jamais annoncer un écran comme fait tant qu'il ne l'est pas.** La
   distinction *spécifié* / *implémenté* de `docs/COUVERTURE.md` est la référence.
4. **Router vers l'agent compétent** : plateforme et déploiement → **PLEIADE** ·
   code → **ARCHITECTE** · rédaction → **SECRÉTAIRE**.
5. ⚠ **Modèle de branches PLEIADE** *(voir `PLEIADE\MEMOIRE.md` §2bis)* : travailler
   sur une branche provisoire, intégrer dans `main`, et **ne jamais pousser sur
   `prod`** sans demande explicite — cela **déploie devant les participants**.
6. **Aucun détail opérationnel réel** dans les jeux d'essai : noms d'unités et de
   personnes fictifs.
