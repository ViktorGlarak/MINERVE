# Avis DESIGNER n°110 — Moteur IA, Réglages : le panneau « Journal et archives »

**Date** : 2026-10-15 · **Demandeur** : utilisateur · **Mise en œuvre** : PLEIADE (`app-ia`, `src/components/ReglagesMoteur.tsx`)

## Constat de l'utilisateur
> « Je n'arrive pas à comprendre à quel bouton est rattaché, ou avec quel bouton fonctionne, "Archiver et vider". »

## Diagnostic
1. **Cinq gestes sans rapport sur une seule rangée** : deux exports (tout, une journée), un champ date, un ménage (archiver et vider) et une suppression définitive. La proximité fait croire qu'ils forment une chaîne (loi de proximité, Gestalt). « Archiver et vider » est collé à « Exporter cette journée », donc on pense qu'il s'y rattache.
2. **Le champ date est coincé entre « tout » et « cette journée ».** On ne sait pas s'il règle les deux exports.
3. **Le geste le plus fréquent n'est pas mis en avant.** L'export, qu'on fait tous les jours, est en bouton secondaire. Le ménage rare est en orange plein, le bouton le plus visible du panneau.
4. **Le texte d'aide parle de l'export, mais sous les cinq boutons.** Et rien ne dit que l'archivage est automatique.
5. **Les archives n'expliquent pas leur contenu** : seulement le journal et les cycles, pas les fiches, le réseau social, le fil ni les opinions.

## Recommandations
Un seul panneau, découpé en **trois blocs titrés**, du geste quotidien au geste rare :

- **R1. « Exporter pour analyse »**, en tête.
  - Une ligne d'état : « En ligne : 136 lignes et 491 cycles depuis le 14/10 à 17:52 ».
  - Deux choix côte à côte, chacun complet en lui-même :
    - « Tout ce qui est en ligne », avec son bouton principal ;
    - « Une journée », avec le champ date **dans** ce choix et le bouton « Exporter le 15/10 ». Le bouton dit la date.
  - L'aide sur le contenu de l'export reste sous ce bloc, raccourcie.
- **R2. « Archives quotidiennes »**, au milieu.
  - Une phrase : « Chaque heure, le moteur range seul ce qui a plus de 2 jours. Une archive ne contient que le journal et les cycles (ni fiches, ni réseau social, ni fil, ni opinions). »
  - La liste des archives, chacune avec un lien « Télécharger ».
- **R3. « Ménage »**, en bas, séparé par un filet, boutons **en contour** (jamais pleins).
  - « Archiver et vider maintenant… » : une ligne d'explication à côté, « range tout le journal en ligne dans les archives et le retire de la base. **Exportez d'abord** si vous voulez l'analyser : l'export suivant serait presque vide. »
  - « Supprimer toutes les archives… (fin d'exercice) », en rouge, avec sa phrase.
  - Les points de suspension annoncent la confirmation.
- **R4. La confirmation dit la conséquence chiffrée** : « 136 lignes et 491 cycles seront rangés dans les archives et retirés de la base. Le prochain export pour analyse n'en contiendra plus. »
- **R5. Le message de résultat s'affiche dans le panneau**, pas en haut de la page hors de vue : « 627 lignes rangées dans l'archive du 15/10. »

## Doctrine
On regroupe par intention, pas par type de contrôle. Un geste destructif se tient à distance des gestes quotidiens et s'explique là où il est. Le bouton le plus visible est celui qu'on utilise le plus, pas le plus dangereux.
