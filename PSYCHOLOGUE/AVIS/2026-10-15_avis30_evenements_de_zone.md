# Avis PSYCHOLOGUE n°30 — Événements de zone : évacuation, confinement, couvre-feu, coupures, bombardements…

**Date** : 2026-10-15 · **Demandeur** : utilisateur (« si on annonce qu'une ville doit évacuer, est-ce que les avatars de cette ville se questionnent, voire évacuent ? et leur mémoire prend-elle en compte qu'ils deviennent réfugiés ? ») · **Décisions utilisateur** : déclenchement par l'animation et détection des annonces officielles ; « tout ce qui peut se passer ». · **Mise en œuvre** : PLEIADE (`app-ia`)

## Constat (code au 15/10)
- Une annonce devient un fait, avec un niveau de menace, une croyance et de la peur. Mais elle **n'est pas rattachée à la ville de l'avatar** : la phrase « ça touche ta ville » est dite à tous les anxieux.
- Aucune décision de départ.
- Le domicile de la fiche a toujours le dernier mot : un avatar qui dit « on part chez ma sœur » continue de vivre, de travailler et de voir sa ville d'origine. Il ne devient jamais un déplacé.

## Lecture psychologique
- **Face à un ordre d'évacuation, on ne part pas tous**, ni tout de suite. La littérature sur les évacuations (Lindell et Perry, *Protective Action Decision Model*) montre qu'on évalue trois choses :
  1. la **crédibilité de la source** et la **menace** perçue ;
  2. le **coût du départ** (enfants, âge, absence de véhicule, animaux, logement) ;
  3. les **obligations** (métiers essentiels, proches dépendants).
- Il y a toujours des **hésitants**, qui partent plus tard, et des **refus**. On refuse par méfiance envers l'autorité, par attachement au lieu, ou parce qu'on ne peut pas.
- **Le déplacé change de vie.** Il dort ailleurs, chez un proche ou dans un centre d'accueil. Il ne travaille plus, s'inquiète pour son logement, ressent fatigue, honte ou colère. Il se rapproche des autres déplacés, et ce qui touche aux déplacés le concerne désormais au premier chef. Le retour est progressif et lui aussi chargé d'émotion.
- **Chaque type d'événement transforme le quotidien à sa façon.**
  - Un confinement ou un couvre-feu enferme, désœuvre et rend plus présent sur le téléphone.
  - Une coupure d'eau ou d'électricité impose des files d'attente, de la débrouille, de l'agacement.
  - Une coupure du réseau fait disparaître des écrans.
  - Un bombardement provoque la peur maximale, l'abri et le silence, puis une rafale de messages à la sortie, et des départs précipités.
  - Une pénurie apporte des files, des prix et des tensions.
  - Une route coupée ou un barrage empêche d'aller travailler et allonge les trajets.
  - Une manifestation ou des troubles imposent prudence et curiosité.
- **Ce qui ne touche pas sa ville** se lit comme une nouvelle, pas comme sa vie. Un proche qui vit dans la ville touchée inquiète, mais moins que sa propre ville.

## Décisions

