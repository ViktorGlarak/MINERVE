# ROUTAGE — Arbre de décision Mercure

Utilisé par Claude (NOYAU) pour choisir quel agent appeler.

---

## Principe de compétence — règle absolue

> **NOYAU (Claude) est toujours la dernière main.**
> Chaque output d'agent Ollama est relu et raffiné par NOYAU avant livraison.
> L'agent fournit la base (countrybook, narrative, structure) — NOYAU élève la qualité finale.
> L'utilisateur ne reçoit jamais un draft brut d'agent local.

---

## Arbre de décision

```
La demande concerne...
│
├── du CODE ou de la TECHNIQUE ?
│   ├── Écriture, debug, refactoring, architecture → ARCHITECTE (qwen2.5-coder:14b)
│   └── Erreur incompréhensible, logique de programme → PENSEUR puis ARCHITECTE
│
├── un RAISONNEMENT ou une PLANIFICATION ?
│   ├── Problème complexe, stratégie, arbitrage → PENSEUR (deepseek-r1:14b, local)
│   ├── Évaluation DOCTRINALE d'une production ILI (Sun Tzu / Morelli 10 principes → LO) → EXPERT_INFLUENCE
│   │       (dépôt doctrinal unique : EXPERT_INFLUENCE\REFERENCES\ ; PENSEUR raisonne en citant cette doctrine)
│   └── Plan d'action avec du code → PENSEUR (plan) + ARCHITECTE (exécution)
│
├── une IDÉE NON ABOUTIE à stocker / faire mûrir (sans produire) ?
│   └── → BROUILLON (deepseek-r1:14b, LOCAL — économise les tokens) ; promu ensuite vers l'agent compétent
│
├── de la RÉDACTION en français ?
│   ├── Mail, synthèse, rapport, correction → SECRÉTAIRE (mistral-nemo)
│   └── Documentation technique → ARCHITECTE (contenu) + SECRÉTAIRE (mise en forme)
│
├── une TÂCHE SIMPLE et RAPIDE ?
│   ├── Formatage JSON/CSV, extraction, tri → ÉCLAIREUR (llama3.1:8b)
│   └── Traduction courte, question factuelle → ÉCLAIREUR (llama3.1:8b)
│
├── une question sur le SYSTÈME MERCURE lui-même ?
│   └── Claude répond directement (NOYAU)
│
├── un PROMPT pour générer une IMAGE ?
│   └── IMAGIER (llama3.1:8b) → prompt Gemini ou Flow
│
├── un PROMPT pour générer une VIDÉO ?
│   └── CINÉASTE (llama3.1:8b) → prompt + paramètres LTX 2.3 / ComfyUI
│
├── du CONTENU DE SCÉNARIO (article, post, inject, tract, document fictif) ?
│   └── SCÉNARISTE (mistral-nemo)
│
├── un DISCOURS DE PERSONNAGE POLITIQUE ?
│   ├── Personnage mercurien (Olamao, Junker, Stoph, Ribiki, ...) → ANALYSTE (deepseek-r1:14b)
│   ├── Personnage DR / Arnland (Président, ministres, ...) → ANALYSTE_ARN (deepseek-r1:14b)
│   ├── Personnage Ruthnia Bella (Youkachenko, opposition Tikhanov/Saniki, gouvernement RB) → ANALYSTE_BOT (deepseek-r1:14b)
│   ├── Personnage OTAN ou figure internationale fictive → SCÉNARISTE (mistral-nemo)
│   └── Figure RÉELLE (Rutte SG OTAN, Guterres ONU, ...) → NOYAU (Claude) directement
│       Raison : les figures réelles nécessitent un contrôle éthique et de cohérence que Claude assure lui-même
│       ⚠ Youkachenko n'est PAS une figure réelle — c'est le président FICTIF de Ruthnia Bella (calqué sur Loukachenko) → ANALYSTE_BOT
│
├── une VOIX à générer (paramètres OmniVoice, texte TTS, profil voix) ?
│   └── VOIX (mistral-nemo)
│
├── une question sur la RÉPUBLIQUE DE MERCURE (politique, militaire, géo, personnages, scénarios) ?
│   └── ANALYSTE (deepseek-r1:14b) → Countrybook MER
│
├── une question sur ARNLAND / DACIE ROMANIE (politique, militaire, géo, personnages, scénarios) ?
│   └── ANALYSTE_ARN (deepseek-r1:14b) → Countrybook ARN
│       Note : "Arnland" dans ORION 26 = "Dacie Romanie (DR)" dans AURIGE 2BB
│
├── une question sur la RUTHNIA BELLA (régime Youkachenko, opposition Tikhanov/Saniki, médias RB/BC1, arcs narratifs RB) ?
│   └── ANALYSTE_BOT (deepseek-r1:14b) → dossier `ANALYSTE\BOTHNIA\`
│       Note : Ruthnia Bella = Biélorussie fictive. Youkachenko, opposition et BC1 sont des entités FICTIVES → ne jamais router vers NOYAU comme "figure réelle"
│       Rappel camps : Youkachenko + BC1 = 🔴 rouge · Tikhanov (Nouvelle Pahonie) = 🔴 rouge pro-MER · Saniki (Bison Libre) = 🔴 rouge pro-MER
│
├── une question sur le CALENDRIER ÉDITORIAL ou la COHÉRENCE NARRATIVE d'AURIGE 2BB ?
│   └── GUILLAUME (claude-opus-4-7) → chef d'orchestre éditorial AURIGE 2BB
│       Cas : "qu'est-ce qu'on publie aujourd'hui ?", "est-ce cohérent avec ce qui est sorti ?", "quelle est la prochaine étape narrative ?"
│       Sait : tous les acteurs, camps, médias fictifs, statut de chaque publication (publié / à produire / date à définir)
│
├── une question sur le CALENDRIER ÉDITORIAL ou la COHÉRENCE NARRATIVE d'AURIGE 7BB ?
│   └── MINAUTORE (claude-opus-4-7) → chef d'orchestre éditorial AURIGE 7BB
│       Cas : mêmes que GUILLAUME mais pour l'exercice AURIGE 7BB
│       Note : synchromatrice AURIGE 7BB à ingérer — agent initialisé le 2026-05-30
│
├── du CONTENU RS FICTIF pour un exercice AURIGE (entraînement PC niveau brigade) ?
│   └── MASTAURIGE (mistral-nemo:latest) → avatars CASW, tweet cards HTML offline
│       Cas : onglet RS de l'agrégateur WEB, posts fictifs scénario AURIGE 2BB et exercices brigade
│       Note : MASTAURIGE est INDÉPENDANT de Mastorion — pas de lien avec la plateforme sociale fictive
│
├── un POST / THREAD / CAMPAGNE réseaux sociaux fictifs (Mastodon, Mastorion) ?
│   └── MASTODONTE (mistral-nemo:latest) → Expert Mastodon API + contenu RS exercices
│       Cas : propagande, contre-narrative, hashtags, sondages, threads coordonnés
│       Note : Mastorion = plateforme distincte avec IA dédiée (développement futur — hors système Mercure actuel)
│
└── une question sur la DOCTRINE ILI, la SYNCHROMATRICE ou la PLANIFICATION des effets informationnels ?
    └── EXPERT_INFLUENCE (Claude Opus 4.7) → Expert doctrine ILI transversal
        Cas : "comment structurer une synchromatrice ?", "quel effet ILI pour cet inject ?", "la séquence est-elle cohérente ?", "calibrage réalisme opération d'influence"
        Note : transversal tous exercices — travaille en dialogue avec GUILLAUME (calendrier) et ANALYSTE (contenu pays)
```

