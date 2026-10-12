---
name: charte-otan-media
description: "Charte graphique du média fictif \"Site OTAN\" (template reproduisant nato.int) — camp OTAN/bleu"
metadata: 
  node_type: memory
  type: reference
  originSessionId: a68d232b-0e67-4473-8fe3-3260ee347b9f
---

Template **Site OTAN** = média institutionnel fictif reproduisant nato.int, pour les communiqués/déclarations officielles du camp **OTAN/bleu** (ex. Rutte). Créé 2026-06-22.

**Fichier :** `Sites\Site OTAN\OTAN_TEMPLATE.html` — déposé dans 3 instances MASTAURIGE : collab 7BB (`…\AURIGE 7BB\…\SERVEUR_COLLABORATIF\mastaurige\Sites\Site OTAN\`) + 2 vierges (`D:\CECPC\MASTAURIGE\{SERVEUR_COLLABORATIF\mastaurige,LOCALSTORAGE_WEB_VERSION}\Sites\Site OTAN\`).

**Charte :** header blanc + logo NATO/OTAN (base64), nav (À propos · Nos activités · Presse · Multimédia · Travailler avec nous) + Recherche + FRANÇAIS ; **fond hero diagonal bleu pâle** (#eef1fa) ; fil d'Ariane bleu ; **titre sérif navy** (Georgia, #1B2A6B) + sous-titre bold + date + « X MIN DE LECTURE » ; corps justifié (`.BodySubTitle`/`.BodySubTitle2`, listes) ; **rail de partage sticky** (X/FB/in/WhatsApp/Telegram/lien/imprimer, SVG inline) ; **newsletter** (carte blanche sur navy) ; **footer navy** (#16205A) 3 colonnes + logo + réseaux. Couleurs : navy #16205A, titre #1B2A6B, liens #0B4DA2.

**Autonome** : aucun JS/tracking/fonte externe (Georgia+Arial système). Logo source `CREATION\04- OTAN\nato.png` → base64 quantifié 64 couleurs, 207×104, **~3 Ko** (générateur PIL `quantize` ; refaire pareil pour rester léger). Placeholders `__TITRE__/__SOUS_TITRE__/__DATE__/__CHAPO__` + zone contenu commentée.

⚠ **Template SEUL** : pas encore enregistré dans le dict `SITES` de `moteur/articles.js` + `OUTILS/generer_articles.py` → **pas encore bakable** comme article. Câblage (code, dossier « Site OTAN », prefix `OTAN_`, tokens) = étape suivante quand on voudra produire des articles OTAN.

Détail outillage = `MASTAURIGE/MEMOIRE.md` (entrée 2026-06-22 « Site OTAN »). Suivi exercice = `MINAUTORE/MEMOIRE.md`. Voir [[methode_web_exercices]], [[charte_tv4_media]] (autre camp).
