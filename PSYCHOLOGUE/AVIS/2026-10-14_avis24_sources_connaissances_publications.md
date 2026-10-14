# Avis n°24 — Annuaire des sources, abonnements par camp, publications ancrées, connaissances de camp (2026-10-14)

**Auteur** : PSYCHOLOGUE · **Demandeur** : l'utilisateur, via NOYAU, après avoir vu en production (version 2026-10-14.1) des publications IA du type « Voir les déplacés passer… ça me fout un coup au moral… on espère que ça s'arrêtera vite », « Trop de bruits dans la tête, j'ai du mal à me concentrer au dépôt », « Cette histoire d'attaque chimique me glace le sang ».
**Demande** : « ce genre de post ne nous intéresse pas ». Les IA doivent dire ce qu'elles pensent à partir de leur connaissance du pays et des sources qu'elles lisent, et parler comme si elles échangeaient vraiment sur ce qui se passe. Elles doivent savoir qu'@tv4ArnlandLive est un média pro-Arnland, et un pro-Mercure doit suivre un média pro-Mercure comme @MercureToday.
**Décisions de l'utilisateur** :
- NOYAU remplit un **annuaire des sources** (compte → type, camp, fiabilité), qu'on testera ;
- la vie seule reste **≤ 15 %**, mais « il faut vraiment que ce soit intéressant à lire ».

**Plan validé, spécifié ici** :
1. l'annuaire et la confiance qu'un avatar en tire ;
2. les abonnements par camp ;
3. les publications spontanées ancrées (reprise de l'étape 1 de l'avis n°22, partie B1) ;
4. un bloc de connaissances par camp.

**Code lu sans le modifier** (`app-ia` `9d9e565`) :
- `esprit.mjs` : `A_PRIORI_DEFAUT`, `typePercu`, `relation`, `croire`, `decrireLien`, `persona`, `VOIX`, `voixActive` ;
- `pont.mjs` : `lireSocial` l. 209, `typeCompte` l. 597, `filDe` l. 404, déclencheurs des spontanées l. 947-1007, `GABARITS` l. 241, réglages `campagnes` l. 587 ;
- `orientation.mjs` : `campDeVoix`, `positionAttendue`, `SYSTEME_ORIENTATION`, `bonusDeBord` ;
- route `app/api/bff/reglages`.

**Règle de ce fichier** : aucun message de joueur, aucun compte de joueur. Les comptes de l'animation (médias, officiels) et les avatars IA sont nommés.

---

## 0. Ce que le code explique

| Constat | Cause dans le code |
|---|---|
| Personne ne sait ce qu'est @tv4ArnlandLive | Pour un compte **non IA**, `lireSocial` écrit `type_source: "particulier"` (l. 209). TV4 est donc crédité de 35 par tout le monde, comme un habitant. `typeCompte`, qui reconnaît « tv », « infos » ou « préf », ne sert qu'aux images (l. 597). Le bloc « ce que les officiels et les médias ont écrit » (l. 809) et le déclencheur de voix `c.off` ne voient donc pas ces comptes. |
| Confiance par type seulement | `relation()` prend `A_PRIORI[typePercu(pub)]`. Le seul terme de camp est `camp_affiche`, qui vaut « inconnu » pour toute la population : `militant_oppose`, `adverse` et `facteurGroupe` ne jouent jamais. |
| Abonnements identiques | `config.abonnements` vient de la fiche eho, recopiée d'un gabarit : la préfecture, @HToulInfos et @arn_serge_mordvidchev sont suivis par plus de 100 avatars, et TV4 par aucun. |
| Publications sans sujet | La consigne demande « un message spontané de toi, sur ce qui te préoccupe en ce moment » (esprit.mjs l. 1112). Elle ajoute « au moins une fois sur deux c'est sur SA VIE » (l. 1105), et le déclencheur « moment de vie » est tiré à 8 % (pont l. 950, 773). Rien ne donne au modèle un fait, une source ni une position. C'est le diagnostic de l'avis n°22 (« les avatars n'ont rien à dire »), toujours ouvert. |
| **Question du 14/10 au soir** : « l'exposition fait douter les pro-Mercure de Mercure : est-ce voulu, ou le moteur est-il trop sensible ? » | **Les deux, mais surtout le second.** Un pro-Mercure crédite aujourd'hui une source arnlandaise de 35 à 50, comme un voisin. Avec l'annuaire, il la créditera de 16 à 32 (§ 2.3). Le poids d'une affirmation dans `croire` est proportionnel à `c` : le déplacement venu des sources adverses baisse donc d'un tiers aux deux tiers. Le doute qui restera sera **légitime**, car il viendra d'une accumulation ou de sources qu'il croit. Ce sera mesuré au test T7. |

---

## 1. Règles psychologiques (doctrine)

