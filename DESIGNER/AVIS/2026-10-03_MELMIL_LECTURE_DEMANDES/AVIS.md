# Avis DESIGNER n°35 — MELMIL : le rôle « Lecture et demandes » (cellule FORAD)

> **Date** : 2026-10-03 · **App** : `app-melmil` (atelier de préparation) · **Demandé par** : NOYAU, sur une décision de l'utilisateur
> **Statut** : 🟡 à appliquer (PLEIADE / ARCHITECTE). DESIGNER contribue, il ne tranche pas.
> **Code lu** : `ecran-atelier.tsx`, `onglets-gt.tsx` (FicheIncident), `champs.tsx`, `statut.tsx`, `produits.tsx` (MediasIncident, FicheDemande, OngletDemandes), `compte-rendu.tsx`, `planche.tsx`, `carte.tsx`.

## La décision à rendre évidente

La FORAD **lit tout** (planche de préparation, synthèse, incidents, fiches, comptes rendus) et **ne modifie rien**, sauf ses **demandes de produit** : elle en crée (avec ou sans incident), complète ou supprime celles de **sa cellule** tant qu'elles sont « Envoyée », joint des fichiers à ses demandes directes, et télécharge tout ce qui est livré ou joint. Le serveur applique la règle. L'écran doit la rendre évidente **sans se transformer en mur de champs grisés**.

**Principe directeur** : pour ce rôle, l'atelier devient **un document à lire, avec une seule action : demander un produit**. Même écran, mêmes places, mêmes onglets (on garde les repères pour parler avec la GREY CELL : « la section Qui de l'incident 08.01.03 »), mais **les valeurs s'affichent comme du texte** et **les gestes impossibles disparaissent**.

---

## R1 — Dire le mode une fois, à un endroit fixe, sans alarme

- **Une pastille dans l'en-tête**, juste après le titre de l'exercice (avant le parcours GT) : icône Lucide `Eye` + **« Lecture et demandes »**. Style neutre (contour `--bord`, texte `--texte-doux`), **ni rouge ni orange** (le rouge est réservé aux alertes, doctrine n°20). C'est un bouton : au clic ou au toucher, une petite bulle (`details` ou popover, accessible au clavier) :
  > **Vous lisez la planification.** Vous pouvez demander des produits à la cellule Prod, compléter ou supprimer les demandes de la FORAD tant qu'elles ne sont pas prises en charge, et télécharger les fichiers. Pour changer un incident, adressez-vous à la GREY CELL.
- **Pas de bandeau permanent, pas de fenêtre à l'arrivée** : la pastille suffit, elle est toujours visible (Nielsen 1, REF-14) et ne coûte pas une ligne d'écran.
- **Les textes d'aide qui décrivent un geste interdit sont réécrits** (sinon l'écran promet ce qu'il refuse, Nielsen 4) :
  - Planche, au-dessus : « Glissez un incident vers un autre jour… » → **« Construite à partir de l'atelier, en direct. Cliquez un incident pour lire sa fiche et demander un produit. »**
  - Onglet Demandes, intro : **« Les demandes de produit adressées à la cellule Prod, et où elles en sont. Créez la vôtre ici, ou depuis la fiche d'un incident. »**
  - État vide de l'atelier (« Réglages → calendrier → verser un export JEMM ») → **« La planification n'a pas encore commencé. »**

## R2 — Les champs : du texte lu, pas des champs désactivés

- `ChampTexte` et `ChampNombre` lisent le mode **eux-mêmes** et rendent un **`<p class="valeur-lue">`** (multiligne : `white-space: pre-wrap`, interligne 1,4, doctrine n°26) au lieu d'un `<input>`. **Aucun des ~40 appels n'a à changer.**
- **Valeur vide** → **« Non renseigné »** en `--texte-doux` italique. ⛔ Jamais le *placeholder* (« E-MAIL, RS, CHAT… » lu comme une valeur réelle serait une fausse information).
- L'`<input type="time">` de l'heure (écrit en dur dans `FicheIncident`, hors `ChampTexte`) → texte « 14:30 ». **À ne pas oublier.**
- `ChoixEtims` → **`EtiquettesEtims`** (le composant de lecture existe déjà) ; aucune ETIM → « Aucune ETIM ».
- `GrilleExcon` → une liste « Cellule : état » en texte (mot + couleur existante, jamais la couleur seule, doctrine n°10).
- `Etiquette` (libellés) inchangée : le couple libellé / valeur garde la structure de la fiche.

