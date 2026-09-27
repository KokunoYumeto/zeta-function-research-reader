"""Actual-shear correction identities (reader L45-60 and L13543-13777, (AS7)-(AS40);
bundle proof_sources/lanes/web_bundle_audit/actual_shear_energy_morphism.md) and the
ambient projection (reader L14207-14229).  Own sympy code for the inv_NS audit."""
import sympy as sp

res = []


def check(name, expr):
    e = sp.simplify(sp.expand(expr)) if not isinstance(expr, sp.MatrixBase) else sp.simplify(expr)
    ok = (e == 0) if not isinstance(e, sp.MatrixBase) else all(sp.simplify(x) == 0 for x in e)
    res.append((name, ok))
    print(("PASS" if ok else "FAIL") + "  " + name + ("" if ok else "  residual " + str(e)[:200]))


# (AS14)/(AS24): t^T K t = g . T,  T = t_r (t_th, t_z)
F, gth, gz, F0, g0th, g0z = sp.symbols('F g_th g_z F0 g0_th g0_z', real=True)
tr_, tth, tz = sp.symbols('t_r t_th t_z', real=True)
t = sp.Matrix([tr_, tth, tz])
Kmat = lambda F_, a, b: sp.Matrix([[0, -2*F_, 0], [2*F_ + a, 0, 0], [b, 0, 0]])
K = Kmat(F, gth, gz)
K0 = Kmat(F0, g0th, g0z)
T = sp.Matrix([tr_*tth, tr_*tz])
g = sp.Matrix([gth, gz])
g0 = sp.Matrix([g0th, g0z])
check("AS24 t^T K(F,g) t = g.T (source p.81 display)", (t.T*K*t)[0] - (g.T*T)[0])
dK = K - K0
check("AS26-aux t^T dK t = (g - g0).T; both 2dF entries cancel", (t.T*dK*t)[0] - ((g - g0).T*T)[0])
# (AS26): -g.T = -|g0| T_N - (g - g0).T, N = g0/|g0|, K = (-N_z, N_th)
g0n = sp.sqrt(g0th**2 + g0z**2)
N = g0/g0n
Kv = sp.Matrix([-N[1], N[0]])
TN = (T.T*N)[0]
TK = (T.T*Kv)[0]
check("AS26 (N,K) orthonormal: N.K = 0, |K| = 1", (N.T*Kv)[0] + sp.simplify((Kv.T*Kv)[0] - 1))
check("AS26 T = T_N N + T_K K", T - (TN*N + TK*Kv))
check("AS26 -g.T = -|g0| T_N - (g-g0).T", -(g.T*T)[0] - (-g0n*TN - ((g - g0).T*T)[0]))

