# Avis DESIGNER n°94 — Social : programmer une publication sans ambiguïté

**Date** : 2026-10-10 · **Demande** : « quand on clique sur l'icône "programmé" on ne sait pas vraiment si en cliquant sur "publier" le post sera "programmé" ou "publié » ; quitte à ajouter un bouton « valider ».
**Lu sans rien modifier** : `app-social\apps\web\src\app\components\compose\compose.ts` (l. 229-244, 293-300, 949-978), `sidebar.ts` (entrée « Programmés »), `pages\scheduled\scheduled.ts`.
**Statut** : proposition argumentée. Le bug serveur (post publié tout de suite) est traité à part par PLEIADE.

## Constat (gravité 3 sur 4, Nielsen 1 « état du système visible »)

1. **Aucune validation** : le calendrier en ligne est lié directement à `scheduledAt`. Un simple clic sur un jour programme déjà, souvent à une heure non choisie (minuit ou l'heure courante).
2. **Fermer ne dit rien** : un clic sur le fond ferme la fenêtre et garde la date. On ne sait pas si on vient de confirmer ou d'abandonner. `Échap` n'est pas géré.
3. **Le seul signal après coup** est une horloge colorée (couleur seule, règle 10) avec une infobulle au survol. Le bouton reste « Publier » avec l'icône d'envoi : il annonce le contraire de ce qui va se passer.
4. `minScheduleDate = new Date()` est calculé à l'ouverture du composant : au bout d'une heure de rédaction, on peut choisir une heure déjà passée.
5. Les dates sont formatées dans le fuseau du navigateur (`toLocaleString('fr-FR')`), sans le nommer.

## Recommandations (modèle X pour tous les habillages, règle 15 Jakob)

X fonctionne ainsi : une fenêtre « Programmer » avec un bouton « Confirmer », puis le bouton principal devient « Programmer » et un bandeau « Sera envoyé le … » s'affiche. Mastodon accepte la programmation dans son API (au moins 5 min à l'avance), mais son interface web officielle ne la propose pas. On reprend donc le geste de X partout et on ne change que les couleurs selon l'habillage.

### R1. La fenêtre « Programmer la publication »
- **Champs** : *Date* (jj/mm/aaaa) et *Heure* (hh:mm, format 24 h, pas de 5 min), sur deux champs nommés. Le calendrier ne sert qu'à choisir la date. Sous les champs, une ligne en clair qui se met à jour : « **Sera publié le samedi 10 octobre à 14 h 30 (heure de Paris)** ».
- **Valeur proposée à l'ouverture** : le prochain quart d'heure qui tombe au moins 5 min plus tard (règle 19, Tesler). Si une date est déjà programmée, on l'affiche.
- **Raccourcis** (facultatif, utiles sous pression) : « +15 min », « +1 h », « Demain 08 h 00 ».
- **Boutons** : **« Confirmer »** (action principale, règle 6) et « Annuler ». Si une date est déjà fixée, on ajoute à gauche le lien discret « Retirer la programmation ».
- **Fermeture** : un clic à l'extérieur ou `Échap` ferme la fenêtre **sans rien changer**, comme « Annuler » (règle maison). Le focus revient sur l'horloge (règle 11). **Seul « Confirmer » enregistre.**
- **Valeurs refusées**, avec un message sous le champ et « Confirmer » désactivé (règle 24) :
  - date passée : « Cette heure est déjà passée. » ;
  - **moins de 2 min** à l'avance : « Choisissez au moins 2 minutes plus tard, ou publiez maintenant. » Deux minutes suffisent au rythme d'un exercice ; Mastodon impose 5 min, on peut s'aligner si PLEIADE préfère ;
  - au-delà de la fin de l'exercice, si le système la connaît : simple avertissement, sans blocage.
  - Le minimum se recalcule **à chaque ouverture et à la confirmation**, pas une seule fois au chargement de la page. Le serveur refuse lui aussi une date passée (règle 17, strict en sortie).
- Lien en pied de fenêtre : « Voir les publications programmées » (comme X).

### R2. Après « Confirmer » : un état visible dans la zone de rédaction
- **Bandeau au-dessus du texte** (fond atténué, icône horloge, texte et non couleur seule) : « 🕑 **Sera publié le sam. 10 oct. à 14 h 30** (heure de Paris) · Modifier · ✕ ».
- **Bouton principal** : le libellé « Publier » devient **« Programmer »** et l'icône d'envoi devient une horloge. C'est la correction décisive : le bouton dit ce qu'il va faire (règle 25).
- L'icône horloge de la barre d'outils reste active. Son infobulle et son `aria-label` disent « Programmé le … », et c'est cohérent avec le bandeau.

### R3. Annuler la programmation
- Le **✕ du bandeau** (`aria-label` « Ne plus programmer ») retire la date. Le bouton redevient « Publier » et le texte saisi est conservé.
- « Modifier » ou un clic sur le bandeau rouvre la fenêtre avec la date déjà remplie.
- Dans la fenêtre : « Retirer la programmation ».
- **Aucune boîte de confirmation** : le geste est sans perte et se refait en deux clics.
- Une fois la publication envoyée, on l'annule depuis **Programmés**, avec les boutons Modifier et Supprimer qui existent déjà.

### R4. Après l'envoi
- Notification de succès : « **Programmé pour le samedi 10 octobre à 14 h 30 (heure de Paris)** », avec un lien **« Voir dans Programmés »** qui reprend le libellé exact du menu (règles 30 et 36). Elle reste affichée 6 à 8 s.
- La publication **n'apparaît pas dans le fil**. La zone de rédaction se vide, y compris le bandeau. Facultatif : un compteur sur l'entrée « Programmés » du menu.
- Si l'heure est passée entre la confirmation et l'envoi : « L'heure choisie (14 h 30) est passée. **Publier maintenant** / Changer l'heure ». On ne publie jamais en silence.
- Côté animation, le vocabulaire « programmées / en direct » reste celui des écrans de pilotage. Dans le réseau social, on garde « Programmés », libellé du menu existant.

### R5. Fuseau horaire
- Tout s'affiche en **heure de Paris** (`Intl.DateTimeFormat('fr-FR', { timeZone: 'Europe/Paris' })`), quel que soit le réglage du poste. La mention « (heure de Paris) » est visible dans la fenêtre, le bandeau et la notification.
- Elle évite l'ambiguïté entre l'heure d'été et l'heure d'hiver, ainsi que les postes réglés en UTC. Le stockage reste en ISO UTC.
- **Question à l'utilisateur** : l'heure de programmation est-elle l'heure réelle ou une heure d'exercice décalée (D+, heure JEMM) ? Si c'est une heure d'exercice, il faut l'afficher à côté de l'heure réelle et non à sa place.

## Effort estimé
Faible à moyen, entièrement dans `compose.ts` : un état « brouillon de date » séparé de la date confirmée, le bandeau, le libellé et l'icône du bouton, le formatage par fuseau. Il faut aussi un contrôle côté serveur, à vérifier par PLEIADE avec le bug en cours.

Sources : Nielsen 1, 3 et 9 (REF-14) ; Jakob et Tesler (REF-06) ; règles 6, 10, 11, 17, 19, 24, 25, 30 et 36 (`MEMOIRE.md` §3) ; règle maison sur la fermeture par clic extérieur et Échap.
