# Checks for 31_ (audit of NJS0-NJS10, SSR0-SSR7 and RSR0-RSR8, in the programme's working folder
# quantum_tau_programme_bridge_20260924/next_edition_after_647).
# claude-ab (Opus 5.5, max effort), 25 September 2026.
import mpmath as mp
import sympy as sp

mp.mp.dps = 40
ok_all = True


def report(name, ok, detail=''):
    global ok_all
    ok_all &= bool(ok)
    print(('PASS ' if ok else 'FAIL ') + name + ('  ' + detail if detail else ''))


def F0(s):
    return s * (s - 1) / 8 * mp.pi ** (-s / 2) * mp.gamma(s / 2) * mp.zeta(s)


t = mp.mpf('0.3')
g = lambda s: mp.exp(t * s ** 2)
h = lambda s: 8 * g(s) * F0(s) / s          # h_t
j = lambda s: g(s) / s                      # j_t
k = lambda s: j(s) - h(s)                   # k_t = g (1 - 8 F0)/s
eta = lambda n, s: g(s) * (n - mp.power(n, 1 - s)) / s
delta = lambda n, s: 8 * g(s) * F0(s) * (n - mp.power(n, 1 - s)) / s

# 1. NJS1.2: k_t(0) = -8 F0'(0) = -xi'(0)/xi(0) = -((1/2) log(4 pi) - 1 - gamma/2)
eps = mp.mpf('1e-15')
k0 = (k(eps) + k(-eps)) / 2
B0 = mp.log(4 * mp.pi) / 2 - 1 - mp.euler / 2
dF0 = mp.diff(lambda s: F0(s), mp.mpf('1e-30')) if False else (F0(mp.mpf('1e-12')) - F0(mp.mpf('-1e-12'))) / mp.mpf('2e-12')
report('1  NJS1.2: k_t(0) = -8 F0\'(0) = -(log(4 pi)/2 - 1 - gamma/2)', abs(k0 + 8 * dF0) < 1e-10 and abs(k0 + B0) < 1e-10,
       'k_t(0) = %s' % mp.nstr(k0, 15))

# 2. NJS2.1-2.3: eta_n(0) = delta_n(0) = n log n; eta - delta = (n - U_n) k; cocycle eta_mn = m eta_n + U_n eta_m.
ok2 = True
for n in [2, 3, 7]:
    ok2 &= abs((eta(n, eps) + eta(n, -eps)) / 2 - n * mp.log(n)) < 1e-10
    ok2 &= abs((delta(n, eps) + delta(n, -eps)) / 2 - n * mp.log(n)) < 1e-10
    for s in [mp.mpc('0.3', '4.1'), mp.mpc('-2.2', '0.5')]:
        ok2 &= abs(eta(n, s) - delta(n, s) - (n * k(s) - mp.power(n, 1 - s) * k(s))) < 1e-25 * (1 + abs(eta(n, s)))
        for m in [2, 5]:
            ok2 &= abs(eta(m * n, s) - (m * eta(n, s) + mp.power(n, 1 - s) * eta(m, s))) < 1e-25 * (1 + abs(eta(m * n, s)))
report('2  NJS2.1-2.3: both discrepancies have value n log n at 0; eta - delta = (n - U_n) k; cocycle law', ok2)

# 3. NJS5.5 and SSR3.5 at the first two nontrivial zeros: h_t(rho) = 0, k_t(rho) = g(rho)/rho, eta_n(rho) != 0.
ok3 = True
for m in [1, 2]:
    rho = mp.zetazero(m)
    # g_t(rho) = e^{t rho^2} is tiny (about e^{-60} at rho_1 with t = 0.3), so compare after dividing by g_t(rho)
    gr = g(rho)
    ok3 &= abs(h(rho) / gr) < 1e-30 and abs(k(rho) / gr - 1 / rho) < 1e-30
    ok3 &= all(abs(eta(n, rho) / gr) > 1e-3 for n in [2, 3, 10])
report('3  NJS5.5 / SSR3.5: at rho_1, rho_2: h_t(rho) = 0, k_t(rho) = g_t(rho)/rho, eta_n(rho) != 0', ok3)

# 4. NJS5 existence remark: F0 zero-free would force F0 = const (symmetry), contradicting F0(0) = 1/8 != pi/24 = F0(2).
report('4  NJS5 remark (elementary): F0(0) = 1/8 and F0(2) = pi/24 differ (pi != 3)', abs(F0(mp.mpf(2)) - mp.pi / 24) < 1e-35 and abs(mp.pi / 24 - mp.mpf(1) / 8) > 1e-3)

# 5. NJS6.3 and NJS6.5b: F^j_{t,0} = 0, F^j_{t,m} = g (m^{1-s} - (m+1)^{1-s} + 1)/s, and sum_{a<n} F^j_{t,a} = eta_n.
def phi(m, s):
    return -1 / s if m == 0 else (mp.power(m, 1 - s) - mp.power(m + 1, 1 - s)) / s
ok5 = True
for s in [mp.mpc('0.7', '2.0'), mp.mpc('1.9', '-3.1')]:
    Fj = [g(s) * phi(m, s) + j(s) for m in range(12)]
    ok5 &= abs(Fj[0]) < 1e-30
    ok5 &= all(abs(Fj[m] - g(s) * (mp.power(m, 1 - s) - mp.power(m + 1, 1 - s) + 1) / s) < 1e-28 for m in range(1, 12))
    ok5 &= all(abs(mp.fsum(Fj[:n]) - eta(n, s)) < 1e-28 for n in range(2, 12))
