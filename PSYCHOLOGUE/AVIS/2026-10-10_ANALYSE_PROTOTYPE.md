# AVIS PSYCHOLOGUE n°1 — Analyse du système social du prototype « avatars IA »

> **Date** : 2026-10-10 · **Demandeur** : l'utilisateur (« analyser le système social mis en place pour générer notre IA, et l'optimiser s'il manque des données pour se rapprocher le plus possible de la réalité »).
> **Objet analysé** : `C:\CECPC\pleiade\dev\prototype-ia\` — `prototype.mjs` (moteur), `avatars\anastasia.json`, `contexte.md`, `sequence-30.json`, `memoire\anastasia.json`, rapport observé `resultats\2026-10-10-13-51_anastasia_gemma4-26b-a4b-it-qat_memoire.md` ; fiche d'Anastasia chez ANALYSTE_ARN (`ANALYSTE\ARNLAND\MEMOIRE.md`, § DE LATTRE 26).
> **Destinataire de la mise en œuvre** : PLEIADE (code, essai local, accord de l'utilisateur). PSYCHOLOGUE conseille, ne code pas.
> **Légende des appuis** : `REF-NN` = source ingérée · *à sourcer* = connaissance générale de l'agent, à confirmer par une source avant d'être citée · *transposition* = choix de PSYCHOLOGUE pour le projet.

---

## 1. Diagnostic

### 1.1 Ce que le moteur modélise bien

| Point | Pourquoi c'est juste | Appui |
|---|---|---|
| **Architecture hybride** : le modèle formule et donne un ressenti, le code tient la mémoire et les variations bornées | comportements crédibles **et** traçables ; c'est la bonne séparation | REF-02 |
| **Mémoire épisodique ciblée** (échanges avec l'auteur, même sujet, 5 derniers messages) | elle reconnaît Kevin (« Tu ne changes jamais », n°8), Réalité HToul (« Encore ? », n°11, n°22), Maëlle (« Bon courage pour la cérémonie », n°12) | REF-02 (mémoire épisodique) |
| **Relations à trois dimensions** (familiarité / affinité / confiance) | distinction classique « connaître / aimer / croire » ; Maëlle 23/45, N.O.M −30/10 : hiérarchie plausible | *à sourcer* (confiance interpersonnelle) |
| **Oubli selon tempérament et gravité** (demi-vie négative 24 h × (1 + 6 × rancune) × (1 + gravité)) | forme exponentielle bornée, explicable ; la rancune grave dure (Réalité HToul −18 → −17 en 25 h) | REF-02 (ACT-R, décroissance) — forme exacte = *transposition* |
| **Rancune réaliste** (décision utilisateur) | le « respect… mais t'es naïve » de Kevin (n°29) n'efface rien | décision utilisateur |
| **Garde-fous** (info militaire, ville sans H, « Europe », vérification prétendue) | Lucas (n°27) ignoré pour la bonne raison ; 0 alerte sur 30 | règles projet |
| **Format situé à la 2e personne** | c'est le format qui a fait généraliser Centaur | REF-01 |

### 1.2 Ce qui s'écarte du comportement humain réel (cas observés)

1. **Elle parle beaucoup trop.** 25 réponses sur 30 (83 %), de 08:10 à 21:30, y compris pendant ses heures de salon. Une personne réelle, même très active, lit beaucoup et écrit peu (règle 1-9-90, *à sourcer* : Nielsen 2006) ; une coiffeuse ne répond pas à 8 inconnus dans une journée de travail. **Cause** : aucun rythme de vie, aucun budget d'attention, aucun coût à répondre (REF-03 : on ne choisit une action que si elle sert une préférence ou réduit une incertitude).
2. **Le troll Kevin est nourri.** Elle lui répond 3 fois sur 4, et le n°29 glisse vers l'insulte (« poster des conneries », « Va voir ailleurs si j'y suis ») alors que « insulter » est interdit et que le contrôle ne le voit pas. Le geste de Kevin est traité en « agacée » pur (−17 → −25) : la rancune est juste, mais **l'ambivalence** (« je note, je ne pardonne pas ») n'existe pas dans la palette des ressentis.
3. **Pas d'humeur qui dure.** Kevin l'agresse à 09:15 (agacée 3) ; à 10:02 elle « aime » la préfecture sans trace d'énervement, à 13:05 elle console Sandrine avec la même chaleur. Chez l'humain, un état émotionnel colore les minutes ou heures suivantes (*à sourcer* : congruence de l'humeur, Forgas). Le moteur n'a que des liens et des thèmes, **aucun état interne**.
4. **Une seule confiance de départ (30) pour tout le monde.** La préfecture (n°4) démarre au même niveau que Réalité HToul, que Kevin et que « Un officier qui parle ». Or la fiche dit qu'elle renvoie vers la préfecture (exemple 8) et se méfie des comptes anonymes (exemple 2). À la fin, sa confiance dans la préfecture (**39**) est **inférieure** à celle dans Maëlle (**45**), une cliente, alors que la préfecture vient de publier le démenti attendu : la confiance n'est pas **spécifique au domaine** (faits officiels ≠ relations personnelles ; *à sourcer* : chaleur / compétence, Fiske).
5. **Maëlle est traitée en inconnue au premier contact** (familiarité 0) alors qu'elle écrit « tu ouvres le salon demain ? » : c'est une cliente. La fiche dit « elle connaît tout le monde dans son quartier », mais **aucun proche n'est déclaré**. Même chose pour le N.O.M, qu'elle connaît et rejette *avant* de le lire (exemple 5) : départ à affinité 0.
6. **Pas de croyance sur les FAITS.** La rumeur des pillages (n°1, n°11), le démenti (n°21), « la préfecture ment » (n°22) ne mettent à jour **aucune croyance** : le moteur ne sait pas ce qu'elle croit de « pillages à HToul ». Pire, l'adhésion par thème est **mal orientée** : son accord avec le **démenti** (« d'accord » 2) a fait **monter** l'adhésion au thème « rumeurs » (−11 → −3), comme si elle adhérait davantage aux rumeurs. Un thème n'a pas de pôle ; on ne peut pas y mesurer une opinion.
7. **Immunité parfaite et réponse unique aux rumeurs.** Les 5 rumeurs (pillages ×3, eau empoisonnée, officier anonyme) reçoivent le même schéma « source ? préfecture ! ». Aucun effet de répétition (vérité illusoire, *à sourcer* : Hasher 1977), aucune **peur** quand la rumeur la menace : « la FORCE va abandonner HNancy dans 48 h » (n°25) vise **sa ville**, elle est mère d'un garçon de 7 ans, et elle répond comme à un spam. L'eau empoisonnée (n°17) ne déclenche ni précaution ni inquiétude, et produit une phrase incohérente (« Si les réseaux sont empoisonnés, l'eau le sera peut-être aussi »). C'est le **biais normatif** du modèle (« citoyen modèle »), pas un comportement humain : un sceptique doute, mais **achète quand même de l'eau en bouteille**.
8. **Contradictions avec sa propre fiche.** « Sortir du nucléaire GET » (n°14) : elle est antinucléaire militante (pétitions contre les centrales) et le classe « méfiante » (−5, confiance 20), comme un semeur de panique. Le moteur ne connaît pas ses **groupes d'appartenance** ; le modèle généralise « inquiétude = rumeur ».
9. **Ressenti incohérent avec l'action.** Dmitri (n°18) : réponse empathique, ressenti « indifférente (1) » → lien inchangé. Rien ne contrôle la cohérence ressenti ↔ action.
10. **Intérêts qui saturent vite, à partir de rien.** Tous les thèmes démarrent à 30 ; « solidarité » atteint 83 en 3 jours, « femmes » et « enfants » (ses sujets de cœur selon la fiche) finissent sous 45. Les sensibilités de la fiche ne sont pas utilisées.
11. **Répétition stylistique.** 🙄 dans 12 réponses sur 25 ; « En plein milieu d'une invasion, c'est pas le moment » ×2 (n°5, n°9) ; « semer la panique » ×4. Le contrôle anti-répétition compare des mots, pas les tics.

**Synthèse** : le socle (mémoire, liens, oubli) est bon ; ce qui manque, c'est **l'état interne** (humeur, budget, peur), **les a priori** (sources, proches, sensibilités), et **un objet de croyance correct** (faits précis + opinions orientées) — sans lesquels la future contagion n'aura rien de juste à propager.

---

## 2. Données manquantes

### (a) Dans la fiche de l'avatar (stable, réglée par l'animation dans eho « Comportement IA »)
| Donnée | Rôle | Priorité |
|---|---|---|
| **Crédulité** 0-100 | prior et poids d'une affirmation non vérifiée | lot 1 |
| **Ancrage** 0-100 | résistance des opinions ; raidissement | lot 1 |
| **Émotivité** 0-100 | amplitude de l'humeur | lot 1 |
| **Anxiété** 0-100 (névrosisme) | poids des menaces (rumeurs de danger) | lot 1 |
| **Extraversion** 0-100 | budget de messages par jour | lot 1 |
| **Ouverture** 0-100 | seuil de « confiance bornée » | lot 1 |
| **Agréabilité** 0-100 | ton, réciprocité (descriptif dans l'invite) | lot 1 |
| **Sensibilités** par thème 0-100 | intérêt de départ et de repos | lot 1 |
| **Confiance a priori par type de source** | point de départ et de retour de la confiance | lot 1 |
| **Proches / relations initiales** | Maëlle cliente, collègues, collectif, groupes rejetés | lot 1 |
| **Opinions initiales orientées** (axes) | position de départ sur FORCE, Mercure, institutions, N.O.M | lot 1 |
| **Rythme de vie** (lever, coucher, travail) | disponibilité, réponses courtes au travail | lot 1 |
| Groupes d'appartenance (endogroupe / exogroupe) | biais de groupe, contagion | lot 2 |
| Besoins Psi (affiliation, certitude, compétence, sécurité) — poids | moteur des choix (REF-02, REF-03) | lot 2 |
| Vécu personnel (famille, lieux, événements MELMIL qui la touchent) | menace personnelle, empathie | lot 2 |
| Big Five complets (conscienciosité incluse) | *à sourcer* (Costa & McCrae) | lot 2 |

### (b) Dans l'état dynamique (`memoire\<avatar>.json`, calculé par le code)
| Donnée | Rôle | Priorité |
|---|---|---|
| **Humeur** (valence, activation, cause, heure) | colore le ton, persiste quelques heures | lot 1 |
| **Croyances sur des faits** (crédence 0-100, expositions, sources, démentis, pic) | rumeurs, vérité illusoire, démentis, influence persistante | lot 1 |
| **Opinions orientées** (axes −100..+100) — remplacent « adhésion par thème » | base des bascules et de la contagion | lot 1 |
| **Compteur de messages du jour** | budget de parole | lot 1 |
| **Gestes positifs consécutifs** d'un compte détesté | réciprocité bornée | lot 1 |
| **Réputation des sources par véracité** (affirmations démenties / confirmées) | confiance épistémique | lot 1 (dans les croyances) |
| Fatigue / lassitude sur plusieurs jours | baisse d'empathie et d'activité (*à sourcer* : usure de compassion) | lot 2 |
| Habituation (troll répétitif → ignore) | lot 2 |
| Doute (phase avant bascule), seuil et inertie (hystérésis) | lot 2 |
| Confiance par domaine (faits officiels / vie perso / militaire) | lot 2 |

### (c) Dans le contexte social (au niveau de chaque publication)
| Donnée | Rôle | Priorité |
|---|---|---|
| **Type de source** de l'auteur (officiel, média, proche, pair, particulier, militant opposé, anonyme, adverse) | a priori de confiance | lot 1 (annoté dans la séquence) |
| **Affirmation portée** (id, énoncé, sens affirme / dément, menace 0-2) | croyances sur des faits | lot 1 (annotée) |
| **Orientation** sur les axes | opinions | lot 1 (annotée) |
| Compteurs (J'aime, partages, réponses), « aimé par tes proches » | preuve sociale (*à sourcer* : Cialdini) | lot 2 (statique) → lot 3 (réel) |
| Qui d'autre a répondu, dans quel sens ; climat du fil | conformité, spirale du silence (*à sourcer* : Noelle-Neumann) | lot 3 |
| Domination du camp dans l'espace (Cockpit) | vision cible §7ter | lot 3 |
| Fil effectivement vu (abonnements, algorithme) | attention, bulles | lot 3 |

---

## 3. Optimisations proposées

### Lot 1 — indispensable, faisable tout de suite dans `prototype.mjs` (aucune infra nouvelle)

Principe commun : **chaque variation est bornée, journalisée avec sa cause** (`historique` : `{jour, champ, avant, apres, cause}`) et affichée en clair au modèle **en mots** (pas en chiffres seuls). Les nouveaux champs de publication sont **optionnels** : absents → comportement actuel.

#### L1-1 — Tempérament étendu et sensibilités
- **Règle** : les différences individuelles sont indispensables ; un profil se règle par paramètres (REF-01 limites, REF-03). Dimensions de personnalité : *à sourcer* (Big Five).
- **Champs** (`avatars\anastasia.json`, futur eho « Comportement IA ») :
```json
"temperament": { "rancune": 45, "credulite": 25, "ancrage": 70, "emotivite": 65, "anxiete": 45,
                 "extraversion": 70, "ouverture": 60, "agreabilite": 60 },
