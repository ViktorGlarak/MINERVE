# MÉMOIRE — AURIGE / AURIGE_2BB (Exercice AURIGE 2BB — 2e Brigade Blindée)

> Ce fichier est géré par l'agent AURIGE.
> Il stocke l'état, les décisions d'architecture et les leçons propres à l'exercice AURIGE 2BB.
> Il est **distinct** de `GUILLAUME\MEMOIRE.md` (éditorial) et `MASTAURIGE\MEMOIRE.md` (technique).

---

## Identité de l'exercice

| Info | Valeur |
|---|---|
| Nom exercice | **AURIGE 2BB** |
| Unité entraînée | 2e Brigade Blindée |
| Niveau entraîné | **PC Brigade** |
| Code éditorial | GUILLAUME 26 (GLM26) |
| Période scénario fictif | D+31 → D+41 (26 Mai → 04 Juin 2026) |
| Chemin racine | `D:\CECPC\PRODUCTION\EXER\AURIGE 2BB\` |
| Agent éditorial | **GUILLAUME** (`GUILLAUME\MEMOIRE.md`) |
| Agent production | **MASTAURIGE** (`MASTAURIGE\MEMOIRE.md`) |
| Agent doctrine ILI | **EXPERT_INFLUENCE** |

---

## État de production — Vue AURIGE (cadre)

### Jours produits

| Jour | Date | Statut MASTAURIGE | Livrable WEB |
|---|---|---|---|
| D+31 | 26 Mai | ✅ Produit | `03_Productions\D+31_26_MAI\` |
| D+32 | 27 Mai | ✅ Produit | `03_Productions\D+32_27_MAI\` |
| D+33 | 28 Mai | ✅ Produit | `03_Productions\D+33_28_MAI\` |
| D+34 | 29 Mai | ✅ En cours | `03_Productions\D+34_29_MAI\` |
| D+35 | 30 Mai | ⏳ À produire | — |
| D+36 | 31 Mai | ⏳ À produire | — |
| D+37 | 01 Jun | ⏳ À produire | — |
| D+38 | 02 Jun | ⏳ À produire | — |
| D+39 | 03 Jun | ⏳ À produire | — |
| D+40 | 04 Jun | ⏳ À produire | — |

### Injects produits (vue globale)
- **~45 injects** dans index_master.html au 2026-05-29
- Séries couvertes : 04.01, 07.01→07.08, 08.01→08.03
- Gap critique identifié : **D+35 (HSARREBOURG)** — moment le plus important, sous-représenté

---

## Bilan pédagogique — Leçons apprises

### D+31→D+34 : niveau trop stratégique

Les injects produits pour la première semaine étaient calibrés trop haut (discours présidents, médias nationaux, escalade diplomatique). Ils conviennent pour un **PC division** mais pas pour le **PC brigade** qui est la cible de l'exercice.

**Correction à appliquer à partir de D+35 :**
- Ratio : 4 injects locaux brigade / 1 inject stratégique de cadrage par jour
- Injects locaux prioritaires : manifestation dans la ZO, plainte du maire, tags, tracts, RS humiliants, sermon hostile, journal local
- Villes cibles : HCHATEAU-SALINS, HLUNEVILLE, HSARREBOURG, HToul (pas HNANCY — trop grande = niveau division)

> Référence complète : `AURIGE\MEMOIRE.md` section "Doctrine calibration brigade"

---

## Décisions d'architecture propres à AURIGE 2BB

### Génération melmil_data.js via PS1 — validée (2026-05-29)
`Actualiser_MELMIL.bat` → `generate_data.ps1` testé et fonctionnel sur la dernière version du XLS.
**Changement notable :** 07.06 (infiltration SF OTAN) est maintenant dans le XLS — les cards 07.06.01i et 07.06.02i sont passées de ghost r7 à cards réelles r1. Entrées `MELMIL_EDITORIAL_DAYS` correspondantes nettoyées.
**Règle :** après chaque mise à jour du XLS, toujours relancer le BAT. Les positions de drag d'incidents entiers sont remises à zéro (VERSION_KEY) — normal et attendu.

### Synchronisation MELMIL ↔ index_master (2026-05-29)
Bidirectionnelle via `card-day-*` localStorage. Priorité : drag MELMIL > date selector index_master > defaults `MELMIL_SUBINJECT_DAYS`. Fonctionnel depuis `syncDayOverrides()` Sync 2 ajouté dans melmil.js.

### Convention codes injects
Format canonique `XX.YY.ZZi / XX.YY.ZZAi` — migration P-xx/R-x terminée le 2026-05-29. Injects multi-jours gérés par `MELMIL_SUBINJECT_DAYS`.

### Série 04.01 — NRBC (nouvelle, propre à 2BB)
Incident site Seveso BRENNTAG HToul instrumentalisé par MER pour accuser l'OTAN. ROW_MAP `r1`, CLASS_MAP `c41` (#BF360C). Référence pour exercices futurs impliquant des incidents NRBC.

### Série 08.02 — Captures/Redditions
- `08.02.02Ai` : TV4 capture 104 MER HNANCY (28 Mai)
- `08.02.02Bi` : @KolesnikovAndrei maltraitance POW + discrédit DAC vs FR (29 Mai)
- 08.02.01i / 08.02.03i / 08.02.04i : non encore créés (D+36)

---

## Futurs développements spécifiques AURIGE 2BB

- [ ] Pages LinkedIn fictives (agents MER dans la ZO) — D+37+
- [ ] Pages Wikipedia fictives (personnages exercice)
- [ ] Journal local HTML (L'Est Républicain fictif)
- [ ] Radio locale fictive (Radio Moselle fictive)
- [ ] Injects D+35 (CLIMAX HSARREBOURG) — gap critique à combler en priorité

---

## Leçons à injecter dans les prochains exercices AURIGE

1. **Calibrer d'emblée pour le niveau brigade** — ne pas produire de cadre stratégique avant d'avoir les injects locaux de la ZO
2. **Documenter les villes ZO dès le début** — et les assigner à des arcs narratifs distincts
3. **Synchronisation MELMIL ↔ index_master** — implémenter dès le départ, pas après coup
4. **MELMIL_SUBINJECT_DAYS** — prévoir d'emblée les injects multi-jours
5. **Ratio 4:1** (local:stratégique) — règle éditoriale à inscrire dans la synchromatrice dès le montage
