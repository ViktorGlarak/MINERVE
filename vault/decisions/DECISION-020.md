---
id: DECISION-020
aliases: ["DECISION-020"]
type: decision
title: L'onglet « Choix d'avatar » supprimé — un écran qui liste les avatars n'a de sens que côté animation
tags: [eho, pleiade, depouillement, joueur, securite]
source: ../../PLEIADE/MEMOIRE.md
linkedTo: [DECISION-015, DECISION-018, ARCH-013]
relevantFor: [pleiade, exercices]
tier: 2
created: 2026-09-16
updated: 2026-09-16
---

# DECISION-020 — Retirer « Choix d'avatar » de la section joueur

## Contexte / problème
L'onglet annonçait « Sélectionnez votre personnage » mais **ne sélectionnait
rien** : aucun clic sur les cartes, aucun enregistrement. Vestige du commit
initial, de l'époque où un avatar était encore un compte Keycloak — prémisse
close depuis que l'EHO est devenu la base des avatars.

⚠ Surtout, il **contredisait la règle du jeu** : hors STARTEX, un joueur ne doit
rien savoir d'officiel. Or la page servait à tout joueur connecté **la bio et les
groupes des 453 avatars**. *« Mon EHO » cachait ce que « Choix d'avatar »
distribuait, dans le même menu, au même joueur.*

## Décision
Entrée retirée du menu, **page supprimée**. Le menu joueur se réduit à
`Mon EHO` · `EHO GT` · `Planche relationnelle`.

## Conséquences / à respecter
- ⚠ **Ne pas le réintroduire** : un écran qui liste les avatars n'a de sens que
  **côté animation**.
- ⭐ **Effet de bord qui débloque un chantier** : cette page était le **seul écran
  joueur** à consommer l'annuaire. Le verrou qui empêchait de réduire la charge
  utile pour les non-admins a donc sauté — un joueur connecté peut encore y lire
  ce que sa planche lui cache. **Arbitrage toujours ouvert.**

## 🔗 Source de vérité
`PLEIADE/MEMOIRE.md` (§ vocabulaire d'interface, § faille des routes API) et le
commit `0371bdf` du dépôt `eho`.
