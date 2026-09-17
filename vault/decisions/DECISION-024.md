---
id: DECISION-024
aliases: ["DECISION-024"]
type: decision
title: LEAC — une saisie annulée ne remonte pas ; le compactage du journal est une question de justesse, pas de volume
tags: [leac, synchronisation, hors-ligne, crdt, conception]
source: ../../LEAC/MEMOIRE.md
linkedTo: [ARCH-014, DECISION-021, DECISION-023]
relevantFor: [leac, pleiade]
tier: 1
created: 2026-09-17
updated: 2026-09-17
---

# DECISION-024 — Ne pas remonter ce qui n'a rien changé

## Contexte / problème
Constat de l'utilisateur à l'usage : poser une note puis la retirer laissait
**deux** opérations en attente. Écrire un paragraphe en cinq reprises en
laissait cinq. L'écran annonçait « 7 saisies à remonter » pour un état revenu à
son point de départ.

La question posée était celle du **volume**. La vraie raison est plus grave.

## ⭐⭐ Le vrai argument : la justesse, pas le volume
Serveur à « rien ». Tablette A pose 3, se ravise, retire sa note. Tablette B,
hors ligne elle aussi, pose 4 sur le même point.

- **A remonte son retrait** : celui-ci porte une horloge **plus récente** que le
  4 de B. À la fusion, le retrait gagne et **efface le travail de B** — alors
  que A n'a rien changé, il a écrit puis annulé.
- **A ne remonte rien** : le 4 de B tient. C'est le seul résultat correct.

Une opération **nette nulle** n'est donc pas seulement inutile : elle **écrase
le travail d'autrui au nom d'un geste qui n'a pas eu lieu**.

## Décision
Pour une cible donnée, tant qu'**aucune** opération n'est partie, on ne garde
que l'**écart net** par rapport à ce que le serveur connaît déjà. Écart nul,
rien ne reste.

⚠⚠ **Jamais une opération déjà remontée.** Elle appartient à l'histoire
commune : d'autres l'ont reçue, le serveur l'a rangée. Revenir dessus localement
ne l'effacerait nulle part ailleurs — on perdrait seulement de vue ce qu'on a
envoyé.

## Conséquences / à respecter
- **Une quatrième table locale : `socle`** — ce que le serveur connaît de chaque
  cible. Sans elle, impossible de distinguer une saisie qui change quelque chose
  d'une saisie qui ramène la cible à son état d'origine.
- ⚠ Le socle se met à jour **même quand une opération distante n'est pas
  appliquée à l'écran** : « ce que le serveur détient » et « ce que j'affiche »
  sont deux choses différentes, et c'est au premier que la prochaine saisie doit
  se comparer.
- ⚠ **`0` et `false` ne sont pas vides.** Un poids à 0 neutralise une fonction :
  c'est une décision du chef de contrôle, pas une absence. Sous test.
- **Ce qu'on perd, assumé** : les états intermédiaires d'une frappe. Le journal
  sert à **synchroniser**, pas à reconstituer les hésitations de quelqu'un. La
  traçabilité des actes relève de `JournalAudit` — autre table, autre sujet.
- ⚠ Toute migration de schéma qui crée le socle doit le **reconstituer**. Un
  socle vide signifie « le serveur ne connaît rien » et ferait **taire une
  suppression légitime** : retirer une note déjà remontée passerait pour un
  geste annulé, et le serveur la garderait pour toujours.

## 🔗 Source de vérité
Détail complet : voir `source:` ci-dessus. **Cette note ne recopie pas — elle pointe.**
