---
name: feedback-fichier-utilisateur-borne
description: "Un fichier importé (Excel, CSV) ne doit jamais dicter la taille d'une boucle serveur — incident Admin DELATTRE 26 du 06/10"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 699185de-99a6-4263-a321-d605be7e2b29
  modified: 2026-10-06T13:41:01.675Z
---

Tout code serveur PLÉIADE qui lit un fichier fourni par un utilisateur doit être **borné** : ne parcourir que les lignes réellement présentes (`eachRow({ includeEmpty: false })`), s'arrêter à la dernière colonne d'en-tête nommée, et plafonner taille / lignes / colonnes avec un refus clair. Jamais `for (r <= ws.rowCount)` × `cellCount`.

**Why:** le 2026-10-06, `scenario_replis contraint.xlsx` (5 lignes remplies, mise en forme jusqu'à la ligne 1 048 576) faisait construire 22 millions de cellules à l'import de l'Admin → « heap out of memory » → redémarrage en boucle, 404 pour toute la zone, programmateur coupé. `oom_kill` restait à 0 (c'est Node qui s'arrête, pas le cgroup). Correctif app-admin `9a87114`.

**How to apply:** à chaque import ou lecture de fichier (admin, eho, MELMIL/JEMM, presse…), vérifier les bornes ; un 404 intermittent d'une app = conteneur qui redémarre → chercher d'abord une requête qui épuise le processus (demander à l'utilisateur ce que faisaient les animateurs à ce moment). Lié : [[feedback-tester-en-local-avant-push]].
