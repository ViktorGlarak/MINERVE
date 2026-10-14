# Avis n°23 — Orientation des avatars, réponses qui répondent, suivi de conversation (2026-10-14)

**Auteur** : PSYCHOLOGUE · **Demandeur** : l'utilisateur, via NOYAU, sur le relevé du jour (`AVIS\2026-10-14_RELEVE_TEXTES_IA_13h05.md`).
**Objet** : valider, réorienter ou refuser les 9 pistes du relevé. Les 3 premières (P1, P2, P3) sont spécifiées pour être **codées et testées en local tout de suite**.
**Matériau lu** : le relevé ; les extraits complets de l'export de 13 h 05 (186 textes IA, 430 messages de joueurs, 4 compteurs de publications retenues) ; le code du moteur, lu sans le modifier : `app-ia/src/moteur/pont.mjs`, `esprit.mjs`, `redacteur.mjs`, `hashtags-herites.mjs`, `arobase.mjs` ; la route `/api/service/retex` d'`app-social` (`apps/api/src/service/index.ts`).
**Règle de ce fichier** : il part sur GitHub. Aucun message de joueur n'y est cité et aucun compte de joueur n'y est nommé. Les textes des avatars IA, qui sont fictifs, sont cités.
**Lien avec l'avis n°22** : il est toujours en pause. Son étape 1 (forme) et sa partie B5 (suivi des fils) recoupent les pistes 3 et 6. P3 reprend B5 sous une forme réduite (1 ou 2 échanges), comme l'utilisateur l'a demandé.

---

## 0. Ce que la lecture du code ajoute au relevé (causes, pas seulement symptômes)

