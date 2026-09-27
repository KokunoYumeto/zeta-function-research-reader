#!/usr/bin/env python3
"""Audit 46: independent checks for YM-05, YM-02, YM-07 §27, NS-04 (a),(b), S6-5 (and an S6-1
dimension count), and the YM<->zeta / YM<->Collatz overlap identities.
No workbench code is imported; all inputs are typed in from the cited source lines.
"""
from fractions import Fraction as F
import itertools, math, random
import sympy as sp
import mpmath as mp
mp.mp.dps = 50
ok_all = True
def rep(name, ok, val=None):
    global ok_all
    ok_all &= bool(ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + ("" if val is None else f": {val}"))

m = {1: F(64, 3), 2: F(5834, 39), 3: F(336572872, 208845),
     4: F(17270702970768271, 341697152160), 5: F(1638684)}
t = {1: F(16, 3), 2: F(137, 6), 3: F(225985217, 1253070),
     4: F(110695177857394584026401, 18025447358750832000), 5: F(190128)}
def mpf(q): return mp.mpf(q.numerator) / q.denominator
def make(N):
    b = {(i, j): 3 * (m[i] * t[j] + m[j] * t[i]) for i in range(1, N + 1) for j in range(1, N + 1)}
    ell = lambda x: sum((m[i] + 4 * t[i]) * x**i for i in range(1, N + 1))
    dl = lambda x: sum(b[i, j] * x**(i + j) for i in range(1, N + 1) for j in range(1, N + 1) if i + j >= N + 1)
    D = lambda x: (1 - ell(x))**2 - F(8, 3) * dl(x)
    d = lambda x: mp.mpf(3) / 2 * (1 + mp.sqrt(mpf(D(x)))) + sum(mpf(F(3, 2) * m[i] - 6 * t[i]) * mpf(x)**i for i in range(1, N + 1))
    return ell, dl, D, d
def root(D, lo, hi, n=90):
    for _ in range(n):
        mid = (lo + hi) / 2
        if D(mid) > 0: lo = mid
        else: hi = mid
    return lo, hi

print("== YM-05 (17 Sep, fourth reference q4; reader R24-R31) from the same m_i,t_i, i<=4")
ell4, dl4, D4, d4 = make(4)
lo, hi = root(D4, F(181, 10000), F(182, 10000))
rep("R26 alpha_[4] in (0.018104972231644127075, ...076)", F('0.018104972231644127075') < lo and hi < F('0.018104972231644127076'), mp.nstr(mpf(lo), 22))
rep("R26 1/(2 sqrt alpha_[4]) < 3.715960362535435237", 1 / (2 * mp.sqrt(mpf(lo))) < mp.mpf('3.715960362535435237'), mp.nstr(1 / (2 * mp.sqrt(mpf(lo))), 20))
rep("R29 p4 = (3/2)m4 - 6t4 = 32092619324045301088/823531037954625", F(3, 2) * m[4] - 6 * t[4] == F(32092619324045301088, 823531037954625))
rep("R31 d_[4](4/225) > 1.6584 (g^2 = 15/4)", d4(F(4, 225)) > mp.mpf('1.6584'), mp.nstr(d4(F(4, 225)), 10))
rep("R31 d_[4](1/64) > 1.89811 (g^2 = 4)", d4(F(1, 64)) > mp.mpf('1.89811'), mp.nstr(d4(F(1, 64)), 10))
ell5, dl5, D5, d5 = make(5)
a5lo, _ = root(D5, F(18, 1000), F(19, 1000))
rep("YM-01 domain contains YM-05 domain: alpha_5 > alpha_[4]", a5lo > hi)
rep("YM-01 bound at g^2 >= 15/4 (1.6993) exceeds YM-05's 1.6584", d5(F(4, 225)) > mp.mpf('1.6993') > mp.mpf('1.6584'), mp.nstr(d5(F(4, 225)), 10))

