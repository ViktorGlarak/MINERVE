---
id: LESSON-021
type: lesson
title: Donner une photo à un avatar MASTAURIGE = 3 couches (feed + fichier + markup trombino)
tags: [mastaurige, avatars, trombinoscope, feed, images]
source: ../../MASTAURIGE/MEMOIRE.md
linkedTo: [PROJ-MASTAURIGE, AGENT-MASTAURIGE]
relevantFor: [mastaurige, exercices]
tier: 2
created: 2026-06-23
updated: 2026-06-23
---

# LESSON-021 — Photo d'avatar : feed et trombino sont DEUX mécanismes distincts

## Symptôme observé
Après avoir déposé l'image et câblé le feed, la photo apparaît dans index_master (feed) **mais pas dans le trombinoscope** (rond resté en initiales).

## Cause racine
Le feed et le trombino lisent l'avatar **différemment** :
- **Feed** : le rond vient du champ `avatar.{type,value}` du **tweet baké** (`tweets_data.js`) ; `avatars.js` ne sert qu'au créateur (et est strippé du kit joueur).
- **Trombino** (`Sites\Trombinoscope\ACTEURS_A3_model.html`) : section « Avatars RS » **hand-maintained**, markup figé par avatar — soit `<div class="avatar-rs-photo-wrap"><img src="img/MER_*.jpg" onerror=…>…</div>` (photo), soit `<div class="avatar-rs-initials">XX</div>` (**aucune balise img** → l'image du dossier n'est jamais référencée). Le générateur `generer_trombino_bios.py` n'injecte que le popup/cartes cliquables (idempotent) — il ne (re)génère pas cette section.

## Correctif / règle à appliquer
Pour donner une photo à un avatar, traiter **3 couches** :
1. déposer le `.jpg` (carré ~400², léger) dans **`assets\images\avatars tweet\`** (feed) **et** **`Sites\Trombinoscope\img\`** (trombino) ;
2. **feed** : passer `avatars.js` + chaque tweet du persona en `avatar.type "image"` (⚠ câbler **par handle**, jamais par initiales partagées — ex. « MK » = Maïa **et** Marion Kessler) ;
3. **trombino** : éditer le markup `ACTEURS_A3_model.html` (initiales → photo-wrap), puis **propager** (`OUTILS\sync_trombino_joueurs.py` — le hook de sync peut rater à cause de la casse du chemin).

## 🔗 Source de vérité
Détail : `MASTAURIGE/MEMOIRE.md` (2026-06-23). **Pointeur, pas copie.**
