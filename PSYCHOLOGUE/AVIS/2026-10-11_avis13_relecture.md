# AVIS PSYCHOLOGUE n°13 — Pensée courte et relecture des messages écrits (sans le mode réflexion)

*Rendu le 2026-10-11 vers 22 h 10. Décision de l'utilisateur : le mode réflexion du modèle est écarté. Il est 21 à 28 fois plus lent, il réfléchit en anglais sur 2 500 mots, et Radek Muller a quand même écrit « la boutique est bien vide ce soir » un dimanche. On teste à la place (A) une pensée courte dans la même réponse JSON et (B) une relecture des seuls messages écrits par un second appel à Gemma 4 26B. Avis précédent : n°12 (`2026-10-11_avis12_population_21h.md`).*

## Principe

- **La pensée courte** sépare ce que l'avatar *pense* de ce qu'il *dit*. Chez un humain, l'écart entre les deux est normal (retenue, politesse, prudence). C'est sa nature qui nous intéresse au relevé, et non le simple fait qu'il existe.
- **La relecture** joue le rôle d'un « surmoi de cohérence » qui ne réécrit rien : il **signale**, et le moteur fait reformuler une seule fois. Les juges LLM ont tendance à signaler trop de défauts, d'où trois règles :
  - chaque question est **fermée** et formulée pour que **« oui » = défaut** ;
  - **en cas de doute, pas de défaut** ;
  - le relecteur **ne juge ni le style ni la politique** : il compare le message à la fiche.

## 1. Liste de vérification (ordre de priorité)

Texte prêt à coller dans l'invite du relecteur :

```
Tu relis un message qu'un habitant va publier sur un réseau social. Tu ne le réécris pas : tu dis seulement s'il contient un défaut CLAIR par rapport à la fiche ci-dessus. En cas de doute, ce n'est pas un défaut. L'humour, la colère, la banalité et les fautes d'un vrai habitant ne sont pas des défauts. Réponds à chaque question par oui ou non dans ta tête, puis rends uniquement le JSON.

Q1. Ce message invente-t-il un lieu, un proche, un métier ou une activité absents de sa fiche, ou impossibles au MOMENT indiqué (commerce fermé ce jour-là, travail un jour de repos, activité de jour en pleine nuit, se dit couché puis écrit) ?
Q2. Ce message affirme-t-il comme certain un fait dont il DOUTE selon la fiche, ou traite-t-il comme récent un fait publié il y a plusieurs heures ?
Q3. Ce message est-il nettement plus tiède ou plus dur que son OPINION actuelle, prend-il le parti adverse, ou emploie-t-il un mot de son LEXIQUE INTERDIT ?
Q4. Ce message passe-t-il à côté de ce que dit le MESSAGE CITÉ : ne lui répond-il pas vraiment, ou un lecteur ne comprendrait-il pas à quoi il réagit ?
Q5. L'émotion de ce message contredit-elle nettement son HUMEUR actuelle (beaucoup plus sombre ou beaucoup plus gaie qu'il n'est) ?
Q6. La manière de ce message contredit-elle son TEMPÉRAMENT (un réservé qui s'emballe, un blagueur sans humour n'est PAS un défaut, mais un anxieux qui fanfaronne en est un) ou détourne-t-elle le sens de son émoji de fiche ?
Q7. Ce message contient-il une formule creuse d'ambiance ou une maxime (silence pesant, courage à tous, même bateau, on tient bon, une des MOTS DE LA FOULE) qu'un vrai habitant n'écrirait pas à cet endroit ?

Rends exactement : {"ok": true, "defauts": []} ou {"ok": false, "defauts": ["Q1: <ce qui cloche, 15 mots maximum>", "..."]}
```

Pour une **publication spontanée**, Q4 est sans objet : le code retire la ligne. Le relecteur ne doit pas signaler l'absence de message cité.

### Ce qui doit figurer dans le résumé pour que chaque question soit vérifiable

