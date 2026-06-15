---
id: ARCH-006
type: architecture
title: Pipeline de production média (image → vidéo → voix → montage)
tags: [architecture, production, image, video, voix, pipeline]
source: ../../SYSTEME/DOSSIER_POSTE.md
linkedTo: [TOOL-008, TOOL-009, TOOL-010, LESSON-009, LESSON-010, LESSON-011, PROJ-PROD-MEDIA]
relevantFor: [production, assets]
tier: 2
created: 2026-06-15
updated: 2026-06-15
---

# ARCH-006 — Pipeline de production média

## Flux validé
1. **Image source** : Adobe Firefly (1er) → Flow Google (2e, texte dans l'image) → Gemini (3e). Voir [[TOOL-010]].
2. **Animation** : ComfyUI + LTX 2.3 (i2v, ou ia2v si piste audio). Voir [[TOOL-009]].
3. **Voix off** : OmniVoice TTS (Voice Clone / Design). Voir [[TOOL-008]].
4. **Montage** : Adobe Premiere Pro (overlays logos en mode Multiply, assemblage). Durée clip ia2v = durée exacte de l'audio.

## Agents concernés
IMAGIER (prompts image) · CINÉASTE (prompts LTX) · VOIX (OmniVoice) · ARCHIVISTE (BDA).

## Règles associées
Prompts image [[LESSON-009]] · texte TTS [[LESSON-010]] · prompts LTX [[LESSON-011]].

## 🔗 Source de vérité
[[../../SYSTEME/DOSSIER_POSTE.md]] §3/§5. Canvas : [[PROJ-PROD-MEDIA]].
