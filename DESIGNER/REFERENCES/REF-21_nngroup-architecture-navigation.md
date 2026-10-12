# REF-21 — Nielsen Norman Group : architecture de l'information et navigation

- **Fournie par l'utilisateur le** 2026-10-06 (lien `information-architecture-3-steps`, **404** : remplacé par l'IA Study Guide et ses articles).
- **Nature** : articles du cabinet de référence en ergonomie, accès libre, droits réservés (on cite, on ne recopie pas).
- **Lu** : `/articles/ia-study-guide/`, `ia-vs-navigation`, `top-10-ia-mistakes`, `navigation-you-are-here`, `local-navigation`, `menu-design`, `vertical-nav`, `flat-vs-deep-hierarchy`, `progressive-disclosure`, `tabs-used-right`, `card-sorting-definition`, `tree-testing`, `simplicity-vs-choice`, `dashboards-preattentive`, `onboarding-tutorials`, `help-and-documentation`.

## À retenir
1. **L'architecture de l'information (IA) précède la navigation** : l'IA est l'ossature (inventaire, regroupement, vocabulaire contrôlé), la navigation n'en est que la partie visible. Elle se travaille en tableur et en schéma, pas en maquette.
2. **Trois questions d'orientation** : où suis-je, d'où viens-je, où puis-je aller. Combiner plusieurs signaux (entrée active, titre, URL lisible, fil d'Ariane). Les signaux sont presque toujours **trop discrets** : ce qui semble trop voyant au concepteur passe inaperçu.
3. **Test express** : montrer une page sans sa navigation et demander « Où êtes-vous ? Comment le savez-vous ? ».
4. **Navigation globale (constante) et locale (voisinage)** : la locale ne doit **jamais être plus visible** que la globale.
5. **Menus** : pas de hamburger sur grand écran ; dans une application, **navigation principale à gauche** ; emplacement courant toujours indiqué ; ouverture au clic ; pas de cascade au-delà d'un niveau ; l'icône **complète** le libellé, ne le remplace pas.
6. **Navigation verticale à gauche** : tient **13 entrées et plus**, absorbe la croissance ; mot-clé en tête du libellé, entrées rares en bas.
7. **10 erreurs d'IA**, dont : sous-sites mal intégrés (**= nos apps multiples**), navigation incohérente (entrées qui apparaissent et disparaissent), trop de techniques de navigation mélangées, libellés inventés.
8. **Révélation progressive** : peu d'options d'abord, le reste à la demande ; **au-delà de 2 niveaux, l'utilisabilité chute** ; le premier niveau se décide par **fréquence d'usage** (analyse de tâches) ; le lien vers le niveau 2 est visible et bien nommé.
9. **Onglets** : peu, sur une ligne, libellés de 1-2 mots, le plus utilisé en premier et sélectionné par défaut, ≥ 2 indices de sélection ; **à proscrire pour comparer** deux contenus.
10. **Valider** : tri de cartes (30-50 cartes, ≥ 15 participants) puis test d'arborescence (taux de réussite, caractère direct).
11. **Chaque option coûte** un effort ; tableau de bord **opérationnel** = temps réel (notre cas) : longueurs et positions, pas de camembert ni de jauge.
12. **Aide** : les tutoriels en cartes successives sont « dramatically overused » ; préférer l'aide **tirée** (contextuelle, rappelable) à l'aide **poussée**.

## Ce que ça change pour nos projets
- Les apps de PLÉIADE sont des **sous-sites mal intégrés** : chaque app a sa navigation, son vocabulaire, ses onglets. Il faut une **navigation globale commune** et un « vous êtes ici » franc.
- Décider de ce qui est visible d'après la **fréquence des tâches** des animateurs, pas d'après l'ordre de création des fonctions.
- Avant toute refonte lourde : inventaire, tri de cartes avec des animateurs, test d'arborescence.
