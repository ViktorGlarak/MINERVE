# Avis n°18 — Première demi-heure en production : le chœur de la solidarité (2026-10-12)

**Auteur** : PSYCHOLOGUE · **Demandeur** : NOYAU (pour PLEIADE)
**Sources** :
- relevé `AVIS\2026-10-11_RELEVE_POPULATION_10h10.md` (il est daté du 11 par erreur d'outil : c'est le 12/10 à 10 h 10) ;
- export `C:\Users\MTR\.pleiade\analyses-ia\moteur-ia_export_2026-10-12_1009.json` (journal, cycles 57 à 72, `population.avatars[].etat`) ;
- code lu, sans le modifier : `app-ia\src\moteur\pont.mjs` (`filDe`, `proposer`, `CHOEUR`, `ticsPopulation`, `gabaritsPopulation`, boucle de lecture l. 554-640), `esprit.mjs` (`persona` l. 1000-1018, Q7, `retirerFormulesCreuses`, `relireHybride`).

> **Fenêtre jugée** : de 9 h 46 à 10 h 10 (heure de Paris), soit les cycles 61 à 68, après la correction d'`IA_T0`. Avant 9 h 45, le moteur tournait avec une heure interne négative, et cette période n'est **pas** jugée sur le comportement. La version app-ia 2026-10-12.7 (reprise des # du message parent) n'est en ligne que depuis 10 h 06 : aucun message relevé ne la concerne.
> **Messages de joueurs** : aucun extrait nominatif n'est recopié ici. Les comptes humains (joueurs ou animation, que le relevé ne distingue pas) sont désignés H1, H2 et H3.

---

## 1. Diagnostic de la première vraie demi-heure

### 1.1 Les chiffres (24 min)

| Mesure | Valeur | Commentaire |
|---|---|---|
| Lectures (somme des cycles) | 160 | NOYAU en compte 273, sans doute avec un autre décompte |
| J'aime IA | 70 | |
| Réponses IA publiées | **16** | |
| Publications spontanées publiées | 3 | 12 brouillons, dont 9 retenus « rien ne le pousse à écrire » |
| Retenues par la relecture | 2 | deux « Bon courage », justement retenues |
| Bloquées / erreurs | 0 / 0 | |
| Part de l'IA dans les événements du réseau | **37 %** (19 sur 52) | acceptable sur le réseau entier |
| Réponses IA sous **une seule** publication (H1, annonce d'un groupe d'entraide) | **11 sur 16 (69 %)** en 4 min 58 s, contre 2 réponses humaines | dans ce fil, l'IA fait **85 %** des réponses |
| Réponses IA sous des messages humains de détresse ou de solidarité (H1, H2, H3) | 15 sur 16 | 1 seule réponse d'IA à IA (kenaupifObiwan → RudyKafMob) |
| Réponses qui étaient au départ des **partages** convertis par la règle « partage sans information → réponse » | **15 sur 16** (journal) | c'est la cause n°1 (§2) |
| Réponses faites de formules (courage, bravo, initiative, force à vous) | 15 sur 16 | « initiative » 7 fois sur 11 sous H1 |
| Réponses qui apportent un élément concret (aide proposée, question pratique, info locale, fait vécu) | **0 sur 15** | les deux réponses humaines du fil proposent, elles, une voiture et un relais |
| Rapport J'aime / réponses | 4,4 | on attend ≥ 8 (règle 1-9-90 : on aime beaucoup plus qu'on ne répond) |

### 1.2 Ce qui sonne vrai

- **Les publications spontanées publiées sont ancrées dans une vie** :
  - Kuz_MarketingPro (agricultrice, HToul) : les convois sur la départementale, puis « nourrir les bêtes, ça me fera du bien de bouger ». Le code a retiré son « Courage à tous », et le message en sort meilleur ;
  - RudyKafMob : HSarrebourg, les gares, les convois, l'attente d'infos de la préfecture ;
  - Lav_Gru_Icon : une recherche d'emploi à HChaumont.
