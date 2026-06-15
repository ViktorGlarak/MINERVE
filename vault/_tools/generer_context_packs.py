# -*- coding: utf-8 -*-
"""
generer_context_packs.py — produit vault/context-packs/PACK-<domaine>.md
Un « pack » = manifeste de rechargement LLM : pour travailler sur un domaine, voici
les notes (triees par tier) + les fichiers autoritaires (`source:`) a ouvrir.
Derive du champ `relevantFor` des notes. Les packs ne sont PAS des notes (pas indexes/valides).
"""
import os, re, sys, datetime, unicodedata

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
VAULT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NOTE_DIRS = ["decisions", "tools", "lessons", "architecture", "projects", "agents", "entities", "knowledge"]
MIN_NOTES = 2  # pas de pack pour un domaine a 1 seule note


def slug(s):
    s = "".join(c for c in unicodedata.normalize("NFD", s.lower()) if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


def parse_fm(path):
    txt = open(path, encoding="utf-8").read()
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", txt, re.S)
    if not m:
        return None
    fm = {}
    for line in m.group(1).splitlines():
        mk = re.match(r"^([A-Za-z_]+)\s*:\s*(.*)$", line)
        if not mk:
            continue
        k, v = mk.group(1), mk.group(2).strip()
        if v.startswith("[") and v.endswith("]"):
            v = [x.strip() for x in v[1:-1].split(",") if x.strip()]
        fm[k] = v
    return fm


def collect():
    notes = []
    for d in NOTE_DIRS:
        base = os.path.join(VAULT, d)
        if not os.path.isdir(base):
            continue
        for root, _, files in os.walk(base):
            for fn in sorted(files):
                if not fn.endswith(".md") or fn.startswith("_"):
                    continue
                fm = parse_fm(os.path.join(root, fn))
                if not fm or "id" not in fm:
                    continue
                fm["_rel"] = os.path.relpath(os.path.join(root, fn), VAULT).replace("\\", "/")
                notes.append(fm)
    return notes


def aslist(v):
    return v if isinstance(v, list) else ([v] if v else [])


def main():
    notes = collect()
    by_dom = {}
    for n in notes:
        for dom in aslist(n.get("relevantFor")):
            by_dom.setdefault(dom, []).append(n)

    folder = os.path.join(VAULT, "context-packs")
    os.makedirs(folder, exist_ok=True)
    for fn in os.listdir(folder):
        if fn.startswith("PACK-") or fn == "_README.md":
            os.remove(os.path.join(folder, fn))

    today = datetime.date.today().isoformat()
    made = []
    for dom, ns in sorted(by_dom.items()):
        if len(ns) < MIN_NOTES:
            continue
        ns = sorted(ns, key=lambda x: (str(x.get("tier", "9")), x["id"]))
        sources = []
        for n in ns:
            s = str(n.get("source", "")).strip().strip('"')
            if s and s not in sources:
                sources.append(s)
        out = ["# 📦 Context-pack — %s" % dom, "",
               "> ⚙️ Généré (`generer_context_packs.py`). **À charger pour travailler sur « %s ».**" % dom,
               "> Notes triées par tier (1 = prioritaire). Les fichiers `source:` sont la vérité à ouvrir.",
               "> Généré le %s · %d notes." % (today, len(ns)), "",
               "## Notes (par tier)", "",
               "| Tier | ID | Titre | Type |", "|---|---|---|---|"]
        for n in ns:
            out.append("| %s | [%s](../%s) | %s | %s |" % (
                n.get("tier", ""), n["id"], n["_rel"], n.get("title", ""), n.get("type", "")))
        out += ["", "## 📄 Fichiers autoritaires à ouvrir (sources)", ""]
        out += (["- [`%s`](%s)" % (os.path.basename(s), s) for s in sources] if sources
                else ["- *(aucune source externe)*"])
        out.append("")
        open(os.path.join(folder, "PACK-%s.md" % slug(dom)), "w", encoding="utf-8").write("\n".join(out))
        made.append((dom, len(ns)))

    # overview
    ov = ["# 📦 Context-packs — vue d'ensemble", "",
          "> Généré. Chaque pack = bundle de rechargement LLM pour un domaine.", "",
          "| Domaine | Notes | Pack |", "|---|---|---|"]
    for dom, c in made:
        ov.append("| %s | %d | [PACK-%s](PACK-%s.md) |" % (dom, c, slug(dom), slug(dom)))
    ov.append("")
    open(os.path.join(folder, "_README.md"), "w", encoding="utf-8").write("\n".join(ov))
    print("context-packs generes :", len(made))


if __name__ == "__main__":
    main()
