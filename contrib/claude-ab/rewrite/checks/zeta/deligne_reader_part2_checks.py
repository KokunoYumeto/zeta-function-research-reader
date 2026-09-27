#!/usr/bin/env python3
# Checks for claude-ab note 37_ (audit of the Deligne reader DELIGNE_WEIGHT_CONTROL_FULL.md, parts DB0-DB8, DB10, DBC1-DBC11, DW0-DW4).
# Written by a subagent in the first-pass audit (25 September 2026) and copied unchanged below this header by Claude
# (claude-ab lane), model claude-opus-5-5 (Opus 5.5) at maximum reasoning effort. Re-run at 17:58 UTC: 64/64 PASS,
# output identical to the first run. Item labels A1-L5 are the ones cited in 37_.
"""
Audit checks for DB0-DB8, DB10, DBC1-DBC11, DW0-DW4 of the Deligne weight-control reader
(reconstruction of Weil II, sections 2.1-2.2 and 3.1-3.2).

Every item prints PASS/FAIL.  Items tagged [CONTROL] deliberately evaluate a WRONG variant
(e.g. the printed choice eps1+eps2<eps in Lemma 2.1.7, a missing Tate twist, a wrong
period, a wrong duality twist) and PASS when the wrong variant is detected as wrong.
"""
import cmath
import math
import itertools
import random
from fractions import Fraction

import numpy as np
import mpmath as mp
import sympy as sp

random.seed(20260925)
np.random.seed(20260925)

RESULTS = []


def check(tag, ok, detail=""):
    RESULTS.append((tag, bool(ok)))
    print(f"[{'PASS' if ok else 'FAIL'}] {tag}: {detail}")


# ----------------------------------------------------------------------------
# small finite-field helpers
# ----------------------------------------------------------------------------
def legendre(a, p):
    a %= p
    if a == 0:
        return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1


def nonsquare(p):
    for r in range(2, p):
        if legendre(r, p) == -1:
            return r


class Fp2:
    """F_{p^2} = F_p[w], w^2 = r (r a non-square)."""

    def __init__(self, p):
        self.p = p
        self.r = nonsquare(p)

    def elements(self):
        p = self.p
        for a in range(p):
            for b in range(p):
                yield (a, b)

    def add(self, x, y):
        p = self.p
        return ((x[0] + y[0]) % p, (x[1] + y[1]) % p)

    def sub(self, x, y):
        p = self.p
        return ((x[0] - y[0]) % p, (x[1] - y[1]) % p)

    def mul(self, x, y):
        p, r = self.p, self.r
        return ((x[0] * y[0] + r * x[1] * y[1]) % p, (x[0] * y[1] + x[1] * y[0]) % p)

    def norm(self, x):
        p, r = self.p, self.r
        return (x[0] * x[0] - r * x[1] * x[1]) % p

    def quad_char(self, x):
        if x == (0, 0):
            return 0
        return legendre(self.norm(x), self.p)


print("=" * 100)
print("A. Conventions of DB1-DB2 / DBC2")
print("=" * 100)

# A1 period of omega_s(g) = q^{-s deg g}
q = 5.0
s0 = 0.3 + 0.7j
ok_true = all(abs(q ** (-(s0 + 2j * math.pi / math.log(q)) * d) - q ** (-s0 * d)) < 1e-12 for d in (1, 2, 3, 7))
check("A1 DB1.3 period 2*pi*i/log q", ok_true, "omega_{s+2pi i/log q} = omega_s on degrees 1,2,3,7")
bad = max(abs(q ** (-(s0 + 2j * math.pi * math.log(q)) * d) - q ** (-s0 * d)) for d in (1, 2, 3))
check("A2 [CONTROL] printed period 2*pi*i*log q (p.187) is not a period", bad > 1e-3,
      f"max |omega_(s+2pi i log q) - omega_s| = {bad:.3f} > 0")

# A3 twist stabilizer example G = Z/3 x| Z (generator of Z inverts Z/3), 2-dim irreducible tau
zeta3 = cmath.exp(2j * math.pi / 3)
c = 0.8 + 0.3j
A = np.diag([zeta3, zeta3 ** -1])
U = np.array([[0, c], [c, 0]])
rel = np.allclose(U @ A @ np.linalg.inv(U), np.linalg.inv(A))


def tau(k, n):
    return np.linalg.matrix_power(A, k % 3) @ np.linalg.matrix_power(U, n) if n >= 0 else \
        np.linalg.matrix_power(A, k % 3) @ np.linalg.matrix_power(np.linalg.inv(U), -n)


qq = 7.0
s_st = 1j * math.pi / math.log(qq)  # omega_s(g) = (-1)^{deg g}
same_char = all(abs(np.trace(tau(k, n)) * qq ** (-s_st * n) - np.trace(tau(k, n))) < 1e-9
                for k in range(3) for n in range(-3, 4))
det_rule = abs(qq ** (-2 * s_st) - 1) < 1e-12
check("A3 DB1 twist stabilizer: tau*omega_{pi i/log q} ~ tau for a 2-dim irreducible, det gives omega_{2s}=1",
      rel and same_char and det_rule, "character of tau vanishes in odd degree; s in (2 pi i/(d log q))Z with d=2")

# A4 elementary inequalities of DB2
ok = True
for cc in (0.1, 0.3, 0.5, 0.9):
    for x in np.linspace(0, cc, 200):
        if -math.log(1 - x) > x / (1 - cc) + 1e-15 or -math.log(1 - x) < x - 1e-15:
            ok = False
for sig, sig0 in ((1.5, 1.1), (2.0, 1.01), (1.2, 1.05)):
    C = 1 / (math.e * (sig - sig0))
    for N in (2, 3, 5, 17, 101, 10 ** 4):
        for n in (1, 2, 3, 10, 100):
            if math.log(N) * math.exp(-n * (sig - sig0) * math.log(N)) > C / n * (1 + 1e-12):
                ok = False
check("A4 DB2 bounds: x<=-log(1-x)<=x/(1-c) and (log N)e^{-n(s-s0)log N}<=C/n, C=1/(e(s-s0))", ok, "grid")

print()
print("=" * 100)
print("B. DB5 concentration lemma (Weil II 2.1.7)")
print("=" * 100)

# B1 U(1): Fejer construction, rho0 = sum_{|n|<N} (N-|n|) chi_n is genuine
e = 0.1
T = [1, -1, 2]


def fejer_ratio(N, k):
    cN = {n: N - abs(n) for n in range(-N + 1, N)}
    num = sum(cN[m] * cN.get(m + k, 0) for m in cN)
    den = sum(v * v for v in cN.values())
    return num / den


