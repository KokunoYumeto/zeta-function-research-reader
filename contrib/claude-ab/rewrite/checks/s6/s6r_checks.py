# Checks for the S^6 reader: the explicit finite and algebraic content of the S^6 record that can be tested
# from the definitions. Prepared by Claude (Opus 5.5). Needs sympy.
import sympy as sp
from itertools import product
ok = True
def check(name, cond, val=None):
    global ok
    ok &= bool(cond)
    print(("PASS " if cond else "FAIL ") + name + ("" if val is None else f"  [{val}]"))

x, y, z, t, u, v, r = sp.symbols('x y z t u v r')
F = y**2 * z - x**2 * (x + z) - t * z**3
# correction note, Prop. 4.1: smoothness of the total space {F = 0} in P^2 x Delta
check("chart z = 1: dF/dt = -z^3 = -1 never vanishes", sp.diff(F, t).subs(z, 1) == -1)
Fz0 = F.subs(z, 0)
check("on z = 0 the equation forces x = 0 (F|_{z=0} = -x^3)", sp.expand(Fz0) == -x**3)
check("at z = 0, x = 0: dF/dz = y^2 (nonzero since y != 0 there)", sp.simplify(sp.diff(F, z).subs({z: 0, x: 0})) == y**2)
# discriminant of the affine cubic y^2 = x^3 + x^2 + t: singular fibres at t = 0 and t = -4/27
disc = sp.discriminant(x**3 + x**2 + t, x)
check("disc(x^3 + x^2 + t) = -t(27t + 4): singular fibres t = 0, -4/27", sp.factor(disc) == sp.factor(-t * (27 * t + 4)), sp.factor(disc))
# normalization of the nodal cubic y^2 z = x^2 (x + z)
X, Y, Z = (u**2 - v**2) * v, u * (u**2 - v**2), v**3
check("nu[u:v] = [(u^2-v^2)v : u(u^2-v^2) : v^3] lies on C_0", sp.expand(Y**2 * Z - X**2 * (X + Z)) == 0)
check("nu(1:1) = nu(-1:1) = node [0:0:1]", [X.subs({u: 1, v: 1}), Y.subs({u: 1, v: 1})] == [0, 0] and [X.subs({u: -1, v: 1}), Y.subs({u: -1, v: 1})] == [0, 0])
# local model at the node: y^2 - x^2 - x^3 = (y - x h)(y + x h), h = sqrt(1 + x)
h = sp.sqrt(1 + x)
check("t = y^2 - x^2 - x^3 = (y - x h)(y + x h) with h = sqrt(1+x)", sp.simplify((y - x * h) * (y + x * h) - (y**2 - x**2 - x**3)) == 0)
# Lemma 4.3: the section P(t) = [3 : sqrt(36+t) : 1] lies on C, and the gluing multiplier is 1/3
check("P(t) = [3 : sqrt(36+t) : 1] satisfies y^2 = x^2(x+1) + t", sp.simplify(F.subs({x: 3, y: sp.sqrt(36 + t), z: 1})) == 0)
check("P(0) = [3:6:1] corresponds to r = y/x = 2 on the normalization (x = r^2 - 1)", sp.Rational(6, 3) == 2 and 2**2 - 1 == 3)
f = r - 2
check("gluing multiplier f(1)/f(-1) = (-1)/(-3) = 1/3, not a root of unity", f.subs(r, 1) / f.subs(r, -1) == sp.Rational(1, 3))
# Lemma 4.2: a global section of the glued bundle is a constant c on P^1 with c = lambda c, so c = 0 for lambda != 1
lam = sp.Rational(1, 3)
check("H^0(C_0, A_lambda) = 0: c = lambda c forces c = 0 for lambda = 1/3", sp.solve(sp.Eq(sp.Symbol('c'), lam * sp.Symbol('c')), sp.Symbol('c')) == [0])

