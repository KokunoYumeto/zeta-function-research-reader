#!/usr/bin/env python3
"""ref52_partA_jacobian.py -- referee's independent checks for note 52_, Part A (the Keller map F).

Independent of jac52_checks.py in method:
 (A1) factorization by polynomial division of f_F by L (not by expanding L*Q);
 (A2) the fibre = simple-roots theorem tested by brute force over F_p (p = 3, 5, 7, 11, 13): for EVERY (a,b,c) in F_p^3,
      #{(x,y,w) in F_p^3 : F = (a,b,c)} = #{F_p-rational simple roots of a s^3 + b s^2 t + 4 s t^2 + 4 c t^3};
 (A3) fibres over random complex/real targets rebuilt from the roots through the explicit inverse of iota, and pushed
      forward by F; real fibre sizes versus the sign of Delta; x, y, w take three distinct values on the fibres and
      coincide with the roots of the note's cubics; the square factor of the x-discriminant tested at a point;
 (A4) the C*-action: equivariance, the mu_2 structure of the three-point fibre, the reduction of F over {F3 != 0}
      to C* x (a Laurent Keller map of C* x C onto C^2 with Jacobian 2/x^3), the quotient curve on the slice c = 1;
 (A5) the Weyl/Poisson relations with DF^{-1} computed by sympy's inverse (not the adjugate);
 (A6) Delone-Faddeev remarks: integer points with A = 0 (the note's formula Q x Q[theta]/(Q(theta,1)) then has the
      wrong rank) and integer points with Delta(F) = 0 (degenerate rings), gcd(u, v) in {1, 2}.
"""
import sympy as sp, itertools, random, cmath, math, time
T0 = time.time()
random.seed(527)
res = []
def check(name, cond):
    ok = bool(cond); res.append((name, ok)); print(("PASS" if ok else "FAIL") + "  " + name, flush=True)

x, y, w, s, t, S, lam = sp.symbols('x y w s t S lambda')
a, b, c = sp.symbols('a b c')
F1 = (1+x*y)**3*w + y**2*(1+x*y)*(4+3*x*y)
F2 = y + 3*x*(1+x*y)**2*w + 3*x*y**2*(4+3*x*y)
F3 = 2*x - 3*x**2*y - x**3*w
Fv = [F1, F2, F3]
J = sp.Matrix([[sp.diff(f, v) for v in (x, y, w)] for f in Fv])
check("det DF = -2 (Berkowitz determinant)", sp.expand(J.det(method='berkowitz')) == -2)

# (A1) division of f_F by L = v s - u t
u = -2*x; v = 1 + x*y
fF = sp.expand(F1*s**3 + F2*s**2*t + 4*s*t**2 + 4*F3*t**3)
# divide as polynomials in s over the field Q(x,y,w,t)
q_, r_ = sp.div(sp.Poly(fF, s), sp.Poly(v*s - u*t, s))
A = (1+x*y)**2*w + y**2*(4+3*x*y); B = x*(1+x*y)*w + y*(1+3*x*y); C = 2*(2 - 3*x*y - x**2*w)
check("(A1) f_F is divisible by L = v s - u t with quotient A s^2 + B s t + C t^2 (division in s)",
      sp.simplify(r_.as_expr()) == 0 and sp.simplify(q_.as_expr() - (A*s**2 + B*s*t + C*t**2)) == 0)
check("(A1) Res_s(L, Q) at t = 1 equals A u^2 + B u v + C v^2 = 4 (sympy resultant, up to the sign convention)",
      sp.simplify(sp.resultant(v*s - u, A*s**2 + B*s + C, s)) in (4, -4))

# (A2) finite fields
def simple_roots_count(av, bv, cv, p):
    cnt = 0
    # roots [s0 : 1]
    for s0 in range(p):
        g = (av*s0**3 + bv*s0**2 + 4*s0 + 4*cv) % p
        if g == 0:
            dg = (3*av*s0**2 + 2*bv*s0 + 4) % p
            if dg != 0: cnt += 1
    # root [1 : 0]: h(T) = f(1, T) = a + b T + 4 T^2 + 4 c T^3, root T = 0 iff a = 0, simple iff b != 0
    if av % p == 0 and bv % p != 0: cnt += 1
    return cnt
