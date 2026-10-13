# Avis DESIGNER n°105 — 2026-10-13 — app-cockpit : refaire la vue principale (catégories de suivi + contrôle général de l'espace informationnel)

> **Écrans lus** (lecture seule, `app-cockpit` à `dea51d1`) : `CockpitApp.tsx`, `DashboardGrid.tsx`, `sections\Sections.tsx`, `Section.tsx`, `SourceCard.tsx`, `SidePanel.tsx`, `Header.tsx`, `Footer.tsx`, `MenuFixe.tsx`, `BarreFiltre.tsx`, `Demarrage.tsx`, `dialogs\AddSourceDialog.tsx`, `store\cockpit-store.tsx`, `store\workspaces.ts`, `types.ts`, `lib\instances.ts`, routes `api\bff\*`. Aucun code modifié.
> **Constat de l'utilisateur** (capture à 50 %, Cockpit de DELATTRE 26) : la vue principale est « incompréhensible ». Barre de stats (8 880 publications, 4 069 utilisateurs, 8 136 commentaires), bandeaux de catégories repliés (27 BIM 2, HIGHCON 19, FORAD 1889, GREYCELL 2012, IA 103), un énorme bloc « NOUVEAUX MESSAGES 149 » en mosaïque de cartes de comptes à compteurs rouges, « Flux en direct » et « Tendances » à droite ; pied : 4 025 sources, 149 publications collectées, 10 s, « À partir du ».
> **Besoin** : depuis cette vue, (1) **créer et gérer des catégories de suivi** (camps, cellules, groupes eho, hashtags, comptes) ; (2) une **interface de contrôle général** de l'espace informationnel de l'exercice : fil du réseau social, messages privés (Chat), presse (`app-press`), messagerie (`app-messagerie`)… Public : animateurs (rôle analyste), militaires, pas développeurs. Il faut comprendre **en 5 secondes** : *que se passe-t-il, où, qui pèse, qu'est-ce qui a changé depuis que j'ai regardé.*
> Suite des avis n°73 (audit du Cockpit), n°72 (groupes eho), n°92 (tendances, « publications » ≠ « messages »), n°75/96/103 (Reporting, `GrapheTemps`). Leurs acquis sont gardés (§ « Ce qu'on garde »).
> Ce sont des **propositions** : le besoin de l'utilisateur, les choix de PLEIADE / ARCHITECTE et les règles CYBERSECU priment.

---

## 1. Pourquoi la page est incompréhensible (diagnostic sur le code)

| # | Constat | Où dans le code | Règle / heuristique | Gravité |
|---|---|---|---|---|
| D1 | **L'unité affichée est la source, pas l'information.** Suivre un groupe d'eho copie **chaque membre** en source (`addGroup`, `Demarrage.suivre`) : FORAD = 1 889 cartes, GREYCELL = 2 012. D'où 4 025 sources et la mosaïque. Personne ne lit 4 000 cartes. | `AddSourceDialog.addGroup`, `Demarrage` | Tesler (règle 19), Hick (16) | **4** |
| D2 | **Les nombres ne disent pas ce qu'ils comptent.** « FORAD 1889 » = nombre de **sources suivies** (`count={sources.length}`), pas d'activité. « 149 » = publications non lues. « 8 880 » = tout le réseau depuis son début. Trois sortes de nombres côte à côte, sans unité. | `CategorySection`, `UnreadSection`, `StatsSection` | Nielsen 2, REF-07 (l'étiquette dernier recours… mais ici il en manque) | **4** |
| D3 | **« Nouveaux messages » montre QUI a publié, pas QUOI.** Le bloc liste les cartes des sources à non-lus ; pour lire les 149, il faut cliquer carte après carte, chaque clic ouvrant un panneau modal flouté. | `UnreadSection`, `SourceCard.open`, `SidePanel` | Nielsen 7, règle 38 (flux) | **3** |
| D4 | **Rien ne répond à « depuis que j'ai regardé ».** Le non-lu est par source et s'efface au clic ; pas d'heure de dernier passage, pas de variation, pas de « calme / agité ». | `acknowledge`, `unread` | Nielsen 1, règle 25 | **3** |
| D5 | **Rien ne répond à « qui pèse ».** Aucun classement d'auteurs, aucune mesure d'audience ou d'interactions ; les tendances donnent des volumes de hashtags seulement. | — | Besoin utilisateur | **3** |
| D6 | **Un seul canal.** Le Cockpit ne lit que les réseaux sociaux (`TYPES_RESEAU` dans `lib\instances.ts`) : ni Chat, ni presse, ni messagerie. | `lib\instances.ts` | Besoin utilisateur | **3** (données) |
| D7 | **Une catégorie n'est qu'un dossier** (nom + couleur) : elle ne sait pas « tous les membres du groupe FORAD, y compris ceux ajoutés demain », ni « les hashtags #X et #Y ». Un nouvel avatar d'eho n'est pas suivi. | `Category`, `Source.category` | Tesler (19) | **3** |
| D8 | **Disposition libre** (colonnes glissées, séparateurs, zoom 50-200 %) : chaque poste a sa page, personne ne partage un même repère ; la capture à 50 % en est le symptôme. | `DashboardGrid`, `Footer` | Règle 28 (mémorisation : navigation stable) | **2** |
| D9 | **Mots et couleurs** : « messages » désigne le Chat (doctrine n°92) et ne convient pas aux publications ; « Acquitter tout » est le seul bouton rouge (couleur d'alerte usée pour une action banale) ; le compteur rouge sur chaque carte rend tout alarmant. | `UnreadSection`, `pl-tag-halt` | Règle 20 (Von Restorff), règle 36 | **2** |
| D10 | **Le panneau de lecture masque le tableau** (fond noir flouté, modal) : on ne peut pas lire en gardant la situation sous les yeux. | `SidePanel` | Règle 38 (liste-détail, volet d'appui) | **2** |

**Conclusion** : le Cockpit est un **carnet de sources** qu'on a fait grossir jusqu'à 4 000 entrées. Le besoin est une **vue de situation**. Il faut changer d'unité : la **catégorie de suivi** (une règle) et le **contenu** (une publication, un message, un article), et compter **des variations depuis le dernier passage**, pas des stocks.

---

## 2. Trois décisions communes aux trois concepts

Quel que soit le concept retenu :

**C1 — La catégorie de suivi devient une RÈGLE, pas une liste de cartes.**
```
Catégorie de suivi « Camp FORAD »                     ● couleur  + libellé « FORAD » (jamais la couleur seule)
  Inclure    [Groupe eho : FORAD ×]  [Cellule : FORAD (comptes fd..) ×]  [#OpFORAD ×]  [+ Ajouter une règle ▾]
                                      Groupe eho · Camp · Cellule · Compte · Hashtag · Mot-clé
  Exclure    [@fd_test ×]                                               [+ Exclure ▾]
  Canaux     ☑ Réseau social  ☑ Chat  ☐ Presse  ☑ Messagerie
  Alerte     ○ Aucune  ● Flambée (× 3 par rapport à l'heure passée)  ○ Dès le 1er contenu (critique)
  Partage    ● Ma cellule (GREYCELL)  ○ Moi seulement
  ─────────────────────────────────────────────────────────────────────────
  Aperçu     Couvre 1 889 avatars et 1 hashtag · 214 contenus sur la dernière heure       [Annuler] [Créer la catégorie]
```
- Un groupe d'eho est suivi **par son identifiant** : les membres ajoutés plus tard sont couverts sans rien faire. Les 4 025 « sources » disparaissent de l'écran ; elles restent consultables dans la fiche de la catégorie (« 1 889 avatars couverts › »).
- La règle est résolue **côté serveur** (BFF ou Admin, qui garde déjà les espaces, P8). C'est un préalable ARCHITECTE/PLEIADE : sans lui, le navigateur continue d'interroger 4 000 sources toutes les 10 s.
- **Un contenu peut appartenir à plusieurs catégories** (un avatar FORAD qui écrit #OpFORAD) : il est compté une fois par catégorie, une fois dans le total.
- Modèles prêts à l'emploi (règle 39) : « Un camp », « Une cellule », « Un groupe d'eho », « Un hashtag à surveiller », « Une liste de comptes ». Le premier écran (P1 de l'avis n°73) les propose.

**C2 — « Depuis votre dernier passage » est l'état de référence.**
L'app note l'heure du dernier passage **par animateur** (pas par carte). Tout chiffre est donné **avec sa variation** : `214 contenus · +38 depuis 14:02`. Un trait « Nouveau depuis 14:02 » sépare le neuf de l'ancien dans toute liste. « J'ai fait le point » remet le compteur à zéro (remplace « Acquitter tout », en bouton neutre).

**C3 — Un vocabulaire par canal, un mot générique.**
« **Contenus** » pour tout ; « publications » (réseau social), « messages » (Chat et messagerie), « articles » (presse). Le bloc s'appelle « Nouveaux contenus », jamais « Nouveaux messages ». Le rôle se nomme « animation » (« Réservé à l'animation »), jamais « Admin ».

**Règles d'interface communes** : fenêtres et menus fermés au **clic extérieur + Échap**, focus rendu au déclencheur ; **couleur de camp toujours doublée d'un libellé** (`● FORAD`, `● Camp rouge`) ; **une seule couleur d'alerte**, rare, avec une forme (▲) et un mot ; états relus avec leur fraîcheur (« En direct · relu il y a 4 s ») ; un canal injoignable le dit (« ✕ Presse injoignable depuis 14:05 ») au lieu de montrer zéro.

**Préalable données (ARCHITECTE / PLEIADE, CYBERSECU)** : aujourd'hui seuls les réseaux sociaux sont lus. Il faut des connecteurs BFF pour le **Chat** du social, `app-press` (articles publiés, éventuellement lectures), `app-messagerie` (courriels), et une mesure de **poids** (interactions : réactions, partages, réponses ; audience : abonnés). ⚠ **Messages privés** (Chat, messagerie) : qui, dans l'animation, peut lire le contenu des échanges des joueurs, et faut-il n'en montrer que les métadonnées (volume, interlocuteurs) par défaut ? → **CYBERSECU tranche** ; les maquettes montrent un contenu masqué derrière « Afficher le message » pour poser la question.

---

## 3. Concept A — « Salle de veille par canaux »

**Principe** : une colonne par canal (Réseau social · Chat · Presse · Messagerie), comme TweetDeck / X Pro, et les catégories de suivi en filtres qui s'appliquent à toutes les colonnes à la fois.

```
┌ PLÉIADE · DELATTRE 26 ── Apps de la zone ▾ ──────────────────────────────────────────── Guide · gc05 ┐
│ COCKPIT   Veille · Reporting · Catégories de suivi          ● En direct · relu il y a 4 s   [+ Catégorie de suivi] │
├────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ Catégories : [Toutes] [● FORAD] [● GREYCELL] [● Camp rouge] [● #OpFORAD ▲ flambée] [● IA] [+ ]   Depuis 14:02 (il y a 12 min) │
├──────────────────────────┬──────────────────────────┬──────────────────────────┬───────────────────────────────────┤
│ RÉSEAU SOCIAL  +96  ▲    │ CHAT  +21                │ PRESSE  +4               │ MESSAGERIE  +7                    │
│ 412 publications · 1 h   │ 58 messages · 1 h        │ 9 articles · 1 h         │ 23 courriels · 1 h                │
│ ▁▂▂▃▅▇ sparkline         │ ▁▁▂▂▃▂                   │ ▁▁▁▂▁▂                   │ ▂▁▂▂▃▂                            │
│ ─ 12 nouveaux ↑ (pause) ─│                          │                          │                                   │
│ ● FORAD  @fd_milice 14:13│ ● FORAD → ● GREYCELL     │ TV4 · 14:10              │ ● HIGHCON  pc.brigade → cellule   │
│ « Les convois… » ♥42 ↻17 │ @vera_k ↔ @dan_o (6 msg) │ « Le gouverneur… »  ★ 3  │ « OBJ : point de situation »      │
│ ▸ 23 publications sur    │ [Afficher les messages]  │ BC1 · 14:02              │ ...                               │
│   #OpFORAD en 10 min     │ ...                      │ ...                      │                                   │
│ ── Nouveau depuis 14:02 ─│ ── Nouveau depuis 14:02 ─│ ── Nouveau depuis 14:02 ─│ ── Nouveau depuis 14:02 ──        │
│ ...                      │ ...                      │ ...                      │ ...                               │
├──────────────────────────┴──────────────────────────┴──────────────────────────┴───────────────────────────────────┤
│ Tendances : #OpFORAD 214 ▲×4 · #Delattre 96 · #Pont 41 ↩12        Qui pèse (1 h) : @fd_milice · @tv4_info · @gc_vox │
└────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
       Clic sur un contenu → volet de lecture non modal à droite (fil, auteur, camp, origine), Échap le ferme.
```

- **Hiérarchie** : en haut, les filtres de catégories et l'heure de référence ; au centre, quatre flux de même poids ; en bas, une bande « Tendances · Qui pèse ». Le volet de lecture glisse par-dessus la dernière colonne.
- **Créer / régler une catégorie** : « + » en bout de barre de filtres → fenêtre C1 ; « ⋯ » sur une puce → Modifier, Dupliquer, Supprimer ; l'ordre des puces se règle par glisser.
- **Passer d'un canal à l'autre** : ils sont tous visibles ; on masque une colonne (« Colonnes ▾ ») si l'écran est étroit ; sous 1280 px, onglets de canal.
- **Volume** : chaque colonne se **met en pause** dès qu'on la survole ou qu'on y fait défiler (« 12 nouveaux ↑ » au lieu de pousser le texte) ; les **rafales sont regroupées** (« 23 publications sur #OpFORAD en 10 min » repliable) ; listes virtualisées ; l'en-tête de colonne porte la variation, pas un stock.
- **États** : *rien de neuf* → en-tête « Calme · dernier contenu 13:58 », pas d'encart vide ; *alerte* → la puce de la catégorie et le contenu portent ▲ + « Alerte », liseré fixe ; *flambée* → puce « ▲ flambée × 4 », la colonne concernée affiche un bandeau « #OpFORAD : 23 publications en 10 min › » ; *canal injoignable* → en-tête « ✕ Presse injoignable depuis 14:05 ».
- **Forces** : modèle connu des analystes (Jakob) ; l'ensemble des canaux d'un coup d'œil ; le plus simple à construire sur l'existant (le « Flux en direct » devient la colonne Réseau social).
- **Faiblesses** : **quatre flux qui défilent ne disent ni « où » ni « qui pèse »** : on revient à lire, pas à comprendre ; le réseau social écrase les autres canaux (412 contre 9) ; la largeur coûte (4 colonnes lisibles exigent ≥ 1 440 px) ; le croisement « catégorie × canal » reste à faire de tête.

**À maquetter (A)** : barre de plateforme ; en-tête d'app (onglets Veille · Reporting · Catégories de suivi, état « En direct », action principale) ; barre de puces de catégories (actif, flambée ▲, « + », menu « ⋯ ») ; repère « Depuis 14:02 » + « J'ai fait le point » ; 4 colonnes (en-tête avec total, variation, mini-courbe ; carte de contenu par canal : publication, conversation de Chat masquée, article, courriel ; trait « Nouveau depuis » ; regroupement de rafale ; bouton « 12 nouveaux ↑ ») ; bande Tendances · Qui pèse ; volet de lecture non modal ; fenêtre « Nouvelle catégorie de suivi » ; états : calme, flambée, canal injoignable.

---

## 4. Concept B — « Tableau de situation par catégories »

**Principe** : une grille **catégories × canaux** où chaque case donne le volume depuis le dernier passage, sa tendance et ce qui domine ; on lit la situation d'abord, on n'ouvre les contenus qu'au clic.

```
┌ PLÉIADE · DELATTRE 26 ── Apps de la zone ▾ ──────────────────────────────────────────── Guide · gc05 ┐
│ COCKPIT   Situation · À traiter (38) · Reporting · Catégories de suivi    ● En direct · relu il y a 4 s  [+ Catégorie de suivi] │
├────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ CE QUI A CHANGÉ depuis 14:02 (il y a 12 min)                                               [J'ai fait le point]    │
│ ▲ #OpFORAD flambe : 23 publications en 10 min (× 4)  ›   ▲ Alerte : @gc_vox cité par TV4  ›   +38 contenus · 3 nouveaux comptes actifs │
├───────────────────────────────────────────────────────────────────────────────┬────────────────────────────────────┤
│ Catégorie de suivi      Réseau social    Chat         Presse      Messagerie  │ TENDANCES (1 h)                    │
│ ● FORAD     1 889 av.   +41 ▲ ▂▃▅▇       +12  ▂▂▃     +1   ▁▁▂    +3   ▁▂▁    │ #OpFORAD    214  ▲ × 4  ↩ 37       │
│   qui pèse : @fd_milice (♥ 310) · @fd_echo                                     │ #Delattre    96  =                 │
│ ● GREYCELL  2 012 av.   +18 = ▃▃▃▃     +6   ▁▂▂     0    ▁▁▁    +2   ▂▂▂    │ #Pont        41  ▼  ↩ 12           │
│ ● Camp rouge  (eho)     +9  ▼ ▅▃▂▁     —            +2   ▁▂▃    —           │ [+ Suivre ce hashtag] au survol    │
│ ● #OpFORAD  hashtag     +23 ▲▲ flambée —            +1          —           │────────────────────────────────────│
│ ● HIGHCON   19 av.      +0  calme      +3           —           +2          │ QUI PÈSE (1 h, toutes catégories)  │
│ ● BIM 2     27 av.      +1             0            —           0           │ 1 @fd_milice   ● FORAD   ♥310 ↻88  │
│ ● IA        103 av.     +14 ▲          +0           —           —           │ 2 @tv4_info    Presse    ★ 5 art.  │
│ Hors catégories         +32            +9           +3          +4          │ 3 @gc_vox      ● GREYCELL ♥120     │
│ Total zone              +138           +30          +7          +11         │────────────────────────────────────│
│                                                                               │ CANAUX   ● Social ● Chat           │
│ (clic sur une case = la liste des contenus dans le volet ; clic sur une        │          ● Presse ✕ Messagerie     │
│  catégorie = sa fiche : règles, avatars couverts, courbe)                       │          injoignable depuis 14:05  │
├───────────────────────────────────────────────────────────────────────────────┴────────────────────────────────────┤
│ Volet (non modal, à droite, 480 px) : « FORAD × Réseau social · 41 nouvelles publications »  liste triée, Échap ferme │
└────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

- **Hiérarchie** : en haut, **« Ce qui a changé »** (3 faits au plus, phrases écrites : flambée, alerte, bilan) ; au centre, la **grille de situation** (une ligne par catégorie, une colonne par canal) ; à droite, Tendances, Qui pèse, État des canaux ; le contenu ne vient qu'au clic, dans un **volet non modal**.
- **Créer / régler une catégorie** : action principale « + Catégorie de suivi » (fenêtre C1) ; clic sur le nom d'une ligne → **fiche de la catégorie** (règles, avatars couverts, courbe `GrapheTemps` de la journée, bouton Modifier) ; « ⋯ » en bout de ligne → Modifier, Épingler en tête, Masquer de la situation, Supprimer ; ordre par glisser **dans la liste des catégories** (onglet Catégories de suivi), pas dans la page.
- **Passer d'un canal à l'autre** : les canaux sont des **colonnes** ; cliquer l'en-tête « Chat » ouvre la liste de tous les messages du Chat, toutes catégories ; une case ouvre le croisement.
- **Volume** : **on agrège** : 4 000 avatars et 150 contenus / 10 min deviennent ~8 lignes × 4 cases. Les nombres sont des variations depuis le dernier passage ; la mini-courbe montre la dernière heure (domaine commun par colonne, pour comparer) ; « Qui pèse » limite à 2 noms par ligne et un top 5 global.
- **États** : *rien de neuf* → la case affiche « calme » en gris, la ligne ne disparaît pas (mémoire de position, règle 28), et le bandeau dit « Rien de notable depuis 14:02 · 4 contenus » ; *alerte* → ▲ + « Alerte » dans le bandeau, liseré fixe sur la ligne, seule couleur d'alerte de la page ; *flambée* → case « ▲▲ flambée » + phrase dans le bandeau, et le hashtag remonte en tête des Tendances avec « × 4 » ; *canal injoignable* → colonne grisée, en-tête « ✕ injoignable depuis 14:05 », jamais « 0 ».
- **Forces** : **répond aux 4 questions en 5 secondes** (où : la ligne ; quoi : la case ; qui pèse : la ligne et le top ; qu'est-ce qui a changé : le bandeau et les « + ») ; tient le volume sans effort ; stable d'un poste à l'autre ; met en évidence un canal calme (la presse ne se noie plus sous le réseau social) ; reprend des briques déjà validées (`GrapheTemps`, tendances avec ↩).
- **Faiblesses** : un clic de plus pour lire ; tout repose sur la **qualité des catégories** (une zone mal découpée donne un tableau vide ou une ligne « Hors catégories » énorme) ; demande des **agrégats côté serveur** (comptes par catégorie et par canal, poids) ; moins « vivant » qu'un flux : il faut un volet ou un onglet de lecture pour le travail fin.

**À maquetter (B)** : barre de plateforme ; en-tête (onglets Situation · À traiter (n) · Reporting · Catégories de suivi, état « En direct », action principale) ; bandeau « Ce qui a changé » (3 phrases, « J'ai fait le point ») ; grille de situation (ligne catégorie : pastille + libellé + nombre d'avatars couverts ; case : variation, flèche + mot, mini-courbe, « calme » ; ligne « Hors catégories » ; ligne « Total zone » ; ligne en alerte) ; colonne droite : Tendances (× 4, ↩, « Suivre ce hashtag »), Qui pèse (rang, camp en libellé, mesure), État des canaux ; volet non modal (liste d'un croisement) ; fiche de catégorie (règles, avatars couverts, courbe) ; fenêtre « Nouvelle catégorie de suivi » ; premier écran sans catégorie (modèles + groupes eho en un clic) ; états : calme, flambée, canal injoignable.

---

## 5. Concept C — « Boîte de réception triée + panneau de lecture »

**Principe** : tous les contenus de tous les canaux arrivent dans une **liste unique triée par importance**, à traiter comme une boîte de réception (Outlook, Gmail), avec les catégories et les canaux en rail à gauche et un panneau de lecture riche à droite.

```
┌ PLÉIADE · DELATTRE 26 ── Apps de la zone ▾ ──────────────────────────────────────────── Guide · gc05 ┐
│ COCKPIT   À traiter · Reporting · Catégories de suivi              ● En direct · relu il y a 4 s  [+ Catégorie de suivi] │
├──────────────────────┬──────────────────────────────────────────────┬──────────────────────────────────────────────┤
│ VUES                 │ À traiter · FORAD · tous canaux    Trier : Importance ▾ │ ● FORAD · Réseau social · 14:13              │
│ ▸ À traiter      38  │ [Rechercher…]  Canal: [Tous][Social][Chat][Presse][Msg] │ @fd_milice  (Milice de Fort-Rouge)           │
│   Signalés        2  │ ─────────────────────────────────────────────│ Camp : ● FORAD  · groupe eho FORAD ›         │
│   Tout            —  │ ▲ ALERTE  #OpFORAD · 23 publications/10 min  │ Origine : Scénario « Convois » ↗ (animation) │
│ CATÉGORIES DE SUIVI  │    ▸ déplier la rafale             14:13     │ ──────────────────────────────────────────── │
│ ● FORAD          21  │ ● FORAD  @fd_milice  Social   ♥42 ↻17 14:13  │ « Les convois de la 3e brigade ont franchi   │
│ ● GREYCELL        9  │   « Les convois de la 3e brigade… »          │   le pont… »                    [image]       │
│ ● Camp rouge      3  │ ● GREYCELL @vera_k ↔ @dan_o  Chat  6 msg 14:11│ ♥ 42  ↻ 17  ↩ 9   · audience 1 240 abonnés   │
│ ● #OpFORAD  ▲    23  │   [Afficher les messages]                     │ ──────────────────────────────────────────── │
│ ● HIGHCON         0  │ Presse  TV4 « Le gouverneur dément… » 14:10  │ Réponses (9) · Fil complet ›                 │
│ ● IA              4  │ ── Nouveau depuis 14:02 ──────────────────── │ Autres contenus de @fd_milice (1 h) : 6      │
│ + Nouvelle catégorie │ ● FORAD  @fd_echo  Social          13:58     │ ──────────────────────────────────────────── │
│ CANAUX               │ ...                                          │ [Vu ✓]  [À suivre ☆]  [Signaler ▾]           │
│ Social 21 · Chat 9   │                                              │   Signaler → à ma cellule · au MELMIL (fait) │
│ Presse 2 · Msg 6     │                                              │                                              │
│ ✕ Messagerie injoign.│ [Tout marquer vu jusqu'ici]                  │                                              │
├──────────────────────┴──────────────────────────────────────────────┴──────────────────────────────────────────────┤
│ Tendances : #OpFORAD 214 ▲×4 · #Delattre 96 · #Pont 41      Dernier passage 14:02 · 38 à traiter                   │
└────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

- **Hiérarchie** : à gauche, le **rail** (vues, catégories avec leurs non-traités, canaux) ; au centre, la **liste triée** (alertes et rafales en tête, puis importance = alerte > flambée > poids > récence) ; à droite, le **panneau de lecture** (contenu, auteur et camp en libellé, origine pour l'animation (avis n°85), interactions, fil, gestes de traitement).
- **Créer / régler une catégorie** : « + Nouvelle catégorie » en bas du rail (fenêtre C1) ; « ⋯ » au survol d'une catégorie (Modifier, Monter / Descendre, Supprimer) ; glisser un contenu sur une catégorie propose « Suivre @fd_echo dans FORAD ? ».
- **Passer d'un canal à l'autre** : segmenté « Canal » au-dessus de la liste (Tous · Social · Chat · Presse · Messagerie), croisé avec la catégorie choisie dans le rail ; le rail montre les effectifs par canal.
- **Volume** : **tri par importance** et **regroupement** (rafale de hashtag, conversation de Chat = 1 ligne, reprises d'un même article = 1 ligne) : 150 contenus deviennent ~40 lignes ; « Tout marquer vu jusqu'ici » ; lignes denses de 2 lignes ; liste virtualisée ; pas d'insertion en haut pendant la lecture (« 6 nouveaux ↑ »).
- **États** : *rien de neuf* → « Tout est traité · dernier contenu 13:58 », avec un lien « Voir tout » ; *alerte* → ligne épinglée en tête, ▲ + « ALERTE » ; *flambée* → ligne de rafale en tête et ▲ sur la catégorie du rail ; *canal injoignable* → ✕ dans le rail et bandeau dans la liste filtrée.
- **Forces** : **orientée traitement** (Vu, À suivre, Signaler à la cellule ou au MELMIL) : c'est le travail réel de l'analyste ; lecture rapide et riche, sans fenêtre ; modèle universellement connu ; garde la trace de ce qui a été vu.
- **Faiblesses** : **pas de vue d'ensemble** : on voit un contenu, pas la situation ; pression de la « boîte à vider » (150 / 10 min ne se traitent pas un par un : risque de survol aveugle) ; « qui pèse » se lit mal dans une liste ; le tri « importance » doit être expliqué sinon il paraît arbitraire ; le statut « vu » par animateur ou par cellule est une décision à prendre.

**À maquetter (C)** : barre de plateforme ; en-tête (onglets, état, action principale) ; rail (vues avec effectifs, catégories avec pastille + libellé + non-traités + ▲, « + Nouvelle catégorie », canaux avec ✕) ; barre de liste (titre de la vue, recherche, segmenté Canal, tri expliqué) ; lignes de contenu par canal (publication, conversation masquée, article, courriel, rafale repliable, ligne en alerte) ; trait « Nouveau depuis » ; panneau de lecture (contenu, auteur, camp en libellé, origine, interactions, fil, Vu / À suivre / Signaler ▾) ; « Tout marquer vu jusqu'ici » ; fenêtre « Nouvelle catégorie de suivi » ; états : tout traité, flambée, canal injoignable.

---

## 6. Comparaison

| Question de l'animateur (5 s) | A — Canaux | B — Situation | C — Boîte de réception |
|---|---|---|---|
| Que se passe-t-il ? | ◐ en lisant | ● bandeau + grille | ◐ en lisant |
| Où (camp, cellule, canal) ? | ◐ filtre par filtre | ● la ligne × la colonne | ◐ rail, un à la fois |
| Qui pèse ? | ○ bande du bas | ● par ligne + top 5 | ○ dans le panneau |
| Qu'est-ce qui a changé ? | ◐ trait « Nouveau » | ● « Ce qui a changé » + « + n » | ● non-traités |
| Lire et traiter un contenu | ● | ◐ via le volet | ● |
| Tenir 4 000 sources / 150 contenus en 10 min | ◐ pause + rafales | ● agrégats | ◐ tri + regroupement |
| Effort de mise en œuvre | faible | moyen (agrégats serveur) | moyen |

---

## 7. ⭐ Recommandation DESIGNER

**Construire B comme page d'accueil (« Situation ») et C comme onglet de travail (« À traiter »), partagés par la même fenêtre de catégorie de suivi et le même volet de lecture. Écarter A comme page principale.**

- **B répond au besoin écrit par l'utilisateur** (« comprendre en 5 secondes ») ; c'est la mise en page canonique du tableau de bord de situation (règle 38) et la seule qui reste lisible quand le volume monte. **C répond au travail qui suit** (lire, trier, signaler) ; une case de B ouvre C déjà filtré sur ce croisement (catégorie × canal). Deux onglets, un seul chemin par destination (règle 33).
- A est le plus facile, mais il **reconduit le problème** : on lit des flux au lieu de comprendre une situation. Son seul usage légitime : un **mode « mur »** plein écran pour un vidéoprojecteur en salle d'animation, plus tard, si on le demande.
- **Ordre de mise en œuvre proposé** : (1) catégories de suivi par règle, résolues côté serveur, avec heure de dernier passage (préalable à tout, ARCHITECTE/PLEIADE) ; (2) B sur le seul canal Réseau social, avec les colonnes Chat / Presse / Messagerie affichées « bientôt » plutôt que masquées ; (3) C ; (4) connecteurs Chat, presse, messagerie, après décision CYBERSECU sur les messages privés.
- **Valider avec 3 à 5 animateurs** sur les maquettes cliquables avant de coder (règle 40) : test « que se passe-t-il ? » à 5 s sur B, et tâche « trouvez qui a lancé #OpFORAD et signalez-le à votre cellule » sur B → C.

### Ce qu'on garde de l'existant
- **`TootItem`** (rendu d'une publication, médias, son, extrait parent) → ligne de C et volet ; **Tendances** avec le total commentaires compris et « ↩ » (avis n°92) ; **liste de groupes d'eho avec recherche** et archivés signalés (avis n°72) → dans la fenêtre de catégorie ; **premier écran** P1 (groupes en un clic) → devient « créer une catégorie depuis un modèle » ; **`MenuFixe`** (Échap, clic extérieur, focus rendu) ; **puce « Depuis le … × »** (filtre actif visible, P3) ; **priorité critique = alerte fixe**, sans clignotement (P2) → devient l'alerte « Dès le 1er contenu » d'une catégorie ; **espaces partagés gardés par l'Admin** (P8) → hébergent les catégories de suivi par cellule ; **Reporting** et **`GrapheTemps`** → mini-courbes de B et courbe de la fiche de catégorie ; **barre de plateforme** et **`AideEcran`** (« ? » contextuel).
- **À retirer** : mosaïque de cartes de sources sur la page principale (les sources deviennent une liste dans la fiche de catégorie) ; disposition libre par glisser + séparateurs + zoom 50-200 % (page stable, règle 28 ; le zoom du navigateur suffit) ; « Acquitter tout » en rouge ; « Nouveaux messages » ; panneau modal flouté (→ volet non modal) ; réglage « Actualiser toutes les n s » dans le pied (→ état « En direct · relu il y a n s » ; le réglage passe dans un menu Affichage, s'il faut le garder).

### Points à trancher par l'utilisateur
1. « Dernier passage » et « Vu » : **par animateur** ou **par cellule** ? (proposition : dernier passage par animateur, « Vu / Signalé » partagé par la cellule).
2. Messages privés (Chat, messagerie) : contenu visible ou métadonnées seules par défaut ? → **CYBERSECU**.
3. Mesure du **poids** : interactions (réactions, partages, réponses), audience (abonnés), ou les deux ? → données à fournir par ARCHITECTE.
4. Noms d'onglets : « Situation · À traiter » ou « Vue d'ensemble · À lire ».

⭐ **Doctrine dégagée** : *un outil de contrôle compte des variations depuis le dernier regard, pas des stocks ; il affiche des catégories (des règles), pas des sources (des copies) ; la vue d'ensemble et le traitement sont deux pages reliées, pas une page qui fait les deux.*
