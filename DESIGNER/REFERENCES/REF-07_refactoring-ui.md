# REF-07 — Refactoring UI (Adam Wathan & Steve Schoger)

- **Source** : https://refactoringui.com. Livre de 218 pages par les créateurs de Tailwind CSS. **Payant** : seule la page de présentation publique a été ingérée.
- **Ingéré** : 2026-09-24. ⚠ **Ingestion partielle** : les tactiques ci-dessous sont celles que la page publique énumère. Le détail (exemples, valeurs) est dans le livre ; voir la question ouverte n°2 dans MEMOIRE.
- **Nature** : des **tactiques** de design visuel destinées aux développeurs. L'idée : pas besoin de talent artistique, il suffit d'appliquer des règles.

## Tactiques
**Démarrer**
- Commencer par **une fonctionnalité, pas par une mise en page**. Les détails viennent plus tard.
- **Choisir une personnalité** (sérieuse, chaleureuse, technique…) et s'y tenir.
- **Limiter les choix** : se donner à l'avance une échelle d'espacements, une échelle typographique et une palette déclinée en nuances.

**Hiérarchie**
- La **taille ne fait pas tout** : le poids et la couleur comptent autant.
- **Mettre en valeur en atténuant le reste**, au lieu de tout grossir.
- **Les étiquettes sont un dernier recours** : la forme doit suffire (« 12 cases remplies » plutôt que « Cases remplies : 12 »).
- **Hiérarchie visuelle ≠ hiérarchie du document** : un `h1` n'a pas à être énorme.
- **Pas de texte gris sur fond de couleur** : prendre une nuance du fond à la place.

**Mise en page et espacement**
- **Commencer avec trop d'espace**, puis resserrer.
- **Un système d'espacements**, pas des valeurs au hasard.
- **Ne pas remplir tout l'écran** : une largeur utile vaut mieux qu'un formulaire étiré sur 1 900 px.
- Les grilles sont surestimées : des colonnes fixes là où il le faut, fluides ailleurs.
- **Pas d'espacement ambigu** : l'écart **à l'intérieur** d'un groupe doit être nettement plus petit que l'écart **entre** les groupes.

**Texte**
- **Une échelle typographique**.
- Des polices de qualité, adaptées à leur rôle.
- Soigner la **longueur de ligne** (≈ 45 à 75 caractères).
- Aligner sur la **ligne de base** plutôt qu'au centre.
- **Interligne inversement proportionnel à la taille** : plus grand pour le texte courant, plus serré pour les gros titres.
- Un lien n'a pas forcément besoin de couleur quand le contexte suffit.

**Couleur**
- Raisonner en **HSL** (aujourd'hui plutôt **oklch**, voir REF-01).
- Prévoir **plus de nuances qu'on ne le pense** (9 à 10 par teinte), **définies à l'avance**.
- Des **gris légèrement teintés**, pas des gris neutres.
- Un contraste accessible peut rester élégant.
- **Ne jamais s'appuyer sur la couleur seule** pour transmettre une information.

**Profondeur**
- Une **source de lumière cohérente**.
- L'**ombre traduit l'élévation**. Les ombres en deux couches (une large et douce, une courte et nette) sont plus réalistes.
- Superposer des éléments crée de la profondeur, même en design plat.

**Finitions**
- Soigner les réglages par défaut (cases à cocher, listes).
- Des **bordures d'accent** ; des fonds discrètement décorés.
- **Prévoir les états vides** (première ouverture, aucun résultat).
- **Moins de bordures** : l'espacement, un fond différent ou une ombre séparent aussi bien.

---

## Complément du 2026-09-24 : chapitre gratuit « Building Your Color Palette »
- **Source** : https://www.refactoringui.com/previews/building-your-color-palette, chapitre offert par les auteurs. ⚠ Le reste du livre est **payant**. Aucune copie non autorisée n'a été cherchée ni utilisée. Leur article gratuit sur Medium (« 7 practical tips for cheating at design ») refuse la lecture automatique : à retenter.
- **Une palette complète comprend trois familles** :
  - **gris** : **8 à 10 nuances**, sans noir pur ; on part d'un gris foncé ;
  - **couleur principale** : 1 ou 2 teintes de **5 à 10 nuances** chacune, dont des très claires pour les fonds teintés et des foncées pour le texte ;
  - **couleurs d'accent** : rouge pour la suppression, jaune pour l'avertissement, vert pour le succès, avec plusieurs nuances chacune, à employer avec parcimonie.
- **Méthode pour construire l'échelle 100 → 900** :
  1. choisir la **base** (500), qui doit bien fonctionner comme fond de bouton ;
  2. fixer les **extrêmes** : 900 pour le texte, 100 pour les fonds teintés, en les essayant dans un vrai composant, une alerte par exemple ;
  3. placer d'abord **700 et 300**, puis combler les trous (800, 600, 400, 200).
- **« Faites confiance à vos yeux, pas aux chiffres »** : le système donne le cadre, l'œil ajuste.
