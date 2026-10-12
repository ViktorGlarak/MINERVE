# REF-05 — Mem0 (couche de mémoire dynamique : extraction de faits + décision ADD / UPDATE / DELETE / NOOP)

- **Sources** : README https://github.com/mem0ai/mem0 (lu le 2026-10-12, fourni par l'utilisateur) ; papier Chhikara et al., *Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory*, arXiv 2504.19413 (2025).
- **Licence** : Apache 2.0. **Langages** : Python (`pip install mem0ai`) et **TypeScript** (`npm install mem0ai`). Bases : Qdrant, Chroma, pgvector ; graphe optionnel Neo4j, Memgraph, Kuzu. Modèles : OpenAI par défaut, **Ollama** possible ; embeddings OpenAI par défaut (Qwen 600M+ recommandé pour l'hybride). Déploiement : librairie, serveur Docker auto-hébergé, ou plateforme cloud (exclue : règle CYBERSECU).

## Ce que fait le projet
- Trois niveaux de mémoire : **utilisateur** (préférences et traits durables), **session** (contexte d'une conversation), **agent** (état et actions confirmées).
- **Pipeline `add` du papier, en deux phases** :
  1. **Extraction** : le LLM reçoit un résumé global de la conversation + les derniers messages et produit des **faits candidats** (phrases courtes).
  2. **Mise à jour** : pour chaque fait, recherche des *s* mémoires les plus proches (vecteurs), puis le LLM **décide par appel d'outil** : **ADD** (nouveau), **UPDATE** (enrichit ou corrige une mémoire existante), **DELETE** (contredite), **NOOP** (déjà su).
- **Mem0-g** (variante graphe) : triplets entité-relation, détection de conflits, invalidation des nœuds obsolètes ; gain ≈ +2 % seulement.
- **Résultats LOCOMO** (papier) : +26 % relatifs (LLM-juge) sur la mémoire OpenAI ; latence p95 **−91 %** et **−90 % de tokens** par rapport au contexte complet ; meilleur sur les quatre familles de questions (un saut, multi-sauts, **temporelles**, domaine ouvert).
- ⚠ **Évolution notable (README, « algorithme d'avril 2026 »)** : Mem0 est **revenu sur son propre pipeline** — « *single-pass ADD-only extraction — one LLM call, no UPDATE/DELETE* », les mémoires **s'accumulent** au lieu d'être réécrites, et la contradiction se règle **à la lecture** (rappel multi-signal : sens + BM25 + entités, fusionnés). Gains annoncés : LoCoMo 92,5 (+21), LongMemEval 94,4 (+27). Leçon : la résolution des contradictions **à l'écriture par LLM** coûte cher et se trompe ; garder l'historique et trancher au rappel est plus robuste.

## Ce que dit le CODE SOURCE (clone local du 2026-10-07, v3 — lecture par agents d'exploration, transmise par NOYAU)
> ⚠ Contredit en partie le papier : **le pipeline ADD / UPDATE / DELETE / NOOP n'existe plus dans l'open source.**
- **Extraction en une passe, ADD seul** (`mem0/configs/prompts.py:468-944`, `ADDITIVE_EXTRACTION_PROMPT`). Les contradictions ne sont pas résolues : elles **s'accumulent comme nouvelles mémoires formulées en « transition »** (« *User switched from A to B after…* »), avec un drapeau de **temporaire** quand le texte le dit (« *for a month* », « *trying out* »).
- **Mémoires « riches » de 15-80 mots** plutôt qu'atomiques (contexte conservé dans la phrase).
- **Garde-fous de prompt** réutilisables : « *No Detail Contamination* » (ne pas mélanger deux faits en un), « *No Implicit Attribute Inference* » (ne rien déduire qui n'est pas dit), « *Meaning-Preserving* » (« *I used to love X* » ⇒ n'aime plus X), **résolution des dates relatives avec la date d'OBSERVATION du message, jamais la date système**.
- **Recherche hybride** cosinus + BM25 + **bonus d'entité** (`mem0/utils/scoring.py`), seuil 0,1 sur le cosinus seul ; **entités extraites sans LLM** (spaCy / compromise) et liées par co-occurrence (seuil 0,95).
- **Expiration douce** : `expiration_date` **masquée à la lecture**, jamais supprimée.
- **Décroissance par fraîcheur** (« decay », facteur 0,3-1,5 sur le score, 20 derniers accès) : **plateforme seulement** (`docs/platform/features/memory-decay.mdx`), absente de l'OSS. **Aucune importance ni oubli en OSS** ; la mémoire graphe de triplets est **retirée** de l'OSS. Bug : `linked_memory_ids` demandés au LLM, jamais persistés.

## Ce qui est pertinent pour la psychologie des avatars
- Le **registre des faits acquis** (ce que l'avatar a dit de sa propre vie) est exactement une « mémoire utilisateur » Mem0 : un petit nombre de faits durables, soumis à doublons (« ma bagnole » / « ma voiture ») et à contradictions (« je vis seul » / « ma femme »).
- La grille **ADD / UPDATE / DELETE / NOOP** est une bonne **grille de lecture** pour journaliser ce que fait le registre — à condition de **ne jamais appliquer DELETE à une croyance** : un démenti ne supprime pas une rumeur crue, il la fait baisser avec un reste (influence persistante, Lewandowsky 2012 — *à sourcer*), ce que fait déjà `croire()` (plancher 25 % du pic, démenti × 0,6).
- La leçon « ADD-only + tranchage au rappel » rejoint la psychologie : on ne **désapprend** pas, on **superpose** ; la version la plus récente et la plus répétée domine à l'évocation.
- Les trois niveaux Mem0 ↔ nos trois autorités : **fiche** (permanent, utilisateur) > **registre** (l'exercice, session) > **message** (le tour, agent).

## Ce que nous avons déjà d'équivalent (app-ia 2026-10-12.2)
| Mem0 | Moteur |
|---|---|
| extraction de faits par LLM | `vie.mjs` : expression régulière d'abord, **un** appel JSON court seulement si elle trouve quelque chose (5-10 % des messages) — moins cher que Mem0 (1 appel par message) |
| NOOP / UPDATE / ADD | registre : **le premier fait l'emporte** (NOOP), changement raconté avec marqueur = UPDATE (l'ancien fait est **clos**, `jusqua_t = t`, pas supprimé), ≤ 1 changement permanent / semaine |
| recherche des *s* mémoires proches avant de décider | ✗ rapprochement par **clé exacte** (`sansAccents(cle)`) seulement : « bagnole » ≠ « voiture », « mon fils » ≠ « mon gamin » |
| DELETE | jamais pour une croyance (juste) ; faits temporaires périmés par durée |
| rappel multi-signal | sens (bge-m3) avec **repli** sur les mots communs — pas de fusion |

## À récupérer (idées précises)
1. **Rapprochement sémantique avant d'écrire au registre** (phase 2 de Mem0, sans LLM) : avant d'ajouter un fait, comparer son embedding (`cle + valeur`, bge-m3 déjà en cache) aux faits actifs ; si cos ≥ 0,80 avec un fait existant → le traiter comme **le même fait** (NOOP, ou UPDATE si marqueur de changement). Tue les doublons « bagnole / voiture », « gamin / fils ». Coût : 1 embedding par fait extrait (≈ 5-10 % des messages).
2. **Journaliser la décision à 4 issues** pour l'animation : chaque fait extrait sort avec `issue ∈ {ajouté, confirmé, changé, contradiction refusée}` dans le journal du pont ; la **contradiction refusée** (fait permanent contredit sans récit de changement) devient une **alerte d'animation** et un défaut Q1 de la relecture (avis n°13). Coût : 0.
3. **Fusion mots + sens au rappel** (le « multi-signal » du README) : au lieu du repli, combiner par rang (RRF : `1/(60+rang_sens) + 1/(60+rang_mots)`) — un souvenir qui partage un nom propre rare (« rue des Carmes ») remonte même si le sens est moyen. Coût : 0 appel (les mots communs existent déjà).
4. **Garde-fous de prompt dans l'appel d'extraction de `vie.mjs`** (tirés du code, 0 appel de plus) : *pas de contamination* (un fait par entrée, pas « voiture en panne et sœur malade ») ; *pas d'inférence implicite* (« je rentre tard du dépôt » ne fait pas un métier) ; *sens préservé* (« avant, j'avais un chien » ⇒ fait **clos**, pas actif) ; **dates relatives résolues avec la date du message** (rejoint REF-06 idée 1). Sortie en phrases de 15-40 mots avec le contexte, plutôt que « clé : valeur » nue, pour la version rappelée ; la clé reste pour le rapprochement.
5. **Mémoires de transition** : quand un changement est raconté, écrire **une entrée « transition »** (« ne vit plus seul : sa compagne est arrivée mardi »), au lieu de seulement clore l'ancien fait — c'est ce que l'avatar peut raconter ensuite. Le drapeau « temporaire si le texte le dit » (« pour un mois », « en attendant ») vient compléter notre table de durées par défaut.
6. **Expiration douce** : nous l'avons déjà (`jusqua_t` masque le fait dans `blocVie` sans le retirer du registre) — à garder tel quel ; le code de Mem0 confirme le choix.
7. **Ne pas récupérer** : la décision par LLM à chaque fait (retirée du code) ; la librairie (vector store + 1 appel par message × 105 avatars) ; Mem0-g (retiré de l'OSS) ; la décroissance « decay » (plateforme seulement, et notre fraîcheur 0,5^(âge/(24+20·imp)) la couvre).

## Coût
- Librairie TS disponible mais exige un magasin vectoriel et des appels modèle par message : **non** (nous avons déjà bge-m3 + MariaDB). Idées 1-3 = code local dans `vie.mjs` / `rappel.mjs`, 0 à 1 embedding de plus par fait ; aucun service, rien ne sort.
- Licence Apache 2.0.

## Verdict : **RÉCUPÉRER L'IDÉE** (rapprochement sémantique avant écriture + journal des 4 issues ; garde-fous de prompt et dates résolues à la date du message ; mémoires de transition ; fusion mots + sens + bonus d'entité)
Raison : c'est le défaut le plus visible de notre registre (clé exacte) et la correction coûte un embedding déjà en cache. Le code de Mem0 (ADD seul, contradictions accumulées en « transition », expiration masquée et non supprimée) **valide** notre choix « premier fait l'emporte, ancien fait clos, par le code » — et ses garde-fous de prompt sont directement transposables à l'appel d'extraction de `vie.mjs`.
