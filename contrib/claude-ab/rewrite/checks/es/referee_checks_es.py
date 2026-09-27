#!/usr/bin/env python3
"""Referee checks (independent of the author's and first-pass scripts) for note 43 and ES items in 47.
Exact integer arithmetic; sympy only for factorisation and primality."""
import math, itertools, time
from fractions import Fraction as Fr
import sympy as sp

T0 = time.time()
def out(*a):
    print(*a, flush=True)

# ---------------------------------------------------------------- ES-09: matrices, orbits, genera, incl. even D
A1 = sp.Matrix([[1,0,0,0],[6,0,1,0],[-6,-1,-1,0],[-2,1,0,1]])
A2 = sp.Matrix([[1,0,0,0],[0,0,-1,0],[-6,1,0,0],[3,0,1,1]])
Ai = sp.Matrix([[1,0,0,0],[0,1,0,0],[0,1,1,0],[-1,0,0,1]])
I4 = sp.eye(4)
out("ES-09 A1^3=I:", A1**3 == I4, " A2^4=I:", A2**4 == I4, " A1*A2*Ainf=I:", A1*A2*Ai == I4)

def perms(D):
    """the three affine permutations on (Z/D)^3 as given in core.tex eq:affine"""
    pts = [(x, y, z) for x in range(D) for y in range(D) for z in range(D)]
    idx = {p: i for i, p in enumerate(pts)}
    a1 = [idx[((6 + y) % D, (-6 - x - y) % D, (z - 2 + x) % D)] for (x, y, z) in pts]
    a2 = [idx[((-y) % D, (x - 6) % D, (z + 3 + y) % D)] for (x, y, z) in pts]
    ai = [idx[(x % D, (y + x) % D, (z - 1) % D)] for (x, y, z) in pts]
    return pts, a1, a2, ai

def orbits(n, gens):
    seen = [-1] * n; orbs = []
    for s in range(n):
        if seen[s] >= 0: continue
        k = len(orbs); stack = [s]; seen[s] = k; comp = [s]
        while stack:
            u = stack.pop()
            for g in gens:
                v = g[u]
                if seen[v] < 0:
                    seen[v] = k; stack.append(v); comp.append(v)
        orbs.append(comp)
    return orbs

def cycles_on(perm, comp):
    cs = set(comp); seen = set(); c = 0
    for s in comp:
        if s in seen: continue
        c += 1; u = s
        while u not in seen:
            seen.add(u); u = perm[u]
    return c

def check_relation(D, a1, a2, ai):
    # composed right to left: a1 a2 ainf = id pointwise ?  test both compositions
    n = len(a1)
    r1 = all(a1[a2[ai[i]]] == i for i in range(n))
    r2 = all(ai[a2[a1[i]]] == i for i in range(n))
    return r1 or r2

for D in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15]:
    pts, a1, a2, ai = perms(D)
    orbs = orbits(len(pts), [a1, a2, ai])
    sizes = sorted(len(o) for o in orbs)
    genera = []
    for o in orbs:
        n = len(o)
        c1 = cycles_on(a1, o); c2 = cycles_on(a2, o); ci = cycles_on(ai, o)
        chi = c1 + c2 + ci - n            # 2 - 2g
        genera.append(Fr(2 - chi, 2))
    fg = Fr(5*D**3 - 12*D**2 - 17*D + 24, 24)
    f0 = Fr(5*D**3 - 12*D**2 - 81*D + 216, 216)
    f1 = Fr(5*D**3 - 12*D**2 - 9*D + 27, 27)
    formula = [fg] if D % 3 else sorted([f0, f1])
    out(f"D={D:2d}: relation {check_relation(D,a1,a2,ai)}, orbit sizes {sizes}, genera {sorted(genera)}, "
        f"formula {'(g)' if D%3 else '(g0,g1)'} {[str(f) for f in formula]}, "
        f"transitive={len(orbs)==1}, match={sorted(genera)==formula}")

# ---------------------------------------------------------------- Theorem 43.1 summary-table wording:
# are the pairs counted by 2|E_a|+|M_a| all solutions whose LEAST denominator is a?  Find counterexamples.
def divisors_sq(a):
    ds = [1]
    for q, e in sp.factorint(a).items():
        ds = [d * q**k for d in ds for k in range(2*e + 1)]
    return ds

def pairs(p, a):
    R = 4*a - p; S = p*a
    res = []
    for d in divisors_sq(p*a):   # divisors of S^2 = (pa)^2 via divisors of (pa)^2
        pass
    return res

def solutions_with_a(p, a):
    R = 4*a - p; S = p*a
    sols = []
    S2 = S*S
    for d in sp.divisors(S2):
        if (d + S) % R == 0:
            d2 = S2 // d
            if (d2 + S) % R == 0:
                y = (d + S)//R; z = (d2 + S)//R
                sols.append((y, z))
    return sols

