# Avis DESIGNER n°13 — MELMIL, « Confié à » par groupes

> **Date** : 2026-09-28 (soir) · **Règle métier fixée par l'utilisateur** :
> - un **event** est confié à un groupe de premier niveau (GREYCELL, FORAD…) ;
> - une **storyline**, à un sous-groupe du groupe de son event ;
> - un **incident**, à des personnes de ce sous-groupe. Si personne n'est coché, c'est **tout le sous-groupe** qui le gère.

## Solution retenue

**R1 · Le choix proposé suit la hiérarchie** *(Hick, règle 16 : moins de choix, les bons)* :
- l'event ne propose que les groupes de premier niveau ;
- la storyline, que les sous-groupes du groupe de son event ;
- l'incident, que les personnes de ces sous-groupes.

On ne peut pas se tromper de niveau.

**R2 · Des pastilles qu'on coche d'un clic, dans la couleur du groupe**, avec « ✓ » ou « + » en plus de la couleur *(règle 10)*. C'est le même geste que pour les ETIM *(Jakob, règle 15)*.

**R3 · Dire ce que signifie « rien de coché »** *(Nielsen 1, règle 25)* : sous les pastilles de l'incident, une ligne d'état écrit « → Tout le sous-groupe DEV / PROD gère l'incident. », ou « → 1 personne désignée. ». On ne laisse pas deviner une règle implicite.

**R4 · Un état vide qui dit quoi faire, au bon endroit** *(règle 18)* :
- « Confiez d'abord l'event 08 à un groupe (onglet Events) » ;
- « Le groupe de l'event n'a pas encore de sous-groupe : créez-en dans l'onglet Équipe ».

**R5 · Ne rien perdre en changeant de règle** : l'ancienne attribution par personnes reste affichée, en petit, avec « Effacer », tant qu'on ne l'a pas retirée.

**R6 · Voir le résultat partout où il sert** :
- une colonne « Confié à » dans le tableau des incidents, masquée au téléphone ;
- le sous-groupe dans l'en-tête de chaque storyline ;
- dans la fiche d'une personne, ce qui lui revient : events, storylines, incidents.
