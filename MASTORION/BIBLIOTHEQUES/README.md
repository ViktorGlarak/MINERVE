# BIBLIOTHÈQUES DE PERSONAS — import MASTORION

> Classeurs Excel au **format d'import MASTORION** (*Groupes & Users → Importer*).
> Générés depuis les sources MINERVE par `MASTORION\OUTILS\generer_bibliotheque.py`.

## Fichiers

| Fichier | Contenu |
|---|---|
| `BIBLIOTHEQUE_TEST_3_EXERCICES.xlsx` | **220 personas** — tous les avatars de **MINOTAURE 26 (7BB)**, **GUILLAUME (2BB)** et **ORION 26 (CASW)**, dédoublonnés. Fichier de **test**. |

## Comment importer

1. **Partir d'une base vierge** — `SAUVEGARDES\RESTAURER.bat` → `BASE_VIERGE`
   *(l'import n'efface jamais : sans ça, les univers se mélangent)*
2. Admin (`localhost:4201`) → **Groupes & Users** → **Importer** → choisir le classeur
3. Vérifier l'aperçu (modifiable) puis valider

## Ce que l'import crée — taxonomie des groupes (refondue le 2026-07-28)

**35 groupes** au total, tous porteurs de sens (avant refonte : 55 groupes hétérogènes, souvent à 1 membre, avec des libellés à rallonge issus de la base CASW). Moyenne : **2,2 groupes par persona**.

**1. Les 3 onglets = les camps** (pour le ciblage des likes/retweets synthétiques)
`CAMP ROUGE` (107) · `CAMP BLEU` (61) · `CAMP NEUTRE` (52)

**2. Colonne `groups` — format `PAYS - FONCTION`**

| Pays | Code | Fonctions présentes |
|---|---|---|
| Mercure | `MER` | MILITAIRE, PATRIOTE, JOURNALISTE, POLITICIEN, PACIFISTE, FAMILLE DE MILITAIRE, SOCK-PUPPET, CITOYEN |
| Arnland | `ARN` | JOURNALISTE, PRO-MERCURE, PATRIOTE, AUTORITE LOCALE, CITOYEN, MILITAIRE, POLITICIEN, REFUGIE, PACIFISTE, GROUPE CLANDESTIN |
| France | `FR` | JOURNALISTE, PATRIOTE, MILITAIRE, CITOYEN, PACIFISTE, POLITICIEN |
| Bothnia | `BOT` | JOURNALISTE, OPPOSITION, POLITICIEN |
| Titane | `TIT` | POLITICIEN |

**Groupes transverses (sans pays)** : `ONG` · `INSTITUTION INTERNATIONALE` · `MEDIA INTERNATIONAL` · `ANIMATION EXERCICE` *(+ `OTAN` et `UE` prévus dans la taxonomie, sans membre dans ce jeu de données)*

**3. Appartenance aux exercices** : `EXERCICE ORION 26` (192) · `EXERCICE MINOTAURE 26` (35) · `EXERCICE GUILLAUME 2BB` (13)

> Un persona **cumule** ses appartenances : `@HmunikVoice` = `ARN - PRO-MERCURE` + les 3 exercices ; `@ArnlandLovePeace` = `ARN - PACIFISTE` + `ARN - PRO-MERCURE` (façade écolo, manœuvre rouge).

### Corrections manuelles (table `OVERRIDES` du générateur)
21 personas AURIGE sont classés d'après la **connaissance MINERVE** et non d'après la déduction automatique. Le cas le plus important : **la Lorraine « H-préfixe » du 7BB est ARNLANDAISE** (fiction), alors que la Lorraine du 2BB est la vraie France — les handles en `57`/`67` ne sont donc **pas** des départements français côté MINOTAURE (`@BernardLutz67` = habitant de HSaverne → `ARN - CITOYEN`). Autres cas : sock-puppets Strava à façade pro-FR (`MER - SOCK-PUPPET`), comptes « Témoignage/Voix » pilotés par Mercure (`ARN - PRO-MERCURE`), N.O.M (`ARN - GROUPE CLANDESTIN`).

## Règle de priorité appliquée (demande utilisateur 2026-07-27)

En cas de conflit sur une fiche (âge, camp, biographie) :
**MINOTAURE 26 > GUILLAUME 2BB > ORION 26**

Chaîne de sourçage des biographies (la colonne `qualifications` indique la source retenue pour chaque persona) :
1. **EHO MINOTAURE** (`bios.js` du trombinoscope 7BB) — bios narratives complètes (parcours, objectifs, forces, faiblesses)
2. **Registre MINOTAURE** — notes curatées du registre d'avatars 7BB
3. **Registre MASTAURIGE / GUILLAUME 2BB**
4. **CASW ORION 26** — biographies de la base d'origine

## Limites connues

- **~17 % sans biographie** : avatars créés spécifiquement pour AURIGE et n'ayant de fiche nulle part (ex. `@Stepan_Roubek`, `@TemoignageArn`, `@MakarovSid`). À enrichir à la main dans l'Admin, ou dans les sources MINERVE puis régénérer.
- **Aucun portrait** : la colonne `avatar` attend une **URL**. Les portraits ORION pointent vers un serveur hors ligne (`masstalk-api.orion.fr`) et les portraits AURIGE sont des fichiers locaux. → MASTORION affichera des **initiales**. Pour les activer : déposer les images dans `apps\api\uploads\users\` et renseigner `avatar` = `/api/uploads/users/<fichier>`.
- **Mots de passe** : repris de la base CASW quand ils existent, sinon **vides** → MASTORION en génère un aléatoire, visible dans l'Admin (colonne mot de passe).
- `@TemoignageDAC`/`@VoixDACia` (2BB) et `@TemoignageArn`/`@VoixArnland` (7BB) sont le **même persona renommé** (DAC → ARN) : les deux sont présents car ce sont des comptes distincts.

## Régénérer

```
python D:\CECPC\PRODUCTION\IA\MINERVE\MASTORION\OUTILS\generer_bibliotheque.py
```
Le script relit les sources MINERVE (lecture seule) et réécrit le classeur.
