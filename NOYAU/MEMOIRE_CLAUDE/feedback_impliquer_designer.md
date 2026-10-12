---
name: feedback_impliquer_designer
description: "Sur tout sujet d'ergonomie / visuel / compréhension d'un écran, faire TRAVAILLER l'agent DESIGNER (sous-agent avec sa consigne et sa mémoire), pas seulement lire sa mémoire"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 699185de-99a6-4263-a321-d605be7e2b29
  modified: 2026-10-07T15:08:47.458Z
---

Sur toute demande d'ergonomie, de visuel ou de compréhension d'un écran PLÉIADE, **l'agent DESIGNER doit être impliqué** : lancer un sous-agent qui lit `SYSTEME\PROMPTS\designer.md` et `DESIGNER\MEMOIRE.md`, relit ou produit la proposition, rédige son avis (`DESIGNER\AVIS\<date>_<sujet>\AVIS.md`) et ajoute sa ligne au tableau des avis. Claude peut contribuer (maquette, code), mais l'avis est celui de DESIGNER.

**Why:** le 2026-10-07 (liste des scénarios de l'app-admin), l'utilisateur : « pense à faire cela avec l'agent IA DESIGNER, j'espère que t'as eu le réflexe » puis « tu peux contribuer mais je veux que l'agent DESIGNER soit impliqué ». J'avais seulement lu sa doctrine. Sa relecture a ensuite changé des choix importants (« Lancé » au lieu de « En cours », un seul mot « à corriger », filtre de cellule de l'avis n°56).

**How to apply:** dès qu'un écran est jugé « brouillon », peu clair ou à améliorer : maquette (localhost si demandé) → sous-agent DESIGNER en relecture → intégrer ses recommandations en citant qui propose quoi → points à trancher par l'utilisateur. Voir [[agent_designer]].
