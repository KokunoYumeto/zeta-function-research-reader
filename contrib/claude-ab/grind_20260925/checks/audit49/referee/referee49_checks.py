#!/usr/bin/env python3
"""Referee checks for note 49_ (independent of audit49_checks.py).

Each item prints PASS/FAIL (or INFO for an illustration) with the compared quantities.
Run: python3 referee49_checks.py
"""
import random
from fractions import Fraction
from math import gcd

import mpmath as mp
import numpy as np
import sympy as sp
from scipy.special import loggamma

random.seed(4949)
mp.mp.dps = 30
RES = []


def report(label, name, ok, detail=""):
    RES.append(ok)
    print(("PASS " if ok else "FAIL ") + label + " " + name + (("  [" + str(detail) + "]") if detail != "" else ""), flush=True)


def info(label, name, detail):
    print("INFO " + label + " " + name + "  [" + str(detail) + "]", flush=True)


# ============================================================ R-A: TPL
def left_null(M):
    ns = M.T.nullspace()
    if not ns:
        return sp.zeros(0, M.rows)
    return sp.Matrix.hstack(*ns).T


def colspace_basis(M):
    cs = M.columnspace()
    if not cs:
        return sp.zeros(M.rows, 0)
    return sp.Matrix.hstack(*cs)


def rk(M):
    return 0 if (M.rows == 0 or M.cols == 0) else M.rank()


def rand_mat(r, c):
    return sp.Matrix(r, c, lambda i, j: random.randint(-2, 2))


ok = True
fails = []
ntested = 0
for trial in range(60):
    dB, dp, dm = random.randint(1, 5), random.randint(0, 5), random.randint(0, 5)
    rp = rand_mat(dB, dp) if dp else sp.zeros(dB, 0)
    rm = rand_mat(dB, dm) if dm else sp.zeros(dB, 0)
    # force degeneracies in a third of the cases
    if dp and trial % 3 == 0:
        rp = rp * sp.diag(*([0] * min(2, dp) + [1] * (dp - min(2, dp))))
    if dm and trial % 3 == 1 and dp:
        rm = rp[:, :min(dp, dm)].row_join(sp.zeros(dB, dm - min(dp, dm))) if dm >= 1 else rm
    dA = dp + dm
    d = rp.row_join(-rm)                                   # Cech d(a+,a-) = r+a+ - r-a-
    H0 = sp.Matrix.hstack(*d.nullspace()) if (dA and d.nullspace()) else sp.zeros(dA, 0)
    # K0 = ker r+ (+) ker r-, embedded in A+ (+) A-
    kp = rp.nullspace() if dp else []
    km = rm.nullspace() if dm else []
    Kcols = [v.col_join(sp.zeros(dm, 1)) for v in kp] + [sp.zeros(dp, 1).col_join(v) for v in km]
    K = sp.Matrix.hstack(*Kcols) if Kcols else sp.zeros(dA, 0)
    # res(a+,a-) = r+ a+
    resA = rp.row_join(sp.zeros(dB, dm))                   # on ambient A+ (+) A-
    # costalk quotients B/r+A+, B/r-A- via left-null-space coordinates
    Lp, Lm = left_null(rp) if dp else sp.eye(dB), left_null(rm) if dm else sp.eye(dB)
    delta = (-Lp).col_join(-Lm)                            # delta(b) = ([-b],[-b])
    Mq = left_null(rp.row_join(rm)) if dA else sp.eye(dB)  # H^1 coordinates: B/(r+A+ + r-A-)
    Sp = Lp.T * (Lp * Lp.T).inv() if Lp.rows else sp.zeros(dB, 0)
    Sm = Lm.T * (Lm * Lm.T).inv() if Lm.rows else sp.zeros(dB, 0)
    q = (-Mq * Sp).row_join(Mq * Sm)                        # q([v+],[v-]) = [v- - v+]
    # well-definedness of q on classes: M r+ = M r- = 0
    good = (Mq * rp).is_zero_matrix if dp else True
    good = good and ((Mq * rm).is_zero_matrix if dm else True)
    # exactness: 0 -> K0 -> H0 -> B -> C -> H1 -> 0
    dimK0, dimH0 = K.cols, H0.cols
    dimC, dimH1 = delta.rows, Mq.rows
    inj = rk(K) == dimK0
    K_in_H0 = (d * K).is_zero_matrix if dimK0 else True
    resH0 = resA * H0 if dimH0 else sp.zeros(dB, 0)
    ex_H0 = (resA * K).is_zero_matrix if dimK0 else True
    ex_H0 = ex_H0 and (dimH0 - rk(resH0) == dimK0)
    ex_B = ((delta * resH0).is_zero_matrix if dimH0 else True) and (dB - rk(delta) == rk(resH0))
    ex_C = (q * delta).is_zero_matrix and (dimC - rk(q) == rk(delta))
    surj = rk(q) == dimH1
    # ker delta = r+A+ ∩ r-A-  (dimension, and the image of res lies in both images)
    inter = rk(rp) + rk(rm) - rk(rp.row_join(rm)) if dA else 0
    kerdelta_ok = (dB - rk(delta)) == inter
    ntested += 1
    if not all([good, inj, K_in_H0, ex_H0, ex_B, ex_C, surj, kerdelta_ok]):
        ok = False
        fails.append((trial, good, inj, K_in_H0, ex_H0, ex_B, ex_C, surj, kerdelta_ok))
