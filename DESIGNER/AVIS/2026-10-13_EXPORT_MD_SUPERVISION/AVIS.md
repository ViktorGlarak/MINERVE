# Avis DESIGNER n°106 — 2026-10-13 — Console d'animation, Supervision : télécharger en .md les contenus de sa cellule

> **Écran lu** (lecture seule, `app-admin`) : `components\Monitoring.tsx` (en-tête `PageHeader` + `AideEcran`, 4 `pa-stat`, panneau « Journal » à bascules `pl-bascule`), `Shell.tsx` (`PageHeader` a une prop `action`, `Panel`), `dialogs\Modal.tsx`, `IncidentPicker.tsx`. Aucun code modifié.
> **Arbitrages de l'utilisateur (déjà pris)** : périmètre = ce que la cellule a publié (scénarios ET direct de ses animateurs) + réactions des autres comptes (commentaires, citations) ; cellule de l'animateur seulement, déduite du compte ; niveau Event > Storyline > Incident ou Scénario, un niveau inclut le dessous, « tout » possible ; types publications, commentaires, citations, articles, hashtags (contenus de la zone qui reprennent les hashtags lancés), « tout » possible ; fichier rangé Event > Storyline > Incident, chronologique, réactions sous le contenu visé.
> Avis rendu comme **proposition** (§1 de la mémoire) : mise en œuvre → PLEIADE ; périmètre, mention de diffusion → CYBERSECU.

## 1. Placement
- **Dans l'en-tête de page** (prop `action` de `PageHeader`, la place de « + Nouveau scénario » ailleurs), à droite du titre : bouton **secondaire** `pl-btn` + icône `download`, libellé **« Télécharger les contenus (.md)… »**. Les points de suspension annoncent une fenêtre (Jakob, REF-06).
- **Pas dans le panneau « Journal »** : le journal montre des gestes techniques (parti, non parti, tic). L'export porte sur des **contenus** ; les mêler ferait croire qu'on télécharge le journal.
- Compte sans cellule : bouton désactivé, raison au survol et au focus (« Votre compte n'est rattaché à aucune cellule : demandez-le à l'Administration »).

