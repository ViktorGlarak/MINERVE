# REF-22 — GOV.UK Design System : naviguer dans un service (complète REF-10)

- **Fournie par l'utilisateur le** 2026-10-06.
- **Nature** : système de design du gouvernement britannique, contenu Open Government Licence, code MIT. ⛔ On reprend les **méthodes**, jamais l'identité (police, couronne) — cf. REF-10.
- **Lu** : composants `service-navigation`, `header`, `breadcrumbs`, `back-link`, `tabs`, `summary-list`, `task-list` ; motifs `navigate-a-service`, `complete-multiple-tasks`, `question-pages`, `step-by-step-navigation`.

## À retenir
1. **Une navigation seulement si** le service est utilisé de façon répétée, a plusieurs tâches **et** pas d'ordre clair. **Un parcours linéaire n'a pas de menu** : liste de tâches ou pages successives. D'abord simplifier le parcours, ce qui supprime parfois le besoin de navigation.
2. **« La navigation n'est pas un plan du site »** : seulement les rubriques les plus utiles.
3. **Le bandeau identifie la plateforme** ; le **nom du service et ses liens** vont dans une barre de navigation de service distincte (états `current` / `active`, `aria-current`).
4. **Fil d'Ariane** seulement pour une structure à plusieurs niveaux, pas en plus d'une barre latérale ; **lien retour** sur les pages de question, **jamais avec un fil d'Ariane** ; le retour rend la page **dans l'état où on l'a laissée**.
5. **Onglets** : si les sections sont nettement nommées et que la première sert la plupart des gens ; **pas pour lire dans l'ordre ni comparer** ; « les onglets cachent du contenu, tout le monde ne les remarque pas » ; un onglet vide se **retire**, il ne se grise pas ; composant **jamais testé** en recherche utilisateur.
6. **Liste de tâches** : tâches multiples, dans l'ordre choisi, sur plusieurs sessions ; tâches nommées par un **verbe** ; statuts sobres (commencer par 2) ; **ligne entière cliquable** (on clique sur le statut).
7. **Liste récapitulative** : paires clé-valeur + « Modifier » contextualisé.
8. **Une chose par page** pour les questions ; bouton « Continuer ».
9. **Pas à pas** : parcours à début et fin traversant plusieurs services ; étapes numérotées et dépliables.

## Ce que ça change pour nos projets
- **Séparer** la barre de PLÉIADE (identité, zone, compte, changer d'app) de la navigation **propre** à chaque app.
- Les gestes **ponctuels et linéaires** (préparer un scénario, importer JEMM, rédiger un CR) : un **parcours guidé ou une liste de tâches**, pas un onglet de plus.
- Le **pilotage** répétitif (planche, veille, messagerie) : une navigation courte, réduite aux rubriques utiles.
