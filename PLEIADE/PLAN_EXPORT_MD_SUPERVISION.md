# Plan — Console d'animation, Supervision : télécharger en .md les contenus de sa cellule

> ✅ **EN PRODUCTION le 2026-10-13** (lots A, B, C et D) : MELMIL `8c35400`, réseau social `e584d33`, presse `3ab3abc`, Console `122b604`. Détail : journal PLEIADE, 13/10, suites 10 et 11.

> Rédigé le 2026-10-13. Sources :
> - demande et arbitrages de l'utilisateur (même jour) ;
> - avis DESIGNER n°106 (`DESIGNER\AVIS\2026-10-13_EXPORT_MD_SUPERVISION\AVIS.md`) ;
> - avis CYBERSECU, conditions **E1 à E15** (`CYBERSECU\MEMOIRE.md` §4 et §9) ;
> - relevé du code de `app-admin`, `app-melmil`, `app-social` et `app-press`.
>
> Règles de chaque lot : essai en local, puis feu vert de l'utilisateur **pour chaque dépôt** avant le push.

## 1. Ce qui est décidé

| Sujet | Décision |
|---|---|
| Qui exporte | Un rôle Console (`admin` ou `operateur`), vérifié côté serveur (E1). |
| Cellule | **La sienne seulement**, tirée du jeton. Si elle est indéterminée (aucune ou deux) : refus, avec le message « cellule indéterminée ». (E2) |
| Périmètre | Ce que la cellule a publié (ses scénarios et les publications en direct de ses animateurs), **plus les réactions** des autres comptes : commentaires et citations. Les filtres ne font que réduire ce périmètre (E3). |
| Niveau de tri | Un Event, une Story lane ou un Incident (arbre MELMIL), ou un scénario. Un niveau inclut tout ce qui est en dessous. « Tout ce que la cellule a publié » est choisi par défaut. |
| Types | Publications, articles, commentaires, citations, reprises de hashtags. La case « Tout » les coche toutes. |
| Hashtags | Les hashtags **lancés** par les contenus choisis, et **tous** les contenus publics de la zone qui les reprennent. |
| Rangement du fichier | `##` Event › `###` Story lane › `####` Incident ; les contenus par ordre chronologique ; les réactions sous le contenu qu'elles visent ; les reprises de hashtags à la fin de l'incident qui a lancé le hashtag. |
| Exclu | Chat et messagerie privés, contenus programmés pas encore parus, contenus supprimés, toute la couche IA, médias (on donne seulement leur nombre) (E4). |
| Origine | **Jamais dans le fichier.** On écrit « scénario n°… » ou « en direct » (E6). |
| Auteurs | Leur nom d'avatar et leur handle fictifs seulement. Jamais de compte de zone (gc/gw/fd), de `sub`, de nom réel ni d'identifiant interne (E7). |
| Texte | Placé dans des blocs neutralisés : `<` et `>` neutralisés, **aucun lien ni image actifs** (les adresses restent du texte), caractères invisibles retirés (E13). Sur ce point, CYBERSECU l'emporte sur DESIGNER, qui proposait des liens « ouvrir ». |
| Fichier | `EXERCICE_<zone>_<cellule>_<périmètre>_<AAAAMMJJ-HHMM>.md`, nom généré par le serveur. L'en-tête et la dernière ligne portent « EXERCICE — DONNÉES FICTIVES — usage animation » ; l'en-tête donne aussi les totaux, l'état complet ou INCOMPLET, l'empreinte et la consigne de conservation (E12). |
| Limites | 5 000 éléments, 5 Mo, 5 000 caractères par texte ; 10 exports par heure ; une troncature est toujours annoncée (E11). |
| Trace | Une ligne au journal de la Console pour chaque export et chaque refus : qui, cellule, filtres, nombres, empreinte (E10). |
| Sur le poste | Dossier dédié sur C:. Jamais sur D:, dans le dépôt, sur une clé personnelle ni chez un agent cloud. Purge en fin d'exercice. Consigne donnée au briefing (E14). |

