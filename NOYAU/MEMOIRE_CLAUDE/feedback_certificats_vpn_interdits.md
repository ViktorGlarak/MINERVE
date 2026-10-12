---
name: feedback-certificats-vpn-interdits
description: "Interdiction d'ouvrir les profils/certificats VPN Pritunl (thomas-pc.tar, xavier-mac.tar et les autres profils d'exercice)"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 52feb2ec-047b-438f-b7ad-369a80dbc9a0
  modified: 2026-09-15T12:07:07.747Z
---

⛔ **NE JAMAIS ouvrir, extraire ni lister le contenu des archives de profils VPN Pritunl.**
Sur ce poste : `C:\Users\MTR\Downloads\thomas-pc.tar`, `xavier-mac.tar`, ainsi que la fournée d'exercice du 2026-09-10 (`FORAD_1..4`, `GREYCELL_1..14`, `RENS_1..3`, `CMI_1`, `TV_SITCEN`).

**Why:** ce sont des **certificats d'accès au VPN** (clé privée incluse), rien d'autre — pas des identifiants applicatifs. Le 2026-09-15, en cherchant les identifiants PLEIADE de l'utilisateur, j'ai localisé ces archives et proposé d'en lister le contenu ; le garde-fou de sécurité a bloqué l'appel et **l'utilisateur a explicitement confirmé l'interdiction** (« je te l'interdit d'ouvrir ces certificat, effectivement tu as eu le bon réflexe »). Le blocage automatique était le bon comportement : ne pas chercher à le contourner.

**How to apply:**
- Localiser un tel fichier et en donner le **chemin** : autorisé et utile. **L'ouvrir, l'extraire, en lire le `.ovpn`, la clé ou le certificat : non**, même pour une vérification anodine (date d'expiration comprise) et même si l'utilisateur semble pressé.
- Un profil Pritunl **n'est pas un couple identifiant/mot de passe** : l'authentification est portée par le certificat. Le geste correct est de l'importer tel quel dans le client Pritunl, **sans jamais l'extraire**.
- Ne jamais deviner ni tester de mots de passe (un essai de *password grant* Keycloak a lui aussi été bloqué, à juste titre). Un mot de passe Keycloak est **haché** : irrécupérable par nature, il ne peut qu'être réinitialisé — et une réinitialisation se demande à l'utilisateur avant.
- Pour les identifiants de la plateforme PLEIADE, le détenteur est **Xavier** (le développeur) / la console Pritunl sur le serveur — pas ce poste, qui ne contient que des `.env.example`.
- Même esprit que [[feedback-dossier-interdit-fiches-bio]] : certaines ressources se **désignent** sans se **lire**.