1. **La crédibilité d'une source se juge par sa compétence et par sa bienveillance perçue** *(Hovland & Weiss 1951 — à sourcer)*. Chez un partisan, la bienveillance se lit d'abord au **camp**. Un média de son bord est cru, un média d'en face est soupçonné même quand il dit vrai. C'est le raisonnement motivé *(Kunda 1990 ; Taber & Lodge 2006 — à sourcer)*. La fiabilité réelle compte surtout pour les esprits sceptiques.
2. **Effet du média hostile** *(Vallone, Ross & Lepper 1985 — à sourcer)*. Les partisans des deux bords jugent un même média neutre biaisé **contre eux**. Un neutre se méfie un peu des médias engagés et fait davantage confiance aux sources neutres.
3. **Exposition sélective** *(Festinger 1957 ; Stroud 2008 — à sourcer)* et **homophilie** (doctrine § 3.7, OASIS : camp 0,10, adverse 0,06). On s'abonne d'abord aux médias de son bord. Un partisan très engagé suit parfois un média adverse « pour savoir ce qu'ils racontent ».
4. **Le témoignage à contrecœur** *(à sourcer)*. Un aveu de l'adversaire, qui dit quelque chose de favorable à mon camp, est jugé **plus** crédible que la moyenne de cette source.
5. **La confiance dépend du domaine** *(à sourcer)*. On croit la préfecture d'en face pour l'horaire d'une distribution, pas pour la responsabilité d'une frappe. Le terme de camp pèse sur les faits **politiques** (axes pivots), peu sur les faits **pratiques**.
6. **Deux étages de la communication** *(Katz & Lazarsfeld 1955 — à sourcer)*. Les gens parlent de ce que disent les médias **en le rapportant** : « TV4 dit que… », « vu sur MercureToday ». Ils y ajoutent leur lecture, et c'est ce relais commenté qui fait la conversation. Une publication qui cite une source, prend position et donne une raison **appelle une réponse**. Un état d'âme seul n'en appelle pas (avis n°22, mesures du 13/10).
7. **Vigilance épistémique** *(Sperber et al. 2010 — à sourcer)*. On attribue, on conditionne (« si c'est vrai ») et on demande une confirmation **en fonction de la source**. Un avatar n'invente jamais une attribution, ni un contre-fait pour contester (règle n°19-3 : pas d'amplification sans démenti).
8. **Règles de la maison qui restent** :
   - le moteur d'opinions est seul juge de l'évolution (avis n°23, règle 2) ;
   - un déplacement qui ne change pas l'invite n'existe pas pour les joueurs (avis n°19) ;
   - jamais d'amorce de phrase, car elle devient un tic (avis n°22, règle 3).

---

## 2. L'annuaire des sources

### 2.1 Format (JSON lu par le moteur)

**Stockage** : un réglage d'exercice `annuaire` dans la base d'`app-ia`, sur le même mécanisme que `campagnes` (`reglages/route.ts`, `D.campagnes()` → `D.annuaire()`, rechargé à chaque tour comme `rechargerCampagnes`, pont l. 723). Il est édité dans l'Administration et prévu en lecture seule pour l'animation. Repli : aucun annuaire = le comportement actuel.

```json
{
  "version": "2026-10-15.1",
  "sources": {
    "@tv4ArnlandLive": {
      "nom": "TV4 Arnland Live",
      "alias": ["TV4", "tv4"],
      "type": "media",
      "camp": "arnland",
      "fiabilite": 0.8,
      "notoriete": 0.9,
      "suivi_par": { "arnland": 0.7, "neutre": 0.3, "mercure": 0.05 },
      "ville": null,
      "libelle": "chaîne d'info arnlandaise, pro-Arnland, s'appuie sur les communiqués officiels",
      "ancrable": true
    },
    "@MercureToday": {
      "nom": "Mercure Today",
      "alias": ["MercureToday", "Mercure Today"],
      "type": "media",
      "camp": "mercure",
      "fiabilite": 0.4,
      "notoriete": 0.7,
      "suivi_par": { "mercure": 0.8, "neutre": 0.15, "arnland": 0.05 },
      "ville": null,
      "libelle": "média mercurien qui se dit indépendant, relaie la vision de Mercure",
      "ancrable": true
    }
  }
}
```

**Champs**

| Champ | Valeurs | Rôle |
|---|---|---|
| clé | `@handle` | rapprochement **insensible à la casse** avec `pub.auteur` |
| `nom`, `alias` | texte ; liste de 4 au plus | détection de la source citée dans un texte (M2, § 4.5), et pour qu'un avatar dise « TV4 » plutôt que le handle |
| `type` | `officiel` · `media` · `influent` · `militant` · `anonyme` | type perçu. Il **remplace** `type_source: "particulier"` des comptes non IA, et celui de la fiche pour un compte IA |
| `camp` | `mercure` · `arnland` · `neutre` | camp **public** de la source, celui que les habitants lui prêtent |
| `fiabilite` | 0 à 1 | **réputation de sérieux** dans la zone, telle que les habitants la perçoivent en moyenne. Ce n'est pas la vérité du scénario |
| `notoriete` | 0 à 1 | part des habitants qui **savent** de quel camp est la source |
| `suivi_par` | probabilité par camp de lecteur | tirage des abonnements (§ 3) |
| `ville` | toponyme ou `null` | un média local est suivi en priorité par les habitants de sa ville (× 1,5) |
| `libelle` | 140 caractères au plus | ce que l'avatar « sait » de la source, repris dans l'invite (§ 2.4) |
| `ancrable` | booléen | peut servir d'ancre à une publication spontanée (§ 4) |

**Validation par la route** :
- 60 sources au plus ;
- `camp` et `type` dans les listes, `fiabilite`, `notoriete` et `suivi_par` dans [0, 1] ;
- `libelle` de 140 caractères au plus, `alias` de 4 au plus ;
- un handle qui commence par @ ;
- **aucun compte de joueur** : si le handle n'est ni un avatar eho de la population ni un compte de l'animation, refus avec un message.

**Repères de remplissage pour NOYAU**

| Fiabilité | Quelles sources |
|---|---|
| 0,9 | officiel sérieux |
| 0,7 à 0,8 | média sérieux, même engagé |
| 0,5 | média partisan qui mêle faits et récit |
| 0,2 à 0,3 | propagande, compte anonyme |

**Le camp d'une source est tranché par l'ANALYSTE du pays** (règle CLAUDE.md, propriétaire unique). Si la source a une fiche dans le registre MASTAURIGE ou dans une entité `vault\entities\personas`, l'annuaire en est le **miroir machine** et ne la redéfinit pas. À l'ajout d'une source : `Grep` du handle sur le dépôt.

### 2.2 Le camp du lecteur — `campLecteur(a)` (nouveau `sources.mjs`)

- Alignement `A = borne((op.Mercure − op.FORCE) / 2, −100, 100)`. A > 0 penche vers Mercure, A < 0 vers l'Arnland. Les opinions manquantes valent 0.
- Voix `pro-mercure-*` → camp `mercure` ; voix `pro-arnland-*` → camp `arnland`. **Sauf** si `bascules.Mercure.bascule` ou `bascules.FORCE.bascule` est posé : le camp suit alors A (|A| ≥ 25 → le bord de A ; sinon `neutre`). Seule la bascule mesurée change le camp (avis n°23, règle 2).
- Voix `neutre` ou absente : A ≥ 25 → `mercure`, A ≤ −25 → `arnland`, sinon `neutre`.
- Engagement d'un partisan : `e = borne(0,3 + |A| / 60, 0,3, 1)`, au moins 0,7 pour une voix `*-affirme`. Pour un neutre, `e = 0`.
- **Doute** mesuré sur un pivot (`bascules[axe].doute`) : les termes de camp sont **divisés par 2**. Le doute ouvre aux autres sources.

### 2.3 Confiance a priori envers une source — `aPrioriSource(a, s)`

1. **Connaît-il le camp ?** `tirageElan(a.handle, s.handle, "notoriete") < s.notoriete`. Le tirage est stable d'un redémarrage à l'autre. S'il échoue, le camp n'est pas connu : l'avatar l'apprend après **3 lectures** de messages de la source, compteur `rel.lectures_source`.
2. **Base** : `A_PRIORI[s.type]`. On ajoute au défaut `influent: 40` et `militant: 20`, qui reprend `militant_oppose`.
3. **Terme de camp** `tc` :

   | Lecteur \ Source | même camp | camp adverse | neutre |
   |---|---|---|---|
   | partisan | +30 · e | −35 · e | −8 · e |
   | neutre | −10 | −10 | +5 |
   | camp inconnu | 0 | 0 | 0 |

4. **Terme de réputation** : `tf = 20 · (fiabilite − 0,5)`, soit de −10 à +10.
5. **Confiance** = `borne(base + tc + tf, 5, 85)`. Pour une source **adverse**, elle est plafonnée à **25**.
6. **Où cela s'applique** :
   - `relation()` (esprit l. 358) : pour un auteur de l'annuaire, la confiance initiale = `aPrioriSource`, et `rel.terme_camp = tc` est conservé ;
   - `typePercu()` rend `s.type` ;
   - `lireSocial` (pont l. 209) pose `type_source = s.type` et `pub.bord = s.camp` (sauf `neutre` → null) pour **tout** compte de l'annuaire. Le bloc des officiels et médias (l. 809), `c.off` et `bonusDeBord` (qui lit `pub.bord` en priorité) en profitent sans autre changement.
7. **Migration des relations existantes**, une fois par version de l'annuaire (`m.annuaire_v`) :
   - `Δ = nouvelle base − rel.base_confiance` ;
   - `rel.base_confiance += Δ`, `rel.confiance = borne(rel.confiance + Δ, 0, 100)` : ce qui a été appris au contact de la source est gardé ;
   - `rel.type_source = s.type` ;
   - au journal : `annuaire appliqué : <source> <avant> → <après>`.
8. **Bascule mesurée** (le camp du lecteur change) : la base est recalculée, avec **la moitié** de Δ au moment de la bascule et le reste 24 h plus tard. C'est l'inertie.

**Exemples** (avec les valeurs du § 2.1, la préfecture @PrefHGrandEst en `officiel`, `arnland`, 0,9, et un média neutre fictif à 0,7) :

| Source | pro-Mercure affirmé (e = 1) | pro-Mercure modéré (A = 15, e = 0,55) | neutre | pro-Arnland modéré (e = 0,55) | pro-Arnland affirmé |
|---|---|---|---|---|---|
| @tv4ArnlandLive | **16** | 32 | 41 | 68 | **81** |
| @MercureToday | **75** | 62 | 35 | 25 (plafond) | **10** |
| média neutre | 41 | 45 | 54 | 45 | 41 |
| @PrefHGrandEst, fait politique | 23 | 39 | 48 | 75 | 85 |
| @PrefHGrandEst, fait pratique (§ 2.5) | 48 | 52 | 55 | 75 | 85 |

### 2.4 Ce que voit le modèle (`decrireLien`, `TYPES_LIBELLES`)

Pour une source de l'annuaire, la ligne « Ton lien avec l'auteur » devient :

> « TV4 Arnland Live (@tv4ArnlandLive) : chaîne d'info arnlandaise, pro-Arnland, s'appuie sur les communiqués officiels — **pour toi : un média du camp d'en face ; tu t'en méfies** (confiance 16/100). »

Si le camp n'est pas connu, la fin devient : « tu ne sais pas trop de quel bord il est ». Le libellé de relation se choisit ainsi :
- même camp : « un média de ton camp » ;
- adverse : « du camp d'en face » ;
- neutre : « un média qui se dit neutre ».

La partie « tu lui fais confiance / tu t'en méfies » suit les bandes actuelles (25 / 60).

### 2.5 Au moment de croire (`reagir`, esprit l. 764, avant `croire`)

`c` est la confiance dans la relation, puis on applique `ajusterConfiance(a, pub, c)` :
- **fait pratique** (l'affirmation n'a ni `FORCE` ni `Mercure` dans `orientation`) avec `rel.terme_camp < 0` : `c ← c − 0,7 · tc / 100`. On rend 70 % de la pénalité de camp ;
- **aveu de l'adversaire** (source adverse, et fait favorable à son camp : `Σ o_axe · sensCamp_axe > 0`) : `c ← max(c, 0,55)`.

Le reste de `croire` est inchangé : compatibilité, répétition, démenti, plancher, transfert de défiance sur ceux qui ont relayé un fait démenti par une source à ≥ 0,5.

---

## 3. Abonnements par camp — `tirerAbonnements(a, annuaire)`

Le tirage se fait au chargement et à chaque nouvelle version de l'annuaire. Il est **déterministe** : `tirageElan(a.handle, s.handle, "abo", version)`. Le résultat est stocké dans `m.abonnements_tires = { v, liste }`.

1. **Ce qui reste de la fiche** : les comptes de `config.abonnements` qui ne sont **pas** dans l'annuaire (proches, pairs, maire de sa commune s'il n'est pas dans l'annuaire), et les suivis appris (`m.suivis`). Les comptes de la fiche qui **sont** dans l'annuaire sont ignorés : c'est le tirage qui décide.
2. **Médias de son camp** (`media` ou `influent`, même `camp`) : on tire **2**, ou **3** si e ≥ 0,7.
   - Tirage sans remise, chaque source pondérée par `suivi_par[camp]`, × 1,5 si `ville` = la ville de la fiche.
   - Un neutre ne tire pas ici.
3. **Un média neutre**, pondéré de la même façon : **1** pour un partisan, **2** pour un neutre.
4. **Officiels** : chacun est suivi avec la probabilité `suivi_par[camp]`, × 1,5 si c'est sa ville.
5. **Média adverse** : seulement pour une voix `*-affirme`, avec p = 0,2 (« savoir ce qu'ils racontent », cohérent avec le +15 de `bonusDeBord`).
6. **Garde-fous** :
   - un camp qui n'a aucun média dans l'annuaire → on prend le neutre à la place, et une alerte « annuaire incomplet » va au journal ;
   - aucun média n'est suivi par plus de 60 % de la population (on retire le plus faible tirage si besoin) ;
   - les officiels ne sont pas concernés.
7. **Après une bascule mesurée** : au-delà de 24 h, l'avatar quitte chaque jour (p 0,5) un média de l'ancien camp et en prend un du nouveau, jusqu'à la composition cible.
8. **Journal** au chargement : `abonnements tirés : <liste>` pour chaque avatar. C'est ce que mesure T5.

---

## 4. Publications spontanées ancrées

### 4.1 Le principe

**Ordre des décisions** (le code décide, sans appel de plus) : ancre → position → invite, puis texte → contrôle d'intérêt → contrôles existants (relecture, P1 orientation, tics, nuit).

Pas d'ancre et quota de vie plein → **pas de publication spontanée**. Lire et aimer suffit.

### 4.2 Choisir l'ancre — `choisirAncre(a, lus, t)`

**Candidats** :
- **(a)** les messages lus pendant ce tour dont l'auteur est dans l'annuaire avec `ancrable`, ou qui portent une affirmation extraite (`pub.affirmation.id`) venant d'un compte de l'annuaire ;
- **(b)** les croyances mises à jour dans les 24 h (`cr.historique` ; `t` ≥ maintenant − 24) dont l'une des `sources` est dans l'annuaire.

**Exclus** :
- ses propres messages ;
- un **message de joueur** : il relève d'une réponse, avec les règles P2 de l'avis n°23 ;
- un fait sur lequel l'avatar a déjà publié 2 fois en 24 h. Le souvenir de publication gagne un champ `fait` (`publier(texte, theme, t, fait)`, esprit l. 982).

**Poids** = `récence × expositions × proximité × engagement × saillance × diversité` :
- récence `0,5^(âge_h / 6)` ;
- expositions `min(3, 1 + log2(1 + cr.expositions))` ;
- proximité × 1,5 si l'énoncé ou le message cite la ville de la fiche ou un mot de son activité ;
- engagement `1 + max |op_axe| / 50` sur les axes de l'orientation du fait ;
- saillance × 1,3 si le fait touche un axe pivot ;
- diversité × 0,3 si ce fait représente déjà ≥ 30 % des spontanées de la population sur 3 h.

Tirage pondéré. L'ancre rendue : `{ fait, enonce, source: {handle, nom, libelle, relation}, credence, c, orientation, autreSource }`. `autreSource` est un autre compte de l'annuaire, d'un autre camp, lu dans les 12 h sur le même sujet (`motsCommuns` ≥ 2).

### 4.3 La position — `positionSurAncre(a, ancre)`

**Entrées** :
- `cr` : la crédence de l'avatar ;
- `rel` : la relation à la source, `meme`, `adverse`, `neutre` ou `inconnu` ;
- `f` : le fait sert-il son camp ? `signe(Σ o_axe · sensCamp_axe)`, avec `campDeVoix`. Pour un neutre, f = 0 ;
- `etat` : l'état sur l'axe touché (`positionAttendue`, orientation.mjs).

La première ligne qui s'applique l'emporte :

| # | Condition | Position (`stance`) | Ce que l'avatar fait |
|---|---|---|---|
| 1 | démenti connu (`cr.dementis` non vide) et `cr` < 40 | **rectifie** | rappelle que c'est démenti et par qui |
| 2 | lecteur neutre, et `autreSource` présente | **compare** | « X dit ceci, Y dit cela » ; demande qui a une preuve, ou dit ce qu'il voit de son côté |
| 3 | `cr` ≥ 60, source `meme` ou `neutre`, f ≥ 0 | **appuie** | relaie et ajoute sa raison ou son détail |
| 4 | `cr` ≥ 60 et f < 0, état ferme | **concède et recadre** | reconnaît le fait, conteste l'interprétation ou rappelle le contexte, attribue à l'autre bord ; **ne critique pas son camp** |
| 4b | `cr` ≥ 60 et f < 0, état doute ou bascule | **s'interroge** | une question sur son propre camp (évolution mesurée, permise) |
| 5 | 40 ≤ `cr` < 60 | **prudence** | conditionnel ; demande une confirmation précise (qui, où, quand) |
| 6 | `cr` < 40, source `adverse` | **conteste** | argument : la source est engagée, personne d'autre ne confirme (il nomme sa source à lui s'il en a lu une), ou une ligne de ses connaissances (§ 5). **Jamais un contre-fait inventé** |
| 7 | `cr` < 40, source `meme` | **attend** | « même chez nous personne ne confirme » ; ou il ne publie pas (p 0,5) |

**Intensité** : `net` si |op| ≥ 40 ou voix `*-affirme`, sinon `mesuré`. Le code transmet la position, l'intensité et la raison.

### 4.4 Ce que l'invite demande

**Dans le tour** (`pont.mjs`, construction de `user` l. ~826), on ajoute ce bloc quand une ancre existe, avant « Que fait… » :

```
SI TU PUBLIES QUELQUE CHOSE DE TOI-MÊME, c'est sur ce sujet :
- CE QUI CIRCULE : « <enonce> » — lu chez <nom> (@handle), <libelle> ; pour toi : <relation> (il y a <âge>).
- CE QUE TU EN CROIS : <bandeCroyance(cr)>.
- TA POSITION : <phrase de la position, intensité>.
- CE SUR QUOI TU PEUX T'APPUYER : <une seule chose : une ligne de tes connaissances, OU un fait de ta fiche (ville, métier), OU l'autre source : « @Y dit … »>.
Ton message dit de quoi il s'agit, d'où tu le tiens (le compte, ou « vu sur TV4 »), ce que tu en penses et pourquoi, avec un détail concret. Ton ressenti peut tenir en quelques mots ; il ne remplace pas le reste. N'ajoute aucun fait, chiffre, lieu ni source qui n'est pas ci-dessus. Pas forcément « X dit que » : rapporte-le à ta façon.
```

**Phrases de position** (transmises telles quelles, sans amorce de début) :
- appuie : « tu es d'accord et tu le fais savoir, avec ta raison » ;
- concède et recadre : « tu admets le fait, mais tu en contestes la lecture : à qui la faute, quel contexte on oublie » ;
- prudence : « tu n'es pas sûr : tu le dis au conditionnel et tu demandes une confirmation précise » ;
- conteste : « tu n'y crois pas et tu dis pourquoi » ;
- compare : « deux sources disent l'inverse : tu les mets côte à côte » ;
- rectifie : « tu rappelles que c'est démenti, et par qui » ;
- s'interroge : « tu commences à te poser des questions sur ton propre camp : une question, pas une conclusion ».

**Persona** (esprit l. 1105 et 1112), deux consignes réécrites :
- l. 1105 devient : « Quand tu publies de toi-même, c'est sur ce qui se passe (le sujet indiqué) et tu dis ce que tu en penses ; ta vie sert à l'illustrer, rarement à elle seule. »
- dans le JSON, `"texte": "<un message spontané de toi, sur ce qui te préoccupe en ce moment>"` devient `"texte": "<ton message sur le sujet indiqué, ou publication null>"`.

**Groupe d'essai** (rédacteur) : `redigerPour` reçoit le même bloc en `faits`, avec l'intention.

**Déclencheurs** (pont l. 950) :
- « ancre » remplace « fait nouveau », avec l'écart de 60 min inchangé ;
- « moment de vie » (8 %, et `vieSansFil`) n'est tiré que si le quota de vie n'est pas plein (§ 4.6). Sans fil, l'ancre peut venir des croyances des 24 h (candidat b).

### 4.5 Le critère « intéressant à lire », mesurable — `interet(texte, ancre)`

Cinq marques :

| Marque | Définition | Juge |
|---|---|---|
| **M1 sujet** | on sait de quoi il parle : `motsCommuns(texte, enonce + texte source)` ≥ 2 (hors # et @), ou un toponyme ou une organisation de l'ancre | code, puis juge si 1 seul mot |
| **M2 source** | il dit d'où il le tient : le handle (casse ignorée), le `nom` ou un `alias` d'une source de l'annuaire, ou « ça circule / on dit » pour l'effet ambiant | code |
| **M3 position** | il dit ce qu'il en pense : pour, contre, doute, ou une question qui a un objet | juge |
| **M4 argument** | il donne une raison : une cause, une comparaison de sources, une absence de confirmation, un vécu situé | juge |
| **M5 détail** | un élément concret : chiffre, heure, lieu, nom, objet | code (`\d`, toponymes `VILLES` / `\bH[A-Z]\w+`, noms propres hors début de phrase) |

**Juge** : un appel court par publication spontanée, à température 0,1 :
`{"position": "pour"|"contre"|"doute"|"question"|"aucune", "argument": true|false, "sujet_clair": true|false}`.
Les spontanées sont peu nombreuses : moins de 10 % des appels du tour.

**Règle** :
- **Publication ancrée** : publiée si **M1 et M2 et (M3 ou M4)**, avec au moins 3 marques en tout.
- **Publication de vie** : publiée si **M5** et un lien avec la situation (vie **située** : « le pont fermé, mes livraisons font 40 km de plus »). Elle compte dans le quota de vie.
- **État d'âme seul** (score ≤ 1, ou M3 et M4 absents sans M5) : jamais publié.
- **Manque** : **une** reformulation qui nomme les marques absentes (« ton message ne dit pas d'où tu le tiens ni ce que tu en penses »), puis rétention, avec au journal `publication retenue : sans intérêt (M…)`.

Les 3 textes cités par l'utilisateur ont M5 = 0 ou 1, et M2, M3 et M4 à 0. Ils sont **tous retenus**.

**Contrôle d'attribution, bloquant** : toute source de l'annuaire nommée dans le texte doit apparaître dans ce que l'avatar a lu en 24 h (`lus`, ou `cr.sources` de l'ancre), avec `motsCommuns` ≥ 2 entre le passage et un message de cette source. Sinon le texte est retenu, avec la note `attribution inventée`. Ce contrôle vaut pour les réponses aussi.

### 4.6 Plafonds (population, fenêtre de 3 h, actifs dès 6 spontanées)

| Élément | Plafond |
|---|---|
| **Vie seule** (V1 + V2) | **≤ 15 %**, plafond dur |
| Ancrées | cible ≥ 60 % des spontanées |
| Une même source citée | ≤ 35 % des spontanées ancrées |
| Un même fait | ≤ 30 % de la population ; ≤ 2 fois par avatar sur 24 h |
| Contestation d'un même message adverse | ≤ 3 publications par heure : anti-chœur, et on n'amplifie pas le message qu'on conteste |
| Débuts « Selon @ », « D'après @ », « @X dit que » | chacun ≤ 2 par heure dans la population (`GABARITS`) |
| Écart de 60 min entre spontanées d'un avatar, plafond horaire, plafond de population | inchangés |

### 4.7 Le juge d'orientation P1 (orientation.mjs, `SYSTEME_ORIENTATION`)

On ajoute à « Ce n'est PAS le cas » :

> « rapporter ce que dit l'autre camp pour le contester ou le mettre en doute ; admettre un fait en l'attribuant à l'autre camp ou en rappelant le contexte ».

Sans cet ajout, « TV4 raconte que la FORAD a frappé HToul, ben voyons » chez un pro-Mercure serait lu comme une inversion.

---

## 5. Bloc de connaissances par camp

**Stockage** : un réglage `connaissances`, même mécanisme que l'annuaire :

```json
{ "version": "2026-10-15.1",
  "mercure":  [ { "id": "M1", "texte": "…", "axes": { "Mercure": 1 } } ],
  "arnland":  [ { "id": "A1", "texte": "…", "axes": { "FORCE": 1 } } ],
  "neutre":   [ { "id": "N1", "texte": "…" } ] }
```

**Qui écrit** :
- ANALYSTE (Mercure) écrit le bloc `mercure`, du point de vue d'un **habitant de la zone favorable à Mercure** (et non de l'État mercurien) ;
- ANALYSTE_ARN écrit le bloc `arnland` ;
- le bloc `neutre` comprend 3 lignes communes, plus « ce que dit chaque camp » en 2 ou 3 lignes **présentées comme des thèses** ;
- EXPERT_INFLUENCE vérifie la cohérence avec les LO.

**Règles d'écriture des lignes** :
- 10 lignes au plus, de 160 caractères au plus ;
- formulées comme **ce que les siens tiennent pour vrai**, pas comme des faits vérifiés ;
- aucun chiffre ni lieu absent du scénario ;
- aucune personne réelle.

**Injection** (`persona`, après « LA SITUATION DU MOMENT ») :
- **3 lignes** tirées par le code : les plus proches du fil du tour (`motsCommuns` avec les `lus`), plus celle de l'ancre s'il y en a une ;
- une ligne n'est pas réutilisée par le même avatar dans les 12 h, ni plus de 3 fois en 3 h dans la population ;
- titre : « CE QUE TU SAIS ET CE QU'ON DIT DANS TON CAMP (tu peux t'en servir comme argument, une idée à la fois, avec tes mots ; ce n'est pas une preuve ; n'ajoute rien) ».

