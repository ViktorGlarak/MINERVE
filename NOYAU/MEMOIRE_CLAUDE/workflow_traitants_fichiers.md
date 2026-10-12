---
name: workflow-traitants-fichiers
description: "Bascule 2026-06-24 — les traitants éditent MASTAURIGE à la main (fichiers), plus par l'IA ; problème de fusion offline↔réseau à résoudre"
metadata: 
  node_type: memory
  type: project
  originSessionId: 4377e89f-f0dd-40af-851d-ddfb523fd276
---

**Changement de méthode acté le 2026-06-24** (connexion internet de l'utilisateur insuffisante pour corriger en masse via l'IA les demandes de tous les traitants).

**Nouveau flux traitants :** ils modifient **à la main** :
- le **texte des articles/courriers** dans `Sites/<site cible>/<article>.html` ;
- le **texte / likes / retweets** des tweets dans `…\LOCALSTORAGE_WEB_VERSION\moteur\tweets_data.js`.
- ⚠ Consigne donnée aux traitants : **ne pas toucher heure ni date du tweet** (sinon casse le lien avec la card MELMIL).

**Partage :** les traitants ont un **serveur** qui les met sur le **même dossier MASTAURIGE / localStorage** (édition commune). L'utilisateur **récupère ce dossier localstorage** et **écrase** le sien dans `D:\CECPC\PRODUCTION\EXER\AURIGE 7BB\00_Boites à outils\MASTAURIGE`.

**2 problèmes posés (l'utilisateur veut des PROPOSITIONS, pas d'implémentation au 2026-06-24) :**
1. **Simplifier l'édition manuelle** (éviter de casser le JSON `tweets_data.js` / le HTML). Pistes proposées : (A) mini-éditeur `EDITEUR.html` autonome via File System Access API (formulaire texte/likes/RT, n'expose pas date/heure, réécrit le fichier sur disque) ; (B) repères d'édition `<!-- ÉDITABLE -->` + `// ==== code ====` + `VALIDER.bat` (node --check, erreurs en FR).
2. **Fusionner ses modifs OFFLINE avec celles des traitants (réseau)** sans perdre une version. Pistes : (1) prévention = **découper `tweets_data.js` par série/owner** + propriété des séries → 0 collision ; (2) **Git local** (3-way merge, transfert USB `git bundle`, éditeur de fusion VS Code) OU **script « fusion par id »** avec snapshot de référence (réutilise la logique de `EXE_MASTER_VERSION`/MASTER qui fusionne déjà par id) ; (3) tamponner les éditions (traitant+ts).

**⚠ Contrainte navigateurs (2026-06-24) : postes traitants = UNIQUEMENT Microsoft Edge + Firefox (pas de Chrome).** → La **File System Access API** (écriture disque directe, piste A initiale) est **inutilisable** : Firefox ne l'implémente pas ; Edge la supporte mais uniquement en contexte sécurisé (https / http://localhost) — or les traitants sont en `http://<pc>:port` ou `file://` → bloquée même sur Edge. Modèles viables cross-browser : **A′** éditeur → **téléchargement** du fichier corrigé (Blob+`<a download>`, marche partout, friction = remettre le fichier) ; **A″** éditeur → **le serveur écrit** le fichier (POST, le plus robuste car serveur déjà présent, sérialise les écritures, indépendant du navigateur). Garde-fou validateur : préférer une **page web** (Edge/Firefox) qui charge `tweets_data.js` et signale les erreurs de syntaxe, plutôt qu'un `.bat` Node (Node non garanti sur les postes traitants). Les pistes de **fusion** (Git/USB, découpe, fusion-par-id) sont indépendantes du navigateur.

**⚠ Nuance technique clé :** l'édition **fichiers** (tweets_data.js + HTML) est capturée par un copier-coller de dossier. MAIS statuts de card, overrides date/heure et tweets **créés via l'interface** vivent dans le **localStorage / `etat_mastaurige.json`** du serveur, PAS dans les fichiers → si les traitants utilisent l'interface, la récup + fusion doit aussi couvrir `etat_mastaurige.json` (la console MASTER est faite pour ça). Rester « 100 % fichiers » évite ce 2ᵉ canal.

Voir [[mastaurige_serveur_collaboratif]], [[mastaurige_pipeline_injects]], [[recup_injects_guillaume_2bb_7bb]].
