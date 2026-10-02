# Avis n°28 — Lier un scénario de l'admin à un incident MELMIL

> **Date** : 2026-10-02 · **Demandeur** : l'utilisateur (« quelque chose de très ergonomique et visuel ») · **Écrans** :
> - `app-admin` : création d'un scénario, liste, fiche d'un scénario ;
> - `app-melmil` : carte de la planche, fiche d'incident (planification), détail d'une carte.
>
> **Statut** : ✅ en ligne le 2026-10-02 (admin `7d6d96f`, MELMIL `c27d368`, version `2026-10-02.4`).
> Suite de l'avis n°27 : le rangement par le code tapé dans le nom reste en **secours**.

## Décisions de l'utilisateur (qui priment)

- Choisir l'incident est **obligatoire** à la création.
- Dans MELMIL, le bouton affiche **le nombre de scénarios et leur état**.
- Les scénarios existants dont le nom porte un code connu sont **rattachés automatiquement**.

## Recommandations

### Admin, création d'un scénario
1. **R1 — L'incident d'abord, en tête du formulaire.** C'est l'ancre du scénario, et le champ obligatoire. L'ordre du formulaire suit l'ordre de la pensée : sur quel incident je travaille, puis comment je l'appelle (REF-06 Tesler, REF-14 heuristique 2 « correspondance avec le monde réel »).
2. **R2 — Un sélecteur avec recherche, groupé comme MELMIL.**
   - Une seule zone de saisie filtre par code (`08.01.04` équivaut à `I04`), par intitulé ou par storyline.
   - La liste est groupée par **storyline, avec son titre** : « 08.01 — Pénurie énergétique ».
   - Chaque option montre le **code** (police à chasse fixe), l'**intitulé**, le **moment** (« D+31 · 14:00 ») et, s'il y en a déjà, « **2 scénarios** ». On voit ainsi le doublon avant de le créer (REF-06 Hick : reconnaître, ne pas se souvenir ; REF-14 heuristique 5 « prévenir l'erreur »).
   - Clavier complet : flèches, Entrée, Échap ; l'option active est visible et annoncée (REF-19, modèle listbox ; REF-13 2.1.1).
3. **R3 — Une fois choisi, l'incident devient une étiquette lisible** : code, intitulé et moment, avec un bouton « Changer ». La liste se referme, l'écran respire (REF-07 : mettre en valeur en atténuant le reste).
4. **R4 — Le système pré-remplit ce qu'il sait** (Tesler), et l'humain corrige :
   - le **nom** prend l'intitulé de l'incident si le champ est vide ;
   - le **début** prend la date et l'heure de l'incident, quand MELMIL les connaît.
5. **R5 — Des états clairs** (REF-14 heuristiques 1 et 9) :
   - pendant le chargement, « Chargement des incidents MELMIL… » ;
   - si MELMIL ne répond pas, un message qui dit **quoi faire** (« MELMIL ne répond pas. Réessayez dans un instant ») avec un bouton « Réessayer ». La création reste bloquée, puisque l'incident est obligatoire ;
   - si la zone n'a pas de MELMIL, le champ disparaît et une ligne l'explique : la règle ne peut pas bloquer une zone sans MELMIL.

### Admin, liste et fiche
6. **R6 — Les en-têtes de groupe portent les titres MELMIL** : « Event 08 — Crise énergétique » › « Storyline 08.01 — Pénurie énergétique ». Le code reste devant, en chasse fixe.
7. **R7 — Lié ou seulement deviné, ça se voit.** Un scénario lié à MELMIL montre son code normalement. Un code seulement lu dans le nom est souligné en pointillé, avec l'infobulle « Code lu dans le nom, pas lié à MELMIL ». La différence ne repose pas sur la seule couleur (REF-07, règle 10).
8. **R8 — Dans la fiche d'un scénario**, un bandeau « Incident MELMIL : 08.01.I04 — Fuite du rapport », avec « Ouvrir dans MELMIL ↗ » et « Changer ». C'est là que l'on rattache à la main un ancien scénario.

### MELMIL
9. **R9 — Sur la carte de la planche, un pictogramme discret** (▶ et le nombre), au pied de la carte, à côté de l'agrafe. Il n'apparaît que s'il existe au moins un scénario. Si un scénario est **en lecture**, le pictogramme prend la couleur « en direct », doublée par le texte de l'infobulle et de l'`aria-label` : « 2 scénarios · 1 en lecture » (REF-07 règle 10 ; même logique que l'agrafe, avis n°24).
10. **R10 — Dans la fiche d'incident et dans le détail d'une carte**, un bloc « Scénarios (admin) » :
    - une ligne par scénario : état (texte + couleur), nom, créneau, et le lien « Ouvrir ↗ » ;
    - en bas, l'action « **Créer un scénario pour cet incident ↗** ». Elle ouvre l'admin avec le formulaire pré-rempli sur cet incident : le parcours se fait dans les deux sens, sans ressaisie (REF-06 Tesler) ;
    - si l'admin ne répond pas, une ligne grise « Admin injoignable — scénarios non affichés ». Jamais un « 0 » trompeur (règle « un échec de lecture n'est pas un résultat valide », CYBERSECU § 8).

## Sécurité (avec CYBERSECU)

- La liste des incidents que MELMIL publie ne contient **aucun nom, grade, compte ni ETIM de personne** : seulement code, intitulé, storyline, event, D+ et heure (anonymat option A).
- Les deux routes de service exigent la **clé de la zone** (`X-API-Key`, comparaison à temps constant). Côté navigateur, MELMIL ne parle qu'à son propre serveur, avec une session ouverte.
