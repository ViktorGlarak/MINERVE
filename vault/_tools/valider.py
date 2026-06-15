# -*- coding: utf-8 -*-
"""
valider.py — 🛡️ Gardien du vault MINERVE (Phase 0).
Fait respecter le contrat _SCHEMA.md. À lancer avant chaque commit / fin de session.

Contrôles :
  ERREURS (bloquantes, exit 1)
    - frontmatter absent / champ obligatoire manquant
    - type hors enum · id ne respectant pas le pattern du type · id dupliqué
    - tier hors {1,2,3} · created/updated non ISO
    - lien cassé ([[ID]] ou linkedTo pointant vers un id inexistant)
    - champ `camp` hors d'une note entity (règle anti-divergence du camp)
  AVERTISSEMENTS (non bloquants)
    - note orpheline (jamais référencée, hors daily/agent)
    - titre dupliqué (duplication probable)

Usage :  py valider.py        (exit 0 = OK, exit 1 = au moins une erreur)
"""
import os, re, sys, datetime

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
VAULT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # _tools/ -> vault/
SCAN_DIRS = ["decisions", "tools", "lessons", "architecture", "projects", "agents", "entities", "daily"]

REQUIRED = ["id", "type", "title", "tags", "source", "linkedTo", "relevantFor", "tier", "created", "updated"]
TYPES = {"decision", "tool", "lesson", "architecture", "project", "agent", "entity", "daily"}
ID_PAT = {
    "decision": r"^DECISION-\d{3}$", "tool": r"^TOOL-\d{3}$", "lesson": r"^LESSON-\d{3}$",
    "architecture": r"^ARCH-\d{3}$", "project": r"^PROJ-[A-Z0-9-]+$", "agent": r"^AGENT-[A-Z0-9-]+$",
    "entity": r"^ENT-[A-Za-z0-9-]+$", "daily": r"^DAILY-\d{4}-\d{2}-\d{2}$",
}

errors, warns = [], []


def err(p, m): errors.append("%s — %s" % (p, m))
def warn(p, m): warns.append("%s — %s" % (p, m))


def parse_fm(txt):
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", txt, re.S)
    if not m:
        return None, ""
    fm = {}
    for line in m.group(1).splitlines():
        mk = re.match(r"^([A-Za-z_]+)\s*:\s*(.*)$", line)
        if not mk:
            continue
        k, v = mk.group(1), mk.group(2).strip()
        if v.startswith("[") and v.endswith("]"):
            v = [x.strip() for x in v[1:-1].split(",") if x.strip()]
        fm[k] = v
    return fm, txt[m.end():]


def is_iso(d):
    try:
        datetime.date.fromisoformat(str(d)); return True
    except Exception:
        return False


def collect():
    notes = []
    for d in SCAN_DIRS:
        base = os.path.join(VAULT, d)
        if not os.path.isdir(base):
            continue
        for root, _, files in os.walk(base):
            for fn in sorted(files):
                if not fn.endswith(".md") or fn.startswith("_"):
                    continue
                p = os.path.relpath(os.path.join(root, fn), VAULT).replace("\\", "/")
                fm, body = parse_fm(open(os.path.join(root, fn), encoding="utf-8").read())
                notes.append((p, fm, body))
    return notes


def main():
    notes = collect()
    ids = {}
    titles = {}

    # 1) validation par note
    for p, fm, body in notes:
        if fm is None:
            err(p, "frontmatter absent")
            continue
        for f in REQUIRED:
            if f not in fm:
                err(p, "champ obligatoire manquant : %s" % f)
        t = fm.get("type")
        if t not in TYPES:
            err(p, "type invalide : %r" % t)
        nid = fm.get("id")
        if nid:
            if nid in ids:
                err(p, "id DUPLIQUÉ : %s (déjà dans %s)" % (nid, ids[nid]))
            else:
                ids[nid] = p
            if t in ID_PAT and not re.match(ID_PAT[t], str(nid)):
                err(p, "id %r ne respecte pas le pattern du type %s" % (nid, t))
        if str(fm.get("tier")) not in {"1", "2", "3"}:
            err(p, "tier invalide : %r" % fm.get("tier"))
        for df in ("created", "updated"):
            if df in fm and not is_iso(fm[df]):
                err(p, "%s non ISO (AAAA-MM-JJ) : %r" % (df, fm[df]))
        # ANTI-DIVERGENCE : le camp ne vit que dans une note entity (persona)
        if "camp" in fm and t != "entity":
            err(p, "champ `camp` interdit hors d'une note entity (règle propriétaire unique)")
        if fm.get("title"):
            titles.setdefault(str(fm["title"]).lower(), []).append(p)

    # 2) liens (linkedTo + [[ID]] du corps)
    referenced = set()
    for p, fm, body in notes:
        if fm is None:
            continue
        link_ids = list(fm.get("linkedTo", []) if isinstance(fm.get("linkedTo"), list) else [])
        body_ids = re.findall(r"\[\[([A-Z][A-Z0-9-]+)\]\]", body or "")
        for rid in link_ids + body_ids:
            referenced.add(rid)
            if rid not in ids:
                err(p, "lien cassé : [[%s]] (id inexistant)" % rid)

    # 3) orphelins (hors daily/agent = points d'entrée / nav)
    for p, fm, body in notes:
        if fm is None:
            continue
        if fm.get("type") in ("daily", "agent"):
            continue
        if fm.get("id") and fm["id"] not in referenced:
            warn(p, "note ORPHELINE (jamais référencée) : %s" % fm["id"])

    # 4) titres dupliqués
    for tl, ps in titles.items():
        if len(ps) > 1:
            warn(ps[1], "titre dupliqué « %s » → %s" % (tl, ", ".join(ps)))

    # rapport
    print("=== VALIDATION VAULT — %d notes ===" % len(notes))
    if errors:
        print("\n❌ ERREURS (%d) :" % len(errors))
        for e in errors:
            print("  •", e)
    if warns:
        print("\n⚠ AVERTISSEMENTS (%d) :" % len(warns))
        for w in warns:
            print("  •", w)
    if not errors and not warns:
        print("✅ Tout est conforme.")
    elif not errors:
        print("\n✅ Aucune erreur bloquante (%d avertissement(s))." % len(warns))
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
