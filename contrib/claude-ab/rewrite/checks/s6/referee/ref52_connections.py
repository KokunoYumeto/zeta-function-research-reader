#!/usr/bin/env python3
"""ref52_connections.py -- referee's checks of the connections proposed in REFEREE_REPORT_52.md (Part B).

 (C1) the Levi half of the index-12 character equals the S6 programme's own 'marked peripheral character'
      chi: SL2(Z) ->> Z/12 of the higher-torus update (15_ Theorem 6.1, eq. (88); 14_ p.1):
      (chi(C0), chi(C1), chi(C2')) = (-1, 4, -3) with C1 = [[-1,-1],[1,0]], C2' = [[0,1],[-1,0]], C0 = [[1,1],[0,1]] (15_ eq. (27));
      and on the monodromy, ab(pi(T_j)) = -phi(Heisenberg part of T_j) gives the same triple (-1, 4, -3);
 (C2) Gritsenko-Hulek (alg-geom/9702007, Lemma 1.1 and (1.10a,b)): the order-12 character chi_12 = chi_3 chi_4^{-1} of
      the paramodular group of level t = 6 restricts on the parabolic of a divisor-6 isotropic vector (our u) to
      v_eta^2 (Levi), v_H (integral Heisenberg H(Z)) and [0,0;kappa/6] -> e(kappa/12) (centre).  We check that on the
      overlap Stab(u) n Stab(gamma), e(Phi/12) takes exactly these values, and that L_T and t_gamma (which generate
      G_Z^ab = Z/12 x Z/12) lie in the overlap; hence e(+-Phi/12) = chi_12|G_Z and G = Stab(gamma) n ker(chi_12);
 (C3) H' = G n Heis is the kernel of v_H([p, r; kappa]) = (-1)^{p+r+pr+kappa} on the standard Heisenberg group
      H(Z) = {h(p,r,6 kappa)} (index 6 in Heis(Z)); [G_Z : Gamma^J] = 6, [Gamma^J : G n Gamma^J] = 12, [G : G n Gamma^J] = 6;
 (C4) fusion evidence: Phi(t_f) for every primitive f in gamma-perp (box), grouped by the divisor d of f, is constant
      on each class (t_f the primitive transvection x -> x + Q0(f,x)/d f);
 (C5) both one-dimensional cusp types (divisor 1: gamma; divisor 6: u) have unipotent radicals with centre Z and
      commutator subgroup 12Z (so the 'opposite cusp type' remark changes nothing about the group).
"""
import math, itertools, random, sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
random.seed(11)
res = []
def check(name, cond):
    ok = bool(cond); res.append((name, ok)); print(("PASS" if ok else "FAIL") + "  " + name, flush=True)
# reuse the pure-integer helpers of ref52_partB_group.py without re-running its checks
src = open(os.path.join(HERE, 'ref52_partB_group.py')).read()
helpers = src[src.index('# ---------- integer 4x4'):src.index('# ---------- (1) the data')]
exec(helpers)
g_, u_, w_, d_ = [1,0,0,0], [0,1,0,0], [0,0,1,0], [0,0,0,1]
def lin(*terms):
    v = [0,0,0,0]
    for coef, vec in terms: v = [a + coef*b for a, b in zip(v, vec)]
    return v
T1 = from_images([g_, lin((-1,u_),(-1,w_)), lin((-6,g_),(1,u_)), lin((2,g_),(1,u_),(1,w_),(1,d_))])
T2 = from_images([g_, lin((6,g_),(1,w_)), lin((-1,u_)), lin((-3,g_),(1,u_),(1,d_))])
Q0 = [[0,0,0,1],[0,0,6,0],[0,-6,0,0],[-1,0,0,0]]
I4 = eye(4)
def preserves(g): return mul(mul(tr(g), Q0), g) == Q0
part2 = src[src.index('# ---------- (2) Levi / Heisenberg decomposition'):src.index('check(f"(2) ab is well defined')]
exec(part2)      # defines L, h, decompose, S2, T_, ab_euclid, ab12 table, gens2
def qf(p, r): return p*p + p*r + r*r
def phi(p, r, s): return (s - 6*qf(p, r)) % 12
def Phi(g):
    M, (p, r, s) = decompose(g)
    return (phi(p, r, s) + ab_euclid(M)) % 12
