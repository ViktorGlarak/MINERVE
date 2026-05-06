# MÉMOIRE — CINÉASTE

## Format d'entrée
```
### [YYYY-MM-DD] Exercice : [NOM] — [Titre de la séquence]
**Workflow :** i2v / ia2v
**Image source :** description de l'image d'entrée
**Prompt utilisé :** texte exact
**Paramètres :** motion_bucket_id, fps, num_frames
**Résultat :** PASS / FAIL + observations
**Leçon :** ce qu'il faut retenir
```

---

## Contexte des exercices
- Vidéos destinées à simuler des reportages, flux d'actualité, vidéos de terrain
- Durées courtes : 3-8 secondes par clip (assemblage Premiere Pro ensuite)
- Style cible : reportage TV français, caméra embarquée, drone, CCTV

---

## Patterns de prompt efficaces
<!-- Formulations LTX 2.3 validées -->

---

## Workflow i2v — Règle absolue [2026-05-06]
On génère TOUJOURS l'image source en premier (IMAGIER → Gemini/Flow/Adobe Firefly).
Le prompt LTX i2v décrit UNIQUEMENT le mouvement, pas le contenu visuel (déjà dans l'image).
LTX reçoit : image source + prompt de mouvement → produit le clip animé.
Adobe Firefly (licence Adobe de l'utilisateur) est l'outil image prioritaire.

## Règles fondamentales LTX 2.3 (source officielle)
- Format : UN SEUL paragraphe fluide de 4-8 phrases, verbes au présent
- Ordre : plan → lumière → action → sujet → caméra → audio
- Émotions via indices physiques UNIQUEMENT (pas de "triste", "confus")
- Jamais de texte lisible dans le prompt (LTX ne le rend pas)
- Pas de physique complexe (sauts, chutes violentes)
- Construire par itération : commencer simple, ajouter progressivement

## Patterns à éviter
- Éviter les mouvements trop rapides (artefacts visuels)
- Ne pas décrire des changements de scène (LTX anime l'existant, ne recrée pas)
- Pas de labels émotionnels directs → remplacer par posture, regard, tension musculaire
- Pas trop de personnages simultanément dans la scène

## Logos et texte dans les vidéos LTX — règle importante
LTX ne peut pas reproduire fidèlement un logo spécifique ni du texte précis.
Solution validée : LTX génère le décor/mouvement, le vrai logo PNG est overlayé dans Premiere Pro.
Technique Premiere Pro : mode de fusion **Multiply** sur le logo noir/blanc → le blanc disparaît, le noir s'intègre sur le fond comme un vrai tag.
Appliqué pour : N.O.M logo (N.O.M.png depuis D:\CECPC\PRODUCTION\BDA\02 - MERCURE\N.O.M\)
Valable pour tout logo ou texte précis dans une vidéo générée par LTX.

---

## 4 Styles validés pour exercices de crise — [2026-05-06]

### Style 1 : Reportage TV — caméra portée (journaliste terrain)
Commence par : "A handheld news camera captures..."
Inclure : instabilité naturelle du journaliste, lumière plate overcast, tracking lent, sons ambiants de rue.

### Style 2 : Surveillance CCTV — plan fixe
Commence par : "A static overhead security camera records..."
Inclure : compression grand angle, qualité monochrome CCTV, caméra IMMOBILE (ne pas décrire de mouvement), sons ambiants environnement.

### Style 3 : Drone aérien — descente lente
Commence par : "An aerial drone shot descends slowly over..."
Inclure : paysage français en dessous, diffusion lumière overcast, tilt progressif pour révéler l'élément focal, son du vent.

### Style 4 : Caméra embarquée — véhicule approchant
Commence par : "A dashcam records from inside a vehicle traveling along..."
Inclure : route française précise, élément de scène qui grossit progressivement, ralentissement du véhicule, sons moteur.

## Résultats validés par exercice

### AURIGE 2BB — 07.08.01 Sujet JT tags N.O.M HNancy [2026-05-06]
5 clips LTX produits. Structure JT : large rue → gros plan tag → police patrouille → interview expert → large quartier habitants.
N.O.M tag description validée pour LTX : "black spray-painted stencil graffiti, skull inside a downward-pointing inverted triangle, letters N.O.M. below in bold stencil font, paint edges slightly dripping"
Style général : handheld news + static locked shots, overcast flat light, cold documentary atmosphere, pas de color grade cinématique.
Plan 2 splitté en 2 clips séparés (tag close-up + police) car LTX gère mal les transitions de sujet.
