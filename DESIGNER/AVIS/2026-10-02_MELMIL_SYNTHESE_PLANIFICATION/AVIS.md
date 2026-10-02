# Avis DESIGNER n°34 — MELMIL, synthèse de planification

> **Date** : 2026-10-02 · **App** : `app-melmil`, atelier de préparation · **Demande** : « une partie SYNTHÈSE qui permette de voir **en un coup d'œil où on en est sur la planification** : nombre d'incidents, en prépa, sans pièce jointe et sans scénario, etc. Nouvel onglet si nécessaire, mais **pense bien ergonomie**. » L'utilisateur veut la voir **en local d'abord**.
> **Statut** : proposition argumentée. DESIGNER contribue, PLEIADE / ARCHITECTE applique et l'utilisateur tranche.
> **Lu avant l'avis** : `ecran-atelier.tsx`, `modele.ts`, `statut.tsx`, `onglets-gt.tsx`, `pieces-jointes.ts`, `ecarts.ts`, `scenarios-admin.ts`, `scenarios-incident.tsx`, `produits.tsx` (+ `produits/modele.ts`), `globals.css`.
> **Sources** : REF-06 Laws of UX (Miller, Hick, Jakob, Von Restorff, proximité, Doherty) · REF-07 Refactoring UI (hiérarchie, couleur jamais seule, étiquette en dernier recours) · REF-14 Nielsen (1 état visible, 4 cohérence, 6 reconnaître plutôt que se souvenir, 8 minimalisme) · REF-13 WCAG 2.2 (1.4.1, 1.4.11, 1.3.1, 2.4.4) · REF-10 GOV.UK (dire comment agir) · REF-12 Carbon (couches, données denses).
> ⚠ **Limite** : nos fiches n'incluent pas encore de source dédiée aux tableaux de bord (Stephen Few, NN/g *dashboards* — §5 bis n°9). Ce qui suit en tient lieu par les sources ci-dessus ; les points qui n'en découlent pas sont signalés « avis ».

---

## 0. Constat : la réponse existe déjà, mais en miettes

Tout est calculable sans rien ajouter au modèle, et une partie est déjà affichée : le compte de chaque onglet, les statuts dans l'en-tête de chaque storyline (n°16), le bandeau JEMM (n°33 R6), les écarts (onglet dédié), les retards de demandes (onglet Demandes), le ▶ n des scénarios sur les cartes (n°28). Pour répondre à « où en est-on ? », il faut aujourd'hui **ouvrir 4 onglets et additionner de tête** — c'est exactement ce que Nielsen 6 (reconnaître plutôt que se souvenir) et Tesler (le système porte la complexité, REF-06) demandent d'éviter.

La synthèse n'invente donc rien : elle **rassemble, trie et renvoie** vers l'endroit où l'on agit.

---

## 1. Recommandations

### R1 — Un onglet « Synthèse », en tête de la famille *Visualiser* ; l'arrivée reste la planche de préparation
- **Libellé de l'onglet : `Synthèse`** (un mot, comme ses voisins). **Titre de la page : « Où en est la planification ? »** — la question que se pose l'utilisateur, à laquelle la page répond (REF-10 : parler la langue de l'utilisateur).
- **Place : premier onglet de *Visualiser*** (`synthese`, `planche`, `ecarts`, `demandes`). Une vue d'ensemble se lit avant le détail (avis, principe « vue d'ensemble d'abord ») ; la famille reste le repère (Jakob, REF-06) : *Construire* ne bouge pas, et les onglets de *Visualiser* et *Organiser* glissent d'un cran sans changer d'ordre ni de famille.
- **Pas d'onglet d'arrivée par défaut.** L'arrivée sur la planche de préparation est une **décision utilisateur du 2026-10-02** (avis n°25 : l'écran d'arrivée = la tâche la plus fréquente). La synthèse se consulte, on n'y travaille pas. ⇒ Elle s'ouvre par un clic, et par lien direct `?onglet=synthese` (n°25 R4). *Question à l'utilisateur* : s'il veut l'inverse, c'est un changement d'une ligne (`actif = onglet ?? "planche"`).
- **Pas de compteur sur l'onglet** : un nombre à côté de « Synthèse » ne dirait pas de quoi il parle (Nielsen 8).
- Données **en direct** : la page se recalcule à chaque geste de l'atelier partagé, comme la planche. Pas de bouton « Rafraîchir » (la pastille « en direct » de l'en-tête le dit déjà, Nielsen 1).

