# MÉMOIRE — DELATTRE (exercice DELATTRE 26)

> **Source de vérité détaillée de l'exercice DELATTRE 26.** Créée le **2026-07-22**.
> ⭐ **RÉFLEXE : CONSULTER cette mémoire AVANT toute production · y CONSIGNER APRÈS chaque avancée**, sans attendre de rappel utilisateur.
> Successeur de MINAUTORE (AURIGE 7BB / MINOTAURE 26), lui-même successeur de GUILLAUME (AURIGE 2BB).

---

## 1. ⚠️ IDENTITÉ DE L'EXERCICE — À RENSEIGNER

> **Rien n'est encore connu de DELATTRE 26 au 2026-07-22** hormis son nom. Demander ces éléments à l'utilisateur
> avant toute production, puis remplir ce tableau — **il conditionne tout le reste** (surtout le **niveau**, qui
> détermine la calibration des injects).

| Champ | Valeur | Impact |
|---|---|---|
| Nom complet / cadre OTAN | **DELATTRE 26** (usage courant : « DELATTRE ») | — |
| Organisateur | ⚠️ *à renseigner* | — |
| **Unité(s) entraînée(s)** | ⚠️ *à renseigner* | Destinataires des injects |
| **Niveau** (brigade / division / CA) | ⚠️ *à renseigner* | **⭐ Détermine la calibration — le point n°1 du RETEX** |
| Lieu + dates réelles | ⚠️ *à renseigner* | Calendrier |
| Temps de jeu (D+ → dates) | ⚠️ *à renseigner* | `DAY_MAP` MELMIL + `dayorder` |
| Zone d'opérations + H-codes | ⚠️ *à renseigner* | Cohérence géographique |
| **Camps** (qui attaque / défend) | ⚠️ *à renseigner* | ⚠ **Vérifier le sens : le 7BB était INVERSÉ vs le 2BB** |
| Pays fictifs impliqués | ⚠️ *à renseigner* | Quels ANALYSTES mobiliser |
| Sources de montage | ⚠️ *à renseigner* (JEMM ? Event List ? synchromatrice ? OPORD ?) | Pipeline d'ingestion |
| Storylines → LO | ⚠️ *à renseigner* | `lo_config.js` |

---

## 2. Socle hérité — acquis valables dès maintenant

### Lignes Opératoires GLM26 (référence permanente)
**LO1** Appui hybride à la manœuvre (effort permanent) · **LO2** Volonté de combattre · **LO3** Guerre des pertes ·
**LO4** Vent de libération · **LO5** Rupture des alliances.
→ Tout inject a une **LO principale** ; sans LO il est orphelin. Les LO sont **une aide, pas une contrainte**.

### Règles narratives permanentes
Équilibre des camps · **règle du CLIMAX** (pic informationnel sur le moment tactique majeur) · **noyau de vérité 80/20** ·
neutralité visuelle des camps pour les entraînés · **Steps PSYOPS 1→2→3 sans saut** · pas de renvoi vers un contenu futur ·
**GET** et non « Europe » pour la zone fictive · codage **H-préfixe** · numéros de téléphone fictifs cohérents.

### Propriété des données (anti-divergence)
- **Camp d'un persona** : fait foi **uniquement** dans le registre MASTAURIGE (+ `avatars.js`) et les entités `vault\entities\personas\`.
  L'Analyste du pays **tranche**, tout le monde **cite** — on ne recopie jamais une valeur de camp.
- Doctrine narrative d'un personnage pays → l'**ANALYSTE** du pays. Format/HTML → **MASTAURIGE**. Effets ILI → **EXPERT_INFLUENCE**.

---

## 3. ⭐ RETEX MINOTAURE 26 — à appliquer dès le montage
> Fiche complète : `MINAUTORE\RETEX_MINOTAURE_26.md` (points forts / erreurs / recommandations, sourcés).

**Les 5 leçons :**
1. **Calibrer TACTIQUE** — trop d'injects stratégiques pour une cible brigade = aucun effet (constat unanime des 3 documents).
2. **Fermer la boucle de retour** — sans retour sur le traitement des injects : « travailler dans le vent », démotivation. **Mesure la plus rentable.**
3. **Les GT produisent des scénarios**, pas des débats d'objectifs (sur MINOTAURE, injects décidés dans les 2 derniers jours).
4. **Casser les silos** RENS / FORAD / DIV (fiches bio faites **deux fois**).
5. **Reconduire ce qui a marché** : MASTAURIGE + EHO matérialisé + **1 traitant par LO**.

