@echo off
REM ============================================================
REM  MASTORION - Basculer vers une sauvegarde / un univers
REM  ATTENTION : REMPLACE le contenu actuel de la plateforme.
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
echo   BASCULER MASTORION
echo ============================================
echo.
echo Sauvegardes et univers disponibles :
echo.
set N=0
for %%F in ("%DOSSIER%*.sql") do (
  set /a N+=1
  echo    !N!^) %%~nF
)
if %N%==0 (
  echo    [aucune sauvegarde trouvee]
  echo.
  pause
  exit /b 1
)
echo.
set "CHOIX="
set /p CHOIX="Numero a charger (Entree = annuler) : "
if not defined CHOIX exit /b 0

set "SELECTION="
set I=0
for %%F in ("%DOSSIER%*.sql") do (
  set /a I+=1
  if "!I!"=="%CHOIX%" set "SELECTION=%%~nxF"
)
if not defined SELECTION (
  echo Choix invalide.
  pause
  exit /b 1
)

echo.
echo ATTENTION : tout le contenu actuel de MASTORION (personas,
echo groupes, scenarios, posts) sera REMPLACE par :
echo     %SELECTION%
echo.
set "CONFIRM="
set /p CONFIRM="Taper OUI en majuscules pour confirmer : "
if not "%CONFIRM%"=="OUI" (
  echo Annule.
  pause
  exit /b 0
)

echo.
echo Chargement de la base...
docker exec -i mastorion-db mariadb -umastorion -pmastorion < "%DOSSIER%%SELECTION%"
if errorlevel 1 goto erreur

set "DOSSIER_IMG=%DOSSIER%%SELECTION:.sql=%_uploads"
if exist "%DOSSIER_IMG%" (
  echo Chargement des images...
  robocopy "%DOSSIER_IMG%" "%UPLOADS%" /MIR /NFL /NDL /NJH /NJS /NP >nul
) else (
  echo [info] Pas d'images associees a cette sauvegarde.
)

echo.
echo === TERMINE ===
echo.
echo IMPORTANT : dans le navigateur, DECONNECTE-TOI puis RECONNECTE-TOI.
echo Les comptes ont ete remplaces : ton ancienne session affichera
echo sinon des erreurs "Token invalide".
echo.
pause
exit /b 0

:erreur
echo.
echo [ERREUR] Le chargement a echoue.
pause
exit /b 1