found = []
for p in sp.primerange(13, 400):
    if p % 12 != 1: continue
    h = (p - 1)//12
    for a in range(3*h + 1, 9*h + 1):
        for (y, z) in solutions_with_a(p, a):
            assert Fr(1, a) + Fr(1, y) + Fr(1, z) == Fr(4, p)
            if min(y, z) < a:
                found.append((p, a, y, z))
    if len(found) > 3: break
out("Summary-table check (43 sec.0): solutions counted in shell a whose least denominator is < a:",
    found[:4], f"({len(found)} found by p={p})")

# ---------------------------------------------------------------- counts quoted in 43
cnt_1e6 = sum(1 for p in sp.primerange(2, 10**6) if p % 12 == 1)
out("primes p=1 mod 12 below 1e6:", cnt_1e6, "(note: 19,564)")
cnt_2e5 = sum(1 for p in sp.primerange(2, 2*10**5) if p % 12 == 1)
out("primes p=1 mod 12 below 2e5:", cnt_2e5, "(note: 4,472)")
pr700 = [p for p in sp.primerange(2, 700) if p % 12 == 1]
out("primes p=1 mod 12 below 700:", len(pr700), " shells:", sum(6*((p-1)//12) for p in pr700), "(note: 27 primes, 4,398 shells)")

# both first shells empty, via the proved predicates (independent of E/M enumeration) and via direct E/M
def r3_occupied(a):
    return any(q % 3 == 2 for q in sp.factorint(a))
def r7_occupied(a):
    f = sp.factorint(a)
    n3 = sum(e for q, e in f.items() if q % 7 == 3)
    n24 = sum(e for q, e in f.items() if q % 7 in (2, 4))
    return any(q % 7 in (5, 6) for q in f) or n3 >= 3 or (n3 >= 1 and n24 >= 1)
both_empty = [p for p in sp.primerange(13, 10**6) if p % 12 == 1
              and not r3_occupied((p + 3)//4) and not r7_occupied((p + 7)//4)]
out("primes p=1 mod 12 < 1e6 with both shells empty (predicates):", len(both_empty), " first:", both_empty[:3],
    " all 1 mod 24:", all(p % 24 == 1 for p in both_empty))
# direct E/M check on the first 40 of them
def EM(p, a):
    R = 4*a - p; D = divisors_sq(a)
    return [u for u in D if (4*u + 1) % R == 0], [u for u in D if (u + a) % R == 0]
ok_direct = all(not any(EM(p, (p+3)//4)) and not any(EM(p, (p+7)//4)) for p in both_empty[:40])
out("  direct E/M emptiness confirmed on the first 40:", ok_direct)

# ---------------------------------------------------------------- item-level arithmetic quoted in 43
out("item 2 witness (636, 5611746, 70588) at 2521:", Fr(1,636) + Fr(1,5611746) + Fr(1,70588) == Fr(4,2521))
out("item 26: 4*16849-67369 =", 4*16849 - 67369, " 4*16850-67369 =", 4*16850 - 67369, " 7*29*83 =", 7*29*83,
    " 67369 prime:", sp.isprime(67369), " 67369 mod 24 =", 67369 % 24)
out("item 6: 4*236094-944329 =", 4*236094 - 944329, " 944329 mod 840 =", 944329 % 840, " factor a:", sp.factorint(236094))
out("item 22 constants: 125873811/262144 =", float(Fr(125873811, 262144)), "; 327448292668/47045881 =", float(Fr(327448292668, 47045881)))
out("22-digit prime length:", len("7510085481569082811681"), " BPSW prime:", sp.isprime(7510085481569082811681),
    " mod 840 =", 7510085481569082811681 % 840)
out("bounded_transport example p=37,a=12:", solutions_with_a(37, 12), " E,M =", EM(37, 12))
out("first-two-shell example p=373,a=95: R =", 4*95 - 373, " E,M =", EM(373, 95))
out("X5: 289^3 mod 840 =", pow(289, 3, 840))
out("unit squares mod 840:", sorted({c*c % 840 for c in range(840) if math.gcd(c, 840) == 1}))
nonsq = [c for c in range(840) if math.gcd(c, 840) == 1 and c % 24 == 1]
out("unit classes =1 mod 24:", len(nonsq))
# item 8 equality primes: 4p = 3t^2 + 6t - 25
for p in (41, 761, 1193, 1721, 3881):
    t = sp.symbols('t'); sol = [s for s in sp.solve(3*t**2 + 6*t - 25 - 4*p, t) if s > 0]
    out(f"item 8: 4p=3t^2+6t-25 at p={p}: t={sol}, p mod 8 = {p % 8}, prime={sp.isprime(p)}")
# R3 count integrality: P2 = 1 mod 4 whenever a = 1 mod 3
bad = 0
for a in range(4, 200000, 3):
    f = sp.factorint(a)
    P2 = math.prod(2*e + 1 for q, e in f.items() if q % 3 == 2)
    if P2 % 4 != 1: bad += 1
out("P2 = 1 mod 4 for all a = 1 mod 3 below 2e5:", bad == 0)
out(f"total {time.time()-T0:.1f}s")
