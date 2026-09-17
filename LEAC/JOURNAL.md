# JOURNAL — LEAC (historique chronologique, append-only)

> Comptes rendus datés des travaux sur le système LEAC. Les règles et l'état durable sont dans `MEMOIRE.md`.

---

## 2026-09-17 (suite 2) — Paramétrage persisté, tableau de bord de la réunion

**Demande utilisateur** : « ok tu peux avancer » — poursuite du développement
sur la feuille de route annoncée.

### 1. Le paramétrage survit à la fermeture de l'application — commit `86da06d`

L'écran de l'officier de marque était **en mémoire** : fermer l'onglet effaçait
l'équipe, les pondérations et le porteur du drapeau. Il écrit désormais dans le
**même journal d'opérations** que la notation — un paramétrage corrigé *en cours*
de contrôle remonte donc au serveur comme le reste.

- ⭐ **Granularité retenue : un CHAMP par membre** (`MembreEquipe#<id>#nom`),
  jamais un objet « équipe » entier. Écrire l'équipe en bloc ferait qu'un ODM
  modifiant un **poids** écraserait le **nom** qu'un collègue vient de corriger
  sur une autre ligne — alors que les deux gestes n'ont rien à voir. Champ par
  champ, ils se fondent sans conflit. *(Même propriété que les 5 cartouches
  d'observation, obtenue de la même façon.)*
- `useEcritureDifferee` **extrait** — les observations et le paramétrage en
  avaient un besoin identique ; dupliquée, la minuterie aurait divergé au premier
  correctif. **Deux déclencheurs : repos de saisie ET sortie de champ.** La v2.5
  n'écrivait qu'à la sortie de case (§ II.B) — insuffisant sur tablette : écran
  verrouillé, bascule d'application, batterie à plat, et la sortie de champ
  n'arrive jamais. On perdrait le **dernier** paragraphe, donc le plus récent.
- Texte = différé ; **poids et cases à cocher = écrits immédiatement** (différer
  un clic n'apporte rien et retarde sa remontée).
- Le drapeau qui deviendrait **orphelin** (retirer le droit d'observer à son
  porteur) est **déplacé**, pas perdu.

### 2. Tableau de bord de la réunion quotidienne (§ V.B.9) — commit `d352962`

`/tableau-de-bord` + `src/lib/domaine/bilan.ts`. Trois questions, **dans cet
ordre** — et l'ordre est le fond du sujet :

1. ⭐ **Où en est-on** — le taux de remplissage, **avant** toute note. Lire
   « 4,2 » sur 8 % de points saisis fait conclure qu'un PC est au niveau alors
   que personne n'a encore rien vu.
   ⚠ **Le taux se compte en POINTS, pas en moyenne de taux** : un domaine à 60
   critères et un domaine à 6 ne représentent pas le même travail restant. Une
   moyenne de taux dirait « 50 % » là où il reste 59 points sur 66.
2. **Qu'est-ce qui ressort** — note par fonction, puis détail par sous-domaine,
   dépliable. ⚠ Le détail **s'arrête au niveau au-dessus des feuilles** : le
   critère par critère appartient à la grille, pas à une réunion — déplier
   soixante lignes devant une assemblée ne fait lire personne.
3. **Qu'en dit le porteur du drapeau.**

⭐⭐ **Le drapeau devient un vrai filtre.** En v2.5 c'était un *avertissement*
(« la première personne cochée aura un petit drapeau ») : une règle que le
logiciel n'appliquait pas. L'appliquer demandait de connaître l'**auteur** de
chaque observation — d'où `lireEtatDetaille`, qui rend l'auteur de chaque valeur
de l'état dérivé. Les remarques des autres sont **écartées du bilan, jamais
supprimées**, et l'écran l'écrit noir sur blanc.

⚠ **Écran en LECTURE SEULE, à dessein.** On ne corrige pas une note pendant la
réunion : celui qui l'a posée n'est pas forcément là, et une note changée sans
lui est une note que personne n'assume.

### 3. Ce que les tests verrouillent — **78/78** (+27)

13 tests sur le bilan, tous sur des erreurs **invisibles à l'œil** :
- ⭐ Une fonction **non abordée est EXCLUE** de la moyenne, elle **ne compte pas
  zéro**. Sans cette règle, le premier matin d'un contrôle affiche « Inapte
  opérationnel » à un PC dont personne n'a rien vu.
- Une fonction de **poids 0** sort du calcul **mais reste à l'écran**, motif écrit
  en clair — *« pourquoi cette ligne n'est pas dans la moyenne »* est exactement
  la question posée à voix haute en réunion.
- Taux en points et non en moyenne de taux (cas 60/60 + 0/6).
- Contrôle vierge : note `null`, barème `null`, taux `0` — **pas `NaN`**.

### 📝 Fichiers autoritaires modifiés
- `app-leac` : commits **`86da06d`** et **`d352962`** — `docs/COUVERTURE.md`
  passe à 🟢 **10 faites** / 🟡 57 / ⚪ 21 / 🔵 29.
- `LEAC\MEMOIRE.md` — tableau d'état, règle métier n°4 (drapeau) recadrée.

### ⚠ Rien n'est poussé
`app-leac` est **en avance de 8 commits** sur `origin/main`. Dépôt partagé avec
Xavier : pas de poussée sans demande explicite.

### ⏭️ Prochaine étape
1. **Écran de validation de fin de cycle** (§ III.B) — figer un cycle, valider
   les observations, basculer vers la 3A.
2. **Génération 3A (.pptx) / CR (.docx)** — ⏳ bloqué sur le **modèle de CR** du
   CECPC (§ X, « en cours de rédaction »), demandé par l'utilisateur.
3. **Import/export Excel des grilles** — ⏳ bloqué de même (§ XII).
4. Trancher la **durée de vie du PIN hors ligne**.

---

## 2026-09-17 (suite) — Documentation ingérée, dépôt créé, socle v3 écrit

**Demande utilisateur** : à partir des deux mementos v2.5, produire une version
« nettement plus optimisée, plus fluide, plus esthétique » ; créer le dépôt privé
`cecpc-pleiade/leac` ; **100 % des fonctionnalités assimilées** ; finalité = les
contrôleurs sur **tablette en extérieur**, puis **synchronisation par VPN** au
retour pour **concaténer les données de chaque contrôleur**.

### Ce que la documentation a révélé
- ⭐⭐ **Le défaut central de la v2.5** est écrit noir sur blanc dans le memento
  utilisateur § V.B.8 : *« toute modification effectuée durant la synchronisation
  sera perdue »*. C'est exactement ce que la demande de l'utilisateur vise.
- ⚠ **Les 5 « erreurs récurrentes » (§ V.D) viennent TOUTES du dispositif
  technique, aucune du métier** : réinstallation complète, `multi-master.info` à
  supprimer, câble réseau à débrancher au démarrage, et — la plus parlante — **une
  apostrophe** dans une grille qui casse la synchronisation (SQL concaténé). Elles
  occupent **un cinquième du memento**. C'est l'argument le plus fort pour la
  réécriture, et il vient du document lui-même.
- ⚠ **Deux sections des mementos sont « en cours de rédaction »** : le **modèle CR**
  (§ X) et le **format des grilles Excel** (§ XII). Ce sont des **trous dans la
  source**, pas des oublis — signalés à l'utilisateur, à demander au CECPC.

### Fait
- **Dépôt privé `cecpc-pleiade/leac` créé** (API GitHub, identifiants du poste,
  jamais affichés), cloné dans `C:\CECPC\pleiade\leac`, **poussé** (`main`).
- ⭐ **`docs/COUVERTURE.md`** — les **117 fonctions** des deux mementos, une par
  une, avec leur état : 🟢 4 faites · 🟡 63 modèle en place · ⚪ 21 spécifiées ·
  🔵 **29 repensées**. Les 29 ne sont pas des abandons : 27 disparaissent parce que
  la contrainte technique qui les imposait (hub, IP fixes, PC maître, clé USB,
  comptes locaux) n'existe plus, chacune justifiée dans sa ligne.
- **`prisma/schema.prisma`** — modèle complet, **annoté paragraphe par paragraphe**
  du memento, pour qu'on puisse vérifier la couverture sans relire les PDF.
- ⭐⭐ **`src/lib/sync/fusion.ts`** — le moteur de concaténation. Journal
  d'opérations, **horloge de Lamport** (jamais l'heure de la tablette, qui dérive
  après 5 jours en campagne), **ordre d'arbitrage total et déterministe**,
  opérations perdantes **conservées avec leur motif**, distinction entre vraie
  collision (deux auteurs) et auto-correction.
- **`src/lib/domaine/notation.ts`** — seules les feuilles se notent, moyenne
  remontante **par niveau**, `null ≠ 0`, pondération par fonction, barèmes
  (`min` incluse / `max` exclue), échelle sans dérive flottante.
- **`src/app/globals.css`** — système visuel PLEIADE **adapté au terrain** :
  contraste élevé, cibles 48 px, clair par défaut, note en un appui, état de
  synchro permanent.
- **`README.md`** + **`docs/ARCHITECTURE.md`**.
- **Vérifié : 51/51** contrôles, dont l'invariant qui compte — *l'ordre d'arrivée
  des opérations ne change pas le résultat*.

### ⚠ Ce qui N'EST PAS fait, et ne doit pas être annoncé autrement
**Aucun écran n'est écrit.** Le socle (modèle, logique, design, doc) est là ; toute
l'interface reste à produire. `docs/COUVERTURE.md` distingue explicitement
*spécifié* de *implémenté*, et fait référence.

### 🔤 Renommage du dépôt — `leac` → **`app-leac`** (même jour)
**Demande utilisateur** : aligner le nom sur la nomenclature des autres apps.
Fait par l'API GitHub (`PATCH /repos`), dossier local renommé
(`C:\CECPC\pleiade\app-leac`), **remote réaligné**, tests repassés **51/51**.
- ℹ️ GitHub laisse une **redirection** depuis l'ancien nom : un clone existant
  continuerait de fonctionner. Le remote a tout de même été mis à jour
  explicitement — une redirection silencieuse finit toujours par surprendre.
- ⚠ **La nomenclature n'est pas universelle** : **`eho`** est une app du catalogue
  et ne porte PAS le préfixe `app-`. À signaler si l'on veut une règle stricte.

### ⭐ Écran de notation terrain écrit et VALIDÉ (même jour)
**Déclencheur** : l'utilisateur a demandé à *voir* dans un navigateur. Il n'y
avait alors **aucun écran** — le socle seul. Plutôt que de le lui dire sèchement,
j'ai construit l'écran de notation, qui était la prochaine étape proposée.

- **Verdict utilisateur** : *« Ça me plaît, on peut partir là-dessus. »*
  👉 **Le parti pris de design fait désormais référence** pour tous les écrans
  suivants (consigné en `MEMOIRE.md` §7).
- **Ce qui a été montré** : grille S4 LOGISTIQUE **réelle** (libellés du memento),
  note en **un appui** sur une rangée de crans, **moyennes remontant en direct**
  par niveau, compteur rempli/attendu, niveau de barème calculé, pastille de
  synchronisation permanente, les 5 cartouches d'observation.
- ⚠ **Réappuyer sur le cran choisi efface la note** — seul moyen de revenir à
  « non noté » sans menu, et « non noté » n'est pas la note la plus basse.
- Commit **`aeceeb8`**. Vérifié : `tsc` 0, `eslint` 0/0, **51/51**, page en 200.
- ⚠ **Toujours une démonstration** : notes en mémoire, IndexedDB et journal
  d'opérations pas branchés. L'écran le dit à l'utilisateur, en toutes lettres.

#### 🔧 Deux pannes d'outillage rencontrées et corrigées
1. ⚠⚠ **Cache npm du poste corrompu** — `npm install` a échoué (entrée `_cacache`
   manquante pour `exceljs`) **en sortant avec un code de succès** : l'échec était
   donc invisible, et seul `next: command not found` l'a révélé. Réparé par
   `npm cache verify` (31 entrées manquantes purgées, 354 Mo récupérés).
   👉 **Peut expliquer d'autres installs bizarres sur ce poste.**
2. **`eslint.config.mjs` passait par `FlatCompat`**, que `eslint-config-next` 16
   ne supporte plus : re-sérialisation d'une **référence circulaire**
   (`plugins.react`) et trace illisible qui ne nomme pas la cause. Remonté sur le
   montage d'`eho`, qui tourne.

### ⭐⭐ Persistance hors ligne + écran de synchronisation (commit `7c640d1`)
**Contexte** : l'utilisateur a demandé les deux documents manquants au CECPC et
m'a dit de « faire le reste en attendant ». J'ai donc traité les deux chantiers
qui ne dépendent d'aucun document.

#### La base locale n'est **pas un cache**
Elle doit tenir **une semaine sans voir le serveur** et savoir exactement ce
qu'il lui reste à remonter. Un cache, on peut le vider ; ceci, jamais — ce serait
jeter le travail d'un contrôleur. Trois tables aux rôles **distincts** :
- `operations` — **le journal**, la vérité de ce qui n'est pas remonté ;
- `valeurs` — l'état courant, **pure commodité de lecture** (se reconstruirait
  depuis le journal) ; rejouer 4 000 opérations à chaque écran serait absurde ;