**À porter en amont (prérequis de montage, pas des erreurs de production) :** internet ouvert au poste (ou 2 postes),
postes de la cellule regroupés, carte de la ZO affichée, traitants en copie des mails chef/adjoint, **formation aux logiciels**,
ratio expert image/opérateurs équilibré (1 pour 7 = goulot), **abonnements outils financés par le CECPC**,
**synthèse des country books**, **annuaire des avatars**.

**⚠ JEMM** : jugé dispersant, non modifiable, à faible apport vs MASTAURIGE et **inadapté au niveau brigade** ;
droits traitants bloquants en l'absence du chef/adjoint. → MASTAURIGE reste l'outil de travail réel.

---

## 4. Actifs réutilisables — ne pas refaire ce qui existe

| Actif | Où | Statut |
|---|---|---|
| **EHO 7BB** — profond, « réutilisable pour de futurs exercices » (RETEX) | `MINAUTORE\MEMOIRE.md` + trombinoscope 7BB | ✅ disponible |
| **Gabarit MASTAURIGE v0.3** (portage post-MINOTAURE du 2026-07-22) | `D:\CECPC\MASTAURIGE\LOCALSTORAGE_WEB_VERSION` | ✅ à jour (format JEMM, split de card, correctifs calendrier, STARTEX + statuts permanents) |
| **Registre des avatars** (base CASW ORION 26, réutilisée 2BB puis 7BB) | `MASTAURIGE\MEMOIRE.md` + `moteur\avatars.js` | ⚠ **à consulter AVANT tout nouveau compte fictif** |
| **Chartes médias** : Today Mercure, TV4 International, BC1, HEXAGONE, Site OTAN, EFS | `MASTAURIGE\MEMOIRE.md` | ✅ cloner, ne pas recréer |
| **Doctrine ILI** : Storm-1516/VIGINUM, Morelli, Sun Tzu, mentalité russe, lawfare | `EXPERT_INFLUENCE\REFERENCES\` | ✅ |
| **Catalogue d'injects niveau brigade** + doctrine de calibration | `AURIGE\MEMOIRE.md` | ✅ anti-« trop stratégique » |
| **Méthodologie transverse AURIGE** (11 points) | `AURIGE\MEMOIRE.md` § méthodologie | ✅ |
| **Générateur de carte d'état** | `MINAUTORE\generer_etat_exercice.py` | 🔁 à adapter pour DELATTRE |

⚠ **Vérifier la transposabilité** de tout actif 7BB : les **camps** et la **zone** peuvent différer sur DELATTRE 26.

---

## 5. Chantiers d'ouverture (dès que l'identité est connue)

- [ ] Renseigner le tableau §1 (identité) — **bloquant pour le reste**
- [ ] Créer l'instance outillage depuis la **vierge v0.3** + configurer le calendrier (`OUTILS\CONFIGURER_EXERCICE.py` → `DAY_MAP`)
- [ ] Établir la table **H-préfixe** de la ZO
- [ ] Définir les **storylines → LO** (`lo_config.js`)
- [ ] Constituer l'EHO (réutiliser le 7BB si la zone/les camps le permettent)
- [ ] Adapter le générateur de **carte d'état** (`DELATTRE\ETAT_EXERCICE.md`)
- [ ] **Poser d'emblée les demandes RETEX** : responsable du retour sur injects, référent inter-cellules, prérequis SIC

---

## 6. Journal de l'exercice

> *(À alimenter à chaque avancée : décisions, injects produits, validations d'agents, corrections.)*

### [2026-07-22] Création de l'agent
Agent **DELATTRE** créé (20ᵉ du système MINERVE) à la demande de l'utilisateur, en préparation de l'exercice **DELATTRE 26**.
Enregistré au registre `CLAUDE.md`, dans `SYSTEME\ROUTAGE.md`, compteur `NOYAU\MEMOIRE.md` porté à 20.
Prompt système `SYSTEME\PROMPTS\delattre.md` créé depuis le modèle MINAUTORE + gabarit `aurige.md`, **enrichi du RETEX MINOTAURE**.
⚠ **Identité de l'exercice non encore communiquée** — à recueillir auprès de l'utilisateur.
