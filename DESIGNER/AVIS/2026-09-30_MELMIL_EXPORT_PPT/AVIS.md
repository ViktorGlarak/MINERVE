# Avis DESIGNER n°17 — MELMIL : export PowerPoint pour les autorités (2026-09-30)

**Demande utilisateur.** Tout se crée dans MELMIL. Une fois le travail fini, ou après des modifications, il faut pouvoir l'exporter **au format du PowerPoint de montage**, pour le transmettre aux autorités, et que celles-ci voient les modifications. Plusieurs diapositives par storyline sont admises pour tout faire tenir.

**Ce qui fait foi** : le PPT d'origine, `EXER\DELATTRE 26\01_Montage exercice\20260909 - GREY CELL_MAIN v4.pptx`, pages 1 à 10. Il ne porte aucun marquage de diffusion réel. Il a été mesuré avec python-pptx et rendu par PowerPoint. DESIGNER **ne change pas le format** : il ajoute ce qui aide à la relecture.

## Reprise fidèle
- Format 16:9, 33,87 × 19,05 cm ; police Calibri.
- **Page 1, synthèse** : tableau STORYLINE / COORDINATION / JEMM, en-tête bleu, lignes bleu clair alternées.
- **Page 2, chronologie** : bandeau phases / D+ / dates, **une ligne par storyline**, ses périodes en barres vertes côte à côte.
- **Fiche par storyline** :
  - bandeau bleu « EXERCICE – EVENT … / STORY LINE NMR 06-01 » et sous-titre jaune « STORYLINE : … » ;
  - bandeau des jours coloré par phase, avec **★** sur les jours d'incident ;
  - encadrés noirs à gauche : description, effets attendus, objectifs principal et secondaires ;
  - QUI / OÙ / QUAND ;
  - tableau INCIDENT / QUAND / QUI / PAR QUI / QUOI (le QUOI porte le sujet en gras, la description, puis « ➢ » l'effet attendu en rouge) ;
  - légende TO BE COORDINATED / COORDINATED et cadre EXCON COORDINATION REQUIRED colorié.

## Recommandations (appliquées)

| # | Recommandation | Source |
|---|---|---|
| R1 | Un seul bouton, **« Exporter en PPT »**, dans l'en-tête de l'atelier, visible depuis tous les onglets. | Jakob, Hick (REF-06) |
| R2 | **Deux choix seulement** : le périmètre (tout, ou un event) et, facultatif, **« signaler les changements depuis le … »**, pré-rempli avec la date du dernier export de ce poste. | Hick ; Tesler (REF-06) |
| R3 | **Les changements sautent aux yeux** : liseré rouge à gauche de la ligne, mention **NOUVEAU** ou **MODIFIÉ**, marque sur la fiche et dans la synthèse, et une **diapositive de récapitulatif** en tête. C'est ce que l'autorité doit relire en premier. | Von Restorff (REF-06) ; Nielsen 1 |
| R4 | **Annoncer avant d'exporter** : « 4 storylines, 11 incidents, 15 changements depuis le 30/09/2026 ». | Nielsen 1 (REF-14) |
| R5 | **Une storyline trop chargée continue** sur (1/2), (2/2)…, chaque page avec le même bandeau et les mêmes encadrés : aucun tableau ne déborde. | Demande utilisateur ; lisibilité (REF-07) |
| R6 | Un pied de page discret : « Export MELMIL — exercice — date », avec la légende du rouge. | Nielsen 1 |

## Vérifications
- Le fichier produit **par le navigateur** s'ouvre dans PowerPoint : 7 diapositives, rendus `diapo_1…7.png`. L'exemple, sur données fictives, est dans `EXEMPLE_export_donnees_fictives.pptx`.
- ⚠ **Piège trouvé** : un morceau de texte **vide** suffit pour que PowerPoint déclare le fichier « endommagé », alors que python-pptx l'ouvre. On valide toujours un export PPT **dans PowerPoint lui-même**.
- 12 tests (jours, phases, étoiles, périodes, périmètre, changements, JEMM, pagination) ; 271 tests au total ; l'image a été reconstruite comme sur le serveur.
