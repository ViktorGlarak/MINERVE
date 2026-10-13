# Question de l'utilisateur à vérifier DANS LE CODE d'app-ia (posée sur le Mac le 2026-10-13)

> Pour la session du PC : l'utilisateur veut **s'assurer de bien comprendre** ce que change le 2ᵉ nœud de calcul (le Mac, branché le 2026-10-13 à 10 h 22). Le Mac a répondu **d'après la documentation seulement**, sans accès au code. Merci de **vérifier dans le code d'app-ia** (sélection des lecteurs, `parc.mjs`, `parc-serveur.ts`, boucle de cycle), puis de confirmer ou de corriger les points ci-dessous en citant fichier et ligne. Réponse attendue en clair pour l'utilisateur, à consigner dans `PLEIADE/PROJET_AVATARS_IA.md` § 8.

## Sa compréhension, telle qu'il l'a formulée
> « Quand le moteur tourne avec 1 machine et 103 avatars IA, l'ordinateur sélectionne 20 avatars par cycle et leur fait lire le fil d'actualité.
> Quand il tourne avec 2 machines et 103 avatars, les avatars sont divisés (ici 50 et 53), donc au lieu d'avoir 20 avatars sélectionnés par cycle on en a 40, c'est bien ça ? »

## Réponse donnée depuis le Mac (À VÉRIFIER)
1. **Le nombre de lecteurs par cycle ne dépend pas du nombre de machines.** Il est fixé par la psychologie du moteur : réveillé, disponible, attiré par le fil. La cible PSYCHOLOGUE est ~12 % de la population (`PSYCHOLOGUE/MEMOIRE.md` l. 160), bornée par `MAX_LECTEURS` (l. 339). Le tableau de bord montrait « Lectures 9, moy. 59 » par cycle sur la capture du 11/10.
   → **À vérifier** : où et comment les lecteurs sont choisis ; valeur de `MAX_LECTEURS` ; le parc modifie-t-il ce nombre d'une façon ou d'une autre ?
2. **Chaque avatar est rattaché à UNE machine, toujours la même** (affectation stable par rendez-vous, `parc.mjs`). D'où ~50 / 53.
   → **À vérifier** : la répartition réelle actuelle (PC / Mac), visible dans l'onglet Parc de calcul.
3. **À chaque cycle, les lecteurs choisis partent chacun vers SA machine, et les deux files tournent en parallèle** (« une file par nœud, en parallèle »). Le cycle finit donc ~2 fois plus vite, et le suivant démarre 90 s après la fin. Résultat : **~2 fois plus de lectures par HEURE** (chaque avatar lit son fil plus souvent, donc réagit plus vite), mais **pas 2 fois plus de lecteurs par cycle**.
   - Exemple donné : 60 lectures × 13 s ≈ 13 min avec 1 machine, contre ≈ 6,5 min avec 2 ; avec la pause de 90 s, ~4 cycles par heure contre ~7,5.
   → **À vérifier** : la durée réelle des cycles avant et après le branchement du Mac (Journal / Tableau de bord), et la limite de 2 requêtes simultanées par nœud côté app-ia.
4. **Usage possible de la capacité gagnée**, à décider par l'utilisateur :
   - (a) plus de réactivité : c'est l'effet automatique actuel ;
   - (b) plus de qualité : rédacteur et nuances d'émotion pour tous, au lieu du seul groupe d'essai ;
   - (c) plus d'avatars, vers les ~4 000 du modèle eho.

## Ce que l'utilisateur attend
Une confirmation ou une correction **chiffrée et sourcée dans le code**, en quelques lignes simples. Si sa formule « 20 → 40 par cycle » est en fait juste (si le moteur ajuste le nombre de lecteurs à la capacité du parc), le dire clairement.
