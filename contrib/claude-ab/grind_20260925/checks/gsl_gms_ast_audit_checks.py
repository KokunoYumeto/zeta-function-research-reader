# Checks for 24_ (audit of GSL, GMS and AST; commit 064f33b of the three-lane continuation).
# claude-ab (Opus 5.5, max effort), 25 September 2026.
# Every item prints PASS/FAIL with the residual it measured.
import mpmath as mp

mp.mp.dps = 40
ok_all = True


def report(name, ok, detail=''):
    global ok_all
    ok_all &= bool(ok)
    print(('PASS ' if ok else 'FAIL ') + name + ('  ' + detail if detail else ''))


def F0(s):
    """F0(s) = s(s-1)/8 * pi^(-s/2) Gamma(s/2) zeta(s) = xi(s)/4, entire; uses F0(s) = F0(1-s) left of 1/2."""
    s = mp.mpc(s)
    if abs(s) < mp.mpf(10) ** -30 or abs(s - 1) < mp.mpf(10) ** -30:
        return mp.mpf(1) / 8
    if mp.re(s) < 0.5:
        s = 1 - s
        if abs(s - 1) < mp.mpf(10) ** -30:
            return mp.mpf(1) / 8
    return s * (s - 1) / 8 * mp.pi ** (-s / 2) * mp.gamma(s / 2) * mp.zeta(s)


def G(s):
    return F0(s) * F0(s + 1)


# 1. GSL3.7 in closed form: G(s) = s^2 (s^2 - 1) zeta(1-s) zeta(1+s) / (64 cos(pi s/2))
err = 0
for s in [mp.mpc(0.3, 5), mp.mpc(-0.7, 12), mp.mpc(1.3, -3), mp.mpc(0.05, 30), mp.mpc(-2.2, 7.5)]:
    rhs = s ** 2 * (s ** 2 - 1) * mp.zeta(1 - s) * mp.zeta(1 + s) / (64 * mp.cos(mp.pi * s / 2))
    err = max(err, abs(G(s) - rhs) / abs(rhs))
report('1  G(s) = s^2(s^2-1) zeta(1-s) zeta(1+s)/(64 cos(pi s/2))  (GSL3.5-3.7)', err < 1e-30, 'max rel err %.1e' % err)

# 2. G(0) = 1/64 and G(it) = |F0(1+it)|^2 > 0 on the line of the pole at 0
e2 = abs(G(0) - mp.mpf(1) / 64)
e2b = 0
for t in [1, 10, 50, 120]:
    g = G(mp.mpc(0, t))
    e2b = max(e2b, abs(g - abs(F0(mp.mpc(1, t))) ** 2) / abs(g), abs(mp.im(g)) / abs(g))
report('2  G(0) = 1/64 and G(it) = |F0(1+it)|^2 > 0', e2 < 1e-35 and e2b < 1e-30, 'errs %.1e, %.1e' % (e2, e2b))

# 3. Exceptional values (GSL1.4-1.5, GMS2.11, AST1.3)
e3 = abs(F0(-1) - mp.pi / 24) + abs(F0(2) - mp.pi / 24)
for r in range(1, 5):
    lhs = F0(-2 * r)
    rhs = r * (2 * r + 1) * (-1) ** r * mp.pi ** r / (2 * mp.factorial(r)) * mp.zeta(-2 * r, derivative=1)
    rhs2 = (1 + 2 * r) * (2 * r) / mp.mpf(8) * mp.pi ** (-(1 + 2 * r) / mp.mpf(2)) * mp.gamma((1 + 2 * r) / mp.mpf(2)) * mp.zeta(1 + 2 * r)
    e3 = max(e3, abs(lhs - rhs) / abs(rhs), abs(lhs - rhs2) / abs(rhs2))
report('3  F0(-1) = F0(2) = pi/24; F0(-2r) = r(2r+1)(-1)^r pi^r zeta\'(-2r)/(2 r!) = F0(1+2r), r = 1..4', e3 < 1e-30, 'max err %.1e' % e3)