- `meta` — identité de l'appareil + **horloge persistée**. ⚠ L'identifiant
  d'appareil doit **survivre aux redémarrages** : c'est lui qui départage deux
  saisies d'horloge égale. S'il changeait, l'arbitrage cesserait d'être
  reproductible et deux postes pourraient diverger.

#### ⭐ Un seul chemin d'écriture, sans exception
On n'écrit **jamais** une valeur : on **émet une opération**, l'état dérivé suit
dans la **même transaction**. ⚠ Si un chemin contournait le journal, la saisie
s'afficherait correctement sur la tablette et **ne remonterait jamais** — le
contrôleur croirait son travail enregistré. C'est la perte silencieuse que la v3
doit rendre impossible.

#### Deux exigences de terrain dans le branchement React
1. **L'appui repeint le cran immédiatement**, la base suit en parallèle. ⚠ Sur
   tablette, un retard de 80 ms se lit comme un **appui raté** — l'utilisateur
   réappuie, et pose deux fois la note.
2. **Si l'écriture locale échoue, l'écran REVIENT en arrière et le dit.** Une
   note affichée mais non enregistrée est le pire état possible : le contrôleur
   passe à la suite en confiance.

#### L'écran de synchronisation répond à trois questions, dans cet ordre
Ce qui n'est pas parti · ce qui est arrivé des autres · ⭐ **ce qui a été
recouvert, et par qui**. La troisième est la seule qui compte : une
synchronisation qui annonce « terminée » **cache les désaccords entre
contrôleurs**, alors qu'un désaccord sur une note est une **information
d'animation**, pas un incident à masquer.
- ⚠ **Les opérations ne sont marquées « remontées » qu'APRÈS accusé.** Marquer
  avant perdrait le travail si l'envoi échouait en route ; renvoyer ne coûte rien
  puisque le serveur déduplique sur l'identifiant d'opération.
