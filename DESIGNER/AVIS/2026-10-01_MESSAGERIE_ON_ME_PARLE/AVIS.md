# Avis DESIGNER n°22 — Messagerie : « on me parle » en orange

**Date** : 2026-10-01 · **App** : `app-messagerie`, liste des conversations (colonne de gauche)
**Demande de l'utilisateur** : la liste ne se mettait pas à jour toute seule, si bien que le premier message d'une personne restait invisible avant rechargement. Il veut aussi que la discussion qui reçoit un message « clignote en orange (un joli orange) », pour voir que quelqu'un parle, en privé, en groupe ou dans un canal.

## Recommandations retenues

| # | Recommandation | Source |
|---|---|---|
| R1 | **Un seul orange, réservé à ce signal.** Le bleu reste celui des actions ; l'orange veut dire « nouveau message », et rien d'autre. | Von Restorff (doctrine n°20) |
| R2 | **Une pulsation douce, pas un clignotement brutal.** On n'anime que l'opacité d'un voile orange, sur 1,6 s, avec un aller-retour entre 100 et 35 %. On reste donc sous un cycle par seconde, et on n'est jamais dans le flash. | doctrine n°14, WCAG 2.3.1 |
| R3 | **Un signal qui tient sans le mouvement.** Un liseré orange de 4 px à gauche et un voile teinté signalent le fil même à l'arrêt. | doctrine n°10 |
| R4 | **Jamais par la couleur seule.** La pastille porte le nombre de messages non lus, le nom passe en gras, et un lecteur d'écran entend « 2 messages non lus ». | doctrine n°10 |
| R5 | **Pastille : texte SOMBRE sur l'orange.** Le blanc n'y atteint pas 4,5 : 1. | doctrine n°21 |
| R6 | **Couleurs en `oklch`, avec une paire pour le thème sombre.** Clair : `oklch(0.72 0.17 52)`, voile à 16 %. Sombre : `oklch(0.77 0.16 58)`, voile à 18 %. | doctrine n°2 |
| R7 | **« Réduire les animations » est respecté.** La pulsation s'arrête, mais le liseré et le voile restent. | doctrine n°14 |
| R8 | **Le signal s'arrête quand on ouvre le fil.** Le fil ouvert, muet ou archivé ne pulse pas. | Nielsen 1 (état visible) |
| R9 | **Le signal se voit hors de la liste visible** : un point orange sur l'onglet « Canaux » ou « Discussions » qui contient le message, et « (n) » dans le titre de l'onglet du navigateur. | Jakob (usage des messageries courantes) |

## Hors design, mais lié : le nom de celui qui parle

Le titre d'une conversation privée était celui qu'avait choisi son créateur. La personne qui recevait un message y voyait donc **son propre nom**. La liste et la fiche affichent désormais le nom de l'**autre** membre.

## Vérification

Faite en local avec Playwright, sur des données fictives : Paul écrit pour la première fois.
- La conversation apparaît dans la liste **sans rechargement**, en moins d'une seconde.
- Elle pulse en orange, avec la pastille « 1 », le point orange sur « Discussions » et « (1) Messagerie » dans le titre de l'onglet.
- Au deuxième message, la pastille passe à 2.
- À l'ouverture du fil, l'orange disparaît.
- Avec « réduire les animations », la pulsation est à `none`.

Capture : `apres_message_recu.png`.
