# CLAUDE.md — Maintenance du vault atomique MINERVE

> ⚠ **Subordonné au [CLAUDE.md racine](../CLAUDE.md)** (source de vérité du projet). En cas de conflit, **la racine prime**. Ce fichier ne régit QUE la couche méta `vault/`.

> **Nature du vault** : couche méta « qui lie, ne copie jamais ». Notes atomiques (1 concept, autoportantes, courtes) qui **renvoient** aux fichiers autoritaires via `source:`. Le lore in-world (camps, doctrine pays, personas) **n'est jamais** transformé en note ici — il reste chez les agents.

---

## 🔁 Au DÉMARRAGE de session (réflexe)
1. Charger **[INDEX.md](INDEX.md)** (registre des notes, tier 1 en priorité).
2. Charger la **dernière note `daily/`** (reprise du fil — section « Prochaine étape »).
3. Charger le **canvas du projet actif** (`projects/`) selon la tâche.
4. Ne PAS charger tout le vault : suivre le **tiering** (tier 1 toujours · tier 2 au besoin via `relevantFor` · tier 3 archive).

## 🟢 En FIN de session (réflexe)
1. Créer/compléter **`daily/AAAA-MM-JJ.md`** (copier `templates/daily-note.md`) : objet, avancées, décisions/leçons, **fichiers autoritaires modifiés**, prochaine étape.
2. Pour toute connaissance transversale durable apparue : créer la **note atomique** correspondante (`decisions/`, `tools/`, `lessons/`, `architecture/`, `entities/`) depuis le template — frontmatter complet (cf. **`_SCHEMA.md`**), `source:` vers le fichier autoritaire, liens `[[...]]`.
3. **Relancer `py _generer_index.py`** (régénère `INDEX.md`).
4. 🛡️ **Lancer `py valider.py`** — DOIT sortir en exit 0 (zéro erreur) avant tout commit. Le validateur fait respecter `_SCHEMA.md` : liens cassés, orphelins, id dupliqués, et la **règle anti-divergence du camp** (champ `camp` réservé aux notes `entity`).

## ✍️ Créer une note — règles
- Frontmatter YAML systématique : `id, type, title, tags, source, linkedTo, relevantFor, tier, created, updated`.
- **id** : `DECISION-XXX` / `TOOL-XXX` / `LESSON-XXX` / `ARCH-XXX` / `PROJ-xxx` / `DAILY-AAAA-MM-JJ` (incrément simple).
- **Règle d'or** : ne JAMAIS recopier le contenu d'une source autoritaire. Synthèse courte + `source:` + `[[liens]]`. Si tu te surprends à copier 3 phrases d'un `MEMOIRE.md`, mets un lien à la place.
- **Pas de note orpheline** : au moins un `linkedTo` ou une mention dans un canvas/INDEX.
- Un `[[NOTE-XXX]]` vers une note non encore créée est permis (marque un TODO de note).

## 🧭 Tiering (rechargement LLM)
- **tier 1** : INDEX, canvas du projet actif, dernière daily, règles non négociables (ex. [[ARCH-001]], [[LESSON-001]]).
- **tier 2** : decisions/tools/lessons chargés à la demande selon `relevantFor`.
- **tier 3** : archive (exercices terminés, ex. AURIGE 2BB).

## 🔗 Articulation avec l'existant
- **`source:`** pointe toujours vers la vérité (`../../AGENT/MEMOIRE.md`, `../../CLAUDE.md`, etc.).
- [MINERVE_HOME](../MINERVE_HOME.md) = carte humaine ; **INDEX** = registre des notes atomiques.
- La mémoire harness `MEMORY.md` (hors repo) reste ; `daily/` est le journal **in-repo, git-tracké** (complémentaire).
- ⚠ Ne jamais renommer/déplacer une note depuis Obsidian — passer par Claude/git (cohérence des renvois).
