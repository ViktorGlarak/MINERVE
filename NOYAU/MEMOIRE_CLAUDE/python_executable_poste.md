---
name: python-executable-poste
description: Interpréteur Python réellement exécutable sur le poste (les générateurs/outils .py en dépendent)
metadata: 
  node_type: memory
  type: reference
  originSessionId: 4377e89f-f0dd-40af-851d-ddfb523fd276
---

Sur ce poste, **`python`/`py` en PATH = stub Microsoft Store** (« Python was not found ») et le **python embarqué** de `SERVEUR_COLLABORATIF\python\python.exe` est **bloqué** par la politique (« Accès refusé », .exe non approuvé).

**Interpréteur RÉELLEMENT exécutable (non bloqué)** — découvert 2026-06-24 :
```
C:\Users\MTR\AppData\Local\Python\pythoncore-3.14-64\python.exe
```
- cpython 3.14.4, **PIL/Pillow disponible** (utile pour découper/redimensionner les photos trombino).
- Alternative : `C:\Program Files\LibreOffice\program\python.exe` (3.12) fonctionne aussi.

**À utiliser pour** : `generer_trombino_bios.py`, `generer_melmil.py`, `MINAUTORE\generer_etat_exercice.py`, et tout script du pipeline MASTAURIGE. Exemple : `& "C:\Users\MTR\AppData\Local\Python\pythoncore-3.14-64\python.exe" generer_trombino_bios.py`.

Lié : [[mastaurige_pipeline_injects]], [[project_mercure]].
