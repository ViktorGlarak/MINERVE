# MÉMOIRE — MASTAURIGE

## Création
Agent créé le **2026-05-24** pour la génération de contenus RS fictifs dans les exercices de type AURIGE (entraînement PC niveau brigade). MASTAURIGE est INDÉPENDANT de Mastorion — pas de lien avec la plateforme fictive ORION 26.

---

## Distribution par exercice

| Exercice | Mode de distribution | Statut |
|---|---|---|
| AURIGE 2BB | HTML statique ZIP offline (`WEB/index.html`) | Actif |
| Exercices AURIGE futurs | HTML statique ZIP offline (même format) | Extensible |

---

## ⚠ RÈGLE OBLIGATOIRE — Consultation MASTAURIGE avant toute création d'avatar

> **Tout nouvel avatar RS fictif pour un exercice Mercure doit être déclaré ici AVANT production.**
> S'applique à TOUS les agents : NOYAU, GUILLAUME, EXPERT_INFLUENCE, ANALYSTE, SCÉNARISTE, et tout futur agent.
> Processus : (1) vérifier si l'avatar existe dans CASW ORION 26 → (2) si non, créer une fiche dans `avatars_casw_aurige2bb.md` → (3) mettre à jour ce registre.
> Créer sans consulter = doublon possible, contradiction de profil, perte de traçabilité.

---

## Avatars utilisés — AURIGE 2BB (registre au 26 mai 2026)

### Avatars issus de la base CASW ORION 26
→ Fiches complètes dans `CASW/avatars_casw_orion26.md`
→ Avatars recommandés par camp dans `CASW/PROCESS_TWEETS_AURIGE.md` section 7

| Handle | Nom | ID CASW | Camp | Injects AURIGE 2BB |
|---|---|---|---|---|
| @HmunikVoice | Pavlus Juri Gautoreif | 3727 | 🔴 Rouge | 07.01, 07.02, P-02, P-05c, P-07a, P-11, P-15, P-17, P-18 |
| @NOVUSORDOMUNDI | NOVUS ORDO MUNDI | 3691 | 🔴 Rouge | 07.02 |
| @ArnlandLovePeace | Clémence Gavaloff | 1392 | 🔴 Rouge | 07.05 |
| @MaiaKovalenko | Maïa Sokhaguvka | 3726 | 🔴 Rouge | 07.04 |
| @BelovDimitri | Dimitri Belov | 1851 | 🔵 Bleu | 07.05 |
| @GromovaYelena | Yelena Gromova | 1845 | 🔵 Bleu | 07.01 |
| @IndependentArnish | Arnish Independent | 3510 | 🔵 Bleu | 07.02 |

### Avatars nouveaux — spécifiques AURIGE 2BB
→ Fiches complètes dans `CASW/avatars_casw_aurige2bb.md`
→ Créés le 26 mai 2026 **sans consultation préalable** (corrigé rétroactivement)

| Handle | Nom affiché | Initiales | Camp | Rôle | Injects |
|---|---|---|---|---|---|
| @EastWatch_Intl | EastWatch International | EW | 🟡 Pseudo-neutre | Relais analytique — blanchiment progressif MER | P-03, P-04, P-08, P-09, P-12, P-20 |
| @CorrespondantEst | Correspondant Est | CE | 🟡 Pseudo-neutre | Correspondant terrain — couche 2 piège rétroactif | P-14, P-16 |
| @TemoignageDAC | Témoignage DAC | TD | 🔴 Rouge (camouflé civil) | Couche 1 flou architecture déni Storm-1516 | P-05a |
| @VoixDACia | Voix DACia | VD | 🔴 Rouge (camouflé civil) | Voix anti-guerre / anti-mobilisation DAC | P-06 |

---

## Hashtags actifs — AURIGE 2BB

