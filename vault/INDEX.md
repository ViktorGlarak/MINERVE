# 🗂️ INDEX — Vault atomique MINERVE

> ⚙️ **Fichier généré** par `_generer_index.py` — ne pas éditer à la main.
> Registre des notes atomiques (couche méta « qui lie, ne copie jamais »).
> Le détail vit dans les fichiers `source:` ; ces notes pointent, elles ne dupliquent pas.
> Carte humaine du système : [MINERVE_HOME](../MINERVE_HOME.md) · Source de vérité : [CLAUDE.md](../CLAUDE.md)

**379 notes** · généré le 2026-06-18

## ⭐ Tier 1 — à charger en priorité

| ID | Titre | Type | relevantFor |
|---|---|---|---|
| [ARCH-001](architecture/ARCH-001.md) | Vault MINERVE — source de vérité unique | architecture | systeme, tous |
| [ARCH-004](architecture/ARCH-004.md) | Registre des agents (renvoi) | architecture | systeme, noyau |
| [DECISION-001](decisions/DECISION-001.md) | Architecture 3 dossiers MASTAURIGE | decision | mastaurige, exercices |
| [ENT-arnland](entities/pays/ENT-arnland.md) | Arnland (Dacie Romanie — DAC/DR) | entity | arnland, exercices, ili |
| [ENT-bothnia](entities/pays/ENT-bothnia.md) | Bothnia (Republic of Bothnia — BOT) | entity | bothnia, exercices, ili |
| [ENT-mercure](entities/pays/ENT-mercure.md) | République de Mercure (MER) | entity | mercure, exercices, ili |
| [LESSON-001](lessons/LESSON-001.md) | Anti-divergence camp — propriétaire unique | lesson | mastaurige, analystes, exercices |
| [LESSON-008](lessons/LESSON-008.md) | Lancer VERIFIER en fin de session | lesson | mastaurige, qualite |
| [PROJ-AURIGE-7BB](projects/AURIGE-7BB.md) | AURIGE 7BB / MINOTAURE 26 | project | exercices, minautore |
| [PROJ-MASTAURIGE](projects/MASTAURIGE.md) | MASTAURIGE — outillage production média | project | mastaurige |
| [PROJ-MINERVE](projects/MINERVE-systeme.md) | MINERVE — système multi-agents | project | systeme, noyau |
| [TOOL-002](tools/TOOL-002.md) | verifier_mastaurige.py (contrôles A-I) | tool | mastaurige, qualite |

## 🔧 Décisions

| ID | Titre | Tier | Source (vérité) | Liens |
|---|---|---|---|---|
| [DECISION-001](decisions/DECISION-001.md) | Architecture 3 dossiers MASTAURIGE | 1 | [`MEMOIRE.md`](../../MASTAURIGE/MEMOIRE.md) | [[DECISION-002]] [[TOOL-003]] [[TOOL-004]] [[TOOL-005]] [[ARCH-003]] |
| [DECISION-002](decisions/DECISION-002.md) | Pipeline « inject as code » | 2 | [`MEMOIRE.md`](../../MASTAURIGE/MEMOIRE.md) | [[DECISION-003]] [[TOOL-007]] [[DECISION-004]] |
| [DECISION-003](decisions/DECISION-003.md) | lo_config.js — source unique séries→LO | 2 | [`MEMOIRE.md`](../../MASTAURIGE/MEMOIRE.md) | [[DECISION-004]] [[LESSON-001]] [[ARCH-001]] |
| [DECISION-004](decisions/DECISION-004.md) | MELMIL v0.2 — matrice par LO, cards 2 couleurs | 2 | [`MEMOIRE.md`](../../MASTAURIGE/MEMOIRE.md) | [[DECISION-003]] [[ARCH-002]] |
| [DECISION-005](decisions/DECISION-005.md) | Format codes incident 2 ou 3 chiffres | 3 | [`MEMOIRE.md`](../../MASTAURIGE/MEMOIRE.md) | [[DECISION-002]] |
| [DECISION-006](decisions/DECISION-006.md) | Trombino — pages A3 auto + bande bio + cache-buster | 2 | [`MEMOIRE.md`](../../MASTAURIGE/MEMOIRE.md) | [[TOOL-001]] [[LESSON-002]] |

## 🛠️ Outils

| ID | Titre | Tier | Source (vérité) | Liens |
|---|---|---|---|---|
| [TOOL-001](tools/TOOL-001.md) | generer_trombino_bios.py | 2 | [`MEMOIRE.md`](../../MASTAURIGE/MEMOIRE.md) | [[DECISION-006]] [[LESSON-002]] [[LESSON-007]] |
| [TOOL-002](tools/TOOL-002.md) | verifier_mastaurige.py (contrôles A-I) | 1 | [`MEMOIRE.md`](../../MASTAURIGE/MEMOIRE.md) | [[LESSON-008]] [[LESSON-001]] |
| [TOOL-003](tools/TOOL-003.md) | GENERER_VIERGE.py | 2 | [`MEMOIRE.md`](../../MASTAURIGE/MEMOIRE.md) | [[DECISION-001]] [[TOOL-006]] |
| [TOOL-004](tools/TOOL-004.md) | GENERER_KIT_JOUEURS.py | 2 | [`MEMOIRE.md`](../../MASTAURIGE/MEMOIRE.md) | [[DECISION-001]] [[TOOL-005]] |
| [TOOL-005](tools/TOOL-005.md) | Console MASTER (fusion / renumérotation / actus) | 2 | [`MEMOIRE.md`](../../MASTAURIGE/MEMOIRE.md) | [[DECISION-001]] [[TOOL-004]] |
| [TOOL-006](tools/TOOL-006.md) | CONFIGURER_EXERCICE.py + exercice_config.json | 2 | [`MEMOIRE.md`](../../MASTAURIGE/MEMOIRE.md) | [[TOOL-003]] [[ARCH-003]] |
| [TOOL-007](tools/TOOL-007.md) | generer_injects.py | 2 | [`MEMOIRE.md`](../../MASTAURIGE/MEMOIRE.md) | [[DECISION-002]] [[DECISION-003]] |
| [TOOL-008](tools/TOOL-008.md) | OmniVoice TTS (Voice Clone / Voice Design) | 2 | [`PARAMETRES_OMNIVOICE.md`](../../VOIX/PARAMETRES_OMNIVOICE.md) | [[ARCH-006]] [[LESSON-010]] |
| [TOOL-009](tools/TOOL-009.md) | LTX 2.3 i2v/ia2v (ComfyUI) | 2 | [`PARAMETRES_LTX.md`](../../CINEASTE/PARAMETRES_LTX.md) | [[ARCH-006]] [[LESSON-011]] |
| [TOOL-010](tools/TOOL-010.md) | Stack image (Firefly / Flow / Gemini) | 2 | [`PROMPTS_TYPES.md`](../../IMAGIER/PROMPTS_TYPES.md) | [[ARCH-006]] [[LESSON-009]] |
| [TOOL-011](tools/TOOL-011.md) | generer_melmil.py (import MELMIL unifié GESTIM + JEMM) | 2 | [`MEMOIRE.md`](../../MASTAURIGE/MEMOIRE.md) | [[PROJ-AURIGE-7BB]] [[DECISION-002]] |

## 📚 Leçons

| ID | Titre | Tier | Source (vérité) | Liens |
|---|---|---|---|---|
| [LESSON-001](lessons/LESSON-001.md) | Anti-divergence camp — propriétaire unique | 1 | [`CLAUDE.md`](../../CLAUDE.md) | [[ARCH-001]] [[TOOL-002]] [[DECISION-003]] |
| [LESSON-002](lessons/LESSON-002.md) | Espace insécable dans les labels → fusion de sections | 2 | [`MEMOIRE.md`](../../MASTAURIGE/MEMOIRE.md) | [[TOOL-001]] [[LESSON-007]] |
| [LESSON-003](lessons/LESSON-003.md) | Pas de liens croisés vers articles futurs | 2 | [`MEMOIRE.md`](../../SCENARISTE/MEMOIRE.md) | [[LESSON-004]] |
| [LESSON-004](lessons/LESSON-004.md) | Règle GET (Grand East Territory) | 2 | [`CLAUDE.md`](../../CLAUDE.md) | [[LESSON-005]] |
| [LESSON-005](lessons/LESSON-005.md) | Numéros de téléphone fictifs | 3 | [`DOSSIER_POSTE.md`](../../SYSTEME/DOSSIER_POSTE.md) | [[LESSON-004]] |
| [LESSON-006](lessons/LESSON-006.md) | Langue du tweet = langue de l'avatar | 2 | [`MEMOIRE.md`](../../MASTAURIGE/MEMOIRE.md) | [[LESSON-001]] |
| [LESSON-007](lessons/LESSON-007.md) | Bloc parseur non borné → record poubelle | 2 | [`MEMOIRE.md`](../../MASTAURIGE/MEMOIRE.md) | [[TOOL-001]] [[LESSON-002]] |
| [LESSON-008](lessons/LESSON-008.md) | Lancer VERIFIER en fin de session | 1 | [`MEMOIRE.md`](../../MASTAURIGE/MEMOIRE.md) | [[TOOL-002]] [[LESSON-001]] |
| [LESSON-009](lessons/LESSON-009.md) | Prompts image — scènes civiles sans drapeaux + texte verbatim | 2 | [`DOSSIER_POSTE.md`](../../SYSTEME/DOSSIER_POSTE.md) | [[TOOL-010]] [[ARCH-006]] |
| [LESSON-010](lessons/LESSON-010.md) | Texte TTS — préfixe H non prononcé, sigles lettre par lettre | 2 | [`DOSSIER_POSTE.md`](../../SYSTEME/DOSSIER_POSTE.md) | [[TOOL-008]] [[ARCH-006]] |
| [LESSON-011](lessons/LESSON-011.md) | Prompts LTX — paragraphe mouvement, ia2v synchro labiale | 2 | [`DOSSIER_POSTE.md`](../../SYSTEME/DOSSIER_POSTE.md) | [[TOOL-009]] [[ARCH-006]] |
| [LESSON-012](lessons/LESSON-012.md) | Auditer le vault contre les countbooks SOURCES, pas seulement les mémoires | 2 | [`CLAUDE.md`](../../CLAUDE.md) | [[LESSON-001]] [[ENT-karpovitch]] [[ENT-bothnia]] |
| [LESSON-013](lessons/LESSON-013.md) | Serveur HTTP Python local lent → double pile IPv6 + Nagle + cache | 2 | [`MEMOIRE.md`](../../MASTAURIGE/MEMOIRE.md) | [[ARCH-008]] |

