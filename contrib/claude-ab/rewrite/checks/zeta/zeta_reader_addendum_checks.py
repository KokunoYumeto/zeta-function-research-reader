#!/usr/bin/env python3
"""Checks for note 48_ (addendum to the published zeta reader), claude-ab, Opus 5.5, 26 September 2026.
Independent of the reviewer's and the verifier's scripts. Items:
Z1 (F1) the first Hurwitz jet on other sheets: d/da zeta(s,a) = -s zeta(s+1,a); vanishes at s0-1 for zeros s0 of zeta(.,a).
Z2 (F2) transfer-compatible forms: with n = 2, 3 the admissible entries (rho, eta) are exactly eta = rho# on a synthetic configuration.
Z3 (F3) the Carleman sum for S = {2^a 3^b}: sum_{log n < R}(1/log n - log n/R^2) / R -> (4/3) kappa, kappa = 1/(2 log 2 log 3);
    threshold t* = log2 log3 / (2 pi); the growth quadratic coefficient 1/(4t) via sup_tau (1+|tau|)^M e^{-t tau^2 + tau v}.
Z4 (F4) r_n = 1 - j + eps at divisor-minimal elements (all proper M-divisors uniquely factored) of the Hilbert monoid 1 mod 4.
Z5 (F5) the abscissa example: k = 3, S = {0.7 +- 10i, 0.3 +- 10i}: all c_w > 0, no real w with Re w = 3*beta_max.
Z6 (O1) det(W_p | V_rho) for an on-line zero: rank 2m, det = p^m, average weight 1.
Z7 (section 7.1) the angle |arg w| < pi/4: sector identity, constants, lattice sum 2 kappa log X + O(1).
Z8 (section 7.2) composite moduli in Prop. 2.8: the decomposition of Phi_{1/8}; zeros of Z_{1/8}, Z_{1/12} left of the line."""
import itertools, math
from fractions import Fraction as Fr
from collections import Counter, defaultdict
import mpmath as mp
res = []
def ok(name, cond, info=""):
    res.append(cond); print(("[PASS] " if cond else "[FAIL] ") + name + (": " + str(info) if info != "" else ""))

mp.mp.dps = 30
# Z1
worst = 0
for a0 in (mp.mpf('0.3'), mp.mpf('0.5'), mp.mpf(2), mp.mpf('3.7')):
    for s in (mp.mpc('0.2', '5'), mp.mpc('-1.3', '2.2'), mp.mpc('0.7', '-14')):
        lhs = mp.diff(lambda a: mp.zeta(s, a), a0)
        rhs = -s * mp.zeta(s + 1, a0)
        worst = max(worst, abs(lhs - rhs) / abs(rhs))
s0 = mp.findroot(lambda s: mp.zeta(s, 2), mp.mpc('1.40779', '23.32799'))
jet_at = mp.diff(lambda a: mp.zeta(s0 - 1, a), 2)
val0 = [mp.limit(lambda s: s * mp.zeta(s + 1, a0), 0) for a0 in (mp.mpf('0.3'), mp.mpf(2))]
ok("Z1 d/da zeta(s,a) = -s zeta(s+1,a) on four sheets; the a-jet vanishes at s0 - 1 for the zero s0 of zeta(.,2) near 1.408+23.328i; s zeta(s+1,a) -> 1 at s = 0",
   worst < 1e-15 and abs(jet_at) < 1e-15 and all(abs(v - 1) < 1e-15 for v in val0), f"max rel. error {mp.nstr(worst, 3)}, s0 = {mp.nstr(s0, 12)}, |jet| = {mp.nstr(abs(jet_at), 3)}")

# Z2: synthetic #- and conjugation-stable configuration; entries allowed by n = 2 and n = 3
cfg = [mp.mpc('0.5', '14.134725'), mp.mpc('0.5', '-14.134725'), mp.mpc('0.5', '21.022040'), mp.mpc('0.5', '-21.022040'),
       mp.mpc('0.7', '30'), mp.mpc('0.3', '30'), mp.mpc('0.7', '-30'), mp.mpc('0.3', '-30'),
       mp.mpc('0.5', '40'), mp.mpc(mp.mpf('0.5'), 40 + 2 * mp.pi / mp.log(2))]
sharp = lambda r: 1 - mp.conj(r)
def allowed(ns):
    out = set()
    for i, r in enumerate(cfg):
        for j, e in enumerate(cfg):
            if all(abs(mp.power(n, r + mp.conj(e) - 1) - 1) < 1e-20 for n in ns): out.add((i, j))
    return out
