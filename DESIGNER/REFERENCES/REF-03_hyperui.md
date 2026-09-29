# REF-03 — HyperUI

- **Source** : https://github.com/markmead/hyperui · site https://www.hyperui.dev
- **Ingéré** : 2026-09-24 · **Licence** : MIT · auteur Mark Mead (≈12 k étoiles)
- **Nature** : composants **Tailwind CSS v4** en **HTML pur**, à copier-coller. Aucun paquet, aucun JavaScript imposé.

## Ce qu'il faut en retenir
- Catalogue de **motifs** classés « Application UI » (tableaux, formulaires, alertes, badges, menus, pagination, grilles de statistiques, barres latérales…), « Marketing » (bannières, sections, pieds de page, témoignages…) et un volet **neobrutalism**.
- Utile comme **banque de départ** : on repère la structure d'un motif (espacements, hiérarchie) puis on la réécrit avec nos jetons.

## Pour nos projets
- Compatible avec toute notre pile (toutes les apps PLÉIADE sont en **Tailwind 4**).
- Le **webserver** et les sites d'exercice statiques (HTML autonome, sans React) peuvent reprendre ces motifs tels quels.
- ⚠ Les couleurs d'origine sont celles de Tailwind (`gray-*`, `indigo-*`) : les **remplacer par nos jetons** avant d'intégrer, sinon on réintroduit des couleurs hors charte.
