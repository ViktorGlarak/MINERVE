---
name: project-mercure
description: "Système MINERVE — assistant multi-agents pour production d'exercices militaires de crise. Architecture, chemin, agents, règles de cohérence."
metadata: 
  node_type: memory
  type: project
  originSessionId: 73fcca0d-c040-42d3-9859-fa36df54c216
---

Système MINERVE est un assistant multi-agents IA local (Ollama) orchestré par Claude (NOYAU), dédié à la production de contenus médias pour exercices militaires/civils de gestion de crise (CECPC).

**Chemin racine :** `D:\CECPC\PRODUCTION\IA\MINERVE\`

**Why:** Le dossier a été renommé de BDA\Mercure vers IA\MINERVE — toujours vérifier ce chemin si des références semblent incorrectes.

**How to apply:** Avant toute session, le CLAUDE.md à la racine du projet est la source de vérité absolue. Y référer pour les chemins, la liste des agents, et les checklists de mise à jour.

## Agents (18 au total — registre canonique dans CLAUDE.md)
- NOYAU = Claude (orchestrateur)
- ARCHITECTE = qwen2.5-coder:14b (code)
- PENSEUR = deepseek-r1:14b (raisonnement)
- SECRÉTAIRE = mistral-nemo (rédaction FR)
- ÉCLAIREUR = llama3.1:8b (tâches rapides)
- IMAGIER = llama3.1:8b (prompts image)
- CINÉASTE = llama3.1:8b (prompts vidéo LTX)
- SCÉNARISTE = mistral-nemo (contenu scénario)
- VOIX = mistral-nemo (OmniVoice TTS)
- ARCHIVISTE = llama3.1:8b (BDA assets)
- ANALYSTE = deepseek-r1:14b (expert République de Mercure)
- ANALYSTE_ARN = deepseek-r1:14b (expert Arnland / Dacie Romanie)
- ANALYSTE_RB = deepseek-r1:14b (expert Ruthnia Bella — Youkachenko, opposition, BC1)
- MASTODONTE = mistral-nemo (Mastodon / RS fictifs)
- MASTAURIGE = mistral-nemo (contenus RS exercices AURIGE, tweet cards)
- GUILLAUME = Claude cloud opus-4-7 (chef d'orchestre éditorial AURIGE 2BB)
- EXPERT_INFLUENCE = Claude cloud opus-4-7 (doctrine ILI, synchromatrice — transversal)
- MINAUTORE = Claude cloud opus-4-7 (chef d'orchestre éditorial AURIGE 7BB)

> ⚠ Le registre des agents est dupliqué dans 6 fichiers (CLAUDE.md, CONFIG.md, ROUTAGE.md, DOSSIER_POSTE.md, NOYAU/MEMOIRE.md, ici) — source récurrente de dérive. CLAUDE.md fait foi.

## Chemins permanents distincts du chemin racine
- BDA (bibliothèque d'assets) : `D:\CECPC\PRODUCTION\BDA\` — chemin correct, ne pas confondre avec le chemin du système MINERVE
- Exercices : `D:\CECPC\PRODUCTION\EXER\`
