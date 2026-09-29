# REF-10 — GOV.UK : principes de conception et Design System

- **Sources** : https://www.gov.uk/guidance/government-design-principles · https://design-system.service.gov.uk (composants, modèles de parcours, styles). Pages lues : principes, error summary, spacing, question pages.
- **Ingéré** : 2026-09-24 · **Accès** : libre · **Licence** : code sous MIT, contenus sous OGL. ⚠ La police GDS Transport et la couronne sont **réservées à GOV.UK** : on reprend les **méthodes**, jamais l'identité.
- **Nature** : c'est la référence mondiale des **services publics** simples et accessibles (WCAG 2.2 AA), fondée sur des tests auprès des usagers.

## Les 11 principes de conception du gouvernement britannique
1. **Partir des besoins des usagers**, pas de suppositions.
2. **En faire moins** : se concentrer sur l'essentiel, réutiliser plutôt que refaire.
3. **Concevoir avec des données** : l'usage réel plutôt que l'intuition.
4. **Travailler dur pour que ce soit simple.**
5. **Itérer, puis itérer encore** : sortir tôt, tester, corriger.
6. **C'est pour tout le monde** : inclusif et accessible.
7. **Comprendre le contexte** : où et comment on s'en sert.
8. **Construire des services, pas des sites.**
9. **Être cohérent, pas uniforme.**
10. **Ouvrir le travail** : ça le rend meilleur.
11. **Réduire l'impact environnemental.**

## Règles concrètes du Design System
- **Une seule chose par page** (question pages) : la question sert de titre, un **lien « Retour »** en haut, un bouton **« Continuer »** aligné à gauche.
- **Ne demander que ce qui est nécessaire** ; ne jamais redemander une information déjà connue : la **pré-remplir**.
- **Pas d'astérisque** : on marque les champs **« (facultatif) »**, les autres sont réputés obligatoires.
- **Texte d'aide** : une phrase courte, sans point final, sans lien.
- **Résumé des erreurs** (error summary) : affiché **en haut de la page**, même pour une seule erreur. **Le focus s'y place.** Chaque erreur est un **lien vers le champ fautif**, et son texte est identique au message affiché à côté du champ. Le titre de la page est préfixé par « Erreur : ».
- **Rédaction des erreurs** : dire ce qui se passe **et comment corriger**, sans jargon ni « veuillez ». Exemple : « Saisissez votre nom complet ».
- **Échelle d'espacement** (unités 0 à 9) : 0, 5, 10, 15, 20, 25, 30, 40, 50, 60 px sur grand écran, réduite sur mobile, avec une bascule à 640 px.

## Pour nos projets
- Les **formulaires de l'admin** (item de scénario) et les **réglages de MELMIL** gagneraient au **résumé d'erreurs** et au marquage « (facultatif) ».
- Le principe **« une seule chose par page »** convient au terrain (LEAC sur tablette), moins aux planches denses des animateurs.
