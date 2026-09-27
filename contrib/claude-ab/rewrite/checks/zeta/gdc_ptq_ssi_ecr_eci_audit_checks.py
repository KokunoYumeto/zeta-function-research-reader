# Checks for 25_ (audit of GDC, PTQ, SSI, ECR and ECI; commit 064f33b).
# claude-ab (Opus 5.5, max effort), 25 September 2026.
import mpmath as mp

mp.mp.dps = 40
ok_all = True


def report(name, ok, detail=''):
    global ok_all
    ok_all &= bool(ok)
    print(('PASS ' if ok else 'FAIL ') + name + ('  ' + detail if detail else ''))


f0 = lambda v: mp.pi / 2 * v ** 2 * (2 * mp.pi * v ** 2 - 3) * mp.exp(-mp.pi * v ** 2)
Sig = lambda f, u: 2 * mp.nsum(lambda n: f(n * u), [1, mp.inf])


def F0(s):
    s = mp.mpc(s)
    if abs(s) < mp.mpf(10) ** -30 or abs(s - 1) < mp.mpf(10) ** -30:
        return mp.mpf(1) / 8
    if mp.re(s) < 0.5:
        s = 1 - s
        if abs(s - 1) < mp.mpf(10) ** -30:
            return mp.mpf(1) / 8
    return s * (s - 1) / 8 * mp.pi ** (-s / 2) * mp.gamma(s / 2) * mp.zeta(s)


# 1. SSI3.7: |chi(-2N-1+it)|^2 = pi^{-4N-3} y coth(pi y) prod_{k=1}^N (k^2+y^2) prod_{j=0}^N ((j+1/2)^2+y^2), y = t/2,
#    with chi(s) = pi^{s-1/2} Gamma((1-s)/2)/Gamma(s/2)
chi = lambda s: mp.pi ** (s - mp.mpf(1) / 2) * mp.gamma((1 - s) / 2) / mp.gamma(s / 2)
e1 = 0
for N in range(0, 4):
    for t in [mp.mpf('0.3'), mp.mpf(3), mp.mpf(17), mp.mpf(60)]:
        y = t / 2
        rhs = mp.pi ** (-4 * N - 3) * y * mp.coth(mp.pi * y)
        for k in range(1, N + 1):
            rhs *= k ** 2 + y ** 2
        for j in range(0, N + 1):
            rhs *= (j + mp.mpf(1) / 2) ** 2 + y ** 2
        lhs = abs(chi(mp.mpc(-2 * N - 1, t))) ** 2
        e1 = max(e1, abs(lhs - rhs) / rhs)
report('1  SSI3.7: exact modulus of chi on Re s = -2N-1 (N = 0..3)', e1 < 1e-30, 'max rel err %.1e' % e1)

# 2. SSI7.1: Moebius inverse (1/2) sum mu(n) b(nx) = f(x) for b = Sigma f0
e2 = 0
for x in [mp.mpf('0.5'), mp.mpf('0.9'), mp.mpf('1.7')]:
    acc = 0
    for n in range(1, 60):
        mu = mp.mpf(int(__import__('sympy').mobius(n)))
        if mu != 0:
            acc += mu * Sig(f0, n * x)
    e2 = max(e2, abs(acc / 2 - f0(x)))
report('2  SSI7.1: (1/2) sum_n mu(n) (Sigma f0)(n x) = f0(x) at x = 0.5, 0.9, 1.7', e2 < 1e-25, 'max err %.1e' % e2)

# 3. SSI5.6: f_F^{(2r)}(0)/(2r)! = F(-2r)/(2 zeta'(-2r)) with F = M_0 Sigma f0 = 2 F0; compare with the Taylor series of f0
tay = mp.taylor(f0, 0, 9)
e3 = 0
for r in range(1, 5):
    rhs = 2 * F0(-2 * r) / (2 * mp.zeta(-2 * r, derivative=1))
    closed = r * (2 * r + 1) * (-1) ** r * mp.pi ** r / (2 * mp.factorial(r))
    e3 = max(e3, abs(tay[2 * r] - rhs), abs(tay[2 * r] - closed))
e3 = max(e3, abs(tay[0]), abs(tay[1]), abs(tay[3]))
report('3  SSI5.6: Taylor coefficients of f0 at 0 are F(-2r)/(2 zeta\'(-2r)) = r(2r+1)(-1)^r pi^r/(2 r!)', e3 < 1e-25, 'max err %.1e' % e3)

# 4. SSI6.3 for F = 2 F0: int_0^oo f0(x) dx/x = -F(0) = -1/4 and int_0^oo f0(x) log x dx = F(1)/2 = 1/8
i1 = mp.quad(lambda x: f0(x) / x, [0, 1, mp.inf])
i2 = mp.quad(lambda x: f0(x) * mp.log(x), [0, 1, mp.inf])
report('4  SSI6.3: int f0 dx/x = -1/4, int f0 log x dx = 1/8', abs(i1 + mp.mpf(1) / 4) < 1e-30 and abs(i2 - mp.mpf(1) / 8) < 1e-30,
       'errs %.1e, %.1e' % (abs(i1 + 0.25), abs(i2 - 0.125)))

# 5. ECR3.3: (u^{-1/2}/pi) int e^{t(1/2+iy)^2} u^{-iy} dy = e^{t/4} (pi t)^{-1/2} u^{-1/2} exp(-(log u - t)^2/(4t))
e5 = 0
for t in [mp.mpf('0.5'), mp.mpf(2)]:
    for u in [mp.mpf('0.7'), mp.mpf('2.3')]:
        lhs = u ** (-mp.mpf(1) / 2) / mp.pi * mp.quad(lambda y: mp.exp(t * (mp.mpf(1) / 2 + 1j * y) ** 2) * u ** (-1j * y), [-mp.inf, 0, mp.inf])
        rhs = mp.exp(t / 4) / mp.sqrt(mp.pi * t) * u ** (-mp.mpf(1) / 2) * mp.exp(-(mp.log(u) - t) ** 2 / (4 * t))
        e5 = max(e5, abs(lhs - rhs) / abs(rhs))
