# Avis DESIGNER n°118 — 2026-10-17 — Social sur téléphone (barre du haut, panneau du bas, Chat)

> **Constat utilisateur** : sur téléphone, les animateurs n'avaient pas accès à tous les boutons d'administration ; puis « le Chat a l'air de ne pas être fonctionnel ».
> **Causes** : sous 960 px, colonne de droite masquée (incarnation « au nom de », tendances, « Régler ») et recherche masquée ; sous 600 px, « Se connecter » / « Déconnexion » masqués ; page Chat écrasée dans 64 px (règle `.sur-chat`) et zone d'écriture sous le bord (100vh) ; à 320 px, page élargie (notifications PrimeNG 350 px, barre du bas, boutons des publications, outils de la zone d'écriture).
> **Correctif** (sous 960 px, ordinateur inchangé) : barre du haut — bouton « au nom de @avatar ▾ » / « Choisir un avatar » (« Tendances » pour un joueur) qui ouvre la colonne de droite en panneau du bas, loupe ; Chat en colonne de la hauteur de l'écran ; largeurs réparties sous 420 px.
> Revue sur captures iPhone 13, iPhone SE (320 px), iPad Mini et ordinateur ; essai local avec contenus fictifs.

## Verdict : validé avec réserves — 8 corrections, appliquées dans le même lot
**Juste** : la forme (panneau du bas, avis n°117) ; cibles 44 px ; état « au nom de » toujours visible (règle 25) ; Chat utilisable, champ ≥ 16 px (avis n°116) ; aucun débordement à 320 px ; ordinateur identique.

1. Doublon de l'avatar (`.incarne-rail`) dans la barre du bas du Chat (8 éléments, < 44 px à 320 px) → masqué sous 600 px.
2. Texte « Sélectionnez un avatar dans le panneau "Au nom de" » qui ne désigne plus rien sur téléphone → « Pour publier, choisissez d'abord un avatar. » + bouton « Choisir un avatar » qui ouvre le panneau (`PanneauService` partagé) ; message « Impersonation requise » → « Avatar requis ».
3. Déconnexion en icône seule collée à la loupe, compte réel invisible → retirée de la barre ; « Connecté : nom · rôle » + « Se déconnecter » en pied du panneau.
4. Focus du panneau : focus sur « Fermer » à l'ouverture, rendu au déclencheur à la fermeture, fond `inert`, `aria-labelledby`, `aria-haspopup="dialog"`, Échap seulement si ouvert.
5. En-tête du fil de Chat sur 2 lignes, rappel tronqué → rappel masqué sous 600 px, nom sur une ligne avec points de suspension.
6. Contenu du panneau : « Régler », « Redevenir moi », interrupteur « Origine » à 44 px ; carte « Bienvenue » masquée dans le panneau.
7. « Choisir un avatar » affaibli par l'opacité → couleur d'accent, gras, bordure accent.
8. En-tête « Boîtes de mes avatars » à 320 px → « Alertes » sur sa propre ligne.

## Peut attendre
Tablette : bouton « au nom de » plafonné à 420 px (fait) ; panneau latéral plutôt que du bas à cette taille. Trois rappels de l'avatar sur l'accueil (garder le bandeau au point d'action). Avatar « A » de l'opérateur à côté de la zone d'écriture alors qu'on publie au nom d'un avatar (aussi sur ordinateur). À vérifier sur un vrai iPhone : Chat clavier ouvert, panneau avec une vraie liste d'avatars, notifications à 320 px.

## Règle générale
Quand un écran change de forme sur téléphone, **réécrire les textes qui désignent un emplacement** (« dans le panneau… », « à droite… ») — mieux : les remplacer par un **bouton qui y mène**.
