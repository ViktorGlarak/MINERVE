# Avis PSYCHOLOGUE n°28 — Audit complet du moteur IA et des fiches : vers des dialogues réels

**Date** : 2026-10-15 · **Demandeur** : utilisateur (« se rapprocher du dialogue le plus réel possible ») · **Mise en œuvre** : PLEIADE (`app-ia`, générateur et fiches eho)

**Matière** :
- le code du moteur 2026-10-15.2 (`pont.mjs`, `esprit.mjs`, `redacteur.mjs`, juges et modules) ;
- les exports du 14/10 : **E1** du 13/10 15:46 au 14/10 11:04, **E2** du 14/10 11:05 à 15:48 ;
- les 105 fiches de la population et les 100 fiches de lecteurs.

En tout : 370 messages produits par le moteur, comparés à 746 messages de comptes hors population (joueurs et animation). Aucun message de joueur n'est recopié ici.

## 1. Verdict
**Un avatar passe pour un humain sur un message isolé, mais il se démasque en une minute de lecture.** Surtout, **les dialogues meurent au premier échange**.

Le moteur sait décider *quoi* penser : opinions, camp, sources, émotions. Il ne sait pas encore *converser* : tenir un tour de parole, se souvenir de ce qui vient d'être dit, répondre vite, court et à quelqu'un. Et il écrit avec **une seule voix** pour 105 personnes.

## 2. Constats chiffrés

### 2.1 La conversation
- **Aucun fil n'atteint 4 tours.** 141 échanges s'arrêtent à 2 tours et 5 vont jusqu'à 3. Quand un joueur relance, l'avatar ne répond jamais (0 sur 5). Sous les publications des avatars, 16 commentaires de joueurs n'ont reçu **aucune** réponse de l'auteur (E1 et E2, avant les correctifs de la 14.x sur le parent des commentaires).
- **Les commentaires de joueurs sont presque invisibles pour le modèle.** Il ne propose de répondre que dans 0,19 % des décisions sur un commentaire (4 sur 2 135), contre 6,4 % sur une publication (E1). Au total, 4 % des commentaires de joueurs reçoivent une réponse.
- **L'entonnoir est étroit avant même le modèle.** 6 à 9 avatars lisent par tour, sur 103. Chaque lecture fait 8 messages évincés (E1). Le taux de réponse aux messages de joueurs passe de 18,7 % (E1) à 10,1 % (E2).
- **Les filtres tuent 60 % des réponses que le modèle propose** (88 sur 146, E1) : « sans substance », « déjà n réponses », tics, « partage sans information ».
- **La latence est lente et irrégulière.** La médiane avant la première réponse est de 4,8 min, mais le 3e quartile atteint 30 min. Un échange de 4 répliques prend au moins 15 à 30 min, puisqu'il faut un cycle par réplique. Un avatar au travail interpellé peut attendre une à deux heures.
- **Ce que l'avatar voit quand on lui répond** : le message, plus **90 caractères** du message parent. Il ne voit ni la racine, ni les répliques précédentes, ni ce que les autres ont répondu. La réponse est jugée **dans un lot de 4 messages**, au milieu d'un JSON d'une quarantaine de champs. Une consigne lui dit même « tu as déjà répondu à X aujourd'hui : ne le reprends pas », y compris quand X lui répond.
- **On parle de la personne au lieu de lui parler.** 70,5 % des réponses à un joueur ne s'adressent pas à lui. 3,4 % lui posent une question. Le tutoiement est quasi absent.

