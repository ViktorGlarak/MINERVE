# MÉMOIRE — ANALYSTE ARNLAND (Expert Arnland / pays allié fictif)

> 🗂️ **Articulation avec le vault** — **Roster & camps : autorité unique = `vault/entities/`** (1 persona = 1 note `ENT-*`, camp défini une seule fois). **Ce fichier = détail exhaustif** (doctrine, ORBAT, fiches bio HN, chronologies, règles éditoriales). Vue générée à jour : `vault/_vues/MEMOIRE_arnland.generee.md`. ⚙️ `vault/_tools/valider.py` **bloque** toute contradiction de camp entre ce fichier et les entités.

Agent créé le **2026-05-23** — migré vers `ANALYSTE\ARNLAND\` le **2026-05-25**.
**Sources countrybook** (officiel ORION 26, sections A→F + Annexes) :
- `D:\CECPC\Orion 26 - Arnland (1).docx` (version Word, 11,5 Mo)
- `D:\CECPC\PRODUCTION\EXER\01 ORION 26\ORION-4\01 - CORPUS DOCUMENTAIRE\Orion 26 - Arnland.pdf` (5,1 Mo)

> Synthèse opérationnelle consolidée dans cette mémoire (l'ancien fichier `PAYS_ARNLAND.md` n'existe plus — réf. supprimée le 2026-05-31). **✅ Ingestion portée à 100 % le 2026-05-31** (sections A→F + Annexe Personalities) → voir **§ COUNTRYBOOK ARNLAND — COMPLÉMENT INTÉGRAL**. ⚠ Correction : Alltinget = **132** sièges (et non 128).

---

## 🎯 CORRECTION DES CAMPS — fiches bio HN Arnland (2026-06-18, validé utilisateur/créateur)

Audit des **21 fiches Arnland** du trombino MINAUTORE : le générateur déduisait le camp du **titre de poste** (heuristique) → orientation réelle (dans le **narratif**) ignorée. **7 camps corrigés** (autorité ANALYSTE_ARN, miroir `vault/entities/ENT-*` + bios.js) :

| Figure | Avant | ✅ Après | Justification narratif |
|---|---|---|---|
| **Grigori Hartmann** (Maire HSarre-Union) | bleu | **🔴 rouge** | Élu sur des **listes pro-MER**, mercurianophone, relaie le discours pro-MER |
| **Dmitri Kovalev** (Maire HAlberstroff) | bleu | **🔴 rouge** | **Ouvertement pro-MER**, facilite la présence MER + actions para-légales, publie en mercurien |
| **Henri Weber** (Maire HSarrebourg) | neutre | **🔴 rouge** | « En réalité **proche des milieux pro-MER** », relaie des messages pro-MER |
| **Boris Kalugin** (Représentant **CICR/ICRC**) | bleu | **⚪ neutre** | Le CICR est **neutre par mandat** (humanitaire impartial) |
| **Elena Petrovna** (**Blue Shield**) | bleu | **⚪ neutre** | Protection du patrimoine, organisation internationale neutre |
| **Igor Mishin** (Arnish Refugee Council) | bleu | **⚪ neutre** | ONG humanitaire (réfugiés) |
| **Nikolaï Brenner** (Maire HMorhange) | bleu | **⚪ neutre** | Ex-officier ARN mais « positionnement **ambigu** », soutien des patriotes mercuriens |

**Inchangés (corrects)** : gouvernement ARN + préfet (🔵), Gervais/Krauss/Voloshyn (🔵 maires pro-ARN), Borchenko (⚪ double jeu éco), Volkonsky/Savchenko (🔴 pro-MER explicites) ; **Lang et Thiebaut** laissés tels quels (validé).

**Correction DURABLE** : table `CAMP_OVERRIDE` (par id `arn_*`) dans `MASTAURIGE\…\OUTILS\generer_trombino_bios.py` (les 2 instances 7BB) — prime sur l'heuristique → une régénération ne revient PAS en arrière. `vault/entities/ENT-{hartmann,kovalev,weber,kalugin,petrovna,mishin,brenner}.md` alignés (autorité camp). ⚠ Le **camp détermine l'effet ILI** : un mauvais camp inverse l'effet — d'où l'audit.

## ⚠ ÉVOLUTIONS SYSTÈME — 2026-05-29

### Règle MASTAURIGE obligatoire
Tout fichier sous `...\MASTAURIGE\` requiert la consultation de MASTAURIGE. ANALYSTE_ARN produit le **contenu DAC/ARN** — MASTAURIGE gère le **format et l'intégration technique**.

### Doctrine calibration brigade (AURIGE)
Les injects AURIGE 2BB doivent être calibrés niveau **PC brigade**, pas état-major de division.
- Contenu ARN/DAC attendu par le PC brigade : plaintes de maires de villes DAC fictives (H-préfixe), journaux locaux, signalements citoyens, rumeurs locales sur les forces
- Villes ZO prioritaires : HCHATEAU-SALINS, HLUNEVILLE, HSARREBOURG, HToul
- Personnage DJOBOVIC (8e DAC) : ancrage possible pour injects locaux (prise de position, communication terrain)

### [2026-06-21] ✅ VALIDÉ — Manif anti-OTAN 07.11.I02 (3 tweets, D+37, camps INVERSÉS 7BB)
Re-revue ANALYSTE_ARN après corrections : **doctrinalement correct et crédible**.
- **Personas (descriptifs trombino, handles + camps conservés) :**
  - **@GavrilovBorislav** → « Borislav Gavrilov — Habitant **HDieuze** · diaspora mercurianophone d'Arnland » (🔴). Profil diaspora MER locale enracinée (« trois générations »), pas agent MER auto-désigné. ZO HLorraine, préfixe H OK, onomastique slave cohérente.
  - **@MakarovSid** → « Sid Makarov — Habitant **HBlamont** · diaspora mercurianophone d'Arnland » (🔴). Idem.
  - **@MarionKessler57** → « Marion Kessler — civil Moselle » (⚪). Civile non alignée, nom franco-allemand cohérent Arnish/Lorrain non-diaspora. Ancrage de crédibilité du cortège.
- **Tweets** : escalade même jour (Kessler 9h HMorhange ⚪ → Gavrilov midi HDieuze 🔴 → Makarov 16h HBlamont 🔴). Registre « notre ville / nos droits / chez nous », **plus de « vive MER » ni auto-désignation** → effet ILI crédible (victimisation locale, pas slogan d'État). Gavrilov « occupants pas libérateurs » inverse le narratif OTAN « nation hôte libérée » (storyline 07-04) sans réclamer MER. Makarov : grief surveillance/répression → posture victimaire rouge.
- **Note** : HMorhange = maire **Brenner** (⚪ ambigu) → une manif y démarrant avec une civile ⚪ renforce la cohérence, aucun conflit.

### [2026-06-20] Récup HN 2BB→7BB dans le collab MINOTAURE (20 injects)
Liste Guillaume `HN - ADAPTATION 2BB 7BB V1.docx` bakée dans le collab 7BB : **7 courriers HN** (maires/préfet — corridors humanitaires, écoles, musées, cultes, relances préfet) + 6 articles (panique civils, Guterres/ONU, POW/CICR) + 7 tweets. Codes 7BB **08.01.I0x / 08.02.I0x** (+ 2 vers 07.12.I05/06). Adaptation H-préfixe conservée (HSARREBOURG, HMORHANGE, HNANCY…), DAC→ARN. ⚠ **À valider par ANALYSTE_ARN** : noms des maires signataires des courriers (cohérence avec le roster HN + camps : Weber 🔴, Brenner ⚪, Birkmann 🔵) ; camps des courriers (mis « neutre » par défaut). Détail technique : `MASTAURIGE\MEMOIRE.md` [2026-06-20].

### [2026-06-20] ⭐ ROSTER HLORRAINE V2 — fiches EHO ARNLAND (intégrées agents + trombino)
Source : `CREATION\06 - Arnland\EHO ARNLAND - MODIFICATIONS V2.odt` (copiée depuis E:). **6 figures** intégrées (parser `parse_eho_v2` dans `generer_trombino_bios.py` → bios.js + pop-up). **Réseau informel d'élus lorrains** gravitant autour de **Mordidchev** — exploitable ILI.

| Figure | Rôle | Âge | Camp | Parti | Levier ILI clé |
|---|---|---|---|---|---|
| **Rémy Laffin** | Gouverneur région HGrand Est | 67 | ⚪ neutre (corrompu) | aucun (haut fonctionnaire) | **Liens cachés groupe N.O.M** (chantage majeur, traçable via flux financiers régionaux) ; ami de Mordidchev ; surveillé par Radulov ; pré-retraite |
| **Serge Mordidchev** | Maire **HNancy** | 50 | ⚪ neutre | ASP (opposition centre-gauche) | **Très actif sur X** ; pivot du réseau lorrain ; ami Laffin (éclaboussable si N.O.M révélé) ; calcul politique trop visible |
| **Nathalie Martin** | Maire **HSarre-Union** (~35% merc.) | 41 | 🔴 pro-MER | sans étiquette (droite rég.) | **Fille Kimberley** liée à 2 militaires ARN pro-MER (Crusadier, Degardin) — levier de pression/coopération ; X rare |
| **Robert Danevois** | Maire **HChateau-Salins** | 38 | 🔴 pro-MER | sans étiquette | **Lien suspecté avec Léon-Philippe Thely** (agitateur pro-MER) ; activité éco à l'arrêt → réceptif aux offres ; X absent |
| **Nadia Promesy** | Maire **HSarrebourg** (~20% merc.) | 37 | 🔵 pro-ARN modéré | APP local / union | Jeune, non-partisane, difficile à attaquer ; connexions indirectes réseau Mordidchev-Danevois (associable) ; X modeste/sobre |
| **Jean-Louis Adriane** | Maire **HLunéville** | 63 | ⚪ neutre | indépendant | Ami Mordidchev/Promesy ; lié à **Antoine Bourguignon** (prés. agriculteurs régionaux — réseau agroalimentaire stratégique en pénurie) ; sur X (info pratique) |

⚠ **Remplacements de villes (validé utilisateur 2026-06-20)** : Mordidchev prend **HNancy** (ex-Gervais 🔵), Promesy prend **HSarrebourg** (ex-Weber 🔴), Martin prend **HSarre-Union** (ex-Hartmann 🔴). Les **anciens maires sont GARDÉS au trombino EN RÉSERVE** (« sans ville attribuée », camps conservés) — réemployables si on doit recaser un maire. **5 en réserve (au 2026-06-20)** : Gervais (ex-HNancy 🔵), Weber (ex-HSarrebourg 🔴), Hartmann (ex-HSarre-Union 🔴), **Krauss (ex-HLunéville 🔵, reprise par Adriane)**, **Thiebaut (ex-HChateau-Salins 🔵, reprise par Danevois)**. ✅ **Courriers HN signés par les maires V2 (2026-06-20)** : les 7 courriers 08.01 (collab `Sites\COURRIERS`) ont leurs signataires remplacés par ville — HNancy=Mordidchev, HSarrebourg=Promesy, HChateau-Salins=Danevois, HSarre-Union=Martin, HLunéville=Adriane ; préfet=Birkmann ; HHaguenau (Lang) conservée car sans fiche V2. ✅ **Entités vault** créées : `vault\entities\personas\ENT-{laffin,mordidchev,martin-nathalie,danevois,promesy,adriane}.md` (build vert). Détail technique : `MASTAURIGE\MEMOIRE.md` [2026-06-20].

### Nouveaux injects 08.02 créés (2026-05-29)
- `08.02.02Ai` : TV4 — capture 104 soldats MER par 8e DAC / DJOBOVIC (28 Mai)
- `08.02.02Bi` : @KolesnikovAndrei — rumeurs maltraitance POW, discrédit DAC vs FR (29 Mai 16h00)

---

## Convention géographique — Préfixe H

**Règle :** Toute ville française réelle prend le préfixe **"H"** dans les exercices Mercure.
Le H marque le caractère fictif de l'environnement d'exercice.

| Ville réelle | Code exercice |
|---|---|
| Paris | HPARIS |
| Nancy | HNANCY |
| Lunéville | HLUNEVILLE |
| Sarrebourg | HSARREBOURG |
| Lyon | HLYON |
| Marseille | HMARSEILLE |
| Strasbourg | HSTRASBOURG |
| *(toute autre ville française)* | H + nom |

**Portée :** intégralité du territoire Dacie Romanie / Arnland = France fictive.
**Application :** injects, articles, discours, tweets, ordres, documents — sans exception.

---

## Nom du pays selon l'exercice

| Exercice | Nom du pays | Notes |
|---|---|---|
| ORION 26 | **Arnland** | Nom canonique |
| AURIGE 2BB (scénario Guillaume) | **Dacie Romanie (DR)** | Mêmes personnalités, même structure |
| Exercices futurs | À définir par l'agent éditorial | Toujours pointer vers cette mémoire |

Même pays, même Countrybook, même personnalités — seul le nom change selon l'exercice.

---

## Données politiques

- Régime : démocratie parlementaire (république)
- Parlement : **Alltinget — 132 sièges** ⚠ *(corrigé le 2026-05-31 : countrybook = 132, FPTP, mandats 4 ans — l'ancienne valeur « 128 » était erronée)*
- Parti au pouvoir : APP (centre-droit, pro-OTAN)
- Opposition : ASP (ambiguë sur SCO, amplifiée par Mercure)
- ⚠ **6 partis au total** (pas seulement APP/ASP) — voir § COMPLÉMENT INTÉGRAL

### Personnages gouvernementaux
| Personnage | Rôle |
|---|---|
| **Sture Pallesson** | Président (APP, centre-droit), pro-OTAN |
| **Vincent Karrlson** | Premier Ministre (APP) |
| **Mira Janković** | Ministre des Affaires étrangères |
| **Andrei Belov** | Ministre de la Défense |
| **Dmitri Radulov** | Ministre de l'Intérieur |
| **Viktor Dragunov** | Finances |
| **Vladislav Marinov** | Chef ASP (opposition, pro-SCO ambiguë) |

### Personnages judiciaires
| Personnage | Rôle |
|---|---|
| **Stanislav Vuković** | Président Cour suprême |
| **Mariya Stepanenko** | Juge constitutionnel |
| **Nikolai Zoric** | Juge pénal |

### Personnages internationaux
| Personnage | Rôle |
|---|---|
| **Kristina Zoric** | Porte-parole OTAN |
| **Milan Andreev** | Porte-parole UE |
| **Boris Kalugin / Tatiana Velkova** | ICRC |
| **Yegor Malenko** | Président Dushman (allié-partenaire) |

---

## Données militaires

- ADF : ~129 000 actifs | SDF : ~200 000 (mobilisation)
- Équipement : M1 Abrams, CV90, BMP-2, T-72, HIMARS
- Aviation : 110 jets (Mirage F1, MiG-21, Su-25)
- SAM : SA-5, SA-3, Crotale
- Marine : 25 bâtiments — bases : HBrest, HCherbourg, HToulon

### Commandement militaire
| Personnage | Rôle |
|---|---|
| **VONG** | CHOD (chef des armées) |
| **HUS** | CGS (état-major terrestre) |
| **BYSTROM** | Marine |
| **FRIES** | Armée de l'air |
| **GRADHOLM** | SOF |
| **ARNE** | BMF |
| **Général Aleksandr Stanev** | Chef ASPS |

### Unités engagées — AURIGE 2BB (Lorraine)

| Unité | Commandant | Type | Rôle dans l'exercice |
|---|---|---|---|
| **8e DAC** (8ème Division Armoured Corps) | **Général DJOBOVIC** | Blindée / méca DAC | Unité principale DAC en Lorraine — combat retardateur puis contre-pression sur MER |

**Général DJOBOVIC — CO 8e DAC :**
- Commandant de la 8ème Division Armoured Corps, forces de Dacie Romanie
- Responsable de l'encerclement et de la capture de 104 soldats MER à HNANCY dans la nuit du 27 au 28 mai 2026 (D+32→D+33)
- Opération : manœuvre en tenaille nocturne (armour + méca) — zéro perte DAC
- Citation publiée TV4 : *"One hundred and four prisoners. No casualties on our side. This is what Dacia Romania's army delivers."*
- **À utiliser dans les injects bleus** : figure de la compétence tactique DAC, contrepoids aux narratives MER de supériorité
- **Exploitable par MER (ILI)** : si Mercure produit un inject de déni ou de retournement sur la capture des 104 hommes, DJOBOVIC est la cible nominative à discréditer

**Éléments canonisés (détails fixés le 2026-06-01 pour l'inject corruption 07.04.07i) :**
- Prénom / grade complet : **gén. de brigade Marko DJOBOVIĆ**
- Ville natale (adresse perso DAC) : **HCOMPIEGNE** (14, rue Saint-Georges) *(corrigé 2026-06-01 — était HMETZ)*
- **Inject 07.04.07i — « Factures & corruption » (LO 4 + LO 5, D+37 / 01 Jun)** : ILI MER l'accuse d'avoir acquis une **Arrinera Hussarya GT** (265 680 £) via des **fonds d'aide détournés**, en lien avec des **officiers polonais**. Concession vendeuse : **Auto Premium Kowalczyk Sp. z o.o.** (Varsovie, NIP 701-024-58-63), propriété du **frère du chef du bataillon polonais déployé, ppłk Tomasz KOWALCZYK**. 3 produits : `07.04.07Ai` (article Today Mercure), `07.04.07Bi` (tweet @MaiaKovalenko), `07.04.07Ci` (facture polonaise fuitée).
- ⚠ L'inject **insinue** sur la probité des officiers **français** voisins **sans les incriminer** (effet de doute, pas d'accusation directe).
- Camp de DJOBOVIĆ inchangé : **🔵 BLEU (DAC)** — il est la **cible** de l'ILI MER, pas un allié de MER.

---

## 📰 ENVIRONNEMENT INFORMATIONNEL (countrybook, approfondi 2026-05-31)

> Section E « Information Setting » du countrybook Arnland. Complète le couple TV4/HEXAGONE déjà listé.

**Chiffres clés :** **Press Freedom 97/180** (RSF 2024 — « média challenged ») · 3 quotidiens nationaux (~945 000 ex.) · **4 chaînes TV + 7 radios** (AM 3 / FM 15 / SW 2 ; 3 stations TV + 5 612 répéteurs) · indicatif pays **+463** · câbles sous-marins via **HMARSEILLE**.

**Caractère du paysage média (≠ Bothnia) :**
- **Presse = extension des partis politiques** : perçue comme **opinion/éditorial plus que factuelle**. Diffusion surtout urbaine → **rate ~35 % de la population rurale**.
- **Journaux régionaux = porte-voix du Gouverneur de chaque Län** (suit sa ligne politique ; les voix alternatives, en ville, subissent procédures, grèves, coupures de courant).
- **Chaînes TV d'État à allégeances partisanes** ; partisanerie ouverte largement répandue.
- **Paysage « diversifié » mais emprise de l'élite** : réforme transparence de propriété (2014) mais gains fragiles ; violences/impunité contre journalistes.
- ⭐ **« Information warfare » avec Mercure** : Arnland a **banni les médias et réseaux sociaux mercuriens**, cyber-harcèlement, **procès pour « trahison »** → posture défensive anti-MER exploitable (narratif MER : « Arnland censure, viole la liberté de la presse »).
- **Magnat des médias : Tor Horby** (Horby Holdings — réseaux HPARIS).
- **Régulateurs :** **National Council for Media Affairs** (organe indépendant sous le Ministère des Travaux publics/Transports/Télécoms/IT) ; **Ministry of Information and Communications** (sécurité de l'information, Information Classification Act).

**Implication ILI 7BB :** média arnish **partisan, fragile, urbain** = terrain favorable aux narratifs MER de délégitimation (LO 4 — « État failli/corrompu qui muselle la presse »). Le bannissement des médias MER alimente la posture victimaire rouge (« la vérité censurée »).

---

## ⚔️ FORCES ARN — AURIGE 7BB / MINOTAURE 26 (GET-R-FOR)

> ⚠ **Différent du 8e DAC d'AURIGE 2BB.** Pour MINOTAURE 26, les forces ARN engagées = **GET-R-FOR** (*Air-Land Joint Force GET-Response-Force*), régénérées et appuyant directement le MC-LCC à partir de D+20. Source : OPORD 03 PH3b (Main Body + Annexe Z « ARN Forces »).

| Unité | Mission 7BB | Subordination |
|---|---|---|
| **61ᵉ MECH BDE** | Participe à la **prise/contrôle de HMETZ** (NET D+20) | TACON **MNC-W (US DIV)** |
| **62ᵉ RECCE BDE** | **Contrôle de HNANCY** (NET D+25) | TACON **MND-SW** |
| **63ᵉ ARMD BDE** | **Réserve** de la GET-R-FOR | GET-R-FOR |
| **SDF BDE « WEST » (HMARNE)** | Sécurité **à l'ouest de la HMARNE** : HREIMS, HTROYES, HCHALONS-EN-CHAMPAGNE | TACON MC-LCC |
| **SDF BDE « EAST » (HALSACE)** | **Harcèle le FGF-L dans les HVOSGES** (dès D+20) | TACON ARRC/MN |

**Posture narrative :** l'Arnland est la **nation hôte** que l'OTAN vient libérer ; la GET-R-FOR combat aux côtés de la coalition. Cible ILI rouge privilégiée (storyline **07-04 Rupture des alliances**) : présenter l'ARN comme **abandonné/instrumentalisé par l'OTAN** (« c'est l'Arnland qui paie le prix du sang ») — cf. narratifs ORION 26 (« On se bat seuls », « Arnland buries the dead »).

---

## 📇 FICHES BIO HN (Host Nation) — ingérées le 2026-06-10

> **Sources :** `D:\CECPC\PRODUCTION\CREATION\06 - Arnland\HN FICHE BIO\` (32 fichiers .docx) + `06 - Arnland\Interlocuteurs   +Tampons HN.docx`.
> Deux corpus distincts : **MINOTAURE 26** (théâtre HLorraine, daté 2026-06-09) et **ORION 26 O41** (théâtre HPoitou/HVienne, datés 2026-03-17). Chaque fiche = Nom/Prénom/Âge + Parcours + Objectifs + Forces + Faiblesses + ligne Réseaux sociaux.

### A. MINOTAURE 26 — `20260609_NU_MINOTAURE_26 - FICHES BIO ARNLAND.docx` ⭐ pour AURIGE 7BB

**Gouvernement national (bios détaillées — confirment le roster déjà connu) :**
| Personnage | Poste | Angle ILI exploitable (faiblesses de la fiche) |
|---|---|---|
| **Sture Pallesson** (48) | Président (APP) | Échec « War on Corruption » 2006 → lois sans effet ; privilégie la com sur l'action ; coalition fragile. Battu 2014, réélu sur la crise. Ex-gouverneur HHauts-de-France. X institutionnel |
| **Vincent Karrlson** (54) | Premier ministre (APP) | Apparatchik sans base électorale ni charisme — choisi pour sa loyauté ; mal à l'aise en crise médiatique. X minimal |
| **Mira Jankovic** (46) | MAE | Suspicion interne APP sur ses loyautés ; attaquée personnellement par réseaux pro-MER. Très active sur X (contre-narratifs, droit international) |
| **Andrei Belov** (57) | MINDEF | Issu du complexe militaro-industriel ; dépendance OTAN ; tensions budgétaires avec Karrlson ; accès journalistes difficile. ⚠ **Anomalie source** : son § Parcours mentionne « Daniel Schmidt » (reliquat copier-coller de la fiche ORION SCHMIDT) — **Belov fait foi pour 7BB** |
| **Dmitri Radulov** (51) | MININT | Ex-ASPS, dur, affaires de surveillance abusive classées ; rhétorique « 5e colonne » contre la diaspora MER (risque radicalisation) ; friction avec Jankovic. RS populiste-sécuritaire |

**Échelon territorial HLorraine (= la ZO 7BB) — personnages clés injects brigade :**
| Personnage | Poste | Profil / levier ILI |
|---|---|---|
| **Augustin Birkmann** (46) | Préfet région HLORRAINE | Homme de procédures, intègre mais dépassé par le tempo ; conteste légalement les injonctions Radulov ; isolé de Paris(HParis). Aucun RS personnel |
| **Henri Weber** (63) | Maire HSARREBOURG | ⭐ Pharmacien, **proche des milieux pro-MER** (origines familiales) ; ville à **35 % de diaspora mercurienne** ; relaie des messages pro-MER. Cible/relais parfait LO4 |
| **Émile Gervais** (44) | Maire HNANCY | Jeune ambitieux (gauche), vitrine « capitale de résistance », très actif RS, tensions avec le gouvernement, inexpérimenté militaire. Hub logistique/humanitaire |
| **Bernard Thiebaut** (67) | Maire HCHATEAU-SALINS | Agriculteur retraité, maire depuis 2001, **liens familiaux avec des familles mercuriennes frontalières** ; commune en dépopulation ; aucun RS |
| **Dorothée Lang** (41) | Maire HHAGUENAU | **Biculturelle MER/ARN**, avocate droit des minorités, position intenable, **sous surveillance MININT**, ~45 % électeurs d'origine MER. Personnage charnière LO4/LO5 |
| **Isabelle Krauss** (39) | Maire HLUNEVILLE | Patriote arnlandaise (aile sociale APP, proche Karrlson), base arrière/hôpital de campagne ; peu charismatique. Présente Facebook + **ArnNet** |
| **Boris Kalugin** (52) | Représentant ICRC Arnland | Médecin, depuis 2020 ; POW/civils/sensibilisation ; moyens limités, accès difficile *(même fiche qu'ORION — personnage stable inter-exercices)* |

#### ⭐ MAJ 2026-06-11 — fichier `20260611_NU_MINOTAURE_26 - FICHES BIO ARNLAND.docx` (4 nouveaux maires + 2 leaders pro-MER)
| Personnage | Poste | Camp | Note |
|---|---|---|---|
| **Irina Voloshyn** | Maire HTOUL | 🔵 bleu | nouvelle fiche |
| **Nikolaï Brenner** | Maire HMORANGE | ⚪ neutre | positionnement ambigu (ex-officier ARN mais soutien des patriotes MER) — *corrigé 06-18* |
| **Grigori Hartmann** | Maire HSARRE-UNION | 🔴 rouge | élu sur des **listes pro-MER**, mercurianophone (ville saisie par 27BIM en CAX1) — *corrigé 06-18* |
| **Dmitri Kovalev** | Maire HALBERSTROFF | 🔴 rouge | **ouvertement pro-MER**, actions para-légales — *corrigé 06-18* |
| **Piotr Volkonsky** | Leader religieux protestant **pro-Mercure** | 🔴 rouge | relais ILI 07-03 « libération », sermons pro-MER |
| **Nataliya Savchenko** | Leader associative **pro-Mercure** | 🔴 rouge | mobilisation de la diaspora MER, victimisation |
| **Maksym Borchenko** (52) | **Patron de Borchenko Transports**, membre FEA (Federation of Employers in Arnland) | ⚪ **neutre** (double-jeu) | Né à HSarrebourg ; logistique transfrontalière, l'une des rares infrastructures encore opérationnelles ; **entrepôt transfrontalier bloqué sous contrôle de fait des forces MER** (levier) ; 340 employés bilingues (arnlandais/mercurien) → pression sociale ; opportuniste « évite de s'engager prématurément d'un côté ou de l'autre » ; X minimaliste, aucune déclaration politique. **Acteur économique pivot** — cible/levier ILI possible (chantage entrepôt, légitimité sociale). *(Découvert 06-12 : son en-tête manquait au parseur trombino, fiche fusionnée à tort dans Petrovna — corrigé.)* |
> Détail complet (parcours/objectifs/forces/faiblesses) dans le .docx + **`bios.js` du trombinoscope** (cartes cliquables). Pallesson, Karrlson, Jankovic, Belov, Radulov, Birkmann, Weber, Gervais, Thiebaut, Lang, Krauss, Kalugin, Mishin (ARC), Petrovna (Blue Shield) = fiches **mises à jour** (version 06-11 plus riche). **+ Maksym Borchenko (ajouté 06-12).**

> **Usage 7BB :** ces maires sont exactement le catalogue « injects brigade » (plainte du maire, notable hostile, relais pro-MER local). Weber et Lang = relais/victimes des narratifs rouges 07-03 « Vent de libération » ; Gervais et Krauss = cibles de discrédit ; Thiebaut = inject « liens familiaux ambigus » ; Volkonsky/Savchenko = **voix pro-MER locales** (07-03). **MINAUTORE doit citer ces fiches, pas les redéfinir.**

### B. ORION 26 O41 — 31 fiches HN théâtre HPoitou/HVienne (datées 2026-03-17)

Roster compact (fiche complète dans le .docx du même nom) :
| Domaine | Personnages |
|---|---|
| **Gouvernement** | MINDEF **Daniel Schmidt** (54) · MAE **Aleksandr Fischer** (58) |
| **Préfets** | Région HPoitou-Charente : **Erik Karlson** (55) · Dép. HVienne : **Sergey Ivanov** (63) · Dép. HCharente-Maritime : **Alexei Lebedev** (43) · Dép. HDeux-Sèvres : **KULIS** *(fiche tabulaire)* |
| **Maires** | HPoitiers : **Olena Hoffmann** (40) · HSaint-Maixent : **Dimitri Steiner** (51) |
| **Militaires** | Com 5e Secteur HPoitiers : **Erik Alvarez** (51) · Com 5e Brigade HAngoulême : **Anton Kellerov** (49) · Com Légion de Gendarmerie : **Baltzar Bold** (55) · DMD HVienne : **Nikolai Kravchenko** (49) · DMD HDeux-Sèvres : **CHAREYRON** (+ adj. DEPOIRE ; *« Dmitri Volkov » dans le doc densification*) · DMD HCharente-Maritime : **FLUXA** (+ LAPORTE ; *« Serge Lazare » idem*) |
| **Police / Gendarmerie** | Com Rég. Police : **Aleksandr Weiss** (50) · Police HVienne : **Katerina Vogelnyk** (40) · Police HDeux-Sèvres : **Serhiy Brandtsev** (43) · Gendarmeria Poitou : **Konrad Steinbeck** (51) · Gendarmerie HVienne : **Lukas Havrylenko** (44) · Gend. HDeux-Sèvres : **KERMOVANT** *(fiche tabulaire)* · ALC HCharente-Maritime : **Jannik Kostich** (41) · Resp. prison : **Viktor Kovalenko** (48) |
| **ONG / OI** | ICRC : **Boris Kalugin** (52) · UNOCHA : **Anastasia Sokolova** (38) · UNHCR (porte-parole) : **Marko Iliev** (38) · ARC : **Igor Mishin** (48) · Blue Shield : **Elena Petrovna** (47) · NGO ISC : **Alexandr Korolev** (55) · CultarNGO : **Viktor Ivanovitch** (42) · ACDA : **Viktor Steinbach** (45) · AISA : **Markus Voldyski** (48) |

Complément : `E20260317_...éléments modification bios.docx` = tableau de densification (objectifs/forces/faiblesses) pour Alvarez, DMD, ONG — déjà fusionné dans les fiches individuelles.

### C. Tampons & signatures HN — `Interlocuteurs   +Tampons HN.docx`

Document **visuel** (~0,8 Ko de texte, le reste = images) : **logos, tampons et blocs-signatures officiels** des autorités HN — préfectures HTOURS, HVIENNE, HCharente-Maritime, mairies HNIORT (bureau du maire + bureau communication J. Fabionneau), services régionaux de santé, signataires D. IVANOV (préfet HVienne), Viktor LANTANOV (MININT), Yann Lamoureux (bureau population HTours). Mail type `chh1@gouv.an`, téléphones en 05 49 78 XX XX (cohérent règle plages fictives zone 05).
**Usage :** réservoir d'authenticité pour tout **courrier officiel HN fictif** (en-têtes, tampons, signatures scannées) — à ouvrir manuellement pour copier les visuels. POC exercice : SITCEN/GREY CELL/Host nation.

---

## Données économiques

- PIB : $625,3 Mds
- Déficit : 24% | Dette : 46% PIB | Coût emprunt : 6,8%
- Chômage : 9% officiel + sous-emploi significatif
- Corruption : 119/180 (TI) — 50% recettes fiscales non perçues
- Agriculture : 1er producteur Skolkan (blé, orge, maïs)
- Énergie nucléaire : 71,7% de l'électricité (CNI)

---

## Figures et médias AURIGE 2BB — Rôle dans les injects

> Mis à jour le 26 mai 2026.

### Sture Pallesson — Utilisation dans AURIGE 2BB

**Rôle :** Président de la Dacie Romanie (DAC) — figure politique pro-OTAN centrale dans l'exercice.
**Apparaît dans :** TV4_Article_Pallesson ×4 (LO 2 — discours politique, leadership coalition)

⚠ Pallesson est un **chef d'État civil**, non militaire. Ne pas le confondre avec le CHOD VONG ou le CGS HUS. Ses déclarations dans les injects portent sur la légitimité de l'intervention OTAN et la souveraineté DAC — cible de dénigrement MER (LO 4).

**Règle éditoriale :** Tout inject MER ciblant Pallesson l'attaque sur sa crédibilité politique ou sa légitimité démocratique — jamais sur des aspects militaires (il n'est pas chef des armées en première ligne).

### Alexandre Youkachenko — Chef d'État adversaire/allié MER

**Rôle :** Président de la Ruthnia Bella — allié stratégique de Mercure dans AURIGE 2BB.
**Apparaît dans :** BCI_Article_Youkachenko · BCI_Article_Youkachenko_ConsSec
**Camp :** 🔴 Rouge — allié MER (LO 5 — escalade RB, nouveaux partenaires MER)
**Agent référent pour profil complet :** ANALYSTE MERCURE (section 6 de sa MEMOIRE)

### Médias AURIGE 2BB — camp bleu

| Média | Code | Rôle |
|---|---|---|
| TV4 International | TV4 | Média occidental — source principale pour injects pro-DAC/OTAN |
| **HEXAGONE** | HEX | **Média officiel français** — presse FR fictive dans l'exercice — HEX_Article_Rutte |

**Note HEXAGONE :** Représente la presse française dans le scénario AURIGE 2BB. Positionné côté coalition/DR. À utiliser pour tout inject de presse française officielle.

---

## 📘 COUNTRYBOOK ARNLAND — COMPLÉMENT INTÉGRAL (2026-05-31, ingestion 100 %)

> Vérification du 2026-05-31 : la mémoire existante n'était qu'une **synthèse opérationnelle**. Ci-dessous **toutes** les sections du countrybook (A→F + Annexe Personalities) pour faire d'ANALYSTE_ARN un **expert référent complet** (tous usages, pas seulement ILI). Source : `Orion 26 - Arnland.pdf` / `Orion 26 - Arnland (1).docx`.

### A. POLITIQUE — détail

**Géographie :** **508 371 km²**, capitale **HPARIS**, borde **Bothnia (N)**, **Mercure (E)**, **Framland (S)** ; littoral **3 312 km** (Atlantique + Méditerranée). 4 zones climatiques : océanique (ouest), continental (centre/est), méditerranéen (sud-est), montagne (>600-800 m). Point culminant **Mont Blanc 4 810 m** (frontière est avec Mercure). **12 Läns** (régions) → départements. = **France fictive** (Bretagne, Normandie, Champagne, Bourgogne, Alsace, Provence-Côte d'Azur, Pyrénées, Alpes…). Pop : voir § D (**36,2 M**).

**Histoire :** Empire Skolkan (14e-19e s. ; comprenait Arnland + Bothnia + Framland + Mercure). **Indépendance déc. 1917** (⚠ **l'Aquitaine/Bordeaux reste possession MER** — forte diaspora). Roi **Alexandre Ier** (« Optimistic Alexander ») jusqu'à l'**abolition de la monarchie en 1931** (coup → État communiste). **Chute du communisme 1991** → transition démocratie + économie de marché.

**Système politique :** République ; **Alltinget 132 sièges** (FPTP, 4 ans). **High Council of Justice** (15 membres ; Président de la République = Chair). **Cour suprême** (Chief Justice + 17 juges ; 3 panels : constitutionnel/civil/pénal). 12 **Cours d'appel** (1 par Län) + Cours de 1ʳᵉ instance. **15 ministères**, **12 Läns** administrés par **Landsting** (conseils régionaux) sous **Landshövding** (gouverneurs). Seuls **Aff. étrangères / Dév. national / Défense / Justice** sont purement nationaux.

**Relations extérieures — ⚠ POINT MAJEUR :** Arnland a **QUITTÉ le SCO** (retrait annoncé à HPARIS déc. 2014, ratifié **fév. 2016**) → **rapprochement EU/OTAN** (membre **EAPC 2016**, programme **MAP**). Jamais membre du **SSTO**. Adhère SIA/SFTA (1973), entré au SCO en 1947 puis sorti. Friction MER : MER offre la **double-nationalité** aux ancêtres mercuriens (2016) → Arnland **refuse la double-nationalité dès le 01/07/2018** (perte des droits sociaux/pension). Olamao loue publiquement le **gouverneur de PACA** (qualifié de guerre hybride). **UN Partnership Framework 2021-2026** (Country Team à HPARIS).

**Partis (6, pas 2) :**
| Parti | Ligne | Président / Porte-parole |
|---|---|---|
| **APP** Arnland Prosperity Party | Centre-droit (dominant depuis 1991, pro-Ouest, base NO) | **Oleg Dimitrov** / Irina Zhivković |
| **ASP** Arnland Socialist Party | Gauche (ex-communistes, pro-SCO/MER) | **Vladislav Marinov** / Katarina Durova *(ex-PM puis Président **Kasper Bro** 2010)* |
| **ARP** Arnland Republican Party | Droite (appui ponctuel à l'APP) | Mikhail Sidorov / Radmila Petrović |
| **SDP** Social Democratic Party | Centre-gauche | Bojan Karadzic / Natalya Kostova |
| **ALP** Arnland Liberal Party | Centre (soutient l'APP minoritaire actuel) | Luka Pavlenko / Anya Savchenko |
| **ACP** Arnland Communist Party | Communiste | Ivan Volkov |

**Politique intérieure / ordre public :** Min. Intérieur (law enforcement, pénal, frontières, pompiers/ambulances). **ALC** (Arnland Län Constabulary) = police **décentralisée par Län, sous les gouverneurs, peu formée, corrompue, pas de QG national**. **APS** (système pénitentiaire) sous-financé, corruption, prisons surpeuplées. **ACDA** (Civil Defence Agency) — bascule en cas d'urgence déclarée par le PM.

### B. MILITAIRE — ORBAT complet

**Structure générale :** **ADF** (Active Defence Force) = **8 brigades interarmes** + brigades CS/CSS (National Force Pool) + **Ballistic Missile Force** + **1 brigade SOF**. **SDF** (Standby Defence Force) = **12 brigades régionales de réserve** (mobilisation). Marine conséquente, **petite Air Force** (appui sol). Effectifs : **ADF ~129 000 / SDF ~200 000** (mob).
**État des forces :** équipement **vétuste/mal entretenu**, conscrits mal formés/motivés (désertions, certaines vers MER), **mais** officiers & sous-off. juniors compétents. **Commandement surcompliqué.**
**Chaîne :** Président = CINC → MoD → **CHOD** → Terre/Marine/Air. Organisations quasi-indépendantes : **DSOF** (SOF), **DGPL** (procurement/log), **DMISS** (rens. & sécurité — quasi-autonome). **DSDF** (réserve, même rang que le CGS, QG propre). Ballistic Missile Force → CHOD. War College autonome. *(Chefs nommés déjà en mémoire : CHOD VONG, CGS HUS, Marine BYSTROM, Air FRIES, SOF GRADHOLM, BMF ARNE.)*

**7 Secteurs militaires de défense & sécurité (Land Forces ADF) :**
| Secteur (HQ) | Brigade(s) | Région couverte |
|---|---|---|
| **Capital** (HPARIS) | **101e Bde Inf Motorisée = Garde Présidentielle** (cérémonie + réserve stratégique) | Île-de-France |
| **1er** (HLille) | 1 Bde Inf Mécanisée | Hauts-de-France |
| **2e** (HTroyes) ⭐ | 1 **Bde de Reconnaissance** | **Grand Est + Bourgogne-Franche-Comté** *(zone des exercices AURIGE/ORION)* |
| **3e** (HLyon) | 1 Bde Inf Motorisée | Auvergne-Rhône-Alpes |
| **4e** (HTOULOUSE) | 1 Bde Inf Mécanisée *(1ère à intégrer l'assistance bilatérale)* | Occitanie + PACA |
| **5e** (HPOITIERS) | 1 Bde de Chars | Poitou-Charente |
| **6e** (HRennes) | 1 Bde de Chars + 1 Bde Inf Motorisée | Bretagne / Centre-Val de Loire / Normandie / Pays de Loire |
| **National Force Pool** (HPARIS) | 1 Bde Arty lourde, 2 Bde Génie, 2 Bde Transmissions, 2 Bde CSS, 1 Bde Médicale | national |

**SDF (12 bdes régionales) :** sous les gouverneurs en paix → GSHQ en guerre ; **éclectiques** (certaines = coquilles vides). ⭐ **Grand Est + PACA : brigades fortes, en FUSION avec la milice TANTALE depuis 2014** ; TAN active en **Auvergne (IVO Hclermont-Ferrand)**, Centre-Val de Loire, financée/instruite par MER, caches d'armes, infiltre les SDF locales.
**Marine :** classes **Kashin-mod, Jianghu-III, Nanuchka, Parchim** ; AEW/ASW/SAR ; bases **HBrest / HCherbourg / HToulon**.
**Air :** ~110 jets — **Mirage F1, MiG-21, Su-25** ; SAM **Crotale, Mistral, SA-3/SA-5** ; rôle = appui aux forces terrestres.

### C. ÉCONOMIE — détail
PIB **625,3 Mds $**, /hab **~16 526 $** (≈ 2/3 des grandes éco. EU) ; croissance **-2,75 % (2020)**, puis **-2,2 % (2022)** et **-2,8 % (2024)**. **Déficit jusqu'à 29,5 % du PIB (2022)** → austérité (→24,5 %). Dette/inflation/chômage > moyenne EU ; **chômage ~9 %**. **Crise financière 2023** (note dégradée à **BB**) ; **prêt FMI-SCO de 47 Mds $ (2020)** contre austérité. Public = 30 % du PIB. **Tax/PIB 35,9 %**. Exports **45 Mds $** (machines, optique, électronique) ; imports **56 Mds $** (pétrole brut, agri, métaux) → **balance négative**. Nucléaire **72 %** de l'énergie. **Charbon Grand Est** (MER y investit lourdement ; exporté vers MER). Pêche **11 Mds $** (3e marché Skolkan). Forêt ~5 % du PIB. **Tourisme 8,5 % du PIB**. Aide internationale 3,3 % du PIB. Syndicats puissants (grèves anti-austérité). Héritage communiste : industrialisation intensive, urbanisation 35 %(1952)→60 %(1991), agriculture collectivisée puis privatisée (1991).

### D. SOCIÉTÉ — détail
**Population 36,2 M** ; ethniquement homogène (Arnish dominant) ; langue **arnish** (+ **mercurien** au NE et au sud ; français/anglais 2ᵉ langue). Ménage moyen 2,6 pers ; solo 18 % ; nucléaire 34 %. Natalité **8,7/1000**, mortalité **13,17/1000**, croissance **-0,44 %**. Espérance de vie **75,5 H / 80,1 F** (3 ans sous l'UE) ; 25 % fumeurs ; décès = cardiopathie ischémique, AVC, Alzheimer, cancer du poumon. Pop active **22,2 M (58,7 %)** ; chômage 9 % (+ sous-emploi). Salaire min **1 689 $/mois** ; semaine 36-40 h ; 24 j congés. ⚠ **Paradoxe social :** pays au revenu type tiers-monde **mais population éduquée/cultivée** ; classe moyenne réelle 5-15 %, mais ~50 % s'auto-déclarent classe moyenne. Urbain **62 %**, densité 70,7/km². **HPARIS 2,14 M** (aire urbaine >5 M), **HMARSEILLE 794 k** (2e ville). ~1/3 rural.
⭐ **Diaspora mercurienne : 8 % (3,4 M)** — Grand Est (~1,7 M), Occitanie+PACA (~1,1 M) ; surtout urbaine ; **HMARSEILLE 16 % mercuriens**. Citoyenneté facile sous le communisme (dual permis), **durcie après 1991** (tests d'arnish ; beaucoup de Mercuriens sans citoyenneté). Sondage 2020 (NGO « Minority Rights Empowerment Arnland », 40 k répondants) : mieux intégrés au N/O ; **jeunes hommes 20-30 ans se sentent discriminés + veulent le soutien de MER** ; discrimination systémique > interpersonnelle. **Olamao très populaire dans la diaspora** (depuis 2014). Éducation/santé : couverte ; santé sous moyenne OCDE.

### E. INFORMATION
*(Déjà approfondi — voir § « Environnement informationnel ».)* Compléments : régulateur **National Council for Media Affairs** (sous Min. Travaux publics/Transports/Télécoms/IT) ; **Min. de l'Information et des Communications** (sécurité de l'info, Information Classification Act) ; indicatif **+463** ; câbles sous-marins via **HMARSEILLE**.

### F. INFRASTRUCTURE
**National Infrastructure Plan** (Min. Dév. national, aligné UE), 3 piliers : Green Deal/résilience · économie numérique · modernisation. Position : double façade **Atlantique + Méditerranée**.
- **Numérique :** Min. I&C aligné « Europe fit for the Digital Age » ; cyber via **ENISA** + **NATO CCDCOE (Estonie)** ; **DESI : 29e/28** (dernier) ; **5G Dushman** (contrat 2028, en examen sécuritaire AISA) ; passerelles **HSete / HRennes / HSt-Valery-en-Caux** ; **HLyon & HPARIS** vitaux ; **Arnland Telephone Network** (monopole fixe jusqu'à 2027) ; fibre quasi-complète.
- **Énergie :** réseau régional (>40 interconnexions frontalières). Électricité : **EDA** (Energy Distribution Arnland, privé-État lié au **nucléaire Dushman**) ; **nucléaire 71,7 % / renouvelable 21,3 % / fossile 7 %** ; 100 000 km de lignes, continuité 98 % ; 22 hubs de stockage (+68 prévus). ⚠ **Gaz : 63 % importé via le pipeline central Skolkan contrôlé par Bothnia + Mercure** + LNG 35 % (terminaux **HDunkerque / HMontoir-de-Bretagne / HFos-sur-Mer**) ; conso 40 Mds m³, 11 M consommateurs. Hydro : barrages **HSerre-Ponçon, HEguzon, HGrand-Maison, HTignes, HMareges** (CNI). Éolien : 3 fermes (HChampagne, HPyrénées-Orientales, HBretagne). Solaire : **HMerle-Sud** (vallée de la Gironne, nord HMARSEILLE).
- **Déchets :** Min. Environnement + **Arnland Environment Authority**.

### Annexe « Personalities » — roster nominatif
**Cabinet (annexe) :** Mira Janković (Aff. étrangères) · Boris Novak (Dév. national/international) · Andrei Belov (Défense) · Elena Vasilieva (Justice) · Dmitri Radulov (Intérieur) · Natalya Pavlenko (Environnement) · Viktor Dragunov (Finances) · Irina Petrova (Santé) · Anastasia Kravtsova (Culture/Jeunesse/Sports) · Ivan Baranov (Agriculture/Alimentation) · Zoran Filipović (Transport) · Milena Zhukova (Éducation/Recherche) · Sergei Nikitin (Travail/Protection sociale) · Tatiana Bodrova (Économie/Commerce) · Alexei Morozov (Technologies/Numérisation).
**Justice :** Président Cour suprême **Stanislav Vuković** · Juge constit. **Mariya Stepanenko** · Juge pénal **Nikolai Zoric** · Avocate générale **Ekaterina Milova** · Avocat de la défense célèbre **Yuri Antonov**.

> ⚠ **Note tête de l'État :** le countrybook (annexe) liste les **chefs de partis** (APP : Oleg Dimitrov). **« Président Sture Pallesson »** est la tête d'État jouée dans les exercices (ORION/AURIGE 2BB en « Dacie Romanie ») — figure scénario, à distinguer du roster structurel du countrybook.

> ✅ **Countrybook Arnland ingéré à 100 %** (A→F + Annexe Personalities). ANALYSTE_ARN à parité avec ANALYSTE (Mercure) et ANALYSTE_BOT (Bothnia).

---

## Tensions actives — exploitables dans les scénarios

| Tension | Détail | Exploitable pour |
|---|---|---|
| **Diaspora mercurienne** | 8% pop. (3,4M) — Grand Est (1,7M), PACA/Occitanie (1,1M), HMARSEILLE (16%) | Justification R2P d'Olamao, recrutement TANTALE, tensions locales |
| **Dépendance gazière** | 63% via pipeline Bothnia/Mercure | Pression économique, chantage énergétique |
| **TANTALE** | Milice proxy de Mercure sur sol DR/Arnland | Déstabilisation intérieure, incidents armés fictifs |
| **N.O.M** | Groupe fictif anti-OTAN, couverture écologique | Propagande, attentats fictifs, tracts |
| **Corruption systémique** | 119/180 TI, judiciaire dysfonctionnel | Crédibilité réduite des institutions, fragilité narrative |
| **Polarisation ASP/APP** | ASP amplifié par Mercure | Désinformation interne, voix dissonantes |
| **Jeunes Mercuriens 20-30** | Groupe le plus radicalisé | Recrutement TANTALE/N.O.M, incidents locaux |

---

## Points infrastructure critiques

- **Pipeline gazier Bothnia/Mercure** : vulnérabilité énergétique, 63% du gaz
- **HPARIS / HLyon** : nœuds numériques critiques
- **Garonne → HBordeaux (port mercurien)** : friction commerciale/militaire latente
- **Barrages hydroélectriques** : CNI
- **HMARSEILLE** : 3e port Méditerranée, base navale, 16% diaspora mercurienne
- **5G Dushman** : contrat en examen sécuritaire 2026 → point de friction narratif possible

---

## Vocabulaire narratif (cohérence discours)

- "invasion" — jamais "opération" pour qualifier l'action mercurienne
- "sovereignty" / "notre souveraineté"
- "freedom" / "we will not surrender"
- "our citizens" — jamais "compatriots" (terme exclusivement mercurien)
- "international law" / "international community"
- Ton : urgent, digne, émotion contrôlée

---

## Apprentissages par exercice

| Date | Exercice | Apprentissage |
|---|---|---|
| 2026-05-23 | AURIGE 2BB (Guillaume) | Arnland → "Dacie Romanie (DR)". Pallesson = Président DR. TANTALE = bras armé intérieur mercurien. |
| — | À compléter | — |