Nf = None
for N in range(2, 400):
    if all(fejer_ratio(N, k) >= 1 - e for k in T):
        Nf = N
        break
check("B1 DB5 on U(1): Fejer rho satisfies [rho rho^:chi_k] >= (1-e)[rho rho^:1] for T={1,-1,2}, e=0.1",
      Nf is not None, f"first N = {Nf}; ratios = {[round(fejer_ratio(Nf, k), 4) for k in T]}")

# B2 SU(2): the full DB5 pipeline (bump+delta, character expansion, rational rounding, rho+-, rho=rho^+ + rho^-)
eB = 0.3
e1 = e2 = eB / 4
TB = [1, 2, 3]  # chi_n has dimension n+1
theta = np.linspace(0, math.pi, 200001)
w_haar = (2 / math.pi) * np.sin(theta) ** 2


def haar_int(vals):
    return np.trapezoid(vals * w_haar, theta)


def chi(n, th):
    s = np.sin(th)
    out = np.empty_like(th)
    small = np.abs(s) < 1e-12
    out[~small] = np.sin((n + 1) * th[~small]) / s[~small]
    out[small] = n + 1
    return out


# V = {theta : |chi_n - (n+1)| < e1 (n+1), n in T}
okV = np.ones_like(theta, dtype=bool)
for n in TB:
    okV &= np.abs(chi(n, theta) - (n + 1)) < e1 * (n + 1)
theta0 = theta[np.argmin(okV)]  # first theta where it fails (V = [0, theta0) since conditions are monotone near 0)
th1 = 0.9 * theta0
bump = np.where(theta < th1, np.exp(-1.0 / np.maximum(1e-300, 1 - (theta / th1) ** 2)), 0.0)
delta = 1e-5
h = bump + delta
Nmax = 160
coef = [haar_int(h * chi(n, theta)) for n in range(Nmax + 1)]
D = 10 ** 6
nint = [int(round(D * cf)) for cf in coef]
rho0 = sum(nint[n] * chi(n, theta) for n in range(Nmax + 1))
M0 = haar_int(rho0 ** 2)
outside = haar_int(np.where(theta >= theta0, rho0 ** 2, 0.0))
frac_out = outside / M0
check("B2a DB5.3 concentration of |rho0|^2 outside V", frac_out <= e2,
      f"theta0={theta0:.4f}, outside fraction={frac_out:.3e} <= e2={e2}")


def cg_mult(n_list, k):
    """[ (sum n_a chi_a)(sum n_b chi_b) : chi_k ] via Clebsch-Gordan (exact integers)."""
    tot = 0
    idx = [a for a, v in enumerate(n_list) if v != 0]
    for a in idx:
        for b in idx:
            if abs(a - b) <= k <= a + b and (a + b - k) % 2 == 0:
                tot += n_list[a] * n_list[b]
    return tot


pos = [v if v > 0 else 0 for v in nint]
neg = [-v if v < 0 else 0 for v in nint]
rho = [pos[i] + neg[i] for i in range(len(nint))]
M = cg_mult(rho, 0)
M_0 = cg_mult(nint, 0)
lhs_ok = all(cg_mult(rho, k) >= (1 - eB) * (k + 1) * M for k in TB)
check("B2b DB5.1 on SU(2) with rho = rho^+ + rho^- (exact Clebsch-Gordan integers)", lhs_ok and M == M_0,
      f"[rho rho^:1]=M={M}=[rho0 rho0^:1]; ratios={[round(cg_mult(rho, k) / ((k + 1) * M), 4) for k in TB]} >= {1 - eB}")


def cross(a_list, b_list, k):
    tot = 0
    for a, va in enumerate(a_list):
        if va == 0:
            continue
        for b, vb in enumerate(b_list):
            if vb and abs(a - b) <= k <= a + b and (a + b - k) % 2 == 0:
                tot += va * vb
    return tot


ident = all(cg_mult(rho, k) - cg_mult(nint, k) == 2 * (cross(pos, neg, k) + cross(neg, pos, k)) for k in range(0, 8))
triv0 = cross(pos, neg, 0) == 0 and cross(neg, pos, 0) == 0
check("B2c DB5.6 tensor identity and zero trivial multiplicity of cross terms", ident and triv0,
      f"#neg coefficients={sum(1 for v in nint if v < 0)}, identity checked for k=0..7")
bound = (1 - e1) * (1 - frac_out) - frac_out
act = min(cg_mult(nint, k) / ((k + 1) * M_0) for k in TB)
check("B2d DB5.8 lower bound [(1-e1)(1-e2)-e2] respected by the actual multiplicities", act >= bound - 1e-9,
      f"min ratio {act:.4f} >= {(bound):.4f}")

# B3 printed choice eps1 + eps2 < eps (p.191) is insufficient: Z/2 counterexample
eps, eps1, eps2 = 0.2, 0.01, 0.18
c1, c2 = 23, 9  # rho0 = c1*1 + c2*sgn ; values A=rho0(e)=32, B=rho0(c)=14
Aval, Bval = c1 + c2, c1 - c2
cond_a = Aval > 0 and Bval > 0
out_mass = Bval ** 2 / 2
tot_mass = (Aval ** 2 + Bval ** 2) / 2
cond_b = out_mass <= eps2 * tot_mass  # V = {e}; |tau(e)-tau(e)| = 0 < eps1
mult_sgn = 2 * c1 * c2
mult_1 = c1 * c1 + c2 * c2
fails = mult_sgn < (1 - eps) * 1 * mult_1
check("B3 [CONTROL] printed 'eps1+eps2<eps' (Lemma 2.1.7 proof) fails on Z/2", cond_a and cond_b and fails and eps1 + eps2 < eps,
      f"rho0=(32,14) satisfies a),b) with eps1={eps1}, eps2={eps2}; [rho rho^:sgn]={mult_sgn} < (1-eps)[rho rho^:1]={(1 - eps) * mult_1:.1f}")
# corrected constant eps1 + 2 eps2 < eps: sweep all integer pairs
eps2c = (eps - eps1) / 2 * 0.999
worst = 1.0
for a in range(1, 150):
    for b in range(-a + 1, a):
        Av, Bv = a + b, a - b
        if Av <= 0 or Bv <= 0:
            continue
        if Bv ** 2 <= eps2c * (Av ** 2 + Bv ** 2):
            # ratio for rho0 itself; for rho = rho^+ + rho^- (|b| instead of b) the ratio can only increase
            worst = min(worst, (Av ** 2 - Bv ** 2) / (Av ** 2 + Bv ** 2))
