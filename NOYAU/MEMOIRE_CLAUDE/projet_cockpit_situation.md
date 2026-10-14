---
name: projet-cockpit-situation
description: Refonte du Cockpit (Situation · À traiter · Reporting sur catégories de suivi) — lots 1-2 en prod le 2026-10-13, chantier EN PAUSE à la demande de l'utilisateur
metadata:
  type: project
---

Refonte de la vue principale du Cockpit (avis DESIGNER 105, conditions CYBERSECU K1 à K13) : lots 1 et 2 **en production le 2026-10-13** sur DELATTRE 26. Les catégories de suivi sont des règles enregistrées sur le serveur. Le dernier passage est noté par animateur. Le partage se fait par cellule, par zone ou pour soi seul. Le collecteur du social s'appuie sur la résolution eho. « À traiter » propose « Tout marquer vu » ; le Reporting suit les catégories. La plateforme crée la base d'une instance existante au déploiement (`assurerBaseInstance`).

▶️ **Repris le 14/10** (après une pause depuis le 13/10 au soir). Le 14/10, **en production** : lot 3 (presse), vues enregistrées, Reporting sans groupes comparatifs (`app-press` `93b3ae1`, `app-cockpit` `9a8558d`, Cockpit sur `cockpit.delattre-26.pleiade.internal`). Le 14/10 au soir : **lot 4 prêt en local** (4 dépôts : plateforme, messagerie, social, Cockpit `lot4` incluant le correctif de déconnexion), à pousser dans l'ordre plateforme → messagerie → social → Cockpit. Ensuite : lot 5.

**Why:** l'utilisateur veut passer à autre chose ; le chantier reprendra plus tard.

**How to apply:** chantier actif. Lire d'abord l'encadré en tête de `PLEIADE\PLAN_COCKPIT_SITUATION.md` (état, ordre de reprise, questions ouvertes) et le journal PLEIADE (2026-10-13, suites 3 à 9). Voir [[pleiade-droits-github]].
