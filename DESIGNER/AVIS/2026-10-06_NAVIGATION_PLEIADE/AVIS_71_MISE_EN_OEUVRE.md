# Avis n°71 — Mise en œuvre des recommandations R1 à R7 de l'avis n°69 (2026-10-06)

**Demande utilisateur** : « travaille tous les R avec DESIGNER, récupère tout le contexte, contrôle avec l'agent et par toi-même, je veux voir le rendu en localhost ; on verra si on déploie de suite ou après l'exercice ».
**Périmètre** : 8 dépôts (`app-admin`, `app-melmil`, `eho`, `app-press`, `app-messagerie`, `app-cockpit`, `app-leac`, `app-social`). **Rien n'est poussé** : tout est en local, testé, en attente de décision.
**Méthode** : contexte relu (inventaire n°69, doctrine §3.7, REF-21 à REF-25), chaque R dessiné d'après une règle sourcée, codé, puis contrôlé : compilation TypeScript de chaque app, rendu en local (captures `apres\`), image Docker de chaque app sur base vide avec redémarrage.

## R3 — La barre de plateforme, commune à toutes les apps (constat n°1 : des îlots)
- **Dessin** : une barre de 30 px, **toujours sombre** quel que soit le thème de l'app (c'est l'étage de la plateforme, pas de l'app — GOV.UK sépare l'en-tête de plateforme de la navigation du service, REF-22), au-dessus du bandeau de chaque app : « **PLÉIADE · delattre-26** » (lien vers le portail), « **Apps de la zone ▾** », et à droite le nom de l'app où l'on est.
- Le menu liste **toutes les apps de la zone, groupées par type** (Admin, MELMIL, Identités (EHO), Réseau social, Presse…), avec « **vous êtes ici** » sur l'app courante, « Portail de la zone » en tête et « **Premiers pas (aide)** » (→ R6).
- **Règle de sûreté** : la liste ne s'ouvre qu'à l'**animation** (rôle connu de chaque app) ; un **joueur** ne voit que le retour au portail, qui filtre lui-même par groupe. Sur la **presse**, la barre n'existe que côté rédaction (jamais sur le site public, média fictif) ; sur le **réseau social**, elle n'apparaît qu'à l'animation.
- **Technique** : un composant serveur `BarreZone` + `barre-zone.css`, **copiés à l'identique** dans les 7 apps Next (pas de paquet partagé) ; chaque app le nourrit de sa propre découverte Pléiade (`/api/internal/zones/:zone/instances`, déjà présente partout ; ajoutée à MELMIL et eho par copie de `voisines.ts` de LEAC ; cockpit : `appsDeLaZone()` sans filtre). Réseau social : `/api/zone/apps` rend en plus `portail`, composant Angular `app-barre-zone`. Portail = l'hôte d'une app sans son premier étiquette (`melmil.delattre-26.x` → `delattre-26.x`), ou `PLEIADE_PORTAIL_URL`. La messagerie (écran en `100dvh`) retire la hauteur de la barre (`--bz-h`).
- ⚠ Limite connue : la découverte Pléiade ne dit pas quelles apps sont **visibles au portail pour quel groupe** (`portail_visible`, `portail_groupes` ne sortent pas de l'API). D'où la règle « animation seulement ». À demander à Xavier pour un filtrage fin par groupe.

## R4 — MELMIL : sept destinations au lieu de onze (constat n°3)
- **Avant** : 11 onglets en 3 familles + le menu « Étape ▾ » qui ouvrait aussi les onglets GT + la pastille Demandes = trois chemins vers les mêmes écrans.
- **Après** : **5 onglets à plat**, dans l'ordre de fréquence pendant l'exercice — *Planche de préparation · Déroulé · Incidents · Synthèse · Demandes de produit* — et **2 menus** : **Construction ▾** (Events, Storylines, Écarts avec JEMM) et **Organisation ▾** (Équipe, Journal, Réglages). Le menu porte le nom de l'onglet ouvert (« Construction · Events ») et la somme des compteurs quand aucun de ses onglets n'est ouvert ; chaque entrée garde son compteur. Règles 31 et 33 (REF-23 : 3 à 7 destinations ; REF-21 : révélation progressive à 2 niveaux, un seul chemin).
- Le menu **« Étape ▾ » ne change plus d'onglet** : il montre où en est la préparation et, pour l'Admin seul, change d'étape. Sans le rôle, c'est une simple pastille d'état.
- Clavier : les flèches parcourent aussi les onglets rangés (le menu s'ouvre pour donner le focus). Les onglets masqués selon le rôle (Lecture, Admin) le restent.
- Même nom partout pour le choix du groupe d'animation : « **Groupes** » (était « Afficher » sous les onglets).

## R5 — Admin et cockpit : une action principale, le reste dans « Plus ▾ » (constats n°4 et n°5)
- **Éditeur de scénario** : la ligne ne garde que *Vérifier* et *Lancer / Pause / Reprendre* ; **Plus ▾** range Kit IA, Importer un fichier, Exporter en XLSX, et — sous un trait, au bas — *Réinitialiser le scénario*. Onglet « Configuration » → « **Réglages** ».
- **Timeline** : les trois bascules empilées (Chronogramme | Agenda, Par conversation | Par avatar, Plages repliées | Échelle réelle) tiennent dans **un menu « Affichage ▾ »** ; le zoom reste visible (geste fréquent). « Heures : Heure réelle | T+ » reste tel quel (décision utilisateur, avis n°45).
- **Cockpit** : dix commandes égales → « **+ Source** » seule en relief, *Catégorie · Fil global · Recherche · Rafraîchir · Espace* à côté, et **Plus ▾** (Modifier la disposition, Espaces de travail, Reporting, Exporter (JSON)).
- Menus au modèle *Menu Button* de l'APG (REF-19) : Échap et clic à côté ferment, le focus revient au bouton.

## R1 — Corrections immédiates (constats n°7 à n°10)
| Où | Avant | Après |
|---|---|---|
| Social, habillage Instagram | « Plus » **déconnectait** | « Se déconnecter », icône de sortie |
| Social | « In the name of » | « Au nom de » |
| MELMIL, refus d'accès | rôles « Animation », « Lecture et demandes » (inexistants) | « Admin », « GA1 » ou « GA2 » (groupes d'animation), « Prod » ou « Lecture » — les vrais rôles du bouclier |
| Messagerie, refus d'accès | « Modération » ou « Administration » | « Supervision » (le vrai rôle) |
| MELMIL | deux écrans « Réglages » | « Réglages » (atelier) et « Réglages de la planche JEMM » |
| MELMIL Déroulé, Admin Arbre | « Tout replier · Tout déplier » | « Tout déplier · Tout replier », comme partout |
| eho | titres ≠ menu (« Planche relationnelle officielle », « Planches relationnelles des joueurs ») | titres = libellés du menu |
| Cockpit | Layout, Reset, Export JSON, Username | Disposition, Réinitialiser, Exporter (JSON), Nom d'utilisateur |

## R2 — Lexique de zone (constat n°2)
- `PLEIADE\LEXIQUE_ZONE.md` : une notion = un mot, l'état de chaque renommage, et **5 arbitrages demandés** à l'utilisateur (« Supervision » de l'Admin → « Journal de la zone » ? « Avatars » → « Trombinoscope » ? onglet « Rédaction » → « Journalistes » ? rôles du catalogue (Xavier) ; LEAC « Paramétrage » → « Réglages » ?).
- Appliqué sans attendre (sans ambiguïté) : **« publication »** remplace « item » dans tout l'Admin (fenêtre « Publication #5 », « Nouvelle publication », confirmations, réglages) ; « Au nom de » ; titres eho ; ordre déplier/replier ; français du cockpit.

## R6 — Aide tirée (REF-25, REF-21 : jamais de visite guidée)
- Un bouton **« ? »** près du titre de l'écran, qui ouvre trois lignes : *À quoi sert cet écran · Par quoi commencer · Ensuite*. Posé sur : Admin (Tableau de bord, Scénarios, éditeur de scénario, Supervision), **MELMIL (les 11 onglets**, à droite de la rangée), eho (Avatars, Groupes, Planche officielle, Avatars autorisés), presse (Tableau de bord, Articles, Réglages), cockpit (en-tête).
- Une page **« Premiers pas »** dans l'Admin (`/aide`) : deux listes par rôle (*Administration — monter la zone* ; *Animateurs — une journée d'exercice*), chaque étape disant **où** elle se fait, avec le lien ; plus quatre rappels. Atteignable depuis la barre de plateforme de **toutes** les apps (« Premiers pas (aide) »).

## R7 — Observer cinq animateurs
- `PLEIADE\OBSERVATION_ANIMATEURS.md` : protocole prêt à l'emploi (3 tâches lues mot pour mot, feuille de relevé, exploitation, grille d'une journée d'animateur). À faire par l'utilisateur pendant un temps calme ; c'est ce qui tranchera l'ordre définitif des onglets MELMIL (R4) et les arbitrages du lexique.

## Vérifications
- **TypeScript** : `tsc --noEmit` propre sur les 7 apps Next ; `ng build` propre sur le réseau social.
- **Rendu local** (captures `apres\`) : barre de plateforme et menu dans Admin, MELMIL, presse, cockpit ; Admin « Plus ▾ », « Affichage ▾ », « ? », page Premiers pas ; MELMIL 7 destinations, menu Construction, « Construction · Events », menu Étape, « ? » ; presse « ? » ; cockpit en-tête regroupé.
- **Non vu à l'écran** (pas de session locale) : eho (barre, titres, « ? »), messagerie, LEAC, réseau social — contrôlés par la compilation et le démarrage des images.
- **Docker** (image de chaque app, base vide, démarrage + redémarrage) : voir `PLEIADE\JOURNAL.md` du 2026-10-06 (résultats).

## Ce qui reste à décider (utilisateur)
1. **Déployer maintenant ou après l'exercice.** Les R1 sont sans risque ; R3 change l'aspect de toutes les apps ; R4 change les repères des animateurs dans MELMIL (à annoncer).
2. Les 5 arbitrages du lexique.
3. Lancer R7 pendant DELATTRE 26.

⭐ **Doctrine confirmée** : une plateforme de plusieurs apps a **deux étages de navigation** (plateforme, puis app), le même partout ; au plus **sept destinations** par app, choisies par fréquence ; **un seul chemin** par écran ; l'aide se **tire**, elle ne se pousse pas.
