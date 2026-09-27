"""Independent sympy re-derivation of exact identities in the NS reader's
leading-field sections (navier_stokes_workbench.tex L80-355 and L981-1175).

Written for the inv_NS first-pass audit (27 Sep 2026).  Own code; it does not
import the bundle's checkers.  Every check prints PASS/FAIL.

Coordinates (reader L86-121, source (3.2)):  tau = 1 - t = q (1 - eta^2),
z = q^D eta, s = r^2/2 = q X, A = 1/2 + h, D = 1/2 - h, d = 1 - eta^2,
L = 1 - 2 h eta^2.  We work in the independent variables (q, eta, X) and build
the physical derivative fields d/dt, d/dz, d/dr (at fixed other physical
variables) from the inverse Jacobian, so nothing in the claimed formulas is
assumed.
"""
import sympy as sp

results = []


def check(name, expr, simplifier=None):
    e = expr
    if simplifier is not None:
        e = simplifier(e)
    else:
        e = sp.simplify(sp.expand(e))
    ok = (e == 0)
    results.append((name, ok))
    print(("PASS" if ok else "FAIL") + "  " + name + ("" if ok else "   residual: " + str(e)[:300]))
    return ok


q, X = sp.symbols('q X', positive=True)
eta = sp.symbols('eta', real=True)
h = sp.symbols('h', positive=True)
A = sp.Rational(1, 2) + h
D = sp.Rational(1, 2) - h
d = 1 - eta**2
L = 1 - 2*h*eta**2
r = sp.sqrt(2*q*X)

# ---------------------------------------------------------------- A1 coordinates
# physical (t, z, s) as functions of (q, eta, X)
t_of = 1 - q*d
z_of = q**D*eta
s_of = q*X
J = sp.Matrix([[sp.diff(f, v) for v in (q, eta, X)] for f in (t_of, z_of, s_of)])
Jinv = sp.simplify(J.inv())   # rows: (q, eta, X); cols: (t, z, s)
q_t, q_z, q_s = Jinv[0, 0], Jinv[0, 1], Jinv[0, 2]
e_t, e_z, e_s = Jinv[1, 0], Jinv[1, 1], Jinv[1, 2]
X_t, X_z, X_s = Jinv[2, 0], Jinv[2, 1], Jinv[2, 2]

pw = lambda e: sp.simplify(sp.powsimp(sp.powdenest(sp.expand_power_base(e, force=True), force=True), force=True))
check("A1 q_t = -1/L", pw(q_t + 1/L))
check("A1 eta_t = D eta/(q L)", pw(e_t - D*eta/(q*L)))
check("A1 X_t = X/(q L)", pw(X_t - X/(q*L)))
check("A1 q_z = 2 eta q^(1-D)/L", pw(q_z - 2*eta*q**(1-D)/L))
check("A1 eta_z = d/(q^D L)", pw(e_z - d/(q**D*L)))
check("A1 X_z = -2 eta X/(q^D L)", pw(X_z + 2*eta*X/(q**D*L)))
check("A1 q_s = eta_s = 0, X_s = 1/q", pw(q_s) + pw(e_s) + pw(X_s - 1/q))
check("A1 L - 2 D eta^2 = d", L - 2*D*eta**2 - d)
check("A1 A + D = 1", A + D - 1)
check("A1 2A - 1 = 2h", 2*A - 1 - 2*h)
check("A1 -2A - D = -A - 1", -2*A - D + A + 1)
check("A1 1 - 2D = 2h", 1 - 2*D - 2*h)
# uniqueness of q: g(q) = q - z^2 q^(2h), g'(q) = 1 - 2 h z^2 q^(2h-1) = L on the chart
zz = sp.symbols('zz', real=True)
gprime = sp.diff(q - zz**2*q**(2*h), q)
check("A1 g'(q) = L when z = q^D eta", pw(gprime.subs(zz, q**D*eta) - L))

qt_, et_, Xt_ = -1/L, D*eta/(q*L), X/(q*L)
qz_, ez_, Xz_ = 2*eta*q**(1-D)/L, d/(q**D*L), -2*eta*X/(q**D*L)


