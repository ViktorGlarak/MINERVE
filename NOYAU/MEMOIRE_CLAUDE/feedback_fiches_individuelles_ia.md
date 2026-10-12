---
name: feedback-fiches-individuelles-ia
description: "Avatars IA : pour l'instant on perfectionne les FICHES INDIVIDUELLES en plus du moteur de groupe (décision utilisateur 2026-10-11) ; l'ancrage des fiches viendra plus tard"
metadata:
  type: feedback
  originSessionId: 699185de-99a6-4263-a321-d605be7e2b29
  modified: 2026-10-11T18:23:14.534Z
---

Le 2026-10-11, l'utilisateur a corrigé une mauvaise compréhension de ma part : « base ancrée » (page Population IA : les effectifs et les % ne réécrivent jamais une fiche) ne voulait PAS dire « fiches intouchables ». **Pour le moment on a la main sur les fiches individuelles** : en plus de corriger le moteur (règles de groupe, voix de cohorte), on s'autorise à **perfectionner chaque fiche de comportement** pour que tout soit 100 % cohérent et le plus proche possible de la réalité. À terme les fiches seront ancrées.

**Why:** les relevés de population ne corrigeaient que le collectif ; les 4-5 avatars de base, eux, avaient été réglés un par un (Weber, Marina…) et c'est ce niveau de finition qui est attendu pour les 105.

**How to apply:** à chaque relevé PSYCHOLOGUE (`releve-population.mjs`), produire la liste nominative d'anomalies ; PSYCHOLOGUE propose une correction précise par avatar ; PLEIADE l'applique par `corriger-fiches.mjs` (PUT `comportement-ia`, note datée dans `_note`, mémoire d'exercice intacte) ; le pont recharge la fiche à chaud (`updatedAt`). Ne jamais re-tirer une orientation par ce canal. Voir [[projet-avatars-ia]], [[agent-psychologue]].

**Sur le serveur (aucune clé sur le poste, outillage du 2026-10-11, pas encore poussé)** : l'utilisateur fait « Exporter pour analyse » dans le Moteur IA → `releve-population.mjs --export=<fichier>` ; corrections PSYCHOLOGUE → l'utilisateur fait « Télécharger les fiches » dans eho (Population IA) → `corriger-fiches.mjs corrections.json --fiches=<export eho> --sortie=import.json` → l'utilisateur dépose `import.json` dans « Importer » (vérification, puis Appliquer). Fichiers dans `%USERPROFILE%\.pleiade\analyses-ia\`. Cohorte, orientation et opinions de départ : refusées par l'import.
