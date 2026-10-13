# Avis DESIGNER n°104 — 2026-10-13 — app-ia : gérer une grappe de nœuds de calcul (« Parc de calcul »)

> Écrans lus : `C:\CECPC\pleiade\app-ia\src\components\TableauMoteur.tsx` (Tableau de bord : un seul « nœud de calcul », état `noeud {ok, quand, detail}`, phrase « Nœud de calcul injoignable »), `ReglagesMoteur.tsx` (Réglages), `Shell.tsx` (3 onglets). Avis CYBERSECU du 2026-10-12 (soir), partie **(B) GRAPPE**, règles B1 à B9. Aucun code modifié.
> Demande de l'utilisateur : le Moteur IA gère une **grappe** d'ordinateurs de calcul (à terme ~10 PC/Mac sous Gemma 4, ~20 avatars chacun), qu'on active facilement. Si une machine lâche, ses avatars sont **repris automatiquement** par une autre.
> Suite des avis n°98 (famille de l'écran, interrupteur relu, confirmations asymétriques) et n°102 (fenêtres, conséquences nommées avant confirmation). Leurs recommandations restent valables.
> Ce sont des **propositions** : le besoin de l'utilisateur, les règles CYBERSECU et les choix de PLEIADE priment.

---

## Constat

- L'écran ne connaît qu'**un** nœud, et seulement par un échec : le mot « Nœud de calcul injoignable » apparaît quand le cycle a échoué. Il n'y a ni nom, ni adresse, ni temps de réponse. Avec dix machines, la question devient : **lesquelles tournent, qui porte quels avatars, et que s'est-il passé quand l'une a lâché ?**
- La reprise automatique est une bonne nouvelle **si elle se voit**. Une bascule silencieuse laisse l'animation croire que tout va bien alors qu'un nœud est perdu. Elle peut aussi masquer un jeton refusé, que CYBERSECU (B5) veut traiter comme une **alerte de configuration**.
- Gérer des machines n'est **pas un réglage du comportement** des avatars (crise, persuasion, axes). C'est un objet à part, avec ses propres actions et son propre cycle de vie. Le mettre dans Réglages allongerait encore un écran que l'avis n°102 vient de réordonner.

---

## R1. Où placer l'écran : un 4ᵉ onglet « Parc de calcul », un résumé dans le Tableau de bord, un indicateur dans l'en-tête (gain fort, effort faible)

- **Onglet « Parc de calcul »** entre Journal et Réglages : `Tableau de bord · Journal · Parc de calcul · Réglages`. Le tableau des nœuds est une vue de travail (trier, agir ligne par ligne). Il lui faut la pleine largeur.
- **Tableau de bord** : le panneau « Moteur » garde sa phrase, mais l'état « Nœud de calcul injoignable » devient un état du **parc** (R6). Un petit panneau « Parc de calcul » s'ajoute sous « Moteur » : une barre de répartition des avatars par nœud et un lien « Gérer le parc → ». On le regarde d'un coup d'œil, on agit dans l'onglet.
- **Indicateur global** dans l'en-tête de l'app, à droite des onglets, visible sur **tous** les onglets (R2).
- Le mot « nœud » est déjà à l'écran ; on le garde comme unité. Le nom d'onglet est un point à trancher (« Parc de calcul » ou « Nœuds de calcul »).

---

## R2. Indicateur global dans l'en-tête (gain fort, effort faible)

Un bouton-lien compact vers l'onglet. **Forme et mot, jamais la couleur seule** (REF-07) :

```
●  3 nœuds sur 4 en service · 105 avatars répartis          (tout va bien : neutre)
▲  3 nœuds sur 4 en service · 105 avatars répartis          (un nœud perdu, avatars repris : orange)
✕  Aucun nœud maîtrisé · 6 avatars de scénario en pause     (rouge, prioritaire sur tout le reste)
✕  Aucun nœud en service · moteur à l'arrêt                 (rouge)
```

- Le texte décrit **ce qui tourne**, pas ce qui manque. Le symbole porte le niveau d'alerte.
- Sous 1180 px, on garde le symbole et « 3/4 · 105 », et l'`aria-label` porte la phrase complète.
- Il est relu avec le reste de l'état (toutes les 15 s, comme aujourd'hui). Il affiche « relu il y a n s » au survol (doctrine n°98 : un état s'affiche relu, avec sa fraîcheur).

---

## R3. Le tableau des nœuds (gain fort, effort moyen)

```
Parc de calcul                      Zone DELATTRE 26 · Réservé à l'Administration · Relu toutes les 15 s
┌──────────────────────────────────────────────────────────────────────────────────────────────┐
│ ▲ PC-Salle-B ne répond plus depuis 14:02. Ses 19 avatars ont été repris par 3 nœuds.   [Vu]  │
└──────────────────────────────────────────────────────────────────────────────────────────────┘
 3 nœuds sur 4 en service · 105 avatars · 6 de scénario sur nœud maîtrisé       [ + Ajouter un nœud ]
 Répartition  ▕████████ PC Thomas 34 ▏███████ Mac Thomas 33 ▏██████ PC-Salle-A 38 ▏ PC-Salle-B 0 ▕

 État              Nom             Adresse            Classe        Avatars     Temps moy.  Dernier contact   
 ✕ Perdu           PC-Salle-B      10.8.0.21:11435    ○ Tiers       0  (19 ↗)   —           14:02 · il y a 9 min  [⋯]
 ● En service      PC Thomas       10.8.0.3:11435     ◆ Maîtrisé    34 dont 4 ★ 3,1 s       il y a 12 s           [⋯]
 ● En service      Mac Thomas      10.8.0.51:11435    ◆ Maîtrisé    33 dont 2 ★ 4,6 s       il y a 12 s           [⋯]
 ● En service      PC-Salle-A      10.8.0.20:11435    ○ Tiers       38 ▲        5,8 s       il y a 13 s           [⋯]
 ❚❚ En pause       PC-Salle-C      10.8.0.22:11435    ○ Tiers       0           —           hier 18:40            [⋯]
   ▸ détail de la ligne (sondes, jeton, admission, dernières opérations)
```

**Colonnes**
- **État** : symbole et mot. ● En service · ❚❚ En pause (geste humain) · ✕ Perdu (ne répond plus) · ⚠ Jeton refusé (401/403) · ◌ Modèle absent · ○ En essai (ajouté, pas encore sondé). Les lignes à problème sont **triées en tête** par défaut, puis par nom.
- **Nom** : le nom saisi. Le responsable du nœud apparaît en dessous, en petit (B8).
- **Adresse** : en chiffres à chasse fixe. Le port est toujours 11435 ; on l'affiche quand même, car c'est ce que l'animation recopie.
- **Classe** : ◆ Maîtrisé / ○ Tiers. Une forme et un mot. Le rouge est réservé aux pannes, donc **pas de couleur de classe**.
- **Avatars** : le nombre d'avatars affectés et, avec une étoile ★, ceux de scénario ou influenceurs (« dont 4 ★ »). Sur un nœud perdu : « 0 (19 ↗) » = 19 avatars partis ailleurs, qui reviendront. Au-delà du plafond conseillé (20 par nœud, à régler), une marque ▲ « chargé » : un nœud chargé allonge le cycle de toute la population.
- **Temps moyen** : la durée moyenne d'un appel au modèle sur les 12 derniers cycles. Un tiret tant qu'il n'y a pas de mesure, **jamais 0**.
- **Dernier contact** : relatif (« il y a 12 s ») sous 1 h, sinon heure ou jour, avec la date complète au survol.
- **Actions** : un menu « ⋯ » (APG Menu Button, nom accessible « Actions pour PC-Salle-B ») : Mettre en pause / Remettre en service · Tester maintenant · Modifier · Changer le jeton · Voir ses productions dans le Journal · Retirer du parc (séparé, en rouge, en dernier).

**Détail de la ligne** (Disclosure, une ligne ouverte à la fois) :
- les **4 sondes du dernier cycle**, en liste de contrôle : Joignable ✓ · Jeton accepté ✓ · Modèle présent ✓ (`gemma4:26b-a4b-it-qat`, `bge-m3`) · Temps moyen 3,1 s ;
- **jeton** : « défini le 12/10 à 21:14 · empreinte …a3f9 » et rien d'autre, jamais la valeur (B1) ;
- **admission** (B8) : responsable, date de la matrice O8, empreinte TLS si posée (B9) ;
- **les 5 dernières opérations** sur ce nœud (ajouté, mis en pause, jeton changé, perdu, repris), avec qui et quand, et un lien vers le Journal filtré.

**Barre de répartition** : un segment par nœud, **étiqueté en texte** (nom et nombre), dans des neutres distingués par un séparateur. Un nœud perdu ou en pause garde une place vide marquée, pour qu'on voie le trou. Ordre fixe (celui du tableau trié par nom), pour que la barre ne saute pas à chaque relecture.

---

## R4. Ajouter un nœud : une fenêtre, un essai de connexion avant d'enregistrer (gain fort, effort moyen)

```
┌ Ajouter un nœud de calcul ───────────────────────────────────────── ✕ ┐
│ Nom             [ PC-Salle-D                    ]                      │
│ Responsable     [ Sgt Martin                    ]                      │
│ Adresse VPN     10.8.0.[ 23 ]  : 11435                                 │
│                 Adresse de la machine dans le VPN de la zone.          │
│ Jeton           [ ••••••••••••••••••••••••••••• ]  coller              │
│                 Généré sur la machine (kit du nœud). Il ne sera plus   │
│                 jamais affiché après l'enregistrement.                 │
│ Classe          ( ) ◆ Maîtrisé — peut porter les avatars de scénario   │
│                     et les influenceurs                                │
│                 (•) ○ Tiers — ne porte que la population ordinaire     │
│ Matrice O8      [ 13/10/2026 ]  rejouée le        (obligatoire si Tiers)│
│                                                                        │
│ [ Essayer la connexion ]                                               │
│   ✓ Joignable (210 ms)   ✓ Jeton accepté   ✓ Modèle présent            │
│   ✓ Réponse d'essai en 2,8 s                                           │
│   Environ 21 avatars lui seront confiés au prochain cycle. Son premier │
│   cycle sera plus lent (mémoire du modèle à remplir).                  │
│                                                                        │
│ [x] Mettre en service dès l'enregistrement                             │
│                                       [ Annuler ]  [ Enregistrer ]     │
└────────────────────────────────────────────────────────────────────────┘
```

- **L'adresse se saisit par son dernier nombre**, après un préfixe `10.8.0.` affiché et non modifiable, avec le port fixe. L'écran rend impossibles les adresses que CYBERSECU interdit (B2 : IPv4 littérale dans la plage de la zone, port fixe, sans nom d'hôte ni chemin). Le serveur revérifie quand même, et refuse `.0`, `.255` et l'adresse du serveur avec un message sous le champ.
- **Jeton** : champ masqué, sans bouton « afficher » (il est collé, pas tapé). La vérification de forme est immédiate : « 32 octets reconnus » ou « ce n'est pas un jeton du kit ». Le navigateur ne doit pas proposer de le mémoriser (réglage à valider par CYBERSECU).
- **Essayer la connexion** lance les 4 sondes et les affiche **une par une**, dans l'ordre. En cas d'échec, la ligne dit quoi faire : « Injoignable : la machine est-elle allumée et connectée au VPN ? » · « Jeton refusé : recopiez le jeton affiché par le kit sur la machine » · « Modèle absent : lancez le kit du nœud, qui télécharge le modèle ».
- **Enregistrer n'est actif qu'après un essai réussi.** Si l'essai échoue, un lien secondaire « Enregistrer en pause » garde la saisie (sauf le jeton, qu'il faudra recoller) pour réessayer plus tard.
- **Modifier** reprend la même fenêtre. Le champ jeton y est vide et porte la mention « défini le 12/10 · …a3f9 — laisser vide pour le garder ». Changer l'adresse ou la classe **relance l'essai**.
- **Fermeture au clic extérieur et par Échap** (règle de l'utilisateur). Comme dans l'avis n°102, si une saisie est en cours, la fenêtre demande « Abandonner l'ajout ? ». À la fermeture, le jeton est effacé de la mémoire de la page.

---

## R5. Mettre en pause, retirer : dire avant ce que deviennent ses avatars (gain fort, effort faible)

**Mettre en pause** (geste courant : on éteint une machine pour la nuit, on la remet demain) :

```
┌ Mettre en pause PC Thomas ? ─────────────────────────────────────── ✕ ┐
│ Ses 34 avatars seront repris au prochain cycle :                       │
│   · 4 avatars de scénario ★ → Mac Thomas (seul autre nœud maîtrisé)    │
│   · 30 autres → PC-Salle-A 16, Mac Thomas 14                           │
│ Les appels en cours se terminent ; aucun nouveau ne lui est confié.    │
│ Remis en service, il retrouve ses avatars.                             │
│                                         [ Annuler ]  [ Mettre en pause ]│
└────────────────────────────────────────────────────────────────────────┘
```

- Les chiffres sont **calculés par le serveur** (simulation de la réaffectation), pas estimés par la page.
- Si ce nœud est le **dernier nœud maîtrisé**, la fenêtre l'écrit en tête, en orange : « Les 6 avatars de scénario et influenceurs seront mis en pause : aucun autre nœud maîtrisé n'est en service (règle de sécurité). » Le bouton devient « Mettre en pause quand même ».
- S'il s'agit du **dernier nœud en service** : « Le moteur s'arrêtera : plus aucun nœud ne peut faire parler les avatars. »
- Focus sur **Annuler** (geste non urgent ; asymétrie de l'avis n°98). « Remettre en service » ne demande pas de confirmation, seulement un essai de connexion préalable, avec le résultat dans la ligne.

**Retirer du parc** (fin d'exercice, machine rendue, suspicion) :
- Même fenêtre en danger, avec en plus : « Le jeton est effacé de l'instance. Les publications déjà produites gardent le nom de ce nœud. » Puis un rappel non bloquant : « Pensez à **révoquer son profil VPN** côté serveur » (B8, A10).
- **Retirer n'efface pas l'historique** : le nœud disparaît du tableau, mais son nom reste lisible dans le Journal et dans le détail des publications.

---

## R6. Alertes : visibles, nommées, et qui disent ce que le système a déjà fait (gain fort, effort moyen)

Un bandeau en haut de **tous** les onglets, une ligne par alerte, la plus grave en premier. Chaque alerte dit **ce qui s'est passé, ce que le moteur a fait, et ce qu'il reste à faire**.

| Situation | Bandeau | Ce qu'il propose |
|---|---|---|
| Nœud perdu (coupure nette) | ▲ « PC-Salle-B ne répond plus depuis 14:02. Ses 19 avatars ont été repris par 3 nœuds. » | [Vu] ; l'alerte reste dans le tableau tant que le nœud est perdu |
| Nœud revenu | ● « PC-Salle-B répond de nouveau (14:20). Ses 19 avatars lui reviennent au prochain cycle. » | Disparaît seule après 10 min |
| Jeton refusé (401/403) | ⚠ « PC-Salle-A refuse le jeton : nœud mis hors service. Ses 38 avatars sont repris. Le jeton a pu être changé sur la machine, ou l'adresse est celle d'une autre machine. » | [Changer le jeton] · [Vérifier l'adresse] ; **ne disparaît pas** sans action (B5 : alerte de configuration) |
| Modèle absent | ◌ « Mac Thomas n'a plus le modèle gemma4… Ses avatars sont repris. » | [Tester maintenant] |
| Plus aucun nœud maîtrisé | ✕ « Aucun nœud maîtrisé en service : les 6 avatars de scénario et influenceurs sont en pause. Les 99 autres continuent sur les nœuds tiers. » | [Voir le parc] ; rouge, en tête (B7) |
| Plus aucun nœud | ✕ « Aucun nœud de calcul en service : le moteur ne fait plus parler les avatars. » | Remplace l'état « Nœud de calcul injoignable » du Tableau de bord |
| Parc saturé | ▲ « 105 avatars sur 3 nœuds : 35 par nœud en moyenne, au-delà des 20 conseillés. Le cycle s'allonge (4 min 10 au lieu de 2 min). » | [Ajouter un nœud] |

- **Pas de clignotement** : un nœud n'est déclaré perdu qu'après **deux sondes manquées** de suite, et repris qu'après deux réussies (remontée PLEIADE). Sinon une machine instable fait faire des allers-retours aux avatars et casse le cache que le hachage stable doit préserver.
- Les alertes sont annoncées (`role="alert"` pour les rouges, `role="status"` pour les autres), sans répétition à chaque relecture de 15 s.
- Chaque transition s'inscrit au **Journal**, sous un type « Parc de calcul » dans le menu des types (avis n°98), en phrases : « 14:02 — PC-Salle-B perdu · 19 avatars déplacés : 8 → PC Thomas, 6 → Mac Thomas, 5 → PC-Salle-A ». Les réaffectations sont agrégées (B4), il n'y a pas une ligne par avatar.

---

## R7. État de départ : un seul nœud, celui de l'environnement (gain moyen, effort faible)

```
 1 nœud en service · 105 avatars                                   [ + Ajouter un nœud ]
 ● En service   Nœud de l'environnement   10.8.0.3:11435   ◆ Maîtrisé   105 ▲   3,1 s   il y a 12 s   [⋯]
                Défini par la configuration de l'instance (ia.yml)

 ┌──────────────────────────────────────────────────────────────────────────┐
 │ Un seul nœud fait parler les 105 avatars. Ajoutez des machines pour      │
 │ raccourcir le cycle et pour qu'une panne ne l'arrête pas : leurs avatars │
 │ seront repris automatiquement par les autres.                            │
 │ Il faut sur chaque machine : le VPN de la zone, le kit du nœud, son      │
 │ jeton.                                                                   │
 └──────────────────────────────────────────────────────────────────────────┘
```

- Le nœud de l'environnement est une **ligne comme les autres**, marquée « Défini par la configuration de l'instance ». Il peut être mis en pause, mais pas modifié ni retiré depuis l'écran : son adresse et son jeton viennent de l'orchestrateur.
- L'encadré d'explication disparaît dès le deuxième nœud.
- L'indicateur d'en-tête dit simplement « 1 nœud · 105 avatars », sans « sur ».

---

## R8. Traçabilité dans le Journal (gain moyen, effort faible)

- Le volet de détail d'une publication (avis n°98) ajoute une ligne « Produit par : PC-Salle-B (10.8.0.21) » (B4, visible de l'Administration seulement).
- Le Journal reçoit un **filtre « Nœud »**, ouvert depuis le menu ⋯ d'une ligne (« Voir ses productions »). C'est le premier pas pour retirer d'un coup les productions d'un nœud compromis (B4). Le geste de retrait en masse lui-même mérite un avis à part, le jour où il est conçu.

---

## R9. Accessibilité et vocabulaire, en bref

- Le tableau est un vrai `<table>` avec `<caption>` et des en-têtes `scope="col"`. Le tri est annoncé (`aria-sort`). Le menu ⋯ est atteignable au clavier.
- Les fenêtres suivent APG Dialog : titre relié, focus initial maîtrisé, focus piégé, Échap et clic extérieur, retour du focus sur le bouton d'origine.
- États, classes et alertes : **symbole et mot**, jamais la couleur seule (REF-07). Cibles de 24 px au moins.
- **Vocabulaire** : « animation » pour les personnes (« l'équipe d'animation »), « Administration » en toutes lettres pour le rôle, **jamais « Admin »**. On écrit « nœud », pas « node » ni « worker ». On écrit « mis en pause » pour un geste humain et « perdu » pour une panne : deux mots différents, car ce sont deux causes différentes.

---

## Remontées PLEIADE et CYBERSECU

- **R-API-1 (PLEIADE)** : `GET /api/bff/noeuds` renvoie, par nœud, l'état, les 4 sondes, les avatars affectés (dont scénario), le temps moyen, le dernier contact, `jeton: { pose, empreinte4 }` (jamais la valeur), la provenance (`environnement` ou `ecran`). Il renvoie aussi l'agrégat de l'en-tête et les alertes ouvertes.
- **R-API-2 (PLEIADE)** : `POST /api/bff/noeuds/essai` lance les sondes **sans enregistrer**. Une route de **simulation de réaffectation** (pause ou retrait) donne les chiffres des fenêtres de R5.
- **R-API-3 (PLEIADE)** : hystérésis à deux sondes pour « perdu » et « repris » ; retour des avatars sur leur nœud d'origine (hachage stable) ; précondition à l'écriture (409 si le nœud a changé entre-temps, doctrine n°98).
- **R-API-4 (PLEIADE)** : les erreurs de validation au format `{ error, champ }` (adresse, jeton, classe), placées sous le bon champ.
- **CYBERSECU** : (a) l'**essai** envoie le jeton à l'adresse saisie avant l'enregistrement. Il doit donc passer par **la même liste blanche (B2)**, la même garde de rôle (B3), et être limité en fréquence ; (b) réglage du champ jeton face aux gestionnaires de mots de passe du navigateur ; (c) **401/403** : B5 demande « pas de bascule silencieuse ». Cet avis propose que les avatars soient **repris quand même, mais avec une alerte qui ne disparaît pas sans action**. À confirmer ; (d) champ « matrice O8 » et « responsable » obligatoires pour un nœud tiers (B8) ; empreinte TLS (B9) affichée dans le détail quand elle existe.

---

## Points à trancher par l'utilisateur

1. **Nom de l'onglet** : « Parc de calcul » (proposé) ou « Nœuds de calcul » ?
2. **Plafond conseillé** par nœud (20 avatars proposé) : réglable dans l'écran, ou fixe ?
3. **Nouveau nœud** : mis en service dès l'enregistrement si l'essai réussit (proposé, case cochée par défaut), ou toujours en pause d'abord ?
4. **Nœud de l'environnement** : modifiable depuis l'écran, ou réservé à la configuration (proposé) ?
5. **Jeton refusé** : avatars repris avec une alerte persistante (proposé), ou laissés en pause jusqu'à correction ? À voir avec CYBERSECU.

Mise en œuvre : PLEIADE, en local d'abord (règle « tester en local avant de pousser »), après la validation par CYBERSECU de l'essai de connexion et du champ jeton.
