# REF-04 — Cognee (mémoire hybride graphe de connaissances + vecteurs)

- **Source** : README du dépôt https://github.com/topoteretes/cognee (lu le 2026-10-12, fourni par l'utilisateur) ; site docs.cognee.ai (page « memify » introuvable le jour de la lecture — les points marqués *[connaissance de l'agent]* viennent de la doc telle que connue, à revérifier).
- **Licence** : Apache 2.0. **Langage** : Python 3.10-3.14. Points d'entrée : API Python, CLI, conteneurs Docker, serveur MCP.
- **Contexte de la veille** : avis n°16 (MEMOIRE §4.16) — ce qu'on peut récupérer pour la mémoire des avatars, pas « adopter la librairie ».

## Ce que fait le projet
- Promesse : « *Give your AI agents persistent long-term memory with small models for free* » — tout peut tourner en local, sans clé d'API, avec un petit modèle d'extraction.
- **Architecture de mémoire hybride** à trois composants : **graphe de connaissances** (entités + relations extraites du texte) · **stockage vectoriel** (embeddings pour la recherche par le sens) · **sessions** (mémoire de travail temporaire, « distillée » en mémoire permanente sur demande). Le moteur choisit lui-même la stratégie de rappel (graphe, vecteurs ou les deux) selon la requête.
- **Pipeline ECL** : *Extract* (un modèle **GLiNER** embarqué repère entités et relations **sans LLM**) → *Cognify* (enrichissement : découpage, entités, relations, résumés, ontologie) → *Load* (écriture dans les bases).
- **Opérations** : `remember` (stocker), `recall` (rappeler), `improve` (améliorer **avec un retour d'usage** — les mémoires jugées utiles sont renforcées), `forget` (supprimer). *[connaissance de l'agent]* : `memify` = passe d'algorithmes de mémoire après cognify (retour, poids d'importance, élagage, conscience temporelle) ; types de recherche GRAPH_COMPLETION / CHUNKS / INSIGHTS / TEMPORAL.
- **Bases** : graphe Neo4j ou Kuzu ; vecteurs LanceDB ; PostgreSQL + pgvector (+ extension graphe en démo v1.6). **Modèles** : GLiNER local pour l'extraction ; LLM optionnel (OpenAI ou **Ollama**) pour les réponses et les traitements avancés.
- Résolution des contradictions et oubli : **pas de mécanisme explicite** dans le README (`forget` = suppression manuelle ; pas de validité temporelle des faits comme chez Graphiti, REF-06).

