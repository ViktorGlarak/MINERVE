# 🗂️ vault/ — Mémoire atomique MINERVE

> **En une phrase :** une base de connaissance en **notes atomiques** (1 concept = 1 note autoportante), **par-dessus** les dossiers d'agent existants — elle ne les remplace pas, elle les **structure** et **garantit la cohérence** (notamment les **camps**).

## Comment ça s'articule avec le reste du projet
| Couche | Rôle | Exemple |
|---|---|---|
| **Dossiers d'agent** (`ANALYSTE/`, `MASTAURIGE/`…) | **Détail exhaustif** : doctrine, ORBAT, chronologies, règles éditoriales | `ANALYSTE/BOTHNIA/MEMOIRE.md` |
| **`vault/` (ici)** | **Structure atomique + autorité du camp + navigation** | `entities/personas/ENT-tikhanov.md` |

➡️ **Pas de doublon dangereux** : pour le **camp** d'un persona, **l'autorité unique = la note entité** ; les `MEMOIRE.md` citent. `_tools/valider.py` **bloque** toute contradiction. Pour le **détail**, l'autorité = la `MEMOIRE.md`.

## Une seule commande
```
py _tools/build.py
```
→ génère (agents · context-packs · INDEX · vues mémoire) **puis valide** (liens, orphelins, duplications, **cohérence des camps**). Sort en erreur si quoi que ce soit cloche. **À lancer avant tout commit.**

## Structure
```
vault/
├── INDEX.md            # registre généré de toutes les notes
├── _SCHEMA.md          # contrat frontmatter (gelé)
├── README.md           # ce fichier
├── CLAUDE.md           # règles de maintenance (rituels session)
├── _tools/             # générateurs + validateur (build.py orchestre)
├── _vues/              # MEMOIRE générées depuis les notes (Phase 4, lecture seule)
├── daily/              # journaux de session (continuité)
├── decisions/ tools/ lessons/ architecture/   # savoir technique
├── projects/           # canvas par domaine
├── agents/             # canvas par agent (GÉNÉRÉS — ne pas éditer)
├── context-packs/      # « quoi charger pour la tâche X » (GÉNÉRÉS)
├── entities/           # personas (camp = autorité) + pays
│   ├── personas/  ENT-*.md   (champ camp: 🔴/🔵/⚪)
│   └── pays/      ENT-bothnia / arnland / mercure
├── knowledge/          # savoir countrybook/doctrine (REF-*) : éco, militaire, médias…
└── templates/          # modèles de notes
```

## Ce qui est GÉNÉRÉ (ne jamais éditer à la main)
`INDEX.md` · `agents/AGENT-*.md` · `context-packs/PACK-*.md` · `_vues/*.generee.md`
→ régénérés par `build.py`. Tout le reste est **authored** (édité à la main depuis les templates).

## Types de notes (voir `_SCHEMA.md`)
`decision` · `tool` · `lesson` · `architecture` · `project` · `agent` · `entity` · `reference` · `daily`

## État (2026-06-15)
275 notes · 196 entités (3 pays, **0 divergence de camp**) · 21 références countrybook · 19 agents · branche `vault-rework`.
