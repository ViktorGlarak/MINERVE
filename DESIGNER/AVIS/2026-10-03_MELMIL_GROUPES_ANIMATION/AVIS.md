# Avis DESIGNER n°40 — MELMIL : deux groupes d'animation (GA1, GA2) et la source de chaque event

> **Date** : 2026-10-03 · **App** : `app-melmil` (atelier de préparation) · **Demandé par** : NOYAU, sur 7 décisions de l'utilisateur
> **Statut** : 🟡 proposé, à appliquer par PLEIADE / ARCHITECTE. DESIGNER contribue, il ne tranche pas.
> **Code lu (lecture seule)** : `ecran-atelier.tsx`, `onglets-gt.tsx` (OngletEvents/CarteEvent, OngletStorylines, OngletIncidents, FicheIncident), `lecture.tsx`, `statut.tsx`, `planche.tsx`, `carte.tsx`, `planche-jemm.tsx`, `onglets-suivi.tsx` (Réglages), `aligner-jemm.tsx`, `lib/atelier/aligner.ts`, `lib/ui/style-planche.tsx`. J'ai aussi regardé **le travail en cours, non commité**, pour m'y aligner : `lib/atelier/groupes.ts` (`GROUPES_ANIMATION`, `prochainCodeMelmil`, `codeMelmilInvalide`, `modificationsHorsPerimetre`, `idsDuGroupe`), `EventAtelier.ga` / `.source` (migration : GA1, source déduite du code), `alignerPerimetre`, `verserJemm(…, { ga })`, `habilitation.ts` (`ROLES_GA`, `gasDe`).

## Ce que le code m'apprend avant de conseiller

1. ⚠ **La planche JEMM n'a pas de filtre d'events aujourd'hui.** Elle propose seulement **« Affichage : Liste | Clair | Classique »** (`ChoixStylePlanche`, un segment `.selecteur-style` en `aria-pressed`, **mémorisé par poste** sous `melmil.style-planche`). « Comme sur la planche JEMM » se traduit donc par : **même forme de contrôle, même place (au-dessus de la planche, à droite), même mémoire par poste**. Il n'y a pas de filtre existant à copier.
2. ⚠ **« Aligner sur JEMM » (Réglages) supprime aujourd'hui tout event absent des exports choisis** (`alignerSurJemm` → « Events SUPPRIMÉS »). Avec des events « Créés dans MELMIL » et des events du GA2, ce geste détruirait le travail des autres. `alignerPerimetre` (en cours) corrige le fond ; l'écran doit suivre (R10).
3. Le **mode lecture n°35 est déjà un contexte React** (`LectureContexte`, `useLecture`, `SiModifiable`, `ValeurLue`), lu par les champs, le stepper, les cartes de la planche (`draggable={!lecture}`). **Il suffit de l'imbriquer par élément** : c'est la pièce maîtresse de cet avis (R4).
4. Deux mots voisins existent déjà et prêtent à confusion : les **GT** (GT1 → GT3, les *étapes* du parcours dans l'en-tête) et le **« Confié à »** des events (des *groupes de l'Équipe*, avis Confié du 28/09). Un « GA1 » posé à côté de « GT1 · en cours » se lira mal si on n'y prend pas garde (R1, R13).

**Principe directeur** : chaque animateur **travaille dans son GA et voit le reste comme un document**. Ce qui est à lui se modifie comme aujourd'hui ; ce qui est à l'autre GA se **lit** (mode n°35, élément par élément) avec une seule action possible : **demander un produit**. On garde les mêmes écrans, les mêmes places, le même ordre.

---

## R1 — L'en-tête : dire une fois, au même endroit, dans quel GA on est

- **Une pastille juste après le titre de l'exercice**, à la place même de la pastille « Lecture et demandes » (n°35, R1). Deux rôles, une seule place pour « mon mode » : on le cherche toujours au même endroit (Jakob, REF-06).
  - Animateur : icône Lucide `Users` + **« Groupe d'animation GA1 »**, ramené à **« GA1 »** sous 900 px. Style **plein** (`--accent` / `--sur-accent`, comme le segment actif de `.selecteur-style`) : c'est *mon* groupe.
  - Admin : **« Admin · tous les groupes »**, style contour neutre.
  - Lecture et demandes : la pastille du n°35, inchangée.
  - Personne qui porte GA1 **et** GA2 : **« GA1 + GA2 »**.
  - Personne qui n'a **aucun** GA ni Admin ni Lecture (bouclier mal coché) : pastille contour **« Aucun groupe d'animation »** + tout l'atelier en lecture (n°35) ; bulle : « Demandez à l'Admin de vous cocher GA1 ou GA2 sur le bouclier. » Un état inconnu doit se voir, pas se deviner (Nielsen 1, REF-14).
