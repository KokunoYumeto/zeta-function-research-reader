#!/usr/bin/env python3
"""Independent checks of the statements that the workbench reader proves or quotes.

Written by claude-ab (model claude-opus-5-5, Opus 5.5) on 26 September 2026 from the
definitions in the reader, without importing any workbench code or any script of the
first-pass audits (audit43-audit46).  Exact integer / Fraction / sympy arithmetic
throughout; mpmath only for displayed decimals.

Sections:  ES  (Erdos-Straus shell criterion, R3 sieve, mod-840 classes, classical families)
           CZ  (Collatz: nu_3 lemma, merging families, section-5 progression, one-step cycles,
                the 678 bound, the sqrt(15)/4 inequality, cylinder classes)
           EP  (Erdos 817: digit set mod 19, lift, kappa_m, B* and A# certificates, composition)
           YM  (alpha_5 by root isolation, d_5, Casimir lemma on the cube, face count,
                S6-5 cubic, NS-04(b) Kasner identities, the Keller map F)
"""
import itertools, math, random, time
from fractions import Fraction as Fr
import sympy as sp

T0 = time.time()
FAIL = []
def ok(name, cond, info=""):
    print(("[PASS] " if cond else "[FAIL] ") + name + (": " + str(info) if info != "" else ""))
    if not cond:
        FAIL.append(name)

# ----------------------------------------------------------------------------- ES
def divisors_of_square(a):
    f = sp.factorint(a)
    ds = [1]
    for q, e in f.items():
        ds = [d * q**k for d in ds for k in range(2 * e + 1)]
    return ds

def shell_sets(p, a):
    R = 4 * a - p
    D = divisors_of_square(a)
    E = [u for u in D if (4 * u + 1) % R == 0]
    M = [u for u in D if (u + a) % R == 0]
    return R, E, M

def ordered_pairs(p, a):
    """ordered (y,z) in Z_{>0}^2 with 1/a + 1/y + 1/z = 4/p, by brute force over y."""
    num = 4 * a - p            # 1/y + 1/z = num/(p a)
    den = p * a
    cnt = 0
    y = den // num + 1         # y > den/num
    while y * num <= 2 * den:  # y <= 2 den/num for the smaller one; count both orders below
        r_num = num * y - den  # 1/z = (num*y - den)/(den*y)
        if r_num > 0 and (den * y) % r_num == 0:
            z = den * y // r_num
            cnt += 1 if z == y else 2
        y += 1
    return cnt

