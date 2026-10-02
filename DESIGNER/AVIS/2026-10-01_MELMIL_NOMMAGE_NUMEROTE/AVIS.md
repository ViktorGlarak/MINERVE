# Avis DESIGNER n°20 — MELMIL : le nommage numéroté des pièces jointes (2026-10-01)

> ⚠ **Mise à jour du 2026-10-01 après-midi** (décision utilisateur) : le **NMR est devenu le code de l'incident sans points** (`0801I01`), et non plus un numéro de pièce. Le numéro de pièce ne reste que pour les demandes sans incident. R3 et R4 ne valent donc plus que pour ces demandes. Le reste de l'avis (date, aperçu, cellule, titre, export) est inchangé. Code : `app-melmil` `dea3dd6`.

**Demande utilisateur.** La règle de nommage devient `AAAAMMJJ_MR_DL26_SITCEN-GYC-NMR-titre` :
- la **date** est celle de l'**incident** : un incident prévu le 10 octobre donne `20261010`. Elle reste modifiable au besoin ;
- **GYC** est le code court de la cellule. Décision utilisateur : **GYC** pour la GREY CELL, **FOR** pour la FORAD ;
- **NMR** est le numéro de la pièce jointe : `001`, `002`… Décision utilisateur : la numérotation est **propre à chaque incident** ;
- le **titre** est saisi par l'utilisateur, proposé d'après celui de l'incident.

DESIGNER a été consulté « pour faire quelque chose de propre et cohérent ».

| # | Recommandation | Source |
|---|---|---|
| R1 | **Un aperçu du nom final, en direct**, sous chaque fichier. La personne voit exactement ce qui sera enregistré avant de déposer. | État du système visible (Nielsen 1, règle 25) |
| R2 | **La date est pré-remplie** avec le jour où l'incident est joué, dans un **champ date** (calendrier) et non en texte libre. Une mention dit « le jour où l'incident est joué — modifiable », puis « date modifiée à la main » une fois changée. | Tesler, le système pré-remplit (règle 19) ; tolérant en entrée (Postel, règle 17) |
| R3 | **Le numéro est calculé par MELMIL, affiché, jamais saisi**. Il suit le plus grand numéro déjà porté par les fichiers de l'incident, et ne descend jamais sous leur nombre. Plusieurs fichiers déposés ensemble prennent les numéros suivants dans l'ordre. Saisi à la main, il produirait des doublons. | Prévenir l'erreur plutôt que l'expliquer (Nielsen 5, REF-14) |
| R4 | **« Pièce n°003 — titre »** comme étiquette de chaque fichier : le numéro se lit avant le titre. | La forme de la donnée parle (règle 7) |
| R5 | **La cellule affiche son nom ET son code** (« FORAD (FOR) », « GREY CELL (GYC) ») : on choisit avec le nom, on retrouve le code dans le fichier. | Reconnaissance plutôt que rappel (Nielsen 6) |
| R6 | **Le titre de l'incident est proposé.** Pour une livraison de la cellule Prod ou une demande sans incident, c'est le nom du produit. Un fichier déjà nommé selon la règle garde son titre. | Tesler (règle 19) |
| R7 | **Aucune rupture pour l'existant.** À l'export, un fichier nommé librement ou selon l'ancienne règle est renommé au nouveau format, avec la date de l'incident et son rang parmi les fichiers de l'incident. Le serveur n'accepte plus que la nouvelle règle au dépôt. | Cohérence (Nielsen 4) |

**Vérifié en local** (données fictives) :
- incident 06.02.I01, joué à D+34 : date proposée `20261013` ;
- deux fichiers déjà présents sur l'incident : les deux nouveaux deviennent `…-FOR-003-Bilan-des-pertes-exagere.pdf` et `…-FOR-004-…` ;
- 289 tests, dont 11 sur le nommage.

Capture : `nommage_v2.png`. Code : `app-melmil` `4ca8bdf` (`2026-10-01.3`).
