# -*- coding: utf-8 -*-
"""
Genere vault/agents/AGENT-*.md (un canvas par agent) — LIENS PURS, zero duplication.
Source : la table « Navigation par agent » de ../MINERVE_HOME.md (prompt + memoire).
Rattachement agent->notes : DETERMINISTE via le champ `source:` des notes atomiques
(une note dont la source de verite est AGENT/MEMOIRE.md appartient a cet agent).

Role / modele NE SONT PAS copies : on renvoie au registre de ../CLAUDE.md.
Idempotent. Appele automatiquement par _generer_index.py.
"""
import os, re, sys, datetime, unicodedata

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
VAULT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # _tools/ -> vault/
ROOT = os.path.dirname(VAULT)
NOTE_DIRS = ["decisions", "tools", "lessons", "architecture", "projects", "entities"]


def slug(name):
    name = "".join(c for c in unicodedata.normalize("NFD", name) if not unicodedata.combining(c))
    name = re.sub(r"\(([^)]+)\)", r"-\1", name)        # "ANALYSTE (Mercure)" -> "ANALYSTE -Mercure"
    return re.sub(r"[^A-Za-z0-9]+", "-", name).strip("-").upper()


def parse_agents():
    """(nom, prompt_path, memoire_path) depuis la table de MINERVE_HOME.md."""
    home = open(os.path.join(ROOT, "MINERVE_HOME.md"), encoding="utf-8").read()
    out = []
    for m in re.finditer(r"^\|\s*([^|]+?)\s*\|\s*\[prompt\]\(([^)]+)\)\s*\|\s*\[m[ée]moire\]\(([^)]+)\)\s*\|",
                         home, re.M):
        nom, prompt, mem = m.group(1).strip(), m.group(2).strip(), m.group(3).strip()
        out.append((nom, prompt, mem))
    return out


def scan_notes():
    """[(id, type, source_root_relative, rel_path_from_agents)]"""
    notes = []
    for d in NOTE_DIRS:
        folder = os.path.join(VAULT, d)
        if not os.path.isdir(folder):
            continue
        for fn in sorted(os.listdir(folder)):
            if not fn.endswith(".md") or fn.startswith("_"):
                continue
            txt = open(os.path.join(folder, fn), encoding="utf-8").read()
            mid = re.search(r"^id:\s*(\S+)", txt, re.M)
            msrc = re.search(r"^source:\s*(.*)$", txt, re.M)
            if not mid:
                continue
            src = (msrc.group(1).strip().strip('"') if msrc else "")
            src_root = re.sub(r"^(\.\./)+", "", src).replace("\\", "/").lower()
            notes.append((mid.group(1), src_root))
    return notes


def build(nom, prompt, mem, related):
    sid = "AGENT-" + slug(nom)
    today = datetime.date.today().isoformat()
    mem_dir = os.path.dirname(mem)
    readme = (mem_dir + "/README.md") if mem_dir else "README.md"
    has = bool(related)
    fm = [
        "---",
        "id: %s" % sid,
        "type: agent",
        "title: %s" % nom,
        "tags: [agent]",
        "source: ../../%s" % mem,
        "linkedTo: [%s]" % ", ".join(related),
        "relevantFor: [agents]",
        "tier: %d" % (2 if has else 3),
        "created: %s" % today,
        "updated: %s" % today,
        "---",
        "",
        "# 🤖 %s — Canvas agent" % nom,
        "",
        "> ⚙️ **Généré** par `_generer_agents.py` — ne pas éditer à la main. Liens purs (zéro copie).",
        "> **Rôle & modèle Ollama : voir le registre** → [CLAUDE.md](../../CLAUDE.md) (source de vérité unique).",
        "",
        "## Fiches autoritaires",
        "- 🧠 Mémoire (vérité vivante) : [%s](../../%s)" % (os.path.basename(mem), mem),
        "- 🗣️ Prompt système : [%s](../../%s)" % (os.path.basename(prompt), prompt),
        "- 📄 README : [%s](../../%s)" % (os.path.basename(readme), readme),
        "",
        "## Notes atomiques rattachées (par `source:`)",
    ]
    if related:
        fm += ["- [[%s]]" % r for r in related]
    else:
        fm += ["- *(aucune note atomique transversale pour l'instant — à créer si une connaissance durable émerge)*"]
    fm += ["", "## Navigation", "- Carte du système : [MINERVE_HOME](../../MINERVE_HOME.md) · Index vault : [INDEX](../INDEX.md)", ""]
    return sid, "\n".join(fm)


def main():
    agents = parse_agents()
    notes = scan_notes()
    folder = os.path.join(VAULT, "agents")
    os.makedirs(folder, exist_ok=True)
    # nettoyage des anciens AGENT-*.md (idempotence stricte)
    for fn in os.listdir(folder):
        if fn.startswith("AGENT-") and fn.endswith(".md"):
            os.remove(os.path.join(folder, fn))
    n = 0
    for nom, prompt, mem in agents:
        mem_norm = mem.replace("\\", "/").lower()
        afolder = os.path.dirname(mem_norm)  # ex. "voix", "analyste/mercure"
        # rattache toute note dont la source vit dans le dossier de l'agent (pas que MEMOIRE.md :
        # aussi PARAMETRES_OMNIVOICE.md, PATTERNS.md, etc.)
        related = sorted(nid for nid, src in notes
                         if src and (src == mem_norm or (afolder and src.startswith(afolder + "/"))))
        sid, content = build(nom, prompt, mem, related)
        open(os.path.join(folder, sid + ".md"), "w", encoding="utf-8").write(content)
        n += 1
    print("agents generes :", n)


if __name__ == "__main__":
    main()
