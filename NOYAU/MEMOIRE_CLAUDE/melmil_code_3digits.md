---
name: melmil-code-3digits
description: "Format des codes d'incident AURIGE : le dernier segment ZZ peut être à 2 OU 3 chiffres (XX.YY.ZZ ou XX.YY.ZZZ) — supporté partout depuis 2026-06-02"
metadata: 
  node_type: memory
  type: reference
  originSessionId: 9cd755be-0651-44f5-8932-5974a21bced9
---

**Décision utilisateur (2026-06-02) :** un incident peut être nommé **`XX.YY.ZZ`** (2 chiffres) **OU `XX.YY.ZZZ`** (3 chiffres) sur le dernier segment. Les deux doivent fonctionner partout (index_master, MELMIL, générateur .bat, validateur).

**Ce qui a été assoupli (3ᵉ segment `\d{2}` → `\d{2,3}`) :**
- `MELMIL\melmil.js` → fonction `bridgeCode` (pont auto tweets/créations → MELMIL).
- `tweets_engine.js` → fonction `normalizeIncident` (créateur de tweets ; message d'aide mis à jour : « XX.YY.ZZ ou XX.YY.ZZZ »).

**Déjà compatibles (aucune modif nécessaire) :**
- `generate_data.py` (lancé par `Actualiser_MELMIL.bat`) : lit la colonne Code **verbatim**, sans filtre de format → accepte n'importe quel code, dont 3 chiffres. (Le `.ps1` de secours idem.)
- `melmil.js` : `getParentInjectCode` (`\d+`) et `buildInjects` (`^(\d+\.\d+)`) étaient déjà flexibles.
- `index_master.html` : aucune regex de code inject (le seul `\d{2}` est un parseur d'heure).
- `verifier_mastaurige.py` : pas d'hypothèse sur le nombre de chiffres.

**Conséquence pratique :** le code **`01.01.119`** est désormais pleinement valide. Il peut être ajouté tel quel dans `MELMIL.xls` (puis `Actualiser_MELMIL.bat`) pour devenir une vraie card incident — **plus besoin de renuméroter** en 2 chiffres. En attendant, il est curé en ghost (cf. [[melmil-coherence]] et l'inject 01.01.119 dans melmil_inject_index.js).

Voir [[mastaurige]] [[web-architecture]].
