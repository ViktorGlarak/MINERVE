# Avis DESIGNER n°11 — MELMIL, Équipe : de l'araignée à l'organigramme

> **Date** : 2026-09-28 (après-midi) · **Suite de l'avis n°10**, après les premiers essais de l'utilisateur sur ses vraies données (non lues par l'assistant : confidentielles).

## Les trois remarques de l'utilisateur
1. Dans HOSTNATION, on ne voyait **que des noms de sous-groupes**, pas les personnes. Ses personnes sont dans ses sous-groupes, et l'araignée n'affichait les petits-enfants qu'en puces.
2. DEV / PROD, rangé dans GREYCELL, doit **aussi être relié à FORAD** : un groupe n'avait qu'un seul rattachement.
3. L'exercice au centre, dans un rond, **n'aide pas à comprendre** : les groupes sont **dans** l'exercice, pas autour.

## Diagnostic
- Une **mise en page radiale** fixe un nombre de couronnes : au-delà, on masque. Elle confond aussi « contenir » avec « être au centre ». *(Règle 15, Jakob : l'organigramme est le schéma que tout militaire sait lire.)*
- Deux relations différentes, « est rangé dans » et « travaille avec », doivent se **distinguer à l'œil**. *(Règle 10 : pas une seule variable visuelle pour deux sens.)*

## Solution retenue

**R1 · L'exercice devient le CADRE** : un bandeau en tête (« EXERCICE · DE LATTRE 26 · 8 groupes · 17 personnes »), et les groupes sont à l'intérieur.

**R2 · Un organigramme, à toute profondeur** :
- les groupes de premier niveau en colonnes ;
- leurs sous-groupes emboîtés dessous ;
- **chaque carte montre ses personnes** (jusqu'à 10, puis « + n autres ») ;
- traits de hiérarchie en équerre, dans la couleur du groupe enfant.

**R3 · Un seul parent, plus des liens « travaille aussi avec »** : la hiérarchie reste un arbre, donc lisible. Les coopérations sont des liens à part :
- tracés en **pointillé gris** dans l'organigramme ;
- **et écrits** dans les deux cartes (« ↔ FORAD »), pour qu'ils se lisent sans le trait, en vue Liste et au téléphone.

**R4 · Une légende** en pied de cadre : trait plein = rangé dans ; pointillé = travaille aussi avec.

**R5 · Largeur maîtrisée** : un organigramme large défile **dans son cadre**, jamais la page. Au téléphone, la vue Liste d'office.

## Vérifié (structure fictive du même genre, en local)
3 niveaux sous HOSTNATION, tous avec leurs personnes ; un lien DEV / PROD ↔ FORAD tracé et écrit des deux côtés ; 0 débordement à 1440 px, 1024 px et au téléphone ; 0 erreur.

## Pistes pour la suite
- Donner un **libellé** au lien (« appui », « coordination »…).
- Glisser une carte pour changer de parent.
- Exporter l'organigramme (image, PDF) pour un briefing.