## 2. Lots

### Lot A — Réseau social (`app-social`)
- `GET /api/service/export-cellule` : clé de zone, GET seul (E8).
  - Paramètres stricts :
    - `cellule` ;
    - fenêtre de 14 jours au plus ;
    - jusqu'à 50 identifiants de scénarios ;
    - codes d'incident et de storyline ;
    - jusqu'à 20 hashtags ;
    - les types demandés.
  - Rend les publications et commentaires dont l'**origine** est cette cellule, filtrés par scénario, incident ou storyline. Y ajoute les **réactions** (réponses, citations de publications et de commentaires), puis les **reprises** des hashtags donnés.
  - Contenu rendu : publics et parus seulement ; texte limité à 5 000 caractères ; ni origine, ni compte de zone ; indicateur `tronque`.
- **Normaliser la cellule d'une publication en direct** d'un animateur. Elle se déduit de ses groupes, comme `celluleDeGroupes`, et ne dépend plus d'un groupe coloré sur la plateforme.
- ⚠ Les gestes antérieurs au 09/10 n'ont pas d'origine : ils ne pourront pas figurer dans l'export.

### Lot B — Presse (`app-press`)
- Au moment de la publication (`publish`), enregistrer l'**origine** que la Console envoie déjà (scénario, cellule, incident, storyline).
- Route `GET /api/service/export-cellule` sur le même modèle : articles, entrées de direct, commentaires publiés.
- Articles anciens, publiés sans origine : on les retrouve par les identifiants que la Console a gardés (`ScenarioItem.remotePostId`).

### Lot C — MELMIL (`app-melmil`)
- `GET /api/service/arbre` : la liste des events, storylines et incidents (identifiants, codes, titres), y compris les storylines et events sans incident. **Jamais le texte du FAM JEMM** (E12).

### Lot D — Console d'animation (`app-admin`)
- **Bouton** « Télécharger les contenus (.md)… » dans l'en-tête de la Supervision. Il est inactif quand le compte n'a pas de cellule, avec la raison affichée.
- **Fenêtre** : un formulaire unique en 4 blocs (cellule affichée ; périmètre, en arbre MELMIL ou en liste de scénarios ; types ; période facultative), un **aperçu chiffré** recalculé à chaque choix, et le bouton « Télécharger 214 contenus ».
  - États prévus : rien à exporter ; export long (progression, avec possibilité d'annuler) ; erreur ; **app injoignable**, avec le choix « Télécharger sans la presse » (le fichier porte alors « INCOMPLET »).
- **Côté serveur** :
  - `POST /api/bff/export-md/apercu` (comptes seulement) et `POST /api/bff/export-md` (le fichier) ;
  - le périmètre combine les scénarios de la cellule (et leurs identifiants distants) et l'arbre MELMIL ;
  - le fichier est généré en mémoire, sans rien écrire sur le disque du serveur ;
  - le journal et les limites (E9 à E11) s'appliquent.
- **Génération du Markdown en fonction pure**, testée sur la matrice E15 : un joueur reçoit 403 ; une cellule vide reçoit 403 ; FORAD ne voit pas GREYCELL ; aucun contenu programmé, de Chat, d'origine ni de compte gc/gw dans le fichier ; un filtre ne fait jamais sortir du périmètre ; les tentatives d'injection sont neutralisées ; une troncature est annoncée.

**Ordre** : C, A, B, puis D. Une fois A et D faits, l'export fonctionne déjà pour le réseau social ; la presse s'ajoute ensuite.

## 3. Réponses de l'utilisateur (2026-10-13)
1. **L'Administration seule** peut exporter une autre cellule que la sienne. Ce choix est journalisé.
2. La mention « **EXERCICE — DONNÉES FICTIVES — usage animation** » est validée.
3. Le **nom de celui qui exporte n'apparaît pas** dans le fichier. Il figure au journal seulement.