print("== YM-02 (HEAT_AND_COMPLEMENT H12, H30) constants")
R = F(1, 55)
rep("H12 1/55 < alpha_5", R < a5lo)
rep("H12 d5(1/55) > 13/8 (equivalently chi(1/55) < 11/24)", d5(R) > mp.mpf(13) / 8, mp.nstr(d5(R), 12))
rep("H12 C = (1+255*11/24)/(1-11/24)^2 = 67896/169", (1 + 255 * F(11, 24)) / (1 - F(11, 24))**2 == F(67896, 169))
rep("H30 d5 at g^2 = 13 exceeds d_ph = 29047/10000", d5(F(1, 4 * 169)) > mp.mpf('2.9047'), mp.nstr(d5(F(1, 4 * 169)), 10))
def J_int(d):  # 1 + int_0^inf |9 tau - 6| e^{-d tau} d tau, split at 2/3
    tau = sp.symbols('tau', positive=True)
    return 1 + sp.integrate((6 - 9 * tau) * sp.exp(-d * tau), (tau, 0, sp.Rational(2, 3))) + sp.integrate((9 * tau - 6) * sp.exp(-d * tau), (tau, sp.Rational(2, 3), sp.oo))
dd = sp.Rational(13, 8)
closed = 1 + 6 / dd - 9 / dd**2 + 18 / dd**2 * sp.exp(-2 * dd / 3)
rep("H17 signed time integral closed form", sp.simplify(J_int(dd) - closed) == 0)
rep("H17 exp(-13/12) < 339/1000", sp.exp(-sp.Rational(13, 12)) < sp.Rational(339, 1000), float(sp.exp(-sp.Rational(13, 12))))
CJ = F(67896, 169) * (1 + 6 / F(13, 8) - 9 / F(13, 8)**2 + 18 * F(339, 1000) / F(13, 8)**2)
rep("H18 C_J = 5156090136/3570125", CJ == F(5156090136, 3570125), CJ)
rep("H7 path: xi_n = c_n^2/4, so c_n <= 2 sqrt(alpha5) <=> xi_n <= alpha5; c_n < 2/sqrt(55) <=> xi_n < 1/55",
    abs((mp.mpf(2) * mp.sqrt(mpf(a5lo))) ** 2 / 4 - mpf(a5lo)) < mp.mpf('1e-40') and abs((2 / mp.sqrt(55))**2 / 4 - mp.mpf(1) / 55) < mp.mpf('1e-40'))

print("== YM-07 §27 (spatial_continuum.md FC1-FC9): brute-force face count, Neumann radius")
for L in range(2, 7):
    V = range(-L, L + 1)
    faces = sum(1 for n in itertools.product(V, repeat=3) for i in range(3) for j in range(i + 1, 3)
                if n[i] + 1 <= L and n[j] + 1 <= L)
    rep(f"FC1 L={L}: enumerated faces = 12L^2(2L+1)", faces == 12 * L * L * (2 * L + 1), faces)
    rep(f"FC8 L={L}: 3/(16 M_L) = 1/(64 L^2 (2L+1))", F(3, 16 * faces) == F(1, 64 * L * L * (2 * L + 1)))
rep("FC5 smallest nonzero one-link Casimir j(j+1) = 3/4 at j=1/2; physical (gauge-invariant) minimum c_j = 3",
    min(F(k, 2) * (F(k, 2) + 1) for k in range(1, 6)) == F(3, 4))
rep("§27 disk at L=2 is 1/1280, far below alpha_5 ~ 0.0184: global Neumann route certifies nothing where YM-01 applies",
    F(1, 1280) < F(1, 64) < a5lo)
print("INFO §27 FC9: along L=j^2 the disk radius ~ 1/(128 j^6); e.g. j=2 ->", float(F(1, 64 * 16 * (2 * 16 + 1))))

