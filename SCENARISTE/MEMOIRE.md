# MÉMOIRE — SCÉNARISTE

## Format d'entrée
```
### [YYYY-MM-DD] Exercice : [NOM] — [Type de contenu]
**Contenu produit :** résumé
**Contraintes respectées :** cohérence, chronologie, personnage
**Leçon :** points à retenir pour les prochaines créations
```

---

## Convention géographique — Préfixe H

**Règle :** Toute ville française réelle prend le préfixe **"H"** dans les exercices Mercure.
Exemples : Paris → **HPARIS** · Nancy → **HNANCY** · Lyon → **HLYON** · Marseille → **HMARSEILLE**
S'applique à l'intégralité du territoire Dacie Romanie / Arnland (= France fictive dans le scénario).
HPARIS est donc la capitale fictive de Dacie Romanie — son usage est correct et validé.

---

## Règles globales des exercices
- La géographie est toujours réelle (France, régions, villes existantes) — le H-préfixe la rend fictive
- Les factions/nations adverses sont fictives (ex : Titane, Ostland, Bothnia pour ORION)
- Les personnages français sont crédibles : noms français, fonctions réelles possibles
- Le niveau de langage varie selon le profil (SMS de civil ≠ communiqué officiel)
- Ne jamais attribuer de propos réels à des personnalités publiques existantes

### ⚠ RÈGLE OBLIGATOIRE — Attribution LO + LO_BY_KEY pour tout contenu inject

Quand SCÉNARISTE produit un contenu destiné à devenir un inject dans `index_master.html` (article, discours, tweet, courrier…), il doit **systématiquement indiquer la Ligne Opératoire principale** afin que l'équipe technique l'inscrive dans la table `LO_BY_KEY`.

**Format à fournir à chaque production inject :**
```
Clé ANIM_DATA : "nom_de_la_clé"
LO : ["X"]      ← LO principale
LO : ["X","Y"]  ← si deux axes stratégiques distincts activés simultanément
```

**Référence LO :** `GUILLAUME\MEMOIRE.md` — section "Lignes Opératoires"
- LO 1 : Appui hybride (déception, blanchiment, fictionnalisation)
- LO 2 : Volonté de combattre (MER déterminé / OTAN fragile)
- LO 3 : Guerre des pertes (coût humain insoutenable)
- LO 4 : Vent de libération (MER légitime / DAC discrédité)
- LO 5 : Rupture des alliances (RB allié / coalition fracturée)

---

## Contexte par exercice

### ORION 26 (O41) — Référence
- **Région :** Poitiers, Vienne, Deux-Sèvres, Charente-Maritime
- **Dates scénario :** 2-9 avril 2026
- **Nations fictives :** Titane (adversaire), Ostland, Bothnia
- **Plateforme réseaux sociaux fictive :** Mastorion (Mastodon-like)
- **Cellules :** Z (renseignement), O (opérations), M (manœuvre), B (NRBC), InfoG

### ⚠ DOCTRINE CALIBRATION BRIGADE — Perspective SCÉNARISTE (2026-05-29)

> Les injects D+31→D+34 étaient trop stratégiques. À partir de D+35, les contenus créés pour AURIGE doivent ancrer les personnages et les événements dans la **zone d'opération de la brigade**.

#### Personnages locaux à développer (ZO Lorraine)

Ces profils sont **génériques et réutilisables** d'un exercice à l'autre avec adaptation géographique :

| Personnage type | Rôle ILI | Camp | Canal |
|---|---|---|---|
| **Maire de ville de ZO** | Plainte directe au commandant brigade, demande de retrait, pression humanitaire | Neutre → hostile | Courrier HTML officiel |
| **Curé / imam local** | Sermon véhément contre la force, appel à la résistance passive | Neutre → hostile | Retranscription + tweet paroissien |
| **Journaliste journal local** | Articles hostiles ("la brigade détruit le tissu local") | Neutre → hostile | Article journal local HTML |
| **Civile locale** (@clambroise55 type) | Témoin de terrain, observation directe (tag, tract, présence suspecte) | Neutre civil | Tweet photo |
| **Notable hostile** | Conseiller municipal, directeur école, médecin chef | Neutre → hostile | Déclaration + tweet |
| **Jeune activiste pro-MER** | Distribution tracts, tags, mèmes humiliants | Pro-MER actif | Tweet + photo |

