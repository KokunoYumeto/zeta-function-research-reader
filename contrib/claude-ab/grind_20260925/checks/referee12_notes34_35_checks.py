#!/usr/bin/env python3
"""Checks for the twelfth referee pass on notes 34_ (proof of YM Theorem 14.2) and 35_ (DW).

Claude (claude-ab lane), model claude-opus-5-5 (Opus 5.5) at maximum reasoning effort,
25 September 2026.  Adapted from the referee's scratch script (32 items, of which 4 were
expected failures documenting findings); here every item tests the corrected statement,
so every item should PASS.

Part A (note 34_): the regulator identities, the proved windows for Q_2 and Q_10 with
outward rounding, the box side and the two scale limits, the cubic commutator term.
Part B (note 35_): the hash of DW against ETR0's record, DW7.6-DW9 on explicit models,
the full solution set of F N F^-1 = p^-1 N on a Jordan block, the GJN relations,
the geometric-Frobenius convention, the Jordan-string vector, and the weight bookkeeping
of Weil II (1.6.14) and (1.7.5) as printed.

Item B1 reads two programme files.  Set PROGRAMME_SOURCE_DIR to the folder that contains
AMPLIFICATION_AND_GLOBAL_EULER_PRODUCT.md and EULER_TENSOR_INTAKE_INDEPENDENT_REVIEW.md;
if they are absent, B1 is reported as SKIPPED.
"""
import hashlib, itertools, math, os, re
import numpy as np
import sympy as sp
import mpmath as mp

RESULTS = []


def report(tag, title, ok, detail=""):
    ok = None if ok is None else bool(ok)
    RESULTS.append((tag, ok))
    status = "SKIPPED" if ok is None else ("PASS" if ok else "FAIL")
    print(f"[{tag}] {status} | {title}")
    if detail:
        for line in str(detail).split("\n"):
            print(f"       {line}")


mp.mp.dps = 50
PI = mp.pi

# ============================ Part A: note 34_ ============================
j = sp.symbols('j', positive=True, integer=True)
Lj, aj, Nj = j**2, 1 / (100 * j), 2 * j**2 + 1
sigj = 2 * sp.sqrt(2) * sp.sin(sp.pi / (2 * Nj))
Dj = 2 * sigj / aj
okA1 = sp.simplify(Dj - 400 * sp.sqrt(2) * j * sp.sin(sp.pi / (4 * j**2 + 2))) == 0
report("A1", "Delta_j = 2 sigma_j/a_j = 400 sqrt2 j sin(pi/(4j^2+2)) for L_j = j^2, a_j = 1/(100j), N_j = 2L_j+1", okA1)

ratio = lambda x: (4 * x**2 / (4 * x**2 + 2)) * (mp.sin(PI / (4 * x**2 + 2)) / (PI / (4 * x**2 + 2)))
worst = max(ratio(mp.mpf(x)) for x in list(range(1, 2001)) + [10**4, 10**5, 10**6])
report("A2", "j Delta_j/(100 sqrt2 pi) = [4j^2/(4j^2+2)]*[sin x/x] < 1 (both factors < 1); numerically for j <= 2000 and 1e4..1e6",
       worst < 1, f"max ratio = {mp.nstr(worst, 16)}")

defi = lambda x: 1 - ratio(mp.mpf(x))
c4 = -(mp.mpf(1) / 4 - PI**2 / 96)
okA3 = abs(defi(10**4) * 2 * 10**8 - 1) < 1e-8 and abs((defi(10**4) - mp.mpf(1) / (2 * 10**8)) * 10**16 - c4) < 1e-6
report("A3", "relative deficit of j Delta_j = 1/(2j^2) - (1/4 - pi^2/96)/j^4 + O(j^-6)", okA3,
       f"deficit at j=2: {mp.nstr(defi(2), 8)} (1/(2j^2) = 0.125); next coefficient {mp.nstr(c4, 8)}")

Dnum = lambda x: 400 * mp.sqrt(2) * x * mp.sin(PI / (4 * x**2 + 2))
win = {x: (Dnum(mp.mpf(x)) * (1 - mp.mpf(1) / (10 * x)), Dnum(mp.mpf(x)) * (1 + mp.mpf(1) / (10 * x))) for x in (2, 10)}
outward = {2: (mp.mpf('186.637'), mp.mpf('206.284')), 10: (mp.mpf('43.765'), mp.mpf('44.650'))}
first_version = {2: (mp.mpf('186.64'), mp.mpf('206.28')), 10: (mp.mpf('43.77'), mp.mpf('44.65'))}
encl = all(outward[x][0] <= win[x][0] and outward[x][1] >= win[x][1] for x in (2, 10))
inward = [(x, e) for x in (2, 10) for e, (pv, wv) in enumerate(zip(first_version[x], win[x])) if (e == 0 and pv > wv) or (e == 1 and pv < wv)]
report("A4", "proved windows Delta_j(1 +- 1/(10j)) for j = 2, 10; the corrected intervals (rounded outward) enclose them; "
       "three of the four ends printed in the first version were rounded inward", encl and len(inward) == 3,
       "\n".join(f"j={x}: ({mp.nstr(win[x][0], 10)}, {mp.nstr(win[x][1], 10)})" for x in (2, 10)))

