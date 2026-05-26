# MÉMOIRE — AURIGE (Référentiel architecture exercices AURIGE)

> Créé le 26 mai 2026.
> Ce fichier est la **référence canonique** pour l'organisation de tout exercice de la série AURIGE.
> Il s'applique à AURIGE 2BB et à tous les exercices futurs de type AURIGE.

---

## Contexte — Qu'est-ce qu'un exercice AURIGE ?

Les exercices AURIGE sont des **entraînements PC (Poste de Commandement) niveau brigade** produits par le CECPC. Ils simulent un environnement informationnel adversarial dans un théâtre fictif, avec :
- Des **injects ILI** (Lutte Informatique d'Influence) produits par les agents IA Mercure
- Des **médias fictifs** (sites HTML, tweets, articles) distribués aux stagiaires
- Un **animateur** qui pilote la diffusion des injects via un agrégateur WEB
- Des **stagiaires** (PC brigade) qui doivent détecter, analyser et contrer les manipulations informationnelles adverses

**Exercices de la série :**
| Exercice | Brigade | Statut |
|---|---|---|
| AURIGE 2BB | 2e Brigade Blindée | En production (D+31→D+41, mai–juin 2026) |
| Futurs AURIGE | À définir | Architecture identique — réutiliser cette structure |

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

## Correspondance agents IA ↔ dossiers

| Dossier | Agent(s) concerné(s) | Usage |
|---|---|---|
| `00_Boites à outils\MASTAURIGE\WEB\` | **MASTAURIGE**, **GUILLAUME** | Production et intégration des injects dans index_master.html |
| `01_Montage exercice\` | **GUILLAUME**, **EXPERT_INFLUENCE** | Lecture synchromatrice, GAME PLAN |
| `02_Ordres\` | **ANALYSTE ARNLAND**, **ANALYSTE MERCURE** | Référence contexte tactique |
| `03_Productions\` | **MASTAURIGE** (WEB jour), **IMAGIER**, **CINÉASTE** | Archivage productions |
| `04_FORAD\` | **ANALYSTE MERCURE**, **EXPERT_INFLUENCE** | Profils HVI, doctrine |
| `05_MTR\` | Aucun agent | Personnel MTR uniquement |

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
