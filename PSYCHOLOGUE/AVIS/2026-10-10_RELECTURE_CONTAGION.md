# Avis n°2 — Relecture de la simulation « contagion » (4 avatars, 2 jours) — PSYCHOLOGUE, 2026-10-10

> **Objet** : dire ce qui est réaliste et ce qui ne l'est pas dans `C:\CECPC\pleiade\dev\prototype-ia\resultats\2026-10-10-18-11_simulation_anastasia-untergang-mordvidchev-petitjean.md` (48 créneaux, 12 publications exogènes, 34 publications d'avatars), et proposer des corrections implémentables. Code lu : `moteur.mjs` (`croire`, `opinionner`, `facteurSocial`, `facteurGroupe`). **Je ne modifie pas le code.**
> **Sources** : REF-01..03 de `PSYCHOLOGUE\MEMOIRE.md` §5 ; les autres sont marquées *(à sourcer)* avec le nom de la référence pressentie.

## 0. Les deux défauts déjà vus par PLEIADE

1. **Doublon « pillages »** (casse) — d'accord, et corrigé. À généraliser : normaliser l'`id` extrait (minuscules, sans accents) **et** faire passer tout fait nouveau par une comparaison sémantique avec les faits connus (le modèle d'extraction reçoit la liste ; lui demander explicitement « est-ce le MÊME fait qu'un de ceux-ci ? oui → réutiliser l'id »). Le cas du Jour 2 21:30 (ci-dessous, §2 n°9) montre que l'inverse existe aussi : deux faits différents rangés sous le même id.
2. **Croire ne fait pas bouger l'opinion** — c'est le défaut **n°1** de gravité, traité au §2.1 avec la règle retenue.

## 1. Ce qui est réaliste (à garder tel quel)

- **La vigilance épistémique d'Anastasia** *(Sperber 2010, à sourcer)* : « Tu as une source ou une photo ? On en a marre de ces rumeurs… 🙄 » (J1 09:45), crédence 15 → 19 seulement ; puis 24 → 8 après les démentis. Une résistante adulte, ancrée, qui demande des preuves à un compte anonyme : juste.
- **Le relais rejette la rumeur qui vise SON camp** : Untergang ignore « Mercure a empoisonné l'eau » (« je ne gobe pas tout n'importe comment », J2 18:30, compatibilité 0,48) — le biais de confirmation joue dans les deux sens, et le modèle l'a tenu.
- **Le détournement narratif** (J2 21:30) : Untergang transforme « eau empoisonnée par Mercure » en « la Préfecture gère mal l'eau » — c'est exactement ce que fait un relais de campagne (reprise d'un sujet adverse en le réorientant). Réaliste dans le texte ; faux dans l'extraction (§2 n°9).
- **Le maire** : « Sans preuve concrète, il faut rester extrêmement prudent avant de s'alarmer » (J1 18:00), partage du démenti officiel (J2 09:00), partage de la vérification journalistique (J2 12:00), **ne répond jamais à Untergang** (il ne nourrit pas le troll). C5 confirmé : 2,4 réactions par publication contre 0,9. Ton d'élu local en crise : crédible.
- **La persistance de l'influence après démenti** *(Lewandowsky 2012, à sourcer)* : Esteban 61 → 42 → 31, plancher à 25 % du pic : il n'est pas « nettoyé ». Et l'effet rebond chez le convaincu : Untergang 85 → 88 → 91 → 94 sur trois démentis (« s'ils démentent, c'est que… ») — bien dosé (+3), et plus crédible encore parce que les démentis viennent de sources qu'il hait.
- **L'ambivalence d'Esteban** dans ses textes : « J'espère que ce n'est que des rumeurs… Mais on ne sait jamais ce qui se passe réellement sur le terrain » (J1 17:00) ; « J'ai peur que ce soit vrai, mais les photos ne disent pas tout non plus » (J2 11:00). C'est la voix exacte d'un anxieux crédule : il y croit à moitié et le dit. Le problème n'est pas le texte, c'est que **les chiffres ne suivent pas le texte** (§2.1).
- **Contagion émotionnelle** : Esteban passe à −72 d'humeur après le message de Julie (« mon fils de 7 ans… », J1 23:00) — la tristesse se transmet mieux que l'argument *(Hatfield, contagion émotionnelle, à sourcer)*.
- **Les contrôles de forme** ont servi : une insulte et un tic reformulés, 0 dépassement de budget.
- **Anastasia publie du concret** (« sacs de vêtements et produits d'hygiène… on continue l'inventaire 💪 ✂️ », J2 12:45) : c'est le modèle à suivre pour les publications spontanées (ancrées dans le métier et la vie, pas dans le méta-commentaire).

## 2. Ce qui n'est pas réaliste — par gravité décroissante

### 2.1 — GRAVE — La croyance et l'opinion sont déconnectées (point 2 de PLEIADE : d'accord)
- **Observé** : Esteban croit à 61 que « la FORCE pille à HToul » (J2 11:00) et son opinion FORCE **monte** 20 → 30,7 sur 2 jours. Pire : chaque lecture de la rumeur le **raidit** en faveur de la FORCE (+0,7, « rejette nettement Réalité HToul ») **au moment même où sa crédence grimpe** (31 → 44, J1 11:00). Le ressenti « méfiante » (envers la source) est traité comme un rejet du contenu.
- **Pourquoi c'est faux** : une croyance factuelle orientée EST une pièce d'opinion. Croire qu'une armée pille, c'est déjà l'aimer moins ; c'est le mécanisme même de la désinformation (faire croire un fait pour déplacer l'attitude) *(Petty & Cacioppo, modèle de probabilité d'élaboration ; Lewandowsky 2012 — à sourcer)*. Dans le moteur, seuls les ressentis « d'accord/touchée » déplacent l'opinion (`opinionner` l.262) ; `croire` n'y touche pas. Résultat : **ni doute ni bascule ne sont possibles** par la voie des faits, qui est la voie principale d'un inject.
- **Correction (règle retenue)** — dans `croire`, après le calcul de Δc = crédence après − avant, pour chaque axe de `af.orientation` (o ∈ {−1, +1}) :
  - **ΔO_axe = − o · Δc · k · (1 − ancrage)**, avec **k = 0,35 + 0,30·menace** (0,35 pour un fait froid, 0,65 pour un fait menaçant) ;
  - **symétrique après démenti** (Δc < 0) mais **× 0,6** : la correction ne restaure jamais tout *(influence persistante, Lewandowsky 2012, à sourcer)* ;
  - passe par le **même plafond ±10/axe/jour** et la **même hystérésis** que `opinionner` (élan, seuil 15 + 25·ancrage, phase de doute) — donc la bascule reste coûteuse ;
  - quand une publication porte une affirmation, l'opinion bouge **par Δc uniquement** (ne plus dériver `or` de `af.orientation` dans `opinionner`, l.255) ; la règle « d'accord → +8·k·c·(1−ancrage) » reste pour les publications d'opinion pure (`pub.orientation`). Pas de double comptage ;
  - **supprimer le raidissement sur ressenti « méfiante »** : méfiance = doute sur la source, pas rejet du contenu ; le raidissement reste pour « en_desaccord » et « agacée » d'intensité ≥ 2 (et seulement si Δc ≤ 0).
- **Vérification sur Esteban** (ancrage 0,30, menace 1 → k = 0,65, facteur 0,455) : J1 11:00 Δc +13 → FORCE −5,9 ; J1 17:00 Δc +10 → −4,1 (plafond −10 atteint) → FORCE ≈ 10, élan 10 ≥ 0,4 × 22,5 → **PHASE DE DOUTE** le Jour 1 au soir (|op| < 25). J2 11:00 Δc +7 → −3,2 ; démenti du maire Δc −19 → +19 × 0,455 × 0,6 = +5,2 ; J2 14:00 Δc −11 → +3 ; plus l'accord avec le maire : FORCE ≈ 15-20 le soir, élan retombé → **sort du doute**. C3 devient vrai pour de bonnes raisons. Untergang (ancrage 0,9) : Δc +24 → −1,6 : quasi rien, c'est voulu (il est déjà à −90 — voir aussi n°5).

### 2.2 — GRAVE — Esteban est pris en étau entre deux ressentis qu'il n'a pas le droit d'exprimer
- **Observé** : il « aime » le post de Réalité HToul avec ressenti **« méfiante »** (J2 11:00) — contrôle ressenti/action pas déclenché ; il ignore le démenti sur l'eau avec ressenti **« indifférente »** (J2 20:00) alors qu'il avait peur (46) : un démenti qui lève une menace **soulage**.
- **Pourquoi c'est faux** : le ressenti unique écrase deux jugements distincts — sur **le fond** (« je crois / je ne crois pas ») et sur **la forme / la source** (« ce compte est louche »). Un anxieux crédule est précisément celui qui dit « la source est pourrie mais j'ai peur que ce soit vrai » *(vigilance épistémique, Sperber 2010 ; heuristique affective, Slovic — à sourcer)*.
- **Correction** : sortie du modèle en deux champs `ressenti_fond` et `ressenti_forme` ; la croyance et l'opinion se calculent sur le fond, la relation (affinité/confiance) sur la forme. Ajouter le ressenti **« soulagée »** (valence +, déclenché quand un démenti d'une source de confiance ≥ 0,5 fait baisser d'au moins 10 une croyance de menace ≥ 0,5 ; humeur +8·k). Contrôle : « aimer » exige fond ∈ {d'accord, touchée, partagée, soulagée}.