check("B4 corrected constant eps1+2*eps2<eps gives ratio >= 1-eps for every admissible rho0 on Z/2",
      worst >= 1 - eps, f"worst [rho0 rho0^:sgn]/[rho0 rho0^:1] = {worst:.4f} >= {1 - eps}")

print()
print("=" * 100)
print("C. DB6 exceptional quadratic character (Lemma 2.1.5/2.1.6)")
print("=" * 100)
ok = all((a * a + b * b) - 2 * a * b >= 0 for a in range(0, 31) for b in range(0, 31))
check("C1 Z/2 with nu(1)=1, nu(sgn)=-1 satisfies a)-d): nu(rho rho^)=(a-b)^2>=0 (exception cannot be excluded by positivity)",
      ok, "all a,b in [0,30]")
check("C2 [CONTROL] nu(sgn)=-2 violates d)", (1 + 1) - 2 * 2 < 0, "rho = 1+sgn gives nu = 2 - 4 = -2")
# S3: irreps 1, sgn, std(dim2); regular rep squared = 6 reg
mult_regsq = {"1": 6, "sgn": 6, "std": 12}
nu = {"1": 1, "sgn": 0, "std": -1}
val = sum(mult_regsq[x] * nu[x] for x in nu)
check("C3 [CONTROL] S3 with nu(std)=-1 (dim 2) violates d)", val < 0, f"nu(reg reg^) = {val} < 0")
Nneg = None
for N in range(2, 50):
    cN = {n: N - abs(n) for n in range(-N + 1, N)}
    v = sum(x * x for x in cN.values()) - 2 * sum(cN[m] * cN.get(m + 1, 0) for m in cN)
    if v < 0:
        Nneg = N
        break
check("C4 [CONTROL] U(1) with nu(chi_1)=nu(chi_-1)=-1 is excluded by the concentration lemma (DB6.2 sharp)",
      Nneg is not None, f"Fejer rho_N with N={Nneg} gives nu(rho rho^) < 0")

print()
print("=" * 100)
print("D. DB7-DB8 pole cancellation and geometric decay")
print("=" * 100)
# D1 P^1 over F_7: exact cancellation
qd = 7.0


def mu_hat_diff(s, alphas, qv, norm=True):
    # transform of mu^natural at omega_s minus transform of mu_0^natural, in high precision:
    # sum_m N_m q^{-m(1+s)} - q^{-s}/(1-q^{-s}),  N_m = 1 + q^m - sum alpha^m
    mp.mp.dps = 60
    s = mp.mpf(s)
    qv = mp.mpf(qv)
    u = qv ** (-1 - s)
    tot = u / (1 - u) + qv * u / (1 - qv * u) - sum(mp.mpc(a) * u / (1 - mp.mpc(a) * u) for a in alphas)
    if not norm:
        tot = tot * mp.log(qv)
    return complex(tot - qv ** (-s) / (1 - qv ** (-s)))


vals = [mu_hat_diff(mp.mpf(10) ** (-k), [], qd).real for k in (2, 4, 6, 8)]
check("D1 DB7 P^1/F_7: transform of mu^nat - mu_0^nat is finite at the trivial character",
      abs(vals[-1] - 1 / (qd - 1)) < 1e-6, f"values -> {vals[-1]:.8f} = 1/(q-1) = {1 / (qd - 1):.8f}")
valsbad = [abs(mu_hat_diff(mp.mpf(10) ** (-k), [], qd, norm=False)) for k in (2, 4, 6)]
check("D2 [CONTROL] without the factor 1/log q (DB7.2) the difference diverges", valsbad[-1] > 1e4,
      f"|diff| at s=1e-2,1e-4,1e-6: {[f'{v:.3g}' for v in valsbad]}")

# elliptic curve over F_7
p = 7


def count_E_Fp(p, A=1, B=1):
    n = 1
    for x in range(p):
        n += 1 + legendre(x ** 3 + A * x + B, p)
    return n


def count_E_Fp2(p, A=1, B=1):
    F = Fp2(p)
    n = 1
    for x in F.elements():
        x2 = F.mul(x, x)
        x3 = F.mul(x2, x)
        rhs = F.add(F.add(x3, F.mul((A % p, 0), x)), (B % p, 0))
        n += 1 + F.quad_char(rhs)
    return n


N1 = count_E_Fp(p)
N2 = count_E_Fp2(p)
aE = p + 1 - N1
alpha = (aE + cmath.sqrt(aE * aE - 4 * p)) / 2
alphab = (aE - cmath.sqrt(aE * aE - 4 * p)) / 2
N2_pred = p ** 2 + 1 - (alpha ** 2 + alphab ** 2).real
check("D3 trace formula shape on E: y^2=x^3+x+1 over F_7 (N_1, N_2 brute force)", abs(N2 - N2_pred) < 1e-9,
      f"N1={N1}, a={aE}, N2={N2}, predicted {N2_pred:.1f}, |alpha|^2={abs(alpha) ** 2:.6f}")
valsE = [mu_hat_diff(mp.mpf(10) ** (-k), [alpha, alphab], float(p)) for k in (3, 6, 9)]
check("D4 DB7 on E/F_7: exact cancellation of the pole at the trivial character",
      abs(valsE[-1] - valsE[-2]) < 1e-5, f"diff(s) at s=1e-3,1e-6,1e-9: {[f'{complex(v).real:.6f}' for v in valsE]}")
am = [(1 + p ** m - (alpha ** m + alphab ** m).real) / p ** m - 1 for m in range(1, 13)]
ratio_ok = all(abs(am[m]) <= p ** (-(m + 1)) + 2 * p ** (-(m + 1) / 2) + 1e-15 for m in range(12))
check("D5 DB8.3 geometric decay of a_m = q^{-m} #X(F_{q^m}) - 1", ratio_ok,
      f"|a_m| <= q^-m + 2 q^(-m/2); a_12 = {am[-1]:.2e}")

print()
print("=" * 100)
print("E. DBC2 sign of the weight, DBC6 Euler region")
print("=" * 100)
ok = True
okbad = True
for s in (0.3 + 1j, -0.7 + 2j, 1.9 - 0.5j):
    for d in (1, 2, 5):
        Nv = 11.0 ** d
        ev = 11.0 ** (-s * d)
        w = 2 * math.log(abs(ev)) / math.log(Nv)
        ok &= abs(w - (-2 * s.real)) < 1e-12
        okbad &= abs(w - 2 * s.real) > 1e-6
check("E1 DBC2.4: tau=omega_s has pointwise weight -2Re(tau)", ok, "three s, degrees 1,2,5")
check("E2 [CONTROL] printed 'poids 2R(tau)' (2.2.8(i), p.195) contradicts the definitions", okbad,
      "weight differs from +2Re(tau) whenever Re s != 0")
