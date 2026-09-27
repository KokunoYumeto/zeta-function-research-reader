"""Exact identities of the vacuum-hydrodynamics continuation
(continuations/20260919-vacuum-hydrodynamics/: README.md L23-124, manuscripts/IDENTITY_AND_COMPLETION.md
(1.2)-(7.8), SLAB_COMPARATORS.md (S1)-(S9), manuscripts/RESEARCH.md (2)-(33)).
Own sympy/mpmath/scipy code for the inv_NS audit (27 Sep 2026)."""
import sympy as sp
import mpmath as mp
import time

T0 = time.time()
res = []


def check(name, expr, tol=None):
    if tol is None:
        if isinstance(expr, sp.MatrixBase):
            ok = all(sp.simplify(x) == 0 for x in expr)
        elif isinstance(expr, bool):
            ok = expr
        else:
            ok = sp.simplify(expr) == 0
    else:
        ok = bool(abs(expr) < tol)
    res.append((name, ok))
    print(("PASS" if ok else "FAIL") + "  " + name + ("" if ok or tol is None else "  value " + str(expr)))


# ============================================================ 1. compact TT lift (5.2)-(5.4), (6.1)-(6.2)
x1, x2, x3, w = sp.symbols('x1 x2 x3 w', real=True)
xs = (x1, x2, x3)
Apot = [sp.Function('A%d' % i)(*xs) for i in range(3)]
Vv = [sp.diff(Apot[2], x2) - sp.diff(Apot[1], x3),
      sp.diff(Apot[0], x3) - sp.diff(Apot[2], x1),
      sp.diff(Apot[1], x1) - sp.diff(Apot[0], x2)]           # V = curl A, div V = 0
bf = sp.Function('b')(w)
S = sp.Matrix(3, 3, lambda i, j: (sp.diff(Vv[j], xs[i]) + sp.diff(Vv[i], xs[j]))/2)
lap = lambda f: sum(sp.diff(f, xx, 2) for xx in xs)
LV = sp.zeros(4, 4)                   # index 0 = w, 1..3 = x_i
for i in range(3):
    for j in range(3):
        LV[i+1, j+1] = sp.diff(bf, w)*S[i, j]
    LV[0, i+1] = LV[i+1, 0] = -bf/2*lap(Vv[i])
Y = (w, x1, x2, x3)
check("TT: div V = 0 for V = curl A", sum(sp.diff(Vv[i], xs[i]) for i in range(3)))
check("TT: trace of L_b V = 0", LV.trace())
check("TT: divergence of L_b V (all four components) = 0",
      sp.Matrix([sum(sp.diff(LV[a, bb], Y[a]) for a in range(4)) for bb in range(4)]))
check("TT: Delta V_i = 2 d_j S_ij for divergence-free V (Newton decoder input)",
      sp.Matrix([lap(Vv[i]) - 2*sum(sp.diff(S[i, j], xs[j]) for j in range(3)) for i in range(3)]))
norm2 = sum(LV[a, bb]**2 for a in range(4) for bb in range(4))
check("TT: |L_b V|^2 = b'^2 S:S + b^2 |Delta V|^2 / 2",
      norm2 - (sp.diff(bf, w)**2*sum(S[i, j]**2 for i in range(3) for j in range(3)) + bf**2*sum(lap(Vv[i])**2 for i in range(3))/2))
astar = sp.symbols('a_*', positive=True)
A0bar = -astar*sp.diag(-3, 1, 1, 1)
check("TT: cross contraction A0bar : L_b V = 0", sum(A0bar[a, bb]*LV[a, bb] for a in range(4) for bb in range(4)))
check("TT: residual without mixed block = b' Delta V_i/2 (so the mixed block is needed)",
      sp.Matrix([sum(sp.diff((LV[a, i+1] if a > 0 else 0), Y[a]) for a in range(4)) - sp.diff(bf, w)*lap(Vv[i])/2 for i in range(3)]))

# ============================================================ 2. conformal constraints in 4 spatial dims
y = sp.symbols('y1:5', real=True)
phi = sp.Function('phi')(*y)
n = 4
hm = phi**2*sp.eye(n)
hinv = hm.inv()
Gam = [[[sum(hinv[a, dd]*(sp.diff(hm[dd, bb], y[c]) + sp.diff(hm[dd, c], y[bb]) - sp.diff(hm[bb, c], y[dd]))
             for dd in range(n))/2 for c in range(n)] for bb in range(n)] for a in range(n)]


def ricci(a, bb):
    return sp.simplify(sum(sp.diff(Gam[c][a][bb], y[c]) - sp.diff(Gam[c][a][c], y[bb])
                           + sum(Gam[c][c][dd]*Gam[dd][a][bb] - Gam[c][bb][dd]*Gam[dd][a][c] for dd in range(n))
                           for c in range(n)))


Rscal = sp.simplify(sum(hinv[a, a]*ricci(a, a) for a in range(n)))
lap4 = sum(sp.diff(phi, yy, 2) for yy in y)
check("Lich: R(phi^2 delta) = -6 phi^-3 Delta phi in four dimensions", Rscal + 6*lap4/phi**3)
# momentum constraint for K = phi^-2 Abar with Abar symmetric tracefree (generic entries)
Ab = sp.Matrix(4, 4, lambda i, j: sp.Function('a%d%d' % (min(i, j), max(i, j)))(*y))
Ab[3, 3] = -(Ab[0, 0] + Ab[1, 1] + Ab[2, 2])
Kt = Ab/phi**2
divK = []
for bb in range(n):
    s_ = 0
    for a in range(n):
        for c in range(n):
            cov = sp.diff(Kt[a, bb], y[c]) - sum(Gam[dd][c][a]*Kt[dd, bb] + Gam[dd][c][bb]*Kt[a, dd] for dd in range(n))
            s_ += hinv[a, c]*cov
    divK.append(sp.simplify(s_ - sum(sp.diff(Ab[a, bb], y[a]) for a in range(n))/phi**4))
