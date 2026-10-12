# OASIS (camel-ai/oasis) — analyse comparative avec le projet « avatars IA » de PLÉIADE

> Analysé le 2026-10-11 (nuit) à la demande de l'utilisateur. Sources : dépôt GitHub `camel-ai/oasis` (README, `oasis/social_agent/agent.py`, `agents_generator.py`, `oasis/social_platform/recsys.py`, `data/reddit/user_data_36.json`), article arXiv 2411.11581 (« OASIS: Open Agent Social Interaction Simulations with One Million Agents », nov. 2024, version HTML). Licence **Apache 2.0** (usage et modification libres). ~5 300 étoiles, 647 forks, dernier push août 2026, adossé au framework CAMEL (même équipe).

## 1. Ce qu'est OASIS

Un **simulateur de réseau social fermé** (X-like et Reddit-like) peuplé d'agents LLM, conçu pour la **recherche** : étudier la propagation d'information, la polarisation, l'effet de troupeau, la désinformation, à grande échelle (jusqu'à **1 million** d'agents). Ce n'est pas un réseau social utilisable par des humains : les agents parlent entre eux dans une base SQLite, par **pas de temps discrets** (`env.step()`), et on observe après coup.

Architecture (4 composants) :
- **Environment server** (`social_platform/platform.py`, 71 Ko) : le réseau (posts, follows, likes, commentaires), persistance SQLite.
- **Recommendation system** (`recsys.py`) : `rec_sys_random`, `rec_sys_reddit` (hot score façon Reddit : log10(|votes|) + récence/45000), `rec_sys_personalized` (similarité bio ↔ posts, SentenceTransformer `paraphrase-MiniLM-L6-v2`), `rec_sys_personalized_twh` (**TwHIN-BERT**, cosinus × fraîcheur × ressemblance aux posts déjà aimés). Nombre de posts montrés : `max_rec_post_len`. Fil = posts des comptes suivis (classés par popularité) + posts « extérieurs » recommandés.
- **Agent module** (`agent.py`, `agent_action.py`) : un `ChatAgent` CAMEL par avatar ; prompt système = profil ; à chaque pas l'agent reçoit l'état de la plateforme en texte (posts recommandés, notifications) et choisit **par function calling** parmi **21-23 actions** (`create_post`, `repost`, `follow/unfollow`, `mute/unmute`, `like/dislike post/comment`, `create_comment`, `search_posts`, `search_user`, `trend`, `refresh`, `do_nothing`, + signalement, groupes, « interview » depuis 2025), avec un raisonnement (chain-of-thought) stocké en mémoire.
- **Time engine** (`clock/`) : 1 pas = 3 minutes simulées ; chaque agent a un **vecteur d'activité sur 24 h** (`active_threshold`, probabilité d'être actif à chaque heure, tiré de données réelles).

Profil d'agent (`user_data_36.json`) : `realname`, `username`, `bio`, `persona` (un paragraphe), `age`, `gender`, `mbti`, `country`, `profession`, `interested_topics` ; version X : + `user_char`, `following_agentid_list`, `previous_tweets`. Générateurs de profils fournis (`generator/`), jeu de données HuggingFace `echo-yiyiyi/oasis-dataset`.

Modèles : n'importe quel modèle via `camel.models.ModelFactory` (OpenAI recommandé dans les exemples ; **vLLM / modèles locaux** possibles — les expériences à 1 M d'agents ont tourné sur 4 à 24 GPU A100 pendant une semaine). Coût mesuré : ~335 600 jetons d'entrée par pas pour 100 agents (Qwen).

## 2. Ce que leurs expériences ont montré (utile pour PSYCHOLOGUE)

