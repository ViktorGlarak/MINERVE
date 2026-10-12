# Avis n°69 — Navigation de PLÉIADE : pourquoi les animateurs se perdent, et quoi faire (2026-10-06)

**Demande utilisateur** : les animateurs de la zone DELATTRE 26 sont perdus à cause de la multitude d'outils et d'onglets. Former DESIGNER sur ce sujet (sources fournies, ingérées en REF-21 à REF-26, doctrine §3.7 règles 27-40) et l'appliquer aux apps existantes (MELMIL, admin…) et futures.

**Méthode** : inventaire de la navigation lu dans le code des 9 apps (libellés exacts, rôles, onglets, boutons, liens entre apps), passé au crible de la doctrine §3.7. ⚠ Aucun test avec des animateurs n'a encore été fait (règle 40) : les gravités sont des estimations d'expert.

## 1. Ce qu'un animateur traverse aujourd'hui

| App | 1er niveau | 2e niveau | Profondeur | Forme de navigation |
|---|---|---|---|---|
| MELMIL | 2 espaces (Planification, Planche JEMM) + pastille Demandes | **11 onglets** en 3 familles (10 pour un GA, 8 en Lecture) + menu « Étape ▾ » + 2 à 4 sélecteurs par onglet | ~6 | segments + onglets |
| Admin | 3 (Tableau de bord, Scénarios, Supervision) | éditeur : 4 onglets + Heure réelle/T+ + Chronogramme/Agenda + zoom + regroupement | ~5 | onglets soulignés |
| EHO | 11 (admin) / 7 (animateur) / 4 (joueur) | Planche/Liste, sections de fiche | 3 | barre latérale |
| Cockpit | **10 commandes d'en-tête de même poids** | mode Layout | 2 | en-tête d'icônes |
| Presse (rédaction) | 3 à 5 onglets | Réglages 5, éditeur 10 panneaux | 3 | onglets |
| Social | 4 à 7 **selon l'habillage** | — | 3 | barre propre à chaque réseau imité |
| Messagerie | 4 icônes + 3 filtres ; Supervision 2 | — | 3 | icônes |
| LEAC | accueil + 8 destinations par contrôle | Paramétrage 6 | 4 | familles Terrain / Équipe / Production |
| Portail | cartes d'apps | page de choix d'instance | 2 | grille |

## 2. Constats (gravité 0-4, Nielsen REF-14)

