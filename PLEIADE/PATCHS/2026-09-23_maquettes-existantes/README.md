# app-press — « Maquettes existantes » (10 sites d'exercice)

Ces fichiers contiennent la branche `maquettes-existantes` d'`app-press`. Elle part de `origin/main` (`e8e22ee`) et compte 3 commits :

| Commit | Contenu |
|---|---|
| `99b649f` | Se déconnecter ferme aussi la session Keycloak de la zone *(le patch du 2026-09-21, jamais poussé)* |
| `1a40aa1` | Maquettes existantes, vague 1 : TV4, Today Mercure, Bothnia Channel 1 |
| `5c43ffe` | Onglets « génériques / existantes », vagues 2 et 3 : Hexagone, TF1 Info, Omerta, ONU, OTAN, ZubrRadio, EFS |

## Appliquer

Tu peux récupérer la branche entière, commits compris, depuis le paquet :

```bash
git fetch app-press_maquettes-existantes.bundle maquettes-existantes:maquettes-existantes
```

Tu peux aussi appliquer les patchs dans l'ordre :

```bash
git am 000*.patch
```

## Ce que ça change

- **Réglages ▸ Maquette et thème** : deux onglets, « Maquettes génériques » et « Maquettes existantes ». Le second reprend les templates HTML de MASTAURIGE (dossier `Sites/` d'AURIGE 7BB) sous forme d'habillages fidèles. La charte d'origine est verrouillée par défaut ; « Retoucher les couleurs » permet de la modifier.
- **`src/skins/`** : un registre qui ne contient que des données (`registry.ts`), cinq vues par site (Shell, Home, Article, List, Page) qui n'accèdent jamais à la base, et une feuille de style par site, limitée à son habillage par la classe `.sk-<clé>`. Les réactions, le fil en direct et la mention d'exercice sont les composants existants, posés dans des « îlots » `.site` qui reçoivent les couleurs de la charte.
- **Schéma Prisma** : deux colonnes facultatives, `Site.skin` (VarChar 40) et `Article.skinFields` (Text, JSON). Elles sont ajoutées par `db push` au démarrage, sans perte de données.
- **`lib/sanitize.ts`** : les classes de corps d'article des templates sont désormais autorisées (`figures-box`, `ops-box`, `BodySubTitle`, `z-seg`…), ainsi que l'attribut `class` sur `ul`, `h2` et `blockquote`. Cela reste limité à des classes : aucun style en ligne n'est accepté.
- **`lib/notice.ts`** : `EXERCISE_NOTICE` y est déplacé pour pouvoir être importé côté navigateur. `lib/site.ts` le réexporte, donc les imports existants continuent de fonctionner.
- **Polices** : PT Serif, PT Sans, Oswald, Source Sans 3, Lora, Overpass, Zilla Slab et Red Hat Display, embarquées via `next/font`.
- **`public/skins/`** : les logos d'Hexagone, TF1, Omerta et OTAN, extraits du base64 des templates.

## Vérifié en local

`tsc` passe sans erreur et les 5 tests existants passent. Les 10 sites ont été capturés et comparés aux templates d'origine. Les 40 pages (accueil, rubrique, recherche, direct × 10) renvoient 200 sans erreur navigateur. Le parcours complet des réglages a été rejoué avec Playwright.

## Deux points d'attention

- **Le retour en arrière n'est pas automatique.** Si une instance passe sur cette image puis revient sur une image sans ces colonnes, `db push` voudra les supprimer et s'arrêtera faute de `--accept-data-loss`.
- **TF1 Info et Omerta Média reproduisent de vrais médias**, logo compris, comme les templates d'origine.
