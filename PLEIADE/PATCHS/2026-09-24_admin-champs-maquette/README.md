# app-admin — champs de maquette presse dans le formulaire d'item

Pour Xavier. Deux patchs à appliquer sur `main` d'app-admin (`git am *.patch`) :

1. `0001` — « Se déconnecter ferme aussi la session Keycloak de la zone » (déjà transmis le 21/09, repris ici pour que la série s'applique d'un bloc).
2. `0002` — **les champs que l'app annonce**.

## Ce que fait 0002

- press annonce désormais dans `/api/service/health` un tableau `item_fields` (chapô, alerte, à la une, puis les champs de **la maquette choisie par la rédaction** : lieu TV4/BC1, « L'essentiel » TF1, référence/signataire ONU, émission ZubrRadio, bouton EFS…). Commit press `aeda6d5`.
- L'admin lit `item_fields` (comme `needs_title`), affiche les champs sous la rubrique, groupés par intertitre, les garde sur l'item (nouvelle colonne `scenario_items.fields`, JSON, `db push` additif) et les renvoie dans `fields` à la publication.
- L'admin ne connaît aucune maquette : si la rédaction change de maquette, le formulaire suit.

## Compatibilité

- admin nouveau + press ancien : pas d'`item_fields` → formulaire inchangé.
- admin ancien + press nouveau : `fields` jamais envoyé → comportement d'avant.
- Ordre de déploiement indifférent.

## Vérifié

Admin et press en local (clé de service d'essai, eho simulé) : item créé dans le formulaire sur une presse en maquette ONU → champs gardés sur l'item → publication → la page ONU affiche la référence, le signataire et sa fonction. `npm test` : 5/5. `tsc` propre.
