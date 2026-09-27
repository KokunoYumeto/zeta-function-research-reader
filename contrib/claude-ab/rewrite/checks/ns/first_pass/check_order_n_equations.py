"""Assembled check of the reader's order-n coefficient equations (phi), (U), (Pi), (Omega)
(navier_stokes_workbench.tex L1011-1075; source (5.2)-(5.6), pp. 46-47).

Fields (reader L1011-1017):  u_th = sum_n r q^(b+lam_n) phi_n / C  (b = -A-1/2),
u_z = sum_n q^(-A+lam_n) U_n,  r u_r = sum_n q^(lam_n) V_n,  p = sum_n q^(-2A+lam_n) Pi_n,
lam_n = 2 n h, with V_n from the order-n continuity formula (reader eq. (V)).

We build the FULL Navier-Stokes momentum residual (viscosity one, including axial
viscosity) for generic profile functions of orders n = 0, 1, 2, expand it in powers
of q (h = 1/100 fixed, q = w^100 so every exponent is an integer power of w), and
compare the coefficient of each order with the displayed coefficient equations.
Own code for the inv_NS audit; nothing is imported from the bundle.
"""
import sympy as sp
import time

t0 = time.time()
results = []


def report(name, ok, extra=""):
    results.append((name, ok))
    print(("PASS" if ok else "FAIL") + "  " + name + ("" if ok else "  " + extra))


q, X, w = sp.symbols('q X w', positive=True)
eta = sp.symbols('eta', real=True)
h = sp.Rational(1, 100)
A = sp.Rational(1, 2) + h
D = sp.Rational(1, 2) - h
d = 1 - eta**2
Lf = sp.Function('Lf')
L = Lf(eta)          # kept as an unevaluated function of eta so that denominators stay monomial
Lval = 1 - 2*h*eta**2
r = sp.sqrt(2*q*X)
C = sp.symbols('C', positive=True)
N = 3                                            # orders 0, 1, 2
lam = [2*n*h for n in range(N)]

qt_, et_, Xt_ = -1/L, D*eta/(q*L), X/(q*L)
qz_, ez_, Xz_ = 2*eta*q**(1-D)/L, d/(q**D*L), -2*eta*X/(q**D*L)
Dt = lambda e: qt_*sp.diff(e, q) + et_*sp.diff(e, eta) + Xt_*sp.diff(e, X)
Dz = lambda e: qz_*sp.diff(e, q) + ez_*sp.diff(e, eta) + Xz_*sp.diff(e, X)
Dr = lambda e: (r/q)*sp.diff(e, X)
Tb = lambda bb, g: (-bb*g + D*eta*sp.diff(g, eta) + X*sp.diff(g, X))/L
Zb = lambda bb, g: (2*bb*eta*g + d*sp.diff(g, eta) - 2*eta*X*sp.diff(g, X))/L

phi = [sp.Function('phi%d' % n)(X, eta) for n in range(N)]
Mf = [sp.Function('M%d' % n)(X, eta) for n in range(N)]        # F_n = int_0^X U_n
U = [sp.diff(Mf[n], X) for n in range(N)]
Pi = [sp.Function('Pi%d' % n)(X, eta) for n in range(N)]
V = [(2*eta*X*U[n] - 2*eta*(D + lam[n])*Mf[n] - d*sp.diff(Mf[n], eta))/L for n in range(N)]
E = [sp.sqrt(2*X)*phi[n]/C for n in range(N)]
b = -A - sp.Rational(1, 2)
c = -A

u_th = sum(r*q**(b + lam[n])*phi[n]/C for n in range(N))
u_z = sum(q**(c + lam[n])*U[n] for n in range(N))
u_r = sum(q**lam[n]*V[n] for n in range(N))/r
p = sum(q**(-2*A + lam[n])*Pi[n] for n in range(N))


def to_w(e):
    e = sp.expand(e)
    e = e.subs(q, w**100)
    e = sp.powdenest(sp.expand_power_base(e, force=True), force=True)
    return sp.expand(e)


def coeff_w(e, k):
    return sp.expand(e).coeff(w, k)


def evalL(e):
    """replace Lf and its eta-derivatives by 1 - 2 h eta^2"""
    e = e.subs({sp.Derivative(Lf(eta), (eta, 3)): 0, sp.Derivative(Lf(eta), (eta, 2)): -4*h,
                sp.Derivative(Lf(eta), eta): -4*h*eta})
    return e.subs(Lf(eta), Lval)


