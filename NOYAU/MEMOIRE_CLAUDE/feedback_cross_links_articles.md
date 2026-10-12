---
name: feedback-cross-links-articles
description: "Règle — les sections \"Related articles\" des articles HTML exercice ne doivent jamais pointer vers des articles futurs (chronologie exercise)"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 73fcca0d-c040-42d3-9859-fa36df54c216
---

Ne jamais inclure dans la section "Related articles" (ou équivalent) d'un article HTML d'exercice un lien vers un article publié à une date postérieure à l'article courant.

**Why:** En simulation temps réel, les stagiaires consultent les articles selon la chronologie de l'exercice. Un lien vers un article futur spoile un événement que l'animateur n'a pas encore "joué", brisant l'immersion et l'effet pédagogique. Identifié lors de l'audit du 2026-05-29 : 8 articles contenaient de tels liens (ex : BCI_Article_Frontiere du 30 Mai liait vers BCI_Article_MobilisationGenerale du 4 Juin).

**How to apply:** À la création ou mise à jour de tout article HTML (TM, BC1, TV4, HEX...) :
- Identifier la date de l'article en cours
- Pour chaque lien "Related" : date article lié ≤ date article courant
- Même jour = acceptable
- Futur = supprimer le lien

La chronologie de référence complète des articles existants est dans [[guillaume-memoire]] section "Règle éditoriale — Liens croisés".