def Dt(e):
    return qt_*sp.diff(e, q) + et_*sp.diff(e, eta) + Xt_*sp.diff(e, X)


def Dz(e):
    return qz_*sp.diff(e, q) + ez_*sp.diff(e, eta) + Xz_*sp.diff(e, X)


def Dr(e):
    # d/dr at fixed (t, z): only X moves, dX/dr = r/q
    return (r/q)*sp.diff(e, X)


f = sp.Function('f')(X, eta)
b = sp.symbols('b', real=True)
# commutation of the coordinate vector fields (consistency of the chart)
check("A1 [d_t, d_z] = 0 on generic q^b f", pw(Dt(Dz(q**b*f)) - Dz(Dt(q**b*f))))
check("A1 [d_t, d_r] = 0", pw(Dt(Dr(q**b*f)) - Dr(Dt(q**b*f))))
check("A1 [d_z, d_r] = 0", pw(Dz(Dr(q**b*f)) - Dr(Dz(q**b*f))))

# ---------------------------------------------------------------- A2 derivative maps
Tb = lambda bb, g: (-bb*g + D*eta*sp.diff(g, eta) + X*sp.diff(g, X))/L
Zb = lambda bb, g: (2*bb*eta*g + d*sp.diff(g, eta) - 2*eta*X*sp.diff(g, X))/L
check("A2 d_t(q^b f) = q^(b-1) T_b f", pw(Dt(q**b*f) - q**(b-1)*Tb(b, f)))
check("A2 d_z(q^b f) = q^(b-D) Z_b f", pw(Dz(q**b*f) - q**(b-D)*Zb(b, f)))
check("A2 d_zz(q^b f) = q^(b-2D) Z_(b-D) Z_b f", pw(Dz(Dz(q**b*f)) - q**(b-2*D)*Zb(b-D, Zb(b, f))))

# ---------------------------------------------------------------- A4-A7 ansatz
C = sp.symbols('C', positive=True)
Ff = sp.Function('F')(X, eta)            # F = phi/C, smooth at the axis
M = sp.Function('M')(X, eta)             # M = int_0^X U
U = sp.diff(M, X)
E = sp.sqrt(2*X)*Ff
Pi = sp.Function('Pi')(X, eta)
V0 = (2*eta*X*U - 2*D*eta*M - d*sp.diff(M, eta))/L
u_th = q**(-A)*E
u_z = q**(-A)*U
u_r = V0/r
p = q**(-2*A)*Pi

# Cartesian extension (reader L130-135): u1 = v0 x1/(2q) - q^(-A-1/2) F x2 with V0 = X v0
x1, x2 = sp.symbols('x1 x2', real=True)
th = sp.symbols('theta', real=True)
v0 = sp.Function('v0')(X, eta)
ur_c, uth_c = X*v0/r, q**(-A)*sp.sqrt(2*X)*Ff
u1 = ur_c*sp.cos(th) - uth_c*sp.sin(th)
u1_claim = v0/(2*q)*(r*sp.cos(th)) - q**(-A-sp.Rational(1, 2))*Ff*(r*sp.sin(th))
check("A4 Cartesian u1 formula", pw(u1 - u1_claim))

# incompressibility d_s(r u_r) + d_z u_z = 0 <=> (V0)_X = L^{-1}(2A eta U - d U_eta + 2 eta X U_X)
cont = sp.diff(V0, X)/q + Dz(u_z)
check("A5 continuity d_s(r u_r)+d_z u_z = 0 with V0=(2eta X U-2D eta M-d M_eta)/L", pw(cont))
check("A5 (V0)_X = (2A eta U - d U_eta + 2 eta X U_X)/L",
      pw(sp.diff(V0, X) - (2*A*eta*U - d*sp.diff(U, eta) + 2*eta*X*sp.diff(U, X))/L))

