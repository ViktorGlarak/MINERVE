---
name: charte-tv4-media
description: "Charte graphique complète du site média fictif \"TV4 International\" — à réutiliser pour toute page web simulant ce média occidental lié à Dacia Romania"
metadata: 
  node_type: memory
  type: reference
  originSessionId: 73fcca0d-c040-42d3-9859-fa36df54c216
---

# Charte graphique — TV4 International

**Fichier de référence :** `D:\CECPC\PRODUCTION\EXER\AURIGE 2BB\GUILLAUME\TV4_Article_Pallesson.html`
**Type :** Chaîne d'information indépendante, style médias occidentaux (Euronews, TV4 suédoise)
**Langue :** Anglais principal (EN / FR / DR)
**Camp narratif :** Occidental / neutre-favorable Dacia Romania — opposé à BC1 (pro-Mercure)
**Usage :** Média fictif couvrant la DR et l'OTAN dans les exercices AURIGE / ORION

---

## Identité visuelle

### Logo TV4
- Deux blocs jointifs : orange | blanc+bordure orange
- Gauche : fond orange `#F5A800`, texte "TV" bleu `#5599CC`, italic bold Arial Black
- Droite : fond blanc, texte "4" bleu `#5599CC`, bordure 3px orange, italic bold Arial Black
- Dimensions header : font-size 28px, padding 6px 10-12px
- **Pas d'espace entre les deux blocs** — border-left: none sur le bloc droite

```html
<span class="tv4-left">TV</span><span class="tv4-right">4</span>
```

### Palette de couleurs
```css
--orange:       #F5A800;   /* logo bg, ticker, accents, border-left widgets */
--orange-dark:  #D4900A;   /* hover, kicker, feed-time, tags */
--orange-pale:  #FFF3D0;   /* tags bg, hero caption bg */
--blue:         #5599CC;   /* logo texte, liens, social */
--blue-dark:    #2D6EA0;   /* nav, widget-title, meta-source */
--blue-light:   #89BAE0;   /* accents légers */
--blue-pale:    #EBF4FB;   /* blockquote bg */
--ticker-grey:  #C5D0E2;   /* sub-ticker bg */
--dark:         #1A1A2A;   /* top-bar, ticker label, footer, address-speaker */
--off-white:    #F5F5F3;   /* body bg */
--light-grey:   #E2E2DE;   /* séparateurs, règles */
--mid-grey:     #B0B0AC;   /* texte secondaire */
--text:         #1A1A18;
--text-soft:    #555550;
```

---

## Structure de page

### 1. Top utility bar
- Fond : `--dark`, border-bottom 3px orange
- Gauche : date + ville + heure CET (pas MSK — occidental)
- Droite : sélecteur EN / FR / DR (EN actif = fond orange, texte dark)

### 2. Header
- Fond : **blanc** (≠ BC1 navy) + border-bottom 4px orange
- Box-shadow légère : `0 2px 8px rgba(0,0,0,0.08)`
- Layout : [logo TV4] [nom + sous-titre] [search + badge LIVE]
- Nom site : `TV4 International` — Source Serif 4, 20px, bold, dark
- Sous-titre : `Independent News · tv4international.dr`
- Search : fond off-white, bouton orange

### 3. Navigation
- Fond : `--blue-dark`
- Onglets : Home, News, World, Politics, Defence, Economy, Society, Live
- Actif : border-bottom 3px orange

### 4. Double ticker
- **Ticker principal** : fond orange, label fond dark + texte orange, texte dark bold — animation 50s
- **Sub-ticker** : fond `--ticker-grey`, texte dark centré — ligne fixe éditoriale de l'article

### 5. Grille contenu
```css
grid-template-columns: 1fr 310px;
gap: 26px;
max-width: 1200px;
```

---

## Article

### Hero image
```css
.article-hero { width:100%; overflow:hidden; line-height:0; border-bottom: 4px solid var(--orange); }
img { width:100%; height:auto; display:block; }
```
- Caption : fond `--orange-pale`, border-bottom `#E8D090`, italic 11px Source Serif 4

### En-tête
- **Kicker** : 10px, bold, 0.2em uppercase, `--orange-dark`
- **Headline** : Source Serif 4, 30px, bold, `--dark`, lh 1.18
- **Deck** : Source Serif 4, 16px, italic, text-soft, border-left 4px **orange** (≠ BC1 rouge)
- **Blockquote** : fond `--blue-pale`, border-left 4px **blue** (≠ BC1 rouge), italic 16.5px, `--blue-dark`
- **Boutons sociaux** : Twitter + Facebook (≠ BC1 qui a VK + Telegram)

### Bloc discours complet
- `.address-label` : 10px uppercase, border-top 3px orange, couleur `--orange-dark`
- `.address-speaker` : fond dark, texte orange (nom) + blanc atténué (titre) — logo TV4 mini à droite
- `.address-box` : border 1px light-grey, padding 20px 24px, font 15px lh 1.82
- `.para-break` : `<hr>` border-top 1px light-grey, margin 18px 0 — séparateur de blocs discours
- `.closing` : Source Sans 3, 17px, 900, uppercase, centré, `--blue-dark`, border-top 3px orange

---

## Sidebar

### Widget-title
- Fond `--blue-dark`, texte blanc, **border-left 4px orange** (signature TV4)

### Feed-time
- Couleur `--orange-dark` (≠ BC1 rouge)

### Tags article
- Fond `--orange-pale`, border `#E8D090`, texte `--orange-dark`
- Hover : fond orange, texte blanc

---

## Footer
- Fond `--dark`, border-top 4px orange
- Logo TV4 mini (font-size 20px)
- Liens hover → couleur orange

---

## Typographies
| Usage | Police | Notes |
|---|---|---|
| Headline, deck, corps, blockquote | Source Serif 4 | 15–30px, 400/600/700 |
| Nav, meta, tags, UI, kicker | Source Sans 3 | 10–15px, 400/700/900 |
| Logo TV4 | Arial Black / Impact | italic, 900 |

---

## Règles éditoriales fictives

- **Ton** : occidental indépendant, factuel, favorable à DR et OTAN (opposé à BC1)
- **Langue** : anglais principal, sélecteur EN/FR/DR
- **Boutons sociaux** : Twitter + Facebook (médias occidentaux — pas VK/Telegram)
- **Fuseau** : CET (Central European Time — DR est en Europe)
- **Domaine fictif** : `tv4international.dr`
- **Lien BC1** : dans les articles TV4, Bella Channel 1 peut être cité comme "pro-Mercure state media"

## Différenciateurs TV4 vs BC1

| Élément | TV4 | BC1 |
|---|---|---|
| Couleur dominante | Orange + bleu ciel | Navy + rouge |
| Header fond | Blanc | Navy foncé |
| Logo | TV orange + 4 blanc | BC navy + 1 rouge |
| Blockquote | Fond bleu pâle, bordure bleue | Fond gris, bordure rouge |
| Boutons sociaux | Twitter, Facebook | VK, Telegram |
| Fuseau | CET | MSK |
| Ton éditorial | Occidental / pro-DR | Étatique / pro-Mercure |
| Ticker principal | Orange | Rouge |

**Lié à :** [[charte-bc1-media]] [[aurige-guillaume]] [[chartes-documents-a4]]
