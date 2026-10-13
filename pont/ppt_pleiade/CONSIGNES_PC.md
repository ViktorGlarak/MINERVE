# Refonte du diaporama « PLÉIADE » pour l'officier — à terminer sur le PC (2026-10-13)

> Commencé sur le Mac, **à terminer sur le PC** : Keynote ne s'est pas laissé piloter depuis la session Mac, et il n'y a ni PowerPoint ni LibreOffice sur le Mac. **Le rendu visuel n'a donc pas été vérifié.** Le fichier .pptx est valide : python-pptx le relit, 11 diapositives.

## 1. La demande de l'utilisateur
L'officier qui va présenter PLÉIADE a reçu un diaporama de 10 diapositives :
`smb://fichiers.delattre-26.pleiade.internal/delattre-26/greycell/PLÉIADE, simuler l'espace informationnel d'un exercice.pdf`

L'utilisateur demande deux choses :
1. le refaire, **beaucoup plus propre**, avec **DESIGNER** ;
2. **analyser les données** pour que tout soit exact.

## 2. Ce qui est fait (Mac)
- **Avis DESIGNER n°107** : `DESIGNER/AVIS/2026-10-13_PPT_PRESENTATION_PLEIADE/AVIS.md` (diagnostic, direction de refonte, plan en 11 diapositives). À lire en entier avant de toucher au deck.
- **Décisions de l'utilisateur** sur les questions de DESIGNER :
  1. **Charte PLÉIADE** (piste A) : fond clair `#F3F0E7`, sombre `#161719` pour 3 temps forts seulement (couverture, diapo 7 « 105 », conclusion), une seule emphase graphite `#1B1C1F` / craie `#EDE3C8`, angles vifs, pas d'ombre.
  2. **Dernière diapositive informative**, sans demande aux décideurs.
  3. **Illustrations marquées « ILLUSTRATION · données fictives »** pour la courbe d'opinion et les écrans. Aucune donnée réelle.
  4. **Livraison en PowerPoint (.pptx modifiable, avec notes de l'orateur) et en PDF de secours.**
- **Deck généré** : `PLEIADE/PRESENTATION/PLEIADE_presentation_v2.pptx`, produit par `pont/ppt_pleiade/construire.py` (python-pptx). Pour le régénérer :
  ```
  pip install python-pptx
  py pont\ppt_pleiade\construire.py PLEIADE\PRESENTATION\PLEIADE_presentation_v2.pptx
  ```
  - Police **Arial**, le repli d'Archivo prévu par DESIGNER. python-pptx ne sait pas incorporer de police, et Archivo est sans doute absente du poste de projection.
  - Corps 20-24 pt, légendes 16-18 pt, titres-messages 32 pt.
  - Grille de DESIGNER (960 × 540 pt) ; textes détaillés dans les **notes de l'orateur**.
- **Analyse des données** : erreurs trouvées dans le PDF de l'officier, et corrigées dans le nouveau deck et dans `PLEIADE/PRESENTATION/PLEIADE_DOSSIER_DE_PRESENTATION.md` § 6.5.
  1. ❌ **p. 8, « > 1 000 lectures pour 138 messages de joueurs »** : présenté comme une réussite, alors que la source (`PLEIADE/JOURNAL.md`, 2026-10-12 suite 18) est un **diagnostic de défaut**. Seules **4 publications de joueurs sur 42** avaient reçu une réponse de l'IA, défaut corrigé le jour même (app-ia 12.15). **Retiré.** L'erreur venait du dossier rédigé sur le Mac, corrigé depuis.
  2. ❌ **p. 8, « ≈ 37 % des événements »** : mesure sur **24 minutes** seulement (avis PSYCHOLOGUE n°18, « le chœur de la solidarité », 15 réponses sur 16 faites de formules). **Retiré.**
  3. ❌ **p. 9, « libre de droits (Gemma 4) »** : faux. C'est une **licence libre** (Apache 2.0), ce qui n'est pas la même chose. Corrigé.
  4. ⚠ **p. 7, « 105 avatars, citoyens de l'Arnland »** : en réalité **100 citoyens** de l'Arnland (15 / 70 / 15 %), **3 avatars de test et 2 relais mercuriens**. Corrigé.
  5. ⚠ **p. 6, « Avant (ORION à MINOTAURE) : pages HTML diffusées par mail en ZIP »** : ORION avait un serveur (MASTORION) ; le ZIP concerne AURIGE 2BB et MINOTAURE. Corrigé en « Avant (AURIGE 2BB, MINOTAURE) ».
  6. Défauts typographiques relevés par DESIGNER : chiffres coupés (« > 1 / 000 », « ≈ 37 / % »), tiret cadratin en p. 1. Les nombres du nouveau deck utilisent des espaces insécables.
  7. ⚠ **p. 3, « Admin »** : le nom à l'écran de la console est « **Animation** ». Corrigé.
  8. ✅ Vérifiés et conservés : les 4 arguments ; la frise (avril → octobre) ; environ 4 000 avatars dans l'EHO ; 36 nuances d'émotion ; le rédacteur et les nuances **en essai** ; parc PC + Mac (branché le 13/10) ; 11 guides de l'ANSSI ; « être sur le VPN ne donne aucun droit ».

## 3. Ce qu'il reste à faire sur le PC (dans l'ordre)
1. `git pull`, puis lire l'avis DESIGNER n°107 et ce fichier.
2. **Ouvrir `PLEIADE_presentation_v2.pptx` dans PowerPoint** et faire la **revue visuelle de chaque diapositive**. Points à surveiller en priorité, car jamais vus rendus :
   - texte qui déborde de sa boîte ou chevauche un schéma (diapos 3 « frise », 5 « zone », 6 « flux », 8 « programme / IA ») ;
   - diapo 3 : la frise (pointillés puis trait plein, étiquettes au-dessus et au-dessous de l'axe), dont les traits verticaux peuvent être mal placés ;
   - diapo 8 : la barrière de garde-fous et le mot « Publié » à droite ;
   - diapo 9 : le graphique natif (courbe illustrative de −100 à +100, ligne verticale « message des joueurs ») ;
   - diapo 7 : la barre 15 / 70 / 15 et ses étiquettes ;
   - aucun chiffre coupé sur deux lignes ; au plus 40 mots par diapositive (le reste va dans les notes).
3. **Corriger** dans `construire.py` (de préférence) ou directement dans PowerPoint, puis régénérer.
4. **Faire relire le rendu par DESIGNER** sur les images exportées (avis n°107, contrôles de fin).
5. **Si Archivo est installée** sur le poste de projection, elle peut remplacer Arial (charte complète). Sinon, garder Arial.
6. **Exporter le PDF de secours** depuis PowerPoint.
7. **Déposer les deux fichiers** (.pptx et .pdf) **là où l'utilisateur l'indiquera**, a priori à côté de l'original sur le partage `greycell` de DELATTRE 26, sous un nouveau nom, **sans écraser le PDF de l'officier**.
8. Consigner :
   - dans `DESIGNER/MEMOIRE.md` : l'avis n°107 appliqué ;
   - dans `PLEIADE/JOURNAL.md` : la refonte du support de présentation ;
   - puis commit `[PC]`, pull et push.

## 4. Plan du nouveau deck (11 diapositives, titres-messages)
1. *(sombre)* PLÉIADE · L'espace informationnel d'entraînement du CECPC (motif constellation)
2. La lutte informationnelle se joue en ligne : PLÉIADE la reproduit en vase clos (périmètre fermé, porte VPN, 4 piliers)
3. Six mois, quatre exercices : chaque manque a produit un outil (frise ; pointillés pour l'époque ZIP, trait plein pour le serveur)
4. D'un ZIP envoyé par mail à une plateforme unique, mise à jour en direct (avant / après, 5 lignes)
5. Une zone par exercice : les applications à la carte, une seule identité partout (schéma de zone, barre EHO)
6. Du plan JEMM à l'écran des joueurs, dans un seul circuit (6 étapes fléchées)
7. *(sombre)* Nouveauté DELATTRE 26 : un espace informationnel qui réagit (« 105 », barre 15 / 70 / 15)
8. Le programme tient la psychologie ; l'IA ne fait que lire et formuler (schéma IA, programme, IA, puis garde-fous)
9. Pour la première fois, on voit l'effet d'une action de joueur sur l'opinion (courbe ILLUSTRATIVE + ce que suit le COCKPIT)
10. Fermé, local, réparti : rien ne sort de la salle (VPN, serveur, nœuds de calcul)
11. *(sombre)* Ce que PLÉIADE permet (4 verbes et la suite : en essai, à l'étude, ensuite)