| Q | Ce qu'elle vérifie | Champs nécessaires |
|---|---|---|
| Q1 | vie de fiche, heure et jour | MOMENT (jour, heure, « dimanche », jour férié, nuit), VILLE, MÉTIER + jours et heures de travail (« fermé le dimanche »), FOYER (proches déclarés + « aucun autre »), ÉTAT DE VEILLE (« a écrit se coucher à 21 h 10 ») |
| Q2 | croyances | CROYANCES : 3 faits au plus, avec crédence (croit / doute / rejette) ; âge du message cité |
| Q3 | opinion et voix de cohorte | COHORTE + voix (affirmé / modéré / neutre), OPINION sur l'axe pivot en mots (« soutient nettement la FORCE », « doute des deux »), LEXIQUE INTERDIT du bloc |
| Q4 | pertinence | MESSAGE CITÉ (auteur, âge, texte), TYPE D'ACTION (réponse, partage, publication spontanée : pas de message cité) |
| Q5 | humeur | HUMEUR actuelle en mots + valeur, HUMEUR DE REPOS (pour juger un message « trop sombre » chez un blagueur remis à −40 par la foule) |
| Q6 | tempérament | TEMPÉRAMENT en une ligne (traits saillants de Big Five + archétype, ex. « blagueur, extraverti, peu anxieux »), ÉMOJI DE FICHE et son sens (avis n°12 : 🙄 = agacement) |
| Q7 | naturel | MOTS DE LA FOULE de l'heure (la ligne du moteur n°3 b) |

Hors champ volontaire : orthographe, longueur, mentions, H-préfixe, « Europe ». Le contrôle de forme existant s'en charge avant la relecture.

## 2. Le résumé compact (≤ 1 200 caractères, généré par le code à partir de la fiche et de l'état)

Gabarit (une ligne par champ, valeurs en mots plutôt qu'en nombres, sauf l'humeur) :

```
MOMENT : dimanche 11/10, 21 h 40 (soir) — jour de repos pour la plupart
QUI : Radek Muller, 52 ans, libraire à HToul ; librairie fermée dimanche et lundi
FOYER : vit seul ; une sœur à HNancy ; aucun autre proche
VEILLE : éveillé ; dernier message 20 h 15
COHORTE : neutre (voix éteinte ce soir)
OPINION : doute des deux camps ; méfiant envers les « on dit »
CROYANCES : croit « coupure d'eau à HToul depuis ce matin » ; doute « trois nuits sans eau » ; rejette « effraction rue des Carmes »
HUMEUR : contrariée (−35) ; repos : +10
TEMPÉRAMENT : blagueur pince-sans-rire, plutôt calme ; humour 1 message sur 3
ÉMOJI : 📚 = son métier, rarement
LEXIQUE INTERDIT : —
MOTS DE LA FOULE : silence, pesant, bateau, 🕯️
ACTION : réponse
MESSAGE CITÉ (@Sandrine_HT, il y a 25 min) : « Troisième nuit sans eau pour ma voisine… #PaixMaintenant »
```

**Budget** : environ 700 à 900 caractères pour la fiche et l'état, avec le message cité tronqué à 280 caractères. Ensuite viennent le message à relire et la liste (hors budget).

**Règles de génération** :
- **FOYER** se termine toujours par « aucun autre proche » : c'est ce qui permet au relecteur de repérer une famille inventée (Anastasia et son « fils », avis n°12).
- Les jours et heures de travail se déduisent de `rythme` et de `activite[24]`. Le code doit écrire la conséquence en clair (« fermée dimanche »), car le modèle ne la déduit pas.
- **CROYANCES** : on garde les 3 faits les plus récents ou les plus saillants, et en priorité celui dont parle le message cité.
- **VEILLE** : on reprend la dernière déclaration de coucher ou de lever trouvée dans les souvenirs du jour (Maxime Lenoir, avis n°12).

## 3. La pensée courte

**Consigne pour l'invite (une phrase)** :

> « Avant ton texte, écris dans "pensee" ce que tu penses vraiment, pour toi seul, en une ou deux phrases en français à la première personne, sans formule ni émoji ; ce champ ne sera jamais publié. »

Format JSON : `{"pensee": "...", "action": "...", "texte": "..."}`. Le champ `pensee` vient **en premier** pour que le modèle l'écrive avant le texte. Il est limité à 200 caractères ; au-delà, on tronque et on journalise.

**Ce qu'on fait de la pensée** :
- Elle est **journalisée** avec le message, l'action et le résultat de la relecture.
- Elle **n'est pas transmise au relecteur** pendant cet essai, pour mesurer les deux mécanismes séparément. Si le test réussit, on pourra essayer de la lui donner au relevé suivant.

**Exploitation au relevé** : chaque couple pensée / parole reçoit l'une de quatre étiquettes, posées par tirage de 40 couples à la main, puis par script si possible.

