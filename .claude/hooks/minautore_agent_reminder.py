# -*- coding: utf-8 -*-
# Hook PostToolUse : dès qu'un fichier de l'exercice MINOTAURE / AURIGE 7BB est modifié,
# rappelle que l'agent MINAUTORE doit PILOTER le travail et faire RELIRE/CORRIGER par les
# agents compétents. Silencieux pour tout le reste.
import sys, json

try:
    data = json.load(sys.stdin)
except Exception:
    sys.exit(0)

p = (((data.get("tool_input") or {}).get("file_path")) or "").replace("\\", "/")
low = p.lower()

# Cible : tout contenu de l'exercice 7BB / MINOTAURE — mais PAS la mémoire de l'agent
# (sinon le rappel se déclenche quand on consigne, ce qui est inutile).
is_7bb = ("aurige 7bb" in low) or ("minautore" in low) or ("minotaure" in low)
is_memoire = low.endswith("minautore/memoire.md") or low.endswith("minautore\\memoire.md")

if is_7bb and not is_memoire:
    msg = (
        "⚠ EXERCICE MINOTAURE / AURIGE 7BB — tu modifies du contenu de CET exercice. "
        "Tu DOIS opérer en tant qu'agent MINAUTORE (charge SYSTEME/PROMPTS/minautore.md + "
        "MINAUTORE/MEMOIRE.md : chef d'orchestre éditorial 7BB) et NE PAS décider seul. "
        "RÉFLEXE n°1 : MINAUTORE est LE référent de l'exercice — pour savoir quel inject/date/"
        "persona/jour ou si un article est utilisé, CONSULTE D'ABORD sa carte "
        "`MINAUTORE/ETAT_EXERCICE_7BB.md` (et régénère-la via `py MINAUTORE/generer_etat_exercice.py` "
        "après ta modif), JAMAIS un grep à l'aveugle. "
        "Fais RELIRE et CORRIGER par l'agent compétent AVANT de clôturer :\n"
        "  • camp / identité / doctrine d'un persona ARN  → ANALYSTE_ARN (autorité du camp)\n"
        "  • effets ILI, séquence PSYOPS, synchromatrice, fit LO  → EXPERT_INFLUENCE\n"
        "  • rédaction (tweets, courriers, voix locale)  → SCENARISTE\n"
        "  • personas/camp Mercure, TTP Storm-1516  → ANALYSTE (Mercure)\n"
        "  • format RS / HTML / outillage  → MASTAURIGE\n"
        "Rapporte explicitement « validé / corrigé par <AGENT> » à l'utilisateur, "
        "puis CONSIGNE l'avancée dans MINAUTORE/MEMOIRE.md."
    )
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PostToolUse",
            "additionalContext": msg
        }
    }))

sys.exit(0)