**Pourquoi** : Carbon distingue l'état **lecture seule** (contenu lisible, sélectionnable, copiable, contraste normal) de l'état **désactivé** (contraste volontairement faible, contenu « hors jeu ») — REF-12. Un champ désactivé est exempté du contraste 4,5 : 1 (WCAG 1.4.3, REF-13) : donc **illisible par construction** pour qui doit justement *lire*. Et un cadre de champ promet la saisie (affordance) : le voir refuser frustre (Nielsen 5, REF-14).

## R3 — Boutons de création et de suppression : masqués, pas désactivés

- **Masqués** pour ce rôle : « + Nouvel event », « + Nouvelle storyline dans … », « + Nouvel incident dans … », tous les « Supprimer » (event, storyline, incident, compte rendu, média), « Dupliquer sur un autre jour », « Importer des fichiers » (médias de l'incident), « Retirer » (vignettes), « Changer d'étape », « Marquer dans JEMM » (`LigneStatut`, `BandeauJemm`).
- **Gardés** : « Fermer », « Télécharger » (vignettes, fichiers fournis, produits livrés, CR), les filtres, « Tout déplier / replier », le parcours GT (il ne fait qu'ouvrir un onglet), l'export PowerPoint (lecture ; *à confirmer*, voir Questions).
- **Pourquoi masquer** : la restriction est **permanente et liée au rôle**, pas passagère (pas un formulaire incomplet). Un bouton désactivé répété 15 fois est du bruit (Nielsen 8, REF-14 ; Hick, REF-06) ; GOV.UK déconseille les boutons désactivés (« faible contraste, déroutant », REF-10) ; leur explication en infobulle est inaccessible au toucher et au clavier (WCAG 1.4.13). L'explication est donnée **une seule fois**, par la pastille (R1).

## R4 — Statut : la même jauge, mais une étape, pas un bouton

- `StepperStatut` reçoit le mode et rend **le même dessin** (4 segments, pastilles, libellés longs/courts, segments passés) en **`<ol aria-label="Statut de l'incident">`** avec `<li aria-current="step">` sur l'étape actuelle — plus de `role="radio"`, plus de focus, `cursor: default`, pas de survol.
- `LigneStatut` garde **« Validé le 02/10 à 16:40 par … »** ; la proposition « Marquer dans JEMM » disparaît, le signal « ! absent du dernier export » reste (c'est une information).
- **Pourquoi** : garder la forme apprise (Jakob, REF-06 ; avis n°33) ; et ne pas annoncer au lecteur d'écran un groupe radio qu'on ne peut pas changer (WCAG 4.1.2, REF-13).

## R5 — La fiche d'incident : « Demander un produit » en action principale

- Pour ce rôle, **l'en-tête de la fiche porte l'action principale** : à gauche de « Fermer », un bouton `frappe-pleine` **« Demander un produit »** (`title` : « Un produit que les IA en ligne ne savent pas faire : la cellule Prod le réalise »). Il ouvre la même `FicheDemande` pré-remplie avec l'incident (avis n°16, R3).
- C'est **la seule action principale de l'écran** (doctrine n°6) — aujourd'hui elle est enfouie tout en bas, dans « Médias et demandes de produit », sous les champs. Pour la FORAD, la fiche *est* le point de départ d'une demande.
- La rubrique « Médias et demandes de produit » reste en bas : **vignettes avec « Télécharger »** et **liste des demandes** de l'incident (code, statut, nom, échéance). Le bouton « Demande de produit complexe » y reste aussi (même geste au même endroit pour qui a l'habitude ; libellé identique pour l'animation).
- Le message « Aucun fichier pour cet incident. Déposez vos créations… » → **« Aucun fichier pour cet incident. »**

## R6 — Comptes rendus : lire et télécharger

- Tableau ETIM × PSYREP/CIMICREP : « n°k » ouvre toujours l'exemplaire ; **« + Créer », « Importer… », « Supprimer » masqués** ; « .docx (n) » gardé.
- Case sans CR : **« Aucun »** en `--texte-doux` (au lieu des boutons de création).
- `FicheCompteRendu` : `CaseTexte` → texte lu (même règle que R2), cases à cocher (`CelluleFiche`) → ☑ / ☐ en texte ; mention d'en-tête « commun à … · modifié en direct par tous » → **« commun à … · lecture seule »** ; « Télécharger cet exemplaire (n°2) » reste l'action principale ; « Supprimer » masqué.

## R7 — Planche de préparation : on clique, on ne glisse pas

- `Planche.onDeplacer` devient **facultatif** ; absent → `draggable={false}` sur les en-têtes de storyline et les incidents (`carte.tsx`), aucun `onDragStart`, aucune cellule ne s'allume.
- Curseur : **`pointer`** (la carte ouvre la fiche), **jamais `grab` / `move`**.
- Infobulle de l'en-tête : supprimer « Glissez l'en-tête pour tout déplacer. »
- Le clic sur une carte ouvre la fiche (inchangé) : la planche reste la vue d'arrivée (avis n°25).

## R8 — Onglets : masquer ce qui ne sert qu'à administrer, garder les places

| Onglet | Pour ce rôle | Raison |
|---|---|---|
| Events, Storylines, Incidents | **gardés, en lecture** (R2) | le cœur de la lecture |
| Synthèse, Planche de préparation | **gardés** | lecture pure ; dans la Synthèse, masquer le bouton « Marquer dans JEMM » |
| Demandes de produit | **gardé** — son compteur = **demandes FORAD en cours** (non livrées, non refusées) | c'est son espace de travail |
| Équipe | **gardé, en lecture** (organigramme sans « + Groupe » ni panneau d'édition) | savoir à qui s'adresser |
| Écarts avec JEMM, Journal, Réglages | **masqués** | administration de la GREY CELL ; rien à y faire, rien à y apprendre pour une demande |

- Les onglets restants gardent **le même ordre** dans leurs familles (avis n°25, R3). « Organiser » ne contient plus qu'« Équipe » : acceptable.
- Lien direct vers un onglet masqué (`?onglet=reglages`) → **ouvrir la planche**, sans message d'erreur.

## R9 — Demandes de produit : ce que la FORAD peut faire, sans ambiguïté

- **« + Nouvelle demande sans incident »** reste l'action principale de l'onglet (avis n°19).
- **Cellule demandeuse** : pour ce rôle, **fixée à FORAD** et affichée en texte (« Cellule demandeuse : FORAD ») au lieu des deux puces — le serveur refuserait GREY CELL ; ne pas proposer un choix impossible (Nielsen 5).
- Filtre « cellule » : **pré-sélectionné sur « FORAD »** à l'arrivée, « Toutes les cellules » à un clic (non mémorisé).
- `FicheDemande` — la variable `lecture` existante s'étend : **lecture** si la demande n'est **pas de la FORAD**, ou si son statut n'est **plus « Envoyée »**. En lecture, une ligne sous le titre :
  - demande d'une autre cellule : **« Demande de la GREY CELL : lecture seule. »**
  - demande FORAD prise en charge : **« Prise en charge par la cellule Prod : elle ne se modifie plus. Pour un changement, contactez la cellule Prod. »**
- Demande FORAD « Envoyée » : champs modifiables, **« Joindre des fichiers »** (demande directe), **« Supprimer la demande »** (libellé existant gardé : même capacité, même mot, doctrine n°32). Confirmation : « Supprimer la demande DP-04 ? Ses fichiers joints disparaissent avec elle. »
- « Télécharger » visible sur **tous** les fichiers fournis et produits livrés, toutes cellules confondues.

## R10 — Si le serveur refuse quand même

Filet de sécurité (un écran bien fait ne devrait jamais le montrer, mais une demande peut être prise en charge pendant qu'on la complète) :

1. **Annuler l'effet local** : relire l'état partagé, pour qu'aucune valeur refusée ne reste affichée comme enregistrée (Nielsen 1).
2. **Le dire dans la zone d'alerte existante** (`role="alert"` du haut, déjà en place), avec la raison et quoi faire (GOV.UK, REF-10 ; doctrine n°24) :
   - refus de rôle : **« Action refusée : le rôle « Lecture et demandes » permet de lire la planification et de demander des produits, pas de la modifier. Rien n'a été enregistré. »**
   - demande passée en prise en charge entre-temps : **« La demande DP-04 vient d'être prise en charge par la cellule Prod : votre modification n'a pas été enregistrée. Contactez la cellule Prod pour la changer. »**
3. Le serveur doit donc **renvoyer un code distinct** pour ces deux cas (403 rôle / 409 statut), sinon l'écran ne peut dire que « refusé ».

## Principe d'implémentation (le plus simple)

1. **Un seul drapeau dans le contexte qui existe déjà** : `QuiContexte` (`produits.tsx`) porte déjà `prod` ; y ajouter `lecture: boolean` (rôle « Lecture et demandes »), alimenté côté serveur comme `prod`, et un hook `useLecture()`.
2. **Les composants de champ le lisent eux-mêmes** : `ChampTexte`, `ChampNombre`, `ChoixEtims`, `GrilleExcon`, `StepperStatut`, `CaseTexte`, `CelluleFiche`. → l'essentiel du travail se fait en **6 fichiers**, sans toucher aux appels.
3. **Un petit `<SiModifiable>{…}</SiModifiable>`** (rend `null` en lecture) autour des ~15 boutons de R3 et R6.
4. `Planche` : `onDeplacer?` facultatif ; `ecran-atelier.tsx` ne le passe pas en lecture. Onglets : un filtre sur la liste `FAMILLES`.
5. `FicheDemande` : étendre la condition `lecture` existante (R9).
6. Classe CSS **`.valeur-lue`** : taille et couleur du texte courant, `min-height` égale à un champ pour que la fiche ne « saute » pas d'un rôle à l'autre, aucune bordure.

**Effort estimé** : ½ à 1 journée, essentiellement mécanique. **Vérification** : un compte FORAD et un compte GREY CELL côte à côte (deux navigateurs), clair et sombre, téléphone ; parcourir fiche incident → « Demander un produit » → envoyer → compléter → la Prod prend en charge → la fiche FORAD passe en lecture avec sa phrase ; tenter un glisser sur la planche ; ouvrir `?onglet=reglages`.

## ⛔ Ce qu'il ne faut pas faire

- **`<fieldset disabled>` sur l'écran ou la fiche** : il désactive aussi « Fermer », les onglets, « Demander un produit », les filtres — et grise tout (contraste exempté, donc illisible). Acceptable au plus sur un sous-bloc sans aucun bouton utile ; R2 le rend inutile.
- **Des champs grisés** avec leurs *placeholders* visibles.
- **Des boutons désactivés partout**, expliqués par infobulle (inaccessibles au toucher).
- **Un cadenas sur chaque champ**, un bandeau rouge, une fenêtre « Vous êtes en lecture seule » à chaque arrivée.
- **Changer la mise en page** pour ce rôle (autre ordre des sections ou des onglets) : la FORAD et la GREY CELL doivent pointer les mêmes endroits.
- **Masquer de l'information** : tout ce qui se lit reste visible (statut, ETIM, traçabilité, CR, scénarios liés).
- **Croire l'écran** : il guide, le serveur décide (règle déjà posée ; CYBERSECU à consulter sur le contrôle d'accès).

## Questions à trancher (défauts proposés)

1. **Export PowerPoint** pour la FORAD : *gardé* par défaut (c'est de la lecture). À confirmer.
2. **Le rôle est-il toujours FORAD ?** Si un autre rôle « Lecture et demandes » apparaissait (autre cellule), la cellule demandeuse viendrait de l'Équipe et non d'une valeur fixe.
3. **Journal** : masqué par défaut ; à rouvrir en lecture si la FORAD veut suivre « qui a changé quoi ».

## Sources

REF-14 Nielsen (1 état visible, 4 cohérence, 5 prévention des erreurs, 8 minimalisme, 9 erreurs) · REF-12 IBM Carbon (lecture seule ≠ désactivé) · REF-10 GOV.UK (boutons désactivés à éviter ; messages d'erreur qui disent quoi faire) · REF-13 WCAG 2.2 (1.4.3, 1.4.13, 4.1.2) · REF-06 Laws of UX (Hick, Jakob) · REF-07 Refactoring UI (atténuer le secondaire) · doctrine §3 n°6, 10, 20, 24, 26 · avis antérieurs n°16, 19, 25, 32, 33.
