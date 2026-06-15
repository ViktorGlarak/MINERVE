# CLAUDE.md — Maintenance du vault atomique MINERVE

> ⚠ **Subordonné au [CLAUDE.md racine](../CLAUDE.md)** (source de vérité du projet). En cas de conflit, **la racine prime**. Ce fichier ne régit QUE la couche méta `vault/`.

> **Nature du vault** : base de connaissance atomique (1 concept = 1 note autoportante) où **chaque fait a un seul propriétaire**. Les notes techniques **renvoient** aux fichiers autoritaires via `source:` (lien, jamais copie). Le contenu **in-world** (personas, pays, doctrine) est progressivement atomisé dans **`entities/`** avec propriété unique stricte (le **camp** d'un persona n'existe que dans SA note) — voir [`_SCHEMA.md`](_SCHEMA.md) et la feuille de route rework (commencer par Bothnia).

## ⚙️ Une seule commande
**`py _tools/build.py`** = génère (agents · context-packs · INDEX) **puis valide**. Sort en exit ≠ 0 si une erreur (lien cassé, duplication…). À lancer avant tout commit.
Outils dans `_tools/` : `build.py` (orchestre) · `valider.py` (🛡️ gardien) · `generer_index.py` · `generer_agents.py` · `generer_context_packs.py`.

---

## 🔁 Au DÉMARRAGE de session (réflexe) — commande **`/session_start`**
> Déclenché à la main par l'utilisateur quand il commence à travailler (`.claude/commands/session_start.md`).
1. Charger **[INDEX.md](INDEX.md)** (registre, tier 1 en priorité).
2. Charger la **dernière note `daily/`** (reprise du fil — « Prochaine étape »).
3. Charger le **context-pack du domaine** de la tâche (`context-packs/PACK-<domaine>.md`) : il liste les notes + les fichiers `source:` à ouvrir. Sinon, le **canvas** du projet/agent concerné.
4. Ne PAS charger tout le vault : suivre le **tiering** (tier 1 toujours · tier 2 au besoin via `relevantFor` · tier 3 archive).

## 🟢 En FIN de session (réflexe) — commande **`/session_end`**
> Déclenché à la main par l'utilisateur quand il termine (`.claude/commands/session_end.md`).
1. Créer/compléter **`daily/AAAA-MM-JJ.md`** (copier `templates/daily-note.md`) : objet, avancées, décisions/leçons, **fichiers autoritaires modifiés**, prochaine étape.
2. Pour toute connaissance durable apparue : créer la **note atomique** (`decisions/`, `tools/`, `lessons/`, `architecture/`, `entities/`) depuis le template — frontmatter complet (cf. **`_SCHEMA.md`**), `source:` vers le fichier autoritaire, liens `[[...]]`.
3. **Lancer `py _tools/build.py`** → régénère tout + **valide** (DOIT sortir en exit 0 avant commit). Le validateur fait respecter `_SCHEMA.md` : liens cassés, orphelins, id dupliqués, et la **règle anti-divergence du camp** (`camp` réservé aux notes `entity`).
4. **Ne pas éditer à la main** : `INDEX.md`, `agents/AGENT-*.md`, `context-packs/PACK-*.md` (tous générés).

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