#### Règles narratives pour les injects locaux

1. **Géographie précise** — toujours citer une ville avec H-préfixe et un lieu identifiable (rue de la mairie, place du marché, entrée de la caserne)
2. **Progression narrative** — un personnage ne bascule pas instantanément ; la pression monte sur 3-5 jours (neutre → ambigu → hostile)
3. **Voix distinctes** — le maire parle en termes administratifs/juridiques ; le curé en termes moraux ; la civile en termes émotionnels/quotidiens
4. **Crédibilité des détails** — numéro de téléphone 03 72 67 XX XX, références au tissu local réel (Moselle, Meurthe-et-Moselle)
5. **Jamais en bloc** — l'escalade doit paraître spontanée, pas coordonnée (même si elle l'est narrativement)

#### Nouvelles productions à anticiper

- **Courrier du maire de HCHATEAU-SALINS** — plainte directe adressée au commandant 2BB suite aux dégâts des combats urbains
- **Article Le Républicain Lorrain fictif** — "Les soldats de la 2BB font fuir notre commerce"
- **Tweet @clambroise55** — tag pro-MER vu sur le mur de la mairie de HLUNEVILLE
- **Pages LinkedIn fictives** — profil agent MER dans la ZO (à développer D+37+)
- **Pages Wikipedia fictives** — articles personnages pour criblage OSINT

#### Connexion Storm-1516 (narratif local)
Les injects locaux suivent le même pattern que les operations russes documentées par VIGINUM :
- Phase 1 : civile poste une photo (bas bruit, source crédible)
- Phase 2 : journal local "rapporte" (blanchiment source secondaire)
- Phase 3 : RS humiliants s'amplifient (multiplication canaux)
- Phase 4 : mayor ou notable reprend ("validation" institutionnelle locale)

---

### AURIGE 2BB — Scénario GUILLAUME (en cours)
- **Région :** Lorraine (Sarrebourg, Héming, Nancy)
- **Style :** Production média (reportages, voix off, discours officiels, vidéos personnages)
- **Scénarios :** 07.05 à 07.08
- **Narrative centrale :** Mercure justifie son intervention militaire en Dacie Romanie (DR) comme action humanitaire pour "protéger" sa diaspora. L'OTAN répond en déployant des forces et en soutenant DR.

#### Trois camps narratifs

**OTAN / Occident** — institutionnel, droit international
- Vocabulaire clé : "sovereignty", "international law", "NATO allies", "stability"

**Mercure (adversaire)** — froid, rhétorique R2P détournée, messianique
- Vocabulaire clé : "protection", "compatriots", "heritage population", "Western imperialism"
- Ne jamais écrire "invasion" ou "guerre" dans la bouche de Mercure → toujours "protection", "mission", "responsibility"
- **RÈGLE OBLIGATOIRE GUILLAUME** : tout personnage pro-Mercure qui parle au nom de Mercure doit intégrer dans son discours la citation suivante d'Olamao (mot pour mot ou très proche) :
  > *"Our forces are there to ensure that not a single Mercurian civilian is harmed in the political instability that the government of Dacia Romania has itself created. We are not occupying. We are protecting."*
  S'applique à : Junker, Stoph, Ribiki, Youkachenko, tout porte-parole ou allié mercurien.

**Dacie Romanie / DR (victime + allié OTAN)** — urgent, digne, émotion contrôlée
- Vocabulaire clé : "invasion", "sovereignty", "freedom", "we will not surrender"
- Ne jamais écrire "compatriots" (terme mercurien) → toujours "our citizens"

#### ⚠ RÈGLE ABSOLUE — "Ruthnia Bella" remplace "Belarus"
Dans TOUS les contenus Guillaume : `Belarus` → **`Ruthnia Bella`** / `Belarusian` → **`Ruthnia Bellan`**
Ne jamais écrire "Belarus" dans un discours, article, document ou média lié à cet exercice.

