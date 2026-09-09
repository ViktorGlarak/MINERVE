# JOURNAL — MASTORION (historique chronologique, append-only)

> Compte-rendus datés des travaux sur la plateforme MASTORION. Les règles et l'état durable sont dans `MEMOIRE.md`.

---

## 2026-07-27 — Création de l'agent + première analyse du repo

- Agent MASTORION créé (21ᵉ agent) selon la checklist CLAUDE.md : registre, compteur NOYAU (20→21), branche ROUTAGE, prompt `SYSTEME\PROMPTS\mastorion.md`, dossier `MASTORION\` (README/MEMOIRE/JOURNAL — convention 2 fichiers dès le jour 1).
- Contexte donné par l'utilisateur : MASTORION = plateforme parallèle à MASTAURIGE, **beaucoup plus performante**, visant les exercices **division/corps**. Le repo `D:\CECPC\MASTORION\mastorion-v0` est un clone GitHub ; le travail passe par MINERVE pour capitaliser le savoir existant et améliorer ensuite la plateforme.
- **Consigne ferme** : aucune modification du dossier `D:\CECPC\MASTORION` pour le moment (lecture seule).
- Première analyse complète du repo effectuée en lecture seule — synthèse consignée dans `MEMOIRE.md` § « Connaissance de la plateforme » ; **rapport intégral** (références `fichier:ligne`) archivé dans `ANALYSE_REPO_2026-07-27.md`.
- Convention de branches posée par l'utilisateur : dans `mastorion-v0`, travail sur la branche **`MEYTRE`** (créée via GitHub Desktop), jamais sur `main` ; MINERVE reste sur `main`. Règle consignée dans `MEMOIRE.md` § Règles.
- Procédure de test local établie (lecture seule du code : `db.ts`, `index.ts` ensureAdmin, `docker-compose.yml`, `.env.prod.example`) : `.env.example` manquant, provider mysql en dur, admin auto-créé. Consignée dans `MEMOIRE.md` § « Procédure de test local ».

## 2026-07-27 (suite) — Mise en route du test local (autorisée par l'utilisateur)

- L'utilisateur a levé la consigne lecture seule pour les **fichiers non versionnés** (installation/test). Docker Desktop installé (étape 0 utilisateur) → blocage WSL absent → `wsl --install --no-distribution` + reboot (utilisateur) → moteur Docker 29.6.2 OK.
- Conteneur `mastorion-db` créé (mariadb:11, port 3306, identifiants `mastorion`, restart unless-stopped).
- `apps/api/.env` créé (mysql localhost, admin `admin@mastorion.local` / `admin123`, JWT local) — vérifié ignoré par git.
- **Découverte bloquante : D: en exFAT** → symlinks npm workspaces impossibles (2 échecs EISDIR reproductibles) → **clone d'exécution créé sur `C:\CECPC\MASTORION\mastorion-v0`** (NTFS, branche MEYTRE, origin→GitHub, .env copié) ; règle consignée en MEMOIRE.
- ✅ **PLATEFORME LANCÉE ET VALIDÉE** : `npm install` OK sur C:, `npm run dev` → API :3000 (v0.2.49) + social :4200 + admin :4201 + cockpit :4202 tous en HTTP 200 ; login admin OK ; `seed:full` exécuté (⚠ découvert : il RESET la base → compte unique `test@test.fr` / `password123`). Premier test utilisateur imminent.
- **Clarifications de périmètre demandées par l'utilisateur** (fin de session) : « où est MASSTALK ? » → l'Admin le remplace intégralement (vestiges : `masstalkUsername`, CLI reconcile) · « ou plutôt RocketChat » → **vérifié par grep : aucune messagerie dans la plateforme**, 0 occurrence dans le repo, rien dans le schéma Prisma → consigné en § « Ce que la plateforme NE fait PAS » + roadmap n°10 (canal messagerie fictive, à clarifier : outil externe CECPC ou brique à concevoir) · « déploiement serveur ? » → confirmé, § « Modèle de déploiement cible ».

## 2026-07-28 (suite) — Audit de la classification par les 4 agents-experts

- Déclencheur utilisateur : `@6e_Army`/`@20e_Army` en MER - POLITICIEN. Correction de la règle (groupe « officiel » = statut ≠ métier → croiser `activite`).
- 4 agents saisis en parallèle, chacun lisant sa mémoire avant de juger : **ANALYSTE** (Mercure), **ANALYSTE_ARN**, **ANALYSTE_BOT** (+France+transverses), **MINAUTORE+GUILLAUME** (emploi éditorial réel dans les injects). ~70 corrections appliquées dans `OVERRIDES`.
- **2 bugs de parsing découverts grâce à l'audit** (l'AIEA signalée absente par ANALYSTE_BOT) : séparateur de la 1ʳᵉ fiche + pseudos à apostrophe/espaces → **29 fiches récupérées, 220 → 249 personas**.
- Points doctrinaux : règle des comptes à façade (nature > masque), anti-inversion Bothnia (Tikhanov/Saniki = opposition PRO-MER), acteurs économiques ARN sortis de « patriote », milice TANTALE en groupe clandestin.
- Résultat intermédiaire : 49 groupes, 0 non-classé. 4 arbitrages soumis à l'utilisateur.
- **Arbitrages tranchés le même jour** : (1) Titane ramené sous MER, code TIT supprimé ; (2) pas de région française réelle → `@clambroise55` en ARN ; (3) `@GavrilovBorislav` = sergent MER d'après sa bio (⚠ contredit la revue 7BB du 21/06 — injects à revoir) ; (4) homonyme `@Kozi_Aus` exclu. Classeur final : **248 personas, 47 groupes**.

## 2026-07-28 (suite) — Annuaire visuel de lecture (demande utilisateur)

- Nouveau classeur `RECAPS\ANNUAIRE_PERSONAS.xlsx` : rendu esthétique, filtres natifs, code couleur camp/pays, tableau de bord avec graphiques — pour la lecture humaine, hors format d'import. Généré par `OUTILS\generer_annuaire_visuel.py`, qui réutilise `generer_bibliotheque.construire()` (source unique, cohérence garantie avec le fichier d'import).
- 🐛 Bug trouvé en le construisant : le champ `pays` des personas transverses (ONG, institutions, animation) valait l'artefact CASW brut `"Animation"` au lieu de rester vide — ce champ alimente le profil importé dans MASTORION. Corrigé dans `generer_bibliotheque.py` ; les deux classeurs régénérés et vérifiés (AIEA/Amnesty/CICR ont bien `pays` vide désormais).

## 2026-07-28 — Refonte de la taxonomie des groupes

- Constat utilisateur après import dans MASTORION : **55 groupes** hérités de CASW, souvent à 1 membre, libellés à rallonge. Demande : repenser les groupes en `PAYS - FONCTION` (MER - POLITICIEN, ARN - JOURNALISTE, ARN - PACIFISTE…), « tout détailler pour que ce soit très bien rangé ».
- Bug corrigé dans `generer_bibliotheque.py` : `charger_casw()` capturait les puces de la **section biographie** comme des groupes → restreint à la section `### Groupes`.
- Nouvelle taxonomie implémentée (tables `PAYS_CODE`, `MAP_CASW`, `MAP_EHO`, `MAP_ACTIVITE`, `MOTIFS_INSTITUTION`, `OVERRIDES`) + **cumul de groupes** par persona. **55 → 35 groupes**, 6 singletons légitimes, 2,2 groupes/persona, 0 « NON CLASSE ».
- 4 pièges identifiés et documentés en MEMOIRE (regex `\bun\b`/`\beu\b`, `\d{2}` = faux département alors que la Lorraine H-préfixe du 7BB est arnlandaise, pays « ANIMATION » masquant les institutions, personas multi-groupes).
- Classeur régénéré ; README bibliothèques mis à jour avec le tableau pays × fonctions.

