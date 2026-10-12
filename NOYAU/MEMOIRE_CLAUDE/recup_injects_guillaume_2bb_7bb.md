---
name: recup-injects-guillaume-2bb-7bb
description: Méthode + capacité pour rapatrier les injects Guillaume (2BB) vers Minotaure (7BB) — store baked articles + générateur
metadata: 
  node_type: memory
  type: project
  originSessionId: 08c749e1-d2a0-4ea6-ab1e-0268dec9e9b0
---

**Tâche en cours (démarrée 2026-06-19)** : rapatrier les injects éditoriaux de GUILLAUME (AURIGE 2BB) vers MINOTAURE (7BB), par listes successives fournies par l'utilisateur (fichiers `.docx` de mapping `code 2BB → code 7BB + jour`). « il y aura d'autres listes ».

**LO5 = FAIT** (1re liste, `E:\10_PRZ\DIVERS\LO5 - ADAPTATION 2BB 7BB V1.docx`) : 17 codes 07.04.0XYi → **07.10/11/12** ; 11 tweets + 6 articles = **17 cards, 1 par numéro** (pas de doublon). 07.11.I04 = tweet @J_Vasseur SEUL (autorité GUILLAUME l.136 ; le « courrier » 2BB écarté car absent du fichier). Bakés sur disque dans le collab. **9 attachés aux cards socle (07.10.I01-04, 07.11.I01-05) sans les bouger ; 8 en ghost** (07.10.I05/06, 07.11.I06/07, 07.12.I01-04 — pas de card socle JEMM).

**HN = FAIT** (2ᵉ liste, `E:\10_PRZ\DIVERS\HN - ADAPTATION 2BB 7BB V1.docx`) : 20 injects 08.0x → 7BB 08.01/08.02 (+ 2 vers 07.12.I05/06), **fusionnés** avec LO5 (37 cards, 0 doublon). Nouveau **type courrier** géré (site `courrier` + `buildAutoBridge` lit `a.type`). 7 courriers maires/préfet + 6 articles + 7 tweets. Tous GHOST (pas de socle 08.xx). Générateur `_cbtmp\gen_hn_bake.py` (mode FUSION). À valider ANALYSTE_ARN : noms maires + camps courriers.

🛑 **INSTANCE = LE SERVEUR COLLABORATIF** : `D:\CECPC\PRODUCTION\EXER\AURIGE 7BB\00_Boites à outils\MASTAURIGE\SERVEUR_COLLABORATIF\mastaurige` (collab.js + serveur.py). **C'est l'instance de travail quotidienne**, PAS `LOCALSTORAGE_WEB_VERSION` ni l'ancien proto `D:\CECPC\MASTAURIGE\…`. Leçon 2026-06-19 : j'ai baké à tort dans LOCALSTORAGE (annulé/restauré) avant de refaire dans le collab. **Toujours confirmer l'instance + consulter MASTAURIGE & MINAUTORE AVANT d'écrire.** Backups collab : `_cbtmp\backup_collab_*`.

**Capacité créée** : store **baked articles** symétrique aux tweets (avant, seuls les tweets persistaient sur disque). Voir détail dans `MASTAURIGE\MEMOIRE.md` entrée [2026-06-19]. Fichiers 7BB modifiés : `moteur/articles_data.js` (NOUVEAU, `MASTAURIGE_ARTICLES`), `moteur/articles.js` (baseline baked), `MELMIL/melmil.js` (boucle articles dans `buildAutoBridge`), chargement dans `index_master.html` + `MELMIL/melmil_ili.html`. Articles riches = `external:true`, .html **copié-collé adapté** dans `Sites/<dossier>/`.

**Procédé reproductible (listes suivantes)** :
1. Lire la liste (mapping). **Consulter GUILLAUME** (`GUILLAUME\MEMOIRE.md`) — il documente ces injects (cf. [[feedback_impliquer_agents_concernes]]).
2. Extraire le contenu réel depuis le 2BB : `tweets_data.js` (tweets), `melmil_inject_index.js` (type/clé), `.html` des sites (articles), `COURRIERS/` (courriers). ⚠ un code peut avoir **plusieurs cards** (ex. 07.04.07Ci = tweet + courrier).
3. Adapter 2BB→7BB : DAC→ARN, Dacia Romania→Arnland, Bella Channel 1→Bothnia Channel 1, Polish→coalition (casse titre ET MAJUSCULES).
4. Baker : tweets → `MASTAURIGE_TWEETS` (tweets_data.js) ; articles → `MASTAURIGE_ARTICLES` (articles_data.js) + copie .html adaptée dans `Sites/`.
5. Dates : **melmil fait foi** si la card socle existe, sinon jour du fichier.
6. Générateur type : `D:\CECPC\_cbtmp\gen_lo5_bake.py` (à adapter par liste). Backups : `D:\CECPC\_cbtmp\backup_lo5_*`.

**À refiner (utilisateur, « on modifiera au besoin »)** : avatars 2BB nominatifs DAC (`@VoixDACia`, `@TemoignageDAC`) → remapper registre MASTAURIGE ; quelques tournures mécaniques ; camp TV4=bleu à confirmer. **Contrôle utilisateur prévu : le lendemain (≈ 2026-06-20).**

**⚠ Porting vierge** : la capacité « store baked articles » est à porter dans la vierge **en fin de MINAUTORE** (vierge intacte d'ici là) — cf. [[vierge_porting_fin_minautore]].
