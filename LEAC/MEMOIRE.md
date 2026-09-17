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
4. ⭐⭐ **Le drapeau** *(§ V.A.3)* — **à quoi il sert**, car le memento ne le dit
   jamais. Il y a **DEUX sortes de domaines** :
   - **Domaine de FONCTION** (S4 Logistique, S2…) — `fonctionId` renseigné.
     **Un seul** contrôleur le note et l'observe. ⚠ **Le drapeau n'y a rien à
     faire** : il n'y a qu'une voix, celle du titulaire.
   - **Domaine TRANSVERSE** (fonctionnement général du PC, travail collectif) —
     `fonctionId = null`, `transverse = true`. **Plusieurs** contrôleurs le
     notent *(memento § IV.B : le chef d'équipe « a notamment en charge la
     synthèse du fonctionnement général et du travail collectif du PC »)*.

   Sur un transverse, les **notes** se moyennent (pondération par membre), mais
   les **observations sont du texte** : trois paragraphes ne donnent pas un
   paragraphe, aucune opération ne les fusionne. **Le drapeau désigne la voix
   reprise à la réunion** *(memento p. 27 : « le bilan de cycle de la personne
   désignée par le drapeau »)*.

   ⚠⚠ **Le drapeau appartient au DOMAINE, pas au contrôle.** Chaque transverse a
   **son propre** porteur, qui peut être quelqu'un d'autre. Un drapeau unique
   pour tout le contrôle est une **faute** : il fait disparaître du tableau de
   bord les observations du S4 sur **sa propre** grille. *(Erreur effectivement
   commise le 2026-09-17, corrigée le même jour — commit `eeb64ea`.)*

   ⭐ **Écrit comme « QUI le porte »** (`Domaine#<id>#porteDrapeau`), champ
   unique par domaine — **pas** un booléen sur chaque membre. Avec un booléen,
   deux tablettes hors ligne désignant chacune leur porteur remontent deux
   `true` sur des **cibles différentes** : la fusion les garde **tous les deux**
   et le domaine se retrouve avec **deux drapeaux**. Champ unique = même cible =
   l'horloge tranche = **un seul porteur par construction**.

   ⚠ **Écart assumé avec le memento** *(voir `app-leac\docs\COUVERTURE.md`,
   § « Écarts assumés »)* : la v2.5 dit *« SEULS ses commentaires seront vus »*.
   Appliqué à la lettre, le travail écrit des autres **disparaît** de la réunion.
   En v3 le bilan du porteur reste la **parole officielle, seule affichée par
   défaut** — l'intention est tenue — mais les autres sont **consultables d'un
   geste**, nommées. **Réversible en une ligne** si le CECPC préfère la règle
   stricte.
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
17. ⭐⭐ **Une saisie annulée ne remonte pas.** Tant qu'aucune opération n'est
    partie, on ne garde que l'**écart net** par rapport à ce que le serveur
    connaît (table `socle`). ⚠ Ce n'est **pas** une économie de volume : un
    retrait remonté porte une horloge récente et **écraserait la note qu'un
    collègue vient de poser hors ligne**, au nom d'un geste qui n'a pas eu lieu.
    ⚠⚠ **Jamais une opération déjà remontée** — elle appartient à l'histoire
    commune. Voir `vault\decisions\DECISION-024`.

18. ⭐⭐ **On pose une MENTION, pas une note — et on ENREGISTRE LE MOT.**
    *« Comme la note n'est pas visible, on empêche les chiffres de guider le
    contrôleur »* (CECPC) ; *« les notes ne sont pas communiquées, seul le niveau
    est révélé »* (cours CBA Rubben). Le journal garde `"Remarquable"`, jamais
    `4,75` : l'échelle est en cours de recalibration, et un journal de nombres
    aurait perdu ce que le contrôleur voulait dire.
    ⚠ **Un mot retiré de l'échelle ne vaut pas zéro** — il ne compte pas, et il
    est **signalé**. Voir `vault\decisions\DECISION-025`.
    ⚠ **Où le chiffre a le droit d'apparaître** : tableau de bord de l'équipe
    (outil de travail interne), **jamais** l'écran de notation ni le compte rendu.
19. **Échelle N4 retenue** *(à faire confirmer)* : Exceptionnel 5 · Remarquable
    **4,75** · **Très satisfaisant 4,5** · **Satisfaisant 4** · Moyen 3,5 ·
    Insuffisant 3 · Défaillant 2,5 · Mauvais esprit 2. Le haut passe au **quart
    de point**, le bas reste au demi : c'est en haut que les seuils sont serrés.
    ⚠ **Effet de bord assumé** : remonter Remarquable de 4,50 à 4,75 remonte les
    moyennes — une grille tout « Remarquable » passe du niveau 4 au niveau 5.
20. **Barème CFOT 2026** — ≥ 4,65 niveau 5 · 4,4–4,65 niveau 4 · 4–4,4 niveau 3 ·
    < 4 niveau 2. ⚠ **Remplace** celui du memento v2.5 (4,5 / 4 / 3). Le
    **niveau 1 = « non observé »** : ce n'est pas une tranche de note.
