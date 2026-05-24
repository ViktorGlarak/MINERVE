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
- Figure réelle (Rutte, Loukachenko) → NOYAU (Claude) directement
- Figure OTAN fictive → SCÉNARISTE
NOYAU assure le contrôle qualité final dans tous les cas.

---

## Décisions d'architecture

### [2026-05-06] Claude comme orchestrateur réel
Choix validé : Claude appelle les modèles Ollama via API PowerShell (localhost:11434).
Continue (VSCode) reste disponible pour accès direct aux agents individuels.
Niveau 2 (script Python autonome) prévu pour une prochaine étape.

### [2026-05-24] 14 agents au total
4 généralistes (ARCHITECTE, PENSEUR, SECRÉTAIRE, ÉCLAIREUR) +
3 spécialistes exercices (IMAGIER, CINÉASTE, SCÉNARISTE) +
6 agents spécialisés (VOIX, ARCHIVISTE, ANALYSTE, ANALYSTE_ARN, MASTODONTE, MASTAURIGE) +
NOYAU (Claude — orchestrateur)

ANALYSTE_ARN ajouté le 2026-05-23 — expert Arnland/Dacie Romanie, deepseek-r1:14b partagé avec ANALYSTE + PENSEUR.
MASTAURIGE ajouté le 2026-05-24 — contenus RS fictifs pour exercices AURIGE (entraînement PC niveau brigade), avatars CASW, tweet cards HTML offline. mistral-nemo:latest partagé avec MASTODONTE + SCÉNARISTE + SECRÉTAIRE + VOIX. Indépendant de Mastorion (plateforme distincte, IA dédiée future).
