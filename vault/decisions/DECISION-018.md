---
id: DECISION-018
aliases: ["DECISION-018"]
type: decision
title: Le curseur d'alignement est ouvert sur les STARTEX — il y mesure une ATTITUDE, pas une identité
tags: [eho, pleiade, startex, curseur, depouillement, joueur]
source: ../../PLEIADE/MEMOIRE.md
linkedTo: [DECISION-015, DECISION-016, DECISION-020, TOOL-016, ARCH-013]
relevantFor: [pleiade, exercices, mastorion]
tier: 2
created: 2026-09-16
updated: 2026-09-16
---

# DECISION-018 — Le même curseur pose deux questions différentes

## Contexte / problème
Sur une carte du package STARTEX, le joueur ne pouvait **rien** régler : la fiche
n'affichait que l'officiel. Or l'attitude d'une autorité connue **bouge avec ce
que les joueurs font** sur le terrain et sur les réseaux — *« un maire ménagé se
rapproche, un maire humilié bascule »*.

## Décision
Le curseur d'alignement devient modifiable **aussi** sur les STARTEX. Ce n'est
pas un relâchement du dépouillement : c'est une **autre question**.

| Carte | Question | Départ du curseur | Comptée en écart ? |
|---|---|---|---|
| Avatar inconnu | « **qui est-il ?** » — identification | « je ne me prononce pas » | **oui** |
| Autorité STARTEX | « **où en est-il avec nous ?** » — attitude | **la position officielle** | **jamais** |

## Pourquoi (alternatives écartées)
- **Un second champ** (`attitudeCurseur`) a été écarté : *deux champs qui disent
  la même chose finissent par se contredire* — voir [[DECISION-016]], même
  raisonnement. Un seul chemin d'écriture, commun aux deux cas.
- **Partir de zéro** a été écarté : sans point de départ visible, **il n'y a pas
  de dérive à lire**. Le curseur part de la position officielle, marquée d'un
  repère.

## Conséquences / à respecter
- ⚠ **L'IDENTITÉ reste verrouillée** sur un STARTEX : `paysEstime` et
  `fonctionEstimee` sont **ignorés côté serveur** (vérifié par un appel forgé qui
  tentait de les poser en même temps que le curseur).
- **Jamais un écart** : le calcul d'écart rend `null` sur un STARTEX. Côté
  animateur, c'est de la **matière d'animation**, pas une faute de lecture.
- La carte de la planche **suit l'alignement observé** dès qu'il existe — un maire
  qui bascule doit se voir sur la planche, pas au fond de sa fiche.
- ⏳ **Non traité** : l'historique des mouvements. On enregistre la position
  actuelle, pas son évolution — impossible aujourd'hui de dire « il a basculé au
  D+37 ».

## 🔗 Source de vérité
`PLEIADE/MEMOIRE.md` (tableau « le curseur pose DEUX questions ») et le commit
`5aa9dac` du dépôt `eho`.
