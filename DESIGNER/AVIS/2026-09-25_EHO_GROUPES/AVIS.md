# Avis DESIGNER n°6 — eho, onglet « Groupes » : voir les membres d'un groupe

> **Date** : 2026-09-25 · **Demande** : cliquer sur un groupe et voir la liste de ses avatars — le **nom de compte du réseau social** (@) et le **nom / prénom** — sans la fiche complète. Beau, fluide, responsive. Mise en ligne directe.

## Solution retenue

**R1 · Toute la ligne du groupe s'ouvre** (nom, effectif, chevron `›`). Le menu « ⋯ » (Modifier, Camps, Supprimer) reste à part, à droite, pour ne pas ouvrir la liste par erreur *(Fitts : une grande cible pour l'action fréquente)*.

**R2 · La liste s'ouvre dans la fenêtre commune d'eho** (même mécanique que les fiches : `Échap`, focus piégé, retour au groupe cliqué). Sur téléphone, elle occupe presque tout l'écran *(Jakob : un seul geste appris pour toutes les fenêtres d'eho)*.

**R3 · En-tête** : la pastille de la famille (couleur du pays), le nom du groupe en casse normale, l'effectif. Juste dessous, une **recherche instantanée** sur le @ et le nom *(Hick : dans un groupe de 167 membres, on cherche plutôt qu'on ne lit)*.

**R4 · Une ligne par membre, lisible d'un coup d'œil** :
- portrait rond de 32 px, ou initiales ;
- **Prénom Nom** en gras, **@compte** en chasse fixe, atténué ;
- badge « Inactif » seulement pour l'exception ;
- un lien discret « Fiche › » pour qui veut aller plus loin.

Les membres sont triés par nom *(REF-07 : la hiérarchie par le poids et la couleur, pas par des étiquettes)*.

**R5 · « Copier les @ »** met la liste des comptes du groupe dans le presse-papiers. C'est utile pour préparer une publication ou un scénario sur le réseau social *(Tesler : l'application fait le travail répétitif)*. La confirmation « 167 comptes copiés » s'affiche 2 s.

**R6 · Fluidité** : chargement à l'ouverture, avec des lignes squelettes pour éviter un écran vide *(Doherty)*. Les lignes hors écran ne sont pas dessinées (`content-visibility: auto`) : un groupe de 700 membres défile sans à-coup.

## Sécurité (relevé en préparant)

La route `GET /api/groups/[id]/members` était ouverte à **toute session**, joueurs compris. Or un nom de groupe (« ARN - MILITAIRE ») révèle ce qu'un joueur doit trouver.
→ Elle est désormais réservée à l'animation, et à la clé de service qu'utilise `app-admin`.
