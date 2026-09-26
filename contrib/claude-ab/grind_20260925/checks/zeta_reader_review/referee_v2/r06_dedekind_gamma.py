#!/usr/bin/env python3
"""Referee v2, script r06.  The Dedekind separator paragraph (Section 4.6 of the reader v2).

 1. Gamma_R(1-s) Gamma_R(1+s) = 1/cos(pi s/2) and Gamma_C(1-s) Gamma_C(1+s) = s/(pi sin(pi s)),
    Gamma_R(s) = pi^{-s/2} Gamma(s/2), Gamma_C(s) = 2 (2 pi)^{-s} Gamma(s), at random complex points.
 2. The rate: for (r1, r2) and n = r1 + 2 r2, |Gamma part of xi_K(1-s) xi_K(1+s)| * e^{n pi |t|/2}
    = |1/cos(pi s/2)|^{r1} |s/(pi sin pi s)|^{r2} e^{n pi|t|/2} is polynomially bounded above and below on the
    vertical lines x in {-1, -0.5, 0, 0.5, 1}: its log minus r2*log|t| tends to r1 log 2 + r2 log(2/pi).
 3. The functional equation of a Dedekind zeta function numerically: K = Q(i), zeta_K = zeta(s) L(s, chi_-4),
    Lambda_K(s) = |d|^{s/2} Gamma_C(s) zeta_K(s) (d = -4, r1 = 0, r2 = 1) satisfies Lambda_K(s) = Lambda_K(1-s).
"""
import mpmath as mp, random
mp.mp.dps = 40
ok_all = True
def rep(name, cond, info=""):
    global ok_all
    ok_all &= bool(cond); print(("[PASS] " if cond else "[FAIL] ") + name + ("" if not info else ": " + str(info)))
GR = lambda s: mp.pi**(-s / 2) * mp.gamma(s / 2)
GC = lambda s: 2 * (2 * mp.pi)**(-s) * mp.gamma(s)
random.seed(7); w1 = w2 = 0
for _ in range(30):
    s = mp.mpc(random.uniform(-3, 3), random.uniform(-40, 40))
    w1 = max(w1, abs(GR(1 - s) * GR(1 + s) * mp.cos(mp.pi * s / 2) - 1))
    w2 = max(w2, abs(GC(1 - s) * GC(1 + s) * mp.pi * mp.sin(mp.pi * s) / s - 1))
rep("1  Gamma identities at 30 random points", w1 < 1e-30 and w2 < 1e-30, f"max errors {mp.nstr(w1, 3)}, {mp.nstr(w2, 3)}")

worst = 0
for r1, r2 in ((1, 0), (2, 0), (0, 1), (3, 0), (1, 1), (4, 0), (2, 1), (0, 2)):
    n = r1 + 2 * r2
    for x in (-1, -0.5, 0, 0.5, 1):
        for T in (60, 120):
            s = mp.mpc(x, T)
            g = abs(1 / mp.cos(mp.pi * s / 2))**r1 * abs(s / (mp.pi * mp.sin(mp.pi * s)))**r2
            val = mp.log(g) + n * mp.pi * T / 2 - r2 * mp.log(T) - (r1 * mp.log(2) + r2 * mp.log(2 / mp.pi))
            worst = max(worst, abs(val))
rep("2  rate e^{-n pi|t|/2} with polynomial factor |t|^{r2} on every vertical line (n = r1 + 2 r2)", worst < 1e-3, f"max |log-deviation| {mp.nstr(worst, 3)} at T = 60, 120")

def chi4(n): return 0 if n % 2 == 0 else (1 if n % 4 == 1 else -1)
def LamK(s):
    zK = mp.zeta(s) * mp.dirichlet(s, [0, 1, 0, -1])
    return mp.power(4, s / 2) * GC(s) * zK
ws = 0
for s in (mp.mpc('0.3', '7.1'), mp.mpc('-0.4', '12.5'), mp.mpc('0.8', '-3.3')):
    ws = max(ws, abs(LamK(s) - LamK(1 - s)) / abs(LamK(s)))
rep("3  Q(i): Lambda_K(s) = Lambda_K(1-s) with Gamma_C (r2 = 1)", ws < 1e-25, f"max rel. error {mp.nstr(ws, 3)}")
print("ALL CHECKS PASS" if ok_all else "SOME CHECKS FAILED")
