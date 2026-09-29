# REF-19 — WAI-ARIA Authoring Practices Guide (APG, W3C)

- **Source** : https://www.w3.org/WAI/ARIA/apg/patterns/ (pages lues : liste des modèles, Dialog modal, Tabs)
- **Ingéré** : 2026-09-24 · **Accès** : libre · **C'est la référence normative du comportement des composants.**

**30 modèles** : Accordion · Alert · Alert Dialog · Breadcrumb · Button · Carousel · Checkbox · Combobox · **Dialog (modal)** · Disclosure · Feed · Grid · Landmarks · Link · Listbox · Menu · Menubar · Menu Button · Meter · Radio Group · Slider (simple ou à plusieurs curseurs) · Spinbutton · Switch · Table · **Tabs** · Toolbar · Tooltip · Tree View · Treegrid · Window Splitter.

## Dialog (modal)
- `Tab` et `Maj+Tab` **tournent à l'intérieur** de la fenêtre et n'en sortent pas ; `Échap` ferme.
- **Focus à l'ouverture** :
  - le **titre** (ou un élément statique en `tabindex="-1"`) pour une fenêtre longue ;
  - l'**action la moins dangereuse** pour une confirmation destructrice ;
  - l'action principale pour une fenêtre simple.
- **À la fermeture**, le focus **revient à l'élément qui l'a ouverte**.
- Attributs : `role="dialog"`, `aria-modal="true"`, `aria-labelledby` pointant sur le titre visible.
- L'arrière-plan est **rendu inerte** (attribut `inert`) : bloqué pour la souris comme pour le clavier.

## Tabs (onglets)
- Rôles `tablist` (avec un `aria-label`), `tab` (`aria-selected`, `aria-controls`) et `tabpanel` (`aria-labelledby`).
- **Flèches gauche et droite** pour passer d'un onglet à l'autre, en bouclant ; `Début` et `Fin` pour aller au premier et au dernier.
- `Tab` entre dans la liste sur l'onglet actif, puis en sort vers le panneau.
- Activation **automatique au focus** si le panneau s'affiche sans délai.