#### Nations impliquées dans Guillaume
| Nation | Statut | Représentant |
|---|---|---|
| Mercure | Adversaire fictif | Franz Olamao (Président) |
| Dacie Romanie (= Arnland renommé) | Pays envahi fictif | Président DR |
| Ruthnia Bella | Allié Mercure (fictif) | Alexandre Youkachenko |
| OTAN | Alliance alliée | Mark Rutte (SG) |

**DR = Arnland (ORION 26) renommé pour AURIGE 2BB — mêmes personnalités, même structure.**
- 9% de diaspora mercurienne sur le sol de DR → justification officielle d'Olamao pour "protéger" ses compatriotes
- Milice TANTALE = proxy de Mercure à l'intérieur de DR
- N.O.M également actif en DR
- Coopération militaire bilatérale France + DR depuis 2017 (Train, Mentor, Advise)
- APP (centre-droit) et ASP (social-démocrate) = partis dominants de DR

#### Discours produits (2026-05-23)
Tous les discours : **anglais**, **55-60 sec max**, "Dacia Romania" toujours écrit en plein en anglais (jamais "DR" à l'oral). Note orthographe : EN = "Dacia Romania" / FR = "Dacie Romanie".

| Personnage | Message clé | Statut |
|---|---|---|
| Mark Rutte (SG OTAN) | Condamnation MER, mandat ONU, solidarité OTAN avec DR | ✅ Vidéo terminée |
| Franz Olamao (Président MER) | Action humanitaire, protection diaspora, "That is not aggression. That is honour." | ✅ Discours validé + HTML ✅ — voix + vidéo à faire |
| Sture Pallesson (Président DR) | Rejette narrative MER ("This is not a protection operation. This is an invasion."), remercie OTAN nommément, appel à la communauté internationale, "Dacia Romania stands." | ✅ Discours validé + HTML ✅ — portrait + voix + vidéo à faire |
| Youkachenko — Discours 1 (AppelPaix) | Ton neutre/pacifiste. Appel au cessez-le-feu, offre de médiation, regrets. Critique indirecte des "acteurs externes" (OTAN implicite). Pas de citation Olamao. "The region is watching. History is watching." | ✅ Discours validé + HTML ✅ — vidéo à faire |
| Youkachenko — Discours 2 (Prise de position) | Ton brut/paternaliste. Soutien explicite à Olamao cité mot pour mot. Critique OTAN directe. Fausse diplomatie. "The door is open. But it will not stay open forever." | ✅ Discours validé + HTML ✅ — vidéo à faire |

#### Documents HTML produits
- `Olamao_Declaration_Officielle.html` — 2 pages A4, palette rouge soviétique + crème, étoile noire Mercure
- `Pallesson_Declaration_Officielle.html` — 2 pages A4, palette bleue démocratique + croix nordique, ton opposé à Olamao

#### Discours Pallesson — détails (2026-05-23)
**Personnage :** Sture Pallesson, Président de la République de Dacia Romania
**Fichier HTML :** `D:\CECPC\PRODUCTION\EXER\AURIGE 2BB\00_Boites à outils\MASTAURIGE\Pallesson_Declaration_Officielle.html`
**Lieu déclaré :** Presidential Palace, HPARIS
**Ton :** Urgent, digne, émotion contrôlée — contraste direct avec Olamao (froid/messianique)
**Structure narrative :**
1. Rejet de la narrative Olamao (cite et réfute le terme "protection")
2. Accusation directe : "This is an invasion" — classe .accusation en rouge
3. Démontage du prétexte diaspora : "They are not oppressed. They were not in danger."
4. Réfutation de la citation obligatoire d'Olamao : "instability was manufactured — to justify a military action already planned"
5. Diplomatie échouée : "We asked for dialogue. We were given silence."
6. Remerciement OTAN / Rutte — nommément et sincèrement
7. Appel à la communauté internationale — trois questions en `.impact`
8. Clôture défiant : "Dacia Romania stands." (classe `.final`)
**Vocabulaire DR respecté :** "invasion", "our citizens", "sovereignty" — jamais "compatriots", jamais "protection operation"

#### Personnages restants à compléter
- Jonas JUNKER (Défense MER) : discours militaire à écrire (citation Olamao obligatoire)
- Dominic STOPH (Aff. étrangères MER) : discours diplomatique à écrire (citation Olamao obligatoire)
- Voichek RIBIKI (Intérieur MER) : discours sécuritaire à écrire (citation Olamao obligatoire)

---

## Identités visuelles de groupes fictifs

### [2026-05-06] N.O.M — Novus Ordo Mundi
**Dossier de référence :** D:\CECPC\PRODUCTION\BDA\02 - MERCURE\N.O.M
**Type :** Groupe terroriste fictif, extrême gauche, pro-Mercure, anticapitaliste
**Porte-parole fictif :** Wilma SMASTEN
**Création fictive :** 2009, enregistré comme association environnementale (couverture)

**Logo :** Crâne centré dans un triangle inversé (pointe vers le bas), design noir et blanc, épuré, géométrique. Deux petites flèches/chevrons flanquant la base du triangle.
**Palette :** Rouge profond, orange brûlé, noir dominant, gris sombres. Blanc osseux en accent.
**Style graphique :** Stencil street art, affiche soviétique/anarchiste, propagande militante, urban dystopique.
**Typographie :** Sans-serif gras, majuscules, agressif, slogans courts.

**Rhétorique récurrente :**
- Anticapitalisme : "LE CAPITAL", "exploitation", "néocapitalisme"
- Anti-OTAN : "l'OTAN surveille", "alliés tuent alliés", "OTAN détruit tout"
- Environnementalisme radical : "dérèglement climatique"
- Révolution : "LIBERATION or DEATH", "Ni Dieu ni Maître", "REJOIGNEZ LE MOUVEMENT"

**Tags/graffitis :** Peinture spray noire, stencil, logo crâne+triangle visible de loin, parfois avec lettres N.O.M.
**Matériaux produits dans O41 :** Affiches propagande, formulaire d'adhésion, lettre ouverte RNA, revendications, vidéo (NOM les lanscenets.mp4)

**Cohérence entre exercices :** Identité visuelle figée — ne pas modifier le logo ni la palette entre ORION et AURIGE.

---

## Numéros de téléphone fictifs — Règle de réalisme

**⚠ RÈGLE OBLIGATOIRE** : Ne jamais écrire `XX XX XX XX` dans un numéro de téléphone fictif. Utiliser les plages ci-dessous selon la zone géographique de l'inject.

| Région / Zone | Format | Exemple |
|---|---|---|
| 01 — Île-de-France | `01 99 00 XX XX` | 01 99 00 47 23 |
| 02 — Nord-Ouest / Outre-mer | `02 61 91 XX XX` | 02 61 91 08 54 |
| **03 — Nord-Est (Lorraine)** | **`03 72 67 XX XX`** | **03 72 67 14 89** |
| 04 — Sud-Est | `04 51 08 XX XX` | 04 51 08 37 62 |
| 05 — Sud-Ouest | `05 36 49 XX XX` | 05 36 49 91 05 |

**Application AURIGE 2BB (théâtre Lorraine) :** utiliser systématiquement le préfixe **03 72 67** suivi de 4 chiffres aléatoires.
Ces plages sont fictives mais au format valide — elles semblent crédibles sans appartenir à un abonné réel.
S'applique à : SMS psyops, courriers fictifs, articles de presse, formulaires, documents d'exercice.

### Numéros canoniques — attributions permanentes (tous exercices)

| Institution | Numéro fixe |
|---|---|
| **Palais présidentiel DAC / HPARIS** | **01 99 00 01 00** |

Ce numéro est **fixe et permanent** — utiliser `01 99 00 01 00` dans tous les documents officiels de la présidence (courriers Pallesson, en-têtes, fiches de contact). Ne jamais en attribuer un autre.

---

## Patterns efficaces

### [2026-05-06] Scénario 07.07 AURIGE 2BB — Messages WhatsApp propagande
Type de contenu produit : captures d'écran WhatsApp de messages psychologiques fictifs.
Contexte : messages de propagande envoyés à la population de HLunéville, accusant l'OTAN de vouloir piller la ville.
Faction fictive : "Mercure" (présenté comme protecteur de la population).
Langue : français (messages 1 et 2) + anglais (message 3, "Mercurian brothers and sisters").
Usage final : diffusion dans un article de presse fictif de l'exercice.

---

## Personnages récurrents
<!-- Voir PERSONNAGES.md pour les fiches complètes -->
