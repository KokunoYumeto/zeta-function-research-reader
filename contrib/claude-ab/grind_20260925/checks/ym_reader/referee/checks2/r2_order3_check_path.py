import sys, time
sys.argv = ['x']
sys.path.insert(0, '.')
exec(open('./r2_order3_run.py').read().split("if len(sys.argv) > 1")[0])
done = 0
for c, members in sorted(classes.items()):
    rep = members[0]
    if typ(rep) == "path":
        t0 = time.time()
        a = sorted((tuple(k), round(v, 8)) for k, v in class_data(rep))
        b = sorted((tuple(k), round(v, 8)) for k, v in class_data(rep, general=True))
        print("path", rep, "fast == general:", a == b, f"{time.time()-t0:.1f}s", flush=True)
        done += 1
        if done == 2: break
