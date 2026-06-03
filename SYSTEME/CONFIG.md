# CONFIG — Paramètres du système Mercure

## Environnement
- **OS :** Windows 11 Pro
- **Ollama :** localhost:11434
- **Interface principale :** Claude Code (VSCode)
- **Interface directe agents :** Continue (VSCode)

## Modèles installés

> **Le registre des agents (qui utilise quel modèle) est dans `CLAUDE.md` — source unique.** Ici, uniquement l'infra : taille des modèles et statut. Pour savoir quels agents tournent sur un modèle, voir la colonne *Modèle* du registre CLAUDE.md. Deux agents sur le même modèle sont **co-résidents en VRAM** (un seul chargement partagé).

| Modèle | Taille | Statut | Usage |
|---|---|---|---|
| qwen2.5-coder:14b | 9 GB | Installé | Agent code (cf. registre) |
| deepseek-r1:14b | 9 GB | Installé | Raisonnement (PENSEUR) + analystes pays + **BROUILLON** (cf. registre) |
| mistral-nemo:latest | 7.1 GB | Installé | Rédaction FR + scénario + RS (cf. registre) |
| llama3.1:8b | 4.9 GB | Installé | Tâches rapides + prompts image/vidéo + BDA (cf. registre) |
| Claude (cloud) — claude-opus-4-7 | — | Actif (API, pas d'Ollama) | NOYAU + agents éditoriaux/doctrine (cf. registre) |
| nomic-embed-text | 274 MB | Installé | Embedding (RAG futur — utilitaire, non-agent) |
| qwen2.5-coder:1.5b | 986 MB | Installé | Autocomplete Continue (utilitaire, non-agent) |

## Outils de génération image/vidéo
| Outil | Type | Accès | Priorité |
|---|---|---|---|
| Adobe Firefly | Image | Licence Adobe | 1er choix |
| Flow (Google) | Image | Gratuit | 2ème choix |
| Gemini | Image | Gratuit | 3ème choix |
| ComfyUI + LTX 2.3 | Vidéo i2v | Local (standalone) | Unique outil vidéo |
| Adobe Premiere Pro | Montage | Licence Adobe | Assemblage final |

## Workflow vidéo validé
Image (Firefly/Flow/Gemini) → Animation LTX i2v → Overlays Premiere Pro → Export

## Répertoire Mercure
`D:\CECPC\PRODUCTION\IA\Mercure`

## Prochaines étapes prévues
- [ ] Niveau 2 : Script Python orchestrateur autonome (sans Claude)
- [ ] Intégration nomic-embed pour recherche dans les mémoires (RAG)
- [ ] Construction du dataset CONVERGENCE pour fine-tuning futur
