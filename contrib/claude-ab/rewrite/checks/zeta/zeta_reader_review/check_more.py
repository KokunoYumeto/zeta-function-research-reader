#!/usr/bin/env python3
"""Further checks for the understatement report."""
import mpmath as mp, numpy as np
mp.mp.dps = 25
ok = True
def report(name, cond, extra=""):
    global ok
    ok &= bool(cond)
    print(f"[{'ok' if cond else 'FAIL'}] {name} {extra}")

# (a) Lemma 5.6 with delta_n = C D^n: conclusion max|a_j| <= D (and fails when D < max|a_j|)
a = [1.5*np.exp(0.3j), 1.5*np.exp(-0.3j), -0.7]
for D, expect in [(1.6, True), (1.5, True), (1.4, False)]:
    vals = [2*D**n + 1 - sum(x**n for x in a) for n in range(1, 400)]
    allpos = all(abs(v.imag) < 1e-6*abs(v) + 1e-9 and v.real >= 0 for v in vals)
    report(f"(a) delta_n = 2 D^n + 1, D = {D}: delta_n - sum a_j^n >= 0 for all n <= 399 is {allpos} (max|a_j| = 1.5)", allpos == expect)
# curve application: |alpha_j| <= q from #X(F_{q^n}) = 1 + q^n - sum alpha^n >= 0 (e.g. an elliptic curve, q = 7, a_p = 3)
q, ap = 7, 3
al = np.roots([1, -ap, q])
cnt = [1 + q**n - sum(x**n for x in al) for n in range(1, 30)]
report("(a') elliptic curve q=7, a=3: point counts >= 0 and |alpha| = sqrt(q) <= q", all(c.real >= 0 for c in cnt) and max(abs(al)) <= q)

# (b) Prop 4.6: negative index of Q_A on T-even data = number of off-line pairs in the support
rng = np.random.default_rng(5)
def omega_matrix(n_on, n_pairs):
    N = n_on + 2*n_pairs
    M = np.zeros((N, N), complex)
    m = rng.integers(1, 4, size=N)
    for i in range(n_on):
        M[i, i] = m[i]
    for p in range(n_pairs):
        i, j = n_on + 2*p, n_on + 2*p + 1
        M[i, j] = M[j, i] = m[i]       # rho <-> rho#
    return M
good = True
for n_on in range(0, 5):
    for n_pairs in range(0, 5):
        if n_on + n_pairs == 0: continue
        ev = np.linalg.eigvalsh(omega_matrix(n_on, n_pairs))
        good &= (np.sum(ev < -1e-12) == n_pairs) and (np.sum(ev > 1e-12) == n_on + n_pairs)
report("(b) signature of Weil's pairing (= Q_A/2 on T-even data) is (n_on + n_pairs, n_pairs)", good)

# (c) Thm 4.2 / Prop 4.6 for L(s, chi), chi mod 5 complex (chi(2) = i): zeros are #-symmetric: L(1 - conj(rho), chi) = 0
chi = {1: 1, 2: 1j, 4: -1, 3: -1j}
Lchi = lambda s: mp.mpf(5)**(-s)*mp.fsum(chi[r]*mp.zeta(s, mp.mpf(r)/5) for r in range(1, 5))
found = []
with mp.workdps(15):
    ts = np.arange(0.5, 25, 0.05)
    vals = [abs(Lchi(mp.mpc(0.5, t))) for t in ts]
mins = [ts[i] for i in range(1, len(ts) - 1) if vals[i] < vals[i-1] and vals[i] < vals[i+1] and vals[i] < 0.3]
for g0 in mins[:5]:
    z = mp.findroot(Lchi, mp.mpc(0.5, g0))
    if abs(Lchi(z)) < 1e-15:
        found.append(z)
found = sorted(found, key=lambda z: z.imag)[:6]
worst = max(abs(Lchi(1 - mp.conj(z))) for z in found)
report("(c) zeros of L(s,chi) (chi mod 5 complex) are invariant under rho -> 1 - conj(rho)", worst < 1e-12,
       f"({len(found)} zeros, first {mp.nstr(found[0],10)}; max |L(1-conj rho)| = {mp.nstr(worst,3)}); so A(Z_chi) = Z_chi - 1")
# note: rho -> 1 - rho is NOT a symmetry of Z_chi for complex chi
report("(c') but 1 - rho is not a zero of L(s,chi) (it is a zero of L(s, conj chi))", abs(Lchi(1 - found[0])) > 1e-3, f"(|L(1-rho,chi)| = {mp.nstr(abs(Lchi(1 - found[0])),4)})")

