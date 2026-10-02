# AVIS DESIGNER n°32 — MELMIL, comptes rendus : télécharger le bon exemplaire + garder « Importer »

**Date** : 2026-10-02
**Écran** : `app-melmil` · `src/components/atelier/compte-rendu.tsx` — tableau des CR d'un incident (ligne = ETIM, colonne = type de CR) et fiche ouverte d'un CR.
**Demande utilisateur** : (1) « Télécharger .docx » dans la fiche d'un exemplaire ouvert télécharge le mauvais (le lot / n°1) ; (2) garder « Importer » même après le 1er CR.
**Posture** : DESIGNER contribue, ne tranche pas. Recommandations sourcées sur la doctrine `DESIGNER\MEMOIRE.md` §3.

---

## Constat (lu dans le code)

- **Bug de téléchargement** : la fiche appelle `onTelecharger={() => setANommer(... crsPartages(...) ...)}` (ligne 323) qui renvoie **tous** les exemplaires → on télécharge le lot, pas l'exemplaire ouvert. L'écran affiche « n°2 » mais l'action porte sur autre chose : **l'action ne porte pas sur ce qui est montré** (Nielsen 1 « visibilité de l'état », REF-14 ; Nielsen 2 « correspondance système/monde réel »).
- **« Importer » disparaît** dès qu'un CR existe (il n'est que dans la branche « aucun CR », lignes 255-266). On ne peut plus reprendre un exemplaire supplémentaire rempli dans Word, alors que « +1 » (vide) reste, lui. **Incohérence de parcours** : la même capacité (ajouter un exemplaire) existe vide mais pas depuis un fichier.

---

## Recommandations

### R1 — La fiche télécharge l'exemplaire OUVERT (correctif de fond)
Dans `ComptesRendusIncident`, faire porter `onTelecharger` sur **le CR courant seul** : `onTelecharger={() => setANommer([courant])}`. Un geste agit sur l'objet affiché, jamais sur un ensemble que l'utilisateur n'a pas désigné (Nielsen 1 & 2, REF-14 ; « tolérant en entrée, strict en sortie » REF-06).
Le **lot** reste accessible **depuis le tableau** par `.docx (n)` — deux portées, deux points d'entrée distincts (voir R3).
*Effort : faible (une ligne).*

### R2 — Nommer l'exemplaire partout où on le consulte / télécharge
Rendre visible **quel** exemplaire on tient, du tableau jusqu'au dialogue de nommage (Nielsen 1 « visibilité de l'état » REF-14 ; « l'étiquette est un dernier recours mais la donnée doit se nommer » REF-07) :
- **Fiche (en-tête, ligne 376)** : afficher le rang quand l'exemplaire fait partie d'un lot → **« CIMICREP n°2 / 3 »** (calculer le rang via `crsPartages(...).findIndex(c => c.id === cr.id)` ; n'afficher « n°k / N » que si `N > 1`, sinon le nom seul comme aujourd'hui).
- **Bouton de la fiche** : garder le libellé **« Télécharger .docx »**, et lui ajouter `title`/`aria-label` **« Télécharger cet exemplaire (CIMICREP n°2) »** — distingue sans ambiguïté « cet exemplaire » de « tout le lot » **par le mot, pas par la couleur** (règle 10 « jamais l'info par la couleur seule », REF-07 ; REF-13).
- **Dialogue de nommage (`DialogueExportCr`, titre ligne 91)** : quand on vient d'un exemplaire unique ouvert, titrer **« Télécharger le CIMICREP n°2 »** (et non le nom nu) ; le cas lot garde son titre actuel « Télécharger les 3 CIMICREP … (un par page, un seul fichier) ». Passer le rang au dialogue (nouveau prop optionnel `rang`/`sur`).
*Effort : faible à moyen.*

### R3 — Deux portées, deux chemins — ne pas doubler les boutons du tableau
L'utilisateur demande s'il faut un bouton de téléchargement **par exemplaire** dans le tableau, à côté de « n°1 », « n°2 ». **Recommandation : non.** Doubler chaque « n°k » d'une icône ⬇ alourdit une cellule déjà dense (contrainte explicite ; Hick « moins de choix quand le temps presse », REF-06 ; « limiter les choix » REF-07). On garde **un seul modèle mental** :
- **« n°1 », « n°2 »** = *ouvrir* l'exemplaire (puis le télécharger depuis la fiche, qui porte sur l'ouvert — R1). 2 clics, cohérent avec le cas à un seul exemplaire (« Ouvrir » puis télécharger).
- **« .docx (n) »** = *tout le lot* dans un seul fichier. C'est la **seule** action « lot » de la cellule, ce qui lève l'ambiguïté.

