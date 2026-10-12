---
name: efs-site-base
description: Page EFS (style) validée comme modèle de référence pour toute future page/site EFS dans AURIGE — Site EFS/EFS_Reserves_Faibles_2026.html
metadata: 
  node_type: memory
  type: reference
  originSessionId: 9cd755be-0651-44f5-8932-5974a21bced9
---

**Modèle de référence EFS (validé par l'utilisateur le 2026-06-02) :**
`D:\CECPC\PRODUCTION\EXER\AURIGE 2BB\00_Boites à outils\MASTAURIGE\WEB\Site EFS\EFS_Reserves_Faibles_2026.html`

C'est la **base à réutiliser telle quelle** pour toute future page de type EFS (don du sang). Pour une nouvelle page : cloner ce fichier, garder le chrome/CSS, remplacer le contenu de l'article.

**Doctrine de production EFS (à respecter) :**
- **Style EFS reproduit** : barre utilitaire, header + nav (Don de sang / plasma / plaquettes / Qui peut donner ? / Où donner ?), bouton rouge « PRENDRE RENDEZ-VOUS », fil d'Ariane, titre + méta (date · durée · partage), hero **« RÉSERVES FAIBLES ! » recréé en CSS** (bandeau bleu #1aa3e0 + cercle rouge #e2001a), corps avec `ul.dots`, encart `.band`, blockquote témoignage, CTA rouge, footer. Palette navy #1b2a63 / rouge #e2001a / bleu ciel #1aa3e0.
- **Texte réécrit** (pas de copier-coller verbatim du site réel) ; les **faits** sont restitués (réserves, déficit, durées de conservation, dates de campagne).
- **Logo EFS** = placeholder texte « EFS / Du donneur aux patients » (marque réelle non reconstituée).
- **Graphiques/données factuelles fournis par l'utilisateur** : OK à intégrer en **base64** (ex. `ReservesFaibles-DonDeSang-Juin2026-Graph.png` intégré). Embed via script **Python** jetable (AMSI bloque PowerShell) — cf. [[feedback-image-hero-card]].
- back-btn.js en dernière ligne ; `Site EFS/` n'est pas dans la liste SITE_DIRS du validateur (pas de contrôle back-btn automatique, mais le mettre quand même).

**Usage narratif :** la page EFS est un **noyau de vérité ⚪ neutre** (institution réelle), exploité par les injects MER. 1ère utilisation = inject **07.01.07** (campagne don du sang juin 2026, LO 2+3, front intérieur français / lien armée-nation) avec tweets `@MaiaKovalenko` (07.01.07Bi) + `@HmunikVoice` (07.01.07Ci). Voir [[web-architecture]] [[mastaurige]].