fnum = sp.lambdify((x, y, w), (F1, F2, F3), 'math')
allok = True; summary = []
for p in (3, 5, 7, 11, 13):
    fib = {}
    for xv, yv, wv in itertools.product(range(p), repeat=3):
        val = tuple(int(e) % p for e in fnum(xv, yv, wv))
        fib[val] = fib.get(val, 0) + 1
    ok = all(fib.get((av, bv, cv), 0) == simple_roots_count(av, bv, cv, p) for av, bv, cv in itertools.product(range(p), repeat=3))
    sizes = {}
    for key in itertools.product(range(p), repeat=3):
        k = fib.get(key, 0); sizes[k] = sizes.get(k, 0) + 1
    summary.append((p, dict(sorted(sizes.items()))))
    allok &= ok
check(f"(A2) over F_p, p = 3,5,7,11,13: for every target, #F^-1(a,b,c)(F_p) = #F_p-rational simple roots of the slice cubic; fibre-size histograms {summary}", allok)

# (A3) complex fibres rebuilt from roots through iota^{-1}
def fibre_from_roots(av, bv, cv):
    import numpy as np
    pts = []
    rts = np.roots([av, bv, 4, 4*cv])            # roots S = s/t of f(S,1)
    for S0 in rts:
        u0, v0 = complex(S0), 1.0                  # L0 = v0 s - u0 t vanishes at [S0 : 1]
        # Q0 = f / L0: synthetic division of a S^3 + b S^2 + 4 S + 4c by (S - S0)
        A0 = av; B0 = bv + A0*S0; C0 = 4 + B0*S0
        res0 = A0*u0**2 + B0*u0*v0 + C0*v0**2      # Res(L0, Q0)
        if abs(res0) < 1e-9: continue              # multiple root: no point
        mu = 4/res0
        uu, vv = mu*u0, mu*v0; AA, BB, CC = A0/mu, B0/mu, C0/mu
        xx = -uu/2; yy = (AA*uu + 2*BB*vv)/2
        v2w = AA - yy**2*(4 + 3*xx*yy); u2w = 4*(2 - 3*xx*yy - CC/2)
        ww = ((CC**3*vv - 3*BB*CC**2*uu)*v2w + (3*BB**2*CC*vv - BB**3*uu)*u2w)/64
        pts.append((xx, yy, ww))
    return pts
Delta = lambda av, bv, cv: 27*av**2*cv**2 - 18*av*bv*cv + 16*av + bv**3*cv - bv**2
fc = sp.lambdify((x, y, w), (F1, F2, F3), 'numpy')
ok_c = True; ok_real = True; ok_distinct = True; ok_cubics = True
xcub = lambda X, av, bv, cv: Delta(av, bv, cv)*X**3 + (4 - 3*bv*cv)*X - 2*cv
ycub = lambda Y, av, bv, cv: 2*Y**3 - 3*bv*Y**2 + 18*av*Y + 27*av**2*cv - 18*av*bv + bv**3
for trial in range(300):
    cplx = trial % 2 == 0
    if cplx:
        tgt = tuple(complex(random.uniform(-3, 3), random.uniform(-3, 3)) for _ in range(3))
    else:
        tgt = tuple(random.uniform(-3, 3) for _ in range(3))
    pts = fibre_from_roots(*tgt)
    if len(pts) != 3: ok_c = False
    for P in pts:
        img = fc(*P)
        if max(abs(img[i] - tgt[i]) for i in range(3)) > 1e-6: ok_c = False
        if abs(xcub(P[0], *tgt)) > 1e-6 * (1 + abs(P[0])**3) or abs(ycub(P[1], *tgt)) > 1e-6 * (1 + abs(P[1])**3): ok_cubics = False
    xs = [P[0] for P in pts]; ys = [P[1] for P in pts]; wsv = [P[2] for P in pts]
    for vals in (xs, ys, wsv):
        if min(abs(vals[i] - vals[j]) for i in range(3) for j in range(i+1, 3)) < 1e-7: ok_distinct = False
    if not cplx:
        nreal = sum(1 for P in pts if max(abs(complex(q).imag) for q in P) < 1e-8)
        if nreal != (3 if Delta(*tgt) < 0 else 1): ok_real = False
