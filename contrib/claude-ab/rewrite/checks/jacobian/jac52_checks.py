#!/usr/bin/env python3
"""jac52_checks.py -- exact checks (sympy) for note 52_: the Jacobian-conjecture counterexample F of Alpöge (20 July 2026),
F(x,y,w) = ((1+xy)^3 w + y^2(1+xy)(4+3xy), y + 3x(1+xy)^2 w + 3xy^2(4+3xy), 2x - 3x^2 y - x^3 w).

Structure (the multiplication map L*Q with a resultant normalization on an affine slice, as in Tao's exposition of
21 July 2026; the explicit coordinates here are ours): with u = -2x, v = 1+xy and
A = (1+xy)^2 w + y^2(4+3xy), B = x(1+xy) w + y(1+3xy), C = 2(2 - 3xy - x^2 w),
the binary cubic f_F(s,t) = F1 s^3 + F2 s^2 t + 4 s t^2 + 4 F3 t^3 factors as (v s - u t)(A s^2 + B s t + C t^2),
and q(u,v) = A u^2 + B u v + C v^2 = 4.
"""
import sympy as sp, time
T0 = time.time()
res = []
def check(name, cond):
    ok = bool(cond); res.append((name, ok)); print(("PASS" if ok else "FAIL") + "  " + name, flush=True)

x, y, w, s, t = sp.symbols('x y w s t')
a, b, c = sp.symbols('a b c')
u_, v_, A_, B_, C_ = sp.symbols('u v A B C')
F1 = (1+x*y)**3*w + y**2*(1+x*y)*(4+3*x*y)
F2 = y + 3*x*(1+x*y)**2*w + 3*x*y**2*(4+3*x*y)
F3 = 2*x - 3*x**2*y - x**3*w
F = sp.Matrix([F1, F2, F3])
DF = F.jacobian([x, y, w])
check("det DF = -2", sp.expand(DF.det()) == -2)
check("F(0,0,-1/4) = F(1,-3/2,13/2) = F(-1,3/2,13/2) = (-1/4,0,0)",
      all(list(F.subs({x: p[0], y: p[1], w: p[2]})) == [sp.Rational(-1, 4), 0, 0]
          for p in [(0, 0, sp.Rational(-1, 4)), (1, sp.Rational(-3, 2), sp.Rational(13, 2)), (-1, sp.Rational(3, 2), sp.Rational(13, 2))]))

# ---- 1. the factorization and the normalization
u = -2*x; v = 1 + x*y
A = (1+x*y)**2*w + y**2*(4+3*x*y)
B = x*(1+x*y)*w + y*(1+3*x*y)
C = 2*(2 - 3*x*y - x**2*w)
f_F = F1*s**3 + F2*s**2*t + 4*s*t**2 + 4*F3*t**3
check("(A1) f_F(s,t) = (v s - u t)(A s^2 + B s t + C t^2)", sp.expand(f_F - (v*s - u*t)*(A*s**2 + B*s*t + C*t**2)) == 0)
check("(A2) resultant normalization q(u,v) = A u^2 + B u v + C v^2 = 4", sp.expand(A*u**2 + B*u*v + C*v**2 - 4) == 0)
check("(A2') v C - u B = 4 (the s t^2 coefficient)", sp.expand(v*C - u*B - 4) == 0)
check("u and v never vanish together: u = 0 => v = 1", sp.expand(v.subs(x, 0)) == 1)

# ---- 2. the inverse of iota: W = {vC - uB = 4, Au^2 + Buv + Cv^2 = 4} -> C^3
yW = (A_*u_ + 2*B_*v_)/2
xW = -u_/2
xyW = sp.expand(xW*yW)
v2w = A_ - yW**2*(4 + 3*xyW)            # = v^2 w on W
u2w = 4*(2 - 3*xyW - C_/2)               # = u^2 w on W  (u^2 w = 4 x^2 w)
wW = sp.expand(((C_**3*v_ - 3*B_*C_**2*u_)*v2w + (3*B_**2*C_*v_ - B_**3*u_)*u2w)/64)
sub = {u_: u, v_: v, A_: A, B_: B, C_: C}
check("(A3) iota^{-1} o iota = id on C^3 (x, y, w recovered exactly)",
      sp.expand(xW.subs(sub) - x) == 0 and sp.expand(yW.subs(sub) - y) == 0 and sp.expand(wW.subs(sub) - w) == 0)
