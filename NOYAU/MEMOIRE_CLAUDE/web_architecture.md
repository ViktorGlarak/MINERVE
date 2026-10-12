---
name: web-architecture
description: "Architecture du dossier WEB — agrégateur de news fictif multi-sites pour AURIGE 2BB, navigable offline, avec outils animateur index_master.html"
metadata: 
  node_type: memory
  type: project
  originSessionId: 73fcca0d-c040-42d3-9859-fa36df54c216
---

# Architecture WEB — AURIGE 2BB

**Chemin racine WEB :** `D:\CECPC\PRODUCTION\EXER\AURIGE 2BB\00_Boites à outils\MASTAURIGE\WEB\`

## Structure de dossiers

```
WEB/
├── index_master.html          ← FICHIER MAÎTRE ANIMATEUR (data-master="1") — NE PAS DISTRIBUER
├── images/
│   └── avatars tweet/         ← Avatars PNG pour tweet cards (initiales ou photo portrait)
├── MELMIL/                    ← MODULE MELMIL ILI (déplacé ici 2026-05-27, était dans 00_Boites à outils\MELMIL)
│   ├── MELMIL_ILI_GUILLAUME.html  ← Tableau des 45 injects D+31→D+40
│   ├── melmil.css / melmil.js     ← Styles + logique drag-and-drop + localStorage
│   ├── melmil_data.js             ← AUTO-GÉNÉRÉ — ne pas modifier
│   ├── MELMIL.xls                 ← Source de vérité (3 feuilles : Events, Incidents, Injections)
│   ├── generate_data.ps1          ← Lit MELMIL.xls → génère melmil_data.js
│   └── Actualiser_MELMIL.bat      ← Double-clic → lance le PS1
├── PS1/                       ← Scripts PowerShell génération ZIP stagiaires
│   ├── CREER_MEDIA_ZIP.ps1
│   ├── CREER_RZO_ZIP.ps1
│   └── CREER_COMPLET_ZIP.ps1
├── Site Today Mercure/        ← Articles TM_Article_*.html (camp rouge)
├── Site Bella Channel 1/ ← Articles BCI_Article_*.html (camp rouge/RB)
├── Site Hexagone/             ← Articles HEX_Article_*.html (camp bleu/presse FR fictive)
├── Site TV4/                  ← Articles TV4_Article_*.html (camp bleu/média occidental)
└── [autres sites à venir]
```

## index_master.html — fichier animateur

**Unique point d'entrée animateur.** Jamais distribué aux stagiaires. Détecté par `document.body.dataset.master === "1"`.

### Fonctions clés
| Fonction | Rôle |
|---|---|
| `filterArticles()` | Filtre les cards par onglet (média/RS), jour, mode cumul/exact, texte libre |
| `initStatusSelects()` | Crée le sélecteur statut par card (En cours / Finalisé / Envoyé) |
| `initDateTimeEditors()` | Crée l'éditeur Jour+Heure par card + regroupe tout dans `.card-right-panel` |
| `initClassifySidebars()` | Panneaux de classification camp (rouge/bleu/gris) — vue animateur |
| `initPublishToggles()` | Bascule publication par card |
| `updateCounts()` | Met à jour les compteurs onglets (MÉDIAS / RÉSEAUX SOCIAUX) |
| Generate (Split/Complet) | Exports stagiaires — suppriment tous les éléments animateur avant téléchargement |

### Panneau droit par card — `.card-right-panel` (depuis 2026-05-27)

Chaque card (article ET tweet) possède un panneau flottant absolu à droite, centré verticalement :
```css
.card-right-panel { position: absolute; left: calc(100% + 10px); top: 50%; transform: translateY(-50%); display: flex; flex-direction: column; gap: 8px; }
```

Contenu du panel (de haut en bas) :
1. **`.card-status-wrap`** — sélecteur ⬜ En cours / 🟠 Finalisé / ✅ Envoyé — persistance localStorage
2. **`.card-datetime-wrap`** — sélecteur Jour (26 Mai→04 Jun + **En attente**) + champ Heure — repositionne la card dans le DOM en temps réel

**Option "En attente" :** la card devient invisible dans les filtres de jours normaux — visible uniquement via le bouton orange "En attente" de la barre de filtres. Persistance localStorage (`card-attente-KEY`).

### sessionStorage — restauration état navigation
Avant chaque ouverture d'article, l'état complet est sauvegardé : onglet actif, jour, mode cumul/exact, recherche, scrollY, classification camps. Restauré automatiquement au retour (bouton précédent).

### Exports stagiaires — éléments supprimés
Les fonctions generate (Split médias / Split RS / Extraction complète) suppriment systématiquement : `.card-right-panel`, `.card-status-wrap`, `.card-datetime-wrap`, `.camp-badge`, `.classify-btn`, `.publish-toggle`, `.anim-icon-row`.

## Structure des cards

### Article card
```html
<div class="article-card" data-category="media" data-dayorder="31" onclick="openCard(this,'./Site X/Article.html')">
```
- `data-category` : `"media"` ou `"social"`
- `data-dayorder` : nombre 26-35 (jours de l'exercice) ou `"attente"`
- `onclick openCard` → sauvegarde sessionStorage → navigate vers l'article

### Tweet card
```html
<div class="article-card tweet-card" data-category="social" data-dayorder="31" onclick="markTweet(this,'@handle')">
```
- `onclick markTweet` → marque comme vu (localStorage), pas de navigation
- Avatar : initiales texte (ex: `EW`) ou `background: url('...') center/cover; color: transparent;` pour photo portrait

## Ajouter un nouvel inject

### Article HTML
1. Créer `Site [Canal]/[CODE]_Article_[Nom].html` (HTML autonome, Base64 pour images)
2. Ajouter un `.article-card` dans `index_master.html` : bloc HTML + entrée `ANIM_DATA` + entrée `LO_BY_KEY`
3. Respecter `data-dayorder` (numéro du jour D+ de l'exercice)

### Tweet card
1. Ajouter un `.article-card.tweet-card` dans `index_master.html`
2. Ajouter une entrée `ANIM_DATA` + `LO_BY_KEY` avec la clé `@handle`
3. Vérifier que l'avatar est dans `images/avatars tweet/`

## Sites médias actifs — AURIGE 2BB

| Site | Camp | Dossier | Préfixe fichier |
|---|---|---|---|
| Today Mercure | 🔴 Rouge | `Site Today Mercure/` | `TM_Article_` |
| Bella Channel 1 | 🔴 Rouge | `Site Bella Channel 1/` | `BCI_Article_` |
| HEXAGONE | 🔵 Bleu | `Site Hexagone/` | `HEX_Article_` |
| TV4 International | 🔵 Bleu | `Site TV4/` | `TV4_Article_` |

## Bouton MELMIL dans index_master.html (depuis 2026-05-27)

Un bouton **⚡ MELMIL ILI** (classe `.btn-melmil`, fond `#FFD700`, font 900 11px) est intégré dans le `<header>` entre la barre de recherche et le badge ANIMATEUR. Il ouvre `MELMIL/MELMIL_ILI_GUILLAUME.html` dans un nouvel onglet. Il est supprimé dans les 3 fonctions d'export (ajouté aux tableaux de nettoyage).

**Lié à :** [[charte-tv4-media]] [[charte-bc1-media]] [[aurige-guillaume]] [[mastaurige]]
