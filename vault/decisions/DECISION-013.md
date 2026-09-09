---
id: DECISION-013
aliases: ["DECISION-013"]
type: decision
title: L'app EHO est propriétaire des personas — l'Admin MASTORION ne gère que les comptes humains
tags: [mastorion, eho, personas, admin, import, roles]
source: ../../MASTORION/MEMOIRE.md
linkedTo: [ARCH-011, LESSON-027, LESSON-028, TOOL-016]
relevantFor: [mastorion, exercices]
tier: 2
created: 2026-09-09
updated: 2026-09-09
---

# DECISION-013 — L'app EHO propriétaire des personas ; l'Admin = humains seulement

## Contexte / problème
Dans MASTORION, les 452 personas d'exercice étaient mélangés aux comptes réels
(admins, joueurs) dans le panneau Admin, et l'import/export Excel y vivait aussi.
La mission EHO v2 introduit joueurs et animateurs comme comptes MASTORION :
le mélange devenait ingérable et dangereux (un import pouvait toucher un humain).

## Décision
Décision utilisateur (2026-09-09) : **l'app EHO (`apps/eho`) est l'outil du cycle
de vie des personas** — création, fiches, groupes, portraits, **import/export
Excel** (`/gestion`). **Le panneau Admin de MASTORION ne configure plus que les
comptes humains** (admins, animateurs, joueurs). Comptes joueurs = comptes
MASTORION standard (username+mdp), créés par l'animateur, **EHO par cellule**
(équipe d'1 possible), rôles `EHO_ANIM` / `EHO_PLAYER`.

## Pourquoi (alternatives écartées)
- Tout laisser dans l'Admin : mélange humains/personas, import dangereux, et
  un `EHO_ANIM` sans `APP_ADMIN` n'aurait rien pu faire.
- Filtrage purement visuel : refusé — l'isolation doit être **côté serveur**.

## Conséquences / à respecter
- Le service front EHO n'appelle **plus aucun** `/api/admin/*`.
- Admin : `comptes=humains` (paramètre **optionnel** — défaut = comportement
  historique, retouche minimale du code de Xavier).
- Critère structurel : **persona = compte sans aucun rôle** ; tout humain a un
  rôle → intouchable par import/modèles/suppression.

## 🔗 Source de vérité
Détail complet : voir `source:` ci-dessus. **Cette note ne recopie pas — elle pointe.**
