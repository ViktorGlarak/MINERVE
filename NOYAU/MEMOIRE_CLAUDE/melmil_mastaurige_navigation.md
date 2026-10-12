---
name: melmil-mastaurige-navigation
description: "Navigation MELMIL↔MASTAURIGE (2026-05-28) — popup click-to-card, highlightCardFromUrl, architecture incident/inject, ghost cards, sous-injects dans card parent"
metadata: 
  node_type: memory
  type: project
  originSessionId: 73fcca0d-c040-42d3-9859-fa36df54c216
---

## Navigation MELMIL → MASTAURIGE (ajouté 2026-05-28)

Cliquer sur un inject card dans `MELMIL_ILI_GUILLAUME.html` ouvre un popup listant les cards MASTAURIGE liées. Cliquer sur un bouton navigue vers `index_master.html?card=KEY` avec animation de ciblage (flash or + icône ▶).

**Fichier de données :** `MELMIL/melmil_inject_index.js` — `var MASTAURIGE_INDEX` — 27 entrées, types tweet/article/tract/courrier. Chargé AVANT `melmil.js`.

**Règle maintenance :** Toute nouvelle card dans index_master doit être ajoutée à `melmil_inject_index.js` si elle correspond à un inject MELMIL.

**Why:** L'animateur naviguait visuellement dans MELMIL sans pouvoir accéder directement aux cards associées dans MASTAURIGE — perte de temps en exercice.

**How to apply:** Quand on crée une nouvelle card dans index_master ET qu'elle couvre un inject MELMIL, ajouter `"XX.XX.XXi": [{key, type, label}]` dans melmil_inject_index.js.

---

## highlightCardFromUrl() — système de ciblage entrant (2026-05-28)

Fonction dans `index_master.html` qui lit `?card=KEY`, bascule l'onglet correct, réinitialise les filtres (TOUT / cumulatif), défile jusqu'à la card, applique 2 animations :
- `.melmil-link-highlight` : flash or 3× (2.7s)
- `.melmil-link-active` : icône ▶ rebondissante en marge gauche (10s ou jusqu'au clic)

**Centrage scroll :** `setTimeout(120ms)` indispensable avant `scrollIntoView()` — laisse le temps au navigateur de recalculer le layout après `filterArticles()`.

---

## Sticky headers — hiérarchie z-index (corrigé 2026-05-28)

```css
:root { --header-h: 57px; --cattabs-h: 62px; }
.g-header      { z-index: 120; top: 0; }
.cat-tabs      { z-index: 100; top: var(--header-h); }
.day-filter-bar{ z-index: 90;  top: calc(var(--header-h) + var(--cattabs-h)); }
```

**Why:** .g-header et .cat-tabs partageaient z-index:100 et top:0 → les onglets peignaient par-dessus le header, rendant les boutons MELMIL/ACTEURS inaccessibles en bas de page.

---

## Bouton "Afficher la classification" (déplacé 2026-05-28)

Désormais dans `.day-filter-bar` (barre jaune), extrême droite via `margin-left: auto`. Un seul bouton pour les deux onglets (media + social). Supprimer `max-width`/`margin: auto` de `.day-filter-inner` pour que le margin-left:auto fonctionne sur toute la largeur.

---

## Règle — Intégration images (double endroit)

Toute image disponible pour un inject doit être intégrée dans :
1. `index_master.html` card-thumb : `./images/FICHIER.jpg`
2. Article HTML hero section : `../images/FICHIER.jpg` (relatif depuis `Site Médias/`)

---

## Architecture MELMIL — Incident vs Injects (2026-05-28)

> **Règle canonique — tous agents.**

| Niveau | Code | Exemple | Rendu MELMIL |
|---|---|---|---|
| **Incident** | `XX.YY.ZZi` | `07.05.03i` | Card indépendante dans le tableau (vient du XLS) |
| **Inject** | `XX.YY.ZZAi`, `Bi`… | `07.05.03Ai` | Ligne compacte cliquable **à l'intérieur** de la card `07.05.03i` |

**Lettres libres :** Vérifier dans `melmil_data.js` avant d'assigner une lettre — si A est pris dans le XLS, utiliser B, etc.

**Comportement technique (`buildGhostInjects()` dans melmil.js) :**
- Si `XX.YY.ZZAi` a un parent `XX.YY.ZZi` dans MELMIL → rendu en `.inj-sub-item` à l'intérieur de la card parent. Cliquable → popup MASTAURIGE de l'inject.
- Si pas de parent dans MELMIL → ghost card standalone (bordure pointillée) si `MELMIL_EDITORIAL_DAYS` fournit un dayorder.

**`MELMIL_EDITORIAL_DAYS` :** Uniquement pour les ghosts standalone (sans parent MELMIL). Les sous-injects n'y sont PAS — ils suivent leur parent.

**Format d'affichage unifié (2026-05-28) :** Les petits dots sont remplacés. Toutes les cards MASTAURIGE (qu'elles soient incidents réguliers ou sous-injects) s'affichent dans le même format `[dot] [identifiant] [titre tronqué]` via `.inj-sub-list` / `.inj-sub-item`. Cliquer sur une ligne d'incident ouvre le popup de l'inject parent ; cliquer sur une ligne de sous-inject ouvre le popup du sous-inject spécifiquement.

---

## Règle — Vérification descriptions visuelles

Toujours ouvrir l'image avant de rédiger sa description. Chercher TOUTES les occurrences dans l'article (caption + deck + corps). Pour symboles identitaires (drapeaux) : formulation générique si doute.

**Why:** Erreur corrigée le 2026-05-28 — BCI_Article_Manifestations.html décrivait "drapeaux MER et RB" alors que l'image montrait le Pahonia (drapeau nationaliste biélorusse). 3 occurrences corrigées.
