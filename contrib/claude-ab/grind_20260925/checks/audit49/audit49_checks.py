#!/usr/bin/env python3
"""Checks for note 49_ (audit of TPL0-TPL13, OZR0-OZR10, FT1-FT10, PCJ0-PCJ10).

Every check prints PASS or FAIL with the quantity it compares.  Exact
arithmetic (sympy, fractions) is used wherever the statement is exact;
mpmath is used for the analytic identities at sample points.
Run: python3 audit49_checks.py   (a few seconds)
"""
import itertools
import random
from fractions import Fraction
from math import gcd

import mpmath as mp
import sympy as sp

random.seed(20260927)
mp.mp.dps = 40
RESULTS = []
IDS = (["A%d" % i for i in range(1, 7)] + ["B%d" % i for i in range(1, 12)] + ["C%d" % i for i in range(1, 10)]
       + ["D%d" % i for i in range(1, 6)] + ["E1", "E2"])


def check(name, ok, detail=""):
    label = IDS[len(RESULTS)] if len(RESULTS) < len(IDS) else "X%d" % len(RESULTS)
    RESULTS.append(ok)
    print(("PASS " if ok else "FAIL ") + label + " " + name + (("  [" + str(detail) + "]") if detail != "" else ""))


def rank(M):
    return sp.Matrix(M).rank()


def nullspace_dim(M, ncols):
    if len(M) == 0:
        return ncols
    return ncols - rank(M)


# ---------------------------------------------------------------- Part A: TPL
def shift_power(m, a):
    """Matrix of multiplication by t^a on J_m = C[t]/(t^m), basis 1,t,...,t^{m-1}."""
    M = sp.zeros(m, m)
    for j in range(m):
        if j + a < m:
            M[j + a, j] = 1
    return M


def tpl9_dims(m, a, b):
    rp, rm = shift_power(m, a), shift_power(m, b)
    d = rp.row_join(-rm)  # d(a+,a-) = r+ a+ - r- a-
    rd = d.rank()
    h0 = 2 * m - rd
    h1 = m - rd
    im_res = rp.rank() + rm.rank() - rd  # dim(r+A+ ∩ r-A-)
    return h0, h1, im_res


ok = True
bad = []
for m in range(1, 9):
    for a in range(0, m + 1):
        for b in range(0, m + 1):
            k, h = min(a, b), max(a, b)
            got = tpl9_dims(m, a, b)
            if got != (m + k, k, m - h):
                ok = False
                bad.append((m, a, b, got))
check("TPL9.6: dim H^0 = m+k, dim H^1 = k, dim im(res) = m-h for all m<=8, 0<=a,b<=m", ok, bad[:3])

# TPL9.5: (y,u) -> (t^{b-a} y + u, y) is an isomorphism J_m ⊕ t^{m-a}J_m -> H^0 (a<=b)
ok = True
for m in range(1, 8):
    for a in range(0, m + 1):
        for b in range(a, m + 1):
            rp, rm = shift_power(m, a), shift_power(m, b)
            # basis of source: y in J_m (m vectors), u in t^{m-a}J_m (a vectors: t^{m-a},...,t^{m-1})
            cols = []
            for j in range(m):
                y = sp.zeros(m, 1); y[j] = 1
                x = shift_power(m, b - a) * y
                cols.append(x.col_join(y))
            for j in range(m - a, m):
                u = sp.zeros(m, 1); u[j] = 1
                cols.append(u.col_join(sp.zeros(m, 1)))
            Mimg = sp.Matrix.hstack(*cols) if cols else sp.zeros(2 * m, 0)
            # each image vector lies in H^0: r+ x = r- y
            d = rp.row_join(-rm)
            in_h0 = (d * Mimg).is_zero_matrix
            inj = Mimg.rank() == m + a
            if not (in_h0 and inj and m + a == 2 * m - d.rank()):
                ok = False
check("TPL9.5: the map (y,u) -> (t^(b-a)y+u, y) is an isomorphism onto H^0 (m<=7, a<=b)", ok)

