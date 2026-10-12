---
name: melmil-structure-lo
description: MELMIL (synchromatrice AURIGE 2BB) v0.2 — 5 lignes = Lignes Opératoires GLM26 (procédé rouge) ; couleur de card = sphère (rouge/bleu) ; routage série→LO
metadata: 
  node_type: memory
  type: project
  originSessionId: 9cd755be-0651-44f5-8932-5974a21bced9
---

**MELMIL v0.2** (`MASTAURIGE\WEB\MELMIL\MELMIL_ILI_GUILLAUME.html` + `melmil.js` + `melmil.css`) — le tableau n'est plus organisé par séries (07/08/GHOST) mais par **5 Lignes Opératoires GLM26** :
- r1 **LO1** Appui hybride (Fictionnalisation · Déception · Ciblage chefs bleus)
- r2 **LO2** Volonté de combattre (Détermination MER · Fragilité OTAN)
- r3 **LO3** Guerre des pertes (Profondeur stratégique MER · Insoutenabilité)
- r4 **LO4** Vent de libération (MER légitime · {PAYS} discrédité)
- r5 **LO5** Rupture des alliances (Au sein de la coalition · Entre coalition & {PAYS})

**Plus de ligne r6/r7.** La distinction rouge/bleu passe par la **COULEUR de card — 2 couleurs seulement** :
- 🔴 **card rouge** = sphère info ROUGE (MER/RB) — défaut.
- 🔵 **card bleue** = sphère info BLEUE authentique (OTAN/ONU/Occident, ex. Rutte).

**Règle rouge/bleu (doctrine — voir [[expert_influence]]) :** les LO = **procédé ROUGE**. Un **avatar rouge qui simule du bleu** (sock-puppet, faux « neutre ») reste une **manœuvre rouge → card ROUGE dans sa LO**. Seul le **bleu authentique** est en card bleue. Discriminant = la **série** (`SPHERE_BLUE = {'08.03':true}` ; tout le reste = rouge).

**Mécanique :** `ROW_MAP[série]` → ligne (r1-r5) ; `sphereClass(série)` → classe `inj-red`/`inj-blue` (CSS melmil.css). Sous-lignes = **libellés** seulement. `var PAYS_DELEGITIME='DAC'` pilote les libellés LO4/LO5 (`'ARN'` pour Arnland → `.pays-label` MAJ auto). Incidents (melmil_data.js) sans LO → dérivée série→LO. Orphelins hors-XLS → ligne LO de leur série (style ghost dashed). Auto-réparation des positions `melmil-subinj` obsolètes (source de vérité > vieux drag).

**Carte série→LO (défauts à valider dans `ROW_MAP`) :** 07.07/07.08→LO1 · 07.01/07.06/04.01→LO2 · 07.02/08.01/08.02→LO3 · 07.03/07.04→LO4 · 07.05/01.01/08.03→LO5 (08.03 = card bleue). ⚠ Défauts à confirmer : 07.04, 04.01, 08.02, 07.06, 01.01.

**Restant non-2-couleurs (interim) :** les petits points de TYPE (tweet/article/tract/courrier) dans les cards gardent leurs couleurs — à collapser plus tard si besoin.

Lié : [[melmil_coherence]], [[glm26_matrice_ili]], [[melmil_mastaurige_navigation]], [[melmil_code_3digits]].
