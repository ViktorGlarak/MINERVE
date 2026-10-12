---
name: feedback-image-hero-card
description: "Règle AURIGE : l'image principale d'un article doit être à la fois le hero (Base64 dans l'article) ET la vignette de sa card dans index_master.html"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 9cd755be-0651-44f5-8932-5974a21bced9
---

Quand on intègre l'**image principale** d'un article AURIGE (MASTAURIGE), faire les **deux** à chaque fois :

1. **Hero de l'article** — image **en Base64** directement dans le fichier `Site …/XXX.html` (HTML autonome) : remplacer le bloc `<span class="hero-placeholder">[ PHOTO À PRODUIRE … ]</span>` par `<img src="data:image/jpeg;base64,…" alt="…" style="width:100%;height:100%;object-fit:cover;display:block;">`.
2. **Vignette de la card** dans `index_master.html` — **la même image**, en **référence fichier** (pas Base64) : remplacer la `<div class="card-thumb" style="…">TEXTE</div>` par `<div class="card-thumb"><img src="./images/NOM.jpg" alt="…"></div>` (modèle : card Guterres).

**Why:** l'utilisateur a demandé (02/06) que l'image principale serve aussi de vignette de card — cohérence visuelle animateur. Le hero en Base64 garde l'article autonome (zip offline) ; la vignette en réf fichier évite d'alourdir `index_master.html` (l'image vit dans `WEB/images/`).

**How to apply:**
- Embarquer le Base64 **sans PowerShell** : l'AMSI/antivirus bloque le motif `ToBase64String`+`data:image`. Utiliser un petit script **Python** jetable (`base64.b64encode` + `re.subn` du placeholder) lancé via `py`, puis le supprimer. (Alternative projet : `certutil -encode`.)
- Vignette : cibler la card par son texte unique (ex. `>BLOCAGES<br>LORRAINE</div>`) pour ne pas toucher une autre card du même média.
- Lancer ensuite `verifier_mastaurige.py` (cf. [[feedback-verifier-fin-session]]). Voir [[web-architecture]] [[mastaurige]].