# Classification implied by TPL9: every J_m-linear endomorphism of J_m is t^a * unit (a=valuation), so the
# rank-one free diagrams are classified by (dim ker r+, dim ker r-) = (a,b).
ok = True
t = sp.symbols('t')
for m in range(1, 7):
    for trial in range(20):
        coeffs = [random.randint(-3, 3) for _ in range(m)]
        if all(c == 0 for c in coeffs):
            continue
        a = next(i for i, c in enumerate(coeffs) if c != 0)
        # multiplication by g = sum coeffs[i] t^i on J_m
        G = sp.zeros(m, m)
        for i, c in enumerate(coeffs):
            G += c * shift_power(m, i)
        if (m - G.rank()) != a:  # dim ker = valuation
            ok = False
check("TPL9 classification: dim ker(mult by g) = ord_t(g) on J_m (m<=6, random g)", ok)


def rand_int_matrix(r, c, lo=-2, hi=2):
    return sp.Matrix(r, c, lambda i, j: random.randint(lo, hi))


# TPL5.3: exactness of 0 -> ker r+ ⊕ ker r- -> H^0 -> B -> B/r+A+ ⊕ B/r-A- -> H^1 -> 0, by dimensions
ok = True
for trial in range(40):
    dB, dp, dm = random.randint(1, 6), random.randint(0, 6), random.randint(0, 6)
    rp = rand_int_matrix(dB, dp) if dp else sp.zeros(dB, 0)
    rm = rand_int_matrix(dB, dm) if dm else sp.zeros(dB, 0)
    # sometimes lower the rank
    if dp and random.random() < 0.5:
        rp = rp * sp.diag(*([0] + [1] * (dp - 1)))
    both = rp.row_join(rm)
    rk_p, rk_m, rk_s = rp.rank(), rm.rank(), both.rank()
    dimK0 = (dp - rk_p) + (dm - rk_m)
    dimH0 = dp + dm - rk_s
    dimKer_delta = rk_p + rk_m - rk_s       # r+A+ ∩ r-A-
    dimH1K = (dB - rk_p) + (dB - rk_m)
    dimH1 = dB - rk_s
    # exactness: the alternating sum of dimensions vanishes, and ker(delta) = im(res) = H^0/K0
    alt = dimK0 - dimH0 + dB - dimH1K + dimH1
    if alt != 0 or dimKer_delta != dimH0 - dimK0:
        ok = False
check("TPL5.3 dimension bookkeeping only (an identity in the ranks; exactness itself is tested by the referee's R-A1)", ok)


# TPL10.5: 0 -> coker(N|H^0) -> H^1_tot -> ker(N|H^1) -> 0 and H^2_tot = coker(N|H^1),
# on random diagrams of free J_m-modules with J_m-linear restrictions (so N = t commutes).
def jm_block(m, poly_coeffs):
    M = sp.zeros(m, m)
    for i, c in enumerate(poly_coeffs):
        M += c * shift_power(m, i)
    return M


def random_jm_map(m, rows, cols):
    blocks = [[jm_block(m, [random.randint(-2, 2) if random.random() < 0.6 else 0 for _ in range(m)])
               for _ in range(cols)] for _ in range(rows)]
    if rows == 0 or cols == 0:
        return sp.zeros(m * rows, m * cols)
    return sp.Matrix(sp.BlockMatrix(blocks))


def quotient_dim_map(Nmat, sub_basis_cols, amb_dim):
    """dim ker and dim coker of the map induced by N on V/W with W spanned by sub_basis_cols (N W ⊂ W)."""
    W = sub_basis_cols
    rW = W.rank() if W.shape[1] else 0
    # dim of N(V)+W and dim of {v : N v ∈ W}
    NV_plus_W = Nmat.row_join(W) if W.shape[1] else Nmat
    dim_coker = amb_dim - NV_plus_W.rank()
    # preimage of W under N: solve N v ∈ W  <=>  [N | -W] (v; w) = 0
    Aug = Nmat.row_join(-W) if W.shape[1] else Nmat
    ns = Aug.nullspace()
    pre = sp.Matrix.hstack(*[v[:amb_dim, :] for v in ns]) if ns else sp.zeros(amb_dim, 0)
    pre_plus_W = pre.row_join(W) if W.shape[1] else pre
    dim_pre = pre_plus_W.rank()  # contains W
    dim_ker = dim_pre - rW
    return dim_ker, dim_coker