check("Lich: div_h(phi^-2 Abar) = phi^-4 div_delta Abar (n = 4, Abar tracefree)", sp.Matrix(divK))
tau_, Lc, th_ = sp.symbols('tau_* L vartheta_*', positive=True)
qq = sp.symbols('q', positive=True)
Kfull = Kt + tau_/4*phi**2*sp.eye(4)
trK = sp.simplify((hinv*Kfull).trace())
check("Lich: tr_h K = tau_*", trK - tau_)
K2 = sp.simplify(sum(hinv[a, a]*hinv[bb, bb]*Kfull[a, bb]**2 for a in range(4) for bb in range(4)))
q_ab = sum(Ab[a, bb]**2 for a in range(4) for bb in range(4))
check("Lich: |K|_h^2 = phi^-8 |Abar|^2 + tau^2/4", K2 - (q_ab/phi**8 + tau_**2/4))
ham = (-6*lap4/phi**3) + trK**2 - (q_ab/phi**8 + tau_**2/4) + 12/Lc**2
kap = sp.Rational(3, 4)*tau_**2 + 12/Lc**2
check("Lich: phi^3 x Hamiltonian residual = -6 Delta phi + kappa phi^3 - q phi^-5", sp.expand(phi**3*ham - (-6*lap4 + kap*phi**3 - q_ab/phi**5)))
ast = 1/(Lc*sp.sin(th_))
taus = -4/Lc*sp.cot(th_)
check("Lich: kappa_* = (3/4)tau_*^2 + 12/L^2 = 12 a_*^2", sp.simplify(kap.subs(tau_, taus) - 12*ast**2))
# barrier facts: phi = 1 subsolution, M = (sup q/kappa)^(1/8) supersolution; derivative (6.8) positive
pp, Q_, kk = sp.symbols('p Q kappa', positive=True)
check("Lich: d/dphi(kappa phi^3 - q phi^-5) = 3 kappa phi^2 + 5 q phi^-6", sp.diff(kk*pp**3 - Q_*pp**-5, pp) - (3*kk*pp**2 + 5*Q_*pp**-6))
check("Lich: phi^3 - phi^-5 >= 3(phi - 1) for phi >= 1 (difference has nonneg. derivative, zero at 1)",
      bool(sp.simplify(sp.diff(pp**3 - pp**-5 - 3*(pp - 1), pp) - (3*pp**2 + 5*pp**-6 - 3)) == 0))
# linearised constraint (7.6)
phit = sp.Function('phit')(sp.Symbol('t'))
qt = sp.Function('qt')(sp.Symbol('t'))
expr = kk*phit**3 - qt*phit**-5
check("(7.6) d/dt(kappa phi^3 - q phi^-5) = (3kappa phi^2 + 5 q phi^-6) phidot - qdot phi^-5",
      sp.diff(expr, sp.Symbol('t')) - ((3*kk*phit**2 + 5*qt*phit**-6)*sp.diff(phit, sp.Symbol('t')) - sp.diff(qt, sp.Symbol('t'))*phit**-5))

# ============================================================ 3. Kasner map (1.2)-(1.3), (4.9), range
nu, c = sp.symbols('nu c', positive=True)
b11, b22, b12, b13, b23 = sp.symbols('b11 b22 b12 b13 b23', real=True)
B = sp.Matrix([[b11, b12, b13], [b12, b22, b23], [b13, b23, -b11 - b22]])
chi = sp.sqrt(1 + sp.Rational(4, 3)*(B*B).trace())
Pw = sp.Rational(1, 4) - sp.Rational(3, 4)/chi
Pp = sp.eye(3)/4 + (sp.eye(3)/4 + B)/chi
check("Kasner: tr P = P_w + tr P_perp = 1 (generic tracefree B)", Pw + Pp.trace() - 1)
check("Kasner: tr P^2 = 1", sp.simplify(Pw**2 + (Pp*Pp).trace() - 1))
check("Kasner (1.3): chi (P_perp - I/4) - I/4 = B and chi (1 - 4 P_w) = 3", (chi*(Pp - sp.eye(3)/4) - sp.eye(3)/4 - B).applyfunc(sp.simplify).norm() + sp.simplify(chi*(1 - 4*Pw) - 3))
Binv = (3*Pp + (Pw - 1)*sp.eye(3))/(1 - 4*Pw)
check("Kasner (4.9): inverse (3P_perp + (P_w - 1)I)/(1 - 4P_w) returns B", Binv.applyfunc(sp.simplify) - B)
Sst = sp.Matrix(3, 3, lambda i, j: sp.Symbol('S%d%d' % (min(i, j), max(i, j))))
check("Kasner: B = -2 nu S/c^2 <=> S = -(c^2/2nu) B (so S = -(c^2/2nu)(3P_perp+(P_w-1)I)/(1-4P_w))",
      (-c**2/(2*nu))*(-2*nu*Sst/c**2) - Sst)
# surjectivity on the block-Kasner set: generic symmetric P_perp with the two constraints
pw_ = sp.symbols('P_w', real=True)
p11, p22, p12, p13, p23 = sp.symbols('p11 p22 p12 p13 p23', real=True)
p33 = 1 - pw_ - p11 - p22
Pperp = sp.Matrix([[p11, p12, p13], [p12, p22, p23], [p13, p23, p33]])
Bp = (3*Pperp + (pw_ - 1)*sp.eye(3))/(1 - 4*pw_)
cons = (Pperp*Pperp).trace() - (1 - pw_**2)          # = 0 on the Kasner set
check("Kasner surj.: inverse image is tracefree", sp.simplify(Bp.trace()))
lhs = 1 + sp.Rational(4, 3)*(Bp*Bp).trace() - 9/(1 - 4*pw_)**2
check("Kasner surj.: 1 + (4/3) tr B'^2 - 9/(1-4P_w)^2 = (4/3)*9/(1-4P_w)^2 * constraint",
      sp.simplify(lhs - sp.Rational(4, 3)*9*cons/(1 - 4*pw_)**2))