- La simulation fait tourner **le même code de fusion** que celui du serveur.

**Vérifié** : `tsc` 0 · `eslint` 0/0 · **51/51** · les deux pages en **200**.
Un avertissement React 19 corrigé au passage (`setState` synchrone dans un effet,
cause de rendus en cascade).

⚠ **Restent non persistées : les observations** (les 5 cartouches). L'écran le dit
en toutes lettres à l'utilisateur.

### Observations persistées + écran de paramétrage ODM (commits `a2f1f0c`, `fe90ede`, `8b51061`)

#### Observations — le piège du texte libre
⚠ Une note se pose en un appui ; une observation se tape **caractère par
caractère**. Une opération par frappe = **des centaines d'opérations pour une
phrase**, journal gonflé et revue de synchronisation noyée sous le bruit.
👉 On reprend la règle **déjà posée par v2.5** (§ II.B, « enregistre à chaque
sortie de case ») **plus un filet : écriture après 800 ms de repos**. ⚠ Sortir
d'un champ **n'est pas garanti sur tablette** — on verrouille l'écran, on bascule
d'application, la batterie lâche. Attendre le `blur` seul, c'est accepter de
perdre **le dernier paragraphe**, donc le plus récent.
- ⭐ **Chaque cartouche est un CHAMP distinct** : deux contrôleurs remplissant
  l'un « points positifs » et l'autre « propositions » **ne peuvent pas se
  recouvrir**. La granularité par champ achète cette propriété gratuitement.
