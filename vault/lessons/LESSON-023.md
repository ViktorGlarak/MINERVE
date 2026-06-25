---
id: LESSON-023
type: lesson
title: Backreference \1 via bash dans une str de remplacement Python → octal \x01 (corrompt le fichier)
tags: [outillage, python, bash, injection, mastaurige, piege]
source: ../../MASTAURIGE/MEMOIRE.md
linkedTo: [TOOL-016, TOOL-004, PROJ-MASTAURIGE]
relevantFor: [mastaurige, outillage]
tier: 2
created: 2026-06-25
updated: 2026-06-25
---

# LESSON-023 — `\1` n'est pas un backreference dans une str Python normale (et bash aggrave)

## Symptôme
Après injection d'un flag `<script>` avant `<script src="bios.js">`, la **balise de chargement de bios.js a disparu** (remplacée par un caractère invisible) → `TROMBI_BIOS` undefined → EHO **vide**, cartes **non cliquables**.

## Cause racine
Injection faite en `python -c "...re.sub(r'(...)','...\\n\\1',...)"` **via bash** : `\\1` devient `\1` après bash, et `\1` dans une str Python **non-raw** = **octal `\x01`** (≠ backreference re.sub). Le groupe capturé a été remplacé par un octet de contrôle invisible → fichier corrompu.

## Règle
- Pour injecter du texte : préférer un **`.replace()` SIMPLE** (aucune regex, aucun groupe).
- Si un backreference Python est nécessaire : **raw-string** `r'...\1'` **ou** `\g<1>`, et **éviter bash** (écrire un script `.py` lancé en fichier).
- Garde-fou post-écriture : vérifier `'\x01' not in fichier`.
- ✅ `GENERER_KIT_JOUEURS.py` ([[TOOL-004]]) utilisait déjà `.replace()` simple → sain ; seule l'injection ad-hoc était fautive.

## 🔗 Source de vérité
Détail : `MASTAURIGE/MEMOIRE.md` (2026-06-25). **Pointeur, pas copie.**
