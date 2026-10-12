---
name: convention-injects-relance
description: "Convention XX.YY.ZZAi.Rx — injects de relance MELMIL (jouées si non-réponse des entraînés), draggables et synchronisés avec index_master.html"
metadata: 
  node_type: memory
  type: project
  originSessionId: 73fcca0d-c040-42d3-9859-fa36df54c216
---

Les **injects de relance** portent le suffixe `.Rx` après le code de leur inject parent.

**Format :** `XX.YY.ZZAi.R1` (relance 1 de l'inject `XX.YY.ZZAi`)

**Why:** Les injects P-xx et R-x créés antérieurement n'apparaissaient pas dans MELMIL faute de convention standard. Le nouveau format `.Rx` permet d'ancrer la relance sur son inject parent et de l'intégrer automatiquement dans la card MELMIL de l'incident.

**How to apply:**
- Créer card dans index_master.html + ANIM_DATA (`num:"07.05.02Ai.R1"`) + LO_BY_KEY
- Ajouter dans melmil_inject_index.js : `"07.05.02Ai.R1": [{key:"...", type:"...", label:"[RELANCE R1] — condition — contenu"}]`
- Pas de ligne dans MELMIL.xls — l'incident parent `07.05.02i` doit exister
- melmil.js modifié le 2026-05-29 : getParentInjectCode + savePositions regex + buildGhostInjects CSS badge orange

**Migration P-xx / R-x complète (2026-05-29)** : tous les anciens codes ont été renommés. Les 2 seules véritables relances `.Rx` sont :
- `08.01.01Ai.R1` (courrier_maire_hsarrebourg_relance) — maire WEBER 48h sans réponse
- `08.01.01Ai.R2` (courrier_prefet_escalation) — préfet Birkmann 5 jours sans réponse

Les autres (P-xx, R1, R4, R5, R6) étaient des injects ordinaires mal nommés — maintenant correctement intégrés dans 07.07, 07.08, 07.05, 08.03, 07.01. Voir [[melmil-coherence]] section "Migration P-xx / R-x complète".
