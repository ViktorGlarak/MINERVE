# CONVERGENCE — Fusion des connaissances

## Objectif
Centraliser et consolider les connaissances accumulées par tous les agents pour :
1. Avoir une vue globale de ce qui a été appris
2. Préparer un dataset structuré pour un futur fine-tuning sur Ollama

## Fichiers
- `SYNTHESE.md` — Connaissance agrégée mise à jour manuellement ou par Claude
- `DATASET/` — Paires question/réponse au format JSONL pour fine-tuning futur

## Format du dataset (JSONL)
```json
{"prompt": "Question ou tâche posée", "response": "Réponse idéale de l'agent", "agent": "ARCHITECTE", "date": "2026-05-06"}
```

## Fréquence de mise à jour recommandée
Après chaque session significative : extraire les échanges importants et les ajouter dans DATASET/.
