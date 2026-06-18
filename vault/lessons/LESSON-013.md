---
id: LESSON-013
type: lesson
title: Serveur HTTP Python local lent → double pile IPv6 + Nagle + cache
tags: [perf, serveur, reseau, python, ipv6]
source: ../../MASTAURIGE/MEMOIRE.md
linkedTo: [ARCH-008]
relevantFor: [mastaurige, technique]
tier: 2
created: 2026-06-17
updated: 2026-06-17
---

# LESSON-013 — Pourquoi un serveur HTTP Python local « rame »

## Symptôme
Pages très lentes à charger (même sur poste puissant). Mesure : `GET /` via **`127.0.0.1` = 16 ms** mais via **`localhost` = 2033 ms**.

## Cause racine (la principale)
`localhost` (et les noms de machine) sont souvent résolus en **IPv6 `::1` d'abord**. Si le serveur n'écoute qu'en **IPv4 (`0.0.0.0`)**, le navigateur tente l'IPv6, échoue (~2 s), puis se rabat sur IPv4 — **à chaque nouvelle connexion**.

## Correctifs (du plus impactant au moindre)
1. **Écouter en double pile** : bind `::` avec `IPV6_V6ONLY=0` (IPv6 **et** IPv4) → 2033 ms → 29 ms. Repli IPv4 si IPv6 indispo.
2. **Keep-alive** : `protocol_version = "HTTP/1.1"` (connexions réutilisées).
3. **Désactiver Nagle** : `TCP_NODELAY` + bufferiser la sortie (`wbufsize`) → fin des pauses ~200 ms (ACK différé). `templates.js` 287 Ko : ~690 ms → 2 ms.
4. **Cache conditionnel** : `Last-Modified` + `304 Not Modified` → on ne re-télécharge que ce qui a changé (clé quand l'UI se rafraîchit par rechargement).
5. **Table MIME fixe** au lieu de `mimetypes.guess_type` (qui lit le registre Windows au 1ᵉʳ appel).

## À retenir
Avant d'incriminer la machine ou le LAN : **mesurer `127.0.0.1` vs `localhost`**. Un écart = problème de pile IP, pas de puissance.

## Source
[[../../MASTAURIGE/MEMOIRE.md]] § correctif perf. Architecture : [[ARCH-008]].
