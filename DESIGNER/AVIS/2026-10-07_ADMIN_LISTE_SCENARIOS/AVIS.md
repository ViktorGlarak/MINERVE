# Avis DESIGNER n°76 — app-admin, liste des Scénarios (maquette « Après »)

> **Date** : 2026-10-07 · **Écran** : app-admin › Scénarios (DELATTRE 26) · **Objet** : relecture de la maquette de l'orchestrateur `index.html` (versions Après / Avant), confrontée au code (`ScenariosList.tsx`, `format.ts`, `actions/route.ts`) et aux avis passés n°27, 36, 46, 47, 56, 69.
> **Statut** : proposition. L'utilisateur et PLEIADE tranchent ; mise en œuvre par PLEIADE / ARCHITECTE.

---

## 1. Constats

### 1.1 Ce que la maquette règle bien (à garder)
- **Des états expliqués** par une légende permanente : c'est le principe « aide tirée, état vide qui dit quoi faire » (règle 39) et la réponse à « c'est quoi "en lecture" ? ».
- **Des colonnes nommées** : « 06/10 14:29 → 22:32 », « 0/26 » ne se devinent plus (règle 7 inversée : ici l'étiquette manquait vraiment ; Nielsen 6).
- **Supprimer passe dans « ⋯ »**, séparé et en rouge, au lieu d'une corbeille à un clic d'un scénario lancé (Nielsen 5, règle 37).
- **« prochaine : dans 42 min »** en sous-ligne de la période : l'état du système est lisible sans ouvrir le scénario (règle 25).
- **« Mes scénarios »** : l'animateur qui revient retrouve les siens sans chercher (règle 28) ; le code sait déjà qui est l'auteur (`createdById`).

### 1.2 Grille de Nielsen (problèmes RESTANTS dans la maquette « Après », gravité 0 à 4)

| Heuristique | Problème restant | Gravité |
|---|---|---|
| 1. État visible | « En cours » sur 08.02.I03 dont la **première publication part dans 3 jours** : le mot dit « ça se passe maintenant », ce n'est pas vrai | 2 |
| 2. Langage de l'utilisateur | « En cours » ne correspond à **aucun bouton** : l'éditeur dit **Lancer · Pause · Reprendre**. Et « En lecture » est déjà un **homonyme** dans la zone : MELMIL a un rôle « Lecture et demandes » (= **lecture seule**) et affiche aussi l'état des scénarios de l'animation (`scenarios-admin.ts`) | 3 (avant) → 2 (« En cours ») |
| 4. Cohérence | **Quatre mots pour une notion** : « à corriger » (en-têtes), « en erreur » (ligne), « point bloquant » (ligne), « À surveiller » (filtre) ; « publiés / publiées » ; la confirmation de suppression dit encore « items » (lexique de zone : « publication ») | 3 |
| 5. Prévention des erreurs | Le menu « ⋯ » propose « Mettre en pause » sur **toutes** les lignes, y compris Brouillon et Terminé | 1 |
| 6. Reconnaissance | Les définitions sont dans une **bulle au survol seul** : rien au clavier, rien sur tablette. Le « ? » d'aide de l'écran actuel a **disparu** de la maquette | 2 |
| 8. Minimalisme | Un brouillon porte une barre de progression vide et « durée 8 h » ; 9 boutons de filtre sur une ligne (règle 37 : ~5) ; lignes de **52 px** contre 40 aujourd'hui (≈ −25 % de scénarios visibles, contraire à l'avis n°47) | 2 |
| 9. Aider à corriger | « avatar hors cellule » dit le problème, **pas comment le corriger** (changer l'avatar, ou demander l'autorisation à l'Administration : le drapeau `horsCellule` existe depuis aujourd'hui) | 3 |
| 3, 7, 10 | Rien de bloquant (pause, recherche par code, « ? » à rétablir) | 0-1 |

