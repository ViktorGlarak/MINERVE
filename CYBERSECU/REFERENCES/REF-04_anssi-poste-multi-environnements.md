# REF-04 — Sécurisation du poste de travail multi-environnements (non classifiés) — Les fondamentaux

- **Fichier** : `anssi-fondamentaux-securisation-poste-multi-environnements-v1-0.pdf` · **Éditeur / référence** : ANSSI, ANSSI-PA-114 · **Date / version** : v1.0 du 16/01/2026 (version initiale) · **Pages** : 26 · **Marquage** : public (Licence Ouverte Etalab v2.0). La mention « Diffusion Restreinte » du document désigne le **niveau de sensibilité des environnements** que le poste peut héberger (NP/DR au sens de l'II 901), pas le marquage du document.
- **Ingéré** : 2026-10-01

> ℹ Les « recommandations » prennent ici la forme de **fonctions de sécurité numérotées par section** (3.1.1 … 3.18.7) et de **recommandations non fonctionnelles** (4.1.1 … 4.6.3). Numérotation **d'origine** conservée.

## En une phrase

Pour faire cohabiter sur **un seul poste** plusieurs environnements de sensibilités ou d'opérateurs différents (jusqu'à NP/DR, jamais Secret), l'ANSSI exige un **socle** de confiance minimal qui isole chaque environnement utilisateur dans **sa propre machine virtuelle**, avec démarrage vérifié, chiffrement intégral, réseau contrôlé par le socle (VPN non débrayable), journalisation protégée et exploitation par rôles.

## Ce que dit le document

