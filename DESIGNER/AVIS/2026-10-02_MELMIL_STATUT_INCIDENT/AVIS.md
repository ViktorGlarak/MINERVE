# Avis DESIGNER n°33 — MELMIL : le statut d'un incident en 4 étapes

> **Date** : 2026-10-02 · **App** : `app-melmil` (atelier de préparation) · **Demande** : utilisateur, relayée par NOYAU.
> **Statut de l'avis** : proposition argumentée. Ce qui fait foi : le besoin de l'utilisateur, puis les choix de PLEIADE / ARCHITECTE.
> **Code lu** : `lib/atelier/modele.ts`, `components/atelier/onglets-gt.tsx` (tableau, `Statut`, `FicheIncident`), `components/carte.tsx`, `lib/atelier/versPlanche.ts`, `lib/atelier/ecarts.ts`, `app/globals.css`.
> ⚠ **Déjà fait dans la copie de travail** (non commité, constaté le 2026-10-02) : le type `"preparation" | "validation" | "valide" | "jemm"`, les libellés, `lireStatut()` (migration) et le statut `"jemm"` donné aux incidents créés par l'import ou l'alignement JEMM. Cet avis **s'aligne sur ces libellés** ; il porte sur l'affichage, le geste et les garde-fous.

---

## Le besoin, en une phrase

Voir **d'un coup d'œil** où en est chaque incident (préparation → validation → validé → dans JEMM), et le faire avancer **d'un clic**, sans alourdir une fiche déjà dense (ETIM, comptes rendus, scénarios, médias, pièces jointes).

## Le principe qui guide tout l'avis

**Un seul repère, une seule forme, partout.** Le statut est dit par **trois moyens à la fois** : une **couleur**, une **forme qui se remplit** (la progression) et un **mot**. Jamais la couleur seule : orange, jaune et vert sont exactement les teintes que confondent les daltoniens rouge-vert (WCAG 1.4.1, REF-13 ; Refactoring UI, REF-07). La forme choisie est la **jauge circulaire qui se remplit** (« Harvey ball »), lue partout comme un avancement, et déjà proche de la pastille réseau de LEAC (rond plein / demi-rond, avis du 2026-09-27).

| Étape | Valeur | Libellé exact | Libellé court (stepper < 480 px) | Forme (« pastille de statut ») |
|---|---|---|---|---|
| 1 | `preparation` | **En préparation** | Préparation | cercle rempli **au quart**, orange |
| 2 | `validation` | **En validation** | Validation | cercle rempli **à moitié**, jaune |
| 3 | `valide` | **Validé** | Validé | cercle **plein** vert, **✓** blanc dedans |
| 4 | `jemm` | **Dans JEMM** | JEMM | **pastille allongée** verte, **« J »** dedans |

---

## R1 — Un composant unique `PastilleStatut` (SVG), réutilisé partout

