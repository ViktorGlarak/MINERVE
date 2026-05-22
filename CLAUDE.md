# CLAUDE.md — Source de vérité du système Mercure

> Ce fichier est **la référence canonique** du projet. Toute valeur définie ici prime sur les autres fichiers.
> Quand une information change ici, mettre à jour les fichiers listés dans la section correspondante.

---

## Chemin racine du projet

```
D:\CECPC\PRODUCTION\IA\Mercure\
```

**Fichiers à mettre à jour si ce chemin change :**
- `SYSTEME\CONFIG.md` — section "Répertoire Mercure"
- `SYSTEME\DOSSIER_POSTE.md` — section "7. SYSTÈME MERCURE"
- `.claude\settings.local.json` — toute permission contenant ce chemin

---

## Registre des agents (source de vérité)

| Agent | Modèle Ollama | Partage avec | Rôle |
|---|---|---|---|
| NOYAU | Claude (cloud) | — | Orchestrateur |
| ARCHITECTE | qwen2.5-coder:14b | — | Code & debug |
| PENSEUR | deepseek-r1:14b | ANALYSTE | Raisonnement complexe |
| SECRÉTAIRE | mistral-nemo:latest | SCÉNARISTE, VOIX | Rédaction FR |
| ÉCLAIREUR | llama3.1:8b | IMAGIER, CINÉASTE, ARCHIVISTE | Tâches rapides |
| IMAGIER | llama3.1:8b | ÉCLAIREUR, CINÉASTE, ARCHIVISTE | Prompts image |
| CINÉASTE | llama3.1:8b | ÉCLAIREUR, IMAGIER, ARCHIVISTE | Prompts vidéo LTX |
| SCÉNARISTE | mistral-nemo:latest | SECRÉTAIRE, VOIX | Contenu scénario |
| VOIX | mistral-nemo:latest | SECRÉTAIRE, SCÉNARISTE | Paramètres OmniVoice |
| ARCHIVISTE | llama3.1:8b | ÉCLAIREUR, IMAGIER, CINÉASTE | Gestion BDA |
| ANALYSTE | deepseek-r1:14b | PENSEUR | Expert République de Mercure |

**Fichiers à mettre à jour si un agent est ajouté, supprimé ou change de modèle :**
- `SYSTEME\CONFIG.md` — tableau "Modèles installés"
- `SYSTEME\ROUTAGE.md` — arbre de décision
- `NOYAU\MEMOIRE.md` — entrée "agents au total"
- `SYSTEME\DOSSIER_POSTE.md` — tableau "Modèles IA locaux (Ollama)"
- `SYSTEME\PROMPTS\` — créer ou supprimer le prompt système de l'agent
- Créer le dossier `NOM_AGENT\` avec `README.md` et `MEMOIRE.md`

---

## Chemins permanents (ne changent pas)

| Ressource | Chemin |
|---|---|
| Bibliothèque d'assets (BDA) | `D:\CECPC\PRODUCTION\BDA\` |
| Index BDA | `D:\CECPC\PRODUCTION\BDA\_CATALOGUE.md` |
| Exercice AURIGE 2BB | `D:\CECPC\PRODUCTION\EXER\AURIGE 2BB` |
| Exercice ORION 26 | `D:\CECPC\PRODUCTION\EXER\01 ORION 26` |
| ComfyUI | `C:\Users\MTR\Documents\ComfyUI_windows_portable\ComfyUI` |
| Whisper | `..\models\audio_encoders\openai_whisper-large-v3-turbo` |
| Continue config | `C:\Users\MTR\.continue\config.yaml` |

---

## Règles de cohérence — checklist à appliquer

### Quand un agent est ajouté
- [ ] Ajouter au registre ci-dessus
- [ ] `SYSTEME\CONFIG.md` — tableau modèles
- [ ] `SYSTEME\ROUTAGE.md` — arbre de décision
- [ ] `SYSTEME\DOSSIER_POSTE.md` — tableau modèles
- [ ] `NOYAU\MEMOIRE.md` — mettre à jour le compteur d'agents
- [ ] `SYSTEME\PROMPTS\nom_agent.md` — créer le prompt système
- [ ] `NOM_AGENT\README.md` et `NOM_AGENT\MEMOIRE.md` — créer les fichiers

### Quand le chemin racine change
- [ ] Mettre à jour ce fichier en premier
- [ ] `SYSTEME\CONFIG.md`
- [ ] `SYSTEME\DOSSIER_POSTE.md`
- [ ] `.claude\settings.local.json`
- [ ] Vérifier toutes les permissions avec `Grep("D:\\CECPC")`

### Après chaque session productive
- [ ] Mettre à jour `AGENT\MEMOIRE.md` des agents sollicités
- [ ] Mettre à jour `NOYAU\MEMOIRE.md` si nouveau pattern de routage appris
- [ ] Mettre à jour `SYSTEME\DOSSIER_POSTE.md` si nouvelle règle de production validée
- [ ] Mettre à jour `CONVERGENCE\SYNTHESE.md` si connaissance transversale dégagée
