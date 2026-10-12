# Banc IA — mesures sur le Mac (2026-10-12)

> Projet avatars IA, étape 5 « parc de machines ». Mesuré depuis le Mac. **À intégrer par PLEIADE (PC) dans `PLEIADE/PROJET_AVATARS_IA.md` § 8**, ce fichier n'étant qu'un relais entre les deux postes.

**Machine** : MacBook Pro M3 Max (14 cœurs CPU, 30 cœurs GPU), 36 Go de mémoire unifiée (~300 Go/s), Ollama 0.40.2.
**Modèles** : `gemma4:26b-a4b-it-qat` (15 Go) et `gemma4:31b-it-qat` (18 Go), téléchargés le 2026-10-12.
**Invite** : synthétique, proche d'une lecture du moteur : ~1 900 jetons en entrée (fiche courte + 30 publications), sortie JSON `{pensee, message}`, `think: false`, `num_ctx` 8192. Une invite **différente à chaque passage**, pour ne pas profiter du cache. Scripts : `vitesse.py`, `parallele.py`.

## Vitesse (3 passages, après chargement du modèle)

| Modèle | Total par lecture | Lecture de l'invite | Écriture |
|---|---|---|---|
| Gemma 4 26B (A4B) | **3,0 à 3,4 s** | ~1 000 jetons/s | ~73 jetons/s |
| Gemma 4 31B | **21 à 22 s** | ~130 jetons/s | ~14 jetons/s |

À comparer avec le PC (essai 3) : 26B **2,8 s**, 31B **20,6 s** (déborde de la carte).

## Constats

