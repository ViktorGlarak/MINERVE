# DIAGNOSTIC PLÉIADE — contrôle des apps, besoins, axes d'amélioration (2026-10-03)

> Demandé par l'utilisateur le 2026-10-03. Sources : relevé technique des 12 dépôts (`C:\CECPC\pleiade\`), relevé des mémoires MINERVE (présentation de Xavier, RETEX MINOTAURE 26, DELATTRE, journal PLEIADE depuis le 20/09, CYBERSECU §5, DESIGNER §6, LEAC, MASTAURIGE), sondage de la zone `delattre-26` en production. Faits datés ; les propositions sont en partie 4.

---

## 1. Ce qui tourne réellement (zone `delattre-26`, sondé le 2026-10-03)

| Instance | Usage constaté | Santé technique |
|---|---|---|
| **eho** | 3 983 avatars, ~500 incarnables ; camps, appropriation | version + `/api/sante` ✅ · 109 tests **non lancés en CI** |
| **MELMIL** | planification GT1→GT3, CR partagés, demandes Prod, synthèse — **58 des 130 entrées du journal** | version + sante ✅ · 350 tests en CI ✅ · `gabarits.ts` 8 008 lignes |
| **admin** | scénarios liés aux incidents MELMIL, Kit IA, scheduler | **ni version ni sante** · 31 tests en CI ✅ |
| **social** (1 seule instance) | animateurs « au nom de » ; joueurs DIV1 depuis le 03/10 | **ni version ni sante** · 7 tests **non lancés** · 157 `any` · `multer` 1.x |
| **cockpit** | ajouté le 01/10, resté vide jusqu'à correctif ; ne lit que le social | **ni version ni sante** · **0 test** |
| **messagerie** | animateurs entre eux | sante ✅, pas de version · 9 tests en CI |
| **presse** × 4 (Hexagone, Today Mercure, TV4 International, ⚠ **TF1 Info**) | sites + rédaction | sante ✅, pas de version · 8 tests en CI |
| webserver, wordpress | **non déployés, 0 usage**, 1 commit chacun (11/09), ni README ni CI | — |
| LEAC | zone à part `cecpc-div-eval` ; 25/117 fonctions faites, 48 modélisées | version + sante ✅ · 403 vérifications en CI |

**Vision (Xavier) vs réalité** : la présentation promet plusieurs réseaux (Facebook, Twitter, YouTube…) partageant les mêmes personnages, un cockpit multi-réseaux et une messagerie « où naît la rumeur ». En production : **un seul réseau social**, un cockpit qui n'a qu'une source, une messagerie utilisée par l'animation seule. L'argument « reproductibilité » (catalogue, zones) est tenu ; l'argument « réalisme multi-plateformes » n'est pas encore exercé.

## 2. Pourquoi tout cela existe — les besoins, et ce qui les couvre

Les besoins viennent de trois endroits : la vision de Xavier (entraîner communicants et analystes dans un espace d'information étanche), le **RETEX MINOTAURE 26** (la cellule d'animation) et les demandes de DE LATTRE 26.

| Besoin | Couvert par | Constat |
|---|---|---|
| Planifier et visualiser les injects | JEMM (officiel), **MELMIL**, admin (scénarios), MASTAURIGE MELMIL v0.x | **4 outils** ; MELMIL est devenu le pivot (lien admin↔MELMIL fait) |
| Annuaire des avatars, identités réelles sur les réseaux (RETEX) | eho + social « au nom de » ; trombinoscope MASTAURIGE ; Kit IA | couvert, en double avec MASTAURIGE |
| Sites de presse crédibles | app-press ; `Sites/` HTML MASTAURIGE ; webserver ; wordpress | **4 chemins**, double maintenance déclarée |
| Publication programmée | admin, messagerie, social | 3 schedulers |
| Veille / reporting | cockpit (social seulement) | partiel ; cockpit joueur demandé |
| **Savoir comment les joueurs ont traité les injects** — « le point qui démotive le plus » (RETEX) | **rien de dédié** | ⚠ le besoin n°1 du RETEX n'a pas d'outil |
| Carte de la zone, synthèse des country books, guide/formation aux apps (RETEX) | **rien** | ⚠ |
| Coordination des cellules | MELMIL (Équipe, journal), eho (planches GT) | couvert |
| CR officiels, export pour les autorités | MELMIL | couvert |
| Contrôle des PC | LEAC | couvert, hors ILI |