ok = True
for trial in range(12):
    m = random.randint(1, 3)
    kB, kp, km = random.randint(1, 2), random.randint(0, 2), random.randint(0, 2)
    rp = random_jm_map(m, kB, kp)
    rm = random_jm_map(m, kB, km)
    NB = sp.diag(*([shift_power(m, 1)] * kB)) if kB else sp.zeros(0, 0)
    NA = sp.diag(*([shift_power(m, 1)] * (kp + km))) if (kp + km) else sp.zeros(0, 0)
    dimA, dimB = m * (kp + km), m * kB
    d = rp.row_join(-rm) if (kp + km) else sp.zeros(dimB, 0)
    # commutation d N_A = N_B d
    if dimA and not (d * NA - NB * d).is_zero_matrix:
        ok = False
        continue
    # total complex A -> B ⊕ A -> B
    d0 = d.col_join(NA) if dimA else sp.zeros(dimB, 0)
    d1 = (-NB).row_join(d) if dimA else -NB
    if dimA and not (d1 * d0).is_zero_matrix:
        ok = False
        continue
    r0 = d0.rank() if dimA else 0
    r1 = d1.rank()
    H0tot = dimA - r0
    H1tot = (dimB + dimA) - r1 - r0
    H2tot = dimB - r1
    # H^0(X,F) = ker d with N_A; H^1 = B/dA with N_B
    kerd = d.nullspace() if dimA else []
    K = sp.Matrix.hstack(*kerd) if kerd else sp.zeros(dimA, 0)
    dimH0 = K.shape[1]
    # N on ker d: coker dimension = dimH0 - rank(N_A K) (N_A K ⊂ ker d)
    coker_N_H0 = dimH0 - ((NA * K).rank() if dimH0 else 0)
    ker_N_H0 = dimH0 - ((NA * K).rank() if dimH0 else 0)
    imd = d if dimA else sp.zeros(dimB, 0)
    ker_N_H1, coker_N_H1 = quotient_dim_map(NB, imd, dimB)
    lhs_ok = (H1tot == coker_N_H0 + ker_N_H1) and (H2tot == coker_N_H1) and (H0tot == ker_N_H0)
    if not lhs_ok:
        ok = False
check("TPL10.4-10.5: H^0_tot = ker N|H^0 and H^1_tot = coker N|H^0 + ker N|H^1 (12 random J_m diagrams; the H^2 comparison is definitional)", ok)

# TPL10.2: M - 1 = N H(N) with H(N) invertible, on a random nilpotent matrix
Nm = sp.Matrix([[0, 1, 2, 0], [0, 0, 3, 1], [0, 0, 0, 5], [0, 0, 0, 0]])
M = (Nm).exp()
H = sp.zeros(4, 4)
for j in range(4):
    H += Nm ** j / sp.factorial(j + 1)
check("TPL10.1-10.2: exp(N) - 1 = N H(N) with det H(N) = 1", (M - sp.eye(4) - Nm * H).is_zero_matrix and H.det() == 1)


# ---------------------------------------------------------------- Part B: OZR
x, y, tt, r, p = sp.symbols('x y t r p', positive=True)
hfun = sp.Function('h')(x)
E = sp.exp(2 * tt * (x ** 2 - y ** 2))
lap = sp.diff(hfun * E, x, 2) + sp.diff(hfun * E, y, 2)
target = E * (sp.diff(hfun, x, 2) + 8 * tt * x * sp.diff(hfun, x) + 16 * tt ** 2 * (x ** 2 + y ** 2) * hfun)
check("OZR4 / OZD3.3: Laplacian of h(x)e^{2t(x^2-y^2)} (the 4t terms cancel)", sp.simplify(lap - target) == 0)