ell = 2 * Lj * aj
okA5 = (sp.simplify(ell - j / 50) == 0 and sp.simplify(Lj * aj - j / 100) == 0
        and sp.simplify(sp.limit(Dj * ell, j, sp.oo) - 2 * sp.sqrt(2) * sp.pi) == 0
        and sp.simplify(sp.limit(Dj / (2 * sp.pi / ell), j, sp.oo) - sp.sqrt(2)) == 0)
report("A5", "half-side L_j a_j = j/100, side l_j = j/50; Delta_j l_j -> 2 sqrt2 pi = %.6f; Delta_j/(2pi/l_j) -> sqrt2" % (2 * math.sqrt(2) * math.pi), okA5)

sig = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]], complex)]


def expsu2(x):
    n = np.linalg.norm(x)
    if n == 0:
        return np.eye(2, dtype=complex)
    return math.cos(n / 2) * np.eye(2) - 1j * math.sin(n / 2) * sum(x[a] / n * sig[a] for a in range(3))


rng = np.random.default_rng(12)
okA6, lines = True, []
for trial in range(3):
    ys = [sg * rng.normal(size=3) for sg in (1, 1, -1, -1)]      # U_p = Z1 Z2 Z3^-1 Z4^-1
    tot = sum(ys)
    pred = 0.25 * sum(np.dot(ys[k], np.cross(ys[i], ys[l])) for i in range(4) for l in range(i + 1, 4) for k in range(4) if k not in (i, l))
    vals = []
    for eps in (1e-2, 5e-3, 2.5e-3):
        U = np.eye(2, dtype=complex)
        for y in ys:
            U = U @ expsu2(eps * y)
        vals.append(((2 - np.trace(U).real) - 0.25 * eps**2 * np.dot(tot, tot)) / eps**3)
    extrap = 2 * vals[2] - vals[1]
    okA6 &= abs(extrap - pred) < 1e-3 * max(1, abs(pred)) and abs(pred) > 1e-3
    lines.append(f"trial {trial}: extrapolated cubic coefficient {extrap:.5f}, predicted {pred:.5f}")
report("A6", "plaquette term 2 - tr U_p = (1/4)|sum y|^2 + cubic commutator term (nonzero for >= 3 chord edges)", okA6, "\n".join(lines))

# ============================ Part B: note 35_ ============================
src = os.environ.get("PROGRAMME_SOURCE_DIR", "quantum_tau_programme_bridge_20260924/next_edition_after_719")
dwf = os.path.join(src, "AMPLIFICATION_AND_GLOBAL_EULER_PRODUCT.md")
etrf = os.path.join(src, "EULER_TENSOR_INTAKE_INDEPENDENT_REVIEW.md")
if os.path.exists(dwf) and os.path.exists(etrf):
    raw = open(dwf, 'rb').read()
    act = hashlib.sha256(raw).hexdigest()
    rec = re.search(r'1bc4b572[0-9a-f]*', open(etrf, encoding='utf-8').read()).group(0)
    fixed = [rec[:i] + rec[i + 1:] for i in range(len(rec)) if rec[:i] + rec[i + 1:] == act]
    okB1 = raw.count(b'\n') == 578 and act.endswith('39faaa6f') and len(rec) == 65 and len(fixed) > 0
    report("B1", "DW: 578 lines, SHA-256 1bc4b572...39faaa6f; ETR0 records a 65-digit string; deleting one character from it gives DW's hash",
           okB1, f"DW sha256 = {act}\nETR0 record = {rec}")
else:
    report("B1", "DW hash against ETR0's record (source files not available)", None)

mp.mp.dps = 45
beta, gam, m = mp.mpf('0.73'), mp.mpf('17.9'), 3
orbit = [mp.mpc(beta, gam), mp.mpc(beta, -gam), mp.mpc(1 - beta, -gam), mp.mpc(1 - beta, gam)]


