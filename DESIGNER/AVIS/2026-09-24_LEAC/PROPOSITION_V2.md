# Proposition DESIGNER n°2 bis — LEAC « v2 » : fluide, net, professionnel

- **Demande de l'utilisateur** (2026-09-24, soir) : « les boutons ne sont pas très esthétiques… propose quelque chose de beaucoup plus fluide, esthétique, pro ». DESIGNER peut conseiller **sur toute l'étendue de ses capacités, architecture comprise** : repenser des parties de page, en ajouter, en supprimer. Tout se fait **en local d'abord**.
- **Ce qui change de statut** : le parti pris esthétique du 2026-09-17 (« angles vifs, aucune ombre portée ») est **levé** à la demande de l'utilisateur. Ses **exigences fonctionnelles restent**, parce qu'elles viennent du terrain et non du goût :
  - cibles de 48 px ;
  - contraste au soleil (texte secondaire jamais plus clair que `#4A5058`) ;
  - clair par défaut ;
  - mention posée en un appui ;
  - synchronisation toujours visible ;
  - carnet en premier écran (décision du 2026-09-22).

## 1. Le système visuel (tous les écrans d'un coup)

| Élément | Avant | Après | Source |
|---|---|---|---|
| Rayons | 2 px partout | **10 px** pour les cartes, **8 px** pour les boutons et champs, **999 px** pour les pastilles | REF-01 (`radius`) |
| Profondeur | aucune ombre, des filets partout | **cartes posées sur une ombre douce en deux couches**, filets allégés | REF-07 (profondeur, moins de bordures) |
| Boutons | un cadre noir de 1 px, texte de 12 px | trois rôles distincts : **principal** (aplat graphite), **secondaire** (fond blanc, bord léger), **discret** (texte seul) ; texte de 15 px, 48 px de haut | REF-01 (`primary`/`secondary`), Hick |
| Pastilles d'état | cadre de la couleur | **fond teinté** de la couleur, texte foncé de la même teinte | REF-15 (crans 3/11) |
| Champs | cadre gris de 2 px | bord léger, **anneau de focus bleu de 3 px** | REF-13 (2.4.7), REF-01 (`ring`) |
| Titres de rubrique | capitales espacées de 11 px | capitales de 12 px, espacement réduit | REF-07, REF-17 |
| Mentions | cadre et liseré | même geste ; rayon de 8 px, **liseré intérieur** de la famille, choisie = aplat | parti pris §7 conservé |

## 2. L'architecture (ce qu'on repense)

1. **Accueil**
   - Les **contrôles d'abord**, en cartes : badge de statut, fonction tenue, bouton « Ouvrir ».
   - Les 5 grosses tuiles d'administration deviennent **une seule liste « Administration »** en bas, avec une ligne par action : elles pesaient plus lourd que le travail lui-même.
   - Le contrôle de démonstration devient une **carte compacte**.
2. **En-tête d'un contrôle**
   - **Une barre compacte** : retour, intitulé (tronqué proprement), unité, fonction en pastille, **état de synchronisation**.
   - L'intitulé n'est plus répété une seconde fois en sur-titre juste en dessous.
3. **Carnet**
   - La **zone de saisie** en premier, bien visible.
   - Le long paragraphe « ces notes restent sur l'appareil » devient **un encart repliable** (« Où sont gardées mes notes ? »). Seul l'**avertissement d'installation** reste affiché, en encart d'alerte, **quand il s'applique**.
4. **Grilles**
   - Un **en-tête de domaine** : nom en grand, **barre de progression**, sélecteur de domaine.
   - Un **sélecteur segmenté** Liste / Un par un.
   - La recherche, puis un bouton **« Filtres »** qui ouvre les options, avec leur **nombre** quand certaines sont actives.
5. **Bilan**
   - **Trois indicateurs en tête** (Avancement · Note · Label) sur trois colonnes sur ordinateur, empilés sur téléphone.
6. **Navigation** : la barre unique du 2026-09-24 est conservée. Elle passe au même style (pastille active arrondie, icône et libellé).

## 3. Ce qu'on ne touche pas

- les règles métier ;
- le calcul ;
- la synchronisation ;
- les données ;
- les chiffres interdits sur l'écran de notation (règle 18).