# (AS17)-(AS19): pressure from the constraint and A - A0 = -Pi_n dK
n1, n2, n3, m1, m2, m3 = sp.symbols('n1 n2 n3 m1 m2 m3', real=True)   # n and n' = dn/dv
k_, m_, damp = sp.symbols('k m d', nonzero=True)
nv = sp.Matrix([n1, n2, n3])
npr = sp.Matrix([m1, m2, m3])
f1, f2, f3 = sp.symbols('f1 f2 f3')
fv = sp.Matrix([f1, f2, f3])
nn = (nv.T*nv)[0]
Pin = sp.eye(3) - nv*nv.T/nn
pi_formula = lambda KK, tt, ff: sp.I/(k_*m_)*((nv.T*KK*tt)[0] - (npr.T*tt)[0] + (nv.T*ff)[0])/nn
Aop = lambda KK: -KK + nv*(nv.T*KK - npr.T)/nn
# t' from (AS16) with pi substituted must equal A t - m^2 d t - Pi_n f, on the constraint n.t = 0
t1, t2 = sp.symbols('s1 s2')
# parametrize t with n^T t = 0: t = t1*a1 + t2*a2 with a1, a2 spanning n-perp (generic)
a1 = sp.Matrix([n2, -n1, 0])
a2 = sp.Matrix([n3, 0, -n1])
tt = t1*a1 + t2*a2
tprime = -K*tt - m_**2*damp*tt - sp.I*k_*m_*nv*pi_formula(K, tt, fv) - fv
check("AS17-18 t' = A t - m^2 d t - Pi_n f after substituting the pressure", tprime - (Aop(K)*tt - m_**2*damp*tt - Pin*fv))
# consistency: n^T t' = -n'^T t (differentiated constraint) holds for the solved t'
check("AS17 solved t' satisfies n^T t' = -n'^T t", (nv.T*tprime)[0] + (npr.T*tt)[0])
check("AS19 A - A0 = -Pi_n dK", Aop(K) - Aop(K0) + Pin*dK)
# (AS20)-(AS22) bijection of constrained solution data
f0 = fv + Pin*dK*tt
pi = pi_formula(K, tt, fv)
pi0 = pi - sp.I/(k_*m_)*(nv.T*dK*tt)[0]/nn
lhs_K = -K*tt - m_**2*damp*tt - sp.I*k_*m_*nv*pi - fv          # = t'
lhs_K0 = tprime + K0*tt + m_**2*damp*tt + sp.I*k_*m_*nv*pi0     # t' + K0 t + m^2 d t + ikm n pi0
check("AS21 (t, f0, pi0) solves the K0 equation with right side -f0", lhs_K0 + f0)
check("AS22 inverse map returns (f, pi)", (f0 - Pin*dK*tt - fv) + sp.Matrix([pi0 + sp.I/(k_*m_)*(nv.T*dK*tt)[0]/nn - pi, 0, 0]))
# (AS25): (1/2) d|t|^2/dv = -g.T - d|t|^2 for real t with n.t = 0, m = 1, f = 0 (normal term orthogonal)
treal = t1*a1 + t2*a2
tp = Aop(K)*treal - damp*treal
check("AS25 t.(A t - d t) = -t^T K t - d|t|^2 (normal term drops since n.t = 0)",
      (treal.T*tp)[0] - (-(treal.T*K*treal)[0] - damp*(treal.T*treal)[0]))

# (AS7): derivative formula for delta g_theta = d_R dV - dV/R
R = sp.symbols('R', positive=True)
dV = sp.Function('dV')(R)
for iR in range(0, 5):
    lhs = sp.diff(sp.diff(dV, R) - dV/R, R, iR)
    rhs = sp.diff(dV, R, iR + 1) - sum(sp.binomial(iR, j)*(-1)**j*sp.factorial(j)*R**(-j-1)*sp.diff(dV, R, iR - j)
                                       for j in range(iR + 1))
    check("AS7 d_R^%d(d_R dV - dV/R) formula" % iR, lhs - rhs)

# (AS11)-(AS13): first-jet map and its inverse
v_, vR, w_, wR, a_, b_ = sp.symbols('v v_R w w_R a b')
LR = sp.Matrix([[-1/R, 1, 0, 0], [0, 0, 0, 1]])
j = sp.Matrix([v_, vR, w_, wR])
Jmap = lambda jj: list(LR*jj) + [jj[0], jj[2]]
Jinv = lambda a, b, v, w: sp.Matrix([v, a + v/R, w, b])
img = Jmap(j)
check("AS12 J^-1 J = id", Jinv(img[0], img[1], img[2], img[3]) - j)
back = Jmap(Jinv(a_, b_, v_, w_))
check("AS12 J J^-1 = id", sp.Matrix(back) - sp.Matrix([a_, b_, v_, w_]))
check("AS13 ker L_R contains (v, v/R, w, 0)", LR*sp.Matrix([v_, v_/R, w_, 0]))

# (AS33)-(AS34): production decomposition; (AS38) norm identity
s_, gam0, x_, y_ = sp.symbols('s gamma0 x y', real=True)
e1, e2 = sp.symbols('e1 e2', real=True)
eT = sp.Matrix([e1, e2])
dg1, dg2 = sp.symbols('dg1 dg2', real=True)
dg = sp.Matrix([dg1, dg2])
Tform = x_**2*(-s_*Kv + gam0*N + eT)
gfull = g0 + dg
check("AS34 -g.T/x^2 = -|g0| gamma0 - g0.e_T - dg.(-sK + gamma0 N + e_T)",
      -(gfull.T*Tform)[0]/x_**2 - (-g0n*gam0 - (g0.T*eT)[0] - (dg.T*(-s_*Kv + gam0*N + eT))[0]))
