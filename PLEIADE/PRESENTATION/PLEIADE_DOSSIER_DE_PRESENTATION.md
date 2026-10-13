# PLÉIADE — Dossier de présentation

> **État au 13 octobre 2026.** Document source destiné à une IA chargée de produire des supports (diaporamas, fiches, schémas) qui expliquent PLÉIADE : ce que c'est, d'où ça vient, comment ça marche et ce que ça permet, en particulier avec les nouveautés de l'exercice **DELATTRE 26**.
>
> Mention à reporter sur tout support : **« Exercice · non classifié »**. Tous les pays, personnages, médias et villes cités sont **fictifs** (univers d'entraînement Skolkan) ; les villes fictives portent le préfixe « H » (HNancy, HToul…).

---

## 0. Mode d'emploi pour l'IA qui produit les supports

- **Public visé** : décideurs et cadres de la Défense (commandement, CECPC, futurs utilisateurs en écoles et en régiments), animateurs d'exercice, et partenaires techniques. **Expliquer sans jargon** : chaque terme technique est défini au glossaire (§12).
- **Ton** : factuel, concret, orienté usage (« ce que l'outil permet de faire à l'exercice »). Pas de superlatif non étayé.
- **Structure suggérée** pour un diaporama : voir le §13 (plan en 18 diapositives) ; une version courte de 6 diapositives est proposée aussi.
- **Messages clés** à faire ressortir : §1.
- **Ce qu'il ne faut PAS mettre** sur un support : voir §14 (adresses réseau, détails de sécurité internes, chiffres incertains).
- Les **chiffres** du §11 sont vérifiés à la date du document ; ceux qui sont approximatifs sont signalés « environ ».

---

## 1. PLÉIADE en une phrase, et les messages clés

**En une phrase :** PLÉIADE est la plateforme d'entraînement du CECPC qui déploie en quelques minutes, pour chaque exercice, un **espace informationnel complet et fermé** (réseau social, presse, messagerie, fiches de personnages, planche des injects, outils de mesure), dans lequel les joueurs agissent et où l'animation **pilote, mesure et fait réagir** cet espace, y compris avec une **population d'avatars animés par intelligence artificielle**.

**Les 4 arguments** (repris de la présentation du développeur de la plateforme) :
1. **Réalisme** : les joueurs travaillent sur des outils qui ressemblent à ceux du monde réel (réseau social façon X, sites de presse, messagerie), peuplés de personnages crédibles.
2. **Rapidité** : un exercice se monte en déployant une « zone » et ses applications en quelques minutes, au lieu de bricoler des outils à chaque fois.
3. **Isolation** : tout se passe sur un réseau fermé, accessible par VPN seulement. « Un exercice de crise fabrique de fausses rumeurs et de faux communiqués : ils doivent rester dans la salle. »
4. **Reproductibilité** : ce qui a été construit pour un exercice (personnages, médias, scénarios) se réutilise pour le suivant.

**Les deux formules à employer** (fixées par l'utilisateur le 10/10/2026) :
- **« Plateforme SaaS modulaire »** : chaque exercice assemble les modules dont il a besoin, comme des briques.
- **« Digital workspace »** : un seul espace de travail, une seule connexion, une même barre « Apps de la zone » pour passer d'un outil à l'autre.

**Le message de fond :** PLÉIADE est né du terrain. Chaque exercice a révélé un manque, et chaque manque a produit un outil (§2). Avec DELATTRE 26, la plateforme franchit un cap : elle ne se contente plus de **diffuser** des injects, elle **mesure l'impact informationnel des joueurs** et fait **réagir une population simulée** de façon crédible.

---

## 2. D'où vient PLÉIADE : six mois d'évolution guidée par les exercices

| Quand | Exercice / étape | Constat (le problème) | Réponse (ce qui a été créé) |
|---|---|---|---|
| **Avril 2026** | **ORION 26** (région Poitiers / Vienne, du 2 au 9 avril) | Découverte de **Mastodon** installé sur un serveur du COMCYBER : il ne fonctionne pas pour l'exercice. Presse, messagerie, réseau social et avatars existaient déjà, mais séparément. | Optimisation et création de **MASTORION** (réseau social d'exercice) et d'un premier **COCKPIT**, premier outil de **mesure et de suivi** de ce qui se passe sur le réseau. |
| **Mai 2026** | **AURIGE 2BB** (niveau brigade, Lorraine ; chef d'orchestre éditorial « GUILLAUME ») | **JEMM** (l'outil de gestion des injects) n'est pas adapté à l'**influence**. Les joueurs n'ont **pas d'accès Internet**. | Création de **MELMIL** (planche des injects d'influence), de l'**EHO** (fiches des personnages) et de la **presse en pages HTML**, le tout **interopérable** et transmissible **par mail, en ZIP**. Synchronisation **manuelle** de JEMM vers MELMIL. |
| **Juin–juillet 2026** | **MINOTAURE 26** (AURIGE 7BB, clos le 3 juillet) | Le modèle « ZIP par mail » montre ses limites : une copie par poste, des fusions à la main. Le RETEX relève aussi : pas de boucle de retour sur le traitement des injects (« on travaille dans le vent »), **impact de l'influence non mesurable** (« so what ? »), fiches de personnages faites deux fois, besoin d'un **annuaire des avatars**. | Amélioration de MELMIL, de l'EHO et de la presse, toujours diffusés par ZIP. Le RETEX recommande de **s'appuyer sur MASTORION / MASTAURIGE** pour la suite. |
| **Août 2026** | **Fusion** | Deux lignées d'outils se recoupent : l'outillage hors ligne **MASTAURIGE** (MELMIL, EHO, presse HTML) et le réseau social client-serveur **MASTORION**. | **Fusion de MASTAURIGE et de MASTORION : naissance de PLÉIADE.** *(Le nom PLÉIADE est officialisé le 11 septembre ; « MASTORION » ne désigne plus que le réseau social, lui-même renommé « social » le 16 septembre.)* |
| **Septembre 2026** | **Serveur CECPC** | Passer d'outils sur chaque poste à **une seule base qui fait foi**, accessible à tous. | **Installation du serveur au CECPC** et de PLÉIADE dessus, **accessible par Internet via VPN**. Première mise en production d'une application (LEAC) le 17 septembre ; MELMIL rejoint la plateforme le 22–23 septembre. |
| **Octobre 2026** | **DELATTRE 26** (niveau division, du 6 au 20 octobre) | Il faut **mesurer l'impact informationnel des joueurs** dans la sphère, et que cette sphère **réagisse**. | **MELMIL intégré au jeu** ; **premiers avatars « socialement augmentés » par IA** ; **COCKPIT amélioré** pour mieux mesurer ; amélioration de tous les outils MELMIL ; **titres de presse supplémentaires** ; **chat** intégré au réseau social (réponse au besoin exprimé par la **LLE**). |

**Ce qu'il faut retenir de cette histoire :** on est passé de **fichiers HTML envoyés par mail** (un exemplaire par poste, sans mesure) à une **plateforme serveur unique** (une seule base, mise à jour en direct, mesurée), puis à un **espace informationnel vivant** (une population simulée qui lit, réagit et change d'avis).

---

## 3. Le principe : une zone par exercice, des applications à la carte

### 3.1 La zone
- Une **zone** = **une bulle étanche par exercice** (par exemple « DELATTRE 26 »). Elle a ses propres comptes, ses propres données, ses propres adresses.
- Ce qui se passe dans une zone **ne fuit pas** dans une autre : on peut faire tourner plusieurs exercices en même temps, ou une zone d'essai à côté de la zone de production.

### 3.2 Les applications (le catalogue)
- Dans chaque zone, on **déploie les applications** dont l'exercice a besoin, choisies dans un **catalogue** (§4). Une application déployée dans une zone s'appelle une **instance**. On peut avoir plusieurs instances du même type (par exemple **plusieurs titres de presse**).
- L'**orchestrateur** PLÉIADE fait le travail technique tout seul : il crée l'application, sa base de données, son accès sécurisé et son adresse.

### 3.3 Une seule identité partout
- Chaque **personnage** (avatar) existe **une seule fois**, dans l'**EHO** (l'annuaire des personnages de la zone), et garde **la même identité dans toutes les applications** : il publie sur le réseau social, signe dans la presse, écrit dans la messagerie, toujours le même.
- Chaque **personne réelle** (joueur, animateur, administrateur) se connecte **une seule fois** et passe d'une application à l'autre par la barre **« Apps de la zone »**.

