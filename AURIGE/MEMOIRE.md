# MÉMOIRE — AURIGE (Référentiel architecture exercices AURIGE)

> Créé le 26 mai 2026. Mis à jour 2026-05-31 — rôle d'initialisateur formalisé.
> Ce fichier est la **référence canonique** pour l'organisation de tout exercice de la série AURIGE.
> Il s'applique à AURIGE 2BB et à tous les exercices futurs de type AURIGE.

---

## Rôle AURIGE — Base d'initialisation des agents exercice

> **AURIGE est la source de vérité de la doctrine d'exercice CECPC.**
> Tout nouvel agent éditorial d'exercice (GUILLAUME pour 2BB, MINAUTORE pour 7BB, futurs) est **initialisé à partir du template AURIGE**.
> Template complet : `SYSTEME\PROMPTS\aurige.md`

### Éléments universels conservés dans AURIGE (transférables à tout exercice)

| Élément | Contenu |
|---|---|
| Univers Skolkan | Acteurs permanents GET, citations canoniques Olamao/Pallesson, règle "Ruthnia Bella" |
| Camps narratifs | BLEU / ROUGE / GRIS + médias fictifs associés |
| 5 LO GLM26 | LO 1→5 — référence stratégique universelle |
| Règles cohérence narrative | CLIMAX, noyau de vérité, équilibre camps, neutralité visuelle, règle LO |
| Steps PSYOPS | Step 1→2→3, escalade obligatoirement progressive |
| Catalogue séries ILI | 07.01→08.03, logique thématique constante |
| Règle H-préfixe | Codage géographique universel (ville réelle → H+nom) |
| Doctrine calibration brigade | Max 1-2 stratégiques/semaine, catalogue 15 types injects locaux |
| Architecture dossier exercice | 6 dossiers numérotés 00→05, nommage D+XX_JJ_MOIS |
| Framework agents | Qui appeler pour quoi — universel tous exercices |

### Éléments spécifiques à chaque exercice (non transférables, à compléter)

- Zone géographique et H-codes de la ZO (HNANCY, HCHATEAU-SALINS, etc.)
- Brigade ou unité entraînée (2BB, 7BB, etc.)
- Game Plan / synchromatrice (D+XX réels, dates calendaires)
- Injects produits et leur statut de production
- Acteurs locaux fictifs (commandants, maires, notables, médias locaux)

### Procédure d'initialisation d'un nouvel agent exercice

