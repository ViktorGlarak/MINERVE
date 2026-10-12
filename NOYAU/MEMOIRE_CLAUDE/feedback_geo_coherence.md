---
name: feedback-geo-coherence
description: Règle géographique AURIGE 2BB — vérifier cohérence tactique avant de citer une localité dans un inject
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 73fcca0d-c040-42d3-9859-fa36df54c216
---

Ne jamais citer une localité précise dans un inject sans avoir vérifié qu'elle est cohérente avec la phase tactique du jour de guerre (D+).

**Why:** Erreur corrigée le 2026-05-28 : inject @HmunikVoice D+33/J3 citait "secteur de HLUNEVILLE" — ville trop éloignée du front à J3. L'utilisateur a corrigé en "sur les bords de la Moselle". Table D+ = D+31 → J1 (frontière), D+33 → J3 (bords Moselle), D+37 → J7 (Nord-Ouest Nancy).

**How to apply:**
- Si la localisation est certaine et cohérente avec la phase tactique → citer directement.
- Si incertain → utiliser une formulation vague : "sur les bords de la Moselle", "dans le secteur nord", "à quelques kilomètres de la frontière".
- Si localisation précise requise → demander confirmation à l'utilisateur avant de rédiger l'inject.
- Cette règle s'applique à tous les agents (GUILLAUME, ANALYSTE, MASTAURIGE, EXPERT_INFLUENCE) pour tous les injects AURIGE 2BB.

Lié à : [[glm26_matrice_ili]] (table D+ synchromatrice)
