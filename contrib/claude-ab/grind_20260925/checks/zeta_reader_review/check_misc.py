#!/usr/bin/env python3
import os
"""Smaller checks for the understatement report (each item names the reader statement)."""
import mpmath as mp, numpy as np, sympy as sp, csv, itertools
mp.mp.dps = 30
ok = True
def report(name, cond, extra=""):
    global ok
    ok &= bool(cond)
    print(f"[{'ok' if cond else 'FAIL'}] {name} {extra}")

# ---- 1. Section 3.5, global residue duality: sharper constant zeta(2)(1/pi + 8 pi/5) ~ 8.79 (note 26_) vs 21.19
z2 = mp.zeta(2)
worst = max(abs(1/mp.zeta(mp.mpc(-1, t)))*(1 + abs(t))**1.5 for t in np.linspace(0, 400, 1601))
report("1a |1/zeta(-1+it)| (1+|t|)^{3/2} <= 4 pi^2 zeta(2) on [0,400]", worst <= 4*mp.pi**2*z2, f"(max ratio {mp.nstr(worst/(4*mp.pi**2*z2),4)})")
c_crude = z2*(1 + 4*mp.pi**2)/mp.pi; c_sharp = z2*(1/mp.pi + 8*mp.pi/5)
# direct evaluation of the two integrals with the bound kept: int (1+|t|)^{-2} dt = 2, int (1+|t|)^{-7/2} dt = 4/5
c_direct = (z2*2 + 4*mp.pi**2*z2*mp.mpf(4)/5)/(2*mp.pi)
report("1b constant", abs(c_direct - c_sharp) < 1e-25, f"crude {mp.nstr(c_crude,6)}, sharp {mp.nstr(c_sharp,6)}")
# pairing test with F = G = e^{s^2}
F = lambda s: mp.exp(s*s)
def B(F, G):
    I2 = mp.quad(lambda t: F(mp.mpc(2, t))*G(1 - mp.mpc(2, t))/mp.zeta(mp.mpc(2, t)), [-8, 0, 8])
    Im1 = mp.quad(lambda t: F(mp.mpc(-1, t))*G(1 - mp.mpc(-1, t))/mp.zeta(mp.mpc(-1, t)), [-8, 0, 8])
    return (I2 - Im1)/(2*mp.pi)          # ds = i dt, 1/(2 pi i) * i = 1/(2 pi)
bF = max((1 + abs(t))*abs(F(mp.mpc(sig, t))) for sig in (-2, 2) for t in np.linspace(0, 3, 3001))
val = B(F, F)
report("1c |B_zeta(e^{s^2}, e^{s^2})| <= 8.79 b_{2,1}^2", abs(val) <= c_sharp*bF**2, f"(|B| = {mp.nstr(abs(val),6)}, 8.79 b^2 = {mp.nstr(c_sharp*bF**2,6)})")

# ---- 2. Section 2.1, Theorem D: hypothesis verified (Platt-Trudgian, height 3e12) for n <= N(3e12)
T = mp.mpf('3e12')
NT = T/(2*mp.pi)*mp.log(T/(2*mp.pi*mp.e)) + mp.mpf(7)/8
report("2  N(3e12) ~ 1.24e13 >= 1e13", NT > 1e13, f"(Riemann-von Mangoldt main term {mp.nstr(NT,4)})")

# ---- 3. Section 2.1, Corollary B at a = 1: error O(T2 d(Delta) + K(Delta)) -> 0 once Delta >= (1+delta) sqrt(2 log T2)/log 2
def b(n):
    r = mp.mpf(1)/n; m = n; p = 2
    while p*p <= m:
        if m % p == 0:
            r *= (1 - p)
            while m % p == 0: m //= p
        p += 1
    if m > 1: r *= (1 - m)
    return r
def d(D, nmax=2000):
    return mp.fsum(abs(b(n))*mp.mpf(n)**-0.5*mp.exp(-D*D*mp.log(n)**2/2)/mp.log(n) for n in range(2, nmax))
print("3  T*d(Delta(T)) with Delta(T) = 1.1 sqrt(2 log T)/log 2  (d from the copy's 02_ section 4.2):")
prev = None
for Tn in [1e4, 1e6, 1e8, 1e12]:
    D = 1.1*mp.sqrt(2*mp.log(Tn))/mp.log(2)
    v = Tn*d(D)
    n2 = Tn*abs(b(2))*2**-0.5*mp.exp(-D*D*mp.log(2)**2/2)/mp.log(2)
    print(f"     T={Tn:.0e}: Delta={mp.nstr(D,4)}, T d(Delta) = {mp.nstr(v,4)}  (n=2 term alone {mp.nstr(n2,4)})")
    if prev is not None: ok &= v < prev
    prev = v