def es_section():
    primes = [p for p in sp.primerange(13, 700) if p % 12 == 1]
    shells = 0; bad = 0; odd_M = 0
    for p in primes:
        h = (p - 1) // 12
        for a in range(3 * h + 1, 9 * h + 1):
            R, E, M = shell_sets(p, a)
            shells += 1
            if ordered_pairs(p, a) != 2 * len(E) + len(M): bad += 1
            if len(M) % 2: odd_M += 1
    ok("ES shell count: ordered (y,z) = 2|E_a|+|M_a| on every shell, primes p=1 mod 12 below 700",
       bad == 0, f"{shells} shells, {len(primes)} primes")
    ok("ES |M_a| even on every shell", odd_M == 0)
    # minimal denominator: 1/a < 4/p <= 3/a gives p/4 < a <= 3p/4; for p = 12h+1 the integers are 3h+1..9h
    okr = all([k for k in range(1, 10**5) if 4 * k > p and 4 * k <= 3 * p] == list(range(3 * ((p - 1) // 12) + 1, 9 * ((p - 1) // 12) + 1))
              for p in (13, 37, 61, 97, 1201, 12 * 777 + 1))
    ok("ES integers in (p/4, 3p/4] are exactly 3h+1..9h for p = 12h+1 (spot values)", okr)
    # Q_p > 0
    miss = [p for p in sp.primerange(13, 30000) if p % 12 == 1 and
            not any(shell_sets(p, a)[1] or shell_sets(p, a)[2]
                    for a in range(3 * ((p - 1) // 12) + 1, 9 * ((p - 1) // 12) + 1))]
    ok("ES Q_p > 0 for every prime p = 1 mod 12 below 30000", not miss, miss[:5])
    # R3 sieve at a = 3h+1 (R = 3)
    badR3 = 0; nR3 = 0
    for p in sp.primerange(13, 200000):
        if p % 12 != 1: continue
        h = (p - 1) // 12; a = 3 * h + 1
        R, E, M = shell_sets(p, a)
        f = sp.factorint(a)
        P1 = math.prod(2 * e + 1 for q, e in f.items() if q % 3 == 1)
        P2 = math.prod(2 * e + 1 for q, e in f.items() if q % 3 == 2)
        has2 = any(q % 3 == 2 for q in f)
        nR3 += 1
        if R != 3 or (bool(E or M) != has2) or len(E) != P1 * (P2 - 1) // 2 or len(M) != len(E):
            badR3 += 1
    ok("ES R3 sieve: shell a=(p+3)/4 occupied iff a has a prime factor = 2 mod 3; |E|=|M|=P1(P2-1)/2",
       badR3 == 0, f"{nR3} primes below 2e5")
    # R7 sieve at a = 3h+2 (R = 7): occupied iff (prime factor = 5 or 6 mod 7) or n3 >= 3 or (n3 >= 1 and n24 >= 1)
    badR7 = 0; nR7 = 0
    for p in sp.primerange(13, 200000):
        if p % 12 != 1: continue
        h = (p - 1) // 12; a = 3 * h + 2
        R, E, M = shell_sets(p, a)
        f = sp.factorint(a)
        n3 = sum(e for q, e in f.items() if q % 7 == 3)
        n24 = sum(e for q, e in f.items() if q % 7 in (2, 4))
        pred = any(q % 7 in (5, 6) for q in f) or n3 >= 3 or (n3 >= 1 and n24 >= 1)
        nR7 += 1
        if R != 7 or bool(E or M) != pred: badR7 += 1
    ok("ES R7 sieve: shell a=(p+7)/4 occupied iff factor =5,6 mod 7, or n3>=3, or n3>=1 and n24>=1",
       badR7 == 0, f"{nR7} primes below 2e5")
    sq = sorted({(c * c) % 840 for c in range(840) if math.gcd(c, 840) == 1})
    ok("ES unit squares mod 840 = {1,121,169,289,361,529}", sq == [1, 121, 169, 289, 361, 529], sq)
    # classical families
    badf = 0
    for p in sp.primerange(3, 20000):
        if p % 3 == 2:
            x, y, z = p, (p + 1) // 3, p * (p + 1) // 3
        elif p % 4 == 3:
            x, y, z = (p + 1) // 4, p * (p + 1) // 2, p * (p + 1) // 2
        elif p % 24 == 13:
            a = (p + 3) // 4; x, y, z = a, p * a // 2, p * a
        else:
            continue
        if Fr(1, x) + Fr(1, y) + Fr(1, z) != Fr(4, p): badf += 1
    ok("ES classical families for p=2 mod 3, p=3 mod 4, p=13 mod 24 (p<20000)", badf == 0)

# ----------------------------------------------------------------------------- CZ
def nu(n, q):
    k = 0
    while n % q == 0:
        n //= q; k += 1
    return k

def Tstep(n):
    m = 3 * n + 1; a = nu(m, 2)
    return m >> a, a

def word_of(n, steps):
    w = []
    for _ in range(steps):
        n, a = Tstep(n); w.append(a)
    return n, w

def cz_section():
    ok("CZ nu_3((2^e+2)/3) = nu_3(e-1) for all even 2 <= e <= 3000",
       all(nu((2**e + 2) // 3, 3) == nu(e - 1, 3) for e in range(2, 3001, 2)))
    bad = 0
    for v in list(range(0, 400)) + [random.randrange(10**9) for _ in range(100)] + [10**30 + 7]:
        n = 20241207 + 1549681956 * v; m = 14024703 + 2**30 * v; y = 30361811 + 2324522934 * v
        yn, wn = word_of(n, 1); ym, wm = word_of(m, 19)
        if not (yn == y and wn == [1] and ym == y and wm == [1] * 16 + [8, 2, 3] and m < n): bad += 1
    ok("CZ section-5 progression: n ->(1) y <-(1^16,8,2,3) m, m<n (500 values of v incl. 10^30+7)", bad == 0)
    # merging families from the definitions (independent implementation)
    fam = 0; badfam = 0
    for e in range(2, 21, 2):
        he = (2**e + 2) // 3
        for b in range(1, 7):
            for sig in (0, 1):
                a = 1
                while not (2**(a + e + 2 * b - sig) < 3**(a + b)): a += 1
                J = 2**(e + 2 * b - sig); Q = 3**(a + b); K = 2**a * J
                d, r = (4, 3) if sig == 0 else (32, 27)
                # n = r mod d and J n + he 3^b = 0 mod Q
                n0 = None
                x = (-he * 3**b * pow(J, -1, Q)) % Q
                for k in range(d):
                    if (x + k * Q) % d == r: n0 = x + k * Q; break
                if n0 is None or n0 == 0:
                    badfam += 1; continue
                m0 = (K * n0 + 2**a * he * 3**b) // Q - 1
                lw = [1] if sig == 0 else [1, 2, 1]
                rw = [1] * a + [e] + [2] * (b - 1) + ([3] if sig == 0 else [1, 1, 3])
                for v in (0, 1, 2, 7, 10**12 + 3):
                    n = n0 + d * Q * v; m = m0 + d * K * v
                    yn, wn = word_of(n, len(lw)); ym, wm = word_of(m, len(rw))
                    fam += 1
                    if not (wn == lw and wm == rw and yn == ym and 0 < m < n and nu(n, 3) == b + nu(he, 3)):
                        badfam += 1
    ok("CZ merging families (Theorem 2) from the definitions: words, common value, 0<m<n, nu_3(n)=b+t_e",
       badfam == 0, f"{fam} pairs, e<=20, b<=6, both selectors")
    # one exponent-1 step cycles: word (1,2^{m-1}) gives n(D) = 2*4^{m-1}-3^{m-1}; D = 2*4^{m-1}-3^m
    sols = []
    for mm in range(1, 200):
        D = 2 * 4**(mm - 1) - 3**mm; N = 2 * 4**(mm - 1) - 3**(mm - 1)
        if N % D == 0: sols.append((mm, N // D))
    ok("CZ word (1,2,...,2): integer cycle values only n=-1 (m=1) and n=-5 (m=2), none positive (m<200)",
       sols == [(1, -1), (2, -5)], sols)
    # hypothesis of the 678 bound: every odd n <= 330749 reaches 1 (each odd n descends below itself; induction)
    capped = 0
    for n0 in range(3, 330750, 2):
        xx = n0; steps = 0
        while xx >= n0:
            xx, _ = Tstep(xx); steps += 1
            if steps > 10**5: capped += 1; break
    ok("CZ every odd n <= 330749 falls below itself under T (so all reach 1 by induction)", capped == 0)
    # the 678 bound: least m admitting 3^m < 2^A <= (3+1/s)^m with s = 330751
    s = 330751
    mstar = None
    for mm in range(1, 5000):
        A = mm * 0  # smallest A with 2^A > 3^m
        A = (3**mm).bit_length()          # 2^A > 3^m >= 2^(A-1)
        if 2**A * s**mm <= (3 * s + 1)**mm:
            mstar = mm; break
    kmin = None
    if mstar:
        # smallest k with (4s)^m <= 2^k (3s+1)^m at m = mstar (the ratio grows with m)
        k = 0; L4 = (4 * s)**mstar; R3 = (3 * s + 1)**mstar
        while not (L4 <= 2**k * R3): k += 1
        kmin = k
    ok("CZ cycle bound: least m with a power of 2 in (3^m,(3+1/s)^m] is m*>1635, forcing k>=679",
       mstar is not None and mstar > 1635 and kmin is not None and kmin >= 679, f"m*={mstar}, k>={kmin}")
    # sqrt(15)/4 inequality, exact: (sqrt(u)+sqrt(v))/2 <= (sqrt15/4) sqrt(x-1), u=(x-2)/2, v=(3x-1)/2
    x = sp.symbols('x', positive=True)
    lhs = (sp.sqrt((x - 2) / 2) + sp.sqrt((3 * x - 1) / 2)) / 2
    rhs = sp.sqrt(15) / 4 * sp.sqrt(x - 1)
    ok("CZ sqrt15/4 inequality equality at x=7", sp.simplify(lhs.subs(x, 7) - rhs.subs(x, 7)) == 0)
    worst = max(float((lhs - rhs).subs(x, sp.Rational(k, 10))) for k in range(20, 2000))
    ok("CZ sqrt15/4 inequality holds on x in [2, 200] (grid; the proof is Cauchy-Schwarz)", worst <= 1e-15, worst)
    # cylinder classes: odd n with given first m exponent word form one class mod 2^(A+1)
    badc = 0
    for m in (1, 2, 3):
        classes = {}
        for n in range(1, 2**15, 2):
            _, w = word_of(n, m)
            A = sum(w)
            if A > 11: continue
            classes.setdefault(tuple(w), set()).add(n % 2**(A + 1))
        badc += sum(1 for w, c in classes.items() if len(c) != 1)
    ok("CZ each exponent word w (A<=11) is realised by exactly one class of odd n mod 2^(A+1)", badc == 0)

# ----------------------------------------------------------------------------- EP
def subset_sums(A):
    S = {0}
    for a in A:
        S |= {s + a for s in S}
    return S

def has_kap(Hset, k, modulus=None):
    H = sorted(Hset)
    if modulus is None:
        Hs = set(H)
        for i, x in enumerate(H):
            for y in H[i + 1:]:
                d = y - x
                if all(x + j * d in Hs for j in range(2, k)): return True
        return False
    R = {h % modulus for h in H}
    for x in R:
        for d in range(1, modulus):
            if all((x + j * d) % modulus in R for j in range(1, k)): return True
    return False

def ep_section():
    D = sorted(subset_sums([1, 7, 8]))
    ok("EP digit set H({1,7,8}) = {0,1,7,8,9,15,16}", D == [0, 1, 7, 8, 9, 15, 16], D)
    ok("EP no nonconstant 4-AP mod 19 inside the digit set", not has_kap(set(D), 4, 19))
    for m in (1, 2, 3):
        A = [19**j * w for j in range(m) for w in (1, 7, 8)]
        H = subset_sums(A)
        ok(f"EP lift m={m}: |H(A_m)| = 7^m and H(A_m) has no nonconstant 4-AP", len(H) == 7**m and not has_kap(H, 4))
    # kappa_m = (8*3^m - 3*2^m)/(12(3^m-2^m)) equals the class-value variance/Q on random blocks
    bad = 0; tested = 0
    while tested < 60:
        m = random.choice([3, 4, 5])
        b = [random.choice([-1, 1]) * random.randint(1, 9) for _ in range(m - 1)]
        b.append(-sum(b))
        if b[-1] == 0: continue
        tested += 1
        vals = [sum(bi * yi for bi, yi in zip(b, y)) for y in itertools.product(range(3), repeat=m) if min(y) == 0]
        mu = Fr(sum(vals), len(vals))
        var = Fr(sum((v - mu)**2 for v in vals), len(vals))
        Q = sum(bi * bi for bi in b)
        kap = Fr(8 * 3**m - 3 * 2**m, 12 * (3**m - 2**m))
        if mu != 0 or var != kap * Q: bad += 1
    ok("EP class-value mean 0 and variance kappa_m * sum b_i^2 on 60 random blocks with nonzero entries", bad == 0 and tested == 60)
    ok("EP kappa_3 = 16/19 and kappa_m <= 16/19 for 3 <= m <= 40",
       Fr(8 * 27 - 24, 12 * 19) == Fr(16, 19) and all(Fr(8 * 3**m - 3 * 2**m, 12 * (3**m - 2**m)) <= Fr(16, 19) for m in range(3, 41)))
    Bs = [1, 4, 5, 17, 21, 22]
    HB = subset_sums(Bs)
    ok("EP B*={1,4,5,17,21,22}: S=70, |H|=38", sum(Bs) == 70 and len(HB) == 38)
    ok("EP H(B*) mod 97 has no nonzero-step 5-AP", not has_kap(HB, 5, 97))
    ok("EP H(B*) mod 93 has no nonzero-step 6-AP", not has_kap(HB, 6, 93))
    ok("EP H(B*) mod 96 does contain a 5-AP (97 is not beaten by 96 for this block)", has_kap(HB, 5, 96))
    Ash = [3, 4, 7, 34, 37, 41, 216, 250, 253, 257]
    HA = subset_sums(Ash)
    marks = [0, 4, 7, 41, 257]
    dists = sorted(b - a for a, b in itertools.combinations(marks, 2))
    ok("EP A# = pairwise distances of (0,4,7,41,257), S=1102<1651=13*127, |H|=291",
       dists == Ash and sum(Ash) == 1102 and 1651 == 13 * 127 and len(HA) == 291)
    ok("EP H(A#) mod 1651 has no nonzero-step 6-AP", not has_kap(HA, 6, 1651))
    ok("EP H(A#) contains the 5-AP 0,257,514,771,1028", all(257 * j in HA for j in range(5)))
    ok("EP 1651^3 < 93^5 and 97 < 5^3... comparisons", 1651**3 < 93**5 and 93**5 < 7**12 and 97**2 < 23**3)
    # composition C = A u R.B, R = 2S(A)+1, preserves 4-admissibility (small instance)
    A = [1, 4, 5]; B = [1, 3]
    R = 2 * sum(A) + 1
    C = A + [R * b for b in B]
    ok("EP composition A u (2S(A)+1)B of 4-admissible sets is 4-admissible; 2S(C)+1 = (2S(A)+1)(2S(B)+1)",
       not has_kap(subset_sums(C), 4) and 2 * sum(C) + 1 == (2 * sum(A) + 1) * (2 * sum(B) + 1))

# ----------------------------------------------------------------------------- YM
def ym_section():
    m = {1: Fr(64, 3), 2: Fr(5834, 39), 3: Fr(336572872, 208845),
         4: Fr(17270702970768271, 341697152160), 5: Fr(1638684)}
    t = {1: Fr(16, 3), 2: Fr(137, 6), 3: Fr(225985217, 1253070),
         4: Fr(110695177857394584026401, 18025447358750832000), 5: Fr(190128)}
    X = sp.symbols('X')
    ell = sum(sp.Rational(m[i] + 4 * t[i]) * X**i for i in range(1, 6))
    dl = sum(sp.Rational(3 * (m[i] * t[j] + m[j] * t[i])) * X**(i + j)
             for i in range(1, 6) for j in range(1, 6) if i + j >= 6)
    Dp = sp.expand((1 - ell)**2 - sp.Rational(8, 3) * dl)
    roots = sp.Poly(Dp, X).intervals(eps=sp.Rational(1, 10**24))
    pos = sorted(iv for (iv, mult) in roots if iv[1] > 0)
    lo, hi = pos[0]
    alpha = (lo + hi) / 2
    ok("YM first positive root alpha_5 of D_5 in (0.0184249535761176166, 0.0184249535761176167)",
       sp.Rational('0.0184249535761176166') < lo and hi < sp.Rational('0.0184249535761176167'),
       sp.N(alpha, 22))
    thr = 1 / (2 * sp.sqrt(alpha))
    ok("YM threshold g^2 >= 1/(2 sqrt(alpha_5)) = 3.68355198398572...", abs(sp.N(thr, 20) - sp.Float('3.6835519839857273044', 20)) < 1e-15, sp.N(thr, 20))
    def d5(xv):
        return sp.Rational(3, 2) * (1 + sp.sqrt(Dp.subs(X, xv))) + sum(sp.Rational(Fr(3, 2) * m[i] - 6 * t[i]) * xv**i for i in range(1, 6))
    v = sp.N(d5(sp.Rational(1, 64)), 15)
    ok("YM d_5(1/64) (g^2 = 4) > 1.9068", v > 1.9068, v)
    ok("YM d_5(0) = 3", d5(0) == 3)
    ok("YM d_5(alpha_5) > 3/2", sp.N(d5(lo), 12) > 1.5, sp.N(d5(lo), 12))
    ok("YM coefficients (3/2)m_i - 6 t_i >= 0, first = 0",
       all(Fr(3, 2) * m[i] - 6 * t[i] >= 0 for i in range(1, 6)) and Fr(3, 2) * m[1] - 6 * t[1] == 0)
    # Casimir lemma on the cube graph: every singlet-admissible spin assignment has sum_f j_f >= 4 j_e
    V = list(itertools.product((0, 1), repeat=3))
    E = [(u, w) for u in V for w in V if u < w and sum(abs(a - b) for a, b in zip(u, w)) == 1]
    inc = {vv: [i for i, (u, w) in enumerate(E) if vv in (u, w)] for vv in V}
    spins = (0, 1, 2)   # twice the spin (j <= 1, exhaustive)
    cnt = 0; bad = 0
    for js in itertools.product(spins, repeat=len(E)):
        good = True
        for vv in V:
            s = [js[i] for i in inc[vv]]
            tot = sum(s)
            if tot % 2 or 2 * max(s) > tot:
                good = False; break
        if not good or not any(js): continue
        cnt += 1
        tot = sum(js)
        if any(tot < 4 * j for j in js): bad += 1
    ok("YM Casimir lemma: on the cube graph every nonzero vertex-singlet spin assignment (j<=1, exhaustive) has sum j_f >= 4 j_e",
       bad == 0, f"{cnt} admissible assignments")
    # face count and the section-27 radius
    good = True
    for L in range(2, 6):
        rng = range(-L, L + 1)
        faces = 0
        for n in itertools.product(rng, repeat=3):
            for i, j in ((0, 1), (0, 2), (1, 2)):
                if n[i] + 1 <= L and n[j] + 1 <= L: faces += 1
        if faces != 12 * L * L * (2 * L + 1): good = False
    ok("YM face count M_L = 12 L^2 (2L+1) for L=2..5 by enumeration; 3/(16 M_L) = 1/(64 L^2 (2L+1))",
       good and Fr(3, 16 * 12 * 4 * 5) == Fr(1, 64 * 4 * 5))
    # S6-5 cubic
    P = lambda a: a[0] * (a[0]**2 - 3 * (a[1]**2 + a[2]**2 + a[3]**2))
    vals = set()
    for a in itertools.product(range(-8, 9), repeat=4):
        if sum(a) % 2 == 0: vals.add(P(a))
    g = 0
    for vv in vals: g = math.gcd(g, vv)
    ok("S6 P(a)=a0(a0^2-3|v|^2) on D4 (|a_i|<=8): gcd of values 2, value 6 not attained, 3|P => 9|P",
       g == 2 and 6 not in vals and -6 not in vals and all(vv % 9 == 0 for vv in vals if vv % 3 == 0))
    a0, a1, a2, a3 = sp.symbols('a0:4')
    # Re((a0 + a1 i + a2 j + a3 k)^3) = a0^3 - 3 a0 |v|^2 : quaternion cube
    def qmul(p, q):
        w1, x1, y1, z1 = p; w2, x2, y2, z2 = q
        return (w1*w2 - x1*x2 - y1*y2 - z1*z2, w1*x2 + x1*w2 + y1*z2 - z1*y2,
                w1*y2 - x1*z2 + y1*w2 + z1*x2, w1*z2 + x1*y2 - y1*x2 + z1*w2)
    qq = (a0, a1, a2, a3)
    cube = qmul(qmul(qq, qq), qq)
    ok("S6 Re(q^3) = a0(a0^2 - 3|v|^2) for a quaternion q", sp.expand(cube[0] - a0 * (a0**2 - 3 * (a1**2 + a2**2 + a3**2))) == 0)
    # NS-04(b) Kasner identities with generic tracefree symmetric B
    b11, b22, b12, b13, b23 = sp.symbols('b11 b22 b12 b13 b23', real=True)
    B = sp.Matrix([[b11, b12, b13], [b12, b22, b23], [b13, b23, -b11 - b22]])
    chi = sp.sqrt(1 + sp.Rational(4, 3) * (B * B).trace())
    Pw = sp.Rational(1, 4) - sp.Rational(3, 4) / chi
    Pp = sp.eye(3) / 4 + (sp.eye(3) / 4 + B) / chi
    ok("NS Kasner: P_w + tr P_perp = 1", sp.simplify(Pw + Pp.trace() - 1) == 0)
    ok("NS Kasner: P_w^2 + tr P_perp^2 = 1", sp.simplify(sp.expand(Pw**2 + (Pp * Pp).trace() - 1)) == 0)
    Binv = sp.simplify((3 * Pp + (Pw - 1) * sp.eye(3)) / (1 - 4 * Pw))
    ok("NS Kasner: inverse B = (3 P_perp + (P_w - 1) I)/(1 - 4 P_w) returns B", sp.simplify(Binv - B) == sp.zeros(3))
    # Keller map F
    x, y, w = sp.symbols('x y w')
    F1 = (1 + x * y)**3 * w + y**2 * (1 + x * y) * (4 + 3 * x * y)
    F2 = y + 3 * x * (1 + x * y)**2 * w + 3 * x * y**2 * (4 + 3 * x * y)
    F3 = 2 * x - 3 * x**2 * y - x**3 * w
    Jd = sp.Matrix([F1, F2, F3]).jacobian([x, y, w]).det()
    pts = [(0, 0, sp.Rational(-1, 4)), (1, sp.Rational(-3, 2), sp.Rational(13, 2)), (-1, sp.Rational(3, 2), sp.Rational(13, 2))]
    imgs = {tuple(sp.simplify(f.subs({x: p[0], y: p[1], w: p[2]})) for f in (F1, F2, F3)) for p in pts}
    ok("JC det DF = -2 and three points map to (-1/4, 0, 0)", sp.expand(Jd) == -2 and imgs == {(sp.Rational(-1, 4), 0, 0)})

if __name__ == "__main__":
    random.seed(20260926)
    for sec in (es_section, cz_section, ep_section, ym_section):
        t1 = time.time(); sec(); print(f"   ({sec.__name__} {time.time() - t1:.1f}s)")
    print("ALL PASS" if not FAIL else f"FAILURES: {FAIL}")
    print(f"total {time.time() - T0:.1f}s")