## Ce que dit le CODE SOURCE (clone local — lecture par agents d'exploration, transmise par NOYAU)
Quatre mécanismes d'agent, plus précis que le README :
1. **Poids de souvenir appris par retour** (`cognee/tasks/memify/apply_feedback_weights.py`) : `w ← w + 0,1·(r − w)` (r = signal de retour), **demi-pas** pour un signal implicite ; influence du poids sur le classement **réglable**.
2. **Oubli SANS HORLOGE** pour les préférences (`modules/user_preferences/weights.py`) : `w_eff = 0,5 + (w − 0,5)·(1 − 0,02)^tours_inactifs`, **calculé à la lecture** (rien n'est réécrit), suppression sous 0,01. L'oubli compte les **tours sans usage**, pas les heures.
3. **Consolidation de session en deux passes LLM** (`modules/session_distillation/`) : un **curateur** par lot propose, un **rédacteur** accepte ou rejette avec une raison (`already_known` / `not_durable` / `unsupported`) et un « *why_learned* » ; seuil de confiance ≥ 0,75.
4. **« Supersession » sans LLM** pour les relations à valeur unique — habite, travaille chez (`tasks/graph/resolve_temporal_contradictions.py`) : le fait récent marque l'ancien `superseded`, **rien n'est supprimé** ; détection LLM des autres contradictions à seuil 0,5.
- Aussi : graphe d'événements `Event{name, description, time_from, time_to, location}` avec la règle « tout verbe est un événement » (**trop fin pour nous**) ; recherche **TEMPORAL** : le LLM extrait l'intervalle de la question avec la date du jour injectée, filtre par date puis reclasse par le sens. Le reste (chunks, ontologies, graphe de code, text-to-SQL) est documentaire, sans intérêt.

## Ce qui est pertinent pour la psychologie des avatars
- **Mémoire sémantique en graphe** (qui est qui, qui tient quel rôle, quelle institution dit quoi) : c'est la « base de son camp » de notre doctrine (§3.2, mémoire sémantique — étape 3 non commencée). Un graphe d'entités donne au rappel un second chemin que le sens seul ne donne pas : « le maire » ↔ « Mordvidchev » ↔ « la mairie de HNancy ».
- **Sessions distillées en mémoire permanente** = notre consolidation (mémoire de travail → marquants / résumés).
- **`improve` / retour d'usage** = l'idée ACT-R (REF-02) que l'**activation d'un souvenir monte quand il sert** : un souvenir rappelé et effectivement utilisé devient plus facile à rappeler ensuite. Chez nous l'importance `imp` est **figée à l'écriture** ; rien ne monte à l'usage.
- **Extraction d'entités sans LLM** (GLiNER) : montre qu'on peut étiqueter les souvenirs par entités **à coût nul en appels modèle**.

## Ce que nous avons déjà d'équivalent (app-ia 2026-10-12.2)
| Cognee | Moteur |
|---|---|
| vecteurs + rappel par le sens | `rappel.mjs` : bge-m3 sur processeur, int8 en base, score 0,5 sens + 0,2 importance + 0,15 fraîcheur + 0,15 lien, seuil relatif |
| sessions → mémoire permanente | `memoire.mjs` : 48 h détaillé → marquants (≤ 30, imp ≥ 5) → résumés par jour / semaine, par le code |
| graphe d'entités | ✗ rien ; le « lien » du rappel ne connaît que l'auteur et les abonnements |
| `improve` (renforcement à l'usage) | ✗ `imp` figé à l'écriture |
| `forget` | consolidation : « aimer / ignorer » de imp < 3 oubliés ; relations passantes purgées après 72 h |

## À récupérer (idées précises)
1. **Renforcement à l'usage** (`improve`, ACT-R) : quand un souvenir rappelé est **repris dans la réponse** (le texte publié partage ≥ 3 mots pleins avec lui, ou la pensée courte le cite), `imp = min(10, imp + 1)` et `derniere_utilisation = t` ; le facteur fraîcheur du rappel prend `max(t_écriture, derniere_utilisation)`. Effet attendu : les souvenirs qui structurent la semaine de l'avatar (le témoin anonyme, l'insulte d'Untergang) restent rappelables au J6 sans grossir le JSON. Coût : 0 appel modèle.
2. **Étiquetage par entités de l'exercice, sans modèle** : un lexique fermé fourni par l'animation (lieux H-préfixés, institutions, personnages, hashtags des campagnes) → chaque souvenir reçoit `entites: [...]` à l'écriture (recherche de chaînes, comme `reperer()` de `vie.mjs`). Le facteur `lien` du rappel devient `1` même auteur · `0,5` abonnement **· `0,5` ≥ 1 entité commune avec la publication lue**. C'est un graphe à un saut, sans base de graphe.
3. **Oubli sans horloge, calculé à la lecture** (code n°2) : pour les **sensibilités par thème** et les **hashtags** (aujourd'hui demi-vies en heures : 72 h, 24/48/72 h), compter plutôt les **retours au fil sans contact** avec le thème ou le #, `v_eff = repos + (v − repos)·0,98^n_tours_inactifs`, sans réécrire la mémoire. Psychologiquement plus juste qu'une horloge : un avatar qui n'a pas lu le fil pendant 24 h n'a pas « oublié » 24 h de rancune — l'oubli se fait par ce qu'on vit entre-temps (interférence, pas décroissance — *à sourcer*). Pour les **relations**, garder l'horloge (décision utilisateur : demi-vie par rancune et gravité), mais le même calcul à la lecture économise les réécritures de `oublier()`.
4. **Poids appris par retour** (code n°1) : formule plus propre que « +1 » pour l'idée 1 : `imp ← imp + 0,1·(10 − imp)` quand le souvenir rappelé est repris, demi-pas (0,05) s'il n'est que présent dans l'invite d'un message publié ; plafond 10, jamais de baisse (l'oubli reste à la fraîcheur).
5. **Raisons de rejet à la consolidation** (code n°3), sans LLM : quand un fait extrait est refusé par le registre, journaliser la raison `déjà_su` / `non_durable` / `non_étayé` (= rejoint le journal des 4 issues de REF-05). La **double passe LLM** elle-même, non (coût).
6. **Supersession** (code n°4) : c'est exactement `enregistrerFaits` (fait récent raconté comme changement → ancien clos) — à étendre aux **clés à valeur unique** du bloc `vie` (domicile, métier, transport) qui, elles, ne sont jamais remplacées aujourd'hui : un déménagement raconté marque la fiche `superseded_par` le registre, au lieu de rester en contradiction (fiche > registre reste l'autorité, mais l'invite montre la valeur à jour).
7. **Ne pas récupérer** : le graphe de connaissances complet (Neo4j/Kuzu + LanceDB + pipeline Python), le graphe d'événements par verbe, la recherche TEMPORAL par LLM (notre filtre par `depuis_t`/`jusqua_t` suffit).

## Coût
- Service Python + base de graphe + base vectorielle à ajouter dans le conteneur : **lourd**, contraire à la règle « pas de service lourd sauf gain net ». Les idées 1-2 se font dans `memoire.mjs` / `rappel.mjs` sans dépendance.
- Appels modèle : idées 1-2 = **0**. Licence Apache 2.0 (pas de contrainte).
- CYBERSECU : rien ne sort (les deux idées sont du code local).

## Verdict : **RÉCUPÉRER L'IDÉE** (oubli sans horloge calculé à la lecture ; poids appris par retour ; supersession des clés à valeur unique ; raisons de rejet), librairie **sans intérêt pour nous**
Raison : le README ne montrait que le graphe (service lourd, sans intérêt), mais le **code** contient quatre mécanismes **sans LLM**, psychologiquement justes et transposables en quelques lignes dans `esprit.mjs` / `vie.mjs` / `memoire.mjs`. Verdict relevé de « s'en inspirer plus tard » à « récupérer l'idée » le 2026-10-12 après lecture du code.
