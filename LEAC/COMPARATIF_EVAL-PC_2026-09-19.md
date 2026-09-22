# Comparatif ÉVAL-PC (client) ↔ LEAC v3 — 2026-09-19

> ✅ **Les six lots A→F ont été mis en place EN LOCAL le 2026-09-19** (neuf
> commits `app-leac`, non poussés — voir `JOURNAL.md`). Les points 2.1 à 2.14
> sont faits, sauf 2.15 (IA, hors périmètre). F est construit ÉTEINT par
> défaut (`LEAC_PIECES_JOINTES`, `LEAC_AUTO_EVALUATION`), en attente des
> arbitrages du § 4.

> Source : `REFERENCES/2026-09-19_EVAL-PC_prompt-creation_client.md` — prompt de
> spécification produit par un client sur son téléphone avec une IA (Lovable /
> GPT). **Aucune modification du code** : ce document compare et propose.
>
> Lecture d'ensemble : ÉVAL-PC est une app **connectée en permanence** (chaque
> saisie va en base, « Synchroniser » = recharger) pensée pour un **centre
> d'entraînement**. LEAC v3 est **hors ligne d'abord** (journal d'opérations,
> tablette sur le terrain) pensé pour l'**équipe de contrôle CECPC**. Ce sont
> deux points de départ différents ; la plupart des idées d'ÉVAL-PC s'absorbent
> sans toucher à notre socle, quelques-unes le contredisent.

## 1. Ce que LEAC a déjà, parfois mieux

| ÉVAL-PC | LEAC | Constat |
|---|---|---|
| Rôles admin / evaluator / visitor, promotion par e-mail, dernier admin protégé | `administrateurs_entite`, fonction par contrôle, dernier admin irrévocable | ✅ équivalent — et LEAC ne confond pas rôle et fonction |
| Membres par e-mail, droits **par domaine** | `domainesOuverts()` : transverses à tous, domaine de fonction au titulaire, commandement voit tout | ✅ mais **déduit de la fonction**, pas réglable (voir §2.1) |
| Hiérarchie Domaine ▸ Module ▸ Critère | `Noeud` récursif, 14 domaines, 1 352 critères | ✅ identique, profondeur libre |
| Critère « non pertinent » (`enabled=false`), barré, exclu des moyennes | `retenu=false` via le mandat (onglet Critères), sort des grilles et de la couverture | ✅ identique — chez nous c'est un acte du mandat, journalisé |
| Pondérations | onglet Pondérations, mandat du N+1 | ✅ |
| Échelle 2 → 5 par demi-points | mentions (mots) N4, valeurs au quart de point en haut | ✅ LEAC est **plus juste** (DECISION-025 : on enregistre le mot) — voir §3 |
| Moyennes et taux de remplissage à chaque niveau | `Resultat {note, attendues, remplies}` par nœud | ✅ |
| Niveau 1-5 par seuils + Label 10 exigences A/B/C, obligatoires, plafond « sans appuis » | `label.ts`, exigences, plafond, invalidation ; **décision du CC** sur le label | ✅ LEAC plus complet (DECISION-026) — ⚠ leurs seuils de niveau diffèrent (§3) |
| Tableau de bord : remplissage, moyennes par domaine, observations, résultat final | tableau de bord + réunion quotidienne par cycle, bilan du porte-drapeau | ✅ partiel — manquent les vues analytiques (§2.4) |
| Compte rendu + « Générer 3A (PPTX) » | CRF .docx (lettre + 7 annexes, Annexe III structurée) + 3A .pptx, générés hors ligne | ✅ LEAC plus complet |
| Auto-save avec debounce | écriture différée dans le journal (`useEcritureDifferee`) | ✅ |
| Thème clair/sombre | `data-theme="sombre"` | ✅ |
| Mention de diffusion en en-tête | `EXERCICE · NON CLASSIFIÉ` | ✅ — ⚠ la leur dit « Diffusion restreinte » (§3) |
| Reprise desktop↔mobile | journal synchronisé entre appareils | ✅ supérieur : on reprend **avec** les saisies hors ligne |
| Archivage / suppression (admin) | clôture + archivage par unité, suppression en INITIALISATION/EN_PREPARATION | ✅ |
| Fiche d'identité de l'unité | référentiel des unités + insigne | ✅ |
| Physionomie du PC | onglet « Grille physio » (§ V.A.4) | 🟡 grille présente, **pas de graphiques** |

