import json, urllib.request, time, sys
ctx = ("Tu es Radek Muller, 44 ans, libraire à Toul, père de deux enfants, modéré, attaché à sa ville. "
       "Voici les dernières publications de ton fil : ")
fil = " ".join(f"[@habitant{i}] La route de Nancy est encore coupée ce matin, les camions militaires passent sans arrêt, on attend des explications de la préfecture. Certains disent que Mercure prépare quelque chose, d'autres parlent de rumeurs. #Toul #Info" for i in range(30))
inv = ctx + fil + "\nRéagis en une ou deux phrases naturelles, en français, comme sur un réseau social. Réponds en JSON {\"pensee\":..., \"message\":...}."
def run(model):
    body = {"model": model, "messages": [{"role": "user", "content": f"[lecture {time.time_ns()}] " + inv}], "stream": False, "think": False,
            "format": "json", "options": {"num_ctx": 8192, "temperature": 0.8, "num_predict": 220}}
    req = urllib.request.Request("http://localhost:11434/api/chat", json.dumps(body).encode(), {"Content-Type": "application/json"})
    t = time.time(); r = json.load(urllib.request.urlopen(req, timeout=600)); d = time.time() - t
    pe, pc = r.get("prompt_eval_count", 0), r.get("eval_count", 0)
    pd, ed = r.get("prompt_eval_duration", 1) / 1e9, r.get("eval_duration", 1) / 1e9
    return d, pe, pe / pd, pc, pc / ed, r["message"]["content"][:160]
for m in sys.argv[1:]:
    run(m)  # chauffe (chargement)
    for i in range(3):
        d, pe, ps, pc, ts, txt = run(m)
        print(f"{m:24} total {d:5.1f} s | entrée {pe} jetons à {ps:6.0f}/s | sortie {pc} jetons à {ts:5.1f}/s | {txt!r}", flush=True)
    urllib.request.urlopen(urllib.request.Request("http://localhost:11434/api/generate", json.dumps({"model": m, "keep_alive": 0}).encode()))
