---
name: feedback-fermer-clic-exterieur
description: "Règle d'ergonomie PLÉIADE — toute fenêtre ou liste ouverte par un bouton se ferme d'un clic à l'extérieur (et Échap)"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 699185de-99a6-4263-a321-d605be7e2b29
  modified: 2026-10-09T05:34:49.351Z
---

Toute fenêtre, popover ou liste déroulante ouverte par un bouton doit se fermer d'un **clic à l'extérieur** (et à la touche Échap), sans obliger à recliquer sur l'icône.

**Why:** demande de l'utilisateur le 2026-10-09 sur le réseau social (« il m'est obligé de recliquer sur l'icône pour fermer cette fenêtre »).

**How to apply:** pour toute nouvelle fenêtre dans une app PLÉIADE : `p-dialog` avec `[dismissableMask]="true"` ; popover maison avec un écouteur `document:click` (fermer si la cible n'est pas dans le conteneur) + `document:keydown.escape`. Vérifier en essai navigateur (clic à côté → fermé). Lié : [[feedback-impliquer-designer]].