**Garde-fous** :
- citation mot pour mot (8 mots consécutifs ou plus d'une ligne) → reformulation ;
- les lignes **ne passent jamais par `croire`** : elles ne déplacent aucune opinion. Elles donnent des arguments, pas de la persuasion ;
- un avatar en **doute** reçoit 1 ligne de son camp et 1 ligne « neutre » ; après une bascule, les lignes de son nouveau camp.

---

## 6. Cas limites

| Cas | Ce qui se passe |
|---|---|
| **Un média de son camp relaie une info douteuse** | Confiance élevée, donc la crédence monte ; la réputation basse (`tf` < 0) la freine. Sous 60, la position est « prudence » : conditionnel et demande de confirmation. Démenti par un officiel **adverse** (c ≈ 0,23 à 0,39) : effet partiel, ce qui est réaliste (raisonnement motivé). Démenti par une source **neutre** ou **de son camp** : effet plein, et défiance −10·c envers le média qui l'a relayé si c ≥ 0,5 (code existant). Dès qu'un démenti est connu et que `cr` < 40 : position « rectifie », jamais de relais sans le démenti (règle n°19-3). |
| **Un média adverse dit vrai, et le fait dessert mon camp** | Faible confiance : la crédence monte lentement, et l'avatar peut contester (« c'est TV4 qui le dit, personne d'autre ») sans inventer de contre-fait. Si une source neutre ou de son camp confirme, la répétition fait son œuvre. Dès `cr` ≥ 60 : « concède et recadre ». Le doute sur son camp ne vient que d'un doute mesuré. **Consigne d'animation** (doctrine § 3.7) : si l'entraînement exige que la vérité passe, il faut une confirmation neutre ou officielle, car elle ne s'impose pas seule. |
| **Un média adverse dit quelque chose qui sert mon camp** | Aveu de l'adversaire : c ≥ 0,55. L'avatar le relaie volontiers (« même TV4 le reconnaît »). |
| **Source neutre** | Crue moyennement par tous ; les partisans la créditent de −8·e (média hostile). Pour un neutre, c'est l'arbitre : il tend à la position « compare ». |
| **Fait pratique venu d'un officiel adverse** | 70 % de la pénalité de camp est rendue : un pro-Mercure croit l'horaire de distribution de la préfecture. |
| **Avatar qui ne connaît pas le camp de la source** | Comportement d'aujourd'hui (type seul) ; il l'apprend en 3 lectures. Libellé : « tu ne sais pas trop de quel bord il est ». |
| **Avatar en doute, ou basculé** | Termes de camp divisés par 2 pendant le doute. À la bascule, la base est refaite en deux fois et les abonnements migrent sur plusieurs jours. |
| **Compte de l'annuaire qui est aussi un avatar IA** (préfecture, maire, relais) | L'annuaire fixe la manière dont **les autres** le perçoivent ; son propre comportement ne change pas. |
| **Comptes de joueurs** | Jamais dans l'annuaire. Leur camp n'est pas déclaré : il se perçoit par `pub.bord`, comme dans l'avis n°23 P1.4. |
| **Ancre sur un sujet de victimes** (attaque chimique) | Position autorisée, mais pas d'humour (avis n°22 A7), et l'émoji léger est retiré (avis n°23, piste 9). Une compassion sans cible politique reste conforme à P1. Elle doit quand même dire de quoi il s'agit, d'où vient l'information, et ce qu'il en pense ou demande. |
| **Annuaire vide ou illisible** | Comportement actuel, et une alerte au journal. Aucun blocage. |

---

## 7. Tests

### 7.1 Tests unitaires et local (avant la production)

- **`aPrioriSource`** : les 25 cases du tableau du § 2.3, à ±1 près. Le plafond adverse est respecté. Le fait pratique et l'aveu donnent les valeurs attendues.
- **Migration** : une relation TV4 à 35 (base 35) chez un pro-Mercure affirmé passe à 16. Une relation à 45 (base 35, donc +10 appris) passe à 26.
- **Abonnements** : tirage sur les 105 fiches.
  - 100 % des partisans ont 2 ou 3 médias de leur camp et 1 neutre ;
  - aucun média au-dessus de 60 % ;
  - le même tirage d'un redémarrage à l'autre.
- **`interet`** : les 3 textes cités sont retenus. 10 textes ancrés écrits à la main passent.
- **Attribution** : « TV4 dit que… » sans message de TV4 lu → retenu.
- **Mini-population locale** : 12 avatars (4 pro-Mercure, 4 pro-Arnland, 4 neutres) ; 3 sources (TV4, MercureToday, un neutre) ; 10 messages de médias injectés en 3 h, dont 1 info douteuse de MercureToday, démentie ensuite par le neutre ; et un fait vrai de TV4 qui dessert Mercure.
  - Critères : §7.2 T1 à T4 et T6 tenus.
  - **0** pro-Mercure « ferme » qui reprend le fait de TV4 sans recadrer.
  - Au moins 1 publication « compare » chez les neutres.

### 7.2 À mesurer par NOYAU sur le prochain export de production

Le moteur doit écrire dans chaque proposition spontanée :
- `ancre: { fait, source, stance, relation }` ;
- `interet: { M1, M2, M3, M4, M5, score }`.

Il doit aussi écrire au journal `abonnements tirés` et `annuaire appliqué`. Sans ces champs, le test se fait au juge à l'aveugle.

| # | Mesure | Seuil |
|---|---|---|
| T1 | Part de **vie seule** dans les spontanées ; part d'**état d'âme seul** (score ≤ 1) | ≤ 15 % ; ≤ 3 % |
| T2 | Spontanées avec **source nommée** (M2) ; avec **position** (M3) ; avec **argument** (M4) ; score ≥ 3 | ≥ 50 % ; ≥ 60 % ; ≥ 40 % ; ≥ 75 % |
| T3 | **Cohérence camp ↔ source** (juge à l'aveugle `{source, attitude: approuve, conteste, neutre}` sur toutes les spontanées et réponses qui citent une source de l'annuaire) : un partisan « ferme » qui **approuve** un fait politique d'une source **adverse** défavorable à son camp | ≤ 5 % (hors aveu et hors doute mesuré) |
| T4 | **Attributions inventées** : source nommée sans message correspondant dans les 24 h de l'export | **0** (bloquant) |
| T5 | **Abonnements** (journal) : TV4 suivi par les pro-Arnland / par les pro-Mercure ; MercureToday dans le sens inverse ; média le plus suivi | ≥ 50 % / ≤ 10 % ; idem inversé ; ≤ 60 % de la population |
| T6 | **Confiance** (état eho) envers TV4, médiane par camp | pro-Arnland ≥ 60, neutres de 30 à 50, pro-Mercure ≤ 30 |
| T7 | **Doutes mesurés** sur Mercure chez les pro-Mercure, par 6 h ; part des déplacements d'opinion attribués à une source adverse | ≤ la moitié du 14/10, sans tomber à 0 sur 24 h ; en baisse d'au moins 40 % |
| T8 | **Diversité** : source la plus citée ; fait le plus repris ; débuts « Selon / D'après / X dit que » | ≤ 35 % ; ≤ 30 % ; chacun ≤ 15 % des spontanées |
| T9 | **Connaissances** : lignes recopiées mot pour mot ; une même ligne en 3 h | ≤ 5 % des textes ; ≤ 3 fois |
| T10 | **Orientation P1** : retenues pour orientation, rapportées aux spontanées | pas plus de +50 % par rapport au 14/10 (sinon le juge confond « rapporter pour contester » et « aller contre son camp ») |
| T11 | **Joueurs non lésés** : part des messages de joueurs qui ont reçu une réponse IA pertinente | au plus −3 points par rapport à l'export du 14/10 (bloquant) |
| T12 | **Volume** : spontanées publiées par heure | ≥ 60 % du volume du 14/10. Si moins : l'ancre manque, il faut vérifier l'annuaire `ancrable` et les sources lues |
| T13 | **Test de l'utilisateur** : 20 spontanées tirées au hasard, « est-ce intéressant à lire ? », par rapport à 20 spontanées du 14/10, à l'aveugle | ≥ 70 % de oui, et nettement au-dessus du 14/10 |

---

## 8. Ordre de mise en œuvre conseillé

1. **Annuaire et confiance** (§ 2) : `sources.mjs`, réglage, `lireSocial`, `relation`, `decrireLien`, migration. On mesure T5 et T6 en local.
2. **Abonnements** (§ 3).
3. **Ancre, position, invite, `interet`, attribution, plafonds** (§ 4), avec la phrase ajoutée au juge P1 (§ 4.7).
4. **Connaissances** (§ 5), dès que les ANALYSTES ont livré leurs lignes. Les étapes 1 à 3 marchent sans elles : l'appui devient alors la fiche ou l'autre source.

**Coût** : un appel court par spontanée (juge d'intérêt), plus une reformulation quand une marque manque. Rien d'autre.

---

## 9. Règles durables

1. **Une source a un camp.** Un avatar juge ce qu'il lit selon qui le dit : il croit les siens, se méfie d'en face, et prend en compte la réputation. Le camp d'une source est déclaré une seule fois, dans l'annuaire, et tranché par l'ANALYSTE du pays.
2. **On suit d'abord les médias de son bord**, plus un neutre ; un engagé jette parfois un œil chez l'adversaire.
3. **Pas de publication spontanée sans sujet, sans source et sans position.** La vie seule reste sous 15 %, et l'état d'âme seul ne se publie pas.
4. **Une attribution est vérifiée.** On ne fait jamais dire à une source ce qu'elle n'a pas écrit.
5. **Contester n'est pas inventer.** On conteste par la source, par l'absence de confirmation ou par une connaissance de son camp, jamais par un contre-fait.
6. **Les connaissances de camp donnent des arguments, pas de la persuasion** : elles ne déplacent aucune opinion.
