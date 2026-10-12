# Lecture du CODE SOURCE — Graphiti (Zep)

> Veille du 2026-10-12 (demande utilisateur). Clone local `getzep/graphiti`, commit 0a3b1711 (11/10/2026), lu par un agent d'exploration ; `G\` = `graphiti_core\`. Complète la fiche REF-06 (lue sur README + papier). **Ce qui est écrit ici vient du code, pas des articles.**

## Point important
Dans cette version, il n'existe **plus** de `extract_edge_dates.py` ni `invalidate_edges.py`. La datation est dans le prompt `extract_edges.edge` (règles DATETIME) et `extract_edges.extract_timestamps[_batch]` ; la détection de contradiction est fusionnée avec le dédoublonnage (`dedupe_edges.resolve_edge`) ; **le « depuis quand » est tranché par du code déterministe** (`G\utils\maintenance\edge_operations.py:715-783`), pas par le LLM.

## 1. Modèles
- **Arête-fait `EntityEdge`** (`G\edges.py:263-290`) : `name` (type de relation), `fact` (phrase), `fact_embedding`, `episodes[]` (épisodes qui attestent le fait — compteur réutilisé par le reranker `episode_mentions`), `valid_at` / `invalid_at` (**temps du monde**), `created_at` / `expired_at` (**temps du système**), `reference_time`, `attributes`. Bi-temporel.
  - `valid_at` : « when the fact became true; future-tense plans/promises use the episode reference time rather than the future occurrence date ».
  - `invalid_at` : « when the fact stopped being true; soft deadlines are not invalid_at ».
- **Nœuds** : `EntityNode` (name, name_embedding, `summary` évolutif, attributes typés), `EpisodicNode` (content, valid_at), `CommunityNode`, `SagaNode` (chaîne d'épisodes).
- **Résumé évolutif d'un nœud** (`node_operations.py:1088-1169`) : on ajoute les faits nouveaux à l'ancien résumé ; **≤ 2 000 caractères → gardé tel quel sans LLM** ; sinon LLM par lots de 30, tronqué à 1 000. Prompt : « Use ONLY facts explicitly stated… NEVER infer », « Current state over superseded state », « NEVER manufacture pattern language from a single occurrence », « If the new episodes add no durable fact, return the existing summary unchanged », « 2-6 dense sentences in third person ».

## 2. Pipeline par épisode (`graphiti.py:1432-1547`)
1. 10 derniers épisodes en contexte. 2. `extract_nodes` (1 appel). 3. résolution des nœuds : exact → MinHash → 0/1 appel. 4. `extract_edges` (1 appel, dates en ligne). 5. par arête : 2 recherches hybrides, `resolve_edge` (0/1), `extract_timestamps` (0/1), invalidation déterministe. 6. attributs et résumés. 7. sauvegarde, communautés en option. Épisodes traités **séquentiellement** par groupe.

## 3. Prompts (extraits exacts)
- `extract_nodes` : « NEVER extract abstract concepts, feelings, or generic words » ; termes de parenté nus interdits (« extract "Nisha's dad" not "dad" ») ; le locuteur est toujours le premier nœud ; test de spécificité « Could this have its own Wikipedia article… or is it specific enough to distinguish… within this conversation? » ; dates exclues ; « When in doubt, do NOT extract ».
- `extract_edges` : noms obligatoirement dans la liste ENTITIES ; « extract the more detailed version as a NEW fact — it is NOT a duplicate » ; « NEVER generalize ». **Règles DATETIME** : présent → `valid_at` = date de l'épisode ; futur / promesse → `valid_at` = date de l'épisode, jamais la date future ; « by March 2026 » n'est pas un `invalid_at` ; « until … » peut l'être ; changement / fin exprimés → `invalid_at` ; sinon `null` ; date seule = 00:00, année seule = 1er janvier.
- `extract_timestamps` (appelé seulement pour une arête NOUVELLE sans date ; petit modèle) : « NEVER hallucinate dates… Resolve relative expressions ("last week", "yesterday") using REFERENCE TIME… Do NOT infer dates from unrelated events ». Lots de 20.
- **Garde-fou regex sur le futur** (`temporal_edge_utils.py:14-71`) : marque de futur (`will|going to|plans to|promises to|'ll`…) → `valid_at` ramené à `reference_time` ; `invalid_at` futur effacé si échéance douce (`by|before|deadline`) sans marque de fin d'état (`until|through|no longer`…).
- `dedupe_edges.resolve_edge` (`G\prompts\dedupe_edges.py:44-114`) — sortie `{duplicate_facts:[idx], contradicted_facts:[idx]}` : « NEVER mark facts as contradicted unless the new fact explicitly makes the old fact false » ; « NEVER mark facts as duplicates if they have key differences… numeric values, dates, or key qualifiers » ; « Do NOT treat additional activity, progress, status… as contradictions of role, ownership, responsibility, membership » ; « Do NOT infer contradiction from recency alone, episode dates, weekly snapshots, section headings… ». Exemples : « software engineer » → « senior engineer » = contradiction (titre mis à jour), « ran 5 miles Tuesday » / « 3 miles Wednesday » = ni l'un ni l'autre.

## 4. Comment le CODE date une contradiction (`edge_operations.py:715-783`)
1. Nouvelle arête déjà munie d'un `invalid_at` → historique : `expired_at = now`.
2. Un candidat contradictoire dont `valid_at` est **postérieur** au nouveau (fait ancien raconté en retard) → c'est le **nouveau** qui est clos : `new.invalid_at = candidat.valid_at`.
3. Intervalles sans chevauchement → rien.
4. Sinon, si `old.valid_at < new.valid_at` → `old.invalid_at = new.valid_at`, `old.expired_at = now`.
5. **Rien n'est supprimé.**
Candidats : doublons = arêtes entre la même paire de nœuds (2 sens) ; à invalider = recherche hybride sur tout le groupe. Raccourcis sans LLM : même source / cible / fait normalisé → on ajoute l'épisode ; aucun candidat → pas d'appel.

## 5. Résolution d'entités
Candidats : propriétés d'identité (15), nom exact, cosinus ≥ **0,6** (15). Déterministe (`dedup_helpers.py`) : nom exact unique → fusion ; **entropie** : nom < 6 caractères ou < 2 mots ou entropie de Shannon < 1,5 → pas de flou, LLM ; flou = trigrammes + MinHash 32 permutations + LSH, fusion si Jaccard ≥ **0,9** ; à la fusion, les attributs non vides écrasent, les vides n'effacent jamais. LLM en lot (`dedupe_nodes.nodes`) : « same real-world object… NEVER mark… related but distinct » ; « EXACTLY n resolutions with IDs 0..n-1 » ; `-1` si doute.

## 6. Recherche hybride (`G\search\`)
Constantes : limite 10, **cosinus min 0,6**, MMR λ 0,5, BFS profondeur 3, requête BM25 ≤ 128 mots. Méthodes en parallèle (2 × limit chacune) : BM25 (plein texte), cosinus, BFS (`RELATES_TO|MENTIONS*1..3` depuis les nœuds des résultats). Rerankers : **RRF** `score += 1/(rang+1)` (**k = 1**, pas 60 ; aucune pondération entre listes) ; MMR non glouton ; `node_distance` = en réalité **un seul saut** (voisin direct = 1, sinon ∞ ; centre 0,1) ; `episode_mentions` = tri par `len(episodes)` ; cross-encoder (OpenAI nano « True/False » par logprob, Gemini, ou **local `BAAI/bge-reranker-v2-m3`**). Recettes : `search()` = BM25 + cosinus RRF ; `search_()` = + BFS + cross-encoder. Filtres temporels sur les 4 dates. **Aucun filtre par défaut n'exclut les faits expirés.** Bizarrerie : `search()` modifie `limit` sur l'objet de recette global réutilisé par la résolution des arêtes.

## 7. Communautés
Propagation de labels pondérée par le nombre d'arêtes (bascule si poids > 1, itération jusqu'à stabilité, aucun seuil à régler) ; résumé par **tournoi deux à deux** (`summarize_pair`, « SUMMARIES MUST BE LESS THAN 1000 CHARACTERS »), ≈ N−1 appels ; mise à jour incrémentale = 2 appels par nœud.

