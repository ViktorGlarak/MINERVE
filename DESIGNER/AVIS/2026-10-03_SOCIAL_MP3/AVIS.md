# Avis n°39 — Réseau social : joindre et écouter un MP3 sur un post principal

> **Date** : 2026-10-03 · **Demandeur** : l'utilisateur · **App** : `app-social` (Angular 21, PrimeNG / PrimeIcons, signaux) — `components/compose/compose.ts`, `components/post-card/post-card.ts`, `pages/post-detail/post-detail.ts`, `components/video-grid/video-grid.ts`, `pages/profile/profile.ts`.
> **Code lu** : web au commit `e9aed18` ; serveur avec les modifications **non commitées** en cours (`upload.ts`, `social/posts.ts`, `service/index.ts` : `audio/mpeg`, signature ID3 / trame MPEG, `SOCIAL_UPLOAD_AUDIO_MAX_SIZE` = 20 Mo par défaut, `typeDeMedia` → `"audio"`, `refuserAudioEnReponse`).
> **Statut** : 🟡 proposé, à arbitrer par l'utilisateur. La mise en œuvre revient à MASTORION / PLEIADE / ARCHITECTE, **à tester en local avant tout push**.
> ⚠ DESIGNER contribue, il ne tranche pas : ce sont des propositions argumentées. Le besoin de l'utilisateur et les choix de PLEIADE / ARCHITECTE font foi. Les 5 mises en page (Mastodon par défaut, X/Twitter, Facebook, Instagram, YouTube) gardent leur charte : on ne touche qu'à des **jetons existants** (`--masto-*`).

## Besoin exprimé (2026-10-03)

Joindre des fichiers **.mp3** aux **posts principaux** (pas aux réponses), avec « un visuel correct pour la lecture des fichiers MP3 ». Usages d'exercice : messages audio, interceptions radio, discours, podcasts d'avatars fictifs.

## Constat (lecture du code, 2026-10-03)

| # | Constat | Gravité (0-4) | Source |
|---|---|---|---|
| C1 | **Partout, « pas vidéo » veut dire « image »**. `post-card` (post et réponses), `profile` (grille Instagram) et l'app **`app-cockpit`** (`TootItem.tsx`) affichent tout ce qui n'est pas `video` dans un `<img>`. Un post audio y deviendrait une **image cassée**. Ce sont les seuls endroits qui casseraient de façon visible. | 4 | Heuristique 1 « état du système visible » (REF-14) |
| C2 | **Le bouton « trombone » du composer est inaccessible au clavier** : c'est un `<label>` sans nom accessible, et l'`<input type="file" hidden>` qu'il porte ne reçoit jamais le focus. Le bouton média des réponses et « Ajouter un média » en édition ont le même défaut. | 3 | WCAG 2.1.1 Clavier, 4.1.2 Nom, rôle et valeur (REF-13) |
| C3 | **Le composer ne connaît pas les limites** (10 / 50 / 20 Mo) : un MP3 de 30 Mo part entier sur le VPN avant d'être refusé, avec un toast générique **sans accents** (« Fichier trop volumineux. Reduisez la taille du media. ») qui disparaît après 5 s. | 3 | Heuristique 5 « prévenir l'erreur », 9 « aider à corriger » (REF-14) ; Doherty (REF-06) ; erreurs à la GOV.UK, règle 24 |
| C4 | **L'aperçu en édition est toujours un `<img>`** (`editMediaPreview`), même pour une vidéo choisie. Celui des réponses aussi (`comment-preview-img`). L'audio aggraverait un défaut qui existe déjà. | 2 | Heuristique 1 |
| C5 | **Info-bulle fausse sur les réponses** : « Ajouter une image », alors que le champ accepte aussi les vidéos. | 1 | Heuristique 2 « correspondance avec le monde réel » |
| C6 | **Pas de durée pour l'audio** : `videoMetaForUpload` ne lance `ffprobe` que pour les vidéos, donc `duration_seconds` restera vide pour un MP3. La carte ne pourra afficher la durée qu'après chargement du fichier. | 2 | Règle 19 (Tesler) : le système porte ce qu'il sait déjà |
| C7 | **Après « retirer », on ne peut pas reprendre le même fichier** : la valeur de l'`<input>` n'est pas remise à zéro, donc rechoisir le même MP3 ne déclenche plus `change`. | 1 | Heuristique 3 « contrôle et liberté » |
| C8 | **Aucun thème sombre trouvé** dans le code lu : PrimeNG est réglé sur `darkModeSelector: false` et `styles.scss` ne définit que des jeux de jetons clairs, un par mise en page. Les recommandations restent sur les jetons `--masto-*` : elles suivront le jour où un thème sombre arrivera. | — | Règle 1 (jetons sémantiques, REF-01) |
| C9 | Le profil n'a **pas d'onglet « Médias »** : seulement « Publications » (Mastodon, X, Facebook), une grille « PUBLICATIONS » (Instagram) et « Vidéos » (YouTube, qui passe en fait **tous** les posts à `app-video-grid`). | — | — |