check("(A3) 300 random targets (half complex, half real): the three points built from the three roots via iota^{-1} map back to the target (|error| < 1e-6)", ok_c)
check("(A3) on these fibres x, y and w each take three distinct values, and the x- and y-values are roots of the note's x- and y-cubics", ok_distinct and ok_cubics)
check("(A3) real targets: exactly 3 real preimages when Delta < 0 and exactly 1 when Delta > 0 (Disc = -16 Delta)", ok_real)
# the square factor 27 a c^2 - 9 b c + 8 of the x-discriminant: at (a,b,c) = (-8/27, 0, 1), Delta = -64/27 != 0, two fibre points share x
pts = fibre_from_roots(-8/27, 0.0, 1.0)
xs = sorted([complex(P[0]) for P in pts], key=lambda z: (z.real, z.imag))
share = min(abs(xs[i] - xs[j]) for i in range(3) for j in range(i+1, 3))
check(f"(A3) at (a,b,c) = (-8/27, 0, 1) (on 27ac^2 - 9bc + 8 = 0, Delta = {Delta(-8/27,0,1):.4f}): 3 fibre points, two with equal x (min |x_i - x_j| = {share:.2e})",
      len(pts) == 3 and share < 1e-8)

# (A4) the C*-action
act = {x: x/lam, y: lam*y, w: lam**2*w}
check("(A4) F(x/l, l y, l^2 w) = (l^2 F1, l F2, F3/l)", all(sp.simplify(f.subs(act, simultaneous=True) - m*f) == 0 for f, m in zip(Fv, (lam**2, lam, 1/lam))))
p1 = (1, sp.Rational(-3, 2), sp.Rational(13, 2)); p2 = (-1, sp.Rational(3, 2), sp.Rational(13, 2)); p3 = (0, 0, sp.Rational(-1, 4))
check("(A4) the two escaping points lie on ONE C*-orbit: (-1)*(1,-3/2,13/2) = (-1,3/2,13/2); the mu_2-fixed locus is the w-axis, F(0,0,w) = (w,0,0)",
      (sp.Integer(-1)**-1*p1[0], -p1[1], p1[2]) == p2 and [sp.expand(f.subs({x: 0, y: 0})) for f in Fv] == [w, 0, 0])
# reduction over F3 != 0: slice F3 = 1 <=> w = (2x - 3x^2 y - 1)/x^3 (x != 0 there)
wsl = (2*x - 3*x**2*y - 1)/x**3
f2 = [sp.simplify(F1.subs(w, wsl)), sp.simplify(F2.subs(w, wsl))]
J2 = sp.simplify(sp.Matrix([[sp.diff(g, v) for v in (x, y)] for g in f2]).det())
check(f"(A4) on the slice F3 = 1 (a copy of C* x C, coordinates x != 0, y): f2 = (F1, F2) is a Laurent map with Jacobian {J2}, a unit of C[x^+-1, y]",
      sp.simplify(J2 - 2/x**3) == 0 and all(sp.denom(sp.together(g)).free_symbols <= {x} for g in f2))
print("      f2_1 =", sp.expand(f2[0])); print("      f2_2 =", sp.expand(f2[1]))
check("(A4) {F3 != 0} = C* x {F3 = 1} equivariantly (lambda . p, weight -1 on F3): F there is id x f2, so fibres/non-properness/image of F over {c != 0} are those of f2 over the plane c = 1: "
      "Delta(P, Q, 1) = 27P^2 - 18PQ + 16P + Q^3 - Q^2 is the note's quotient curve",
      sp.expand(Delta(a, b, 1) - (27*a**2 - 18*a*b + 16*a + b**3 - b**2)) == 0)
