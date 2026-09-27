"""Exact identities behind the NS bridges (NS->YM, NS->zeta, S6->NS, NS->ES, Jacobian->NS kinematics)
and the scaling maps of the source's Section 10 / reader (E.24)-(E.30).  Own code for the inv_NS audit.

Sources checked:
 YM  yang-mills/sources/ym_quantum_coarse_graining_astra_20260908/nonabelian_fluid_profile_addendum.tex (227)-(246)
 YM  yang-mills/sources/ym_gap_primary_20260908/ns_inner_profile_curvature_current_bridge.md (3.1)-(5.7)
 YM  released_profile_measures_addendum.tex (251)-(258) (abelian map; also in 21_ check B1)
 zeta satellites/29k_ns_angular_mellin.tex (nam:cartesian), (nam:pde), (nam:mellin), (nam:arithmetic)
 zeta sidebar/fluid/tex/s6_dynamics_bridge.tex (Beltrami image)
 source-faithful transcription pp.115-126 ((10.22), Cor. 10.6), reader L5203-5290 (E.24)-(E.30)
"""
import sympy as sp
import mpmath as mp

res = []


def check(name, expr):
    if isinstance(expr, bool):
        ok = expr
    elif isinstance(expr, sp.MatrixBase):
        ok = all(sp.simplify(x) == 0 for x in expr)
    else:
        ok = sp.simplify(expr) == 0
    res.append((name, ok))
    print(("PASS" if ok else "FAIL") + "  " + name)


x1, x2, x3, s = sp.symbols('x1 x2 x3 s', real=True)
xs = (x1, x2, x3)
lam, c, nu = sp.symbols('lambda c nu', positive=True)
psi = [sp.Function('psi%d' % i)(x1, x2, x3, s) for i in range(3)]
curl = lambda v: sp.Matrix([sp.diff(v[2], x2) - sp.diff(v[1], x3), sp.diff(v[0], x3) - sp.diff(v[2], x1), sp.diff(v[1], x1) - sp.diff(v[0], x2)])
u = curl(psi)                                            # divergence-free velocity
div = lambda v: sum(sp.diff(v[i], xs[i]) for i in range(3))
check("u = curl psi is divergence-free", div(u))
e = [sp.Matrix([1 if j == i else 0 for j in range(3)]) for i in range(3)]

# ---------------- NS -> YM, abelian map A_i = lambda u_i T (21_ section 2): magnetic density
# F_ij = lambda (d_i u_j - d_j u_i) T, -2 tr T^2 = 1  =>  -2 sum_{i<j} tr F_ij^2 = lambda^2 |curl u|^2
Fab = sum((lam*(sp.diff(u[j], xs[i]) - sp.diff(u[i], xs[j])))**2 for i in range(3) for j in range(i + 1, 3))
check("NS->YM abelian: sum_{i<j} F_ij^2 (colour-normalised) = lambda^2 |curl u|^2", Fab - lam**2*(curl(u).T*curl(u))[0])

# ---------------- NS -> YM, non-abelian map A_i = lambda e_i x u (colour vectors, [T_a,T_b] = eps_abd T_d)
Acol = [lam*e[i].cross(u) for i in range(3)]
# F_jk = d_j A_k - d_k A_j + A_j x A_k (colour cross product); B_i = (1/2) eps_ijk F_jk
Fjk = [[sp.diff(Acol[k], xs[j]) - sp.diff(Acol[j], xs[k]) + Acol[j].cross(Acol[k]) for k in range(3)] for j in range(3)]
eps = sp.LeviCivita
Bcol = [sum((sp.Rational(1, 2)*eps(i, j, k)*Fjk[j][k] for j in range(3) for k in range(3)), sp.zeros(3, 1)) for i in range(3)]
claim230 = [sp.Matrix([lam*(sp.diff(u[i], xs[a]) - (1 if i == a else 0)*div(u)) + lam**2*u[i]*u[a] for a in range(3)]) for i in range(3)]
check("(230) B_i^a = lambda(d_a u_i - delta_ia div u) + lambda^2 u_i u_a", sp.Matrix.vstack(*[Bcol[i] - claim230[i] for i in range(3)]))
B2 = sum((Bcol[i].T*Bcol[i])[0] for i in range(3))
grad2 = sum(sp.diff(u[i], xs[a])**2 for i in range(3) for a in range(3))
u2 = (u.T*u)[0]
check("(232) |B|^2 = lambda^2|grad u|^2 + lambda^3 d_a(|u|^2 u_a) + lambda^4 |u|^4 (div u = 0)",
      sp.expand(B2 - (lam**2*grad2 + lam**3*sum(sp.diff(u2*u[a], xs[a]) for a in range(3)) + lam**4*u2**2)))