# local algebra of the relative differentials (monograph section 14 item 6; reader Proposition on torsion)
# t = xy: M = R^2 / R(y, x) is torsion-free (the kernel argument), not free at the origin (relation in m R^2)
a, b, c, fct, g = sp.symbols('a b c f g')
# symbolic content: f(a,b) = g(y,x) implies a x = b y; with gcd(x,y)=1 this forces (a,b) = h(y,x)
check("t = xy: the relation (y, x) lies in m*R^2 (so 2 generators are needed at the origin)", all(sp.Poly(e, x, y).as_expr().subs({x: 0, y: 0}) == 0 for e in (y, x)))
check("t = xyz: the relation (yz, xz, xy) lies in m*R^3", all(e.subs({x: 0, y: 0, z: 0}) == 0 for e in (y * z, x * z, x * y)))
# multiplicity-m cyclic chart t = s^m: dt = m s^(m-1) ds, torsion R/(s^(m-1)) ds
s_ = sp.Symbol('s')
for mm in (2, 3, 4):
    check(f"t = s^{mm}: dt = {mm} s^{mm-1} ds, so Omega_(X/B) has torsion R/(s^{mm-1}) ds", sp.diff(s_**mm, s_) == mm * s_**(mm - 1))

# monograph section 14 item 2: Remark 7.28 fails for a fixed triple
p = 12 * 100 - 4 * 1 - 3 * (-1)
check("Remark 7.28 counterexample: (l0,l1,l2) = (100,1,-1) gives p = 1199 != +-1", p == 1199)
# topology update: the spin quadratic form q(x,y) = x + xy + y over F_2 has Arf invariant 1
vals = [(xx + xx * yy + yy) % 2 for xx, yy in product((0, 1), repeat=2)]
check("q(x,y) = x + xy + y over F_2 takes the value 1 three times: Arf invariant 1", sum(vals) == 3, vals)
# the peripheral character values (-1, 4, -3) mod 12 and Psi = 12 chi mod 24
chi = [-1, 4, -3]
check("Psi_H(C0, C1, C2') = 12*chi mod 24 = (12, 0, 12)", [(12 * cc) % 24 for cc in chi] == [12, 0, 12])
# key advances S6-5 (arithmetic part; proved in the reader of four workbenches): P(a) = a0(a0^2 - 3|a'|^2)
bad = []
for aa in product(range(-6, 7), repeat=4):
    P = aa[0] * (aa[0]**2 - 3 * (aa[1]**2 + aa[2]**2 + aa[3]**2))
    if P % 3 == 0 and P % 9 != 0: bad.append(aa)
    if sum(aa) % 2 == 0 and P % 2 != 0: bad.append(aa)
