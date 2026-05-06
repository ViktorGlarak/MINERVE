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

### [2026-05-06] Règle QC
Claude contrôle systématiquement la qualité des réponses des agents Ollama avant livraison. Si FAIL, Claude corrige directement et note la leçon. L'utilisateur ne doit jamais avoir à "passer derrière" un agent.

### [2026-05-06] Texte dans les images
Quand l'utilisateur fournit un texte précis à afficher dans une image générée, ce texte doit être intégré mot pour mot dans le prompt, entre guillemets, avec "legible word for word". Jamais résumer ou paraphraser.

---

## Patterns de routage appris

### [2026-05-06] Mockups UI (WhatsApp, interfaces mobiles)
llama3.1:8b insuffisant pour décrire fidèlement des interfaces mobiles.
Claude répond directement pour ce type de demande sans passer par l'IMAGIER.

---

## Décisions d'architecture

### [2026-05-06] Claude comme orchestrateur réel
Choix validé : Claude appelle les modèles Ollama via API PowerShell (localhost:11434).
Continue (VSCode) reste disponible pour accès direct aux agents individuels.
Niveau 2 (script Python autonome) prévu pour une prochaine étape.

### [2026-05-06] 7 agents au total
4 généralistes (ARCHITECTE, PENSEUR, SECRÉTAIRE, ÉCLAIREUR) +
3 spécialistes exercices (IMAGIER, CINÉASTE, SCÉNARISTE)
