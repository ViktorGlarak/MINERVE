---
id: LESSON-035
aliases: ["LESSON-035"]
type: lesson
title: Un build applicatif qui passe ne prouve RIEN pour un déploiement conteneurisé — reproduire l'image en local
tags: [leac, pleiade, deploiement, docker, podman, ci]
source: ../../LEAC/JOURNAL.md
relevantFor: [leac, pleiade, mastorion]
linkedTo: [LESSON-033, ARCH-013]
tier: 1
created: 2026-09-17
updated: 2026-09-17
---

# LESSON-035 — `npm run build` ne voit pas ce qui casse une image

## Symptôme observé
La première mise en production de LEAC échoue sur **`exit code 125`**, après
2 min 29 s de build. J'avais vérifié `npm run build`, `tsc`, `eslint` et les
214 tests — **sept fois**, tous verts — et conclu que tout allait bien.

## Cause racine
**Deux défauts, et aucun des deux n'est dans le champ de `npm run build`** :

| Défaut | Pourquoi le build applicatif ne le voit pas |
|---|---|
| Le dépôt n'avait pas de dossier `public/` | Next n'en a pas besoin. Seul le `COPY --from=builder /app/public` du `Dockerfile` échoue. ⚠ Et **Git n'enregistre pas un dossier vide** : le créer ne suffit pas, il faut y mettre un vrai fichier |
| `docker-entrypoint.sh` extrait en **CRLF** | Le script n'est jamais **exécuté** pendant la construction. Au démarrage, le noyau cherche un interpréteur dont le nom se termine par un retour chariot et rend « no such file or directory » — en désignant un fichier qui est pourtant là |

Le `Dockerfile` avait été repris d'une app voisine (`app-messagerie`) qui, elle,
a un `public/`. Copier un fichier d'infrastructure sans vérifier ses hypothèses.

## Correctif / règle à appliquer
⭐ **Avant toute mise en production, construire l'image et la faire tourner** —
depuis un **clone propre**, jamais depuis la copie de travail, qui contient des
fichiers ignorés par Git :

```bash
git clone "file:///chemin/du/depot" /tmp/essai && cd /tmp/essai
docker build -t essai -f Dockerfile .
# puis démarrer avec une vraie base et interroger la sonde
```

Trois minutes, et cela valide **ce que rien d'autre ne valide** : que
`prisma db push` applique réellement le schéma. C'est ainsi qu'avait déjà été
trouvé l'index sur une colonne `TEXT`, que MySQL refuse.

⚠ **Vérifier avant de « réparer »** : le CRLF venait de `core.autocrlf=true` sur
le poste Windows, mais le blob stocké dans Git était bien en **LF** — contrôlé
avec `git show HEAD:fichier | od -c`. Le serveur n'était donc pas touché. Sans
cette vérification, j'aurais corrigé un problème que le dépôt n'avait pas et
laissé le vrai en place. Un `.gitattributes` (`*.sh text eol=lf`) ferme la classe
entière. ⚠ **Aucun dépôt PLEIADE n'en a** : le piège y est latent partout.

## 🔗 Source de vérité
Détail / trace : voir `source:`. **Pointeur, pas copie.**