# radial pressure balance d_r p = u_th^2/r  <=>  Pi_X = E^2/(2X) = F^2
bal = Dr(p) - u_th**2/r
check("A7 d_r p - u_th^2/r = q^(-2A) r/q (Pi_X - F^2)", pw(bal - q**(-2*A)*(r/q)*(sp.diff(Pi, X) - Ff**2)))

# ---------------------------------------------------------------- A9 transport identity
W = 1 - (2*D*eta*M + d*sp.diff(M, eta))/X
Hc = D*eta + d*U
mat = lambda e: Dt(e) + u_r*Dr(e) + u_z*Dz(e)
check("A9 (d_t+u.grad)(q^b f) = q^(b-1)/L {W X f_X + H_c f_eta - b(1-2 eta U) f}",
      pw(mat(q**b*f) - q**(b-1)/L*(W*X*sp.diff(f, X) + Hc*sp.diff(f, eta) - b*(1 - 2*eta*U)*f)))

# ---------------------------------------------------------------- A10 angular/axial sources
H = sp.sqrt(2*X)*E                       # = 2 X F
l = X*sp.diff(sp.log(H), X)
Sq = -W*l - h*(1 - 2*eta*U) - Hc*sp.diff(sp.log(E), eta)
Sn = (-W*X*sp.diff(U, X) - A*(1 - 2*eta*U)*U - Hc*sp.diff(U, eta)
      - d*sp.diff(Pi, eta) + 4*A*eta*Pi + 2*eta*X*sp.diff(Pi, X))
check("A10 r u_th = q^(-h) H", pw(r*u_th - q**(-h)*H))
check("A10 (d_t+u.grad)(r u_th) = -q^(-h-1) H S_q / L", pw(mat(r*u_th) + q**(-h-1)*H*Sq/L))
check("A10 (d_t+u.grad)u_z + d_z p = -q^(-A-1) S_n / L", pw(mat(u_z) + Dz(p) + q**(-A-1)*Sn/L))

# ---------------------------------------------------------------- A11-A15 stress integration
Qs = sp.Function('Qs')(X, eta)
Ns = sp.Function('Ns')(X, eta)
# defining radial ODEs: D_X Q_s + (1+l) Q_s = S_q ;  D_X N_s + N_s = S_n
subsQ = {sp.Derivative(Qs, X): (Sq - (1 + l)*Qs)/X}
subsN = {sp.Derivative(Ns, X): (Sn - Ns)/X}
Gg = sp.Function('G')(X, eta)
kk = sp.symbols('k', real=True)
check("A12 (d_r + k/r)(q^(-A-1/2) G) = q^(-A-1)(sqrt(2X) G_X + k G/sqrt(2X))",
      pw(Dr(q**(-A-sp.Rational(1, 2))*Gg) + kk/r*q**(-A-sp.Rational(1, 2))*Gg
         - q**(-A-1)*(sp.sqrt(2*X)*sp.diff(Gg, X) + kk*Gg/sp.sqrt(2*X))))
a_sh = 1 - 2*X*sp.diff(sp.log(E), X)
bs = 2*X*sp.diff(U, X)/E
check("A13 a = 2 - 2 l", pw(a_sh - (2 - 2*l)))
check("A13 d_r u_th - u_th/r = -q^(-A-1/2) F a", pw(Dr(u_th) - u_th/r + q**(-A-sp.Rational(1, 2))*Ff*a_sh))
check("A13 d_r u_z = q^(-A-1/2) F b_s", pw(Dr(u_z) - q**(-A-sp.Rational(1, 2))*Ff*bs))
g1 = sp.Function('g1')(X, eta)
check("A14 (d_r+2/r)(d_r g - g/r) = (d_rr + r^-1 d_r - r^-2) g",
      pw((Dr(Dr(g1) - g1/r) + 2/r*(Dr(g1) - g1/r)) - (Dr(Dr(g1)) + Dr(g1)/r - g1/r**2)))
check("A14 (d_r+1/r) d_r g = d_rr g + r^-1 d_r g", pw((Dr(Dr(g1)) + Dr(g1)/r) - (Dr(Dr(g1)) + Dr(g1)/r)))

