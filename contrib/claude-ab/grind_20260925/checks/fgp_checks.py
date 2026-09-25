# Checks of selected claims in the fixed-generic-point folder (P, W, TP, clock-history).
from fractions import Fraction
from math import gcd, log
import itertools
ok = True
# G = Z x Z/4 with T=(1,0), J=(0,1), eps=(0,2); A(m,k) = (-m, 2m-k mod 4)
def add(x, y): return (x[0]+y[0], (x[1]+y[1]) % 4)
def A(x): return (-x[0], (2*x[0]-x[1]) % 4)
def inv(x): return (-x[0], (-x[1]) % 4)
EPS = (0, 2)
# W2: N_A(g) = A(g) g = eps^m
for m, k in itertools.product(range(-7, 8), range(4)):
    g = (m, k); N = add(A(g), g)
    ok &= (N == ((0, 0) if m % 2 == 0 else EPS))
print("W2 parity norm A(g)g = eps^m:", ok)
# W2 defect: no section s(t)=T J^c intertwines A with inversion on L
defect_free = [c for c in range(4) if A((1, c)) == inv((1, c))]
print("W2 sections t->T J^c commuting with A (expect none):", defect_free)
# W5: endomorphisms f with f(T)=(n,c), f(J)=(0,b) [J torsion must map to torsion]; need f(eps)=eps and fA=Af
def f_apply(n, c, b, x):  # x = (m,k) -> m*(n,c) + k*(0,b)
    return ((m := x[0]) * n, (x[0]*c + x[1]*b) % 4)
sols = []
for n in range(-9, 10):
    for c in range(4):
        for b in range(4):
            if f_apply(n, c, b, EPS) != EPS: continue
            if all(f_apply(n, c, b, A(x)) == A(f_apply(n, c, b, x)) for x in [(1, 0), (0, 1), (3, 2), (-2, 3)]):
                sols.append((n, c, b))
ns = sorted({s[0] for s in sols}); bs = sorted({s[2] for s in sols}); cs = sorted({s[1] for s in sols})
ok &= all(n % 2 == 1 for n in ns) and bs == [1, 3] and cs == [0, 1, 2, 3] and len(sols) == len([n for n in range(-9, 10) if n % 2]) * 4 * 2
print("W5 degrees n allowed:", ns, "; c:", cs, "; b:", bs, "; count", len(sols))
# W10: B = mu_1 A, B(g) = T*A(g); B^2 = multiplication by eps, B^4 = id
def B(x): return add((1, 0), A(x))
for x in [(m, k) for m in range(-5, 6) for k in range(4)]:
    ok &= (B(B(x)) == add(EPS, x)) and (B(B(B(B(x)))) == x)
print("W10 B^2 = eps*, B^4 = id:", ok)
# P8/P11: lcm of 4p over P equals 4*prod(P)
def lcm(a, b): return a*b//gcd(a, b)
for P in [(2,), (3,), (2, 3), (3, 5, 7), (2, 5, 11)]:
    L = 1
    for p in P: L = lcm(L, 4*p)
    M = 1
    for p in P: M *= p
    ok &= (L == 4*M)
print("P11 lcm(4p) = 4 M_P:", ok)
# TP10: Dirichlet-convolution exponential of Lambda(n)/log n equals the all-ones function (coefficients of zeta)
X = 400
def is_prime(n): return n > 1 and all(n % q for q in range(2, int(n**0.5)+1))
Lam_over_log = [Fraction(0)]*(X+1)
for p in range(2, X+1):
    if is_prime(p):
        k, q = 1, p
        while q <= X:
            Lam_over_log[q] += Fraction(1, k); k += 1; q *= p
def dconv(a, b):
    c = [Fraction(0)]*(X+1)
    for i in range(1, X+1):
        if a[i] == 0: continue
        for j in range(1, X//i+1):
            if b[j] != 0: c[i*j] += a[i]*b[j]
    return c
expf = [Fraction(0)]*(X+1); expf[1] = Fraction(1)
term = expf[:]
r = 1
while True:
    term = dconv(term, Lam_over_log); term = [t/ r for t in term]
    if all(t == 0 for t in term): break
    expf = [e+t for e, t in zip(expf, term)]; r += 1
ok &= all(expf[n] == 1 for n in range(1, X+1))
print("TP10 exp_*(R) = D on n <=", X, ":", all(expf[n] == 1 for n in range(1, X+1)), "(terms used r <", r, ")")
# TP13: sum_{p^k} log p p^{-ks} = -zeta'/zeta check at s=2 via mpmath
import mpmath as mp
mp.mp.dps = 30
s = mp.mpf(2)
lhs = mp.nsum(lambda n: 0, [1, 1])
primes = [p for p in range(2, 20000) if is_prime(p)]
val = mp.fsum(mp.log(p) * p**(-s) / (1 - p**(-s)) for p in primes)
tail_bound = mp.fsum(mp.log(n)*n**(-s) for n in range(20000, 20001))  # indicative only
ref = -mp.diff(mp.zeta, s)/mp.zeta(s)
print("TP13 -zeta'/zeta(2) =", mp.nstr(ref, 12), "; prime sum (p<20000) =", mp.nstr(val, 12))
ok &= abs(ref - val) < 1e-3
# Clock-history section 5: bilateral-shift spectrum check on a truncated model: D_n/sqrt(n) acts as shift on shells;
# verify ||f_L||^2 = L s and ||(D-lam)f_L||^2 = 2 n s for the shell sum (model shells as orthonormal-with-mass vectors)
n = 3; s_mass = 1.0
import cmath
lam = cmath.sqrt(n) * cmath.exp(0.7j)
Lsh = 50
# shells S_j mass n^{-j} s; D 1_{S_j} = 1_{S_{j-1}}; represent functions by coefficient per shell, norm^2 = sum |c_j|^2 n^{-j} s
coef = {j: lam**j for j in range(Lsh)}
def norm2(cf): return sum(abs(v)**2 * n**(-j) * s_mass for j, v in cf.items())
Df = {}
for j, v in coef.items(): Df[j-1] = Df.get(j-1, 0) + v
res = {j: Df.get(j, 0) - lam*coef.get(j, 0) for j in set(Df) | set(coef)}
print("clock-history shells: ||f_L||^2 =", round(norm2(coef), 6), "(L s =", Lsh*s_mass, "); ||(D-lam)f_L||^2 =", round(norm2(res), 6), "(2 n s =", 2*n*s_mass, ")")
ok &= abs(norm2(coef) - Lsh*s_mass) < 1e-9 and abs(norm2(res) - 2*n*s_mass) < 1e-9
print("ALL PASS" if ok else "FAILURE")