## 🏛️ Architecture

| ID | Titre | Tier | Source (vérité) | Liens |
|---|---|---|---|---|
| [ARCH-001](architecture/ARCH-001.md) | Vault MINERVE — source de vérité unique | 1 | [`CLAUDE.md`](../../CLAUDE.md) | [[LESSON-001]] [[ARCH-004]] |
| [ARCH-002](architecture/ARCH-002.md) | Routage par modèle Ollama / co-résidence VRAM | 2 | [`ROUTAGE.md`](../../SYSTEME/ROUTAGE.md) | [[ARCH-004]] |
| [ARCH-003](architecture/ARCH-003.md) | Structure des exercices AURIGE | 2 | [`aurige.md`](../../SYSTEME/PROMPTS/aurige.md) | [[TOOL-006]] [[DECISION-001]] |
| [ARCH-004](architecture/ARCH-004.md) | Registre des agents (renvoi) | 1 | [`CLAUDE.md`](../../CLAUDE.md) | [[ARCH-001]] [[ARCH-002]] |
| [ARCH-005](architecture/ARCH-005.md) | Boucle QC — NOYAU évalue chaque réponse agent | 2 | [`QC.md`](../../SYSTEME/QC.md) | [[ARCH-001]] [[ARCH-002]] [[PROJ-MINERVE]] |
| [ARCH-006](architecture/ARCH-006.md) | Pipeline de production média (image → vidéo → voix → montage) | 2 | [`DOSSIER_POSTE.md`](../../SYSTEME/DOSSIER_POSTE.md) | [[TOOL-008]] [[TOOL-009]] [[TOOL-010]] [[LESSON-009]] [[LESSON-010]] [[LESSON-011]] [[PROJ-PROD-MEDIA]] |
| [ARCH-007](architecture/ARCH-007.md) | Roadmap technique MINERVE (RAG · CONVERGENCE · orchestrateur autonome) | 3 | [`CONFIG.md`](../../SYSTEME/CONFIG.md) | [[ARCH-001]] [[ARCH-002]] [[PROJ-MINERVE]] |
| [ARCH-008](architecture/ARCH-008.md) | MASTAURIGE collaboratif temps réel (serveur central + collab.js) | 2 | [`MEMOIRE.md`](../../MASTAURIGE/MEMOIRE.md) | [[PROJ-MASTAURIGE]] [[DECISION-001]] [[LESSON-013]] |

## 🗂️ Projets (canvas)

| ID | Titre | Tier | Source (vérité) | Liens |
|---|---|---|---|---|
| [PROJ-AURIGE-7BB](projects/AURIGE-7BB.md) | AURIGE 7BB / MINOTAURE 26 | 1 | [`MEMOIRE.md`](../../MINAUTORE/MEMOIRE.md) | [[ARCH-003]] [[DECISION-001]] [[TOOL-006]] |
| [PROJ-MASTAURIGE](projects/MASTAURIGE.md) | MASTAURIGE — outillage production média | 1 | [`MEMOIRE.md`](../../MASTAURIGE/MEMOIRE.md) | [[DECISION-001]] [[DECISION-002]] [[DECISION-004]] [[DECISION-006]] [[TOOL-001]] [[TOOL-002]] [[TOOL-005]] [[LESSON-001]] [[LESSON-002]] [[LESSON-007]] |
| [PROJ-MINERVE](projects/MINERVE-systeme.md) | MINERVE — système multi-agents | 1 | [`CLAUDE.md`](../../CLAUDE.md) | [[ARCH-001]] [[ARCH-002]] [[ARCH-004]] [[ARCH-005]] [[ARCH-007]] [[PROJ-PROD-MEDIA]] [[PROJ-MASTAURIGE]] [[PROJ-AURIGE-7BB]] |
| [PROJ-PROD-MEDIA](projects/PROD-MEDIA.md) | Production média (image · vidéo · voix) | 2 | [`DOSSIER_POSTE.md`](../../SYSTEME/DOSSIER_POSTE.md) | [[ARCH-006]] [[TOOL-008]] [[TOOL-009]] [[TOOL-010]] [[LESSON-009]] [[LESSON-010]] [[LESSON-011]] |

## 🤖 Agents (canvas générés)