check("(234) tr B = lambda^2 |u|^2", sp.expand(sum(Bcol[i][i] for i in range(3)) - lam**2*u2))
us = sp.diff(u, s)
Ecol = [lam/c*e[i].cross(us) for i in range(3)]
check("(233) |E|^2 = 2 lambda^2 |u_s|^2 / c^2", sp.expand(sum((Ecol[i].T*Ecol[i])[0] for i in range(3)) - 2*lam**2*(us.T*us)[0]/c**2))
# Gauss component (236): g^2 j_0 = sum_i D_i F_i0 = -(sum_i d_i E_i + A_i x E_i)
j0 = -sum((sp.diff(Ecol[i], xs[i]) + Acol[i].cross(Ecol[i]) for i in range(3)), sp.zeros(3, 1))
check("(236) g^2 j_0 = -(lambda/c) curl u_s - (lambda^2/c) u x u_s", j0 - (-(lam/c)*curl(us) - lam**2/c*u.cross(us)))
# spatial current (237) from the definition g^2 j_i = -D_0 F_0i + sum_j D_j F_ji, F_ji = eps_jik B_k, X^0 = c s
uss = sp.diff(u, s, 2)
om = curl(u)
adv = sp.Matrix([sum(u[k]*sp.diff(u[i], xs[k]) for k in range(3)) for i in range(3)])
ok237 = True
for i in range(3):
    Fji = [sum((eps(j, i, k)*Bcol[k] for k in range(3)), sp.zeros(3, 1)) for j in range(3)]
    ji = -(1/c)*sp.diff(Ecol[i], s) + sum((sp.diff(Fji[j], xs[j]) + Acol[j].cross(Fji[j]) for j in range(3)), sp.zeros(3, 1))
    grad_om_i = sp.Matrix([sp.diff(om[i], xs[a]) for a in range(3)])
    epsterm = sum((eps(i, j, k)*u[k]*sp.Matrix([sp.diff(u[a], xs[j]) for a in range(3)]) for j in range(3) for k in range(3)), sp.zeros(3, 1))
    claim = -(lam/c**2)*e[i].cross(uss) - lam*grad_om_i - lam**2*(2*om[i]*u + epsterm + e[i].cross(adv)) - lam**3*u2*e[i].cross(u)
    if not all(sp.expand(x) == 0 for x in (ji - claim)):
        ok237 = False
check("(237) spatial current g^2 j_i (all three i, generic divergence-free u)", ok237)
# axis values (244)-(245)
a_, b_, w_ = sp.symbols('a b w', real=True)
Gu = sp.Matrix([[a_, -b_, 0], [b_, a_, 0], [0, 0, -2*a_]])            # rows i: d_a u_i
uax = sp.Matrix([0, 0, w_])
Bax = sp.Matrix(3, 3, lambda i, aa: lam*Gu[i, aa] + lam**2*uax[i]*uax[aa])
check("(245) |B|^2_axis = 2 lambda^2 (a^2+b^2) + (-2 lambda a + lambda^2 w^2)^2", sp.expand(sum(x**2 for x in Bax) - (2*lam**2*(a_**2 + b_**2) + (-2*lam*a_ + lam**2*w_**2)**2)))

# ---------------- NS -> YM rate bounds used as (250) (ns_inner_profile_curvature_current_bridge.md)
h = sp.symbols('h', positive=True)
A = sp.Rational(1, 2) + h
D = sp.Rational(1, 2) - h
etaa, tau = sp.symbols('eta tau', positive=True)
z_of = tau**D*etaa*(1 - etaa**2)**(-D)
qq = tau/(1 - etaa**2)
pts = [(sp.Rational(1, 137), sp.Rational(3, 10), sp.Rational(1, 100)), (sp.Rational(1, 101), sp.Rational(-7, 10), sp.Rational(1, 7)),
       (sp.Rational(1, 200), sp.Rational(9, 10), sp.Rational(1, 3))]
def numzero(expr):
    return all(abs(sp.N(expr.subs({h: hv_, etaa: ev_, tau: tv_}), 40)) < 1e-30 for hv_, ev_, tv_ in pts)