# continuity for every order (exact; not only generic-order formula)
cont = sp.diff(r*u_r, X)/q + Dz(u_z)   # d_s(r u_r) + d_z u_z with d_s = (1/q) d_X
report("continuity holds order by order (sum over n = 0..2)", sp.simplify(evalL(to_w(cont))) == 0)

# ---------------- angular equation
res_th = Dt(u_th) + u_r*Dr(u_th) + u_z*Dz(u_th) + u_r*u_th/r \
    - (Dr(Dr(u_th)) + Dr(u_th)/r - u_th/r**2) - Dz(Dz(u_th))
norm_th = to_w(res_th/(r*q**(b - 1)/C))
for n in range(N):
    claim = Tb(b + lam[n], phi[n]) - 2*(X*sp.diff(phi[n], X, 2) + 2*sp.diff(phi[n], X))
    for i in range(N):
        j = n - i
        if 0 <= j < N:
            claim += V[i]*(sp.diff(phi[j], X) + phi[j]/X) + U[i]*Zb(b + lam[j], phi[j])
    if n >= 1:
        claim -= Zb(b + lam[n-1] - D, Zb(b + lam[n-1], phi[n-1]))
    k = int(100*lam[n])
    diff = sp.simplify(evalL(coeff_w(norm_th, k) - sp.expand(claim)))
    report("angular coefficient equation (phi) at order n=%d" % n, diff == 0, str(diff)[:200])

# ---------------- axial equation
res_z = Dt(u_z) + u_r*Dr(u_z) + u_z*Dz(u_z) + Dz(p) - (Dr(Dr(u_z)) + Dr(u_z)/r) - Dz(Dz(u_z))
norm_z = to_w(res_z/q**(c - 1))
for n in range(N):
    claim = Tb(c + lam[n], U[n]) + Zb(-2*A + lam[n], Pi[n]) - 2*(X*sp.diff(U[n], X, 2) + sp.diff(U[n], X))
    for i in range(N):
        j = n - i
        if 0 <= j < N:
            claim += V[i]*sp.diff(U[j], X) + U[i]*Zb(c + lam[j], U[j])
    if n >= 1:
        claim -= Zb(c + lam[n-1] - D, Zb(c + lam[n-1], U[n-1]))
    k = int(100*lam[n])
    diff = sp.simplify(evalL(coeff_w(norm_z, k) - sp.expand(claim)))
    report("axial coefficient equation (U) at order n=%d" % n, diff == 0, str(diff)[:200])

# ---------------- radial equation times r
res_r = Dt(u_r) + u_r*Dr(u_r) + u_z*Dz(u_r) - u_th**2/r + Dr(p) \
    - (Dr(Dr(u_r)) + Dr(u_r)/r - u_r/r**2) - Dz(Dz(u_r))
norm_r = to_w(r*res_r*q)          # multiply by q: power q^(lam) <-> q^(lam-1)


def Omega(k):
    out = Tb(lam[k], V[k]) - 2*X*sp.diff(V[k], X, 2)
    # careful: T_lam V (sign -lam V) from r d_t(q^lam V / r)
    for i in range(N):
        j = k - i
        if 0 <= j < N:
            out += V[i]*(sp.diff(V[j], X) - V[j]/(2*X)) + U[i]*Zb(lam[j], V[j])
    if k >= 1:
        out -= Zb(lam[k-1] - D, Zb(lam[k-1], V[k-1]))
    return out


for m in (-1, 0, 1):
    claim = 0
    if m >= 0:
        claim += Omega(m)
    n = m + 1
    claim += 2*X*sp.diff(Pi[n], X) - sum(E[i]*E[n-i] for i in range(N) if 0 <= n - i < N)
    k = int(100*(2*h*m)) if m >= 0 else -2          # q^(lam_m) with q^(-2A+lam_(m+1)) = q^(lam_m - 1)
    # after multiplying by q, terms q^(lam_m - 1) -> q^(lam_m); for m = -1: q^(-2h) -> w^-2
    diff = sp.simplify(evalL(coeff_w(norm_r, k) - sp.expand(claim)))
    report("radial equation x r at q^(lam_%d - 1): Omega_%d + 2X Pi_%d,X - sum E_iE_j (eqs. (Pi),(Omega))" % (m, m, n)
           if m >= 0 else "radial equation x r at q^(-2A): 2X Pi_0,X - E_0^2 (leading pressure balance)",
           diff == 0, str(diff)[:200])

print("\nsummary: %d checks, %d PASS, %d FAIL; %.1f s" % (len(results), sum(o for _, o in results),
                                                      sum(not o for _, o in results), time.time() - t0))
