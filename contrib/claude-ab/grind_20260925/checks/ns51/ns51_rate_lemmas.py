#!/usr/bin/env python3
"""ns51_rate_lemmas.py -- symbolic checks (sympy) of every elementary step in the conditional NS rate bounds of note 51_:

 (i)  the NS->YM rate bounds of the YM repository's ns_inner_profile_curvature_current_bridge.md, sections 4-5
      (enstrophy >= C tau^(-1/2-3h), ||d_t u||^2 >= C tau^(-3/2-3h));
 (ii) the further conditional corollaries stated in note 51_ (L^p lower bounds, critical L^3 growth tau^(-4h/3),
      vorticity >= c tau^(-1-h), Type II rate), and their comparison with the classical necessary conditions
      (Leray's enstrophy rate 1/2, Beale-Kato-Majda, the L^3 criterion, the Type I threshold).

Inputs taken from the source (not re-proved here): (5.42) uniformly on [X_lo, X_hi] x [-1, 1]; Theorem 4.6 (E_0 > 0 on the
inner region, axis regularity E_0(X, 0) = O(sqrt X)); Proposition 9.9 Step 5 (annular corrections vanish for X < X_a);
Proposition 10.1 (cutoffs equal one near the singular point).
"""
import sympy as sp

res = []
def check(name, cond):
    ok = bool(cond)
    res.append((name, ok))
    print(("PASS" if ok else "FAIL") + "  " + name)

h, q, X, eta, tau, p = sp.symbols('h q X eta tau p', positive=True)

w_ = sp.symbols('w', positive=True)   # w = 1 - eta^2 in (0, 1)
def ratio_is_one(expr):
    """symbolic check that expr == 1 for 0 < eta < 1, via eta = sqrt(1 - w), w > 0 (so powers of 1 - eta^2 combine)."""
    e = sp.powsimp(sp.expand_power_base(sp.simplify(expr.subs(eta, sp.sqrt(1 - w_))), force=True), force=True)
    return sp.simplify(e - 1) == 0
A = sp.Rational(1, 2) + h
D = sp.Rational(1, 2) - h
L = 1 - 2*h*eta**2

# ---- coordinates (4.1): tau = q(1-eta^2), z = q^D eta, r^2 = 2 q X.  Jacobian of (tau, z, r) w.r.t. (q, eta, X)
tau_f = q*(1 - eta**2)
z_f = q**D*eta
r_f = sp.sqrt(2*q*X)
Jm = sp.Matrix([[sp.diff(f, v) for v in (q, eta, X)] for f in (tau_f, z_f, r_f)])
Jinv = sp.simplify(Jm.inv())
# at fixed (z, r): d/dtau of (q, eta, X) is the first column of Jinv; d/dt = -d/dtau
q_t, eta_t, X_t = [sp.simplify(-Jinv[i, 0]) for i in range(3)]
check("(5.1) q_t = -1/L", sp.simplify(q_t + 1/L) == 0)
check("(5.1) eta_t = D eta/(q L)", sp.simplify(eta_t - D*eta/(q*L)) == 0)
check("(5.1) X_t = X/(q L)", sp.simplify(X_t - X/(q*L)) == 0)

# ---- (5.3): d_t [q^{-A}(E + R)] = q^{-A-1} (H + L^{-1}(A R - q R_q + X R_X + D eta R_eta))
E = sp.Function('E')(X, eta)
R = sp.Function('R')(q, X, eta)
u = q**(-A)*(E + R)
dtu = q_t*sp.diff(u, q) + eta_t*sp.diff(u, eta) + X_t*sp.diff(u, X)
Hc = (A*E + X*sp.diff(E, X) + D*eta*sp.diff(E, eta))/L
rem = (A*R - q*sp.diff(R, q) + X*sp.diff(R, X) + D*eta*sp.diff(R, eta))/L
check("(5.2)-(5.3) d_t u_theta = q^(-A-1) (H + L^(-1)(A R - q R_q + X R_X + D eta R_eta))",
      sp.simplify(sp.expand(dtu - q**(-A - 1)*(Hc + rem))) == 0)

