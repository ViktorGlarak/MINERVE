---
id: LESSON-022
type: lesson
title: Obsidian — un chemin en code-span ne crée AUCUN lien de graphe ; utiliser des [[wikilinks]]
tags: [vault, obsidian, doctrine, expert-influence, liens]
source: ../../EXPERT_INFLUENCE/MEMOIRE.md
linkedTo: [AGENT-EXPERT-INFLUENCE]
relevantFor: [vault, expert-influence]
tier: 2
created: 2026-06-23
updated: 2026-06-23
---

# LESSON-022 — Code-span ≠ lien : relier les notes par wikilinks

## Symptôme observé
Dans Obsidian, les **livres de doctrine** d'EXPERT_INFLUENCE (Sun Tzu, Morelli, mentalité russe ILI, jus ad/in bello) apparaissaient **isolés** (« à part »), non reliés aux mémoires.

## Cause racine
Les livres étaient cités en **chemins entre backticks** (`` `REFERENCES/xxx.md` ``). Obsidian traite le contenu en **code** comme du texte inerte → **aucune arête de graphe**. Un lien md `[texte](chemin)` relie faiblement ; seul le **wikilink `[[nom]]`** (résolu par basename, peu importe le dossier) crée un vrai lien.

## Correctif / règle à appliquer
- Relier par **`[[basename]]`** (sans extension) : `[[art_de_la_guerre_suntzu]]`, `[[principes_propagande_morelli]]`, `[[mentalite_russe_ILI]]`, `[[jus_ad_bellum_jus_in_bello]]`.
- Ajouter une **section « Bibliothèque »** (en-tête mémoire) + un **footer « Voir aussi »** dans chaque fiche pour interconnecter le cluster.
- ⚠ **Pré-requis** : la racine du vault Obsidian doit **inclure** le dossier des notes (ici `EXPERT_INFLUENCE/`). Si Obsidian n'ouvre que `vault/`, les fiches hors `vault/` resteront hors graphe → il faudrait les déplacer/aliaser dans `vault/`.

## 🔗 Source de vérité
Détail : `EXPERT_INFLUENCE/MEMOIRE.md` (§ Bibliothèque doctrinale, 2026-06-23). **Pointeur, pas copie.**