## 8. Limites
~**3 appels LLM + 1 à 2 par fait** par épisode (8 faits ≈ 12-20 appels) + embeddings par nœud et par fait + 2 recherches par fait. Sortie structurée exigée (Pydantic) — « particularly problematic when using smaller models » ; client OpenAI-compatible (Ollama) en `json_schema` ou `json_object` ; deux tailles de modèle ; température 0 ; client GLiNER2 possible. Bases : Neo4j 5.26, FalkorDB (+ `falkordblite` embarqué), Neptune, Kuzu (déprécié). **Pas de mode sans base graphe** (tout en Cypher). Apache 2.0.

## 9. Idées transposables à notre moteur (sans Neo4j)
1. Séparer les deux temps : `depuis_t`/`jusqua_t` (monde) + `appris_t`/`clos_t` (système) + `fait_remplacant_id`.
2. **Le LLM juge, le code date** : un appel `{doublons, contredits}` à indexation continue, puis la règle de chevauchement en JS (dont le récit rétrospectif qui clôt le NOUVEAU fait).
3. Prompt de contradiction anti-faux positifs, repris en français avec ses 3 exemples.
4. Garde-fou regex du futur (« va / compte / prévoit / promet / -ra » → depuis = maintenant ; « avant le / d'ici » ≠ fin ; « jusqu'au / ne plus » = fin).
5. Datation séparée, petit modèle, lots de 20, seulement pour les faits nouveaux sans date.
6. Raccourcis déterministes : fait identique normalisé → `nb_attestations++` ; entités : exact → MinHash Jaccard ≥ 0,9 avec refus du flou sous 6 caractères / entropie 1,5.
7. Candidats en SQL (même paire ; top 10 hybride sur les faits actifs), MariaDB FULLTEXT + cosinus bge-m3 (MariaDB 11.7+ : `VECTOR`, `VEC_DISTANCE_COSINE`), seuil 0,6.
8. **RRF** sur les listes sens / mots / importance / fraîcheur / lien (k = 60 plus doux que le k = 1 de Graphiti) au lieu de pondérer des scores.
9. Reranker local `bge-reranker-v2-m3` sur les 20 premiers.
10. Bonus de proximité sociale à un saut (relations avec compteurs).
11. Bonus `nb_attestations` (fait souvent raconté = central).
12. **Afficher les intervalles au rappel** (« vrai de 2019 à 2023 ») : le passé se raconte au lieu de s'oublier.
13. Résumé évolutif par relation sans LLM tant que < 2 000 caractères, sinon 2-6 phrases avec les règles « état courant », « pas de tendance d'une seule occurrence », « inchangé si rien de durable ».
14. Cercles de l'avatar (famille, travail) par propagation de labels sur les compteurs de relations (~30 lignes de JS).
15. Budget d'appels comme règle de conception : viser 1 appel combiné entités + faits + dates (`format` JSON d'Ollama) puis 1 `resolve` en lot seulement s'il y a des candidats.
16. Sorties JSON robustes avec un petit modèle : indices hors bornes ignorés, « EXACTEMENT n résolutions 0..n-1 », nettoyage des blocs ```json.
