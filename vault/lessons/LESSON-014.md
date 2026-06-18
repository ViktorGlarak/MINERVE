---
id: LESSON-014
type: lesson
title: Le camp d'une fiche ≠ son titre de poste — lire l'orientation dans le narratif
tags: [camp, ili, trombino, arnland, generation]
source: ../../ANALYSTE/ARNLAND/MEMOIRE.md
linkedTo: [ENT-arnland, PROJ-AURIGE-7BB]
relevantFor: [arnland, mastaurige, exercices]
tier: 2
created: 2026-06-18
updated: 2026-06-18
---

# LESSON-014 — Le camp se lit dans le NARRATIF, pas dans le titre de poste

## Symptôme observé
`generer_trombino_bios.py` déduisait le camp Arnland de l'**intitulé de poste** (heuristique : `pro-mer`→rouge, certaines villes→neutre, sinon **bleu par défaut**). Résultat : des **maires pro-MER** (Hartmann élu sur listes pro-MER, Kovalev pro-MER assumé, Weber « proche des milieux pro-MER ») classés 🔵, et des **ONG neutres par mandat** (CICR/Kalugin, Blue Shield/Petrovna) classées 🔵. 7 fiches fausses sur 21.

## Cause racine
L'orientation réelle (pro-MER / pro-ARN / impartial) n'est **pas dans le titre** mais dans le **contenu de la fiche** (parcours, objectifs, réseaux sociaux). Une heuristique de poste ne peut pas la voir. Un maire reste « maire » quel que soit son camp.

## Correctif / règle à appliquer
- **Toujours faire trancher le camp par l'orientation narrative**, pas par le poste. Un audit fiche par fiche est nécessaire quand le camp est dérivé automatiquement.
- Correction **durable** = table d'**override explicite par id** (`CAMP_OVERRIDE`) qui **prime sur l'heuristique** dans le générateur → une régénération ne réintroduit pas l'erreur.
- **Autorité du camp = `vault/entities/ENT-*`** (un camp = une note) ; `valider.py` **bloque** toute divergence entités ↔ `bios.js` ↔ mémoires. Aligner les 3 lors d'une correction.
- ⚠ Enjeu : le **camp pilote l'effet ILI** — un mauvais camp produit l'effet **inverse** (ex. cibler un allié pro-MER comme s'il était bleu).

## 🔗 Source de vérité
[[../../ANALYSTE/ARNLAND/MEMOIRE.md]] § « CORRECTION DES CAMPS ». Mécanique outil : `MASTAURIGE/MEMOIRE.md` § « CAMPS TROMBINO ARNLAND ». Voir [[ENT-arnland]].
