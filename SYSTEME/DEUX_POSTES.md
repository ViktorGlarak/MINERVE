# Travail sur deux postes — PC pro + Mac perso

> Mis en place le **2026-10-12** depuis le Mac. **GitHub (`ViktorGlarak/MINERVE`) fait foi** : c'est le seul point de rencontre entre les deux postes.
> Ce fichier est la procédure de référence. CLAUDE.md § « Travail sur deux postes » le résume.

---

## 1. Les deux postes

| | **PC pro** (Windows) | **Mac perso** |
|---|---|---|
| Étiquette des commits | `[PC]` | `[MAC]` |
| Chemin du dépôt | `D:\CECPC\PRODUCTION\IA\MINERVE` | `/Users/thomas/Documents/PRO/MINERVE` |
| Accès à `D:\` (BDA, EXER, CREATION) et à `C:\CECPC\pleiade` | ✅ | ❌ |
| Domaine naturel | Code PLÉIADE, MELMIL, MASTAURIGE, assets, tout ce qui touche aux fichiers locaux | Documents seuls : doctrine (EXPERT_INFLUENCE, PSYCHOLOGUE, DESIGNER, CYBERSECU), BROUILLON, rédaction, réflexion |
| Lancer Python | `py` | `python3` (ex. `python3 vault/_tools/build.py`) |

**Règle d'or : jamais le même agent ouvert en même temps sur les deux postes.** Si c'est nécessaire, faire un commit et un push sur l'un avant de commencer sur l'autre.

## 2. Le rythme Git

1. **Début de session** : `git pull --rebase`, puis regarder ce que l'autre poste a apporté (`git log --oneline ORIG_HEAD..HEAD`) et le signaler à l'utilisateur.
2. **Après chaque avancée consignée en mémoire** (la règle de mise à jour de CLAUDE.md impose déjà cette consignation) : commit avec l'étiquette du poste, puis `git pull --rebase`, puis `git push`. Petits commits fréquents = conflits rares et petits.
3. **Fin de session** : `/session_end` (le commit se fait toujours avec l'accord de l'utilisateur), puis pull et push.
4. **Interdit** : `git push --force`, et laisser des modifications non poussées d'un jour sur l'autre.

Réglage à faire **une fois par poste** (déjà fait sur le Mac) :
```
git config pull.rebase true
git config rebase.autoStash true
```

## 3. Les conflits

| Fichier | Comportement |
|---|---|
| `**/JOURNAL.md`, `vault/daily/*.md` | **Fusion automatique** (`merge=union` dans `.gitattributes`) : les ajouts des deux postes sont gardés. Vérifier seulement l'ordre chronologique si les deux ont écrit le même jour. |
| `MEMOIRE.md`, CLAUDE.md, prompts | **Fusion selon le sens par Claude** : garder les deux apports, sans doublon ni perte. En cas de contradiction (ex. un camp de persona), **demander à l'utilisateur**. |
| Fichiers générés par le vault (`vault/INDEX.md`, canvas, `vault/_vues/`, `vault/context-packs/`) | Ne jamais fusionner à la main : prendre l'une des versions, puis relancer `build.py`. |

## 4. Ce qui reste propre à chaque poste (non versionné)

- `.claude/settings.local.json` : permissions et hooks propres au poste. Les hooks du PC pointent vers `D:/...` et utilisent `py`, ce qui ne marche pas sur le Mac. **Retiré du suivi Git le 2026-10-12.**
- `__pycache__/`, `*.pyc`.
- **La mémoire automatique de Claude** (`~/.claude/projects/<projet>/memory/`) : elle **n'est pas synchronisée**. **Règle : rien de durable n'y est stocké.** Tout ce qui compte va dans le dépôt :
  - les fichiers de l'ancienne mémoire automatique du PC (dont `aurige_guillaume.md`, l'état de production des personnages) sont **migrés dans `NOYAU/MEMOIRE_CLAUDE/`** ;
  - la mémoire automatique ne garde que ce qui est propre au poste (chemins, outils installés).

## 5. Migration à faire sur le PC pro (une seule fois)

> 📋 À exécuter par la session Claude du PC, après le pull qui apporte ce fichier.

- [x] `.claude/settings.local.json` est toujours présent (sinon le restaurer depuis la sauvegarde `settings.local.json.bak_pc` faite avant le pull) ; supprimer ensuite la sauvegarde. *(Il avait disparu au pull : restauré depuis la sauvegarde, qui n'existe plus. Ignoré par `.gitignore`.)*
- [x] `git config pull.rebase true` et `git config rebase.autoStash true`.
- [x] Copier **tous** les `.md` de `C:\Users\MTR\.claude\projects\d--CECPC-PRODUCTION-IA-MINERVE\memory\` vers `NOYAU\MEMOIRE_CLAUDE\` (dont `MEMORY.md`, l'index), **sans les modifier**. *(95 fichiers, vérifiés octet par octet ; aucun secret trouvé.)*
- [x] Dans les fichiers copiés et dans CLAUDE.md, repérer les références à `memory\…` et les remplacer par `NOYAU\MEMOIRE_CLAUDE\…` (voir CLAUDE.md § « Règle de mise à jour automatique »). *(CLAUDE.md était déjà à jour. Dans `MEMORY.md`, les deux liens vers `EXPERT_INFLUENCE\REFERENCES\` sont passés en `../../`, ce qui les rend valides. La mention de l'ancien dossier dans `rename_systeme_minerve.md` est gardée : c'est un fait historique.)*
- [x] Remplacer le contenu de la mémoire automatique du PC par un seul pointeur : « La mémoire durable est dans le dépôt : `NOYAU\MEMOIRE_CLAUDE\` ; procédure deux postes : `SYSTEME\DEUX_POSTES.md` ».
- [x] Vérifier `py vault\_tools\build.py` (exit 0).
- [x] Commit `[PC] Migration mémoire auto -> NOYAU/MEMOIRE_CLAUDE + procédure deux postes appliquée`, puis pull et push.
- [x] Cocher cette liste ici (dans le même commit) et noter la date.

**État :** ✅ fait sur le PC pro le 2026-10-12.
