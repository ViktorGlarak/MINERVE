---
name: pleiade-push-prod-auto
description: Un push sur la branche prod met à jour tout seul les instances de DELATTRE 26 (pas de « Déployer » à demander) ; prévenir de la pause des scénarios avant le push
metadata:
  node_type: memory
  type: project
  originSessionId: 699185de-99a6-4263-a321-d605be7e2b29
  modified: 2026-10-06T10:26:55.820Z
---

Constaté le 2026-10-06 : après un push `main` + `prod`, les instances de la zone DELATTRE 26 se mettent à jour **d'elles-mêmes** en quelques minutes (eho passé de 2026-10-05.4 à 2026-10-06.1 sans action de l'utilisateur ; MELMIL toujours sur la dernière version poussée). L'utilisateur l'a confirmé : il n'a jamais eu à redéployer.

**Why:** une note du 2026-10-01 (notes de version presse) disait qu'une zone non-`prod` n'était pas mise à jour par la promotion et qu'il fallait « Déployer » chaque instance — c'est périmé. J'ai fait faire des étapes inutiles à l'utilisateur toute la journée du 06/10.

**How to apply:**
- Après un push, ne plus demander de « Déployer » ; vérifier la mise en ligne par `/api/sante` (eho, MELMIL) quelques minutes après.
- Le redémarrage arrive donc **automatiquement** peu après le push : pour le réseau social et l'admin (planificateur), conseiller de **mettre en pause les scénarios qui publient dans les minutes à venir AVANT de dire « push »**, puis de les reprendre (une publication échue pendant la coupure passe en « Erreur », sans nouvelle tentative).
- Lié : [[feedback_tester_en_local_avant_push]], [[feedback_indicateur_etat]].
