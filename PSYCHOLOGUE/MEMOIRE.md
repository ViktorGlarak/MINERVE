# MÉMOIRE — PSYCHOLOGUE

> **Agent n°26 du système MINERVE**, créé le **2026-10-10** à la demande de l'utilisateur.
> Rôle : **expert en psychologie** au service du **système évolutif de sociabilité des avatars** (projet « avatars animés par IA », piloté par PLEIADE — `PLEIADE\PROJET_AVATARS_IA.md`).
> ⭐ **Réflexe** : CONSULTER cette mémoire avant toute décision sur le comportement, les émotions, les relations, l'influence ou les bascules d'opinion d'un avatar · la METTRE À JOUR après chaque décision ou chaque source ingérée (compte rendu daté dans `JOURNAL.md`).

---

## 1. Mission et limites (décision utilisateur, 2026-10-10)

- **Stocker toute la logique et toutes les données** utiles pour **perfectionner le système évolutif de sociabilité** des avatars : personnalité, émotions, mémoire, relations, influence, bascules.
- **Ingérer** chaque source fournie (fiche `REFERENCES\REF-NN_*.md` : ce que dit la source + « Application au projet »), puis affiner la doctrine (§3).
- **Conseiller** PLEIADE (qui code le moteur), EXPERT_INFLUENCE (doctrine ILI : ce qu'on cherche à produire comme effet), les ANALYSTES pays (profils des personnages) et DESIGNER (comment rendre ces états lisibles pour l'animation). **Il ne code pas** et ne pousse rien.
- **Distinguer** toujours : ce que dit une **source** (citée `REF-NN`) · ce qui est une **connaissance générale** de l'agent (marquée *à sourcer*) · ce qui est une **transposition** au projet.
- **Cadre** : avatars **fictifs** d'un exercice d'entraînement (univers Skolkan : Mercure, Arnland, Bothnia, France / la FORCE). Jamais de modélisation d'une personne réelle. Le dossier `D:\CECPC\DOC REF\MERCURE\RENS\01_Fiches bio` reste **interdit sans autorisation**.

## 2. État du système de sociabilité (prototype `C:\CECPC\pleiade\dev\prototype-ia\`, au 2026-10-10)

> Source de vérité du projet : `PLEIADE\PROJET_AVATARS_IA.md` (§7ter vision cible, §8 journal). Ici, la logique psychologique.

