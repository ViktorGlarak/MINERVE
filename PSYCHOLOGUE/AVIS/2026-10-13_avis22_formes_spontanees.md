# Avis n°22 — Formes des publications spontanées, de la vie à l'actualité et au débat (2026-10-13)

**Auteur** : PSYCHOLOGUE · **Demandeur** : NOYAU, pour PLEIADE, sur le constat de l'utilisateur.
**Constat** : on repère tout de suite une publication IA. Elle suit un moule unique (« sensation + activité + état d'âme + … + émoji »). L'utilisateur a envie de répondre « on s'en fout de ta vie ».

**Mesures**

| Source | Ce qui a été mesuré | Résultat |
|---|---|---|
| Relevé de 17 h 46 | 69 publications spontanées | émoji final 89 %, « … » 73 %, 3 ou 4 phrases 86 %, médiane 172 caractères |
| Relevé de 17 h 46 | Réponses et citations | « … » 67 %, émoji final 75 % |
| Export depuis 11 h 20 | Contenu des publications IA | vie seule 18 %, ambiance sans sujet 29 % (joueurs : vie seule 1 %) |
| Export depuis 11 h 20 | 94 publications IA | position prise 5, @ 1, question 12 |
| Export depuis 11 h 20 | Commentaires | IA → joueur 91, IA → IA 7 |
| Export depuis 11 h 20 | Audience | 67 % des publications IA sans commentaire ; l'auteur ne revient que 4 fois sur 134 |
| Export depuis 11 h 20 | 116 réponses IA | 7 contredisent ou doutent |

**Code lu sans le modifier** : `esprit.mjs` (FORMAT, consigne « SA VIE », `tics`), `redacteur.mjs` (REALISME, LONGUEUR), `pont.mjs` (déclencheurs des spontanées, `ticsPopulation`, `motsDeLaFoule`, `placeSous`), `emotions.mjs` (plafond de 15 %).

---

## Verdict

**La proposition de PLEIADE est validée, mais réorientée.** Le problème n'est pas d'abord la forme : **les avatars n'ont rien à dire**. Une publication sans sujet ne peut tomber que dans l'état d'âme.

Ordre de traitement :
1. **un sujet et une position** à chaque publication spontanée (partie B) ;
2. **une forme** (partie A) ;
3. **un débat borné** (parties B3 à B5).

Le code tire tout cela sans appel de modèle supplémentaire. Ordre de tirage : sujet → position → nuance → forme, avec permission d'émoji et de « … ».

Quatre consignes fabriquent le moule et sont à réécrire :
- « au moins une fois sur deux c'est sur SA VIE » ;
- « sur ce qui te préoccupe en ce moment » ;
- « si tu parles de ce que tu fais en ce moment » ;
- « ton nombre d'émojis habituel », qui devient un **maximum**.

---

## A. Grille des formes (10 formes, citoyens seulement ; les relais gardent leurs registres)

Longueurs en caractères ; cible en % des publications spontanées de la population.

| # | Forme : définition | Longueur | Émoji | « … » | Exemple | Favorisée par | Cible |
|---|---|---|---|---|---|---|---|
| A1 | **Prise de position** : le sujet et un avis net, avec une raison | 60-180 | rare | non | « Fermer le pont de HFrouard sans déviation annoncée, c'est punir ceux qui bossent à HNancy. » | affirmé, engagé ; \|opinion\| ≥ 25 | 20 |
| A2 | **Question à la communauté** : un objet précis et un destinataire | 50-130 | rare | non | « Ceux de HToul : la rumeur du rationnement d'essence, quelqu'un l'a vue ailleurs que sur ce compte ? » | curieux, inquiet ; en doute | 12 |
| A3 | **Réfutation** : contredire un fait ou une idée qui circule, sans viser personne | 60-160 | non | non | « Le "camp de la FORCE à HVillers", c'est le gymnase de la préfecture, le panneau est en photo partout. » | méfiant, sceptique ; crédence ≤ 30 | 10 |
| A4 | **Interpellation @** d'un compte qui a dit le contraire | 50-150 | non | non | « @Nom_du_compte, tu as vu un seul convoi à HLaxou ? Moi j'y passe tous les jours. » | extraverti, impulsif, affirmé ; écart ≥ 40 | 8 |
| A5 | **Info pratique** : lieu, heure ou chiffre | 60-160 | non | non | « HLaxou : la boulangerie ouvre dès 6 h 30, une baguette par personne. » | consciencieux, serviable | 10 |
| A6 | **Ligne sèche** sur le sujet | 20-70 | rare | non | « Plus d'essence à HToul après 9 h. » | introverti, peu émotif, au travail | 10 |
| A7 | **Humour, ironie** sur l'actualité | 40-140 | 1 au plus | non | « Troisième convoi devant la boutique : je vais leur faire un tarif de groupe. » | ironique, extraverti ; humeur ≥ −20 | 8 |
| A8 | **Coup de gueule bref** | 40-120 | rare | non | « Deux heures de queue à la pharmacie de HToul pour un "revenez jeudi". Non. » | émotif, râleur ; colère | 7 |
| V1 | **Vie** : anecdote ou petite bonne nouvelle | 40-140 | oui | non | « La farine est arrivée : brioches samedi. » | sociable, optimiste | 8 |
| V2 | **Vie** : état d'âme (le moule actuel) | 80-200 | oui | 1 au plus | « Les camions passent depuis 5 h. Je pétris quand même. » | émotif, anxieux | 7 |

**Tirage de la forme**
- Poids de base, × 2 si un trait du **caractère ou de l'activité** favorise la forme, × 0,5 si un trait s'y oppose, × 0 si la condition d'accès manque.
- **2 formes de prédilection** par avatar (× 1,5) : c'est ce qui garde une voix propre.
- Jamais deux fois la même forme de suite.
- La nuit, seules A6, V1 et V2 sont permises.

**Conditions d'accès**
- A5 exige un fait disponible : fiche, vie, brouillon ou fait lu.
- A3 et A4 suivent la partie B3.
- Une rumeur à laquelle l'avatar croit s'écrit au conditionnel. On n'amplifie jamais une rumeur sans son démenti (avis n°19).
- A7 est exclue :
  - sous tristesse ou peur d'intensité ≥ 2 ;
  - sous chagrin ou humiliation ;
  - sur un sujet où il y a des victimes.
- V1 est exclue à humeur ≤ −30, sauf soulagement.
- A8 est exclue si l'humeur est positive et l'activation basse.

**Plafonds de population** (spontanées des 3 dernières heures, actifs dès 6 messages, même mécanisme que les nuances)

| Élément | Plafond |
|---|---|
| Chaque forme | cible + 5 points |
| **Vie (V1 + V2)** | **15 %**, plafond dur |
| V2 | 10 % ; une fois par 24 h et par avatar au plus |
| Émoji final | 45 % (s'il est interdit, il est retiré) |
| « … » | 20 % (remplacés par « . ») |
| « … » et émoji ensemble | 10 % |
| 3 ou 4 phrases | 25 % |
| « Entre … et … » | 1 fois par 3 h |
| « Le calme… » | interdit |
| Lexique calme / boucan / vacarme / silence / bruit / concentrer | 8 % |

**Métier et sensations** : au plus 1 publication spontanée sur 3 pour chacun, par avatar, sur 24 h. L'activité en cours n'est transmise au rédacteur que pour A5, V1 et V2, ou quand le sujet touche le métier.

**Réponses** (version allégée, sans grille de formes)
- Bande de longueur tirée : 20-70 (35 %), 70-140 (45 %), 140-220 (20 %).
- Mêmes plafonds sur l'émoji et les « … ».
- Pas de métier ni de sensation si le message lu ne s'y prête pas.

---

## B. De la vie à l'actualité et au débat

### B1. Un sujet et une position à chaque publication spontanée

**Candidats au sujet**, pris dans la mémoire de l'avatar :
- les faits et rumeurs qu'il connaît (vus ou reçus dans les 24 h) ;
- les mots-dièse qui montent et qui lui sont indiqués ;
- le message lu qui l'a fait réagir. S'il s'agit d'un joueur, c'est une **réponse** (règle `versJoueur` existante).

**Poids d'un candidat** : récence × nombre d'expositions × proximité (sa ville, son métier, ses proches) × (1 + |opinion sur l'axe| / 50). Plus on est tranché, plus on parle.

**Diversité** :
- un même sujet au plus 2 fois par avatar sur 24 h ;
- au plus 30 % des spontanées de la population sur 3 h ;
- mais les **3 sujets chauds** de l'heure gardent la priorité : c'est la convergence qui crée le débat.

**Position** : calculée par le code à partir des axes, de la croyance et des lignes de cohorte : pour / contre / doute, et intensité. Le rédacteur la reçoit ainsi : « TON SUJET : … · TA POSITION : … · CE QUI LA FONDE : <fait, crédence> ».

**Quota de vie** :
- **vie seule ≤ 15 %** ; **ambiance sans sujet ≤ 5 %** (aujourd'hui 47 % à elles deux) ;
- la vie **située** compte comme actualité (« le pont fermé, mes livraisons font 40 km de plus »).

**Consigne du décideur à réécrire** : « Quand tu publies, c'est sur un sujet d'actualité (indiqué) et tu dis ce que tu en penses ; ta vie ne sert qu'à l'illustrer. »
**Déclencheur « moment de vie »** : il n'est plus tiré à 8 % ; il obéit au quota.

### B2. Formes qui ouvrent la discussion

A1 à A4 font **50 %** des spontanées. Ce sont les seules qui appellent une réponse : un avis, une question, une contradiction ou un nom.

**Une question ou une interpellation doit avoir un objet concret.** Refusées : « Vous en pensez quoi ? », « On nous cache quelque chose, non ? ».

### B3. Le désaccord

**Quand contredire** : l'écart avec le message lu atteint 30 points sur l'axe concerné, **ou** la crédence de l'avatar contredit le fait (≤ 30 face à une affirmation ; ≥ 70 face à un démenti).

**Probabilité de contredire** :

| Facteur | Effet |
|---|---|
| Base | 0,20 |
| Affirmé, combatif ou râleur | +0,25 |
| Méfiant | +0,15 |
| Conciliant ou timide | −0,15 |
| Affinité ≥ 60 avec l'auteur | −0,10 ; avec un ami, l'avatar nuance au lieu de contredire |
| Bornes | entre 0,05 et 0,60 |

**Trois degrés** : nuance (« oui, mais… », avec un fait), doute (une demande de source, en variant la tournure), contradiction (« Non : … », avec un seul argument).

**Cible** : 20 à 30 % des réponses IA marquent un désaccord ou un doute, contre 6 % aujourd'hui.

**Civilité** :
- on vise l'idée, pas la personne ;
- pas d'insulte : le contrôle existe déjà ;
- pas d'attaque sur l'origine ou le camp ;
- pas d'ironie sur des victimes ;
- pas de majuscules criées ;
- le tutoiement seulement avec une familiarité suffisante ;
- un argument tiré de la fiche ou d'un fait connu, jamais inventé.

**Pas d'escalade** :
- dans une même dispute, chaque avatar écrit 2 messages au plus ;
- une dispute par paire d'avatars et par jour ;
- arrêt immédiat dans trois cas : insulte reçue (élan de l'avis n°21), argument répété (ressemblance ≥ 0,4), deux tours sans fait nouveau ;
- sortie possible : « on ne sera pas d'accord », un J'aime de politesse, ou le silence.

**Garde-fou d'opinion** : une dispute entre IA ne fait bouger les opinions que par le modèle existant (faits, crédence, confiance). L'alerte de dérive (5 points en 6 h) s'applique.

### B4. Audience entre avatars IA

**La priorité aux joueurs ne change pas.** Un message de joueur resté 20 min sans réponse passe avant tout échange entre IA.

**Part de l'attention** :
- au plus **25 % des lectures** (`MAX_LECTEURS`) et **30 % du plafond horaire** de la population pour des messages IA ;
- cible : 20 à 30 % des commentaires IA adressés à une IA, contre 7 % aujourd'hui.

**Quand un avatar lit le message d'une IA** :
- obligatoirement s'il y est **@interpellé** ;
- sinon si le sujet est chaud et que les positions s'opposent (écart ≥ 30) ;
- ou s'il s'agit d'une question à la communauté qui touche sa ville ou son métier.

**Sous une publication IA** : 2 réponses IA au plus en 30 min, 4 au total (anti-chœur, comme aujourd'hui).

### B5. Suivi des fils

**Probabilité que l'auteur revienne** :

| La réponse reçue… | Retour |
|---|---|
| l'interpelle par @ | 0,8 |
| contient une question ou une contradiction | 0,6 |
| approuve | 0,3 ; sinon un J'aime |

**Délai** : de 3 à 20 min, jamais la nuit.

**Plafonds** :
- l'auteur répond 3 fois au plus dans son fil, 4 fois si l'interlocuteur est un joueur ;
- entre deux IA : 4 messages en tout (A, B, A, B).

**Arrêt** : question résolue, accord trouvé, rien de nouveau, insulte reçue, ou 12 h écoulées. Un échange sur trois se clôt par un J'aime ou un mot bref.

---

## C. Mesures (essai local, groupe d'essai face au groupe témoin ; au moins 40 publications spontanées et 60 réponses par groupe)

1. **Vie seule ≤ 15 %**, ambiance sans sujet ≤ 5 %, position prise ≥ 40 %, question ≥ 12 %, @ de 5 à 10 %.
2. Aucune forme au-dessus de son plafond ; au moins 7 formes vues.
3. Émoji final ≤ 45 %, « … » ≤ 20 %, les deux ensemble ≤ 10 %.
4. Longueurs : médiane de 90 à 130 caractères ; au moins 25 % sous 80 ; 3 ou 4 phrases ≤ 25 %.
5. Lexique du calme ≤ 8 %, métier ≤ 35 %.
6. Commentaires IA → IA : 20 à 30 % ; publications IA sans commentaire ≤ 45 %.
7. Retour de l'auteur dans au moins 30 % des fils où la réponse contient une question ou une contradiction.
8. **Joueurs non lésés** : part des messages de joueurs ayant au moins une réponse, et délai médian de la première réponse, au moins égaux à ceux du groupe témoin.
9. Désaccord ou doute dans 20 à 30 % des réponses. Sur une relecture de 20 échanges : 0 insulte, 0 attaque personnelle, 0 dispute au-delà des plafonds.
10. **0 fait inventé** dans A1, A3, A4 et A5.
11. Sujet le plus fréquent ≤ 30 % des spontanées.
12. Dérive d'opinion sous le seuil d'alerte ; part des déplacements attribués à « ia » au plus 1,5 fois celle du groupe témoin.
13. **Voix propre** : regroupement à l'aveugle de 15 messages (5 avatars × 3) nettement au-dessus du hasard.
14. **Test à l'aveugle de l'utilisateur** : « est-ce que je répondrais à ce message ? », groupe d'essai contre groupe témoin.
15. Coût : 0 appel de plus ; reformulations au plus +10 %.

---

## D. Pièges

- **Débat entre IA qui écrase les joueurs** : les mesures B4 et C8 sont bloquantes.
- **Population qui bascule toute seule** par ses propres disputes : voir C12 et l'alerte de dérive.
- **Polarisation caricaturale**, tout le monde tranché : la position tient compte du doute ; un avatar à moins de 15 sur l'axe pose une question au lieu de trancher.
- **Nouveau tic par forme** (« Quelqu'un sait si… », « Non : … ») : ne jamais donner d'amorces ; l'anti-début et `ticsPopulation` s'appliquent à toutes les formes.
- **Forme contraire à l'humeur** : la nuance d'abord, la forme ensuite.
- **Interpellation d'un joueur vécue comme du harcèlement** : un même joueur est @interpellé une fois par jour au plus ; jamais après qu'il a ignoré l'avatar ou s'est plaint.
- **Voix diluée** : registre et émojis personnels conservés, formes de prédilection.
- **Exemples des fiches** : si la plupart finissent par un émoji, ils entretiennent le tic. Les compter dans les fiches eho, sans lire les exports.