---

## Commandes API Ollama

```powershell
# Template d'appel générique
$body = @{
    model  = "NOM_DU_MODELE"
    prompt = "VOTRE_PROMPT"
    stream = $false
} | ConvertTo-Json

$r = Invoke-RestMethod -Uri "http://localhost:11434/api/generate" `
     -Method Post -Body $body -ContentType "application/json" -TimeoutSec 120

$r.response
```

> Temps de chargement représentatifs par **type de modèle** (le registre complet des agents est dans `CLAUDE.md`).

| Modèle | Exemples d'agents | Temps de chargement estimé |
|---|---|---|
| qwen2.5-coder:14b | ARCHITECTE | ~15-30s (1ère fois) |
| deepseek-r1:14b | PENSEUR, ANALYSTE, ANALYSTE_ARN, ANALYSTE_BOT, **BROUILLON** | ~15-30s (1ère fois) |
| mistral-nemo:latest | SECRÉTAIRE, SCÉNARISTE, VOIX, MASTODONTE, MASTAURIGE | ~10s |
| llama3.1:8b | ÉCLAIREUR, IMAGIER, CINÉASTE, ARCHIVISTE | ~5s |
| Claude (cloud) | NOYAU, GUILLAUME, EXPERT_INFLUENCE, MINAUTORE | immédiat (API) |
