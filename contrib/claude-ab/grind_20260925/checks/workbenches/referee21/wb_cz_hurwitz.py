# Referee 21 (wbreader): Theorem 2.9 numerically: recover M_1, M_2 (hence lambda) from the zero motion of
# Z(s,t) = sum_w lambda_w zeta(s, 1 + t r_w) near rho_1, (m,A) = (2,4), words (1,3),(2,2),(3,1).
import mpmath as mp
mp.mp.dps = 40
# residues of the words mod 2^(A+1) = 32 (odd n with the given first two exponents), computed from T
def T(n):
    x = 3*n+1; a = (x & -x).bit_length()-1; return x >> a, a
res = {}
for n in range(1, 64, 2):
    y, a1 = T(n); _, a2 = T(y)
    if a1 + a2 == 4: res.setdefault((a1, a2), set()).add(n % 32)
print("residues mod 32:", res)
r = {w: min(v) for w, v in res.items()}
lam = {(1,3): mp.mpf('0.5'), (2,2): mp.mpf('0.2'), (3,1): mp.mpf('0.3')}
M1 = sum(lam[w]*r[w] for w in lam); M2 = sum(lam[w]*r[w]**2 for w in lam)
print("true M1, M2:", M1, M2)
rho = mp.zetazero(1)
Z = lambda s, t: sum(lam[w]*mp.zeta(s, 1+t*r[w]) for w in lam)
h = mp.mpf('1e-6')
roots = {}
for k in (-2, -1, 1, 2):
    roots[k] = mp.findroot(lambda s: Z(s, k*h), rho)
c1 = (8*(roots[1]-roots[-1]) - (roots[2]-roots[-2]))/(12*h)
c2 = (-(roots[2]+roots[-2]) + 16*(roots[1]+roots[-1]) - 30*rho)/(24*h*h)
z1 = mp.zeta(rho, derivative=1); z2 = mp.zeta(rho, derivative=2)
b1 = -rho*mp.zeta(rho+1); b1p = -mp.zeta(rho+1) - rho*mp.zeta(rho+1, derivative=1); b2 = rho*(rho+1)*mp.zeta(rho+2)/2
M1rec = -z1*c1/b1
M2rec = -(z1*c2 + z2*c1**2/2 + M1rec*b1p*c1)/b2
print("recovered M1 =", mp.nstr(M1rec, 12), " M2 =", mp.nstr(M2rec, 12))
# lambda from moments (Vandermonde) 
nodes = [r[w] for w in [(1,3),(2,2),(3,1)]]
V = mp.matrix([[x**i for x in nodes] for i in range(3)])
sol = mp.lu_solve(V, mp.matrix([1, M1rec, M2rec]))
print("recovered weights (1,3),(2,2),(3,1):", [mp.nstr(mp.re(x), 8) for x in sol])
# K-2 non-identifiability: h_w = 1/prod(r_w - r_v)
hw = [1/mp.fprod([nodes[i]-nodes[j] for j in range(3) if j != i]) for i in range(3)]
print("sum h_w r_w^i, i=0,1,2:", [mp.nstr(sum(hw[i]*nodes[i]**p for i in range(3)), 5) for p in range(3)])
