# Avis DESIGNER n°93 — eho, fiche d'un avatar : relecture de conformité des lots L1 à L3 (avis n°91)

- **Date** : 2026-10-10
- **Matière** : captures de la fiche d'Isabella Orchkova vue par un animateur GREYCELL (gc10), à 1440 px (pleine page), à 390 px, et un gros plan sur la section « Affiché ». Code lu **sans rien modifier** : `eho\src\app\(admin)\users\[id]\page.tsx` et `api\users\[id]\reel\route.ts`. Réponses de l'utilisateur aux 11 questions (`PLEIADE\PROJET_AVATARS_IA.md`).
- **Hors champ (lots suivants, connus)** : lieu affiché, langue de publication, source de la fiche, localisation réelle, section IA.
- **Statut** : relecture. DESIGNER contribue, il ne tranche pas. Mise en œuvre : PLEIADE.

## 1. Ce qui est conforme

- **Ordre et titres** : réel → personnage → affiché → IA → rangement → technique (Q1 validée). Chaque section porte un filet de couleur, un glyphe et une étiquette « qui voit » (règle 10 : la couleur n'est jamais seule). Rouge et bleu restent réservés au camp.
- **En-tête** : e-mail et UUID retirés, @ copiable, camp **lu** dans les groupes (le code gère aussi « sans camp » et « 2 camps — à corriger »), « IA : non activée », **bandeau des trois couches** avec ancres, **Enregistrer seul**, état « n modifications non enregistrées / Enregistré à », alerte si l'on quitte la page sans enregistrer, en-tête collant.
- **Réel** : en lecture seule, cellules avec leur raison (« GREYCELL — par PACK GREYCELL »), titulaire, usage relevé **à la demande**, état « à venir » écrit en clair. La route renvoie un refus aux joueurs, et la couche est visible de toute l'animation (Q8).
- **Personnage** : libellés renommés (« Pays d'appartenance (fiction) » avec son aide, « Catégorie (trombinoscope) », « Registre et ton », « Compétences et diplômes »), trois sous-blocs, champs vides repliés, étiquette « EN » automatique.
- **Affiché** : portrait, bannière, nom et @ regroupés, aide « le changer casse les scénarios », compteur 0/500, **aperçu du profil**. L'aperçu ne puise rien dans le personnage (« Pas de description. »).
- **IA** : état vide rédigé, pas de formulaire mort (règle 18).
- **Rangement** : seulement les groupes dont l'avatar est membre, rangés par famille ; allégeance en choix unique ; 🔒 et raison affichés **avant** le refus du serveur ; × pour retirer ; recherche pour ajouter.
- **Technique** : repliée ; « Supprimer » en texte rouge, plus en aplat.

## 2. Écarts

| # | Écart | Gravité (0-4) |
|---|---|---|
| E1 | Le sélecteur de fichier natif s'affiche **en anglais** (« Choose File / No file chosen ») et se tronque à 1440 px (« No fil…osen », « N… »). C'est le premier contrôle de la section que voient les joueurs. | 2 |
| E2 | **Au téléphone** : il n'y a pas de sommaire (il est masqué sous 1024 px, alors que l'avis prévoyait une barre défilante), et l'en-tête collant, avec son bandeau sur trois lignes, occupe environ un tiers de l'écran sur une page de près de 4 000 px de haut. | 2 |
| E3 | « Catégorie (trombinoscope) » est restée en **texte libre**. Une faute de frappe sort l'avatar de son bloc du trombinoscope. | 2 |
| E4 | Section Personnage : la phrase « se change dans Rangement » est vraie pour l'Administration, pas pour un animateur, qui trouvera l'allégeance verrouillée 🔒. | 1 |
| E5 | La biographie interne tient dans 5 lignes avec un défilement interne : le texte est coupé à 1440 px et presque illisible à 390 px. C'est pourtant ce qu'il faudra relire pendant la traduction en français (Q6). | 1 |
| — | Écarts non retenus avant la mise en ligne : pas de « Voir sur le réseau ↗ » ni de menu « ⋯ » (1) ; la liste Certification est trop large par rapport aux autres champs (1) ; le bouton Enregistrer désactivé est peu contrasté (1, toléré car l'état est aussi écrit) ; le segment « Affiché » du bandeau répète le nom tant que le lieu affiché n'existe pas (attendu, lot 4). | 1 |

## 3. Corrections proposées avant mise en ligne (petites, sans schéma)

1. **Sélecteur de fichier en français** (E1) : masquer l'`<input type="file">` derrière un bouton « Choisir une image… », suivi du nom du fichier ou de « aucun fichier ». L'input reste dans le DOM, relié à son libellé et accessible au clavier.
2. **Téléphone** (E2) : sous `md`, ne garder collante que la ligne « nom + Enregistrer », et laisser le bandeau des trois couches défiler avec la page. Ajouter un sommaire horizontal défilant (les six ancres, comme à 1440 px) juste sous l'en-tête.
3. **Catégorie en liste fermée** (E3) : proposer une liste des catégories du trombinoscope (`lib/trombinoscope.ts`). Une valeur hors liste déjà enregistrée reste affichée avec la mention « hors liste ».
4. **Formulation selon les droits** (E4) : quand l'allégeance est verrouillée, écrire « se change dans Rangement (Administration seulement) 🔒 ».
5. **Biographie interne à hauteur automatique** (E5) : la zone grandit avec le texte, entre 5 et environ 15 lignes, puis défile.

Contrôle avant push (règle du poste) : refaire les captures à 1440 et 390 px. Pas de capture en sombre, puisqu'eho n'a pas d'habillage sombre.

**Sources** : avis n°91 ; règles 5, 10, 18, 25, 30 de la mémoire DESIGNER ; Nielsen 4 et 5 (REF-14) ; REF-21 et REF-22 (navigation sur petit écran).