### 2.2 La voix
| | Avatars | Joueurs |
|---|---|---|
| Longueur médiane d'un commentaire | **172 car.** | **51 car.** |
| Commentaires de moins de 80 car. | **0 %** | 84 % |
| Émoji | 81 % (en fin de message : 78 %) | 15 % |
| Points de suspension | 72 % | 8 % |
| Début en minuscule | 0 % | 24 % |
| Sans ponctuation finale | 2 % | 57 % |
| Mot-dièse | 100 % | 80 % |
| Les trois marqueurs ensemble (« … » + émoji + #) | **58,6 %** | 1,1 % |

- **38 % des messages IA finissent par « #freegrandest #mercure ».** Les joueurs écrivent toujours l'ordre inverse : c'est une empreinte immédiate.
- **Une phraséologie commune.** 62,7 % des messages IA contiennent une formule employée par au moins 3 avatars (« on finit par ne plus savoir » chez 18 avatars, « ce qui se passe » chez 23), contre 11,7 % chez les joueurs. Ce sont des voix riches une par une, mais **interchangeables** : le vocabulaire est plus partagé entre avatars (0,209) qu'entre joueurs (0,139).
- **Les tics de population** : « j'espère » 11,6 % (joueurs 0,7 %), « rumeur » 12,2 % (1,5 %), « on finit par » 7,8 % (0 %), 😟 et 😰 en tête des émojis.

### 2.3 Les fiches
- **Le registre n'est jamais décrit.** Aucune fiche ne dit « tutoie », « fait des fautes », « familier », « minuscules ».
- **Des consignes en gabarit.** Trois consignes sont identiques dans 100 fiches, dont « il varie les émojis », qui suppose qu'il en met. Les 100 lecteurs n'ont que **7 consignes distinctes** à eux tous.
- **Des exemples qui fixent le moule.** Il n'y en a aucun de moins de 60 caractères ; la médiane est de 128 caractères dans la population et de 100 chez les lecteurs. Les mêmes formules passent d'une fiche à l'autre : « la présence de la FORCE » dans 30 fiches de lecteurs, « Encore une… » 42 fois dans la population.
- **Des tempéraments centrés.** 49 à 86 % des valeurs sont entre 30 et 70. Chez les lecteurs, l'émotivité est entièrement entre 30 et 59, et l'extraversion a un écart-type de 5.
- **Des sensibilités plates.** « Vie quotidienne » vaut 81 et « rumeurs » 72 chez presque tous, d'où la sur-présence de « rumeur » et du café-boulot.
- **1 115 interdits pour 92 formulations**, dont « employer des mots anglais », qui pousse vers une langue de rédacteur relu.

### 2.4 La technique
- **Fenêtre de contexte : `num_ctx` 8 192.** Persona (3 000 à 3 500 jetons), lot de lecture (3 000 à 5 000) et sortie peuvent la dépasser, avec une **troncature silencieuse** à mesurer (`prompt_eval_count`).
- **Jusqu'à une dizaine d'appels au modèle pour un message** (typiquement 3 à 5) : rédacteur, contrôle, relecture, pertinence, orientation, reformulations. Chaque couche **lisse** un peu plus et allonge le cycle, donc la latence.
- **De 40 à 50 consignes simultanées** dans l'invite.

### 2.5 À vérifier
Aucune ligne de journal « publié » n'apparaît pour **Rolf Weber** et **Sergueï Untergang** (37 messages). Ces deux comptes semblent incarnés par l'animation, et ils faussent les compteurs du moteur. À confirmer par l'utilisateur.

## 3. Lecture psychologique

1. **Une conversation est une suite de tours de parole, pas une série de commentaires.** C'est l'analyse conversationnelle (Sacks, Schegloff et Jefferson, 1974). Une question appelle une réponse, un salut un salut : ce sont des **paires adjacentes**, et le second terme absent se remarque. Chaque tour s'appuie sur le précédent, et on corrige les malentendus (réparation). Un avatar qui ne voit que 90 caractères du tour précédent ne peut pas « enchaîner ». Il commente, il ne converse pas.
2. **Le moindre effort collaboratif** (Clark et Wilkes-Gibbs, 1986). Entre interlocuteurs qui partagent un contexte, les répliques **raccourcissent** : « ah ok », « t'es sûr ? », « où ça ? ». La longueur médiane des joueurs (51 caractères, 58 % en une phrase) en est la trace. Les filtres « sans substance » et « début déjà pris » et l'obligation du détail concret **interdisent précisément ces répliques**.
3. **L'accommodation** (théorie de Giles). On ajuste son registre à celui de l'autre : tu ou vous, familier, émojis. Ici, aucun registre n'est mémorisé par relation, et toutes les fiches écrivent en français soigné.
4. **Idiolecte contre consensus de style.** Chaque personne a ses tics : son émoji, sa ponctuation, ses fautes, ses mots. Ils sont **stables chez elle et différents d'une personne à l'autre**. Le moteur fait l'inverse. Il **interdit à chacun de se répéter** (`tics`, `themesUses`, « émojis déjà utilisés »), mais il laisse **toute la population partager** les mêmes « … », 😟 et « on finit par ». On obtient la variété là où les humains sont constants, et l'uniformité là où ils diffèrent.
5. **Le modèle suit la foule.** Les repères d'OASIS (avis n°6) et le chœur du doute (n°27) le montrent : la pente du modèle est la posture consensuelle et prudente. Plus on empile de juges écrits par le même modèle, plus on **renforce** cette pente.
6. **Le rythme humain est en rafales.** Sur un vrai réseau, on reste dans une conversation : on guette la réponse pendant 10 à 20 min, puis on décroche. Ici, après avoir écrit, l'avatar repart pour 10 à 30 min de pause : l'échange est cassé par construction.
7. **La règle 1-9-90 doit rester.** La plupart lisent, peu écrivent : les lecteurs et la loi de puissance des J'aime vont dans le bon sens. Le réalisme ne demande pas **plus** de messages, il demande que **ceux qui parlent tiennent la conversation**.

## 4. Plan de corrections, en quatre lots

### Lot A — La conversation (impact maximal)
- **A1. Le fil complet dans l'invite.** La racine, puis les 6 à 8 dernières répliques du fil, avec leur auteur, en marquant « toi », sans couper à 90 caractères. S'y ajoutent « déjà dit sous ce message par d'autres », **qui est l'interlocuteur** (un humain du réseau ou un avatar, la relation résumée en mots, sans chiffres) et le **registre** tu ou vous **mémorisé par relation**.
- **A2. Une voie un-à-un pour les interpellations** (mention, réponse à son message). Un appel dédié, avec l'historique comme dans la messagerie privée, et une sortie réduite à `{action, texte}`. On ne passe plus par le lot de 4 messages.
  - Exemptions : budget du jour (`brider`), « sans substance », « début déjà pris », « phrase inachevée ».
  - Le juge de pertinence devient **indulgent**.
- **A3. Une fenêtre de conversation.**
  - Après avoir écrit à quelqu'un, l'avatar revient voir ses notifications 2 à 5 min plus tard, avec une activité plancher de 0,5 pendant 20 min.
  - Une interpellation se lit avec une probabilité plancher : 0,35 au travail, 1 en temps libre.
  - Une **voie rapide** traite seulement les avatars interpellés, toutes les 30 s.
  - **Cible** : 30 à 90 s de latence sur une interpellation.
- **A4. Des bornes de retour humaines.**
  - On compte **tous** les retours, pas seulement ceux que force le code.
  - La probabilité décroît d'un retour à l'autre (0,8, puis 0,6, 0,4, 0,25), au lieu d'un plafond dur de 2.
  - On supprime « ne le reprends pas » quand l'interlocuteur s'adresse à l'avatar.
  - L'avatar peut **clore** (« bon, on ne sera pas d'accord », « ok merci »).
  - Face à un avatar dans un fil où un joueur est actif, 2 retours sont permis au lieu de 1.
