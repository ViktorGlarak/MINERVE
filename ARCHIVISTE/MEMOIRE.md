# MÉMOIRE — ARCHIVISTE

## Règle fondamentale
Toujours consulter D:\CECPC\PRODUCTION\BDA\_CATALOGUE.md avant de suggérir la création d'un nouvel asset.
Si un asset similaire existe, le proposer à l'utilisateur ou l'adapter plutôt que recréer.

## ⚠ RÈGLE SYSTÈME — 2026-05-29

### Règle MASTAURIGE — images dans l'écosystème
Les images utilisées dans l'écosystème MASTAURIGE (`...\MASTAURIGE\WEB\images\`) sont sous la responsabilité de MASTAURIGE. ARCHIVISTE référence ces assets dans la BDA — mais pour leur intégration dans les fichiers MASTAURIGE, MASTAURIGE est consulté.

### Chemin dossier images MASTAURIGE AURIGE 2BB
`D:\CECPC\PRODUCTION\EXER\AURIGE 2BB\00_Boites à outils\MASTAURIGE\WEB\images\`

Sous-dossier avatars tweet : `images\avatars tweet\`

### Doctrine calibration brigade
À partir de D+35 AURIGE 2BB, les assets image à créer en priorité sont des visuels locaux brigade (tags, manifestations, vandalisme, tracts sur murs) — voir `AURIGE/MEMOIRE.md` section "Catalogue injects brigade".

---

## Assets connus — Groupes fictifs

### N.O.M (Novus Ordo Mundi)
- **Localisation :** D:\CECPC\PRODUCTION\BDA\02 - MERCURE\N.O.M\ (23 fichiers)
- **Exercices :** ORION 26 (O41), AURIGE 2BB (07.08)
- **Logo :** Crâne dans triangle inversé, noir/blanc, stencil style
- **Identité figée** : ne pas modifier entre les exercices
- **Contenu disponible :** affiches propagande, formulaire adhésion, lettre ouverte RNA, revendication, vidéo (NOM les lanscenets.mp4)
- **Référence détaillée :** SCENARISTE/MEMOIRE.md

---

## Assets connus — Médias fictifs
<!-- À documenter depuis 03 - LOGOS MEDIA -->

---

## Assets connus — Lieux
<!-- À alimenter au fil des productions -->

---

## Architecture canonique — Exercices AURIGE

> Ajouté le 26 mai 2026. Source : analyse dossier AURIGE 2BB + confirmation utilisateur.
> **Cette structure s'applique à TOUS les exercices de la série AURIGE, présents et futurs.**
> Référence complète : `AURIGE\MEMOIRE.md`

### Structure de dossiers obligatoire

```
AURIGE [UNITÉ]\
├── 00_Boites à outils\     ← Outils animateur — index_master.html, sites fictifs
│   └── MASTAURIGE\WEB\     ← Agrégateur principal + médias fictifs prêts à diffuser
├── 01_Montage exercice\    ← Synchromatrice, GAME PLAN, BRIEF
├── 02_Ordres\              ← OPORD, FRAGO, annexes
├── 03_Productions\         ← Productions brutes (vidéo Premiere Pro + WEB par jour)
├── 04_FORAD\               ← Documents Force Adverse (profils HVI, doctrine)
└── 05_MTR\                 ← Personnel MTR — ignoré des agents IA
```

### Règles d'archivage pour ARCHIVISTE

- **Assets prêts à diffuser** → `00_Boites à outils\MASTAURIGE\WEB\`
- **Productions brutes** (Premiere Pro, PSD, fichiers source) → `03_Productions\[07.xx]\`
- **Productions WEB par jour** → `03_Productions\D+XX_JJ_MOIS\MASTAURIGE_D+XX\WEB\`
- **Profils personnages FORAD** → `04_FORAD\`
- **05_MTR\** : jamais référencé, jamais consulté par les agents IA

### Nommage obligatoire

- Séparateur jours : **underscore uniquement** — `D+31_26_MAI` ✅ — `D+31_26-MAI` ❌
- Sous-dossier outils : toujours nommé **`MASTAURIGE`** dans `00_Boites à outils`

### Logique du nommage des dossiers jour — `D+XX_JJ_MOIS`

```
D+31_26_MAI
├── D+31  → Jour tactique fictif du scénario (31e jour depuis le déclenchement)
│            Reste stable tant que le scénario ne change pas
└── 26_MAI → Date calendaire réelle de diffusion des injects
              Change à chaque édition de l'exercice
```

Le `D+XX` provient de la synchromatrice de l'exercice. La date réelle (`JJ_MOIS`) correspond au calendrier de l'édition en cours. **Le format est fixe, les valeurs changent.**

### Exercice de référence

| Exercice | Chemin |
|---|---|
| AURIGE 2BB | `D:\CECPC\PRODUCTION\EXER\AURIGE 2BB\` |

---

## Règles de cohérence inter-exercices

### [2026-05-06] N.O.M → AURIGE 2BB scénario 07.08
L'identité N.O.M établie dans O41 doit être réutilisée telle quelle dans AURIGE 2BB.
Palette, logo, style de tag, rhétorique = identiques. Aucune variation créative non validée.
