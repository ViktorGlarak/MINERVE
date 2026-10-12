---
name: feedback-modele-officiel-identique
description: "« Reproduire à l'identique » un modèle officiel (CR, fiche) = partir du FICHIER d'origine comme gabarit d'export et copier sa mise en page réelle, pas la redessiner en grille ; vérifier avec un exemplaire rempli"
metadata:
  type: feedback
---

Quand l'utilisateur demande de remplacer un modèle de compte rendu par un document fourni « à l'identique », **reprendre le fichier d'origine lui-même** (converti en .docx par LibreOffice si .odt) comme gabarit d'export, et redessiner l'écran d'après SA mise en page (cadres, intitulés suivis de la réponse, cases à cocher Word…). Ne pas le réinterpréter en grille « intitulé | case ».

**Why :** le 2026-10-04, ma 1re version du SCAMER (grille de 3 colonnes) « n'y ressemblait pas totalement » ; l'utilisateur a dû fournir un exemplaire rempli pour que je comprenne (réponses à la suite des intitulés, 6 cadres, FORMCHECKBOX). Refait en 2026-10-04.17.

**How to apply :** rendre le modèle en PDF/PNG et le regarder AVANT de coder ; lister sa structure XML (tables, paragraphes, champs) ; demander/chercher un exemplaire rempli pour la logique de remplissage ; vérifier le marquage de chaque fichier fourni ([[feedback-marquages-diffusion]] — le rempli SCAMER était DR) ; garder l'ancienne version lisible pour les données déjà saisies ; tester un aller-retour export → import et l'ENREGISTREMENT côté serveur (le filtre `relireAtelier` jetait les clés nommées).
