---
id: A7
parcours: animateur
ordre: 7
app: admin
titre: "Lire le journal et corriger une publication"
consigne: "Consultez le journal de votre scénario et modifiez une publication avant son départ."
validation: auto
signal: "PATCH /api/bff/scenarios/{id}/items/{itemId}"
niveau: premiers-pas
---

# Lire le journal et corriger une publication

> Consultez le journal de votre scénario et modifiez une publication avant son départ.

## Ce que vous allez apprendre
- Lire le **Journal** d'un scénario
- La **Timeline**
- Corriger une publication programmée

## Pas à pas
1. Dans votre scénario, onglet **Journal** : chaque action y laisse une ligne.
2. Onglet **Timeline** : ajoutez une publication à T+15 min si besoin, puis cliquez-la.
3. Dans **Publication #N**, modifiez le texte, puis **Enregistrer**.

## Bon à savoir
- Une publication déjà partie est verrouillée : le bouton devient **Fermer**.
