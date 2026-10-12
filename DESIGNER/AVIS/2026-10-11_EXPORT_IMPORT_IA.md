# Avis DESIGNER n°99 — 2026-10-11 — eho, Population IA : « Exporter / importer les fiches IA »

> Écran lu : `C:\CECPC\pleiade\eho\src\app\(admin)\population-ia\page.tsx` (interrupteur, effectifs, liste), `components\confirmer.tsx`. Aucun code modifié.
> Besoin (décision utilisateur) : exporter les fiches de la population IA (105 au plus) pour les relire et les corriger hors ligne, puis les réimporter. Le serveur fait d'abord une vérification sans rien écrire, l'utilisateur confirme, ensuite seulement le serveur applique. `cohorte` et `orientation_initiale` sont protégées, la mémoire n'est jamais importée, une sauvegarde est faite avant.
> Ce sont des **propositions** : le besoin de l'utilisateur et les choix de PLEIADE priment.

## R1. Emplacement : une section à part, en bas de la page (gain fort, effort faible)

- **Après « Les avatars »**, en dernière section, avec la même carte blanche (`rounded-xl border bg-white`). C'est une tâche **rare, de préparation**. Placée avant les effectifs, elle gênerait le geste de tous les jours (Hick, REF-06 ; mettre en valeur en atténuant le reste, REF-07).
- Titre h2 : **« Fiches de comportement : exporter, corriger, réimporter »**.
- Phrase d'introduction : *« Pour relire ou corriger les fiches hors ligne : téléchargez-les, modifiez le fichier, puis déposez-le ici. Rien ne change avant votre confirmation. La cohorte, l'orientation de départ et la mémoire d'exercice ne sont jamais modifiées par un import. »*
- Deux blocs côte à côte (empilés sous 640 px) : **Exporter** à gauche, **Importer** à droite. Les deux boutons sont **secondaires** (bordure, pas d'aplat indigo) : l'action principale de la page reste « Appliquer » des effectifs (une seule action principale, REF-01).

## R2. Exporter : un bouton qui dit ce qu'il télécharge

- Bouton : **« Télécharger les fiches (105 avatars) »**, où le nombre est `pop.total`. Si le total vaut 0, le bouton est désactivé avec la mention *« Aucun avatar n'a de fiche de comportement dans cette zone. »*
- Sous le bouton, une ligne discrète : *« Contient la fiche, la cohorte, le lieu et la mémoire d'exercice de chaque avatar. À garder pour l'animation : ne pas transmettre aux joueurs. »*
- Nom du fichier : `fiches-ia_<zone>_2026-10-11_1742.json`. Lisible, daté, et rangé dans l'ordre chronologique.
- Après le téléchargement, message `role="status"` : *« Fichier téléchargé : 105 avatars, le 11/10 à 17:42. »*
- **Remontée PLEIADE** : mettre un en-tête dans le fichier (`format`, `version`, `zone`, `exporteLe`), pour reconnaître un mauvais fichier à l'import. Pour chaque avatar, ordonner les clés `username`, `nom`, `comportement`, puis `etat` **en dernier**, sous un nom qui dit qu'il n'est pas réimporté (par exemple `etat_non_importe`). Celui qui corrige à la main voit ainsi ce qui compte.

## R3. Importer : déposer, vérifier tout de suite, montrer le résultat dans la page (gain fort)

**Dépôt**
- Une zone en pointillés : *« Déposez le fichier ici »* et un bouton **« Choisir un fichier… »**. Le libellé est le nôtre, en français, et l'`input type=file` reste masqué (avis n°93). On accepte `.json`.
- **Pas de bouton « Vérifier » en plus** : la vérification part dès que le fichier est choisi (Tesler, REF-06). Pendant ce temps, la zone affiche *« Vérification du fichier… »*.
- Dans l'écran, écrire **« Vérification »** plutôt qu'« essai à blanc », qui est un mot de métier.

**Erreurs sur le fichier entier** (à la GOV.UK, REF-10 : dire comment corriger, dans un encadré qui reçoit le focus)
- Fichier illisible : *« Ce fichier n'est pas lisible. Téléchargez les fiches pour avoir un modèle, corrigez-le, puis réessayez. »*
- Fichier valide mais sans aucun avatar reconnu : *« Ce fichier ne contient aucune fiche d'avatar. Il doit venir de « Télécharger les fiches ». »*
- Fichier trop gros : *« Fichier trop volumineux (2 Mo au plus, 500 avatars au plus). »* Le serveur doit **borner** la taille et le nombre d'entrées (incident de l'import Excel du 06/10).
- Fichier exporté depuis une autre zone : un **avertissement**, pas un refus : *« Ce fichier a été exporté depuis la zone « X ». Seuls les avatars présents ici sont pris en compte. »*