def Wfull(p):
    n = 4 * m
    Wm = mp.matrix(n, n)
    lp = mp.log(p)
    for b, om in enumerate(orbit):
        for x in range(m):
            for y in range(x + 1):          # p^om * exp((log p) N), N eps^j = eps^{j+1}
                Wm[b * m + x, b * m + y] = mp.exp(om * lp) * lp**(x - y) / mp.factorial(x - y)
    return Wm


worst, worst_im = mp.mpf(0), mp.mpf(0)
for p in (2, 3, 7):
    Wm = Wfull(p)
    Wr = mp.eye(4 * m)
    for r in range(1, 6):
        Wr = Wr * Wm
        trv = sum(Wr[i, i] for i in range(4 * m))
        form = 2 * m * (mp.power(p, r * beta) + mp.power(p, r * (1 - beta))) * mp.cos(r * gam * mp.log(p))
        worst = max(worst, abs(trv - form) / abs(form))
        worst_im = max(worst_im, abs(mp.im(trv)))
report("B2", "DW7.6: tr(W_p^r | V_rho) = 2m(p^{r beta} + p^{r(1-beta)}) cos(r gamma log p), real (beta = 0.73, gamma = 17.9, m = 3; p = 2, 3, 7; r <= 5)",
       worst < mp.mpf(10)**-38 and worst_im < mp.mpf(10)**-30, f"max relative error {mp.nstr(worst, 3)}")

mp.mp.dps = 40
okB3 = True
for p in (2, 5):
    for k in (1, 2):
        Tp = lambda r: 2 * m * (mp.power(p, r * beta) + mp.power(p, r * (1 - beta))) * mp.cos(r * gam * mp.log(p))
        c = [mp.mpf(1)]
        for n in range(1, 13):
            c.append(sum(Tp(r)**(2 * k) * c[n - r] for r in range(1, n + 1)) / n)
        okB3 &= all(mp.re(x) >= 0 and abs(mp.im(x)) < 1e-25 for x in c)
        if k == 1:
            poly = [mp.mpc(1)] + [mp.mpc(0)] * 12
            for w1 in orbit:
                for w2 in orbit:
                    z = mp.power(p, w1 + w2)
                    ser = [mp.binomial(m * m + n - 1, n) * z**n for n in range(13)]
                    poly = [sum(poly[a] * ser[n - a] for a in range(n + 1)) for n in range(13)]
            okB3 &= max(abs(poly[n] - c[n]) / max(abs(c[n]), 1) for n in range(13)) < mp.mpf(10)**-25
report("B3", "DW7.7 and DW8.3: the local factor of the 2k-th tensor power has nonnegative coefficients and equals the product over ordered tuples", okB3)

okB4, lines = True, []
for k in range(1, 7):
    cnt = sum(1 for tup in itertools.product(range(4), repeat=2 * k)
              if tup.count(2) == 0 and tup.count(3) == 0 and tup.count(0) == tup.count(1))
    okB4 &= cnt == math.comb(2 * k, k)
mp.mp.dps = 30
b0, g0 = mp.mpf('0.7'), mp.mpf('5.3')
orb = [mp.mpc(b0, g0), mp.mpc(b0, -g0), mp.mpc(1 - b0, -g0), mp.mpc(1 - b0, g0)]
s1 = 1 + 2 * b0
sig2 = [w1 + w2 for w1 in orb for w2 in orb]
others = mp.mpf(1)
for sg in sig2:
    if abs(sg - 2 * b0) > 1e-20:
        others *= mp.zeta(s1 - sg)
e = mp.mpf('1e-12')
Lval = mp.mpf(1)
for sg in sig2:
    Lval *= mp.zeta(s1 + e - sg)
okB4 &= abs(e**2 * Lval - others) / abs(others) < 1e-9 and mp.re(others) > 0 and abs(mp.im(others)) < 1e-20
report("B4", "DW8.5-8.6: s_k = 1 + 2kB has C(2k,k) contributing tuples (k <= 6), so order m^{2k} C(2k,k); for m = k = 1 the pole is genuine",
       okB4, f"m = k = 1, beta = 0.7, gamma = 5.3: eps^2 L_1(s_1 + eps) -> {mp.nstr(others, 12)} (product of the other 14 factors)")

kk, B = sp.symbols('k B', positive=True)
report("B5", "DW8.11: s_k - (k+1) = k(2B - 1)", sp.expand((1 + 2 * kk * B) - (kk + 1) - kk * (2 * B - 1)) == 0)

mp.mp.dps = 45
okB6 = True
for p in (2, 3, 11):
    dv = mp.det(Wfull(p))
    okB6 &= abs(dv - mp.power(p, 2 * m)) / mp.power(p, 2 * m) < mp.mpf(10)**-35
