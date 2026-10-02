# REF-11 — Recommandations pour la mise en œuvre d'un site web : maîtriser les standards de sécurité côté navigateur

- **Fichier** : `anssi-guide-recommandations_mise_en_oeuvre_site_web_maitriser_standards_securite_cote_navigateur-v2.0.pdf` (source : `D:\CECPC\PLEIADE\DOC\CYBER SECU\`) · **Éditeur / référence** : ANSSI, guide **ANSSI-PA-009** · **Date / version** : **v2.0 du 28/04/2021** (historique : 1.0 du 22/04/2013 « version initiale » ; 1.1 du 13/08/2013 « corrections et précisions mineures, notamment sur TLS » ; 2.0 « refonte du guide sous l'angle des standards de sécurité web ») · **Pages** : 76 · **Marquage** : aucun marquage de confidentialité ; **« Licence ouverte / Open Licence (Étalab – v2.0) »** — réutilisation libre sous réserve de mentionner la paternité (source et date de dernière mise à jour). Recommandations **non normatives** (sauf disposition réglementaire contraire).
- **Public visé** : Développeur, Administrateur, RSSI, DSI, Utilisateur (liste en couverture).
- **Ingéré** : 2026-10-01

> Succède à la note DAT-NT-009 de 2013 (**REF-10**). Ce guide **fait foi** pour tout ce qui touche au navigateur (CSP, cookies, CORS, Referrer-Policy, SRI, iframes…). Il **exclut** volontairement les mécanismes sans implémentation navigateur (SSRF, SQLi, LFI/RFI, XXE, infrastructure) : pour ceux-là, voir REF-10.

---

## En une phrase

Guide ANSSI de 2021 qui, après un rappel des menaces et des règles d'hygiène, détaille **63 recommandations numérotées** (71 entrées avec les variantes « R− » alternative et « R+ » renforcée) pour configurer correctement les standards appliqués par le navigateur — **TLS/HSTS/CT, échappement et API DOM, `eval` proscrit, SRI, CSP (dont `frame-ancestors`), X-Frame-Options, Referrer-Policy, Web Storage/IndexedDB, cookies (`HttpOnly`, `Secure`, `SameSite`, `Path`, domaines distincts), XHR/Fetch, CORS, anti-CSRF, `noopener`, COOP, mode strict, Web Workers, iframes sandbox, postMessage** — puis le maintien en condition de sécurité (profils de déploiement, composants tiers).

---

## Ce que dit le document (synthèse structurée, fidèle)

### Convention de lecture (§1.3)
- **R** = recommandation à l'état de l'art ; **R−** = alternative de premier niveau, moins sûre ; **R+** = recommandation renforcée pour entités matures en SSI. Pratiques « à apprécier en fonction de la sensibilité du site ».

### 2. Menaces et types d'attaques
- Menaces les plus connues : **compromission des ressources** (atteinte à l'intégrité → défiguration, ou **point d'eau / watering hole** piégeant les visiteurs), **vol de données** (authentifiants, données personnelles, bancaires), **déni de service**. Scénarios élaborés : **attaque par rebond** (porte d'entrée vers le SI de l'hébergeur, relais, dépôt illégal), point d'eau discret.
- Classes : **XSS**, **CSRF**, **SSRF**, **SQLi**, **LFI/RFI**, **XXE** (renvois OWASP Cheat Sheets). **Seuls XSS (principalement) et CSRF sont traités.** XSS/CSRF sont généralement **au début du chemin de compromission** (ex. une XSS orchestre le navigateur d'un administrateur pour jouer une SQLi post-authentification).
- Protection = prévention + MCS + détection + **tests d'intrusion et audits réguliers**.

### 3. Rappel des règles d'hygiène
Sécurité à considérer sur 4 niveaux : **conception** (dès le début, issue de l'analyse de risques — la sécurisation a posteriori ne corrige pas les mauvaises pratiques comme une dépendance non maintenue) ; **intégrité du comportement côté client** (protéger ses utilisateurs des contenus tiers et utilisateurs malveillants) ; **configuration de l'hébergement** ; **détection et information**.
- **3.1 Défense en profondeur** : plusieurs mesures indépendantes par menace ; mauvaise approche = tout concentrer au point d'entrée ou ne compter que sur un pare-feu périmétrique.
- **3.2 Moindre privilège** : autant de rôles que de besoins d'accès ; limiter les permissions d'accès aux API du navigateur ; limiter les droits de l'utilisateur applicatif sur le système de fichiers.
- **3.3 Réduction de la surface d'attaque** (ne se substitue pas au moindre privilège, et inversement) : filtrer le port d'administration ; désactiver les services par défaut inutiles (ex. FTP) ; exclure modules inutiles (WebDAV, proxy, bibliothèques de tests, composants de développement).
- **3.4 Sécurité des échanges** : HTTPS ; **obligatoire** pour les données personnelles (loi Informatique et Libertés du 6 janvier 1978, RGPD).
- **3.5 Conformité du contenu présenté** : le navigateur doit afficher l'application conformément à l'intention du développeur.
- **3.6 Audit** : outils dans la CI (dépendances vulnérables, analyses statique/dynamique), stratégie d'audit avec jalons, prestataires **PASSI**, tests d'intrusion, **bug bounty** en complément.
- **3.7 Journalisation** : renvoi au guide journalisation ANSSI (DAT-NT-012) ; **horodatage et synchronisation des horloges** cruciaux dans une application découpée en services ; corrélation ; attention au **DoS par saturation des journaux** et à l'**exfiltration de données sensibles** présentes dans les journaux d'erreur.

### 4. Utilisation de TLS
- HTTPS garantit authenticité du serveur, confidentialité, intégrité ; sans lui, abus même non malveillants (hotspots Wi-Fi injectant de la publicité) et MITM (pages piégées, rebonds, touche aussi les sites **statiques**). Versions préconisées : **TLSv1.2 et TLSv1.3** → **R1**.
- La redirection HTTP→HTTPS laisse une fenêtre d'interception → **HSTS** (RFC 6797) : force HTTPS **et empêche l'utilisateur de passer outre les alertes de certificat** (invalide, autorité non reconnue) → **R2**. Prérequis : **pérennité de l'accès HTTPS** (l'accès en clair devient impossible). TOFU comblé par la liste **HSTS preload** (hstspreload.org).
- **Certificate Transparency** (RFC 6962) : journaux CT prouvant l'émission d'un certificat → **R3** surveillance des CT logs.

### 5. Mécanismes de sécurité web
**5.1 Stratégie par défaut** — hypothèse : le navigateur est de confiance.
- **SOP** : Origin = triplet **protocole, hôte, port** (80/443 implicites). Cross-origin : l'inclusion native (image, iframe) est permise, l'accès par script est bloqué. Subtilités : iframe A/B mutuellement inaccessibles ; XHR/Fetch : requête émise mais **réponse refusée** par défaut ; Web Storage / IndexedDB strictement par Origin ; **cookies** : stratégie différente (le **chemin** est contrôlé, **le port non**, envoi possible à plusieurs sous-domaines). Contournements prévus : CORS (XHR/Fetch), Web Messaging (iframes/fenêtres). **Toujours actifs quelle que soit l'origine** : JavaScript (un script tiers a les mêmes droits que ceux de la page : DOM, cookies, WebStorage — ex. surcharge de `window.alert`), CSS (peut remplacer des styles, charger des images), multimédia (chargés ; lecture des pixels bloquée cross-origin).
- **CORS** : contrat serveur↔navigateur via en-têtes ; remplace proxyfication et JSON-P. Cinématique : `Origin` posé par le navigateur → `Access-Control-Allow-Origin: %ORIGINE_ADMISE%` ou `Access-Control-Allow-Origin: *` → accepté si `*` ou égal à l'Origin.
- **CSP** : liste d'autorisations des ressources, via en-tête `Content-Security-Policy` ou `<meta http-equiv="Content-Security-Policy">`. Exemples : `default-src 'self' https:;` (même origine et HTTPS) ; contre-exemple `default-src 'self'; script-src 'unsafe-inline' 'unsafe-eval';` (« pas une bonne pratique »).

**5.2 Protection contre les XSS** — trois causes principales :
- **5.2.1 Contextes de composition** : méthodes dangereuses `document.write()`, `insertAdjacentHTML()`, `.innerHTML`, `.outerHTML` ; préférer `textContent`, `document.createTextNode()`, `element.setAttribute()` ; attention aux **sinks** (même `textContent` est un sink sur un élément `<script>`) — liste des sinks : standard **Trusted Types**. Exemple : Template String ES6 + `innerHTML` vulnérable (`meteo.city.name = "<iframe src=\"http://autre.site.web\"></iframe>"` interprété) vs `<template>` + `textContent` (affiché, non interprété) → **R4**. Préconisation : ne pas générer les pages HTML dynamiquement côté serveur ; le client consomme des services web en **JSON** avec `Content-Type: application/json` ; **pas de CSS ni JS inline** → **R5**, **R6**. La génération serveur par modèle+données présente plus de risques (injection lors du parsing du template) ; ne pas transmettre de contenu tiers de faible confiance directement dans le HTML. XSS stocké / réfléchi / DOM → **échappement contextuel** → **R7** (exemple : `encodeURIComponent` pour le contexte URL, `textContent` pour le HTML), **R8** (forme attendue, liste d'autorisations).
  - **`X-XSS-Protection` n'est plus préconisé** (surface d'attaque, nouvelles vulnérabilités, contournements ; retrait en cours/fait). Mesure standard : **CSP**. Pour désactiver le filtre implicite : `X-XSS-Protection: 0` ; **toléré** en l'absence de CSP stricte ou pour navigateurs anciens : `X-XSS-Protection: 1; mode=block`.
- **5.2.2 Évaluation de code** : `eval()` à proscrire au profit de `JSON.parse()` (exemple : chaîne forgée `… , alert()` exécutée par `eval`, exception levée par `JSON.parse`) → **R9** ; `setTimeout`/`setInterval` avec chaîne, `Function('code')`, `.constructor('code')` → **R10** (utiliser une lambda).
- **5.2.3 Intégrité des ressources** : **SRI** (attribut `integrity` sur `<link>` / `<script>`, empreinte calculée **après vérification** de la ressource, utile seulement en HTTPS). Exemple Bootstrap 3.3.7 / jQuery 3.2.1 avec `integrity="sha384-…"` et `crossorigin="anonymous"`. Calcul : `curl -s $URL | openssl dgst -$METH -binary | openssl enc -base64 -A` (script `./sri.sh sha384 <url>`), automatisable (webpack + `webpack-subresource-integrity`, après audit de la dépendance). Pas d'URL de rapport en cas d'échec (trace seulement dans la console). → **R11** (ressources internes), **R12** (ressources tierces, CDN). Limites : CSS et JS seulement ; ne vérifie pas les dépendances chargées par le script ; exige la maîtrise des **en-têtes de cache** ; URL **versionnées** nécessaires. **Trusted Types** (brouillon) : verrouille les sinks sans les proscrire — à suivre.

**5.3 Mise en œuvre de CSP** — contre-mesure très efficace contre le XSS, défense en profondeur forte, **ne remplace pas la correction des vulnérabilités**.
- **R13** : mettre en œuvre CSP (liste d'autorisations, moindre privilège).
- CSP efficace **seulement en HTTPS**. L'en-tête permet plus que la balise : `frame-ancestors`, `sandbox`, `report-uri`, mode `report-only` → **R14** (en-tête) ; **R14−** (balise `<meta>`, à placer **le plus tôt possible** — elle ne s'applique pas aux contenus qui la précèdent). Mise en œuvre : chaîne de reverse-proxies, hébergeur, ou CMS/framework (plugins cités à titre indicatif, non vérifiés : WordPress `gd-security-headers`, Drupal `Security Kit`).
- **Cumul des CSP** : plusieurs en-têtes (application + reverse proxy) et/ou plusieurs `<meta>` → **seulement dans le sens du durcissement** ; la ressource doit satisfaire **toutes** les politiques.
- **Directives** : `script-src`, `style-src`, `img-src`, `media-src`, `object-src`, `font-src` ; `child-src` (workers et frames enfants) et `frame-ancestors` (parents) ; `form-action` et `connect-src` (XHR, Fetch, WebSockets, **EventSource**) ; `default-src` (s'applique aux directives omises) ; globales : `upgrade-insecure-requests`, `block-all-mixed-content`, `sandbox`.
- **Sources** : `https:`, `domaine.fr`, `https://domaine.fr:8443`, jokers (`*://*.domaine.fr:*`, `*` = tout) ; `'none'` ; `'self'` ; `'unsafe-inline'` (script-src/style-src) ; `'unsafe-eval'` (script) ; empreinte `'sha256-…'` ou nonce (`nonce-2726c7f26c`) **renouvelé à chaque transmission de la CSP** ; `strict-dynamic` (CSP 3).
- Par défaut, définir une CSP **désactive** l'inline et l'évaluation (sauf `unsafe-*`). **Piège** : sans `default-src`, une directive omise = `*`.
- CSP bloque par convention : ressources `data:` base64, évaluation, CSS/JS inline → **R15** (pas de `data:`, `'unsafe-eval'`, `'unsafe-inline'`). Transition : hash/nonce pour l'inline de confiance + `strict-dynamic`. → **R16** (`default-src` obligatoire, pas `*` ; `default-src 'none'` pour les pages très sensibles comme une mire d'authentification).
- **Clickjacking** (§5.3.5) : `frame-ancestors` → **R17** ; `X-Frame-Options` (non standard, « rendu obsolète par CSP ») en défense en profondeur → **R18**. `frame-ancestors` **non supporté en `<meta>`**. Équivalences : `deny` ≙ `'none'`, `sameorigin` ≙ `'self'`, `allow-from https://site.fr` ≙ `frame-ancestors https://site.fr` (un seul paramètre pour `allow-from`).
- **Rapports** (§5.3.6) : CSP 2 `report-uri` ; CSP 3 (brouillon) `Reporting-Endpoints` + `report-to` ; mode `Content-Security-Policy-Report-Only` pour déployer sans casser. Risques : un rapport révèle des vulnérabilités (pire avec `'report-sample'`), fuite de **Capability URLs** (jetons de réinitialisation…), données de navigation (URL, Referer), point d'entrée supplémentaire **non authentifiable** → domaine/serveur dédié → **R19**.
- **Requêtes silencieuses** (§5.3.7) : attribut `ping` des liens (POST vers des URL arbitraires, sans JavaScript → CSRF, DDoS), **Resource Hints** (`dns-prefetch`, `preconnect`, `prefetch`, `prerender`, en `<link>` ou en-tête `Link`) → CSP par en-tête (`connect-src`, `prefetch-src`, ou `default-src`) → **R20**. Mention de **Permissions Policy** (brouillon) pour les API du navigateur.