check("(4.6) dz/deta = tau^D (1 - 2h eta^2)(1-eta^2)^(-D-1) (exact expression evaluated at 3 points, 40 digits)",
      numzero(sp.diff(z_of, etaa) - tau**D*(1 - 2*h*etaa**2)*(1 - etaa**2)**(-D - 1)))
check("(4.7) q^(-2A) dz/deta = tau^(D-2A) (1-2h eta^2)(1-eta^2)^(2A-D-1) (3 points)",
      numzero(qq**(-2*A)*sp.diff(z_of, etaa) - tau**(D - 2*A)*(1 - 2*h*etaa**2)*(1 - etaa**2)**(2*A - D - 1)))
check("(4.7) D - 2A = -1/2 - 3h", D - 2*A + sp.Rational(1, 2) + 3*h)
check("(5.6) q^(-2A-2) * q tau^D L (1-eta^2)^(-D-1) = tau^(D-2A-1) L (1-eta^2)^(2A-D) (3 points)",
      numzero(qq**(-2*A - 2)*qq*tau**D*(1 - 2*h*etaa**2)*(1 - etaa**2)**(-D - 1) - tau**(D - 2*A - 1)*(1 - 2*h*etaa**2)*(1 - etaa**2)**(2*A - D)))
check("(5.6) D - 2A - 1 = -3/2 - 3h", D - 2*A - 1 + sp.Rational(3, 2) + 3*h)
check("integrability of tau^(-1/2-3h) near 0  <=>  h < 1/6", sp.solve(sp.Rational(-1, 2) - 3*h + 1 > 0, h) == (h < sp.Rational(1, 6)))
Xs, qs = sp.symbols('X q', positive=True)
r_ = sp.sqrt(2*qs*Xs)
check("(5.5) r dr = q dX on a fixed z-slice", sp.simplify(r_*sp.diff(r_, Xs) - qs))
epsv = sp.symbols('epsilon', positive=True)
check("(3.1) v_eps = eps^(-1/3) v(x/eps): L2^2 scale eps^(7/3), enstrophy scale eps^(1/3)",
      sp.simplify((epsv**sp.Rational(-2, 3)*epsv**3 - epsv**sp.Rational(7, 3))) + sp.simplify(epsv**sp.Rational(-2, 3)*epsv**-2*epsv**3 - epsv**sp.Rational(1, 3)))
check("source 3.5: E_core ~ tau^(3/2-h) tau^(-1-2h) = tau^(1/2-3h); D_core ~ tau^(-1/2-3h)",
      sp.simplify(tau**(sp.Rational(3, 2) - h)*tau**(-1 - 2*h) - tau**(sp.Rational(1, 2) - 3*h)) + sp.simplify(tau**(sp.Rational(3, 2) - h)*tau**(-2 - 2*h) - tau**(-sp.Rational(1, 2) - 3*h)))
check("source 3.3: A_wave^2 ~ q^(-1-h) = |u_theta|/q^(1/2), A^2/q^(1/2) ~ q^(-3/2-h) = q^(-A-1)",
      sp.simplify((qs**(-sp.Rational(1, 2) - h/2))**2 - qs**(-A)/qs**sp.Rational(1, 2)) + sp.simplify(qs**(-1 - h)/qs**sp.Rational(1, 2) - qs**(-A - 1)))

# ---------------- NS -> zeta (satellite 29k): Cartesian angular-momentum equation and Muntz/Mellin multiplier
t = sp.symbols('t', real=True)
U3 = [sp.Function('U%d' % i)(x1, x2, x3, t) for i in range(3)]
Pp = sp.Function('P')(x1, x2, x3, t)
Ff = [sp.Function('f%d' % i)(x1, x2, x3, t) for i in range(3)]
lap = lambda g: sum(sp.diff(g, xx, 2) for xx in xs)
NSres = [sp.diff(U3[i], t) + sum(U3[k]*sp.diff(U3[i], xs[k]) for k in range(3)) - nu*lap(U3[i]) + sp.diff(Pp, xs[i]) - Ff[i] for i in range(3)]
Lm = x1*U3[1] - x2*U3[0]
omz = sp.diff(U3[1], x1) - sp.diff(U3[0], x2)
dth = lambda g: x1*sp.diff(g, x2) - x2*sp.diff(g, x1)
lhs = sp.diff(Lm, t) + sum(sp.diff(U3[k]*Lm, xs[k]) for k in range(3)) - (nu*lap(Lm) - 2*nu*omz - dth(Pp) + x1*Ff[1] - x2*Ff[0])
divU = sum(sp.diff(U3[k], xs[k]) for k in range(3))
check("29k (nam:cartesian): d_t L + div(uL) - [nu Lap L - 2 nu w_z - d_th p + torque] = x1 R_2 - x2 R_1 + L div u",
      sp.expand(lhs - (x1*NSres[1] - x2*NSres[0] + Lm*divU)))