chi_p = 3/(1 - 4*pw_)
check("Kasner surj.: forward map at chi = 3/(1-4P_w) returns (P_w, P_perp)",
      sp.simplify(sp.Rational(1, 4) - sp.Rational(3, 4)/chi_p - pw_) + (sp.eye(3)/4 + (sp.eye(3)/4 + Bp)/chi_p - Pperp).applyfunc(sp.simplify).norm())
# range P_w >= -1/2: (1-P_w)^2 <= 3(1-P_w^2)  <=>  (1-P_w)(1+2P_w)... check the factorisation
check("Kasner range: 3(1-P_w^2) - (1-P_w)^2 = 2(1-P_w)(1+2P_w)", sp.expand(3*(1 - pw_**2) - (1 - pw_)**2 - 2*(1 - pw_)*(1 + 2*pw_)))
# (4.11) expansion
eps = sp.symbols('epsilon')
Bs = eps*B
chis = sp.sqrt(1 + sp.Rational(4, 3)*(Bs*Bs).trace())
zz = (B*B).trace()*eps**2
Pws = sp.series(sp.Rational(1, 4) - sp.Rational(3, 4)/chis, eps, 0, 4).removeO()
check("(4.11) P_w = -1/2 + z/2 + O(B^4)", sp.expand(Pws - (-sp.Rational(1, 2) + zz/2)))
Pps = (sp.eye(3)/4 + (sp.eye(3)/4 + Bs)/chis).applyfunc(lambda e: sp.series(e, eps, 0, 3).removeO())
check("(4.11) P_perp = I/2 + B - z I/6 + O(B^3)", (Pps - (sp.eye(3)/2 + Bs - zz*sp.eye(3)/6)).applyfunc(sp.expand))
check("(4.11) tr(P0 + diag(0,B))^2 = 1 + z", sp.expand((sp.Rational(1, 4) + sum((sp.Rational(1, 2)*sp.eye(3) + B)[i, i]**2 for i in range(3))
                                                          + 2*sum(B[i, j]**2 for i in range(3) for j in range(i+1, 3))) - (1 + zz.subs(eps, 1))))

# ============================================================ 4. homogeneous Einstein metric (4.2)-(4.7), (4.13)
lamb = sp.symbols('lambda', positive=True)
p = sp.symbols('p1:5', real=True)
th = 4*lamb/Lc
# log a_A from (4.2): (1/4) log sin th + (p_A - 1/4) log tan(th/2) + const
loga = [sp.log(sp.sin(th))/4 + (p[A_] - sp.Rational(1, 4))*sp.log(sp.tan(th/2)) for A_ in range(4)]
HA = [sp.simplify(sp.diff(la, lamb)) for la in loga]
check("(4.4) H_A = (1/L)cot + (4/L)(p_A - 1/4)csc", sp.Matrix([sp.simplify(HA[A_] - (sp.cot(th)/Lc + 4/Lc*(p[A_] - sp.Rational(1, 4))/sp.sin(th))) for A_ in range(4)]))
# direct Ricci of g = -dl^2 + sum a_A^2 dy_A^2 with generic a_A(l); then express through H_A = a_A'/a_A
af = [sp.Function('a%d' % A_)(lamb) for A_ in range(4)]
coords = (lamb,) + tuple(sp.symbols('Y1:5', real=True))
g5 = sp.diag(-1, *[af[A_]**2 for A_ in range(4)])
g5i = g5.inv()
G5 = [[[sum(g5i[a, dd]*(sp.diff(g5[dd, bb], coords[cc]) + sp.diff(g5[dd, cc], coords[bb]) - sp.diff(g5[bb, cc], coords[dd]))
            for dd in range(5))/2 for cc in range(5)] for bb in range(5)] for a in range(5)]


def ric5(a, bb):
    return sp.simplify(sum(sp.diff(G5[cc][a][bb], coords[cc]) - sp.diff(G5[cc][a][cc], coords[bb])
                           + sum(G5[cc][cc][dd]*G5[dd][a][bb] - G5[cc][bb][dd]*G5[dd][a][cc] for dd in range(5))
                           for cc in range(5)))


Hs = sp.symbols('H1:5', real=True)
Hd = sp.symbols('Hd1:5', real=True)
toH = {}
for A_ in range(4):
    toH[sp.Derivative(af[A_], (lamb, 2))] = af[A_]*(Hd[A_] + Hs[A_]**2)
    toH[sp.Derivative(af[A_], lamb)] = af[A_]*Hs[A_]
Ric = sp.zeros(5, 5)
for i in range(5):
    for j in range(i, 5):
        Ric[i, j] = Ric[j, i] = sp.simplify(ric5(i, j).subs(toH))
# mixed Ricci R^a_b + 4/L^2 delta^a_b in terms of H, Hd
mixed = (g5i*Ric).applyfunc(sp.simplify) + 4/Lc**2*sp.eye(5)
C0, S0 = sp.symbols('C0 S0', real=True)          # cot(th), csc(th), th = 4 lambda/L
Hexpr = [C0/Lc + 4/Lc*(p[A_] - sp.Rational(1, 4))*S0 for A_ in range(4)]
dC0, dS0 = -4/Lc*S0**2, -4/Lc*S0*C0                 # d/dlambda of cot(4l/L), csc(4l/L)
Hdexpr = [sp.diff(Hexpr[A_], C0)*dC0 + sp.diff(Hexpr[A_], S0)*dS0 for A_ in range(4)]
check("(4.4) derivative rules d cot(4l/L)/dl = -(4/L)csc^2, d csc/dl = -(4/L)csc cot",
      sp.simplify(sp.diff(sp.cot(th), lamb) + 4/Lc/sp.sin(th)**2) + sp.simplify(sp.diff(1/sp.sin(th), lamb) + 4/Lc*sp.cos(th)/sp.sin(th)**2))
