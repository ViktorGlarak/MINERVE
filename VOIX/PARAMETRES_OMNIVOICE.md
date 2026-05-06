# PARAMÈTRES OMNIVOICE — Référence complète
Source : capture ComfyUI OmniVoice + documentation interface

---

## Paramètres principaux

| Paramètre | Défaut | Plage | Description | Conseil |
|---|---|---|---|---|
| `steps` | 32 | 4-64 | Étapes de diffusion. 16=rapide, 32=équilibré, 64=meilleure qualité | Toujours 64 pour prod finale |
| `guidance_scale` | 2.0 | — | Guidage texte. Plus élevé = plus aligné au texte | 2.0-3.0 pour voix naturelle |
| `t_shift` | 0.10 | 0-1 | Décalage temporel. Petit = accent sur étapes précoces | 0.1 défaut suffisant |
| `speed` | 1.0 | 0.5-2.0 | Vitesse de parole. >1=plus rapide, <1=plus lent | 0.95 pour journaliste posée |
| `duration` | 0.0 | 0-60 | Durée fixe (secondes). Écrase speed. 0=auto | Laisser à 0 (auto) |
| `position_temperature` | 5.0 | 0-20 | Aléatoire position masque. 0=déterministe | 5.0 défaut OK |
| `class_temperature` | 0.0 | 0-5 | Aléatoire tokens. 0=déterministe, plus élevé=plus varié | 0.0 pour cohérence |
| `layer_penalty_factor` | 5.0 | 0-20 | Pénalité codebook profond | 5.0 défaut OK |
| `denoise` | true | — | Ajoute token débruitage. Voix plus propre | Toujours true |
| `preprocess_prompt` | true | — | Nettoie l'audio réf (silences, ponctuation) | Toujours true |
| `postprocess_output` | true | — | Supprime les silences longs en sortie | Toujours true |
| `keep_model_loaded` | false | — | Garde le modèle en RAM entre les runs | True si sessions intensives |

## Paramètre Longform TTS uniquement
| Paramètre | Défaut | Plage | Description |
|---|---|---|---|
| `words_per_chunk` | 100 | 0-500 | Mots par chunk. 0=pas de chunking. Découpe aux fins de phrase |

---

## Modèles Whisper ASR (transcription audio référence)

| Modèle | VRAM | Qualité |
|---|---|---|
| whisper-large-v3-turbo | ~1.5 GB | Très bonne + rapide ← **Recommandé** |
| whisper-large-v3 | ~3 GB | Meilleure qualité |
| whisper-medium | ~1.5 GB | Bonne |
| whisper-small | ~0.5 GB | Correcte |
| whisper-tiny | ~0.4 GB | Basique |

---

## Tags d'expression non-verbale
À insérer dans le texte entre crochets pour ajouter des nuances :

| Tag | Effet |
|---|---|
| `[laughter]` | Rire |
| `[sigh]` | Soupir |
| `[sniff]` | Reniflement |
| `[question-en]` | Intonation montante (EN) |
| `[question-oh]` | Question surprise |
| `[question-ch]` | Question (dialecte) |
| `[question-ei]` | Question (dialecte) |
| `[surprise-ah]` | Surprise légère |
| `[surprise-oh]` | Surprise marquée |
| `[surprise-wa]` | Surprise forte |
| `[surprise-yo]` | Surprise exclamative |
| `[dissatisfaction-hm]` | Mécontentement |
| `[confirmation-en]` | Acquiescement |

---

## Attributs Voice Design (mode sans audio référence)
Format : attributs séparés par des virgules dans le champ ref_text ou prompt

| Catégorie | Options disponibles |
|---|---|
| **Genre** | male, female |
| **Âge** | child, young, middle-aged, elderly |
| **Ton** | very low pitch, low pitch, medium pitch, high pitch, very high pitch |
| **Style** | whisper |
| **Accent anglais** | american accent, british accent, australian accent, canadian accent, indian accent, irish accent, scottish accent, south african accent |

**Exemple :** `female, middle-aged, low pitch, british accent`