## 2. Ce qu'ÉVAL-PC apporte et que LEAC n'a pas — à absorber

Classé par valeur pour l'équipe de contrôle, avec ce que ça coûte.

### 2.1 ⭐⭐ Droits par domaine **réglables** (Écriture / Lecture / Aucun)
Aujourd'hui les grilles ouvertes se déduisent de la fonction. ÉVAL-PC ajoute
un réglage explicite par membre et par domaine, avec un niveau **Lecture
seule** que nous n'avons pas (chez nous : on voit et on note, ou on ne voit
pas). Cas réel : un contrôleur S4 qui doit **lire** le S6 pour recouper sans
pouvoir y noter ; un stagiaire en observation.
**Proposition** : garder la déduction par fonction comme **valeur par défaut**,
ajouter dans Paramétrage › Équipe une grille membre × domaine (Écrit / Lit /
Rien) que l'ODM ajuste. `domainesOuverts()` reste la règle, le réglage la
surcharge. Rejoué côté serveur (`/api/sync` refuse une note sur un domaine en
lecture). Coût moyen ; touche le modèle (`MembreEquipe`), l'habilitation et
l'écran de notation.

### 2.2 ⭐⭐ « Évaluation rapide » — un critère à la fois
Carrousel tactile : un critère plein écran, gros boutons, suivant/précédent,
sommaire des domaines avec progression et saut direct. C'est **le** mode de
saisie debout, dans un PC, entre deux briefings. Notre écran de notation est
une liste par domaine (une rangée de crans par critère) — efficace assis,
moins debout.
**Proposition** : ajouter un mode « un par un » dans l'écran de notation
(bascule liste ↔ carte), même journal, même `useNotation` ; raccourcis clavier
pour le poste desktop (chiffres = mention, ←/→ = navigation). Coût faible :
c'est un habillage sur des hooks existants.

### 2.3 ⭐ Recherche et filtres dans la grille
Recherche plein texte sur libellé/code, filtres « non notés », « par
mention », « drapeau », repli des domaines volumineux par défaut et ouverture
automatique quand un filtre est actif. Avec 1 352 critères, retrouver « le
critère sur les ordres partiels » sans dérouler est un vrai gain.
**Proposition** : barre de recherche + trois filtres dans l'écran de notation
et l'onglet Critères du paramétrage. Coût faible, aucune donnée nouvelle.

### 2.4 ⭐ Tableau de bord analytique
Ce qui manque chez nous : histogramme des mentions, **Top 5 / Bottom 5** des
critères, points forts / faibles / critiques calculés, **radar** par domaine,
**courbe d'évolution** dans le temps. Le radar et le top/bottom parlent
immédiatement en réunion quotidienne et alimentent l'Annexe III.
**Proposition** : ajouter ces vues au tableau de bord existant, calculées
depuis le journal (rien à stocker) ; l'évolution s'obtient **sans snapshots** :
notre journal est horodaté, on rejoue à la date voulue. Tout se dessine sans
bibliothèque (SVG) pour rester hors ligne. Coût moyen.

### 2.5 ⭐ Comparaison de 2 à 4 contrôles
Moyennes, barres, radar superposé, tableau domaine par domaine avec écart
max, export Excel, impression. Chez nous l'historique par régiment existe
(unités › [id]) mais ne compare pas. Valeur forte pour le CECPC : « le 21e RIMa
a-t-il progressé depuis le contrôle de 2024 ? » — c'est la question du N+1.
**Proposition** : page `/administration/unites/[id]/comparaison` (même unité,
plusieurs contrôles clôturés) puis libre (plusieurs unités) ; export .xlsx
généré dans le navigateur comme le CRF. Coût moyen ; dépend de contrôles
clôturés en base (`niveauFinal`, `labelFinal` déjà persistés).

