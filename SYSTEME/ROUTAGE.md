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
├── une question sur le SYSTÈME MINERVE lui-même ?
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
├── une question sur le CALENDRIER ÉDITORIAL ou la COHÉRENCE NARRATIVE d'AURIGE 7BB / MINOTAURE 26 ?
│   └── MINAUTORE (claude-opus-4-7) → chef d'orchestre éditorial AURIGE 7BB
│       Cas : mêmes que GUILLAUME mais pour l'exercice AURIGE 7BB
│       ⚠ EXERCICE CLOS le 2026-07-03 → MINAUTORE = ARCHIVE DE RÉFÉRENCE (plus l'exercice actif)
│       Contient le RETEX : MINAUTORE\RETEX_MINOTAURE_26.md (à lire avant tout nouvel exercice)
│
├── une question sur DELATTRE 26 (dit « DELATTRE ») — calendrier éditorial, cohérence narrative, injects ?
│   └── DELATTRE (claude-opus-4-7) → chef d'orchestre éditorial DELATTRE 26  ⭐ EXERCICE À VENIR
│       Cas : mêmes que GUILLAUME / MINAUTORE, mais pour DELATTRE 26
│       Successeur de : GUILLAUME (2BB) → MINAUTORE (7BB) → DELATTRE
│       Note : agent créé le 2026-07-22 — identité de l'exercice (unité, niveau, dates, zone, camps) À RENSEIGNER
│       Réflexe : DELATTRE hérite du RETEX MINOTAURE (calibrer TACTIQUE, exiger la boucle de retour,
│                GT productifs, casser les silos) + des actifs réutilisables (EHO 7BB, vierge MASTAURIGE v0.3,
│                registre avatars, chartes médias)
│
├── du CONTENU RS FICTIF pour un exercice AURIGE (entraînement PC niveau brigade) ?
│   └── MASTAURIGE (mistral-nemo:latest) → avatars CASW, tweet cards HTML offline
│       Cas : onglet RS de l'agrégateur WEB, posts fictifs scénario AURIGE 2BB et exercices brigade
│       Note : MASTAURIGE est INDÉPENDANT de MASTORION — outillage HTML statique niveau brigade
│
├── un POST / THREAD / CAMPAGNE réseaux sociaux fictifs (Mastodon) ?
│   └── MASTODONTE (mistral-nemo:latest) → Expert Mastodon API + contenu RS exercices
│       Cas : propagande, contre-narrative, hashtags, sondages, threads coordonnés
│
├── une question sur le SYSTÈME GLOBAL (orchestrateur, zones, instances, Keycloak, Traefik, serveur, VPN, déploiement, articulation entre apps) ?  ⭐ créé 2026-09-11
│   └── PLEIADE (claude-opus-4-7) → Expert du système PLEIADE — orchestrateur de zones d'exercice
│       Cas : "comment déployer une instance ?", "comment marchent les zones/realms Keycloak ?", "qui parle à qui entre eho et le réseau social ?", "état du serveur / de l'infra"
│       Chemins : C:\CECPC\pleiade\ (racine) · pleiade-platform · mastorion · eho · (pleiade-infra NON cloné)
│       ⚠ RÈGLE : dépôts PARTAGÉS avec le développeur — aucun commit/push sans demande explicite ; serveur Podman ROOTFUL → toujours sudo, prod jamais touchée sans autorisation
│       ⚠ NOM : « MASTORION » ne désigne PLUS le système (→ PLEIADE) mais seulement le réseau social, qui sera renommé
│       Collabore : MASTORION (détail du réseau social), ARCHITECTE (code), MASTAURIGE, EXPERT_INFLUENCE, DELATTRE
│
├── une question sur le RÉSEAU SOCIAL d'exercice (API social, admin, cockpit, sentinel, modèle de données, scénarios) ?  ⭐ créé 2026-07-27, recadré 2026-09-11
│   └── MASTORION (claude-opus-4-7) → Expert du réseau social — exercices DIVISION/CORPS
│       Cas : "comment fonctionne le feed / les scénarios ?", "où brancher les avatars/camps ?", "porter le savoir MASTAURIGE dans l'app"
│       Chemin : C:\CECPC\pleiade\app-social  (⚠ les anciens clones D:\ et C:\CECPC\MASTORION\mastorion-v0 sont DÉPASSÉS)
│       ⚠ RÈGLE : dépôt partagé — aucun commit/push sans autorisation explicite de l'utilisateur
│       Collabore : PLEIADE (insertion dans le système), MASTAURIGE (savoir hérité), ARCHITECTE (code), EXPERT_INFLUENCE (ILI), SCÉNARISTE, analystes pays
│
├── une question sur le système LEAC (documentation, décisions, suivi du projet) ?  ⭐ créé 2026-09-17
│   └── LEAC (claude-opus-4-7) → Référent unique du système LEAC
│       Cas : "qu'est-ce que LEAC ?", "où en est le projet ?", "qu'a-t-on décidé ?", "que reste-t-il à faire ?", tout document LEAC à ingérer
│       Fichiers : LEAC\MEMOIRE.md (état durable) · LEAC\JOURNAL.md (historique) · LEAC\REFERENCES\ (documents fournis)
│       ⭐ RÈGLE (demandée par l'utilisateur) : le CONSULTER dès que LEAC est évoqué, même en passant — et le METTRE À JOUR à chaque avancée, à l'ouverture et à la fermeture de session
│       ⚠ ÉTAT : identité du système ENTIÈREMENT à renseigner (objet, nature, périmètre, acteurs, échéances) — documentation attendue ; NE RIEN SUPPOSER tant qu'un champ porte ⚠️
│       Collabore : ⚠ à préciser une fois le périmètre connu — a priori ARCHITECTE (code), PENSEUR (arbitrage), SECRÉTAIRE (rédaction), PLEIADE si rattachement plateforme
│
├── un avis de DESIGN sur un site ou un applicatif, ou un document de design à ingérer ?  ⭐ créé 2026-09-24
│   └── DESIGNER (claude-opus-4-7) → Conseiller en design (UI / UX)
│       Cas : "c'est lisible ?", "comment rendre cet écran plus clair ?", "quelle couleur / quel espacement ?", "cette fenêtre est-elle accessible ?", "ingère ce design system / cet article"
│       Fichiers : DESIGNER\MEMOIRE.md (terrain + doctrine sourcée) · DESIGNER\JOURNAL.md · DESIGNER\REFERENCES\REF-NN_*.md
│       ⚠ RÈGLE : il CONTRIBUE, il ne tranche pas — besoin utilisateur, chartes des médias fictifs, modèles officiels (CR, ordres) et choix PLEIADE/ARCHITECTE priment ; il ne code pas
│       Collabore : PLEIADE, MASTORION, LEAC (apps), MASTAURIGE (chartes d'exercice), ARCHITECTE (mise en œuvre), IMAGIER (visuels)
│
├── une question de SÉCURITÉ / CYBERSÉCURITÉ sur PLÉIADE, ou un document de sécurité à ingérer ?  ⭐ créé 2026-10-01
│   └── CYBERSECU (claude-opus-4-7) → Référent cybersécurité de PLÉIADE
│       Cas : "est-ce sûr ?", "comment protéger X ?", "quels en-têtes / quel TLS / quelle taille de clé ?", "ce secret est-il exposé ?", "audit de sécurité d'une app", "anonymat des comptes", "ingère ce guide ANSSI"
│       Fichiers : CYBERSECU\MEMOIRE.md (doctrine sourcée + posture + règles décidées + plan) · CYBERSECU\JOURNAL.md · CYBERSECU\REFERENCES\REF-NN_*.md
│       ⭐ RÈGLE (demandée par l'utilisateur) : le CONSULTER dès qu'un sujet touche la sécurité, et le METTRE À JOUR à chaque décision ou correction de sécurité
│       ⚠ Il conseille et vérifie, il ne pousse rien : mise en œuvre par PLEIADE / ARCHITECTE, tests en local, accord de l'utilisateur
│       Collabore : PLEIADE (plateforme), ARCHITECTE (code), MASTORION (réseau social), LEAC (tablette hors ligne), DESIGNER (écrans)
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
| Claude (cloud) | NOYAU, GUILLAUME, EXPERT_INFLUENCE, MINAUTORE, DELATTRE, **MASTORION** | immédiat (API) |
