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

### 4. Écran de fin de cycle (§ III.B / § III.C) — commit `edbf801`

`/fin-de-cycle` + `src/lib/domaine/cycle.ts`. Trois gestes dans l'ordre du soir :
lire les réserves, écrire le bilan et les synthèses, figer.

⭐⭐ **La décision centrale — figer est un état MÉTIER, pas un verrou
d'écriture.** Une note posée hors ligne **avant** le figeage peut très bien ne
remonter qu'**après** : c'est même le cas normal d'un contrôleur qui rentre au
bureau en fin de soirée. La refuser reconstruirait de nos mains le défaut annoncé
au § V.B.8. Elle est donc **acceptée, conservée, et signalée** — l'écran liste ce
qui est arrivé depuis la décision, et le chef de contrôle tranche s'il rouvre.
→ [[DECISION-023]]

⚠ La comparaison se fait sur l'**horloge de Lamport**, jamais sur une date : deux
tablettes n'ont pas la même heure, et une tablette éteinte trois jours revient
avec une horloge murale fausse. L'horloge de référence est lue **avant** d'écrire
le figeage, sinon le figeage se signalerait lui-même comme une saisie tardive.

**Une seule réserve est bloquante** — l'absence de porteur du drapeau (le cycle
serait figé sur un bilan sans auteur). Tout le reste informe sans empêcher :
exiger la complétude produit le piège classique où un contrôleur absent bloque un
cycle indéfiniment. ⚠ L'écran **dit pourquoi** les autres ne bloquent pas — sinon
un avertissement qui laisse passer se lit comme un bug.

Le reste :
- § III.C — les **synthèses générales** restent **visibles et verrouillées** hors
  chef de contrôle. Les masquer ferait croire qu'elles n'existent pas, et la
  question reviendrait à chaque contrôle.
- ⚠ Ces verrous sont de **lisibilité**. La règle qui compte s'applique **au
  serveur**, à la réception des opérations — un écran ne protège rien, et le
  fichier le dit pour qu'on ne s'y trompe pas.
- **Confirmation maison, jamais `confirm()`** : sur tablette la boîte système est
  minuscule, hors charte, et se valide par réflexe.
- **Rouvrir n'efface rien** : c'est une opération de plus, la trace reste.
- **Sélecteur de rôle**, marqué comme échafaudage de démonstration : il permet
  d'**éprouver** le cloisonnement au lieu de le croire sur parole. Il disparaît
  avec la session Keycloak.
- Les membres de démonstration ont un `identityId`, **sauf `m6`** : c'est le
  renfort de dernière minute (§ V.B.3), créé en local, sans identité de zone. Les
  écrans doivent le supporter — c'est un cas réel, pas une donnée incomplète.

**14 tests de plus (92/92)**, dont ceux qui verrouillent qu'une saisie **à**
l'horloge du figeage n'est **pas** tardive, et que le figeage ne se signale pas
lui-même.

### 5. Cycles réels, validation de grille, et le drapeau expliqué — commit `7510830`

**Question de l'utilisateur** : *« à quoi sert le système de donner le drapeau
dans LEAC, je ne comprends pas son utilité »*. Elle est justifiée : le memento
dit ce que le drapeau **fait**, jamais **pourquoi** il existe.

#### ⭐ Le drapeau — la réponse, à conserver
Un **domaine transverse** (fonctionnement général du PC, travail collectif)
**n'appartient à aucune fonction** : plusieurs contrôleurs l'observent, chacun
depuis son poste. Pour les **notes**, aucun problème — elles se moyennent,
pondérées par membre (c'est le rôle de `PonderationTransverse`). Pour les
**observations**, qui sont du **texte libre**, on ne peut pas faire la moyenne
de quatre paragraphes. **Il faut une voix.** Le drapeau désigne celle dont le
bilan est projeté le soir *(memento p. 27 : « le bilan de cycle de la personne
désignée par le drapeau »)*.

Ce qui rend la v2.5 incompréhensible : désignation par **ordre de clic**,
porteur **jamais nommé** ensuite, et conséquence annoncée comme un simple
**avertissement dans un manuel**.

⚠ **Écart assumé, documenté** dans `docs/COUVERTURE.md` § « Écarts assumés » :
la v2.5 dit *« SEULS ses commentaires seront vus »* — le travail écrit de trois
contrôleurs disparaît de la réunion sans que personne le sache. En v3, le bilan
du porteur reste la **parole officielle seule affichée par défaut** (l'intention
est tenue : une seule voix), mais les autres sont **dépliables**, nommées, sous
la mention « hors bilan officiel ». **Réversible en une ligne** si le CECPC
préfère la règle stricte — l'utilisateur a été prévenu.

#### § V.B.7 — le cycle entre dans la CLÉ des notes
Le numéro de cycle était une constante : « ouvrir le cycle suivant » ne pouvait
rien vouloir dire. Il devient une valeur du journal (`Controle#…#cycleCourant`),
et surtout les notes portent le cycle dans leur cible :
`Note#<cycle>:<pointId>#valeur`.

⭐ **Ce n'est pas un filtre, c'est la cible.** Chaque cycle **renote les mêmes
critères**, et c'est **l'écart entre cycles** qui dit si le PC progresse. Sans le
cycle dans la clé, la 2ᵉ journée écraserait la 1ʳᵉ.

⚠ Les notes écrites **avant** ce changement sont rattachées au cycle d'origine,
en trois lignes marquées à retirer. Une donnée qui s'évapore parce qu'on a changé
un format de clé est exactement la perte silencieuse que cette application
refuse — **y compris quand la victime est une base de démonstration**.

#### § III.D — chacun valide SA grille
L'état `grilleValidee` s'affichait mais rien ne permettait de le poser. Le bouton
n'apparaît que sur **sa propre** ligne : une validation est un engagement (« ce
que j'ai noté, je l'assume »), elle ne se délègue pas plus qu'une signature.

