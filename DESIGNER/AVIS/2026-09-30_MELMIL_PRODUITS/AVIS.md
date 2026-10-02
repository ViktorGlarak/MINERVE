# Avis DESIGNER n°15 — MELMIL : médias des incidents et demandes de produit complexe (2026-09-30)

**Besoin utilisateur.** Sur certains incidents, il faut des images, des vidéos ou des sons. FORAD et GreyCell les font souvent eux-mêmes avec les IA en ligne. Ce qu'elles ne savent pas faire, ils le demandent à la cellule « Prod », qui travaille sous Photoshop, en montage, etc. Il faut, sur chaque incident :
- voir les fichiers qui s'y rattachent ;
- pouvoir en importer ;
- un bouton **« Demande de produit complexe »** ;
- et que la cellule Prod livre le produit fini dans l'incident.

La base du formulaire est « Demande-InfoG vierge.docx » (ORION 26, sans marquage de diffusion), à remanier.

**Décisions de l'utilisateur :**
- un **rôle « Prod »** coché sur le bouclier de l'instance ;
- l'**import ouvert à tous les animateurs** ;
- 500 Mo par fichier ;
- ⭐ **aucune fiche Word** : « un seul et même outil », rien à exporter ni à importer.

**Ce qui fait foi :** le besoin exprimé ci-dessus et le formulaire InfoG (ses 4 parties). DESIGNER propose la forme.

## Recommandations (appliquées)

| # | Recommandation | Source |
|---|---|---|
| R1 | **Les fichiers de l'incident d'abord, en vignettes** (aperçu pour les images, genre écrit pour vidéo et son), avec les deux gestes juste à côté : « Importer des fichiers » et « Demande de produit complexe ». Un état vide qui dit quoi faire. | Proximité (REF-06) ; états vides (REF-07) |
| R2 | **« Complexe » se mérite** : le champ « Pourquoi une IA en ligne ne suffit pas » est **obligatoire**, avec des exemples (visage à garder, logo exact, montage de sources, voix, durée). L'aide du bouton le rappelle. | Tesler : on dit ce qu'on attend (REF-06) |
| R3 | **Ce que MELMIL sait est déjà écrit** : incident, date de jeu, demandeur (grade, nom, cellule tirés de l'Équipe), émetteur, cible, message (= effet attendu), échéance (= moment où l'incident est joué). On complète, on ne recopie pas. | Tesler (REF-06) ; pré-remplir (§3.4 n°19) |
| R4 | **Un statut = un mot ET une couleur**, jamais la couleur seule. Le fond est clair, pour rester lisible aussi sur la barre sombre de la fiche. | WCAG 1.4.1 (REF-13) ; REF-07 |
| R5 | **La cellule Prod a SA file** (onglet « Demandes de produit ») : triée par échéance, avec les **retards écrits en toutes lettres**, des filtres par statut (« À traiter » par défaut) et un compteur des demandes qui attendent. | Hick : moins de choix (REF-06) ; état visible (Nielsen 1, REF-14) |
| R6 | **Erreurs à la GOV.UK** : un résumé en tête, qui reçoit le focus ; chaque manque est un lien vers son champ ; les champs facultatifs sont marqués « (facultatif) ». | REF-10, REF-14 (heuristique 9) |
| R7 | **Un seul outil** : la demande, son suivi et la livraison vivent dans MELMIL, sans fiche Word. | Décision utilisateur |
| R8 | Le formulaire InfoG est **remanié**, pas recopié. Les 4 parties sont gardées (produit, intention, contenu, direction artistique). Les listes ont été revues pour l'exercice : faux document, style « propagande », « amateur / pris sur le vif », ton « menaçant »… Les champs fournis sont cochés parmi les fichiers de l'incident, au lieu d'un « joindre les fichiers ». | Jakob : faire comme l'habitude du terrain (REF-06) |

## Vérifications
- Parcours complet en local, sur une base d'essai à données fictives : fiche vide → dépôt de 2 fichiers → demande pré-remplie → envoi incomplet (résumé de 2 erreurs) → envoi → Prod : « En cours », dépôt du produit fini, « Marquer livrée » → médias de l'incident (« Produit Prod · DP-01 ») → onglet de la file.
- Sans le rôle Prod, le changement de statut est **refusé par le serveur** (403), alors que compléter le formulaire reste permis.
- 0 débordement au téléphone, aucune erreur de page, 241 tests OK.
- Captures : `captures\01…09`.