1. **(4) Les apps sont des îlots** : au moins **6 systèmes de navigation** de formes différentes, **aucun retour au portail**, aucun moyen de passer d'une app à l'autre sans repasser par l'adresse du portail — NN/g « sous-sites mal intégrés » (REF-21), règle 29.
2. **(3) Même mot, plusieurs choses ; même chose, plusieurs mots** — règle 36 :
   - l'unité programmée s'appelle **incident** et **inject** (MELMIL), **item** et **publication** (admin), post / tweet (social) ;
   - le rôle d'animation : « Animation », « Animateurs », « Conduite d'exercice », « GA1 / GA2 » ;
   - « Réglages » ×2 dans MELMIL (onglet de l'atelier ≠ panneau de la planche JEMM), « Configuration », « Paramétrage » ailleurs ;
   - « Journal » et « Supervision » désignent trois choses différentes selon l'app ; « Planche » six.
3. **(3) MELMIL : 11 onglets et 3 chemins vers les mêmes écrans** (onglets + menu « Étape ▾ » + pastille Demandes) ; le choix de groupes s'appelle « Afficher » à un endroit et « Groupes » à un autre — règles 31, 33.
4. **(3) Éditeur de scénario (admin) : bascules empilées sur 4 niveaux** (7 actions d'en-tête → 4 onglets → Heure réelle/T+ → Chronogramme/Agenda → zoom → regroupement), et l'en-tête répété dans la barre compacte — règles 32, 37.
5. **(3) Cockpit : 10 commandes au même poids**, dont des icônes seules et des libellés anglais (Layout, Reset, Export JSON) — règles 6, 36, 37.
6. **(2) Barres de filtres de 11 à 12 commandes** sur une ligne (admin Scénarios, MELMIL Demandes et Écarts) — règle 37.
7. **(2) Menu ≠ titre** : EHO « Planche officielle » → page « Planche relationnelle officielle » ; LEAC « Bilan » → `/tableau-de-bord` ; presse : l'onglet « Rédaction » des Réglages porte le nom de l'espace — règle 30.
8. **(2) Messages de refus qui citent des rôles introuvables** dans le bouclier PLÉIADE (MELMIL : « Animation », « Lecture et demandes » ; messagerie : « Modération », « Administration » au lieu de « Supervision ») — règle 36, heuristique 9.
9. **(2) Petites incohérences de geste** : « Tout déplier / Tout replier » dans un ordre ici, l'inverse là ; « Explorer » ne mène pas au même endroit selon l'habillage social.
10. **(4, défaut)** Social, habillage Instagram : le bouton **« Plus » déconnecte** l'utilisateur (`instagram-layout.ts:80-83`).

> Le **social** imite volontairement de vrais réseaux (charte, Jakob REF-06) : sa navigation par habillage **reste** ; on corrige seulement le défaut n°10 et on s'assure que « Programmés » reste accessible à l'animation quel que soit l'habillage.

## 3. Recommandations, classées par gain pour l'animateur

| # | Recommandation | Gain | Effort | Qui |
|---|---|---|---|---|
| **R1** | **Corrections immédiates** : bouton « Plus » d'Instagram, messages de refus avec les **vrais noms de rôles**, titres de page = libellés du menu, ordre unique « Tout déplier · Tout replier », libellés français du cockpit | moyen, immédiat | ½ j | ARCHITECTE |
| **R2** | **Lexique de zone** (vocabulaire contrôlé, une page) : un mot par notion pour l'unité programmée, les rôles, Réglages / Journal / Supervision / Planche ; puis renommage progressif à chaque passage dans une app | fort, durable | 1 j de lexique (+ au fil de l'eau) | DESIGNER + utilisateur (arbitrage des mots) |
| **R3** | **Barre de plateforme commune** en haut de chaque app : nom de la zone, **« Apps de la zone ▾ »** (passer de MELMIL à l'admin, à EHO… en un clic), retour au portail, compte. La navigation propre à l'app reste dessous, **moins visible** | **le plus fort** : répond aux constats 1 et « où suis-je ? » | 2-3 j (un composant par famille d'apps + une route du portail qui liste les apps de l'utilisateur) | PLEIADE / Xavier (portail) + ARCHITECTE |
| **R4** | **MELMIL : 7 destinations au plus**, choisies par fréquence ; un seul chemin par écran (le menu « Étape ▾ » ne fait plus que changer d'étape) ; « Réglages » de JEMM renommé ; même nom pour le choix de groupes | fort pour les cellules | 1-2 j après l'analyse de tâches | DESIGNER + ARCHITECTE |
| **R5** | **Éditeur de scénario** : une action principale (Lancer / Pause) + « Plus ▾ » (Kit IA, Importer, Exporter, Réinitialiser) ; Heure réelle/T+ et Chronogramme/Agenda déplacés dans un petit menu « Affichage » ; barres de filtres repliées derrière « Filtres (n) » | moyen | 1 j | DESIGNER + ARCHITECTE |
| **R6** | **Aide tirée** : un « ? » par écran qui dit à quoi il sert et quoi faire ensuite ; **checklist de prise en main par rôle** (Administration, Animateurs) sur le portail ; pas de visite guidée | moyen, surtout au premier jour d'exercice | 1-2 j | DESIGNER (textes) + ARCHITECTE |
| **R7** | **Valider pendant DELATTRE 26** : test express d'orientation (captures sans navigation) et observation de **5 animateurs** sur 3 tâches (créer un scénario pour un incident, retrouver une publication, répondre à une demande de produit) ; analyse de tâches d'une journée d'animateur → décide R4 | indispensable avant R4 | 2 h par séance | utilisateur + DESIGNER |

**Ordre conseillé** : R1 (tout de suite) → R2 (lexique à valider par l'utilisateur) → R7 (pendant l'exercice) → R3 → R4 / R5 → R6.

## 4. Pour les apps futures (règles applicables dès la conception)
- Partir d'un **inventaire des tâches** et de leur **fréquence** ; au plus **7 destinations**, 2 niveaux de révélation.
- Poser la **barre de plateforme** dès le premier écran ; reprendre le **lexique de zone**.
- Un geste ponctuel = **parcours guidé**, pas un onglet.
- Mises en page **liste-détail / volet d'appui / flux** (REF-23) plutôt qu'un onglet par vue.
- Prévoir dès le départ le « ? » de chaque écran et les **états vides** qui disent quoi faire.

## 5. Statut
Avis rendu le 2026-10-06. **Rien n'est encore appliqué** : en attente du choix de l'utilisateur sur les recommandations à engager.
