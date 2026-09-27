#!/usr/bin/env python3
"""es50_support_core.py -- an independent re-implementation (claude-ab) of the two computations in the
author's report "Finite Central-Cover Reductions for Residual Erdos--Straus Shells":

  (1) the divisor-visible elementary j=1 sieve over the shells R | M, R = 3 (mod 4), M = 840*11*19*23;
  (2) the support closure over all P-smooth shells, P = {3,5,7,11,19,23}, with the certificate congruence
      tested modulo gcd(M, R) (a class is "supported" by R when some lift of it modulo lcm(M, R) is certified).

Elementary j=1 certificate (R, m, u): R = 3 mod 4, u | m^2, n = -R (mod 4m), n = -4u (mod R), gcd(n, R) = 1.
Base classes: n = r (mod 840) with r in S840, and n a unit modulo 11, 19, 23 (23,760 classes).
A prime l of {2,3,5,7,11,19,23} is available for (R, class) when l does not divide R and n = -R (mod 4l)
(mod 8 for l = 2); u runs over the products of l^0, l^1, l^2 over the available l.
Expected (the report): 4951 classes survive (1); 2970 = S840 x Q11 x Q19 x Q23 are unsupported in (2).
"""
import time
from math import gcd
from itertools import product
import numpy as np

T0 = time.time()
S840 = [1, 289, 361, 169, 121, 529]
M = 840 * 11 * 19 * 23
MODD = 3 * 5 * 7 * 11 * 19 * 23
BASE = [2, 3, 5, 7, 11, 19, 23]
ODD = [3, 5, 7, 11, 19, 23]

def crt(res, mods):
    x, m = 0, 1
    for r, q in zip(res, mods):
        t = ((r - x) * pow(m, -1, q)) % q
        x += m * t; m *= q
    return x % m

cls = np.array([crt([s, x, y, z], [840, 11, 19, 23]) for s in S840 for x in range(1, 11)
                for y in range(1, 19) for z in range(1, 23)], dtype=np.int64)
assert len(cls) == 23760
res = {q: cls % q for q in ODD}
box_cache = {}
def box(g, mask):
    key = (g, mask)
    if key not in box_cache:
        s = {1 % g}
        for i, l in enumerate(BASE):
            if mask >> i & 1:
                s = {(v * pow(l, e, g)) % g for v in s for e in (0, 1, 2)}
        arr = np.zeros(g, dtype=bool)
        arr[list(s)] = True
        box_cache[key] = arr
    return box_cache[key]

def hits_for_state(rho, idx):
    """boolean array over classes cls[idx]: supported by the shell state rho (R mod M)."""
    g = 1
    for q in ODD:
        if rho % q == 0: g *= q
    c = cls[idx]
    mask = np.zeros(len(idx), dtype=np.int64)
    if rho % 8 == 7:                      # 2 | a for every class (c = 1 mod 8)
        mask |= 1
    for i, q in enumerate(BASE[1:], start=1):
        if rho % q == 0: continue
        mask |= ((res[q][idx] + rho) % q == 0).astype(np.int64) << i
    if g == 1:
        return np.ones(len(idx), dtype=bool)      # modulo 1 every target is hit
    t = ((-c) * pow(4, -1, g)) % g
    out = np.zeros(len(idx), dtype=bool)
    for mval in np.unique(mask):
        sel = mask == mval
        out[sel] = box(g, int(mval))[t[sel]]
    return out

# (1) divisor-visible sieve: states R | M with R odd, R = 3 (mod 4)
visible = sorted(d for d in (np.prod([q for q, b in zip(ODD, bits) if b]) for bits in product((0, 1), repeat=6))
                 if d % 4 == 3)
alive = np.ones(len(cls), dtype=bool)
for R in visible:
    idx = np.nonzero(alive)[0]
    h = hits_for_state(int(R), idx)
    alive[idx[h]] = False
n_visible = int(alive.sum())
print(f"(1) divisor-visible shells: {len(visible)}; survivors {n_visible} (report: 4951)", flush=True)

# (2) semigroup of P-smooth residue states modulo M
seen = {1}; frontier = [1]
while frontier:
    nxt = []
    for r in frontier:
        for q in ODD:
            s = (r * q) % M
            if s not in seen:
                seen.add(s); nxt.append(s)
    frontier = nxt
states = sorted(r for r in seen if r % 4 == 3)
print(f"(2) semigroup size {len(seen)} (report: 45139); states = 3 mod 4: {len(states)} (report: 22074)", flush=True)
supported = ~alive.copy()               # visible deletions are supported (indeed covered)
for rho in states:
    idx = np.nonzero(~supported)[0]
    if len(idx) == 0: break
    h = hits_for_state(rho, idx)
    supported[idx[h]] = True
unsup = cls[~supported]
print(f"    unsupported classes: {len(unsup)} (report: 2970)", flush=True)
def is_sq(c, q):
    return pow(int(c) % q, (q - 1) // 2, q) == 1
core = [c for c in cls if all(is_sq(c, q) for q in (11, 19, 23))]
print(f"    equal to S840 x Q11 x Q19 x Q23 ({len(core)} classes): {sorted(core) == sorted(int(c) for c in unsup)}")
print(f"    time {time.time() - T0:.1f}s")
