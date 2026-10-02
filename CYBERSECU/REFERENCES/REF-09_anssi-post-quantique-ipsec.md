# REF-09 — Transition post-quantique d'IPsec (Fiche technique ANSSI)

- **Fichier** : `transition_post_quantique_ipsec.pdf` · **Éditeur / référence** : ANSSI, **ANSSI-FT-117** · **Date / version** : v1.0 du 02/02/2026 (version initiale) · **Pages** : 22 · **Marquage** : public (Licence Ouverte v2.0 Etalab, cyber.gouv.fr)
- **Public visé** : développeur, administrateur, RSSI, DSI, utilisateur
- **Ingéré** : 2026-10-01

## En une phrase

Dans IPsec, seul **IKEv2** est menacé (DH + signatures) ; l'ANSSI privilégie l'**hybridation** via **RFC 9370** (échanges de clés multiples dans `IKE_INTERMEDIATE`, avec ML-KEM, implémenté dans **strongSwan 6.0**) et tolère temporairement la **PSK** (RFC 8784, corrigée par **RFC 9867** en 2025) ; le point dur est la **fragmentation** (IKEv2 sur UDP, résolue par RFC 7383) ; l'authentification hybride n'est pas standardisée.

## Ce que dit le document (synthèse structurée, fidèle)

### 1. Introduction (p. 3)
- IPsec : RFC 4301 (architecture), 7296 (IKEv2), 4302 (AH), 4303 (ESP). Complète l'avis ANSSI [1, 2]. Même cadre : KEM PQ, hybridation recommandée, messages plus gros, augmenter tailles symétriques et de hachés.

