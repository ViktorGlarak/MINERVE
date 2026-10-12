---
name: vierge-porting-fin-minautore
description: "Portage de la vierge MASTAURIGE post-MINOTAURE : v0.3 FAIT le 2026-07-22 (moteur MELMIL/CSS, STARTEX, statuts) ; RESTE le kit JOUEURS à blanchir + 6 fichiers à merger"
metadata: 
  node_type: memory
  type: project
  originSessionId: 52feb2ec-047b-438f-b7ad-369a80dbc9a0
  modified: 2026-07-22T12:03:12.148Z
---

Portage du gabarit **VIERGE** `D:\CECPC\MASTAURIGE\LOCALSTORAGE_WEB_VERSION`, débloqué par la fin de MINOTAURE/7BB. **Backup avant portage : `D:\CECPC\MASTAURIGE\_BACKUP_VIERGE_20260722_portage`.**

## ✅ FAIT — v0.3, 2026-07-22 (détail : `CHANGELOG.md` de la vierge + `MASTAURIGE\MEMOIRE.md`)
- `MELMIL\melmil.js` remonté en entier (77→99 Ko) **avec réinjection du `DAY_MAP` NEUTRE** (d1→d10). Gains : **support du format JEMM `XX.YY.Izz`** (la vierge ne gérait QUE l'ancien `XX.YY.ZZi` !), **split de card sur plusieurs jours** (sous-inject `XX.YY.Izz<Lettre>`), **les 3 correctifs calendrier** (bugs 2BB encore EN DUR), +15 fonctions génériques, « STARTER »→« STARTEX PACKAGE ».
- `MELMIL\melmil.css` remonté (+80 lignes, 0 perte) — classes `.inj-jemm-locked`, `.jemm-tag`, `.sl-band-bar` sinon absentes.
- `moteur\starter_package.js` **créé générique** (`ART = []`) + inclus dans `index_master.html` → STARTEX = emplacement permanent.
- `moteur\statuts_data.js` **créé** (store **vide**) + inclus tôt dans le `<head>` → statut de production permanent.
- `shared\back-btn.js` : CSS impression.
- ✅ `node --check` (tous les .js) + `py_compile` (tous les .py) = 0 échec.

## ⏭ RESTE À FAIRE
**1. Kit JOUEURS vierge à BLANCHIR** — `D:\CECPC\MASTAURIGE\JOUEURS_WEB_VERSION` contient **toujours MINOTAURE** (vérifié 2026-07-22 : `bios.js` 114 Ko, 2 `moteur/actus/lot_*.js`, `ACTUS/` 1 entrée, `Sites/` 7 dossiers, `articles_data.js` 8 Ko). Approche propre : merger d'abord les outils ci-dessous, **puis RÉGÉNÉRER** le kit via `OUTILS\GENERER_KIT_JOUEURS.py` (sort un jour-0 propre). Génériques à conserver : auto-load actus avant le rendu inline + stub `ACTUS_LOTS=[]` ; EHO (rôle/âge, RZO `rzoBands`, cartes éditables, `back-btn.js`, export `EHO_EDITS`) ; bouton « Importer les actus » retiré.

**2. Six fichiers à MERGER (pas à copier)** — ⚠ **la vierge n'est PAS qu'en retard, elle a ses propres évolutions** ; diffé DANS LES DEUX SENS avant d'écraser :
- `OUTILS\GENERER_KIT_JOUEURS.py` — 86 lignes master vs 4 vierge → **le plus rentable**, à faire avant le blanchiment.
- `OUTILS\verifier_mastaurige.py` — la vierge a le CONTROLE I (avatars↔trombino) que le master n'a pas.
- `moteur\createur.js` — la vierge a `splitTime` (séparation jour/heure).
- `moteur\tweets_engine.js` · `MELMIL\SYNCHROMATRICE\synchromatrice.js` (7 marqueurs 7BB → à neutraliser).
- `MASTAURIGE\EXE_MASTER_VERSION` : vérifier que le correctif courrier est bien présent.

*(✅ `MELMIL\generer_melmil.py` RÉGLÉ le 2026-07-22 — décision utilisateur « **on garde le JEMM** » : `jemm_code()` retourne le Literal TEL QUEL, la conversion vers l'ancien format cassait le rattachement des cards. Reste un écart mineur : défaut `etat` = `Draft` côté vierge vs `Validated` côté master.)*

**NE PAS porter** : `moteur\joueur.js` (**la vierge est EN AVANCE** : visionneuse overlay + repli `Sites/`), `OUTILS\CONFIGURER_EXERCICE.py` (génère le `DAY_MAP` d'un nouvel exercice = sa raison d'être), `moteur\articles_data.js` (10 PROTOTYPES gardés exprès), et les données par exercice (`melmil_data.js`, `tweets_data.js`, `avatars.js`, `lo_config.js`).

**Why:** la vierge conditionne tous les futurs exercices ; elle contenait encore les bugs calendrier 2BB et ignorait le format JEMM.

**How to apply:** ⚠ **NE JAMAIS relancer `OUTILS\GENERER_VIERGE.py` (côté 2BB)** — il régénérerait la vierge depuis le 2BB = **ROLLBACK** total (avertissement écrit dans `MASTAURIGE_VERSION.txt`). Après tout portage de moteur, **vérifier les classes CSS** utilisées. Voir [[mastaurige_vierge_chemin]], [[aurige7bb_actif]], [[aurige_template_base]].
