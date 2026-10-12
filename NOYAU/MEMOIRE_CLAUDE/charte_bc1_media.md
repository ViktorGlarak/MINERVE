---
name: charte-bc1-media
description: "Charte graphique complète du site média fictif \"Bella Channel 1\" (BC1) — à réutiliser pour toute page web simulant ce média d'État biélorusse"
metadata: 
  node_type: memory
  type: reference
  originSessionId: 73fcca0d-c040-42d3-9859-fa36df54c216
---

# Charte graphique — Bella Channel 1 (BC1)

**Fichier de référence :** `D:\CECPC\PRODUCTION\EXER\AURIGE 2BB\GUILLAUME\BCI_Article_Loukachenko.html`
**Type :** Site d'information d'État, style médias de l'Europe de l'Est (inspiré de news.by / Belarus 1)
**Langue :** Anglais (EN / RU / BY — sélecteur de langue en haut)
**Usage :** Média fictif biélorusse pro-Mercure dans les exercices AURIGE / ORION

---

## Identité visuelle

### Logo BC1
- Fond blanc, bordure 3px rouge `#CC0000`
- Dimensions : 62px × 50px (header) / 50px × 40px (footer)
- Texte : `BC` en navy `#12125A` + `1` en rouge `#CC0000`
- Police : Arial Black / Impact, font-weight 900, font-size 21px, letter-spacing -0.03em
- Rendu HTML :
```html
<span class="bc1-logo-text">BC<span class="one">1</span></span>
```

### Palette de couleurs
```css
--navy:       #12125A;   /* fond header, nav, widget-title, footer */
--navy-mid:   #1A1A7E;   /* nav secondaire, hover states */
--navy-light: #2A2A9A;   /* accents légers */
--red:        #CC0000;   /* logo "1", ticker, kicker, accent */
--red-dark:   #990000;   /* ticker-label, hover rouge */
--white:      #FFFFFF;
--off-white:  #F2F2F0;   /* fond body */
--light-grey: #E4E4E0;   /* séparateurs */
--mid-grey:   #B8B8B4;   /* texte secondaire */
--text:       #1A1A18;   /* corps texte */
--text-soft:  #555550;   /* métadonnées, captions */
--ticker-bg:  #0C0C46;   /* top-bar */
```

---

## Structure de page

### 1. Top utility bar
- Fond : `#0C0C46`, border-bottom rouge 0.4
- Gauche : date + ville + heure (MSK)
- Droite : sélecteur langue `EN | RU | BY` (EN actif = fond rouge)

### 2. Header
- Fond : `--navy`
- Layout 3 colonnes : [logo BC1] [nom + sous-titre] [search bar + badge LIVE]
- Nom site : `Bella Channel 1` — Source Serif 4, 24px, bold, blanc
- Sous-titre : `National Public Broadcasting · bellarussiachannel1.by` — 10px, uppercase, 0.2em, blanc 42%
- Badge LIVE : point rouge animé (blink 1.4s) + texte "Live coverage — Dacia Romania crisis"
- Search bar : input navy transparent + bouton rouge

### 3. Navigation
- Fond : `--navy-mid`
- Onglets : Home, Politics, World, Economy, Society, Defence, Sport, Culture, Live
- Actif : border-bottom 3px rouge
- Police : Source Sans 3, 12px, bold, 0.07em uppercase

### 4. Breaking news ticker
- Fond : `--red` (bande rouge pleine)
- Label gauche : fond `--red-dark`, point animé + "BREAKING" uppercase
- Texte défilant : animation `marquee` 45s linear infinite, `padding-left: 100%`
- `@keyframes marquee { 0% { transform: translate3d(0,0,0); } 100% { transform: translate3d(-100%,0,0); } }`

### 5. Contenu principal — grille 2 colonnes
```css
display: grid;
grid-template-columns: 1fr 310px;
gap: 26px;
max-width: 1200px;
margin: 26px auto;
padding: 0 20px;
```

---

## Article (colonne principale)

### Image hero
```css
.article-hero { width: 100%; overflow: hidden; line-height: 0; }
img { width: 100%; height: auto; display: block; }
```
- Caption en dessous : fond `#EEEEEA`, italic 11px, Source Serif 4