#### Rôle joué, partagé entre les écrans
Le sélecteur de démonstration passe dans `src/lib/demo/role.tsx` et remonte au
`layout` : le cloisonnement se traverse d'un écran à l'autre, sinon on ne peut
pas l'éprouver. ⚠ Il vit dans `sessionStorage`, **pas dans le journal** — ce
n'est pas une donnée du contrôle, l'y écrire l'enverrait au serveur et le ferait
apparaître dans la revue de synchronisation. Lu via `useSyncExternalStore` :
l'outil prévu pour un magasin extérieur à React, qui traite aussi le rendu
serveur, lequel n'a pas de stockage.

### 6. CORRECTIF — le drapeau ne s'applique qu'aux transverses — commit `eeb64ea`

**Relance de l'utilisateur** : *« un profil qui porte le drapeau met en avant ses
observations sur toutes les grilles ? »* — lecture exacte de ce que faisait mon
code, **et mon code était faux**.

Mon filtre était **global** : il retenait les observations du porteur sur tout le
contrôle. Les remarques du S4 sur **sa propre** grille disparaissaient donc du
tableau de bord dès que le drapeau était ailleurs — alors que personne d'autre
n'écrit sur un domaine de fonction.

**Ce que dit réellement le memento** : le § V.A.3 est situé dans l'onglet
« pondérations », au milieu des domaines transverses. Le drapeau y coche « les
personnes qui pourront mettre des observations **dans les domaines
transverses** ». Il ne concerne qu'eux.

La distinction vit désormais dans `src/lib/domaine/domaines.ts`, avec la règle
`remonteAuTableauDeBord` en **un seul endroit** — elle était auparavant répartie
entre l'écran et le hook, et fausse aux deux.

⚠ **Corollaire** : le drapeau appartient au **domaine**, pas au contrôle. Chaque
transverse a **son propre** porteur. L'onglet Pondérations devient donc un bloc
par transverse — la forme exacte de l'écran du memento p. 15 : poids, « observe »,
drapeau, pour chaque membre.

⭐ **Écrit comme « QUI le porte »**, champ unique par domaine, et non comme un
booléen sur chaque membre. Avec un booléen, deux tablettes hors ligne qui
désignent chacune leur porteur remontent deux `true` sur des **cibles
différentes** : la fusion les garde **tous les deux**, le domaine se retrouve
avec **deux drapeaux**. Champ unique = même cible = l'horloge tranche.

Aussi : un domaine transverse réel rejoint les données de démonstration
(FONCTIONNEMENT GÉNÉRAL ET TRAVAIL COLLECTIF DU PC, § IV.B), et l'écran de
notation permet d'en changer — sans quoi le drapeau restait **invérifiable à
l'usage**. `GRILLES_PAR_MEMBRE` ne contient plus que les domaines de fonction :
un transverse n'appartient à personne.

**11 tests de plus (103/103)**, tous sur la règle qui était fausse.

### 📝 Fichiers autoritaires modifiés
- `app-leac` : commits **`86da06d`**, **`d352962`**, **`edbf801`** et
  **`7510830`** et **`eeb64ea`** — `docs/COUVERTURE.md` passe à 🟢 **15 faites** /
  🟡 52 / ⚪ 21 / 🔵 29, et gagne une section **« Écarts assumés avec le
  memento v2.5 »**.
- `LEAC\MEMOIRE.md` — tableau d'état, règle métier n°4 (drapeau) recadrée.

### ⚠ Rien n'est poussé
`app-leac` est **en avance de 10 commits** sur `origin/main`. Dépôt partagé avec
Xavier : pas de poussée sans demande explicite.

### ⏭️ Prochaine étape
1. ⏳ **En attente de l'utilisateur** : confirmer l'**écart assumé sur le
   drapeau** (dépliable) ou revenir à la règle stricte du memento.
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