- **La seule réponse d'IA à IA est juste** : kenaupifObiwan répond à RudyKafMob sur l'attente. Son 🛠️ vient de son métier (il est mécanicien) : l'émoji a un sens. Il tombe un peu à plat, mais ce n'est pas un défaut de fiche.
- **K_Rud_85 sous H3** (une proche sur la D32) : une compassion sobre et à sa place.
- **Aucun événement de guerre inventé dans les messages, aucune orientation inversée, aucune invention de vie publiée.** La couleur politique reste discrète chez les neutres : 7 % de messages colorés.
- **Les garde-fous de code ont travaillé** :
  - le tic de l'émoji ❤️ a été attrapé au 4e emploi (2 reformulations) ;
  - une formule creuse a été retirée (Kuz) ;
  - 11 blocs nocturnes ont été refusés à juste titre (4 orientations inversées, 2 inventions de vie « mes trois enfants » contre 4 dans la fiche, 4 moules, 1 événement inventé) ;
  - 9 publications spontanées ont été retenues, et c'était souvent heureux (§1.3).
- **L'humeur ne sombre plus** : valence moyenne +4,9 (de −10 à +37), plus aucune tristesse uniforme (tristesse 6, peur 8, tendresse 8, neutre 10, sans émotion 71). Le défaut de l'avis n°17 est corrigé. Il faudra seulement vérifier qu'un avatar qui habite près de la D32 n'est pas serein (§5).
- **Le volume global est bon** : l'IA fait 37 % des événements et n'écrase pas le réseau. **Le problème est sa concentration, pas sa quantité.**

### 1.3 Ce qui sonne faux

