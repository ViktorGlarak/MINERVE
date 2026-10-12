# Avis n°68 — app-admin : corps d'article « Mise en forme | HTML » (2026-10-06)

**Demande utilisateur** : dans la fenêtre d'un item de presse, pouvoir écrire le corps de l'article soit en HTML, soit « en basique » avec des boutons (gras, italique…), comme sur un forum. Prototype montré en local.

## Constat
- Le corps était un simple champ texte. Le journal accepte déjà du HTML (`asHtml` le laisse passer s'il contient des balises, puis `cleanHtml` l'assainit) : seul l'admin change.
- Risque propre au terrain : des corps collés depuis les sites d'exercice portent des **encadrés de maquette** (`class="figures-box"`, `ops-box`, `decree-box`…), des images, des tableaux. Un éditeur visuel les **efface** sans bruit.

## Recommandations (appliquées)
- **R1 Segment « Mise en forme | HTML »** au-dessus du champ (même contrôle `tc-seg` que les autres bascules de l'admin, `radiogroup`), **mémorisé par poste** — confort, pas donnée de l'item. Une phrase courte à côté dit ce qui part (« Le texte part en HTML, mis en page par le journal » / « assaini par le journal à la réception »).
- **R2 Barre d'outils en groupes** séparés par un trait (règle 9, proximité) : Gras · Italique · Souligné · Barré | Intertitre · Sous-intertitre | Puces · Numéros · Citation · Trait | Lien · Effacer la mise en forme | (à droite) Annuler · Rétablir. Icônes Lucide + **infobulle avec raccourci** (Ctrl+B…), état actif en craie (`aria-pressed`), modèle **Toolbar de l'APG** (un seul arrêt de tabulation, flèches/Début/Fin). Barre collante en haut du cadre au défilement.
- **R3 Lien sans fenêtre du navigateur** : barre « Adresse du lien » sous la barre d'outils (Entrée = appliquer, Échap = annuler, « Retirer le lien » si déjà lié) ; `https://` ajouté s'il manque.
- **R4 Ne rien offrir que le journal jette** : seuls intertitres h2/h3, listes, citation, trait, lien ; pas de code, pas d'image (la photo de tête a son champ).
- **R5 Jamais de perte silencieuse** : un corps qui contient ce que la mise en forme ne sait pas afficher **s'ouvre en HTML** quel que soit le réglage du poste ; demander « Mise en forme » affiche un **encart dans le champ** (pas de fenêtre empilée) qui **nomme** les éléments (`<div> class="figures-box"…`) et propose « Rester en HTML » (bouton principal) / « Passer quand même ».
- **R6 HTML lisible** au passage en mode HTML : une balise de bloc par ligne, `<li>` sans le `<p>` interne.
- **R7 Compteur** « n car. de texte » (+ « n car. de code » en HTML).
- Réactions de lecteur, réseau social, messagerie : **champ texte inchangé** (pas d'HTML là-bas).

⭐ **Doctrine** : un éditeur riche ne doit jamais détruire en silence ce qu'il ne sait pas afficher — il le détecte, le nomme, et laisse l'humain choisir, la voie sûre en bouton principal.

## Vérifié en local (Playwright, thème sombre)
Captures : `1-mise-en-forme.png` (ancien corps en texte brut, ouvert en paragraphes), `2-barre-lien.png`, `3-mise-en-forme-remplie.png`, `4-html.png`, `5-alerte-perte.png`. Ouvrir puis enregistrer sans toucher : corps **inchangé** (texte brut et HTML à encadré, dans les deux modes). 0 erreur JS.
⚠ Défaut trouvé et corrigé pendant l'essai : `setEditable()` de Tiptap émet une mise à jour par défaut → l'éditeur caché (vide) effaçait le corps à l'ouverture d'un article à encadré ; corrigé (`setEditable(x, false)`) + garde-fou (seul l'éditeur visible modifie le corps).
