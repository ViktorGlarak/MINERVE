@echo off
rem Proxy du noeud de calcul (avis CYBERSECU du 2026-10-12). VPN connecte requis.
rem Sous VOTRE compte, jamais en administrateur. Fermer cette fenetre arrete le proxy.
rem Au premier lancement, le jeton est cree dans %USERPROFILE%\.pleiade\ollama-cle.txt (a recopier vous-meme dans l'onglet Parc de calcul).
rem 2026-10-13 (grappe) : l'adresse VPN de CE PC se lit dans %USERPROFILE%\.pleiade\noeud-ecoute.txt (une ligne : 10.8.0.X) ; 10.8.0.3 sinon.
cd /d "%~dp0"
set ECOUTE=10.8.0.3
if exist "%USERPROFILE%\.pleiade\noeud-ecoute.txt" set /p ECOUTE=<"%USERPROFILE%\.pleiade\noeud-ecoute.txt"
echo Adresse VPN d'ecoute : %ECOUTE%
node proxy-ollama.mjs --sources=10.8.0.1 --ecoute=%ECOUTE%
pause