1. **Le chœur de la solidarité (défaut majeur).** Sous H1, onze inconnus écrivent la même chose en cinq minutes : « Super initiative » ×4, « Bravo pour l'initiative ! ❤️ » / « Bravo pour cette initiative » ×3, « Courage à toute l'équipe » ×2, « C'est magnifique ce que vous faites ». Sur un vrai réseau, une annonce de ce genre reçoit beaucoup de J'aime, quelques partages, et un ou deux commentaires **concrets** (« j'ai des couvertures, je dépose où ? », « vous êtes où exactement ? »). Ici, c'est l'IA qui fait du bruit et les humains qui apportent de l'aide. Un joueur repère la population IA au premier coup d'œil.
2. **Les pensées sont identiques.** Sous H1, 9 pensées sur 11 commencent par « C'est super / bien / beau / courageux… ». Selon la règle de l'avis n°13, des pensées identiques veulent dire que **le chœur est déjà dans l'invite** : le défaut est en amont, pas dans la formulation. Les 25 lecteurs reçoivent la même publication, avec le même cadrage, sans savoir que d'autres ont déjà répondu.
3. **Personne ne répond à la question posée.** H2 (une famille arrivée dans la nuit) demande explicitement une info. Quatre avatars ont essayé de lui répondre, et tous ont écrit « Bon courage » (2 publiés, 2 retenus). Pas un lieu, pas un « je ne sais pas, mais la mairie… ». C'est un défaut de pertinence (Q4) que rien ne contrôle.
4. **Le moule des publications spontanées.** Sur 12 brouillons, **8** contiennent « j'ai du mal à me concentrer / difficile de se concentrer / pas facile de rester concentrée / dur de rester motivée », **6** commencent par « Entre… et… » et 5 contiennent « ici à H[ville] ». La retenue « rien ne le pousse à écrire » a évité un deuxième chœur par chance. Deux de ces messages sont quand même passés (Kuz, Lav_Gru_Icon). Ce moule vient en partie des blocs nocturnes : **14 sur 95** contiennent « concentr » et 14 commencent par « entre ».
5. **Des réponses en rafale chez le même avatar** : BenitskyBogdan répond à deux fils en **2 secondes**, IvaStockPro_ en 18 secondes. Une personne réelle ne fait pas ça.
6. **Défauts mineurs** :
   - « la la préfecture » chez RudyKafMob : le remplacement de `PrefHGrandEst` ne tient pas compte de l'article déjà écrit ;
   - le relevé annonce 103 avatars animés, alors que 100 sont attendus si les 5 avatars de scénario sont en pause. À vérifier.

---

## 2. Le chœur et ses causes dans le code

Le chœur n'a pas une seule cause : c'est une **chaîne de six maillons**, et chacun laisse passer ce que le précédent a produit.

| # | Maillon | Où dans le code | Ce qui s'est passé |
|---|---|---|---|
| 1 | **Exposition simultanée** | `filDe` (pont.mjs l. 268-279) | H1 a vite eu 5 ♥. `popularite ≥ 2` et le tri par popularité placent la publication **en tête des 4 lectures** (`LECTURE = 4`) de presque tous les avatars éveillés, **dans les mêmes cycles** (65-66). `MAX_LECTEURS = 25` borne le nombre total de lecteurs, mais pas leur **débit** : jusqu'à 25 lecteurs en 3 minutes. |
| 2 | **Une invite qui pousse au partage** | `persona`, esprit.mjs l. 1010 | « PARTAGER vaut mieux qu'aimer quand on est d'accord et que ça touche … sa ville ». Une annonce d'entraide sur la D32 coche toutes les cases, donc le modèle choisit « partager » avec un « mot court ». Un mot court de partage, c'est précisément « Bravo pour l'initiative ❤️ ». |
| 3 | **La conversion du partage en réponse** (règle n°2 de mon avis n°12, mal outillée) | pont.mjs l. 564-567 | Un partage sans fait, sans source officielle et sans # de campagne devient une **réponse qui garde le mot de partage**. Résultat : **15 des 16 réponses**. L'avis n°12 disait « compatir = répondre **ou aimer** ». Le code a choisi « répondre » à tous les coups, et transforme ainsi un geste muet en commentaire creux. Il y a aussi un angle mort : un **appel à l'aide précis** (groupe d'entraide, point de dépôt, besoin de bénévoles) est une information **utile** qui mérite de circuler. Le partager était juste. |
| 4 | **Un anti-chœur trop étroit** | `CHOEUR` / `choeurPlein` (l. 365-382) | Il ne compte que les réactions **sous déclencheur de voix de cohorte** (messages colorés), par bloc. Une réponse neutre de compassion n'y entre jamais : ce compteur ne sert à rien contre un chœur de solidarité. |
| 5 | **Un anti-tic qui ne voit pas les formules courtes** | `ticsPopulation` (l. 255-260) et `gabaritsPopulation` | L'anti-tic travaille sur des groupes de 4 mots, dont 2 mots pleins de 5 lettres ou plus, écrits par **au moins 2 autres avatars**. « Super initiative » (2 mots) et « Bravo pour l'initiative » (3 mots) passent sous le seuil. Aucun gabarit ne couvre les formules d'éloge. Seul le ❤️ final a été attrapé. |
| 6 | **Formules creuses et relecture** | `retirerFormulesCreuses` (esprit.mjs l. 1261-1270), Q7, groupe témoin | (a) La liste ne contient que des formules d'**ambiance** (courage à tous, tenez bon…), pas d'**éloge** (super initiative, bravo pour…). (b) **Faille** : si le message n'est **qu'une** formule (reste < 25 caractères), la fonction rend le texte **intact**. C'est ainsi que « Bon courage pour la suite. » d'IvaStockPro_ est publié. (c) 6 réponses sur 11 sous H1 viennent du **groupe témoin**, qui n'a pas de relecture. Les 5 réponses relues passent Q7, parce que l'éloge n'est pas listé. Q7 a attrapé les 2 « Bon courage » (précision 2 sur 2). |

**Pourquoi l'anti-chœur local a suffi et pas la production.** En local, les avatars se lisaient surtout entre eux. Les messages déclencheurs étaient **colorés** (donc comptés par `CHOEUR`), dispersés, et rarement aimés en quelques minutes. En production, **un seul message humain émouvant** reçoit des J'aime réels, devient « populaire » au sens de `filDe`, et part d'un coup chez 25 lecteurs. Il **n'est pas coloré**, donc aucun compteur ne le protège. Le prompt pousse au partage, la règle n°12 convertit chaque partage en commentaire, et aucun plafond **par message** n'existe : on a seulement un plafond par avatar (rythme horaire) et un plafond par population (40 par heure, pas atteint en 24 min). Le taux de réponse observé dépasse 50 % des lecteurs de H1 (13 tentatives d'écriture pour 25 lecteurs au plus). Le réel, pour le message d'un inconnu, se situe autour de 1 à 5 %.

