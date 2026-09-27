#!/usr/bin/env python3
"""ref_series_darboux.py -- referee check of the coefficient claims of note 51_ section 4.2 and of the Darboux asymptotics
that Theorem 51.2 implies (a consequence the note does not state).

(1) Independent computation of the Taylor coefficients a_k of alpha_h(x) = sum a_k x^k (x = q^2/4) by Newton iteration
    on truncated power series in Arb ball arithmetic (python-flint arb_series), up to k = N; comparison with the exact
    rationals of hydro_series_coeffs_first60.txt and with a_1..a_7 quoted in the note; signs of all a_k.
(2) Darboux: Theorem 51.2 (analytic on a neighbourhood of the closed disk |x| <= x* minus {x*}; square-root branch point
    at x*) implies  a_k = -C x*^(-k) k^(-3/2) (1 + O(1/k)),  C = kappa sqrt(x*) / (2 sqrt(pi)),
    kappa^2 = 2 G_x/G_aa = 4 F_q / (q* F_aa)  (alpha_h = alpha* + kappa sqrt(x* - x) + O(x* - x)).
    Checked by Richardson extrapolation of s_k = a_k x*^k k^(3/2).
(3) The corrected ratios (a_k/a_{k+1})/(1 + 3/(2k)) -> x* with O(1/k^2) error.
"""
import sys, time
from flint import arb_series, arb, ctx, fmpq
import mpmath as mp

N = int(sys.argv[1]) if len(sys.argv) > 1 else 320
T0 = time.time()
ctx.prec = 2400
ctx.cap = N + 2
res = []
def check(name, ok, extra=""):
    res.append((name, bool(ok))); print(("PASS" if ok else "FAIL") + "  " + name + (("  " + extra) if extra else ""), flush=True)

x = arb_series([0, 1], prec=N + 1)
def G_Ga(al):
    G = arb_series([0], prec=N + 1); Ga = arb_series([0], prec=N + 1)
    base = arb_series([1], prec=N + 1); S = arb_series([0], prec=N + 1)
    for m in range(0, N + 1):
        if m > 0:
            inv = 1 / (m + al)
            base = base * x * inv / m
            S = S + inv
        G = G + base * (al + 2 * m)
        Ga = Ga + base * (1 - (al + 2 * m) * S)
    return G, Ga
al = arb_series([0, -2], prec=N + 1)
for it in range(int(mp.log(N, 2)) + 3):
    G, Ga = G_Ga(al)
    al = al - G / Ga
G, Ga = G_Ga(al)
co = al.coeffs()
a = [co[k] if k < len(co) else arb(0) for k in range(N + 1)]
resid = max(abs(c).upper() for c in G.coeffs()) if G.coeffs() else arb(0)
print(f"computed a_k, k <= {N}, in {time.time()-T0:.0f}s; max |coeff of G(alpha_h(x), x)| <= {arb(resid).str(3)}")
# (1) comparison with the exact rationals
exact = {}
for line in open('../hydro_series_coeffs_first60.txt'):
    if line.startswith('#'):
        continue
    k, p, q = line.split()
    exact[int(k)] = fmpq(int(p), int(q))
ok1 = all(a[k].contains(arb(exact[k])) for k in exact)
check(f"arb-series coefficients contain the exact rationals a_1..a_{max(exact)} of hydro_series_coeffs_first60.txt", ok1)
quoted = {1: fmpq(-2), 2: fmpq(-3), 3: fmpq(-29, 3), 4: fmpq(-2843, 72), 5: fmpq(-392029, 2160), 6: fmpq(-14509367, 16200),
          7: fmpq(-63074754607, 13608000)}
check("a_1..a_7 quoted in note 51_ section 4.2 are correct", all(a[k].contains(arb(v)) for k, v in quoted.items()))
negs = all(a[k] < 0 for k in range(1, N + 1))
check(f"all a_k < 0 for 1 <= k <= {N} (decided by the balls)", negs)
maxrel = max((a[k].rad() / abs(a[k].mid())) for k in range(1, N + 1))
print(f"   worst relative ball radius of a_k: {arb(maxrel).str(3)}")

