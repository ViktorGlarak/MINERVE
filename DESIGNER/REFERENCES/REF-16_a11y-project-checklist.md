# REF-16 — The A11Y Project : liste de contrôle

- **Source** : https://www.a11yproject.com/checklist/
- **Ingéré** : 2026-09-24 · **Accès** : libre
- **Nature** : la liste de contrôle d'accessibilité la plus pratique, à passer **avant chaque livraison**.

**Contenu** : langage simple · libellés de boutons et de liens **uniques et parlants**.
**Code global** : `lang` sur `<html>` · un **titre unique par page** · zoom jamais bloqué · repères `<nav>` et `<main>` · pas de `tabindex` positif · **pas d'`autofocus`** · délais de session prolongeables · aucune information portée par le seul attribut `title`.
**Clavier** : **focus visible** · ordre du focus conforme à l'ordre visuel · rien de focalisable qui soit invisible.
**Images** : `alt` partout, vide pour une image décorative ; un texte équivalent pour les graphiques.
**Titres** : **un seul `h1`** · niveaux dans l'ordre, sans saut.
**Contrôles** : `<a href>` pour un lien, `<button>` pour une action · liens reconnaissables **autrement que par la couleur** · **lien d'évitement** (« aller au contenu ») · signaler l'ouverture d'un nouvel onglet.
**Tableaux** : `<th scope>` · `<caption>`.
**Formulaires** : `<label for>` sur chaque champ · `<fieldset>` et `<legend>` pour grouper · `autocomplete` · **erreurs listées au-dessus du formulaire** et reliées aux champs (`aria-describedby`) · erreur, avertissement et succès signalés **autrement que par la couleur**.
**Apparence** : lisible à 200 % · lisible en contraste élevé · mises en page simples et cohérentes.
**Animation** : sobre · respecte `prefers-reduced-motion`.
**Contraste** : texte 4,5 : 1 · grand texte 3 : 1 · **icônes et bords de champs 3 : 1**.
**Tactile** : toutes les orientations · pas de défilement horizontal · cibles assez grandes et espacées.
