# -*- coding: utf-8 -*-
# Hook PostToolUse : rappelle de consigner toute modif de l'outillage MASTAURIGE
# dans MASTAURIGE\MEMOIRE.md. Silencieux pour tout le reste.
import sys, json

try:
    data = json.load(sys.stdin)
except Exception:
    sys.exit(0)

p = ((data.get("tool_input") or {}).get("file_path")) or ""

# Cible : les vrais dossiers MASTAURIGE (dossier en MAJUSCULES) — exclut MASTAURIGE\MEMOIRE.md
# (case-sensitive : ne matche pas les fichiers de mémoire auto en minuscules "mastaurige_*").
if "MASTAURIGE" in p and not p.lower().replace("\\", "/").endswith("mastaurige/memoire.md") \
        and not p.lower().endswith("\\memoire.md") and not p.lower().endswith("/memoire.md"):
    msg = (
        "⚠ RÈGLE MASTAURIGE (CLAUDE.md) : tu viens de modifier l'outillage MASTAURIGE. "
        "Mémoire en 2 fichiers : CONSULTER MASTAURIGE\\MEMOIRE.md (état durable : règles, "
        "conventions, capacités — ~85 Ko, lisible) AVANT ; puis CONSIGNER APRÈS — un compte-rendu "
        "daté du changement dans MASTAURIGE\\JOURNAL.md, et si tu crées/changes une RÈGLE ou "
        "CAPACITÉ durable, mets aussi à jour MEMOIRE.md."
    )
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PostToolUse",
            "additionalContext": msg
        }
    }))

sys.exit(0)
