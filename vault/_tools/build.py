# -*- coding: utf-8 -*-
"""
build.py — orchestrateur unique du vault MINERVE.
Lance, dans l'ordre :  generer_agents -> generer_context_packs -> generer_index -> valider.
Une seule commande a retenir :  py _tools/build.py

Sort en exit 1 si la validation echoue (liens casses, duplication, etc.).
"""
import os, sys, subprocess

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
TOOLS = os.path.dirname(os.path.abspath(__file__))
PY = sys.executable
ENV = dict(os.environ, PYTHONIOENCODING="utf-8")  # force UTF-8 dans les sous-process
STEPS = [
    ("generer_agents.py", "🤖 canvas agents"),
    ("generer_context_packs.py", "📦 context-packs"),
    ("generer_index.py", "🗂️ INDEX"),
    ("valider.py", "🛡️ validation"),
]


def main():
    print("=== BUILD VAULT MINERVE ===")
    for script, label in STEPS:
        path = os.path.join(TOOLS, script)
        if not os.path.exists(path):
            print("  ⏭️  %-22s (absent, ignoré)" % label)
            continue
        print("\n▶ %s (%s)" % (label, script))
        r = subprocess.run([PY, path], cwd=TOOLS, env=ENV)
        if r.returncode != 0:
            print("\n❌ BUILD INTERROMPU à l'étape : %s (exit %d)" % (label, r.returncode))
            sys.exit(r.returncode)
    print("\n✅ BUILD OK — vault à jour et validé.")


if __name__ == "__main__":
    main()
