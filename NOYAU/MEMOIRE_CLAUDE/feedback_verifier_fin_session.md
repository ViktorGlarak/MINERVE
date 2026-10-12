---
name: feedback-verifier-fin-session
description: "Réflexe obligatoire : lancer verifier_mastaurige.py en fin de chaque session de production AURIGE, avant de rendre la main"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 9cd755be-0651-44f5-8932-5974a21bced9
---

En fin de **chaque** session de production AURIGE (création/intégration d'injects dans MASTAURIGE), lancer le validateur **avant** de clôturer :
`…\MASTAURIGE\WEB\OUTILS\verifier_mastaurige.py` (double-clic `VERIFIER.bat`, ou `'' | py verifier_mastaurige.py` en non-interactif).

**Why:** Le 2026-06-02, 4 tweets ont été ajoutés à `tweets_data.js` sans leurs entrées `ANIM_DATA`/`LO_BY_KEY` → encadré info animateur vide ; l'utilisateur a dû le signaler. Or le validateur **avait déjà** le contrôle (CONTROLE A/B) qui l'aurait attrapé. Le manque n'était pas l'outil, mais le réflexe de le lancer.

**Cause racine structurelle = vérité dupliquée :** un tweet/article porte `num`+`lo` dans `tweets_data.js` (rendu) ET dans `ANIM_DATA`/`LO_BY_KEY` d'`index_master.html` (encadré animateur). Créer 1 inject = jusqu'à 5 touchpoints dans 2-3 fichiers → lent et fragile. Refonte « source unique » proposée mais non retenue pour l'instant ; en attendant, le validateur est le filet.

**How to apply:**
- Tout nouveau tweet ajouté à la main dans `tweets_data.js` → ajouter AUSSI son entrée `ANIM_DATA` + `LO_BY_KEY` (clé = id du tweet) dans `index_master.html`. (Le créateur de tweets intégré le fait seul ; l'édition fichier directe, non.)
- Tout nouvel avatar → `avatars.js` + trombinoscope (`ACTEURS_A3_AURIGE2BB.html`).
- Lancer VERIFIER ; viser « TOUT EST BON » avant de rendre la main. Contrôles : A (tweet→info), B (article→info+fichier), G (camp tweet↔avatar), H (num/LO `tweets_data.js`↔`index_master`), I (avatar↔trombinoscope). Voir [[mastaurige]].
