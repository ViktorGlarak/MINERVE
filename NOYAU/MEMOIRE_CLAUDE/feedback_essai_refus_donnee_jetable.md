---
name: feedback_essai_refus_donnee_jetable
description: "Un essai de droits (refus attendu) d'une action destructive se joue sur une donnée jetable créée pour l'essai, jamais sur une donnée existante — même en base locale"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 699185de-99a6-4263-a321-d605be7e2b29
  modified: 2026-10-07T09:28:30.718Z
---

Un essai qui vérifie qu'une action destructive est REFUSÉE (suppression, retrait de groupe…) se fait sur une donnée **jetable créée pour l'essai**, avec des `assert` qui vérifient le choix de la cible AVANT l'action.

**Why:** le 2026-10-07, un script d'essai des droits eho filtrait mal (`group=` au lieu de `groupId=`) : il a pris un avatar hors camp, le refus ne s'est pas appliqué et l'avatar de démo ZubizarettaIker a été **réellement supprimé** de la base locale. Restauré à l'identique (id, fiche, groupe) depuis l'export et les scénarios. Si le refus échoue, l'action passe : la cible doit pouvoir disparaître sans dommage.

**How to apply:** créer la cible (ex. `essai_jetable_rouge`) avec la clé de service, vérifier ses groupes, tenter l'action refusée, puis la supprimer ; vérifier en fin d'essai qu'il ne reste aucune trace (compte d'avatars identique). Voir [[feedback_tester_en_local_avant_push]].