# 4. The source vector f0 (GMS2.5, AST1.3): int_0^oo f0(v) v^(s-1) dv = s(s-1)/8 pi^(-s/2) Gamma(s/2)
f0 = lambda v: mp.pi / 2 * v ** 2 * (2 * mp.pi * v ** 2 - 3) * mp.exp(-mp.pi * v ** 2)
e4 = 0
for s in [mp.mpf(2.5), mp.mpc(3, 2), mp.mpc(0.5, 1), mp.mpc(-1.2, 0.7)]:
    lhs = mp.quad(lambda v: f0(v) * v ** (s - 1), [0, 1, mp.inf])
    rhs = s * (s - 1) / 8 * mp.pi ** (-s / 2) * mp.gamma(s / 2)
    e4 = max(e4, abs(lhs - rhs) / abs(rhs))
e4b = abs(mp.quad(f0, [0, 1, mp.inf]))   # int f0 = 0, and f0(0) = 0
report('4  Mellin transform of f0 is C0(s) = s(s-1)/8 pi^(-s/2) Gamma(s/2); int f0 = 0', e4 < 1e-25 and e4b < 1e-30, 'errs %.1e, %.1e' % (e4, e4b))

# 5. Poisson identity used in GMS9.1: Sigma ghat(u) = u^-1 Sigma g(1/u) + u^-1 g(0) - int g  (Sigma f(u) = 2 sum_{n>=1} f(nu))
Sig = lambda f, u: 2 * mp.nsum(lambda n: f(n * u), [1, mp.inf])
e5 = 0
for (g, gh, gint) in [(lambda v: mp.exp(-mp.pi * v ** 2), lambda x: mp.exp(-mp.pi * x ** 2), 1),
                      (lambda v: mp.exp(-2 * mp.pi * v ** 2), lambda x: mp.exp(-mp.pi * x ** 2 / 2) / mp.sqrt(2), 1 / mp.sqrt(2))]:
    for u in [mp.mpf('0.7'), mp.mpf('1.3')]:
        lhs = Sig(gh, u)
        rhs = Sig(g, 1 / u) / u + g(0) / u - gint
        e5 = max(e5, abs(lhs - rhs))
report('5  Poisson: Sigma ghat(u) = u^-1 Sigma g(1/u) + u^-1 g(0) - int g', e5 < 1e-30, 'max err %.1e' % e5)

# 6. The 3-4-2 inequality (GSL3.1-3.2): (1+2cos x)^2 = 3 + 4cos x + 2cos 2x, and the zeta product >= 1
e6 = max(abs((1 + 2 * mp.cos(x)) ** 2 - (3 + 4 * mp.cos(x) + 2 * mp.cos(2 * x))) for x in mp.linspace(0, 7, 50))
mn = mp.inf
for d in [mp.mpf('0.01'), mp.mpf('0.1'), mp.mpf('0.25')]:
    for t in mp.linspace(1, 100, 199):
        v = mp.zeta(1 + d) ** 3 * abs(mp.zeta(mp.mpc(1 + d, t))) ** 4 * abs(mp.zeta(mp.mpc(1 + d, 2 * t))) ** 2
        mn = min(mn, v)
report('6  (1+2cos)^2 identity; zeta(1+d)^3 |zeta(1+d+it)|^4 |zeta(1+d+2it)|^2 >= 1 on a grid', e6 < 1e-35 and mn >= 1, 'identity err %.1e; grid min %.4f' % (e6, mn))

# 7. Matched exponential rates (GSL3.9-3.10): |G| e^{pi|t|/2} is polynomially bounded above on strips and below on the line
lo = mp.inf
for t in mp.linspace(1, 200, 400):
    lo = min(lo, abs(G(mp.mpc(0, t))) * mp.exp(mp.pi * t / 2))
hi = 0
for x in [-2, 0.5, 2]:
    for t in mp.linspace(1, 200, 200):
        hi = max(hi, abs(G(mp.mpc(x, t))) * mp.exp(mp.pi * t / 2) / (1 + t) ** 12)
report('7  |G(it)| e^{pi t/2} bounded below on [1,200]; |G(x+it)| e^{pi t/2} <= C(1+t)^12 for x in {-2, 1/2, 2}', lo > 1e-3 and hi < 1e3,
       'min %.3e; max ratio %.3e' % (lo, hi))

