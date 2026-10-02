# REF-07 — Transition post-quantique de TLS 1.3 (Fiche technique ANSSI)

- **Fichier** : `transition_post_quantique_tls_1_3.pdf` · **Éditeur / référence** : ANSSI, **ANSSI-FT-115** · **Date / version** : v1.0 du 02/02/2026 (version initiale) · **Pages** : 16 · **Marquage** : public (Licence Ouverte v2.0 Etalab, téléchargeable sur cyber.gouv.fr)
- **Public visé** (page de garde) : développeur, administrateur, RSSI, DSI, utilisateur
- **Ingéré** : 2026-10-01

## En une phrase

État des lieux de la migration post-quantique de TLS 1.3 (RFC 8446) : seul le protocole **Handshake** est menacé (échange DH + signatures) ; l'ANSSI **privilégie l'hybridation** (classique + post-quantique, ex. ECDH + ML-KEM) et admet la **clé pré-partagée (PSK)** comme mesure **temporaire** ; l'échange de clés hybride est déjà implémenté (OpenSSL 3.5.0, Chrome), l'authentification hybride n'est **pas encore standardisée**.

## Ce que dit le document (synthèse structurée, fidèle)

### 1. Introduction (p. 3)
- Complète l'**avis de l'ANSSI sur la migration vers la cryptographie post-quantique** [5, 6].
- La cryptographie asymétrique actuelle est vulnérable à la menace quantique ; objectif : remplacer signatures classiques par signatures post-quantiques, et échanges DH par des **KEM** (Key Encapsulation Mechanism) post-quantiques.
- **Pendant la transition, l'hybridation est recommandée par l'ANSSI** : un mécanisme classique éprouvé (mais vulnérable au quantique) combiné à un mécanisme supposé résistant au quantique (mais dont l'assurance de robustesse est moindre).
- Conséquence : **forte augmentation de la taille des messages** d'échange de clés et d'authentification (clés, chiffrés, signatures PQ très grands).
- Cryptographie symétrique non menacée, mais **l'ANSSI recommande d'augmenter les tailles de clés symétriques et des sorties de hachage** [5, 6].

### 2. Présentation de TLS 1.3 (p. 4-6)
- Trois sous-protocoles : **Handshake** (négociation des suites, secret partagé, authentification serveur et optionnellement client, dérivation des clés), **Record** (fragmentation, protection symétrique confidentialité + intégrité), **Alert** (messages d'erreur, sans crypto propre).
- Seul le **Handshake** est impacté (DH + signatures). Record et Alert ne le sont pas (mais la sécurité des clés du Record dépend du Handshake).
- Le document ne considère que **l'authentification par signature, recommandée par l'ANSSI** [7 = guide « Recommandations de sécurité relatives à TLS »].
- Handshake (fig. 2) : `ClientHello` (suites symétriques + hachage de la KDF, **groupes DH supportés avec une clé publique par groupe**, mécanismes de signature supportés, identifiant de PSK éventuel) → `ServerHello` (choix, groupe DH négocié + clé publique) → `EncryptedExtensions` → `[CertificateRequest]` → `Certificate` + `CertificateVerify` (signature sur les messages échangés) → `Finished` ; côté client : `[EndOfEarlyData]`, `[Certificate]`, `[CertificateVerify]`, `Finished`. Tous les messages sauf `ClientHello`/`ServerHello` sont protégés par le Record.
- Deux types de PSK : **« resumption psk »** (issue d'une session TLS 1.3 précédente) et **« external psk »** (établie hors TLS). Il est possible de négocier une PSK **sans** échange DH : la sécurité repose alors **uniquement** sur la PSK. Avec PSK, `Certificate`/`CertificateVerify` deviennent optionnels (authentification implicite).
- **0-RTT** (note 1, p. 6) : données applicatives envoyées dès le `ClientHello`, chiffrées avec la PSK, **sans confidentialité persistante (PFS)**.

### 3. Transition post-quantique (p. 7-10)
- Deux voies : PSK (§3.1) ou **hybridation (§3.2) = solution privilégiée par l'ANSSI**.
- **La transition pour la confidentialité est plus urgente que pour l'authentification**, à cause des attaques **« store-now decrypt-later »**.

#### 3.1 PSK
- Utilisable si **confidentialité et intégrité (classiques ET post-quantiques) de la PSK** sont assurées ; attention particulière à la **gestion/distribution** ; **mesure temporaire** : hybridation et mécanismes PQ « devront être effectuées à terme ».
- Confidentialité PQ possible via dérivation des clés à partir de la PSK.
- **Attention** : compromission de la PSK **rétroactive** sur toutes les sessions qui l'ont utilisée. Exemple : PSK fixe + nouveau secret DH par session → PFS assurée en classique mais **pas en post-quantique** (un attaquant quantique casse les DH enregistrés).
- La PSK assure aussi une authentification mutuelle → même solution envisageable pour l'authentification PQ.
- Implémentation : **OpenSSL** implémente TLS 1.3 avec PSK.

#### 3.2.1 Hybridation de l'échange de clés
- Deux échanges : classique (ex. DH) + post-quantique (ex. **ML-KEM**, FIPS 203), puis **combinaison** des deux secrets. **Attention** : la combinaison doit assurer une sécurité classique ET PQ (méthodes citées dans l'avis ANSSI).
- Modifications : `ClientHello` liste des **noms de mécanismes hybrides** (groupe DH + KEM) avec clé publique DH et clé publique KEM (**concaténables**) ; `ServerHello` renvoie le mécanisme hybride négocié + clé publique DH + **chiffré d'encapsulation** (concaténables) ; `EncryptedExtensions` / `HelloRetryRequest` peuvent lister des groupes hybrides.
- **Attention** : proposer plusieurs hybrides rend le `ClientHello` **de taille conséquente**.
- Documents : draft *Hybrid key exchange in TLS 1.3* (draft-ietf-tls-hybrid-design-12, janv. 2025) [15] ; draft *Post-quantum hybrid ECDHE-MLKEM Key Agreement for TLSv1.3* (draft-ietf-tls-ecdhe-mlkem-01, sept. 2025) [10] ; draft *ML-KEM Post-Quantum Key Agreement for TLS 1.3* (non hybride, draft-ietf-tls-mlkem-00, avril 2025) [8].
- Implémentations : **OpenSSL 3.5.0** (DH + ML-KEM hybride) ; **Google Chrome** (DH + ML-KEM, « fonctionnel uniquement sur les navigateurs de poste bureautique ») ; **Meta**, bibliothèque TLS **Fizz** avec **liboqs**.

#### 3.2.2 Hybridation de l'authentification par signature
- Nécessite signatures **et certificats** hybrides (deux certificats distincts, ou un certificat sur la concaténation des clés, etc.) ; concerne aussi les **chaînes de certification**. **Pas de standard pour l'authentification hybride** à ce jour.
- Modifications : mécanismes de signature hybrides dans `ClientHello` et `CertificateRequest` ; certificats et signatures hybrides dans `Certificate`/`CertificateVerify`.
- Document : draft *Use of ML-DSA in TLS 1.3* (draft-ietf-tls-mldsa-01, sept. 2025) [9].
- Implémentation : **OpenSSL 3.5.0 implémente ML-DSA (FIPS 204) et SLH-DSA (FIPS 205), mais leur usage dans TLS 1.3 n'est pas encore possible**.
- Information : la fragmentation des gros messages est **gérée nativement** par TLS 1.3.

### 4. Conclusion (p. 11)
Hybridation recommandée pour l'échange de clés **et** l'authentification ; PSK « envisageable mais temporaire » ; suivre l'évolution des travaux et implémentations.

## Toutes les règles et recommandations

> Le document **ne comporte pas de règles numérotées** (pas de « RègleXXX/RecoXXX »). Les prescriptions figurent dans le texte et dans les encadrés « Attention ». La numérotation **TLS-n** ci-dessous est **ajoutée à l'ingestion** pour pouvoir les citer.

| N° (ajouté) | Prescription (texte du document) | Page |
|---|---|---|
| TLS-1 | Pendant la transition, **l'hybridation** (classique + post-quantique) est recommandée par l'ANSSI. | 3, 7, 11 |
| TLS-2 | Augmenter les **tailles de clés symétriques** et des **sorties de fonctions de hachage** (renvoi à l'avis ANSSI). | 3 |
| TLS-3 | Authentification TLS **par signature** (recommandée par l'ANSSI, guide TLS [7]) — seule considérée. | 4 |
| TLS-4 | Traiter **en priorité la confidentialité** (échange de clés) avant l'authentification (menace « store-now decrypt-later »). | 7 |
| TLS-5 | PSK admissible seulement si sa **confidentialité et son intégrité classiques et PQ** sont assurées, avec une attention particulière à sa **gestion et distribution**. | 7 |
| TLS-6 | PSK = **mesure temporaire** ; hybridation et mécanismes PQ **à mettre en œuvre à terme**. | 7, 11 |
| TLS-7 | Attention : compromission de PSK **rétroactive** → PFS non assurée en post-quantique. | 7 |
| TLS-8 | La **combinaison des secrets** classique et PQ doit assurer une sécurité classique ET post-quantique. | 8 |
| TLS-9 | Attention : plusieurs propositions hybrides → `ClientHello` **volumineux**. | 8 |
| TLS-10 | Hybridation de l'authentification : signatures **et certificats/chaînes** hybrides — **pas de standard** à ce jour ; suivre les travaux. | 9, 11 |
| TLS-11 | 0-RTT : données **sans PFS** (information, note 1). | 6 |

## Tableau « autorisé / recommandé / à proscrire »

| Élément | Statut selon la fiche | Échéance / remarque |
|---|---|---|
| TLS 1.3 avec échange de clés **hybride ECDHE + ML-KEM** | **Recommandé** (solution privilégiée) | Dès maintenant (urgence confidentialité) ; implémenté OpenSSL 3.5.0, Chrome desktop |
| ML-KEM **seul** (non hybride) dans TLS 1.3 | Décrit par un draft [8] ; **non recommandé** en soi (l'ANSSI recommande l'hybridation pendant la transition) | — |
| Échange DH/ECDHE **classique seul** | Vulnérable au quantique (store-now decrypt-later) | À faire évoluer vers l'hybride |
| **PSK** (external/resumption) pour sécurité PQ | **Toléré, temporaire**, sous conditions de gestion | Hybridation « à terme » |
| PSK fixe + DH (sans KEM PQ) | PFS **non assurée en PQ** | — |
| Authentification par **signature** (certificats) | **Recommandée** (vs PSK) | — |
| Signatures/certificats **hybrides** (ML-DSA + classique) | Souhaité, **pas encore standardisé** ; non utilisable dans TLS 1.3 avec OpenSSL 3.5.0 | Suivre draft-ietf-tls-mldsa |
| **0-RTT** | Pas de PFS (information) | — |
| Tailles symétriques / hachage | **À augmenter** (renvoi avis ANSSI ; cf. REF-06 : ≥192 bits sym., ≥384 bits hachage en PQ) | — |

> ⚠ **Codepoints / noms de groupes** : la fiche **ne donne aucun codepoint ni nom de groupe IANA** (elle cite seulement les drafts). Les noms courants (ex. `X25519MLKEM768`, `SecP256r1MLKEM768`) sont **hors document** — à vérifier dans les drafts/IANA avant usage.

## Chiffres et seuils à retenir

- Version visée : **TLS 1.3, RFC 8446**.
- **OpenSSL 3.5.0** : échange hybride DH + ML-KEM ; ML-DSA et SLH-DSA présents mais **pas utilisables dans TLS 1.3**.
- Standards NIST cités : **FIPS 203 (ML-KEM)**, **FIPS 204 (ML-DSA)**, **FIPS 205 (SLH-DSA)**.
- Drafts : hybrid-design **-12** (01/2025), ecdhe-mlkem **-01** (09/2025), mlkem **-00** (04/2025), mldsa **-01** (09/2025).
- Aucune date butoir propre à la fiche (l'échéance générale « au-delà du 1er janvier 2030 » vient de REF-06, RecoSécuLongTerme).

## Application à PLÉIADE

> Section d'**analyse** (MINERVE/CYBERSECU), non issue du document. Les éléments techniques sur les produits (Traefik, Go, Node) sont **hors document** et marqués « à vérifier ».

| Contrôle | Applicabilité | Détail |
|---|---|---|
| **À vérifier : Traefik n'accepte que TLS 1.3** (ou TLS 1.2 minimum durci), `minVersion` dans les `tlsOptions` | **Applicable** | La fiche ne traite que TLS 1.3 ; le guide TLS ANSSI [7] est la référence pour 1.2. |
| **À vérifier : groupes d'échange de clés de Traefik** (`curvePreferences`) — présence d'un groupe **hybride ECDHE + ML-KEM** en tête | **Applicable — transition PQ, priorité 1** | Traefik est écrit en Go ; les versions récentes de Go proposeraient un groupe hybride X25519+ML-KEM-768 (**hors document, à vérifier** selon la version de Traefik/Go déployée). Priorité car c'est la **confidentialité** (enregistrement du trafic des zones aujourd'hui, déchiffrement demain). |
| **À vérifier : taille du `ClientHello` hybride / MTU** via le VPN (tablettes au retour, liens dégradés) | Partiellement | TLS gère la fragmentation, mais des équipements intermédiaires peuvent mal supporter un gros `ClientHello` (TLS-9). Tester une synchro tablette via VPN après activation. |
| **À vérifier : 0-RTT désactivé** sur Traefik | **Applicable** | Pas de PFS en 0-RTT (TLS-11) ; risque de rejeu côté API (POST de synchro). |
| **À vérifier : authentification par certificat (signature)**, pas de PSK TLS | Applicable | TLS-3. La PKI de zone signe en classique (RSA/ECDSA) : **pas de certificat hybride disponible** aujourd'hui (TLS-10) → l'authentification PQ est **à suivre**, non bloquante (moins urgente que la confidentialité). |
| **À vérifier : clés et certificats de la CA de zone** (`pleiade-infra/pki`) — algorithme et taille | Applicable (renvoi REF-06) | RSA ≥ 2048 jusqu'à fin 2030, **≥ 3072 à partir de 2031** (3072 recommandé dès maintenant) ou ECDSA P-256/P-384. Durée de vie de la racine à confronter à 2030/2031. |
| **À vérifier : appels inter-apps** (Next.js → eho, Keycloak, `X-API-Key`) : passent-ils en HTTPS TLS 1.3 ou en HTTP clair sur le réseau Docker/Podman ? | Applicable | Si HTTP interne : hors périmètre de la fiche mais à documenter comme risque (en-tête `X-API-Key` en clair). |
| **À vérifier : clients Node.js** (fetch serveur) — version d'OpenSSL embarquée (≥ 3.5 pour l'hybride) | Partiellement | Le gain PQ n'existe que si **client ET serveur** négocient l'hybride. Navigateurs des tablettes : Chrome hybride « uniquement sur poste bureautique » selon la fiche → **les tablettes Android pourraient ne pas en bénéficier** (à vérifier). |
| Keycloak (OIDC sur TLS) | Applicable via Traefik | Mêmes contrôles TLS que les apps. |
| SSH / VPN | Hors champ de cette fiche | → REF-08 (SSH), REF-09 (IPsec, principes transposables au VPN). |

**Échéance transition PQ** : la fiche ne fixe pas de date ; REF-06 (RecoSécuLongTerme) recommande de viser la sécurité PQ pour tout usage **au-delà du 1er janvier 2030** ou s'il existe un risque d'**attaque rétroactive** → l'échange de clés hybride est à activer **dès que la pile le permet** ; l'authentification hybride attendra des standards.

## Limites / points d'attention

- Fiche d'**état des lieux** (non normative ; recommandations « livrées en l'état », à valider par l'administrateur/RSSI).
- **Aucun paramètre concret** (noms de groupes, codepoints, niveaux ML-KEM) : pour le dimensionnement, se reporter à REF-06 (ML-KEM-768 préféré à ML-KEM-512, hybride obligatoire pour RègleSécuAsym).
- Ne traite pas TLS 1.2, ni la configuration des suites symétriques (renvoi au guide TLS ANSSI [7], non ingéré ici).
- Références datées (drafts 2025) : sujet « très étudié », à réévaluer régulièrement.
- Mention de Chrome « uniquement sur poste bureautique » : à revalider à date, impacte les tablettes.
