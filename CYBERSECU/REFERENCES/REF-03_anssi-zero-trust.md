# REF-03 — Modèle Zero Trust — Les fondamentaux

- **Fichier** : `anssi-fondamentaux-zero-trust-v1.0.pdf` · **Éditeur / référence** : ANSSI, ANSSI-PA-111 · **Date / version** : v1.0 du 20/06/2025 (version initiale) · **Pages** : 34 · **Marquage** : public (Licence Ouverte Etalab v2.0)
- **Public visé (couverture)** : développeur, administrateur, RSSI, DSI, utilisateur
- **Ingéré** : 2026-10-01

> ⚠ **Numérotation** : ce document **ne numérote pas** ses recommandations (puces sous les sections 3.1 à 3.4). La numérotation **ZT-01 … ZT-55** ci-dessous est **ajoutée par CYBERSECU**, dans l'ordre exact du document, avec la section d'origine entre crochets. Citer « ANSSI-PA-111 §3.x, ZT-nn ».

## En une phrase

Le Zero Trust est un **modèle** (pas un produit) qui réduit la **confiance implicite** accordée à un sujet en contrôlant chaque accès de façon granulaire, dynamique et régulière (sujet + contexte/poste + criticité de la ressource), et qui doit **compléter** — jamais remplacer — la défense périmétrique dans une stratégie de défense en profondeur.

## Ce que dit le document

### 1. Préambule — positionnement
- Contexte : télétravail, BYOD (fr. « AVEC »), accès hétérogènes on-premise/cloud ; les éditeurs promeuvent des produits « Zero Trust ».
- Le contrôle d'accès logique repose sur : (1) évaluation dynamique et régulière du **sujet** ; (2) évaluation dynamique et régulière du **contexte d'accès**, notamment l'état de sécurité du poste ; (3) la **criticité DIC** de la ressource.
- Zero Trust et défense périmétrique sont **complémentaires**, pas opposés. Les présenter comme une rupture « pourrait mener à une dégradation du niveau de sécurité global ». Le Zero Trust **ne remplace en aucun cas** VPN/pare-feux.
- Risques : politiques complexes → **faux sentiment de sécurité** (accès illégitime autorisé à tort) ou **frein opérationnel** (accès légitime refusé à tort). Bien implémenté et maintenu, il permet une posture plus proactive.
- Complète l'avis scientifique ANSSI de 2020 ; ne traite ni la stratégie de migration (renvoi CISA Zero Trust Maturity Model) ni le détail des cas d'usage.

