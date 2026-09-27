#!/usr/bin/env python3
"""Checks for note 21_ (cross-programme bridges, part 1).

claude-ab, model claude-opus-5-5 (Opus 5.5, maximum reasoning effort), 25 September 2026.
Independent code: nothing here is taken from the programmes' own checkers.

 A. Navier-Stokes auxiliary torus -> Erdos-Straus (erdos-straus-foundation, ns_operator_bridge/):
    A1 J v = lambda v for the source eigen-directions; A2 the intertwining multiplier v.((J^m)^T n) = lambda^m v.n;
    A3 image/kernel of J mod N (T2), N = 1..60, by brute force; A4 the aliasing core of (T12):
    {(u,v) in G^2 : u^3 v = u v^5 = 1} = {(u,u^-3) : u^14 = 1} for G = U(R), R <= 300;
    A5 the shell example p = 13, a = 4, R = 3 of (T14)-(T16) with explicit characters;
    A6 (T15) with explicit characters on a non-cyclic group U(15) = <2> x <14>;
    A7 the sharp irrational-direction constant (S1)-(S4) by exhaustive search and the Pell sequence.
 B. Navier-Stokes profile -> Yang-Mills (yang-mills-interacting-workbench, released_profile_measures_addendum.tex):
    B1 curvature of A_i = lambda u_i T and -2 tr sum_{i<j} F_ij^2 = lambda^2 |curl u|^2 (sympy);
    B2 C_{R,t} ~ 9/(4 pi^4 t^8) and 72/(pi^4 t^9 C_{R,t}) -> 32/t;
    B3 the support bound |hhat(k)| >= H/2 for |k| <= 1/(2R) on an explicit bump;
    B4 the integrability exponents of (254)-(255).
 C. Erdos-Straus -> Fable quartic (es-fable-zeta-bridge-20260920):
    C1 the coefficients of H_ES, p = -5 u4/u3 and the quartic relation, symbolically on the ES variety;
    C2 the witness (13; 4, 18, 468); C3 the reciprocal quartic H_rec and its roots; C4 det DP = -2 for the map P of (EZ4).
 D. Mellin abscissa of a terminal power singularity (note 21_, Proposition 21.6), on a model.
 E. Split-zero heat comparison -> Yang-Mills Grams (RH_HEAT_TRANSFER.md, T1-T7): the relative-column-error Gram sandwich
    and its heat-semigroup instance (1-eps)^2 G <= G_T <= G, on random positive matrices.
 F. The Jacobian polynomial ("Fable/Jacobi", attributed in the YM workbench to L. Alpoge, 20 July 2026): det DF = -2 and the
    three points with image (-1/4, 0, 0).
"""
import math, os, itertools
import numpy as np
import sympy as sp
import mpmath as mp

out = []
def say(s=""):
    print(s); out.append(s)

# ---------------- A ----------------
r2 = sp.sqrt(2)
J = sp.Matrix([[3, 1], [1, 5]])
vr = sp.Matrix([1, 1 - r2]); vt = sp.Matrix([r2 - 1, 1])
lr, lt = 4 - r2, 4 + r2
say("A1 det J = %s ; J v_r - (4-sqrt2) v_r = %s ; J v_t - (4+sqrt2) v_t = %s"
    % (J.det(), sp.simplify(J * vr - lr * vr).T, sp.simplify(J * vt - lt * vt).T))
ok = True
rng = np.random.default_rng(1)
for m in range(0, 5):
    Jm = J ** m
    for _ in range(20):
        n = sp.Matrix(rng.integers(-9, 10, size=2).tolist())
        for v, l in [(vr, lr), (vt, lt)]:
            lhs = (v.T * (Jm.T * n))[0]
            rhs = l ** m * (v.T * n)[0]
            if sp.simplify(lhs - rhs) != 0:
                ok = False
say("A2 v.((J^m)^T n) = lambda^m v.n for m = 0..4 and 20 random n each: %s" % ok)

