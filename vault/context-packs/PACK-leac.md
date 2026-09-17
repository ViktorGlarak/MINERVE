# 📦 Context-pack — leac

> ⚙️ Généré (`generer_context_packs.py`). **À charger pour travailler sur « leac ».**
> Notes triées par tier (1 = prioritaire). Les fichiers `source:` sont la vérité à ouvrir.
> Généré le 2026-09-17 · 6 notes.

## Notes (par tier)

| Tier | ID | Titre | Type |
|---|---|---|---|
| 1 | [ARCH-014](../architecture/ARCH-014.md) | LEAC v3 — journal d'opérations et horloge de Lamport remplacent le PC maître, la clé USB et la réplication MariaDB | architecture |
| 1 | [DECISION-024](../decisions/DECISION-024.md) | LEAC — une saisie annulée ne remonte pas ; le compactage du journal est une question de justesse, pas de volume | decision |
| 2 | [DECISION-021](../decisions/DECISION-021.md) | LEAC — on écrit un CHAMP par cible, jamais un objet entier ; c'est la granularité qui achète l'absence de conflit | decision |
| 2 | [DECISION-022](../decisions/DECISION-022.md) | LEAC — le « drapeau » devient un choix explicite et un filtre réel, il ne dépend plus d'un ordre de clic | decision |
| 2 | [DECISION-023](../decisions/DECISION-023.md) | LEAC — figer un cycle est un état métier, jamais un verrou d'écriture sur le journal | decision |
| 2 | [LESSON-034](../lessons/LESSON-034.md) | « Pas de note » n'est pas « zéro » — la confusion est invisible à l'œil et fait déclarer un PC inapte | lesson |

## 📄 Fichiers autoritaires à ouvrir (sources)

- [`MEMOIRE.md`](../../LEAC/MEMOIRE.md)
