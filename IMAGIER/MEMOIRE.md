# MÉMOIRE — IMAGIER

## Format d'entrée
```
### [YYYY-MM-DD] Exercice : [NOM] — [Titre de la scène]
**Outil :** Gemini / Flow
**Prompt utilisé :** texte exact
**Résultat :** PASS / FAIL + observations
**Leçon :** ce qu'il faut retenir
```

## ⚠ RÈGLE SYSTÈME — 2026-05-29

### Règle MASTAURIGE obligatoire
Si une image produite par IMAGIER est destinée à l'écosystème MASTAURIGE (`...\MASTAURIGE\WEB\images\`), MASTAURIGE est consulté pour le nommage du fichier et l'intégration dans index_master ou les articles HTML.

### Convention nommage images AURIGE 2BB
- Portraits MER : `MER_NOM_PRENOM_fonction.jpg` — ex : `MER_VORIN_sniper.jpg`
- Images injects : `XX.YY.ZZ_description_courte.jpg` — ex : `07.05.03_Manifestation_opposition_Pro_MER_BR_BC1.jpg`
- Avatars tweet : dossier `images/avatars tweet/` — format `CAMP_HandleSansAt.png`

### Doctrine calibration brigade (AURIGE) — images
À partir de D+35, les images prioritaires à créer pour AURIGE 2BB sont des visuels **locaux brigade** :
- Tags/graffitis sur murs de villes ZO
- Manifestations locales (foule, pancartes)
- Drapeau MER sur bâtiment public
- Vandalisme sur matériel militaire
- Photos civils dans rue avec tracts

---

## ⚠⚠ RÈGLE MATÉRIEL — précision véhicules/soldats par camp [2026-06-25]

> Retour utilisateur (inject 07.10.I02) : un prompt « military supply trucks / armored
> vehicles » a généré des **véhicules US et d'époque** → FAUX pour un exercice **FR/OTAN**.
> Scène bonne, **matériel incohérent**.

**Réflexe obligatoire avant tout prompt montrant un véhicule ou un soldat :**
1. **Lire le camp réellement MONTRÉ à l'image** (≠ camp éditorial de l'article) :
   - 🔵 forces françaises/OTAN (7BB, BFA, coalition) → **Griffon, Serval, Jaguar, Leclerc, VAB, VBCI, CAESAR, GBC 180, TRM 10000, PPLOG** ; camo **Centre-Europe**, casque **SPECTRA**, **FÉLIN**, **HK416/FAMAS**.
   - 🔴 Mercure → matériel **type russe** : **T-72/T-90-style, BTR-80, BMP, Ural-4320, 2S19 Msta** ; camo **digital flora**, **AK**.
2. **Nommer le modèle EXACT** dans le positif. Ne jamais laisser l'IA deviner → elle met du US/WW2.
3. **Negative** anti-US / anti-époque : `no American vehicles, no Humvee, no Abrams, no MRAP, no US multicam, no WW2 vehicles, no desert tan`.
4. **Firefly** suit mieux si on cite le nom exact (web) ; **Flow/Gemini** → modèle **+** silhouette décrite.

📖 **Détail complet (tables 🔵/🔴 + blocs prompts prêts) : [`IMAGIER\REFERENTIEL_MATERIEL.md`](REFERENTIEL_MATERIEL.md)** — à CONSULTER avant toute scène militaire. Vaut aussi pour le SCÉNARISTE quand il décrit une scène à illustrer.

