---
name: aurige7bb-minotaure
description: "Exercice AURIGE 7BB = MINOTAURE 26 (GT2, Mailly 9-13 mars 2026, D+33-D+41). Cadre, manœuvre, camps INVERSÉS, storylines ILI — agent MINAUTORE renseigné."
metadata: 
  node_type: memory
  type: project
  originSessionId: 410ff7ab-cce4-44f7-9471-211855cef197
---

**AURIGE 7BB** = exercice OTAN **MINOTAURE 26**, Groupe de Travail **GT2**, camp de **Mailly** (Bât Daguet), **9–13 mars 2026**, temps de jeu **D+33→D+41** (OPORD 03 PH3b Stage 33, cadre **MNC-W**). Dossier de montage : `EXER\AURIGE 7BB\01_Montage exercice\`. Ingéré et reporté dans `MINAUTORE\MEMOIRE.md` + `SYSTEME\PROMPTS\minautore.md` le 2026-05-31.

**Mission OTAN :** « RESTORE ARN GET sovereignty » — l'OTAN ATTAQUE vers l'est (plateau HLORRAIN) pour libérer l'Arnland envahi par MER. Adversaire = FORAD **MER / FGF-L** (Freedom for GET Forces-Land, doctrine TITAN, REDBOOK DIVFORAD).

**⚠ Camps INVERSÉS vs AURIGE 2BB :** ici 🔵 BLEU = OTAN/France/ARN = **les entraînés** (7BB, 27BIM, BFA) qui **attaquent** ; 🔴 ROUGE = **MER** qui **défend puis "libère"** et que **MINAUTORE doit faire vivre en ILI**. MER se pose en libérateur, traite les bleus d'« envahisseurs/colonisateurs ».

**Théâtre :** Lorraine/Alsace réelles, codage **H-préfixe** (HLUNEVILLE, HCHATEAU-SALINS, HSARREBOURG, HMOSELLE/HMEURTHE/HMEUSE/HRHINE, HVOSGES). Lignes de défense MER : **ADL** (HMOSELLE) → **MDL** → **UDL** (Vosges, risque chimique/WMD).

**Acteur voisin GET — Bothnia (décision 2026-05-31, CANON) :** un **countrybook Bothnia complet existe** (`EXER\01 ORION 26\ORION-4\01 - CORPUS DOCUMENTAIRE\BOTHNIA.docx`, ~1700 l.) → **il fait foi pour MINOTAURE 26 et tous les exercices futurs**, et a été **ingéré à 100 % le 2026-05-31** dans `ANALYSTE\BOTHNIA\MEMOIRE.md` (§ COUNTRYBOOK BOTHNIA + § COMPLÉMENT INTÉGRAL : sections A→F + Annexe Leading Figures — politique/cabinet/partis, médias, ORBAT terre/mer/air/frontières, éco, société, infrastructure, roster nominatif). **Les 3 analystes pays (Mercure, Arnland, Bothnia) sont désormais experts référents complets — parité countrybook.** Arnland porté à 100 % le 2026-05-31 (vérification : la mémoire n'était qu'une synthèse ; § COMPLÉMENT INTÉGRAL ajouté — géo/histoire, système politique/6 partis, ORBAT 7 secteurs militaires + SDF/TANTALE, éco, société/diaspora, infra ; ⚠ correction Alltinget 128→**132**). Méthode de vérification : mapper les sections du countrybook (PDF/docx) vs la mémoire avant d'affirmer la complétude. **Mercure vérifié & complété à 100 % le 2026-05-31** (`CREATION\02 - MERCURE\Orion 26 - CB MERCURE.pdf` — 7 sections + annexe ; couverture était ~85 % ; § 1.12 ajouté : 5 ministres manquants, structure Min. Intérieur, 9 présidents régionaux, chefs OIG Skolkan, Section 7 Infrastructure gaz/transport/énergie, services sociaux). **Les 3 countrybooks (MER/ARN/BOT) sont désormais vérifiés à 100 % par mapping — pas seulement « déclarés ingérés ».** Outils : `pdftotext -layout` (mingw64) pour PDF, py3.14 stdlib zipfile/XML pour docx/pptx/xlsx. Bothnia = République **démocratique parlementaire**, Présidente **Lena Peters** (BUP), PM Olaf Roland, Min. Int. Nele Meyer ; capitale **Brahea** ; allié MER via **SCO/SSTO** ; base **Den Helder** (bail 2027) ; neutre « raisonnable » mais soutient le FGF-L ; ligne média « neutralité » + opinion divisée = terrain ILI. ⭐ **BC1 = « Bothnia Channel 1 »** dans le countrybook (le code BC1 était habillé « Bella Channel 1 » en 2BB). ⚠ **Youkachenko/BC1-Bella/Ruthnia Bella = AURIGE 2BB UNIQUEMENT** (reskin figé).

**Agent renommé 2026-05-31 : ANALYSTE_RB → ANALYSTE_BOT** (expert Bothnia canon + legacy RB 2BB). Dossier `ANALYSTE\RUTHNIA_BELLA\` → `ANALYSTE\BOTHNIA\` ; prompt `analyste_rb.md` → `analyste_bot.md`. Propagé : CLAUDE.md, ROUTAGE, NOYAU (compteur inchangé 18), prompt, README. Voir [[renommage_ruthnia_bella]].

**Casting rouge militaire RÉSOLU :** le PDF `…20260303_NP_GLM26_SITCEN_RENS_Profils-HVI-MER.pdf` (« Profiles of Enemy Commanders ») a été extrait via `pdftotext -layout` le 2026-05-31 — toute la chaîne FGF-4 (cdt corps MIZINTSEV, 41 TKDIV PRUNIERE, 42 MECHDIV KOULIKOV, 43 ABN ZHUKOV + brigades) + chefs hybrides TANTALE (KALEVA chef, MILANOV 2IC SOCMED) consignée chez ANALYSTE MERCURE § 1.5.ter. ⚠ pdftotext dispo via mingw64, py3.14 sans libs office (extraction via stdlib zipfile/XML).

**Catalogue ILI (Event List) :** 4 storylines `07-01`..`07-04` (= LO2 Volonté combattre / LO3 Guerre pertes / LO4 Vent libération / LO5 Rupture alliances ; LO1 = effort permanent) + 6 opportunités (MENACE DRONE, NRBC PERSISTANT, SEVESO, MASCAL, CYBER BTS, CYBER ATK GRIFFON). Format codes `07-0X-YZ` (dizaine = phase). Voir [[glm26_matrice_ili]], [[aurige_template_base]], [[aurige_brigade_calibration]].

**Reste à faire :** construire le calendrier éditorial (0 inject produit) ; le MANNING contient des noms RH réels — **ne pas les copier** dans les fichiers agent.
