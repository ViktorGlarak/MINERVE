# MÉMOIRE — VOIX (OmniVoice / ComfyUI)

## Format d'entrée
```
### [YYYY-MM-DD] Exercice : [NOM] — Profil : [VOIX]
Texte généré, paramètres utilisés, résultat, leçon.
```

---

## Réglages optimaux par profil — [2026-05-06]

### Journaliste féminine FR (voix off JT)
**Mode :** Voice Clone
**Référence audio :** femme-journaliste-Claire Chazal (fichier existant)
**Whisper :** whisper-large-v3-turbo (équilibre qualité/VRAM)
**Paramètres recommandés :**
- steps : **64** (qualité production)
- guidance_scale : **2.0**
- speed : **0.95** (légèrement posé, style JT)
- class_temperature : **0.0** (cohérence avec la référence)
- denoise : true | preprocess_prompt : true | postprocess_output : true
- keep_model_loaded : true (si plusieurs segments à générer)

**Pour le texte :** Ponctuation soignée — OmniVoice lit les virgules et points.
Éviter les abréviations non prononcées. Écrire "N.O.M." avec les points pour forcer la diction lettre par lettre.

---

### Expert sécurité intérieure (interviewé)
**Mode :** Voice Design (pas de référence audio)
**Attributs :** `male, middle-aged, low pitch`
**Paramètres recommandés :**
- steps : **64**
- guidance_scale : **2.5** (plus aligné = plus autoritaire)
- speed : **0.90** (parole mesurée, réfléchie)
- class_temperature : **0.5** (légère variation = plus naturel)

---

### Citoyen français (résident, témoin)
**Mode :** Voice Design
**Attributs :** `female, middle-aged, medium pitch` ou `male, young, medium pitch`
**Paramètres recommandés :**
- steps : **32** (moins de perfection = plus naturel)
- guidance_scale : **2.0**
- speed : **1.0** (rythme naturel)
- class_temperature : **1.0** (plus de variation = plus humain)

---

### Résident anglophone (scénario bilingue AURIGE)
**Mode :** Voice Design
**Attributs :** `male, young, medium pitch, american accent`
**Paramètres recommandés :**
- steps : **64**
- guidance_scale : **2.0**
- speed : **1.05**

---

## Règles générales validées

### Texte pour voix off journaliste
- Écrire le texte exactement comme il doit être prononcé
- "N.O.M." → le modèle prononce "N point O point M point" — tester et ajuster si besoin
- "HNancy" → écrire "Nancy" dans le texte TTS (le H est un préfixe exercice, pas prononcé)
- Ponctuation = intonation : virgule = pause courte, point = pause longue
- Majuscules n'affectent pas la prononciation

### Tags non-verbaux utiles pour les exercices
- Expert interviewé : `[confirmation-en]` pour acquiescements naturels
- Citoyen inquiet : `[sigh]` en début de réplique
- Journaliste : éviter les tags non-verbaux (voix professionnelle neutre)

---

## Résultats validés par exercice

### AURIGE 2BB
<!-- À alimenter après les premières générations -->
