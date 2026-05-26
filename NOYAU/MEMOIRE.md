# MÉMOIRE — NOYAU (Orchestrateur)

## Format d'entrée
```
### [YYYY-MM-DD] Catégorie : Titre
Contenu de la connaissance acquise.
```

---

## Contexte du projet — CE QUE FAIT L'UTILISATEUR
Mercure est un assistant de production d'exercices militaires et civils de gestion de crise.
L'utilisateur crée des exercices complets incluant : scénarios, personnages fictifs, documents, images IA, vidéos IA, montage Premiere Pro.
Exercices de référence : ORION 26 (grand exercice multi-cellules, Vienne/Poitiers) et AURIGE 2BB (production média, Lorraine).

## Préférences utilisateur

### [2026-05-06] Init : Création du système Mercure
Système multi-agents créé. L'utilisateur souhaite un orchestrateur (Claude) qui délègue aux agents Ollama locaux.
Préférence : réponses en français, annonce toujours de l'agent qui répond.

### [2026-05-06] Règle de mémoire proactive
L'utilisateur veut que Claude mette à jour automatiquement les fichiers MEMOIRE.md des agents concernés après chaque apprentissage, correction ou avancée significative. Objectif : ne jamais avoir à répéter un sujet déjà traité. Appliquer après chaque session productive.

### [2026-05-06 — mis à jour 2026-05-23] Règle QC — Principe de compétence
Claude (NOYAU) est plus performant que les agents Ollama locaux. En conséquence :
- **Tout output d'agent est systématiquement relu par NOYAU** avant livraison à l'utilisateur
- Si le contenu est perfectible (fond, forme, cohérence géopolitique, ton), NOYAU ne rejette pas — il **utilise le travail de l'agent comme base** et le raffine directement
- L'agent fournit la matière première (ancrage countrybook, structure narrative) ; NOYAU élève la qualité finale
- L'utilisateur ne reçoit que la version finale contrôlée — jamais un draft brut d'agent Ollama
Ce principe s'applique à tous les agents sans exception : ANALYSTE, ANALYSTE_ARN, SCÉNARISTE, IMAGIER, etc.

### [2026-05-06] Texte dans les images
Quand l'utilisateur fournit un texte précis à afficher dans une image générée, ce texte doit être intégré mot pour mot dans le prompt, entre guillemets, avec "legible word for word". Jamais résumer ou paraphraser.

---

## Patterns de routage appris

### [2026-05-06] Mockups UI (WhatsApp, interfaces mobiles)
llama3.1:8b insuffisant pour décrire fidèlement des interfaces mobiles.
Claude répond directement pour ce type de demande sans passer par l'IMAGIER.

### [2026-05-23] Discours de personnages politiques
SCÉNARISTE seul est insuffisant — il écrit bien mais sans ancrage géopolitique réel.
Règle validée :
- Personnage mercurien → ANALYSTE rédige le discours
- Personnage DR / Arnland → ANALYSTE_ARN rédige le discours
- Figure réelle (Rutte, Youkachenko) → NOYAU (Claude) directement
- Figure OTAN fictive → SCÉNARISTE
NOYAU assure le contrôle qualité final dans tous les cas.

---

## Décisions d'architecture

### [2026-05-06] Claude comme orchestrateur réel
Choix validé : Claude appelle les modèles Ollama via API PowerShell (localhost:11434).
Continue (VSCode) reste disponible pour accès direct aux agents individuels.
Niveau 2 (script Python autonome) prévu pour une prochaine étape.

### [2026-05-25 — mis à jour 2026-05-25] 16 agents au total
4 généralistes (ARCHITECTE, PENSEUR, SECRÉTAIRE, ÉCLAIREUR) +
3 spécialistes exercices (IMAGIER, CINÉASTE, SCÉNARISTE) +
7 agents spécialisés (VOIX, ARCHIVISTE, ANALYSTE, ANALYSTE_ARN, MASTODONTE, MASTAURIGE, GUILLAUME) +
NOYAU (Claude — orchestrateur)

