---
description: Rituel de DÉBUT de session de travail MINERVE (vault)
---

Je commence ma session de travail sur le projet **MINERVE**. Exécute le **rituel de démarrage du vault** (cf. `vault/CLAUDE.md`) :

0. **Synchronise (deux postes, cf. `SYSTEME/DEUX_POSTES.md`)** : `git pull --rebase`. Résume en 1-2 lignes les commits arrivés de l'autre poste (`git log --oneline ORIG_HEAD..HEAD`, étiquettes `[PC]` / `[MAC]`). En cas de conflit, applique la section 3 de `DEUX_POSTES.md` avant toute autre chose. Si `SYSTEME/DEUX_POSTES.md` § 5 n'est pas encore coché et que tu es sur le PC pro, propose de faire la migration.
1. **Charge le contexte** : lis `vault/INDEX.md` (notes **tier 1** en priorité). Si je t'indique un domaine précis (mastaurige, bothnia, arnland, mercure, production…), lis aussi `vault/context-packs/PACK-<domaine>.md`.
2. **Reprends le fil** : trouve la note la plus récente de `vault/daily/` (par date dans le nom) et **résume-moi sa section « ⏭️ Prochaine étape »**.
3. **Crée la daily du jour** : calcule la date du jour (AAAA-MM-JJ). Si `vault/daily/<date>.md` n'existe **pas**, crée-le depuis `vault/templates/daily-note.md` en remplaçant la date et l'`id` (`DAILY-<date>`). S'il existe déjà, n'y touche pas.
4. **Synthèse de reprise** : dis-moi en 3-4 lignes **où on en était** et **ce qui est prévu**, puis **attends mes instructions**. Ne lance aucune production tant que je n'ai pas précisé la tâche du jour.
