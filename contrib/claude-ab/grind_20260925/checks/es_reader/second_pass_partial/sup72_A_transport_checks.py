#!/usr/bin/env python3
"""Independent checks for the 72-statement supplement (bounded_transport.tex and
connes_primitive_intersections.tex, exact_audit/fixed_y_successor.tex).

Written from the definitions only; no workbench code is imported.
Exact integer arithmetic throughout (sympy only for primality/factorisation).

Sections
 A1  thm:glue / K_L = K_D cap K_E / obstruction / bounded fibre (random tests)
 A2  prop:crt (noncoprime CRT inverse formula)
 A3  thm:divisor-crt (algorithm vs brute force)
 A4  prop:nonzero-obstruction (p=241,a=64) and prop:local-counterexample (p=37,a=18)
 A5  thm:ratio (common integral domain of ratio transport) vs brute force
 A6  cor:adjacent / cor:connes-consecutive and the height remark (+ sharpened bound)
 A7  prop:no-shear, thm:shear, cor:family, thm:no-two-shears (+ generality tests)
 A8  prop:affine-point, thm:full-connes-shear (+ p=1753 example)
 A9  connes: prop:connes-finite-return, thm:connes-common-pairs,
     prop:connes-pair-witness, prop:connes-abstract-loss,
     prop:connes-middle-return, thm:connes-marked-successor (+ sharpened parametrisation)
 A10 thm:exact-audit-fixed-y (fixed-denominator successor)
"""
import random, time, itertools, sys
from math import gcd
from fractions import Fraction
from sympy import isprime, factorint, divisors, primerange

random.seed(20260926)
T0 = time.time()
FAIL = []
def check(cond, msg):
    if not cond:
        FAIL.append(msg)
        print("FAIL:", msg)
def lcm(a, b):
    return a // gcd(a, b) * b

# ---------------------------------------------------------------- shell basics
def shells(p):
    h = (p - 1) // 12
    return range(3 * h + 1, 9 * h + 1)

def W_direct(p, a):
    """W_a from the definition: coprime ordered (m,n), m,n | pa, R | m+n."""
    S = p * a; R = 4 * a - p
    D = divisors(S)
    return {(m, n) for m in D for n in D if gcd(m, n) == 1 and (m + n) % R == 0}

