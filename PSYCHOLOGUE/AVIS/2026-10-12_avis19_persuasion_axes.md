# Avis n°19 — Coefficient de persuasion et axes d'opinion éditables (2026-10-12)

**Auteur** : PSYCHOLOGUE · **Demandeur** : NOYAU (pour PLEIADE)
**Sources** :
- constat de l'essai réel DELATTRE 26, relevé de 15 h 47 (105 avatars, environ 6 h de fonctionnement), transmis par NOYAU ;
- code lu, sans le modifier : `app-ia\src\moteur\esprit.mjs` (`AXES` l. 12, `nettoyerAxes` l. 93, `croyance` l. 394, `perimerAbsences` l. 397, `croire` l. 426-476, `seuilBascule` / `plafondJour` l. 488-489, `deplacerOpinion` l. 495-532, `opinionner` l. 534-550, `decrirePositions` l. 551, `evoluer` l. 604 (k), `bloc` l. 731, `sensHashtag` l. 733, `filtrerHashtags` l. 824, `voixActive` l. 850) ; `pont.mjs` (`crise()` l. 470, `maxParHeure` l. 30, `colore` l. 418, `voix_defaut` l. 94) ; `memoire.mjs` l. 65-69 (contrôle d'orientation des blocs nocturnes) ; `synthese-opinions.ts` ; `app\api\bff\reglages\route.ts` (liste `AXES` figée l. 12) ; `components\ReglagesMoteur.tsx` (coefficient de crise) ;
- doctrine : `PSYCHOLOGUE\MEMOIRE.md` §3.4 (mise à jour pondérée, confiance bornée, retour de flamme, hystérésis), §3.7 (OASIS : troupeau et extrémisation), avis n°2 (croyance → opinion), n°3 (plafond et seuil par ancrage), n°4 (inertie au retour), n°8 (hashtags).

> **Décisions de l'utilisateur prises en compte** : (1) l'« option 3 » n'est acceptée que si elle est **réglable depuis l'app-ia** (écran Réglages du Moteur IA, comme le coefficient de crise : effet au cycle suivant, historique), sous la forme d'un coefficient « persuasion » où 1 = comportement actuel ; (2) les axes d'opinion doivent pouvoir être **ajoutés, supprimés et modifiés** depuis le Moteur IA.

---

## 0. Lecture du constat : pourquoi les opinions bougent si peu

Les chiffres de 15 h 47 sont **cohérents avec les formules**. Ce n'est pas une panne :

| Mesure | Valeur | Ce que disent les formules |
|---|---|---|
| Humeur | 1 346 variations, de −60 à +69 | normal : l'humeur répond à chaque lecture |
| Relations | ~9 400 variations | normal : chaque lecture touche la familiarité |
| Opinions | 400 variations, dérive moyenne Mercure −1,3, max 8,7, 11 avatars > 5 points | attendu (calcul ci-dessous) |
| FORCE / institutions / N.O.M | ±1,1 / ±0,5 / ±0,7 | aucun fait orienté sur ces axes n'a été cru |
| Bascules / doute | 0 / 1 | attendu : il faudrait 17 à 29 points d'élan |
| Faits crus | 1 seul (28 porteurs, crédence 23,5) | le goulot est en amont (extraction, création de faits) |

**Calcul pour un neutre type** (crédulité 0,3, ancrage 0,5, source inconnue c ≈ 0,35, menace 1) :
- prior de crédence = (5 + 40 × 0,3) × (0,3 + 0,7 × 0,35) ≈ **9** ; il ne déplace pas l'opinion (seule la variation compte) ;
- trois expositions convergentes font monter la crédence d'environ 15 à 20 points ;
- ΔO = Δc × k × (1 − ancrage) = 18 × 0,65 × 0,5 ≈ **5,9 points** sur Mercure, ce qui correspond aux 11 avatars à plus de 5 points ;
- sur 105 avatars dont 28 porteurs, la moyenne tombe à ≈ −1,3. C'est exactement ce qui est mesuré.

Un accord d'opinion pure avec un inconnu vaut s × 8 × k × c × (1 − ancrage) = 8 × 1 × 0,35 × 0,5 ≈ **1,4 point**. Il en faudrait une douzaine sur un même axe pour atteindre le seuil d'un neutre.

**Trois conclusions** :
1. Le moteur est calibré pour **une semaine** : c'est l'esprit des avis n°3 et n°4, qui visaient « une bascule de crédule en 36 h, dans un cas-limite ». Pour un exercice de quelques jours où l'animation veut **montrer** l'effet des joueurs, ce calibrage est trop lent. Le coefficient de persuasion est donc justifié.
2. **Un coefficient multiplie ce qui existe.** Deux fois zéro, ça reste zéro. FORCE, institutions et N.O.M sont immobiles parce que **rien d'orienté sur ces axes n'a été cru**, pas parce que les gains sont faibles. Le coefficient ne remplace pas une meilleure extraction (§C2).
3. **Un écart de 5 à 9 points ne se voit pas dans les textes.** `decrirePosition` ne change de libellé qu'à −60, −20, +20 et +60. Un avatar qui passe de −10 à −18 reste « partagé » dans son invite et écrit donc la même chose. Sans un levier de visibilité, même un coefficient de 2 restera invisible pour les joueurs (§A6).

---

## A. Le coefficient de persuasion `p`

### A1. Principe

`p` règle la **réceptivité** de la population, c'est-à-dire la facilité avec laquelle une lecture déplace une croyance ou une opinion. Il ne règle **pas** la quantité de lectures : c'est le rôle du coefficient de crise.

Il préserve les quatre garanties de la doctrine :
- **mise à jour pondérée** : le déplacement reste proportionnel à la confiance et à (1 − ancrage), et un ancré reste toujours plus lent qu'un crédule ;
- **confiance bornée** : on ne bouge toujours pas vers une position trop éloignée ;
- **effet plafond** : les extrêmes se renforcent toujours plus lentement ;
- **hystérésis** : il faut toujours un élan accumulé et une phase de doute avant de basculer.

Règle de construction : **chaque voie d'influence est multipliée au total par `p`, une seule fois**. Une voie à deux étages (croyance, puis opinion) reçoit donc √p à chaque étage, sinon elle serait amplifiée p^1,5 fois.

### A2. Sur quels termes il agit

| Terme (code) | Effet de `p` | Forme | Raison |
|---|---|---|---|
| **Accord d'opinion** (`opinionner`, l. 541 : s·8·k·c·(1−anc)·fs·fg) | **oui** | **× p** | voie directe, un seul étage |
| **Poids d'une croyance** (`croire`, l. 443 ; plafond 0,9 conservé) | **oui** | **× √p** | 1er étage de la voie « fait » ; plafond 0,9 inchangé |
| **Bonus de répétition** (l. 446) | **oui** | **× √p** | fait partie du 1er étage |
| **Démenti** (l. 451 : 0,8·c·…) | **oui** | **× √p**, facteur plafonné à 0,95 | symétrie obligatoire : un `p` qui amplifie la rumeur sans amplifier le démenti fausserait l'exercice contre les joueurs bleus |
| **Croyance → opinion** (l. 473 : o·Δc·k·(1−anc)) | **oui** | **× √p** | 2e étage de la voie « fait » ; total √p × √p = p |
| **Fait d'absence périmé** (l. 404) | **oui** | **× √p** | c'est un démenti (avis n°4 D2), il suit la même règle |
| **Plafond journalier** (`plafondJour` = 6 + 14·(1−anc)) | **oui** | **× √p** | sinon le plafond absorbe l'amplification chez les crédules ; √p et non p pour qu'il reste un frein |
| **Seuil de bascule** (10 + 25·anc) et doute à 0,4 × seuil | **non** | × 1 | l'élan grandit déjà p fois plus vite ; baisser aussi le seuil donnerait p^1,5 et ferait sauter l'hystérésis, qui est le garant de la crédibilité |
| **Inertie au retour** (avis n°4 D1) | **non** | × 1 | elle dépend du temps écoulé et de l'engagement, pas de la réceptivité |
| **Raidissement au rejet** (l. 545 : −s·1,5·k·anc, ±4/jour) | **non au-dessus de 1** | **× min(1, p)** | le retour de flamme est faible et rare dans la littérature *(Wood & Porter 2019 ; Swire-Thompson et al. 2020 — à sourcer)* ; l'amplifier produirait des contre-effets que l'animation ne veut pas montrer ; il baisse avec une population sceptique |
| **Engagement par un #** (±2, plafond 6/jour, l. 839) | **non** | × 1 | reprendre un # est un acte d'affichage, pas une persuasion (avis n°8) |
| **Prior d'une croyance nouvelle** (l. 394) | **non** | × 1 | le point de départ reste lié à la crédulité et à la source ; seul le mouvement est amplifié |
| **Humeur, relations, confiance** | **non** | × 1 | hors sujet : elles bougent déjà beaucoup (1 346 et 9 400 variations) |

**Recommandation : un `p` atténué pour les sources IA citoyennes.** L'animation veut voir l'effet **des joueurs**. Or, d'après OASIS (§3.7), le risque de troupeau vient des échanges **d'IA à IA**. Je recommande donc :
- **p plein** quand la source (auteur de la publication, ou auteur d'origine pour un partage) est un **compte humain** (joueur ou animation) ou un **relais** (`config.lignes`, qui porte la campagne adverse que les joueurs doivent contrer) ;
- **p_IA = √p** quand la source est un **citoyen IA**.

À p = 2, un joueur pèse donc 2 fois plus qu'aujourd'hui, et un citoyen IA 1,41 fois plus. La population **reste** influençable par elle-même, mais l'effet des joueurs se détache. Le pont connaît déjà les comptes IA (`synthese-opinions.ts` les distingue de la même façon). Si l'implémentation est trop lourde, on peut faire sans dans un premier temps : c'est le garde-fou A4 qui tient alors seul le troupeau.

### A3. Bornes, pas, valeur par défaut

- **Bornes : 0,5 à 3,0.**
  - En dessous de 0,5, la population devient imperméable : aucun usage en exercice.
  - Au-dessus de 3, même avec les garde-fous, des neutres basculeraient sur un seul fait cru, ce qui n'est plus crédible.
- **Pas : 0,25.**
- **Défaut : 1,0**, soit exactement le comportement actuel. Test de non-régression : à p = 1, l'état produit doit être identique octet pour octet.
- **Confirmation à l'écran** au-dessus de 2,0, comme pour le coefficient de crise.
- **Effet** : au cycle suivant, sans effet rétroactif. Baisser `p` n'annule rien de ce qui a bougé : on ne désapprend pas (règle de l'avis n°16).
- **Historique** : qui, quand, de combien à combien. Le motif de chaque variation d'opinion porte `persuasion ×p` (ou `×√p`) pour que le débriefing puisse expliquer chaque chiffre (règle L1-8).

### A4. Interaction avec le coefficient de crise

- Les deux coefficients sont **indépendants** et réglés séparément. La crise règle le **volume** (lectures, messages par heure) et `p` règle la **réceptivité** par lecture. Psychologiquement, ce sont deux choses distinctes : l'activation, et la persuasibilité.
  - La menace élève déjà la persuasibilité *dans* la formule (k = 0,35 + 0,30·menace ; anxiété dans le poids des croyances). Il ne faut donc pas indexer `p` sur la crise.
- **Mais ils se cumulent dans les faits** : le flux d'influence est à peu près proportionnel à crise × p. L'écran doit afficher ce produit :
  - « Flux d'influence ≈ crise × persuasion = 3,2 » ;
  - confirmation si le produit dépasse **4** ;
  - avertissement en orange au-dessus de **3**.

### A5. Garde-fous de crédibilité (actifs pour tout p ≥ 1, et indispensables au-dessus de 1,5)

1. **Les ancrés restent toujours plus lents** : c'est garanti par construction, car tous les facteurs sont multiplicatifs avec (1 − ancrage) et le plafond garde sa forme 6 + 14·(1 − ancrage). Il faut le vérifier par un test unitaire : pour tout p, le déplacement d'un avatar d'ancrage 0,75 est inférieur à celui d'un avatar d'ancrage 0,3 dans la même situation.
2. **Pas de bascule sans une vraie phase de doute** : une bascule exige **une phase de doute d'au moins 2 h** (le temps passé depuis `b.doute = true`), quel que soit `p`.
   - Avant ces 2 h, l'élan qui dépasse le seuil est conservé (comme `b.retenu`) et la position reste à ±1.
   - Cela empêche la bascule en un cycle et rend la phase de doute **visible** (l'avatar « pose des questions » pendant au moins 2 h).
3. **Pas de bascule sur une source unique** : l'élan qui mène à une bascule doit venir d'**au moins 2 sources distinctes** (auteurs ou faits). C'est la version minimale de la règle de l'avis n°2 (« ≥ 3 sources convergentes dont une crue »). On garde une liste `b.sources` (identifiants) remise à zéro avec l'élan.
4. **Pas de bascule en masse** : sur un même axe, **5 % de la population au plus bascule par heure glissante** (5 avatars sur 105, et 2 au minimum). Les avatars suivants restent en doute, avec leur élan conservé, jusqu'à l'heure suivante. Le journal l'indique : « bascule différée (plafond de population) ».
5. **Alerte de dérive** (règle OASIS, §3.7, adaptée à quelques jours) : la Console signale un axe dont la dérive moyenne dépasse **5 points en 6 h**, ou dont plus de **10 % des avatars** entrent en doute dans la même heure. C'est une alerte, pas un blocage : c'est peut-être l'effet recherché, mais l'animation doit le savoir.
6. **Rien ne change pour les relais** : un relais est en campagne, ses opinions sont tenues par sa fiche. Si le moteur fait déjà bouger les opinions des relais, `p` ne doit pas s'y appliquer (à vérifier par PLEIADE).

### A6. Le levier de visibilité (indépendant de `p`, à faire en premier)

Le constat montre des déplacements réels mais **muets**. Je propose une ligne de **tendance** dans l'invite (`decrirePositions`) :
- quand l'écart depuis la position de départ dépasse 5 points sur 48 h, sans doute ni bascule, ajouter : « ces derniers jours, ce que tu lis te rend **plus méfiant envers** Mercure (tu ne le dirais pas encore franchement) » ou « … **plus indulgent envers** … » ;
- la formulation est tirée du signe et de l'axe, sans chiffre ;
- elle apparaît au plus pour 2 axes à la fois, ceux qui ont le plus bougé.

C'est une nuance de ton, pas un changement de camp. Elle laisse la relecture (Q3, opinion et lexique) inchangée. Elle rend visible un déplacement de 5 à 15 points, c'est-à-dire tout ce que `p` entre 1,5 et 2 va produire. Sans elle, le coefficient ne servira qu'au tableau de débriefing.

### A7. Ce que l'écran doit dire (une phrase par palier)

Réglette de 0,5 à 3 par pas de 0,25. L'étiquette suit la valeur, et la phrase s'affiche sous la réglette. Les plafonds sont donnés pour un crédule (ancrage 0,3) et pour un ancré (ancrage 0,75).

| Palier | Étiquette | Phrase affichée |
|---|---|---|
| 0,5 – 0,75 | **sceptique** | « Population sceptique : les opinions bougent environ deux fois moins qu'au réglage de référence, et les rumeurs s'installent lentement. Plafond par jour : 11 points pour un crédule, 7 pour un ancré. » |
| 1,0 | **référence** | « Comportement de référence (calibré pour une semaine) : un fait relayé par les joueurs déplace la population de 1 à 2 points en moyenne en 6 h, et une bascule demande plusieurs jours. » |
| 1,25 – 1,5 | **réceptive** | « Population réceptive : effets environ 1,5 fois plus forts ; les crédules exposés plusieurs fois commencent à douter dans la journée. Plafond par jour : 19 / 12 points. » |
| 1,75 – 2,0 | **impressionnable** | « Population impressionnable : effets doublés pour les messages des joueurs (×1,4 entre avatars). Une campagne soutenue fait douter des neutres en quelques heures ; premières bascules de crédules en 1 à 2 jours. Plafond par jour : 22 / 13 points. » |
| 2,25 – 3,0 | **démonstration** | « Réglage de démonstration : effets jusqu'à 3 fois plus forts, bascules possibles en une demi-journée. Risque d'effet de troupeau. À réserver à une séquence courte et à surveiller. Plafond par jour : 27 / 16 points. » |

Sous la réglette : « Ne change que la réceptivité. Le nombre de messages dépend du coefficient de crise. Flux d'influence ≈ crise × persuasion = X. Les ancrés restent toujours plus lents que les crédules. Rien n'est rétroactif. »

### A8. Valeur de départ pour la suite de DELATTRE 26

**Je recommande p = 2,0**, avec p_IA = √2 ≈ 1,41 pour les citoyens IA, le levier A6 et les garde-fous A5.2 à A5.4 en place.

Projection, à volume de faits comparable, sur 6 h :

| Mesure (axe Mercure) | Constat à p = 1 | Attendu à p = 2 |
|---|---|---|
| Dérive moyenne | −1,3 | −2,5 à −3,5 (plus de porteurs franchissent le seuil de crédence) |
| Avatars à plus de 5 points | 11 | 25 à 35 |
| Écart maximal | 8,7 | 15 à 18 (plafond d'un crédule : 22) |
| Avatars en doute | 1 | 5 à 12 (neutres proches de zéro) |
| Bascules | 0 | 0 à 3 dans la journée, aucune parmi les ancrés (≥ 0,7) |

**Relecture à H+3 après le changement** :
- moins de 15 % des avatars exposés ont bougé de plus de 5 points → passer à **2,5** ;
- une bascule chez un avatar d'ancrage ≥ 0,7, plus de 10 % d'avatars en doute en une heure, ou une alerte de dérive sans inject majeur → redescendre à **1,5** ;
- FORCE, institutions et N.O.M toujours immobiles → ce n'est **pas** `p` qu'il faut monter, c'est l'extraction qu'il faut regarder (§C2).

---

## B. Axes d'opinion éditables

### B1. Les champs d'un axe

Le registre est stocké dans les réglages de l'app-ia (comme `campagnes`) et relu à chaque cycle.

| Champ | Contrainte | Rôle |
|---|---|---|
| `cle` | ASCII, 2 à 24 caractères, **immuable** | identifiant dans l'état (`opinions`, `bascules`, `orientation` des croyances, `campagnes`, journal) |
| `libelle` | ≤ 40 caractères | ce qu'affichent les écrans et l'invite (« tu soutiens fermement *la FORCE* ») |
| `description` | ≤ 200 caractères | ce qu'est l'axe pour le **modèle**, dans l'extraction et dans le contrôle d'orientation : qui ou quoi, et ce qui n'en fait pas partie (« les institutions = préfecture, mairie, autorités civiles ; pas l'armée ») |
| `pole_plus` | ≤ 60 caractères | ce que veut dire +100 (« soutient l'accueil des réfugiés ») |
| `pole_moins` | ≤ 60 caractères | ce que veut dire −100 (« veut fermer la région aux réfugiés ») |
| `pivot` | booléen, **réservé à FORCE et Mercure** en v1 | l'axe sert à `bloc()`, à la voix de cohorte, au sens par défaut d'un #, au contrôle d'orientation nocturne |
| `statut` | `actif` / `archive` | voir B4 |
| `version` | entier, +1 à chaque changement de description ou de pôles | inscrit dans le journal des variations, pour le débriefing |
| `init` | recette de position initiale (B2) | conservée pour la traçabilité, rejouable à l'identique |
| `indices` | facultatif, 10 mots au plus | complète l'expression `colore` de `pont.mjs` l. 418 (aujourd'hui FORCE, Mercure, N.O.M, OTAN… en dur) |
| `cree_par`, `cree_le`, `maj_par`, `maj_le` | — | historique, comme pour la crise |

Le registre de départ reprend **les 4 axes actuels avec leur libellé actuel** (FORCE et Mercure en pivot). Le comportement doit rester identique : c'est le test de non-régression de l'étape 3.

### B2. Position initiale d'un avatar sur un nouvel axe

| Méthode | Verdict | Raison |
|---|---|---|
| 0 pour tous | **non** | personne n'est exactement à 0 ; à 0, `Math.sign` vaut 0 et l'hystérésis ne joue plus (l. 505) : le premier message ferait « basculer » sans doute ni élan |
| Selon le tempérament seul | **non** | le tempérament dit **à quel point** on tient à une position (extrémité, ancrage), pas **laquelle** |
| Estimée par le modèle depuis la fiche | **non par défaut** | 105 appels, un résultat non reproductible, et un risque de stéréotype (« agricultrice donc contre ») que personne ne relit ; à la rigueur plus tard, comme *suggestion* que l'opérateur valide |
| **Demandée à l'opérateur par groupe eho, étirée par l'ancrage, avec un peu de bruit** | **oui, méthode recommandée** | simple, crédible, traçable, reproductible, et c'est l'animation qui sait ce que pense chaque cohorte de la scénarisation |
| Dérivée d'un axe existant | **oui, en option** | utile quand le nouvel axe est corrélé à un axe connu (ex. « OTAN » ≈ N.O.M inversé) |

**Méthode recommandée (une formule, déterministe)** :
1. L'opérateur donne un **centre** (de −100 à +100) pour chaque groupe eho (IA ARN · PRO-MERCURE, PRO-ARNLAND, NEUTRE, relais par camp…). Le défaut est 0, et l'écran propose les groupes existants.
2. Pour chaque avatar : **v = centre × (0,6 + 0,8 × ancrage) + bruit**, avec un bruit uniforme de **−8 à +8**, borné à ±95.
   - Un ancré est plus près du pôle de son groupe (×1,2 à ancrage 0,75), un crédule plus près du centre (×0,84 à 0,3) : c'est l'extrémité qui dépend du tempérament, pas la direction.
   - Si |v| < 3, on prend v = ±3 (le signe du centre, ou celui du bruit si le centre vaut 0) pour que l'hystérésis ait un sens.
3. Le bruit est **tiré d'une graine** égale au hachage de `cle_axe + id de l'avatar` : relancer donne le même résultat, et l'opération est idempotente.
4. **Option « dérivé »** : v = a × opinion(axe source) + b, avec a entre −1 et 1, puis le même bruit. Exemple : « OTAN » = −0,7 × N.O.M.
5. **Aperçu obligatoire avant validation** : histogramme par groupe, moyenne, et les 5 avatars les plus extrêmes. Ensuite seulement, on écrit.
6. **Écriture** : pour chaque avatar, `m.opinions[cle] = v` et `m.bascules[cle] = { depart: v, elan: 0, doute: false, bascule: null }`, plus une ligne de journal « axe créé : position initiale v (groupe X, centre C) ». Un avatar ajouté plus tard reçoit sa valeur selon la même recette, au chargement. Une valeur individuelle posée dans la fiche eho (`opinions_initiales[cle]`) l'emporte toujours.
7. **Pas d'effet rétroactif** : les faits déjà crus n'ont pas d'orientation sur le nouvel axe, et on ne relance pas l'extraction sur le passé. L'axe vit à partir de sa création. Il faut le dire à l'écran.

### B3. Renommer, modifier la description

| Opération | Ce qui change dans l'état | Règle |
|---|---|---|
| **Changer le libellé** | rien (la clé est immuable) | libre ; le journal garde la clé, les écrans affichent le nouveau libellé |
| **Préciser la description sans changer de référent** (« mieux dit ») | rien ; `version` +1 | l'extraction l'utilise au cycle suivant ; le journal porte la version, pour expliquer un changement de comportement de l'extraction au débriefing |
| **Changer le référent** (« institutions » devient « la préfecture seulement ») ou **inverser les pôles** | — | **interdit en modification**. L'écran demande : « Est-ce la même chose, mieux dite, ou autre chose ? ». Si c'est autre chose, on **crée un nouvel axe** (B2) et on archive l'ancien (B4). Inverser les pôles demanderait de retourner les opinions, les élans, les orientations des croyances et les campagnes : la source d'erreur est trop grande pour un gain nul |
| **Changer `pivot`** | — | non modifiable en v1 |

### B4. Supprimer = archiver (jamais détruire en cours d'exercice)

Archiver un axe :
- **ce qui est gelé** : l'opinion, les bascules et l'élan restent dans l'état avec leur dernière valeur. `deplacerOpinion` ignore un axe archivé : pas de mouvement, pas de journal ;
- **ce qui disparaît des invites** : la ligne de position, l'axe dans la consigne d'extraction (`nettoyerAxes` filtre les axes actifs), le contrôle d'orientation ;
- **croyances** : les entrées d'orientation sur cet axe restent dans chaque croyance, mais elles sont ignorées ;
- **campagnes #** : un poids sur un axe archivé est ignoré. L'écran des campagnes l'affiche en gris avec « axe archivé ». L'enregistrement d'une **nouvelle** campagne sur un axe archivé est refusé ;
- **débriefing** : `synthese-opinions` montre l'axe archivé, grisé, avec ses valeurs figées et la date d'archivage ;
- **restaurer** est possible : l'axe reprend là où il était gelé, sans rattrapage ;
- **purge définitive** seulement après la fin de l'exercice et un export de l'état.

**Verrous** :
- **FORCE et Mercure ne sont pas archivables** pendant l'exercice. Ils portent la voix de cohorte (`voixActive`, l. 853-854), le bloc affirmé / modéré / neutre (`bloc`, l. 731), le sens par défaut des # (l. 736) et le contrôle d'orientation nocturne (`memoire.mjs` l. 66). Leur libellé et leur description restent modifiables.
- institutions, N.O.M et tout axe créé sont archivables.

### B5. Nombre d'axes

- **6 axes actifs recommandés** (les 4 actuels et 2 de scénario), **8 au maximum** (blocage dur), sans compter les axes archivés.
- **Raisons** :
  - **fiabilité de l'extraction** : Gemma 26B, à température 0,2, doit choisir les axes « explicitement visés ». Au-delà de 6 libellés, les fausses attributions augmentent (l'avis n°9 en a déjà trouvé avec 4 axes) ;
  - **saillance** : tout ce qui est dans l'invite devient un sujet. 8 lignes « tu soutiens… » font parler politique des avatars qui parlaient de leur vie (voir §C3) ;
  - **réalisme** : une personne ordinaire a peu d'attitudes politiques saillantes en même temps *(à sourcer : Converse 1964 ; Zaller 1992)* ;
  - **lisibilité du débriefing**.

### B6. Ce qu'il faut rendre dynamique dans le code (inventaire)

| Endroit | Aujourd'hui | Demain |
|---|---|---|
| `esprit.mjs` l. 12 `AXES` | constante | registre (axes actifs), relu à chaque cycle |
| `esprit.mjs` l. 84-92 consigne d'extraction | axes et exemples en dur | liste générée : `cle` = description + pôles |
| `esprit.mjs` l. 93 `nettoyerAxes` | clés de la constante | axes actifs |
| `esprit.mjs` l. 59 `decrirePosition` | libellé de la constante | `libelle` |
| `esprit.mjs` l. 146-147 opinions initiales | fiche eho seule | fiche eho, puis recette d'axe pour les clés manquantes |
| `route.ts` l. 12 validation des campagnes | 4 axes en dur | axes actifs |
| `pont.mjs` l. 418 `colore` | expression en dur | plus les `indices` des axes actifs |
| `bloc`, `voixActive`, `sensHashtag`, `memoire.mjs` l. 66 | FORCE et Mercure en dur | **inchangés en v1** (axes pivots verrouillés) |
| `synthese-opinions.ts` | lit tous les axes de l'état | ajouter libellé, statut et version |

---

## C. Points de vigilance et ordre de mise en œuvre

### C1. Points de vigilance

1. **`p` amplifie aussi les erreurs.** Un fait fantôme (avis n°7) ou une orientation mal extraite est amplifié comme un vrai fait. Avant de passer à 2, il faut vérifier sur le relevé que les faits crus sont bien ceux des joueurs et de l'animation (champ `ne_de`).
2. **Le goulot de FORCE, institutions et N.O.M est l'extraction, pas le gain.** 400 variations d'opinion pour environ 9 400 de relation, et un seul fait cru : il faut contrôler au relevé combien de publications reçoivent une `orientation`. Si moins de 5 % des publications des joueurs en reçoivent une, c'est la consigne d'extraction qu'il faut revoir (exemples d'opinion implicite, « soutenir les soldats » = FORCE +1).
3. **La saillance des axes.** Afficher dans l'invite seulement les axes **pivots**, les axes où |opinion| ≥ 20, ceux qui ont bougé dans les dernières 24 h, ou ceux que vise la publication lue. Sinon, chaque axe ajouté devient un sujet de conversation, et le chœur politique remplace le chœur de la solidarité (avis n°18).
4. **Le troupeau (OASIS).** À p ≥ 2 sans p_IA atténué, une rumeur reprise par 10 citoyens IA s'auto-entretient. C'est l'argument principal pour p_IA = √p et pour le plafond de bascules par heure.
5. **Le démenti doit suivre.** Si l'animation monte `p` pendant une rumeur rouge, les démentis bleus sont amplifiés de la même façon : c'est voulu. L'entraîné doit voir que son démenti **pèse aussi plus**.
6. **Pas de rétroactivité ni de « désapprentissage »** : ni en baissant `p`, ni en archivant un axe, ni en changeant une description.
7. **Traçabilité** : chaque variation d'opinion porte `p`, la voie (accord / croyance / démenti) et la version de l'axe. Sans cela, le débriefing ne pourra pas dire « cet écart vient de votre message à 14 h 12, amplifié par le réglage de 15 h ».
8. **Les relais** ne sont pas concernés par `p` (A5.6).

### C2. Ordre de mise en œuvre

1. **Visibilité et traçabilité, sans `p`** : la ligne de tendance (A6) et le motif enrichi dans le journal. C'est environ 1 h de travail. On en juge l'effet sur les textes au relevé suivant, à p = 1.
2. **Coefficient de persuasion** :
   - réglage en base, `D.persuasion()` relu à chaque cycle, écran et historique (sur le modèle de la crise), indicateur crise × p ;
   - application aux 6 termes de A2 (× p, × √p, plafond × √p, raidissement × min(1, p)) ;
   - p_IA = √p pour les citoyens IA ;
   - tests : non-régression à p = 1 (état identique), et ordre crédule > ancré pour p ∈ {0,5 ; 1 ; 2 ; 3}.
3. **Garde-fous de bascule** (A5.2 à A5.5) : doute ≥ 2 h, 2 sources distinctes, 5 % de la population par heure, alerte de dérive. Ils doivent être **en ligne avant** de passer à p > 1,5.
4. **Passage à p = 2 sur DELATTRE 26**, puis relecture à H+3 avec les critères de A8.
5. **Registre des axes en lecture** : les 4 axes actuels migrés dans le registre, sans aucun changement de comportement (test de non-régression), et les 7 endroits de B6 rendus dynamiques.
6. **Édition du libellé et de la description** (avec `version`).
7. **Ajout d'un axe** : recette par groupe, aperçu, écriture idempotente, avatars ajoutés plus tard.
8. **Archivage et restauration**, avec les verrous pivots et le traitement des campagnes.
9. **Saillance des axes dans l'invite** (C1.3). À faire **avant** d'ajouter un 5e axe actif.

---

## Résumé des valeurs

| Élément | Valeur |
|---|---|
| `p` : bornes, pas, défaut | 0,5 à 3,0 · 0,25 · **1,0** (comportement actuel) ; confirmation au-dessus de 2,0 |
| Accord d'opinion | × p |
| Poids de croyance, répétition, démenti, croyance → opinion, fait périmé | × √p chacun (total p par voie ; démenti plafonné à 0,95) |
| Plafond journalier | × √p (crédule 15,8 → 22,3 à p = 2 ; ancré 9,5 → 13,4) |
| Seuil de bascule, doute, inertie au retour, # | inchangés |
| Raidissement | × min(1, p) |
| Sources citoyens IA | p_IA = √p |
| Crise et persuasion | indépendants ; afficher crise × p ; confirmation au-dessus de 4 |
| Garde-fous | doute ≥ 2 h avant bascule · ≥ 2 sources distinctes · ≤ 5 % de bascules par axe et par heure (2 au minimum) · alerte si dérive > 5 points en 6 h ou > 10 % en doute en 1 h |
| Valeur pour DELATTRE 26 | **2,0**, relecture à H+3 (2,5 si moins de 15 % ont bougé de plus de 5 points ; 1,5 si un ancré bascule) |
| Axes | 6 actifs recommandés, 8 au maximum ; clé immuable ; FORCE et Mercure non archivables |
| Position initiale | centre par groupe eho × (0,6 + 0,8 × ancrage) + bruit uniforme de ±8 à graine fixe ; |v| ≥ 3 ; aperçu avant écriture |
| Suppression | archivage (gel, retrait des invites, campagnes ignorées), restauration possible, purge après l'exercice |
