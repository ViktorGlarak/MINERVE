# Avis n°85 — Social : repère d'origine des publications (animation seulement)

> **Date** : 2026-10-09 · **Demandeur** : utilisateur (animation DELATTRE 26) · **App** : `app-social` (habillages X, Facebook, Instagram)
> **Statut** : proposition. DESIGNER **contribue, ne tranche pas** (MEMOIRE §1). Code lu sans rien modifier : `apps/web/src/app/components/post-card/post-card.ts`, `apps/api/prisma/schema/social.prisma` et `base.prisma`, `eho/prisma/schema.prisma`.

## 1. Besoin

Pour l'animation et l'administration, un repère **qu'on active ou désactive**, qui dit d'où vient une publication, un commentaire ou un repost :

| Origine | Ce qu'on veut lire |
|---|---|
| Joueur, via son avatar | **groupe** (ex. DIV 1) + **compte réel** (ex. dv01) |
| Animateur, à la main, via un avatar | **cellule** (GREYCELL, FORAD…) + compte réel |
| Console d'animation (scénario) | cellule du scénario + **scénario** (lien vers la console) + **incident MELMIL** (lien vers MELMIL), ou storyline, ou « bruit de fond » |
| Réactions générées | likes et reposts simulés, avec leur scénario |

## 2. Constats