ok = True
for N in range(1, 61):
    g = math.gcd(N, 14)
    img = set(); ker = 0
    for x in range(N):
        for y in range(N):
            a, b = (3 * x + y) % N, (x + 5 * y) % N
            img.add((a, b))
            if a == 0 and b == 0:
                ker += 1
    pred = {(a, b) for a in range(N) for b in range(N) if (5 * a - b) % g == 0}
    if not (ker == g and len(img) == N * N // g and img == pred):
        ok = False; say("  A3 mismatch at N=%d" % N)
say("A3 J mod N, N = 1..60: kernel size gcd(N,14), image = {(a,b): gcd(N,14) | 5a-b}, |image| = N^2/gcd: %s" % ok)

ok = True; checked = 0
for R in range(2, 301):
    G = [u for u in range(1, R) if math.gcd(u, R) == 1]
    inv = {u: pow(u, -1, R) for u in G}
    sol = {(u, v) for u in G for v in G if (u ** 3 * v) % R == 1 and (u * v ** 5) % R == 1}
    pred = {(u, pow(inv[u], 3, R)) for u in G if pow(u, 14, R) == 1}
    checked += 1
    if sol != pred:
        ok = False; say("  A4 mismatch at R=%d" % R)
say("A4 {(u,v): u^3 v = u v^5 = 1} = {(u, u^-3): u^14 = 1} in U(R), R = 2..300 (%d groups): %s" % (checked, ok))

def characters_cyclic_product(R, gens_orders):
    """Characters of U(R) given an explicit decomposition into cyclic factors <g_i> of orders n_i.
    Returns (elements as exponent tuples -> residue map, list of characters as dicts residue -> complex)."""
    elems = {}
    for exps in itertools.product(*[range(n) for (_, n) in gens_orders]):
        r = 1
        for (g, n), e in zip(gens_orders, exps):
            r = (r * pow(g, e, R)) % R
        elems[r] = exps
    assert len(elems) == math.prod(n for _, n in gens_orders)
    chars = []
    for ks in itertools.product(*[range(n) for (_, n) in gens_orders]):
        chi = {r: complex(np.exp(2j * np.pi * sum(k * e / n for k, e, (_, n) in zip(ks, exps, gens_orders))))
               for r, exps in elems.items()}
        chars.append(chi)
    return elems, chars

def packet_coeffs(a, R):
    fac = sp.factorint(a)
    box = list(itertools.product(*[range(2 * e + 1) for e in fac.values()]))
    c = {}
    for e in box:
        u = 1
        for (l, _), k in zip(fac.items(), e):
            u *= l ** k
        c[u % R] = c.get(u % R, 0) + 1
    return c, fac, box

def F(chi, a_fac, R, g):
    val = chi[pow(g, -1, R)]
    for l, v in a_fac.items():
        val *= sum(chi[pow(l, e, R)] for e in range(2 * v + 1))
    return val

def mul(chi, psi, i, j, R):
    return {r: chi[r] ** i * psi[r] ** j for r in chi}

# A5: p = 13, h = 1, a = 4, R = 3
p, a = 13, 4; R = 4 * a - p
elems, chars = characters_cyclic_product(R, [(2, 2)])
c, fac, box = packet_coeffs(a, R)
g_t = (-pow(4, -1, R)) % R; g_t2 = (-a) % R
T14 = sum(F(ch, fac, R, g_t) for ch in chars).real / len(chars)
T15 = sum(F(mul(ch, ps, 3, 1, R), fac, R, g_t) * F(mul(ch, ps, 1, 5, R), fac, R, g_t2)
          for ch in chars for ps in chars).real / len(chars) ** 2
J2 = J ** 2
d2 = math.gcd(int(J2[0, 0]), int(J2[0, 1]))
T16 = sum(F(mul(ch, ps, int(J2[0, 0]), int(J2[0, 1]), R), fac, R, g_t) for ch in chars for ps in chars).real / len(chars) ** 2
say("A5 shell p=13, a=4, R=3: c(1)=%d, c(2)=%d; targets -4^-1 = %d, -a = %d; (T14) mean = %.6f; (T15) joint mean = %.6f (independent product c(2)c(2) = %d); J^2 = %s, d_2 = %d, (T16) mean = %.6f"
    % (c.get(1, 0), c.get(2, 0), g_t, g_t2, T14, T15, c.get(2, 0) ** 2, J2.tolist(), d2, T16))

# A6: U(15) = <2> (order 4) x <14> (order 2); packets a = 13 and b = 11 (p = 37 = 12*3+1, a in [10, 27], R = 4*13-37 = 15)
p, a, b = 37, 13, 11; R = 4 * a - p
elems, chars = characters_cyclic_product(R, [(2, 4), (14, 2)])
ca, faca, _ = packet_coeffs(a, R); cb, facb, _ = packet_coeffs(b, R)
G = sorted(elems)
res = []
for g_t in [1, 2, 4, 7]:
    for h_t in [1, 8, 13]:
        lhs = sum(F(mul(ch, ps, 3, 1, R), faca, R, g_t) * F(mul(ch, ps, 1, 5, R), facb, R, h_t)
                  for ch in chars for ps in chars).real / len(chars) ** 2
        rhs = sum(ca.get((g_t * u) % R, 0) * cb.get((h_t * pow(pow(u, 3, R), -1, R)) % R, 0)
                  for u in G if pow(u, 14, R) == 1)
        res.append(abs(lhs - rhs))
say("A6 U(15) non-cyclic, packets a=13, b=11, 12 target pairs: max |(T15) character mean - aliasing sum| = %.2e" % max(res))

c_ = mp.sqrt(4 + 2 * mp.sqrt(2))
mp.mp.dps = 60
for name, v in [("v_r", (mp.mpf(1), 1 - mp.sqrt(2))), ("v_t", (mp.sqrt(2) - 1, mp.mpf(1)))]:
    vf = (float(v[0]), float(v[1]))
    M = 1500
    m_ = np.arange(-M, M + 1)
    cands = []
    for n in range(-M, M + 1):
        vals = np.abs(vf[0] * m_ + vf[1] * n) * np.sqrt(m_ ** 2 + n ** 2)
        if n == 0:
            vals[M] = np.inf
        for jj in np.nonzero(vals < float(1 / c_) + 1e-6)[0]:
            cands.append((int(m_[jj]), n))
    # double precision cannot order these candidates (excesses ~1e-13); recompute them at 60 digits
    exact = sorted(((abs(v[0] * a_ + v[1] * b_) * mp.sqrt(a_ * a_ + b_ * b_) - 1 / c_, (a_, b_)) for (a_, b_) in cands), key=lambda t: t[0])
    say("A7 %s: %d candidates within 1e-6 of 1/c in |k|_inf <= %d, recomputed at 60 digits; exact minimiser %s with excess %s over 1/c = %s; all excesses > 0: %s"
        % (name, len(cands), M, exact[0][1], mp.nstr(exact[0][0], 4), mp.nstr(1 / c_, 12), all(e > 0 for e, _ in exact)))
mp.mp.dps = 30
alpha = 1 + mp.sqrt(2); d_ = mp.sqrt(4 - 2 * mp.sqrt(2))
pj, qj = 1, 0
vals = []
for j in range(1, 13):
    pj, qj = pj + 2 * qj, pj + qj
    k = (pj - qj, qj)
    val = abs(1 * k[0] + (1 - mp.sqrt(2)) * k[1]) * mp.sqrt(k[0] ** 2 + k[1] ** 2)
    pred = mp.sqrt(1 / c_ ** 2 + alpha ** (-4 * j) / d_ ** 2)
    vals.append((j, k, float(val), float(abs(val - pred))))
say("A7 Pell vectors k_{r,j} = (p_j - q_j, q_j): j, k, |v_r.k||k|, |value - sqrt(1/c^2 + alpha^{-4j}/d^2)|:")
for t in vals[::3]:
    say("    %s" % (t,))
m, n = sp.symbols('m n', integer=True)
wr = sp.Matrix([1, 1 + r2]); wt = sp.Matrix([-1 - r2, 1]); kk = sp.Matrix([m, n])
say("A7 (S2): (v_r.k)(w_r.k) - (m^2+2mn-n^2) = %s ; (v_t.k)(w_t.k) - (n^2-2mn-m^2) = %s"
    % (sp.expand((vr.T * kk)[0] * (wr.T * kk)[0] - (m ** 2 + 2 * m * n - n ** 2)),
       sp.expand((vt.T * kk)[0] * (wt.T * kk)[0] - (n ** 2 - 2 * m * n - m ** 2))))

# ---------------- B ----------------
x, y, z, lam = sp.symbols('x y z lambda', real=True)
u = [sp.Function('u%d' % i)(x, y, z) for i in range(3)]
X = [x, y, z]
T = -sp.I * sp.Matrix([[1, 0], [0, -1]]) / 2
A = [lam * u[i] * T for i in range(3)]
tot = 0
maxcomm = 0
for i in range(3):
    for j in range(i + 1, 3):
        Fij = sp.diff(A[j], X[i]) - sp.diff(A[i], X[j]) + (A[i] * A[j] - A[j] * A[i])
        maxcomm = max(maxcomm, int((A[i] * A[j] - A[j] * A[i]).is_zero_matrix is not True))
        tot += -2 * (Fij * Fij).trace()
curl = [sp.diff(u[2], y) - sp.diff(u[1], z), sp.diff(u[0], z) - sp.diff(u[2], x), sp.diff(u[1], x) - sp.diff(u[0], y)]
say("B1 -2 tr(T^2) = %s ; commutators vanish: %s ; -2 sum_{i<j} tr F_ij^2 - lambda^2 |curl u|^2 = %s"
    % (sp.simplify(-2 * (T * T).trace()), maxcomm == 0, sp.simplify(sp.expand(tot - lam ** 2 * sum(cc ** 2 for cc in curl)))))
mp.mp.dps = 30
for t in [10, 100, 1000, 10000]:
    Rr = 1
    C = mp.mpf(1) / (1280 * mp.pi ** 5 * t) * 4 * mp.pi * mp.quad(lambda r: r ** 6 * mp.e ** (-t * r), [0, 1 / (2 * Rr)])
    ratio = 72 / (mp.pi ** 4 * t ** 9) / C
    say("B2 R=1, t=%5d: C_{R,t} * 4 pi^4 t^8 / 9 = %.8f ; 72/(pi^4 t^9 C_{R,t}) * t/32 = %.8f"
        % (t, float(C * 4 * mp.pi ** 4 * t ** 8 / 9), float(ratio * t / 32)))
# B3: h(x) = (1-|x|^2)^2 on the unit ball, R = 1: hhat(k) = 4 pi int_0^1 h(r) r^2 sin(kr)/(kr) dr
H = 4 * mp.pi * mp.quad(lambda r: (1 - r * r) ** 2 * r * r, [0, 1])
worst = min(4 * mp.pi * mp.quad(lambda r: (1 - r * r) ** 2 * r * r * (mp.sin(k * r) / (k * r)), [0, 1]) / H
            for k in [mp.mpf(i) / 40 for i in range(1, 21)])
say("B3 bump (1-|x|^2)^2 on the unit ball: min over 0 < |k| <= 1/2 of hhat(k)/H = %.6f (claimed >= 1/2; the proof gives >= 1 - |k|R >= 1/2)" % float(worst))
hh = sp.symbols('h', positive=True)
say("B4 exponents in (254): magnetic -1/2-3h > -1 iff h < 1/6: %s ; electric -3/2-3h > -1 for no h >= 0: %s"
    % (sp.solve_univariate_inequality(-sp.Rational(1, 2) - 3 * hh > -1, hh), sp.solve_univariate_inequality(-sp.Rational(3, 2) - 3 * hh > -1, hh)))

# ---------------- C ----------------
x, y, z, U, V = sp.symbols('x y z U V')
p = 4 * x * y * z / (x * y + x * z + y * z)          # the ES relation 4/p = 1/x + 1/y + 1/z, solved for p
S = p + x + y + z
H_ES = sp.expand(-(U - p * V) * (U - x * V) * (U - y * V) * (U - z * V) / S)
Pz = sp.Poly(sp.together(H_ES * S).expand(), U, V)
coef = lambda i: sp.simplify(sp.Poly(H_ES, U, V).coeff_monomial(U ** (4 - i) * V ** i))
u0, u1, u2, u3, u4 = [coef(i) for i in range(5)]
checks = [sp.simplify(u0 + 1 / S), sp.simplify(u1 - 1), sp.simplify(u2 + (p * (x + y + z) + x * y + x * z + y * z) / S),
          sp.simplify(u3 - 5 * x * y * z / S), sp.simplify(u4 + p * x * y * z / S), sp.simplify(-5 * u4 / u3 - p),
          sp.simplify(625 * u0 * u4 ** 3 - 125 * u3 * u4 ** 2 + 25 * u2 * u3 ** 2 * u4 - 4 * u3 ** 4)]
say("C1 on 4/p = 1/x+1/y+1/z: u0+1/S, u1-1, u2+e2/S, u3-5xyz/S, u4+pxyz/S, -5u4/u3-p, quartic relation: %s" % checks)
pv, xv, yv, zv = 13, 4, 18, 468
say("C2 witness (13; 4, 18, 468): 4/13 - (1/4+1/18+1/468) = %s ; distinct roots: %s"
    % (sp.Rational(4, 13) - (sp.Rational(1, 4) + sp.Rational(1, 18) + sp.Rational(1, 468)), len({pv, xv, yv, zv}) == 4))
H_rec = sp.factor(sp.simplify((1 / u4) * V / (U - V) * H_ES.subs({U: p * V, V: U}, simultaneous=True)))
target = -V * (p * V - x * U) * (p * V - y * U) * (p * V - z * U) / (x * y * z)
say("C3 H_rec = u4^-1 V/(U-V) H_ES(pV, U) equals -V(pV-xU)(pV-yU)(pV-zU)/(xyz): %s (roots U/V = p/x, p/y, p/z and V = 0)"
    % (sp.simplify(H_rec - target) == 0))

aa, y0, z0, w0 = sp.symbols('a y0 z0 w0')
Ii = sp.I
P0 = aa**3*z0 + 2*aa**2*y0 - Ii*aa
P2 = -aa**3*y0**2*z0 - 2*Ii*aa**2*y0*z0 + aa**2*w0 - 2*aa**2*y0**3 - 10*Ii*aa*y0**2 + 3*aa*z0 + y0
P3 = 2*aa**3*y0**3*z0 + 6*Ii*aa**2*y0**2*z0 + 2*aa**2*w0*y0 + 4*aa**2*y0**4 + 2*Ii*aa*w0 - 4*Ii*aa*y0**3 - 2*aa*y0*z0 + 2*Ii*z0 + 7*y0**2
P4 = 2*aa**3*y0**4*z0 + 8*Ii*aa**2*y0**3*z0 + aa**2*w0*y0**2 + 4*aa**2*y0**5 + 2*Ii*aa*w0*y0 + 7*Ii*aa*y0**4 - 10*aa*y0**2*z0 - 4*Ii*y0*z0 - w0 - 3*y0**3
say("C4 the crosswalk's four-dimensional map P = (P0, P2, P3, P4) of (EZ4): det DP = %s" % sp.simplify(sp.Matrix([P0, P2, P3, P4]).jacobian([aa, y0, z0, w0]).det()))

# ---------------- D ----------------
alpha_, s_ = mp.mpf('0.53'), None
f = lambda t: t ** (-alpha_) + t ** (-mp.mpf('0.2'))
for sig in [mp.mpf('0.40'), mp.mpf('0.53'), mp.mpf('0.60'), mp.mpf('1.0')]:
    vals = [mp.quad(lambda t: f(t) * t ** (sig - 1), [mp.mpf(10) ** (-k), 1]) for k in (4, 8, 16)]
    say("D model f(t) = t^-0.53 + t^-0.2 on (0,1]: sigma = %.2f, int_{eps}^1 f t^(sigma-1) dt at eps = 1e-4, 1e-8, 1e-16: %s"
        % (float(sig), [round(float(v), 4) for v in vals]))

# ---------------- E ----------------
rng0 = np.random.default_rng(11)
worst = 0.0
for trial in range(200):
    d1, d2 = 4, 3
    M_ = rng0.normal(size=(d1 + d2, d1 + d2)) + 1j * rng0.normal(size=(d1 + d2, d1 + d2))
    Gm = M_.conj().T @ M_ + 0.05 * np.eye(d1 + d2)
    Ab, Cb, Sb = Gm[:d1, :d1], Gm[:d1, d1:], Gm[d1:, d1:]
    Hs = Ab - Cb @ np.linalg.inv(Sb) @ Cb.conj().T
    def msqrt_inv(Mx):
        ev, Q = np.linalg.eigh(Mx); return (Q * ev ** -0.5) @ Q.conj().T
    cN2 = 1 + np.linalg.norm(msqrt_inv(Hs) @ Cb @ msqrt_inv(Sb), 2) ** 2
    P = np.zeros_like(Gm); P[d1:, d1:] = Sb
    lam_max = np.linalg.eigvalsh(msqrt_inv(Gm) @ P @ msqrt_inv(Gm)).max()
    worst = max(worst, abs(lam_max - cN2) / cN2)
say("E0 (HM10)/(HM13) Schur-complement constant: max relative |lambda_max(G^-1/2 diag(0,S) G^-1/2) - (1 + ||H^-1/2 C S^-1/2||^2)| over 200 random Grams = %.2e" % worst)
rng = np.random.default_rng(7)
worst_lo = worst_hi = 1e9
for trial in range(200):
    n, k = 12, 5
    Phi = rng.normal(size=(n, k)) + 1j * rng.normal(size=(n, k))
    delta = rng.uniform(0.01, 0.6)
    Dl = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
    Dl = Dl / np.linalg.norm(Dl, 2) * delta          # ||Dl|| = delta, so ||Dl Phi x|| <= delta ||Phi x||
    PhiJ = Phi + Dl @ Phi
    G = Phi.conj().T @ Phi; GJ = PhiJ.conj().T @ PhiJ
    lo = np.linalg.eigvalsh(GJ - (1 - delta) ** 2 * G).min(); hi = np.linalg.eigvalsh((1 + delta) ** 2 * G - GJ).min()
    worst_lo = min(worst_lo, lo); worst_hi = min(worst_hi, hi)
Phi0 = rng.normal(size=(6, 3)); G0 = Phi0.T @ Phi0
say("E1' for delta > 1 the lower bound fails: Phi_J = 0 satisfies ||(Phi_J - Phi)x|| <= 2 ||Phi x||, but (1-2)^2 G <= 0 is false (min eigenvalue of 0 - G = %.3f)" % np.linalg.eigvalsh(-G0).max())
say("E1 relative column error ||(Phi_J - Phi)x|| <= delta ||Phi x|| => (1-delta)^2 G <= G_J <= (1+delta)^2 G: min eigenvalues over 200 trials %.2e, %.2e (>= 0 up to rounding)" % (worst_lo, worst_hi))
worst = [1e9, 1e9, 1e9, 1e9]
for trial in range(200):
    n, k = 10, 4
    Q, _ = np.linalg.qr(rng.normal(size=(n, n)))
    a0 = rng.uniform(0.5, 3.0)
    ev = a0 + rng.exponential(2.0, size=n); ev[0] = a0
    A = (Q * ev) @ Q.T
    Phi = rng.normal(size=(n, k))
    T_ = rng.uniform(0.05, 2.0)
    CT = Q @ np.diag(1 - np.exp(-T_ * ev)) @ Q.T
    eps = np.exp(-T_ * a0)
    G2 = Phi.T @ Phi; E = Phi.T @ A @ Phi
    PhiT = CT @ Phi; G2T = PhiT.T @ PhiT; ET = PhiT.T @ A @ PhiT
    vals = [np.linalg.eigvalsh(G2T - (1 - eps) ** 2 * G2).min(), np.linalg.eigvalsh(G2 - G2T).min(),
            np.linalg.eigvalsh(ET - (1 - eps) ** 2 * E).min(), np.linalg.eigvalsh(E - ET).min()]
    worst = [min(w, v) for w, v in zip(worst, vals)]
say("E2 C_T = I - exp(-TA), A >= a0 > 0, eps = exp(-T a0): (1-eps)^2 G2 <= G2_T <= G2 and (1-eps)^2 E <= E_T <= E; min eigenvalues over 200 trials: %s"
    % ["%.2e" % w for w in worst])

# ---------------- F ----------------
x, y, w = sp.symbols('x y w')
F1 = (1 + x * y) ** 3 * w + y ** 2 * (1 + x * y) * (4 + 3 * x * y)
F2 = y + 3 * x * (1 + x * y) ** 2 * w + 3 * x * y ** 2 * (4 + 3 * x * y)
F3 = 2 * x - 3 * x ** 2 * y - x ** 3 * w
Fm = sp.Matrix([F1, F2, F3])
detDF = sp.simplify(Fm.jacobian([x, y, w]).det())
pts = [(0, 0, sp.Rational(-1, 4)), (1, sp.Rational(-3, 2), sp.Rational(13, 2)), (-1, sp.Rational(3, 2), sp.Rational(13, 2))]
imgs = [tuple(Fm.subs({x: P[0], y: P[1], w: P[2]})) for P in pts]
say("F det DF = %s ; images of (0,0,-1/4), (1,-3/2,13/2), (-1,3/2,13/2): %s" % (detDF, imgs))
lm = sp.symbols('lambda_', nonzero=True)
sym = [sp.simplify(Fm[0].subs({x: lm * x, y: y / lm, w: w / lm ** 2}, simultaneous=True) - Fm[0] / lm ** 2),
       sp.simplify(Fm[1].subs({x: lm * x, y: y / lm, w: w / lm ** 2}, simultaneous=True) - Fm[1] / lm),
       sp.simplify(Fm[2].subs({x: lm * x, y: y / lm, w: w / lm ** 2}, simultaneous=True) - lm * Fm[2])]
say("F symmetry F(lambda x, y/lambda, w/lambda^2) - (F1/lambda^2, F2/lambda, lambda F3) = %s" % sym)

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "cross_programme_bridges_part1_checks_OUTPUT.txt"), "w") as fh:
    fh.write("\n".join(out) + "\n")
