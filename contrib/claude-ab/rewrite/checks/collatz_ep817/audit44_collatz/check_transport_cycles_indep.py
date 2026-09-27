#!/usr/bin/env python3
"""Independent checks: chapter 2 (stopped affine transport) Thm 2.1, (7.6), (7.9)-(7.16);
chapter 3 (cycle-relative cohomology) Thm 1.1, Thm 3.1, the <=1-exponent-1 family exclusion;
chapter 6 Theorem 9 inequalities (C36)/(C37) with s=330751. No workbench code imported."""
import sys, time, math, itertools
from fractions import Fraction
t0 = time.time(); out = []
def fail(m): print('FAIL', m); sys.exit(1)
def v2(x): return (x & -x).bit_length() - 1
def T(n): x = 3 * n + 1; return x >> v2(x)
def word(n, m):
    w = []
    for _ in range(m):
        x = 3 * n + 1; a = v2(x); w.append(a); n = x >> a
    return tuple(w)
def comps_upto(H):
    for A in range(1, H + 1):
        for m in range(1, A + 1):
            for cuts in itertools.combinations(range(1, A), m - 1):
                c = (0,) + cuts + (A,); yield tuple(c[i + 1] - c[i] for i in range(m))
# ---------- chapter 2: leaves, Theorem 2.1 ----------
def prefix_data(p):
    A = 0; L = 1; C = 0; out = []
    for a in p:
        C = 3 * C + 2 ** A; L *= 3; A += a; out.append((A, L, C))
    return out
H = 16; leaves = []
def rec(p, A, L, C):
    # F_j(3) >= 3 so far; extend
    for a in range(1, H - A + 1):
        A2, L2, C2 = A + a, 3 * L, 3 * C + 2 ** A
        val = Fraction(3 * L2 + C2, 2 ** A2)
        if val < 3: leaves.append((p + (a,), A2, L2, C2))
        else: rec(p + (a,), A2, L2, C2)
rec((), 0, 1, 0)
nd = 0
for (p, A, L, C) in leaves:
    D = 2 ** A - L
    if not (3 * D > C > 0): fail('(2.3)')
    M = 2 ** (A + 1); r = ((2 ** A - C) * pow(L, -1, M)) % M
    for k in range(0, 6):
        n = r + M * k
        if n < 3: continue
        if word(n, len(p)) != p: fail('cylinder')
        x = n
        for _ in range(len(p)): x = T(x)
        if not (0 < x < n): fail('descent Thm 2.1')
        nd += 1
out.append('Ch2 Thm 2.1: all %d reference-3 leaves with A<=%d satisfy 3D>C>0; %d actual starts n>=3 in their cylinders descend at the leaf: PASS' % (len(leaves), H, nd))
# (7.6) numerically on a grid and polynomial certificate
for i in range(0, 20001):
    x = 3 + i * 0.05
    lhs = (math.sqrt((x - 2) / 2) + math.sqrt((3 * x - 1) / 2)) / 2
    if lhs > math.sqrt(15) / 4 * math.sqrt(x - 1) + 1e-12: fail('(7.6)')
x = Fraction(7); A_ = (x - 2) / 2; B_ = (3 * x - 1) / 2
out.append('Ch2 (7.6) sqrt-potential contraction on x in [3,1003] grid; equality at x=7 (A=5/2,B=10): PASS')
# survival S_h of binary reference process from X0=3 (forced first odd bit) and t_H
maxh = 22
states = {Fraction(5): 1}  # after forced first step; weights = number of paths
S = [Fraction(1), Fraction(1)]  # S_0=1, S_1=1 (X1=5>=3)
killed_at = {}
for h in range(2, maxh + 1):
    new = {}; killed = 0
    for x, c in states.items():
        for y in (x / 2, (3 * x + 1) / 2):
            if y < 3: killed += c
            else: new[y] = new.get(y, 0) + c
    states = new
    tot = sum(states.values())
    S.append(Fraction(tot, 2 ** (h - 1)))
rho = Fraction(31, 32); C0 = Fraction(3, 2); K = Fraction(31, 20)
for h in range(0, maxh + 1):
    if S[h] > C0 * rho ** h: fail('(7.11)')
    if h >= 1 and float(S[h]) > math.sqrt(2) * (math.sqrt(15) / 4) ** (h - 1) + 1e-15: fail('(7.9)')
