---
name: feedback-marquages-diffusion
description: "Avant d'ajouter un document officiel à un dépôt partagé, relever son marquage RÉEL (filigranes, métadonnées) et non celui de son nom de fichier ; signaler et exclure, laisser l'arbitrage à l'utilisateur"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 7f9a0a6b-9fe5-457d-b4e3-f0b50bf62931
  modified: 2026-09-17T12:59:29.464Z
---

Avant d'ajouter au dépôt un document officiel (CECPC, armée, tout organisme),
**relever son marquage de diffusion réel** — filigranes d'en-tête
(`word/header*.xml`), métadonnées `customXml`, pieds de page — et **jamais** se
fier au marquage annoncé par le nom de fichier. Si un marquage protecteur
apparaît : **le dire, exclure le fichier du dépôt, et laisser l'utilisateur
trancher**. Ne jamais publier de sa propre initiative, ne jamais bloquer non plus.

**Why :** le 2026-09-17, le modèle de CRF du CECPC était nommé
`AAAAMMJJ_NP_...` (NP = non protégé) mais portait un filigrane « DIFFUSION
RESTREINTE » sur chaque page et dans ses métadonnées. GitHub est externe à
l'infrastructure du ministère. L'utilisateur a explicitement validé la démarche
— « tu as très bien fait et tu pourras refaire cela si tu en trouves d'autres à
l'avenir » — puis a tranché que ce filigrane-là était une erreur.

**How to apply :** scanner les `.docx` / `.pptx` / `.xlsx` (ce sont des zip
d'XML) pour `diffusion restreinte|secret|confidentiel|classifi`. ⚠ Distinguer un
**marquage** d'une **occurrence dans le contenu** : les grilles d'évaluation N4
parlent de « gestion des documents classifiés » comme d'un critère à noter, ce
qui n'est pas un marquage. Une fois un cas tranché par l'utilisateur, **écrire
la décision dans le dépôt** (ici `app-leac/docs/sources/README.md`) : le
filigrane reste dans le fichier, et sans trace la même alerte se relance
indéfiniment. Voir aussi [[feedback-certificats-vpn-interdits]] et
[[feedback-dossier-interdit-fiches-bio]].
