# Avis DESIGNER n°9 — eho : ranger 235 groupes

> **Date** : 2026-09-28 · **Demande** : « 235 groupes, c'est incompréhensible » — les diminuer drastiquement, sans rien casser dans les autres applicatifs.

## Constat
Moins de 15 groupes servaient à DE LATTRE 26. Le reste :
- **49 groupes de classement** pays × catégorie, doublons des champs `pays` et `label` que l'écran Avatars range déjà ;
- **180 groupes d'autres exercices** (ORION 26 phases 2 et 4, AURIGE…), venus avec l'import du réseau social.

La liste violait la hiérarchie (règle 5) et la loi de Hick (règle 16) : 235 choix identiques.

## Solution retenue

**R1 · Masquer, ne pas supprimer** *(prévention des erreurs, heuristique 5 ; réversibilité)* : un groupe « archivé » disparaît des écrans d'eho, mais garde tout (id, nom, membres, camps). Les autres applications le voient toujours. Supprimer aurait cassé l'incarnation, les likes d'app-admin et la rédaction d'app-press.

**R2 · Un assistant qui propose, l'humain qui valide** *(Tesler, règle 19)* : le tri est pré-rempli par famille, avec la raison de chaque proposition et un avertissement quand un groupe de classement contient des membres que les filtres ne retrouveraient pas. On peut tout garder ou tout archiver par famille, ou décocher ligne par ligne.

**R3 · Le résultat avant d'appliquer** *(Nielsen 1, règle 25)* : « Après rangement : 6 groupes visibles, 229 archivés ».

**R4 · Aucune supposition invisible** : l'exercice en cours n'est deviné que si le nom de la zone le désigne. Sinon, il se choisit, et « Appliquer » reste bloqué tant que ce n'est pas fait. Un premier essai avait choisi ORION 26 au lieu de DE LATTRE 26.

**R5 · Les archives restent à portée** *(reconnaître plutôt que se souvenir, Nielsen 6)* : une section repliée en bas de page, fouillée par la recherche, avec « Ressortir » d'un clic. Dans la fiche d'un avatar, ses groupes archivés restent affichés, et un lien montre les autres.

## Résultat mesuré (base DE LATTRE fusionnée, en local)
235 → **6 visibles** (3 camps, Exercice DE LATTRE 26, Réseau RZO, STARTEX). Groupes et appartenances intacts (235 groupes, 5 297 appartenances). Aucun débordement au téléphone.
