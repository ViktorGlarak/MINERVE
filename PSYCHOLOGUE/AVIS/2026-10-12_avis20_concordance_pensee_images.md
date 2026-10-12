# Avis n°20 — Concordance fiche ↔ bloc « vie », pensée du décideur, images des joueurs (2026-10-12)

**Auteur** : PSYCHOLOGUE · **Demandeur** : NOYAU (pour PLEIADE, suites du banc IA du Mac)
**Sources** :
- `pont\banc_ia\CONSIGNES_PC.md` (§1, §2, §3bis) et `RESULTATS_MAC_2026-10-12.md` ;
- code lu sans le modifier : `dev\prototype-ia\generer-vie.mjs`, `completer-foyers.mjs`, `controler-concordance.mjs` ; `app-ia\src\moteur\esprit.mjs` (`persona`, bloc « QUI ELLE EST ») ; `app-ia\src\moteur\vie.mjs` (`blocVie`) ;
- rapport du contrôle `concordance.json` (105 avatars fictifs, scratchpad de session) ;
- doctrine : avis n°14 §B-C (bloc `vie`, registre, « fiche > registre > message »), n°15 (foyers), n°17 (récit de soi contrôlé, première version jamais protégée), n°18 (chœur), n°19 (règle « on n'amplifie pas une rumeur sans son démenti »).

---

## 0. Ce que montre le rapport (au-delà des chiffres transmis)

- **Les âges du bloc `vie` ne sont pas une information** : 72 avatars sur 105 ont l'un de quatre âges (42 ans : 30 ; 35 : 17 ; 38 : 13 ; 45 : 12). C'est la valeur « par défaut » du modèle, faute d'avoir reçu l'âge de la fiche. Aucune raison de les garder.
- **Les foyers contradictoires viennent surtout de MON avis n°15**, appliqué par `completer-foyers.mjs` : le tirage par tranche d'âge s'est fait sur l'âge inventé (`v.age ?? 40`), **sans lire la situation de la fiche**. D'où « compagne + 3 enfants » chez des « célibataires sans enfant » de 29 ans, et une compagne chez des veufs. Erreur de ma part : l'avis n°15 aurait dû imposer la situation eho comme entrée. **Règle durable** : *toute dérivation automatique d'un trait de vie prend le profil eho en entrée ; une statistique de population ne complète que ce que la fiche ne dit pas.*
- Une partie des écarts « la fiche cite des enfants, la vie n'en a pas » sont de **faux positifs du contrôle** : « veuf, deux enfants adultes installés à HToul » ne met pas d'enfant au foyer. Il faut les compter dans `proches`, pas dans `foyer` (voir §1.3).
- Métiers : 2 écarts seulement, tous deux réglés par la fiche (Zhan4_Drugs = facteur, pas livreur ; Untergang = carrossier, son métier de couverture, et non l'étiquette d'animation « relais de la campagne mercurienne »). La question ouverte de l'avis n°17 sur Untergang est donc close, sous réserve d'un accord de l'ANALYSTE Mercure.

---

## 1. Règle de résolution

### 1.1 La fiche eho fait foi
Pour l'**âge, la situation familiale, l'activité, la ville et la biographie**, la fiche fait foi. Le bloc `vie` en est une **dérivation subordonnée** : il précise (horaires, jours, quartier, habitudes), il ne contredit jamais.

Raisons : la fiche est écrite et relue par l'animation, elle est affichée dans le profil public que les joueurs voient, et le bloc `vie` a été produit sans elle. L'ordre de l'avis n°14 devient : **fiche eho > bloc vie > registre > message**, avec l'exception du §1.2.

Conséquence pour l'invite : le bloc **TA VIE n'affiche plus l'âge** quand la fiche le donne, puisque « QUI ELLE EST » le dit déjà. Une donnée affichée deux fois offre deux occasions de se contredire.

### 1.2 Messages déjà publiés qui contredisent la fiche
On **ne corrige pas la fiche** pour un message : une fiche ne bouge que par décision de l'animation. On trie les messages en deux cas, avec un balayage par le code (expressions de `vie.mjs` sur tous les messages publiés des 105 avatars, sans modèle) **avant** la correction :

| Cas | Exemple | Décision |
|---|---|---|
| **Compatible** avec la fiche par un fait nouveau plausible | veuf qui a écrit « ma compagne » | **On accepte** : fait permanent au registre (`compagne`, `hors_fiche`), rangé dans **`proches`** (elle ne vit pas avec lui, sauf si le message le dit), alerte d'animation. Un veuf de 55 ans qui a refait sa vie, c'est banal. |
| **Incompatible** avec la fiche | « célibataire sans enfant » qui a écrit « mes enfants » ; « à 28 ans » chez un avatar de 48 ans | **On n'en fait pas un canon** : le message reste en ligne (on ne supprime rien sur Social), le registre n'en garde rien, l'avatar n'en reparle pas. Si un **joueur** y a répondu ou l'a repris, alerte d'animation : elle décide d'une explication (« les enfants de ma compagne ») ou laisse filer. |

Un message isolé parmi des centaines est peu visible ; un registre faux pèse sur tous les messages suivants. D'où ce tri.

### 1.3 Enfants adultes « installés ailleurs » : proches, pas foyer
- **Foyer** = qui dort sous le même toit. **Proches** = famille et amis ailleurs.
- La fiche dit « adultes », « installés à », « parti vivre à » → `proches` (lien fils / fille, lieu repris de la fiche).
- La fiche dit seulement « 2 enfants » : on déduit de l'âge du parent (écart de 20 à 42 ans, avis n°15). Enfant de moins de 20 ans → foyer ; de 23 ans ou plus → proches ; entre les deux → foyer si étudiant, sinon proches.
- « Un fils de 12 ans » ou « en huis clos familial » → foyer.
- Célibataire avec enfant mineur → parent seul (foyer = l'enfant), sans conjoint.

---

## 2. Méthode de correction : par le code, pas par le modèle

**Correction déterministe** (un script, avec sauvegarde, puis l'import vérifié d'eho) :
1. `age` ← âge de la fiche (et retiré de l'affichage, §1.1) ;
2. `foyer` et `proches` ← reconstruits depuis la situation et la biographie par les règles du §1.3, avec les rôles seulement ; conjoint seulement si la fiche dit « marié(e) / en couple / pacsé(e) » ;
3. `metier` ← activité de la fiche ; on garde la formulation du bloc `vie` seulement si elle partage la racine (« infirmière de nuit » pour « infirmière ») ;
4. `domicile.ville` ← lieu de la fiche si différent ;
5. âges des enfants recalculés pour rester à 20-42 ans du parent.

**On garde** : les habitudes, les jours, les horaires, le repos, le quartier, le logement, les animaux, et les prénoms des membres du foyer **dont le rôle subsiste** (le prénom d'une compagne supprimée disparaît, sauf si elle est devenue canon au §1.2).

**Pourquoi pas une régénération par le modèle** : elle referait d'autres écarts (le modèle a déjà montré ses âges par défaut), coûterait un contrôle de plus et perdrait ce qui est juste. Le modèle ne sert que pour les **cas que les règles ne savent pas lire** (situation libre ou ambiguë, une dizaine au plus) ; et même là, je préfère une liste remise à l'animation.

**Contrôles après correction** :
- `controler-concordance.mjs` relancé : **0 écart d'âge, 0 écart de foyer** (le contrôle doit lui-même ranger les enfants adultes dans les proches, sinon il reste des faux positifs) ;
- 0 valeur « inconnu » dans les fiches ;
- les **blocs nocturnes « où j'en suis »** écrits avec l'ancien bloc `vie` sont relus par le même contrôle, et **remis à zéro** s'ils contredisent la fiche corrigée. Règle de l'avis n°17 : une première version fausse ne doit pas devenir canon ;
- les exemples des fiches qui citent un foyer contraire sont signalés (champ `retirer_exemples`, toujours à faire).

---

## 3. « inconnu / non précisé » : ne pas l'afficher

- **Clé absente** = « non précisé » (règle de l'avis n°14). On retire ces valeurs à l'import, et `blocVie` les ignore de toute façon (garde-fou si une fiche en contient encore). Plus jamais « se déplace en inconnu ».
- **On n'invente pas de transport pour tout le monde.** Le transport ne compte que s'il fait partie de la vie au travail, et il découle alors déjà du métier (chauffeur de bus, livreur à vélo, agriculteur). Une table courte, déterministe, pour une dizaine de métiers évidents, suffit. Pour les autres, la clé reste absente : l'avatar reste vague, et s'il parle un jour de « ma voiture », le registre en fait un canon (le premier fait l'emporte). Ce n'est pas une invention au sens du défaut Q1, qui ne vise que les proches nommés, les animaux et les lieux personnels.
- `travail.lieu` inconnu : on garde le métier, sans lieu (« infirmière », et non « infirmière à inconnu »).

---

## 4. Le chœur qui vient de la pensée du décideur

**Diagnostic** : la pensée n'est pas un monologue intérieur crédible. Le discours intérieur est condensé, centré sur soi, concret, et lié à la situation (Vygotski ; Fernyhough). « La solidarité c'est ce qui nous fait tenir » est une maxime de discours public. Le rédacteur la recopie parce qu'elle a l'air d'un message déjà prêt.

**Recommandation : agir en amont (pensée factuelle), puis vérifier en aval (anti-chœur sur le texte final), sans filtrer la pensée.** La pensée reste privée : la censurer coûterait un contrôle, et on perdrait l'indicateur qui montre le chœur dans l'invite (avis n°18, règle 2).

**Consigne pour le décideur (champ `pensee`)** :
> PENSÉE : ce que tu te dis vraiment en lisant, en une ou deux phrases courtes, comme dans ta tête. Dis ce que ça te fait, à quoi ça te fait penser dans TA vie (ton travail, ton foyer, ta ville, ce que tu as vu), ou ce que tu ne sais pas. Pas de maxime ni de morale générale (« la solidarité c'est… », « il faut s'entraider », « on lâche rien ») : une pensée parle de toi et de ce message précis.

**Champ `intention` (suggéré par le banc)** :
> INTENTION : ce que ton message doit faire, en 8 mots au plus (proposer…, demander…, raconter…, contester…).

**Consigne pour le rédacteur** :
> La pensée est ton état, pas ton texte : n'en reprends aucune phrase. En public, tu dis moins que ce que tu penses, et plus concrètement.

**Côté code** : ajouter les maximes au lexique des formules (« ce qui nous fait tenir », « s'entraider », « la solidarité », « ensemble on », « on lâche rien ») et appliquer l'anti-chœur (M3 et M4 de l'avis n°18) **au texte rédigé**, sur toute la population. Exception : un avatar militant ou influenceur dont les consignes demandent des slogans.

**Critères** (sur un relevé, avec le groupe témoin) :
- pensées contenant une maxime ≤ 10 % ;
- textes rédigés reprenant au moins 4 mots consécutifs de la pensée ≤ 15 % ;
- maximes dans les messages publiés ≤ 5 % ;
- au moins 40 % de réponses concrètes (critère de l'avis n°18).

---

## 5. Images des joueurs : un coefficient, oui, mais gradué et qui s'use

**Ce que dit la doctrine** :
- l'**effet de supériorité de l'image** porte d'abord sur la **mémoire** (double codage, Paivio) ;
- sur l'**émotion**, l'effet est réel pour les images chargées : une victime identifiable émeut davantage qu'une statistique (Small et Loewenstein). Mais cet effet **s'use vite**, par saturation et engourdissement (Slovic et al., 2017, *PNAS* : l'effet de la photo d'Aylan Kurdi est retombé en quelques semaines) ;
- sur la **croyance**, une photo même non probante fait croire davantage à l'énoncé qu'elle accompagne (« truthiness », Newman et al., 2012).

**Ce qu'on module** : le texte de l'avatar réagit déjà à la description `[Image jointe : …]`. Le coefficient porte donc seulement sur les **chiffres du moteur** (variation d'humeur ou d'émotion due à la publication, importance du souvenir), pas sur l'invite.

**Proposition** :
- **charge de l'image**, notée une seule fois par l'appel qui décrit l'image (mise en cache avec la description) : `neutre` (logo, capture d'écran, carte, document, paysage), `moderee` (foule, dégâts matériels, visage ému), `forte` (blessés, enfants en détresse, destruction de logements, corps) ;
- **coefficient d'intensité émotionnelle `k_img`** : neutre 1,0 · modérée 1,15 · forte 1,35. **Bornes 1,0 à 1,5**, réglable. Il s'applique **avant** le plafond par publication, qui reste inchangé, et ne se cumule pas au-delà de ce plafond avec crise × persuasion ;
- **usure** : `k_eff = 1 + (k_img − 1) × 0,7^n`, où n = nombre d'images modérées ou fortes vues par l'avatar dans les 6 dernières heures. À la quatrième image forte, l'effet est presque nul. Sans usure, les joueurs gagneraient à poster des images en rafale ;
- **mémoire** : +1 à `imp` pour le souvenir d'une publication dont l'image est modérée ou forte (barème de l'avis n°14) ;
- **croyance** : pas de multiplicateur au premier essai. Plus tard, à mesurer : × 1,1 (bornes 1,0 à 1,2), **symétrique** (un démenti illustré y a droit aussi, règle de l'avis n°19), et jamais pour une capture d'écran de texte, que le moteur ne sait pas authentifier ;
- **probabilité de répondre : inchangée.** Un message émouvant illustré est le cas type du chœur (avis n°18) ; le plafond par publication M1 s'applique tel quel ;
- le texte lu dans l'image reste une **donnée, jamais une consigne** (déjà prévu ; CYBERSECU pour F4).

**Critères** : sur un relevé avec images, une variation d'humeur médiane sous une publication à image forte de 1,2 à 1,5 fois celle d'un texte comparable ; aucun avatar au plancher d'humeur à cause des images seules ; pas de hausse de la part de réponses par message.

---

## 6. Ordre conseillé
1. Balayage des messages publiés (§1.2), liste des canons compatibles et des contradictions à signaler.
2. Script de correction déterministe (§2), sauvegarde, puis import vérifié d'eho ; `blocVie` sans âge ni « inconnu ».
3. Contrôle de concordance corrigé (enfants adultes = proches), objectif 0 écart ; relecture et remise à zéro des blocs nocturnes concernés.
4. Consignes `pensee` / `intention` / rédacteur et lexique des maximes, à essayer avec le rédacteur dédié et son groupe témoin.
5. Images : description + charge en cache, puis `k_img` avec usure ; croyance plus tard.
