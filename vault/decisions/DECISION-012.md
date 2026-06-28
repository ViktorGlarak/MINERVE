---
id: DECISION-012
aliases: ["DECISION-012"]
type: decision
title: avatars.js = liste maître des comptes RS — EHO généré + garde-fou VERIFIER
tags: [mastaurige, avatars, eho, verifier, casw]
source: "../../MASTAURIGE/MEMOIRE.md"
linkedTo: [PROJ-MASTAURIGE, AGENT-MINAUTORE, AGENT-ANALYSTE-ARN]
relevantFor: [mastaurige, avatars, outillage]
tier: 2
created: 2026-06-28
updated: 2026-06-28
---

# DECISION-012 — avatars.js = liste maître des comptes RS (EHO généré + garde-fou)

## Contexte / problème
Deux listes de comptes RS **manuelles et séparées** divergeaient : le **créateur** (`moteur/avatars.js`, lu par « créer un tweet ») et l'**EHO** (section ACTEURS de `Sites/Trombinoscope/ACTEURS_A3_model.html`). Constat : @ArnlandLovePeace présent dans l'EHO mais **pas sélectionnable** ; 9 comptes 7BB récents dans le créateur mais **absents de l'EHO**. De plus le **garde-fou camp** (VERIFIER) était **silencieusement inactif** depuis le déplacement de `avatars.js`/`tweets_data.js` vers `moteur/` (le vérificateur les cherchait à la racine → `tweets_data_driven=False` → CONTROLE G/H/I sautés).

## Décision
- **`moteur/avatars.js` = SOURCE UNIQUE** des comptes RS (handle, nom, **camp**, img/initiales). Le créateur la lit ; l'**EHO en est dérivée**.
- **Outil `OUTILS/generer_acteurs_addendum.py`** : (re)génère, entre marqueurs `ACTEURS_ADDENDUM`, les comptes d'avatars.js **absents** de la curation EHO → **addendum** qui préserve la mise en page A3. À relancer après tout ajout dans avatars.js.
- **VERIFIER réparé** : chemins → `moteur/` (réactive CONTROLE G camp + I) ; **CONTROLE A/B gatés sur `anim_keys`** (modèle data-driven 7BB : ANIM_DATA vide → checks 2BB inopérants) ; **CONTROLE I refait = bidirectionnel** avatars.js ⟷ EHO.

## Pourquoi (alternatives écartées)
- **EHO = maître** : l'EHO n'a que des initiales → on perdrait les photos jpg du créateur. Écarté.
- **Garder 2 listes + simple checker** : possible mais 2 fichiers à maintenir à la main. Maître + génération = moins d'entretien.

## Conséquences / à respecter
- Ajout d'un compte = **dans `avatars.js`** puis relancer `generer_acteurs_addendum.py`. **Réutiliser** un persona existant (roster Analyste pays + réserve **CASW**) avant d'en créer un (cf. mémoire harness `feedback-mastaurige-consultation`).
- Camps tranchés (user) : **@BC1_News = neutre** (peut pencher rouge) · **@MarionKessler57 = bleu**.
- ⚠ **Reste obsolète (à moderniser)** : VERIFIER détecte `Articles = 0` (les articles 7BB sont data-driven `articles_data.js`/`CR_previewArticle`, plus `openCard`) → contrôles articles inopérants.

## 🔗 Source de vérité
Détail technique complet : `source:` (`MASTAURIGE/MEMOIRE.md`, entrées 2026-06-28). **Cette note pointe, ne recopie pas.**
