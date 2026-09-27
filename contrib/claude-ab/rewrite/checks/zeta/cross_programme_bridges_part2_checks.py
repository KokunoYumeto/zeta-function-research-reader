# Checks for 28_ (cross-programme bridges, part 2): the Jacobian polynomial in the NS material calculation and the YM
# tensor transfer; the S6 period block in the YM magnetic background; the cyclotomic clock transfer (Bost-Connes).
# claude-ab (Opus 5.5, max effort), 25 September 2026.
import itertools
from fractions import Fraction
import sympy as sp

ok_all = True


def report(name, ok, detail=''):
    global ok_all
    ok_all &= bool(ok)
    print(('PASS ' if ok else 'FAIL ') + name + ('  ' + detail if detail else ''))


# ---------- J: the Jacobian polynomial F and its material generator ----------
x, y, w, z, tau = sp.symbols('x y w z tau')
F1 = (1 + x * y) ** 3 * w + y ** 2 * (1 + x * y) * (4 + 3 * x * y)
F2 = y + 3 * x * (1 + x * y) ** 2 * w + 3 * x * y ** 2 * (4 + 3 * x * y)
F3 = 2 * x - 3 * x ** 2 * y - x ** 3 * w
F = sp.Matrix([F1, F2, F3]); X = sp.Matrix([x, y, w])
J = F.jacobian(X)
detJ = sp.simplify(J.det())
report('J1 det DF = -2 identically', detJ == -2, 'det = %s' % detJ)
adj = J.adjugate()
Jinv = adj / detJ
# Piola: each row of cof(DF) = adj^T has zero divergence  <=>  sum_j d_j adj[j,i] = 0 for each i
piola = [sp.simplify(sum(sp.diff(adj[j, i], X[j]) for j in range(3))) for i in range(3)]
report('J2 Piola identity: the columns of adj(DF) are divergence-free', all(p == 0 for p in piola), str(piola))
U0 = (Jinv * sp.Matrix([2, 0, 0])).applyfunc(sp.expand)
U = (Jinv * sp.Matrix([2, 6 * F3, 0])).applyfunc(sp.expand)
polyU = all(sp.Poly(u, x, y, w) is not None for u in list(U0) + list(U))
divU0 = sp.simplify(sum(sp.diff(U0[i], X[i]) for i in range(3)))
divU = sp.simplify(sum(sp.diff(U[i], X[i]) for i in range(3)))
report('J3 U0 = DF^{-1}(2,0,0) and U = DF^{-1}(2, 6F3, 0) are polynomial and divergence-free', polyU and divU0 == 0 and divU == 0,
       'deg U0 = %d, deg U = %d' % (max(sp.Poly(u, x, y, w).total_degree() for u in U0), max(sp.Poly(u, x, y, w).total_degree() for u in U)))
zz = sp.sqrt(1 - 8 * tau)
g = sp.Matrix([1 / zz, -sp.Rational(3, 2) * zz, sp.Rational(13, 2) * zz ** 2])
Fg = sp.simplify(F.subs({x: g[0], y: g[1], w: g[2]}))
dg = g.diff(tau)
res0 = sp.simplify(dg - U0.subs({x: g[0], y: g[1], w: g[2]}))
res1 = sp.simplify(dg - U.subs({x: g[0], y: g[1], w: g[2]}))
report('J4 gamma(tau) = (z^-1, -3z/2, 13z^2/2), z = sqrt(1-8 tau): F(gamma) = (-1/4 + 2 tau, 0, 0); gamma is an integral curve of U0 and of U',
       list(Fg) == [2 * tau - sp.Rational(1, 4), 0, 0] and list(res0) == [0, 0, 0] and list(res1) == [0, 0, 0], str(list(Fg)))
# material tensor along gamma, in the variable z (tau = (1 - z^2)/8)
zp = sp.symbols('zp', positive=True)
tz = (1 - zp ** 2) / 8
gz = {x: 1 / zp, y: -sp.Rational(3, 2) * zp, w: sp.Rational(13, 2) * zp ** 2}
Jg = sp.simplify(J.subs(gz))
J0 = J.subs({x: 1, y: -sp.Rational(3, 2), w: sp.Rational(13, 2)})
B = sp.eye(3); B[1, 2] = 6 * tz
A = sp.simplify(Jg.inv() * B * J0)
C = sp.simplify(A.inv())
K = sp.simplify(C * C.T)
zeta = C.T * sp.Matrix([0, 0, 1])
nz2 = sp.simplify((zeta.T * zeta)[0])
lead = [sp.limit(zp ** 6 * K[i, j], zp, 0) for i in range(3) for j in range(3)]
v = sp.Matrix([sp.Rational(1, 4), sp.Rational(3, 8), -sp.Rational(9, 4)])
report('J5 det A = 1, A(tau=0) = I; |zeta|^2 z^6 -> 81/16; z^6 K -> v v^T with v = (1/4, 3/8, -9/4), |v|^2 = 337/64',
       sp.simplify(A.det()) == 1 and A.subs(zp, 1) == sp.eye(3) and sp.limit(nz2 * zp ** 6, zp, 0) == sp.Rational(81, 16)
       and lead == list(v * v.T) and (v.T * v)[0] == sp.Rational(337, 64))