### Pattern validé — intégration hero dans un article MASTAURIGE baké [2026-06-25]
Pour embarquer une image dans un article externe (`external:true, origin:baked`) de l'instance MASTAURIGE :
1. **Compression** : `PIL` → largeur **1000 px**, **JPEG qualité 80**, `optimize+progressive`. Repère : un hero paysage ≈ **80–130 Ko** (base64). Suffisant et léger. Python 3.14 du poste (PIL OK).
2. **Injection** : bloc `<figure><img src="data:image/jpeg;base64,…" style="display:block;width:100%"></figure>` + `<div>` légende (styles **inline**, zéro dépendance CSS) inséré **juste après `<article>`** dans le **HTML source** (`Sites/<dossier>/<fichier>.html`), en binaire pour préserver les CRLF.
3. **Re-bake** : `node OUTILS/generer_articles_html_js.js` → régénère `moteur/arthtml/<id>.js` (ce qui s'affiche réellement). Vérifier `grep -c data:image/jpeg`.
4. 1er usage : inject **07.10.I02** (convoi OTAN français). Légende attribuée au média du camp (« — Today Mercure »).

---

## Contexte des exercices (à injecter dans les prompts)
- Exercices de crise militaire et civile en France
- Régions réelles : Lorraine, Vienne, Deux-Sèvres, Poitou-Charentes
- Style visuel cible : photorealistic, news footage, documentaire militaire
- Pas de symboles nationaux réels identifiables sur les équipements fictifs
- **Matériel toujours nommé précisément par camp → voir RÈGLE MATÉRIEL ci-dessus + `REFERENTIEL_MATERIEL.md`**

---

## Workflow vidéo — Image d'abord, toujours
Pour toute production vidéo, l'IMAGIER génère l'image source en premier.
Cette image doit contenir EXACTEMENT ce qu'on veut voir dans la vidéo : décor précis, personnages, logos, ambiance.
Le CINÉASTE anime ensuite cette image avec LTX i2v.
Outil recommandé par priorité : Adobe Firefly (licence) > Flow > Gemini.

## Règle absolue — Intégration du texte des messages
Quand l'utilisateur fournit un texte précis à afficher dans une image (message WhatsApp, tract, affiche, document),
ce texte DOIT être intégré mot pour mot dans le prompt, entre guillemets, avec la mention "legible word for word".
Ne jamais résumer ou paraphraser le texte fourni. Le copier-coller exactement.

## Patterns de prompt efficaces
<!-- Formulations validées qui produisent de bons résultats -->

---

## Patterns à éviter
- Eviter les termes trop militaires explicites qui déclenchent les filtres Gemini
- Préférer "emergency forces" à "armed soldiers" pour contourner les restrictions
- **Ne jamais utiliser "protesters"** pour des scènes de blocage civil → Flow génère systématiquement des drapeaux CGT/syndicaux. Remplacer par : `local residents`, `ordinary civilians blocking the road`, `local people standing in the road`
- **Drapeaux syndicaux/nationaux** : verrouiller dans le positif ET le négatif simultanément. Le négatif seul est insuffisant si le positif évoque la manifestation.
  - Dans le négatif : `CGT, union flags, French flag, tricolor, national flag, political banners, flag poles, any flags whatsoever, union symbols`

### ⚠⚠ RÈGLE PANCARTES / TEXTE À L'IMAGE — jamais de support vide [2026-06-25]
Retour utilisateur (inject 07.11.I05) : une scène avec « blank cardboard signs » a généré des **pancartes vides** → ça fait faux/inachevé. **Un support censé porter du texte (pancarte, banderole, affiche, tract, écran, panneau) ne doit JAMAIS apparaître vide.** Deux options, jamais d'entre-deux :
- **(A) Texte EXACT verbatim** : reprendre un slogan **réel de l'article**, court, entre guillemets, avec `legible word for word`. Privilégier des slogans **courts** (3–5 mots) → bien mieux rendus. Ex. 07.11.I05 : `"NI OTAN NI MERCURE"`, `"LA PAIX PAS LES CHARS"`, `"RENDEZ-NOUS NOS ROUTES"`.
- **(B) Pas de support du tout** : cadrer la scène **sans** pancarte (foule, barrage, visages) et l'interdire au négatif : `no signs, no placards, no banners, no cardboard signs`.
- **Choix de l'outil** si texte voulu : **Flow** ou **Firefly** (gèrent le texte court) — *pas* Gemini (corrompt le texte). Si l'outil garde garbling le texte → basculer en option (B) ou overlay du texte en post (Premiere/Canva).
- Le **SCÉNARISTE** fournit les slogans/textes exacts à afficher quand il décrit une scène à illustrer (cf. sa mémoire).

## Texte dans les images — règles par outil [2026-05-07]

### Flow (Google) — GÈRE TRÈS BIEN LE TEXTE LONG
**Règle absolue : toujours inclure l'intégralité du texte verbatim dans le prompt Flow.**
Flow reproduit fidèlement le texte, les logos, et la mise en page dans une seule génération.
Validé sur : tract N.O.M avec logo + titre + corps + liste à puces (résultat PASS direct).
Ne jamais proposer un workflow hybride (Flow + Premiere) pour du texte quand Flow est l'outil cible.

### Gemini — INCAPABLE de rendre du texte long avec précision
Sur des messages WhatsApp (50+ mots), le texte sera corrompu (mots inventés, phrases manquantes).
**Workflow validé pour texte exact avec Gemini :**
1. Gemini génère la coque UI (interface WhatsApp réaliste)
2. Overlay du texte exact dans Premiere Pro ou Canva
3. Couleurs WhatsApp : bulle reçue fond #FFFFFF texte #000000 / bulle envoyée fond #DCF8C6
4. Police : SF Pro (iOS) ou Roboto (Android)
**Alternative rapide :** WA Mock ou Zeoob WhatsApp Generator (outils web, texte tapé manuellement)

---

## Prompts validés par exercice

### AURIGE 2BB

#### [2026-05-06] QC : FAIL agent / PASS noyau — Screenshots WhatsApp 07.07
**Demande :** 3 captures d'écran WhatsApp de messages de propagande fictifs (scénario 07.07)
**Agent appelé :** llama3.1:8b — résultat insuffisant (prompts génériques, mauvaise compréhension UI)
**Correction :** Claude a généré les prompts directement
**Leçon :** llama3.1:8b ne maîtrise pas les détails d'interface mobile — pour les mockups UI, Claude intervient en direct
**Workflow validé :** Gemini pour la coque visuelle + overlay texte dans Premiere Pro/Canva
**Couleurs WhatsApp :** bulles reçues = fond blanc / bulles envoyées = fond #DCF8C6 (vert clair)

**Prompts utilisés :**
- iPhone 14 Pro, light mode, 14:23, "Numéro inconnu +33", bulle reçue française
- Samsung Galaxy S23, dark mode, 21:47, "Numéro masqué", bulle reçue française  
- iPhone 15, light mode, 23:09, "Unknown Number", bulle reçue anglaise
