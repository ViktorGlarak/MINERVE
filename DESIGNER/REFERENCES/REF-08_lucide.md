# REF-08 — Lucide (icônes)

- **Source** : https://github.com/lucide-icons/lucide · https://lucide.dev
- **Ingéré** : 2026-09-24 · **Licence** : ISC (libre, y compris usage commercial)
- **Nature** : plus de **1 600 icônes SVG** issues d'un fork communautaire de **Feather Icons**.

## Ce qu'il faut en retenir
- **Style unique** : grille **24 × 24**, **trait de 2 px**, extrémités et jonctions **arrondies**. Toutes les icônes se ressemblent : c'est ce qui les rend combinables.
- Paquets pour chaque cadre : `lucide-react`, `-vue`, `-svelte`, `-solid`, `-preact`, `-angular`, `-astro`, `-react-native`, `lucide-static` (SVG bruts, sprite, police).
- Réglages : `size`, `color` (hérite de `currentColor`), `strokeWidth`, `absoluteStrokeWidth` (trait constant quelle que soit la taille).
- **Tree-shaking** : on n'embarque que les icônes importées.
- **Aucun logo de marque**, par principe (raisons juridiques et de cohérence). Nos logos de médias fictifs restent donc à produire nous-mêmes.

## Pour nos projets
- **Déjà utilisé** : `lucide-react` 1.45 dans **app-admin** et **app-press**. MELMIL et LEAC n'ont pas de bibliothèque d'icônes.
- Règles d'emploi :
  - une icône **accompagne** un libellé, elle ne le remplace pas, sauf pour les gestes universels (fermer, rechercher) ; dans ce cas, `aria-label` est obligatoire ;
  - **une seule épaisseur de trait** par application ;
  - taille alignée sur le corps du texte : 16 px pour du texte à 14 px, 20 px pour 16 px.
