---
name: minerve-local-rag
description: "MINERVE Local (RAG consultation lecture seule, Ollama) — CODE PRÊT, indexation à lancer (1 commande). En pause 2026-06-28."
metadata: 
  node_type: memory
  type: project
  originSessionId: 4377e89f-f0dd-40af-851d-ddfb523fd276
---

**MINERVE Local** = assistant conversationnel local (Ollama) en parallèle de MINERVE-Claude (VSCode = conception). Discuté le 2026-06-28, **EN PAUSE** (phase dialogue, rien codé). Détail complet : note vault `vault/decisions/DECISION-011.md`.

**Décisions figées :**
- **Rôle = CONSULTATION SEULE / lecture stricte** : répond aux questions (countrybooks, profils, LO, injects GUILLAUME 2BB / MINAUTORE 7BB) ; **ne crée/modifie/ajoute JAMAIS** rien. Claude reste le seul qui écrit.
- **Accès uniquement via Ollama** (séparation nette d'avec Claude/VSCode).
- **Techno = RAG local** : Ollama (LLM + embeddings) + couche de récupération. Répondeur = **mistral-nemo** (FR). Embeddings = viser **bge-m3** (multilingue) plutôt que nomic-embed-text. Interface = **chat terminal minimal** d'abord (Open WebUI plus tard).
- **Corpus = tout `IA\MINERVE`** ; **citations obligatoires** (fichier source).

**⚠⚠ Règle fiches bio (NON NÉGOCIABLE) :** l'IA LOCALE peut indexer `D:\CECPC\DOC REF\MERCURE\RENS\01_Fiches bio` (hors-ligne, autorisé), **mais MOI (Claude) JAMAIS** — ni le contenu, ni les chunks dérivés. **Ségrégation** : collection séparée `fiches_bio/` que je n'ouvre jamais ; j'écris le code générique, **l'utilisateur lance** cette indexation, le magasin sensible reste hors de ma portée. Voir [[feedback_dossier_interdit_fiches_bio]].

**État 2026-06-28 :** CODE CONSTRUIT — `MINERVE_LOCAL/minerve_local.py` (index+chat, lecture seule, citations) + README ; plomberie Ollama validée. ⚠ **bge-m3 trop lent ici (~2,2 s/embed)** → script basculé sur **nomic-embed-text**. Pas encore d'index. **Reprise = 1 commande** : `python minerve_local.py index` (~2-3 min) puis `... chat`. Détail : `vault/decisions/DECISION-011.md`. Voir aussi [[project_mercure]], [[expert_influence]], [[analyste_mercure_storm1516]].