- 📊 **Récap des injects joués généré** (demande utilisateur) : `RECAPS\RECAP_INJECTS_GUILLAUME_MINOTAURE.xlsx` — onglets GUILLAUME (70 injects/176 produits) et MINOTAURE (84/105), avec types de produit. Script `OUTILS\generer_recap_injects.py` + `RECAPS\README.md`. Mise au point : lecteur JS tolérant nécessaire (commentaires internes + **clés non quotées côté 2BB**) ; sources de produits différentes par exercice (index typé 2BB vs `articles_data.js` 7BB). 3 écarts de source documentés (22 injects 2BB hors MELMIL, 4 injects sans produit, 9 HTML 7BB non déclarés).
- ⭐ **1ʳᵉ bibliothèque de personas générée** (demande utilisateur) : `BIBLIOTHEQUES\BIBLIOTHEQUE_TEST_3_EXERCICES.xlsx` — 220 personas (MINOTAURE 35 + GUILLAUME 13 + ORION 222, dédoublonnés), 3 onglets = 3 camps, priorité bio MINOTAURE > GUILLAUME > ORION. Script `OUTILS\generer_bibliotheque.py` + `BIBLIOTHEQUES\README.md`. Sources en lecture seule (avatars.js 7BB/2BB, bios.js EHO, registre MASTAURIGE, CASW ORION). 4 itérations de mise au point : heuristique du registre captait des libellés d'injects → filtres ajoutés ; commentaires d'`avatars.js` d'abord sur-appliqués (en-tête et séparateurs `====` pris pour des descriptions) → capture restreinte à l'intérieur du tableau + seuil de lettres. Validé : 0 doublon, colonnes conformes à l'import.
- **Outillage sauvegarde/restauration créé** (question utilisateur « peut-on repartir sur une base vierge ? ») : dossier `C:\CECPC\MASTORION\SAUVEGARDES\` avec `BASE_VIERGE.sql` (état de référence figé : 1 user, 0 groupe/scénario/post), `SAUVEGARDER.bat` et `RESTAURER.bat` (base + images, confirmation « OUI »). Mécanisme **testé** : groupe témoin inséré → restauration → disparu, user conservé. Analyse au passage de `resetDb()` : ne supprime pas la table `groups`.
- **Audit de la mémoire de l'agent** (demande utilisateur : « ces notions sont-elles bien assimilées ? ») → 1 règle devenue fausse corrigée (§ périmètre d'écriture : la lecture seule stricte ne vaut plus que pour D:, l'exécution est autorisée sur C:, le code source reste sous autorisation) + 3 manques comblés (MASSTALK↔Admin, absence de messagerie, roadmap n°10) + 1 ligne obsolète supprimée (« Sentinel hors périmètre »).

- ✅ **SENTINEL MONTÉ** (demande utilisateur) : découverte que turbo dev lance déjà sentinel-api (:3100) + sentinel-ui (:4203, repli de port silencieux) ; modèles Ollama natifs pullés (qwen2.5:3b + snowflake-arctic-embed:137m) ; conteneurs sentinel-pg (pgvector, :5433) + sentinel-worker buildés/démarrés via compose overlay ; bug résolu : secret JWT divergent entre api et sentinel-api (« Token invalide ») → `.env` aligné sur `mastorion-dev-secret` + redémarrage dev ; validation : `/api/sentinel-health` = status ok, 8 tables `sentinel_*` créées par le worker dans pgvector. Détails durables en MEMOIRE.

## 2026-09-09 — Réseau RZO + 54 fiches EHO manquantes → bibliothèque 248 → 404 personas

- Suite du portage EHO éditable côté MASTAURIGE (vierge) : l'utilisateur demande de vérifier si les comptes nouvellement découverts (réseau RZO 107 acteurs, section addendum) existent dans `BIBLIOTHEQUE_TEST_3_EXERCICES.xlsx`. Vérifié précisément : addendum déjà couvert (0 manquant, source commune `avatars.js`) ; RZO totalement absent (`generer_bibliotheque.py` ne lisait jamais `rzo_data.js`).
- **Découverte plus large** : 54 des 59 fiches `bios.js` (EHO) n'avaient jamais été importées — tout le gouvernement/commandement militaire/clergé des deux pays (présidents, ministres, préfets, maires, généraux, évêques) — car `construire()` ne créait un persona qu'à partir d'un compte **avec handle** (avatars.js/CASW), l'EHO ne servant qu'à enrichir une bio déjà repérée. Beaucoup de RZO recoupent ces 54 (ex. Nadia Promesy = même personne côté RZO et côté EHO).
- Question posée à l'utilisateur (3 options) → **intégration complète sans doublon** choisie.
- Implémentation `generer_bibliotheque.py` : `construire()` étendu (ajoute les fiches EHO sans handle, `@<id_eho>` synthétique) + nouvelle fonction `fusionner_rzo()` (fusion par nom si déjà présent — tag `RESEAU RZO` + `GROUPE CLANDESTIN` si réseau HFM/NOM/Redskulls — sinon fiche légère créée) + classificateurs `classer_rzo_fonction`/`classer_rzo_pays`.
- 🐛 2 bugs trouvés et corrigés en vérifiant : (1) « Pro-MER » classé à tort comme nationalité mercurienne (corrigé en `ARN - PRO-MERCURE`, cohérent avec l'audit à 4 agents) ; (2) `norm()` vide silencieusement un nom 100 % cyrillique → 3 acteurs RZO (Алексей Аксёненко/Сюзанна Светличная/Капитан Хэдок) fusionnés à tort en une seule fiche (corrigé par repli sur le nom brut minuscule quand `norm()` renvoie vide — piège à retenir pour tout futur générateur).
- **Résultat vérifié : 404 personas, 0 doublon username/email**, cas de fusion contrôlés un par un (Promesy/Adriane/Danevois/Martin : bio complète conservée, tag réseau ajouté, aucun doublon). `generer_annuaire_visuel.py` aligné (appelle aussi `fusionner_rzo()`).
