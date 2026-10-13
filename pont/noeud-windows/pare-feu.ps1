# Pare-feu du nœud de calcul (avis CYBERSECU du 2026-10-12, condition O3) — À LANCER EN ADMINISTRATEUR.
#   powershell -ExecutionPolicy Bypass -File pare-feu.ps1 -Source 10.8.0.1 [-Ecoute 10.8.0.X]   (-Ecoute : l'adresse VPN de CE PC ; 10.8.0.3 par défaut)
# -Source : l'IP du serveur VUE dans le journal du proxy (%USERPROFILE%\.pleiade\noeud-ia\proxy.log, ligne « refusé : source »).
param([Parameter(Mandatory = $true)][string]$Source, [string]$Ecoute = "10.8.0.3")

if (-not ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
  Write-Host "À lancer en administrateur." -ForegroundColor Red; exit 1 }
if ($Source -notmatch '^\d{1,3}(\.\d{1,3}){3}$') { Write-Host "Source : une adresse IPv4." -ForegroundColor Red; exit 1 }
if ($Ecoute -notmatch '^10\.8\.0\.(\d{1,3})$' -or [int]$Matches[1] -lt 2 -or [int]$Matches[1] -gt 254) { Write-Host "Ecoute : l'adresse VPN de ce PC, 10.8.0.2 à 10.8.0.254." -ForegroundColor Red; exit 1 }

$node = (Get-Command node).Source

# 1. Retirer les règles entrantes LARGES sur node.exe créées par l'invite « Autoriser l'accès » de Windows.
$larges = Get-NetFirewallRule -Direction Inbound -ErrorAction SilentlyContinue | Where-Object {
  $_.DisplayName -ne 'PLEIADE - noeud de calcul (proxy Ollama)' -and
  (($_ | Get-NetFirewallApplicationFilter).Program -like '*node.exe') }
foreach ($r in $larges) { Write-Host "Suppression : $($r.DisplayName) [$($r.Profile)]"; Remove-NetFirewallRule -Name $r.Name }

# 2. Une seule règle : entrant TCP, adresse locale 10.8.0.3, port 11435, programme node.exe, depuis le seul serveur, tous profils.
Get-NetFirewallRule -DisplayName 'PLEIADE - noeud de calcul (proxy Ollama)' -ErrorAction SilentlyContinue | Remove-NetFirewallRule
New-NetFirewallRule -DisplayName 'PLEIADE - noeud de calcul (proxy Ollama)' -Direction Inbound -Action Allow -Protocol TCP `
  -LocalAddress $Ecoute -LocalPort 11435 -RemoteAddress $Source -Program $node -Profile Any | Out-Null

# 3. Journaliser les paquets refusés (tous profils).
Set-NetFirewallProfile -Profile Domain,Private,Public -LogBlocked True -LogFileName '%systemroot%\system32\LogFiles\Firewall\pfirewall.log'

Write-Host "OK : seule la source $Source peut joindre $($Ecoute):11435 (node.exe). Paquets refusés journalisés dans pfirewall.log." -ForegroundColor Green
