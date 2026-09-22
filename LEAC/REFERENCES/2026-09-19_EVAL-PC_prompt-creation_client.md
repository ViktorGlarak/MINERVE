# Prompt complet de création — ÉVAL-PC
## Application d'évaluation des postes de commandement (PC)

> Document de spécification destiné à être fourni à une IA de génération d'application (Lovable, GPT, Claude, etc.) pour recréer l'application.

---

## 1. Vision générale

Créer une application web responsive (React + TypeScript, base de données PostgreSQL avec authentification et sécurité au niveau des lignes) destinée aux **centres d'entraînement** : elle permet aux **évaluateurs** d'évaluer les **postes de commandement (PC)** des unités qui s'y présentent, via des grilles de critères structurées, une saisie de notes et d'observations, des tableaux de bord statistiques, la génération de comptes rendus et d'une présentation d'« Analyse Après Action » (3A).

L'application supporte aussi un mode **auto-évaluation** : les unités en préparation opérationnelle peuvent s'auto-évaluer de façon totalement étanche vis-à-vis des évaluations officielles.

Titre affiché : **ÉVAL-PC** — sous-titre : *« Évaluation des postes de commandement »*. Mention en en-tête : *« Document de travail — Diffusion restreinte »*.

---

## 2. Rôles et permissions

Quatre rôles, stockés dans une table `user_roles` séparée (jamais sur le profil utilisateur), avec une fonction `has_role(user_id, role)` en security definer :

