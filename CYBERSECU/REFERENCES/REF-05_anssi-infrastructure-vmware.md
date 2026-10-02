# REF-05 — Sécurisation d'une infrastructure VMware — Les fondamentaux

- **Fichier** : `anssi-fondamentaux-securisation_infrastructure_vmware_v1-0.pdf` · **Éditeur / référence** : ANSSI, ANSSI-BP-103 · **Date / version** : v1.0 du 02/04/2024 (version initiale) · **Pages** : 20 · **Marquage** : public (Licence Ouverte Etalab v2.0)
- **Public visé (couverture)** : développeur, administrateur, RSSI, DSI, utilisateur
- **Ingéré** : 2026-10-01

> ℹ Recommandations numérotées **R1 à R50** dans le document (numérotation d'origine conservée). NB : les liens de documentation éditeur pointent vers techdocs.broadcom.com (vSphere 8.0 et 9.0).

## En une phrase

L'hyperviseur concentre toutes les données et traitements : c'est une **cible privilégiée** (étatique et rançongiciel) qu'il faut traiter comme une **infrastructure critique** — séparer plan de contrôle et plan de données, cloisonner l'administration du socle de celle des VM et par zone de confiance, durcir les hôtes, superviser et sauvegarder.

## Ce que dit le document

### 1. Préambule
- La virtualisation est le sous-jacent du cloud (compute, network, storage). Compromettre l'hyperviseur = accès à **tout** ce qu'il héberge → considérer les menaces **étatique** (espionnage, déstabilisation) et **cybercriminelle** (lucrative, destruction).
- Recommandations à adapter au contexte, au service porté et à sa criticité ; ni exhaustif ni détaillé.

### 2. Principes généraux
- **Architecture (§2.1)** : le socle de virtualisation doit être **indépendant des VM** qu'il héberge. Séparation **plan de contrôle** (pilotage) / **plan de données** (VM) = première mesure. Terminologie VMware : *Management domain* (cluster d'administration) / *Workload domain* (cluster de production).
- **Privilèges (§2.2)** : rôles vSphere = ensembles de privilèges ; politique d'accès = utilisateur + rôle + objet (VM, datastore, vSwitch, port group).
- **Cloisonnement réseau (§2.3)** : vSwitch/dvSwitch (niveau 2 ; dvSwitch : gestion centralisée, PVLAN, capture), vNic ; adaptateurs **VMkernel** (IP, trafic vers ESXi, vCenter, NSX, stockage, sauvegarde, supervision). La segmentation facile permet d'isoler les VM selon usage, exposition, sensibilité.
- **Micro-segmentation (§2.4)** : filtrage granulaire et cumulable par VM/groupe, géré centralement, **indépendant de l'OS invité**. Limite la **latéralisation**, les flux **nord-sud** (vers l'extérieur de la zone) et **est-ouest** (internes à la zone), filtrage plus précis (tags). **Un agent dans la VM est moins sûr qu'un filtrage au niveau hyperviseur** (modules noyau, openvswitch). NSX (sous licence) : NSX Manager, NSX Controllers (plan de contrôle), module noyau ESXi (pare-feu par interface virtuelle), NSX Edges (remplaçables par des pare-feux physiques pour mieux cloisonner). Mesure de défense en profondeur, **insuffisante seule**.
- **Vecteurs d'attaque (§2.5)** — rançongiciel fréquent : compromission bureautique → latéralisation ; compromission d'un **sous-traitant** ; vulnérabilité de l'hyperviseur ; **binaires compromis** ; **absence de MCS** ; absence de sécurisation ; **implant sur le stockage** ; **hyperviseurs exposés sur Internet**.

