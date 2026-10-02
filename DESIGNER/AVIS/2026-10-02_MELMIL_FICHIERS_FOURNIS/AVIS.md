# Avis n°30 — MELMIL : affichage des fichiers fournis d'une demande

> **Date** : 2026-10-02 · **Demandeur** : l'utilisateur · **Écran** : `app-melmil`, fiche d'une demande de produit, champ « Fichiers fournis » (`components/atelier/produits.tsx`).
> **Statut** : ✅ en ligne le 2026-10-02 (`app-melmil` `3e0da58`, `2026-10-02.7`).

## Constat de l'utilisateur
Après l'ajout de la récupération des fichiers fournis (suite 12), chaque fichier s'affiche sur une **ligne pleine largeur** avec des liens **bleus** « Ouvrir / Télécharger ». L'utilisateur trouve cela « bizarre » et demande si c'est normal ou améliorable.

## Verdict (DESIGNER) : améliorable, deux écarts au design system
1. **Le bleu.** Le bleu `--anneau` (#1f5f8b) est l'accent JEMM de MELMIL, réservé à des repères rares (focus, espace JEMM). L'employer pour chaque lien de fichier en banalise l'usage — contraire à « une seule couleur d'accent, rare » (REF-06 Von Restorff) et à la cohérence (REF-14, heuristique 4). Ailleurs (carte média), les actions sont des boutons **neutres** `frappe`.
2. **La pleine largeur.** Une ligne par fichier étirée sur toute la largeur de la fiche fait des bandes vides et un balayage inconfortable (REF-07 : lignes trop longues, espace ambigu). Les médias d'un incident, eux, sont en **grille de cartes** (`.media-grille`, `minmax(150px, 1fr)`) : c'est le motif déjà connu de l'utilisateur (REF-06 Jakob).

## Recommandations
- **R1 — Une grille de cartes compactes**, comme les médias de l'incident : `repeat(auto-fill, minmax(240px, 1fr))`. Plus de bande pleine largeur.
- **R2 — Boutons neutres** `frappe frappe-mini` pour « Ouvrir » et « Télécharger » (mêmes boutons que la carte média). Le nom du fichier reste un lien, mais en couleur de **texte**, souligné au survol — pas en bleu.
- **R3 — L'accent (craie/anneau) uniquement pour la SÉLECTION** (la pastille ✓ « sert de base »), pas pour les actions. En lecture, pas de pastille : juste les cartes avec « Ouvrir / Télécharger ».
- **R4 — Carte lisible** : nom tronqué avec `title`, et les actions dessous. Icône de genre (IMG/DOC/SON/VIDÉO) possible plus tard ; non bloquant.
- Cohérence : à terme, la **livraison** de la cellule Prod et les médias d'incident gagneraient le même gabarit de carte — hors périmètre de cet avis.