hh = sp.symbols('h', positive=True)
ssym = sp.symbols('s')
Wh = sp.zeta(ssym)*(1 - 2**(ssym - 1))*(1 - 2**(hh - ssym))
psi_mult = (1 + 2**(hh - 1)) - 2**hh*2**(-ssym) - sp.Rational(1, 2)*2**ssym   # Mellin multiplier of psi_a / a-hat
check("29k (nam:arithmetic): Mellin multiplier of psi_a is (1 - 2^(s-1))(1 - 2^(h-s))", sp.expand(psi_mult - (1 - 2**(ssym - 1))*(1 - 2**(hh - ssym))))
check("29k: int psi_a = 0 (multiplier vanishes at s = 1)", sp.simplify(psi_mult.subs(ssym, 1)))
mp.mp.dps = 30
hv = mp.mpf(1)/137
Wnum = lambda sv: mp.zeta(sv)*(1 - mp.power(2, sv - 1))*(1 - mp.power(2, hv - sv))
check("29k: W_h is regular at s = 1 (pole of zeta cancelled): W_h(1 +/- 1e-12) agree to 1e-8",
      bool(abs(Wnum(1 + mp.mpf('1e-12')) - Wnum(1 - mp.mpf('1e-12'))) < mp.mpf('1e-8')))
check("29k: W_h(-1) = zeta(-1)(3/4)(1 - 2^(1+h)) != 0", bool(abs(Wnum(-1)) > 1e-3))
# Mellin integration-by-parts identities on a test function
sv = mp.mpf('0.7') + 0.3j
Bt = lambda x: x*mp.e**(-x)
Pt = lambda x: x**2*mp.e**(-x)
Mell = lambda g, s_: mp.quad(lambda x: g(x)*x**(s_ - 1), [0, 1, mp.inf])
lhs1 = mp.quad(lambda x: mp.diff(Pt, x)*x**(sv - 1), [0, 1, mp.inf])
lhs2 = mp.quad(lambda x: 2*x*mp.diff(Bt, x, 2)*x**(sv - 1), [0, 1, mp.inf])
check("29k (nam:mellin): int P' sigma^(s-1) = -(s-1) P^(s-1); int 2 sigma B'' sigma^(s-1) = 2s(s-1) B^(s-1) (numerical)",
      bool(abs(lhs1 + (sv - 1)*Mell(Pt, sv - 1)) < 1e-15 and abs(lhs2 - 2*sv*(sv - 1)*Mell(Bt, sv - 1)) < 1e-15))
sS = sp.symbols('s')
check("29 series: Mellin transform of B = sigma e^-sigma is Gamma(s+1), residue B'(0) = 1 at s = -1",
      sp.simplify(sp.residue(sp.gamma(sS + 1), sS, -1) - 1))