- C'est un `details` comme `PastilleLecture` (même composant à généraliser : `PastilleMode`). Bulle au clic :
  > **Vous êtes dans le GA1.** Vous créez et modifiez les events du GA1 et tout ce qui en dépend (storylines, incidents, statuts, comptes rendus, fichiers). Les events du GA2 se lisent ; vous pouvez y demander un produit. Pour modifier un event du GA2, adressez-vous au GA2.
- ⚠ **Ne pas l'écrire « GA1 » nu au milieu du parcours GT** : le mot complet « Groupe d'animation » sur ordinateur, une icône de personnes, un style plein (les étapes GT sont des contours) et un `title`/`aria-label` « Votre groupe d'animation : GA1 ». Trois indices de forme, pas seulement un mot (doctrine n°10).

## R2 — « Mon GA / Tous » : un seul choix, pour tout l'atelier, mémorisé par poste

- **Forme** : un **segment de 2 options** dans la forme de `.selecteur-style` (déjà appris sur la planche) :
  **`Afficher :  [ GA1 seul ]  [ Tous les groupes ]`** — on écrit **le nom du GA** et non « Mon GA » (le mot dit exactement ce qu'on verra).
  - Admin (pas de GA) : **`[ Tous ] [ GA1 ] [ GA2 ]`** ; avec un GA3, une option de plus, rien d'autre à changer.
  - Personne GA1 + GA2 : `[ GA1 + GA2 ] [ Tous ]` (équivaut à « Tous » tant qu'il n'y a que 2 GA : dans ce cas, **ne pas afficher le segment**).
  - Sémantique : `role="radiogroup"` + `aria-checked` (choix exclusif ; c'est mieux que les `aria-pressed` de `ChoixStylePlanche`, à aligner au passage), flèches gauche/droite.
  - ⛔ Pas une case « Afficher l'autre GA » : avec un GA3, une case ne dit plus lequel. ⛔ Pas de puces multi-sélection par GA : une possibilité de plus à comprendre pour un besoin qu'on n'a pas (Hick, REF-06).
- **Où** : **une fois, sous la barre d'onglets**, à droite, sur la même ligne que la zone d'alerte, **visible dans tous les onglets qu'il concerne** : Events, Storylines, Incidents, Synthèse, Planche de préparation, Écarts. Il **n'apparaît pas** dans Demandes (on demande sur tout incident, et la Prod travaille pour tout le monde), Équipe, Journal ni Réglages.
  - **Pourquoi un seul choix** : un choix par onglet crée l'état « où sont passés mes events ? » à chaque changement d'onglet (Nielsen 4 et 6, REF-14). Un seul réglage = un seul modèle mental. Les liens de la Synthèse (`?onglet=gt3&manque=…`) n'ont rien à porter : le périmètre suit.
- **Mémoire** : par poste, `localStorage` `melmil.portee-ga` (comme `melmil.style-planche` : un confort de lecture, pas une donnée de l'exercice), lu après le premier rendu, enveloppé de try/catch.
- **Par défaut, au premier passage** : **« Tous les groupes »** (*à confirmer*, Question 1). Rien n'est caché sans qu'on l'ait choisi ; les éléments de l'autre GA sont de toute façon marqués (R3) et non modifiables, donc la concentration est préservée.
- **Ce qui se voit quand on cache** : jamais rien. Une ligne `.bandeau-filtre` (`role="status"`), en tête de l'onglet :
  > **GA2 masqué** : 3 events, 9 storylines, 41 incidents. · **Afficher tous les groupes**
  Le lien rebascule le segment. Sur la planche, la même ligne au-dessus du tableau. Si l'autre GA n'a encore rien : pas de ligne.
- **Compteurs d'onglets** (`groupe-compte`) : ils comptent **ce qui est affiché** ; `title` : « 4 events affichés sur 7 (GA2 masqué) ». Un nombre qui ne correspond pas à la liste ouverte fait douter de la liste.

## R3 — Marquer ce qui appartient à l'autre GA : un mot, une forme, pas une couleur

- **Une pastille propriétaire, sur les éléments qui portent un titre** :
  - le mien : **« GA1 »** en pastille pleine discrète (ou rien : voir plus bas) ;
  - l'autre : **« GA2 · lecture »** avec l'icône `Eye` (même dessin que la pastille n°35, en petit : `.pastille-ga` dérivée de `.pastille-lecture summary`, 0.6875rem, contour `--trait-fort`).
  - Pour alléger, *proposition* : quand l'affichage est « GA1 seul », **aucune pastille** (tout est à moi). En « Tous », la pastille propriétaire apparaît **sur tous les events** (GA1 comme GA2) : comparer, c'est voir les deux.
- **Où elle se pose** (un seul niveau de rappel par écran, pas sur chaque ligne) :
  | Écran | Emplacement |
  |---|---|
  | Events (GT1) | en-tête de la `CarteEvent`, à côté du code |
  | Storylines (GT2) | dans le `summary` du groupe d'event (`groupe-tete`), après le nom de l'event |
  | Incidents (GT3) | dans l'`intertitre-event` (avant `intertitre-compte`) ; **pas** sur chaque ligne du tableau |
  | Fiche d'incident | en-tête, sous le code (R4) |
  | Planche de préparation | dans l'étiquette de rangée (`rangee-label`, sous le nom de l'event, à la place de `sous` ou à côté) |
  | Liste par jour (`PlancheListe`) | à côté du code d'event de chaque intertitre |
- ⛔ **Pas de couleur par GA** : la couleur porte déjà la storyline (cartes), le statut (orange/jaune/vert), l'espace (« Préparation » ambre) et l'alerte (rouge rare, doctrine n°20). Une cinquième signification par la couleur se lirait mal, et la couleur seule ne suffit jamais (WCAG 1.4.1, doctrine n°10).
- **Sur la planche** : les cartes de l'autre GA restent **lisibles** (texte au contraste normal : ⛔ pas d'`opacity` sur la carte, qui ferait tomber le texte sous 4,5 : 1 — WCAG 1.4.3, REF-13). On les distingue par la **forme** :
  - **bordure en pointillé** de la carte (`.carte-sl[data-lecture] { border-style: dashed; }`) ;
  - en-tête et incidents **non déplaçables** (`draggable={false}`, curseur `pointer`, infobulle sans « Glissez l'en-tête… ») : c'est déjà ce que fait `Carte` quand `useLecture()` vaut `true` ;
  - l'étiquette de rangée porte « GA2 · lecture » sur fond `--fond-creux`.
  - Clic : la fiche s'ouvre à droite, **en lecture** (R4).
  - L'ordre des rangées **ne change pas** (code croissant), même en « Tous » : regrouper par GA casserait la position apprise des events (avis n°25, R3 ; Jakob).

## R4 — Le mode lecture n°35, appliqué élément par élément

- **Mécanique (le plus simple)** : imbriquer `LectureContexte.Provider value={lecture || !modifiable(ev)}` autour de **chaque** `CarteEvent`, de **chaque** groupe d'event des Storylines, de **chaque** intertitre d'event des Incidents (avec ses tableaux et son bouton « + Nouvel incident »), de la `FicheIncident` et, sur la planche, des cartes de chaque rangée. **Tout le n°35 suit sans une ligne de plus** : champs en texte (`ValeurLue`, « Non renseigné »), boutons masqués (`SiModifiable`), stepper en `<ol aria-current="step">`, pas de glisser, comptes rendus « lire / télécharger », vignettes avec « Télécharger » seulement, « Marquer dans JEMM » absent.
  - `modifiable(ev)` = `admin || mesGa.includes(ev.ga)`, à mettre dans `groupes.ts` à côté de `modificationsHorsPerimetre` (même règle partout).
  - Pour `Planche` (composant partagé avec la planche JEMM) : un drapeau `lectureSeule` sur la `Rangee` (ou une fonction `rangeeModifiable(code)` passée en prop) ; la planche JEMM ne la passe pas.
- **La fiche d'incident d'un autre GA** = la fiche « Lecture et demandes » du n°35, avec :
  - en tête, sous le code : la pastille **« GA2 · lecture »**, et sa bulle : « Cet incident appartient au GA2 : vous le lisez. Vous pouvez demander un produit. Pour le modifier, adressez-vous au GA2. » ;
  - **« Demander un produit » en action principale** dans l'en-tête (`frappe-pleine`, à gauche de « Fermer ») — la condition actuelle `{lecture && …}` le fait déjà dès que le contexte imbriqué vaut `true` ;
  - la rubrique « Médias et demandes de produit » : vignettes en téléchargement, liste des demandes, bouton « Demande de produit complexe » gardé.
  - ⚠ Le formulaire de demande ne doit **pas** être en lecture : c'est la raison pour laquelle `LectureContexte` est séparé de `QuiContexte` (écart du n°35) ; vérifier que `FicheDemande` n'hérite pas du contexte imbriqué (la poser hors du Provider, ou forcer `value={false}` autour).
- **Pourquoi** : la restriction est **permanente et liée à l'élément** ; un champ désactivé est illisible par construction (contraste exempté, WCAG 1.4.3), un bouton désactivé répété est du bruit (Nielsen 8) ; l'état « lecture seule » de Carbon (REF-12) est fait pour ce cas.

## R5 — Créer un event (GT1) : la source se choisit d'abord

« + Nouvel event » ne crée plus un event vide d'un clic : il **ouvre un petit formulaire en place** (une `carte-ui` en tête de la grille, focus sur le segment ; ou une fenêtre si l'on préfère, avec piège du focus et retour au bouton — doctrine n°11).

1. **Segment `role="radiogroup"`** : **`[ Créé dans MELMIL ]  [ Depuis un export JEMM ]`**, « Créé dans MELMIL » coché par défaut (c'est le seul chemin qui n'exige pas de fichier). Sous chaque option, une phrase qui dit la conséquence (Tesler : le système porte la règle, REF-06) :
   - MELMIL : « Vous le construisez ici. Aucun import JEMM ne le touchera. Ses incidents s'arrêtent au statut « Validé ». »
   - JEMM : « Un export JEMM = un event. Il se met à jour plus tard avec « Mettre à jour depuis JEMM », sans toucher aux autres events. »
2. **Créé dans MELMIL** :
   - **Code** : champ `chiffre`, **pré-rempli** par `prochainCodeMelmil` (20, 21…), modifiable. Aide sous le champ : « 01 à 19 : réservés aux events de JEMM. »
   - **Avertissement (non bloquant)** si le code existe dans la **planche JEMM** (`codesJemm` / `jemm.evenements`) : « ⚠ La planche JEMM a déjà un event 21 (« ILI-B »). Choisissez un autre code pour ne pas les confondre. » Ton d'avertissement (`--texte`, icône ⚠), pas rouge : rien n'est encore faux.
   - **Erreur (bloquante)** si `codeMelmilInvalide` renvoie un texte (format, < 20, déjà dans l'atelier) : message GOV.UK sous le champ, relié par `aria-describedby`, bouton principal grisé tant que c'est faux. ⚠ Le code en cours **bloque** les codes < 20 alors que la décision dit « codes libres » : à trancher (Question 2) ; mon conseil : **garder le blocage** (un event MELMIL en 07 entrerait en collision avec un futur export JEMM, refusé ou confondu).
   - **Nom** (obligatoire) et c'est tout ; la description se remplit ensuite sur la carte.
3. **Depuis un export JEMM** :
   - un bouton **« Choisir l'export JEMM… »** (un seul fichier : *un export = un event*) ;
   - **aperçu avant création** : « Event **07 « ILI »** · 6 storylines · 41 incidents · D+27 → D+35 » ; calendrier non posé → le dire et renvoyer à l'Admin (comme aujourd'hui) ;
   - **refus** sur place si le code est déjà pris (R11).
4. **Propriétaire**, sous le reste :
   - animateur d'un seul GA : en texte, **« Propriétaire : GA1 (votre groupe) »**, pas de choix ;
   - animateur GA1 + GA2 : deux puces, **aucune pré-cochée**… ou la première ? *(Question 4 ; défaut : aucune, choix obligatoire)* ;
   - Admin : **deux puces GA1 / GA2, aucune pré-cochée**, choix obligatoire (« Choisissez le groupe qui portera cet event. »). Un propriétaire choisi par défaut pour l'Admin finirait par tout mettre au GA1 sans que personne l'ait voulu.
5. **Bouton principal parlant** (doctrine n°6) : **« Créer l'event 21 »** / **« Créer l'event 07 depuis JEMM »** ; « Annuler » à côté. Après création : la nouvelle carte reçoit le focus et une bordure d'accent 2 s (fin de parcours nette, Peak-End).

## R6 — La carte d'un event : propriétaire, source, mise à jour

- **En-tête de `CarteEvent`** : `[code] [nom] … [GA1] [⟳ JEMM]` ou `[GA1] [MELMIL]`.
  - Pastille source : **« Synchronisé avec JEMM »** en long (≥ 1024 px), **« JEMM »** en court ; **« Créé dans MELMIL »** / **« MELMIL »**. Contour neutre, mot toujours écrit ; l'icône `RefreshCw` (ou « ⟳ ») pour JEMM, `PenLine` pour MELMIL. Pas de vert pour JEMM : le vert est le statut « Validé / Dans JEMM ».
  - La source **ne se change pas** une fois l'event créé (Question 6).
- **« Mettre à jour depuis JEMM… »** (events JEMM seulement, et seulement si je peux modifier l'event) :
  - **où** : au pied de la carte, à gauche de « Supprimer », bouton `frappe` (secondaire : ce n'est pas l'action de tous les jours). Les points de suspension disent qu'un choix de fichier suit (doctrine n°32).
  - **au-dessus**, une ligne d'état permanente : « Dernière mise à jour depuis JEMM : 02/10 à 14:30 par Cne X (export 01.10.26) » — ou « Jamais mis à jour depuis sa création ». C'est la réponse à « suis-je à jour ? » (Nielsen 1). Champ à ajouter : `jemmMaj: { le, par, fichier }`.
  - **parcours** : choix du fichier (ou du dossier, comme l'alignement, pour les pièces jointes) → **fenêtre « Mettre à jour l'event 07 depuis JEMM »** qui montre le **bilan de CET event** (on réutilise `Bilan` d'`aligner-jemm.tsx`, alimenté par `alignerPerimetre([ev.id])`) : renumérotés, mis à jour, créés, **supprimés dans cet event**, gardés car porteurs de pièces jointes, jours ou heures qui changent, appariements douteux en tête. Une phrase fixe en haut du bilan : **« Les autres events ne sont pas touchés. »** Options existantes gardées (« Garder le jour et l'heure de MELMIL », « Supprimer aussi ceux qui portent des pièces jointes »).
  - **bouton principal** : **« Mettre à jour l'event 07 (41 incidents) »** ; « Annuler ». C'est la confirmation : **pas de seconde fenêtre** « Êtes-vous sûr ? » (le bilan l'a déjà dit).
  - **après** : « ✓ Event 07 mis à jour : 3 incidents créés, 1 supprimé, 12 modifiés. » dans la carte (`aria-live="polite"`), la ligne d'état se met à jour.
  - **export qui ne correspond pas** : « Cet export porte l'event 08 « GREY CELL », pas le 07. Choisissez l'export de l'event 07. » Si JEMM a **renuméroté** l'event (même nom, autre code libre), le bilan le dit en tête : « JEMM a renuméroté cet event : 06 → 07. »
- **« Changer de groupe… »** (Admin seul, `SiAdmin`) : `frappe-mini` à côté de la pastille propriétaire. Fenêtre courte : deux puces GA1 / GA2, la phrase de conséquence « L'event 07, ses 6 storylines et ses 41 incidents passent au GA2 : le GA1 ne pourra plus les modifier. », bouton **« Passer l'event 07 au GA2 »**. Journalisé.

## R7 — Le statut qui s'arrête à « Validé » : 3 étapes, pas 4 grisées

- Pour un incident d'un event « Créé dans MELMIL » (`incidentSansJemm`), `StepperStatut` reçoit `etapes = STATUTS.slice(0, 3)` et dessine **3 segments** (En préparation → En validation → Validé), qui occupent la même largeur (le stepper est en grille : 3 colonnes au lieu de 4 ; sur téléphone, 3 de front au lieu du 2 × 2).
  - ⛔ **Pas de 4ᵉ segment grisé** « Dans JEMM » : une étape grisée dit « il reste quelque chose à faire » — ici c'est faux, et c'est un contrôle désactivé de plus.
  - La `LigneStatut`, quand le statut est « Validé » : « Validé le 02/10 à 16:40 par … **· fin du parcours (event créé dans MELMIL)** ». La raison est écrite une fois, là où l'on regarde.
- `BandeauJemm` et la proposition « Marquer dans JEMM » ne portent **que** sur les incidents d'events JEMM (sinon MELMIL proposerait un statut interdit).
- Le **filtre par statut** (Incidents) garde ses 4 puces ; « Dans JEMM » compte simplement 0 si l'affichage ne contient que des events MELMIL (puce masquée à 0 ? non : on garde la place, Jakob).
- **Migration** : un incident d'un event MELMIL resté en `jemm` passe à `valide` (ou s'affiche « Validé » et se corrige au prochain geste) ; le dire dans le journal.

## R8 — Écarts avec JEMM : seulement les events JEMM, et le dire

- La comparaison ne porte que sur les events `source = "jemm"` (dans le périmètre affiché, R2).
- **Une ligne en tête** de l'onglet : « Les events créés dans MELMIL (21 « ILI-B », 22) ne sont pas comparés : ils n'existent pas dans JEMM. » Sans elle, « ✓ Aucun écart » se lirait comme « tout l'atelier est dans JEMM » (Nielsen 1 ; avis n°34, R8 : jamais un chiffre qui trompe).
- Les « Dans JEMM seulement » qui appartiennent à un **event JEMM absent de l'atelier** : regroupés sous « Event 09 de la planche JEMM, pas encore dans l'atelier » + lien **« Le créer depuis JEMM › »** (ouvre GT1, formulaire R5 en mode JEMM).
- Chaque groupe d'écarts porte la pastille propriétaire (R3) ; le compteur de l'onglet compte le périmètre affiché.

## R9 — Planche de préparation et listes

- Le segment de R2 s'affiche **au-dessus de la planche, à gauche du choix « Affichage : Liste | Clair | Classique »**, sur la même ligne (`flex justify-end gap-4`) : les deux réglages de lecture de la planche au même endroit, comme sur la planche JEMM.
  - ⚠ Sur la planche il s'agit du **même** réglage global que dans les autres onglets (pas un second) : le changer ici le change partout.
- « GA1 seul » : `versPlanche` reçoit le périmètre et **ne dessine que les rangées du GA** (les jours restent ceux du calendrier : la largeur de la planche ne saute pas). Ligne « GA2 masqué : … » au-dessus.
- « Tous » : rangées marquées et cartes en pointillé (R3), non déplaçables (R4). Un incident à moi ne peut de toute façon pas tomber dans une rangée de l'autre GA (la planche n'accepte déjà le dépôt que dans la rangée de son event).
- La **liste par jour** suit les mêmes règles.
- **Export PowerPoint** : il garde son propre choix de périmètre (avis n°17, R2) et n'hérite pas du réglage d'écran ; y ajouter « Groupe : tous / GA1 / GA2 » si l'utilisateur le veut (*facultatif*).

## R10 — Réglages : que deviennent « Verser » et « Aligner » globaux

- **« Verser un export JEMM dans l'atelier » disparaît des Réglages** : son rôle (démarrer sur ce qui existe) est repris, event par event, par « + Nouvel event → Depuis un export JEMM » (R5), avec un propriétaire. Deux chemins pour la même capacité finiraient par diverger (doctrine n°32 : même capacité, même mot, même endroit).
  - Pour le démarrage d'un exercice à 10 events, l'Admin peut garder un **versement groupé** : *si l'utilisateur le souhaite*, le formulaire R5 en mode JEMM accepte **plusieurs fichiers pour l'Admin seulement**, avec un choix de GA par ligne d'aperçu (« 06 ILI → [GA1] [GA2] »). Sinon, rien.
- **« Aligner l'atelier sur JEMM » devient « Mettre à jour tous les events JEMM »** (Admin) :
  - même moteur que le bouton par event (`alignerPerimetre` sur les events JEMM dont le code figure dans les exports choisis) ;
  - **ne supprime plus aucun event** : un event JEMM absent des exports choisis est **laissé tel quel** et listé (« Non touchés : 08 GREY CELL (GA2), absent des exports choisis ») ; les events MELMIL sont listés à part (« Jamais concernés : 21, 22 ») ;
  - un export dont l'event n'existe pas dans l'atelier : listé « Nouveaux events : à créer depuis GT1 » (ou créés avec un GA choisi par ligne, comme le versement groupé) ;
  - le **bilan groupé par event**, avec la pastille de GA, bouton « Mettre à jour 5 events JEMM » ;
  - le texte d'aide actuel (« ce que JEMM ne contient pas est supprimé ») est **réécrit** : « Pour chaque event JEMM choisi, les storylines et incidents absents de son export sont supprimés (sauf ceux qui portent des pièces jointes). Les autres events ne sont jamais touchés. »
- La rubrique « Sauvegarde » reste juste au-dessus, avec le même rappel « avant une mise à jour d'ensemble ».

## R11 — Les messages de refus

À la GOV.UK (doctrine n°24) : ce qui s'est passé, pourquoi, quoi faire ; dans la zone `role="alert"` existante (ou sur place dans le formulaire) ; l'effet local est annulé (n°35, R10). Le serveur renvoie une **raison distincte** (`ga`, `source`, `role`) pour que l'écran ne dise pas seulement « refusé ».

| Cas | Message |
|---|---|
| Geste sur un élément de l'autre GA (filet de sécurité ; l'écran ne devrait pas le permettre) | « Action refusée : l'event 08 et ce qui en dépend appartiennent au GA2. Vous pouvez les lire et y demander un produit ; pour les modifier, adressez-vous au GA2. Rien n'a été enregistré. » *(le nom de l'élément vient de `modificationsHorsPerimetre` : « l'incident 08.01.I03 (GA2) »)* |
| Import d'un export dont l'event est au GA2 | « Import refusé : l'event 08 « GREY CELL » appartient au GA2. Seul le GA2, ou l'Admin, peut le mettre à jour depuis JEMM. Rien n'a été modifié. » |
| Import d'un export dont le code est celui d'un event créé dans MELMIL | « Import refusé : le code 21 est celui d'un event créé dans MELMIL (« ILI-B », GA1). Un event créé dans MELMIL n'est jamais remplacé par un import. Changez le code de l'event MELMIL, ou vérifiez l'export. » |
| Création depuis JEMM d'un event qui existe déjà dans mon GA | Pas un refus sec : « L'event 07 existe déjà (GA1, synchronisé avec JEMM). **Mettre à jour l'event 07 depuis cet export ›** » |
| Changement de groupe sans être Admin (serveur) | « Action refusée : seul l'Admin change le groupe d'un event. Rien n'a été enregistré. » |

## R12 — Synthèse : une seule, qui suit le périmètre et le dit

- **Pas d'onglet ni de bloc « par GA » séparé** : la Synthèse suit le réglage R2, et **son titre le dit** : « Où en est la planification ? · **GA1** » / « · **tous les groupes** ». Un « 29 % » sans périmètre se lirait comme le total de l'exercice (avis n°34, R8).
- En « Tous », **une ligne de comparaison** sous la phrase d'avancement (utile à l'Admin et aux chefs de GA) :
  > GA1 : 18 incidents sur 30 validés ou dans JEMM (60 %) · GA2 : 4 sur 12 (33 %)
  Phrase d'abord, pas de jauge (avis n°34 : ⛔ jauges, scores).
