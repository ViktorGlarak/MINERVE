# Avis n°73 — Cockpit : ce qu'on peut optimiser (2026-10-06)

**Demande utilisateur** : « voir avec DESIGNER et tes connaissances ce que tu peux optimiser sur l'app cockpit ; fais-moi des propositions ».
**Matière** : code de `app-cockpit` (en ligne : `e792921`), captures de la journée, retours de l'utilisateur pendant DELATTRE 26 (il ignorait qu'il fallait ajouter des sources ; groupes d'ORION au lieu d'eho ; 264 avatars rangés par erreur ; « je ne vois pas de diagramme »), grille d'audit §3.6 et règles 1-40.
**Statut** : propositions seulement, rien d'appliqué.

## Ce que le cockpit fait bien
- Flux en direct, tendances, fil global, recherche : la mise en page « flux » est la bonne (règle 38).
- Depuis aujourd'hui : groupes d'eho, en-tête à une action principale (« + Source »), actions groupées par catégorie.

## Constats (gravité Nielsen 0-4)

| # | Constat | Règle / heuristique | Gravité |
|---|---|---|---|
| C1 | **La configuration vit dans le navigateur** (sources, catégories, disposition, `localStorage`) : un autre poste, un autre navigateur ou un nettoyage = tout à refaire ; deux animateurs d'une même cellule ne partagent rien. L'export JSON existe mais personne ne le fait. | Nielsen 5 (prévention des erreurs), règle 19 (Tesler) | **4** |
| C2 | **Premier écran vide muet** : sans source, des panneaux « Aucune tendance », « En attente »… sans dire qu'il faut d'abord suivre quelque chose. Vécu par l'utilisateur ce jour. | Règles 18 et 39, Nielsen 10 | **3** |
| C3 | **Aucun moyen de retrouver une source** parmi 264 cartes : pas de filtre, pas de « seulement les non-lus ». | Nielsen 7 (efficacité), règle 37 | **3** |
| C4 | **Actions de la carte cachées** : la croix « Retirer » n'apparaît qu'au survol (20 × 20 px, sous le minimum de 24 px), rouge vif collée aux cartes voisines → clic accidentel ; « Modifier » n'existe qu'au **clic droit**, que personne ne devine. | Règles 12 et 6, Nielsen 6 (reconnaître plutôt que se souvenir) | **3** |
| C5 | **Les cartes clignotent** dès qu'il y a du non-lu (priorités normale et critique) : avec des dizaines de sources actives, tout clignote et l'alerte ne signale plus rien. | Règle 20 (Von Restorff : une alerte rare), règle 14 | **2** |
| C6 | **Le filtre « À partir du » est caché dans le pied de page** alors qu'il vide les panneaux et le Reporting : un filtre actif doit se voir. | Règle 25 (état du système visible), Nielsen 1 | **2** |
| C7 | **Vocabulaire** : « toots » (jargon Mastodon) au lieu de « publications » ; « Intervalle », « MAJ » ; pied de page en petites capitales mono, peu lisible. | Règles 36 et 26 | **1** |
| C8 | **« Statistiques »** affiche les totaux de **tout le réseau social**, pas des sources suivies, sans le dire. | Nielsen 2 (correspondance avec le monde réel) | **2** |
| C9 | **Le seul diagramme (Reporting) est rangé dans « Plus ▾ »** depuis ce midi ; l'utilisateur l'a cherché. | Règle 32 (visible selon la fréquence) | **2** |

## Propositions, classées par gain pour l'animateur

### Gains rapides (une demi-journée en tout, sans risque)
- **P1 — Premier écran qui guide (C2).** Sans source : un encart « Commencez par suivre un camp » avec les **groupes actifs d'eho en boutons** (CAMP ROUGE, CAMP BLEU…) : un clic = le groupe suivi **et** sa catégorie créée. Plus un lien « Suivre un compte ou un hashtag ».
- **P2 — Un seul signal d'alerte (C5).** Plus de clignotement pour la priorité normale (la pastille de non-lus suffit) ; la priorité **critique** garde un liseré fixe et remonte en tête de « Nouveaux messages ».
- **P3 — Le filtre actif se voit (C6, C8).** « À partir du » affiché dans l'en-tête quand il est réglé (« Depuis le 06/10 × ») ; « Statistiques » renommé « Réseau social — toute la zone ».
- **P4 — Mots (C7).** « publications » partout ; « Actualiser toutes les 30 s » ; « Dernière mise à jour 15:12 » ; pied de page en casse normale.
- **P5 — Reporting visible (C9).** Le remettre en bouton à côté de « Recherche » (« Courbes »), ou un mini-graphe par catégorie dans le panneau Statistiques.

### Gains moyens (un jour chacun)
- **P6 — Retrouver et trier (C3).** Un champ « Filtrer les sources » en haut du tableau (nom, @, réseau) et une bascule « Seulement les non-lus » ; les catégories vides de résultat se replient.
- **P7 — Actions de carte visibles (C4).** Un bouton « ⋯ » sur chaque carte (Modifier, Changer de catégorie, Retirer), la croix rouge disparaît ; **sélection multiple** (cases à cocher en mode « Sélectionner ») pour déplacer ou retirer quelques sources d'un coup — complément de « Toutes (n) ▾ ».

### Chantier structurant (après l'exercice)
- **P8 — Configuration partagée et sauvegardée sur le serveur (C1).** Les espaces de travail enregistrés côté cockpit, par cellule (GREYCELL, FORAD…) : on retrouve son tableau sur n'importe quel poste, et une cellule partage le même. Demande une base au cockpit (il n'en a pas en phase 1) → à voir avec PLEIADE / Xavier et CYBERSECU (qui peut voir l'espace d'une autre cellule).

## Recommandation DESIGNER
Faire **P1 à P5 tout de suite** (risque nul, gain immédiat pendant l'exercice), **P6-P7 ensuite**, **P8 après DELATTRE 26**. Valider P6/P7 en regardant 2 ou 3 animateurs s'en servir (règle 40).

⭐ **Doctrine confirmée** : un outil de veille ne vaut que par ce qu'on y a configuré — le premier écran doit amener à le configurer, et cette configuration ne doit pas pouvoir se perdre.