report("B6", "DW8.12 (35.N1): det(W_p | V_rho) = p^{2m}, so the average weight is 1 for every beta", okB6)

pp, cr, rho = sp.symbols('p c rho', positive=True)
okB7 = True
for mm in range(1, 8):
    Nm = sp.zeros(mm)
    for a in range(1, mm):
        Nm[a, a - 1] = 1
    Wm = cr * sum((((sp.log(pp))**q / sp.factorial(q)) * Nm**q for q in range(mm)), sp.zeros(mm))
    okB7 &= sp.simplify(Wm * Nm * Wm.inv() - Nm) == sp.zeros(mm)
    Cp = Wm * Nm - Nm * Wm / pp
    okB7 &= sp.simplify(Cp - (1 - 1 / pp) * Wm * Nm) == sp.zeros(mm) and Cp.subs({pp: 7, cr: sp.Rational(3, 2)}).rank() == mm - 1
mm = 6
Nm = sp.zeros(mm)
for a in range(1, mm):
    Nm[a, a - 1] = 1
Fp = lambda x: x**rho * sp.diag(*[x**(-q) for q in range(mm)])
okB7 &= sp.simplify(Fp(pp) * Nm * Fp(pp).inv() - Nm / pp) == sp.zeros(mm)
aa, bb = sp.symbols('a b', positive=True)
okB7 &= sp.simplify(sp.powsimp(Fp(aa) * Fp(bb) - Fp(aa * bb), force=True)) == sp.zeros(mm)
report("B7", "DW9: W_p N W_p^-1 = N; the defect W_p N - p^-1 N W_p = (1 - p^-1) W_p N has rank m - 1; F = p^rho S_p satisfies F N F^-1 = p^-1 N and F_a F_b = F_ab", okB7)

mm = 4
Nm = sp.zeros(mm)
for a in range(1, mm):
    Nm[a, a - 1] = 1
X = sp.Matrix(mm, mm, sp.symbols('x0:%d' % (mm * mm)))
sol = sp.solve(list(X * Nm - Nm * X / pp), list(X), dict=True)[0]
Xs = X.subs(sol)
free = sorted(Xs.free_symbols - {pp}, key=str)
Sp = sp.diag(*[pp**(-q) for q in range(mm)])
cs = sp.symbols('c0:%d' % mm)
U = sum((cs[q] * Nm**q for q in range(mm)), sp.zeros(mm))
eqs = list(Xs - Sp * U)
solc = sp.solve(eqs, list(cs), dict=True)
okB8 = (len(free) == mm and len(solc) == 1 and all(sp.simplify(q.subs(solc[0])) == 0 for q in eqs)
        and [sp.simplify(Xs[q, q] / Xs[0, 0]) for q in range(mm)] == [pp**(-q) for q in range(mm)])
report("B8", "every F with F N = p^-1 N F on one Jordan block is S_p u(N), u a polynomial in N; its eigenvalues are u(0) p^-j (the weight shift -2j is forced)", okB8)

u_, lam, a_, b_ = sp.symbols('u lambda a b', positive=True)
hh = sp.Function('h')
H = lambda l, q: hh(u_) * u_**(-l) * sp.log(u_)**q / sp.factorial(q)
Pa = lambda f, a: hh(u_) / hh(u_**a) * f.subs(u_, u_**a)
Cb = lambda f, b: hh(u_) / hh(u_ / b) * f.subs(u_, u_ / b)
okB9 = True
for q in range(4):
    lhs = sp.expand_log(sp.powsimp(Pa(H(lam, q), a_), force=True), force=True)
    okB9 &= sp.simplify(sp.expand(lhs - a_**q * H(a_ * lam, q))) == 0
    lhs = sp.expand(sp.expand_log(Cb(H(lam, q), b_), force=True))
    rhs = sp.expand(b_**lam * sum((-sp.log(b_))**(q - l) / sp.factorial(q - l) * H(lam, l) for l in range(q + 1)))
    okB9 &= sp.simplify(sp.powsimp(lhs - rhs, force=True)) == 0
bv, dim = 3, 9
idx = {(e, q): 3 * e + q for e in range(3) for q in range(3)}
Nmat, Pmat = sp.zeros(dim), sp.zeros(dim)
for (e, q), i in idx.items():
    if q >= 1:
        Nmat[idx[(e, q - 1)], i] = 1
    if e + 1 < 3:
        Pmat[idx[(e + 1, q)], i] = bv**q