ps1 = X*Qs/L
ps2 = X*Ns/(L*E)
T0th = Ff*(ps1 - a_sh)
T0z = Ff*(ps2 + bs)
vlap_th = Dr(Dr(u_th)) + Dr(u_th)/r - u_th/r**2
slap_z = Dr(Dr(u_z)) + Dr(u_z)/r
R0th = mat(u_th) + u_r*u_th/r - vlap_th          # R(u,p).e_th + d_zz u_th (axisymmetric)
R0z = mat(u_z) + Dz(p) - slap_z                  # R(u,p).e_z + d_zz u_z
lhs_th = R0th + (Dr(q**(-A-sp.Rational(1, 2))*T0th) + 2/r*q**(-A-sp.Rational(1, 2))*T0th)
lhs_z = R0z + (Dr(q**(-A-sp.Rational(1, 2))*T0z) + 1/r*q**(-A-sp.Rational(1, 2))*T0z)
check("A15 R0_theta = -(d_r+2/r)(q^(-A-1/2) T0_theta)  [full, using the Q_s ODE]",
      pw(sp.expand(lhs_th).subs(subsQ)))
check("A15 R0_z = -(d_r+1/r)(q^(-A-1/2) T0_z)  [full, using the N_s ODE]",
      pw(sp.expand(lhs_z).subs(subsN)))
# regular primitives solve the ODEs: Q_s = int_0^X H S_q/(X H): check (X H Q_s)_X = H S_q form
check("A11 D_X Q + (1+l)Q = S_q  <=>  (X H Q)_X = H S_q",
      pw(sp.diff(X*H*Qs, X) - H*(X*sp.diff(Qs, X) + (1 + l)*Qs)))
# zero-stress equivalence (L228-233)
phi = C*Ff
Qz = -2*L*sp.diff(phi, X)/phi
Nz = -2*L*sp.diff(U, X)
check("A15b T0 = 0 <=> Q_s = -2L phi_X/phi (first slot)", pw(X*Qz/L - a_sh))
check("A15b T0 = 0 <=> N_s = -2L U_X (second slot)", pw(X*Nz/(L*E) + bs))
check("A15b zero-stress angular equation -2L(X phi_XX+2phi_X)/phi",
      pw(X*sp.diff(Qz, X) + (1 + l)*Qz + 2*L*(X*sp.diff(phi, X, 2) + 2*sp.diff(phi, X))/phi))
check("A15b zero-stress axial equation -2L(X U_XX + U_X)",
      pw(X*sp.diff(Nz, X) + Nz + 2*L*(X*sp.diff(U, X, 2) + sp.diff(U, X))))

# ---------------------------------------------------------------- A16 five moments
Ii = sp.Function('I')(X, eta)
Jj = sp.Function('J')(X, eta)
Ss = sp.Function('S')(X, eta)
mom = {sp.Derivative(Ii, X): H, sp.Derivative(Jj, X): U*H,
       sp.Derivative(Ss, X): U**2 - E**2/2, sp.Derivative(Pi, X): E**2/(2*X)}


def dmom(e):
    """d/dX using the moment rules, including mixed eta derivatives."""
    out = sp.diff(e, X)
    reps = {}
    for fun, val in ((Ii, H), (Jj, U*H), (Ss, U**2 - E**2/2), (Pi, E**2/(2*X))):
        reps[sp.Derivative(fun, X, eta)] = sp.diff(val, eta)
        reps[sp.Derivative(fun, eta, X)] = sp.diff(val, eta)
        reps[sp.Derivative(fun, X)] = val
    return out.subs(reps)


Qmom = -W + ((1 - h)*Ii - D*eta*sp.diff(Ii, eta) - d*sp.diff(Jj, eta) + 2*(h - D)*eta*Jj)/(X*H)
Nmom = -W*U + (D*(M - eta*sp.diff(M, eta)) + 4*h*eta*Ss - d*sp.diff(Ss, eta))/X + 4*A*eta*Pi - d*sp.diff(Pi, eta)
check("A16 (X H Q_s)_X = H S_q for the five-moment formula of Q_s",
      pw(dmom(X*H*Qmom) - (H*Sq).subs({sp.Derivative(Pi, X): E**2/(2*X)})))
