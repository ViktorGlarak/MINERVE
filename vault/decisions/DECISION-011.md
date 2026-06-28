---
id: DECISION-011
aliases: ["DECISION-011"]
type: decision
title: MINERVE Local — assistant RAG de CONSULTATION (lecture seule, Ollama)
tags: [ia-locale, rag, ollama, consultation, mercure, influence]
source: "../../SYSTEME/CONFIG.md"
linkedTo: [PROJ-MINERVE, AGENT-ANALYSTE-MERCURE, AGENT-EXPERT-INFLUENCE, AGENT-PENSEUR]
relevantFor: [ia-locale, rag, consultation]
tier: 2
created: 2026-06-28
updated: 2026-06-28
---

# DECISION-011 — MINERVE Local (assistant RAG de consultation, lecture seule)

> 🟡 **STATUT : CODE PRÊT, INDEXATION À LANCER (en pause 2026-06-28).** Construit : `MINERVE_LOCAL/minerve_local.py` (RAG 100 % Ollama, `index`/`chat`, lecture seule, citations) + `README.md`. Plomberie validée (embed + chat mistral-nemo OK). ⚠ **bge-m3 trop lent sur ce poste (~2,2 s/embed → ~1 h pour 503 fichiers)** → script basculé sur **`nomic-embed-text`** (rapide ; bge-m3 gardé pour un ré-index « qualité » offline). **Reprise = 1 commande** : `python minerve_local.py index` (nomic, ~2-3 min) puis `python minerve_local.py chat`. Pas encore d'`index/public.pkl`.

## Contexte / problème
On veut un **MINERVE Local** qui tourne **sur ce poste, en parallèle** du MINERVE actuel (Claude/VSCode). Objectif : pouvoir **dialoguer pour consulter** tout le corpus construit (countrybooks Mercure/Arnland/Bothnia, doctrine ILI [[REF-storm1516]], mémoires agents, exercices [[AGENT-GUILLAUME]] 2BB & [[AGENT-MINAUTORE]] 7BB, [[PROJ-MINERVE]]) **sans dépenser de tokens Claude** et **hors-ligne**.

## Décision
- **Rôle = CONSULTATION SEULE (lecture stricte).** Il répond à des questions (countrybooks, profils, LO, injects d'exercice). Il **ne crée JAMAIS** de daily/note, **ne modifie ni n'ajoute AUCUNE donnée**. MINERVE-Claude reste le **seul** qui écrit.
- **Accès uniquement via Ollama** → séparation nette : Claude/VSCode = conception/optimisation ; Ollama = MINERVE Local de test.
- **Techno = RAG local** : Ollama (LLM + embeddings) + fine couche de récupération (Ollama seul ne fait pas le RAG).
  - **Modèle de réponse : `mistral-nemo`** (FR fluide ; installé). Upgrade possible plus tard : `qwen2.5:14b-instruct` / `mistral-small`.
  - **Embeddings : viser `bge-m3`** (multilingue, meilleur en FR) plutôt que `nomic-embed-text` (anglophone, installé).
- **Interface : 1ᵉʳ test = chat terminal minimal.** Plus tard : Open WebUI (chat web local) — décidé contre, pour l'instant.
- **Corpus = tout `IA\MINERVE`.** Citations **obligatoires** : il indique toujours le **fichier source** (contrôle anti-divergence).

## Pourquoi (alternatives écartées)
- **Modelfile Ollama doctrine baked** : corpus trop gros pour le system prompt → écarté.
- **Fine-tune (dataset CONVERGENCE)** : effort long, payoff différé → plus tard.
- **Open WebUI d'emblée** : repoussé — terminal d'abord pour tester vite et léger.
- **deepseek-r1:14b** comme répondeur : « pense » en anglais + `<think>` verbeux → moins bon pour de la **restitution FR propre** que mistral-nemo.

## Conséquences / à respecter
- ⚠⚠ **Fiches bio — règle de ségrégation NON NÉGOCIABLE.** Le dossier `D:\CECPC\DOC REF\MERCURE\RENS\01_Fiches bio` : **l'IA LOCALE y a accès** (hors-ligne, autorisé par l'utilisateur) **MAIS CLAUDE (moi, API/internet) N'Y ACCÈDE JAMAIS** — ni le contenu, ni les « chunks » texte qui en dérivent. **Indexation ségréguée** : ce dossier va dans une **collection séparée** (ex. `fiches_bio/`) que Claude **n'ouvre jamais** ; Claude écrit le **code générique** d'indexation, **l'utilisateur lance** l'indexation de cette collection, le magasin sensible reste **hors de portée de Claude**.
- **Fraîcheur** : ré-indexer périodiquement (script) — les mémoires évoluent côté Claude.
- **Limite connue** : un modèle ~14B local **n'égale pas Claude** — bon pour la **restitution** de faits indexés, faible pour la **synthèse croisée fine**.
- ✅ **Fait (2026-06-28)** : `MINERVE_LOCAL/minerve_local.py` (index+chat) + README ; `bge-m3` tiré ; corpus public indexé (`index/public.pkl`). **Reste** : (1) valider la qualité des réponses sur des requêtes types ; (2) l'**utilisateur** lance l'indexation `fiches_bio` ségréguée ; (3) upgrade éventuel (répondeur `mistral-small`, ou Open WebUI).

## 🔗 Source de vérité
Infra & roadmap : voir `source:` (`SYSTEME/CONFIG.md` § « Prochaines étapes » + « Modèles installés »). **Cette note ne recopie pas — elle pointe.**