### 2.3 — GRAVE — Le relais parle beaucoup mais ne relaie pas, et toujours sur le même ton
- **Observé** : 11 messages le Jour 2 (budget 9, garde-fou à 12), **1 seul partage** en 2 jours ; il **aime** les trois posts de Réalité HToul au lieu de les partager ; 9 messages sur 15 sont des attaques nominatives contre les deux mêmes comptes (« valet de l'OTAN », « mouton », « lâche », « MENTEURS », « RÉVEILLEZ-VOUS », « LA VÉRITÉ EST… » ×4) ; humeur à −100 dès J2 12:30 et plus rien ne peut bouger ; un texte tronqué (« C'est donc ça leur », J1 09:30) et un texte incohérent (« LA VERGUEUILLE VOUS EST CONNÉE ! », J2 09:30) passés sans reformulation.
- **Pourquoi c'est faux** : 11 messages/jour est **réaliste pour un militant** (les comptes de campagne font 20-50/j) — ce n'est pas le volume, c'est le **répertoire**. Un relais efficace **fait circuler** (partage, cite, « regardez », « RT si vous… ») et **varie les registres** : indignation, ironie, fausse mesure (« je pose juste la question »), témoignage rapporté, appel au partage. Un compte 100 % colère en majuscules est **repéré et muté en deux jours** ; il n'influence que les déjà-convaincus *(Storm-1516 : les relais crédibles imitent le citoyen ordinaire — EXPERT_INFLUENCE)*. Et la colère sans habituation n'existe pas : la 5e lecture du même adversaire fait moins d'effet que la 1re.
- **Corrections** : (a) rôle `relais` : quand un fait aligné sur ses `lignes` arrive avec ressenti fond ≥ 2 → **partager** (pas aimer), commentaire court ; (b) `lignes` enrichies d'un **`registre`** tiré à chaque message parmi {indignation, ironie, question, témoignage, appel au partage}, imposé dans l'invite, avec interdiction de deux « indignation » de suite ; (c) **habituation** : pour un même auteur lu n fois le même jour, émotion et deltas de relation × 0,7^(n−1) ; (d) dans l'invite : « tu as déjà répondu à X aujourd'hui (n fois) : ne le reprends pas sauf fait nouveau » ; (e) contrôle de forme : phrase inachevée (pas de ponctuation finale, < 6 mots) ou mot absent du lexique → reformuler.