### 1.3 Accessibilité et couleur
- **Contraste** (calculé sur les jetons de la maquette) : `--faint` #6a7189 = **3,5 : 1** sur le panneau et 3,9 : 1 sur l'en-tête → **en dessous de 4,5 : 1** pour du texte de 11-12 px. Touchés : le mot **« Terminé »**, les **en-têtes de colonnes**, « durée… », « pas lancé ». Passer en `--muted` (6,5 : 1) — règle 21, REF-13. Les autres couples passent (vert 6,7 ; ocre 5,9 ; rouge sur fond rouge 5,2 ; cellules 4,7-4,9).
- **Le rouge revient en 5 endroits** : fond de ligne, liseré gauche, texte, pastilles des en-têtes, bordure du filtre « À surveiller ». Avec les erreurs « avatar hors cellule » qui vont se multiplier, on retombe dans le défaut d'origine (règle 20, Von Restorff).
- ⚠ **Collision avec l'avis n°56** : la maquette pose un **liseré rouge de 3 px à gauche** des lignes en erreur. Or c'est **exactement la place du liseré de cellule** (gris-bleu GREYCELL / ocre FORAD) déjà en ligne (`.pa-scn-ligne[data-cellule]::before`). Doctrine n°56 : une appartenance se montre par un repère **constant, même place**. L'erreur ne doit pas le recouvrir.
- ⚠ **Filtre de cellule appauvri** : la maquette ne garde que « GREYCELL · FORAD », sans « Toutes », sans « ? » (scénarios sans cellule), sans effectifs ni liseré — tout ce que l'avis n°56 (R3, R4) a fait mettre en place.
- ⚠ **Repères existants absents de la maquette** : « storyline · n », « l'incident a changé de jour », « n incidents non couverts », code lu dans le nom (pointillé). À conserver dans la colonne Scénario (avis n°27, 31).

---

## 2. Recommandations (classées par gain)

