# MÉMOIRE — ANALYSTE BELLA RUSSIA (Expert Bella Russia / Biélorussie)

Agent créé le **2026-05-27** — Spécialiste transversal tous exercices impliquant la Bella Russia.

---

## ⚠ ÉVOLUTIONS SYSTÈME — 2026-05-29

### Règle MASTAURIGE obligatoire
Tout fichier sous `...\MASTAURIGE\` requiert la consultation de MASTAURIGE. ANALYSTE_BR produit le **contenu BR** — MASTAURIGE gère le **format et l'intégration technique**.

### Doctrine calibration brigade (AURIGE)
Injects BR AURIGE doivent être calibrés niveau brigade. Les articles BC1 globaux (Youkachenko discours national) restent du cadre. Ce qui intéresse le PC brigade : signaux BR dans la ZO, présence de ressortissants BR, tweets de figures BR sur des événements locaux de la ZO.

### Injects BR récents D+34 (29 Mai 2026)
- `07.05.03Fi` / `BCI_Article_Manifestations_NP_BL` : Manifestations J+4 dans 4 villes BR — NP + Bison Libre + nationalistes (+15-20% vs D+33)
- `08.02.02Bi` : @KolesnikovAndrei (pro-MER) — rumeurs maltraitance POW MER par 8e DAC HNANCY — appel CICR + discrédit DAC vs FR (LO 2+3)

### Synchronisation MELMIL ↔ index_master
Quand la date d'un inject BR change dans index_master (sélecteur de jour), MELMIL se met à jour au rechargement via `syncDayOverrides()`. Dans l'autre sens, un drag dans MELMIL met à jour index_master via `card-day-*` localStorage.

---

## Correspondance géographique réelle

**Bella Russia = Biélorussie (Belarus)** dans tous les exercices Mercure.

> Convention H-prefix : uniquement pour les villes françaises (DR / Arnland).
> Les villes biélorusses gardent leur nom réel dans les injects (ex : **Minsk**, pas HMinsk).

| Lieu réel | Nom exercice |
|---|---|
| Biélorussie | **Bella Russia (BR)** |
| Minsk (capitale) | **Minsk** (inchangé) |

---

## Régime politique

- **Régime :** Autoritarisme présidentiel — contrôle total de l'exécutif
- **Dirigeant :** Alexandre **Youkachenko** — Président
  - Calqué sur Loukachenko (Biélorussie réelle)
  - Au pouvoir depuis les années 1990 — régime à parti unique de facto
  - Posture : anti-OTAN systématique, allié stratégique de Mercure
  - Discours publics : LO 5 (légitimation de l'alliance MER-BR, dénigrement de l'OTAN)
- **Parti au pouvoir :** Bloc Nationale Uni (BNU) — pro-Youkachenko, pro-MER
- **Parlement :** Assemblée Nationale BR — chambre verrouillée, rôle symbolique

---

## Gouvernement BR — Figures clés (régime Youkachenko)

> Mis à jour au fil des sessions de production. Référence canonique pour tout inject ou article BC1 impliquant un membre du gouvernement BR.

| Personnage | Poste | Camp | Rôle éditorial | Apparaît dans |
|---|---|---|---|---|
| **Alexandre Youkachenko** | Président de la République de Bella Russia | 🔴 Rouge | Signataire des décrets, discours officiels, allié MER — voix souveraniste anti-OTAN | BCI_Article_Youkachenko · BCI_Article_Youkachenko_ConsSec · tous articles BC1 |
| **Ivan Lubrakov** | Ministre de l'Intérieur (Ministry of Internal Affairs) | 🔴 Rouge | Porte-parole officiel pour : fermeture des frontières, gardes-frontières, sécurité intérieure, ordre public | BCI_Article_Frontiere (30 Mai) · TV4_Article_Frontiere_BR_01 (30 Mai) — inject 07.05.05 |
| **Général Aleksei Marchuk** | CEMA — Chef des Forces Armées de Bella Russia | 🔴 Rouge | Déclarations militaires — posture défensive, mobilisation — NE PAS le citer pour des sujets civils ou frontaliers | BCI_Article_CemaBR (01 Jun) |

### Règle de attribution éditoriale BR

> **Lubrakov parle pour tout ce qui est frontières, police, sécurité intérieure.**
> **Marchuk parle uniquement pour les sujets militaires (armée, mobilisation, opérations).**
> Ne pas confondre les deux — erreur corrigée le 2026-05-30 dans BCI_Article_Frontiere où Marchuk était cité à tort pour l'annonce de fermeture des frontières.

---

## Opposition politique

> Créés le 2026-05-27 — personnages actifs dans AURIGE 2BB à partir de D+27.

### SVETLANA Tikhanov — Nouvelle Pahonie

> Source : `D:\CECPC\PRODUCTION\CREATION\07 - BELLA RUSSIA\POLITIQUE\Opposition BellaRussia.docx`

| Donnée | Valeur |
|---|---|
| **Parti** | **Nouvelle Pahonie** — mouvement jeune, nationaliste, actif dans les diasporas BR à l'étranger |
| **Rôle** | Dirigeante de Nouvelle Pahonie — figure d'une opposition nationaliste et indépendantiste |
| **Positionnement** | Double opposition : anti-Youkachenko ET anti-OTAN — "We are strangled both by NATO but also by Youkachenko" |
| **Discours** | Appel à l'action autonome du peuple BR — refuse la passivité face aux deux blocs |
| **Formation** | Diplômée en communication de **HParis** — a fondé un blog sur la défense des frontières nationales |
| **Rayonnement** | Fort à l'international via les diasporas — parti sans élu mais influence croissante |
| **Tweet référence** | *"WE the 'ordinary people' should take this matter in our own hands rather than suffering the said consequences passively. Time for dialogue is exceeded."* — #NouvellePahonie |
| **LO** | Exploitable camp bleu pour montrer fracture intérieure BR (P.03) — mais ambiguïté anti-OTAN à manier avec précaution |
| **Relation Youkachenko** | Opposition frontale — mais refuse aussi l'alignement occidental |
| **Calqué sur** | Sviatlana Tsikhanouskaya + nationalistes biélorusses |

**Utilisation éditoriale :**
Ses déclarations sont ambiguës — elle n'est PAS pro-OTAN. TV4 peut la citer prudemment comme voix de dissidence BR. EastWatch est le canal adapté pour la nuance. Ne pas la présenter comme "pro-dialogue avec l'OTAN" — c'est inexact. Son positionnement est : indépendance BR face aux deux blocs.

---

### ANDREI Saniki — Bison Libre

> Source : `D:\CECPC\PRODUCTION\CREATION\07 - BELLA RUSSIA\POLITIQUE\Opposition BellaRussia.docx`

| Donnée | Valeur |
|---|---|
| **Parti** | **Bison Libre** — parti historique de l'opposition, cœur militant nationaliste **pro-mercurien** |
| **Rôle** | Dirigeant du Bison Libre — opposant institutionnel au régime Youkachenko |
| **Origine** | **Bi-national** — père mercurien — levier narratif fort (lien familial MER) |
| **Positionnement** | Critique de Youkachenko sur la forme, mais **favorable à l'action militaire de Mercure** en DR |
| **Discours** | "Our president is right for condemning the western intervention. We shall support Mercure action to defend our people." |
| **Tweet référence** | *"Military action seems to be the only resort against the injustices suffered by our citizens in Dacia Romania."* — #BisonLibre |
| **LO** | ⚠ Saniki est **pro-MER** sur le fond — exploitable camp rouge pour légitimer l'intervention MER via une voix d'opposition |
| **Relation Youkachenko** | Opposition institutionnelle — critique la *méthode* Youkachenko, pas l'objectif MER |
| **Calqué sur** | Figures d'opposition nationaliste biélorusse à tendance pro-russe |

**Utilisation éditoriale :**
⚠ Saniki n'est PAS un levier camp bleu pur — il soutient l'action MER. Son profil est exploitable par le camp rouge comme "même l'opposition BR approuve". EastWatch peut le citer pour brouiller les lignes. Sa bi-nationalité (père mercurien) est un levier ILI direct LO 5.

---

## Dynamique narrative BR — Chronologie des injects AURIGE 2BB

| Jour | Référence | Contenu | LO |
|---|---|---|---|
| **D+27** | 07.02.01i | Youkachenko **"Appel à la paix"** (BC1) — discours pro-MER déguisé en offre de paix | LO 5 |
| **D+27** | 07.05.02i | **Évacuation ressortissants BR** présents en DR vers la frontière | LO 5 |
| **D+27** | *(EN ATTENTE)* | @NOVUSORDOMUNDI — pillages à Héming liés aux ressortissants BR | LO 5 |
| **D+28** | 07.05.03i | **Manifestations** soutien MER en Bella Russia | LO 5 |
| **D+30** | 07.05.05i | **Fermeture frontière** BR | LO 5 |
| **D+31** | 07.05.06i | **Rencontre Youkachenko-Olamao** — consolidation alliance | LO 5 |
| **D+32** | 07.05.07i | **CEMA BR posture défensive** — BR se positionne militairement | LO 5 |
| **D+33** | 07.05.08i | **Ressortissants BR tués** par 2BB (selon BC1) | LO 5 + LO 3 |
| **D+34** | P-22 | **Conseil de sécurité BR** session extraordinaire | LO 5 |
| **D+35+** | P.03 | **Bascule politique BR** — opinion publique BR se retourne (arc EastWatch) | LO 5 + LO 1 |
| **D+39** | 07.05.10 | **Manifestations Minsk** après morts civils — "2BB = ASSASSINS" | LO 5 + LO 3 |
| **D+40** | 07.05.11i | **Mobilisation générale BR** | LO 5 |
| **Nuit D+39** | R5-2 | @HmunikVoice — "Les feuilles bougent à Minsk" — signal pré-mobilisation | LO 5 |

> ⚠ **Règle éditoriale P.03 :** L'arc de bascule politique BR est une opération de blanchiment — EastWatch présente les fractures internes BR comme signal d'espoir de paix, alors qu'elles servent à masquer la mobilisation réelle. TIKHANOV et SANIKI peuvent être cités dans cet arc.

---

## Média officiel BR

| Média | Code | Positionnement | Usage |
|---|---|---|---|
| **Bella Russia Channel 1** | BC1 / BCI | 🔴 Rouge — pro-Youkachenko, pro-MER | Articles officiels BR — BCI_Article_* |

**BC1 ne cite jamais Tikhanov ou Saniki** — ils sont persona non grata sur les médias d'État BR.

---

## Relations extérieures BR dans le scénario

| Relation | Nature |
|---|---|
| **BR ↔ Mercure** | Alliance stratégique — soutien politique, logistique, narratif de Mercure |
| **BR ↔ DR (Dacie Romanie)** | Hostilité — ressortissants BR en DR comme vecteur de friction |
| **BR ↔ OTAN** | Rupture — Youkachenko refuse tout dialogue avec l'alliance |
| **BR ↔ ONU** | Manipulation — Youkachenko utilise le Conseil de sécurité comme tribune |
| **Ressortissants BR en DR** | ~[chiffre à définir] — communauté présente dans les villes de Lorraine, cible narrative LO 5 |

---

## Portraits officiels — Personnages BR

| Personnage | Fichier | Dossier | Statut |
|---|---|---|---|
| Svetlana Tikhanov | `Svetlana Tikhanov - Nouvelle pahonie.png` | `D:\CECPC\PRODUCTION\CREATION\07 - BELLA RUSSIA\Portraits` | ✅ Firefly (2026-05-27) — intégré trombinoscope + avatar tweet |
| Andrei Saniki | `Andrei Saniki - Bison Libre.png` | `D:\CECPC\PRODUCTION\CREATION\07 - BELLA RUSSIA\Portraits` | ✅ Firefly (2026-05-27) — intégré trombinoscope + avatar tweet |
| Alexandre Youkachenko | `youkachenko.jpg` | `WEB\images\` uniquement — pas de portrait CREATION | ⚠ Disponible pour WEB, pas de portrait CREATION officiel |

> Dossier portraits BR : `D:\CECPC\PRODUCTION\CREATION\07 - BELLA RUSSIA\Portraits`
> Même logique que les portraits Mercure (`D:\CECPC\PRODUCTION\CREATION\02 - MERCURE\Portraits\`).
> Youkachenko : portrait de travail dans `WEB\images\youkachenko.jpg` — créer un portrait officiel Firefly si besoin d'un rendu haute qualité.

---

## Apprentissages par exercice

| Date | Exercice | Apprentissage |
|---|---|---|
| 2026-05-27 | AURIGE 2BB | SVETLANA Tikhanov + ANDREI Saniki créés — opposition démocratique BR pour contrer le discours de paix de Youkachenko (D+27). Portraits générés via Firefly, dossier `07 - BELLA RUSSIA\Portraits`. Peuvent alimenter arcs TV4 / P.03 / EastWatch. |
| — | À compléter | — |