T0 = inv_unimodular4(mul(T1, T2))
# (C1) peripheral character
C1 = [[-1,-1],[1,0]]; C2p = [[0,1],[-1,0]]; C0 = [[1,1],[0,1]]
chi = lambda M: (-ab_euclid(M)) % 12           # 15_ normalization: chi(C0) = chi(T) = -1
trip_S6 = tuple(((chi(M) + 6) % 12) - 6 for M in (C0, C1, C2p))
levi = [decompose(g)[0] for g in (T0, T1, T2)]
heis = [decompose(g)[1] for g in (T0, T1, T2)]
trip_ab = tuple(((ab_euclid(M) + 6) % 12) - 6 for M in levi)
trip_phi = tuple(((-phi(*hh) + 6) % 12) - 6 for hh in heis)
check(f"(C1) S6 update's marked peripheral character: (chi(C0), chi(C1), chi(C2')) = {trip_S6} (15_ eq. (88): (-1, 4, -3)); "
      f"C1 C2' = C0^-1, C1^3 = C2'^4 = I", trip_S6 == (-1, 4, -3) and mul(C1, C2p) == inv2(C0) and mpow(C1, 3) == eye(2) and mpow(C2p, 4) == eye(2))
check(f"(C1) Levi parts of (T0, T1, T2): {levi}; C1 = R^T, C2' = S^T, C0 = T; (ab(pi T0), ab(pi T1), ab(pi T2)) = {trip_ab} = the S6 triple",
      tr(levi[1]) == C1 and tr(levi[2]) == C2p and trip_ab == (-1, 4, -3))
check(f"(C1) Heisenberg parts of (T0, T1, T2): {heis}; -phi = -(s - 6(p^2+pr+r^2)) gives {trip_phi} = the same triple: on G the peripheral character is read off the Heisenberg data",
      trip_phi == (-1, 4, -3))
# (C2) GH chi_12 on the overlap Stab(u) n Stab(gamma)
def fixes(g, v): return [sum(g[i][j]*v[j] for j in range(4)) for i in range(4)] == v
LT = L(T_); tg = h(0, 0, 1)
check("(C2) L_T is the centre generator of Stab(u) (w -> w + u = transvection x -> x + Q0(u,x)/6 u); t_gamma = h(0,0,1) (delta -> delta + gamma) "
      "fixes u and w and acts on <gamma, delta> by [[1,1],[0,1]]: it is 'T' of the Levi SL2 of Stab(u); both lie in G_Z",
      fixes(LT, u_) and fixes(LT, g_) and LT == from_images([g_, u_, lin((1,w_),(1,u_)), d_])
      and fixes(tg, u_) and fixes(tg, w_) and fixes(tg, g_) and tg == from_images([g_, u_, w_, lin((1,d_),(1,g_))]))
# unipotent radical of Stab(u): gamma -> gamma + a u, delta -> delta + b u, w -> w + 6b gamma - 6a delta + s u
def radu(a, b, s):
    return from_images([lin((1,g_),(a,u_)), u_, lin((1,w_),(6*b,g_),(-6*a,d_),(s,u_)), lin((1,d_),(b,u_))])
ok_rad = all(mul(mul(tr(radu(a,b,s)), Q0), radu(a,b,s)) == Q0 for a in range(-2,3) for b in range(-2,3) for s in range(-2,3))
# elements of Stab(u) n Stab(gamma) in the radical: a = 0.  GH: centre [0,0;kappa/6] -> e(kappa/12) with kappa = s,
# H(Z) element [0, b; 0] -> v_H = (-1)^b.  So predicted Phi = s + 6b (mod 12).
ok_ov = all(Phi(radu(0, b, s)) == (s + 6*b) % 12 for b in range(-5, 6) for s in range(-13, 14))
# Levi of Stab(u) (acting on <gamma, delta>, fixing u, w) meets G_Z in <t_gamma>: t_gamma^k, predicted v_eta^2(T^k) = e(k/12)
ok_lev = all(Phi(mpow(tg, k)) == k % 12 for k in range(-13, 14))
check("(C2) on the overlap Stab(u) n Stab(gamma): radical elements (a=0) have Phi = s + 6b = GH's chi_12 value (centre e(s/12), v_H = (-1)^b); "
      "t_gamma^k has Phi = k = GH's v_eta^2(T^k); the radical formula is Q0-symplectic", ok_rad and ok_ov and ok_lev)
