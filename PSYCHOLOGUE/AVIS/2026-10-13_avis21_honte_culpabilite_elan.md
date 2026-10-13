# Avis n°21 — Honte, culpabilité et élan d'action dans le moteur (2026-10-13)

**Auteur** : PSYCHOLOGUE · **Demandeur** : NOYAU, pour PLEIADE (décision de l'utilisateur : consigne 3ter point 7 et règle 6 du dictionnaire)
**Sources** : `DICTIONNAIRE_EMOTIONS.json` (familles honte et culpabilité, nuances gene, humiliation, remords, mepris, inquietude, champ `elan`, règle 6) ; MEMOIRE §4bis ; avis n°5 (E5, E6), n°12, n°14 (compteurs), n°19 (règle « pas de rumeur amplifiée sans son démenti »).
**Code lu sans le modifier** : `app-ia\src\moteur\esprit.mjs` (`EMOTIONS` l. 29, `ressentir` l. 630, `decrireHumeur` l. 662, FORMAT l. 1089 et 1092) ; `emotions.mjs` (`choisirNuance`, `contexteRepere`) ; `pont.mjs` (`redigerPour` l. 530, boucle des réactions l. 690-725, démenti relayé d'office par l'élu l. 723).

---

## 0. Ce que montre le code

- La nuance est choisie **dans `redigerPour`, après la décision**, et seulement si le décideur a déjà choisi `repondre` ou `partager` avec un texte. Un élan qui doit **changer l'action** (se taire, corriger) ne peut donc pas passer par la nuance seule : il doit être une **conversion par le code**, sur un contexte connu **avant** la rédaction (insulte reçue, fait relayé puis démenti). Le précédent existe : le démenti relayé d'office par l'élu (l. 723).
- `gene`, `humiliation` et `remords` sont des nuances **« sur contexte »**. Si le décideur choisit `honte` ou `culpabilite` sans contexte repéré, `choisirNuance` ne trouve aucune nuance libre dans ces familles et tombe sur `constat`. Il faut la règle ci-dessous (§1.3).
- Un piège à éviter : l'élan qui convertit en `ignorer` doit agir **avant** l'appel au rédacteur, pour ne pas payer un appel inutile.

---

## 1. Les deux familles dans le moteur

### 1.1 Valeurs (`EMOTIONS`, format [Δ valence, Δ activation, libellé féminin])

```
honte:       [-7, -8, "honteuse"],
culpabilite: [-5,  4, "coupable"],
```

- **Honte** : plus négative que la tristesse (-6), et l'activation **baisse** : c'est une émotion de retrait (se cacher, se taire).
- **Culpabilité** : négative modérée, activation **légèrement en hausse** : c'est une émotion d'action (réparer).
- **Plancher propre** dans `ressentir` : la valence ne descend pas sous **-40** par l'effet de ces deux familles (au lieu de -60). On a honte ou des remords, on ne s'effondre pas pour un message.

### 1.2 Étiquettes de niveau (`ETIQ`, masculin)

```
honte:       ["gêné", "honteux", "humilié"],
culpabilite: ["embêté", "coupable", "rongé par le remords"],
```

### 1.3 Quand le décideur peut les choisir

Phrase à ajouter après l'énumération `"emotion"` (FORMAT des deux modes, l. 1089 et 1092) :

> `"honte"` seulement si c'est TOI qu'on moque, qu'on insulte ou qu'on prend en défaut devant les autres ; `"culpabilite"` seulement si c'est TOI qui as relayé une information fausse ou blessé quelqu'un. Jamais pour ce que font les autres, ton pays ou le gouvernement.

**Garde-fou par le code** (le décideur se trompera quand même) :
- `honte` est acceptée si le message vise l'avatar (son nom y figure ou c'est une réponse sous son message). Sinon, elle devient `degout` (la « honte pour eux » est de l'indignation ou du mépris).
- `culpabilite` est acceptée si le message vise l'avatar **ou** s'il a partagé le fait concerné dans les 72 h (`aDejaPartage`). Sinon, elle devient `tristesse`.
- Nuance quand l'émotion est acceptée sans contexte repéré par le code : honte → `gene` ; culpabilite → `remords`, seulement si l'intensité est 2 ou plus, sinon `gene`.
- **Mesure** : honte et culpabilité ensemble doivent rester sous **5 %** des réactions. Au-dessus, la phrase de l'énumération est trop lâche.

### 1.4 Effets sur les opinions et les relations

- **Opinions et croyances : aucun effet.** C'est le démenti qui agit sur la croyance, et il est déjà codé. La honte ne fait pas changer d'avis : elle fait taire.
- **Honte : aucun effet de relation supplémentaire.** Le `ressenti` (agacée, en désaccord) et les compteurs `insultes` / `attaques` de l'avis n°14 suffisent déjà. Les ajouter ferait compter l'insulte deux fois.
- **Culpabilité après un démenti (remords)** :
  - confiance envers **l'auteur du message relayé à tort** : **-10**, une seule fois par fait (« je me suis fait avoir ») ;
  - confiance envers la **source du démenti** si elle est officielle ou un média : **+3** ;
  - **prudence pendant 24 h** : la probabilité de partager un fait qui ne vient ni d'un compte officiel ni d'un média est multipliée par **0,7**.

---

## 2. L'élan d'action, nuance par nuance

| Nuance | Où il agit | Condition et probabilité | Ce qui se passe |
|---|---|---|---|
| **humiliation** (insulte qui le vise) | **conversion par le code**, avant le rédacteur | p(riposte) = **0,25** ; **+0,35** si le caractère contient fier, impulsif, sanguin, colérique ou direct, ou si `emotivite` ≥ 0,66 ; **-0,15** si pudique, discret ou réservé ; borné entre **0,10 et 0,70** ; tirage rejouable (`tirage(avatar, pub.id)`) | sinon : `ignorer`, sans J'aime |
| **remords** (fait relayé puis démenti) | **conversion par le code**, même si le décideur a ignoré | p = **0,60** ; **+0,20** si conciliant, honnête ou méticuleux, ou `agreabilite` ≥ 0,66 ; **0** si sa croyance dans le fait reste ≥ 60 (il ne croit pas le démenti), si le démenti vient d'un compte anonyme ou adverse, ou si l'avatar est un relais | **partage cité du démenti** avec un mot de correction ; une réponse si le démenti lui est adressé |
| **mepris** | **dans `redigerPour`**, juste après le choix de la nuance et avant l'appel au rédacteur | p(ignorer) = **0,40** ; **0,20** si le message lui est adressé directement, notamment par un joueur | sinon : ironie brève, **120 caractères au plus** |
| **inquietude** | **consigne au rédacteur** seulement, l'action ne change pas | une question dans **70 %** des cas (tirage rejouable), pas toujours, pour ne pas créer un tic | fin du message par une question pratique |
| **gene** | consigne au rédacteur | — | rectification brève, autodérision |

### 2.1 Humiliation
- **Émotion enregistrée** : si l'avatar se tait, `ressentir` reçoit `honte` à l'intensité 3. S'il riposte, on garde la `colere` du décideur (colère secondaire, règle 3 du dictionnaire).
- **Retrait** : s'il s'est tu, pas de publication spontanée pendant **1 h** (p = 0,7).
- **Consigne au rédacteur** pour la riposte :
  > Tu viens d'être rabaissé devant tout le monde. Réponds en UNE phrase, brève, blessée mais digne. Ne te justifie pas, n'insulte pas, ne dis pas que ça t'a touché.

### 2.2 Remords
- **Moment** : au créneau où l'avatar **lit** le démenti. Si la publication spontanée de ce créneau est libre, la correction la prend. Sinon, elle est mise en attente (`a.m.correctionsDues`) pour le créneau suivant, **au plus 6 h** après, puis abandonnée.
- **Intention** (8 mots au plus) : `corriger mon partage : c'était faux`.
- **Consigne au rédacteur** :
  > Tu avais relayé « {fait en 10 mots} ». {Source du démenti} dit que c'est faux. Dis simplement que tu t'es trompé et donne la correction, en une ou deux phrases. Pas de « mais », pas d'excuse à rallonge, pas de leçon aux autres.
- **Pas de suppression** du message d'origine : l'arbitrage de l'exercice a besoin de la trace. Cela applique la règle n°19 : le démenti circule par ceux qui avaient fait circuler la rumeur.

### 2.3 Mépris
- **Consigne au rédacteur** pour l'ironie :
  > Une seule phrase, ironie froide ; tu peux reprendre ses mots entre guillemets. Pas d'insulte, pas d'argument.

### 2.4 Inquiétude
- **Consigne au rédacteur**, dans 70 % des cas :
  > Termine par UNE question pratique et concrète (qui, quand, où, comment). Pas de question rhétorique.

---

## 3. Garde-fous

1. **Corrections** : au plus **1 par fait** et par avatar, pour toujours ; au plus **2 par jour** et par avatar. Sur la population, au plus **4 corrections par démenti et par heure**. Les autres attendent le créneau suivant, dans la limite de 6 h.
2. **Excuses** : au plus **une excuse (« désolé », « je me suis trompé ») par 24 h** et par avatar. Une deuxième correction le même jour est factuelle, sans excuse. Les formules d'excuse passent par `ticsPopulation`.
3. **Jamais d'excuse à quelqu'un qui l'a insulté.** La honte ne produit pas d'excuse, seulement le silence ou la riposte.
4. **Riposte** : au plus **1 par insulteur et par jour**. Dès la 2e insulte du même auteur dans la journée, l'avatar ignore toujours. On évite ainsi l'escalade en ping-pong entre avatars.
5. **Ignorer après une insulte ou par mépris ne touche pas la relation au-delà de ce qui existe** (ignoré en étant agacé : -2 d'affinité, avis n°5 E6). La familiarité ne baisse pas.
6. **Mépris** : le taux de conversion en `ignorer` est mesuré ; il doit rester **sous 50 %** des mépris. La règle des 15 % par nuance s'applique toujours.
7. **Honte et culpabilité ne s'accumulent pas** : plancher -40 (§1.1), l'étiquette dure 3 h au plus (fenêtre `recentes` existante), et un avatar n'est pas « humilié » plus d'une fois par jour par le même auteur (l'intensité redescend à 1 ensuite).
8. **Joueurs** : un joueur qui interpelle directement un avatar n'est ignoré par mépris qu'avec p = 0,20. Une insulte d'un joueur suit la règle de l'humiliation : le silence est réaliste, et il apprend quelque chose au joueur.

---

## 4. Mise en essai et mesures

- Même réglage que les nuances (groupe « relu » contre groupe témoin), pour pouvoir comparer.
- **Cibles** :
  - riposte aux insultes : **25 à 45 %** ;
  - correction par ceux qui avaient relayé, dans les 12 h après le démenti : **40 à 70 %** ;
  - mépris converti en silence : **30 à 50 %** ;
  - questions dans les messages « inquiétude » : **50 à 80 %** ;
  - honte et culpabilité choisies par le décideur : **moins de 5 %**.
- **Rien à attendre sur les opinions** : si elles bougent, c'est un défaut.