check("A16 (X N_s)_X = S_n for the five-moment formula of N_s (Pi_X = E^2/2X)",
      pw(dmom(X*Nmom) - Sn.subs({sp.Derivative(Pi, X): E**2/(2*X)})))
check("A16 (X W)_X = 1 - 2 D eta U - d U_eta", pw(sp.diff(X*W, X) - (1 - 2*D*eta*U - d*sp.diff(U, eta))))

# ---------------------------------------------------------------- A17-A19 cone algebra
Pc, Jc, v = sp.symbols('P_c J_c v', real=True)
poly = 2*(Pc - v)**2 - (v - 2)*Jc**2
vp = Pc + Jc**2/4 + sp.sqrt(Jc**2)*sp.sqrt((Pc - 2)/2 + Jc**2/16)
vm = Pc + Jc**2/4 - sp.sqrt(Jc**2)*sp.sqrt((Pc - 2)/2 + Jc**2/16)
check("A17 v_+ is a root of 2(P-v)^2-(v-2)J^2", sp.simplify(sp.expand(poly.subs(v, vp))))
check("A17 v_- is a root of 2(P-v)^2-(v-2)J^2", sp.simplify(sp.expand(poly.subs(v, vm))))
check("A17 p(2) = 2(P-2)^2 and p(P) = -(P-2)J^2", sp.expand(poly.subs(v, 2) - 2*(Pc - 2)**2) + sp.expand(poly.subs(v, Pc) + (Pc - 2)*Jc**2))
aa, bb_, w_ = sp.symbols('a b_s w', real=True)
cc = 1 - bb_*w_/aa
jj = w_ + bb_/aa
vv = aa + bb_**2/aa
check("A18 (v-2)j^2 - 2c^2 = (1+b^2/a^2)((a-2)w^2+2bw+b^2/a-2)",
      sp.simplify((vv - 2)*jj**2 - 2*cc**2 - (1 + bb_**2/aa**2)*((aa - 2)*w_**2 + 2*bb_*w_ + bb_**2/aa - 2)))
p1, p2, FF = sp.symbols('p1 p2 FF', real=True)
ts = -bb_/aa
vs = aa*(1 + ts**2)
Pc_ = p1 + ts*p2
Jc_ = p2 - ts*p1
T0t, T0zz = FF*(p1 - aa), FF*(p2 + bb_)
check("A19 T0_th + t_s T0_z = F(P_c - v_s)", sp.simplify(T0t + ts*T0zz - FF*(Pc_ - vs)))
check("A19 T0_z - t_s T0_th = F J_c", sp.simplify(T0zz - ts*T0t - FF*Jc_))

# ---------------------------------------------------------------- A20-A21 heat exterior
Z, vv2 = sp.symbols('Z v', positive=True)
integrand = sp.exp(-vv2)*vv2**h*(1 + Z*vv2)**(-h)
ode_integrand = (Z**2*sp.diff(integrand, Z, 2) + ((2 + 2*h)*Z + 1)*sp.diff(integrand, Z) + h*(1 + h)*integrand)
Bv = sp.exp(-vv2)*vv2**(h + 1)*(1 + Z*vv2)**(-h - 1)
check("A20 heat ODE integrand = h * d/dv[e^-v v^(h+1)(1+Zv)^(-h-1)]", sp.simplify(ode_integrand - h*sp.diff(Bv, vv2)))
check("A20 positivity numerator A(1+Zv) - h Z v = A + Zv/2", sp.expand(A*(1 + Z*vv2) - h*Z*vv2 - (A + Z*vv2/2)))
# numerical confirmation of the ODE for the actual integral at h = 1/137, several Z
import mpmath as mpm
mpm.mp.dps = 30
hh = mpm.mpf(1)/137
Hf = lambda ZZ: mpm.quad(lambda vv: mpm.e**(-vv)*vv**hh*(1 + ZZ*vv)**(-hh), [0, 1, 10, mpm.inf])/mpm.gamma(1 + hh)
worst = 0
for ZZ in [mpm.mpf('0.1'), mpm.mpf('0.7'), mpm.mpf(3), mpm.mpf(20)]:
    H0 = Hf(ZZ)
    H1 = mpm.diff(Hf, ZZ)
    H2 = mpm.diff(Hf, ZZ, 2)
    worst = max(worst, abs(ZZ**2*H2 + ((2 + 2*hh)*ZZ + 1)*H1 + hh*(1 + hh)*H0))