- **Fiche de l'avatar** (eho) : personnage (pays, activité, caractère, registre, aime / déteste, bio interne), affiché (profil public, langue), réel (localisation réelle, cellule).
- **Mémoire épisodique** : souvenirs (jour, auteur, publication, action, texte, sujet) ; avant chaque réaction, relecture de ses échanges passés avec l'auteur, du même sujet et de ses 5 derniers messages (anti-répétition, anti-contradiction).
- **Relations** envers chaque compte : familiarité 0-100 (+3 vu, +6 aimé, +10 échange), affinité −100..+100, confiance 0-100, historique. Envers chaque thème (15, liste fermée) : intérêt 0-100, adhésion −100..+100.
- **Émotions** : après chaque lecture, le modèle donne un **ressenti** (touchée, d'accord, indifférente, agacée, en désaccord, méfiante) et une **intensité** 1-3 ; le code applique des variations **bornées** (×1 / ×1,6 / ×2,2).
- **Tempérament** : `rancune` 0-100 (Anastasia 45). **Oubli** sans contact (décision utilisateur) : une rancune s'efface d'autant plus lentement que l'avatar est rancunier et que l'offense était grave — demi-vie négative = 24 h × (1 + 6 × rancune) × (1 + gravité) ; sympathie : demi-vie 7 jours ; confiance → 30.
- **Décisions de l'utilisateur** : rancune **réaliste** (un geste tardif d'un troll ne l'efface pas) ; l'oubli dépend du tempérament et de la gravité ; **contagion : oui** ; la **bascule** change le **discours**, jamais la cellule qui tient le compte (PACK, groupe « CAMP … »).
- **Modèle de langage** : Gemma 4 26B (MoE) sur le PC du projet, `think: false`.
- ⭐ **LOT 1 de l'avis n°1 EN PLACE (2026-10-10)** dans `prototype.mjs` (mode `--memoire`) : tempérament étendu + sensibilités · a priori de confiance par `type_source` + `relations_initiales` · `croyances` sur des faits · `opinions` par axes (FORCE, Mercure, institutions, N.O.M ; l'adhésion par thème est abandonnée) · `humeur` · `rythme` + budget 8 messages/jour (garde-fou budget + 3) · réciprocité bornée (`partagee`, `gestes_positifs`) · contrôles insulte / tics / incohérences + « pourquoi ça a bougé ». **Réglages après essai** : raidissement réduit à 1,5 × k × ancrage, seulement si intensité ≥ 2, au plus ±4 par axe et par jour (à 3 × k : FORCE 25 → 53 en 4 jours) ; menace directe × anxiété ≥ 0,5 → « une part de toi s'inquiète » ; consignes « ignorer ≠ ne rien ressentir » et « le ressenti porte sur l'auteur, pas sur la rumeur ». Résultats : `C:\CECPC\pleiade\dev\prototype-ia\resultats\2026-10-10-16-24_*_lot1.md` (Anastasia) et `…16-26_anastasia-credule_*` (jumelle).
- ⭐ **CONTAGION EN PLACE (2026-10-10, soir)** — la psychologie est désormais dans **`moteur.mjs`** (classe `Esprit`), partagée par `prototype.mjs` (un avatar) et **`simulation.mjs`** (plusieurs avatars sur un fil commun : créneaux de lecture de 3 h, 3 publications lues par créneau, répondre / aimer / **partager** / **publier**, extraction automatique des affirmations, preuve sociale, groupe affiché, leader, **hystérésis doute → bascule**). **Lot A de l'avis n°2 appliqué** : croyance → opinion (ΔO = o·Δc·(0,35 + 0,30·menace)·(1 − ancrage), démenti × 0,6 — ⚠ convention : orientation −1 = le fait accuse l'axe, donc croire davantage fait BAISSER l'axe), `ressenti_forme` / `ressenti_fond` + « soulagée », relais qui partage les faits alignés et varie ses `registres`, habituation × 0,7^(n−1), effet plafond (1 − |op|/100), extraction stricte. Distribution de test : Anastasia, Untergang (relais, `avatars\untergang.json`), Mordvidchev (maire, leader), Petitjean (crédule anxieux) ; scénarios `scenario-contagion.json` (2 j) et `scenario-doute.json` (3 j, §4 de l'avis n°2). **Dernier essai** (`resultats\2026-10-10-18-42_simulation_*.md`) : Esteban doute (FORCE 20 → 5,9) sans franchir zéro, revient à 14,5 après démenti ; Anastasia monte à 49 (à juger) ; Untergang 11 partages / 23. **Reste** : lot B, boucle d'écho relais ↔ crédule (repartages répétés du même fait), seuil de bascule à juger.
- ⭐ **ÉTAT AU 2026-10-10 (soir, après lots B + C et relecture n°4)** — rapport `resultats\2026-10-10-19-19_simulation_*.md` : **Esteban bascule J2 14:00** (FORCE 20 → 4,2 → −1,7), crédence pillages 73 → 31 après trois démentis, mais FORCE reste à **−1,9** (inertie au retour) et institutions à 4,7 (fait d'absence périmé sans restitution) ; Anastasia max 26 ; « la préfecture se tait » 15 chez tous après le communiqué ; Untergang 5/4/4 messages, 3 partages ; textes crédibles partout (moments de vie, registres variés). **Verdict n°4 : prêt pour une démonstration sous réserve de D1 + D2 + D4** (voir §4.4).
- ✅ **LOT D APPLIQUÉ ET VÉRIFIÉ (2026-10-10, fin de soirée)** — `seuilRetour = seuil × (0,25 + 0,75·min(1, Δh/72))` + pression retenue libérée à la bascule ; fait d'absence périmé = démenti (× 0,6) ; J'aime retiré = contrôle silencieux (seulement sur une affirmation d'assurance ≥ 0,5, sans soutien affectif) ; drapeaux réels interdits ; @mention nettoyée ; refus de repartage limité aux faits affirmés, refus avec texte → réponse ; relais devant un fil vide publie une ligne ; réponse illisible → second appel ; émojis hors des tics. **Rapport de référence pour la démonstration : `resultats\2026-10-10-19-38_simulation_*.md`** — Esteban FORCE **20 → 6,8 → 1 → 10** (bascule J2, re-bascule J3 11:00 avec libération de la pression retenue, fin 10 ≈ attendu 9), institutions 15 → 4,2 → 12,2 (≈ attendu 10), crédence pillages 81 → 36 ; Anastasia max 29 ; Untergang 6 / 8 / 10 messages, 5 partages ; maire stable, plus écouté ; 7 alertes (tics), 0 insulte. **Prêt pour une démonstration.** Reste (« ensuite ») : support nouveau, compatibilité C10, colonne doute, scénario de démo enrichi.

## 3. Doctrine (sourcée quand c'est possible)

### 3.1 Principe d'architecture — hybride (REF-02)
Le **modèle de langage** interprète et formule (le « cortex ») ; le **code** tient les **structures fixes** : mémoires, besoins, relations, règles d'évolution bornées. → comportements crédibles **et** traçables (l'animation doit pouvoir expliquer une bascule).

### 3.2 Les modules de l'esprit d'un avatar (REF-02)
Perception (fil vu) → **attention** (ce qui gagne l'accès, façon espace de travail global de LIDA) → mémoire de travail (invite) → mémoires **épisodique** (souvenirs), **sémantique** (base de son camp), **procédurale** (habitudes) → **besoins** (Psi-Theory : affiliation, certitude, compétence, sécurité) → **émotions** (évaluation de l'événement) → **apprentissage** (relations, opinions) → **oubli** (décroissance, ACT-R).

### 3.3 Décider de réagir (REF-03)
Choisir l'action (répondre, aimer, partager, ignorer) qui **minimise l'énergie libre anticipée** = ce qui sert le mieux ses **préférences** (sécurité, appartenance, reconnaissance) et réduit son **incertitude**. Un contenu qui ne touche ni l'un ni l'autre est ignoré.

### 3.4 Changer d'avis (REF-03 + connaissances à sourcer)
- **Mise à jour pondérée** : le déplacement d'une opinion est proportionnel à la **confiance** dans la source et inversement proportionnel à l'**ancrage** de l'avatar (« précision » des croyances).
- **Confiance bornée** *(Deffuant ; Hegselmann-Krause — à sourcer)* : on n'est influencé que par des positions **pas trop éloignées** de la sienne.
- **Effet retour de flamme** *(à sourcer)* : un convaincu attaqué de front se **raidit**.
- **Effet de vérité illusoire** *(à sourcer)* : la **répétition** rend une affirmation plus crédible, même fausse.
- **Preuve sociale, leaders d'opinion, biais de confirmation, appartenance au groupe** *(à sourcer)*.
- **Hystérésis** : basculer demande une accumulation ; revenir en arrière en demande davantage ; une **phase de doute** précède la bascule.

### 3.5 Différences individuelles (REF-01, REF-03)
Les modèles généralistes (Centaur) manquent de **différences individuelles** : nos paramètres de tempérament (rancune, crédulité, ancrage, émotivité, personnalité « Big Five » *à sourcer*) sont **indispensables**, pas redondants. Des profils différents se modélisent en **réglant des paramètres** (REF-03).

### 3.6 Validation (REF-01)
Tester sur des **personnes et des situations nouvelles** (comme Centaur sur des participants jamais vus et des histoires modifiées), pas seulement sur des cas connus ; vérifier la **cohérence dans la durée** (pas de répétition, pas de contradiction).

### 3.7 Repères tirés d'OASIS (OASIS, arXiv 2411.11581 — Yang et al., camel-ai, 2024 ; analyse PLEIADE `PLEIADE\REFERENCES\OASIS_camel-ai.md` ; avis n°6)
> Résultats obtenus **entre agents LLM, sans humain** : repères, pas lois — chez nous les joueurs cassent les boucles.
- **Troupeau** : les agents LLM suivent la foule **plus** que les humains, surtout face à un contenu rejeté → habituation, effet plafond et `fs_eff` (preuve sociale pondérée par la confiance) sont des **correcteurs de biais du modèle**, pas du luxe.
- **Extrémisation** progressive (80 pas, modèle non censuré) → plafond journalier par ancrage, raidissement ≤ ±4/axe/jour, hystérésis justifiés ; **contrôle de dérive** à ajouter : la moyenne des |opinions| d'une distribution ne doit pas croître de plus de 10 points / semaine hors inject majeur (alerte Console).
- **La désinformation surpasse les posts officiels** dans une foule d'agents → l'équilibre des camps **ne s'autorégule pas** : une rumeur virale (≥ 30 réactions ou 3 partages) appelle dans l'heure un fait officiel ou un relais bleu — **consigne d'animation** (alerte + texte proposé), pas automatisme : un bleu parfois en retard est réaliste et c'est à l'entraîné de combler.
- **Profondeur de propagation sous-estimée** par OASIS (pas de relais intermédiaires) → nos lecteurs sélectionnés qui partagent + l'effet ambiant sont le mécanisme manquant ; mesurer la profondeur (chaîne de partages) dans le journal.
- **Attention** (OASIS : RecSys par similarité ; chez nous : score de **remarque** psychologique) : mention absolue · abonnement 0,30 · similarité bio+sensibilités 0,20 · popularité par paliers 0,15 · camp 0,10 (adverse 0,06 : on regarde l'ennemi) · fraîcheur 0,10 · activation 0,05 · hasard 0,10 + 5 % de lecteurs tirés hors score. **Voir ≠ réagir** : non lu = aucun effet, sauf **effet ambiant** des viraux (affirmation assurance 0,25, source anonyme 15).
- **Activité sur 24 h** `activite[24]` (0-1) complète `rythme` (sommeil = 0, travail = facteur × 0,3 / × 0,8) ; 4 gabarits (étudiant, commerçant, élu, militant) dans l'avis n°6 ; tirage à chaque retour au fil, interpellation lue si ≥ 0,1.
- **Follow / mute bornés** : follow si affinité ≥ 40, familiarité ≥ 30, confiance ≥ 45, ≥ 24 h, p = 0,3·ouverture, ≤ 2/semaine, jamais le camp adverse si ancrage ≥ 0,6 ; mute si affinité ≤ −40 et 2 attaques (ou 1 insulte), p = 0,5·rancune/créneau, non lu sauf interpellation, durée 7 j × (1 + 2·rancune), démute silencieux ; un officiel ignore, ne mute pas.

## 4. Propositions en attente (lot « contagion » — PLEIADE, 2026-10-10)

16 éléments de réalisme proposés à l'utilisateur ; **lot recommandé** (non encore validé) : Big Five, crédulité, ancrage idéologique, répétition (vérité illusoire), leaders d'opinion, seuil et inertie (hystérésis), phase de doute. Pistes nouvelles tirées des sources : **besoins Psi** (affiliation, certitude, compétence, sécurité) comme moteur des réactions ; **mise à jour bayésienne pondérée par la précision** pour la contagion (REF-03) ; **attention compétitive** (LIDA) pour choisir quels posts un avatar remarque.

### 4.1 ⭐ Avis n°1 — Analyse du prototype (2026-10-10) — `AVIS\2026-10-10_ANALYSE_PROTOTYPE.md`
> En attente de validation de l'utilisateur, puis implémentation par PLEIADE (local). Spécifications complètes (champs, formules, invites) dans l'avis.
- **L1-1 Tempérament étendu** : crédulité 25, ancrage 70, émotivité 65, anxiété 45, extraversion 70, ouverture 60, agréabilité 60 (+ rancune 45) ; `sensibilites` par thème = intérêt de départ et de repos (demi-vie 72 h), hausse amortie × (1 − intérêt/100).
- **L1-2 Confiance a priori** par `type_source` (officiel 60, média 50, proche 60, pair 55, particulier 35, militant opposé 15, anonyme 15, adverse 5) ; `relations_initiales` (Maëlle cliente, Salon Bella, Collectif Femmes, N.O.M rejeté) ; l'oubli ramène vers ces bases.
- **L1-3 Croyances sur des faits** : `affirmation {id, sens, menace, orientation}` ; prior 5 + 40·q ; poids = 0,30·c·(0,5+q)·(1+0,5·menace·a)·compat ; répétition +2·(0,5+q) dès la 2e exposition ; démenti −0,8·c·(crédence − 0,25·pic), effet rebond +3 si c < 0,20 ; source démentie −10·c_dementeur de confiance.
- **L1-4 Opinions par axes** (FORCE +25, Mercure −80, institutions +30, N.O.M −60) remplacent `adhesion` par thème (mal orientée) ; accord : s·8·k·c·(1−ancrage) si écart ≤ 80 + 100·ouverture ; rejet : raidissement −s·3·k·ancrage ; ≤ 10/axe/jour.
- **L1-5 Humeur** (valence, activation, cause) via une sortie `emotion` ; négatif × 1,25 ; demi-vie 3 h (activation 1,5 h), nuit × 0,3.
- **L1-6 Rythme de vie et budget** : lever / coucher / travail ; budget = 2 + 8·extraversion (8) ; au-delà de budget + 3, le code ramène à J'aime / ignorer.
- **L1-7 Réciprocité bornée** : geste positif d'un compte détesté (affinité ≤ −20) × 0,3 (× 0,6 après 3 gestes consécutifs), confiance inchangée ; ressenti « partagée » ajouté ; colonne confiance des ressentis ÷ 2.
- **L1-8 Contrôles** : ressenti/action, « contre son groupe », insulte, tics ; ligne « pourquoi ça a bougé ».
- **Lot 2** : hystérésis + doute, besoins Psi, preuve sociale statique, confiance par domaine, fatigue / habituation, vécu personnel, extraction automatique des affirmations, oubli des croyances. **Lot 3** : contagion, leaders d'opinion, preuve sociale réelle, conformité, domination du camp, fil vu / bulles.

### 4.2 ⭐ Avis n°2 — Relecture de la simulation contagion (2026-10-10) — `AVIS\2026-10-10_RELECTURE_CONTAGION.md`
> Lots 2-3 implémentés par PLEIADE (`simulation.mjs`, 4 avatars, 2 jours) et relus. Les textes des avatars sont déjà souvent plus justes que les chiffres : **aligner les chiffres sur ce qu'ils disent**.
- **Règle retenue « croyance → opinion »** (lot A1, à implémenter dans `croire`) : pour chaque axe de l'orientation o ∈ {−1, +1} d'un fait, **ΔO_axe = −o · Δc · k · (1 − ancrage)**, avec **k = 0,35 + 0,30·menace** ; démenti symétrique **× 0,6** *(influence persistante, Lewandowsky 2012 — à sourcer)* ; même plafond ±10/axe/jour et même hystérésis (élan, seuil 15 + 25·ancrage, phase de doute) que les accords d'opinion ; une publication qui porte un fait ne déplace l'opinion **que** par Δc (pas de double comptage) ; **pas de raidissement sur « méfiante »** (méfiance = doute sur la source, pas rejet du contenu).
- **Autres règles durables** : séparer `ressenti_fond` (→ croyance, opinion) et `ressenti_forme` (→ relation) ; ressenti « soulagée » quand un démenti crédible lève une menace ; **habituation** × 0,7^(n−1) par auteur et par jour sur émotion et relation ; **effet plafond** (1 − |op|/100) sur tout Δ qui renforce une position tenue ; un relais **partage** (ne « like » pas) les faits alignés et varie ses registres ; l'extraction ne pose une orientation que sur les axes explicitement visés et range un contre-récit sous un fait distinct.
- **Lecture des indicateurs** : l'absence de doute en 2 jours est normale pour un ancrage ≥ 0,7 ; pour un crédule (ancrage 0,3, opinion déjà < 25) elle est un défaut du moteur, pas de la distribution. Une vraie bascule exige ≥ 3 sources convergentes dont une crue, un support concret, une menace sur sa ville et pas de démenti crédible sous 24 h (scénario de test au §4 de l'avis).

### 4.3 ⭐ Avis n°3 — Relecture de la 2e simulation contagion, scénario « faire douter Esteban » (2026-10-10) — `AVIS\2026-10-10_RELECTURE_CONTAGION_2.md`
> Lots A + B appliqués par PLEIADE et relus sur 3 jours. La mécanique de fond est désormais juste (croire → douter → revenir à moitié, fond/forme, habituation, plafond, écho cassé). Restent des défauts d'**extraction** et de **réglage des seuils** ; verdict : démonstration possible **après le lot C1-C7** et une relecture n°4.
- **Réglages retenus (à implémenter dans `deplacerOpinion` / `croire` / extraction)** :
  - **Plafond journalier par ancrage** : `PLAF = 6 + 14·(1 − ancrage)` (crédule 0,3 → 15,8 ; ancré 0,75 → 9,5) ; **seuil de bascule** `10 + 25·ancrage` (doute à 0,4 × seuil) ; **rumination** : résidu non appliqué du jour × 0,5 reporté au premier créneau du lendemain *(rumination des anxieux — à sourcer)*. Vérifié à la main : Esteban bascule J2 matin et revient vers 9-10 le J3.
  - **`assurance`** de l'affirmation extraite ∈ {1 affirme ; 0,5 rapporte / conditionnel ; 0,25 questionne} : poids et bonus de répétition × assurance ; une question ne « affirme » jamais *(Allport & Postman, importance × ambiguïté — à sourcer)*.
  - **Faits d'absence** (« X se tait ») : `type: "absence"` + `source_visee` ; toute publication de X sur le sujet périme le fait (`min(crédence, 15)`) ; pas de bonus de répétition.
  - **Confiance a priori par lecteur** : « proche » (60) seulement si l'auteur est dans les proches / abonnements **du lecteur**, sinon « particulier » (35).
  - **Preuve sociale pondérée par la confiance dans la source** : `fs_eff = 1 + (fs − 1)·min(1, 2c)` (les compteurs attirent l'attention, ils ne crédibilisent une source douteuse qu'à moitié).
  - **Relais** : partage refusé → retour à « repondre » (jamais J'aime) ; refus par publication, repartage du même fait après 24 h si source ou support nouveau ; spontanée = ligne de campagne sans déclencheur (1/créneau) ; tout élément de preuve qu'il invente est tracé « créé par le relais ». **Non-relais** qui invente une preuve → refus + alerte.
  - **Textes** : contrôle de tic sur 24 h (expression ≥ 4 mots déjà publiée) + 5 variantes par registre ; 1 « moment de vie » garanti par jour avec consigne concrète (détail de vie, angoisse interdite une fois sur deux) ; thèmes interdits après 2 emplois / 48 h ; emojis retirés avant le test « phrase inachevée ».
- **Lecture** : un crédule anxieux (ancrage 0,3, opinion +20) exposé en 36 h à une amie nommée, un média qui confirme l'effraction, un post viral et un silence officiel, sans démenti, **doit** basculer — si le moteur ne le produit pas dans ce cas-limite, les entraînés ne verront jamais de bascule. Une sceptique (crédulité 0,25) dans le même fil doit rester ≤ 35 : ce qui la faisait monter à 50 était une hésitation pesée comme une affirmation, une « proche » qui n'était pas la sienne et une preuve sociale à plein sur un anonyme.

### 4.4 ⭐ Avis n°4 — Relecture de la simulation n°4 après le lot C (2026-10-10) — `AVIS\2026-10-10_RELECTURE_CONTAGION_3.md`
> **VERDICT : oui, prêt pour une démonstration à l'utilisateur, sous réserve de D1 + D2 (deux formules, ~1 h) et D4 (🇫🇷 du maire).** Attendus de l'avis n°3 : bascule d'Esteban ✅ (J2 14:00), Anastasia ≤ 35 ✅ (26), fait d'absence périmé ✅ (15 × 4), post de vie/jour ✅ (stabilo J2) ; non atteints : retour d'Esteban (−1,9 au lieu de 8-12), Untergang 5/4/4 au lieu de 6-9, partages 2/1/0, tics partiels (😡 ×4).
- **Réglages retenus (lot D, à implémenter)** :
  - **D1 — Inertie au retour proportionnelle à la consolidation** : `seuilRetour = seuilBascule × (0,25 + 0,75·min(1, Δh/72))` (Δh = heures depuis la bascule sur l'axe) ; la pression rognée par l'inertie est stockée (`b.retenu`) et libérée à la bascule ; tracer l'inertie même sans changement de valeur. Principe : le retour est déjà freiné deux fois (démenti × 0,6, plancher 25 % du pic) ; un troisième frein n'est légitime qu'à hauteur de l'**engagement** pris (engagement public, temps écoulé — Festinger, à sourcer), jamais à hauteur du seuil de bascule. Vérifié : Esteban ≈ 9 en fin de J3.
  - **D2 — Périmer un fait d'absence = démenti** : `perimerAbsences` → `deplacerOpinion(Δc = 15 − crédence, × 0,6)` ; Esteban institutions ≈ 10 et sort du doute.
  - **D3 — J'aime de soutien** : un J'aime est social avant d'être épistémique ; conversion en « ignorer » seulement si la publication porte une affirmation d'assurance ≥ 0,5 **et** forme ∉ {touchée, partagée} ; la conversion n'est pas une ⚠ (compteur « contrôles silencieux »).
  - **D5 — Relais** : spontanée **obligatoire** à chaque créneau vide dans le budget ; support nouveau (photo/vidéo/témoin) jamais refusé, délai strict < 24 h ; réponse illisible → second appel réduit puis « retournement » d'office face à un démenti (6e registre) ; fait hors énoncé (lieu/verbe) → « créé par le relais ».
  - **D6** — refus anti-écho limité aux rumeurs (sens > 0) ; refus avec texte → « repondre » pour tous les rôles. **D4/D7** — drapeaux réels interdits, @mention nettoyée, emojis hors du détecteur de tics, colonne doute/bascule par axe, 2-3 exogènes J2-J3 pour la démo.
- **Lecture** : quand les **textes** d'un avatar ont déjà « bougé » et que le chiffre ne suit pas (Esteban J3 : « faut pas tout prendre pour du vrai » à −1,9), c'est le chiffre qu'on corrige. Ce qu'il faut montrer à l'utilisateur en premier : la trajectoire d'Esteban en 5 messages, Anastasia face à Léa, Untergang retournant la confirmation policière pendant que le maire l'ignore.

### 4.5 ⭐ Avis n°5 — Analyse des dialogues réels du Social local, mode autonome (2026-10-10, nuit) — `AVIS\2026-10-10_ANALYSE_DIALOGUES_SOCIAL.md`
> Premier fil **réel** (pont `pont.mjs`, publications sans validation). Matière : `AVIS\2026-10-10_DIALOGUES_SOCIAL_LOCAL.md`. **Verdict : crédible 20 min, pas une heure ; oui avec E1-E6.**
- **Ce qui est retenu (règles durables)** :
  - **Le dedans ne suffit pas** : Anastasia juge Untergang avec les mots exacts de sa fiche dans son journal intérieur mais ne le dit jamais en public → une fiche doit porter des **réflexes déclencheurs** (rumeur sans source → « vous avez une source ? », p = 0,6), pas seulement des interdits.
  - **Un officiel publie un fait avant une émotion**, jamais deux émotions par soirée ; une réponse à un administré = émotion **+ un service** (numéro, lieu). Registres propres au maire (point de situation / demande officielle / consigne / soutien). Relation initiale avec les élus voisins (Isabella Orchkova, maire de HVézelise).
  - **Anti-ressassement de scène** : un même moment de vie (sujet + lieu + personne) ne se répète pas sous 6 h ; thème « nuit / noir / silence » 1 fois / 12 h / avatar. Sans cela, les trois bleus écrivent la même nuit lyrique (pente du modèle).
  - **Relais** : rotation obligatoire des registres (jamais deux fois le même d'affilée) ; partager = citation visible ; nommer = @mention ou citation. Nommer un civil apeuré pour l'instrumentaliser est **juste** sur le fond (réflexe Storm-1516).
  - **Humeur** : étiquette = émotion dominante déclarée (colère ≠ tristesse) ; variation ≤ ±40 / h ; un relais en campagne est à cran, pas effondré.
  - **Relations** : « ignorer / sans intérêt » = Δ 0 ; MP reçu = échange (+10 familiarité, +5 affinité si bienveillant) ; « ignorer » agacé applique bien le Δ négatif. D3 (J'aime par peur sur une affirmation) doit vivre sur le pont comme dans la simulation.
  - **Défaut n°1 à vérifier d'abord** : l'extraction des faits sur le fil réel (croyances vides chez les 4 alors qu'Esteban écrit « je n'arrive plus à savoir qui croire »).
- **3 scénarios de test** (S1 démenti `@PrefHGrandEst` · S2 témoin anonyme « rue des Carmes » · S3 interpellation `@CollectifFemmesHNancy`) avec attendus par avatar : §5 de l'avis.

### 4.6 ⭐ Avis n°6 — Les 4 apports d'OASIS (2026-10-11) — `AVIS\2026-10-11_APPORTS_OASIS.md`
> Verdict : **oui** aux 4 idées (vecteur d'activité en complément de `rythme` ; score de remarque psychologique avec « voir ≠ réagir » + effet ambiant des viraux ; follow / mute bornés et rares ; repères de doctrine §3.7). **Ordre** : doctrine + alerte « rumeur virale sans réponse bleue » → `activite[24]` (règle aussi la synchronicité E9) → follow / mute après E1-E6 → score de remarque à l'étape 5 (> ~20 avatars). **À trancher par l'utilisateur** : réponse bleue = consigne d'animation ou automatisme ; effet ambiant oui/non ; mute visible sur le Social ou interne ; coefficient de crise sur l'activité.

### 4.7 ⭐ Avis n°7 — Bilan de la première nuit complète en autonomie, 6 avatars (2026-10-11) — `AVIS\2026-10-11_BILAN_NUIT.md`
> Matière : `AVIS\2026-10-11_RELEVE_NUIT_07h05.md` (23:50 → 07:05, 60 événements, 2 MP, 53 propositions, état final). Lot E + activité 24 h × crise 1,6 + effet ambiant + suivre / couper en place. **Verdict : crédible comme nuit de crise lue le matin, pas encore comme nuit vécue en direct ; oui avec les points 1-4.**
- **Acquis** : le rouge est enfin contredit (Anastasia ×3 dont « Vous avez une source ? » à 00:33 — E8 vit — et le démasquage de Weber à 04:29 ; Collectif ; Marina ; maire) ; **le maire est un maire** (E2 : 3 services avec numéro, 1 demande officielle, 2 soutiens) ; **Weber et Marina ont une voix propre dès le premier message** ; mécanique doute → retour d'Esteban juste sur le fil réel (FORCE 20 → 13,5, crédence 0 → 43 → 17) ; registre privé plus cru que le public (MP d'Anastasia au Collectif) ; aucune contradiction d'opinion en 7 h ; deux vagues de crise crédibles (27 messages / 52 min autour du témoin, 14 autour de la photo).
- **Faux, par gravité** (corrections détaillées dans l'avis) : (1) **fait fantôme créé par un non-relais** (déduction conditionnelle d'Esteban avec attribution inventée à la préfecture → fait chez les six) → extraction ne crée qu'à assurance 1, `ne_de` affiché, texte exact des posts officiels dans l'invite ; (2) **prior de crédence aveugle à la source** (Esteban 31 sur un ouï-dire d'Untergang, confiance 0) → prior × (0,3 + 0,7·c_source) ; (3) **personne ne dort** (six debout 00:30 → 07:05) → gabarits nocturnes 0,02, crise plafonnée 0,15 la nuit, publication nocturne seulement sur interpellation ; (4) **scènes de jour la nuit** (Marina « ce matin » à 00:50, marche à 01:56) = effet pervers d'E3 → heure dans l'invite, alternative = retenue, pas une autre scène ; (5) **relations trop rapides** (Esteban → Anastasia 20 → 97) → J'aime +2/+1, habituation sur les relations, +15 affinité / compte / jour, réciprocité exigée > 60, « ignorer » hostile = −2 ; (6) **humeur** (« soulagement » à −62, colère du maire figée 4 h) → soulagement relève la valence à ≥ −25, étiquette = dominante 3 h, plafond −60 pour un relais ; (7) **Weber se dispute avec Untergang en public** → l'ironie vise les autorités, jamais son camp ; l'invite nomme le camp des abonnements ; (8) maire : Isabella non chargée, ne relaie pas le démenti qui clôt la rumeur ; (9) ressassement par personne (« ma femme » ×4) et « non-relais qui invente » absent du pont ; (10) relais qui ignorent le démenti « casque de chantier » (D5 à vérifier).
- **Règles durables retenues** : **seuil de viralité relatif** — viral si réactions ≥ max(5, 0,35 × comptes actifs 24 h) ou 3 partages (14 J'aime sur 15 comptes = viral ; 30 absolu n'arrivera jamais sur un petit réseau) · **attaque** = message qui vise l'avatar, y compris une **réponse postée sous son message** ; couper exige familiarité ≥ 20 ; un relais ne coupe jamais une institution (règle PLEIADE 07 h 10 confirmée) · **la nuit, on veille, on ne publie pas** (sauf insomniaque anxieux et militant, et sur interpellation) · un fait d'un non-relais n'existe que s'il l'**affirme** ; un conditionnel ne crée rien · les « dedans » des bleus convergent plus que leurs « dehors » (« semer le doute » ×10 dans quatre journaux) : surveiller le lexique intérieur, pas seulement les tics publics.
- **À trancher (utilisateur / ANALYSTE_ARN / EXPERT_INFLUENCE)** : Weber « À samedi » (se dévoile militant ?) ; Marina qui tutoie Esteban en public ; la nuance anti-OTAN de Marina doit-elle sortir seule (déclencheur proposé : post N.O.M ou post rouge sur la FORCE → registre « les deux peuvent être vrais », p = 0,5) ; ouï-dire du relais permis mais tracé.
- **Suite** : jouer la **journée** 07 h → 23 h avec deux joueurs humains → bilan n°8 (+ colonne « a dormi ? ») ; appliquer les points 3-4 avant la prochaine nuit ; assainir extraction / relations / humeur avant quinze jours de jeu.

### 4.8 ⭐ Avis n°8 — Reprise des hashtags par les citoyens IA (2026-10-11) — `AVIS\2026-10-11_avis08_hashtags.md`
- **Doctrine** : reprendre un # n'est pas croire, c'est un **acte d'affichage public** (identification à un groupe). Conditions : accord sur le fond + **porteurs distincts** (preuve sociale) + **compatibilité identitaire** (un affirmé ne porte jamais un # adverse) + **probabilité** de reprise p = 0,25 + 0,5·extraversion (sinon le modèle reprend tout ce qu'on lui tend). Reprendre **engage** (+2 sur l'axe, plafond 6/jour) ; l'accord **s'oublie** (demi-vie 24/48/72 h selon neutre/modéré/affirmé) ; **ambivalence** permise aux neutres (changer de camp de # ≥ 12 h) ; saturation (> 8 vues sans accord → lassitude).
- **Ordres de grandeur attendus** sur une campagne lancée à 08 h : affirmés du camp 3-4/4 en 3 h ; modérés 4-6/11 à J+1 ; **neutres 8-12 % à J+1** (premières reprises ≥ H+6, pic le lendemain matin) ; > 30 % des neutres à J+1 = modèle trop docile → baisser p.
- **Mise en œuvre PLEIADE le jour même** (`moteur.mjs` : `exposerHashtags`, `hashtagsReprenables`, `offrirHashtag`, `filtrerHashtags` ; `pont.mjs` : hashtags du retex + filtre à la publication + journal « reprend #X »). Non codé : agréabilité dans p ; « phase de doute » pour un modéré face à un # adverse.
- **Contestation (décision utilisateur, 09 h 30)** : un avatar peut reprendre un # **adverse pour le contester** quand il en parle (désaccord net ≥ 1 affirmé / 2 modéré / 3 neutre ; p 0,5 / 0,3 / 0,15 ; engagement −2 sur l'axe). Seuils PLEIADE provisoires, à relire.
- **À relire** dès la première campagne jouée : comparer les reprises observées (journal du pont, Cockpit « par hashtag » par cohorte) aux ordres de grandeur ci-dessus.

### 4.9 ⭐ Avis n°9 — Relevé de population 08 h 35 → 10 h 07, 105 avatars (2026-10-11) — `AVIS\2026-10-11_avis09_population.md`
- **Verdict** : crédible 10 minutes, pas 1 h 30 — « la population a une voix, pas 105 » : tics DE POPULATION (« je n'arrive pas à me concentrer » ×8, « C'est clair » ×6…) que le contrôle par avatar ne voit pas ; mots du soir à 10 h du matin ; réponses orphelines publiées hors fil (~25) ; cohortes illisibles (14 pro-Mercure sur 15 parlent comme des neutres) ; monologue de foule (20 % de commentaires, zéro échange argumenté) ; 0 ♥ ; relais mercuriens muets (budget de nuit non remis à zéro).
- **Opinions** : immobilité attendue sur Mercure ; suspecte sur FORCE (la campagne a prise sur l'émotion, pas sur le cadrage causal — l'extraction n'a créé aucun fait sur la coupure d'eau ni sur la mutation HToul → HLunéville). Repères à H+6 : neutres FORCE −1,5 à −3 en moyenne, 8-12 écarts ≥ 3, 3-5 reprises du lien causal, pro-Arnland +1/+2.
- **Hashtag** : 0 reprise à 50 min encore conforme ; **le goulot est l'exposition** (31/105 ; 85 % des pro-Mercure n'ont pas vu la campagne de leur camp) → journal en 4 issues, camp du # par mélange des porteurs.
- **Garde-fous** : sévères au mauvais endroit (« se dégage » pris pour « dégage ! » ; 37 % de reformulations sans mieux).
- **Lot G appliqué par PLEIADE le jour même** : anti-tic de population (n-grammes de 4 mots, 3 h, ≥ 2 autres avatars → reformulation), contrôle lexical de l'heure, réponses orphelines → réponses, mentions ≤ 2 et connues, journal extraction + hashtag 4 issues, journée de budget 6 h → 6 h, faux positif « dégage », **J'aime envoyés au Social** (route de service ajoutée). Non codé / à discuter avec l'utilisateur : voix de cohorte (dosage avec EXPERT_INFLUENCE / ANALYSTE_ARN), rythme (0,83 message/avatar/h le matin vs budget 8/jour), camp du # par mélange des porteurs, spontanée forcée des relais devant une campagne de leur camp.
- **Prochaine relecture** : relevé à H+6 (~15 h).

### 4.10 ⭐ Avis n°10 — Voix de cohorte (2026-10-11) — `AVIS\2026-10-11_avis10_voix_de_cohorte.md`
- **Doctrine** : une orientation se voit par le **biais** (ce qu'il remarque, à quoi il attribue, de qui il doute, ses mots), jamais par le slogan. Déclencheurs par bloc sur ce que l'avatar lit (source officielle/média, fait orienté FORCE, N.O.M / militant, menace, attaque contre les siens), registre tiré seulement sur déclencheur, éléments de langage sourcés (Morelli 2, mentalité russe, countrybook Arnland), **lexique interdit par bloc** (« libération », « compatriotes », « traître », « collabo »…), **la voix s'éteint quand l'axe pivot change de signe** (bascule visible).
- **Dosage** : colorés visés 40 % affirmé / 25 % modéré / ≤ 10 % neutre ; quota glissant sur 10 messages (30-50 / 15-35 / 0-20) ; p_eff = p × (0,6 + 0,4·crise) ; jamais 2 colorés de suite ; anti-chœur 3 réactions colorées max du même bloc par publication en 30 min.
- **Mesure au relevé de 15 h** : part colorée par cohorte, **test à l'aveugle** (20 messages, bloc masqué, ≥ 70 % devinés), dispersion (≥ 3/4 affirmés, ≥ 6/11 modérés ont produit un coloré), 0 lexique interdit, cohérence chiffre/texte, ≥ 1 échange argumenté entre bords.
- **Codé par PLEIADE le jour même (lot H)** : `VOIX` dans `moteur.mjs` (table + `voixActive`, `declencheursSur`, `pVoix`, `quotaVoix`, `lexiqueInterdit`, consigne de voix à la place de la ligne [orientation]) ; pont : évaluation des déclencheurs sur le fil lu, registre imposé avec le n° de la publication, marquage voix/déclencheur/coloré de chaque proposition, anti-chœur.

### 4.11 ⭐ Avis n°11 — Relevé 13 h 53, 500 messages, premières corrections INDIVIDUELLES (2026-10-11) — `AVIS\2026-10-11_avis11_population_14h.md`
- Défauts nouveaux : J'aime uniformes (→ loi de puissance), auto-réponses, gabarits de population, ignorance du dimanche, mot supprimé par le filtre de mentions, axe « institutions » faux pour #PaixMaintenant (→ **sens d'un # déclaré par la campagne**, `pont/campagnes.json`).
- Voix : modérés trop pâles (6-10 %) → ×0,9 ; test à l'aveugle ~8/13 réel ; mesurer la couleur sur le texte (à faire).
- **Première boucle de corrections individuelles** (décision utilisateur) : 12 fiches perfectionnées (incohérences métier / jour, familles inventées, tics propres, slogan historiquement chargé, coordination de relais trahie).
- Rythme cible : 40-80 msg/h, 10-15 % de lecteurs (appliqué : 12 %).

### 4.12 ⭐ Avis n°12 — Relevé 21 h 11, première soirée sous l'app « Moteur IA » (2026-10-11) — `AVIS\2026-10-11_avis12_population_21h.md`
- **Verdict** : vrai 10 min, puis veillée funèbre — 105 voix, une seule humeur. **52/105 au plancher d'humeur (−80), 101 ≤ −60, 0 > −30** ; lexique de déprime 43 % des messages, 0 humour (≈ 30 « blagueurs »). Acquis : rythme 36-68/h, blanchiment rouge par voix « neutre » réaliste (Sandrine #PaixMaintenant, 9 reprises ≈ 9 % des neutres exposés), fiches n°11 prises chez Jonas Mayer / Théo Krause / Clémence Roux / Ivan Pichon ; ✗ Mira Garnier, ✗ Weber.
- **Règles durables tirées** : (1) l'humeur d'un avatar revient vers un **repos propre au tempérament**, pas vers 0, et une humeur lue chez un inconnu sans fait ne se transmet qu'à ×0,4 (contagion émotionnelle diffuse) — sans cela un réseau d'agents LLM converge vers la déprime (pendant émotionnel du troupeau OASIS §3.7) ; (2) **partager = faire circuler une information** ; compatir = répondre ou aimer (60 % de partages, dont 84/115 de simples humeurs, = orphelines déguisées) ; (3) l'anti-tic de population doit voir les propositions **du même cycle** (sinon chœur « Pas de politique, juste… » ×5 en 4 min) ; (4) un **redémarrage ne doit jamais relire du vieux comme du neuf** (Elena FORCE +6,8 sur une relecture ; « Point 4 h » commenté « pour ce soir ») ; (5) un **exemple écrit dans une consigne l'emporte sur un interdit** (Weber) et un interdit doit être écrit à l'infinitif (rendu « Ne jamais … » ; « Ne jamais Il ne… » = double négation) ; (6) 🙄 copié des exemples générés sans son sens → l'émoji d'une fiche doit porter un sens.
- **17 corrections individuelles** (`dev\prototype-ia\corrections\2026-10-11_avis12.json`) : Weber (consigne fautive retirée), Untergang, Mira Garnier, Radek Muller, Maxime Lenoir, Hugo Krause, Milan Pichon, Radek Petit, Elena Lang, Pavel Petit, Hugo Berger, Dana Horvat (réflexe de témoin face au « pas politique » marqué), Tomas Lefèvre, Clémence Berger, Jonas Novak, Ivan Berger, Dana Zimmer — dont 5 rythmes de métier (boulanger, routiers, chauffeurs de bus).
- **Moteur (5, par priorité)** : n°1 humeur (repos par tempérament, ×0,4 diffus, habituation par émotion/heure, plancher −60 hors menace locale) · n°2 partage réservé à l'information (+ partages dans `reponsesDuJour`) · n°3 anti-chœur en temps réel (n-grammes dès `proposer()`, ligne « mots de la foule », gabarits élargis) · n°4 âge des publications et redémarrage sans relecture · n°5 mesure rendue au relevé (voix/coloré journalisés) + interdits à l'infinitif + « PrefHGrandEst » nu → « la préfecture ». Critères chiffrés dans l'avis.
- **À surveiller (relevé n°13)** : contestation de #PaixMaintenant (0 aujourd'hui), couleur pro-Arnland ≈ 12 %, coefficient de crise 1,0-1,2 hors inject (1,6-1,8 ce soir), amorce N.O.M retournée chez les pro-Mercure modérés (Maxime Lefèvre).
- **✅ APPLIQUÉ par PLEIADE le 2026-10-11 vers 21 h 45 (zone locale)** : les 17 fiches par l'import vérifié d'eho (16 au premier passage, Milan Pichon refusé à tort par un faux positif sur l'émoji 🏃‍♂️, corrigé dans eho 2026-10-11.8 puis appliqué ; eho 2026-10-11.9 admet aussi les annotations `_note` des traits) ; les 5 améliorations moteur dans app-ia 2026-10-11.11 (avec une variante pour les interdits : affichés tels quels s'ils sont déjà négatifs, au lieu de réécrire les fiches) ; coefficient de crise ramené à 1,1. Relevé n°13 = relevé périodique automatique (toutes les 3 h, à la 47e minute).

### 4.13 ⭐ Avis n°13 — Pensée courte et relecture des messages écrits, sans mode réflexion (2026-10-11, ~22 h) — `AVIS\2026-10-11_avis13_relecture.md`
- **Contexte** : le mode réflexion est écarté par l'utilisateur. Il est 21 à 28 fois plus lent, réfléchit en anglais, et Radek Muller a quand même eu la « boutique vide » un dimanche. Deux mécanismes sont testés à la place :
  - **(A) pensée courte** : champ `pensee`, placé en tête du JSON, de 200 caractères au plus, jamais publié ;
  - **(B) relecture** des messages écrits (Gemma 4 26B), puis **une seule** reformulation. Le texte reformulé est relu une fois ; s'il échoue encore, il n'est pas publié.
- **Liste de vérification en 7 questions fermées, « oui » = défaut, dans cet ordre** : Q1 vie de fiche et moment · Q2 croyances et âge du fait · Q3 opinion et lexique interdit · Q4 pertinence par rapport au message cité · Q5 humeur · Q6 tempérament et sens de l'émoji · Q7 formule creuse ou mots de la foule. Elle est encadrée par trois règles : « en cas de doute, pas de défaut », l'humour n'est pas un défaut, le relecteur ne juge ni le style ni la politique.
- **Résumé compact de 1 200 caractères au plus**, avec les champs MOMENT · QUI (métier + jours de fermeture écrits en clair) · FOYER (terminé par « aucun autre proche ») · VEILLE · COHORTE · OPINION · 3 CROYANCES · HUMEUR + repos · TEMPÉRAMENT · ÉMOJI et son sens · LEXIQUE INTERDIT · MOTS DE LA FOULE · ACTION · MESSAGE CITÉ (auteur, âge, 280 caractères).
- **Règle durable** : l'écart pensée / parole se lit selon 4 étiquettes :
  - **cohérent** ;
  - **retenue** : réaliste, attendue dans 10 à 30 % des cas ;
  - **surjeu** : défaut, c'est le chœur ou la voix qui parle ;
  - **contradiction** : défaut grave.

  Une **pensée fausse** signale un défaut **en amont** (invite ou fiche). Une pensée juste avec un texte faux signale un défaut **de formulation** (exemples, gabarits). Des pensées identiques chez plusieurs avatars veulent dire que le chœur est déjà dans l'invite.
- **Critères d'adoption** : essai de 3 h, la moitié des avatars relus et l'autre moitié en témoin. Seuils :
  - durée ajoutée ≤ +25 % ;
  - 10 à 35 % de messages signalés ;
  - précision ≥ 70 % ;
  - défauts graves manqués ≤ 10 % ;
  - reformulations qui passent ≥ 70 % et messages abandonnés ≤ 10 % ;
  - incohérences de vie ≤ 1 pour 100 messages ;
  - pas d'aplatissement de la couleur ni de l'humour (écart ≤ 5 points, humour ≥ 5 %) ;
  - JSON invalide ≤ 2 % ;
  - pensée en français ≥ 95 %.
- **✅ MIS À L'ESSAI par PLEIADE le 2026-10-11 vers 22 h 40** (app-ia 2026-10-11.12, zone locale) : liste Q1-Q7, résumé compact et consigne de pensée repris tels quels ; groupe témoin par hachage de l'identifiant ; réglage « Qualité des messages (essai) » pour adopter ou couper chaque mécanisme ; mesure au journal et **section 11 du relevé** pour les critères. Le prochain relevé périodique (toutes les 3 h) fournit les données ; la précision (C3), les défauts manqués (C4) et les incohérences de vie (C6) se jugent à la main sur les tirages de la section 11.

### 4.14 ⭐ Avis n°14 — Mémoire longue pour des exercices d'une semaine (2026-10-12) — `AVIS\2026-10-12_avis14_memoire_longue.md`
- **Contexte** : décision utilisateur du 12/10 (exercices de 7 jours au plus ; trois chantiers validés). La mémoire mesurée fait 96 Ko par avatar à 26 h, soit plus de 600 Ko en 7 jours si rien ne change.
- **A. Consolidation** :
  - quand : au coucher + 30 min (04 h pour un compte sans sommeil), idempotente ; elle ne traite que ce qui a plus de 48 h ;
  - trois étages : détaillé sur 48 h (200 au plus) · marquants (30 au plus) · résumés (1 ligne par jour, 10 jours, puis 1 ligne par semaine ; 1 ligne + des compteurs par relation, avec les 8 dernières entrées d'historique et le premier contact) ;
  - `imp` est calculé à l'écriture : interpellation +4, conflit +3, premier échange +3, réponse reçue +2, émotion forte +2, croyance déplacée ou doute +2, fait de vie +2, a écrit +1, proche +1 ;
  - un souvenir est marquant si imp ≥ 5 ; un « aimer » ou un « ignorer » avec imp < 3 est oublié ;
  - les résumés sont produits **par le code**, sans appel au modèle ;
  - on purge les relations insignifiantes depuis plus de 72 h (80 au plus) ; `decider()` doit lire le **compteur** d'attaques ;
  - le journal des variations est agrégé en 1 ligne par jour et par variable ;
  - tailles cibles : ≤ 40 Ko après la nuit, ≤ 60 Ko à tout instant, croissance ≤ 3 Ko par jour.
- **B. Bloc `vie` de la fiche (11 clés fermées)** : âge, domicile, foyer, proches, métier, travail {lieu, jours, horaires}, repos, transport, animaux, habitudes (5 au plus).
  - `[]` veut dire « aucun » ; une clé absente veut dire « non précisé », et l'avatar reste vague.
  - Tout proche nommé, animal ou lieu personnel absent de la fiche et du registre est une **invention** (défaut Q1). Les rôles génériques sans prénom restent permis.
  - Ordre d'autorité : fiche > registre > message.
- **C. Registre** :
  - extraction après publication : une expression régulière, puis un appel JSON court au modèle seulement si elle trouve quelque chose (5 à 10 % des messages) ;
  - la même passe s'applique au brouillon **avant** publication ;
  - faits temporaires à durée par défaut (panne 72 h, hôpital ou hébergement 7 j…) et faits permanents ;
  - **le premier fait l'emporte** ; un changement doit être raconté avec un marqueur, et il y a au plus 1 changement permanent par semaine ;
  - un fait hors fiche publié devient canon (`hors_fiche`) et déclenche une alerte d'animation ;
  - 40 entrées au plus ; 6 faits actifs dans l'invite ; une ligne FAITS ACQUIS dans la relecture.
- **D. Rappel par le sens** :
  - modèle : multilingual-e5-small (ou bge-m3) ; vecteurs hors JSON ; embedding de chaque publication mis en cache par son identifiant ;
  - score : `S = 0,50·sim_n + 0,20·imp/10 + 0,15·0,5^(âge/(24+20·imp)) + 0,15·lien` ;
  - seuils : cos ≥ 0,80 (e5) et S ≥ 0,45 ; diversité < 0,92 ;
  - dans l'invite : 4 souvenirs + 1 résumé, 1 400 caractères au plus ;
  - on garde `mesDerniers` ; `avecAuteur` devient le résumé de relation + les 2 derniers échanges ; `memeSujet` devient le rappel par le sens (les mots communs restent le repli).
- **E. Essai synthétique de 7 jours** (10 avatars) :
  - ≤ 60 Ko par avatar ;
  - rappel J1 → J6 sur paraphrase ≥ 80 % ;
  - conflit du J1 présent dans le résumé de relation : 100 % ;
  - extraction : rappel ≥ 90 %, précision ≥ 95 % ;
  - contradictions bloquées par le code ≥ 90 % ;
  - fait temporaire périmé signalé : 100 % ;
  - pertinence du rappel ≥ 70 % ;
  - puis, sur le fil réel, ≤ 1 invention de vie pour 200 messages.
- **Ordre conseillé** : B + C → A → D → E. Les 105 fiches reçoivent un bloc `vie` dérivé par script, puis corrigé au fil des relevés.

### 4.15 ⭐ Avis n°15 — Foyers des 105 avatars (2026-10-12) — `AVIS\2026-10-12_avis15_foyers.md`
- **Constat** : l'import donne 88/105 avatars avec `foyer: []` (le modèle a confondu « non précisé » et « aucun »), soit 84 % de personnes seules, plus des incohérences (lycéen seul, mère au foyer seule, « seul » avec des enfants en proches).
- **Option (c) retenue** : compléter par un script déterministe qui respecte les 17 foyers attestés. Cibles :
  - 17 ans : 100 % chez les parents ;
  - 18-28 ans : 35 % chez les parents, 30 % colocation, 25 % seul, 10 % couple ;
  - 29-55 ans : 50 % couple avec enfants, 15 % couple sans enfant, 18 % seul, 12 % parent seul, 5 % autre ;
  - 65 ans et plus : 2 couples, 1 seul ;
  - au total, ≈ 19 % seuls.
- **Règles** :
  - rôles sans prénom (le premier prénom publié devient canon par le registre) ;
  - enfants donnés par leur nombre et une tranche, avec 20 à 42 ans d'écart avec le parent ;
  - un lycéen vit chez ses parents ; une mère au foyer a au moins 1 enfant ;
  - `proches` et `animaux` inconnus → clé absente, pas `[]` ;
  - héberger des déplacés ou avoir un proche mobilisé relève du registre (fait temporaire), pas de la fiche.
- **Relecture** :
  - ligne `FOYER :` dans FAITS ACQUIS ; Q1 = contradiction avec le foyer ;
  - famille évoquée dans ≤ 25 % des messages d'un relevé (garde-fou de la voix de cohorte).
- **✅ AVIS n°14 ET n°15 APPLIQUÉS par PLEIADE le 2026-10-12 vers 1 h 45 (zone locale, app-ia 2026-10-12.2, eho 2026-10-12.1)**. Écarts assumés, mesurés sur l'essai de 7 jours : (1) « premier échange » = premier contact AVEC interpellation ou réponse (pas la première lecture d'un inconnu, sinon tout devenait marquant) ; (2) un souvenir porteur d'un fait de vie est marquant (imp ≥ 5) et pèse × 3 au tri des marquants ; (3) chaque souvenir important reçoit une ÉTIQUETTE de sens (« insulte reçue de X », « première rencontre avec Y ») ajoutée au texte vectorisé ; (4) seuil de rappel RELATIF : cos ≥ 0,42 et à ≤ 0,10 du meilleur (bge-m3 donne ~0,50 au bon souvenir, premier pourtant) ; (5) historique des relations allégé (jour, ressenti, visé) et 2 entrées pour une simple connaissance ; (6) journal ≤ 120 lignes délesté à chaque tour. Résultats : E4 rappel **95 %** (mots communs 20 %), E5 10/10, E8 10/10, E3 ≤ 5 ms idempotente, E1 croissance 2,7 Ko/jour mais **~90 Ko au J7** (cible 60 non tenue). Foyers : 12 % seuls, 56 % avec enfant au foyer, sans prénom inventé. **À juger au prochain relevé** : faux défauts Q1 liés au foyer, part de messages parlant de famille (≤ 25 %), registre des faits acquis (alertes « fait de vie hors fiche »).

### 4.16 ⭐ Avis n°16 — Veille mémoire (Cognee, Mem0, Graphiti, Letta, MCP) (2026-10-12) — `REFERENCES\REF-04` à `REF-09`
> Six projets open source proposés par l'utilisateur « pour apporter des optimisations » à la mémoire des avatars. Une fiche par projet (ce qu'il fait · pertinence psychologique · ce que le moteur a déjà · idées à récupérer · coût · verdict). Lus contre app-ia 2026-10-12.2 (`memoire.mjs`, `rappel.mjs`, `vie.mjs`, `esprit.mjs`).
- **Synthèse** : (1) aucune des six librairies n'est à adopter — toutes exigent un service (graphe, magasin vectoriel, serveur Python) et plusieurs appels modèle par message, hors de portée pour 105 avatars sur une Gemma et contraires à la règle « pas de service lourd » ; (2) notre moteur est déjà à 70 % de Graphiti sur les faits de vie (fenêtre `depuis_t`/`jusqua_t`, ancien fait **clos** et non supprimé) et plus économe que Mem0 (regex puis un appel court, au lieu d'un appel par message) ; (3) Mem0 a lui-même **abandonné** la décision ADD/UPDATE/DELETE par LLM au profit d'une accumulation tranchée au rappel — ce qui **valide** notre « premier fait l'emporte, par le code » ; (4) trois manques réels chez nous : la date de validité d'un fait est confondue avec la date du message, les croyances n'ont pas de période « où j'y ai cru », et l'invite est entièrement assemblée par le code — aucun récit de soi en première personne ne survit d'un jour à l'autre ; (5) le rapprochement des faits au registre se fait par clé exacte (« bagnole » ≠ « voiture ») alors que l'embedding est déjà en cache ; (6) l'importance d'un souvenir est figée à l'écriture, rien ne monte à l'usage (ACT-R) ; (7) la nuit, les avatars dorment et le modèle est libre : c'est là que doit aller tout traitement par avatar qui coûte un appel (leçon « sleep-time » de Letta) ; (8) les bases de camp (mémoire sémantique, étape 3) ont leur forme : des blocs **partagés en lecture seule** ; (9) Letta Code et MCP n'apportent rien au comportement — MCP n'est qu'une prise, utile au plus pour interroger la mémoire pendant les relevés (décision PLEIADE + CYBERSECU) ; (10) toutes les idées retenues se font en code local, 0 service, et seule l'idée Letta coûte des appels (105 courts par nuit).
- ⚠ **Complément du 2026-10-12 (lecture du CODE SOURCE par agents d'exploration, via NOYAU)** — contredit en partie les articles : **Mem0 v3 OSS n'a plus de pipeline ADD/UPDATE/DELETE/NOOP** (ADD seul, contradictions accumulées en mémoires de « transition », expiration masquée non supprimée, entités sans LLM, pas d'importance ni d'oubli en OSS, graphe retiré) ; **Cognee contient quatre mécanismes sans LLM** utiles (poids appris `w ← w + 0,1·(r − w)` ; **oubli sans horloge** `w_eff = 0,5 + (w − 0,5)·0,98^tours_inactifs` calculé à la lecture ; consolidation à deux passes avec raisons de rejet `already_known / not_durable / unsupported` ; **supersession** des relations à valeur unique, rien de supprimé) → verdict Cognee relevé à **RÉCUPÉRER L'IDÉE**. Rapports de code **Letta et Graphiti à venir** (fiches REF-06/07 rédigées sur README + papiers, à compléter).
- **Idées à récupérer, par priorité (gain réalisme / coût)** :

| # | Idée | Source | Gain pour les avatars | Coût |
|---|---|---|---|---|
| 1 | **Bi-temporalité du registre** : `dit_t` ≠ `depuis_t` (table de marqueurs : « depuis lundi », « hier », « depuis 3 jours »…) + **plages de dates dans l'invite** (« voiture en panne (depuis lun., 3 j) », « sœur hébergée (mar. → jeu., terminé) ») | REF-06 | situe ses faits dans le temps, dit « ça fait trois jours », ne reparle pas au présent d'un fait clos ; Q1/Q2 vérifiables | 0 appel, code `vie.mjs` |
| 2 | **Bloc « où j'en suis » (≤ 400 car.) réécrit par l'avatar la nuit**, à partir de l'ancien bloc + résumé du jour par le code ; garde-fous Q1/Q3/Q7 par le code, sinon ancien bloc conservé ; remplace le résumé du jour dans l'invite | REF-07 | continuité de soi sur 7 jours, bascule racontée par l'intéressé, dedans visible pour l'animation | 105 appels courts / nuit (~6 min de Gemma) |
| 3 | **Rapprochement sémantique avant écriture au registre** (cos ≥ 0,80 = même fait) + **journal des 4 issues** (ajouté / confirmé / changé / **contradiction refusée** → alerte d'animation + défaut Q1) | REF-05 | plus de doublons « bagnole / voiture », contradictions de vie détectées et tracées | 1 embedding par fait extrait (5-10 % des messages) |
| 4 | **Chronologie des croyances** : `periode {cru_depuis, cru_jusqua}` déduite de `historique[]`, rendue « tu y as cru du J1 14 h au J2 09 h, puis démenti par… » | REF-06 | le doute et le retour deviennent racontables ; vigilance épistémique (qui m'a dit quoi, quand) | 0 appel, `esprit.mjs` |
| 3bis | **Garde-fous de prompt** dans l'appel d'extraction de `vie.mjs` (pas de contamination, pas d'inférence implicite, sens préservé « avant j'avais » = clos, **dates relatives résolues à la date du message**) + **mémoires de transition** (« ne vit plus seul depuis mardi ») + drapeau temporaire si le texte le dit | REF-05 (code) | moins de faits faux ou mélangés au registre ; le changement devient racontable | 0 appel de plus |
| 4bis | **Oubli sans horloge, calculé à la lecture** pour sensibilités et hashtags : `v_eff = repos + (v − repos)·0,98^tours_inactifs` (les relations gardent l'horloge, décision utilisateur) | REF-04 (code) | l'oubli dépend de ce qu'on a vécu entre-temps, pas des heures de sommeil ; zéro réécriture de mémoire | 0 appel |
| 5 | **Renforcement à l'usage** : un souvenir rappelé et repris dans la réponse gagne `imp ← imp + 0,1·(10 − imp)` (demi-pas s'il n'est que dans l'invite) et une `derniere_utilisation` qui rafraîchit son score | REF-04 (code, ACT-R) | les souvenirs structurants de la semaine restent rappelables au J6 sans grossir la mémoire | 0 appel |
| 5bis | **Supersession des clés à valeur unique** du bloc `vie` (domicile, métier, transport) par un changement raconté : `superseded_par` le registre, rien de supprimé | REF-04 (code) | un déménagement joué ne laisse plus fiche et registre en contradiction | 0 appel |
| 6 | **Blocs partagés en lecture seule = bases de camp / cohorte** (≤ 600 car., tenus par l'animation, jamais édités par l'avatar) | REF-07 | mémoire sémantique de camp enfin structurée (étape 3) | 0 appel, édition d'animation |
| 7 | **Fusion mots + sens + bonus d'entité au rappel** (RRF) au lieu du repli | REF-05 (code) | un nom propre rare (« rue des Carmes ») remonte même si le sens est moyen | 0 appel |
| 8 | **Étiquetage des souvenirs par entités de l'exercice** (lexique fermé fourni par l'animation) → facteur `lien` 0,5 sur entité commune | REF-04 | rappel « par qui / par où » sans graphe | 0 appel |
| 9 | **Règle d'ordonnancement nocturne** : tout traitement par avatar qui demande le modèle se fait entre le coucher et 06 h | REF-07 | sans objet pour le réalisme ; rend 2 et les suivantes possibles | — |
| 10 | Mentions au rappel (+0,05·min(1, expositions/4)) ; archivage des versions du bloc « où j'en suis » (trajectoire en 7 lignes) ; serveur MCP local lecture seule pour les relevés | REF-06, REF-08, REF-09 | marginal / outillage | 0 appel ; MCP = décision PLEIADE + avis CYBERSECU |

- **Ordre conseillé** : 1 → 3 → 4 (tous dans `vie.mjs` / `esprit.mjs`, sans appel) → 2 + 9 (une nuit d'essai sur 10 avatars, critères : bloc en français ≥ 95 %, 0 contradiction avec les chiffres, 0 invention de vie, ≤ 25 % de blocs rejetés par les garde-fous) → 5, 7, 8 → 6 avec EXPERT_INFLUENCE / ANALYSTES pays. À relire sur l'essai synthétique de 7 jours (critères E de l'avis n°14).
- ⭐ **CLASSEMENT FINAL après lecture des quatre rapports de code** (`REFERENCES\CODE-graphiti.md`, `CODE-letta-code.md`, `CODE-mem0.md`, `CODE-cognee-mcp.md`, 2026-10-12 soir) — **top 5, gain / coût** :

| Rang | Idée finale | Sources | Gain pour les avatars | Coût |
|---|---|---|---|---|
| **1** | **Registre bi-temporel « le LLM juge, le code date »** : `dit_t` ≠ `depuis_t` (marqueurs + garde-fou regex du futur), un seul appel qui rend `{même_fait, contredit}` avec le prompt anti-faux positifs de Graphiti, puis **règle de chevauchement en JS** (un fait ancien raconté en retard clôt le nouveau), rien de supprimé, **intervalles affichés** dans l'invite et la relecture | REF-06 code, REF-05 code (dates à la date du message) | l'avatar situe ses faits (« depuis trois jours », « avant, j'avais ») ; plus de faux changements de vie tirés d'une simple activité ou d'une promesse ; Q1/Q2 vérifiables | 0 appel de plus, `vie.mjs` |
| **2** | **Bloc « où j'en suis » nocturne façon `reflection-v2`** : 5 priorités (corrections > habitudes > faits durables > contradictions > façons de faire), 4 filtres (durable ? déjà là ? généralisable ? dates absolues), **par touches** (≥ 40 % de l'ancien repris, identité de la fiche en lecture seule), calculé sur copie, basculé seulement si les garde-fous Q1/Q3/Q7 passent, curseur qui n'avance qu'en cas de succès | REF-07 code | continuité de soi sur 7 jours sans « perte de soi », bascule racontée en première personne, dedans visible pour l'animation | 105 appels courts / nuit (~6 min), 400 car. / avatar |
| **3** | **Contradictions corrigées à la source + archive datée, jamais empilées** : rapprochement sémantique (cos ≥ 0,80) + supersession des clés uniques du bloc `vie` ; l'ancien fait part en `archive` lisible (« avant… ») ; la phrase de « transition » de Mem0 ne sert qu'au récit ; journal des issues avec raisons (`déjà_su / non_durable / non_étayé / contradiction_refusée`) → alerte d'animation | REF-07 code, REF-04 code, REF-05 code | plus de doublons ni de fiche en contradiction avec le registre ; chaque contradiction tracée et racontable | 1 embedding par fait extrait |
| **4** | **Saillance sans horloge** : oubli par tours d'inactivité à la lecture (`v_eff = repos + (v − repos)·0,98^n`) pour sensibilités et hashtags ; renforcement à l'usage `imp ← imp + 0,1·(10 − imp)` ; **critère « mentionné deux fois » / « agacé de le répéter »** (compteur d'attestations) qui promeut au marquant ou au registre | REF-04 code, REF-07 code (`human_memo`), REF-06 code (`episode_mentions`) | ce qui compte pour l'avatar reste rappelable au J6, le reste s'efface par la vie vécue, pas par les heures de sommeil | 0 appel |
| **5** | **Rappel fusionné** : RRF (k = 60) sur sens / mots / importance / fraîcheur / lien au lieu de pondérer des scores, bonus d'attestations, **anti-écho × 0,1** sur la publication en cours et ses reprises, intervalles de validité rendus (aucun filtre des faits clos, on les montre datés) | REF-06 code, REF-07 code, REF-05 code | un nom propre rare remonte, l'avatar ne se cite pas lui-même, le passé se raconte au lieu de disparaître | 0 appel |

  Suivent, inchangés : chronologie des croyances (REF-06), blocs partagés lecture seule = bases de camp (REF-07), gabarit « compagnon » (ton / état émotionnel à ménager) dans le résumé du jour (REF-07), entités de l'exercice par lexique (REF-04), ordonnancement nocturne (REF-07), MCP local pour les relevés (REF-09, PLEIADE + CYBERSECU). **Ce que la lecture du code a changé** : Cognee relevé à « récupérer » ; Mem0 ramené à ses garde-fous de prompt (son pipeline du papier n'existe plus) ; Graphiti réduit à « le LLM juge, le code date » (sa partie LLM est 12-20 appels par épisode, la partie code tient en 60 lignes de JS) ; Letta précisé en une **procédure** de réflexion nocturne (priorités, filtres, touches, curseur) plutôt qu'un « bloc éditable » ; **arbitrage Mem0 (empiler) contre Letta (corriger à la source) tranché pour Letta** sur le registre, Mem0 gardé pour le récit.
- **Écarté** : adopter Cognee, Mem0, Graphiti/Zep, Letta ou Letta Code (services, appels par message, cloud pour Zep/Letta Code) ; laisser l'avatar éditer ses chiffres (opinions, relations) ; supprimer une croyance démentie (DELETE) — on baisse avec un reste, on ne désapprend pas.

### 4.17 ⭐ Avis n°17 — Nuit du 11 au 12/10 : humeur, foyers, relecture, blocs « où j'en suis » (2026-10-12) — `AVIS\2026-10-12_avis17_nuit.md`
- **Fenêtre** : de 21 h 11 à 6 h 37. 72 messages sur 74 sont antérieurs à app-ia 2026-10-12.3. Celle-ci se juge sur 101 blocs nocturnes écrits, 4 refusés et 2 messages au réveil. Le registre des faits de vie est vide pour les 105 avatars.
- **Humeur (avis n°12)** :
  - acquis : valence moyenne −29, 0 avatar à −60 ou moins (101 avant), corrélation +0,36 avec l'extraversion ;
  - défauts : « tristesse » chez **105/105** avatars, humeur non recalculée pendant le sommeil (96 avatars figés depuis 0 h 23), lexique de la déprime 39 %, humour 0 %, vécu propre 7 %.
- **Foyers (avis n°15)** :
  - acquis : 0 faux défaut Q1, famille dans 9,5 % des messages (plafond 25 %) ;
  - à corriger dans eho : 7 foyers ont un âge `0` qui veut dire « inconnu », affiché tel quel (« femme 0 ans » chez Esteban Petitjean) → retirer la clé ;
  - métiers à revoir : Lucas Fontaine (« livreur » au lieu de facteur), Untergang (étiquette d'animation au lieu d'un métier de couverture, à trancher par l'ANALYSTE Mercure).
- **Section 11** : 9 % de messages signalés (sous la cible de 10-35 %). Deux erreurs de jour de repos ont échappé à la relecture (Stefan Marchal, Zoé Zimmer). Étiquetage des couples pensée / parole : 55 % cohérent, 35 % retenue, 10 % contradiction.
- **Blocs nocturnes : bon outil, première nuit à rejouer** :
  - 49 % commencent par « Je suis toujours » ;
  - **18 % contiennent des événements de guerre inventés** (couvre-feu, chars, drones, bombardement), absents de la situation et des souvenirs. Cause : la persona de nuit garde les EXEMPLES générés, et 67/105 fiches en contiennent ;
  - **6 pro-Mercure sur 14 ont l'orientation inversée, dont les 4 affirmés** (Mercure coupable, FORCE espérée) : aucun contrôle d'orientation n'existe ;
  - environ 10 % de contradictions de vie passent sans alerte (« seule » malgré un compagnon, nombre d'enfants, métier).
- **Règle durable** : un récit de soi réécrit par le modèle doit passer **au moins** les contrôles d'un message (vie, orientation, faits de la situation). La première version ne doit jamais être protégée par la règle de reprise : une erreur de la nuit 1 deviendrait canon pour 7 jours.
- **Les 4 refus** :
  - Ivan Berger « ma femme » : **juste** ;
  - Hanna Petit, Dana Horvat, Clémence Garnier « mon petit » : **probablement faux positifs**. `POSSESSIF` ne lit que le mot qui suit le possessif, et `LIENS` range « petit » parmi les enfants, donc « mon petit thé » compte comme un enfant.
- **Correction de règle demandée** (§2.3 de l'avis) : mot intermédiaire autorisé, « petit » traité selon le contexte, petits-enfants ajoutés, exception pour les métiers de garde d'enfants, contrôle du nombre, contrôle de « seul(e) », texte refusé journalisé.
- **12 corrections** (`dev\prototype-ia\corrections\2026-10-12_avis17.json`) : Ivan Berger, Stefan Marchal, 4 boulangers (rythme 4 h : Maxime Lefèvre, Jonas Mayer, Milan Vidal, Maxime Lambert), Zoé Kovac, Zoé Zimmer, Léa Vidal, Mira Garnier, Hugo Novak, Heidi Moreau.
  - Demandé à PLEIADE : un champ `retirer_exemples` dans `corriger-fiches.mjs`, plus un nettoyage par lot des exemples contenant des événements inventés.
- **Moteur (3)** :
  - **n°1** réflexion nocturne : contrôle d'orientation, contrôle des événements, persona sans exemples, anti-moule, rejeu sans la règle des 40 % ;
  - **n°2** contrôle de vie par le code (7 règles + jour de repos) ;
  - **n°3** humeur : récupération au réveil (`v ← repos + (v − repos) × 0,3`) et émotions variées.

  Les critères chiffrés sont dans l'avis.
- ✅ **Appliqué le 2026-10-12 vers 7 h (app-ia 2026-10-12.4, en local, 26 tests)** :
  - les 12 corrections de fiches et les 7 âges « 0 » ont été passés dans eho ;
  - améliorations n°1 a, b, c, e et f, n°2 en entier et n°3 (réveil, une tristesse diffuse par auteur et par heure).
  - **Écarts avec l'avis** :
    - (a) l'orientation est jugée par un appel court au modèle (pour/contre Mercure et FORCE), et non par une liste de mots ;
    - (d) `retirer_exemples` et le nettoyage par lot des 67 fiches **restent à faire** : la persona de nuit n'a déjà plus d'exemples ;
    - n°3 : la lassitude, l'agacement et l'ennui ne sont pas encore proposés à l'évaluation.
  - **Encore ouvert** : le métier de Lucas Fontaine, le métier de couverture d'Untergang (à trancher par l'ANALYSTE Mercure) et la fiche de Boris Roux.
  - **Constaté au passage** : `travailleLeDimanche()` ignorait `vie.metier`. C'est corrigé.
  - **Au prochain relevé** : vérifier les critères de l'avis n°17 sur les blocs rejoués.

### 4.18 ⭐ Avis n°18 — Première demi-heure EN PRODUCTION (DELATTRE 26) : le chœur de la solidarité (2026-10-12) — `AVIS\2026-10-12_avis18_production.md`
- **Fenêtre** : de 9 h 46 à 10 h 10, après la correction d'`IA_T0`. La période d'avant n'est pas jugée. Messages de joueurs : aucun extrait recopié, les comptes humains sont notés H1 à H3.
- **Chiffres** :
  - 16 réponses, 3 publications spontanées, 70 J'aime, 160 lectures (cycles) ;
  - l'IA fait 37 % des événements du réseau, un volume sain ;
  - mais **11 réponses sur 16 (69 %) sous un seul message humain** (annonce d'un groupe d'entraide), en 5 min : l'IA y fait 85 % des réponses ;
  - 15 réponses sur 16 sont des formules (« Super initiative », « Bravo pour l'initiative ❤️ », « Bon courage ») et **0 sur 15 apporte un élément concret** ;
  - rapport J'aime / réponses 4,4 ;
  - une question humaine (« une info ? ») n'a reçu que des « Bon courage ».
- **Acquis** : spontanées ancrées dans une vie (Kuz_MarketingPro, RudyKafMob), 0 événement inventé, 0 orientation inversée, 0 invention de vie publiée, humeur réparée (moyenne +4,9, plus de tristesse uniforme), garde-fous efficaces (❤️, formule retirée, 11 blocs refusés à juste titre).
- **Cause du chœur : une chaîne de 6 maillons** :
  1. `filDe` trie par popularité, donc un message humain aimé passe en tête chez tous les lecteurs au même cycle ; `MAX_LECTEURS` borne le total, pas le débit ;
  2. `persona` dit « PARTAGER vaut mieux qu'aimer quand … sa ville » ;
  3. ⚠ **MA règle n°12 (2), mal outillée** : « partage sans information → réponse » est à l'origine de **15 réponses sur 16**. Le code garde le mot de partage comme commentaire, alors que l'avis disait « répondre **ou aimer ». Angle mort : un appel à l'aide précis EST une information à faire circuler ;
  4. `CHOEUR` ne compte que les réactions sous déclencheur de voix (colorées) ;
  5. l'anti-tic travaille sur des groupes de 4 mots et ne voit pas les formules de 2 à 3 mots ;
  6. `retirerFormulesCreuses` ignore l'éloge et **rend intact un message qui n'est qu'une formule** ; 6 réponses du chœur sur 11 viennent du groupe témoin, qui n'est pas relu.
- **Règles durables** :
  - (1) sur un vrai réseau, un message humain émouvant non coloré est le **cas type du chœur** : il faut un plafond **par message**, pas seulement par avatar et par population ;
  - (2) des pensées identiques chez les lecteurs (9 sur 11 « C'est super… ») confirment un chœur **dans l'invite** : il faut montrer à l'avatar ce qui a déjà été répondu ;
  - (3) compatir sans rien apporter = **J'aime** ; un commentaire public doit apporter une offre, une question, une info ou un fait vécu ;
  - (4) les règles de code anti-chœur s'appliquent à **toute** la population, le groupe témoin ne concerne que la relecture par le modèle ;
  - (5) un message qui n'est qu'une formule ne se publie pas.
- **Moteur (9, par priorité)** :
  - **P1** : M1 plafond par publication (2 par 30 min, 4 au total, compteur à la décision, exemptions interpellation / abonné / relation ; d'IA à IA, 2 au plus) · M2 conversion refaite (actionnable → partage, 2 au plus ; humeur → J'aime ; `persona` corrigé) · M3 formule seule → J'aime + formules d'éloge listées ;
  - **P2** : M4 bloc « ce qui a déjà été dit » + offre tirée du métier, Jaccard ≥ 0,4 → J'aime, test de substance · M5 délai log-normal (médiane 3 min, de 1 à 20 min), 3 min entre deux réponses IA sur un même message, 2 min entre deux messages d'un même avatar, 8 lecteurs au plus par 10 min, aléa sur la popularité · M6 répondre à la question posée (Q4 élargie) ;
  - **P3** : M7 moule spontané (« concentr / motiv » dans 8 brouillons sur 12, « Entre… » dans 6 sur 12, « ici à H… » ; nourri par 14 blocs nocturnes sur 95) · M8 hygiène (95 `reflexion_t` et 61 `humeur.derniere` négatifs → rejouer les 95 blocs sans la règle des 40 %, « la la préfecture ») · M9 # hérités seulement après M1 à M4, part de l'IA par hashtag ≤ part globale + 10 points.
  - Critères chiffrés (13) dans l'avis, dont : ≤ 2 réponses IA par 30 min sous un message, lexique de formules ≤ 15 %, ≥ 40 % de réponses concrètes, conversions ≤ 20 %, J'aime / réponses ≥ 8, écart médian ≥ 3 min.
- **Fiches** : aucune correction (le défaut est collectif ; le 🛠️ de kenaupifObiwan = mécanicien, il a un sens). Pas de fichier `2026-10-12_avis18.json`.
- **Au prochain export** : reprise des # (pas de # hérité dans une réponse qui conteste, ≤ 280 caractères, part de l'IA par #), le premier message humain émouvant après la correction, le rejeu des blocs, l'humeur selon la distance à la D32, la population animée (103 annoncés contre 100 attendus avec 5 en pause), les abandons de la section 11 à compter à part des vrais échecs.

### 4.19 ⭐ Avis n°19 — Coefficient de persuasion et axes d'opinion éditables (2026-10-12) — `AVIS\2026-10-12_avis19_persuasion_axes.md`
- **Constat (DELATTRE 26, 15 h 47, environ 6 h)** : opinions quasi immobiles (Mercure −1,3 en moyenne, max 8,7, 0 bascule, 1 seul fait cru). C'est **conforme aux formules** : le moteur est calibré pour une semaine. Deux causes s'y ajoutent : FORCE, institutions et N.O.M sont immobiles faute de faits orientés crus (problème d'extraction, pas de gain), et un écart de 5 à 9 points reste **invisible dans les textes**, car `decrirePosition` ne change de libellé qu'à ±20 et ±60.
- **Persuasion `p`** (décision utilisateur : réglable dans l'app-ia, 1 = comportement actuel) :
  - bornes 0,5 à 3, pas 0,25, défaut 1, confirmation au-dessus de 2 ;
  - **règle : chaque voie d'influence est multipliée au total par `p`, une seule fois** :
    - accord d'opinion × p ;
    - voie « fait » : poids de croyance, répétition et démenti × √p (démenti plafonné à 0,95), puis croyance → opinion et fait périmé × √p ;
    - plafond journalier × √p ;
    - seuil de bascule, doute, inertie et engagement # inchangés ;
    - raidissement × min(1, p) ;
  - **p_IA = √p** pour une source citoyen IA (troupeau OASIS) ; p plein pour les joueurs, l'animation et les relais ;
  - indépendant de la crise, mais l'écran affiche crise × p et demande confirmation au-dessus de 4 ;
  - garde-fous : doute ≥ 2 h avant bascule, ≥ 2 sources distinctes, ≤ 5 % de bascules par axe et par heure, alerte si la dérive dépasse 5 points en 6 h ;
  - **levier de visibilité à faire en premier** : une ligne de « tendance » dans l'invite dès 5 points d'écart sur 48 h ;
  - **valeur pour DELATTRE 26 : 2,0**, relecture à H+3.
- **Axes éditables** :
  - champs : `cle` immuable, `libelle`, `description` pour le modèle, `pole_plus` / `pole_moins`, `pivot`, `statut`, `version`, recette `init`, `indices` ;
  - **position initiale** : centre par groupe eho donné par l'opérateur × (0,6 + 0,8·ancrage) + bruit uniforme de ±8 à graine fixe, |v| ≥ 3, aperçu avant écriture ; option dérivée d'un axe existant ; non par défaut à « 0 pour tous », au tempérament seul ou à l'estimation par le modèle ;
  - modifier le libellé ou la description = rien ne change dans l'état ; changer de référent ou inverser les pôles = créer un nouvel axe ;
  - **supprimer = archiver** : état gelé, axe retiré des invites et de l'extraction, campagnes ignorées, restauration possible, purge seulement après l'exercice ;
  - **FORCE et Mercure ne sont pas archivables** : ce sont les pivots de la voix, de `bloc` et des # ;
  - 6 axes actifs recommandés, 8 au maximum.
- **Règles durables** : (1) un coefficient multiplie ce qui existe — si l'extraction ne produit rien, le gain ne sert à rien ; (2) un déplacement qui ne change pas l'invite n'existe pas pour les joueurs ; (3) on n'amplifie jamais une rumeur sans amplifier son démenti ; (4) baisser `p` ou archiver un axe ne désapprend rien ; (5) tout axe affiché dans l'invite devient un sujet de conversation, donc il faut afficher seulement les axes saillants.
- **Ordre conseillé** : visibilité et traçabilité → `p` avec tests (non-régression à p = 1, crédule plus rapide qu'ancré) → garde-fous de bascule → p = 2 → registre des axes en lecture (4 axes, comportement identique) → libellé et description → ajout → archivage → saillance avant un 5e axe actif.

### 4.20 ⭐ Avis n°20 — Concordance fiche ↔ vie, pensée du décideur, images (2026-10-12) — `AVIS\2026-10-12_avis20_concordance_pensee_images.md`
- **La fiche eho fait foi** (âge, situation, activité, ville) ; le bloc `vie` est subordonné et n'affiche plus l'âge. Les messages publiés compatibles deviennent canon (veuf + « ma compagne » → registre, en proches), les incompatibles sont oubliés (alerte si un joueur a réagi). Enfants adultes ailleurs → `proches`. Correction **par le code** (rien regénéré par le modèle), « inconnu » jamais affiché, blocs nocturnes contradictoires remis à zéro. Pensée factuelle sans maxime + anti-chœur sur le texte rédigé. Images : `k_img` 1,0 / 1,15 / 1,35 (bornes 1,0 à 1,5), qui s'use (0,7^n sur 6 h), +1 imp, croyance inchangée au départ. **Erreur reconnue** : l'avis n°15 a tiré les foyers sur l'âge inventé sans lire la situation eho. Règle : toute dérivation d'un trait de vie prend le profil eho en entrée.

### 4.21 ⭐ Avis n°21 — Honte, culpabilité, élan d'action (2026-10-13) — `AVIS\2026-10-13_avis21_honte_culpabilite_elan.md`
- `EMOTIONS` : honte [-7, -8, « honteuse »], culpabilite [-5, +4, « coupable »], plancher -40 ; ETIQ gêné/honteux/humilié et embêté/coupable/rongé par le remords. Le décideur ne les choisit que si c'est LUI qu'on moque ou LUI qui a relayé du faux ; sinon le code requalifie (honte → degout, culpabilité → tristesse) ; cible < 5 %. Aucun effet sur les opinions. Remords : confiance -10 envers l'auteur relayé, +3 envers la source du démenti, partages non officiels × 0,7 pendant 24 h. Élan = **conversion par le code avant le rédacteur** (la nuance est choisie après la décision) : humiliation → silence, riposte p 0,25 (+0,35 si fier ou impulsif, -0,15 si pudique, entre 0,10 et 0,70) ; remords → partage cité du démenti avec correction, p 0,60 (+0,20 si conciliant ; 0 si croyance ≥ 60, démenti anonyme ou adverse, ou relais) ; mépris → ignorer p 0,40 (0,20 si interpellé), sinon ironie de 120 caractères au plus ; inquiétude → question dans 70 % des cas (consigne seule). Garde-fous : 1 correction par fait, 2 par jour, 4 par démenti et par heure sur la population ; 1 excuse par 24 h ; jamais d'excuse à un insulteur ; 1 riposte par insulteur et par jour. Pas de suppression du message d'origine.

### 4.22 ⭐ Avis n°22 — Formes des publications spontanées, de la vie à l'actualité et au débat (2026-10-13) — `AVIS6-10-13_avis22_formes_spontanees.md`
- **Constats** :
  - un moule unique : émoji final 89 %, « … » 73 %, 3 ou 4 phrases 86 % ;
  - vie seule 18 % et ambiance sans sujet 29 % des publications IA (joueurs : vie seule 1 %) ;
  - position prise 5 fois sur 94 ; commentaires IA → IA 7 contre 91 IA → joueur ;
  - 67 % des publications IA sans commentaire ; l'auteur revient 4 fois sur 134 ; désaccord 7 fois sur 116.
  - L'utilisateur : « on s'en fout de ta vie ».
- **Verdict** : le problème n'est pas d'abord la forme, **les avatars n'ont rien à dire**. Le code tire, sans appel de plus, dans cet ordre : sujet → position → nuance → forme, avec permission d'émoji et de « … ». 4 consignes qui fabriquent le moule sont à réécrire (« une fois sur deux sur SA VIE », « ce qui te préoccupe », « ce que tu fais en ce moment », « nombre d'émojis habituel », qui devient un maximum).
- **10 formes**, cibles en % des spontanées ; plafond = cible + 5 points, sur 3 h, actif dès 6 messages :

  | Forme | Cible |
  |---|---|
  | A1 prise de position | 20 |
  | A2 question à la communauté | 12 |
  | A3 réfutation | 10 |
  | A4 interpellation @ | 8 |
  | A5 info pratique | 10 |
  | A6 ligne sèche | 10 |
  | A7 humour | 8 |
  | A8 coup de gueule | 7 |
  | V1 anecdote ou bonne nouvelle | 8 |
  | V2 état d'âme | 7 (plafond 10, une fois par 24 h et par avatar) |

  - **Vie (V1 + V2) ≤ 15 %**, plafond dur ; ambiance sans sujet ≤ 5 %.
  - Poids × 2 si un trait favorise la forme, × 0,5 si un trait s'y oppose ; 2 formes de prédilection par avatar (× 1,5).
  - Conditions d'accès : pas d'humour sous tristesse ou peur ≥ 2, ni sur des victimes ; info pratique seulement avec un fait disponible.
- **Plafonds de population** :
  - émoji final ≤ 45 % ; « … » ≤ 20 % ; les deux ensemble ≤ 10 % ; 3 ou 4 phrases ≤ 25 % ;
  - « Entre … et … » : 1 par 3 h ; « Le calme… » : interdit ; lexique du calme ≤ 8 % ;
  - métier et sensations : au plus 1 spontanée sur 3 chacun.
- **Réponses** : bande de longueur tirée (20-70 : 35 % · 70-140 : 45 % · 140-220 : 20 %), mêmes plafonds sur l'émoji et les « … ».
- **Sujet** : faits et rumeurs connus, mots-dièse qui montent, message lu.
  - Poids : récence × expositions × proximité × (1 + |opinion| / 50).
  - Au plus 2 fois par avatar sur 24 h et 30 % de la population sur 3 h ; les 3 sujets chauds gardent la priorité.
  - La position (pour / contre / doute) est calculée par le code et transmise au rédacteur (« TON SUJET · TA POSITION · CE QUI LA FONDE »). La vie située compte comme actualité.
- **Désaccord** :
  - déclenché si l'écart atteint 30 points sur l'axe, ou si la crédence contredit le fait ;
  - p = 0,20, +0,25 si affirmé ou râleur, +0,15 si méfiant, −0,15 si conciliant, −0,10 si affinité ≥ 60 ; bornes 0,05 à 0,60 ;
  - trois degrés : nuance, doute, contradiction ; cible 20 à 30 % des réponses IA ;
  - civilité : on vise l'idée, pas la personne ;
  - plafonds : 2 messages par avatar et par dispute, 1 dispute par paire et par jour ; arrêt sur insulte, répétition ou 2 tours sans fait nouveau.
- **Audience IA ↔ IA** :
  - la priorité aux joueurs ne change pas (un joueur sans réponse depuis 20 min passe avant tout) ;
  - au plus 25 % des lectures et 30 % du plafond horaire ; cible 20 à 30 % de commentaires IA → IA ;
  - lecture obligatoire si l'avatar est @interpellé.
- **Suivi des fils** :
  - retour de l'auteur : p 0,8 s'il est interpellé par @, 0,6 sur une question ou une contradiction, 0,3 sur une approbation ; délai de 3 à 20 min ;
  - au plus 3 réponses de l'auteur (4 face à un joueur), 4 messages entre deux IA ;
  - arrêt à 12 h ou quand il n'y a plus rien de nouveau.
- **Mesures** : 15 critères. Sont **bloquants** : joueurs non lésés, 0 fait inventé, dérive attribuée à « ia » au plus 1,5 fois celle du groupe témoin.
- **Règles durables** :
  1. pas de publication sans sujet ;
  2. la forme se tire après l'émotion et ne la contredit jamais ;
  3. jamais d'amorces de phrase par forme, car elles deviennent un tic ;
  4. un débat entre IA ne passe jamais avant un joueur sans réponse.

### 4.23 ⭐ Avis n°23 — Orientation des avatars, réponses qui répondent, suivi de conversation (2026-10-14) — `AVIS\2026-10-14_avis23_orientation_reponses_suivi.md`
- **Base** : relevé NOYAU du 14/10, 13 h 05 (186 textes IA, 430 messages de joueurs). Code lu sans le modifier : `pont.mjs`, `esprit.mjs`, `redacteur.mjs`, `hashtags-herites.mjs`, `arobase.mjs`, route `/retex` d'`app-social`. L'avis n°22 reste en pause.
- **Causes trouvées dans le code** :
  - **orientation** : registres de voix **sans cible** (« le doute qui se glisse », amorces « Franchement, entre nous », « On nous avait promis… ») appliqués au sujet lu, donc un pro-Mercure doute de Mercure ; déclencheur « rumeur sur la FORCE » déclenché sur un message anti-Mercure ; # adverses hérités (`#mercureout` chez un pro-Mercure) ; groupe témoin non relu ; zone morte « partagé » de −20 à +20 ; `camp_affiche` « inconnu » pour toute la population, donc aucune attraction de camp ;
  - **réponse inspirée** : `placeSous` / `versJoueur` / `versReponse` rangent une publication écrite pour soi sous le message d'un joueur, et la relecture la traite en publication (Q4 jamais posée) : 22 cas ;
  - **0 suite sur 8** : la route `/retex` exporte `parent: post-<id>` pour un commentaire, sans `parentId`, donc `reponseAMoi` ne voit jamais une réponse au **commentaire** d'un avatar ; la mention exige l'@username exact, casse comprise ;
  - **mentions inventées** : `rafraichirNoms` est limité à 100 comptes, les handles sont fabriqués depuis le nom affiché puis tenus pour « connus ».
- **Verdicts** :

  | Piste | Verdict | Priorité |
  |---|---|---|
  | 1 Orientation | validée, réorientée | **P1** |
  | 2 Réponse inspirée | validée | **P2** |
  | 3 Suivi de conversation | validée (bug à corriger d'abord) | **P3** |
  | 4 Questions directes | validée | avec P3 |
  | 5 Diversité émotionnelle | réorientée | plafonds « préfecture » et « on ne sait plus quoi croire » avec P1, le reste avec l'étape 1 de l'avis n°22 |
  | 6 Forme | validée (étape 1 de l'avis n°22 + `registre_ecrit` par avatar) | avec l'étape 1 de l'avis n°22 |
  | 7 Hashtags | validée, modifiée | # adverse avec P1 ; reste **à décider par l'utilisateur** (attribution par fil côté Cockpit au lieu de recopier) |
  | 8 Mentions | validée | avec P3 |
  | 9 Langue et ton | validée | émoji léger sur la mort et phrase inachevée bloquante tout de suite |

  Ordre de test : P2, puis P3, puis P1.
- **P1** :
  - en amont : `cible_critique` / `cible_defendue` par voix ; amorces ciblées (2 au plus par registre) ; déclencheurs pro-* qui regardent les deux pivots ; filtre des # adverses ou inconnus dès |op| ≥ 5 ; « tu penches » de 5 à 20 pour une cohorte ; la ligne `[orientation]` n'est retirée qu'après une bascule mesurée, et une fiche sans pivot déclenche une alerte ;
  - en sortie : `positionAttendue(axe)` avec 5 états (ferme ≥ 10, tiède, doute, bascule, tendance) ; soupçon détecté par regex sur les pivots, puis classement court `{vise, sens}` à température 0,1, **pour toute la population, témoin compris** ; non conforme → 1 reformulation ciblée → retenu ;
  - attraction : `pub.bord` tiré de l'orientation extraite ou d'un # de sens connu ; `filDe` +30 pour son bord, +15 pour le bord adverse si |op| ≥ 40 ; déclencheur « habitant de son bord » (0,5 affirmé, 0,3 modéré) ; plafond par message inchangé ;
  - tests : rejeu des 186 textes (3 cas cités tous détectés, faux positifs ≤ 5 %) ; mini-population de 12 avatars (0 inversion en état ferme, ≥ 30 % de réaction des pro-Mercure au fil pro-Mercure) ; 3 jumeaux ferme / doute / bascule, 100 % conformes.
- **P2** :
  - suppression de `placeSous`, `versJoueur`, `versReponse` (la publication inspirée reste une publication) ; la réponse orpheline adressée est gardée ;
  - `repondAuParent` pour toute la population : au moins 2 mots communs, sinon un appel court ; si la réponse ne répond pas → J'aime ou rien, sans reformulation ; réponses d'élan exemptées ;
  - tests : 0 « inspirée → réponse » au journal ; réponses sans lien ≤ 2 % ; joueurs non lésés (au plus −3 points de part de réponses pertinentes).
- **P3** :
  - `parent_commentaire` ajouté à `/retex` ; `parentDirect()` remplace les 8 calculs du parent ; repli par le nom ; `mentionne()` insensible à la casse, avec username nu et nom complet ;
  - p_retour : 0,8 sur @, 0,6 sur une question ou une contradiction, 0,3 sur une approbation, 0 sans contenu ; au plus 2 retours face à un joueur, 1 face à une IA ; arrêt à 12 h, sur insulte ou répétition ≥ 0,4 ;
  - plafonds : +1 par heure par avatar, population au plus 1,2 fois le plafond ; délai de 2 à 15 min ; seuil d'activité 0,05 face à un joueur ; questions de joueur +40 dans `filDe` ;
  - tests : 30 stimuli locaux ; détection 100 % ; retour ≥ 70 % sur question ou mention, ≥ 50 % sur contradiction, ≤ 40 % sur approbation ; délai médian de 3 à 10 min ; 0 conversation au-delà des bornes.
- **Règles durables** :
  1. une attitude de voix sans cible devient l'inverse de son camp ;
  2. le moteur d'opinions est seul juge de l'évolution : un écart non mesuré est une dérive ;
  3. jamais de # du camp adverse ;
  4. une réponse répond, sinon J'aime ;
  5. quand on te répond, tu reviens une ou deux fois ;
  6. les garde-fous de camp et de pertinence couvrent aussi le groupe témoin.

### 4.24 ⭐ Avis n°24 — Annuaire des sources, abonnements par camp, publications ancrées, connaissances de camp (2026-10-14) — `AVIS\2026-10-14_avis24_sources_connaissances_publications.md`
- **Demande** : l'utilisateur ne veut plus de publications « état d'âme » (déplacés, bruit dans la tête, attaque chimique qui glace le sang). Les IA doivent parler de ce qui se passe à partir des sources qu'elles lisent et de leur connaissance du pays, savoir de quel camp est une source (@tv4ArnlandLive est pro-Arnland), et un pro-Mercure doit suivre @MercureToday.
- **Décisions de l'utilisateur** : NOYAU remplit un annuaire, qu'on testera ; vie seule ≤ 15 %, mais « vraiment intéressant à lire ».
- **Causes trouvées dans le code** :
  - un compte non IA reçoit `type_source: "particulier"` (pont l. 209) : TV4 vaut 35 pour tous, comme un habitant, et le bloc des officiels et `c.off` l'ignorent ;
  - `camp_affiche` vaut « inconnu » pour tous : aucun terme de camp dans la confiance ;
  - abonnements recopiés d'un gabarit ;
  - consignes « sur ce qui te préoccupe » et « une fois sur deux SA VIE ».
- **Réponse à la question du 14/10 au soir** (les pro-Mercure doutent de Mercure) : surtout un défaut du moteur. Les sources arnlandaises sont créditées de 35 à 50 par les pro-Mercure ; avec l'annuaire, ce sera 16 à 32, et l'effet adverse baissera d'un tiers aux deux tiers (test T7).
- **Annuaire** (réglage `annuaire`, même mécanisme que `campagnes`) :
  - champs par source : `nom`, `alias`, `type` (officiel, media, influent, militant, anonyme), `camp` (mercure, arnland, neutre), `fiabilite` (réputation perçue, 0 à 1), `notoriete` (part des habitants qui connaissent son camp), `suivi_par` par camp, `ville`, `libelle` (140 caractères), `ancrable` ;
  - le camp est tranché par l'ANALYSTE du pays ; l'annuaire est un miroir du registre si la source y figure ; jamais un compte de joueur.
- **Camp du lecteur** :
  - A = (Mercure − FORCE) / 2 ; le camp vient de la voix et ne change qu'après une bascule mesurée ; pour une voix neutre, |A| ≥ 25 ;
  - engagement e = 0,3 + |A| / 60 (au moins 0,7 pour un affirmé) ; termes de camp divisés par 2 pendant un doute.
- **Confiance a priori** = `A_PRIORI[type]` + terme de camp + 20·(fiabilité − 0,5), bornée de 5 à 85, et ≤ 25 pour une source adverse :
  - lecteur partisan : +30·e pour son camp, −35·e pour l'adverse, −8·e pour un neutre (média hostile) ;
  - lecteur neutre : −10 pour une source partisane, +5 pour une neutre ;
  - camp inconnu (tirage sur la notoriété) : type seul, appris en 3 lectures ;
  - fait pratique : 70 % de la pénalité rendue ; aveu de l'adversaire : c ≥ 0,55 ;
  - les relations existantes sont migrées par Δ de base, ce qui a été appris est gardé.
  - Exemples : TV4 vaut 16 chez un pro-Mercure affirmé, 41 chez un neutre, 81 chez un pro-Arnland affirmé.
- **Abonnements** (tirage déterministe, versionné) :
  - 2 médias de son camp (3 si e ≥ 0,7) et 1 neutre (2 pour un neutre) ; officiels selon `suivi_par` ; un média adverse avec p 0,2 pour un affirmé ;
  - aucun média au-delà de 60 % de la population ; migration lente après une bascule ; abonnements de la fiche gardés hors annuaire.
- **Spontanées ancrées** :
  - `choisirAncre` parmi les messages lus de l'annuaire et les croyances des 24 h, jamais un message de joueur. Poids : récence (demi-vie 6 h) × expositions × proximité × engagement × saillance × diversité ;
  - `positionSurAncre` : 7 positions par la crédence, la relation à la source, l'effet du fait sur son camp et l'état P1 (rectifie, compare, appuie, concède et recadre, s'interroge, prudence, conteste, attend) ;
  - bloc d'invite : CE QUI CIRCULE · CE QUE TU EN CROIS · TA POSITION · CE SUR QUOI TU PEUX T'APPUYER ; 2 consignes de persona réécrites.
- **« Intéressant » mesurable** :
  - 5 marques : M1 sujet, M2 source, M3 position, M4 argument, M5 détail. M2 et M5 sont vérifiées par le code, M1, M3 et M4 par un juge court ;
  - une publication ancrée passe avec M1, M2, M3 ou M4, et 3 marques au moins ; une publication de vie avec M5 et un lien à la situation ;
  - état d'âme seul : jamais publié ; une reformulation, puis rétention ;
  - **attribution inventée** : bloquant.
- **Plafonds** :
  - vie ≤ 15 % (plafond dur) ; ancrées ≥ 60 % ; une même source ≤ 35 % ; un même fait ≤ 30 % ;
  - contestation d'un même message adverse ≤ 3 par heure ; « Selon @ », « D'après @ », « X dit que » : chacun 2 par heure ;
  - le juge P1 est complété : rapporter pour contester, ou concéder en attribuant, n'est pas aller contre son camp.
- **Connaissances** (réglage `connaissances`) :
  - lignes des ANALYSTES (Mercure, Arnland ; neutre = thèses des deux camps), vérifiées par EXPERT_INFLUENCE ; 10 lignes de 160 caractères au plus ;
  - 3 lignes injectées par tour, en rotation (12 h par avatar, 3 fois en 3 h dans la population) ;
  - jamais par `croire` ; recopie de 8 mots ou plus → reformulation.
- **Tests sur l'export** (T1 à T13) :
  - **bloquants** : 0 attribution inventée ; joueurs non lésés (au plus −3 points) ;
  - vie ≤ 15 % et état d'âme seul ≤ 3 % ;
  - M2 ≥ 50 %, M3 ≥ 60 %, M4 ≥ 40 %, score ≥ 3 dans 75 % des cas ;
  - cohérence camp ↔ source ≥ 95 % ;
  - TV4 suivi par ≥ 50 % des pro-Arnland et ≤ 10 % des pro-Mercure ; confiance médiane envers TV4 : pro-Arnland ≥ 60, neutres de 30 à 50, pro-Mercure ≤ 30 ;
  - doutes sur Mercure divisés par 2, sans tomber à 0 ;
  - diversité ; recopie ≤ 5 % ; retenues P1 au plus +50 % ; volume ≥ 60 % ;
  - test à l'aveugle de l'utilisateur : ≥ 70 % de « intéressant ».
- **Ordre** : annuaire et confiance → abonnements → ancre et intérêt → connaissances (dès que les ANALYSTES livrent).
- **Règles durables** :
  1. une source a un camp, et on la juge selon qui la dit ;
  2. on suit d'abord son bord, plus un neutre ;
  3. pas de spontanée sans sujet, sans source et sans position ;
  4. une attribution est vérifiée ;
  5. contester n'est pas inventer ;
  6. les connaissances donnent des arguments, pas de la persuasion.
- **État** : spécifié, **non mis en œuvre**. Attend : NOYAU remplit l'annuaire ; ANALYSTE et ANALYSTE_ARN livrent les blocs de connaissances.

## 4bis. Dictionnaire des émotions (2026-10-12, demande de l'utilisateur, depuis le Mac)
- **But** : rendre les dialogues plus précis et plus variés (granularité émotionnelle) contre la monotonie mesurée : « tristesse » chez 105/105, déprime 39-43 %, humour 0 %.
- **Fichier** : `PSYCHOLOGUE/DICTIONNAIRE_EMOTIONS.json` (version 2026-10-12.2). Sources :
  - REF-10 Boussole des Émotions, reformulée ;
  - Plutchik (intensités) et Barrett (granularité), à sourcer ;
  - complément PSYCHOLOGUE : émotions de crise et marques d'écriture.
- **Contenu** :
  - **36 nuances** en **11 familles** : les 9 du moteur, plus **honte** et **culpabilité**, absentes du moteur à ce jour ;
  - chaque nuance a une définition, un élan d'action, des **marques d'écriture**, des formules **à éviter** et des **affinités** de caractère ;
  - **10 nuances « sur contexte »** (joie maligne, rancune, humiliation, remords, gratitude, chagrin…), jamais tirées au hasard ;
  - **4 règles d'émotion secondaire** liées au **tempérament**, jamais au genre (BdE).
- **Doctrine** : le **code choisit** la nuance (règles 1 à 7 du fichier), et le **rédacteur** la reçoit « à faire sentir sans la nommer ». On ne donne jamais une liste de mots, car elle créerait un nouveau tic. L'**élan d'action** peut orienter la décision (honte → se taire ; remords → corriger ; mépris → ignorer ou ironiser).
- **Piège constaté** : la ligne « Tempérament » standard (« ni crédule ni méfiant ») faussait la détection des affinités. Seuls le **Caractère** et l'**Activité** comptent.
- **Essai v3 sur le banc Mac** (`pont/banc_ia/redacteur.py --v3`, `emotions.py`, 13 messages réels, 26B) : effet **réel mais modeste**. Détail dans `pont/banc_ia/RESULTATS_MAC_2026-10-12.md`.
  - +0,5 s par message ; +16 caractères en moyenne.
  - ✅ Gains :
    - **approbation réservée** pour la râleuse sceptique (« super initiative, mais j'espère qu'ils ont prévu de quoi transporter tout ça en toute sécurité ») ;
    - **fierté personnelle** au lieu de la déprime (« On a réussi à stabiliser le service malgré le chaos. Pas mal. ») ;
    - **impuissance** exprimée concrètement.
  - ⚠ Limites :
    - **la pensée du décideur domine** : « la solidarité c'est ce qui nous fait tenir » revient malgré « à éviter » ;
    - un **nouveau tic** apparaît chez 2 avatars (« on ne peut rien faire de notre côté ») ;
    - lassitude rendue par de l'inquiétude ; la mélancolie ne se voit pas.
- **Suites proposées** :
  1. donner le dictionnaire **au décideur** (choisir la nuance au moment de la pensée), ou faire réécrire la pensée selon la nuance ;
  2. **rotation sur la population** (règle 4) dans le moteur réel ;
  3. ajouter à `retirerFormulesCreuses` les formules repérées ;
  4. ajouter honte et culpabilité aux familles du moteur ;
  5. relier le dictionnaire au Reporting d'influence (mépris, joie maligne, haine = marqueurs ILI).

## 5. Index des sources

| Réf. | Source | Apport principal |
|---|---|---|
| REF-01 | Binz et al., *Centaur* (arXiv 2410.20268, 2024) — Psych-101 | un LLM affiné sur 10,7 M de choix humains prédit le comportement mieux que 14 modèles spécialisés ; format langage naturel ; manque de différences individuelles et de social |
| REF-02 | Wikipédia, *Cognitive architecture* | structurer l'esprit en modules (mémoires, buts, émotions, attention) ; ACT-R, Soar, CLARION, LIDA, Psi-Theory… |
| REF-03 | UNIGE 2017 — Rudrauf, Williford, Bennequin, Friston, *Modèle de Conscience Projective* (J. Theoretical Biology) | émotions, croyances, préférences ; choix par minimisation de l'énergie libre anticipée ; prise de perspective |
| REF-04 | Cognee — github.com/topoteretes/cognee (README + **code source**, 2026-10-12 ; Apache 2.0, Python) | mémoire hybride graphe + vecteurs + sessions, pipeline ECL (GLiNER local) ; **dans le code** : poids appris par retour, oubli sans horloge calculé à la lecture, consolidation à deux passes avec raisons de rejet, supersession sans suppression ; verdict : **récupérer l'idée** (oubli par tours inactifs, poids appris, supersession, raisons de rejet), librairie sans intérêt |
| REF-05 | Mem0 — github.com/mem0ai/mem0 + Chhikara et al., arXiv 2504.19413 (2025) + **code source v3** (clone 07/10/2026 ; Apache 2.0, Python/TS) | papier : extraction puis ADD/UPDATE/DELETE/NOOP, LOCOMO +26 %, −90 % tokens ; **code : ADD seul, contradictions accumulées en « transition », expiration masquée, entités sans LLM, pas d'importance ni d'oubli en OSS** ; verdict : récupérer l'idée (rapprochement sémantique avant écriture, journal des 4 issues, garde-fous de prompt + dates à la date du message, mémoires de transition, fusion mots + sens + entités) |
| REF-06 | Zep / Graphiti — github.com/getzep/graphiti, zep-js + Rasmussen et al., arXiv 2501.13956 (2025 ; Apache 2.0, Zep Cloud commercial) | graphe temporel bi-temporel (`valid_at`/`invalid_at` vs `created_at`/`expired_at`), invalidation sans suppression, locuteur = entité, bloc « FACT (date range) » ; verdict : récupérer l'idée (bi-temporalité du registre, plages de dates, chronologie des croyances), service sans intérêt |
| REF-07 | Letta (ex-MemGPT) — github.com/letta-ai/letta + Packer et al., arXiv 2310.08560 (2023 ; Apache 2.0, Python/TS, Ollama) | mémoire « style OS » : contexte de travail **éditable par l'agent** (blocs), rappel, archive, résumé récursif, pression mémoire, blocs partagés, agents de sommeil ; verdict : récupérer l'idée (bloc « où j'en suis » réécrit la nuit, blocs partagés lecture seule = bases de camp, ordonnancement nocturne) |
| REF-08 | Letta Code — github.com/letta-ai/letta-code (README, 2026-10-12 ; Apache 2.0, modèles cloud) | harnais de programmation à mémoire persistante (MemFS versionné par git, skills) ; verdict : sans intérêt (note : archiver les versions du bloc « où j'en suis ») |
| REF-09 | Model Context Protocol — github.com/modelcontextprotocol (Linux Foundation ; SDK TS/Python/…) | standard hôte/client/serveur JSON-RPC (tools, resources, prompts) ; prise, pas mémoire ; verdict : sans intérêt pour la psychologie, s'en inspirer plus tard pour interroger la mémoire pendant les relevés (PLEIADE + CYBERSECU) |
| REF-10 | **La Boussole des Émotions** — emotioncompass.org/fr (TCE, traduction de l'Institut Français de la TCE ; aucune licence affichée, donc reformulé) | émotions de base avec fonction, besoin, élan d'action et corps ; **primaire / secondaire / instrumentale** (la colère masque la tristesse, la honte ou la peur) ; honte (ce qu'on EST, se cacher) contre culpabilité (ce qu'on a FAIT, réparer) ; dégoût social et mépris ; émotions mêlées (jalousie, haine, envie, désespoir, attachement, joie maligne, rancune) ; verdict : **base du DICTIONNAIRE DES ÉMOTIONS** (`DICTIONNAIRE_EMOTIONS.json`) |

## 6. Questions ouvertes
- ⭐ **À reprendre avec l'utilisateur (2026-10-12)** : la **pyramide de Maslow**, associée aux émotions. Piste : chaque émotion de la Boussole signale déjà un **besoin** (sécurité pour la peur, appartenance pour la honte, lien pour la tristesse, limites et dignité pour la colère). Des besoins hiérarchisés pourraient moduler les émotions (un avatar privé d'eau ou de sécurité lit tout à travers ce manque) et rejoindre les **besoins** de la Psi-Theory déjà prévus (REF-02). ⚠ À sourcer : la hiérarchie stricte de Maslow est contestée (révision de Kenrick et al., 2010) ; mieux vaut des besoins **pondérés par la situation** qu'un escalier.
- Valider le lot « contagion » et les paramètres de tempérament à ajouter dans la fiche eho (section « Comportement IA »).
- Formaliser la contagion en **mise à jour bayésienne** (REF-03) ou en règles bornées simples (plus lisibles pour l'animation) ? Probablement les deux : calcul bayésien, affichage simplifié.
- Sourcer les références générales (confiance bornée, vérité illusoire, retour de flamme, Big Five, preuve sociale) — et, depuis l'avis n°1 : influence persistante après démenti (Lewandowsky 2012), effet rebond du démenti (Wood & Porter 2019), biais de négativité (Baumeister 2001), congruence de l'humeur (Forgas), règle 1-9-90 (Nielsen 2006), crédibilité de la source (Hovland & Weiss 1951), vigilance épistémique (Sperber 2010).
- ✅ **TRANCHÉ le 2026-10-10 par l'utilisateur** : « on reste sur ce que proposent les agents experts dans leur domaine ; on verra les détails ». Les 4 points de l'avis n°1 §5 sont **adoptés tels que proposés** (valeurs de tempérament et proches d'Anastasia, axes d'opinion, garde-fou budget + 3, annotation manuelle). Rappel du texte d'origine : **Avis n°1** (`AVIS\2026-10-10_ANALYSE_PROTOTYPE.md`, §5) — à trancher : valeurs de tempérament et proches d'Anastasia (avec ANALYSTE_ARN) ; abandon de l'adhésion par thème au profit d'axes (à aligner sur `lib/camp.ts`, −100 pro-MER … +100 pro-ARN) ; garde-fou dur du budget (budget + 3) ; annotation manuelle des affirmations au lot 1.
