# REF-08 — Transition post-quantique de SSHv2 (Fiche technique ANSSI)

- **Fichier** : `transition_post_quantique_ssh_v2.pdf` · **Éditeur / référence** : ANSSI, **ANSSI-FT-116** · **Date / version** : v1.0 du 02/02/2026 (version initiale) · **Pages** : 16 · **Marquage** : public (Licence Ouverte v2.0 Etalab, cyber.gouv.fr)
- **Public visé** : développeur, administrateur, RSSI, DSI, utilisateur
- **Ingéré** : 2026-10-01

## En une phrase

SSHv2 est menacé par le quantique dans le **handshake du Transport Layer** (échange DH + signature du serveur) et dans l'**authentification utilisateur par clé** ; la PSK n'existe pas en SSH, donc la seule voie est l'**hybridation**, déjà disponible pour l'échange de clés (**OpenSSH 9.9**, hybride ECDH + ML-KEM **par défaut depuis OpenSSH 10.0**), tandis que l'authentification hybride n'est pas standardisée.

## Ce que dit le document (synthèse structurée, fidèle)

### 1. Introduction (p. 3)
- SSH v2 défini par les RFC 4250-4254 [7-11]. Complète l'avis ANSSI sur la migration post-quantique [1, 2].
- Même cadre que les autres fiches : remplacement des signatures classiques et des DH par signatures PQ et **KEM** PQ ; **hybridation recommandée** pendant la transition ; messages plus gros ; symétrique non menacé mais **augmenter tailles de clés symétriques et de hachés**.

### 2. Présentation de SSHv2 (p. 4-7)
- Usages : administration à distance, transfert sécurisé, redirection de flux. Assure confidentialité, intégrité, authentification client et serveur. Au-dessus de **TCP**.
- Trois protocoles : **Transport Layer** (handshake + canal chiffré symétrique), **User Authentication**, **Connection**.
- **Impactés** : la partie **handshake** du Transport Layer (DH + signature serveur) et **User Authentication** (si authentification par signature). **Non impactés** : la protection symétrique du Transport Layer et le protocole Connection.
- Handshake (fig. 2) : `Version` → `SSH_MSG_KEXINIT` (listes : groupes DH + hachage ; algorithmes de signature serveur — le client liste ceux qu'il supporte, le serveur ceux pour lesquels il **possède une clé** ; algorithmes symétriques client→serveur et serveur→client ; choix **par ordre de préférence du client**) → `SSH_MSG_KEXDH_INIT` (clé publique DH client) → `SSH_MSG_KEXDH_REPLY` (clé publique DH serveur, **certificat ou clé publique du serveur**, signature sur l'empreinte des messages, clés DH et secret DH) → `SSH_MSG_NEWKEYS`.
- Le handshake peut être relancé en cours de session pour **renouveler les clés**.
- User Authentication : par signature, mot de passe ou GSS-API ; **seule l'authentification par signature est vulnérable au quantique**. Le client envoie sa clé publique (ou le certificat de son hôte) + une signature (identifiant de session, nom d'utilisateur…).
- Notes : la gestion des clés publiques serveur côté client et des clés clientes autorisées côté serveur **n'est pas traitée**.

