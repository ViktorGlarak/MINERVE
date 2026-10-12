---
name: feedback-numeros-fictifs
description: Plages de numéros de téléphone fictifs à utiliser dans les injects — jamais de XX XX XX XX
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 73fcca0d-c040-42d3-9859-fa36df54c216
---

Ne jamais écrire `XX XX XX XX` dans un numéro de téléphone fictif dans les injects, SMS, courriers ou documents d'exercice.

Utiliser les plages fictives ci-dessous — au format valide français, crédibles, n'appartenant pas à un abonné réel :

| Région / Zone | Format | Exemple concret |
|---|---|---|
| 01 — Île-de-France | `01 99 00 XX XX` | 01 99 00 47 23 |
| 02 — Nord-Ouest / Outre-mer | `02 61 91 XX XX` | 02 61 91 08 54 |
| **03 — Nord-Est (Lorraine)** | **`03 72 67 XX XX`** | **03 72 67 14 89** |
| 04 — Sud-Est | `04 51 08 XX XX` | 04 51 08 37 62 |
| 05 — Sud-Ouest | `05 36 49 XX XX` | 05 36 49 91 05 |

**Why:** Les prompts image IA généraient des numéros avec des "XX XX XX XX" non réalistes. L'utilisateur veut des injects crédibles à 100%.

**How to apply:** Pour tout contenu d'exercice mentionnant un numéro de téléphone français :
- Identifier la zone géographique du contenu
- Appliquer le préfixe correspondant + 4 chiffres aléatoires concrets
- **AURIGE 2BB (Lorraine) → `03 72 67` systématiquement**
- S'applique à : SMS psyops, tweets, bio d'avatars, courriers fictifs, formulaires, captures d'écran, prompts IA

---

## Numéros canoniques — attributions permanentes

| Institution | Numéro fixe | Format international | Exercices |
|---|---|---|---|
| **Palais présidentiel DAC / HPARIS** | **01 99 00 01 00** | +33 1 99 00 01 00 | Tous exercices |

**Règle :** Ce numéro est FIXE pour tous les exercices. Ne jamais en attribuer un autre au palais présidentiel de Dacia Romania / Arnland. Utiliser systématiquement `01 99 00 01 00` dans tous les documents officiels de la présidence (courriers Pallesson, en-têtes, pieds de page, fiches de contact).
