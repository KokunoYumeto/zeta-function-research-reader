#!/usr/bin/env python3
"""Checks for the formal-logarithm findings (reader Thm 2.3, Cor 2.4, Prop 2.6).

F1  Divisor-minimal form of Thm 2.3: if every proper M-divisor of n factors uniquely,
    then r_n = 1 - j + eps (j = #factorizations of n, eps = sum 1/k over pure powers u^k).
    In particular r_n <= -1/6 at every divisor-minimal non-factorial n, not only at the least one.
F2  For congruence monoids M_H (H proper) the first negative coefficient is <= -1/2
    (note 11_, Lemma 11.2 step 7), dropped by the reader.

Exact rational arithmetic. r_n computed by the derivation recursion with the completely
additive weight Omega(n) (number of prime factors with multiplicity):
    sum_{ab=n} Omega(a) r_a d_b = Omega(n) d_n.
"""
from fractions import Fraction
from math import gcd
import itertools, sys

def omega_table(N):
    om = [0]*(N+1)
    spf = list(range(N+1))
    for p in range(2, int(N**0.5)+1):
        if spf[p] == p:
            for m in range(p*p, N+1, p):
                if spf[m] == m:
                    spf[m] = p
    for n in range(2, N+1):
        om[n] = om[n//spf[n]] + 1
    return om

def analyse(member, N, name, om):
    M = [n for n in range(1, N+1) if member(n)]
    Mset = set(M)
    # atoms
    atoms = []
    for n in M:
        if n == 1: continue
        isatom = True
        for d in range(2, int(n**0.5)+1):
            if n % d == 0 and d in Mset and (n//d) in Mset:
                isatom = False; break
        if isatom: atoms.append(n)
    # number of factorizations (multisets of atoms) by DP over atoms in increasing order
    fac = {1: 1}
    nf = [0]*(N+1); nf[1] = 1
    for a in atoms:
        for n in range(a, N+1):
            if n % a == 0 and nf[n//a]:
                nf[n] += nf[n//a]
    # eps(n): sum of 1/k over pure-power factorizations u^k (u atom, k>=1)
    atomset = set(atoms)
    eps = [Fraction(0)]*(N+1)
    for u in atoms:
        k, v = 1, u
        while v <= N:
            eps[v] += Fraction(1, k)
            k += 1; v *= u
    # formal log coefficients
    d = [0]*(N+1)
    for n in M: d[n] = 1
    r = [Fraction(0)]*(N+1)
    # divisors lists restricted to M
    divs = [[] for _ in range(N+1)]
    for a in M:
        if a == 1: continue
        for m in range(a, N+1, a):
            if d[m] and d[m//a]:
                divs[m].append(a)
    for n in M:
        if n == 1: continue
        s = Fraction(0)
        for a in divs[n]:
            if a != n:
                s += om[a]*r[a]*d[n//a]
        r[n] = d[n] - s/om[n]
    # classify
    nonUF = [n for n in M if n > 1 and nf[n] >= 2]
    def proper_Mdivisors(n):
        return [a for a in divs[n] if a != n]
    divmin = [n for n in nonUF if all(nf[a] == 1 for a in proper_Mdivisors(n))]
    # F1: formula at divisor-minimal elements
    bad = [n for n in divmin if r[n] != 1 - nf[n] + eps[n]]
    over = [n for n in divmin if r[n] > Fraction(-1, 6)]
    # elements all of whose M-divisors (incl. n) are UF: r_n in {0} U {1/k}
    allUF = [n for n in M if n > 1 and nf[n] == 1 and all(nf[a] == 1 for a in proper_Mdivisors(n))]
    badUF = [n for n in allUF if r[n] != eps[n]]
    neg = [n for n in M if r[n] < 0]
    first = min(nonUF) if nonUF else None
    print(f"--- {name}  (N = {N})")
    print(f"  atoms up to N: {len(atoms)}; non-UF elements: {len(nonUF)}; divisor-minimal non-UF: {len(divmin)}")
    print(f"  least non-UF element n0 = {first}, r_n0 = {r[first] if first else None}")
    print(f"  F1 formula r_n = 1 - j + eps fails at {len(bad)} divisor-minimal elements; r_n > -1/6 at {len(over)}")
    print(f"  (a') r_n = eps_n at all {len(allUF)} elements whose M-divisors all factor uniquely: failures {len(badUF)}")
    print(f"  negative coefficients up to N: {len(neg)}; of these divisor-minimal: {len(set(neg)&set(divmin))}; divisor-minimal elements with r_n<0: {sum(1 for n in divmin if r[n]<0)}/{len(divmin)}")
    print(f"  first few divisor-minimal non-UF: {[(n, nf[n], str(r[n])) for n in divmin[:8]]}")
    return dict(bad=len(bad), over=len(over), badUF=len(badUF), n0=first, r0=r[first] if first else None,
                divmin=len(divmin), neg=len(neg))

om = omega_table(70000)
res = {}
# Hilbert monoid {n = 1 mod 4}
res['hilbert'] = analyse(lambda n: n % 4 == 1, 20000, "M = {n = 1 mod 4} (Hilbert monoid)", om)
# even sheet monoid q=5
res['S5'] = analyse(lambda n: n % 5 in (1, 4), 20000, "M = {n = +-1 mod 5} (even sheet a=1/5)", om)
# one-sided q=5, q=7 (larger N needed for n0)
res['M5'] = analyse(lambda n: n % 5 == 1, 30000, "M = {n = 1 mod 5}", om)
res['S7'] = analyse(lambda n: n % 7 in (1, 6), 20000, "M = {n = +-1 mod 7}", om)
# <4,8> and <8,32> (numerical semigroups <2,3>, <3,5> in exponent)
def gen_monoid(gens, N):
    S = {1}
    frontier = [1]
    while frontier:
        new = []
        for x in frontier:
            for g in gens:
                y = x*g
                if y <= N and y not in S:
                    S.add(y); new.append(y)
        frontier = new
    return S
for gens in [(4, 8), (8, 32), (4, 6, 9), (9, 27), (6, 10, 15)]:
    S = gen_monoid(gens, 2**16)
    res[str(gens)] = analyse(lambda n, S=S: n in S, 2**16 if max(gens) < 30 else 60000, f"M = <{','.join(map(str,gens))}>", om)

# F2: congruence monoids, first negative coefficient <= -1/2, all subgroups H of (Z/q)^x, q <= 16
def subgroups(q):
    G = [a for a in range(1, q) if gcd(a, q) == 1]
    subs = set()
    for k in range(1, 3):
        for gens in itertools.combinations(G, k):
            H = {1}
            changed = True
            while changed:
                changed = False
                for h in list(H):
                    for g in gens:
                        x = (h*g) % q
                        if x not in H:
                            H.add(x); changed = True
            subs.add(frozenset(H))
    return G, subs
print("\n--- F2: congruence monoids M_H, H proper, q <= 16: first negative coefficient")
worst = Fraction(-100)
cases = 0
for q in range(3, 17):
    G, subs = subgroups(q)
    for H in subs:
        if len(H) == len(G):
            continue
        N = 25000
        member = lambda n, H=H, q=q: gcd(n, q) == 1 and (n % q) in H
        Mlist = [n for n in range(1, N+1) if member(n)]
        d = [0]*(N+1)
        for n in Mlist: d[n] = 1
        r = [Fraction(0)]*(N+1)
        firstneg = None
        for n in Mlist:
            if n == 1: continue
            s = Fraction(0)
            # divisors a of n in M, a<n, with n/a in M
            a = 2
            while a*a <= n:
                if n % a == 0:
                    b = n//a
                    if d[a] and d[b]:
                        s += om[a]*r[a] + (om[b]*r[b] if b != a else 0)
                a += 1
            r[n] = d[n] - s/om[n]
            if r[n] < 0:
                firstneg = (n, r[n]); break
        if firstneg is None:
            print(f"  q={q} H={sorted(H)}: no negative coefficient up to {N}")
            continue
        cases += 1
        worst = max(worst, firstneg[1])
        if firstneg[1] > Fraction(-1, 2):
            print(f"  VIOLATION q={q} H={sorted(H)}: {firstneg}")
print(f"  {cases} proper (q,H) with a negative coefficient below 25000; largest first negative value = {worst} (<= -1/2 expected)")

ok = all(v['bad'] == 0 and v['over'] == 0 and v['badUF'] == 0 for v in res.values()) and worst <= Fraction(-1, 2)
print("\nALL CHECKS PASS" if ok else "\nSOME CHECK FAILED")
