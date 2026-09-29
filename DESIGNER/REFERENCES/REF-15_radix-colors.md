# REF-15 — Radix Colors : l'échelle en 12 crans

- **Source** : https://www.radix-ui.com/colors/docs/palette-composition/understanding-the-scale · dépôt https://github.com/radix-ui/colors
- **Ingéré** : 2026-09-24 · **Licence** : MIT
- **Nature** : des palettes où **chaque cran a un usage défini**. On n'a plus à se demander quelle nuance prendre pour une bordure ou un survol.

| Crans | Usage |
|---|---|
| **1 – 2** | fonds de l'application, fonds discrets (cartes, barres latérales, blocs de code) |
| **3 / 4 / 5** | fond d'un composant **au repos / au survol / enfoncé ou sélectionné** |
| **6 / 7 / 8** | bordure **discrète** (non interactive) / bordure d'un **composant interactif** / bordure forte et **anneau de focus** |
| **9 / 10** | **aplat** le plus saturé (boutons, bandeaux) / son survol |
| **11 / 12** | **texte peu contrasté** / **texte très contrasté** |

- **Garantie** : les crans 11 et 12, posés sur le cran 2 de la même échelle, atteignent **Lc 60 et Lc 90** en contraste APCA.
- Le **mode sombre** a sa propre échelle, avec les **mêmes usages cran par cran** : on ne recalcule rien.
- Existe en **version transparente** (alpha), qui s'adapte à la surface sur laquelle elle est posée.

**Pour nos projets** : c'est la règle la plus directement applicable à nos thèmes. L'échelle `graphite-50…900` de MELMIL et de LEAC a 9 crans **sans usage défini** : chacun choisit sa nuance, d'où des écarts de contraste d'un écran à l'autre.
