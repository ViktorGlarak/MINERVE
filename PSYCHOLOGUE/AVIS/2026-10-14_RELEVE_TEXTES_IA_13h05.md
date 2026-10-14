# Relevé des textes des avatars IA face aux joueurs — 14/10/2026, 7 h 37 → 13 h 05

**Auteur** : NOYAU (Claude Code), à la demande de l'utilisateur (« analyse tous les textes, les réponses des IA par rapport aux messages des joueurs, pour qu'on continue à améliorer le comportement de l'IA »).
**Source** : `moteur-ia_export_jour_2026-10-14_le_2026-10-14_1305.json` (rangé dans `%USERPROFILE%\.pleiade\analyses-ia\`). Lu en entier : 186 textes IA (73 publications, 95 réponses, 18 partages), 430 messages de joueurs, 627 événements du réseau social.
**Règle de ce fichier** : il part sur GitHub. Les textes des avatars IA (fictifs) sont cités ; **les messages des joueurs sont résumés, sans nom de compte**.
**Contexte** : l'avis n°22 (13/10) n'a pas été mis en œuvre (pause demandée par l'utilisateur) ; ce relevé en confirme les mesures et en ajoute.

---

## 1. Ce qui marche

- **Réactivité à l'événement** : l'attaque chimique annoncée à 10 h 09 est reprise dès 10 h 11 ; une trentaine de réponses dans l'heure, adressées aux joueurs inquiets (« on est enfermés », « ma grand-mère ne répond pas »). Les conseils donnés sont plausibles et utiles au jeu (rester à l'abri, attendre les consignes).
- **Géographie locale tenue** : chacun parle depuis sa ville (HToul, HFrouard, HSaint-Dizier…), avec des détails de métier (dépôt, labo photo, livraisons, boulangerie).
- **Garde-fous actifs** : formules creuses retirées (« Courage à vous » ×10), tics de la population détectés, invention de proche refusée (« Ma cousine »), relecture qui corrige.
- **Quelques vraies voix** : un avatar demande une source pour le chiffre de 616 morts ; un autre relève que l'image météo ne montre aucun nuage ; un autre ironise sur « la chair à canon ».

## 2. Mesures

| Mesure | Avatars IA | Joueurs | Avis n°22 (13/10) |
|---|---|---|---|
| Points de suspension « … » | **68 %** (127/186) | 5 % | 73 % |
| Émoji en fin de message | **83 %** (154/186) | 18 % | 89 % |
| Finit par 2 hashtags ou plus | **60 %** (111/186) | — | — |
| Commence par une minuscule | 0 % | 24 % | — |
| Registre SMS (jsp, wsh, askip…) | 0 | 8 | — |
| Longueur médiane (hors #) | **156 car.** | ≈ 65 car. (extraits) | 172 |
| « on ne sait plus / quoi croire » | 12 % | — | — |
| « préfecture / Info.gouv » | 13 % | — | — |
| Messages de joueurs ayant reçu une réponse IA | 78/430 (18 %) | — | — |
| Joueur qui répond à un avatar IA → l'IA revient | **0/8** | — | « auteur revient 4/134 » |
| Questions directes de joueurs sans réponse IA | 7/19 | — | — |
| Réponses IA → IA | 13/113 (12 %) | — | 7 |
| Réponses qui contredisent ou demandent une source | ≈ 5/113 | — | 7/116 |

## 3. Défauts, par ordre de gravité

### 3.1 ⚠ L'orientation des avatars est écrasée (effet ILI inversé)
37 textes viennent d'avatars **pro-Mercure** (cohorte et `orientation_initiale`). **Aucun ne défend Mercure**, et plusieurs **doutent de Mercure** :
- DomyKos_87 (pro-mercure-modéré) : « j'ai un doute sur ces histoires de cérémonies officielles de Mercure… »
- Rb_4ever (pro-mercure-modéré), pensée : « si le conflit s'enclenche vraiment à cause de l'influence de Mercure »
- _OlegGaspi_ (pro-mercure-affirmé) : « On nous avait promis que ce serait une opération de maintien de l'ordre… »
La fiche dit pourtant « [orientation] il est déçu de la FORCE et pense que Mercure est mal compris ; il le dit ouvertement ».
Pendant ce temps, un **fil de joueurs pro-Mercure** (hommage aux soldats, honneur, respect) est lu par **26 avatars** : 25 l'ignorent. Les avatars de son camp ne s'y joignent pas.
→ Le modèle ramène tout le monde à une voix **neutre, inquiète et prudente**. C'est l'erreur que la règle de camp du dépôt veut éviter : un avatar qui dit l'inverse de son camp produit l'effet ILI inverse.

### 3.2 Réponses hors sujet : « inspirée de X → réponse sous son message »
Le moteur range sous un message une publication de vie inspirée par lui. Résultat : des réponses qui ne répondent pas.
- À « bonne nuit, demain café et grandes ambitions » : KrapovicOlga répond par son café et ses stocks de légumes.
- À un message de soutien entre mères (« faites passer ») : Domi_Borie95 répond sur les camions et les routes.
- À une jeune réfugiée qui décrit sa famille calfeutrée : CosmoTrak répond « je vais vérifier le sac de mon fils ».
- À un message d'angoisse sur des proches disparus : Sacha_GreenPen_2000 parle de sa scie circulaire.
Au moins 10 cas. Pour un joueur, c'est un interlocuteur qui ne l'a pas lu.

### 3.3 Le joueur qui répond n'a jamais de suite
8 joueurs ont répondu à un avatar IA : **aucune** suite. L'avatar visé ne revient pas, même mentionné. L'effet « notification » poussé le 13/10 (2026-10-13.4) ne se voit pas en production. Les 7 questions directes restées sans réponse ne sont pas des messages de foule : elles visaient quelqu'un.

### 3.4 Biais de « citoyen sage » du modèle
13 % des textes renvoient vers la préfecture ou Info.gouv, 12 % disent « on ne sait plus quoi croire ». La population entière a la même émotion : la peur, le doute, l'appel au calme. Pas de colère franche, pas de déni, pas de complotisme, presque pas d'humour, aucune accusation (2 textes sur 186), alors que les joueurs accusent, ironisent et s'emportent.

### 3.5 Forme reconnaissable (moule de l'avis n°22, toujours là)
« … » 68 %, émoji final 83 %, médiane 156 caractères, aucune minuscule ni abréviation. Les joueurs écrivent court, sans ponctuation soignée, parfois en SMS.

### 3.6 Hashtags plaqués
`# du fil repris` recopie tous les hashtags du parent (60 % des textes finissent par 2 hashtags ou plus). On trouve donc **#freegrandest #mercure** sous un café en terrasse ou une sacoche de facteur. Par défaut, `sans # → #3615MyLife` colle ce hashtag à des messages qui n'en ont pas besoin. Sur un vrai réseau, on ne remet presque jamais les hashtags en répondant.

### 3.7 Mentions inventées
Les mentions sont fabriquées depuis le nom affiché (« @rolf_weber », « @caroline_denis », « @marie_duval », « @norbert_petrescu »…), sans vérifier que le compte existe sous ce nom. Il y a aussi 3 mentions sans « @ » (« _DFataliste encore une rumeur… »). **À vérifier** côté réseau social : ces @ mènent-ils au bon profil ?

### 3.8 Fautes de ton et de langue
- Émoji déplacé : « j'en ai la tête qui tourne 😂 » à propos d'armes chimiques (donpedro).
- Réponse blessante à quelqu'un qui ne joint pas sa mère : « On ne sait jamais si c'est vrai ce que vous écrivez ici » (Aberkane_Therese_Peintre).
- Expressions fausses : « c'est l'hôpital qui se fout de la charité » mal employée, « c'est mieux vaut mieux », « Le tractor », « un vrai casse-dalle » pour une livraison difficile.
- Phrases inachevées encore publiées après « reformulation sans mieux » (KrapovicOlga 9 h 25, Grigori_elec 9 h 41, K_Rud_85 11 h 44).
- Pensée et texte qui divergent : la pensée parle de céréales du petit, le texte d'un camion de convoi (Kuz_MarketingPro).

## 4. Pistes, à faire valider par PSYCHOLOGUE avant mise en œuvre

1. **Orientation d'abord** : la position du camp devient une contrainte de sortie vérifiée par la relecture (un pro-Mercure qui doute de Mercure → reformulé ou retenu). Les avatars d'un camp sont attirés par les fils de leur camp (fil pro-Mercure ci-dessus).
2. **Fin de la « réponse inspirée »** : une publication de vie ne se range plus sous le message d'un autre ; elle part en publication. Une réponse doit répondre au contenu du parent (contrôle par la relecture).
3. **Suivi de conversation** : quand un joueur répond à un avatar ou le mentionne, cet avatar est prioritaire au tour suivant (lecture et réponse permise), dans la limite d'un ou deux échanges.
4. **Questions directes** : un message avec « ? » adressé à quelqu'un, ou à tous, a une probabilité de réponse plus haute.
5. **Diversité émotionnelle par tempérament** : la colère, le déni, l'ironie, la défiance envers les autorités sont permis selon la fiche ; plafond de population pour « préfecture » et « on ne sait plus ».
6. **Forme** : reprendre l'étape 1 de l'avis n°22 (plafonds émoji / « … », formes courtes, minuscules et abréviations selon le gabarit).
7. **Hashtags** : en réponse, 0 hashtag par défaut (1 au plus, s'il sert) ; ne plus forcer #3615MyLife ; pas de hashtag d'actualité sur un message de vie.
8. **Mentions** : n'écrire un @ que pour un compte réel (handle exact pris dans l'événement), sinon le nom sans @.
9. **Langue et ton** : interdire 😂 et les émojis légers sur un sujet de mort, de blessure ou d'arme ; une phrase inachevée est retenue, jamais publiée.
