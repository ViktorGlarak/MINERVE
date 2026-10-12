# Lexique de la zone — un mot par notion (avis DESIGNER n°69, R2)

> **Pourquoi** : l'inventaire du 2026-10-06 a trouvé le même objet sous quatre noms et le même mot pour quatre objets. Un animateur qui change d'app doit réapprendre le vocabulaire — c'est l'une des causes de « on est perdus ». Règle 36 (DESIGNER §3.7) : une notion = un mot, partout.
> **Statut** : ✅ = appliqué dans le code le 2026-10-06 · 🟡 = proposé, à arbitrer par l'utilisateur · ⛔ = volontairement laissé tel quel (et pourquoi).

## 1. Les notions et leur mot

| Notion | Mot retenu | Où on le lisait autrement | Statut |
|---|---|---|---|
| Ce que l'Admin programme et publie (tweet, article, message) | **publication** | Admin : « item » (Item #5, Nouvel item, Supprimer l'item…) | ✅ Admin renommé (fenêtre, confirmations, arbre, réglages) |
| Ce que JEMM / MELMIL planifie (un événement du scénario, avec son heure et son moyen) | **incident** | MELMIL : « inject » dans le titre de l'app (« Planche des injects ») | 🟡 garder « incident » à l'écran ; « inject » reste le mot JEMM, cité seulement dans les imports / exports |
| Un message du réseau social | **post** (fil, profil) — « tweet » seulement dans l'habillage Twitter | Admin « Cite le tweet » | ⛔ les habillages imitent de vrais réseaux (Jakob) : chacun garde ses mots |
| Les réglages d'une app ou d'un objet | **Réglages** | Admin : onglet « Configuration » ; LEAC : « Paramétrage », « Affichage » ; MELMIL : deux « Réglages » différents | ✅ Admin → « Réglages » ; ✅ MELMIL : « Réglages » (atelier) et « Réglages de la planche JEMM » ; 🟡 LEAC (« Paramétrage » d'un contrôle = réglages ; « Affichage » = préférences de l'appareil — à décider) |
| L'historique des actions | **Journal** | messagerie « Journal du scénario » ; admin panneau « Journal récent » | ✅ cohérent (le complément précise l'objet) |
| Le suivi en direct des publications de toute la zone (Admin) | 🟡 **Journal de la zone** | Admin : onglet « Supervision » | 🟡 à arbitrer : « Supervision » désigne aussi la modération de la messagerie et un rôle |
| La modération de la messagerie (voir tout, corriger) | **Supervision** (= nom du rôle au bouclier) | message de refus « Modération » / « Administration » | ✅ refus corrigé |
| La grille des avatars (eho) | 🟡 **Trombinoscope** | menu « Avatars », vue « Planche », route `/trombinoscope` | 🟡 à arbitrer ; aujourd'hui « Avatars » |
| Le graphe des relations entre avatars (eho) | **Planche officielle** / **Planches relationnelles** (joueurs) | titres de page « Planche relationnelle officielle », « Planches relationnelles des joueurs » | ✅ titres alignés sur le menu |
| La grille calendaire de MELMIL | **Planche de préparation** / **Planche JEMM** | — | ✅ inchangé |
| Agir sous l'identité d'un avatar | **Au nom de** | social « In the name of », presse « Publié au nom de », messagerie « Écrire au nom de » | ✅ social traduit ; les deux autres sont des compléments corrects |
| Le rôle qui anime l'exercice | **Animation** (catalogue) ; à l'écran : « Animateur » | eho « Animateurs », admin « Conduite d'exercice », MELMIL « GA1 / GA2 », messagerie « Animation » | 🟡 les libellés du catalogue sont dans `pleiade-platform` (Xavier) : proposer **Animation** partout sauf MELMIL (GA1/GA2 = deux groupes, nommés GREYCELL/FORAD à l'écran) |
| Le rôle qui administre | **Administration** | MELMIL « Admin », presse « Direction » | ⛔ presse : « Direction » est le mot du métier (rédaction) ; 🟡 MELMIL « Admin » → « Administration » (catalogue, Xavier) |
| Replier / déplier tout | **Tout déplier · Tout replier** (dans cet ordre) | MELMIL Déroulé et Admin Arbre dans l'ordre inverse | ✅ |
| Les mots anglais du cockpit | **Disposition, Réinitialiser, Exporter (JSON), Nom d'utilisateur** | Layout, Reset, Export JSON, Username | ✅ |
| Le groupe d'animation affiché (MELMIL) | **Groupes** | « Afficher » sous les onglets, « Groupes » sur la planche | ✅ |
| Les onglets de la médiathèque, des réglages… | — | presse Réglages › « Rédaction » (même nom que l'espace) | 🟡 proposer « Journalistes » |

## 2. Les mots des statuts (inchangés, mais à connaître)
- **Scénario** : Brouillon · **Lancé** · **Pause** · Terminé *(décision du 2026-10-07, avis DESIGNER n°76 ; ex-« En lecture », « En pause »)*.
- **Publication** : Brouillon · **Programmée** (attend son heure dans un scénario lancé) · Publiée · **Non partie** · Prise en compte *(décision du 2026-10-07, avis n°77 ; ex-« Erreur »)*. « publication » est **féminin** partout (« 35 / 35 publiées »).
- **Journal de l'animation** : Publiée · Non partie · Action · Cycle · Ignorée — **jamais** publish, error, tick, skip, item.
- **Nom de l'app d'animation à l'écran** : **Animation** (jamais « ADMIN »).
- **Chiffres** : sans zéro ajouté (« 0 », « 14 », pas « 00 »).
- **Casse** : CAPITALES espacées seulement pour les sur-titres de panneau et les en-têtes de colonnes ; boutons, filtres et étiquettes en casse normale.
- **Article** : Brouillon · Programmé · Publié · Archivé.
- **Incident (MELMIL)** : En préparation · En validation · Validé · Dans JEMM.
- **Demande de produit** : Envoyée · Prise en charge · Livrée (avis attendu) · Approuvée (close) · Refusée.

## 3. À arbitrer (réponse attendue de l'utilisateur)
1. Admin, onglet **« Supervision »** → **« Journal de la zone »** ?
2. eho, menu **« Avatars »** → **« Trombinoscope »** ?
3. Presse, onglet de réglages **« Rédaction »** → **« Journalistes »** ?
4. Catalogue Pléiade (à demander à Xavier) : rôles **« Animation »** (eho, admin) et **« Administration »** (MELMIL) ?
5. LEAC : **« Paramétrage »** → **« Réglages »** ?
