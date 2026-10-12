import sys, time, concurrent.futures as cf
sys.argv = ["x"]; exec(open("vitesse.py").read().split("for m in sys.argv")[0])
m = "gemma4:26b-a4b-it-qat"; run(m)
for n in (1, 2, 4):
    t = time.time()
    with cf.ThreadPoolExecutor(n) as ex: list(ex.map(lambda _: run(m), range(n * 2)))
    d = time.time() - t
    print(f"{n} en parallèle : {n*2} lectures en {d:5.1f} s → {d/(n*2):4.1f} s par lecture en moyenne, soit {3600*n*2/d:5.0f} lectures/heure", flush=True)