| # | Recommandation | Source | Effort |
|---|---|---|---|
| **R1** | **Nommer l'état actif « Lancé »** (et non « En cours ») et utiliser **les mêmes quatre mots partout** : badge, filtres (pas de pluriels différents), en-têtes de groupes, tableau de bord, Supervision, MELMIL (`scenarios-admin.ts`), lexique de zone §2. La définition de chaque état vit à **trois endroits stables** : la légende d'une ligne (gardée), le « ? » de l'écran (rétabli), et une bulle **au survol ET au focus** du badge (badge focalisable ou `aria-describedby`). | Règles 36, 15 (Jakob), 28 ; Nielsen 2 et 4 ; règle 11, WCAG 1.4.13 | **Faible** (2 tables de libellés + filtres + lexique) |
| **R2** | **Un seul mot pour le problème : « à corriger »**, et le rouge **sur la ligne fautive seulement** : icône ⚠ + texte rouge « 1 publication à corriger — avatar hors cellule : changez l'avatar, ou demandez l'autorisation à l'Administration ». **Pas de fond rouge ni de liseré rouge** (le liseré gauche reste la cellule, avis n°56) ; en-têtes de groupes en texte neutre avec l'icône ⚠ (« 2 à corriger »), sans pastille rouge. Distinguer les deux origines par le complément, pas par un autre mot : « à corriger avant de lancer » (vérification) / « publication à corriger » (envoi). | Règles 20, 24, 10, 36 ; Nielsen 9 ; avis n°56 | **Faible** |
| **R3** | **Remplacer « À surveiller » par « À corriger (n) »** — un filtre = une question. « Ce qui part bientôt » relève de la **Supervision** (suivi en direct) et de la sous-ligne « prochaine : dans 42 min » (gardée) ; si l'utilisateur tient à un filtre, en faire un **second, « Part dans l'heure »**, jamais mélangé à l'erreur. Le bouton n'est pas rouge (seul le chiffre peut l'être s'il est > 0). **Garder « Mes scénarios »**. | Règles 16, 33, 20, 28 ; Nielsen 8 | **Faible** (« À corriger », « Mes ») à **moyen** (« Part dans l'heure ») |
| **R4** | **Colonnes nommées, mais densité conservée** : lignes de **40 px** (avis n°47) ; texte secondaire en `--muted` (contraste) ; pour un **Brouillon** : « 26 publications » sans barre ni durée ; « durée » retirée partout (la période suffit) ; « publiées » partout ; **garder les repères existants** (storyline · n, décalage d'incident, incidents non couverts, code deviné). | Règles 5, 9, 21, 26 ; avis n°27, 31, 47 | **Faible à moyen** |
| **R5** | **Filtres en deux groupes nommés, tels que l'avis n°56 les a fixés** : « État : Tous · Brouillon · Lancé · En pause · Terminé » et « Cellule : Toutes · GREYCELL · FORAD · ? » avec effectifs et liseré, mémorisés par poste (déjà le cas). Les filtres de travail (« Mes scénarios », « À corriger ») restent à gauche, à côté de la recherche. Neuf boutons sur une ligne : on dépasse les ~5 de la règle 37, mais ce sont des gestes **fréquents** ; ne replier derrière « Filtres (n) » que si la ligne passe à deux étages. | Règles 37, 32 ; avis n°56 R3-R4 | **Faible** |
| **R6** | **Menu « ⋯ » selon l'état** : Brouillon → Ouvrir, Dupliquer, Exporter, Supprimer… ; Lancé → Ouvrir, **Pause**, … ; En pause → Ouvrir, **Reprendre**, … (mêmes verbes que l'éditeur). Comportement « bouton de menu » au clavier (flèches, Échap, retour du focus). La ligne entière ouvre le scénario, mais le lien est sur le **titre** pour le clavier et la lecture d'écran. Corriger « item(s) » → « publication(s) » dans la confirmation de suppression. | Nielsen 5 ; règles 11, 36, 37 ; REF-19 | **Faible** |

---

## 3. Libellés des états (proposition)

Les verbes de l'éditeur sont **Lancer · Pause · Reprendre** : l'état doit être le **participe du verbe** qui l'a produit. C'est ce qui rend le mot devinable sans aide (Nielsen 2).

| Technique | Aujourd'hui | Maquette | **Proposé** | Phrase d'aide (légende, « ? », bulle) |
|---|---|---|---|---|
| `draft` | Brouillon | Brouillon | **Brouillon** | « Pas encore lancé : rien ne part. Vérifiez, puis « Lancer ». » |
| `playing` | En lecture | En cours | **Lancé** | « Lancé : chaque publication part **toute seule** à son heure, même si personne ne regarde. Pour arrêter : « Pause ». » |
| `paused` | En pause | En pause | **En pause** | « Arrêté : rien ne part. À la reprise, tout ce qui reste est **décalé de la durée de la pause**. » *(vérifié dans le code : `resume` décale début et fin)* |
| `done` | Terminé | Terminé | **Terminé** | « Plus rien ne partira : toutes les publications sont parties, ou à corriger (voir le scénario). » |

**Pourquoi pas « En cours »** : faux pour un scénario lancé dont la première publication est dans plusieurs jours (cas réel 08.02.I03), et sans lien avec un bouton. **Pourquoi pas « Programmé »** : le mot est déjà pris deux fois dans la zone — état d'un **article** de presse (Brouillon · Programmé · Publié) et origine des publications au Reporting (« **programmées / en direct** », règle de vocabulaire du 06/10) — et il ment pour un scénario à moitié parti. « Lancé » est compatible avec ce vocabulaire : un scénario **lancé** produit des publications **programmées**.

Accord en genre : « scénario » est masculin → **Lancé**, **Terminé**. Filtres au singulier, identiques au badge (pas « Brouillons / Terminés » d'un côté et « Brouillon / Terminé » de l'autre).

---

## 4. Points à faire valider par l'utilisateur
1. **« Lancé »** plutôt que « En cours » ? (si oui : MAJ `PLEIADE\LEXIQUE_ZONE.md` §2, MELMIL `scenarios-admin.ts`, tableau de bord, Supervision, messages du serveur « en lecture »).
2. **« À corriger »** à la place d'« À surveiller » — et faut-il en plus un filtre **« Part dans l'heure »**, ou la Supervision suffit-elle ?
3. Un scénario **Terminé** qui a une publication à corriger reste-t-il dans « À corriger » ? (proposé : oui, tant que l'erreur n'est pas traitée ou acquittée).
4. Le texte d'aide de l'erreur « avatar hors cellule » : qui l'animateur doit-il contacter, concrètement (« l'Administration » suffit-il) ?
5. Test express (règle 40) : montrer la nouvelle liste à **2 ou 3 animateurs qui ne l'ont jamais vue** et leur demander « que veut dire *Lancé* ? que devez-vous corriger ? » avant de pousser.