### 3. Transition post-quantique (p. 8-10)
- **La confidentialité est plus urgente que l'authentification** (« store-now decrypt-later »).
- **3.1 PSK** : admise en principe par l'avis ANSSI, mais **pas nativement supportée par SSHv2** et **aucun travail** ne permet d'utiliser une PSK dans le protocole.
- **3.2.1 Hybridation de l'échange de clés** : DH classique + KEM PQ (ex. ML-KEM), puis combinaison ; **Attention** : la combinaison doit assurer une sécurité classique et PQ. `KEXINIT` liste des noms de mécanismes hybrides ; `KEXDH_INIT` = clé publique DH + clé publique KEM (concaténables) ; `KEXDH_REPLY` = clé publique DH + chiffré d'encapsulation (concaténables).
  - Documents : draft *PQ/T Hybrid Key Exchange in SSH* (**draft-ietf-sshm-mlkem-hybrid-kex-02**, avril 2025) [6] — ECDH + ML-KEM ; draft **`sntrup761x25519-sha512`** (*Hybrid Streamlined NTRU Prime sntrup761 and X25519 with SHA-512*, **draft-ietf-sshm-ntruprime-ssh-03**, mai 2025) [5]. **Pas de standard officiel** à ce jour.
  - Implémentations : **OpenSSH 9.9** implémente deux échanges hybrides : ECDH + **NTRU Prime** et ECDH + **ML-KEM** ; **le second est utilisé par défaut depuis OpenSSH 10.0** ; conformes à [5, 6] ; OpenSSH facilite l'ajout d'autres hybrides.
  - Un travail académique établit des preuves de sécurité de SSHv2 avec échanges hybrides [3] (Benčina et al., ePrint 2025).
- **3.2.2 Hybridation de l'authentification** : certificats et signatures hybrides (côté serveur dans `KEXINIT`/`KEXDH_REPLY`, côté client dans User Authentication) ; concerne aussi les chaînes de certification ; **aucun standard** à ce jour.
- Information : messages plus gros ; SSH sur **TCP** gère segmentation et réassemblage.

### 4. Conclusion (p. 11)
Hybridation recommandée pour échange de clés et authentification ; **PSK impossible en SSHv2** ; hybride ECDH + ML-KEM par défaut depuis OpenSSH 10.0 ; authentification hybride « nécessite plus de travaux » ; suivre l'évolution.

## Toutes les règles et recommandations

> **Pas de règles numérotées** dans la fiche. Numérotation **SSH-n ajoutée à l'ingestion**.

| N° (ajouté) | Prescription (texte du document) | Page |
|---|---|---|
| SSH-1 | **Hybridation** recommandée pendant la transition (échange de clés et authentification par signature). | 3, 8, 11 |
| SSH-2 | Augmenter tailles de **clés symétriques** et de **sorties de hachage** (avis ANSSI). | 3 |
| SSH-3 | Traiter **d'abord la confidentialité** (échange de clés) — « store-now decrypt-later ». | 8 |
| SSH-4 | **PSK non disponible** en SSHv2 → la voie PSK n'est **pas possible** ; seule l'hybridation s'applique. | 8, 11 |
| SSH-5 | La **combinaison** des secrets classique et PQ doit assurer une sécurité classique ET post-quantique. | 9 |
| SSH-6 | Authentification hybride (serveur et client) : signatures, certificats, chaînes — **pas de standard**, suivre les travaux. | 9-11 |
| SSH-7 | Seule l'authentification **par signature** est vulnérable au quantique (mot de passe, GSS-API non concernés par la menace quantique au sens de la fiche). | 6 |

## Tableau « autorisé / recommandé / à proscrire »