## 2. La fenêtre : un formulaire unique, 4 blocs, lu de haut en bas
Pas d'étapes : 4 choix courts, tous visibles, l'aperçu suit (Hick : l'option recommandée pré-choisie).
1. **Cellule** — en lecture, pas un choix : « GREYCELL (déduite de votre compte) ».
2. **Périmètre** — segmenté « Arborescence MELMIL · Scénarios ».
   - Arborescence : arbre Event › Storyline › Incident **avec recherche** (codes et titres, comme l'avis n°27), **un seul choix** (radio par nœud) ; le nœud choisi montre ce qu'il inclut (« inclut 3 storylines, 11 incidents ») et ses descendants sont teintés. Racine **« Tout ce que GREYCELL a publié »**, pré-choisie. Deux branches en fin d'arbre : « Non classés » (scénario sans incident) et « En direct, hors incident ».
   - Scénarios : liste rangée comme la page Scénarios (n°27), avec recherche.
   - Chaque nœud porte son effectif ; un nœud à 0 reste visible, atténué (on ne fait pas disparaître de repères).
3. **Types** — cases, avec une case « Tout » maîtresse (état mixte). Ordre : Publications · Articles de presse · Commentaires · Citations · Reprises de hashtags. Sous cette dernière, une phrase : « Tout contenu de la zone, quel que soit son auteur, qui reprend un hashtag lancé par les contenus choisis (7 hashtags : #PontDeVrena, … ) ».
4. **Période (facultatif)** — « Toute la durée » par défaut ; sinon du / au, en heure de zone.

**Aperçu chiffré**, sous les blocs, recalculé à chaque choix (≤ 400 ms, `aria-live="polite"`) : « **214 contenus** (162 publications, 52 articles) · **38 réactions** · **41 reprises** de 7 hashtags — environ 180 Ko ». Puis le **nom du fichier** en mono, modifiable : `DELATTRE26_GREYCELL_SL02-Ponts_20261013-1432.md` (zone, cellule, périmètre, date-heure ; ASCII, sans espace).
Pied : **« Télécharger 214 contenus »** (action principale, le verbe dit l'effet) · Annuler. Fenêtre `Modal` existante : Échap, piège du focus, retour au bouton.

## 3. États
- **Rien à exporter** : bouton principal inactif, la phrase dit quoi faire : « GREYCELL n'a rien publié dans ce périmètre. Élargissez à l'Event ou retirez la période. »
- **Export long** (> 2 s) : le bouton devient « Préparation… 120 / 214 », Annuler reste actif ; à la fin, bandeau « Fichier téléchargé : 214 contenus, 38 réactions » (Peak-End).
- **Erreur** : bandeau dans la fenêtre, qui reçoit le focus, ce qui s'est passé + comment corriger ; les choix sont conservés (GOV.UK, REF-10).
- **App injoignable** (social, presse) : jamais d'export partiel silencieux. « La presse ne répond pas : les 52 articles ne seront pas dans le fichier. » → « Télécharger sans la presse » ou « Réessayer » ; le fichier porte alors la mention « INCOMPLET : presse absente » en en-tête.

## 4. Le fichier
- **Bandeau de diffusion en première ET en dernière ligne** : « EXERCICE DELATTRE 26 — contenus fictifs, usage exercice » (libellé exact à fixer par l'utilisateur / CYBERSECU).
- **En-tête** en liste : zone, cellule, périmètre (chemin complet), types, période, fuseau, date d'export, auteur de l'export, totaux, état complet / incomplet, rappel « les liens ne s'ouvrent que depuis la zone (VPN) ».
- **Titres** : `#` document · `##` Event · `###` Storyline · `####` Incident (code + titre MELMIL) · contenus en blocs. « Reprises de hashtags » en `#####` à la fin de l'incident où le hashtag est lancé.
- **Un contenu** : ligne de tête `**13/10 14:32** · @compte (Nom affiché) · Social · Publication · scénario SC-0207` (ou « en direct »), texte en citation `>`, une ligne « J'aime · partages · réponses · [ouvrir](url) ». Média : `[image : nom.jpg]`, jamais intégrée.
- **Une réaction** : élément de liste sous le contenu visé, `↳ 14:40 · @compte · Commentaire :` + texte ; une citation est une réaction de type « Citation ».
- Dates **absolues** (jour/mois heure:minute), jamais relatives.

## 5. À éviter
Tableaux Markdown pour du texte long ; HTML ; dates relatives ; identifiants internes ; camp recopié (propriétaire unique : registre / eho) ; export lancé sans aperçu ; nom générique `export.md` ; contenus d'autres cellules ; Chat et messagerie (hors périmètre) ; texte non échappé (`*`, `_`, `>`, `[`… d'un tweet casseraient la mise en forme) ; une case « Réactions » en plus de Commentaires / Citations (doublon).

## 6. Exemple (20 lignes)
```markdown
> **EXERCICE DELATTRE 26 — contenus fictifs, usage exercice**

# Contenus publiés — GREYCELL
- **Zone** : DELATTRE 26 · **Cellule** : GREYCELL (déduite du compte gc05)
- **Périmètre** : EV1 Crise du Vrena › SL02 Les ponts · **Types** : tout
- **Période** : 12/10 08:00 → 13/10 14:00 (heure de zone) · **Exporté le** 13/10/2026 14:32
- **Totaux** : 214 contenus · 38 réactions · 41 reprises de hashtags · complet

## EV1 — Crise du Vrena
### SL02 — Les ponts
#### INC-07 — Sabotage du pont de Vrena
**12/10 09:14** · @MercureToday (Today Mercure) · Presse · Article · scénario SC-0207
> Le pont de Vrena fermé après une explosion nocturne
[ouvrir](https://press.delattre26.zone/articles/pont-vrena)

**12/10 09:20** · @ManFredK (Manfred Kessler) · Social · Publication · en direct
> Qui avait intérêt à couper le Vrena ? #PontDeVrena
J'aime 112 · partages 31 · réponses 2 · [ouvrir](https://social.delattre26.zone/@ManFredK/88)
- ↳ **12/10 09:31** · @EastWatch_Intl · Commentaire : « Sources ? »
- ↳ **12/10 09:47** · @lina_b · Citation : « Encore la désinformation habituelle. »
```

## 7. Remontées
- **PLEIADE** : export calculé **côté serveur** (cellule tirée de la session, jamais d'un paramètre), route d'aperçu (comptes seuls) distincte du téléchargement, rattachement d'une publication en direct à un incident (sinon branche « hors incident »), calcul des hashtags lancés.
- **CYBERSECU** : libellé de diffusion, journalisation de l'export (qui, quand, périmètre), plafond de taille.
- **Doctrine** : un export montre ce qu'il contiendra avant d'être lancé, et un fichier incomplet le dit dans sa première ligne.
