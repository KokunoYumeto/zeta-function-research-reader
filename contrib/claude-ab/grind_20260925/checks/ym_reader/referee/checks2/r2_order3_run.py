# Driver: exact m(v3), t(v3), ||v3||_loc at the anchor (see r2_order3.py for the definitions).
# Paths and corners (distinct faces, every link at most twice): v3[L] = sum_s alpha_s P_s(W_p W_q W_r) with
#   alpha_s = (2/3) sum_{splits (r, S={p,q}), p~q} x^S_{b} (3 + c^S_b - c_s)/(2 c_s),  x^S_b = (2/9)(6 - c^S_b)/(2 c^S_b),
# b = spin of s on the link p∩q.  Other classes use the general split sum v3_cluster().  Usage: python3 r2_order3_run.py [check]
import sys, itertools, time, json
sys.path.insert(0, '.')
from r2_order3 import *

anchor = ((0, 0, 0), 0); R = 3
P = [(n, i, j) for n in itertools.product(range(-R, R + 1), repeat=3) for i in range(3) for j in range(i + 1, 3)]
Ls = {p: set(links_of(p)) for p in P}
near = [p for p in P if max(abs(x) for x in p[0]) <= 2]
adj = {p: [q for q in P if q != p and Ls[p] & Ls[q]] for p in near}
A0 = [p for p in P if anchor in Ls[p]]
labels3 = set()
for a in A0:
    for y in [a] + adj[a]:
        for z in set([a, y] + adj[a] + adj.get(y, [])):
            labels3.add(tuple(sorted((a, y, z))))
def typ(L):
    U = sorted(set(L))
    if len(U) == 1: return "self"
    if len(U) == 2: return "repeated"
    a, b, c = U
    sh = [Ls.get(a, set(links_of(a))) & Ls.get(b, set(links_of(b))), Ls.get(a, set(links_of(a))) & Ls.get(c, set(links_of(c))), Ls.get(b, set(links_of(b))) & Ls.get(c, set(links_of(c)))]
    nadj = sum(1 for x in sh if x)
    if nadj == 3: return "common-edge" if (sh[0] == sh[1] == sh[2]) else "corner"
    if nadj == 2: return "path"
    return "disconnected"
labels3 = [L for L in labels3 if typ(L) != "disconnected"]
classes = {}
for L in labels3: classes.setdefault(canon(L)[0], []).append(L)

def fast_cluster(L):
    f = W(L[0])
    for x in L[1:]: f = product(f, W(x))
    bl = blocks_fast(f)
    out = {}
    lk = [set(links_of(x)) for x in L]
    for key, M in bl.items():
        cs = casimir(key)
        if cs == 0: continue
        spin = dict(key); alpha = 0.0
        for idx in range(3):
            r = L[idx]; S = [L[k] for k in range(3) if k != idx]
            sh = set(links_of(S[0])) & set(links_of(S[1]))
            if not sh: continue
            (e,) = tuple(sh)
            b = spin[e]
            cSb = 6 * 0.75 + b * (b + 1)
            xS = (2.0 / 9.0) * (6 - cSb) / (2 * cSb)
            alpha += (2.0 / 3.0) * xS * (3 + cSb - cs) / (2 * cs)
        if abs(alpha) > 1e-15: out[key] = alpha * M
    return out

def class_data(rep, general=False):
    t = typ(rep)
    bl = v3_cluster(rep) if (general or t not in ("path", "corner")) else fast_cluster(rep)
    return [(key, tnorm(M)) for key, M in bl.items() if tnorm(M) > 1e-12]

if len(sys.argv) > 1 and sys.argv[1] == "check":
    for c, members in sorted(classes.items()):
        rep = members[0]
        if typ(rep) in ("path", "corner"):
            t0 = time.time()
            a = sorted((tuple(k), round(v, 8)) for k, v in class_data(rep))
            b = sorted((tuple(k), round(v, 8)) for k, v in class_data(rep, general=True))
            print(typ(rep), "fast == general:", a == b, f"{time.time()-t0:.1f}s", flush=True)
            if typ(rep) == "corner": break
    sys.exit()

t0 = time.time()
res = {}
for ci, (c, members) in enumerate(sorted(classes.items())):
    t1 = time.time()
    res[c] = class_data(members[0])
    print(f"class {ci+1}/{len(classes)} {typ(members[0])}: {len(members)} anchored, {len(res[c])} blocks, {time.time()-t1:.1f}s", flush=True)

def transport(rep, L):
    for g in G:
        im = [g_plaq(g, p) for p in rep]
        for q0 in im:
            tvec = tuple(L[0][0][k] - q0[0][k] for k in range(3))
            if sorted((tuple(x + y for x, y in zip(q[0], tvec)), q[1], q[2]) for q in im) == sorted(L):
                return g, tvec
    raise AssertionError(L)
m3 = t3 = l3 = 0.0; per = {}
for c, members in classes.items():
    rep = members[0]; data = res[c]
    Mv = sum(sum(j for _, j in key) * nr for key, nr in data); Lv = sum(casimir(key) * nr for key, nr in data)
    for L in members:
        g, tvec = transport(rep, L)
        mapl = lambda l: (tuple(x + y for x, y in zip(g_link(g, l)[0], tvec)), g_link(g, l)[1])
        Tv = sum(dict((mapl(l), j) for (l, j) in key).get(anchor, 0) * nr for key, nr in data)
        m3 += Mv; t3 += Tv; l3 += Lv
        pt = per.setdefault(typ(rep), [0, 0.0, 0.0, 0.0]); pt[0] += 1; pt[1] += Lv; pt[2] += Mv; pt[3] += Tv
print(f"\norder 3 at the anchor: m(v3) = {m3:.10f}, t(v3) = {t3:.10f}, ||v3||_loc = {l3:.10f}")
print("workbench F26: m3 =", 336572872 / 208845, " t3 =", 225985217 / 1253070, " C23 bound on ||v3||_loc:", 944984 / 351)
print("per type [count, loc, m, t]:", {k: [v[0]] + [round(x, 6) for x in v[1:]] for k, v in per.items()})
print("C21 per-cluster loc bounds x counts:", {"self": 4 * 40 / 27, "repeated": 84 * 66 / 13, "path": 460 * 1408 / 351, "common-edge": 40 * 512 / 117, "corner": 24 * 3504 / 351})
json.dump({str(c): [[list(map(list, key)), nr] for key, nr in d] for c, d in res.items()}, open('./r2_order3_classdata.json', 'w'))
print(f"total {time.time()-t0:.1f}s")