---

## 3. Améliorations du moteur, par priorité

### Priorité 1 : stopper le chœur (sans attendre)

**M1. Plafond de réponses IA par publication**
- Compteur `REPONSES_IA[pubId]`, incrémenté **au moment de la décision** (dans la boucle, de façon synchrone, avant la relecture et avant le délai de publication). Sinon, les réponses programmées mais pas encore publiées échappent au compte.
- Publication d'un compte **sans lien** avec le lecteur : **2 réponses IA au plus par tranche de 30 min, 4 au total**.
- Exemptés (ils ne consomment pas le quota) : l'interpellation (`@handle`), la réponse à son propre message, un auteur suivi ou une relation au moins « connaissance ».
- Fil d'IA à IA : 2 réponses IA au plus sous un message d'IA.
- Quota atteint : l'action devient **J'aime** si `ressenti_fond` vaut `d_accord` ou si `ressenti_forme` vaut `touchee`, sinon **ignorer**, avec la note « fil déjà fourni ».

**M2. Refaire la conversion « partage sans information »**
- Un message **actionnable** se partage (aussi pour un non-relais), avec 2 partages IA au plus par publication. Repérage par une liste de mots, par exemple `groupe d'entraide | collecte | dépos(er|ez) | point d'accueil | bénévoles | covoiturage | hébergement | on cherche | besoin de | si quelqu'un (a|sait)`.
- Un message d'humeur partagé sans information devient un **J'aime**, pas une réponse. Il ne devient une réponse que si le mot d'accompagnement passe le test de substance de M4.
- Dans `persona`, remplacer « PARTAGER vaut mieux qu'aimer quand on est d'accord et que ça touche son camp, sa ville… » par « PARTAGER sert à faire circuler une **information utile** (un fait, une consigne, un appel à l'aide précis) ; pour dire qu'on approuve ou qu'on compatit, un J'aime suffit ».

**M3. Une réponse faite d'une seule formule devient un J'aime, et les formules d'éloge entrent dans la liste**
- Dans `retirerFormulesCreuses` : si une formule est trouvée et que le reste fait moins de 25 caractères, renvoyer `{ vide: true }`. L'appelant transforme alors la réponse en J'aime (ou en « ignorer » si l'avatar n'est pas d'accord), au lieu de rendre le texte intact.
- Ajouter les formules d'éloge et de soutien :
  - super / belle / chouette initiative ;
  - bravo pour (l' / cette / votre / ton) initiative ;
  - c'est (super / magnifique / beau / génial) ce que (vous faites / tu fais) ;
  - force à (vous / toi / toute l'équipe) ;
  - courage à (elle / lui / eux / toute l'équipe) ;
  - bon courage pour la suite ;
  - merci pour (ce / ton / votre) (partage / message).
- Ces règles de **code** s'appliquent à **toute la population**, groupe témoin compris. Le témoin ne sert qu'à mesurer la relecture par le modèle.

### Priorité 2 : faire répondre différemment, au bon moment

**M4. Diversité imposée : « ce qui a déjà été dit » et un test de substance**
- **Invite** : sous toute publication qui a déjà au moins une réponse (humaine ou IA) dans les 2 dernières heures, afficher les **4 dernières réponses** (100 caractères chacune), suivies de : « Si tu réponds, apporte UNE chose que personne n'a dite : ce que TOI tu peux faire (vu ton métier, ton lieu, tes moyens), une question pratique, une info de ton coin, ou une réserve. Sinon, un J'aime suffit. »
  - Le bloc `vie` donne de quoi le faire. IvaStockPro_ est chauffeur routier, kenaupifObiwan est mécanicien, BenitskyBogdan est éducateur sportif : chacun peut proposer une aide concrète et différente.
- **Code**, avant la relecture : une réponse dont les mots pleins recouvrent ceux d'une réponse existante sous le même message (Jaccard ≥ 0,4), ou qui commence par les mêmes 2 mots, ou qui partage un mot d'éloge (initiative / bravo / super / courage / force) avec au moins 2 réponses du fil, devient un **J'aime**.
- **Test de substance** (sous un message humain) : une réponse doit contenir au moins un de ces éléments, sinon elle devient un J'aime :
  - une question (« ? ») ;
  - une offre (« je peux », « j'ai », « je passe », « je dépose ») ;
  - un lieu ou un horaire ;
  - un fait vécu à la 1re personne.

**M5. Étalement des lectures et des réponses**
- **Délai de publication** d'une réponse à un message qui n'interpelle pas l'avatar : tiré dans une loi log-normale, **médiane 3 min, de 1 à 20 min**. Aujourd'hui, il va de 5 à 45 s. Les interpellations et les messages privés gardent leur délai court.
- **Même publication** : au moins **3 min** entre deux réponses IA programmées (on décale l'heure de publication).
- **Même avatar** : au moins **2 min** entre deux messages publics (aujourd'hui, BenitskyBogdan en publie deux en 2 s).
- **Débit de lecture** : **8 nouveaux lecteurs au plus par tranche de 10 min** sur une même publication. Au-delà, `filDe` ne la propose plus pendant le reste de la tranche. Le total de 25 sur 6 h ne change pas.
- **Tri de `filDe`** : multiplier la popularité par un aléa U(0,5 ; 1,5), pour que tous les avatars n'aient pas la même tête de fil au même cycle.

**M6. Pertinence : répondre à la question posée**
- Si le message parent pose une question ou demande de l'aide (« ? », « si quelqu'un », « quelqu'un sait », « on cherche », « une info »), la réponse doit contenir une piste (lieu, service, numéro de la préfecture déjà publié, « je ne sais pas, mais… ») ou une offre. Sinon, elle devient un J'aime.
- Compléter Q4 : « … ou le message cité pose une question ou demande de l'aide, et la réponse n'y répond pas ».

### Priorité 3 : moules, hygiène, hashtags

**M7. Moule des publications spontanées**
- Élargir le gabarit « concentration » : `/(du mal|dur|difficile|pas facile|compliqué|n'arrive (pas|plus)|impossible)[^.!?]{0,30}(concentr|motiv|bosser|travailler)/i`. Au plus **2 par heure** dans la population et **1 par jour** par avatar.
- Nouveaux gabarits :
  - message qui commence par « Entre (deux / le / la / les) … » : au plus 2 par heure ;
  - « ici à H[Ville] » : au plus 3 par heure.
- Ajouter « concentr » et l'ouverture « Entre… » à l'anti-moule du bloc nocturne (14 blocs sur 95 sont concernés).
- Dans l'invite de lecture, rappeler que `publication` vaut **null la plupart du temps** : aujourd'hui, 12 brouillons pour environ 25 lectures.

**M8. Hygiène de l'horloge interne et petit correctif**
- **95 avatars** ont `reflexion_t = −1430,7` et **61** ont `humeur.derniere` négatif : ce sont des traces de la période où `IA_T0` était faux. Il faut :
  - remettre `humeur.derniere` à l'heure courante ;
  - faire **rejouer la nuit prochaine les 95 blocs « où j'en suis » sans la règle des 40 %**. Ils ont été écrits le matin, sous une mauvaise heure, et une première version fautive ne doit pas devenir canon (règle de l'avis n°17).
  - Les 145 souvenirs ont une heure positive : rien à faire de ce côté.
- Corriger « la la préfecture » : remplacer `(\b[Ll]a |\b[Ll]e )?@?PrefHGrandEst` par « la préfecture », sans doubler l'article.

**M9. Reprise des # (12.7) : garde-fou contre l'amplification**
- Ne faire hériter le # qu'aux réponses qui ont passé M1 à M4. Un chœur de 11 réponses aurait mis 11 `#Réfugiés` d'origine IA dans le Cockpit et faussé l'analyse.
- Mesurer, par hashtag, la part de l'IA dans le volume horaire. Cible : **au plus la part de l'IA sur tout le réseau + 10 points**.

### Critères de réussite (prochain export, 2 h de jour au moins)

| Critère | Aujourd'hui | Cible |
|---|---|---|
| Réponses IA par publication sans interpellation, par tranche de 30 min / au total | 11 en 5 min | **≤ 2 / ≤ 4** |
| Part de la publication la plus commentée dans les réponses IA de l'heure (si au moins 10 réponses) | 69 % | **≤ 30 %** |
| Part de l'IA dans les réponses d'un fil humain | 85 % | **≤ 50 %** |
| Réponses faites d'une seule formule | ≥ 1 (IvaStockPro_) | **0** |
| Lexique de formules (courage, bravo, initiative, force à, super…) dans les réponses IA | 94 % | **≤ 15 %** |
| Paires de réponses IA quasi identiques sous le même message (Jaccard ≥ 0,4) | nombreuses | **0** |
| Réponses IA à un message humain qui apportent un élément concret | 0 % | **≥ 40 %** |
| Conversions « partage → réponse » parmi les réponses | 94 % | **≤ 20 %** |
| Écart médian entre deux réponses IA sous le même message | ≈ 27 s | **≥ 3 min** |
| Rapport J'aime / réponses IA | 4,4 | **≥ 8** |
| Question humaine qui reçoit des réponses IA | 0 réponse qui y répond | **≥ 1 piste ou « je ne sais pas, mais… »** |
| « concentr / motiv » et ouverture « Entre… » dans les publications spontanées | 8 et 6 sur 12 | **≤ 2 par heure chacun** |
| Messages humains qui répondent à une IA (indice de crédibilité) | à mesurer | en hausse, à relever |

---

## 4. Corrections de fiches individuelles

**Aucune.** Les défauts de cette demi-heure viennent de la **population et du moteur**, pas d'une fiche :
- les réponses en chœur viennent d'avatars différents, chacun avec un message plausible pris isolément ;
- le 🛠️ de kenaupifObiwan a un sens (il est mécanicien) ;
- les inventions « mes trois enfants » de Bon_VRprof et Taisiya_88 ont été refusées à juste titre, et leur fiche (4 enfants) fait foi ;
- les 4 orientations inversées (TeleCityKov, BenitskyBogdan, Kolee_Nik, Lepetitfreredebazouzou) se trouvent dans des blocs **écrits sous la mauvaise heure**. On les rejuge après le rejeu prévu en M8, pas avant.

Aucun fichier `corrections\2026-10-12_avis18.json` n'est créé.

---

## 5. Ce qu'il faudra regarder au prochain export

1. **Reprise des #** (12.7) :
   - part des réponses IA qui reçoivent un # hérité ;
   - seuls les # du parent sont repris, sans invention ni accumulation (au plus 1 ou 2) ;
   - aucun # hérité dans une réponse qui **conteste** le parent (sinon, un opposant porterait le slogan de l'autre camp) ;
   - aucun message ne dépasse 280 caractères à cause de l'héritage ;
   - part de l'IA par hashtag (M9) ;
   - premières reprises enregistrées pour #Réfugiés (accord net +1,2, 5 avatars à +2 ou plus).
2. **Le premier message humain émouvant après M1 à M6** : nombre de réponses IA, écart entre elles, éléments concrets, et réaction des humains (est-ce qu'un joueur répond à une IA ?).
3. **Les critères du §3**, et en particulier le rapport J'aime / réponses et la part des conversions.
4. **Le rejeu des 95 blocs nocturnes** (M8) : critères de l'avis n°17 (événements inventés, orientation, moule « je travaille toujours / je continue mes », vie), plus le nouveau moule « concentr ».
5. **Humeur selon la distance à la D32** : un avatar de HToul, HSaint-Dié ou HRambervillers ne doit pas être au-dessus de +20 un matin d'exode. Un avatar de HChaumont ou HSarrebourg peut l'être.
6. **Population animée** : 100 attendus si les 5 avatars de scénario sont en pause, et non 103. Vérifier qu'aucun de ces 5 n'écrit.
7. **Section 11 (relecture)** : les abandons (20 %) sont ici des « Bon courage » transformés en J'aime, ce qui est le **bon** résultat. Il faut les compter à part des vrais échecs de reformulation, sinon le critère C5 est faussé.
8. **Opinions** : aucun mouvement de 3 points ou plus en 24 min, ce qui est normal. Il faut au moins 2 h d'injects pour juger la contagion en production.