print("== NS-04 (a): TT lift, Lichnerowicz coefficient, decoder (vacuum-hydrodynamics README L23-84)")
x1, x2, x3, w = sp.symbols('x1 x2 x3 w', real=True)
X = (x1, x2, x3)
g = sp.exp(-(x1**2 + x2**2 + x3**2))
Apot = (x2 * g, x3**2 * g, (x1 + x1 * x2) * g)   # arbitrary vector potential; V = curl A is divergence free
Vf = [sp.diff(Apot[2], x2) - sp.diff(Apot[1], x3), sp.diff(Apot[0], x3) - sp.diff(Apot[2], x1), sp.diff(Apot[1], x1) - sp.diff(Apot[0], x2)]
rep("V = curl A is divergence free", sp.simplify(sum(sp.diff(Vf[i], X[i]) for i in range(3))) == 0)
b = sp.Function('b')
S = [[(sp.diff(Vf[i], X[j]) + sp.diff(Vf[j], X[i])) / 2 for j in range(3)] for i in range(3)]
lap = lambda f: sum(sp.diff(f, xi, 2) for xi in X)
# 4x4 tensor in coordinates (w, x1, x2, x3)
Lt = sp.zeros(4, 4)
for i in range(3):
    for j in range(3): Lt[i + 1, j + 1] = sp.diff(b(w), w) * S[i][j]
    Lt[0, i + 1] = Lt[i + 1, 0] = -b(w) / 2 * lap(Vf[i])
coords = (w,) + X
rep("L_bV tracefree", sp.simplify(Lt.trace()) == 0)
div = [sp.simplify(sum(sp.diff(Lt[a, c], coords[c]) for c in range(4))) for a in range(4)]
rep("L_bV divergence free (all four components)", all(dv == 0 for dv in div))
norm2 = sum(Lt[a, c]**2 for a in range(4) for c in range(4))
rep("|L_bV|^2 = b'^2|S|^2 + b^2|Delta V|^2/2", sp.simplify(norm2 - (sp.diff(b(w), w)**2 * sum(S[i][j]**2 for i in range(3) for j in range(3)) + b(w)**2 * sum(lap(v)**2 for v in Vf) / 2)) == 0)
Lc, th = sp.symbols('L theta', positive=True)
a_s = 1 / (Lc * sp.sin(th)); tau_s = -4 / Lc * sp.cot(th); Lam = -6 / Lc**2
rep("Lichnerowicz (n=4): (3/4)tau*^2 - 2 Lambda = 12 a*^2 = kappa*", sp.simplify(sp.Rational(3, 4) * tau_s**2 - 2 * Lam - 12 * a_s**2) == 0)
rep("cross term <diag(-3,1,1,1), L_bV> = 0 so q = kappa* + beta*^2 |L_bV|^2 >= kappa*",
    sp.simplify(-3 * Lt[0, 0] + Lt[1, 1] + Lt[2, 2] + Lt[3, 3]) == 0)
rep("Newton decoder: Delta V_i = 2 d_j S_ij (so N(S) = 2 Delta^{-1} d_j S_ij = V for decaying V)",
    all(sp.simplify(lap(Vf[i]) - 2 * sum(sp.diff(S[i][j], X[j]) for j in range(3))) == 0 for i in range(3)))
phi, beta, tau = sp.symbols('phi beta tau', positive=True)
Ssym = sp.Matrix(3, 3, lambda i, j: sp.Symbol(f's{min(i,j)}{max(i,j)}'))
Ssym[2, 2] = -Ssym[0, 0] - Ssym[1, 1]
Abar_E = -a_s * sp.eye(3) + beta * Ssym          # x-block of Abar at w=0 (b(0)=0, b'(0)=1)
Kmixed_E = phi**-4 * Abar_E + tau / 4 * sp.eye(3)  # (h^-1 K) on the E block, h = phi^2 delta
TF = lambda M3: M3 - M3.trace() / 3 * sp.eye(3)
rep("decoder: phi^4 TF_E(K^sharp) = beta S at w = 0", sp.simplify(phi**4 * TF(Kmixed_E) - beta * Ssym) == sp.zeros(3, 3))