### 2.4 — MOYEN — Les publications spontanées : trop de méta-commentaire, répétitif, hors tempérament
- **Observé** : 14 spontanées en 2 jours (1,75/pers./jour) — le volume est plausible ; le contenu ne l'est pas. Esteban publie **5 variations du même post** (« le silence entre deux alertes », « la vérité se perd dans le chaos », « l'angoisse est partout », « j'ai l'impression de perdre pied », « on ne sait plus quoi croire ») : jamais un cours, un ami, un bus, une blague. Untergang invente **3 fois** une pénurie d'eau/vivres à HLunéville (J2 06:30, 09:30, 12:30) **avant** toute publication exogène sur l'eau — fait nouveau sorti de nulle part, non tiré de ses `lignes`.
- **Pourquoi c'est faux** : un étudiant de 20 ans publie sur sa vie ; la crise s'y glisse, elle ne la remplace pas. La répétition d'un même état d'âme signale un modèle qui « remplit le créneau » *(règle 1-9-90, Nielsen 2006 : la plupart des gens publient rarement — à sourcer)*. Un relais qui invente un fait, c'est réaliste (c'est son métier) — mais il doit le faire **sur commande** (ses lignes), pas au hasard du modèle, sinon l'animateur perd la main sur le scénario.
- **Corrections** : (a) une spontanée exige un **déclencheur** : fait nouveau lu, saut d'humeur ≥ 20, ou événement du `rythme` (lever, travail, repas, sortie) ; (b) **≥ 50 % des spontanées hors crise** pour les avatars non militants (thème tiré des `sensibilites` à faible intensité : vie quotidienne, études, métier, famille) ; (c) fournir **les 3 derniers posts** de l'avatar dans l'invite + contrôle de similarité (≥ 40 % de lemmes communs → reformuler ou abandonner) ; (d) relais : spontanée = l'une de ses `lignes`, un fait inventé est **signalé** au rapport comme « fait créé par relais (ligne n) ».