# frame (e_r, K_a, N_a) orthonormal with K_a, N_a in the (theta, z) plane
ang = sp.symbols('alpha', real=True)
er = sp.Matrix([1, 0, 0])
Ka = sp.Matrix([0, sp.cos(ang), sp.sin(ang)])
Na = sp.Matrix([0, Ka[2], -Ka[1]])
sa = sp.symbols('s_a', real=True)
tvec = x_*(er - sa*Ka) + y_*Na
check("AS38 |t|^2 = (1 + s_a^2) x^2 + y^2", (tvec.T*tvec)[0] - ((1 + sa**2)*x_**2 + y_**2))

# ambient projection (reader L14209-14221): B^l B = I2, B B^l = I3 - K_a n^T/|n_tan|
c0 = sp.symbols('c0', nonzero=True)
ss = sp.symbols('sigma', real=True)
Umat = sp.Matrix.hstack(er - sa*Ka, Na)
Mm = sp.Matrix([[1, 1], [c0*sp.sqrt(1 + ss**2), -c0*sp.sqrt(1 + ss**2)]])
Bm = Umat*Mm
Wa = sp.Matrix.vstack(er.T, Na.T)
Bl = Mm.inv()*Wa
ntan = sp.symbols('ntan', positive=True)
nPhi = ntan*(sa*er + Ka)
check("proj W_a U = I_2", Wa*Umat - sp.eye(2))
check("proj B^l B = I_2", sp.simplify(Bl*Bm) - sp.eye(2))
check("proj B B^l = I_3 - K_a n^T/|n_tan|", sp.simplify(Bm*Bl - (sp.eye(3) - Ka*nPhi.T/ntan)))
check("proj det M = -2 c0 sqrt(1+s^2)", Mm.det() + 2*c0*sp.sqrt(1 + ss**2))

# threshold arithmetic (AS28) and (AS36): random positive constants
import random
random.seed(1)
bad = 0
for _ in range(2000):
    gm, cT, CB, Lg, Cbox, hh = [random.uniform(0.01, 5) for _ in range(5)] + [random.uniform(1e-4, 1e-2)]
    import math
    ell = math.ceil(max(1, (4*Lg*Cbox/(gm*cT))**(1/6), math.log(max(1, 4*CB/(gm*cT)))/(2*hh*math.log(2))))
    lower = gm*cT - CB*2**(-2*hh*ell) - Lg*Cbox*ell**-6
    if lower < gm*cT/2 - 1e-12:
        bad += 1
    gp = gm*random.uniform(1, 3); cm = random.uniform(0.01, 2); CT = random.uniform(0.01, 5)
    smax = random.uniform(0, 3); Gmax = random.uniform(0.01, 3); Wc = smax + Gmax + CT
    ell2 = math.ceil(max(1, (4*gp*CT/(gm*cm))**0.5, (8*Wc*Lg*Cbox/(gm*cm))**(1/6),
                         math.log(max(1, 8*Wc*CB/(gm*cm)))/(2*hh*math.log(2))))
    Eell = gp*CT*ell2**-2 + (CB*2**(-2*hh*ell2) + Lg*Cbox*ell2**-6)*(smax + Gmax + CT*ell2**-2)
    if Eell > gm*cm/2 + 1e-12:
        bad += 1
ok = bad == 0
res.append(("AS28/AS36 thresholds give the stated margins (2000 random constant sets)", ok))
print(("PASS" if ok else "FAIL") + "  AS28/AS36 thresholds give margins g_-c_T/2 and E_l <= g_-c_-/2 (2000 random sets; numerical)")

print("\nsummary: %d checks, %d PASS, %d FAIL" % (len(res), sum(o for _, o in res), sum(not o for _, o in res)))
