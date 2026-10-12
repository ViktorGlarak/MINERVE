---
name: feedback-avatar-langue
description: "Règle : la langue d'un tweet doit correspondre à la langue établie de l'avatar (sa bio / ses tweets existants) — vérifier avant d'écrire"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 9cd755be-0651-44f5-8932-5974a21bced9
---

Quand on écrit un tweet pour un avatar AURIGE, **sa langue doit correspondre à celle déjà établie pour ce compte** (bio + tweets existants). Ne pas écrire en français un avatar dont le compte est en anglais (et inversement), **sauf intention explicite**.

**Why:** le 02/06, les tweets `07.05.12Bi/Ci` (@S_Tikhanov, @A_Saniki) ont été écrits en français alors que ces comptes s'expriment en **anglais** → incohérence relevée par l'utilisateur. Corrigés en anglais.

⚠ **RÉVISION 04/06/2026 — les MÉGAPHONES officiels pro-MER passent en ANGLAIS** (infosphère internationale). L'utilisateur a tranché : les voix officielles/analystes pro-MER s'expriment en **anglais**, contrairement aux avatars **civils camouflés** locaux (DAC/Lorraine) qui restent en **français**. Ceci **annule** la désignation FR de `@HmunikVoice` du 02/06.

**How to apply :** avant de rédiger, **vérifier la langue des tweets existants de l'avatar dans `tweets_data.js`** (grep le handle). Langues établies :
- **Anglais** : `@HmunikVoice`, `@KolesnikovAndrei`, `@MaiaKovalenko` (mégaphones/analystes officiels pro-MER — **basculés EN le 04/06**, cf. tweets 07.01.04Fi/Gi/Hi) ; `@S_Tikhanov`, `@A_Saniki` (opposition RB, audience internationale) ; `@EastWatch_Intl`, `@BelovDimitri`, `@GromovaYelena`, `@IndependentArnish`.
- **Français** : `@clambroise55`, `@VoixDACia`, `@TemoignageDAC`, `@MarionKessler57` (civils francophones camouflés DAC/Lorraine — ciblent l'opinion locale).
- Médias : TM/BC1 = anglais ; **TV4 = français** ; HEXAGONE/TF1/Omerta = français ; **ZubrRadio.FM = français** (radio francophone visant le front intérieur FR).

> ⚠ **Conséquence du basculement 04/06** : les tweets de `@HmunikVoice`/`@KolesnikovAndrei`/`@MaiaKovalenko` **antérieurs au 04/06 restent en français** (avatars temporairement bilingues) — à retraduire en anglais si l'utilisateur le demande, sinon les laisser.

Voir [[mastaurige]]. En cas de doute sur un avatar, demander à l'utilisateur plutôt que de trancher.
