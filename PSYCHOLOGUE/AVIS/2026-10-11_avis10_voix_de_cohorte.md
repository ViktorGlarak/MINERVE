# AVIS PSYCHOLOGUE n°10 — Voix de cohorte (proposition prête à coder, 2026-10-11 ~11 h 30)

*Décision utilisateur : « voix de cohorte — oui, j'applique ce que PSYCHOLOGUE propose ». Sources : PSYCHOLOGUE MEMOIRE §3-4 (4.8, 4.9), avis n°9 ; EXPERT_INFLUENCE MEMOIRE + `REFERENCES\principes_propagande_morelli.md`, `mentalite_russe_ILI.md` ; ANALYSTE\ARNLAND MEMOIRE (countrybook société / information, tensions, vocabulaire narratif, fiche Anastasia) ; code `moteur.mjs`, `pont.mjs`, `orienter-citoyens.mjs`. Codé par PLEIADE le jour même (lot H).*

**Constat préalable dans le code** : la cohorte n'existait pas pour le moteur — `orientation_initiale` écrit dans eho mais jamais lu ; `bloc()` dérive affirmé/modéré/neutre de max(|Mercure|, |FORCE|), donc un « déçu » tiré à FORCE −20 était traité en neutre ; seule trace : la ligne `[orientation]` noyée parmi les consignes → 14 pro-Mercure sur 15 parlaient comme des neutres. La voix s'appuie désormais sur `orientation_initiale` tant que l'axe pivot garde son signe (FORCE pour les pro-M ; FORCE/Mercure pour les pro-A) ; si le signe s'inverse, **la voix s'éteint : c'est la bascule qui devient visible**.

## 1. Principe — une orientation se voit par le biais, pas par le slogan
Un citoyen ordinaire ne milite pas : il **remarque** sélectivement (le pro-M voit chaque convoi, chaque pénurie « depuis qu'ils sont là » ; le pro-A voit la rumeur et celui qui la propage), il **minimise** (démentis officiels ↔ défauts concrets de la FORCE), il **attribue** la même pénurie à une cause différente (présence de la FORCE ↔ invasion mercurienne — Morelli n°2 et son miroir), il **fait confiance** à des sources différentes (`confiance_a_priori` officiel 15-35 vs 55-80), il a **ses mots** (ANALYSTE_ARN : « invasion / nos concitoyens » côté bleu ; « on ne nous dit pas tout / la paix d'abord » côté rouge). Quatre marqueurs observables : à qui il répond · à quoi il attribue · de qui il doute · son lexique.

## 2. Par bloc (déclencheurs → p ; registre ; éléments de langage ; interdits ; consigne)
- **Pro-Mercure affirmé (4)** — post officiel/média sur pénurie/retard p 0,6 ; fait portant une orientation FORCE p 0,7 ; militant aligné → partage avec un mot p 0,4 ; rumeur de menace p 0,5. Registre « le déçu qui l'assume » (« Depuis qu'ils sont là, … », « On nous avait promis… », « Ma belle-sœur de l'autre côté de la frontière… », « Mercure a tort sur beaucoup de choses, mais pas là-dessus »). EdL : inversion causale (Morelli 2 ; ligne N.O.M), « on ne nous dit pas tout » (déni), « les Mercuriens d'ici, personne ne les défend » (diaspora 8 %), « la paix d'abord » (LO 5). Interdits : « libération », « compatriotes », « force d'occupation / OTAN criminelle », appel à agir, fait non vu.
- **Pro-Mercure déçu (11)** — officiel sur pénurie → question/réserve p 0,35 ; rumeur FORCE → « si c'est vrai… » p 0,4 ; démenti → « on verra » p 0,3 ; N.O.M p 0,2. Registre « le doute qui se glisse ». EdL : « on attendait mieux », « les torts ne sont pas tous d'un côté », « pourvu que ça s'arrête ». Interdits : défendre Mercure frontalement, « occupation », s'en prendre à un déplacé.
- **Pro-Arnland affirmé (4)** — rumeur contre la FORCE (assurance ≤ 0,5 ou source particulier/anonyme) → « source ? » p 0,7 ; N.O.M / militant → contestation p 0,6 ; officiel utile → partage p 0,5 ; un déçu qui lâche prise p 0,4. Registre « ferme et poli ». EdL : « invasion » jamais « opération », « nos concitoyens », « ils font le jeu de Mercure », « l'info officielle, c'est la préfecture ». Interdits : « traître / collabo », glorifier la guerre, nier une pénurie réelle, position militaire.
- **Pro-Arnland attaché (11)** — rumeur contre la FORCE p 0,35 ; attaque contre les siens p 0,5 ; officiel utile → J'aime/partage p 0,4 ; N.O.M p 0,2. Registre « rassuré, pas militant ». EdL : « ils sont là, c'est déjà ça », ré-attribution causale à l'invasion, « on tient », reconnaître le défaut concret. Interdits : « traître », slogan hors # offert, nier un problème.
- **Neutre (72)** — sa couleur est l'**ambivalence** : dispute rouge/bleu sous ses yeux → « arrêtez tous les deux » p 0,25 ; fait nouveau crédible (confiance ≥ 0,5) → la question qui manque p 0,3 ; le reste = vie quotidienne. Registre « ni l'un ni l'autre ». Interdits : « occupation », « libération », « ta source ? » plus d'une fois par jour.