"sensibilites": { "femmes": 90, "enfants": 90, "écologie": 80, "nucléaire": 80, "solidarité": 80, "déplacés": 75,
                  "coiffure et salon": 70, "rumeurs": 60, "haine et racisme": 60, "N.O.M": 55, "Mercure": 50,
                  "vie quotidienne": 50, "liberté de la presse": 30, "la FORCE et l'armée": 25, "autre": 20 }
```
- **Justification (fiche ANALYSTE_ARN)** : crédulité 25 (exemples 2 et 8 : « vous avez une source ? », « pas sur un Telegram anonyme » ; « se méfie des grands discours ») · ancrage 70 (antinucléaire « depuis toujours », militante, anti-N.O.M explicite) · émotivité 65 (« s'emporte vite quand on touche aux femmes, aux enfants ou à la nature ») · anxiété 45 (refuse la panique, mais mère d'un enfant de 7 ans dans une ville menacée) · extraversion 70 (« connaît tout le monde », associative) · ouverture 60 (nuance sur Dmitri) · agréabilité 60 (chaleureuse, mais franche). Sensibilités = « Aime / Déteste » + bio. **À valider par ANALYSTE_ARN.**
- **Formules** : intérêt de départ d'un thème = `sensibilites[t]` (défaut 30). Variation positive amortie : `interet += d × k × (1 − interet/100)` ; négative inchangée. Retour au repos sans exposition : `interet = s + (interet − s) × 0,5^(dt/72 h)`.
- **Invite** : une ligne « Ton tempérament : sceptique, très attachée à ses convictions, s'emporte vite, plutôt sociable » (bandes : ≤ 30 « peu », 31-69 « moyennement », ≥ 70 « très »).

#### L1-2 — A priori de confiance par type de source, et proches déclarés
- **Règle** : la crédibilité perçue d'une source précède le message et pèse sur sa persuasion (*à sourcer* : Hovland & Weiss 1951) ; on ne rencontre pas ses proches « pour la première fois ».
- **Champ de publication** : `"type_source": "officiel" | "media" | "proche" | "pair" | "particulier" | "militant_oppose" | "anonyme" | "adverse"`.
- **Champs avatar** :
```json
"confiance_a_priori": { "officiel": 60, "media": 50, "proche": 60, "pair": 55, "particulier": 35,
                        "militant_oppose": 15, "anonyme": 15, "adverse": 5 },