| ID | Titre | Tier | Source (vérité) | Liens |
|---|---|---|---|---|
| [AGENT-ANALYSTE-ARN](agents/AGENT-ANALYSTE-ARN.md) | ANALYSTE_ARN | 2 | [`MEMOIRE.md`](../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-alvarez]] [[ENT-andreev-milan]] [[ENT-antonov]] [[ENT-arne]] [[ENT-arnland]] [[ENT-baranov]] [[ENT-belov]] [[ENT-birkmann]] [[ENT-blazic]] [[ENT-bodrova]] [[ENT-bold]] [[ENT-borchenko]] [[ENT-borovic]] [[ENT-brandtsev]] [[ENT-brenner]] [[ENT-bystrom]] [[ENT-chareyron]] [[ENT-depoire]] [[ENT-dimitrov]] [[ENT-djobovic]] [[ENT-dragunov]] [[ENT-durova]] [[ENT-filipovic]] [[ENT-fischer]] [[ENT-fluxa]] [[ENT-fries]] [[ENT-gervais]] [[ENT-gradholm-arn]] [[ENT-hartmann]] [[ENT-havrylenko]] [[ENT-hoffmann]] [[ENT-hus]] [[ENT-iliev]] [[ENT-ivanov-sergey]] [[ENT-ivanovitch]] [[ENT-jaksic]] [[ENT-jankovic]] [[ENT-kalugin]] [[ENT-karadzic]] [[ENT-karlson-erik]] [[ENT-karrlson]] [[ENT-kellerov]] [[ENT-kermovant]] [[ENT-korolev]] [[ENT-kostich]] [[ENT-kostova]] [[ENT-kovalenko-viktor]] [[ENT-kovalev]] [[ENT-krauss]] [[ENT-kravchenko]] [[ENT-kravtsova]] [[ENT-kulis]] [[ENT-lang]] [[ENT-laporte]] [[ENT-lebedev]] [[ENT-malenko]] [[ENT-marinov]] [[ENT-milenkovic]] [[ENT-milova]] [[ENT-mishin]] [[ENT-morozov]] [[ENT-nikitin]] [[ENT-novak]] [[ENT-novik-lidija]] [[ENT-pallesson]] [[ENT-pavlenko-luka]] [[ENT-pavlenko-natalya]] [[ENT-petrova-irina]] [[ENT-petrovic-radmila]] [[ENT-petrovna]] [[ENT-radojevic]] [[ENT-radulov]] [[ENT-savchenko]] [[ENT-savchenko-anya]] [[ENT-schmidt]] [[ENT-sidorov]] [[ENT-sokolova-anastasia]] [[ENT-stanev]] [[ENT-steinbach-viktor]] [[ENT-steinbeck]] [[ENT-steiner]] [[ENT-stepanenko]] [[ENT-thiebaut]] [[ENT-vasilieva]] [[ENT-velkova]] [[ENT-vogelnyk]] [[ENT-voldyski]] [[ENT-volkonsky]] [[ENT-volkov-ivan]] [[ENT-voloshyn]] [[ENT-vong]] [[ENT-vrenko]] [[ENT-vukovic]] [[ENT-weber]] [[ENT-weiss]] [[ENT-zhivkovic]] [[ENT-zhukova]] [[ENT-zoric-kristina]] [[ENT-zoric-nikolai]] [[REF-arnland-economie]] [[REF-arnland-infrastructure]] [[REF-arnland-medias]] [[REF-arnland-militaire]] [[REF-arnland-politique]] [[REF-arnland-societe]] [[REF-arnland-strategie]] |
| [AGENT-ANALYSTE-BOT](agents/AGENT-ANALYSTE-BOT.md) | ANALYSTE_BOT | 2 | [`MEMOIRE.md`](../../ANALYSTE/BOTHNIA/MEMOIRE.md) | [[ENT-adam]] [[ENT-amin]] [[ENT-anders-lorentz]] [[ENT-andersen-line]] [[ENT-astapenka]] [[ENT-baradzin]] [[ENT-boerck]] [[ENT-bohler]] [[ENT-bothnia]] [[ENT-breesson]] [[ENT-brrouette]] [[ENT-bruske]] [[ENT-bryl]] [[ENT-buerger]] [[ENT-declercq]] [[ENT-dewaele]] [[ENT-diniz]] [[ENT-dubrouski]] [[ENT-dziadok-maryia]] [[ENT-dziadok-natallia]] [[ENT-eklund]] [[ENT-erik-petra]] [[ENT-gradholm]] [[ENT-groop]] [[ENT-hansen]] [[ENT-holm]] [[ENT-horby]] [[ENT-hurski]] [[ENT-ivanouski]] [[ENT-jansen]] [[ENT-jensen-niels]] [[ENT-kalenik]] [[ENT-karpovitch]] [[ENT-kavalenka]] [[ENT-koho]] [[ENT-koivisto]] [[ENT-kosmannen]] [[ENT-kramer]] [[ENT-lapitski]] [[ENT-lindquist]] [[ENT-madsen-freja]] [[ENT-madsen-ida]] [[ENT-maes]] [[ENT-makarevich]] [[ENT-malmsten]] [[ENT-marozau]] [[ENT-meyer]] [[ENT-muller-aiko]] [[ENT-nielsen-kasper]] [[ENT-novik]] [[ENT-nyberg]] [[ENT-palmquetil]] [[ENT-pavlenko-nikolai]] [[ENT-pedersen-anders]] [[ENT-peters]] [[ENT-petrovic]] [[ENT-pierrinen]] [[ENT-radzivil]] [[ENT-radzivil-aliaksandr]] [[ENT-rasmussen]] [[ENT-richter]] [[ENT-roland]] [[ENT-rosendaal]] [[ENT-rosenquist]] [[ENT-rylander]] [[ENT-rynkevich]] [[ENT-saniki]] [[ENT-schmit]] [[ENT-shauchenka]] [[ENT-shymanovich]] [[ENT-sokal]] [[ENT-sokolova-natalia]] [[ENT-strutz]] [[ENT-thinnes]] [[ENT-thulin]] [[ENT-tikhanov]] [[ENT-tsikhanouski]] [[ENT-turchyn]] [[ENT-uhlmensch]] [[ENT-vasilevich]] [[ENT-viklund]] [[ENT-weber-dorit]] [[ENT-zeelen]] [[ENT-zhuk]] [[REF-bothnia-economie]] [[REF-bothnia-infrastructure]] [[REF-bothnia-medias]] [[REF-bothnia-militaire]] [[REF-bothnia-politique]] [[REF-bothnia-societe]] [[REF-bothnia-strategie]] |
| [AGENT-ANALYSTE-MERCURE](agents/AGENT-ANALYSTE-MERCURE.md) | ANALYSTE (Mercure) | 2 | [`MEMOIRE.md`](../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-abdoulaiev]] [[ENT-andreev-boris]] [[ENT-antonova]] [[ENT-auer-georg]] [[ENT-auer-tobias]] [[ENT-bauer-yuri]] [[ENT-baumgartner]] [[ENT-bielski]] [[ENT-bogdanov]] [[ENT-caruso]] [[ENT-conti]] [[ENT-denisov]] [[ENT-druey]] [[ENT-dvornikov]] [[ENT-ebner]] [[ENT-erickson]] [[ENT-franke]] [[ENT-fredotov]] [[ENT-frolov]] [[ENT-fuchs]] [[ENT-gallo]] [[ENT-gerlach]] [[ENT-gourka]] [[ENT-grabowski]] [[ENT-gratchev]] [[ENT-grun]] [[ENT-guierassimov]] [[ENT-gunther]] [[ENT-gusev]] [[ENT-haider]] [[ENT-hofer]] [[ENT-horvat]] [[ENT-ivazov]] [[ENT-jerman]] [[ENT-julius]] [[ENT-junker]] [[ENT-kaczmarek]] [[ENT-kaleva]] [[ENT-kievov]] [[ENT-kirillov]] [[ENT-kiselev]] [[ENT-konig-lorenz]] [[ENT-konig-markus]] [[ENT-koulikov]] [[ENT-kozlov]] [[ENT-kuznetsov]] [[ENT-leitgeb]] [[ENT-lennartsson]] [[ENT-maizieree]] [[ENT-majcen]] [[ENT-majewski]] [[ENT-makarova-francesco]] [[ENT-mancini]] [[ENT-matovnikov]] [[ENT-maximov]] [[ENT-mercure]] [[ENT-michalski]] [[ENT-mikhailovic]] [[ENT-mikhelev]] [[ENT-milanov]] [[ENT-mizintsev]] [[ENT-morozov-nikolai]] [[ENT-moser]] [[ENT-muller-angela]] [[ENT-muller-viktoria]] [[ENT-neumann]] [[ENT-numelin]] [[ENT-oblak]] [[ENT-olamao]] [[ENT-orlov-irina]] [[ENT-palmieri]] [[ENT-pawlak]] [[ENT-petrov-marco]] [[ENT-pichler]] [[ENT-popov]] [[ENT-pruniere]] [[ENT-rasof]] [[ENT-reither]] [[ENT-ribiki]] [[ENT-rossi]] [[ENT-rozman]] [[ENT-rupnik]] [[ENT-sanders]] [[ENT-sanna-oleg]] [[ENT-schmid]] [[ENT-schwarz]] [[ENT-seidl]] [[ENT-sikorski]] [[ENT-sokolova-iouri]] [[ENT-soloviev]] [[ENT-soucek]] [[ENT-stoph]] [[ENT-tapeur]] [[ENT-tarasov]] [[ENT-toti]] [[ENT-urban]] [[ENT-urban-franziska]] [[ENT-vassielvski]] [[ENT-vassiliev]] [[ENT-viktorovitch]] [[ENT-vinogradov]] [[ENT-vogel]] [[ENT-volkov-alessia]] [[ENT-vostrikov]] [[ENT-vydra]] [[ENT-wagner-natalia]] [[ENT-wallner]] [[ENT-werner]] [[ENT-winkler]] [[ENT-zaitsev]] [[ENT-zajac]] [[ENT-zhukov]] [[ENT-zimmerman]] [[ENT-zupan]] [[REF-mercure-economie]] [[REF-mercure-information]] [[REF-mercure-militaire]] [[REF-mercure-politique]] [[REF-mercure-relations]] [[REF-mercure-societe]] [[REF-storm1516]] |
| [AGENT-ARCHITECTE](agents/AGENT-ARCHITECTE.md) | ARCHITECTE | 3 | [`MEMOIRE.md`](../../ARCHITECTE/MEMOIRE.md) | — |
| [AGENT-ARCHIVISTE](agents/AGENT-ARCHIVISTE.md) | ARCHIVISTE | 3 | [`MEMOIRE.md`](../../ARCHIVISTE/MEMOIRE.md) | — |
| [AGENT-BROUILLON](agents/AGENT-BROUILLON.md) | BROUILLON | 3 | [`MEMOIRE.md`](../../BROUILLON/MEMOIRE.md) | — |
| [AGENT-CINEASTE](agents/AGENT-CINEASTE.md) | CINÉASTE | 2 | [`MEMOIRE.md`](../../CINEASTE/MEMOIRE.md) | [[TOOL-009]] |
| [AGENT-ECLAIREUR](agents/AGENT-ECLAIREUR.md) | ÉCLAIREUR | 3 | [`MEMOIRE.md`](../../ECLAIREUR/MEMOIRE.md) | — |
| [AGENT-EXPERT-INFLUENCE](agents/AGENT-EXPERT-INFLUENCE.md) | EXPERT_INFLUENCE | 3 | [`MEMOIRE.md`](../../EXPERT_INFLUENCE/MEMOIRE.md) | — |
| [AGENT-GUILLAUME](agents/AGENT-GUILLAUME.md) | GUILLAUME | 3 | [`MEMOIRE.md`](../../GUILLAUME/MEMOIRE.md) | — |
| [AGENT-IMAGIER](agents/AGENT-IMAGIER.md) | IMAGIER | 2 | [`MEMOIRE.md`](../../IMAGIER/MEMOIRE.md) | [[TOOL-010]] |
| [AGENT-MASTAURIGE](agents/AGENT-MASTAURIGE.md) | MASTAURIGE | 2 | [`MEMOIRE.md`](../../MASTAURIGE/MEMOIRE.md) | [[ARCH-008]] [[DECISION-001]] [[DECISION-002]] [[DECISION-003]] [[DECISION-004]] [[DECISION-005]] [[DECISION-006]] [[LESSON-002]] [[LESSON-006]] [[LESSON-007]] [[LESSON-008]] [[LESSON-013]] [[PROJ-MASTAURIGE]] [[TOOL-001]] [[TOOL-002]] [[TOOL-003]] [[TOOL-004]] [[TOOL-005]] [[TOOL-006]] [[TOOL-007]] [[TOOL-011]] |
| [AGENT-MASTODONTE](agents/AGENT-MASTODONTE.md) | MASTODONTE | 3 | [`MEMOIRE.md`](../../MASTODONTE/MEMOIRE.md) | — |
| [AGENT-MINAUTORE](agents/AGENT-MINAUTORE.md) | MINAUTORE | 2 | [`MEMOIRE.md`](../../MINAUTORE/MEMOIRE.md) | [[PROJ-AURIGE-7BB]] |
| [AGENT-NOYAU](agents/AGENT-NOYAU.md) | NOYAU | 3 | [`MEMOIRE.md`](../../NOYAU/MEMOIRE.md) | — |
| [AGENT-PENSEUR](agents/AGENT-PENSEUR.md) | PENSEUR | 3 | [`MEMOIRE.md`](../../PENSEUR/MEMOIRE.md) | — |
| [AGENT-SCENARISTE](agents/AGENT-SCENARISTE.md) | SCÉNARISTE | 2 | [`MEMOIRE.md`](../../SCENARISTE/MEMOIRE.md) | [[LESSON-003]] |
| [AGENT-SECRETAIRE](agents/AGENT-SECRETAIRE.md) | SECRÉTAIRE | 3 | [`MEMOIRE.md`](../../SECRETAIRE/MEMOIRE.md) | — |
| [AGENT-VOIX](agents/AGENT-VOIX.md) | VOIX | 2 | [`MEMOIRE.md`](../../VOIX/MEMOIRE.md) | [[TOOL-008]] |

## 🌍 Entités (personas · pays · doctrine)