### 3.4 Comment les applications se parlent (4 mécanismes simples)
1. **Identité unique** : tout le monde se réfère au même identifiant de personnage, fourni par l'EHO.
2. **Découverte automatique** : chaque application demande à la plateforme quelles autres applications existent dans sa zone, et les trouve seule.
3. **Clé de service par zone** : les programmes (par exemple, la publication programmée d'un inject) peuvent agir même quand personne n'est connecté, mais seulement dans leur zone.
4. **Contrat commun** : le réseau social, la presse et la messagerie acceptent les mêmes ordres de publication. La console d'animation peut donc publier n'importe où sans connaître le détail de chaque outil.

### 3.5 Mise à jour en continu
- Les améliorations sont **déployées pendant l'exercice**, sans l'interrompre : une nouvelle version validée est mise en ligne et la zone se met à jour d'elle-même. Chaque mise en ligne est tracée dans des **notes de version**.
- Règle de travail : **tout est testé sur une copie locale avant d'être mis en ligne**.

---

## 4. Le catalogue des applications

| Application | À quoi elle sert | Qui l'utilise |
|---|---|---|
| **EHO** (l'annuaire des personnages) | Les **fiches de tous les avatars** de l'exercice (environ 4 000 sur DELATTRE 26) : identité, camp, groupes, portrait, biographie, trombinoscope, relations. C'est la **source d'identité de toute la zone**. Les joueurs y voient les fiches qu'ils ont le droit de voir (« STARTEX » : les autorités officielles connues au départ). | Administration, animation, joueurs (vue limitée) |
| **Réseau social** (« social ») | Un réseau social **façon X / Twitter** (habillages possibles : Mastodon, Facebook, Instagram, YouTube). On publie toujours **« au nom de » un personnage**. Réponses, citations, J'aime, favoris, sondages, lieux, « Qui peut répondre ? », programmation de publications, **chat privé entre avatars**. | Joueurs et animation |
| **Console d'animation** (« Animation ») | Écrire et **programmer des scénarios** multi-applications (qui publie quoi, où, quand), importer depuis un tableur, se greffer sur une publication existante, y compris celle d'un joueur. Chaque scénario est **rattaché à un incident de MELMIL**. Scénarios de « bruit de fond ». | Animation (cellules GREYCELL, FORAD) |
| **MELMIL** (la planche des injects) | La **planche de jeu de l'influence** : events, storylines, incidents, **alimentée par les exports de JEMM**. Atelier de préparation, **demandes de produit** vers la cellule de production, **déroulé** heure par heure, comptes rendus, **impression de l'A4 à l'A0**. | Animation (accès réservé : « une planche d'injects ne se montre pas à ceux qui la subissent ») ; joueurs pour les demandes seulement |
| **Presse** | Des **sites de presse** crédibles : un site public et une rédaction. **Une instance = un titre** (chaînes et journaux fictifs, organisations internationales, préfecture…). Articles programmables, PDF joints, aperçu avant publication. | Rédacteurs (animation), lecteurs (tous) |
| **Messagerie** | Une **messagerie façon Telegram** : canaux, groupes, conversations privées, envois programmés. « Là où une rumeur naît avant d'atteindre les réseaux ouverts. » | Animation, joueurs |
| **COCKPIT** (veille et mesure) | **Tout voir sur un seul écran** : veille multi-réseaux par sources, relevé en continu, disposition personnelle. Et surtout le **Reporting** : l'activité heure par heure, par cellule, par hashtag, et l'**opinion de la population simulée** (§7). | Analystes, animation |
| **Moteur IA** | Le **cerveau des avatars animés par IA** (§6) : tableau de bord, journal, réglages, **parc de calcul**. | Administration |
| **LEAC** | Le logiciel de **contrôle des postes de commandement** (CECPC / CNCIA / EMAT) : notation sur **tablette hors ligne** sur le terrain, regroupement par VPN au retour. Nouvelle version (v3) d'un logiciel de 2022, désormais application PLÉIADE. | Contrôleurs, chefs de contrôle |
| **Serveur de fichiers** | Mettre à disposition des fichiers et des pages statiques (par exemple des sites HTML d'exercice). | Animation |
| **WordPress** | Un site WordPress classique relié à la connexion de la zone. | Selon besoin |

**Repère** : 11 applications au catalogue au 13/10/2026, chacune dans son propre dépôt de code (règle **« 1 application = 1 dépôt »**), dans l'organisation GitHub `cecpc-pleiade`.

---

## 5. Qui fait quoi : les acteurs et leurs droits

### 5.1 Trois profils
- **Administration** : a la main sur tout (création de la zone, des comptes, des modèles, du moteur IA).
- **Animateurs** (cellules d'animation **GREYCELL** et **FORAD**) : préparent et jouent les injects, animent les personnages, suivent la mesure.
- **Joueurs** (sur DELATTRE 26 : l'état-major de la **1re Division**, et les brigades) : agissent dans l'espace informationnel avec leurs propres avatars et voient ce qu'un acteur réel verrait.

### 5.2 Des camps et des groupes
- Chaque avatar appartient à des **groupes** dans l'EHO. Trois groupes seulement désignent un **camp** : **CAMP ROUGE**, **CAMP BLEU**, **CAMP NEUTRE**.
- Les avatars sont **répartis par cellule** : chaque cellule anime les siens (par exemple CAMP ROUGE pour FORAD, CAMP BLEU pour GREYCELL, CAMP DIV1 pour les joueurs).
- Les **avatars IA** forment un groupe **à part** (« CAMP IA ») : ils ne sont joués par personne.

### 5.3 Des règles appliquées côté serveur
- Un joueur **ne peut pas** voir ce qui ne lui est pas destiné, même en bricolant l'adresse : chaque application vérifie les droits **sur le serveur**, pas seulement à l'écran.
- Les **comptes de zone sont anonymes** (pas d'adresse mail, pas de nom réel) : aucun lien entre un compte et une personne.
- L'**origine réelle** d'une publication (qui l'a vraiment écrite, quelle cellule) n'est visible **que de l'animation**.

---

## 6. ⭐ Nouveauté DELATTRE 26 : les avatars « socialement augmentés » par IA

### 6.1 Le besoin
Sur les exercices précédents, le réseau social ne réagissait **que** si un animateur écrivait. Résultat : un espace informationnel figé, où l'action des joueurs n'avait pas d'écho mesurable. DELATTRE 26 a besoin d'une **population** qui **lit**, **réagit**, **se souvient** et **change d'avis** selon ce que les joueurs et l'adversaire publient.

### 6.2 Ce qui a été fait
- **105 avatars animés par IA** sur DELATTRE 26 : **100 citoyens de l'Arnland** (le pays fictif envahi), orientés **15 % pro-Mercure, 15 % pro-Arnland, 70 % neutres**, plus 3 avatars de test et 2 relais mercuriens.
- Chacun a une **fiche complète** : âge, métier, foyer, horaires, caractère, goûts, façon d'écrire, positions de départ.
- Ils **vivent** : ils se lèvent, travaillent, dorment ; au travail ils écrivent peu ; le dimanche certains commerces sont fermés. Ils parlent de leur vie (« Fin du café, je remonte dans le bus. Je pense aux gens qui attendent sur la route. 🚌 ») autant que de la crise.
- Ils **réagissent** aux publications des joueurs et de l'adversaire : J'aime, réponse, citation, ou silence. **Comme dans la vraie vie, la plupart lisent beaucoup et écrivent peu.**

### 6.3 Comment ils « pensent » : le code fait la psychologie, l'IA fait l'expression
C'est le point central à expliquer. Le modèle d'IA **ne décide pas seul** : un programme tient la psychologie de chaque avatar, et l'IA sert à **lire** et à **formuler**.

| Ce que tient le PROGRAMME (règles chiffrées, sourcées en psychologie) | Ce que fait l'IA |
|---|---|
| **L'humeur**, qui monte, retombe et revient vers un état de repos propre au caractère | **Lire** les publications du fil et comprendre ce qu'elles disent |
| **La mémoire** : souvenirs classés par importance, consolidés la nuit, rappelés par le sens | **Formuler** la réaction (pensée, puis texte) dans la voix du personnage |
| **Les relations** avec chaque compte : familiarité, sympathie, confiance, rancune | **Décrire** une image jointe, à l'étude |
| **Les opinions** sur des axes (la Force alliée, Mercure, les institutions, le groupe N.O.M…), qui bougent avec la crédibilité de la source, la répétition, l'émotion, la pression du groupe | |
| **Les bascules** d'opinion, avec une phase de doute (un avatar convaincu résiste ; il peut finir par changer de discours) | |
| **Qui lit, quand, et qui réagit** | |

**Garde-fous** : un **interrupteur général** (coupé par défaut, relu toutes les 15 secondes) ; des **interdits absolus** (aucune insulte, aucune information militaire, ne jamais se dire IA, ne rien inventer qui ne soit dans la situation) ; des **plafonds** de messages par heure ; une **relecture automatique** de chaque message écrit avant publication ; une **alerte de dérive** ; des bascules limitées par heure. L'animation garde la main : geler, imposer, arrêter.

### 6.4 Les derniers progrès (12–13 octobre 2026)
- **Un « rédacteur » dédié** : un premier passage décide de la réaction, un second écrit le texte, court et naturel, sans formules toutes faites. Les messages sont devenus plus courts et plus concrets (une offre précise remplace un « courage à tous »).
- **Un dictionnaire des émotions** (36 nuances en 11 familles, construit à partir de travaux de psychologie) : l'avatar n'est plus « triste » ou « joyeux » mais **las**, **sceptique avec réserve**, **fier de son équipe**, **agacé**… et cela se **voit à sa façon d'écrire** plutôt qu'il ne le dit. Objectif : casser la monotonie (au début, toute la population avait la même humeur).
- **Des fiches cohérentes** : les 105 profils ont été contrôlés et corrigés (âge, foyer) pour que l'IA ne reçoive jamais deux versions contradictoires d'un même personnage.
- **Un parc de calcul en grappe** (§8.2) : le travail est réparti sur plusieurs ordinateurs, avec reprise automatique si l'un s'arrête.

### 6.5 Quelques chiffres mesurés (à citer avec leur contexte)
- ⚠ **Correction du 13/10** : deux chiffres d'une version précédente de ce dossier étaient présentés à tort comme des réussites.
  - « environ 37 % des événements » vient d'une fenêtre de **24 minutes** (12/10, 9 h 46 à 10 h 10), dont l'analyse relevait surtout un **chœur de formules** (15 réponses sur 16).
  - « 1 004 lectures pour 138 messages de joueurs » vient d'un **diagnostic** (12/10, 1 h 25) : **4 publications de joueurs sur 42 seulement** avaient reçu une réponse de l'IA. Le défaut a été **corrigé le jour même** : un message de joueur qui inspire un avatar reçoit désormais une réponse sous ce message.
  - **Ne pas les utiliser comme preuves de succès.** Ils illustrent au contraire la **boucle d'amélioration** : relevé, diagnostic, correction en quelques heures.
- Chiffres fiables pour un support :
  - **105 avatars IA**, dont 100 citoyens de l'Arnland (15 % pro-Mercure, 15 % pro-Arnland, 70 % neutres), 3 de test et 2 relais mercuriens ;
  - **environ 3 secondes** par texte écrit ;
  - **environ 13 secondes** par machine pour la lecture complète d'un fil par un avatar.
- **Effet du rédacteur, en essai local** (13/10, avec groupe témoin) : des messages plus courts (135 caractères contre 177 pour le témoin) et quasiment plus de formules creuses. À présenter comme un **résultat d'essai**, pas comme un résultat de production.

---

## 7. ⭐ Nouveauté DELATTRE 26 : mesurer l'impact informationnel (COCKPIT)

### 7.1 Le besoin
Le RETEX de MINOTAURE 26 était clair : **l'impact de l'influence n'était pas mesurable** (« so what ? »). Sans mesure, impossible de dire à un état-major si son action informationnelle a porté.

### 7.2 Ce que mesure le Reporting du COCKPIT
- **L'activité** heure par heure, par **série** (par exemple : 27e BIM, 1re DIV, FORAD, GREYCELL, autres comptes), en direct ou dans le temps.
- **Ce que publie chaque cellule**, et si c'était programmé ou en direct.
- **Les hashtags** : qui reprend quel mot d'ordre, en nombre et en part (un hashtag repris est le signal qu'une campagne « prend »).
- ⭐ **L'opinion de la population simulée** :
  - où se situe la population sur chaque axe (la Force alliée, Mercure, les institutions…) ;
  - **qui fait bouger l'opinion** : les joueurs et l'animation, les avatars IA eux-mêmes, ou les faits ;
  - **quels avatars sont ébranlés** (en train de douter) ;
  - une courbe par série de comptes.

**Ce que ça change** : pour la première fois, on peut **montrer à un joueur l'effet de son action** sur une population, et pas seulement compter ses publications.

---

## 8. Ce qui tourne « sous le capot »

### 8.1 Le serveur et l'accès
- Un **serveur au CECPC** héberge la plateforme et toutes les zones.
- **On n'y entre que par VPN**, avec un **profil nominatif**, révocable individuellement. Aucune adresse publique, rien d'indexable sur Internet.
- **Connexion unique** pour toutes les applications d'une zone, gérée par **Keycloak** (un « royaume » de connexion par zone).

### 8.2 Le calcul de l'IA : local, et réparti
- **Le modèle d'IA tourne en local**, sur des ordinateurs de l'équipe, et **jamais dans un service en ligne** : les messages de l'exercice ne sortent pas du réseau fermé.
- Modèle utilisé : **Gemma 4** (Google, **licence libre** Apache 2.0, ce qui n'est pas « libre de droits »), version 26B, rapide car seule une petite partie du modèle travaille à chaque mot.
- Le serveur n'ayant pas de carte graphique, il confie le calcul à des **« nœuds de calcul »** joints par le VPN, chacun protégé par un **jeton** et un **pare-feu** dédiés.
- **Le parc de calcul** (nouveau, 13/10) : un PC et un Mac sont branchés ; chaque avatar est rattaché à une machine ; **si une machine s'arrête, ses avatars sont repris automatiquement** par une autre. Deux machines font tourner les cycles environ **deux fois plus vite** : les avatars lisent leur fil plus souvent et réagissent plus vite. On peut ajouter d'autres machines pour aller vers une population plus nombreuse.

### 8.3 La sécurité (en clair)
- **Réseau fermé**, accès par VPN nominatif.
- **« Être sur le VPN ne donne aucun droit »** : chaque application vérifie elle-même qui vous êtes et ce que vous avez le droit de faire (principe du « zero trust » recommandé par l'ANSSI).
- **Comptes anonymes**, droits vérifiés côté serveur, aucun secret dans le code.
- Une doctrine de sécurité fondée sur **11 guides de l'ANSSI**, et un référent cybersécurité consulté à chaque décision touchant la sécurité.
- **IA locale uniquement** pour la génération des messages.

---

## 9. Un exercice avec PLÉIADE, vu de bout en bout (exemple DELATTRE 26)

1. **Préparer** : l'administration crée la zone « DELATTRE 26 » et y déploie les applications. L'EHO est rempli à partir d'un **modèle de personnages** réutilisable (des centaines d'avatars, groupes et portraits déjà prêts).
2. **Concevoir le jeu** : l'animation importe les **exports de JEMM** dans **MELMIL** (events, storylines, incidents) et prépare les injects dans l'atelier.
3. **Programmer** : dans la **Console d'animation**, chaque inject devient un scénario daté (publication sur le réseau social, article de presse, message), **rattaché à son incident MELMIL**.
4. **Jouer** : les joueurs consultent le réseau social, la presse et la messagerie, publient avec leurs avatars, répondent, démentent. Les animateurs font vivre les personnages adverses et neutres.
5. **Faire réagir** : la **population IA** lit le fil, réagit, se souvient, et voit son opinion bouger selon qui occupe l'espace informationnel.
6. **Mesurer** : le **COCKPIT** montre en direct l'activité, la reprise des hashtags et **l'évolution de l'opinion** ; MELMIL suit le déroulé et les demandes de produits.
7. **Restituer** : comptes rendus (PSYREP, CIMICREP…), impression de la planche, données pour le **RETEX**.

---

## 10. Ce que PLÉIADE permet, en résumé

- **Entraîner** un état-major à la **lutte informationnelle** dans un espace réaliste et fermé.
- **Monter** un exercice vite, et **réutiliser** personnages, médias et scénarios d'un exercice à l'autre.
- **Piloter** l'animation à partir d'une **planche d'injects unique** (MELMIL), reliée à JEMM.
- **Faire vivre** l'espace informationnel avec une **population simulée crédible**, qui ne dépend pas du nombre d'animateurs disponibles.
- **Mesurer** l'effet des actions des joueurs sur l'opinion, ce qui était impossible avant.
- **Évoluer en continu** : les améliorations sont livrées pendant l'exercice, à partir des retours du terrain.
- **Contrôler** les postes de commandement avec LEAC, sur la même plateforme.

---

## 11. Chiffres clés (au 13/10/2026)

| Indicateur | Valeur |
|---|---|
| Exercices dans la lignée | **4** : ORION 26, AURIGE 2BB, MINOTAURE 26 (AURIGE 7BB), DELATTRE 26 |
| Durée de l'évolution | **6 mois** (avril → octobre 2026) |
| Applications au catalogue | **11** |
| Avatars dans l'EHO de DELATTRE 26 | **environ 4 000** (4 037 au 10/10) |
| Avatars animés par IA | **105** |
| Incidents JEMM de DELATTRE 26 | **62** (2 events, 8 storylines) |
| Jours de jeu DELATTRE 26 | **15** (du 6 au 20 octobre) |
| Nuances d'émotion du dictionnaire | **36** (11 familles) |
| Machines de calcul IA branchées | **2** (PC et Mac), extensible |
| Temps d'écriture d'un message par l'IA | **environ 3 s** |

---

## 12. Glossaire

- **Avatar** : personnage fictif de l'exercice, avec une identité unique valable dans toutes les applications.
- **Avatar IA / socialement augmenté** : avatar animé automatiquement par le Moteur IA, avec une psychologie (humeur, mémoire, relations, opinions).
- **Zone** : bulle étanche qui contient tout un exercice (comptes, applications, données).
- **Instance** : une application déployée dans une zone (par exemple, un titre de presse).
- **Orchestrateur** : la partie de PLÉIADE qui crée les zones et y déploie les applications.
- **EHO** : l'annuaire des personnages de la zone ; source d'identité de toutes les applications.
- **STARTEX** : les fiches officielles (autorités) que les joueurs connaissent au début de l'exercice.
- **Inject** : un événement introduit par l'animation pour faire réagir les joueurs (publication, article, message).
- **JEMM** : l'outil de gestion des injects utilisé pour l'ensemble de l'exercice ; ses exports alimentent MELMIL.
- **MELMIL** : la planche des injects d'influence de PLÉIADE (events, storylines, incidents).
- **Event / storyline / incident** : les trois niveaux de JEMM, du thème général à l'inject précis.
- **COCKPIT** : l'application de veille et de mesure.
- **Cellules d'animation** : GREYCELL et FORAD (les animateurs).
- **Camp** : CAMP ROUGE, CAMP BLEU ou CAMP NEUTRE.
- **ILI / LI** : lutte informationnelle (influence).
- **RETEX** : retour d'expérience après un exercice.
- **Nœud de calcul** : un ordinateur qui fait tourner le modèle d'IA pour la plateforme, joint par le VPN.
- **Parc de calcul (grappe)** : l'ensemble des nœuds de calcul, avec répartition et reprise automatique.
- **Keycloak** : le service de connexion unique.
- **VPN** : le tunnel chiffré par lequel on accède au réseau fermé de PLÉIADE.

---

## 13. Plan de diaporama suggéré

**Version complète (18 diapositives)**
1. Titre : « PLÉIADE — l'espace informationnel d'entraînement du CECPC » · « Exercice · non classifié »
2. Le problème : la lutte informationnelle se joue dans un espace numérique qu'il faut reproduire à l'exercice
3. PLÉIADE en une phrase + les 4 arguments (réalisme, rapidité, isolation, reproductibilité)
4. Six mois d'évolution : frise ORION → AURIGE 2BB → MINOTAURE → fusion → serveur → DELATTRE 26 (tableau du §2)
5. D'un ZIP par mail à une plateforme unique (avant / après)
6. Le principe de la zone et des applications à la carte (schéma : une zone, des instances, une identité)
7. Le catalogue des applications (tableau du §4, avec des icônes)
8. Qui fait quoi : administration, animation, joueurs (§5)
9. MELMIL : la planche des injects reliée à JEMM
10. La Console d'animation : programmer les injects
11. ⭐ DELATTRE 26 : pourquoi des avatars IA (le besoin, §6.1)
12. ⭐ Comment pensent les avatars : le programme fait la psychologie, l'IA fait l'expression (tableau du §6.3)
13. ⭐ Exemples de messages et derniers progrès : rédacteur, dictionnaire des émotions (§6.4)
14. ⭐ Mesurer l'impact : le Reporting et l'opinion de la population (§7)
15. Sous le capot : serveur, VPN, IA locale, parc de calcul (§8)
16. Un exercice de bout en bout (§9, en 7 étapes)
17. Chiffres clés (§11)
18. Ce que PLÉIADE permet, et la suite (population plus nombreuse, lecture des images, nouvelles machines)

**Version courte (6 diapositives)** : 1 · 3 · 4 · 7 · 12 et 14 fusionnées (« faire réagir et mesurer ») · 17.

**Idées de visuels** : frise chronologique ; schéma « zone » (une bulle, des briques d'applications, une identité qui circule) ; tableau « programme / IA » en deux colonnes ; courbe d'opinion par série ; capture du réseau social façon X (avec des données fictives).

---

## 14. Précautions : ce qu'il ne faut pas mettre sur un support

- **Aucune adresse réseau**, aucun nom de machine, aucun port, aucun jeton, aucun détail de configuration du VPN ou du serveur.
- **Pas de détail sur les faiblesses de sécurité** encore en cours de correction : ne parler que des principes (§8.3).
- **Pas de données de joueurs** : utiliser uniquement des exemples fictifs (les messages d'avatars cités ici sont fictifs).
- **Nombre de dépôts de code** : dire « un dépôt par application ». Les décomptes varient selon les sources (12 à 14).
- **Ne pas présenter comme acquis** ce qui est encore en essai :
  - le rédacteur et le dictionnaire des émotions sont **en essai** sur une partie de la population, avec un groupe témoin ;
  - la **lecture des images** par les avatars est **à l'étude**.
- **Ne pas confondre** : « Mercure » est un **pays fictif** de l'univers d'exercice ; « MASTORION » est l'**ancien nom** du réseau social, aujourd'hui « social ».
- Les **noms de personnes réelles** de l'équipe ne sont pas nécessaires : parler du « développeur de la plateforme », du « CECPC », des « cellules d'animation ».
