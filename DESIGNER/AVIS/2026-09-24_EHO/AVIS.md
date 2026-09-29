# Avis DESIGNER n°4 — eho (Environnement humain des opérations)

> **Date** : 2026-09-24 · **Demande** : analyser eho et proposer, **sans coder**, ce qu'il faudrait changer pour une app plus fluide et utilisable par tous, du téléphone à l'ordinateur (même démarche que LEAC et MELMIL).
> **Version examinée** : `eho` `main` = `aa791a4` (`2026-09-24.1`), en local sur le port 3001, comptes `anim_test` (animation) et `joueur_test` (joueur).
> **Méthode** : 13 écrans × 3 tailles (iPhone 13, iPad Mini, 1440 px), mesures automatiques (débordements, largeur utile, taille des cibles), passage de la grille §3.6 (Nielsen, WCAG 2.2 AA, hiérarchie), lecture du code pour les points invisibles à l'écran. Captures dans `captures\`.
> ⚠ **DESIGNER contribue, ne tranche pas** : les choix fonctionnels de Xavier et de PLEIADE priment.

> ## ✅ Suite donnée — le 2026-09-24 (soir), en local
> L'utilisateur a validé l'avis et demandé sa mise en œuvre **en local**, **plus** une exigence nouvelle : à **~3 500 avatars (DE LATTRE 26)**, la plupart des pages « buguaient » sous la charge → **charger les avatars par groupe**.
> - **Tout est appliqué** sur `eho`, branche locale **`refonte-v2`** : `7263464` (charge), `f3bece5` (R1–R11), `f67be82` (garde de la nouvelle route). Version `2026-09-24.2`. **Non poussé.**
> - **Correctifs de l'avis, découverts en codant** :
>   - **P4 était en partie faux** : la fiche d'un avatar proposait DÉJÀ la liste des zones. Il existait donc une alternative clavier au glisser pour la zone. Ce qui manquait : la **rubrique** et la **sélection multiple**. C'est ce qui a été ajouté (« Sélectionner » + « Ranger dans pays › rubrique »).
>   - **« Appliquer un modèle » demandait déjà de TAPER le code du modèle** (bonne pratique). Seul le style du bouton a changé (secondaire).
>   - **Cause de fond des cadres noirs** : Tailwind 4 donne aux bordures la couleur du texte. C'est corrigé dans `@layer base`.
> - **Mesures à 3 500 avatars** (CPU ×4, réseau type VPN) — trombinoscope 9,1 s / 8,4 Mo / saisie 3,4 s → **2,2 s / 44 Ko / 0,37 s** ; Mon EHO gel 2,0 s → **0,2 s**, données 2,3 Mo → **0,76 Mo** ; planche relationnelle : taper ne redessine plus le plan (tâches longues 291 → 50 ms).

---

## 1. Ce qui marche déjà — à garder