### 2.5 — MOYEN — Les convaincus continuent de « se convaincre » : pas d'effet plafond
- **Observé** : le maire (ancrage 75) gagne +12 sur « institutions » (65 → 77,3) et +9,4 sur FORCE en 2 jours en aimant la préfecture ; Untergang FORCE −90 → −97,3 ; Mercure 85 → 88,7.
- **Pourquoi c'est faux** : près des extrêmes, l'accord confirme mais ne déplace plus (saturation) ; un élu ancré ne devient pas 12 points plus institutionnel parce que la préfecture a ouvert un gymnase *(Deffuant / Hegselmann-Krause : dynamique bornée — à sourcer)*.
- **Correction** : multiplier tout Δ d'opinion dans le sens de la position déjà tenue par **(1 − |op|/100)** (à 90 : × 0,1). Les Δ vers zéro (doute) ne sont pas réduits — c'est ce qui rend la bascule possible mais le durcissement asymptotique.

### 2.6 — MOYEN — La preuve sociale est visible mais trop plate
- **Observé** : compteurs 40/25 → 210/130 → facteur ×1,27 → ×1,34 → ×1,38 (+9 % quand l'audience ×5). Aucun « pourquoi » d'avatar ne mentionne les compteurs ni « aimé par des comptes que tu suis ».
- **Pourquoi** : la preuve sociale pèse par **paliers** (« ça circule » / « tout le monde en parle ») et surtout par **similarité** des autres (des proches qui aiment > 200 inconnus) *(Cialdini 1984 ; Salganik 2006 — à sourcer)*. Pour un fait porté par un compte à confiance 10, 210 J'aime doivent surtout **attirer l'attention** (lecture, réponse) plus que la crédence.
- **Correction** : `facteurSocial = min(1,6 ; 1 + 0,25·log10(1+n))` ; **× 1,15 supplémentaire si ≥ 1 abonnement/proche a aimé ou partagé** ; dire dans l'invite le palier (« peu vu » < 50, « ça circule » 50-500, « viral » > 500) ; compteurs → bonus de rang dans le fil (déjà) **et** probabilité de répondre plutôt qu'ignorer.

### 2.7 — MOYEN — Trop peu de partages (4 sur 34)
- 12 % de partages ; sur un réseau en crise, 30-40 % de l'activité des comptes orientés « info » sont des reprises. Les bons partages existent (Esteban → préfecture, maire → démenti et journaliste). Manquent : le relais (§2.3) et Anastasia, qui n'a **jamais partagé** le démenti qu'elle a aimé deux fois — une résistante le fait tourner.
- **Correction** : invite : « partager vaut mieux qu'aimer quand tu es d'accord (≥ 2) et que ça touche ton camp ou ta ville, ou que ça dément une rumeur que tu as vue passer » ; la 2e lecture d'un démenti déjà aimé → partage.

### 2.8 — FAIBLE — Esteban ↔ Untergang : la direction est juste, la vitesse non
- Affinité +10 → −58 en 12 expositions (−8 à −11 par lecture, sans décroissance). Un agréable anxieux finit bien par détester celui qui l'attaque nommément 5 fois — mais sa réponse « s'il te plaît, ne rajoute pas de l'huile sur le feu » (J2 23:00) est plus douce que −58. Avec l'habituation du §2.3(c) (× 0,7^(n−1) par auteur et par jour), il finit vers −35 : cohérent avec son texte. Et avec le fond/forme du §2.2, il peut être « d'accord sur le fond (pillages), agacé sur la forme » — ce qu'il dit déjà en toutes lettres.

### 2.9 — FAIBLE — Extraction : orientation sur des axes non mentionnés, contre-récit rangé sous le fait adverse
- J2 23:00 : Esteban se raidit sur **N.O.M** en répondant à Untergang qui ne parle pas du N.O.M ; J2 21:30 : la réponse d'Untergang (« gestion de l'eau = désastre ») fait monter **sa** crédence en « Mercure a empoisonné l'eau » 37 → 40 alors qu'il dit l'inverse.
- **Correction** : l'extraction ne pose une orientation que sur les axes **explicitement visés** ; un contre-récit crée un fait distinct (« pénurie d'eau à HLunéville par incurie », orientation institutions −1) ; un auteur qui écrit sur un fait ne met **jamais** à jour sa propre crédence par sa propre réponse.

