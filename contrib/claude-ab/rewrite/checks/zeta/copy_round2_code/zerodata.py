#!/usr/bin/env python3
"""Compute certified zeros rho_n = 1/2 + i gamma_n (Arb isolates them on the
critical line), zeta'(rho_n) and zeta(rho_n + 1), for n in [n0, n0+count).
Output: npz with gamma (float64), zp (complex128), z1 (complex128),
plus max radius of the Arb enclosures for audit."""
import sys, time
import numpy as np
from flint import acb, ctx, acb_series

n0 = int(sys.argv[1]); count = int(sys.argv[2]); out = sys.argv[3]
ctx.prec = 80
block = 500
gam = np.empty(count); zp = np.empty(count, dtype=complex); z1 = np.empty(count, dtype=complex)
maxrad = 0.0
t0 = time.time()
k = 0
while k < count:
    m = min(block, count - k)
    zs = acb.zeta_zeros(n0 + k, m)
    for j, r in enumerate(zs):
        # r is 0.5 + i*gamma exactly on the line (Arb certifies this)
        d = acb_series([r, 1]).zeta()[1]
        w = (r + 1).zeta()
        gam[k + j] = float(r.imag.mid())
        zp[k + j] = complex(float(d.real.mid()), float(d.imag.mid()))
        z1[k + j] = complex(float(w.real.mid()), float(w.imag.mid()))
        maxrad = max(maxrad, float(d.real.rad()), float(d.imag.rad()), float(r.imag.rad()))
    k += m
    print(f"{n0+k-1} done, gamma={gam[k-1]:.3f}, elapsed {time.time()-t0:.1f}s, maxrad {maxrad:.2e}", flush=True)
np.savez(out, n0=n0, gamma=gam, zp=zp, z1=z1, maxrad=maxrad)
print("saved", out, flush=True)
