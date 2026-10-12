---
id: A4
parcours: animateur
ordre: 4
app: admin
titre: "Programmer une publication dans la Console d'animation"
consigne: "Créez un scénario, programmez-y une publication dans 5 minutes, lancez-le, mettez-le en pause, reprenez-le."
validation: auto
signal: "POST /api/bff/scenarios/{id}/actions (start, pause, resume)"
niveau: premiers-pas
---

# Programmer une publication dans la Console d'animation

> Créez un scénario, programmez-y une publication dans 5 minutes, lancez-le, mettez-le en pause, reprenez-le.

## Ce que vous allez apprendre
- Créer un scénario
- Ajouter une publication programmée
- **Vérifier** et **Lancer**
- **Pause** et **Reprendre**

## Pas à pas
1. **+ Nouveau scénario** : **Cible du scénario** (« Bruit de fond » pour l'essai), **Cellule**, **Nom**, **Début**, puis **Créer**.
2. Onglet **Arbre** : **Ajouter une publication sur** le réseau social. Dans **Nouvelle publication**, choisissez l'**App cible**, le **Persona** (l'avatar : **Rechercher un persona…** → **L'utiliser**), le texte, puis **Quand** → **Délai** : 5 min. **Ajouter**.
3. **Vérifier**, puis **Lancer** (si le début est passé : **Maintenant**).
4. **Pause** (« Scénario en pause »), puis **Reprendre** (« Lecture reprise ») : tout le scénario est décalé de la durée de la pause.

## Bon à savoir
- **Lancer** reste grisé tant que le scénario n'a pas été vérifié.
- Les apps cibles possibles : réseau social, presse, messagerie.
- Dans la console, un avatar s'appelle un **Persona**.
