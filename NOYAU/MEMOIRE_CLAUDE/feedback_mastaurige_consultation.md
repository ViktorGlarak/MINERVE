---
name: feedback-mastaurige-consultation
description: "Règle obligatoire : MASTAURIGE doit être consulté avant toute création d'avatar RS fictif — applicable à tous les agents Mercure"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 73fcca0d-c040-42d3-9859-fa36df54c216
---

Avant de créer un avatar RS fictif pour un exercice Mercure, MASTAURIGE doit obligatoirement être consulté.

**Processus en 3 étapes :**
1. Vérifier si l'avatar existe dans `MASTAURIGE/CASW/avatars_casw_orion26.md` (222 avatars ORION 26)
2. Si non, vérifier `MASTAURIGE/CASW/avatars_casw_[exercice].md` (avatars spécifiques à l'exercice)
3. Si inexistant : créer la fiche CASW dans le fichier approprié ET déclarer dans `MASTAURIGE/MEMOIRE.md`

**Why:** Lors de la production AURIGE 2BB, 4 nouveaux avatars (@EastWatch_Intl, @CorrespondantEst, @TemoignageDAC, @VoixDACia) ont été créés et intégrés dans index_master.html sans consultation préalable de MASTAURIGE. Risque de doublon, contradiction de profil, perte de traçabilité. Corrigé rétroactivement en créant `avatars_casw_aurige2bb.md`.

**How to apply:** S'applique à TOUS les agents du projet Mercure — NOYAU, GUILLAUME, EXPERT_INFLUENCE, ANALYSTE, SCÉNARISTE, MASTAURIGE lui-même. Dès qu'un contenu RS fictif est envisagé avec un nouveau compte, stopper et consulter MASTAURIGE d'abord. Voir règle consolidée dans `MASTAURIGE/MEMOIRE.md` et `MASTAURIGE/CASW/PROCESS_TWEETS_AURIGE.md` section 7.

## MASTAURIGE = registre canonique des personas — source de vérité du CAMP (décidé 2026-06-01)

Décision utilisateur : centraliser l'identité des avatars comme on le fait pour les Analystes. **Le registre MASTAURIGE (`MASTAURIGE\MEMOIRE.md` § Avatars + miroir `avatars.js`) est l'UNIQUE propriétaire de l'identité d'un persona : handle, nom, image, et surtout le CAMP (🔴/🔵/⚪).** Les autres IA citent, ne recopient jamais.
- L'**Analyste pays** reste l'autorité de **décision** du camp (expertise) + la **doctrine** (LO, emploi) ; mais le camp est **stocké une seule fois** (registre MASTAURIGE). Changement de camp → l'Analyste tranche puis met à jour `MASTAURIGE\MEMOIRE.md` + `avatars.js`.
- **Garde-fou auto** : `WEB\OUTILS\verifier_mastaurige.py` **CONTROLE G** signale tout tweet dont le `camp` **contredit durement** (rouge↔bleu) son avatar. Un avatar ⚪ neutre qui penche (façade blanchiment, ex. @EastWatch_Intl en rouge) n'est PAS une divergence — exclu volontairement.
- Règle canonique mise à jour dans `CLAUDE.md` § « Propriétaire unique d'une fiche personnage » (table par TYPE : identité+camp → MASTAURIGE ; doctrine → Analyste).
**Why:** dérive Svetlana Tikhanov (camp « bleu » recopié dans 7 fichiers, faux = rouge pro-MER, corrigé 2026-06-01) après celle de Saniki. Un seul endroit fait foi + un lint qui alerte.

## ⚠ Renforcement 2026-06-28 — consulter l'ANALYSTE PAYS + la réserve CASW AVANT de créer (récidive)

Incident : pour l'inject 07.09.I03 (église HThal-Marmoutier), j'ai **créé un nouvel avatar `@HenriBraun67`** pour un « habitant local pro-MER » **alors qu'ANALYSTE_ARN possède déjà des habitants locaux diaspora mercurianophone 🔴 inutilisés/peu utilisés avec de vrais noms Arnland** (`@Stepan_Roubek` HSarrebourg, `@MakarovSid` HBlamont, `@GavrilovBorislav` HDieuze…). Corrigé : @HenriBraun67 supprimé, **réutilisation de `@Stepan_Roubek`**.

**Règle (réflexe AVANT toute création d'avatar) :** 1) lire le **roster de l'Analyste pays** (`ANALYSTE/ARNLAND|MERCURE|BOTHNIA/MEMOIRE.md`) pour un persona existant qui colle (nom + camp + profil) ; 2) regarder la **réserve CASW** (avatars ORION 26 inutilisés, avec photo) ; 3) regarder les avatars de `avatars.js` **non utilisés** dans les tweets. **Créer un nouvel avatar = DERNIER recours**, et seulement après ces 3 vérifs + validation de l'Analyste. **Why:** un nom franco-générique sans photo (« Henri Braun », initiales) gaspille une réserve riche de personas Arnland déjà profilés et casse la cohérence onomastique. **How:** demander explicitement « quel persona existant chez l'Analyste/CASW pour ce rôle ? » avant d'en inventer un.

Lié à : [[aurige-guillaume]], [[mastaurige]], [[melmil-coherence]]
