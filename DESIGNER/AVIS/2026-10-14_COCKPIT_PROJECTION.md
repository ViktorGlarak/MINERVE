# Avis DESIGNER n°108 — 2026-10-14 — app-cockpit : la « Projection grand écran »

> **Écran lu** (lecture seule) : `app-cockpit\src\components\situation\ProjectionView.tsx`, `app\projection\page.tsx`, jetons de `app\pleiade-theme.css` et `app\globals.css`, `NouvelleCategorie.tsx` (choix de la couleur d'une catégorie). Captures 1920 × 1080 sur données de démonstration factices : vue réelle, page entière, survol d'une carte.
> **Contexte** : la page a été codée sans avis séparé (suite de l'avis n°105, §8.4 : « A conservé en Projection grand écran »). Elle s'affiche sur un grand écran vu par toute la salle d'animation, lu de **4 à 8 m**. Derniers ajouts demandés par l'utilisateur et contrôlés ici : le repère de l'app d'origine (icône du catalogue + nom de l'instance dans un cadre bleu ciel `#38bdf8` pour le réseau social, jaune `#f5b942` pour la presse), la bande verticale des catégories de suivi avec les étiquettes nommées, la ligne « ↳ Commentaire en réponse à… » ou « Mise à jour du direct de… ».
> **Contraintes acquises, non discutées** : CYBERSECU K10 (public et agrégats seulement ; Chat et messagerie en nombre seul, sans texte ni interlocuteur) ; « Retirer de la projection » discret, visible au survol.
> Ce sont des **propositions** : le besoin de l'utilisateur, les choix de PLEIADE et d'ARCHITECTE et les règles CYBERSECU priment.

---

## Verdict : ✅ VALIDÉ AVEC RÉSERVES

**Ce qui est juste et à garder** : la structure (fil à gauche, agrégats à droite, horloge) ; le respect complet de K10 (nombres seuls pour le privé, avec la phrase « ni contenu, ni interlocuteur » qui rassure la salle) ; les contrastes, tous conformes WCAG (texte méta `#9aa0b4` sur la carte `#1b1c1f` à 6,5:1 ; cadre bleu ciel 8,0:1 ; cadre jaune 9,7:1 ; étiquettes blanches sur fond teinté 12,7 à 13,1:1) ; la catégorie portée **par la couleur et par son nom** (règle 10) ; la ligne de réponse placée **avant** le texte (ordre de lecture) ; le bouton Retirer qui apparaît aussi au focus clavier ; les états « Chargement… » et « Aucun contenu public depuis 6 heures ».

**Ce qui empêche de valider sans réserve** : la page **défile** alors que personne ne la fait défiler (5 cartes visibles et une 6ᵉ coupée en deux à 1920 × 1080, 12 cartes sur 1 960 px) ; les tailles sont pensées pour un écran de bureau, pas pour le fond d'une salle ; une perte de liaison laisse le fil affiché comme s'il était en direct ; la presse ne se distingue du réseau social que par la couleur et une petite icône.

### Le calcul de lisibilité utilisé

Hypothèse : écran de **2 m de large** en 1920 px (1 px ≈ 1,04 mm), hauteur des capitales ≈ 0,7 × la taille de police (Archivo).

| Taille | À 4 m | À 6 m | À 8 m |
|---|---|---|---|
| 13 px (titres de section, mention privée) | 8' | 5' | 4' |
| 17 px (heure, @compte, ligne de réponse) | 11' | 7' | 5' |
| 24 px (texte des contenus) | 15' | 10' | 7,5' |
| 30 px | 19' | 12,5' | 9' |
| 40 px (chiffres des catégories) | 25' | 17' | 12,5' |

Repère ergonomique courant : **16 minutes d'arc** au minimum pour lire un caractère, 20 à 22 de confort. *Ce repère vient des normes d'affichage (ISO 9241-303, AVIXA) que je n'ai pas encore ingérées : c'est un avis chiffré, pas une règle sourcée ; à ingérer.* Conséquence honnête : **un fil de textes n'est pas lisible à 8 m** sur un écran de 2 m en 1080p, quelle que soit la mise en page. Il faut donc concevoir pour **deux distances** : le **coup d'œil depuis le fond** (quoi, d'où, combien, quelle catégorie : nom, cadre d'origine, bande, chiffres, horloge) et la **lecture du texte depuis la moitié avant de la salle**. Même calcul que l'avis n°107 (diaporama : 24 pt au moins).

---

## Recommandations (classées par gain pour la salle)

### 1. Une page qui tient dans l'écran, sans jamais une demi-carte — **obligatoire avant mise en ligne**
- **Constat** : racine en `min-h-screen`, liste sans hauteur bornée : la page défile et la carte du bas est coupée (capture 1920 × 1080 : la 6ᵉ carte « Rédaction » n'a que son nom visible). Une projection n'a ni souris ni molette : ce qui dépasse n'existe pas, et une carte coupée fait croire à un défaut.
- **Recommandation** :
  - racine `h-screen overflow-hidden` au lieu de `min-h-screen` ; `main` en `min-h-0` (déjà) ; la `<ul>` du fil en `flex-1 min-h-0 overflow-hidden` ;
  - n'afficher que les cartes **entières** : mesurer la hauteur disponible (`ResizeObserver` sur la liste) et ne rendre que les cartes qui tiennent, ou masquer celles dont le bas dépasse ; jamais de dégradé qui coupe un texte ;
  - sous la dernière carte, une ligne `text-[18px] text-ink-muted` : « + 7 contenus plus anciens dans la Situation du Cockpit » ;
  - **objectif : 5 cartes entières en 1920 × 1080** (voir n°2 et n°4 pour y arriver) ;
  - vérifier que la pastille « N » de Next.js (mode développement, coin bas gauche) n'existe pas en production (`devIndicators: false` au besoin).
- **Source** : Nielsen 8 (esthétique et minimalisme, REF-14) ; règle 38 (flux) ; avis n°105 §8.4 (« la projection n'a aucune commande »).

### 2. Une échelle de tailles pour la salle — **obligatoire avant mise en ligne**
- **Constat** : plusieurs textes destinés à la salle sont entre 13 et 17 px (5' à 7' d'arc à 6 m) : titres de section (13 px, capitales espacées), heure et @compte (17 px), ligne de réponse (17 px, italique gris), sous-ligne des catégories (14 px), mention privée (13 px), badge média (13 px). Le texte principal (24 px) est lisible jusqu'à ~4 m seulement.
- **Recommandation** (plancher de 18 px pour tout ce que la salle lit ; le pied de page reste à l'opérateur) :

| Élément | Aujourd'hui | Proposé |
|---|---|---|
| Texte du contenu | 24 px, `line-clamp-4` | **30 px**, `leading-[1.3]`, **`line-clamp-2`** (le texte entier reste dans la Situation) |
| Nom de l'auteur | 22 px | **26 px** semibold |
| @compte | 17 px | **20 px** ; masqué s'il répète le nom (« Rédaction @Rédaction ») et pour la presse (pas de @ dans un journal) |
| Cadre d'origine | 16 px, h 36 | **20 px**, h 40, icône 28 px |
| Heure | 17 px | **22 px** `font-mono` `text-ink-soft` |
| Ligne de réponse | 17 px | **22 px** (voir n°5) |
| Étiquettes de catégorie | 15 px, h 28 | **18 px**, h 32 |
| Titres de section (fil et colonne) | 13 px | **18 px**, `tracking-[0.16em]` |
| Sous-ligne « réseau social 3 · presse 1 » | 14 px | **18 px** |
| « Nombre de messages seulement… » | 13 px | **16 px** |
| Badge média (« IMAGE ») | 13 px | **16 px** |
| Horloge, chiffres des catégories et du privé | 30 / 40 px | inchangés (bons) |

- **Source** : calcul ci-dessus (avis chiffré, repère ISO 9241-303 / AVIXA à ingérer) ; règle 26 (le texte courant des outils est à 14-16 px **pour un poste à 60 cm**, pas pour une salle) ; REF-17 (taille d'abord, le reste ensuite) ; avis n°107.

### 3. Dire à la salle quand l'écran n'est plus en direct — **obligatoire avant mise en ligne**
- **Constat** : en cas d'erreur, seul un « ✕ Cockpit injoignable » rouge de 16 px apparaît dans l'en-tête ; le fil et les chiffres restent affichés tels quels. Depuis la salle, un écran figé depuis dix minutes ressemble exactement à un écran calme. Même chose pour un canal injoignable : ses chiffres valent 0 au lieu de « inconnu », et le libellé affiche la clé technique (« presse », « social ») au lieu du nom.
- **Recommandation** :
  - garder l'heure du dernier chargement réussi ; au-delà de **2 cycles manqués (40 s)**, remplacer « ● En direct » par un bandeau pleine largeur sous l'en-tête, `h-[56px] text-[24px]`, `bg-halt-on text-halt` : « ✕ Liaison perdue depuis 11:32 · données de 11:31 » ; le fil et la colonne passent en `opacity-50` ;
  - à côté de « En direct », la fraîcheur : « En direct · relu à 11:35:20 » (ou « il y a 8 s ») en `text-[16px] text-ink-muted` ;
  - canal injoignable : `LIBELLE_CANAL[k]` au lieu de la clé ; dans les cartes de catégories, « presse — » au lieu de « presse 0 » tant que la presse ne répond pas ;
  - erreur au tout premier chargement (pas encore de données) : message centré `text-[28px]`, « Le Cockpit ne répond pas. Nouvel essai toutes les 20 s. », au lieu de la page vide avec l'erreur dans le coin.
- **Source** : Nielsen 1 (visibilité de l'état du système, REF-14) ; règle 25 ; avis n°105 C2/règles communes (« un canal injoignable le dit au lieu de montrer zéro »).

### 4. Moins de couleurs concurrentes : la couleur à la bande, les mots aux étiquettes — **souhaitable** (gain de hiérarchie et de place)
- **Constat** : une carte porte jusqu'à **cinq marques colorées** : la bande (catégorie), le cadre coloré (canal), le mot « Commentaire » coloré (canal encore), les étiquettes teintées (catégorie encore) et la plaque blanche de l'icône, qui est **l'élément le plus lumineux de la carte** et attire l'œil à chaque ligne. Pire, les couleurs se confondent : la catégorie « Frontière » (`#3b82f6`) et le cadre « réseau social » (`#38bdf8`) sont deux bleus à **1,7:1** l'un de l'autre ; « Pont de Nancy » (orange) et le cadre presse (jaune) à **2,0:1**. La couleur d'une catégorie est libre (`<input type="color">`, rouge `#ef4444` par défaut), donc d'autres collisions et des couleurs trop sombres pour la bande sont possibles.
- **Recommandation** :
  - **étiquettes neutres** : fond `bg-sunken`, bord `border border-line-control`, un carré `w-3 h-3` de la couleur de la catégorie, puis le nom en `text-ink` ; la couleur pleine reste réservée à la bande (qui est la lecture à distance), le nom à l'étiquette (lecture de près) ;
  - les étiquettes **montent dans la ligne d'en-tête**, alignées à droite avant l'heure (elles passent dessous seulement si elles ne tiennent pas) : environ 45 px gagnés par carte, ce qui donne la 5ᵉ carte de la recommandation n°1 ;
  - « Commentaire » / « Mise à jour du direct » en `text-ink-soft` semibold, **sans** la couleur du canal (n°5) ;
  - plaque de l'icône : retirer `bg-white` si les icônes du catalogue ont un fond transparent ; sinon une plaque `bg-ink-soft` ou un fond de la couleur du canal à 20 % ;
  - **palette fermée de catégories** (dans `NouvelleCategorie.tsx`, hors de cette page → PLEIADE) : 6 teintes claires à au moins 3:1 sur `#1b1c1f`, **sans bleu ciel ni jaune-orangé** (réservés aux canaux), sans le rouge `--color-halt` (réservé à l'alerte) et sans gris (réservé à « aucune catégorie »), par exemple vert `#4ade80`, violet `#a78bfa`, rose `#f472b6`, indigo `#818cf8`, lime `#a3e635`, sarcelle `#2dd4bf` (à contrôler à côté du bleu ciel sur le vrai projecteur) ; défaut = vert, pas rouge.
- **Source** : REF-07 (mettre en valeur en atténuant le reste ; la couleur n'est qu'un moyen parmi d'autres) ; règle 20 (Von Restorff : une marque saillante doit être rare) ; règle 22 (une échelle à usages fixés : personne ne choisit plus une nuance) ; règle 21 (3:1 pour un élément graphique porteur de sens).

### 5. Distinguer presse et réseau social sans compter sur la couleur, et rendre la réponse lisible d'un coup d'œil — **obligatoire avant mise en ligne pour le mot du canal, souhaitable pour le reste**
- **Constat** : bleu ciel et jaune restent distincts pour la plupart des daltonismes (axe bleu-jaune préservé chez les protanopes et deutéranopes), mais pas pour les tritanopes, ni sur un vidéoprojecteur délavé ; l'icône de 28 px ne se lit pas à 6 m ; le nom de l'instance ne dit pas toujours son type (« Today Mercure » peut être un compte du réseau). Sur la ligne de réponse, l'extrait est en **italique gris de 17 px** : c'est la partie la moins lisible de la carte, alors qu'elle porte le contexte. Pour la presse, « Mise à jour du direct **de Rédaction** » répète l'auteur.
- **Recommandation** :
  - dans le cadre, **le type en mot avant le nom** : `[icône] PRESSE · Today Mercure (essai)` et `[icône] RÉSEAU · Réseau social essai` (type en capitales `text-[16px] tracking-[0.12em]`, nom en `text-[20px]`) — obligatoire ;
  - ligne de réponse reformulée et dessinée comme une citation, sur **une seule ligne** : `↳ Répond à Olga Sanz · « Les autorités de Mercure annoncent… »`, en `text-[22px]`, `text-ink-soft`, extrait **non italique** (les guillemets suffisent) et tronqué, avec un filet `border-l-2 border-line-strong pl-3` qui le rattache au texte en dessous ; pour la presse : `↳ Mise à jour du direct · « Pont de Nancy : la circulation coupée »`, sans « de Rédaction » ;
  - presse : afficher la **première ligne de l'article en semibold** (titre) puis la suite, et l'auteur sans @.
- **Source** : règle 10 (jamais l'information par la couleur seule, REF-07) ; Jakob (règle 15 : la réponse se présente comme dans les réseaux sociaux connus, avec un filet de rattachement) ; REF-17 (l'italique pour une courte emphase, pas pour un texte à lire de loin) ; règle 7.

### 6. Garder le bouton Retirer invisible pour la salle — **souhaitable**
- **Constat** : le bouton n'apparaît qu'au survol, mais sur un écran projeté le pointeur reste souvent posé au milieu de l'écran : le bouton (et le curseur) restent alors visibles de toute la salle. Après un retrait, aucune confirmation ni annulation à portée : il faut aller chercher « Retirés de la projection » dans le pied de page en 12 px. Pas d'anneau de focus défini sur le bouton.
- **Recommandation** :
  - masquer le pointeur après **3 s sans mouvement** (`cursor-none` sur la racine) et n'afficher le bouton au survol que si la souris a bougé dans les 3 dernières secondes ; il reste visible au focus clavier ;
  - après un retrait : un message en bas à droite, 10 s, `text-[14px]` : « Retiré de la projection pour toute la zone · **Annuler** » (rétablit le contenu) ;
  - `focus-visible:outline-2 focus-visible:outline-craie focus-visible:outline-offset-2` sur le bouton ; pied de page en `text-ink-muted` (le `text-ink-faint` actuel fait 3,5:1, sous les 4,5:1 exigés à 12 px) et bouton du pied à 24 px de haut au moins.
- **Source** : Nielsen 3 (contrôle et liberté : annuler sans chercher) et Nielsen 1 ; règle 12 (cibles de 24 px, WCAG 2.5.8) ; règle 21 et REF-13 (4,5:1, focus visible 2.4.7).

### 7. Montrer à la salle ce qui vient d'arriver — **souhaitable** ⚠ *remplacé par l'addendum « animation d'arrivée » en fin d'avis*
- **Constat** : le fil se recharge toutes les 20 s sans pause ; une nouvelle carte pousse les autres vers le bas sans signal. La salle ne sait pas si la carte du haut vient d'arriver ou date d'il y a 30 min, sauf à comparer l'heure de la carte et l'horloge.
- **Recommandation** : marquer pendant **2 minutes** les contenus arrivés depuis le chargement précédent : le mot « NOUVEAU » en `text-[16px] font-semibold` craie sur `bg-craie-soft`, dans la ligne d'en-tête, et un fond de carte `bg-craie-soft` qui s'efface au chargement suivant. Pas d'animation de glissement (respect de « réduire les animations ») ; si animation, un fondu d'opacité de 200 ms seulement.
- **Source** : avis n°105 C2 (ce qui a changé avant le stock) ; règle 14 (animer `opacity`, 150-250 ms, respecter `prefers-reduced-motion`) ; règle 10 (un mot, pas seulement une teinte).

### 8. Tenir les textes longs et les noms longs — **souhaitable**
- **Constat** : la ligne d'en-tête est en `flex-wrap` avec l'heure en `ml-auto` : un nom long, un @compte long et un nom d'instance long renvoient le cadre et l'heure à la ligne, et l'heure se retrouve à gauche sous le nom. Un nom de catégorie long n'est pas borné.
- **Recommandation** : sortir l'heure du `flex-wrap` (colonne fixe à droite, `shrink-0`) ; nom en `truncate max-w-[40%]`, @compte en `truncate`, nom d'instance en `truncate max-w-[360px]` ; étiquettes de catégorie `max-w-[260px] truncate` et au plus **3**, puis « +2 » ; le texte reste en `line-clamp-2` (n°2) avec `break-words` (déjà là). Tester avec un jeu de démonstration « pire cas » : 12 contenus, noms de 40 caractères, texte de 500 caractères, 4 catégories sur un contenu.
- **Source** : REF-07 (concevoir avec des données réalistes, pas idéales) ; règle 9 (proximité : l'heure appartient à la carte, pas au nom).

### Plus tard
- **Variation des catégories** : à côté du chiffre de la dernière heure, `▲ +3` ou `▼ −2` par rapport à l'heure précédente, en mots et en flèche (avis n°105 : des variations, pas des stocks).
- **Mode « lisible à 8 m »** (bascule au clavier, touche `G`) : texte à 40 px, 3 cartes, colonne de droite réduite aux chiffres, pour les salles profondes.
- **Valider sur le vrai écran de salle** avec 3 animateurs placés au fond : « que se passe-t-il ? », « d'où vient ce contenu ? », « est-ce que c'est en direct ? » (règle 40).

---

## Conformité K10 vérifiée
Aucune des recommandations n'ajoute de contenu privé : le Chat et la messagerie restent en nombre seul, la ligne de réponse ne cite que des contenus publics (publication du réseau, direct de presse), la liste des retraits reste à l'opérateur. Le bandeau de perte de liaison et le marqueur « Nouveau » ne portent que de l'état.

⭐ **Doctrine dégagée** : *un écran de salle se conçoit pour deux distances (le coup d'œil depuis le fond, la lecture depuis l'avant), il tient dans l'écran sans défilement, et il dit lui-même quand il n'est plus en direct ; la couleur pleine y est réservée à une seule dimension par élément.*

---

## Addendum — animation d'arrivée (2026-10-14, demande de l'utilisateur)

> **Demande** : remplacer l'étiquette « NOUVEAU » (réduite à 0,7 s, jugée ridicule) par « une jolie animation qui fasse glisser les cadres des messages vers le bas ». Code relu après application de l'avis : `ProjectionView.tsx` (page sans défilement, `tiennent` mesuré par `ResizeObserver`, cartes au-delà en `invisible`, `nouveaux` repérés à chaque relecture).
> **Je révise le §7** (« pas de glissement ; au plus un fondu de 200 ms ») : il visait un mouvement décoratif. Ici le glissement **explique** quelque chose (les nouveaux contenus entrent par le haut, les anciens descendent et sortent par le bas) : c'est exactement l'usage légitime d'une animation selon REF-09. Il remplace l'étiquette, et le repère reste visible depuis le fond, ce que 0,7 s d'étiquette ne permettait pas.
> ⚠ **Écart assumé** à la règle 14 (150-250 ms) : elle vaut pour une interface qui **répond à un geste**. Sur un écran d'ambiance, sans geste, vu à 6-8 m, un mouvement de 200 ms passe inaperçu ou ressemble à un saut. Je propose 500-700 ms, toujours très court devant le cycle de 20 s. *Avis, pas règle sourcée.*

### Chorégraphie (un lot = tout ce qu'une relecture apporte)

| Temps | Ce qui bouge | Comment |
|---|---|---|
| 0 ms | **Les cartes déjà là glissent vers le bas d'un seul bloc**, de la hauteur exacte du lot | FLIP : `translateY(ancienne − nouvelle position) → 0`, **700 ms**, `cubic-bezier(0.22, 1, 0.36, 1)` (départ franc, arrivée très douce, **sans rebond**). Toutes ensemble, même durée : la colonne se lit comme un tout qui descend |
| 0-700 ms | **Les cartes du bas sortent** sous le bord de la colonne | Rien de spécial : elles glissent avec le bloc et sont rognées par l'`overflow-hidden` de la `<ul>`. On ne les passe en `invisible` (et on ne met à jour « + n contenus plus anciens ») **qu'à la fin** du glissement |
| 150 ms + décalage | **Les nouvelles cartes apparaissent dans l'espace libéré** | `opacity 0 → 1` + `translateY(-20px → 0)`, **500 ms**, même courbe. Ordre : **du bas du lot vers le haut** (le plus ancien du lot d'abord, le plus récent en dernier, en tête) ; décalage **90 ms** entre cartes, **plafonné à 270 ms au total** (au-delà de 4 cartes : 270 / (n − 1)) |
| 300 ms → ~3,3 s | **Repère d'arrivée qui dure** | Liseré **craie** de 2 px sur le pourtour de la nouvelle carte (`<span data-lisere className="absolute inset-0 border-2 border-craie pointer-events-none opacity-0" aria-hidden />`), animé en opacité seule : 0 → 0,9 en 300 ms, tenu ~1 s, **estompé en ~2 s**. Pas de fond coloré, pas la couleur d'une catégorie (la bande reste la seule couleur pleine, recommandation n°4) |

Le liseré remplace l'étiquette : visible depuis le fond, éteint bien avant la relecture suivante, donc jamais « tout est nouveau » même quand ça poste beaucoup.

### Gros lot : fondu plutôt que glissement
Si le lot visible compte **au moins la moitié des cartes qui tiennent** (3 sur 5), le glissement traverserait tout l'écran en 700 ms : un balayage brutal, pas une explication. Dans ce cas :
1. la colonne s'estompe (`opacity 1 → 0`, **200 ms**) **avant** d'afficher les nouvelles données (le nombre d'arrivées est connu dans `charger`, avant `setD`) ;
2. les nouvelles cartes apparaissent en fondu + 20 px, décalage plafonné à 270 ms ;
3. liseré sur la seule carte de tête (sinon tout l'écran s'allume).

### « Réduire les animations » (`prefers-reduced-motion: reduce`)
- **Aucun déplacement** : les cartes existantes prennent leur nouvelle place sans glisser ; les nouvelles apparaissent en **fondu seul** de 300 ms.
- **Le liseré est gardé** (opacité seule, aucun mouvement) : c'est lui qui porte « arrivé à l'instant ».
- Test `matchMedia("(prefers-reduced-motion: reduce)").matches` relu à chaque lot.

### Mise en œuvre sans dépendance (Web Animations API, ~40 lignes)
```tsx
// Chaque <li> porte data-cle={cle(c)}. Positions mémorisées après chaque rendu.
const positions = useRef(new Map<string, number>());
const premierRendu = useRef(true);
useLayoutEffect(() => {
  const ul = liste.current; if (!ul) return;
  const reduit = matchMedia("(prefers-reduced-motion: reduce)").matches;
  const lis = [...ul.querySelectorAll<HTMLElement>(":scope > li[data-cle]")];
  const avant = positions.current, apres = new Map<string, number>();
  lis.forEach((li) => apres.set(li.dataset.cle!, li.offsetTop)); // position de mise en page, hors transform
  if (!premierRendu.current) {
    const EASE = "cubic-bezier(0.22, 1, 0.36, 1)";
    const neufs = lis.filter((li) => !avant.has(li.dataset.cle!));
    if (!reduit) lis.forEach((li) => {                            // 1. poussée FLIP
      const old = avant.get(li.dataset.cle!); if (old == null) return;
      const dy = old - li.offsetTop; if (!dy) return;
      li.animate([{ transform: `translateY(${dy}px)` }, { transform: "none" }], { duration: 700, easing: EASE });
    });
    const pas = neufs.length > 1 ? Math.min(90, 270 / (neufs.length - 1)) : 0;
    [...neufs].reverse().forEach((li, i) => {                     // 2. entrée, du bas du lot vers le haut
      li.animate(reduit ? [{ opacity: 0 }, { opacity: 1 }]
        : [{ opacity: 0, transform: "translateY(-20px)" }, { opacity: 1, transform: "none" }],
        { duration: reduit ? 300 : 500, delay: reduit ? 0 : 150 + i * pas, easing: EASE, fill: "backwards" });
      li.querySelector<HTMLElement>("[data-lisere]")?.animate(    // 3. liseré qui s'estompe
        [{ opacity: 0 }, { opacity: 0.9, offset: 0.1 }, { opacity: 0.9, offset: 0.4 }, { opacity: 0 }],
        { duration: 3000, delay: 300, easing: "ease-out" });
    });
  }
  premierRendu.current = false; positions.current = apres;
}, [d]);
```
- **Sortie par le bas** : dans `mesurer`, quand des cartes arrivent et que `tiennent` diminue, appliquer la nouvelle valeur **après 700 ms** (`setTimeout`) pour que les cartes sortantes glissent sous le bord au lieu de disparaître d'un coup.
- **Pas d'animation** au premier chargement, au redimensionnement, ni au retour d'un onglet masqué ; le tic de l'horloge (un rendu par seconde) ne déclenche rien puisque l'effet ne dépend que de `d`.
- Un **retrait** (« Retirer de la projection ») profite du même mécanisme : les cartes du dessous remontent en 700 ms au lieu de sauter.
- Retirer `NOUVEAU_MS`, l'état `nouveaux` et l'étiquette.

**Motion (framer-motion) ?** **Non pour cette page.** `layout` + `AnimatePresence` feraient la même chose en moins de lignes, mais pour **un seul écran** la Web Animations API suffit, sans dépendance de plusieurs dizaines de Ko. REF-09 réserve Motion aux transitions de mise en page **répétées dans plusieurs écrans** (exemple : déplacer une carte d'une colonne à l'autre dans la planche MELMIL) : à reconsidérer si ce besoin apparaît ailleurs.

### À éviter
- **Tout mouvement permanent** : défilement automatique, bandeau défilant, carrousel, pulsation, clignotement. Entre deux lots, l'écran est **immobile** : c'est la condition pour qu'on puisse lire.
- **Rebond ou ressort qui dépasse** : ludique, et la carte « tremble » au moment où l'œil veut la lire.
- Animer `height`, `top` ou `margin` : chaque image recalcule la mise en page de toute la colonne (saccades sur un poste de salle modeste). Seulement `transform` et `opacity`.
- Agrandir (`scale`) la nouvelle carte, la faire venir de côté ou flasher son fond : effets plus forts que l'information portée (règle 20).
- Animer la colonne de droite à chaque relecture : les chiffres changent sans bouger (au plus, plus tard, un fondu de 300 ms du nouveau chiffre).
- Dépasser ~1 s au total : une partie de la salle lirait une colonne en mouvement.

**Sources** : REF-09 (une animation explique d'où vient un élément et où il va ; `transform` et `opacity` seulement ; réduire les animations = fondu à la place du déplacement, opacité gardée) ; règle 14 (adaptée, écart assumé ci-dessus) ; règle 20 (Von Restorff) ; Nielsen 1 (le liseré dit « ceci vient d'arriver »).
