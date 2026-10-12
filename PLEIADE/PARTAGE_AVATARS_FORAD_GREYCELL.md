# Partage des avatars entre FORAD et GREYCELL — DELATTRE 26

> **Statut : PROPOSITION DÉFINITIVE (2026-10-07), en attente des décisions de l'utilisateur** — voir § 4 bis. Rien n'est appliqué dans la zone.
> Données : export eho `EXER\DELATTRE 26\01_Montage exercice\SAVE EHO\avatars-eho-2026-10-06.xlsx` (version 20:07) — 4 028 avatars, 236 groupes.
> Simulation en lecture seule : script `simul_partage.py` (dossier de travail de la session).

## 1. Principe
- Les **camps** (CAMP ROUGE, CAMP BLEU…) regroupent les **avatars principaux**, nettement orientés : on ne les modifie pas.
- Les autres avatars, **neutres** (bruit, gens qui écoutent les partis et peuvent s'orienter peu à peu), reçoivent l'un des deux groupes eho à créer : **PACK FORAD** ou **PACK GREYCELL**. Ils ne reçoivent **jamais** CAMP BLEU ni CAMP ROUGE.
- **On ajoute, on ne retire rien** : chaque avatar garde tous ses groupes actuels (COS vert, DALINKA, STARTEX, RESEAU RZO…) ; on lui ajoute seulement son PACK.
- **L'historique prime** : un avatar déjà utilisé par une cellule **lui reste** (posts, réponses, articles, messages, **likes et partages compris**), sinon il changerait de bord sous les yeux des joueurs. Le partage ne s'applique qu'aux avatars jamais utilisés.
- Une seule règle, réglée dans eho (« Avatars autorisés »), appliquée partout : direct du réseau social, Kit IA (périmètre « Ma cellule »), vérification **bloquante** des scénarios d'animation (l'Administration peut passer outre).

## 2. Les groupes ouverts dans eho (« Avatars autorisés ») — validé
Un groupe ouvert l'est **en entier** : pour qu'aucun avatar ne soit partagé par erreur, on n'ouvre que :
| Public | Groupes ouverts |
|---|---|
| FORAD | **CAMP ROUGE + PACK FORAD** |
| GREYCELL | **CAMP BLEU + PACK GREYCELL** |
| Joueurs DIV1 | CAMP DIV1 |
| RENS | RESEAU RZO |

