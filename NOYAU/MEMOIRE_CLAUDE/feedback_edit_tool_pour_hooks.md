---
name: feedback_edit_tool_pour_hooks
description: "Pour les éditions de contenu (data/HTML des exercices), préférer l'outil Edit/Write à Python/Bash pour déclencher les hooks de rappel"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: a68d232b-0e67-4473-8fe3-3260ee347b9f
---

Pour modifier le **contenu** d'un exercice (tweets/articles/dates/hashtags dans `tweets_data.js`, `articles_data.js`, `melmil_data.js`, HTML des `Sites/…`), **préférer l'outil Edit/Write** plutôt qu'un script Python/Bash.

**Why:** les hooks PostToolUse (`minautore_agent_reminder`, `aurige_methodo_reminder`, `mastaurige_memoire_reminder`) ne se déclenchent que sur les outils **Edit/Write/MultiEdit**, **pas** sur les écritures via Bash/Python. Passer par Edit fait apparaître automatiquement le rappel « opère en MINAUTORE / consulte la carte / fais valider par l'agent compétent » → le réflexe ne dépend plus de ma seule vigilance. (Demande user 2026-06-21, en appui de [[feedback_agent_minautore_pilote_7bb]].)

**How to apply:**
- **Par défaut** : éditer le contenu via **Edit** (remplacement ciblé d'un `old_string` unique) — idéal pour une date, un texte de tweet, un hashtag, une phrase d'article.
- **Exception** : Python/Bash reste OK pour le **lourd/structurel** (renumérotation de plusieurs injects, suppression d'objets, regénération `melmil_data.js`, audits). Dans ce cas, **suivre le process à la main** (carte MINAUTORE d'abord, agents pour validation, régénérer `ETAT_EXERCICE_7BB.md`) puisque le hook ne se déclenchera pas.
- Toujours **régénérer `MINAUTORE/ETAT_EXERCICE_7BB.md`** après une modif d'exercice (cf. [[feedback_agent_minautore_pilote_7bb]]).
