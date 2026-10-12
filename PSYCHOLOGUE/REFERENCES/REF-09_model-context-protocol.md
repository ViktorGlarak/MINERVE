# REF-09 — Model Context Protocol (MCP) : standard de connexion des applications LLM aux outils et aux données

- **Source** : organisation https://github.com/modelcontextprotocol (lue le 2026-10-12, fournie par l'utilisateur) ; spécification sur modelcontextprotocol.io.
- **Gouvernance** : projet ouvert, « *hosted by The Linux Foundation* », SDK officiels co-maintenus avec Microsoft (C#), Google (Go), etc. **SDK** : TypeScript, Python, Java, Kotlin, C#, Go, PHP, Ruby, Rust, Swift. Dépôts principaux : spécification, SDK, `servers` (implémentations de référence, 91 k étoiles), registre communautaire. Licence des SDK : MIT *[connaissance de l'agent, à vérifier dépôt par dépôt]*.

## Ce que fait le projet
- « *An open protocol that enables seamless integration between LLM applications and external data sources and tools.* » Architecture **hôte / client / serveur** en **JSON-RPC** ; transports **stdio** (processus local) et **HTTP streamable**.
- Primitives *[connaissance de l'agent]* : côté serveur **tools** (actions), **resources** (données lisibles), **prompts** (gabarits) ; côté client **sampling** (le serveur demande une génération au modèle de l'hôte), **roots**, **elicitation** (demander une saisie à l'utilisateur).
- Ce n'est **pas** un système de mémoire : c'est la **prise standard** par laquelle Cognee (REF-04), Mem0 (REF-05), Graphiti (REF-06) et Letta (REF-07) exposent leur mémoire aux assistants (tous fournissent un serveur MCP).

## Ce qui est pertinent pour la psychologie des avatars
- **Rien pour le comportement des avatars** : MCP ne dit pas comment se souvenir, oublier, croire ou changer d'avis.
- Une pertinence **d'outillage pour l'agent PSYCHOLOGUE** : les relevés (avis n°9 à n°12) se font aujourd'hui sur des exports et des relevés périodiques ; un serveur MCP **local, en lecture seule** devant la base du moteur (« mémoire de l'avatar X », « journal des variations de X entre t₁ et t₂ », « croyances actives d'une cohorte ») permettrait à l'analyste d'interroger directement « pourquoi Esteban a basculé » pendant un relevé, sans script ad hoc.

## Ce que nous avons déjà d'équivalent (app-ia 2026-10-12.2)
| MCP | Moteur / outillage |
|---|---|
| serveur d'outils / ressources | routes HTTP d'app-ia (relevé périodique toutes les 3 h, route de service des J'aime), `export-analyse.ts`, `archives.ts` |
| interrogation par un assistant | lecture des exports Markdown par l'agent PSYCHOLOGUE (relevés `AVIS\*_RELEVE_*.md`) |

## À récupérer (idées précises)
1. **Éventuellement, plus tard** : un serveur MCP **stdio, local, lecture seule** « app-ia-memoire » (SDK TypeScript, dans le dépôt app-ia) exposant 4 ressources : mémoire d'un avatar · journal des variations (filtre avatar / variable / période) · croyances et faits acquis actifs · relevé du dernier cycle. Usage : analyses PSYCHOLOGUE / DESIGNER pendant les relevés. **Décision PLEIADE** (outillage) et **avis CYBERSECU** obligatoire (accès à la base de zone depuis le poste ; jamais en HTTP exposé ; jamais vers un service cloud).
2. **Ne pas récupérer** : rien côté moteur ; ne pas brancher les serveurs MCP des librairies de mémoire (ils supposent leur service).

## Coût
- Idée 1 : quelques dizaines de lignes TypeScript + le SDK MCP (dépendance npm) ; 0 appel modèle ; **risque** = surface d'accès à la base (à cadrer par CYBERSECU).

## Verdict : **SANS INTÉRÊT POUR LA PSYCHOLOGIE** ; **S'EN INSPIRER PLUS TARD** côté outillage d'analyse (lecture locale de la mémoire des avatars par l'agent PSYCHOLOGUE), sur décision PLEIADE + CYBERSECU
Raison : MCP est une prise, pas une mémoire ; aucune règle de comportement d'avatar n'en dépend. Son seul apport serait de rendre les relevés interrogeables en direct.