Lecture : la plateforme a été construite **du côté « produire et diffuser »** (avatars, injects, publications, presse) ; le côté **« observer et boucler »** (ce que les joueurs ont fait de l'inject, mesure de l'effet, retour aux traitants) reste à bâtir, alors que c'est ce que le RETEX réclame en premier.

## 3. Constats transverses

1. **Mise en ligne peu fiable, invisible.** Quatre fois depuis le 21/09, « poussé mais pas déployé » (main sans prod, vieille image, instance neuve sans pull). admin, social, cockpit, platform **n'ont pas de numéro de version consultable** : on ne peut pas prouver ce qui tourne.
2. **Tests inégaux et CI muette.** Aucun workflow ne lance tests, lint ni `tsc` ; seuls les Dockerfiles avec `RUN npm test` testent (platform, admin, press, messagerie, leac, melmil). **eho (109 tests) et social (7) ne sont jamais testés automatiquement ; cockpit n'a aucun test.**
3. **Code dupliqué entre apps** : press/messagerie 29 chemins communs (7 identiques), leac/melmil 14 (copies qui divergent), WordPress OIDC en double (platform + app-wordpress), `vanilla-cockpit` (3 455 lignes, mort depuis le 13/09) à côté d'app-cockpit, `sentinel-*` intouché depuis le 05/08.
4. **Effort concentré sur MELMIL et instable** : 58 entrées de journal sur 130, mais nommage des pièces jointes changé 3 fois, « Confié à » ajouté puis supprimé, comptes rendus retravaillés 4 fois. Le RETEX disait déjà : « les consignes changeantes ont coûté plus que les difficultés techniques ».
5. **Sécurité en pause.** Plan de durcissement « ⏸ en attente de Xavier » ; **E1** (terminal WebSocket sans authentification), **E3** (mots de passe en clair), **E4** (registre d'images ouvert), **E5** (socket Podman root) toujours ouverts ; le tableau §5 n'a pas été mis à jour après les corrections (E2 social, M13, M14 faits mais non marqués). Portail de zone public, lecture anonyme du social ouverte.
6. **Dette de dépôts dormants** : pleiade-infra ne reflète plus le serveur (domaines `mastorion.internal`), certificats versionnés ; webserver et wordpress sans README ni CI ; `pleiade-promouvoir` ne connaît pas LEAC (bloquant à la 2ᵉ mise à jour).
7. **Mémoires désynchronisées** : DESIGNER §6 garde 3 avis « 🟡 » déjà en ligne ; LEAC a un tableau d'avancement contradictoire ; DELATTRE a encore organisateur, lieu, camps « à renseigner ».
8. **Risque de contenu** : un titre de presse en production s'appelle **« TF1 Info »** (média réel) — contraire à la règle « pas de reprise de sites réels » appliquée aux maquettes.
9. **Branches** : tout est fusionné dans `origin/main` (1 branche en suspens dans platform) ; ce sont les `main` locaux qui sont périmés — hygiène à faire, pas une divergence réelle.

## 4. Axes d'amélioration — par priorité

### A. Rendre la mise en ligne prouvable (effort faible, gain immédiat)
- `version.ts` + `/api/sante` dans **admin, social, cockpit, platform** (même contrat que MELMIL).
- Les workflows lancent `npm test` et `tsc` **avant** le build, dans tous les dépôts ; eho et social d'abord.
- Ajouter `leac` à `pleiade-promouvoir` ; règle « instance neuve = pull de l'image » (déjà corrigée côté platform, à vérifier sur le serveur).
- Un tableau « version attendue / version en ligne » par instance dans l'orchestrateur.

### B. Boucler la boucle d'entraînement (le besoin n°1 du RETEX)
- Dans MELMIL, un onglet **« Conduite »** (ouvert à l'exercice) : pour chaque incident, les publications réellement parues (admin/social/presse, déjà liées par code), les **réactions des joueurs** (commentaires, reprises, posts des avatars DIV1 — maintenant possibles) et un champ « effet observé » rempli par le traitant.
- Le cockpit alimente cette vue (il sait déjà lire le social) ; le reporting par groupe de sources devient « effet par inject ».
- C'est ce qui transforme « travailler dans le vent » en retour mesurable, et fournit la matière du prochain RETEX sans ressaisie.

### C. Réduire les doublons (dette et double maintenance)
- Extraire le socle de zone (`lib/zone/*`, routes `/api/service/*`, auth Keycloak, `version`/`sante`) en **un paquet interne** consommé par press, messagerie, leac, melmil, admin, cockpit.
- Supprimer `vanilla-cockpit`, `images/wordpress-oidc` (garder app-wordpress ou l'inverse), geler ou retirer `sentinel-*` si non utilisé pour DE LATTRE.
- **Décider le sort de MASTAURIGE** : conserver uniquement ce que PLÉIADE ne fait pas (ZIP hors ligne, tweet cards imprimables, trombinoscope A3) comme **exports de PLÉIADE**, et cesser la double maintenance des templates de presse.

### D. Stabiliser MELMIL
- Une **spécification figée** des conventions (nommage des pièces, gabarits de CR, statuts, codes) relue par la cellule avant modification ; un changement = une version datée.
- Sortir les gabarits (8 008 lignes) en fichiers de données ; `gabarits.ts` ne devrait contenir que le chargement.
- Rôle lecture seule et journal plus long (demandes ouvertes).

### E. Reprendre la sécurité (avec Xavier)
- Ordre : **E1, E3, E4, E5** (élevés, côté serveur), puis M2 (en-têtes globaux Traefik) et M4 (force brute Keycloak).
- Mettre à jour le §5 de CYBERSECU (marquer E2, M13, M14) ; trancher la lecture anonyme du social et le portail public.

### F. Exploiter la vision multi-réseaux et les joueurs
- Déployer **2 à 3 apparences** du social (Twitter, Facebook, YouTube) pour que le cockpit et « la même identité partout » servent à quelque chose.
- **Cockpit joueur** : désormais simple à cadrer (rôle « Joueurs » existant) — lire les abonnements du joueur avec son propre compte, sans la partie animation.
- Un **guide des apps** par profil (joueur, traitant, chef, Prod) — la formation manquait au RETEX ; le Kit IA en est déjà la moitié.

### G. Contenu et exercice
- Renommer « TF1 Info » (nom fictif).
- Carte de la zone et synthèse des country books : à produire comme fichiers servis par **webserver** (qui trouve enfin un usage) et référencés dans le Kit IA.
- Compléter l'identité DE LATTRE (organisateur, lieu, camps, ETIM) et trancher la graphie MORDVIDCHEV.

### H. Hygiène
- Nettoyer les `main` locaux et les ~40 branches fusionnées de melmil ; mettre pleiade-infra en accord avec le serveur ; corriger DESIGNER §6 et le tableau LEAC.

## 5. Ce que je proposerais de faire en premier (ordre)
1. **A** en entier (une demi-journée) — ça protège toutes les mises en ligne à venir.
2. **G** « TF1 Info » et **E** E1/E4 côté serveur (à planifier avec Xavier).
3. **B** l'onglet Conduite de MELMIL — à concevoir avec DESIGNER et la cellule avant l'exercice (D+27 = 06/10) ou juste après, en mode RETEX.
4. **F** apparences du social et cockpit joueur, **C** socle partagé — après l'exercice.