## Recommandations

### 1. Le lecteur dans la carte d'un post

**R1 — Le lecteur natif `<audio controls>`, posé dans un bandeau dessiné par nous** *(recommandé ; effort : ½ journée)*.
Pourquoi le natif : le clavier, le lecteur d'écran, la barre de position, le volume, le contrôle au doigt sur mobile (et, le plus souvent, les commandes de l'écran verrouillé) et, sur Chrome et Edge, la vitesse de lecture **sont déjà là et déjà testés**. Un lecteur maison doit tout refaire, et chaque oubli devient un défaut d'accessibilité (WCAG 2.1.1, 4.1.2). C'est la loi de Jakob (REF-06) : le contrôle audio du navigateur est celui que tout le monde connaît. Seul défaut : son aspect varie d'un navigateur à l'autre, et on ne peut pas le styler. Le bandeau autour donne l'unité visuelle.

Maquette textuelle (largeur de la carte, sous le texte du post, à la place d'une image) :

```
┌──────────────────────────────────────────────────────────────┐
│  (🔊)  Audio · 2:14                                          │  ← ligne 1 : pastille + libellé
│  [ ▶  0:00 / 2:14  ━━━━━━━━━━━━━━━━━━━━━━━━  🔈  ⋮ ]          │  ← ligne 2 : <audio controls> 100 %
└──────────────────────────────────────────────────────────────┘
```

Gabarit Angular proposé (dans `post-card.ts`, nouvelle branche du bloc `.post-media`) :

```html
@else if (dp().media_type === 'audio') {
  <figure class="post-audio">
    <figcaption class="post-audio-label" [id]="'audio-' + dp().id">
      <i class="pi pi-volume-up" aria-hidden="true"></i>
      <span>Audio</span>
      @if (dp().duration_seconds) { <span class="post-audio-duree">· {{ duree(dp().duration_seconds) }}</span> }
    </figcaption>
    <audio controls
           [attr.preload]="dp().duration_seconds ? 'none' : 'metadata'"
           [src]="dp().media_url!"
           [attr.aria-labelledby]="'audio-' + dp().id"></audio>
  </figure>
}
```

Règles de forme :
- **Même cadre que les images et les vidéos** : la `.post-media` existante (`margin-top: 10px`, bordure `1px var(--masto-border)`, rayon de 10 px) ; fond `var(--masto-panel-light)` ; marge intérieure de 12 px ; `audio { width: 100%; display: block; }`. Le son se lit alors comme « un média de plus », à la même place que les autres (cohérence, heuristique 4).
- **Deux lignes à toutes les largeurs**, pas de variante mobile : la ligne 2 prend toute la largeur, donc la barre de position reste longue et facile à viser même sur téléphone (Fitts ; cibles ≥ 24 px, 44 px en tactile, règle 12). Hauteur totale ≈ 90 px.
- **Libellé** en `var(--masto-text)` à 0,8 rem, durée en `font-variant-numeric: tabular-nums`. ⚠ Ne pas mettre la durée en `--masto-text-secondary` : sur la mise en page Instagram, `#8e8e8e` sur blanc donne ≈ 3,3 : 1, sous le 4,5 : 1 exigé pour un petit texte (règle 21).
- **Pastille** : icône PrimeIcons `pi-volume-up` (ou `pi-microphone`, au choix de l'utilisateur) en couleur `var(--masto-accent)`, **décorative** (`aria-hidden`) : l'information est portée par le mot « Audio » (règle 10, jamais l'information par la seule couleur ou la seule icône).
- **Durée** au format `m:ss`, `h:mm:ss` au-delà d'une heure (discours, podcasts).
- **Pas de nom de fichier sur la carte publiée** : aucun vrai réseau ne l'affiche, et un « interception_v3_FINAL.mp3 » trahirait les coulisses de l'animation. Le **texte du post** sert de titre et de description.
- `preload="none"` quand le serveur a fourni la durée (voir R3) : sur une connexion VPN faible, un fil de 20 posts audio ne télécharge rien tant qu'on n'appuie pas sur lecture. Sinon `preload="metadata"`, qui ne lit que l'en-tête pour obtenir la durée.

**R2 — Variante, seulement si le rendu natif déçoit à l'essai en local : un lecteur maison bâti sur des éléments natifs** *(effort : 1 à 1,5 jour + tests au clavier et au lecteur d'écran)*.
Même bandeau, mais `<audio>` sans `controls`, piloté par :
- un `<button type="button">` lecture / pause : icône `pi-play` / `pi-pause`, **nom accessible qui change** (« Lire le son » / « Mettre en pause »), cible de 44 × 44 ;
- un `<input type="range" min="0" [max]="duree" step="1">` pour la position : c'est le modèle **Slider** de l'APG (REF-19), qu'un `range` natif fournit sans ARIA à écrire (flèches ±1 s, Début / Fin). On ajoute `aria-label="Position de lecture"` et `[attr.aria-valuetext]="'1 min 05 s sur 3 min 20 s'"` ;
- le temps « 1:05 / 3:20 » en chiffres tabulaires, **visible en permanence**, pas au survol ;
- un bouton de vitesse **unique qui fait défiler** 1× → 1,25× → 1,5× → 2× (utile pour réécouter vite un long discours, et on évite un menu de plus, Hick, règle 16), nom accessible « Vitesse de lecture : 1,5 fois ».
⛔ Jamais de `<div>` cliquables : ce serait la porte ouverte aux défauts que R1 évite. ⚠ Limite : seuls les modèles Dialog et Tabs de l'APG sont détaillés dans nos fiches ; le Slider est cité dans l'index de REF-19, pas encore ingéré en détail.

**R3 — Côté serveur, renseigner `duration_seconds` pour l'audio** *(effort : ¼ h)*.
`probeDuration` (ffprobe) sait déjà lire la durée d'un MP3 : l'appeler aussi quand `typeDeMedia` vaut `"audio"` (sans vignette). La carte, la grille YouTube et la grille Instagram peuvent alors afficher « 2:14 » **avant** toute lecture (règle 19, Tesler ; heuristique 1). Si ffmpeg est absent, `null`, et la carte retombe sur `preload="metadata"` (R1).

**R4 — Un seul son à la fois** *(effort : ¼ h)*.
Lancer un son **met en pause** tout autre son ou vidéo en cours, dans toute l'app (fil, page du post, aperçu du composer). Un seul point de code, pas une logique par composant (règle « un seul calcul partout ») : un service racine qui écoute l'événement `play` en phase de capture (l'événement ne remonte pas, la capture le voit quand même) :

```ts
document.addEventListener('play', e => {
  const t = e.target;
  if (!(t instanceof HTMLMediaElement)) return;
  document.querySelectorAll<HTMLMediaElement>('audio, video')
    .forEach(m => { if (m !== t && !m.paused) m.pause(); });
}, true);
```

C'est le comportement attendu par tous (Jakob) : deux voix superposées seraient inaudibles, et dans un PC d'exercice personne ne cherchera quel post parle.

**R5 — Aucune lecture automatique, nulle part** : ni au chargement, ni au défilement, ni pour enchaîner le son suivant, ni sur la page du post YouTube (où la vidéo, elle, démarre seule aujourd'hui). Le joueur décide quand le son sort de ses haut-parleurs. WCAG 1.4.2 (contrôle de l'audio) ; heuristique 3 « contrôle et liberté ». Quand la carte est détruite (changement de page), le son s'arrête : acceptable, **pas de mini-lecteur persistant** dans cette première version.

**R6 — L'état « en lecture » sans animation obligatoire.** Le lecteur natif le montre déjà (bouton pause). Si la variante R2 ajoute un repère (barres d'égaliseur), il doit être **figé** sous `prefers-reduced-motion: reduce` et doublé par le changement d'icône du bouton (règles 10 et 14).

**R7 — Mettre fin au « tout ce qui n'est pas vidéo est une image »** *(effort : ½ h, à faire même si le reste attend)*.
Dans chaque affichage de média, des branches **explicites** `image` / `video` / `audio`, et une branche par défaut qui ne casse pas : « Pièce jointe » + lien d'ouverture. À corriger dans `post-card` (post et réponses), `profile` (grille Instagram), `post-detail` (lecteur YouTube) et, **hors de ce dépôt**, `app-cockpit/src/components/TootItem.tsx` (à signaler à PLEIADE). Dans le cockpit, un simple « 🔊 Audio · 2:14 » suffit : c'est un outil de veille, pas un lecteur.

**R8 — Transcription : à décider (proposition, pas une exigence imposée).** WCAG 1.2.1 (niveau A) demande une alternative textuelle aux contenus seulement audio. Dans un exercice, une interception peut volontairement ne pas avoir de transcription : c'est le travail de la cellule de l'écouter. Mais **un PC n'a pas toujours de casque ni de haut-parleurs**. Par défaut, je propose : le **texte du post** sert de description (R10 y invite), et pas de champ « transcription » dans cette version. Plus tard, si le besoin se confirme : un repliable « Transcription » (modèle Disclosure de l'APG) sous le lecteur.

### 2. Le composer

**R9 — Un vrai bouton, qui dit ce qu'il accepte** *(effort : ½ h)*.
- Remplacer le `<label>` par un `<button type="button" class="tool-btn" (click)="fichier.click()">` + `<input #fichier type="file" hidden>` : il devient atteignable au clavier (corrige C2).
- Nom accessible **et** info-bulle identiques : **« Joindre une image, une vidéo ou un son MP3 »**. L'icône peut rester `pi-paperclip`, qui veut dire « pièce jointe » quel que soit le type.
- `accept="image/*,video/*,audio/mpeg,.mp3"` : l'extension `.mp3` en plus du type, parce que certains systèmes déclarent `audio/mp3` ou rien du tout (le serveur accepte déjà `audio/mp3`, et c'est sa vérification de signature qui fait foi).
- Remettre `fichier.value = ''` après « Retirer » et après publication (corrige C7).