GW = sp.groebner([v_*C_ - u_*B_ - 4, A_*u_**2 + B_*u_*v_ + C_*v_**2 - 4], u_, v_, A_, B_, C_, order='grevlex', domain='QQ')
back = {x: xW, y: yW, w: wW}
comp = [sp.expand(e.subs(back)) for e in (u, v, A, B, C)]
check("(A3) iota o iota^{-1} = id on W (modulo the two defining equations of W)",
      all(GW.reduce(sp.expand(comp[i] - [u_, v_, A_, B_, C_][i]))[1] == 0 for i in range(5)))
import itertools
eqsW = [v_*C_ - u_*B_ - 4, A_*u_**2 + B_*u_*v_ + C_*v_**2 - 4]
JW = sp.Matrix([[sp.diff(e, zz) for zz in (u_, v_, A_, B_, C_)] for e in eqsW])
minors = [JW[:, list(cols)].det() for cols in itertools.combinations(range(5), 2)]
check("W is a smooth complete intersection of dimension 3: the equations and all 2x2 minors of their Jacobian generate the unit ideal",
      sp.groebner(eqsW + minors, u_, v_, A_, B_, C_, order='grevlex', domain='QQ').exprs == [1])

# ---- 3. discriminant, non-properness set, minimal polynomials
Delta = 27*a**2*c**2 - 18*a*b*c + 16*a + b**3*c - b**2
S = sp.symbols('S')
check("(A4) Disc_s(a s^3 + b s^2 + 4 s + 4 c) = -16 Delta", sp.expand(sp.discriminant(a*S**3 + b*S**2 + 4*S + 4*c, S) + 16*Delta) == 0)
sub3 = {a: F1, b: F2, c: F3}
check("(A7) x-cubic: Delta(F) x^3 + (4 - 3 F2 F3) x - 2 F3 = 0 identically", sp.expand((Delta*x**3 + (4 - 3*b*c)*x - 2*c).subs(sub3)) == 0)
check("(A7) y-cubic (monic up to 2): 2y^3 - 3 F2 y^2 + 18 F1 y + 27 F1^2 F3 - 18 F1 F2 + F2^3 = 0 identically",
      sp.expand((2*y**3 - 3*b*y**2 + 18*a*y + 27*a**2*c - 18*a*b + b**3).subs(sub3)) == 0)
wc = (8*S**3 + 3*(108*a**2*c**2 - 72*a*b*c + 136*a - 5*b**3*c + 2*b**2)*S**2
      + 6*Delta*(27*a**2*c**2 - 18*a*b*c + 52*a + b**3*c + 14*b**2)*S
      + Delta*(729*a**4*c**4 - 972*a**3*b*c**3 + 2322*a**3*c**2 + 54*a**2*b**3*c**3 + 270*a**2*b**2*c**2 - 3735*a**2*b*c - 338*a**2
               - 36*a*b**4*c**2 + 122*a*b**3*c + 1372*a*b**2 + b**6*c**2 - 2*b**5*c - 80*b**4))
check("(A7) w-cubic (monic up to 8) vanishes identically at S = w", sp.expand(wc.subs(sub3).subs(S, w)) == 0)
samp = {a: 1, b: 2, c: 3}
yc = 2*S**3 - 3*b*S**2 + 18*a*S + 27*a**2*c - 18*a*b + b**3
check("(A7) the y- and w-cubics have nonzero discriminant at (a,b,c) = (1,2,3), so y and w separate generic fibres (their cubics are minimal)",
      sp.discriminant(yc.subs(samp), S) != 0 and sp.discriminant(wc.subs(samp), S) != 0)
