# REF-06 — Règles et recommandations concernant le choix et le dimensionnement des mécanismes cryptographiques (Guide ANSSI)

- **Fichier** : `anssi-guide-mecanismes-crypto-3.00.pdf` · **Éditeur / référence** : ANSSI, **ANSSI-PG-083** · **Date / version** : **v3.00 du 2026-03-20** (« Menace quantique prise en compte ») — historique : 1.02 (2004-11-19, première version applicable), 1.10 (2006-12-19), 1.20 (2010-01-26), 2.00 (2012-06-18), 2.02 (2013-03-29), 2.04 (2020-01-01) · **Pages** : 81 · **Marquage** : public (Licence Ouverte v2.0 Etalab, cyber.gouv.fr)
- **Public visé** : développeur, administrateur, RSSI, DSI, utilisateur
- **Ingéré** : 2026-10-01
- *Convention de lecture* : dans l'extraction PDF les exposants sont aplatis ; ici `2^128` = 2 puissance 128.

## En une phrase

Le référentiel ANSSI qui fixe les **tailles minimales et propriétés** des mécanismes cryptographiques (symétrique ≥ 128 bits, bloc ≥ 128 bits, hachage ≥ 256 bits, RSA/DH ≥ 2048 bits **jusqu'à fin 2030 puis ≥ 3072 bits dès 2031**, courbes ≥ 250 bits, aléa à état interne ≥ 192 bits) et, nouveauté v3.00, des **règles/recos post-quantiques** (sym. ≥ 192 bits, hachage ≥ 384 bits, **hybridation classique + PQ obligatoire** pour ML-KEM/ML-DSA, viser le PQ pour tout usage **au-delà du 1er janvier 2030**).

## Ce que dit le document (synthèse structurée, fidèle)

### 1. Introduction (p. 4-7)
- **Objet** : règles et recommandations pour le **choix et le dimensionnement** de mécanismes cryptographiques.
- **Exclus** (§1.3) : la **gestion des clés** (document séparé : RGS Annexe B2, 2012) ; la liste exhaustive des mécanismes recommandés (→ **Guide de sélection d'algorithmes cryptographiques**, ANSSI 2021) ; l'implémentation (canaux auxiliaires, fautes) ; méthodes d'évaluation ; analyse de menaces ; lien avec Critères Communs ; fournitures d'évaluation ; **cryptographie quantique / QKD** et attaques avec accès en superposition à un oracle ; **mots de passe et biométrie** (→ guide ANSSI MFA et mots de passe, 2021), même s'ils utilisent de la crypto.
- **Règles** = conditions **nécessaires** (mécanisme « conforme au référentiel »), non suffisantes ; **Recommandations** = état de l'art avec marge substantielle, dérogeables pour contrainte majeure (fonctionnalité, performances, coût).
- **Règles PQ / Recos PQ** : conditions supplémentaires **seulement lorsqu'une résistance aux attaques quantiques est visée** ; une règle PQ est nécessaire pour revendiquer une protection contre un « adversaire quantique ».
- Analyse visant à rester valable **au moins 15 ans** ; mise à jour tous les **2 à 5 ans**. **Volontairement aucune table récapitulative** des tailles minimales (risque de confusion).
- Codification : `Règle<Domaine>.n` / `Reco<Domaine>.n` (ex. RègleFactorisation.3).

### 2. Règles et recommandations (p. 8-45)
Recommandations générales (RecoSécuLongTerme, RecoMécanismesÉprouvés) puis : 2.1 **symétrique** (taille de clé, chiffrement par bloc, modes, flot, MAC, hachage, XOF) ; 2.2 **asymétrique** (hypothèses de sécurité, factorisation, log discret GF(p), courbes GF(p) et GF(2^n), réseaux euclidiens, KEM/chiffrement, signature, authentification/établissement de clé, secrets faible entropie) ; 2.3 **aléa** (architecture, générateur physique, retraitement).
- Information p. 8 : attaque **« store now, decrypt later »** sur DH enregistré ; l'authentification est moins exposée au rétroactif **mais** les produits à longue durée de vie doivent **dès à présent** utiliser une authentification PQ ; la date 2030 est une estimation « très approximative » du temps de maturité du calcul quantique, révisable.
- §2.2 : meilleure sécurité long terme = mécanisme reposant **à la fois** sur un problème classique et un problème PQ (**principe de non-régression de sécurité**). Familles PQ citées : réseaux euclidiens, codes correcteurs, multivarié, isogénies.
- **Modes d'hybridation conformes** (p. 26-27) — KEM : (1) **classique + PQ** (méthode « la plus souhaitable », clés combinées par une KDF bien choisie, éventuellement avec chiffrés et clés publiques) ; (2) classique + **symétrique pré-partagé** (chaque secret partagé **entre deux entités seulement** ; perte possible de non-répudiation / PFS) ; (3) symétrique pré-partagé + PQ (difficilement compatible avec RecoPQConfidentialitéPersistante). Signatures : **concaténation** classique + PQ (valide ssi les deux sont valides) ; ou signature PQ à base de hachage (ex. SLH-DSA), conforme seule, hybridation optionnelle.

### Annexe A — Définitions (p. 46-65)
Rappels non mathématiques : confidentialité, intégrité, non-répudiation, authentification ; recherche exhaustive (table 2 des ordres de grandeur) ; modes CTR/CBC (IV aléatoire pour CBC, compteur jamais répété pour CTR — ex. messages ≤ 2^32−1 blocs et IV dont les 32 bits de poids faible sont nuls) ; MAC (≥ 96 bits typiquement ; CBC-MAC surchiffré, GMAC ; chiffrement authentifié **AES-GCM, AES-CCM**) ; modèles IND-CPA, IND-CCA2, INT-CTXT ; hachage (préimage, collision, anniversaires 2^(n/2)) ; XOF ; asymétrique (RSA-2048 = deux premiers de 1024 bits ; un module RSA de 256 bits se factorise en moins d'une heure) ; KEM (Fujisaki-Okamoto ; « chiffrement hybride » ≠ hybridation PQ) ; propriétés de signature (contrefaçon, **sécurité forte en contrefaçon**, propriété exclusive, signature liée au message, non-resignabilité) ; authentification + établissement de clé **imbriqués** contre l'attaque par le milieu ; réductions fines/lâches ; aléa (exemple DSA : 2 bits connus du nonce de 160 bits suffisent à retrouver la clé) ; **gestion de clés** : crypto-période, clés noires/rouges, **danger d'un secret largement partagé** entre de nombreux utilisateurs (préférer une architecture asymétrique avec bi-clés certifiées), PKI/IGC, séquestre.

### Annexe B — Éléments académiques (p. 66-70)
Coûts : en **2026**, casser une clé **DES 56 bits** ≈ **30 €** et **26 h** sur une machine dédiée d'≈ **100 k€** ; préimage partielle SHA-256 (79 bits à zéro) toutes les **10 min** dans Bitcoin (≈ 200 k€) ; recherche exhaustive 128 bits ≈ **100 milliards de milliards d'euros** → hors de portée. Attaques : 2016 Bhargavan-Leurent, bloc **64 bits en CBC**, ≈ **785 Go** capturés ; 2017 collision **SHA-1** en 2^63,1 (≈ 150 k€) ; 2020 collision à préfixe choisi SHA-1 en 2^63,5 (≈ 50 k€). Records : factorisation **829 bits** (2020-02-28, Thomé et al.) ; machine dédiée Shamir-Tromer (2003) : 1024 bits en < 1 an pour quelques dizaines de M€ (jamais construite) ; Mersenne 2^1039−1 (SNFS, 2007) ; log discret GF(p) **795 bits** (2019) ; courbes : **secp112r1** (2009), sect113r1 (2015), Koblitz 113 bits (2014), **ECCp-131 non résolu** ; SVP Darmstadt : dimension **210** (2026-01-01, Ding et Zhao).

## Toutes les règles et recommandations

> Liste **exhaustive** (numérotation d'origine). Total : **23 règles** (17 classiques + 6 PQ) et **23 recommandations** (16 classiques + 7 PQ) = **46**. Page = pagination imprimée du guide.

### Recommandations générales
| Réf. | Contenu | p. |
|---|---|---|
| **RecoSécuLongTerme** | En cas d'utilisation prévue **au-delà du 1er janvier 2030** ou de risque d'**attaque rétroactive**, viser une **sécurité post-quantique**. | 8 |
| **RecoMécanismesÉprouvés** | Employer des mécanismes **éprouvés et reconnus** par la communauté académique. | 8 |

### 2.1.1 Taille de clé symétrique
| Réf. | Contenu | p. |
|---|---|---|
| **RègleTailleCléSym** | Taille minimale des clés symétriques : **128 bits** (bits effectifs ; DES = 56 bits). | 10 |
| **RecoPQTailleCléSym** | En PQ, clés symétriques d'**au moins 192 bits**. (128 bits « présumé suffisant » contre Grover à assez long terme ; pourrait devenir une règle.) | 10 |
| Exemples | AES-128 conforme à la règle, **pas** à la reco PQ ; AES-192/256 conformes aux deux ; **Triple-DES deux clés non conforme** (112 bits). 64 bits « clairement insuffisant », 80 bits « pas hors de portée ». | 11 |

### 2.1.2.1 Chiffrement par bloc
| Réf. | Contenu | p. |
|---|---|---|
| **RègleTailleBlocSym** | Blocs d'**au moins 128 bits**. (Bloc 64 bits : limite des anniversaires atteinte après quelques Go.) | 12 |
| **RèglePrimChiffBloc** | Aucune attaque classique en **Nop < 2^128** (hors recherche exhaustive complète). | 13 |
| **RèglePQPrimChiffBloc** | En PQ, aucune attaque quantique avec **Nop < 2^80** et profondeur **Nprof < 2^48**. | 13 |
| **RecoPQPrimChiffBloc** | En PQ, aucune attaque quantique avec **Nop < 2^128** et **Nprof < 2^64**. | 13 |
| Exemples | AES-128 : conforme aux 2 règles, **pas** à RecoPQPrimChiffBloc ; AES-192/256 : conformes à tout ; **3DES trois clés non conforme** (attaque en 2^112) ; 3DES (2 ou 3 clés) non conforme à RègleTailleBlocSym (bloc 64 bits). | 12-14 |
| **RègleModeChiff** | Dans le modèle pertinent, aucune attaque de complexité < recherche exhaustive exploitant **Nbloc significativement < 2^(n/2)** blocs sous une même clé. | 14 |
| **RecoModeChiff** | 1. mode **non déterministe** ; 2. mode avec **preuve de sécurité** pertinente ; 3. **ne pas employer isolément un mode sans intégrité**. | 14 |
| Exemples | **CBC** avec AES et **IV aléatoire** par message, transmis en clair : conforme règle + Reco .1 et .2 (IV générés dans le périmètre de sécurité, avec un générateur d'aléa sûr, ni contrôlables ni prédictibles). **AES-GCM** : conforme règle et toutes les recos — **un même IV ne doit jamais être réutilisé sous une même clé**. CBC/OFB/CFB/CTR n'apportent **aucune intégrité**. | 15 |

### 2.1.2.2 Chiffrement par flot (dédié)
| Réf. | Contenu | p. |
|---|---|---|
| **RègleChiffFlot** | Aucune attaque classique avec **Nop < 2^128** et **au plus 2^64 bits** de flot de sortie. | 16 |
| **RèglePQChiffFlot** | En PQ, **état interne d'au moins 256 bits**. | 16 |
| **RecoChiffFlot** | 1. état interne **≥ 256 bits** ; 2. **compléter par un mécanisme d'intégrité** (malléabilité). | 16 |
| Exemple | **ChaCha20** conforme RègleChiffFlot, RèglePQChiffFlot, RecoChiffFlot.1 ; non conforme à .2 **s'il n'est pas complété par un mécanisme d'intégrité**. | 16 |

### 2.1.3 Intégrité (MAC)
| Réf. | Contenu | p. |
|---|---|---|
| **RègleMAC** | 1. primitive sous-jacente **conforme au référentiel** ; 2. aucune attaque classique avec **Nop < 2^128** et **Nbloc + Nforge < 2^64** ; 3. motif d'intégrité **≥ 96 bits** si la sécurité ne dépend pas de la taille des messages, **≥ 128 bits** sinon. | 17 |
| **RecoMAC** | 1. primitive conforme aux recos afférentes ; 2. **preuve de sécurité** ; 3. motifs **≥ 128 bits**. | 17 |
| **RèglePQMAC** | En PQ, primitive sous-jacente conforme aux **règles PQ** afférentes. | 17 |
| **RecoPQMAC** | En PQ, primitive conforme aux **recos PQ** afférentes. | 17 |
| Exemples | **CMAC-AES-128** (128 ou tronqué 96 bits) : conforme RègleMAC, RèglePQMAC, RecoMAC, **pas** RecoPQMAC ; **GMAC-AES-128** idem **si tag 128 bits** ; **HMAC-SHA-256 : conforme à toutes les règles et recos, y compris PQ** (HMAC n'exige pas la résistance en collision → 256 bits de sortie suffisent en PQ). **Non conformes** : CBC-MAC avec messages de taille variable (extension) ; CBC-MAC « retail » avec DES/3DES. CMAC/GMAC sûrs jusqu'à ≈ 2^(n/2) blocs ; CBC-MAC = IV fixé à zéro. | 18-19 |

### 2.1.4 Hachage et XOF
| Réf. | Contenu | p. |
|---|---|---|
| **RègleHachage** | 1. empreintes **≥ 256 bits** ; 2. meilleure attaque en collision ≈ **2^(h/2)** ; 3. meilleure attaque en préimage ≈ **2^h**. | 19 |
| **RecoHachage** | Déconseillé d'employer une fonction pour laquelle une **attaque partielle** est connue. | 20 |
| **RecoPQHachage** | En PQ, empreintes **≥ 384 bits**. (Attaques quantiques en collision 2^(h/3) ou 2^(2h/5) → pour h = 256 : ≈ 2^85 ou 2^102 ; 256 bits « présumé suffisant » à assez long terme.) Pour les signatures PQ à base de hachage sans besoin de collision : **≥ 128 bits** (classique), **≥ 192 bits** recommandé (PQ). | 20 |
| Exemples | **SHA2-256, SHA3-256** : conformes règles + RecoHachage, **pas** RecoPQHachage ; **SHA3-384** conforme à tout. **Non conformes** : **SHA-1** (Hachage.1 et .2 ; collision pratique ≈ 2^63 publiée en 2017) ; **SHA3-224** (Hachage.1) ; **SHAKE-128 à 256 bits de sortie** (Hachage.3 : préimage en 2^128). | 21 |
| **RègleXOF** | 1. collision ≥ **min(2^(h/2), 2^128)** ; 2. préimage ≥ **min(2^h, 2^128)**. | 21 |
| **RèglePQXOF** | En PQ : 1. pas d'attaque quantique en collision avec **Nop < min(2^(h/3), 2^80)** et **Nprof < 2^48** ; 2. pas d'attaque en préimage avec **Nop < min(2^(h/2), 2^80)** et **Nprof < 2^48**. | 21-22 |
| **RecoXOF** | 1. préimage ≥ **min(2^h, 2^256)** ; 2. déconseillé si attaque partielle connue. | 22 |
| **RecoPQXOF** | En PQ : 1. collision : **Nop ≥ min(2^(h/3), 2^128)**, **Nprof ≥ 2^64** ; 2. préimage : **Nop ≥ min(2^(h/2), 2^128)**, **Nprof ≥ 2^64**. | 22 |
| Exemples | **SHAKE-256** conforme à tout ; **SHAKE-128** conforme RègleXOF.1/.2, RèglePQXOF.1/.2, RecoXOF.2, **pas** RecoXOF.1, RecoPQXOF.1/.2. Une XOF conforme peut donner une fonction de hachage non conforme (SHAKE-128/256 bits). | 23 |

### 2.2 Asymétrique — hypothèses
| Réf. | Contenu | p. |
|---|---|---|
| **RègleSécuAsym** | Contre un adversaire classique, la sécurité repose sur au moins : un **problème mathématique largement éprouvé** ou un **mécanisme symétrique conforme**. | 24 |
| **RèglePQSécuAsym** | En PQ, sécurité reposant sur au moins : un problème **présumé résistant au calcul quantique** ou un mécanisme symétrique conforme. (= définition d'un « mécanisme post-quantique ».) | 24 |
| Conséquences | Factorisation / log discret : conformes à RègleSécuAsym, **non** à RèglePQSécuAsym (Shor). (M)LWE/(M)SIS : conformes à RèglePQSécuAsym, **non** à RègleSécuAsym. → **Aucun problème seul ne satisfait les deux : un produit PQ doit hybrider** (non-régression). | 25 |

### 2.2.1.1 Factorisation (RSA)
| Réf. | Contenu | p. |
|---|---|---|
| **RègleFactorisation** | 1. module **≥ 2048 bits** pour une utilisation **ne dépassant pas fin 2030** ; 2. **≥ 3072 bits** pour une utilisation **à partir de 2031** ; 3. exposant secret ≈ **même taille que le module** ; 4. en **chiffrement**, exposant public **> 2^16 = 65536** et **≤ 256 bits** ; 5. premiers choisis **aléatoirement uniformément** (éventuellement sous conditions satisfaites par un grand sous-ensemble). | 27 |
| **RecoFactorisation** | 1. modules **≥ 3072 bits même avant 2030** ; 2. pour **toute** application, exposant public **> 65536 et ≤ 256 bits** ; 3. premiers **de même taille**. | 27 |
| Information | Record 829 bits (2020) ; **1024 bits = prise de risque incompatible** ; 3072 bits ≈ 128 bits symétriques ; exposant 3 à proscrire en chiffrement et déconseillé partout ; e = **65537** usuel ; exposants secrets petits **à proscrire** ; p, q ni trop proches ni de tailles trop différentes ; **aucune sécurité PQ**. | 28 |

### 2.2.1.2 Logarithme discret
| Réf. | Contenu | p. |
|---|---|---|
| **RègleLogDiscretGFp** | 1. module premier **≥ 2048 bits** jusqu'à **fin 2030** ; 2. **≥ 3072 bits à partir de 2031** ; 3. sous-groupe d'ordre multiple d'un premier **≥ 250 bits**. | 29 |
| **RecoLogDiscretGFp** | 1. modules **≥ 3072 bits même avant 2030** ; 2. sous-groupes d'**ordre premier**. | 29 |
| **RègleCourbeElliptiqueGFp** | 1. sous-groupe d'ordre multiple d'un premier **≥ 250 bits** ; 2. courbes « particulières » (problème plus facile, ex. couplages) : le problème réduit doit respecter ses propres règles. | 30 |
| **RecoCourbeElliptiqueGFp** | Sous-groupes d'**ordre premier**. | 30 |
| Exemples conformes | **FRP256v1** (JO n° 241 du 16/10/2011, paramètres validés ANSSI) ; **P-256, P-384, P-521** (FIPS 186-5, 2023) ; **brainpoolP256r1, brainpoolP384r1, brainpoolP512r1**. | 31 |
| **RègleCourbeElliptiqueGF2n** | 1. ordre multiple d'un premier **≥ 250 bits** ; 2. **n premier** ; 3. courbes particulières : règles du problème réduit. | 31 |
| **RecoCourbeElliptiqueGF2n** | Sous-groupes d'ordre premier. | 31 |
| Exemples | **B-283, B-409, B-571** (FIPS 186-5) conformes. Corps finis de petite caractéristique, notamment GF(2^n) pour le log discret multiplicatif, **à proscrire** ; autres structures : avis ANSSI au cas par cas. Aucune sécurité PQ. | 29, 32 |

### 2.2.1.3 Réseaux euclidiens
| Réf. | Contenu | p. |
|---|---|---|
| **RèglePQRéseauEuclidien** | 1. (M)LWE et 2. (M)SIS : meilleure attaque quantique ≥ résolution de **SVP en dimension 400** (≈ **2^94** au moins). | 32 |
| **RecoPQRéseauEuclidien** | 1. (M)LWE et 2. (M)SIS : ≥ **SVP en dimension 600** (≈ **2^143** au moins). | 32 |

### 2.2.2 Encapsulation de clé / chiffrement asymétrique
| Réf. | Contenu | p. |
|---|---|---|
| (exigence de base) | Tout KEM / chiffrement asymétrique doit être **a minima sémantiquement sûr** (IND-CPA). | 34 |
| **RecoConfidentialitéAsym** | 1. mécanismes avec **preuve de sécurité** ; 2. en hybridation, preuves **dans le même modèle** et mode d'hybridation sûr contre l'adversaire le plus fort supporté par les deux. | 34 |
| Conformes | **ECIES-KEM** (ISO 18033-2) — à hybrider avec un KEM PQ pour le PQ ; **ML-KEM-512** (FIPS 203) **si hybridé** — **ML-KEM-768 préférable** ; **Frodo-KEM-640** si hybridé — **Frodo-KEM-976 préférable** ; **RSAES-OAEP** (PKCS#1 v2.1) sous RègleFactorisation.1-4, à hybrider pour le PQ. | 34-35 |
| Non conformes | **ML-KEM seul** (tout jeu de paramètres) : viole RègleSécuAsym ; **RSAES PKCS#1 v1.5** là où un oracle de padding est possible (Bleichenbacher 1998). | 35 |

### 2.2.3 Signature
| Réf. | Contenu | p. |
|---|---|---|
| (exigence de base) | Tout mécanisme de signature doit être **a minima robuste aux contrefaçons**. | 35 |
| **RecoSignature** | 1. **preuve de sécurité** ; 2. en hybridation, preuves dans le même modèle et mêmes propriétés additionnelles. Le hachage avant signature doit avoir un niveau cohérent. | 35-36 |
| Conformes | **RSA-SSA-PSS** (PKCS#1 v2.1) sous RègleFactorisation.1-4 ; **ECDSA** (FIPS 186-5) et **ECKCDSA** avec **FRP256v1, P-256, P-384, P-521, B-283, B-409, B-571** ; hybridation possible : signer avec **ML-DSA** (FIPS 204) puis signer (message, signature) avec le mécanisme classique ; **SLH-DSA** (FIPS 205) conforme **aux deux règles seul** → « peut être utilisé tel quel **après 2030** ». | 36 |
| Non conformes | **RSA-SSA PKCS#1 v1.5** si **e petit** et vérification de padding mal implémentée (Bleichenbacher 2006) ; **ML-DSA seul**. | 36-37 |
| Attention / Information | Propriétés additionnelles parfois nécessaires (sécurité forte en contrefaçon, propriété exclusive, liée au message, non-resignabilité). Exemples : ECDSA dans Bitcoin (malléabilité) ; **« Le protocole SSH requiert que les signatures satisfassent la sécurité forte en contrefaçon. L'utilisation d'ECDSA n'est pas compatible avec ce protocole »** ; ACME/Let's Encrypt préliminaire (RSA sans propriété exclusive) ; DRKey (non-resignabilité). | 37 |

### 2.2.4 Authentification d'entités et établissement de clé
| Réf. | Contenu | p. |
|---|---|---|
| **RecoConfidentialitéPersistante** | 1. compromission de secrets long terme **sans effet sur les sessions passées** (PFS) ; 2. **effacer** tout secret temporaire (éphémères, clé de session) **au plus tard à la fin de chaque session**. | 38 |
| **RecoPQConfidentialitéPersistante** | En PQ, PFS maintenue **face à un adversaire quantique** qui compromet les secrets long terme. Non conforme : **DH hybridé avec une clé pré-partagée** (compromission de la PSK → déchiffrement du passé). | 39 |
| **RègleSecretFaibleEntropie** | Si un mécanisme d'authentification utilise un **secret de faible entropie** (mot de passe, biométrie), **aucune recherche exhaustive hors ligne** ne doit être possible pour un attaquant actif ou passif. Exemple : 8 caractères alphanumériques = **au mieux 47 bits** d'entropie. Attention aux attaques anniversaires sur une liste d'empreintes de mots de passe. | 39 |
| Information | Lier authentification et établissement de clé (attaques par le milieu). | 38 |

### 2.3 Génération d'aléa
| Réf. | Contenu | p. |
|---|---|---|
| **RègleArchiGénAléa** | 1. **retraitement algorithmique avec état interne** obligatoire ; 2. sans générateur physique : **mémoire non volatile** ; 3. état interne **≥ 192 bits** ; 4. sources d'initialisation donnant une entropie voisine de la longueur de l'état (ou au moins ≥ seuil de .3 si justifié). | 41-42 |
| **RecoArchiGénAléa** | État interne **≥ 256 bits**, mémoire non volatile, **rafraîchissement régulier** par une source d'aléa. | 42 |
| Information | Générateur physique **non retraité exclu** ; « lissages » insuffisants ; tests statistiques en sortie de retraitement **inutiles voire dangereux** ; générateur physique évalué **AIS31 (BSI)** présumé conforme. Sources : physique, **systémique** (ex. `/dev/random` Linux), importée, manuelle. | 42-43 |
| **RègleGénPhysAléa** | 1. **description fonctionnelle** du générateur physique ; 2. tests statistiques (usine/ponctuels) sans défaut significatif. | 43 |
| **RecoGénPhysAléa** | Un **raisonnement** justifie la qualité de l'aléa (tests NIST FIPS 140-2, SP 800-22 cités en exemple). | 43 |
| **RègleGénAléaRetraitement** | 1. primitives **conformes** ; 2. état interne fiable → sorties parfaitement aléatoires même si les sources défaillent, sans fuite sur l'état ; 3. compromission de l'état/sources → **rien sur les sorties passées**. | 44 |
| Conformes | **NIST SP 800-90A r1** : **HMAC_DRBG** et **Hash_DRBG avec SHA-384**, **CTR_DRBG avec AES-256**. | 45 |

## Tableau « autorisé / recommandé / à proscrire »

| Famille | Autorisé (conforme aux règles) | Recommandé (recos, dont PQ) | À proscrire / non conforme | Échéance |
|---|---|---|---|---|
| Clé symétrique | ≥ 128 bits (AES-128) | ≥ 192 bits en PQ (AES-192/256) | ≤ 112 bits (3DES 2 clés), 64, 80 bits | — |
| Chiffrement par bloc | AES-128/192/256 | AES-192/256 (RecoPQPrimChiffBloc) | **3DES** (2 et 3 clés : bloc 64 bits ; attaque 2^112) | — |
| Mode | CBC (IV aléatoire), CTR (compteur non répété), GCM | Non déterministe, prouvé, **avec intégrité** (AES-GCM, IV jamais réutilisé) | Mode sans intégrité **isolé** ; réutilisation d'IV ; mode déterministe | — |
| Flot | ChaCha20 | + mécanisme d'intégrité ; état ≥ 256 bits | Flot sans intégrité (malléable) | — |
| MAC | HMAC-SHA-256, CMAC-AES, GMAC-AES (tag 128) ; tag ≥ 96 bits | Tag ≥ 128 bits ; HMAC-SHA-256 conforme aussi en PQ | CBC-MAC taille variable ; CBC-MAC retail DES/3DES ; GMAC tronqué < 128 | — |
| Hachage | SHA2-256, SHA3-256 | **SHA3-384** (≥ 384 bits en PQ) ; SHAKE-256 | **SHA-1**, SHA3-224, SHAKE-128 tronqué à 256 bits comme hachage | — |
| RSA (chiffrement/signature) | Module ≥ 2048 ; OAEP ; PSS ; e > 65536 (≤ 256 bits) en chiffrement | **≥ 3072 bits dès maintenant** ; e > 65536 pour toute application | 1024 bits ; e = 3 ; petits exposants secrets ; PKCS#1 v1.5 chiffrement (oracle de padding) ; PKCS#1 v1.5 signature avec e petit / padding mal vérifié | **2048 bits jusqu'à fin 2030 ; ≥ 3072 bits à partir de 2031** |
| DH GF(p) | Module ≥ 2048, sous-groupe ≥ 250 bits | ≥ 3072 bits ; ordre premier | Corps de petite caractéristique | **≥ 3072 à partir de 2031** |
| Courbes elliptiques | FRP256v1, P-256/384/521, brainpoolP256r1/384r1/512r1, B-283/409/571 ; ordre ≥ 250 bits | Ordre premier | n composé (GF(2^n)) ; courbes « particulières » mal choisies | Aucune sécurité PQ |
| Signature classique | ECDSA/ECKCDSA (courbes listées), RSA-PSS | Avec preuve ; hybridation PQ si long terme | **ECDSA dans SSH** (sécurité forte requise) | — |
| KEM PQ | ML-KEM-512, Frodo-KEM-640 **hybridés** | **ML-KEM-768**, **Frodo-KEM-976** hybridés ; réseaux ≥ SVP dim. 600 | **ML-KEM seul** | Viser le PQ si usage > 01/01/2030 |
| Signature PQ | ML-DSA **hybridé** (concaténation) ; **SLH-DSA seul** | SLH-DSA utilisable tel quel après 2030 | **ML-DSA seul** | — |
| Hybridation | Classique + PQ (le plus souhaitable) ; classique + PSK (paire unique) | PFS PQ préservée | DH + PSK (non conforme à RecoPQConfidentialitéPersistante) | — |
| Aléa | Retraitement à état ≥ 192 bits | État ≥ 256 bits, rafraîchi ; HMAC/Hash_DRBG SHA-384, CTR_DRBG AES-256 | Générateur physique non retraité ; « lissage » | — |
| Secrets faibles | Pas de recherche exhaustive hors ligne possible | — | Empreinte de mot de passe attaquable hors ligne | — |

## Chiffres et seuils à retenir

- **128** bits sym. min. · **192** bits sym. recommandé PQ · **256** bits état interne flot PQ.
- Bloc **≥ 128 bits** · limite des anniversaires **2^(n/2)** blocs par clé.
- MAC : tag **≥ 96 bits** (≥ 128 si dépend de la longueur, ex. GMAC) ; **128** recommandé.
- Hachage **≥ 256 bits** ; **≥ 384 bits** recommandé PQ.
- RSA/DH : **2048 bits jusqu'au 31/12/2030**, **3072 bits à partir de 2031** (3072 recommandé dès maintenant) ; e = **65537** ; exposant public chiffrement **> 2^16** et **≤ 256 bits**.
- ECC : sous-groupe **≥ 250 bits**.
- Réseaux : SVP dim. **400** (règle, ≈ 2^94) / **600** (reco, ≈ 2^143).
- Aléa : état interne **≥ 192 bits** (règle) / **≥ 256 bits** (reco).
- Date pivot : **1er janvier 2030** (RecoSécuLongTerme).
- Mot de passe 8 alphanum. : **≤ 47 bits** d'entropie.
- Ordres de grandeur (table 2) : 2^32 op/s par cœur 4 GHz ; 2^60 op/s meilleurs supercalculateurs ; 2^128 = toute la puissance mondiale pendant 13,8 milliards d'années.
- Records : RSA **829** bits (2020) ; log discret GF(p) **795** bits (2019) ; SVP dim. **210** (2026).
- Validité visée du guide : **≥ 15 ans** ; révision tous les **2 à 5 ans**.

## Application à PLÉIADE

> Analyse MINERVE/CYBERSECU, **hors document**. Les comportements des produits (Traefik, Keycloak, Next.js/Auth.js, Node.js, Pritunl) sont donnés comme **pistes à vérifier**, pas comme faits.

### TLS de Traefik et PKI de zone
| À vérifier | Statut | Règle(s) |
|---|---|---|
| Algorithme et taille de la **clé de la CA racine** de zone (`pleiade-infra/pki`) : RSA ≥ 3072 ou ECDSA P-256/P-384 | **Applicable** | RègleFactorisation.1-2, RecoFactorisation.1, RègleCourbeElliptiqueGFp |
| **Durée de validité de la CA** : si elle dépasse le **31/12/2030**, une RSA-2048 devient non conforme → 3072 ou ECDSA | **Applicable — échéance 2031** | RègleFactorisation.2 |
| Certificats serveurs : RSA ≥ 2048 (≥ 3072 conseillé) ou ECDSA courbe listée ; signature **RSA-PSS ou ECDSA** (pas de SHA-1) ; empreinte SHA-256 minimum | Applicable | RègleHachage.1, RecoSignature |
| Suites symétriques : **AES-GCM** (de préférence AES-256 pour la reco PQ) ou ChaCha20-Poly1305 ; **pas de 3DES, pas de CBC sans intégrité, pas de SHA-1** | Applicable | RègleTailleBlocSym, RecoModeChiff.3, RecoPQTailleCléSym |
| Échange de clés éphémère (**PFS**) obligatoire ; ECDHE sur courbes ≥ 250 bits ; groupe **hybride + ML-KEM-768** dès que Traefik le permet | Applicable — **transition PQ** | RecoConfidentialitéPersistante, RecoSécuLongTerme, ML-KEM-768 hybridé (cf. REF-07) |
| Groupes DH finis (`ffdhe`) éventuels ≥ 2048 (≥ 3072 en 2031) | Partiellement | RègleLogDiscretGFp |

### SSH du serveur
| À vérifier | Statut | Règle(s) |
|---|---|---|
| Clés hôte et admin : RSA ≥ 3072 conseillé ; **éviter ECDSA en SSH** (texte du guide) ; Ed25519 **non cité** → à arbitrer avec le guide de sélection ANSSI | Applicable | RègleFactorisation, Information §2.2.3 |
| KEX hybride ML-KEM (OpenSSH ≥ 10.0) | Applicable — **transition PQ** | RecoSécuLongTerme (cf. REF-08) |
| Chiffrement AES-GCM / ChaCha20-Poly1305 ; MAC HMAC-SHA-256/512 ; retrait de `hmac-sha1`, `3des-cbc` | Applicable | RègleHachage, RègleTailleBlocSym |
| Authentification par mot de passe désactivée | Applicable | RègleSecretFaibleEntropie |

### VPN Pritunl (OpenVPN / WireGuard — protocole à confirmer)
| À vérifier | Statut | Règle(s) |
|---|---|---|
| Canal de données AES-256-GCM (ou ChaCha20-Poly1305) ; pas de BF-CBC/3DES (bloc 64 bits — cf. attaque 785 Go) | Applicable | RègleTailleBlocSym, RecoPQTailleCléSym |
| Certificats VPN : RSA ≥ 2048 (≥ 3072 conseillé / 2031) ou ECDSA courbe listée | Applicable (sans ouvrir les certificats : vérifier via la console) | RègleFactorisation |
| PSK WireGuard éventuelle : **une par paire**, consciente de la perte de PFS PQ | Partiellement — **transition PQ temporaire** | Modes d'hybridation p. 26, RecoPQConfidentialitéPersistante |

### Keycloak — mots de passe
| À vérifier | Statut | Règle(s) |
|---|---|---|
| Politique de hachage des mots de passe (algorithme, nombre d'itérations / coût) : l'empreinte stockée ne doit pas permettre une **recherche exhaustive hors ligne** praticable (sel unique, fonction lente) | **Partiellement** (mots de passe hors champ du guide ; renvoi au guide ANSSI MFA/mots de passe) | RègleSecretFaibleEntropie |
| Politique de longueur des mots de passe (8 alphanum. ≤ 47 bits) ; MFA pour les comptes d'administration de zone | Partiellement | RègleSecretFaibleEntropie |
| Clés de signature des jetons OIDC : **RS256 = RSASSA-PKCS1-v1_5** (non conforme si e petit / padding mal vérifié) → préférer **PS256** (RSA-PSS) ou **ES256** (ECDSA P-256), clé RSA ≥ 2048 (3072 conseillé) ; rotation des clés de realm | Applicable | RecoSignature, RègleFactorisation |

### Secrets applicatifs Next.js (AUTH_SECRET, JWT), clés d'API, aléa
| À vérifier | Statut | Règle(s) |
|---|---|---|
| `AUTH_SECRET` / secrets JWT HS256 : **≥ 128 bits d'aléa réel** (≥ 192, idéalement 256 bits, pour la reco PQ), générés par un CSPRNG, **distincts par app et par zone** | **Applicable** | RègleTailleCléSym, RecoPQTailleCléSym |
| JWT signés **HS256 = HMAC-SHA-256** : conforme (y compris PQ) ; jetons chiffrés (JWE) en **AES-GCM** sans réutilisation d'IV | Applicable | RègleMAC, Exemple HMAC-SHA-256, RecoModeChiff |
| Clés de service `X-API-Key` : ≥ 128 bits d'aléa ; **éviter une clé unique partagée par toutes les apps** (Annexe A.4.1 : secret largement partagé = conséquences dramatiques ; « chaque secret pré-partagé ne doit l'être qu'entre deux entités ») → **une clé par couple appelant/appelé**, crypto-période et rotation | **Applicable** | RègleTailleCléSym, A.4.1, p. 26 |
| Stockage des clés d'API côté serveur : comparer une **empreinte HMAC/SHA-256** plutôt que la clé en clair (une clé à haute entropie n'est pas un « secret faible ») | Applicable | RègleHachage |
| Génération d'aléa : `crypto.randomBytes` / `crypto.randomUUID` / `/dev/urandom` (CSPRNG noyau à retraitement) — **jamais `Math.random()`** pour un secret, un IV, un jeton | Applicable | RègleArchiGénAléa, RègleGénAléaRetraitement |
| **Conteneurs et tablettes** : aléa disponible dès le démarrage (pas de graine figée dans une image Docker, pas de secret généré au build et copié dans l'image) | Applicable | RègleArchiGénAléa.4 (entropie d'initialisation) |
| Données chiffrées au repos sur tablettes hors ligne (si existant) : AES-256-GCM, clé ≥ 128 bits non dérivée d'un code court sans fonction lente | Applicable si la fonction existe | RègleTailleCléSym, RègleSecretFaibleEntropie |

### Transition post-quantique — synthèse des échéances
| Échéance | Action |
|---|---|
| **Dès maintenant** (risque rétroactif, RecoSécuLongTerme) | Échange de clés **hybride** (ML-KEM-768 + ECDHE) sur Traefik, SSH (OpenSSH ≥ 10.0) et VPN dès que les briques le permettent ; AES-256 et SHA-384 pour la marge PQ. |
| **Avant le 31/12/2030** | Toute clé RSA/DH devant servir en 2031 passée à **≥ 3072 bits** (CA de zone en premier). |
| **Au-delà du 01/01/2030** | Viser une authentification PQ hybride (ML-DSA + classique) ou SLH-DSA quand les standards protocolaires existeront (cf. REF-07/08/09 : pas encore). |
| Hors champ | Symétrique déjà conforme (AES-128 reste conforme aux règles PQ) ; HMAC-SHA-256 conforme PQ. |

## Limites / points d'attention

- Le guide fixe des **minima et des principes**, pas une liste exhaustive : pour choisir concrètement un algorithme, il renvoie au **Guide de sélection d'algorithmes cryptographiques (ANSSI, 2021)** — non ingéré. **X25519/Ed25519/Curve25519, Poly1305, Argon2, PBKDF2, bcrypt ne sont pas mentionnés** : leur absence ne vaut ni conformité ni non-conformité.
- **Gestion des clés** (cycle de vie, stockage, révocation) **exclue** → RGS Annexe B2 (non ingéré).
- **Mots de passe** exclus (seule RègleSecretFaibleEntropie s'applique) → guide ANSSI MFA/mots de passe 2021 (non ingéré).
- Implémentation (canaux auxiliaires) exclue.
- Les seuils PQ sont des **recommandations** qui « pourraient devenir des règles » si le calcul quantique progresse ; la date 2030 est « très approximative ».
- Le respect des règles est **nécessaire mais pas suffisant** : une analyse spécifique reste requise.
- Non normatif hors disposition réglementaire ; à valider par l'administrateur/RSSI.
