#!/bin/sh
# Fin d'exercice (réserves O2 rotation, O5/F3 purge) : jeton détruit, journal purgé, règles pare-feu retirées.
rm -f "$HOME/.pleiade/ollama-cle.txt" "$HOME/.pleiade/proxy-ollama.log" "$HOME/.pleiade/essai-cle.txt"
echo "Jeton et journal supprimés. Retirer aussi le pare-feu : sudo sh pare-feu.sh --retirer"
echo "Puis : retirer le profil VPN du Mac dans Pritunl, et effacer OLLAMA_CLE de l'instance app-ia."