- « Avancement » : « validés ou dans JEMM » reste juste (pour un event MELMIL, « Validé » est la fin). La légende « Validé » peut ajouter « (fin du parcours pour les events créés dans MELMIL) ».
- « À traiter » : « JEMM non marqués », « Dans JEMM absent du dernier export » et « écarts » ne comptent que les events JEMM ; les liens « Voir les N › » ouvrent Incidents dans le même périmètre.
- Tableau « Par storyline » : la pastille propriétaire sur chaque intertitre d'event (R3).

## R13 — Les mots

- **« Groupe d'animation »** (GA1, GA2) = qui peut modifier. **« Confié à »** (groupes de l'Équipe) = qui s'en occupe dans l'organigramme. Les deux restent distincts ; sur la carte d'event, l'un est une pastille d'en-tête (« GA1 »), l'autre reste un champ « Confié à ». Ne jamais écrire « groupe » seul dans un message.
- **« GT »** reste réservé aux étapes ; ne jamais abréger « GA » en « G1 ».
- Source : **« Synchronisé avec JEMM »** / **« Créé dans MELMIL »** partout (formulaire, pastille, bilan, messages) — un seul couple de mots.

## Principe d'implémentation (le plus simple)

1. `QuiContexte` reçoit `gas: string[]` et `admin: boolean` ; `modifiable(ev)` dans `groupes.ts`.
2. **`LectureContexte` imbriqué par event** (R4) : l'essentiel de l'avis sans toucher aux champs.
3. Un hook `usePorteeGa()` (calqué sur `useStylePlanche`) + un composant `ChoixPorteeGa` + un composant `LigneMasques` ; `idsDuGroupe` (déjà écrit) filtre les listes, `versPlanche` reçoit le périmètre et marque les rangées.
4. `PastilleMode` (généralise `PastilleLecture`) et `PastilleGa` / `PastilleSource` (petites, contour, mot + icône).
5. `CarteEvent` : pastilles, ligne d'état JEMM, « Mettre à jour depuis JEMM… » (fenêtre + `Bilan` réutilisé), « Changer de groupe… » (Admin).
6. Formulaire `NouvelEvent` (R5) à la place du clic direct.
7. `StepperStatut` : prop `etapes`.
8. Réglages : retirer « Verser », recâbler « Aligner » sur `alignerPerimetre`, textes réécrits.
9. **CYBERSECU à consulter** sur le contrôle d'accès par GA côté serveur (l'écran guide, le serveur décide).

