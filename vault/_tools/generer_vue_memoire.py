# -*- coding: utf-8 -*-
"""
generer_vue_memoire.py — Phase 4 (test) : assemble une MÉMOIRE « vue générée »
par pays depuis les notes atomiques (ENT-<pays> + REF-<pays>-* + personas).
Écrit dans vault/_vues/MEMOIRE_<pays>.generee.md — NE TOUCHE PAS la vraie
ANALYSTE/<PAYS>/MEMOIRE.md (comparaison avant toute bascule).

Démontre l'inversion du flux : la mémoire devient une PROJECTION des notes
(où le camp vit en autorité unique). Idempotent.
"""
import os, re, datetime

VAULT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAYS = [("bothnia", "Bothnia"), ("arnland", "Arnland"), ("mercure", "Mercure")]
CAMP_ORDER = ["rouge", "neutre", "bleu"]
CAMP_LABEL = {"rouge": "🔴 rouge", "neutre": "⚪ neutre", "bleu": "🔵 bleu"}
TODAY = datetime.date.today().isoformat()


def fm_and_body(path):
    txt = open(path, encoding="utf-8").read()
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", txt, re.S)
    if not m:
        return {}, txt
    fm = {}
    for line in m.group(1).splitlines():
        mk = re.match(r"^([A-Za-z_]+)\s*:\s*(.*)$", line)
        if mk:
            fm[mk.group(1)] = mk.group(2).strip()
    return fm, m.group(2).strip()


def strip_fm_heading(body):
    # retire le 1er titre H1 et les blockquotes de tete pour reinjecter proprement
    body = re.sub(r"^#\s+[^\n]+\n+", "", body)
    return body.strip()


def role_of(body):
    m = re.search(r"R[ôo]le\s*:\s*([^\n]+)", body)
    if m:
        return m.group(1).strip().rstrip(".")
    m = re.search(r"##\s*R[ôo]le\s*\n+([^\n]+)", body)
    return m.group(1).strip().rstrip(".") if m else ""


def collect(slug):
    pays_note, refs, personas = None, [], []
    # pays
    p = os.path.join(VAULT, "entities", "pays", "ENT-%s.md" % slug)
    if os.path.exists(p):
        fm, body = fm_and_body(p)
        pays_note = (fm, strip_fm_heading(body))
    # knowledge
    kdir = os.path.join(VAULT, "knowledge")
    for fn in sorted(os.listdir(kdir)) if os.path.isdir(kdir) else []:
        if fn.startswith("REF-%s-" % slug) and fn.endswith(".md"):
            fm, body = fm_and_body(os.path.join(kdir, fn))
            refs.append((fm, strip_fm_heading(body)))
    # personas
    pdir = os.path.join(VAULT, "entities", "personas")
    for fn in sorted(os.listdir(pdir)):
        if not fn.endswith(".md"):
            continue
        fm, body = fm_and_body(os.path.join(pdir, fn))
        if fm.get("pays", "").lower() == slug:
            personas.append((fm, role_of(body)))
    return pays_note, refs, personas


def build_view(slug, nom):
    pays_note, refs, personas = collect(slug)
    out = []
    out.append("# 🤖 MÉMOIRE %s — VUE GÉNÉRÉE" % nom.upper())
    out.append("")
    out.append("> ⚙️ **Document généré** par `generer_vue_memoire.py` depuis le vault atomique — **ne pas éditer à la main**.")
    out.append("> Démonstration Phase 4 (inversion du flux). La vraie autorité de travail reste `ANALYSTE/%s/MEMOIRE.md` tant que la bascule n'est pas validée." % nom.upper())
    out.append("> Le **camp** de chaque persona provient de **sa note entité** (source unique). Généré le %s." % TODAY)
    out.append("")
    if pays_note:
        out.append("## Carte d'identité")
        out.append("")
        out.append(pays_note[1])
        out.append("")
    # savoir countrybook
    if refs:
        out.append("---")
        out.append("")
        out.append("## Countrybook (savoir structuré)")
        out.append("")
        for fm, body in refs:
            out.append("### " + fm.get("title", fm.get("id", "")))
            out.append("")
            out.append(body)
            out.append("")
    # roster par camp
    out.append("---")
    out.append("")
    out.append("## Roster — %d personas (camp = autorité des notes entité)" % len(personas))
    out.append("")
    for camp in CAMP_ORDER:
        grp = sorted([(fm, r) for fm, r in personas if fm.get("camp") == camp], key=lambda x: x[0].get("title", ""))
        if not grp:
            continue
        out.append("### %s — %d" % (CAMP_LABEL[camp], len(grp)))
        out.append("")
        out.append("| Persona | Rôle | Note |")
        out.append("|---|---|---|")
        for fm, r in grp:
            out.append("| **%s** | %s | [[%s]] |" % (fm.get("title", ""), r, fm.get("id", "")))
        out.append("")
    out.append("---")
    out.append("> Source de vérité détaillée (tant que non basculé) : [`ANALYSTE/%s/MEMOIRE.md`](../../ANALYSTE/%s/MEMOIRE.md)." % (nom.upper(), nom.upper()))
    out.append("")
    return "\n".join(out)


def main():
    dst = os.path.join(VAULT, "_vues")
    os.makedirs(dst, exist_ok=True)
    for slug, nom in PAYS:
        view = build_view(slug, nom)
        open(os.path.join(dst, "MEMOIRE_%s.generee.md" % slug), "w", encoding="utf-8").write(view)
    print("vues memoire generees :", len(PAYS), "pays ->", os.path.relpath(dst, VAULT))


if __name__ == "__main__":
    main()