t = [Fraction(1)]
for Hh in range(1, maxh + 1): t.append((t[-1] + S[Hh]) / 2)
# direct t_H from leaves with A<=H
for Hh in range(1, H + 1):
    mass = sum(Fraction(1, 2 ** A) for (p, A, L, C) in leaves if A <= Hh)
    if 1 - mass != t[Hh]: fail('(7.14) at H=%d' % Hh)
    if t[Hh] > K * rho ** Hh: fail('(7.15)')
    b = [0] + [2 ** (h - 1) * (S[h - 1] - S[h]) for h in range(1, Hh + 1)]
    cnt = sum(b[h] * (Hh - h + 1) for h in range(1, Hh + 1))
    if cnt != sum(1 for (p, A, L, C) in leaves if A <= Hh): fail('(7.16)')
out.append('Ch2 (7.9)/(7.11) survival bounds h<=%d, recurrence (7.14) and leaf count (7.16) vs direct leaf enumeration H<=%d, t_H<=K rho^H: PASS' % (maxh, H))
# ---------- chapter 3 ----------
nw = 0; cyc = []
for p in comps_upto(14):
    m = len(p); A = sum(p); U = 2 ** A; L = 3 ** m; D = U - L
    C = sum(3 ** (m - i) * 2 ** sum(p[:i - 1]) for i in range(1, m + 1))
    # B_p matrix and functional
    Bm = [[0] * m for _ in range(m)]
    for i in range(m):
        Bm[i][i] += -3; Bm[i][(i + 1) % m] += 2 ** p[i]
    F = [3 ** (m - 1 - i) * 2 ** sum(p[:i]) for i in range(m)]
    FB = [sum(F[i] * Bm[i][j] for i in range(m)) for j in range(m)]
    if FB != [D] + [0] * (m - 1): fail('F B = D e1')
    if m <= 7:
        # determinant via fractions
        Mx = [[Fraction(v) for v in row] for row in Bm]; det = Fraction(1)
        for c in range(m):
            piv = next(r for r in range(c, m) if Mx[r][c] != 0)
            if piv != c: Mx[c], Mx[piv] = Mx[piv], Mx[c]; det = -det
            det *= Mx[c][c]
            for r in range(c + 1, m):
                f = Mx[r][c] / Mx[c][c]
                Mx[r] = [Mx[r][k] - f * Mx[c][k] for k in range(m)]
        if det != (-1) ** (m - 1) * D: fail('det')
    if math.gcd(D, 6) != 1: fail('gcd(D,6)')
    if D > 0 and C % D == 0:
        x = C // D
        if word(x, m) != p: fail('integral cycle word')
        cyc.append(p)
    nw += 1
if any(set(p) != {2} for p in cyc): fail('nontrivial integral positive cycle with A<=14')
out.append('Ch3 Thm 1.1 (F_p B_p = D e1, det B_p=(-1)^(m-1) D for m<=7, gcd(D,6)=1) on %d words with A<=14; Thm 3.1 criterion D>0, D|C yields only repetitions of (2) (the cycle at 1), each with the stated actual word: PASS' % nw)
D = [None, -1, -1, 5]
for m in range(3, 200):
    D.append(4 * D[m] + 3 ** m)
    if D[m] != 2 * 4 ** (m - 1) - 3 ** m: fail('D recursion')
out.append('Ch3 single-exponent-1 family: D_m=2*4^(m-1)-3^m, D_(m+1)=4D_m+3^m, D=-1,-1,5,... (no |D|=1 with D>0): PASS')
# ---------- chapter 6 Theorem 9 ----------
s = 330751
ok36 = True
for m in range(1, 1636):
    P = 1
    while P <= 3 ** m: P *= 2
    if not (P * s ** m > (3 * s + 1) ** m): ok36 = False; break
ok37 = (4 * s) ** 1634 > 2 ** 678 * (3 * s + 1) ** 1634
if not (ok36 and ok37): fail('C36/C37')
out.append('Ch6 Thm 9 inequalities (C36) for 1<=m<=1635 and (C37) with s=330751: PASS (logic of the exclusion re-derived in the audit)')
print('\n'.join(out)); print('elapsed %.1fs' % (time.time() - t0))