### 2. Présentation d'IPsec (p. 4-8)
- IPsec : souvent utilisé pour un **VPN** entre initiateur et répondeur ; confidentialité et intégrité des paquets IP, authentification mutuelle.
- Trois protocoles : **IKEv2** (sur **UDP**, partie « handshake » : authentification mutuelle, négociation, secrets → associations de sécurité SA), **AH** (intégrité + anti-rejeu), **ESP** (confidentialité + intégrité + anti-rejeu). **Seul IKEv2 est impacté** ; AH/ESP sont symétriques (mais leurs clés dépendent d'IKEv2).
- **SA** : IKE SA (bidirectionnelle, protège les échanges IKEv2 après `IKE_SA_INIT`) ; Child SA (unidirectionnelles, par paires, protègent les paquets IP via AH ou ESP ; granularité réglable : une paire pour tout le tunnel ou une par connexion TCP…).
- `IKE_SA_INIT` : SAi1 (propositions : algorithmes symétriques, **groupes DH**, fonctions pseudo-aléatoires PRF), KEi (clé publique DH), Ni (nonce) ; réponse SAr1, KEr, Nr, [CertReq]. Clés IKE dérivées du secret DH + Ni/Nr.
- `IKE_AUTH` (chiffré) : IDi, [Cert], [CertReq], [IDr], **AUTH** (signature **ou** code d'authentification calculé avec la PRF et une **clé pré-partagée**), SAi2, TSi, TSr ; réponse IDr, [Cert], AUTH, SAr2, TSi, TSr. Deux modes d'authentification : **signature + certificat** ou **PSK symétrique**.
- Les clés des premières Child SA dérivent du **même secret DH et des mêmes nonces** que l'IKE SA ; RFC 6023 permet une initiation sans Child SA.
- `CREATE_CHILD_SA` : rafraîchit l'IKE SA ou crée/rafraîchit des Child SA ; nouvelle clé DH (KEi/KEr) **optionnelle pour les Child SA** ; clés dérivées du secret DH (s'il existe), des nonces et d'une clé de l'IKE SA.

### 3. Transition post-quantique (p. 9-13)
- Deux voies : PSK (§3.1) ou **hybridation (§3.2), privilégiée par l'ANSSI**. **Confidentialité plus urgente** que l'authentification (« store-now decrypt-later »).

#### 3.1 PSK
- Conditions : confidentialité et intégrité classiques et PQ de la PSK ; attention à sa **gestion/distribution** ; **mesure temporaire**, hybridation « à terme ».
- **Authentification PQ par PSK** : possible nativement (champ AUTH = code symétrique).
- **Confidentialité PQ par PSK** : pas par défaut. **RFC 8784 (2020)** mélange une PSK (distincte de celle d'authentification) à la dérivation des clés avec le DH. **Limitation** : la PSK n'entre que dans les clés des **futures Child SA** — **le trafic IKEv2 lui-même reste protégé uniquement par le DH**.
- **RFC 9867 (nov. 2025)** étend la PSK à la dérivation des clés protégeant les échanges IKEv2, via des échanges intermédiaires (RFC 9242) entre `IKE_SA_INIT` et `IKE_AUTH`, et permet de négocier d'autres PSK dans `CREATE_CHILD_SA`.
- **Attention** : compromission de PSK **rétroactive** ; PSK fixe + DH par session → PFS classique mais **pas post-quantique**.
- Implémentations : **strongSwan** (authentification PSK IKEv2 ; RFC 8784 **depuis la 5.7.0**).

#### 3.2.1 Hybridation des échanges de clés
- Échanges dans `IKE_SA_INIT` et `CREATE_CHILD_SA` ; classique (DH) + PQ (ex. ML-KEM) puis combinaison (**Attention** : sécurité classique ET PQ).
- SAi1/SAr1/SAi/SAr peuvent porter des noms de mécanismes hybrides, **mais KEi/KEr ne peuvent pas transporter l'hybride sans modifier le protocole** : clés publiques et chiffrés PQ trop gros, IKEv2 sur UDP **ne gère pas nativement la fragmentation**.
- **RFC 7383 (2014)** : fragmentation au niveau IKEv2 pour **tous les messages chiffrés**, **sauf `IKE_SA_INIT`** (motivée à l'origine par les chaînes de certificats).
- **RFC 9370 (2023)** : **échanges de clés multiples successifs** — `IKE_SA_INIT` négocie et échange les clés DH, puis des messages **`IKE_INTERMEDIATE`** (RFC 9242, chiffrés donc fragmentables via RFC 7383) portent les échanges supplémentaires (fig. 3 : N + 1 échanges). **Un seul `IKE_INTERMEDIATE` suffit pour un hybride** (clé publique KEM de l'initiateur → chiffré du répondeur). RFC 9370 définit la combinaison successive des secrets et, pour `CREATE_CHILD_SA`, des messages **`IKE_FOLLOWUP_KE`**. Généralisable à plusieurs mécanismes.
- Document : draft *Post-quantum Hybrid Key Exchange with ML-KEM in IKEv2* (**draft-ietf-ipsecme-ikev2-mlkem-03**, sept. 2025) [8].
- Implémentations : **strongSwan** gère RFC 7383 ; **strongSwan 6.0** implémente l'hybride RFC 9370 et intègre **ML-KEM**.

#### 3.2.2 Hybridation de l'authentification
- Certificats et signatures hybrides dans `AUTH`/`Cert` (`IKE_AUTH`) ; chaînes concernées ; **pas de standard**. Les tailles sont gérées par RFC 7383 (messages chiffrés) → l'hybridation de l'authentification requiert surtout l'implémentation de RFC 7383.

### 4. Conclusion (p. 14)
Hybridation recommandée ; PSK envisageable mais temporaire ; RFC 8784 protège le trafic IP mais pas IKEv2, corrigé par RFC 9867 ; RFC 9370 + RFC 9242 + RFC 7383 pour l'hybride ; strongSwan 6.0 ; authentification hybride non standardisée ; suivre les travaux.

### Annexe A — Fragmentation (p. 15-16)
- Chaque interface a une **MTU** ; **IPv6 : MTU minimale à implémenter = 1280 octets** ; en pratique souvent **1500 octets**.
- La fragmentation IP pose problème : **certains pare-feux rejettent les paquets IP fragmentés** (anti-déni de service).
- Trois solutions : messages ≤ MTU ; transport fiable (TCP) qui segmente ; fragmentation au niveau applicatif.
- Exemple : un protocole sur **UDP** à petits messages de handshake nécessitera des **modifications conséquentes** et une étude approfondie pour le PQ — la complexité de la transition dépend de la conception du protocole.

## Toutes les règles et recommandations

> **Pas de règles numérotées** dans la fiche. Numérotation **IPS-n ajoutée à l'ingestion**.

| N° (ajouté) | Prescription (texte du document) | Page |
|---|---|---|
| IPS-1 | **Hybridation** recommandée (échanges de clés + authentification par signature). | 3, 9, 14 |
| IPS-2 | Augmenter tailles de **clés symétriques** et de **hachés** (avis ANSSI). | 3 |
| IPS-3 | **Confidentialité d'abord** (store-now decrypt-later). | 9 |
| IPS-4 | PSK : confidentialité et intégrité classiques et PQ de la PSK, **gestion/distribution soignées**, **mesure temporaire**, hybridation à terme. | 9, 14 |
| IPS-5 | Attention : **RFC 8784** ne protège pas le trafic IKEv2 (seulement les Child SA futures) → limitation de sécurité ; **RFC 9867** la corrige. | 9-10 |
| IPS-6 | Attention : compromission de PSK **rétroactive** → PFS non assurée en PQ. | 10 |
| IPS-7 | La **combinaison** des secrets doit assurer une sécurité classique ET PQ. | 10 |
| IPS-8 | Hybride IKEv2 : passer par **RFC 9370** (`IKE_INTERMEDIATE` / `IKE_FOLLOWUP_KE`) avec **RFC 9242** et **RFC 7383** (fragmentation) — KEi/KEr ne suffisent pas. | 11-12 |
| IPS-9 | Authentification hybride : **non standardisée** ; nécessite surtout RFC 7383. | 12-13 |
| IPS-10 | Annexe : éviter la dépendance à la **fragmentation IP** (pare-feux rejetant les fragments ; MTU IPv6 min. 1280 octets). | 15-16 |

## Tableau « autorisé / recommandé / à proscrire »

| Élément | Statut selon la fiche | Échéance / remarque |
|---|---|---|
| IKEv2 + **hybride DH + ML-KEM via RFC 9370** (+ RFC 9242, RFC 7383) | **Recommandé** (solution privilégiée) | strongSwan ≥ 6.0 ; draft ikev2-mlkem-03 |
| Authentification IKEv2 par **PSK** | **Toléré, temporaire** (assure une authentification PQ) | Hybridation à terme |
| **RFC 8784** (PSK dans la dérivation) | Utilisable mais **limitation** : IKEv2 non protégé | strongSwan ≥ 5.7.0 |
| **RFC 9867** (PSK aussi pour IKEv2) | Corrige RFC 8784 | Publiée nov. 2025 |
| DH **classique seul** | Vulnérable (store-now decrypt-later) | À hybrider |
| Hybride dans KEi/KEr sans modification | **Impossible** (taille / fragmentation) | — |
| Signatures/certificats hybrides | Non standardisés | Suivre |
| Dépendre de la fragmentation IP | **À éviter** | — |

## Chiffres et seuils à retenir

- RFC : **7296** (IKEv2), **4301/4302/4303**, **6023** (sans Child SA), **7383** (fragmentation, 11/2014), **8784** (PSK PQ, 06/2020), **9242** (Intermediate, 05/2022), **9370** (échanges multiples, 05/2023), **9867** (PSK dans IKE_INTERMEDIATE/CREATE_CHILD_SA, 11/2025).
- strongSwan **5.7.0** (RFC 8784) ; strongSwan **6.0** (RFC 9370 + ML-KEM).
- MTU IPv6 minimale **1280 octets** ; courante **1500 octets**.
- Hybride = **1 seul** échange `IKE_INTERMEDIATE` supplémentaire.

## Application à PLÉIADE

> Analyse MINERVE/CYBERSECU (hors document). ⚠ **Pritunl n'est pas un VPN IPsec** : il repose sur **OpenVPN** (canal de contrôle TLS) et peut proposer **WireGuard** (hors document — à vérifier sur l'instance PLÉIADE). Cette fiche est donc **hors champ au sens strict** mais ses **principes sont transposables**. Ne jamais ouvrir les certificats/profils VPN : vérifications par la console d'administration ou la documentation.

| Contrôle | Applicabilité | Détail |
|---|---|---|
| **À vérifier : protocole réellement utilisé par Pritunl** (OpenVPN ? WireGuard ? IPsec ?) dans la console | **Applicable (préalable)** | Détermine quelle fiche s'applique : OpenVPN → logique TLS (REF-07) ; WireGuard → logique PSK/hybride ci-dessous ; IPsec → cette fiche intégralement. |
| **OpenVPN** : à vérifier — version d'OpenVPN/OpenSSL (≥ 3.5 pour un groupe hybride ML-KEM), `tls-version-min 1.3`, groupes ECDH (`tls-groups`), algorithme de chiffrement du canal de données (AES-256-GCM plutôt que AES-128 : REF-06 recommande ≥ 192 bits en PQ) | Partiellement (via REF-07/REF-06) | Le canal de contrôle OpenVPN est un handshake TLS : mêmes enjeux store-now decrypt-later. Support PQ réel côté OpenVPN/Pritunl **à vérifier**. |
| **WireGuard** : à vérifier — activation d'une **clé pré-partagée** (PresharedKey) par pair | Partiellement — **transition PQ** | Analogue à la voie PSK de la fiche (IPS-4/IPS-6) : protection PQ **temporaire**, gestion/distribution à maîtriser, une PSK **par paire de pairs** (REF-06 : « chaque secret pré-partagé ne doit l'être qu'entre deux entités »), PFS PQ non garantie si la PSK fuit. |
| **À vérifier : MTU du tunnel** et passage des **fragments** pour les tablettes hors ligne qui se resynchronisent par VPN (réseaux mobiles / Wi-Fi d'emprise) | **Applicable** | Annexe A : pare-feux rejetant les fragments ; IPv6 min. 1280 octets. Un handshake PQ plus gros (TLS dans le tunnel, ou OpenVPN lui-même) peut échouer silencieusement → tester la synchro LEAC après tout changement crypto. |
| **À vérifier : rotation des clés / renouvellement de session** du VPN | Applicable | Équivalent `CREATE_CHILD_SA` : rafraîchir les clés avec un nouvel échange (PFS). |
| Authentification des clients VPN (certificats Pritunl) | Applicable, PQ hors champ | Pas de standard hybride ; tailles de clés selon REF-06 (RSA ≥ 3072 recommandé, ≥ 2048 jusqu'à fin 2030). |
| Liens IPsec éventuels (interconnexion de site, routeur militaire) | Applicable si existants | Exiger IKEv2, RFC 7383, et à terme RFC 9370 + ML-KEM (strongSwan ≥ 6.0). |

**Échéance** : pas de date dans la fiche ; REF-06 → sécurité PQ visée pour tout usage au-delà du **1er janvier 2030** ou en cas de risque d'attaque rétroactive. Le VPN transporte **tout** le trafic des zones : c'est un candidat prioritaire à l'enregistrement « store now », donc à la transition.

## Limites / points d'attention

- Fiche spécifique **IPsec/IKEv2** : ne traite ni OpenVPN ni WireGuard (cas de Pritunl) — la transposition ci-dessus est une **analyse**, pas une prescription ANSSI.
- Aucune taille de paramètre imposée (renvoi REF-06 : ML-KEM-768 préférable, hybride obligatoire pour RègleSécuAsym).
- Les versions logicielles citées datent de 02/2026.
- RFC 9867 très récente (11/2025) : support logiciel à vérifier.