print("== NS-04 (b): homogeneous Kasner map (README L86-104)")
nu, c = sp.symbols('nu c', positive=True)
Bm = -2 * nu * Ssym / c**2
chi = sp.sqrt(1 + sp.Rational(4, 3) * (Bm * Bm).trace())
Pw = sp.Rational(1, 4) - 3 / (4 * chi)
Pp = sp.eye(3) / 4 + (sp.eye(3) / 4 + Bm) / chi
rep("tr P = 1", sp.simplify(Pw + Pp.trace() - 1) == 0)
rep("tr P^2 = 1", sp.simplify(Pw**2 + (Pp * Pp).trace() - 1) == 0)
rep("inverse formula returns S", sp.simplify(-c**2 / (2 * nu) * (3 * Pp + (Pw - 1) * sp.eye(3)) / (1 - 4 * Pw) - Ssym) == sp.zeros(3, 3))
eps = sp.Symbol('eps')
Pp_eps = Pp.subs({s: eps * s for s in Ssym.free_symbols}, simultaneous=True)
rep("derivative of P_perp at S=0 is -2 nu S / c^2 (first-order radial response)",
    sp.simplify(sp.diff(Pp_eps, eps).subs(eps, 0) - Bm) == sp.zeros(3, 3))
# surjectivity onto P_w < 1/4: random Kasner data -> inverse -> forward
random.seed(46); worst = 0
for _ in range(200):
    pw = random.uniform(-0.5, 0.2499)
    # eigenvalues p1,p2,p3: sum = 1-pw, sum of squares = 1-pw^2 (circle in the plane); pick an angle
    s1, s2 = 1 - pw, 1 - pw**2
    r2 = s2 - s1**2 / 3
    if r2 < 0: continue
    ang = random.uniform(0, 2 * math.pi); r = math.sqrt(r2)
    e1 = [1 / math.sqrt(2), -1 / math.sqrt(2), 0]; e2 = [1 / math.sqrt(6), 1 / math.sqrt(6), -2 / math.sqrt(6)]
    ev = [s1 / 3 + r * (math.cos(ang) * e1[k] + math.sin(ang) * e2[k]) for k in range(3)]
    Pnum = sp.diag(*ev)
    Bnum = (3 * Pnum + (pw - 1) * sp.eye(3)) / (1 - 4 * pw)
    chin = math.sqrt(1 + 4 / 3 * float((Bnum * Bnum).trace()))
    Pw_back = 0.25 - 3 / (4 * chin); Pp_back = sp.eye(3) / 4 + (sp.eye(3) / 4 + Bnum) / chin
    worst = max(worst, abs(Pw_back - pw), max(abs(float(v)) for v in (Pp_back - Pnum)))
rep("forward(inverse(P)) = P on 200 random block-Kasner data with P_w in [-1/2, 1/4)", worst < 1e-12, worst)

print("== S6-5 (27_...tex L265-300) and an S6-1 dimension count")
def qmul(p, q):
    a0, a1, a2, a3 = p; b0, b1, b2, b3 = q
    return (a0*b0 - a1*b1 - a2*b2 - a3*b3, a0*b1 + a1*b0 + a2*b3 - a3*b2,
            a0*b2 - a1*b3 + a2*b0 + a3*b1, a0*b3 + a1*b2 - a2*b1 + a3*b0)
Pa = lambda a: a[0] * (a[0]**2 - 3 * (a[1]**2 + a[2]**2 + a[3]**2))
box = [a for a in itertools.product(range(-6, 7), repeat=4) if sum(a) % 2 == 0]
rep("Re(a^3) = P(a) for quaternions a (so tau(sqrt2(a,a,a)) = 2 sqrt2 Re(a^3) = 2 sqrt2 P(a))",
    all(qmul(qmul(a, a), a)[0] == Pa(a) for a in box[:4000]))
