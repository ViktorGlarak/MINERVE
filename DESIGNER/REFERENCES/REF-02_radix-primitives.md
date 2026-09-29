# REF-02 — Radix Primitives

- **Source** : https://github.com/radix-ui/primitives · docs https://www.radix-ui.com/primitives
- **Ingéré** : 2026-09-24 · **Licence** : MIT · maintenu par **WorkOS** (≈19 k étoiles)
- **Nature** : composants React **sans style**, dont le travail est le **comportement** : accessibilité, clavier, focus.

## Les 4 principes
1. **Accessible** — suit les modèles **WAI-ARIA** ; gère focus, navigation clavier, lecteurs d'écran.
2. **Sans style** — aucune apparence imposée : on habille avec nos jetons.
3. **Ouvert** — chaque sous-partie est exposée (`Dialog.Trigger`, `Dialog.Content`…) ; `asChild` fait porter le comportement par notre propre élément.
4. **Non contrôlé par défaut** — fonctionne seul, mais se pilote par l'état si besoin.

Installation : paquet unique `radix-ui` ou primitive par primitive (`@radix-ui/react-dialog`). Adoption **incrémentale** possible.

## Primitives utiles (liste de la documentation)
Accordion · Alert Dialog · Aspect Ratio · Avatar · Checkbox · Collapsible · Context Menu · **Dialog** · **Dropdown Menu** · Form · Hover Card · Label · Menubar · Navigation Menu · **Popover** · Progress · Radio Group · Scroll Area · **Select** · Separator · Slider · Switch · **Tabs** · **Toast** · Toggle / Toggle Group · Toolbar · **Tooltip** ; utilitaires Portal, Slot, Visually Hidden.

## Pour nos projets
- Ce que Radix résout est ce qu'on **refait à la main et oublie souvent** : piège du focus dans une fenêtre modale, `Échap` pour fermer, retour du focus au bouton d'origine, menus au clavier, `aria-*`.
- Exemple concret : la fiche de compte rendu de MELMIL (2026-09-24) est une fenêtre modale maison : elle gère `Échap`, mais **ni le piège du focus ni le retour du focus**. Une primitive `Dialog` le ferait.
- ⚠ Ajouter une dépendance relève d'ARCHITECTE / PLEIADE : DESIGNER **recommande**, il ne décide pas.
