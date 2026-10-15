# Avis PSYCHOLOGUE n°26 — Un joueur engage la conversation sous le message d'un avatar

**Date** : 2026-10-15 · **Demandeur** : utilisateur · **Mise en œuvre** : PLEIADE (`app-ia`, `pont.mjs`, `conversation.mjs`, nouveau `sujets.mjs`)

## Cas observé (production, 15/10)
Un avatar cite un message sur un lieu de l'Est (charniers évoqués, accès refusé) et écrit en substance « on entend tout et son contraire, j'attends de voir les communiqués avant de trancher ». Un joueur lui répond sous sa citation avec des faits et deux hypothèses, en terminant par « on en saura plus quand les légistes pourront accéder aux emplacements ».

Demande de l'utilisateur : l'avatar visé doit pouvoir répondre, et **les avatars que ce sujet intéresse** doivent pouvoir donner leur avis.

## Lecture psychologique
- **Norme de réciprocité et attente comblée.** L'avatar a dit attendre une information, et on la lui apporte en s'adressant à lui. Ne rien répondre est un « second terme absent » qui se remarque, d'autant plus que l'interlocuteur est humain. Le message n'est ni une question ni une contradiction, mais c'est une **contribution informative adressée**. Socialement, elle appelle une réponse plus qu'une simple approbation.
- **Notification = interpellation.** Recevoir une réponse à son propre message est vécu comme être nommé : on la voit d'abord, et on se sent tenu d'y donner suite. Un avatar « lecteur », discret par tempérament, se tait devant le flux, mais il répond quand on lui parle. C'est déjà la règle pour une mention ; elle doit valoir pour une réponse.
- **Attention sélective par l'intérêt.** Dans un fil, on s'arrête sur ce qui touche nos préoccupations : biais d'attention vers les stimuli pertinents pour soi, effet « cocktail party ». Les sensibilités de la fiche (« la FORCE et l'armée », « Mercure », « haine et racisme », « rumeurs »…) doivent orienter ce que l'avatar lit en premier, au moins pour les messages des joueurs, que l'exercice cherche à faire vivre.

## Décisions
- **P1. Retour dans la conversation.** Un message de **plus de 80 caractères** qui répond à l'avatar compte comme une contribution : probabilité de retour **0,6**, comme une question. Venant d'un **joueur**, elle monte à **0,7**, la mention restant à 0,8. Les bornes ne changent pas : 2 retours par fil et par joueur, 12 h.
- **P2. Une réponse à son message est une interpellation partout.** Elle lève la conversion « lecteur → J'aime », le plafond de la population et le plafond horaire (+1), comme une mention.
- **P3. Attirance par le sujet**, pour les messages de joueurs seulement. Le code repère les thèmes du message, et de son parent, par mots-clés. Il ajoute au tri de lecture **l'intérêt effectif de l'avatar pour le thème le plus fort, au-delà de 40**, soit 0 à 60 points. Pas pour les messages d'avatars, pour ne pas créer de chambres d'écho IA.
- **P4. Garde-fous inchangés.** Au plus 2 réponses IA en 30 min sous un même message, 4 au total. Tout le reste est conservé : le juge de pertinence, le contrôle d'orientation, la relecture, et l'interdiction de toute information militaire.

## À mesurer au prochain export
Pour les messages de joueurs adressés à un avatar :
- le taux de réponse de l'avatar visé (cible 50 à 70 %) ;
- le nombre d'autres avatars qui interviennent (cible 1 à 2, jamais plus de 4) ;
- l'adéquation entre les sensibilités de ceux qui interviennent et le thème ;
- l'absence de réponses génériques.

## Addendum n°26 bis — la réponse parlait du joueur au lieu de lui parler (constat utilisateur, même matinée)
L'avatar a répondu, mais à la troisième personne (« J'ai vu passer les infos de @… sur les charniers… #3615MyLife »). Cause : ce n'était pas une réponse du modèle, c'était une **publication inspirée** du message du joueur, que le moteur range sous ce message sans la réécrire. Psychologiquement, c'est un contresens de position : on ne commente pas quelqu'un **devant lui**, sous son propre message, comme s'il était absent.

**Décision P5** : avant d'être rangée sous un message, la publication est **réécrite en adresse directe** (tu ou vous, selon le registre de l'avatar), en réponse à ce que la personne dit, sans @ ni nom à la troisième personne, et en ne gardant que les mots-dièse du fil. Si la réécriture échoue, elle n'est pas rangée sous le message.

**Mise en œuvre** : app-ia 2026-10-15.2.
