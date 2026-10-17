---
name: reference-ca-zone-mobile
description: "Symptôme « Sans réseau — Cette page n'est pas sur l'appareil » (LEAC) ou ⊗ « non sécurisé » sur téléphone/tablette avec VPN actif = autorité interne « Mastorion Internal CA » non approuvée sur l'appareil ; procédure iOS"
metadata:
  node_type: memory
  type: reference
  originSessionId: 699185de-99a6-4263-a321-d605be7e2b29
  modified: 2026-09-28T13:26:07.623Z
---

Constaté le 2026-09-25 sur l'iPhone de l'utilisateur, VPN actif. LEAC affichait « **Sans réseau — Cette page n'est pas sur l'appareil** », alors que l'ordinateur marchait.

**Cause** : les apps de zone (`*.cecpc-div-eval.pleiade.internal`, etc.) présentent un certificat signé par l'autorité **privée « Mastorion Internal CA »**. L'appareil ne la connaît pas, d'où le **⊗** devant l'adresse dans Safari. L'exception « Consulter ce site web » laisse passer la première visite, mais pas les requêtes du **service worker** de LEAC. Celui-ci échoue et affiche sa page `/hors-ligne`.
⚠ Ce n'est **ni le VPN ni le serveur**.

**Correctif, une fois par appareil (iOS)** :
1. Transférer `C:\CECPC\pleiade\pleiade-infra\pki\ca.crt`. C'est le certificat PUBLIC de l'autorité, sans clé, fait pour être distribué (README de `pleiade-infra`).
2. L'ouvrir, puis *Réglages → Profil téléchargé → Installer*.
3. ⚠ **Indispensable** : *Réglages → Général → Informations → Réglages de confiance des certificats* → activer « Mastorion Internal CA ».
4. *Réglages → Safari → Avancé → Données des sites web* → supprimer le site, pour purger le service worker bloqué.
5. Rouvrir avec le VPN : cadenas normal.

**How to apply** : devant ⊗ ou « Sans réseau » sur un mobile alors que le PC marche, penser d'abord à cette autorité. Toute tablette de contrôleur LEAC doit l'avoir installée **avant** le terrain. Vérifier l'émetteur avec `openssl s_client … | openssl x509 -noout -issuer`.
⚠ Ne pas confondre avec les certificats **VPN Pritunl**, qu'il ne faut jamais ouvrir ([[feedback_certificats_vpn_interdits]]).

**⭐ Complément du 2026-09-27 — vaut aussi pour les PC (Chrome/Edge sous Windows)** : même cause, symptôme différent. LEAC reste sur l'**ancienne version**, et changer de page donne « comme pas connecté » (cas d'Axel, puis de l'utilisateur sur son propre poste). Vérifié : l'autorité est **absente du magasin racine Windows** du poste principal. Test rapide : `Invoke-WebRequest https://leac…/api/sante` → « relation de confiance SSL/TLS ». Correctif Windows : double-cliquer `ca.crt` → Installer → Utilisateur actuel → « Autorités de certification racines de confiance », redémarrer Chrome, puis purger le worker (F12 → Application → Service workers, ou effacer les données du site APRÈS avoir synchronisé). Effacer les cookies seuls ne répare que temporairement.

**Android / Samsung (One UI), procédure donnée le 2026-09-28** :
- Télécharger `ca.crt`. ⚠ L'ouvrir ne l'installe pas.
- Installer : Paramètres → Sécurité et confidentialité → Autres paramètres de sécurité → Installer depuis le stockage de l'appareil → **Certificat CA** → Installer quand même → code de verrouillage (**un verrouillage d'écran est obligatoire**) → choisir `ca.crt`.
- Vérifier : Afficher les certificats de sécurité → onglet **Utilisateur** → « Mastorion Internal CA ».
- Chrome et Samsung Internet l'utilisent d'office. Firefox : Paramètres secrets → « Utiliser les certificats d'autorité tiers ».
- Si LEAC avait été ouvert avant : Chrome → Paramètres des sites → Toutes les données des sites → `leac` → Effacer.

**Portée (précisée le 2026-09-27)** : TOUS les appareils sont concernés, les PC compris (Windows, Mac, iOS, Android ; Firefox a son propre magasin). Pour éviter le passage appareil par appareil : GPO pour les PC du domaine, MDM pour la flotte mobile. ⏳ **Fiche d'une page « Installer le certificat de la zone » pour les utilisateurs** : proposée, **reportée à plus tard** par l'utilisateur.

**Complément du 2026-09-25** : l'utilisateur a contourné en ouvrant LEAC dans un **autre navigateur** du même iPhone, et cela a marché. Le blocage tenait donc au service worker gardé par Safari. Contournement immédiat : un autre navigateur, ou supprimer les données du site dans Safari. L'installation de l'autorité reste à faire plus tard, et elle est indispensable pour les tablettes de terrain.

**⚠ Complément du 2026-10-17 — deuxième cause possible sur iPhone, même autorité installée** : les certificats de zone sont signés pour **10 ans** (`pleiade-platform/src/certificat-manager.ts`, `-days 3650` ; constaté sur `delattre-26.pleiade.internal` : 16/09/2026 → 13/09/2036). Apple refuse depuis iOS 13 tout certificat de site TLS valable **plus de 825 jours**, autorité privée comprise. Symptôme : « Connexion non privée » persiste après l'installation et l'approbation de l'autorité. Correctif côté serveur (pas sur l'appareil) : signer pour ≤ 397 jours avec renouvellement, puis régénérer le certificat de la zone (déjà relevé par l'audit du 15/10). Firefox sur iPhone utilise le moteur de Safari : mêmes règles, mêmes réglages.