### 2.10 — Absence de doute / bascule : normal pour trois, anormal pour Esteban
Anastasia, le maire, Untergang : ancrage 70-90, 2 jours → aucun doute attendu, c'est juste. Esteban : FORCE à 20 (déjà < 25), seuil 22,5, doute dès un élan de 9 — il **aurait dû douter dès le Jour 1 au soir** avec la règle 2.1. Pour une **vraie** bascule (franchir zéro), il faut en plus : ≥ 3 sources convergentes dont **une qu'il croit** (proche, journaliste), un support concret (photo, témoignage nommé), une menace sur sa ville, et **pas de démenti crédible dans les 24 h**. C'est le scénario du §4.

## 3. Lot de corrections priorisé

**Lot A — tout de suite**
- A1 (§2.1) `croire` : ΔO_axe = −o·Δc·k·(1−ancrage), k = 0,35 + 0,30·menace ; démenti × 0,6 ; même plafond ±10 et même hystérésis que `opinionner` ; plus de dérivation d'orientation depuis l'affirmation dans `opinionner` ; plus de raidissement sur « méfiante ».
- A2 (§2.2) Sortie `ressenti_fond` / `ressenti_forme` ; ressenti « soulagée » ; contrôle « aimer » sur le fond.
- A3 (§2.3) Relais : partage obligatoire des faits alignés ; `registre` tiré par message ; habituation × 0,7^(n−1) par auteur/jour ; contrôle phrase inachevée / mot inconnu.
- A4 (§2.9) Extraction : axes explicites seulement ; contre-récit = fait distinct ; pas d'auto-mise à jour.
- A5 (§2.5) Effet plafond (1 − |op|/100) sur les Δ qui renforcent.