| Rôle | Périmètre |
|---|---|
| **admin** | Tout : création/archivage/suppression d'évaluations, gestion des droits utilisateurs, modèles, paramètres |
| **evaluator** | Saisie des critères sur les évaluations dont il est membre, selon ses droits par domaine |
| **unit** (référent d'unité) | Uniquement ses **auto-évaluations** (`mode='self'`). Ne voit jamais les évaluations officielles |
| **visitor** | Lecture seule par défaut |

Règles clés :
- Les nouveaux inscrits deviennent `visitor` ; promotion explicite par un admin (page Gestion des droits, attribution de rôle par adresse e-mail).
- **Étanchéité stricte** : admins/évaluateurs ne voient que `mode='official'` ; les référents d'unité ne voient que leurs `mode='self'`.
- L'admin peut promouvoir un utilisateur en « Référent d'unité ».

### Membres d'une évaluation (droits par domaine)
Sur chaque évaluation, le propriétaire/admin peut ajouter des évaluateurs **par adresse e-mail de connexion** (page « Paramètres de l'évaluation »). Pour chaque membre, des droits **par domaine de critères, indépendants** : **Écriture**, **Lecture seule**, ou **Aucun accès**. Un même évaluateur peut donc éditer certains domaines et seulement lire les autres. Table `evaluation_members(evaluation_id, user_id, can_edit, assigned_family_ids, read_family_ids)`.

---

## 3. Modèle de données

### Table `evaluations`
- `id`, `owner_id`, `title`, `unit` (JSON : fiche d'identité de l'unité), `staff` (JSON : effectifs/physionomie du PC), `families` (JSON : domaines de critères), `criteria` (JSON : critères), `ratings` (JSON : notes + observations + commentaires + validations par critère), `report` (texte du compte rendu), `status` ('active'|'archived'), `archived_at`, `mode` ('official'|'self', défaut 'official'), `updated_at`.
- Index sur `(mode, owner_id)`.

### Structure hiérarchique des critères (3 niveaux)
- **Niveau 1 — Domaine** de critères (ex. « Commandement », « Logistique »…)
- **Niveau 2 — Module** (sous-domaine, regroupant les critères d'un domaine)
- **Niveau 3 — Critère** : intitulé, description, pondération, note, observation, indicateur `enabled`.

Chaque critère peut être marqué **non pertinent** (`enabled=false`) par un évaluateur : il est alors barré, exclu de la saisie, des moyennes, du tableau de bord et du compte rendu. Filtre « Pertinents / Non pertinents » + compteur.

**Échelle de notation** : 2 / 2,5 / 3 / 3,5 / 4 / 4,5 / 5 (demi-points de 2 à 5). Les moyennes de domaine et de module sont **toujours visibles** dans l'arborescence, avec le taux de remplissage.

### Autres tables
- `evaluation_snapshots(evaluation_id, snapshot_date, weighted_average, fill_rate, rated_count, total_count)` — capture quotidienne automatique (upsert) à chaque mise à jour, pour le suivi de progression.
- `profiles` — dont `active_evaluation_id` (dernière évaluation ouverte, synchronisée entre appareils).
- Pièces jointes par critère : stockage de fichiers + métadonnées dans le JSON du critère.

---

## 4. Pages / navigation (barre latérale)

1. **Accueil** — fiche de l'évaluation active : titre, unité évaluée, dates, et badge du **résultat final** (ex. « 5 A ») qui lie vers « Niveau et Label ».
2. **Assistant IA** (`/chat`) — assistant conversationnel intégré, accessible aussi sur mobile.
3. **Évaluations** (`/evaluations`) — liste des évaluations ; sélection de l'évaluation active (persistée serveur pour reprise desktop↔mobile). Pour un rôle `unit` : « Mes auto-évaluations » + bouton « Nouvelle auto-évaluation ».
4. **Fiche évaluateur** (`/profil-evaluateur`)
5. **Fiche d'identité de l'unité** (`/unite`)
6. **Mandat d'évaluation** (`/mandat`)
7. **Physionomie du PC** (`/physionomie`) — avec graphiques.
8. **Critères** (`/criteres`) — arborescence repliable Domaine ▸ Module ▸ Critère ; moyennes et remplissage affichés à chaque niveau ; recherche, filtres par domaine/état/note ; saisie note + observation (auto-save avec debounce) ; pièces jointes ; switch « Pertinent ». Repliés par défaut quand la grille est volumineuse (1500+ critères), ouverture auto dès qu'un filtre est actif.
9. **Évaluation rapide** (`/evaluation-rapide`) — carousel « un critère à la fois » optimisé tactile : gros boutons de notes, raccourcis clavier (2–5 pour noter, ←/→ pour naviguer), sommaire latéral des domaines avec progression et saut direct, auto-save des observations (debounce 700 ms + sur blur).
10. **Tableau de bord** (`/tableau-de-bord`) — voir §5.
11. **Comparaison** (`/comparaison`) — 2 à 4 évaluations : moyennes pondérées, barres comparatives, radar superposé, tableau famille par famille avec écart max, export Excel, impression.
12. **Niveau et Label** (`/niveau-atteint`) — voir §6.
13. **Compte-Rendu et 3A** (`/compte-rendu`) — rédaction du compte rendu + bouton **« Générer 3A (PPTX) »** qui produit une présentation PowerPoint d'Analyse Après Action basée sur un modèle fourni (titre/date pré-remplis).
14. **Modèles** (`/modeles`) — bibliothèque de modèles de grilles de critères réutilisables.
15. **Paramètres** (`/parametres`) — **options d'affichage et d'ergonomie uniquement** : thème clair/sombre/système, taille du texte, densité d'affichage, réduction des animations, contraste élevé, état par défaut du menu latéral — appliqués en direct et persistés localement.
16. **Paramètres de l'évaluation** (`/parametres-evaluation`) — gestion des membres/évaluateurs et droits par domaine (cf. §2).
17. **Gestion des droits** (`/administration`, admin) — liste des utilisateurs, attribution des rôles (admin / évaluateur / visiteur / référent d'unité), protection du dernier admin.

Bandeau discret « Auto-évaluation » dans l'en-tête quand l'évaluation active est en mode `self`.

---

## 5. Tableau de bord (commun desktop et mobile)

- **Taux de remplissage général** et **par domaine**.
- **Moyenne pondérée générale** et **par domaine** (barres + radar).
- Distribution des notes (histogramme).
- Points forts / points faibles / points critiques.
- Top 5 / Bottom 5 des critères.
- Observations saisies.
- **Évolution dans le temps** (courbe à partir des snapshots quotidiens).
- Carte **« Résultat final — Niveau opérationnel atteint »**.

---

## 6. Niveau opérationnel et Label de l'exercice

### Niveau (basé sur la moyenne pondérée générale)
| Moyenne | Niveau | Mention |
|---|---|---|
| ≥ 4,5 | **5** | Aucune remise à niveau nécessaire |
| 4 à < 4,5 | **4** | Remise à niveau partielle recommandée |
| 3,5 à < 4 | **3** | Remise à niveau fortement recommandée |
| 3 à < 3,5 | **2** | Remise à niveau indispensable et en profondeur |
| < 3 | **1** | Non observé |

### Label (10 exigences cochables, certaines obligatoires)
Caractérise le type d'exercice sur lequel s'appuie l'évaluation, en complément du niveau :
1. MEDOT + production OPO1 < 96 h **(obligatoire)** — du Mission Brief N+1 à la diffusion de l'ordre aux subordonnés ;
2. Introduction de cas non conformes anticipés par l'HICON **(obligatoire)** ;
3. Exercice en environnement interarmées / interalliés ;
4. Gestion d'un flux logistique réaliste ;
5. Emploi des systèmes d'information et de communication en configuration dégradée ;
6. Conduite d'une phase de transition ;
7. Prise en compte du volet informationnel / communication opérationnelle ;
8. Gestion des effets du temps et des marges de manœuvre ;
9. Intégration d'éléments interministériels ou partenaires ;
10. Conduite d'un AAR / retour d'expérience formalisé.

Barème :
- 9 à 10 exigences validées → **label A**
- 7 à 8 → **label B**
- 5 à 6 → **label C**
- ≤ 4 ou exigences obligatoires non réalisées → **évaluation non validée**

Règles supplémentaires : une unité dont toutes les fonctions ne sont pas contrôlées ne peut prétendre qu'au label B (bascule à cocher). Le non-respect des critères obligatoires rétrograde l'exercice en simple observation.

**Résultat de l'exercice = Niveau + Label** (ex. « 5 A »), affiché sur la page Niveau et Label **et** sur la page d'accueil de l'évaluation. Les cases sont persistées par évaluation.

---

## 7. Deux versions : desktop complet / mobile lite

- **Détection automatique** de la largeur d'écran + **bascule manuelle** dans la barre latérale (préférence `auto | mobile | desktop`, persistée).
- **Version lite mobile** : navigation limitée à **Choix de l'évaluation, Évaluation rapide, Tableau de bord, Assistant IA**, plus le bouton de bascule et le bouton **Synchroniser** (recharge les données serveur avec retour visuel). Toute autre route redirige automatiquement vers la liste des évaluations.
- Périmètre mobile spécifique pour les référents d'unité : évaluations, accueil, fiche unité, physionomie, critères, tableau de bord.
- **Synchronisation multi-appareils** : la sélection de l'évaluation active est stockée côté serveur (profil) ; la saisie étant déjà persistée en base à chaque modification, l'utilisateur reprend exactement où il en était sur un autre appareil.
- Application **installable (PWA légère)** : manifest + icônes 192/512 (maskable), balises Apple ; pas de service worker de cache (éviter les problèmes de mises à jour) — un `sw.js` de nettoyage désinscrit les anciens workers.

---

## 8. Sécurité et technique

- Base PostgreSQL avec **RLS sur toutes les tables** : politiques filtrant par `mode`, `owner_id`, appartenance via `evaluation_members`, et `has_role` (security definer). GRANT explicites à `authenticated` / `service_role` sur chaque table publique ; aucun accès `anon` aux données métier.
- Fonctions security definer : `EXECUTE` révoqué d'`anon` et `PUBLIC` ; conservé pour `authenticated` uniquement sur les fonctions requises par les politiques RLS.
- Logique serveur via fonctions RPC typées (validation Zod des entrées) : création d'évaluation (admin) et d'auto-évaluation (rôle `unit`, force `mode='self'`), archivage/désarchivage/suppression (admin), mise à jour (RLS), snapshots, membres, préférences utilisateur.
- Authentification par e-mail ; gestion des utilisateurs et rôles côté serveur.
- Import/export : import de grilles (JSON), export Excel de la comparaison, impression des rapports.
- Checklist de rendu mobile automatisée (script parcourant chaque route à 320/375/414 px avec captures d'écran et rapport) pour détecter les régressions.

---

## 9. UX / design

- Interface en **français**, ton institutionnel (vocabulaire militaire : unité, PC, mandat, physionomie, remise à niveau).
- Design sobre et professionnel, thème clair/sombre, composants de type shadcn/ui + Tailwind.
- Auto-save généralisé avec indicateurs visuels ; confirmations pour les actions destructrices ; barres de progression partout où une saisie longue existe.
- Menu latéral repliable ; en-tête avec titre du module courant et mention de diffusion.

---

## 10. Données de démonstration

Prévoir une évaluation de démonstration (ex. « 7e BB ») avec une grille complète (plusieurs domaines/modules, ~50–1500 critères possibles) et une distribution de notes réaliste : **10 % de 5 · 40 % de 4,5 · 30 % de 4 · 10 % de 3,5 · 8 % de 3 · 2 % de 2,5**. Fonction admin « Réinitialiser la démo ».
