# Lecture du CODE SOURCE — Mem0

> Veille du 2026-10-12. Clone local `mem0ai/mem0` du 07/10/2026 (SDK 2.2.1 / TS 3.3.1, commit b7ad69a) ; `<R>` = racine. Complète REF-05. **Le code ne fonctionne plus comme le Mem0 des articles.**

## À savoir d'abord (« v3 », `docs/migration/oss-v2-to-v3.mdx`)
- Plus de `graph_memory.py`, ni `mem0/graphs`, ni `openmemory/`.
- **Extraction en une passe, ADD seul** : un seul appel LLM, **plus aucune décision UPDATE / DELETE**. Recherche hybride sémantique + BM25 + entités. La mémoire graphe est retirée de l'open source (plateforme payante). Gains annoncés : LoCoMo 71,4 → 91,6, LongMemEval 67,8 → 93,4, extraction ~2× plus rapide.
- Les anciens prompts FACT_RETRIEVAL et ADD/UPDATE/DELETE/NONE restent dans `prompts.py` mais ne sont plus importés (`main.py:19-24`) ; côté TS `getUpdateMemoryMessages` est importé sans être appelé.

## 1. Extraction des faits
**ADDITIVE_EXTRACTION_PROMPT (actif)**, `prompts.py:468-944` + `generate_additive_extraction_prompt` (l.1016-1062) : « You are a Memory Extractor — a precise, evidence-bound processor… Your sole operation is ADD ». Sections : Summary (jamais rempli en OSS), **Last k Messages** (10 derniers, tronqués à 300 caractères), Recently Extracted Memories, Existing Memories (top 10 par similarité), New Messages, **Observation Date**, Current Date, Custom Instructions.
Règles citées :
- **Ancrage temporel** : « CRITICAL: "User went to Paris last week" is useless 6 months later. "User went to Paris the week of May 15, 2023" is meaningful forever. » Les dates relatives se résolvent avec l'Observation Date, jamais la Current Date.
- **Mémoires riches** (15-80 mots) plutôt qu'atomiques : « Bad: "User has a dog" | Good: "User has a dog named Poppy and their morning walks together are the highlight of their day" ».
- **Transitions** (l.612-620) : « the memory MUST capture the transition — what the new state is AND what it replaces… Good: "User switched from almond milk to oat milk lattes after developing an almond sensitivity" … When the change is explicitly temporary or a trial, capture that too — "for a month", "trying out" — these signal the old arrangement may resume. »
- **Sens exact** : « "I used to love hiking" = no longer loves hiking ». « Misinterpreting… is worse than not extracting at all. »
- Intégrité : No Fabrication, **No Implicit Attribute Inference** (genre, âge), No Echo Extraction, **No Detail Contamination from Context** (ne pas injecter dans un nouveau fait un détail d'une mémoire existante).
- Liaison : `linked_memory_ids` si même entité, préférence modifiée, continuation ou **contradiction** ; « "User has a dog named Max" and "User went on a camping trip with Max…" are two distinct memories, not duplicates. »
- Exhaustivité : ≥ 10 messages → 5 à 15 mémoires, éviter la « first topic dominance » ; « When in doubt, extract. A slightly redundant memory is far less costly than a missing one. »
Sortie : `{"memory":[{"id","text","attributed_to":"user|assistant","linked_memory_ids":[…]}]}`. `AGENT_CONTEXT_SUFFIX` si portée agent (« Agent was informed that [fact] »).
**Ancien FACT_RETRIEVAL** (inutilisé) : 7 catégories, « Today's date is {date} », faits dans la langue de l'utilisateur ; variantes USER / AGENT (traits de personnalité de l'assistant).

## 2. Mise à jour (flux actif `_add_to_vector_store`, `main.py:881-1220`)
Clé de portée `user_id&agent_id&run_id` ; 10 derniers messages depuis SQLite ; embedding des nouveaux messages puis **top 10 mémoires existantes, aucun seuil** ; UUID remplacés par « 0 », « 1 »… (**anti-hallucination**) ; un appel LLM `json_object` (erreur = `LLMError`, jamais liste vide) ; **dédoublonnage par hash MD5 du texte exact seulement** (le sémantique est délégué au LLM) ; payload avec `text_lemmatized` (BM25), hash, dates, `attributed_to` ; historique event ADD. **Aucun UPDATE ni DELETE automatique** : les contradictions s'accumulent, formulées en transition, et le classement par date départage. **Bug** : `linked_memory_ids` jamais persistés.
**Ancien flux (inutilisé)** DEFAULT_UPDATE_MEMORY_PROMPT (`prompts.py:176-324`) : UPDATE = « keep the fact which has the most information » (fusion par réécriture, ID conservé) ; DELETE = « contradicts » (« Loves cheese pizza » + « Dislikes cheese pizza » → DELETE, le nouveau n'est pas ajouté dans l'exemple).
UPDATE / DELETE manuels (API) : `_update_memory` garde `created_at`, historique `prev → data` ; `_delete_memory` = **suppression physique** du vecteur, historique `DELETE` avec `is_deleted=1` et l'ancien texte.
**Table history** (SQLite `storage.py:102-126`) : `id, memory_id, old_memory, new_memory, event, created_at, updated_at, is_deleted, actor_id, role` ; table `messages` : 10 derniers par portée, purge à chaque sauvegarde.

## 3. « Graphe » = entity store par co-occurrence
Seconde collection vectorielle `<collection>_entities`. **Extraction d'entités SANS LLM** (`utils/entity_extraction.py`, spaCy ; TS : `compromise` + regex) : PROPER (NER, 0,95 ; suite de noms propres 0,8), IDENTIFIER (0,9), QUOTED (0,75), TOPIC (0,45) ; listes noires ; DATE / CARDINAL / MONEY rejetés. Liaison : texte exact normalisé puis cosinus **≥ 0,95** ; union des `linked_memory_ids`. **Pas de prompt de contradiction ni de suppression de relation** ; doc plateforme : « It does not assign typed, labeled relationships ». (Ancien Mem0, absent du clone : EXTRACT_RELATIONS triplets avec USER_ID, DELETE_RELATIONS « outdated / contradictory » mais « DO NOT DELETE if… same type of relationship but different destination nodes », Neo4j cosinus ~0,7.)

## 4. Niveaux user / agent / run, métadonnées
Au moins un identifiant obligatoire ; cloisonnement par la combinaison exacte ; les clés d'identité passées en `metadata` sont ignorées (sécurité) ; `actor_id` = `name` du message ; champs promus dans les résultats : `user_id, agent_id, run_id, actor_id, role, attributed_to, expiration_date`. **Mémoire procédurale** (`memory_type="procedural_memory"` + `agent_id`) = résumé intégral verbatim de l'historique d'exécution, une seule mémoire. `infer=False` = stockage brut sans LLM.

## 5. Stockage local et embeddings
Python : Qdrant embarqué (`/tmp/qdrant`, dim **1536**, `on_disk=False`), BM25 fastembed `Qdrant/bm25` (désactivé silencieusement sans fastembed), embedder OpenAI `text-embedding-3-small`, LLM `gpt-5-mini` ; **Ollama supporté** (`nomic-embed-text`, dim par défaut **512** ≠ 1536 du store : piège). TS (le plus proche de Node.js) : **SQLite via better-sqlite3**, cosinus en JS, `keywordSearch`, BM25 maison (k1 1,5, b 0,75), stemming Porter (`natural`).

## 6. Recherche, résumé, importance, décroissance, oubli
- Score hybride (`main.py:1642-1745`, `utils/scoring.py`) : `top_k=20`, `threshold=0.1` (**sur le cosinus seul, avant combinaison**), `rerank=False` ; sur-échantillonnage `max(top_k×4, 60)` ; BM25 normalisé par sigmoïde dépendant de la longueur de la requête (≤ 3 termes → (5,0 ; 0,7)… > 15 → (12 ; 0,5)) ; **bonus entité** = `sim × 0,5 × 1/(1 + 0,001 × (n_liens − 1)²)` (entité fréquente pénalisée, façon IDF), max sur ≤ 8 entités de requête ; combinaison `(sémantique + bm25 + entité) / max_possible` (1 + 1 + 0,5).
- **Expiration douce (OSS, réelle)** : `expiration_date` (YYYY-MM-DD, incluse, UTC) ; mémoires expirées **masquées, pas supprimées** (`show_expired=True` pour les revoir) ; date illisible = non expirée.
- **Décroissance par fraîcheur (« Memory Decay ») : plateforme seulement** (`project.update(decay=True)` lève une erreur en OSS). Algorithme documenté (`docs/platform/features/memory-decay.mdx`) : facteur multiplicatif borné **0,3 à 1,5** (≈ 1,5 juste après un accès ; 1,2-1,4 dans la journée ; 0,6-1,0 après quelques jours ; 0,4-0,6 après quelques semaines ; plancher 0,3) ; candidats `top_k×3` ≥ 50 ; **20 derniers accès** gardés par mémoire ; repli sur `event_date` puis `updated_at` ; **biais de classement, jamais filtre**.
- Importance stockée : aucune. Résumé : seulement procédural. Oubli : `delete`, `delete_all` par 1 000, `reset()`.

## Idées transposables à notre moteur
1. Journal **append-only** à côté du registre : `history(memory_id, old, new, event, created_at, is_deleted, actor, role)` ; un changement raconté écrit UPDATE old → new au lieu d'écraser ; DELETE garde l'ancien texte → l'avatar peut dire « avant j'habitais à… ».
2. **Format « transition »** en sortie de notre appel court : « X est passé de A à B parce que… » + drapeau `temporary` (« pour un mois », « j'essaie ») → alimente les faits temporaires avec durée.
3. Expiration douce (date incluse, masquée à la lecture, réveil possible : « tu te souviens de mon plâtre ? »).
4. **Dates relatives résolues à l'extraction** avec la date d'observation (parseur type chrono-node possible sans LLM).
5. Dédoublonnage à deux étages sans LLM : hash du texte normalisé, puis ≤ 10 voisins passés au modèle avec des **IDs entiers locaux** (anti-hallucination), remappés ensuite.
6. Entités par règles (compromise + regex) + table `entities(text_norm, type, linked_fact_ids[])`, fusion exacte puis cosinus ≥ 0,95 → « graphe par co-occurrence » gratuit et clé pour trouver les faits concurrents.
7. Classement hybride léger : `(cos + sigmoïde(bm25) + bonus_entité) / 2,5`, seuil sur le cosinus seul (0,1) ; SQLite / better-sqlite3 suffit.
8. **Fraîcheur comme biais, jamais filtre** (le decay plateforme refait en 20 lignes) : 20 derniers accès, facteur 0,3-1,5 ; faits fondateurs exemptés (plancher 1,0) pour ne pas affaiblir « premier fait l'emporte ».
9. Garde-fous à reprendre dans le prompt court : No Detail Contamination, No Implicit Attribute Inference, Meaning-Preserving, No Echo Extraction, `attributed_to` (ce que l'avatar a dit de lui / ce qu'on lui a dit).
10. Fenêtre glissante des 10 derniers messages par portée, tronqués à 300 caractères, pour résoudre les pronoms.
11. **À ne pas copier** : l'ADD-only pur (contradictions accumulées, départagées au classement — notre registre déterministe est plus sûr pour un personnage) ; le DELETE automatique de l'ancien flux (efface sans trace de transition) ; demander des liens au LLM sans les persister ; dimension d'embedder ≠ dimension du store.
