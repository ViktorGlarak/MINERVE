# REF-01 — shadcn/ui

- **Source** : https://github.com/shadcn-ui/ui · docs https://ui.shadcn.com (thème : /docs/theming)
- **Ingéré** : 2026-09-24 · **Licence** : MIT
- **Nature** : collection de composants React **qu'on copie dans son code** (CLI / registre), pas une dépendance. « Open code » : le composant devient le nôtre, on le lit et on le modifie.

## Ce qu'il faut en retenir
- **Pile** : primitives accessibles **Radix UI** (ou Base UI) + **Tailwind CSS** + **variables CSS** pour le thème, mode sombre intégré.
- **Composition plutôt que configuration** : de petits morceaux assemblés (`Card` + `CardHeader` + `CardContent`…) plutôt qu'un gros composant à 40 options.
- **« Blocks »** : des assemblages prêts (tableau de bord, connexion, barre latérale) ; **Charts** (graphiques).
- Pensé pour être **lu et généré par une IA** : conventions régulières, peu de magie.

## ⭐ Le vocabulaire de jetons (réutilisable tel quel)
Principe : **paires surface / texte** — le jeton de base colore la surface, `-foreground` colore le texte et les icônes posés dessus.

| Paire | Rôle |
|---|---|
| `background` / `foreground` | fond et texte par défaut de l'app |
| `card` / `card-foreground` | surfaces surélevées |
| `popover` / `popover-foreground` | menus, infobulles, fenêtres flottantes |
| `primary` / `primary-foreground` | action principale (une par écran) |
| `secondary` / `secondary-foreground` | actions secondaires |
| `muted` / `muted-foreground` | surfaces discrètes, texte d'appoint |
| `accent` / `accent-foreground` | états interactifs (survol, sélection) |

Jetons simples : `destructive` (erreur, suppression) · `border` · `input` (bord des champs) · `ring` (anneau de focus) · `chart-1…5` · famille `sidebar-*` · `radius` (rayon de base, décliné sm → 4xl).

- **Format de couleur : `oklch(L C H)`** — la clarté (L) est perceptuellement régulière : deux teintes au même L paraissent aussi claires l'une que l'autre (ce que HSL ne garantit pas).
- **Mode sombre** : les mêmes noms redéfinis sous `.dark` — le code des composants ne change pas.
- **Ajouter une couleur** : la déclarer sous `:root` et `.dark`, l'exposer à Tailwind par `@theme inline`, l'utiliser (`bg-warning`, `text-warning-foreground`).

## Pour nos projets
- Nos thèmes PLÉIADE (`--color-shell / panel / ink…` de l'admin et de press, `graphite / craie` de MELMIL et LEAC) jouent le même rôle mais **sans la discipline « paire surface/texte »** : c'est ce qui manque pour garantir le contraste en clair ET en sombre sans vérifier écran par écran.
- Adopter la **méthode** (paires sémantiques, oklch, `.dark`) n'oblige pas à adopter les composants.
