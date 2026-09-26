#!/usr/bin/env python3
"""Independent checks of the ES core reduction (ES-01, ES-02, ES-03).

Sources audited (read-only, erdos-straus-foundation @ d20b32e):
  bounded_transport.tex  lem:units (L49-100), E/M count (L118-133), biconditional (L150-174)
  counterexample_sieve/all_shell_no_hit.tex thm:shellwise-no-hit (L79), thm:global-no-hit (L295)
  first_two_shell_sieve.tex thm:r3-factor-sieve (L18), thm:r7-factor-sieve (L95), cor (L214)

All code is my own. Exact integer arithmetic throughout.
"""
import sys, time
from math import gcd
from fractions import Fraction
from sympy import primerange, factorint, divisors

T0 = time.time()
def log(*a):
    print(*a); sys.stdout.flush()

def EM(a, p):
    R = 4 * a - p
    ds = divisors(a * a)
    E = [u for u in ds if (4 * u + 1) % R == 0]
    M = [u for u in ds if (u + a) % R == 0]
    return E, M

# ---------------------------------------------------------------- 0. classical identities
log("== 0. Elementary reductions (RESEARCH_STATE L11-36) ==")
bad = 0
for p in primerange(2, 200000):
    if p % 3 == 2:
        t = (p, (p + 1) // 3, p * (p + 1) // 3)
    elif p % 4 == 3:
        t = ((p + 1) // 4, p * (p + 1) // 2, p * (p + 1) // 2)
    elif p % 24 == 13:
        a = (p + 3) // 4
        t = (a, p * a // 2, p * a)
    else:
        assert p % 24 == 1
        continue
    if Fraction(1, t[0]) + Fraction(1, t[1]) + Fraction(1, t[2]) != Fraction(4, p):
        bad += 1
    if p % 3 == 2:
        assert (p + 1) % 3 == 0
    if p % 4 == 3:
        assert (p + 1) % 4 == 0 and (p * (p + 1)) % 2 == 0
    if p % 24 == 13:
        assert ((p + 3) // 4) % 2 == 0
log("identities fail for", bad, "primes < 2e5 outside 1 mod 24 (expect 0)")

# ---------------------------------------------------------------- 1. brute force per shell
log("\n== 1. lem:units bijection, E/M counts, Phi and inverse (10a), brute force ==")
nshell = 0
for p in primerange(13, 1000):
    if p % 12 != 1:
        continue
    h = (p - 1) // 12
    for a in range(3 * h + 1, 9 * h + 1):
        R, S = 4 * a - p, p * a
        assert gcd(R, S) == 1 and R % 4 == 3 and 3 <= R <= 2 * p - 3
        # brute force ordered (y,z): 1/y+1/z = R/S
        bf = set()
        y = S // R + 1
        while R * y <= 2 * S:  # y <= z
            num = S * y
            den = R * y - S
            if num % den == 0:
                z = num // den
                bf.add((y, z)); bf.add((z, y))
            y += 1
        # W_a and the reconstruction map (eq:reconstruct)
        dS = divisors(S)
        img = {}
        for m in dS:
            for n in dS:
                if gcd(m, n) == 1 and (m + n) % R == 0:
                    k = (m + n) // R
                    yz = ((S // n) * k, (S // m) * k)
                    assert yz not in img
                    img[yz] = (m, n)
                    fr = Fraction(yz[0], yz[1])
                    assert (fr.numerator, fr.denominator) == (m, n)  # inverse = reduced y/z
                    assert Fraction(R * yz[0] - S, S) == fr
        assert set(img) == bf, (p, a)
        E, M = EM(a, p)
        assert len(bf) == 2 * len(E) + len(M)
        assert all(y != z for (y, z) in bf)
        assert len(M) % 2 == 0
        # Phi (10) and its inverse (10a)
        Phi = {}
        for eps, U in ((0, E), (1, M)):
            for u in U:
                g = gcd(a, u); A, B, D = a // g, u // g, g * g // u
                assert g * g % u == 0 and a == A * B * D and u == B * B * D and gcd(A, B) == 1
                num = A + p ** (1 - eps) * B
                assert num % R == 0
                C = num // R
                y0, z0 = p ** eps * A * C * D, p * B * C * D
                sigmas = (0, 1) if eps == 0 else (0,)
                for s in sigmas:
                    w = (y0, z0) if s == 0 else (z0, y0)
                    assert Fraction(1, a) + Fraction(1, w[0]) + Fraction(1, w[1]) == Fraction(4, p)
                    assert w not in Phi
                    Phi[w] = (eps, u, s)
        assert set(Phi) == bf
        for (y, z), tag in Phi.items():
            dy = R * y - S
            i = 0
            t = dy
            while t % p == 0:
                t //= p; i += 1
            assert i in (0, 1, 2)
            inv = {0: (0, a * a // dy, 0), 1: (1, p * a * a // dy, 0), 2: (0, dy // (p * p), 1)}[i]
            assert inv == tag, (p, a, y, z, inv, tag)
        nshell += 1
log("shells checked by brute force (all primes 13<=p<1000, p=1 mod 12, all a in A_p):", nshell, "all assertions passed")

# ---------------------------------------------------------------- 2. min denominator lies in A_p
log("\n== 2. every sorted solution has min denominator in A_p (naive search, p<120) ==")
for p in primerange(13, 120):
    if p % 12 != 1:
        continue
    h = (p - 1) // 12
    mins = set(); cnt = 0
    for x in range(1, 2 * p + 1):
        r = Fraction(4, p) - Fraction(1, x)
        if r <= 0:
            continue
        for y in range(x, 4 * p * p + 1):
            r2 = r - Fraction(1, y)
            if r2 <= 0:
                continue
            if r2.numerator == 1 and r2.denominator >= y:
                mins.add(x); cnt += 1
    ok = all(3 * h + 1 <= x <= 9 * h for x in mins)
    # compare with the shell counts: number of sorted triples with x=a and a<=y<=z
    log(f"p={p}: sorted solutions={cnt}, minimal denominators={sorted(mins)}, all in A_p=[{3*h+1},{9*h}]: {ok}")

# ---------------------------------------------------------------- 3. Q_p>0 and ES(p) for p<10^4
log("\n== 3. Q_p and first occupied shell for all primes p=1 mod 12, p<10^4 ==")
maxfirst = (0, 0); npr = 0; nQ0 = 0
for p in primerange(13, 10000):
    if p % 12 != 1:
        continue
    h = (p - 1) // 12
    Q = Fraction(0); first = None
    for a in range(3 * h + 1, 9 * h + 1):
        E, M = EM(a, p)
        q = len(E) + Fraction(len(M), 2)
        if q and first is None:
            first = a - 3 * h  # shell index from the bottom
        Q += q
    npr += 1
    if Q == 0:
        nQ0 += 1
    assert Q.denominator == 1
    if first > maxfirst[0]:
        maxfirst = (first, p)
log(f"primes checked: {npr}; Q_p=0 for {nQ0} of them; largest index (a-3h) of first occupied shell: {maxfirst}")

# ---------------------------------------------------------------- 4. residual-3 and residual-7 sieves
log("\n== 4. residual-3 and residual-7 factor sieves, all primes p=1 mod 12 < 10^6 ==")
lam = {1: 0, 3: 1, 2: 2, 6: 3, 4: 4, 5: 5}
n = 0; surv = []; r3fail = r7fail = 0; r3counts_ok = r7counts_ok = 0
for p in primerange(13, 10 ** 6):
    if p % 12 != 1:
        continue
    n += 1
    h = (p - 1) // 12
    # --- R3
    a = 3 * h + 1
    f = factorint(a)
    E, M = EM(a, p)
    P1 = 1; P2 = 1
    for l, v in f.items():
        if l % 3 == 1: P1 *= 2 * v + 1
        elif l % 3 == 2: P2 *= 2 * v + 1
        else: raise AssertionError
    assert set(E) == set(M) == {u for u in divisors(a * a) if u % 3 == 2}
    assert len(E) == P1 * (P2 - 1) // 2
    assert Fraction(len(E)) + Fraction(len(M), 2) == Fraction(3 * P1 * (P2 - 1), 4)
    has2 = any(l % 3 == 2 for l in f)
    assert (len(E) > 0) == has2
    if has2:
        l = min(x for x in f if x % 3 == 2)
        D = a // l; C0 = (1 + p * l) // 3; C1 = (1 + l) // 3
        for t in ((a, C0 * D, p * l * C0 * D), (a, p * C1 * D, p * l * C1 * D)):
            assert sum(Fraction(1, x) for x in t) == Fraction(4, p)
    else:
        r3fail += 1
    r3counts_ok += 1
    # --- R7
    a7 = 3 * h + 2
    f7 = factorint(a7)
    assert a7 % 7 != 0
    E7, M7 = EM(a7, p)
    n3 = sum(v for l, v in f7.items() if l % 7 == 3)
    n24 = sum(v for l, v in f7.items() if l % 7 in (2, 4))
    pred = any(l % 7 in (5, 6) for l in f7) or n3 >= 3 or (n3 >= 1 and n24 >= 1)
    assert (len(E7) + len(M7) > 0) == pred, p
    # group-ring coefficients
    coeff = [0] * 6; coeff[0] = 1
    for l, v in f7.items():
        new = [0] * 6
        for r in range(6):
            if coeff[r]:
                for e in range(2 * v + 1):
                    new[(r + lam[l % 7] * e) % 6] += coeff[r]
        coeff = new
    b = sum(lam[l % 7] * v for l, v in f7.items()) % 6
    assert len(E7) == coeff[5] and len(M7) == coeff[(b + 3) % 6]
    # table witnesses
    tbl = []
    for l in f7:
        if l % 7 == 5: tbl.append(('E', l))
        if l % 7 == 6: tbl.append(('M', a7 * l))
    threes = [l for l, v in f7.items() if l % 7 == 3 for _ in range(v)]
    if len(threes) >= 3:
        tbl.append(('M', a7 * threes[0] * threes[1] * threes[2]))
    for l in f7:
        for t in f7:
            if l % 7 == 3 and t % 7 == 2: tbl.append(('M', a7 * l * t))
            if l % 7 == 3 and t % 7 == 4: tbl.append(('M', a7 * l // t))
    for ch, u in tbl:
        assert (a7 * a7) % u == 0
        assert (u in E7) if ch == 'E' else (u in M7)
    if not pred:
        r7fail += 1
    r7counts_ok += 1
    if not has2 and not pred:
        surv.append(p)
log(f"primes p=1 mod 12 below 10^6: {n}; R3 fails: {r3fail}; R7 fails: {r7fail}; both fail (two-shell survivors): {len(surv)}")
log("all survivors are 1 mod 24:", all(q % 24 == 1 for q in surv), "; first ten:", surv[:10])
log("R3 always hits for p=13 mod 24 (a=3h+1 even):",
    all(((p - 1) // 12 * 3 + 1) % 2 == 0 for p in primerange(13, 10 ** 5) if p % 24 == 13))

# worked examples from the source
E, M = EM(4, 13); log("p=13,a=4: E,M =", E, M, "(source: {2,8},{2,8})")
E, M = EM(95, 373); log("p=373,a=95: E,M =", E, M, "(source: {5,19}, empty)")
E, M = EM(12, 37); log("p=37,a=12: E,M =", E, M, "(source: E={8}, M empty)")
log("time %.1fs" % (time.time() - T0))
