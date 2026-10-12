---
name: feedback_agent_minautore_pilote_7bb
description: "Tout travail sur l'exercice MINOTAURE/AURIGE 7BB doit être PILOTÉ par l'agent MINAUTORE et RELU/CORRIGÉ par les agents compétents — pas exécuté seul"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: a68d232b-0e67-4473-8fe3-3260ee347b9f
---

Sur l'exercice **MINOTAURE / AURIGE 7BB**, je dois **opérer en tant qu'agent MINAUTORE** (charger `SYSTEME/PROMPTS/minautore.md` + `MINAUTORE/MEMOIRE.md`), pas seulement « toucher sa mémoire ». Et toute production/décision doit être **relue et corrigée par l'agent compétent**, qui **propose des corrections si besoin** :
- camp / identité / doctrine d'un persona ARN → **ANALYSTE_ARN** (autorité du camp)
- effets ILI, séquence PSYOPS (steps 1→3), synchromatrice, fit LO → **EXPERT_INFLUENCE**
- rédaction (tweets, courriers, voix locale) → **SCENARISTE**
- personas/camp Mercure, TTP Storm-1516 → **ANALYSTE (Mercure)**
- format RS/HTML/outillage → **MASTAURIGE**

**Why:** l'utilisateur l'a demandé **plusieurs fois** ; je retombais dans l'exécution mécanique de ses consignes (renum, dates, textes) sans appliquer le jugement éditorial de MINAUTORE ni faire valider les camps/ILI/rédaction par les agents — sur du **contenu diffusé aux entraînés**, ça produit des erreurs (mauvais camp = effet ILI inverse). Frustration explicite le 2026-06-21.

**MINAUTORE = LE référent de l'exercice (réflexe n°1).** Il doit TOUT maîtriser : quel inject joue de quand à quand, quelle storyline/LO, quel persona à quelle date, si tel article est utilisé. Pour toute question de ce type → **consulter D'ABORD MINAUTORE** (sa carte générée `MINAUTORE/ETAT_EXERCICE_7BB.md` + `MEMOIRE.md`), **jamais un grep à l'aveugle**. La carte est **générée** par `py MINAUTORE/generer_etat_exercice.py` (depuis les données réelles : socle JEMM + bakés) → **la relancer après TOUTE modif** pour que MINAUTORE reste à jour et fiable. *(Demande explicite + répétée user 2026-06-21 : « questionner MINAUTORE et le faire intervenir doit devenir LE réflexe quand on parle de l'exercice ».)*

**How to apply:**
1. Solution **imposée par le système** : hook PostToolUse `.claude/hooks/minautore_agent_reminder.py` (déclenché à chaque Edit/Write d'un fichier `AURIGE 7BB`/`MINOTAURE`) → injecte le rappel de routage. (cf. [[feedback_mastaurige_memoire]] même mécanisme.)
2. Pour une **production substantielle** (nouveau tweet/article, attribution de camp, séquence ILI) : lancer un **sous-agent** (Agent tool) chargé du prompt+mémoire de l'agent compétent pour **relire et proposer des corrections**, puis appliquer.
3. **Rapporter explicitement** « validé / corrigé par <AGENT> » à l'utilisateur et **consigner** dans `MINAUTORE/MEMOIRE.md`.
4. Généralise à **tout exercice** : l'agent chef d'orchestre de l'exercice pilote, les agents thématiques relisent. [[transition_minautore]] [[aurige7bb_actif]]
