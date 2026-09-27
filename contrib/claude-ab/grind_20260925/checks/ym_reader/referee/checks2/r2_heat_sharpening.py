# Referee check: sharper constants for Section 4 of the YM reader (Theorem 4.1, Props. 4.2-4.4).
# (1) Lemma: if |p y| + ||T y|| <= chi ||y|| on an l^1-type space, then |p (I-T)^{-1} y| <= chi ||y||
#     (not chi/(1-chi)).  Proof in the report; here a randomized sanity test on l^1(n).
# (2) Consequence: ||Chat(tau)||_row <= (1+255chi)/(1-chi) e^{-3(1-chi)tau}, i.e. C' = 2829/13 at chi = 11/24.
# (3) The benchmark table recomputed with C' and with the alternative unobserved-fraction bound beta/(9 l_2).
# (4) Two-sided gap bound: Delta_L/kappa <= (K_o)_pp/(G_0)_pp <= (3+w_K)/(1-w_0).
# (5) Comparison of Theorem 4.1 with the earlier edition's U29b.
from fractions import Fraction as Fr
import numpy as np, mpmath as mp
mp.mp.dps = 40
rng = np.random.default_rng(1)

# ---- (1) randomized test of the mean lemma on l^1(n) (complex) ----
worst = 0.0
for trial in range(2000):
    n = rng.integers(2, 9)
    chi = rng.uniform(0.05, 0.95)
    Dm = rng.normal(size=(n + 1, n)) + 1j * rng.normal(size=(n + 1, n))
    colsum = np.abs(Dm).sum(axis=0)
    Dm = Dm / colsum * chi * rng.uniform(0.3, 1.0, size=n)   # l^1 -> l^1 norm <= chi (columnwise)
    p, T = Dm[0], Dm[1:]
    S = np.linalg.inv(np.eye(n) - T)
    pS = p @ S
    ratio = np.max(np.abs(pS)) / chi       # dual (l^inf) norm of y -> pSy, divided by chi
    worst = max(worst, ratio)
print(f"(1) max over 2000 random cases of ||pS||/chi = {worst:.6f}  (lemma says <= 1; old bound allowed 1/(1-chi))")

# ---- (2) constants ----
chi = Fr(11, 24)
C_old = (1 + 255 * chi) / (1 - chi)**2
C_new = (1 + 255 * chi) / (1 - chi)
C_new256 = (1 + 256 * chi) / (1 - chi)
print("(2) C_old =", C_old, float(C_old), "  C_new = (1+255chi)/(1-chi) =", C_new, float(C_new), "  (1+256chi)/(1-chi) =", C_new256, float(C_new256))
print("    ratio C_old/C_new = 1/(1-chi) =", C_old / C_new)

# exact chi at R = 1/55 from F26
m = {1: Fr(64, 3), 2: Fr(5834, 39), 3: Fr(336572872, 208845), 4: Fr(17270702970768271, 341697152160), 5: Fr(1638684)}
t = {1: Fr(16, 3), 2: Fr(137, 6), 3: Fr(225985217, 1253070), 4: Fr(110695177857394584026401, 18025447358750832000), 5: Fr(190128)}
def d5(x):
    ell = sum((m[i] + 4 * t[i]) * x**i for i in range(1, 6))
    dl = sum(3 * (m[i] * t[j] + m[j] * t[i]) * x**(i + j) for i in range(1, 6) for j in range(1, 6) if i + j >= 6)
    Dx = (1 - ell)**2 - Fr(8, 3) * dl
    s = sum((Fr(3, 2) * m[i] - 6 * t[i]) * x**i for i in range(1, 6))
    return mp.mpf(3) / 2 * (1 + mp.sqrt(mp.mpf(Dx.numerator) / Dx.denominator)) + mp.mpf(s.numerator) / s.denominator
chiR = 1 - d5(Fr(1, 55)) / 3
print("    exact chi(1/55) =", mp.nstr(chiR, 10), " C_old(exact chi) =", mp.nstr((1 + 255 * chiR) / (1 - chiR)**2, 8), " C_new(exact chi) =", mp.nstr((1 + 255 * chiR) / (1 - chiR), 8))

# ---- (3) benchmark table ----
d = Fr(13, 8)
e_bound = Fr(339, 1000)
def CJ_of(C): return C * (1 + 6 / d - 9 / d**2 + 18 * e_bound / d**2)
B = {'0': (Fr(149, 468), Fr(2361994073, 4691494080)), '1': (Fr(97, 468), Fr(376882691, 938298816)),
     '2': (Fr(73313, 657072), Fr(982069718963833, 3919180324550400)), 'K': (Fr(187, 468), Fr(586668421, 1563831360)),
     'J': (Fr(6779, 73008), Fr(152338674005989, 435464480505600))}
def widths(x, C):
    u = (55 * x)**6 / (1 - (55 * x)**2)
    w = {k: B[k][0] * x**2 + B[k][1] * x**4 + C / d**int(k) * u for k in '012'}
    w['K'] = B['K'][0] * x**2 + B['K'][1] * x**4 + 606 * u
    beta = B['J'][0] * x**2 + B['J'][1] * x**4 + CJ_of(C) * u
    return w, beta
def floor4(v): return Fr(int(v * 10000), 10000)
print("(3) g^2 | d_ph | [old C] fraction l1^2/(u0u2), 1-beta/(9 l2), etaE, etaG | [new C'] same four | gap upper bound (3+wK)/(1-w0)")
for g2 in (Fr(10), Fr(12), Fr(25, 2), Fr(13), Fr(16)):
    x = 1 / (4 * g2**2)
    dph = Fr(29047, 10000) if g2 == 13 else floor4(d5(x))
    row = [str(g2), str(dph)]
    for C in (C_old, C_new):
        w, beta = widths(x, C)
        l = {k: Fr(1, 3**int(k)) - w[k] for k in '012'}; uu = {k: Fr(1, 3**int(k)) + w[k] for k in '012'}
        fr = l['1']**2 / (uu['0'] * uu['2'])
        fr2 = 1 - beta / (9 * l['2'])
        etaE = beta / (dph * l['1']); etaG = beta / (dph**2 * l['2'])
        row += [f"{float(fr):.7f}", f"{float(fr2):.7f}", f"{float(etaE):.3e}", f"{float(etaG):.3e}"]
    w, beta = widths(x, C_old)
    ub = (3 + w['K']) / (1 - w['0'])
    row.append(f"d5={mp.nstr(d5(x), 7)} <= Delta/kappa <= {float(ub):.6f}")
    print("   ", " | ".join(row))

# ---- (5) Theorem 4.1 versus the earlier U29b (R1 = 45/4096, prefactor 6184/25, rate 15/8) ----
R1 = Fr(45, 4096)
q = float(55 * R1)
tau_star = 4 * np.log(1 / (float(C_old) / (6184 / 25) * q**6))
print(f"(5) 55*R1 = {q:.5f}; as xi -> 0, U29b is sharper than Theorem 4.1 for tau > {tau_star:.3f}")
chi1 = 1 - d5(R1) / 3
print("    the reader's 'other radii' family at R = R1: rate d5(R1) =", mp.nstr(d5(R1), 8), " prefactor (1+255chi)/(1-chi)^2 =", mp.nstr((1 + 255 * chi1) / (1 - chi1)**2, 8),
      " (so the family, not Theorem 4.1 itself, supersedes U29b)")
