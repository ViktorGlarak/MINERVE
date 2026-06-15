---
description: Rituel de FIN de session de travail MINERVE (vault)
---

Je termine ma session de travail sur **MINERVE**. Exécute le **rituel de clôture du vault** (cf. `vault/CLAUDE.md`) :

1. **Daily du jour** : mets à jour (ou crée depuis `vault/templates/daily-note.md`) `vault/daily/<AAAA-MM-JJ>.md` avec :
   - 🎯 l'objet de la session, ✅ ce qui a avancé,
   - 🧩 les décisions/leçons (avec les `[[notes]]` créées ou modifiées),
   - 📝 les **fichiers autoritaires modifiés** (ex. `ANALYSTE/<pays>/MEMOIRE.md`, `MASTAURIGE/MEMOIRE.md`),
   - ⏭️ surtout la **« Prochaine étape »** (pour la reprise).
2. **Notes atomiques** : pour toute connaissance durable apparue aujourd'hui (décision, outil, leçon, architecture, **entité/persona**, savoir countrybook `reference`), crée la note depuis le template adapté (`vault/templates/`), **frontmatter complet** (cf. `vault/_SCHEMA.md`), `source:` vers le fichier autoritaire + liens `[[...]]`. ⚠ Un **`camp:`** ne se met **QUE** dans une note `entity`.
3. **Build + validation** : lance **`py vault/_tools/build.py`** — il DOIT sortir en **exit 0** (régénère agents/packs/index/vues + valide liens, orphelins, duplications et **cohérence des camps**). Corrige si rouge.
4. **Bilan + commit** : résume-moi ce qui a été consigné, puis **propose un commit** (avec message clair) — **ne commit pas sans mon accord**.