# 8. AST: the defect d_r(rho) = e^{-i Im(rho) log r}(r^Re rho - r^{1-Re rho}); |d_r(rho)| = |r^rho - r^{rho#}|, d_r(rho#) = -d_r(rho)
d = lambda r, rho: mp.exp(-1j * mp.im(rho) * mp.log(r)) * (r ** mp.re(rho) - r ** (1 - mp.re(rho)))
sharp = lambda r, rho: 1 - mp.conj(rho)
e8 = 0
for rho in [mp.mpc(0.5, 14.1347), mp.mpc(0.3, 40), mp.mpc(0.9, 7), mp.mpc(0.51, 1000)]:
    for r in [mp.mpf('1.1'), mp.mpf(2), mp.mpf(30)]:
        direct = r ** mp.conj(rho) - r ** (1 - rho)           # (T_r^* - r T_{1/r}) eigenvalue
        e8 = max(e8, abs(direct - d(r, rho)), abs(abs(d(r, rho)) - abs(r ** rho - r ** sharp(r, rho))), abs(d(r, sharp(r, rho)) + d(r, rho)))
report('8  d_r(rho) = r^conj(rho) - r^(1-rho); |d_r| = |r^rho - r^(rho#)|; d_r(rho#) = -d_r(rho)', e8 < 1e-30, 'max err %.1e' % e8)

# 9. AST6.2 bounds and the sharp range of |d_r/d_t| off the line:
#    |d_r/d_t| = sqrt(r/t) sinh(x log r)/sinh(x log t), x = Re rho - 1/2, monotone in |x|,
#    strictly between sqrt(r/t) log r/log t (x -> 0) and (r-1)/(t-1) (|x| -> 1/2)
bad = 0
worst = 0
for r in [mp.mpf('1.1'), mp.mpf(2), mp.mpf(5), mp.mpf(30)]:
    for t in [mp.mpf('1.1'), mp.mpf(2), mp.mpf(5), mp.mpf(30)]:
        lo_p = 2 * mp.sqrt(r) * mp.log(r) / ((t + 1) * mp.log(t))
        hi_p = (r + 1) * mp.log(r) / (2 * mp.sqrt(t) * mp.log(t))
        a0 = mp.sqrt(r / t) * mp.log(r) / mp.log(t)
        a1 = (r - 1) / (t - 1)
        vals = []
        for beta in [mp.mpf(k) / 1000 for k in range(1, 1000) if k != 500]:
            v = abs(d(r, mp.mpc(beta, 50)) / d(t, mp.mpc(beta, 50)))
            vals.append((abs(beta - mp.mpf(1) / 2), v))
            if not (lo_p <= v <= hi_p):
                bad += 1
            if not (min(a0, a1) - 1e-30 <= v <= max(a0, a1) + 1e-30):
                bad += 1
        vals.sort()
        mono = all(vals[i][1] <= vals[i + 1][1] + 1e-30 for i in range(len(vals) - 1)) or all(vals[i][1] >= vals[i + 1][1] - 1e-30 for i in range(len(vals) - 1))
        if r != t and not mono:
            bad += 1
        worst = max(worst, abs(vals[0][1] - a0) / a0 if r != t else 0)
report('9  AST6.2 bounds hold; sharp range between sqrt(r/t)log r/log t and (r-1)/(t-1), monotone in |Re rho - 1/2|', bad == 0,
       'violations %d; |x|->0 limit rel err %.1e' % (bad, worst))

# 10. GMS6.3: at the first zero rho1, v(lambda) = F_+(lambda)/(lambda - (rho1+1)) has v(rho1+1) = F0'(rho1) != 0
rho1 = mp.zetazero(1)
dF0 = mp.diff(F0, rho1)
report('10 F0\'(rho1) != 0 (so [v_rho] != 0 in Q_+ and the normal row does not split)', abs(dF0) > 1e-6, '|F0\'(rho1)| = %.4e' % abs(dF0))

