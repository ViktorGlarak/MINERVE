# MINERVE Local — assistant de CONSULTATION (lecture seule)

> RAG local **100 % Ollama** pour interroger en français tout le corpus MINERVE
> **sans tokens Claude, hors-ligne**. ⚠ **LECTURE SEULE** : ne modifie/ne crée **aucune** donnée.
> Décisions : [`vault/decisions/DECISION-011.md`](../vault/decisions/DECISION-011.md).

## Prérequis
- **Ollama** lancé (`localhost:11434`).
- Modèles : **`mistral-nemo`** (réponse, FR) + **`bge-m3`** (embeddings) → `ollama pull bge-m3`.
- Python du poste : `C:\Users\MTR\AppData\Local\Python\pythoncore-3.14-64\python.exe` (numpy requis, déjà présent).

## Usage
```bat
cd "D:\CECPC\PRODUCTION\IA\MINERVE\MINERVE_LOCAL"
set PY=C:\Users\MTR\AppData\Local\Python\pythoncore-3.14-64\python.exe

REM 1) indexer le corpus public (tout IA\MINERVE) — à relancer quand les mémoires évoluent
"%PY%" minerve_local.py index

REM 2) discuter (lecture seule, réponses sourcées)
"%PY%" minerve_local.py chat
```
Exemples de questions : « profil du général Prunière ? », « que dit le countrybook sur Den Helder ? »,
« quelles LO pour la série 07.11 ? », « camp de @MarionKessler57 ? ».

## ⚠ Fiches bio sensibles — collection SÉGRÉGUÉE (utilisateur uniquement)
Le dossier `D:\CECPC\DOC REF\MERCURE\RENS\01_Fiches bio` ne doit **jamais** être ouvert par Claude
(ni son contenu, ni les chunks dérivés). **C'est l'utilisateur** qui lance son indexation, dans une
**collection séparée** que Claude n'ouvre pas :
```bat
"%PY%" minerve_local.py index --root "D:\CECPC\DOC REF\MERCURE\RENS\01_Fiches bio" --collection fiches_bio
```
Le `chat` fusionne automatiquement toutes les collections présentes dans `index/`.

## Comment ça marche
1. **index** : lit les `.md` du corpus → découpe → embeddings **bge-m3** → vecteurs dans `index/<collection>.pkl`.
2. **chat** : embedde la question → retrouve les passages les plus proches (toutes collections) →
   les passe à **mistral-nemo** → réponse en français **citant les fichiers source**.

## Limites
- Modèle local ~12B : très bon en **restitution** de faits indexés, plus faible en **synthèse croisée fine** (≠ Claude).
- **Fraîcheur** : relancer `index` après une session de production Claude (les mémoires changent).
- Exclus de l'index public : `vault/_vues`, `vault/context-packs`, `vault/agents` (générés/dup), `.git`, `__pycache__`.
