# Avis n°31 — admin : un scénario peut cibler une storyline (ensemble d'incidents)

> **Date** : 2026-10-02 · **Demandeur** : l'utilisateur · **Écrans** : `app-admin` (création/fiche d'un scénario), `app-melmil` (planche).
> **Statut** : 🟢 appliqué en local (voir `PLEIADE\JOURNAL.md`).

## Besoin
Un animateur a créé un scénario « 08.01 » pour une **storyline** entière, pas un incident. Le modèle ne liait un scénario qu'à **un** incident → le scénario ne s'affichait pas correctement sur la planche. Il faut permettre un scénario **au niveau storyline**, en l'obligeant à **désigner l'ensemble des incidents** concernés, pour que le pictogramme apparaisse sur chacun d'eux.

## Décisions de l'utilisateur
- Cible : **un incident OU une storyline** (au choix à la création).
- Storyline : **tous les incidents cochés par défaut**, décochables (≥ 1 requis).
- Périmètre : **borné à une seule storyline**.

## Recommandations (ergonomie)
- **R1 — Un choix d'emblée** : un **segment « Cet incident / Toute une storyline »** en tête du formulaire. Pas de second champ obscur.
- **R2 — Mode storyline** : on choisit la storyline, puis ses incidents en **cases à cocher** (motif déjà connu : ETIM, fichiers fournis), **tous cochés** par défaut, avec compte « 4 incidents » et « Tout cocher / décocher ». Au moins un requis (le forçage demandé).
- **R3 — Rien de neuf visuellement sur la planche** : le pictogramme « ▶ » reste le même ; il s'affiche désormais sur **tous** les incidents du scénario, pas un seul.
- **R4 — Lisibilité de la fiche/liste** : un scénario de storyline s'affiche « **Storyline 08.01 — 4 incidents** » (et se range sous l'en-tête 08.01), un scénario d'incident garde « Incident 08.01.I04 ».
- **R5 — Ne rien casser** : les scénarios mono-incident existants restent identiques ; leur ensemble = leur unique incident.