# 11. Gamma reflection for both parities (Prop. 24.4): Gamma((1-s)/2)Gamma((1+s)/2) = pi/cos(pi s/2),
#     Gamma(1-s/2)Gamma(1+s/2) = (pi s/2)/sin(pi s/2); both ~ e^{-pi|t|/2} times a power of |t|
e11 = 0
for s in [mp.mpc(0.3, 5), mp.mpc(-1.7, 22), mp.mpc(2.2, -9)]:
    e11 = max(e11, abs(mp.gamma((1 - s) / 2) * mp.gamma((1 + s) / 2) - mp.pi / mp.cos(mp.pi * s / 2)) / abs(mp.pi / mp.cos(mp.pi * s / 2)),
              abs(mp.gamma(1 - s / 2) * mp.gamma(1 + s / 2) - (mp.pi * s / 2) / mp.sin(mp.pi * s / 2)) / abs((mp.pi * s / 2) / mp.sin(mp.pi * s / 2)))
report('11 Gamma reflection products for even and odd characters', e11 < 1e-30, 'max rel err %.1e' % e11)

# 12. Prop. 24.4 for chi mod 5 (chi(2) = i, odd) and chi mod 8 (real, even): G_chi(it) != 0 and |G_chi| e^{pi|t|/2} polynomial on the line
def Lam(s, chi, q, a):
    s = mp.mpc(s)
    return (mp.mpf(q) / mp.pi) ** ((s + a) / 2) * mp.gamma((s + a) / 2) * mp.dirichlet(s, chi)
chi5 = [0, 1, 1j, -1j, -1]
chi8 = [0, 1, 0, -1, 0, -1, 0, 1]   # the real character mod 8 attached to Q(sqrt 2): chi(-1) = +1
lo12 = mp.inf
hi12 = 0
for (chi, q, a) in [(chi5, 5, 1), (chi8, 8, 0)]:
    for t in mp.linspace(0.5, 60, 120):
        g = Lam(mp.mpc(0, t), chi, q, a) * Lam(mp.mpc(1, t), chi, q, a)
        lo12 = min(lo12, abs(g) * mp.exp(mp.pi * t / 2))
        hi12 = max(hi12, abs(g) * mp.exp(mp.pi * t / 2) / (1 + t) ** 4)
report('12 G_chi(it) = Lam(it,chi)Lam(1+it,chi): |G_chi| e^{pi t/2} bounded below and polynomially above (chi mod 5 odd, chi mod 8 even)',
       lo12 > 1e-3 and hi12 < 1e3, 'min %.3e; max ratio %.3e' % (lo12, hi12))

# 13. The Davenport-Heilbronn function f = c L(s,chi) + cbar L(s,chibar), c = (1 - i kappa)/2, is not of the form P(s) L(s, psi)
#     (P a Dirichlet polynomial). For primes p beyond the support of P and coprime to both moduli, comparing the coefficients
#     of p and p^2 gives A_p = b(1) psi(p) and B_p = b(1) psi(p)^2 with A_p = c x + cbar xbar, B_p = c x^2 + cbar xbar^2, x = chi(p);
#     hence A_p^2 = b(1) B_p. For p = 1 mod 5 (x = 1) this forces b(1) = A^2/B = 1; for p = 2 mod 5 (x = i) it forces
#     b(1) = A^2/B = -kappa^2. (b(1) = 0 is excluded since A_p = 1 at p = 1 mod 5.) Contradiction.
kap = (mp.sqrt(10 - 2 * mp.sqrt(5)) - 2) / (mp.sqrt(5) - 1)
c = (1 - 1j * kap) / 2
AB = lambda x: ((c * x + mp.conj(c) * mp.conj(x)) ** 2, c * x ** 2 + mp.conj(c) * mp.conj(x) ** 2)
A1, B1 = AB(mp.mpc(1, 0))
A2, B2 = AB(mp.mpc(0, 1))
b1_from_1 = A1 / B1
b1_from_2 = A2 / B2
report('13 DH is not P(s)L(s,psi): b(1) = 1 from p = 1 mod 5 but b(1) = -kappa^2 from p = 2 mod 5',
       abs(b1_from_1 - 1) < 1e-30 and abs(b1_from_2 + kap ** 2) < 1e-30 and abs(b1_from_1 - b1_from_2) > 0.5,
       'b(1) = %s vs %s (kappa = %s)' % (mp.nstr(b1_from_1, 8), mp.nstr(b1_from_2, 8), mp.nstr(kap, 10)))

print('ALL PASS' if ok_all else 'SOME FAILED')