**Effort estimé** : 1,5 à 2,5 jours (le formulaire de création et la mise à jour par event sont les plus longs ; le reste est mécanique grâce au n°35).
**Vérification** : deux navigateurs (GA1, GA2) + un Admin + un « Lecture et demandes » ; clair et sombre ; téléphone. Parcours : créer un event MELMIL (code 20 proposé, avertissement sur un code JEMM), créer un event depuis JEMM, mettre à jour depuis JEMM (bilan limité, autres events intacts), ouvrir une fiche du GA2 (lecture + « Demander un produit »), tenter un glisser sur une carte du GA2, basculer « GA1 seul » puis recharger (mémoire), Synthèse en « Tous » et « GA1 », import refusé (event GA2, code MELMIL), « Mettre à jour tous les events JEMM » sans event supprimé.

## ⛔ Ce qu'il ne faut pas faire

- **Une couleur par GA** (cartes bleues / vertes) : collision avec storylines, statuts, espace et alertes ; couleur seule.
- **Atténuer les cartes de l'autre GA par l'opacité** : texte sous 4,5 : 1.
- **Cacher l'autre GA sans le dire**, ou **par défaut sans que l'utilisateur l'ait choisi**.
- **Un réglage d'affichage par onglet** ou un onglet « GA2 » à part.
- **Regrouper les rangées ou les listes par GA** : on perd la position des events.
- **Des champs grisés ou des boutons désactivés** sur les éléments de l'autre GA (le n°35 dit pourquoi).
- **Un 4ᵉ segment « Dans JEMM » grisé** pour les events MELMIL.
- **Un import global qui touche aux events MELMIL ou supprime des events** ; une synchronisation automatique avec JEMM.
- **Un propriétaire pré-choisi pour l'Admin** ; un changement de groupe sans phrase de conséquence.
- **Écrire « GA1 » nu à côté de « GT1 »**, ou « groupe » seul (Équipe ou animation ?).

