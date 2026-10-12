---
name: mastaurige-vierge-chemin
description: Emplacement du gabarit vierge MASTAURIGE (web/localStorage) + générateur qui le produit
metadata:
  node_type: memory
  type: project
  originSessionId: 9cd755be-0651-44f5-8932-5974a21bced9
---

Le **gabarit vierge MASTAURIGE** (version web HTML / localStorage, v0.2) est à **`D:\CECPC\MASTAURIGE\LOCALSTORAGE_WEB_VERSION`** depuis le **2026-06-04**.

- Historique : `…\CREATION\08 - MASTAURIGE VIERGE` → `D:\CECPC\MASTAURIGE` (2026-06-03) → **`D:\CECPC\MASTAURIGE\LOCALSTORAGE_WEB_VERSION`** (2026-06-04).
- Le sous-dossier `LOCALSTORAGE_WEB_VERSION` distingue la **version web actuelle** (HTML + localStorage) d'éventuelles futures versions (`.exe` Tauri/Electron + IA locale envisagés — cf. discussion 2026-06-04).
- Structure : racine = `index_master.html` + docs ; dossiers `Sites/ moteur/ MELMIL/ assets/ shared/ OUTILS/ PS1/`.

**Produit par** `OUTILS\GENERER_VIERGE.py` (côté 2BB : `D:\CECPC\PRODUCTION\EXER\AURIGE 2BB\00_Boites à outils\MASTAURIGE\WEB\OUTILS\`). La constante `DST` (ligne 12) pointe désormais sur `D:\CECPC\MASTAURIGE\LOCALSTORAGE_WEB_VERSION`. **Source de vérité = le 2BB** ; relancer le script reconstruit la vierge à l'identique (reset + copie + chemins `../../` + blanking + renommage MELMIL→`melmil_ili.html`).

**Si la vierge est encore déplacée :** mettre à jour `DST` du générateur + ce mémo + [[transition-minautore]]. Voir [[methode_web_exercices]] et [[web_architecture]].
