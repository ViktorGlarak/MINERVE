---
name: trombino-bios-popup
description: "Trombinoscope avec fiches bio cliquables (pop-up) — generer_trombino_bios.py, bios.js, 41 fiches Arnland+Bothnia, 2026-06-11"
metadata: 
  node_type: memory
  type: project
  originSessionId: 08c749e1-d2a0-4ea6-ab1e-0268dec9e9b0
---

Le trombinoscope MASTAURIGE (`Sites\Trombinoscope\ACTEURS_A3_model.html`) a des **cartes cliquables → pop-up fiche bio**. Outil : `OUTILS\generer_trombino_bios.py` qui (1) parse 3 fiches bio (`CREATION\06 - Arnland\...20260611...docx` + `CREATION\07 - RUTHNIA BELLA\FICHES BIO\` : `Fiches bio BOTHNIA.docx` + `Fiche Bio - RUTHNIA BELLA.odt` — ce dernier = **Bothnia** militaires/opposition/religieux, pas RB), (2) écrit `bios.js` (41 fiches, `window.TROMBI_BIOS`), (3) injecte un **bloc idempotent** `<!-- BIOS:START/END -->` (CSS+popup+init). Cartes existantes → cliquables par match de nom ; manquantes → cartes addendum dans `.page-dr` (Arnland HN) + `.page-br` (Bothnia).

**Camps = autorité analyste/registre** : Arnland officiel 🔵, pro-MER 🔴 ; Bothnia état 🟢 neutre ; **Tikhanov/Saniki figés 🔴** (registre MASTAURIGE). Appliqué vierge + 7BB.

**Why:** rendre les ~35 nouvelles personnalités des fiches bio visibles et consultables dans le trombino.
**MAJ 2026-06-12 :** **45 fiches** (était 41). Page A3 en hauteur **auto** + cache-buster `bios.js?v=`. Fiches manquantes en **bande `.bio-band`** au bas de la page pays (plus de pages dédiées). Rename **« Dacie Romanie → Arnland »** (DR=Arnland). **5 bugs parseur corrigés** (fuites/fusions de sections — détail dans MASTAURIGE\MEMOIRE.md) : (1) 3 officiers Bothnia sautés (Kosmannen/Koho/**Groop**) ; (2) label **Faiblesses** avec espace insécable `\xa0` non reconnu → faiblesses avalées dans Forces (LINDQUIST) ; (3) record poubelle bot_mil_saniki (bloc militaire non borné) → scan coupé à « OPPOSITION POLITIQUE » ; (4) Tikhanov/Saniki en bio complète, camp rouge forcé ; (5) **Maksym Borchenko** (patron transports) manquait (en-tête absent de `heads`) → fusionné à tort dans Petrovna ; ajouté, Petrovna nettoyée. ⚠ Réflexe : après tout changement, **auditer fusion** (Forces>5/Faiblesses>6/Objectifs>6) + réconcilier sources↔bios.js.

**How to apply:** ré-ingérer/modifier une fiche bio → relancer `generer_trombino_bios.py` (régénère bios.js + ré-injecte, idempotent). ⚠ Après régénération : **hard-refresh navigateur (Ctrl+Shift+R)**. Bios consignées chez [[arnland_fiches_bio_hn]] (ANALYSTE_ARN) + ANALYSTE_BOT. Voir [[trombino_img_convention]], [[mastaurige_instance_7bb]].
