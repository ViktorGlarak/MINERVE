# MÉMOIRE — LEAC

> **Source de vérité durable du système LEAC.** Créée le **2026-09-17**.
> ⭐ **RÉFLEXE NON NÉGOCIABLE : CONSULTER cette mémoire DÈS QUE LEAC EST ÉVOQUÉ · y CONSIGNER APRÈS chaque avancée**, sans attendre de rappel utilisateur.
> CR daté → `LEAC\JOURNAL.md` · règle / décision / capacité durable → **ce fichier**.

---

## 1. Identité du système

**LEAC = Logiciel d'Élaboration et d'Appui au Contrôle.**

| Champ | Valeur |
|---|---|
| Objet | **Contrôler un poste de commandement** : préparer, noter sur le terrain, concaténer le travail de l'équipe, produire la **3A** puis le **compte rendu** |
| Nature | Application web — **réécriture v3** d'un logiciel existant (v2.5 du 2022-05-19) |
| Origine | Développé par le **CDAD-R** (Rambouillet). Concrétise la fiche de besoin **CNCIA 2015**, validée **EMAT 2017** |
| Administration générale | **CECPC** |
| Finalité doctrinale | **Standardiser les procédures au niveau armée de terre** ; référentiels adaptables selon le niveau du PC, les évolutions doctrinales et le RETEX |
| Utilisateurs | 4 profils : **chef de contrôle**, **chef d'équipe**, **officier de marque (ODM)**, **contrôleur** |
| Périmètre v3 | Localhost d'abord, puis **app de zone PLEIADE** |
| Dépôt | **`cecpc-pleiade/app-leac`** (privé) · local `C:\CECPC\pleiade\app-leac` · port dev **3700** |
| Documents sources | `LEAC\REFERENCES\` — les deux mementos v2.5 (utilisateur 44 p., administrateur 34 p.) |

### ⭐ La finalité v3, telle que l'utilisateur l'a formulée
> *« Les contrôleurs se retrouvent avec LEAC sur leur tablette en extérieur, et
> lorsqu'ils reviennent au bureau, grâce au VPN et à une connexion internet, ils
> peuvent synchroniser leurs données dans le LEAC du serveur pour bien concaténer
> toutes les données de chaque contrôleur. »*

C'est **la** exigence structurante. Tout le reste en découle.

---

## 2. Les 4 acteurs et leurs rôles *(memento utilisateur § I)*

| Acteur | Grade type | Ce qu'il fait |
|---|---|---|
| **Chef de contrôle** | colonel | Lien avec la direction d'exercice. **Valide** le paramétrage (pondérations), les observations de fin de cycle, la note finale. **Seul** à tenir la synthèse générale (2 cartouches : sur le PC / sur l'exercice) |
| **Chef d'équipe** | lieutenant-colonel | Commande et coordonne l'équipe. Porte la **synthèse du fonctionnement général et du travail collectif du PC** |
| **Officier de marque (ODM)** | officier d'active | **Référent du contrôle.** Seul à pouvoir l'initialiser. Responsable du paramétrage, de la **concaténation des données** et des productions. **Clôture** le contrôle |
| **Contrôleur** | officier, expert de son domaine | Maîtrise son référentiel, note, **étaye ses observations**, fait des propositions |

⚠ **Tout membre de l'équipe, chef de contrôle inclus, est potentiellement contrôleur.**

---

## 3. Le cycle de vie d'un contrôle — 8 statuts

`INITIALISATION → EN_PREPARATION → EXPORT → EN_CONTROLE → 3A → COMPTE_RENDU → CLOTURE → ARCHIVE`

Verrous portés par les statuts :
- **3A** → les **notations** se verrouillent ; la 3A reste modifiable.
- **COMPTE_RENDU** → seuls les **commentaires** des contrôleurs restent modifiables.
- Suppression d'un contrôle possible **uniquement** en initialisation ou préparation.

---

## 4. ⭐⭐ Les règles métier à ne jamais perdre

1. **Seules les FEUILLES se notent.** *(admin § VI.B.1)* Les niveaux supérieurs
   ne font que **la moyenne des niveaux inférieurs**. ⚠ La moyenne remonte **par
   niveau**, jamais à plat sur toutes les feuilles — sinon un sous-domaine à 3
   critères pèse plus qu'un sous-domaine à 2.
2. ⚠ **Un nœud sans feuille notée n'a PAS de note — il n'a pas zéro.** Confondre
   les deux fausse toutes les moyennes au-dessus et fait croire, à la réunion
   quotidienne, que le PC est en difficulté alors qu'on n'a simplement pas encore
   noté.
3. **Pondération à deux étages** : par **fonction** (note finale) et, sur les
   domaines **transverses**, par **membre**.
4. **Le drapeau** *(§ V.A.3)* — ⭐ **à quoi il sert**, car le memento ne le dit
   jamais : un **domaine transverse** (fonctionnement général du PC, travail
   collectif) n'appartient à aucune fonction, **plusieurs contrôleurs
   l'observent**. Les **notes** se moyennent (pondération par membre) ; les
   **observations**, qui sont du **texte libre**, ne se moyennent pas. Le drapeau
   désigne donc **la voix dont le bilan est projeté à la réunion du soir** —
   sinon le tableau de bord afficherait quatre paragraphes concurrents et le chef
   de contrôle arbitrerait en séance.
   ⚠ **Recadré en v3** : la v2.5 le donnait à *« la première personne cochée »*,
   c'est-à-dire à un **ordre de clic**. Une conséquence aussi lourde ne peut pas
   dépendre de l'ordre dans lequel on a coché des cases : en v3 le porteur se
   **désigne explicitement**, et le tableau de bord **filtre réellement** sur
   l'auteur des observations (`lireEtatDetaille` rend l'auteur de chaque valeur).
   ⚠ **Écart assumé avec le memento** *(voir `app-leac\docs\COUVERTURE.md`,
   § « Écarts assumés »)* : la v2.5 dit *« SEULS ses commentaires seront vus »*.
   Appliqué à la lettre, le travail écrit de trois contrôleurs **disparaît** de
   la réunion. En v3 le bilan du porteur reste la **parole officielle, seule
   affichée par défaut** — l'intention est tenue — mais les autres sont
   **consultables d'un geste**, nommées, « hors bilan officiel ». **Réversible
   en une ligne** si le CECPC préfère la règle stricte.
5. **Barème** *(admin § VI.E.7)* : note finale → tranche, niveau, label.
   ⚠ **Convention de bornes : `min` incluse, `max` exclue.** Sans elle, une note
   pile sur une borne tombe dans deux tranches ou aucune, selon l'ordre des lignes.
6. **Échelle de notation** paramétrable (note min, note max, **pas**). ⚠ La
   construire par **multiplication**, jamais par additions successives : `2 + 0,5
   + 0,5` dérive et sort « 3.4999999 ».
7. **Intitulé d'un contrôle** *(§ V.A.1)* : `TYPE_UNITÉ-EN-PROJECTION_UNITÉ-EN-MÉTRO`
   (ex. `VAP_GTD-INF_BARKHANE10_1RI`, `ANTARES_152RI`).
8. **Une unité n'est jamais supprimée, seulement désactivée** *(admin § IV.A.3)*.
9. **Un contrôleur ne modifie que les lignes physio de SON domaine** ; seul l'ODM
   change l'affectation de domaine.
10. **On ne consulte un contrôle archivé que si l'on y a contribué** *(§ VI.B.8)*.
11. **Rubrique physio** : `valeurs` vide = **saisie libre** ; sinon **liste de choix**.
12. **Import Excel complet des grilles = ÉCRASE tout l'existant** *(admin § VI.B.1)*.
13. ⭐⭐ **Figer un cycle est un état MÉTIER, pas un verrou d'écriture** *(§ III.B)*.
    Une saisie émise hors ligne **avant** le figeage et remontée **après** est
    **acceptée**, puis **signalée**. La refuser reconstruirait le défaut annoncé
    en § V.B.8 (*« toute modification durant la synchronisation sera perdue »*).
    ⚠ La comparaison se fait sur l'**horloge de Lamport**, jamais sur une date :
    deux tablettes n'ont pas la même heure. Voir `vault\decisions\DECISION-023`.
14. **Une seule réserve empêche de figer** : l'absence de porteur du drapeau.
    Tout le reste **informe sans bloquer** — sinon un contrôleur absent bloque un
    cycle indéfiniment. Le chef de contrôle est l'autorité, on l'informe.
15. ⭐ **Le cycle fait partie de la CIBLE d'une note**, pas d'un filtre :
    `Note#<cycle>:<pointId>`. Chaque cycle **renote les mêmes critères**, et
    c'est **l'écart entre cycles** qui dit si le PC progresse. Sans le cycle dans
    la clé, la 2ᵉ journée écrase la 1ʳᵉ et le découpage perd sa raison d'être.