| Défaut du relevé | Cause trouvée dans le code | Où |
|---|---|---|
| 3.1 Un pro-Mercure doute de Mercure | **(a)** Le registre de voix est une **attitude sans cible**. « Le doute qui se glisse » et ses amorces (« Franchement, entre nous, … », « On nous avait promis… ») ne disent pas **de qui** on doute. Le modèle applique donc le doute au sujet du message lu. Exemples : DomyKos_87 a reçu l'amorce « Franchement, entre nous » sous un message **anti-Mercure** et a douté… de Mercure. _OlegGaspi_ a reçu « On nous avait promis… » et a écrit « …que ce serait une opération de maintien de l'ordre », ce qui est une déception envers **Mercure**. **(b)** Le déclencheur « rumeur sur la FORCE » (`c.or.FORCE === -1`) s'est déclenché sur un message qui **accuse Mercure**. Son test ne regarde pas l'orientation sur l'axe Mercure. **(c)** Les hashtags du parent sont recopiés **sans regarder leur camp** : un avatar pro-Mercure a publié avec `#mercureout #balancetonmer`. **(d)** Ces 3 textes viennent du **groupe témoin**, que rien ne relit (47 réponses sur 121 relevées). **(e)** `decrirePosition` écrit « tu es partagé sur… » pour toute opinion comprise entre −20 et +20. Un modéré à −12 lit donc qu'il est neutre. | `esprit.mjs` VOIX (≈ l. 1200-1250), `decrirePosition` (l. 59) ; `pont.mjs` l. 514-518 ; `relireHybride` (témoin non relu) |
| 3.1 Le fil pro-Mercure est lu par 26 avatars, 25 l'ignorent | Aucun facteur « mon camp » dans l'attention. `camp_affiche` vaut « inconnu » pour **toute** la population (tous les en-têtes de l'export le confirment), donc `facteurGroupe` et la relation « pair » ne jouent jamais. Les déclencheurs pro-Mercure ne réagissent qu'aux pénuries, aux rumeurs et au N.O.M, jamais à un habitant de leur bord. | `pont.mjs` `filDe` (l. 376) ; `esprit.mjs` l. 349, 438 |
| 3.2 « Inspirée de X → réponse sous son message » | La publication spontanée est demandée « sur ce qui te préoccupe en ce moment ». Elle est ensuite **rangée** sous le message d'un joueur dès que `trouverSource` lui trouve 1 ou 2 mots communs (`placeSous`, `versJoueur`, `versReponse`). Le rédacteur la reçoit comme une « réponse », mais avec une intention de publication. **La relecture la traite en publication** (`pub: orpheline`, qui est nul) : la question Q4 (« répond-il au message cité ? ») n'est donc **jamais posée**. On compte 22 cas dans l'export. | `pont.mjs` l. 886-887, 896, 911, 918-921 |
| 3.3 Le joueur qui répond n'a jamais de suite (0 sur 8) | **Bug de structure.** Les avatars répondent surtout **en commentaire** sous les messages des joueurs. Quand un joueur répond sous ce commentaire, la route `/retex` d'`app-social` exporte `parent: post-<id>`, c'est-à-dire **la publication**, et non le commentaire visé, alors que `SocialComment.parentId` existe en base. `reponseAMoi` trouve donc comme auteur du parent le joueur qui a publié, pas l'avatar. Aucune notification, aucune priorité. Autre point : la mention est testée par `p.texte.includes(a.handle)`, qui exige l'@username exact et respecte la casse. Un prénom-nom ou un @ mal casé ne compte pas. | `app-social` route `/retex` ; `pont.mjs` `reponseAMoi` l. 339, `avecParent` l. 348, et 6 autres calculs `fil.find((x) => x.id === p.parent)` (l. 596, 703, 775, 807, 854) |
| 3.7 Mentions inventées | `rafraichirNoms` ne lit que `/api/service/users?limit=100`. La population IA compte à elle seule environ 100 comptes, donc beaucoup de joueurs n'ont pas de nom connu. Leur handle est alors **fabriqué** depuis le nom affiché (`pont.mjs` l. 201, `@rolf_weber`), puis traité comme un compte « connu » par `arobaser` et le nettoyage des mentions. Un @ inconnu est réduit au username nu (« _DFataliste encore… ») au lieu du nom affiché. | `pont.mjs` l. 185-187, 201, 503-504 |

---

## 1. Verdicts

| # | Piste du relevé | Verdict | Priorité |
|---|---|---|---|
| 1 | Orientation d'abord : contrôle de sortie et attraction vers les fils de son camp | **VALIDÉE, réorientée** : on corrige d'abord les causes en amont (cible du doute, déclencheur, hashtags adverses, zone morte), puis on ajoute un contrôle de sortie qui **distingue l'évolution mesurée de la dérive** | **P1, maintenant** |
| 2 | Fin de la « réponse inspirée » ; une réponse répond au parent | **VALIDÉE** | **P2, maintenant** (à tester en premier : c'est le plus simple) |
| 3 | Suivi de conversation | **VALIDÉE**, à condition de corriger d'abord le bug du parent de commentaire | **P3, maintenant** |
| 4 | Questions directes | **VALIDÉE**, fusionnée avec P3 (même passe de code) | Avec P3 |
| 5 | Diversité émotionnelle par tempérament | **RÉORIENTÉE** : une permission écrite dans la consigne ne change rien, le modèle l'ignore. Il faut des plafonds de population tout de suite, et des émotions tirées par le code plus tard | Plafonds avec P1, le reste avec l'étape 1 de l'avis n°22 |
| 6 | Forme | **VALIDÉE** : c'est l'étape 1 de l'avis n°22, avec en plus un registre d'écriture par avatar | Avec l'étape 1 de l'avis n°22 |
| 7 | Hashtags | **VALIDÉE, modifiée** : l'interdiction d'hériter un # adverse passe dans P1 ; le reste demande une **décision de l'utilisateur**, car cela contredit sa demande du 12/10 (« tout message IA porte un # ») | Le # adverse avec P1 ; le reste après P1 à P3 |
| 8 | Mentions | **VALIDÉE** (cause trouvée, voir § 0) | Avec P3, qui a besoin d'identifier correctement l'interlocuteur |
| 9 | Langue et ton | **VALIDÉE** | Émoji léger et phrase inachevée : tout de suite (2 règles de code) ; le reste avec l'étape 1 |

**Règle transversale.** Les contrôles de **code** de P1, P2 et P3 s'appliquent à **toute la population, groupe témoin compris**. C'est l'extension de la règle n°18 (4). Le témoin sert à mesurer la relecture par le modèle, pas à laisser passer un effet ILI inversé ou une réponse qui ne répond pas. Le seul appel au modèle ajouté pour tous est le **classement d'orientation de P1**, et seulement sur soupçon (§ P1.3). Il protège le camp, ce n'est pas une expérience de qualité.

**Ordre de test conseillé** : P2 (suppression, mesure immédiate), puis P3 (qui demande un petit changement dans `app-social`), puis P1 (le plus gros chantier).

---

## P1. Faire respecter l'orientation de l'avatar, sans lui interdire d'évoluer

### P1.1 Règle psychologique

- **Identité sociale et cohérence** *(Tajfel & Turner 1979, théorie de l'identité sociale ; Festinger 1957, dissonance — à sourcer)*. Un habitant attaché à un bord **remarque** ce qui le conforte, **attribue** les torts à l'autre bord et **défend** les siens quand ils sont attaqués. Il ne doute de son propre bord qu'à la suite d'une accumulation de faits. C'est l'hystérésis de la doctrine § 3.4 : *une phase de doute précède la bascule, basculer demande une accumulation*.
- **Homophilie et exposition sélective** *(McPherson et al. 2001 ; à sourcer)*. On lit, on aime et on commente davantage les messages de son bord. OASIS donne le repère : camp 0,10 contre 0,06 pour le camp adverse (§ 3.7).
- **Biais du modèle** (§ 3.7, OASIS). Les agents LLM convergent vers la foule et vers une voix prudente et consensuelle (« on ne sait plus quoi croire », « attendons la préfecture »). Les correcteurs de code ne sont pas un luxe : ce sont des **correcteurs de biais du modèle**. Le dépôt en tire la règle de camp (CLAUDE.md) : *un avatar qui dit l'inverse de son camp produit l'effet ILI inverse*.
- **Distinction à tenir** : l'**évolution légitime** est mesurée par le moteur d'opinions (`m.opinions`, `m.bascules[axe].doute` / `.bascule`, `tendances()`), parce que l'avatar a cru des faits et en a reçu les effets. La **dérive** est un texte qui contredit la position actuelle **sans** que le moteur ait mesuré ce mouvement. La première se laisse voir. La seconde se corrige.

### P1.2 Corrections en amont (sans appel au modèle, à faire d'abord)

1. **Une cible explicite pour chaque voix** (`esprit.mjs`, `VOIX`). On ajoute deux champs à chaque bloc, `cible_critique` et `cible_defendue`, et l'invite les reprend chaque fois qu'un registre est imposé (`pont.mjs` l. 744, ligne « Ce que tu lis en N te fait réagir… ») :
   - pro-mercure-* : « ton doute, ta colère portent sur **la FORCE, ses promesses et les communiqués** ; **jamais sur Mercure** » ;
   - pro-arnland-* : « ce que tu critiques, ce sont **les rumeurs et ceux qui font le jeu de Mercure** ; tu ne mets **jamais** la FORCE en doute sur le fond, seulement sur des manques concrets » ;
   - neutre : aucune cible imposée.
2. **Des amorces sans ambiguïté.** On supprime les amorces qui ne nomment pas leur cible (« On nous avait promis… », « Franchement, entre nous, … », « On verra bien. »), ou on leur ajoute la cible (« La FORCE nous avait promis… »). Conformément à la règle n°22-3 (une amorce devient un tic), on préfère **réduire** les amorces à 2 par registre au plus, toutes ciblées.
3. **Déclencheurs qui regardent les deux axes pivots.** Pour pro-mercure-*, les tests « rumeur sur la FORCE », « fait qui touche la FORCE » et « rumeur de menace » exigent en plus `c.or.Mercure !== -1` et l'absence de # adverse dans le message (point 4). Même chose en miroir pour pro-arnland-* (`c.or.FORCE !== +1` sur « un déçu qui lâche prise »). Rappel de la convention : orientation −1 = le fait accuse l'axe.
4. **Jamais un hashtag adverse.** Dans `proposer` (`pont.mjs` l. 510-518), avant `heriterHashtags`, on **filtre** `parentTags` : on retire tout # dont le sens déclaré (`CAMPAGNES`) ou appris (`h.sens`) est **opposé** à l'opinion de l'avatar sur cet axe dès |opinion| ≥ 5. Le seuil actuel de `sensHashtag`, 25, laisse passer tous les modérés. Pour un avatar de cohorte pro-*, un # **de sens inconnu** ne s'hérite pas non plus en réponse. Effet de bord voulu : moins de # plaqués (piste 7).
5. **Une zone morte plus étroite pour les avatars de cohorte** (`decrirePosition` / `decrirePositions`). Si l'avatar a une voix pro-*, on écrit :
   - pour |v| < 5 : « tu es partagé » ;
   - pour 5 ≤ |v| < 20 : « tu **penches** pour / contre X, sans le crier » ;
   - au-delà : les libellés actuels.

   C'est l'application de la règle n°19 (2) : un écart que l'invite ne montre pas n'existe pas pour les joueurs.
6. **La consigne d'orientation ne disparaît plus en silence.** Aujourd'hui la ligne `[orientation]` est retirée de la persona dès que `voixActive()` est faux (`esprit.mjs` l. 1085). Pour un pro-Mercure, c'est le cas dès que FORCE ≥ −5, y compris quand `opinions_initiales` n'a pas d'axe FORCE, qui vaut alors 0. Nouvelle règle :
   - on la retire seulement si `m.bascules[pivot].bascule` existe : c'est la bascule mesurée, qui doit se voir ;
   - si l'avatar est en doute sur le pivot, on la remplace par « tu restais attaché à <bord>, mais ce que tu lis t'ébranle : tu poses des questions, tu ne changes pas de camp » ;
   - **contrôle au chargement** : une fiche à voix pro-* sans opinion initiale sur son pivot déclenche une alerte au journal (« fiche incomplète »).

### P1.3 Contrôle de sortie (après la relecture, avant `sansSubstance` ; réactions ET publications spontanées)

**Position attendue**, calculée par le code. Nouvelle fonction `Esprit.positionAttendue(axe)` → `{ signe, force, etat }` :

| État | Condition (moteur d'opinions) | Ce qui est permis vis-à-vis de son propre bord | Ce qui est interdit |
|---|---|---|---|
| **ferme** | \|op\| ≥ 10, ni doute ni bascule sur l'axe | défendre, critiquer l'autre bord, se taire, parler de sa vie | douter de son bord, le critiquer, défendre l'autre bord |
| **tiède** | \|op\| < 10, ni doute ni bascule | une **question** sur son bord | défendre l'autre bord |
| **doute** | `bascules[axe].doute === true` | questions, réserves, « je ne sais plus » **sur son bord** | défendre ouvertement l'autre bord |
| **bascule** | `bascules[axe].bascule` présent | la **nouvelle** position fait référence | revenir à l'ancienne sans nouvelle bascule mesurée |
| **tendance** | `tendances(t)` signale l'axe | une nuance d'indulgence ou de méfiance dans le sens de la tendance | — |

Axes pivots par voix (convention à **vérifier** dans les `opinions_initiales` des fiches) :
- pro-mercure : Mercure > 0 et FORCE < 0 ;
- pro-arnland : le contraire ;
- neutre : aucun contrôle de bord, seulement le lexique interdit.

**Étape 1, soupçon (code, pour tous)** : `soupconOrientation(a, texte, pub)` est vrai si :
- l'avatar a une voix pro-* ;
- **et** le texte ou le parent touche un pivot : `/\bmercure\b|\bMER\b|\bFORCE\b|Force\.L|soldats?|arm[ée]e|militaires?|convois?|OTAN|Arnland|Pallesson|occupation|invasion|op[ée]ration/i`, ou porte un # de sens connu.

L'estimation est de 15 à 25 % des textes des avatars de cohorte.

**Étape 2, classement (un appel court, température 0,1, pour tous, seulement sur soupçon)** :
`{"vise": "Mercure" | "FORCE" | "institutions" | "aucun", "sens": "pour" | "contre" | "doute" | "neutre", "pourquoi": "<12 mots>"}`
Invite : « Dans ce message, qui l'auteur défend-il, critique-t-il ou met-il en doute ? » Les champs sont lus par le code, jamais publiés.

**Étape 3, décision du code** : on compare `{vise, sens}` à `positionAttendue(vise)` en suivant le tableau ci-dessus.
- Conforme → publié.
- Non conforme → **une** reformulation, avec une consigne explicite : « Tu es <bord>. Ton message met en doute <son bord> : ce n'est pas toi en ce moment. Garde le sujet et l'émotion, mais ton doute ou ta colère portent sur <cible_critique>. » Puis on reclasse.
- Toujours non conforme → **retenu** (J'aime si `ressenti_fond` vaut d'accord, sinon rien), avec au journal `orientation retenue` (vise, sens, état, opinion).

**Cas limites** :
- une compassion pour des victimes sans cible politique (vise « aucun ») n'est **pas** une dérive ;
- un pro-Mercure qui critique la **préfecture** est conforme (axe institutions, aligné) ;
- une ironie : on laisse le classement trancher, et en cas de doute on publie (même règle que la relecture : un doute n'est pas un défaut) ;
- un relais : il est exclu, ses lignes le tiennent ;
- un message privé : même contrôle (un pro-Mercure n'y trahit pas plus son camp) ;
- un échec du classement (JSON illisible) : publié et compté à part.

### P1.4 Attraction vers les fils de son bord

- **Bord d'un message**, sans `camp_affiche` : signe de `pub.orientation` / `pub.affirmation.orientation` sur les pivots (extraction déjà faite pour tout message ≥ 40 caractères), sinon # de sens connu (`CAMPAGNES`). Il est calculé une fois, dans `lireSocial`, et stocké dans `pub.bord ∈ {mercure, arnland, null}`.
- **`filDe`, score** : +30 si l'avatar a une voix pro-* active, si |op pivot| ≥ 10 et si `pub.bord` est **le sien** ; +15 si `pub.bord` est **adverse** et |op pivot| ≥ 40 (on surveille l'ennemi). Les priorités au-dessus restent intactes : interpellation et réponse à soi (1000), abonnement (100), joueur sans réponse (60 + 30).
- **Nouveau déclencheur de voix** pour pro-mercure-* et pro-arnland-* : « un habitant de son bord ». Test : `!pub.estIA && pub.bord === son bord`. Probabilité 0,5 pour un affirmé, 0,3 pour un modéré. Action : aimer **ou** répondre dans son registre.
- **Ce qui ne bouge pas** : le plafond par message (2 réponses IA par 30 min, 4 au total) et le quota de voix (`quotaVoix`). Le fil d'un joueur pro-Mercure doit recevoir 2 ou 3 voix de son bord, pas un chœur.

### P1.5 Plafonds de population liés au biais du « citoyen sage » (piste 5, partie immédiate)

On ajoute deux entrées à `GABARITS` (`pont.mjs` l. 236) :
- « renvoi vers la préfecture / Info.gouv » : `/(attend(ons|re)|suivez|voir|consignes?) [^.!?]{0,20}(pr[ée]fecture|info\.?gouv)/i`, au plus 2 par heure ;
- « on ne sait plus quoi croire » : `/(on ne sait plus|je ne sais plus|difficile de savoir) [^.!?]{0,12}(quoi|qui) croire|qui raconte quoi/i`, au plus 1 par heure.

### P1.6 Test en local

**A. Rejeu hors fil de l'export du 14/10** (script à écrire par PLEIADE, par exemple `scripts/rejeu-orientation.mts`). Les 186 textes passent par `soupconOrientation` puis le classement, avec l'état d'opinion de chaque avatar lu dans eho, sans rien publier.
- **Rappel** : les 3 textes cités au relevé (DomyKos_87, Rb_4ever, _OlegGaspi_) sont **tous** classés non conformes.
- **Faux positifs** : au plus 5 % des textes non conformes, jugés par l'utilisateur sur un échantillon de 20 textes signalés.
- **Hashtags** : 0 # adverse dans les textes une fois le filtre P1.2-4 appliqué (`#mercureout`, `#balancetonmer` chez un pro-Mercure).

**B. Mini-population locale** : 12 avatars (4 pro-mercure, 4 pro-arnland, 4 neutres) ; 2 comptes joueurs ; 3 h de jour ; un fil de joueur pro-Mercure (hommage, honneur) et un fil anti-Mercure.
- **0 texte publié** par un pro-Mercure qui doute de Mercure ou défend la FORCE alors que son état est « ferme ». La vérification se fait a posteriori, par le même classement à température 0, sur tous les textes de cohorte publiés.
- **Attraction** : ≥ 30 % des lecteurs pro-Mercure du fil pro-Mercure réagissent (J'aime ou réponse), avec au moins 2 réponses (contre 1 sur 26 le 14/10), sans dépasser 2 réponses IA en 30 min.
- **Part colorée** des avatars pro-* entre plancher et plafond de `quotaVoix` (modéré 15-35 %, affirmé 30-50 %).
- « On ne sait plus quoi croire » au plus 5 %, renvoi à la préfecture au plus 5 % des textes IA.

**C. Non-régression de l'évolution légitime** : 3 jumeaux d'un pro-Mercure-modéré.
- (i) État « ferme », FORCE −30. (ii) `bascules.FORCE.doute = true`, FORCE −12. (iii) `bascules.FORCE.bascule` posée, FORCE +8.
- On fait passer les mêmes 5 textes types, dont « je me demande si Mercure ne nous a pas raconté des histoires » et « la FORCE fait ce qu'elle peut ».
- Attendu : (i) les deux sont retenus ou reformulés ; (ii) le premier passe, le second est reformulé ; (iii) les deux passent.
- Critère : **100 % conforme au tableau**.

---

## P2. Plus de « réponse inspirée » rangée sous le message d'un autre

### P2.1 Règle psychologique

- **Paires adjacentes et pertinence** *(analyse conversationnelle, Sacks & Schegloff ; principe de coopération et maxime de pertinence, Grice 1975 — à sourcer)*. Une réponse est le second terme d'une paire : elle se rapporte au premier, par son sujet, sa question ou son émotion. Une « réponse » qui parle d'autre chose est perçue comme une **non-écoute**, ce qui est pire que le silence pour celui qui a écrit.
- **REF-03** : on choisit l'action qui sert ses préférences (appartenance, reconnaissance) ou réduit l'incertitude. Écrire sa vie sous la détresse d'un autre ne sert rien de tout cela. L'action juste est un J'aime ou une vraie réponse.
- **Règle n°18 (3)** : un commentaire public doit apporter quelque chose **à ce message-là**.
- Je reconnais que la conversion « inspirée → réponse » répondait à une demande légitime de l'utilisateur (12/10 : « qu'ils s'impliquent plus dans les posts des joueurs »). Cette implication doit passer par la **réaction au message numéroté**, que la persona demande déjà (« si ce que tu as envie d'écrire RÉAGIT à un message de ton fil… réponds à ce numéro »), et non par le reclassement d'une publication écrite pour soi.

### P2.2 Spécification codable

1. **Suppression** dans `pont.mjs` :
   - `placeSous` et `versJoueur` (l. 886-887) ;
   - les deux exemptions `|| versJoueur` du test de rétention (l. 889) : la publication inspirée obéit de nouveau au déclencheur et à l'écart de 60 min ;
   - `action: versJoueur ? "repondre" : "publier"` dans `redigerPour` (l. 896) → toujours `"publier"` ;
   - `srcRep` / `versReponse` (l. 918-921) et leurs branches dans `proposer(...)` (l. 923) : `action` vaut `orpheline ? "repondre" : "publier"`.

   On garde `source` (pour la mesure) ; `noterDecision(..., { modele: "publier (inspirée)", finale: "publier" })`.
2. **La « réponse orpheline » reste**, car c'est une publication *adressée* (@ ou « courage <Prénom> »). Elle passe déjà la relecture avec `pub = orpheline`, donc avec Q4 ; elle passe aussi le contrôle 3.
3. **Contrôle de pertinence, toute la population**. Nouvelle fonction `repondAuParent(texte, parent)` dans `esprit.mjs`, appliquée à toute action `repondre` et `partager` (mot d'accompagnement), après la relecture :
   - **passe par le code** si `motsCommuns(texte, parent.texte)` (`hashtags-herites.mjs`, hors # et @) donne au moins 2 mots ; ou au moins 1 mot si le parent fait moins de 80 caractères ; ou si le texte reprend un terme à chiffre du parent (D32, 616) ;
   - **sinon**, un appel court (température 0,1) : « MESSAGE : « … » / RÉPONSE : « … ». La réponse réagit-elle à ce que dit le message : son sujet, sa question ou ce qu'il ressent ? » → `{"repond": true|false, "pourquoi": "<12 mots>"}` ;
   - **on économise l'appel** pour le groupe « relu » si la relecture a tourné avec `pub` et n'a pas levé Q4 ;
   - `repond: false` → **pas de reformulation** : J'aime si `ressenti_fond` ∈ {d_accord, soulage} ou `ressenti_forme` vaut « touchee », sinon rien. Au journal : `réponse sans lien → J'aime`.
4. **Cas limites** :
   - le soutien à une détresse avec peu de mots communs (« moi non plus, pas de nouvelles de mon frère depuis hier ») est pertinent : c'est l'appel au modèle qui le reconnaît, d'où l'étape 2 ;
   - un parent très court (« ? », un émoji, « bonne nuit ») : on juge sur le parent **et** son propre parent (`avecParent`) ; sur un « bonne nuit » sans autre contenu, la seule réponse pertinente est courte et liée (« bonne nuit, ici aussi ça a été long »), sinon J'aime ;
   - les réponses d'**élan** (riposte, correction, avis n°21) sont **exemptées**, car construites sur le parent ;
   - le chat privé n'est pas concerné (la conversation y est entière).
5. **Coût** : 1 appel court pour 20 % des réponses au plus (estimation à vérifier au test).

### P2.3 Test en local

- **Rejeu unitaire** : une fixture du tour avec 3 messages de joueurs (« bonne nuit », détresse, appel à l'aide) et une `rep.publication` du modèle ayant 1 ou 2 mots communs avec l'un d'eux. Attendu : `action: "publier"` et `cible: null`, dans **100 %** des cas (les 22 cas du 14/10 ne peuvent plus se produire). La note « inspirée de … → réponse sous son message » n'apparaît **plus jamais** au journal.
- **Session locale de 3 h** (mini-population B de P1) avec 20 messages de joueurs : 5 de vie, 5 de détresse, 5 questions, 5 opinions.
  - **Réponses sans lien** : au plus 2 % des réponses IA publiées (objectif 0). Le jugement se fait a posteriori, à l'aveugle, par le même appel à température 0, et l'utilisateur relit les cas signalés.
  - **Joueurs non lésés** (critère bloquant de l'avis n°22) : la part de messages de joueurs recevant au moins une réponse IA **pertinente** ne baisse pas de plus de 3 points par rapport à la session témoin sans P2. Si elle baisse davantage, on avance la piste 4 (questions directes).

---

## P3. Suivi de conversation : l'avatar à qui l'on répond revient (1 ou 2 échanges)

### P3.1 Règle psychologique

- **Norme de réciprocité** *(Gouldner 1960 — à sourcer)* et **absence remarquable** *(Schegloff : le second terme manquant d'une paire adjacente se remarque — à sourcer)*. Quand quelqu'un vous répond ou vous nomme, se taire est un acte. Une vraie personne revient presque toujours, sauf devant un troll, une insulte ou une simple approbation.
- **Attention** (doctrine § 3.7) : la mention est **absolue** dans le score de remarque. C'est la notification qu'un vrai compte voit en premier.
- **Bornes** (avis n°22 B5, réduites à la demande de l'utilisateur) : un échange humain sur un réseau s'éteint vite. On fixe 1 ou 2 retours, jamais de ping-pong.

### P3.2 Spécification codable

**1. Corriger la détection (bloquant)**
- `app-social`, route `/retex` (`apps/api/src/service/index.ts`) : on ajoute à chaque commentaire `parent_commentaire: c.parentId ? \`commentaire-${c.parentId}\` : null` (le champ existe en base). La modification se fait chez PLEIADE, testée en local avant d'être poussée.
- `pont.mjs`, `lireSocial` (l. 204) : `pub.parentCommentaire = ev.parent_commentaire || null`.
- Nouvel assistant `parentDirect(p) = fil.find((x) => x.id === p.parentCommentaire) ?? fil.find((x) => x.id === p.parent)`. Il **remplace** les 8 calculs actuels du parent : `reponseAMoi` (l. 341), `avecParent` (l. 350), `redigerPour` (l. 596), `interpelle` (l. 703), `viseTot` (l. 775), `visePar` (l. 807), `appliquer…reponseAMoi` (l. 854).
- **Repli** si le Social est ancien et sans le champ : un commentaire qui nomme l'avatar (voir point 2) sous une publication où l'avatar a commenté dans les 6 dernières heures compte comme une réponse à l'avatar.

**2. Élargir la mention**
`mentionne(a, texte)` est vrai si :
- `@username` est présent, **sans tenir compte de la casse** ;
- ou `username` sans @, comme mot entier ;
- ou le **nom affiché complet**.

Le prénom seul ne compte que s'il est unique dans le fil de cette publication. Cette fonction remplace `p.texte.includes(a.handle)` aux l. 355, 376, 703, 813, 815, 817 et dans l'exemption du plafond par message.

**3. Priorité au tour suivant** (largement en place : score 1000 et `interpelle` contourne `prochaineLecture`)
- Face à un **joueur**, le seuil d'activité passe de 0,1 à 0,05 (l. 710), sauf pendant le sommeil.
- La nuit (01-06 h), on ne répond pas : la fenêtre de 24 h de `horsFil` fait lire le message au réveil.
- **Contexte** : `avecParent` montre déjà le message de l'avatar (`moi: true`). On l'étend aux **3 derniers messages** de l'échange, pour que l'avatar sache ce qu'il a dit.

**4. Décision de revenir** (code, après la décision du modèle). Si la publication est une **conversation avec un joueur** (réponse à l'avatar ou mention), que le modèle a choisi `aimer` ou `ignorer` et que ce n'est ni une insulte (l'élan de l'avis n°21 s'en charge) ni un troll (affinité ≤ −40 et rancune ≥ 0,6), on tire `tirageElan(a.handle, pub.id, "suivi") < p_retour`, avec :

| Le message du joueur… | p_retour |
|---|---|
| mentionne l'avatar par @ | 0,8 |
| pose une question (« ? » et un mot interrogatif) ou contredit (`ressenti_fond` ∈ {rejette, doute}) | 0,6 |
| approuve ou remercie | 0,3 (sinon J'aime) |
| n'a pas de contenu (15 caractères au plus : « ok », « merci », un émoji) | 0 (J'aime) |

Si le tirage réussit, un appel court écrit la réponse (rédacteur si l'avatar est dans le groupe d'essai, sinon persona sans simulation), avec la consigne : « <Nom> te répond directement. Réponds-lui d'abord à sa question ou à son objection, en une ou deux phrases, puis arrête-toi. » Le texte passe ensuite les contrôles habituels, puis P1 et P2.

**5. Bornes**
- **État** : `a.m.conversations[`${postId}|${interlocuteur}`] = { n, dernierT, derniers: [] }`.
- **Retours de l'avatar par conversation** : au plus **2** face à un joueur ; au plus **1** face à une IA (A → B → A, puis arrêt).
- **Arrêt** :
  - plafond atteint ;
  - 12 h écoulées ;
  - insulte (avis n°21) ;
  - répétition (`ressemblance` ≥ 0,4 avec ses messages de la conversation) ;
  - message du joueur sans contenu ;
  - deux tours sans fait nouveau.
- **Plafonds horaires** : un retour compte dans `maxParHeure` ; il garde l'exemption actuelle de **+1 par heure** (l. 817), qui est étendue aux réponses directes. Il compte aussi dans `envoisPopulation`, avec une exemption bornée : au-delà du plafond de population, les retours vers des joueurs passent jusqu'à **1,2 fois** ce plafond, pas plus.
- **Délai humain** : `delai: [120_000, 900_000]` (2 à 15 min) au lieu de 5 à 45 s. Une réponse en 10 s à une réponse fait robot (avis n°18 M5).
- **Piste 4, fusionnée** : dans `filDe`, +40 pour un message de joueur qui contient « ? » et un mot interrogatif, toujours sans réponse IA après 10 min. Une question **adressée** à un avatar relève de P3 (score 1000).

### P3.3 Test en local

**Tests unitaires**
- fixture `/retex` avec `parent_commentaire` qui vise le commentaire d'un avatar → `reponseAMoi` vrai ;
- même fixture sans le champ et avec le nom de l'avatar dans le texte → vrai par le repli ;
- sans le nom → faux ;
- `mentionne` : @ mal casé, username nu et nom complet → vrai ; prénom partagé par 2 comptes du fil → faux.

**Scénario local** : Social, eho, 6 à 10 avatars, 2 comptes joueurs de test, en journée. 30 stimuli :
- 10 réponses à un commentaire d'avatar contenant une question ;
- 5 réponses à un commentaire d'avatar qui le contredisent ;
- 5 approbations ;
- 5 @mentions dans une publication neuve ;
- 5 réponses sous une publication d'avatar.

**Critères de réussite**

| Critère | Seuil |
|---|---|
| Détection | 100 % des 30 stimuli entrent dans le fil de l'avatar visé au premier tour où il est éveillé ; le diagnostic du fil (`noterHorsFil`, `noterEvince`) ne montre aucun motif pour eux |
| Retour sur question ou mention | ≥ 70 % |
| Retour sur contradiction | ≥ 50 % |
| Approbations | retour ≤ 40 %, J'aime ≥ 50 % |
| Délai médian | 3 à 10 min, aucun sous 1 min |
| Conversations | 0 conversation avec plus de 2 retours de l'avatar vers un même joueur ; 0 chaîne IA ↔ IA de plus de 3 messages |
| Plafonds | aucun avatar au-delà de `maxParHeure` + 1 ; population ≤ 1,2 fois `MESSAGES_PAR_HEURE` × crise |
| Pertinence | les retours passent P2 dans 100 % des cas |
| En production, au prochain relevé | « joueur qui répond à un avatar → l'IA revient » ≥ 60 % (0 sur 8 le 14/10) ; « questions directes sans réponse IA » ≤ 2 sur 19 |

---

## 2. Les six autres pistes : une ligne de spécification chacune

| # | Spécification | Priorité |
|---|---|---|
| 4 | Questions directes : `filDe` +40 pour une question de joueur sans réponse IA après 10 min (mot interrogatif exigé, question rhétorique exclue) ; consigne « si l'on pose une question à laquelle ta ville ou ton métier te permet de répondre, réponds-y d'abord » (avis n°18 M6) | Avec P3 |
| 5 | Plafonds de population « préfecture » (2 par heure) et « on ne sait plus quoi croire » (1 par heure) dans `GABARITS` (§ P1.5) ; puis nuance tirée **au décideur** selon le tempérament (dictionnaire des émotions, rotation de population, règle 4) ; colère, ironie et défiance passent par les voix affirmées et les fiches (méfiant, râleur), le déni et le complotisme seulement si la fiche le porte (crédulité ≥ 0,6 ou caractère méfiant), **jamais** avec un fait inventé | Plafonds avec P1 ; le reste avec l'étape 1 de l'avis n°22 |
| 6 | Étape 1 de l'avis n°22 telle quelle (émoji final ≤ 45 %, « … » ≤ 20 %, bandes de longueur des réponses 20-70 / 70-140 / 140-220), avec en plus un `registre_ecrit` par avatar tiré de la fiche (langage et âge) : soigné, courant ou relâché ; en registre relâché, 30 % des réponses sans majuscule initiale ni point final, et des abréviations **seulement** si la fiche en donne | Avec l'étape 1 de l'avis n°22 |
| 7 | En réponse et en citation : 0 # par défaut ; 1 au plus s'il s'agit d'une campagne **alignée** sur l'avatar (p 0,15) ; jamais de # adverse (déjà dans P1) ; plus de `#3615MyLife` forcé ; `hashtagsDuSujet` seulement si au moins 2 termes distinctifs concordent. **À décider par l'utilisateur** : je propose que le Cockpit attribue une réponse aux # de **son fil** (côté serveur) au lieu de les recopier dans le texte. La mesure par hashtag reste, le plaquage disparaît | Le # adverse avec P1 ; le reste après P1 à P3, sur décision de l'utilisateur |
| 8 | `rafraichirNoms` lit **tous** les comptes (pagination, ou résolution par `identity_id`) ; un handle fabriqué depuis le nom affiché (l. 201) est marqué `fabrique` et exclu de `arobaser` et des « connus » ; un @ inconnu redevient le **nom affiché**, pas le username nu | Avec P3 |
| 9 | Émoji léger (😂🤣😅😆😁🙃😜) retiré par le code quand le texte ou le parent touche la mort, une blessure, une arme, un gaz, une attaque ou une disparition ; « phrase inachevée » ajoutée à `BLOQUANT` quand elle survit à la reformulation (retenue, jamais publiée) ; pour le groupe relu, Q4bis « met-il en doute la parole d'une personne en détresse ? » ; écart entre pensée et texte confié au rédacteur | Émoji et phrase inachevée tout de suite ; le reste avec l'étape 1 |

---

## 3. Règles durables

1. **Une attitude de voix sans cible devient l'inverse de son camp.** Tout registre de cohorte (doute, déception, colère) nomme **ce sur quoi** il porte.
2. **Le moteur d'opinions est seul juge de l'évolution.** Un texte peut s'écarter du camp de la fiche si et seulement si l'état mesuré (doute, bascule, tendance) l'autorise. Tout autre écart est une dérive du modèle et se corrige.
3. **On n'hérite jamais d'un hashtag du camp adverse.** Un # porte un camp, et le recopier, c'est le soutenir.
4. **Une réponse répond.** Un texte écrit pour soi ne se range jamais sous le message d'un autre. Une réponse sans lien avec son parent devient un J'aime, ou rien.
5. **Quand on te répond, tu reviens**, une ou deux fois, avec un délai humain, sans ping-pong et sans dépasser les plafonds.
6. **Les garde-fous de camp et de pertinence s'appliquent au groupe témoin.** Le témoin mesure la relecture, il ne doit pas laisser passer un effet inversé.