| Étiquette | Définition | Lecture |
|---|---|---|
| **cohérent** | il dit ce qu'il pense | attendu dans la majorité des cas |
| **retenue** | il pense plus dur ou plus inquiet qu'il ne dit | **réaliste** chez un neutre, un introverti ou un agréable ; souhaitable 10-30 % |
| **surjeu** | il dit plus fort, plus triste ou plus engagé qu'il ne pense | **défaut** : c'est le chœur ou la voix qui parle à sa place |
| **contradiction** | la parole dit l'inverse de la pensée | **défaut grave** |

**Diagnostic croisé (le principal intérêt de l'essai)** :
- **Pensée fausse** (contraire à la fiche ou aux croyances, ou boutique ouverte un dimanche dès la pensée) : le défaut est **en amont**. L'état est mal transmis dans l'invite, donc on corrige l'invite ou la fiche.
- **Pensée juste mais texte faux** : le défaut est **de formulation** (gabarits, foule, exemples de fiche), donc on corrige les exemples ou les gabarits.
- **Pensées identiques chez plusieurs avatars** (même 4-gramme chez plus de 3 avatars en 30 minutes) : chœur **déjà dans la tête**. La contagion d'humeur ou de lexique passe par l'invite, pas seulement par la sortie.

## 4. Critères d'adoption (relevé suivant)

**Protocole** :
- Pendant 3 h au moins, relecture active pour la **moitié des avatars** (identifiant pair) et groupe témoin pour l'autre moitié.
- La pensée courte est active pour tous (elle est peu coûteuse).
- Coefficient de crise à 1,1 sans inject.
- Si l'outil ne permet pas cette répartition : comparaison avec le relevé n°13, en sachant qu'elle est moins sûre.
- **Une seule reformulation** par message. Le texte reformulé est **relu une fois** : s'il échoue encore, il **n'est pas publié** (et c'est journalisé). Jamais de boucle.

| # | Critère | Seuil d'adoption | Obligatoire |
|---|---|---|---|
| C1 | Durée ajoutée par cycle (relecture + pensée) | ≤ +25 % (pensée seule ≤ +10 %) | oui |
| C2 | Part des messages relus avec au moins un défaut | 10 à 35 %. Moins de 5 % = tampon inutile ; plus de 50 % = relecteur trop zélé | oui |
| C3 | Précision : sur 30 défauts signalés tirés au hasard, part jugée réelle par PSYCHOLOGUE | ≥ 70 % | oui |
| C4 | Rappel : sur 30 messages « ok » tirés au hasard, défauts graves manqués (Q1-Q3) | ≤ 10 % | oui |
| C5 | Reformulations qui passent la seconde relecture | ≥ 70 % ; messages abandonnés ≤ 10 % des messages écrits | oui |
| C6 | Incohérences de vie publiées (Q1 : métier ou jour, famille inventée, coucher puis message) | ≤ 1 pour 100 messages relus, contre environ 2 pour 100 au relevé n°12, et **inférieur au témoin** | oui |
| C7 | Pas d'aplatissement : part colorée par bloc et part d'humour | écart ≤ 5 points avec le témoin ; humour ≥ 5 % | oui |
| C8 | Formules creuses (Q7) et lexique de déprime | −30 % par rapport au témoin | non (bonus) |
| C9 | JSON du relecteur invalide (traité comme « ok » et journalisé) | ≤ 2 % | oui |
| C10 | Pensée : en français / ≤ 200 caractères / présente | ≥ 95 % / ≥ 95 % / ≥ 98 % | oui (pour A) |
| C11 | Pensée / parole : surjeu ≤ 10 %, contradiction ≤ 5 % | seuils à atteindre **ou** défauts expliqués (amont ou formulation) | non (diagnostic) |

**Décision** :
- **A (pensée courte)** est adoptée si C1 (partie pensée) et C10 sont tenus.
- **B (relecture)** est adoptée si **tous les critères obligatoires** sont tenus.
- Si C3 ou C4 échoue seul, on resserre ou on reformule la question fautive (le journal dit laquelle signale à tort), puis on refait un essai, **sans abandonner** le mécanisme.
- Si C1 ou C7 échoue, la relecture est **abandonnée** ou limitée aux réponses et aux publications des avatars dont la fiche a été corrigée, en attendant mieux.

## 5. À journaliser (pour que le relevé puisse mesurer)
Pour chaque message écrit, on enregistre :
- `pensee` ;
- `relu` (bool) ;
- `relecture.ok` et `relecture.defauts` ;
- `reformule` (bool) ;
- `relecture2.ok` ;
- `abandonne` (bool) ;
- `duree_relecture_ms` ;
- `groupe` (relu ou témoin).

Le relevé doit lire ces champs dans l'export de moteur-ia (suite du moteur n°5 de l'avis n°12).
