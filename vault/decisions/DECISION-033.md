---
id: DECISION-033
aliases: ["DECISION-033"]
type: decision
title: app-melmil — la planche des injects suit les trois niveaux de JEMM, et rien d'autre
tags: [melmil, jemm, pleiade, injects, planche, mastaurige, exercices]
source: ../../PLEIADE/JOURNAL.md
linkedTo: [PROJ-MASTAURIGE, ARCH-009, DECISION-002]
relevantFor: [pleiade, mastaurige, exercices, delattre]
tier: 1
created: 2026-09-22
updated: 2026-09-22
---

# DECISION-033 — Reprendre MELMIL en app de zone, sans réinventer son classement

## Contexte / problème
Le MELMIL de la boîte à outils MASTAURIGE demande, pour chaque exercice, de
déposer des `.json`, de lancer un `.bat`, puis d'écrire à la main le
calendrier et les lignes opératoires dans le HTML. Le rangement des injects
reposait sur une table **série → ligne opératoire** tenue à la main
(`lo_config.js`), qui devait être re-décidée à chaque exercice.

## Décision
Nouvelle app de zone PLÉIADE **`app-melmil`** (dépôt `cecpc-pleiade/app-melmil`,
12ᵉ dépôt), alimentée par **import d'un export JSON de JEMM depuis l'écran**,
et rangée sur **les trois niveaux que JEMM porte déjà** :

| JEMM | Sur la planche |
|---|---|
| **Event** | une **rangée** (colonne « EVENT ») |
| **Storyline** | une **carte colorée**, posée sur les jours où elle joue |
| **Injection** (dit *incident*) | une **ligne dans la carte** |

Rien d'autre n'est inventé : **aucune ligne opératoire à configurer**.
Ce que JEMM ne dit pas — les **phases d'exercice** (CONVEX, WU TEC, WU TAC,
CAX 1, 3A INTER, CAX 2) et les **jours GELEX** — se pose à l'écran, **par
plage de dates** et non jour par jour.

## Pourquoi (alternatives écartées)
- **Garder le routage série → LO** : c'est précisément ce qui demandait une
  décision humaine par exercice, et qui divergeait.
- **Régler les phases jour par jour** : un exercice de deux cents jours aurait
  demandé deux cents lignes ; une plage en demande une.
- **Faire gagner une phase sur l'autre en cas de chevauchement** : écarté par
  l'utilisateur — un chevauchement est une **information**, la zone est donc
  **rayée des deux couleurs**, et c'est l'animateur qui juge.

## Conséquences / à respecter
- ⚠ **Premier essai en `localStorage`** : la planche n'est **pas partagée**
  entre postes. L'état est exportable en un fichier.
- ⚠ La continuité d'une carte se juge en **colonnes** : une storyline qui
  joue deux jours de suite = **une carte** ; la même qui revient plus tard =
  **une autre carte**.
- ⚠ Un ré-import **ne supprime jamais** un inject absent de l'export : il le
  **signale** (défaut connu de la chaîne MASTAURIGE, qui écrasait le socle).
- ⏳ Reste à faire : pousser `catalog/melmil.yml` (branche locale
  `catalogue-melmil`), `pleiade-promouvoir` + sudoers côté serveur, puis v1
  (état partagé, rôle animateur, contenus MASTAURIGE, impression).

## 🔗 Source de vérité
Détail complet : `source:` (2026-09-22, suites 1 à 11) et
`C:\CECPC\pleiade\app-melmil\README.md`. **Cette note ne recopie pas.**