report('5  NJS6.3, NJS6.5b: corrected coefficients and the telescoped block sum = eta_n', ok5)

# 6. Lemma 31.1 (sharpness): for S = {a^k}, evaluation at s0 = 2 pi i/log a annihilates every eta_{a^k}; it is nonzero on B.
ok6 = True
for a in [2, 3, 10]:
    s0 = 2j * mp.pi / mp.log(a)
    # divide by the Gaussian g_t(s0) = e^{-t (2 pi/log a)^2}, which is small for a = 2, 3
    ok6 &= all(abs(eta(a ** kk, s0) / g(s0)) < 1e-30 * a ** kk for kk in range(1, 8)) and abs(g(s0)) > 0
    # but not for a non-power of a: n = a + 1
    ok6 &= abs(eta(a + 1, s0) / g(s0)) > 1e-3
report('6  Lemma 31.1: ev at 2 pi i/log a kills eta_{a^k} for all k (a = 2, 3, 10), and does not kill eta_{a+1}', ok6)

# 7. Lemma 31.2: pushout of the residue extension along ev_{s0}.
# At s0 = 0: in the basis (e, [h]) the cover acts by n [[1, -log n], [0, 1]]; multiplicative; class -log (nonsplit).
ok7 = True
U = lambda n: sp.Matrix([[n, -n * sp.log(n)], [0, n]])
for (m, n) in [(2, 3), (4, 6), (5, 5)]:
    ok7 &= sp.simplify(U(m) * U(n) - U(m * n)).applyfunc(lambda z: sp.simplify(sp.expand_log(z, force=True))) == sp.zeros(2, 2)
# Ext^1(C_chi, C_psi) = 0 for chi != psi: the cocycle is a coboundary with b = c(n0)/(chi(n0) - psi(n0)) independent of n.
# At s0 != 0 the pushout along ev_{s0} is split by h_t(s0): delta_n(s0)/(n - n^{1-s0}) = h_t(s0) for every n.
for s0 in [mp.mpc('0.4', '1.3'), mp.mpc('-1.5', '0'), 2j * mp.pi / mp.log(2)]:
    ratios = []
    for n in [2, 3, 5, 12]:
        den = n - mp.power(n, 1 - s0)
        if abs(den) > 1e-20:
            ratios.append(delta(n, s0) / den)
    ok7 &= len(ratios) >= 2 and max(abs(r_ - h(s0)) for r_ in ratios) < 1e-25 * (1 + abs(h(s0)))
# the obstruction at 0: an extension value v would need n v - n log n = n v for all n: impossible since log 2 != 0
ok7 &= mp.log(2) != 0
# genuine numerical test of (b) = NPE4.2: Laurent data j(f) = (a_0, res_0 f) by contour integrals on |s| = 0.1,
# for f = h_t and f = U_n h_t = n^{1-s} h_t, and for f = h_t + F with F = g_t (entire, F(0) = 1).
def laurent(fun):
    r0 = mp.mpf('0.1')
    res = mp.quad(lambda th: fun(r0 * mp.expj(th)) * r0 * mp.expj(th), [0, 2 * mp.pi]) / (2 * mp.pi)
    a0 = mp.quad(lambda th: fun(r0 * mp.expj(th)), [0, 2 * mp.pi]) / (2 * mp.pi)
    return a0, res
err7b = 0
for f in [h, lambda z: h(z) + g(z)]:
    a0, c0 = laurent(f)
    for n in [2, 3, 7]:
        a0n, c0n = laurent(lambda z, n=n, f=f: mp.power(n, 1 - z) * f(z))
        pred = (n * a0 - n * mp.log(n) * c0, n * c0)
        err7b = max(err7b, abs(a0n - pred[0]), abs(c0n - pred[1]))
ok7 &= err7b < 1e-25
report('7  Lemma 31.2 / NPE4.2: Laurent data j(U_n f) = n(I - log n N) j(f) computed by contour integrals for f = h_t, h_t + g_t and n = 2, 3, 7; '
       'the 2x2 matrices multiply correctly; at s0 != 0 the cocycle is the coboundary of h_t(s0) (an identity, since delta_n = (n - n^{1-s}) h_t)', ok7,
       'contour err %.1e' % err7b)

# 8. RSR7: I in P B iff roots of P are actual zeros with d_a <= m_a (test: P(s) = (1 - s/rho1)(1 - s/conj(rho1)) divides F0 near rho1).
rho1 = mp.zetazero(1)
P = lambda s: (1 - s / rho1) * (1 - s / mp.conj(rho1))
qfun = lambda s: F0(s) / P(s)
val = (qfun(rho1 + mp.mpf('1e-12')) + qfun(rho1 - mp.mpf('1e-12'))) / 2
report('8  RSR7 instance (elementary): F0/P is regular at rho_1 (P with roots rho_1, conj rho_1, P(0) = 1), value finite and nonzero', abs(P(0) - 1) < 1e-35 and 1e-8 < abs(val) < 1e8,
       '|F0/P|(rho_1) = %s' % mp.nstr(abs(val), 10))

print('ALL PASS' if ok_all else 'SOME CHECK FAILED')