report("R-A1", "TPL5.3 exactness with the maps built explicitly (res, delta=([-b],[-b]), q=[v- - v+]) on %d random diagrams" % ntested, ok, fails[:2])

# R-A2: the audit's check A4 is an identity in the rank variables (vacuous)
dp_, dm_, dB_, rp_, rm_, rs_ = sp.symbols('dp dm dB rkp rkm rks')
dimK0 = (dp_ - rp_) + (dm_ - rm_)
dimH0 = dp_ + dm_ - rs_
alt = dimK0 - dimH0 + dB_ - ((dB_ - rp_) + (dB_ - rm_)) + (dB_ - rs_)
kerdelta = rp_ + rm_ - rs_
report("R-A2", "audit check A4 is vacuous: its alternating sum and its 'ker delta' test are identically 0 in the rank symbols",
       sp.expand(alt) == 0 and sp.expand(kerdelta - (dimH0 - dimK0)) == 0, (sp.expand(alt), sp.expand(kerdelta - (dimH0 - dimK0))))

# ============================================================ R-B: OZR, sharpness
# R-B1 Riemann-von Mangoldt main term
rows = []
okB1 = True
for T in [100, 500, 1000, 2000]:
    N = mp.nzeros(T)
    main = T / (2 * mp.pi) * mp.log(T / (2 * mp.pi * mp.e)) + mp.mpf(7) / 8
    rows.append((T, int(N), float(main)))
    if abs(N - main) > 2 * mp.log(T):
        okB1 = False
report("R-B1", "N(T) - (T/2pi)log(T/2pi e) - 7/8 is O(log T) at T = 100..2000 (sanity, not a proof)", okB1, rows)

# R-B2 Stirling on vertical lines for Gamma(s/2)
okB2 = True
errs = []
for xv in [-1.2, 0.5, 2.4]:
    for yv in [60.0, 300.0, 2000.0]:
        s = mp.mpc(xv, yv)
        lhs = mp.re(mp.loggamma(s / 2))
        rhs = (xv / 2 - mp.mpf(1) / 2) * mp.log(yv / 2) - mp.pi * yv / 4 + mp.log(2 * mp.pi) / 2
        errs.append(float(abs(lhs - rhs) * yv))
        if abs(lhs - rhs) > 1 / mp.mpf(yv):
            okB2 = False
report("R-B2", "Stirling: log|Gamma(s/2)| = ((x-1)/2)log(|y|/2) - pi|y|/4 + log(2pi)/2 + O(1/|y|)", okB2, "max |err|*|y| = %.3g" % max(errs))

# R-B3 the completed factor G = F0/zeta for the p = 2 test phi = eta(x)(1+y^2)^{-1}
u = sp.symbols('u')
f0 = sp.exp(-1 / u)
g = f0 / (f0 + f0.subs(u, 1 - u))
g2 = sp.lambdify(u, sp.diff(g, u, 2), 'numpy')
g0 = sp.lambdify(u, g, 'numpy')


def eta(xa):
    out = np.zeros_like(xa)
    left = (xa > -1.5) & (xa < -0.5)
    right = (xa > 1.5) & (xa < 2.5)
    mid = (xa >= -0.5) & (xa <= 1.5)
    with np.errstate(all='ignore'):
        out[left] = g0(xa[left] + 1.5)
        out[right] = g0(2.5 - xa[right])
    out[mid] = 1.0
    return np.nan_to_num(out)


