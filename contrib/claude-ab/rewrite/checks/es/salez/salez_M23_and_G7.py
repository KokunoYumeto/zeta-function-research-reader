#!/usr/bin/env python3
"""Classes not covered by any single Salez modular equation, at M23 = 840*11*19*23 and at Salez's G7.
Uses es_families.py / coverage.py (referee pass B).  Calibration: Salez reports 147,348 residues at G7."""
import sys, os, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from es_families import families_dividing, check_identity
from coverage import Domain
S840 = [1, 121, 169, 289, 361, 529]
def crt(res, mods):
    x, m = 0, 1
    for r, q in zip(res, mods):
        t = ((r - x) * pow(m, -1, q)) % q
        x += m * t; m *= q
    return x % m
def issq(c, q): return pow(c % q, (q - 1) // 2, q) == 1
t0 = time.time()
L1 = 840 * 11 * 19 * 23
fams = families_dividing(L1)
D = Domain(L1); D.add_families(fams, record=False)
surv = [c for s in S840 for x in range(1, 11) for y in range(1, 19) for z in range(1, 23)
        for c in [crt([s, x, y, z], [840, 11, 19, 23])] if not D.cov[D.coord(c)]]
sq = [c for c in surv if all(issq(c, q) for q in (11, 19, 23))]
print(f"M23: families with modulus | M23: {len(fams)}; uncovered base classes: {len(surv)} = {len(sq)} square + {len(surv)-len(sq)} non-square")
for p0 in (3361, 18481, 2840041, 1201):
    cov = [(t, par, m) for (t, par, m, rs) in fams if (p0 % m) in rs]
    ok = all(check_identity(t, par, p0) for (t, par, m) in cov)
    print(f"  {p0}: covered by {len(cov)} families (identities valid at p0: {ok})" + (f", e.g. {cov[0]}" if cov else ""))
G7 = 840 * 11 * 13 * 17 * 19 * 23
D7 = Domain(G7); D7.add_families(families_dividing(G7), record=False)
n_all = int(D7.cov.size); n_cov = int(D7.cov.sum())
print(f"G7 = {G7}: classes = 1 (24) that are units: {n_all}; uncovered: {n_all - n_cov} (Salez: 147,348)")
print(f"time {time.time()-t0:.0f}s")