**Résultat de la vérification**, affiché **dans la section** et non dans une fenêtre. Une liste de 105 lignes se relit, se fait défiler et se compare. Une fenêtre qui se ferme au clic extérieur ferait perdre la relecture, et la règle « clic extérieur » ne s'applique pas à un contenu de page.
1. Bandeau d'état en tête, qui reçoit le focus : **« Vérification de « fiches-ia_…json » : rien n'a encore été modifié. »** (Nielsen 1, REF-14).
2. Quatre compteurs, chacun avec une forme et un mot, jamais la couleur seule (REF-07) : **● 12 modifiés · ✕ 2 refusés · – 3 ignorés · = 88 inchangés**. Chaque compteur est un lien vers son groupe.
3. **Regroupement par statut**, dans l'ordre de ce qui demande une action. Chaque groupe est un `<details>` natif, accessible au clavier, avec son effectif dans le titre :
   - **Refusés : dépliés.** Pour chaque avatar, la raison et la façon de corriger, avec le champ en clair : *« Sensibilité · peur : doit être un nombre de 0 à 100 (lu : “beaucoup”). »* Ces fiches ne seront pas appliquées, les autres oui.
   - **Modifiés : dépliés.** Tableau à 2 colonnes, **Avatar** (nom, @identifiant, lien vers la fiche dans un nouvel onglet) et **Changements** en puces courtes : « Consignes +3 », « Interdits +2 », « Sensibilité · peur 40 → 55 ». On montre 4 puces au plus, puis « +n autres ». Un lien **« Voir le détail »** déplie sur place l'avant et l'après des textes (ancien barré, nouveau en gras). Une tentative sur un champ protégé apparaît **dans la ligne**, en marqueur orange distinct : *« Cohorte : changement ignoré (base ancrée) »*.
   - **Ignorés : repliés**, avec la raison en mots : *« inconnu dans cette zone »*, *« n'a pas de fiche de comportement »*, *« hors population IA »*.
   - **Inchangés : repliés**, le compte suffit.
4. Si le fichier contient de la mémoire, **une seule ligne**, pas une par avatar : *« La mémoire d'exercice présente dans le fichier est ignorée. »*
5. Les noms de champ sont **en français**, jamais en notation technique (`sensibilites.peur` → « Sensibilité · peur »). **Remontée PLEIADE** : un seul dictionnaire de libellés, partagé avec la fiche de l'avatar.
6. Aucun changement : *« Rien à appliquer : les 105 fiches du fichier sont identiques à celles de la zone. »* Seul le bouton « Fermer » est proposé.

## R4. Confirmer : une case de sauvegarde cochée, un bouton qui compte (gain fort)

- Pied du résultat :
  - case **cochée par défaut** : **« Télécharger d'abord une sauvegarde des fiches actuelles »**. On met en avant l'option recommandée (Hick, REF-06) ;
  - bouton principal **« Appliquer les 12 modifications »** ;
  - lien **« Abandonner »**, qui vide le résultat.
  - S'il y a des refus, une mention à côté du bouton : *« Les 2 fiches refusées ne seront pas appliquées. »*
- `confirmer`, sans `danger`, puisqu'on peut revenir en arrière avec la sauvegarde :
  - titre : **« Appliquer 12 modifications de fiches ? »** ;
  - texte : *« Les fiches de Nom1, Nom2, Nom3, Nom4, Nom5 et 7 autres vont changer. La cohorte, l'orientation de départ et la mémoire d'exercice ne changent pas. Le moteur prendra les nouvelles fiches en compte dans les dix minutes. »* Si la case est cochée, ajouter : *« Une sauvegarde des fiches actuelles est téléchargée avant. »* ;
  - bouton : **« Appliquer »**.
- La sauvegarde est téléchargée **avant** l'envoi. **Remontée PLEIADE / CYBERSECU** : garder aussi une copie côté serveur (le navigateur peut bloquer le téléchargement) et journaliser l'import (qui, quand, combien de fiches).
- **Le serveur applique exactement ce qui a été montré** (doctrine n°98 : un état s'affiche relu, et l'on refuse si l'état a changé). La vérification rend une empreinte de l'état des fiches, et l'application la renvoie. Si une fiche a été modifiée entre-temps : *« Des fiches ont changé depuis la vérification (modification par un autre animateur ?). Rien n'a été appliqué : relancez la vérification. »* avec un bouton **« Vérifier à nouveau »** (409).

## R5. Après l'application : une fin nette, et le moyen de revenir en arrière (Peak-End, REF-06)

- Le résultat est remplacé par un bandeau vert `role="status"`, qui reçoit le focus : **« 12 fiches mises à jour à 17:46. Le moteur les prendra en compte d'ici 17:56. »**
- Deuxième ligne : *« Sauvegarde : fiches-ia_…_avant-import.json. Pour revenir en arrière, déposez ce fichier ici. »*
- Liste repliée **« Avatars modifiés (12) »**, avec un lien vers chaque fiche.
- Échec partiel : *« 10 fiches mises à jour, 2 en échec »*, avec la raison par avatar et le même format que les refus.
- Facultatif, à voir avec PLEIADE : si le moteur annonce la version des fiches qu'il a chargée, remplacer « d'ici 17:56 » par l'état relu **« en attente du moteur »**, puis **« prises en compte à 17:51 »** (doctrine n°98).

## Accessibilité et règles maison

- Pas de fenêtre ouverte par un bouton, en dehors de `confirmer` qui gère déjà Échap, le voile et le retour du focus. Les détails se déplient sur place.
- La zone de dépôt reste utilisable au clavier (le bouton « Choisir un fichier… »).
- Le focus va au bandeau de vérification, puis au bandeau final.
- Les statuts portent une forme et un mot.
- Au téléphone, le tableau des modifiés devient une pile de cartes.
- Vocabulaire : « fichier », « fiche », « animation », « vérification ». Jamais « JSON », « Admin » ou « dry-run ».
