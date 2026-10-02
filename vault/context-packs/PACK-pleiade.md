# 📦 Context-pack — pleiade

> ⚙️ Généré (`generer_context_packs.py`). **À charger pour travailler sur « pleiade ».**
> Notes triées par tier (1 = prioritaire). Les fichiers `source:` sont la vérité à ouvrir.
> Généré le 2026-10-02 · 33 notes.

## Notes (par tier)

| Tier | ID | Titre | Type |
|---|---|---|---|
| 1 | [ARCH-012](../architecture/ARCH-012.md) | PLEIADE — orchestrateur de zones d'exercice (instances, Keycloak, Traefik) | architecture |
| 1 | [ARCH-013](../architecture/ARCH-013.md) | Une zone PLEIADE — 11 dépôts, 1 app = 1 dépôt, et 4 mécanismes qui les font parler | architecture |
| 1 | [ARCH-014](../architecture/ARCH-014.md) | LEAC v3 — journal d'opérations et horloge de Lamport remplacent le PC maître, la clé USB et la réplication MariaDB | architecture |
| 1 | [DECISION-014](../decisions/DECISION-014.md) | PLEIADE = le système global · MASTORION = seulement le réseau social (qui sera renommé) | decision |
| 1 | [DECISION-015](../decisions/DECISION-015.md) | L'EHO devient un dépôt autonome — STARTEX et comparaison portés, cellules écartées | decision |
| 1 | [DECISION-017](../decisions/DECISION-017.md) | Modèle de branches — on travaille sur une provisoire, on intègre dans main, on déploie par prod | decision |
| 1 | [DECISION-019](../decisions/DECISION-019.md) | Une seule copie de travail des dépôts PLEIADE, sur C: — le doublon D: supprimé | decision |
| 1 | [DECISION-024](../decisions/DECISION-024.md) | LEAC — une saisie annulée ne remonte pas ; le compactage du journal est une question de justesse, pas de volume | decision |
| 1 | [DECISION-027](../decisions/DECISION-027.md) | LEAC — Keycloak dit QUI VOUS ÊTES, LEAC dit CE QUE VOUS AVEZ LE DROIT D'Y FAIRE | decision |
| 1 | [DECISION-029](../decisions/DECISION-029.md) | Se déconnecter d'une app ferme la ZONE, pas la session de l'organisateur | decision |
| 1 | [DECISION-030](../decisions/DECISION-030.md) | Modèles d'EHO — ce qui doit exister sur TOUTE zone entre dans l'image, pas dans le volume | decision |
| 1 | [DECISION-031](../decisions/DECISION-031.md) | LEAC — le bouclier Pléiade INSCRIT un administrateur, il ne remplace pas le registre | decision |
| 1 | [DECISION-032](../decisions/DECISION-032.md) | LEAC — le carnet de terrain entre avant la grille, et ne quitte jamais l'appareil | decision |
| 1 | [DECISION-033](../decisions/DECISION-033.md) | app-melmil — la planche des injects suit les trois niveaux de JEMM, et rien d'autre | decision |
| 1 | [DECISION-035](../decisions/DECISION-035.md) | MELMIL est un document d'animation — le rôle du bouclier conditionne l'accès, pas la discrétion de la carte | decision |
| 1 | [LESSON-032](../lessons/LESSON-032.md) | Un échec de lecture ne doit jamais être présenté comme un résultat valide | lesson |
| 1 | [LESSON-035](../lessons/LESSON-035.md) | Un build applicatif qui passe ne prouve RIEN pour un déploiement conteneurisé — reproduire l'image en local | lesson |
| 1 | [LESSON-037](../lessons/LESSON-037.md) | Un indicateur doit mesurer EXACTEMENT ce qu'il prétend rapporter — deux fois le même jour | lesson |
| 1 | [LESSON-038](../lessons/LESSON-038.md) | Une image à volume de données ne fixe pas USER — le dossier monté appartient à root | lesson |
| 1 | [LESSON-039](../lessons/LESSON-039.md) | Derrière un proxy, une adresse absolue se construit sur les en-têtes, jamais sur req.url | lesson |
| 1 | [LESSON-040](../lessons/LESSON-040.md) | Un contrôle qui arrive APRÈS coup ne protège rien — il détruit ce qu'il refuse | lesson |
| 1 | [LESSON-041](../lessons/LESSON-041.md) | Une donnée qui n'existe que sur l'appareil doit demander la persistance — et c'est l'installation qui l'obtient | lesson |
| 1 | [LESSON-042](../lessons/LESSON-042.md) | Le portail d'une zone est PUBLIC — cocher un groupe donne l'accès, décocher ne cache pas la carte | lesson |
| 2 | [DECISION-016](../decisions/DECISION-016.md) | Le rangement du joueur (rubriques + ordre) est une préférence d'affichage, stockée à part | decision |
| 2 | [DECISION-018](../decisions/DECISION-018.md) | Le curseur d'alignement est ouvert sur les STARTEX — il y mesure une ATTITUDE, pas une identité | decision |
| 2 | [DECISION-020](../decisions/DECISION-020.md) | L'onglet « Choix d'avatar » supprimé — un écran qui liste les avatars n'a de sens que côté animation | decision |
| 2 | [DECISION-021](../decisions/DECISION-021.md) | LEAC — on écrit un CHAMP par cible, jamais un objet entier ; c'est la granularité qui achète l'absence de conflit | decision |
| 2 | [DECISION-034](../decisions/DECISION-034.md) | eho — UNE fiche d'avatar, UN verrou : la planche relationnelle ouvre la même fiche que l'onglet | decision |
| 2 | [LESSON-030](../lessons/LESSON-030.md) | Ne jamais déduire un champ d'API par supposition avant une suppression de masse | lesson |
| 2 | [LESSON-031](../lessons/LESSON-031.md) | exFAT (D:) n'exécute aucun binaire natif — clone d'exécution sur NTFS obligatoire | lesson |
| 2 | [LESSON-033](../lessons/LESSON-033.md) | Ne jamais écrire un chemin Windows en littéral dans un script de substitution | lesson |
| 2 | [LESSON-036](../lessons/LESSON-036.md) | Retirer un rôle du catalogue Pléiade le SUPPRIME de Keycloak — le déclaratif efface, il n'ignore pas | lesson |
| 2 | [TOOL-017](../tools/TOOL-017.md) | lib/bio.ts — rendre lisibles les bios de la bibliothèque sans les modifier | tool |

## 📄 Fichiers autoritaires à ouvrir (sources)

- [`MEMOIRE.md`](../../PLEIADE/MEMOIRE.md)
- [`MEMOIRE.md`](../../LEAC/MEMOIRE.md)
- [`JOURNAL.md`](../../PLEIADE/JOURNAL.md)
- [`JOURNAL.md`](../../LEAC/JOURNAL.md)
