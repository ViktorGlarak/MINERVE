# OUTILS — MASTORION (outillage MINERVE, pas du projet Mastorion)

> ⚠ **Ces scripts ne font PAS partie du dépôt `mastorion-v0`.** Ils ont été écrits côté MINERVE le **2026-07-27** pour l'exploitation locale de la plateforme. Le dépôt de Xavier TALANDIER ne contient **aucun** `.bat` et reste intact.
>
> **Copie de référence versionnée** = ce dossier. **Copie utilisée au quotidien** = `C:\CECPC\MASTORION\SAUVEGARDES\` (à côté des fichiers `.sql` qu'ils manipulent). En cas de modification, reporter ici.

## Contenu

| Script | Rôle |
|---|---|
| `SAUVEGARDER.bat` | Fige l'état courant de la plateforme (base MariaDB + dossier `uploads`). Demande un **nom** : un nom parlant (`UNIVERS SKOLKAN`) pour une **bibliothèque d'univers**, ou Entrée pour un **point de retour daté**. |
| `RESTAURER.bat` | Liste les sauvegardes/univers, en recharge un après confirmation « OUI ». Sert de **bascule d'univers**. |

## Prérequis
- Docker Desktop lancé, conteneur `mastorion-db` démarré.
- Chemins codés en dur : conteneur `mastorion-db` · uploads `C:\CECPC\MASTORION\mastorion-v0\apps\api\uploads`.

## Après une restauration
**Se déconnecter puis se reconnecter** dans le navigateur : les comptes ont été remplacés, l'ancienne session provoque des erreurs « Token invalide ».

## À ne pas confondre
Le projet fournit `deploy/backup-db.sh` — script **Linux**, pour le **serveur de production** (dump toutes les 4 h par cron, conteneur `orion26-mariadb-1`). Il ne remplace pas ces `.bat`, qui sont l'équivalent **poste Windows**.

Détails, pièges d'écriture batch et procédure complète : `MASTORION\MEMOIRE.md`.
