# Avis n°36 — app-admin : les scénarios de bruit de fond

> **Date** : 2026-10-03 · **Demandeur** : l'utilisateur · **Écrans** : `app-admin`, création d'un scénario (`NewScenarioDialog.tsx`), liste « Scénarios » (`ScenariosList.tsx`), bandeau en tête de la fiche (`IncidentPicker.tsx` › `BandeauIncident`, appelé par `editor/ScenarioEditor.tsx`).
> **Statut** : 🟡 proposé, à arbitrer par l'utilisateur. La mise en œuvre revient à PLEIADE / ARCHITECTE, à tester en local avant tout push.
> Suite des avis n°27 (ranger les scénarios), n°28 (lien avec l'incident MELMIL) et n°31 (scénario de storyline).
> ⚠ DESIGNER contribue, il ne tranche pas : ce sont des propositions argumentées. Le besoin de l'utilisateur et les choix de PLEIADE / ARCHITECTE font foi.

## Besoin exprimé

Pouvoir créer des **scénarios de bruit** : du bruit de fond informationnel sur les réseaux de l'exercice (posts ordinaires, ambiance, actualité banale). Ils ne sont reliés à **aucun incident ni aucune storyline MELMIL**, mais on doit pouvoir les **nommer** et les retrouver **bien rangés** dans l'onglet « Scénarios ». L'utilisateur propose une 3e option dans « Cible du scénario » ou une case à cocher.

## Constat (lecture du code, 2026-10-03)

| # | Constat | Gravité (Nielsen, 0-4) | Source |
|---|---|---|---|
| C1 | Dès que la zone a un MELMIL, l'incident est **obligatoire**, côté formulaire (`cibleOk`) comme côté serveur (`resoudreCible`). Un bruit de fond n'a donc **aucun chemin de création**. | 3 | Heuristique 7 « souplesse » (REF-14) |
| C2 | « Sans incident » a **un seul sens** aujourd'hui : « Non classés », c'est-à-dire **à ranger**, avec un message qui invite à choisir l'incident. Un bruit voulu s'y perdrait, mêlé aux oublis et aux anciens scénarios. | 3 | Heuristique 2 « correspondance avec le monde réel », région commune (REF-06) |
| C3 | Le bandeau de la fiche dit « Ce scénario n'est rattaché à aucun incident : choisissez-le… ». Pour un bruit, c'est une **fausse alerte permanente**. | 2 | Heuristique 1 « état du système visible » (REF-14) |
| C4 | Le segment actuel est fait de deux `<button>` **sans rôle ni état annoncé** (`aria-pressed` ou `radio` absents). Ajouter un 3e choix est l'occasion de le rendre accessible. | 2 | REF-13 4.1.2 ; WAI-ARIA APG (REF-19) |

## Recommandations (classées par gain)

### 1. Création

**R1 — Un 3e segment, pas une case à cocher.** `Cet incident | Toute une storyline | Bruit de fond`.
- *Pourquoi un segment* : les trois cas **s'excluent**. C'est un seul choix parmi trois, tous visibles d'un coup (Hick, REF-06). Une case « Scénario de bruit » posée à côté du segment créerait un **mode caché** : il faudrait griser le segment quand elle est cochée, et l'écran pourrait afficher deux réponses contradictoires (« Cet incident » sélectionné et « bruit » coché). C'est l'erreur que l'heuristique 5 demande de prévenir (REF-14).
- **Ordre** : « Bruit de fond » en **dernier**, parce que c'est l'exception à la règle « un scénario = un incident ». **« Cet incident » reste le choix par défaut**, c'est-à-dire l'option recommandée en premier (Hick, REF-06 ; règle 16).
- **Libellé** : « **Bruit de fond** ». Il est court, il tient dans le segment à côté des deux autres, et il dit la chose sans jargon. « Scénario de bruit » répéterait le mot « scénario » déjà porté par le titre de la fenêtre. Le même mot sert **partout** : segment, section de la liste, bandeau de la fiche, étiquette de ligne (cohérence, heuristique 4, REF-14).
- **Accessibilité** : `role="radiogroup"` avec `aria-label="Cible du scénario"`, chaque segment en `role="radio"` + `aria-checked`, les flèches pour passer d'un choix à l'autre (modèle Radio Group du WAI-ARIA APG, REF-19 ; REF-13 4.1.2). L'état sélectionné reste marqué par le fond plein **et** le poids du texte, pas par la couleur seule (règle 10). Au téléphone, si les trois ne tiennent pas, le segment passe à la ligne (`flex-wrap`), sans couper les libellés.
- *Effort* : faible.

**R2 — En mode « Bruit de fond », une ligne d'aide prend la place du sélecteur d'incident** (même endroit, pour que la fenêtre ne saute pas) :
> *Posts ordinaires, ambiance, actualité banale. Rattaché à aucun incident : il n'apparaîtra pas dans MELMIL.*

La seconde phrase dit la **conséquence** du choix avant qu'on le valide (heuristique 1, REF-14 ; GOV.UK : dire ce qui va se passer, REF-10). Le focus passe directement au champ **Nom**, puisque c'est la seule chose qui reste à décider (Fitts et économie de gestes, REF-06).

**R3 — Le champ Nom devient l'ancre du scénario.**
- **Placeholder** en mode bruit : « *Ambiance — marché de Toul, matinée* ». Il montre un **modèle** : la nature, puis le lieu ou le thème, puis le moment. C'est le pendant du « 08.01.I04 — … » des scénarios d'incident (avis n°27, R5).
- **Pré-remplissage** : rien à pré-remplir, l'app ne sait rien de ce bruit (Tesler, REF-06 : on pré-remplit ce que l'on **sait**, on n'invente pas). En revanche, **si le nom avait été pré-rempli par le système** (intitulé de l'incident ou de la storyline, `nomTouche === false`), le passage en « Bruit de fond » **le vide**. Sinon on créerait un bruit nommé « 08.01.I04 — Fuite du rapport ». Un nom tapé par l'humain, lui, est **conservé**.
- **Début / fin** : défaut inchangé (maintenant → +4 h).
- **Description** : placeholder adapté, « *Ce que ce bruit doit installer : ton, thèmes, rythme…* ».
- **Remarque douce, jamais un refus** (Postel, REF-06) : si le nom tapé en mode bruit **commence par un code MELMIL** connu, une ligne le signale : « *Ce nom commence par 08.01.I04 : voulez-vous plutôt le rattacher à cet incident ?* » avec un lien « Rattacher à 08.01.I04 », qui bascule le segment sur « Cet incident » avec l'incident choisi. L'utilisateur reste libre de créer quand même.
- *Effort* : faible.

