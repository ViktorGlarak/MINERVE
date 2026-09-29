---
id: LESSON-041
aliases: ["LESSON-041"]
type: lesson
title: Une donnée qui n'existe que sur l'appareil doit demander la persistance — et c'est l'installation qui l'obtient
tags: [leac, indexeddb, stockage, pwa, tablette, hors-ligne, eviction]
source: ../../LEAC/MEMOIRE.md
linkedTo: [DECISION-032, LESSON-040, ARCH-014, LESSON-037]
relevantFor: [leac, pleiade, mastorion]
tier: 1
created: 2026-09-22
updated: 2026-09-22
---

# LESSON-041 — « Best-effort » veut dire « effaçable »

## Symptôme observé
Le carnet de terrain vit dans IndexedDB et **n'a aucune copie ailleurs**
([[DECISION-032]]). Par défaut, ce stockage est **« best-effort »** : un
navigateur à court de place peut **vider** les données d'un site, sans rien
demander. Une semaine de notes et de vocaux tiendrait à la place libre sur la
tablette.

## Cause racine
Le réflexe « c'est écrit dans la base locale, donc c'est gardé » est faux. La
garantie s'appelle **`navigator.storage.persist()`**, et elle se **demande**.
⚠ Mesuré le 2026-09-22 : dans un navigateur ordinaire, elle est **REFUSÉE** —
Chromium la réserve aux sites **installés** ou très fréquentés. J'avais écrit
un contrôle qui l'affirmait accordée : **c'est le contrôle qui avait tort, pas
le produit**. On ne décide pas à la place du navigateur.

## Correctif / règle à appliquer
1. Toute donnée **sans copie serveur** demande la persistance à l'ouverture.
2. On **ne suppose jamais** qu'elle est accordée : on lit la réponse, et
   quand c'est non, **l'écran le dit** avec ce qu'il faut faire.
3. ⭐ **Ce qui l'obtient sur le terrain : installer l'application sur l'écran
   d'accueil** de la tablette (LEAC a déjà manifeste et service worker). À dire
   aux contrôleurs, c'est une consigne d'emploi, pas un détail technique.
4. Un échec d'écriture (`QuotaExceededError`) rend un **motif clair** — sans
   quoi l'écran n'affiche simplement « rien de nouveau », et l'utilisateur croit
   son travail enregistré. Même famille de défaut que [[LESSON-037]] : ne
   jamais laisser un indicateur dire autre chose que ce qu'il mesure.

## 🔗 Source de vérité
Mesures et détail : `source:` (Règle 29) et `LEAC/JOURNAL.md` du 2026-09-22.
**Pointeur, pas copie.**