subsH = {Hs[A_]: Hexpr[A_] for A_ in range(4)}
subsH.update({Hd[A_]: Hdexpr[A_] for A_ in range(4)})
quad = sum(pi**2 for pi in p[:3]) + (1 - p[0] - p[1] - p[2])**2 - 1
lin = {p[3]: 1 - p[0] - p[1] - p[2]}
ok = True
needs_quad = False
for i in range(5):
    for j in range(5):
        e = sp.expand(mixed[i, j].subs(subsH).subs(lin))
        e = sp.expand(e.subs(S0**2, 1 + C0**2))
        e = sp.expand(sp.rem(sp.Poly(e, S0).as_expr(), S0**2 - 1 - C0**2, S0)) if e.has(S0) else e
        if e != 0:
            r_ = sp.rem(sp.expand(e*Lc**2), sp.expand(quad), p[0])
            if sp.expand(r_) != 0:
                ok = False
            else:
                needs_quad = True
check("(4.5) Ric(g_S) = -(4/L^2) g_S for all Kasner data (sum p = sum p^2 = 1)", ok)
check("(4.5) the quadratic Kasner constraint is actually used (some component vanishes only modulo it)", bool(needs_quad))
# Kretschmann for the diagonal metric, in terms of H, Hd
def riem(a, bb, cc, dd):
    return (sp.diff(G5[a][dd][bb], coords[cc]) - sp.diff(G5[a][cc][bb], coords[dd])
            + sum(G5[a][cc][e]*G5[e][dd][bb] - G5[a][dd][e]*G5[e][cc][bb] for e in range(5)))


Kret = 0
for a in range(5):
    for bb in range(5):
        for cc in range(5):
            for dd in range(cc + 1, 5):
                val = riem(a, bb, cc, dd)
                if val != 0:
                    val = sp.simplify(val.subs(toH))
                    if val != 0:
                        Kret += 2*g5[a, a]*g5i[bb, bb]*g5i[cc, cc]*g5i[dd, dd]*val**2
Kret = sp.simplify(Kret)
Kformula = 4*sum((Hd[A_] + Hs[A_]**2)**2 for A_ in range(4)) + 4*sum((Hs[A_]*Hs[B_])**2 for A_ in range(4) for B_ in range(A_ + 1, 4))
check("Kretschmann of diagonal Bianchi-I: 4 sum (a''/a)^2 + 4 sum_{A<B} (H_A H_B)^2", sp.expand(Kret - Kformula))
lim_claim = 4*(sum(p[A_]**2*(p[A_] - 1)**2 for A_ in range(4)) + sum(p[A_]**2*p[B_]**2 for A_ in range(4) for B_ in range(A_ + 1, 4)))
# lambda^4 K as lambda -> 0: C0 ~ L/(4 lambda), S0 ~ L/(4 lambda); exact limit by series in lambda
lam_small = sp.symbols('ls', positive=True)
KH = Kformula.subs(subsH)
KH = KH.subs({C0: sp.cot(4*lam_small/Lc), S0: 1/sp.sin(4*lam_small/Lc)})
lim_val = sp.limit(sp.expand(KH*lam_small**4).subs(Lc, 1).subs(lin), lam_small, 0)
check("(4.13) lim lambda^4 R_abcd R^abcd = 4[sum p^2(p-1)^2 + sum_{A<B} p_A^2 p_B^2] (exact limit, sum p = 1 used)",
      sp.expand(lim_val - lim_claim.subs(lin)))
# volume, anisotropy (4.6); Hamiltonian (3.4)
v0, chiS = sp.symbols('v_0 chi', positive=True)
V_S = chiS*v0*sp.sin(th)
EA = [sp.simplify(HA[A_] - sum(HA)/4) for A_ in range(4)]
check("(4.6) theta = sum H_A = (4/L) cot(4 lambda/L) given sum p = 1",
      sp.simplify((sum(HA) - 4/Lc*sp.cot(th)).subs(p[3], 1 - p[0] - p[1] - p[2])))
check("(4.6) V' = theta V for V = chi v0 sin(4 lambda/L)", sp.simplify(sp.diff(V_S, lamb) - 4/Lc*sp.cot(th)*V_S))
QA = [sp.simplify((V_S*EA[A_]).subs(p[3], 1 - p[0] - p[1] - p[2])) for A_ in range(4)]
check("(4.6) Q_A = V E_A = (4 chi v0/L)(p_A - 1/4) (constant)", sp.Matrix([sp.simplify(QA[A_] - (4*chiS*v0/Lc*(p[A_] - sp.Rational(1, 4))).subs(p[3], 1 - p[0] - p[1] - p[2])) for A_ in range(4)]))
# with Kasner data from B: Q_w = -3 v0/L, Q_perp = (v0/L)(I + 4B); tr Q^2 = 12 v0^2 chi^2/L^2
Qw = 4*chi*v0/Lc*(Pw - sp.Rational(1, 4))
Qp = 4*chi*v0/Lc*(Pp - sp.eye(3)/4)
check("(4.6) Q_S = (v0/L) diag(-3, I + 4B)", sp.simplify(Qw + 3*v0/Lc) + (Qp - v0/Lc*(sp.eye(3) + 4*B)).applyfunc(sp.simplify).norm())
check("(4.6) tr Q_S^2 = 12 v0^2 chi^2 / L^2", sp.simplify(Qw**2 + (Qp*Qp).trace() - 12*v0**2*chi**2/Lc**2))
check("(3.4) flat slices: tr Q^2 = (3/4) V'^2 + (12/L^2) V^2 for V = chi v0 sin",
      sp.simplify(12*v0**2*chiS**2/Lc**2 - (sp.Rational(3, 4)*sp.diff(V_S, lamb)**2 + 12/Lc**2*V_S**2)))
