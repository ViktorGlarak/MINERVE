---
name: feedback-indicateur-etat
description: "Un indicateur d'état doit mesurer exactement ce qu'il prétend rapporter, sinon ne pas l'afficher"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 7f9a0a6b-9fe5-457d-b4e3-f0b50bf62931
  modified: 2026-09-22T00:00:00.000Z
---

2026-09-21, Pléiade : j'ai ajouté au tableau de bord un voyant « cecpc Connect branché / à
brancher ». Il jugeait sur **deux** pièces (fournisseur d'identité **et** groupe maître) alors
que la chose rapportée — le bouton « cecpc » sur l'écran de connexion — **ne dépend que de la
première**. Résultat : une zone qui marchait s'affichait comme cassée. L'utilisateur l'a vu de
ses yeux et a demandé le retrait, en ajoutant que ce bouton devant être présent en permanence,
un bouton de réparation en façade n'avait pas lieu d'être. Retiré (revert `280b779`).

**Deuxième occurrence, le même jour (2026-09-21)** : ma sonde de déploiement d'eho comparait
l'**empreinte des fichiers statiques** de la page de connexion. Trois mises en production
successives ne touchaient que le **serveur** — aucun fichier client ne changeait, l'empreinte
restait identique, donc « pas déployé » trois fois de suite, à tort, pendant que
l'utilisateur réessayait. Même défaut de fond : je mesurais un **effet de bord**, pas la chose.
Corrigé : `GET /api/sante` → `{ version }` sur **eho** comme sur **LEAC** (`lib/version.ts`,
à incrémenter à chaque push sur `prod`). ⚠ Une sonde qui lit une liste peut aussi la trouver
**vide** pendant un redémarrage → faux positif ; exiger une réponse non vide.

**Why:** un indicateur qui se trompe coûte plus qu'il ne rapporte. On va vérifier à la main ce
qu'il affirme, puis on cesse de le croire, et il devient du bruit. ⚠ Mes 11 contrôles navigateur
étaient tous verts : ils vérifiaient que l'affichage suit l'API, jamais que l'API dit vrai. Un
simulacre écrit à partir de mon hypothèse ne peut pas la contredire.

**How to apply:** avant d'afficher un état, écrire noir sur blanc la question posée à
l'utilisateur, puis vérifier que la mesure y répond **exactement** — ni plus large, ni plus
étroite. Si la mesure est plus exigeante que la question, elle produira de fausses alarmes.
Tester au moins un cas contre le vrai système, pas seulement contre un simulacre. Pour un
déploiement, lire une **marque posée par le code** (version), jamais un effet de bord. Et se
demander si l'exception mérite une place permanente dans l'interface : voir
[[pleiade-deploy-mecanique]].