### 2. Glossaire (notions clés)
- **Niveau de confiance implicite** : intégrité attendue d'un sujet/composant, indépendante du contexte instantané ; **nul** dans le modèle théorique.
- **Niveau de confiance explicite (score de confiance)** : estimation continue (conformité à la politique + niveau de menace). **Ne peut pas dépasser** la confiance implicite accordée aux fonctions et sources de données qui le calculent.
- **Niveau de criticité** : par critère D, I, C. **Niveau de risque** = confiance explicite (vraisemblance) × criticité DIC (impact).
- **Plan de contrôle** (supervision, décisions, configuration des conditions d'accès) / **plan de données** (fonctions et échanges métier).
- **Sujet** (utilisateur, processus automatique, équipement actif) / **ressource** (entité passive) / **session** (canal authentifié reliant les actions à une identité).
- ABAC, RBAC, EDR, SIEM, API, assurance sécurité.

### 3. Objectif (§2.2) — contrôles granulaires, dynamiques, réguliers
Besoin d'en connaître ; moindre privilège ; **même attention quelle que soit l'origine** (intérieur ou extérieur) ; attributs dynamiques (comportement, horaires, géolocalisation) ; **réévaluation régulière** des conditions d'accès.

### 4. Architecture fonctionnelle (§2.3)
- Repose sur **ABAC** : attributs du **sujet** (habilitation, rôle), de la **ressource** (classification, propriétaire), du **contexte** (heure, lieu, état des mises à jour du poste).
- Blocs (NIST SP 800-207) : **PDP** (décision), **PIP** (attributs), **PEP** (application). Répartition technique dépendante des éditeurs (ex. détection locale EDR et/ou centrale SIEM).
- Déroulé (figure 1, étapes 1 à 7) : demande d'accès → authentification/preuve d'identité → évaluation des attributs → conditions d'accès (timeout de session, etc.) → canal sécurisé. Puis **contrôle des actions** en session (pur ABAC par action, ou confiance implicite **limitée dans le temps** avec rôle/groupe transmis — DAC/RBAC). **Maintien** : réauthentification périodique, réévaluation continue → session maintenue, mise à jour ou fermée.
- Exemple « Alice » : MFA, accès autorisé avec rôle (mixte ABAC/RBAC), tentatives répétées sur des fichiers non autorisés → baisse du score → perte des droits, session fermée, nouvelles demandes rejetées.

### 5. Contraintes sur les attributs (§2.3.2)
Six critères (disponibilité/intégrité) : **pertinence** ; **mise à jour des sources** ; **fraîcheur** (valeur en cache = identité compromise non prise en compte) ; **fiabilité de calcul** (ML difficile) ; **disponibilité d'accès** (indisponibilité = refus = déni de service) ; **authenticité** (perte = accès à tort). La confidentialité des attributs est hors sujet du document, mais certains attributs sujets ont de forts besoins de confidentialité.

### 6. Fonctionnalités (§2.3.3)
- **Identités et authentifiants** : référentiels centraux d'**identités uniques** (utilisateurs, processus, équipements), attributs à jour (changement de fonction, poste compromis) ; robustesse de l'authentifiant (type, protection repos/transit, entropie, dissémination, durée de vie, renouvellement) ; MFA forte contre hameçonnage et rejeu ; **authentification continue** (vol de cookies de session → la confiance se dégrade dans le temps). L'**authentification passive** (ex. biométrie faciale) améliore l'acceptabilité mais **ne répond pas aux bonnes pratiques ANSSI**. Prérequis renforcés : compte unique, généralisation de l'authentification forte et multifacteur.
- **Données** : inventorier et catégoriser (valeur, réglementaire) ; **labéliser** existant + nouveau (métadonnées protégées cryptographiquement). Prérequis complexe vu la volumétrie.
- **Actifs et vulnérabilités** : état attendu (gestion de configuration, versions de référence, inventaire avec criticité DIC et dépendances) ; écarts (inventaire périodique vs attendu — **un inventaire ne garantit pas l'intégrité** ; scans de vulnérabilités paramétrage + CVE ; contrôle d'intégrité/authenticité : measured boot, liste d'applications autorisées par condensat/signature) ; **gestion des changements** (qualification DIC, choix de traitement, tests de non-régression) ; **mise à jour automatisée** (un équipement non conforme est refusé → il faut pouvoir le mettre à jour et le réévaluer automatiquement). Comparer un numéro de version **n'offre aucune assurance** d'intégrité.
- **Détecter la menace** : identifier événements redoutés (couples source de menace/événement redouté, EBIOS RM), composants à superviser (chemins d'attaque), techniques à superviser (MITRE ATT&CK) ; collecter (limites : flux chiffrés, équipements sans journaux) ; analyser par **signature** (IoC) et/ou **anomalie** (ML) ; évaluer le niveau de menace — réduire faux positifs/négatifs est long. Risque : dégradation des accès ou faux sentiment de sécurité.
- **Contrôler les autorisations** : règles au moindre privilège, trois types de critères (conformité simple ; score de confiance simple pondéré ; score complexe comportemental) ; contrôle des **sessions** (durée de vie max, délai avant réauthentification, configurables dynamiquement) et des **ressources** (pur ABAC ou mixte ABAC session / RBAC ressource avec rôles mis à jour dynamiquement). Prérequis parfois **non réalisables** sur certains systèmes.

### 7. Mécanismes de mise en œuvre (§2.4)
- **Assurance de l'identité** : MFA forte avec certificat ; authentification forte des processus/équipements par **défi/réponse** conforme RGS B1/B2/B3 ; stockage des authentifiants en **composant matériel dédié** (HSM) ; **SSO** / fédération. Exemples : **mTLS** ou IPsec à authentification mutuelle par certificat ; **FIDO2** avec jeton matériel protégé par PIN ou biométrie.
- **Intégrité de l'équipement** : un poste personnel et un poste géré n'ont **pas** la même confiance par défaut. Secure Boot UEFI / Measured Boot ; liste d'autorisation applicative ; mise à jour centralisée ; durcissement pilotable par API ; anti-malware/EDR.
- **Protection des réseaux** : **SDP** (port fermé par défaut, authentification préalable sur le plan de contrôle, tunnel ouvert dynamiquement, agent local requis) ; cloisonnement LAN (VLAN/PVLAN), réseau distant (VPN IPsec ou TLS = cloisonnement par le chiffre), service applicatif (inaccessible par défaut, ouverture du port à l'utilisateur + authentification mutuelle).
- **Protection des applications** (conteneurs et chaîne d'approvisionnement **non traités**) : **proxy Zero Trust** (sortant vers Internet, authentification obligatoire, coupure dynamique si confiance dégradée) ; **reverse proxy Zero Trust** (authentification préalable, conditions selon profil ; en option WAF, liste d'autorisation de commandes ; pas d'agent mais limité aux protocoles supportés). Postes maîtrisés = plus d'attributs, plus authentiques que les postes personnels.
- **Protection des données** : contrôle d'accès dynamique (labélisation obligatoire à la création/import, contrôle de l'export, masquage dynamique) ; protection cryptographique au repos et en transit.

### 8. Principaux risques (§2.5)
Centralisation des décisions (nouveau service transverse critique) ; disponibilité/intégrité/authenticité des attributs ; justesse du score de confiance ; écart modèle/produits (« Zero Trust n'est qu'un modèle ») ; manque de standardisation (dépendance éditeur, fédération difficile) ; impact sur les performances (dimensionnement) ; dépendance au cloud (Zero Trust **n'implique pas** le cloud).

## Toutes les recommandations

*(numérotation ZT-nn ajoutée ; section d'origine entre crochets)*

**§3.1 Objectifs de sécurité et état des lieux**
- **ZT-01** [3.1] Définir les objectifs de sécurité de chaque système selon une **approche par les risques** (il peut être plus pertinent d'améliorer son système d'administration que d'acheter du « Zero Trust »).
- **ZT-02** [3.1] Évaluer le niveau de sécurité de chaque système par **audits techniques et organisationnels** pour mesurer l'écart à l'objectif.
- **ZT-03** [3.1] Utiliser d'abord les **solutions déjà disponibles** pour réduire la confiance implicite.

**§3.2.1 Identification des cas d'usage**
- **ZT-04** Identifier les cas d'usage où le Zero Trust apporte un gain de sécurité ; au minimum, ne **pas dégrader** la sécurité si la motivation est financière ou de performance.
- **ZT-05** Par cas d'usage : **inventaire détaillé et à jour** des utilisateurs, processus automatiques et équipements.
- **ZT-06** Établir de façon itérative la **cartographie détaillée** des composants du périmètre.
- **ZT-07** Identifier les **chemins d'accès** sujet→ressource (qui accède à quoi, pour quoi) et les scénarios d'accès.

**§3.2.2.1 Identifier et appliquer les attributs de sécurité**
- **ZT-08** Identifier tous les attributs (sujets, ressources, environnement) et leurs **valeurs ou plages autorisées**.
- **ZT-09** Identifier les **sources de données** et le mode de calcul des attributs dynamiques.
- **ZT-10** Définir les processus d'application des attributs, **à la création et sur l'existant**.
- **ZT-11** **Documenter** chaque attribut (sources, calcul, plages, périmètre couvert).

**§3.2.2.2 Disponibilité et qualité des données**
- **ZT-12** Disposer des données nécessaires aux attributs pertinents.
- **ZT-13** Être capable de **collecter** ces données et de les fournir au contrôle d'accès.
- **ZT-14** *(conformité)* Définir et maintenir les **versions de référence** (logiciels, durcissement, correctifs) par type d'équipement.
- **ZT-15** *(conformité)* Pouvoir collecter via **agents locaux** de conformité ou **scans centraux**.
- **ZT-16** *(menace)* S'assurer que les **journaux pertinents** peuvent être générés ou que les flux sont accessibles **en clair**.
- **ZT-17** *(menace)* Pouvoir capturer et analyser (**capteurs** réseau ou sur équipements).
- **ZT-18** *(menace)* S'assurer de la **fiabilité des alertes** (faibles faux positifs/négatifs), surtout en analyse comportementale. *Le renforcement détection/réponse ne justifie pas d'abandonner la défense en profondeur : le principe de précaution prévaut.*

**§3.2.2.3 Gestion des attributs dans le temps**
- **ZT-19** Utiliser des **référentiels uniques** gérés de façon centralisée (comptes utilisateurs, comptes administrateurs, ressources matérielles et logicielles).
- **ZT-20** Maintenir les référentiels de comptes et **désactiver automatiquement** tout compte considéré comme compromis.
- **ZT-21** Pouvoir **renouveler les secrets** de sujets et ressources (pour les certificats : **infrastructure de gestion de clés**).
- **ZT-22** Maintenir les équipements à jour : référentiel des correctifs + gestion **centralisée** des mises à jour.
- **ZT-23** Maintenir les référentiels de détection (IoC, modèles) + **veille CTI**.
- **ZT-24** Protéger en **authenticité et intégrité** les attributs au repos et en transit (cryptographie sur attributs/métadonnées). *BYOD : niveau d'assurance faible sur les valeurs remontées.*

**§3.2.3 Politique de contrôle d'accès — général**
- **ZT-25** Politique **uniquement sur des attributs maîtrisés** (maintenus à jour, couverture et qualité connues).
- **ZT-26** Inclure les attributs **itérativement**, du simple au complexe (analyse comportementale en dernier).
- **ZT-27** À chaque itération, **évaluer l'efficacité** du contrôle dynamique et ajuster la politique.
- **ZT-28** **Pondérer** les scores selon l'importance et la fiabilité de chaque attribut.
- **ZT-29** Bâtir la politique sur des **critères de conformité** ; le score de confiance n'est qu'un **critère supplémentaire**.
- **ZT-30** Définir pour chaque type d'équipement un **niveau de confiance implicite** (si le type n'est pas un critère de conformité).
- **ZT-31** Évaluations continues pour un score explicite ; le score d'un équipement **ne peut dépasser** sa confiance implicite. *Note 9 : un poste BYOD ne peut **en aucun cas** servir à l'administration, même si son évaluation semble intègre.*
- **ZT-32** Définir des **seuils** de score cohérents avec la criticité DIC des ressources.

**§3.2.3 — Robustesse de la preuve d'identité**
- **ZT-33** Tout accès (utilisateur, processus, équipement) identifié de façon **unique** et authentifié par un **certificat**.
- **ZT-34** Tout utilisateur utilise un **second facteur** déverrouillant la clé privée de son certificat.
- **ZT-35** Secret de type certificat protégé dans un **composant matériel dédié** ; **jeton physique** pour les utilisateurs.
- **ZT-36** **Pas d'authentification passive**.

**§3.2.3 — Équipements**
- **ZT-37** **BYOD = faible confiance** par défaut, accès limités aux services non critiques.
- **ZT-38** Administration depuis des postes à **confiance implicite élevée** (guide d'administration ANSSI PA-022 applicable, y compris pour administrer le plan de contrôle Zero Trust).

**§3.2.3 — Moindre privilège après authentification**
- **ZT-39** Après authentification, **canal sécurisé** (C, I, A cryptographiques).
- **ZT-40** Accès à privilège via **tunnel VPN IPsec** ; l'usage **exclusif** d'un reverse proxy Zero Trust **n'est pas recommandé** pour ces accès.
- **ZT-41** Accès utilisateurs aux services publics Internet via un **proxy Zero Trust**.

**§3.3 Acquisition, développement et maintenance**
- **ZT-42** Définir des **jalons intermédiaires**, cohérence des risques à chaque jalon.
- **ZT-43** Privilégier les **protocoles standards** (limiter la dépendance éditeur ou accepter le risque).
- **ZT-44** Vérifier la **compatibilité ABAC** des ressources, sinon prévoir développements ou solutions tierces.
- **ZT-45** S'assurer du **niveau d'assurance sécurité** des solutions acquises ou développées.
- **ZT-46** Campagnes de tests pour trouver les règles causant des **refus à tort**.
- **ZT-47** Tests de sécurité (**audits de configuration, tests d'intrusion**) pour trouver les règles **trop permissives**.
- **ZT-48** Prévoir une **durée d'apprentissage** conséquente pour les décisions comportementales.
- **ZT-49** Prévoir les moyens de **support utilisateurs** en cas de refus à tort et d'accompagnement au changement.

**§3.4 Architecture**
- **ZT-50** **Cloisonner le réseau** (logique ou physique) — reste nécessaire contre les attaques réseau.
- **ZT-51** Cloisonner **plan de contrôle et plan de données**.
- **ZT-52** Tout accès plan de données → plan de contrôle par **canal sécurisé à authentification mutuelle**.
- **ZT-53** **Chaîne d'accès d'administration distincte** de celle des utilisateurs.
- **ZT-54** **Redondance et synchronisation d'état** des équipements du plan de contrôle.
- **ZT-55** **Répartir et segmenter** les services de contrôle d'accès par type d'usage (limiter l'impact d'une défaillance).

**Total : 55 recommandations** (3 + 4 + 4 + 7 + 6 + 17 + 8 + 6).

## Chiffres et seuils à retenir

- **0** : niveau de confiance implicite dans le modèle théorique.
- **Score explicite ≤ confiance implicite** (du type d'équipement et des sources de calcul) — règle structurante.
- **6** critères de qualité des attributs ; **3** familles d'attributs (sujet / ressource / contexte) ; **3** blocs PDP/PIP/PEP ; **3** types de critères de décision (conformité, score simple, score complexe) ; **7** risques principaux (§2.5).
- Le document ne fixe **aucune valeur numérique** de seuil, de durée de session ou de période de réauthentification : il demande de les **définir selon la criticité DIC**.
- Normes citées : RGS annexes B1/B2/B3, NIST SP 800-162 (ABAC) et 800-207 (ZTA), CSA SDP v2.0, CISA ZTMM v2, guide ANSSI PG-078 (MFA), PA-022 (administration), EBIOS RM, IGI 1300.

## Application à PLÉIADE

Lecture : PLÉIADE a déjà plusieurs briques « Zero Trust compatibles » (IdP unique **Keycloak** OIDC, **reverse proxy Traefik** avec TLS de zone, **VPN Pritunl**). Le document invite à les **compléter**, pas à « acheter du Zero Trust ».

| Réf. | Statut | Ce que ça implique pour PLÉIADE | À vérifier |
|---|---|---|---|
| ZT-01/02 | **Applicable** | Faire une analyse de risques par zone (exercice = données fictives, mais l'infra, les comptes et la PKI sont réels). Prioriser l'administration avant tout gadget. | À vérifier : existe-t-il une analyse de risques écrite (EBIOS RM allégé) et un audit de l'état actuel ? |
| ZT-03 | **Applicable** | Exploiter à fond Keycloak (politiques de session, MFA, révocation), Traefik (middlewares), Pritunl avant d'ajouter un outil. | À vérifier : les fonctions de sécurité natives de Keycloak/Traefik sont-elles activées ou justifiées si désactivées ? |
| ZT-05/06/07 | **Applicable** | Inventaire par zone : comptes (gc01…), comptes de service, **clés X-API-Key**, conteneurs, postes animateurs, tablettes LEAC ; cartographie des flux inter-apps (eho ⇄ apps, MELMIL, LEAC sync). | À vérifier : une matrice « qui appelle quoi » (app → app, avec la clé utilisée) est-elle tenue à jour dans `PLEIADE\` ? |
| ZT-19 | **Applicable** | Keycloak = référentiel unique des identités humaines, eho = source d'identité des apps : éviter tout compte local parallèle dans une app. Séparer le référentiel des **comptes d'administration** (realm admin distinct ?). | À vérifier : aucune app n'a de base d'utilisateurs locale contournant Keycloak ; les admins ne sont pas dans le même realm que les joueurs. |
| ZT-20 | **Applicable** | Pouvoir désactiver d'un clic un compte de zone compromis et **révoquer ses sessions** actives (Keycloak « logout all sessions » + invalidation côté apps). | À vérifier : désactiver un compte dans Keycloak coupe-t-il effectivement l'accès à chaque app dans un délai connu (durée de vie des jetons / cookies de session) ? |
| ZT-21 | **Applicable** | Rotation des secrets : secrets clients OIDC, **X-API-Key** inter-apps, mots de passe MariaDB, CA de zone (IGC). | À vérifier : procédure écrite et testée de rotation des X-API-Key et de renouvellement des certificats de la CA de zone, avec durée de vie définie. |
| ZT-22 / ZT-14 | **Applicable** | Versions de référence des images Docker, de l'OS hôte, de Keycloak, Traefik, MariaDB ; mises à jour centralisées. | À vérifier : liste des versions déployées par zone comparée aux versions de référence ; délai de correction des CVE critiques. |
| ZT-24 | **Partiellement** | Les « attributs » PLÉIADE = rôles/groupes Keycloak transmis dans le jeton OIDC : ils doivent être **signés** et vérifiés par chaque app (pas lus en clair depuis un en-tête modifiable). | À vérifier : chaque app valide la signature et l'émetteur du jeton OIDC (JWKS de Keycloak) et ne fait jamais confiance à un en-tête d'identité ajouté en amont sans contrôle. |
| ZT-25/26/29 | **Applicable** | Politique d'accès sur attributs simples et maîtrisés (rôle de zone, groupe eho, appartenance à la zone). Pas de score comportemental. | À vérifier : la politique d'accès de chaque app est écrite et ne repose que sur des rôles/groupes Keycloak ou eho. |
| ZT-31 / ZT-37 / ZT-38 | **Applicable (important)** | Les postes animateurs « sur des réseaux de natures différentes » et non maîtrisés = **faible confiance** : accès joueur oui, **administration non**. Administrer PLÉIADE (serveur, Keycloak admin, app-admin, Traefik, BDD) uniquement depuis un poste maîtrisé. | À vérifier : l'interface d'administration Keycloak, `app-admin` et l'accès SSH au serveur sont-ils inaccessibles depuis les postes animateurs non maîtrisés ? |
| ZT-33/34/35 | **Partiellement** | Certificat + jeton matériel pour tous est irréaliste pour des joueurs anonymes (gc01…). À appliquer au moins aux **administrateurs** (FIDO2/WebAuthn dans Keycloak) et aux **processus** (mTLS entre services au lieu de seules X-API-Key). | À vérifier : MFA (idéalement WebAuthn/FIDO2) imposée sur les comptes admin Keycloak ; les appels inter-apps sont-ils authentifiés par plus qu'un secret statique partagé ? |
| ZT-36 | **Applicable** | Ne pas introduire d'authentification passive (ex. reconnaissance d'appareil seule). | À vérifier : aucun flux « se souvenir de cet appareil » ne remplace l'authentification. |
| ZT-39 | **Applicable** | TLS partout, y compris **entre conteneurs** si le réseau Docker n'est pas considéré comme sûr. | À vérifier : aucun flux applicatif en HTTP clair hors du réseau interne du serveur ; Traefik redirige 80→443. |
| ZT-40 | **Applicable** | Accès à privilège via **VPN** (Pritunl ; le document cite IPsec) et pas seulement via Traefik exposé. | À vérifier : SSH et consoles d'administration ne sont joignables **que** par le VPN d'administration, jamais par la seule exposition Traefik. |
| ZT-41 | **Hors champ** | PLÉIADE ne fournit pas l'accès Internet des postes. | — |
| ZT-43 | **Applicable** | Déjà aligné : OIDC, TLS, standards ouverts. | À vérifier : pas de mécanisme d'authentification propriétaire maison entre apps. |
| ZT-45 / ZT-47 | **Applicable** | Code développé en interne (Next.js) : revue de sécurité, analyse des dépendances npm, tests d'intrusion avant exercice. | À vérifier : un audit de dépendances (`npm audit` ou équivalent) et un test d'intrusion ont-ils été faits sur la version déployée ? |
| ZT-46 / ZT-49 | **Applicable** | Tester les refus à tort **avant** l'exercice (comptes gc, tablettes LEAC hors ligne puis resynchronisées) ; prévoir un support animateur. | À vérifier : une recette « tous les profils peuvent faire leurs actions » est jouée avant chaque ouverture de zone. |
| ZT-50/51 | **Applicable** | Cloisonner : réseau Docker par zone, plan de contrôle (Keycloak, Traefik dashboard, admin, BDD) séparé du plan de données (apps exposées aux joueurs). | À vérifier : les conteneurs d'une zone ne peuvent pas joindre ceux d'une autre zone ; MariaDB n'est pas exposée hors du réseau interne. |
| ZT-52 | **Applicable** | Apps → Keycloak/eho par canal TLS authentifié (validation du certificat CA de zone, pas de `rejectUnauthorized=false`). | À vérifier : aucun code ne désactive la vérification TLS (`NODE_TLS_REJECT_UNAUTHORIZED=0`, `rejectUnauthorized: false`). |
| ZT-53 | **Applicable (important)** | Chaîne d'administration ≠ chaîne utilisateurs : admin par VPN dédié + poste maîtrisé, joueurs par Traefik public de zone. | À vérifier : les URL d'administration ne sont pas servies par le même point d'entrée que les apps joueurs, ou sont filtrées par IP/VPN. |
| ZT-54/55 | **Partiellement** | Keycloak = point de défaillance unique : s'il tombe, toutes les apps tombent (risque « centralisation des décisions » §2.5). Prévoir sauvegarde/restauration rapide, voire mode dégradé (LEAC hors ligne le fait déjà côté terrain). | À vérifier : temps de restauration de Keycloak mesuré ; comportement des apps si Keycloak est indisponible. |
| ZT-08..11, ZT-16..18, ZT-23, ZT-28, ZT-30, ZT-32, ZT-48 | **Hors champ / différé** | Score de confiance dynamique, analyse comportementale, CTI : disproportionné pour une plateforme d'exercice. Retenir seulement la **journalisation** des authentifications (Keycloak events) et des appels inter-apps. | À vérifier : les événements de connexion Keycloak (succès/échec) sont conservés et consultables. |

## Limites / points d'attention

- **Recommandations non numérotées** par l'ANSSI : la numérotation ZT-nn est une convention CYBERSECU ; toujours citer aussi la section d'origine.
- Document **de principe** (« ni exhaustif ni détaillé ») ; aucun seuil chiffré, aucune stratégie de migration.
- Le cloisonnement **par conteneurs** et la **chaîne d'approvisionnement logicielle** sont explicitement **exclus** de la section protection des applications (§2.4.2.2) — or c'est le cœur de PLÉIADE : il faut d'autres référentiels pour cela.
- Les recommandations d'identité (certificat + jeton matériel pour tous) visent un SI d'entreprise ; elles ne sont pas transposables telles quelles aux **comptes anonymes de zone** — à réserver aux admins et aux flux machine.
- Le document met en garde contre le **faux sentiment de sécurité** : un « reverse proxy avec SSO » (Traefik + Keycloak) n'est **pas** à lui seul du Zero Trust, et ne suffit pas pour les accès à privilège (ZT-40).
- Mention de l'IGI 1300 (classifié) à titre d'exemple d'attributs : sans objet pour PLÉIADE (non classifié).
