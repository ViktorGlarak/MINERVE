# REF-01 — Guide d'hygiène informatique — Renforcer la sécurité de son système d'information en 42 mesures

- **Fichier** : `guide_hygiene_informatique_anssi.pdf` (source : `D:\CECPC\PLEIADE\DOC\CYBER SECU\`) · **Éditeur / référence** : ANSSI (Agence nationale de la sécurité des systèmes d'information), référence d'impression `20170901-1756` · **Date / version** : Version 2.0 — septembre 2017 (1re version : janvier 2013) · **Pages** : 72 (pages 2, 61 et 71 blanches) · **Marquage** : public — Licence Ouverte / Open Licence (Etalab V1)
- **Ingéré** : 2026-10-01

> ⚠ Document de **2017** : certaines références techniques ont vieilli (WPA2, SMS comme facteur de possession, renvois aux notes techniques 2012-2016, URL `ssi.gouv.fr` aujourd'hui `cyber.gouv.fr`). Le fond (les 42 mesures) reste le socle de base de l'ANSSI. Voir § « Limites ».

---

## En une phrase

Socle de **42 mesures d'hygiène** réparties en 10 chapitres, chacune notée **« standard »** (à atteindre partout d'abord) et parfois **« renforcé »**, que l'ANSSI estime suffisantes pour éviter « la majeure partie des attaques informatiques ayant requis une intervention de l'agence ».

## Ce que dit le document (synthèse structurée, fidèle)

**Public visé (avant-propos)** : entités publiques ou privées dotées d'une DSI, ou professionnels chargés de leur sécurité. Né du constat que l'application de ces mesures aurait évité la majorité des attaques traitées par l'ANSSI. La v2 intègre nomadisme, séparation des usages, et ajoute les **indicateurs de niveau standard / renforcé**. « La sécurité n'est plus une option. »

**Mode d'emploi (p. 3)** — le guide est une base de **plan d'actions** :
1. Faire un **état des lieux** de chaque règle avec l'**outil de suivi** en annexe (niveau standard atteint ? renforcé ?).
2. À défaut de connaissance de son SI, solliciter un spécialiste pour un diagnostic (renvoi au guide ANSSI-CGPME, mars 2015).
3. Viser **d'abord** les règles dont le niveau **standard** n'est pas atteint. Quand un référentiel ANSSI impose ces mesures, sauf mention contraire, c'est le niveau **standard** qui est exigé.
4. Une fois le standard atteint partout, nouveau plan visant le **renforcé**.

**Les 10 chapitres** : I Sensibiliser et former (1-3) · II Connaître le SI (4-7) · III Authentifier et contrôler les accès (8-13) · IV Sécuriser les postes (14-18) · V Sécuriser le réseau (19-26) · VI Sécuriser l'administration (27-29) · VII Gérer le nomadisme (30-33) · VIII Maintenir le SI à jour (34-35) · IX Superviser, auditer, réagir (36-40) · X Pour aller plus loin (41-42).

**Annexes** : outil de suivi (tableau des 42 mesures, colonnes Standard / Renforcé, p. 60-65) ; bibliographie (guides, notes techniques ANSSI 2010-2016, ressources en ligne : catalogue des qualifications, CERT-FR, CNIL).

---

## Toutes les recommandations / mesures

Légende : **[S]** = niveau standard · **[R]** = niveau renforcé (complément explicitement marqué « renforcé » dans le guide). Les mesures 38, 41, 42 sont **entièrement** de niveau renforcé.

### I — Sensibiliser et former

**Mesure 1 — Former les équipes opérationnelles à la sécurité des systèmes d'information** [S]
Admins réseau/sécu/système, chefs de projet, développeurs, RSSI formés à la prise de poste puis à intervalles réguliers sur : législation, principaux risques et menaces, maintien en condition de sécurité, authentification et contrôle d'accès, paramétrage fin et durcissement, cloisonnement réseau, journalisation ; liste adaptée au métier (développement sécurisé pour les développeurs, etc.) ; clauses de formation SSI dans les contrats de prestation (infogérants). Exemples de fautes visées : comptes trop privilégiés, comptes personnels pour exécuter des services, mots de passe faibles sur comptes privilégiés.

**Mesure 2 — Sensibiliser les utilisateurs aux bonnes pratiques élémentaires de sécurité informatique** [S] [R]
[S] Dès l'arrivée puis régulièrement : enjeux SSI, informations sensibles, obligations légales, consignes (pas d'équipement personnel sur le réseau, ne pas divulguer ni réutiliser les mots de passe pro/perso, signaler les événements suspects), moyens disponibles (verrouillage de session, outil de protection des mots de passe). [R] Élaboration et signature d'une **charte des moyens informatiques**.

**Mesure 3 — Maîtriser les risques de l'infogérance** [S]
Évaluer en amont les risques de l'externalisation ; étudier offres et limites de responsabilité ; imposer des exigences (réversibilité, audits, sauvegarde et restitution des données en format ouvert normalisé, maintien du niveau de sécurité) ; **plan d'assurance sécurité (PAS)** contractuel. Les solutions non maîtrisées (ex. hébergées dans le nuage) ne relèvent pas de l'infogérance et sont **déconseillées pour des informations sensibles**.

### II — Connaître le système d'information

**Mesure 4 — Identifier les informations et serveurs les plus sensibles et maintenir un schéma du réseau** [S]
Lister les données sensibles, en déduire les composants qui les hébergent (serveurs/postes critiques → mesures spécifiques de sauvegarde, journalisation, accès) ; maintenir une **cartographie** : zones IP et plan d'adressage, équipements de routage et de sécurité, interconnexions externes et partenaires, localisation des serveurs sensibles.

**Mesure 5 — Disposer d'un inventaire exhaustif des comptes privilégiés et le maintenir à jour** [S]
Inventaire : comptes administrateurs ou à droits supérieurs, comptes pouvant accéder aux répertoires des responsables ou de tous, utilisateurs de postes non administrés ; **revue périodique** (supprimer les accès obsolètes) ; **nomenclature claire** pour comptes de service et d'administration (facilite revue et détection d'intrusion).

**Mesure 6 — Organiser les procédures d'arrivée, de départ et de changement de fonction des utilisateurs** [S] [R]
[S] Procédures définies avec les RH couvrant : création/suppression des comptes et boîtes aux lettres, droits à attribuer/retirer lors d'un changement de fonction, accès physiques (badges, clés), équipements mobiles affectés, documents et informations sensibles (transfert/changement des mots de passe et codes). Révocation de **tous** les droits au départ. [R] Procédures **formalisées** et mises à jour selon le contexte.

**Mesure 7 — Autoriser la connexion au réseau de l'entité aux seuls équipements maîtrisés** [S] [R]
[S] Seuls les terminaux maîtrisés par l'entité se connectent aux réseaux (filaire et sans fil) ; solutions pragmatiques pour les autres (Wi-Fi à **SSID dédié** pour terminaux personnels/visiteurs). [R] **Authentification des postes sur le réseau** (802.1X ou équivalent).

### III — Authentifier et contrôler les accès

**Mesure 8 — Identifier nommément chaque personne accédant au système et distinguer les rôles utilisateur/administrateur** [S] [R]
[S] Comptes **nominatifs** ; comptes génériques (admin, user) **marginaux** et rattachés à un nombre limité de personnes physiques ; comptes de service (apache, mysqld) admis ; génériques et service gérés selon une politique au moins aussi stricte ; chaque administrateur a un **compte d'administration nominatif distinct** (ex. `pmartin` / `adm-pmartin`), aux secrets différents, **dédié** à l'administration et utilisé sur des **environnements dédiés**. [R] Journalisation liée aux comptes (connexions réussies/échouées).

**Mesure 9 — Attribuer les bons droits sur les ressources sensibles du système d'information** [S]
Liste des ressources sensibles (répertoires, bases de données, boîtes aux lettres) ; pour chacune : population autorisée, contrôle d'accès strict (authentification + appartenance), **éviter dispersion et duplication** vers des lieux moins contrôlés (exports de configuration, documentation technique, bases métier) ; **revue régulière** des droits.

**Mesure 10 — Définir et vérifier des règles de choix et de dimensionnement des mots de passe** [S]
Sensibiliser aux mots de passe devinables et à la réutilisation (notamment perso/pro) ; mesures de contrôle : **blocage des comptes après plusieurs échecs**, désactivation des **connexions anonymes**, **outil d'audit de robustesse** ; communication préalable sur le sens des règles. Renvoi : note technique mots de passe (juin 2012).

**Mesure 11 — Protéger les mots de passe stockés sur les systèmes** [S]
Proscrire post-it, fichiers en clair, envoi par mail à soi-même, « se souvenir du mot de passe » ; utiliser un **coffre-fort numérique** et des mécanismes de **chiffrement** ; mot de passe maître robuste et mémorisé.

**Mesure 12 — Changer les éléments d'authentification par défaut sur les équipements et services** [S] [R]
[S] Considérer les configurations par défaut comme **connues des attaquants** ; changer les authentifiants par défaut **dès l'installation**, conformément aux mesures 10-11 ; secret « en dur » impossible à changer → signaler au distributeur. [R] **Renouvellement régulier** des authentifiants après changement.

**Mesure 13 — Privilégier lorsque c'est possible une authentification forte** [S] [R]
[S] Deux facteurs parmi : ce que je sais (mot de passe, tracé, signature), ce que je possède (carte à puce, jeton USB, carte magnétique, RFID, téléphone recevant un SMS), ce que je suis (biométrie). [R] Privilégier la **carte à puce**, à défaut **OTP avec jeton physique** ; la carte à puce exige une infrastructure de gestion des clés mais sert à plusieurs fins (chiffrement, messagerie, poste).

### IV — Sécuriser les postes

**Mesure 14 — Mettre en place un niveau de sécurité minimal sur l'ensemble du parc informatique** [S] [R]
[S] Sur tout le parc (postes, serveurs, imprimantes, téléphones, USB) : limiter applications et modules de navigateur au nécessaire ; **pare-feu local et antivirus** ; **chiffrer les partitions** de données utilisateur ; **désactiver l'autorun** ; poste en dérogation (ex. impossible à mettre à jour) → **isolé**. [R] **Sauvegardes régulières** des données vitales sur **équipements déconnectés**, restauration **vérifiée périodiquement** (menace rançongiciel).

**Mesure 15 — Se protéger des menaces relatives à l'utilisation de supports amovibles** [S] [R]
[S] Sans interdiction totale : identifier des mesures, sensibiliser ; **proscrire les clés inconnues**, limiter les clés non maîtrisées sauf inspection antivirus. [R] **Interdire l'exécution** depuis les amovibles (AppLocker, montage `noexec`) ; **procédure de mise au rebut** stricte jusqu'à destruction sécurisée.

**Mesure 16 — Utiliser un outil de gestion centralisée afin d'homogénéiser les politiques de sécurité** [S]
La sécurité vaut celle du maillon le plus faible ; politiques (mots de passe, restrictions de connexion, configuration navigateurs) appliquées simplement et rapidement, notamment pour les contre-mesures de crise ; outil central (ex. Active Directory) incluant le plus d'équipements possible ; harmonisation matériels/OS ; durcissement poussé depuis un point central.

**Mesure 17 — Activer et configurer le pare-feu local des postes de travail** [S] [R]
[S] Activer le pare-feu local pour freiner le **déplacement latéral** (les flux poste à poste sont rares). [R] Bloquer les ports d'administration par défaut (**TCP 135, 445, 3389** Windows ; **TCP 22** Unix) sauf depuis des ressources identifiées ; analyse des flux entrants utiles ; **blocage par défaut + liste blanche** ; **journaliser les flux bloqués**.

**Mesure 18 — Chiffrer les données sensibles transmises par voie Internet** [S]
Aucune garantie sur le trajet Internet → **chiffrement systématique** avant envoi par courriel ou hébergement en ligne ; secret de déchiffrement transmis par **canal de confiance ou canal distinct** (main propre, téléphone). Renvoi au catalogue des produits qualifiés.

### V — Sécuriser le réseau

**Mesure 19 — Segmenter le réseau et mettre en place un cloisonnement entre ces zones** [S]
Réseau « à plat » = compromission d'une machine met tout en péril ; dès la conception, **zones aux besoins de sécurité homogènes** (serveurs d'infrastructure, métiers, postes utilisateurs, postes admin, ToIP…) ; VLAN et sous-réseaux dédiés voire infrastructures dédiées ; **filtrage IP par pare-feu** entre zones ; cloisonner particulièrement **l'administration** ; si cloisonnement a posteriori difficile, l'intégrer à chaque extension/renouvellement.

**Mesure 20 — S'assurer de la sécurité des réseaux d'accès Wi-Fi et de la séparation des usages** [S]
Limiter par segmentation l'impact d'une intrusion radio ; filtrer les flux des postes Wi-Fi au strict nécessaire ; chiffrement robuste (**WPA2, AES CCMP**) et authentification centralisée, si possible par **certificats clients** ; mot de passe unique partagé déconseillé (sinon complexe, renouvelé, jamais diffusé) ; administration sécurisée des points d'accès ; Wi-Fi personnels/visiteurs **séparés** (SSID et VLAN distincts, accès Internet dédié).

**Mesure 21 — Utiliser des protocoles réseaux sécurisés dès qu'ils existent** [S]
Sur Internet **comme en interne** : protocoles reposant sur **TLS** (https, IMAPS, SMTPS, POP3S) ; protocoles sûrs par conception (**SSH** au lieu de TELNET/RLOGIN).

**Mesure 22 — Mettre en place une passerelle d'accès sécurisé à Internet** [S] [R]
[S] Pas d'accès direct des terminaux utilisateurs à Internet ; passerelle avec **pare-feu** au plus près de l'accès et **serveur mandataire (proxy)** assurant authentification des utilisateurs et **journalisation des requêtes**. [R] Antivirus de contenu, filtrage par catégories d'URL ; MCS des équipements de passerelle ; redondance selon besoin de disponibilité ; **résolution DNS directe désactivée** pour les terminaux (déléguée au proxy) ; postes nomades passant d'abord par une connexion sécurisée au SI pour naviguer.

**Mesure 23 — Cloisonner les services visibles depuis Internet du reste du système d'information** [S]
Services exposés hébergés en interne : haut niveau de protection, **administrateurs compétents, formés en continu et disponibles** — sinon privilégier un hébergement externalisé professionnel ; infrastructures d'hébergement **physiquement cloisonnées** du reste du SI ; filtrage de ces flux **distinct** des autres flux ; flux entrants imposés via un **reverse proxy** embarquant des mécanismes de sécurité.

**Mesure 24 — Protéger sa messagerie professionnelle** [S] [R]
[S] Messagerie = **principal vecteur d'infection** ; sensibiliser (expéditeur connu ? message attendu ? lien cohérent ? vérifier par autre canal) ; mesures organisationnelles contre les escroqueries (faux virement du dirigeant) ; **proscrire la redirection vers une messagerie personnelle** ; antivirus en amont des boîtes ; **TLS** entre serveurs et entre postes et serveurs. [R] Ne pas exposer directement les serveurs de boîtes aux lettres (**relais dédié** en coupure d'Internet) ; **anti-spam** ; enregistrements DNS **MX, SPF, DKIM, DMARC**.

**Mesure 25 — Sécuriser les interconnexions réseau dédiées avec les partenaires** [S] [R]
[S] Interconnexion via Internet → **tunnel site à site, de préférence IPsec** ; partenaire **non sûr par défaut** → filtrage IP au plus près de l'entrée ; **matrice des flux** entrants/sortants réduite au juste besoin, maintenue, configuration conforme. [R] Équipement de filtrage **dédié** aux connexions partenaires ; sonde de **détection d'intrusion** ; **point de contact à jour** chez le partenaire pour réagir aux incidents.

**Mesure 26 — Contrôler et protéger l'accès aux salles serveurs et aux locaux techniques** [S]
Sécurité physique à l'état de l'art ; accès par serrure ou badge ; pas d'accès non accompagné des prestataires sauf traçabilité stricte et plages horaires ; **revue régulière** des droits d'accès ; retrait des droits / changement des codes au départ d'un collaborateur ou d'un prestataire ; **prises réseau** des zones ouvertes au public restreintes ou désactivées.

### VI — Sécuriser l'administration

**Mesure 27 — Interdire l'accès à Internet depuis les postes ou serveurs utilisés pour l'administration du système d'information** [S] [R]
[S] Aucun accès Internet (web, messagerie) depuis un poste ou serveur d'administration ; **poste distinct** pour les usages Internet des admins, ou à défaut bureautique virtualisée distante **depuis** le poste d'admin ; la réciproque (accès à l'administration depuis un poste bureautique) est **déconseillée** (élévation de privilèges). [R] Mises à jour récupérées depuis une **source sûre**, **contrôlées**, puis transférées (support amovible dédié) ; **zone d'échanges** pour automatiser.

**Mesure 28 — Utiliser un réseau dédié et cloisonné pour l'administration du système d'information** [S] / [R] selon la solution
Cloisonner le réseau d'administration, notamment vis-à-vis du réseau bureautique (contre le rebond poste utilisateur → ressource d'admin). Par ordre de préférence : **cloisonnement physique** [R] ; à défaut, **cloisonnement logique cryptographique par tunnels IPsec** [S] ; au minimum, **cloisonnement logique par VLAN** [S].

**Mesure 29 — Limiter au strict besoin opérationnel les droits d'administration sur les postes de travail** [S]
Par défaut **aucun utilisateur**, quelle que soit sa position hiérarchique, n'est administrateur de son poste ; **magasin d'applications validées** ; seuls les administrateurs des postes ont ces droits, pendant leurs interventions ; délégation ponctuelle **tracée, limitée dans le temps et retirée à échéance**.

### VII — Gérer le nomadisme

**Mesure 30 — Prendre des mesures de sécurisation physique des terminaux nomades** [S] [R]
[S] Sensibiliser à la vigilance (équipement à portée de vue) ; terminaux **banalisés** (aucune mention de l'entité) ; **filtre de confidentialité** sur chaque écran. [R] Support externe (carte à puce, jeton USB) conservé **à part** pour les secrets de déchiffrement/authentification, rendant le poste seul inutilisable.

**Mesure 31 — Chiffrer les données sensibles, en particulier sur le matériel potentiellement perdable** [S]
Ne stocker que des **données chiffrées** sur tout matériel nomade (portables, ordiphones, clés USB, disques externes) ; accès par un secret unique et robuste ; **commencer par un chiffrement complet du disque** avant le chiffrement d'archives/fichiers (qui peut laisser des résidus en clair, ex. fichiers de restauration).

**Mesure 32 — Sécuriser la connexion réseau des postes utilisés en situation de nomadisme** [S] [R]
[S] Tunnel **VPN IPsec** (fortement recommandé plutôt que VPN SSL/TLS) vers une passerelle de l'entité, **établi automatiquement et non débrayable** (aucun flux hors tunnel) ; dérogation possible pour portails captifs ou usage d'un partage de connexion mobile de confiance. [R] **Authentification forte** (mot de passe + certificat sur support externe, ou OTP) pour empêcher la réutilisation d'authentifiants d'un poste volé.

**Mesure 33 — Adopter des politiques de sécurité dédiées aux terminaux mobiles** [S] [R]
[S] **Ne pas mutualiser** usages personnel et professionnel sur un même terminal ; terminaux pro sécurisés à part entière ; **gestion centralisée des mobiles (MDM)** : moyen de déverrouillage, magasin limité aux applications validées ; à défaut, configuration préalable et sensibilisation avant remise. [R] **Assistant vocal** intégré déconseillé (surface d'attaque).

### VIII — Maintenir le système d'information à jour

**Mesure 34 — Définir une politique de mise à jour des composants du système d'information** [S]
Veille (CERT-FR) et application des correctifs de sécurité **dans le mois** suivant leur publication ; politique déclinée en procédures : méthode d'inventaire, sources d'information, outils de déploiement, qualification et déploiement progressif ; composants **obsolètes non supportés isolés** (filtrage réseau strict et **secrets d'authentification dédiés**).

**Mesure 35 — Anticiper la fin de la maintenance des logiciels et systèmes et limiter les adhérences logicielles** [S]
Inventaire des systèmes et applications ; solutions supportées sur toute leur durée d'usage ; suivi des mises à jour et **dates de fin de support** ; parc **homogène** (pas de versions multiples d'un produit) ; limiter les **adhérences** (dépendances) surtout vers des composants en fin de support ; clauses contractuelles de suivi des correctifs ; identifier délais et ressources de migration (tests de non-régression, sauvegarde, migration des données).

### IX — Superviser, auditer, réagir

**Mesure 36 — Activer et configurer les journaux des composants les plus importants** [S] [R]
[S] Identifier les composants critiques ; régler format, rotation, taille, catégories ; événements critiques **conservés au moins un an** ; journaliser au minimum : **pare-feu** (paquets bloqués), **systèmes et applications** (authentifications et autorisations, échecs **et** succès, arrêts inopinés), **services** (erreurs de protocole, ex. HTTP **403, 404, 500** ; traçabilité des flux aux interconnexions : URL sur relais HTTP, en-têtes SMTP) ; **source de temps NTP identique** pour corréler. [R] **Centralisation** des journaux sur un dispositif dédié (recherche automatisée, archivage long, empêcher l'effacement des traces).

**Mesure 37 — Définir et appliquer une politique de sauvegarde des composants critiques** [S] [R]
[S] Politique formalisée et mise à jour incluant : données vitales et serveurs concernés, types de sauvegarde (dont **hors ligne**), fréquence, procédure d'exécution, stockage et **restrictions d'accès aux sauvegardes**, **tests de restauration** (systématiques par ordonnanceur, ponctuels, généraux), destruction des supports. [R] **Exercice de restauration au moins une fois par an**, avec trace technique des résultats.

**Mesure 38 — Procéder à des contrôles et audits de sécurité réguliers puis appliquer les actions correctives associées** [R]
Audits **au moins annuels** (internes ou externes, techniques et/ou organisationnels) ; actions correctives identifiées, planifiées, suivies ; indicateurs dans un tableau de bord de direction ; un audit **ne prouve jamais l'absence** de vulnérabilité. PASSI qualifiés : audit d'architecture, de configuration, de code source, tests d'intrusion, audit organisationnel et physique.

**Mesure 39 — Désigner un référent en sécurité des systèmes d'information et le faire connaître auprès du personnel** [S]
Référent soutenu par la direction, **connu de tous**, premier contact : définition des règles, vérification de leur application, sensibilisation et plan de formation, **centralisation et traitement des incidents** ; formé à la SSI et à la **gestion de crise** ; relais du RSSI dans les grandes entités.

**Mesure 40 — Définir une procédure de gestion des incidents de sécurité** [S]
Signaux d'alerte (connexion impossible, activité inhabituelle, services non autorisés, fichiers modifiés, alertes antivirus multiples) ; **réflexe : déconnecter la machine du réseau, la laisser sous tension, ne pas redémarrer** ; prévenir hiérarchie et référent SSI ; recours possible à un **PRIS** (copie de disque, analyse mémoire/journaux/codes) ; éradication, **changement des mots de passe compromis** ; **registre centralisé** des incidents ; plainte possible.

### X — Pour aller plus loin

**Mesure 41 — Mener une analyse de risques formelle** [R]
Mesures justifiées par des risques identifiés ; démarche : contexte → appréciation (probabilité × gravité) → traitement ; **plan de traitement validé par une autorité de haut niveau** ; trois approches (bonnes pratiques, analyse fondée sur les retours d'expérience, gestion structurée) ; méthode recommandée : **EBIOS**.

**Mesure 42 — Privilégier l'usage de produits et de services qualifiés par l'ANSSI** [R]
Catalogues ANSSI de produits et prestataires qualifiés : **PASSI** (audit), **PRIS** (réponse aux incidents), **PDIS** (détection), **SecNumCloud** (nuage).

---

## Chiffres et seuils à retenir

| Seuil | Mesure |
|---|---|
| **42** mesures, **10** chapitres, 2 niveaux (standard / renforcé) | Mode d'emploi |
| Correctifs de sécurité appliqués **dans le mois** suivant publication | 34 |
| Journaux des événements critiques conservés **≥ 1 an** (plus selon obligations légales) | 36 |
| Codes HTTP à journaliser : **403, 404, 500** | 36 |
| **Une seule source NTP** commune à tous les composants | 36 |
| Exercice de restauration des sauvegardes **≥ 1 fois par an** | 37 [R] |
| Audit de sécurité **≥ 1 fois par an** | 38 [R] |
| Ports d'admin à bloquer sur les postes : **TCP 135, 445, 3389** (Windows), **TCP 22** (Unix) | 17 [R] |
| **2 facteurs** distincts pour l'authentification forte | 13 |
| Wi-Fi : **WPA2 / AES CCMP** (valeur 2017) | 20 |
| Messagerie : **MX, SPF, DKIM, DMARC** | 24 [R] |
| Nommage admin : identifiant utilisateur ≠ identifiant admin (`pmartin` / `adm-pmartin`) | 8 |
| Délégation de privilèges : **tracée, limitée dans le temps, retirée à échéance** | 29 |

---

## Application à PLÉIADE

Rappel du contexte : par **zone** d'exercice, apps web Next.js conteneurisées (Docker/Podman) sur un serveur Linux, derrière **Traefik** (TLS, **PKI/CA interne de zone**), **Keycloak** (OIDC), **MariaDB**, clés de service inter-apps (**`X-API-Key`**), accès par **VPN Pritunl**, dépôts GitHub `cecpc-pleiade`, **déploiement automatique** depuis `main`/`prod`, postes Windows des animateurs, **tablettes LEAC hors ligne** synchronisées au retour, comptes de zone **anonymes** (`gc01`…).

> Statut : **Applicable** · **Partiellement** (adaptation nécessaire ou portée réduite) · **Hors champ** (ne relève pas de PLÉIADE ou relève de l'hébergeur / de l'unité). Les « À vérifier » sont des **contrôles à réaliser** : aucune affirmation n'est faite ici sur l'état actuel du code.

| # | Statut | Ce que ça implique pour PLÉIADE | À vérifier |
|---|---|---|---|
| 1 | Applicable | Les développeurs/administrateurs PLÉIADE (y compris les agents IA qui codent) doivent maîtriser durcissement conteneurs, OIDC, journalisation, développement sécurisé. | À vérifier : existence d'un mémo « développement sécurisé PLÉIADE » (secrets, validation d'entrée, OIDC) lu par tout contributeur. |
| 2 | Partiellement | Animateurs et joueurs : consignes simples (ne pas partager les comptes de zone, verrouiller le poste, signaler un comportement anormal). [R] Charte d'usage de la zone. | À vérifier : une fiche consignes / charte est remise aux animateurs à l'ouverture d'une zone. |
| 3 | Partiellement | Dépendance à des tiers (GitHub, registres d'images, éventuel hébergeur) = externalisation ; données d'exercice éventuellement sensibles. | À vérifier : liste des services tiers utilisés et, pour chacun, réversibilité (export des données en format ouvert) ; aucune donnée sensible d'exercice dans un service non maîtrisé. |
| 4 | Applicable | Cartographie par zone : réseaux Docker/Podman, ports exposés par Traefik, flux inter-apps (`X-API-Key`), Keycloak, MariaDB, VPN, synchro LEAC ; désigner les composants sensibles (Keycloak, eho, MariaDB, CA). | À vérifier : un schéma à jour des flux d'une zone type (apps ↔ eho ↔ Keycloak ↔ MariaDB ↔ Traefik ↔ VPN) existe dans `PLEIADE`. |
| 5 | Applicable | Inventaire des comptes privilégiés : admins Keycloak (realm master et realms de zone), `root` MariaDB, comptes de service des apps, détenteurs des clés `X-API-Key`, admins GitHub de l'organisation, admins Pritunl, accès SSH au serveur. Nomenclature claire. | À vérifier : un inventaire des comptes privilégiés et clés de service par zone, revu à chaque ouverture/fermeture de zone. |
| 6 | Applicable (adapté) | Le cycle de vie est **celui de la zone** : création des comptes `gc01…` à l'ouverture, **révocation/suppression à la fermeture**, rotation des mots de passe entre exercices ; départ d'un développeur → retrait GitHub, VPN, SSH, Keycloak admin. | À vérifier : procédure de fermeture de zone qui désactive les comptes Keycloak, révoque les profils VPN et les clés de service ; procédure de départ d'un contributeur. |
| 7 | Partiellement | Le VPN est le point d'entrée : seuls des terminaux identifiés (postes animateurs, tablettes LEAC dotées) doivent recevoir un profil. [R] Authentification du terminal (certificat machine). | À vérifier : liste des profils VPN émis ↔ terminaux identifiés ; pas de profil partagé entre plusieurs appareils. |
| 8 | Partiellement | **Écart assumé** : les comptes de zone anonymes (`gc01…`) contredisent le principe nominatif. Compensation requise : table de correspondance compte ↔ personne tenue **hors ligne** par la direction d'exercice, comptes d'admin **nominatifs et distincts** (jamais d'admin anonyme), comptes de service nommés. [R] Journaliser les connexions réussies/échouées dans Keycloak. | À vérifier : tout compte à privilèges (Keycloak admin, admin de zone, SSH, MariaDB) est nominatif ; table `gc01 → personne` existe et est protégée ; les événements de connexion Keycloak sont activés et conservés. |
| 9 | Applicable | Ressources sensibles : bases MariaDB, exports (scénarios, injects MELMIL, notes LEAC), volumes Docker, fichiers `.env`. Contrôle par rôles OIDC, pas de copies d'exports dans des lieux non maîtrisés. | À vérifier : chaque route API d'admin/export vérifie le rôle Keycloak côté serveur ; revue des rôles à chaque zone ; pas de dumps de base dans les dépôts ni sur des partages ouverts. |
| 10 | Applicable | Politique de mots de passe Keycloak (longueur, interdiction des triviaux), **protection anti-force brute** (verrouillage après échecs), aucune connexion anonyme sur les API. | À vérifier : realm Keycloak avec password policy et brute force detection activées ; aucune route API répondant sans authentification hors `/api/sante`. |
| 11 | Applicable | Secrets (clés `X-API-Key`, secrets clients OIDC, mots de passe MariaDB, clés de la CA) : jamais en clair dans Git ni dans les images ; gestionnaire de secrets ou variables chiffrées ; mots de passe utilisateurs **hachés** côté Keycloak/apps. | À vérifier : recherche de secrets dans l'historique Git des 12 dépôts (ex. gitleaks) ; `.env` exclus par `.gitignore` ; secrets injectés au déploiement, pas dans le `Dockerfile`. |
| 12 | Applicable | Aucun mot de passe par défaut : admin Keycloak initial, `root` MariaDB, admin WordPress, admin Pritunl, comptes de seed (`dev\` scripts). [R] Rotation régulière (à chaque exercice). | À vérifier : les scripts de bootstrap/seed génèrent des secrets aléatoires par zone au lieu de valeurs fixes ; aucun identifiant de type `admin/admin` en production. |
| 13 | Applicable | **MFA** (TOTP au minimum) pour tous les comptes à privilèges : admins Keycloak, admin de zone, GitHub de l'organisation, Pritunl. Pour les comptes de jeu, au cas par cas. | À vérifier : OTP obligatoire sur les rôles admin Keycloak ; 2FA imposée sur l'organisation GitHub `cecpc-pleiade`. |
| 14 | Applicable | Socle minimal sur serveur, postes animateurs et tablettes : logiciels limités, pare-feu, antivirus (postes Windows), **chiffrement du stockage**, autorun désactivé. [R] Sauvegardes déconnectées. Images conteneurs minimales. | À vérifier : images de base minimales (alpine/distroless/slim) sans outils inutiles ; tablettes LEAC chiffrées ; postes animateurs avec Defender/pare-feu actifs. |
| 15 | Partiellement | Transferts par clé USB (mises à jour, exports, synchro hors VPN) à encadrer. [R] Pas d'exécution depuis l'amovible, destruction en fin de vie. | À vérifier : s'il existe un mode de synchro LEAC par fichier/clé, contrôle d'intégrité (signature/empreinte) avant import. |
| 16 | Partiellement | Équivalent PLÉIADE : configuration **déclarative et homogène** (images, compose/quadlets, Traefik, realms Keycloak versionnés) appliquée depuis l'orchestrateur `pleiade-platform` ; pour les postes, gestion centralisée relève de l'unité. | À vérifier : toutes les zones sont instanciées depuis le même gabarit versionné (pas de configuration manuelle divergente). |
| 17 | Applicable (transposé) | Sur le serveur : pare-feu hôte (nftables/firewalld) n'exposant que Traefik et le VPN ; réseaux Docker/Podman isolés ; **MariaDB et Keycloak admin jamais exposés** ; SSH limité aux sources d'administration ; journaliser les rejets. | À vérifier : `ss -tlnp` / scan externe ne montre que 443 (et ports VPN) ; MariaDB non publiée hors réseau interne ; port 22 filtré. |
| 18 | Applicable | Exports d'exercice envoyés par courriel/cloud chiffrés ; secret transmis par un autre canal. | À vérifier : procédure de transmission des exports de zone (chiffrement + canal séparé pour le secret). |
| 19 | Applicable | **Une zone = un segment isolé** ; dans la zone, réseaux séparés « exposé » (Traefik ↔ apps) et « données » (apps ↔ MariaDB) ; administration à part ; aucune communication entre zones. | À vérifier : réseaux Docker/Podman distincts par zone et par niveau ; un conteneur d'une zone ne peut pas joindre la base d'une autre zone. |
| 20 | Partiellement | Si un Wi-Fi terrain sert aux tablettes : WPA2/WPA3, pas de mot de passe largement diffusé, séparation visiteurs. | À vérifier : configuration du point d'accès utilisé sur le terrain (chiffrement, mot de passe renouvelé par exercice, admin modifié). |
| 21 | Applicable | **HTTPS partout**, y compris **en interne** (inter-apps, synchro LEAC) ; SSH pour l'administration ; TLS vers MariaDB si hors hôte. | À vérifier : aucune redirection ni route en HTTP clair accessible ; appels inter-apps via TLS (CA de zone) ; HSTS activé sur Traefik. |
| 22 | Partiellement | Conteneurs : sortie Internet à restreindre au strict nécessaire (pas d'accès sortant libre) ; résolution DNS contrôlée. Navigation des postes : ressort de l'unité. | À vérifier : politique de flux sortants des conteneurs (egress) documentée ; les apps n'appellent pas d'API externes non prévues. |
| 23 | Applicable | Traefik = **reverse proxy** obligatoire pour tout flux entrant ; aucune app exposée directement ; services visibles isolés du reste ; administrateurs compétents et disponibles pendant l'exercice. | À vérifier : aucun conteneur n'a de port publié hors Traefik ; middlewares de sécurité (en-têtes, limitation de débit) actifs. |
| 24 | Partiellement | La messagerie d'exercice (app-messagerie) est fictive mais peut porter des liens/fichiers : antivirus/filtrage des pièces jointes, pas de redirection vers des messageries réelles ; si un SMTP réel existe : TLS, SPF/DKIM/DMARC. | À vérifier : l'app messagerie filtre types et tailles de pièces jointes et ne relaie pas vers l'extérieur. |
| 25 | Partiellement | Interconnexions avec des partenaires (autre unité, exports JEMM) : tunnel chiffré, matrice des flux minimale, point de contact. | À vérifier : matrice des flux inter-sites documentée pour chaque exercice interconnecté. |
| 26 | Partiellement | Salle serveur / emplacement du serveur de zone sur le terrain : accès contrôlé, prises réseau publiques désactivées. | À vérifier : localisation physique du serveur pendant l'exercice et contrôle d'accès associé. |
| 27 | Partiellement | Le serveur PLÉIADE ne doit pas servir à naviguer ; administration depuis un poste dédié plutôt que depuis le poste bureautique quotidien. [R] Images et mises à jour issues de sources sûres, vérifiées. | À vérifier : le poste qui administre le serveur (SSH, Keycloak admin, Pritunl) n'est pas utilisé pour la messagerie/navigation ; images tirées de registres de confiance, épinglées par digest. |
| 28 | Applicable | Interfaces d'administration (console Keycloak, Pritunl, Traefik dashboard, SSH, MariaDB) sur un **réseau/chemin d'administration distinct**, jamais sur l'accès joueurs. | À vérifier : la console d'admin Keycloak (`/admin`) n'est pas joignable depuis le réseau joueurs ; dashboard Traefik désactivé ou protégé. |
| 29 | Applicable | Conteneurs **non root**, capacités Linux minimales ; utilisateurs des postes animateurs et tablettes sans droits admin ; droits admin de zone limités dans le temps à l'exercice. | À vérifier : `USER` non root dans chaque `Dockerfile` ; `cap_drop: ALL` / `no-new-privileges` ; rôles admin de zone retirés à la clôture. |
| 30 | Applicable | **Tablettes LEAC** : banalisées, filtre de confidentialité si usage en public, vigilance anti-vol. [R] Secret sur support séparé. | À vérifier : procédure de dotation/restitution des tablettes avec contrôle de présence à chaque fin de journée. |
| 31 | Applicable (critique) | Tablettes hors ligne = matériel **perdable** contenant des notations de contrôle : **chiffrement complet du stockage** de l'appareil + données applicatives locales chiffrées ou effaçables ; secret robuste. | À vérifier : chiffrement de l'appareil activé ; stockage local LEAC (IndexedDB/fichiers) non lisible sans déverrouillage ; effacement des données après synchronisation réussie. |
| 32 | Applicable | Accès distant uniquement via **VPN** (Pritunl : OpenVPN/WireGuard — le guide préconise IPsec, voir Limites), si possible **non débrayable**. [R] Authentification forte du VPN (certificat + OTP). Synchro LEAC uniquement à travers le VPN. | À vérifier : les apps ne sont pas joignables hors VPN ; Pritunl exige un second facteur ; les profils VPN des tablettes sont révocables individuellement. |
| 33 | Applicable | Tablettes LEAC **dédiées** à l'usage professionnel (pas de comptes perso), **MDM** si possible (verrouillage, applications autorisées), assistant vocal désactivé. | À vérifier : tablettes configurées avant remise (code de verrouillage, pas de compte personnel, assistant vocal coupé). |
| 34 | Applicable | Politique de mise à jour : OS du serveur, moteur Docker/Podman, Traefik, Keycloak, MariaDB, **images de base**, **dépendances npm/Next.js** — correctifs de sécurité **sous un mois** ; veille CERT-FR et alertes GitHub (Dependabot) ; déploiement progressif (`main` → `prod`). | À vérifier : Dependabot/`npm audit` actifs sur les 12 dépôts ; date de dernière mise à jour de chaque image de base ; aucune alerte critique ouverte > 30 jours. |
| 35 | Applicable | Suivre les fins de support (versions Node.js, Next.js, Keycloak, MariaDB) ; **harmoniser les versions** entre les apps ; limiter les dépendances npm. | À vérifier : tableau des versions par dépôt (Node, Next, Prisma, Keycloak) et dates de fin de support ; pas de version de Node en fin de vie. |
| 36 | Applicable | Journaliser : Traefik (accès, 4xx/5xx), Keycloak (événements de connexion échecs/succès, événements admin), apps (actions sensibles : export, suppression, changement de rôle, appels `X-API-Key` refusés), synchro LEAC ; **NTP commun** ; conserver **≥ 1 an** ou durée décidée et motivée. [R] Centralisation hors du serveur applicatif. | À vérifier : access logs Traefik activés ; événements Keycloak activés avec rétention définie ; horloge synchronisée sur le serveur et les tablettes ; logs exportés à la fermeture de zone. |
| 37 | Applicable | Sauvegarde des bases MariaDB, volumes (fichiers, médias), realms Keycloak, **CA de zone** ; au moins une copie **hors ligne** ; accès restreint ; **test de restauration** réel. [R] Exercice de restauration annuel tracé. | À vérifier : script de sauvegarde par zone + restauration testée sur une zone vierge (base + volume + `/api/sante` = 200). |
| 38 | Applicable | Audits réguliers : revue de configuration, revue de code des points d'authentification, test d'intrusion avant un exercice majeur ; plan d'actions suivi. | À vérifier : date du dernier audit/test d'intrusion de PLÉIADE et suivi des corrections. |
| 39 | Applicable | Désigner un **référent SSI PLÉIADE** connu des animateurs (l'agent CYBERSECU l'appuie, ne le remplace pas). | À vérifier : nom et contact du référent SSI affichés dans la documentation d'exercice. |
| 40 | Applicable | Procédure d'incident : isoler le conteneur/la zone **sans l'éteindre** (conserver mémoire/journaux), prévenir hiérarchie et référent, rotation des clés `X-API-Key`/secrets OIDC/profils VPN compromis, **registre des incidents**. Tablette perdue = incident (révocation du profil VPN et de la session). | À vérifier : fiche réflexe incident PLÉIADE (y compris perte de tablette) et registre centralisé. |
| 41 | Applicable | Analyse de risques (EBIOS RM) de la plateforme : sensibilité des données d'exercice, menace sur la zone, scénarios (vol de tablette, fuite de clé de service, compromission Keycloak). | À vérifier : existence d'une analyse de risques validée par l'autorité compétente. |
| 42 | Partiellement | Privilégier composants et prestataires qualifiés lorsque c'est possible (passerelle VPN, audit PASSI) ; la pile open source (Keycloak, Traefik) n'est en général pas qualifiée. | À vérifier : décision documentée sur l'usage de produits qualifiés pour le VPN/la PKI. |

**Hors champ pour PLÉIADE** (relèvent de l'unité / de l'infrastructure d'accueil, pas de la plateforme) : gestion RH globale des arrivées/départs (6, hors comptes PLÉIADE), Active Directory et gestion centralisée des postes de l'unité (16), passerelle Internet des postes bureautiques (22), messagerie professionnelle réelle (24), contrôle d'accès des locaux permanents (26).

---

## Limites / points d'attention

- **Ancienneté (septembre 2017)** : WPA2 (WPA3 existe depuis), SMS cité comme facteur de possession (aujourd'hui considéré faible), VPN **IPsec** préféré au VPN SSL/TLS (Pritunl repose sur OpenVPN/WireGuard : écart à justifier ou à couvrir par une autre référence ANSSI plus récente), notes techniques citées de 2012-2016 dont plusieurs ont été remplacées. Les URL `www.ssi.gouv.fr` sont à transposer vers `cyber.gouv.fr`.
- **Orientation « SI d'entreprise »** (postes Windows, AD, messagerie, Wi-Fi bureautique) : ni conteneurs, ni CI/CD, ni chaîne d'approvisionnement logicielle (dépendances npm, images), ni OIDC ne sont traités explicitement — la transposition à PLÉIADE ci-dessus est une **interprétation** de CYBERSECU, pas un texte ANSSI.
- **Comptes anonymes de zone** : écart direct à la mesure 8 ; acceptable pour le jeu seulement avec compensation (correspondance tenue hors ligne, admins nominatifs, journalisation).
- **Niveaux** : quand un référentiel ANSSI impose ces mesures, c'est le niveau **standard** qui est exigé sauf mention contraire (mode d'emploi). Mesures 38, 41, 42 = renforcé uniquement ; mesure 28 mêle les deux niveaux selon la solution de cloisonnement.
- Le guide est un **socle d'hygiène**, pas une analyse de risques : il ne remplace ni l'homologation ni une démarche EBIOS (mesure 41).
- Section « Application » : les contrôles « À vérifier » n'ont **pas** été exécutés lors de l'ingestion ; aucune conclusion sur l'état réel de PLÉIADE ne doit en être tirée.
