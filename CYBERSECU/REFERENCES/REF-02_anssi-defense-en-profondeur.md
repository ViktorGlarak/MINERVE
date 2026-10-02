# REF-02 — Les Essentiels — Défense en profondeur – Mise en œuvre

- **Fichier** : `anssi_essentiels_defense_profondeur_mise_en_oeuvre_1.0.pdf` (source : `D:\CECPC\PLEIADE\DOC\CYBER SECU\`) · **Éditeur / référence** : ANSSI, collection « Les Essentiels » (contact : www.cyber.gouv.fr / conseil.technique@ssi.gouv.fr) — pas de numéro de référence · **Date / version** : V1.0 (07/26) — juillet 2026 · **Pages** : 2 · **Marquage** : public
- **Ingéré** : 2026-10-01

> Fiche de synthèse très courte (2 pages, format plaquette). Le titre « Mise en œuvre » laisse supposer un document compagnon sur les **principes** de la défense en profondeur ; il n'est pas dans ce fichier.

---

## En une phrase

La défense en profondeur consiste à empiler des **barrières** (protection avant / défense pendant / résilience après), chacune faite de plusieurs **mesures**, placées sur les composants du SI, et dont l'efficacité tient à leur **multiplicité**, leur **indépendance** et leur **robustesse** — illustré par un exemple anti-rançongiciel en 7 barrières.

## Ce que dit le document (synthèse structurée, fidèle)

**1. Vocabulaire**
- Une **barrière** = un **objectif de sécurité** répondant à **une étape d'un scénario de risque**.
- Une **mesure** = l'**unité élémentaire** (organisationnelle, technique ou opérationnelle) dont l'action contribue à l'objectif d'une barrière.

**2. Trois axes de mise en œuvre d'une barrière**
- **Rôle (« quoi »)** dans la couverture d'un scénario : **protection (avant)**, **défense (pendant)**, **résilience (après)**.
- **Placement (« où »)** sur les composants du SI : **utilisateurs, locaux, identités, réseaux, équipements, applications, données**.
- **Implémentation (« comment »)** : les mesures choisies pour atteindre l'objectif.

**3. Trois critères d'efficacité, à deux niveaux**
- Critères : **multiplicité, indépendance, robustesse**.
- Au niveau **des barrières** : des remparts **successifs et autonomes**, capables de s'opposer à **chaque étape** de progression de l'attaquant.
- Au niveau **des mesures** : chaque barrière est robuste et repose sur des mesures **variées, complémentaires**, sur des **socles technologiques distincts** ne partageant pas les mêmes faiblesses.

**4. Indépendance entre barrières — critère « particulièrement important »**
Une défaillance d'une barrière de **protection du SI de production** ne doit pas entraîner une **perte de visibilité depuis le SI de supervision**, ni compromettre les **barrières de résilience du SI d'administration**.

**5. Proportionnalité et non-exhaustivité**
Les mesures s'adaptent au **niveau d'exposition**, à la **criticité** et aux **scénarios de risque retenus**. L'exemple ne traite **qu'un seul scénario** (rançongiciel) : il n'est pas exhaustif, doit être adapté au contexte et complété pour couvrir l'ensemble des scénarios.

---

## Toutes les recommandations / mesures

### A. Principes (p. 1)

- **P1** — Déployer des **barrières complémentaires**, chacune constituée d'un **ensemble de mesures**.
- **P2** — Définir chaque barrière selon son **rôle** (protection / défense / résilience), son **placement** (utilisateurs, locaux, identités, réseaux, équipements, applications, données) et son **implémentation** (mesures).
- **P3** — Assurer **multiplicité, indépendance, robustesse** au niveau des **barrières** (remparts successifs et autonomes à chaque étape d'attaque).
- **P4** — Assurer les mêmes critères au niveau des **mesures** (variées, complémentaires, sur socles technologiques distincts).
- **P5** — Garantir l'**indépendance entre barrières de protection, de défense et de résilience** (production ≠ supervision ≠ administration).
- **P6** — Adapter les mesures à l'**exposition**, à la **criticité** et aux **scénarios de risque retenus** ; couvrir **tous** les scénarios, pas un seul.

### B. Exemple de mise en œuvre — protection contre un rançongiciel (§ 1, p. 1-2)

Format d'origine : « → Barrière (rôle, composant) » puis « > mesures ».

**Barrière 1 — Détecter et bloquer les tentatives d'hameçonnage** (défense, réseau)
- 1a. Maintenir à jour les **règles de détection**.
- 1b. Analyser les courriels **statiquement par signature** et **dynamiquement en sandbox**.
- 1c. Utiliser une **passerelle entrante** réalisant ces analyses **en amont** du serveur de courriels.

**Barrière 2 — Limiter la vraisemblance qu'un utilisateur exécute un logiciel malveillant** (protection, utilisateur)
- 2a. **Sensibiliser régulièrement** sur les tentatives d'hameçonnage.
- 2b. Tester le comportement des utilisateurs par des **campagnes internes d'hameçonnage**.

**Barrière 3 — Limiter les capacités d'un attaquant à installer des outils** (protection, équipement)
- 3a. Limiter les droits des utilisateurs selon le **moindre privilège** sur leurs postes (ex. pas de droits d'administration).
- 3b. Assurer que les **correctifs de sécurité** des postes sont à jour.

**Barrière 4 — Détecter et bloquer l'installation de logiciels malveillants** (défense, équipement)
- 4a. **Analyse comportementale** sur les postes utilisateurs (ex. **EDR**).
- 4b. Mise à jour des **règles de détection** sur les postes.

**Barrière 5 — Limiter les capacités d'un attaquant à établir un canal de commande/contrôle vers Internet** (protection, réseau)
- 5a. **Serveur mandataire** pour les accès Internet et **résolveur DNS** pour les domaines publics **en DMZ**, rendus **non contournables par défaut**.
- 5b. Maintenir à jour les **règles de filtrage**.

**Barrière 6 — Limiter les capacités de latérisation par compromission d'un compte à privilèges sur le poste** (protection, identité)
- 6a. **Comptes d'administration dédiés** aux postes utilisateur.
- 6b. **Audits réguliers du service d'annuaire central**.

**Barrière 7 — Pallier la perte de données** (résilience, donnée)
- 7a. **Sauvegarde** des données avec **au moins une copie hors ligne**.
- 7b. **Tester régulièrement** les procédures de sauvegarde **et de restauration**.

### C. Exemples de barrières génériques (§ 2, tableau p. 2)

| Barrière générique | Composant | Multiplicité des mesures | Indépendance des mesures | Robustesse des mesures |
|---|---|---|---|---|
| **G1 — Protection : authentification utilisateur** | Identité | Authentification **multi-facteur** | **Jeton physique indépendant** du poste d'accès au SI | Authentification par **défi-réponse cryptographique** ; **dimensionnement approprié des secrets** |
| **G2 — Défense : analyse par anomalie des flux** | Réseau | **Plusieurs points** de collecte et d'analyse des flux | **Centralisation des alertes sur des serveurs dédiés et séparés de la production** ; **sondes derrière des TAP physiques** | **Règles de détection à jour** ; **fiabilisation des alertes** |
| **G3 — Résilience : site de repli à froid** | Tous (ou juste le SI) | **Redondance des fonctions critiques** nécessaires à la continuité d'activité | **Indépendance complète** des composants du repli à froid vis-à-vis de la production | **Test régulier** des procédures de repli ; **MCS** des composants du repli |

**Décompte** : 6 principes + 7 barrières / 14 mesures (exemple rançongiciel) + 3 barrières génériques (11 exemples de mesures dans le tableau).

---

## Chiffres et seuils à retenir

| Élément | Valeur |
|---|---|
| Rôles d'une barrière | **3** : protection (avant), défense (pendant), résilience (après) |
| Composants de placement | **7** : utilisateurs, locaux, identités, réseaux, équipements, applications, données |
| Critères d'efficacité | **3** : multiplicité, indépendance, robustesse — appliqués à **2** niveaux (barrières, mesures) |
| Sauvegarde | **au moins une copie hors ligne** |
| Exemple traité | **1** seul scénario (rançongiciel), **7** barrières, **14** mesures |
| Aucun seuil temporel chiffré | les fréquences restent qualitatives (« régulièrement », « à jour ») |

---

## Application à PLÉIADE

> Statut : **Applicable** · **Partiellement** · **Hors champ**. Les « À vérifier » sont des contrôles à réaliser, non exécutés lors de l'ingestion.

### Principes

| Réf. | Statut | Ce que ça implique pour PLÉIADE | À vérifier |
|---|---|---|---|
| P1-P2 | Applicable | Décrire la sécurité d'une zone comme une **matrice barrières × composants** : identités (Keycloak/eho), réseaux (VPN, Traefik, réseaux Docker), équipements (serveur, postes animateurs, tablettes LEAC), applications (apps Next.js, clés `X-API-Key`), données (MariaDB, volumes, stockage local tablette), utilisateurs (animateurs, joueurs `gc01…`), locaux (emplacement du serveur sur le terrain). | À vérifier : une matrice « barrière / rôle / composant / mesures » existe pour PLÉIADE, au moins pour les scénarios prioritaires. |
| P3 | Applicable | Chaque étape d'une attaque type doit rencontrer un rempart : accès (VPN) → authentification (Keycloak + MFA) → autorisation (rôles vérifiés côté serveur) → mouvement latéral (réseaux par zone, `X-API-Key` par app) → données (moindre privilège MariaDB, sauvegardes). | À vérifier : pour un scénario « vol d'identifiants d'un compte de zone », lister la barrière qui arrête l'attaquant à chaque étape. |
| P4 | Applicable | Ne pas reposer sur **un seul socle** : ex. VPN **et** OIDC (pas « le VPN suffit, donc l'API est ouverte ») ; `X-API-Key` **et** filtrage réseau entre conteneurs. Éviter qu'une même faiblesse (ex. la CA de zone ou un secret partagé) fasse tomber toutes les barrières à la fois. | À vérifier : aucune API interne ne fait confiance à la seule provenance réseau (« derrière le VPN donc autorisé ») ; chaque app a sa propre clé de service, non partagée. |
| P5 | Applicable (essentiel) | **Séparer production, supervision et administration** : les journaux (Traefik, Keycloak, apps) doivent survivre à la compromission d'un conteneur applicatif ; les **sauvegardes** et l'**accès d'administration** ne doivent pas être joignables ni effaçables depuis la production ; la console d'administration et la CA de zone hors du chemin joueurs. | À vérifier : un attaquant root dans un conteneur d'app ne peut ni effacer les logs ni atteindre les sauvegardes ni la clé privée de la CA ; les sauvegardes sont stockées hors du serveur de zone. |
| P6 | Applicable | Proportionner : zone d'entraînement à contenu fictif ≠ zone portant des données réelles ou sensibles ; mais traiter **tous** les scénarios retenus (rançongiciel, fuite de données d'exercice, perte de tablette, compromission de la chaîne de déploiement GitHub, usurpation d'identité de zone). | À vérifier : liste des scénarios de risque retenus pour PLÉIADE (lien avec REF-01 mesure 41 / EBIOS). |

### Exemple rançongiciel transposé

| Barrière | Statut | Transposition PLÉIADE | À vérifier |
|---|---|---|---|
| 1 — Hameçonnage (défense, réseau) | Partiellement | Concerne surtout les **postes animateurs** et les comptes **GitHub/Keycloak admin** (messagerie réelle hors plateforme). Dans l'app messagerie d'exercice : filtrer pièces jointes et liens. | À vérifier : l'app messagerie limite les types de pièces jointes et ne permet pas de liens exécutables. |
| 2 — Exécution par l'utilisateur (protection, utilisateur) | Partiellement | Sensibiliser animateurs et développeurs (hameçonnage visant leurs accès GitHub, Pritunl, Keycloak). | À vérifier : brief sécurité aux animateurs à l'ouverture de zone. |
| 3 — Installation d'outils (protection, équipement) | Applicable | Moindre privilège : postes animateurs et tablettes **sans droits admin** ; conteneurs **non root**, système de fichiers en lecture seule si possible ; correctifs à jour (OS, images, npm). | À vérifier : `USER` non root et `read_only` dans les définitions de conteneurs ; tablettes sans mode développeur/root. |
| 4 — Détection d'installation (défense, équipement) | Partiellement | EDR/antivirus sur postes Windows (unité) ; sur le serveur, détection d'anomalies (intégrité des images, processus inattendus dans les conteneurs). | À vérifier : un mécanisme signale un conteneur dont l'image ou le processus diffère du déploiement attendu. |
| 5 — Canal C2 vers Internet (protection, réseau) | Applicable | **Restreindre les sorties** des conteneurs et du serveur (pas d'accès Internet libre) ; DNS maîtrisé ; en zone isolée/terrain, idéalement aucune sortie. | À vérifier : un `curl` vers un domaine externe depuis un conteneur d'app est bloqué (hors besoins listés). |
| 6 — Latérisation via compte à privilèges (protection, identité) | Applicable | **Comptes admin dédiés et nominatifs**, distincts des comptes de jeu ; **audit régulier de l'annuaire** = revue des realms Keycloak / d'eho (rôles admin, clients OIDC, comptes orphelins). | À vérifier : revue Keycloak à chaque zone (comptes admin, clients, secrets, sessions) consignée. |
| 7 — Perte de données (résilience, donnée) | Applicable | Sauvegardes MariaDB + volumes + realms + CA avec **une copie hors ligne** ; **restauration testée** ; pour LEAC, conserver les données locales jusqu'à confirmation de synchronisation. | À vérifier : dernier test de restauration complet d'une zone (date, résultat) ; la tablette ne purge ses notations qu'après accusé de réception du serveur. |

### Barrières génériques transposées

| Barrière | Statut | Transposition PLÉIADE | À vérifier |
|---|---|---|---|
| G1 — Authentification utilisateur | Applicable | Keycloak : **MFA** pour les rôles privilégiés (TOTP ou mieux, clé physique **FIDO2/WebAuthn** = défi-réponse cryptographique sur jeton indépendant du poste) ; secrets correctement dimensionnés (mots de passe, `X-API-Key` aléatoires et longues). | À vérifier : politique OTP/WebAuthn sur les comptes admin ; longueur et entropie des clés `X-API-Key` générées. |
| G2 — Analyse par anomalie des flux | Partiellement | Collecter à plusieurs points (Traefik, Keycloak, VPN) ; **centraliser les alertes hors du serveur de production** ; règles de détection simples (pics d'échecs de connexion, `X-API-Key` refusées, volumes d'export anormaux). TAP physique peu réaliste en zone terrain. | À vérifier : les journaux et alertes sont copiés en continu hors de l'hôte applicatif. |
| G3 — Site de repli à froid | Partiellement | Capacité à **reconstruire une zone** ailleurs à partir de GitHub (code) + sauvegardes (données) + secrets, avec composants **indépendants** de la production ; tester la procédure. | À vérifier : procédure de reconstruction d'une zone sur un second serveur, chronométrée, testée au moins une fois. |

**Hors champ** : passerelle de messagerie d'entreprise et sandbox de courriels (barrière 1, sauf messagerie d'exercice), EDR des postes de l'unité (barrière 4 : relève de l'unité), TAP physiques (G2) sur infrastructure qui n'appartient pas à PLÉIADE.

---

## Limites / points d'attention

- **Document très court (2 pages)** : c'est une plaquette de mise en œuvre, sans définitions longues ni référentiel de conformité ; aucun seuil temporel chiffré.
- **Un seul scénario** traité (rançongiciel) — le document le dit explicitement ; il ne doit pas servir de liste de contrôle exhaustive.
- Orienté **SI d'entreprise** (courriel, postes, annuaire central, EDR) : la transposition aux conteneurs, à l'OIDC, aux clés de service et aux tablettes hors ligne est une **interprétation** de CYBERSECU.
- Le texte source comporte des coquilles (« niveau exposition », « pour atteinte l'objectif ») ; le sens retenu est celui, évident, de « niveau d'exposition » et « atteindre l'objectif ».
- Le titre « Mise en œuvre » suggère un document compagnon (principes de la défense en profondeur) **non fourni** ici.
- Se lit **avec REF-01** : les barrières 3, 6, 7 recoupent les mesures 29, 8/5, 37 du guide d'hygiène.