| ID | Titre | Tier | Source (vérité) | Liens |
|---|---|---|---|---|
| [ENT-abdoulaiev](entities/personas/ENT-abdoulaiev.md) | Sliman Abdoulaïev | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-adam](entities/personas/ENT-adam.md) | Lisa Adam | 3 | [`MEMOIRE.md`](../../../ANALYSTE/BOTHNIA/MEMOIRE.md) | [[ENT-bothnia]] |
| [ENT-alvarez](entities/personas/ENT-alvarez.md) | Erik Alvarez | 3 | [`MEMOIRE.md`](../../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] |
| [ENT-amin](entities/personas/ENT-amin.md) | Nero Amin | 3 | [`MEMOIRE.md`](../../../ANALYSTE/BOTHNIA/MEMOIRE.md) | [[ENT-bothnia]] |
| [ENT-anders-lorentz](entities/personas/ENT-anders-lorentz.md) | Lorentz Anders | 3 | [`MEMOIRE.md`](../../../ANALYSTE/BOTHNIA/MEMOIRE.md) | [[ENT-bothnia]] |
| [ENT-andersen-line](entities/personas/ENT-andersen-line.md) | Line Andersen | 3 | [`MEMOIRE.md`](../../../ANALYSTE/BOTHNIA/MEMOIRE.md) | [[ENT-bothnia]] |
| [ENT-andreev-boris](entities/personas/ENT-andreev-boris.md) | Boris Andreev | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-andreev-milan](entities/personas/ENT-andreev-milan.md) | Milan Andreev | 3 | [`MEMOIRE.md`](../../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] |
| [ENT-antonov](entities/personas/ENT-antonov.md) | Yuri Antonov | 3 | [`MEMOIRE.md`](../../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] |
| [ENT-antonova](entities/personas/ENT-antonova.md) | Zoya Antonova | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-arne](entities/personas/ENT-arne.md) | Arne | 3 | [`MEMOIRE.md`](../../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] |
| [ENT-arnland](entities/pays/ENT-arnland.md) | Arnland (Dacie Romanie — DAC/DR) | 1 | [`MEMOIRE.md`](../../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-pallesson]] [[ENT-volkonsky]] [[ENT-savchenko]] [[ENT-borchenko]] [[LESSON-004]] |
| [ENT-astapenka](entities/personas/ENT-astapenka.md) | Alyaksei Astapenka | 3 | [`MEMOIRE.md`](../../../ANALYSTE/BOTHNIA/MEMOIRE.md) | [[ENT-bothnia]] |
| [ENT-auer-georg](entities/personas/ENT-auer-georg.md) | Georg Auer | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-auer-tobias](entities/personas/ENT-auer-tobias.md) | Tobias Auer | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-baradzin](entities/personas/ENT-baradzin.md) | Sviatlana Baradzin | 3 | [`MEMOIRE.md`](../../../ANALYSTE/BOTHNIA/MEMOIRE.md) | [[ENT-bothnia]] |
| [ENT-baranov](entities/personas/ENT-baranov.md) | Ivan Baranov | 3 | [`MEMOIRE.md`](../../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] |
| [ENT-bauer-yuri](entities/personas/ENT-bauer-yuri.md) | Yuri Bauer | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-baumgartner](entities/personas/ENT-baumgartner.md) | Marc Baumgartner | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-belov](entities/personas/ENT-belov.md) | Andrei Belov | 3 | [`MEMOIRE.md`](../../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] |
| [ENT-bielski](entities/personas/ENT-bielski.md) | Anton Bielski | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-birkmann](entities/personas/ENT-birkmann.md) | Augustin Birkmann | 3 | [`MEMOIRE.md`](../../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] |
| [ENT-blazic](entities/personas/ENT-blazic.md) | Vesna Blazic | 3 | [`MEMOIRE.md`](../../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] |
| [ENT-bodrova](entities/personas/ENT-bodrova.md) | Tatiana Bodrova | 3 | [`MEMOIRE.md`](../../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] |
| [ENT-boerck](entities/personas/ENT-boerck.md) | Andreas Boerck | 3 | [`MEMOIRE.md`](../../../ANALYSTE/BOTHNIA/MEMOIRE.md) | [[ENT-bothnia]] [[ENT-peters]] |
| [ENT-bogdanov](entities/personas/ENT-bogdanov.md) | Stanislav Bogdanov | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-bohler](entities/personas/ENT-bohler.md) | Erika Bohler | 3 | [`MEMOIRE.md`](../../../ANALYSTE/BOTHNIA/MEMOIRE.md) | [[ENT-bothnia]] |
| [ENT-bold](entities/personas/ENT-bold.md) | Baltzar Bold | 3 | [`MEMOIRE.md`](../../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] |
| [ENT-borchenko](entities/personas/ENT-borchenko.md) | Maksym Borchenko | 2 | [`MEMOIRE.md`](../../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] |
| [ENT-borovic](entities/personas/ENT-borovic.md) | Tanja Borović | 3 | [`MEMOIRE.md`](../../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] |
| [ENT-bothnia](entities/pays/ENT-bothnia.md) | Bothnia (Republic of Bothnia — BOT) | 1 | [`MEMOIRE.md`](../../../ANALYSTE/BOTHNIA/MEMOIRE.md) | [[ENT-peters]] [[ENT-tikhanov]] [[ENT-saniki]] [[LESSON-001]] [[LESSON-004]] |
| [ENT-brandtsev](entities/personas/ENT-brandtsev.md) | Serhiy Brandtsev | 3 | [`MEMOIRE.md`](../../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] |
| [ENT-breesson](entities/personas/ENT-breesson.md) | Josef Breesson | 3 | [`MEMOIRE.md`](../../../ANALYSTE/BOTHNIA/MEMOIRE.md) | [[ENT-bothnia]] |
| [ENT-brenner](entities/personas/ENT-brenner.md) | Nikolaï Brenner | 3 | [`MEMOIRE.md`](../../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] |
| [ENT-brrouette](entities/personas/ENT-brrouette.md) | Leonard Brrouette | 3 | [`MEMOIRE.md`](../../../ANALYSTE/BOTHNIA/MEMOIRE.md) | [[ENT-bothnia]] |
| [ENT-bruske](entities/personas/ENT-bruske.md) | Sven Bruske | 3 | [`MEMOIRE.md`](../../../ANALYSTE/BOTHNIA/MEMOIRE.md) | [[ENT-bothnia]] |
| [ENT-bryl](entities/personas/ENT-bryl.md) | Palina Bryl | 3 | [`MEMOIRE.md`](../../../ANALYSTE/BOTHNIA/MEMOIRE.md) | [[ENT-bothnia]] |
| [ENT-buerger](entities/personas/ENT-buerger.md) | Dr Cecilia Buerger | 3 | [`MEMOIRE.md`](../../../ANALYSTE/BOTHNIA/MEMOIRE.md) | [[ENT-bothnia]] |
| [ENT-bystrom](entities/personas/ENT-bystrom.md) | Bystrom | 3 | [`MEMOIRE.md`](../../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] |
| [ENT-caruso](entities/personas/ENT-caruso.md) | Ksenia Caruso | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-chareyron](entities/personas/ENT-chareyron.md) | Chareyron | 3 | [`MEMOIRE.md`](../../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] |
| [ENT-conti](entities/personas/ENT-conti.md) | Federico Conti | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-declercq](entities/personas/ENT-declercq.md) | Annelies de Clercq | 3 | [`MEMOIRE.md`](../../../ANALYSTE/BOTHNIA/MEMOIRE.md) | [[ENT-bothnia]] |
| [ENT-denisov](entities/personas/ENT-denisov.md) | Ilya Denisov | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-depoire](entities/personas/ENT-depoire.md) | Depoire | 3 | [`MEMOIRE.md`](../../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] |
| [ENT-dewaele](entities/personas/ENT-dewaele.md) | Patrick De Waele | 3 | [`MEMOIRE.md`](../../../ANALYSTE/BOTHNIA/MEMOIRE.md) | [[ENT-bothnia]] |
| [ENT-dimitrov](entities/personas/ENT-dimitrov.md) | Oleg Dimitrov | 3 | [`MEMOIRE.md`](../../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] |
| [ENT-diniz](entities/personas/ENT-diniz.md) | Catarina Diniz | 2 | [`MEMOIRE.md`](../../../ANALYSTE/BOTHNIA/MEMOIRE.md) | [[ENT-bothnia]] [[ENT-schmit]] |
| [ENT-djobovic](entities/personas/ENT-djobovic.md) | Marko Djobović | 3 | [`MEMOIRE.md`](../../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] |
| [ENT-dragunov](entities/personas/ENT-dragunov.md) | Viktor Dragunov | 3 | [`MEMOIRE.md`](../../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] |
| [ENT-druey](entities/personas/ENT-druey.md) | Ursula Druey | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-dubrouski](entities/personas/ENT-dubrouski.md) | Mikalai Dubrouski | 3 | [`MEMOIRE.md`](../../../ANALYSTE/BOTHNIA/MEMOIRE.md) | [[ENT-bothnia]] |
| [ENT-durova](entities/personas/ENT-durova.md) | Katarina Durova | 3 | [`MEMOIRE.md`](../../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] |
| [ENT-dvornikov](entities/personas/ENT-dvornikov.md) | Sergueï Dvornikov | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-dziadok-maryia](entities/personas/ENT-dziadok-maryia.md) | Maryia Dziadok | 3 | [`MEMOIRE.md`](../../../ANALYSTE/BOTHNIA/MEMOIRE.md) | [[ENT-bothnia]] |
| [ENT-dziadok-natallia](entities/personas/ENT-dziadok-natallia.md) | Natallia Dziadok | 3 | [`MEMOIRE.md`](../../../ANALYSTE/BOTHNIA/MEMOIRE.md) | [[ENT-bothnia]] |
| [ENT-ebner](entities/personas/ENT-ebner.md) | Artem Ebner | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-eklund](entities/personas/ENT-eklund.md) | Henrik Eklund | 3 | [`MEMOIRE.md`](../../../ANALYSTE/BOTHNIA/MEMOIRE.md) | [[ENT-bothnia]] [[ENT-nyberg]] [[ENT-viklund]] |
| [ENT-erickson](entities/personas/ENT-erickson.md) | Josef Erickson | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-erik-petra](entities/personas/ENT-erik-petra.md) | Petra Erik | 3 | [`MEMOIRE.md`](../../../ANALYSTE/BOTHNIA/MEMOIRE.md) | [[ENT-bothnia]] |
| [ENT-filipovic](entities/personas/ENT-filipovic.md) | Zoran Filipović | 3 | [`MEMOIRE.md`](../../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] |
| [ENT-fischer](entities/personas/ENT-fischer.md) | Aleksandr Fischer | 3 | [`MEMOIRE.md`](../../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] |
| [ENT-fluxa](entities/personas/ENT-fluxa.md) | Fluxa | 3 | [`MEMOIRE.md`](../../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] |
| [ENT-franke](entities/personas/ENT-franke.md) | Sebastian Franke | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-fredotov](entities/personas/ENT-fredotov.md) | Anatoli Fredotov | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-fries](entities/personas/ENT-fries.md) | Fries | 3 | [`MEMOIRE.md`](../../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] |
| [ENT-frolov](entities/personas/ENT-frolov.md) | Piotr Frolov | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-fuchs](entities/personas/ENT-fuchs.md) | Verena Fuchs | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-gallo](entities/personas/ENT-gallo.md) | Pavel Gallo | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-gerlach](entities/personas/ENT-gerlach.md) | Sabine Gerlach | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-gervais](entities/personas/ENT-gervais.md) | Émile Gervais | 3 | [`MEMOIRE.md`](../../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] |
| [ENT-gourka](entities/personas/ENT-gourka.md) | Sergueï Gourka | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-grabowski](entities/personas/ENT-grabowski.md) | Rafal Grabowski | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-gradholm](entities/personas/ENT-gradholm.md) | Malte Gradholm | 3 | [`MEMOIRE.md`](../../../ANALYSTE/BOTHNIA/MEMOIRE.md) | [[ENT-bothnia]] |
| [ENT-gradholm-arn](entities/personas/ENT-gradholm-arn.md) | Gradholm (ARN) | 3 | [`MEMOIRE.md`](../../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] |
| [ENT-gratchev](entities/personas/ENT-gratchev.md) | Ievgueni Gratchev | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-groop](entities/personas/ENT-groop.md) | Tyko Groop | 3 | [`MEMOIRE.md`](../../../ANALYSTE/BOTHNIA/MEMOIRE.md) | [[ENT-bothnia]] |
| [ENT-grun](entities/personas/ENT-grun.md) | Louise Grun | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-guierassimov](entities/personas/ENT-guierassimov.md) | Igor Guierassimov | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-gunther](entities/personas/ENT-gunther.md) | Greta Günther | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-gusev](entities/personas/ENT-gusev.md) | Leonid Gusev | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-haider](entities/personas/ENT-haider.md) | Agnieszka Haider | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-hansen](entities/personas/ENT-hansen.md) | Hanna Hansen | 3 | [`MEMOIRE.md`](../../../ANALYSTE/BOTHNIA/MEMOIRE.md) | [[ENT-bothnia]] [[ENT-petrovic]] [[ENT-tikhanov]] |
| [ENT-hartmann](entities/personas/ENT-hartmann.md) | Grigori Hartmann | 3 | [`MEMOIRE.md`](../../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] |
| [ENT-havrylenko](entities/personas/ENT-havrylenko.md) | Lukas Havrylenko | 3 | [`MEMOIRE.md`](../../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] |
| [ENT-hofer](entities/personas/ENT-hofer.md) | Margarita Hofer | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-hoffmann](entities/personas/ENT-hoffmann.md) | Olena Hoffmann | 3 | [`MEMOIRE.md`](../../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] |
| [ENT-holm](entities/personas/ENT-holm.md) | Viktor Holm | 3 | [`MEMOIRE.md`](../../../ANALYSTE/BOTHNIA/MEMOIRE.md) | [[ENT-bothnia]] |
| [ENT-horby](entities/personas/ENT-horby.md) | Tor Horby | 3 | [`MEMOIRE.md`](../../../ANALYSTE/BOTHNIA/MEMOIRE.md) | [[ENT-bothnia]] |
| [ENT-horvat](entities/personas/ENT-horvat.md) | Gregor Horvat | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-hurski](entities/personas/ENT-hurski.md) | Andrej Hurski | 3 | [`MEMOIRE.md`](../../../ANALYSTE/BOTHNIA/MEMOIRE.md) | [[ENT-bothnia]] |
| [ENT-hus](entities/personas/ENT-hus.md) | Hus | 3 | [`MEMOIRE.md`](../../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] |
| [ENT-iliev](entities/personas/ENT-iliev.md) | Marko Iliev | 3 | [`MEMOIRE.md`](../../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] |
| [ENT-ivanouski](entities/personas/ENT-ivanouski.md) | Yauhen Ivanouski | 3 | [`MEMOIRE.md`](../../../ANALYSTE/BOTHNIA/MEMOIRE.md) | [[ENT-bothnia]] |
| [ENT-ivanov-sergey](entities/personas/ENT-ivanov-sergey.md) | Sergey Ivanov | 3 | [`MEMOIRE.md`](../../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] |
| [ENT-ivanovitch](entities/personas/ENT-ivanovitch.md) | Viktor Ivanovitch | 3 | [`MEMOIRE.md`](../../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] |
| [ENT-ivazov](entities/personas/ENT-ivazov.md) | Ivan Ivazov | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-jaksic](entities/personas/ENT-jaksic.md) | Radovan Jakšić | 3 | [`MEMOIRE.md`](../../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] |
| [ENT-jankovic](entities/personas/ENT-jankovic.md) | Mira Janković | 3 | [`MEMOIRE.md`](../../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] |
| [ENT-jansen](entities/personas/ENT-jansen.md) | Ingo Jansen | 3 | [`MEMOIRE.md`](../../../ANALYSTE/BOTHNIA/MEMOIRE.md) | [[ENT-bothnia]] |
| [ENT-jensen-niels](entities/personas/ENT-jensen-niels.md) | Niels Jensen | 3 | [`MEMOIRE.md`](../../../ANALYSTE/BOTHNIA/MEMOIRE.md) | [[ENT-bothnia]] |
| [ENT-jerman](entities/personas/ENT-jerman.md) | Maja Jerman | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-julius](entities/personas/ENT-julius.md) | Peter Julius | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-junker](entities/personas/ENT-junker.md) | Jonas Junker | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-kaczmarek](entities/personas/ENT-kaczmarek.md) | Bartosz Kaczmarek | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-kalenik](entities/personas/ENT-kalenik.md) | Dmitri Kalenik | 3 | [`MEMOIRE.md`](../../../ANALYSTE/BOTHNIA/MEMOIRE.md) | [[ENT-bothnia]] |
| [ENT-kaleva](entities/personas/ENT-kaleva.md) | Viktor Kaleva | 2 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] [[ENT-milanov]] |
| [ENT-kalugin](entities/personas/ENT-kalugin.md) | Boris Kalugin | 3 | [`MEMOIRE.md`](../../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] |
| [ENT-karadzic](entities/personas/ENT-karadzic.md) | Bojan Karadzic | 3 | [`MEMOIRE.md`](../../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] |
| [ENT-karlson-erik](entities/personas/ENT-karlson-erik.md) | Erik Karlson | 3 | [`MEMOIRE.md`](../../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] |
| [ENT-karpovitch](entities/personas/ENT-karpovitch.md) | Artsiom Karpovitch | 3 | [`MEMOIRE.md`](../../../ANALYSTE/BOTHNIA/MEMOIRE.md) | [[ENT-bothnia]] |
| [ENT-karrlson](entities/personas/ENT-karrlson.md) | Vincent Karrlson | 3 | [`MEMOIRE.md`](../../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] |
| [ENT-kavalenka](entities/personas/ENT-kavalenka.md) | Yury Kavalenka | 3 | [`MEMOIRE.md`](../../../ANALYSTE/BOTHNIA/MEMOIRE.md) | [[ENT-bothnia]] |
| [ENT-kellerov](entities/personas/ENT-kellerov.md) | Anton Kellerov | 3 | [`MEMOIRE.md`](../../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] |
| [ENT-kermovant](entities/personas/ENT-kermovant.md) | Kermovant | 3 | [`MEMOIRE.md`](../../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] |
| [ENT-kievov](entities/personas/ENT-kievov.md) | Slava Kievov | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-kirillov](entities/personas/ENT-kirillov.md) | Aleksandr Kirillov | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-kiselev](entities/personas/ENT-kiselev.md) | Timur Kiselev | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-koho](entities/personas/ENT-koho.md) | Harri Koho | 3 | [`MEMOIRE.md`](../../../ANALYSTE/BOTHNIA/MEMOIRE.md) | [[ENT-bothnia]] |
| [ENT-koivisto](entities/personas/ENT-koivisto.md) | Koivisto | 3 | [`MEMOIRE.md`](../../../ANALYSTE/BOTHNIA/MEMOIRE.md) | [[ENT-bothnia]] |
| [ENT-konig-lorenz](entities/personas/ENT-konig-lorenz.md) | Lorenz König | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-konig-markus](entities/personas/ENT-konig-markus.md) | Markus König | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-korolev](entities/personas/ENT-korolev.md) | Alexandr Korolev | 3 | [`MEMOIRE.md`](../../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] |
| [ENT-kosmannen](entities/personas/ENT-kosmannen.md) | Teemu Kosmannen | 3 | [`MEMOIRE.md`](../../../ANALYSTE/BOTHNIA/MEMOIRE.md) | [[ENT-bothnia]] |
| [ENT-kostich](entities/personas/ENT-kostich.md) | Jannik Kostich | 3 | [`MEMOIRE.md`](../../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] |
| [ENT-kostova](entities/personas/ENT-kostova.md) | Natalya Kostova | 3 | [`MEMOIRE.md`](../../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] |
| [ENT-koulikov](entities/personas/ENT-koulikov.md) | Gueorgy Koulikov | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-kovalenko-viktor](entities/personas/ENT-kovalenko-viktor.md) | Viktor Kovalenko | 3 | [`MEMOIRE.md`](../../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] |
| [ENT-kovalev](entities/personas/ENT-kovalev.md) | Dmitri Kovalev | 3 | [`MEMOIRE.md`](../../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] |
| [ENT-kozlov](entities/personas/ENT-kozlov.md) | Maksim Kozlov | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-kramer](entities/personas/ENT-kramer.md) | Anna Kramer | 3 | [`MEMOIRE.md`](../../../ANALYSTE/BOTHNIA/MEMOIRE.md) | [[ENT-bothnia]] |
| [ENT-krauss](entities/personas/ENT-krauss.md) | Isabelle Krauss | 3 | [`MEMOIRE.md`](../../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] |
| [ENT-kravchenko](entities/personas/ENT-kravchenko.md) | Nikolai Kravchenko | 3 | [`MEMOIRE.md`](../../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] |
| [ENT-kravtsova](entities/personas/ENT-kravtsova.md) | Anastasia Kravtsova | 3 | [`MEMOIRE.md`](../../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] |
| [ENT-kulis](entities/personas/ENT-kulis.md) | Kulis | 3 | [`MEMOIRE.md`](../../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] |
| [ENT-kuznetsov](entities/personas/ENT-kuznetsov.md) | Roman Kuznetsov | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-lang](entities/personas/ENT-lang.md) | Dorothée Lang | 3 | [`MEMOIRE.md`](../../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] |
| [ENT-lapitski](entities/personas/ENT-lapitski.md) | Marina Lapitski | 3 | [`MEMOIRE.md`](../../../ANALYSTE/BOTHNIA/MEMOIRE.md) | [[ENT-bothnia]] |
| [ENT-laporte](entities/personas/ENT-laporte.md) | Laporte | 3 | [`MEMOIRE.md`](../../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] |
| [ENT-lebedev](entities/personas/ENT-lebedev.md) | Alexei Lebedev | 3 | [`MEMOIRE.md`](../../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] |
| [ENT-leitgeb](entities/personas/ENT-leitgeb.md) | Magdalena Leitgeb | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-lennartsson](entities/personas/ENT-lennartsson.md) | Sixten Lennartsson | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-lindquist](entities/personas/ENT-lindquist.md) | Kevin Lindquist | 3 | [`MEMOIRE.md`](../../../ANALYSTE/BOTHNIA/MEMOIRE.md) | [[ENT-bothnia]] |
| [ENT-madsen-freja](entities/personas/ENT-madsen-freja.md) | Freja Madsen | 3 | [`MEMOIRE.md`](../../../ANALYSTE/BOTHNIA/MEMOIRE.md) | [[ENT-bothnia]] |
| [ENT-madsen-ida](entities/personas/ENT-madsen-ida.md) | Ida Madsen | 3 | [`MEMOIRE.md`](../../../ANALYSTE/BOTHNIA/MEMOIRE.md) | [[ENT-bothnia]] |
| [ENT-maes](entities/personas/ENT-maes.md) | Dries Maes | 3 | [`MEMOIRE.md`](../../../ANALYSTE/BOTHNIA/MEMOIRE.md) | [[ENT-bothnia]] |
| [ENT-maizieree](entities/personas/ENT-maizieree.md) | Sasha Maizierèe | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-majcen](entities/personas/ENT-majcen.md) | Miha Majcen | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-majewski](entities/personas/ENT-majewski.md) | Patryk Majewski | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-makarevich](entities/personas/ENT-makarevich.md) | Ulyana Makarevich | 3 | [`MEMOIRE.md`](../../../ANALYSTE/BOTHNIA/MEMOIRE.md) | [[ENT-bothnia]] |
| [ENT-makarova-francesco](entities/personas/ENT-makarova-francesco.md) | Francesco Makarova | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-malenko](entities/personas/ENT-malenko.md) | Yegor Malenko | 3 | [`MEMOIRE.md`](../../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] |
| [ENT-malmsten](entities/personas/ENT-malmsten.md) | Anders Malmsten | 3 | [`MEMOIRE.md`](../../../ANALYSTE/BOTHNIA/MEMOIRE.md) | [[ENT-bothnia]] |
| [ENT-mancini](entities/personas/ENT-mancini.md) | Alla Mancini | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-marinov](entities/personas/ENT-marinov.md) | Vladislav Marinov | 3 | [`MEMOIRE.md`](../../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] |
| [ENT-marozau](entities/personas/ENT-marozau.md) | Tatsiana Marozau | 3 | [`MEMOIRE.md`](../../../ANALYSTE/BOTHNIA/MEMOIRE.md) | [[ENT-bothnia]] |
| [ENT-matovnikov](entities/personas/ENT-matovnikov.md) | Aleksandr Matovnikov | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-maximov](entities/personas/ENT-maximov.md) | Pavel Maximov | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-mercure](entities/pays/ENT-mercure.md) | République de Mercure (MER) | 1 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-olamao]] [[ENT-kaleva]] [[ENT-milanov]] [[LESSON-001]] [[LESSON-004]] |
| [ENT-meyer](entities/personas/ENT-meyer.md) | Nele Meyer | 3 | [`MEMOIRE.md`](../../../ANALYSTE/BOTHNIA/MEMOIRE.md) | [[ENT-bothnia]] [[ENT-peters]] |
| [ENT-michalski](entities/personas/ENT-michalski.md) | Iwona Michalski | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-mikhailovic](entities/personas/ENT-mikhailovic.md) | Dimitri Mikhailovic | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-mikhelev](entities/personas/ENT-mikhelev.md) | Kristian Mikhelev | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-milanov](entities/personas/ENT-milanov.md) | Arkan Milanov | 2 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] [[ENT-kaleva]] |
| [ENT-milenkovic](entities/personas/ENT-milenkovic.md) | Zoya Milenković | 3 | [`MEMOIRE.md`](../../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] |
| [ENT-milova](entities/personas/ENT-milova.md) | Ekaterina Milova | 3 | [`MEMOIRE.md`](../../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] |
| [ENT-mishin](entities/personas/ENT-mishin.md) | Igor Mishin | 3 | [`MEMOIRE.md`](../../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] |
| [ENT-mizintsev](entities/personas/ENT-mizintsev.md) | Vladimir Mizintsev | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-morozov](entities/personas/ENT-morozov.md) | Alexei Morozov | 3 | [`MEMOIRE.md`](../../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] |
| [ENT-morozov-nikolai](entities/personas/ENT-morozov-nikolai.md) | Nikolaï Morozov | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-moser](entities/personas/ENT-moser.md) | Heidi Moser | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-muller-aiko](entities/personas/ENT-muller-aiko.md) | Dr Aiko Müller | 3 | [`MEMOIRE.md`](../../../ANALYSTE/BOTHNIA/MEMOIRE.md) | [[ENT-bothnia]] |
| [ENT-muller-angela](entities/personas/ENT-muller-angela.md) | Angela Muller | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-muller-viktoria](entities/personas/ENT-muller-viktoria.md) | Viktoria Müller | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-neumann](entities/personas/ENT-neumann.md) | Alexei Neumann | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-nielsen-kasper](entities/personas/ENT-nielsen-kasper.md) | Kasper Nielsen | 3 | [`MEMOIRE.md`](../../../ANALYSTE/BOTHNIA/MEMOIRE.md) | [[ENT-bothnia]] |
| [ENT-nikitin](entities/personas/ENT-nikitin.md) | Sergei Nikitin | 3 | [`MEMOIRE.md`](../../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] |
| [ENT-novak](entities/personas/ENT-novak.md) | Boris Novak | 3 | [`MEMOIRE.md`](../../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] |
| [ENT-novik](entities/personas/ENT-novik.md) | Siarhei Novik | 3 | [`MEMOIRE.md`](../../../ANALYSTE/BOTHNIA/MEMOIRE.md) | [[ENT-bothnia]] |
| [ENT-novik-lidija](entities/personas/ENT-novik-lidija.md) | Lidija Novik | 3 | [`MEMOIRE.md`](../../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] |
| [ENT-numelin](entities/personas/ENT-numelin.md) | Fred Numelin | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-nyberg](entities/personas/ENT-nyberg.md) | Samuel Nyberg | 3 | [`MEMOIRE.md`](../../../ANALYSTE/BOTHNIA/MEMOIRE.md) | [[ENT-bothnia]] [[ENT-viklund]] [[ENT-eklund]] |
| [ENT-oblak](entities/personas/ENT-oblak.md) | Nik Oblak | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-olamao](entities/personas/ENT-olamao.md) | Franz Olamao | 2 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] [[ENT-junker]] |
| [ENT-orlov-irina](entities/personas/ENT-orlov-irina.md) | Irina Orlov | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-pallesson](entities/personas/ENT-pallesson.md) | Sture Pallesson | 3 | [`MEMOIRE.md`](../../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] |
| [ENT-palmieri](entities/personas/ENT-palmieri.md) | Dmitri Palmieri | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-palmquetil](entities/personas/ENT-palmquetil.md) | Tony Palmquetil | 3 | [`MEMOIRE.md`](../../../ANALYSTE/BOTHNIA/MEMOIRE.md) | [[ENT-bothnia]] |
| [ENT-pavlenko-luka](entities/personas/ENT-pavlenko-luka.md) | Luka Pavlenko | 3 | [`MEMOIRE.md`](../../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] |
| [ENT-pavlenko-natalya](entities/personas/ENT-pavlenko-natalya.md) | Natalya Pavlenko | 3 | [`MEMOIRE.md`](../../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] |
| [ENT-pavlenko-nikolai](entities/personas/ENT-pavlenko-nikolai.md) | Nikolai Pavlenko | 3 | [`MEMOIRE.md`](../../../ANALYSTE/BOTHNIA/MEMOIRE.md) | [[ENT-bothnia]] |
| [ENT-pawlak](entities/personas/ENT-pawlak.md) | Petra Pawlak | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-pedersen-anders](entities/personas/ENT-pedersen-anders.md) | Anders Pedersen | 3 | [`MEMOIRE.md`](../../../ANALYSTE/BOTHNIA/MEMOIRE.md) | [[ENT-bothnia]] |
| [ENT-peters](entities/personas/ENT-peters.md) | Lena Peters | 2 | [`MEMOIRE.md`](../../../ANALYSTE/BOTHNIA/MEMOIRE.md) | [[ENT-bothnia]] [[ENT-roland]] [[ENT-meyer]] |
| [ENT-petrov-marco](entities/personas/ENT-petrov-marco.md) | Marco Petrov | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-petrova-irina](entities/personas/ENT-petrova-irina.md) | Irina Petrova | 3 | [`MEMOIRE.md`](../../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] |
| [ENT-petrovic](entities/personas/ENT-petrovic.md) | Milena Petrovic | 3 | [`MEMOIRE.md`](../../../ANALYSTE/BOTHNIA/MEMOIRE.md) | [[ENT-bothnia]] [[ENT-hansen]] |
| [ENT-petrovic-radmila](entities/personas/ENT-petrovic-radmila.md) | Radmila Petrović | 3 | [`MEMOIRE.md`](../../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] |
| [ENT-petrovna](entities/personas/ENT-petrovna.md) | Elena Petrovna | 3 | [`MEMOIRE.md`](../../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] |
| [ENT-pichler](entities/personas/ENT-pichler.md) | Jakob Pichler | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-pierrinen](entities/personas/ENT-pierrinen.md) | Niampsa Pierrinen | 3 | [`MEMOIRE.md`](../../../ANALYSTE/BOTHNIA/MEMOIRE.md) | [[ENT-bothnia]] |
| [ENT-popov](entities/personas/ENT-popov.md) | Vladimir Popov | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-pruniere](entities/personas/ENT-pruniere.md) | Thierry Prunière | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-radojevic](entities/personas/ENT-radojevic.md) | Svetlana Radojević | 3 | [`MEMOIRE.md`](../../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] |
| [ENT-radulov](entities/personas/ENT-radulov.md) | Dmitri Radulov | 3 | [`MEMOIRE.md`](../../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] |
| [ENT-radzivil](entities/personas/ENT-radzivil.md) | Valery Radzivil | 3 | [`MEMOIRE.md`](../../../ANALYSTE/BOTHNIA/MEMOIRE.md) | [[ENT-bothnia]] |
| [ENT-radzivil-aliaksandr](entities/personas/ENT-radzivil-aliaksandr.md) | Aliaksandr Radzivil | 3 | [`MEMOIRE.md`](../../../ANALYSTE/BOTHNIA/MEMOIRE.md) | [[ENT-bothnia]] |
| [ENT-rasmussen](entities/personas/ENT-rasmussen.md) | Emil Rasmussen | 3 | [`MEMOIRE.md`](../../../ANALYSTE/BOTHNIA/MEMOIRE.md) | [[ENT-bothnia]] |
| [ENT-rasof](entities/personas/ENT-rasof.md) | Sergueï Rasof | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-reither](entities/personas/ENT-reither.md) | Theresa Reither | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-ribiki](entities/personas/ENT-ribiki.md) | Voichek Ribiki | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-richter](entities/personas/ENT-richter.md) | Ann Richter | 3 | [`MEMOIRE.md`](../../../ANALYSTE/BOTHNIA/MEMOIRE.md) | [[ENT-bothnia]] |
| [ENT-roland](entities/personas/ENT-roland.md) | Olaf Roland | 3 | [`MEMOIRE.md`](../../../ANALYSTE/BOTHNIA/MEMOIRE.md) | [[ENT-bothnia]] [[ENT-peters]] |
| [ENT-rosendaal](entities/personas/ENT-rosendaal.md) | Oliver Rosendaal | 3 | [`MEMOIRE.md`](../../../ANALYSTE/BOTHNIA/MEMOIRE.md) | [[ENT-bothnia]] |
| [ENT-rosenquist](entities/personas/ENT-rosenquist.md) | Wilhelm Rosenquist | 3 | [`MEMOIRE.md`](../../../ANALYSTE/BOTHNIA/MEMOIRE.md) | [[ENT-bothnia]] |
| [ENT-rossi](entities/personas/ENT-rossi.md) | Mikhaïl Rossi | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-rozman](entities/personas/ENT-rozman.md) | Rok Rozman | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-rupnik](entities/personas/ENT-rupnik.md) | Jure Rupnik | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-rylander](entities/personas/ENT-rylander.md) | Quirin Rylander | 3 | [`MEMOIRE.md`](../../../ANALYSTE/BOTHNIA/MEMOIRE.md) | [[ENT-bothnia]] |
| [ENT-rynkevich](entities/personas/ENT-rynkevich.md) | Halina Rynkevich | 3 | [`MEMOIRE.md`](../../../ANALYSTE/BOTHNIA/MEMOIRE.md) | [[ENT-bothnia]] |
| [ENT-sanders](entities/personas/ENT-sanders.md) | Ragnar Sanders | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-saniki](entities/personas/ENT-saniki.md) | Andrei Saniki | 2 | [`MEMOIRE.md`](../../../ANALYSTE/BOTHNIA/MEMOIRE.md) | [[ENT-bothnia]] [[ENT-tikhanov]] [[LESSON-001]] [[LESSON-006]] |
| [ENT-sanna-oleg](entities/personas/ENT-sanna-oleg.md) | Oleg Sanna | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-savchenko](entities/personas/ENT-savchenko.md) | Nataliya Savchenko | 2 | [`MEMOIRE.md`](../../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] [[ENT-volkonsky]] [[LESSON-001]] |
| [ENT-savchenko-anya](entities/personas/ENT-savchenko-anya.md) | Anya Savchenko | 3 | [`MEMOIRE.md`](../../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] |
| [ENT-schmid](entities/personas/ENT-schmid.md) | Zala Schmid | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-schmidt](entities/personas/ENT-schmidt.md) | Daniel Schmidt | 3 | [`MEMOIRE.md`](../../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] |
| [ENT-schmit](entities/personas/ENT-schmit.md) | Marc Schmit | 3 | [`MEMOIRE.md`](../../../ANALYSTE/BOTHNIA/MEMOIRE.md) | [[ENT-bothnia]] [[ENT-diniz]] |
| [ENT-schwarz](entities/personas/ENT-schwarz.md) | Antonia Schwarz | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-seidl](entities/personas/ENT-seidl.md) | Benedikt Seidl | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-shauchenka](entities/personas/ENT-shauchenka.md) | Yan Shauchenka | 3 | [`MEMOIRE.md`](../../../ANALYSTE/BOTHNIA/MEMOIRE.md) | [[ENT-bothnia]] |
| [ENT-shymanovich](entities/personas/ENT-shymanovich.md) | Paval Shymanovich | 3 | [`MEMOIRE.md`](../../../ANALYSTE/BOTHNIA/MEMOIRE.md) | [[ENT-bothnia]] |
| [ENT-sidorov](entities/personas/ENT-sidorov.md) | Mikhail Sidorov | 3 | [`MEMOIRE.md`](../../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] |
| [ENT-sikorski](entities/personas/ENT-sikorski.md) | Andrzej Sikorski | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-sokal](entities/personas/ENT-sokal.md) | Vassilina Sokal | 3 | [`MEMOIRE.md`](../../../ANALYSTE/BOTHNIA/MEMOIRE.md) | [[ENT-bothnia]] |
| [ENT-sokolova-anastasia](entities/personas/ENT-sokolova-anastasia.md) | Anastasia Sokolova | 3 | [`MEMOIRE.md`](../../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] |
| [ENT-sokolova-iouri](entities/personas/ENT-sokolova-iouri.md) | Iouri Sokolova | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-sokolova-natalia](entities/personas/ENT-sokolova-natalia.md) | Natalia Sokolova | 3 | [`MEMOIRE.md`](../../../ANALYSTE/BOTHNIA/MEMOIRE.md) | [[ENT-bothnia]] |
| [ENT-soloviev](entities/personas/ENT-soloviev.md) | Igor Soloviev | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-soucek](entities/personas/ENT-soucek.md) | Walter Soucek | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-stanev](entities/personas/ENT-stanev.md) | Aleksandr Stanev | 3 | [`MEMOIRE.md`](../../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] |
| [ENT-steinbach-viktor](entities/personas/ENT-steinbach-viktor.md) | Viktor Steinbach | 3 | [`MEMOIRE.md`](../../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] |
| [ENT-steinbeck](entities/personas/ENT-steinbeck.md) | Konrad Steinbeck | 3 | [`MEMOIRE.md`](../../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] |
| [ENT-steiner](entities/personas/ENT-steiner.md) | Dimitri Steiner | 3 | [`MEMOIRE.md`](../../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] |
| [ENT-stepanenko](entities/personas/ENT-stepanenko.md) | Mariya Stepanenko | 3 | [`MEMOIRE.md`](../../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] |
| [ENT-stoph](entities/personas/ENT-stoph.md) | Dominic Stoph | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-strutz](entities/personas/ENT-strutz.md) | Prof. Veronika Strutz | 3 | [`MEMOIRE.md`](../../../ANALYSTE/BOTHNIA/MEMOIRE.md) | [[ENT-bothnia]] |
| [ENT-tapeur](entities/personas/ENT-tapeur.md) | Peter Tapeur | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-tarasov](entities/personas/ENT-tarasov.md) | Emanuele Tarasov | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-thiebaut](entities/personas/ENT-thiebaut.md) | Bernard Thiebaut | 3 | [`MEMOIRE.md`](../../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] |
| [ENT-thinnes](entities/personas/ENT-thinnes.md) | Edric Thinnes | 3 | [`MEMOIRE.md`](../../../ANALYSTE/BOTHNIA/MEMOIRE.md) | [[ENT-bothnia]] |
| [ENT-thulin](entities/personas/ENT-thulin.md) | Dr Leopold Thulin | 3 | [`MEMOIRE.md`](../../../ANALYSTE/BOTHNIA/MEMOIRE.md) | [[ENT-bothnia]] |
| [ENT-tikhanov](entities/personas/ENT-tikhanov.md) | Svetlana Tikhanov | 2 | [`MEMOIRE.md`](../../../ANALYSTE/BOTHNIA/MEMOIRE.md) | [[ENT-bothnia]] [[ENT-saniki]] [[LESSON-001]] [[LESSON-006]] |
| [ENT-toti](entities/personas/ENT-toti.md) | Paolo Toti | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-tsikhanouski](entities/personas/ENT-tsikhanouski.md) | Ihar Tsikhanouski | 3 | [`MEMOIRE.md`](../../../ANALYSTE/BOTHNIA/MEMOIRE.md) | [[ENT-bothnia]] |
| [ENT-turchyn](entities/personas/ENT-turchyn.md) | Anton Turchyn | 3 | [`MEMOIRE.md`](../../../ANALYSTE/BOTHNIA/MEMOIRE.md) | [[ENT-bothnia]] |
| [ENT-uhlmensch](entities/personas/ENT-uhlmensch.md) | Vensel Uhlmensch | 3 | [`MEMOIRE.md`](../../../ANALYSTE/BOTHNIA/MEMOIRE.md) | [[ENT-bothnia]] |
| [ENT-urban](entities/personas/ENT-urban.md) | Wiktoria Urban | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-urban-franziska](entities/personas/ENT-urban-franziska.md) | Franziska Urban | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-vasilevich](entities/personas/ENT-vasilevich.md) | Raman Vasilevich | 3 | [`MEMOIRE.md`](../../../ANALYSTE/BOTHNIA/MEMOIRE.md) | [[ENT-bothnia]] |
| [ENT-vasilieva](entities/personas/ENT-vasilieva.md) | Elena Vasilieva | 3 | [`MEMOIRE.md`](../../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] |
| [ENT-vassielvski](entities/personas/ENT-vassielvski.md) | Piotr Vassielvski | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-vassiliev](entities/personas/ENT-vassiliev.md) | Sergueï Vassiliev | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-velkova](entities/personas/ENT-velkova.md) | Tatiana Velkova | 3 | [`MEMOIRE.md`](../../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] |
| [ENT-viklund](entities/personas/ENT-viklund.md) | Oskar Viklund | 3 | [`MEMOIRE.md`](../../../ANALYSTE/BOTHNIA/MEMOIRE.md) | [[ENT-bothnia]] [[ENT-nyberg]] [[ENT-eklund]] |
| [ENT-viktorovitch](entities/personas/ENT-viktorovitch.md) | Vladimir Viktorovitch | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-vinogradov](entities/personas/ENT-vinogradov.md) | Moritz Vinogradov | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-vogel](entities/personas/ENT-vogel.md) | Alexandre Vogel | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-vogelnyk](entities/personas/ENT-vogelnyk.md) | Katerina Vogelnyk | 3 | [`MEMOIRE.md`](../../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] |
| [ENT-voldyski](entities/personas/ENT-voldyski.md) | Markus Voldyski | 3 | [`MEMOIRE.md`](../../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] |
| [ENT-volkonsky](entities/personas/ENT-volkonsky.md) | Piotr Volkonsky | 2 | [`MEMOIRE.md`](../../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] [[ENT-savchenko]] [[LESSON-001]] |
| [ENT-volkov-alessia](entities/personas/ENT-volkov-alessia.md) | Alessia Volkov | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-volkov-ivan](entities/personas/ENT-volkov-ivan.md) | Ivan Volkov | 3 | [`MEMOIRE.md`](../../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] |
| [ENT-voloshyn](entities/personas/ENT-voloshyn.md) | Irina Voloshyn | 3 | [`MEMOIRE.md`](../../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] |
| [ENT-vong](entities/personas/ENT-vong.md) | Vong | 3 | [`MEMOIRE.md`](../../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] |
| [ENT-vostrikov](entities/personas/ENT-vostrikov.md) | Alexei Vostrikov | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-vrenko](entities/personas/ENT-vrenko.md) | Tomaš Vrenko | 3 | [`MEMOIRE.md`](../../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] |
| [ENT-vukovic](entities/personas/ENT-vukovic.md) | Stanislav Vuković | 3 | [`MEMOIRE.md`](../../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] |
| [ENT-vydra](entities/personas/ENT-vydra.md) | Marta Vydra | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-wagner-natalia](entities/personas/ENT-wagner-natalia.md) | Natalia Wagner | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-wallner](entities/personas/ENT-wallner.md) | Niklas Wallner | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-weber](entities/personas/ENT-weber.md) | Henri Weber | 3 | [`MEMOIRE.md`](../../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] |
| [ENT-weber-dorit](entities/personas/ENT-weber-dorit.md) | Dorit Weber | 3 | [`MEMOIRE.md`](../../../ANALYSTE/BOTHNIA/MEMOIRE.md) | [[ENT-bothnia]] |
| [ENT-weiss](entities/personas/ENT-weiss.md) | Aleksandr Weiss | 3 | [`MEMOIRE.md`](../../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] |
| [ENT-werner](entities/personas/ENT-werner.md) | Elias Werner | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-winkler](entities/personas/ENT-winkler.md) | Sarah Winkler | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-zaitsev](entities/personas/ENT-zaitsev.md) | Konstantin Zaitsev | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-zajac](entities/personas/ENT-zajac.md) | Mateusz Zajac | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-zeelen](entities/personas/ENT-zeelen.md) | Maryam Zeelen | 3 | [`MEMOIRE.md`](../../../ANALYSTE/BOTHNIA/MEMOIRE.md) | [[ENT-bothnia]] |
| [ENT-zhivkovic](entities/personas/ENT-zhivkovic.md) | Irina Zhivković | 3 | [`MEMOIRE.md`](../../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] |
| [ENT-zhuk](entities/personas/ENT-zhuk.md) | Michal Zhuk | 3 | [`MEMOIRE.md`](../../../ANALYSTE/BOTHNIA/MEMOIRE.md) | [[ENT-bothnia]] |
| [ENT-zhukov](entities/personas/ENT-zhukov.md) | Mikhail Zhukov | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-zhukova](entities/personas/ENT-zhukova.md) | Milena Zhukova | 3 | [`MEMOIRE.md`](../../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] |
| [ENT-zimmerman](entities/personas/ENT-zimmerman.md) | Henrik Zimmerman | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |
| [ENT-zoric-kristina](entities/personas/ENT-zoric-kristina.md) | Kristina Zoric | 3 | [`MEMOIRE.md`](../../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] |
| [ENT-zoric-nikolai](entities/personas/ENT-zoric-nikolai.md) | Nikolai Zoric | 3 | [`MEMOIRE.md`](../../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] |
| [ENT-zupan](entities/personas/ENT-zupan.md) | Jasna Zupan | 3 | [`MEMOIRE.md`](../../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] |

