---
id: LESSON-028
aliases: ["LESSON-028"]
type: lesson
title: La bio MASTORION est PUBLIQUE côté réseau social — le renseignement animateur va dans observations
tags: [mastorion, eho, bio, observations, fuite, opsec]
source: ../../MASTORION/OUTILS/generer_bibliotheque.py
linkedTo: [DECISION-013, ARCH-011, LESSON-027]
relevantFor: [mastorion, bibliotheques, exercices]
tier: 2
created: 2026-09-09
updated: 2026-09-09
---

# LESSON-028 — bio = vitrine publique, observations = dossier animateur

## Symptôme observé
Les mentions « ⚠ COMPTES MULTIPLES — même entité que @X » avaient été posées
en tête de `bio` de 4 comptes. Or l'API sociale sert la bio À TOUS : les
joueurs auraient lu noir sur blanc le lien Gavrilov↔Grass_hopper — précisément
ce que l'exercice d'analyse doit leur faire découvrir.

## Cause racine
Confusion entre les deux champs : `bio` = profil public du réseau social
(en jeu), `observations` = champ de fiche visible animateur seulement.
Le board joueur EHO ne transmet d'ailleurs AUCUN champ officiel.

## Correctif / règle à appliquer
**Tout renseignement animateur (liens entre comptes, notes d'emploi, vrais
camps) va dans `observations` — jamais dans `bio`.** Générateur corrigé
(mention en observations + purge des bios héritées), base assainie, modèle
SKOLKAN-PERSONA recapturé propre. Avant d'écrire dans un champ persona :
se demander « qui le voit en jeu ? ».

## 🔗 Source de vérité
Détail / trace : voir `source:`. **Pointeur, pas copie.**
