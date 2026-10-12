---
name: mastaurige-outils-optim
description: "Outils d'optimisation MASTAURIGE livrés le 2026-05-31 : contrôleur lint, export 1-clic, MELMIL sans Excel, sauvegarde rangement, ménage."
metadata: 
  node_type: memory
  type: project
  originSessionId: 410ff7ab-cce4-44f7-9471-211855cef197
---

5 optimisations livrées le **2026-05-31** dans `EXER\AURIGE 2BB\00_Boites à outils\MASTAURIGE\WEB\` (hors dépôt git IA\MINERVE). Documentées en détail dans `MASTAURIGE\MEMOIRE.md` § « OUTILS D'OPTIMISATION ».

1. **Contrôleur lint (lecture seule)** : `WEB\OUTILS\verifier_mastaurige.py` + `VERIFIER.bat`. Vérifie la règle des 4 éléments (card+ANIM_DATA+LO_BY_KEY+melmil_inject_index), data-camp, back-btn.js, MASTAURIGE_INDEX non cassé. À lancer avant chaque export.
2. **Export 1-clic** : `WEB\PS1\CREER_ZIP_AUTO.ps1` + `.bat` — récupère seul index_media/rzo/complet.html depuis Téléchargements ou WEB et zippe. Anciens CREER_*_ZIP.ps1 = secours.
3. **MELMIL sans Excel** : `WEB\MELMIL\generate_data.py` (MELMIL.xls = XML Tableur 2003, lu en Python stdlib). `Actualiser_MELMIL.bat` essaie Python puis bascule sur le PS1 Excel. Sortie validée identique (47/47 injects). ⚠ Source = logiciel **GESTIM** ; futurs exercices = autres logiciels/formats → `generate_data.py` à faire évoluer en lecteur adaptatif par type de fichier (même sortie melmil_data.js).
4. **Sauvegarde rangement** : boutons 💾 Sauvegarder / 📂 Charger dans la **barre d'outils de MELMIL_ILI_GUILLAUME.html** (déplacés depuis index_master le 2026-05-31, car MELMIL = surface de planif visuelle). Export/import localStorage card-*/melmil-* en JSON ; fonctions inline + styles `.btn-save` dans melmil.css. localStorage partagé MELMIL↔index_master.
5. **Ménage** : résidus P-xx/R-x → `WEB\MELMIL\_archive\`.

✅ Oubli réel détecté par le lint et **corrigé le 2026-05-31** : tweet `@EastWatch_contraoff_blanchiment` → ajout LO 1 (blanchiment Storm-1516). Lint repasse à « TOUT EST BON » (120 ANIM_DATA = 120 LO_BY_KEY).

**Gabarit vierge (2026-05-31)** : `D:\CECPC\PRODUCTION\CREATION\08 - MASTAURIGE VIERGE` = outil MASTAURIGE vide + squelette génériqué (J+1…J+10, Acteur 1…7). Généré par `WEB\OUTILS\creer_gabarit_vierge.py` (réexécutable). Mode d'emploi `LISEZ-MOI_GABARIT.md`. ⚠ strip MELMIL.xls en TEXTE (pas ElementTree). Nouvel exercice = copier dossier + déposer export GESTIM + Actualiser_MELMIL.bat + reparamétrer 3 fichiers (libellés MELMIL html, ROW_MAP/CLASS_MAP/DAY_MAP dans melmil.js, DAY_OPTIONS index_master).

**Versioning (2026-05-31)** : convention `vX.Y`, **on démarre à v0.1** — ⚠ la **v1.0 = quand l'utilisateur juge l'outil abouti** (ne pas l'attribuer soi-même). Vierge + AURIGE 2BB = v0.1. Fichiers : `MASTAURIGE_VERSION.txt` (autoritaire, racine de chaque instance), `CHANGELOG.md` (racine vierge = maître), version affichée pied index_master + barre MELMIL. Bump = 3 endroits (CHANGELOG + VERSION.txt + affichage). Outil `OUTILS\COMPARER.bat` (comparer_au_gabarit.py, lecture seule) : compare machinerie exercice vs vierge (hash fichiers purs + moteur melmil.js sans ROW/CLASS/DAY_MAP), dit quoi reporter. Vierge = référence (dernier numéro), exercices figés à leur version. Modèle = exercice évolue → reporter au vierge + bump.

**Idée 6 reportée après AURIGE 2BB** : externaliser ANIM_DATA + LO_BY_KEY hors du monolithe index_master.html (447 Ko) vers injects_data.js. Voir [[mastaurige]].
