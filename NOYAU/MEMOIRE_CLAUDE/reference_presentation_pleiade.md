---
name: reference-presentation-pleiade
description: "Où trouver la présentation de PLEIADE écrite par Xavier (PDF classé dans MINERVE) et ce qu'elle contient"
metadata: 
  node_type: memory
  type: reference
  originSessionId: 52feb2ec-047b-438f-b7ad-369a80dbc9a0
  modified: 2026-09-15T12:58:45.373Z
---

**`D:\CECPC\PRODUCTION\IA\MINERVE\PLEIADE\REFERENCES\Pleiade-presentation.pdf`** — la présentation de PLEIADE par **Xavier** (le développeur), 19 pages, créée le 2026-09-14, classée le 2026-09-15 depuis le Bureau de l'utilisateur. Sommaire page par page dans `REFERENCES/README.md` à côté.

Le propos : déployer en quelques minutes un **écosystème d'information complet et étanche** (réseaux sociaux, presse, messageries) pour entraîner journalistes, communicants et analystes. Une **zone** = une bulle par exercice. Points saillants : **ADMIN** (scénarios heure par heure en `T+hh:mm`, import XLSX, **greffe sur une publication existante, y compris d'un participant**) · **COCKPIT** (veille multi-apps, relevé 10 s, disposition personnelle exportable, priorités par source, reporting comparatif) · **réseau fermé, entrée par profil VPN nominatif** · `pleiade deploy --zone <Zone>` pour les développeurs.

**Why:** l'utilisateur voulait ce draft rangé dans le projet, retrouvable par lui comme par moi. C'est la seule vision d'ensemble écrite par l'auteur de la plateforme — utile avant toute discussion d'architecture avec Xavier.

**How to apply:**
- ⚠ **C'est un DRAFT de présentation, pas une spécification** : quand il contredit le code de `D:\CECPC\PLEIADE\`, **le code fait foi**.
- Deux écarts déjà relevés : les domaines y sont en `*.<zone>.pleiade.local` (le code porte encore `*.mastorion.internal` — renommage en cours) ; le catalogue compte **8 applications** et non 4 (`social` remplace `mastorion`, plus `admin`, `cockpit`, `messagerie`, `presse`).
- ⭐ **`admin` et `cockpit` recoupent le savoir MINERVE** (synchromatrice MELMIL, veille, RETEX) — piste à creuser, cf. [[retex_minotaure_26]].
- Convention : les documents de référence externes d'un agent vont dans `NOM_AGENT\REFERENCES\`, avec un `README.md` qui en donne le sommaire et la provenance (même schéma que `EXPERT_INFLUENCE\REFERENCES\`).
