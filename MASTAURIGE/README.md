# MASTAURIGE — Agent contenus RS fictifs exercices AURIGE

## Rôle
MASTAURIGE est l'agent spécialisé dans la génération de contenus réseaux sociaux fictifs pour les **exercices de type AURIGE** — entraînement et contrôle des Postes de commandement de niveau brigade.

Il génère des tweets et posts en incarnant les avatars CASW (Cellule d'Action sur les réseaux Sociaux en Wartime), selon leurs profils, camps narratifs et styles d'écriture. Les contenus sont distribués en HTML statique (ZIP offline), sans passer par la plateforme Mastorion.

> **Note importante :** MASTAURIGE est INDÉPENDANT de Mastorion. Mastorion est une plateforme fictive dédiée à ORION 26, qui disposera à l'avenir de son propre système IA distinct. MASTAURIGE ne gère pas Mastorion.

## Modèle
`mistral-nemo:latest` — partagé avec MASTODONTE, SCÉNARISTE, SECRÉTAIRE, VOIX

## Distinction avec MASTODONTE
| Agent | Rôle |
|---|---|
| MASTODONTE | Expert technique Mastodon/Mastorion : API, OAuth, endpoints, structure Status, fédération |
| MASTAURIGE | Expert contenu exercice AURIGE : avatars CASW, tweets, tableaux MASSTALK V3, HTML tweet cards |

## Exercices couverts
- **AURIGE 2BB** — Zone Lorraine (Sarrebourg, Héming, Nancy), distribution HTML/ZIP
- **Exercices AURIGE futurs** — tout exercice de type brigade PC (format identique)

## Sources de contexte obligatoires
Toujours fournir à MASTAURIGE au moment de l'appel :
1. `CASW/agents_rules_orion26.md` — règles format tableau, hashtags, barème viralité
2. `CASW/avatars_casw_orion26.md` — base 222 avatars (identité, compte Mastodon, style)
3. Le contexte scénario du jour (thème, zone géo, événement à animer)

## Outputs produits
1. **Tableau MASSTALK V3** : `| id | account_id | compte | message | nb_likes | nb_retweets | reply_to | delta |`
2. **Blocs HTML tweet card** : prêts à coller dans `WEB/index.html` (section `data-category="social"`)

## Chemin prompt système
`D:\CECPC\PRODUCTION\IA\Mercure\SYSTEME\PROMPTS\mastaurige.md`

## Chemins ressources exercices
| Ressource | Chemin |
|---|---|
| Base avatars CASW | `D:\CECPC\PRODUCTION\IA\Mercure\MASTAURIGE\CASW\avatars_casw_orion26.md` |
| Règles AGENTS | `D:\CECPC\PRODUCTION\IA\Mercure\MASTAURIGE\CASW\agents_rules_orion26.md` |
| Process tweets | `D:\CECPC\PRODUCTION\IA\Mercure\MASTAURIGE\CASW\PROCESS_TWEETS_AURIGE.md` |
| Index WEB AURIGE | `D:\CECPC\PRODUCTION\EXER\AURIGE 2BB\00_Boites à outils\MASTAURIGE\WEB\index.html` |