# (2) Darboux constant
mp.mp.dps = 40
qs = mp.mpf('0.778472800990330076180356446189')
Fq = mp.mpf('1.75035806101433995507814928965'); Faa = mp.mpf('5.00598854867858334954068222753')   # RESEARCH.md (32), numerical
xs = qs ** 2 / 4
kappa = mp.sqrt(4 * Fq / (qs * Faa))
C = kappa * mp.sqrt(xs) / (2 * mp.sqrt(mp.pi))
print(f"   kappa = {mp.nstr(kappa, 15)} (two_roots() in the certificate uses 1.34); predicted C = {mp.nstr(C, 15)}")
def af(k):
    return mp.mpf(a[k].mid().str(60, radius=False))
s = {k: af(k) * xs ** k * mp.mpf(k) ** mp.mpf(1.5) for k in range(1, N + 1)}
# Richardson extrapolation in 1/k (orders 1..4) at the end of the range
def richardson(f, ks, order):
    # fit f(k) = L + c1/k + ... + c_order/k^order through order+1 points and return L
    import itertools
    pts = ks[-(order + 1):]
    M = mp.matrix([[mp.mpf(1)] + [mp.mpf(1) / mp.mpf(kk) ** j for j in range(1, order + 1)] for kk in pts])
    rhs = mp.matrix([f[kk] for kk in pts])
    return mp.lu_solve(M, rhs)[0]
ks = list(range(N - 40, N + 1, 8))
for kk in (40, 100, 200, N):
    print(f"   s_{kk} = a_k x*^k k^(3/2) = {mp.nstr(s[kk], 12)}")
ests = [richardson(s, ks, o) for o in (1, 2, 3, 4)]
print("   Richardson limits (orders 1-4):", [mp.nstr(e, 12) for e in ests])
check("Darboux: a_k x*^k k^(3/2) -> -kappa sqrt(x*)/(2 sqrt(pi)) (relative agreement < 1e-6)", abs(ests[-1] + C) / C < mp.mpf('1e-6'),
      f"extrapolated {mp.nstr(ests[-1], 12)} vs -C = {mp.nstr(-C, 12)}")
# (3) corrected ratio
for kk in (40, 100, 200, N - 1):
    r = af(kk) / af(kk + 1) / (1 + mp.mpf(3) / (2 * kk))
    print(f"   k = {kk}: (a_k/a_(k+1))/(1+3/(2k)) - x* = {mp.nstr(r - xs, 6)};  times k^2: {mp.nstr((r - xs) * kk ** 2, 6)}")
# (4) consequence: absolute convergence on the circle |x| = x* and Abel sum at x = x*
#     sum_k a_k x*^k = alpha* (the series converges on the closed disk since a_k x*^k = O(k^(-3/2)))
pts = ks
M = mp.matrix([[mp.mpf(1)] + [mp.mpf(1) / mp.mpf(kk) ** j for j in range(1, 5)] for kk in pts])
coef = mp.lu_solve(M, mp.matrix([s[kk] for kk in pts]))        # s_k ~ L + c1/k + c2/k^2 + ...
L_, c1, c2 = coef[0], coef[1], coef[2]
SN = mp.fsum(af(k) * xs ** k for k in range(1, N + 1))
tail = L_ * mp.zeta(1.5, N + 1) + c1 * mp.zeta(2.5, N + 1) + c2 * mp.zeta(3.5, N + 1)
ast = mp.mpf('-0.569714080972361784438457668663')
print(f"   partial sum S_N = sum_(k<=N) a_k x*^k = {mp.nstr(SN, 15)}; Darboux tail estimate {mp.nstr(tail, 10)}; "
      f"S_N + tail = {mp.nstr(SN + tail, 15)}; alpha* = {mp.nstr(ast, 15)}")
check("Abel sum at the radius: S_N + Darboux tail = alpha* (to 1e-8): the series (27) converges also at |q^2| = q*^2",
      abs(SN + tail - ast) < mp.mpf('1e-8'), f"difference {mp.nstr(SN + tail - ast, 3)}")
n = len(res); npass = sum(ok for _, ok in res)
print(f"\nsummary: {n} checks, {npass} PASS, {n - npass} FAIL  [{time.time()-T0:.0f}s]")
