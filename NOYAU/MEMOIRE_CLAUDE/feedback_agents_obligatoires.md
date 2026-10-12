---
name: feedback-agents-obligatoires
description: "Règle absolue — mettre à jour SIMULTANÉMENT les mémoires de TOUS les agents concernés lors de toute production, pas après coup sur rappel"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 73fcca0d-c040-42d3-9859-fa36df54c216
---

Toute production (tweet card, article, image, inject, fonctionnalité technique) doit entraîner la mise à jour **simultanée** des mémoires de TOUS les agents concernés — pas après coup sur rappel de l'utilisateur.

**Why:** L'utilisateur a rappelé cette règle à plusieurs reprises. Oublier de mettre à jour un agent pendant la session de travail = travail incomplet. La mémoire des agents est aussi importante que le code ou le contenu produit.

**How to apply:**
- Avant de terminer toute tâche de production, identifier TOUS les agents dont la mémoire est impactée
- Pour un inject AURIGE 2BB : mettre à jour MASTAURIGE/MEMOIRE.md ET GUILLAUME/MEMOIRE.md EN MÊME TEMPS que le code
- Pour une fonctionnalité technique : MASTAURIGE/MEMOIRE.md + GUILLAUME/MEMOIRE.md + auto-memory si architectural
- Ne JAMAIS attendre que l'utilisateur demande "et l'agent X, il est au courant ?"
- La règle de mise à jour automatique est dans CLAUDE.md section "Règle de mise à jour automatique — OBLIGATOIRE"

**Agents typiquement concernés par les productions AURIGE 2BB :**
- MASTAURIGE → tout ce qui touche au WEB/index_master.html, tweet cards, MELMIL
- GUILLAUME → tout inject créé ou modifié (références, LO, timing, narratif)
- EXPERT_INFLUENCE → si l'inject touche à la doctrine ILI ou aux LO
- ANALYSTE_RB → si l'inject concerne Ruthnia Bella (07.05.xx)
