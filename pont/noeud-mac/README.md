# Nœud de calcul MAC pour les avatars IA (préparé le 2026-10-12)

> Objectif : que le serveur PLÉIADE (app-ia, zone DELATTRE 26) utilise **aussi** les modèles du Mac, en plus du PC, pour animer davantage d'avatars.
> Même contrat de sécurité que le nœud du PC : **avis CYBERSECU du 2026-10-12, réserves O1 à O8** (`CYBERSECU/MEMOIRE.md`, `PLEIADE/JOURNAL.md` 2026-10-12 suite 2).
> Ce dossier est le **kit du Mac**. Il transite par le dépôt pour que le PC et CYBERSECU le relisent. Le jeton et le journal vivent **hors dépôt**, dans `~/.pleiade/`.

## Ce qui est prêt (fait depuis le Mac)

| Élément | État |
|---|---|
| Modèles `gemma4:26b-a4b-it-qat` et `gemma4:31b-it-qat` (vision comprise) | ✅ installés, mesurés (`pont/banc_ia/`) |
| Ollama n'écoute que sur 127.0.0.1:11434, sans `OLLAMA_HOST` ni `OLLAMA_DEBUG`, version 0.40.2 (**O4**) | ✅ constaté |
| Disque chiffré (FileVault, équivalent de **D3** BitLocker) | ✅ constaté |
| `proxy_ollama.py` : Python sans dépendance (Node absent du Mac), **O1 / O2 / O5 / D1** | ✅ écrit |
| `essai_proxy.py` : matrice de refus **O8** en local, jeton jetable | ✅ **21/21 conformes** (après les améliorations de l'avis CYBERSECU du soir) ; le journal ne contient ni jeton ni contenu |
| Améliorations CYBERSECU (soir) : `num_predict` borné 1-2048, options non numériques → 400, `options` non-objet → 400, **1 image par requête**, 1 Mo sans image et ≤ 2 Mo avec (**A9**) | ✅ |
| **Pare-feu pf réappliqué à chaque lancement** par `LANCER_NOEUD.command` (mot de passe demandé, puis `sudo -k`) ; le nœud ne démarre pas sans lui (**A3**) | ✅ |
| **Mac sur le VPN : 10.8.0.51**, interface `utun7` point à point (= **tun**) ; **PC 10.8.0.3 injoignable depuis le Mac** (port 11435 et ping), cohérent avec un client-to-client désactivé ; serveur 10.8.0.1 joignable (**O7, constat côté client** ; reste à le confirmer côté serveur) | ✅ 2026-10-12 |
| `~/.ollama/logs` : **aucune invite** retrouvée (**A5**) ; `~/.pleiade` **exclu de Time Machine**, hors iCloud (**A6**) ; `~/.pleiade/noeud.conf` créé (ECOUTE=10.8.0.51, SOURCES=10.8.0.1 provisoire, à confirmer dans le journal) | ✅ |
| Démarrage refusé si l'IP VPN est absente (échec fermé, **O1 / D5**) | ✅ vérifié |
| `pare-feu.sh` : règle pf, seule la source serveur vers l'IP VPN :11435 (**O3**) | ✅ écrit, **pas appliqué** (VPN absent) |
| `LANCER_NOEUD.command` : double-clic, empêche la veille pendant le service (**D4**) | ✅ écrit |
| `FIN_EXERCICE.sh` : jeton détruit, journal purgé (**O2 rotation, F3**) | ✅ écrit |

Différences avec le proxy du PC :
- 3 modèles admis au lieu de 2 (le 31B en plus, pour le rédacteur des avatars de scénario) ;
- le corps de la requête est reconstruit depuis une liste blanche, `num_ctx` ≤ 16 384, `num_predict` ≤ 2 048 et `keep_alive` est fixé (**D1** appliqué d'emblée) ;
- plafond de 1 Mo réglable (`--plafond-ko`). ⚠ **Images (consigne 3bis)** : une photo en base64 pèse 0,3 à 3 Mo. Le plafond à retenir pour la lecture des images est **à décider avec CYBERSECU**.

## Ce qui manque — dans l'ordre

### A. Côté PC / app-ia (bloquant : sans lui, le Mac ne peut rien ajouter)
1. **app-ia ne connaît qu'UN nœud** (`OLLAMA_URL`, et `adresseNoeud()` n'admet en `http://` que `10.8.0.3:11435`). Il faut le **parc de machines** (consignes `pont/banc_ia/CONSIGNES_PC.md` § 3) :
   - une liste de nœuds (adresse, jeton, modèles, rôle) ;
   - la répartition des avatars, chaque avatar gardant sa machine pour profiter du cache ;
   - la **bascule** si le Mac disparaît ;
   - un modèle par avatar (31B pour les avatars de scénario) ;
   - `adresseNoeud()` étendu à l'IP VPN du Mac, et seulement elle.
2. **Catalogue `ia.yml`** : un second jeton secret (`OLLAMA_CLE_MAC`, ou un champ par nœud).
3. **CYBERSECU** : relire ce kit, trancher le plafond pour les images, et acter le changement de périmètre : un **ordinateur personnel** devient lieu de traitement des messages de joueurs (**D6 / F4**).

### B. Côté utilisateur (le Mac sur le VPN) — ✅ VPN connecté le 2026-10-12 (10.8.0.51)
0. **Encore à faire par l'utilisateur** (Réglages système, **A3 / A7**) : activer le **pare-feu macOS** (Réseau → Pare-feu) et le **verrouillage automatique ≤ 5 min avec mot de passe** (Écran verrouillé). Recommandé : une session macOS dédiée au nœud.
1. **Profil Pritunl NOMINATIF pour le Mac** : à créer par l'administrateur du VPN, puis client Pritunl à installer sur le Mac. ⛔ Claude n'ouvre jamais un profil ni un certificat VPN.
2. ⚠ **À vérifier** : le serveur VPN est-il joignable depuis le réseau où se trouve le Mac (domicile) ? Le PC s'y connecte depuis le réseau du travail.
3. Une fois connecté, noter l'**adresse VPN du Mac** (10.8.0.X) et créer `~/.pleiade/noeud.conf` :
   ```
   ECOUTE=10.8.0.X
   SOURCES=10.8.0.1
   ```
   `10.8.0.1` est l'adresse du serveur **à confirmer dans le journal** lors d'un premier appel depuis app-ia (réserve O3 : ne pas supposer).
4. Double-cliquer `LANCER_NOEUD.command`. Au premier lancement, le jeton est créé dans `~/.pleiade/ollama-cle.txt` (droits 600, jamais affiché).
5. Pare-feu : `sudo sh pare-feu.sh 10.8.0.X 10.8.0.1`.
6. Recopier le jeton dans la Configuration de l'instance app-ia, **sans le coller dans une conversation IA**, puis redéployer.
7. **O7 et O8 sur le vrai montage** :
   - depuis le LAN : port fermé ;
   - depuis un autre client VPN : port fermé ;
   - depuis le conteneur app-ia avec le jeton : 200.

### C. Fin d'exercice
`sh FIN_EXERCICE.sh`, puis `sudo sh pare-feu.sh --retirer`, puis retrait du profil VPN du Mac et effacement du jeton dans l'instance.

## Pendant le service
- La fenêtre du lanceur doit rester ouverte, Mac **branché sur secteur**. Couvercle fermé : seulement avec un écran externe, sinon le Mac se met en veille malgré `caffeinate`.
- Le journal `~/.pleiade/proxy-ollama.log` montre chaque appel (heure, source, route, modèle, statut, durée), sans contenu.