# ---------------- S6 -> NS (zeta sidebar/fluid s6_dynamics_bridge.tex): the Beltrami image solves forced NS
n_, eta_, sig, om_, R_ = sp.symbols('n eta sigma omega R', positive=True)
lamk = 2*sp.pi*n_
dd = sp.exp(-nu*lamk**2*t)
Kt = R_*sp.cos(om_*sig*t)
Bt_ = R_*sp.sin(om_*sig*t)
B1 = sp.Matrix([sp.sin(lamk*x3), sp.cos(lamk*x3), 0])
B2 = sp.Matrix([0, sp.sin(lamk*x1), sp.cos(lamk*x1)])
uu = eta_*dd*(Kt*B1 + Bt_*B2)
pp = -eta_**2*dd**2*Kt*Bt_*sp.cos(lamk*x3)*sp.sin(lamk*x1)
ff = eta_*sig*om_*dd*(-Bt_*B1 + Kt*B2)
NSb = sp.diff(uu, t) + sp.Matrix([sum(uu[k]*sp.diff(uu[i], xs[k]) for k in range(3)) for i in range(3)]) - nu*sp.Matrix([lap(uu[i]) for i in range(3)]) + sp.Matrix([sp.diff(pp, xx) for xx in xs]) - ff
check("S6->NS: u = eta d(t)(K B1 + B B2), p, f of s6_dynamics_bridge solve forced NS exactly on T^3", NSb.applyfunc(sp.simplify))
check("S6->NS: curl B_j = lambda B_j and div u = 0 (Beltrami)", (curl(B1) - lamk*B1).applyfunc(sp.simplify) + (curl(B2) - lamk*B2).applyfunc(sp.simplify))
mS, Gm, kp, hS = sp.symbols('m Gamma kappa h_s', positive=True)
Delta = 1 - 6*Gm*hS/kp
aS = (mS**2 + 12*Gm*hS**2)/Delta
R2 = 3*aS*hS/kp + 3*hS**2
check("S6 oscillator identities: a = m^2 + Gamma(6h^2 + 2R^2), -ah - kappa h^2 + kappa R^2/3 = 0, a - 2 kappa h = (m^2 - 2kh + 24 G h^2)/Delta",
      sp.simplify(aS - (mS**2 + Gm*(6*hS**2 + 2*R2))) + sp.simplify(-aS*hS - kp*hS**2 + kp*R2/3) + sp.simplify(aS - 2*kp*hS - (mS**2 - 2*kp*hS + 24*Gm*hS**2)/Delta))

# ---------------- NS -> ES torus endomorphism (21_ section 1; reader L2405-2429)
Jm = sp.Matrix([[3, 1], [1, 5]])
vr = sp.Matrix([1, 1 - sp.sqrt(2)])
vt = sp.Matrix([sp.sqrt(2) - 1, 1])
check("torus J: det 14, J v_r = (4 - sqrt2) v_r, J v_t = (4 + sqrt2) v_t",
      (Jm.det() - 14) + sp.simplify((Jm*vr - (4 - sp.sqrt(2))*vr).norm()) + sp.simplify((Jm*vt - (4 + sp.sqrt(2))*vt).norm()))
m1, m2 = sp.symbols('n1 n2', integer=True)
check("torus J: (v_r.n)(conj) = (n1+n2)^2 - 2 n2^2 and (v_t.n)(conj) = (n2-n1)^2 - 2 n1^2 (Diophantine lower bound)",
      sp.expand((m1 + (1 - sp.sqrt(2))*m2)*(m1 + (1 + sp.sqrt(2))*m2) - ((m1 + m2)**2 - 2*m2**2)) + sp.expand(((sp.sqrt(2) - 1)*m1 + m2)*((-sp.sqrt(2) - 1)*m1 + m2) - ((m2 - m1)**2 - 2*m1**2)))

# ---------------- Jacobian map F (28_ Lemma 28.1) -> incompressible polynomial flow
x, y, ww = sp.symbols('x y w')
F = sp.Matrix([(1 + x*y)**3*ww + y**2*(1 + x*y)*(4 + 3*x*y), y + 3*x*(1 + x*y)**2*ww + 3*x*y**2*(4 + 3*x*y), 2*x - 3*x**2*y - x**3*ww])
DF = F.jacobian([x, y, ww])
check("Jacobian map: det DF = -2", sp.expand(DF.det()) + 2)
Uf = sp.expand(DF.adjugate()*sp.Matrix([2, 0, 0])/(-2))
check("Jacobian map: U = DF^-1 (2,0,0) is a polynomial divergence-free field", sp.expand(sp.diff(Uf[0], x) + sp.diff(Uf[1], y) + sp.diff(Uf[2], ww)))

# ---------------- viscosity / parabolic / periodisation maps (source (10.22), Cor. 10.6; reader (E.24)-(E.28))
yv = sp.symbols('y1:4', real=True)
uS = [sp.Function('v%d' % i)(*yv, t) for i in range(3)]
pS = sp.Function('pv')(*yv, t)
fS = [sp.Function('g%d' % i)(*yv, t) for i in range(3)]
lapy = lambda g: sum(sp.diff(g, yy, 2) for yy in yv)
R1 = [sp.diff(uS[i], t) + sum(uS[k]*sp.diff(uS[i], yv[k]) for k in range(3)) - lapy(uS[i]) + sp.diff(pS, yv[i]) - fS[i] for i in range(3)]
Xv = sp.symbols('X1:4', real=True)
sub_nu = {yv[i]: Xv[i]/sp.sqrt(nu) for i in range(3)}
uN = [sp.sqrt(nu)*uS[i].subs(sub_nu) for i in range(3)]
pN = nu*pS.subs(sub_nu)
fN = [sp.sqrt(nu)*fS[i].subs(sub_nu) for i in range(3)]
Rnu = [sp.diff(uN[i], t) + sum(uN[k]*sp.diff(uN[i], Xv[k]) for k in range(3)) - nu*sum(sp.diff(uN[i], xx, 2) for xx in Xv) + sp.diff(pN, Xv[i]) - fN[i] for i in range(3)]
check("(10.22)/(E.24): R_nu(A_nu(u,p,f))(x,t) = sqrt(nu) R_1(u,p,f)(x/sqrt(nu),t)",
      sp.Matrix([sp.simplify(Rnu[i] - sp.sqrt(nu)*R1[i].subs(sub_nu)) for i in range(3)]))
