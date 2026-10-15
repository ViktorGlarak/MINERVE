# Avis PSYCHOLOGUE n°27 — Le « chœur du doute » : moins de doute général, plus de faits, d'idées et de questions

**Date** : 2026-10-15 · **Demandeur** : utilisateur · **Mise en œuvre** : PLEIADE (`app-ia`, `pont.mjs`, nouveau `doute.mjs`)

## Constat de l'utilisateur
Un avatar cite un joueur qui écrit « c'est un bot pro Mercure, ne perdez pas de temps avec eux ». Il commente : « Il dit que c'est un bot Mercure, mais c'est encore une info qui tombe sans preuve concrète… On va finir par croire que tout est faux, même le vrai ! On ne sait plus quoi penser de tout ce bazar #3615MyLife ».

> « Ce genre de commentaire n'apporte rien et on en voit beaucoup. C'est bien que les avatars se questionnent, mais on n'a pas besoin que tous partagent le même point de vue. Il faut qu'ils partagent des faits, une idée, qu'ils questionnent les joueurs pour apprendre des choses, pour essayer de soutirer des infos claires. »

## Lecture psychologique
- **Un biais du modèle, pas un trait de population.** Le « citoyen perplexe » est la posture refuge du modèle de langage : elle est sans risque, sans engagement et toujours plausible. Déjà relevé au 13/10 (« biais du sage citoyen »). Répétée par des dizaines d'avatars, elle fabrique un **faux consensus** : tout le monde doute de la même façon, avec les mêmes mots. C'est l'inverse d'une population réelle, où l'incertitude se dit de façons très différentes (on prend parti, on cherche, on se tait, on interroge).
- **Le doute utile pose une question.** Dans une vraie foule, celui qui doute vraiment **demande** : « tu l'as vu où ? », « c'était quand ? », « qui te l'a dit ? ». C'est l'**épistémique sociale** de la rumeur (Allport et Postman ; Shibutani, *Improvised News*) : face à l'ambiguïté, on cherche des informations auprès des autres. Ces questions font aussi travailler les joueurs, qui doivent sourcer et préciser, et elles donnent à l'exercice des **informations exploitables**.
- **Une perplexité qui reste tolérable.** Le doute général n'est pas interdit, mais il devient rare, comme le « moment de vie » (avis n°24).

## Décisions
- **P1. Repérer le doute général par le code** : « on ne sait plus quoi penser », « tout et son contraire », « le vrai du faux », « qui croire », « sans preuve », « on va finir par croire », « on verra bien », « quel bazar »…
- **P2. Un quota pour la population** : **un message de doute général toutes les 45 min au plus**, sur toute la population et pour tous les types (réponse, citation, publication spontanée). Au-delà, le message est réécrit **une fois** avec un apport :
  - **face à un joueur** : **une question précise** pour en savoir plus (ce qu'il a vu, où, quand, d'où il le tient, qui d'autre l'a vu), comme quelqu'un qui veut vraiment savoir, avec au plus une phrase de ce que l'avatar sait ou croit lui-même ;
  - **face à un avatar** : **ce que l'avatar en pense et pourquoi** (une raison, un fait de chez lui ou lu ailleurs), ou une question précise.
  - Si la réécriture doute encore ou est vide de substance, l'avatar ne publie pas : J'aime s'il est d'accord, sinon rien. Une publication spontanée est retenue.
- **P3. La citation d'un joueur sans apport devient une réponse.** On ne cite pas un joueur pour dire qu'on ne sait pas : réécrite en question, la citation passe en **réponse sous son message** (on s'adresse à lui, comme pour l'avis n°26 bis).
- **P4. Exemptions** : l'avatar interpellé (mention, réponse à son message) n'est pas soumis au quota, mais sa réécriture suit la même consigne. L'élan imposé (avis n°21) est exempté.

## À mesurer au prochain export
- la part des messages de doute général (cible : moins de 5 % des messages IA) ;
- le nombre de questions précises posées aux joueurs, et la part de joueurs qui y répondent ;
- la diversité des débuts de message.
