# Avis n°96 — 2026-10-10 — Cockpit, Reporting : graphique « par hashtag »

> DESIGNER contribue, il ne tranche pas. Décision de départ : l'utilisateur (2026-10-10). Mise en œuvre : PLEIADE.
> Code lu sans rien modifier : `ReportingView.tsx`, `GrapheTemps.tsx`, `CellulesVues.tsx`, `globals.css` (`ck-vues`, `ck-chip`, `ck-totaux`), `api/bff/trending/route.ts`.

## 0. Trois points à régler avant de dessiner

1. **Vocabulaire** : ne pas écrire « messages ». Ce mot désigne le Chat (avis n°92, règle 36). L'unité existante est **« contenus »** (Tout), « publications » ou « commentaires », selon le sélecteur Contenu. Plus bas, « contenus » est employé dans ce sens.
2. **Tension avec la doctrine du n°75** (« plusieurs séries dans le temps = des lignes, jamais des aires empilées ») : elle reste valable pour la lecture **Nombres**. La lecture **Parts** pose une autre question, celle de la composition d'un tout. L'empilement à 100 % y est légitime, parce que chaque couche a sa propre base. On l'écrit dans le code pour qu'on ne le « corrige » pas plus tard.
3. **Séries qui se recouvrent** : un avatar peut appartenir à deux séries (groupe d'eho et catégorie, par exemple). En Nombres, cela ne gêne pas. En Parts, la somme dépasserait 100 %. Proposition : calculer les parts sur la **somme des attributions** (séries + Hors séries) et l'**écrire** sous le graphique quand il y a un recouvrement : « 12 contenus appartiennent à plusieurs séries : les parts portent sur 112 attributions. » La règle de calcul finale revient à PLEIADE/ARCHITECTE.

## R1. Placement et titre

- Un **panneau `pl-panel` à part**, placé **entre** « Activité par heure » et « Publications par cellule ». Pas d'onglet, parce qu'on compare ce graphique au précédent (règle 34). Pas de section repliée : un panneau toujours présent reste stable (règle 28), et son état vide est compact.
- En-tête du panneau, sur le modèle des autres : eyebrow **« Par hashtag »**, suivi en `text-[12px] text-ink-faint` de « — qui porte quels hashtags, heure par heure ».
- Titre du graphique (`GrapheTemps.titre`), qui suit Contenu et la lecture choisie :
  - en Nombres : « Contenus avec #otan + #ukr par heure, par série » ;
  - en Parts : « Part de chaque série dans les contenus avec #otan + #ukr ».
- **Contenu** : un seul réglage pour la page. Le sortir du premier panneau et le placer sur une ligne `ck-gt-reglages` sous l'en-tête de la page, avec la mention « s'applique aux deux graphiques ». Deux sélecteurs « Contenu » qui pourraient diverger seraient une source d'erreur (Nielsen 4). Variante minimale si on ne veut rien déplacer : rappeler en lecture seule dans le panneau hashtag « Contenu : Tout (réglé au-dessus) ».

## R2. Choix des hashtags

Ordre de haut en bas, dans une bande `bg-sunken` comme le choix d'un groupe d'eho :

1. **Saisie** `pl-input` avec le placeholder « Ajouter un hashtag (# facultatif) ». Entrée ou virgule valide la saisie. On tolère `#`, la casse, les accents et les espaces autour (Postel, règle 17). On affiche toujours la forme `#tag`. Un doublon est ignoré sans message d'erreur.
2. **« Tendances du moment »** : 12 puces `ck-chip` au plus, cochables (`aria-pressed`), avec le total en chiffres tabulaires et « ↩n » atténué pour les commentaires (code du n°92). Le libellé dit franchement que ces tendances sont celles **du moment**, et non celles de la période.
3. **« Choisis : »** : les puces retenues, chacune avec un ✕ (`aria-label="Retirer #otan"`, cible ≥ 24 px). Dès qu'il y en a deux, on ajoute un libellé : **« 2 hashtags additionnés — un contenu qui en emploie plusieurs compte une fois »**. On ajoute aussi « Tout retirer » en lien discret. Plafond proposé : **10**, au-delà, la saisie se désactive et un texte l'explique.

- **État vide** (aucun hashtag) : on ne dessine aucun axe. On affiche le texte de `ck-gt-vide` : **« Choisissez un ou plusieurs hashtags dans les tendances ou tapez-en un. »** (règle 18).
- **Hashtag sans aucun contenu sur la période** : il reste dans « Choisis » et on affiche « Aucun contenu avec #x sur la période », jamais un graphique vide sans explication (doctrine n°72).
- **Mémorisation** du choix et de la lecture par poste (`ck_reporting_hashtags`, avec try/catch), comme la période. En direct, le calcul suit la même cadence de 60 s, sans indicateur de chargement.

## R3. Bascule Nombres / Parts

- Un contrôle segmenté **`ck-vues` en radiogroup**, identique à Contenu, placé à droite de la ligne de réglages du panneau : **« Nombres · Parts (%) »**. On préfère « Nombres » à « Courbes », parce que la bascule change **ce qu'on mesure**, et pas seulement la forme. C'est une proposition, à trancher par l'utilisateur. Le choix est mémorisé.
- **Nombres** : on garde `GrapheTemps` tel quel (lignes, couleurs des séries, légende cliquable avec total).
- **Parts** : aires empilées, axe vertical **0 · 25 · 50 · 75 · 100 %** nommé « part des contenus avec #… ».
  - **Ordre** : les séries dans l'ordre de la légende, **la première sur la ligne de base** (c'est elle qu'on lit le mieux, et elle répond directement à « 60 % venait de FORAD »). **Hors séries en haut**, comme reste, contre la borne des 100 %.
  - **Hors séries** : gris réservé `var(--color-ink-faint)` **et hachuré** (motif du « direct » du n°74), pour éviter la confusion avec une série automatique qui recevrait le même jeton de la `PALETTE`, puisque ce gris y figure en 7e position. Libellé dans la légende : « Hors séries (comptes dans aucune série) ».
  - Aplats à **~75 % d'opacité** avec un **filet de 1 px couleur `--color-panel`** entre les couches, pour qu'elles se distinguent dans les deux thèmes.
  - **Légende cliquable en Parts** : un clic **met en avant** une série (les autres passent à 25 % d'opacité) au lieu de la masquer. La masquer obligerait à recalculer les parts, et la phrase « 60 % » changerait de sens sans que l'utilisateur le voie. On le dit dans l'aide : « cliquez une série pour la mettre en avant ».
- **Heures sans contenu** : la part n'existe pas. On ne dessine **rien**, ni 0 ni interpolation : l'aire **s'interrompt** et la colonne reste vide, avec un fond hachuré très léger en `--color-line-soft`. La bulle affiche « Aucun contenu avec #… à cette heure ».
- **Faibles effectifs** : 1 contenu fait 100 %, et le graphique devient trompeur. On ajoute, sous l'aire des parts, une **bande de volume de 28 px** (une barre par heure, en `--color-ink-muted`, avec le nombre total au survol) titrée « contenus par heure ».
- **Alternative à étudier** : des **colonnes empilées à 100 %**, une par heure, plutôt que des aires. Les données sont horaires, donc discrètes, une heure vide devient naturellement une colonne vide et rien n'est interpolé. À trancher par l'utilisateur ; les deux lectures respectent les règles ci-dessus.

## R4. Info-bulle (les deux lectures)

On garde `ck-gt-bulle`. En-tête : « ven. 10/10 · 14:00–15:00 · **25 contenus** avec #otan + #ukr ». Une ligne par série, **dans l'ordre de l'empilement** en Parts et triée par valeur en Nombres : pastille, nom, **« 15 · 60 % »**. Hors séries vient en dernier. Le nombre et le pourcentage figurent dans les deux lectures : on lit la même chose quelle que soit la vue.

## R5. Résumé chiffré

Sous le graphique, un tableau `ck-totaux` (mêmes classes que les totaux existants). Colonnes **Série · Contenus · Part**, avec une pastille de couleur. La ligne **Hors séries** est en italique. La dernière ligne, **Total**, compte les contenus distincts. La mention du recouvrement (point 0.3) se place sous le tableau si elle s'applique. La colonne choisie est en gras, selon le code `choisi` existant. On ne fait pas de tableau à côté du graphique : la largeur de 1 100 px est déjà prise, et sur un téléphone le tableau se placerait sous le graphique de toute façon.

## R6. Accessibilité

- Le tableau R5 est l'alternative principale, comme pour le graphique existant. On ajoute un `<details>` **« Voir heure par heure »**, fermé par défaut, avec un tableau heures × séries (nombre et %), pour qui ne peut pas survoler.
- `aria-label` du SVG = titre + total par série et part. Couleur jamais seule : hachure pour Hors séries, nom dans la bulle et la légende, ordre fixe (règle 10).
- **À faire aussi sur le graphique existant** : la bulle ne s'ouvre qu'à la souris. Proposition : SVG focusable (`tabIndex=0`), les flèches ← → déplacent l'heure survolée, Échap ferme (règle 11). On le fait une fois dans `GrapheTemps`, et les deux graphiques en profitent.

## Ordre conseillé

1. R2 + Nombres : on réutilise `GrapheTemps`, avec la série Hors séries en plus. C'est le plus rapide.
2. R5, puis R3 Parts (prop `lecture="parts"` dans `GrapheTemps` plutôt qu'un second composant) avec la bande de volume.
3. R6, clavier dans `GrapheTemps`.

**Critère de réussite** : à partir d'une capture en Parts, un animateur dit en moins de 10 s « à 14 h, 60 % des contenus avec #x venaient de FORAD, sur 25 contenus ».