e2 = sp.simplify(K[0, 0] * K[1, 1] - K[0, 1] ** 2 + K[0, 0] * K[2, 2] - K[0, 2] ** 2 + K[1, 1] * K[2, 2] - K[1, 2] ** 2)
e2lim = sp.limit(sp.simplify(zp ** 6 * e2), zp, 0)
trlim = sp.limit(sp.simplify(zp ** 6 * K.trace()), zp, 0)
report('J5b z^6 e2(K) -> 121/64 and z^6 tr K -> 337/64, with det K = 1: so lambda2 -> 121/337, lambda1 ~ (64/121) z^6, lambda3 ~ (337/64) z^-6',
       e2lim == sp.Rational(121, 64) and trlim == sp.Rational(337, 64) and sp.simplify(K.det()) == 1, str((e2lim, trlim)))
tr = K.trace()
c0 = sp.limit(sp.simplify(zp ** 12 * tr ** 2 / 9), zp, 0)
cd = sp.limit(sp.simplify(zp ** 12 * sp.Rational(1, 2) * sum((K[i, i] - tr / 3) ** 2 for i in range(3))), zp, 0)
co = sp.limit(sp.simplify(zp ** 12 * sum(K[i, j] ** 2 for i in range(3) for j in range(3) if i < j)), zp, 0)
report('J6 endpoint spectral-measure coefficients 113569/36864, 100825/12288, 531/512 (FABEL_CORRECTIONS)',
       (c0, cd, co) == (sp.Rational(113569, 36864), sp.Rational(100825, 12288), sp.Rational(531, 512)), str((c0, cd, co)))
# J7: flows of an automorphism are complete. Example: the polynomial automorphism G(x,y,w) = (x, y + x^2, w + (y + x^2)^3), V = (2,0,0)
xG = sp.Matrix([x, y + x ** 2, w + (y + x ** 2) ** 3])
DG = xG.jacobian(X)
Ginv = lambda a, b, c: sp.Matrix([a, b - a ** 2, c - b ** 3])
a0, b0, c0_ = sp.symbols('a0 b0 c0')
curve = Ginv(a0 + 2 * tau, b0, c0_)   # preimage of the straight line a = a0 + 2 tau
dcurve = curve.diff(tau)
UG = (DG.inv() * sp.Matrix([2, 0, 0])).subs({x: curve[0], y: curve[1], w: curve[2]})
report('J7 for a polynomial automorphism G, the integral curves of DG^{-1}v are G^{-1}(line), polynomial in tau (defined for all tau)',
       sp.simplify(dcurve - UG) == sp.zeros(3, 1) and all(sp.Poly(c, tau) is not None for c in curve))

# ---------- S: the S6 period block in the YM magnetic background ----------
m, L, q, y1, y2, dy1, dy2 = sp.symbols('m L q y1 y2 dy1 dy2')
Bm = sp.Matrix([[6 * m, L], [-q, m]])
D = L * q + 6 * m ** 2
u = (Bm.inv() * sp.Matrix([y1, y2])).applyfunc(sp.simplify)
ok_inv = sp.simplify(Bm.det() - D) == 0 and sp.simplify(u - sp.Matrix([m * y1 - L * y2, q * y1 + 6 * m * y2]) / D) == sp.zeros(2, 1)
du1 = sp.diff(u[0], y1) * dy1 + sp.diff(u[0], y2) * dy2
du2 = sp.diff(u[1], y1) * dy1 + sp.diff(u[1], y2) * dy2
# A_orig = 2 pi u1 du2 (coefficient of H_c); compare with b y1 dy2 + df
bb = 2 * sp.pi / D
f = 2 * sp.pi / D ** 2 * (m * q / 2 * y1 ** 2 - L * q * y1 * y2 - 3 * m * L * y2 ** 2)
Aorig = sp.expand(2 * sp.pi * u[0] * du2)
rhs = sp.expand(bb * y1 * dy2 + sp.diff(f, y1) * dy1 + sp.diff(f, y2) * dy2)
wedge = sp.simplify(sp.diff(u[0], y1) * sp.diff(u[1], y2) - sp.diff(u[0], y2) * sp.diff(u[1], y1))
report('S1 det B = D = Lq + 6m^2; u = B^{-1}(y1, y2); du1^du2 = D^{-1} dy1^dy2; A_orig = (2pi/D) y1 dy2 + df (magnetic_translation 1.4)',
       ok_inv and sp.simplify(Aorig - rhs) == 0 and sp.simplify(wedge - 1 / D) == 0)

# ---------- C: the cyclotomic clock transfer (integral Bost-Connes relations) ----------
Nmax = 72


def elem(d):
    return {k % 1: v for k, v in d.items() if v != 0}


def mul(a, b):
    out = {}
    for r, cr in a.items():
        for s, cs in b.items():
            t = (r + s) % 1
            out[t] = out.get(t, 0) + cr * cs
    return {k: v for k, v in out.items() if v != 0}


