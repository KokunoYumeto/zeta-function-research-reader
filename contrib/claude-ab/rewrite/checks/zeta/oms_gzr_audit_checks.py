# Checks for 26_ (audit of OMS and GZR; CGS and DCP read in part; commit 064f33b).
# claude-ab (Opus 5.5, max effort), 25 September 2026.
import random
import mpmath as mp

mp.mp.dps = 40
ok_all = True


def report(name, ok, detail=''):
    global ok_all
    ok_all &= bool(ok)
    print(('PASS ' if ok else 'FAIL ') + name + ('  ' + detail if detail else ''))


# 1. GZR1.7: zeta'(-2r) = (-1)^r 2^{-2r-1} pi^{-2r} (2r)! zeta(1+2r)
e1 = max(abs(mp.zeta(-2 * r, derivative=1) - (-1) ** r * mp.mpf(2) ** (-2 * r - 1) * mp.pi ** (-2 * r) * mp.factorial(2 * r) * mp.zeta(1 + 2 * r))
         / abs(mp.zeta(-2 * r, derivative=1)) for r in range(1, 6))
report('1  GZR1.7: zeta\'(-2r) in closed form, r = 1..5', e1 < 1e-35, 'max rel err %.1e' % e1)

# 2. GZR2.3-2.4: |chi(-1+it)|^2 = pi^-3 y coth(pi y)(y^2 + 1/4), y = t/2, and |1/zeta(-1+it)| <= 4 pi^2 zeta(2) (1+|t|)^{-3/2}
chi = lambda s: mp.pi ** (s - mp.mpf(1) / 2) * mp.gamma((1 - s) / 2) / mp.gamma(s / 2)
e2 = 0
worst = 0
for t in list(mp.linspace(0.05, 5, 30)) + list(mp.linspace(5, 400, 80)):
    y = t / 2
    e2 = max(e2, abs(abs(chi(mp.mpc(-1, t))) ** 2 - mp.pi ** -3 * y * mp.coth(mp.pi * y) * (y ** 2 + mp.mpf(1) / 4)) / abs(chi(mp.mpc(-1, t))) ** 2)
    worst = max(worst, abs(1 / mp.zeta(mp.mpc(-1, t))) / (4 * mp.pi ** 2 * mp.zeta(2) * (1 + t) ** (-mp.mpf(3) / 2)))
report('2  GZR2.3 closed form; GZR2.4 bound |1/zeta(-1+it)| <= 4 pi^2 zeta(2)(1+|t|)^{-3/2} on 110 points in (0, 400]', e2 < 1e-30 and worst <= 1,
       'rel err %.1e; max ratio to the bound %.4f' % (e2, worst))

# 3. GZR4.2 and GZR4.7: the reciprocal recursion gives the Taylor coefficients of 1/u, and det M = c_0^m (random data, m = 1..6)
random.seed(7)
e3 = 0
for m in range(1, 7):
    u = [mp.mpc(random.uniform(0.5, 2), random.uniform(-1, 1))] + [mp.mpc(random.uniform(-1, 1), random.uniform(-1, 1)) for _ in range(m + 3)]
    c = [1 / u[0]]
    for n in range(1, m + 3):
        c.append(-sum(u[r] * c[n - r] for r in range(1, n + 1)) / u[0])
    # c are the Taylor coefficients of 1/u: check u * c = 1 to order m+2
    for n in range(0, m + 3):
        conv = sum(u[r] * c[n - r] for r in range(0, n + 1))
        e3 = max(e3, abs(conv - (1 if n == 0 else 0)))
    M = mp.matrix(m, m)
    for i in range(m):
        for j in range(m):
            M[i, j] = (-1) ** j * c[m - 1 - i - j] if i + j <= m - 1 else 0
    e3 = max(e3, abs(mp.det(M) - c[0] ** m) / abs(c[0] ** m))
report('3  GZR4.2 reciprocal recursion; GZR4.7 det M_rho = c_0^m for m = 1..6', e3 < 1e-30, 'max err %.1e' % e3)