## 3. Dosage
Part colorée visée : **affirmé 40 %**, **modéré 25 %**, **neutre ≤ 10 %** (un message de vie où la couleur se glisse compte 0,5). **Quota glissant sur les 10 derniers messages** : affirmé 30-50 %, modéré 15-35 %, neutre 0-20 % ; sous le plancher → prochain déclencheur obligatoire (p = 1) ; au plafond → p = 0 + « pas de politique ce créneau ». Crise : p_eff = p × (0,6 + 0,4·coef) borné [0,3 ; 1] ; plancher/plafond +10 si coef ≥ 1,5, −10 si ≤ 0,5.

## 4. Garde-fous anti-caricature
Jamais 2 colorés de suite · anti-chœur : pas plus de 3 réactions colorées du même bloc sur une même publication en 30 min · lexique interdit par bloc → reformulation avec le mot cité · un déçu qui écrit « Mercure a raison » → reformulation · un bleu qui qualifie une personne → « vise l'idée » · un coloré n'ajoute jamais de # non offert · la voix s'éteint quand l'axe pivot change de signe.

## 5. Mesure au relevé de 15 h
(1) part colorée par cohorte : affirmés 30-50 %, modérés 15-35 %, neutres ≤ 20 % ; (2) **test à l'aveugle** : 20 messages colorés, bloc masqué, l'animateur devine ≥ 70 % (déçu ↔ neutre ≥ 60 %) ; (3) dispersion : ≥ 3/4 affirmés et ≥ 6/11 modérés par camp ont produit ≥ 1 coloré en 6 h ; (4) 0 lexique interdit, 0 chœur > 3 ; (5) cohérence chiffre/texte (coloré pro-M avec FORCE < −10, pro-A avec FORCE > +10) ; (6) au moins un échange argumenté entre bords.

## À CODER → mise en œuvre PLEIADE (lot H, 11 h 50)
1. `this.voix` lu depuis `orientation_initiale` (ou déduit de la cohorte eho pour les 3 citoyens de test), `voixActive()` par le signe de l'axe pivot — ✅
2. `VOIX[bloc].declencheurs` évalués par le pont sur le fil lu (`declencheursSur`) — ✅
3. Registres par bloc tirés seulement sur déclencheur, injectés dans la ligne « registre » avec le n° de la publication — ✅
4. Quota glissant 10 messages (`pVoix`, `quotaVoix`, modulation par `crise()`) — ✅
5. Marquage `voix` / `declencheur` / `colore` sur chaque proposition — ✅
6. Garde-fous : jamais 2 colorés de suite, anti-chœur 3/30 min/bloc, lexique interdit dans `controler` — ✅ (reformulations déçu/attaché couvertes par le lexique)
7. Consignes `[orientation]` remplacées à l'invite par la consigne de la voix (la fiche eho n'est pas réécrite ; voix éteinte = ligne retirée) — ✅
8. Relevé 15 h : les 6 mesures + tirage à l'aveugle — à faire au relevé
