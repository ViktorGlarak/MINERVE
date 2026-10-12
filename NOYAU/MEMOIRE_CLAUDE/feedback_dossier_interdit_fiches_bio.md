---
name: feedback-dossier-interdit-fiches-bio
description: "Dossier interdit d'accès automatique — D:\\CECPC\\DOC REF\\MERCURE\\RENS\\01_Fiches bio (documents sensibles, demander avant)"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 4377e89f-f0dd-40af-851d-ddfb523fd276
---

**Interdiction d'accès automatique** au dossier `D:\CECPC\DOC REF\MERCURE\RENS\01_Fiches bio` et à tout son contenu (lecture, recherche, glob, bash/powershell). Demandé le 2026-06-25.

**Why:** ce dossier contient des documents **sensibles qui ne doivent pas se retrouver sur internet**. Un accès silencieux (ex. les `allow` larges `Read(//d/CECPC/**)` et `Read(//d/CECPC/DOC REF/**)` déjà présents dans settings.local.json) risquerait de les exposer.

**How to apply:**
- Ne **jamais** y accéder par défaut. Si un accès devient nécessaire pour une tâche, **demander d'abord l'autorisation explicite** à l'utilisateur en expliquant pourquoi, et attendre son feu vert.
- Garde-fou en place : règle `permissions.ask` dans `.claude\settings.local.json` (Read/Glob/Grep sur `//d/CECPC/DOC REF/MERCURE/RENS/01_Fiches bio/**`) → prime sur les `allow` larges et fait apparaître une demande de confirmation.
- Vaut aussi pour Bash/PowerShell (cat, Get-Content, grep, find…) visant ce chemin : demander avant.
