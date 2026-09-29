# 📦 Context-pack — leac

> ⚙️ Généré (`generer_context_packs.py`). **À charger pour travailler sur « leac ».**
> Notes triées par tier (1 = prioritaire). Les fichiers `source:` sont la vérité à ouvrir.
> Généré le 2026-09-24 · 22 notes.

## Notes (par tier)

| Tier | ID | Titre | Type |
|---|---|---|---|
| 1 | [ARCH-014](../architecture/ARCH-014.md) | LEAC v3 — journal d'opérations et horloge de Lamport remplacent le PC maître, la clé USB et la réplication MariaDB | architecture |
| 1 | [DECISION-024](../decisions/DECISION-024.md) | LEAC — une saisie annulée ne remonte pas ; le compactage du journal est une question de justesse, pas de volume | decision |
| 1 | [DECISION-025](../decisions/DECISION-025.md) | LEAC — on pose une MENTION et on enregistre le MOT, jamais le chiffre | decision |
| 1 | [DECISION-026](../decisions/DECISION-026.md) | LEAC — le LABEL qualifie l'exercice, et une exigence obligatoire manquante invalide le contrôle | decision |
| 1 | [DECISION-027](../decisions/DECISION-027.md) | LEAC — Keycloak dit QUI VOUS ÊTES, LEAC dit CE QUE VOUS AVEZ LE DROIT D'Y FAIRE | decision |
| 1 | [DECISION-028](../decisions/DECISION-028.md) | LEAC — l'AUTEUR fait partie de la cible d'une note ; un transverse noté par plusieurs n'est pas une collision | decision |
| 1 | [DECISION-029](../decisions/DECISION-029.md) | Se déconnecter d'une app ferme la ZONE, pas la session de l'organisateur | decision |
| 1 | [DECISION-031](../decisions/DECISION-031.md) | LEAC — le bouclier Pléiade INSCRIT un administrateur, il ne remplace pas le registre | decision |
| 1 | [DECISION-032](../decisions/DECISION-032.md) | LEAC — le carnet de terrain entre avant la grille, et ne quitte jamais l'appareil | decision |
| 1 | [DECISION-036](../decisions/DECISION-036.md) | LEAC — quatre PROFILS permanents (utilisateur, superviseur, officier de marque, administrateur) | decision |
| 1 | [LESSON-035](../lessons/LESSON-035.md) | Un build applicatif qui passe ne prouve RIEN pour un déploiement conteneurisé — reproduire l'image en local | lesson |
| 1 | [LESSON-037](../lessons/LESSON-037.md) | Un indicateur doit mesurer EXACTEMENT ce qu'il prétend rapporter — deux fois le même jour | lesson |
| 1 | [LESSON-038](../lessons/LESSON-038.md) | Une image à volume de données ne fixe pas USER — le dossier monté appartient à root | lesson |
| 1 | [LESSON-039](../lessons/LESSON-039.md) | Derrière un proxy, une adresse absolue se construit sur les en-têtes, jamais sur req.url | lesson |
| 1 | [LESSON-040](../lessons/LESSON-040.md) | Un contrôle qui arrive APRÈS coup ne protège rien — il détruit ce qu'il refuse | lesson |
| 1 | [LESSON-041](../lessons/LESSON-041.md) | Une donnée qui n'existe que sur l'appareil doit demander la persistance — et c'est l'installation qui l'obtient | lesson |
| 1 | [LESSON-042](../lessons/LESSON-042.md) | Le portail d'une zone est PUBLIC — cocher un groupe donne l'accès, décocher ne cache pas la carte | lesson |
| 2 | [DECISION-021](../decisions/DECISION-021.md) | LEAC — on écrit un CHAMP par cible, jamais un objet entier ; c'est la granularité qui achète l'absence de conflit | decision |
| 2 | [DECISION-022](../decisions/DECISION-022.md) | LEAC — le « drapeau » devient un choix explicite et un filtre réel, il ne dépend plus d'un ordre de clic | decision |
| 2 | [DECISION-023](../decisions/DECISION-023.md) | LEAC — figer un cycle est un état métier, jamais un verrou d'écriture sur le journal | decision |
| 2 | [LESSON-034](../lessons/LESSON-034.md) | « Pas de note » n'est pas « zéro » — la confusion est invisible à l'œil et fait déclarer un PC inapte | lesson |
| 2 | [LESSON-036](../lessons/LESSON-036.md) | Retirer un rôle du catalogue Pléiade le SUPPRIME de Keycloak — le déclaratif efface, il n'ignore pas | lesson |

## 📄 Fichiers autoritaires à ouvrir (sources)

- [`MEMOIRE.md`](../../LEAC/MEMOIRE.md)
- [`MEMOIRE.md`](../../PLEIADE/MEMOIRE.md)
- [`JOURNAL.md`](../../LEAC/JOURNAL.md)