q = (r ** x - r ** (1 - x)) ** 2
check("OZR4: q_r' = 2 log r (r^{2x} - r^{2-2x})", sp.simplify(sp.diff(q, x) - 2 * sp.log(r) * (r ** (2 * x) - r ** (2 - 2 * x))) == 0)
check("OZR4: q_r'' = 4 (log r)^2 (r^{2x} + r^{2-2x})", sp.simplify(sp.diff(q, x, 2) - 4 * sp.log(r) ** 2 * (r ** (2 * x) + r ** (2 - 2 * x))) == 0)
check("OZR4: q_r(1) = (r-1)^2 and q_r(1/2) = 0", sp.simplify(q.subs(x, 1) - (r - 1) ** 2) == 0 and sp.simplify(q.subs(x, sp.Rational(1, 2))) == 0)

w = (1 + y ** 2) ** (-p / 2)
check("OZR8.4: w_p'' = p((p+1)y^2 - 1)(1+y^2)^{-p/2-2}",
      sp.simplify(sp.diff(w, y, 2) - p * ((p + 1) * y ** 2 - 1) * (1 + y ** 2) ** (-p / 2 - 2)) == 0)
# derivative bounds |w^(k)| <= C (1+|y|)^{-p}: ratio w^(k)/w is O(1/|y|^k)
ok = True
for pv in [1.2, 1.5, 3.0]:
    wv = (1 + y ** 2) ** (-sp.Float(pv) / 2)
    for k in (1, 2):
        ratio = sp.lambdify(y, sp.diff(wv, y, k) / wv)
        vals = [abs(ratio(Y)) for Y in [0.5, 1, 10, 100, 1000]]
        if max(vals) > 10:
            ok = False
check("OZR8.1 for w_p: |w_p^(k)| <= C w_p for k = 1, 2 (sampled for p = 1.2, 1.5, 3)", ok)

# |F_0(2+iy)|^2 identity, F_0 = s(s-1) pi^{-s/2} Gamma(s/2) zeta(s) / 8
ok = True
for Y in [mp.mpf('0.3'), mp.mpf(1), mp.mpf(5), mp.mpf('17.5'), mp.mpf(-3)]:
    s = mp.mpc(2, Y)
    F0 = s * (s - 1) * mp.power(mp.pi, -s / 2) * mp.gamma(s / 2) * mp.zeta(s) / 8
    rhs = (4 + Y ** 2) * (1 + Y ** 2) / (64 * mp.pi ** 2) * (mp.pi * Y / 2) / mp.sinh(mp.pi * Y / 2) * abs(mp.zeta(s)) ** 2
    if abs(abs(F0) ** 2 - rhs) > mp.mpf(10) ** -30 * max(1, rhs):
        ok = False
check("OZR5: |F_0(2+iy)|^2 = (4+y^2)(1+y^2)/(64 pi^2) (pi y/2)/sinh(pi y/2) |zeta(2+iy)|^2", ok)

# functional equation zeta(s) = chi(s) zeta(1-s)
ok = True
for s in [mp.mpc(0.3, 2), mp.mpc(-1.5, 7), mp.mpc(2.5, -4)]:
    chi = mp.power(mp.pi, s - mp.mpf(1) / 2) * mp.gamma((1 - s) / 2) / mp.gamma(s / 2)
    if abs(mp.zeta(s) - chi * mp.zeta(1 - s)) > mp.mpf(10) ** -30:
        ok = False
check("OZR6: zeta(s) = pi^{s-1/2} Gamma((1-s)/2)/Gamma(s/2) zeta(1-s)", ok)

# OZR3.1 Euler-Maclaurin with K0 = 1, 2, 3 at a point inside the critical strip
def em_zeta(s, K0, N=400):
    # remainder integral int_1^oo B_{2K0}({u}) u^{-s-2K0} du, summed over unit intervals, tail by the next term bound
    B = lambda k, xx: mp.bernpoly(k, xx)
    tot = mp.mpf(0)
    for n in range(1, N):
        tot += mp.quad(lambda uu: B(2 * K0, uu - n) * mp.power(uu, -s - 2 * K0), [n, n + 1])
    val = 1 / (s - 1) + mp.mpf(1) / 2
    for k in range(1, K0 + 1):
        val += mp.bernoulli(2 * k) / mp.factorial(2 * k) * mp.rf(s, 2 * k - 1)
    val -= mp.rf(s, 2 * K0) / mp.factorial(2 * K0) * tot
    return val