- ⚠ Purge des minuteries au démontage : sans elle, quitter l'écran juste après
  une frappe laisse un `setTimeout` écrire dans un composant mort.

#### ⭐⭐ Paramétrage ODM — deux AVERTISSEMENTS du memento devenus des propriétés du formulaire
1. **La règle de nommage** (§ V.A.1) était écrite **en rouge** : un avertissement
   en rouge dans un memento, c'est **une règle qu'on oublie** — elle reposait sur
   la mémoire d'un officier tapant un champ libre une fois tous les six mois. Les
   exemples du memento le prouvent : `VAP_GTD-INF_BARKHANE10_1RI` a **4 segments**,
   `ANTARES_152RI` en a **2**. 👉 On saisit les morceaux, **l'intitulé se compose**.
2. **Le drapeau** (§ V.A.3) : « *la première personne cochée aura un petit
   drapeau* ». ⚠ **Une conséquence aussi lourde ne peut pas dépendre d'un ordre de
   clic.** Il se donne explicitement, il est nommé, retirer le droit d'observer à
   son porteur **le déplace** au lieu de le laisser orphelin, et si personne ne le
   porte l'écran le dit — sinon aucun commentaire ne remonterait à la réunion
   quotidienne sans que personne comprenne pourquoi.

Aussi : alerte sur les **fonctions obligatoires non pourvues**, affichée au
paramétrage plutôt qu'au déploiement quand il est trop tard ; suivi **vert/gris**
des validations de grille (§ V.A.6) ; poids par fonction, **0 neutralisant** une
fonction sans la retirer de l'équipe.