- **Fichier** : nouveau `components/atelier/pastille-statut.tsx` (ou à côté d'`agrafe.tsx`, qui joue le même rôle pour les pièces jointes). Props : `statut`, `taille` (12 px par défaut, 9-10 px sur la planche), `absentDeJemm?` (voir R6).
- SVG `aria-hidden="true"` : le mot est toujours présent à côté, ou dans l'`aria-label` du conteneur (même règle que l'agrafe, avis n°23 R5).
- **Dessin** (viewBox 12 × 12) : cercle r = 5, **trait 1,5 px** de la couleur « trait », intérieur vide = `var(--fond-carte)` ; secteur rempli de la couleur « aplat » (90° pour l'étape 1, 180° pour l'étape 2) ; étape 3 = disque plein + coche blanche (trait 1,6) ; étape 4 = rectangle arrondi **18 × 12**, rayon 6, « J » en **Archivo 800, 9 px**, centré.
- **Pourquoi « J » et pas « JEMM » dans la pastille** : « JEMM » à 9 px dans une pastille fait 26-28 px de large, devient illisible sur la planche (texte à 7,5 px) et casse l'alignement de la colonne. Le **mot** « JEMM » est dit à côté (tableau, fiche) ; la pastille ne porte que l'initiale (REF-07 : « l'étiquette est un dernier recours », la forme parle). Le « J » blanc sur le vert clair fait **5,2 : 1** (WCAG 1.4.3 AA, même à petite taille).

## R2 — Couleurs exactes (calculées, contrastes vérifiés)

Jetons à ajouter dans `app/globals.css`, **paires aplat / trait / texte**, redéfinies sous `:root[data-theme="sombre"]` (REF-01, REF-15). Un seul vert pour « Validé » et « Dans JEMM » : c'est la **forme** (✓ contre « J ») qui les distingue, pas une deuxième nuance de vert (REF-07 : limiter les choix).

| Jeton | Clair | Sombre |
|---|---|---|
| `--statut-prep` (aplat) | `oklch(0.72 0.17 55)` ≈ `#f3821d` | `oklch(0.78 0.15 60)` ≈ `#fc9e47` |
| `--statut-prep-trait` | `oklch(0.55 0.15 50)` ≈ `#b45000` — **5,1 : 1** sur blanc | = aplat (**7,8 : 1** sur `#1d2125`) |
| `--statut-valid` (aplat) | `oklch(0.86 0.17 92)` ≈ `#f9cc21` | `oklch(0.88 0.16 95)` ≈ `#f9d544` |
| `--statut-valid-trait` | `oklch(0.55 0.11 85)` ≈ `#8f6b09` — **4,9 : 1** sur blanc | = aplat (**11,3 : 1**) |
| `--statut-ok` (aplat **et** trait, étapes 3 et 4) | `oklch(0.52 0.13 150)` ≈ `#1d7d3e` — **5,2 : 1** sur blanc | `oklch(0.76 0.15 150)` ≈ `#61cb7c` — **8,0 : 1** |
| `--statut-ok-texte` (✓ et « J ») | `#ffffff` (5,2 : 1 sur le vert) | `#14171a` (8,9 : 1 sur le vert) |
| Texte sur aplat orange / jaune (segment actif du stepper) | `#14171a` — **6,9 : 1** / **11,7 : 1** | `#14171a` — **8,7 : 1** / **12,5 : 1** |

- **Pourquoi un « trait » plus foncé en clair** : un jaune reste jaune seulement très clair (1,5 : 1 sur blanc). C'est le **contour** qui porte le contraste de 3 : 1 exigé pour un élément graphique (WCAG 1.4.11), l'aplat n'est qu'un complément.
- ⚠ Les couleurs `#8a8f98 / #b7791f / #2f855a` de `COULEUR_STATUT` (onglets-gt.tsx l. ~495) disparaissent, ainsi que `.statut::before` (globals.css l. ~788).

## R3 — La FICHE : un stepper de 4 segments dans l'EN-TÊTE, le `<select>` disparaît

**Placement** : dans le bandeau d'en-tête de `FicheIncident` (fond `--espace-prep-fond`), **sur une ligne sous le titre**, pleine largeur. Le `<select>` « Statut » est **retiré** de la section « Quand » (grille `sm:grid-cols-[110px_90px_1fr]` : Code, Jour, Heure).
→ **Bilan pour la densité : un champ de moins dans le corps, une ligne de 28 px dans l'en-tête.** La fiche ne s'alourdit pas, elle se range : le statut qualifie **tout l'incident**, il n'a rien à faire parmi « Quand » ; en tête, il est vu à l'ouverture sans défiler (Nielsen 1 « état du système visible », REF-14 ; proximité, REF-06).

**Forme** : contrôle segmenté de 4 boutons accolés, ordre de gauche à droite = ordre de progression.
- Chaque segment : `PastilleStatut` 12 px + libellé exact (« En préparation », « En validation », « Validé », « Dans JEMM »). Sous 480 px de large : libellés courts (« Préparation », « Validation », « Validé », « JEMM »), libellé complet dans l'`aria-label`.
- **Segment actif** : aplat de sa couleur, texte `#14171a` (blanc sur le vert en clair), **gras**. **Étapes passées** : fond `--fond-carte`, texte normal, pastille pleine (on voit le chemin parcouru). **Étapes à venir** : fond `--fond-carte`, texte `--texte-doux`, pastille à sa forme. Les segments gardent le fond blanc de la carte pour se détacher du bandeau orangé de l'espace « préparation » (sinon l'orange de l'étape 1 se perd dans l'orange de l'espace).
- **Hauteur 28 px**, cibles ≥ 24 × 24 (WCAG 2.5.8, REF-13 ; Fitts, REF-06).
- **Un clic = enregistré**, réponse à l'écran immédiate (Doherty < 400 ms, REF-06). **On peut cliquer n'importe quelle étape, y compris revenir en arrière** : pas de « suivant » imposé, pas de boîte de confirmation (geste réversible : liberté et contrôle, Nielsen 3 ; une confirmation sur un geste réversible n'apprend qu'à cliquer « OK »).
- **Accessibilité** : `role="radiogroup"` + `aria-label="Statut de l'incident"`, chaque segment `role="radio"` + `aria-checked` ; Tab entre sur le segment coché, **flèches** gauche / droite pour changer (WAI-ARIA APG Radio Group, REF-19) ; anneau de focus `--anneau` visible (2.4.7).
- Pourquoi pas le `<select>` : il **cache** les 4 étapes (2 clics, aucune idée de progression), alors que 4 choix visibles d'un coup se lisent sans effort (Hick, REF-06 ; reconnaître plutôt que se souvenir, Nielsen 6).

## R4 — Traçabilité : UNE ligne sous le stepper, pas d'historique

- Sous le stepper, en `text-xs`, `--texte-doux` : **« Validé le 02/10 à 14:32 par gc05 »** (le verbe suit le statut : « En préparation depuis le… », « En validation depuis le… », « Validé le… », « Dans JEMM depuis le… »).
- La `trace` actuelle (`modifiePar` / `modifieLe`) dit qui a touché **n'importe quel champ** : elle ne suffit pas. Ajouter deux champs à l'incident, **`statutPar`** et **`statutLe`**, posés par `modifierIncident` seulement quand `statut` change (relecture : absents → ligne masquée, rien d'inventé).
- Sans rôle chef / rédacteur dans l'app, c'est **cette ligne qui rend la validation responsable** (on voit qui a validé). Pas de liste d'historique : elle chargerait la fiche pour un besoin rare.

## R5 — Le TABLEAU (onglet Incidents) : pastille + mot, colonne triable

- Cellule `col-statut` : `PastilleStatut` 12 px + libellé exact. **Garder le mot** : une pastille seule avec le mot en infobulle obligerait à survoler (impossible au clavier sans travail, invisible au toucher, WCAG 1.4.13) et à mémoriser un code de formes (Nielsen 6). C'est aussi la règle déjà tenue : « statut = mot + couleur » (avis du 2026-09-30 « MELMIL, médias et demandes de produit », R4).
- **Largeur** : `.table-incidents .col-statut { width: 8.75rem; }` (au lieu de 9.5rem) — « En préparation » à 13 px + pastille + écart y tient sans retour à la ligne ; `white-space: nowrap`.
- **Rendre la colonne triable** (`ThTri colonne="statut"`), tri dans l'**ordre de progression** (pas alphabétique) : le chef greycell trie pour voir d'abord les « En validation ».
- Résumé de storyline (`resume-storyline`) : remplacer `PLURIEL_STATUT` par **« 2 en préparation, 1 en validation, 3 validés, 5 dans JEMM »** (singulier : « en préparation », « en validation », « validé », « dans JEMM »).

## R6 — JEMM : MELMIL **propose**, l'humain **décide** ; une incohérence se **signale**

MELMIL sait déjà, par code, si un incident est dans la planche JEMM (`ecarts.ts`). Mais `ecarts.ts` pose une règle saine : **« la vue ne corrige rien, elle constate »**. Donc :

1. **Jamais de passage automatique à « Dans JEMM »** (contrôle de l'utilisateur, Nielsen 3 ; un incident peut porter le code d'un autre après une renumérotation).
2. **Proposition d'un clic dans la fiche** : si le code est **présent dans le dernier export JEMM** et que le statut n'est pas « Dans JEMM », la ligne de R4 devient : **« Présent dans JEMM — Marquer « Dans JEMM » »** (le second morceau est un bouton `frappe-mini`, 28 px). Tesler (REF-06) : c'est le système qui porte ce qu'il sait déjà.
3. **Proposition groupée** dans l'onglet Incidents, en tête, **seulement si n > 0** : bandeau discret **« 12 incidents sont présents dans JEMM sans être marqués. [Les marquer « Dans JEMM »] »** — avec la liste des codes dépliable avant d'appliquer (voir le résultat avant d'agir, avis du 2026-09-28 « eho, ranger les groupes », R3).
4. **Incohérence « Dans JEMM » mais absent du dernier export** (et seulement si un export JEMM existe) : la pastille reçoit le **« ! »** déjà employé sur la planche (`.i-absent`, fond `#FFD700`, texte `#1a1a1a`) ; dans la fiche, la ligne de R4 dit **« ⚠ Absent du dernier export JEMM (15/10 08:12) »**. On **ne rétrograde pas** le statut : on le signale.
- Technique : `ecran-atelier.tsx` dispose déjà de `jemm` ; lui faire passer aux onglets un `Set` des codes présents (`codesJemm`), calculé une fois.

## R7 — La PLANCHE de préparation : oui, une petite pastille, à DROITE

- **Où** : dans `Incident` de `components/carte.tsx`, **au bout de la ligne des repères** (`i-reperes`), après l'heure et les marques `↔` / `!` — donc **calée à droite**. La pastille du **moyen** reste **à gauche** du code.
- **Pourquoi pas de confusion** : (a) **place** opposée (gauche = moyen, droite = statut) ; (b) **forme** différente (le moyen est un point plein de 5 px sans contour ; le statut est une jauge cerclée, une coche ou un « J ») ; (c) le moyen « CHAT » est vert et « MEDIA » jaune, d'où l'obligation d'une forme : une simple pastille colorée de statut serait **illisible** à côté.
- **Taille** : 9 px en style classique (texte à 7,5 px), 10 px en style clair ; le « J » passe à une pastille de 13 × 9.
- **Lisibilité sur toutes les couleurs de storyline** : sur la planche, toujours le **dessin clair** (intérieur blanc) entouré d'un **anneau `rgba(0,0,0,0.55)`** de 1 px, comme la pastille du moyen (`box-shadow`) — lisible sur un fond de storyline sombre comme clair (1.4.11).
- Ajouter le statut à l'infobulle (`title`) et au nom accessible du bouton : « 06.01.I05 — Sujet · E-MAIL · **En validation** ».
- **Uniquement sur la planche de PRÉPARATION** (source atelier). Sur la planche **JEMM**, `etat` porte l'état JEMM (`draft / started / ended`, déjà rendu par hachures, liseré doré, transparence) : n'y rien ajouter. Passer la **valeur** (`statutAtelier: StatutIncident`) via `versPlanche.ts` plutôt que de relire le libellé dans `etat`.

## R8 — Filtre par statut : oui, une rangée de pastilles avec effectifs

- En tête de l'onglet Incidents : **« Statut : Tous (48) · En préparation (20) · En validation (6) · Validé (10) · Dans JEMM (12) »**, boutons `aria-pressed`, un seul actif à la fois, mémorisé par onglet.
- Un filtre actif **déplie d'office** les storylines qui contiennent un incident retenu et masque les autres (règle déjà posée : avis « storylines repliées » R6).
- C'est l'outil du chef greycell : « montre-moi ce qui attend ma validation ». Sans filtre, il faudrait déplier 30 storylines.

## R9 — Migration (déjà codée, à compléter)

- `lireStatut()` : idée → **En préparation**, à coordonner → **En validation**, coordonné → **Validé** : ✅ conforme.
- Les incidents **anciennement** « coordonné » parce qu'importés de JEMM ne se distinguent plus des autres : **ne pas les passer en bloc à « Dans JEMM »** à l'aveugle. La **proposition groupée de R6** les rattrape proprement (ceux dont le code est réellement dans JEMM), d'un clic, à la première ouverture.
- Les **nouveaux** imports / alignements créent en « Dans JEMM » : ✅ conforme (déjà dans la copie de travail).

---

## Ce qu'il NE faut PAS faire

- ❌ Une pastille de **couleur seule** (orange / jaune / vert = paire classique du daltonisme ; et le jaune et le vert sont déjà pris par les moyens MEDIA et CHAT sur la planche).
- ❌ Garder le `<select>`, ou ajouter une **section « Statut »** dans la fiche : le stepper prend la place du select, pas une place en plus.
- ❌ Passer **automatiquement** à « Dans JEMM », ou **rétrograder** automatiquement un incident absent de JEMM.
- ❌ Une **confirmation** à chaque changement de statut (geste réversible).
- ❌ Un **liseré de statut** sur la carte de la planche : le bord et le fond appartiennent à la couleur de storyline.
- ❌ Réutiliser les **hachures** `etat-draft` pour « En préparation » : elles veulent dire « brouillon JEMM » (MASTAURIGE).
- ❌ Du **rouge** : il reste réservé aux alertes (avis n°1 R5, Von Restorff REF-06).
- ❌ Une animation, une pulsation, ou un historique complet des changements dans la fiche.
- ❌ Deux nuances de vert pour « Validé » et « Dans JEMM » : une seule, la forme fait la différence.

## Vérification attendue (avant de pousser, règle « tester en local »)

1. Clair **et** sombre (et `colorScheme: "dark"` du système) : pastilles, stepper actif, « J » lisibles.
2. Clavier : Tab entre dans le stepper, flèches changent, la ligne « … le … par … » se met à jour.
3. Planche de préparation, styles classique et clair, sur une storyline **jaune** et une **verte** : la pastille de statut reste distincte de celle du moyen.
4. Un incident marqué « Dans JEMM » dont on retire le code de l'export : « ! » + message ; un incident présent non marqué : proposition d'un clic.
5. Téléphone 360 px, texte à 150 % : stepper sur une ligne avec libellés courts, sans débordement.
