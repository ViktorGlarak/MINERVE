# -*- coding: utf-8 -*-
# Hook PostToolUse : dès qu'un fichier d'un exercice de TYPE AURIGE est modifié
# (AURIGE 2BB / GUILLAUME, AURIGE 7BB / MINOTAURE, futurs AURIGE),
# rappelle d'appliquer + faire ÉVOLUER la méthodologie AURIGE transférable,
# pour qu'une amélioration trouvée sur un exercice profite à TOUS.
# Silencieux pour tout le reste.
import sys, json

try:
    data = json.load(sys.stdin)
except Exception:
    sys.exit(0)

p = (((data.get("tool_input") or {}).get("file_path")) or "").replace("\\", "/")
low = p.lower()

# Cible : contenu d'un exercice AURIGE — PAS la doctrine/mémoire AURIGE elle-même.
# ⚠ On retire "mastaurige" AVANT de chercher "aurige" : sinon "m-ast-AURIGE" déclenche
# un faux positif sur tout l'outillage MASTAURIGE (et la vierge, qui n'est pas un exercice).
cleaned = low.replace("mastaurige", "")
is_aurige = ("aurige" in cleaned) or ("minotaure" in low) or ("minautore" in low)
is_base = low.endswith("/aurige.md") or low.endswith("aurige/memoire.md") or low.endswith("aurige\\memoire.md")

if is_aurige and not is_base:
    msg = (
        "⚠ EXERCICE DE TYPE AURIGE (GUILLAUME 2BB · MINOTAURE 7BB · futurs). "
        "La MÉTHODOLOGIE AURIGE est transférable et ÉVOLUE — applique-la et fais-la vivre : "
        "base doctrinale = `SYSTEME/PROMPTS/aurige.md` + mémoire `AURIGE/MEMOIRE.md`. "
        "Si ta façon de travailler change/s'améliore (outillage, conventions, doctrine narrative, "
        "calibration niveau brigade, réflexes inter-agents, pipeline injects…), "
        "CONSIGNE-le dans la base AURIGE pour que TOUS les exercices AURIGE en profitent "
        "(pas seulement celui en cours). "
        "Et consulte le chef d'orchestre de CET exercice : GUILLAUME (2BB) / MINAUTORE (7BB)."
    )
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PostToolUse",
            "additionalContext": msg
        }
    }))

sys.exit(0)
