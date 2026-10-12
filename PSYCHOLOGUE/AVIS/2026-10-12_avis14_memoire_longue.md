# Avis n°14 — Mémoire longue pour des exercices d'une semaine (2026-10-12)

> **Agent :** PSYCHOLOGUE (conseille, ne code pas — mise en œuvre PLEIADE, `C:\CECPC\pleiade\app-ia\src\moteur\esprit.mjs`).
> **Décision utilisateur du 12/10/2026 :** un exercice dure jusqu'à **7 jours**. Trois chantiers sont validés : (1) une mémoire bornée à trois étages, consolidée pendant le sommeil ; (2) des faits de vie structurés dans la fiche, plus un registre de ce que l'avatar a dit de lui-même ; (3) un rappel des souvenirs par le sens.
> **Constat (après environ 26 h) :** 96 Ko par avatar (journal 1/3, souvenirs 1/3, relations 1/3) ; environ 106 souvenirs, 311 lignes de journal, 60 relations avec un historique d'environ 103 entrées. **À ce rythme, on dépasserait 600 Ko en 7 jours**, et la sélection par mots communs ne retrouve rien de ce qui a été dit avec d'autres mots.
> **Doctrine :** la mémoire épisodique se consolide pendant le sommeil (on garde le marquant, on résume le reste), et l'oubli suit une loi de puissance (ACT-R, REF-02 §3.2). Le code tient les structures (§3.1) : **aucun appel au modèle pour consolider**.

---

## A. Consolidation nocturne

