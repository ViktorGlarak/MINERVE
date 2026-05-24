# PROCESS — Génération et intégration de tweets AURIGE 2BB
*Maintenu par Claude (NOYAU) — créé le 2026-05-24*

---

## 1. Décision d'architecture — Agent

**Agent utilisé : MASTAURIGE** (mistral-nemo:latest)
Aucun nouvel agent créé. MASTAURIGE est l'agent Mercure dédié à l'animation Mastorion pour tous les exercices.

**Distinction avec MASTODONTE :**
- MASTODONTE = expert API Mastodon (technique, OAuth, endpoints, fédération)
- MASTAURIGE = expert contenu exercice (avatars, génération posts, HTML tweet cards)

---

## 2. Fichiers de référence CASW (ce dossier)

| Fichier | Rôle |
|---|---|
| `agents_rules_orion26.md` | Règles d'utilisation avatars + format tableau MASSTALK V3 + hashtags |
| `avatars_casw_orion26.md` | Base 222 avatars ORION 26 (identité, Mastodon, style d'écriture) |
| `PROCESS_TWEETS_AURIGE.md` | Ce fichier — procédure complète |

Ces fichiers sont des **copies** de la base ORION 26. Les originaux restent dans :
`D:\CECPC\PRODUCTION\EXER\01 ORION 26\01 - O41 - ARCHIVAGE - DOCUMENTS TRIES\01 - ORIGINE WORKING FIELDO41\99-TOOLS\setup\orion26-stobo\`

---

## 3. Étape 1 — Préparer le brief MASTAURIGE

Fournir à MASTAURIGE lors de l'appel :
1. Le contenu de `agents_rules_orion26.md` (règles format)
2. Les fiches des avatars ciblés extraites de `avatars_casw_orion26.md`
3. Le contexte scénario du jour :
   - Zone géographique : Sarrebourg, Héming, Nancy (Lorraine)
   - Événement à animer : ex. "convois OTAN bloqués sur la RN4, habitants en colère"
   - Camp(s) à activer : Rouge, Bleu ou les deux
   - Nombre de posts souhaité + éventuelle structure de thread

**Exemple de prompt MASTAURIGE :**
> "Génère un fil de 5 posts autour du blocage de convois OTAN à Sarrebourg. 3 posts pro-Mercure (@HmunikVoice, @NOVUSORDOMUNDI, @ArnlandLovePeace) et 2 pro-OTAN (@IndependentArnish, @GromovaYelena). Format tableau MASSTALK V3."

---

## 4. Étape 2 — Output tableau MASSTALK V3

MASTAURIGE produit ce tableau :

| id | account_id | compte | message | nb_likes | nb_retweets | reply_to | delta |
|---|---|---|---|---|---|---|---|
| C1 | 6056 | @HmunikVoice | Les convois de l'OTAN traversent... | 41 | 23 |  | 1 |
| C2 | 6012 | @NOVUSORDOMUNDI | Des soldats pillent... | 28 | 14 |  | 5 |
| C3 | 5801 | @IndependentArnish | Les blocages ne sont pas spontanés... | 19 | 7 |  | 8 |

Règles colonnes :
- `id` : C1/C2... = posts racines ; C1-r1/C1-r2... = réponses ; C1-r1-s1... = sous-réponses
- `account_id` : champ `idCompte` de la fiche avatar (section Comptes)
- `reply_to` : vide pour les posts racines, sinon l'id du post parent
- `delta` : minutes entre ce post et le précédent

---

## 5. Étape 3 — Conversion HTML pour index.html

Chaque ligne du tableau devient un bloc HTML dans `WEB/index.html`.

**Template :**
```html
<!-- TWEET — @pseudo / Camp — Thème -->
<div class="article-card tweet-card camp-[rouge|bleu|gris]" data-category="social"
     onclick="markTweet(this, '@pseudo')">
    <div class="tweet-header">
        <div class="tweet-avatar [rouge|bleu|gris]">XX</div>
        <div class="tweet-identity">
            <span class="tweet-name">Prénom Nom</span>
            <span class="tweet-handle">@pseudo</span>
        </div>
        <div class="tweet-camp [rouge|bleu|gris]">[PRO-MERCURE|PRO-OTAN|NEUTRE]</div>
        <span class="badge-new">NEW</span>
    </div>
    <div class="tweet-body">
        Contenu du post avec <span class="tweet-hashtag">#Hashtag</span>
    </div>
    <div class="tweet-footer">
        <span class="tweet-time">J+X — HHhMM</span>
        <span>♥ [nb_likes]</span>
        <span>↻ [nb_retweets]</span>
        <span class="tweet-platform">MASTORION</span>
    </div>
</div>
```

**Règles de traduction tableau → HTML :**

| Champ tableau | Valeur HTML |
|---|---|
| Label/Faction = Rouge | `camp-rouge`, `.tweet-avatar.rouge`, `.tweet-camp.rouge`, `PRO-MERCURE` |
| Label/Faction = Bleu | `camp-bleu`, `.tweet-avatar.bleu`, `.tweet-camp.bleu`, `PRO-OTAN` |
| Label/Faction = Gris | `camp-gris`, `.tweet-avatar.gris`, `.tweet-camp.gris`, `NEUTRE` |
| Initiales XX | 1ère lettre Prénom + 1ère lettre Nom (Pavlus Gautoreif → PG) |
| `delta` + heure base | Calculer GDH fictif (ex: J+1 — 08h47) |
| Hashtags dans message | `<span class="tweet-hashtag">#Tag</span>` |

**Où insérer dans index.html :**
Après le commentaire `<!-- AJOUTER ICI les cartes data-category="social" -->` dans la section RÉSEAUX SOCIAUX.

---

## 6. Détermination du camp

Le champ **Label/Faction** dans la fiche avatar définit le camp :
- `Rouge` → pro-Mercure / anti-OTAN
- `Bleu` → pro-OTAN / pro-Arnland
- `Gris` → neutre (ONG, institutions, compte non partisan)

---

## 7. Avatars recommandés — AURIGE 2BB (Lorraine)

**Camp Rouge :**
| Handle | Personnage | Ton | Contexte AURIGE |
|---|---|---|---|
| @HmunikVoice | Pavlus Juri Gautoreif | Virulent, éloquent, familier | Propagande radio anti-OTAN Lorraine |
| @NOVUSORDOMUNDI | N.O.M | Radical, court | Menaces, actions groupe fictif |
| @ArnlandLovePeace | Clémence Gavaloff | Agressif, littéraire | Étudiante passionnaria pro-Mercure |
| @MaiaKovalenko | Maïa Sokhaguvka | Courant, malicieux | Journaliste collecte de renseignements |

**Camp Bleu :**
| Handle | Personnage | Ton | Contexte AURIGE |
|---|---|---|---|
| @IndependentArnish | Arnish Independent | Neutre professionnel | Presse quotidienne |
| @GromovaYelena | Yelena Gromova | Formel, audiovisuel | Rédactrice en chef TV4 |
| @BelovDimitri | Dimitri Belov | Visuel, narratif | Correspondant international |
| @IvanovSerguei | Sergueï Ivanov | Précis, judiciaire | Justice et faits de société |

**Camp Gris :**
| Handle | Personnage | Usage |
|---|---|---|
| @IAEA_AIEA_off | AIEA | Déclarations officielles internationales |
| @Amnesty_International | Amnesty | Droits humains, alertes |
| @UNHCR_off | UNHCR | Flux de réfugiés, protection civile |

---

## 8. Système NEW badge — localStorage

Les tweets dans index.html ont un badge NEW comme les articles. Le système track les posts lus via leur `@handle` dans le localStorage du navigateur (clé `aurige2bb_viewed`).

**Fonctionnement :**
- Un tweet non lu affiche un badge rouge pulsant "NEW"
- Cliquer sur la carte marque le tweet comme lu (badge disparaît)
- L'onglet "RÉSEAUX SOCIAUX" affiche un point rouge si un tweet non lu existe
- La lecture persiste tant que le navigateur n'est pas vidé

**Reset (côté utilisateur) :**
```javascript
localStorage.removeItem('aurige2bb_viewed'); location.reload();
```
À taper dans la console du navigateur (F12).

**Important :** Réextraire le ZIP ne remet PAS les tweets en "non lu". Le localStorage est stocké dans le navigateur, pas dans les fichiers.

---

## 9. Distribution ZIP

Les tweets étant statiques dans `index.html`, ils sont inclus automatiquement dans le ZIP global `WEB/`. Aucune manipulation supplémentaire requise.
Le ZIP contient : `index.html` + `images/` + `logos/` + `Site TV4/` + `Site BC1/` + `Site Hexagone/`

---

## 10. Scalabilité — autres exercices futurs

Ce process est réutilisable pour ORION 26, AURIGE 3, ou tout futur exercice :
- Copier `avatars_casw_orion26.md` dans le dossier CASW de l'exercice concerné
- Adapter les hashtags au contexte narratif de l'exercice
- Si nouvelle base avatars : créer `avatars_casw_[exercice].md` dans le même format
- MASTAURIGE peut gérer plusieurs exercices simultanément
