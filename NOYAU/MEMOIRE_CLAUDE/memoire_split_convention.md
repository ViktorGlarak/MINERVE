---
name: memoire-split-convention
description: "Axe 1 (22/07/2026) : MASTAURIGE mémoire scindée MEMOIRE.md (durable, 85 Ko) + JOURNAL.md (historique) ; convention pour toute mémoire d'agent qui gonfle"
metadata: 
  node_type: memory
  type: project
  originSessionId: 52feb2ec-047b-438f-b7ad-369a80dbc9a0
  modified: 2026-07-22T13:04:33.588Z
---

**Axe d'optimisation « mémoire compacte » réalisé le 2026-07-22.** Une mémoire d'agent qui grossit sans fin devient illisible avant de travailler.

**Fait :** `MASTAURIGE\MEMOIRE.md` (monté à **397 Ko**, au-delà de la limite de lecture d'un coup — or c'est LE fichier à lire avant toute intervention MASTAURIGE) a été **scindé** :
- **`MASTAURIGE\MEMOIRE.md`** = **état durable** (~85 Ko, lisible d'un bloc) : règles, conventions, capacités, architecture, registres avatars.
- **`MASTAURIGE\JOURNAL.md`** = **historique chronologique** append-only (~314 Ko) : ex-section « v0.2 FAIT FOI » (280 Ko) + journal d'activité daté. **Fait foi pour l'historique** ; consulté au `grep`.
Découpe via script Python (indices de ligne + assertions de garde, backup `.bak_20260722_split`) — rien perdu.

**Pointeurs mis à jour** : hook `mastaurige_memoire_reminder.py` (ne dit plus « section v0.2 FAIT FOI » → « CR daté dans JOURNAL.md, règle durable dans MEMOIRE.md ») + `CLAUDE.md` (2 endroits).

**Convention go-forward** (capitalisée dans `AURIGE\MEMOIRE.md` § méthodo point 12) : toute mémoire d'agent **actif** qui dépasse ~150 Ko ou n'est plus lisible d'un coup → scinder `MEMOIRE.md` (durable) + `JOURNAL.md` (daté). Exercice **CLOS** → bannière 🗄️ ARCHIVE en tête (fait pour MINAUTORE 7BB et GUILLAUME 2BB, qui restent lisibles ~118/80 Ko sans scission).

**Où écrire désormais un changement MASTAURIGE :** CR daté → `MASTAURIGE\JOURNAL.md` ; nouvelle règle/capacité durable → aussi `MASTAURIGE\MEMOIRE.md`.

**Why:** issu de l'analyse système du 2026-07-22 (axe n°1, choisi par l'utilisateur) — pousser le système plus loin sans dette.

**How to apply:** avant d'intervenir sur MASTAURIGE, lire `MEMOIRE.md` (suffit) ; pour un détail d'implémentation daté, `grep JOURNAL.md`. Voir [[project_mercure]], [[aurige7bb_actif]], [[agent_delattre]].
