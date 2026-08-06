# RECAPS — vues de synthèse des exercices passés

> Classeurs Excel **de consultation** (≠ `BIBLIOTHEQUES\`, qui contient les fichiers destinés à l'**import** MASTORION).
> Générés depuis l'outillage MASTAURIGE des exercices, en lecture seule.

## `RECAP_INJECTS_GUILLAUME_MINOTAURE.xlsx`

Vue « qu'a-t-on joué ? » — **un onglet par exercice** :

| Onglet | Exercice | Injects | Produits |
|---|---|---|---|
| **GUILLAUME** | AURIGE 2BB | 70 | 176 — Tweet 105 · Article 60 · Courrier 8 · Tract 3 |
| **MINOTAURE** | AURIGE 7BB | 84 | 105 — Tweet 60 · Article 28 · Courrier 9 · Tract 8 |

**Colonnes** : `numero` · `nom` · **`types_de_produit`** (ex. « Tweet x3 + Article ») · `nb_produits` · `description` · `date_de_jeu` · `etat` · `destinataires` · `lo` · `detail_des_produits` (liste des produits rattachés, avec leur sous-code).
Filtres automatiques actifs sur la ligne d'en-tête + volets figés.

### Sources (par exercice)
| Donnée | 2BB / GUILLAUME | 7BB / MINOTAURE |
|---|---|---|
| Liste des injects (n° + nom + desc + date + état) | `MELMIL\melmil_data.js` | idem (socle synchronisé JEMM) |
| Tweets | `tweets_data.js` (champ `num`) | `moteur\tweets_data.js` |
| Articles / tracts / courriers | `MELMIL\melmil_inject_index.js` (index typé inject→cards) | `moteur\articles_data.js` (champs `num`, `type`, `site`) |
| Noms de secours | commentaires `<!-- code — libellé -->` de `index_master.html` | — |

> Les sous-injects (`07.01.04Bi`, `07.02.I08B`) sont **rattachés à leur inject parent** ; leur code exact reste visible dans `detail_des_produits`.

## ⚠ Écarts constatés (état des sources, pas des bugs du script)

1. **22 injects du 2BB sont absents du socle MELMIL** alors qu'ils ont bien été joués (`04.01.*`, `07.07.*`, `07.08.*`, `08.01.01Ai.R1/R2`, `01.01.119i`…). Ils apparaissent quand même dans l'onglet, avec `destinataires` = « ⚠ hors matrice MELMIL » et un nom repris des commentaires de l'agrégateur. Cause probable : `melmil_data.js` (2BB) date du 2026-06-02 et n'a pas été régénéré ensuite.
2. **4 injects sans produit MASTAURIGE** : `08.02.03i`, `08.03.01i` (2BB) · `05.09.I06`, `05.11.I04` (7BB) — inscrits à la matrice mais sans production rattachée.
3. **9 produits HTML du 7BB ne sont pas déclarés dans `articles_data.js`** → ils n'apparaissent donc pas dans le récapitulatif :
   `Olamao_Declaration_Officielle` · `HEX_Article_CICR_POW_01` · `HEX_Article_Guterres_Statement` · `ONU_Declaration_Guterres_03Juin` · `OTAN_Declaration_Rutte` · `TV4_Article_Guterres_Doute_01` · `TV4_Article_Guterres_Statement` · `TV4_Article_Panique_01` · `TM_Article_POW_Morhange_01`
   *(les 9 autres fichiers non référencés sont des `_TEMPLATE.html`, normaux.)*

## Régénérer

```
python D:\CECPC\PRODUCTION\IA\MINERVE\MASTORION\OUTILS\generer_recap_injects.py
```
