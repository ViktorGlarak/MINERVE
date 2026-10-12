# REF-01 — Centaur : un modèle fondationnel de la cognition humaine (Psych-101)

- **Source** : Marcel Binz et 46 co-auteurs (Max Planck Institute, Google DeepMind, Oxford, Princeton…), *Centaur: a foundation model of human cognition*, arXiv:2410.20268 (oct. 2024, v3), licence CC BY 4.0.
- **Pages lues** : https://huggingface.co/papers/2410.20268 · https://www.alphaxiv.org/abs/2410.20268v1 (le 2026-10-10, fournies par l'utilisateur).
- **Ressources publiques** : modèle `marcelbinz/Llama-3.1-Centaur-70B-adapter` (Hugging Face) · jeu de données `marcelbinz/Psych-101` · test `Psych-101-test` (accès restreint, CC-BY-ND-4.0) · code `github.com/marcelbinz/Llama-3.1-Centaur-70B` · collaboration `github.com/marcelbinz/Psych-201`.

## Ce que c'est
- Le **premier « modèle fondationnel »** qui prétend **prédire et simuler le comportement humain dans n'importe quelle expérience exprimable en langage naturel**.
- Base **Llama 3.1 70B**, affinée par **QLoRA** (modèle gelé en 4 bits + adaptateurs de rang 8 ; **0,15 %** des paramètres entraînés ; une époque ; ~5 jours sur un GPU A100 80 Go).

## Psych-101, le jeu de données
- **160 expériences** de psychologie, **60 092 participants**, **10 681 650 choix** humains essai par essai, ~253 millions de jetons.
- Domaines : bandits multi-bras (exploration / exploitation), prise de décision, mémoire, apprentissage supervisé, processus de décision markoviens, raisonnement, apprentissage probabiliste…
- Chaque expérience est **retranscrite en langage naturel** (« Vous appuyez <<C>> et obtenez −8 points ») : un format commun pour des paradigmes hétérogènes.

## Résultats
- **Meilleur que 14 modèles cognitifs spécialisés** (théorie des perspectives, Rescorla-Wagner…) sur **159 expériences sur 160**, chez des participants jamais vus ; pseudo-R² **0,50** contre 0,32 (modèles cognitifs) et 0,36 (Llama non affiné).
- **Généralise** : nouvelle « histoire de couverture » (tapis magique au lieu d'un vaisseau), structure modifiée (bandit à 3 bras), **domaines absents** (raisonnement logique, jeux économiques, décision morale, catégories naturelles…).
- **Simulations en boucle ouverte** : reproduit la distribution des trajectoires d'apprentissage d'une population humaine (stratégies sans modèle, avec modèle, mixtes) ; **échoue volontairement** à imiter des agents non humains (contrôle).
- **Temps de réponse** (loi de Hick) : R² conditionnel 0,58 contre 0,40 (Llama) et 0,38 (modèles cognitifs).
- **Alignement neuronal (IRMf)** : après affinage, ses représentations internes prédisent mieux l'activité cérébrale (tâche à deux étapes, 94 participants ; lecture de phrases, effet faible mais significatif).
- **Découverte guidée par le modèle** : utilisé pour améliorer un modèle de décision multi-attributs (« minimisation du regret scientifique »).

## Limites reconnues par les auteurs
- Expériences en langage naturel seulement (pas la vie réelle) ; population **WEIRD** (occidentale, éduquée, industrialisée, riche, démocratique) ; **peu de différences individuelles** (âge, traits de personnalité) ; pas de développement ni de psychiatrie ; peu de psychologie sociale et de jeux économiques dans les données (piste d'extension).

## Application au projet « avatars animés par IA » (transposition de PSYCHOLOGUE, pas un avis des auteurs)
1. **Preuve de principe** : un grand modèle de langage, guidé par des données comportementales, **prédit des choix humains** mieux que des modèles spécialisés. Notre approche (un LLM local qui décide « répondre / aimer / ignorer » et formule le ressenti) va dans le sens de l'état de l'art.
2. **Le format compte** : décrire la situation en langage naturel (« tu vois tel post, de tel compte, que fais-tu ? ») est exactement le format qui a permis la généralisation de Centaur. → garder des invites concrètes, situées, à la deuxième personne.
3. **Ce qui manque à Centaur et que nous devons apporter** : les **différences individuelles** (personnalité, rancune, crédulité, ancrage) et la **dimension sociale** — c'est précisément le cœur de notre système (relations, contagion). → nos paramètres de tempérament ne sont pas redondants avec un modèle généraliste : ils sont indispensables.
4. **Matériel** : Centaur (70B) ne tient pas sur le PC du projet (RTX 5070 Ti 12 Go) ; envisageable plus tard sur une machine plus puissante du parc. Psych-101 est **public** : ses paradigmes (exploration / exploitation, apprentissage par renforcement) peuvent servir à **calibrer** des comportements (ex. la tendance d'un avatar à explorer de nouveaux comptes ou à rester dans sa bulle).
5. **Validation** : comme Centaur se valide sur des participants **jamais vus** et des situations **modifiées**, nos essais doivent tester des publications et des personnes nouvelles, pas seulement des cas connus.