### 3. Architecture de référence (figures 1 et 2)
Zone Admin – socle VMware (vCenter par zone, vCenter d'admin, bastion SSH de secours) ; zone Admin – VM métier (VM de rebond par zone) ; workload domains par zone ; VLAN distincts : prod par zone, utilisateur, admin métier, admin VMware, admin VMware SSH, **superadmin** VMware, **vMotion par zone**, admin iDRAC par zone, superadmin iDRAC ; pare-feux d'administration. Code couleur : violet = admin hyperviseurs, rouge = admin métier des VM, jaune = iDRAC, vert = vMotion, bleu = flux autorisés.

## Toutes les recommandations

**3.1 Générales**
- **R1** Appliquer **au plus vite** les mises à jour de sécurité du socle.
- **R2** S'abonner aux **bulletins de sécurité** de toutes les briques logicielles et matérielles.

**3.2 Architecture**
- **R3** Séparer les flux : **plan de contrôle** (vCenter admin et workload, NSX Manager/Controller, interfaces d'admin ESXi) / **plan de données** (services, stockage métier). *Le port d'administration d'une VM ne doit pas être mutualisé avec le plan de contrôle du socle.*
- **R4** Port d'administration d'une VM cloisonné du plan de contrôle du socle, **au minimum par un VLAN dédié**.
- **R5** Flux **administration, stockage, sauvegarde** cloisonnés entre eux (VLAN et adaptateurs VMkernel dédiés).
- **R6** Flux d'administration sur un **port réseau physique dédié**.
- **R7** **Cluster dédié à l'administration** (Management domain), séparé de la production, hébergeant les vCenter (production et admin). *Peut servir de SI d'administration (guide PA-022).*
- **R8** Clusters/serveurs de production **dédiés par zone de sensibilité ou de confiance**.
- **R9** Chaque zone gérée par un **vCenter dédié**, hébergé dans la zone d'administration.
- **R10** Dans le cluster d'admin, **segmentation VLAN** isolant les plans de contrôle de chaque environnement de production.
- **R11** SI d'admin complexe : un cluster ESXi *management domain* + un *workload domain* pour les outils d'administration.
- **R12** Zones de confiance définies selon la **sensibilité des ressources** (valeur métier).
- **R13** Administration des **hyperviseurs** cloisonnée de l'administration **métier des VM**.
- **R14** Par zone : un **vCenter** pour l'administration du socle et un **système de rebond** pour l'administration des VM métier.
- **R15** Administration des **cartes de contrôle à distance** (iDRAC, iLO) cloisonnée du reste.
- **R16** Flux **vMotion** cloisonnés **par zone** de confiance.
- **R17** Créer les **règles de filtrage** correspondant aux flux autorisés (figure 2 ; liste des ports VMware).
- **R18** Le socle VMware est une **infrastructure critique** : protections adéquates, intégré au **SI d'administration**.
- **R19** Tout le matériel lié (iLO/iDRAC, baies de stockage…) administré de façon sécurisée.
- **R20** **Interface réseau dédiée** à l'administration ESXi (SSH, flux vCenter), connectée au réseau d'administration, **jamais accessible depuis un réseau de production**.
- **R21** **Annuaire d'administration indépendant** des annuaires de production (ex. AD) ; vérifier régulièrement les **chemins de contrôle** (pas d'élévation de privilège dans un sens ou l'autre ; guide BP-099).
- **R22** Clusters ESXi et datastores **dédiés par niveau de sensibilité** des applications/données.
- **R23** **Vérification régulière des configurations** ESXi par comparaison à la configuration de déploiement (host profiles ou export via API).
- **R24** Segmentation **PVLAN** des VM quand c'est possible.
- **R25** **Synchronisation horaire** des VM configurée avec vigilance (ex. contrôleurs AD : ne pas prendre l'hyperviseur comme source — désynchronisation au redémarrage ou au snapshot).
- **R26** **Proxy dédié** au SI d'administration pour les mises à jour Internet, filtrant les URL VMware **par liste d'autorisation**.

**3.3 Actions d'administration** *(deux modèles : équipe dédiée ou mutualisée)*
- **R27** Politique **RBAC** des comptes d'administration cohérente avec le modèle de délégation (taille de l'équipe).
- **R28** **Moindre privilège** pour tous les comptes d'administration et **comptes de service** (ex. supervision).
- **R29** **MFA** pour les administrateurs sur vSphere/vCenter (guide PG-078).
- **R30** **Comptes dédiés** aux actions d'administration automatisées via API.
- **R31** **Superviser les connexions aux API** pour identifier les sources légitimes (ex. orchestrateurs).
- **R32** Tous les composants dans le **MCS** (ESXi, vmware-tools, vCenter, outils VMware et tiers).
- **R33** Outils additionnels limités au **strict besoin** ; désinstaller ceux inutilisés.

**3.4 Durcissement des ESXi**
- **R34** **Désactiver SSH** sur les ESXi ; activer le **lockdown mode « normal »** avec un **compte bris de glace**.
- **R35** **Secure Boot** systématique ; **signature des VIB** systématiquement vérifiée.
- **R36** Appliquer le guide **TLS** de l'ANSSI (PA-035) aux accès HTTPS vSphere (Web, API) — **TLS 1.2 minimum**.
- **R37** **TLS systématique pour vMotion**.
- **R38** **Tagging VLAN au niveau de l'hyperviseur**, jamais dans la VM.
- **R39** **Pare-feu local** des ESXi configuré.
- **R40** Accès aux interfaces d'administration des VM **impérativement séparé** de celui du socle.

**3.5 Supervision de sécurité**
- **R41** Archiver et superviser : accès aux hôtes (`auth.log`) ; modifications de config ESXi et VM ; redémarrages ESXi ; connexions vSphere/vCenter ; **trafic des interfaces** (une interface d'admin doit avoir un trafic faible — trafic élevé = exfiltration possible) ; **suspension de VM** (dump mémoire ?) ; **arrêt massif de VM** (chiffrement des vmdk ?) ; usage des comptes techniques internes **vpx-user** et **dcui** (root) ; historique `shell.log` ; *guest operations* ; upload/download sur les datastores.

**3.6 Micro-segmentation (NSX)**
- **R42** NSX Manager et Controllers sur le **cluster d'administration uniquement**, jamais en production.
- **R43** Sécuriser l'accès à NSX Manager/Controller, limiter leurs usages, **moindre privilège** (la micro-segmentation repose sur leur non-compromission).
- **R44** Règles de filtrage **jamais fondées sur un critère modifiable par la VM** (hostname, adresse MAC).
- **R45** **Tout flux non explicitement autorisé est bloqué**.
- **R46** Règles **génériques** en complément de règles spécifiques (maintenabilité).
- **R47** Isoler les zones de sensibilités différentes par des **pare-feux physiques**.
- **R48** Infrastructures dynamiques : **pare-feux physiques pour le nord-sud** (IP/ports) + **micro-segmentation pour l'est-ouest** (IP, ports, type de VM, tag, OS, filtrage TLS, horaire…).

**3.7 Sauvegarde**
- **R49** Sauvegarder l'infrastructure de virtualisation : au moins les **binaires** pour réinstaller une infra minimale (OS, logiciels, correctifs, firmware), les procédures d'import des configurations ou les **scripts de configuration** ; **tester régulièrement** la restauration des VM.
- **R50** Sauvegarder les environnements hébergés selon *Les Fondamentaux — Sauvegarde des SI* (BP-100).

**Total : 50 recommandations** (R1–R50).

## Chiffres et seuils à retenir

- **TLS 1.2 minimum** pour les accès HTTPS vSphere (R36) ; TLS **obligatoire** pour vMotion (R37).
- **8** vecteurs d'attaque recensés (§2.5) ; **11** catégories d'événements à superviser (R41).
- Lockdown mode **« normal »** + **1** compte bris de glace (R34).
- **1** vCenter par zone de confiance (R9, R14) ; VLAN admin **au minimum** pour isoler le port d'admin des VM (R4).
- Pas d'autre seuil chiffré (délais de patch : « au plus vite », R1).
- Références : guides ANSSI BP-099 (AD), BP-100 (sauvegarde), PA-035 (TLS), PA-022 (administration), PG-078 (MFA) ; guide de durcissement VMware.

## Application à PLÉIADE

Lecture générale : **PLÉIADE n'utilise pas VMware à notre connaissance** (serveur Linux + conteneurs Docker/Podman). Le document reste pertinent par **transposition** : l'**hôte de conteneurs** joue le rôle de l'hyperviseur (le compromettre = accéder à toutes les zones), le **démon Docker/Podman et son socket** jouent le rôle du vCenter (plan de contrôle), les **zones d'exercice** jouent le rôle des zones de confiance, **Traefik** est le point nord-sud et les **réseaux Docker** portent l'est-ouest. Si le serveur PLÉIADE est lui-même une **VM** chez un hébergeur ou sur un hyperviseur du CECPC, tout le document s'applique **à l'hébergeur** — à vérifier.

| Réf. | Statut | Ce que ça implique pour PLÉIADE | À vérifier |
|---|---|---|---|
| Préambule / §2.5 | **Applicable** | L'hôte PLÉIADE concentre toutes les zones : cible de choix pour un rançongiciel. | À vérifier : le serveur PLÉIADE est-il une machine physique ou une VM ? Si VM, qui administre l'hyperviseur et selon quelles règles ? |
| R1 / R2 / R32 | **Applicable (important)** | Patcher au plus vite l'OS hôte, le moteur de conteneurs, Traefik, Keycloak, MariaDB, Pritunl, Node.js et les images de base ; s'abonner aux bulletins (CERT-FR, éditeurs, GitHub Security Advisories / Dependabot sur `cecpc-pleiade`). | À vérifier : alertes Dependabot actives sur les 12 dépôts ; date du dernier patch de l'hôte ; abonnement CERT-FR. |
| R3 / §2.1 | **Applicable (transposé)** | Séparer **plan de contrôle** (socket Docker/Podman, Keycloak admin, Traefik dashboard, app-admin, SSH) et **plan de données** (apps joueurs). | À vérifier : le tableau de bord Traefik et la console admin Keycloak ne sont pas exposés sur le point d'entrée joueurs. |
| R4 / R13 / R14 / R40 | **Applicable (transposé)** | L'**administration de l'hôte** (SSH, moteur de conteneurs) doit être cloisonnée de l'**administration fonctionnelle des apps** (app-admin, comptes admin dans les apps). Un admin de zone ne doit pas devenir admin de l'hôte. | À vérifier : les comptes « admin de zone » (app-admin, eho) n'ont aucun accès SSH ni au socket Docker. |
| R5 | **Partiellement** | Séparer les flux admin / sauvegarde / applicatifs (au moins par réseaux Docker distincts et pare-feu hôte). | À vérifier : le flux de sauvegarde des bases ne transite pas par le réseau exposé aux joueurs. |
| R6 / R20 | **Partiellement** | Idéalement, une interface (ou au moins un VPN) **dédiée à l'administration**, jamais joignable depuis le réseau des joueurs. | À vérifier : SSH n'écoute que sur l'interface VPN d'administration (ou est filtré par IP), pas sur l'interface publique. |
| R7 / R11 / R18 | **Applicable** | Considérer le serveur PLÉIADE et son CI/CD comme **infrastructure critique**, intégrée à un **SI d'administration** (postes d'admin maîtrisés, VPN admin). | À vérifier : liste des postes autorisés à administrer PLÉIADE ; ces postes sont-ils maîtrisés ? |
| R8 / R12 / R22 | **Applicable** | Zones dédiées par sensibilité : ne pas mettre sur le même hôte une zone d'exercice ouverte et des données sensibles réelles ; volumes et bases **par zone**. | À vérifier : volumes et bases MariaDB **séparés par zone** ; critère écrit de « zone de confiance ». |
| R9 / R10 | **Partiellement** | Un plan de contrôle par zone (realm Keycloak, secrets, réseau) plutôt qu'un plan unique partagé. | À vérifier : chaque zone a son realm/client Keycloak et ses propres secrets (X-API-Key non réutilisées entre zones). |
| R15 / R19 | **Applicable** | Carte de contrôle à distance du serveur (iDRAC/iLO/IPMI) : réseau isolé, mot de passe changé, firmware à jour, jamais exposée. | À vérifier : la carte BMC du serveur est-elle sur un réseau isolé avec mot de passe non par défaut ? |
| R16 / R37 | **Hors champ** | Pas de vMotion. Transposition : toute **migration/copie** de volumes ou de bases entre machines se fait chiffrée. | À vérifier : copies de sauvegarde transférées via canal chiffré (SSH/TLS). |
| R17 / R45 | **Applicable (important)** | **Matrice de flux** explicite et pare-feu en **refus par défaut** : entrée 443 (Traefik) + port VPN ; inter-conteneurs uniquement les appels nécessaires (app → eho, app → Keycloak, app → sa base). | À vérifier : pare-feu hôte (nftables/firewalld) en politique « drop » par défaut ; matrice des flux documentée et conforme. |
| R21 | **Applicable (important)** | L'**annuaire d'administration** de la plateforme (accès serveur, GitHub, admin Keycloak master) doit être **indépendant** de l'annuaire de zone (Keycloak realms joueurs / eho). Aucun chemin d'élévation : un compte gc01 compromis ne doit jamais mener à l'admin plateforme. | À vérifier : les admins plateforme sont dans le realm `master` (ou un IdP séparé), pas dans les realms de zone ; aucun rôle de zone ne donne de droit sur `master`. |
| R23 | **Applicable** | Vérifier régulièrement la conformité de la configuration à l'état de déploiement (infrastructure as code : comparer le serveur aux fichiers `pleiade-infra` / `pleiade-platform`). | À vérifier : un contrôle de dérive (diff config déployée ↔ dépôt) est fait avant chaque exercice. |
| R24 / R38 / R44 | **Applicable (transposé)** | La segmentation se décide **au niveau de l'hôte** (réseaux Docker, pare-feu), jamais dans le conteneur ; ne jamais filtrer sur un critère que le conteneur contrôle (nom d'hôte, en-tête `Host`/`X-Forwarded-For` non validé). | À vérifier : les contrôles d'accès par IP dans Traefik/apps ne reposent pas sur un `X-Forwarded-For` falsifiable ; les conteneurs n'ont pas `NET_ADMIN`. |
| R25 | **Applicable** | Synchronisation horaire de l'hôte maîtrisée (NTP/NTS) ; conteneurs héritant de l'hôte. Crucial pour la validité des jetons OIDC (expiration) et l'horodatage LEAC. | À vérifier : décalage horaire hôte < quelques secondes ; jetons Keycloak non rejetés pour cause d'horloge. |
| R26 | **Partiellement** | Les téléchargements de mises à jour/images par l'hôte devraient passer par un proxy ou un registre **en liste d'autorisation** (registres d'images et dépôts de paquets connus). | À vérifier : l'hôte peut-il sortir librement vers Internet ? Liste des registres d'images autorisés. |
| R27 / R28 | **Applicable** | RBAC proportionné à une petite équipe ; moindre privilège pour les **comptes de service** (clés X-API-Key à portée limitée par app et par zone ; utilisateur MariaDB par app avec droits sur sa seule base). | À vérifier : chaque app a son propre utilisateur MariaDB limité à sa base ; chaque X-API-Key n'ouvre que les routes nécessaires. |
| R29 | **Applicable (important)** | **MFA obligatoire** pour les administrateurs : console Keycloak, GitHub `cecpc-pleiade`, accès serveur (clé SSH + passphrase/token), Pritunl. | À vérifier : MFA imposée au niveau de l'organisation GitHub ; OTP/WebAuthn requis sur le realm `master` Keycloak. |
| R30 / R31 | **Applicable** | **Comptes dédiés** à l'automatisation (déploiement depuis `main`/`prod` = jeton CI dédié, pas un compte personnel) ; superviser d'où viennent les appels API (CI, apps). | À vérifier : le déploiement automatique utilise un compte/clé de déploiement dédié à portée minimale ; les appels X-API-Key sont journalisés avec l'app appelante. |
| R33 | **Applicable** | Retirer de l'hôte et des images les outils non nécessaires (images minimales, pas d'outils de debug en production). | À vérifier : liste des paquets/services actifs sur l'hôte justifiée ; images basées sur des bases minimales. |
| R34 | **Applicable (transposé)** | SSH : désactiver l'accès root et par mot de passe, clés uniquement, accès limité au VPN admin ; prévoir un **accès bris de glace** documenté (console). | À vérifier : `PermitRootLogin no`, `PasswordAuthentication no` ; procédure bris de glace écrite et testée. |
| R35 | **Applicable (transposé)** | Secure Boot sur le serveur ; vérifier l'**authenticité des binaires** et images (signatures de paquets, images officielles épinglées par digest). | À vérifier : Secure Boot actif ; images tierces (Keycloak, MariaDB, Traefik) épinglées par digest depuis des sources officielles. |
| R36 | **Applicable (important)** | Appliquer le guide TLS ANSSI à **Traefik** et aux interfaces d'admin : **TLS 1.2 minimum** (1.3 privilégié), suites robustes, CA de zone correctement gérée. | À vérifier : `minVersion: VersionTLS12` (ou 1.3) dans les options TLS de Traefik ; test externe des suites acceptées. |
| R39 | **Applicable** | **Pare-feu local de l'hôte** configuré (attention : Docker contourne souvent les règles UFW/iptables standards via ses propres chaînes). | À vérifier : un port publié par erreur par un conteneur (`-p 3306:3306`) est-il bloqué ? Test de scan externe. |
| R41 | **Applicable (transposé)** | Superviser : connexions SSH (`auth.log`), changements de configuration/déploiements, redémarrages, connexions admin Keycloak, **volume de trafic** des interfaces d'admin, **arrêt massif de conteneurs**, **suppression/chiffrement massif de volumes**, usage de root, historique shell, `docker exec` dans les conteneurs, téléversements vers app-webserver. | À vérifier : ces événements sont collectés hors de l'hôte et une alerte existe au moins sur l'arrêt massif de conteneurs et les échecs d'authentification admin. |
| R42 / R43 | **Applicable (transposé)** | Le **socket Docker/Podman** et l'API Traefik = équivalent NSX Manager : accès restreint, jamais monté dans une app de zone, moindre privilège. | À vérifier : seul Traefik (en lecture seule, ou via un proxy de socket) accède au socket ; aucune app Next.js n'y a accès. |
| R46 | **Applicable** | Règles génériques (refus inter-zones) + règles spécifiques (app → eho). | À vérifier : la configuration réseau est générée par l'orchestrateur et lisible. |
| R47 / R48 | **Partiellement** | Nord-sud : pare-feu devant le serveur (réseau CECPC / hébergeur) + Traefik ; est-ouest : réseaux Docker par zone. Pour des zones de sensibilités **différentes**, le document demande des pare-feux **physiques** → hôtes distincts. | À vérifier : existe-t-il un pare-feu réseau en amont du serveur ? Des zones de sensibilités différentes partagent-elles le même hôte ? |
| R49 | **Applicable (important)** | Pouvoir **reconstruire** la plateforme : dépôts GitHub (faisant foi), scripts `dev\` et `pleiade-infra`, images versionnées, sauvegarde de la CA de zone (clé hors ligne), configuration Keycloak exportée ; **tester la restauration**. | À vérifier : une restauration complète d'une zone sur une machine vierge a-t-elle été chronométrée ? La clé de la CA est-elle sauvegardée hors du serveur ? |
| R50 | **Applicable** | Sauvegarde des données de zone (MariaDB, volumes, données LEAC concaténées) selon le guide BP-100 : copies hors ligne, chiffrées, testées. | À vérifier : sauvegardes MariaDB automatisées, au moins une copie hors du serveur et hors ligne, test de restauration daté. |
| §2.4 (agent dans la VM moins sûr) | **Applicable (transposé)** | Le filtrage doit être fait par l'hôte, pas par l'app dans le conteneur (qui peut être compromise). | À vérifier : les restrictions réseau ne dépendent pas d'un code applicatif. |

## Limites / points d'attention

- Document **spécifique VMware/vSphere/NSX** : la transposition aux conteneurs est une **interprétation CYBERSECU**, non un avis ANSSI. Les conteneurs partagent le noyau de l'hôte : leur isolation est **plus faible** qu'entre VM (cf. REF-04 §2.3) — les recommandations de cloisonnement par zone sont donc **au moins** aussi nécessaires.
- Recommandations « les plus importantes » seulement ; renvoi au guide de durcissement VMware et à une analyse de risques pour aller plus loin.
- Plusieurs mesures supposent une infrastructure dimensionnée (clusters dédiés, ports physiques dédiés, pare-feux physiques) : pour PLÉIADE (probablement un seul serveur), viser l'**équivalent logique** (VPN admin, réseaux séparés, pare-feu hôte) et **documenter** l'écart.
- Point ouvert majeur : **savoir si le serveur PLÉIADE tourne lui-même sur un hyperviseur** (VMware ou autre) — dans ce cas, R1–R50 s'appliquent pleinement à l'hébergeur.
- Les recommandations AD (R21, R25) sont transposées à Keycloak : la logique (annuaire d'admin indépendant, pas de chemin d'élévation) est identique.
