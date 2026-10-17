# Avis DESIGNER n°119 — 2026-10-17 — PLÉIADE en application installable (PWA du portail, maquette locale)

> **Demande utilisateur** : « fais-moi la version PWA de PLÉIADE en localhost », puis « analyse avec DESIGNER et CYBERSECU pour voir si tout est bon ».
> **Objet revu** : maquette `C:\CECPC\pleiade\dev\pwa` (non versionnée) — portail DELATTRE-26 en tuiles vers les vraies apps, manifeste, icônes générées du logo, service worker, page hors ligne.
> Revue sur captures ordinateur 1280, iPhone 13, iPhone SE, et sur les icônes à 16, 32, 48, 96, 192, 512 px.

## Verdict : à reprendre — 12 corrections, appliquées le même jour
1. **Pictogrammes des applications** : vignettes PNG disparates → une famille unique, Lucide, trait 2 px, craie sur carré `#212327` arrondi 8 px (Social `users`, Messagerie `message-square`, Cockpit `radar`, Animation `clapperboard`, Moteur IA `bot`, MELMIL `layout-grid`, Identités `fingerprint`).
2. **Bandeau d'installation** : toujours affiché, « Ouvert dans le navigateur » inutile → affiché seulement s'il y a une action (bouton « Installer » si le navigateur le propose, consignes « Partager → Sur l'écran d'accueil » sur iPhone), masquable et mémorisé, rien une fois installée.
3. **Zone injoignable** : état discret en haut à droite seulement → bandeau d'alerte « Zone injoignable. Connectez le VPN de la zone, puis Réessayer », tuiles estompées avec « nécessite le VPN », couleur d'alerte `#f87171`.
4. **Page hors ligne** : générique → « DELATTRE-26 ne répond pas », deux vérifications (VPN, réseau), bouton Réessayer.
5. **Téléphone (< 600 px)** : tuiles en grille de 2 trop petites → liste (lignes 64 px, pictogramme 40 px, nom 16 px, description 13-14 px, chevron).
6. **Sous-titres** : redites du nom → ce que l'on y fait (« Préparer et lancer les scénarios », « Planche des injects »…).
7. **Sections** : une seule liste → Animation (Animation, Cockpit, Moteur IA, MELMIL) / Réseaux sociaux & Messagerie / Identités et fichiers.
8. **Typographie** : police système → Archivo hébergée sur place (`@font-face`) ; titres de section 14 px en casse normale ; pied 12 px en casse normale (pas de capitales espacées sous 12 px).
9. **iPhone** : contenu sous la barre d'état → marges de sécurité sur l'en-tête et le pied (`env(safe-area-inset-*)`), pas sur le corps.
10. **Icône d'application** : étoiles minuscules à 48 px et moins → deux dessins : grand (512, 192, iPhone 180) avec réticule épaissi, petit (masquable, 96, 48, favicons, badge) recadré sur les étoiles seules.
11. **Bouton de notification d'essai** : visible de tous → seulement avec `?essai`.
12. **Manifeste** : nom « PLÉIADE — DELATTRE-26 », icônes 48/96/192/512 + masquable, raccourcis Messagerie / Réseau social / Cockpit.

## Arbitrages laissés à l'utilisateur
- Nom court sous l'icône : « PLÉIADE » (une seule appli quelle que soit la zone) ou le nom de la zone (« DELATTRE 26 »).
- Un lanceur unique (le portail) ou une PWA par application.
- Écrans de démarrage iPhone (images par taille d'écran) : à faire seulement si l'appli est retenue.
- Notifications poussées : passent par Apple / Google, donc par Internet (voir CYBERSECU).

## Règle générale
**Une icône d'application se dessine pour 48 px**, pas pour 512 : ce qui ne se lit pas à 48 px (réticule fin, petites étoiles) disparaît du petit dessin ; garder deux dessins, le grand et le petit.
