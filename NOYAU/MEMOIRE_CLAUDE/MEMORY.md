# MEMORY — Projet MINERVE (D:\CECPC\PRODUCTION\IA\MINERVE)

## Règles transverses et garde-fous
- [⛔ Tester EN LOCAL avant tout push PLÉIADE](feedback_tester_en_local_avant_push.md) — docker run + base + volume, /api/sante 200, opération rejouée ; build ≠ démarrage (incident eho 01/10)
- [⭐ Push prod = mise à jour AUTOMATIQUE de DELATTRE 26](pleiade_push_prod_auto.md) — pas de « Déployer » ; pauser les scénarios AVANT le push (redémarrage social/admin)
- [Règle — Notes de version à chaque push PLÉIADE](feedback_release_notes_pleiade.md) — demande de Xavier (03/10) ; aucun CHANGELOG ni tag prod-* existant
- [Règle — Fenêtres : fermeture au clic extérieur (+ Échap)](feedback_fermer_clic_exterieur.md) — toute fenêtre/liste ouverte par un bouton (09/10)
- [Règle — « animation », jamais « Admin » ; « programmées / en direct »](feedback_vocabulaire_animation.md) — libellés PLÉIADE (06/10)
- [⛔ Essai de refus = donnée jetable](feedback_essai_refus_donnee_jetable.md) — jamais sur une donnée existante, même locale (avatar de démo supprimé le 07/10)
- [⛔ Fichier importé = boucle bornée](feedback_fichier_utilisateur_borne.md) — import Excel 1 048 576 lignes a fait tomber l'Admin (06/10) ; 404 intermittent = redémarrage
- [⚠ Indicateur d'état — mesurer exactement ce qu'on rapporte](feedback_indicateur_etat.md) — tester contre le vrai système ; vérifier un déploiement par `/api/sante`
- [Essai d'image Docker sous Windows — CRLF](reference_essai_image_crlf.md) — construire avec `git -c core.autocrlf=false archive HEAD | docker build -`
- [⚠ « Sans réseau » / ancienne version LEAC / ⊗ = CA de zone non approuvée (mobile ET PC)](reference_ca_zone_mobile.md) — installer pleiade-infra/pki/ca.crt ; absent du poste principal (27/09)
- [Droits GitHub cecpc-pleiade](pleiade_droits_github.md) — press, admin, social, messagerie, cockpit ouverts (01/10) ; push hors mode auto
- [⛔ Dossier interdit — DOC REF\MERCURE\RENS\01_Fiches bio](feedback_dossier_interdit_fiches_bio.md) — ne jamais y accéder sans autorisation
- [⚠ Marquages de diffusion — vérifier le filigrane réel](feedback_marquages_diffusion.md) — signaler, exclure, laisser trancher
- [⛔ Certificats VPN Pritunl — ne jamais les ouvrir](feedback_certificats_vpn_interdits.md) — localiser oui, ouvrir/extraire non
- [Référence — Python exécutable du poste](python_executable_poste.md) — `…\pythoncore-3.14-64\python.exe` ; `python` du PATH = stub Store
- [Règle — Éditer via Edit/Write (hooks)](feedback_edit_tool_pour_hooks.md) — les hooks PostToolUse ne voient pas Bash/Python
- [Règle — Suivre par défaut les propositions des agents experts](feedback_suivre_agents_experts.md) — détails réglés ensuite ; garde-fous (push, sécu) inchangés (10/10)
- [Réflexe — Consulter les agents concernés avant d'affirmer](feedback_impliquer_agents_concernes.md) — croiser plusieurs sources
- [Règle — MAJ simultanée de tous les agents concernés](feedback_agents_obligatoires.md) — jamais après coup
- [Règle — GET, jamais « Europe »](feedback_get_territoire.md) — tout contenu fictif
- [Règle — Numéros de téléphone fictifs](feedback_numeros_fictifs.md) — plages par zone ; Lorraine 03 72 67 XX XX
- [Règle — Cohérence géographique des injects](feedback_geo_coherence.md) — localité vs phase D+ ; sinon formulation vague
- [Règle — Enregistrement chez l'Analyste pays](feedback_analyste_pays_obligatoire.md) — tout personnage MER/ARN/RB, immédiatement
- [Règle — Langue du tweet = langue de l'avatar](feedback_avatar_langue.md) — vérifier dans tweets_data.js
- [Règle — Pas de liens vers des articles futurs](feedback_cross_links_articles.md) — « Related » ≤ même date
- [Règles PPT exercices — pédagogie + agents](feedback_ppt_exercices.md) — actions attendues, objectifs, solutions
- [Prompts image — matériel exact par camp, pas de pancarte vide](feedback_referentiel_materiel_images.md) — IMAGIER\REFERENTIEL_MATERIEL.md

## Système MINERVE / PLÉIADE
- [⭐ LIRE À CHAQUE SESSION — agenda & rappels perso chez SECRÉTAIRE](feedback_rappels_secretaire.md) — SECRETAIRE\MEMOIRE.md § AGENDA ; y ranger tout « rappelle-moi »
- [⭐ Avatars IA — on perfectionne aussi les FICHES INDIVIDUELLES (11/10)](feedback_fiches_individuelles_ia.md) — moteur de groupe + fiche par fiche ; ancrage plus tard ; boucle relevé → PSYCHOLOGUE → corriger-fiches.mjs
- [🤖 Projet avatars animés par IA (10/10) — piloté par PLEIADE](projet_avatars_ia.md) — suivi PLEIADE\PROJET_AVATARS_IA.md ; cadrage Mastodon à traduire vers app-social ; ⏸️ EN PAUSE depuis le 13/10 (moteur 2026-10-13.4 en prod ; reprise : avis PSYCHOLOGUE 22, étape 1)
- [🧭 Projet tutoriel guidé PLÉIADE (08/10)](projet_tutoriel_guide_pleiade.md) — décisions de conception ; ⛔ localhost seul jusqu'au feu vert
- [🔔 À RAPPELER — likes invisibles dans la vue joueurs du social](rappel_likes_vue_joueurs.md) — après la réflexion partage des avatars
- [Système MINERVE — architecture et chemins](project_mercure.md) — CLAUDE.md = source de vérité
- [Renommage système Mercure → MINERVE](rename_systeme_minerve.md) — le pays fictif reste « Mercure »
- [📄 Présentation PLÉIADE par Xavier](reference_presentation_pleiade.md) — PLEIADE\REFERENCES ; draft, le code fait foi
- [⭐ Agent MASTORION (27/07)](agent_mastorion.md) — réseau social ; dépôt en lecture seule sauf autorisation
- [⭐🔒 Agent CYBERSECU (01/10)](agent_cybersecu.md) — référent cybersécu PLÉIADE ; 11 guides ANSSI ; CONSULTER avant tout sujet sécu, METTRE À JOUR après
- [⭐🧠 Agent PSYCHOLOGUE (10/10)](agent_psychologue.md) — psychologie des avatars IA ; 3 sources ingérées ; consulter avant chaque lot de réalisme
- [⭐ Impliquer l'agent DESIGNER (sous-agent), pas seulement sa mémoire](feedback_impliquer_designer.md) — toute question d'ergonomie (07/10)
- [⭐ Agent DESIGNER (24/09)](agent_designer.md) — conseil design UI/UX ; doctrine sourcée DESIGNER\MEMOIRE.md ; contribue, ne tranche pas
- [⏸️ MINERVE Local — RAG (en pause)](minerve_local_rag.md) — Ollama, lecture seule, fiches bio ségréguées

## Exercices
- [⭐ Agent DELATTRE (22/07) — DELATTRE 26](agent_delattre.md) — identité dans DELATTRE\MEMOIRE.md
- [⭐ RETEX MINOTAURE 26](retex_minotaure_26.md) — à lire avant tout nouvel exercice ; 5 leçons
- [✅ AURIGE 7BB / MINOTAURE — clos 03/07/2026](aurige7bb_actif.md) — MINAUTORE = archive de référence
- [AURIGE 7BB = MINOTAURE 26 — dossier ingéré](aurige7bb_minotaure.md) — camps INVERSÉS, Lorraine H-préfixe
- [⚠ Calendrier 7BB avec GELEX](calendrier_7bb_gelex.md) — 29 Jun = GELEX ; 30 Jun = D+39
- [Règle — Agent MINAUTORE pilote le 7BB](feedback_agent_minautore_pilote_7bb.md) — relectures ANALYSTE_ARN / EXPERT_INFLUENCE / SCENARISTE
- [Règle — AURIGE 7BB = ARN, jamais DAC](feedback_dac_vs_arn_7bb.md) — #ARNLibre
- [Bascule AURIGE 2BB → MINAUTORE](transition_minautore.md) — 04/06/2026
- [Récup injects Guillaume 2BB → 7BB](recup_injects_guillaume_2bb_7bb.md) — LO5 fait, gen_lo5_bake.py
- [AURIGE 2BB — Scénario Guillaume](aurige_guillaume.md) — personnages et packages
- [TODO — Visages et voix des 3 ministres Mercure](todo_ministres_mercure.md) — OmniVoice, discours, vidéo à faire
- [Images à créer — AURIGE 2BB](images_a_creer_aurige2bb.md) — 15 images classées
- [Rappel — @NOVUSORDOMUNDI en attente](rappel_novusordomundi_attente.md) — à rejouer avec 07.05.02i/03i
- [Ivan Lubrakov — Min. Intérieur RB](aurige_lubrakov.md) — fermeture des frontières
- [Renommage Bella Russia → Ruthnia Bella](renommage_ruthnia_bella.md) — MELMIL.xls à mettre à jour
- [Fiches bio HN Arnland ingérées](arnland_fiches_bio_hn.md) — détail chez ANALYSTE_ARN
- [Doctrine calibration AURIGE — niveau brigade](aurige_brigade_calibration.md) — catalogue 15 types d'injects
- [AURIGE — Template base exercice](aurige_template_base.md) — SYSTEME\PROMPTS\aurige.md

## Doctrine ILI
- [GLM26 — 5 lignes opératoires](glm26_matrice_ili.md) — référence transversale ; + série 04.01 NRBC HToul
- [EXPERT_INFLUENCE — doctrine ILI](expert_influence.md) — transversal tous exercices
- [ANALYSTE MERCURE — Storm-1516](analyste_mercure_storm1516.md) — référentiel réalisme ILI
- [Doctrine — Mentalité russe ILI](../../EXPERT_INFLUENCE/REFERENCES/mentalite_russe_ili.md) — checklist réflexe rouge
- [Doctrine — Jus ad bellum / in bello](../../EXPERT_INFLUENCE/REFERENCES/jus_ad_bellum_jus_in_bello.md) — lawfare ILI, checklist 7 points

## MASTAURIGE, MELMIL, sites
- [Règle — Consulter + MAJ MASTAURIGE\MEMOIRE.md](feedback_mastaurige_memoire.md) — non négociable, hook en place
- [Mémoire MASTAURIGE scindée MEMOIRE / JOURNAL](memoire_split_convention.md) — agent actif > 150 Ko = scinder
- [MASTAURIGE — agent animation](mastaurige.md) — tweet cards, base 222 avatars ORION 26
- [Règle — Consultation MASTAURIGE avant tout avatar](feedback_mastaurige_consultation.md) — vérifier les CASW
- [MASTAURIGE 7BB — instance MASTER](mastaurige_instance_master_7bb.md) — `…\MASTAURIGE\LOCALSTORAGE_WEB_VERSION`
- [Outillage MASTAURIGE 7BB](mastaurige_instance_7bb.md) — MELMIL D+33-41, storylines 07-01..04
- [Gabarit vierge MASTAURIGE — chemin](mastaurige_vierge_chemin.md) — D:\CECPC\MASTAURIGE\LOCALSTORAGE_WEB_VERSION
- [Vierge MASTAURIGE — portage v0.3](vierge_porting_fin_minautore.md) — ne jamais relancer GENERER_VIERGE.py
- [MASTAURIGE collaboratif — prototype SSE](mastaurige_serveur_collaboratif.md) — à valider sur 2 machines
- [Workflow traitants — édition à la main + fusion](workflow_traitants_fichiers.md) — connexion faible
- [Outils d'optimisation MASTAURIGE](mastaurige_outils_optim.md) — VERIFIER, export 1 clic
- [Pipeline « inject as code »](mastaurige_pipeline_injects.md) — lo_config.js, archi 3 dossiers
- [Réflexe — Lancer VERIFIER en fin de session](feedback_verifier_fin_session.md) — verifier_mastaurige.py
- [JEMM remplace GESTIM — import JSON](jemm_melmil_import.md) — generer_melmil.py unifié
- [TODO — durcir l'import JEMM (lire_existant)](todo_durcir_import_jemm.md) — risque de remplacement total
- [MELMIL v0.2 — matrice par LO](melmil_structure_lo.md) — couleur de card = sphère
- [MELMIL — cohérence des codes](melmil_coherence.md) — doublons corrigés, suffixes
- [MELMIL ↔ MASTAURIGE — navigation](melmil_mastaurige_navigation.md) — ?card=KEY
- [Format codes incident — 2 ou 3 chiffres](melmil_code_3digits.md) — \d{2,3}
- [Convention — relances XX.YY.ZZAi.Rx](convention_injects_relance.md) — relances MELMIL
- [Trombinoscope — photos dans Trombinoscope/img/](trombino_img_convention.md) — auto-contenu
- [Trombinoscope — fiches bio en pop-up](trombino_bios_popup.md) — bios.js
- [Architecture WEB — agrégateur AURIGE 2BB](web_architecture.md) — index_master, exports
- [Méthode — sites web fictifs](methode_web_exercices.md) — HTML autonome Base64
- [Règle — image principale = hero Base64 + vignette](feedback_image_hero_card.md) — embed via Python
- [Chartes documents A4](chartes_documents_A4.md) — Mercure, DR, Biélorussie
- [Charte BC1](charte_bc1_media.md) — navy #12125A + rouge
- [Charte TV4](charte_tv4_media.md) — orange #F5A800 + bleu
- [Charte Site OTAN](charte_otan_media.md) — template nato.int
- [Modèle page EFS](efs_site_base.md) — EFS_Reserves_Faibles_2026.html
- [Référence — portraits Mercure et Ruthnia Bella](reference_portraits.md) — CREATION\02 et \07
- [Règle — Modèle officiel « à l'identique »](feedback_modele_officiel_identique.md) — partir du fichier d'origine, pas d'une grille ; voir un exemplaire rempli
- [Cockpit Situation](projet_cockpit_situation.md) — lots 1-2 en prod le 13/10 ; repris le 14/10, lot 3 (presse) prêt en local, puis vues enregistrées