dom = [idx[(e, q)] for e in (0, 1) for q in range(3)]
img = [idx[(e, q)] for e in (1, 2) for q in range(3)]
okB9 &= sp.simplify((Nmat * Pmat)[:, dom] - (bv * Pmat * Nmat)[:, dom]) == sp.zeros(dim, len(dom))
Pr = Pmat[img, dom]
okB9 &= sp.simplify(Pr * Nmat[dom, dom] * Pr.inv() - Nmat[img, img] / bv) == sp.zeros(6)
report("B9", "GJN2.2, GJN5.2 from the germ definitions; N P_b = b P_b N (GJN4.4), hence P_b N P_b^-1 = b^-1 N on the image of P_b", okB9)

q_, t_, al = sp.symbols('q t alpha', positive=True)
N2 = sp.Matrix([[0, 0], [1, 0]])
F2 = sp.diag(al, al / q_)
okB10 = (sp.simplify(F2 * N2 * F2.inv() - N2 / q_) == sp.zeros(2)
         and sp.simplify(F2 * sp.exp(t_ * N2) * F2.inv() - sp.exp(t_ * N2 / q_)) == sp.zeros(2)
         and sp.simplify(F2.inv() * N2 * F2 - q_ * N2) == sp.zeros(2))
report("B10", "geometric Frobenius: F N F^-1 = q^-1 N, equivalently F exp(tN) F^-1 = exp(q^-1 t N); arithmetic Frobenius gives q N", okB10)

okB11 = True
Qs, als = sp.symbols('Q alpha', positive=True)
for jn in range(8):
    n = jn + 1
    Ns = sp.zeros(n)
    for r in range(1, n):
        Ns[r - 1, r] = 1
    NN = sp.kronecker_product(Ns, sp.eye(n)) + sp.kronecker_product(sp.eye(n), Ns)
    Om = sp.zeros(n * n, 1)
    for r in range(n):
        Om[r * n + (jn - r)] = (-1)**r
    Fs = sp.diag(*[Qs**r * als for r in range(n)])
    okB11 &= NN * Om == sp.zeros(n * n, 1)
    okB11 &= sp.simplify(sp.kronecker_product(Fs, Fs) * Om - als**2 * Qs**jn * Om) == sp.zeros(n * n, 1)
report("B11", "the Jordan-string vector sum (-1)^r v_r (x) v_{j-r} is killed by N(x)1 + 1(x)N and has eigenvalue alpha^2 Q^j (j <= 7)", okB11)

ii, jv, j1, j2, kv = sp.symbols('i j j1 j2 k')
wt = lambda base, twist: base - 2 * twist            # the twist (k) has weight -2k (Weil II p. 170)
okB12 = (sp.simplify(wt(ii + kv, kv) - (ii - kv)) == 0                         # (1.6.14.1)
         and sp.simplify(wt(-j1 - j2, (jv - j1 - j2) / 2) - (-jv)) == 0        # (1.6.14.4)
         and sp.simplify(wt(jv, jv) - (-jv)) == 0                              # (1.6.14.5)
         and sp.simplify(wt(-jv, (ii + jv) / 2) - ii) != 0                     # (1.6.14.3) as printed: not isobaric
         and sp.simplify(wt(-jv, -(ii + jv) / 2) - ii) == 0)                   # with the negative twist: isobaric
report("B12", "Weil II p. 170: (1.6.14.1), (1.6.14.4), (1.6.14.5) are isobaric; (1.6.14.3) as printed is not, and becomes isobaric with the twist -(i+j)/2", okB12,
       f"weight defect of the printed (1.6.14.3): {sp.simplify(wt(-jv, (ii + jv) / 2) - ii)}")

wts = {w: sp.Symbol('V%d' % w) for w in range(-3, 4)}
Mstrict = lambda i: [w for w in wts if w < i]
Mweak = lambda i: [w for w in wts if w <= i]
gr = lambda M, i: sorted(set(M(i)) - set(M(i - 1)))
okB13 = all(gr(Mstrict, i) == [i - 1] for i in range(-2, 4)) and all(gr(Mweak, i) == [i] for i in range(-2, 4))
report("B13", "Weil II p. 171, proof of (1.7.5): M'_i = sum over j < i gives Gr_i = V'_{i-1} (weight i - 1); j <= i gives weight i", okB13)

print()
npass = sum(1 for _, o in RESULTS if o is True)
nskip = sum(1 for _, o in RESULTS if o is None)
print(f"SUMMARY: {npass}/{len(RESULTS)} PASS" + (f", {nskip} SKIPPED" if nskip else "")
      + ("" if all(o is not False for _, o in RESULTS) else "; FAIL: " + ", ".join(t for t, o in RESULTS if o is False)))
