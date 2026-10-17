# Avis DESIGNER n°120 — 2026-10-17 — Audit téléphone de toutes les applications PLÉIADE

> **Demande utilisateur** : « Fais une analyse de toutes les applications pour le responsive design sur téléphone, il y a encore des applications avec des problèmes qui ne nous permettent pas de voir correctement sur téléphone. »
> **Méthode** : 5 relectures en parallèle, en lecture seule, règles des avis n°116 à n°119. Rendu réel Playwright (iPhone SE 320, 375, iPhone 13 390, iPad Mini 768) sur copies jetables (`git archive` d'origin/main), avec les modes de développement documentés et des contenus fictifs ; analyse du code là où le rendu demandait des identifiants. Aucun dépôt modifié. Captures : scratchpad de la session, `audit-mobile\`.
> Versions auditées : admin 97fb528 · ia 31cf78f · melmil 8c35400 · eho 314e35d · press 93b3ae1 · leac 149e8c8 · social 616d616 · messagerie 0733855 · cockpit 6056df1 · portail 142d735/c30414d.

## Synthèse

| Appli | Verdict téléphone | Bloquants | Ampleur |
|---|---|---|---|
| Console d'animation (admin) | Consultation possible, travail principal impossible | 8 | Gros |
| Moteur IA (ia) | Inutilisable (carte, onglets, Parc) | 4 | Moyen (carte = gros morceau) |
| Serveur de fichiers (webserver) | Inutilisable (débordement, aucune action au doigt) | 2 | Gros |
| Réseau social, habillages X / Facebook / Instagram / YouTube | Cassés (standard corrigé n°118) | 5 | Moyen à gros |
| Messagerie, supervision | Inutilisable (825 px) ; écran joueur bon | 1 | Moyen |
| Presse | Public presque bon ; rédaction dézoomée | 3 | Petit (public) + moyen (rédaction) |
| Portail de zone | Bon au téléphone ; cassé tablette/ordinateur dès 7 titres de presse | 1 | Petit |
| MELMIL | Bon sauf Déroulé | 1 | Moyen |
| Cockpit | Bon sauf « Nouvelle catégorie » et Reporting | 1 | Petit à moyen |
| eho | Bon | 0 | Petit |
| LEAC | Le plus abouti ; écarts à sa règle des 48 px | 0 | Moyen |
| Connexion Keycloak (thème) | Zoom iOS à l'entrée de la zone | 0 (gênant fort) | Petit |
| WordPress | Rien dans le dépôt (thème de l'image) | 0 | — |

## Défauts transversaux (une correction, plusieurs applis)
1. **Barre PLÉIADE commune (`barre-zone.css`)**, identique dans ia, melmil, admin, cockpit, messagerie, eho, presse, leac : le menu « Apps de la zone » (`left:0; min-width:280px`) sort de l'écran ou élargit la page ; lignes de 25 px, bouton de 22 px. → sous 640 px, panneau du bas, lignes de 44 px. Corriger à la source puis recopier partout.
2. **Champs sous 16 px (zoom iOS)** presque partout : thème PLÉIADE `--text-control: 13px` (admin, ia, cockpit-supervision, messagerie-supervision, presse-rédaction), MELMIL 14 px (formulaire joueurs `/demandes` compris), eho 14 px, social racine 14 px (« Répondre… » à 11,9 px, zone d'écriture 13,3 px, Chat 14 px), LEAC 12-14 px, Keycloak 13 px, presse publique 13,6 px. → règle globale `@media (max-width:767px){input,select,textarea{font-size:16px}}` dans chaque thème.
3. **En-têtes à onglets qui ne passent pas à la ligne** (admin 184-204 px de haut, ia ~410 px de large, presse-rédaction 477 px, messagerie-supervision 828 px, melmil 9 onglets dont 6 cachés) → sous 640 px, nom de l'appli + sélecteur « Vue ▾ » en panneau du bas ; compte et déconnexion dans un menu.
4. **Bulle d'aide « ? »** (`AideEcran` / `.ae-bulle`, 360 px accrochée à gauche) : élargit la page (eho 455-525 px, admin, presse). → panneau du bas ou `position:fixed; inset-inline:16px`, « ? » de 44 px.
5. **Fenêtres en `vh`, bouton Fermer de 28 px** (`Modal.tsx` partagé) → `dvh`, 44 px, plein écran sous 640 px.
6. **Capitales espacées sous 12 px** (sur-titres, « Exercice · non classifié », pastilles) → 12-13 px, casse normale sur téléphone.
7. MELMIL : le filet `overflow-x: clip` **cache** les débordements au lieu de les corriger.

## Bloquants par appli (détail des relectures)
- **admin** : en-tête collé 184-204 px ; éditeur 591 px (onglets) ; barre compacte posée à `top:55px` sur l'en-tête, boutons hors écran ; Arbre sans avatar ni texte (grille fixe) ; Timeline sans piste ; fenêtre de publication coupée ; Supervision 702 px (6 cases sur une ligne) ; Tableau de bord `minmax(380px,1fr)`.
- **ia** : carte — fausse panne « assertion failed » sous 391 px (marge de cadrage 330 px) et 30 s de « Chargement… » ; panneau non repliable (bouton recouvert par « Fond de carte »), carte visible ~40 % ; barre d'onglets ~410 px ; Parc en tableau de 7 colonnes (709 px).
- **webserver** : vue grille par défaut à 585 px (`repeat(2,1fr)` + `nowrap`) ; ouvrir/télécharger au double-clic, renommer/supprimer au clic droit — rien au doigt. Hors téléphone : la page lit `isDir`/`mtime`, le serveur envoie `type`/`modified` (dossiers affichés comme fichiers, dates « — ») ; titre `cfg.name` vs `appName` ; accents manquants.
- **social** : YouTube 522 px sans menu ; X — Chat réduit à la barre (même défaut que `.sur-chat` corrigé en n°118) ; X / Facebook / Instagram — « Au nom de » inaccessible, bouton « Choisir un avatar » sans effet (panneau seulement dans l'habillage standard) ; Facebook 376 px à 320 et plus d'accès au Chat ; X sous 600 px sans « Publier » ni déconnexion.
- **messagerie** : supervision (4 écrans) à 825-828 px (en-tête sur une ligne, journal en grille fixe, tableaux).
- **presse** : menu Rubriques coupé à gauche (Quotidien, Magazine) ; tableau d'article qui élargit la page (tous habillages) ; habillage BC1 à 367 px.
- **portail** : section Presse `min-width` = page de 1 378 px sur iPad, 1 592 px sur écran 1 280 dès 12 titres (`portail.ts:236-238`).
- **melmil** : Déroulé — frise réduite à 10-85 px sous 640 px.
- **cockpit** : fenêtre « Nouvelle catégorie » à 429 px dans un cadre de 350.

## Ordre de correction proposé
1. **Petits correctifs à fort effet** : portail (1 ligne), barre PLÉIADE commune, règle 16 px dans chaque thème, thème Keycloak (16 px, marges, boutons 48 px), presse publique (~15 lignes CSS), eho (onglets joueur `grid-cols-4`, bulle d'aide), cockpit « Nouvelle catégorie », webserver débordement (`minmax(0,1fr)`).
2. **Social, 4 habillages** : rendre commun le dispositif n°118 (barre du haut, panneau du bas, Chat une colonne). Avant : savoir quels habillages servent en zone (variable `LAYOUT`).
3. **Supervision de la messagerie** et **rédaction de la presse** (en-têtes, cartes, champs).
4. **Moteur IA** : en-tête et onglets, Parc et Réglages en cartes, puis carte en version téléphone (plein écran, barre de 3 boutons, panneaux du bas, cadrage borné).
5. **Console d'animation** : coquille et débordements, puis éditeur (forme téléphone). Décision utilisateur préalable : éditer un scénario sur téléphone, ou seulement consulter et piloter (Vérifier, Pause, publier une non partie) ?
6. **MELMIL Déroulé** en liste chronologique ; **LEAC** cibles 48 px, champs 16 px, décalage de la barre latérale, en-tête de grille allégé ; **webserver** interaction tactile (bouton « ⋯ » + panneau du bas).

## Règle générale
Une correction téléphone se vérifie **sur tous les écrans d'une appli, écrans secondaires et habillages compris** (supervision, rédaction, réglages, fenêtres) — et un composant partagé (barre PLÉIADE, `Modal`, bulle d'aide, thème) se corrige **à la source**, puis se recopie partout.