def W_fast(p, a, Da2=None):
    """W_a via the passing residual divisors d | S^2 (lem:units): m/n = d/S reduced.
    Only uses: d = p^i v, v | a^2, d = -S mod R."""
    S = p * a; R = 4 * a - p
    if Da2 is None:
        Da2 = divisors(a * a)
    out = set()
    for v in Da2:
        for i in range(3):
            d = p ** i * v
            if (d + S) % R == 0:
                g = gcd(d, S)
                out.add((d // g, S // g))
    return out

def witness_from_pair(p, a, m, n):
    S = p * a; R = 4 * a - p
    k = (m + n) // R
    return (a, (S // n) * k, (S // m) * k)

def is_witness(p, x, y, z):
    return Fraction(1, x) + Fraction(1, y) + Fraction(1, z) == Fraction(4, p)

# cross-check W_fast against W_direct on small primes
for p in [13, 37, 61, 73, 97, 109, 157]:
    for a in shells(p):
        check(W_fast(p, a) == W_direct(p, a), f"W_fast!=W_direct p={p} a={a}")
print("[A0] W_a via residual divisors equals W_a by definition on 7 small primes: ok")

# ---------------------------------------------------------------- A1 thm:glue
def ordmod(q, D):
    if D == 1:
        return 1
    x, k = q % D, 1
    while x != 1:
        x = x * q % D; k += 1
    return k

def phi(qs, e, D):
    """product q_j^{e_j} mod D (negative exponents via inverses)."""
    r = 1
    for q, ej in zip(qs, e):
        if ej >= 0:
            r = r * pow(q, ej, D) % D
        else:
            r = r * pow(pow(q, -1, D), -ej, D) % D
    return r % D

def glue_test(trials=150):
    nobs_nonzero = nobs_zero = 0
    done = 0
    while done < trials:
        s = random.choice([1, 2, 3])
        qs = random.sample([2, 3, 5, 7, 11, 13], s)
        P = 1
        for q in qs:
            P *= q
        cand = [m for m in range(3, 120) if gcd(m, P) == 1]
        D = random.choice(cand); E = random.choice(cand)
        L = lcm(D, E)
        T = [ordmod(q, L) for q in qs]           # phi_L depends only on e mod T
        size = 1
        for t_ in T:
            size *= t_
        if size > 4000:
            continue
        done += 1
        box = list(itertools.product(*[range(t) for t in T]))
        # K_L = K_D cap K_E on the period box
        for e in box:
            inD = phi(qs, e, D) == 1 % D; inE = phi(qs, e, E) == 1 % E
            check((phi(qs, e, L) == 1 % L) == (inD and inE), "K_L != K_D cap K_E")
        HD = sorted({phi(qs, e, D) for e in box}); HE = sorted({phi(qs, e, E) for e in box})
        rD = random.choice(HD); rE = random.choice(HE)
        x = next(e for e in box if phi(qs, e, D) == rD % D)
        y = next(e for e in box if phi(qs, e, E) == rE % E)
        diff = tuple(xi - yi for xi, yi in zip(x, y))
        # obstruction zero iff diff in K_D + K_E iff exists kD in K_D with diff-kD in K_E
        # kD may be taken mod lcm of periods (period box of L) -- phi_E depends on e mod ord_E | T
        KD = [e for e in box if phi(qs, e, D) == 1 % D]
        zero = any(phi(qs, tuple(di - ki for di, ki in zip(diff, k)), E) == 1 % E for k in KD)
        common = [e for e in box if phi(qs, e, D) == rD % D and phi(qs, e, E) == rE % E]
        check(zero == (len(common) > 0), "glue obstruction criterion")
        if zero:
            nobs_zero += 1
            kD = next(k for k in KD if phi(qs, tuple(di - ki for di, ki in zip(diff, k)), E) == 1 % E)
            e0 = tuple(xi - ki for xi, ki in zip(x, kD))
            check(phi(qs, e0, D) == rD % D and phi(qs, e0, E) == rE % E, "e0 not a common lift")
            # every common lift differs from e0 by K_L
            for c in common:
                check(phi(qs, tuple(ci - ei for ci, ei in zip(c, e0)), L) == 1 % L, "fibre e0+K_L")
        else:
            nobs_nonzero += 1
    return nobs_zero, nobs_nonzero
z, nz = glue_test()
print(f"[A1] thm:glue: K_L=K_D cap K_E, obstruction criterion, e0+K_L fibre on 150 random systems "
      f"({z} zero / {nz} nonzero obstructions): ok")

# ---------------------------------------------------------------- A2 prop:crt
cnt = 0
for _ in range(3000):
    D = random.randint(1, 300); E = random.randint(1, 300)
    g = gcd(D, E); L = lcm(D, E); D0, E0 = D // g, E // g
    r = random.randrange(D); s = random.randrange(E)
    if (s - r) % g:
        # incompatible: no w mod L
        check(not any(w % D == r and w % E == s for w in range(L)), "prop:crt incompatible has solution")
        continue
    c = (s - r) // g
    v = pow(D0, -1, E0) if E0 > 1 else 0
    w = r + D * ((v * c) % E0 if E0 > 1 else 0)
    check(w % D == r and w % E == s, "prop:crt formula")
    sols = [t for t in range(L) if t % D == r and t % E == s]
    check(sols == [w % L], "prop:crt uniqueness mod L")
    cnt += 1
print(f"[A2] prop:crt inverse formula and uniqueness on {cnt} compatible random pairs: ok")

# ---------------------------------------------------------------- A3 thm:divisor-crt
def divisor_crt(Ns, fs, congs):
    N = 0
    for x in Ns:
        N = gcd(N, x)
    f = 1
    for x in fs:
        f = lcm(f, x)
    if N % f:
        return []
    r, Lm = 0, 1
    for (c, b, M) in congs:
        g = gcd(c, M)
        if b % g:
            return []
        m = M // g
        ri = (pow(c // g, -1, m) * (b // g)) % m if m > 1 else 0
        # merge r mod Lm with ri mod m (prop:crt)
        gg = gcd(Lm, m)
        if (ri - r) % gg:
            return []
        if m // gg > 1:
            cc = (ri - r) // gg
            v = pow(Lm // gg, -1, m // gg)
            r = r + Lm * ((v * cc) % (m // gg))
        Lm = lcm(Lm, m); r %= Lm
    fac = factorint(N)
    out = []
    # monoid DP with stored exponent choices
    states = [(1, ())]
    for ell, e in sorted(fac.items()):
        d = factorint(f).get(ell, 0)
        states = [(u * ell ** j, ch + (j,)) for (u, ch) in states for j in range(d, e + 1)]
    for u, ch in states:
        if u % Lm == r % Lm:
            out.append(u)
    return sorted(out)

ntest = 0
for _ in range(1500):
    Ns = [random.choice([360, 720, 5040, 2**5*3**3*5, 4*9*49, 1001*6, 1260, 30030])
          * random.choice([1, 2, 3]) for _ in range(random.randint(1, 3))]
    fs = [random.choice([1, 2, 3, 4, 6, 5, 12]) for _ in range(random.randint(0, 2))]
    congs = [(random.randint(-5, 12), random.randint(-20, 20), random.randint(1, 40))
             for _ in range(random.randint(0, 3))]
    N = 0
    for x in Ns:
        N = gcd(N, x)
    brute = sorted(u for u in divisors(N) if all(x % u == 0 for x in Ns)
                   and all(u % f == 0 for f in fs)
                   and all((c * u - b) % M == 0 for (c, b, M) in congs))
    check(divisor_crt(Ns, fs, congs) == brute, f"divisor-crt mismatch {Ns} {fs} {congs}")
    ntest += 1
# E/M substitution on actual shells
for p in [37, 61, 73, 241, 1201]:
    for a in shells(p):
        R = 4 * a - p
        Ea = divisor_crt([a * a], [], [(4, -1, R)])
        Ma = divisor_crt([a * a], [], [(1, -a, R)])
        check(Ea == sorted(u for u in divisors(a * a) if (4 * u + 1) % R == 0), "E_a via divisor-crt")
        check(Ma == sorted(u for u in divisors(a * a) if (u + a) % R == 0), "M_a via divisor-crt")
print(f"[A3] thm:divisor-crt algorithm = brute force on {ntest} random systems and on all shells of 5 primes: ok")

# ---------------------------------------------------------------- A4 the two finite propositions
p, a = 241, 64
check(isprime(p) and 4 * a - p == 15 and a * a == 2 ** 12, "241 setup")
check((-pow(4, -1, 15)) % 15 == 11 and (-64) % 15 == 11, "241 targets")
js3 = [j for j in range(13) if pow(2, j, 3) == 11 % 3]; js5 = [j for j in range(13) if pow(2, j, 5) == 11 % 5]
check(set(js3) == set(range(1, 13, 2)) and set(js5) == {0, 4, 8, 12}, "241 local lifts")
check(not (set(js3) & set(js5)), "241 no common exponent")
check(all(pow(2, j, 15) != 11 for j in range(0, 200)), "241 no integral exponent lift at all")
check(not any((4 * u + 1) % 15 == 0 or (u + 64) % 15 == 0 for u in divisors(64 * 64)), "241 E=M=empty")
p, a = 37, 18
R = 4 * a - p; S = p * a
check(R == 35 and S == 666, "37/18 setup")
D324 = divisors(324)
tab = {Dm: ([u for u in D324 if (4 * u + 1) % Dm == 0], [u for u in D324 if (u + 18) % Dm == 0]) for Dm in (5, 7)}
check(tab[5] == ([1, 6, 36, 81], [2, 12, 27, 162]) and tab[7] == ([12, 54], [3, 108]), "37/18 table")
check(W_direct(37, 18) == set(), "37/18 W empty")
F5 = [(i, j) for i in range(3) for j in range(5) if (i + 3 * j) % 4 == 0]
F7 = [(i, j) for i in range(3) for j in range(5) if (2 * i + j) % 6 == 5]
check(sorted(F5) == sorted([(0, 0), (1, 1), (2, 2), (0, 4)]) and sorted(F7) == sorted([(2, 1), (1, 3)]), "37/18 fibres")
check(all(pow(2, i, 5) * pow(3, j, 5) % 5 == 1 for i, j in F5), "K5 description")
check((2 ** 5 * 3) == 96 and 4 * 96 + 1 == 385 == 5 * 7 * 11 and 96 % 35 == 26, "U(5,1)=96")
check(22 % 5 == 2 and 22 % 7 == 1 and 13 % 5 == 3 and 13 % 7 == 6, "orchard CRT (22,13)")
print("[A4] prop:nonzero-obstruction (p=241,a=64) and prop:local-counterexample (p=37,a=18): all displayed data reproduce")

# ---------------------------------------------------------------- A5 thm:ratio
def primes_1mod12(lo, hi):
    return [q for q in primerange(lo, hi) if q % 12 == 1]

npairs = 0; nonempty = 0
for p in primes_1mod12(13, 260):
    Ws = {a: W_fast(p, a) for a in shells(p)}
    for a in shells(p):
        for b in shells(p):
            if a == b:
                continue
            g = gcd(a, b); Lr = lcm(4 * a - p, 4 * b - p)
            Dg = divisors(p * g)
            formula = {(m, n) for m in Dg for n in Dg if gcd(m, n) == 1 and (m + n) % Lr == 0}
            # brute: integral witnesses at a whose transported image is integral at b
            brute = set()
            for (m, n) in Ws[a]:
                x, y, z = witness_from_pair(p, a, m, n)
                fac = Fraction(b * (4 * a - p), a * (4 * b - p))
                y2, z2 = fac * y, fac * z
                if y2.denominator == 1 and z2.denominator == 1:
                    check(is_witness(p, b, int(y2), int(z2)), "ratio image not a witness")
                    brute.add((m, n))
            check(brute == formula, f"thm:ratio p={p} a={a} b={b}")
            npairs += 1; nonempty += bool(brute)
print(f"[A5] thm:ratio common domain = {{m,n | pg, coprime, lcm(R_a,R_b) | m+n}} on all {npairs} ordered shell pairs "
      f"of the primes p=1 mod 12 below 260 ({nonempty} nonempty): ok")

# ---------------------------------------------------------------- A6 adjacent persistent ratios
t = time.time()
cases = []
for p in primes_1mod12(13, 2_000_000):
    h = (p - 1) // 12
    # R(R+4) | p+1 with a=(p+R)/4, a+1 <= 9h
    R = 3
    while R * (R + 4) <= p + 1:
        a = (p + R) // 4
        if (p + 1) % (R * (R + 4)) == 0 and 3 * h + 1 <= a and a + 1 <= 9 * h:
            cases.append((p, R, a))
        R += 4
check(all(R % 12 == 7 for (_, R, _) in cases), "adjacent: R = 7 mod 12 forced")
check(all(10 * R * (R + 4) <= p + 1 for (p, R, _) in cases), "adjacent: 10R(R+4) <= p+1")
check(all(((p + 1) // (R * (R + 4))) % 12 == 10 for (p, R, _) in cases), "adjacent: (p+1)/(R(R+4)) = 10 mod 12")
eq = [(p, R) for (p, R, _) in cases if 10 * R * (R + 4) == p + 1]
check((769, 7) in eq, "769 equality")
print(f"[A6] adjacent persistent ratios, all primes p=1 mod 12 below 2e6: {len(cases)} cases; "
      f"every case has R=7 mod 12 and (p+1)/(R(R+4)) = 10 mod 12, so 10R(R+4) <= p+1; "
      f"equality cases (p,R): {eq[:8]}{'...' if len(eq) > 8 else ''} ({len(eq)} total); "
      f"R(R+4)=p+1 never occurs ({time.time()-t:.1f}s)")
# brute check of the corollary's two-pair claim on small primes
for p in primes_1mod12(13, 3000):
    for a in shells(p):
        if a + 1 not in shells(p):
            continue
        R = 4 * a - p
        com = W_fast(p, a) & W_fast(p, a + 1)
        pred = {(p, 1), (1, p)} if (p + 1) % (R * (R + 4)) == 0 else set()
        check(com == pred, f"cor:adjacent p={p} a={a}")
check(witness_from_pair(769, 194, 769, 1)[0] == 194 and 4 * 194 - 769 == 7 and 770 == 10 * 7 * 11, "769 example")
print("[A6] cor:adjacent common pairs = {(p,1),(1,p)} iff R(R+4) | p+1, all adjacent shells of primes p=1 mod 12 below 3000: ok")

# ---------------------------------------------------------------- A7 shears
def all_edges(p, lo, hi):
    """All L- and J-edges between consecutive shells a, a+1 with lo <= a < a+1 <= hi.
    Brute force from the definition of W."""
    Ws = {}
    for a in range(lo, hi + 1):
        Ws[a] = W_fast(p, a)
    Ledges, Jedges = [], []
    for a in range(lo, hi):
        Wn = Ws[a + 1]
        for (m, n) in Ws[a]:
            if (m + n, n) in Wn:
                Ledges.append((a, m, n))
            if (m, m + n) in Wn:
                Jedges.append((a, m, n))
    return Ws, Ledges, Jedges

def shear_param(p, lo, hi):
    """predicted L-edge sources (a,m,1) from eq. (shear-m), (shear-ap)."""
    out = set()
    R = 3
    while True:
        base = R * (R + 5) // 4 - 1
        if 4 * base - R > p:  # a >= m >= base so p = 4a - R >= 4 base - R
            break
        t = 0
        while True:
            m = base + R * (R + 4) * t
            if 4 * m - R > p:
                break
            c = 0
            while True:
                a = m + c * m * (m + 1)
                if 4 * a - R > p:
                    break
                if 4 * a - R == p and lo <= a and a + 1 <= hi:
                    out.add((a, m, 1))
                c += 1
            t += 1
        R += 4
    return out

t = time.time()
nL = nJ = 0; nprimes = 0
for p in primes_1mod12(13, 4000):
    h = (p - 1) // 12
    Ws, Le, Je = all_edges(p, 3 * h + 1, 9 * h)
    nprimes += 1
    # prop:no-shear: L(m,n), J(m,n) never in P(S_a) (m+n never divides S_a)
    for a, W in Ws.items():
        for (m, n) in W:
            check((p * a) % (m + n) != 0, "prop:no-shear")
    # thm:shear classification
    check(set(Le) == shear_param(p, 3 * h + 1, 9 * h), f"thm:shear L-edges p={p}")
    check({(a, n, m) for (a, m, n) in Je} == set(Le), f"thm:shear J = PLP p={p}")
    for (a, m, n) in Le:
        R = 4 * a - p
        check(n == 1 and a % m == 0 and (a + 1) % (m + 1) == 0 and (m + 1) % R == 0 and (m + 2) % (R + 4) == 0,
              "shear-domain conditions")
    # thm:no-two-shears: no directed path of length two; components are single edges
    edges = [((a, m, n), (a + 1, m + n, n)) for (a, m, n) in Le] + [((a, m, n), (a + 1, m, m + n)) for (a, m, n) in Je]
    srcs = {e[0] for e in edges}; tgts = {e[1] for e in edges}
    check(not (srcs & tgts), f"no-two-shears p={p}")
    check(len(srcs) == len(edges) and len(tgts) == len(edges), f"degree<=1 p={p}")
    nL += len(Le); nJ += len(Je)
print(f"[A7] prop:no-shear; thm:shear (brute-force L-edges = parametrised family; J-edges = swapped L-edges); "
      f"thm:no-two-shears (no length-2 path, all degrees <= 1): all shells of {nprimes} primes p=1 mod 12 below 4000, "
      f"{nL} L-edges, {nJ} J-edges ({time.time()-t:.1f}s)")

# cor:family
for c in range(0, 60):
    p = 73 + 1680 * c
    if not isprime(p):
        continue
    a = 20 + 420 * c
    h = (p - 1) // 12
    check(3 * h + 1 <= a and a + 1 <= 9 * h, "family interval")
    check((20, 1) in W_fast(p, a) and (21, 1) in W_fast(p, a + 1), f"cor:family c={c}")
check(witness_from_pair(73, 20, 20, 1) == (20, 4380, 219) and witness_from_pair(73, 21, 21, 1) == (21, 3066, 146), "73 triples")
print("[A7] cor:family: (20,1) -> (21,1) passes at every prime p = 73 + 1680c, c < 60; triples at p=73 reproduce")

# generality: which hypotheses does thm:no-two-shears need?  Test other prime classes,
# shells p/4 < a < p (all first-denominator shells of Theorem 43.1(b)).
t = time.time()
gen = {1: 0, 5: 0, 7: 0, 11: 0}
paths = {1: [], 5: [], 7: [], 11: []}
for p in primerange(5, 1500):
    lo = p // 4 + 1; hi = p - 1
    Ws, Le, Je = all_edges(p, lo, hi)
    edges = [((a, m, n), (a + 1, m + n, n)) for (a, m, n) in Le] + [((a, m, n), (a + 1, m, m + n)) for (a, m, n) in Je]
    srcs = {e[0] for e in edges}
    for e in edges:
        if e[1] in srcs:
            paths[p % 12].append((p, e))
    gen[p % 12] += 1
print(f"[A7-gen] length-2 shear paths over all shells p/4<a<p, primes 5<=p<1500, by p mod 12: "
      + ", ".join(f"{k}: {len(v)} paths in {gen[k]} primes" for k, v in paths.items())
      + f" ({time.time()-t:.1f}s)")
for k in (5, 11):
    if paths[k]:
        print(f"        first length-2 path at p = {k} mod 12: {paths[k][0]}")

# ---------------------------------------------------------------- A8 affine point maps
def Psi(N, M, c, x):
    return Fraction(N, M) * x - Fraction(c, M)
for _ in range(400):
    N, M, L3 = random.randint(1, 60), random.randint(1, 60), random.randint(1, 60)
    c, d = random.randint(-30, 30), random.randint(-30, 30)
    x = Fraction(random.randint(-50, 50), N)
    check(Psi(M, L3, d, Psi(N, M, c, x)) == Psi(N, L3, c + d, x), "affine composition")
    y = Psi(N, M, c, x)
    check(y.denominator in divisors(M) and Fraction(M, N) * y + Fraction(c, N) == x, "affine inverse")
    # divisor return
    ret = {u: M // (N // u - c) for u in divisors(N) if N // u > c and M % (N // u - c) == 0}
    brute = {}
    for u in divisors(N):
        im = Psi(N, M, c, Fraction(1, u))
        if im > 0 and im.numerator == 1:
            brute[u] = im.denominator
    check(ret == brute, "affine divisor return")
    # conjugate formula
    for u in divisors(N):
        xx = Fraction(1, u)
        iota = lambda Nn, z: 1 / (Nn * z)
        if u != c:
            val = iota(M, Psi(N, M, c, iota(N, xx)))
            check(val == xx / (1 - c * xx), "conjugate affine formula")
nE = 0
for p in primes_1mod12(13, 4000):
    h = (p - 1) // 12
    _, Le, _ = all_edges(p, 3 * h + 1, 9 * h)
    for (a, m, n) in Le:
        b = a + 1; c = (a // m - 1) // (m + 1)
        check(a == m + c * m * (m + 1), "edge param c")
        u, v = a * m, b * (m + 1)
        check((a * a) % u == 0 and (b * b) % v == 0, "u|a^2, v|b^2")
        check(Psi(a * a, b * b, c, Fraction(1, u)) == Fraction(1, v), "Psi(1/u)=1/v")
        e, ep = a * a // u, b * b // v
        check(e == 1 + c * (m + 1) and ep == 1 + c * m and e - ep == c, "indices")
        if c > 0:
            check((b * b) % e != 0, "uncorrected no return")
        # J version
        u2, v2 = a // m, b // (m + 1)
        check(v2 == u2 - c and (a * a) % u2 == 0 and (b * b) % v2 == 0, "J divisors")
        nE += 1
p, a, b, m, c = 1753, 440, 441, 20, 1
check(isprime(p) and 4 * a - p == 7 and 4 * b - p == 11 and a == m + c * m * (m + 1), "1753 setup")
check(Psi(a * a, b * b, 1, Fraction(1, 8800)) == Fraction(1, 9261) and a * a == 193600 and b * b == 194481, "1753 Psi")
check(witness_from_pair(p, a, 20, 1) == (440, 2313960, 115698) and witness_from_pair(p, b, 21, 1) == (441, 1546146, 73626), "1753 witnesses")
print(f"[A8] prop:affine-point (400 random maps: composition, inverse, divisor return, conjugate formula); "
      f"thm:full-connes-shear on all {nE} L-edges below 4000 and the p=1753 example: ok")

# ---------------------------------------------------------------- A9 Connes-Consani interface
for _ in range(300):
    N, M = random.randint(1, 400), random.randint(1, 400)
    g, L2 = gcd(N, M), lcm(N, M)
    # H_N = (1/N)Z; H_N cap H_M = H_g ; H_N + H_M = H_L  (test on the window of numerators)
    inter = {Fraction(k, N) for k in range(-3 * N, 3 * N + 1) if (Fraction(k, N) * M).denominator == 1}
    check(inter == {Fraction(k, g) for k in range(-3 * g, 3 * g + 1)}, "H_N cap H_M")
    check(gcd(L2 // N, L2 // M) == 1, "H_N + H_M = H_L generator")
    check((N % M == 0) == (Fraction(1, M) in {Fraction(k, N) for k in range(N + 1)}), "inclusion criterion")
for p in primes_1mod12(13, 400):
    for a in shells(p):
        R = 4 * a - p
        Wa = W_fast(p, a)
        # prop:connes-pair-witness: formula and converse
        for (m, n) in Wa:
            k = (p * a) // (m * n) * (m + n) // R
            check((p * a) % (m * n) == 0 and is_witness(p, a, k * m, k * n), "pair witness")
        # prop:connes-middle-return
        Da2 = divisors(a * a)
        pairs = {}
        for u in Da2:
            gg = gcd(u, a); mm, nn = u // gg, a // gg
            pairs[u] = (mm, nn)
            check(a % mm == 0 and a % nn == 0 and gcd(mm, nn) == 1 and a * mm // nn == u, "mu_a")
            check(((u + a) % R == 0) == ((mm + nn) % R == 0), "mu_a mark")
            if (u + a) % R == 0:
                y, z = Fraction(p * (a + u), R), Fraction(p * (a + a * a // u), R)
                check(y.denominator == 1 and z.denominator == 1 and is_witness(p, a, int(y), int(z)) and y / z == Fraction(u, a), "middle return")
        check(len(set(pairs.values())) == len(Da2), "mu_a injective")
        allpairs = {(mm, nn) for mm in divisors(a) for nn in divisors(a) if gcd(mm, nn) == 1}
        check(set(pairs.values()) == allpairs, "mu_a onto")
        # abstract loss: phi_{pa,pb}(1/m) integral primitive only when a=b (test b=a+1..)
        for b in (a + 1, a + 2):
            if b in shells(p):
                for (m, n) in Wa:
                    mp, np_ = Fraction(b * m, a), Fraction(b * n, a)
                    check(not (mp.denominator == 1 and np_.denominator == 1 and gcd(int(mp), int(np_)) == 1), "abstract loss")
print("[A9] connes: H_N intersections/sums, pair-witness formula, middle-channel bijection mu_a and its mark, "
      "abstract-isomorphism non-return: ok (primes below 400)")

t = time.time()
succ = []
for p in primes_1mod12(13, 300000):
    h = (p - 1) // 12
    R = 3
    while R * (R + 4) <= p + 4:
        a = (p + R) // 4
        if a + 1 <= 9 * h:
            both = ((a * a + a) % R == 0) and (((a + 1) ** 2 + (a + 1)) % (R + 4) == 0)
            check(both == ((p + 4) % (R * (R + 4)) == 0), "marked successor criterion")
            check((4 * a * a + 1) % R != 0 and (4 * (a + 1) ** 2 + 1) % (R + 4) != 0, "E never marked")
            if both:
                succ.append((p, R, a))
        R += 4
for (p, R, a) in succ:
    k = (p + 4) // (R * (R + 4))
    check(k % 4 == 1 and a == R * (R + 5) // 4 - 1 + R * (R + 4) * ((k - 1) // 4), "marked param")
    check(R % 12 == 7 and ((k - 1) // 4) % 3 == 0, "sharpened: R=7 mod 12, t=0 mod 3")
    x1 = (a, p * a * (a + 1) // R, p * (a + 1) // R); x2 = (a + 1, p * (a + 1) * (a + 2) // (R + 4), p * (a + 2) // (R + 4))
    check(is_witness(p, *x1) and is_witness(p, *x2), "marked successor triples")
print(f"[A9] thm:connes-marked-successor on all primes p=1 mod 12 below 3e5: {len(succ)} successful (p,R); "
      f"criterion R(R+4) | p+4, E never marked, parametrisation, and every case has R=7 mod 12 and t=0 mod 3 "
      f"(first: {succ[:4]}) ({time.time()-t:.1f}s)")

# ---------------------------------------------------------------- A10 fixed-denominator successor
t = time.time()
ndom = nsrc = 0
for p in primes_1mod12(13, 1500):
    h = (p - 1) // 12
    for a in range(3 * h + 1, 9 * h):
        b = a + 1; R = 4 * a - p; A = a * b
        Ia = {witness_from_pair(p, a, m, n)[1:] for (m, n) in W_fast(p, a)}
        Ib = {witness_from_pair(p, b, m, n)[1:] for (m, n) in W_fast(p, b)}
        Da = {(y, z) for (y, z) in Ia if (A * A) % (A + z) == 0}
        Db = {(y, zp) for (y, zp) in Ib if 0 < zp < A and (A * A) % (A - zp) == 0}
        img = set()
        for (y, z) in Da:
            zp = Fraction(A * z, A + z)
            check(zp.denominator == 1 and 0 < zp < min(z, A), "T_a integral and decreasing")
            img.add((y, int(zp)))
        check(img == Db, f"T_a bijection p={p} a={a}")
        for (y, zp) in Db:
            z = Fraction(A * zp, A - zp)
            check(z.denominator == 1 and (y, int(z)) in Da, "inverse")
        # budget equivalence on every source witness
        for (m, n) in W_fast(p, a):
            _, y, z = witness_from_pair(p, a, m, n)
            U, V = a * (R + 4) * m + p * n, (a + 1) * R * n
            g = gcd(U, V); mp, np_ = U // g, V // g
            check(Fraction(mp, np_) == Fraction(y, 1) / (Fraction(1, 1) / (Fraction(1, z) + Fraction(1, A))), "ratio formula")
            cond = (p * b) % mp == 0 and (p * b) % np_ == 0 and (mp + np_) % (R + 4) == 0
            check(cond == ((A * A) % (A + z) == 0), "budget equivalence")
            nsrc += 1
        ndom += len(Da)
# examples
check(witness_from_pair(13, 4, 13, 2) == (4, 130, 20), "p=13 source")
check(witness_from_pair(37, 12, 3, 74) == (12, 42, 1036), "p=37 source")
check(Fraction(156 * 1036, 156 + 1036) == Fraction(20202, 149), "p=37 z'")
U, V = 12 * 15 * 3 + 37 * 74, 13 * 11 * 74
check((U, V, gcd(U, V), U // gcd(U, V), V // gcd(U, V)) == (3278, 10582, 22, 149, 481), "p=37 U,V")
print(f"[A10] thm:exact-audit-fixed-y: bijection D_a -> D_b^-, strict decrease, ratio formula and the budget "
      f"equivalence on all {nsrc} source witnesses (primes p=1 mod 12 below 1500; {ndom} domain points); "
      f"both examples reproduce ({time.time()-t:.1f}s)")

print()
print("TOTAL FAILURES:", len(FAIL))
print(f"runtime {time.time()-T0:.1f}s")
