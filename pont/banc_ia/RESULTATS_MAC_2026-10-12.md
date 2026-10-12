# Banc IA — mesures sur le Mac (2026-10-12)

> Projet avatars IA, étape 5 « parc de machines ». Mesuré depuis le Mac. **À intégrer par PLEIADE (PC) dans `PLEIADE/PROJET_AVATARS_IA.md` § 8**, ce fichier n'étant qu'un relais entre les deux postes.

**Machine** : MacBook Pro M3 Max (14 cœurs CPU, 30 cœurs GPU), 36 Go de mémoire unifiée (~300 Go/s), Ollama 0.40.2.
**Modèles** : `gemma4:26b-a4b-it-qat` (15 Go) et `gemma4:31b-it-qat` (18 Go), téléchargés le 2026-10-12.
**Invite** : synthétique, proche d'une lecture du moteur : ~1 900 jetons en entrée (fiche courte + 30 publications), sortie JSON `{pensee, message}`, `think: false`, `num_ctx` 8192. Une invite **différente à chaque passage**, pour ne pas profiter du cache. Scripts : `vitesse.py`, `parallele.py`.

## Vitesse (3 passages, après chargement du modèle)

| Modèle | Total par lecture | Lecture de l'invite | Écriture |
|---|---|---|---|
| Gemma 4 26B (A4B) | **3,0 à 3,4 s** | ~1 000 jetons/s | ~73 jetons/s |
| Gemma 4 31B | **21 à 22 s** | ~130 jetons/s | ~14 jetons/s |

À comparer avec le PC (essai 3) : 26B **2,8 s**, 31B **20,6 s** (déborde de la carte).

## Constats

1. **Sur le 26B, le Mac vaut le PC.** En l'ajoutant au parc, on double le débit sans changer la voix des avatars : ~1 150 lectures/heure par machine.
2. **Le 31B n'est pas plus rapide sur le Mac que sur le PC** (~21 s), malgré sa mémoire suffisante. **2/3 du temps passe à lire l'invite** (130 jetons/s). Il est donc exclu pour le volume et possible seulement pour des appels **à invite courte** : la relecture (résumé ≤ 1 200 caractères, soit ~400 jetons) prendrait **environ 6-7 s** (estimation à mesurer sur une vraie invite).
3. **Effet du cache** : quand l'invite reprend exactement le même début qu'un passage précédent, le 31B tombe à **~7 s** et le 26B à **~1,3 s**. Piste : **ordonner les invites du moteur du plus stable au plus variable** (consignes → fiche de l'avatar → mémoire → fil) et garder un même avatar sur la même machine. À creuser avec la façon dont `esprit.mjs` construit l'invite.
4. **Parallélisme** : Ollama sur le Mac traite les requêtes **une par une** (réglage par défaut). 2 ou 4 requêtes simultanées donnent le même débit total. À réessayer avec `OLLAMA_NUM_PARALLEL=4`, qui demande de relancer Ollama.

## Reste à faire
- Rejouer les **vraies invites** du moteur (demandées au PC : `pont/banc_ia/*.json`), avec la **qualité** en plus du temps : alertes de l'essai 3, verdicts de relecture sur les messages piégés connus.
- Mesurer la relecture 31B avec une invite réelle.
- Décision utilisateur sur la répartition des rôles, et avis **CYBERSECU** sur l'entrée d'un ordinateur personnel dans le VPN de l'exercice.