ANALYSTE_ARN ajouté le 2026-05-23 — expert Arnland/Dacie Romanie, deepseek-r1:14b partagé avec ANALYSTE + PENSEUR.
MASTAURIGE ajouté le 2026-05-24 — contenus RS fictifs pour exercices AURIGE (entraînement PC niveau brigade), avatars CASW, tweet cards HTML offline. mistral-nemo:latest partagé avec MASTODONTE + SCÉNARISTE + SECRÉTAIRE + VOIX. Indépendant de Mastorion (plateforme distincte, IA dédiée future).
GUILLAUME ajouté le 2026-05-25 — chef d'orchestre éditorial AURIGE 2BB. Connaît tous les acteurs, camps, médias fictifs et gère le calendrier de publication (statut publié/à produire/date à définir). **Migration 2026-05-25 : deepseek-r1:14b → claude-opus-4-7 (cloud)** — même modèle qu'EXPERT_INFLUENCE, pour garantir la qualité doctrinale et narrative. Partage avec EXPERT_INFLUENCE, ANALYSTE, ANALYSTE_ARN.
EXPERT_INFLUENCE ajouté le 2026-05-25 — expert doctrine ILI et conception de synchromatrice. Transversal tous exercices. Claude Opus 4.7 (cloud) — modèle susceptible d'évoluer sur décision de l'utilisateur. Partage avec GUILLAUME, ANALYSTE, ANALYSTE_ARN, PENSEUR.

### [2026-05-25] Dossier GUILLAUME — créé + GAME PLAN AURIGE 2BB ingéré
Dossier `GUILLAUME\` créé à la racine Mercure (manquait). Contient :
- `GUILLAUME\README.md` — rôle, modèle, fichiers de référence
- `GUILLAUME\MEMOIRE.md` — GAME PLAN AURIGE 2BB ingéré (données MAINBODY réelles) + 8 axes lacunaires + 15 propositions ILI doctrine russe

**Données MAINBODY désormais connues de GUILLAUME :**
- D+35 (30 mai) = CLIMAX — RUPTURE LDP, SAISIE HSARREBOURG — GAP CRITIQUE (aucun inject de victoire MER)
- D+32–34 : DPs fuyant HLUNEVILLE N4 → ancrage humanitaire (08.01.02i TV4 Panique)
- D+37 : Arrivée 13e RG DAC — opportunité narrative "OTAN envoie des renforts car elle perd"
- D+37–38 : Population hostile HLUNEVILLE / D+39+ : population hostile HSARREBOURG
- AUTH ARN exactions IRREG confirmées — à nier en architecture 3 couches (P-05)

**15 propositions ILI (P-01 à P-15) soumises à validation :**
`EXER\AURIGE 2BB\00_Boites à outils\MASTAURIGE\PROPOSITIONS_ILI_DOCTRINERUSSE.md`
Couvrent 8 axes manquants (déni plausible, blanchiment, noyau vérité, industrialisation, localisation, opportunisme, saturation, appropriation)

---

### [2026-05-25] Dossier ANALYSTE — structure par pays + Countrybook Mercure ingéré
Dossier `ANALYSTE\` créé à la racine Mercure, centralise tous les analystes par pays :
- `ANALYSTE\MERCURE\` — Expert Mercure (Countrybook complet) + Doctrine OI Storm-1516 (rapport VIGINUM TLP:CLEAR)
- `ANALYSTE\ARNLAND\` — Expert Arnland / Dacie Romanie (migré depuis `ANALYSTE_ARN\`, nom du pays variable selon exercice)
- `ANALYSTE_ARN\` — supprimé le 2026-05-25

**ANALYSTE MERCURE maîtrise désormais :**
1. Countrybook Mercure (943 paragraphes, CB MERCURE FR.docx) — géographie, politique, militaire (607K, triade nuc), économie (PIB 550 Mds$), société (3 ethnies Inen), info (172/180 RSF), infrastructure, tous les personnages
2. Storm-1516 (VIGINUM, 77 opérations) — 16 TTP, 4 phases de diffusion, acteurs (DOUGAN, KOROVINE, KHOROCHENKY)
Prompt système mis à jour : `SYSTEME\PROMPTS\analyste.md`.
