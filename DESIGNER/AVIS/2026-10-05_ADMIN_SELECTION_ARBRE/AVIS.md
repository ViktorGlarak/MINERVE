# Avis DESIGNER n°64 — Admin, arbre d'un scénario : « Tout sélectionner » par partie et barre d'outils

> **Date** : 2026-10-05 · **Demandeur** : utilisateur · **Écran** : app-admin › Scénarios › un scénario › Arbre (`src/components/editor/TreeView.tsx`)
> DESIGNER **propose**, il ne tranche pas (MEMOIRE §1). Le besoin exprimé fait foi.

## Besoin

« Le bouton Sélection existe, mais pas Tout sélectionner. Parfois on voudrait sélectionner 100 % des tweets sans sélectionner les articles de presse. » Et : « revoir l'architecture des boutons à cet endroit pour faire un truc propre ».

## Constats (heuristiques de Nielsen, REF-14 — gravité 0 à 4)

| # | Constat | Heuristique | Gravité |
|---|---|---|---|
| C1 | Aucun moyen de tout cocher : pour supprimer 60 tweets il faut 60 clics. | 7 — flexibilité et efficacité | **3** |
| C2 | La seule unité qui a du sens pour l'utilisateur (« les tweets », « la presse ») est la **partie d'app** de l'arbre, mais elle n'a aucune case. | 2 — correspondance avec le monde réel | 3 |
| C3 | En mode Sélection, rien ne s'affiche tant qu'aucune ligne n'est cochée : on ne sait pas ce que le mode attend ni comment en sortir. | 1 — état du système visible ; 6 — reconnaître plutôt que se souvenir | 2 |
| C4 | « Supprimer » (destructif) est au milieu de la barre, entre les décalages et le texte d'aide ; « Tout désélectionner » est un lien discret tout à droite. | 5 — prévention des erreurs | 2 |
| C5 | La barre du haut mélange trois rôles sans séparation : chercher/filtrer, présenter (replier), agir (sélection). | 8 — design minimaliste ; proximité (REF-07, REF-06) | 1 |
| C6 | Pas de sortie au clavier du mode Sélection. | 3 — contrôle et liberté | 1 |

## Recommandations (classées par gain)

**R1 — Une case « tout sélectionner » sur l'en-tête de chaque partie d'app** *(gain fort, effort faible)*.
En mode Sélection, l'en-tête de chaque app porte une case à **trois états** (vide / partielle / pleine) suivie du libellé « Tout » et du nombre. Elle coche **toutes les publications de cette app qui passent la recherche et le filtre de statut**, y compris les réponses repliées et une partie repliée, en excluant celles « en cours de publication » (non sélectionnables). L'état partiel (`indeterminate`) dit qu'une partie seulement est cochée. — *Fitts (REF-06) : la case est là où l'on regarde la partie ; Jakob (REF-06) : la case maîtresse de liste est un usage universel (messageries, Gmail, Carbon DataTable REF-12).*

**R2 — Une barre de sélection toujours visible en mode Sélection** *(gain fort, effort faible)*.
Dès qu'on entre en mode Sélection, la barre apparaît, même vide, avec à gauche une case « Tout » pour **tout ce qui est affiché** (toutes apps) et le compte, et un texte qui dit quoi faire quand rien n'est coché : « Cochez des publications, ou une app entière avec sa case. » — *Nielsen 1 et 6 ; Peak-End (REF-06) : soigner l'état vide.*

**R3 — Ordonner la barre de sélection : quoi → comment → danger → sortie** *(gain moyen, effort faible)*.
Gauche : case Tout + compte (« 12 sélectionnés sur 58 »). Centre : actions sur brouillons (Décaler, Publier maintenant), suivies de leur limite (« ne concernent que les brouillons »). Droite : **Supprimer** en rouge, isolé par un séparateur, puis **« Terminer »** qui quitte le mode. La case Tout remplace le lien « Tout désélectionner ». — *Hick : grouper par rôle ; prévention des erreurs : le destructif à l'écart (Nielsen 5) ; proximité (REF-07).*

**R4 — Barre du haut en trois groupes** *(gain moyen, effort faible)*.
① Trouver : recherche + filtre de statut. ② Présenter : Tout replier / Tout déplier. ③ Agir, poussé à droite : « Sélectionner » (bouton bascule ; appuyé, il se lit « Sélection active »). Un filet vertical sépare les groupes. — *Proximité et alignement (REF-07) ; une seule action principale (REF-01).*

**R5 — Clavier** *(gain faible, effort minime)*.
`Échap` quitte le mode Sélection (et vide la sélection) quand aucune fenêtre n'est ouverte ; les cases d'en-tête sont de vraies cases (`<input type=checkbox>`, `aria-checked="mixed"` via `indeterminate`), libellées « Tout sélectionner sur <app> ». — *REF-02, REF-13 (2.1.1, 4.1.2).*

## Ce que l'avis ne change pas

Le comportement des actions (décaler, publier, supprimer), les confirmations existantes, le glisser-déposer et l'ordre des parties.

## Suite

Appliqué dans app-admin le 2026-10-05 (branche `selection-par-partie`), à valider par l'utilisateur avant mise en ligne.
