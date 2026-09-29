# Avis DESIGNER n°7 — MELMIL, planification : choisir les ETIM d'un incident

> **Date** : 2026-09-25 · **Demande** : à la création d'un incident, choisir les ETIM concernées (« ETIM 27 », « ETIM 9 » pour les régiments ou les brigades), et voir leurs noms sur la carte de l'incident dans la planification.

## Solution retenue

**R1 · Une liste d'ETIM par exercice, pas une saisie libre par incident.**
La saisie libre produit des variantes qui ne se regroupent plus (« ETIM 27 », « ETIM 27 BIM », « ETIM 27 BIM ou 9 BIMa » dans le JEMM fictif de DE LATTRE 26). La liste se gère dans Réglages : ajouter, renommer (le nouveau nom suit sur les incidents), retirer (avec confirmation et le nombre d'incidents touchés) *(Postel : tolérant en entrée, strict en sortie — règle 17)*.

**R2 · Dans la fiche, une pastille par ETIM, cochée d'un toucher.**
C'est plus rapide qu'une liste déroulante multiple, et on voit tout d'un coup d'œil *(Hick, règle 16)*. Une pastille cochée est pleine, dans la teinte de la Planification, et porte un « ✓ » ; une pastille libre est cerclée et porte un « + ». L'état ne tient donc pas à la seule couleur *(règle 10)*. Hauteur 32 px, au-dessus du seuil de 24 px *(règle 12)*. `aria-pressed` pour les lecteurs d'écran.

**R3 · « Autre ETIM… » sur place.**
Une ETIM qui manque s'ajoute depuis la fiche, sans passer par Réglages, et arrive cochée *(Tesler, règle 19)*.

**R4 · Le nom en clair sur la carte de la planche.**
Une étiquette sombre par ETIM, sous le sujet. Elle reste lisible sur toutes les couleurs de storyline, en style clair comme en classique. Les mêmes étiquettes, dans la teinte de l'espace, apparaissent dans le tableau des incidents et dans la liste par jour (téléphone).

**R5 · État vide qui dit quoi faire** : « Aucune ETIM déclarée pour l'exercice : saisissez la première ci-dessous » *(règle 18)*.

## Ce qui n'a pas été fait (à proposer si le besoin se confirme)

- Un **filtre par ETIM** sur la planche.
- Une **couleur par ETIM** : écarté pour l'instant, car la couleur des cartes porte déjà la storyline (Von Restorff, règle 20).
