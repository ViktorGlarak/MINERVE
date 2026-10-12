#!/bin/sh
# Pare-feu du nœud Mac (équivalent de pare-feu.ps1 du PC, réserve CYBERSECU O3).
# Seule l'adresse du SERVEUR (observée dans le journal du proxy) peut joindre le port 11435, et seulement sur l'IP VPN du Mac.
# Usage (administrateur) : sudo sh pare-feu.sh 10.8.0.X 10.8.0.1      ·  retrait : sudo sh pare-feu.sh --retirer
set -eu
ANCRE="com.apple/pleiade-noeud"
if [ "${1:-}" = "--retirer" ]; then pfctl -a "$ANCRE" -F all 2>/dev/null; echo "Règles du nœud retirées."; exit 0; fi
ECOUTE="${1:?adresse VPN du Mac}"; SOURCE="${2:?adresse du serveur observée}"
case "$ECOUTE$SOURCE" in *[!0-9.]*) echo "adresses invalides"; exit 1;; esac
printf 'pass in quick proto tcp from %s to %s port 11435\nblock drop in log quick proto tcp to any port 11435\n' "$SOURCE" "$ECOUTE" | pfctl -a "$ANCRE" -f -
pfctl -E 2>/dev/null || true
echo "Règles actives :"; pfctl -a "$ANCRE" -s rules