ok = worst < mpm.mpf('1e-15')
results.append(("A20n heat ODE holds numerically for the quadrature (h=1/137)", ok))
print(("PASS" if ok else "FAIL") + "  A20n heat ODE numerically at Z in {0.1,0.7,3,20}: max residual " + mpm.nstr(worst, 3))
check("A20n H(0) = 1 (Gamma normalisation)", 0 if abs(Hf(0) - 1) < mpm.mpf('1e-20') else 1)

# radial heat equation for K = c s^(-A) H(2 tau/s), s = r^2/2
cinf, tau, s_ = sp.symbols('c_inf tau s', positive=True)
Hh = sp.Function('Hh')
K = cinf*s_**(-A)*Hh(2*tau/s_)
ds = lambda e: sp.diff(e, s_)
dr_K = lambda e: sp.sqrt(2*s_)*ds(e)          # d_r = r d_s, r = sqrt(2 s)
oper = dr_K(dr_K(K)) + dr_K(K)/sp.sqrt(2*s_) - K/(2*s_)
Zs = 2*tau/s_
Hp = sp.Subs(sp.Derivative(Hh(Z), Z), Z, Zs).doit()
claim_oper = cinf*s_**(-A-1)*((2*A**2 - sp.Rational(1, 2))*Hh(Zs) + (4*A + 2)*Zs*sp.diff(Hh(Zs), tau)*s_/2 + 2*Zs**2*sp.diff(Hh(Zs), tau, 2)*s_**2/4)
check("A21 (d_rr + r^-1 d_r - r^-2)K = c s^(-A-1){(2A^2-1/2)H + (4A+2)Z H' + 2 Z^2 H''}", sp.simplify(oper - claim_oper))
check("A21 d_t K = -2 c s^(-A-1) H'   (d_t = -d_tau)", sp.simplify(-sp.diff(K, tau) - (-2*cinf*s_**(-A-1)*sp.diff(Hh(Zs), tau)*s_/2)))
check("A21 2A^2 - 1/2 = 2h(1+h)", sp.expand(2*A**2 - sp.Rational(1, 2) - 2*h*(1 + h)))
# heat equation <=> ODE: -d_tau K - oper = -c s^(-A-1) * 2*[Z^2H''+((2+2h)Z+1)H'+h(1+h)H]
Hz = sp.Function('Hz')(Z)
lhs = (-2*sp.diff(Hz, Z)) - ((2*A**2 - sp.Rational(1, 2))*Hz + (4*A + 2)*Z*sp.diff(Hz, Z) + 2*Z**2*sp.diff(Hz, Z, 2))
ode = Z**2*sp.diff(Hz, Z, 2) + ((2 + 2*h)*Z + 1)*sp.diff(Hz, Z) + h*(1 + h)*Hz
check("A21 heat equation d_tK = (d_rr+r^-1d_r-r^-2)K is -2 x (source ODE)", sp.expand(lhs + 2*ode))
check("A21 q^-A c X^-A H(2d/X) = c s^-A H(2 tau/s)",
      pw((q**(-A)*cinf*X**(-A)*Hh(2*d/X)).subs(X, s_/q) - cinf*s_**(-A)*Hh(2*d*q/s_)))
# Theorem 3.1 (3.5) normalisation: s^-A H(2tau/s) = 2^A r^(-1-2h) H(4 tau/r^2)
rr = sp.symbols('rr', positive=True)
check("A21 s^-A = 2^A r^(-1-2h) and 2tau/s = 4tau/r^2 (H_ext(Z) = 2^A c H(4Z))",
      pw((rr**2/2)**(-A) - 2**A*rr**(-1-2*h)) + sp.simplify(2*tau/(rr**2/2) - 4*tau/rr**2))