21. ⭐⭐ **Le LABEL qualifie l'EXERCICE, pas l'unité.** Les critères mesurent la
    production → un **niveau** ; les 10 exigences mesurent les conditions du
    contrôle → une **lettre**. 9-10 = A · 7-8 = B · 5-6 = C.
    ⚠⚠ **« ≤ 4 exigences OU exigences obligatoires non réalisées = contrôle non
    validé »** : neuf exigences sur dix ne donnent **pas** le label A si une des
    **cinq obligatoires** manque. Et cela peut entraîner la **rétrogradation de
    l'ANTARES en observation**.
    ⚠ « Sans ses appuis » est un **plafond** (label C max), pas une note : il ne
    peut que faire baisser. Voir `vault\decisions\DECISION-026`.
22. **La pondération porte sur le DOMAINE**, pas sur le membre qui l'observe —
    le classeur NG donne Fonctionnement général 8, Travail collectif 6, … total
    54. ✅ **Le classeur NG fait foi** ; l'annexe VII du modèle de CRF porte
    d'autres valeurs, elle est d'une autre époque.
    ⭐ **Le mandat du N+1 les adapte** : seules les valeurs *changées* sont
    enregistrées, et le compte rendu dit lesquelles s'écartent du référentiel.
23. ⭐ **Les CINQ cartouches du logiciel = les cinq rubriques des annexes V et
    VI** du compte rendu (observation générale · points forts · points faibles ·
    points à confirmer · proposition). Correspondance **exacte**. L'annexe I n'en
    reprend que trois : c'est un **résumé**, pas une perte.

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
| Tests de logique métier | ✅ **214/214** |
| ⭐ **Écran de notation terrain** | ✅ **écrit et validé** 2026-09-17 (`src/app/page.tsx`) — commit `aeceeb8` |
| ⭐ **Persistance hors ligne** (IndexedDB + journal d'opérations) | ✅ 2026-09-17 — `src/lib/offline/` — commit `7c640d1` |
| ⭐ **Écran de synchronisation** + revue des collisions | ✅ 2026-09-17 — `src/app/synchronisation/` |
| **Observations** (5 cartouches) persistées | ✅ 2026-09-17 — commit `a2f1f0c` |
| ⭐ **Écran de paramétrage ODM** (4 onglets § V.A) | ✅ 2026-09-17 — `src/app/parametrage/` — commits `fe90ede` puis `86da06d` (**persisté** au journal d'opérations, un champ par membre) |
| Règle de nommage de l'intitulé, **assistée et testée** | ✅ `src/lib/domaine/intitule.ts` — commit `8b51061` |
| ⭐ **Tableau de bord de la réunion quotidienne** (§ V.B.9) | ✅ 2026-09-17 — `src/app/tableau-de-bord/` + `src/lib/domaine/bilan.ts` — commit `d352962` |
| ⭐ **Écran de fin de cycle** (§ III.B / III.C) | ✅ 2026-09-17 — `src/app/fin-de-cycle/` + `src/lib/domaine/cycle.ts` — commit `edbf801` |
| **Cycles réels** (§ V.B.7) + **validation de grille** (§ III.D) | ✅ 2026-09-17 — commit `7510830` · le cycle entre dans la clé des notes |
| ⭐ **Domaines transverses** (§ V.A.3) — pondération, observateurs, drapeau **par domaine** | ✅ 2026-09-17 — `src/lib/domaine/domaines.ts` — commit `eeb64ea` |
| ⭐ **Compactage du journal** — une saisie annulée ne remonte pas | ✅ 2026-09-17 — `src/lib/sync/compactage.ts` + table `socle` — commit `675cfd3` |
| ⭐⭐ **App de zone PLEIADE déployable** — Dockerfile, workflow `prod`, sondes, Keycloak | ✅ 2026-09-17 — commit `4eccf1f` + `catalog/leac.yml` · voir `docs/DEPLOIEMENT.md` |
| ⭐⭐ **Notation par MENTIONS** — chiffres invisibles, le mot enregistré | ✅ 2026-09-17 — `domaine/echelle.ts` — commit `f0b69eb` |
| ⭐ **Lecture des grilles Excel** du CECPC, deux formats + contrôle qualité | ✅ 2026-09-17 — `import/grille.ts` · `npm run grille:lire` — commit `aeb9773` |
| ⭐⭐ **Les VRAIES grilles branchées** — 14 domaines, 1 352 critères, 5 niveaux | ✅ 2026-09-17 — commit `165009b` |
| ⭐ **LABEL de l'exercice** — 10 exigences, A/B/C, plafond « sans appuis » | ✅ 2026-09-17 — `domaine/label.ts` — commit `95c7fcb` |
| ⭐ **Compte rendu final (.docx)** — lettre + annexes I à VII | ✅ 2026-09-17 — `/compte-rendu` — commits `16627e3` et `02ca61d` |
| ⭐ **3A (.pptx)** — une diapo par domaine, taux à côté du camembert | ✅ 2026-09-17 — commit `02ca61d` |
| **Pondérations adaptables par le mandat du N+1** | ✅ 2026-09-17 — commit `e3079f8` |
| ⭐ **Branches `main` et `prod` en place sur GitHub** | ✅ 2026-09-17 — `prod` créée depuis `main` au commit `f3e0555` |
| **Note d'intégration pour la plateforme** | ✅ `docs/INTEGRATION-PLEIADE.md` — écrite pour qui devra comprendre sans avoir écrit |
| Glossaire, écrans d'administration | ❌ à écrire |
| Génération 3A (.pptx) / CR (.docx) | ❌ balises inventoriées, génération à écrire |
| Import/export Excel | ❌ spécifié |

**Répartition de la couverture** : 🟢 **~25 faites** · 🟡 ~48 modèle en place · ⚪ ~18
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
