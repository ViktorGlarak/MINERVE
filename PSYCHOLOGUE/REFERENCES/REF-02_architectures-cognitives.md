# REF-02 — Les architectures cognitives (structurer l'esprit d'un agent)

- **Source** : Wikipédia (en), *Cognitive architecture* — https://en.wikipedia.org/wiki/Cognitive_architecture (lue le 2026-10-10, fournie par l'utilisateur).
- ⚠ La page est **sommaire** sur les émotions et le social. Les compléments marqués *[connaissance de l'agent]* viennent de la littérature générale et sont **à sourcer** avant d'être cités comme références.

## Ce que dit la page
- Une **architecture cognitive** est « une hypothèse sur les **structures fixes** qui fournissent un esprit, naturel ou artificiel, et sur la façon dont elles **travaillent ensemble** » pour produire un comportement intelligent — à la fois une théorie de l'esprit et une implémentation logicielle.
- Histoire : EPAM (Herbert Simon, 1960) ; *The Architecture of Cognition* (John R. Anderson, 1983) ; Allen Newell (1990) lance les théories unifiées implémentées en logiciel.
- Trois axes de classement : **symbolique** (règles) / **connexionniste** (réseaux de neurones) / **hybride** ; centralisée / distribuée ; holistique / modulaire. Deux philosophies : intelligence programmée « par le haut » contre comportement qui **émerge** de règles simples « par le bas ».
- **Exemples notables listés** : 4CAPS ; 4D-RCS (NIST) ; **ACT-R** (Anderson, Carnegie Mellon) ; Extended Artificial Memory ; **ASMO** (les comportements **se disputent** les ressources de l'agent) ; CHREST ; **CLARION** (hybride, Ron Sun) ; CMAC ; Copycat (Hofstadter) ; **DAYDREAMER** (Erik Mueller) ; DUAL ; FORR ; Framsticks ; DeepMind (apprentissage de jeux) ; mémoire associative holographique ; mémoire temporelle hiérarchique (Numenta) ; **CoJACK** (ACT-R dans des agents multi-agents) ; **IDA / LIDA** (théorie de l'**espace de travail global**, Stan Franklin) ; MANIC ; PRS (raisonnement procédural) ; **Psi-Theory** (Dietrich Dörner) ; **Spaun** (2,5 millions de neurones impulsionnels) ; **Soar** (Newell, Laird) ; **Society of Mind** et **The Emotion Machine** (Marvin Minsky) ; mémoire distribuée clairsemée ; architectures de subsomption (Rodney Brooks).

## Compléments utiles au projet *[connaissance de l'agent, à sourcer]*
- **Psi-Theory / MicroPsi** (Dörner, Bach) : l'agent est mû par des **besoins** (existence, **affiliation**, **certitude**, **compétence**) ; les **émotions** émergent de la façon dont ces besoins sont satisfaits ou menacés et **modulent** la perception et l'action (seuil d'attention, résolution, activation). → modèle très proche de ce qu'il faut à un avatar social.
- **CLARION** : sous-système **motivationnel** (pulsions) et méta-cognitif, apprentissage implicite / explicite.
- **Soar** (extensions) : émotions par **évaluation cognitive** (« appraisal ») d'un événement : nouveauté, pertinence pour les buts, contrôle, conformité aux normes.
- **LIDA** : à chaque « cycle », des coalitions de contenus **se disputent l'accès à la conscience** (espace de travail global) ; seul le contenu gagnant est diffusé et sert à agir. → modèle naturel de l'**attention** : un avatar ne « voit » vraiment qu'une partie de son fil.
- **ACT-R** : mémoire déclarative à **activation** qui décroît avec le temps et remonte avec l'usage (loi de puissance de l'oubli) ; production de règles. → modèle de l'**oubli** et du rappel.
- **DAYDREAMER** : l'agent rejoue et imagine des scénarios, avec émotions associées.

## Application au projet *[transposition de PSYCHOLOGUE]*
L'« esprit » d'un avatar se structure comme une petite architecture cognitive, module par module :

| Module (littérature) | Dans nos avatars | État dans le prototype |
|---|---|---|
| Perception | le fil qu'il voit (abonnements, tendances) | publications d'essai fournies |
| Attention / espace de travail global (LIDA) | ce qui retient son attention : intérêt du thème, lien avec l'auteur, émotion | partiel (lien + thèmes dans l'invite) |
| Mémoire de travail | le contexte de la décision | l'invite |
| Mémoire épisodique | ses souvenirs d'échanges | ✅ `memoire/<avatar>.json` |
| Mémoire sémantique | ce qu'il « sait » du monde : base de son camp | ⏳ étape 3 (bases de camp) |
| Mémoire procédurale | ses habitudes : heures, ton, fréquence | ⏳ (rythme de vie) |
| Besoins / motivation (Psi) | affiliation, certitude, compétence, sécurité | ⏳ à ajouter |
| Émotions (appraisal) | ressenti après chaque lecture | ✅ ressenti + intensité |
| Apprentissage | évolution des relations et des opinions | ✅ relations ; ⏳ opinions (étape 4) |
| Oubli (ACT-R) | les liens s'estompent | ✅ selon rancune et gravité |

→ Principe directeur : **le modèle de langage fait office de « cortex »** (interpréter, formuler), **le code tient les structures fixes** (mémoires, besoins, relations, règles d'évolution) — c'est la logique hybride recommandée par les architectures cognitives, et elle garantit la **traçabilité** des bascules pour l'animation.
