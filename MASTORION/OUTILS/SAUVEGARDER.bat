@echo off
REM ============================================================
REM  MASTORION - Sauvegarde de l'etat actuel (base + images)
REM  Sert a deux choses :
REM   - figer une BIBLIOTHEQUE D'UNIVERS (ex: UNIVERS SKOLKAN)
REM   - prendre un point de retour date avant d'experimenter
REM ============================================================
setlocal enabledelayedexpansion
set "PATH=%LOCALAPPDATA%\Programs\DockerDesktop\resources\bin;%PATH%"
set "DOSSIER=%~dp0"
set "UPLOADS=C:\CECPC\MASTORION\mastorion-v0\apps\api\uploads"

where docker >nul 2>&1
if errorlevel 1 (
  echo.
  echo [ERREUR] Docker introuvable. Docker Desktop est-il installe ?
  pause
  exit /b 1
)

set "DBUP="
for /f "delims=" %%N in ('docker ps --filter "name=mastorion-db" --format "{{.Names}}" 2^>nul') do set "DBUP=%%N"
if not defined DBUP (
  echo.
  echo [ERREUR] Le conteneur mastorion-db n'est pas demarre.
  echo Lance Docker Desktop, attends la baleine, puis reessaie.
  pause
  exit /b 1
)

echo.
echo ============================================
echo   SAUVEGARDE MASTORION
echo ============================================
echo.
echo Donne un nom clair si c'est une bibliotheque d'univers.
echo   Exemples : UNIVERS SKOLKAN   /   UNIVERS ORION 26
echo   (Entree = sauvegarde datee du jour)
echo.
set "NOM="
set /p NOM="Nom de la sauvegarde : "

if not defined NOM (
  for /f "delims=" %%I in ('powershell -NoProfile -Command "Get-Date -Format \"yyyy-MM-dd_HH'h'mm\""') do set "NOM=SAUVEGARDE_%%I"
)

if exist "%DOSSIER%%NOM%.sql" (
  echo.
  echo Une sauvegarde "%NOM%" existe deja.
  set "ECRASER="
  set /p ECRASER="Taper OUI pour la remplacer : "
  if not "!ECRASER!"=="OUI" (
    echo Annule.
    pause
    exit /b 0
  )
)

echo.
echo Sauvegarde de la base de donnees...
docker exec mastorion-db mariadb-dump -umastorion -pmastorion --databases mastorion > "%DOSSIER%%NOM%.sql"
if errorlevel 1 goto erreur
if not exist "%DOSSIER%%NOM%.sql" (
  echo.
  echo [ERREUR] Fichier non cree. Evite les caracteres speciaux
  echo dans le nom : \ / : * ? " ^< ^> ^|
  pause
  exit /b 1
)

echo Sauvegarde des images (avatars, medias)...
if exist "%UPLOADS%" (
  robocopy "%UPLOADS%" "%DOSSIER%%NOM%_uploads" /MIR /NFL /NDL /NJH /NJS /NP >nul
)

echo.
echo === TERMINE ===
echo   Base   : %NOM%.sql
echo   Images : %NOM%_uploads\
echo.
echo Pour recharger cet etat plus tard : RESTAURER.bat
echo.
pause
exit /b 0

:erreur
echo.
echo [ERREUR] La sauvegarde a echoue.
pause
exit /b 1
