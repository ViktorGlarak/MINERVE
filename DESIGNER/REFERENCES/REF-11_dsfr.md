# REF-11 — DSFR, le Système de design de l'État français

- **Sources** : https://github.com/GouvernementFR/dsfr (README ; le site systeme-de-design.gouv.fr refuse la lecture automatique)
- **Ingéré** : 2026-09-24 · Maintenu par le **SIG** (Service d'information du Gouvernement) · Code sous licence **Etalab 2.0**
- **Nature** : composants HTML, CSS et JS des sites de l'État, conformes au **RGAA**.

## ⛔ Restriction d'usage (texte du dépôt)
> « Given its role as a marker of the French State's visual identity, the DSFR **must not be used by entities outside the public administration**. It cannot be used outside a **.gouv.fr** domain name. »

- ⚠ Nos outils PLÉIADE ne sont pas des sites `.gouv.fr` : **interdiction d'utiliser le DSFR, la police Marianne, le logo ou le bloc-marque**.
- ⚠ Les **sites d'exercice** qui imitent un ministère ou une préfecture ne doivent pas non plus reprendre le DSFR ni la Marianne. Utiliser une **identité fictive** (règle MINERVE : jamais d'usurpation d'une organisation réelle hors exercice). Avis à faire valider par l'utilisateur au cas par cas.
- Ce qu'on peut reprendre : les **idées**, qui ne sont pas protégées.

## Principes réutilisables
- Couleurs de référence : bleu France `#000091`, rouge Marianne `#E1000F` (à ne pas recopier pour nous).
- Deux polices : Marianne (sans empattement) et Spectral (avec empattement).
- Espacement sur une base de **4 / 8 px** (unités « v »), grille à **12 colonnes**.
- Icônes **Remix Icon**, nommage des classes **BEM**.
- **Thème sombre** piloté par l'attribut `data-fr-scheme` (`system`, `light`, `dark`) : **suivre le système par défaut** est une bonne pratique.
- **RGAA** : le référentiel français d'accessibilité, qui reprend WCAG (voir REF-13).