### En-tête article
- **Kicker** : 10px, bold, 0.2em uppercase, rouge — ex: "Politics · Dacia Romania Crisis"
- **Headline** : Source Serif 4, 30px, bold, navy, line-height 1.18
- **Deck** : Source Serif 4, 16px, italic, text-soft, border-left 3px rouge, padding-left 14px
- **Byline** : 11px, flex row — source | lieu | date | boutons sociaux (Share / VK / Telegram)

### Corps texte
- Police : Source Serif 4, 15px, line-height 1.78
- `<blockquote>` : fond `#F6F6F2`, border-left 4px rouge, italic 16.5px, navy — `<cite>` 10px uppercase
- `.transcript-label` : 10px uppercase rouge, border-top 2px navy
- `.transcript-box` : fond `#F4F4F0`, border 1px light-grey + border-left 3px mid-grey, italic 14px

### Tags
- Fond off-white, border 1px mid-grey, 10px uppercase, text-soft

---

## Sidebar (310px)

### Widget structure
- `.widget-title` : fond navy, blanc, 10px uppercase 0.2em
- `.widget-body` : padding 12px 14px

### Types de widgets utilisés
1. **Live Updates** — feed horodaté (heure rouge, texte 12px)
2. **Related Articles** — thumb gris 68×50 + catégorie rouge + titre Source Serif 4 13px navy + date
3. **On Air Now** — carte navy sombre + titre gros, "Next bulletin: XX:00 MSK"

---

## Footer
- Fond `--navy`
- Layout : [logo BC1 + nom] ← → [liens footer]
- Liens : 11px uppercase, blanc 48%, hover blanc 85%
- Copyright : 10px, blanc 28%, centré

---

## Typographies
| Usage | Police | Taille | Poids |
|---|---|---|---|
| Headline, deck, corps | Source Serif 4 | 15–30px | 400–700 |
| Nav, meta, tags, UI | Source Sans 3 | 10–15px | 400–700 |
| Logo BC1 | Arial Black / Impact | 21px | 900 |

Google Fonts : `Source+Serif+4` (ital, opsz, 400/600/700) + `Source+Sans+3` (400/600/700)

---

## Règles éditoriales fictives

- **Ton** : média d'État de Ruthnia Bella, neutre en apparence, légèrement pro-Mercure dans le choix des angles
- **Langue** : anglais (interface EN/RU/BY simulée)
- **Boutons sociaux** : Share, VK, Telegram (pas Twitter/X — cohérence géopolitique)
- **Horodatage** : fuseau MSK (Moscow Standard Time, UTC+3)
- **Lien domaine fictif** : `bellarussiachannel1.by`
- **Référence de style** : news.by / Belarus 1 — structure classique presse d'État ex-soviétique

## ⚠ RÈGLE ABSOLUE — "Ruthnia Bella" remplace "Belarus"

Dans TOUS les contenus liés à cet exercice (site BC1, discours, articles, documents) :
- `Belarus` → **`Ruthnia Bella`**
- `Belarusian` → **`Ruthnia Bellan`**
- `Republic of Belarus` → **`Republic of Ruthnia Bella`**
- `Belarusian Security Council` → **`Ruthnia Bellan Security Council`**

**Pourquoi :** Dans l'univers fictif de l'exercice, la Biélorussie réelle est remplacée par "Ruthnia Bella" — pays fictif. Ne jamais écrire "Belarus" dans un contenu de production.
**Concerne :** BCI article, documents officiels, discours Loukachenko, sidebar, footer, ticker, tags — absolument tout.

---

## Image autonome (portabilité)

Pour rendre un fichier HTML autonome (partageable sans fichier image externe) :
1. Convertir l'image avec `certutil -encode image.jpg img_b64.txt`
2. Lire le Base64 avec PowerShell : `Get-Content img_b64.txt | Where-Object { $_ -notmatch "-----" }` → `-join ""`
3. Injecter dans le HTML : `src="data:image/jpeg;base64,[b64]"`
4. Supprimer `img_b64.txt`

**Lié à :** [[chartes-documents-a4]] [[aurige-guillaume]]
