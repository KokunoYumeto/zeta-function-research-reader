#!/usr/bin/env python3
"""ref50_misc.py -- referee checks of the remaining statements of note 50_ and reader Section 6.
Each item prints PASS/FAIL (or DATA) with details.  Written independently of es50_checks.py."""
import time, random, cmath
from math import gcd, isqrt, prod
from fractions import Fraction as Fr
from itertools import product, combinations
from sympy import isprime, factorint, divisors, jacobi_symbol, primerange, n_order, primitive_root
from sympy import legendre_symbol

T0 = time.time()
random.seed(3)
def rep(tag, ok, msg=""):
    print(("PASS " if ok else "FAIL ") + tag + (": " + msg if msg else ""), flush=True)
def is_sol(p, x, y, z): return x > 0 and y > 0 and z > 0 and 4 * x * y * z == p * (x * y + y * z + z * x)
def shell_sol(p, R, u, ch):
    a = (p + R) // 4; N = p * a; d = p * p * u if ch == 'E' else p * u
    assert (p + R) % 4 == 0 and (a * a) % u == 0 and gcd(R, p * a) == 1
    assert ((N + d) % R == 0) and ((N + N * N // d) % R == 0)
    return a, (N + d) // R, (N + N * N // d) // R

# 1. solutions quoted in §12 of 50_ and in the reader
for p, x, y, z in ((3361, 841, 110139970, 950330), (18481, 4625, 3330091390, 4504750),
                   (2840041, 710012, 261184725275808711129, 288066170388), (12601, 3151, 7264426096, 13259408),
                   (5, 2, 20, 4)):
    rep(f"1 quoted solution 4/{p}", is_sol(p, x, y, z), f"x={x}, least shell R = {4*x - p}")

# 2. the p* certificates: all (shift, q) with (p/q) = -1 for the eight shifts
ps = 8803369
cert = []
for name, S in (("p+1", ps+1), ("p+2", ps+2), ("p+3", ps+3), ("p+4", ps+4), ("p+7", ps+7), ("p+8", ps+8), ("2p+1", 2*ps+1), ("3p+1", 3*ps+1)):
    for q in factorint(S):
        if q > 2 and legendre_symbol(ps % q, q) == -1:
            cert.append((name, q))
rep("2 p* = 8803369 non-residue factors of the eight shifts", True, f"{cert}; p*+2 = {factorint(ps+2)}, 2p*+1 = {factorint(2*ps+1)}")
for name, q in cert:
    R = q if q % 8 == 7 else 3 * q
    a = (ps + R) // 4
    sol = shell_sol(ps, R, a // 2 if name == "p+2" else 2 * a, 'E')
    rep(f"2 p* certificate {name}, q = {q}, R = {R}", is_sol(ps, *sol), f"x = {sol[0]}")

# 3. the 43201 example of the missed p+24 condition (M-channel u = 6, R = 13*35)
p = 43201; R = 13 * 35
sol = shell_sol(p, R, 6, 'M')
rep("3 43201 = 361 (mod 840) solved by the p+24 condition, R = 455, u = 6", is_sol(p, *sol) and p % 840 == 361 and
    legendre_symbol(p % 13, 13) == -1, f"p+24 = {factorint(p+24)}; 4/43201 = 1/{sol[0]} + 1/{sol[1]} + 1/{sol[2]}")

# 4. Rosati family and the two 29-channels
def rosati_ok(n, k, c):
    m = 4 * k - 1
    return (n + c) % m == 0 and k % c == 0 and is_sol(n, k * n, k * (n + c) // m, k * n * (n + c) // (m * c))
ok = all(rosati_ok(n, 80, 40) for n in range(917, 917 + 1276 * 2000, 1276))
rep("4a the whole first 29-channel 917 (mod 1276) lies in Rosati's class n = -40 (mod 319), k = 80, c = 40",
    ok and 1276 % 319 == 0 and (917 + 40) % 319 == 0, "identity verified on 2000 members")
# every 14a class (n = -B/C mod 4BCD-1) with modulus dividing 2204 that contains 1605
hits = []
for m in divisors(2204):
    if m % 4 != 3: continue
    T = (m + 1) // 4
    for B in divisors(T):
        for C in divisors(T // B):
            D = T // B // C
            if (1605 * C + B) % m == 0: hits.append((m, B, C, D))
rep("4b 14a classes with modulus | 2204 containing 1605 (mod 2204)", True, f"{hits} (C = 1, i.e. Rosati's c | k family: {[h for h in hits if h[2] == 1]})")
def chart14a_ok(n, B, C, D):
    m = 4 * B * C * D - 1
    if (B + n * C) % m: return False
    A = (B + n * C) // m
    return is_sol(n, A * B * D, A * C * D * n, B * C * D * n)
rep("4c 1605 (mod 2204) lies in 14a (B,C,D) = (2,23,3), n = -2/23 (mod 551)",
    all(chart14a_ok(n, 2, 23, 3) for n in range(1605, 1605 + 2204 * 2000, 2204)))
# 4d the n = 1 (mod 3) part of the first channel is in 76 mod 87 (as stated); both statements are consistent
rep("4d 917 (mod 1276) and n = 1 (mod 3) implies n = 76 (mod 87)", all((n % 87 == 76) == (n % 3 == 1) for n in range(917, 917 + 1276 * 300, 1276)))
# 4e lock (b) = Rosati C = 1: class n = -mu (mod h), h = 4 mu t - 1
rep("4e lock (b) with (mu, t) is Rosati's family k = mu t, c = mu", all(rosati_ok(n, mu * t, mu)
    for mu in (5, 11, 17) for t in (1, 2, 5) for n in range((-mu) % (4 * mu * t - 1) or 4 * mu * t - 1, 3000, 4 * mu * t - 1) if n > 1))

# 5. locks: 1201 has no type-(a) certificate, 5569 no type-(b), for any odd mu (finite: mu < p for (a), 7 mu <= p+2 for (b))
def lock_a_exists(p):
    for mu in range(1, p, 2):
        N = (p + mu) // 2
        for d in divisors(N):
            if d % 2 and (d + p) % (4 * mu) == 0: return (mu, d)
    return None
def lock_b_exists(p):
    for mu in range(1, (p + 2) // 7 + 2, 2):
        N = (p + mu) // 2
        for h in divisors(N):
            if (h + 1) % (4 * mu) == 0: return (mu, h)
    return None
rep("5a 1201: no type-(a) lock for any odd mu < 1201; type (b) exists", lock_a_exists(1201) is None and lock_b_exists(1201) is not None, f"(b): {lock_b_exists(1201)}")
rep("5b 5569: no type-(b) lock for any odd mu; type (a) exists", lock_b_exists(5569) is None and lock_a_exists(5569) is not None, f"(a): {lock_a_exists(5569)}")

# 6. complement squares = Lopez Type C: 4UVW = pW + U + V; least p = 1 (24) without one, least hard one
def typeC(p):
    # R = 4UV - p > 0 and R | U + V, with U <= V; R <= U + V forces 4UV - U - V <= p
    for U in range(1, isqrt(p) + 2):
        Vmin = max(U, p // (4 * U) + 1)
        V = Vmin
        while 4 * U * V - U - V <= p:
            R = 4 * U * V - p
            if R > 0 and (U + V) % R == 0: return (U, V, (U + V) // R)
            V += 1
    return None
S840 = {1, 121, 169, 289, 361, 529}
none = [p for p in range(25, 12000, 24) if isprime(p) and typeC(p) is None]
rep("6 complement squares (Lopez Type C) fail first at 97; first hard failure 3361",
    none[:1] == [97] and [p for p in none if p % 840 in S840][:1] == [3361], f"failures below 12000: {none}")
U, V, W = typeC(8803369) or (0, 0, 0)
rep("6b p* is Type C", U * V > 0 and 4 * U * V * W == 8803369 * W + U + V, f"(U, V, W) = {(U, V, W)}")

# 7. norm forms, and the stronger forms p+1 (x^2+y^2) and p+7 (x^2+xy+2y^2)
def prim_rep(n, a, b, c):
    """is n = a x^2 + b x y + c y^2 with gcd(x, y) = 1 (positive definite form)?"""
    D = b * b - 4 * a * c
    ymax = isqrt(4 * a * n // (-D)) + 1
    for y in range(0, ymax + 1):
        # a x^2 + b y x + c y^2 - n = 0
        disc = b * b * y * y - 4 * a * (c * y * y - n)
        if disc < 0: continue
        s = isqrt(disc)
        if s * s != disc: continue
        for x in ((-b * y + s), (-b * y - s)):
            if x % (2 * a) == 0 and gcd(x // (2 * a), y) == 1: return True
    return False
def eight_survivor(p):
    for S in (p+1, p+2, p+3, p+4, p+7, p+8, 2*p+1, 3*p+1):
        for q in factorint(S):
            if q > 2 and legendre_symbol(p % q, q) == -1: return False
    return True
survs = [p for p in range(25, 700000, 24) if isprime(p) and p % 840 in S840 and eight_survivor(p)]
bad = []
for p in survs:
    tests = [((p+1)//2, (1,0,1)), (p+4, (1,0,1)), (p+2, (1,0,2)), (p+8, (1,0,2)), (2*p+1, (1,0,2)),
             ((p+3)//4, (1,1,1)), ((3*p+1)//4, (1,1,1)), ((p+7)//8, (1,1,2))]
    for n, f in tests:
        if not prim_rep(n, *f): bad.append((p, n, f))
strong = [p for p in survs if prim_rep(p + 1, 1, 0, 1) and prim_rep(p + 7, 1, 1, 2) and prim_rep((p + 7) // 4, 1, 1, 2)]
rep("7 norm-form corollary on the eight-shift survivors below 7*10^5", not bad, f"{len(survs)} survivors; failures {bad[:3]}")
rep("7b stronger forms: p+1 = x^2+y^2 and p+7, (p+7)/4 = x^2+xy+2y^2 primitively (2 splits in Q(sqrt -7))",
    len(strong) == len(survs), f"{len(strong)} of {len(survs)}")

# 8. Theorem 50.6: the disjunct (p/R) = -1 is implied by the other one
viol = 0; tested = 0
for p in [p for p in range(25, 300000, 24) if isprime(p) and p % 840 in S840]:
    for R in (11, 19, 23, 31, 43, 47, 59, 67, 71, 79, 83, 311):
        if p == R: continue
        if jacobi_symbol(p % R, R) == -1:
            tested += 1
            if not any(q > 2 and legendre_symbol(p % q, q) == -1 for q in factorint(p + R)): viol += 1
rep("8 (p/R) = -1 implies an odd prime q | p+R with (p/q) = -1 (so the first disjunct of Thm 50.6 is redundant)",
    viol == 0 and tested > 1000, f"{tested} cases, {viol} violations")

# 9. width-one versus group barrier: prime powers (exhaustive over subgroups), the example, and the count 124
def subgroup(gens, R):
    K = {1}; fr = [1]
    while fr:
        nx = []
        for k in fr:
            for g in gens:
                y = (k * g) % R
                if y not in K: K.add(y); nx.append(y)
        fr = nx
    return K
bad = 0; cnt = 0
for R in (3, 7, 11, 19, 23, 27, 31, 43, 47, 49, 59, 67, 71, 79, 83, 121, 243, 343, 361, 529, 1331, 2187):
    units = [x for x in range(1, R) if gcd(x, R) == 1]
    subs = {frozenset(subgroup([g], R)) for g in units}
    subs |= {frozenset(subgroup([g, h], R)) for g, h in combinations(units[:60], 2)}
    for K in subs:
        cnt += 1
        w1 = ((R - 1) in K) or ((-4) % R in K)
        gb = (R - 1) in subgroup(list(K) + [4], R)
        if w1 != gb: bad += 1
rep("9a prime powers R = q^k, q = 3 (mod 4): (-1 in K or -4 in K) <=> -1 in <4, K>, all (cyclic and 2-generated) subgroups", bad == 0, f"{cnt} subgroups")
# a composite R where they differ, smallest over all R < 200 and all subgroups generated by one element
ex = None
for R in range(3, 200, 4):
    for g in range(2, R):
        if gcd(g, R) != 1: continue
        K = subgroup([g], R)
        if not (((R - 1) in K) or ((-4) % R in K)) and (R - 1) in subgroup(list(K) + [4], R):
            ex = (R, g, sorted(K)); break
    if ex: break
rep("9b smallest R (with a cyclic K) where the width-one barrier is strictly sharper", ex is not None, str(ex))
a = (433 + 91) // 4
K = subgroup([q % 91 for q in factorint(a)], 91)
E = [u for u in divisors(a * a) if (4 * u + 1) % 91 == 0]; Mset = [u for u in divisors(a * a) if (u + a) % 91 == 0]
rep("9c (433, 91): a = 131, K = <40>, -1, -4 not in K, -1 in <4,K>, (131/91) = -1, shell empty",
    a == 131 and sorted(K) == [1, 27, 40, 53, 66, 79] and 90 not in K and 87 not in K and 90 in subgroup(list(K) + [4], 91)
    and jacobi_symbol(131, 91) == -1 and not E and not Mset)
def divs_sq(a):
    ds = [1]
    for q, e in factorint(a).items():
        ds = [d * q**k for d in ds for k in range(2 * e + 1)]
    return ds
def occupied(p, R):
    a = (p + R) // 4
    return any((4 * u + 1) % R == 0 or (u + a) % R == 0 for u in divs_sq(a))
def times4(K, R):
    out = set(K); cur = set(K)
    while True:
        cur = {(4 * k) % R for k in cur}
        if cur <= out: return out
        out |= cur
sep = 0; viol = 0
for p in [p for p in range(25, 3000, 24) if isprime(p)]:
    for R in range(3, 3 * p, 4):
        if R % p == 0: continue
        a = (p + R) // 4
        K = subgroup([q % R for q in factorint(a)], R)
        w1 = not (((R - 1) in K) or ((-4) % R in K))
        gb = not ((R - 1) in times4(K, R))
        if w1 or gb:
            if occupied(p, R): viol += 1
        if w1 and not gb: sep += 1
rep("9d shells R < 3p, p = 1 (24) < 3000: barriers never violated; shells killed by width-one only", viol == 0, f"{sep} (claim 124)")

# 10. Proposition 50.9: non-coprime shells need p | a (so a >= p) and p^2 | R needs R >= 3p^2 (p = 1 mod 4)
rep("10a p | R => p | a, and a > 3p/4 is never a least denominator", all(((p + k * p) // 4) % p == 0
    for p in primerange(5, 400) for k in range(3, 200, 4) if (p + k * p) % 4 == 0))
p, R = 73, 7 * 73**2
a = (p + R) // 4; N = p * a; d = 4 * 73**3
rep("10b the p = 73 example: d | N^2, d = -N mod R, y = 60, z not integral, no solution with this a",
    (N * N) % d == 0 and (d + N) % R == 0 and (N + d) // R == 60 and Fr(N + N * N // d, R) == Fr(1920, 73)
    and not any((N * y) % (R * y - N) == 0 for y in range(N // R + 1, 2 * N // R + 2) if R * y > N), f"z = {Fr(N + N*N//d, R)}")

# 11. Proposition 50.10 counts (coprime shells R | p^2 - 1, p = 1 (mod 4), p < 2000, R < 3p)
n1 = n2 = 0; ok1 = ok2 = True
for p in primerange(5, 2000):
    if p % 4 != 1: continue
    for R in divisors(p * p - 1):
        if R % 4 != 3 or R >= 3 * p: continue
        a = (p + R) // 4
        ds = divisors(a * a)
        E = {u for u in ds if (4 * u + 1) % R == 0}; Mm = {u for u in ds if (u + a) % R == 0}
        n2 += 1; ok2 &= ((len(E) % 2 == 1) == ((p + 1) % R == 0)) and all(a * a // u in E for u in E)
        if (p - 1) % R == 0: n1 += 1; ok1 &= (E == Mm)
rep("11 Prop 50.10 (1): R | p-1 => E = M", ok1, f"{n1} shells (claim 233)")
rep("11 Prop 50.10 (2): R | p^2-1 => E closed under complement, |E| odd iff R | p+1", ok2, f"{n2} shells (claim 947)")

# 12. pair-count Dirichlet series: coefficients by characters versus direct count, R = 7 and R = 15
def dirichlet_chars(R):
    units = [x for x in range(1, R) if gcd(x, R) == 1]
    # characters via a basis of the group: brute force over homomorphisms given by values on generators
    fac = factorint(R); chars = [dict((u, 1) for u in units)]
    for q, e in fac.items():
        qe = q**e
        g = primitive_root(qe); ph = qe - qe // q
        new = []
        for ch in chars:
            for k in range(ph):
                d = {}
                for u in units:
                    ind = next(i for i in range(ph) if pow(g, i, qe) == u % qe)
                    d[u] = ch[u] * cmath.exp(2j * cmath.pi * k * ind / ph)
                new.append(d)
        chars = new
    return chars, units
def A_direct(n, R):
    c = 0
    for X in divisors(n):
        for Y in divisors(n // X):
            if gcd(X, Y) == 1 and (X + Y) % R == 0: c += 1
    return c
bad = 0; checked = 0
for R in (7, 15, 11):
    chars, units = dirichlet_chars(R)
    phi = len(units)
    for n in range(1, 400):
        if gcd(n, R) != 1: continue
        # coefficient of n^-s in phi^-1 sum_chi chi(-1) zeta_R(s) L(s,chi) L(s,chibar) / zeta_R(2s)
        tot = 0
        for ch in chars:
            s = 0
            # sum over n = Z * d^2 * X * Y: mu(d) chi(X) chibar(Y)
            for dd in range(1, isqrt(n) + 1):
                if n % (dd * dd): continue
                mu = 0 if any(e > 1 for e in factorint(dd).values()) else (-1)**len(factorint(dd))
                if mu == 0: continue
                m2 = n // (dd * dd)
                for X in divisors(m2):
                    for Y in divisors(m2 // X):
                        s += mu * ch[X % R] * ch[Y % R].conjugate()
            tot += ch[R - 1] * s
        val = tot / phi
        checked += 1
        if abs(val - A_direct(n, R)) > 1e-6: bad += 1
rep("12 pair-count Dirichlet series coefficients (R = 7, 11, 15, n < 400)", bad == 0, f"{checked} coefficients")

# 13. Collatz predecessors: Pi_k = (2^(e+2k) n - 1)/3, Pi_{k+1} = 4 Pi_k + 1, Pi_k = 5 (mod 8) for k >= 1
ok = True
for n in range(1, 3000, 2):
    if n % 3 == 0: continue
    e = 1 if (2 * n) % 3 == 1 else 2
    Pi = [(2**(e + 2 * k) * n - 1) // 3 for k in range(6)]
    ok &= all((2**(e + 2 * k) * n - 1) % 3 == 0 for k in range(6))
    ok &= all(Pi[k + 1] == 4 * Pi[k] + 1 for k in range(5)) and all(Pi[k] % 8 == 5 for k in range(1, 6))
    # each Pi_k maps to n under the Syracuse map
    for P in Pi:
        t = 3 * P + 1
        while t % 2 == 0: t //= 2
        ok &= (t == n)
rep("13 Collatz: odd predecessors, Pi_{k+1} = 4 Pi_k + 1, Pi_k = 5 (mod 8) for k >= 1", ok)
ok = all(is_sol(P, *shell_sol(P, 3, 2, 'E')) for P in primerange(5, 20000) if P % 8 == 5)
rep("13b every prime P = 5 (mod 8) below 20000 is solved by R = 3, u = 2", ok)

# 14. mu = 17: the finite condition on the six classes modulo 42840 (independent re-derivation)
good = []
for c in range(1, 42840, 24):
    if c % 840 not in (361, 529) or c % 9 != 1 or c % 17 not in (8, 15, 16): continue
    # N = (p+17)/2 modulo 68 needs p modulo 136: p = 1 (mod 8) and p mod 17 given
    pm = c % 136
    N68 = ((pm + 17) // 2) % 68
    W = [1, 3, 7, 9, 21, 63]
    chi = lambda r: legendre_symbol(r % 17, 17) * (1 if r % 4 == 1 else -1)
    T = {(-c) % 68, 67}
    ok = True
    for r in range(1, 68, 2):
        if r % 17 == 0 or chi(r) != -1: continue
        S = {(r * w) % 68 for w in W} | {(N68 * pow(r * w, -1, 68)) % 68 for w in W}
        if not (S & T): ok = False
    good.append((c, ok, chi(67), chi((-c) % 68)))
rep("14 mu = 17: the six classes mod 42840 satisfy the finite condition; targets have chi = -1",
    len(good) == 6 and all(g[1] and g[2] == -1 and g[3] == -1 for g in good), str([g[0] for g in good]))

print(f"time {time.time() - T0:.1f}s")
