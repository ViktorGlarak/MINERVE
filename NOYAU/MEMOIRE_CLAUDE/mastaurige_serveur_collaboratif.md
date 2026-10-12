---
name: mastaurige-serveur-collaboratif
description: "Piste MASTAURIGE commun temps réel (serveur Python/SSE) — prototype 2026-06-16, à valider par test 2 machines"
metadata: 
  node_type: memory
  type: project
  originSessionId: 08c749e1-d2a0-4ea6-ab1e-0268dec9e9b0
---

Piste lancée le **2026-06-16** : un **MASTAURIGE commun** hébergé sur un PC du réseau, **co-édité en temps réel** par 6-15 traitants, au lieu que chacun ouvre le sien (état isolé en `localStorage`).

**Verrou identifié :** MASTAURIGE est 100 % statique, tout l'état vit dans le `localStorage` du navigateur (isolé par machine) → un simple partage de dossier ne partage RIEN. Il faut un **serveur** qui détient l'état au centre et le pousse aux clients.

**Modèle retenu :** un PC « ouvert » du réseau (typiquement le PC Admin) fait tourner le serveur ; les traitants ouvrent leur navigateur dessus. Stack = **Python bibliothèque standard uniquement** (zéro pip) : `http.server` + **SSE** (push temps réel) + POST (écritures) + `etat.json` central. Choix SSE car natif navigateur sans dépendance.

**Accès sans IP :** le serveur génère un raccourci `OUVRIR_MASTAURIGE.url` (pointant sur le **nom** du PC, pas l'IP → stable malgré DHCP) à copier dans le dossier partagé ; les traitants double-cliquent. N'importe quel PC peut être serveur s'il peut (1) lancer le programme, (2) ouvrir le port 8765 au pare-feu, (3) rester allumé. Les PC traitants verrouillés ne conviennent pas.

**⚠ EMPLACEMENT CANONIQUE (depuis 2026-06-18) = `D:\CECPC\PRODUCTION\EXER\AURIGE 7BB\00_Boites à outils\MASTAURIGE\SERVEUR_COLLABORATIF\`** (dans l'exercice 7BB). On y fait TOUTES les mises à jour MINAUTORE. **Déploiement** : l'utilisateur copie le sous-dossier `mastaurige\` sur le PC Admin (remplace l'ancien) → traitants rafraîchissent. Le serveur lit les fichiers à chaud (aucun cache serveur) → éditer un `.html`/trombino = servi immédiatement (refresh navigateur ; le SSE ne pousse que l'état collaboratif). **La VIERGE reste vierge** (mises à jour vierge à la FIN de MINAUTORE). L'ancien `D:\CECPC\MASTAURIGE\SERVEUR_COLLABORATIF\` est **superseded**. `mastaurige\` y a été reconstruit à neuf depuis l'instance 7BB (Arnland/Bothnia/Starter Package) + couche collab (collab.js, _collab_admin.html, tags). Serveur fonctionnel (4 postes : 3 traitants + BASE).

**Livrable initial = PROTOTYPE** dans `D:\CECPC\MASTAURIGE\SERVEUR_COLLABORATIF\` (serveur.py + client_test.html + LANCER_SERVEUR.bat + README.md + etat.json + **`python\`** Python portable). Ne contient PAS encore MASTAURIGE — il sert à prouver le réseau d'abord.

**2026-06-17 — PC Admin sans Python :** 1er essai terrain (PC Admin du réseau traitants, via USB) → `.bat` échouait « Python absent ». Réglé en embarquant un **Python embeddable** (`python\`, ~11 Mo, stdlib complet, aucune install) ; `LANCER_SERVEUR.bat` l'utilise en priorité. ⚠ Non testable sur le poste dev (sa politique bloque les `.exe` non approuvés → « Accès refusé » même après Unblock-File ; un .exe PyInstaller serait bloqué pareil). **Plan B si le PC Admin bloque aussi le python.exe** : IT installe/autorise Python, ou héberger sur un autre poste avec Python approuvé (le raccourci `.url` se régénère au nom de l'hôte).

**Why:** demande utilisateur pour fluidifier le travail multi-traitants ; c'est la bonne évolution mais elle dépend d'un prérequis réseau non garanti (PC verrouillés).

**⚠ 2026-06-24 — SERVEUR HS, repli vers la version LOCALSTORAGE.** Les PC traitants ne peuvent plus faire tourner le serveur. Sur demande user, **100 % du contenu à jour du collab MINOTAURE a été rapatrié dans `…AURIGE 7BB\…\MASTAURIGE\LOCALSTORAGE_WEB_VERSION`** (ancien périmé → `.bak`) **sans modifier le collab** : copie intégrale du dossier `SERVEUR_COLLABORATIF\mastaurige\` + `collab.js` remplacé par un **SEED LOCAL autonome** qui injecte une fois (par navigateur, gardé `mast-seed-version`) les **92 clés** de `etat_mastaurige.json` (snapshot 2026-06-23 21:39) après purge des clés périmées (0 conflit), puis laisse l'app en localStorage pur. `_collab_admin.html` retiré. Détail canonique : `MASTAURIGE\MEMOIRE.md` § « SERVEUR COLLAB HS → repli ». Le serveur reste reportable si l'IT débloque un port/python.

**How to apply:** ⚠ **POINT BLOQUANT à valider AVANT le portage** = les navigateurs des PC verrouillés peuvent-ils joindre un port TCP du PC serveur (pas juste SMB) ? Test = double-clic du raccourci depuis un PC traitant ; si le compteur/note se synchronise entre 2 machines → temps réel validé, on porte tout MASTAURIGE (schéma SQLite par card, remplacer localStorage par appels serveur + `/flux`, conflits même-card, présence). Sinon → repli synchro par fichier (non temps réel). Détail technique exhaustif : `MASTAURIGE\MEMOIRE.md` § « MASTAURIGE COLLABORATIF ». Voir [[mastaurige]], [[project_mercure]].
