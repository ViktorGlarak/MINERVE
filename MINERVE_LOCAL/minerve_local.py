# -*- coding: utf-8 -*-
"""
============================================================
 MINERVE Local — assistant de CONSULTATION (LECTURE SEULE)
 cf. vault/decisions/DECISION-011.md
------------------------------------------------------------
 RAG local 100% Ollama : interroge en français le corpus MINERVE
 (mémoires agents, countrybooks, doctrine ILI, décisions vault,
 injects GUILLAUME 2BB / MINAUTORE 7BB...) SANS tokens Claude, hors-ligne.

 ⚠ LECTURE SEULE : ce script NE MODIFIE/NE CRÉE AUCUNE donnée du projet.
   Il lit le corpus, l'indexe (vecteurs), et répond en CITANT ses sources.

 Usage :
   # indexer le corpus public (tout IA\\MINERVE) :
   python minerve_local.py index
   # discuter :
   python minerve_local.py chat
   # (utilisateur uniquement) collection SÉGRÉGUÉE des fiches bio sensibles —
   #   CLAUDE N'OUVRE JAMAIS ce dossier ni le .pkl résultant :
   python minerve_local.py index --root "D:\\CECPC\\DOC REF\\MERCURE\\RENS\\01_Fiches bio" --collection fiches_bio

 Modèles (Ollama) : réponse = mistral-nemo (FR) · embeddings = bge-m3 (multilingue).
   bge-m3 pas encore tiré ? -> `ollama pull bge-m3` (ou --embed nomic-embed-text en attendant).
============================================================
"""
import os, sys, re, json, glob, pickle, argparse, urllib.request
import numpy as np

OLLAMA      = "http://localhost:11434"
EMBED_MODEL = "nomic-embed-text"   # rapide sur ce poste. bge-m3 (meilleur FR) testé = ~2,2 s/embed -> trop lent
                                   #   pour l'indexation en masse ici ; le garder pour un ré-index « qualité » offline.
CHAT_MODEL  = "mistral-nemo:latest"
HERE        = os.path.dirname(os.path.abspath(__file__))
INDEX_DIR   = os.path.join(HERE, "index")
PUBLIC_ROOT = os.path.dirname(HERE)   # = IA\MINERVE
TOPK        = 6
CHUNK       = 1100
OVERLAP     = 150
# dossiers exclus du corpus public (générés/dup/techniques)
SKIP_PARTS  = [os.sep + p + os.sep for p in (
    ".git", "__pycache__", "node_modules", "MINERVE_LOCAL",
    os.path.join("vault", "_vues"), os.path.join("vault", "context-packs"),
    os.path.join("vault", "agents"),
)] + [os.sep + "index" + os.sep]

