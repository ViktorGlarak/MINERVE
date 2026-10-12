#!/bin/sh
# Lance le nœud de calcul Mac (double-clic). Lit ~/.pleiade/noeud.conf : ECOUTE=10.8.0.X  SOURCES=10.8.0.1
# Le Mac ne se met pas en veille tant que cette fenêtre est ouverte (réserve D4). Fermer la fenêtre = nœud arrêté.
cd "$(dirname "$0")"
. "$HOME/.pleiade/noeud.conf" || { echo "Créer ~/.pleiade/noeud.conf (voir README)"; read r; exit 1; }
exec caffeinate -i -s python3 -I proxy_ollama.py --ecoute "$ECOUTE" --sources "$SOURCES"
