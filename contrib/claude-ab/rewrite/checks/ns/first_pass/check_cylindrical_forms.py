"""Cylindrical conservative forms used by the reader: weighted residual identities (L1325-1336),
radial stress primitives (L1377-1383), mean-correction transport and vector Laplacian (MC11, L3545-3579),
and the integrating-factor identity int R^e (d_R + e/R) h dR = 0 (L3673).  Own sympy code (inv_NS audit).
Here Delta_0 = d_RR + R^-1 d_R + d_zz."""
import sympy as sp

res = []


def check(name, expr):
    ok = (sp.simplify(sp.expand(expr)) == 0) if not isinstance(expr, sp.MatrixBase) else all(sp.simplify(sp.expand(x)) == 0 for x in expr)
    res.append((name, ok))
    print(("PASS" if ok else "FAIL") + "  " + name)


R, th, z, t = sp.symbols('R theta z t', real=True)
# (1) conservative vs non-conservative transport differ exactly by U_i * div U (generic polar components)
Ur, Ut, Uz = [sp.Function(n)(R, th, z) for n in ('Ur', 'Ut', 'Uz')]
Dr = lambda f: sp.diff(f, R)
Dth = lambda f: sp.diff(f, th)
Dz = lambda f: sp.diff(f, z)
divU = Dr(Ur) + Ur/R + Dth(Ut)/R + Dz(Uz)
ncr = Ur*Dr(Ur) + Ut*Dth(Ur)/R + Uz*Dz(Ur) - Ut**2/R
nct = Ur*Dr(Ut) + Ut*Dth(Ut)/R + Uz*Dz(Ut) + Ur*Ut/R
ncz = Ur*Dr(Uz) + Ut*Dth(Uz)/R + Uz*Dz(Uz)
check("MC11 r: conservative form = standard cylindrical (U.grad U)_r + U_r div U",
      (Dr(Ur**2) + Ur**2/R + Dth(Ut*Ur)/R + Dz(Uz*Ur) - Ut**2/R) - (ncr + Ur*divU))
check("MC11 theta: conservative form (radial weight 2) = (U.grad U)_th + U_th div U",
      (Dr(Ur*Ut) + 2*Ur*Ut/R + Dth(Ut**2)/R + Dz(Uz*Ut)) - (nct + Ut*divU))
check("MC11 z: conservative form = (U.grad U)_z + U_z div U",
      (Dr(Ur*Uz) + Ur*Uz/R + Dth(Ut*Uz)/R + Dz(Uz**2)) - (ncz + Uz*divU))
# (2) vector Laplacian from the frame rules d_th e_r = e_th, d_th e_th = -e_r (frame-independent of R, z)
er_, et_, ez_ = sp.Matrix([sp.cos(th), sp.sin(th), 0]), sp.Matrix([-sp.sin(th), sp.cos(th), 0]), sp.Matrix([0, 0, 1])
Uvec = Ur*er_ + Ut*et_ + Uz*ez_
lapvec = sp.diff(Uvec, R, 2) + sp.diff(Uvec, R)/R + sp.diff(Uvec, th, 2)/R**2 + sp.diff(Uvec, z, 2)
lap0 = lambda f: sp.diff(f, R, 2) + sp.diff(f, R)/R + sp.diff(f, z, 2)
check("vector Laplacian r-component (frame calculus)", (lapvec.T*er_)[0] - (lap0(Ur) + sp.diff(Ur, th, 2)/R**2 - Ur/R**2 - 2*Dth(Ut)/R**2))
check("vector Laplacian theta-component", (lapvec.T*et_)[0] - (lap0(Ut) + sp.diff(Ut, th, 2)/R**2 - Ut/R**2 + 2*Dth(Ur)/R**2))
check("vector Laplacian z-component", (lapvec.T*ez_)[0] - (lap0(Uz) + sp.diff(Uz, th, 2)/R**2))
# (3) instance check of the standard non-conservative cylindrical advection against Cartesian (random points)
import random
X_, Y_, Z_ = sp.symbols('X Y Z', real=True)
psi = [X_*Y_*Z_*sp.exp(-X_**2), sp.sin(Y_)*Z_**2 + X_**3, X_**3*sp.cos(Z_) + Y_**2*X_]
cart = (X_, Y_, Z_)
u = [sp.diff(psi[2], Y_) - sp.diff(psi[1], Z_), sp.diff(psi[0], Z_) - sp.diff(psi[2], X_), sp.diff(psi[1], X_) - sp.diff(psi[0], Y_)]
adv = [sum(u[k]*sp.diff(u[i], cart[k]) for k in range(3)) for i in range(3)]
to_pol = {X_: R*sp.cos(th), Y_: R*sp.sin(th), Z_: z}
e_r, e_t = (sp.cos(th), sp.sin(th), 0), (-sp.sin(th), sp.cos(th), 0)
comp = lambda v, e: sum(v[i]*e[i] for i in range(3))
ur_e, ut_e, uz_e = [sp.simplify(comp(u, e).subs(to_pol)) for e in (e_r, e_t, (0, 0, 1))]
advr_e = comp(adv, e_r).subs(to_pol)
ncr_e = ur_e*sp.diff(ur_e, R) + ut_e*sp.diff(ur_e, th)/R + uz_e*sp.diff(ur_e, z) - ut_e**2/R
div_e = sp.diff(ur_e, R) + ur_e/R + sp.diff(ut_e, th)/R + sp.diff(uz_e, z)
random.seed(3)
worst = 0
for _ in range(5):
    pt = {R: random.uniform(0.3, 2), th: random.uniform(0, 6.28), z: random.uniform(-1, 1)}
    worst = max(worst, abs(float((advr_e - ncr_e).subs(pt))), abs(float(div_e.subs(pt))))
