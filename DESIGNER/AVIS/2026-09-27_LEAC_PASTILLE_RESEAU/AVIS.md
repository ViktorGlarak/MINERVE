# Avis DESIGNER n°8 — LEAC : la pastille « En direct / Copie / Injoignable »

> **Date** : 2026-09-27 · **Demande** : voir d'un coup d'œil si l'écran vient du serveur ou de la copie du service worker (« disconnect » / « direct » en vert). Contexte : deux postes (Axel, puis l'utilisateur) sont restés sur l'ancienne version, persuadés d'être en ligne — le certificat de la zone n'était pas approuvé.

## Solution retenue

**R1 · L'état du système toujours visible, au même endroit** *(Nielsen 1, règle 25 ; règle LEAC « l'état de synchronisation est permanent »)* : une pastille dans le bandeau, sur toutes les pages, jamais une notification fugace.

**R2 · Trois états, chacun avec son texte ET sa forme** *(règle 10)* :
- **En direct** : vert, rond plein avec un halo ;
- **Hors ligne · copie de l'appareil** : ambre, demi-rond ;
- **Serveur injoignable** : rouge, croix.

Au téléphone (< 560 px), le texte court : « Direct », « Copie », « Injoignable ». Couleurs claires, lisibles sur le bandeau graphite dans les deux thèmes.

**R3 · Ne dire que ce qui est mesuré** *(mémoire « indicateur d'état »)* :
- la page marquée par le service worker = copie ;
- une vraie réponse de `/api/sante` = serveur joint ;
- jamais `navigator.onLine`.

**R4 · Un appui explique et propose l'action** *(Tesler, règle 19 ; heuristique 9)* : ce que signifie l'état, la dernière réponse du serveur (« il y a 3 min »), quoi vérifier (réseau, VPN, cadenas), « Vérifier maintenant », et « Recharger depuis le serveur » quand on est sur la copie.

**R5 · Le diagnostic que l'on sait poser, on le pose** : « copie + serveur qui répond » est la signature du certificat de zone non approuvé. C'est dit en clair, dans un encadré d'alerte : l'unique alerte rouge de la fenêtre *(Von Restorff, règle 20)*.

## Écarts
- Pas de couleur de fond sur tout le bandeau selon l'état : trop envahissant sur 8 h de contrôle, et cela noierait les autres signaux.
- Le navigateur ne distingue pas « pas de réseau » de « certificat refusé » : l'état « injoignable » cite donc les deux causes.