16. **Chacun valide SA grille** *(§ III.D)* — jamais celle d'un autre. Une
    validation est un engagement sur ce qu'on a noté ; elle ne se délègue pas
    plus qu'une signature.

---

## 5. ⭐⭐ Le défaut de la v2.5 que la v3 corrige

Le memento utilisateur § V.B.8 avertit :
> *« **ATTENTION** : toute modification effectuée durant la synchronisation sera
> perdue. »*

Le dispositif v2.5 imposait : **hub réseau**, **16 postes en IP fixes**, un
**« PC maître »**, des **fichiers JSON sur clé USB**, et une **réplication MariaDB
multi-maître** sur les postes.

⚠ **Les 5 « erreurs récurrentes » du memento (§ V.D) venaient TOUTES de ce
dispositif, aucune du métier** — dont la plus parlante : **une apostrophe** dans
une grille cassait la synchronisation (SQL concaténé). Elles occupaient **un
cinquième du memento utilisateur**. C'est le meilleur argument de la réécriture.

---

## 6. ⭐⭐ Le mécanisme de concaténation retenu (v3)

**Une saisie n'écrit pas une ligne : elle ajoute un ÉVÉNEMENT daté.**
`(cible, champ, valeur, auteur, horloge)` — on transporte des **intentions**, pas
des états, et on les rejoue. Code : `src/lib/sync/fusion.ts`.

