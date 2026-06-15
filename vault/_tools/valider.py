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
import os, re, sys, datetime, unicodedata, json

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
VAULT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # _tools/ -> vault/
ROOT = os.path.dirname(VAULT)  # racine du projet MINERVE
# camp affiché -> camp canonique (emoji = signal fiable ; 🟢 = neutre/pro-MER d'État)
EMOJI_CAMP = {"🔴": "rouge", "🔵": "bleu", "⚪": "neutre", "🟢": "neutre"}
# bios.js du trombino (hors repo) — cross-check dur si présent
BIOS_JS = r"D:\CECPC\MASTAURIGE\LOCALSTORAGE_WEB_VERSION\Sites\Trombinoscope\bios.js"
# mémoires « vérité exhaustive » à surveiller (cohérence du camp)
MEMOIRES = [os.path.join(ROOT, "ANALYSTE", p, "MEMOIRE.md") for p in ("MERCURE", "ARNLAND", "BOTHNIA")] + \
           [os.path.join(ROOT, "MASTAURIGE", "MEMOIRE.md")]


def _norm(s):
    s = unicodedata.normalize("NFD", (s or "").lower())
    return re.sub(r"[^a-z]", "", "".join(c for c in s if not unicodedata.combining(c)))
SCAN_DIRS = ["decisions", "tools", "lessons", "architecture", "projects", "agents", "entities", "knowledge", "daily"]

REQUIRED = ["id", "type", "title", "tags", "source", "linkedTo", "relevantFor", "tier", "created", "updated"]
TYPES = {"decision", "tool", "lesson", "architecture", "project", "agent", "entity", "reference", "daily"}
ID_PAT = {
    "decision": r"^DECISION-\d{3}$", "tool": r"^TOOL-\d{3}$", "lesson": r"^LESSON-\d{3}$",
    "architecture": r"^ARCH-\d{3}$", "project": r"^PROJ-[A-Z0-9-]+$", "agent": r"^AGENT-[A-Z0-9-]+$",
    "entity": r"^ENT-[A-Za-z0-9-]+$", "reference": r"^REF-[A-Za-z0-9-]+$", "daily": r"^DAILY-\d{4}-\d{2}-\d{2}$",
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

    # 5) ANTI-CONFLIT : le camp d'un persona (autorité = note entity) ne doit
    #    contredire AUCUNE source externe (bios.js en dur ; MEMOIRE en avertissement).
    check_camp_coherence(notes)


def check_camp_coherence(notes):
    # camps autorité = notes entity persona
    ent = {}           # norm(nom) -> (camp, id, nom)
    last_count = {}
    for p, fm, body in notes:
        if fm and fm.get("type") == "entity" and fm.get("camp"):
            nom = str(fm.get("title", ""))
            ent[_norm(nom)] = (fm["camp"], fm["id"], nom)
            last_count[_norm(nom.split()[-1])] = last_count.get(_norm(nom.split()[-1]), 0) + 1
    if not ent:
        return

    # (a) bios.js — cross-check DUR (si le fichier est présent sur la machine)
    if os.path.exists(BIOS_JS):
        try:
            raw = open(BIOS_JS, encoding="utf-8").read()
            data = json.loads(raw.split("=", 1)[1].rsplit(";", 1)[0])
            for b in data.values():
                k = _norm(b.get("nom", ""))
                if k in ent and b.get("camp") and b["camp"] != ent[k][0]:
                    err("bios.js", "camp %s = « %s » mais entité %s = « %s » (CONTRADICTION)"
                        % (b.get("nom"), b["camp"], ent[k][1], ent[k][0]))
        except Exception as e:
            warn("bios.js", "non analysable (%s)" % e)

    # (b) MEMOIRE.md — avertissement par PROXIMITÉ : un emoji de camp dont la
    #     fenêtre ±40 caractères contient le nom d'UN seul persona, avec mismatch.
    #     (évite les faux positifs des lignes multi-sujets et des noms courts)
    def low(s):
        return "".join(c for c in unicodedata.normalize("NFD", s.lower()) if not unicodedata.combining(c))
    # jetons de nom par entité : nom complet + nom de famille unique (longueur ≥ 5)
    tokens = []  # (jeton_low, camp, id, nom)
    for k, (camp, eid, nom) in ent.items():
        full = low(nom).strip()
        if len(full.replace(" ", "")) >= 5:
            tokens.append((full, camp, eid, nom))
        last = low(nom.split()[-1])
        if len(last) >= 5 and last_count.get(_norm(nom.split()[-1])) == 1:
            tokens.append((last, camp, eid, nom))
    W = 40
    for mf in MEMOIRES:
        if not os.path.exists(mf):
            continue
        rel = os.path.relpath(mf, ROOT).replace("\\", "/")
        for i, line in enumerate(open(mf, encoding="utf-8"), 1):
            if re.search(r"@[A-Za-z0-9_]", line):
                continue          # ligne d'avatar (camp = registre avatars.js, hors périmètre entités pays)
            ll = low(line)
            for pos, ch in enumerate(line):
                if ch not in EMOJI_CAMP:
                    continue
                lcamp = EMOJI_CAMP[ch]
                win = ll[max(0, pos - W):pos + W]
                hits = {(c, eid, nom) for tok, c, eid, nom in tokens if tok and tok in win}
                if len(hits) == 1:
                    c, eid, nom = next(iter(hits))
                    if lcamp != c:
                        warn("%s:%d" % (rel, i), "camp affiché %s ≠ entité %s (%s) — vérifier"
                             % (lcamp, c, eid))

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
