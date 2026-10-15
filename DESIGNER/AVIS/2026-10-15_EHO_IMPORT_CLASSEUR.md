# Avis DESIGNER n°109 — eho, Import / Export : savoir si l'import a pris

**Date** : 2026-10-15 · **Demandeur** : utilisateur · **Mise en œuvre** : PLEIADE (dépôt `eho`, `src/app/(admin)/import/page.tsx`, `src/app/api/import/route.ts`)

## Constat de l'utilisateur
> « Je n'arrive pas à savoir si l'import a bien été réalisé ou non à chaque fois. »

## Diagnostic
1. **Un seul geste, sans vérification préalable.** « Importer » écrit tout de suite. On ne sait ni ce qui va changer avant, ni ce qui a changé après.
2. **Le bilan est éphémère.** Quatre compteurs apparaissent sous le formulaire et disparaissent si on quitte la page ou si on recharge. En revenant sur la page, rien ne dit qu'un import a déjà eu lieu, ni quand, ni avec quel fichier. C'est le cas de l'utilisateur, qui a importé avant un push sans savoir si « ça a pris ».
3. **« 100 mis à jour » ne veut rien dire.** Un avatar est compté « mis à jour » même quand aucune valeur ne change. Rien ne dit quels champs ont bougé.
4. **Échec silencieux.** Si le serveur répond autre chose que du JSON (fichier trop gros, coupure), la page reste sur « Import en cours... » et rien ne s'affiche.
5. **L'aide est fausse.** La liste des « colonnes reconnues » omet `bio_publique`, `lieu_affiche`, `langue_publication`, `source_fiche`, `localisation_reelle`, `certification`… que l'import lit bien. Elle fait douter du fichier.

## Recommandations
Reprendre le parcours n°99, celui des fiches IA, que l'utilisateur connaît déjà : on dépose le fichier, une vérification s'affiche dans la page, on confirme, et un bilan reste visible.

- **R1. Vérification d'office au dépôt, rien n'est écrit.** Bandeau « Vérification de « fichier.xlsx » : rien n'a encore été modifié. »
- **R2. Quatre statuts, avec une forme et un mot, jamais la couleur seule.**
  - ✕ refusés, avec la raison par ligne (onglet, ligne, avatar) ;
  - \+ à créer ;
  - ● à modifier ;
  - = inchangés.
  - Les refusés et les modifiés sont dépliés ; les créés et les inchangés sont repliés.
  - Pour un modifié, on affiche les **champs qui changent** en puces (« Bio · Pays · Âge 0 → 25 · + groupe CAMP IA »).
- **R3. Annoncer les groupes créés à la volée** : « 2 groupes seront créés : … ». Créer un groupe est un effet de bord qu'on ne doit pas découvrir après coup.
- **R4. Un bouton qui dit ce qu'il fait** : « Appliquer : 3 créations, 97 modifications », puis la fenêtre de confirmation `confirmer`.
  - Si tout est inchangé, pas de bouton, mais la phrase « Rien à appliquer : les N avatars du fichier sont identiques à ceux de la zone. »
  - Si la zone a changé entre la vérification et l'application, le serveur répond 409 et la page dit « La zone a changé depuis la vérification : relancez-la. »
- **R5. Un bilan final qui reste** : « ✓ Import appliqué à 18:52 : 3 créés, 97 modifiés, 0 refusé. » Il reste affiché jusqu'au prochain dépôt.
- **R6. « Dernier import » en tête de page**, relu du journal et persistant d'une visite à l'autre : « Dernier import : profils-lecteurs….xlsx, le mer. 14/10 à 18:52, par tmeytre : 0 créé, 100 mis à jour, 0 refusé. » C'est **la** réponse à « est-ce que ça a pris ? ».
- **R7. Toute erreur s'affiche.** Une réponse non JSON (413, 502…) donne « Le serveur n'a pas répondu (HTTP 413) : rien n'a été modifié » ou « … : vérifiez le dernier import ci-dessus ». La page n'est jamais bloquée sur « en cours ».
- **R8. L'aide tirée de la vraie liste** : les colonnes reconnues viennent de `COLONNES` (une seule source, plus d'oubli), repliées sous « Colonnes reconnues (29) ».
- **R9. Ne pas toucher au reste.** Le choix « Groupe à appliquer à toutes les lignes » et le bouton « Exporter en .xlsx » restent tels quels. Le choix de groupe est pris en compte dans la vérification (« + groupe X » dans les puces).

## Doctrine
Un import qui écrit doit se lire trois fois :
- **avant**, ce qui va changer ;
- **juste après**, ce qui a changé ;
- **plus tard**, quand et avec quel fichier.

Un compteur qui disparaît au rechargement ne prouve rien.