A23 = allowed((2, 3)); A2 = allowed((2,))
pairs = {(i, j) for i, r in enumerate(cfg) for j, e in enumerate(cfg) if abs(e - sharp(r)) < 1e-20}
offline = {(i, j) for (i, j) in pairs if i != j}
ok("Z2 transfer relation for n = 2 and 3 allows exactly the entries (rho, rho#) (10: six on-line diagonal, four off-line (rho, rho#) with rho# != rho); n = 2 alone allows more (a pair 2 pi/log 2 apart)", A23 == pairs and len(pairs) == 10 and len(offline) == 4 and len(A2) > len(A23), f"{len(A23)} entries for n = 2, 3 ({len(offline)} off the diagonal); {len(A2)} for n = 2")

# Z3
kappa = 1 / (2 * math.log(2) * math.log(3))
def carleman_sum(R):
    tot = 0.0
    for a in range(0, int(R / math.log(2)) + 2):
        for b in range(0, int(R / math.log(3)) + 2):
            if a + b == 0: continue
            x = a * math.log(2) + b * math.log(3)
            if x < R: tot += 1 / x - x / R**2
    return tot
ratios = [carleman_sum(R) / ((4 / 3) * kappa * R) for R in (100, 400, 1600)]
tstar = math.log(2) * math.log(3) / (2 * math.pi)
# growth: sup_tau (1+|tau|)^M e^{-t tau^2 + tau v} vs e^{v^2/(4t)}: the log difference is O(M log v)
t = 0.2; M = 3
diffs = []
for v in (10.0, 20.0, 40.0, 80.0):
    taus = [v / (2 * t) + k * 0.01 for k in range(-2000, 2001)]
    sup = max(M * math.log(1 + abs(tau)) - t * tau**2 + tau * v for tau in taus)
    diffs.append(sup - v * v / (4 * t) - M * math.log(1 + v / (2 * t)))
ok("Z3 Carleman sum for {2^a 3^b} is (4/3) kappa R (1 + o(1)); threshold t* = log2 log3/(2 pi) = 0.12120; the quadratic growth coefficient is 1/(4t) (the remainder is O(M log v))",
   abs(ratios[-1] - 1) < 0.02 and abs(tstar - 0.12120) < 5e-5 and max(abs(d) for d in diffs) < 1.0, f"ratios {[round(r, 4) for r in ratios]}, t* = {tstar:.6f}, growth remainders {[round(d, 3) for d in diffs]}")

