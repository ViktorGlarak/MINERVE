---
name: trombino-img-convention
description: "Convention : les photos du trombinoscope vivent dans Trombinoscope/img/ (auto-contenu) — ne pas aller les chercher dans CREATION/WEB"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 9cd755be-0651-44f5-8932-5974a21bced9
---

**Les portraits du trombinoscope sont centralisés dans `Trombinoscope/img/`** (dossier auto-contenu), mis en place le **2026-06-04**. Le HTML les référence en **`src="img/<nom>"`** (relatif au dossier du trombino) — **plus de chemins fragiles** `../../../../../../CREATION/…` ni `../images/`.

**Why:** demande utilisateur — « plus propre et efficace que de te laisser aller chercher les photos dans tous les dossiers ». Avant : le trombino pointait sur CREATION (6 niveaux) + `WEB/images/`, et dans la **vierge** les images étaient **cassées** (portraits CREATION non livrés).

**How to apply :**
- Pour ajouter une personnalité au trombino : **copier sa photo dans `Trombinoscope/img/`** (nom ASCII sans espaces) puis référencer `src="img/<nom>"`. Ne pas pointer ailleurs.
- `src="img/…"` fonctionne **à l'identique** en 2BB (`WEB/Trombinoscope/img/`) et dans la vierge (`Sites/Trombinoscope/img/`) — pas de réécriture de chemin.
- Le **générateur** `GENERER_VIERGE.py` copie désormais `Trombinoscope/img/` → vierge (et ne réécrit plus que `index_master`/`shared`).
- Fiches `<img>` : garder le fallback `onerror=…actor-initials` (initiales si photo absente).

Voir [[mastaurige]], [[methode_web_exercices]]. Tikhanov (@S_Tikhanov) & Saniki (@A_Saniki) ajoutés à la page **Bothnia** du trombino le 2026-06-04 (opposition nationaliste pro-MER) — fiches doctrine dans `ANALYSTE\BOTHNIA` ; camp = registre MASTAURIGE.
