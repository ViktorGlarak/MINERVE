---
id: DECISION-030
aliases: ["DECISION-030"]
type: decision
title: Modèles d'EHO — ce qui doit exister sur TOUTE zone entre dans l'image, pas dans le volume
tags: [pleiade, eho, modeles, avatars, deploiement, portraits]
source: ../../PLEIADE/MEMOIRE.md
linkedTo: [DECISION-029, LESSON-038, LESSON-039]
relevantFor: [pleiade, delattre, mastorion]
tier: 1
created: 2026-09-21
updated: 2026-09-21
---

# DECISION-030 — « SKOLKAN PERSONA 21.09.26 », modèle INTÉGRÉ

## Contexte / problème
Sur la zone `delattre-26`, le catalogue de modèles d'eho ne proposait que
« VIERGE ». Le modèle `SKOLKAN` capturé le 15/09 n'existait que dans le
**volume de données du poste** (`EHO_DATA_DIR/templates/`), donc nulle part
ailleurs. L'utilisateur voulait le classeur des 453 avatars disponible
**sur cette instance et sur toute instance future**.

## Décision
Deux natures de modèles, à ne pas confondre :
- **capturé** — pris depuis l'écran, vit dans le volume de l'instance, local ;
- **intégré** — vit dans le dépôt (`eho/modeles/<code>/`), copié dans l'image,
  listé `builtin`, **non supprimable**, présent partout d'emblée.

« SKOLKAN PERSONA 21.09.26 » (453 avatars, 58 groupes, STARTEX, planche
officielle 43 nœuds / 56 liens, **118 portraits livrés**) devient un modèle
intégré.

## Pourquoi (alternatives écartées)
- Réimporter le JSON zone par zone : recommence à chaque nouvelle zone, et
  emporte le défaut ci-dessous.
- ⚠ **Défaut corrigé au passage** : un modèle capturé embarque des `avatar_url`
  **absolues vers le poste d'origine** (`http://localhost:3001/…`) — portraits
  cassés partout ailleurs. Dans un modèle intégré, elles sont **relatives** et
  les fichiers sont livrés ; l'application les rend absolues **pour l'instance**
  ([[LESSON-039]]).

## Conséquences / à respecter
- Les identifiants d'avatars sont **conservés** : le même avatar garde son
  `identityId` sur toutes les zones qui appliquent le modèle — utile pour toute
  reprise de contenu entre zones.
- L'application dépose les portraits dans le volume : elle suppose donc un
  volume **accessible en écriture** ([[LESSON-038]]).
- Appliquer un modèle reste un geste **destructeur** (sauvegarde automatique
  avant, plafonnée à 3) : le dire avant, jamais l'enchaîner à l'aveugle.

## 🔗 Source de vérité
Détail complet : voir `source:` ci-dessus. **Cette note ne recopie pas — elle pointe.**