def eta2(xa):
    out = np.zeros_like(xa)
    left = (xa > -1.5) & (xa < -0.5)
    right = (xa > 1.5) & (xa < 2.5)
    with np.errstate(all='ignore'):
        out[left] = g2(xa[left] + 1.5)
        out[right] = g2(2.5 - xa[right])
    return np.nan_to_num(out)


def theta(t):
    """smooth, =1 on |t|<=1, 0 for |t|>=2"""
    t = np.abs(t)
    out = np.ones_like(t)
    out[t >= 2] = 0.0
    tr = (t > 1) & (t < 2)
    with np.errstate(all='ignore'):
        out[tr] = np.nan_to_num(g0(2 - t[tr]))
    return out


hx = 0.005
xs = -1.5 + hx * (np.arange(800) + 0.5)
E, E2 = eta(xs), eta2(xs)


def logabsG(xg, yg):
    s = xg + 1j * yg
    return np.log(np.abs(s - 1)) - np.log(4.0) - xg / 2 * np.log(np.pi) + loggamma(1 + s / 2).real


def pieces(R, hy=0.01):
    """(1/2pi) int log|G| theta_R Lap(phi) over the plane, and int |log|G|| |Lap phi| over |y|<=2R."""
    Ys = hy * (np.arange(int(2 * R / hy)) + 0.5)
    I = 0.0
    Aabs = 0.0
    for chunk in np.array_split(Ys, max(1, len(Ys) // 2000)):
        X, Y = np.meshgrid(xs, chunk, indexing='ij')
        w = 1 / (1 + Y ** 2)
        w2 = (6 * Y ** 2 - 2) / (1 + Y ** 2) ** 3
        lap = E2[:, None] * w + E[:, None] * w2
        L = logabsG(X, Y)
        I += np.sum(L * theta(Y / R) * lap) * hx * hy
        Aabs += np.sum(np.abs(L) * np.abs(lap)) * hx * hy
    return 2 * I / (2 * np.pi), 2 * Aabs     # factor 2: the integrand is even in y


vals = []
for R in [5, 10, 20, 40, 80, 160]:
    Iv, Av = pieces(R)
    vals.append((R, round(Iv, 6), round(Av, 3)))
okB3 = abs(vals[-1][1] - 1.0) < 2e-3 and abs(vals[-2][1] - 1.0) < 2e-3 and (vals[-1][2] - vals[-2][2]) > 0.5 * (vals[-2][2] - vals[-3][2]) > 0
report("R-B3", "p=2 test: (1/2pi) int log|G| theta_R Lap(phi) -> phi(1) = 1, while int |log|G|| |Lap phi| grows like log R", okB3, vals)

# ============================================================ R-C: FT
n_ = sp.symbols('n', positive=True, integer=True)
A_, B_, q_ = sp.symbols('A B q', positive=True)


def lattice_matrix(lam, src, tgt):
    """integer matrix of w -> lam*w from lattice src (basis list) to lattice tgt (basis list):
    column j = coordinates of lam*src[j] in tgt basis (tgt basis (a, i b) orthogonal)."""
    cols = []
    for v in src:
        w = sp.expand(lam * v)
        re, im = sp.re(w), sp.im(w)
        cols.append([sp.simplify(re / sp.re(tgt[0])), sp.simplify(im / sp.im(tgt[1]))])
    return sp.Matrix(cols).T


okC1 = True
for nv in [2, 3, 6]:
    for qv in [sp.Rational(1), sp.Rational(3, 2)]:
        Aval, Bval = sp.log(5), 2 * sp.pi
        Lq = [qv * Aval, sp.I * Bval]
        Lnq = [nv * qv * Aval, sp.I * Bval]
        Mu = lattice_matrix(1, Lnq, Lq)          # u: E_nq -> E_q, w -> w
        Mv = lattice_matrix(nv, Lq, Lnq)         # v: E_q -> E_nq, w -> n w
        degu, degv = Mu.det(), Mv.det()
        Pu = [sp.Matrix([[1]]), Mu.T, sp.Matrix([[degu]])]                # pullback: H^0, H^1 = Hom(L,Z), H^2
        Su = [sp.Matrix([[degu]]), degu * (Mu.T).inv(), sp.Matrix([[1]])]  # transfer: tr o u^* = deg
        Pv = [sp.Matrix([[1]]), Mv.T, sp.Matrix([[degv]])]
        want_P = [sp.Matrix([[1]]), sp.diag(nv, 1), sp.Matrix([[nv]])]
        want_S = [sp.Matrix([[nv]]), sp.diag(1, nv), sp.Matrix([[1]])]
        want_v = [sp.Matrix([[1]]), sp.diag(1, nv), sp.Matrix([[nv]])]
        okC1 = okC1 and degu == nv and degv == nv
        okC1 = okC1 and all(Pu[i] == want_P[i] and Su[i] == want_S[i] and Pv[i] == want_v[i] for i in range(3))
        # u^* tr = sum over deck translations; translations act as identity on the lattice, hence on H^*
        okC1 = okC1 and all((Pu[i] * Su[i] - nv * sp.eye(Pu[i].rows)).is_zero_matrix for i in range(3))
report("R-C1", "FT6.7/6.8/6.10 derived from the lattice maps (pullback = M^T on Hom(L,Z), transfer = deg (M^T)^-1, top degree = deg)", okC1)

# R-C2 FT10 with the operator actually applied to z_N
okC2 = True
for nv in [2, 3, 5]:
    for N in [0, 2, 7]:
        lam = mp.sqrt(nv) * mp.expjpi(mp.mpf('0.31'))
        z = {Fraction(nv) ** k: lam ** (-k) for k in range(-N, N + 1)}
        Fz = {r * nv: c for r, c in z.items()}
        diff = dict(Fz)
        for r, c in z.items():
            diff[r] = diff.get(r, 0) - lam * c
        nz = sum(mp.mpf(r.numerator) / r.denominator * abs(c) ** 2 for r, c in z.items())          # / AB
        nd = sum(mp.mpf(r.numerator) / r.denominator * abs(c) ** 2 for r, c in diff.items() if abs(c) > 1e-25)
        okC2 = okC2 and abs(nz - (2 * N + 1)) < 1e-20 and abs(nd - 2 * nv) < 1e-20
report("R-C2", "FT10.8-10.10 with F_n applied to z_N: ||z_N||^2 = (2N+1)AB, ||(F_n - lambda)z_N||^2 = 2nAB", okC2)

# R-C3 every cohomological degree: normalised basis vectors are sent to sqrt(n) times normalised basis vectors
grams = lambda qq: [sp.Matrix([[qq * A_ * B_]]), sp.diag(B_ / (qq * A_), qq * A_ / B_), sp.Matrix([[1 / (qq * A_ * B_)]])]
P = [sp.Matrix([[1]]), sp.diag(n_, 1), sp.Matrix([[n_]])]
okC3 = True
for i in range(3):
    Gq, Gnq = grams(q_)[i], grams(n_ * q_)[i]
    for j in range(Gq.rows):
        e = sp.zeros(Gq.rows, 1); e[j] = 1
        img = P[i] * e
        ratio = sp.simplify((img.T * Gnq * img)[0] / (e.T * Gq * e)[0])
        single = sum(1 for k in range(img.rows) if img[k] != 0) == 1     # a basis vector goes to a multiple of a basis vector
        okC3 = okC3 and ratio == n_ and single
report("R-C3", "FT8: in degrees 0,1,2, F_n maps each orthonormalised basis vector at scale q to sqrt(n) times the one at scale nq (so FT10's circle |lambda| = sqrt n holds in every degree)", okC3)

# ============================================================ R-D: PCJ
# R-D1 PCJ10 trace on a jet block is the rho-block of the Weil form: T(a*a) = m h_a(rho) conj(h_a(rho^#))
t = sp.symbols('t')
okD1 = True
for trial in range(20):
    m = random.randint(1, 4)
    rho = sp.Rational(random.randint(1, 99), 100) + sp.I * sp.Rational(random.randint(-3000, 3000), 100)
    terms = {Fraction(random.randint(1, 12), random.randint(1, 12)): complex(random.randint(-3, 3), random.randint(-3, 3)) for _ in range(3)}

    def jet_matrix(coeffs, rho=rho, m=m):
        # multiplication by sum c_r r^{rho + t} mod t^m, basis 1, t, ..., t^{m-1}
        ser = 0
        for r, c in coeffs.items():
            rr = sp.Rational(r.numerator, r.denominator)
            ser += sp.nsimplify(c) * rr ** rho * sum((sp.log(rr) * t) ** j / sp.factorial(j) for j in range(m))
        ser = sp.expand(ser)
        M = sp.zeros(m, m)
        for j in range(m):
            coeff_j = ser.coeff(t, j) if j > 0 else ser.subs(t, 0)
            for k in range(m - j):
                M[k + j, k] = coeff_j
        return M
    a_star = {1 / r: complex(c).conjugate() * float(r) for r, c in terms.items()}      # (c b_r)^* = conj(c) r b_{1/r}
    Ta = (jet_matrix(a_star) * jet_matrix(terms)).trace()
    h = lambda s: sum(complex(c) * mp.power(mp.mpf(r.numerator) / r.denominator, s) for r, c in terms.items())
    rho_n = mp.mpc(float(sp.re(rho)), float(sp.im(rho)))
    rho_sharp = 1 - mp.conj(rho_n)
    want = m * h(rho_n) * mp.conj(h(rho_sharp))
    if abs(complex(sp.N(Ta, 30)) - complex(want)) > 1e-8 * max(1, abs(want)):
        okD1 = False
report("R-D1", "PCJ10: Tr pi(a*a) on J_m equals m h_a(rho) conj(h_a(rho^#)), the rho-block of RTT's W(h_a,h_a) (20 random a, rho, m<=4)", okD1)

# R-D2 residue trace with a genuine multiplicity: f = zeta^2 has a double zero at rho_1
rho1 = mp.zetazero(1)
cs = {Fraction(2): mp.mpf('0.7'), Fraction(1, 3): mp.mpf('-1.3'), Fraction(5, 2): mp.mpf('0.2')}
hn = lambda s: sum(c * mp.power(mp.mpf(r.numerator) / r.denominator, s) for r, c in cs.items())
eps = mp.mpf('0.1')
res2 = mp.quad(lambda th: hn(rho1 + eps * mp.expj(th)) * 2 * mp.zeta(rho1 + eps * mp.expj(th), derivative=1)
               / mp.zeta(rho1 + eps * mp.expj(th)) * 1j * eps * mp.expj(th), [0, 2 * mp.pi]) / (2j * mp.pi)
report("R-D2", "PCJ10.4 with multiplicity m = 2 (f = zeta^2): residue of h f'/f = 2 h(rho)", abs(res2 - 2 * hn(rho1)) < 1e-15, mp.nstr(abs(res2 - 2 * hn(rho1)), 3))

# R-D3 Bohr: the geometric norm of D = C_2 + C_3 - C_5 is sqrt2+sqrt3+sqrt5 (torus max, attained at z=(1,1,-1),
# which is not of the form (2^{ig},3^{ig},5^{ig})); the sup of |h_D(1/2+ig)| over the line approaches it (Kronecker).
target = float(np.sqrt(2) + np.sqrt(3) + np.sqrt(5))
out = []
for T in [1e2, 1e4, 1e6, 1e7]:
    gam = np.linspace(0, T, int(min(T * 40, 4e7)) + 1)
    v = np.abs(np.sqrt(2) * np.exp(1j * gam * np.log(2)) + np.sqrt(3) * np.exp(1j * gam * np.log(3))
               - np.sqrt(5) * np.exp(1j * gam * np.log(5)))
    out.append((T, round(target - float(v.max()), 6)))
info("R-D3", "Bohr/Kronecker illustration: (sqrt2+sqrt3+sqrt5) - max_{0<=g<=T} |2^{1/2+ig} + 3^{1/2+ig} - 5^{1/2+ig}|", out)

# ============================================================ R-E: Witt vectors
def witt_coords_of_integer(k, M):
    """Witt coordinates c_1..c_M (big Witt vectors, prod_n (1 - c_n t^n)^{-1} convention) of k*1 in W(Z)."""
    tt = sp.symbols('tt')
    f = sp.series((1 - tt) ** (-k), tt, 0, M + 1).removeO()
    f = sp.Poly(f, tt)
    coeffs = []
    for n in range(1, M + 1):
        c = f.coeff_monomial(tt ** n)
        coeffs.append(int(c))
        f = sp.Poly(sp.expand(f.as_expr() * (1 - c * tt ** n)), tt)
        f = sp.Poly(sum(f.coeff_monomial(tt ** j) * tt ** j for j in range(M + 1)), tt)
    return coeffs


okE1 = True
table = []
for p in [2, 3, 5, 7]:
    M = 3 * p + 2
    cp = witt_coords_of_integer(p, M)                      # coordinates of p*1
    vp1 = [1 if n == p else 0 for n in range(1, M + 1)]    # coordinates of V_p(1)
    for Nmod in range(2, 31):
        equal = all((cp[i] - vp1[i]) % Nmod == 0 for i in range(M))
        expected = (p % Nmod == 0)                          # p A = 0 in A = Z/N  iff  N | p
        if equal != expected:
            okE1 = False
            table.append((p, Nmod, equal))
report("R-E1", "V_p(1) = p in W(Z/N) (Witt coordinates up to degree 3p+2) exactly when N | p, i.e. when pA = 0 (p <= 7, N <= 30)", okE1, table[:4])

# R-E2 ghost components over Z and the characteristic-p identity (1 - t)^p = 1 - t^p
okE2 = True
tt = sp.symbols('tt')
for p in [2, 3, 5]:
    ghost_Vp1 = sp.series(tt * sp.diff(-sp.log(1 - tt ** p), tt), tt, 0, 4 * p).removeO()
    ghost_p = sp.series(tt * sp.diff(-p * sp.log(1 - tt), tt), tt, 0, 4 * p).removeO()
    gv = [ghost_Vp1.coeff(tt, n) for n in range(1, 4 * p)]
    gp = [ghost_p.coeff(tt, n) for n in range(1, 4 * p)]
    okE2 = okE2 and gv == [p if n % p == 0 else 0 for n in range(1, 4 * p)] and gp == [p] * (4 * p - 1)
    okE2 = okE2 and sp.Poly((1 - tt) ** p - (1 - tt ** p), tt, modulus=p).is_zero
    okE2 = okE2 and not sp.Poly((1 - tt) ** p - (1 - tt ** p), tt).is_zero
report("R-E2", "ghost(V_p 1) = (p at multiples of p, else 0), ghost(p) = (p,p,...); and (1-t)^p = 1-t^p holds mod p but not over Z", okE2)

# ============================================================ R-F: Lemma 49.2 sanity
# a(u) = exp(-u - 1/u) lies in A;  M0 a(s) = 2 K_s(2);  s M0 a = M0(-u d/du a) <=> K_{s+1}(2) - K_{s-1}(2) = s K_s(2)
okF = True
for s in [mp.mpc(0.3, 2.0), mp.mpc(-2.5, 7.0), mp.mpc(4.0, -11.0)]:
    direct = mp.quad(lambda uu: mp.exp(-uu - 1 / uu) * mp.power(uu, s - 1), [0, 1, 10, mp.inf])
    okF = okF and abs(direct - 2 * mp.besselk(s, 2)) < 1e-18
    lhs = s * 2 * mp.besselk(s, 2)
    rhs = mp.quad(lambda uu: (uu - 1 / uu) * mp.exp(-uu - 1 / uu) * mp.power(uu, s - 1), [0, 1, 10, mp.inf])
    okF = okF and abs(lhs - rhs) < 1e-18 * max(1, abs(lhs))
# uniform bound K(sigma) <= 2/(N - A0) for |sigma| <= A0 < N
for A0, N in [(0.5, 2), (2.3, 4), (5.0, 6)]:
    for sig in np.linspace(-A0, A0, 7):
        Kv = mp.quad(lambda uu: mp.power(uu, sig - 1) / (mp.power(uu, N) + mp.power(uu, -N)), [0, 1, mp.inf])
        okF = okF and Kv <= 2 / (N - A0) + 1e-20
report("R-F1", "Lemma 49.2 step 1: s M0 a = M0((-u d_u) a) (a = e^{-u-1/u}, M0 a = 2K_s(2)); K(sigma) <= 2/(N-A0) uniformly", okF)

# ============================================================ R-G: the relation ring W of Proposition 49.6
# normal form V_b F_c ; product (V_b1 F_c1)(V_b2 F_c2) = d V_{b1 b2/d} F_{c1 c2/d}, d = gcd(c1, b2)
def nf_mult(x, y):
    out = {}
    for (b1, c1), k1 in x.items():
        for (b2, c2), k2 in y.items():
            d = gcd(c1, b2)
            key = (b1 * (b2 // d), (c1 // d) * c2)
            out[key] = out.get(key, 0) + d * k1 * k2
    return {k: v for k, v in out.items() if v}


okG1 = True
for trial in range(300):
    X = [{(random.randint(1, 12), random.randint(1, 12)): random.randint(-3, 3)} for _ in range(3)]
    if nf_mult(nf_mult(X[0], X[1]), X[2]) != nf_mult(X[0], nf_mult(X[1], X[2])):
        okG1 = False
report("R-G1", "the normal-ordered product on symbols V_bF_c is associative (300 random triples), consistent with W free on {V_bF_c}", okG1)


def sigma(n, u):
    out = {}
    for k, c in u.items():
        key = (k * n) % 1
        out[key] = out.get(key, 0) + c
    return {k: v for k, v in out.items() if v}


def rho_t(n, u):
    out = {}
    for k, c in u.items():
        for j in range(n):
            key = ((k + j) / n) % 1
            out[key] = out.get(key, 0) + c
    return {k: v for k, v in out.items() if v}


pairs = [(b, c) for b in range(1, 7) for c in range(1, 7)]
inputs = [Fraction(0)] + [Fraction(j, Nn) for Nn in (7, 11, 12, 13, 60) for j in range(1, 6)]
cols = {}
rows = []
for (b, c) in pairs:
    vec = {}
    for idx, g0_ in enumerate(inputs):
        outv = rho_t(b, sigma(c, {g0_: 1}))
        for key, val in outv.items():
            vec[(idx, key)] = val
    rows.append(vec)
    for key in vec:
        cols.setdefault(key, len(cols))
Mbc = np.zeros((len(pairs), len(cols)))
for i, vec in enumerate(rows):
    for key, val in vec.items():
        Mbc[i, cols[key]] = val
rank_bc = np.linalg.matrix_rank(Mbc)
# ghost coordinates of W(Q): (F_n w)_m = w_{nm}, (V_n w)_m = n w_{m/n} if n | m else 0
Mdim = 400
def VF_on_basis(b, c, k):
    # V_b F_c e_k = b e_{bk/c} if c | k else 0   (derived: F_c e_k = e_{k/c} if c|k; V_b e_j = b e_{bj})
    return (b * k // c, b) if k % c == 0 else None
Mgh = np.zeros((len(pairs), Mdim * Mdim // 20))
colg = {}
for i, (b, c) in enumerate(pairs):
    for k in range(1, Mdim):
        r_ = VF_on_basis(b, c, k)
        if r_ is not None:
            key = (k, r_[0])
            colg.setdefault(key, len(colg))
            Mgh[i, colg[key]] = r_[1]
rank_gh = np.linalg.matrix_rank(Mgh[:, :len(colg)])
report("R-G2", "the 36 operators V_bF_c (b,c<=6) are linearly independent on Z[Q/Z] (as rho~_b sigma_c) and on ghost coordinates of W",
       rank_bc == len(pairs) and rank_gh == len(pairs), (rank_bc, rank_gh, len(pairs)))

# sanity of the ghost-coordinate formulas: F_n and V_n on ghosts reproduce F_n V_n = n and V_n F_n = mult. by ghost(V_n 1)
okG3 = True
for n in (2, 3, 6):
    w = {m: random.randint(-5, 5) for m in range(1, 200)}
    F = lambda n, w: {m: w[n * m] for m in w if n * m in w}
    V = lambda n, w: {m: (n * w[m // n] if m % n == 0 else 0) for m in w}
    FV = F(n, V(n, w))
    VF = V(n, F(n, w))
    okG3 = okG3 and all(FV[m] == n * w[m] for m in FV)
    okG3 = okG3 and all(VF[m] == (n * w[m] if m % n == 0 else 0) for m in VF if m * n < 200)
report("R-G3", "ghost-coordinate model: F_nV_n = n, V_nF_n = multiplication by ghost(V_n 1) = (n if n|m else 0)", okG3)

print()
print("ALL PASS" if all(RES) else "SOME CHECKS FAILED", "(%d/%d)" % (sum(RES), len(RES)))