vals = {Pa(a) for a in box}
rep("gcd of P over D4 (box |a_i|<=6) is 2, so the generated group is 2 sqrt2 * 2Z = 4 sqrt2 Z", math.gcd(*[v for v in vals if v]) == 2 and -2 in vals)
rep("P(a) = 6 never attained (tau = 12 sqrt2 not a value); proof: 3|P => 3|a0 => 9|P",
    6 not in vals and all(v % 9 == 0 for v in vals if v % 3 == 0))
rep("P(a) = 6 has no integer solution at all in |a_i| <= 8 (argument does not use D4)",
    all(Pa(a) != 6 for a in itertools.product(range(-8, 9), repeat=4)))
D4basis = sp.Matrix([[1, -1, 0, 0], [0, 1, -1, 0], [0, 0, 1, -1], [0, 0, 1, 1]])
G = 6 * D4basis * D4basis.T
rep("Gram of I = 6 G_D4 has det 5184 = 6^4 * 4", G.det() == 5184)
rep("min squared norm of I = 6 * 2 = 12", min(6 * sum(x * x for x in a) for a in box if any(a)) == 12)
rep("[N:R] = sqrt(|disc(A5^4 D4)|) = sqrt(6^4*4) = 72 (N unimodular)", math.isqrt(6**4 * 4) ** 2 == 6**4 * 4 and math.isqrt(6**4 * 4) == 72)
rep("S6-4 value-group quotient Z/4 x Z/3 = Z/12 (orders 4*3, coprime)", math.gcd(4, 3) == 1)
rep("S6-1: h^0(omega^-m) = floor(m/2)+1 (from f_*O(kS2) = O(floor(k/4)p2), k=2m) equals dim C[U,V]_m, degU=1, degV=2, m<=60",
    all((2 * mm) // 4 + 1 == sum(1 for j in range(mm // 2 + 1)) for mm in range(61)))

print("== Overlaps: AMT7-9 composed minimum lift; OK1-2 (L22); T7 constants; Collatz fixture")
random.seed(7)
def rmat(r, cc): return sp.Matrix(r, cc, lambda i, j: sp.Rational(random.randint(-5, 5), random.randint(1, 4)))
Mq = rmat(6, 6); Q = Mq * Mq.T + sp.eye(6)
L1 = rmat(4, 6); L2 = rmat(2, 4)
Sec = lambda Lam, Qm: Qm.inv() * Lam.T * (Lam * Qm.inv() * Lam.T).inv()
Q1 = (L1 * Q.inv() * L1.T).inv()
rep("AMT7-9: S_{L2 L1, Q} = S_{L1, Q} S_{L2, Q1} (exact rationals)", sp.simplify(Sec(L2 * L1, Q) - Sec(L1, Q) * Sec(L2, Q1)) == sp.zeros(6, 2))
Xm = rmat(6, 3); W = (L1 * Q.inv() * L1.T).inv(); Ss = Q.inv() * L1.T * W
lhs = (Xm - Ss * L1 * Xm).T * Q * (Xm - Ss * L1 * Xm); rhs = Xm.T * Q * Xm - (L1 * Xm).T * W * (L1 * Xm)
rep("OK1-2 / L22 Pythagorean identity for the minimum section", sp.simplify(lhs - rhs) == sp.zeros(3, 3))
rep("T7: (3/10)^2/(51/50) = 3/34 and (3/34)/(13/100) = 150/221", F(3, 10)**2 / F(51, 50) == F(3, 34) and F(3, 34) / F(13, 100) == F(150, 221))
q = sp.symbols('q')
Xu = sp.Rational(1, 2) + q / 32; Xv = sp.Rational(1, 8) + q / 16 + q**2 / 32
rep("Collatz fixture: X_v - X_u = (q-3)(q+4)/32 identically; X_u(3) = X_v(3) = 19/32",
    sp.expand(Xv - Xu - (q - 3) * (q + 4) / 32) == 0 and Xu.subs(q, 3) == Xv.subs(q, 3) == sp.Rational(19, 32))
print("ALL PASS" if ok_all else "SOME FAIL")