| Élément | Statut selon la fiche | Échéance / remarque |
|---|---|---|
| Échange de clés **hybride ECDH + ML-KEM** | **Recommandé** ; défaut d'**OpenSSH ≥ 10.0** | Dès maintenant (priorité confidentialité) |
| Échange hybride **ECDH (X25519) + NTRU Prime** (`sntrup761x25519-sha512`) | Hybride implémenté (OpenSSH 9.9), draft [5] | Acceptable au sens « hybride » ; la fiche ne le classe pas (REF-06 ne dimensionne que les réseaux euclidiens LWE/SIS — NTRU Prime n'y figure pas) |
| Échange DH/ECDH **classique seul** | Vulnérable (store-now decrypt-later) | À remplacer par un hybride |
| **PSK** | **Non supportée** par SSHv2 | — |
| Clés hôte / utilisateur classiques (signature) | Vulnérables au quantique, pas de remplacement standard | Suivre les travaux ; moins urgent |
| Signatures/certificats hybrides | Non standardisés | — |

> Rappel REF-06 (§ 2.2.3, Information) : **« Le protocole SSH requiert que les signatures satisfassent la sécurité forte en contrefaçon ; l'utilisation d'ECDSA n'est pas compatible avec ce protocole »** — à prendre en compte pour le choix des clés hôte/utilisateur.
> Le nom d'algorithme OpenSSH de l'hybride ML-KEM (`mlkem768x25519-sha256`) **n'est pas écrit dans la fiche** (hors document, à vérifier dans `ssh -Q kex`).

## Chiffres et seuils à retenir

- **OpenSSH 9.9** : 2 hybrides (NTRU Prime + ECDH ; ML-KEM + ECDH).
- **OpenSSH 10.0** : hybride ML-KEM **par défaut**.
- `sntrup761x25519-sha512` : draft-ietf-sshm-ntruprime-ssh-**03** (05/2025).
- ML-KEM hybride : draft-ietf-sshm-mlkem-hybrid-kex-**02** (04/2025).
- RFC SSH : **4250, 4251, 4252, 4253, 4254** (janvier 2006).

## Application à PLÉIADE

> Analyse MINERVE/CYBERSECU (hors document). Éléments produits marqués « à vérifier ».

| Contrôle | Applicabilité | Détail |
|---|---|---|
| **À vérifier : version d'OpenSSH du serveur PLÉIADE** (`ssh -V`, `sshd -V`) — **≥ 10.0** (hybride ML-KEM par défaut) ou au moins **≥ 9.9** | **Applicable — transition PQ, priorité 1** | L'administration du serveur passe par SSH : un enregistrement des sessions (mots de passe saisis, secrets copiés, `.env`) serait déchiffrable a posteriori. |
| **À vérifier : `KexAlgorithms` de `sshd_config`** — hybride en tête, ne pas le **retirer** par un durcissement copié d'un vieux guide | **Applicable** | Vérifier aussi le client d'admin (poste Windows : version d'OpenSSH Windows, souvent plus ancienne → la négociation retomberait en classique). |
| **À vérifier : type des clés hôte et utilisateur** (`HostKey`, clés des administrateurs) | Applicable (renvoi REF-06) | RSA ≥ 3072 recommandé (≥ 2048 seulement jusqu'à fin 2030) ; **ECDSA déconseillé en SSH selon REF-06** (sécurité forte en contrefaçon requise). Ed25519 n'est **pas cité** par l'ANSSI dans ces documents (ni conforme ni non conforme) → **à trancher** avec le guide de sélection ANSSI. |
| **À vérifier : authentification par clé uniquement** (`PasswordAuthentication no`) | Applicable (hors menace quantique) | La fiche note que mot de passe ≠ menace quantique, mais REF-06 RègleSecretFaibleEntropie s'applique à tout secret faible. |
| **À vérifier : liste des clés autorisées** (`authorized_keys`) et vérification des empreintes d'hôte côté client | Applicable — hors fiche | La fiche exclut explicitement ces sujets ; ils restent le principal risque concret. |
| Authentification hybride (clés hôte PQ) | Hors champ actuel | Aucun standard ; à suivre. |
| Accès Git vers GitHub en SSH depuis le serveur / postes | Partiellement | Dépend de la version d'OpenSSH client et du support côté GitHub (à vérifier). |

**Échéance** : aucune date dans la fiche ; REF-06 → viser le PQ pour tout usage au-delà du **1er janvier 2030** ou en cas de risque rétroactif → **mise à niveau d'OpenSSH ≥ 10.0 dès que possible** (coût faible).

## Limites / points d'attention

- Fiche d'état des lieux non normative ; aucun paramètre (niveau ML-KEM) n'est imposé — REF-06 : préférer ML-KEM-768 à ML-KEM-512.
- Gestion des clés publiques (known_hosts, authorized_keys) explicitement **hors champ**.
- NTRU Prime n'est pas dimensionné par REF-06 (qui ne traite que (M)LWE/(M)SIS) : préférer l'hybride ML-KEM, conforme à la référence FIPS 203.
- Les numéros de version OpenSSH sont ceux de la fiche (02/2026) : la distribution Linux du serveur peut livrer une version plus ancienne (rétroportage) → vérifier sur la machine.
