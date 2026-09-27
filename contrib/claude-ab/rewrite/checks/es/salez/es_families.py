# Copied unchanged from the working files of referee pass B (an independent Claude instance, 27 September 2026).
# It implements Salez's seven modular equations (arXiv:1406.6307, Proposition 3) with explicit denominators.
"""
es_families.py -- the seven single-identity ("modular equation") families for
4/p = 1/x + 1/y + 1/z, in the normal forms of Salez (arXiv:1406.6307), with the
explicit denominators, plus an enumerator of all family classes whose modulus
divides a given L.

Type II relation (p | y, p | z):  4ABCD = A + B + pC,  x = ABD, y = ACDp, z = BCDp
Type I  relation (p | z only)  :  4ABCD = p(A+B) + C,  x = ACD, y = BCD, z = pABD

 14a  B,C,D const : p = -B/C  (mod 4BCD-1)             A linear
 14b  A,B,E const : E | A+B, p = -E (mod 4AB)           D linear   (classical)
 14c  B,D,E const : p = -E-4B^2 D (mod 4BDE)            A,C linear
 15a  A,B,E const : E | A+B, pE = -1 (mod 4AB)          D linear   (classical)
 15b  B,C,F const : p = -F (mod 4BC), pB+C = 0 (mod F)  A,D linear
 15c  B,D,F const : F | 4B^2 D+1, p = -F (mod 4BD)      A,C linear
 15d  C,D,F const : p = -F (mod 4CD), p^2 = -4C^2 D (mod F)   B linear, A quadratic

Each 'family' below is returned as (tag, params, modulus m, list of residues mod m).
The function denominators(tag, params, p) returns (x,y,z) for any positive p in the class.
"""
from math import gcd
from fractions import Fraction
from itertools import product
import random


def factor(n):
    f = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1
            n //= d
        d += 1 if d == 2 else 2
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f


def divisors_from_fact(f):
    ds = [1]
    for q, e in f.items():
        ds = [d * q ** k for d in ds for k in range(e + 1)]
    return sorted(ds)


def divisors(n):
    return divisors_from_fact(factor(n))


def inv(a, m):
    return pow(a, -1, m)


def denominators(tag, par, p):
    """explicit (x,y,z) for the family 'tag' with constant parameters 'par' at p."""
    if tag == '14a':
        B, C, D = par
        m = 4 * B * C * D - 1
        assert (B + p * C) % m == 0
        A = (B + p * C) // m
        return (A * B * D, A * C * D * p, B * C * D * p)
    if tag == '14b':
        A, B, E = par
        assert (A + B) % E == 0 and (p + E) % (4 * A * B) == 0
        C = (A + B) // E
        D = (p + E) // (4 * A * B)
        return (A * B * D, A * C * D * p, B * C * D * p)
    if tag == '14c':
        B, D, E = par
        assert (p + E) % (4 * B * D) == 0
        A = (p + E) // (4 * B * D)
        assert (A + B) % E == 0
        C = (A + B) // E
        return (A * B * D, A * C * D * p, B * C * D * p)
    if tag == '15a':
        A, B, E = par
        assert (A + B) % E == 0 and (p * E + 1) % (4 * A * B) == 0
        C = (A + B) // E
        D = (p * E + 1) // (4 * A * B)
        return (A * C * D, B * C * D, p * A * B * D)
    if tag == '15b':
        B, C, F = par
        assert (p + F) % (4 * B * C) == 0 and (p * B + C) % F == 0
        D = (p + F) // (4 * B * C)
        A = (p * B + C) // F
        return (A * C * D, B * C * D, p * A * B * D)
    if tag == '15c':
        B, D, F = par
        g = (4 * B * B * D + 1)
        assert g % F == 0
        g //= F
        assert (p * g + 1) % (4 * B * D) == 0
        A = (p * g + 1) // (4 * B * D)
        assert (A + B) % g == 0
        C = (A + B) // g
        return (A * C * D, B * C * D, p * A * B * D)
    if tag == '15d':
        C, D, F = par
        assert (p + F) % (4 * C * D) == 0
        B = (p + F) // (4 * C * D)
        num = p * (p + F) + 4 * C * C * D
        assert num % (4 * C * D * F) == 0
        A = num // (4 * C * D * F)
        return (A * C * D, B * C * D, p * A * B * D)
    raise ValueError(tag)


def check_identity(tag, par, p):
    x, y, z = denominators(tag, par, p)
    return x > 0 and y > 0 and z > 0 and Fraction(1, x) + Fraction(1, y) + Fraction(1, z) == Fraction(4, p)


def sqrt_mod_prime(c, q):
    c %= q
    return [r for r in range(q) if (r * r - c) % q == 0]