**5.4 Referrer-Policy** — l'en-tête `Referer` peut fuiter des données d'URL (exemple `https://www.site.fr/main?login=jdoe&email=john.doe@here.com` envoyé au CDN, au site cible du lien, et lisible par `document.referrer`), grave pour les Capability URLs. Valeurs : `no-referrer`, `no-referrer-when-downgrade` (défaut du standard), `origin`, `same-origin`, `strict-origin`, `origin-when-cross-origin`, `strict-origin-when-cross-origin` (défaut de certains navigateurs), `unsafe-url` → **R21** (définir explicitement, **ne pas garder le défaut**, **jamais `unsafe-url`**). La directive CSP `referrer` est obsolète. Le `Referer` n'inclut jamais `#fragment` ni `user:password@`. Modulation par élément : attribut `referrerpolicy` sur `<a>`, `<area>`, `<img>`, `<iframe>`, `<link>` ; `rel="noreferrer"` (sur `<a>`, `<link>`, `<area>`) → **R22**. `<script>` ne gère pas `referrerpolicy` → API Fetch.

**5.5 Web Storage, IndexedDB, cookies**
- `localStorage`/`sessionStorage` : seul contrôle = SOP ; **tous les scripts d'une Origin y accèdent** (un JS injecté lit le `sessionStorage` même après déconnexion) → **R23 / R23−**. IndexedDB : même modèle, utilisable dans un Web Worker → **R24 / R24−**. **Web SQL Database** obsolète → **R25**.
- **Cookies** (0 à 4 ko) : → **R26** (rien de sensible sauf jetons de session). Attributs : `Domain` (inclut les sous-domaines ; absent = hôte émetteur), `Path` (défaut `/`), `Max-Age` (ex-`Expires` ; absent = cookie de session navigateur), `HttpOnly`, `Secure` (les navigateurs modernes empêchent un site HTTP de poser/modifier un cookie `secure` ; voir **Cookie Prefixes**), `SameSite` = `Strict` / `Lax` (envoyé en same-site et lors des navigations cross-origin « sûres » au sens RFC 7231, i.e. pas POST/PUT/DELETE) / `None` ; absent ≙ `Lax` (navigateurs modernes) ou `None` (anciens). **Deux sites sur le même domaine mais des ports différents ne sont pas isolés pour les cookies.**
- Same-origin / same-site / cross-site : `blog.site.fr` et `forum.site.fr` sont **same-site** mais pas same-origin.
- → **R27** domaines distincts par périmètre de responsabilité (exemple : cookie `Set-Cookie: Domain=cms.fr; sessionId=abc123; Secure; HttpOnly; SameSite=Lax` envoyé au service `cms.fr/webproxy` qui relaie les en-têtes vers `externe.fr` → usurpation ; solution : `admin.cms.fr`). **Ne pas spécifier `Domain`** est en général une bonne pratique. → **R28** `Path` ajusté (ex. cookie supplémentaire `Path=/admin`), mais path/domain **ne protègent pas contre la lecture** par un JS de même contexte. → **R29, R30** (`HttpOnly`), **R31** (`Secure`), **R32, R33** (`SameSite`).
- Un cookie est une **entrée utilisateur** : un sous-domaine corrompu peut poser un cookie sur un domaine voisin/parent → vérifier la cohérence, réauthentifier en cas de doute ; protections en écriture : **Cookie Prefixes**, **Public Suffix List**.
- Ces stockages sont **effaçables** par l'utilisateur (« effacer les données de navigation », **Clear Site Data**) → prévoir récupération/renouvellement. Mention **Credential Management API** / **WebAuthn**.

