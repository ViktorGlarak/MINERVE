# PROTOCOLE QC — Contrôle Qualité par le Noyau (Claude)

## Principe
Chaque réponse d'un agent Ollama est interceptée et évaluée par Claude avant d'être transmise à l'utilisateur.
Si la réponse est insuffisante, Claude corrige, relance ou complète. La leçon est stockée en mémoire.

---

## Boucle QC complète

```
Utilisateur → Demande
     ↓
[MERCURE - Claude]
  1. Routing : quel agent ?
  2. Construction du prompt enrichi (contexte mémoire + system prompt)
  3. Appel API Ollama
     ↓
[AGENT Ollama répond]
     ↓
[MERCURE - Claude évalue]
  QC sur 5 critères (voir ci-dessous)
     ↓
  ┌─ PASS → Réponse transmise + mémoire mise à jour
  └─ FAIL → Relance avec prompt amélioré (max 2 tentatives)
                ↓
           Toujours FAIL → Claude complète/corrige lui-même
                ↓
           Leçon stockée dans MEMOIRE.md de l'agent
```

---

## 5 Critères d'évaluation QC

| Critère | Question posée | Poids |
|---|---|---|
| **Complétude** | La réponse couvre-t-elle tous les aspects demandés ? | Éliminatoire |
| **Précision** | Le contenu est-il techniquement correct ? | Éliminatoire |
| **Clarté** | La réponse est-elle bien structurée et compréhensible ? | Important |
| **Format** | Le format est-il adapté (code, liste, prose) ? | Important |
| **Pertinence** | Répond-elle vraiment à ce qui était demandé, sans hors-sujet ? | Important |

---

## Actions correctives selon le problème détecté

| Problème | Action Claude |
|---|---|
| Réponse incomplète | Relance avec "Complète en ajoutant : [manquant]" |
| Erreur technique | Corrige directement + note dans MEMOIRE.md |
| Mauvais format | Reformate la réponse de l'agent |
| Hors sujet | Relance avec prompt plus ciblé |
| Réponse trop vague | Relance avec "Sois plus précis sur : [point]" |
| Échec répété (2x) | Claude répond directement + note le pattern d'échec |

---

## Enrichissement du prompt (apprentissage)

Avant chaque appel agent, Claude injecte dans le prompt :
1. Le system prompt de l'agent (`SYSTEME/PROMPTS/agent.md`)
2. Les entrées pertinentes de `AGENT/MEMOIRE.md` (contexte accumulé)
3. Les patterns connus qui améliorent les réponses de cet agent

Après chaque appel réussi ou échoué, Claude met à jour `AGENT/MEMOIRE.md` :
- Ce qui a bien fonctionné → section "Patterns efficaces"
- Ce qui a échoué → section "Patterns à éviter"
- Contexte utile découvert → section correspondante

---

## Format d'entrée mémoire post-session

```markdown
### [YYYY-MM-DD] QC : [Résultat PASS/FAIL] — [Titre court]
**Demande :** résumé de ce qui était demandé
**Prompt envoyé :** version finale du prompt qui a fonctionné
**Problème détecté :** (si FAIL) description du problème
**Correction appliquée :** ce que Claude a fait pour corriger
**Leçon :** ce qu'il faut retenir pour les prochains appels
```