1. **Les données n'existent pas encore côté post.** `SocialPost` porte seulement `parAnimation` (vrai/faux). Ni le compte réel, ni le groupe, ni le scénario ou l'incident ne sont stockés sur la publication (le scénario n'apparaît que dans `SystemLog.scenarioId` / `functionalId`). → **Préalable hors design** : PLEIADE / MASTORION ajoutent l'origine à l'écriture (compte réel, groupe ou cellule, scénario, n° d'incident ou storyline).
2. **Fuite = faute grave.** Le repère ne doit **jamais être envoyé** à un navigateur de joueur. Le masquer en CSS ne suffit pas : l'API ne renvoie ces champs qu'aux rôles animation et administration. → **CYBERSECU à consulter** (même logique que `parAnimation`, R4).
3. **La couleur de groupe existe déjà** : `Group.color` dans eho (défaut `#6364ff`) ; MELMIL a sa palette fermée de 8 teintes pour les cellules (avis n°43). Deux sources possibles : à unifier (question Q1).
4. **Un signe déjà adopté** : dans MELMIL, l'appartenance à une cellule se dit par un **trait vertical à gauche** (avis n°43, leçon : « un même sens = un même signe partout »).
5. **Précédent dans la carte** : le badge « Programmé · heure » (vu par l'animation seulement) est déjà glissé dans l'en-tête du post. L'en-tête est **plein** (nom, @, heure, Programmé, ✎ 🗑, ⋯) : on n'y ajoutera rien de long.
6. **Le geste connu des joueurs** : X, Facebook et Instagram ont tous une **ligne de contexte au-dessus du post** (« dv01 a reposté », « Suggéré pour vous »). Notre `boost-header` la reproduit déjà.

## 3. Trois variantes

Textes communs aux trois variantes (le **mot de type** est toujours écrit en premier : la couleur n'est jamais le seul porteur, règle 10) :

| Origine | Texte exact | Liens |
|---|---|---|
| Joueur | `Joueur · DIV 1 · dv01` | aucun |
| Animateur à la main | `Animation · GREYCELL · anim03` | aucun |
| Scénario + incident | `Scénario · GREYCELL · Pression sur Hxxx · Incident 07.01.I03` | « Pression sur Hxxx » → console (scénario) ; « Incident 07.01.I03 » → MELMIL (fiche de l'incident) |
| Scénario + storyline | `Scénario · FORAD · Rumeurs eau · Storyline 07-02` | scénario → console ; storyline → MELMIL (planche filtrée), si le lien existe |
| Scénario, bruit de fond | `Scénario · FORAD · Ambiance Toul · Bruit de fond` | scénario → console ; « Bruit de fond » en texte simple |
| Scénario supprimé depuis | `Scénario · GREYCELL · scénario supprimé · Incident 07.01.I03` | « scénario supprimé » en italique, non cliquable |
| Origine non enregistrée (posts antérieurs) | `Origine inconnue` | aucun, style de repli |

**Liens** : soulignés en permanence (pas seulement au survol) + icône `ExternalLink` 12 px (Lucide, REF-08) car ils ouvrent une autre app ; ouverture dans un **nouvel onglet** pour garder sa place dans le fil (Q4) ; le clic **ne déclenche pas** l'ouverture du post (`stopPropagation`, la carte est cliquable). Cible ≥ 24 px de haut (règle 12). Texte trop long : nom du scénario coupé à ~32 caractères avec « … », titre complet en infobulle et dans `aria-label`.

**Couleur** : celle du groupe (joueurs) ou de la cellule (animateurs, scénarios). **Repli** : ardoise neutre + trait **en pointillés**, quand le groupe n'a pas de couleur ou que l'origine est inconnue. **Contraste** : trait et cadre ≥ **3 : 1** sur le fond de la carte, dans chaque habillage clair et sombre (WCAG 1.4.11, règle 21) ; texte ≥ **4,5 : 1** (règle 21) : texte cran 11-12 sur fond cran 3 (règle 22, REF-15). ⚠ Éviter le **bleu de X/Facebook**, le **vert du repost** et le **rose du like** pour un groupe : ils signifient déjà quelque chose dans l'habillage (règle 20, Von Restorff REF-06 ; avis n°43 R5). Le « DIV 1 bleu » de l'exemple est à confirmer (Q2).

### A. Ligne d'origine au-dessus de la carte + trait gauche (recommandée)

- **Anatomie** : une ligne de **24 px** collée au-dessus de la carte, **hors de l'habillage** (la carte elle-même n'est pas touchée) : fond teinté du groupe (cran 3), texte 12 px cran 11-12, icône 14 px de type (`User` joueur, `PenLine` animation, `Workflow` scénario, `Sparkles` simulé). Un **trait de 4 px** à la couleur du groupe sur le bord gauche, de la ligne jusqu'au bas de la carte (le même signe que MELMIL).
- **Style « outil »** : police système, coins droits, pas d'arrondi ni d'ombre de l'habillage : on voit tout de suite que ce n'est pas un élément du réseau.
- **Repost** : la ligne d'origine décrit **l'acte affiché** (qui a reposté) et **remplace la teinte** du `boost-header` sans le supprimer ; l'origine du post repris s'ajoute en fin de ligne : `Joueur · DIV 1 · dv01 — original : Scénario · GREYCELL · Incident 07.01.I03` (le segment « original » cliquable ouvre une petite fenêtre détaillée). Le trait gauche prend la couleur de **l'acte** (le repost).
- **Commentaire** : version compacte **dans la ligne d'en-tête du commentaire**, en fin de ligne, 11 px, sans fond : `▍DIV 1 · dv01` (trait de 3 px devant) ; le détail complet (type, scénario, incident) dans une infobulle et au clic.
- **Citation** : l'encart cité ne porte pas de repère (il s'ouvre en un clic).
- **Réactions simulées** : pas de ligne dans le fil (ce ne sont pas des posts) ; dans la fenêtre « Favoris / Partages / Citations » (avis n°82), chaque ligne simulée porte en fin de ligne `Simulé · Pression sur Hxxx`.
- **+** lisible d'un coup d'œil, place pour les liens, aucune modification de la carte habillée, même signe que MELMIL, geste connu (ligne de contexte, Jakob REF-06).
- **−** ajoute 24 px par post (≈ 1 000 px sur 40 posts) ; répétitif quand une cellule publie 10 posts de suite.

### B. Cadre complet coloré + étiquette en coin

- **Anatomie** : bordure de **2 px** à la couleur du groupe tout autour de la carte ; étiquette posée **sur le bord haut, à gauche** (comme une légende de `fieldset`), 20 px, fond de la couleur pleine, texte blanc ou noir selon le contraste : `DIV 1 · dv01`, `GREYCELL · Pression sur Hx…`. L'incident et le scénario : au clic sur l'étiquette (fenêtre de détail), faute de place.
- **Commentaire** : bordure 1 px + étiquette 16 px. **Repost** : cadre à la couleur de l'acte, étiquette « original » au clic.
- **+** zéro hauteur ajoutée, regroupement par couleur très visible de loin.
- **−** **touche à l'habillage** (bordures, séparateurs et état focus/sélection de X et Instagram), donc casse l'illusion pendant une démonstration ; **40 cadres colorés saturent le fil** et plus rien ne ressort (règle 5, Von Restorff REF-06) ; la couleur devient le porteur principal (règle 10 fragile) ; les liens demandent un clic de plus ; le coin droit est pris par le menu ⋯.

### C. Pastille discrète + détail au clic

- **Anatomie** : une pastille de **20 px** de haut dans l'en-tête, après l'heure : point de couleur 8 px + nom court du groupe (`DIV 1`, `GREYCELL`), 11 px. Au clic : **fenêtre de détail** (popover) avec Type, Groupe ou cellule, Compte réel, Scénario ↗, Incident ↗, Heure de création ; fermeture au clic extérieur et à Échap, retour du focus sur la pastille (règle 11, REF-19).
- **Commentaire** : même pastille, en fin d'en-tête. **Repost** : pastille dans le `boost-header` pour l'acte, celle du post repris dans son en-tête.
- **+** quasi invisible, fil inchangé, très peu de risque de casser l'illusion.
- **−** l'en-tête, déjà plein, **passe sur deux lignes** en largeur étroite ; on ne voit ni le compte réel ni l'incident sans cliquer (une action de plus par post, Doherty/Fitts REF-06) ; un point de 8 px se lit mal pour balayer le fil par couleur.

### Comparaison

| Critère | A | B | C |
|---|---|---|---|
| Lisible sans clic (compte, scénario, incident) | ✅ | ⚠ groupe seul | ❌ groupe seul |
| Illusion de l'habillage préservée | ✅ hors de la carte | ❌ bordure touchée | ✅ |
| Fil saturé avec 40 posts | ⚠ +24 px/post | ❌ | ✅ |
| Même signe que MELMIL (trait) | ✅ | ❌ | ❌ |
| Couleur non seule porteuse | ✅ mot de type + noms | ⚠ | ✅ |

## 4. Recommandation : **variante A**

Elle seule fait le travail demandé **sans clic** (compte réel, scénario, incident visibles et cliquables), sans toucher à la carte habillée, avec le **même signe que MELMIL** (règle 36, vocabulaire et signes contrôlés ; avis n°43). Le coût en hauteur est accepté parce que l'interrupteur permet de revenir au fil nu à tout moment. On reprend de C la **fenêtre de détail** au clic sur le segment « original » d'un repost et sur le repère compact d'un commentaire.

## 5. Interrupteur, mémorisation, légende, filtre

- **Où** : dans la **barre de l'app Social réservée à l'animation** (à côté du sélecteur « Au nom de »), pas dans un menu : c'est un geste fréquent (règle 32). Un vrai `role="switch"` avec un libellé fixe : **« Origine des publications »**, état écrit à côté : **« Affichée » / « Masquée »** (règle 10 ; Nielsen 1, état visible, REF-14).
- **Quand le repère est affiché**, un rappel discret en haut du fil : **« Origine affichée — visible par l'animation seulement »** : utile avant une capture d'écran ou un partage d'écran devant des joueurs (et pour les captures des PPT d'exercice).
- **Mémorisation** : **par poste** (stockage local), comme « Mise en forme | HTML » (avis n°68) et l'affichage de MELMIL. **Par défaut : masquée** sur un poste neuf (le risque de fuite à l'écran prime sur le confort, Q5).
- **Vue « comme un joueur »** : quand un animateur prévisualise en tant que joueur, le repère **disparaît**, interrupteur compris (un aperçu doit être fidèle, jamais enrichi : doctrine de l'avis n°62).
- **Légende** : pas de légende séparée posée sur le fil (leçon de l'avis n°43 : ne pas répéter des noms déjà écrits). Le nom du groupe est **écrit dans chaque ligne** ; une flèche **▾** à droite de l'interrupteur ouvre une petite liste « Couleurs des groupes » (trait coloré + nom + type Joueurs / Cellule), qui se ferme au clic extérieur et à Échap.
- **Filtre « n'afficher que… »** : **pas utile en v1**. Le cockpit fait déjà le tri par cellule et par utilisateur (Reporting, avis n°74 et n°75) : un second chemin vers la même réponse (règle 33). Et un fil filtré ne montre plus ce que voient les joueurs. Si le besoin revient à l'usage, préférer **« Mettre en évidence : [groupe ▾] »** (les autres posts atténués, rien de masqué).
- **Accessibilité** : la ligne est un vrai texte (lu par le lecteur d'écran : « Origine : Scénario, GREYCELL, Pression sur Hxxx, incident 07.01.I03 ») ; liens et interrupteur atteignables au clavier avec anneau de focus (règle 11) ; aucune animation à l'apparition (règle 14).

## 6. Questions à trancher par l'utilisateur

1. **Source des couleurs** : couleur du groupe eho (`Group.color`) pour tous, ou palette MELMIL pour les cellules ? Il faudrait **une seule source** (PLÉIADE), pour que GREYCELL ait la même couleur dans MELMIL, dans le cockpit et dans Social.
2. **DIV 1 en bleu** : on le garde (proche du bleu de X et Facebook) ou on prend une teinte de la palette fermée ?
3. **Joueur dans plusieurs groupes** : lequel afficher (celui qui ouvre l'avatar utilisé, cf. « Avatars autorisés », avis n°62, paraît le plus juste) ?
4. **Liens** : nouvel onglet (recommandé) ou même onglet ? MELMIL a-t-il un lien direct vers la fiche d'un incident et vers une storyline (à vérifier par PLEIADE) ?
5. **Par défaut** : masquée (recommandé) ou affichée ?
6. **Compte réel des animateurs** (anim03) : affiché comme celui des joueurs ?
7. **Réactions simulées** : marquées seulement dans les listes Favoris / Partages (recommandé), ou aussi un compteur « dont n simulés » sous le post ?
8. **Préalables techniques** (hors design) : stocker l'origine sur chaque post, commentaire et repost (PLEIADE / MASTORION) ; ne la servir qu'à l'animation et à l'administration (**CYBERSECU**).

## 7. Suite proposée

Maquette des 3 variantes en localhost, sur un faux fil de ~30 posts mêlant les 7 origines du tableau §3, dans les 3 habillages, avec l'interrupteur. Contrôle à 1440 et 390 px, en clair et en sombre.

Sources : règles 5, 10, 11, 12, 14, 20, 21, 22, 32, 33, 36 de la doctrine ; REF-06 (Jakob, Von Restorff, Fitts, Doherty), REF-08, REF-13 (1.4.3, 1.4.11, 2.5.8), REF-14 (Nielsen 1, 4), REF-15, REF-19 ; avis n°43, n°62, n°68, n°74-75, n°82.