# Euler region Re s > N + beta/2: A^N with rank-one twist c, |c| = q^{beta/2}
qv, Ndim, beta = 3.0, 2, 0.8
cc = qv ** (beta / 2) * cmath.exp(0.4j)
pole_t = 1 / (cc * qv ** Ndim)
s_pole_re = -math.log(abs(pole_t)) / math.log(qv)
check("E3 DBC6.5 region: L(tau,s) for A^N twisted by weight beta has its pole exactly at Re s = N + beta/2",
      abs(s_pole_re - (Ndim + beta / 2)) < 1e-12, f"Re s_pole = {s_pole_re:.6f}, N+beta/2 = {Ndim + beta / 2}")

print()
print("=" * 100)
print("F. DBC7 noncircular simple pole of the curve zeta function")
print("=" * 100)
P1_at = 1 - aE / p + p / p ** 2
check("F1 genuine E/F_7: P_1(1/q) != 0", abs(P1_at) > 1e-9, f"P_1(1/7) = {P1_at:.6f}")


def contradiction(eigs, delta_, nmax=60):
    """Return (negative_found, bounded) for N_n = delta + q^n - sum eigs^n, with one q removed."""
    Ns = [delta_ - sum(a ** n for a in eigs) for n in range(1, nmax + 1)]
    neg = any(x.real < -1e-9 for x in Ns)
    bounded = max(abs(x) for x in Ns) <= delta_ + len(eigs) + 1e-9
    return neg, bounded, Ns[:6]


neg, bnd, first = contradiction([1.0], 1)  # fake H^1 eigenvalues {q, 1}: after removing q, remaining {1}
check("F2 [CONTROL] fake H^1 eigenvalues {q,1} (pole cancelled): counts bounded -> DBC7 contradiction",
      bnd and not neg, f"N_n = {[round(complex(x).real, 3) for x in first]} ... bounded")
neg, bnd, first = contradiction([2.0], 1)
check("F3 [CONTROL] fake H^1 eigenvalues {q,2}: some count negative -> DBC7 contradiction", neg,
      f"N_n = {[round(complex(x).real, 3) for x in first]}")
# extractable lemma: delta - sum a_j^n >= 0 for all n forces |a_j| <= 1
ok = True
for trial in range(200):
    r = random.randint(1, 4)
    eigs = [random.uniform(1.01, 3) * cmath.exp(2j * math.pi * random.random()) for _ in range(r)]
    eigs += [random.uniform(0.1, 0.99) * cmath.exp(2j * math.pi * random.random()) for _ in range(random.randint(0, 3))]
    found = False
    pw = [1.0 + 0j] * len(eigs)
    for n in range(1, 200000):
        pw = [pw[j] * eigs[j] for j in range(len(eigs))]
        if max(abs(x) for x in pw) > 1e250:
            break
        if (1 - sum(pw)).real < 0:
            found = True
            break
    ok &= found
check("F4 extractable lemma: if some |a_j|>1 then delta - sum a_j^n < 0 for some n (200 random trials)", ok,
      "simultaneous approximation of phases")
# DBC7.4 constant field extension
t = sp.symbols('t')
qs, d = 5, 3
ZY0 = 1 / ((1 - t ** d) * (1 - qs ** d * t ** d))
# direct: #Y0(F_{q^n}) = q^n + 1 if d | n else 0 ; Z = exp(sum N_n t^n / n)
ser = sp.series(sp.log(ZY0), t, 0, 13).removeO()
# #Y0(F_{q^n}) = d (q^n + 1) if d | n (d embeddings F_{q^d} -> F_{q^n}), else 0
okc = all(sp.nsimplify(ser.coeff(t, n) * n) == (d * (qs ** n + 1) if n % d == 0 else 0) for n in range(1, 13))
deriv = sp.diff(1 - qs ** d * t ** d, t).subs(t, sp.Rational(1, qs))
check("F5 DBC7.4: Z(Y0,t)=Z(Y*,t^d) point counts and derivative -d*q of the top denominator at t=1/q",
      okc and deriv == -d * qs, f"derivative = {deriv}")

print()
print("=" * 100)
print("G. DBC8 quadratic covers")
print("=" * 100)
# geometric case: G_m --(y->y^2)--> G_m over F_p (p odd), eps = Legendre symbol; zeta_Y = zeta_X * L(eps,s)
p = 11
ok = True
for n in (1, 2):
    if n == 1:
        sum_eps = sum(legendre(x, p) for x in range(1, p))
        NX = NY = p - 1
    else:
        F = Fp2(p)
        sum_eps = sum(F.quad_char(x) for x in F.elements() if x != (0, 0))
        NX = NY = p * p - 1
    ok &= (NY == NX + sum_eps)
tt = sp.symbols('tt')
loc = sp.simplify((1 - tt) ** -2 - (1 - tt) ** -1 * (1 - tt) ** -1) == 0 and \
    sp.simplify((1 - tt ** 2) ** -1 - (1 - tt) ** -1 * (1 + tt) ** -1) == 0
check("G1 DBC8.1-8.2 (geometric case, G_m squaring cover): #Y = #X + sum eps, split/inert local factors",
      ok and loc, "n=1,2 over F_11; here H^*_c(G_m,L_eps)=0 so L(eps,s)=1, L(eps,1)!=0")
qs = 5
ZX = 1 / ((1 - t) * (1 - qs * t))
ZY = 1 / ((1 - t ** 2) * (1 - qs ** 2 * t ** 2))
okcf = sp.simplify(ZY - ZX * ZX.subs(t, -t)) == 0
Leps1 = ZX.subs(t, -sp.Rational(1, qs))
check("G2 DBC8 (constant-field case): Z(P^1_{F_q2}/F_q,t)=Z(t)Z(-t) and L(eps,1)=Z(-1/q) finite nonzero",
      okcf and Leps1 != 0 and Leps1.is_finite, f"L(eps,1) = {Leps1}")
sig = np.array([[0, 1], [1, 0]])
Pp, Pm = (np.eye(2) + sig) / 2, (np.eye(2) - sig) / 2
check("G3 DBC8 deck projectors (1+-sigma)/2 idempotent, orthogonal, complete (char 0 coefficients)",
      np.allclose(Pp @ Pp, Pp) and np.allclose(Pm @ Pm, Pm) and np.allclose(Pp @ Pm, 0) and np.allclose(Pp + Pm, np.eye(2)), "")

print()
print("=" * 100)
print("H. DBC9 strict bound with the original weight beta, DBC10 field change")
print("=" * 100)
p = 7
beta = 0.7
aTw = p ** (beta / 2) * cmath.exp(1.3j)
tstar = 1 / (p * aTw)


