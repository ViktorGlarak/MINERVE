---
id: DECISION-010
type: decision
title: Méthode « storylanes v2 » de la synchromatrice — arcs/procédés ILI par LO
tags: [synchromatrice, storylanes, lo, expert-influence, mastaurige, aurige]
source: ../../EXPERT_INFLUENCE/MEMOIRE.md
linkedTo: [PROJ-AURIGE-7BB, AGENT-EXPERT-INFLUENCE, AGENT-MASTAURIGE, AGENT-MINAUTORE]
relevantFor: [exercices, mastaurige, expert-influence]
tier: 2
created: 2026-06-23
updated: 2026-06-23
---

# DECISION-010 — Storylanes v2 (synchromatrice)

## Contexte / problème
L'ancienne synchromatrice = **12 storylines descriptives statiques** (1 slogan par couple LO×bloc), sans procédé, sans escalade, découplées des injects. Demande : une méthode **nettement plus cohérente avec l'influence mercurienne** pour mieux organiser le prochain exercice.

## Décision
Une **storylane = un ARC/PROCÉDÉ d'influence complet** rattaché à **une LO**, code `07.XX`, fenêtre D+, **plusieurs injects coordonnés**. 4 principes : **hero-centric ou thématique** · **arc = séquence** (amorce/noyau de vérité → firehose multi-voix → verrouillage lawfare/dismay) · **récurrence en escalade** (même code, 2 entrées, fenêtres D+ croissantes = salami) · **LO = colonne, injects = chair**, calibré **niveau brigade**. Numérotation **`07.1x`=LO1 … `07.5x`=LO5** (dizaine = LO).

## Pourquoi (alternatives écartées)
Étiquette statique = ni contrôle réflexif, ni firehose, ni salami (défauts de l'audit corpus). L'arc séquencé + récurrence rend ces procédés russes **opérables et visibles** ; chaîne d'analyse par arc = effet (Sun Tzu) → principe (Morelli) → mentalité russe → phase Storm-1516 → LO.

## Conséquences / à respecter
- 1ʳᵉ proposition livrée : **16 storylanes** (2 récurrentes : 07.20 VORIN, 07.52 sang français) seedées dans `…\MELMIL\SYNCHROMATRICE\synchromatrice.js` ; clé localStorage **`v1→v2`** (l'ancien état est ignoré → la proposition s'affiche d'emblée).
- **Aucune autre fenêtre touchée** ; moteur de rendu inchangé (`pack()` empile nativement 2 entrées de même code).
- Itérations possibles : ajuster les fenêtres D+, ajouter des arcs, rattacher les vrais codes d'injects `.Ixx`.
- Doctrine = [[AGENT-EXPERT-INFLUENCE]] (§ Méthode storylanes v2) ; outil = [[PROJ-MASTAURIGE]].

## 🔗 Source de vérité
`EXPERT_INFLUENCE/MEMOIRE.md` (§ MÉTHODE STORYLANES v2) + `MASTAURIGE/MEMOIRE.md` (changement outil). **Cette note pointe, ne recopie pas.**