check("(A7) x-cubic discriminant = -4 Delta (27ac^2 - 9bc + 8)^2",
      sp.expand(sp.discriminant(Delta*S**3 + (4 - 3*b*c)*S - 2*c, S) + 4*Delta*(27*a*c**2 - 9*b*c + 8)**2) == 0)
check("Delta is irreducible over Q", len(sp.factor_list(Delta)[1]) == 1 and sp.factor_list(Delta)[1][0][1] == 1)
# absolute irreducibility: Delta = 27a^2 c^2 + (b^3 - 18ab) c + (16a - b^2) is quadratic in c with coprime coefficients;
# a factorization over C would be into two c-linear factors, which needs its c-discriminant to be a square in C[a,b].
check("Delta is irreducible over C: coefficients in c are coprime and disc_c(Delta) = (b^2 - 12a)^3, not a square",
      sp.gcd(sp.gcd(27*a**2, b**3 - 18*a*b), 16*a - b**2) == 1
      and sp.expand(sp.discriminant(Delta, c) - (b**2 - 12*a)**3) == 0)
check("-Delta is not a square in C(a,b,c): Delta(a,0,0) = 16a", sp.expand(Delta.subs({b: 0, c: 0})) == 16*a)
check("the generic slice cubic a S^3 + b S^2 + 4S + 4c is irreducible over C(a,b,c): it is linear in c with coprime coefficients 4 and S(aS^2+bS+4)",
      sp.gcd(sp.Integer(4), S*(a*S**2 + b*S + 4)) == 1)
check("Delta o F = 4AC - B^2 = -Disc(Q): Disc(f_F) = Res(L,Q)^2 Disc(Q) = 16 Disc(Q)", sp.expand(Delta.subs(sub3) - (4*A*C - B**2)) == 0)
check("the root is [u : v] = [2(y - F2) : 3 F1]: 3 F1 u - 2 (y - F2) v = 0 identically", sp.expand(3*F1*u - 2*(y - F2)*v) == 0)
Y = sp.symbols('Y')
fab = lambda ss, tt: a*ss**3 + b*ss**2*tt + 4*ss*tt**2 + 4*c*tt**3
check("f(2(Y - b), 3a) = 4a (2Y^3 - 3bY^2 + 18aY + 27a^2 c - 18ab + b^3) in Q[a,b,c,Y] (so the y-cubic is the root equation)",
      sp.expand(fab(2*(Y - b), 3*a) - 4*a*(2*Y**3 - 3*b*Y**2 + 18*a*Y + 27*a**2*c - 18*a*b + b**3)) == 0)

# ---- 4. the twisted cubic: triple-root cubics in the slice, and the image complement
cc = sp.symbols('cc', nonzero=True)
tw = {a: sp.Rational(4, 27)/cc**2, b: sp.Rational(4, 3)/cc, c: cc}
check("(A5) the curve (4/(27c^2), 4/(3c), c) is the set of triple-root cubics: f = (4/27)(s/c + 3 t)^3 c ... Delta = 0 and 3bc = 4",
      sp.simplify(Delta.subs(tw)) == 0 and sp.simplify((3*b*c).subs(tw)) == 4
      and sp.expand(sp.Rational(4, 27)/cc**2*s**3 + sp.Rational(4, 3)/cc*s**2*t + 4*s*t**2 + 4*cc*t**3 - sp.Rational(4, 27)/cc**2*(s + 3*cc*t)**3) == 0)
check("on Delta = 0, 3bc = 4 forces the triple-root curve: Delta|_{b = 4/(3c)} = (27ac^2 - 4)^2/(27c^2)",
      sp.simplify(Delta.subs(b, sp.Rational(4, 3)/c) - (27*a*c**2 - 4)**2/(27*c**2)) == 0)

