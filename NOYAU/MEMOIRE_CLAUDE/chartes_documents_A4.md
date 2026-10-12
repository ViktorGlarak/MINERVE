---
name: chartes-documents-a4
description: Chartes graphiques des documents officiels A4 créés pour AURIGE 2BB — à réutiliser pour chaque nouvel exercice ou personnage
metadata: 
  node_type: memory
  type: reference
  originSessionId: 73fcca0d-c040-42d3-9859-fa36df54c216
---

# Chartes graphiques — Documents officiels A4

Chaque charte est liée à un camp narratif / pays fictif ou réel. La réutiliser pour tout nouveau personnage du même camp garantit la cohérence visuelle.

---

## MERCURE — Charte "République autoritaire soviétique"
**Fichier référence :** `D:\CECPC\PRODUCTION\EXER\AURIGE 2BB\GUILLAUME\Olamao_Declaration_Officielle.html`
**Personnages concernés :** Olamao, Junker, Stoph, Ribiki, tout officiel mercurien

### Palette
```css
--red:        #861729;
--red-dark:   #5C0F1C;
--red-light:  #A01E33;
--cream-dark: #C8BF98;
--cream-light:#F0EAD2;
--black:      #0D0D0D;
--gold:       #B8933A;
```

### Structure de page
- `display: flex; flex-direction: column`
- **Panneaux latéraux :** 18mm rouge plein des deux côtés (`panel-left` / `panel-right`), filet or `1.5px opacity 0.55`
- **Fond page :** crème parchmin `#F0EAD2`
- **Fond body :** quasi-noir `#1A1A1A`

### Header (page 1)
- Gradient rouge centré (`red-dark → red → red-light`)
- Filigrane étoile SVG (opacité 0.032)
- Étoile SVG noire 5 branches centrée au-dessus du titre
- `republic-name` : Playfair Display 20pt, 900, letter-spacing 0.16em, crème
- `republic-sub` : EB Garamond 8pt, 0.2em, crème atténué
- Règle dorée (`header-rule`) en dessous
- Barre de classif noire : "Official Document — Presidential Use Only"

### Mini-header (page 2)
- Gradient rouge + règle dorée en dessous
- `m-name` gauche / `m-page` droite

### Typographie spéciale
- `.punch` : font-weight 600, 11pt, indent 5mm
- `.impact` : Playfair Display 12pt, bold, centré, rouge foncé
- `hr` : rouge, opacity 0.28

### Footer
- Bordure rouge 2px en haut
- Gauche : adresse institution | Centre : étoile SVG | Droite : nom + titre + tampon "OFFICIAL" (rotate -4deg, rouge)

### Impression
- Marges : None | Background graphics : ✅

---

## DACIE ROMANIE — Charte "Démocratie occidentale, identité nordique"
**Fichier référence :** `D:\CECPC\PRODUCTION\EXER\AURIGE 2BB\GUILLAUME\Pallesson_Declaration_Officielle.html`
**Personnages concernés :** Pallesson, ministres DR, officiels Dacie Romanie

### Palette
```css
--navy:        #1B4672;
--blue:        #2E6AB5;
--blue-light:  #5B8DC9;
--blue-pale:   #EDF3FB;
--orange:      #C44200;   /* couleur de la croix nordique */
--white:       #FFFFFF;
--paper:       #F8FAFD;
--text:        #1A2535;
--text-soft:   #4A5568;
--rule:        #C8D8E8;
```

### Structure de page
- `display: flex; flex-direction: column`
- **Aucun panneau latéral**
- **Bande drapeau horizontale en haut :** 3 sections flex (bleu | orange cross | bleu), proportions 5:2:7
  - Page 1 : 7mm | Page 2 : 4mm
- **Fond page :** blanc institutionnel `#F8FAFD`
- **Fond body :** ardoise bleue `#3A4558`

### Header (page 1)
- Fond blanc, layout 3 colonnes : [drapeau SVG] [identité] [référence DR/PC/2026]
- Règle rouge-orange 1.5px en bas + status line bleu pâle
- `republic-name` : Playfair Display 16pt, 700, navy, letter-spacing 0.09em
- Drapeau SVG : croix nordique (bleu fond + or bordure + rouge-orange)

### Mini-header (page 2)
- Fond blanc, règle `--rule` en bas
- `m-name` bleu gauche / `m-page` droite

