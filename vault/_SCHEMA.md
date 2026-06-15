# _SCHEMA — Contrat frontmatter GELÉ du vault MINERVE

> 🔒 **Schéma figé (Phase 0).** Toute note du vault DOIT respecter ce contrat. `valider.py` le fait respecter.
> Changer ce schéma = décision explicite + mise à jour de `valider.py` + revalidation complète.

## Règles d'or (non négociables)
1. **1 fait = 1 propriétaire = 1 note.** Aucune donnée n'existe à deux endroits. Le reste **lie** (`source:` ou `[[ID]]`), ne copie pas.
2. **1 entité = 1 note.** Un persona / un pays / un concept = une seule note autorité. Son **camp** (persona) n'est défini **que** dans sa note.
3. **Pas d'orphelin.** Toute note (hors `daily`/`agent`) est référencée au moins une fois.
4. **Lien, jamais copie.** Se surprendre à recopier 3 phrases d'une source = mettre un lien à la place.

## Champs frontmatter (TOUS obligatoires)
| Champ | Type | Règle |
|---|---|---|
| `id` | string | Unique dans tout le vault. Préfixe = type (voir ci-dessous). |
| `type` | enum | `decision` · `tool` · `lesson` · `architecture` · `project` · `agent` · `entity` · `reference` · `daily` |
| `title` | string | Court, explicite. |
| `tags` | liste `[a, b]` | Minuscules, kebab-case. |
| `source` | string | Chemin relatif vers le fichier AUTORITAIRE (`../../AGENT/MEMOIRE.md`) ou `""`. |
| `linkedTo` | liste d'`id` | Notes connexes (peut être `[]`). |
| `relevantFor` | liste | Domaines de pertinence (`mastaurige`, `exercices`, `bothnia`…). |
| `tier` | `1`\|`2`\|`3` | 1 = charge toujours · 2 = au besoin · 3 = archive. |
| `created` | date ISO | `AAAA-MM-JJ`. |
| `updated` | date ISO | `AAAA-MM-JJ`. |

### Champs ADDITIONNELS par type
- **entity (persona)** : `camp` (`rouge`\|`bleu`\|`neutre`) — **autorité unique du camp**. `pays`, `handle` (optionnels).
- **entity (pays)** : `pays` (nom). 
- **entity (doctrine)** : `lo` (optionnel, ex. `LO3`).

> ⚠ Le champ `camp` ne peut apparaître QUE dans une note `entity` persona. Toute autre occurrence = violation (le validateur la signale).

## Patterns d'`id` par type
| type | pattern | exemple |
|---|---|---|
| decision | `DECISION-NNN` | `DECISION-001` |
| tool | `TOOL-NNN` | `TOOL-001` |
| lesson | `LESSON-NNN` | `LESSON-001` |
| architecture | `ARCH-NNN` | `ARCH-001` |
| project | `PROJ-XXX` | `PROJ-MASTAURIGE` |
| agent | `AGENT-XXX` | `AGENT-MASTAURIGE` (généré) |
| entity | `ENT-XXX` | `ENT-tikhanov` · `ENT-bothnia` · `ENT-lo3` |
| reference | `REF-XXX` | `REF-bothnia-economie` · `REF-storm1516` |
| daily | `DAILY-AAAA-MM-JJ` | `DAILY-2026-06-15` |

> **reference** = savoir countrybook/doctrine structuré (économie, société, ORBAT, médias, infrastructure, doctrine ILI…) **non lié à un persona unique**. Vit dans `knowledge/`. C'est la matière qui, à terme (Phase 4), permet de générer les `MEMOIRE.md` sans perte. `source:` pointe vers la `MEMOIRE.md` d'origine.

## Liens dans le corps
- `[[ID]]` (majuscule) = lien vers une autre note → **doit résoudre** (sinon lien cassé).
- `[[../chemin/fichier.md]]` = lien fichier (autorisé, non vérifié comme id).