| Point | Règle |
|---|---|
| Domaines disjoints | Deux contrôleurs sur deux domaines **ne peuvent pas** entrer en conflit — cibles disjointes. **99 % des retours de terrain.** |
| Horloge | ⚠ **Horloge de Lamport**, jamais l'heure de la tablette : une tablette partie 5 jours **dérive**, et l'heure murale ferait gagner la plus en retard. Lamport ne dit pas *quand*, il dit *après quoi*. |
| Ordre d'arbitrage | **Total et déterministe** : horloge → appareil → id d'opération. ⚠ Sans ordre total, deux postes synchronisés divergent **en se croyant tous deux à jour** — le pire des bugs, parce qu'il est silencieux. |
| Perdantes | **Jamais jetées** (`appliquee=false` + `motifRejet`). ⚠ *Une valeur qui disparaît sans explication est un bug perçu, même quand le calcul est juste.* |
| Vraie collision | Seulement si **deux auteurs différents** sur la même cible. Une auto-correction n'en est pas une — les confondre noie l'ODM ou lui cache un vrai désaccord. |
| Idempotence | L'UUID d'opération est généré par la **tablette** → renvoyer deux fois ne joue qu'une fois. |

---

## 7. Parti pris de design — ✅ **VALIDÉ par l'utilisateur le 2026-09-17**