### Typographie spéciale
- `.section-label` : Playfair 7pt, bold, 0.28em, bleu, border-bottom 1px rule — **sépare les adressages**
- `.accusation` : Playfair 10.5pt, bold, orange (couleur croix)
- `.final` : Playfair 12.5pt, 900, navy, majuscules, centré — "Dacia Romania endures."
- `hr` : bleu pâle, opacity 0.2

### Footer
- Règle `--rule` 1.5px en haut
- Gauche : adresse | Centre : drapeau SVG (opacity 0.25) | Droite : nom + titre
- **Pas de tampon**

### Impression
- Marges : None | Background graphics : ✅

---

## BIÉLORUSSIE — Charte "Régime autoritaire slave, identité nationale biélorusse"
**Fichier référence :** `D:\CECPC\PRODUCTION\EXER\AURIGE 2BB\GUILLAUME\Loukachenko_Declaration_Officielle.html`
**Personnages concernés :** Loukachenko, officiels biélorusses

### Palette
```css
--red:         #CC0000;   /* rouge drapeau Belarus */
--red-dark:    #990000;
--green:       #1A7F37;   /* vert drapeau Belarus */
--green-dark:  #125A27;
--green-light: #28A045;
--white:       #FFFFFF;
--paper:       #F7F7F5;
--text:        #1A1A1A;
--text-soft:   #4A4A4A;
--rule:        #D0D0D0;
```

### Structure de page
- `display: flex; flex-direction: row` — layout horizontal : rushnik | contenu
- **Panneau gauche unique :** 18mm, motif rushnik (diamants rouges sur blanc), SVG data-URI, `background-size: 9mm 9mm`, bordure droite rouge 3px
- **Fond page :** blanc cassé neutre `#F7F7F5`
- **Fond body :** sombre neutre `#2A2A2A`

### Header (page 1)
- Gradient vert (`green-dark → green → green-light`)
- Layout 3 colonnes : [drapeau Belarus SVG] [identité] [référence BY/PR/2026]
- Règle rouge 3px + règle verte 1px sous le header
- Status bar vert pâle en dessous
- `republic-name` : Playfair Display 15pt, 700, blanc, letter-spacing 0.1em
- Drapeau SVG : rouge 2/3 + vert 1/3 + rushnik blanc-rouge sur gauche

### Mini-header (page 2)
- Gradient vert + bordure rouge 2px en bas
- `m-name` blanc gauche / `m-page` atténué droite

### Typographie spéciale
- `.citation` : italic, border-left 3px rouge, background rouge 3% — **citation Olamao obligatoire**
- `.solo` : Playfair 10pt, bold, centré, vert foncé — ex : "We are not surprised."
- `.door-open` : Playfair 12pt, bold, centré, vert — "The door is open."
- `.final` : Playfair 10.5pt, bold, centré, rouge — "But it will not stay open forever."
- `hr` : `--rule`, neutre

### Footer
- Bordure rouge 2px en haut
- Gauche : adresse | Centre : drapeau SVG (opacity 0.2) | Droite : nom + titre
- **Pas de tampon**

### Impression
- Marges : None | Background graphics : ✅

---

## Règles communes à tous les documents

- **Format :** A4 (210mm × 297mm), 2 pages, `overflow: hidden`
- **Fonts :** Playfair Display + EB Garamond (Google Fonts)
- **Corps texte :** EB Garamond 10.4pt, line-height 1.68, justifié
- **Langue :** anglais exclusivement
- **Print :** Chrome/Edge → Ctrl+P → PDF, marges : None, Background graphics : ✅
- **Nommage fichiers :** `[NOM]_Declaration_Officielle.html`

## Différenciateurs visuels par camp

| Élément clé | Mercure | Dacie Romanie | Biélorussie |
|---|---|---|---|
| Panneau latéral | Rouge plein ×2 | Aucun | Rushnik gauche ×1 |
| Couleur dominante | Rouge soviétique | Bleu démocratique | Vert Belarus |
| Motif identitaire | Étoile 5 branches | Croix nordique horizontale | Rushnik géométrique |
| Accent contrastant | Or | Rouge-orange | Rouge |
| Fond corps | Crème parchmin | Blanc pur | Blanc cassé neutre |
| Structure header | Centré monolithique | 3 colonnes horizontal | 3 colonnes horizontal |
| Registre graphique | Soviétique autoritaire | Occidental institutionnel | Slave autoritaire moderne |
