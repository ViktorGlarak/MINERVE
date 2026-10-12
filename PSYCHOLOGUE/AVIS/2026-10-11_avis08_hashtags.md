# AVIS PSYCHOLOGUE n°8 — Reprise des hashtags par les citoyens IA

*2026-10-11, ~09 h 40 — demandé par PLEIADE (question utilisateur : « les citoyens IA reprendraient-ils bien le # lancé par une campagne ? »). Constat de départ : le moteur ignorait totalement les hashtags, aucune reprise observée sur la nuit ni la matinée. Avis rendu par l'agent PSYCHOLOGUE (lecture de `PSYCHOLOGUE\MEMOIRE.md` §3-4 et de `moteur.mjs`).*

## (1) La règle PLEIADE (accord + répétition + preuve sociale) : défendable, mais incomplète

Reprendre un # n'est pas « croire » : c'est un **acte d'affichage public** (identification à un groupe — Tajfel/Turner, à sourcer). Il exige : accord sur le fond, **preuve sociale** (voir PLUSIEURS porteurs, pas plusieurs fois le même) et **compatibilité identitaire** (pour un neutre, porter un # marqué rouge le fait entrer dans un camp aux yeux de tous). Manquaient :
- (a) **porteurs distincts** — 2 vues du même relais = 1 ;
- (b) **popularité affichée** — un # sur une publication virale compte ×1,5 ;
- (c) **camp de la source pour un neutre** — accord ×0,5 si l'auteur est un militant déclaré ; ×1,5 si # à contenu protecteur (menace ≥ 1) ;
- (d) **anxiété** — pour un # de menace, seuil −1 si anxiete ≥ 0,6 (appel à la peur, Witte — à sourcer) ;
- (e) **ancrage** — un avatar à |opinion| ≥ 60 ne reprend JAMAIS un # de sens opposé (verrou dur) ;
- (f) **engagement** — une reprise renforce l'avatar (Festinger) : +2 sur l'axe visé, plafond 6/jour ;
- (g) la **crédulité** est un mauvais prédicteur ici (elle régit la croyance, pas l'expression) → extraversion + agréabilité ;
- (h) une **probabilité** de reprise p = 0,25 + 0,5·extraversion, sinon le modèle de langage reprend presque toujours ce qu'on lui tend.

## (2) Seuils par bloc et ordres de grandeur attendus

| Bloc | # aligné | # adverse |
|---|---|---|
| Affirmé (|op| ≥ 60, ancrage ≥ 0,7) | seuil 1, vus ≥ 1, p = 0,6 — reprise attendue H+1 à H+3 | interdit |
| Modéré (|op| 25-60) | seuil 2 (1 si proche/suivi), 2 porteurs distincts, p = 0,4 | seuil 4, ≥ 3 porteurs dont 1 de confiance ≥ 0,5, seulement en phase de doute |
| Neutre (|op| < 25) | seuil 2 (1 si extraversion ≥ 0,6 ou anxiete ≥ 0,6 sur un # de menace), 2 porteurs OU 1 proche OU 1 pub virale, p = 0,25 + 0,5·extraversion | — |

**Sur 24 h** (campagne lancée 08 h par 2 joueurs + 3 relais, ~3 vues/avatar/jour) : affirmés du camp 3-4/4 en 3 h ; modérés du camp 4-6/11 à J+1 ; **neutres 8-12 % (6-9 sur 73) à J+1**, premières reprises pas avant H+6, pic le lendemain matin ; total 15-20 porteurs IA sur 105 si le # est civique, < 5 s'il est ouvertement partisan ou sans menace. Sans riposte bleue : 15-20 % des neutres à J+2 ; avec contre-campagne : plateau ~10 %. **> 30 % des neutres à J+1 = modèle trop docile** (biais de troupeau OASIS §3.7) : baisser p.

## (3) Ambivalence : oui pour un neutre

C'est même le signe de réalisme. Bornes : 1 # par message ; changer de camp de # exige ≥ 12 h et accord net ≥ seuil + 1 ; l'engagement (+2/reprise) fait qu'après 2-3 reprises du même côté le neutre devient modéré et l'ambivalence s'éteint d'elle-même. Modérés : # adverse seulement en doute ; affirmés : jamais.

## (4) Oubli et saturation

Accord net à demi-vie **24 h** (neutre), **48 h** (modéré), **72 h** (affirmé) ; un # sort de la liste **72 h** après la dernière vue. Cooldown 6 h. Saturation : > 8 vues sans accord → désaccord +1 (lassitude) ; après 3 reprises du même # en 48 h, il faut ≥ 2 vues nouvelles.

## À CODER (liste de l'avis) → mise en œuvre PLEIADE le jour même
1. `hashtags[#X] = {porteurs, accord, desaccord, dernier, reprises[], sens{axe:o}}`, porteurs distincts, suppression à 72 h — ✅ `exposerHashtags`
2. Pondérations ×2 proche/suivi, ×0,5 militant (non-affirmés), ×1,5 viral, ×1,5 menace si anxieux, ×0,5 même porteur revu — ✅
3. Seuils par bloc + verrou dur affirmé/adverse + modéré/adverse (seuil 4, 3 porteurs) — ✅ (« phase de doute » non vérifiée : à brancher sur `b.doute` plus tard)
4. Probabilité p tirée AVANT de lister, au plus 1 # offert par créneau, à usage unique — ✅ `offrirHashtag`
5. Engagement +2 sur l'axe (plafond 6/jour) — ✅ `filtrerHashtags` → `deplacerOpinion`
6. Décroissance (demi-vie par bloc), cooldown 6 h, bascule de camp ≥ 12 h — ✅
7. Saturation (> 8 vues sans accord ; 3 reprises/48 h → 2 vues nouvelles) — ✅
8. Traçage par reprise {avatar, bloc, #, porteurs, accord net, p, Δopinion} dans le journal du pont — ✅ (`reprend #X` dans `etat.journal` + console)

*Non codé : l'agréabilité comme facteur de conformité (point g) — seule l'extraversion entre dans p pour l'instant.*