1. Copier `SYSTEME\PROMPTS\aurige.md` → créer `SYSTEME\PROMPTS\[nom_agent].md`
2. Compléter les sections ⚠️ avec les données de l'exercice (zone, brigade, dates)
3. Créer `[NOM_AGENT]\README.md` et `[NOM_AGENT]\MEMOIRE.md`
4. Remplir MEMOIRE.md avec les 5 LO, les règles narrative, le catalogue brigade (hérités d'AURIGE)
5. Enregistrer dans CLAUDE.md, CONFIG.md, ROUTAGE.md, NOYAU\MEMOIRE.md

---

## Convention — Un dossier par exercice (règle automatique)

> **À chaque nouvel exercice AURIGE, l'agent AURIGE crée automatiquement un sous-dossier `AURIGE\[NOM_EXERCICE]\` contenant un `MEMOIRE.md` spécifique à cet exercice.**

```
AURIGE\
├── MEMOIRE.md          ← Ce fichier — cadre général tous exercices
├── AURIGE_2BB\         ← Exercice 2e Brigade Blindée (en cours 2026)
│   └── MEMOIRE.md      ← État, bilan, leçons, décisions propres à 2BB
├── AURIGE_3BB\         ← À créer quand l'exercice 3BB démarre
│   └── MEMOIRE.md
└── AURIGE_[UNITE]\     ← Convention : préfixe AURIGE_ + code unité entraînée
    └── MEMOIRE.md
```

**Ce que chaque `AURIGE\[NOM_EXERCICE]\MEMOIRE.md` contient :**
- Identité de l'exercice (unité, niveau, période, chemins)
- État de production (jours produits, jours restants, gaps)
- Bilan pédagogique (leçons apprises propres à cet exercice)
- Décisions d'architecture prises pour cet exercice
- Leçons à réinjecter dans les exercices futurs

**Ce qu'il ne contient PAS** (géré par les agents spécialisés) :
- Détail éditorial des injects → `GUILLAUME\MEMOIRE.md`
- Règles techniques MASTAURIGE → `MASTAURIGE\MEMOIRE.md`
- Doctrine ILI → `EXPERT_INFLUENCE\MEMOIRE.md`

**Utilité à long terme :** quand on attaque AURIGE 3BB, AURIGE consulte `AURIGE_2BB\MEMOIRE.md` pour capitaliser sur les leçons de 2BB et ne pas répéter les mêmes erreurs.

---

## Contexte — Qu'est-ce qu'un exercice AURIGE ?

Les exercices AURIGE sont des **entraînements PC (Poste de Commandement) niveau brigade** produits par le CECPC. Ils simulent un environnement informationnel adversarial dans un théâtre fictif, avec :
- Des **injects ILI** (Lutte Informatique d'Influence) produits par les agents IA Mercure
- Des **médias fictifs** (sites HTML, tweets, articles) distribués aux stagiaires
- Un **animateur** qui pilote la diffusion des injects via un agrégateur WEB
- Des **stagiaires** (PC brigade) qui doivent détecter, analyser et contrer les manipulations informationnelles adverses

**Exercices de la série :**
| Exercice | Brigade | Statut | Agent éditorial | Dossier |
|---|---|---|---|---|
| AURIGE 2BB | 2e Brigade Blindée | En production (D+31→D+41, mai–juin 2026) | GUILLAUME | `AURIGE\AURIGE_2BB\` |
| AURIGE 7BB | 7e Brigade Blindée | En préparation — synchromatrice à ingérer (initialisé 2026-05-30) | MINAUTORE | `AURIGE\AURIGE_7BB\` |
| Futurs AURIGE | À définir | Architecture identique — réutiliser cette structure | À créer depuis template AURIGE | `AURIGE\AURIGE_[UNITE]\` |

---

## Architecture canonique — Dossier exercice AURIGE

> **Chemin type :** `D:\CECPC\PRODUCTION\EXER\AURIGE [UNITÉ]\`
> **Référence actuelle :** `D:\CECPC\PRODUCTION\EXER\AURIGE 2BB\`

Cette structure à 6 dossiers numérotés est **obligatoire pour tout exercice AURIGE**. Elle ne doit pas être modifiée sans validation.

```
AURIGE [UNITÉ]\
│
├── 00_Boites à outils\        ← Outils de l'animateur (agrégateur WEB, sites fictifs)
│   └── MASTAURIGE\            ← Agrégateur principal
│       └── WEB\               ← index_master.html + sites médias fictifs
│
├── 01_Montage exercice\       ← Documents de montage (synchromatrice, GAME PLAN, BRIEF)
│
├── 02_Ordres\                 ← Ordres d'opérations (OPORD, FRAGO, plans)
│
├── 03_Productions\            ← Toutes les productions classées
│   ├── [07.xx]\               ← Séries de production (vidéo, audio, Premiere Pro)
│   └── [D+XX_DATE]\           ← Productions WEB par jour d'exercice
│       └── MASTAURIGE_D+XX\WEB\
│
├── 04_FORAD\                  ← Documents Force Adverse (MERCURE)
│                                 Profils HVI, ordres FORAD, fiches personnages
│
└── 05_MTR\                    ← Dossier personnel conducteur d'exercice (MTR)
                                  Média brut, notes de travail, ressources personnelles
```

---

## Détail de chaque dossier

### 00_Boites à outils
Contient tous les **outils de l'animateur** — les éléments qu'il utilise pendant l'exercice pour diffuser les injects.

**Sous-dossier obligatoire : `MASTAURIGE\`**
- `WEB\index_master.html` — agrégateur principal animateur (interface de pilotage des injects)
- `WEB\images\` — images des tweets et injects
- `WEB\TRACTS\` — tracts PSYOPS
- `WEB\COURRIERS\` — courriers fictifs (maires, préfets)
- `WEB\Site [Nom]\` — un sous-dossier par média fictif (TV4, BC1, Today Mercure, Hexagone…)

> **Règle :** Ce dossier ne contient que des fichiers prêts à l'emploi. Aucun fichier de travail (Premiere Pro, PSD, etc.) ne doit s'y trouver.

---

### 01_Montage exercice
Documents de **conception et de cadrage** de l'exercice.

Contenu type :
- Synchromatrice (Excel) — planning des injects par date/heure
- GAME PLAN — phases tactiques et dynamiques population
- BRIEF animateur (PPT ou MD)
- Fiche de contexte scénario

---

### 02_Ordres
Ordres opérationnels fictifs distribués aux stagiaires.

Contenu type :
- OPORD (Operation Order)
- FRAGO (Fragmentary Order)
- Annexes renseignement

---

### 03_Productions
**Toutes les productions** — organisées selon deux logiques :

**Par série de production** (contenu vidéo/audio) :
- Nommage : `07.05\`, `07.08\`, etc. — correspond aux séries de la synchromatrice
- Contient : dossiers Premiere Pro (`pr\`), créations graphiques (`créa\`), fichiers source

**Par jour d'exercice** (distributions WEB quotidiennes) :
- Nommage : `D+31_26_MAI\`, `D+32_27_MAI\`, etc.
- Contient : snapshot WEB du jour `MASTAURIGE_D+XX\WEB\`
- Logique : chaque jour, le dossier WEB de distribution est archivé ici

**Logique du nommage `D+XX_JJ_MOIS` :**

```
D+31_26_MAI
│    │
│    └── Date calendaire réelle du jour d'exercice (JJ_MOIS)
│         → Correspond au jour réel pendant lequel l'inject est diffusé
│         → Change à chaque exercice selon le calendrier de l'édition
│
└── Jour tactique fictif de l'exercice (D+XX)
     → "D" = Jour de déclenchement de l'exercice
     → "+31" = 31e jour depuis le début du scénario fictif
     → Identique d'un exercice à l'autre si le scénario est le même
```

**Exemple AURIGE 2BB :**
| Dossier | Jour tactique | Date réelle |
|---|---|---|
| `D+31_26_MAI` | 31e jour du scénario | 26 mai 2026 |
| `D+32_27_MAI` | 32e jour du scénario | 27 mai 2026 |
| `D+40_04_JUIN` | 40e jour du scénario | 4 juin 2026 |

> **Règle inter-exercices :** Le format `D+XX_JJ_MOIS` est fixe. Seules les valeurs changent d'un exercice à l'autre (dates calendaires différentes). Le D+XX reste cohérent avec la synchromatrice de chaque exercice.

> **Règle :** Les fichiers finaux prêts à diffuser sont dans `00_Boites à outils\MASTAURIGE\WEB\`. Les productions brutes et intermédiaires sont dans `03_Productions\`.

---

### 04_FORAD
Documents de la **Force Adverse (MERCURE)** utilisés pour préparer les injects.

Contenu type :
- Profils commandants (PPTX, PDF)
- Organigramme forces FORAD
- Fiches personnages militaires et politiques
- Documents de référence FORAD (GLM26, matrice ILI)

> **Agent référent :** ANALYSTE MERCURE (profils, doctrine) + EXPERT_INFLUENCE (planification ILI)

---

### 05_MTR
Dossier **personnel du conducteur d'exercice** (MTR = initiales responsable).

Contenu libre — notes de travail, médias bruts, ressources personnelles, fichiers temporaires.

> **Règle :** Ce dossier n'est pas partagé avec les agents IA et ne fait pas partie de la production officielle. Son contenu est ignoré des processus de référencement.

---

## Convention géographique — Préfixe H

> S'applique à TOUS les exercices Mercure impliquant le territoire de Dacie Romanie / Arnland.

**Règle :** Toute ville française réelle devient **H + nom de la ville** dans le contexte de l'exercice.
Le préfixe "H" signale que l'on est dans un environnement d'exercice fictif — pas une vraie ville.

```
Paris      → HPARIS
Nancy      → HNANCY
Sarrebourg → HSARREBOURG
Lunéville  → HLUNEVILLE
Lyon       → HLYON
Marseille  → HMARSEILLE
Strasbourg → HSTRASBOURG
```

**Portée :** toutes les villes du territoire Dacie Romanie / Arnland (= France fictive dans le scénario).
**Application :** dans tous les injects, articles, tweets, discours, ordres et documents de l'exercice.

---

## Règles d'usage inter-exercices

1. **Structure obligatoire** — tout exercice AURIGE utilise ces 6 dossiers numérotés, dans cet ordre. Pas de dossier supplémentaire à la racine.
2. **Nommage `MASTAURIGE\`** — le sous-dossier d'outils dans `00_` est toujours nommé `MASTAURIGE`, quel que soit l'exercice.
3. **Séparation production / distribution** — les fichiers de travail vont dans `03_Productions\`, les fichiers prêts à l'emploi vont dans `00_Boites à outils\MASTAURIGE\WEB\`.
4. **Nommage jours** — format `D+XX_JJ_MOIS` (ex : `D+31_26_MAI`) — underscore comme séparateur, pas de tiret.
5. **05_MTR est personnel** — les agents IA n'y référencent rien et n'y lisent rien.

---

## 🔧 MÉTHODOLOGIE DE TRAVAIL (évolutive — capitalisée inter-AURIGE)

> Bonnes pratiques **transférables à TOUS les exercices AURIGE** (GUILLAUME 2BB, MINAUTORE 7BB, futurs). Découvertes sur un exercice → consignées ici pour profiter aux autres. *(Un hook `aurige_methodo_reminder.py` rappelle de faire vivre cette section.)*

1. **Le chef d'orchestre de l'exercice est LE référent** (GUILLAUME pour 2BB, MINAUTORE pour 7BB). Pour toute question « quel inject / quelle date / quel persona / quel jour / cet article est-il utilisé ? » → **le consulter EN PREMIER**, jamais un grep à l'aveugle. *(MINOTAURE l'illustre via `MINAUTORE/ETAT_EXERCICE_7BB.md`.)*
2. **Carte de référence d'exercice GÉNÉRÉE** : chaque chef devrait disposer d'une carte régénérable depuis les données réelles (calendrier D+↔date↔phase, storylines→LO, registre complet des injects code·D+·type·persona, vue par jour). → **à relancer après TOUTE modif** pour rester fiable. Modèle : `MINAUTORE/generer_etat_exercice.py`. *(À porter pour GUILLAUME 2BB.)*
3. **« Modifier un inject » = entrer DANS le document** (article/tweet/courrier HTML), pas seulement la card/dayorder : corriger TOUT le contenu pour cohérence (dates internes, corps, encarts, renvois).
4. **Cohérence des dates** : dateline d'un article = la **date D+ de sa card** ; date d'un **renvoi/related** = la date de l'**article visé** ; dates internes/décoratives (timelines, listes « recent », liens morts) = **+1 mois** (convention 2BB→7BB) ; **refs backstory en body** (ex. vote UNSC fondateur) **préservées**. ⚠ **Anti-spoiler temporel** : un renvoi *related/À lire également/more-card* ne doit JAMAIS pointer un article **postérieur** à celui qu'on lit (on ne lie pas vers le futur) → date du renvoi **≤** date de publication de l'article ; sinon **remplacer par un article antérieur** (même média de préférence) ou **retirer** (surtout si lien mort). *(Diagnostic auto possible : comparer date renvoi vs date card.)*
5. **Relecture/validation par l'agent compétent** (le chef route, ne décide pas seul) : camp/persona pays → **ANALYSTE** du pays ; effets ILI/PSYOPS/synchromatrice/LO → **EXPERT_INFLUENCE** ; rédaction (voix locale, tracts, courriers) → **SCÉNARISTE** ; format RS/HTML → **MASTAURIGE**. Rapporter « validé/corrigé par X ».
6. **Personas locaux crédibles** : un relais pro-MER local ne s'auto-désigne jamais « Citoyen/Patriote MER » (= propagande repérable) → **habitant / diaspora locale** ; ton « notre ville, nos droits », jamais « vive MER ».

---

## Correspondance agents IA ↔ dossiers

| Dossier | Agent(s) concerné(s) | Usage |
|---|---|---|
| `00_Boites à outils\MASTAURIGE\WEB\` | **MASTAURIGE**, **GUILLAUME** | Production et intégration des injects dans index_master.html |
| `01_Montage exercice\` | **GUILLAUME**, **EXPERT_INFLUENCE** | Lecture synchromatrice, GAME PLAN |
| `02_Ordres\` | **ANALYSTE ARNLAND**, **ANALYSTE MERCURE** | Référence contexte tactique |
| `03_Productions\` | **MASTAURIGE** (WEB jour), **IMAGIER**, **CINÉASTE** | Archivage productions |
| `04_FORAD\` | **ANALYSTE MERCURE**, **EXPERT_INFLUENCE** | Profils HVI, doctrine |
| `05_MTR\` | Aucun agent | Personnel MTR uniquement |

### Relation AURIGE ↔ GUILLAUME — Hiérarchie logique

> **GUILLAUME est l'orchestrateur éditorial de AURIGE 2BB** — il opère dans le cadre défini par AURIGE mais est structuré comme un agent racine pour des raisons opérationnelles (toutes les références inter-agents pointent vers `GUILLAUME\MEMOIRE.md`).

**Hiérarchie conceptuelle (pas structurelle) :**
```
AURIGE  (cadre de référence — architecture, règles, conventions)
  └── GUILLAUME  (orchestrateur éditorial — calendrier, LO, cohérence narrative)
        └── MASTAURIGE  (production technique — injects, HTML, MELMIL)
```

Pour un futur exercice AURIGE, un nouvel orchestrateur éditorial serait créé au même niveau racine (ex : `GUILLAUME_AURIGE3BB\`) plutôt que comme sous-dossier d'AURIGE — cela préserve la cohérence des références inter-agents.

---

---

## ⚠ DOCTRINE CALIBRATION — Niveau brigade (ajout 2026-05-29)

> **AURIGE entraîne un PC de niveau BRIGADE — pas une division, pas un état-major.**
> Tous les injects doivent être calibrés pour que le PC brigade puisse les traiter à son niveau.

### Bilan D+31→D+34 AURIGE 2BB : niveau trop élevé

La première semaine a produit des injects utiles pour poser un cadre, mais inadaptés au niveau brigade :
- Discours présidents (Olamao, Pallesson, Youkachenko, Rutte) → **niveau stratégique — hors périmètre brigade**
- Articles médias nationaux/internationaux → **niveau opératif/stratégique**
- Escalade diplomatique RB → **trop loin du terrain de la brigade**

### Règle canonique — équilibre brigade

> **Le PC brigade reçoit quelques injects politiques/stratégiques pour CONTEXTE SEULEMENT (1-2/semaine max). Tous les autres injects doivent toucher DIRECTEMENT sa Zone d'Opérations, ses soldats, sa relation avec la population locale.**

### Catalogue des injects de niveau brigade

**Terrain / visuel :**
- Manifestation locale dans une ville de la ZO (photo + tweet civil)
- Drapeau ennemi sur l'hôtel de ville
- Tags/graffitis anti-brigade ("2BB go home", "MER libérateurs")
- Vandalisme contre la brigade (véhicules, portails, matériel)
- Présence de personnel pro-MER de plus en plus visible dans la ZO

**Parole / discours local :**
- Sermon véhément d'un curé/imam contre la force
- Plainte directe du maire au commandant de brigade (courrier HTML)
- Déclaration hostile d'un notable local (médecin, conseiller municipal)
- Affluence record à la messe (signal de rejet collectif)

**Médias locaux / intercommunaux :**
- Article journal local hostile (L'Est Républicain fictif, Le Républicain Lorrain fictif)
- Retranscription radio locale (Radio Moselle fictive, France Bleu Lorraine Nord fictif)
- Produits RS humiliants (mèmes, montages, vidéos courtes ridiculisant la brigade)
- Tract pro-MER distribué dans les rues de la ZO

**Criblage / personnels :**
- Pages LinkedIn fictives d'agents MER présents dans la ZO (à créer)
- Pages Wikipedia fictives pour personnages de l'exercice (à créer)
- Signalement citoyen de personnels suspects

### Villes ZO AURIGE 2BB — priorité injects locaux

| Ville fictive | Usage | Priorité inject local |
|---|---|---|
| **HCHATEAU-SALINS** | Combat retardateur D+31-34 | **HAUTE** |
| **HLUNEVILLE** | Population D+32-34 | **HAUTE** |
| **HSARREBOURG** | Climax D+35 | **HAUTE** |
| **HToul / HCommercy** | NRBC D+34 | **HAUTE** |
| HNANCY | Logistique | Modérée (trop grande = division) |
| HPHALSBOURG | D+37+ | Modérée |

### Futurs développements (roadmap)
- [ ] Pages LinkedIn fictives — criblage OSINT pour stagiaires
- [ ] Pages Wikipedia fictives — crédibilisation personnalités
- [ ] Journal local HTML fictif (L'Est Républicain fictif)
- [ ] Radio locale fictive (retranscriptions)
- [ ] Grille cartographique pression civile par ville et D+XX

### Structure thématique pour le PC brigade

| Thème | Injects | Phase |
|---|---|---|
| Relations population | Plainte maire, sermon, RS humiliants, journal local | D+31→D+35 |
| Sécurité des arrières | Vandalisme, présence pro-MER, tags, tracts | D+31→D+40 |
| Renseignement HOS | LinkedIn fictif, signalement suspect | D+33→D+40 |
| Veille médiatique | Radio, journal, RS — surveillance locale | Permanent |
| Pression morale | RS humiliants, tracts démoralisants | D+33→D+40 |
| Ordre public | Manifestation, drapeau, graffitis | D+35→D+38 |

---

## Exercice AURIGE 2BB — Référence rapide

| Info | Valeur |
|---|---|
| Chemin racine | `D:\CECPC\PRODUCTION\EXER\AURIGE 2BB\` |
| Fichier maître animateur | `00_Boites à outils\MASTAURIGE\WEB\index_master.html` |
| Synchromatrice | `01_Montage exercice\` (à vérifier) |
| Profils commandants | `04_FORAD\` — PRUNIERE (41e DIV) + ZHUKOV (43e DIV) |
| Agent éditorial | GUILLAUME |
| Agent tweets/RS | MASTAURIGE |
| Agent doctrine ILI | EXPERT_INFLUENCE |
| Agent analyse MER | ANALYSTE MERCURE |
| Agent analyse DAC/ARN | ANALYSTE ARNLAND |