# det h_* and v0 = r_h^4/(2 L^4)
rh, sst, cc_ = sp.symbols('r_h s_* c', positive=True)
xx = 2*cc_*sst/Lc
hstar_det = (rh/Lc)**8*sp.cos(xx)**2/sp.sin(xx)*sp.sin(xx)**3
check("(4.6) det h_* = ((r_h^4/(2L^4)) sin(4 c s_*/L))^2 (both factors positive for 0 < s_* < pi L/(8c))", sp.simplify(sp.expand_trig(hstar_det - (rh**4/(2*Lc**4)*sp.sin(2*xx))**2)))
lim_claim = 4*(sum(p[A_]**2*(p[A_] - 1)**2 for A_ in range(4)) + sum(p[A_]**2*p[B_]**2 for A_ in range(4) for B_ in range(A_ + 1, 4)))
check("(4.13) equals 9/2 at rest (P = (-1/2, 1/2, 1/2, 1/2))",
      lim_claim.subs({p[0]: -sp.Rational(1, 2), p[1]: sp.Rational(1, 2), p[2]: sp.Rational(1, 2), p[3]: sp.Rational(1, 2)}) - sp.Rational(9, 2))
check("(4.13) w-term alone at P_w = 1/4: 4 p^2 (p-1)^2 = 9/64", 4*sp.Rational(1, 16)*sp.Rational(9, 16) - sp.Rational(9, 64))
Pother = [sp.Rational(1, 2) - pi for pi in p]
check("(4.14) P_other = I/2 - P is again Kasner (sum = 1, sum sq = 1) given P Kasner",
      sp.simplify((sum(Pother) - 1).subs(p[3], 1 - p[0] - p[1] - p[2])) +
      sp.rem(sp.expand((sum(x**2 for x in Pother) - 1).subs(p[3], 1 - p[0] - p[1] - p[2])), sp.expand(quad), p[0]))

# ============================================================ 5. homogeneous specialisation (7.1)-(7.2), (6.3), (2.3)-(2.6)
betas = 8*astar*nu/c**2
Bmat = -2*nu*Sst/c**2
Abar_h = sp.diag(3*astar, *[0, 0, 0]) + sp.Matrix(sp.BlockDiagMatrix(sp.Matrix([[0]]), -astar*sp.eye(3) + betas*Sst))
Abar_claim = -astar*sp.Matrix(sp.BlockDiagMatrix(sp.Matrix([[-3]]), sp.eye(3) + 4*Bmat))
check("(7.1) Abar = -a_* diag(-3, I + 4B) for V = S xi, b(w) = w", (Abar_h - Abar_claim).applyfunc(sp.simplify))
Str = Sst.subs(Sst[2, 2], -Sst[0, 0] - Sst[1, 1])
Abc = Abar_claim.subs(Sst[2, 2], -Sst[0, 0] - Sst[1, 1])
qh = sum(Abc[i, j]**2 for i in range(4) for j in range(4))
chih = sp.sqrt(1 + sp.Rational(4, 3)*((-2*nu*Str/c**2)**2).trace())
check("(7.1) q = kappa_* chi^2 with kappa_* = 12 a_*^2", sp.simplify(qh - 12*astar**2*chih**2))
check("(7.1) phi = chi^(1/4) solves kappa phi^3 = q phi^-5", sp.simplify(12*astar**2*chih**(sp.Rational(3, 4)) - qh*chih**(-sp.Rational(5, 4))))
Dg = sp.Matrix(sp.BlockDiagMatrix(sp.Matrix([[-3]]), sp.eye(3) + 4*(-2*nu*Str/c**2)))
check("(7.2) K^sharp = phi^-4 Abar + tau/4 I = -(a_*/chi) diag(-3, I+4B) + tau/4 I (phi^4 = chi)",
      ((chih**sp.Rational(1, 4))**-4*Abc + tau_/4*sp.eye(4) - (-(astar/chih)*Dg + tau_/4*sp.eye(4))).applyfunc(sp.simplify))
rc, fcs = sp.symbols('r_c f_c', positive=True)
nu_c = c*Lc*rc*sp.sqrt(fcs)/(4*rh)
rref2 = rh**2*sp.sin(th_/2)
beta_alt = rc*sp.sqrt(fcs)*rh**3/(c*rref2*sp.sqrt(rh**4 - rref2**2))
check("(6.3) beta_* = 8 a_* nu/c^2 equals r_c sqrt(f_c) r_h^3/(c r_ref^2 sqrt(r_h^4 - r_ref^4))",
      sp.simplify((8*nu_c/(c**2*Lc*sp.sin(th_)) - beta_alt).subs(th_, sp.Rational(7, 10))) + sp.simplify((8*nu_c/(c**2*Lc*sp.sin(th_)) - beta_alt).subs(th_, sp.Rational(3, 2))))
rr_ = sp.symbols('r', positive=True)
Hf = sp.Function('H')(rr_)
sig = sp.symbols('sigma')
Jt = (rr_*(rr_**4 - rh**4)*sp.diff(Hf, rr_) + Lc*rc*sp.sqrt(fcs)*rr_**3)*sig
radial_eq = {sp.Derivative(Hf, (rr_, 2)): sp.solve(sp.diff(rr_*(rr_**4 - rh**4)*sp.diff(Hf, rr_), rr_) + 3*Lc*rc*sp.sqrt(fcs)*rr_**2,
                                                    sp.Derivative(Hf, (rr_, 2)))[0]}
check("(2.4) d_r J = 0 using (2.3)", sp.simplify(sp.diff(Jt, rr_).subs(radial_eq)))
Hp_reg = -Lc*rc*sp.sqrt(fcs)*(rr_**3 - rh**3)/(rr_*(rr_**4 - rh**4))
check("(2.5) regular H' gives J = L r_c sqrt(f_c) r_h^3 sigma", sp.simplify(Jt.subs(sp.Derivative(Hf, rr_), Hp_reg) - Lc*rc*sp.sqrt(fcs)*rh**3*sig))
Jval = Lc*rc*sp.sqrt(fcs)*rh**3*Sst[0, 1]/c
C5, zeta_c = sp.symbols('C_5 zeta_c', positive=True)
check("(2.6)=>(1.1) p[1] = -J/(2 r_h^4) = -2 nu S/c^2", sp.simplify(-Jval/(2*rh**4) + 2*nu_c*Sst[0, 1]/c**2))
dT = -C5/(Lc*rc**4*sp.sqrt(fcs))*Jval
check("(2.6)=>(1.1) dT^TF/(eps+p) = -2 nu S/c^2 with eps + p = C_5 zeta_c c/(2 nu), zeta_c = (r_h/r_c)^3",
      sp.simplify(dT/(C5*(rh/rc)**3*c/(2*nu_c)) + 2*nu_c*Sst[0, 1]/c**2))