# Z4: Hilbert monoid 1 mod 4: formal logarithm coefficients r_n and factorizations
LIM = 4000
M4 = [n for n in range(5, LIM + 1) if n % 4 == 1]
Mset = set(M4)
atoms = []
for n in M4:
    if not any(n % d == 0 and d in Mset and (n // d) in Mset for d in M4 if d * d <= n and d < n): atoms.append(n)
Aset = set(atoms)
fact = defaultdict(set)   # n -> set of sorted atom tuples
fact[1].add(())
for n in [1] + M4:
    pass
for n in M4:
    for u in atoms:
        if u > n: break
        if n % u == 0 and (n // u == 1 or (n // u) in Mset):
            for f in fact[n // u]:
                fact[n].add(tuple(sorted(f + (u,))))
# T_k(n): ordered k-tuples of elements > 1 of M with product n
from functools import lru_cache
@lru_cache(maxsize=None)
def T(k, n):
    if k == 1: return 1 if n in Mset else 0
    return sum(T(k - 1, n // d) for d in M4 if d < n and n % d == 0 and (n // d) in Mset)
def r(n):
    tot = Fr(0); k = 1
    while 5**k <= n:
        tot += Fr((-1)**(k + 1), k) * T(k, n); k += 1
    return tot
bad = 0; tested = 0; neg = 0
for n in M4:
    pdiv = [d for d in M4 if d < n and n % d == 0 and (n // d) in Mset]
    if all(len(fact[d]) == 1 for d in pdiv):
        j = len(fact[n])
        eps = sum(Fr(1, len(f)) for f in fact[n] if len(set(f)) == 1)
        expected = (1 - j + eps) if j >= 2 else eps
        tested += 1
        if r(n) != expected: bad += 1
        if j >= 2: neg += 1
ok("Z4 r_n = 1 - j + eps (j >= 2) and r_n = eps (j = 1) at every element of the Hilbert monoid below 4000 whose proper M-divisors factor uniquely", bad == 0, f"{tested} elements, {neg} of them with j >= 2")

# Z5
S = [mp.mpc(0.7, 10), mp.mpc(0.7, -10), mp.mpc(0.3, 10), mp.mpc(0.3, -10)]
cw = Counter()
for tup in itertools.product(range(4), repeat=3):
    w = sum(S[i] for i in tup)
    cw[(round(float(w.real), 9), round(float(w.imag), 9))] += 1
top = [w for w in cw if abs(w[0] - 2.1) < 1e-9]
ok("Z5 k = 3, S = {0.7 +- 10i, 0.3 +- 10i}: all c_w > 0; the rightmost poles 1 + w have Re = 3.1 and none is real", all(c > 0 for c in cw.values()) and top and all(abs(w[1]) > 1 for w in top), sorted(top))

# Z6: on-line zero rho = 1/2 + i gamma with multiplicity m: V_rho spanned by the blocks of rho and rho-bar
p = 7; m = 3; gam = mp.mpf('14.134725')
rho = mp.mpc(0.5, gam)
eig = [mp.power(p, rho)] * m + [mp.power(p, mp.conj(rho))] * m
det = mp.fprod(eig)
ok("Z6 on-line zero: rank 2m, det(W_p | V_rho) = p^m, average weight 1", abs(det - p**m) < 1e-20 and abs(2 * mp.log(abs(det)) / mp.log(p) / (2 * m) - 1) < 1e-20)

# Z7 (section 7.1): the angle |arg w| < pi/4 step, the sector identity, and the lattice sum
def sector_identity(kv):
    al = mp.pi/(2*kv)
    I1 = mp.quad(lambda ph: mp.sin(ph)**2*mp.cos(kv*ph), [-al, al])
    return (4 - kv**2)*I1 + 2*kv*mp.sin(al)**2 - 4/kv
idres = max(abs(sector_identity(mp.mpf(kv))) for kv in ('0.5', '1', '1.5', '1.9', '2'))
arc = mp.quad(lambda ps: mp.sin(ps/2)**2*mp.cos(ps), [-mp.pi/2, mp.pi/2])
def S2(X):
    tot = 0.0
    for a in range(0, int(X/math.log(2)) + 2):
        for b in range(0, int(X/math.log(3)) + 2):
            if a + b == 0: continue
            x = a*math.log(2) + b*math.log(3)
            if x < X: tot += x**-2 - x**2/X**4
    return tot
lat = [S2(X) - 2*kappa*math.log(X) for X in (100.0, 400.0, 800.0)]
t2 = math.log(2)*math.log(3)/(4*math.pi)
ok("Z7 sector identity (4-k^2)int sin^2 cos k + 2k sin^2(pi/2k) = 4/k (k = 0.5..2); arc constant 1 - pi/4; the angle sum is 2 kappa log X + O(1); threshold (log2)(log3)/(4 pi) = 0.060598",
   idres < 1e-25 and abs(arc - (1 - mp.pi/4)) < 1e-25 and abs(lat[-1] - lat[-2]) < 0.02 and abs(t2 - 0.060598) < 1e-6, f"identity residual {mp.nstr(idres, 3)}, S2 - 2 kappa log X = {[round(v, 4) for v in lat]}, t = {t2:.6f}")

# Z8 (section 7.2): composite moduli in Prop. 2.8
def PhiA(a, s): return mp.polylog(s, mp.exp(2j*mp.pi*a)) + mp.polylog(s, mp.exp(-2j*mp.pi*a))
chi8 = [0, 1, 0, -1, 0, -1, 0, 1]
dec = max(abs(PhiA(mp.mpf(1)/8, s) - (mp.sqrt(2)*mp.dirichlet(s, chi8) - 2*mp.power(4, -s)*(1 - mp.power(2, 1 - s))*mp.zeta(s)))/abs(PhiA(mp.mpf(1)/8, s)) for s in (mp.mpc(2.5, 1), mp.mpc(3, -7)))
Za = lambda s, a: mp.zeta(s, a) + mp.zeta(s, 1 - a)
zs = []
for (a, g) in ((mp.mpf(1)/8, mp.mpc('0.2527', '-7.8196')), (mp.mpf(1)/12, mp.mpc('0.2285', '-6.5307'))):
    s0 = mp.findroot(lambda s: Za(s, a), g); zs.append((s0, abs(PhiA(a, 1 - s0))))
ok("Z8 Phi_{1/8} = sqrt2 L(s, chi_8) - 2*4^-s(1 - 2^{1-s}) zeta(s); zeros of Z_{1/8} and Z_{1/12} in 0 < Re s < 1/2 reflected from zeros of Phi",
   dec < 1e-25 and all(0 < z.real < 0.5 and ph < 1e-15 for z, ph in zs), f"decomposition error {mp.nstr(dec, 3)}; zeros {[mp.nstr(z, 10) for z, _ in zs]}")

print("ALL PASS" if all(res) else "FAILURES")
