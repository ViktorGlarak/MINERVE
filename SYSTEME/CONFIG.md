# CONFIG — Paramètres du système Mercure

## Environnement
- **OS :** Windows 11 Pro
- **Ollama :** localhost:11434
- **Interface principale :** Claude Code (VSCode)
- **Interface directe agents :** Continue (VSCode)

## Modèles installés
| Agent | Modèle | Taille | Statut |
|---|---|---|---|
| NOYAU | Claude (cloud) | — | Actif |
| ARCHITECTE | qwen2.5-coder:14b | 9 GB | Installé |
| PENSEUR | deepseek-r1:14b | 9 GB | Installé |
| SECRÉTAIRE | mistral-nemo:latest | 7.1 GB | Installé |
| ÉCLAIREUR | llama3.1:8b | 4.9 GB | Installé |
| IMAGIER | llama3.1:8b | 4.9 GB | Installé (partage avec ÉCLAIREUR) |
| CINÉASTE | llama3.1:8b | 4.9 GB | Installé (partage avec ÉCLAIREUR) |
| SCÉNARISTE | mistral-nemo:latest | 7.1 GB | Installé (partage avec SECRÉTAIRE) |
| VOIX | mistral-nemo:latest | 7.1 GB | Installé (partage avec SCÉNARISTE) |
| ARCHIVISTE | llama3.1:8b | 4.9 GB | Installé (partage avec ÉCLAIREUR) |
| ANALYSTE | deepseek-r1:14b | 9 GB | Installé (partage avec PENSEUR) |
| Embedding | nomic-embed-text | 274 MB | Installé |
| Autocomplete | qwen2.5-coder:1.5b | 986 MB | Installé |

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