**R4 — Le message de validation dit quoi faire** (même ligne et même style que les messages actuels, sous les dates). En mode bruit, la cible est toujours valide ; il ne reste que le nom :
> *Donnez un nom à ce bruit de fond : c'est sous ce nom qu'il sera rangé dans la liste.*

C'est un texte qui dit **comment corriger**, pas seulement ce qui manque (GOV.UK, REF-10 ; règle 24). Le bouton « Créer » reste le seul bouton principal (règle 6).

**R5 — Côté données : un drapeau explicite, jamais une déduction** *(proposition à PLEIADE / ARCHITECTE, qui décident du modèle)*. Un bruit doit être **déclaré** (par exemple un champ `nature = "incident" | "storyline" | "bruit"`, ou un booléen `bruit`), et non déduit de `incidentId === null`. Sinon il redevient indiscernable d'un « Non classé » (C2). Le serveur accepte alors l'absence d'incident **seulement** quand le drapeau est posé. La règle « incident obligatoire » de l'avis n°28 reste donc entière pour tout le reste. À l'envoi en mode bruit, on n'envoie **ni** `incidentId` **ni** storyline, même si un choix précédent traîne dans l'état du formulaire.
- *Effort* : moyen (schéma + route + DTO). C'est la condition de tout le reste.

### 2. Liste « Scénarios »

**R6 — Une section à elle, « Bruit de fond », placée après l'arborescence MELMIL et avant « Non classés ».**
- **Distincte de « Non classés »** : « Non classés » veut dire *à ranger* (une tâche), « Bruit de fond » veut dire *rangé, volontairement sans incident* (un état). Deux sens, deux régions (région commune, REF-06 ; heuristique 2, REF-14).
- **Pourquoi après l'arborescence, pas en tête** : le repère principal reste le code MELMIL (avis n°27). Le bruit peut être **nombreux** : en tête, il repousserait l'arborescence vers le bas à chaque arrivée. En fin de liste, il reste à une place **fixe**, et repliable (affichage mémorisé par poste, avis n°27 R4) pour qui ne s'en occupe pas.
- **Pourquoi avant « Non classés »** : « Non classés » reste **le dernier groupe**, comme fixé par l'avis n°27 ; on ne déplace pas un repère acquis (Jakob, REF-06).
- **En-tête** : même composant que les en-têtes d'event (`pa-scn-groupe-1`), icône `activity` (onde, déjà dans `Icons.tsx`), titre « **Bruit de fond** », puis le résumé habituel « · 7 scénarios · 2 en lecture · 1 en erreur ». Sous l'en-tête, une ligne neutre, **sans appel à l'action** : « *Scénarios d'ambiance, rattachés à aucun incident MELMIL.* »
- *Effort* : faible, une fois R5 fait.

