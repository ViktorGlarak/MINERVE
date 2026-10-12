---
name: methode-web-exercices
description: "Méthode complète de production de sites web fictifs pour exercices militaires (type AURIGE, ORION) — architecture, chartes, page mère, distribution offline"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 73fcca0d-c040-42d3-9859-fa36df54c216
---

# Méthode — Sites web fictifs pour exercices militaires

## Principe général

Pour chaque exercice, produire un **écosystème web fictif** composé de :
1. Des **sites médias** (1 par camp narratif) — chacun dans son dossier
2. Une **page mère agrégateur** (style Google News) listant tous les articles
3. Le tout dans un dossier `WEB/` **zippable et navigable offline**

**Why :** Le ZIP peut être distribué à n'importe quel participant sans serveur, sans internet, et permet de naviguer fictivement entre les médias comme dans un vrai exercice info-ops.

**How to apply :** Dès qu'un exercice produit plusieurs articles ou sites, appliquer cette architecture systématiquement.

---

## Architecture standard

```
WEB/
├── index.html                    ← Page mère (agrégateur, style Google News)
├── Site [Nom Média A]/
│   ├── article_01.html           ← HTML autonome (image Base64 intégrée)
│   ├── article_02.html
│   └── ...
├── Site [Nom Média B]/
│   ├── article_01.html
│   └── ...
└── (autant de sites que de camps narratifs)
```

---

## Règles de production

### Fichiers HTML
- **Bouton retour MASTAURIGE** : OBLIGATOIRE sur chaque article. Ne jamais créer le bouton en inline. Ajouter systématiquement avant `</body>` : `<script src="../shared/back-btn.js"></script>` — le JS crée automatiquement le bouton fixe en bas à gauche. **NE JAMAIS mettre `#backBtn{display:none;}` dans le CSS.**
- **Template complet obligatoire** : chaque site a son template de référence canonique. Ne JAMAIS créer un article avec un template simplifié (sans nav, sans breadcrumb, sans footer complet). Référence TV4 : `WEB/Site TV4/TV4_Article_Panique_01.html`. Constaté le 2026-05-29 : TV4_Article_SF_HCHATEAU_01 avait été créé avec template simplifié sans nav gauche, breadcrumb, more section, footer complet — corrigé.
- Toujours **autonomes** : images embarquées en Base64 (`certutil -encode` + injection PowerShell)
- Workflow Base64 :
  1. `certutil -encode image.jpg img_b64.txt`
  2. PowerShell : `(Get-Content img_b64.txt | Where-Object { $_ -notmatch "-----" }) -join ""`
  3. Injecter `data:image/jpeg;base64,[b64]` comme `src` de l'img
  4. `Remove-Item img_b64.txt`
- Taille finale typique : ~270 KB par article avec photo

### Page mère index.html
- Polices système uniquement (pas de CDN) → fonctionne **offline**
- Style Google News : cartes articles avec logo source, titre, extrait, date, miniature colorée
- Onglets de filtre par source (JavaScript vanilla)
- Recherche plein texte intégrée
- **Ajouter un article** = copier un bloc `.article-card` et adapter `data-source`, `href`, textes

### Distribution
- Zipper le dossier `WEB/` → clic droit → Compresser en ZIP
- Destinataire : extraire → ouvrir `index.html` → navigation complète offline
- ⚠️ Rappeler : ne pas ouvrir depuis l'intérieur du ZIP (les liens relatifs ne fonctionnent pas)

---

## Chartes graphiques par camp narratif

| Camp | Site fictif | Couleurs | Ton éditorial | Mémoire |
|---|---|---|---|---|
| Occidental / pro-DR / presse officielle DAC | TV4 International | Orange #F5A800 + Bleu #4A8FC2 | Neutre-favorable OTAN | [[charte-tv4-media]] |
| État biélorusse / pro-Mercure | Bella Channel 1 | Navy #12125A + Rouge #CC0000 | Étatique pro-Mercure | [[charte-bc1-media]] |
| (futur) Pro-Mercure direct | À créer selon exercice | — | — | — |

**Règle AURIGE 2BB :** TV4 = unique média de camp DAC/neutre pour tout l'exercice. Ne pas créer d'autre presse locale dacique — pour ne pas perdre les joueurs en entraînement.

### Différenciateurs visuels obligatoires entre médias opposés
- Header fond : blanc (occidental) vs navy (étatique)
- Langue : dropdown dans header (occidental) vs pills en top bar (étatique)
- Nav : verticale gauche (Ukrinform-style) vs horizontale (BBC-style) selon camp
- Social : Twitter/YouTube (occidental) vs VK/Telegram (pro-Mercure/Ruthnia Bella)
- Fuseau horaire : CET (occidental) vs MSK (pro-Mercure)
- Ticker : orange (TV4) vs rouge (BC1)

---

## Règles narratives globales (à adapter par exercice)

- **Géographie** : villes fictives préfixées H (HPARIS, HMARSEILLE) — cohérence countrybook
- **Nations fictives** : vérifier dans la mémoire ANALYSTE_ARN ou ANALYSTE avant d'écrire
- **Règle Belarus → Ruthnia Bella** (exercice AURIGE) : universelle dans tous les contenus
- Chaque camp a son vocabulaire propre — ne jamais mélanger les termes entre camps

---

## Application à AURIGE 2BB (référence)

- Dossier : `D:\CECPC\PRODUCTION\EXER\AURIGE 2BB\GUILLAUME\WEB\`
- Sites créés : TV4 International + Bella Channel 1
- Articles : Pallesson (TV4) + Loukachenko AppelPaix (BC1)
- Mémoire spécifique : [[web-architecture]] [[aurige-guillaume]]

**Lié à :** [[charte-tv4-media]] [[charte-bc1-media]] [[web-architecture]] [[aurige-guillaume]]