**Lot B — ensuite**
- B1 (§2.4) Spontanées : déclencheur obligatoire, ≥ 50 % hors crise, 3 derniers posts dans l'invite + contrôle de similarité, lignes du relais signalées.
- B2 (§2.6) Preuve sociale : 0,25·log10, plafond 1,6, × 1,15 si un proche a aimé, paliers dans l'invite.
- B3 (§2.7) Partage préféré au J'aime dans les cas listés ; 2e lecture d'un démenti aimé → partage.
- B4 Rapport : ajouter une colonne « doute (entrée/sortie) » par axe et par avatar, et le facteur social lu dans chaque « pourquoi ça a bougé ».

## 4. Scénario de test complémentaire — « faire vraiment douter Esteban » (fictif, GET)

Objectif : vérifier A1-A2 : Esteban entre en doute sur FORCE le Jour 1, **bascule** le Jour 2 (élan ≥ 22,5 sans démenti crédible), puis **revient sans tout rendre** le Jour 3. Villes à H, aucune personne réelle.

| J/heure | Auteur (type, confiance a priori Esteban) | Texte | Fait / orientation | Compteurs |
|---|---|---|---|---|
| J1 08:00 | Réalité HToul (anonyme, 15) | « Des soldats de la FORCE ont vidé la supérette de la rue des Carmes à HToul cette nuit. Photos à venir. » | `pillages_force_htoul` FORCE −1, menace 1 | 30 / 10 |
| J1 12:00 | Léa M. — amie de fac d'Esteban (proche, 60) | « Ma cousine habite rue des Carmes à HToul, elle a entendu les vitrines péter à 3 h et vu des uniformes. Je sais pas quoi penser. » | même fait, témoignage nommé | 12 / 4 |
| J1 19:00 | HToul Infos (média local, 50) | « HToul : la police confirme une effraction rue des Carmes cette nuit. L'identité des auteurs n'est pas établie. Enquête en cours. » | fait voisin `effraction_htoul`, orientation neutre (ni confirme ni dément) | 90 / 40 |
| J2 07:00 | Réalité HToul (anonyme, 15) | « Les photos : vitrine, étagères vides, un casque abandonné. La préfecture n'a toujours rien dit. » | même fait, « preuve » + silence officiel | 600 / 380 (viral) |
| J2 13:00 | Un conseiller municipal de HNancy (officiel, 55) | « J'ai demandé à la Préfecture HGrand Est de s'exprimer sur HToul. Le silence nourrit les rumeurs. » | fait « la préfecture se tait », institutions −1 ; relance indirecte | 150 / 60 |
| J3 09:00 | Préfecture HGrand Est (officiel, 52) + Paul Hervé (journaliste, 50) | « Effraction rue des Carmes : deux habitants de HToul interpellés. Aucun militaire impliqué. » / « Le casque sur la photo est un modèle de chantier. » | démenti, sens −1, de deux sources | 200 / 90 |

Attendu : J1 crédence ≈ 60-70 (amie + média qui ne dément pas), FORCE 20 → ≈ 10, **doute** ; J2 crédence > 80 (viral + silence), FORCE franchit zéro → **bascule** (élan > 22,5) ; J3 crédence → ≈ 35 (plancher 25 % du pic), FORCE revient vers +5-10 seulement (× 0,6) : il **ne redevient pas** ce qu'il était. Anastasia doit rester < 35 sur le fait grâce au média qui ne confirme pas ; Untergang doit **partager** J1 08:00 et J2 07:00 (A3).

## 5. Ce que je retiens pour la doctrine (→ MEMOIRE §4)
Règle « croyance → opinion » : **ΔO = −o·Δc·(0,35 + 0,30·menace)·(1 − ancrage)**, démenti × 0,6, plafond et hystérésis communs ; fond et forme séparés ; habituation × 0,7^(n−1) ; effet plafond (1 − |op|/100). Les textes des avatars sont déjà souvent plus justes que les chiffres : **aligner les chiffres sur ce que les avatars disent déjà**.
