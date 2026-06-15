---
id: TOOL-008
type: tool
title: OmniVoice TTS (Voice Clone / Voice Design)
tags: [voix, tts, omnivoice, comfyui, whisper]
source: ../../VOIX/PARAMETRES_OMNIVOICE.md
linkedTo: [ARCH-006, LESSON-010]
relevantFor: [production, voix]
tier: 2
created: 2026-06-15
updated: 2026-06-15
---

# TOOL-008 — OmniVoice TTS

## Rôle
Génération / clonage de voix off, dans ComfyUI.

## Deux modes
- **Voice Clone** : depuis un audio de référence (nécessite Whisper ASR `openai/whisper-large-v3-turbo`).
- **Voice Design** : depuis attributs (genre, âge, ton, accent).

## Profils validés (réf.)
- Journaliste FR féminine : Voice Clone, steps=64, speed=0.95.
- Expert sécurité : Voice Design male/middle-aged/low pitch, steps=64, speed=0.90.
- Citoyen FR : Voice Design, steps=32, class_temperature=1.0.

## 🔗 Source de vérité
[[../../VOIX/PARAMETRES_OMNIVOICE.md]]. Préparation texte : [[LESSON-010]]. Pipeline : [[ARCH-006]].
