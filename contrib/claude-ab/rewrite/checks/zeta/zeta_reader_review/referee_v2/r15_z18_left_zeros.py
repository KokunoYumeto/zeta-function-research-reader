#!/usr/bin/env python3
"""Referee v2, script r15.  Illustration for composite q (Prop 2.8's left side beyond prime q): q = 8 and q = 12.
Phi_{1/q}(s) = 2 q^{-s} sum_{r=1}^{q} cos(2 pi r/q) zeta(s, r/q).  Locate zeros s0 of Phi_{1/q} with 1/2 < Re s0 < 1
(grid of |Phi| minima refined by findroot) and check that 1 - s0 is a zero of Z_{1/q} = zeta(s,1/q) + zeta(s,1-1/q),
with 0 < Re(1 - s0) < 1/2 (left of the critical line).  Numerical illustration only; the theorem is Saias-Weingartner
applied to Phi_{1/q}, whose zeta- and nontrivial components are both nonzero for phi(q) > 2 (script r12)."""
import mpmath as mp
mp.mp.dps = 25
def Phi(q, s):
    return 2 * mp.power(q, -s) * mp.fsum(mp.cos(2 * mp.pi * r / q) * mp.zeta(s, mp.mpf(r) / q) for r in range(1, q + 1))
def Z(q, s):
    return mp.zeta(s, mp.mpf(1) / q) + mp.zeta(s, 1 - mp.mpf(1) / q)
ok = True
for q in (8, 12):
    found = []
    for T0 in range(2, 60, 2):
        best = None
        for re in [0.55 + 0.05 * i for i in range(9)]:
            for im in [T0 + 0.25 * j for j in range(8)]:
                v = abs(Phi(q, mp.mpc(re, im)))
                if best is None or v < best[0]: best = (v, mp.mpc(re, im))
        try:
            s0 = mp.findroot(lambda s: Phi(q, s), best[1])
        except Exception:
            continue
        if 0.5 + 1e-6 < mp.re(s0) < 1 and mp.im(s0) > 1 and abs(Phi(q, s0)) < 1e-15 and all(abs(s0 - f) > 1e-8 for f in found):
            found.append(s0)
    checks = [(s0, abs(Z(q, 1 - s0))) for s0 in found]
    good = [c for c in checks if c[1] < 1e-12]
    print(f"q = {q}: zeros of Phi with 1/2 < Re < 1 found: {len(found)}; e.g. " + ", ".join(mp.nstr(s0, 10) for s0 in found[:4]))
    print(f"        |Z_(1/q)(1 - s0)| at them: max {mp.nstr(max(c[1] for c in checks), 3) if checks else '-'}; left-of-line zeros of Z: " + ", ".join(mp.nstr(1 - s0, 10) for s0, _ in good[:4]))
    ok &= len(good) >= 2
print(("[PASS] " if ok else "[FAIL] ") + "Z_{1/8} and Z_{1/12} have zeros with 0 < Re s < 1/2, reflected from zeros of Phi_{1/q} right of the line")
print("ALL CHECKS PASS" if ok else "SOME CHECKS FAILED")
