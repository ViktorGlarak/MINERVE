# REF-10 — Recommandations pour la sécurisation des sites web

- **Fichier** : `20130422-NP_Securite_Web_NoteTech.pdf` (source : `D:\CECPC\PLEIADE\DOC\CYBER SECU\`) · **Éditeur / référence** : ANSSI (SGDSN), note technique **N° DAT-NT-009/ANSSI/SDE/NP** · **Date / version** : 22 avril 2013, version 1.0 (« Version initiale ») · **Pages** : 23 (dont couverture ; pagination interne « Page x sur 22 ») · **Marquage** : suffixe **« NP »** dans la référence (= Non Protégé) ; mention « diffusable sans restriction », régime « Licence ouverte » Etalab. ⚠ Le mot « public » n'apparaît pas tel quel : c'est « NP / diffusable sans restriction » — document public au sens de la diffusion.
- **Public visé (coché)** : Développeur, Administrateur, RSSI (DSI et Utilisateur non cochés).
- **Ingéré** : 2026-10-01
- **Rédigé par** : DAT · **Approuvé par** : SDE · **Contributeurs** : BSS, BAS, BAI, FRI, LAM.

> ⚠ **Note historique** : cette note est la **v1.0** du document refondu en 2021 sous la référence **ANSSI-PA-009 v2.0** (voir **REF-11**, dont l'historique indique : 1.0 du 22/04/2013, 1.1 du 13/08/2013, 2.0 du 28/04/2021). En cas de divergence, **REF-11 fait foi** pour la partie navigateur ; REF-10 reste utile pour l'**infrastructure, l'administration, la journalisation et la réaction à incident**, que REF-11 ne traite plus.

---

## En une phrase

Note de 2013 listant **29 recommandations** (R1 à R29) pour durcir un site web à trois niveaux — **infrastructure** (défense en profondeur, moindre privilège, administration sécurisée, filtrage, TLS/HSTS), **code applicatif** (traitements côté serveur, requêtes préparées, échappement contextuel, redirections et inclusions en liste blanche, sessions, mots de passe salés, anti-CSRF, X-Frame-Options) et **réaction** (point de contact, surveillance, intégrité, journalisation déportée, conduite à tenir).

---

## Ce que dit le document (synthèse structurée, fidèle)

### 1. Avant-propos — la menace
- Sites web = éléments **très exposés**. Menaces les plus connues : **défiguration** (remplacer le contenu légitime : message politique, dénigrement, revendication) et **déni de service** (indisponibilité). Impact : déficit d'image, manque à gagner.
- Scénarios **plus insidieux et discrets**, pouvant rester insoupçonnés longtemps : site utilisé comme **porte d'entrée** vers le SI de l'hébergeur/propriétaire, comme **relais** d'attaque vers un tiers, comme **dépôt de contenus illégaux**, ou comme **piège pour les clients habituels** (souvent employés et partenaires). **Externaliser l'hébergement ne transfère pas tous les risques.**
- Protection = **mesures préventives + mécanismes de détection**.

### 2. Prévention
Liste « aucunement exhaustive », à adapter au contexte.

#### 2.1 Infrastructure
**2.1.1 Architecture**
- **Défense en profondeur** : plusieurs mesures indépendantes ; découper en éléments nettement séparés aux interactions bien définies, chacun avec ses propres mécanismes. Architectures **n-tiers** adaptées, à condition de **ne pas concentrer la sécurité sur le tiers présentation** : chaque composant assure sa propre protection. Découpage idéalement matériel/logiciel réel : machines distinctes filtrées, ou cloisonnement sur une même machine (processus distincts, confinement type vServer, LXC…). → **R1**.
- **WAF** (pare-feu applicatif web) : barrière **supplémentaire**, ne dispense **en aucun cas** de sécuriser le site. Formes : COTS réseau, ou logiciel greffé sur le serveur web / un **reverse proxy** (ex. open source : ModSecurity pour Apache/IIS/Nginx, Naxsi pour Nginx). Modèle **négatif** (liste noire de signatures) ou **positif** (liste blanche du fonctionnement légitime) — le **positif** est généralement plus sûr mais plus complexe.
- **Composants logiciels** : OS, serveur web, CMS et greffons, bibliothèques Java/PHP/.NET, SGBD, modules… De nombreuses attaques exploitent les **composants tiers**, pas le code spécifique — particulièrement regrettable quand le composant est **présent mais inutilisé**. → **R2, R3**.
- **Mécanismes d'administration** : exposition à limiter ; privilégier **SSH/SFTP** ; **FTP à proscrire** (ne protège ni mots de passe ni contenu). Interface web d'administration → **HTTPS**. Exemple Apache : n'autoriser les `Location` d'administration que dans les virtualhosts `SSLEngine on` (`Order allow,deny` + `Deny from all` dans les virtualhosts non TLS), voire un virtualhost HTTPS dédié ; si le site n'est pas tout en HTTPS, **cookie de session distinct et sécurisé pour l'administration** (sinon vol de session quand l'admin navigue en HTTP) ; `SSLVerifyClient require` pour exiger un **certificat client** si une IGC existe. → **R4**.
- Restreindre l'accès aux **seuls postes d'administration autorisés** : idéalement **réseau d'administration** sur interface dédiée, sinon **VPN IPsec**, a minima **filtrage réseau** — mais **l'adresse IP n'est pas un identifiant fiable** (usurpation crédible) ; premier rempart contre les attaques génériques seulement. Interfaces d'admin web : redoubler de vigilance (contrôle d'accès, traçabilité), **authentification mutuelle TLS** possible ; à défaut mot de passe sous TLS respectant les bonnes pratiques ANSSI. Exemple Tomcat manager : supprimer les comptes par défaut, groupe « manager » dédié (`tomcat-users.xml`), connecteur sécurisé dans `server.xml` (`<Connector port="8443" protocol="HTTP/1.1" SSLEnabled="true" maxthreads="150" scheme="https" secure="true" clientAuth="false" sslProtocol="TLS" />`), forcer `<transport-guarantee>CONFIDENTIAL</transport-guarantee>` dans `web.xml`, filtrage IP via `org.apache.catalina.valves.RemoteAddrValve`. → **R5, R6**.
- **Disponibilité** : contre les attaques élémentaires, mises à jour + bonne gestion de la **complexité des traitements déclenchables par les requêtes** ; haute dispo classique (répartition de charge). Contre les **DDoS** : solutions spécifiques opérateur / **CDN** / prestataires (renvoi CERTA-2012-INF-001). À moindre coût : **fail2ban** — mais à double tranchant (un attaquant peut faire bannir le relais sortant d'une entité regroupant de nombreux clients légitimes → DoS).

**2.1.2 Configuration**
- **Moindre privilège** partout (→ **R7**) : serveur HTTP sous **compte non privilégié**, confiné (chroot, lxc, apparmor) ; filtrage en **modèle positif** (rejet par défaut). Contre-exemple JBoss 4.2/4.3 : contrainte de sécurité sur la console JMX limitée aux méthodes `GET` et `POST` → contournable par `HEAD` ou `PUT` ; correction : supprimer les éléments `http-method` pour couvrir toutes les méthodes.
- **Fichiers servis** limités au strict nécessaire (→ **R8**) : garder hors de l'arborescence web fichiers d'installation, doc, configuration ; compte du serveur web **sans droit de lecture (ni d'écriture !)** sur ce qui ne le concerne pas (ACL POSIX / DACL Windows) ; règles d'accès dans la configuration du serveur. Apache : préférer la config générale aux `.htaccess`, et `AllowOverride None`. Protéger **clés privées** et fichiers de configuration ; cloisonner les rôles des exploitants. Exécution CGI limitée à un répertoire identifié (`ScriptAlias`, aucun autre répertoire avec `ExecCGI`).
- **SGBD** (→ **R9**) : l'utilisateur applicatif n'a pas à modifier le schéma ; `UPDATE`/`DELETE`/`INSERT` seulement sur les tables/colonnes nécessaires, `SELECT` seul ailleurs ; comptes SGBD distincts par composant, voire par profil client (ex. deux connexions : client authentifié / non authentifié) — limite l'impact d'une compromission partielle, voire empêche certaines attaques (ex. XSS stockées).
- **Fuites d'informations** (→ **R10**) — protection à ne pas surestimer, mais utile contre l'automatisé : supprimer les balises `meta` indiquant le générateur ; supprimer les mentions visibles d'outils (CMS, éditeur) ; limiter en production le **débogage dans les messages d'erreur** (ex. ne pas renvoyer la requête SQL) ; **pages d'erreur personnalisées** ; dans certains cas **404 générique** plutôt que 401/403/405 ; **banaliser les en-têtes HTTP** révélant versions serveur/OS ; **désactiver le listage des répertoires** ; **rejeter `TRACE`** en production.
- **Filtrage réseau** (→ **R11**) : pare-feu local (+ externe si possible) ; **règles restrictives en sortie** (quelques flux d'infrastructure : mises à jour, NTP, export de journaux — ports et destinations explicites) ; en entrée, flux métier vers 80/443, flux spécifiques listés exhaustivement.
- **TLS** : HTTPS dès que confidentialité ou intégrité nécessaires (identifiants, données personnelles, paiement) ; dimensionnement crypto selon le **RGS** ; **TLS sur tout le site**, pas seulement les parties « sensibles » (sinon vol de session). Exemple Apache mod_ssl (« au moment de la rédaction ») : `SSLCiphersuite ALL:!SSLv2:!ADH:!RC4:!RC2:!MD5:!EXPORT:!ANON:!DES:!aNULL:!eNULL` ; sur un parc client délimité (intranet), imposer les meilleurs algorithmes, conformes au RGS si possible.
- **HSTS** : `Strict-Transport-Security: max-age=31536000; includeSubDomains` — protège contre la bascule en clair **à double condition** (navigateur compatible, attaquant absent du **premier échange**) → mesure **supplémentaire à coût quasi nul**, **pas une garantie** contre l'homme du milieu. *(Pas de numéro R dans la note 2013.)*

#### 2.2 Code applicatif du site
L'infrastructure ne suffit **en aucun cas**. Principe général → **R12** : tout traitement côté serveur, aucune vérification déléguée au client ; le JavaScript client peut contrôler par ergonomie, mais partir du postulat qu'il **n'a pas pu s'exécuter**.

**2.2.1 Gestion des entrées** — toutes les entrées sont manipulables : variables GET/POST, **champs cachés**, champs calculés par script client, **en-têtes HTTP (cookies, identifiants de session)**. L'attaquant maîtrise totalement son poste.
- **Injections SQL** → **R13** : couche d'abstraction ou **requêtes préparées fortement typées** (Java `java.sql.PreparedStatement` / `Connection.prepareStatement` ; PHP `PDO::prepare` ; ASP.NET `SqlCommand.Prepare`). « **magic quotes** » PHP : **fortement déconseillé**. `mysqli_real_escape_string` : préférable mais **non recommandé** (couplage à la techno SGBD, oubli des variables numériques).
- **XSS** (réfléchi via variable GET + lien piégé ; **XSS stocké** via commentaires touchant tous les visiteurs) → **R14** : échappement **adapté au contexte** + vérification de forme. PHP `htmlspecialchars` = contexte (X)HTML uniquement, **inutile** en contexte JavaScript, CSS, URL ; parfois plusieurs échappements successifs dans un ordre réfléchi.
- **Redirections** (open redirect, ex. paramètre GET de retour après authentification ; codes 301, 302, 303, 307 ou JavaScript) → hameçonnage très efficace → **R15, R16** : redirections statiques ; sinon liste blanche, par **index/étiquettes** si la liste est finie, sinon expression rationnelle et **vérification du nom de domaine** contre une liste blanche.
- **Inclusion de fichiers** (ex. `include( $_GET['id'] . '.php');` détourné en inclusion distante, ou traversée d'arborescence) → **R17** ; si inévitable : index en liste blanche ou contrôle strict de forme.
- **Autres injections** (LDAP, XPath, XML, commande shell…) → **R18** ; **fichiers téléversés** (upload) à manipuler « avec la plus grande précaution » (contenus malveillants ou illégaux).

**2.2.2 Logique applicative**
- **Sessions** : identifiant dans `Cookie` (posé par `Set-Cookie`) — intrinsèquement fragile : un cookie contrefait suffit à usurper (« vol de session »). → **R19** (aléa ≥ 128 bits), **R20** (HTTPS dès qu'une session porte des privilèges ; TLS sur la seule page de login protège le mot de passe, **pas l'identifiant de session**), **R21** (`HttpOnly` + `Secure`). Exemples : PHP `session.cookie_secure` / `session.cookie_httponly` ; Tomcat 6/7 `useHttpOnly="true"` sur `Context` ; `secure` auto en HTTPS **sauf derrière un reverse proxy** qui termine TLS → le poser à la main (code Java ou réécriture sur le proxy, ex. Apache `mod_headers` : `Header edit Set-Cookie ^(.)$ $1;Secure`).
  - **Identifiant de session dans l'URL (GET) : à proscrire.**
  - Durcissements : durée de validité courte ; **réauthentification** pour opérations sensibles si session ancienne ; surveiller l'IP du client (réauth si changement, au moins pour le sensible) ; en authentification mutuelle, vérifier l'association session ↔ certificat client à chaque requête.
  - Gestion des droits : comptes nominatifs, **vérification systématique des autorisations** à chaque accès à une ressource protégée, changement régulier des authentifiants, cycle de vie formalisé des comptes.
  - **URL prévisibles** : ne jamais compter sur le secret d'une URL (circulent en clair, indexées, historiques, journaux) ; `doc?id=42` → l'attaquant essaiera 41, 43 (IDOR).
- **Stockage des mots de passe** → **R22, R23** : fonction non réversible conforme RGS + **sel aléatoire** ; défense en profondeur protégeant surtout les utilisateurs qui réutilisent leurs mots de passe, et donnant du temps pour détecter et alerter.
- **Requêtes illégitimes (XSRF)** : l'attaque « rebondit » souvent sur un site tiers vulnérable ; tout site y est exposé. Contre-mesures : cycle de vie des sessions (expiration, réauth) ; contrôle du **Referer** (falsifiable, ne contre que l'élémentaire ; ex. changement de mot de passe accepté seulement depuis la page de gestion du compte) ; **jetons aléatoires** (générés et stockés côté serveur, champ caché, à usage unique et récent ; transposable aux liens GET). **Clickjacking** : `X-Frame-Options: DENY` ou `X-Frame-Options: SAMEORIGIN` sur chaque élément servi. → **R24**.
- **Inclusion de contenus externes** (publicités, statistiques, scripts, cartographie, réseaux sociaux) : augmente la surface d'attaque (compromission du fournisseur B → diffusion de code malveillant par A) et **fuite d'informations** (ex. un intranet appelant un service externe transmet l'URL visitée, ex. `.../projet-de-fusion-avec-foobar.php`). → **R25**.
- **Paradigme statique** : le dynamique élargit la surface d'attaque ; rendre statique ce qui peut l'être (CMS dynamique en préproduction, publication statique en production, ex. `wget -r`) ; **figer en statique les sites archivés** (moins surveillés, cibles privilégiées). → **R26**.

### 3. Réaction
- **3.1 Méta-informations** : WHOIS permettant de joindre un responsable ; enregistrement **SOA** DNS avec adresse électronique valide. → **R27**.
- **3.2.1 Surveillance** → **R28** : parcourir régulièrement le site ; certaines défigurations sont **discrètes** (pages légitimes servies aux IP de l'organisme, pages compromises aux autres) → veiller depuis un **accès Internet « démarqué »** à adresse dynamique (ex. 3G). Moteurs de recherche + alertes (ex. `hack`, `warez` + `site:example.org`). **Contrôle d'intégrité** des répertoires et de la configuration (TripWire, AIDE ; listings `mtree` stockés hors serveur) ; toute apparition/modification inattendue déclenche une investigation. La **supervision** métier sert aussi la sécurité (détection précoce de DoS).
- **3.2.2 Journalisation** → **R29** : politique écrite (modalités, durées de conservation, analyse, corrélation) ; journaux **transmis hors du serveur** (ex. syslog) contre l'altération rétroactive ; journaliser IP, horodatage, URL, codes d'erreur **+ Referer + User-Agent** (Apache `LogFormat` avec `%{Referer}i` et `%{User-agent}i`) ; **corréler** avec les autres journaux (connexions aux interfaces d'admin, pare-feu local, redémarrages) ; adapter aux ressources et au contexte ; auditd (Linux) / SACL (Windows) pour tracer finement l'accès à des ressources sensibles (ex. clé privée du certificat serveur).
- **3.3 Conduite à tenir** : rassembler et **préserver les preuves** (obtenir vite les journaux chez un hébergeur externe) ; remettre en service un site **sans élément malveillant** et **sans la vulnérabilité exploitée** ; prudence avec la **restauration de sauvegarde** ; renvoi CERTA-2012-INF-002 ; se faire assister (CERT, police…).

### 4. Compléments
Guides et bulletins des fournisseurs ; **OWASP** (« Secure coding practices quick reference guide », « Top 10 ») ; guides ANSSI (bonnes pratiques) ; CERTA pour l'actualité des vulnérabilités.

---

## Toutes les recommandations

> Numérotation d'origine, **29 recommandations (R1 → R29)**. Texte de la recommandation en gras (reformulé au plus près), puis contenu concret tiré du document.

| N° | Recommandation | Contenu concret / valeurs |
|---|---|---|
| **R1** | L'architecture matérielle et logicielle du site et de son hébergement doit respecter la **défense en profondeur**. | Composants séparés aux interactions définies, chacun protégé ; pas de sécurité concentrée sur le tiers présentation ; machines distinctes filtrées ou confinement (processus, vServer, LXC) ; WAF en barrière **supplémentaire** (positif > négatif). |
| **R2** | Les composants applicatifs doivent être **limités au strict nécessaire**. | Supprimer greffons/modules inutiles (le présent-mais-inutilisé est le pire cas). |
| **R3** | Les composants applicatifs doivent être **recensés et maintenus à jour**. | Inventaire + mises à jour (OS, serveur, CMS, bibliothèques, SGBD, modules). |
| **R4** | L'administration doit se faire via des **protocoles sécurisés**. | SSH/SFTP ; **FTP proscrit** ; admin web en HTTPS ; cookie d'admin distinct et `Secure` si le site n'est pas tout HTTPS ; option certificat client (`SSLVerifyClient require`). |
| **R5** | Accès aux mécanismes d'administration **restreint aux seuls postes d'administration autorisés**. | Réseau d'admin / interface dédiée, sinon VPN IPsec, a minima filtrage IP (IP ≠ identifiant fiable) ; ex. Tomcat `RemoteAddrValve`. |
| **R6** | Les administrateurs doivent être **authentifiés de manière sûre**. | Authentification mutuelle TLS (certificats client et serveur) ; sinon mot de passe sous TLS conforme ANSSI ; suppression comptes par défaut ; `transport-guarantee CONFIDENTIAL`. |
| **R7** | **Moindre privilège** sur l'ensemble des éléments. | Serveur HTTP non privilégié + confinement (chroot, lxc, apparmor) ; filtrage positif (rejet par défaut) ; piège des contraintes listant des méthodes HTTP (JBoss GET/POST contourné par HEAD/PUT). |
| **R8** | Fichiers servis **limités au strict nécessaire**. | Hors arborescence web : install, doc, config ; ACL ; `AllowOverride None` ; protéger clés privées ; CGI dans un seul répertoire. |
| **R9** | Droits sur la base de données **gérés finement**. | Pas de droits sur le schéma ; INSERT/UPDATE/DELETE ciblés ; SELECT seul ailleurs ; comptes SGBD distincts par composant / profil client. |
| **R10** | **Limiter les renseignements** sur le fonctionnement technique. | Supprimer `meta` générateur et mentions d'outils ; pas de débogage en prod ; pages d'erreur personnalisées ; 404 générique si utile ; banaliser les en-têtes de version ; pas de listage de répertoires ; rejet `TRACE`. |
| **R11** | **Matrice des flux** précise (entrée/sortie) imposée par filtrage réseau. | Sortant restreint (mises à jour, NTP, export journaux — ports/destinations explicites) ; entrant 80/443 + flux spécifiques listés. |
| **R12** | **Tous les traitements côté serveur** ; entrées client non fiables ; aucune vérification déléguée au client. | Le contrôle JS client n'est qu'ergonomique ; supposer qu'il n'a pas tourné. |
| **R13** | Requêtes BDD via **requêtes préparées fortement typées** ou couche d'abstraction contrôlant les paramètres ; sinon échappement des caractères spéciaux + contrôle de forme. | `PreparedStatement`, `PDO::prepare`, `SqlCommand.Prepare` ; magic quotes fortement déconseillées ; `mysqli_real_escape_string` non recommandé. |
| **R14** | Données externes dans la réponse : **échappement adapté au contexte d'interprétation** + vérification de forme. | `htmlspecialchars` = HTML seulement ; contextes JS/CSS/URL différents ; échappements successifs ordonnés. |
| **R15** | **Favoriser les redirections statiques**. | Éviter les redirections pilotées par une donnée externe. |
| **R16** | Redirections dynamiques **en liste blanche**. | Index/étiquettes si liste finie ; sinon regex + vérification du **domaine** en liste blanche. |
| **R17** | **Ne pas inclure de fichiers** dont nom/chemin dépend d'une donnée externe. | Sinon index en liste blanche / contrôle strict ; risque RFI et traversée de répertoires. |
| **R18** | **Liste blanche ou traitement rigoureux** des données externes à chaque emploi. | LDAP, XPath, XML, shell… ; **fichiers téléversés** avec la plus grande précaution. |
| **R19** | Identifiants de session **aléatoires, entropie ≥ 128 bits**. | Vérifier le paramétrage du framework ; vigilance si mécanisme maison. |
| **R20** | **HTTPS** dès qu'une session est associée à des privilèges. | TLS sur la seule page de login ne protège pas l'identifiant de session. |
| **R21** | Attributs **`HttpOnly`** et (site HTTPS) **`Secure`** sur l'identifiant de session. | Derrière reverse proxy, `Secure` à poser explicitement (ex. `Header edit Set-Cookie ^(.)$ $1;Secure`) ; jamais d'identifiant dans l'URL. |
| **R22** | Mots de passe **non stockés en clair** : fonction cryptographique **non réversible** conforme RGS. | — |
| **R23** | Transformation des mots de passe avec **sel aléatoire**. | — |
| **R24** | Actions sensibles : **mécanismes assurant la légitimité de la requête**. | Expiration/réauth ; contrôle Referer (faible) ; **jetons anti-CSRF** aléatoires à usage unique ; `X-Frame-Options: DENY` / `SAMEORIGIN`. |
| **R25** | **Limiter au strict nécessaire les inclusions de contenus tiers**, après contrôle minimal. | Risque de compromission du fournisseur + fuite d'URL internes. |
| **R26** | **Privilégier un paradigme statique** chaque fois que possible. | Publication statique depuis un CMS de préproduction ; figer les sites archivés. |
| **R27** | **Point de contact** associé au site facilement identifiable. | WHOIS + adresse dans le SOA DNS. |
| **R28** | **Parcourir régulièrement le site** pour déceler toute anomalie. | Accès « démarqué » (ex. 3G) ; alertes moteurs de recherche ; contrôle d'intégrité (TripWire, AIDE, mtree hors serveur) ; supervision. |
| **R29** | **Politique de journalisation** (modalités, durées de conservation, analyse, corrélation). | Export hors serveur (syslog) ; Referer + User-Agent ; corrélation multi-journaux ; auditd / SACL sur ressources sensibles. |

---

## En-têtes et réglages recommandés (prêts à appliquer)

> Valeurs **exactes** du document 2013. Les pièges signalés « (2021) » renvoient à REF-11.

### HSTS
```
Strict-Transport-Security: max-age=31536000; includeSubDomains
```
- Un an, sous-domaines inclus. Pièges (2013) : n'agit qu'après le **premier échange** (TOFU) ; mesure **complémentaire**, pas une garantie anti-MITM. (2021 : devient une recommandation à part entière, R2 de REF-11, et rend l'accès en clair **impossible** — prérequis : HTTPS pérenne.)

### Anti-clickjacking
```
X-Frame-Options: DENY
X-Frame-Options: SAMEORIGIN
```
- À poser **sur chaque élément servi**. (2021 : `X-Frame-Options` est devenu **complémentaire**, la mesure principale est CSP `frame-ancestors`.)

### Cookie de session
- Attributs **`HttpOnly`** et **`Secure`** ; identifiant aléatoire **≥ 128 bits** ; jamais dans l'URL ; durée courte ; réauth pour le sensible.
- Piège reverse proxy : l'application ne voit pas TLS → elle peut omettre `Secure`. Correctif côté proxy (exemple Apache du document) :
```
Header edit Set-Cookie ^(.)$ $1;Secure
```
- Admin : cookie **distinct** de la partie publique si tout n'est pas en HTTPS.

### TLS (exemple historique, Apache mod_ssl)
```
SSLCiphersuite ALL:!SSLv2:!ADH:!RC4:!RC2:!MD5:!EXPORT:!ANON:!DES:!aNULL:!eNULL
```
- ⚠ **Obsolète** (« au moment de la rédaction ») — ne pas réutiliser ; voir REF-11 R1 (TLS 1.2 / 1.3 et guide TLS ANSSI-PA-035).

### Anti-CSRF
- **Jeton aléatoire** généré et stocké côté serveur, champ caché, **usage unique**, récent ; transposable aux liens GET.
- Contrôle du `Referer` : appoint seulement (falsifiable).

### Fuites d'information
- Supprimer `meta generator`, bannières de version dans les en-têtes, pages d'erreur par défaut, listage de répertoires ; **rejeter `TRACE`** ; pas de trace SQL/débogage en production.

### Journalisation
- Champs : IP, horodatage, URL, code de retour, **`Referer`**, **`User-Agent`** (Apache : `%{Referer}i`, `%{User-agent}i`) ; export **hors serveur** (syslog).

### Administration
- SSH/SFTP, **jamais FTP** ; admin web HTTPS, idéalement **certificat client** ; réseau d'admin dédié ou VPN IPsec ; filtrage IP en simple premier rempart.

---

## Application à PLÉIADE

> Contexte : applications Next.js par zone (`<zone>.pleiade.internal`) en conteneurs derrière **Traefik** (TLS, CA interne), authentification **Keycloak** (OIDC) via **Auth.js / NextAuth**, clés de service inter-apps (`X-API-Key`). Aucun fichier PLÉIADE n'a été lu pour cette fiche : tout ce qui suit est **à vérifier** dans le code et la configuration.
> Légende : ✅ **applicable** · 🟡 **partiellement** · ⛔ **hors champ**.

### Infrastructure
- ✅ **R1 — Défense en profondeur.** À vérifier : chaque app protège elle-même ses routes (contrôle de session/rôle **dans l'app**), et ne se repose pas uniquement sur Traefik ou Keycloak. À vérifier : les conteneurs sont sur des réseaux Podman/Docker cloisonnés (une app ne joint pas la base d'une autre). À vérifier : un WAF/middleware de filtrage existe-t-il devant Traefik ? (optionnel, « barrière supplémentaire »).
- ✅ **R2/R3 — Composants.** À vérifier : inventaire des dépendances npm par dépôt (`package-lock.json`), `npm audit` / Dependabot actifs sur les 12 dépôts `cecpc-pleiade` ; images de base des conteneurs à jour ; WordPress (`app-wordpress`) sans thèmes/plugins inutiles.
- ✅ **R4/R5/R6 — Administration.** À vérifier : l'API Traefik/dashboard n'est pas exposée sans authentification ; console Keycloak admin restreinte (réseau VPN / postes d'admin) ; `app-admin` exige un rôle Keycloak dédié et, idéalement, une authentification forte ; pas de FTP pour alimenter `app-webserver` / WordPress ; accès serveur Podman en SSH à clé.
- ✅ **R7 — Moindre privilège.** À vérifier : conteneurs Next.js exécutés en **utilisateur non root** (`USER node` ou équivalent), Podman rootless si possible, systèmes de fichiers en lecture seule hors volumes de téléversement ; routes API qui vérifient **toutes** les méthodes HTTP (piège JBoss : un `middleware` Next.js ou un handler qui ne protège que `GET`/`POST` laisse passer `PUT`/`DELETE`/`PATCH`).
- ✅ **R8 — Fichiers servis.** À vérifier : le dossier `public/` de chaque app ne contient ni `.env`, ni sauvegarde, ni fichier source ; les volumes de téléversement (portraits eho, pièces jointes MELMIL) ne sont pas servis tels quels par un serveur statique sans contrôle d'accès ; aucun `.git` exposé par `app-webserver`.
- ✅ **R9 — Base de données.** À vérifier : l'utilisateur Prisma en production n'a pas les droits DDL (les migrations `prisma migrate deploy` / `db push` tournent avec un compte distinct, au déploiement uniquement) ; une base / un compte par app.
- ✅ **R10 — Fuites.** À vérifier : `poweredByHeader: false` dans `next.config` (sinon en-tête `X-Powered-By: Next.js`) ; Traefik ne renvoie pas de version ; pages d'erreur Next.js personnalisées (`error.tsx`, `not-found.tsx`) sans pile d'appel en production ; pas d'erreur Prisma brute renvoyée au client ; `TRACE` rejeté ; pas d'index de répertoire sur `app-webserver`.
- ✅ **R11 — Matrice des flux.** À vérifier : matrice écrite par zone (entrées 443 sur Traefik ; flux internes app→Keycloak, app→eho, app→base ; sorties limitées). Les conteneurs d'app n'ont pas besoin d'Internet en exercice : les sorties devraient être fermées.
- ✅ **TLS / HSTS.** À vérifier : tout le trafic est en HTTPS (redirection 80→443 sur Traefik), HSTS posé (voir REF-11 pour les pièges sur `*.pleiade.internal` et la CA interne).

### Code applicatif
- ✅ **R12** — À vérifier : toute validation côté client (formulaires React) est **doublée** côté serveur (Server Actions / routes API avec schéma, ex. zod) ; aucun contrôle de droit uniquement dans l'interface (bouton masqué ≠ droit retiré).
- ✅ **R13** — Prisma paramètre les requêtes ; à vérifier : absence de `$queryRawUnsafe` / `$executeRawUnsafe` alimentés par des entrées ; `$queryRaw` en gabarit balisé seulement.
- ✅ **R14 — XSS (réseau social, presse, messagerie, MELMIL).** À vérifier : aucun `dangerouslySetInnerHTML` sur un contenu saisi sans assainissement (ex. DOMPurify) ; rendu Markdown/HTML riche filtré par liste blanche ; liens saisis filtrés (`javascript:` interdit) ; WordPress : rôles sans `unfiltered_html`.
- ✅ **R15/R16 — Redirections.** À vérifier : paramètres `callbackUrl` / `redirect` / `returnTo` (Auth.js, Keycloak `redirect_uri`) validés en **liste blanche de domaines** ; clients Keycloak avec `Valid Redirect URIs` **précis** (pas de `*`).
- ✅ **R17/R18 — Inclusion / injections / téléversements.** À vérifier : aucun chemin de fichier construit à partir d'une entrée (`path.join(uploadDir, req.nom)` → traversée) ; noms de fichiers téléversés **régénérés** côté serveur ; type réel vérifié (signature, pas seulement l'extension) ; taille limitée ; pas d'exécution de commande shell avec entrée utilisateur (conversion d'images, exports PPT MELMIL).
- ✅ **R19/R20/R21 — Sessions Auth.js.** À vérifier : cookie de session avec `HttpOnly` + `Secure` (Auth.js pose le préfixe `__Secure-` en HTTPS — **vérifier que l'app sait qu'elle est en HTTPS derrière Traefik**, ex. `AUTH_URL`/`NEXTAUTH_URL` en `https://` et `AUTH_TRUST_HOST`, sinon `Secure` peut manquer : c'est exactement le piège reverse proxy décrit par la note) ; `AUTH_SECRET` / `NEXTAUTH_SECRET` aléatoire long (≥ 128 bits, ex. 32 octets) et **différent par app** ; durée de session raisonnable ; jamais de jeton dans l'URL.
- 🟡 **R22/R23 — Mots de passe.** Délégués à Keycloak (hachage géré par Keycloak) : à vérifier qu'aucune app ne stocke de mot de passe en propre ; si un compte local subsiste (ex. WordPress), hachage salé.
- ✅ **R24 — CSRF / clickjacking.** À vérifier : Server Actions Next.js (contrôle d'`Origin` intégré) ; routes API mutantes qui acceptent les cookies → jeton CSRF ou contrôle d'`Origin` ; jeton CSRF Auth.js actif ; `X-Frame-Options`/`frame-ancestors` posés (voir REF-11 pour le cas cockpit/admin qui embarquent d'autres apps).
- ✅ **R25 — Contenus tiers.** À vérifier : aucune police, carte, statistique ou CDN Internet chargé par les apps (plateforme fermée : tout doit être auto-hébergé — sinon fuite des URL de zone et panne hors ligne, notamment LEAC).
- 🟡 **R26 — Statique.** À vérifier : les sites médias fictifs / presse publiés sans besoin dynamique pourraient être servis statiquement par `app-webserver` ; les zones d'exercice **closes** archivées en statique ou éteintes.
- ✅ **URL prévisibles (IDOR)** — À vérifier : chaque route `/api/.../[id]` vérifie que l'utilisateur **a le droit** sur l'objet (messagerie, pièces jointes MELMIL, fiches eho) ; pas de sécurité par identifiant « difficile à deviner ».

### Réaction
- ✅ **R27** — Point de contact sécurité PLÉIADE identifié (équipe CECPC) ; ⛔ WHOIS/SOA publics hors champ (domaine interne `.internal`), mais l'équivalent interne (qui alerter) est à définir.
- ✅ **R28** — À vérifier : supervision de disponibilité des apps (`/api/sante`), contrôle d'intégrité des images déployées (empreinte des images, `podman image inspect`), alerte sur fichiers inattendus dans les volumes de téléversement.
- ✅ **R29** — À vérifier : journaux Traefik (accès) avec `Referer` et `User-Agent`, journaux Keycloak (événements de connexion/admin), journaux applicatifs ; **centralisation hors serveur** et horloges synchronisées (NTP) ; politique de conservation écrite.
- ✅ **3.3 Incident** — Procédure : préserver journaux et volumes avant reconstruction ; redéployer depuis GitHub (image propre) **après** correction de la vulnérabilité.

---

## Ce qui a vieilli (note 2013 vs guide 2021)

| Sujet | 2013 (REF-10) | 2021 (REF-11) |
|---|---|---|
| **TLS** | Exemple de suite `SSLCiphersuite ALL:!SSLv2:…` (RC4 exclu), conseil RGS | TLS **1.2 et 1.3** préconisés, renvoi au guide TLS ANSSI-PA-035 (R1) ; HTTPS **pour tout site**, même non sensible |
| **HSTS** | Mesure « supplémentaire à coût quasi nul », non numérotée | **Recommandation R2** ; empêche aussi de contourner les alertes de certificat ; liste de préchargement (preload) |
| **Clickjacking** | `X-Frame-Options: DENY / SAMEORIGIN` | **CSP `frame-ancestors`** (R17), `X-Frame-Options` en complément (R18), qualifié d'« obsolète par CSP » |
| **CSRF** | Expiration, contrôle du `Referer`, jetons | `SameSite` sur les cookies (R32, R33), jeton ≥ 128 bits (R38), contrôle d'`Origin` (R40), preflight CORS (R39) |
| **Cookies** | `HttpOnly`, `Secure` | + `SameSite`, `Path`, pas de `Domain`, domaines distincts, préfixes de cookie (R26 → R33) |
| **XSS** | Échappement serveur (`htmlspecialchars`) | + API DOM sûre, séparation données/structure/style/logique, `eval` proscrit, **CSP**, **SRI**, Trusted Types (R4 → R16) |
| **Contenus tiers** | « Limiter au strict nécessaire » | **SRI** + CSP + isolement en Web Worker / iframe sandbox (R11, R12, R42, R48 → R52+) |
| **Exemples techniques** | Apache, Tomcat 6/7, JBoss 4.x, PHP magic quotes, 3G | Frameworks JS (React, Angular, Vue.js), API Fetch, Node.js |
| **Périmètre** | Infrastructure + code + réaction | **Recentré sur le navigateur** : infrastructure, mots de passe, SQL, journalisation fine et incident **ne sont plus détaillés** → REF-10 reste la source pour ces sujets |

---

## Limites / points d'attention

- **Date : 2013.** Les exemples (Apache 2.2 `Order allow,deny`, Tomcat 6/7, JBoss 4.x, magic quotes PHP, CERTA, 3G) sont datés ; la **suite TLS** citée est obsolète ; renvoyer à REF-11 et au guide TLS ANSSI.
- La note **ne donne pas** de valeur pour CSP, `SameSite`, `Referrer-Policy`, CORS, SRI, COOP : ces mécanismes sont traités dans **REF-11**.
- **Mots de passe** : la note dit « fonction conforme au RGS » sans nommer d'algorithme ; **hors document** (à vérifier dans les guides ANSSI à jour) : choix d'une fonction de dérivation lente.
- Le **contrôle d'IP** (session, admin) est présenté comme utile mais **non fiable** ; à ne pas sur-vendre, et peu pertinent derrière un proxy (toutes les requêtes vues avec l'IP de Traefik si `X-Forwarded-For` n'est pas géré).
- **fail2ban** : le document avertit lui-même du risque de déni de service par bannissement d'un relais partagé — sensible dans PLÉIADE où des dizaines de joueurs peuvent sortir par **la même IP VPN/NAT**.
- Extraction PDF : quelques coquilles d'origine (« recourt », « hammeçonnage », « maveillants ») ; dans l'exemple d'inclusion de fichiers, l'URL encodée est imprimée `http%31%2F%2F…` (le `%31` est une coquille du document pour `%3A`).
- Le document précise lui-même qu'il n'est **pas exhaustif** et que toute mise en œuvre doit être validée par l'administrateur / le responsable SSI.
