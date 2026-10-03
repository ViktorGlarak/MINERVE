# JOURNAL — DESIGNER

## 2026-10-03 — Avis n°36 : admin, scénarios de bruit de fond

- **Demande** : créer dans l'admin des scénarios nommés reliés à aucun incident ni storyline MELMIL (posts ordinaires, ambiance), bien rangés dans « Scénarios ». L'utilisateur proposait une 3e option dans « Cible du scénario » ou une case.
- **Constat** (code lu le 2026-10-03) : incident obligatoire côté formulaire et serveur dès qu'il y a un MELMIL ; « sans incident » = « Non classés » (à ranger) ; le bandeau invite à rattacher ; le segment n'a ni rôle ni état ARIA.
- **Avis** : `AVIS\2026-10-03_ADMIN_SCENARIOS_BRUIT\AVIS.md`, R1 à R15. Points clés : 3e segment « Bruit de fond » plutôt qu'une case (choix exclusifs, pas de mode caché) ; drapeau explicite côté données ; section « Bruit de fond » distincte, entre l'arborescence et « Non classés », sous-groupée par jour ; conversions dans les deux sens par le bandeau.
- **Statut** : proposé, à arbitrer par l'utilisateur ; aucun code modifié.

## 2026-10-02 — Avis n°34 : MELMIL, synthèse de planification

- **Demande** : voir d'un coup d'œil où en est la planification (incidents, en prépa, sans pièce jointe ni scénario…), nouvel onglet possible, ergonomie soignée ; à voir en local d'abord.
- **Constat** : tout est déjà calculable (statuts, `piecesDeLIncident`, `scenariosDe`, `ecarts`, demandes) mais éparpillé sur 4 onglets.
- **Avis** : `AVIS\2026-10-02_MELMIL_SYNTHESE_PLANIFICATION\AVIS.md`, R1 à R9 + maquette textuelle. Points clés : onglet « Synthèse » en tête de *Visualiser* sans changer l'arrivée ; phrase + barre empilée (Validé hachuré / Dans JEMM plein, car même vert) ; chaque manque = un lien vers Incidents filtré par un nouveau paramètre `manque` (non mémorisé), calculé par une seule fonction pure ; jamais de 0 quand les scénarios ou JEMM sont indisponibles.
- **Limite signalée** : pas encore de source dédiée aux tableaux de bord (Few, NN/g) dans nos fiches.
- **Statut** : à appliquer par PLEIADE / ARCHITECTE, en local d'abord.

## 2026-10-02 — Avis n°27 : admin, retrouver ses scénarios dans la masse