# a character of G_Z is fixed by its values on L_T and t_gamma: (ab, phi) : G_Z ->> Z/12 x Z/12 has kernel [G_Z, G_Z]
check("(C2) G_Z^ab = Z/12 x Z/12 is generated by the classes of L_T (=(1,0)) and t_gamma (=(0,1)); Phi(L_T) = Phi(t_gamma) = 1 = GH's chi_12 values "
      "(v_eta^2(T) = e(1/12), centre [0,0;1/6] -> e(1/12)); so chi_12 restricted to G_Z is e(+-Phi/12), whose kernel is G",
      Phi(LT) == 1 and Phi(tg) == 1 and (ab_euclid(T_), phi(0,0,0)) == (1, 0) and (ab_euclid(eye(2)), phi(0,0,1)) == (0, 1))
# (C3) v_H and the standard Jacobi group
vH = lambda p, r, kap: (p + r + p*r + kap) % 2
check("(C3) H' = {h(p,r,6kappa) : v_H([p,r;kappa]) = +1}, v_H = (-1)^{p+r+pr+kappa} (GH (1.5)), and the law of {h(p,r,6kappa)} is the standard "
      "Heisenberg law kappa1+kappa2+(p1 r2 - p2 r1)",
      all(((6*kap - 6*qf(p, r)) % 12 == 0) == (vH(p, r, kap) == 0) for p in range(-5, 6) for r in range(-5, 6) for kap in range(-5, 6))
      and all(mul(h(p1,r1,6*k1), h(p2,r2,6*k2)) == h(p1+p2, r1+r2, 6*(k1+k2+p1*r2-p2*r1))
              for p1, r1, k1, p2, r2, k2 in itertools.product(range(-2, 3), repeat=6) if random.random() < 0.05))
vals_J = {(ab_euclid(M) + phi(p, r, 6*k)) % 12 for M in [mpow(T_, k) for k in range(12)] for p in range(2) for r in range(2) for k in range(2)}
check(f"(C3) Phi on the standard Jacobi group Gamma^J = SL2(Z) x| {{6|s}} takes all 12 values {sorted(vals_J)}: [Gamma^J : G n Gamma^J] = 12, "
      "[G_Z : Gamma^J] = 6, hence G Gamma^J = G_Z and [G : G n Gamma^J] = 6; on Gamma^J, e(Phi/12) = v_eta^2 x v_H (the multiplier of theta/eta)",
      vals_J == set(range(12)))
# (C4) fusion evidence on transvections t_f, f in gamma-perp primitive
def Q0f(a, b):
    return sum(a[i]*Q0[i][j]*b[j] for i in range(4) for j in range(4))
basis = [g_, u_, w_, d_]
byd = {}
for cg, au, bw in itertools.product(range(-6, 7), repeat=3):
    if math.gcd(math.gcd(cg, au), bw) != 1: continue
    f = [cg, au, bw, 0]
    d = math.gcd(math.gcd(Q0f(f, u_), Q0f(f, w_)), Q0f(f, d_))
    d = abs(d)
    imgs = []
    for e in basis:
        coef = Q0f(f, e)
        assert coef % d == 0
        imgs.append([e[i] + (coef // d)*f[i] for i in range(4)])
    tf = from_images(imgs)
    assert mul(mul(tr(tf), Q0), tf) == Q0 and fixes(tf, g_)
    byd.setdefault(d, set()).add(Phi(tf))
check(f"(C4) Phi(t_f) over all primitive f = c gamma + a u + b w (|a|,|b|,|c| <= 6), grouped by divisor d: {dict(sorted((k, sorted(v)) for k, v in byd.items()))} "
      "-- constant on each divisor class (necessary for Phi to extend to a class function on the paramodular group)",
      all(len(v) == 1 for v in byd.values()))
# (C5) both cusp types: commutator in the unipotent radical of Stab(u)
cA, cB = radu(1, 0, 0), radu(0, 1, 0)
comm = mul(mul(cA, cB), mul(inv_unimodular4(cA), inv_unimodular4(cB)))
check("(C5) unipotent radical of Stab(u) (divisor-6 cusp): centre {w -> w + s u : s in Z}, and [rad(1,0,0), rad(0,1,0)] = rad(0,0,+-12): "
      "same Heisenberg type (centre Z, commutator 12Z) as Heis(Z) at gamma",
      comm in (radu(0, 0, 12), radu(0, 0, -12)))
print(f"\nsummary: {len(res)} checks, {sum(o for _, o in res)} PASS, {len(res) - sum(o for _, o in res)} FAIL")
