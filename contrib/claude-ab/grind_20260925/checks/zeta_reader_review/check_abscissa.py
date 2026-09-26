#!/usr/bin/env python3
"""Check for the finding on reader Prop 5.1 ("positivity returns the largest real part").

For ANY finite multiset S in C with positive integer weights m and ANY k >= 1,
  D_S^{(k)}(s) = sum_n (sum_rho m_rho n^rho)^k n^{-s} = sum_w c_w zeta(s - w),  c_w = sum over k-tuples with sum w of prod m > 0,
so the continuation has poles exactly at 1 + w with nonzero residues c_w, the rightmost on Re s = 1 + k beta_max.
A Dirichlet series cannot converge to the left of a pole of its continuation, and it converges absolutely for
Re s > 1 + k beta_max; hence sigma_c = sigma_a = 1 + k beta_max.  Positivity (even k, conjugation-stable S)
is needed only for Landau's conclusion that the REAL point 1 + k beta_max is a pole.
Below: exact grouping for three configurations, and the partial-sum growth left of the abscissa.
"""
import itertools, collections, mpmath as mp
mp.mp.dps = 20
def grouping(S, k):
    c = collections.Counter()
    for tup in itertools.product(S.items(), repeat=k):
        w = sum(r for r, _ in tup)
        c[complex(round(w.real, 10), round(w.imag, 10))] += int(mp.fprod([m for _, m in tup]))
    return c
ok = True
configs = {
    "conjugation-stable quartet, k = 3 (odd)": ({complex(0.7, 10): 1, complex(0.7, -10): 1, complex(0.3, 10): 1, complex(0.3, -10): 1}, 3),
    "conjugation-stable quartet, k = 4 (even)": ({complex(0.7, 10): 1, complex(0.7, -10): 1, complex(0.3, 10): 1, complex(0.3, -10): 1}, 4),
    "NOT conjugation-stable, weights 2 and 1, k = 3": ({complex(0.7, 10): 2, complex(0.3, 25): 1}, 3),
}
for name, (S, k) in configs.items():
    c = grouping(S, k)
    bmax = max(r.real for r in S)
    top = {w: v for w, v in c.items() if abs(w.real - k*bmax) < 1e-9}
    real_pole = any(abs(w.imag) < 1e-9 for w in top)
    print(f"{name}: beta_max = {bmax}; all c_w > 0: {all(v > 0 for v in c.values())}; "
          f"poles on Re s = 1 + k beta_max = {1 + k*bmax:.2f}: {sorted((round(w.imag,3), v) for w, v in top.items())}; real point is a pole: {real_pole}")
    ok &= all(v > 0 for v in c.values()) and len(top) > 0
    # identity check at a point of absolute convergence: truncated series vs sum c_w zeta(s-w)
    s = mp.mpf(1 + k*bmax + 3)
    lhs = mp.nsum(lambda n: (mp.fsum(m*mp.power(n, mp.mpc(r.real, r.imag)) for r, m in S.items()))**k*mp.power(n, -s), [1, mp.inf], method='direct', steps=[20000])
    rhs = mp.fsum(v*mp.zeta(s - mp.mpc(w.real, w.imag)) for w, v in c.items())
    print(f"    identity at s = {s}: |series - sum c_w zeta(s-w)| / |.| = {mp.nstr(abs(lhs - rhs)/abs(rhs), 3)}")
    ok &= abs(lhs - rhs)/abs(rhs) < 1e-3
# oscillation of partial sums on dyadic windows: grows like N^{0.3} left of the abscissa 3.1 (sigma = 2.8),
# decays like N^{-0.3} right of it (sigma = 3.4); no real pole is needed for the divergence (odd k).
import numpy as np
S, k = configs["conjugation-stable quartet, k = 3 (odd)"]
n = np.arange(1, 2**17 + 1, dtype=float)
coef = sum(m*np.exp(complex(r)*np.log(n)) for r, m in S.items())**k
for sig in (2.8, 3.4):
    ps = np.cumsum((coef*n**(-sig)).real)
    ranges = []
    for N0 in (2**11, 2**13, 2**15, 2**16):
        w = ps[N0 - 1:2*N0]
        ranges.append(w.max() - w.min())
    print(f"sigma = {sig}: range of partial sums on [N0, 2N0], N0 = 2^11, 2^13, 2^15, 2^16:", [f"{x:.3f}" for x in ranges])
    if sig < 3.1:
        ok &= ranges[-1] > 1.5*ranges[0]
    else:
        ok &= ranges[-1] < ranges[0]
print("\nALL CHECKS PASS" if ok else "\nSOME CHECK FAILED")