- Demande de l'utilisateur : on ne retrouve plus ses scénarios dans l'app-admin. On cherche par incident MELMIL, et les noms commencent en général par le code.
- Constat : liste plate triée par dernière modification (l'ordre change sans cesse), grandes cartes (environ 5 par écran), aucun regroupement.
- Proposé : rangement par event › storyline › incident lu dans le nom, une ligne par scénario, recherche qui comprend les codes, affichage mémorisé, modèle de nom à la création.
- Signalé au passage : le `createdById` aléatoire des scénarios créés avant la correction d'identité.
- Statut : proposé, en attente de la décision de l'utilisateur. Détail dans `AVIS\2026-10-02_ADMIN_RANGER_SCENARIOS\AVIS.md`.

## 2026-10-01 — Avis n°19 : MELMIL, demande de produit sans incident + cellule demandeuse

- **Demande** : la FORAD ne crée pas d'incident. Il faut un bouton dans l'onglet « Demandes de produit », et chaque demande doit indiquer GREY CELL ou FORAD. DESIGNER a été associé à la mise en place.
- **Avis** : `AVIS\2026-10-01_MELMIL_DEMANDE_SANS_INCIDENT\AVIS.md`, R1 à R6. Les deux décisions clés : une **cellule obligatoire pré-choisie, en choix visibles** ; une **demande directe qui porte elle-même ses fichiers**.
- **Appliqué** dans `app-melmil` `533e548` (`2026-10-01.1`). Vérifié avec Playwright en local.

## 2026-10-01 — Avis n°18 : portail de zone, page « Presse », la carte entière ouvre le site

- **Demande** : supprimer le bouton « Ouvrir », faire ouvrir le site par un clic sur la carte, garder « Espace de rédaction ».
- **Avis** : `AVIS\2026-10-01_PORTAIL_CARTES_PRESSE\AVIS.md`, R1 à R7. Le point clé est le **lien étiré** : il ne faut jamais mettre un lien dans un lien, et le survol du bouton secondaire ne doit pas animer la carte.
- **Appliqué** dans `pleiade-platform` `4995efc` (`portail.ts`, `pageChoix`). Vérifié avec Playwright : zones de clic, survols, focus, téléphone.
- **Leçon technique** : une capture prise juste après un `mouse.move` saisit la transition en cours. Attendre ~400 ms avant de capturer un état de survol.

## 2026-09-30 — Avis n°15 : MELMIL, médias des incidents et demandes de produit complexe

- **Demande** : un bouton « Demande de produit complexe » sur chaque incident (FORAD, GreyCell vers la cellule Prod), et les fichiers de l'incident visibles, avec un import. Le formulaire InfoG d'ORION 26 est à remanier.
- En cours de route, l'utilisateur a renoncé à la fiche Word : « un seul outil ». Elle a été retirée.
- **Avis** : `AVIS\2026-09-30_MELMIL_PRODUITS\AVIS.md` (R1–R8), captures `captures\`.
- **Appliqué** : `app-melmil` `e5fcf86`, et le catalogue de `pleiade-platform` `7de590f`.

## 2026-09-29 — Avis n°14 : maquettes existantes d'app-press (TM, HEX, TV4, BC1)

- **Demande** : optimiser le rendu et l'architecture des 4 maquettes de médias fictifs, en respectant les chartes des pays (Today Mercure = média d'État « russe », en anglais). Les 6 reprises de sites réels sont exclues.
- **Avis** : `AVIS\2026-09-29_PRESSE_MAQUETTES\AVIS.md`, 9 constats et R1–R8, captures `avant\` / `apres\`.
- **Appliqué** : `app-press` branche `design-maquettes` `48b1072` ; image reconstruite comme sur le serveur, tests OK. En attente de validation et de mise en ligne.
- **Leçons** :
  - un banc d'essai de maquette de presse doit contenir des articles **sans photo** ;
  - les images différées ne sont pas chargées dans une capture pleine page : faire défiler la page avant.

## 2026-09-28 — Avis n°13 : MELMIL, « Confié à » par groupes

- **Avis** : `AVIS\2026-09-28_MELMIL_CONFIE\AVIS.md`, R1–R6 : le choix suit la hiérarchie, des pastilles d'un clic, dire ce que signifie « rien de coché », un état vide qui guide, ne rien perdre, montrer le résultat partout.
- **Appliqué** : `app-melmil` `a65d6f2`.

## 2026-09-28 — Avis n°12 : organigramme, placer les groupes reliés côte à côte

- **Avis** : `AVIS\2026-09-28_MELMIL_PLACEMENT\AVIS.md`, R1–R3 : supprimer l'information vide, la proximité suit la relation (chaînes de colonnes, sous-groupe du côté de son partenaire), un placement stable.
- **Appliqué** : `app-melmil` `04b3a15`.

## 2026-09-28 — Avis n°11 : MELMIL, Équipe, de l'araignée à l'organigramme

- **Déclencheur** : trois remarques de l'utilisateur sur l'avis n°10 (niveaux masqués, un seul rattachement, exercice au centre trompeur).
- **Avis** : `AVIS\2026-09-28_MELMIL_ORGANIGRAMME\AVIS.md`, R1–R5.
- **Leçon de doctrine** : une mise en page radiale fixe un nombre de couronnes et confond « contenir » avec « être au centre ». Pour une structure militaire, l'organigramme (Jakob) ; deux relations différentes = deux traits différents, ET un texte.
- **Appliqué** : `app-melmil` `84294f7`.

## 2026-09-28 — Avis n°10 : MELMIL, onglet Équipe (araignée)

- **Avis** : `AVIS\2026-09-28_MELMIL_EQUIPE\AVIS.md`, R1–R7 : lire d'abord et modifier dans le panneau, deux vues (araignée, liste), des choix plutôt que de la saisie, couleur doublée du nom, une seule action principale, état vide, rien de perdu.
- **Appliqué** : `app-melmil` `f9f72b6` (branche `equipe-organigramme`).

## 2026-09-28 — Avis n°9 : eho, ranger 235 groupes

- **Avis** : `AVIS\2026-09-28_EHO_RANGER_GROUPES\AVIS.md`, R1–R5 : masquer sans supprimer, assistant qui propose par famille, résultat avant d'appliquer, aucune supposition invisible, archives à portée.
- **Appliqué** : `eho` `8bb7084` (branche `groupes-archives`), 235 → 6 visibles en local.

## 2026-09-27 — Avis n°8 : LEAC, la pastille d'état du réseau

- **Demande** : voir si l'écran vient du serveur (« direct », en vert) ou de la copie du service worker.
- **Avis** : `AVIS\2026-09-27_LEAC_PASTILLE_RESEAU\AVIS.md`, R1–R5.
- **Appliqué** sur `etat-reseau` (`a4639f3`), puis mis en ligne le même jour (`2026-09-27.1`).

## 2026-09-25 — Avis n°7 : MELMIL, choisir les ETIM d'un incident

- **Demande** : cocher les ETIM concernées à la création d'un incident, et voir leurs noms sur la carte dans la planification.
- **Avis** : `AVIS\2026-09-25_MELMIL_ETIM\AVIS.md`, R1–R5 (voir §6 de la mémoire).
- **Appliqué** : `app-melmil` `5b4d76a`, version `2026-09-25.1`, sur la branche `etim-incidents`. Testé en local au téléphone et sur ordinateur.

## 2026-09-25 — Avis n°6 : eho, onglet Groupes (liste des membres)

- **Demande** : cliquer sur un groupe pour voir ses avatars — @compte du réseau social et nom/prénom, sans la fiche complète. « Très beau et fluide », mis en ligne directement.
- **Avis** : `AVIS\2026-09-25_EHO_GROUPES\AVIS.md`, R1–R6 (voir §6 de la mémoire).
- **Relevé en préparant** : `GET /api/groups/[id]/members` était lisible par tout joueur. Or un nom de groupe révèle ce que le joueur doit découvrir. La route est désormais réservée à l'animation et à la clé de service.
- **Mis en ligne** : `eho` `124679a`, `2026-09-25.4`.

## 2026-09-25 — Avis n°5 : l'écran Avatars d'eho (rail, préchargement, retour)

- **Demande** :
  - voir images et fiches bio des cartes affichées, grâce à un préchargement qui ne fait pas planter ;
  - pouvoir refermer ce qu'on a déplié ;
  - faire défiler plutôt que cliquer, sans agrandir la fenêtre.
- **Défaut trouvé** : si sa lecture échouait, une fiche restait sur « Chargement… » pour toujours.
- **Solution** : `AVIS\2026-09-25_EHO_AVATARS\AVIS.md`, R1 à R5, appliquée sur `eho` `avatars-rail` (`a3bf90a`).
- **Vérifié**, avec 3 500 avatars en CPU ×4 :
  - sur un bloc de 625 cartes, le défilement charge 60 → 420 et la page reste à la même hauteur ;
  - « Revenir au début » ramène à 60 ;
  - la fiche s'ouvre avec sa bio sans chargement ;
  - les portraits à l'écran sont chargés (4/4) ;
  - aucun débordement au téléphone.

## 2026-09-24 (nuit) — Avis n°4 appliqué en local sur eho, + chargement par groupe

- **Demande** : tout mettre en œuvre en local ; en plus, à ~3 500 avatars (DE LATTRE 26), faire charger les avatars « par groupe », les pages buguant sous la charge.
- **Banc d'essai** : copie locale de la base `eho` → **`eho_charge`**, plus 3 050 avatars générés (3 503 au total). Mesure faite en CPU ×4 et réseau 10 Mbit/s, 60 ms.
- **Fait** : l'état complet est dans `AVIS\2026-09-24_EHO\AVIS.md` § « Suite donnée ».
- **Corrigé dans l'avis** :
  - P4 : l'alternative clavier existait déjà pour la zone ;
  - la confirmation de modèle demandait déjà de taper le code.
- **Vérifié** :
  - 0 page plus large que l'écran ;
  - le contenu démarre à 0 px au téléphone et à 68 px sur tablette ;
  - rangement de 3 cartes en une action ;
  - confirmation : focus sur « Annuler », Échap ferme ;
  - mode sombre lisible ;
  - aucune fuite de données officielles vers un joueur (liste et fiche) ;
  - la nouvelle route `/api/avatars/planche` renvoie 403 à un joueur.

## 2026-09-24 (soir) — Avis n°4 : eho, propositions sans code

- **Demande** : analyser eho et dire, **sans coder**, ce qu'il faudrait changer pour le rendre plus fluide et utilisable par tous (téléphone, tablette, ordinateur).
- **Examiné** : `eho` `aa791a4`, en local sur le port 3001, 10 écrans animateur + 3 écrans joueur + la connexion, sur iPhone 13, iPad Mini et 1440 px, plus un passage en mode sombre du système.
- **Constats majeurs** :
  - mode sombre blanc sur blanc (seul `--background` est redéfini) ;
  - menu de 256 px fixe au téléphone ;
  - tableaux Avatars et Modèles coupés sans défilement sous 1024 px ;
  - rangement uniquement par glisser-déposer natif (`draggable`), sans alternative ;
  - JSON brut au tableau de bord ;
  - 8 `confirm()` natifs ;
  - 29 textes à 8-11 px.
- **Rendu** : `AVIS\2026-09-24_EHO\AVIS.md` (12 problèmes, 11 recommandations en 3 lots, ordre conseillé, critère de réussite) et 13 captures.

## 2026-09-24 (soir) — Avis n°3 : MELMIL v2, appliqué en local

- **Demande** : repenser toute l'architecture de MELMIL pour la lisibilité et l'accessibilité, comme pour LEAC, du téléphone à l'ordinateur.
- **Audit de départ** (`2026-09-24.4`, iPhone 13) : sélecteur d'espace poussé hors écran, tableau des incidents débordant de 220 px, contenu à 370 px du haut, 5 boutons en barre, grille illisible au téléphone. Tablette et ordinateur corrects.
- **Proposition** : `AVIS\2026-09-24_MELMIL_V2\PROPOSITION.md` (R1–R8), toute appliquée sur `app-melmil` branche `refonte-v2` (`03e3363`).
- **Corrections trouvées en vérifiant** : « Afficher » cassé lettre par lettre (select trop large), codes coupés « 06.0 / 1 », éditeur à 280 px minimum, menus « Plus » et « Changer d'étape » hors écran, bandeau trop large à 150 %.
- **Résultat** : 0 débordement sur iPhone SE, 13, 13 Pro Max, Pixel 7 (100 et 150 %), iPad Mini, 1440 px ; 166/166 tests ; captures dans le scratchpad de session.

## 2026-09-24 (suite) — 11 sources de plus + premier audit (MELMIL)

- **Décisions de l'utilisateur** :
  1. le gaver de sources fiables et gratuites, en lui laissant proposer les siennes ;
  2. Refactoring UI : pas de livre, on s'en tient aux extraits gratuits ;
  3. pas de thème PLÉIADE unifié.
- **Ingérés** (REF-10 à REF-20) : GOV.UK (principes et Design System), DSFR (⛔ réservé aux sites `.gouv.fr` : inspiration seulement), IBM Carbon (couches, tableau de données), WCAG 2.2 AA (seuils), 10 heuristiques de Nielsen, Radix Colors (12 crans), A11Y Project, Practical Typography, Inclusive Components (index), WAI-ARIA APG (Dialog, Tabs), ressources libres (bradtraversy). Ajout à REF-07 du chapitre gratuit « Building Your Color Palette ».
- **Refus de lecture automatique** : systeme-de-design.gouv.fr et Medium (403) → contournés par le README GitHub du DSFR. L'article Medium de Refactoring UI reste à lire.
- **Correction** : une lecture automatique attribuait 44 × 44 px au critère WCAG 2.5.8. La vraie valeur est 24 × 24 (AA), et 44 × 44 relève du critère 2.5.5 (AAA). Règle 12 corrigée.
- **Doctrine** portée à 26 règles, avec une grille d'audit (§3.6) et une liste de sources à ingérer ensuite (§5 bis).
- **Avis n°1 — MELMIL** : `AVIS\2026-09-24_MELMIL\AVIS.md`. 8 problèmes relevés, dont 1 de gravité 4 (on ne voit pas dans quel espace on est) et 4 de gravité 3. 8 recommandations, dont 5 retouches légères à faire d'abord.

## 2026-09-24 — Création de l'agent + première ingestion (9 sources)

- **Demande de l'utilisateur** : un agent « DESIGNER » qui maîtrise les documents de design fournis petit à petit, pour conseiller sur le design de nos sites et applicatifs. Il n'a pas forcément la vérité sur nos projets, mais il y contribue pour rendre le design plus agréable à l'humain.
- **Ingérés** (une fiche chacun dans `REFERENCES\`) : shadcn/ui, Radix Primitives, HyperUI, Awesome Design Systems (klaufel), Awesome React Design Systems (jbranchaud), Laws of UX, Refactoring UI, Lucide, Motion.
  - Pages GitHub complétées par la documentation : thème shadcn, introduction Radix, accessibilité Motion, fiches Fitts, Hick et Jakob de Laws of UX.
  - Les liens fournis portaient `?utm_source=gemini` : ce paramètre de suivi a été retiré.
- **Terrain relevé dans le code** : deux familles de jetons (thème PLÉIADE pour admin et press, graphite/craie pour MELMIL et LEAC), Tailwind 4 partout, lucide-react dans admin et press, eho non habillé.
- **Doctrine** : 20 règles sourcées dans `MEMOIRE.md` §3.
- **Premier constat utile** : la fiche de compte rendu de MELMIL (livrée le même jour) ferme bien sur `Échap`, mais elle **ne piège pas le focus** et **ne le rend pas** au bouton d'origine (règle 11, REF-02). À proposer à la prochaine intervention sur MELMIL.
- **Questions ouvertes** : DSFR, GOV.UK et Carbon à ingérer ? PDF de Refactoring UI disponible ? Thème PLÉIADE unifié ?
- **Prochaine étape** : ingérer les documents suivants de l'utilisateur ; rendre un premier avis sur un écran réel dès qu'on en sollicite un.