- **A5. Le participant lit le fil.** Un avatar qui a commenté sous une publication lit les nouveaux commentaires de cette publication pendant 2 h. C'est ce qui rend possible une **discussion à plusieurs**.

### Lot B — La voix, par le code (coût nul)
- **B1. La longueur.**
  - Chaque fiche a une **longueur typique**.
  - En conversation, la cible est de 30 à 50 % de répliques de moins de 60 caractères ; une réplique peut faire de 1 à 5 mots.
  - Visé pour un commentaire IA : une médiane de 50 à 90 caractères.
- **B2. La typographie, propre à chaque avatar et appliquée par le code de façon déterministe**, d'après un champ `style` de la fiche :
  - émoji : jamais, rare, ou **signature** (toujours le même) ;
  - points de suspension : oui ou non ;
  - minuscule en début de message, ponctuation finale omise ;
  - abréviations et fautes légères et constantes (« sa » pour « ça », accents omis).
  - **Visé** : émoji ≤ 35 %, points de suspension ≤ 15 %, au moins 15 % de messages sans ponctuation finale.
- **B3. Les mots-dièse.**
  - Ils ne sont plus systématiques dans les réponses (cible : environ 40 %).
  - L'ordre suit la pratique des joueurs.
  - #3615MyLife est réservé aux vrais moments de vie.
  - ⚠ Cela revient sur la règle de l'utilisateur du 12/10 (« tout message porte un # » pour le Cockpit) : **à trancher par lui**.
