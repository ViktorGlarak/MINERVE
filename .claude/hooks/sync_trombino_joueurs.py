# -*- coding: utf-8 -*-
r"""
Hook PostToolUse (Edit|Write|MultiEdit) — sync auto du TROMBINOSCOPE.

Quand on édite le trombino de l'instance COLLAB
(...\SERVEUR_COLLABORATIF\mastaurige\Sites\Trombinoscope\...), recopie
automatiquement vers JOUEURS + LOCALSTORAGE (kit joueurs toujours à jour),
en appelant OUTILS\sync_trombino_joueurs.py (source de vérité de la copie).

Silencieux si l'édition ne concerne pas le trombino.
"""
import json, os, subprocess, sys

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

SYNC = (r"D:\CECPC\PRODUCTION\EXER\AURIGE 7BB\00_Boites à outils\MASTAURIGE"
        r"\SERVEUR_COLLABORATIF\mastaurige\OUTILS\sync_trombino_joueurs.py")


def main():
    try:
        data = json.load(sys.stdin)
    except Exception:
        return
    ti = data.get("tool_input") or {}
    path = (ti.get("file_path") or ti.get("path") or "").replace("\\", "/").lower()
    if not path:
        return
    # déclenche UNIQUEMENT pour le trombino de l'instance collab (le master)
    if "serveur_collaboratif" in path and "/sites/trombinoscope/" in path:
        try:
            r = subprocess.run([sys.executable, SYNC], capture_output=True, text=True, timeout=60)
            out = (r.stdout or "").strip()
            print("[sync] Trombinoscope propage vers JOUEURS + LOCALSTORAGE." + (("\n" + out) if out else ""))
        except Exception as e:
            print("[sync] trombino: echec (%s)" % e)


if __name__ == "__main__":
    main()