CAMP NEUTRE, STARTEX, COS vert, EXERCICE DELATTRE 26… **ne sont pas ouverts directement** : leurs avatars reçoivent PACK GREYCELL (ou PACK FORAD s'ils vivent à Mercure). Les avatars sans groupe ne sont plus ouverts à tous.

## 2 bis. Réservations « Me l'approprier » — décision de l'utilisateur
- **La réservation suit le partage, jamais l'inverse** : un animateur FORAD ne réserve que dans **CAMP ROUGE + PACK FORAD**, un animateur GREYCELL que dans **CAMP BLEU + PACK GREYCELL**. Automatique une fois les « Avatars autorisés » réglés : eho ne laisse déjà réserver qu'un avatar ouvert à la cellule du compte.
- **Réservations existantes** : celles qui tombent du mauvais côté après le partage (avatar réservé mais jamais utilisé — un avatar utilisé reste à sa cellule par la règle 1) sont **listées avant application, puis libérées**.

## 3. Règles d'attribution, par ordre de priorité
| # | Règle | Destination |
|---|---|---|
| 1 | Avatar **déjà utilisé** par une seule cellule | cette cellule |
| 2 | Avatar déjà utilisé par **les deux** cellules | liste à trancher |
| 3 | CAMP DIV1 | joueurs DIV1 uniquement |
| 4 | **Habitant de Mercure** (pays « Mercure », ou groupe « MER - … » / « … Mercure ») — même s'il est en CAMP NEUTRE | **FORAD** (PACK FORAD s'il n'est pas en CAMP ROUGE) |
| 5 | CAMP ROUGE | FORAD |
| 6 | CAMP BLEU | GREYCELL |
| 6 bis | CAMP NEUTRE (hors Mercure) | PACK GREYCELL |
| 7 | **Journaliste** : il suit son journal — **TODAY MERCURE est le seul média rouge** ; journaliste vivant à Mercure → FORAD | FORAD / GREYCELL |
| 8 | Groupes « rouges » d'anciens exercices : O2 - COS rouge, 002-tweeter-mercure, REDTEAM (TROLL, PRESSE, C211…), 02-RED-*, O2-RED-*, Troll LPE, RED_Trolls_nm, O2-CDE-ROSO-Rouge | PACK FORAD |
| 9 | Groupes « bleus » : O2 - COS bleu, 003-tweeter-NATO, O4 Medias Francais, O2 Persona keys bleus GON, O2-CDE-ROSO-Bleu, O2-712CT-Bleu 1, O4 Groupe Officiel Français, O2-CECLANT | PACK GREYCELL |
| 10 | O2 - COS vert (+ UACIN), O2-CDE-ROSO-Gris, STARTEX, EXERCICE DELATTRE 26 | PACK GREYCELL |
| 11 | Les 4 avatars à la fois ROSO-Rouge et ROSO-Bleu/Gris (AbeGarm_vitraux, HoryGreg, MeeminKoryn, RablatMalcolm) | PACK GREYCELL |
| 12 | Groupes d'animation : O4animation1CA (58), O2-CDE-Influence-joueurs-BRUIT (50), O4 animation DIV1 (3) | PACK GREYCELL |
| 13 | Reste neutre (DALINKA, tweeters Arnland, auditeurs, « bruit scénario »…, sans groupe) | coupé en deux, groupe par groupe — **sans rééquilibrage** (décision) |
| — | **RESEAU RZO** (108, groupe du RENS) | **RENS** en plus de la cellule de son camp (ses membres ont des groupes variés : normal) |

## 4. Résultat simulé (sans l'historique ni les réservations, à relever)
| Destination | Avatars |
|---|---|
| FORAD | 1 966 |
| GREYCELL | 2 043 |
| Joueurs DIV1 | 19 |

Dont 167 habitants de Mercure côté FORAD ; RESEAU RZO : 92 côté FORAD, 16 côté GREYCELL (+ RENS). Aucun conflit restant.
Annabelle Buisson (`@Abuisson_Invaz`) et Aurélien Begnis (`@aurelbegnis`), familles de militaire vivant à Mercure : passés en CAMP ROUGE (CAMP BLEU retiré) par l'utilisateur → FORAD.

## 4 bis. Partage DÉFINITIF avec l'historique (export eho du 07/10/2026 08:37, onglet « # Usage ») — PROPOSITION
> Classeur : `PLEIADE\PARTAGE_AVATARS_FORAD_GREYCELL_2026-10-07.xlsx` (Synthèse · À décider · Partage complet · Comptes hors cellules). Script : `partage_def.py` + `partage_xlsx.py` (dossier de travail de la session).
- **Relevé complet** : les 10 sources « OK » (social direct, animation, 7 presses, messagerie). Conclusions eho : 3 849 jamais utilisés, 104 GREYCELL, 50 FORAD, 16 JOUEURS, 9 les deux, 0 inconnu.
- **Résultat avec les propositions** : FORAD **1 952** · GREYCELL **2 057** · joueurs DIV1 **19**. À ajouter : **PACK FORAD 1 671**, **PACK GREYCELL 1 953** ; 404 déjà couverts par leur camp.
- **Réservations** : 8, **aucune du mauvais côté** (5 FORAD, 2 GREYCELL, 1 par chloe.provence — compte CECPC hors fd/gc, cellule à préciser).
- **Comptes hors cellules** : rs20 (RENS) n'a utilisé que des avatars RESEAU RZO — conforme ; dv01-03 (DIV1) que du CAMP DIV1 — conforme ; chloe.provence (StatDirect_A ×6, rzo_kimberley, GotoVictory, Arnland_Singer, rzo_anonymous_3) — à préciser.
- **23 cas à décider** (proposition entre parenthèses) :
  - A. CAMP ROUGE utilisé par les deux cellules (7 : WherearetheFrogs, LetsgoMercure, Skolkan_rules, N_Savchenko, LuftBallons, Pedro_Kantor, shootArnland) → (FORAD, le camp prime).
  - B. CAMP NEUTRE utilisé par les deux (marie_duval → GREYCELL ; Mar1na_Dialecte → FORAD, usage majoritaire).
  - C. CAMP ROUGE utilisé **seulement** par des scénarios GREYCELL (10 : rzo_anonymous_1/2/3/5, rzo_bea_hvt, rzo_bernard_lecone, arn_kovalev, rzo_egor_fiodorov, arn_robert_danevois, Stepan_Roubek) → (FORAD : un groupe ouvert l'est en entier ; les lui donner à GREYCELL imposerait de retirer CAMP ROUGE). ⚠ La règle « l'historique prime » bute ici sur « les camps ne sont pas modifiés ».
  - D. CAMP DIV1 utilisé par GREYCELL (elmircaunity) → (joueurs DIV1).
  - E. Habitant de Mercure déjà utilisé par GREYCELL (BDADaily, NaPalm_for_Breakfast, Love_Our_Soldiers) → (GREYCELL, l'historique prime).

### Décisions de l'utilisateur — 2026-10-07
- **chloe.provence = GREYCELL.** Ses usages sont conformes (StatDirect_A, rzo_kimberley, GotoVictory, Arnland_Singer), sauf rzo_anonymous_3 (CAMP ROUGE).
- **Cas C (10 CAMP ROUGE employés par GREYCELL) : ils n'auraient pas dû l'être → FORAD.** C'est précisément ce que le partage doit empêcher. 8 n'ont encore **rien publié** : seulement des publications **prévues** dans des scénarios GREYCELL (15 au total) ; arn_kovalev a 1 tweet parti, rzo_anonymous_3 2 posts en direct (chloe.provence). **À traiter : retirer ces avatars des scénarios GREYCELL avant que les publications prévues partent.** Le relevé ne donne que des nombres : la liste des scénarios n'y figure pas.

- **Les 13 cas restants tranchés** (classeur rempli par l'utilisateur) : A (7 CAMP ROUGE) → **FORAD** ; Mar1na_Dialecte → **FORAD**, marie_duval → **GREYCELL** ; elmircaunity → **joueurs DIV1** ; E (BDADaily, NaPalm_for_Breakfast, Love_Our_Soldiers) → **FORAD** (⚠ contre ma proposition GREYCELL : la règle Mercure prime ; leurs publications GREYCELL sont déjà parties, aucune prévue).
- **Partage DÉFINITIF** : FORAD **1 955** · GREYCELL **2 054** · joueurs DIV1 **19** ; à ajouter **PACK FORAD 1 674**, **PACK GREYCELL 1 950** ; 404 couverts par leur camp. Classeur `PLEIADE\PARTAGE_AVATARS_FORAD_GREYCELL_2026-10-07_DEFINITIF.xlsx` (le fichier rempli par l'utilisateur est gardé tel quel à côté).
- **Liste « où corriger »** en production le 07/10 : onglet « # Usage — scénarios » de l'export eho (2026-10-07.2). ⚠ BDADaily n'a **pas de camp** : il ne lève pas d'alerte dans cet onglet (sans publication prévue, rien à corriger).

### Liste de corrections pour les animateurs — 2026-10-07 (export eho 09:33)
- Classeur `EXER\DELATTRE 26\01_Montage exercice\CORRECTIONS_AVATARS_SCENARIOS_2026-10-07.xlsx` : Mode d'emploi · À corriger (24 lignes, priorité URGENT < 24 h / BIENTÔT < 3 j, lien vers le scénario, 3 suggestions de remplaçant GREYCELL jamais utilisé — même profil, sinon particulier d'Arnland, sinon population ; pas d'officiel à la place d'un citoyen ; colonnes « avatar choisi » et « Fait ») · Par scénario (6) · Avatars GREYCELL libres (1 959).
- 23 publications à corriger dans 5 scénarios GREYCELL (n°123 OP LIONESS — **première ce soir 18:08**, n°91, n°96, n°107, n°108) + antoine_boyer (n°125 FORAD, brouillon) **en attente de décision**.
- ⚠ Les avatars rouges remplacés sont des **voix pro-Mercure** : aucun avatar GREYCELL ne joue ce rôle. Consigne écrite : message pro-Mercure → supprimer (ou confier à FORAD) ; message neutre → suggestion.
- Nouveau cas : **CorrespondantEst** (MER - SOCK-PUPPET, CAMP NEUTRE → FORAD) employé par le scénario GREYCELL n°140, terminé : rien à corriger.

### RESEAU RZO réservé au RENS — décision de l'utilisateur, 2026-10-07 (« à ce jour »)
- Les 108 avatars du RESEAU RZO (90 CAMP ROUGE, 15 CAMP NEUTRE, 3 CAMP BLEU) ne vont **ni à FORAD ni à GREYCELL** : RENS seul. Remplace la règle § 3 « RENS en plus de la cellule de son camp » et les choix FORAD des avatars rzo_* du cas C.
- Partage recalculé : FORAD **1 863** · GREYCELL **2 038** · RENS **108** · DIV1 **19** ; PACK FORAD 1 672, PACK GREYCELL 1 937.
- **Corrections étendues** : classeur `CORRECTIONS_AVATARS_SCENARIOS_2026-10-07.xlsx` = **120 publications dans 22 scénarios** (dont FORAD : n°43, 95, 105, 125, 134), priorités URGENT / BIENTÔT / à faire / brouillon, onglets d'avatars libres FORAD et GREYCELL.
- **Mécanisme** : eho 2026-10-07.3 — case **« Exclusif »** dans « Camps autorisés… » (un avatar d'un groupe exclusif n'est ouvert qu'aux camps de ce groupe, même s'il est dans CAMP ROUGE). À cocher sur RESEAU RZO, ouvert au seul camp RENS.
- **Kit IA « Ma cellule »** (animation) : par défaut, le kit ne contient que les avatars qu'eho ouvre à la cellule de l'animateur → un kit FORAD, un kit GREYCELL, sans RZO.

### Fichier d'import des PACK — 2026-10-07 (export eho de 09:33)
- `EXER\DELATTRE 26\01_Montage exercice\IMPORT_EHO_PACKS_FORAD_GREYCELL_2026-10-07.xlsx` : onglet « Avatars » = `username` + `groups` (PACK FORAD **1 671**, PACK GREYCELL **1 938**, total 3 609) ; onglet « # Lisez-moi » ignoré par l'import. Décisions tardives intégrées : antoine_boyer → GREYCELL, CorrespondantEst → FORAD (24 cas tranchés). Partage : FORAD 1 862 · GREYCELL 2 039 · RENS 108 · DIV1 19.
- **Essai sur l'eho de démo** : groupes PACK créés, 100 % des lignes appliquées, **aucun champ modifié, aucun groupe retiré** (comparaison des exports avant / après) ; seuls 2 avatars créés car absents de la démo (présents en production). Base de démo remise en l'état.
- ⚠ **Durée ≈ 10 min** pour 3 609 lignes (la page peut sembler figée ; relancer est sans danger : l'import n'ajoute que ce qui manque). ⚠ Un username inconnu d'eho serait **créé** (fiche vide) : refaire le fichier sur un export du jour juste avant l'import.

### Mise à jour sur l'export de 11:50 (`SAVE EHO\avatars-eho-2026-10-07 (1).xlsx`, sources OK)
- Correctif de calcul : les décisions de l'utilisateur s'appliquent **même quand le cas n'est plus en conflit** (des scénarios corrigés faisaient disparaître le conflit et retomber l'avatar dans la règle — ex. habitants de Mercure renvoyés à GREYCELL). Vérifié : toutes les décisions respectées.
- Partage : FORAD **1 861** · GREYCELL **2 040** · RENS 108 · DIV1 19 ; import régénéré : PACK FORAD **1 670**, PACK GREYCELL **1 939** (tous les usernames existent dans l'export).
- **Nouveau cas : MullerDaniel** (ARN - CITOYEN, sans camp) — employé par FORAD (n°125, en cours, 13:22) et GREYCELL (n°123, n°91 : remplaçant que j'avais suggéré). Proposition GREYCELL **écartée** : ✅ **décision utilisateur → FORAD** (« la FORAD a le droit de créer et d'utiliser des comptes d'avatar d'Arnland ») ; GREYCELL le retire des n°123 (ce soir 18:08) et n°91 (08/10 10:43). Import régénéré : PACK FORAD **1 671**, PACK GREYCELL **1 938**.
- Liste de corrections : règle élargie (cellule du partage ≠ cellule du scénario, alerte ou pas) → **106 publications** dans 23 scénarios (120 le matin).

### Application dans eho (production) — 2026-10-07 après-midi, par l'utilisateur
- ✅ Import des PACK fait : PACK FORAD **1 671**, PACK GREYCELL **1 938** (vérifié par l'utilisateur dans « Groupes »).
- « Camps autorisés… » réglés par l'utilisateur. ⚠ Première version : « Exclusif » coché sur Camp rouge, Camp bleu, Camp div1, Pack forad, Pack greycell et Reseau rzo → **incohérent** (un avatar dans plusieurs groupes exclusifs est ouvert à TOUS leurs camps : les 90 RZO ∩ CAMP ROUGE et 3 RZO ∩ CAMP BLEU redevenaient ouverts à FORAD / GREYCELL). Consigne donnée : « Exclusif » **sur Reseau rzo seul** — ✅ **corrigé par l'utilisateur** (capture : badge « exclusif » sur Reseau rzo uniquement) ; contrôle attendu dans « Avatars autorisés » → « Voir comme un camp » (FORAD : Camp rouge ≈ 191 + Pack forad ; GREYCELL : Camp bleu ≈ 101 + Pack greycell ; RENS : Reseau rzo 108).
- Rappel de la règle « Exclusif » : à cocher sur le SEUL groupe à réserver ; plusieurs groupes exclusifs qui se recouvrent s'ouvrent mutuellement.

## 5. En attente
- **Contrôle bloquant des scénarios dans l'animation** (non développé) : proposé à l'utilisateur, en attente de sa réponse. D'ici là, les scénarios programmés publient avec n'importe quel avatar.
- ✅ **antoine_boyer → GREYCELL** (décision utilisateur, 07/10) : FORAD le retire du scénario n°125 ; ligne « URGENT » du classeur de corrections, avec 3 remplaçants FORAD.
- **Correction à la main** des scénarios GREYCELL qui emploient un avatar rouge ou DIV1 (publications prévues) : export eho → onglet « # Usage — scénarios » → colonne ALERTE.
- **Mise en œuvre** (groupes PACK FORAD / PACK GREYCELL, « Avatars autorisés », Kit IA « Ma cellule », vérification bloquante, avatars sans groupe) : sur décision de l'utilisateur, **de préférence après** la correction des scénarios.
- Mise en œuvre (groupes PACK, « Avatars autorisés », Kit IA « Ma cellule », vérification bloquante, avatars sans groupe) : **seulement sur décision de l'utilisateur**.

## 6. Rappel
- Likes invisibles dans la vue des joueurs du réseau social : à reprendre après cette réflexion.