### R2 — Une hiérarchie en 4 blocs, la réponse tout en haut
1. **Avancement** — une phrase + une barre (la réponse en 2 secondes).
2. **À traiter** — les manques, **chacun un lien** vers les incidents concernés.
3. **Par storyline** — où sont les retards, rangé par event › storyline.
4. **Charge par jour** — les trous et les surcharges du calendrier.

Pied de page : une ligne de contexte (demandes, dernière modification). Le GT courant est **déjà** dans l'en-tête : on ne le répète pas (Nielsen 8).

Charge cognitive (Miller / Hick, REF-06) : **une phrase de tête**, puis **au plus 9 lignes de manques réparties en 3 groupes**, et **seuls les manques non nuls s'affichent**. On met en valeur en atténuant le reste (REF-07) : chiffres en `--texte` et en gras, phrases en `--texte`, précisions en `--texte-doux`.

### R3 — L'avancement : une phrase d'abord, une barre empilée ensuite
- **Phrase (h2 + texte, lue en premier par tous, y compris le lecteur d'écran)** :
  « **12 incidents sur 42** sont validés ou dans JEMM (29 %). » puis « Il en reste 30 : 18 en préparation, 12 en validation. »
  Toujours le **numérateur et le dénominateur**, le pourcentage en second (un « 29 % » seul ne dit pas sur quel volume).
- **Barre empilée** pleine largeur (16 px de haut, max 48rem), 4 segments **dans l'ordre des statuts** (préparation → validation → validé → JEMM), **le même ordre que le filtre et le stepper** (cohérence, Nielsen 4) : le vert s'accumule vers la droite, vers l'arrivée.
- **Couleurs `--st-*` du n°33, jamais seules** (WCAG 1.4.1) :
  - En préparation `--st-preparation`, En validation `--st-validation`.
  - ⚠ *Validé* et *Dans JEMM* partagent **le même vert** (`--st-ok`, n°33 R2). Dans une barre, ils se toucheraient sans se distinguer. ⇒ **Dans JEMM = vert plein ; Validé = vert hachuré** (`repeating-linear-gradient(135deg, var(--st-ok) 0 3px, color-mix(in oklch, var(--st-ok) 45%, var(--fond-carte)) 3px 6px)`). La forme (hachure / plein) distingue, pas une 2ᵉ teinte de vert.
  - **2 px de fond entre segments**, contour `--trait-fort` d'1 px autour de la barre (WCAG 1.4.11, 3 : 1 contre le fond).
  - Nombre écrit **dans** le segment s'il fait ≥ 28 px, sinon seulement dans la légende.
- **Légende = 4 liens** sous la barre : `PastilleStatut` + libellé + nombre, ex. « ◔ En préparation 18 ». Chacun ouvre l'onglet Incidents **filtré sur ce statut** (le `FiltreStatut` existe déjà). Un segment de barre n'est pas une cible (trop fin, Fitts) : c'est la légende qui l'est (≥ 24 px, WCAG 2.5.8).
- Accessibilité : la barre est `role="img"` avec un `aria-label` qui reprend la phrase complète des 4 statuts ; la légende est une `<ul>` de liens.
- Juste sous la légende, si non nul, **une seule précision** : « dont 5 non placés (sans D+) » — c'est le seul manque qui touche l'avancement lui-même.

### R4 — « À traiter » : chaque chiffre est une action
Un bloc, **3 groupes titrés** (h3), une liste par groupe. Chaque ligne a toujours la même forme (proximité et alignement, REF-07) :

`[nombre en gras, chiffres tabulaires]  [phrase qui dit le manque]  ·  [lien « Voir les N › »]`

- **Le lien est explicite hors contexte** (WCAG 2.4.4) : texte visible « Voir les 7 », `aria-label="Voir les 7 incidents sans pièce jointe ni scénario dans l'onglet Incidents"`.
- **Seuls les manques non nuls s'affichent** ; en bas de chaque groupe, une ligne `--texte-doux` « ✓ En ordre : ETIM, émetteurs, destinataires » (la fin d'un parcours mérite une confirmation, Peak-End REF-06 — mais en une ligne, pas 6).
- **Ordre = du plus bloquant au moins bloquant** pour la mise en JEMM, **pas par couleur** (la couleur d'alerte reste rare, Von Restorff REF-06).
- **Aucun rouge**, sauf **un seul cas : les demandes de produit en retard** (échéance passée), qui reprennent `--alerte` **et** le mot « en retard ».

| Groupe | Ligne (libellé exact, ex.) | Lien |
|---|---|---|
| **Incidents** | « **7** incidents sans pièce jointe ni scénario » ▸ dépliable : « dont 12 sans pièce jointe · 15 sans scénario » | Incidents filtrés `manque=sans-pj-scenario` |
| | « **5** incidents non placés (sans D+) » | `manque=non-place` |
| | « **9** fiches incomplètes » ▸ dépliable : « sujet 1 · moyen 6 · émetteur 3 · destinataire 4 » (chaque champ un lien) | `manque=incomplet` (ou `manque=sans-moyen`…) |
| | « **3** incidents sans ETIM » | `manque=sans-etim` |
| **Storylines et coordination** | « **2** storylines sans incident » | Storylines (focus 1ʳᵉ) |
| | « **4** cellules EXCON à coordonner, sur 3 storylines » ▸ dépliable : « 06.01 OPFOR, HN · 06.03 LOG · 07.02 ILI » | Storylines |
| **JEMM et production** | « **6** incidents présents dans JEMM sans être marqués » + bouton **« Les marquer « Dans JEMM » »** (le geste du `BandeauJemm`, n°33 R6 : proposé, jamais automatique) | — (action sur place) |
| | « **1** incident marqué « Dans JEMM » absent du dernier export » | Incidents `manque=jemm-absent` |
| | « **8** écarts avec JEMM » ▸ « 5 absents de JEMM · 2 différents · 1 seulement dans JEMM » | onglet Écarts |
| | « **2** demandes de produit **en retard** » (seul rouge) · « 3 à traiter » | Demandes (filtre « À traiter ») |

*« Fiche incomplète »* : une seule ligne au lieu de 5 (Miller). Les champs comptés par défaut : **sujet, moyen, émetteur, destinataire** (ce que JEMM attend). *Question à l'utilisateur* : la **description** est-elle obligatoire avant validation ? Si oui, on l'ajoute à la liste ; sinon on ne la compte pas (un manque qui n'en est pas un use la confiance dans tout le bloc).

**Écartés** (calculables mais sans décision derrière, Nielsen 8) : « confiés à quelqu'un / au sous-groupe » (ne rien cocher est un choix valide, n°10 R3) ; nombre de comptes rendus (un volume, pas un manque — déjà compté dans les pièces jointes) ; nombre d'events (dans l'onglet) ; « sans pièce jointe » et « sans scénario » isolés en lignes principales (ils vont dans le dépliant : un incident qui a un scénario n'a pas forcément besoin d'un fichier, et inversement — c'est la conjonction que l'utilisateur a demandée).

### R5 — Un filtre « manque » dans l'onglet Incidents pour accueillir ces liens
Sans lui, les liens de R4 ouvriraient un tableau non filtré : l'utilisateur devrait retrouver lui-même les 7 incidents (Nielsen 6).
- Lien = `?onglet=gt3&manque=<cle>` (ou `&statut=<s>` pour la légende de R3).
- Dans l'onglet Incidents, **au-dessus du `FiltreStatut`**, une bande **visible et nommée** :
  « **Filtré depuis la synthèse : 7 incidents sans pièce jointe ni scénario** · `Retirer le filtre` · `‹ Retour à la synthèse` »
- Comme le filtre de statut (n°33 R8), il **déplie d'office** les storylines qui contiennent un incident retenu et masque les autres ; il se **combine** (ET) avec statut et storyline.
- ⚠ **Pas mémorisé** (contrairement au filtre de statut) : un filtre arrivé par un lien et oublié cacherait des incidents à la visite suivante sans qu'on le voie (Nielsen 1). Il vit dans l'URL, il disparaît quand on quitte l'onglet ou qu'on clique « Retirer ».
- **Un seul calcul** dans une fonction pure `lib/atelier/synthese.ts` (`manquesDe(atelier, scenarios, codesJemm)` → listes d'ids par clé), utilisée **par la synthèse ET par le filtre** — le même principe que `piecesDeLIncident` pour le tableau et la planche (n°24 R5). Le nombre de la synthèse et le nombre de lignes filtrées ne peuvent pas diverger. Testable comme `pieces-jointes.ts`.

### R6 — « Par storyline » : un tableau rangé par event, une mini-barre par ligne
- Même rangement que l'onglet Incidents : **intertitre par event** (`intertitre-event`, n°16 R3) avec sa propre mini-barre agrégée, puis **une ligne par storyline triée par code** (ordre stable = mémoire de position, n°27).
- Colonnes : **Storyline** (code mono + nom, tronqué) · **Avancement** (mini-barre 8 px, même composant que R3, `aria-label` « 06.01 : 2 en préparation, 1 validé, 3 dans JEMM ») · **Incidents** (nombre) · **Période** (D+3 → D+7) · **À traiter** (nombre de manques de R4 sur cette storyline, vide si 0 — pas de « 0 » qui fait du bruit) · **EXCON** (« 2 à coordonner », vide si 0).
- **Toute la ligne ouvre** l'onglet Incidents filtré sur cette storyline (lien étiré, comme les cartes Presse n°18 ; focus visible sur la ligne).
- Une storyline sans incident affiche « *aucun incident* » en italique doux à la place de la barre (pas une barre vide, qu'on prendrait pour « 0 % fait »).
- Les events sont **dépliés** ici (contrairement à l'onglet Incidents) : une synthèse se parcourt d'un regard ; au-delà de ~25 storylines, replier les events et garder la mini-barre de l'event dans l'intertitre.

### R7 — « Charge par jour » : un histogramme simple, qui est un tableau
- **Utile** : il montre d'un regard les **jours vides** de la phase et les **jours chargés** — une décision de planification (déplacer, ajouter), que la planche montre aussi mais sans total (avis).
- Une colonne par D+ de la phase (`calendrier.premierJour → dernierJour`), hauteur = nombre d'incidents placés ce jour, **empilée par statut** avec les mêmes couleurs/hachures que R3 (cohérence). Le nombre écrit **au-dessus** de chaque colonne ; un jour à 0 garde sa place avec un « 0 » et un trait de base pointillé (le trou doit se voir, pas disparaître). Axe : « D+3 », « D+4 »… sous les colonnes ; les **phases** en bandeau sous l'axe si elles existent.
- Phrase au-dessus : « **2 jours sans incident** : D+5, D+9. Jour le plus chargé : D+7 (11 incidents). »
- À droite, hors axe : « Non placés : 5 » (lien vers `manque=non-place`).
- **Balisage = un `<table>`** (une ligne par jour : jour, total, détail par statut) rendu visuellement en colonnes, ou `<table class="sr-only">` à côté du SVG : le lecteur d'écran lit des chiffres, pas un dessin (WCAG 1.3.1).
- Un clic sur une colonne ouvre la **planche de préparation** (c'est là qu'on déplace un incident de jour). Cible = toute la colonne, ≥ 24 px de large.
- **Téléphone** (< 640 px) : les colonnes deviennent des **lignes** (une par jour, barre horizontale), pas de défilement horizontal de la page.
- Calendrier non posé → bloc remplacé par : « Posez le calendrier dans **Réglages** pour voir la charge par jour. »

### R8 — États : ne jamais afficher un 0 qu'on ne connaît pas
| Situation | Affichage |
|---|---|
| **Scénarios en chargement** | La ligne « sans pièce jointe ni scénario » montre « … » (pas 0), le reste de la page s'affiche. |
| **Admin injoignable**, scénarios en cache | Le chiffre reste, avec la mention doux « d'après la dernière lecture des scénarios (admin injoignable) ». |
| **Injoignable sans cache / hors zone / zone sans admin** | La ligne devient « **12** incidents sans pièce jointe » + mention « Scénarios non vérifiés : admin indisponible dans cette zone ». Le libellé change **avec** le contenu : on ne compte jamais « sans scénario » ce qu'on n'a pas pu vérifier (Nielsen 1 ; la règle de `scenarios-admin.ts` : « un échec de lecture n'est pas aucun scénario »). |
| **Aucun export JEMM chargé** | Le groupe *JEMM et production* remplace ses lignes JEMM par : « Aucun export JEMM chargé : les écarts ne peuvent pas être calculés. **Réglages › verser un export JEMM** » — sinon tous les incidents compteraient comme « absents de JEMM ». |
| **Atelier vide** | Toute la page = un état vide qui guide (REF-07, Peak-End) : « Rien à synthétiser pour l'instant. Commencez par créer un event (**GT1 › Events**). » + bouton secondaire vers l'onglet Events. |
| **Storylines mais 0 incident** | Bloc 1 : « Aucun incident encore. **3 storylines** attendent leurs incidents. » + lien Incidents. Blocs 3–4 masqués. |
| **Tout est en ordre** | Bloc 2 : « ✓ Rien à traiter : chaque incident est placé, complet, et a une pièce jointe ou un scénario. » (une ligne, pas de confettis). |

### R9 — Thèmes, téléphone, accessibilité
- **Thèmes** : uniquement des jetons existants (`--fond-carte`, `--trait`, `--texte`, `--texte-doux`, `--st-*`, `--alerte`) ; la hachure de « Validé » est en `color-mix` sur `--fond-carte`, donc juste dans les deux thèmes. **Tester en mode sombre du système** (leçon eho, `colorScheme: "dark"`).
- **Couches** (Carbon REF-12) : chaque bloc dans une `carte-ui` sur le fond de page ; pas de cartes dans des cartes.
- **Mise en page** : ≥ 1024 px, blocs 1 et 2 côte à côte (1 : 2/5, 2 : 3/5), blocs 3 et 4 pleine largeur dessous ; < 1024 px, tout en colonne dans l'ordre 1 → 4. Rien ne défile horizontalement (la table du bloc 3 passe en liste < 640 px : nom, mini-barre, puis « 6 incidents · D+3 → D+7 · 2 à traiter »).
- **Chiffres** : `font-variant-numeric: tabular-nums` (ou `.chiffre` mono) pour qu'ils s'alignent ; le nombre fait partie du texte du DOM, pas d'un pseudo-élément.
- **Titres** : le h1 reste le nom de l'exercice ; « Où en est la planification ? » en h2, un h3 par bloc, un h4 par groupe du bloc « À traiter » (les « h2/h3 » des schémas ci-dessus se lisent donc un cran plus bas) — la page se parcourt au lecteur d'écran par titres.
- **Pas d'`aria-live`** sur la page : elle se recalcule à chaque geste d'un collègue, l'annoncer serait du bruit.

---

## 2. Maquette textuelle (ordre et libellés exacts)

```
[en-tête de l'atelier inchangé]
[onglets]  Construire : Events · Storylines · Incidents
           Visualiser : ►Synthèse◄ · Planche de préparation · Écarts avec JEMM · Demandes de produit
           Organiser  : Équipe · Journal · Réglages

h2  Où en est la planification ?        (le h1 de la page reste le nom de l'exercice ; blocs = h3, groupes = h4)

┌ BLOC 1 — h2 « Avancement » ──────────────────┐ ┌ BLOC 2 — h2 « À traiter » ───────────────────────────────┐
│ 12 incidents sur 42 sont validés ou dans     │ │ h3 Incidents                                             │
│ JEMM (29 %).                                 │ │  7  incidents sans pièce jointe ni scénario  · Voir les 7 › │
│ Il en reste 30 : 18 en préparation,          │ │     ▸ dont 12 sans pièce jointe · 15 sans scénario       │
│ 12 en validation.                            │ │  5  incidents non placés (sans D+)            · Voir les 5 › │
│ [██████ orange │ ███ jaune │ ▨▨ │ ██ vert ]   │ │  9  fiches incomplètes                        · Voir les 9 › │
│ ◔ En préparation 18 › ◑ En validation 12 ›   │ │     ▸ sujet 1 · moyen 6 · émetteur 3 · destinataire 4    │
│ ✓ Validé 4 ›          J Dans JEMM 8 ›         │ │  ✓ En ordre : ETIM                                       │
│ dont 5 non placés (sans D+)                  │ │ h3 Storylines et coordination                            │
└──────────────────────────────────────────────┘ │  2  storylines sans incident                  · Voir les 2 › │
                                                 │  4  cellules EXCON à coordonner, sur 3 storylines · Voir › │
                                                 │ h3 JEMM et production                                    │
                                                 │  6  incidents présents dans JEMM sans être marqués        │
                                                 │     [Les marquer « Dans JEMM »]                           │
                                                 │  1  incident marqué « Dans JEMM » absent du dernier export · Voir › │
                                                 │  8  écarts avec JEMM                          · Voir les écarts › │
                                                 │  2  demandes de produit en retard (rouge) · 3 à traiter · Voir › │
                                                 └──────────────────────────────────────────────────────────┘
┌ BLOC 3 — h2 « Par storyline » ───────────────────────────────────────────────────────────────────────────┐
│ Storyline              Avancement        Incidents  Période        À traiter  EXCON                      │
│ 06  Event Nord  [mini-barre agrégée]  14 incidents                                                       │
│   06.01 Blocus portuaire  [▬▬▬▨█]         6        D+3 → D+7       2          2 à coordonner             │
│   06.02 Rumeur sanitaire  aucun incident  0        —               —                                     │
│ 07  Event Sud …                                                                                          │
└──────────────────────────────────────────────────────────────────────────────────────────────────────────┘
┌ BLOC 4 — h2 « Charge par jour » ─────────────────────────────────────────────────────────────────────────┐
│ 2 jours sans incident : D+5, D+9. Jour le plus chargé : D+7 (11 incidents).                              │
│  [colonnes empilées par statut, nombre au-dessus, 0 visible]                       Non placés : 5 ›      │
│  D+3 D+4 D+5 D+6 D+7 D+8 D+9 …   [bandeau des phases]                                                    │
└──────────────────────────────────────────────────────────────────────────────────────────────────────────┘
Pied (texte doux) : Demandes de produit : 3 à traiter, 5 livrées · Dernière modification : 14:32 par CNE MARTIN · Journal ›
```

---

## 3. Composants à réutiliser / créer

| Réutiliser | Pour |
|---|---|
| `PastilleStatut`, `libelleStatut`, `resumeStatut` (`statut.tsx`) | légende de la barre, phrases |
| `FiltreStatut` + son état (onglet Incidents) | arrivée depuis la légende (`&statut=`) |
| `BandeauJemm` → son geste `marquerDansJemm` | bouton « Les marquer « Dans JEMM » » |
| `piecesDeLIncident` (`pieces-jointes.ts`) | « sans pièce jointe » |
| `useScenariosAdmin` + `scenariosDe` (`scenarios-admin.ts`) | « sans scénario » et ses états (R8) |
| `ecarts` + `bilanEcarts` (`ecarts.ts`), `codesJemm` (`ecran-atelier.tsx`) | groupe JEMM |
| `A_TRAITER`, échéance (`produits.tsx`) | demandes en retard / à traiter |
| `intertitre-event`, `carte-ui`, `.chiffre`, `frappe-mini`, jetons `--st-*` | habillage |

| Créer | Rôle |
|---|---|
| `lib/atelier/synthese.ts` (pur, testé) | `manquesDe()` → ids par clé de manque ; `avancement()` → effectifs par statut (global, event, storyline) ; `chargeParJour()` |
| `components/atelier/synthese.tsx` | `OngletSynthese`, `BarreStatuts` (taille `grande` 16 px / `mini` 8 px, `aria-label` complet), `LigneManque` |
| param `manque` dans `OngletIncidents` | bande « Filtré depuis la synthèse… » + `Retirer le filtre` + `‹ Retour à la synthèse` |

Effort estimé : R1–R4 + R8 ≈ ½ journée ; R5 ≈ 2 h ; R6 ≈ 2 h ; R7 ≈ 2–3 h. Ordre conseillé si on découpe : **R1-R2-R3-R4-R5-R8**, puis R6, puis R7.

---

## 4. Ce qu'il ne faut PAS faire

- ⛔ **Jauges, compteurs circulaires, camemberts, anneaux** : ils comparent mal les parts (angles et arcs se lisent moins bien que des longueurs alignées, avis) et prennent la place de 3 lignes utiles.
- ⛔ **Un KPI sans action** : tout chiffre de la page ouvre l'endroit où l'on agit, ou on le retire.
- ⛔ **Du rouge partout** : un seul rouge, pour les demandes en retard (Von Restorff). Les manques sont classés par **ordre**, pas par couleur.
- ⛔ **Un « score global » ou une note de santé** composite : personne ne sait ce qu'il faut faire pour le faire monter.
- ⛔ **Un pourcentage sans son volume** (« 29 % » seul).
- ⛔ **Afficher 0 quand on ne sait pas** (scénarios indisponibles, pas d'export JEMM).
- ⛔ **Des tendances, flèches ↑↓, courbes d'évolution** : l'atelier ne garde pas d'historique des effectifs ; ce serait inventé.
- ⛔ **Des compteurs animés** qui défilent jusqu'à leur valeur (REF-09 : une animation explique, ne décore pas ; et la page se recalcule en direct).
- ⛔ **Répéter l'en-tête** (GT courant, nom d'exercice, pastille en direct).
- ⛔ **Changer l'onglet d'arrivée** sans décision de l'utilisateur (n°25).
- ⛔ **Mémoriser le filtre « manque »** dans le navigateur.
- ⛔ **Recalculer les manques à deux endroits** (synthèse et filtre) : une seule fonction.
- ⛔ **Mettre la synthèse dans le bandeau ou l'en-tête** de l'atelier : elle alourdirait l'écran de travail à chaque visite.