---

## 5. Compléments du 07/10 — icônes et légende

### 5.1 Une icône par état : oui, mais la famille « cercle » de Lucide

**Avis** : l'idée de l'utilisateur est bonne, avec une nuance. Il faut **une icône pour chacun des quatre états**, toutes de la même famille, plutôt que le seul triangle ▶ à côté de « Lancé ».

**Pas de tension avec R1.** R1 écartait le **mot** « En lecture », qui a deux sens dans la zone (vidéo, lecture seule). Le **glyphe** ▶ n'a pas ce défaut : dans l'éditeur, il est déjà sur le bouton **« Lancer »**, et Pause / Reprendre suivent. L'état reprend donc le dessin du geste qui l'a produit, comme le mot reprend le verbe (Jakob, règle 15 ; doctrine n°76 « le nom d'un état est le participe du verbe »). Personne ne lira « vidéo » : il y a le mot « Lancé » à côté.

**Pourquoi le cercle, et pas `play` seul** :
- `play` et `pause` nus sont des **boutons** dans l'éditeur. Les mêmes glyphes dans une liste font croire qu'on peut cliquer pour lancer (Nielsen 4). Avec le cercle, on lit un **état** : le bouton garde le glyphe nu, le badge garde le glyphe cerclé.
- Un triangle nu se confond avec le **triangle d'alerte** ⚠ (`triangle-alert`), qui va beaucoup servir avec « avatar hors cellule ». Cerclé, on ne peut plus les confondre (règle 20 : le signal d'alerte reste unique).
- On obtient **quatre formes nettement différentes** dans un même contour : pointillé, triangle, deux barres, coche. Un daltonien les distingue sans voir la couleur (règle 10).

| État | Icône Lucide (`lucide-react`) | Couleur (= couleur du texte du badge, `currentColor`) |
|---|---|---|
| Brouillon | **`CircleDashed`** (`circle-dashed`) — inachevé, rien n'est parti | `--muted` (gris, 6,5 : 1) |
| Lancé | **`CirclePlay`** (`circle-play`) | vert `--online` (6,7 : 1 sur son fond) |
| En pause | **`CirclePause`** (`circle-pause`) | ocre `--dev` (5,9 : 1) |
| Terminé | **`CircleCheck`** (`circle-check`, déjà importé sous le nom `check-circle`) | `--muted` (pas `--faint`, cf. §1.3) |

- ⛔ **`pencil` / `pencil-line` écarté pour Brouillon** : c'est déjà l'icône d'action **« Modifier »** dans l'app (même confusion bouton / état). Le pointillé dit « pas encore là », comme le contour en pointillé du badge.
- ⛔ **Pas de rouge** dans les états : l'erreur n'est pas un état du scénario, elle porte son propre signal (R2).

