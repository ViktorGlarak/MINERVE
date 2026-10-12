"""Rejoue les invites réelles du moteur (pont/banc_ia/NN_*.json) sur un ou plusieurs modèles Ollama.
Usage : python3 -I banc.py gemma4:26b-a4b-it-qat gemma4:31b-it-qat  → resultats_<modele>.json"""
import json, glob, sys, time, urllib.request, os
ici = os.path.dirname(os.path.abspath(__file__))
def appel(corps):
    req = urllib.request.Request("http://localhost:11434/api/chat", json.dumps(corps).encode(), {"Content-Type": "application/json"})
    t = time.time(); r = json.load(urllib.request.urlopen(req, timeout=900)); return time.time() - t, r
for modele in sys.argv[1:]:
    appel({"model": modele, "messages": [{"role": "user", "content": "ok"}], "stream": False, "think": False, "options": {"num_predict": 1}})
    res = []
    for f in sorted(glob.glob(os.path.join(ici, "[01][0-9]_*.json"))):
        d = json.load(open(f)); meta = d.pop("meta"); d["model"] = modele; d["stream"] = False
        duree, r = appel(d)
        txt = r["message"]["content"]
        try: json.loads(txt); lisible = True
        except Exception: lisible = False
        res.append({"fichier": os.path.basename(f), "type": meta["type_appel"], "duree_s": round(duree, 1), "duree_pc_s": round(meta["duree_ms_pc"] / 1000, 1),
                    "jetons_invite": r.get("prompt_eval_count"), "jetons_reponse": r.get("eval_count"), "json_lisible": lisible,
                    "reponse": txt, "reponse_pc_26b": meta["reponse_gemma4"]})
        print(f"{modele:24} {os.path.basename(f):42} {duree:6.1f} s (PC {meta['duree_ms_pc']/1000:5.1f} s) json={'ok' if lisible else 'ILLISIBLE'}", flush=True)
    json.dump(res, open(os.path.join(ici, f"resultats_{modele.replace(':', '_')}.json"), "w"), ensure_ascii=False, indent=1)
    urllib.request.urlopen(urllib.request.Request("http://localhost:11434/api/generate", json.dumps({"model": modele, "keep_alive": 0}).encode()))
