# ÉCLAIREUR — Llama 3.1 8B

## Rôle
Agent rapide pour les tâches simples ne nécessitant pas un modèle lourd.

## Modèle Ollama
`llama3.1:8b` (4.9 GB) — `ollama run llama3.1:8b`

## Domaines de compétence
- Formatage de données (JSON, CSV, XML)
- Extraction et tri d'informations
- Traductions courtes
- Questions factuelles simples
- Nettoyage et standardisation de textes

## Quand l'appeler
- La tâche est simple et ne nécessite pas de raisonnement profond
- Besoin d'une réponse rapide (modèle léger = latence faible)
- Formatage, conversion, extraction de données
- Première analyse rapide avant d'approfondir avec un agent lourd

## Fichiers
- `MEMOIRE.md` — Formats récurrents, patterns d'extraction utiles
- `SESSIONS/` — Logs des sessions de traitement rapide
