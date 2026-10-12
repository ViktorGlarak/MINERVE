# Avis n°92 — 2026-10-10 — Hashtags écrits dans les commentaires : page d'un hashtag (Social) et Tendances (Cockpit)

> DESIGNER contribue, ne tranche pas. Décision de départ (utilisateur, 10/10) : un commentaire compte autant qu'une publication pour les tendances et le compteur d'un hashtag ; le Cockpit affiche « #X : 120, dont 45 en commentaires ». Code lu sans rien modifier : `app-social\…\pages\hashtag\hashtag.ts`, `pages\profile\profile.ts` (carte « Réponse », l. 302-324), `components\right-panel\right-panel.ts` (l. 58), `app-cockpit\src\components\sections\Sections.tsx` (`TrendingSection`), `TootItem.tsx`.

## A. Social — page d'un hashtag

**A1. Option (a) : une liste unique, mêlée par date.** C'est ce que font les deux modèles des joueurs : sur Mastodon, le fil d'un hashtag montre les réponses au milieu des messages ; sur X, la recherche « Récent » mêle tweets et réponses (« En réponse à @x »). Deux onglets (b) iraient contre ce réflexe (règle 15, Jakob REF-06). Ils cacheraient aussi la moitié de la conversation autour du hashtag, alors que le joueur vient justement la voir. Et un onglet ne sert pas à lire dans l'ordre (règle 34). Le profil garde ses onglets : là, c'est le modèle X lui-même.

**A2. Carte du commentaire : reprendre la carte « Réponse » du profil**, avec trois retouches :
- **Extrait du post parent sur 2 lignes au plus** (`line-clamp: 2`, au lieu de 180 caractères). Dans un fil mêlé, le bandeau ne doit pas peser plus que le commentaire (règle 5, atténuer).
- **Les #hashtags et @mentions du texte en liens**, comme dans `post-card`. Aujourd'hui, `rep-texte` affiche du texte brut. Or le joueur doit voir pourquoi la carte est là (règle 25), et le profil y gagne aussi.
- **Même largeur, même séparateur et même en-tête auteur que `post-card`**, sinon la liste paraît faite de deux familles (règle 9). Pas de barre d'actions si elle n'existe pas déjà sur la carte : « Voir la conversation » suffit.

**A3. Libellé du compteur : garder « N publications ».** Sur X, une réponse est un post. Sur Mastodon, l'en-tête d'un hashtag dit « N messages » et compte déjà les réponses. « Messages » fait penser au Chat (messagerie privée) dans notre vocabulaire (règle 36). Aucun détail « dont… » côté joueurs (illusion d'abord, §1). Le même libellé, avec le même total, doit apparaître dans le panneau Tendances de droite (`right-panel.ts` l. 58), sinon les deux chiffres se contredisent (Nielsen 4). Plus tard, si l'on compte les avatars distincts, le modèle Mastodon est tout trouvé : « N publications · M participants ».

**A4. État vide** : « Aucune publication avec ce hashtag. » reste juste, puisqu'un commentaire est une publication.

## B. Cockpit — section « Tendances »

**B1. Ligne : `#tag ………… [réseau n] [réseau n] │ 120  ↩45`**
- Le total reste en mono `text-ink-muted`, à sa place.
- **Juste après le total**, un second nombre atténué : icône Lucide `MessageCircle` (ou `Reply`, celle du bandeau de `TootItem`) en 11 px, puis le nombre en mono 0,68 rem `text-ink-faint` `tabular-nums`. Même gabarit que les compteurs par réseau, donc rien de neuf à apprendre.
- Le placer **après** le total, et pas parmi les réseaux : on lit « 120, dont 45 ». Les compteurs par réseau découpent le total, celui-ci n'en est qu'une part. Un **filet vertical d'1 px** (`border-line`) sépare le groupe réseaux du groupe total + commentaires, sinon on prend l'icône de commentaire pour un 3e réseau (règle 9).
- **Masqué quand il vaut 0** : pas de bruit (règle 5).
- Le bouton porte **`aria-label` et `title`** = « #X : 120 publications, dont 45 en commentaires ». Ajouter le détail par réseau dans le `title` s'il y en a plusieurs (règle 10 : l'icône seule ne suffit pas). Le mot « dont » en clair sur chaque ligne serait plus explicite, mais il coûte ~4 caractères par ligne dans une colonne étroite (règle 7) : on le met **une fois dans la légende**.
- **Légende, une seule fois**, en complétant la ligne « Depuis le… » déjà en place : « Publications et commentaires comptés · ↩ = dont commentaires ».
- Point de cohérence pour l'implémentation : la **somme des compteurs par réseau doit inclure les commentaires** (= le total). Sinon la ligne se contredit.

**B2. Colonnes de veille d'un hashtag : suffisant**, l'étiquette « commentaire » et le bandeau « ↩ @auteur : extrait » de `TootItem` disent déjà ce qu'est l'élément et à quoi il répond. Deux compléments facultatifs :
1. surligner le #tag recherché dans le texte, pour qu'on voie d'un coup d'œil pourquoi l'élément est là ;
2. ne pas ajouter de filtre « Publications / Commentaires » tant que personne ne le demande (règle 37).

Vérifier aussi que l'étiquette `pl-tag-dev` n'a pas une couleur d'alerte (règle 20).

## Effort
A1-A3 faible : réutiliser la carte, changer une ligne CSS, rendre le texte en liens. B1 faible (un `span`, un filet, un `title`). Le décompte côté serveur relève d'ARCHITECTE/PLEIADE, hors du champ de DESIGNER.

Sources : règles 5, 7, 9, 10, 15, 20, 25, 34, 36, 37 (`MEMOIRE.md` §3) ; REF-06 (Jakob), REF-14 (Nielsen 4), REF-07, REF-08 (Lucide).
