# RÉFÉRENTIEL MATÉRIEL — par camp (génération d'images)

> **Pourquoi ce fichier.** Retour utilisateur 2026-06-25 (inject 07.10.I02) : un prompt « military supply trucks / armored logistics vehicles » a généré des **véhicules américains et d'époque**, incohérents avec un exercice **français / OTAN**. Le contenu de la scène était bon, **seul le matériel était faux**.
>
> **Règle d'or.** Dans les exercices AURIGE / ORION (cadre FR-OTAN vs adversaire de doctrine russe), **TOUJOURS nommer le matériel précisément** dans le prompt (modèle exact), camp par camp. Ne jamais laisser l'IA « deviner » → elle tombe sur du générique US/WW2.
>
> **Astuce outil.** **Adobe Firefly** sait s'appuyer sur des références web → plus on **cite le nom exact du modèle** (« French Army Griffon VBMR (Scorpion programme) »), meilleur est le rendu. Flow/Gemini : citer le modèle **+ une description de silhouette** (ex. « 6-wheeled French armoured personnel carrier, sloped armour, remote weapon station ») car ils connaissent moins les désignations.

---

## 🔵 BLEU — Forces françaises / OTAN (les ENTRAÎNÉS : 7BB, BFA, coalition)

### Véhicules — France (armée de Terre, programme SCORPION + parc en service)
| Rôle | Modèle exact à citer | Repère silhouette (pour Flow/Gemini) |
|---|---|---|
| Blindé multirôle (VBMR) | **Griffon (VBMR Griffon)** | 6×6, caisse haute anguleuse, tourelleau téléopéré (RWS) |
| Blindé léger (VBMR-L) | **Serval** | 4×4 compact, vitré, RWS |
| Reco / chasseur de chars (EBRC) | **Jaguar (EBRC Jaguar)** | 6×6, tourelle canon 40 mm CTA |
| Char de bataille | **Leclerc (char Leclerc)** | MBT, tourelle plate basse, canon 120 mm |
| Reco blindée (legacy) | **AMX-10RC**, **ERC-90 Sagaie**, **VBL** | 6×6 canon / petit 4×4 reco |
| Transport de troupe (legacy) | **VAB**, **VBCI** | VAB 4×4 boîte ; VBCI 8×8 avec tourelle 25 mm |
| Artillerie | **CAESAR (155 mm sur camion)**, **TRF1**, **LRU** (roquettes) | canon long sur cabine blindée 6×6 |
| **Logistique / transport** | **GBC 180** (camion tactique), **TRM 10000**, **PPLOG** (Porteur Polyvalent Logistique), **VTL** | camions kaki bâchés FR, cabine carrée |
| Génie | **EBG**, **SPRAT**, **Griffon EPC** | — |
| Hélico | **Tigre** (attaque), **NH90 Caïman**, **Gazelle** | — |

### Véhicules — BFA / Allemagne & alliés OTAN (si Brigade Franco-Allemande / coalition)
- **Boxer** (8×8 modulaire), **Fuchs/Transportpanzer** (6×6), **Leopard 2** (MBT), **PzH 2000** (artillerie chenillée 155 mm), **Puma/Marder** (VCI chenillé).

### Soldat français / OTAN
- **Treillis** : tenue de combat **F3**, camouflage **« Centre-Europe » (bariolé vert/marron/noir)** — *PAS* de multicam US, *PAS* de coyote/tan désert.
- **Casque** : **SPECTRA** (FR) ou casque balistique vert OTAN, parfois sous couvre-casque bariolé.
- **Système fantassin** : **FÉLIN** (gilet + équipement intégré).
- **Arme** : **HK416 F** (standard actuel FR) ; **FAMAS** (legacy, « bullpup » blanc/noir) ; ceux-ci plutôt que M4/M16 US.
- **Gilet** : porte-plaques vert OTAN.