**5.6 XHR, CORS, Fetch**
- Réponse XHR = **données** (JSON/XML), jamais un fragment HTML injecté par `innerHTML` (exemple d'autocomplétion renvoyant `<ul><li>…`) → **R34**. Choix de méthode selon la confidentialité → **R35** ; `GET` (URL conservée dans historiques, journaux, proxies, terminaisons TLS ; réponses mises en cache) seulement pour données publiques, non sensibles, sans changement d'état → **R36−** ; **POST** → **R36** ; **PUT** (preflight systématique en cross-origin) → **R36+**. CSP `connect-src 'self'` → **R37** (couvre XHR, Fetch, EventSource, WebSocket). Jeton **anti-CSRF ≥ 128 bits** issu d'un générateur cryptographique (≈ 22 caractères parmi A–Z, a–z, 0–9), transmis par en-tête de réponse ou `<meta>` → **R38**.
- **CORS détaillé** : remplace JSON-P (évaluation + paramètres en GET → XSS) et la proxyfication serveur (transmet cookies, `Authorization`, `X-Auth-Token` au tiers). Requêtes « méthode simple + en-têtes simples » envoyées **sans condition** (risque de fuite : seule la lecture de la réponse est filtrée, via `Access-Control-Allow-Origin` et `Access-Control-Allow-Methods`) ; les autres déclenchent un **preflight** `OPTIONS` (`Access-Control-Request-Method`, `Access-Control-Request-Headers` → réponse `Access-Control-Allow-Origin`, `-Methods`, `-Headers`, `-Credentials`, mise en cache). → **R39** forcer un preflight (en-tête non standard vérifié) pour les données sensibles ; POST + `application/json`, PUT, ou authentification ⇒ preflight. → **R40** contrôler `Origin` en liste blanche. `Access-Control-Allow-Origin: *` **dangereux pour un intranet** (navigateur d'un employé = relais vers l'interne) ; incompatible avec `Access-Control-Allow-Credentials: true`. CORS décloisonne **toute l'Origin** → **R41** un domaine par service web. Bibliothèques publiques faisant du CORS → **R42** (obscurcies : exclues) / **R42−** (isolées en Web Worker, à défaut iframe). Attribut `crossorigin` (`anonymous` / `use-credentials`) → **R43**.
- **Fetch** : options `mode` (`no-cors`, `cors`, `same-origin`), `credentials` (`same-origin` par défaut, `omit`, `include`), `cache`, `referrerPolicy`, `redirect` (ex. `'error'`), `integrity` → **R44** (préférer Fetch ; les recommandations XHR s'y appliquent). Mention **Fetch Metadata Request Headers** (4 en-têtes complémentaires à `Origin`).

**5.7 HTML5 et JavaScript**
- `target="_blank"` laisse `window.opener` : même site ⇒ équivaut à exécuter du JS dans la page appelante ; cross-site ⇒ réécriture de `location` (tabnabbing) et `postMessage` → **R45** `rel="noopener"` / option `noopener` de `window.open` (`noreferrer` l'implique). Usages légitimes d'`opener` (pop-ups OAuth) dans des pages minimalistes dédiées. → **R46** `Cross-Origin-Opener-Policy: same-origin` (crucial si un écouteur global `window.addEventListener('message')` existe).
- **Mode strict** `"use strict";` en tête de chaque fonction ; fonctions auto-invoquées préférables au niveau fichier (la minification peut le globaliser ou le neutraliser ; pas de concaténation) → **R47**. TypeScript/CoffeeScript/Dart aident mais leurs contrôles disparaissent à l'exécution après transpilation.
- **Template Strings tagués** (fonction d'échappement en préfixe, ex. `safeTag`) — exemple d'implémentation de R7.
- **Cloisonnement** : **Web Workers** (même Origin, pas d'accès DOM/cookies/stockages locaux ; XHR/Fetch/EventSource/WebSocket/IndexedDB possibles ; `postMessage` ; Shared Workers) → **R48** ; limites : `importScripts` charge du cross-origin **sans SRI possible** ; requêtes émises **avec l'Origin de la page** ; → **R48+** worker de faible confiance instancié depuis une URL `data:` (exemple `new Worker('data:text/plain;charset=utf-8;base64,' + btoa(txt))`) ; → **R49** messages au format défini, JSON, postMessage préféré à IndexedDB. jQuery inutilisable en worker (accède au DOM) ⇒ iframe.
- **iframes** : contexte complet (DOM, JS, stockages de sa source) → **R50**. Attribut **`sandbox`** seul = **toutes** restrictions ; dérogations : `allow-forms`, `allow-scripts`, `allow-same-origin`, `allow-popups`, `allow-modals`, `allow-pointer-lock`, `allow-top-navigation`. Iframe même Origin sans sandbox = **aucune isolation** ; avec sandbox ⇒ **Origin nulle**. `allow-same-origin` + `allow-scripts` nécessaires pour un `postMessage` ciblant l'Origin (au lieu de `"*"`) → **R51**. Sur une iframe **même Origin**, `allow-scripts` + `allow-same-origin` ⇒ la sandbox ne vaut plus rien ; si le contenu est chargé hors iframe, la sandbox de l'appelant tombe → **R52** sandbox via **CSP** ; **R52+** traitement sur une **seconde Origin**. → **R53** formats de messages ; risques du canal : changement de référence d'iframe, blocage, interception/falsification, messages d'Origin étrangère, partage mémoire (**Spectre**) → **R54** cibler l'Origin dans `postMessage`, **R55** contrôler l'Origin émettrice et le format à la réception, **R56** compléter par `frame-ancestors` (première ligne) et `child-src` (défense en profondeur). Mention `Cross-Origin-Embedder-Policy` et `Cross-Origin-Resource-Policy`. → **R57** ne pas écrire `document.domain` (domain relaxation, en retrait). → **R58** proscrire JSON-P (préférer CORS).

### 6. Maintien en conditions opérationnelle et de sécurité
- **Contenus** : pas d'information sensible dans les erreurs ; profils `dev`/`debug` vs `prod`/`release` → **R59** ; contrôles automatisés empêchant de déployer un profil non durci → **R60**.
- **Composants** (OS, serveur, CMS et greffons, bibliothèques Java, **Node.js**, PHP, SGBD…) : exemples WordPress (3 thèmes + 2 plugins préinstallés), Tomcat (applications d'exemple, `host-manager`, `manager`) → **R61** (limiter, supprimer, sinon désactiver), **R62** (recenser, mettre à jour, évaluer la pérennité, suivre les vulnérabilités), **R63** (ne pas modifier le cœur ; passer par greffons). Critères d'adoption d'une dépendance : **fonctionnement, origine, sécurité, pérennité**. Frameworks (React, Angular, Vue.js) = base solide si l'on comprend leurs mécanismes.

### Annexe A — Cas d'application du preflight CORS
- « Simple » = méthode **GET, HEAD, POST*** ; en-têtes uniquement **Cache-Control, Content-Language, Content-Type, Expires, Last-Modified, Pragma** ; `Content-Type` parmi **multipart/form-data, application/x-www-form-urlencoded, text/plain**.
- *Note du document : « Le téléversement de fichiers par la méthode POST n'entre pas dans la catégorie des appels avec en-tête et méthode simple. »* — ⚠ alors que son propre tableau classe `POST` + `multipart/form-data` **sans preflight** (voir Limites).
- Exemples : POST urlencoded → pas de preflight ; GET + `Authorization` → preflight ; POST + `application/json` → preflight ; POST + `multipart/form-data` → pas de preflight ; POST multipart + `X-Auth-Token` → preflight ; PUT → preflight.

---

## Toutes les recommandations

> **63 numéros (R1 → R63) + 8 variantes** (R14−, R23−, R24−, R36−, R36+, R42−, R48+, R52+) = **71 entrées**. Intitulés exacts de la « Liste des recommandations » (p. 68–69), puis contenu concret.

### TLS (ch. 4)
- **R1 — Mettre en œuvre TLS à l'état de l'art.** Appliquer le guide « Recommandations de sécurité relatives à TLS » (ANSSI-PA-035) pour **tout site, même sans information sensible** ; TLSv1.2 et TLSv1.3.
- **R2 — Mettre en œuvre HSTS.** Contre le MITM dû aux accès non sécurisés ; prérequis : HTTPS pérenne. Exemple : `Strict-Transport-Security: max-age=31536000; includeSubDomains;` ; preload possible.
- **R3 — Surveiller les CT logs.** L'hébergeur/responsable surveille les journaux Certificate Transparency pour détecter et révoquer les certificats illégitimes sur ses domaines.

### XSS (§5.2)
- **R4 — Utiliser l'API DOM à bon escient.** Toute modification du contenu client via l'API DOM ; ne pas utiliser (ou contrôler) les méthodes/propriétés substituant du contenu interprétable (`innerHTML`, `outerHTML`, `insertAdjacentHTML`, `document.write`) ; préférer `textContent`, `createTextNode`, `setAttribute`, `<template>`.
- **R5 — Dissocier clairement la composition des pages web.** Données (JSON), structure (HTML), style (CSS), logique (JS) séparés ; pas d'inline ; contrôlable par CSP.
- **R6 — Expliciter la nature d'une ressource avec l'en-tête Content-Type.** Content-Type approprié (ex. `application/json` pour les données) pour éviter une interprétation inattendue.
- **R7 — Vérifier l'échappement des contenus inclus.** Toute donnée externe (paramètres, en-têtes, fichiers, saisies, webservices) échappée selon le contexte (`encodeURIComponent` en URL, `textContent` en HTML, template tagué).
- **R8 — Vérifier la conformité des données issues de sources externes.** Contrôle de forme, liste d'autorisations (une donnée numérique ne contient que des chiffres).
- **R9 — Proscrire l'usage de la fonction eval().** Utiliser `JSON.parse()`.
- **R10 — Proscrire l'usage de constructions basées sur l'évaluation de code.** `setInterval`/`setTimeout` avec chaîne, `Function('code')`, `.constructor('code')` interdits.
- **R11 — Contrôler l'intégrité des contenus internes.** SRI sur les JS et CSS internes.
- **R12 — Contrôler l'intégrité des contenus tiers.** En HTTPS, SRI systématique, surtout pour les CDN.

### CSP (§5.3)
- **R13 — Restreindre les contenus aux ressources fiables.** Mettre en œuvre CSP (liste d'autorisations).
- **R14 — Mettre en œuvre CSP par en-tête HTTP.** Privilégier `Content-Security-Policy` (reverse proxy, hébergeur, CMS/framework).
- **R14− — Mettre en œuvre CSP par balise meta dans les pages HTML.** Si l'en-tête est impossible ou pour durcir ponctuellement ; placer la balise au plus tôt ; pas de `frame-ancestors` ni `sandbox` ni rapport en meta.
- **R15 — Interdire des contenus inline.** La CSP ne doit contenir ni `data:`, ni `'unsafe-eval'`, ni `'unsafe-inline'` (transition : hash/nonce, `strict-dynamic`).
- **R16 — Définir la directive default-src.** Présente et différente de `*` ; `default-src 'none'` + autorisations ciblées pour les pages très sensibles. Exemples : `default-src 'self'; img-src 'self' https://my-cdn.fr;` — `default-src 'none'; child-src https://ifr.domaine.fr;`
- **R17 — Utiliser CSP contre le clickjacking.** `frame-ancestors` en liste minimale, sur tout le site ou au moins les pages sensibles (mot de passe, connexion, virements). Valeurs : `'none'`, `'self'`, `a.fr b.fr`.
- **R18 — Utiliser X-Frame-Options contre le clickjacking.** En défense en profondeur, un `X-Frame-Options` strict (`deny` / `sameorigin`).
- **R19 — Etudier les risques liés à la collecte de rapports CSP.** Sensibilité page par page ; activation au cas par cas ; endpoint dédié et sécurisé.
- **R20 — Réduire l'impact des requêtes silencieuses via CSP.** Limiter les Origins atteignables (`connect-src`, `prefetch-src`, `default-src`) contre `ping` et Resource Hints.

### Referrer-Policy (§5.4)
- **R21 — Définir la stratégie de construction de l'en-tête Referer.** Via l'en-tête `Referrer-Policy` ; le défaut ne doit pas être conservé ; `unsafe-url` interdit.
- **R22 — Modifier ponctuellement l'en-tête Referer.** Attribut `referrerpolicy` sur les éléments concernés.

### Stockages et cookies (§5.5)
- **R23 — Ne pas stocker des informations sensibles dans les bases de données locales.** `localStorage`/`sessionStorage` = données sans conséquence (préférences).
- **R23− — Éviter de stocker des informations sensibles dans les bases de données locales.** Sinon, décision issue d'une **analyse de risques**.
- **R24 — Ne pas stocker des informations sensibles dans les bases de données IndexedDB.** Usage type : cache d'état d'application.
- **R24− — Éviter de stocker des informations sensibles dans les bases de données IndexedDB.** Sinon, analyse de risques.
- **R25 — Proscrire l'usage de l'API Web SQL Database.** Obsolète.
- **R26 — Ne pas stocker d'informations sensibles dans les cookies.** Sauf jetons de session ; données temporaires, faible volume.
- **R27 — Cloisonner les sessions au moyen de noms de domaine distincts.** Un domaine par périmètre de responsabilité (ex. `admin.cms.fr`) ; ne pas fixer `Domain`.
- **R28 — Définir le path d'un cookie.** Ajusté à l'arborescence et à la sensibilité (ex. `/admin`).
- **R29 — Maîtriser l'accès aux cookies en JavaScript.** `HttpOnly` pour tout cookie non lu par le client.
- **R30 — Proscrire l'accès en JavaScript à un cookie de session.** `HttpOnly` **obligatoire** pour un cookie de session.
- **R31 — Limiter le transit des cookies aux flux sécurisés.** `Secure` dès que le site est en HTTPS.
- **R32 — Définir une stratégie stricte d'envoi des cookies en cross-site.** `SameSite=Strict` si le cookie n'a pas à suivre une navigation externe ; sinon `Lax` si aucune action privilégiée en `GET`.
- **R33 — Définir une stratégie stricte d'envoi des cookies de session en cross-site.** Cookie de session : `SameSite` **défini et jamais `None`**.

### XHR / CORS / Fetch (§5.6)
- **R34 — Encoder les réponses XMLHttpRequest.** Format non exécutable (JSON, XML), pas de fragment HTML.
- **R35 — Choisir une API selon sa méthode HTTP.** Confidentialité de la donnée compatible avec la méthode ; sinon demander l'évolution de l'API.
- **R36− — Utiliser XHR avec la méthode GET sous certaines conditions.** Données publiques dans l'URL, récupération non sensible (cachable), idempotence (aucun changement d'état).
- **R36 — Utiliser XHR avec la méthode POST.**
- **R36+ — Utiliser XHR avec la méthode PUT.** Preflight systématique en cross-origin ⇒ moins de CSRF et de fuite.
- **R37 — Compléter la mise œuvre de XHR par une configuration CSP.** `default-src 'self' a.fr; connect-src 'self';`
- **R38 — Protéger les appels XHR par un contrôle anti-CSRF.** CSRF-Token aléatoire cryptographique ≥ 128 bits (≈ 22 caractères A–Z a–z 0–9), transmis par en-tête de réponse ou `<meta>`.
- **R39 — Mettre en œuvre un preflight lors des appels CORS.** Données sensibles ⇒ preflight prévu côté serveur et forcé côté client (en-tête non standard vérifié).
- **R40 — Vérifier la valeur de l'Origin lors de la réception d'une requête CORS.** Liste blanche d'Origins.
- **R41 — Cloisonner les services web au moyen de noms de domaines distincts.** Un domaine par WebService indépendant.
- **R42 — Éviter l'usage de bibliothèques publiques effectuant des appels CORS.** Code obscurci + appels CORS ⇒ exclu.
- **R42− — Isoler l'utilisation de bibliothèques publiques effectuant des appels CORS.** Web Worker, à défaut iframe.
- **R43 — Anonymiser le chargement des ressources en cross-origin.** `crossorigin="anonymous"` quand l'authentification n'est pas nécessaire.
- **R44 — Préférer l'utilisation de l'API Fetch à XMLHttpRequest.** Options `mode`, `credentials`, `redirect`, `referrerPolicy`, `integrity`.

### HTML5 / JavaScript (§5.7)
- **R45 — Sécuriser l'ouverture de nouvelles fenêtres.** `rel="noopener"` avec `target` ; option `noopener` dans `window.open`.
- **R46 — Définir une stratégie d'ouverture en cross-origin.** `Cross-Origin-Opener-Policy: same-origin`.
- **R47 — Utiliser le mode strict.** `"use strict";` en tête de chaque fonction (fonctions auto-invoquées).
- **R48 — Isoler les traitements par Web Workers.** JS non maîtrisé, externe, ou appels CORS ⇒ worker (pas de DOM, cookies, stockages).
- **R48+ — Isoler les traitements par Web Worker et Origin « data : ».** Worker de faible confiance instancié depuis une URL `data:`.
- **R49 — Formaliser les échanges en utilisant l'API de Message** (workers). Formats précis, JSON, postMessage plutôt qu'IndexedDB.
- **R50 — Cloisonner les traitements dans des iframes.** Ressources externes nécessitant un DOM.
- **R51 — Cloisonner les traitements avec une sandbox.** Paramétrer l'attribut `sandbox`.
- **R52 — Favoriser la déclaration de sandbox via CSP.** Quand on maîtrise l'hébergement du contenu isolé (directive `sandbox`).
- **R52+ — Cloisonner les traitements par une iframe sur une seconde Origin.**
- **R53 — Formaliser les échanges en utilisant l'API de Message** (iframes). Formats précis, JSON.
- **R54 — Définir l'Origin lors de l'utilisation de l'API de Message.** `postMessage(msg, origineCible)` — jamais `"*"`.
- **R55 — Contrôler l'Origin lors de l'utilisation de l'API de Message.** Vérifier `event.origin` et le format à la réception.
- **R56 — Compléter la déclaration d'une API de messages par la définition d'une CSP.** `frame-ancestors` + `child-src`.
- **R57 — Proscrire l'écriture de document.domain.** Utiliser postMessage.
- **R58 — Proscrire l'usage de JSON-P.** Utiliser CORS.

### MCS (ch. 6)
- **R59 — Définir des profils de déploiement spécifiques aux contextes.** Gestion d'erreurs différente en dev / test / prod.
- **R60 — Empêcher le déploiement d'un profil non adapté au contexte.** Contrôles automatisés bloquant un profil non durci en production.
- **R61 — Limiter les composants logiciels tiers.** Strict nécessaire ; supprimer, sinon désactiver.
- **R62 — Maintenir à jour les composants logiciels tiers utilisés.** Recenser, mettre à jour, évaluer la pérennité, suivre les vulnérabilités publiées.
- **R63 — Ne pas modifier le cœur des composants logiciels tiers utilisés.** Modifications par greffons ou composant adapté.

---

## En-têtes et réglages recommandés (prêts à appliquer)

> Valeurs **telles que données dans le guide**, puis pièges signalés par le guide. Les mentions **« hors document »** sont des compléments de contexte à vérifier, non issus de l'ANSSI.

### TLS — R1
- TLS **1.2 et 1.3** uniquement ; configuration selon ANSSI-PA-035.

### HSTS — R2
```
Strict-Transport-Security: max-age=31536000; includeSubDomains
```
- (Le guide l'écrit avec un `;` final.) Pièges : **HTTPS pérenne obligatoire** (le clair devient impossible) ; HSTS **interdit de passer outre une erreur de certificat** ; TOFU sauf preload.

### CSP — R13 à R17, R20, R37, R56
Exemples du guide :
```
Content-Security-Policy: default-src 'self' https:;
Content-Security-Policy: default-src 'self'; img-src 'self' https://my-cdn.fr;
Content-Security-Policy: default-src 'none'; child-src https://ifr.domaine.fr;
Content-Security-Policy: default-src 'self'; frame-ancestors 'none';
Content-Security-Policy: default-src 'self'; frame-ancestors 'self';
Content-Security-Policy: default-src 'self'; frame-ancestors a.fr b.fr;
Content-Security-Policy: default-src 'self' a.fr; connect-src 'self';
Content-Security-Policy: default-src 'self' a.fr; prefetch-src 'self';
```
- Règles : **en-tête** plutôt que `<meta>` ; **`default-src` présent et ≠ `*`** ; **ni `data:`, ni `'unsafe-eval'`, ni `'unsafe-inline'`** ; nonce **renouvelé à chaque réponse** ; `strict-dynamic` pour la transition.
- Pièges : une directive omise sans `default-src` = `*` ; `frame-ancestors`, `sandbox`, rapports **inopérants en `<meta>`** ; plusieurs CSP (proxy + app) **se cumulent en durcissant** — une CSP statique au proxy peut casser des nonces de l'app ; CSP inutile sans HTTPS ; contre-exemple à ne pas suivre : `script-src 'unsafe-inline' 'unsafe-eval'`.
- Déploiement : `Content-Security-Policy-Report-Only` d'abord. Rapports (exemples du guide, recopiés tels quels) :
```
Content-Security-Policy: default-src: 'self'; report-uri: https://csp.my.fr;
Reporting-Endpoints: my-csp-endpoint="https://csp.my.fr";
Content-Security-Policy: default-src: 'self'; report-to: my-csp-endpoint;
```
  ⚠ Ces exemples contiennent des `:` après les noms de directives (`default-src:`, `report-uri:`, `report-to:`) — **coquille du guide** : la syntaxe CSP sépare nom et valeurs par un espace (`default-src 'self'; report-uri https://csp.my.fr`). Endpoint de rapports sur domaine dédié ; pas de rapports sur les pages à Capability URLs ; éviter `'report-sample'`.

### Anti-clickjacking — R17, R18
```
Content-Security-Policy: frame-ancestors 'none'
X-Frame-Options: deny
```
- Équivalences : `deny` ≙ `'none'` ; `sameorigin` ≙ `'self'` ; `allow-from https://site.fr` ≙ `frame-ancestors https://site.fr` (un seul paramètre). **Hors document** : `allow-from` n'est plus reconnu par les navigateurs actuels → utiliser `frame-ancestors` pour toute liste.

### X-XSS-Protection (§5.2.1)
```
X-XSS-Protection: 0
```
- Toléré seulement sans CSP stricte / navigateurs anciens : `X-XSS-Protection: 1; mode=block`. La vraie protection est la CSP.

### SRI — R11, R12, R43
```html
<script src="https://…/lib-1.2.3.min.js" integrity="sha384-…" crossorigin="anonymous"></script>
```
- Calcul : `curl -s $URL | openssl dgst -sha384 -binary | openssl enc -base64 -A`. Pièges : JS/CSS seulement ; URL **versionnée** ; maîtrise des en-têtes de cache ; dépendances chargées dynamiquement non couvertes ; **auditer avant de calculer l'empreinte** ; pas de SRI pour `importScripts`.

### Referrer-Policy — R21, R22
- Valeurs : `no-referrer`, `no-referrer-when-downgrade`, `origin`, `same-origin`, `strict-origin`, `origin-when-cross-origin`, `strict-origin-when-cross-origin`, `unsafe-url`.
- Règle : **poser l'en-tête explicitement**, ne pas laisser le défaut, **jamais `unsafe-url`**. Le guide ne fixe pas de valeur unique ; valeurs les plus protectrices de sa liste : `no-referrer`, `same-origin`, `strict-origin`, `strict-origin-when-cross-origin`. Par lien : `referrerpolicy="origin"`, `rel="noreferrer"`.

### Cookies — R26 à R33
Exemple du guide :
```
Set-Cookie: Domain=cms.fr; sessionId=abc123; Secure; HttpOnly; SameSite=Lax
```
(⚠ L'exemple sert à illustrer un **problème** — le `Domain` trop large ; et l'ordre « attribut avant nom=valeur » est une coquille : le couple nom=valeur vient en premier.)
- Cible pour un cookie de session : **`HttpOnly`** (R30), **`Secure`** (R31), **`SameSite=Strict`** ou au moins **`Lax`**, jamais `None` (R33), **pas de `Domain`** (R27), `Path` ajusté (R28), contenu = jeton seulement (R26). Préfixes de cookies cités comme protection en écriture (**hors document** pour le détail : `__Host-` impose `Secure`, `Path=/` et l'absence de `Domain` ; `__Secure-` impose `Secure`).
- Pièges : même domaine + ports différents ≠ isolation ; sous-domaines **same-site** entre eux ; path/domain ne protègent pas contre un JS du même contexte ; un cookie est une **entrée non fiable**.

### CORS — R39 à R43
```
Access-Control-Allow-Origin: <origine exacte de la liste blanche>
```
- Jamais `Access-Control-Allow-Origin: *` sur un intranet ; `*` incompatible avec `Access-Control-Allow-Credentials: true` ; vérifier `Origin` côté serveur ; forcer le preflight (en-tête non standard) pour le sensible ; un domaine par service ; `crossorigin="anonymous"` par défaut.

### Anti-CSRF — R38 (+ R32/R33, R36+, R39, R40)
- Jeton aléatoire cryptographique **≥ 128 bits** (~22 caractères alphanumériques), communiqué par en-tête de réponse ou `<meta>`, renvoyé à chaque appel mutant ; compléter par `SameSite` et contrôle d'`Origin`.

### Fenêtres et isolation — R45, R46
```
Cross-Origin-Opener-Policy: same-origin
```
```html
<a href="…" target="_blank" rel="noopener">…</a>
```
- `window.open(url, nom, 'noopener')`. Également cités (sans valeur imposée) : `Cross-Origin-Embedder-Policy`, `Cross-Origin-Resource-Policy`.

### iframes et messages — R50 à R56
```html
<iframe sandbox src="…"></iframe>
<iframe sandbox="allow-scripts allow-same-origin" src="https://autre-origine/…"></iframe>
```
- `postMessage(msg, "https://origine-cible")` (jamais `"*"`) ; à la réception, vérifier `event.origin` + format JSON. Piège : `allow-scripts allow-same-origin` sur une iframe **de même Origin** annule la sandbox ⇒ seconde Origin (R52+) ou sandbox via CSP (R52).

### Fetch — R44
```js
fetch(url, { mode: 'same-origin', credentials: 'omit', referrerPolicy: 'no-referrer', redirect: 'error', integrity: 'sha256-…' })
```

---

## Application à PLÉIADE

> Contexte : apps Next.js par zone `<zone>.pleiade.internal` (réseau social, eho avec portraits téléversés, MELMIL avec pièces jointes et SSE, messagerie temps réel, presse/WordPress, LEAC tablette hors ligne, admin, cockpit), conteneurs derrière **Traefik** (TLS, CA interne), **Keycloak** OIDC via **Auth.js / NextAuth**, clés inter-apps **`X-API-Key`**. **Aucun fichier PLÉIADE n'a été lu** : chaque ligne est un contrôle « À vérifier ».
> Légende : ✅ **applicable** · 🟡 **partiellement** · ⛔ **hors champ**.

### 1. TLS, HSTS, certificats
- ✅ **R1** — À vérifier : entrypoint `websecure` de Traefik limité à **TLS 1.2 minimum** (option TLS `minVersion: VersionTLS12`) ; redirection 80→443 sur toutes les routes, y compris Keycloak.
- 🟡 **R2 — HSTS sur `*.pleiade.internal`.** Applicable mais **piège majeur** : HSTS interdit de passer outre une erreur de certificat. Tant que la **CA interne** n'est pas installée sur un poste ou une tablette, l'utilisateur sera **bloqué net** (sans bouton « continuer »). À vérifier : déploiement de la CA sur tous les terminaux **avant** d'activer HSTS ; démarrer avec un `max-age` court puis monter à `31536000`. `includeSubDomains` posé sur `pleiade.internal` couvrirait **toutes les zones** : à vérifier qu'aucun service interne n'est servi en HTTP clair. ⛔ **Preload** impossible (TLD interne). À vérifier : qui pose HSTS — un middleware Traefik `headers` (`stsSeconds`, `stsIncludeSubdomains`) est le point unique logique.
- 🟡 **R3 — CT logs.** ⛔ pour la CA interne (pas de journaux CT) ; l'équivalent à vérifier : **registre des certificats émis** par la CA de zone et protection de sa clé privée.

### 2. En-têtes posés par Traefik ou par l'app
- ✅ À vérifier : un **middleware Traefik `headers` commun** à toutes les routes pose : HSTS, `X-Frame-Options`, `Referrer-Policy`, `Cross-Origin-Opener-Policy`, `X-XSS-Protection: 0` (option `browserXssFilter` à **ne pas** mettre à `1`), et **hors document** `X-Content-Type-Options: nosniff` (`contentTypeNosniff`).
- ✅ **CSP : plutôt dans l'app** (Next.js `middleware` qui génère un **nonce par requête**) — parce que la CSP doit suivre les nonces. À vérifier : si Traefik pose **aussi** une CSP statique, les deux se **cumulent en durcissant** (guide §5.3.2) : une CSP Traefik sans nonce **bloquera** les scripts inline de Next.js.

### 3. CSP compatible Next.js — R5, R13 à R16, R20, R37
- ✅ À vérifier : présence d'une CSP par en-tête sur chaque app, avec **`default-src 'self'`** (ou `'none'` + autorisations), `script-src 'self' 'nonce-…' 'strict-dynamic'`, `object-src 'none'`, `base-uri 'self'` *(hors document)*, `form-action 'self'` + l'origine Keycloak (formulaires de connexion / déconnexion), `connect-src 'self'` (+ origines d'API réellement appelées depuis le navigateur), `frame-ancestors` (voir §5).
- 🟡 **R15 (pas d'`unsafe-inline`)** : Next.js injecte des scripts inline d'hydratation → **nonce** obligatoire (lu par Next depuis l'en-tête CSP posé dans le middleware) ; conséquence : pages **rendues dynamiquement** (le nonce empêche le rendu statique). `style-src` : selon la bibliothèque CSS (CSS-in-JS, attributs `style` React) un `'unsafe-inline'` sur **styles** peut subsister — à documenter comme écart assumé. **`'unsafe-eval'` uniquement en développement** (`next dev`) : à vérifier qu'il n'est **jamais** en production (lien R59/R60).
- 🟡 **`data:`** (R15) : les portraits eho ou avatars encodés en base64 (`img-src data:`) violent R15 → à vérifier ; préférer des URL servies par l'app.
- ✅ **SSE (MELMIL, messagerie)** : `EventSource` est régi par **`connect-src`** (guide §5.3.3 et R37) → à vérifier que le flux SSE est sur `'self'` ; s'il est servi par une autre app, ajouter son origine exacte, pas un joker.
- ✅ **R19** : si un endpoint de rapports CSP est créé, domaine dédié, pas de `report-sample`, rapports exclus des pages à jetons (réinitialisation, invitations).

### 4. Cookies de session Auth.js / NextAuth — R26 à R33, R27, R41
- ✅ À vérifier sur chaque app, dans l'onglet réseau : cookie de session (Auth.js v5 : `__Secure-authjs.session-token` ; NextAuth v4 : `__Secure-next-auth.session-token` — *noms hors document, à constater*) avec **`HttpOnly`**, **`Secure`**, **`SameSite=Lax`** au minimum (jamais `None`), **sans `Domain`**, `Path=/`. Cookie CSRF Auth.js en `__Host-…csrf-token`.
- ⚠ **Piège reverse proxy (déjà relevé par REF-10)** : derrière Traefik, l'app doit savoir qu'elle est en HTTPS (URL publique `https://` dans `AUTH_URL`/`NEXTAUTH_URL`, hôte de confiance) — sinon les préfixes `__Secure-`/`__Host-` et l'attribut `Secure` peuvent **disparaître**.
- ✅ **R27/R41 — un domaine par app** : à vérifier que chaque app a son propre hôte (ex. `social.<zone>.pleiade.internal`, `eho.<zone>…`) et **non** des chemins sous un hôte commun (`<zone>.pleiade.internal/social`) — sinon cookies et CORS ne sont pas cloisonnés (R28 ne compense que partiellement). ⚠ Aucun cookie posé avec `Domain=.pleiade.internal` ou `Domain=<zone>.pleiade.internal` (il partirait vers **toutes** les apps, voire toutes les zones).
- ⚠ **Same-site** : toutes les apps `*.pleiade.internal` sont **same-site entre elles** (même domaine enregistrable — *déduction hors document*, `.internal` n'étant pas un suffixe public listé). Donc **`SameSite` ne protège pas une app contre une autre app ou une autre zone** : une XSS dans le réseau social peut émettre des requêtes « same-site » vers MELMIL avec les cookies. → contrôle d'`Origin` / jeton CSRF indispensables en plus (R38, R40).
- ✅ **Secrets** : `AUTH_SECRET` distinct par app et par zone, aléatoire (≥ 128 bits — R38 donne la même borne pour les jetons).
- 🟡 **Session Keycloak** : cookies Keycloak (`KEYCLOAK_SESSION`, `AUTH_SESSION_ID`…) posés sur l'hôte Keycloak — à vérifier `Secure` et `SameSite` (le SSO OIDC repose sur des redirections, `Lax` suffit en général ; `None` seulement si une iframe de session Keycloak est utilisée).

### 5. iframes — cockpit et admin embarquent-ils d'autres apps ? — R17, R18, R50 à R56
- ✅ **Par défaut** (toute app non destinée à être embarquée) : `frame-ancestors 'none'` + `X-Frame-Options: deny`.
- ✅ **Si le cockpit / l'admin affichent d'autres apps en iframe** (à vérifier dans le code) : sur l'app **embarquée**, `frame-ancestors https://cockpit.<zone>.pleiade.internal https://admin.<zone>.pleiade.internal` (liste **minimale**, pas `*.pleiade.internal`) — et dans ce cas **retirer `X-Frame-Options: deny`** pour ces routes (sinon il l'emporte selon les navigateurs) ; sur le cockpit/admin, `child-src`/`frame-src` (*`frame-src` hors document*) limité aux origines embarquées ; attribut `sandbox` avec le minimum (`allow-scripts allow-same-origin allow-forms` seulement si nécessaire).
- ⚠ Une iframe de connexion Keycloak **ne doit pas** être autorisée partout : Keycloak pose ses propres `frame-ancestors` (à vérifier dans les en-têtes de sécurité du realm).
- ✅ **postMessage** entre cockpit et apps embarquées : origine cible explicite (R54), contrôle de `event.origin` + schéma JSON (R53, R55) ; jamais `"*"`.
- ✅ **R46** `Cross-Origin-Opener-Policy: same-origin` sur les apps ; ⚠ à tester si une ouverture en pop-up (OIDC en fenêtre, prévisualisation) a besoin de `window.opener` — Auth.js fonctionne par redirection, donc compatible a priori.
- ✅ **R45** : tous les liens `target="_blank"` (liens externes dans les publications du réseau social, articles de presse) en `rel="noopener noreferrer"` — les navigateurs récents appliquent implicitement `noopener` à `target="_blank"` (*hors document*), mais le guide demande de le déclarer explicitement — à vérifier en particulier dans les rendus Markdown/HTML générés hors JSX.

### 6. XSS dans les contenus saisis (réseau social, presse, messagerie, MELMIL) — R4 à R10
- ✅ À vérifier par `grep` sur chaque dépôt : `dangerouslySetInnerHTML`, `innerHTML`, `insertAdjacentHTML`, `document.write`, `eval(`, `new Function(`, `setTimeout("` / `setInterval("` → chaque occurrence justifiée ou assainie (liste blanche de balises).
- ✅ Rendu Markdown/texte riche : assainissement côté serveur **et** affichage par composants React (échappement automatique) ; URLs saisies filtrées (`javascript:`, `data:`).
- ✅ **R6** : API qui renvoient `application/json` ; fichiers téléversés servis avec leur **vrai** `Content-Type` (pas celui fourni par le client) + `nosniff` (*hors document*).
- 🟡 **WordPress (presse)** : CSP via plugin (le guide cite `gd-security-headers`, « non vérifié ») ou via Traefik ; rôles sans HTML non filtré.

### 7. Téléversements (MELMIL pièces jointes, eho portraits)
- ✅ À vérifier : **Annexe A** — un `POST multipart/form-data` **sans en-tête personnalisé** part **sans preflight** : l'endpoint de téléversement est donc **exposé au CSRF** cross-origin si le cookie de session suit (`SameSite=Lax` bloque le POST cross-site, mais **pas** une requête same-site venue d'une autre app `*.pleiade.internal`). → exiger un **jeton CSRF** (R38) ou un **en-tête personnalisé** qui force le preflight (R39) + contrôle `Origin` (R40).
- ✅ Fichiers servis : idéalement depuis une **origine distincte** (principe R52+/R41 : une origine dédiée aux contenus utilisateurs) ou à défaut avec `Content-Disposition: attachment` pour les types non image et CSP `sandbox` sur la réponse (*déclinaison hors document de R52*) ; **SVG** téléversés = vecteur XSS → refuser ou convertir.
- ✅ Portraits eho affichés par les autres apps : chargement en `crossorigin="anonymous"` si aucune authentification n'est requise (R43), sinon passer par l'API de l'app.

### 8. CORS entre apps et clés de service — R39 à R42
- ✅ À vérifier : aucun `Access-Control-Allow-Origin: *` sur une app PLÉIADE (guide : **dangereux pour un intranet**) ; si une app appelle une autre **depuis le navigateur**, `Access-Control-Allow-Origin` = origine exacte, `Access-Control-Allow-Credentials` seulement si nécessaire, contrôle d'`Origin` serveur.
- ✅ **`X-API-Key`** : les appels inter-apps à clé de service doivent rester **serveur à serveur** (route handlers / Server Actions) — la clé ne doit **jamais** apparaître dans le bundle client ni dans `NEXT_PUBLIC_*`. Côté navigateur, un en-tête `X-API-Key` déclencherait un preflight (Annexe A, cas `X-Auth-Token`) et exposerait la clé. ⛔ CORS ne s'applique pas aux appels serveur à serveur (hors champ du guide) : leur sécurité relève du réseau (R11 de REF-10) et de la clé.
- ✅ **R58** : pas de JSON-P ; **R57** : pas de `document.domain` pour faire communiquer les apps.

### 9. Stockage navigateur — LEAC hors ligne, apps temps réel — R23 à R25
- 🟡 **LEAC (tablette hors ligne)** : la notation terrain stockée en **IndexedDB / localStorage** relève de **R24− / R23−** : décision à formaliser par une **analyse de risques** (vol de tablette, JS injecté lisant toute la base de l'origine). À vérifier : aucun jeton d'accès/refresh OIDC en `localStorage` ; données minimales ; purge après concaténation VPN ; envisager un chiffrement applicatif (*hors document*). Rappel du guide : ces stockages sont **effaçables** par l'utilisateur → la synchronisation doit tolérer leur perte.
- ✅ Autres apps : rien de sensible en `localStorage` (préférences d'affichage seulement) ; pas de Web SQL (R25).

### 10. Referrer-Policy — R21
- ✅ À vérifier : en-tête `Referrer-Policy` explicite sur toutes les apps (ex. `strict-origin-when-cross-origin` ou plus strict `same-origin`) — les URL de zone contiennent des noms d'exercice et d'objets ; `unsafe-url` interdit.

### 11. Ressources tierces — R11, R12, R25 (REF-10)
- ✅ À vérifier : aucune ressource chargée depuis Internet (polices Google, CDN) — plateforme fermée et hors ligne ; si une ressource externe subsiste, **SRI** + version figée. 🟡 SRI sur les bundles internes Next.js : option expérimentale du framework (*hors document*) ; à défaut, intégrité garantie par l'image de conteneur.

### 12. MCS — R59 à R63
- ✅ À vérifier : `NODE_ENV=production` dans les images, aucune page de débogage, erreurs génériques côté client ; **contrôle automatisé en CI** empêchant de publier une image en mode dev (R60) ; `npm audit`/Dependabot (R62) ; dépendances inutiles retirées (R61) ; pas de modification de `node_modules` ni de fork non suivi (R63) ; WordPress sans thèmes/plugins préinstallés inutiles (exemple cité par le guide).
- ✅ **Journalisation (§3.7)** : horloges synchronisées entre conteneurs, corrélation Traefik / Keycloak / apps ; pas de données sensibles (jetons, clés `X-API-Key`) dans les journaux d'erreur ; limitation de débit pour éviter la saturation des journaux.

### Hors champ du guide pour PLÉIADE
- ⛔ SSRF (ex. aperçu de liens dans le réseau social qui irait chercher une URL), SQLi, XXE, sécurité Podman/VPN : **explicitement exclus** du guide → traiter avec REF-10 et d'autres références.

---

## Ce qui a vieilli (note 2013 vs guide 2021)

**Ce que le guide 2021 change par rapport à la note 2013 (REF-10)** :
- **HSTS** passe de « mesure supplémentaire » à **recommandation R2** ; TLS 1.2/1.3 remplace la suite de chiffrement Apache de 2013.
- **`X-Frame-Options`** (seule mesure en 2013) devient **secondaire** derrière **CSP `frame-ancestors`**.
- Le **contrôle du `Referer`** contre le CSRF (2013) cède la place à **`SameSite`**, **jeton ≥ 128 bits**, **contrôle d'`Origin`**, preflight CORS ; le `Referer` devient lui-même une **source de fuite** à maîtriser (Referrer-Policy).
- L'échappement serveur (`htmlspecialchars`) est complété par **l'API DOM sûre, la séparation des couches, CSP, SRI, Trusted Types**.
- Le guide 2021 **abandonne** l'infrastructure, l'administration, les mots de passe, la journalisation détaillée et la réaction à incident → **REF-10 reste la référence** sur ces points.

**Ce qui a vieilli dans le guide 2021 lui-même** *(hors document — connaissance générale au 2026-10-01, à vérifier avant d'appliquer)* :
- **`X-XSS-Protection`** : le filtre a disparu des navigateurs majeurs ; seule la valeur `0` garde un sens.
- **`X-Frame-Options: allow-from`** : non reconnu par les navigateurs actuels.
- **`report-uri`** : déprécié au profit de `report-to` / `Reporting-Endpoints` (le guide l'annonçait).
- **`prefetch-src`** et **`block-all-mixed-content`** : abandonnés par la spécification CSP — ne pas compter dessus ; utiliser `default-src` / `upgrade-insecure-requests`.
- **Web SQL**, **`document.domain`** : retirés ou neutralisés par défaut dans les navigateurs récents (le guide l'anticipait).
- **Trusted Types**, **Permissions Policy**, **Fetch Metadata** (`Sec-Fetch-*`), **COEP/CORP**, **Cookie Prefixes** : présentés comme brouillons ou en cours ; ils sont depuis largement implémentés — Fetch Metadata est un bon complément au contrôle d'`Origin`.
- **Attribut `sandbox` `allow-top-navigation`** : le guide le décrit comme « accéder au DOM de la page parente » ; il autorise en réalité la **navigation de la fenêtre principale** — se reporter à la spécification HTML.

---

## Limites / points d'attention

- **Périmètre volontairement restreint** au navigateur : SSRF, SQLi, LFI/RFI, XXE, infrastructure, authentification serveur hors champ.
- **Coquilles relevées dans le document** (à ne pas recopier telles quelles) : exemples de rapports CSP avec `default-src:` / `report-uri:` / `report-to:` (deux-points parasites) ; exemple `Set-Cookie: Domain=cms.fr; sessionId=abc123; …` (le couple nom=valeur doit venir en premier) ; HSTS avec `;` final (toléré) ; dans R36+, phrase redondante ; « s'un site » (note 15).
- **Contradiction interne de l'Annexe A** : la note dit que le téléversement de fichiers par POST « n'entre pas » dans les appels simples, mais le tableau classe `POST` + `multipart/form-data` **sans preflight**. **Prendre l'hypothèse défavorable** : un formulaire `multipart` part **sans preflight** → protéger les endpoints de téléversement par jeton CSRF / contrôle `Origin`.
- **R36+ (PUT)** : la protection vient du preflight, donc d'une configuration CORS **non permissive** ; elle ne protège pas d'une requête same-origin/same-site forgée par une XSS.
- **Plugins cités** (WordPress `gd-security-headers`, Drupal `Security Kit`, `webpack-subresource-integrity`) : « à titre indicatif », **sans visa de sécurité** — à évaluer selon les 4 critères du §6.2.
- **Le guide ne fixe pas de valeur unique** pour `Referrer-Policy`, `SameSite` (Strict vs Lax selon l'usage) ni pour `max-age` HSTS au-delà de l'exemple d'un an.
- **Domaines internes** : HSTS preload et CT logs sont pensés pour l'Internet public ; leur transposition à `*.pleiade.internal` avec CA interne est **partielle** (voir Application).
- Recommandations **non normatives**, « livrées en l'état » ; validation préalable par l'administrateur et le responsable SSI exigée par le document.
- Exemples de code extraits d'un PDF à espacement typographique (`S t r i c t −Transport−Security`) : valeurs reconstituées sans espaces parasites, contenu inchangé.
