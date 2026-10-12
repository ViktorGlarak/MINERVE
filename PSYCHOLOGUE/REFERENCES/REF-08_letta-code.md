# REF-08 — Letta Code (agent de programmation en terminal, à mémoire persistante entre sessions)

- **Source** : README https://github.com/letta-ai/letta-code (lu le 2026-10-12, fourni par l'utilisateur).
- **Licence** : Apache 2.0. Harnais client (CLI, appli de bureau, navigateur) ; l'état de l'agent vit en local ou dans **Letta Cloud** (exécution depuis plusieurs machines). Modèles : clés d'API **cloud** (OpenAI, Anthropic, Z.ai) via `/connect` — aucun modèle local annoncé.

## Ce que fait le projet
- « *A stateful agent harness for building agents that are more like people than tools* » : un agent de programmation qui **se souvient d'une session à l'autre** et évolue sur de longs horizons « *by rewriting their own memory, skills, and prompts* ».
- **Memory blocks** : le prompt système s'**apprend** par réécriture contextuelle (même mécanisme que Letta, REF-07).
- **MemFS** : « *all context is tracked via git* » — la mémoire est un ensemble de **fichiers versionnés**, synchronisables vers un dépôt GitHub personnel ; chaque changement de mémoire est un commit lisible.
- **Skills** : capacités chargeables à la demande depuis des répertoires globaux, de projet ou d'agent (mémoire **procédurale** modulaire).
- Différence avec Letta serveur : Letta Code est l'outil **client** de l'utilisateur ; Letta (REF-07) est l'infrastructure d'agents.

## Ce que dit le CODE SOURCE
> Rapport complet : `CODE-letta-code.md` (commit 271f119). Les mécanismes de mémoire de ce dépôt (MemFS v2 versionné par git, plafonds de taille par hook pre-commit, fichiers `readOnly` d'identité, réflexion `reflection-v2` à 5 priorités / 4 filtres, résumé récursif « compagnon », curseur et worktree) sont **traités dans REF-07** (section « Ce que dit le CODE SOURCE » et idées 4-9), parce qu'ils sont la version actuelle des idées MemGPT / Letta. Cette fiche ne garde que ce qui est propre à l'outil de programmation.

## Ce qui est pertinent pour la psychologie des avatars
- Peu : c'est un outil de programmation, pas un modèle de mémoire. Deux transpositions seulement :
  - **Mémoire versionnée (MemFS)** : l'évolution d'un avatar (son bloc « où j'en suis », ses corrections de fiche) rendue comme une **suite de versions datées** = ce que l'animation et le RETEX veulent voir (« comment Esteban a changé en six jours »).
  - **Skills = mémoire procédurale modulaire** : les savoir-faire d'un **rôle** (maire : point de situation / demande officielle / consigne / soutien ; relais : six registres ; commerçant : horaires, fermetures) chargés **seulement quand le rôle est actif**, plutôt que toujours présents dans l'invite — c'est déjà la logique de nos registres par rôle et de la voix de cohorte à déclencheur (avis n°10).

## Ce que nous avons déjà d'équivalent (app-ia 2026-10-12.2)
| Letta Code | Moteur |
|---|---|
| mémoire versionnée par git | journal des variations (1 ligne par jour et par variable après 48 h), archivé par le pont dans la base du moteur ; `archives.ts` ; corrections de fiches datées (`corrections\*.json`) |
| skills par rôle | registres par rôle (`VOIX`, registres du maire / du relais), déclencheurs sur le fil lu |
| réécriture de son propre prompt | ✗ (voir REF-07, idée 1) |

## À récupérer (idées précises)
1. **Rien d'indispensable.** Une seule idée, mineure et dépendante de REF-07 : si le bloc « où j'en suis » est adopté, **archiver chaque version nocturne** (date, texte, diff en une ligne) à côté du journal des variations, pour que le relevé périodique puisse afficher la **trajectoire en 7 lignes** d'un avatar. Coût : 0 appel, ~400 octets par avatar et par nuit en base, hors JSON de mémoire.
2. **Ne pas récupérer** : l'outil (modèles cloud uniquement ; usage programmation).

## Coût
- Outil : modèles cloud ⇒ exclu (CYBERSECU) ; sans objet pour un réseau d'avatars.
- Idée 1 : négligeable, en base du moteur.

## Verdict : **SANS INTÉRÊT POUR NOUS** (une note : archiver les versions du bloc « où j'en suis », si REF-07 est retenu)
Raison : aucune mécanique psychologique nouvelle par rapport à Letta (REF-07) ; ce qui concerne la mémoire y est déjà, ce qui est propre à Letta Code (git, skills, cloud) relève de l'outillage de programmation.
