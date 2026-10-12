# Avis n°95 — 2026-10-10 — eho, planche des joueurs : zones repliables sans casser le glisser-déposer

> DESIGNER contribue, il ne tranche pas. Code lu sans rien modifier : `eho\src\components\planche.tsx` (1 182 l.), `src\lib\zones-planche.ts`, `src\app\(admin)\trombinoscope\page.tsx` (repli du 2026-10-10, `CadrePays`, `CLE_REPLIES`).

## Ce que dit le code (noms réels et pièges)

- **Zones** : `ZONES_PLANCHE` = **À CLASSER** (clé `""`, la réserve) puis Mercure, Arnland, Bothnia, France, Autre. Dans une zone, des **rubriques** (20 au maximum) puis le bloc **« Sans rubrique »** (`HORS_RUBRIQUE = ""`), **toujours rendu en dernier** et masqué s'il est vide alors que des rubriques existent. Le libellé « Sans rubrique » existe déjà, sur la planche comme dans la barre de rangement : **on garde ce mot et on n'introduit pas « Non classé »**. Il n'y a rien à créer, puisque le bloc reparaît dès qu'il contient une carte.
- **Glisser-déposer HTML5 natif**, sans bibliothèque. `glisse.current` est remis à zéro par `onDragEnd` sur la carte d'origine.
- **Piège 1, le démontage de la source.** Si le bloc d'où part la carte est démonté pendant le glissement (une zone repliée en cours de route), Chrome n'émet plus `dragend` : la carte reste « saisie » et le repère reste affiché. **Rien ne doit donc se replier pendant un glissement.**
- **Piège 2, le scintillement de `dragleave`.** Le bandeau contient des boutons (`VersGt`, « + Rubrique », le compteur). Passer sur l'un d'eux déclenche `dragleave` sur le bandeau. Il faut ignorer l'événement si `e.currentTarget.contains(e.relatedTarget)` est vrai, sinon le minuteur repart à zéro.
- **Piège 3, les boutons imbriqués.** Dans le trombinoscope, tout le bandeau est un `<button>`. Ce n'est pas possible ici à cause des boutons qu'il contient. On fait du **titre** (▶ + nom) le bouton (`aria-expanded`, `aria-controls`) et on l'étend à tout le bandeau par un pseudo-élément (`after:absolute after:inset-0`). Les autres boutons passent au-dessus (`relative z-10`).
- **Piège 4, la pagination.** Un bloc montre 60 cartes (`PAR_PAGE`). `deposer(zone, bloc, null)` ajoute **en fin** de bloc : dans un « Sans rubrique » de plus de 60 cartes, la carte déposée serait invisible une fois la zone dépliée.
- **Défilement automatique** : c'est celui du navigateur, lent, près des bords. Le repli aide justement : les zones repliées raccourcissent la page et rapprochent les cibles. Pas de défilement maison à ajouter.

## Recommandations

**R1. Le repli lui-même, avec les codes du trombinoscope.**
- **Le bandeau.** Il garde ▶, qui pivote de 90° quand la zone est ouverte (150 ms). Replié, il passe en `rounded-md` et affiche « · replié » en petit, avec une opacité de 80 %, à côté du nom.
- **Le compteur** reste visible.
- **Le contenu** d'une zone repliée n'est **pas rendu**, ce qui allège la page de 3 500 cartes.
- **« Tout replier » et « Tout déplier »** : deux boutons texte indigo dans la barre d'en-tête de la planche, près de la recherche et de « Mode sélection ».
- **La mémorisation** se fait en `localStorage`, sous une clé **par planche** : `eho.planche.zones-replies:perso` ou `:<id du GT>`. La lecture et l'écriture sont protégées par `try/catch`.
- **« + Rubrique »** sur une zone repliée commence par la déplier, puis ouvre la saisie.
- **La réserve À CLASSER** est repliable comme les autres zones.

**R2. L'ouverture au survol.**
- **Délai : 700 ms**, à partir du `dragenter` sur le bandeau. Le minuteur n'est pas relancé à chaque `dragover`. Il est annulé à la sortie réelle du bandeau, au dépôt et à la fin du glissement.
- **Pourquoi 700 ms.** On traverse un bandeau de 40 px en moins de 300 ms pour viser une zone plus bas : à 700 ms, ce passage ne déclenche rien. La valeur reste dans la fourchette de macOS (0,5 à 1 s).
- **L'attente se voit.** Le liseré d'accent de 3 px déjà présent en bas du bandeau devient une **barre de progression**. Une barre blanche s'y remplit de gauche à droite en 700 ms, de façon linéaire, en animant `transform: scaleX` depuis la gauche. **Pas de pulsation** : elle n'indique pas la durée restante.
- **Avec « réduire les animations »**, la barre ne se remplit pas : le mot « ouverture… » remplace « · replié », et l'ouverture survient quand même à 700 ms.
- **À l'ouverture**, le bandeau ne bouge pas sous le pointeur, car le contenu se déploie dessous. Le glissement continue vers une rubrique précise.

