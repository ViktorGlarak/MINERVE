# MÉMOIRE — ARCHITECTE (Qwen2.5-Coder 14B)

## Format d'entrée
```
### [YYYY-MM-DD] Catégorie : Titre
Contexte, solution trouvée, points clés.
```

---

## ⚠ RÈGLE ABSOLUE — Écosystème MASTAURIGE (2026-05-29)

> **Avant d'écrire ou modifier tout code dans l'écosystème MASTAURIGE, ARCHITECTE doit consulter la mémoire de MASTAURIGE.**
> MASTAURIGE est l'expert de son propre système. ARCHITECTE peut intervenir sur le code, mais jamais sans connaître les règles et l'état courant de l'outil.

**Écosystème MASTAURIGE = tout ce qui est sous :**
`D:\CECPC\PRODUCTION\EXER\AURIGE 2BB\00_Boites à outils\MASTAURIGE\`

Fichiers critiques à connaître avant toute intervention :
- `melmil.js` — logique drag-and-drop, sync localStorage, ghost cards CAS 1/1.5/2, `syncDayOverrides` (Sync 1 + Sync 2 sous-injects), `buildSubInjectDefaultSplits`, `applySubInjectPosition`
- `melmil_inject_index.js` — `MASTAURIGE_INDEX`, `MELMIL_EDITORIAL_DAYS`, `MELMIL_SUBINJECT_DAYS`
- `index_master.html` — `ANIM_DATA`, `LO_BY_KEY`, `initDateTimeEditors`, exports stagiaire (generate functions)
- `generate_data.ps1` — génère `melmil_data.js` depuis MELMIL.xls via Excel COM

**Règle virgule critique :** dans `melmil_inject_index.js`, chaque bloc `MASTAURIGE_INDEX` doit se terminer par `],` avant tout nouveau commentaire `//` — une virgule manquante invalide silencieusement tout l'objet.

**Règle de priorité localStorage :**
- `melmil-subinj` (SUBINJ_KEY) = drags manuels MELMIL uniquement — ne jamais écrire depuis du code auto
- `card-day-KEY` = position partagée index_master ↔ MELMIL
- `melmil-gg-positions` (STORAGE_KEY) = positions incidents XLS déplacés

## Patterns de prompt efficaces
<!-- Formulations qui produisent de bonnes réponses chez cet agent -->

## Patterns à éviter
<!-- Formulations ou contextes qui produisent des réponses insuffisantes -->

---

## Solutions et bugs résolus
<!-- Problèmes rencontrés et solutions apportées -->

---

## Conventions de code du projet
<!-- Standards, nommage, structure préférés par l'utilisateur -->

---

## Bibliothèques et outils fréquents
<!-- Stack technique récurrent de l'utilisateur -->
