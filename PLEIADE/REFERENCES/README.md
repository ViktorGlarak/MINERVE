# RÉFÉRENCES — agent PLEIADE

Documents de référence **produits hors MINERVE** et déposés ici pour être consultables
par l'utilisateur comme par l'agent. Le fichier d'origine fait foi ; ce dossier n'en est
que le dépôt.

---

## `Pleiade-presentation.pdf` — la présentation de PLEIADE par Xavier

| | |
|---|---|
| **Auteur** | **Xavier** (le développeur de la plateforme) |
| **Nature** | **Draft** — présentation de l'idée générale de PLEIADE, orientée démonstration |
| **Créé le** | 2026-09-14 (métadonnées du PDF), remis le **2026-09-15** |
| **Format** | 19 pages, export navigateur depuis macOS |
| **Titre interne** | « Pléiade » |

> ⚠ **C'est un DRAFT, pas une spécification.** Les écrans qu'il montre sont des maquettes
> de présentation. Quand il contredit le code des dépôts (`C:\CECPC\pleiade\`), **c'est le
> code qui fait foi** — voir les écarts relevés plus bas.

### Le propos, en une phrase

> Déployer **en quelques minutes** un écosystème d'information complet et **étanche**
> (réseaux sociaux, presse, messageries) pour entraîner journalistes, communicants et
> analystes, là où les environnements d'exercice sont aujourd'hui « bricolés, dispersés et
> impossibles à reproduire d'un exercice à l'autre ».

### Ce que contient chaque page

| Pages | Contenu |
|---|---|
| 1–2 | Couverture · **le problème** : le métier se joue dans un espace numérique, il faut le reproduire |
| 3 | **Le catalogue** : réseaux sociaux (Facebook, Instagram, Twitter, YouTube), presse (pure player, quotidien, magazine, chaîne d'info), messagerie (Telegram, WhatsApp, Signal). *Plusieurs instances du même type sont possibles ; **les mêmes personnages y vivent avec la même identité partout*** |
| 4 | **La zone** = une bulle étanche par exercice. Capture de l'orchestrateur (zones `Littoral26` PROD, `Véga` DEV) |
| 5–8 | Les applications vues par le participant : **Facebook**, **Twitter**, **site de presse**, **messagerie** (canaux, groupes, privé — « là où une rumeur naît avant d'atteindre les réseaux ouverts ») |
| 9–11 | **ADMIN — les scénarios** : déroulé heure par heure (qui publie quoi, où, quand, en `T+hh:mm`), arbre/timeline, import-export **XLSX**, lancement et suspension, et ⭐ **greffe sur une publication existante — y compris écrite par un participant** |
| 12–15 | **COCKPIT** : veille multi-applications en un seul écran (relevé toutes les 10 s), **disposition personnelle** enregistrable/exportable comme espace de travail, **priorités par source** (critique/normal/basse) avec accusé de réception, puis **reporting** — comparaison des groupes de sources heure par heure, recherche, export |
| 16 | **Développeurs** : `pleiade deploy --zone <Zone>` — image, base, authentification Keycloak et routage fournis automatiquement |
| 17 | ⭐ **Sécurité** : réseau **fermé**, aucune adresse publique, rien d'indexable ; entrée par **profil VPN nominatif** (`.ovpn`), révocable individuellement. *« Un exercice de crise fabrique de fausses rumeurs et de faux communiqués. Ils doivent rester dans la salle. »* |
| 18–19 | **Les 4 arguments** : Réalisme · Rapidité · Isolation · Reproductibilité |

### ⚠ Écarts avec l'état consigné dans `../MEMOIRE.md`

1. **Nommage des domaines** : le PDF montre `*.<zone>.pleiade.local` (`littoral26.pleiade.local`,
   `facebook.littoral26.pleiade.local`). La mémoire et le code portent encore
   `*.mastorion.internal` / `*.cecpc.internal`. Cohérent avec le recadrage du 2026-09-11
   (« MASTORION est transitoire ») — **le renommage est donc en cours côté Xavier**.
2. **Le catalogue a grandi** : la mémoire annonçait 4 applications. Le dépôt en compte **8**
   (`admin`, `cockpit`, `eho`, `messagerie`, `presse`, `social`, `webserver`, `wordpress`) —
   et le PDF les montre toutes. `social` y remplace `mastorion`, `admin` et `cockpit` sont
   nouveaux. Mémoire corrigée le 2026-09-15.
3. **`admin` et `cockpit` sont des capacités majeures non documentées côté MINERVE** :
   l'orchestration de scénarios multi-applications (avec import XLSX et greffe sur
   l'existant) et la veille/reporting recoupent très directement le savoir MELMIL /
   MASTAURIGE. **À creuser** : ce que MINERVE sait des synchromatrices peut nourrir `admin`.

### Ce que ça confirme de notre travail EHO

L'EHO reste **la source d'identité des personas** (page 3 : « les mêmes personnages y
vivent, avec la même identité partout ») — exactement la liaison inter-instances déjà
consignée en `../MEMOIRE.md` § 6.