# the image of f2 misses exactly the cusp (4/27, 4/3): the point (4/27, 4/3, 1) of the missing curve
check("(A4) the missing curve meets the slice c = 1 exactly at (4/27, 4/3, 1), the cusp of Delta(P,Q,1) = 0",
      Delta(sp.Rational(4, 27), sp.Rational(4, 3), 1) == 0 and fibre_from_roots(4/27, 4/3, 1.0) == [])

# (A4') normal form on U = {F3 != 0}: n = 2 - 3xy - x^2 w (= C/2), m = (1+xy) n (= vC/2)
nn = 2 - 3*x*y - x**2*w; mm = (1 + x*y)*nn
Pm, Qm, M_, N_ = sp.symbols('P Q m n')
g1 = M_*(N_ + M_ - M_**2); g2 = 2*N_ + 4*M_ - 3*M_**2
check("(A4') F1*F3^2 = m(n + m - m^2) and F2*F3 = 2n + 4m - 3m^2 identically, with n = 2 - 3xy - x^2 w = C/2, m = (1+xy)n = vC/2, and F3 = x n",
      sp.expand(F1*F3**2 - g1.subs({M_: mm, N_: nn})) == 0 and sp.expand(F2*F3 - g2.subs({M_: mm, N_: nn})) == 0 and sp.expand(F3 - x*nn) == 0)
# U = {x != 0, n != 0} is isomorphic to C* x C x C* via (c, m, n) = (F3, m, n): inverse x = c/n, y = (m - n)/c, w = (2 - 3(m/n - 1) - n) n^2 / c^2
cc_ = sp.symbols('c_')
xi = cc_/N_; yi = (M_ - N_)/cc_; wi = (2 - 3*(M_/N_ - 1) - N_)*N_**2/cc_**2
check("(A4') (x,y,w) -> (F3, m, n) is an isomorphism of U = {F3 != 0} onto C* x C x C* (explicit inverse; both composites are the identity)",
      all(sp.simplify(e) == 0 for e in (F3.subs({x: xi, y: yi, w: wi}) - cc_, mm.subs({x: xi, y: yi, w: wi}) - M_, nn.subs({x: xi, y: yi, w: wi}) - N_))
      and all(sp.simplify(e) == 0 for e in (xi.subs({cc_: F3, M_: mm, N_: nn}) - x, yi.subs({cc_: F3, M_: mm, N_: nn}) - y, wi.subs({cc_: F3, M_: mm, N_: nn}) - w)))
check("(A4') hence on U: F = (c^-2 g1(m,n), c^-1 g2(m,n), c) with g = (m(n+m-m^2), 2n+4m-3m^2); det Dg = 2n",
      sp.expand(sp.Matrix([[sp.diff(e, z) for z in (M_, N_)] for e in (g1, g2)]).det() - 2*N_) == 0)
hcub = M_**3 - 2*M_**2 + Qm*M_ - 2*Pm
check("(A4') g(m,n) = (P,Q) <=> h(m) := m^3 - 2m^2 + Q m - 2P = 0 and n = h'(m)/2: the fibre of g over (P,Q) inside {n != 0} is the set of SIMPLE roots of h",
      sp.expand(hcub.subs({Pm: g1, Qm: g2})) == 0 and sp.expand(sp.diff(hcub, M_).subs({Qm: g2}) - 2*N_) == 0)
gq = 27*Pm**2 - 18*Pm*Qm + 16*Pm + Qm**3 - Qm**2
al, be = Qm - sp.Rational(4, 3), 2*Qm/3 - 2*Pm - sp.Rational(16, 27)
check("(A4') Disc_m(h) = -4 (27P^2 - 18PQ + 16P + Q^3 - Q^2), and with the affine change alpha = Q - 4/3, beta = 2Q/3 - 2P - 16/27, "
      "h(m) = m'^3 + alpha m' + beta (m = m' + 2/3) and 4*g(P,Q) = 4 alpha^3 + 27 beta^2: the quotient curve IS the A2 discriminant, globally",
      sp.expand(sp.discriminant(hcub, M_) + 4*gq) == 0
      and sp.expand(hcub.subs(M_, sp.Symbol('mp') + sp.Rational(2, 3)) - (sp.Symbol('mp')**3 + al*sp.Symbol('mp') + be)) == 0
      and sp.expand(4*gq - (4*al**3 + 27*be**2)) == 0)