report('5  ECR3.3: the Gaussian source of the extension generator', e5 < 1e-25, 'max rel err %.1e' % e5)

# 6. ECI2.5: K1 D_a = a D_{1/a} K1 and K3 D_a^+ = a^3 D_{1/a}^+ K3 on a test function (K1 h(s) = conj h(1 - conj s))
h = lambda s: mp.exp(s ** 2 / 3) * (s + 2) + mp.sin(s)
K1 = lambda g: (lambda s: mp.conj(g(1 - mp.conj(s))))
K3 = lambda g: (lambda s: mp.conj(g(3 - mp.conj(s))))
Da = lambda a, g: (lambda s: a ** s * g(s))
e6 = 0
for a in [mp.mpf('1.7'), mp.mpf(5)]:
    for s in [mp.mpc(0.3, 2), mp.mpc(-1.1, 0.4)]:
        e6 = max(e6, abs(K1(Da(a, h))(s) - a * Da(1 / a, K1(h))(s)), abs(K3(Da(a, h))(s) - a ** 3 * Da(1 / a, K3(h))(s)))
report('6  ECI2.5: K1 D_a = a D_{1/a} K1 and K3 D_a^+ = a^3 D_{1/a}^+ K3', e6 < 1e-30, 'max err %.1e' % e6)

# 7. ECI3.4: A_c^2 F = [c c^#1 + (1-c)(1-c)^#3] F + c (1-c)^#1 F(s+2) + (1-c) c^#3 F(s-2), for arbitrary entire c, F
c = lambda s: mp.exp(-s ** 2) * mp.cos(s) + s / 7
F = lambda s: mp.exp(s ** 2 / 5) / (s + 9)
Ac = lambda g: (lambda s: c(s) * K1(g)(s) + (1 - c(s)) * K3(g)(s))
e7 = 0
for s in [mp.mpc(0.2, 1.3), mp.mpc(-0.6, -2.2)]:
    lhs = Ac(Ac(F))(s)
    one_minus_c = lambda z: 1 - c(z)
    rhs = (c(s) * K1(c)(s) + (1 - c(s)) * K3(one_minus_c)(s)) * F(s) + c(s) * K1(one_minus_c)(s) * F(s + 2) + (1 - c(s)) * K3(c)(s) * F(s - 2)
    e7 = max(e7, abs(lhs - rhs))
report('7  ECI3.4: the square of the componentwise involution, before the quotient', e7 < 1e-30, 'max err %.1e' % e7)

# 8. ECI6.6: zeta'(1-s) = chi'(s) zeta(s)/chi(s)^2 - zeta'(s)/chi(s)
e8 = 0
for s in [mp.mpc(0.3, 7), mp.mpc(-1.4, 2.5), mp.mpc(2.2, -4)]:
    lhs = mp.zeta(1 - s, derivative=1)
    rhs = mp.diff(chi, s) * mp.zeta(s) / chi(s) ** 2 - mp.zeta(s, derivative=1) / chi(s)
    e8 = max(e8, abs(lhs - rhs) / abs(lhs))
report('8  ECI6.6: differentiated functional equation', e8 < 1e-25, 'max rel err %.1e' % e8)

# 9. ECI12.3: g_t^{#1}(s) = e^{t(1-s)^2} = e^{t(1-2s)} g_t(s), and d_t^{#1} = d_t^{-1}
e9 = 0
for t in [mp.mpf('0.4'), mp.mpf(3)]:
    g = lambda s: mp.exp(t * s ** 2)
    d = lambda s: mp.exp(t * (1 - 2 * s))
    for s in [mp.mpc(0.3, 2), mp.mpc(-0.8, -1.1)]:
        e9 = max(e9, abs(K1(g)(s) - d(s) * g(s)) / abs(g(s) * d(s)), abs(K1(d)(s) * d(s) - 1))
report('9  ECI12.3: the Gaussian source multiplier under the involution', e9 < 1e-30, 'max err %.1e' % e9)

# 10. PTQ5.4 / GDC9.2: on an off-line reflected pair the Weil block [[0,m],[m,0]] has W(e1+e2) = 2m, W(e1-e2) = -2m, signature (1,1);
#     on H_line the transfer-adjoint relation |n^rho|^2 = n holds exactly when Re rho = 1/2 (PTQ3.3)
m = 3
Wb = mp.matrix([[0, m], [m, 0]])
v1 = mp.matrix([1, 1]); v2 = mp.matrix([1, -1])
q = lambda v: (v.T * Wb * v)[0]
ev = mp.eig(Wb)[0]
ok10 = abs(q(v1) - 2 * m) < 1e-30 and abs(q(v2) + 2 * m) < 1e-30 and sorted([mp.re(e) for e in ev]) == [-m, m]
e10 = max(abs(abs(mp.mpf(n) ** mp.mpc(0.5, 21.02)) ** 2 - n) for n in [2, 3, 7])
d10 = min(abs(abs(mp.mpf(n) ** mp.mpc(0.7, 21.02)) ** 2 - n) for n in [2, 3, 7])
report('10 PTQ5.4 signature of an off-line pair; |n^rho|^2 = n on the line and not off it (PTQ3.3)', ok10 and e10 < 1e-30 and d10 > 0.1,
       'line err %.1e; off-line min gap %.3f' % (e10, d10))

print('ALL PASS' if ok_all else 'SOME FAILED')