1. **Sur le 26B, le Mac vaut le PC.** En l'ajoutant au parc, on double le débit sans changer la voix des avatars : ~1 150 lectures/heure par machine.
2. **Le 31B n'est pas plus rapide sur le Mac que sur le PC** (~21 s), malgré sa mémoire suffisante. **2/3 du temps passe à lire l'invite** (130 jetons/s). Il est donc exclu pour le volume et possible seulement pour des appels **à invite courte** : la relecture (résumé ≤ 1 200 caractères, soit ~400 jetons) prendrait **environ 6-7 s** (estimation à mesurer sur une vraie invite).
3. **Effet du cache** : quand l'invite reprend exactement le même début qu'un passage précédent, le 31B tombe à **~7 s** et le 26B à **~1,3 s**. Piste : **ordonner les invites du moteur du plus stable au plus variable** (consignes → fiche de l'avatar → mémoire → fil) et garder un même avatar sur la même machine. À creuser avec la façon dont `esprit.mjs` construit l'invite.
4. **Parallélisme** : Ollama sur le Mac traite les requêtes **une par une** (réglage par défaut). 2 ou 4 requêtes simultanées donnent le même débit total. À réessayer avec `OLLAMA_NUM_PARALLEL=4`, qui demande de relancer Ollama.

## Banc sur les 14 VRAIES invites du moteur (app-ia 2026-10-12.13, exportées par le PC)

Script `banc.py` : rejoue chaque requête `/api/chat` telle quelle, en ne changeant que le modèle. Réponses complètes dans `resultats_gemma4_26b-a4b-it-qat.json` et `resultats_gemma4_31b-it-qat.json`. **Un seul passage par appel** : c'est un échantillon, pas une statistique.

### Temps (s)

| Appel | PC 26B* | Mac 26B | Mac 31B |
|---|---|---|---|
| Lecture (6 ; 3 900-6 100 jetons en entrée, ~500-650 en sortie) | 7,0-26,2 | **11,6-16,3** | 69-92 |
| Lecture avec publication (2) | 12,5-13,1 | **12,7-14,8** | 85-91 |
| Relecture (4 ; ~1 100 jetons) | 1,2-15,4 | **0,8-2,1** | 5,1-14,4 |
| Extraction des faits de vie (2) | 2,2-2,4 | **1,7-2,1** | 10,6-12,4 |

\* Mesuré sur le PC **pendant que sa carte servait aussi le moteur de production** : temps probablement majorés.

JSON lisible : **28/28**.

### Qualité

- **Relecture** : verdicts **identiques** sur les 3 versions (PC 26B, Mac 26B, Mac 31B). Les 2 messages normaux passent. Les 2 messages piégés sont repérés, et sur la bonne question (Q1 librairie un dimanche, Q7 « même bateau »). Le 31B est un peu plus fin : il sépare les deux formules creuses, et son remplacement « à la maison » est plus juste. **Le 31B n'apporte pas de gain décisif sur cet échantillon, pour un temps 5 à 7 fois plus long.**
- **Extraction** : équivalente. Le 26B du PC relève en plus « livraisons à vélo », et le 31B marque à juste titre la panne comme temporaire.
- **Lectures et publications** :
  - Le **31B a les meilleurs moments** :
    - une offre concrète avec son emploi du temps (« Je suis chauffeur sur HChaumont, je finis à 17h30… faites-moi signe ») ;
    - une scène vécue (« un monsieur qui partait avec tout son linge dans un sac plastique ») ;
    - un doute crédible (« Je n'ai rien lu sur Info.gouv.arn… je sais pas trop quoi croire »).
  - ⚠ Mais il a aussi **plus de chœur entre avatars** : « C'est important de s'entraider » mot pour mot chez 3 avatars différents (01, 05, 06), et « Bravo au resto » 3 fois.
  - Le 26B a ses propres formules (« la solidarité… ✊ », « On lâche rien ») mais **varie davantage d'un avatar à l'autre**.
  - À vérifier : la publication Mac 26B de G_Surfer_99 (« flux de blessés à l'hôpital ») invente peut-être un métier ou un fait hors fiche.

### Conclusion du banc
1. **Le Mac est un second nœud 26B à part entière** (~13 s par lecture réelle, ~275 lectures/heure). C'est le vrai gain : **doubler le débit** et le réinvestir dans le réalisme (relecture de toute la population, plus d'avatars parlants), sans changer la voix des avatars.
2. **Le 31B n'est pas à retenir pour le volume** (70-90 s par lecture), **ni pour la relecture** (aucun gain mesuré). Seul usage à essayer : la **rédaction des quelques avatars de scénario**, pour la richesse concrète, à condition que l'anti-chœur du code s'applique.
3. Avant de conclure sur la qualité, il faudrait **plusieurs passages par invite** et un relevé par critère (comme l'essai 3). Avec un seul passage, la variance l'emporte.

## Essai « décideur 26B + rédacteur » (idée retenue par l'utilisateur, 2026-10-12)

**Principe** : le 26B lit le fil et décide comme aujourd'hui. Pour chaque message qu'il choisit d'écrire, un **rédacteur** écrit le texte seul, à partir d'une **invite courte** (~2 000-3 000 jetons). Cette invite contient la fiche, la situation, les exemples et les règles absolues, sans les règles de décision ni le format. Elle y ajoute la publication lue, l'état de l'avatar, sa décision et sa pensée.
Script : `redacteur.py`. Résultats : `redacteur_resultats.json` (13 messages issus des 8 lectures, en 3 versions).

**Temps** : rédacteur 26B **1,5-4,1 s** par message ; rédacteur **31B MLX 17-25 s** par message, dont presque tout pour lire l'invite. Les messages d'une même lecture ne profitent pas du cache (pas d'accélération du 2e message), alors que c'était le cas avec la version `qat`.
**31B MLX en lecture complète** : 52-80 s (contre 69-92 s pour `31b-it-qat`), soit **~20 % plus rapide seulement**. Relecture 8-9 s, extraction 6-9 s.

**Qualité (à juger par l'utilisateur ; textes côte à côte dans le JSON)** :
- **Le 31B s'ancre mieux dans la vie de l'avatar** : « Je viens de voir ça entre deux livraisons », « Je repasse aux chèvres mais je partage », « Je suis en service sur HChaumont là ». Il **reformule** la pensée, quand le 26B rédacteur la **recopie** souvent (« Ah, ça c'est du concret ! », « La pause café est terminée… »).
- ⚠ **Les deux rédacteurs écrivent trop long et trop enthousiaste** (2 à 4 émojis, « Bravo pour l'initiative ! ») alors que l'avatar est **au travail**. Les textes en un seul appel sont plus courts et plus crédibles sur ce point. Cause : l'invite courte a perdu les règles de disponibilité (« au travail, au mieux une réponse courte ») et de concret, et « 280 caractères au plus » pousse à remplir. **À corriger avant toute conclusion** : longueur cible selon la disponibilité et les exemples, et remise des règles de réalisme utiles.
- ⚠ **Inventions** : « ma tournée » (P3trov_Sky) et « bloquées par les troupes ». *Rectifié après vérification* : « HVandœuvre » est bien le domicile de G_Surfer_99 dans TA VIE, et « canalisation à HToul » vient d'un souvenir (« HToul Infos ») : ce ne sont pas des inventions. La relecture du moteur devra s'appliquer au texte rédigé.
- Le chœur reste présent (« la solidarité c'est ce qui nous fait tenir »), parce qu'il vient de la **pensée** du décideur, que les deux rédacteurs reprennent.

**Incohérence de données repérée (pour PLEIADE / eho)** : `_OlegGaspi_` (Marta Lambert). La fiche dit **48 ans, 1 fils** ; le bloc « TA VIE » dit **28 ans, vit seul**. Le modèle reçoit deux personnages contradictoires. À vérifier sur les autres fiches (bloc `vie` généré le 2026-10-12).

### Essai v2 du rédacteur (`redacteur.py --v2`, résultats `redacteur_resultats_v2.json`)
Corrections apportées :
- longueur cible selon la disponibilité (au travail : une phrase, 120 caractères au plus, 0 ou 1 émoji) ;
- règles de réalisme : pas de formule d'encouragement générique, registre et émojis habituels respectés ;
- interdiction d'inventer un lieu, un métier ou un fait ;
- 2 souvenirs au plus sous la publication.

| Rédacteur | Temps par message | Longueur moyenne |
|---|---|---|
| 26B | **2,5 s** (1,1-3,4) | 85 car. |
| 31B `qat` | **18 s** (7-25) ; **7-10 s pour le 2e message d'une même lecture** (cache) | 87 car. |
| 31B MLX | **20 s** (17-24) ; pas de cache | 88 car. |
| *(26B en un seul appel, aujourd'hui)* | *(compris dans la lecture)* | *94 car.* |

**Constats** :
- Les textes sont désormais **courts et sobres** dans les 3 versions. Il y a nettement moins de « Bravo pour l'initiative » et d'émojis. Les publications spontanées sont nettement plus naturelles : « Fin du café, je remonte dans le bus. Je pense aux gens qui attendent sur la route. 🚌 » contre 3 phrases et une formule de fin en un seul appel.
- **Le gain vient surtout de l'INVITE DÉDIÉE, pas du modèle** : en v2, le 26B rédacteur et le 31B donnent des textes très proches. L'avance du 31B en ancrage concret (vue en v1) s'efface quand le texte est court. Il garde un léger plus : il utilise mieux la fiche (« l'hôpital de HVandœuvre ») et varie un peu mieux (« Enfin rentré chez moi… assurer ma ligne demain »).
- La « pensée » du décideur reste la source du chœur (« la solidarité c'est ce qui nous fait tenir ») : les rédacteurs la reprennent. C'est à traiter en amont, au niveau du décideur ou par l'anti-chœur.
- **Pour le 31B, `qat` vaut mieux que MLX** : le cache fonctionne avec `qat` pour les messages suivants d'une même lecture.

**Coût d'une lecture d'avatar (8 lectures réelles, ~1,6 message écrit par lecture)** :
- aujourd'hui (26B, un appel) : ~13 s ;
- décideur 26B + rédacteur 26B : **~17 s** (+30 %). Si le décideur n'écrit plus les textes, une partie de ce surcoût disparaît ;
- décideur 26B + rédacteur 31B `qat` : **~35-40 s** (×3) ;
- 31B seul : 52-92 s.

**Recommandation** : adopter **décideur 26B + rédacteur 26B** (presque tout le gain de qualité pour +30 % de temps). Réserver le **rédacteur 31B `qat`** aux **avatars de scénario et influenceurs**, peu nombreux, si l'utilisateur juge son léger plus visible.

**Données (pour PLEIADE / eho) — 2e cas confirmé** : G_Surfer_99 a **48 ans** dans la fiche et **35 ans** dans TA VIE (lieu de travail « inconnu », déplacement « inconnu »). Marta Lambert : 48 contre 28. **L'âge du bloc `vie` contredit la fiche** : contrôle de concordance à faire sur les 105 fiches.

## Essai v3 : rédacteur + DICTIONNAIRE DES ÉMOTIONS (`redacteur.py --v3`, `emotions.py`, `redacteur_resultats_v3.json`)
- Dictionnaire : `PSYCHOLOGUE/DICTIONNAIRE_EMOTIONS.json`. Le code choisit une nuance, que le rédacteur reçoit « à faire sentir sans la nommer ».
- **26B : 3,0 s par message** (+0,5 s) ; longueur 101 caractères (contre 85).
- **Gains** :
  - approbation réservée pour la râleuse sceptique ;
  - fierté personnelle au lieu de la déprime (« On a réussi à stabiliser le service malgré le chaos. Pas mal. ☕ ») ;
  - impuissance concrète.
- **Limites** :
  - la pensée du décideur domine (« la solidarité c'est ce qui nous fait tenir » revient malgré « à éviter ») ;
  - nouveau tic chez 2 avatars (« on ne peut rien faire de notre côté ») ;
  - lassitude et mélancolie peu visibles.
- **Suites** : voir `PSYCHOLOGUE/MEMOIRE.md` § 4bis (nuance choisie au niveau du décideur, rotation sur la population, formules creuses, familles honte et culpabilité).

## Reste à faire
- ✅ Vraies invites rejouées (voir plus haut).
- Éventuellement : 3 à 5 passages par invite pour une mesure de qualité fiable, et `OLLAMA_NUM_PARALLEL` sur le Mac.
- Décision utilisateur sur la répartition des rôles, et avis **CYBERSECU** sur l'entrée d'un ordinateur personnel dans le VPN de l'exercice.