report("3  T d(Delta(T)) decreasing to 0", prev < 1e-2)

# ---- 4. Section 2.3, Z_{1/5}: Hurwitz functional equation Z_a(1-s) = 2 Gamma(s)(2 pi)^{-s} cos(pi s/2) Phi_a(s),
#         Phi_a(s) = 2 sum cos(2 pi k a) k^{-s}; zeros of Z_{1/5} left of the line <-> zeros of Phi_{1/5} right of it.
a = mp.mpf(1)/5
Z = lambda s: mp.zeta(s, a) + mp.zeta(s, 1 - a)
chi5 = lambda n: {0: 0, 1: 1, 4: 1, 2: -1, 3: -1}[n % 5]
L5 = lambda s: mp.nsum(lambda k: chi5(int(k))*k**(-s), [1, mp.inf]) if mp.re(s) > 1 else None
Phi = lambda s: 2*(mp.polylog(s, mp.expjpi(2*a)).real if False else None)
def Phi(s):   # 2 sum_k cos(2 pi k/5) k^{-s} = 2 * 5^{-s} sum_{r=1}^{5} cos(2 pi r/5) zeta(s, r/5), valid for all s != 1
    return 2*mp.mpf(5)**(-s)*mp.fsum(mp.cos(2*mp.pi*r/5)*mp.zeta(s, mp.mpf(r)/5) for r in range(1, 6))
for s in [mp.mpc('0.3', '7.1'), mp.mpc('1.6', '-3.3')]:
    lhs = Z(1 - s); rhs = 2*mp.gamma(s)*(2*mp.pi)**(-s)*mp.cos(mp.pi*s/2)*Phi(s)
    report(f"4a functional equation at s={mp.nstr(s,3)}", abs(lhs - rhs) < 1e-20*max(1, abs(lhs)))