## 📚 Savoir countrybook / doctrine

| ID | Titre | Tier | Source (vérité) | Liens |
|---|---|---|---|---|
| [REF-arnland-economie](knowledge/REF-arnland-economie.md) | Arnland — économie & énergie | 3 | [`MEMOIRE.md`](../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] [[REF-arnland-strategie]] |
| [REF-arnland-infrastructure](knowledge/REF-arnland-infrastructure.md) | Arnland — infrastructure | 3 | [`MEMOIRE.md`](../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] [[REF-arnland-economie]] |
| [REF-arnland-medias](knowledge/REF-arnland-medias.md) | Arnland — environnement informationnel | 2 | [`MEMOIRE.md`](../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] [[REF-arnland-societe]] |
| [REF-arnland-militaire](knowledge/REF-arnland-militaire.md) | Arnland — forces armées (ADF/SDF, ORBAT) | 2 | [`MEMOIRE.md`](../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] [[ENT-djobovic]] [[REF-arnland-strategie]] |
| [REF-arnland-politique](knowledge/REF-arnland-politique.md) | Arnland — régime & institutions | 3 | [`MEMOIRE.md`](../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] [[ENT-pallesson]] [[ENT-marinov]] |
| [REF-arnland-societe](knowledge/REF-arnland-societe.md) | Arnland — société & diaspora mercurienne | 2 | [`MEMOIRE.md`](../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] [[REF-arnland-strategie]] [[REF-arnland-economie]] |
| [REF-arnland-strategie](knowledge/REF-arnland-strategie.md) | Arnland — tensions & posture narrative | 2 | [`MEMOIRE.md`](../../ANALYSTE/ARNLAND/MEMOIRE.md) | [[ENT-arnland]] [[REF-arnland-societe]] [[REF-arnland-militaire]] |
| [REF-bothnia-economie](knowledge/REF-bothnia-economie.md) | Bothnia — économie & énergie | 3 | [`MEMOIRE.md`](../../ANALYSTE/BOTHNIA/MEMOIRE.md) | [[ENT-bothnia]] [[REF-bothnia-strategie]] |
| [REF-bothnia-infrastructure](knowledge/REF-bothnia-infrastructure.md) | Bothnia — infrastructure | 3 | [`MEMOIRE.md`](../../ANALYSTE/BOTHNIA/MEMOIRE.md) | [[ENT-bothnia]] [[REF-bothnia-economie]] |
| [REF-bothnia-medias](knowledge/REF-bothnia-medias.md) | Bothnia — médias (vecteurs ILI) | 2 | [`MEMOIRE.md`](../../ANALYSTE/BOTHNIA/MEMOIRE.md) | [[ENT-bothnia]] [[REF-bothnia-societe]] |
| [REF-bothnia-militaire](knowledge/REF-bothnia-militaire.md) | Bothnia — forces armées (BNDF, ORBAT) | 2 | [`MEMOIRE.md`](../../ANALYSTE/BOTHNIA/MEMOIRE.md) | [[ENT-bothnia]] [[REF-bothnia-strategie]] |
| [REF-bothnia-politique](knowledge/REF-bothnia-politique.md) | Bothnia — régime & institutions | 3 | [`MEMOIRE.md`](../../ANALYSTE/BOTHNIA/MEMOIRE.md) | [[ENT-bothnia]] [[ENT-peters]] [[ENT-tikhanov]] |
| [REF-bothnia-societe](knowledge/REF-bothnia-societe.md) | Bothnia — société & diaspora (leviers narratifs) | 2 | [`MEMOIRE.md`](../../ANALYSTE/BOTHNIA/MEMOIRE.md) | [[ENT-bothnia]] [[REF-bothnia-strategie]] |
| [REF-bothnia-strategie](knowledge/REF-bothnia-strategie.md) | Bothnia — stratégie & posture régionale | 2 | [`MEMOIRE.md`](../../ANALYSTE/BOTHNIA/MEMOIRE.md) | [[ENT-bothnia]] [[REF-bothnia-economie]] [[REF-bothnia-societe]] |
| [REF-mercure-economie](knowledge/REF-mercure-economie.md) | Mercure — économie & arme gazière | 2 | [`MEMOIRE.md`](../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] [[REF-mercure-relations]] |
| [REF-mercure-information](knowledge/REF-mercure-information.md) | Mercure — environnement informationnel & médias d'influence | 2 | [`MEMOIRE.md`](../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] [[REF-storm1516]] [[REF-mercure-politique]] |
| [REF-mercure-militaire](knowledge/REF-mercure-militaire.md) | Mercure — forces armées (FAM) | 2 | [`MEMOIRE.md`](../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] [[ENT-numelin]] [[ENT-mizintsev]] [[REF-mercure-relations]] |
| [REF-mercure-politique](knowledge/REF-mercure-politique.md) | Mercure — régime & pouvoir | 3 | [`MEMOIRE.md`](../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] [[ENT-olamao]] |
| [REF-mercure-relations](knowledge/REF-mercure-relations.md) | Mercure — relations internationales & infrastructure | 3 | [`MEMOIRE.md`](../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] [[ENT-bothnia]] [[ENT-arnland]] [[REF-mercure-economie]] |
| [REF-mercure-societe](knowledge/REF-mercure-societe.md) | Mercure — société, ethnies & diaspora | 2 | [`MEMOIRE.md`](../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] [[REF-arnland-societe]] |
| [REF-storm1516](knowledge/REF-storm1516.md) | Doctrine Storm-1516 (MOI russe — référentiel réalisme ILI) | 2 | [`MEMOIRE.md`](../../ANALYSTE/MERCURE/MEMOIRE.md) | [[ENT-mercure]] [[REF-mercure-information]] [[LESSON-001]] |

---

## 🔄 Vue live (Dataview, si Obsidian)

```dataview
TABLE type, tier, relevantFor, updated
FROM "vault"
WHERE id AND type != "daily"
SORT tier ASC, id ASC
```
