import sys, numpy as np, itertools
sys.path.insert(0, '.')
from r2_order3 import *
p = ((0, 0, 0), 0, 1)
P = [(n, i, j) for n in itertools.product(range(-2, 3), repeat=3) for i in range(3) for j in range(i + 1, 3)]
seen = set()
for q in P:
    if q == p or not (set(links_of(p)) & set(links_of(q))): continue
    for key, M in blocks_fast(product(W(p), W(q))).items():
        sv = np.linalg.svd(M, compute_uv=False); sv = sv[sv > 1e-9]
        vals = sorted(set(np.round(sv**2, 8)))
        sig = (tuple(j for _, j in key if j != 0.5), tuple((v, int(np.sum(np.abs(sv**2 - v) < 1e-6))) for v in vals))
        if sig not in seen:
            seen.add(sig); print("shared-link spin", sig[0], ": squared singular values (value, multiplicity):", sig[1], " trace norm", round(sv.sum(), 9))