## Questions à trancher (défauts proposés)

1. **Affichage au premier passage** : *« Tous les groupes »* (défaut) ou « Mon GA seul » ?
2. **Code < 20 pour un event MELMIL** : *bloqué* (défaut, comme `codeMelmilInvalide` en cours) ou seulement averti (« codes libres ») ?
3. **Events existants** : tous au GA1 (décidé) ; source déduite du code (≥ 20 → MELMIL, sinon JEMM, comme la migration en cours). *Défaut : la liste des events classés « MELMIL » par cette règle est montrée une fois à l'Admin* (une ligne dans Réglages) pour qu'il vérifie.
4. **Personne GA1 + GA2** : propriétaire à choisir à la création, *aucun pré-coché* (défaut).
5. **Rôle Prod** : ses droits ne changent pas (demandes sur tout incident, lecture du reste) — *défaut*.
6. **Source modifiable après création ?** *Non* (défaut) ; plus tard, éventuellement par l'Admin.

## Sources

REF-14 Nielsen (1 état visible, 4 cohérence, 5 prévention, 6 reconnaître plutôt que se souvenir, 8 minimalisme, 9 erreurs) · REF-12 IBM Carbon (lecture seule ≠ désactivé) · REF-10 GOV.UK (messages d'erreur, boutons désactivés à éviter) · REF-13 WCAG 2.2 (1.4.1, 1.4.3, 1.4.11, 4.1.2) · REF-06 Laws of UX (Hick, Jakob, Tesler, Peak-End) · REF-19 WAI-ARIA APG (Dialog) · REF-07 Refactoring UI (atténuer le secondaire, l'étiquette en dernier recours) · doctrine §3 n°6, 10, 11, 18, 19, 20, 24, 25 · avis antérieurs n°17, 25, 32, 33, 34, 35.
