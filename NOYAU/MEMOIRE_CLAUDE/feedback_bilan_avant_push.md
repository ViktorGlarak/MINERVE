---
name: feedback-bilan-avant-push
description: Avant tout push d'une app PLÉIADE sur main ou prod, faire le bilan (problème résolu + résultats des tests) et attendre le feu vert explicite de l'utilisateur
metadata:
  type: feedback
---

Avant de pousser une app PLÉIADE sur `main` ou sur `prod` (même avec la permission technique de le faire), je présente d'abord à l'utilisateur :
1. **le bilan de la résolution** : la cause trouvée, ce que le correctif change, ce qu'il ne traite pas ;
2. **le bilan des tests** : ce qui a été essayé (tests, essai sur vraie base, cas couverts), avec les résultats, et ce qui n'a pas pu être vérifié ;
puis **j'attends sa réponse explicite** (« oui, tu peux pousser ») avant tout `git push` vers `main` ou `prod`. Les dépôts MINERVE (documentation, mémoires) ne sont pas concernés : ils se poussent après chaque avancée, comme le prévoit `SYSTEME/DEUX_POSTES.md`.

**Why:** le 2026-10-16, l'utilisateur a ajouté la permission `git push origin main:prod` ; j'ai alors poussé deux fois Social en production sans bilan préalable. Le premier push (`e0640ce`, comptes `op-…`) a cassé la connexion de l'utilisateur (boucle sur « Se connecter », adresse e-mail déjà portée par un autre compte) ; il a fallu un second correctif (`107260c`), poussé lui aussi sans attendre. L'utilisateur a demandé de « reprendre les bonnes habitudes ».

**How to apply:** la permission technique ne vaut pas accord. Pour chaque correctif d'app : coder → tester (dont essai sur vraie base quand la base est en jeu, et le chemin de connexion s'il est touché) → message de bilan (résolution + tests + ce qui reste non vérifié + rappel de mettre en pause les scénarios si besoin, cf. [[pleiade-push-prod-auto]]) → attendre « oui » → pousser `main` puis `prod`. Voir aussi [[feedback-tester-en-local-avant-push]].
