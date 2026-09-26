# Referee 21 (wbreader): Section 5.2.2 -- J=[[3,1],[1,5]], eigen-directions, the sharp constant, the group identity;
# Section 5.2.6 -- the curvature identity for a reducible connection.
import mpmath as mp, itertools, sympy as sp
mp.mp.dps = 50
J = sp.Matrix([[3,1],[1,5]]); print("det J =", J.det(), " eigenvalues:", J.eigenvals())
s2 = mp.sqrt(2); vr = (1, 1-s2); vt = (s2-1, 1); c = 1/mp.sqrt(4+2*s2)
print("J v_r = (4-sqrt2) v_r:", sp.simplify(J*sp.Matrix([1,1-sp.sqrt(2)]) - (4-sp.sqrt(2))*sp.Matrix([1,1-sp.sqrt(2)])).T, 
      " J v_t = (4+sqrt2) v_t:", sp.simplify(J*sp.Matrix([sp.sqrt(2)-1,1]) - (4+sp.sqrt(2))*sp.Matrix([sp.sqrt(2)-1,1])).T)
for v, name in ((vr, "v_r"), (vt, "v_t")):
    best = None
    for k1 in range(-300, 301):
        for k2 in range(-300, 301):
            if k1 == 0 and k2 == 0: continue
            val = abs(v[0]*k1 + v[1]*k2)*mp.sqrt(k1*k1+k2*k2)
            if best is None or val < best[0]: best = (val, (k1, k2))
    print(name, " min over |k|<=300:", mp.nstr(best[0], 20), " at", best[1], " 1/sqrt(4+2sqrt2) =", mp.nstr(c, 20), " strictly above:", best[0] > c)
# group identity in (Z/R)^* for R <= 200 (cyclic and non-cyclic): {(u,v): u^3 v = 1 = u v^5} = {(u,u^-3): u^14 = 1}
from math import gcd
ok = True
for R in range(2, 201):
    U = [x for x in range(1, R) if gcd(x, R) == 1]
    lhs = {(u, v) for u in U for v in U if (u**3*v) % R == 1 and (u*v**5) % R == 1}
    rhs = {(u, pow(u, -3, R)) for u in U if pow(u, 14, R) == 1}
    ok &= (lhs == rhs)
print("group identity for all U(R), R<=200:", ok)
# curvature identity: A_i = lam u_i T, T = -i sigma_3/2 (tr T^2 = -1/2): -2 sum_{i<j} tr F_ij^2 = lam^2 |curl u|^2
x, y, z, lam = sp.symbols('x y z lam')
u = [sp.Function('u%d' % i)(x, y, z) for i in range(3)]
Tm = -sp.I*sp.Matrix([[1,0],[0,-1]])/2
X = [x, y, z]
tot = 0
for i, j in ((0,1),(0,2),(1,2)):
    Fij = (sp.diff(lam*u[j], X[i]) - sp.diff(lam*u[i], X[j]))*Tm + (lam*u[i]*Tm)*(lam*u[j]*Tm) - (lam*u[j]*Tm)*(lam*u[i]*Tm)
    tot += (Fij*Fij).trace()
curl = [sp.diff(u[2], y)-sp.diff(u[1], z), sp.diff(u[0], z)-sp.diff(u[2], x), sp.diff(u[1], x)-sp.diff(u[0], y)]
print("curvature identity:", sp.simplify(-2*tot - lam**2*sum(cc**2 for cc in curl)) == 0)
