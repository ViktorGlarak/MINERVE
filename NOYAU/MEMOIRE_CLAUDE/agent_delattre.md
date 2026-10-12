---
name: agent-delattre
description: "Agent DELATTRE créé le 22/07/2026 — chef d'orchestre éditorial de l'exercice DELATTRE 26, successeur de MINAUTORE ; identité de l'exercice encore à renseigner"
metadata: 
  node_type: memory
  type: project
  originSessionId: 52feb2ec-047b-438f-b7ad-369a80dbc9a0
  modified: 2026-07-22T12:28:13.996Z
---

L'exercice suivant s'appelle **DELATTRE 26** (« 26 » = 2026) — on peut simplement dire **« DELATTRE »**. Un agent dédié **DELATTRE** a été créé le **2026-07-22** : c'est le **chef d'orchestre éditorial** de cet exercice, **20ᵉ agent** du système MINERVE (Claude cloud, claude-opus-4-7).

**Lignée des agents exercice :** GUILLAUME (AURIGE 2BB) → MINAUTORE (AURIGE 7BB / MINOTAURE 26, **clos le 03/07**) → **DELATTRE (DELATTRE 26)**.

**Créé conformément à la checklist CLAUDE.md :** registre `CLAUDE.md` · `SYSTEME\PROMPTS\delattre.md` · `DELATTRE\README.md` + `DELATTRE\MEMOIRE.md` · branche dans `SYSTEME\ROUTAGE.md` · compteur `NOYAU\MEMOIRE.md` porté de **19 à 20**.

⚠ **L'identité de l'exercice n'est PAS encore connue** (unité entraînée, **niveau**, dates réelles + temps de jeu D+, zone/H-codes, **camps** — attention, le 7BB était inversé vs le 2BB —, pays fictifs, sources de montage, storylines→LO). Les champs sont marqués ⚠️ dans `DELATTRE\MEMOIRE.md` §1. **Les demander avant toute production** : le **niveau** conditionne toute la calibration.

**Le prompt de DELATTRE embarque déjà** : les 5 LO GLM26, les règles narratives permanentes (CLIMAX, noyau de vérité 80/20, Steps PSYOPS, GET, H-préfixe), le **RETEX MINOTAURE** (calibrer TACTIQUE · fermer la boucle de retour · GT productifs · casser les silos · reconduire MASTAURIGE+EHO+1 traitant par LO), la carte de routage inter-agents, et la liste des **actifs réutilisables** (EHO 7BB, gabarit MASTAURIGE **v0.3**, registre avatars, chartes médias, doctrine EXPERT_INFLUENCE).

## ⏸️ STATUT AU 2026-07-22 : STANDBY
L'utilisateur ne sait **pas encore** ce que sera DELATTRE 26 ni **qui sera entraîné**. → **Ne rien produire, ne rien présumer** (unité, niveau, camps, zone). L'agent existe et est câblé ; il attend son contenu.

## 🔔 RAPPEL DIFFÉRÉ — hook DELATTRE à créer
**À proposer quand l'utilisateur aura fourni les informations de l'exercice** (unité, niveau, dates, zone, camps) : créer un hook de rappel sur le modèle de `minautore_agent_reminder.py` (PostToolUse), qui rappelle d'opérer **en tant que DELATTRE** et de **consulter/mettre à jour `DELATTRE\MEMOIRE.md`** dès qu'un fichier de l'exercice est touché. Nécessite `settings.local.json`. **Demande explicite de l'utilisateur le 2026-07-22 : « tu me rappelleras de mettre un hook plus tard ».** *(Ne pas le créer avant : sans chemin d'exercice connu, le hook n'aurait rien à cibler.)*

**Why:** l'utilisateur veut un expert DELATTRE « référencé un peu partout pour que les liens se fassent naturellement », doté des acquis des exercices précédents.

**How to apply:** toute demande touchant DELATTRE 26 → **DELATTRE en agent primaire** (lire sa mémoire AVANT, y consigner APRÈS), puis router : effets ILI → EXPERT_INFLUENCE · camps/personas → ANALYSTE du pays · format/HTML → MASTAURIGE · rédaction → SCENARISTE · images → IMAGIER · méthodo → AURIGE. ⚠ Question ouverte : **DELATTRE 26 est-il un exercice de type AURIGE ?** Si oui, créer `AURIGE\DELATTRE\MEMOIRE.md` (convention « un dossier par exercice »). Voir [[retex_minotaure_26]], [[aurige7bb_actif]], [[aurige_template_base]], [[vierge_porting_fin_minautore]].
