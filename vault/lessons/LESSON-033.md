---
id: LESSON-033
aliases: ["LESSON-033"]
type: lesson
title: Ne jamais écrire un chemin Windows en littéral dans un script de substitution
tags: [outillage, piege, python, windows, documentation]
source: ../../PLEIADE/JOURNAL.md
linkedTo: [LESSON-032, DECISION-019]
relevantFor: [outillage, pleiade, mastaurige]
tier: 2
created: 2026-09-16
updated: 2026-09-16
---

# LESSON-033 — Un antislash dans un script, et la documentation devient fausse

## Symptôme observé
Une substitution de masse censée écrire `C:\CECPC\pleiade\app-social` dans les
fichiers de documentation a produit `C:\CECPC\pleiadepp-social` — avec un
caractère **invisible** au milieu. Le chemin était faux **et illisible à l'œil** :
rien ne signalait l'erreur dans le rendu.

## Cause racine
`\a` est une séquence d'échappement valide (**BEL**, 0x07). Dans un chemin
Windows écrit en littéral, `…\app-social` devient donc « BEL + pp-social ».
Sournois : `\C` et `\p` **ne sont pas** des échappements valides et passent
intacts — l'erreur ne frappe que certaines lettres (`\a`, `\b`, `\f`, `\n`,
`\r`, `\t`, `\v`, `\0`, `\x`…), ce qui la rend imprévisible.

## Correctif / règle à appliquer
1. **Passer par l'outil d'édition** plutôt qu'un script, dès que c'est possible :
   il prend le texte littéralement.
2. Si un script est nécessaire : **composer l'antislash** (`chr(92)`) ou utiliser
   une chaîne brute — **jamais** un chemin Windows tapé tel quel.
3. ⭐ **Balayer les caractères de contrôle après toute substitution de masse** sur
   des `.md` : un simple parcours des caractères `< 32` hors `\n\r\t` a suffi à
   trouver celui-ci — et en a révélé un **second, antérieur**, dans
   `DELATTRE/MEMOIRE.md` (0x01), que personne n'avait vu.

## Pourquoi ça compte ici
La documentation du projet **est** un livrable : `CLAUDE.md` est la source de
vérité, et un chemin faux y envoie la session suivante à une adresse morte. Même
famille que [[LESSON-032]] : **l'outil se tait, l'utilisateur paie.**

## 🔗 Source de vérité
Trace datée : `PLEIADE/JOURNAL.md`, séance du 2026-09-16.