check("instance: Cartesian (u.grad u).e_r equals the cylindrical formula, and div = 0 (5 random points, |err| < 1e-10)", sp.Integer(0) if worst < 1e-10 else sp.Integer(1))
# axisymmetric conservative residual identities (L1329-1334), viscosity one
r_ = sp.symbols('r', positive=True)
S = sp.Function('S')(r_, z, t)                 # Stokes streamfunction: r u_r = -d_z S, u_z = d_r S / r  => div = 0
ur = -sp.diff(S, z)/r_
uz = sp.diff(S, r_)/r_
ut = sp.Function('ut')(r_, z, t)
p = sp.Function('p')(r_, z, t)
check("axisymmetric: d_r(r u_r) + r d_z u_z = 0", sp.diff(r_*ur, r_) + r_*sp.diff(uz, z))
res_th = sp.diff(ut, t) + ur*sp.diff(ut, r_) + uz*sp.diff(ut, z) + ur*ut/r_ - (sp.diff(ut, r_, 2) + sp.diff(ut, r_)/r_ - ut/r_**2 + sp.diff(ut, z, 2))
res_z = sp.diff(uz, t) + ur*sp.diff(uz, r_) + uz*sp.diff(uz, z) + sp.diff(p, z) - (sp.diff(uz, r_, 2) + sp.diff(uz, r_)/r_ + sp.diff(uz, z, 2))
cons_th = sp.diff(r_**2*ut, t) + sp.diff(r_**2*ur*ut, r_) + sp.diff(r_**2*uz*ut, z) - sp.diff(r_**2*sp.diff(ut, r_) - r_*ut, r_) - sp.diff(r_**2*ut, z, 2)
cons_z = sp.diff(r_*uz, t) + sp.diff(r_*ur*uz, r_) + sp.diff(r_*(uz**2 + p), z) - sp.diff(r_*sp.diff(uz, r_), r_) - sp.diff(r_*uz, z, 2)
check("L1330: r^2 R_theta = d_t(r^2u_th) + d_r(r^2 u_r u_th) + d_z(r^2 u_z u_th) - d_r(r^2 u_th,r - r u_th) - d_zz(r^2 u_th)", r_**2*res_th - cons_th)
check("L1333: r R_z = d_t(r u_z) + d_r(r u_r u_z) + d_z(r(u_z^2 + p)) - d_r(r u_z,r) - d_zz(r u_z)", r_*res_z - cons_z)
# radial stress primitives (L1377-1383): T_theta = -R^-2 int_0^R rho^2 r_theta, T_z = -R^-1 int_0^R rho r_z
Rr = sp.symbols('R', positive=True)
g1 = sp.Function('g1')(Rr)
G2 = sp.Function('G2')(Rr)            # G2' = R^2 r_theta
G1 = sp.Function('G1')(Rr)            # G1' = R r_z
Tth = -G2/Rr**2
Tz = -G1/Rr
check("L1382: (d_R + 2/R) T_theta = -r_theta with T_theta = -R^-2 int rho^2 r_theta",
      (sp.diff(Tth, Rr) + 2*Tth/Rr).subs(sp.Derivative(G2, Rr), Rr**2*g1) + g1)
check("L1383: (d_R + 1/R) T_z = -r_z with T_z = -R^-1 int rho r_z",
      (sp.diff(Tz, Rr) + Tz/Rr).subs(sp.Derivative(G1, Rr), Rr*g1) + g1)
e = sp.symbols('e', integer=True)
hh = sp.Function('h')(Rr)
check("L3673: R^e (d_R + e/R) h = d_R(R^e h) (so compactly supported fluxes integrate to zero)", Rr**e*(sp.diff(hh, Rr) + e*hh/Rr) - sp.diff(Rr**e*hh, Rr))
check("L1352: int R Pi dR = -(1/2) int R^2 Pi_R dR (integration by parts; boundary term R^2 Pi/2)",
      sp.diff(Rr**2*hh/2, Rr) - (Rr*hh + Rr**2*sp.diff(hh, Rr)/2))
print("\nsummary: %d checks, %d PASS, %d FAIL" % (len(res), sum(o for _, o in res), sum(not o for _, o in res)))
