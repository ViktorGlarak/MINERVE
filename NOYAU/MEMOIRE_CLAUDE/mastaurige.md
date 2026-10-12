---
name: mastaurige
description: "Agent MASTAURIGE — animation Mastorion exercices, workflow tweets CASW → HTML index.html"
metadata: 
  node_type: memory
  type: project
  originSessionId: 73fcca0d-c040-42d3-9859-fa36df54c216
---

MASTAURIGE est le 14e agent du système MINERVE, créé le 2026-05-24.

**Rôle :** Animation Mastorion pour tous les exercices (ORION 26, AURIGE 2BB...). Génère des tweets en incarnant les avatars CASW, produit des tableaux MASSTALK V3 et des blocs HTML tweet card pour `index.html`.

**Modèle :** mistral-nemo:latest (partagé avec MASTODONTE, SCÉNARISTE, SECRÉTAIRE, VOIX)

**Distinction MASTODONTE vs MASTAURIGE :**
- MASTODONTE = expert API Mastodon (technique, OAuth, endpoints)
- MASTAURIGE = expert contenu exercice (avatars, tweets, HTML)

**Fichiers clés :**
- Prompt : `SYSTEME/PROMPTS/mastaurige.md`
- Mémoire agent : `MASTAURIGE/MEMOIRE.md`
- Base avatars CASW : `MASTAURIGE/CASW/avatars_casw_orion26.md`
- Règles format : `MASTAURIGE/CASW/agents_rules_orion26.md`
- Process complet : `MASTAURIGE/CASW/PROCESS_TWEETS_AURIGE.md`

**Workflow tweet AURIGE 2BB :**
1. MASTAURIGE génère tableau `| id | account_id | compte | message | nb_likes | nb_retweets | reply_to | delta |`
2. Conversion manuelle en blocs `.tweet-card` HTML
3. Insertion dans `WEB/index.html` section `data-category="social"`
4. ZIP distribué avec les articles — aucune manipulation supplémentaire

**Architecture tweet card HTML :**
- Classe : `article-card tweet-card camp-[rouge|bleu|gris]`
- onclick : `markTweet(this, '@handle')` (pas openCard — pas de navigation)
- NEW badge : tracké en localStorage via @handle (clé `aurige2bb_viewed`)
- Initiales avatar : 1ère lettre Prénom + 1ère lettre Nom

**Avatars AURIGE 2BB prioritaires :**
- Rouge : @HmunikVoice (Gautoreif), @NOVUSORDOMUNDI (NOM), @ArnlandLovePeace (Gavaloff)
- Bleu : @IndependentArnish, @GromovaYelena, @BelovDimitri
- Gris : @IAEA_AIEA_off, @Amnesty_International

**Fonctionnalités animateur index_master.html (ajout 2026-05-27) :**

Le fichier maître `index_master.html` (animateur, `data-master="1"`) embarque des outils d'animation en temps réel invisibles dans les exports stagiaires :

- **`.card-right-panel`** — panneau flottant absolu centré verticalement à droite de chaque card (`top: 50%; transform: translateY(-50%)`), flex-column avec gap 8px
  - **`.card-status-wrap`** (en haut) : sélecteur ⬜ En cours / 🟠 Finalisé / ✅ Envoyé — persistance localStorage
  - **`.card-datetime-wrap`** (en dessous) : sélecteur Jour (26 Mai → 04 Jun + **"En attente"**) + champ Heure — repositionne la card dans le DOM en temps réel
- **Option "En attente"** dans le sélecteur de jour : place la card dans un filtre spécial (bouton orange "En attente" dans la barre de jours) — pour les injects non encore planifiés. Persistance localStorage (`card-attente-KEY`).
- **sessionStorage** : état complet de la navigation (onglet, jour, mode, recherche, scroll, classification) sauvegardé avant chaque ouverture d'article — restauré automatiquement au retour.

**Construction du panel :** `initDateTimeEditors()` retire le `.card-status-wrap` créé par `initStatusSelects()`, le déplace dans `.card-right-panel`, ajoute `.card-datetime-wrap` en dessous, appende le panel à la card.

**Exports stagiaires (generate) :** tous les éléments animateur (`.card-right-panel`, `.card-status-wrap`, `.card-datetime-wrap`, `.camp-badge`, `.classify-btn`, `.publish-toggle`, `.anim-icon-row`) sont supprimés par les 3 fonctions generate avant l'export.

**Why:** [[project_mercure]] — décision prise 2026-05-24 : MASTAURIGE distinct de MASTODONTE pour séparer expertise technique (API) et expertise contenu exercice (avatars/animation).

## Règles canoniques médias fictifs AURIGE 2BB (2026-05-29)

**Langues par site :**
| Site | Langue | Raison |
|---|---|---|
| Today Mercure | **Anglais exclusivement** | Média international fictif de Mercure |
| Bella Channel 1 | **Anglais** | Audience internationale fictive |
| TV4 International | **Anglais** | Média occidental international |
| Tweets civils FR | Français | @clambroise55, @MarionKessler57 — locaux lorrains |
| Tracts MAF | Français | Ciblage soldats francophones |
| Courriers institutionnels | Français | Maires, préfets — contexte DR |

**Profil canonique Aleksander Vorin (tireur d'élite 41e Division) :**
- Cible : **capitaines de compagnie** et chefs de section (commandants de contact)
- PAS de colonels/LTC — uniquement les officiers qui commandent sur le terrain
- Bilan 29 Mai : 11 engagements confirmés dont 1 capitaine FR identifié
- Portrait source : `D:\CECPC\PRODUCTION\CREATION\02 - MERCURE\Portraits\MER_Aleksander VORIN_sniper_tueur_de_CDU.png`
- Pour utiliser dans article TM : copier vers `WEB\images\MER_VORIN_sniper.jpg`