### 2.6 ⭐ Pièces jointes par critère
Photo d'un tableau de situation, d'un ordre, d'une carte : la preuve à côté
de la note. Absent chez nous.
**Proposition** : photo/fichier par critère **et par observation**, stockée
dans IndexedDB hors ligne, remontée à la synchronisation vers `DATA_DIR` (même
mécanisme que les insignes : type par octets, taille plafonnée), référencée
dans le journal par empreinte. ⚠ Sujet à trancher avec le CECPC : une photo
d'un PC en exercice peut porter une **classification** que l'app n'a pas — à
n'ouvrir qu'avec une règle claire (mention, purge à la clôture). Coût élevé
(sync binaire).

### 2.7 ⭐ Bibliothèque de modèles de grilles + import JSON
Aujourd'hui la grille N4 est **embarquée** dans le code ; changer de grille =
livrer une version. ÉVAL-PC en fait une donnée : modèles réutilisables,
import. Cela rejoint notre point ouvert « format Excel des grilles » (memento
admin § XII, en attente CECPC).
**Proposition** : référentiel « Grilles » en administration (import Excel du
CECPC via `import/grille.ts` déjà écrit, ou JSON), version figée au contrôle à
la création. Coût moyen ; **bloqué par le format CECPC**.

### 2.8 Préférences d'affichage
Taille du texte, densité, contraste élevé, réduction des animations, état du
menu — persistées localement. Nous n'avons que le thème.
**Proposition** : page « Affichage » (ou section de l'accueil) avec ces
réglages en variables CSS + `prefers-reduced-motion` respecté. Coût faible ;
la **taille du texte** et le **contraste élevé** vont dans le sens de notre
parti pris (soleil, gants).

### 2.9 Application installable (PWA légère)
Manifest + icônes, sans service worker de cache. Pour une tablette : icône sur
l'écran d'accueil, plein écran. Nous n'avons pas de manifest.
**Proposition** : manifest + icônes ; ⚠ contrairement à ÉVAL-PC nous avons
**besoin** d'un service worker (l'app doit s'ouvrir sans réseau, pas seulement
garder ses données) — à faire avec une stratégie de mise à jour explicite
(version dans `/api/sante`, déjà là). Coût moyen ; **c'est en fait un manque
de notre socle hors ligne** : aujourd'hui les données survivent hors ligne,
mais l'ouverture de l'app suppose que les pages soient déjà chargées.

### 2.10 Physionomie du PC avec graphiques
Effectifs, répartition, graphiques. Nous avons la grille, pas la lecture
visuelle. Coût faible une fois le tableau de bord SVG en place (2.4).

### 2.11 Fiche évaluateur / mandat comme pages
ÉVAL-PC expose « Fiche évaluateur », « Mandat », « Fiche unité » comme pages
de premier niveau. Chez nous le mandat vit dans le paramétrage (pondérations,
critères) et l'unité dans le référentiel. Pas de manque fonctionnel ; une
**page « Mandat »** lisible par toute l'équipe (ce que le N+1 a demandé, sans
pouvoir le modifier) serait un plus de transparence. Coût faible.

### 2.12 Checklist de rendu mobile automatisée
Script qui parcourt chaque route à 320/375/414 px, captures, rapport. Bonne
hygiène ; nos écrans sont testés à la main.
**Proposition** : script Playwright en CI (`main`), non bloquant. Coût faible.

### 2.13 Données de démonstration + « Réinitialiser la démo »
Utile pour former les contrôleurs et pour les recettes. Chez nous : rien
d'intégré (le contrôle d'essai est créé à la main).
**Proposition** : action admin « Créer un contrôle de démonstration » avec une
distribution de mentions réaliste, marqué DEMO, supprimable. Coût faible.

### 2.14 Auto-évaluation étanche (rôle `unit`, `mode='self'`)
Une unité en préparation s'auto-évalue, sans jamais voir ni être vue des
contrôles officiels. **Idée forte pour le CECPC** (préparation des régiments
avant ANTARES) mais c'est un **nouveau public** : des comptes de zone pour
chaque régiment, une étanchéité à prouver, un support.
**Proposition** : ne pas l'absorber tout de suite ; la porter comme
**décision CECPC** (voir §4). Techniquement faisable : un `mode` sur
`Controle`, un garde dans `habilitation.ts`, listes filtrées. Coût moyen, mais
le coût est surtout organisationnel.