- **B4. L'idiolecte permis, le consensus interdit.**
  - `themesUses` cesse d'interdire les mots du sujet.
  - L'émoji signature et les tics personnels sont autorisés.
  - Un **anti-chœur lexical de population** devient bloquant : les 4-grammes employés par au moins 3 avatars en 6 h, comme « on finit par ne plus savoir ».

### Lot C — Les fiches (regénération et import eho)
- **C1. Un idiolecte par avatar** : registre (tu ou vous par défaut, niveau de langue), longueur typique, `style` typographique (B2), 2 ou 3 tics personnels, un émoji signature ou aucun, des mots à lui.
- **C2. Des consignes personnelles** : plus de gabarit commun. Les règles communes (pas d'information militaire, GET…) restent dans le moteur.
- **C3. Des exemples regénérés** : un tiers de moins de 60 caractères, des répliques de conversation (« t'as vu ça où ? », « ah bon ? »), aucune formule partagée entre fiches (contrôle par le code).
- **C4. Des tempéraments et sensibilités réalistes** : des distributions avec des queues (des très émotifs, des très placides, quelques extravertis chez les lecteurs) et des sensibilités contrastées (pas « vie quotidienne 81 » pour tous).

### Lot D — Les contrôles et la technique
- **D1. `num_ctx` à 16 384**, ou un lot de lecture réduit. On mesure `prompt_eval_count` et on retire `pourquoi` et `sur_le_fait` de la sortie du lot. **C'est prioritaire** : une troncature silencieuse fausse tout le reste.
- **D2. Un juge unique** : relecture, pertinence et orientation en un seul appel, suivi d'au plus une réécriture. On passe de 3 à 6 appels à 1 ou 2, avec moins de lissage et des cycles plus courts.
- **D3. Des délais humains** : temps de lecture plus longueur divisée par la vitesse de frappe, en loi log-normale, avec une queue de 10 à 20 min sur 15 % des cas, et court pour une mention.
- **D4. Tracer tous les silences**, y compris la publication jetée pour ressemblance sans ligne de journal.

## 5. Ordre recommandé
1. **D1**, contrôle technique, tout de suite.
2. **A1, A2 et A4**, la conversation, et **B1, B2 (côté code) et B4**, la voix. Une version du moteur.
3. **C1 à C4** : regénérer les 205 fiches avec le générateur, puis les importer dans eho. On vérifie d'abord sur 10 fiches.
4. **A3 et A5** (rythme et voie rapide), **D2 et D3**.
5. **B3**, après la décision de l'utilisateur sur les mots-dièse.

## 6. Critères de réussite (au prochain export, après le lot 2)
- **Fils** : au moins 10 fils de 4 tours ou plus par jour.
- **Retour** : l'avatar interpellé répond dans au moins 60 % des cas.
- **Latence** : médiane d'au plus 3 min pour une interpellation.
- **Adresse et questions** : au moins 50 % des réponses s'adressent à la personne, et au moins 15 % lui posent une question précise.
- **Longueur** : commentaire IA de 50 à 90 caractères en médiane, au moins 30 % sous 60 caractères.
- **Typographie** : émoji ≤ 35 %, points de suspension ≤ 15 %, les trois marqueurs ensemble ≤ 10 %.
- **Formules partagées** par au moins 3 avatars : ≤ 25 % des messages.
- **Garde-fous intacts** : aucune information militaire, aucune orientation inversée non mesurée, plafond de population tenu.

## 7. Questions pour l'utilisateur
1. Mots-dièse : maintenir « tout message porte un # » pour le Cockpit, ou les rendre facultatifs dans les réponses (environ 40 %) ?
2. Fautes et abréviations : les autoriser chez une partie des avatars (par exemple 30 %), légères et constantes ?
3. Rolf Weber et Sergueï Untergang : sont-ils incarnés par l'animation ? Si oui, on les marque comme tels dans le moteur et dans les analyses.
4. Regénérer le registre, les consignes et les exemples des 205 fiches : oui, en commençant par 10 fiches à valider ?