# (d) inputs of Thm 3.9 for L(s,chi): |1/L(2+it)| <= zeta(2); |L(-1+it,chi)| bounded below on the left line
m2 = max(abs(1/Lchi(mp.mpc(2, t))) for t in np.linspace(-100, 100, 401))
m1 = min(abs(Lchi(mp.mpc(-1, t)))/(1 + abs(t))**1.5 for t in list(np.linspace(-100, -2, 197)) + list(np.linspace(2, 100, 197)))   # |t| >= 2 (chi odd: trivial zero at s = -1)
report("(d) |1/L(2+it,chi)| <= zeta(2) on [-100,100]; |L(-1+it,chi)| >= c (1+|t|)^{3/2} for 2 <= |t| <= 100", m2 <= mp.zeta(2) and m1 > 0.01, f"(max |1/L(2+it)| {mp.nstr(m2,4)}, min |L(-1+it)|/(1+|t|)^1.5 = {mp.nstr(m1,4)})")

# (e) Dedekind zeta of Q(i): matched exponential rates alpha = pi for G_K(s) = xi_K(s) xi_K(s+1)
chi4 = lambda s: mp.mpf(4)**(-s)*(mp.zeta(s, mp.mpf(1)/4) - mp.zeta(s, mp.mpf(3)/4))
zK = lambda s: mp.zeta(s)*chi4(s)
xiK = lambda s: s*(s - 1)*mp.mpf(4)**(s/2)*2*(2*mp.pi)**(-s)*mp.gamma(s)*zK(s)
GK = lambda s: xiK(s)*xiK(s + 1)
sym = max(abs(xiK(s) - xiK(1 - s))/abs(xiK(s)) for s in [mp.mpc(0.3, 5), mp.mpc(-0.7, 11), mp.mpc(1.9, 2)])
report("(e1) xi_K(s) = xi_K(1-s) for K = Q(i)", sym < 1e-18)
slopes = []
for x in [-1.5, 0.0, 0.7, 2.0]:
    f = lambda t: mp.log(abs(GK(mp.mpc(x, t)))) + mp.pi*t
    sl = (f(80) - f(40))/mp.log(2)          # local polynomial order between t = 40 and 80
    slopes.append(sl)
    print(f"      Re s = {x:4}: log(|G_K| e^(pi t)) at t = 40, 80: {mp.nstr(f(40),6)}, {mp.nstr(f(80),6)};  local order {mp.nstr(sl,4)}")
# with a mismatched rate e^{-alpha t}, alpha != pi, the log would change by about |pi - alpha|*40 >= 40*0.1 between 40 and 80
report("(e2) |G_K(x+it)| = t^{O(1)} e^{-pi |t|} on every line x (matched rates, alpha = n pi/2 = pi)", all(abs(s) < 15 for s in slopes))
# (f) Lemma 4.13 direction: |d_r/d_t| increasing in |x| iff r > t
def ratio(r, t, x): return np.sqrt(r/t)*np.sinh(x*np.log(r))/np.sinh(x*np.log(t))
xs = np.linspace(1e-4, 0.5, 500)
inc = all(np.all(np.diff(ratio(r, t, xs)) > 0) == (r > t) for r in (1.1, 2, 5, 30) for t in (1.1, 2, 5, 30) if r != t)
report("(f) Lemma 4.13: the ratio is increasing in |x| exactly when r > t", inc)

# (g) Lemma 3.6: constant (1+|gamma|)/(1/2+|gamma|) in place of 2 per power of M, for the first 20 zeros
F = lambda s: mp.exp(s*s/100)
_tt = np.linspace(0, 40, 2001)
b2c = {M: max((1 + abs(t))**M*abs(F(mp.mpc(sg, t))) for sg in (-2, 2) for t in _tt) for M in (0, 1, 2, 3)}
b2 = lambda M: b2c[M]
worst = 0
for k in range(1, 21):
    rho = mp.zetazero(k); gam = abs(rho.imag)
    for M in (0, 1, 2, 3):
        for r in (0, 1, 2):
            lhs = (1 + gam)**M*abs(mp.diff(F, rho, r))/mp.factorial(r)
            rhs = 2**r*((1 + gam)/(mp.mpf(1)/2 + gam))**M*b2(M)
            worst = max(worst, lhs/rhs)
report("(g) (1+|g|)^M |F^(r)(rho)/r!| <= 2^r ((1+|g|)/(1/2+|g|))^M b_{2,M}(F), first 20 zeros", worst <= 1, f"(max ratio {mp.nstr(worst,4)}; factor at gamma_1 = {mp.nstr((1+14.1347)/(0.5+14.1347),5)})")
print("\nALL CHECKS PASS" if ok else "\nSOME CHECK FAILED")
