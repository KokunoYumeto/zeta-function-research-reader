import sys, itertools
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
    sh = [Ls[a] & Ls[b], Ls[a] & Ls[c], Ls[b] & Ls[c]]
    nadj = sum(1 for x in sh if x)
    if nadj == 3:
        return "common-edge" if (sh[0] == sh[1] == sh[2]) else "corner"
    if nadj == 2: return "path"
    return "disconnected"
cnt = {}; cls = {}
for L in labels3:
    t = typ(L)
    if t == "disconnected": continue
    cnt[t] = cnt.get(t, 0) + 1
    c = canon(L)[0]
    cls.setdefault(t, set()).add(c)
print("anchored counts:", cnt, "total", sum(cnt.values()))
print("classes:", {t: len(v) for t, v in cls.items()})