# (7.7) evolution defect: TF_h(K) = phi^-2 Abar and TF_h(pure trace) = 0
TFh = lambda Km: Km - (hinv*Km).trace()/4*hm
check("(7.7) TF_h(K) = K - (tau/4) h = phi^-2 Abar", (TFh(Kfull) - Kt).applyfunc(sp.simplify))
check("(7.7) TF_h(d_t h) = 0 since d_t h = 2 phi phidot delta is pure trace", (TFh(sp.Symbol('pd')*2*phi*sp.eye(4))).applyfunc(sp.simplify))
# (7.3a) curl(-(1/3) xi x (S xi)) = S xi for tracefree symmetric S
Sx = Str
xi = sp.Matrix(xs)
Acal = -sp.Rational(1, 3)*xi.cross(Sx*xi)
curlA = sp.Matrix([sp.diff(Acal[2], x2) - sp.diff(Acal[1], x3), sp.diff(Acal[0], x3) - sp.diff(Acal[2], x1), sp.diff(Acal[1], x1) - sp.diff(Acal[0], x2)])
check("(7.3a) curl(-(1/3) xi x S xi) = S xi (tr S = 0)", (curlA - Sx*xi).applyfunc(sp.expand))

# ============================================================ 6. Newton decoder: Fourier identity and a numerical kernel check
k1, k2, k3 = sp.symbols('k1 k2 k3', real=True)
kv = sp.Matrix([k1, k2, k3])
Vh = sp.Matrix(sp.symbols('V1:4'))
Vh_perp = Vh - kv*(kv.T*Vh)[0]/(kv.T*kv)[0]            # divergence-free Fourier amplitude
Sh = (sp.I/2)*(kv*Vh_perp.T + Vh_perp*kv.T)
Nh = (2/(-(kv.T*kv)[0]))*(sp.I*Sh*kv)
check("decoder: 2 Delta^-1 d_j S_ij returns V in Fourier (k.V = 0)", (Nh - Vh_perp).applyfunc(sp.simplify))
# numerical: V = curl(0,0,psi), psi = exp(-|x|^2); N(S)_i(xi) = (1/2pi) int S_ij(eta)(xi-eta)_j/|xi-eta|^3
from scipy import integrate
import numpy as np
psi = sp.exp(-(x1**2 + x2**2 + x3**2))
Vn = [sp.diff(psi, x2), -sp.diff(psi, x1), 0]
Sn_ = [[sp.lambdify(xs, (sp.diff(Vn[j], xs[i]) + sp.diff(Vn[i], xs[j]))/2, 'numpy') for j in range(3)] for i in range(3)]
Vf = [sp.lambdify(xs, Vn[i], 'numpy') for i in range(3)]
pt = np.array([0.3, -0.2, 0.1])


def decoded(i):
    # spherical coordinates about the evaluation point: (xi - eta) = -rho*om, measure rho^2 d rho d om
    def integrand(rho, th_, ph_):
        om = np.array([np.sin(th_)*np.cos(ph_), np.sin(th_)*np.sin(ph_), np.cos(th_)])
        et = pt + rho*om
        return sum(Sn_[i][j](*et)*(-om[j]) for j in range(3))*np.sin(th_)
    val, err = integrate.tplquad(integrand, 0, 2*np.pi, 0, np.pi, 0, 6.0, epsabs=1e-9, epsrel=1e-9)
    return val/(2*np.pi)


dec = [decoded(i) for i in range(3)]
exact = [Vf[i](*pt) for i in range(3)]
err = max(abs(dec[i] - exact[i]) for i in range(3))
check("decoder: Newton kernel (6.13) recovers V numerically at a point (Gaussian curl field), max err %.1e" % err, err, tol=1e-6)

# ============================================================ 7. slab comparator (S1)-(S9)
kq, Ls, yy = sp.symbols('k L y', positive=True)
Qh = sp.cosh(kq*(Ls - yy))/sp.cosh(kq*Ls)
check("(S1) Q = cosh(k(L-y))/cosh(kL) S solves Q'' = k^2 Q, Q(0)=1, Q'(L)=0",
      sp.simplify(sp.diff(Qh, yy, 2) - kq**2*Qh) + sp.simplify(Qh.subs(yy, 0) - 1) + sp.simplify(sp.diff(Qh, yy).subs(yy, Ls)))