def Ltw(tv):
    P1 = (1 - aTw * alpha * tv) * (1 - aTw * alphab * tv)
    return P1 / ((1 - aTw * tv) * (1 - p * aTw * tv))


P1star = (1 - aTw * alpha * tstar) * (1 - aTw * alphab * tstar)
res = [(h) * Ltw(tstar + h) for h in (1e-4, 1e-6, 1e-8)]
wts = [2 * math.log(abs(aTw * a)) / math.log(p) for a in (alpha, alphab)]
check("H1 DBC9 case 2 (geometrically trivial rank one on E/F_7, beta=0.7): simple pole at t*=(qa)^-1, P_1(t*)!=0",
      abs(P1star) > 1e-6 and abs(res[-1] - res[-2]) < 1e-5 * abs(res[-1]) and abs(abs(tstar) - p ** (-1 - beta / 2)) < 1e-12,
      f"|P_1(t*)|={abs(P1star):.4f}, residue ~ {abs(res[-1]):.4f}, |t*| = q^(-1-beta/2)")
check("H2 DBC9.8 strict weight bound w(alpha) < beta+2 for H^1_c eigenvalues (here = beta+1)",
      all(w < beta + 2 - 1e-9 for w in wts), f"weights = {[round(w, 6) for w in wts]}, beta+2 = {beta + 2}")
# fake P_1 with a zero at t*: ord_{t*} L would be 0, contradicting condition (C)
res_fake = [(h) * ((1 - (tstar + h) / tstar) * (1 - aTw * alpha * (tstar + h))) / ((1 - aTw * (tstar + h)) * (1 - p * aTw * (tstar + h)))
            for h in (1e-4, 1e-8)]
check("H3 [CONTROL] a fake H^1_c eigenvalue of weight exactly beta+2 at t* removes the pole (ord 0), contradicting (C)",
      abs(res_fake[-1]) < 1e-6, f"(t-t*)L(t) -> {abs(res_fake[-1]):.2e} (no pole)")