#### 🔎 Un test a tranché une ambiguïté que je n'avais pas vue
J'avais annoncé la normalisation de l'intitulé comme « testée » **sans l'avoir
testée**. En écrivant les 12 contrôles, ils ont immédiatement révélé une question
non tranchée : **un espace disparaît-il ou devient-il un tiret ?**
👉 **Décision assumée : il devient un TIRET.** « 152 RI » → « 152-RI ». Supprimer
l'espace collerait des mots illisibles (« 1ERRI »), et le memento écrit justement
« GTD-INF » **avec son tiret**. Qui veut « 152RI » le tape sans espace.
**63/63.**

### ⏭️ Prochaine étape
1. **Persister le paramétrage** (même journal d'opérations) — aujourd'hui en
   mémoire.
2. **Tableau de bord de la réunion quotidienne** (§ V.B.9) : domaines, taux de
   remplissage, moyennes, bilan de cycle du porte-drapeau.
3. ⏳ **En attente du CECPC** : format Excel des grilles, modèle de CR.
4. Trancher la **durée de vie du PIN hors ligne**.

---

## 2026-09-17 — Création de l'agent

**Demande utilisateur** : créer dans MINERVE un agent **LEAC** qui **stocke toutes
les données `.md` importantes et le suivi du projet**, avec le réflexe de **tout
mettre à jour à chaque avancée, à l'ouverture et à la fermeture de session**, et
d'**être consulté dès que LEAC est évoqué**.

### Fait
- Dossier `LEAC\` créé avec `README.md`, `MEMOIRE.md`, `JOURNAL.md` et
  `REFERENCES\`. ⭐ **Mémoire et journal séparés dès le départ** — leçon de
  MASTAURIGE, dont la mémoire avait atteint 397 Ko avant d'être scindée.
- Agent ajouté au **registre de `CLAUDE.md`** (23ᵉ), au **compteur de
  `NOYAU\MEMOIRE.md`**, à l'**arbre de routage** et au **prompt système**
  `SYSTEME\PROMPTS\leac.md` — la checklist complète du `CLAUDE.md` racine.
- Les quatre réflexes demandés sont écrits **là où ils s'appliquent** : règle
  d'usage du `README.md`, règles de travail du `MEMOIRE.md`, prompt système, et
  branche de routage.

### ⚠ État
**Rien n'est connu du système LEAC hormis son nom.** L'identité (§1 de la mémoire)
est un tableau de champs ⚠️ à renseigner. **La documentation doit être fournie par
l'utilisateur** — annoncée dans le même message.

### ⏭️ Prochaine étape
1. **Recevoir la documentation**, la classer dans `REFERENCES\`, la résumer dans
   `MEMOIRE.md` §1 et §2.
2. Trancher le **rattachement** : LEAC est-il lié à PLEIADE, à un exercice, ou
   autonome ? Cela déterminera les collaborations de l'agent dans le registre.