check("(S1) -d_y Q|_0 = k tanh(kL)", sp.simplify(-sp.diff(Qh, yy).subs(yy, 0) - kq*sp.tanh(kq*Ls)))
kap_ = sp.symbols('kappa', positive=True)
ser = sp.series(kap_*kq**3*sp.tanh(Ls*kq), kq, 0, 9).removeO()
check("(S3) damping k^3 tanh(Lk) = L k^4 - L^3 k^6/3 + O(k^8) (times kappa)", sp.expand(ser - (kap_*Ls*kq**4 - kap_*Ls**3*kq**6/3 + 2*kap_*Ls**5*kq**8/15)))
check("(S3) L = nu/c gives kappa = 3 nu^2/(2c) from kappa L = 3 nu^3/(2 c^2)", sp.simplify(sp.Rational(3, 2)*nu**2/c*(nu/c) - 3*nu**3/(2*c**2)))
a_, b_ = sp.symbols('a b', positive=True)
mu = kq*sp.sqrt(b_/a_)
qmin = sp.cosh(mu*(Ls - yy))/sp.cosh(mu*Ls)
energy = sp.integrate(sp.expand((a_*sp.diff(qmin, yy)**2 + b_*kq**2*qmin**2).rewrite(sp.exp)), (yy, 0, Ls))
check("(S5) constant coefficients: min energy = sqrt(ab) k tanh(L k sqrt(b/a))", sp.simplify(energy.rewrite(sp.exp) - (sp.sqrt(a_*b_)*kq*sp.tanh(Ls*mu)).rewrite(sp.exp)))
# layer transfer (S8): composing two layers of the same medium equals one layer of total thickness
z_, L1, L2 = sp.symbols('z L1 L2', positive=True)
Zi = sp.sqrt(a_*b_)*kq
sj = lambda Lj: Lj*kq*sp.sqrt(b_/a_)
Tj = lambda zz_, Lj: (Zi*sp.tanh(sj(Lj)) + zz_)/(1 + (zz_/Zi)*sp.tanh(sj(Lj)))
check("(S8) T(T(0;L2);L1) = T(0;L1+L2) for one medium (tanh addition)", sp.simplify((Tj(Tj(0, L2), L1) - Tj(0, L1 + L2)).rewrite(sp.exp)))
# direct: two-layer Neumann problem with different media equals the composition
a1, b1, a2, b2 = sp.symbols('a1 b1 a2 b2', positive=True)
m1, m2 = kq*sp.sqrt(b1/a1), kq*sp.sqrt(b2/a2)
Z1, Z2 = sp.sqrt(a1*b1)*kq, sp.sqrt(a2*b2)*kq
# lower layer (thickness L2, Neumann at bottom): input response Z2 tanh(m2 L2); upper layer transfers it
comp = (Z1*sp.tanh(m1*L1) + Z2*sp.tanh(m2*L2))/(1 + (Z2*sp.tanh(m2*L2)/Z1)*sp.tanh(m1*L1))
# direct solution: q1 = cosh(m1 y) + C sinh(m1 y) on [0,L1] with q1(0)=1; response = -a1 q1'(0) ... match flux and value at L1
Cc = sp.symbols('Cc')
q1 = sp.cosh(m1*yy) + Cc*sp.sinh(m1*yy)
# at the interface the lower layer imposes a1 q1'(L1) = -Z2 tanh(m2 L2) q1(L1)
Csol = sp.solve(sp.Eq(a1*sp.diff(q1, yy).subs(yy, L1), -Z2*sp.tanh(m2*L2)*q1.subs(yy, L1)), Cc)[0]
resp = -a1*sp.diff(q1, yy).subs(yy, 0).subs(Cc, Csol)
numchk = [(resp - comp).subs({a1: 1.3, b1: 0.7, a2: 2.1, b2: 0.4, kq: 1.7, L1: 0.6, L2: 1.1}).evalf(),
          (resp - comp).subs({a1: 0.5, b1: 2.7, a2: 1.1, b2: 3.4, kq: 0.3, L1: 2.6, L2: 0.2}).evalf()]
check("(S8) two different layers: transfer formula equals the direct Neumann solve (2 numeric samples)", max(abs(x) for x in numchk), tol=1e-12)
DD, Ee, Cg, cst = sp.symbols('D E C_GN c_*', positive=True)
fmax = sp.Max(0)
Dcrit = (sp.Rational(9, 10)*Cg**3*Ee**sp.Rational(6, 5)/(cst/2))**5
fvalue = Cg**3*Ee**sp.Rational(6, 5)*Dcrit**sp.Rational(9, 5) - cst/2*Dcrit**2
check("(S7) max_D [C^3 E^(6/5) D^(9/5) - (c/2) D^2] = (1/10)(9/5)^9 C^30 c^-9 E^12",
      sp.simplify(fvalue - sp.Rational(1, 10)*sp.Rational(9, 5)**9*Cg**30*cst**-9*Ee**12))
check("(S7) the critical point is where the D-derivative vanishes",
      sp.simplify(sp.diff(Cg**3*Ee**sp.Rational(6, 5)*DD**sp.Rational(9, 5) - cst/2*DD**2, DD).subs(DD, Dcrit)))
check("GN exponent: Lambda^(3/2) between Lambda^0 and Lambda^(5/2) has theta = 3/5; cube gives E^(6/5) D^(9/5)",
      sp.Rational(3, 2) - sp.Rational(3, 5)*sp.Rational(5, 2) + (3*sp.Rational(2, 5) - sp.Rational(6, 5)) + (3*sp.Rational(3, 5) - sp.Rational(9, 5)))

# ============================================================ 8. Rindler shear sector (RESEARCH.md (2)-(33))
rho, ell, ct = sp.symbols('rho ell ct', positive=True)
rho_c = 2*ell
Rr = rho**2/(4*ell)
x0 = ct + rho_c*sp.log(rho/rho_c)
drho, dct = sp.symbols('drho dct')
dR = sp.diff(Rr, rho)*drho
dx0 = dct + sp.diff(x0, rho)*drho
check("(5) -(R/l)(dx0)^2 + 2 dx0 dR = -(rho/rho_c)^2 (c dt)^2 + d rho^2",
      sp.expand(-(Rr/ell)*dx0**2 + 2*dx0*dR - (-(rho/rho_c)**2*dct**2 + drho**2)))
rv, qv, wv = sp.symbols('r q w', positive=True)
ph = sp.Function('ph')(rv)
bessel_ode = sp.diff(ph, rv, 2) + sp.diff(ph, rv)/rv + (wv**2/rv**2 - qv**2)*ph
Zv = rv*sp.diff(ph, rv)
d2 = {sp.Derivative(ph, (rv, 2)): sp.solve(bessel_ode, sp.Derivative(ph, (rv, 2)))[0]}
Zp = sp.diff(Zv, rv).subs(d2)
check("(14) Z' = (q^2 r - w^2/r) phi for Z = r phi'", sp.simplify(Zp - (qv**2*rv - wv**2/rv)*ph))
Zpp = sp.diff(sp.diff(Zv, rv).subs(d2), rv).subs(d2)
check("(13) Z'' + (q^2r^2+w^2)/(r(w^2-q^2r^2)) Z' + (w^2/r^2 - q^2) Z = 0",
      sp.simplify(Zpp + (qv**2*rv**2 + wv**2)/(rv*(wv**2 - qv**2*rv**2))*Zp + (wv**2/rv**2 - qv**2)*Zv))