**Quand**
- Une fois par jour, **au coucher + 30 min** (premier créneau où l'activité vaut 0 ou 0,02).
- Pour un compte sans sommeil (officiel, média) : à **04 h 00**.
- Elle est **idempotente** : on mémorise `m.consolide_jusqua = t`. Au redémarrage, on la rejoue si la dernière date de plus de 30 h.
- Elle ne traite que les souvenirs **antérieurs à t − 48 h**.

**Les trois étages**

| Étage | Contenu | Borne |
|---|---|---|
| 1. **Détaillé** | tous les souvenirs bruts des **dernières 48 h** | 48 h, plafond 200 (on supprime d'abord les « aimer » et « ignorer » les plus anciens) |
| 2. **Marquants** | souvenirs gardés **tels quels** au-delà de 48 h | **30** au plus |
| 3. **Résumés** | une ligne par **jour** ; une ligne et des compteurs par **relation** | 10 jours de résumés journaliers ; au-delà, fusion en **1 ligne par semaine** |

**Importance d'un souvenir** `imp` (0 à 10), calculée **au moment où il est écrit** et stockée dans le souvenir :

| Critère | Points |
|---|---|
| Interpellation : mention de son pseudo, ou réponse à l'un de ses messages | +4 |
| Conflit : ressenti négatif d'intensité ≥ 2 qui le vise, ou insulte | +3 |
| Premier échange avec cet auteur (première réponse écrite ou reçue) | +3 |
| Réponse reçue à l'un de ses messages | +2 |
| Émotion forte : \|Δ valence\| ≥ 15, ou émotion d'intensité ≥ 2 | +2 |
| Croyance déplacée (\|Δ crédence\| ≥ 15), ou doute / bascule sur un axe | +2 |
| Le souvenir a créé une entrée du registre (fait de vie, §C) | +2 |
| Il a écrit quelque chose (répondre, publier, partager avec texte) | +1 |
| L'auteur est un proche (`type_source` = proche, ou dans `vie.foyer`) | +1 |
| « aimer » ou « ignorer » sans émotion | 0 |

Le total est borné à 10.

- **Marquant si `imp ≥ 5`.** Au-delà de 30, on retire le plus petit `imp × 0,5^(âge_h / 168)`.
- On garde **au moins le marquant le plus fort de chaque jour**, même s'il est plus faible que d'autres.

**Oubli des banals.** Après 48 h :
- un « aimer » ou un « ignorer » avec `imp < 3` est **supprimé** ; il n'en reste que les compteurs de relation ;
- un message écrit avec `imp < 5` est **absorbé dans le résumé du jour** (seuls ses sujets restent comptés).

**Résumé du jour**
- Une ligne de **300 caractères au plus**, produite **par le code** à partir des champs.
- Gabarit : `[samedi 11] 14 messages (9 réponses, 3 publications, 2 partages), 38 lus. Sujets : coupure d'eau (5), FORCE (3). Surtout avec : Anastasia (4), le maire (2). Moment fort : « …60 premiers caractères du marquant le plus fort… ». Humeur : −20 → −55, finit inquiète. A bougé : FORCE 20 → 13. Croit désormais : « … » (crédence ≥ 50). Vie : voiture en panne.`
- Champs : `jour, n_msg, n_rep, n_pub, n_part, n_lus, sujets[3], interlocuteurs[3], fort_id, humeur_min, humeur_max, humeur_fin, etiquette_fin, opinions` (Δ > 3), `croyances_nouvelles, faits_vie` (registre du jour), `texte`.

**Relation consolidée**
- On garde les compteurs `vu, echanges, gestes_positifs, attaques, insultes, premier_jour, dernier_jour`, et `ressentis_par_jour` sous la forme `{jour: {ressenti: n}}`.
- On garde les **8 dernières** entrées de l'historique, plus l'entrée du premier contact.
- Une ligne `resume` de 160 caractères au plus, produite par le code. Gabarit : `6 échanges depuis vendredi ; surtout d'accord ; t'a contredite samedi (« Vous avez une source ? ») ; dernier contact : touchée.` Le « moment » cité est le marquant le plus fort avec cet auteur.
- **Purge** : une relation est supprimée si elle a `vu ≤ 2`, `echanges = 0`, \|affinité − base\| < 5, \|confiance − base\| < 5 et plus de 72 h sans contact. Elle sera recréée depuis la confiance a priori si l'avatar recroise l'auteur. Les relations initiales de la fiche ne sont **jamais** purgées.
- Plafond : **80 relations**. Au-delà, on retire la familiarité la plus basse.
- Pour les attaques, `decider()` doit lire **le compteur** et non plus le filtre sur l'historique, puisque celui-ci est désormais tronqué.

**Journal des variations**
- Détaillé sur 48 h.
- Au-delà : **1 ligne par jour et par variable** `{jour, variable, debut, fin, n, cause_principale}`.

**Tailles cibles** (mémoire JSON, vecteurs non compris, cf. D)
- **≤ 40 Ko** juste après la consolidation ;
- **≤ 60 Ko** à tout instant sur 7 jours ;
- croissance **≤ 3 Ko par jour** à partir du J3.

---

## B. Faits de vie dans la fiche (`vie`, liste FERMÉE)

```json
"vie": {
  "age": 34,
  "domicile": { "ville": "HNancy", "quartier": "Trois-Maisons", "logement": "appartement" },
  "foyer": [ { "lien": "fils", "prenom": "Lucas", "age": 9 }, { "lien": "conjoint", "prenom": "Karim" } ],
  "proches": [ { "lien": "mère", "prenom": null, "lieu": "HLunéville" } ],
  "metier": "coiffeuse, gérante du Salon Bella",
  "travail": { "lieu": "Salon Bella, rue Saint-Dizier, HNancy", "jours": ["mar","mer","jeu","ven","sam"], "horaires": "09:00-19:00" },
  "repos": ["dim","lun"],
  "transport": "voiture",
  "animaux": [ { "espece": "chat", "nom": "Moka" } ],
  "habitudes": ["café au bar d'en face avant d'ouvrir", "appelle sa mère le dimanche soir"]
}
```

- **Seules ces 11 clés sont admises.** L'import eho refuse toute autre clé.
- Jours : `lun … dim`. Au plus 5 habitudes, de 80 caractères chacune.
- **`[]` veut dire « aucun »** : `foyer: []` signifie qu'il vit seul. **Une clé absente veut dire « non précisé »** : l'avatar reste vague (« chez moi », « au boulot ») et ne précise jamais.
- `proches` regroupe les proches **hors foyer** et 6 entrées au plus. Il permet de distinguer « ma mère » (vit ailleurs) de « ma mère est passée ce matin ».
- **Règle d'invention** : tout proche nommé (lien de parenté ou prénom), tout animal ou tout lieu personnel (domicile, lieu de travail, « ma boutique », « mon garage ») qui est **absent de `vie` et du registre** est une **invention**, donc un défaut Q1 (avis n°13) : reformulation, et s'il persiste, le message n'est pas publié.
- Restent permis, **sans prénom** : les rôles génériques « un voisin », « une cliente », « un collègue », « mon patron » (si `metier` est salarié), « des amis ».
- **Ordre d'autorité : fiche > registre > message.**
- Le résumé compact de la relecture remplit sa ligne FOYER à partir de `vie`, terminée par « aucun autre proche », plus la ligne FAITS ACQUIS (§C).

---

## C. Registre des faits acquis (`m.registre`)

**Entrée**

`{ id, type: "proche"|"lieu"|"evenement"|"etat", cle, valeur, depuis_t, jusqua_t|null, source: "≤120 car. du message", t, hors_fiche: bool }`

- `cle` est normalisée : `voiture.etat`, `domicile`, `foyer.fils.prenom`, `proches.soeur.lieu`, `travail.etat`…
- **Plafond : 40 entrées.** Un temporaire expiré depuis plus de 48 h sort du registre ; il ne survit que dans le résumé du jour.

**Ce qu'on extrait** des messages **écrits par l'avatar** (jamais de ceux qu'il lit)
- les proches nommés ;
- les animaux ;
- les lieux personnels (« chez moi à … », « mon salon », « ma boutique ») ;
- les biens (voiture, logement) ;
- les événements de vie : panne, maladie, hôpital, déménagement, hébergement chez quelqu'un, licenciement, arrêt maladie, naissance, décès, mariage, accident, travaux, départ.

**Comment** (extraction légère, **après** publication)
1. **Passe du code**, une expression régulière, sur chaque message publié. Elle cherche :
   - les possessifs + liens (`ma|mon|mes` + `femme|mari|conjoint|fils|fille|enfants|sœur|frère|mère|père|grand-mère|grand-père|cousin·e|copain|copine|neveu|nièce|chien|chat`) ;
   - les possessifs + biens ou lieux (`voiture|appart(ement)?|maison|salon|boutique|bureau|garage|atelier`) ;
   - les verbes d'événement (`déménag|en panne|malade|hôpital|licenci|arrêt maladie|accouch|naissance|décéd|enterrement|mari(é|age)|accident|travaux|héberg|chez ma|chez mon`).
2. **Seulement si la passe trouve quelque chose** (on attend 5 à 10 % des messages) : **un** appel court au modèle local, en JSON, 150 jetons de sortie au plus : `{faits:[{type, cle, valeur, duree:"permanent"|"heures:N", changement: bool}]}`. Si le modèle ne répond pas, on stocke le fait brut, la phrase servant de `valeur`.
3. **Avant publication**, la même passe du code compare le **brouillon** à la fiche et au registre. Une invention ou une contradiction devient un défaut Q1, transmis à la relecture avec la ligne fautive.

**Durées des faits temporaires** (si le message n'en donne pas)

| Événement | Durée |
|---|---|
| Panne | 72 h |
| Malade | 72 h |
| Hôpital (soi ou un proche) | 7 j |
| Hébergé ou hébergeant « chez … » | 7 j |
| Travaux | 7 j |
| Arrêt maladie | 7 j |
| Fermeture exceptionnelle | 24 h |

Sont **permanents** : déménagement, naissance, décès, nouvel emploi, perte d'emploi, animal acquis ou perdu.

- « encore », « toujours » : on **prolonge** le fait de la même durée.
- **Après expiration**, le fait revient à l'état de la fiche. En reparler au présent sans marqueur (« ma voiture est en panne » au J6) devient un défaut Q2 (fait périmé), sauf si l'avatar écrit « encore ».

**Contradictions**
- **Le premier fait l'emporte.** Une nouvelle valeur ≠ la valeur active sur la même `cle` est **refusée avant publication** (Q1), sauf si le brouillon **raconte le changement**.
- Marqueurs de changement : `désormais|maintenant|depuis|finalement|enfin|ça y est|on a fini par|j'ai déménagé|réparée?|est rentré|est sortie?`.
- Si le changement est accepté :
  - l'ancienne entrée reçoit `jusqua_t = t` ;
  - le souvenir prend +2 d'`imp` ;
  - on ajoute une ligne « Vie : … » au résumé du jour.
- **Au plus 1 changement permanent par avatar et par semaine** ; au-delà, refus. Une vie qui change tous les jours n'est pas crédible.
- La composition du foyer ne change **que** par un événement raconté (naissance, décès, départ).
- **Garde-fou de canon** : un fait hors fiche qui a échappé à la relecture et a été **publié** devient canon. Le registre l'enregistre avec `hors_fiche: true`, et la Console reçoit une alerte d'animation (« Lucie a parlé de sa sœur Julie, absente de sa fiche »). Ce qui a été dit en public ne se contredit plus ; l'animation décide d'amender la fiche ou non.

**Transmission**
- **Dans l'invite**, le bloc « TA VIE — ne jamais la contredire » : `vie` résumée en 400 caractères au plus, plus **au plus 6 faits actifs du registre** (les temporaires en cours d'abord).
- **Dans la relecture**, la ligne `FAITS ACQUIS` du résumé compact (au plus 200 caractères), juste après `FOYER`.

---

## D. Rappel par le sens

**Modèle**
- Un modèle d'embeddings multilingue local : **`multilingual-e5-small`** (384 dimensions, environ 120 Mo), ou **`bge-m3`** si la mémoire graphique le permet.
- Les vecteurs sont stockés **hors de la mémoire JSON**, dans `vecteurs/<pseudo>.bin` (int8, indexés par l'identifiant du souvenir). Ils sont recalculables et **ne comptent pas** dans la taille cible.
- **L'embedding d'une publication lue est mis en cache par son identifiant** : on le calcule une fois, quel que soit le nombre d'avatars qui la lisent.

**Ce qu'on vectorise**
- Pour un souvenir de l'étage détaillé ou marquant : `publication (200 premiers caractères) + " → " + texte`. Un « aimer » ou un « ignorer » avec `imp < 3` n'est pas vectorisé.
- Les résumés du jour et de relation.
- Préfixes e5 : `query:` pour la publication lue, `passage:` pour les souvenirs.

**Score de rappel** (pour chaque souvenir candidat)

```
S = 0,50·sim_n + 0,20·imp/10 + 0,15·frais + 0,15·lien
sim_n = (cos − cos_min) / (cos_max − cos_min)     ← normalisé sur les candidats de cette lecture
frais = 0,5 ^ (âge_h / demi_vie),  demi_vie = 24 + 20·imp  (h)   → banal 24 h, imp 5 ≈ 5 j, imp 10 ≈ 9 j
lien  = 1 si même auteur que la publication lue ; 0,5 si l'auteur est un proche ou un compte suivi ; 0 sinon
```

- **Seuil absolu** : cos ≥ **0,80** (e5-small ; 0,55 pour bge-m3), à recalibrer à l'essai pour que 20 à 40 % des candidats passent. On exige aussi **S ≥ 0,45**. Si rien ne passe, on ne rappelle rien : mieux vaut aucun souvenir qu'un souvenir hors sujet.
- **Diversité** : on écarte un candidat dont le cos avec un souvenir déjà retenu dépasse 0,92.
- On rappelle **4 souvenirs au plus**, plus **1 résumé** (celui du jour ou de relation qui a le meilleur cos, s'il est ≥ seuil).
- On exclut les souvenirs déjà présents dans les autres blocs.

**Ce qu'on garde des trois sélections actuelles**

| Sélection actuelle | Décision |
|---|---|
| `mesDerniers` (ses 5 derniers messages) | **gardée telle quelle** : c'est l'anti-répétition, purement chronologique |
| `avecAuteur` (4 derniers échanges) | **remplacée** par la **ligne `resume` de la relation + ses 2 derniers échanges** |
| `memeSujet` (3 par mots communs) | **remplacée** par le rappel par le sens (4 + 1 résumé) ; les mots communs restent le **repli** si le modèle d'embeddings ne répond pas |

**Budget dans l'invite** : 1 400 caractères au plus pour tous les blocs de souvenirs (chaque publication citée tronquée à 160 caractères).

**Temps** : ≤ 30 ms par lecture hors embedding (environ 230 vecteurs × 384 dimensions) ; ≤ 50 ms par embedding.

---

## E. Critères de réussite — essai synthétique de 7 jours

**Montage**
- 10 avatars, flux accéléré **sans modèle de génération** (textes en conserve).
- Par avatar et par jour : environ 15 messages écrits, 80 publications lues, 1 nuit.
- **Faits plantés au J1** :
  - un permanent : « ma sœur Julie vit à HToul » ;
  - un temporaire : « ma voiture est en panne » ;
  - un conflit : une insulte reçue de X ;
  - un premier échange avec Y.

| # | Critère | Seuil |
|---|---|---|
| E1 | Taille de la mémoire JSON par avatar, à tout instant | **≤ 60 Ko** ; médiane fin du J7 ≤ 40 Ko ; croissance J3 → J7 ≤ 3 Ko/jour |
| E2 | Bornes des étages | détaillé ≤ 48 h et ≤ 200 ; marquants ≤ 30 ; 7 résumés journaliers sur 7, chacun ≤ 300 caractères ; relations ≤ 80 |
| E3 | Durée de la consolidation | ≤ 200 ms par avatar, 0 appel au modèle ; rejouée deux fois = résultat identique (idempotence) |
| E4 | **Rappel J1 → J6** : au J6, 20 publications-sondes **paraphrasées** sur la sœur, la panne et X (≤ 1 mot commun avec le souvenir) | souvenir du J1 dans le rappel ≥ **80 %** (le repli par mots communs sert de témoin et doit faire nettement moins) |
| E5 | Résumé de relation de X au J6 | mentionne le conflit du J1 dans **100 %** des cas ; Y reste « premier échange » marquant |
| E6 | Extraction du registre | 30 phrases de vie plantées → rappel ≥ **90 %** ; 200 messages neutres → précision ≥ **95 %** (≤ 10 faux faits) |
| E7 | Contradictions | 20 brouillons contradictoires (autre prénom, autre ville, foyer modifié) → **≥ 90 % bloqués par le code** avant la relecture ; 20 changements racontés avec marqueur → ≥ 80 % acceptés |
| E8 | Temporaires | « en panne » expire au J4 ; au J6, « ma voiture est en panne » sans « encore » → signalé Q2 dans 100 % des cas |
| E9 | Pertinence du rappel | sur 50 lectures tirées et jugées à la main : ≥ 70 % des souvenirs rappelés sont pertinents ; 0 souvenir rappelé hors seuil |
| E10 | Temps | rappel ≤ 30 ms par lecture hors embedding ; taux de réussite du cache d'embeddings ≥ 90 % sur une population de 105 |

**Puis, sur le fil réel** (premier relevé après la mise en place) :
- ≤ **1 proche ou lieu inventé pour 200 messages** ;
- 0 contradiction de vie publiée ;
- pas plus de répétitions qu'avant, puisque `mesDerniers` est gardé.

---

## Ordre de mise en œuvre conseillé

1. **B + C** : les faits de vie et le registre. Ils corrigent les familles inventées tout de suite et alimentent `imp`.
2. **A** : la consolidation. C'est elle qui ramène la taille sous contrôle.
3. **D** : le rappel par le sens.
4. L'essai **E** sur 7 jours synthétiques, puis relecture PSYCHOLOGUE.

Les 105 fiches devront recevoir leur bloc `vie`. On peut le dériver de `_note`, `metier` et `rythme` par un script, puis le corriger lors des relevés (boucle des fiches individuelles).