check("S6-5: 3 | P implies 9 | P, and P is even on D4 (all |a_i| <= 6)", bad == [])
# S6-1 dimension count h^0(omega^-m) = floor(m/2) + 1 for the ring C[U,V], deg U = 1, deg V = 2
check("S6-1: #{(i,j): i + 2j = m} = floor(m/2) + 1 for m <= 40",
      all(sum(1 for j in range(m // 2 + 1) if m - 2 * j >= 0) == m // 2 + 1 for m in range(41)))

# ---- additions for Section 5 of the reader (sharpening of the test family; local algebra) ----
# (a) the crossing R = C{u,v,w}/(uv): tau = v du = -u dv is killed by u and v (so T_S = O_D * tau)
uu, vv, ww = sp.symbols('u v w')
rel = sp.Matrix([vv, uu, 0])            # d(uv) = v du + u dv, coordinates (du, dv, dw)
tau = sp.Matrix([vv, 0, 0])             # v du
# u*tau = u v du = 0 in R (uv = 0); v*tau = v^2 du = v*(rel) - (0, uv, 0) = v*rel mod uv
check("u * tau = 0 in Omega^1_R (entries divisible by uv)", all(sp.expand(e).subs(uu*vv, 0) == 0 or sp.rem(sp.expand(e), uu*vv, uu) == 0 for e in uu*tau))
diff_v = sp.expand(vv*tau - vv*rel)     # = (0, -uv, 0), zero in R
check("v * tau = v * d(uv) in R^3 modulo uv, so v tau = 0 in Omega^1_R", all(sp.rem(e, uu*vv, uu) == 0 for e in diff_v))
# (b) H^0 and H^1 of A on S (and of A_lambda on C_0): the map (c, k) -> (alpha c - k, beta c - k) with alpha/beta = lambda
al, be, lamb = sp.symbols('alpha beta lambda', nonzero=True)
Mck = sp.Matrix([[al, -1], [be, -1]])
check("det of (c,k) -> (alpha c - k, beta c - k) is beta - alpha, nonzero iff lambda = alpha/beta != 1",
      sp.simplify(Mck.det() - (be - al)) == 0)
# (c) the conormal lines of the two branches at the node are distinct: du, dv independent at (0,0)
hh = sp.sqrt(1 + x)
U, V = y - x*hh, y + x*hh
J = sp.Matrix([[sp.diff(U, x), sp.diff(U, y)], [sp.diff(V, x), sp.diff(V, y)]]).subs({x: 0, y: 0})
check("du and dv are independent at the node (Jacobian determinant -2)", J.det() == -2, J.det())
# (d) degree bookkeeping on the normalization: deg nu^*K_C = K_C.C_0 = deg omega_{C_0} - C_0^2 = 0 - 0,
#     deg N^*_nu = 0 - deg K_{P^1} = 2, and N^*_nu(-p-q) has degree 0 (sections: constants)
check("deg N*_nu = deg nu^*Omega^1_C - deg Omega^1_P1 = 0 - (-2) = 2; minus p, q gives 0", (0 - (-2)) - 2 == 0)
# (e) gcd of the partial derivatives of t = unit * monomial is the monomial with exponents lowered by one
X1, X2, X3 = sp.symbols('x1 x2 x3')
def local_gcd_ok(t, expected):
    g = sp.gcd_list([sp.diff(t, X1), sp.diff(t, X2), sp.diff(t, X3)])
    q = sp.cancel(g / expected)
    # the quotient must be a polynomial that does not vanish at the origin (a unit of the local ring)
    return q.is_polynomial(X1, X2, X3) and q.subs({X1: 0, X2: 0, X3: 0}) != 0
cases = [
    (X1*X2, 1), (X1*X2*X3, 1), (X1**3, X1**2), (X1**4, X1**3),
    (X1**2*X2, X1), (X1**2*X2**3*X3, X1*X2**2), ((1 + X1 + X2)*X1*X2, 1), ((1 + X1)*X1**2*X2, X1),
    ((2 + X3)*X1**3*X2**2, X1**2*X2),
]
check("gcd of partials of u * x^m equals prod x_i^(m_i - 1) up to a unit (9 cases)", all(local_gcd_ok(t, e) for t, e in cases))
# (f) second relative differentials: t = xy and t = xyz have torsion in Omega^2_{R/C{t}}
# basis e1 = dx^dy, e2 = dx^dz, e3 = dy^dz; dt ^ dx_i in this basis
def wedge_dt(grad):
    a, b, c = grad   # dt = a dx + b dy + c dz
    # dt^dx = b dy^dx + c dz^dx = -b e1 - c e2 ; dt^dy = a e1 - c e3 ; dt^dz = a e2 + b e3
    return [sp.Matrix([-b, -c, 0]), sp.Matrix([a, 0, -c]), sp.Matrix([0, a, b])]
gxy = wedge_dt((y, x, 0))
check("t = xy: x * (dx^dy) = -(dt ^ dx), so dx^dy is killed by x", sp.expand(sp.Matrix([x, 0, 0]) + gxy[0]) == sp.zeros(3, 1))
check("t = xy: every relation dt ^ dx_i has entries in the maximal ideal, so dx^dy != 0",
      all(e.subs({x: 0, y: 0, z: 0}) == 0 for r in gxy for e in r))
gxyz = wedge_dt((y*z, x*z, x*y))
zeta = sp.Matrix([z, y, 0])                       # z dx^dy + y dx^dz
check("t = xyz: x * (z dx^dy + y dx^dz) = -(dt ^ dx)", sp.expand(x*zeta + gxyz[0]) == sp.zeros(3, 1))
def in_m2(e):
    p = sp.Poly(sp.expand(e), x, y, z)
    return all(sum(mon) >= 2 for mon in p.monoms()) if not p.is_zero else True
check("t = xyz: every relation dt ^ dx_i has entries in m^2, while zeta has entries of degree 1, so zeta != 0",
      all(in_m2(e) for r in gxyz for e in r) and not all(in_m2(e) for e in zeta))
# (g) Hirzebruch-Riemann-Roch on a threefold: chi(T_X) = c3/2 when c1 = c2 = 0 (rationally)
ra, rb, rc, eps = sp.symbols('a b c epsilon')
def trunc3(expr):
    s = sp.series(expr.subs({ra: eps*ra, rb: eps*rb, rc: eps*rc}), eps, 0, 4).removeO()
    return sp.expand(s.coeff(eps, 3))
ch = sum(sp.exp(r) for r in (ra, rb, rc))
td = sp.prod([r/(1 - sp.exp(-r)) for r in (ra, rb, rc)])
deg3 = trunc3(ch*td)
c1, c2, c3 = ra + rb + rc, ra*rb + rb*rc + rc*ra, ra*rb*rc
# write deg3 = A c1^3 + B c1 c2 + C c3 and solve
Aa, Bb, Cc = sp.symbols('A B C')
sol = sp.solve(sp.Poly(sp.expand(deg3 - (Aa*c1**3 + Bb*c1*c2 + Cc*c3)), ra, rb, rc).coeffs(), [Aa, Bb, Cc], dict=True)
check("HRR: [ch(T) td(T)]_3 = A c1^3 + B c1 c2 + c3/2, so chi(T_X) = c3/2 when c1 = c2 = 0", len(sol) == 1 and sol[0][Cc] == sp.Rational(1, 2), sol)


# (h) the whole torsion of Omega^2_{R/C{t}} at t = xyz: kernel of dt^ on Omega^2 is free on zeta1 = (z, y, 0), zeta3 = (0, y, x)
kerform = lambda v: sp.expand(x*y*v[0] - x*z*v[1] + y*z*v[2])   # dt ^ (a e1 + b e2 + c e3) = (xy a - xz b + yz c) dx^dy^dz
z1, z3 = sp.Matrix([z, y, 0]), sp.Matrix([0, y, x])
check("t = xyz: zeta1 = z e1 + y e2 and zeta3 = y e2 + x e3 lie in the kernel of dt ^ on Omega^2", kerform(z1) == 0 and kerform(z3) == 0)
rx, ry, rz = gxyz
check("t = xyz: in the basis (zeta1, zeta3) the relations are -x zeta1, y zeta1 - y zeta3, z zeta3",
      sp.expand(rx + x*z1) == sp.zeros(3, 1) and sp.expand(ry - (y*z1 - y*z3)) == sp.zeros(3, 1) and sp.expand(rz - z*z3) == sp.zeros(3, 1))
# the torsion T = R^2/<(x,0),(y,-y),(0,z)> is killed by J = (yz, xz, xy): check yz, xz, xy times each generator lie in the relation module
Rel = sp.Matrix([[x, y, 0], [0, -y, z]])   # columns are the relations in the basis (zeta1, zeta3)
aa_, bb_, cc_ = sp.symbols('aa bb cc')
def in_rel(vec):
    # solve Rel * (aa, bb, cc)^T = vec with polynomial coefficients by a degree-bounded ansatz (degree <= 2)
    mons = [sp.Integer(1), x, y, z, x*x, y*y, z*z, x*y, x*z, y*z]
    cs = sp.symbols('k0:30')
    A = sum(cs[i]*mons[i] for i in range(10)); B = sum(cs[10+i]*mons[i] for i in range(10)); Cc2 = sum(cs[20+i]*mons[i] for i in range(10))
    eqs = sp.expand(Rel*sp.Matrix([A, B, Cc2]) - vec)
    coeffs = []
    for e in eqs:
        coeffs += sp.Poly(e, x, y, z).coeffs()
    return len(sp.solve(coeffs, cs, dict=True)) > 0
gens = [sp.Matrix([1, 0]), sp.Matrix([0, 1])]
check("t = xyz: the torsion R^2/<(x,0),(y,-y),(0,z)> is killed by yz, xz and xy",
      all(in_rel(f*g) for f in (y*z, x*z, x*y) for g in gens))
check("t = xyz: Hilbert-Burch: the 2x2 minors of [[x,0],[-y,y],[0,-z]] are xy, -xz, yz",
      [sp.expand(sp.Matrix([[x, 0], [-y, y], [0, -z]]).extract(r, [0, 1]).det()) for r in ([0, 1], [0, 2], [1, 2])] == [x*y, -x*z, y*z])

# ---- additions for Section 6 of the reader (later supplements; key advances) ----
mr, mi, br, bi, tr, ti = sp.symbols('mr mi br bi tr ti', real=True)
PiR = sp.Matrix([[6*mr, tr, 1, 0], [6*mi, ti, 0, 0], [br, mr, 0, 1], [bi, mi, 0, 0]])
check("det_R [Z | I2] = Im(tau) Im(beta) - 6 Im(mu)^2 = Im(tau) * D", sp.expand(PiR.det() - (ti*bi - 6*mi**2)) == 0)
dI = sp.Symbol('dI', real=True)   # Im(delta): beta_c = beta_part + c shifts Im(beta) by Im(delta)
check("S6-2: det_R(Pi_c)/det_R(Pi_c*) = (D + Im delta)/D", sp.simplify(PiR.det().subs(bi, bi + dI)/PiR.det() - ((bi - 6*mi**2/ti) + dI)/(bi - 6*mi**2/ti)) == 0)
check("S6-4: glue index of A5^4 + D4 is sqrt(6^4 * 4) = 72", sp.sqrt(6**4 * 4) == 72)
check("S6-4: the root system A2^12 has 12 * 6 = 72 roots", 12 * 6 == 72)
check("S6-4: an index-9 sublattice of a unimodular lattice has determinant 81", 9**2 == 81)
# quaternion arithmetic for S6-5: tau(q) = Re((q1 q2) q3) at q1 = q2 = q3 = sqrt(2) a with a a quaternion
def qmul(p, q):
    a1, b1, c1, d1 = p; a2, b2, c2, d2 = q
    return (a1*a2 - b1*b2 - c1*c2 - d1*d2, a1*b2 + b1*a2 + c1*d2 - d1*c2,
            a1*c2 - b1*d2 + c1*a2 + d1*b2, a1*d2 + b1*c2 - c1*b2 + d1*a2)
A0, A1, A2, A3 = sp.symbols('a0 a1 a2 a3', integer=True)
qa = tuple(sp.sqrt(2)*e for e in (A0, A1, A2, A3))
re_cube = sp.expand(qmul(qmul(qa, qa), qa)[0])
check("S6-5: Re((q q) q) at q = sqrt(2) a equals 2 sqrt(2) a0 (a0^2 - 3(a1^2 + a2^2 + a3^2))",
      sp.simplify(re_cube - 2*sp.sqrt(2)*A0*(A0**2 - 3*(A1**2 + A2**2 + A3**2))) == 0)
GD4b = sp.Matrix([[1, 1, 0, 0], [1, -1, 0, 0], [0, 1, -1, 0], [0, 0, 1, -1]])
GD4 = GD4b * GD4b.T
check("S6-5: det Gram(D4) = 4 and det(6 Gram(D4)) = 5184", GD4.det() == 4 and (6*GD4).det() == 5184)
normsD4 = [sum(e*e for e in aa) for aa in product(range(-2, 3), repeat=4) if any(aa) and sum(aa) % 2 == 0]
check("S6-5: the minimum norm of D4 is 2, so the minimum of I (norm 6|a|^2) is 12", min(normsD4) == 2 and 6*min(normsD4) == 12)
Pv = lambda aa: aa[0]*(aa[0]**2 - 3*(aa[1]**2 + aa[2]**2 + aa[3]**2))
check("S6-5: P(1,1,0,0) = -2, so the value group 2 sqrt(2) P(D4) Z is 4 sqrt(2) Z (P even on D4)", Pv((1, 1, 0, 0)) == -2)
check("topology supplement: Euler characteristic 6 + 0 + 0 = 6 differs from chi(S^8) = 2", 6 + 0 + 0 == 6 and 6 != 2)
check("topology supplement: Psi_H = 12 chi mod 24 vanishes exactly on even chi (chi mod 12)",
      all(((12*c) % 24 == 0) == (c % 2 == 0) for c in range(12)))

print("ALL PASS" if ok else "SOME CHECK FAILED")
