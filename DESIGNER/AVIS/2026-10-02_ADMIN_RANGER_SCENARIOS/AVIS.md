# Avis n°27 — app-admin : retrouver ses scénarios dans la masse

> **Date** : 2026-10-02 · **Demandeur** : l'utilisateur · **Écran** : `app-admin`, page « Scénarios » (`src/components/ScenariosList.tsx`)
> **Statut** : ✅ R1 à R5 en ligne le 2026-10-02 (admin `7d6d96f`).

## Besoin exprimé

« L'organisation du rangement des scénarios ne nous aide pas à nous repérer ; on peine à retrouver nos scénarios dans la masse. »
Réponses de l'utilisateur :
- on cherche un scénario **par son incident MELMIL** ;
- les noms commencent **en général par le code** (« 08.01.I04 — … »).

## Constat (lecture du code, 2026-10-02)

| # | Problème | Gravité (Nielsen, 0-4) | Source |
|---|---|---|---|
| C1 | Liste **plate**, triée par **dernière modification** (`updatedAt desc`) : un scénario change de place dès que quelqu'un le touche. La mémoire de position ne sert à rien. | 3 | Heuristique 6 « reconnaître plutôt que se souvenir » (REF-14) ; Jakob (REF-06) |
| C2 | **Grandes cartes** : deux bandeaux, une description et un bouton « Ouvrir ». Environ 5 scénarios par écran, il faut beaucoup faire défiler. | 3 | Données denses → tableau (Carbon REF-12) ; Refactoring UI, hiérarchie (REF-07) |
| C3 | Aucun **regroupement** : le code MELMIL est dans le nom, mais rien ne s'en sert. | 3 | Région commune, proximité (REF-06) |
| C4 | Recherche limitée au texte libre ; filtres de statut **sans effectifs**. | 2 | Heuristique 1 « état du système visible » (REF-14) |

## Recommandations (classées par gain)

1. **R1 — Ranger selon l'arborescence MELMIL, lue dans le nom.** Event `08` › storyline `08.01` › incident `08.01.I04`.
   - Groupes repliables, chacun avec son effectif et un résumé d'état (« 3 scénarios · 1 en lecture · 1 en erreur »).
   - Ordre **par code**, donc **stable** : un scénario ne bouge plus.
   - Les relances (`08.01.I04A.R1`) se rangent sous leur incident.
   - Un groupe « **Non classés** » en fin de liste, pour les noms sans code, dit comment les classer : « commencez le nom par le code de l'incident ».
   - *Sources* : région commune et proximité (REF-06) ; Tesler (REF-06), le système fait le tri, l'humain n'a rien à ressaisir. *Effort* : moyen. Aucun changement de base.
2. **R2 — Une ligne par scénario au lieu d'une carte** : code (police à chasse fixe), nom, statut (texte + couleur), créneau, publiés x/y, auteur. Toute la ligne ouvre le scénario ; « Supprimer » reste à part, discret. On voit environ 4 fois plus de scénarios par écran.
   - *Sources* : Carbon, tableau de données (REF-12) ; une seule action principale (REF-01) ; cibles d'au moins 24 px (REF-13). *Effort* : moyen.
3. **R3 — Une recherche qui comprend les codes.** Taper `08.01` montre la storyline entière, groupes ouverts ; `I04` trouve l'incident. Les filtres de statut affichent leurs effectifs (« En lecture 4 »).
   - *Sources* : Heuristiques 1 et 7 (REF-14). *Effort* : faible.
4. **R4 — Se souvenir de l'affichage** : groupes ouverts ou fermés et filtre choisi, mémorisés par poste (le stockage du navigateur suffit, c'est un confort individuel).
   - *Source* : Heuristique 6 (REF-14). *Effort* : faible.
5. **R5 — À la création, guider vers le bon nom** : modèle « 08.01.I04 — … » dans le champ, et une remarque douce si le code manque. Aucun refus : Postel, tolérant en entrée (REF-06).
   - *Effort* : faible.

**Écarté pour l'instant** : afficher les **titres** des events et storylines. L'admin ne les connaît pas, il faudrait les demander à MELMIL par une route de service. C'est une étape 2 possible, mais on ne l'engage pas sans besoin exprimé.

## Point annexe signalé (sécurité / CYBERSECU)

Les scénarios créés avant la correction d'identité du 2026-10-02 portent un `createdById` **aléatoire**. Leur auteur ne se voit donc plus le droit de les supprimer ; seul un administrateur le peut. À réparer si l'utilisateur le souhaite. Le rattachement par le nom affiché est fragile, car deux homonymes le partagent : il faut en décider avec l'utilisateur.
