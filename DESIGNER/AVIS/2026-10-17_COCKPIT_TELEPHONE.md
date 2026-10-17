# Avis DESIGNER n°117 — 2026-10-17 — Le Cockpit sur téléphone (app-cockpit, sous 768 px)

> **Constat utilisateur** : Cockpit « totalement bugué » sur téléphone. **Cause** : en-tête et colonnes à largeurs fixes → la page s'affichait en 778 px sur un iPhone de 390 px (dézoom). **Version téléphone** codée sous 768 px seulement (ordinateur inchangé) : en-tête sur deux lignes ; Situation en cartes (une par catégorie, une ligne par canal) ; À traiter en « liste puis lecture » avec 3 listes déroulantes ; Projection hors périmètre (grand écran).
> Revue faite sur captures iPhone 13 (390 px), iPhone SE (320 px) et ordinateur (non-régression), environnement local avec contenus fictifs.

## Verdict : validé avec réserves (10 corrections, appliquées dans le même lot)

**Ce qui est juste** : le choix des formes (cartes, listes déroulantes, liste → lecture → retour : règles 15 et 38) ; listes en 16 px (avis n°116) ; canaux hors règle masqués dans les cartes ; « ‹ Retour à la liste » collant, ~45 px ; lecture plein écran confortable (règle 26) ; ordre de la Situation.

## Corrections (par gain)
1. **Cibles tactiles ≥ 44 px** (règle 12, WCAG 2.5.5) sur téléphone : « + », « ⋯ », choix de vue, onglets (`py-3 text-[14px]`), listes déroulantes (`h-11`), « Tout marquer vu », Vu / À suivre / Signalé (`min-h-11 px-4`). Ordinateur inchangé (`md:`).
2. **Bandeau « Ce qui a changé »** : « J'ai fait le point » débordait de son cadre de 30 px ; petits titres en capitales espacées sur 2-3 lignes ; marge 26 px ≠ 12 px des cartes. → une ligne « Ce qui a changé · depuis HH:MM (il y a …) » en 12 px sur téléphone, bouton pleine largeur `h-11` sous le résumé, `mx-3 md:mx-[26px]`.
3. **Champs des fenêtres en 13 px → zoom iOS** (avis n°116) : 16 px minimum sur téléphone pour tout champ ; jamais de blocage du zoom.
4. **« Hors catégories / Total zone »** illisible (chiffres sans en-tête, légende pâle en bas) (règle 7, Nielsen 6) → une ligne par canal, colonnes « hors cat. » et « total », en-tête 12 px.
5. **Libellés de canaux** en 11 px capitales espacées coupés sur 2 lignes (règles 26, 21) → `w-[112px] whitespace-nowrap text-[13px] text-ink-soft`, sans capitales ; tendance en 13 px ; « fiche › » 12 px.
6. **État du système par la couleur seule** (règles 10, 25 ; avis n°108) → sur téléphone, « ● direct » à droite des onglets, `role="status"`, « relu il y a N s » en alerte au-delà de 40 s.
7. **En-tête sur 3 lignes à 320 px** (règles 5, 32) → mot « Cockpit » réduit sur téléphone et masqué sous 360 px ; choix de vue `max-w-[110px]`.
8. **Haut de liste redondant** (règles 5, 39) → titre gras masqué sur téléphone (les listes le disent) ; « Trié par importance » en `<details>` (une aide qu'on va chercher, accessible au toucher).
9. **Focus et état des bascules** (règle 11) → `aria-pressed` sur Vu / À suivre / Signalé ; focus sur « ‹ Retour » à l'ouverture, retour du focus sur la ligne lue au retour.
10. **Petits textes de la liste** (règles 26, 21) → étiquette de canal 11 px, heure et réactions 12 px `text-ink-muted`, nom et texte 14 px sur téléphone.

## Peut attendre
Vocabulaire « Vue » / « Toutes catégories » (aussi sur ordinateur, règle 36) ; barre de plateforme absente du Cockpit (audit du 15/10) ; « nouveau » des tendances en pastille ; lien Projection masquable sur téléphone ; **à vérifier sur un vrai iPhone** : volet de fiche et fenêtre « Nouvelle catégorie » (débordements, focus, bouton de fermeture ≥ 44 px).

## Règles générales qui en sortent
- Sur téléphone, **pas d'étiquette en capitales espacées sous 12 px**.
- **Pas de hauteur fixe sur un bouton dont le texte peut passer sur deux lignes.**
- Un écran d'outil pensé pour l'ordinateur se décline sur téléphone par **changement de forme** (tableau → cartes, rail → listes, colonnes → liste puis lecture), jamais par réduction.