- **Propagation d'information** (198 cas réels rejoués) : erreur RMSE normalisée ≈ **30 %** ; bonne reproduction de l'ampleur et de la largeur maximale, **profondeur de propagation sous-estimée** (le RecSys simplifié ne reproduit pas les relais intermédiaires).
- **Polarisation** : avec un modèle **non censuré**, les opinions deviennent **progressivement plus extrêmes** au fil de 80 pas ; avec des modèles alignés, variation modérée.
- **Effet de troupeau** (Reddit) : les agents LLM sont **plus sensibles au troupeau que les humains**, surtout face à un contenu traité négativement ; les humains sont plus délibératifs.
- **Désinformation** (1 M d'agents, 733 824 posts en 60 pas) : les posts de désinformation **surpassent constamment** les posts officiels en diffusion.
- **Échelle** : à partir de ~10 000 agents, les dynamiques de groupe deviennent plus riches et plus diverses ; certains effets (troupeau sur contrefactuel) **n'apparaissent qu'à grande échelle**.
- **Limites reconnues par les auteurs** : coût, RecSys simplifié, profils peu nuancés, biais du LLM (troupeau, extrémisme).

## 3. Comparaison avec notre projet

| | OASIS | PLÉIADE « avatars IA » |
|---|---|---|
| Finalité | recherche : observer des phénomènes à grande échelle, agents entre eux | **entraînement** : des avatars crédibles face à de **vrais joueurs**, sur un **vrai réseau** (Social de zone), en **temps réel** |
| Réseau | simulé dans SQLite, pas d'humain dedans | `app-social` réel : joueurs, animation, Cockpit, origine « IA », chat privé |
| Temps | pas discrets (3 min simulées), on rejoue vite | temps réel, rythme humain (retour au fil 10-30 min, plafonds horaires, sommeil) |
| Profil | 10 champs + persona d'un paragraphe | fiche eho complète (caractère, registre, aime / déteste, bio interne, affiché, réel) + fiche de comportement (tempérament 8 traits, sensibilités, a priori de confiance, proches, opinions, rythme, registres, consignes, lignes pour un relais) |
| État intérieur | mémoire de conversation CAMEL (contexte), raisonnement stocké ; **pas** de croyances / opinions / humeur / relations chiffrées | **modèle psychologique explicite** : croyances par fait (répétition, démenti, plancher), opinions par axe (hystérésis, doute, bascule), humeur, relations (familiarité / affinité / confiance, oubli selon rancune), habituation, effet plafond — chaque variation tracée « pourquoi ça a bougé » |
| Décision | function calling parmi 21-23 actions, chain-of-thought | JSON : action + ressenti forme / fond + émotion + intensité + thème + pourquoi ; contrôles de forme et de cohérence ; reformulation |
| Qui voit quoi | **RecSys** : abonnements + recommandation par similarité (TwHIN-BERT), popularité, fraîcheur ; activité horaire par agent | fil global + abonnements + mentions + popularité ; **pas de recommandation par similarité** (étape 5 du plan : « voir ≠ réagir », Sentinel) |
| Actions | post, repost, commentaire, like/dislike, follow, mute, search, trend, signalement, groupes, interview | post, réponse, citation, chat privé ; J'aime journalisés (pas de route de service) ; pas de follow dynamique, pas de recherche |
| Échelle | 1 M (sur grappe de GPU) ; 100-10 000 courant | 6 avatars sur 1 GPU portable ; 500 envisagés avec sélection des lecteurs |
| Validation | données réelles (propagation, polarisation, troupeau) | relectures PSYCHOLOGUE (avis n°1-5), scénarios S1-S3, injects ; pas encore de comparaison à des données réelles |
| Licence / maturité | Apache 2.0, 5 300 ★, équipe de recherche active | interne, 2 jours d'existence |

**Verdict** : OASIS est **plus abouti comme simulateur de masse** (échelle, RecSys, 23 actions, validation sur données réelles, outillage de génération de profils). Notre projet est **plus abouti sur ce qui nous importe** : la psychologie individuelle explicite et traçable, le réalisme du rythme, l'intégration à un vrai réseau avec de vrais joueurs, la validation humaine / l'origine « IA », et le pilotage par doctrine (PSYCHOLOGUE, EXPERT_INFLUENCE). Les deux ne font pas la même chose : OASIS observe une foule, nous animons des personnages.

## 4. Ce qu'on peut leur prendre (par ordre d'intérêt)

1. **Le vecteur d'activité sur 24 h** (`active_threshold[24]`) — plus fin que notre rythme lever / coucher / travail : une probabilité d'être actif par heure, tirée de données réelles. À ajouter à la fiche de comportement (étape 5), avec des gabarits par type (étudiant, commerçant, élu, militant).
2. **Le RecSys par similarité** (`rec_sys_personalized_twh`) pour choisir **qui lit quoi** à 500 avatars : embeddings des bios et des posts (modèle léger `paraphrase-MiniLM-L6-v2`, ou Sentinel / pgvector déjà dans `app-social`), score = similarité × fraîcheur × ressemblance aux posts déjà aimés. C'est exactement la sélection « voir ≠ réagir » dont on a besoin pour l'échelle.
3. **Les résultats de validation comme repères pour PSYCHOLOGUE** : les LLM sont plus moutonniers et plus extrémisants que les humains → nos garde-fous (plafonds d'opinion, hystérésis, habituation, raidissement petit) sont justifiés ; la désinformation « gagne » naturellement dans une foule d'agents → l'équilibre des camps doit être **piloté** (c'est le rôle de l'animation et des relais bleus).
4. **Les actions manquantes chez nous** : `follow/unfollow` dynamiques (un avatar qui se met à suivre un compte qu'il apprécie), `mute` (un avatar qui coupe un troll — réponse réaliste à Untergang), `search` / `trend` (consulter les tendances avant de publier), `dislike` n'existe pas sur notre Social. Follow et mute sont les plus utiles.
5. **La génération de profils en masse** (`generator/`, dataset HuggingFace, persona depuis profession / intérêts / MBTI) — pour peupler 500 fiches de comportement à partir des 4 037 avatars eho : un script qui déduit tempérament, sensibilités et registres de la fiche eho (métier, caractère, aime / déteste).
6. **Le rejeu accéléré** (pas de temps discrets) pour **tester vite** un lot de corrections avant de le mettre en temps réel : notre `simulation.mjs` fait déjà cela ; OASIS confirme que c'est la bonne méthode (ils ne font que ça).
7. **L'« interview »** d'un agent (poser une question hors réseau à un avatar pour connaître son état) : équivalent de notre journal « pourquoi », mais interactif — utile pour l'animation (« pourquoi as-tu répondu ça ? »).

Ce qu'on ne prend pas : l'intégration CAMEL / Python (notre moteur est en Node, branché sur PLÉIADE), les 1 M d'agents (hors besoin et hors matériel), le réseau simulé (nous avons le vrai).

## 5. Suite proposée

- Court terme (après le bilan de nuit) : `active_threshold` 24 h dans les fiches ; `follow` et `mute` comme actions du moteur (le Social a déjà les abonnements ; `mute` à voir côté app-social) ; repères OASIS dans la doctrine PSYCHOLOGUE (§3).
- Étape 5 (sélection à l'échelle) : RecSys par similarité (Sentinel ou MiniLM) + vecteur d'activité → « qui remarque ce post ».
- Plus tard : générateur de fiches de comportement depuis eho ; « interview » d'avatar dans la Console d'animation.
