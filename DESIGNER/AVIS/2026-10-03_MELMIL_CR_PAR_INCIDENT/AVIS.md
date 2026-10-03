# Avis n°38 — MELMIL : un compte rendu appartient à l'incident depuis lequel il a été créé

> **Date** : 2026-10-03 · **Demandeur** : l'utilisateur · **Écrans** : `app-melmil`, section « Comptes rendus du jour (D+x) » de la fiche d'un incident (`components/atelier/compte-rendu.tsx` › `ComptesRendusIncident`, `FicheCompteRendu`), fiche ouverte depuis la planche de préparation ou l'onglet Incidents (`onglets-gt.tsx` › `FicheIncident`), agrafe des cartes (`components/carte.tsx`, `planche-liste.tsx`), colonne « Pièces jointes » et tri (`tri-incidents.ts`), Synthèse (`lib/atelier/synthese.ts`).
> **Statut** : 🟡 proposé, à arbitrer par l'utilisateur. La mise en œuvre revient à PLEIADE / ARCHITECTE, **à tester en local avant tout push**.
> Suite des avis n°21 (CR partagés par jour et ETIM), n°23 (l'agrafe), n°24 (colonne « Pièces jointes »), n°32 (télécharger le bon exemplaire, garder « Importer… ») et n°34 (Synthèse).
> ⚠ DESIGNER contribue, il ne tranche pas : ce sont des propositions argumentées. Le besoin de l'utilisateur et les choix de PLEIADE / ARCHITECTE font foi.

## Besoin exprimé (2026-10-03)

> « Le système est très bon actuellement, cependant il faut que l'on puisse visuellement comprendre que l'incident 07.01.I03 possède un CR, car ce CR a été rempli depuis sa fiche. Si on clique sur le bouton "docx" on a bien tous les CR d'une même colonne qui se téléchargent à la suite comme actuellement [à garder], mais sur la planche de planification il ne faut pas que le CR soit présent sur tous les incidents visuellement, et pareil dans la fiche de l'incident : même si l'incident est lié à une même ETIM, si j'ouvre un CR on devrait avoir uniquement CE CR visible et modifiable sur son onglet (peut-être avoir un indicateur comme quoi un autre CR du même type existe via un autre incident de la même ETIM). Il faut que ergonomiquement ce soit parfait. »

On garde donc **deux notions distinctes**, qu'il faut cesser de confondre à l'écran :

| Notion | Sert à | Clé |
|---|---|---|
| **La colonne** (jour + ETIM + type) | numéroter n°1, n°2… et **télécharger le lot** (.docx, un exemplaire par page) | `jour`, `etim`, `type` |
| **L'incident d'origine** | **afficher** : agrafe, compte, section CR de la fiche, Synthèse | nouveau champ |

## Constat (lecture du code, 2026-10-03, `app-melmil` `1aa2354`)

| # | Constat | Gravité (0-4) | Source |
|---|---|---|---|
| C1 | **Un CR partagé n'a pas d'incident d'origine.** `creerCompteRenduPartage` enregistre `incident: ""`, `jour`, `etim`, `type` : on ne sait plus depuis quelle fiche il a été créé. Tout le reste en découle. | 3 | Le modèle doit porter ce que l'utilisateur veut voir (règle 19, Tesler) |
| C2 | **L'agrafe ment par excès.** `piecesDeLIncident` compte tous les CR du jour et des ETIM de l'incident : un seul PSYREP rempli depuis 07.01.I03 met une agrafe sur **tous** les incidents de D+x qui ont cette ETIM. Le repère ne distingue plus rien (et la Synthèse « sans pièce jointe » est faussée de la même façon). | 3 | Heuristique 1 « état visible », un signal qui est partout ne signale rien (Von Restorff, REF-06) |
| C3 | **La fiche montre et ouvre tous les exemplaires de la colonne** (boutons n°1, n°2…), avec « Commun avec … ». On peut modifier depuis 08.02.I01 un CR rempli pour 07.01.I03. | 3 | Heuristique 5 « prévenir l'erreur » (REF-14) |
| C4 | **« + Créer » rend le CR existant** quand la colonne en a déjà un (`exemplaireSuivant` absent) : depuis un second incident, on « crée » et on tombe sur le CR d'un autre. | 3 | Heuristique 2 « correspondance avec le monde réel » : un bouton fait ce qu'il dit |
| C5 | **Valeurs de départ prises sur la colonne** : GDH à l'heure du premier incident du jour, et pour le CIMICREP la case « incidents » remplie avec **tous** les codes couverts. Avec une origine, ce sont celles de l'incident d'origine qui ont du sens. | 2 | Règle 19 : pré-remplir ce que l'app sait vraiment |
| C6 | **L'en-tête de la fiche du CR** dit « commun à X, Y · modifié en direct par tous » : ce ne sera plus vrai. | 2 | Heuristique 1 |
| C7 | **Les CR convertis le 2026-10-01** (`convertirAnciensComptesRendus`) avaient un incident : la conversion l'a **effacé** (`incident: ""`). Les CR créés depuis n'en ont jamais eu. | 2 | Ne rien perdre en silence (principe MELMIL) |
| C8 | **Suppression d'un incident** : la confirmation ne compte que les anciens CR (`c.incident === i.id`), et un CR partagé survit (`sansOrphelins`). Avec une origine, il faut décider ce qu'il devient. | 2 | Heuristique 5 |

## Recommandations

### 1. Le modèle

**R1 — Un champ d'origine, distinct de `incident`.** Ajouter à `CompteRendu` un champ **`depuisIncident: string`** (id de l'incident d'origine, `""` si inconnu). Ne pas réutiliser `incident` : ce champ désigne aujourd'hui les « anciens CR » propres à un incident, hors colonne (`crsPartages` les exclut par `!c.incident`) ; le détourner casserait la numérotation et le lot .docx.
- `creerCompteRenduPartage` reçoit `depuisIncident` de l'appelant (création, « +1 », import) ; `relireAtelier` le relit (`texte(c.depuisIncident)`).
- `crsPartages` **ne change pas** : la colonne reste jour + ETIM + type, ordre de création → n°1, n°2…
- Deux fonctions pures, testées, et **un seul calcul partout** (n°24 R5) :
  - `crsDeLIncident(a, i)` = CR dont `depuisIncident === i.id` **+** anciens CR (`incident === i.id`) ;
  - `autresDeLaColonne(a, i, etim, type)` = exemplaires de la colonne créés depuis **un autre** incident (ou sans origine).

**R2 — Les CR existants sans origine : retrouver ce qui peut l'être, puis demander, jamais deviner en silence.** Dans cet ordre, à la relecture (pur et idempotent, comme la conversion du 2026-10-01) :
1. **Colonne couverte par un seul incident** (ce jour-là, un seul incident a cette ETIM) → origine = cet incident. Aucune ambiguïté, c'est la règle déjà acceptée pour la conversion.
2. **Sinon, le journal** (proposition à vérifier par ARCHITECTE) : les anciennes créations écrivaient « crée un PSYREP sur l'incident 08.02.I01 ». Si une entrée du journal a le **même auteur, le même type et le même instant** que `trace` du CR, et un seul candidat → origine retrouvée. Le journal est borné (`JOURNAL_MAX`) : ce ne sera pas toujours possible.
3. **Sinon, le CR reste « à attribuer »** (`depuisIncident: ""`) — voir R6 pour l'affichage et R11 pour la Synthèse.

Réponse aux options posées :
- *Les montrer partout comme avant* : non, c'est le défaut à corriger (C2).
- *Sur aucun* : non, on perdrait un CR de vue (il ne serait plus visible que dans le .docx).
- *Sur le premier incident du jour / de l'ETIM* : non, c'est deviner ; si le choix est faux, le CR s'affiche sur le mauvais incident, sans que personne ne le sache.
- ✅ **Les proposer à l'attribution**, sur chaque incident qui pourrait en être l'origine, avec un geste d'un clic (R6). C'est sans risque et vite fait : en pratique quelques CR par exercice.

### 2. La fiche d'un incident

Maquette textuelle d'une case (incident 07.01.I03, ligne « ETIM 7 », colonne PSYREP, D+27) :

```
PSYREP
[ n°2 ]  [ +1 ]  [ Importer… ]  [ .docx (2) ]
Aussi ce jour pour l'ETIM 7 : n°1, créé depuis 08.02.I01 ›
```

Même case sur un incident qui n'a pas encore de PSYREP pour l'ETIM 7 :

```
PSYREP
[ + Créer ]  [ Importer… ]  [ .docx (1) ]
Déjà ce jour pour l'ETIM 7 : n°1, créé depuis 08.02.I01 ›
```

**R3 — La case ne montre en boutons que les exemplaires de CET incident.** Un bouton par exemplaire créé depuis l'incident, qui l'**ouvre** (visible et modifiable), plein comme aujourd'hui (`frappe-pleine`). Les exemplaires des autres incidents n'ont **pas de bouton** dans cette fiche : ni ouverture, ni modification.
- **Libellé du bouton = le numéro de la colonne**, même s'il est seul pour cet incident : « n°2 » et non « Ouvrir », dès que la colonne compte plus d'un exemplaire. C'est le numéro qu'on retrouvera dans le .docx et dans le titre du CR ouvert (« PSYREP n°2 · ETIM 7 · D+27 », déjà fourni par `nomCompteRendu`). Colonne d'un seul exemplaire : « Ouvrir », comme aujourd'hui.
- Le numéro **peut changer** si un exemplaire plus ancien est supprimé (n°2 devient n°1). C'est déjà le cas aujourd'hui ; ne pas figer de numéro en base.
- *Source* : heuristique 5 « prévenir l'erreur » et 6 « reconnaître plutôt que se rappeler » (REF-14) ; règle 5 « mettre en valeur en atténuant le reste » (REF-07).

**R4 — Une ligne d'indication sous les boutons, quand la colonne a des exemplaires d'ailleurs.** À la place de « Commun avec … » / « Sera commun avec … » / « Seul incident de ce jour avec cette ETIM ».
- **Libellé** (texte doux, `text-xs`, comme aujourd'hui) :
  - cet incident en a déjà un : « **Aussi ce jour pour l'ETIM 7 :** n°1, créé depuis 08.02.I01 › »
  - cet incident n'en a pas : « **Déjà ce jour pour l'ETIM 7 :** n°1, créé depuis 08.02.I01 › »
  - plusieurs : « Aussi ce jour pour l'ETIM 7 : n°1 depuis 08.02.I01 ›, n°3 depuis 08.03.I01 › »
  - au-delà de 3 : les 2 premiers puis « et 2 autres » (le détail complet en infobulle et pour le lecteur d'écran).
  - **aucun autre exemplaire** : **pas de ligne du tout**. Le silence est la bonne réponse ; « Seul incident… » ne sert plus à rien, puisque le CR n'est plus commun.
- **Le code est un lien** (`<a>` ou bouton-lien souligné, pas un bouton plein) qui **ouvre la fiche de l'incident concerné** : sur la planche de préparation, le panneau de droite passe à cet incident (`FicheIncident` reçoit un `onOuvrirIncident(id)`) ; dans l'onglet Incidents, même chose. À l'arrivée, la fiche **défile jusqu'à sa section « Comptes rendus du jour »** et le focus va sur le bouton n°1 concerné. On arrive là où l'on peut agir, en un clic.
- Libellé accessible : « Ouvrir la fiche de l'incident 08.02.I01, qui a créé le PSYREP n°1 de l'ETIM 7 ».
- Pas d'icône, pas de couleur d'alerte, pas de pastille : c'est une **information**, pas un problème.
- *Pourquoi le mot « créé depuis »* : il dit d'où vient le CR sans laisser croire qu'il est « à » l'autre incident au sens exclusif (il est toujours téléchargé avec la colonne). *Source* : heuristique 1 (REF-14) ; règle 7, la forme parle avant l'étiquette (REF-07).

**R5 — « + Créer », « +1 » et « Importer… » créent toujours un exemplaire DE CET INCIDENT.**
- **« + Créer »** (cet incident n'en a pas encore) : crée un exemplaire **vide** dans la colonne, avec `depuisIncident` = cet incident. S'il en existe déjà d'autres (R4), il devient n°2 (n°3…) — **plus jamais** « rendre celui qui existe » (C4). L'idempotence en cas de geste rejoué reste assurée par l'**id choisi par l'appelant** (déjà en place).
- **« +1 »** (cet incident en a déjà un) : inchangé dans son rôle, un autre exemplaire vide **de cet incident**. Infobulle : « Ajouter un autre PSYREP vide pour l'ETIM 7, depuis 07.01.I03 ».
- **« Importer… »** : même chose depuis un .docx rempli (toujours un exemplaire de plus, n°32 R4/R5).
- **Pas de confirmation** « un PSYREP existe déjà ce jour, en créer un autre ? » : la ligne R4 l'a déjà dit, juste sous le bouton, avant le clic. Une confirmation en plus serait un double geste pour un cas normal (plusieurs incidents, plusieurs CR). *Source* : heuristique 5 sans tomber dans la confirmation systématique (REF-14).
- **Valeurs de départ = celles de l'incident d'origine** (C5) : GDH du jour à l'heure **de cet incident** ; pour le CIMICREP, la case « incidents » = **son code** seul. ⚠ Point de contenu (doctrine des CR) à confirmer par l'utilisateur ; tout reste modifiable.

**R6 — Les CR « à attribuer » (sans origine) : un bloc à part, un geste.** Sous le tableau, comme les « Anciens comptes rendus » (n°21 R7), et seulement s'il y en a dans les colonnes de cet incident :

```
À attribuer — créés avant le rattachement à un incident
PSYREP n°1 · ETIM 7 · D+27   [ Voir ]  [ C'est celui de cet incident ]
```

- « **Voir** » ouvre le CR (visible et modifiable : il n'a pas de propriétaire, on doit pouvoir le lire pour savoir à qui il est).
- « **C'est celui de cet incident** » pose `depuisIncident` = cet incident, sans confirmation (réversible par R12). Le bloc disparaît alors des autres fiches.
- Phrase d'aide : « On ne sait pas depuis quel incident ils ont été remplis. Ouvrez-les, puis rattachez-les à leur incident : ils apparaîtront sur sa carte. »
- Ils sont **comptés dans le lot .docx** (ils font partie de la colonne) et **numérotés** comme les autres.

**R7 — Le bouton « .docx » : le lot de la colonne, dit par le mot.** On garde ce que l'utilisateur veut garder : tous les exemplaires de la colonne, un par page, dans un seul fichier.
- Visible **dès que la colonne a au moins un exemplaire**, y compris quand cet incident n'en a aucun (on peut vouloir le compte rendu du jour pour l'ETIM depuis n'importe quel incident concerné).
- Libellé inchangé (« .docx », « .docx (2) ») ; **infobulle et `aria-label` qui disent la portée et l'origine** : « Télécharger les 2 PSYREP de l'ETIM 7 à D+27 dans un seul fichier, un par page — n°1 depuis 08.02.I01, n°2 depuis 07.01.I03 ».
- Le **dialogue de nommage** reprend la même phrase en titre (« Télécharger les 2 PSYREP de l'ETIM 7 à D+27 »), pour qu'on sache, avant de valider, que le fichier contient aussi le CR d'un autre incident.
- ⚠ Question : le nom de fichier prend le code de l'incident d'où l'on télécharge (NMR = `i.code`). Pour un lot qui couvre plusieurs incidents, le code de la fiche ouverte reste le plus simple et le plus prévisible ; à confirmer par l'utilisateur.
- Le téléchargement d'un exemplaire seul reste dans sa fiche (n°32 R1).
- *Source* : la portée se dit par le mot, pas par la couleur (doctrine n°32) ; un geste agit sur l'objet affiché.

**R8 — La fiche du CR ouvert dit d'où il vient et avec quoi il part.** L'en-tête (C6) devient :
- « **PSYREP n°2 · ETIM 7 · D+27** » (titre inchangé)
- sous-titre : « Créé depuis 07.01.I03 · se télécharge avec 1 autre PSYREP du même jour et de la même ETIM · modifiable en direct à plusieurs »
- un CR à attribuer : « Incident d'origine inconnu · à rattacher depuis la fiche de son incident ».
- Pas de navigation vers les autres exemplaires depuis ici (on reste sur CE CR, comme demandé).

**R9 — Le texte d'aide de la section est réécrit.** Aujourd'hui : « Par ETIM et par jour, **communs à tous les incidents** de ce jour… ». Proposé :
> « Les comptes rendus créés depuis cet incident, par ETIM. Ceux d'autres incidents du même jour et de la même ETIM sont signalés dessous. **.docx** les télécharge tous ensemble, un par page. »

### 3. Planche de préparation, liste des incidents, Synthèse

**R10 — Agrafe et compte = fichiers de l'incident + CR créés depuis lui (+ anciens CR).** `piecesDeLIncident` ne compte plus la colonne, mais `crsDeLIncident` (R1). Même calcul pour l'agrafe des cartes (`carte.tsx`), la vue liste par jour (`planche-liste.tsx`), la colonne « Pièces jointes » de l'onglet Incidents et son **tri** (`tri-incidents.ts`), l'infobulle (« 1 fichier et 1 compte rendu »). Une seule fonction, toujours (n°24 R5).
- **Rien sur la planche pour « un CR de cette ETIM existe ailleurs »** : ni signe discret, ni agrafe grisée, ni point. Raisons : (1) l'utilisateur le demande explicitement ; (2) la carte fait ≈ 103 px de large et porte déjà code, heure, statut, ETIM, agrafe (n°33 R7) ; (3) un signe qui apparaîtrait sur presque tous les incidents d'un jour chargé redeviendrait le bruit qu'on retire (C2) ; (4) l'information n'est utile qu'au moment de créer un CR, c'est-à-dire **dans la fiche**, où R4 la donne.
- Les CR « à attribuer » ne mettent pas d'agrafe non plus (ils ne sont à personne) : ils sont signalés dans la fiche (R6) et dans la Synthèse (R11).

**R11 — Synthèse : « sans pièce jointe » compte avec la même fonction, et les CR à attribuer ont leur ligne.**
- « Sans pièce jointe » = `piecesDeLIncident(a, i).total === 0` **avec le nouveau calcul** (rien à changer dans `synthese.ts` si R10 est fait dans `pieces-jointes.ts`). Conséquence visible : des incidents qui avaient une agrafe « par la colonne » vont apparaître « sans pièce jointe ». C'est le comportement voulu ; **le dire dans les notes de version** pour que personne ne croie à une perte.
- Dans « À traiter », une ligne de plus, seulement si non nulle (n°34 R4) : « **3 comptes rendus à rattacher à leur incident** — Voir les 3 › », qui ouvre l'onglet Incidents filtré (`manque=cr-a-attribuer`) sur les incidents dont une colonne contient un CR à attribuer.

### 4. Changer l'incident d'origine d'un CR

**R12 — Utile, mais rare : un geste dans la fiche du CR, pas sur la planche.** Cas réels : CR rempli depuis la mauvaise fiche ; incident supprimé ou fusionné ; incident déplacé de jour ou d'ETIM.
- Dans l'en-tête de la fiche du CR (R8), à côté de « Créé depuis 07.01.I03 », un bouton discret « **Changer…** ».
- Il ouvre une petite liste (boutons radio) des **seuls incidents de la colonne** : ceux du même jour qui ont la même ETIM (`incidentsDuCr`) ; pas d'option « aucun » (on ne retire pas une origine connue pour en faire un CR « à attribuer »). Libellés « 08.02.I01 — sujet ». Bouton principal parlant : « **Rattacher à 08.02.I01** », grisé tant que rien ne change.
- Pas de glisser-déposer de CR entre cartes (WCAG 2.5.7, et rien à saisir sur la carte).
- **Ne change ni le jour, ni l'ETIM, ni le numéro** : le CR reste dans sa colonne. Changer de jour ou d'ETIM serait un autre CR (autre lot .docx).
- Journal : « rattache le PSYREP n°1 de l'ETIM 7 à D+27 à 08.02.I01 (était 07.01.I03) ».
- *Source* : doctrine n°37 (un choix se valide dans une fenêtre qui dit ce qui va changer) ; heuristique 3 « contrôle et liberté » (REF-14).

**R13 — Quand l'incident d'origine ne correspond plus à la colonne (jour ou ETIM changés).** Le CR garde sa colonne et son origine. Sur la fiche de l'incident d'origine, il passe dans un bloc « **À reclasser** » sous le tableau (même forme que R6) : « PSYREP n°1 · ETIM 7 · D+27 — l'incident n'est plus à D+27 » (ou « n'a plus l'ETIM 7 »), avec « Voir », « Rattacher à un autre incident… » (R12) et « Supprimer ». Il **reste compté dans l'agrafe** : c'est toujours sa pièce jointe, et on ne la perd pas de vue. Pas de déplacement automatique vers le nouveau jour : le contenu (GDH, faits) appartient au jour d'origine.

**R14 — Suppression d'un incident qui a des CR d'origine.** La confirmation les nomme : « Supprimer l'incident 07.01.I03 et ses 2 comptes rendus (PSYREP n°2 de l'ETIM 7, CIMICREP n°1 de l'ETIM 7) ? » — comme ses fichiers, qui partent avec lui. ⚠ Alternative à arbitrer par l'utilisateur : les garder « à attribuer » (règle n°21 « un CR survit à son incident »). Proposition par défaut : **ils partent avec l'incident**, puisqu'ils sont désormais ses pièces jointes ; la confirmation, qui les énumère, suffit à éviter la perte par surprise.

### 5. À éviter

- ⛔ **Réutiliser `incident`** pour l'origine : casse `crsPartages`, la numérotation et le lot .docx.
- ⛔ **Deviner l'origine** d'un ancien CR (premier incident du jour, premier code) quand plusieurs incidents sont possibles.
- ⛔ **Montrer les exemplaires des autres incidents en boutons grisés** ou en lecture seule dans la case : l'œil les prend pour les siens ; la demande est « uniquement CE CR visible ».
- ⛔ **Un signe sur la planche** pour « CR de l'ETIM existant ailleurs » (agrafe grisée, point, contour).
- ⛔ **Renuméroter par incident** (« n°1 » de 07.01.I03 alors qu'il est n°2 dans le .docx) : deux numérotations pour le même objet.
- ⛔ **Une confirmation à chaque « + Créer »** quand la colonne a déjà un exemplaire.
- ⛔ **Changer le contenu du lot .docx** (le restreindre à l'incident) : explicitement à garder tel quel.
- ⛔ **Couleur d'alerte** pour « à attribuer » ou « à reclasser » : ce sont des tâches, pas des erreurs (une seule couleur d'alerte, rare).
- ⛔ **Déplacer automatiquement** un CR quand son incident change de jour ou d'ETIM.

## Questions à l'utilisateur (réponses par défaut proposées)

1. **Valeurs de départ** d'un CIMICREP créé depuis un incident : case « incidents » = son seul code ? *Défaut : oui.*
2. **Suppression d'un incident** : ses CR partent avec lui (comme ses fichiers) ou restent « à attribuer » ? *Défaut : ils partent, la confirmation les nomme.*
3. **Nom du fichier du lot** .docx : code de l'incident d'où l'on télécharge ? *Défaut : oui (inchangé).*
4. **Récupération par le journal** (R2, étape 2) : à faire si ARCHITECTE la juge fiable, sinon seulement « un seul incident couvert » puis « à attribuer ». *Défaut : les deux premières étapes si fiables.*

## Vérifications attendues (en local)

- 07.01.I03 et 08.02.I01 à D+27, ETIM 7 toutes les deux : PSYREP créé depuis 07.01.I03 → agrafe **sur 07.01.I03 seulement** (planche, liste par jour, colonne « Pièces jointes », tri) ; 08.02.I01 n'a ni agrafe ni bouton, seulement « Déjà ce jour pour l'ETIM 7 : n°1, créé depuis 07.01.I03 › ».
- Le lien ouvre la fiche de 07.01.I03 sur la planche (panneau de droite), section CR, focus sur n°1.
- « + Créer » depuis 08.02.I01 → n°2, ouvert, avec « Créé depuis 08.02.I01 » ; les deux fiches se signalent mutuellement.
- « .docx (2) » depuis l'une ou l'autre fiche → un fichier, n°1 puis n°2.
- Synthèse « sans pièce jointe » cohérente avec l'agrafe ; ligne « à rattacher » sur des données anciennes.
- Deux navigateurs : la saisie en direct dans un même CR continue de fonctionner (n°21 R5).
- Thème sombre, téléphone (la ligne R4 passe à la ligne sans couper les codes), lecteur d'écran (libellés des liens et du .docx).

## Doctrine (DESIGNER)

- **Un repère qui est partout ne signale plus rien** (Von Restorff, REF-06) : l'agrafe doit distinguer les incidents qui ont vraiment une pièce.
- **Prévenir l'erreur** et **reconnaître plutôt que se rappeler** (Nielsen 5 et 6, REF-14) : on ne modifie que ce qui est à soi ; l'existence des autres est dite, avec un lien, au moment où elle compte.
- **Une même notion, un même numéro, un même calcul** (n°24 R5, n°32) : le numéro de la colonne partout, `piecesDeLIncident` pour tous les comptes.
- **La complexité est portée par le système** (Tesler, règle 19) : l'origine est enregistrée au geste de création, l'utilisateur n'a rien à déclarer.
- **Ne jamais deviner en silence** : ce qu'on ne sait pas se montre « à attribuer » et se règle en un clic.

⭐ **Doctrine ajoutée** : *ce qui sert à ranger (la colonne, le lot) n'est pas ce qui sert à montrer (l'origine). Un objet partagé pour l'export s'affiche chez celui qui l'a créé ; les autres en sont informés, pas encombrés.*
