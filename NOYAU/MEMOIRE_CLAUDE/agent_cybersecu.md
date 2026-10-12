---
name: agent-cybersecu
description: "Agent CYBERSECU (créé 2026-10-01) — référent cybersécurité de PLÉIADE ; à consulter dès qu'un sujet touche la sécurité, à mettre à jour à chaque décision ou correction"
metadata:
  node_type: memory
  type: project
  originSessionId: 699185de-99a6-4263-a321-d605be7e2b29
  modified: 2026-10-02T06:01:44.055Z
---

**CYBERSECU**, agent n°25, a été créé le 2026-10-01 à la demande de l'utilisateur. C'est le **référent cybersécurité de PLÉIADE**.
- **Dossier** : `D:\CECPC\PRODUCTION\IA\MINERVE\CYBERSECU\`, avec `MEMOIRE.md`, `JOURNAL.md` et `REFERENCES\REF-01` à `REF-11`.
- **Prompt** : `SYSTEME\PROMPTS\cybersecu.md`.
- **Sources ingérées** : 11 guides ANSSI publics (`D:\CECPC\PLEIADE\DOC\CYBER SECU\`) sur l'hygiène, la défense en profondeur, le zero trust, le poste multi-environnements, VMware, les mécanismes cryptographiques, le post-quantique (TLS, SSH, IPsec) et la sécurité web (2013 et 2021).
- **Contenu de la mémoire** : doctrine sourcée (§3), règles de sécurité déjà décidées (§4), **plan de durcissement** (§5 : 7 écarts élevés, 11 moyens), questions à vérifier sur le serveur (§7).
- **Deux écarts élevés confirmés dans le code** : le terminal WebSocket de l'orchestrateur n'a pas d'authentification, et app-social accepte des jetons locaux signés avec un secret par défaut.

**État au 2026-10-02 :** le récapitulatif a été transmis à Xavier. Le plan est ⏸️ **en attente** : l'utilisateur poursuit l'exercice. On reprendra plus tard, à partir de la réponse de Xavier. Ne rien corriger d'ici là sans demande explicite.

**Why:** l'utilisateur veut que cet agent contienne tout ce que l'assistant sait de la cybersécurité, et ses mises à jour futures, pour bien maîtriser la sécurité de PLÉIADE.

**How to apply:**
- Dès qu'un sujet touche l'authentification, les secrets, TLS, PKI, le VPN, les en-têtes, les droits, l'anonymat, les téléversements ou les dépendances : lire `CYBERSECU\MEMOIRE.md` avant d'agir.
- Après chaque décision, correction ou incident de sécurité : mettre à jour `MEMOIRE.md` (§4 ou §5) et `JOURNAL.md` dans la même session.
- Tout nouveau document de sécurité fourni s'ingère en fiche REF-NN.
- CYBERSECU conseille, il ne pousse pas : la mise en œuvre suit [[feedback-tester-en-local-avant-push]] et demande l'accord de l'utilisateur.
- Ne jamais recopier de secret, d'adresse IP ou de compte serveur dans cette mémoire. Voir aussi [[feedback-certificats-vpn-interdits]].
