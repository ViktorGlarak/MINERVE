# Avis DESIGNER n°3 — app-melmil v2 : architecture, lisibilité, accessibilité, responsive

- **Demande de l'utilisateur** (2026-09-24, soir) : « revoir toute l'architecture de MELMIL pour avoir une appli fluide et bien lisible […] tout comme pour LEAC », en prenant bien en compte le **responsive : téléphone, tablette et ordinateur**. **En local d'abord.**
- **Mesures de départ** (version `2026-09-24.4`, instance locale avec le nom de zone du serveur `delattre-26`, émulation iPhone 13, iPad Mini et ordinateur 1440 × 900) :
  - téléphone :
    - le **sélecteur d'espace sort de l'écran**, on ne peut plus changer d'espace ;
    - le tableau des incidents **déborde de 220 px** ;
    - la page commence à **370 px** (onglets sur 6 lignes) ;
    - la barre d'outils de la planche empile 5 gros boutons, dont « Vider » au même rang que les autres ;
    - la planche en grille n'affiche qu'**un jour et demi** ;
  - tablette : correct, mais les en-têtes sont hauts ;
  - ordinateur : correct (refonte n°1 du matin).
- **Ce qu'on garde** :
  - les **deux espaces** et leurs teintes (ambre pour la planification, bleu pour JEMM) ;
  - le parcours GT1 → GT2 → GT3 → Exercice ;
  - les onglets en familles ;
  - le **tableau des incidents** et sa fiche latérale ;
  - la grille EXCON et les comptes rendus à l'identique ;
  - la planche **grille** sur tablette et ordinateur ;
  - le choix Clair / Classique.

## Recommandations

| # | Proposition | Téléphone | Tablette | Ordinateur | Source |
|---|---|---|---|---|---|
| **R1** | **Système visuel v2**, le même que LEAC : rayons, ombres douces, boutons en 3 rôles (principal / secondaire / discret) plus « danger », pastilles teintées, anneau de focus, champs arrondis | ✔ | ✔ | ✔ | REF-01, REF-07, REF-13 |
| **R2** | **Bandeau responsive** : le sélecteur d'espace est **toujours visible**, avec des libellés courts sur téléphone ; le compte (nom, déconnexion, thème) passe dans **un menu** sous 900 px ; le nom de zone se tronque, puis disparaît sous 420 px | menu, libellés courts | menu | tout visible | Nielsen 1 et 3, Fitts |
| **R3** | **Barre d'outils de la planche JEMM** : « Importer » en principal, « Réglages » en secondaire, le reste dans **« Plus ▾ »** (exporter, restaurer, réinitialiser, purger, et **« Vider » en rouge, isolé en bas du menu**) | ✔ | ✔ | ✔ | Hick ; prévention des erreurs (Nielsen 5) |
| **R4** | **Planche en « Liste par jour »** sur téléphone : un jour par bloc (« MAR 06 OCT · D+1 »), incidents triés par heure, liseré à la couleur de la storyline ; un clic ouvre la fiche. Le sélecteur devient Liste · Clair · Classique | **par défaut** | au choix | au choix | Jakob (agenda), REF-17 |
| **R5** | **En-tête de planification compact** : sur téléphone, seule l'étape en cours est affichée, à côté de « Changer d'étape » | ✔ | — | — | Hick |
| **R6** | **Onglets sur une seule ligne défilante** sur téléphone, sans les titres de famille | ✔ | — | — | REF-19 |
| **R7** | **Incidents en cartes** sur téléphone : le tableau se replie ligne par ligne (code et heure, sujet, statut) ; la fiche s'ouvre en plein écran | ✔ | tableau | tableau | WCAG 1.4.10 |
| **R8** | **Filet anti-débordement**, comme LEAC : mots longs coupés, `select` et `fieldset` bornés, grilles CSS rétrécissables, `overflow-x` bloqué sur téléphone | ✔ | ✔ | — | WCAG 1.4.10 |

**Contrôle de réussite** : 0 débordement de page, sur 4 téléphones × 2 tailles de texte × toutes les pages, **avec le nom de zone du serveur**.