### D1. Déclenchement
- **L'animation** déclare l'événement dans les Réglages, panneau « Événements de zone » : type, villes, début, fin éventuelle et description concrète (par exemple « plus d'eau courante, distribution au gymnase »).
- **Le moteur repère aussi** les annonces des **comptes officiels de l'annuaire**, c'est-à-dire les préfectures et les comptes militaires et officiels non rouges. Une évacuation, un confinement, un couvre-feu ou une coupure qui nomme une ville en H crée un événement « détecté », journalisé et actif. L'animation peut le reprendre à son compte ou l'ignorer, en déclarant la fin.

### D2. Qui est concerné
- **Les habitants** de la ville, d'après le domicile de leur fiche ou le lieu où ils sont hébergés depuis une évacuation.
- **Les travailleurs** de la ville pour une route coupée, un barrage ou des combats : leur lieu de travail est touché.
- Les autres le lisent comme une nouvelle ; si un proche y vit, ils l'apprennent et s'inquiètent un peu.

### D3. Évacuation : la décision, par le code, stable et rejouable
- **Probabilité de partir** : p = 0,45 + 0,30 × anxiété + 0,10 × crédulité, avec les ajustements suivants :
  - **+0,15** avec des enfants au foyer ;
  - **+0,15** si l'avatar a confiance dans l'autorité qui l'annonce ;
  - **−0,30** pour un pro-Mercure affirmé, si l'ordre vient d'une autorité arnlandaise ou de la FORCE ;
  - **−0,20** pour un métier essentiel (soignant, pompier, policier, militaire, élu) ;
  - **−0,15** à 70 ans et plus, ou sans véhicule ;
  - le résultat est borné entre 0,05 et 0,95.
- **Issue du tirage** :
  - **part** : sous 0 à 2 h s'il est très anxieux, sinon sous 1 à 6 h ;
  - **hésite** : 15 % de probabilité au-delà de p ; il repart en 6 à 24 h si l'événement dure ;
  - **reste** : avec la raison écrite (méfiance envers l'autorité, métier, ne peut pas, attachement).
- **Destination** : un proche de la fiche qui vit dans une autre ville (« chez sa sœur à HNancy ») ; sinon un **centre d'accueil** d'une ville voisine non touchée.
- **Pendant le trajet**, l'avatar est très peu actif. **Une fois arrivé**, sa situation passe à « évacué » et elle est **mémorisée** : ville quittée, date, lieu d'hébergement.

### D4. Effets dans la vie, par le code, sans toucher à la fiche
- **Le bloc « TA VIE »** est complété par ce qui se passe chez lui. Par exemple : « Tu as quitté HToul hier à 18 h, tu dors au centre d'accueil de HNancy ; ton travail est à l'arrêt. » Ou : « HToul est confinée depuis ce matin : tu ne sors pas. »
- **L'activité** s'ajuste à l'événement :
  - confinement ou couvre-feu : ×1,3, chez soi ;
  - coupure du réseau : ×0,15 ;
  - bombardement : ×0,3 pendant la première heure (abri), puis ×1,5 ;
  - trajet d'évacuation : ×0,2 ;
  - et plus de « au travail » pour les confinés, les évacués, ou quand le lieu de travail est coupé.
- **Un choc d'humeur, une fois par événement et par avatar** : bombardement −45, évacuation −30, confinement et pénurie −15, coupure −10, route coupée −8, manifestation −5. L'émotion dominante suit : peur, tristesse ou agacement.
- **L'intérêt pour un thème est relevé** : « déplacés » pour les évacués, « vie quotidienne » pour les coupures et pénuries, « la FORCE et l'armée » pour les combats.

### D5. Fin et retour
- Quand l'événement prend fin (fin déclarée ou échéance), les évacués rentrent en 2 à 24 h. Leur situation passe à « rentré » pendant 24 h (« de retour chez toi depuis hier… »), puis s'efface.

### D6. Traçabilité
- Chaque départ, hésitation, refus et retour est inscrit au journal (« évacue », « refuse d'évacuer », « rentre »), avec la raison.
- Le panneau affiche le bilan par événement, par exemple « HToul : 6 évacués, 2 refus, 1 hésitant ».

## Garde-fous
- **La fiche n'est jamais réécrite** : la situation vit dans la mémoire d'exercice, qui s'efface en fin d'exercice avec elle.
- **Aucun lieu n'est inventé** : les destinations sont des villes déjà présentes dans la population, les centres d'accueil sont génériques, et les détails viennent de la description écrite par l'animation.
- **La détection automatique se limite aux comptes officiels de l'annuaire** : jamais un joueur ni une rumeur.
- Un bombardement ne fait jamais écrire de détail militaire (position, unités), et le mécanisme des fuites reste seul à pouvoir le faire.

## À mesurer
- la part d'évacués, d'hésitants et de refus par ville, et leurs raisons ;
- la cohérence de ce qu'ils écrivent (lieu où ils sont, travail, émotions) ;
- l'absence d'avatar qui « vit » encore dans sa ville d'origine après son départ.
