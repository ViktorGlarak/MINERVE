---
id: DECISION-014
aliases: ["DECISION-014"]
type: decision
title: PLEIADE = le système global · MASTORION = seulement le réseau social (qui sera renommé)
tags: [pleiade, mastorion, perimetre, renommage, agents]
source: ../../PLEIADE/MEMOIRE.md
linkedTo: [ARCH-012, DECISION-015, ARCH-011]
relevantFor: [pleiade, mastorion, exercices]
tier: 1
created: 2026-09-11
updated: 2026-09-11
---

# DECISION-014 — PLEIADE est le système ; MASTORION n'est que le réseau social

## Contexte / problème
Le programme d'entraînement s'appelait « MASTORION » — nom porté à la fois par
le système entier et par l'application de réseau social. L'écosystème s'étant
structuré (orchestrateur, gestion d'avatars, infra), le nom unique devenait
ambigu.

## Décision
Décision utilisateur (2026-09-11) :
- **PLEIADE** = le **système global** — orchestrateur de zones d'exercice,
  instances d'applications, Keycloak centralisé, Traefik, serveur Podman + VPN.
- **MASTORION** = **seulement le réseau social**, une app du catalogue —
  **et son nom changera à terme** : ne jamais le figer dans une production.
- Organisation GitHub **`cecpc-pleiade`** (4 dépôts) ; l'ancien
  `XTalandier/mastorion-v0` et ses clones locaux sont **dépassés**.

## Pourquoi (alternatives écartées)
Garder « MASTORION » comme nom du système : entretenait la confusion entre le
tout et une de ses parties, et bloquait le renommage à venir du réseau social.

## Conséquences / à respecter
- **Agent PLEIADE créé** (22ᵉ) pour le système ; l'agent MASTORION est
  **recadré** sur l'intérieur de l'application.
- Routage : architecture / zones / Keycloak / infra / déploiement → **PLEIADE** ;
  API social, scénarios, cockpit, sentinel → **MASTORION**.
- Travailler dans `D:\CECPC\PLEIADE\` (plus dans `D:\CECPC\MASTORION\`).

## 🔗 Source de vérité
Détail complet : voir `source:` ci-dessus. **Cette note ne recopie pas — elle pointe.**