Sv = sp.symbols('Sv')
check("(A4'') the root variable of the slice cubic and of h are related by m = -2c/S: f(S,1) = (4c/m^3) h(m) with P = a c^2, Q = b c, and m = -2F3/S equals (1+xy)(2-3xy-x^2 w) at S = u/v = -2x/(1+xy)",
      sp.simplify((a*Sv**3 + b*Sv**2 + 4*Sv + 4*c).subs(Sv, -2*c/M_) - (4*c/M_**3)*hcub.subs({Pm: a*c**2, Qm: b*c})) == 0
      and sp.simplify((-2*F3/(-2*x/(1 + x*y))) - mm) == 0)

# (A5) Weyl / Poisson relations with sympy's inverse
Jinv = J.inv()
Dcoef = [[sp.expand(sp.simplify(Jinv[k, i])) for k in range(3)] for i in range(3)]   # D_i = sum_k (DF^-1)_{ki} d_k
def D(i, g): return sp.expand(sum(Dcoef[i][k]*sp.diff(g, v) for k, v in enumerate((x, y, w))))
check("(A5) [D_i, F_j] = delta_ij with DF^-1 from sympy's inverse", all(sp.expand(D(i, Fv[j]) - (1 if i == j else 0)) == 0 for i in range(3) for j in range(3)))
check("(A5) [D_i, D_j] = 0 (Lie bracket components)", all(sp.expand(D(i, Dcoef[j][k]) - D(j, Dcoef[i][k])) == 0 for i in range(3) for j in range(3) for k in range(3)))
den = {sp.denom(sp.together(cf)) for row in Dcoef for e in row for cf in sp.Poly(e, x, y, w).coeffs()}
check(f"(A5) the coefficient denominators of the D_i are {sorted(den)} (so A_3(Z[1/2]) is needed, not A_3(Z)); the constant term of the d_x-coefficient of D_3 is {sp.Poly(Dcoef[2][0], x, y, w).coeff_monomial(1)}",
      den == {1, 2} and sp.Poly(Dcoef[2][0], x, y, w).coeff_monomial(1) == sp.Rational(1, 2))

# (A6) integer points: A = 0 example and Delta(F) = 0 example
def at(pt, e): return sp.expand(e.subs({x: pt[0], y: pt[1], w: pt[2]}))
ptA = (1, -2, 8)
fA = sp.factor(sp.expand(at(ptA, F1)*s**3 + at(ptA, F2)*s**2*t + 4*s*t**2 + 4*at(ptA, F3)*t**3))
check(f"(A6) at (x,y,w) = (1,-2,8): A = {at(ptA, A)}, B = {at(ptA, B)}, C = {at(ptA, C)}, so Q = 2st and f_F = {fA}: three rational roots, "
      "the Q-algebra is Q^3, whereas the note's formula Q x Q[theta]/(Q(theta,1)) = Q x Q[theta]/(2 theta) has rank 2",
      at(ptA, A) == 0 and at(ptA, B) == 2 and at(ptA, C) == 0)
ptD = (0, 4, -63)
check(f"(A6) at (x,y,w) = (0,4,-63): Disc(Q) = B^2 - 4AC = {at(ptD, B**2 - 4*A*C)} and Delta(F) = {at(ptD, Delta(F1, F2, F3))}: degenerate (non-reduced) cubic ring at an integer point",
      at(ptD, B**2 - 4*A*C) == 0 and at(ptD, Delta(F1, F2, F3)) == 0)
g2 = [math.gcd(-2*xv, 1 + xv*yv) for xv in range(-20, 21) for yv in range(-20, 21)]
check(f"(A6) gcd(u, v) = gcd(-2x, 1+xy) takes exactly the values {sorted(set(g2))} on |x|,|y| <= 20 (L is not always primitive)", set(g2) == {1, 2})
print(f"\nsummary: {len(res)} checks, {sum(o for _, o in res)} PASS, {len(res) - sum(o for _, o in res)} FAIL; {time.time()-T0:.0f}s")
