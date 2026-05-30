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

## Contexte des exercices (à injecter dans les prompts)
- Exercices de crise militaire et civile en France
- Régions réelles : Lorraine, Vienne, Deux-Sèvres, Poitou-Charentes
- Style visuel cible : photorealistic, news footage, documentaire militaire
- Pas de symboles nationaux réels identifiables sur les équipements fictifs

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
  - Dans le positif : `no flags of any kind, people holding only handwritten cardboard signs`
  - Dans le négatif : `CGT, union flags, French flag, tricolor, national flag, political banners, flag poles, any flags whatsoever, union symbols`

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