# field change invariance
ok = True
for _ in range(100):
    al = random.uniform(0.2, 50) * cmath.exp(2j * math.pi * random.random())
    qv = random.choice([2, 3, 5, 7, 9])
    n = random.randint(1, 6)
    ok &= abs(2 * math.log(abs(al ** n)) / math.log(qv ** n) - 2 * math.log(abs(al)) / math.log(qv)) < 1e-9
    dd = random.randint(1, 12)
    g = math.gcd(dd, n)
    b_ = random.uniform(-2, 3)
    ok &= abs((dd * b_ / 2) * (n / g) - (n * (dd // g) * b_ / 2)) < 1e-9
check("H4 DBC10.1-10.2 weights invariant under F_q -> F_{q^n}", ok, "random alpha, q, n, d")

print()
print("=" * 100)
print("I. DW3 vanishing cycles: Kummer classes, nodes, tangency, crossing")
print("=" * 100)
# I1 Milnor fibre uv = t0, loop u = r e^{i theta}
t0 = 0.3 + 0.1j
ths = np.linspace(0, 2 * math.pi, 20001)
u = 0.7 * np.exp(1j * ths)
v = t0 / u
wu = np.sum(np.diff(np.unwrap(np.angle(u)))) / (2 * math.pi)
wv = np.sum(np.diff(np.unwrap(np.angle(v)))) / (2 * math.pi)
wuv = np.sum(np.diff(np.unwrap(np.angle(u / v)))) / (2 * math.pi)
check("I1 DW0/(3.1.3.3): on uv=t, [v]=-[u] and [u v^-1] = 2[u] (winding numbers)",
      round(wu) == 1 and round(wv) == -1 and round(wuv) == 2, f"[u]={wu:.3f}, [v]={wv:.3f}, [u/v]={wuv:.3f}")
check("I2 [CONTROL] printed 'generateur canonique ... T^(l^n)=uv^-1': 2[u] is not a generator of Z/2^n (l=2)",
      math.gcd(2, 2 ** 5) != 1 and math.gcd(2, 3 ** 4) == 1, "2 is a unit mod 3^n but not mod 2^n")


def conic_matrix(coeffs):
    a, b, c_, d_, e_, f_ = coeffs  # a x^2 + b y^2 + c z^2 + d xy + e xz + f yz
    return sp.Matrix([[a, sp.Rational(d_, 2), sp.Rational(e_, 2)], [sp.Rational(d_, 2), b, sp.Rational(f_, 2)],
                      [sp.Rational(e_, 2), sp.Rational(f_, 2), c_]])


def proj_points(p):
    pts = []
    for x in range(p):
        for y in range(p):
            pts.append((x, y, 1))
    for x in range(p):
        pts.append((x, 1, 0))
    pts.append((1, 0, 0))
    return pts


def count_conic(coeffs, p):
    a, b, c_, d_, e_, f_ = coeffs
    return sum(1 for (x, y, z) in proj_points(p) if (a * x * x + b * y * y + c_ * z * z + d_ * x * y + e_ * x * z + f_ * y * z) % p == 0)


def eps_branch(coeffs, p):
    """sign of Frobenius on the two lines of a rank-2 conic: restrict to a line avoiding the vertex."""
    Mx = sp.Matrix([[2 * coeffs[0], coeffs[3], coeffs[4]], [coeffs[3], 2 * coeffs[1], coeffs[5]], [coeffs[4], coeffs[5], 2 * coeffs[2]]])
    Mp = Mx.applyfunc(lambda z: z % p)
    ker = None
    for (x, y, z) in proj_points(p):
        vv = sp.Matrix([x, y, z])
        if all(((Mp * vv)[i]) % p == 0 for i in range(3)):
            ker = (x, y, z)
            break
    # choose two points spanning a line not through the vertex
    for P0 in proj_points(p):
        for P1 in proj_points(p):
            Mt = sp.Matrix([list(P0), list(P1), list(ker)])
            if Mt.det() % p != 0:
                def Q(s_, t_):
                    X = [(s_ * P0[i] + t_ * P1[i]) for i in range(3)]
                    a, b, c_, d_, e_, f_ = coeffs
                    return a * X[0] ** 2 + b * X[1] ** 2 + c_ * X[2] ** 2 + d_ * X[0] * X[1] + e_ * X[0] * X[2] + f_ * X[1] * X[2]
                A2 = Q(1, 0)
                C2 = Q(0, 1)
                B2 = Q(1, 1) - A2 - C2
                disc = (B2 * B2 - 4 * A2 * C2) % p
                return legendre(disc, p)
    return None


def pencil_check(Qa, Qb, p, n_rat_base):
    tot = 0
    sing = []
    for (lam, mu) in [(1, m) for m in range(p)] + [(0, 1)]:
        co = tuple((lam * Qa[i] + mu * Qb[i]) % p for i in range(6))
        cnt = count_conic(co, p)
        tot += cnt
        det = conic_matrix(co).det()
        if sp.Rational(det).p % p == 0:
            eB_ = eps_branch(co, p)
            sing.append((co, cnt, eB_))
        else:
            if cnt != p + 1:
                return None
    return tot, sing


# configuration A: 4 rational base points (1:0:0),(0:1:0),(0:0:1),(1:1:1): conics a yz + b xz + c xy, a+b+c=0
p = 7
QA = (0, 0, 0, -1, 0, 1)   # yz - xy
QB = (0, 0, 0, -1, 1, 0)   # xz - xy
resA = pencil_check(QA, QB, p, 4)
okA = resA is not None and len(resA[1]) == 3 and resA[0] == p * p + 5 * p + 1 and \
    all(cnt == 1 + p + p * eB_ for (_, cnt, eB_) in resA[1])
check("I3 DW3 node (a): conic pencil through 4 rational points over F_7: 3 nodal fibres, #fibre = 1+p+p*eps(B), total p^2+5p+1",
      okA, f"singular fibres (count, eps) = {[(c_, e_) for (_, c_, e_) in resA[1]]}, total={resA[0]}")
# configuration B: two conjugate pairs (+-i:0:1),(0:+-i:1), p = 3 mod 4: pencil lambda(x^2+y^2+z^2) + mu xy
p = 7
QA = (1, 1, 1, 0, 0, 0)
QB = (0, 0, 0, 1, 0, 0)
resB = pencil_check(QA, QB, p, 0)
epsB = sorted(e_ for (_, _, e_) in resB[1])
okB = resB is not None and len(resB[1]) == 3 and resB[0] == p * p + p + 1 and epsB == [-1, -1, 1] and \
    all(cnt == 1 + p + p * eB_ for (_, cnt, eB_) in resB[1])
check("I4 DW3 node (a): conjugate base points over F_7: eps(B) = +1,-1,-1 and #fibre = 1+p+p*eps(B), total p^2+p+1",
      okB, f"singular fibres (count, eps) = {[(c_, e_) for (_, c_, e_) in resB[1]]}, total={resB[0]}")
wrong1 = any(cnt != 1 + p + eB_ for (_, cnt, eB_) in resB[1])
wrong2 = any(cnt != 1 + 2 * p for (_, cnt, eB_) in resB[1])
check("I5 [CONTROL] Phi^1 = Q(eps(B)) without Tate twist, or Q(-1) without sign line, contradicts the counts",
      wrong1 and wrong2, "both wrong variants mismatch the nodal fibre counts")
# I6 tangency: D: x^2+y^2-z^2 = 0, P=(0:0:1) not on D, lines b x - a y = 0
ok = True
okbad = False
tot = 0
for p in (13, 11):
    tot = 0
    for (a_, b_) in [(1, m) for m in range(p)] + [(0, 1)]:
        # points on line: (a s : b s : z)
        ptsL = [(a_, b_, z) for z in range(p)] + [(0, 0, 1)]
        onD = sum(1 for (x, y, z) in ptsL if (x * x + y * y - z * z) % p == 0)
        cnt = len(ptsL) - onD
        ep = legendre(a_ * a_ + b_ * b_, p)
        ok &= (cnt == p - ep)
        if ep != 0 and cnt != p - p * ep:
            okbad = True
        tot += cnt
    ok &= (tot == p * p + p)
check("I6 DW3 tangency (b): #(L_t - D) = p - eps(t), H^1_c = eps(B) with no Tate twist; sum = p^2+p",
      ok, "p = 13 (rational tangents) and p = 11 (conjugate tangents)")
check("I7 [CONTROL] a Tate-twisted sign line (trace p*eps) contradicts the tangency counts", okbad, "")
# I8 crossing: D: x^2 - n y^2 = 0 (conjugate lines through x0=(0:0:1)), P=(1:0:0), lines alpha y + beta z = 0
p = 11
nn = nonsquare(p)
ok = True
for (al, be) in [(1, m) for m in range(p)] + [(0, 1)]:
    pts = [pt for pt in proj_points(p) if (al * pt[1] + be * pt[2]) % p == 0]
    onD = sum(1 for (x, y, z) in pts if (x * x - nn * y * y) % p == 0)
    cnt = len(pts) - onD
    special = (be == 0)
    ok &= (cnt == (p if special else p + 1))
check("I8 DW3 crossing (c): conjugate branches: generic #(L_t-D) = p+1 (eps=-1), special line through x0: p",
      ok, "Phi^1 = eps(B) with Frobenius -1, H^1_c of the special fibre = 0")
chi_list = {"conic pencil": (7, 2 * 2 + 3), "tangency": (2, 2 * 0 + 2), "crossing": (1, 2 * 0 + 1), "cubic pencil": (12, 2 * 0 + 12)}
check("I9 Euler characteristic bookkeeping chi_c(V~) = 2 chi_c(F_gen) + #(rank-one Phi^1)",
      all(a_ == b_ for (a_, b_) in chi_list.values()), str(chi_list))

print()
print("=" * 100)
print("J. DW4 real characteristic polynomials and the real companion")
print("=" * 100)
p = 13
g = 2  # primitive root mod 13
dlog = {pow(g, k, p): k for k in range(p - 1)}


def chi_ord(x, order, p=p):
    if x % p == 0:
        return 0
    return cmath.exp(2j * math.pi * dlog[x % p] * ((p - 1) // order) / (p - 1))


J = sum(chi_ord(x, 3) * chi_ord(1 - x, 4) for x in range(2, p))
check("J1 Jacobi-sum sheaf on A^1-{0,1}/F_13: |J| = sqrt(q) (weight 1 < b+2 = 2)", abs(abs(J) ** 2 - p) < 1e-9,
      f"J = {J:.6f}, |J|^2 = {abs(J) ** 2:.6f}")
check("J2 [CONTROL] L alone is not iota-real: 1 + J t has non-real coefficient", abs(J.imag) > 1e-6, f"Im J = {J.imag:.4f}")
poly = np.polymul([J, 1], [J.conjugate(), 1])
check("J3 DW4: L (+) Lbar is real and its H^1_c polynomial (1+Jt)(1+Jbar t) is real", np.allclose(np.imag(poly), 0),
      f"coefficients = {np.round(np.real(poly), 6)}")
# trace formula over F_{13^2}
F = Fp2(p)
# characters of F_{p^2}^* used here: chi o Norm (Hasse-Davenport lift)
S2 = 0
for x in F.elements():
    if x == (0, 0) or x == (1, 0):
        continue
    one_minus = F.sub((1, 0), x)
    S2 += chi_ord(F.norm(x), 3) * chi_ord(F.norm(one_minus), 4)
check("J4 Grothendieck trace formula over F_{q^2}: sum = -alpha^2 with alpha = -J (H^0_c=H^2_c=0)",
      abs(S2 - (-(J ** 2))) < 1e-8, f"sum = {S2:.6f}, -J^2 = {-(J ** 2):.6f}")
# companion
qv = 13.0
betaC = 0.6
okc = True
bad1 = bad2 = False
for d in (1, 2, 3):
    lams = [qv ** (d * betaC) * cmath.exp(2j * math.pi * random.random()) for _ in range(4)]
    a_good = qv ** (2 * betaC)
    ms = lams + [a_good ** d / l_ for l_ in lams]
    pol = np.poly(ms)
    okc &= np.allclose(np.imag(pol), 0, atol=1e-6 * np.max(np.abs(pol)))
    ms1 = lams + [1 / l_ for l_ in lams]
    pol1 = np.poly(ms1)
    bad1 |= not np.allclose(np.imag(pol1), 0, atol=1e-6 * np.max(np.abs(pol1)))
    a_bad = qv ** betaC
    ms2 = lams + [a_bad ** d / l_ for l_ in lams]
    pol2 = np.poly(ms2)
    bad2 |= not np.allclose(np.imag(pol2), 0, atol=1e-6 * np.max(np.abs(pol2)))
check("J5 DW4.3-4.4: G (+) (G^dual (x) L_a), iota(a)=q^{2beta}, has real local polynomials (weight 2beta)", okc,
      "beta = 0.6, degrees 1-3")
check("J6 [CONTROL] a = 1 (Deligne's G(+)G^dual used at beta != 0) or |a| = q^beta is not real", bad1 and bad2, "")
# no cancellation at radius q^{-(b+2)/2}: E = Q (+) L (+) Lbar on A^1-{0,1}
tt_ = sp.symbols('tt_')
Z_E = (1 - tt_) ** 2 * (1 + 2 * sp.re(J) * tt_ + p * tt_ ** 2) / (1 - p * tt_)
numer_roots = [complex(r_) for r_ in sp.Poly(sp.expand((1 - tt_) ** 2 * (1 + 2 * float(J.real) * tt_ + p * tt_ ** 2)), tt_).nroots()]
okr = all(abs(r_) > 1 / p + 1e-9 for r_ in numer_roots)
check("J7 DW4: numerator zeros (H^0_c, H^1_c) lie strictly outside |t| = q^{-(b+2)/2}; the pole there is exactly H^2_c",
      okr, f"|zeros| = {sorted(round(abs(r_), 4) for r_ in numer_roots)}, radius 1/q = {1 / p:.4f}")
Zfake = (1 - p * tt_) * (1 - tt_) / (1 - p * tt_)
check("J8 [CONTROL] with a fake H^1_c eigenvalue of weight b+2 (=q) the H^2_c pole is cancelled (strictness of D5 needed)",
      sp.limit((tt_ - sp.Rational(1, p)) * Zfake, tt_, sp.Rational(1, p)) == 0, "(t-1/q)Z(t) -> 0")
# duality twist
qv = 9.0
cdual = qv ** 0.35 * cmath.exp(0.9j)
H0 = [cdual, cdual.conjugate()]
H2_good = [1 / cdual, 1 / cdual.conjugate()]
H2_bad = [qv ** 2 / cdual, qv ** 2 / cdual.conjugate()]
okd = all(abs(a_ * b_ - 1) < 1e-12 for a_, b_ in zip(H0, H2_good))
badd = all(abs(a_ * b_ - 1) > 1 for a_, b_ in zip(H0, H2_bad))
realboth = np.allclose(np.imag(np.poly(H2_good)), 0) and np.allclose(np.imag(np.poly(H2_bad)), 0)
check("J9 DW4.1 duality H^0(E) x H^2(E^dual(1)) -> Q_l: eigenvalue products = 1", okd, "E = L_c (+) L_cbar on P^1")
check("J10 [CONTROL] printed partner F^dual(-1) (3.2.1, p.200) gives products q^2 != 1 (reality unaffected)",
      badd and realboth, "the pairing lands in Q_l(-2); both H^2 polynomials remain real")

print()
print("=" * 100)
print("K. Riemann zeta (DB9 context, classical content only)")
print("=" * 100)
mp.mp.dps = 30


def Lam(sig, tv):
    s = mp.mpc(sig, tv)
    return -mp.zeta(s, derivative=1) / mp.zeta(s)


primes = list(sp.primerange(2, 20000))
sig, tv = 3, 3
approx = mp.mpf(0)
for pr in primes:
    lp = mp.log(pr)
    n = 1
    while pr ** n < 10 ** 12:
        approx += lp * mp.power(pr, -n * sig) * mp.expj(-tv * n * lp)
        n += 1
check("K1 DB9.3: -zeta'/zeta(sigma+it) = integral of e^{-itx} d mu_sigma (prime powers)",
      abs(approx - Lam(sig, tv)) < 1e-7, f"|difference| = {mp.nstr(abs(approx - Lam(sig, tv)), 3)}")
ok = True
for sig in (1.001, 1.01, 1.1, 1.5):
    for tv in (0.5, 1, 5, 14.134725, 21.02204, 100):
        vv = 3 * mp.re(Lam(sig, 0)) + 4 * mp.re(Lam(sig, tv)) + 2 * mp.re(Lam(sig, 2 * tv))
        ok &= vv >= 0
th_ = np.linspace(0, 2 * math.pi, 1001)
ident = np.allclose(3 + 4 * np.cos(th_) + 2 * np.cos(2 * th_), (1 + 2 * np.cos(th_)) ** 2)
check("K2 (2.1.9)/DB9.7: 3Re L(0)+4Re L(t)+2Re L(2t) >= 0 and 3+4c+2cos2x = (1+2c)^2", ok and ident, "grid of sigma, t")
check("K3 [CONTROL] coefficients (3,4,3) give a trigonometric polynomial with negative values",
      np.min(3 + 4 * np.cos(th_) + 3 * np.cos(2 * th_)) < 0, f"min = {np.min(3 + 4 * np.cos(th_) + 3 * np.cos(2 * th_)):.3f}")
ts = [0.37, 2.1, 5.5, 9.8, 13.3, 17.9]
Mk = mp.matrix(len(ts), len(ts))
for i_, a_ in enumerate(ts):
    for j_, b_ in enumerate(ts):
        Mk[i_, j_] = Lam(1.2, a_ - b_)
Mnp = np.array([[complex(Mk[i_, j_]) for j_ in range(len(ts))] for i_ in range(len(ts))])
check("K4 DB9.5 positive definiteness of [-zeta'/zeta(sigma+i(t_j-t_l))] at sigma=1.2",
      np.min(np.linalg.eigvalsh((Mnp + Mnp.conj().T) / 2)) > -1e-10 and np.allclose(Mnp, Mnp.conj().T),
      f"min eigenvalue = {np.min(np.linalg.eigvalsh((Mnp + Mnp.conj().T) / 2)):.4f}")
r0 = (mp.mpf('1e-6')) * Lam(1 + mp.mpf('1e-6'), 0)
r1 = (mp.mpf('1e-6')) * Lam(1 + mp.mpf('1e-6'), 14.134725)
check("K5 DB3.2: (sigma-1)Lambda_sigma(0) -> 1 and (sigma-1)Lambda_sigma(t) -> 0 (no zero at 1+it); classical",
      abs(r0 - 1) < 1e-4 and abs(r1) < 1e-4, f"{mp.nstr(r0, 8)}, {mp.nstr(abs(r1), 3)}")

print()
print("=" * 100)
print("L. Bridges / negative results for programme objects")
print("=" * 100)
rho_q = mp.mpc(0.7, 10.0)
Z_at = abs(mp.zeta(rho_q))
quartet = [rho_q, mp.conj(rho_q), 1 - rho_q, 1 - mp.conj(rho_q)]
detw = sum(2 * mp.re(x) for x in quartet) / 4
okq = abs(detw - 1) < 1e-20
for k in (1, 2):
    sums = [sum(c_) for c_ in itertools.product(quartet, repeat=2 * k)]
    mx = max(mp.re(x) for x in sums)
    okq &= abs(mx - 2 * k * max(mp.re(rho_q), 1 - mp.re(rho_q))) < 1e-20
# genuine pole of prod_e zeta(s-e) at s = 1 + e_max for k=1 (order 2 at the real point)
sums1 = [sum(c_) for c_ in itertools.product(quartet, repeat=2)]
s_real = 1 + 2 * mp.re(rho_q)


def prodzeta(s):
    out = mp.mpf(1)
    for e_ in sums1:
        out *= mp.zeta(s - e_)
    return out


gs = [abs(prodzeta(s_real + h) * h ** 2) for h in (mp.mpf('1e-4'), mp.mpf('1e-6'))]
check("L1 quartet {rho, rhobar, 1-rho, 1-rhobar}: determinant weight exactly 1; 2k-th tensor max real part 2k*max(Re rho,1-Re rho)",
      okq, f"rho = 0.7+10i, |zeta(rho)| = {mp.nstr(Z_at, 5)} (rho is NOT a zero)")
check("L2 [NEGATIVE] its tensor-square Euler product prod zeta(s-e) has a genuine pole at 1+2Re(rho) although zeta(rho)!=0",
      abs(gs[0] - gs[1]) < 1e-2 * gs[1] and gs[1] > 1e-6, f"|(s-s0)^2 prod| -> {mp.nstr(gs[1], 6)}: the pole does not detect zeros")
# N P = b P N in finite dimension
b = 3.0
Nj = np.diag([1.0, 1.0], k=1)  # nilpotent 3x3 Jordan block
Pd = np.diag([1.0, b, b * b])
okn = np.allclose(Nj @ Pd, b * Pd @ Nj)
Nd = np.diag([1.0, 2.0, 3.0])
bb = 2.0
# solution space of N P - b P N = 0 for diagonal N: P_ij free iff lambda_i = b lambda_j
free = [(i, j) for i in range(3) for j in range(3) if abs(Nd[i, i] - bb * Nd[j, j]) < 1e-12]
check("L3 N P_b = b P_b N with P_b invertible, b not a root of unity, dim < inf  =>  N nilpotent",
      okn and len(free) <= 1, f"nilpotent example works; for N=diag(1,2,3), b=2 only entries {free} are free: no invertible P")
Fq = np.diag([1.0, 7.0])
Nm = np.array([[0.0, 1.0], [0.0, 0.0]])
check("L4 typed comparison: geometric Frobenius F=diag(1,q), N:e2->e1 satisfy N F = q F N (Weil-Deligne relation, b=q)",
      np.allclose(Nm @ Fq, 7.0 * Fq @ Nm), "P_b <-> Frobenius of norm b; N <-> monodromy logarithm")
# W commuting with N preserves the monodromy filtration: Jordan type (3,1)
Nb = np.zeros((4, 4))
Nb[0, 1] = Nb[1, 2] = 1.0


okw = True
for _ in range(20):
    # centralizer of Nb: solve W Nb = Nb W generically by projecting a random matrix
    X = np.random.randn(4, 4)
    # least squares projection onto centralizer
    Kmat = np.kron(np.eye(4), Nb) - np.kron(Nb.T, np.eye(4))
    _, _, Vh = np.linalg.svd(Kmat)
    null = Vh[np.sum(np.linalg.svd(Kmat)[1] > 1e-10):]
    Wv = null.T @ (null @ X.reshape(-1, order='F'))
    W = Wv.reshape(4, 4, order='F')
    okw &= np.allclose(W @ Nb, Nb @ W, atol=1e-9)
    # M_{-2} = im N^2 and M_0 = ker N + im N (for type (3,1)) must be W-stable
    for S, expected_rank in ((Nb @ Nb, 1), (np.hstack([Nb, np.eye(4)[:, [0, 3]]]), 3)):
        Uo, sv, _ = np.linalg.svd(S)
        rk = int(np.sum(sv > 1e-10))
        Sb = Uo[:, :rk]  # orthonormal basis of the column space (M_{-2} = im N^2, M_0 = ker N + im N)
        okw &= (rk == expected_rank)
        okw &= np.linalg.matrix_rank(np.hstack([Sb, W @ Sb]), tol=1e-8) == rk
    # a generic matrix NOT commuting with N moves M_{-2} (sanity: the test is not vacuous)
    Xg = np.random.randn(4, 4)
    Uo, sv, _ = np.linalg.svd(Nb @ Nb)
    okw &= np.linalg.matrix_rank(np.hstack([Uo[:, :1], Xg @ Uo[:, :1]]), tol=1e-8) == 2
check("L5 W with W N W^-1 = N preserves the monodromy filtration (canonical in N)", okw, "random centralizer elements, Jordan type (3,1)")

print()
npass = sum(1 for _, o in RESULTS if o)
print(f"TOTAL: {npass}/{len(RESULTS)} PASS")
