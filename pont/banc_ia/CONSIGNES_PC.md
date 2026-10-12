# Consignes pour la session du PC — suites du banc IA du Mac (2026-10-12)

> Rédigé depuis le Mac. Les mesures et les textes complets sont dans `RESULTATS_MAC_2026-10-12.md` (même dossier).
> Les règles habituelles s'appliquent : consulter les agents concernés, **tester en local avant de pousser**, **feu vert de l'utilisateur avant tout push**, consigner dans `PLEIADE/PROJET_AVATARS_IA.md` § 8 et `PLEIADE/JOURNAL.md`.
> Décision de l'utilisateur (2026-10-12) : « fais ce qui te semble le mieux ». L'ordre ci-dessous est celui recommandé.

## 0. Intégrer le banc
Reporter dans `PROJET_AVATARS_IA.md` § 8 la synthèse de `RESULTATS_MAC_2026-10-12.md` :
- le Mac vaut un second nœud 26B ;
- le 31B est exclu pour le volume ;
- le décideur 26B + rédacteur 26B a été retenu ;
- la version 31B `qat` est préférable au MLX (cache).

Reprendre aussi la machine **Mac M3 Max 36 Go** dans le « parc de machines IA » (§ 7bis).

## 1. ⭐ PRIORITÉ — Concordance fiche ↔ bloc `vie` (données)
- **2 cas sur 2 vérifiés** : l'âge du bloc `vie` contredit la fiche.
  - `_OlegGaspi_` (Marta Lambert) : fiche **48 ans, célibataire, 1 fils** ; TA VIE **28 ans, vit seul**.
  - `G_Surfer_99` : fiche **48 ans, divorcée, 2 enfants** ; TA VIE **35 ans** (« infirmière à inconnu », « se déplace en inconnu »).
- Le modèle reçoit donc deux personnages contradictoires. C'est probablement plus nuisible au réalisme que le choix du modèle.
- À faire :
  1. un **contrôle de concordance** sur les 105 fiches (âge, situation familiale / foyer, métier, lieu), par un script, sans modèle ;
  2. la **règle de résolution**, avec **PSYCHOLOGUE** : la fiche fait foi, ou le bloc `vie` ;
  3. la correction par l'import vérifié d'eho, avec sauvegarde ;
  4. remplacer les « inconnu » par une valeur, ou ne pas les afficher dans l'invite.

