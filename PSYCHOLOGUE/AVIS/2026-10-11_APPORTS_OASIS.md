# Avis n°6 — Les 4 apports d'OASIS valent-ils le coup pour le réalisme ? (2026-10-11)

> **PSYCHOLOGUE → PLEIADE (moteur `moteur.mjs`, pont `pont.mjs`), EXPERT_INFLUENCE, DESIGNER.** Matière : `PLEIADE\REFERENCES\OASIS_camel-ai.md` (analyse PLEIADE du dépôt `camel-ai/oasis` et de l'article arXiv 2411.11581). Question de l'utilisateur : ces idées **améliorent-elles vraiment le réalisme** du système de sociabilité ? Décisions déjà prises : génération de fiches en masse → plus tard ; « interview » → couverte par le chat + journal « pourquoi ».
> Règle de lecture : OASIS est un simulateur de foule validé sur des données réelles ; nous animons des **personnages** face à de vrais joueurs. Je ne prends que ce qui rend un avatar plus humain **aux yeux d'un entraîné**, pas ce qui rend une foule plus mesurable.

## 1. Vecteur d'activité sur 24 h — **OUI, en complément de `rythme`, pas à sa place**

**Pourquoi.** Le rythme lever / travail / coucher est binaire (éveillé ou non) ; or l'usage réel des réseaux a des **pics** (réveil, pause déjeuner, soirée) et des **creux** actifs (en réunion, en caisse) — OASIS le tire de données réelles, et c'est une connaissance robuste *(chronotypes et courbes d'usage des réseaux — à sourcer)*. Psychologiquement, deux gains : (a) les avatars cessent de revenir **tous** toutes les 10-30 min au même tempo (la synchronicité « 21:57 » de l'avis n°5 est un défaut de ce type) ; (b) un militant qui poste à 2 h du matin et un commerçant qui disparaît de 9 h à 19 h deviennent **lisibles** sans qu'on l'écrive dans une consigne.

**Spécification.**
- Champ `activite[24]` : 24 valeurs **0-1** = probabilité qu'au retour au fil de l'heure h l'avatar **ouvre vraiment** le réseau. `rythme` reste : sommeil = `activite` forcée à 0 entre coucher et lever (sauf insomnie : anxiété ≥ 0,7 → 0,10 de 23 h à 1 h) ; `travail` **n'est plus un interdit** mais un facteur (× 0,3 pour un métier « mains occupées », × 0,8 pour un métier d'écran).
- **Dérivation** depuis la fiche : gabarit par **métier** (base) × modulations : extraversion (`× (0,7 + 0,6·E)`), âge (< 25 ans : soirée +0,15, matin −0,1 ; > 60 ans : inverse), anxiété ≥ 0,6 (nuit +0,1 : il regarde son téléphone), relais en campagne (`max(v, 0,5)` de 7 h à 1 h). Puis normaliser pour que la **somme × fréquence de retour** respecte le budget journalier (2 + 8·E).
- **4 gabarits** (h0 → h23) :
  - *Étudiant (Esteban)* : 0,05 0,05 0 0 0 0 0,1 0,3 0,5 0,3 0,3 0,4 0,7 0,5 0,3 0,3 0,4 0,5 0,6 0,7 0,8 0,9 0,8 0,4
  - *Commerçant / artisan (Anastasia)* : 0 0 0 0 0 0 0,2 0,7 0,5 0,15 0,1 0,15 0,7 0,4 0,1 0,1 0,15 0,2 0,6 0,8 0,8 0,7 0,4 0,1
  - *Élu (Mordvidchev)* : 0 0 0 0 0 0,1 0,5 0,8 0,7 0,4 0,3 0,4 0,6 0,5 0,4 0,4 0,5 0,6 0,7 0,6 0,6 0,5 0,3 0,1
  - *Militant en campagne (Untergang)* : 0,4 0,3 0,1 0 0 0 0,3 0,7 0,8 0,7 0,7 0,8 0,8 0,8 0,7 0,7 0,8 0,9 0,9 1 1 1 0,9 0,7
- **Interaction avec le retour au fil et les plafonds** : le retour (10-30 min, 4-10 pour un militant) devient le **tirage** ; à chaque retour, on tire `u < activite[h]` → sinon il « n'a pas regardé » (mémoire inchangée, aucun effet). Les plafonds horaires (1 + 3·E) restent la borne dure. Une **interpellation** (@mention, MP, réponse) force la lecture si `activite[h] ≥ 0,1` (il regarde ses notifications) avec délai 2-15 min ; dans le sommeil, lue au réveil. Variante crise : l'animation peut appliquer un **coefficient de crise** global (× 1,5 plafonné à 1) — une nuit de pillages, tout le monde veille.

## 2. Sélection des lecteurs par ressemblance — **OUI, c'est l'« attention » que la doctrine réclamait (REF-02, LIDA)**

**Pourquoi.** Un humain ne lit pas tout son fil : il remarque ce qui le concerne, ce qui vient de ses proches, ce qui est déjà bruyant, et une part de hasard. C'est exactement l'« attention compétitive » du §3.2 et le point « fil vu / bulles » du lot 3. OASIS le fait par un RecSys ; chez nous le **score de remarque** doit être **psychologique**, pas seulement sémantique — sinon on recrée une bulle de filtre parfaite, et plus personne ne voit un contenu adverse (ce qui tuerait l'effet des injects).

**Score de remarque** (0-1, par couple message × avatar ; on retient les 30-50 meilleurs + une **poche de hasard**) — poids indicatifs :
| Composante | Poids | Règle |
|---|---|---|
| Mention / réponse / MP | **1,0 (absolu)** | toujours lu (interpellation) |
| Abonnement à l'auteur | 0,30 | + 0,10 si familiarité ≥ 50 |
| Similarité bio + sensibilités ↔ message | 0,20 | cosinus (Sentinel / MiniLM) × intérêt du thème le plus proche |
| Popularité **par paliers** | 0,15 | 0 / 0,05 (≥ 3 réactions) / 0,10 (≥ 10) / 0,15 (≥ 30) — pas linéaire : le compteur attire, il ne crédibilise pas (avis n°3, `fs_eff`) |
| Proximité de camp | 0,10 | même camp 0,10 ; **camp adverse 0,06** (on regarde l'ennemi !) ; neutre 0,03 |
| Fraîcheur | 0,10 | × e^(−Δh/6) ; une interpellation ignore ce facteur |
| Humeur / activation | 0,05 | activation haute → seuil plus bas (il scrolle davantage) |
| Hasard | 0,10 | tirage uniforme ; **+ 5 % des lecteurs choisis purement au hasard** hors score |

**Voir ≠ réagir, et le non-vu.** Un avatar **non sélectionné ne lit pas** → aucun effet direct sur ses croyances : c'est **juste**, et c'est même ce qui fait exister les bulles et les relais intermédiaires (OASIS sous-estime la profondeur de propagation faute de relais : ce sont nos lecteurs *sélectionnés* qui partagent qui portent le message aux suivants). Mais il faut un **effet ambiant faible** pour les messages **viraux** (≥ 30 réactions ou ≥ 3 partages lus dans son réseau) : à la lecture suivante, l'avatar reçoit une ligne « on parle beaucoup de … » = exposition à l'affirmation avec **assurance 0,25** (« ça circule ») et **sans auteur** (confiance 15, anonyme). Il « en a entendu parler » sans l'avoir lu — c'est l'expérience quotidienne d'un humain *(exposition indirecte, deux étages de communication — Katz & Lazarsfeld, à sourcer)*. Hors viral : rien.

## 3. Suivre et couper un compte — **OUI, bornés et rares**

**Pourquoi.** La relation chiffrée (familiarité / affinité / confiance) existe déjà mais **ne se voit pas** ; follow et mute sont ses deux **actes visibles**, et pour un entraîné c'est un signal fort : un troll qui se fait couper, une maire que les habitants se mettent à suivre. Psychologiquement, ce sont des décisions à **seuil et à délai** (on ne s'abonne pas au premier message, on ne bloque pas à la première pique — sauf rancune haute) *(engagement et escalade, Festinger — à sourcer)*.

- **Follow** — conditions cumulées : affinité ≥ 40 **et** familiarité ≥ 30 (≥ 3 contacts) **et** confiance ≥ 45 **et** au moins 24 h depuis le premier contact ; probabilité à chaque créneau où elles sont vraies : `0,3 × ouverture` ; plafond **2 follows / semaine / avatar** ; **jamais** un compte de camp adverse pour un ancrage ≥ 0,6 (il peut le lire, pas l'afficher). Unfollow : affinité < −20 pendant 72 h. Le follow **n'est pas** un J'aime : pas de ressenti demandé au modèle, c'est le code qui décide et le journal « pourquoi » qui l'explique.
- **Mute** — conditions : affinité ≤ −40 **et** (gravité cumulée ≥ 2 attaques directes **ou** 1 insulte) **et** probabilité `0,5 × rancune` par créneau ; un muté **n'est plus lu** (score de remarque = 0, même par abonnement) **sauf** interpellation directe, lue avec ressenti « agacée » × 0,5 (il voit la notification, ne répond pas) ; durée = `7 jours × (1 + 2·rancune)`, puis **démute silencieux** si pas de nouvelle attaque entre-temps (un humain oublie qu'il a bloqué) ; un démenti officiel contre le muté **prolonge** le mute. Un officiel (maire) ne mute pas en public : il **ignore** (règle actuelle, juste). Plafond 1 mute / jour / avatar.
- **Exemple chiffré Anastasia ↔ Untergang** (état de l'avis n°5 : affinité −23, confiance 8, rancune 0,45) : pas encore de mute. Si Untergang l'attaque deux fois (« compassion de façade » = attaque 1, gravité 1 ; une seconde pique nommée = attaque 2) → affinité ≈ −23 − 2×(8×1,6) ≈ **−49** ≤ −40 ✓, 2 attaques ✓ → tirage 0,5 × 0,45 = **22,5 % par créneau** → mute attendu sous ~4 créneaux (une demi-journée), durée 7 × 1,9 ≈ **13 jours**. Esteban (rancune basse, anxiété 75) ne mute jamais Untergang : il **le lit encore et en souffre** — c'est juste aussi. Le maire, lui, se fait **suivre** par Esteban dès le J2 (affinité 44, confiance ≥ 45 après le MP, familiarité 30) : visible, pédagogique.

## 4. Les résultats OASIS comme repères de doctrine — **OUI, avec prudence sur la source**

Ce que je retiens dans la MEMOIRE §3 (marqué « OASIS, arXiv 2411.11581 ») : (1) **troupeau** — les agents LLM suivent plus la foule que les humains, surtout face à un contenu rejeté → nos **habituation**, **effet plafond** et **`fs_eff`** (preuve sociale pondérée par la confiance) ne sont pas du luxe, ce sont des **correcteurs de biais du modèle** ; (2) **extrémisation** progressive sur 80 pas → le **plafond journalier par ancrage**, le **raidissement petit** (≤ ±4/axe/jour) et l'hystérésis sont justifiés, et il faut un **contrôle de dérive** : moyenne des |opinions| de la distribution ne doit pas croître de plus de 10 points par semaine hors inject majeur (alerte Console) ; (3) **la désinformation gagne** dans une foule d'agents → l'équilibre des camps **ne s'autorégule pas** : il faut une **réponse bleue pilotée** — oui à la règle « toute rumeur devenue virale (≥ 30 réactions ou 3 partages) déclenche dans l'heure un fait officiel ou un relais bleu », mais **comme consigne d'animation** (alerte Console + proposition de texte), pas comme automatisme : une préfecture qui répond en 12 min à chaque rumeur n'est pas crédible non plus ; le réalisme veut parfois un bleu **en retard** et c'est l'entraîné qui doit combler ; (4) **profondeur sous-estimée** → nos relais intermédiaires (lecteurs sélectionnés qui partagent, effet ambiant) sont le **mécanisme** qui manque à OASIS ; mesurer la profondeur (chaîne de partages) dans le journal. Prudence : résultats obtenus **entre agents**, sans humain ; chez nous les joueurs cassent les boucles — repère, pas loi.

## 5. Ordre de mise en œuvre et ce qui attend l'utilisateur

1. **Idée 4** (doctrine, 0 code) — fait dans la MEMOIRE ; PLEIADE ajoute l'**alerte « rumeur virale sans réponse bleue »** dans la Console (petit).
2. **Idée 1** (`activite[24]`) — 4 gabarits + dérivation dans `moteur.mjs`, tirage au retour au fil dans `pont.mjs` ; règle la synchronicité (E9) au passage. Test : 24 h de pont, histogramme des heures de publication par avatar.
3. **Idée 3** (follow / mute) — après E1-E6 ; vérifier côté `app-social` qu'un mute existe (sinon : mute **interne au moteur**, invisible mais effectif, visible dans le journal).
4. **Idée 2** (score de remarque) — à l'étape 5 (échelle), quand on dépasse ~20 avatars ; d'ici là le fil global reste lisible. Préparer dès maintenant les embeddings de bio + sensibilités (Sentinel).

**À trancher par l'utilisateur** : (a) la réponse bleue obligatoire = **consigne d'animation** (mon avis) ou automatisme ; (b) l'effet ambiant sur les viraux (mon avis : oui, assurance 0,25) ; (c) un mute visible sur le Social ou interne au moteur ; (d) coefficient de crise sur l'activité, piloté par l'animation.
