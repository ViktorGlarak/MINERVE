# Avis n°63 — MELMIL : le déroulé de chaque incident, en temps réel (2026-10-05)

> Demande de l'utilisateur : voir, pour chaque incident, son déroulé complet pendant l'exercice — FAM (CRI, observation…) joué à l'heure JEMM de l'incident, puis tweets et articles de presse des scénarios de l'admin, puis le CRQ — et **où l'on en est, à l'heure près**. Proposer l'emplacement (Synthèse, autre onglet ou nouvel onglet).
> Prototype : `prototype.html` (servi en local, données **fictives**, calendrier réel de l'essai : D+27 = mar. 06/10/2026).

## Ce que les données permettent (relevé du code, 2026-10-05)
- **FAM** : présent dans tous les exports JEMM (`Injections[].FunctionalAreaMessage`), **jamais lu par MELMIL** aujourd'hui (`lireExportJemm`). Un FAM « vide » = la bannière `*** EXERCISE … ***` seule, éventuellement suivie du mot type (CRI, DRAFT). Test retenu : il reste ≥ 12 caractères une fois bannière et mot type retirés ; le type se lit sur la première ligne.
- **Joué ?** JEMM ne le dit pas (`ActualDateTime` toujours `null` ; `StateOnDelivered` est un réglage du moyen, pas un état). FAM joué = heure JEMM passée. Tweets / presse : l'admin sait (`status = published`, `publishedAt`).
- **Admin** : `GET /api/service/scenarios` ne renvoie que des compteurs → il faut y ajouter les éléments (heure prévue = début + delta cumulé, type d'app social/presse, statut, heure de publication).
- **CRQ** : un par jour et par groupe d'animation (pas par incident). Dans JEMM, il est joint à l'inject CRQ du jour en `.pdf`, numéroté sur l'inject CRQ, alors que MELMIL exporte un `.docx` numéroté sur l'incident d'où on l'ouvre → rapprocher par **date + cellule + « CRQ-UTMC »**, sans l'extension ni le numéro.
- ⚠ Les exports JEMM du 05/10 portent le marquage **NATO RESTRICTED** (fichier) : aucun de leurs contenus n'est repris dans le prototype.

## Trois propositions
- **B — nouvel onglet « Déroulé » (Visualiser), chronogramme.** ⭐ **Recommandé.** Une ligne par incident rangée par storyline ; sur l'axe du temps, à l'heure près : ◆ FAM, ● tweet, ■ presse, ■ noir CRQ. Plein + ✓ = joué ; contour = à venir ; « ! » pointillé = à corriger ; ✕ = échec de publication. Ligne verte « MAINTENANT » qui avance seule, passé légèrement teinté. Échelles Jour / 3 jours / Période, « Revenir à maintenant ». Clic sur une ligne ou un repère → tiroir : 4 étapes + fil chronologique avec repère « Maintenant » et texte du FAM.
- **A — dans la Synthèse, 4 étapes par incident** (FAM → Tweets → Presse → CRQ, comme un suivi de colis), trait de progression, « Prochain : … dans 1 h 40 », filtres. Sans apprentissage, mais l'heure de chaque élément ne se voit qu'en détail.
- **C — « Maintenant »** : compteurs + 3 colonnes (vient d'être joué 3 h · à venir 6 h · à corriger avant que ce soit joué). Idéal pendant le jeu, sans vue d'ensemble d'un incident.

**Recommandation** : B comme vue, en reprenant **les 4 étapes de A dans le tiroir** et **les compteurs + « À corriger » de C en tête de l'onglet** ; la Synthèse gagne une ligne « Déroulé : n FAM vides · n éléments à jouer dans les 6 h → Voir ».

## Doctrine appliquée
- Jamais la couleur seule (§3.3-10) : forme par type (losange, rond, carré), ✓ / contour / « ! » / ✕ pour l'état.
- Une seule couleur d'alerte, rare (§3.4-20) : le rouge ne marque que ce qui est à corriger.
- L'état du système toujours visible (§3.4-25) : heure de jeu et ligne « MAINTENANT » permanentes.
- Clavier : lignes et repères focalisables, Entrée ouvre, Échap ferme (§3.3-11). « Réduire les animations » respecté.

## Itération 1 (retour utilisateur, même jour)
- Icônes refaites : pictogramme par type (document = FAM, bulle = tweet, journal = presse, presse-papiers = CRQ, Lucide), forme arrondie, **plein + pastille verte ✓ = joué**, contour = à venir, « ! » rouge pointillé = à corriger, ✕ rouge = échec. Les repères à moins de 30 px **se regroupent** en un seul avec « +N » (au lieu de s'empiler), le détail liste tout.
- Demande : depuis le détail, **aller au scénario de l'admin** lié au tweet ou à l'article → bouton « Ouvrir le scénario dans l'admin ↗ » sous chaque tweet / article (en réel : `admin/scenarios/<id>`, nouvel onglet) ; l'élément cliqué est surligné dans le détail.

## Itération 2 — scénarios de storyline et bruit de fond (même jour)
- **Scénario de storyline** (plusieurs incidents) : ses publications vont sur la **ligne de la storyline** (en-tête cliquable, « ▶ n »), jamais recopiées sur chaque incident (sinon un même tweet compterait n fois). Plusieurs scénarios sur un incident : leurs publications s'additionnent sur sa ligne, chacune reliée à son scénario.
- **Bruit de fond** : section séparée tout en bas (trait fort, intitulé « Bruit de fond — sans incident · ni FAM ni CRQ »), **une ligne par cellule** (GREYCELL, FORAD toujours ; « Cellule non renseignée » seulement si elle a des publications), fond **hachuré** (le motif + le texte disent « bruit », pas la couleur seule), mêmes icônes tweet / presse / message ; pas de FAM ni de CRQ ; détail = liste des publications, chacune vers son scénario ; les échecs remontent dans « À corriger ».
- Mise à jour en direct : MELMIL relit l'admin toutes les 30 s (cache serveur 15 s) — vérifié : un tweet ajouté apparaît en ~30 s sans recharger.

## Itération 3 — amorce et suite (même jour, règle utilisateur)
- Règle : l'heure JEMM de l'incident = le FAM ; le CRQ du jour le clôt en fin de journée (un CRQ par jour et par ETIM, **jamais celui du lendemain**). Un scénario peut **amorcer** (tweets 1 à n jours avant le FAM) et **prolonger** (après le CRQ).
- Écran : trois temps — **amorce** (avant le FAM) et **suite** (après le CRQ) en **pointillé fin**, le **cœur FAM → CRQ en trait plein** ; état de l'incident « En amorce » / « En cours » / « Suite » ; détail avec intertitres « Amorce — avant le FAM », « Incident — du FAM au CRQ du jour », « Suite — après le CRQ » et une ligne de synthèse (« Amorce : 2 publications dès mar. 06/10 10:00 · Suite : 4 jusqu'au jeu. 08/10 18:00 ») ; à heure égale : amorce, FAM, incident, CRQ, suite. Un FAM placé après l'heure du CRQ du jour donne une **remarque** (pas une alerte).

## Questions pour l'utilisateur
1. Le **CRQ qui clôt un incident** : celui du jour de la **dernière publication** (hypothèse du prototype), ou celui du **jour de l'incident** (lien actuel de MELMIL) ?
2. Pour « joué », se fier à l'**heure** (FAM) et au **statut admin** (tweets / presse) — d'accord ?
3. Le FAM se lit à l'**import JEMM** : l'afficher en entier dans le tiroir, ou seulement « présent / vide » + type ?
