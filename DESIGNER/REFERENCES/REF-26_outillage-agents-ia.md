# REF-26 — Outillage d'agents IA (RAG-Anything, UXAgent, Pydantic AI) — ⚠ HORS DOCTRINE

- **Fournis par l'utilisateur le** 2026-10-06, avec la question « est-ce utile ? ». **Réponse : ce ne sont pas des sources de design** ; ils servent à construire ou outiller des agents IA. Aucune règle du §3 n'en découle.
- **Lu** : README des trois dépôts ; pour UXAgent aussi la configuration, le code (`gpt.py`, `model.py`, `env.py`) et le résumé arXiv 2504.09407. Licences : **MIT** pour les trois.

| Outil | Ce que c'est | Hors ligne ? | Intérêt pour nous |
|---|---|---|---|
| **RAG-Anything** (HKUDS) | RAG multimodal (texte, images, tableaux) sur LightRAG | Oui en **Ollama** pour le texte (exemple fourni) ; la vision locale non vérifiée ; par défaut **OpenAI** | Aucun pour le design ; piste possible pour **MINERVE Local** (RAG en pause), Ollama seulement |
| **UXAgent** (neuhai) | Utilisateurs simulés par LLM qui naviguent via Playwright (personas, 50 étapes, questionnaire SUS, captures) | **Non prévu** : OpenAI, Bedrock ou Anthropic codés en dur ; adaptable à Ollama par modification du code | Seul intérêt de **méthode** (repérer où un utilisateur se perd) ; ⛔ envoie HTML, éléments cliquables, URL et captures au fournisseur → **avis CYBERSECU obligatoire**, seulement sur maquette aux données fictives ou modèle local ; ne remplace pas 5 vrais animateurs (REF-24) |
| **Pydantic AI** | Framework Python d'agents LLM typés | Oui (Ollama) ; ⛔ ne pas utiliser sa passerelle cloud ni la télémétrie externe | Aucun pour le design ; sujet d'outillage ARCHITECTE |

**Tension relevée** : NN/g fonde tout sur l'observation d'utilisateurs réels ; UXAgent les simule par LLM (réserve formulée par les 16 chercheurs de l'article lui-même).