Clarifier le bouton lot (sans le renommer lourdement) : garder **« .docx (3) »**, et lui donner un `aria-label` **« Télécharger les 3 CIMICREP de ETIM-7 (un par page, un seul fichier) »** (le `title` existe déjà ligne 246 — le doubler en `aria-label` pour le lecteur d'écran, REF-13, REF-16). Le « (n) » est la marque visuelle du lot ; l'absence de « (n) » = un seul fichier logique.
*Effort : faible.*

### R4 — Garder « Importer » après le 1er CR, à côté de « +1 »
Ajouter, dans la **branche « il existe au moins un CR »** (après `+1`, lignes 237-245), le même contrôle d'import que la branche vide (lignes 255-266), en réutilisant le `<label>` + `<input type=file hidden>` déjà écrit. Placement : **après « +1 »**, avant ou après « .docx (n) » — groupé avec les actions « ajouter », pas avec « télécharger » (proximité, règle 9, REF-07).
*Effort : faible (déplacer/dupliquer le `<label>` existant).*

### R5 — Distinguer « +1 » (vide) de « Importer » (depuis un fichier), par le libellé
Les deux ajoutent un exemplaire ; seule la **source** diffère. Ne pas les confondre (Nielsen 2, REF-14) :
- **« +1 »** reste tel quel = *ajouter un exemplaire vide* (garder son `aria-label` « Ajouter un autre CIMICREP pour ETIM-7 », ligne 242).
- Le bouton d'import prend le libellé **« Importer… »** (avec les points de suspension) = *ajouter un exemplaire depuis un fichier Word*. Les « … » sont la convention établie d'« ouvre un choix / demande un fichier » (Jakob « faire comme ailleurs », REF-06). `aria-label` **« Importer un autre CIMICREP rempli dans Word pour ETIM-7 »**.
- **Cohérence avec l'état « aucun CR »** : y renommer aussi l'actuel « Importer » en **« Importer… »** (lignes 255-256) pour que le même geste porte le même mot partout. Garder « + Créer » (vide, premier) ↔ « Importer… » (fichier) dans l'état vide, et « +1 » (vide) ↔ « Importer… » (fichier) dès qu'un CR existe : même paire logique, libellés alignés.
- Conserver l'état transitoire **« Import… »** pendant le chargement (le `import_` ligne 256) — à reporter aussi sur le nouveau bouton de la branche pleine (Nielsen 1, « l'état du système toujours visible », règle 25).
*Effort : faible.*

### R6 — Accessibilité et cibles
- Tous les boutons `.frappe-mini` : vérifier **≥ 24 × 24 px** (WCAG 2.5.8 AA, règle 12, REF-13). Les « n°1 » / « +1 » sont courts : garantir un `min-height`/`min-width` et un `padding` suffisants.
- Chaque « n°k » doit annoncer l'exemplaire **et son contexte** : `aria-label` **« Ouvrir le CIMICREP n°2 pour ETIM-7 »** (le `title` existe déjà ligne 232 sans l'ETIM ; ajouter l'ETIM et le doubler en `aria-label`).
- L'`<input type=file>` d'import doit rester associé à son libellé (déjà via `<label>`), et le `<label>` recevoir un `aria-label` explicite (R5), le texte visible étant seulement « Importer… ».
*Effort : faible.*

---

## Synthèse de la doctrine ajoutée
- **Un geste agit sur l'objet affiché** : si l'écran dit « n°2 », « Télécharger » télécharge n°2, pas le lot (Nielsen 1 & 2).
- **La portée se dit par le mot, pas par la couleur** : « cet exemplaire (n°2) » vs « les 3 … (un par page) » ; « (n) » = lot.
- **Ne pas multiplier les actions dans une cellule dense** : une porte pour ouvrir (puis télécharger l'ouvert), une porte pour le lot.
- **Même capacité = même mot partout** : « Importer… » (points de suspension = ouvre un fichier), présent dans l'état vide **et** après le 1er CR, distinct de « +1 » (vide).