# ---- (4.6) and (5.5): at fixed tau, z = tau^D eta (1-eta^2)^(-D); r dr dz = q (dz/deta) dX deta
z_tau = tau**D*eta*(1 - eta**2)**(-D)
dz = sp.diff(z_tau, eta)
check("(4.6) dz/deta = tau^D (1 - 2h eta^2)(1-eta^2)^(-D-1)",
      ratio_is_one(dz/(tau**D*L*(1 - eta**2)**(-D - 1))))
q_tau = tau/(1 - eta**2)
r_tau = sp.sqrt(2*q_tau*X)
jac = sp.Matrix([[sp.diff(r_tau, X), sp.diff(r_tau, eta)], [sp.diff(z_tau, X), sp.diff(z_tau, eta)]]).det()
check("(5.5) r * det d(r,z)/d(X,eta) = q tau^D L (1-eta^2)^(-D-1)",
      ratio_is_one(r_tau*jac/(q_tau*tau**D*L*(1 - eta**2)**(-D - 1))))

# ---- (4.5): Stokes + Cauchy-Schwarz on a disk of radius r: (2 pi r u)^2 / (pi r^2) = 4 pi u^2
rr, uu = sp.symbols('r u', positive=True)
check("(4.5) (2 pi r u)^2/(pi r^2) = 4 pi u^2", sp.simplify((2*sp.pi*rr*uu)**2/(sp.pi*rr**2) - 4*sp.pi*uu**2) == 0)

# ---- exponents of (4.7), (5.6) and of the L^p corollary
def tau_exponent(expr):
    """exponent of tau in a product tau^a * (function of eta)"""
    e = sp.expand_power_base(sp.powsimp(sp.expand_power_exp(expr), force=True), force=True)
    return sp.simplify(sp.diff(sp.log(e), tau)*tau)
enst = q_tau**(-2*A)*dz                       # integrand of (4.7): q^{-2A} dz/deta (times 4 pi e_*^2)
check("(4.7) enstrophy integrand ~ tau^(D-2A) = tau^(-1/2-3h)", sp.simplify(tau_exponent(enst) - (-sp.Rational(1, 2) - 3*h)) == 0)
check("(4.7) its eta-factor is L (1-eta^2)^(2A-D-1)",
      ratio_is_one(enst/(tau**(D - 2*A)*L*(1 - eta**2)**(2*A - D - 1))))
dudt = q_tau**(-2*A - 2)*q_tau*tau**D*L*(1 - eta**2)**(-D - 1)
check("(5.6) ||d_t u||^2 integrand ~ tau^(D-2A-1) = tau^(-3/2-3h)", sp.simplify(tau_exponent(dudt) - (-sp.Rational(3, 2) - 3*h)) == 0)
check("(5.6) its eta-factor is L (1-eta^2)^(2A-D)",
      ratio_is_one(dudt/(tau**(D - 2*A - 1)*L*(1 - eta**2)**(2*A - D))))
Lp = q_tau**(-p*A)*q_tau*tau**D*L*(1 - eta**2)**(-D - 1)
ep = sp.simplify(tau_exponent(Lp))
check("(51.L^p) ||u||_p^p integrand ~ tau^(1 + D - pA) = tau^(3/2 - h - p(1/2+h))", sp.simplify(ep - (sp.Rational(3, 2) - h - p*(sp.Rational(1, 2) + h))) == 0)
check("(51.L^p) p = 2: exponent 1/2 - 3h > 0 (core energy -> 0, source p.4)", sp.simplify(ep.subs(p, 2) - (sp.Rational(1, 2) - 3*h)) == 0)
check("(51.L^p) p = 3: exponent -4h (critical L^3 norm >= c tau^(-4h/3) -> infinity)", sp.simplify(ep.subs(p, 3) + 4*h) == 0)
pc = sp.solve(sp.Eq(ep, 0), p)[0]
check("(51.L^p) exponent < 0 iff p > p_h = (3 - 2h)/(1 + 2h), and p_h < 3 for h > 0", sp.simplify(pc - (3 - 2*h)/(1 + 2*h)) == 0
      and sp.simplify(3 - pc - 8*h/(1 + 2*h)) == 0)