> Validé sur maquette vivante (écran de notation servi en local, essayé par
> l'utilisateur) : *« Ça me plaît, on peut partir là-dessus. »*
> 👉 **Ce parti pris fait désormais référence pour tous les écrans suivants.**
> Ne pas le rediscuter sans raison ; s'en écarter demande une justification.

**La cible est une tablette tenue à la main, dehors, parfois au soleil, parfois
avec des gants.**

- **Contraste élevé** — pas de gris pâle : dehors, ça disparaît.
- **Cibles de 48 px** — les 44 px recommandés supposent un doigt nu et une main stable.
- **Clair par défaut**, sombre en option — l'inverse de l'habitude, parce que le
  sombre est illisible au soleil.
- **La note se saisit en UN appui** (rangée de crans, pas de menu déroulant) : un
  menu impose 3 gestes et masque la valeur ; sur 300 critères, **900 gestes**.
- **L'état de synchronisation est permanent**, jamais une notification fugace :
  elle arrive toujours quand l'utilisateur regarde ailleurs.
- Système **PLEIADE** : graphite + craie, angles vifs, Archivo + JetBrains Mono,
  mention `EXERCICE · NON CLASSIFIÉ`.

---

## 8. État d'avancement

| Volet | État |
|---|---|
| Dépôt privé `cecpc-pleiade/app-leac` créé et poussé | ✅ 2026-09-17 |
| **Inventaire des 117 fonctions** des 2 mementos | ✅ `docs/COUVERTURE.md` |
| Schéma de données complet (annoté § par §) | ✅ `prisma/schema.prisma` |
| Moteur de fusion terrain | ✅ `src/lib/sync/fusion.ts` |
| Calcul de notation + barèmes | ✅ `src/lib/domaine/notation.ts` |
| Système visuel | ✅ `src/app/globals.css` |
| Tests de logique métier | ✅ **92/92** |
| ⭐ **Écran de notation terrain** | ✅ **écrit et validé** 2026-09-17 (`src/app/page.tsx`) — commit `aeceeb8` |
| ⭐ **Persistance hors ligne** (IndexedDB + journal d'opérations) | ✅ 2026-09-17 — `src/lib/offline/` — commit `7c640d1` |
| ⭐ **Écran de synchronisation** + revue des collisions | ✅ 2026-09-17 — `src/app/synchronisation/` |
| **Observations** (5 cartouches) persistées | ✅ 2026-09-17 — commit `a2f1f0c` |
| ⭐ **Écran de paramétrage ODM** (4 onglets § V.A) | ✅ 2026-09-17 — `src/app/parametrage/` — commits `fe90ede` puis `86da06d` (**persisté** au journal d'opérations, un champ par membre) |
| Règle de nommage de l'intitulé, **assistée et testée** | ✅ `src/lib/domaine/intitule.ts` — commit `8b51061` |
| ⭐ **Tableau de bord de la réunion quotidienne** (§ V.B.9) | ✅ 2026-09-17 — `src/app/tableau-de-bord/` + `src/lib/domaine/bilan.ts` — commit `d352962` |
| ⭐ **Écran de fin de cycle** (§ III.B / III.C) | ✅ 2026-09-17 — `src/app/fin-de-cycle/` + `src/lib/domaine/cycle.ts` — commit `edbf801` |
| **Cycles réels** (§ V.B.7) + **validation de grille** (§ III.D) | ✅ 2026-09-17 — commit `7510830` · le cycle entre dans la clé des notes |
| Glossaire, écrans d'administration | ❌ à écrire |
| Génération 3A (.pptx) / CR (.docx) | ❌ balises inventoriées, génération à écrire |
| Import/export Excel | ❌ spécifié |

**Répartition de la couverture** : 🟢 **14 faites** · 🟡 53 modèle en place · ⚪ 21
spécifiées · 🔵 **29 repensées** (le dispositif technique qui les imposait
disparaît — chacune justifiée dans `docs/COUVERTURE.md`).

---

## 9. Points ouverts / à trancher avec l'utilisateur

- ⏳ **Format d'import Excel des grilles** — memento admin § XII : *« en cours de
  rédaction »*. **Trou dans la doc source**, pas un oubli de notre part. Il faut
  un fichier réel du CECPC.
- ⏳ **Modèle de compte rendu** — § X : *« en cours de rédaction »*. Idem.
- ⏳ **Durée de vie du PIN hors ligne** : combien de jours une tablette reste-t-elle
  utilisable sans revoir le serveur ? Arbitrage sécurité / terrain.
- ⏳ **Reprise de l'existant** : importer les contrôles archivés de la v2.5, ou
  repartir à blanc ?
- ⏳ **Ordre des écrans à construire** — proposition : notation terrain d'abord
  (c'est le cœur et le plus utilisé), puis synchronisation, puis paramétrage.

---

## 10. Règles de travail de l'agent LEAC

1. **Propriété unique** : LEAC est le **seul propriétaire** des informations du
   système LEAC dans MINERVE. Les autres agents **citent**, ne recopient pas.
2. **Consulter avant, consigner après** — y compris quand LEAC n'est qu'évoqué en
   passant.
3. ⚠ **Ne jamais annoncer un écran comme fait tant qu'il ne l'est pas.** La
   distinction *spécifié* / *implémenté* de `docs/COUVERTURE.md` est la référence.
4. **Router vers l'agent compétent** : plateforme et déploiement → **PLEIADE** ·
   code → **ARCHITECTE** · rédaction → **SECRÉTAIRE**.
5. ⚠ **Modèle de branches PLEIADE** *(voir `PLEIADE\MEMOIRE.md` §2bis)* : travailler
   sur une branche provisoire, intégrer dans `main`, et **ne jamais pousser sur
   `prod`** sans demande explicite — cela **déploie devant les participants**.
6. **Aucun détail opérationnel réel** dans les jeux d'essai : noms d'unités et de
   personnes fictifs.
