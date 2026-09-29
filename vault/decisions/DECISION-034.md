---
id: DECISION-034
aliases: ["DECISION-034"]
type: decision
title: eho — UNE fiche d'avatar, UN verrou : la planche relationnelle ouvre la même fiche que l'onglet
tags: [eho, pleiade, fiches, avatars, planche, verrou, react-flow]
source: ../../PLEIADE/MEMOIRE.md
linkedTo: [DECISION-029, DECISION-030]
relevantFor: [pleiade, mastorion, delattre]
tier: 2
created: 2026-09-22
updated: 2026-09-22
---

# DECISION-034 — Une seule fiche, quel que soit l'écran qui l'ouvre

## Contexte / problème
Sur la **planche relationnelle** d'eho, les cartes ne donnaient accès qu'à un
aperçu : pour lire ou corriger une biographie, il fallait retourner dans
l'onglet des EHO. Deux chemins vers la même personne, dont un seul complet.

## Décision
La fiche **biographique complète** s'ouvre au clic sur une carte de la
planche, **à l'identique** de celle des onglets — même composant, même verrou
d'édition. Et elle est **portée par la planche** : « La mienne » ouvre la
fiche de *Mon EHO*, « GT … » celle de l'*EHO du groupe*.

Mise en œuvre : deux briques partagées, `fiche-avatar.tsx` (la fiche) et
`verrou-fiche.ts` (qui édite, et qui est bloqué), utilisées par les deux
écrans. Accès rendu visible : un bouton **« i »** dans les cartes de la
réserve (bande sur toute la hauteur, à droite) et sur les cartes du plan
(en bas à droite, hors des poignées de liaison).

## Pourquoi (alternatives écartées)
- **Dupliquer la fiche** dans la planche : deux copies auraient divergé, et le
  verrou aurait cessé de protéger quoi que ce soit.
- Garder le mot « Fiche » sur les cartes du plan : trop large, il masquait les
  poignées ; un « i » discret suffit.

## Conséquences / à respecter
- ⚠ **Une fiche d'avatar, un verrou** : toute nouvelle vue qui montre un
  avatar réutilise ces deux briques, elle n'en écrit pas de troisième.
- ⚠ Le **transfert d'un encadré** d'une planche à l'autre déplace les cartes,
  **jamais les fiches** : la biographie reste celle de l'EHO de la planche
  d'arrivée (fonctionnalité qui existait déjà, rendue trouvable).

## 🔗 Source de vérité
Détail complet : `source:` et `PLEIADE/JOURNAL.md` du 2026-09-22.
**Cette note ne recopie pas — elle pointe.**
