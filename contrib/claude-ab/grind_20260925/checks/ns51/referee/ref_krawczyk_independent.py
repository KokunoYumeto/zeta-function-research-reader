#!/usr/bin/env python3
"""ref_krawczyk_independent.py -- independent re-verification of the Krawczyk condition K_i in int(A_i) for the certified
cells of certify_hydro_radius.py, using a different interval library (mpmath.iv, see ivG.py), a different number of
series terms (36 instead of 30) and an independently derived tail bound.  The alpha-boxes A_i, centres c_i and the
actual x-boxes X_i are read exactly from cells_dump.pkl; the preconditioner Y_i is recomputed (any Y works).

usage: python3 ref_krawczyk_independent.py <part> <nparts>   (cells i with i % nparts == part)
For each cell it also checks that the independent enclosure K'_i meets the certificate's K_i (both contain the zero).
"""
import sys, pickle, time
import mpmath
from mpmath import iv, mp
import ivG

mp.dps = 40
part = int(sys.argv[1]) if len(sys.argv) > 1 else 0
nparts = int(sys.argv[2]) if len(sys.argv) > 2 else 1
limit = int(sys.argv[3]) if len(sys.argv) > 3 else None
D = pickle.load(open('cells_dump.pkl', 'rb'))
cells = D['cells']
idxs = [i for i in range(len(cells)) if i % nparts == part]
if limit:
    idxs = idxs[:limit]
T0 = time.time()
bad = []; nomeet = []; nsub_used = {}
for n, i in enumerate(idxs):
    cl = cells[i]
    A = ivG.ivbox(cl['A']); X = ivG.ivbox(cl['X']); c = ivG.ivbox(cl['c'])
    x0 = mp.mpc(X.real.mid, X.imag.mid)
    cpt = mp.mpc(c.real.mid, c.imag.mid)
    _, ga0 = ivG.point_G_Ga(cpt, x0)
    Yp = 1 / ga0
    Y = iv.mpc(Yp.real, Yp.imag)
    Gc, _ = ivG.G_Ga(c, X, deriv=False)
    ok = False
    for nsub in (1, 3, 6):
        # enclosure of {G_alpha(alpha, x): alpha in A, x in X} as the rectangular hull of sub-box enclosures
        GaA = None
        ra, rb = A.real.a, A.real.b; ia, ib = A.imag.a, A.imag.b
        # sub-box endpoints: the exact end values of A at both ends, one shared value at each interior cut,
        # so the sub-boxes cover A exactly (no rounding gaps)
        pr = [ra] + [ra + (rb - ra) * p / nsub for p in range(1, nsub)] + [rb]
        pi_ = [ia] + [ia + (ib - ia) * p / nsub for p in range(1, nsub)] + [ib]
        for p in range(nsub):
            for q in range(nsub):
                sub = iv.mpc(iv.mpf([pr[p], pr[p + 1]]), iv.mpf([pi_[q], pi_[q + 1]]))
                _, g = ivG.G_Ga(sub, X)
                GaA = g if GaA is None else iv.mpc(iv.mpf([min(GaA.real.a, g.real.a), max(GaA.real.b, g.real.b)]),
                                                   iv.mpf([min(GaA.imag.a, g.imag.a), max(GaA.imag.b, g.imag.b)]))
        K = c - Y * Gc + (1 - Y * GaA) * (A - c)
        if ivG.contains_interior(A, K):
            ok = True; nsub_used[nsub] = nsub_used.get(nsub, 0) + 1
            break
    if not ok:
        bad.append(i)
    Kc = ivG.ivbox(cl['K'])
    meet = (max(K.real.a, Kc.real.a) <= min(K.real.b, Kc.real.b) and max(K.imag.a, Kc.imag.a) <= min(K.imag.b, Kc.imag.b))
    if not meet:
        nomeet.append(i)
print(f"part {part}/{nparts}: {len(idxs)} cells re-verified in {time.time()-T0:.0f}s (alpha-box subdivision used: {nsub_used}); Krawczyk failures: {len(bad)} {bad[:5]}; "
      f"K' and K disjoint: {len(nomeet)} {nomeet[:5]}")
print("PASS" if not bad and not nomeet else "FAIL")