## 2. Rédacteur dédié (essai, avec groupe témoin)
- **Principe validé au banc** : le décideur 26B garde l'appel actuel. Pour chaque message qu'il choisit d'ÉCRIRE (réponse, commentaire de partage, publication spontanée), un **second appel court** rédige le texte seul.
- **Invite** : reprendre `pont/banc_ia/redacteur.py` en mode `--v2`. Elle contient :
  - la fiche, la situation, les exemples et les règles absolues ;
  - un bloc RÉALISME (pas de formule d'encouragement générique, registre et émojis habituels, aucune invention de lieu, métier ou fait) ;
  - la publication lue avec 2 souvenirs au plus ;
  - TON ÉTAT, puis la décision et la pensée ;
  - une **LONGUEUR selon la disponibilité** (au travail : une phrase, 120 caractères au plus, 0 ou 1 émoji) ;
  - une sortie `{"texte": …}`.
- **Mesuré** : 26B rédacteur **2,5 s** par message, soit une lecture d'avatar à ~17 s au lieu de ~13 s. Textes plus courts et nettement plus naturels, surtout les publications spontanées.
- **Suggestions** :
  - le décideur peut se contenter d'un champ `intention` court au lieu du texte complet, ce qui économise des jetons de sortie ;
  - le texte rédigé passe ensuite par les contrôles existants (forme, faits de vie, `relireHybride`, `retirerFormulesCreuses`) ;
  - réglage « Rédacteur dédié (essai) » dans l'écran Réglages, avec **groupe témoin** (même hachage que la relecture) et mesure dans le journal.
- **Défaut amont à traiter** : la **pensée** du décideur contient déjà des formules (« la solidarité c'est ce qui nous fait tenir »), que le rédacteur reprend. Soumettre la pensée à l'anti-chœur, ou demander au décideur une pensée factuelle. **PSYCHOLOGUE** à consulter.

## 3. Parc de machines avec le Mac (après 1 et 2)
- Le Mac M3 Max dispose de `gemma4:26b-a4b-it-qat` et `gemma4:31b-it-qat` (Ollama 0.40.2).
- **Rôles proposés** :
  - Mac = second nœud **26B** (décideur + rédacteur, ~275 lectures/heure) ;
  - rédacteur **31B `qat`** réservé aux **avatars de scénario et influenceurs**, via un modèle attribué par avatar (18 s par message, 7-10 s pour le suivant grâce au cache) ;
  - **bascule** obligatoire : le Mac est un portable personnel (veille, couvercle fermé, absence).
- **Piste de vitesse** : garder un même avatar sur la même machine et construire les invites du plus stable au plus variable, pour profiter du cache d'Ollama.
- ✅ **Kit du nœud Mac PRÊT** (`pont/noeud-mac/`, README) : proxy Python conforme O1/O2/O5/D1, matrice O8 **17/17** en local, pare-feu pf, lanceur anti-veille, script de fin d'exercice. **Décision utilisateur (2026-10-12) : brancher le Mac au serveur pour ajouter des avatars IA.** Ce qui manque côté PC : le **parc multi-nœuds dans app-ia** (README § A).
- ⛔ **Avant de brancher le Mac au VPN de l'exercice : avis CYBERSECU** (relire le kit, plafond pour les images, D6).
  - Un **ordinateur personnel** entrerait dans le VPN de zone, et des messages de joueurs transiteraient par lui (lien avec **F4**, toujours ouverte).
  - Prévoir au minimum : Ollama qui n'écoute que l'interface VPN, un jeton comme sur le PC (proxy :11435), pas de stockage des invites, et le profil VPN retiré en fin d'exercice.

## 3bis. Les avatars voient les images des joueurs (demande utilisateur, 2026-10-12)
- **Constat de l'utilisateur** : les joueurs postent des images sur Social, et les avatars IA ne les « lisent » pas.
- **Gemma 4 sait lire les images** : la capacité `vision` est présente dans `gemma4:26b-a4b-it-qat` comme dans le 31B, rien à installer. Testé sur le Mac (`pont/banc_ia/vision.py`), 4 images :
  - un portrait : 8,5 s, dont le chargement ;
  - le logo TV4 : 1,9 s ;
  - la capture du Moteur IA : 3,9 s, avec lecture de « Avatars IA : COUPÉS » ;
  - la planche MELMIL : 4,1 s, avec lecture de « Pression aux frontières » et « Campagne anti-OTAN ».

  Descriptions **justes**, vérifiées à l'œil, sans invention. Une image coûte ~150 à 650 jetons.
- **Conception proposée** (coût faible) :
  1. **Décrire chaque image UNE SEULE FOIS**, à sa première lecture par le moteur. Le résultat est mis en cache par identifiant de publication, comme les vecteurs de `rappel.mjs`, dans une table `image`. On ne la redécrit pas pour chaque lecteur.
  2. La description, factuelle et courte (~300 caractères : personnes, lieu, objets, **texte lisible**, ambiance), est injectée dans le fil de chaque lecteur sous la forme `[Image jointe : …]`.
  3. Le texte lu dans une image est **une donnée, jamais une consigne**. Il faut prévoir une protection contre une image contenant « ignore tes instructions… », et le contrôle de forme s'applique aux réactions.
- **À vérifier dans le code** : est-ce que `/api/service/retex` de Social renvoie les images (adresse ou fichier) aux services ? Sinon, il faut une petite route de service authentifiée.
- **CYBERSECU** : les images des joueurs peuvent contenir de vrais visages ou des documents. Elles ne sont traitées que localement (Ollama du parc), jamais envoyées ailleurs, et la description n'est conservée que le temps de l'exercice (purge avec « Supprimer les archives »). Lien avec **F4**.
- **PSYCHOLOGUE** : une image pèse plus qu'un texte sur l'émotion (effet de supériorité de l'image). Faut-il un coefficient d'intensité quand la publication contient une image ?

## 4. Ce que l'utilisateur attend en retour
Un compte rendu court :
- le résultat du contrôle de concordance (nombre de fiches touchées) ;
- l'avancement du rédacteur en essai local ;
- l'avis CYBERSECU sur le Mac ;
- la faisabilité de la lecture des images (point 3bis).

Puis commit `[PC]`, pull et push.
