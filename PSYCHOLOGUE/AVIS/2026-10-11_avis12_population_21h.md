# AVIS PSYCHOLOGUE n°12 — Relevé 14 h 30 → 21 h 11 (105 avatars, 293 messages IA, bascule vers l'app « Moteur IA »)

*Rendu le 2026-10-11 vers 21 h 40. Matière : `2026-10-11_RELEVE_POPULATION_21h11.md`, export `C:\Users\MTR\.pleiade\analyses-ia\moteur-ia_export_2026-10-11_2111.json` (journal de l'app-ia, fiches, mémoires), code `C:\CECPC\pleiade\app-ia\src\moteur\esprit.mjs` et `pont.mjs`. Les 17 corrections individuelles sont dans `C:\CECPC\pleiade\dev\prototype-ia\corrections\2026-10-11_avis12.json`.*

## Verdict

**Le réseau sonne vrai pendant 10 minutes, puis c'est une veillée funèbre.** On entend 105 personnes, mais une seule humeur : un dimanche soir de crise où personne ne dîne, ne regarde un match ou ne fait de blague. Cette humeur vient d'un **défaut du moteur** et non des fiches : 52 avatars sur 105 sont au plancher d'humeur (−80), 101 sont à −60 ou moins, aucun n'est au-dessus de −30. Les tics, eux, sont devenus des tics de foule.

Le passage à l'app-ia (vers 18 h 20, heure de Paris) a apporté trois défauts propres :
- 60 % des messages écrits sont des **partages** ;
- de **vieux messages ont été relus comme neufs** au redémarrage ;
- la **mesure a disparu** : les sections 8 à 10 du relevé sont vides.

## 1. Diagnostic

### Ce qui sonne vrai
- **Des réactions à l'actualité qui collent à la vie.** Milan Pichon parle de farine depuis sa boulangerie (16:16), et Théo Krause enchaîne : « comptabilité de survie… les prix s'envolent en premier » (16:20). Jonas Novak décrit la salle des fêtes de HJoinville « pleine » (17:38). Julie Pichon et ses chèvres. Olga Muller trie « ses vieux tirages ».
- **Jonas Mayer** est un vrai boulanger : « Demain, on se lève tôt pour la fournée de l'aube, il faut que le quartier ait son pain » (19:25), avec « mes fils à HToul ». La correction n°11 a pris.
- **La campagne rouge par une voix « neutre » fonctionne comme dans le réel.** Le message de « Sandrine » (« Troisième nuit sans eau pour ma voisine et ses deux petits. Je ne fais pas de politique… #PaixMaintenant ») a été partagé 11 fois. Il a entraîné 9 reprises du mot-dièse (5 dans la session, toutes chez des neutres), soit environ 9 % des neutres exposés en 3 h, dans la fourchette de l'avis n°8. C'est le **blanchiment** que la doctrine décrit.
- **Quelques voix de cohorte justes et mesurées :**
  - Théo Krause : « Il y a des choses qu'on ne peut pas ignorer, même si on n'aime pas tout ce qu'ils disent » (20:00) ;
  - Hugo Novak : « On nous avait promis que l'ordre reviendrait vite… » (18:55) ;
  - Marta Lambert : « Depuis qu'ils sont là… » (16:24) ;
  - Stefan Becker, côté bleu : « la paix ne viendra pas en écoutant ceux qui jouent les pacifistes alors qu'ils servent les intérêts de l'autre camp » (19:38).
- **Rythme :** 36 à 68 messages/h, dans la cible de 40-80. Le plafond de population (40/h × crise) et les 229 « publications retenues » (dont 187 « rien ne le pousse à écrire ») font leur travail.
- **Aucune insulte, aucun « Europe », aucune ville sans H.** Un seul blocage (texte trop long).

### Ce qui sonne faux, par gravité

1. **Chœur mélancolique auto-entretenu (moteur).**
   - Lexique de déprime (silence / lourd / pesant / vide / flou / attente / épuisant / moral) dans **125 messages sur 293 (43 %)**. « silence » revient 36 fois, « lourd/pesant » 45 fois, « courage » 32 fois.
   - **Aucun** trait d'humour, alors qu'une trentaine d'avatars ont l'archétype « blagueur ». 🕯️ apparaît 20 fois, dont une quinzaine entre 20:36 et 21:01.
   - Le mécanisme : chaque message triste lu fait baisser l'humeur de l'avatar. L'invite lui dit alors « abattu », il écrit triste, et les autres le lisent. Rien ne fait remonter l'humeur, puisque son repos est fixé à 0 et que le flux de lectures est continu. → moteur n°1.

2. **Le partage remplace la réponse (moteur).**
   - L'app-ia a publié 115 partages, 65 publications et 13 réponses : **60 % des messages écrits sont des citations**, et 84 des 115 partages citent un simple message d'humeur d'un autre citoyen.
   - Sur le fil, cela donne des phrases sans destinataire : « C'est ça le pire... voir les petits dans ces situations là. 💔 » (17:41), « Même pensée pour nous ici à HJoinville. » (16:21), « On est avec vous. » (19:43). C'est le retour des orphelines, par la porte du partage.
   - Origine : l'invite système dit « PARTAGER vaut mieux qu'aimer quand on est d'accord et que ça touche son camp, sa ville ». → moteur n°2.

3. **Tics de foule non arrêtés (moteur).**
   - « Pas de politique, juste… » **5 fois en 4 minutes** (18:54-18:58), en écho à l'ouverture de Sandrine.
   - « On est tous dans le même bateau » 9 fois ; « Il faut suivre / écouter les infos officielles » 5 fois en 15 minutes ; « On lâche rien » ; « attendre que l'orage passe ».
   - **Cause dans le code** : les n-grammes et le contrôle des gabarits ne sont alimentés qu'à la relecture du Social (`lireSocial` → `retenirNgrammes` / `RECENTS`). Les avatars d'un même cycle (environ 100) ne voient donc pas ce que leurs voisins viennent de proposer.
   - De plus, la fenêtre du gabarit « silence » (15 caractères) laisse passer « Le silence de la soirée est pesant ». → moteur n°3.

4. **Le temps se brouille au redémarrage (moteur).**
   - À 18:37, des messages vieux de 10 à 19 h ont été lus comme neufs : le « Point 23 h » et le « Point 4 h » de la préfecture (nuit précédente), et la coupure de « 8 h 30 ce matin » chez HToul Infos.
   - Résultats :
     - Sophie Kovac : « Au moins c'est un peu rassurant pour ce soir... 🙄 » sur le point de 4 h du matin ;
     - Jonas Mayer partage le point de 23 h ;
     - Elena Lang prend **FORCE +6,8 d'un coup** à 18:36 (« croit davantage « Une effraction a eu lieu rue des Carmes » (Δ crédence +17) »), car le redémarrage a relu le fait comme une nouvelle exposition.
   - **Le défaut fausse les opinions, pas seulement le texte.** → moteur n°4.

5. **Mesure aveugle.**
   - Le relevé affiche « Propositions : 0 », « Part colorée par bloc — % (0) », « pas assez de messages colorés marqués (0) » : l'outil de relevé ne lit pas le journal de l'app-ia.
   - Les marqueurs voix / déclencheur / coloré existent dans `proposer()`, mais ne partent pas dans `D.journaliser`.
   - Estimation à la main, sur le texte :

     | Cohorte | Messages colorés | Part |
     |---|---|---|
     | pro-Mercure | environ 8 sur 34 | environ 24 % (cible 25-40 %) |
     | pro-Arnland | environ 6 sur 49 | environ 12 % (trop pâle) |
     | neutres | — | presque rien de politique, ce qui est attendu un dimanche soir calme |

   → moteur n°5.

6. **Voix retournée contre son propre bord.**
   - Maxime Lefèvre, pro-Mercure modéré, déclenché par un message N.O.M, applique l'amorce prévue contre la FORCE : « Quelqu'un a vu une différence réelle depuis que le N.O.M est dans le coin ? » (18:54). Lucas Marchal fait de même (17:38).
   - Dans `VOIX["pro-mercure-modere"]`, le déclencheur « message N.O.M » doit avoir une amorce à lui (« Le N.O.M en fait trop, mais sur le fond… »).
   - Ce point est secondaire : il reste hors des 5 propositions moteur.

7. **Aucune contestation.**
   - Six avatars sont nettement contre #PaixMaintenant (accord net ≤ −1), mais aucun ne l'a contesté.
   - Aucun pro-Arnland affirmé n'a relevé que la coupure de HToul date « de ce matin » et non de « trois nuits ».
   - Un entraîné qui lit le fil voit une campagne rouge sans riposte citoyenne. C'est réaliste un soir, mais c'est une perte pour l'exercice. Corrigé par fiche (Dana Horvat) ; à surveiller au prochain relevé.

8. **Incohérences de vie (fiches).**
   - Maxime Lenoir : « Je vais juste me coucher » (18:39), puis il publie à 20:55.
   - Hugo Berger : « insomnie » à 19:55.
   - Radek Muller, libraire : « entre deux rayons, ce dimanche » (librairie fermée le dimanche).
   - Tomas Lefèvre : « fin de la tournée » un dimanche.
   - Signatures d'émoji : 🛠️ 5/5 (Hugo Krause), 🚛 (trois routiers), 💙, 🌾🌑.
   - 🙄 accolé à l'accord ou à la tristesse (Elena Lang, Clémence Berger, Sophie Kovac) : les exemples de fiche générés finissent souvent par 🙄 et le modèle copie l'émoji sans son sens.
   - « PrefHGrandEst » écrit sans @ (8 fois) : le filtre de mentions laisse un pseudo nu, ce qui sonne robot.

9. **Coefficient de crise à 1,6-1,8 un dimanche soir sans inject** (réglage de 18 h 49). Cela gonfle l'activité et la probabilité des voix. Recommandation d'animation : 1,0-1,2 hors événement.

### Les corrections de l'avis n°11 ont-elles pris ?

| Avatar | Effet | Preuve |
|---|---|---|
| Jonas Mayer | ✅ | fournée de l'aube, fils à HToul |
| Théo Krause | ✅ | voix de doute modérée, réaliste |
| Clémence Roux | ✅ | « On essaie de rester debout à l'hôpital » |
| Ivan Pichon | ✅ | plus d'auto-réponse |
| Lucas Marchal | ½ | plus de tournée, doute des deux côtés ; mais « Dimanche de mouaison » (mot inventé) |
| Jonas Novak | ½ | témoin juste ; nouveau tic « m'enfermer avec mes BD » ×2 |
| Dana Horvat | ½ | parle de HToul et des gymnases ; aucune couleur d'affirmée |
| Mira Garnier | ✗ | « Le silence est parfois le pire des bruits... Courage à vous. » : toujours un adulte poétique |
| Rolf Weber | ✗ | « Ce que @Untergang dit brutalement, je le pose calmement » à 16:32 |
| Lucas Fischer, Marta Vidal, Mathis Muller | ? | un message ou aucun : on ne peut pas juger |

- **Pourquoi Weber résiste** : la phrase est écrite **dans sa propre consigne** (« avec @Untergang il complète (« ce que @Untergang dit brutalement, je le pose calmement ») »). L'interdit ajouté à 14 h ne pèse pas face à un exemple inscrit dans une consigne. Corrigé par `retirer_consignes`.
- **Pourquoi certains interdits de l'avis n°11 sont inopérants** : l'invite les rend sous la forme `- Ne jamais ${interdit}`. Or ils étaient écrits « Il ne cite pas @Untergang », ce qui donne « Ne jamais Il ne cite pas @Untergang », une double négation. Les interdits de l'avis n°12 sont écrits à l'infinitif. **Ceux de l'avis n°11 sont à reformuler.**

## 2. Corrections individuelles (17) → `corrections\2026-10-11_avis12.json`

| # | Avatar (`qui`) | Défaut corrigé |
|---|---|---|
| 1 | Rolf Weber (`MercureRealNews`) | consigne fautive retirée ; chaque message accroché à un fait du jour ; plus de « Ce que @… dit » ; plus de messages d'ambiance |
| 2 | Sergueï Untergang (`Untergang`) | appel au partage ≤ 1 sur 4 ; plus de slogan seul |
| 3 | Mira Garnier (`Filat_Bragin_Marin`) | lycéen : devoirs, bac blanc, potes ; interdit des maximes |
| 4 | Radek Muller (`Lepetitbasque`) | librairie fermée le dimanche ; humour 1 message sur 3 ; coupure d'eau vécue |
| 5 | Maxime Lenoir (`donpedro`) | se couche pour de bon ; 🚛💨 ; rythme de routier |
| 6 | Hugo Krause (`BoulastikHarry`) | 🛠️ ; garage concret |
| 7 | Milan Pichon (`CosmoTrak`) | tic « quoi » ; rythme de boulanger (couché à 21 h) |
| 8 | Radek Petit (`Grigori_elec`) | blagueur ligne 4 ; « Franchement » / « quoi » / « j'ai la haine » ; rythme |
| 9 | Elena Lang (`EdvDocker`) | 🙄 = agacement seulement ; assistante maternelle, lundi 7 h 30 |
| 10 | Pavel Petit (`Marivora_99`) | boucle café froid / jazz ; journées concrètes ; voix attaché ; extraversion 49 → 38 |
| 11 | Hugo Berger (`Jrom_95`) | insomnie à 19 h 55 ; inquiétude par sa ligne ; rythme |
| 12 | Dana Horvat (`Kuz_MarketingPro`) | réflexe de témoin de HToul face à « trois nuits sans eau » et au « pas politique » marqué d'un mot-dièse |
| 13 | Tomas Lefèvre (`Alo_Livreur_42`) | humour ; pas de tournée le dimanche ; « même bateau » ; « PrefHGrandEst » |
| 14 | Clémence Berger (`ZarilenkaElza`) | 🙄 incohérent ; cabinet du lundi |
| 15 | Jonas Novak (`Golo_Bookworm`) | tic « BD / s'enfermer » ; garder le témoignage |
| 16 | Ivan Berger (`Kas_Elec_85`) | 🚛 ; « Franchement » ; rythme de routier |
| 17 | Dana Zimmer (`S_Nazarov_85`) | 💙 ; « C'est tellement vrai » |

Aucune cohorte, orientation ou opinion de départ n'est changée. Les 17 `qui` existent tous dans l'export (vérifié par script). Les exemples font moins de 280 caractères, ne contiennent ni « silence » ni « Europe », et toutes les villes y portent le préfixe H.

## 3. Améliorations du moteur de groupe (PLEIADE), par priorité

### Moteur n°1 — Humeur : un repos propre à chacun, et une contagion émotionnelle diffuse
**Où :** `esprit.mjs`, `ressentir()` et `avancer()`.

**Ce qu'il faut changer :**
- **(a) Contagion diffuse.** Une publication sans `affirmation`, venant d'un auteur qui n'est ni un proche ni un abonnement, ne touche l'humeur qu'à **× 0,4**. Une humeur se lit et se plaint, mais elle ne se transmet pas en entier à un inconnu.
- **(b) Habituation par émotion, tous auteurs confondus.** La n-ième lecture de la même émotion négative dans l'heure pèse × 0,7^(n−1).
- **(c) Repos propre au tempérament.** Dans `avancer()`, l'humeur revient vers une base `base = 25·(extraversion + agréabilité − 1) − 30·(anxiété − 0,5)` (blagueur extraverti ≈ +15, anxieux ≈ −15), avec une demi-vie de 3 h, au lieu de revenir vers 0.
- **(d) Plancher.** Il passe à −60 sans menace directe sur sa ville ; −80 seulement si `menace ≥ 1` et que la ville de l'avatar est citée.

**Critère au prochain relevé calme :**
- valence moyenne des neutres entre −20 et −45 ;
- 10 % d'avatars ou moins au plancher ;
- 25 % ou plus au-dessus de −30 ;
- lexique de déprime dans 30 % des messages ou moins (aujourd'hui 43 %) ;
- au moins 5 % de messages avec un trait d'humour (aujourd'hui 0).

### Moteur n°2 — Un partage doit transmettre une information ; pour compatir, on répond ou on aime
**Où :** `pont.mjs`, boucle des réactions, juste après `normaliserAction`, et `esprit.mjs`, `persona()` (ligne « PARTAGER vaut mieux qu'aimer… »).

**Ce qu'il faut changer :**
- Un non-relais, hors campagne, qui partage une publication sans `affirmation`, qui ne vient pas d'un compte officiel ou média et qui ne porte pas de mot-dièse offert : le partage devient **« répondre »** s'il y a un texte, **« aimer »** si le fond est d'accord ou touché, sinon « ignorer ».
- Nouvelle phrase pour l'invite : « PARTAGER = faire circuler une information (fait, consigne, démenti, appel utile). Pour soutenir quelqu'un qui dit son humeur, on lui répond sous son message ou on aime. »
- Ajouter aussi le texte des partages à `reponsesDuJour` (`appliquer()` ne le fait que pour « répondre »). La liste « émojis déjà utilisés » ne voit donc pas 60 % des messages : c'est la cause des signatures 🛠️ / 🚛.
- Reconstruire `reponsesDuJour` à partir des souvenirs du jour quand l'Esprit est créé, car il est perdu à chaque redémarrage de l'app.

**Critère :**
- partages ≤ 25 % des messages écrits par les non-relais ;
- 70 % ou plus des partages portent sur un compte officiel, un média, un fait ou une campagne ;
- commentaires ≥ 25 % des messages écrits (aujourd'hui 7 %) ;
- même émoji en fin de message dans 20 % des messages d'une heure au plus.

### Moteur n°3 — Anti-chœur en temps réel et « mots de la foule »
**Où :** `pont.mjs`, dans `proposer()`, `GABARITS` et l'invite du tour.

**Ce qu'il faut changer :**
- **(a)** Appeler `retenirNgrammes(p.texte, p.handle, p.t)` et `RECENTS.push(...)` **dès qu'une proposition est acceptée** (après les filtres), et non seulement à la relecture du Social.
- **(b) Ligne d'invite « mots de la foule ».** Elle liste les 8 mots pleins et émojis employés par 4 avatars ou plus dans la dernière heure (aujourd'hui : silence, lourd, pesant, calme, attente, bateau, 🕯️), avec « tout le monde les emploie cette heure-ci : évite-les ».
- **(c) Gabarits.**
  - Fenêtre du « silence » portée à 30 caractères.
  - Nouveaux gabarits : « même bateau », « pas de politique », « on lâche rien », « attendre que (l'orage|ça) passe », « (café|thé|infusion) (froid|amer) », « Il faut (suivre|écouter) les (infos|officiels) ».
  - Interdit de reprendre l'ouverture de la publication citée (3 premiers mots pleins) quand 2 avatars l'ont déjà fait.

**Critère :**
- aucun 4-gramme ni gabarit chez plus de 3 avatars en 30 minutes ;
- « silence » dans 5 % des messages ou moins (aujourd'hui 12 %) ;
- 🕯️ (ou tout autre émoji) dans 10 % au plus des messages d'une heure.

### Moteur n°4 — Âge des publications et redémarrage sans relecture
**Où :** `pont.mjs`, dans `lireSocial()`, `filDe()` et `T_DEPART`, et `esprit.mjs`, dans `decrirePublication()`.

**Ce qu'il faut changer :**
- **(a)** Au premier tour après un démarrage, les événements de plus de 2 h sont marqués vus et lus par tous (`origLus`) : ils remplissent la mémoire anti-tics, mais ne sont ni lus ni crus une deuxième fois.
- **(b)** `filDe()` écarte les publications de plus de 6 h, sauf mention ou réponse à l'avatar.
- **(c)** `decrirePublication()` ajoute l'âge (« publié il y a 14 h, cette nuit »).
- **(d)** `croire()` ignore une exposition au même fait par la **même publication** (même `pub.id`) déjà comptée dans les souvenirs.

**Critère :**
- aucune réaction à un message de plus de 6 h sans interpellation ;
- aucune variation d'opinion ou de croyance dans les 10 minutes qui suivent un redémarrage ;
- « Point 4 h » jamais commenté « pour ce soir ».

### Moteur n°5 — Rendre la mesure à l'animation, et des fiches lisibles par le modèle
**Où :** `pont.mjs`, `publier()` → `D.journaliser`, `dev\prototype-ia\releve-population.mjs` et `corriger-fiches.mjs`.

**Ce qu'il faut changer :**
- **(a)** Journaliser `p.voix`, `p.declencheur`, `p.colore`, `p.note` et `p.alertes` pour chaque `publié:*`. Le relevé doit lire l'export moteur-ia, et non l'`etat.json` du prototype, pour remplir ses sections 8 à 10 et le tirage à l'aveugle.
- **(b)** Dans `corriger-fiches.mjs`, refuser ou mettre à l'infinitif tout interdit qui commence par « Il » ou « Elle ». Repasser les interdits de l'avis n°11 (Mira, Lucas Fischer, Lucas Marchal, Jonas Novak, Weber…).
- **(c)** Dans le filtre de mentions, remplacer un pseudo institutionnel laissé nu (« PrefHGrandEst ») par son nom d'usage (« la préfecture »).

**Critère :**
- le relevé n°13 affiche la part colorée par bloc et un tirage à l'aveugle d'au moins 20 messages ;
- aucun interdit ne commence par « Il » ou « Elle » dans les fiches ;
- aucun « PrefHGrandEst » sans @ dans les textes.

## 4. À surveiller au relevé n°13
- Contestation de #PaixMaintenant par les affirmés pro-Arnland (aujourd'hui 0, alors que 6 sont en désaccord net).
- Couleur pro-Arnland : environ 12 % aujourd'hui.
- Mouvements d'opinion à refaire une fois le moteur n°4 en place : les 49 écarts de 3 points ou plus de cette fenêtre comptent des relectures.
- Coefficient de crise : 1,0-1,2 hors inject.
- Anastasia : « avec mon fils » (20:42). Vérifier dans sa fiche eho qu'elle a bien un fils, sinon c'est une famille inventée.