**Taille, trait, place**
- **13 px**, trait **1,6**, l'icône **avant** le mot, 4 px d'écart, centrée verticalement. C'est le gabarit `Icon` de l'app, adapté à un badge en texte de 11,5-12 px (REF-08 : l'icône suit la taille du corps du texte).
- **Une seule couleur** pour l'icône et le mot (`currentColor`), sans second ton.
- **On retire le point vert** de la maquette (`.t-cours::before` avec son halo) : avec l'icône, cela ferait deux signaux pour un même état. Rien ne clignote ni ne pulse (règle 14 ; Supervision montre déjà le direct).
- Les **mêmes icônes** dans les boutons de filtre « État » et dans la légende (règle 36 : un état, un dessin, partout). Aucune dans les en-têtes de groupes, qui comptent les états en mots.

**Lecteur d'écran** : l'icône est **décorative** (`aria-hidden`, déjà le défaut du composant `Icon`). Le mot porte le sens. Dans la cellule de la colonne, on entend « **État : Lancé** » (en-tête de colonne associé, ou `<span class="sr-only">État : </span>`), puis la définition par `aria-describedby` quand le badge reçoit le focus (R1).

**Daltonien** : il voit la forme et le mot. La couleur n'est qu'un troisième indice (règle 10, WCAG 1.4.1). À vérifier au simulateur deutéranopie : vert et ocre se rapprochent, ce qui est sans conséquence puisque le triangle et les deux barres diffèrent.

⚠ **À vérifier à l'import** (lucide-react 1.45) : noms exacts `CircleDashed`, `CirclePlay`, `CirclePause`, `CircleCheck`. Les anciennes versions disaient `PlayCircle` / `PauseCircle`. À ajouter à la table `ICONS` de `components/Icons.tsx`, sans nouvelle dépendance.

### 5.2 Légende des états : UNE option — un dépliant au bout du filtre « État », ouvert la première fois

**Recommandation** : la légende devient un **dépliant** (motif *Disclosure*, REF-19). Il est **ouvert par défaut la première fois** sur un navigateur, puis **reste comme l'utilisateur l'a laissé**.

| Option | Verdict | Pourquoi |
|---|---|---|
| En bas du tableau | ⛔ | Sous 58 lignes, personne ne la voit. Or le problème d'origine (« c'est quoi en lecture ? ») vient d'un **nouvel** utilisateur, qui doit la trouver sans la chercher. |
| En haut, permanente | ⛔ | Pour l'habitué qui revient chaque jour, c'est une ligne de bruit qui repousse le tableau (règle 5, Nielsen 8). |
| Bulle au survol seulement | ⛔ seule | Ni clavier ni tablette. On la garde **en plus**, sur chaque badge (R1). |
| **Dépliant, ouvert à la 1re visite, état mémorisé** | ✅ | Le nouvel utilisateur la voit sans rien faire (constat d'origine). L'habitué la ferme une fois pour toutes (aide tirée, règle 39). Le **déclencheur ne bouge jamais** : rien n'apparaît ni ne disparaît sans qu'on l'ait demandé (règle 28). |

**Déclencheur**
- **Place** : au bout du groupe de filtres **« État »**, juste après « Terminé ». La question se pose à côté des mots qu'elle explique (proximité, règle 9).
- **Libellé** : « **Que veulent dire ces états ?** », avec l'icône `circle-help` (lucide : `CircleHelp`, alias `CircleQuestionMark` selon la version) **avant** le texte, et un chevron `chevron-down` qui pivote quand c'est ouvert. C'est la question de l'utilisateur, mot pour mot ou presque.
- **Style** : bouton **texte** discret (`--muted`, souligné au survol), pas une pastille de filtre. Il ne doit pas passer pour un cinquième état.

**Comportement**
- **Ouverture** : le panneau s'insère **dans la page**, sous la barre de filtres et au-dessus du tableau. Il pousse le tableau ; il ne flotte pas par-dessus les lignes, il ne se ferme pas tout seul. Il montre les 4 états sur une ligne (2 × 2 sur un écran étroit) : **badge avec son icône + la phrase d'aide du §3**.
- **Fermeture** : par le même bouton, ou par un lien « Masquer » à droite du panneau qui rend le focus au déclencheur.
- **Clavier** : `<button aria-expanded="true|false" aria-controls="legende-etats">`, `Entrée` et `Espace` ouvrent et ferment. `Échap` ferme si le focus est dans le panneau, puis rend le focus au déclencheur (règle 11). Anneau de focus visible.
- **Lecteur d'écran** : le panneau est une région nommée (`aria-labelledby` vers le déclencheur). Le lecteur annonce « développé » / « réduit ».
- **Mémoire** : ouvert ou fermé, enregistré **par navigateur** dans `localStorage`, avec la même clé d'affichage que les filtres (`CLE_AFFICHAGE`, propriété `legende: true|false`), lecture et écriture en `try/catch`. **Absent = ouvert** : un premier venu, un navigateur vidé ou une fenêtre privée voient la légende. C'est voulu.
- **Animation** : aucune, ou une ouverture de 150 ms au plus, coupée si « réduire les animations » est actif (règle 14).
- **Redondance voulue, sans rien de neuf à apprendre** : les mêmes 4 définitions dans le « ? » de l'écran (`AideEcran`) et dans la bulle du badge. Le texte est le même partout, écrit **une seule fois** dans le code (table des libellés, à côté de `STATUS_LABEL`).

**Point à faire valider** (n°6) : « ouverte la première fois, puis comme vous l'avez laissée » convient-il, ou l'utilisateur la veut-il **fermée par défaut** ? Le constat d'origine plaide pour l'ouverture.

### 5.3 Erreurs d'un scénario Terminé — ne compter que ce qui manque aux joueurs

**Constat (code vérifié)** : le « ⚠ n » de la liste additionne deux choses de nature différente.
- `scenario.errors` : les **remarques de la dernière vérification**, faite **avant** le lancement. Elles ne sont jamais effacées ensuite. Sur 07.24.I02, les 35 publications sur 35 sont parties, mais « ⚠ 1 » reste affiché. Le signal est faux, et un signal faux use l'alerte (règle 20, Nielsen 1).
- `counts.error` : les publications **réellement non parties** (statut `error`, avec un motif : avatar hors cellule refusé, app injoignable…). C'est la seule chose qui **manque aux joueurs**.

**Deux notions, deux mots** (règle 36, qui complète R2) :
- « **à corriger** » = ce que l'animateur doit traiter **maintenant**. Le mot est fixé en R2 et c'est le seul qui alimente le filtre « À corriger (n) ».
- Pour l'objet lui-même, on écrit **« non partie »** pour une publication en erreur (« 1 publication non partie — avatar hors cellule »), et **« remarque de vérification »** pour un retour de « Vérifier ». « Non partie » dit la conséquence pour les joueurs, là où « en erreur » ne dit que la cause technique.

**Règle d'affichage par état** (ce qui compte dans « ⚠ n », dans les en-têtes de groupes et dans le filtre « À corriger »)

| État | Remarques de vérification | Publications non parties | Ce qu'affiche la ligne |
|---|---|---|---|
| Brouillon | ✅ comptent | — (rien n'est parti) | « 2 à corriger avant de lancer » |
| Lancé | ⛔ ne comptent plus (le lancement a eu lieu, elles ont été vues : règle « avertissements vus avant Lancer ») | ✅ comptent | « 1 publication non partie — avatar hors cellule : … » |
| En pause | ⛔ sauf si le contenu a changé depuis la vérification (empreinte différente, il faudra re-vérifier pour reprendre) : alors « à re-vérifier avant de reprendre » | ✅ comptent | idem Lancé |
| Terminé | ⛔ **jamais** | ✅ comptent, **tant qu'elles ne sont pas prises en compte** | « 1 publication non partie » ; rien du tout si tout est parti ou pris en compte |

Les remarques de vérification restent **consultables** dans l'onglet de vérification du scénario (traçabilité). Elles quittent seulement la liste et les compteurs. C'est une règle d'affichage : aucune donnée n'est effacée.

**Le geste « Prise en compte »** (pour une publication non partie, surtout dans un scénario Terminé, où l'éditeur est en lecture seule)
- **Où** : sur la **ligne de la publication non partie, dans l'éditeur** (onglets Arbre et Chronogramme), dans le menu « ⋯ » de la publication et dans le bandeau de motif. Jamais depuis la liste : on décide en voyant le contenu et le motif (Nielsen 5). La liste propose seulement « Voir » qui ouvre le scénario sur la première publication non partie.
- **Deux sorties, dans cet ordre** (la meilleure option en premier, règle 16) :
  1. « **Publier maintenant** » (le geste existe déjà côté serveur : action `publish`, publication immédiate d'une publication). C'est la vraie réparation quand la cause a disparu (app revenue, autorisation hors cellule accordée). En Terminé, ce geste suppose qu'on puisse encore corriger l'avatar : **point à trancher par PLEIADE**.
  2. « **Prise en compte — ne pas publier** » : l'animateur décide que la publication ne partira pas (sans objet, déjà jouée autrement, remplacée par un post en direct).
- **Libellé de confirmation** : « Cette publication ne partira pas. Elle ne sera plus comptée dans "À corriger". » + champ « Motif (facultatif) », par exemple « remplacée par un post en direct », avec bouton principal « Prendre en compte » et « Annuler ».
- **Qui** : un animateur de la **cellule du scénario** (le même droit que modifier ce scénario), et l'Administration. Ni l'autre cellule, ni le rôle « Lecture et demandes ». ⚠ Avis **CYBERSECU** à demander sur le contrôle côté serveur (droit vérifié dans l'API, pas seulement en masquant le bouton).
- **Traçabilité** : on enregistre **qui** (identité Keycloak + nom affiché), **quand**, et le **motif** s'il y en a un, sur la publication et dans le **Journal** du scénario (« Publication #12 prise en compte par gc03 — remplacée par un post en direct »). La ligne garde un repère discret, gris et sans rouge : icône `circle-check` + « Prise en compte · gc03, 07/10 18:42 », motif au survol et au focus (règle 25 : l'état reste visible).
- **Réversible** : « **Annuler la prise en compte** », par le même menu, par la même personne, une autre personne de la cellule ou l'Administration. C'est tracé de la même façon, et la publication redevient « non partie » et recompte. Le statut technique `error` et son motif d'origine **ne sont jamais écrasés** : la prise en compte est un drapeau posé à côté (`priseEnCompte` : qui, quand, motif).
- **Effet sur les compteurs** : une publication prise en compte **sort** du « ⚠ n », des en-têtes de groupes et du filtre « À corriger ». Elle reste comptée dans « n / N publiées » comme **non publiée** (« 34 / 35 publiées · 1 prise en compte »), parce que c'est la vérité pour les joueurs. Une fois toutes les publications non parties prises en compte, la ligne Terminé redevient neutre.
- ⛔ **Pas d'« acquitter tout »** sur la liste. Un geste par publication, en voyant son contenu : une publication qui manque aux joueurs est un fait d'exercice, pas un bruit d'interface.

**Points à faire valider** :
- (n°7) En Terminé, autorise-t-on « Publier maintenant » après correction de l'avatar (cela rouvre l'édition d'une seule publication), ou seulement « Prise en compte » ?
- (n°8) Le droit de prendre en compte : la cellule du scénario + l'Administration, ou l'Administration seule ?

### 5.4 Décisions de l'utilisateur (07/10, en séance)
- **Icônes d'état** : validées sur le principe (l'utilisateur a lui-même demandé ▶ pour Lancé et ❙❙ pour la pause).
- **« Pause » au lieu de « En pause »** : décision de l'utilisateur, **contre** la règle « participe du verbe » du § 3. L'état s'écrit « ❙❙ Pause » (badge, filtre, légende, bulle). Le verbe du bouton de l'éditeur reste « Pause » : badge et bouton portent donc le même mot, l'icône cerclée distinguant l'état du bouton.
- Maquette mise à jour en conséquence (localhost:3851), avec la règle d'affichage par état (§ 5.3) et l'aperçu du geste « Prise en compte ».

## 6. Décisions de l'utilisateur — 2026-10-07 (les 7 points tranchés en séance)
1. **« Lancé »** pour l'état actif, partout dans la zone (liste, filtres, tableau de bord, Supervision, MELMIL). ✅ recommandé
2. Tri rapide : **« Mes scénarios » + « À corriger »** ; pas de « Part dans l'heure » (la Supervision s'en charge). ✅ recommandé
3. Autorisation « avatars hors cellule » : le message renvoie vers **l'Administration**. ✅ recommandé
4. **Pas d'essai** auprès d'animateurs nouveaux avant la mise en ligne (≠ recommandation : test de 2-3 personnes). Décision de l'utilisateur.
5. Légende des états **ouverte à la première visite**, puis choix retenu par navigateur. ✅ recommandé
6. Scénario Terminé, publication non partie : **« Changer l'avatar et publier maintenant » ET « Prise en compte — ne pas publier »**. ✅ recommandé (rouvre l'édition d'une seule publication : à prévoir côté PLEIADE)
7. Droit de « Prise en compte » : **cellule du scénario + Administration**, vérifié par le serveur, tracé. ✅ recommandé — avis CYBERSECU au développement.
+ « **Pause** » au lieu de « En pause » (§ 5.4).
