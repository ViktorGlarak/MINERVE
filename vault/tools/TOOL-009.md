---
id: TOOL-009
type: tool
title: LTX 2.3 i2v/ia2v (ComfyUI)
tags: [video, ltx, comfyui, animation]
source: ../../CINEASTE/PARAMETRES_LTX.md
linkedTo: [ARCH-006, LESSON-011]
relevantFor: [production, video]
tier: 2
created: 2026-06-15
updated: 2026-06-15
---

# TOOL-009 — LTX 2.3 (ComfyUI)

## Rôle
Animation **image → vidéo** (i2v) ou **image + audio → vidéo** (ia2v, synchro labiale). Unique outil vidéo.

## Paramètres par défaut
- Standard : force=0.70, LoRA strength=0.50, fps=24.
- Talking head : force=0.65, LoRA=0.60.
- ia2v : durée du clip = durée exacte de l'audio.

## Règle
Logos / texte précis → **overlay Premiere Pro**, pas LTX.

## 🔗 Source de vérité
[[../../CINEASTE/PARAMETRES_LTX.md]]. Prompts : [[LESSON-011]]. Pipeline : [[ARCH-006]].