mp.mp.dps = 20
s0 = mp.mpc(0.5, 3)
errs = [abs(em_zeta(s0, K0) - mp.zeta(s0)) for K0 in (2, 3)]
mp.mp.dps = 40
check("OZR3.1: Euler-Maclaurin formula (K0 = 2, 3) reproduces zeta(1/2+3i) (tail beyond u = 400 omitted)", max(errs) < 1e-6, [mp.nstr(e, 3) for e in errs])

# OZR3.2: |zeta(2+ij)| >= 1/zeta(2)
check("OZR3.2: min over j<=200 of |zeta(2+ij)| zeta(2) >= 1",
      min(abs(mp.zeta(mp.mpc(2, j))) * mp.zeta(2) for j in range(0, 201)) >= 1)

# OZR6.1 bookkeeping: with phi_- odd under R(x) = 1-x, (1/2) sum_k [phi(-2k) - phi(1+2k)] = -phi(1) + sum_{k>=1} phi(-2k)
ok = True
for trial in range(5):
    cs = [random.uniform(-1, 1) for _ in range(4)]
    phi = lambda X: sum(c * (X - 0.5) ** (2 * i + 1) * mp.exp(-(X - 0.5) ** 2) for i, c in enumerate(cs))  # odd about 1/2
    lhs = mp.mpf(1) / 2 * mp.nsum(lambda k: phi(-2 * k) - phi(1 + 2 * k), [0, mp.inf])
    rhs = -phi(1) + mp.nsum(lambda k: phi(-2 * k), [1, mp.inf])
    if abs(lhs - rhs) > mp.mpf(10) ** -25:
        ok = False
check("OZR6.1: reflection bookkeeping of the odd part (random odd tests)", ok)

# ---------------------------------------------------------------- Part C: FT
def den(fr):
    return fr.denominator


ok = True
for trial in range(2000):
    a, b = random.randint(1, 60), random.randint(1, 60)
    c, d = random.randint(1, 60), random.randint(1, 60)
    rr, ss = Fraction(a, b), Fraction(c, d)
    a, b = rr.numerator, rr.denominator
    c, d = ss.numerator, ss.denominator
    # c_r c_s = den(r) den(s) b_{rs} = h c_{rs} with h = den r den s / den(rs) = gcd(ac, bd)
    h = den(rr) * den(ss) // den(rr * ss)
    if h * den(rr * ss) != den(rr) * den(ss) or h != gcd(a * c, b * d):
        ok = False
check("FT1.5: c_r c_s = gcd(ac,bd) c_rs, with gcd(ac,bd) = den(r)den(s)/den(rs) (2000 random pairs)", ok)

ok = True
primes = [2, 3, 5, 7, 11]
for trial in range(500):
    e = {pp: random.randint(-3, 3) for pp in primes}
    rr = Fraction(1)
    for pp, ee in e.items():
        rr *= Fraction(pp) ** ee
    coeff = 1
    for pp, ee in e.items():
        if ee < 0:
            coeff *= pp ** (-ee)
    if coeff != den(rr):
        ok = False
check("FT2.5: the normal monomial m_e maps to (prod_{e_p<0} p^{-e_p}) b_r = c_r (500 random exponent vectors)", ok)

def ga_mul(u, v):
    out = {}
    for k1, c1 in u.items():
        for k2, c2 in v.items():
            out[k1 * k2] = out.get(k1 * k2, 0) + c1 * c2
    return {k: c for k, c in out.items() if c}


def Fel(n):
    return {Fraction(n): 1}


def Vel(n):
    return {Fraction(1, n): n}