# ---------- Ollama (urllib, pas de dépendance requests) ----------
def _post(path, payload, timeout):
    req = urllib.request.Request(OLLAMA + path, json.dumps(payload).encode("utf-8"),
                                 {"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode("utf-8"))

def embed(text, model):
    return _post("/api/embeddings", {"model": model, "prompt": text}, 120)["embedding"]

def chat_llm(system, user, model=CHAT_MODEL):
    out = _post("/api/chat", {"model": model, "stream": False,
                              "messages": [{"role": "system", "content": system},
                                           {"role": "user", "content": user}]}, 600)
    return out["message"]["content"]

# ---------- découpage markdown ----------
def chunk_text(txt):
    paras = re.split(r"\n\s*\n", txt)
    chunks, cur = [], ""
    for p in (x.strip() for x in paras):
        if not p:
            continue
        if len(cur) + len(p) + 2 <= CHUNK:
            cur = (cur + "\n\n" + p) if cur else p
        else:
            if cur:
                chunks.append(cur); cur = ""
            if len(p) <= CHUNK:
                cur = p
            else:
                for i in range(0, len(p), CHUNK - OVERLAP):
                    chunks.append(p[i:i + CHUNK])
    if cur:
        chunks.append(cur)
    return chunks

# ---------- indexation ----------
def cmd_index(root, collection, embed_model):
    files = sorted(glob.glob(os.path.join(root, "**", "*.md"), recursive=True))
    files = [f for f in files if not any(s in f for s in SKIP_PARTS)]
    if not files:
        print("Aucun .md trouvé sous", root); return
    embs, meta = [], []
    for fi, f in enumerate(files):
        try:
            txt = open(f, encoding="utf-8").read()
        except Exception:
            continue
        rel = os.path.relpath(f, PUBLIC_ROOT) if collection == "public" else os.path.basename(f)
        for ch in chunk_text(txt):
            try:
                embs.append(embed(ch, embed_model)); meta.append({"source": rel, "text": ch})
            except Exception as ex:
                print("  embed KO:", ex)
        print("[%d/%d] %s  (%d chunks cumulés)" % (fi + 1, len(files), rel, len(meta)))
    if not embs:
        print("Aucun embedding produit."); return
    arr = np.asarray(embs, dtype=np.float32)
    arr /= (np.linalg.norm(arr, axis=1, keepdims=True) + 1e-9)
    os.makedirs(INDEX_DIR, exist_ok=True)
    out = os.path.join(INDEX_DIR, collection + ".pkl")
    with open(out, "wb") as fo:
        pickle.dump({"emb": arr, "meta": meta, "model": embed_model}, fo)
    print("OK collection '%s' : %d chunks (modèle %s) -> %s" % (collection, len(meta), embed_model, out))

# ---------- récupération ----------
def load_collections():
    cols = []
    for f in sorted(glob.glob(os.path.join(INDEX_DIR, "*.pkl"))):
        with open(f, "rb") as fo:
            cols.append((os.path.basename(f)[:-4], pickle.load(fo)))
    return cols

def retrieve(query, k=TOPK):
    cols = load_collections()
    if not cols:
        print("Aucun index. Lance d'abord :  python minerve_local.py index"); return []
    model = cols[0][1].get("model", EMBED_MODEL)
    qe = np.asarray(embed(query, model), dtype=np.float32); qe /= (np.linalg.norm(qe) + 1e-9)
    hits = []
    for _, c in cols:
        sims = c["emb"] @ qe
        for i in np.argsort(-sims)[:k]:
            hits.append((float(sims[i]), c["meta"][i]["source"], c["meta"][i]["text"]))
    hits.sort(key=lambda x: -x[0])
    return hits[:k]

SYSTEM = (
    "Tu es MINERVE Local, assistant de CONSULTATION (LECTURE SEULE) du projet MINERVE. "
    "Réponds en FRANÇAIS, de façon concise et factuelle, UNIQUEMENT à partir du CONTEXTE fourni "
    "(extraits du corpus). CITE toujours le ou les fichiers source entre crochets, ex. [ANALYSTE/MERCURE/MEMOIRE.md]. "
    "Si l'information n'est pas dans le contexte, dis-le clairement plutôt que d'inventer. "
    "Tu n'écris jamais dans les fichiers : tu informes seulement."
)

def cmd_chat():
    print("=== MINERVE Local — consultation (LECTURE SEULE). Tape 'quit' pour sortir. ===")
    while True:
        try:
            q = input("\n❓ ").strip()
        except EOFError:
            break
        if q.lower() in ("quit", "exit", "q", ""):
            break
        hits = retrieve(q)
        if not hits:
            continue
        ctx = "\n\n".join("[%s]\n%s" % (s, t) for _, s, t in hits)
        try:
            ans = chat_llm(SYSTEM, "CONTEXTE :\n" + ctx + "\n\nQUESTION : " + q)
        except Exception as ex:
            print("Erreur modèle:", ex); continue
        print("\n" + ans)
        print("\n— sources : " + ", ".join(sorted({s for _, s, _ in hits})))

if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="MINERVE Local — RAG de consultation (lecture seule, Ollama).")
    sub = ap.add_subparsers(dest="cmd")
    pi = sub.add_parser("index", help="indexer un corpus")
    pi.add_argument("--root", default=PUBLIC_ROOT)
    pi.add_argument("--collection", default="public")
    pi.add_argument("--embed", default=EMBED_MODEL)
    sub.add_parser("chat", help="discuter avec le corpus indexé")
    a = ap.parse_args()
    if a.cmd == "index":
        cmd_index(a.root, a.collection, a.embed)
    elif a.cmd == "chat":
        cmd_chat()
    else:
        ap.print_help()