**R7 — Dans la section, un sous-regroupement par jour, et un ordre stable.**
- **Par jour de début**, avec des en-têtes de niveau 2 (`pa-scn-groupe-2`) : « *Jeu. 15/10 · 4 scénarios · 1 en lecture* ». On pense au bruit dans le temps (« l'ambiance de jeudi matin »), et ses noms sont libres : un tri alphabétique n'aiderait pas à s'y retrouver.
- Dans un jour, **ordre par heure de début, puis par nom**. Il est **stable** : un bruit ne bouge pas quand quelqu'un le modifie (avis n°27 : jamais de tri par « dernière modification »).
- Le regroupement par jour est **toujours** présent, même s'il n'y a qu'un jour : une structure qui change de forme quand les données grossissent casse la mémoire de position (heuristique 4, REF-14).
- *Effort* : faible.

**R8 — Sur la ligne, la colonne du code dit « bruit », au lieu d'un tiret.** Aujourd'hui un « — » dans la colonne du code signifie *il manque quelque chose*. Pour un bruit, la colonne affiche l'icône `activity` suivie du mot « **bruit** », dans le style `pl-tag-outline` : neutre, sans couleur propre. Le mot double l'icône (règle 10). Le reste de la ligne est **inchangé** : nom, statut, créneau, publiés x/y, auteur, supprimer. C'est le même motif que les autres lignes, donc rien à réapprendre (Jakob, REF-06).
- **Pas de couleur dédiée** : l'accent et le rouge sont réservés à la sélection et aux alertes (Von Restorff, règle 20). Le bruit doit rester **calme** à l'écran, comme il l'est dans l'exercice.
- *Effort* : faible.

**R9 — Recherche et filtres.**
- **Filtres de statut** : ils s'appliquent à la section comme aux autres groupes. Une section vide disparaît, et les effectifs des filtres comptent les bruits (« En lecture 4 » inclut les bruits en lecture).
- **Recherche texte** : elle trouve les bruits par leur nom, leur description et leur auteur, comme aujourd'hui. Taper « **bruit** » fait aussi apparaître toute la section, comme taper « 08.01 » montre la storyline (avis n°27, R3).
- **Recherche par code** (« 08.01 », « I04 ») : elle n'affiche **pas** les bruits, c'est le résultat attendu.
- **Pas de nouveau filtre « Nature »** pour l'instant : la section repliable suffit, et chaque rangée de filtres en plus est un choix de plus à chaque visite (Hick, REF-06). Ce filtre ne serait à reconsidérer que si l'utilisateur constate qu'il replie et déplie souvent la section.

**R10 — « Non classés » ouvre une sortie vers le bruit.** Son message devient :
> *Pour ranger un scénario, ouvrez-le et choisissez son incident MELMIL, ou déclarez-le « bruit de fond » (bandeau en haut de la fiche).*

Les anciens scénarios sans incident qui étaient en réalité du bruit trouvent ainsi **leur place en deux clics**, sans ressaisie (Tesler, REF-06).

**R11 *(facultatif)* — Un raccourci discret dans l'en-tête de la section** : un lien « + Bruit de fond » qui ouvre la création **déjà réglée sur « Bruit de fond »**. Même logique que « Créer un scénario pour cet incident » côté MELMIL (avis n°28, R10). Ce n'est pas un second bouton principal : « + Nouveau scénario » reste l'unique action principale de la page (règle 6). Sans droit d'écriture, ce lien n'apparaît pas.

### 3. Fiche d'un scénario de bruit

**R12 — Le bandeau dit ce qu'est le scénario, pas ce qui lui manque.** Au lieu de « Incident MELMIL » :
- intitulé `pl-eyebrow` « **Bruit de fond** », précédé de l'icône `activity` ;
- texte : « *Rattaché à aucun incident MELMIL : ce scénario n'apparaît pas dans MELMIL.* » ;
- action secondaire (`pl-btn-secondary`, éditeurs seulement) : « **Rattacher à un incident…** ». Les points de suspension signalent qu'un choix va s'ouvrir.
- Pour un observateur, le même bandeau **sans le bouton** : pas de bouton qui mènerait à un refus (règle déjà appliquée dans la liste).
- *Sources* : heuristique 1 (REF-14) ; mettre en valeur en atténuant le reste (REF-07) : le bandeau d'un bruit est sobre, il n'appelle rien.

**R13 — Bruit → incident : par le même sélecteur que d'habitude.** « Rattacher à un incident… » ouvre **dans le bandeau** le sélecteur d'incident existant (`IncidentPicker`, avec recherche, groupé par storyline, doublons visibles), plus « Annuler ». Une fois l'incident choisi :
- le drapeau « bruit » est **retiré** et l'incident posé, **dans la même opération** ;
- le **nom est conservé**, l'app ne renomme jamais ce que l'humain a nommé. La liste affichera de toute façon le code de l'incident dans sa colonne ;
- une ligne d'état confirme : « *Rattaché à 08.01.I04, rangé sous la storyline 08.01, visible dans MELMIL.* » (heuristique 1 ; Peak-End, règle 18).
- **Pas de fenêtre de confirmation** : l'opération est réversible et ne retire rien.

**R14 — Incident → bruit : depuis « Changer », pas par un bouton de plus.** Dans le bandeau d'un scénario d'incident, « Changer » ouvre déjà le sélecteur. On y ajoute, **sous la liste**, une dernière option séparée par un filet : « **Aucun incident : en faire du bruit de fond** ». Avant de valider, une phrase dit la conséquence : « *Le pictogramme ▶ disparaîtra de la carte 08.01.I04 dans MELMIL.* » Puis on confirme d'un clic (« Détacher »).
- *Pourquoi* : changer de cible reste **une seule porte d'entrée** (« Changer »). Le bandeau ne se charge pas d'un second bouton pour un geste rare (Hick, REF-06 ; REF-07). Et la phrase de conséquence est due, parce que le geste modifie ce que voit une **autre cellule**, dans MELMIL (heuristique 5, REF-14).
- **Scénario de storyline** : son bandeau n'a pas de « Changer » aujourd'hui (le périmètre se gère dans MELMIL, avis n°31). Le passer en bruit peut attendre un besoin exprimé. Si on le fait, ce sera par le même motif.

**R15 — Un « Non classé » (ancien scénario sans incident) propose les deux sorties.** Son bandeau actuel garde le sélecteur d'incident, et ajoute un bouton secondaire « **C'est du bruit de fond** ». Un clic, et le scénario passe dans la section « Bruit de fond » (lien avec R10).

## À éviter

1. **Une case à cocher en plus du segment**, ou deux contrôles différents pour la même notion selon l'écran (R1).
2. **Déduire le bruit de l'absence d'incident** : il se confondrait avec « Non classés », et la règle « incident obligatoire » deviendrait contournable par simple oubli (R5).
3. **Un faux incident** « BRUIT » ou un code fictif (« 00.00.B01 ») dans MELMIL ou dans le nom. Cela polluerait MELMIL, ses synthèses (avis n°34) et la lecture des codes.
4. **Ranger le bruit dans « Non classés »** avec son message « à ranger » : ce serait une fausse alerte permanente, et le vrai « à ranger » se noierait dedans (C2, C3).
5. **Une couleur vive ou un fond teinté** pour la section ou les lignes de bruit. L'accent et le rouge restent rares (règle 20).
6. **Un onglet ou une page à part** pour le bruit : la recherche serait coupée en deux, on perdrait la vue d'ensemble des statuts « en lecture / en erreur », et cela romprait avec l'habitude d'une seule liste (Jakob, REF-06).
7. **Des noms automatiques** (« Bruit 1 », « Bruit 2 ») : l'utilisateur veut **nommer**, et un nom sans contenu ne se retrouve pas.
8. **Mettre « Bruit de fond » par défaut**, ou en premier dans le segment : la règle reste « un scénario = un incident », et le bruit est l'exception.
9. **Trier les bruits par dernière modification** (avis n°27).
10. **Renommer un scénario au moment d'une conversion**, dans un sens comme dans l'autre (R13).

## Questions à l'utilisateur (réponse par défaut proposée entre crochets)

- **Zone sans MELMIL** : aujourd'hui le champ « Cible » n'y apparaît pas, et tout scénario s'y range par le code lu dans son nom. Faut-il pouvoir y déclarer un bruit ? [Oui, par **une case** « Bruit de fond (ambiance, aucun incident) », puisque là le choix est binaire. C'est le seul cas où la case est le bon contrôle.]
- **Une greffe** (arrivée depuis une publication, bouton ShitStorm) peut-elle être du bruit ? [Oui : le segment reste proposé, avec « Cet incident » par défaut.]
- **MELMIL** doit-il voir le bruit (par exemple « 3 bruits de fond en lecture » dans la synthèse) ? [Non pour l'instant : par définition, le bruit n'appartient pas à la planification des incidents.]

## Doctrine retenue

⭐ **Une absence voulue n'est pas un manque : elle se déclare, elle se nomme, et elle a sa place.** On distingue « sans rattachement **par choix** » (un état, rangé et calme) de « sans rattachement **par oubli** » (une tâche, signalée). On ne déduit jamais l'un de l'autre.
