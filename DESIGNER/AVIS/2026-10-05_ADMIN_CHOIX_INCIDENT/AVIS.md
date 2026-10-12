# Avis DESIGNER n°65 — Admin : la fenêtre de choix de l'incident (création d'un scénario et « Changer… »)

> **Date** : 2026-10-05 · **Demandeur** : utilisateur · **Écrans** : app-admin › « Nouveau scénario » et fiche d'un scénario › « Changer… » (fenêtre « Cible du scénario »). Composants `IncidentPicker.tsx`, `ChoixCible.tsx`, `NewScenarioDialog.tsx`, `BandeauCible.tsx`.
> DESIGNER **propose**, il ne tranche pas (MEMOIRE §1).

## Besoin

« La fenêtre qui s'ouvre est trop petite, on ne voit pas grand-chose, c'est très difficile de choisir les incidents. »

## Constats (captures « avant » : `captures\avant-creation.png`, `avant-changer.png`)

| # | Constat | Heuristique (REF-14) | Gravité |
|---|---|---|---|
| C1 | Fenêtre « Changer… » : la liste déroulante est **rognée par la fenêtre** — on voit **une seule ligne** d'incident sur 89. | 1 visibilité ; 7 efficacité | **4** |
| C2 | Création : fenêtre de 620 px, liste flottante de 320 px posée **par-dessus** le formulaire : 5 incidents visibles, les champs du dessous masqués. | 8 minimalisme ; 6 reconnaissance | 3 |
| C3 | 89 incidents en une seule colonne : pour trouver une storyline il faut faire défiler ou connaître le code. | 6 reconnaître plutôt que se souvenir ; Hick (REF-06) | 3 |
| C4 | Dans « Changer… », il faut d'abord cliquer « Changer » sur l'étiquette pour voir la liste, alors qu'on est venu précisément pour changer. | 7 efficacité | 2 |
| C5 | Mode « Une storyline » : un menu `<select>` puis une liste de cases limitée à 280 px. | 6 ; 8 | 2 |

## Recommandations

**R1 — La liste fait partie de la fenêtre, elle ne flotte plus** *(gain fort, effort moyen)*.
La liste s'affiche dans le flux de la fenêtre, sur une hauteur fixe d'environ la moitié de l'écran (`min(52vh, 520px)`), avec son propre défilement : plus rien n'est rogné ni masqué. — *Nielsen 1 ; Carbon (REF-12) : une liste de sélection longue est un panneau, pas un menu.*

**R2 — Une fenêtre large, en deux colonnes « storylines | incidents »** *(gain fort, effort moyen)*.
Largeur portée à **960 px** (création et « Changer… »). À gauche, la liste des storylines avec leur nombre d'incidents, et « Toutes » en tête ; à droite, les incidents de la storyline choisie. La recherche (code, intitulé, storyline) reste en haut et filtre les deux colonnes. — *Modèle maître-détail (Carbon, Blueprint REF-04/05) ; Hick : on choisit d'abord parmi 15 storylines, puis parmi quelques incidents.*

**R3 — Des lignes d'incident lisibles, le choix courant marqué** *(gain moyen, effort faible)*.
Code, **intitulé entier** (jusqu'à deux lignes), moment D+ et date, nombre de scénarios déjà rattachés ; l'incident actuellement choisi porte une coche et la mention « actuel ». — *REF-07 : la forme de la donnée parle d'elle-même ; Nielsen 1.*

**R4 — « Changer… » ouvre directement la liste** *(gain moyen, effort faible)*.
Dans la fenêtre « Cible du scénario », la liste est ouverte d'emblée, positionnée sur la storyline de l'incident actuel. À la création, une fois l'incident choisi, la liste se replie en étiquette (le formulaire reste court). — *Nielsen 7 ; Tesler (REF-06) : le système sait déjà où l'on en est.*

**R5 — Le mode « Une storyline » suit le même gabarit** *(gain moyen, effort faible)*.
Storylines à gauche (boutons radio), incidents à cocher à droite sur la même hauteur que R1, « Tout cocher / Tout décocher » conservé. — *Cohérence (Nielsen 4) entre les deux modes.*

## Ce qui ne change pas

Le segment « Un incident / Une storyline / Bruit de fond », la recherche tolérante (« 08.01.04 » = « 08.01.I04 »), le clavier (flèches, Entrée, Échap), les règles d'enregistrement.

## Suite

Appliqué dans app-admin le 2026-10-05 (branche `choix-incident-large`) ; captures « après » dans `captures\`.
