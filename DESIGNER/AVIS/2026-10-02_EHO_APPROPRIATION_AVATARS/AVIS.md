# Avis n°29 — S'approprier un avatar, et voir « qui utilise quoi »

> **Date** : 2026-10-02 · **Demandeur** : l'utilisateur · **Apps** : eho (étape 1), kit IA de l'admin (étape 1), sélecteurs d'avatar du réseau social, de la presse et de la messagerie (étape 2).
> **Statut** : 🟡 proposé, décisions prises, en attente de validation par Xavier (eho et réseau social), pas encore codé.

## Besoin

- Dans un camp (GREYCELL, FORAD, DIV1…), un **compte** (gc05, div1…) veut **s'approprier** un ou plusieurs avatars que son camp peut déjà utiliser. L'appropriation est facultative.
- Les animateurs veulent voir rapidement **quel compte tient quels avatars**.
- Les joueurs auront la fonction, mais l'utiliseront peu : leur groupe leur réserve déjà leurs avatars.

## Décisions de l'utilisateur

- **Bloquer** : seul le titulaire, et les animateurs, peut utiliser un avatar réservé. Les autres comptes du camp doivent le faire libérer.
- **Libérer** : le titulaire libère le sien ; les **animateurs** (rôle admin) libèrent n'importe lequel, et « Tout libérer » en fin d'exercice.
- **Étapes** : eho et kit IA d'abord ; les sélecteurs des apps ensuite.

## Recommandations

1. **R1 — S'approprier là où l'on travaille.** Dans la liste des avatars d'eho :
   - un bouton à bascule « ☆ Me l'approprier » / « ★ À moi » (`aria-pressed`, texte toujours écrit) ;
   - un filtre « Mes avatars » ;
   - à l'étape 2, une section « Mes avatars » **en tête** des sélecteurs des apps (REF-06 Jakob et Hick : ce qu'on utilise le plus vient en premier).
2. **R2 — La réservation se voit partout de la même façon** : l'étiquette « 🔒 Réservé · gc05 », dans la même forme sur toutes les apps. Le cadenas est toujours doublé du texte (REF-07, règle 10). Un avatar réservé par un autre compte apparaît **grisé et non sélectionnable**, avec la raison écrite et la marche à suivre : « Demandez à un animateur de le libérer » (REF-14, heuristiques 5 et 9).
3. **R3 — La vue animateur « Qui utilise quoi »**, dans eho, qui détient les avatars :
   - un tableau **par camp**, une ligne par **compte**, avec les portraits (32 px, initiales s'il n'y a pas d'image) et la date de prise ;
   - une recherche dans les deux sens : un `@avatar` ou un compte ;
   - « Libérer » sur chaque avatar, « Tout libérer » par camp et pour toute la zone, avec une confirmation qui annonce le nombre ;
   - un état vide qui explique comment s'approprier un avatar (REF-06 Peak-End).
4. **R4 — Le kit IA respecte les réservations.**
   - Les avatars réservés par **d'autres** comptes sont **retirés** du kit.
   - Ceux du compte qui génère le kit sont **en tête**, marqués « à moi ».
   - Le résumé avant téléchargement le dit : « 12 avatars réservés par d'autres comptes ont été écartés » (REF-14, heuristique 1).
5. **R5 — Rien d'invisible.** La fiche d'un avatar dans eho indique son titulaire et depuis quand. Une appropriation ou une libération est journalisée (qui, quand).

## Sécurité (CYBERSECU)

- Le lien est **compte de zone ↔ avatar**, jamais **personne réelle ↔ avatar** : c'est compatible avec l'anonymat des comptes (option A).
- Le **blocage est vérifié par le serveur** de chaque app, et pas seulement à l'écran : à l'étape 1 dans le kit IA ; à l'étape 2 dans l'incarnation (social, presse, messagerie).
- Les animateurs passent outre, comme pour les camps : les masteradmin court-circuitent déjà la règle des groupes.

## Ajustement après lecture du code (2026-10-02)

- **R6 — L'écran va dans l'admin, la donnée reste dans eho.**
  - L'admin est réservée à l'animation : les joueurs ne peuvent rien voir, par construction. C'est un rappel de l'utilisateur : savoir qu'un avatar est tenu par l'animation, c'est savoir qu'il est piloté.
  - Les comptes gc y travaillent tous les jours (scénarios, kit IA).
  - Les écrans d'administration d'eho, qui listent les avatars, ne leur sont peut-être pas ouverts.
- **R7 — Prévenir plutôt que refuser.** La recherche dit d'emblée « Hors de votre camp », au lieu d'un bouton qui échoue après le clic (REF-14, heuristique 5).
- Réalisé en local : onglet « Avatars » de l'admin, sélecteur des scénarios, kit IA. Voir `PLEIADE\JOURNAL.md` du 2026-10-02, suite 7.

## Second ajustement : s'approprier depuis eho (demande de l'utilisateur, 2026-10-02)

- **R8 — Le geste dans eho, là où l'on regarde les avatars** (la planche). L'admin garde sa section ; une seule donnée.
- **R9 — Un signe propre : le marque-page.** L'étoile ★ des cartes appartient déjà au package STARTEX : deux sens pour un même signe sèmeraient la confusion (REF-07, cohérence).
- **R10 — Une languette centrée sous la carte**, posée à côté du bouton de la carte et non dedans (un bouton dans un bouton n'est pas valide).
  - Libre : elle apparaît au survol ou au clavier, et reste toujours visible sur écran tactile.
  - « À moi » : pleine. Réservé par un autre : le nom du compte, en pointillé.
  - Hors du camp : rien, on ne propose pas l'impossible.
  - Elle ne masque ni le nom ni le @compte.
- **R11 — Libérer l'avatar d'un autre dans eho : les organisateurs** (masteradmin). eho ne distingue pas un compte gc d'un chef d'animation.

## Troisième ajustement : un seul écran (2026-10-02)

- **R12 — L'onglet « Avatars » de l'admin est retiré.** L'utilisateur confirme que tous les comptes qui préparent des scénarios ont accès à la planche d'eho. Garder deux écrans pour un même geste obligeait à se demander où aller, avec deux règles de libération (REF-06 Jakob, REF-14 heuristique 4 « cohérence »).
- **L'admin garde ce qui sert pendant la préparation**, en lecture : le kit IA, les étiquettes et le blocage dans le sélecteur d'avatar, et le lien « Gérer mes avatars dans eho ↗ ».

## Quatrième ajustement : signaler plutôt que bloquer (décision de l'utilisateur, 2026-10-02)

- **R13 — Le kit IA garde les avatars réservés**, marqués 🔒 avec leur titulaire. La consigne est écrite à l'identique dans les trois documents : l'IA ne les emploie que si la demande les nomme. Une règle invisible, ou un avatar absent, empêcherait de les demander nommément.
- **R14 — « Vérifier » avertit, sans bloquer**, dans un encadré à part, ni rouge (bloquant) ni gris (« à savoir ») : orange, « à vérifier ». Un message par avatar, avec les items concernés et la marche à suivre (REF-14, heuristiques 1 et 9 ; une seule couleur d'alerte, REF-06 Von Restorff).
- **R15 — Le sélecteur confirme sur place** avant d'employer l'avatar d'un autre compte, sans fenêtre modale.
