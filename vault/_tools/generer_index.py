# -*- coding: utf-8 -*-
"""
Genere vault/INDEX.md a partir des frontmatters YAML de toutes les notes atomiques.
Aucune dependance externe (parseur frontmatter minimal). Idempotent.

Usage :  py _generer_index.py
Relance OBLIGATOIRE a chaque note creee / modifiee (cf. vault/CLAUDE.md).
"""
import os, re, sys, datetime

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
VAULT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # _tools/ -> vault/

# dossiers de notes atomiques a indexer (on EXCLUT daily/, templates/, et les fichiers racine)
NOTE_DIRS = ["decisions", "tools", "lessons", "architecture", "projects", "agents", "entities", "knowledge"]
TYPE_LABEL = {"decision": "🔧 Décisions", "tool": "🛠️ Outils", "lesson": "📚 Leçons",
              "architecture": "🏛️ Architecture", "project": "🗂️ Projets (canvas)",
              "agent": "🤖 Agents (canvas générés)", "entity": "🌍 Entités (personas · pays · doctrine)",
              "reference": "📚 Savoir countrybook / doctrine"}
TYPE_ORDER = ["decision", "tool", "lesson", "architecture", "project", "agent", "entity", "reference"]


def parse_frontmatter(path):
    """Parseur YAML minimal pour le frontmatter (--- ... ---) des notes."""
    with open(path, encoding="utf-8") as f:
        txt = f.read()
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", txt, re.S)
    if not m:
        return None
    fm = {}
    for line in m.group(1).splitlines():
        if not line.strip() or line.strip().startswith("#"):
            continue
        mk = re.match(r"^([A-Za-z_]+)\s*:\s*(.*)$", line)
        if not mk:
            continue
        key, val = mk.group(1), mk.group(2).strip()
        if val.startswith("[") and val.endswith("]"):
            val = [x.strip() for x in val[1:-1].split(",") if x.strip()]
        fm[key] = val
    return fm


def collect():
    notes = []
    for d in NOTE_DIRS:
        folder = os.path.join(VAULT, d)
        if not os.path.isdir(folder):
            continue
        for root, _, files in os.walk(folder):          # recursif (entities/personas, /pays...)
            for fn in sorted(files):
                if not fn.endswith(".md") or fn.startswith("_"):
                    continue
                p = os.path.join(root, fn)
                fm = parse_frontmatter(p)
                if not fm or "id" not in fm:
                    print("  ⚠ frontmatter manquant/invalide :", os.path.relpath(p, VAULT))
                    continue
                fm["_rel"] = os.path.relpath(p, VAULT).replace("\\", "/")
                notes.append(fm)
    return notes


def fmt_links(v):
    if isinstance(v, list):
        return " ".join("[[%s]]" % x for x in v) if v else "—"
    return "[[%s]]" % v if v else "—"


def build_index(notes):
    today = datetime.date.today().isoformat()
    out = []
    out.append("# 🗂️ INDEX — Vault atomique MINERVE")
    out.append("")
    out.append("> ⚙️ **Fichier généré** par `_generer_index.py` — ne pas éditer à la main.")
    out.append("> Registre des notes atomiques (couche méta « qui lie, ne copie jamais »).")
    out.append("> Le détail vit dans les fichiers `source:` ; ces notes pointent, elles ne dupliquent pas.")
    out.append("> Carte humaine du système : [MINERVE_HOME](../MINERVE_HOME.md) · Source de vérité : [CLAUDE.md](../CLAUDE.md)")
    out.append("")
    out.append("**%d notes** · généré le %s" % (len(notes), today))
    out.append("")

    # Tier 1 d'abord (chargement prioritaire LLM)
    t1 = [n for n in notes if str(n.get("tier", "")) == "1"]
    if t1:
        out.append("## ⭐ Tier 1 — à charger en priorité")
        out.append("")
        out.append("| ID | Titre | Type | relevantFor |")
        out.append("|---|---|---|---|")
        for n in sorted(t1, key=lambda x: x["id"]):
            out.append("| [%s](%s) | %s | %s | %s |" % (
                n["id"], n["_rel"], n.get("title", ""), n.get("type", ""),
                ", ".join(n["relevantFor"]) if isinstance(n.get("relevantFor"), list) else n.get("relevantFor", "")))
        out.append("")

    # Par type
    for t in TYPE_ORDER:
        sub = [n for n in notes if n.get("type") == t]
        if not sub:
            continue
        out.append("## %s" % TYPE_LABEL.get(t, t))
        out.append("")
        out.append("| ID | Titre | Tier | Source (vérité) | Liens |")
        out.append("|---|---|---|---|---|")
        for n in sorted(sub, key=lambda x: x["id"]):
            src = n.get("source", "")
            src_cell = "[`%s`](%s)" % (os.path.basename(str(src)), src) if src else "—"
            out.append("| [%s](%s) | %s | %s | %s | %s |" % (
                n["id"], n["_rel"], n.get("title", ""), n.get("tier", ""),
                src_cell, fmt_links(n.get("linkedTo", "—"))))
        out.append("")

    # Bloc Dataview (live Obsidian, complementaire)
    out.append("---")
    out.append("")
    out.append("## 🔄 Vue live (Dataview, si Obsidian)")
    out.append("")
    out.append("```dataview")
    out.append("TABLE type, tier, relevantFor, updated")
    out.append('FROM "vault"')
    out.append("WHERE id AND type != \"daily\"")
    out.append("SORT tier ASC, id ASC")
    out.append("```")
    out.append("")
    return "\n".join(out)


def main():
    notes = collect()
    idx = build_index(notes)
    with open(os.path.join(VAULT, "INDEX.md"), "w", encoding="utf-8") as f:
        f.write(idx)
    print("INDEX.md genere :", len(notes), "notes")


if __name__ == "__main__":
    main()
