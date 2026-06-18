---
id: DECISION-008
type: decision
title: Accès serveur collaboratif — PIN animateur + vue joueur (pas de .exe)
tags: [mastaurige, serveur, collab, pin, joueur, securite]
source: ../../MASTAURIGE/MEMOIRE.md
linkedTo: [ARCH-008, PROJ-MASTAURIGE, PROJ-AURIGE-7BB]
relevantFor: [mastaurige, technique, exercices]
tier: 2
created: 2026-06-18
updated: 2026-06-18
---

# DECISION-008 — Deux publics sur le serveur collab : animateur (PIN) vs joueur

## Contexte / problème
Besoin : sur le même réseau, donner aux **joueurs** une vue MASTAURIGE **lecture seule** (fil publié), distincte de la vue **animateur** (complète + collaboratif : brouillons, camps, LO, synchromatrice). Question posée : faut-il un **`.exe`** distribué par profil ?

## Décision
**Non au `.exe`.** On garde **navigateur + serveur central** et on gate par **PIN côté serveur** :
- **Animateur** (PIN requis) : `/` + `/etat` `/flux` `/maj` … + instance complète.
- **Joueur** (ouvert) : `/joueur/` = kit `JOUEURS_WEB_VERSION` lecture seule, alimenté **uniquement** par `/actus` (paquet publié, badges de camp retirés).
- **Publication manuelle** : l'animateur upload `actus_*.json` via `/publier` → les joueurs reçoivent au rafraîchissement (garde de version, pas de boucle).
- Prototypé + testé sur la **vierge de test** `D:\CECPC\MASTAURIGE\SERVEUR_COLLABORATIF` ; **pas encore porté sur MINAUTORE** (après validation navigateur).

## Pourquoi (alternatives écartées)
- **`.exe` (PyInstaller/Electron)** : bloqué probable par **AppLocker** (postes verrouillés), faux-positifs antivirus, **redéploiement à chaque MAJ**, ≥ dizaines de Mo — et **ne résout pas** la séparation des vues (logique applicative, identique navigateur/exe).
- **Cacher l'UI animateur en CSS** : ÉCARTÉ — le joueur recevrait quand même `/etat`+`/flux` (fuite de brouillons/camps = exercice spoilé). La séparation doit être **côté serveur**.

## Conséquences / à respecter
- La vue joueur n'est **jamais** la page animateur masquée : kit séparé + feed assaini.
- PIN = `MAST_PIN` (à changer avant l'exercice réel). Niveau adapté à un **LAN d'exercice de confiance**, pas du durcissement anti-attaquant.
- ⚠ À porter sur MINAUTORE **après** validation navigateur (2 machines).

## 🔗 Source de vérité
[[../../MASTAURIGE/MEMOIRE.md]] § « DISPOSITIF PIN + VUE JOUEUR ». Architecture serveur : [[ARCH-008]].