| Hashtag | Camp | Thème |
|---|---|---|
| #NATOInvaders | Rouge | Convois OTAN Lorraine |
| #FuckNato | Rouge | Anti-OTAN radical |
| #ALERTE | Rouge | N.O.M — événement urgent |
| #NATOBetrayDAC | Rouge | Trahison OTAN sur troupes DAC |
| #NATOIllegitimate | Rouge | Délégitimation juridique OTAN |
| #StopWar | Rouge | Antiwar / voix civiles |
| #NonALaGuerre | Rouge | Anti-mobilisation @VoixDACia |
| #ContraOffensive | Rouge | Contre-offensive MER D+38 |
| #LePiège | Rouge | Révélation narrative piège rétroactif |
| #StratégieGagnante | Rouge | Supériorité stratégique MER |
| #TémoignagesDAC | Rouge | Architecture déni couche 3 |
| #CrimesDeGuerre | Rouge | Amplification accusations 2BB |
| #HSARREBOURG | Gris/tous | Ville événement clé D+35 |
| #HSARREGUEMINES | Gris/tous | Axe contre-offensive D+38 |
| #ZURB | Gris/tous | Zone urbaine résidentielle |
| #EastWatch | Gris/neutre | Marque @EastWatch_Intl |
| #FinOffensive | Gris/neutre | Fin offensive US DIV D+36 |
| #StrongerTogether | Bleu | Soutien OTAN |
| #StandWithArnland | Bleu | Solidarité Dacie Romanie |
| #StandWithDaciaRomania | Bleu | Solidarité DAC (variante) |
| #NATOForFreedom | Bleu | Pro-OTAN @BelovDimitri |
| #Lorraine | Gris/tous | Ancrage géographique |
| #Sarrebourg | Gris/tous | Ville événement |

---

## ⚠ Point ouvert — badges camp dans index_master.html

La règle du 2026-05-25 stipule : pas de badge camp visible sur les cartes tweet (les stagiaires doivent classifier eux-mêmes).
En pratique, tous les tweets de index_master.html ont `<div class="camp-badge rouge/bleu">` visible.
**Hypothèse validée :** index_master.html est l'outil animateur — badge acceptable pour le tri. Ne pas reproduire dans une éventuelle vue stagiaire.
**À confirmer par l'utilisateur.**

---

## Règles apprises

### [2026-05-25] Neutralité visuelle des tweets — AURIGE 2BB
Les tweets produits pour AURIGE 2BB ne doivent comporter **aucun indicateur visuel de camp** :
- Pas de bordure colorée (rouge/bleu) sur les cartes tweet
- Pas de badge "PRO-MERCURE" / "PRO-OTAN"
- Pas de couleur de camp sur les avatars — tous gris neutres (#80868b)
- Tous les tweets doivent être visuellement identiques

**Raison :** la cellule stagiaire doit classifier elle-même les comptes selon son analyse. L'IA ne doit pas orienter cette classification par des codes visuels.

**Conséquence pour la production :** ne jamais ajouter de classe `camp-rouge`, `camp-bleu`, `tweet-camp` ou `tweet-avatar.rouge/bleu` dans les nouvelles cartes tweet.

### [2026-05-24] Distribution AURIGE 2BB
Les tweets AURIGE ne passent pas par MASSTALK V3 — ils sont intégrés directement en HTML dans `WEB/index.html` (section `data-category="social"`). Le système NEW badge + localStorage track les tweets lus via leur @handle.

### [2026-05-24] Avatars ORION 26 réutilisables pour AURIGE 2BB
Les avatars de la base ORION 26 sont génériques (journalistes, militants, ONG) et fonctionnent pour AURIGE 2BB. Adapter le contenu des posts au contexte Lorraine sans modifier les profils.

---

## Sessions de production
<!-- À compléter au fil des sessions -->
| Date | Exercice | Thème animé | Avatars | Nombre de posts |
|---|---|---|---|---|
| 2026-05-24 | AURIGE 2BB | Convois OTAN Lorraine + N.O.M | 4 avatars | 4 cards HTML |
