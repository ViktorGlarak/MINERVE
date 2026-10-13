# Nœud de calcul WINDOWS pour les avatars IA (grappe PLÉIADE)

> Kit pour ajouter un PC Windows au **parc de calcul** du Moteur IA. Préparé le 2026-10-13, généralisé à partir du nœud du PC principal (10.8.0.3).
> Règles CYBERSECU (avis du 2026-10-12, conditions O1 à O8, et § B « grappe ») : le PC n'écoute que sur **son adresse VPN**, port **11435**, pour le **seul serveur** (10.8.0.1), avec un **jeton** propre à ce PC.

## Prérequis sur le PC
1. **Node.js** 22 ou plus récent (`node -v`).
2. **Ollama**, avec les modèles :
   ```
   ollama pull gemma4:26b-a4b-it-qat
   ollama pull bge-m3
   ```
   Ollama doit écouter **uniquement** sur `127.0.0.1:11434`, ce qui est le réglage par défaut. Ne jamais régler `OLLAMA_HOST=0.0.0.0`.
3. **Carte graphique** d'au moins 12 Go recommandée pour le modèle 26B.
4. Le **VPN de l'exercice** est connecté, avec un **profil VPN propre à ce PC**, créé par l'administrateur du VPN (révocable en fin d'exercice).
5. **Sécurité du poste** : disque chiffré (BitLocker), verrouillage automatique en 5 minutes au plus, session avec mot de passe.

## Installation
1. Copier ce dossier sur le PC, par exemple dans `C:\PLEIADE\noeud-windows`.
2. Noter **l'adresse VPN du PC**, par exemple `10.8.0.12` : commande `ipconfig`, carte du VPN.
3. Créer le fichier `%USERPROFILE%\.pleiade\noeud-ecoute.txt` contenant **une seule ligne** : cette adresse (`10.8.0.12`).
4. Double-cliquer **`LANCER_PROXY.cmd`**, sous votre compte et **jamais** en administrateur.
   - Au premier lancement, le jeton est créé dans `%USERPROFILE%\.pleiade\ollama-cle.txt` ; il n'est jamais affiché.
   - La fenêtre doit rester ouverte : la fermer arrête le nœud.
5. **Pare-feu**, dans un PowerShell **lancé en administrateur** :
   ```
   powershell -ExecutionPolicy Bypass -File pare-feu.ps1 -Source 10.8.0.1 -Ecoute 10.8.0.12
   ```
6. **Moteur IA → onglet « Parc de calcul » → « Ajouter un nœud »** :
   - nom : par exemple « PC salle 2 » ;
   - adresse : le dernier nombre (`12`) ;
   - jeton : ouvrir `ollama-cle.txt` et le coller dans le formulaire. **Ne jamais le coller dans une conversation avec une IA** ;
   - classe : **Maîtrisé** si c'est une machine de l'exercice, **Tiers** si c'est une machine personnelle ;
   - **Essayer la connexion**, puis **Enregistrer**.

Au tour suivant, une partie des avatars passe sur ce PC. Si le PC s'éteint ou perd le VPN, ses avatars sont repris automatiquement par les autres nœuds.

## Vérifications (CYBERSECU, O8 sur le vrai montage)
- Depuis le réseau local du PC : le port 11435 doit être **fermé**.
- Depuis un autre poste du VPN : le port doit être **fermé**.
- Depuis le Moteur IA (bouton « Essayer la connexion ») : **joignable, modèle présent**.
- Journal du relais : `%USERPROFILE%\.pleiade\noeud-ia\proxy.log`. On y voit l'heure, la source, la route, le statut et la durée de chaque appel, jamais le contenu.
- Essai local des refus, avec un jeton jetable : `node essai-proxy.mjs %TEMP%\essai-proxy`.

## Fin d'exercice
1. Moteur IA → Parc de calcul → **Retirer** le nœud (le jeton est effacé de l'instance).
2. Fermer la fenêtre du relais, puis supprimer `%USERPROFILE%\.pleiade\ollama-cle.txt`.
3. Retirer la règle de pare-feu « PLEIADE - noeud de calcul (proxy Ollama) ».
4. Faire révoquer le profil VPN du PC.