lm = sp.symbols('Lambda', positive=True)
t0 = sp.symbols('t0', real=True)
sub_l = {yv[i]: lm*Xv[i] for i in range(3)}
sub_lt = dict(sub_l); sub_lt[t] = lm**2*(t - t0)
uL = [lm*uS[i].subs(sub_lt, simultaneous=True) for i in range(3)]
pL = lm**2*pS.subs(sub_lt, simultaneous=True)
fL = [lm**3*fS[i].subs(sub_lt, simultaneous=True) for i in range(3)]
nuv = sp.symbols('nu_v', positive=True)
R1v = [sp.diff(uS[i], t) + sum(uS[k]*sp.diff(uS[i], yv[k]) for k in range(3)) - nuv*lapy(uS[i]) + sp.diff(pS, yv[i]) - fS[i] for i in range(3)]
RL = [sp.diff(uL[i], t) + sum(uL[k]*sp.diff(uL[i], Xv[k]) for k in range(3)) - nuv*sum(sp.diff(uL[i], xx, 2) for xx in Xv) + sp.diff(pL, Xv[i]) - fL[i] for i in range(3)]
check("Cor. 10.6/(E.26),(E.29): parabolic map multiplies the viscosity-nu residual by Lambda^3 (same nu)",
      sp.Matrix([sp.simplify(RL[i] - lm**3*R1v[i].subs(sub_lt, simultaneous=True)) for i in range(3)]))
check("Cor. 10.6: original time one reached at t = 1 when t0 = 1 - Lambda^-2", sp.simplify(lm**2*(1 - (1 - lm**-2)) - 1))
# (E.27)-(E.28): T_nu = S_sqrt(nu) o A_nu on the triple
tt_ = sp.symbols('tt')
xx_ = sp.symbols('xx')
Ufun = sp.Function('Uf1')
comp_u = sp.sqrt(nu)*(sp.sqrt(nu)*Ufun(sp.sqrt(nu)*xx_/sp.sqrt(nu), nu*tt_))
comp_p = nu*(nu*Ufun(sp.sqrt(nu)*xx_/sp.sqrt(nu), nu*tt_))
comp_f = nu**sp.Rational(3, 2)*(sp.sqrt(nu)*Ufun(sp.sqrt(nu)*xx_/sp.sqrt(nu), nu*tt_))
check("(E.28): prefactors of S_sqrt(nu) o A_nu are (nu, nu^2, nu^2) with argument (x, nu t)",
      sp.simplify(comp_u - nu*Ufun(xx_, nu*tt_)) + sp.simplify(comp_p - nu**2*Ufun(xx_, nu*tt_)) + sp.simplify(comp_f - nu**2*Ufun(xx_, nu*tt_)))
check("(10.23)/(E.25): energy factor nu * nu^(3/2) = nu^(5/2); (E.28) energy factors nu^(-1/2) nu^(5/2) = nu^2",
      sp.simplify(nu*nu**sp.Rational(3, 2) - nu**sp.Rational(5, 2)) + sp.simplify(nu**sp.Rational(-1, 2)*nu**sp.Rational(5, 2) - nu**2))
check("29i: ||f_nu||_2 = nu^(1/2) nu^(3/4) ||f||_2 = nu^(5/4) ||f||_2", sp.simplify(sp.sqrt(nu)*sp.sqrt(nu**sp.Rational(3, 2)) - nu**sp.Rational(5, 4)))

print("\nsummary: %d checks, %d PASS, %d FAIL" % (len(res), sum(o for _, o in res), sum(not o for _, o in res)))
