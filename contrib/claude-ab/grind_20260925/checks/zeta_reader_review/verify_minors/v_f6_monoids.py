#!/usr/bin/env python3
"""F6 verification (independent code; does not import the review's scripts).

(1) Congruence monoids M_H, H a proper subgroup of (Z/q)^x, q <= 16: exact formal-log coefficients
    r_n from the derivation recursion with the completely additive weight W = Omega:
        r_n W(n) = d_n W(n) - sum_{m in M, 1<m<n, n/m in M} r_m W(m)      (d = indicator of M).
    Report the first negative coefficient and check that it is <= -1/2 (the claim of 11_ step 7).
    Also, at every element n with j >= 2 factorizations whose proper M-divisors all factor uniquely,
    compare r_n with 1 - j + eps and check r_n <= -1/2 and that at most one factorization is a pure
    power (this uses the F4 formula, verified elsewhere; here it is only a numerical cross-check).
(2) The pigeonhole construction without Dirichlet: two primes p != r in one non-identity coset of
    order d give atoms A_j = p^(d-j) r^j with A_0 A_2 = A_1^2.
(3) <4,8>: zeros of 1 - x + x^2 lie on |x| = 1 (Re s = 0); absolute convergence iff Re s > 0.
"""
from fractions import Fraction
from math import gcd
import cmath, math
import sympy

def omega_table(N):
    spf = list(range(N + 1))
    for p in range(2, int(N ** 0.5) + 1):
        if spf[p] == p:
            for m in range(p * p, N + 1, p):
                if spf[m] == m:
                    spf[m] = p
    Om = [0] * (N + 1)
    for n in range(2, N + 1):
        Om[n] = Om[n // spf[n]] + 1
    return Om

def all_subgroups(q):
    G = [a for a in range(1, q) if gcd(a, q) == 1]
    subs = set()
    for a in G:
        for b in G:
            for c in G:
                H, frontier = {1}, [1]
                while frontier:
                    x = frontier.pop()
                    for g in (a, b, c):
                        y = (x * g) % q
                        if y not in H:
                            H.add(y); frontier.append(y)
                subs.add(frozenset(H))
    return G, sorted(subs, key=lambda h: (len(h), sorted(h)))

def analyse(q, H, N, Om):
    inM = [False] * (N + 1)
    M = []
    for n in range(1, N + 1):
        if gcd(n, q) == 1 and (n % q) in H:
            inM[n] = True; M.append(n)
    mdivs = [[] for _ in range(N + 1)]   # proper M-divisors m (1<m<n, n/m in M)
    for m in M[1:]:
        for k in M[1:]:
            if m * k > N: break
            mdivs[m * k].append(m)
    r = [Fraction(0)] * (N + 1)
    for n in M[1:]:
        s = Fraction(Om[n])
        for m in mdivs[n]:
            s -= r[m] * Om[m]
        r[n] = s / Om[n]
    atoms = [n for n in M[1:] if not mdivs[n]]
    F = [0] * (N + 1); F[1] = 1                # number of factorizations (coin-change DP)
    for a in atoms:
        for n in range(a, N + 1):
            if inM[n] and n % a == 0 and F[n // a]:
                F[n] += F[n // a]
    pp = {}
    for a in atoms:
        x, k = a * a, 2
        while x <= N:
            pp.setdefault(x, []).append((a, k)); x *= a; k += 1
    first = next(((n, r[n]) for n in M[1:] if r[n] < 0), None)
    checked = fails = 0
    rmax = None
    for n in M[1:]:
        if F[n] >= 2 and all(F[m] == 1 for m in mdivs[n]):
            eps = sum(Fraction(1, k) for (_, k) in pp.get(n, []))
            checked += 1
            if r[n] != 1 - F[n] + eps or r[n] > Fraction(-1, 2) or len(pp.get(n, [])) > 1:
                fails += 1
            rmax = r[n] if rmax is None else max(rmax, r[n])
    return first, checked, fails, rmax

def main():
    N = 6000
    Om = omega_table(N)
    cases, worst, total_fail = 0, None, 0
    print("(1) proper congruence monoids M_H, q <= 16, n <= %d" % N)
    for q in range(3, 17):
        G, subs = all_subgroups(q)
        for H in subs:
            if len(H) == len(G):
                continue
            first, checked, fails, rmax = analyse(q, H, N, Om)
            if first is None:
                print("  q=%2d H=%s: no negative coefficient below %d" % (q, sorted(H), N)); continue
            cases += 1
            bad = (first[1] > Fraction(-1, 2)) + fails
            total_fail += bad
            worst = first[1] if worst is None else max(worst, first[1])
            print("  q=%2d H=%-22s first negative r_%-5d = %-5s | divisor-minimal non-factorial elements: %4d, max r = %s, failures %d"
                  % (q, sorted(H), first[0], first[1], checked, rmax, bad))
    print("  cases with a negative coefficient below N:", cases, "; largest first-negative value:", worst, "; failures:", total_fail)
    assert total_fail == 0 and worst == Fraction(-1, 2)

    print("(2) pigeonhole construction (no Dirichlet)")
    for (q, H) in [(5, {1, 4}), (7, {1}), (7, {1, 2, 4}), (8, {1, 7}), (13, {1, 3, 9}), (16, {1, 15})]:
        cos = {}
        for p in sympy.primerange(2, 500):
            if gcd(p, q) == 1 and (p % q) not in H:
                key = min((p * h) % q for h in H)
                cos.setdefault(key, []).append(p)
        key, plist = next((k, v) for k, v in sorted(cos.items()) if len(v) >= 2)
        p, rr = plist[0], plist[1]
        d, x = 1, p % q
        while x not in H:
            x = (x * p) % q; d += 1
        A = [p ** (d - j) * rr ** j for j in range(d + 1)]
        in_M = all(a % q in H for a in A)
        atoms_ok = all(((p ** u * rr ** v) % q) not in H
                       for j in range(d + 1) for u in range(d - j + 1) for v in range(j + 1) if 0 < u + v < d)
        rel = A[0] * A[2] == A[1] ** 2
        print("  q=%2d H=%-12s p=%d, r=%d, coset order d=%d: A_j in M_H %s, atoms %s, A0*A2 == A1^2 %s"
              % (q, sorted(H), p, rr, d, in_M, atoms_ok, rel))
        assert in_M and atoms_ok and rel

    print("(3) <4,8>")
    for x in (cmath.exp(1j * math.pi / 3), cmath.exp(-1j * math.pi / 3)):
        print("  root x=%.6f%+.6fi of 1-x+x^2: |x| = %.15f, residual %.1e" % (x.real, x.imag, abs(x), abs(1 - x + x * x)))
    print("  |x| = 1 <=> Re s = 0; 1 + sum_{e>=2} x^e converges absolutely iff |x| < 1 <=> Re s > 0")
    print("ALL F6 CHECKS PASS")

if __name__ == "__main__":
    main()