# ---------------------------------------------------------------- B viscous operators, orders n
phi_ = sp.Function('phi')(X, eta)
Uf = sp.Function('Uf')(X, eta)
Vf = sp.Function('Vf')(X, eta)
check("B1 (d_rr + r^-1 d_r - r^-2)(r phi(X)) = (2r/q)(X phi_XX + 2 phi_X)",
      pw(Dr(Dr(r*phi_)) + Dr(r*phi_)/r - phi_*r/r**2 - 2*r/q*(X*sp.diff(phi_, X, 2) + 2*sp.diff(phi_, X))))
check("B2 (d_rr + r^-1 d_r) U(X) = (2/q)(X U_XX + U_X)",
      pw(Dr(Dr(Uf)) + Dr(Uf)/r - 2/q*(X*sp.diff(Uf, X, 2) + sp.diff(Uf, X))))
check("B3 (d_rr + r^-1 d_r - r^-2)(V(X)/r) = (2X/(q r)) V_XX",
      pw(Dr(Dr(Vf/r)) + Dr(Vf/r)/r - Vf/r**3 - 2*X/(q*r)*sp.diff(Vf, X, 2)))
xi = sp.symbols('xi', positive=True)
gx = sp.Function('gx')
G_ = gx(xi**2)
Xs = sp.symbols('Xs', positive=True)
lhs1 = (2*(Xs*sp.diff(gx(Xs), Xs, 2) + 2*sp.diff(gx(Xs), Xs))).subs(Xs, xi**2)
rhs1 = sp.Rational(1, 2)*(sp.diff(G_, xi, 2) + 3/xi*sp.diff(G_, xi))
check("B4 2(X d_XX + 2 d_X) = (1/2)(d_xixi + 3 xi^-1 d_xi), X = xi^2", sp.simplify(sp.expand(lhs1 - rhs1.doit())))
lhs2 = (2*(Xs*sp.diff(gx(Xs), Xs, 2) + sp.diff(gx(Xs), Xs))).subs(Xs, xi**2)
rhs2 = sp.Rational(1, 2)*(sp.diff(G_, xi, 2) + 1/xi*sp.diff(G_, xi))
check("B4 2(X d_XX + d_X) = (1/2)(d_xixi + xi^-1 d_xi)", sp.simplify(sp.expand(lhs2 - rhs2.doit())))
# K_n = A_X U - U satisfies K_xi + 2K/xi = -U_xi  (A_X U = M/X, X = xi^2)
Mx = sp.Function('Mx')
Kn = Mx(xi**2)/xi**2 - sp.diff(Mx(Xs), Xs).subs(Xs, xi**2)
Un = sp.diff(Mx(Xs), Xs).subs(Xs, xi**2)
check("B5 K_xi + 2K/xi = -U_xi for K = A_X U - U", sp.simplify(sp.diff(Kn, xi) + 2*Kn/xi + sp.diff(Un, xi)))
lam = sp.symbols('lambda_n', real=True)
Mn = sp.Function('Mn')(X, eta)
Unn = sp.diff(Mn, X)
Vn = (2*eta*X*Unn - 2*eta*(D + lam)*Mn - d*sp.diff(Mn, eta))/L
Knn = Mn/X - Unn
check("B6 V_n/X = (2eta(A-lam)U - 2eta(D+lam)K - d(U_eta + K_eta))/L",
      pw(Vn/X - (2*eta*(A - lam)*Unn - 2*eta*(D + lam)*Knn - d*(sp.diff(Unn, eta) + sp.diff(Knn, eta)))/L))
check("B6 (V_n)_X = -Z_(-A+lam) U_n  (order-n continuity)", pw(sp.diff(Vn, X) + Zb(-A + lam, Unn)))

print("\nsummary: %d checks, %d PASS, %d FAIL" % (len(results), sum(ok for _, ok in results), sum(not ok for _, ok in results)))