### 2.15 Assistant IA
Hors périmètre pour le moment (décision utilisateur du 2026-09-18). Noté pour
mémoire.

## 3. Ce qu'il ne faut PAS reprendre tel quel

- **Échelle numérique 2 → 5 affichée** : la directive N4 et notre
  DECISION-025 disent *on pose une mention, on enregistre le mot* ; ÉVAL-PC
  note avec des chiffres. Absorber l'ergonomie (gros boutons), pas l'échelle.
- **Seuils de niveau** : ÉVAL-PC classe ≥ 4,5 → 5, 4 → 4, 3,5 → 3, 3 → 2,
  < 3 → 1 (« non observé »). Nos seuils viennent de la N4 (4,65 / 4,4 / 4 …).
  **Les leurs sont probablement une approximation de l'IA** — à ne pas copier ;
  à signaler au client pour qu'il ne s'y fie pas.
- **Label plafonné à B si toutes les fonctions ne sont pas contrôlées** : chez
  nous c'est **C max** pour « sans ses appuis » (DECISION-026, d'après la
  N4). Divergence de règle — à faire trancher par le CECPC, pas par nous.
- **Snapshots quotidiens** : inutiles avec un journal horodaté ; on rejoue.
- **« Synchroniser » = recharger** : chez eux l'app ne marche pas sans réseau.
  Notre bouton fait un vrai échange bidirectionnel hors ligne → serveur ; ne
  pas régresser.
- **Rôles d'application « visitor » par défaut à l'inscription** : chez nous
  personne ne s'inscrit ; Pléiade crée les comptes. Sans objet.
- **Pas de service worker** : justifié chez eux (toujours en ligne), faux chez
  nous (§2.9).
- **Mention « Diffusion restreinte »** en en-tête : ⚠ à ne pas afficher par
  défaut — une mention de diffusion est une décision de l'autorité, et poser
  DR sur un outil non classifié le rend inutilisable sur réseau non homologué.
  Garder `EXERCICE · NON CLASSIFIÉ`, rendre la mention paramétrable par
  l'administrateur si le CECPC le demande.
- **Notes dans un JSON `ratings` par évaluation** : c'est ce qui rend
  impossible la fusion multi-appareils ; notre journal par cible existe
  précisément pour ça (DECISION-021, DECISION-028).

## 4. À faire trancher par le CECPC / le client

1. **Seuils de niveau** et **plafond du label** : N4 (nous) vs ÉVAL-PC — les
   deux ne peuvent pas être vrais.
2. **Auto-évaluation des unités** : public, comptes, étanchéité, support.
3. **Pièces jointes** : classification des photos prises dans un PC.
4. **Mention de diffusion** de l'application.
5. **Format des grilles** (Excel / JSON) — déjà en attente.

## 5. Ordre proposé si l'utilisateur valide

| Lot | Contenu | Coût | Dépend de |
|---|---|---|---|
| **A** — ergonomie de saisie | 2.2 mode un-par-un + raccourcis · 2.3 recherche/filtres · 2.8 préférences d'affichage | faible | rien |
| **B** — lecture des résultats | 2.4 tableau de bord analytique (histogramme, top/bottom, radar, évolution) · 2.10 physio graphique · 2.11 page Mandat | moyen | rien |
| **C** — droits fins | 2.1 Écrit / Lit / Rien par domaine, rejoué serveur | moyen | rien |
| **D** — comparaison | 2.5 comparaison de contrôles + export .xlsx | moyen | contrôles clôturés |
| **E** — socle hors ligne | 2.9 PWA + service worker versionné · 2.12 checklist mobile · 2.13 démo | moyen | rien |
| **F** — sur décision CECPC | 2.6 pièces jointes · 2.7 grilles importables · 2.14 auto-évaluation | élevé | §4 |

Chaque lot passe par la même chaîne : tests, tsc, lint, build, `main`, puis
`prod` **sur feu vert**.
