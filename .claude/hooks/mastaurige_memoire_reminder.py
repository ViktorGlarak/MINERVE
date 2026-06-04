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
        "Avant de clôturer, CONSIGNE ce changement dans MASTAURIGE\\MEMOIRE.md "
        "(section « v0.2 — FAIT FOI »), et assure-toi d'avoir CONSULTÉ cette mémoire au préalable."
    )
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PostToolUse",
            "additionalContext": msg
        }
    }))

sys.exit(0)