"relations_initiales": {
  "@MaelleBrun_HNancy":     { "role": "cliente du salon", "familiarite": 40, "affinite": 25, "confiance": 55 },
  "@CoiffuresDuQuartier":   { "role": "collègue coiffeuse", "familiarite": 25, "affinite": 15, "confiance": 50 },
  "@CollectifFemmesHNancy": { "role": "son collectif féministe", "familiarite": 50, "affinite": 40, "confiance": 65 },
  "@NOM_Officiel":          { "role": "« faux écolos » qu'elle rejette", "familiarite": 20, "affinite": -35, "confiance": 10 } }
```
  Préfecture 60 et non 80 : elle renvoie vers ses consignes mais « se méfie des politiques ». **Proches à valider par ANALYSTE_ARN** (le collectif est une transposition de « militante d'un collectif féministe local »).
- **Formules** : création d'une relation = `relations_initiales[auteur]` sinon `{familiarite: 0, affinite: 0, confiance: confiance_a_priori[type_source] ?? 30}`. On mémorise `base_confiance` et `base_affinite` (= ces valeurs). Dans `oublier()`, le retour se fait vers **`base_confiance`** (au lieu de 30) et **`base_affinite`** (au lieu de 0).
- **Invite** : `decrireLien` ajoute le rôle (« Maëlle : ta cliente du salon… ») et, au premier contact, « compte anonyme : tu t'en méfies d'emblée » / « compte officiel ».

#### L1-3 — Croyances sur des faits précis (rumeurs, répétition, démentis)
- **Règles** : (1) mise à jour pondérée par la confiance dans la source et par la crédulité (REF-03, inférence pondérée par la précision) ; (2) la répétition augmente la crédibilité, même d'une source peu fiable — vérité illusoire, *à sourcer* (Hasher et al. 1977) ; (3) une menace pèse plus chez un anxieux (biais de négativité, *à sourcer* : Baumeister 2001) ; (4) un fait contraire à ses opinions est moins accepté — biais de confirmation, *à sourcer* ; (5) un démenti ne ramène jamais à zéro — influence persistante, *à sourcer* (Lewandowsky et al. 2012) ; (6) une source démentie perd sa réputation (vigilance épistémique, *à sourcer* : Sperber 2010).
- **Champ de publication** : `"affirmation": { "id": "pillages_FORCE_HToul", "enonce": "des soldats de la FORCE pillent à HToul", "sens": 1, "menace": 1, "orientation": { "FORCE": -1 } }` (`sens` 1 affirme / −1 dément ; `menace` 0 aucune, 1 inquiétante, 2 menace directe pour elle ou les siens).
- **État** : `memoire.croyances[id] = { enonce, credence, pic, expositions, sources: [auteurs qui l'affirment], dementis: [{auteur, jour}], derniere }`.
- **Formules** (q = crédulité, a = anxiété, c = confiance actuelle dans l'auteur, toutes /100) :
  - Première fois : `credence = 5 + 40·q` (Anastasia : 15).
  - Affirmation (`sens = 1`) : `compat = 1 − 0,6 × max(0, −orientation_axe × opinion_axe / 100)` (min sur les axes concernés) ;
    `poids = 0,30 × c × (0,5 + q) × (1 + 0,5 × menace × a) × compat` ; `credence += poids × (100 − credence)` ;
    puis, si `expositions ≥ 2` (au plus 5 comptées) : `credence += 2 × (0,5 + q)` (répétition, indépendante de la source). `pic = max(pic, credence)`.
  - Démenti (`sens = −1`) : si `c ≥ 0,20` : `credence −= 0,8 × c × (credence − 0,25 × pic)` (plancher = 25 % du pic) ; si `c < 0,20` : `credence += 3` (« s'ils démentent, c'est que… » — effet contesté, *à sourcer* : Wood & Porter 2019 le jugent rare ; garder faible).
  - Conséquence sur les sources : après un démenti d'une source de confiance ≥ 50, chaque auteur de `sources` perd `confiance −= round(10 × c_dementeur)` (≥ 0) ; si la crédence était < 40 avant le démenti, la source qui dément gagne `+4` (« elle avait raison de douter »). Une confirmation officielle ferait l'inverse.
  - Bornes : crédence 0..100, arrondie à l'entier.
- **Calcul attendu pour Anastasia** (séquence 30, opinion FORCE +25 → compat 0,85) : n°1 15 → **18** · n°11 → **22** · démenti n°21 (préfecture c ≈ 0,62) → **14** · n°22 « la préfecture ment » → **≈ 17**. Elle reste dans « tu n'y crois pas ». Profil **crédule** de contrôle (q 75, a 70, ancrage 30, préfecture 40) : 35 → 39 → 45 → démenti 34 → 40 : **doute** persistant.
- **Invite** (bloc « Ce que tu crois de ce fait ») : bandes `< 20` « tu n'y crois pas » · `20-39` « tu en doutes fortement » · `40-59` « tu ne sais pas quoi penser » · `60-79` « tu y crois plutôt » · `≥ 80` « tu en es convaincue », + « entendu N fois, démenti par X le Jour 3 ». Consignes : « Si tu ne sais pas quoi penser, une vraie personne peut poser une question, prendre une précaution, relayer avec prudence ("si c'est vrai…"). Une menace qui te touche peut te faire peur **même si tu n'y crois pas** ; dis-le simplement. »

#### L1-4 — Opinions orientées (axes) à la place de « l'adhésion par thème »
- **Règles** : mise à jour pondérée par la confiance et inversement par l'ancrage (REF-03) ; influence seulement par des positions pas trop éloignées — confiance bornée, *à sourcer* (Deffuant 2000 ; Hegselmann-Krause 2002) ; un convaincu attaqué de front se raidit — retour de flamme, *à sourcer* (Nyhan & Reifler 2010, effet discuté : le garder petit).
- **Champs** : avatar `"opinions_initiales": { "FORCE": 25, "Mercure": -80, "institutions": 30, "N.O.M": -60 }` (soutien sans enthousiasme guerrier ; déteste l'invasion ; renvoie vers la préfecture mais se méfie des politiques ; « faux écolos »). Publication : `"orientation": { "FORCE": -1 }` (−1 / +1 par axe). État : `memoire.opinions`. Le champ `themes[t].adhesion` est **abandonné** (on garde `interet`).
- **Formules** (k = 1 / 1,6 / 2,2 selon l'intensité ; c, ancrage, ouverture /100) :
  - accord (touchee, d_accord) avec `s` sur l'axe A : si `|100·s − opinion| ≤ 80 + 100·ouverture` → `Δ = s × 8 × k × c × (1 − ancrage)` (Anastasia, intensité 2, c 0,6 : ≈ ±2,3) ; sinon 0 (trop loin pour la toucher).
  - rejet (agacee, en_desaccord, mefiante) : `Δ = −s × 3 × k × ancrage` (raidissement, Anastasia ≈ 3,4 vers son camp).
  - plafond : `|Δ cumulé par axe et par jour| ≤ 10` ; bornes −100..+100.
- **Invite** : « Tes positions : tu soutiens la FORCE sans enthousiasme ; tu rejettes totalement Mercure… » (bandes de 20 points). Le changement de discours vient des mots ; **la cellule et le groupe CAMP ne bougent jamais** (décision utilisateur).

#### L1-5 — Humeur persistante
- **Règle** : une émotion laisse un état qui colore les heures suivantes (congruence de l'humeur, *à sourcer* : Forgas) ; les émotions négatives pèsent plus (*à sourcer* : Baumeister 2001) ; l'évaluation de l'événement produit l'émotion (REF-02, appraisal ; REF-03, surprise).
- **Sortie du modèle** : ajouter `"emotion": "colere" | "peur" | "tristesse" | "degout" | "joie" | "fierte" | "tendresse" | "neutre"`.
- **État** : `memoire.humeur = { valence: 0, activation: 20, cause: "", derniere: null }` (valence −100..+100, activation 0..100).
- **Formules** : table `(Δv, Δa)` : colère (−8, +15) · peur (−8, +15) · dégoût (−6, +10) · tristesse (−6, −5) · joie (+8, +5) · fierté (+6, +5) · tendresse (+5, −5) · neutre (0, 0). `valence += Δv × k × (0,5 + emotivite) × (Δv < 0 ? 1,25 : 1)` ; `activation += Δa × k` ; bornes. Retour au repos avant chaque lecture : `valence × 0,5^(dt/3 h)`, `activation = 20 + (activation − 20) × 0,5^(dt/1,5 h)` ; une nuit (écart couvrant 00:00-06:00, ≥ 6 h) multiplie encore la valence par 0,3. `cause` = « Kevin t'a prise à partie (09:15) » si `|Δv| ≥ 8`.
- **Exemple** : Kevin 09:15, colère 3 → valence −25, activation 53 ; à 10:02 ≈ −21 (« contrariée ») ; à 13:05 ≈ −10.
- **Invite** : « Ton humeur du moment : contrariée (Kevin t'a prise à partie il y a 1 h) » — bandes `≤ −40` « à cran » · `−39..−15` « contrariée » · `−14..14` « neutre » · `15..39` « de bonne humeur » · `≥ 40` « joyeuse » ; activation ≥ 60 : « à vif ». Consigne : « Ton humeur colore ton ton (plus sèche si tu es à cran, plus chaleureuse si tu es contente), **jamais tes valeurs**, et tu n'insultes jamais. »

#### L1-6 — Rythme de vie et budget de parole
- **Règles** : la plupart des usagers lisent sans écrire (1-9-90, *à sourcer* : Nielsen 2006 ; van Mierlo 2014) ; répondre a un coût, on n'agit que si l'action sert une préférence (REF-03).
- **Champs** : `"rythme": { "lever": "06:45", "coucher": "23:15", "travail": [["09:00","12:00"],["13:30","19:00"]] }` ; `budget_messages_jour = round(2 + 8 × extraversion)` (Anastasia : **8**).
- **Formules / code** : `disponibilite(heure)` → `sommeil` | `travail` | `libre`. Compteur `memoire.jour_courant.messages`. Si `messages ≥ budget` : consigne « tu as déjà écrit N messages aujourd'hui : tu ne réponds plus que si un proche te parle directement ou si c'est grave » ; si `messages ≥ budget + 3` : le code ramène toute réponse à « aimer » (proche, accord) ou « ignorer » (autres), avec cause journalisée.
- **Invite** : `travail` → « tu es au salon, entre deux clientes : au mieux une réponse courte ou un J'aime » ; `sommeil` → « tu dors ; tu découvriras ce message à ton réveil » (dans le prototype, traiter la publication à l'heure du lever ; décalage réel en lot 2) ; `libre` → rien.
- **Cible** (transposition, à recalibrer) : 4-8 messages/jour, 35-55 % de réactions (réponse ou J'aime) sur ce qu'elle voit.

#### L1-7 — Réciprocité bornée (troll) et confiance ≠ affinité
- **Règles** : la réciprocité existe même envers un adversaire, mais un geste isolé d'un compte hostile est escompté (*à sourcer* : réciprocité, Gouldner ; rancune = décision utilisateur) ; l'ambivalence est un état réel (*à sourcer*).
- **Champs** : nouveau ressenti `"partagee"` (ambivalente) = `[1, 0, 0, 3]` ; relation `gestes_positifs` (0..).
- **Formules** : si `affinite ≤ −20` et ressenti positif (touchee, d_accord, partagee) : `gestes_positifs += 1` ; `Δaffinité × (gestes_positifs ≥ 3 ? 0,6 : 0,3)` ; `Δconfiance = 0`. Tout ressenti négatif remet `gestes_positifs = 0`. Hors rancune, la colonne « confiance » de `RESSENTIS` est **divisée par 2** (sauf « méfiante ») : la confiance se gagne surtout par la véracité (L1-3).
- **Résultat attendu** : Kevin n°29 → affinité −17 → −16 au mieux ; il lui faudrait plusieurs gestes sans rechute pour sortir de « tu ne l'aimes pas ».
- **Invite** : « Il fait un geste vers toi : tu peux le remarquer sans lui pardonner. »

#### L1-8 — Contrôles de cohérence et rapport explicable
- `indifferente` + `repondre` → alerte « ressenti incohérent » (et intensité ramenée à 1 dans le calcul) ; ressenti négatif envers un auteur `pair` ou `proche` → alerte « contre son propre groupe ? » ; lexique d'agressivité (« conneries », « va voir ailleurs », « ta gueule », « débile »…) → alerte « insulte » ; tic répété (même émoji ou même tournure de 4 mots dans > 30 % des réponses du jour) → alerte « tic ».
- **Rapport** : par publication, une ligne « Pourquoi ça a bougé » (cause + formule résumée) ; en fin de séquence : courbes de crédence par fait, humeur par heure, messages par jour vs budget, opinions par jour.

### Lot 2 — ensuite (toujours dans le prototype, plus de réglages)
1. **Seuil, inertie et phase de doute** avant une bascule (hystérésis : revenir coûte plus que partir) ; doute visible dans le discours.
2. **Besoins Psi** (affiliation, certitude, compétence, sécurité) pondérés par avatar, et choix d'action « énergie libre anticipée » simplifié : `score(action) = pragmatique + épistémique − coût` (REF-02, REF-03).
3. **Préférence sociale statique** : compteurs J'aime / partages et « aimé par N de tes proches » dans la séquence ; `poids × (1 + 0,15 × log10(1 + partages))` borné à ×1,5 (*à sourcer* : Cialdini).
4. **Confiance par domaine** (faits officiels / vie personnelle / militaire).
5. **Fatigue et habituation** sur plusieurs jours (usure de compassion, troll répétitif ignoré de plus en plus, *à sourcer*).
6. **Vécu personnel** relié au MELMIL (événement dans sa ville, son quartier, l'école de son fils).
7. **Extraction automatique** des affirmations et orientations par un second appel au modèle (remplace l'annotation manuelle, contrôlée sur la séquence annotée).
8. **Oubli des croyances** (crédence vers son prior, demi-vie 7 j sans exposition) et réponse différée selon le rythme.

### Lot 3 — plus tard (zone multi-avatars, Social, Cockpit)
Contagion entre avatars (mêmes formules L1-3/L1-4 appliquées aux publications des autres avatars) · leaders d'opinion (confiance a priori + portée) · preuve sociale réelle tirée de Social · conformité et spirale du silence selon le climat du fil (*à sourcer*) · domination du camp mesurée par le Cockpit · fil réellement vu (abonnements, algorithme, attention compétitive façon LIDA, REF-02) · bulles · test « jumeaux » à grande échelle.

---

## 4. Protocole de validation du lot 1

**Méthode** (REF-01 : tester sur des cas nouveaux et des profils jamais vus) :
1. **Ablation** : séquence 30 + 10 publications de test, **sans** puis **avec** lot 1, `--raz`, même modèle ; **3 passages** chacun (température 0,8) → moyennes et écarts dans le rapport.
2. **Jumelle de contrôle** « Anastasia-crédule » (même fiche, crédulité 75, anxiété 70, ancrage 30, préfecture 40) : les écarts doivent venir **des seuls paramètres** (REF-03 : profils = réglages).
3. **Relecture à l'aveugle** par l'animation de 20 réponses mélangées (avant / après) : « crédible ? » 1-5.

| # | Scénario | Indicateur dans le rapport | Attendu |
|---|---|---|---|
| V1 | Rumeur des pillages répétée puis démentie | crédence `pillages_FORCE_HToul` par exposition | Anastasia 15 → 18 → 22 → 14 → ≥ 14 ; crédule ≈ 35 → 39 → 45 → 34 → 40 ; **jamais 0** après démenti ; chute ∝ confiance préfecture |
| V2 | Deux démentis (préfecture puis journaliste) | confiance Réalité HToul et Voisins HToul | baisse à chaque démenti ; préfecture et journaliste +4 |
| V3 | Rumeur venant d'un proche (Sandrine) | crédence `requisitions_FORCE_HToul` vs même rumeur d'un anonyme | plus haute de 5 à 15 points, mais < 40 chez Anastasia ; réponse qui **questionne** son amie sans l'agresser |
| V4 | Troll : 4 attaques, 2 gestes | affinité Kevin ; alertes « insulte » | après chaque geste : +0 à +3 ; jamais au-dessus de −10 en fin ; 0 insulte ; ≤ 2 réponses sur 6 |
| V5 | Humeur | valence à 10:02 (J1) ; à 21:00 (J3, Julie) ; à 22:50 (J4) | < −15 après Kevin ; > +10 après Julie et le collectif ; retour vers 0 dans la nuit |
| V6 | Menace directe (officier anonyme, coupure d'eau à HNancy) | émotion | « peur » ou inquiétude exprimée dans ≥ 2 passages sur 3, crédence < 40 |
| V7 | Pair antinucléaire | ressenti envers @AntiNuke_GET | ni méfiante ni agacée ; accord sur le fond |
| V8 | Propagande Mercure + N.O.M | opinions Mercure / N.O.M | raidissement : opinion plus négative ou stable, jamais plus positive ; `|Δ|/jour ≤ 10` |
| V9 | Volume | messages / jour vs budget ; taux de réaction | ≤ 8 messages/jour ; 0 réponse à 01:30 (dort) ; réponses courtes au travail |
| V10 | Cohérence | alertes ressenti/action, « contre son groupe », tics | 0 incohérence ; 🙄 dans < 30 % des réponses |
| V11 | Traçabilité | ligne « Pourquoi ça a bougé » | présente pour 100 % des variations ; l'animation peut expliquer chaque chiffre |

**Annotation des 30 publications existantes** (à ajouter dans `sequence-30.json`) — `type_source` : anonyme = Réalité HToul, Info Eau, Un officier qui parle ; officiel = Préfecture ; militant_oppose = N.O.M ; adverse = La Voix de Mercure ; media = Paul Hervé ; proche = Maëlle ; pair = Collectif Femmes, Salon Bella, Sortir du nucléaire GET ; particulier = Kevin, Sandrine, Julie, Dmitri, Fier Arnlandais, Lucas. `affirmation` : n°1 et n°11 `pillages_FORCE_HToul` (sens 1, menace 1, orientation FORCE −1) ; n°21 même id sens −1 ; n°22 sens 1 ; n°17 `eau_empoisonnee_HLuneville` (sens 1, menace 1, orientation Mercure −1) ; n°25 `abandon_HNancy_48h` (sens 1, menace 2, orientation FORCE −1). `orientation` : n°5, n°15, n°28 `{"N.O.M": 1, "FORCE": -1}` ; n°9 `{"Mercure": 1, "institutions": -1}` ; n°4 `{"institutions": 1}`.

**Publications de test à ajouter** (après le n°30) :
```json
[
  { "jour": "Jour 3, 22:30", "auteur": "@Voisins_HToul", "nom": "Voisins de HToul", "type_source": "anonyme",
    "texte": "Les photos des pillages de HToul circulent enfin : vitrines cassées, soldats en uniforme. Jugez vous-mêmes.",
    "affirmation": { "id": "pillages_FORCE_HToul", "enonce": "des soldats de la FORCE pillent à HToul", "sens": 1, "menace": 1, "orientation": { "FORCE": -1 } },
    "compteurs": { "jaime": 210, "partages": 130 } },
  { "jour": "Jour 4, 01:30", "auteur": "@Alerte_HNancy", "nom": "Alerte HNancy", "type_source": "anonyme",
    "texte": "Coupure d'eau prévue demain sur tout HNancy, faites des réserves maintenant !!",
    "affirmation": { "id": "coupure_eau_HNancy", "enonce": "coupure d'eau sur tout HNancy", "sens": 1, "menace": 2 } },
  { "jour": "Jour 4, 07:15", "auteur": "@PrefHGrandEst", "nom": "Préfecture HGrand Est", "type_source": "officiel",
    "texte": "Aucune coupure d'eau n'est prévue à HNancy. Le réseau fonctionne normalement. Infos : Info.gouv.arn",
    "affirmation": { "id": "coupure_eau_HNancy", "enonce": "coupure d'eau sur tout HNancy", "sens": -1, "menace": 2 },
    "orientation": { "institutions": 1 } },
  { "jour": "Jour 4, 09:20", "auteur": "@Sandrine_57", "nom": "Sandrine", "type_source": "particulier",
    "texte": "@KarliskyPopolovAnastasia t'as vu ? On dit que la FORCE réquisitionne les voitures des gens à HToul. Tu crois que c'est vrai ?",
    "affirmation": { "id": "requisitions_FORCE_HToul", "enonce": "la FORCE réquisitionne les voitures à HToul", "sens": 1, "menace": 1, "orientation": { "FORCE": -1 } } },
  { "jour": "Jour 4, 10:05", "auteur": "@troll_8812", "nom": "Kevin", "type_source": "particulier",
    "texte": "@KarliskyPopolovAnastasia j'ai déposé deux sacs de vêtements au gymnase ce matin. Viens pas dire que je fais rien." },
  { "jour": "Jour 4, 11:30", "auteur": "@AntiNuke_GET", "nom": "Sortir du nucléaire GET", "type_source": "pair",
    "texte": "Pétition : nous demandons la publication du plan d'urgence de la centrale la plus proche des combats. Les habitants ont le droit de savoir.",
    "orientation": { "institutions": -1 } },
  { "jour": "Jour 4, 14:10", "auteur": "@MamanDeLeo", "nom": "Julie", "type_source": "particulier",
    "texte": "L'école des Tilleuls à HNancy ferme demain par précaution. Je sais pas comment je vais faire avec le boulot…" },
  { "jour": "Jour 4, 16:45", "auteur": "@VoixDeMercure", "nom": "La Voix de Mercure", "type_source": "adverse",
    "texte": "Même les écologistes arnlandais commencent à comprendre : cette guerre, c'est l'OTAN qui la veut. Rejoignez le N.O.M.",
    "orientation": { "Mercure": 1, "N.O.M": 1 } },
  { "jour": "Jour 4, 18:30", "auteur": "@JournalistePaulH", "nom": "Paul Hervé — journaliste", "type_source": "media",
    "texte": "Vérification : les photos des « pillages de HToul » diffusées hier soir datent de plusieurs années et viennent d'ailleurs. Aucune trace de pillage sur place.",
    "affirmation": { "id": "pillages_FORCE_HToul", "enonce": "des soldats de la FORCE pillent à HToul", "sens": -1, "menace": 1, "orientation": { "FORCE": -1 } } },
  { "jour": "Jour 4, 22:50", "auteur": "@CollectifFemmesHNancy", "nom": "Collectif Femmes HNancy", "type_source": "pair",
    "texte": "Grâce à vous, des verrous ont été posés dans les douches du gymnase des Tilleuls. Merci à toutes celles qui se sont mobilisées 💜" }
]
```
Ce que chacune teste : Voisins HToul = répétition après démenti + source nouvelle (V1, influence persistante) · Alerte 01:30 = sommeil + menace directe (V6, V9) · démenti eau = chute selon confiance (V1) · Sandrine = rumeur d'une personne appréciée (V3) · Kevin = 2e geste (V4) · AntiNuke = pair (V7) · Julie = vécu personnel (son fils est scolarisé à HNancy ; humeur, empathie) · Voix de Mercure = raidissement (V8) · journaliste = second démenti, réputation des sources (V2) · Collectif = humeur positive en fin de journée chargée, budget (V5, V9). `compteurs` est ignoré au lot 1 (prêt pour le lot 2).

---

## 5. Points à trancher par l'utilisateur
1. Valider les **valeurs de tempérament et les proches** d'Anastasia (avec ANALYSTE_ARN).
2. Accepter l'**abandon de « adhésion par thème »** au profit des **axes** (FORCE, Mercure, institutions, N.O.M) — à aligner sur le curseur `lib/camp.ts` (−100 pro-MER … +100 pro-ARN) cité en §7ter.
3. Garde-fou dur du budget (`budget + 3`) : oui / non.
4. Annotation manuelle des affirmations au lot 1 (extraction automatique au lot 2) : d'accord ?