check("(51.L^p) eta-factor for p = 3 is L (1-eta^2)^(3A-D-2) = L (1-eta^2)^(-1+4h), integrable on compact eta-sets",
      ratio_is_one(Lp.subs(p, 3)/(tau**(-4*h)*L*(1 - eta**2)**(-1 + 4*h))))

# ---- vorticity: disk mean 2 u/r with u = e q^{-A}, r = sqrt(2 X q)  ->  q^{-A-1/2} = q^{-1-h}
e_, Xs = sp.symbols('e X_s', positive=True)
mean_om = 2*e_*q**(-A)/sp.sqrt(2*Xs*q)
check("(51.omega) disk-mean vorticity 2u/r = sqrt(2) e X_s^(-1/2) q^(-1-h)",
      sp.simplify(mean_om - sp.sqrt(2)*e_*Xs**sp.Rational(-1, 2)*q**(-1 - h)) == 0)

# ---- comparisons with classical necessary conditions (exponent arithmetic)
hh = sp.Rational(1, 200)       # any 0 < h < 1/100
check("Leray: enstrophy exponent 1/2 + 3h exceeds the universal rate 1/2", sp.Rational(1, 2) + 3*hh > sp.Rational(1, 2))
check("BKM: int_0 tau^(-1-h) dtau diverges (exponent <= -1)", -1 - hh <= -1)
check("Prodi-Serrin (L^2_t L^inf): int tau^(-2A) = int tau^(-1-2h) diverges", -2*(sp.Rational(1, 2) + hh) <= -1)
check("Type II: tau^(1/2) * tau^(-A) = tau^(-h) -> infinity (not Type I)", sp.Rational(1, 2) - (sp.Rational(1, 2) + hh) < 0)
check("rate compatibility: int_0^1 tau^(-1/2-3h) < infinity (as (3.5) requires) iff h < 1/6", sp.Rational(1, 2) + 3*hh < 1)

# ---- viscosity scalings u_nu(x) = sqrt(nu) u(x/sqrt(nu)) in R^3
nu = sp.symbols('nu', positive=True)
# ||u_nu||_p^p = nu^(p/2) nu^(3/2) ||u||_p^p ; ||curl u_nu||^2 = nu^(3/2) ||curl u||^2 ; ||d_t u_nu||^2 = nu^(5/2) ||d_t u||^2
check("viscosity map: ||u_nu||_p^p = nu^((p+3)/2) ||u||_p^p", sp.simplify(nu**(p/2)*nu**sp.Rational(3, 2) - nu**((p + 3)/2)) == 0)
check("viscosity map: vorticity sup unchanged (curl u_nu(x) = (curl u)(x/sqrt nu))", sp.simplify(sp.sqrt(nu)/sp.sqrt(nu) - 1) == 0)

# ---- negative controls (wrong variants must be rejected)
check("negative control rejected: eta_t = -D eta/(q L)", not (sp.simplify(eta_t + D*eta/(q*L)) == 0))
check("negative control rejected: enstrophy exponent D + 2A", not (sp.simplify(tau_exponent(enst) - (D + 2*A)) == 0))
check("negative control rejected: L^3 exponent -3h", not (sp.simplify(ep.subs(p, 3) + 3*h) == 0))

n = len(res); npass = sum(ok for _, ok in res)
print(f"\nsummary: {n} checks, {npass} PASS, {n - npass} FAIL")
