#!/usr/bin/env python3
"""Referee v2, script r08.  Prop 5.2 (average weight of a quartet), corrected at on-line zeros.

On the jet block of a zero of multiplicity m the dilation is W_p = p^rho exp((log p) N), N the nilpotent shift
of size m (reader, Section 3.3).  V_rho = span of the blocks of the DISTINCT points among rho, conj rho, 1-rho,
1-conj rho.  Weight w(alpha) = 2 log|alpha|/log p.
 1. Off-line rho: 4 distinct points, rank 4m, det = p^{2m}, w(det)/rank = 1.
 2. On-line rho: 1 - rho = conj rho, 2 distinct points, rank 2m, det = p^m, w(det)/rank = 1.
 3. The version-1 wording (rank 4m, det p^{2m}) would count each on-line block twice.
"""
import mpmath as mp
mp.mp.dps = 40
ok_all = True
def rep(name, cond, info=""):
    global ok_all
    ok_all &= bool(cond); print(("[PASS] " if cond else "[FAIL] ") + name + ("" if not info else ": " + str(info)))
def block(p, rho, m):
    N = mp.matrix(m, m)
    for i in range(m - 1): N[i, i + 1] = 1
    E = mp.expm(mp.log(p) * N)
    return mp.power(p, rho) * E
def Wp_on(points, p, m):
    blocks = [block(p, z, m) for z in points]
    n = m * len(blocks); W = mp.matrix(n, n)
    for b, B in enumerate(blocks):
        for i in range(m):
            for j in range(m): W[b * m + i, b * m + j] = B[i, j]
    return W
def distinct(pts):
    out = []
    for z in pts:
        if all(abs(z - y) > 1e-20 for y in out): out.append(z)
    return out
res = []
for p in (2, 7, 11):
    for m in (1, 2, 3):
        for rho, kind in ((mp.mpc('0.7', '21.3'), 'off'), (mp.mpc('0.5', '14.134725141734693790'), 'on')):
            pts = distinct([rho, mp.conj(rho), 1 - rho, 1 - mp.conj(rho)])
            W = Wp_on(pts, p, m)
            d = mp.det(W); rank = W.rows
            wt = 2 * mp.log(abs(d)) / mp.log(p)
            res.append((kind, p, m, len(pts), rank, d, wt / rank))
off = [r for r in res if r[0] == 'off']; on = [r for r in res if r[0] == 'on']
rep("1  off-line: 4 points, rank 4m, det = p^{2m}, average weight 1",
    all(r[3] == 4 and r[4] == 4 * r[2] and abs(r[5] - mp.mpf(r[1])**(2 * r[2])) < 1e-25 * r[1]**(2*r[2]) and abs(r[6] - 1) < 1e-30 for r in off))
rep("2  on-line: 2 points, rank 2m, det = p^m, average weight 1",
    all(r[3] == 2 and r[4] == 2 * r[2] and abs(r[5] - mp.mpf(r[1])**r[2]) < 1e-25 * r[1]**r[2] and abs(r[6] - 1) < 1e-30 for r in on),
    [(r[1], r[2], r[4], mp.nstr(mp.re(r[5]), 12)) for r in on if r[1] == 7])
pts4 = [mp.mpc('0.5', 14), mp.conj(mp.mpc('0.5', 14)), 1 - mp.mpc('0.5', 14), 1 - mp.conj(mp.mpc('0.5', 14))]
rep("3  at an on-line zero the four expressions give only two points (1 - rho = conj rho, 1 - conj rho = rho)",
    len(distinct(pts4)) == 2)
print("ALL CHECKS PASS" if ok_all else "SOME CHECKS FAILED")
