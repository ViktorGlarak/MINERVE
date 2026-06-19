---
id: TOOL-012
type: tool
title: Store baked articles (MASTAURIGE_ARTICLES) + type courrier — récup injets 2BB→7BB
tags: [mastaurige, melmil, articles, courrier, recup, baked]
source: ../../MASTAURIGE/MEMOIRE.md
linkedTo: [PROJ-AURIGE-7BB, LESSON-016]
relevantFor: [mastaurige, minautore]
tier: 2
created: 2026-06-20
updated: 2026-06-20
---

# TOOL-012 — Store baked articles + type courrier

## Rôle
Persister des **articles/courriers sur disque** (avant, seuls les tweets avaient un store baked `MASTAURIGE_TWEETS`). Permet de rapatrier les injets éditoriaux de GUILLAUME (2BB) vers MINOTAURE (7BB) sans dépendre du localStorage.

## Mécanique
- **`moteur/articles_data.js`** (NOUVEAU) : `var MASTAURIGE_ARTICLES = [...]` (champ `origin:"baked"`), chargé par `index_master.html` ET `MELMIL/melmil_ili.html` (avant `articles.js`/`melmil.js`).
- **`moteur/articles.js`** : `baseline()` lit `window.MASTAURIGE_ARTICLES` ; `merged()` = baked ∪ localStorage (un item LS de même `id` surcharge) ; `effective/deleted/get/remove/update/restore` gèrent les bakés.
- **`MELMIL/melmil.js` → `buildAutoBridge()`** : boucle `MASTAURIGE_ARTICLES` (bloc « 1b »), lit **`a.type||'article'`** → les **courriers** (type `courrier`) s'affichent avec leur point vert.
- **Type courrier** : site `courrier` ajouté à `articles.js` SITES (code COU, folder `COURRIERS`). Courriers/articles riches = `external:true`, .html **copié-adapté** dans `Sites/<dossier>/`.

## Usage (récup d'une liste 2BB→7BB)
- Générateur type : `D:\CECPC\_cbtmp\gen_hn_bake.py` / `gen_lo5_bake.py` — **mode FUSION** (lit l'existant, append, dédup par `num`). Adaptation systématique DAC→ARN, Dacia Romania→Arnland, Bella Channel 1→Bothnia Channel 1, Polish→coalition (casse titre ET MAJUSCULES). Date = melmil si card socle existe, sinon jour du fichier.
- **À porter dans la vierge en fin de MINAUTORE.**

## 🔗 Source de vérité
Détail : `MASTAURIGE/MEMOIRE.md` [2026-06-19 / 2026-06-20]. Voir aussi [[LESSON-016]] (instance collab). **Pointeur, pas copie.**