**R3. Le bandeau survolé pendant un glissement**, qu'il soit replié ou ouvert (une seule règle pour tous les bandeaux).
- **L'anneau** : `ring-2 ring-amber-400 ring-offset-2`. C'est l'ambre déjà utilisé pour les cibles de dépôt (`border-amber-400`, `Repere`).
- **Le fond** s'éclaircit légèrement (voile `bg-white/15`).
- **Le curseur** prend la forme « déplacer » (`dropEffect = "move"`).
- **Le texte** remplace « · replié » sous le nom par **« Lâcher ici → Sans rubrique »**. Pour la réserve, il devient « Lâcher ici → À classer ». Le message est en texte : le sens ne repose pas sur la couleur seule (règle 10).
- **Une autorité STARTEX vers une autre zone** : pas de `preventDefault`, donc le curseur natif « interdit » s'affiche. Le texte devient « ★ Autorité connue : reste dans Mercure », sans anneau. La zone s'ouvre quand même au bout de 700 ms, ce qui est sans danger.

**R4. Où la carte se pose.**
- **Destination** : le bloc **« Sans rubrique » de la zone, en TÊTE** de ce bloc (index 0, avant la première carte), et non en fin. Le bloc garde sa place, après les rubriques. Une carte posée en tête reste visible malgré la pagination à 60 et se retrouve sans chercher.
- **Enregistrement** : les deux écritures existantes, `paysEstime` puis `enregistrerZone`.
- **Si la carte est déjà dans cette zone**, le dépôt sur le bandeau la remet dans « Sans rubrique », ce qui est cohérent.
- **La zone reste repliée** : on n'ouvre pas ce que le joueur a fermé.

**R5. Le retour après dépôt**, en moins de 400 ms (règle 13).
- **Le compteur** du bandeau s'incrémente, avec une mise en valeur unique : passage à l'échelle 1,15 puis retour à 1, en 200 ms.
- **Le bandeau** s'éclaircit brièvement, pendant 600 ms.
- **Un message bas d'écran** de 4 s, sur le modèle de la barre de rangement : **« Rangé dans Mercure › Sans rubrique · Afficher »**. « Afficher » déplie la zone, la fait défiler jusqu'à la carte et la met en valeur.
- **Accessibilité du message** : il est annoncé par une région `role="status"`. Au téléphone, il s'affiche au-dessus de la barre d'onglets du joueur (56 px).
- **Même message** après un rangement par la barre de sélection dans une zone repliée.

**R6. Au départ du glissement : on ne replie rien.**
- **Aucun repli automatique** au départ : cela déplacerait toute la page sous la main et démonterait la source (piège 1).
- **Une zone ouverte par le survol est provisoire.** À la fin du glissement, ou sur Échap, elle se **referme si la carte n'y a pas été posée**, comme dans le Finder. Si la carte y a été posée, elle reste ouverte et cet état est mémorisé.
- **Les replis provisoires** ne sont appliqués qu'**après** l'événement `dragend`.

**R7. Clavier et accessibilité.**
- **L'alternative au glisser existe déjà** et reste la voie de référence (WCAG 2.5.7) : le **mode sélection** avec la barre « Ranger dans [pays] [rubrique] », et la liste des zones dans la fiche d'un avatar. Le repli n'y change rien.
- **Le bandeau** est un vrai bouton : Entrée et Espace, anneau de focus visible, `aria-expanded`, et un nom accessible du type « Mercure, 214 avatars, replié ».
- **La recherche** ne déplie rien automatiquement. Une zone repliée qui contient des résultats affiche une pastille « 3 résultats », et un clic la déplie.

## Valeurs retenues

| Paramètre | Valeur |
|---|---|
| Délai d'ouverture au survol | **700 ms**, depuis le `dragenter`, sans relance au `dragover` |
| Indication de l'attente | liseré de 3 px rempli en 700 ms, linéaire, `scaleX` (sans animation : « ouverture… ») |
| Bandeau ciblé | `ring-2 ring-amber-400 ring-offset-2` + voile `bg-white/15` + « Lâcher ici → Sans rubrique » |
| Point de chute | « Sans rubrique » de la zone, **index 0** ; zone laissée repliée |
| Retour | compteur ×1,15 sur 200 ms · éclaircissement de 600 ms · message de 4 s avec « Afficher » |
| Rotation ▶ | 90°, 150 ms |
| Clé de mémorisation | `eho.planche.zones-replies:<perso \| id GT>` |