**Bloc prompt BLEU prêt à l'emploi (à coller/adapter) :**
```
French Army (NATO) equipment, accurate and contemporary: Griffon VBMR 6x6 armoured
vehicles and GBC 180 / TRM 10000 tactical supply trucks, kaki green, French
"Centre-Europe" woodland camouflage, soldiers wearing SPECTRA helmets and FELIN gear
with HK416 rifles
```
**Negative (BLEU) :** `no American vehicles, no Humvee, no M1 Abrams, no MRAP, no woodland US multicam, no WW2 vehicles, no desert tan equipment, no Russian vehicles`

---

## 🔴 ROUGE — Mercure (adversaire, doctrine & matériel de type russe)

> Mercure = nation fictive de l'univers Skolkan, **équipée et entraînée à la russe**. Pas d'insigne national réel → silhouette/type russe générique.

| Rôle | Type à citer | Repère silhouette |
|---|---|---|
| Char de bataille | **T-72 / T-80 / T-90-style MBT** | tourelle dôme arrondie, bidons à l'arrière |
| VCI | **BMP-2 / BMP-3-style** | chenillé bas, profilé |
| Transport de troupe | **BTR-80/82-style** (8×8) | 8 roues, caisse en bateau |
| Reco | **BRDM-2-style** | 4×4 amphibie |
| Artillerie | **2S19 Msta / 2S3-style** (155 mm chenillé), **BM-21 Grad** (roquettes) | — |
| **Logistique / transport** | **Ural-4320**, **KamAZ-style** camions 6×6 | camion vert olive cabine ronde, capot proéminent |

### Soldat mercurien (rouge)
- **Camouflage** : type **EMR « digital flora » (pixel vert/beige russe)** ou vert uni soviétique.
- **Casque** : type **6B47 russe** / casque rond vert.
- **Arme** : type **AK (AK-74 / AK-12-style)**, crosse et chargeur incurvé caractéristiques.

**Bloc prompt ROUGE prêt à l'emploi :**
```
Eastern/Russian-pattern military equipment (fictional Mercure forces): T-72-style
main battle tanks, BTR-80-style 8-wheeled APCs, Ural-4320 supply trucks, soldiers in
Russian-style "digital flora" pixel camouflage with AK-pattern rifles and round
green helmets, no national insignia
```
**Negative (ROUGE) :** `no NATO equipment, no French vehicles, no American vehicles, no woodland Centre-Europe camo, no visible national flags or insignia`

---

## ⚖️ Qui pilote quoi dans AURIGE 7BB (rappel — camps INVERSÉS)
- **Entraînés = BLEU = français/OTAN** (7BB, BFA, 27BIM, coalition) → matériel **🔵 ci-dessus**. Ils **attaquent / progressent**.
- **Mercure = ROUGE** → matériel **🔴 ci-dessus**. Il **défend / « libère »**.
- ⚠ Un article **🔴 (Today Mercure)** qui parle de **« nos batteries », « notre 41e division »** = montrer du **matériel ROUGE russe**. Un article **🔵 (TV4/Hexagone/TF1)** qui parle des **forces françaises** = matériel **BLEU français**. **Lire le camp + le texte** avant de choisir le matériel.
- Cas mixte (ex. convoi OTAN vu par un article rouge anti-OTAN, comme 07.10.I02) : c'est du **matériel BLEU français/OTAN** (ce sont les forces alliées qui sont montrées), même si l'angle éditorial est rouge.

---

## ✅ Checklist réflexe avant tout prompt « véhicule / soldat »
1. **Quel camp est montré à l'image ?** (≠ camp éditorial de l'article) → table 🔵 ou 🔴.
2. **Nommer le(s) modèle(s) exact(s)** dans le positif (Griffon, GBC 180, CAESAR / T-72, BTR-80, Ural).
3. **Camouflage correct** : Centre-Europe (FR) vs digital flora (MER). Jamais multicam/tan US par défaut.
4. **Negative prompt** anti-US / anti-époque (voir blocs).
5. **Géo** : Lorraine, villes H-préfixe, paysage Grand Est (vallonné, forêts, Moselle) — pas de désert, pas de steppe.
