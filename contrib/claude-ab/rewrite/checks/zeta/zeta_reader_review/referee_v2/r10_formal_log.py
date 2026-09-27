#!/usr/bin/env python3
"""Referee v2, script r10.  Thm 2.3 and Cor 2.4 at every 'divisor-minimal' element (version 2).

For a multiplicative monoid M of positive integers, r_n = sum_k (-1)^{k+1} T_k(n)/k, T_k(n) = #ordered k-tuples
in (M \ {1})^k with product n (exact Fractions).  At every n in M whose proper M-divisors (1 < d < n, d, n/d in M)
have exactly one factorization:  r_n = eps if n has one factorization (eps = 1/k if n = u^k, else 0), and
r_n = 1 - j + eps <= -1/6 if n has j >= 2 factorizations (eps = sum 1/k over pure-power factorizations).
In congruence monoids M_H (H != G) additionally r_n <= -1/2 (at most one pure-power factorization).
Cor 2.4: at such N with r_N > -1/2: exactly two factorizations a^{j1} = b^{j2}, gcd(j1, j2) = 1, N = c^{j1 j2}.
Monoids: {1 mod 4} (Hilbert), {+-1 mod 5}, {1 mod 5}, {1 mod 7}, <4,6,9>, <4,8>, <9,27>, <8,32> (the last three
via exponents).  Also r at 3*7*11*19 in the Hilbert monoid (-2) and the least element with two factorizations.
"""
from fractions import Fraction as Fr
from math import gcd, isqrt
from functools import lru_cache
ok_all = True
def rep(name, cond, info=""):
    global ok_all
    ok_all &= bool(cond); print(("[PASS] " if cond else "[FAIL] ") + name + ("" if not info else ": " + str(info)))

def analyse(member, LIM, congruence):
    Ms = [n for n in range(2, LIM + 1) if member(n)]
    Mset = set(Ms)
    pdiv = {}
    for n in Ms:
        ds = []
        for d in range(2, isqrt(n) + 1):
            if n % d == 0:
                e = n // d
                if d in Mset and e in Mset:
                    ds.append(d)
                    if e != d: ds.append(e)
        pdiv[n] = sorted(ds)
    atoms = [n for n in Ms if not pdiv[n]]
    aset = set(atoms)
    fact = {1: {()}}
    for n in Ms:
        F = set()
        if n in aset: F.add((n,))
        for d in pdiv[n]:
            if d in aset:
                for f in fact[n // d]:
                    F.add(tuple(sorted(f + (d,))))
        fact[n] = F
    @lru_cache(maxsize=None)
    def T(k, n):
        if k == 1: return 1
        return sum(T(k - 1, n // d) for d in pdiv[n])
    def r(n):
        tot = Fr(0); k = 1
        while True:
            t = T(k, n)
            if t == 0 and k > 1: break
            tot += Fr((-1)**(k + 1), k) * t; k += 1
            if k > 64: break
        return tot
    tested = bad = negs = cong_bad = cor_bad = cor_n = 0; first_two = None; first_neg = None
    for n in Ms:
        rn = r(n)
        if rn < 0 and first_neg is None: first_neg = n
        if len(fact[n]) >= 2 and first_two is None: first_two = n
        if all(len(fact[d]) == 1 for d in pdiv[n]):
            j = len(fact[n]); tested += 1
            eps = sum(Fr(1, len(f)) for f in fact[n] if len(set(f)) == 1)
            exp = eps if j == 1 else 1 - j + eps
            if rn != exp or (j >= 2 and rn > Fr(-1, 6)): bad += 1
            if j >= 2:
                negs += 1
                if congruence and rn > Fr(-1, 2): cong_bad += 1
                if rn > Fr(-1, 2):
                    cor_n += 1
                    pp = [f for f in fact[n] if len(set(f)) == 1]
                    if not (j == 2 and len(pp) == 2 and gcd(len(pp[0]), len(pp[1])) == 1): cor_bad += 1
    return dict(elements=len(Ms), tested=tested, bad=bad, negs=negs, cong_bad=cong_bad, cor_n=cor_n, cor_bad=cor_bad,
                first_two=first_two, first_neg=first_neg, r=r, fact=fact)

cases = [("{1 mod 4}", lambda n: n % 4 == 1, 6000, True),
         ("{+-1 mod 5}", lambda n: n % 5 in (1, 4), 5000, True),
         ("{1 mod 5}", lambda n: n % 5 == 1, 8000, True),
         ("{1 mod 7}", lambda n: n % 7 == 1, 8000, True),
         ("<4,6,9> = {2^a 3^b : a+b even}", None, 20000, False)]
def m469(n):
    a = b = 0
    while n % 2 == 0: n //= 2; a += 1
    while n % 3 == 0: n //= 3; b += 1
    return n == 1 and (a + b) % 2 == 0 and a + b > 0
res = {}
for name, mem, LIM, cong in cases:
    R = analyse(mem if mem else m469, LIM, cong)
    res[name] = R
    rep(f"monoid {name} (n <= {LIM}): formula at every divisor-minimal element; first negative = least element with 2 factorizations"
        + ("; value <= -1/2" if cong else ""),
        R["bad"] == 0 and R["cong_bad"] == 0 and R["cor_bad"] == 0 and R["first_neg"] == R["first_two"],
        f"{R['elements']} elements, {R['tested']} divisor-minimal, {R['negs']} with j >= 2, least with two factorizations {R['first_two']}, Cor 2.4 cases {R['cor_n']}")
H = res["{1 mod 4}"]
n0 = 3 * 7 * 11 * 19
rep("Hilbert monoid: r_{3*7*11*19} = -2 (three factorizations into products of two primes, no pure power)",
    H["r"](n0) == -2 and len(H["fact"][n0]) == 3, f"r = {H['r'](n0)}, factorizations {sorted(H['fact'][n0])}")

# exponent monoids <c^u, c^v>: n = c^e with e in uN + vN; work additively in e
def exp_monoid(u, v, EMAX):
    elems = sorted({a * u + b * v for a in range(EMAX // u + 1) for b in range(EMAX // v + 1) if 0 < a * u + b * v <= EMAX})
    S = set(elems)
    @lru_cache(maxsize=None)
    def T(k, e):
        if k == 1: return 1 if e in S else 0
        return sum(T(k - 1, e - d) for d in elems if d < e and (e - d) in S)
    def r(e):
        return sum(Fr((-1)**(k + 1), k) * T(k, e) for k in range(1, e + 1))
    first = min(e for e in elems if r(e) < 0)
    return first, r(first)
out = {}
for (u, v) in ((2, 3), (3, 4), (3, 5), (2, 5)):
    out[(u, v)] = exp_monoid(u, v, u * v + 2)
rep("Cor 2.4 converse: in <c^u, c^v> the first negative coefficient is at c^{uv} with value -1 + 1/u + 1/v",
    all(out[k][0] == k[0] * k[1] and out[k][1] == -1 + Fr(1, k[0]) + Fr(1, k[1]) for k in out),
    {f"<c^{k[0]},c^{k[1]}>": (f"c^{out[k][0]}", str(out[k][1])) for k in out})
print("ALL CHECKS PASS" if ok_all else "SOME CHECKS FAILED")
