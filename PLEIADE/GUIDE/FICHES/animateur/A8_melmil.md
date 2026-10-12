---
id: A8
parcours: animateur
ordre: 8
app: melmil
titre: "Relier un scénario à la planche MELMIL"
consigne: "Depuis un incident de la planche, créez un scénario qui lui est rattaché. (Seulement si MELMIL est déployé.)"
validation: auto
signal: "POST /api/bff/scenarios avec incidentId (console)"
niveau: premiers-pas
---

# Relier un scénario à la planche MELMIL

> Depuis un incident de la planche, créez un scénario qui lui est rattaché. (Seulement si MELMIL est déployé.)

## Ce que vous allez apprendre
- Lire la planche (EVENT, storylines, incidents)
- Créer un scénario pour un incident
- Suivre l'état des scénarios d'un incident

## Pas à pas
1. Ouvrez un incident sur la planche.
2. Bloc des scénarios : **+ Créer un scénario pour cet incident ↗** ouvre la Console avec l'incident déjà choisi.
3. Créez le scénario ; de retour sur l'incident, il apparaît avec son état (Brouillon, Lancé, Pause, Terminé) et **Ouvrir ↗**.

## Bon à savoir
- Le lien se fait par l'incident (la **Cible du scénario**), pas publication par publication.
