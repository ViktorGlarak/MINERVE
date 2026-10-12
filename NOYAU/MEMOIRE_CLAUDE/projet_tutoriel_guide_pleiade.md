---
name: projet-tutoriel-guide-pleiade
description: "Projet tutoriel/guide interactif PLÉIADE (lancé 2026-10-08) — décisions de conception, LOCALHOST UNIQUEMENT jusqu'au feu vert"
metadata:
  node_type: memory
  type: project
  originSessionId: 699185de-99a6-4263-a321-d605be7e2b29
  modified: 2026-10-11T11:53:34.821Z
---

Projet lancé le 2026-10-08 : guide interactif qui oriente joueur/animateur dans les outils PLÉIADE selon les instances déployées. Phase discussion (pas de code tant que l'utilisateur ne le demande pas). Avis DESIGNER n°81.

Décisions utilisateur (2026-10-08) :
- Zone d'entraînement envisagée comme réponse au volet « fictif ».
- L'aide reste accessible PENDANT l'exercice (se perfectionner sur une app).
- Progression suivie par compte (d'un poste à l'autre).
- Contenu rédigé par PLEIADE + responsables d'apps + cellule d'animation ; fiches stockées dans le dossier de l'agent PLEIADE (`PLEIADE\GUIDE\`, une note par tâche), PAS dans vault/. Scénario-tutoriel sur un modèle Skolkan existant, 1 h max, chaque stagiaire a sa copie et avance à son rythme. Détail : PLEIADE\MEMOIRE.md § « Chantier — Tutoriel guidé ».
- Test avec animateurs, mais d'abord tout en localhost.

Reprise 2026-10-11 — décisions : (1) décor commun + chaque stagiaire son avatar et son fil rouge (cloisonnement par l'action, pas par la vue) ; (2) panneau de guide hors fiction dans la barre de zone, coche au geste détecté, progression par compte ; (3) étapes déclenchées par l'action, l'animateur suit sans piloter. Citoyens IA dans le décor = phase ultérieure. Prochaine étape : maquette DESIGNER du panneau (localhost).

11/10 après-midi : première version CODÉE et JOUÉE en local (branches `tutoriel` de pleiade-platform, eho, app-social, app-admin ; rien de poussé). Zone locale `tuto-locale` (famille `entrainement`, images `:tuto`), montage par `C:\CECPC\pleiade\dev\zone-tuto\` (comptes animateur-tuto / stagiaire01-12, mot de passe d'essai local). Détails et reste à faire : PLEIADE\MEMOIRE.md, chantier Tutoriel. ⏸️ En pause par choix de l'utilisateur (11/10 ~13 h 45) : un push ne le montrera PAS dans DELATTRE 26 (famille exercice → inerte) ; serveur = zone dédiée famille « entrainement » ; bouton « Aide » d'exercice réel non codé.

**Why:** l'utilisateur teste tout lui-même avant toute mise en serveur.
**How to apply:** ⛔ rien sur le serveur (ni push, ni déploiement de zone) sans son feu vert explicite ; voir [[feedback-tester-en-local-avant-push]] et [[agent-designer]].
