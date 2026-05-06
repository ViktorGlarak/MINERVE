# PARAMÈTRES LTX 2.3 — Référence complète
Source : https://ltx.io/model/model-blog/prompting-guide-for-ltx-2

---

## Structure du prompt — Format officiel

**Un seul paragraphe fluide de 4 à 8 phrases descriptives.**
- Verbes au présent pour les mouvements et actions
- Progression naturelle du début à la fin de la scène
- Ordre recommandé :
  1. **Établissement du plan** (terminologie cinématographique)
  2. **Mise en scène** (lumière, palette de couleurs, textures, atmosphère)
  3. **Séquence d'action** (progression du mouvement)
  4. **Définition du sujet** (apparence, vêtements, émotions via des indices physiques)
  5. **Mouvement de caméra** (direction, timing, ce qui apparaît après le mouvement)
  6. **Description audio** (sons ambiants, musique, dialogues entre guillemets)

---

## Mouvements de caméra officiels

| Terme anglais | Description |
|---|---|
| `slow dolly in` | Travelling avant lent |
| `dolly out / pull back` | Travelling arrière |
| `pan left / right` | Panoramique horizontal |
| `tilt up / down` | Inclinaison verticale |
| `track` | Caméra suit le sujet |
| `circle` | Orbite circulaire autour du sujet |
| `overhead` | Vue aérienne plongeante |
| `handheld` | Caméra portée, instable, réactive |
| `zoom in / out` | Zoom optique |

Toujours associer un modificateur de vitesse : `slow`, `quick`, `gradual`, `sudden`

---

## Styles visuels disponibles

**Cinématographiques :** period drama, noir, fantasy, thriller, documentary
**Animés :** stop-motion, 2D animation, 3D animation, claymation, hand-drawn
**Esthétiques :** comic book, cyberpunk, surreal, minimalist, painterly

**Effets atmosphériques :** flickering candles, neon lighting, natural sunlight, fog/mist,
rain, dust, particles, film grain, reflections, golden hour

---

## Ce qu'il faut éviter (ABSOLUMENT)

| À éviter | Raison |
|---|---|
| Labels émotionnels ("sad", "confused") | Utiliser des indices visuels physiques à la place |
| Texte, logos, panneaux lisibles | LTX ne génère pas de texte fiable |
| Physique complexe (sauts, jonglage) | Artefacts garantis |
| Mouvement chaotique non-linéaire | Dégrade la cohérence visuelle |
| Trop de personnages / actions simultanées | Confusion pour le modèle |
| Lumières contradictoires | Sans justification narrative claire |
| Prompt trop complexe d'emblée | Construire par itération |

---

## Synchronisation audio-mouvement

LTX 2.3 excelle à synchroniser mouvements personnages, caméra et animation de scène avec l'audio.
Dialogue entre guillemets : `"Bonjour, que se passe-t-il ici ?"`
Support multilingue (français inclus).

---

## Conseils pratiques

- **Plans rapprochés** = beaucoup de détail précis dans le prompt
- **Plans larges** = moins de détail nécessaire (le modèle interprète)
- **Itérer** : commencer simple, ajouter des éléments progressivement
- **Cohérence** : audio + lumière + mouvement + émotion doivent se soutenir mutuellement

---

## Templates pour exercices de crise (style documentaire / news)

### Reportage TV — Caméra portée
```
A handheld news camera captures [SUJET] on [LIEU EN FRANCE], 
the image slightly unstable with natural journalist movement. 
[SUJET] [ACTION au présent], [DÉTAILS VESTIMENTAIRES et COMPORTEMENT]. 
Overcast daylight filters through [ÉLÉMENTS DE DÉCOR], 
casting flat journalistic light across the scene. 
The camera slowly tracks [DIRECTION] to reveal [ÉLÉMENT SUPPLÉMENTAIRE], 
ambient street sounds and distant voices fill the audio space.
```

### Surveillance CCTV — Fixe
```
A static security camera records [LIEU] from an elevated fixed position, 
wide-angle lens capturing the full scene with characteristic surveillance distortion. 
[SUJET] moves through the frame from [DIRECTION ENTRÉE] to [DIRECTION SORTIE], 
[ACTION au présent] with [COMPORTEMENT]. 
The footage shows [HEURE DU JOUR] lighting, 
a timestamp overlay visible in the corner, 
ambient environmental sounds of [LIEU] carry through the audio.
```

### Drone aérien — Descente
```
An aerial drone shot descends slowly over [LIEU EN FRANCE], 
the wide lens revealing [DESCRIPTION DU PAYSAGE] below. 
[ÉLÉMENTS DE SCÈNE] are visible from above, 
[ACTIVITÉ/SITUATION] unfolding across the frame. 
Overcast sky [OU CONDITIONS MÉTÉO] diffuses the light evenly, 
the drone gradually tilts to reveal [ÉLÉMENT FOCAL], 
wind ambiance and distant [SONS] accompany the descent.
```

### Caméra embarquée — Véhicule
```
A dashcam records from inside a moving vehicle traveling along [TYPE DE ROUTE] 
in [RÉGION DE FRANCE], the road stretching ahead through [PAYSAGE]. 
[CONDITIONS MÉTÉO] light falls on [ÉLÉMENTS VISIBLES], 
[ÉLÉMENTS DE SCÈNE DE CRISE] visible along the roadside. 
The vehicle maintains steady forward movement, 
engine hum and [SONS AMBIANTS] fill the audio,
the camera occasionally adjusting to road vibration.
```
