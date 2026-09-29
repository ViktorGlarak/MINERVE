# REF-12 — IBM Carbon Design System

- **Sources** : https://carbondesignsystem.com · sources de la documentation sur https://github.com/carbon-design-system/carbon-website (pages lues : accueil, jetons de couleur, usage du tableau de données)
- **Ingéré** : 2026-09-24 · **Licence** : Apache 2.0
- **Nature** : le design system d'IBM, conçu pour les **applications de données denses** (tableaux de bord, consoles, tableaux). C'est le plus proche de nos outils d'animation.

## Fondations
- **Grille 2x** : 12 colonnes, points de rupture sm / md / lg / xlg / max.
- **Espacement** (`$spacing-01` à `13`) : **2, 4, 8, 12, 16, 24, 32, 40, 48, 64, 80, 96, 160 px**.
- **Typographie** : IBM Plex, en deux jeux. Le jeu **« productive »** est compact, fait pour les outils. Le jeu **« expressive »** est plus aéré, fait pour les pages éditoriales.
- **4 thèmes** : White, Gray 10 (clairs), Gray 90, Gray 100 (sombres).

## ⭐ Le modèle de couches (jetons de couleur)
- `background` est la surface de base.
- `layer-01 / 02 / 03` sont les surfaces empilées (un panneau dans une page, une carte dans un panneau). Elles **alternent** : chaque couche se distingue de celle qui la porte.
- `layer-accent` sert aux surfaces d'emphase ; `field-01 / 02 / 03` au fond des champs, **selon la couche où ils sont posés**.
- **Bordures** : `border-subtle`, `border-strong`, `border-interactive`.
- **Texte** : `text-primary`, `-secondary`, `-placeholder`, `-helper`, `-on-color`, `-disabled`.
- **États** : `support-error`, `-success`, `-warning`, `-info` ; `focus` ; `interactive`.
- Un thème **redéfinit les valeurs, jamais les noms**. C'est la même logique que shadcn (REF-01) : un champ reste lisible quelle que soit la profondeur où il se trouve.

## Tableau de données (data table)
- **5 hauteurs de ligne** (de très petite à très grande). L'en-tête a **toujours la même hauteur que les lignes**.
- **Barre d'outils** : 5 actions au maximum, les autres dans un menu de débordement. Avec moins de 3 actions par ligne, les montrer directement sous forme d'icônes.
- **Actions groupées** : dès qu'une ligne est cochée, une barre d'actions groupées apparaît en haut ; les actions ligne par ligne se désactivent.
- **Tri** par l'en-tête de colonne ; recherche dépliable ou permanente.
- **Lignes zébrées** : elles aident la lecture horizontale des tableaux larges.
- **Pagination** simple (précédent / suivant) ou avancée (nombre par page, saut de page).
- ⚠ Un tableau de données **n'est pas un tableur** : pas d'interactions complexes dans les cellules.
