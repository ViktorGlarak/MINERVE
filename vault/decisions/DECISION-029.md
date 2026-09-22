---
id: DECISION-029
aliases: ["DECISION-029"]
type: decision
title: Se déconnecter d'une app ferme la ZONE, pas la session de l'organisateur
tags: [pleiade, keycloak, authentification, deconnexion, eho, zones]
source: ../../PLEIADE/MEMOIRE.md
linkedTo: [DECISION-030, LESSON-037, LESSON-039]
relevantFor: [pleiade, mastorion, leac]
tier: 1
created: 2026-09-21
updated: 2026-09-21
---

# DECISION-029 — La chaîne de déconnexion s'arrête au royaume de la zone

## Contexte / problème
Sur un poste partagé, « Se déconnecter » dans eho **ne déconnectait rien** :
l'app fermait sa session NextAuth, Keycloak gardait la sienne, et « Se
connecter » rouvrait le compte précédent en silence. En réparant la chaîne
(l'app ferme aussi la session Keycloak), un second effet est apparu : un
organisateur entré par **cecpc Connect** se faisait déconnecter **jusqu'au
royaume `cecpc`**, donc aussi du tableau de bord Pléiade, et devait retaper son
mot de passe à chaque cycle.

## Décision
- L'app ferme **sa** session **et** celle du **royaume de la zone**
  (`end_session` avec `id_token_hint`, retour sur `/login`).
- Elle **ne propage plus** la déconnexion au royaume `cecpc` : le fournisseur
  d'identité `cecpc` de chaque zone est posé **sans `logoutUrl`**, et
  l'orchestrateur le réconcilie **à chaque démarrage** (avec les adresses de
  retour du client broker).
- Conséquence assumée : le bouton « cecpc » rouvre l'organisateur **en silence**
  tant que sa session Pléiade est ouverte.
- **Un seul geste de déconnexion** : « Changer de compte » et « Se connecter
  avec un autre compte » sont retirés. Le poste partagé se règle par « Se
  déconnecter », pas par un second bouton.

## Pourquoi (alternatives écartées)
- **Déconnexion globale** (*single logout*) : plus sûre sur un poste partagé,
  mais une saisie du mot de passe organisateur par cycle, et la perte de la
  session Pléiade au passage. Écartée par l'utilisateur : « moins risqué et
  plus propre » de ne fermer que la zone.
- **`prompt=login` par sécurité** sur la relance : ce paramètre **traverse le
  brokering** et faisait ré-authentifier le même compte côté `cecpc`. Retiré —
  un paramètre « au cas où » n'est jamais gratuit.

## Conséquences / à respecter
- Un client Keycloak doit déclarer **l'aller ET le retour**
  (`…/broker/cecpc/endpoint` **et** `…/logout_response`) : la comparaison est
  exacte, sans joker. Une seule source les connaît (`retoursCecpcConnect`).
- Le cas « onglet fermé sans se déconnecter » n'a plus de rattrapage côté app :
  la session de zone orpheline sera rouverte par SSO. Accepté en connaissance
  de cause.
- Les apps de Xavier (press, admin, cockpit, messagerie) reçoivent la même
  mécanique **en patchs** — pas de droit de push : `PLEIADE/PATCHS/2026-09-21_deconnexion/`.

## 🔗 Source de vérité
Détail complet : voir `source:` ci-dessus. **Cette note ne recopie pas — elle pointe.**