**R10 — L'aperçu d'un son avant publication** *(effort : ½ h)*.
Même bandeau qu'en R1, avec ce que l'**auteur** a besoin de vérifier. Ici le nom du fichier est utile : il confirme qu'on a pris le bon fichier, et il n'est pas publié.

```
┌──────────────────────────────────────────────────────────────┐
│  (🔊)  interception_radio_D+12.mp3 · 3,2 Mo · 2:14  [✕ Retirer] │
│  [ ▶  0:00 / 2:14  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━  🔈  ⋮ ]       │
└──────────────────────────────────────────────────────────────┘
```

- Lecteur natif `controls preload="metadata"` sur l'URL objet : on **peut écouter** avant de publier. La durée vient de `loadedmetadata`.
- « Retirer » : **un bouton avec un texte** (« Retirer »), placé au bout de la ligne 1, et non une croix posée en `position: absolute` sur le média comme pour une image (il n'y a pas d'image à recouvrir). Nom accessible « Retirer le son ».
- Si le navigateur **ne peut pas lire** le fichier (événement `error` sur l'`<audio>`) : message dans le bandeau, publication bloquée : « Ce fichier ne peut pas être lu. Vérifiez que c'est bien un MP3, ou réexportez-le. » Ce que le navigateur de l'auteur ne lit pas, aucun joueur ne le lira.
- Quand un son est joint, le texte d'invite devient **« Décrivez ce son : titre, contexte… »** au lieu de « Quoi de neuf ? ». Le texte du post sert alors de titre (grille YouTube) et d'alternative textuelle (R8).
- Pendant l'envoi : le bouton « Publier » garde son état de chargement ; si possible, **« Envoi… 45 % »** (progression `HttpClient`, `reportProgress`). 20 Mo sur un VPN prennent du temps, et sans indication l'utilisateur relance (heuristique 1, Doherty).

**R11 — Les erreurs : avant l'envoi, sur place, en disant comment corriger** *(effort : ½ h + exposer les limites)*.
- Le serveur **expose les limites** dans sa config publique (par exemple `social_upload_audio_max_mb`, et la même chose pour la photo et la vidéo) ; le composer contrôle **avant** l'envoi le type et le poids (heuristique 5 ; tolérant en entrée, strict en sortie, Postel).
- Message **sous l'aperçu**, `role="alert"`, qui reste tant que le problème n'est pas réglé, et non un toast de 5 s (WCAG 4.1.3 ; règle 24) :
  - trop lourd : **« Ce son pèse 27 Mo ; le maximum est de 20 Mo. Raccourcissez-le, ou réexportez-le à 128 kbit/s : c'est suffisant pour une voix. »**
  - mauvais format : **« Seuls les sons au format MP3 sont acceptés. Convertissez le fichier (WAV, M4A, OGG…) en MP3. »**
  - refus du serveur (signature invalide, etc.) : **afficher le message du serveur tel quel**. Les textes en cours de rédaction côté serveur sont bons (« Son trop lourd (max 20MB) ») ; il suffit d'écrire « 20 Mo » plutôt que « 20MB » pour un écran en français.
- Corriger au passage le message 413 actuel, sans accents.

**R12 — En édition d'un post principal** : même `accept`, même bouton (R9), et un aperçu qui **suit le type** du fichier choisi (image / vidéo / son), au lieu du `<img>` systématique (corrige C4). Une réponse ne s'édite pas avec un média : rien à prévoir.

### 3. Les réponses

**R13 — Dire ce que le bouton accepte, en positif** : info-bulle et nom accessible **« Joindre une image ou une vidéo »** (corrige aussi C5) ; `accept="image/*,video/*"` inchangé. Je déconseille d'écrire « (pas de son) » sur l'info-bulle : on attirerait l'attention sur une option qui n'existe pas. La liste positive suffit (avis de DESIGNER, dans l'esprit de Polaris pour la rédaction des interfaces, cité par REF-04 : dire ce qu'on peut faire).

**R14 — Si un MP3 passe quand même** (filtre « Tous les fichiers » du sélecteur, ou un futur glisser-déposer) : refus **côté client, immédiat**, fichier non joint, message sous le champ de réponse (`role="alert"`) :
**« Les réponses n'acceptent pas les sons. Pour diffuser ce MP3, publiez-le dans un nouveau post. »**
Le message dit **pourquoi** et **quoi faire à la place** (heuristique 9). Il reprend le sens du message serveur déjà écrit (« Les réponses n'acceptent pas les fichiers audio : images et vidéos seulement »), qui reste le garde-fou final, y compris pour l'API `service` (`reply_to_post_id`). Profiter du passage pour que l'aperçu d'une réponse affiche une **vidéo** comme une vidéo (C4).

### 4. Grilles du profil et mise en page YouTube

**R15 — Oui, un post audio apparaît dans les grilles, avec une vignette « son » qui ne ressemble pas à une vidéo** *(effort : 1 h)*.
- **`app-video-grid`** (accueil YouTube, onglet « Vidéos » du profil, suggestions de la page du post) : aujourd'hui un post audio tomberait dans la vignette « texte ». Proposer une branche `audio` : le même fond sombre en dégradé que la vignette vidéo sans image (`ytv-thumb-fallback`), une grande icône `pi-volume-up` au lieu du triangle de lecture, le texte du post sur 3 lignes, la **durée** dans le badge `ytv-duration` déjà existant, et un petit marqueur texte **« AUDIO »** en haut à gauche. Sans ce mot, le joueur prendrait le son pour une vidéo sans vignette (règle 10, heuristique 2). YouTube héberge des podcasts sous image fixe : le format est connu (Jakob).
- **Page du post YouTube** (`post-detail`) : au lieu de « Publication sans vidéo », un panneau 16/9 sombre avec la grande icône, le texte du post, et le bandeau de R1 posé au bas du panneau. **Pas de lecture automatique** (R5), contrairement à la vidéo.
- **Grille Instagram** (`profile`) : tuile « texte » existante + pastille `pi-volume-up` en haut à droite, comme la pastille `pi-video` des vidéos (même code visuel, `ig-grid-overlay`). Pas de lecteur dans la tuile : on ouvre le post.
- Il n'y a pas d'onglet « Médias » (C9) : rien à filtrer aujourd'hui. Si on en crée un un jour, l'audio y entre.

### 5. À éviter

- ⛔ **La lecture automatique**, même en sourdine, et l'enchaînement automatique sur le son suivant (R5).
- ⛔ **La chute dans `<img>`** de tout ce qui n'est pas une vidéo (R7).
- ⛔ **Une fausse forme d'onde** dessinée au hasard : elle fait croire à une donnée qui n'existe pas. Une vraie forme d'onde (calculée par ffmpeg sur le serveur) est possible plus tard, mais ce n'est pas nécessaire.
- ⛔ **Un lecteur maison en `<div>`**, des commandes qui n'apparaissent qu'au survol (inutilisables au doigt), un temps de lecture caché.
- ⛔ **Le nom du fichier sur la carte publiée** (coulisses de l'animation visibles, et aucun réseau réel ne le fait).
- ⛔ **Des erreurs seulement en toast**, et un refus qui n'arrive qu'après 20 Mo d'envoi (R11).
- ⛔ **Un nouveau jeu de couleurs** pour l'audio : les jetons `--masto-*` de chaque mise en page suffisent, et la charte de chaque réseau fictif prime.
- ⚠ `controlsList="nodownload"` : je **ne** le recommande **pas** par défaut. Le menu natif « Télécharger » peut servir aux analystes de la cellule. À trancher par l'utilisateur.

## Questions à l'utilisateur (réponse par défaut entre parenthèses)

1. **Lecteur natif (R1) ou lecteur maison (R2) ?** *(R1, à juger à l'essai en local sur Chrome, Edge et Firefox ; R2 seulement si le rendu déçoit.)*
2. **Un champ « transcription » ?** *(Non pour l'instant : le texte du post sert de description, R8.)*
3. **Laisser le téléchargement du MP3 par le menu du lecteur ?** *(Oui.)*
4. **L'audio dans la grille YouTube ?** *(Oui, avec la vignette « AUDIO » de R15.)*

## Ordre de mise en œuvre proposé

1. R7 (plus d'image cassée) + R3 (durée côté serveur) — indispensables dès que le serveur accepte l'audio.
2. R1 + R4 + R5 (lecteur, un seul son à la fois, pas de lecture automatique).
3. R9 + R10 + R11 (composer), R13 + R14 (réponses), R12 (édition).
4. R15 (grilles YouTube et Instagram), puis le signalement de `app-cockpit` à PLEIADE.

Essai en local avant tout push : un MP3 avec étiquette ID3, un MP3 sans étiquette, un faux MP3 (un fichier renommé), un fichier de 25 Mo, un son déposé en réponse ; vérifier dans les 5 mises en page, au clavier seul (Tab, Espace, flèches) et sur la largeur d'un téléphone ; vérifier que **le déplacement dans le son** fonctionne, ce qui suppose que `/api/uploads/social` réponde aux requêtes partielles (HTTP 206 / `Range`), y compris derrière Traefik.

## Sources

Nielsen, 10 heuristiques (REF-14) : 1, 2, 3, 4, 5, 9 · WCAG 2.2 (REF-13) : 1.2.1, 1.4.2, 1.4.3, 2.1.1, 2.5.8, 4.1.2, 4.1.3 · WAI-ARIA APG (REF-19) : Slider, Disclosure (cités dans l'index, pas encore ingérés en détail) · Laws of UX (REF-06) : Jakob, Fitts, Hick, Doherty, Postel, Tesler · GOV.UK (REF-10) : messages d'erreur · Refactoring UI (REF-07) : hiérarchie, ne pas transmettre l'information par la seule couleur · Polaris (REF-04) : rédaction des interfaces · Doctrine DESIGNER règles 1, 10, 12, 14, 16, 17, 19, 21, 24.