# Phi_{1/5} = 1/2[(5^{1-s}-1) zeta(s) + sqrt5 L(s,(./5))]  (08_ section 2): check at s = 2.5
s = mp.mpf('2.5')
Lchi5 = mp.mpf(5)**(-s)*mp.fsum(chi5(r)*mp.zeta(s, mp.mpf(r)/5) for r in range(1, 5))
alt = ((5**(1 - s) - 1)*mp.zeta(s) + mp.sqrt(5)*Lchi5)/2
report("4b Phi_{1/5} = [(5^{1-s}-1)zeta + sqrt5 L(s,chi_5)]/2 (two primitive characters)", abs(Phi(s) - alt) < 1e-20)
rows = list(csv.DictReader(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..' + ('/..' if 'verify_minors' in __file__ else ''), '..', 'figures', 'data', 'z15_zeros_150.csv'))))
zs = [mp.mpc(r['beta'], r['gamma']) for r in rows]
left_strip = [z for z in zs if 0 < z.real < 0.5]; left_neg = [z for z in zs if z.real <= 0]; right = [z for z in zs if z.real > 0.5]
print(f"4c zeros of Z_(1/5) below 150: {len(zs)}; right of line {len(right)}, in 0<Re<1/2: {len(left_strip)}, Re<=0: {len(left_neg)}")
report("4d each tested left zero z has Phi_{1/5}(1-z) = 0 (1/2 < Re(1-z) < 1)", max(abs(Phi(1 - z))/abs(Phi(1 - z + 0.1)) for z in left_strip[:6]) < 1e-12,
       f"(max |Phi(1-z)|/|Phi(1-z+0.1)| = {mp.nstr(max(abs(Phi(1 - z))/abs(Phi(1 - z + 0.1)) for z in left_strip[:6]),3)})")

# ---- 5. Lemma 2.8 with complex exponents and for L(s,chi): coefficient matrix has full column rank
rng = np.random.default_rng(3)
sig = rng.normal(size=5) + 1j*rng.normal(size=5)*3
primes = [p for p in range(2, 60) if sp.isprime(p)]
rows_ = [[complex(p)**(r*sj) for sj in sig] for p in primes for r in range(1, 6)]
rk = np.linalg.matrix_rank(np.array(rows_), tol=1e-8)
report("5a complex exponents: sum_j C_j p^{r sigma_j} = 0 for all p, r forces C = 0", rk == len(sig), f"(rank {rk} of {len(sig)})")
chi = {1: 1, 2: 1j, 4: -1, 3: -1j}
rows_ = [[(chi[p % 5]**r)*complex(p)**(r*sj) for sj in sig] for p in primes if p != 5 for r in range(1, 6)]
report("5b same for L(s - sigma_j, chi), chi mod 5 with chi(2) = i", np.linalg.matrix_rank(np.array(rows_), tol=1e-8) == len(sig))

# ---- 6. Lemma 2.9 without the positivity normalisation: nu^{*d} = mu^{*d}  <=>  nu = omega mu, omega^d = 1
x = sp.symbols('x'); c = sp.symbols('c0:3')
mu = 1 + 2*x + x**2                                 # generating polynomial in e^{z}: mu = d0 + 2 d1 + d2
eqs = sp.Poly(sp.expand((c[0] + c[1]*x + c[2]*x**2)**3 - mu**3), x).all_coeffs()
sol = sp.solve(eqs, c, dict=True)
omegas = sorted({sp.nsimplify(sp.simplify(s_[c[0]])) for s_ in sol}, key=str)
report("6  solutions nu = omega*mu with omega^3 = 1 only", len(sol) == 3 and all(sp.simplify(s_[c[1]] - 2*s_[c[0]]) == 0 and sp.simplify(s_[c[2]] - s_[c[0]]) == 0 for s_ in sol),
       f"(omega in {omegas})")

# ---- 7. Prop 3.12: closure of N_S has infinite codimension (S = {2^k} U F): J independent annihilators for every J
t_ = mp.mpf('0.5'); a_ = 2; Fset = [3, 5, 7]
gen = lambda n, s: mp.exp(t_*s*s)*(n - n**(1 - s))/s
for J in [3, 6]:
    pts = [2j*mp.pi*j/mp.log(a_) for j in range(1, J + len(Fset) + 1)]
    A = mp.matrix([[gen(n, s) for s in pts] for n in Fset])            # |F| x (J+|F|)
    Anp = np.array(A.tolist(), dtype=complex)
    ns = np.linalg.svd(Anp)[2][len(Fset):].conj()                        # null space basis, dim J
    worst = max(abs(sum(ns[k, j]*complex(gen(a_**e, pts[j])) for j in range(len(pts)))) for k in range(ns.shape[0]) for e in range(1, 25))
    report(f"7  J={J}: {ns.shape[0]} independent evaluation combinations kill all generators (n in F and n = 2^k, k<25)", ns.shape[0] == J and worst < 1e-10)

# ---- 8. Lemma 6.6 for a NON-affine field V: div U = (div V) o F and F maps U-curves to V-curves
mp.mp.dps = 40
def Fv(p):
    x_, y_, w_ = p
    return [(1 + x_*y_)**3*w_ + y_**2*(1 + x_*y_)*(4 + 3*x_*y_), y_ + 3*x_*(1 + x_*y_)**2*w_ + 3*x_*y_**2*(4 + 3*x_*y_), 2*x_ - 3*x_**2*y_ - x_**3*w_]
def Vv(q):   # polynomial, NOT affine; div V = 2x + z - 1
    return [q[0]**2 + q[1], q[1]*q[2], q[0]**3 - q[2]]
def DFm(p):
    return mp.matrix([[mp.diff(lambda *v: Fv(list(v))[i], p, tuple(1 if k == j else 0 for k in range(3))) for j in range(3)] for i in range(3)])
def Uv(p):
    return mp.lu_solve(DFm(p), mp.matrix(Vv(Fv(p))))
rng2 = np.random.default_rng(7)
worst8 = 0; dets = []
for trial in range(4):
    p = [mp.mpf(float(v)) for v in rng2.uniform(-0.6, 0.6, 3)]
    dets.append(mp.det(DFm(p)))
    div = mp.fsum(mp.diff(lambda *v: Uv(list(v))[i], p, tuple(1 if k == i else 0 for k in range(3))) for i in range(3))
    q = Fv(p)
    worst8 = max(worst8, abs(div - (2*q[0] + q[2] - 1)))
report("8  det DF = -2 and div U = (div V) o F at random points, V = (x^2+y, yz, x^3-z) non-affine",
       all(abs(dd + 2) < 1e-25 for dd in dets) and worst8 < 1e-15, f"(max |div U - (div V)oF| = {mp.nstr(worst8,3)})")
mp.mp.dps = 30
# ---- 9. Prop 6.2 for composite bases: a has exact order d modulo a^d - 1
okk = all(pow(aa, k, aa**dd - 1) != 1 for aa in (6, 10, 12) for dd in range(2, 25) for k in range(1, dd))
report("9  exact order d of a mod a^d-1 for a = 6, 10, 12, d < 25 (so closure of a^Z is Z-hat for every integer a >= 2)", okk)

# ---- 10. reader numbers used in the report
r1 = mp.zetazero(1)
vel = r1*mp.zeta(r1 + 1)/mp.zeta(r1, derivative=1)
report("10 velocity rho1 zeta(rho1+1)/zeta'(rho1) = 0.98358 + 9.65780i", abs(vel - mp.mpc('0.98358', '9.65780')) < 1e-5, mp.nstr(vel, 8))
print("\nALL CHECKS PASS" if ok else "\nSOME CHECK FAILED")
