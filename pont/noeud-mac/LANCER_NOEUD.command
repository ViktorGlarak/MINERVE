#!/bin/sh
# Lance le nœud de calcul Mac (double-clic). Lit ~/.pleiade/noeud.conf : ECOUTE=10.8.0.X  SOURCES=10.8.0.1
# 1) réapplique le pare-feu pf (les règles ne survivent pas à un redémarrage — avis CYBERSECU A3) : mot de passe demandé ;
# 2) lance le proxy sous TON compte (jamais root) ; le Mac ne se met pas en veille tant que cette fenêtre est ouverte (A8).
# Fermer la fenêtre = nœud arrêté.
cd "$(dirname "$0")"
. "$HOME/.pleiade/noeud.conf" || { echo "Créer ~/.pleiade/noeud.conf (voir README)"; read r; exit 1; }
ifconfig | grep -q "inet $ECOUTE " || { echo "VPN non connecté ($ECOUTE absente) : connecter Pritunl puis relancer."; read r; exit 1; }
echo "Pare-feu du nœud (mot de passe administrateur du Mac) :"
sudo sh ./pare-feu.sh "$ECOUTE" "$SOURCES" || { echo "Pare-feu NON appliqué : le nœud ne démarre pas."; read r; exit 1; }
sudo -k
exec caffeinate -i -s python3 -I proxy_ollama.py --ecoute "$ECOUTE" --sources "$SOURCES"
