---
id: LESSON-039
aliases: ["LESSON-039"]
type: lesson
title: Derrière un proxy, une adresse absolue se construit sur les en-têtes, jamais sur req.url
tags: [pleiade, traefik, proxy, eho, portraits, https]
source: ../../PLEIADE/MEMOIRE.md
linkedTo: [DECISION-030, DECISION-029, LESSON-037]
relevantFor: [pleiade, mastorion, leac]
tier: 1
created: 2026-09-21
updated: 2026-09-21
---

# LESSON-039 — Les portraits existaient, le navigateur les refusait

## Ce qui s'est passé
Modèle appliqué, portraits déposés, un fichier répond **200 `image/jpeg`** —
et pourtant **aucune image à l'écran**. Le catalogue Pléiade n'injecte pas
`EHO_PUBLIC_URL` ; l'adresse stockée venait alors de `req.url`, c'est-à-dire
de ce que **le conteneur** reçoit derrière Traefik : `http://…`. Une image
`http` dans une page `https` = **contenu mixte**, bloquée par le navigateur,
**silencieusement**.

## Leçon
Ce que le conteneur voit n'est pas ce que le navigateur voit. Toute adresse
absolue rendue au client (portrait, retour de déconnexion, lien d'un courriel)
se construit dans cet ordre :

1. une **variable publique explicite** (`EHO_PUBLIC_URL`, `NEXTAUTH_URL`) ;
2. sinon **`X-Forwarded-Proto` / `X-Forwarded-Host`** ;
3. sinon, seulement, l'origine de la requête (cas du développement local).

⚠ Corollaire de diagnostic : « le fichier répond 200 » **ne prouve pas** que la
page peut l'afficher. Le blocage est côté navigateur, invisible du serveur.

## Appliqué
- eho : `originePublique(req)` dans `lib/uploads.ts`, utilisée par
  `urlPublique` (téléversement) **et** par l'application d'un modèle intégré.
  Vérifié en local avec des en-têtes de proxy simulés.
- Même lecture d'en-têtes que celle qui fait marcher la déconnexion sur le
  serveur ([[DECISION-029]]) — une seule façon de savoir « où l'on est vu ».
- ⚠ Les adresses ne sont réécrites qu'**à l'application** du modèle : après
  correctif, il faut **ré-appliquer** pour que la base porte les bonnes.
