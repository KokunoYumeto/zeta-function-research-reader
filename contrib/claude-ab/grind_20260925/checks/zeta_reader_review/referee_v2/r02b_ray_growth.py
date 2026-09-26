#!/usr/bin/env python3
"""Referee v2, script r02b.  Growth of an explicit L(w) = Lambda(K_w) on the ray arg w = pi/4.

K_w(s) = e^{t s^2} (e^w - e^{(1-s)w})/s  (reader's Prop 3.11, step 1); Lambda(F) = sum_{|k|<=K} F(ik)/(1+k^2),
a continuous functional on B (|Lambda(F)| <= C b_{0,0}(F)).  The reader's step 2 gives
log|L(u+iv)| <= v^2/(4t) + O(|u|) + O(log|v|); on the ray w = r e^{i pi/4}, v = r/sqrt 2, so the bound is
r^2/(8t) + O(r).  We print log|L(r e^{i pi/4})| - r^2/(8t) (it must be O(r)) and, for comparison,
log|L(i v)| - v^2/(4t) on the imaginary axis (bounded above, attained up to lower-order terms).
"""
import mpmath as mp
mp.mp.dps = 40
t = mp.mpf('0.2'); K = 400
def L(w):
    tot = w * mp.exp(w)                         # k = 0: K_w(0) = w e^w
    for k in range(1, K + 1):
        for s in (mp.mpc(0, k), mp.mpc(0, -k)):
            tot += mp.exp(t * s * s) * (mp.exp(w) - mp.exp((1 - s) * w)) / s / (1 + k * k)
    return tot
ok = True
print("ray arg w = pi/4:")
vals = []
for r in (10, 20, 40, 60):
    w = r * mp.expj(mp.pi / 4)
    d = mp.log(abs(L(w))) - r * r / (8 * t)
    vals.append(d / r)
    u = r / mp.sqrt(2)
    print(f"  r = {r:3d}: log|L| - r^2/(8t) = {mp.nstr(d, 8)},  divided by r: {mp.nstr(d / r, 6)},  minus u = r cos(pi/4): {mp.nstr(d - u, 6)}")
ok &= max(vals) < 1 / mp.sqrt(2) + 0.05   # the bound: excess <= (1+A)|u| + O(log r), A = 0 here
print("imaginary axis:")
for v in (10, 20, 40, 60):
    d = mp.log(abs(L(mp.mpc(0, v)))) - v * v / (4 * t)
    print(f"  v = {v:3d}: log|L(iv)| - v^2/(4t) = {mp.nstr(d, 8)}")
print(("[PASS] " if ok else "[FAIL] ") + "on the ray the excess over r^2/(8t) is O(r) (excess/r bounded)")
print("ALL CHECKS PASS" if ok else "SOME CHECKS FAILED")