# 4. GZR4.3 against a contour integral: for Z(s) = (s - rho)^m u(s) with u = e^s + 2, the residue at rho of F(s)G(1-s)/Z(s)
#    equals sum_{i+j+k=m-1} F^(i)(rho)/i! G^(j)(1-rho)/j! (-1)^j c_k
rho = mp.mpc(0.37, 1.9)
F = lambda s: mp.exp(s / 3) * (s + 1)
G = lambda s: mp.cos(s) + s ** 2
e4 = 0
for m in [1, 2, 3]:
    u = lambda s: mp.exp(s) + 2
    Z = lambda s: (s - rho) ** m * u(s)
    circ = mp.quad(lambda th: F(rho + mp.mpf('0.05') * mp.exp(1j * th)) * G(1 - rho - mp.mpf('0.05') * mp.exp(1j * th))
                   / Z(rho + mp.mpf('0.05') * mp.exp(1j * th)) * 1j * mp.mpf('0.05') * mp.exp(1j * th), [0, 2 * mp.pi]) / (2j * mp.pi)
    ut = mp.taylor(u, rho, m)
    cc = [1 / ut[0]]
    for n in range(1, m):
        cc.append(-sum(ut[r] * cc[n - r] for r in range(1, n + 1)) / ut[0])
    Ft = mp.taylor(F, rho, m)
    Gt = mp.taylor(G, 1 - rho, m)
    formula = sum(Ft[i] * Gt[j] * (-1) ** j * cc[m - 1 - i - j] for i in range(m) for j in range(m) if i + j <= m - 1)
    e4 = max(e4, abs(circ - formula) / abs(formula))
report('4  GZR4.3 residue formula against a numerical contour integral (m = 1, 2, 3)', e4 < 1e-25, 'max rel err %.1e' % e4)

# 5. OMS2.7: b = F_*'(0)/F_*(0) = (1/2) log(4 pi) - 1 - gamma/2
# F_*(s) = F_*(1-s), so F_*'(0) = -F_*'(1); a central difference at 1 avoids the removable point itself.
gF = lambda s: s * (s - 1) / 8 * mp.pi ** (-s / 2) * mp.gamma(s / 2) * mp.zeta(s)
hh = mp.mpf('1e-12')
b_num = -((gF(1 + hh) - gF(1 - hh)) / (2 * hh)) / (mp.mpf(1) / 8)
b_formula = mp.log(4 * mp.pi) / 2 - 1 - mp.euler / 2
report('5  OMS2.7: F_*\'(0)/F_*(0) = (1/2)log(4 pi) - 1 - gamma/2', abs(b_num - b_formula) < 1e-20, 'b = %s; difference-quotient error %.1e' % (mp.nstr(b_formula, 15), abs(b_num - b_formula)))

# 6. OMS2.3: f_* is Fourier self-dual, and k_* = E f_* satisfies k_*(u) = k_*(1/u)
fs = lambda v: mp.pi / 2 * v ** 2 * (2 * mp.pi * v ** 2 - 3) * mp.exp(-mp.pi * v ** 2)
ft = lambda x: mp.quad(lambda v: fs(v) * mp.cos(2 * mp.pi * v * x), [-mp.inf, 0, mp.inf])
e6 = max(abs(ft(x) - fs(x)) for x in [mp.mpf('0.3'), mp.mpf('1.1'), mp.mpf('2.0')])
Ek = lambda u: mp.sqrt(u) * mp.nsum(lambda n: fs(n * u), [1, mp.inf])
e6b = max(abs(Ek(u) - Ek(1 / u)) for u in [mp.mpf('0.4'), mp.mpf('0.8'), mp.mpf('1.7')])
report('6  OMS2.3: f_* = Fourier(f_*); k_*(u) = k_*(1/u)', e6 < 1e-30 and e6b < 1e-30, 'errs %.1e, %.1e' % (e6, e6b))

# 7. OMS4.3: f(0)/2 + Zf(u) = u^-1 Z fhat(1/u) + fhat(0)/(2u), Zf(u) = sum_{n>=1} f(nu), for f(v) = e^{-2 pi v^2}
f = lambda v: mp.exp(-2 * mp.pi * v ** 2)
fh = lambda x: mp.exp(-mp.pi * x ** 2 / 2) / mp.sqrt(2)
Zs = lambda g, u: mp.nsum(lambda n: g(n * u), [1, mp.inf])
e7 = max(abs(f(0) / 2 + Zs(f, u) - (Zs(fh, 1 / u) / u + fh(0) / (2 * u))) for u in [mp.mpf('0.6'), mp.mpf('1.4')])
report('7  OMS4.3: Poisson with both endpoint terms', e7 < 1e-30, 'max err %.1e' % e7)

# 8. GZR7.3 and GZR7.2 on the integrand: s F(s) G(1-s) = F(s) [(1 - (1-s)) G(1-s)]; a^s a^{1-s} = a
s0 = mp.mpc(0.3, 4.4)
e8 = abs(s0 * F(s0) * G(1 - s0) - F(s0) * ((1 - (1 - s0)) * G(1 - s0))) + abs(mp.mpf(3) ** s0 * mp.mpf(3) ** (1 - s0) - 3)
report('8  GZR7.2-7.3 integrand identities', e8 < 1e-35, 'err %.1e' % e8)

print('ALL PASS' if ok_all else 'SOME FAILED')
