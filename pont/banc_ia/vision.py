import base64, json, sys, time, urllib.request
modele = sys.argv[1]
for chemin in sys.argv[2:]:
    img = base64.b64encode(open(chemin, "rb").read()).decode()
    corps = {"model": modele, "stream": False, "think": False, "options": {"temperature": 0.2},
             "messages": [{"role": "user", "images": [img], "content":
              "Tu es un habitant qui voit passer cette image sur un réseau social. Décris en 2 ou 3 phrases, en français, ce qu'elle montre "
              "(personnes, lieu, objets, texte lisible, ambiance), puis dis en une phrase ce qu'un lecteur en retiendrait."}]}
    t = time.time()
    r = json.load(urllib.request.urlopen(urllib.request.Request("http://localhost:11434/api/chat", json.dumps(corps).encode(), {"Content-Type": "application/json"}), timeout=600))
    print(f"--- {chemin.split('/')[-1]} ({time.time()-t:.1f} s, {r.get('prompt_eval_count')} jetons en entrée)\n{r['message']['content']}\n", flush=True)
