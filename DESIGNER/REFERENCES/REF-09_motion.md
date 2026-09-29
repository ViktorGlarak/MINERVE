# REF-09 — Motion (ex-Framer Motion)

- **Source** : https://github.com/motiondivision/motion · docs https://motion.dev (accessibilité : /docs/react-accessibility)
- **Ingéré** : 2026-09-24 · **Licence** : MIT
- **Nature** : bibliothèque d'animation pour JavaScript, React (`motion/react`, remplace `framer-motion`) et Vue (`motion-v`).

## Capacités
Animations déclaratives · gestes (glisser, survoler, appuyer) · **transitions de mise en page** (un élément qui change de place s'y déplace) · animations liées au défilement · **ressorts** (mouvement naturel) · **animations de sortie** (`AnimatePresence`) · moteur hybride accéléré par le GPU (jusqu'à 120 i/s) · tree-shaking.

## ⭐ Accessibilité : non négociable
- Certaines animations **donnent le mal des transports**. Il faut **respecter la préférence système « réduire les animations »** (`prefers-reduced-motion`).
- `<MotionConfig reducedMotion="user">` coupe automatiquement les animations de **déplacement et de mise en page**, et **garde l'opacité et la couleur** (les transitions qui aident à comprendre).
- Le hook `useReducedMotion()` permet de faire soi-même :
  - un **fondu à la place d'un déplacement** ;
  - pas de vidéo lancée automatiquement ;
  - **pas de parallaxe**.

## Règles d'emploi pour nos projets
- Une animation doit **expliquer** : d'où vient un élément, où il va, ce qui a changé. Elle ne sert pas à décorer.
- Durées courtes : **150 à 250 ms** pour l'interface, jamais au point de freiner l'utilisateur (voir Doherty, REF-06).
- N'animer que `transform` et `opacity` ; éviter les propriétés qui forcent le navigateur à recalculer la mise en page (`width`, `top`…).
- Aucune app PLÉIADE n'utilise Motion aujourd'hui. Les transitions CSS suffisent dans la plupart des cas ; Motion ne se justifie que pour les **transitions de mise en page** (par exemple une carte qui passe d'une colonne de la planche MELMIL à une autre).