# ---- 5. the escaping curve of 28_: F(gamma) = (-1/4 + 2 tau, 0, 0) -> (0,0,0) on the discriminant; its root tends to the double root
z = sp.symbols('z', positive=True)
gam = {x: 1/z, y: -3*z/2, w: 13*z**2/2}
check("gamma: F(gamma) = (-z^2/4, 0, 0) and its root [u:v] = [-2/z : -1/2] = [4/z : 1] -> [1 : 0], the double root of f = 4 s t^2 at z = 0",
      [sp.simplify(e.subs(gam)) for e in F] == [-z**2/4, 0, 0] and sp.simplify((u/v).subs(gam) - 4/z) == 0)
check("Delta(0,0,0) = 0: the limit point of F(gamma) lies on the non-properness set", Delta.subs({a: 0, b: 0, c: 0}) == 0)

# ---- 5'. a C^*-symmetry: weights (-1, 1, 2) on (x, y, w) and (2, 1, -1) on (F1, F2, F3); the escaping curve is an orbit
lam = sp.symbols('lambda', nonzero=True)
act = {x: x/lam, y: lam*y, w: lam**2*w}
check("(T) F is C^*-equivariant: F(x/l, l y, l^2 w) = (l^2 F1, l F2, F3/l)",
      [sp.simplify(e.subs(act, simultaneous=True) - m*e) for e, m in zip(F, (lam**2, lam, 1/lam))] == [0, 0, 0])
check("(T) Delta is homogeneous of weight 2: Delta(l^2 a, l b, c/l) = l^2 Delta(a,b,c) (the non-properness surface is C^*-stable)",
      sp.simplify(Delta.subs({a: lam**2*a, b: lam*b, c: c/lam}, simultaneous=True) - lam**2*Delta) == 0)
check("(T) the escaping curve of 28_ is the orbit of the fibre point (1, -3/2, 13/2): gamma(tau) = z . (1, -3/2, 13/2), z = sqrt(1 - 8 tau)",
      all(sp.simplify(e.subs({x: 1, y: sp.Rational(-3, 2), w: sp.Rational(13, 2)}).subs(lam, z) - gam[v0]) == 0
          for e, v0 in zip((x/lam, lam*y, lam**2*w), (x, y, w))))
check("(T) the missing curve (4/(27c^2), 4/(3c), c) is the single C^*-orbit of (4/27, 4/3, 1)",
      all(sp.simplify(e1 - e2) == 0 for e1, e2 in zip((lam**2*sp.Rational(4, 27), lam*sp.Rational(4, 3), 1/lam),
                                                     (sp.Rational(4, 27)/(1/lam)**2, sp.Rational(4, 3)/(1/lam), 1/lam))))
Pq, Qq = sp.symbols('P Q')
gcurve = 27*Pq**2 - 18*Pq*Qq + 16*Pq + Qq**3 - Qq**2
check("(T) in the invariants P = a c^2, Q = b c (weight 0), c^2 Delta = 27P^2 - 18PQ + 16P + Q^3 - Q^2",
      sp.expand(c**2*Delta - gcurve.subs({Pq: a*c**2, Qq: b*c})) == 0)
sing = {Pq: sp.Rational(4, 27), Qq: sp.Rational(4, 3)}
Hs = sp.hessian(gcurve, (Pq, Qq)).subs(sing)
check("(T) that plane cubic has an ordinary cusp at (P,Q) = (4/27, 4/3), the image of the missing orbit: g = dg = 0, Hessian of rank 1, "
      "tangent cone 6(3dP - dQ)^2, and the cubic term Q^3 is nonzero along dQ = 3dP",
      gcurve.subs(sing) == 0 and sp.diff(gcurve, Pq).subs(sing) == 0 and sp.diff(gcurve, Qq).subs(sing) == 0
      and Hs.rank() == 1 and sp.expand((sp.Matrix([1, 3]).T*Hs*sp.Matrix([1, 3]))[0]) == 0
      and sp.expand(gcurve.subs({Pq: sp.Rational(4, 27) + sp.Symbol('eps'), Qq: sp.Rational(4, 3) + 3*sp.Symbol('eps')}, simultaneous=True)
                    - 27*sp.Symbol('eps')**3) == 0)