### 1. Préambule — périmètre
- **Destinataires : les éditeurs** de postes multi-environnements (conception et rédaction d'une cible de sécurité pour évaluation) — **pas les administrateurs système**.
- Principe : le **cloisonnement physique** (un poste par environnement) apporte les meilleures garanties ; le poste multi-environnements est un compromis (coût, mobilité, ergonomie, empreinte environnementale).
- Exemples d'environnements : bureautique, administration (guide PA-022), développement, auditeurs.
- Ne traite **que** le cloisonnement entre **systèmes d'exploitation complets** ; l'isolation d'applications (sandbox, **conteneurs**) dans un environnement n'est **pas** traitée.
- Combinaisons possibles : **NP/NP, NP/DR, DR/DR**, sans limite à deux environnements (ex. DR bureautique + NP admin SI X + NP admin SI Y). **Pas** Secret/Très Secret (IGI 1300).
- Hypothèses : poste de travail **mono-utilisateur**, utilisable en **nomadisme** (guide PA-054). Hérite des travaux **CLIP OS 4/5** (CLIP OS 4 agréé NP/DR ; plus maintenus). Agnostique de l'OS, exemples sous Linux. L'infrastructure de production et la PSSI de déploiement sont hors périmètre.

### 2. Définitions (§2.1)
Tâche, ressource, politique de sécurité, **machine virtuelle** (gérée par hyperviseur), **sandbox** (namespaces, cgroups, UID/GID — **noyau partagé**), **domaine** (ensemble des ressources accessibles à des tâches), **domaine utilisateur** (une VM par environnement), **domaine support** (VM ou sandbox pour une fonction autre), **cloisonnement**, **TCB** (base de confiance : une faille = compromission totale), **socle** (matériel + logiciel faisant tourner les domaines, inclut la TCB ; seules les tâches strictement nécessaires y tournent), **moniteur de référence**, **TPM / vTPM** (ISO/IEC 11889, TCG).

### 3. Architecture type (§2.2)
Deux domaines utilisateurs BUREAUTIQUE ; pour **chacun**, un domaine support **VMM** (gestionnaire de VM et périphériques émulés) et un domaine support **CRYPTO** (vTPM). Domaine support **JOURNALISATION** (journaux du socle, VMM, CRYPTO — **pas** ceux des domaines utilisateurs). Domaines supports **ADMIN, AUDIT, MISE_A_JOUR** pour l'exploitation. Valable quel que soit le nombre de domaines.

### 4. Choix technologique (§2.3)
- **VM obligatoires pour les domaines utilisateurs** : cloisonnement plus fort que les primitives noyau ; surface d'attaque réduite et auditable ; pas de noyau partagé → MCO/MCS indépendants.
- Domaines supports : VM ou sandbox possibles.
- Deux domaines **de même sensibilité doivent quand même être isolés** : « une sensibilité identique n'est pas synonyme d'un droit d'accès identique ».
- La sécurité du poste doit être indépendante du contenu des VM, mais il est recommandé de **durcir** aussi les systèmes invités (défense en profondeur).

### 5. Fonctions de sécurité (chap. 3) — voir liste exhaustive ci-dessous
Thèmes : chaîne de démarrage, intégrité du socle, chiffrement, mémoire vive, durcissement, périphériques émulés/délégués/externes, réseau, temps, journalisation, mise à jour, exploitation, démarrage des domaines, authentification, affichage de confiance, options utilisateur, diodes inter-domaines. Les exemples **illustrent** et ne suffisent pas toujours à implémenter.

### 6. Recommandations non fonctionnelles (chap. 4)
Sensibilité du socle, documentation + SBOM, effacement sécurisé, évaluabilité, défense en profondeur, maintenance.

## Toutes les recommandations

**3.1 Chaîne de démarrage du socle**
- **3.1.1** Intégrité, authenticité et **non-retour en arrière** de la chaîne de démarrage (exécutables et configurations), même face à un attaquant root ou avec accès physique. *Ex. : UEFI Secure Boot + Measured Boot sur RTM (TPM). Retour arrière toléré, limité et contrôlé, pour le fallback de mise à jour.*
- **3.1.2** Configuration du **firmware non modifiable** par l'utilisateur. *Ex. : mot de passe firmware unique à la machine.*

**3.2 Intégrité du socle**
- **3.2.1** Intégrité et authenticité des **exécutables** par cryptographie, inaltérables même par root/accès physique. *Ex. : dm-verity.*
- **3.2.2** Intégrité de l'**image noyau en mémoire**. *Ex. : LSM Lockdown.*
- **3.2.3** Code chargé en espace noyau contrôlé cryptographiquement. *Ex. : signature des modules noyau.*

**3.3 Chiffrement des données**
- **3.3.1** **Toutes** les données (socle + domaines) protégées en confidentialité, intégrité, authenticité. *Ex. : cryptsetup en mode authentifié (dm-crypt + dm-integrity).*
- **3.3.2** Données non chiffrables (ex. partition ESP) : au moins intégrité + authenticité, et **ni données sensibles ni secrets**.
- **3.3.3** **Composant de sécurité physique** pour protéger les secrets sensibles. *Ex. : TPM scellant la clé de partition et générant une clé VPN non extractible.*
- **3.3.4** Données d'un domaine utilisateur chiffrées à partir d'un **facteur de connaissance** de l'utilisateur légitime (combinable) ; seul lui peut déchiffrer (hors séquestre).
- **3.3.5** Algorithmes et clés conformes au **RGS**.

**3.4 Protection de la mémoire vive**
- **3.4.1** Accès à la mémoire des domaines utilisateurs depuis l'espace utilisateur du socle **restreint** (même privilégié). *Ex. : LSM Lockdown, YAMA.*
- **3.4.2** **Chiffrement complet de la DRAM** contre le cold boot. *Ex. : Intel TME, AMD TSME.*

**3.5 Durcissement du socle**
- **3.5.1** Durcissement à l'état de l'art : **défense en profondeur, séparation des privilèges, moindre privilège, minimisation**.
- **3.5.2** Secrets (clés privées, mots de passe) en mémoire **pas plus longtemps que nécessaire**.
- **3.5.3** Respect du guide **cloisonnement système (PG-040)** ; accès contrôlés par un **moniteur de référence** du socle. *Ex. : MAC SELinux/AppArmor.*
- **3.5.4** **Activer toutes les fonctions de sécurité** du matériel, de l'OS et des logiciels ; toute non-activation **justifiée**.
- **3.5.5** **Noyau durci**. *Ex. : options de compilation, patch linux-hardened.*
- **3.5.6** Protection contre les attaques **micro-architecturales** (Meltdown, Spectre) : une attaque depuis un domaine n'affecte ni socle, ni supports, ni autres domaines. *Ex. : atténuations CPU en ligne de commande noyau.*

**3.6 Périphériques émulés et VMM**
- **3.6.1** **Une instance de VMM par domaine utilisateur**.
- **3.6.2** Chaque périphérique émulé **dédié à un seul** domaine utilisateur.
- **3.6.3** VMM et périphériques émulés isolés dans un **domaine support dédié** ; un périphérique émulé dans un processus distinct a son propre domaine support. *Ex. : chaque QEMU isolé (sandbox, MAC, privilèges réduits) ; virtiofsd isolé à part.*
- **3.6.4** **Surface d'attaque minimale** : seuls les périphériques émulés strictement nécessaires.

**3.7 Périphériques physiques délégués**
- **3.7.1** Préférer l'**émulation** au PCI passthrough ; si délégation, sécurisée, innocuité **démontrée et documentée**. *Ex. : IOMMU, VFIO.*

**3.8 Périphériques physiques externes**
- **3.8.1** Pas d'accès **simultané** par plusieurs domaines ou par un domaine et le socle.
- **3.8.2** Usage **alterné** : démontrer et documenter l'absence de fuite.
- **3.8.3** Données écrites sur un support amovible depuis un domaine **lisibles seulement depuis ce domaine** (la lecture depuis d'autres postes équivalents relève de la PSSI).
- **3.8.4** Démontrer et documenter que les supports amovibles **ne rompent pas l'isolation**.

**3.9 Réseau** *(les flux des domaines supports sont assimilés à ceux du socle)*
- **3.9.1** Configuration réseau du socle **non contrôlable** par un domaine ni par l'utilisateur (exceptions : choix Wi-Fi, IP statique, profil prédéfini par l'admin — sans impact sécurité).
- **3.9.2** Flux gérés selon les **exigences réglementaires de chaque domaine** ; tunnels VPN chiffrants dédiés au besoin ; tenir compte de la sensibilité du socle (4.1).
- **3.9.3** Flux du socle dans un **VPN chiffrant non débrayable** maîtrisé par l'entité (guide nomadisme ; portails captifs traités dans ce guide).
- **3.9.4** Auto-configuration réseau : **options minimales**, sans impact sécurité. *Ex. : options DHCP choisies et évaluées.*
- **3.9.5** Communications réseau domaines utilisateurs ↔ socle **interdites** sauf strict besoin des fonctions de sécurité.
- **3.9.6** Communications réseau **entre domaines utilisateurs** interdites dans le poste ; ne pas les mettre dans le **même domaine de broadcast**.
- **3.9.7** Pas d'**usurpation** d'un autre domaine ou du socle sur les réseaux virtuels.
- **3.9.8** Accès réseau des domaines **uniquement via des ressources maîtrisées par le socle** (exception : carte réseau en passthrough → 3.7 s'applique, le reste de 3.9 non).
- **3.9.9** Pas d'usurpation d'une autre machine, du socle ou d'un domaine **sur les réseaux extérieurs**.
- **3.9.10** **Tous les flux filtrés** par le socle, seuls les flux strictement nécessaires acceptés : vers le socle, depuis le socle, depuis les domaines, et dans les tunnels VPN.

**3.10 Sources de temps**
- **3.10.1** Source de temps **intègre**. *Ex. : NTS (RFC 8915).*
- **3.10.2** Socle et domaines supports sur une **source de temps commune** (corrélation des événements).

**3.11 Journalisation**
- **3.11.1** **Domaine support dédié** à la journalisation du socle ; stocke et transmet aux serveurs distants selon la PSSI.
- **3.11.2** Journaux protégés en **intégrité et authenticité**.
- **3.11.3** Contenu minimal : dysfonctionnements métier ; dysfonctionnements des fonctions de sécurité (distinguables) ; **mises à jour, changements de configuration et d'éléments cryptographiques** ; **authentifications** (locales/distantes, réussies/échouées) et déconnexions ; usages des diodes ; journaux VPN du socle.
- **3.11.4** **Aucune information** permettant de contourner une sécurité dans les journaux. *Ex. : clés privées, adresses cassant l'ASLR.*
- **3.11.5** Journaux internes à un domaine utilisateur **non envoyés au socle** ; export selon la PSSI du domaine.

**3.12 Mise à jour**
- **3.12.1** Socle **fonctionnel et sûr même si la mise à jour échoue** (disponibilité = fonction de sécurité en nomadisme). *Ex. : mise à jour atomique avec fallback.*
- **3.12.2** **Échec de mise à jour journalisé**.
- **3.12.3** Mises à jour **signées**, signatures contrôlées à l'application.

**3.13 Exploitation du socle**
- **3.13.1** **Un rôle par type d'action** : Administrateur (fonctionnel, pas root), Auditeur (lecture journaux/états/versions ; ne remplace pas la centralisation), Mise à jour (branche, rollback ; ne construit ni ne signe — pas sur le poste).
- **3.13.2** Chaque rôle **documenté**, actions listées **exhaustivement**.
- **3.13.3** Actions d'exploitation dans des **domaines supports dédiés à chaque rôle**.
- **3.13.4** Ces domaines à **privilèges minimaux**. *Ex. : capabilities restreintes, MAC, polkit.*
- **3.13.5** Ces domaines **sans accès aux données utilisateurs**.
- **3.13.6** Rôles d'administration conformes au guide **administration sécurisée (PA-022)**.
- **3.13.7** Accès à ces domaines par **authentification forte** (guide PG-078). *Si l'exploitation est automatisée, ne pas exposer ces interfaces.*

**3.14 Chaîne de démarrage des domaines utilisateurs**
- **3.14.1** **Démarrage sécurisé** fourni aux domaines (au sens 3.1).
- **3.14.2** Élément de sécurité **RTM par domaine**. *Ex. : vTPM.*
- **3.14.3** Chaque élément cloisonné dans un domaine support dédié, assigné à **un seul** domaine, distinct de celui du socle.

**3.15 Authentification de l'utilisateur**
- **3.15.1** Authentification **sur le socle obligatoire** avant tout accès aux domaines ou au socle.
- **3.15.2** Authentification conforme à la PSSI et aux exigences de **chacun** des domaines.

**3.16 Affichage de confiance**
- **3.16.1** L'utilisateur sait **à tout moment, sans ambiguïté**, avec quel domaine il interagit. *Ex. : barre de confiance.*

**3.17 Options à la main de l'utilisateur** *(mot de passe, Wi-Fi, association d'un périphérique)*
- **3.17.1** Sans impact sur la sécurité du socle ni le cloisonnement.
- **3.17.2** Configuration via un ou plusieurs **domaines supports dédiés**.

**3.18 Communication entre domaines utilisateurs** *(proscrite ; diodes optionnelles si échange de fichiers autorisé ; alternative : passerelle d'échange dans le SI)*
- **3.18.1** **Seuls des dossiers et fichiers** transitent.
- **3.18.2** Diodes **unidirectionnelles**, dédiées à un couple de domaines identifiés.
- **3.18.3** Fichiers à exporter désignés par **action explicite** de l'utilisateur dans le domaine source.
- **3.18.4** Transfert **accepté** par l'utilisateur via une IHM cloisonnée dans un domaine support.
- **3.18.5** Chaque transfert **journalisé** : nom, **hash**, horodatage, sens, raison du refus.
- **3.18.6** Traitements d'innocuité possibles (recherche de motifs, antivirus) ; décision selon PSSI.
- **3.18.7** Outils d'analyse cloisonnés, **non privilégiés**, une instance **par diode**. *Les diodes ne doivent pas devenir un canal non surveillé.*

**4 Recommandations non fonctionnelles**
- **4.1.1** Le socle est au moins aussi sensible que le **plus sensible** des domaines.
- **4.2.1** **Documentation technique** détaillée : architecture justifiée, surface d'attaque, modèle d'attaquant, risques analysés exhaustivement (ex. docs CLIP OS).
- **4.2.2** **SBOM** de tous les composants et versions, tenue à jour, livrée avec chaque mise à jour.
- **4.3.1** **Procédure d'effacement sécurisé** (décommissionnement/recyclage ; guide PA-097).
- **4.4.1** Conception **testable** par un évaluateur, y compris la défense en profondeur.
- **4.5.1** **Défense en profondeur** dès la conception.
- **4.6.1** Conception prenant en compte le cycle de vie et le **MCO/MCS**.
- **4.6.2** **Délai de mise à disposition d'un correctif** spécifié dès la conception.
- **4.6.3** Le processus de mise à jour garantit **aucune vulnérabilité publique** restante sur socle et domaines supports.

**Total : 78** (69 fonctions de sécurité au chap. 3 + 9 recommandations non fonctionnelles au chap. 4).

## Chiffres et seuils à retenir

- Niveau maximal traité : **Diffusion Restreinte** (II 901) ; combinaisons **NP/NP, NP/DR, DR/DR** ; nombre de domaines non limité.
- **1** VM par domaine utilisateur ; **1** VMM et **1** élément RTM (vTPM) **par** domaine ; **1** domaine d'analyse **par** diode.
- **3** rôles d'exploitation types (Administrateur, Auditeur, Mise à jour).
- **5** métadonnées de journal de transfert (nom, hash, horodatage, sens, raison du refus).
- Aucun seuil temporel chiffré (le délai de correctif est à **spécifier** par l'éditeur, 4.6.2).
- Références : RGS, II 901, IGI 1300, guides PA-022 (administration), PA-054 (nomadisme), PA-097 (reconditionnement), PG-040 (cloisonnement système), PG-078 (authentification) ; NTS RFC 8915 ; ISO/IEC 11889 (TPM).

## Application à PLÉIADE

Lecture générale : ce document vise un **produit poste** (éditeurs), pas PLÉIADE. Il est néanmoins utile sur **deux points** : (1) les **postes Windows des animateurs**, qui jonglent entre réseaux de natures différentes (le document rappelle que la bonne réponse de base est **un poste par environnement**) ; (2) le **serveur PLÉIADE** lui-même, qui est un « socle » faisant cohabiter plusieurs zones — les principes (isolation, réseau contrôlé, journalisation, mise à jour signée, exploitation par rôles) se **transposent**, avec la réserve majeure que les conteneurs partagent le noyau (§2.3).

| Réf. | Statut | Ce que ça implique pour PLÉIADE | À vérifier |
|---|---|---|---|
| Préambule (cloisonnement physique) | **Applicable (important)** | Un poste animateur ne doit pas être branché alternativement sur un réseau d'entreprise sensible et sur le réseau d'exercice/Internet sans solution de cloisonnement. Règle par défaut : **poste dédié à l'exercice**. | À vérifier : les postes animateurs utilisés pour PLÉIADE sont-ils dédiés, ou servent-ils aussi sur un autre réseau ? |
| 2.3 (même sensibilité ≠ même droit) | **Applicable** | Deux zones d'exercice de même niveau doivent rester **isolées** l'une de l'autre (réseaux Docker, bases, clés, realms). | À vérifier : aucune ressource (BDD, volume, réseau, secret) n'est partagée entre deux zones. |
| 2.3 (VM > sandbox) | **Partiellement** | Les conteneurs Docker/Podman sont des **sandbox** au sens du document (noyau partagé) : isolation **plus faible** qu'une VM. Si deux zones ont des opérateurs ou exigences différents, envisager une **VM par zone** sur l'hôte. | À vérifier : la décision « conteneurs sur un même noyau pour plusieurs zones » est-elle documentée et assumée dans l'analyse de risques ? |
| 3.1.1 / 3.2.x | **Partiellement** | Sur le serveur : Secure Boot activé, noyau à jour, modules signés si possible. Sur les postes Windows : Secure Boot + BitLocker avec TPM. | À vérifier : Secure Boot actif sur le serveur et les postes ; BitLocker actif sur les postes animateurs. |
| 3.1.2 | **Applicable** | Mot de passe firmware (BIOS/UEFI) sur le serveur et les postes/tablettes. | À vérifier : accès UEFI protégé par mot de passe unique par machine. |
| 3.3.1 / 3.3.3 | **Applicable** | Chiffrement du disque serveur (volumes MariaDB, clés de la CA de zone) et des **tablettes LEAC** (données terrain hors ligne, perte/vol possible). | À vérifier : chiffrement disque actif sur le serveur et sur chaque tablette LEAC ; la clé privée de la CA de zone n'est pas stockée en clair. |
| 3.3.4 | **Applicable (LEAC)** | Les données locales LEAC doivent être protégées par un secret de l'utilisateur (code de déverrouillage de la tablette au minimum). | À vérifier : une tablette LEAC volée ne livre pas ses données sans code. |
| 3.3.5 | **Applicable** | Algorithmes conformes RGS pour TLS (Traefik), PKI de zone, VPN. | À vérifier : tailles de clés et algorithmes de la CA de zone et de Traefik conformes (voir REF crypto ANSSI). |
| 3.5.1 / 3.5.4 | **Applicable** | Hôte et conteneurs **minimaux** ; moindre privilège (conteneurs non root, pas de `--privileged`, capabilities réduites) ; toute fonction de sécurité désactivée **justifiée**. | À vérifier : aucun conteneur n'est lancé en `privileged` ni en root sans justification ; le socket Docker n'est monté dans aucun conteneur applicatif (sauf Traefik, à justifier). |
| 3.5.2 | **Applicable** | Secrets (X-API-Key, mots de passe BDD, secrets OIDC) non persistés en clair plus que nécessaire (pas dans les logs, ni dans le dépôt). | À vérifier : aucun secret dans les dépôts GitHub `cecpc-pleiade` (scan de secrets) ni dans les journaux applicatifs. |
| 3.5.3 | **Applicable** | Moniteur de référence MAC sur l'hôte : SELinux (Podman) ou AppArmor (Docker) actif. | À vérifier : SELinux/AppArmor en mode « enforcing » sur le serveur. |
| 3.6 / 3.7 / 3.14 / 3.16 / 3.18 | **Hors champ** | Spécifique à un poste à VM (VMM, vTPM, barre de confiance, diodes). Seule idée transposable : en cas d'échange de fichiers entre zones ou vers l'extérieur, **journaliser** nom + hash + horodatage + sens. | À vérifier (si échange de fichiers inter-zones) : chaque transfert est-il tracé avec un hash ? |
| 3.8.x | **Partiellement** | Postes animateurs et tablettes : maîtriser les **clés USB** (une clé ayant servi sur un autre réseau ne doit pas servir sur le réseau d'exercice sans contrôle). | À vérifier : politique USB écrite pour les postes animateurs et tablettes. |
| 3.9.1 | **Applicable** | Sur les postes/tablettes gérés, l'utilisateur ne doit pas pouvoir modifier la configuration réseau de sécurité (VPN, pare-feu). | À vérifier : les animateurs ne peuvent pas désactiver le pare-feu ni modifier le profil VPN. |
| 3.9.3 | **Applicable (important)** | Le VPN Pritunl des postes nomades devrait être **non débrayable** (tout le trafic, pas de split-tunnel non maîtrisé) quand ils accèdent à PLÉIADE depuis des réseaux variés. | À vérifier : configuration Pritunl en tunnel complet ou split-tunnel justifié ; la synchronisation LEAC ne passe **que** par le VPN. |
| 3.9.5 / 3.9.6 / 3.9.10 | **Applicable (transposé à l'hôte)** | Sur le serveur : flux entre zones **interdits**, flux vers l'hôte filtrés, filtrage par défaut « tout refusé » (pare-feu hôte + réseaux Docker séparés, pas de réseau « bridge » commun). | À vérifier : pare-feu hôte en refus par défaut ; seuls 443 (Traefik) et le port VPN exposés ; conteneurs de zones différentes dans des réseaux Docker distincts. |
| 3.9.4 | **Partiellement** | Serveur en IP fixe ; limiter l'auto-configuration. | À vérifier : pas de DHCP non maîtrisé sur le serveur. |
| 3.10.1 / 3.10.2 | **Applicable** | Horloge commune et intègre (NTS si possible) pour le serveur, les conteneurs et les tablettes : indispensable pour corréler les journaux **et** pour la fusion des notations LEAC au retour (horodatage). | À vérifier : serveur synchronisé (chrony/NTS) ; tablettes LEAC à l'heure avant départ terrain. |
| 3.11.1 / 3.11.2 / 3.11.3 | **Applicable** | Centraliser les journaux de l'hôte, de Traefik, de Keycloak (authentifications réussies/échouées), des déploiements (mises à jour, changements de config, rotation de certificats) hors des conteneurs, protégés en intégrité. | À vérifier : journaux d'authentification Keycloak et d'accès Traefik conservés hors conteneur, avec une durée de rétention définie. |
| 3.11.4 | **Applicable** | Ne jamais journaliser de secret (X-API-Key, jeton OIDC, mot de passe). | À vérifier : grep des journaux applicatifs sur `X-API-Key`, `Authorization`, `password` → aucun secret. |
| 3.12.1 / 3.12.2 | **Applicable** | Le déploiement automatique depuis `main`/`prod` doit permettre un **retour arrière** immédiat et ne jamais laisser une zone hors service ; échecs journalisés. | À vérifier : procédure de rollback testée (image précédente étiquetée) ; échec de déploiement visible et tracé (vérifié par `/api/sante`). |
| 3.12.3 | **Partiellement** | Transposition : images de conteneurs **traçables et signées** (ou au minimum épinglées par condensat), commits/tags signés sur les branches de production. | À vérifier : les images déployées sont référencées par digest ; la branche `prod` est protégée (revue obligatoire, pas de push direct). |
| 3.13.1 → 3.13.7 | **Applicable** | Séparer les rôles d'exploitation : **admin** de la plateforme, **auditeur** (lecture journaux/versions), **déploiement** (CI). La construction des images ne se fait pas sur le serveur de production. Accès par authentification forte. | À vérifier : comptes distincts admin / lecture seule / CI ; MFA sur GitHub `cecpc-pleiade` et sur l'accès serveur ; liste écrite des actions autorisées par rôle. |
| 3.15.1 | **Applicable** | Tablettes et postes : authentification locale obligatoire avant usage. | À vérifier : verrouillage par code sur les tablettes LEAC. |
| 3.17 | **Partiellement** | Les options laissées aux animateurs (Wi-Fi, mot de passe) ne doivent pas permettre de casser la sécurité. | À vérifier : un animateur ne peut pas installer de logiciel ni désactiver l'antivirus. |
| 4.1.1 | **Applicable** | Le serveur PLÉIADE est au moins aussi sensible que la **plus sensible** des zones qu'il héberge. | À vérifier : le niveau de sensibilité retenu pour le serveur est celui de la zone la plus sensible. |
| 4.2.1 | **Applicable** | Documenter l'architecture, la surface d'attaque et le modèle d'attaquant de PLÉIADE. | À vérifier : un document d'architecture sécurité existe (dans `PLEIADE\`). |
| 4.2.2 | **Applicable (important)** | **SBOM** par app et par image (dépendances npm, image de base), à jour à chaque déploiement, pour savoir en minutes si une CVE publique touche PLÉIADE. | À vérifier : une SBOM est générée par la CI pour chaque dépôt applicatif. |
| 4.3.1 | **Applicable** | Procédure d'effacement des tablettes LEAC, des postes et des volumes de zone en fin d'exercice. | À vérifier : procédure de purge de zone (BDD, volumes, secrets, certificats) écrite et appliquée à la fermeture. |
| 4.4.1 / 4.5.1 | **Applicable** | Concevoir pour que la sécurité soit **testable** (tests d'intrusion, recette) ; plusieurs barrières. | À vérifier : un test de sécurité de zone est prévu avant chaque exercice. |
| 4.6.1 / 4.6.2 / 4.6.3 | **Applicable** | Fixer un **délai cible** de correction des vulnérabilités ; ne pas laisser de CVE publique connue sur l'hôte et les images. | À vérifier : délai cible écrit (ex. critique < N jours, à fixer) ; scan des images sans CVE critique non traitée. |
| 3.4.x, 3.5.5, 3.5.6 | **Partiellement** | Atténuations CPU et noyau à jour sur l'hôte : pertinentes car plusieurs zones partagent le même matériel. Chiffrement DRAM : selon matériel. | À vérifier : atténuations Spectre/Meltdown actives (`/sys/devices/system/cpu/vulnerabilities/`). |

## Limites / points d'attention

- Document destiné aux **éditeurs** de postes, **pas aux administrateurs** : il ne décrit ni l'infrastructure, ni la PSSI, ni l'exploitation en production.
- Il **exclut explicitement** l'isolation par conteneurs/sandbox entre environnements utilisateurs : il ne valide donc **pas** l'usage de conteneurs pour séparer des zones de sensibilités différentes — il dit l'inverse (les VM cloisonnent mieux).
- Hypothèses fortes : **mono-utilisateur**, nomadisme ; non transposable tel quel à un serveur multi-zones.
- La mention « Diffusion Restreinte » décrit le **plafond** des environnements hébergeables ; elle ne concerne pas PLÉIADE tant que les données d'exercice restent NP. Si une zone devait un jour traiter du DR, ce document deviendrait une **exigence**, pas une inspiration.
- Exemples Linux (dm-verity, LSM Lockdown, SELinux…) donnés à titre illustratif ; ils ne suffisent pas toujours seuls.
- CLIP OS cité comme référence historique, **plus maintenu**.