ok = True
for trial in range(2000):
    mm, nn = random.randint(1, 200), random.randint(1, 200)
    dd = gcd(mm, nn)
    lhs = ga_mul(Fel(mm), Vel(nn))
    rhs = {k: dd * c for k, c in ga_mul(Fel(mm // dd), Vel(nn // dd)).items()}
    if lhs != rhs:
        ok = False
check("FT3.6: F_m V_n = gcd(m,n) F_{m/d} V_{n/d}, multiplied out in the group algebra Q[Q>0^x] (2000 random pairs)", ok)


# FT6-FT8 matrices (degrees 0,1,2)
n_, q_, A_, B_ = sp.symbols('n q A B', positive=True)
P = [sp.Matrix([[1]]), sp.diag(n_, 1), sp.Matrix([[n_]])]
S = [sp.Matrix([[n_]]), sp.diag(1, n_), sp.Matrix([[1]])]
vstar = [sp.Matrix([[1]]), sp.diag(1, n_), sp.Matrix([[n_]])]
ok = all((S[i] * P[i] - n_ * sp.eye(P[i].shape[0])).is_zero_matrix and (P[i] * S[i] - n_ * sp.eye(P[i].shape[0])).is_zero_matrix for i in range(3))
check("FT6.9: S P = n and P S = n in degrees 0, 1, 2", ok)
check("FT6.10: the typed matrices of v* equal S in degree 1 and differ in degrees 0 and 2 (derived from the lattice maps in the referee's R-C1)", vstar[1] == S[1] and vstar[0] != S[0] and vstar[2] != S[2])

def gram(qq):
    return [sp.Matrix([[qq * A_ * B_]]), sp.diag(B_ / (qq * A_), qq * A_ / B_), sp.Matrix([[1 / (qq * A_ * B_)]])]

ok = True
for i in range(3):
    Gq, Gnq = gram(q_)[i], gram(n_ * q_)[i]
    # h_{nq}(P x, y) = h_q(x, S y):   P^T G_{nq} = G_q S   (real symmetric forms, real matrices)
    if not sp.simplify(P[i].T * Gnq - Gq * S[i]).is_zero_matrix:
        ok = False
    # h_{nq}(P x, P x') = n h_q(x, x')
    if not sp.simplify(P[i].T * Gnq * P[i] - n_ * Gq).is_zero_matrix:
        ok = False
check("FT8.3: h_nq(Px,y) = h_q(x,Sy) and h_nq(Px,Px') = n h_q(x,x') in every degree", ok)

# Gram matrices from the invariant forms: e = 1, alpha = dx/(qA), beta = dtheta/B, h = dx dtheta/(qAB), area qAB
ok = sp.simplify(q_ * A_ * B_ * (1 / (q_ * A_)) ** 2 - B_ / (q_ * A_)) == 0 and sp.simplify(q_ * A_ * B_ / B_ ** 2 - q_ * A_ / B_) == 0 \
    and sp.simplify(q_ * A_ * B_ / (q_ * A_ * B_) ** 2 - 1 / (q_ * A_ * B_)) == 0
check("FT8.2: Gram matrices qAB, diag(B/(qA), qA/B), 1/(qAB) from the flat metric", ok)

m_, n2_ = sp.symbols('m n2', positive=True)
Pm = [sp.Matrix([[1]]), sp.diag(m_, 1), sp.Matrix([[m_]])]
Sn = [sp.Matrix([[n2_]]), sp.diag(1, n2_), sp.Matrix([[1]])]
ok = all((Pm[i] * Sn[i] - Sn[i] * Pm[i]).is_zero_matrix for i in range(3))
ok = ok and [Pm[i] * Sn[i] for i in range(3)] == [sp.Matrix([[n2_]]), sp.diag(m_, n2_), sp.Matrix([[m_]])]
check("FT7.4-7.5: F_m V_n = V_n F_m with matrices n, diag(m,n), m", ok)

# FT10: apply F_n (e_q -> e_{nq}) to z_N = sum_{|k|<=N} lambda^{-k} e_{n^k}, with |lambda|^2 = n exactly
ok = True
for nval in [2, 3, 5]:
    lam = sp.sqrt(nval) * (sp.Rational(3, 5) + sp.I * sp.Rational(4, 5))
    for N in [0, 1, 3, 6]:
        z = {sp.Rational(nval) ** k: lam ** (-k) for k in range(-N, N + 1)}
        Fz = {nval * q: c for q, c in z.items()}
        diff = dict(Fz)
        for q, c in z.items():
            diff[q] = diff.get(q, 0) - lam * c
        norm2 = lambda v: sp.nsimplify(sp.simplify(sum(q * sp.Abs(sp.expand(c)) ** 2 for q, c in v.items())))  # divided by AB
        if sp.simplify(norm2(z) - (2 * N + 1)) != 0 or sp.simplify(norm2(diff) - 2 * nval) != 0:
            ok = False
check("FT10.8, FT10.10: with F_n applied to z_N (exact, |lambda|^2 = n): ||z_N||^2 = (2N+1)AB, ||(F_n - lambda)z_N||^2 = 2nAB", ok)

# ---------------------------------------------------------------- Part D: PCJ
ok = True
for trial in range(1000):
    rr = Fraction(random.randint(1, 99), random.randint(1, 99))
    a, b = rr.numerator, rr.denominator
    lhs = b * mp.sqrt(mp.mpf(a) / b)
    if abs(lhs - mp.sqrt(a * b)) > 1e-30:
        ok = False
    # involution compatibility: coefficient of C_{1/r} equals that of C_r
    if abs(a * mp.sqrt(mp.mpf(b) / a) - mp.sqrt(a * b)) > 1e-30:
        ok = False
check("PCJ2.3 (an algebraic identity, sampled): b sqrt(a/b) = sqrt(ab) = a sqrt(b/a)", ok)

# PCJ5.4: N recovered by the truncated logarithm, in C[t]/(t^m)
ok = True
qp = sp.symbols('q_p', positive=True)
for m in range(1, 7):
    Nm = shift_power(m, 1)
    E1 = sp.zeros(m, m)
    for j in range(m):
        E1 += (qp * Nm) ** j / sp.factorial(j)
    X = E1 - sp.eye(m)
    L = sp.zeros(m, m)
    for j in range(1, m):
        L += sp.Rational((-1) ** (j + 1), j) * X ** j
    if not sp.simplify(L / qp - Nm).is_zero_matrix:
        ok = False
check("PCJ5.4: N = (1/q_p) sum_{j<m} (-1)^{j+1}/j (e^{q_p N} - 1)^j for m <= 6", ok)

# PCJ5.6: ||pi(A_k) 1|| >= (k q_p)^{m-1}/(m-1)! on the critical line
ok = True
for m in range(2, 6):
    for k in [1, 5, 20, 100]:
        qv = mp.log(2)
        vec = [(k * qv) ** j / mp.factorial(j) for j in range(m)]
        if mp.sqrt(sum(v ** 2 for v in vec)) < (k * qv) ** (m - 1) / mp.factorial(m - 1):
            ok = False
check("PCJ5.6 (illustration): the vector pi(A_k)1 = sum (k log 2)^j/j! t^j has norm >= its last entry (m = 2..5)", ok)

# PCJ10.7: T(a* a) = m (p^{1-sigma} - sqrt p)(p^sigma - sqrt p) < 0 for sigma != 1/2 and = 0 at 1/2
ok = True
for trial in range(500):
    pp = random.choice([2, 3, 5, 7, 11, 13])
    sig = random.uniform(0.01, 0.99)
    if abs(sig - 0.5) < 1e-6:
        continue
    val = (pp ** (1 - sig) - mp.sqrt(pp)) * (pp ** sig - mp.sqrt(pp))
    if not val < 0:
        ok = False
check("PCJ10.7: (p^{1-sigma} - sqrt p)(p^sigma - sqrt p) < 0 for sigma != 1/2 (500 random)", ok)

# PCJ10.2 / 10.4: trace m h(rho) = residue of h zeta'/zeta at a zero (first zero, h = sum c_r r^s)
rho1 = mp.zetazero(1)
cs = {Fraction(2): mp.mpf(0.7), Fraction(1, 3): mp.mpf(-1.3), Fraction(5, 2): mp.mpf(0.2)}
hfun_num = lambda s: sum(c * mp.power(mp.mpf(rr.numerator) / rr.denominator, s) for rr, c in cs.items())
eps = mp.mpf('0.1')
res = mp.quad(lambda th: hfun_num(rho1 + eps * mp.expj(th)) * mp.zeta(rho1 + eps * mp.expj(th), derivative=1)
              / mp.zeta(rho1 + eps * mp.expj(th)) * 1j * eps * mp.expj(th), [0, 2 * mp.pi]) / (2j * mp.pi)
res2 = mp.quad(lambda th: hfun_num(rho1 + eps * mp.expj(th)) * 2 * mp.zeta(rho1 + eps * mp.expj(th), derivative=1)
               / mp.zeta(rho1 + eps * mp.expj(th)) * 1j * eps * mp.expj(th), [0, 2 * mp.pi]) / (2j * mp.pi)
check("PCJ10.4: residue of h f'/f at the first zero is m h(rho), for f = zeta (m = 1) and f = zeta^2 (m = 2)",
      abs(res - hfun_num(rho1)) < 1e-15 and abs(res2 - 2 * hfun_num(rho1)) < 1e-15,
      (mp.nstr(abs(res - hfun_num(rho1)), 3), mp.nstr(abs(res2 - 2 * hfun_num(rho1)), 3)))

# ---------------------------------------------------------------- Part E: integral Bost-Connes comparison
def e_add(u, v):
    w = dict(u)
    for k, c in v.items():
        w[k] = w.get(k, 0) + c
        if w[k] == 0:
            del w[k]
    return w


def scal(c, u):
    return {k: c * v for k, v in u.items()} if c else {}


def sigma(nn, u):
    out = {}
    for k, c in u.items():
        out = e_add(out, {(k * nn) % 1: c})
    return out


def rho_t(nn, u):
    out = {}
    for k, c in u.items():
        for j in range(nn):
            out = e_add(out, {((k + j) / nn) % 1: c})
    return out


def mult(u, v):
    out = {}
    for k1, c1 in u.items():
        for k2, c2 in v.items():
            out = e_add(out, {(k1 + k2) % 1: c1 * c2})
    return out


def rand_elem():
    return {Fraction(random.randint(0, 11), random.choice([1, 2, 3, 4, 6, 12])) % 1: random.randint(-3, 3) for _ in range(3)}


ok = True
for trial in range(300):
    bb, cc = random.randint(1, 12), random.randint(1, 12)
    dd = gcd(bb, cc)
    u = {k: v for k, v in rand_elem().items() if v}
    lhs = sigma(cc, rho_t(bb, u))
    rhs = scal(dd, rho_t(bb // dd, sigma(cc // dd, u)))
    if lhs != rhs:
        ok = False
check("CCM Prop 4.4 relation sigma_c rho~_b = (b,c) rho~_{b'} sigma_{c'} on Z[Q/Z] (300 random cases)", ok)

ok = True
for nn in range(2, 8):
    u = {Fraction(1, 3): 2, Fraction(0): 1}
    pi_n = {Fraction(j, nn): 1 for j in range(nn)}
    if sigma(nn, rho_t(nn, u)) != scal(nn, u):
        ok = False
    if rho_t(nn, sigma(nn, u)) != mult(pi_n, u):
        ok = False
    if rho_t(nn, sigma(nn, {Fraction(0): 1})) == {Fraction(0): nn}:
        ok = False  # V_n F_n = n would hold on e(0); it must fail
check("integral BC: sigma_n rho~_n = n, but rho~_n sigma_n = multiplication by pi_n != n (n = 2..7)", ok)

print()
print("ALL PASS" if all(RESULTS) else "SOME CHECKS FAILED", f"({sum(RESULTS)}/{len(RESULTS)})")
