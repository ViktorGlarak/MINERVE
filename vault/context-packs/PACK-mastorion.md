# 📦 Context-pack — mastorion

> ⚙️ Généré (`generer_context_packs.py`). **À charger pour travailler sur « mastorion ».**
> Notes triées par tier (1 = prioritaire). Les fichiers `source:` sont la vérité à ouvrir.
> Généré le 2026-10-02 · 25 notes.

## Notes (par tier)

| Tier | ID | Titre | Type |
|---|---|---|---|
| 1 | [ARCH-012](../architecture/ARCH-012.md) | PLEIADE — orchestrateur de zones d'exercice (instances, Keycloak, Traefik) | architecture |
| 1 | [ARCH-013](../architecture/ARCH-013.md) | Une zone PLEIADE — 11 dépôts, 1 app = 1 dépôt, et 4 mécanismes qui les font parler | architecture |
| 1 | [DECISION-014](../decisions/DECISION-014.md) | PLEIADE = le système global · MASTORION = seulement le réseau social (qui sera renommé) | decision |
| 1 | [DECISION-017](../decisions/DECISION-017.md) | Modèle de branches — on travaille sur une provisoire, on intègre dans main, on déploie par prod | decision |
| 1 | [DECISION-019](../decisions/DECISION-019.md) | Une seule copie de travail des dépôts PLEIADE, sur C: — le doublon D: supprimé | decision |
| 1 | [DECISION-029](../decisions/DECISION-029.md) | Se déconnecter d'une app ferme la ZONE, pas la session de l'organisateur | decision |
| 1 | [DECISION-030](../decisions/DECISION-030.md) | Modèles d'EHO — ce qui doit exister sur TOUTE zone entre dans l'image, pas dans le volume | decision |
| 1 | [LESSON-032](../lessons/LESSON-032.md) | Un échec de lecture ne doit jamais être présenté comme un résultat valide | lesson |
| 1 | [LESSON-035](../lessons/LESSON-035.md) | Un build applicatif qui passe ne prouve RIEN pour un déploiement conteneurisé — reproduire l'image en local | lesson |
| 1 | [LESSON-037](../lessons/LESSON-037.md) | Un indicateur doit mesurer EXACTEMENT ce qu'il prétend rapporter — deux fois le même jour | lesson |
| 1 | [LESSON-038](../lessons/LESSON-038.md) | Une image à volume de données ne fixe pas USER — le dossier monté appartient à root | lesson |
| 1 | [LESSON-039](../lessons/LESSON-039.md) | Derrière un proxy, une adresse absolue se construit sur les en-têtes, jamais sur req.url | lesson |
| 1 | [LESSON-040](../lessons/LESSON-040.md) | Un contrôle qui arrive APRÈS coup ne protège rien — il détruit ce qu'il refuse | lesson |
| 1 | [LESSON-041](../lessons/LESSON-041.md) | Une donnée qui n'existe que sur l'appareil doit demander la persistance — et c'est l'installation qui l'obtient | lesson |
| 1 | [LESSON-042](../lessons/LESSON-042.md) | Le portail d'une zone est PUBLIC — cocher un groupe donne l'accès, décocher ne cache pas la carte | lesson |
| 2 | [ARCH-011](../architecture/ARCH-011.md) | EHO v2 (MASTORION) — modèles d'EHO, double vue anim/joueurs, tables additives | architecture |
| 2 | [DECISION-013](../decisions/DECISION-013.md) | L'app EHO est propriétaire des personas — l'Admin MASTORION ne gère que les comptes humains | decision |
| 2 | [DECISION-018](../decisions/DECISION-018.md) | Le curseur d'alignement est ouvert sur les STARTEX — il y mesure une ATTITUDE, pas une identité | decision |
| 2 | [DECISION-034](../decisions/DECISION-034.md) | eho — UNE fiche d'avatar, UN verrou : la planche relationnelle ouvre la même fiche que l'onglet | decision |
| 2 | [LESSON-027](../lessons/LESSON-027.md) | Import MASTORION — deux fiches partageant email ou masto_id fusionnent EN SILENCE | lesson |
| 2 | [LESSON-028](../lessons/LESSON-028.md) | La bio MASTORION est PUBLIQUE côté réseau social — le renseignement animateur va dans observations | lesson |
| 2 | [LESSON-029](../lessons/LESSON-029.md) | Clé dupliquée dans un literal dict Python — la dernière écrase les autres EN SILENCE | lesson |
| 2 | [LESSON-030](../lessons/LESSON-030.md) | Ne jamais déduire un champ d'API par supposition avant une suppression de masse | lesson |
| 2 | [LESSON-031](../lessons/LESSON-031.md) | exFAT (D:) n'exécute aucun binaire natif — clone d'exécution sur NTFS obligatoire | lesson |
| 2 | [LESSON-036](../lessons/LESSON-036.md) | Retirer un rôle du catalogue Pléiade le SUPPRIME de Keycloak — le déclaratif efface, il n'ignore pas | lesson |

## 📄 Fichiers autoritaires à ouvrir (sources)

- [`MEMOIRE.md`](../../PLEIADE/MEMOIRE.md)
- [`JOURNAL.md`](../../LEAC/JOURNAL.md)
- [`MEMOIRE.md`](../../LEAC/MEMOIRE.md)
- [`MEMOIRE.md`](../../MASTORION/MEMOIRE.md)
- [`JOURNAL.md`](../../MASTORION/JOURNAL.md)
- [`generer_bibliotheque.py`](../../MASTORION/OUTILS/generer_bibliotheque.py)
- [`JOURNAL.md`](../../PLEIADE/JOURNAL.md)