# hydrodynamic pole: independent numerical root finding of I'_alpha(q) = 0 near alpha ~ -q^2/2
mp.mp.dps = 50
Fq = lambda al, qq_: (mp.besseli(al - 1, qq_) + mp.besseli(al + 1, qq_))/2
series_alpha = lambda qq_: -qq_**2/2 - 3*qq_**4/16 - 29*qq_**6/192 - mp.mpf(2843)*qq_**8/18432 - mp.mpf(392029)*qq_**10/2211840
worst_ratio = 0
for qq_ in [mp.mpf('0.05'), mp.mpf('0.1'), mp.mpf('0.2')]:
    root = mp.findroot(lambda al: Fq(al, qq_), series_alpha(qq_))
    err_ = abs(root - series_alpha(qq_))
    worst_ratio = max(worst_ratio, err_/qq_**12)
check("(27) five series coefficients: |alpha_root(q) - series(q)| / q^12 bounded (q = 0.05, 0.1, 0.2): max %.3f" % float(worst_ratio),
      bool(worst_ratio < 1))
nu_s, c_s, k_s = sp.symbols('nu c k', positive=True)
rc_ = 2*nu_s/c_s
qq = k_s*rc_
alpha_s = -qq**2/2 - 3*qq**4/16 - 29*qq**6/192
omega = sp.I*alpha_s*c_s/rc_          # w = i alpha, omega = c w / rho_c
check("(28) omega = -i nu k^2 - i(3 nu^3/2c^2)k^4 - i(29 nu^5/6 c^4)k^6",
      sp.expand(omega - (-sp.I*nu_s*k_s**2 - sp.I*3*nu_s**3/(2*c_s**2)*k_s**4 - sp.I*29*nu_s**5/(6*c_s**4)*k_s**6)))
# collision (29)-(33) by a different formulation: G = q I_{a+1}(q) + a I_a(q) = q I'_a(q)
G = lambda al, qq_: qq_*mp.besseli(al + 1, qq_) + al*mp.besseli(al, qq_)
Ga = lambda al, qq_: mp.diff(lambda u: G(u, qq_), al)
sol = mp.findroot([lambda al, qq_: G(al, qq_), lambda al, qq_: Ga(al, qq_)], (mp.mpf('-0.55'), mp.mpf('0.76')))
al_c, q_c = sol[0], sol[1]
check("(30)-(31) collision q_c = 0.778472800990330076180356446189 (independent formulation), diff %.1e" % float(abs(q_c - mp.mpf('0.778472800990330076180356446189'))),
      float(abs(q_c - mp.mpf('0.778472800990330076180356446189'))), tol=1e-25)
check("(31) alpha_c = -0.569714080972361784438457668663, diff %.1e" % float(abs(al_c + mp.mpf('0.569714080972361784438457668663'))),
      float(abs(al_c + mp.mpf('0.569714080972361784438457668663'))), tol=1e-25)
Fqd = mp.diff(lambda u: Fq(al_c, u), q_c)
Faa = mp.diff(lambda u: Fq(u, q_c), al_c, 2)
Cc_ = mp.sqrt(2*Fqd/Faa)
check("(32) F_q = 1.75035806101433995507814928965, diff %.1e" % float(abs(Fqd - mp.mpf('1.75035806101433995507814928965'))), float(abs(Fqd - mp.mpf('1.75035806101433995507814928965'))), tol=1e-20)
check("(32) F_aa = 5.00598854867858334954068222753, diff %.1e" % float(abs(Faa - mp.mpf('5.00598854867858334954068222753'))), float(abs(Faa - mp.mpf('5.00598854867858334954068222753'))), tol=1e-20)
check("(33) C = sqrt(2 F_q/F_aa) = 0.836244975595942847875560947195, diff %.1e" % float(abs(Cc_ - mp.mpf('0.836244975595942847875560947195'))),
      float(abs(Cc_ - mp.mpf('0.836244975595942847875560947195'))), tol=1e-20)
# argument-principle count: two zeros of F(., q) in a small disc around alpha_c for q slightly below and above q_c
def nzeros(qq_, rad=mp.mpf('0.02')):
    f = lambda al: Fq(al, qq_)
    fp = lambda al: mp.diff(f, al)
    integ = mp.quad(lambda t_: fp(al_c + rad*mp.expjpi(2*t_))/f(al_c + rad*mp.expjpi(2*t_))*rad*2j*mp.pi*mp.expjpi(2*t_), [0, 0.25, 0.5, 0.75, 1])
    return integ/(2j*mp.pi)
mp.mp.dps = 25
cnt_lo, cnt_hi = nzeros(q_c - mp.mpf('1e-4')), nzeros(q_c + mp.mpf('1e-4'))
check("collision: argument principle counts 2 zeros near alpha_c for q = q_c -/+ 1e-4 (%.6f, %.6f)" % (cnt_lo.real, cnt_hi.real),
      bool(abs(cnt_lo - 2) < 1e-6 and abs(cnt_hi - 2) < 1e-6))
mp.mp.dps = 40
# table rows: q = 0.5 purely damped; q = 1 complex pair
r05 = mp.findroot(lambda al: Fq(al, mp.mpf('0.5')), mp.mpf('-0.14'))
check("table q=0.5: w = -0.139933871958 i (alpha real), diff %.1e" % float(abs(r05 + mp.mpf('0.139933871958'))), float(abs(r05 + mp.mpf('0.139933871958'))), tol=1e-11)
r1 = mp.findroot(lambda al: Fq(al, mp.mpf(1)), mp.mpc('-0.6084', '-0.4309'))
w1 = 1j*r1
check("table q=1: w = 0.430856069761 - 0.608420333512 i, diff %.1e" % float(abs(w1 - mp.mpc('0.430856069761', '-0.608420333512'))),
      float(abs(w1 - mp.mpc('0.430856069761', '-0.608420333512'))), tol=1e-11)

print("\nsummary: %d checks, %d PASS, %d FAIL; %.0f s" % (len(res), sum(o for _, o in res), sum(not o for _, o in res), time.time() - T0))