- **Le trombinoscope et Mon EHO** ont une vraie identité : un bandeau par pays à sa couleur, des rubriques, des cartes avec portrait, une légende en tête (★ STARTEX, ● fiche rédigée).
- **Le Comparatif** est l'écran le plus réussi : officiel à gauche, lecture du joueur à droite, écart souligné. C'est exactement la bonne forme (REF-07 : la forme de la donnée parle d'elle-même).
- **Le menu latéral se replie en icônes** et s'en souvient.
- **Sécurité** : les pages et les API sont gardées séparément, ce qui est rare et précieux.

## 2. Les problèmes, par gravité (0 à 4, Nielsen)

| # | Gravité | Problème | Où | Mesure |
|---|---|---|---|---|
| P1 | **4** | **Mode sombre à moitié fait** : sur un poste réglé en sombre (fréquent sous Windows), le titre, les libellés, les champs et les boutons deviennent **blanc sur blanc**, donc illisibles. Seul le fond de page suit le réglage du système. | toutes les pages | `captures\ordi_sombre_import.png` |
| P2 | **4** | **Au téléphone, le menu garde 256 px** sur 390 : il reste **134 px** pour le contenu. Mon EHO et la planche sont inutilisables ; les titres se cassent mot par mot. | toutes les pages | `tel_mon-eho.png`, `tel_graphe.png` |
| P3 | **3** | **Tableaux coupés sur tablette et téléphone** : dans Avatars (liste), les colonnes Groupes, Statut et Actions sont **hors d'atteinte**, sans défilement (345 px de trop sur iPad, 661 sur iPhone). Même chose pour Modèles (407 / 628 px). | Avatars, Modèles | `tab_users.png` |
| P4 | **3** | **Ranger un avatar ne se fait qu'en le glissant** (glisser-déposer du navigateur). Au doigt sur iPhone, ça ne marche pas ; sur tablette, c'est aléatoire ; au clavier, c'est impossible. Pareil pour tirer un lien sur la planche. WCAG 2.2 **2.5.7** (AA) exige une alternative sans glisser. | Mon EHO, EHO GT, planches | code `planche.tsx`, `graphe.tsx` |
| P5 | **3** | **Planche relationnelle difficile à prendre en main** : un pavé d'aide de 12 lignes en 11 px au-dessus de la liste ; à l'ouverture, la planche officielle est **dézoomée pour tout montrer**, donc les cartes sont illisibles ; la mini-carte couvre le coin ; « Enregistré » ressemble à un bouton grisé et non à un état. | Planche officielle, Planche joueur | `ordi_planche-officielle.png` |
| P6 | **2** | **Tableau de bord technique** : « Dernières actions » affiche du **JSON brut** et des codes (`template_applied`, `bulk_import`) ; chaque chiffre est écrit deux fois (pastille « 453 » + « 453 ») ; « Activité récente : 10 » ne dit pas sur quelle période. | Tableau de bord | `ordi_dashboard.png` |
| P7 | **2** | **Actions destructrices partout et mal signalées** : un « Supprimer » rouge sur chacune des 453 lignes et des 58 cartes ; « Appliquer… » (qui **remplace toute la base**) a la couleur de l'action principale, comme une action anodine ; les 8 confirmations passent par la fenêtre native du navigateur, sans dire ce qui sera perdu. | Avatars, Groupes, Modèles | `ordi_users.png`, `ordi_modeles.png` |
| P8 | **2** | **Tout est indigo** (60 emplois) : les étiquettes de groupe sont toutes de la même couleur, alors que l'information clé est le **pays ou le camp**. Les couleurs de pays du trombinoscope ne sont pas reprises ailleurs. Les 58 groupes sont 58 cartes identiques en capitales, sans recherche ni regroupement par pays. | Avatars, Groupes | `ordi_groups.png` |
| P9 | **2** | **Petits textes et petites cibles** : 29 endroits à 8-11 px (sous-titres de cartes, aides) ; 74 cibles sur 92 font moins de 24 px dans Avatars, et 174 sur 186 dans Groupes (liens texte « Modifier · Camps · Supprimer »). | Avatars, Groupes, cartes | mesures |
| P10 | **1** | **Pages interminables** : le trombinoscope fait 17 000 px sur ordinateur et **77 000 px** au téléphone, sans moyen de sauter à un pays ; dans Mon EHO, 391 cartes « À classer » en tête avant le moindre pays. | Trombinoscope, Mon EHO | mesures |
| P11 | **1** | **Écran de connexion** : « Se connecter via Keycloak » ne parle pas à un joueur, et la zone d'exercice n'y est pas nommée. | Connexion | `login.png` |
| P12 | **1** | **Pas de système** : aucune couleur nommée par rôle ; la police déclarée est Arial alors qu'Inter est chargée (restes du gabarit Next.js). C'est la cause de fond de P1, P8 et P9. | globals.css | code |

## 3. Propositions (sans code), par lots

### Lot 1 — Rendre eho utilisable partout *(≈ 1 jour)*

**R1 · Corriger le mode sombre** *(P1 — quelques minutes)*. Tout de suite : retirer le bloc qui assombrit seulement le fond, pour que l'app reste claire sur tous les postes. Plus tard (R9), soit un vrai thème sombre complet, soit pas de thème sombre du tout. *(REF-01 : un mode sombre redéfinit **tous** les mêmes noms, pas un seul.)*

**R2 · Une navigation par taille d'écran** *(P2)* :
- **Téléphone** : une barre fine en haut (logo, zone, compte). Le joueur n'a que **3 entrées** (Mon EHO, EHO GT, Planche), qui tiennent dans une **barre d'onglets en bas**, à portée de pouce, comme LEAC. L'animateur a 9 entrées : elles passent dans un menu qui s'ouvre par-dessus la page.
- **Tablette** : le menu replié en icônes **par défaut**.
- **Ordinateur** : inchangé.
*(Fitts REF-06 ; Jakob : c'est le schéma de toutes les apps mobiles.)*

**R3 · Les tableaux deviennent des cartes sous 1024 px** *(P3)*. Chaque avatar sur une carte : nom et identifiant, pays en pastille de couleur, 2-3 groupes (« +2 » pour le reste). La colonne Email disparaît de la vue par défaut, et le statut « Actif » ne s'affiche **que s'il y a une exception** (« Inactif »). Même traitement pour Modèles. *(Déjà fait et validé sur MELMIL v2, R7.)*

### Lot 2 — Toucher, clavier, planches *(≈ 3-4 jours)*

**R4 · Ranger sans glisser** *(P4 — accessibilité, obligatoire en WCAG 2.2 AA)*. Un bouton **« Ranger dans… »** sur chaque carte ouvre un choix pays, puis rubrique. Une **sélection multiple** permet de « Ranger ces 12 cartes dans Arnland › Militaire ». Le glisser reste pour la souris. Sur la planche, **« Relier à… »** depuis le menu d'une carte crée un lien sans tirer de pastille. C'est aussi le vrai gain de **fluidité** : ranger 391 avatars un par un à la souris est long, et la sélection multiple divise ce temps.

**R5 · Une planche relationnelle qu'on comprend en 10 secondes** *(P5)* :
- L'aide devient un bouton **« ? Comment faire »** (3 gestes illustrés), montré d'office au premier passage seulement.
- À l'ouverture, **zoom lisible** centré sur le groupe le plus fourni plutôt que « tout montrer ».
- La mini-carte est masquée par défaut sur petit écran.
- « Enregistré » devient un **état** (✓ Enregistré · il y a 5 s), et non un bouton *(Nielsen 1, règle 25)*.
- **Au téléphone** : un mode **consultation** (liste des liens de chaque carte : « Franz Olamao → conseille → Voichek Ribiki ») plutôt qu'un plan à éditer au doigt sur 390 px.

**R6 · Des actions destructrices rares et claires** *(P7)* :
- « Supprimer » quitte les 453 lignes et passe dans la fiche de l'avatar ou dans un menu « ⋯ ».
- « Appliquer ce modèle » devient un bouton secondaire. Sa confirmation dit **ce qui sera remplacé** (« 453 avatars et 58 groupes seront remplacés. Une sauvegarde sera faite : `…json` ») et demande de **taper le code du modèle** pour valider.
- Les 8 fenêtres natives sont remplacées par une vraie fenêtre de confirmation accessible : focus piégé, `Échap`, retour au bouton d'origine *(REF-02 Radix AlertDialog, règle 11)*.
- *(Règle 20 : une seule couleur d'alerte, rare.)*

### Lot 3 — Lisibilité et système *(≈ 3-5 jours)*

**R7 · Un tableau de bord qui parle français** *(P6)*. Des phrases à la place du JSON : « **anim_test** a appliqué le modèle *SKOLKAN PERSONA 21.09.26* — 453 avatars remplacés, sauvegarde faite · 21/09 17:04 », avec une icône par type d'action. Les chiffres ne s'écrivent qu'une fois, avec leur période (« 10 actions ces 7 derniers jours »). Deux raccourcis utiles en tête : « Joueurs qui ont commencé : 1 » et « Écarts à examiner : 0 ».

**R8 · La couleur porte le pays et le camp** *(P8)*. Les couleurs de pays du trombinoscope sont reprises sur les étiquettes, les groupes et la planche ; l'indigo est réservé à l'action principale. La page Groupes est **regroupée par pays** (ARN, BOT, MER…), avec recherche, compteur par pays et noms en casse normale. Le camp est toujours doublé d'un mot ou d'un symbole, jamais la couleur seule *(règle 10)*.

**R9 · Un petit système, comme LEAC et MELMIL v2** *(P9, P12)* :
- des couleurs nommées par rôle (surface/texte, action principale, danger, bordure, focus) ;
- une échelle typographique : 12 px minimum pour le secondaire, 14-16 px pour le courant ;
- des cibles de 24 px au moins, 44 px au doigt ;
- Inter déclarée pour de bon ;
- un anneau de focus visible.

eho garde **son** identité : la décision « pas de thème PLÉIADE unifié » est respectée. On reprend la **méthode**, pas la charte.

**R10 · Se repérer dans les longues pages** *(P10)*. Une rangée de **pastilles pays collantes** en haut du trombinoscope et de Mon EHO (« Mercure 110 · Arnland 146 · … ») pour sauter directement à un pays. Un filtre **« À classer seulement »** et un compteur « reste à classer » par pays. Les cartes s'affichent au fil du défilement : 470 cartes d'un coup alourdissent la page, surtout au téléphone.

**R11 · Connexion** *(P11)*. « Se connecter », le **nom de la zone** en sous-titre, et une ligne d'aide : « Utilisez l'identifiant fourni pour l'exercice ».

## 4. Ordre conseillé

1. **R1** (mode sombre) : immédiat, quelques minutes. Aujourd'hui, un poste en mode sombre ne peut pas utiliser eho.
2. **R2 + R3** : eho devient utilisable au téléphone et à la tablette.
3. **R4** : le toucher et le clavier ; c'est aussi le plus gros gain de temps pour les joueurs.
4. **R5**, puis **R6**.
5. **R7, R8, R11** : lisibilité.
6. **R9, R10** : le socle, qui évite que les défauts reviennent.

**Critère de réussite** (même mesure que MELMIL v2) : 0 débordement et 0 colonne inatteignable sur 4 téléphones × 2 tailles de texte, iPad et 1440 px ; un avatar rangé **sans glisser**, au doigt comme au clavier ; toutes les pages lisibles sur un poste en mode sombre.

## 5. Points à trancher avec l'utilisateur ou avec Xavier

- **eho appartient au dépôt de Xavier** (organisation `cecpc-pleiade`) : faut-il lui soumettre cet avis avant d'y toucher ?
- **Planche au téléphone** : consultation seule (proposé), ou édition complète au doigt ?
- **Thème sombre** : le faire complet, ou y renoncer ?