check("(T) over (0,0,0) the fibre is the single point (0,0,0): the x-cubic reads 4x = 0, then F3 = 0, F2 = y, F1 = w",
      sp.expand((Delta*x**3 + (4 - 3*b*c)*x - 2*c).subs({a: 0, b: 0, c: 0})) == 4*x
      and sp.expand(F2.subs(x, 0)) == y and sp.expand(F1.subs({x: 0, y: 0})) == w)

# ---- 6. Dixmier: the endomorphism of the Weyl algebra A_3
adj = DF.adjugate()
Dcoef = (adj/(-2)).T          # D_i = sum_k Dcoef[i,k] d_k,  Dcoef = (DF^{-1})^T
adjP = [sp.Poly(sp.expand(e), x, y, w) for e in adj]
DinvP = [sp.Poly(sp.expand(e), x, y, w) for e in Dcoef]
check("adj(DF) has integer polynomial entries, so DF^{-1} = adj(DF)/(-2) has entries in Z[1/2][x,y,w] (denominators 1 or 2)",
      all(cf.is_integer for P in adjP for cf in P.coeffs())
      and all(sp.fraction(cf)[1] in (1, 2) for P in DinvP for cf in P.coeffs()))
check(f"entries of DF^{{-1}} have total degrees {sorted(set(P.total_degree() for P in DinvP))} (6 to 11)",
      min(P.total_degree() for P in DinvP) == 6 and max(P.total_degree() for P in DinvP) == 11)
def Dop(i, g):
    return sp.expand(sum(Dcoef[i, k]*sp.diff(g, var) for k, var in enumerate((x, y, w))))
check("(W) [D_i, F_j] = D_i(F_j) = delta_ij", all(sp.expand(Dop(i, F[j]) - (1 if i == j else 0)) == 0 for i in range(3) for j in range(3)))
ok = True
for i in range(3):
    for j in range(i + 1, 3):
        for k, var in enumerate((x, y, w)):
            # k-th component of the Lie bracket [D_i, D_j]
            comp_k = Dop(i, Dcoef[j, k]) - Dop(j, Dcoef[i, k])
            if sp.expand(comp_k) != 0:
                ok = False
check("(W) [D_i, D_j] = 0 as vector fields (so as differential operators)", ok)
check("(P) Poisson version: {P_i, P_j} = 0 for P_i = sum_k (DF^{-1})_{ki} p_k is the same bracket condition", ok)
check("(P) det(DF^{-1}) = -1/2, so the cotangent lift (x, p) -> (F(x), DF(x)^{-T} p) of C^6 has Jacobian determinant (-2)(-1/2) = 1",
      sp.simplify(Dcoef.det() + sp.Rational(1, 2)) == 0)
pi_ = sp.Matrix([1, 1, 1])
pts = [(0, 0, sp.Rational(-1, 4)), (1, sp.Rational(-3, 2), sp.Rational(13, 2)), (-1, sp.Rational(3, 2), sp.Rational(13, 2))]
lift_imgs = []
for P0 in pts:
    sb = {x: P0[0], y: P0[1], w: P0[2]}
    pvec = DF.subs(sb).T*pi_                          # choose p = DF^T pi, so DF^{-T} p = pi
    lift_imgs.append((tuple(F.subs(sb)), tuple(Dcoef.subs(sb)*pvec), tuple(pvec)))
check("(P) the cotangent lift is not injective: three distinct points (x_j, DF(x_j)^T (1,1,1)) all map to ((-1/4,0,0), (1,1,1))",
      all(li[0] == (sp.Rational(-1, 4), 0, 0) and li[1] == (1, 1, 1) for li in lift_imgs) and len(set(li[2] + tuple(P0) for li, P0 in zip(lift_imgs, pts))) == 3)
print(f"\nsummary: {len(res)} checks, {sum(o for _, o in res)} PASS, {len(res) - sum(o for _, o in res)} FAIL; {time.time()-T0:.0f}s")
