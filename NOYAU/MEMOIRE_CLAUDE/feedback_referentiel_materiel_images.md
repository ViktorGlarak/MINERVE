---
name: feedback-referentiel-materiel-images
description: "Prompts image MINERVE — matériel EXACT par camp (FR/OTAN vs Mercure russe) + jamais de pancarte/support de texte vide"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 4377e89f-f0dd-40af-851d-ddfb523fd276
---

Pour tout **prompt d'image** (ou scène vidéo) montrant véhicules/soldats dans les exercices AURIGE/ORION (cadre **FR-OTAN vs adversaire de doctrine russe**) : **nommer le matériel précisément, par camp**. Un prompt générique (« military supply trucks / armored vehicles ») fait générer du **matériel américain ou d'époque (WW2)** → FAUX pour un exercice français/OTAN. Constaté 2026-06-25 sur l'inject **07.10.I02**.

**Why:** le réalisme matériel fait partie de la crédibilité pédagogique de l'exercice ; un Humvee/Abrams US ou un camion d'époque dans un article « forces françaises » casse l'immersion des entraînés.

**How to apply:**
- 🔵 **forces françaises/OTAN** (entraînés 7BB, BFA, coalition) : Griffon, Serval, Jaguar, Leclerc, VAB, VBCI, CAESAR, **camions GBC 180 / TRM 10000 / PPLOG** ; camo **Centre-Europe**, **HK416/FAMAS**, **FÉLIN/SPECTRA**.
- 🔴 **Mercure** : matériel **type russe** — T-72/T-90-style, BTR-80, BMP, **Ural-4320**, 2S19 Msta ; camo **digital flora**, **AK**.
- Choisir selon le camp **MONTRÉ à l'image**, pas le camp éditorial (ex. convoi OTAN vu par un article rouge anti-OTAN = matériel **bleu français**).
- Negative : `no American vehicles, no Humvee, no Abrams, no MRAP, no US multicam, no WW2 vehicles, no desert tan`.
- **Firefly** suit mieux si on cite le nom exact (recherche web) ; **Flow/Gemini** → modèle + description de silhouette.
- Référentiel complet (tables + blocs prompts) : `D:\CECPC\PRODUCTION\IA\MINERVE\IMAGIER\REFERENTIEL_MATERIEL.md` ; consigné aussi dans `IMAGIER\MEMOIRE.md` et `SCENARISTE\MEMOIRE.md`. Lié à [[project_mercure]].

**Règle complémentaire — JAMAIS de pancarte/support de texte vide** (constaté 2026-06-25, inject 07.11.I05 : pancartes générées vides). Tout support censé porter du texte (pancarte, banderole, affiche, tract, écran, panneau) ne doit jamais apparaître vide → soit **(A)** texte **exact verbatim** d'un slogan court de l'article, `legible word for word` (outil Flow/Firefly, pas Gemini) ; soit **(B)** scène **sans** support + négatif `no signs, no placards, no banners`. Le SCÉNARISTE fournit le verbatim exact. Consigné dans `IMAGIER\MEMOIRE.md` (§ Règle pancartes) et `SCENARISTE\MEMOIRE.md`.