def crt_pair(r1, m1, r2, m2):
    g = gcd(m1, m2)
    if (r1 - r2) % g:
        return None
    l = m1 // g * m2
    # solve r = r1 + m1*t = r2 mod m2
    t = ((r2 - r1) // g * inv(m1 // g, m2 // g)) % (m2 // g) if m2 // g > 1 else 0
    return ((r1 + m1 * t) % l, l)


def families_dividing(L, Fmax_15c=None):
    """Enumerate every family class (tag, params, m, residues) with modulus m | L.
    L must be an integer; parameters are the constant parameters of the family."""
    fL = factor(L)
    divL = divisors_from_fact(fL)
    divset = set(divL)
    out = []
    # --- 14a: m | L, m odd, m = 3 mod 4, (m+1)/4 = B*C*D
    for m in divL:
        if m % 2 == 0 or m % 4 != 3:
            continue
        T = (m + 1) // 4
        for B in divisors(T):
            for C in divisors(T // B):
                D = T // B // C
                r = (-B * inv(C, m)) % m
                out.append(('14a', (B, C, D), m, [r]))
    # pairs (A,B) with 4AB | L
    if L % 4 == 0:
        N = L // 4
        for A in divisors(N):
            for B in divisors(N // A):
                m = 4 * A * B
                for E in divisors(A + B):
                    # 14b
                    out.append(('14b', (A, B, E), m, [(-E) % m]))
                    # 15a
                    if gcd(E, m) == 1:
                        out.append(('15a', (A, B, E), m, [(-inv(E, m)) % m]))
        # 14c: 4BDE | L
        for B in divisors(N):
            for D in divisors(N // B):
                for E in divisors(N // B // D):
                    m = 4 * B * D * E
                    out.append(('14c', (B, D, E), m, [(-E - 4 * B * B * D) % m]))
        # 15c: 4BD | L, F | 4B^2D+1
        for B in divisors(N):
            for D in divisors(N // B):
                m = 4 * B * D
                for F in divisors(4 * B * B * D + 1):
                    out.append(('15c', (B, D, F), m, [(-F) % m]))
        # 15b: 4BC F | L, gcd(F, 2BC) = 1
        for B in divisors(N):
            for C in divisors(N // B):
                rest = N // B // C
                for F in divisors(rest):
                    if F % 2 == 0 or gcd(F, B * C) != 1:
                        continue
                    m1 = 4 * B * C
                    r1 = (-F) % m1
                    if F == 1:
                        out.append(('15b', (B, C, F), m1, [r1]))
                        continue
                    r2 = (-C * inv(B, F)) % F
                    rr = crt_pair(r1, m1, r2, F)
                    if rr is not None:
                        out.append(('15b', (B, C, F), rr[1], [rr[0]]))
        # 15d: 4CD F | L, gcd(F, 2CD) = 1, quadratic
        for C in divisors(N):
            for D in divisors(N // C):
                rest = N // C // D
                for F in divisors(rest):
                    if F % 2 == 0 or gcd(F, C * D) != 1:
                        continue
                    m1 = 4 * C * D
                    r1 = (-F) % m1
                    if F == 1:
                        out.append(('15d', (C, D, F), m1, [r1]))
                        continue
                    # solve r^2 = -4C^2 D mod F  (F squarefree here or prime powers: brute force per prime power)
                    fF = factor(F)
                    comp = [(0, 1)]
                    ok = True
                    sols_all = []
                    for q, e in fF.items():
                        qe = q ** e
                        sols = [r for r in range(qe) if (r * r + 4 * C * C * D) % qe == 0]
                        if not sols:
                            ok = False
                            break
                        sols_all.append((sols, qe))
                    if not ok:
                        continue
                    res = [r1]
                    mod = m1
                    for sols, qe in sols_all:
                        new = []
                        for r in res:
                            for s in sols:
                                t = crt_pair(r, mod, s, qe)
                                if t is not None:
                                    new.append(t[0])
                        res = new
                        mod = mod * qe // gcd(mod, qe)
                    if res:
                        out.append(('15d', (C, D, F), mod, sorted(set(res))))
    return out


def selftest(trials=3000, seed=1):
    """verify each family identity on random members of its class."""
    rnd = random.Random(seed)
    fams = families_dividing(4 * 3 * 5 * 7 * 11 * 13 * 9)
    bad = 0
    tested = 0
    by_tag = {}
    for (tag, par, m, rs) in rnd.sample(fams, min(trials, len(fams))):
        for r in rs:
            for k in range(3):
                p = r + m * rnd.randrange(1, 10 ** 6)
                tested += 1
                by_tag[tag] = by_tag.get(tag, 0) + 1
                if not check_identity(tag, par, p):
                    bad += 1
    return tested, bad, by_tag, len(fams)


if __name__ == '__main__':
    t, b, bt, nf = selftest()
    print('families with modulus | 4*3*5*7*11*13*9:', nf)
    print('identity checks:', t, 'failures:', b, 'by tag:', bt)
