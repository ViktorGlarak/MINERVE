---
id: LESSON-038
aliases: ["LESSON-038"]
type: lesson
title: Une image à volume de données ne fixe pas USER — le dossier monté appartient à root
tags: [pleiade, docker, podman, volumes, eho, leac, deploiement]
source: ../../PLEIADE/MEMOIRE.md
linkedTo: [DECISION-030, LESSON-037]
relevantFor: [pleiade, leac, mastorion]
tier: 1
created: 2026-09-21
updated: 2026-09-21
---

# LESSON-038 — « EACCES: permission denied, mkdir '/app/data/uploads' »

## Ce qui s'est passé
Première application d'un modèle sur l'instance eho de `delattre-26` :
**EACCES**. L'image tourne en `USER nextjs` (uid 1001) ; l'orchestrateur monte
`./data:/app/data` depuis un dossier **qu'il crée lui-même en root** ; le
`chown` fait **dans** l'image est **recouvert par le montage**.

⚠ **Défaut latent de TOUTES les instances**, pas un accident de ce modèle :
rien ne pouvait écrire dans le volume — ni portrait téléversé, ni modèle
capturé, ni sauvegarde d'avant-application, donc **aucune** application de
modèle, VIERGE comprise. Il ne s'est vu qu'à la première écriture disque **en
production**. LEAC avait le même schéma (pièces jointes), également corrigé.

## Leçon
Le `chown` d'une image ne survit pas à un montage : c'est **le propriétaire
côté hôte** qui gagne. Une image qui reçoit un volume de données démarre donc
**root**, ajuste le volume, puis **abandonne root** :

```
entrypoint (root) → mkdir -p + chown -R nextjs:nodejs /app/data
                  → exec su-exec nextjs "$0" "$@"
```

⚠ **Piège de test** : un volume **neuf** est initialisé depuis l'image, donc
déjà bien possédé — le défaut ne s'y reproduit pas. Il faut tester sur un
volume **pré-rempli par root**, comme celui du serveur.

## Appliqué
- eho et `app-leac` : plus de `USER nextjs`, `apk add su-exec`, entrypoint
  corrigé. Vérifié en local sur un volume root : propriétaires, processus sous
  `nextjs`, écriture réelle dans `uploads/`.
- eho : le dépôt des portraits devient **best-effort** — un modèle s'applique
  même si ses portraits échouent, et le journal le dit.
- ⏭ À signaler à Xavier : press, messagerie et social ont vraisemblablement le
  même défaut. Alternative côté plateforme : que Pléiade `chown` le dossier
  `data` à l'uid de l'app à la création de l'instance.
- ⚠ Sous Git Bash, `docker exec … /app/data` est converti en chemin Windows :
  `MSYS_NO_PATHCONV=1`.