def sigma(n, a):
    out = {}
    for r, c in a.items():
        t = (n * r) % 1
        out[t] = out.get(t, 0) + c
    return {k: v for k, v in out.items() if v != 0}


def rho(n, a):
    out = {}
    for r, c in a.items():
        for k in range(n):
            t = ((r + k) / n) % 1
            out[t] = out.get(t, 0) + c
    return {k: v for k, v in out.items() if v != 0}


def E(n):
    return {Fraction(k, n): 1 for k in range(n)}


def scal(c, a):
    return {k: c * v for k, v in a.items() if c * v != 0}


def eq(a, b):
    return {k: v for k, v in a.items() if v} == {k: v for k, v in b.items() if v}


import random
random.seed(3)
def rand_elem():
    d = {}
    for _ in range(4):
        den = random.choice([1, 2, 3, 4, 5, 6, 8, 9, 12])
        d[Fraction(random.randrange(den), den)] = random.randint(-3, 3)
    return {k: v for k, v in d.items() if v}
bad = 0
count = 0
from math import gcd
for _ in range(40):
    a, b = rand_elem(), rand_elem()
    for n in [2, 3, 4, 6]:
        for mm in [2, 3, 4, 6]:
            count += 1
            dd = gcd(mm, n)
            checks = [eq(sigma(mm, sigma(n, a)), sigma(mm * n, a)), eq(rho(mm, rho(n, a)), rho(mm * n, a)),
                      eq(sigma(n, rho(n, a)), scal(n, a)), eq(rho(n, sigma(n, a)), mul(E(n), a)),
                      eq(mul(E(n), E(n)), scal(n, E(n))), eq(mul(rho(n, a), rho(n, b)), scal(n, rho(n, mul(a, b)))),
                      eq(rho(n, mul(sigma(n, a), b)), mul(a, rho(n, b))),
                      eq(sigma(mm, rho(n, a)), scal(dd, rho(n // dd, sigma(mm // dd, a))))]
            bad += checks.count(False)
report('C1 integral Bost-Connes relations (14) of CCT-2 on random elements of Z[Q/Z], n, m in {2,3,4,6}', bad == 0, '%d configurations, %d failures' % (count, bad))

# C2: finite-level form of (14c): Z[C_N]/(I_n + E_n Z[C_N]) has order n^(N/n) (the kernel of sigma_n mod n onto (Z/n)[C_{N/n}])
def lattice_index(N, n):
    # basis e_N(a), a = 0..N-1; generators: (e(1/n)-1) e_N(a) and E_n e_N(a)
    gens = []
    step = N // n
    for a in range(N):
        v = [0] * N; v[(a + step) % N] += 1; v[a] -= 1; gens.append(v)
        v = [0] * N
        for k in range(n):
            v[(a + k * step) % N] += 1
        gens.append(v)
    M = sp.Matrix(gens)
    from sympy.matrices.normalforms import smith_normal_form
    S = smith_normal_form(M, domain=sp.ZZ)
    diag = [abs(S[i, i]) for i in range(min(S.shape)) if S[i, i] != 0]
    rank = len(diag)
    idx = 1
    for d_ in diag:
        idx *= d_
    return rank, idx
ok2 = True
det2 = []
for (N, n) in [(4, 2), (6, 2), (6, 3), (8, 4), (12, 3), (12, 6)]:
    r, idx = lattice_index(N, n)
    det2.append((N, n, r, idx, n ** (N // n)))
    ok2 &= (r == N and idx == n ** (N // n))
report('C2 CCT-2a (14c) at finite level: [Z[C_N] : I_n + E_n Z[C_N]] = n^(N/n)', ok2, str(det2))

# C3: CCT-7 (41)-(42a): for odd n and g = T^a, the source-fibre pushforward differs from rho_n exactly when gcd(a,n) > 1,
#     and the difference lies in ker sigma_n
ok3 = True
for n in [3, 5, 9, 15]:
    for a_ in [1, 2, 3, 5, 6, 9]:
        r0 = Fraction(1, 7)            # label of pi_g(chi) (any), choose v0 with n v0 = r0 among the fibre images
        v0 = r0 / n
        dgc = gcd(a_, n)
        A_set = [ (v0 + Fraction(k, n // dgc)) % 1 for k in range(n // dgc) ]
        push = {}
        for t in A_set:
            push[t] = push.get(t, 0) + dgc
        tr_ = rho(n, {r0: 1})
        diff = {k: push.get(k, 0) - tr_.get(k, 0) for k in set(push) | set(tr_)}
        diff = {k: v for k, v in diff.items() if v}
        in_kernel = eq(sigma(n, diff), {})
        ok3 &= in_kernel and ((len(diff) == 0) == (dgc == 1))
report('C3 CCT-7: pushforward = BC transfer iff gcd(a,n) = 1; the defect lies in ker sigma_n', ok3)

print('ALL PASS' if ok_all else 'SOME FAILED')
