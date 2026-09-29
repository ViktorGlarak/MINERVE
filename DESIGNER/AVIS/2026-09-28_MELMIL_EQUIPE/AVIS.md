# Avis DESIGNER n°10 — MELMIL, onglet « Équipe » : l'architecture de l'exercice

> **Date** : 2026-09-28 · **Demande** : l'onglet Équipe ne sert pas, il est « mal pensé ». L'utilisateur veut qu'on puisse créer des groupes et avoir une architecture claire de l'exercice, « une sorte d'araignée avec des groupes et des utilisateurs à l'intérieur » (par exemple GREY CELL, avec des noms et leur grade), et pouvoir rattacher un compte Pléiade de la zone si besoin. On commence simple, on peaufine ensuite.

## Constat sur l'ancien écran
- Une grille de cartes de cellules, où chaque personne était un **formulaire toujours ouvert** (fonction, nom, cellule, précision, contact) : 5 champs par ligne, rien ne se lisait d'un coup d'œil *(règle 5 : la hiérarchie vient de ce qu'on atténue)*.
- La cellule se tapait à la main : une faute de frappe créait une nouvelle cellule.
- Aucun moyen d'emboîter des groupes, ni de voir l'ensemble.

## Solution retenue

**R1 · Lire d'abord, modifier ensuite** *(heuristique 8 : design minimaliste)* : les cartes n'affichent que « GRADE Nom » et, pour le chef et le second, leur fonction. Un clic ouvre la fiche dans le panneau de droite, comme les incidents *(règle 15, Jakob : même geste partout dans l'atelier)*.

**R2 · Deux vues du même contenu** :
- **Araignée** : l'exercice au centre ; les groupes sur une première couronne, reliés par un trait plein ; leurs sous-groupes sur une seconde couronne, reliés par un trait pointillé à leur parent. La hauteur du dessin suit son contenu.
- **Liste** : les groupes en colonnes, les sous-groupes emboîtés.
- Au téléphone, c'est la Liste d'office, car l'araignée n'y a pas la place *(règle 16)*.

**R3 · Des choix plutôt que de la saisie** *(Postel, règle 17)* :
- le grade dans une liste (GAL → SDT, CIV), ordonnée hiérarchiquement, qui sert aussi à trier ;
- le groupe dans une liste ;
- la fonction en boutons segmentés ;
- le compte Pléiade par recherche dans les comptes de la zone.

**R4 · Un groupe se reconnaît à sa couleur, et pas seulement à elle** *(règle 10)* : bandeau de carte, trait et grade teintés, mais le nom est toujours écrit. 8 teintes foncées, texte blanc lisible en clair comme en sombre.

**R5 · Une seule action principale** *(règle 6)* : « + Groupe » en plein ; « + Personne » en secondaire.

**R6 · Premier écran vide qui dit quoi faire** *(règle 18)*.

**R7 · Rien de l'existant n'est perdu** :
- les cellules citées par les personnes ou les events apparaissent comme groupes ;
- un grade saisi dans le nom (« CNE Julie MARTIN », suivant l'ancien libellé « Grade, nom ») est séparé automatiquement.

## Pistes pour la suite (non faites)
- Glisser une personne d'un groupe à l'autre dans l'araignée.
- Exporter l'organigramme (PNG ou PDF) pour le briefing.
- Réserver la création de groupes à un rôle précis : aujourd'hui, tout utilisateur de MELMIL a le rôle `admin`.
