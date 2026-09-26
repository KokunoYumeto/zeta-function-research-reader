#!/usr/bin/env python3
"""Independent checks of the norm-subdivision ("orchard") section of bounded_transport.tex:
lem:split, lem:marked-finite, thm:orchard-partition and the p = 1201 example.
Exact integers only; the returns are enumerated by a brute force that does not use the
delta-parametrisation of lem:marked-finite."""
import time
from math import gcd, isqrt
from fractions import Fraction
from sympy import isprime, primerange, divisors

T0 = time.time()
FAIL = []
def check(c, m):
    if not c:
        FAIL.append(m); print("FAIL:", m)

def det(V, W):
    return V[0] * W[1] - V[1] * W[0]

def split(V, W):
    """lem:split: unique 1 <= r < D, E with W = rV + D E, det(V,E) = 1."""
    D = det(V, W)
    # Bezout for E0 with det(V,E0) = 1: V0*E0[1] - V1*E0[0] = 1
    def egcd(a, b):
        if b == 0:
            return a, 1, 0
        g, x, y = egcd(b, a % b)
        return g, y, x - (a // b) * y
    g, s, t = egcd(V[0], V[1])      # s V0 + t V1 = 1
    E0 = (-t, s)                    # det(V,E0) = V0*s - V1*(-t) = 1
    check(det(V, E0) == 1, "Bezout E0")
    # W = r0 V + D E0  -> r0 = det(W,E0)/det(V,E0) ... solve: W - D E0 = r0 V
    X = (W[0] - D * E0[0], W[1] - D * E0[1])
    r0 = X[0] // V[0] if V[0] else X[1] // V[1]
    check(X == (r0 * V[0], r0 * V[1]), "r0")
    k = r0 // D                     # r = r0 - D k in [0, D)
    r = r0 - D * k
    E = (E0[0] + k * V[0], E0[1] + k * V[1])
    check(1 <= r < D and W == (r * V[0] + D * E[0], r * V[1] + D * E[1]) and det(V, E) == 1, "split data")
    # uniqueness: any other E' with det(V,E')=1 is E + jV, giving r - Dj, outside [1,D) for j != 0
    Z = (V[0] + E[0], V[1] + E[1])
    check(Fraction((D - r) * V[0] + W[0], D) == Z[0] and Fraction((D - r) * V[1] + W[1], D) == Z[1], "Z formula")
    check(Z[0] > 0 and Z[1] > 0 and gcd(*Z) == 1 and det(V, Z) == 1 and det(Z, W) == D - r, "Z properties")
    check(Z[0] <= max(V[0], W[0]) and Z[1] <= max(V[1], W[1]), "coordinate bound")
    return Z

def chain(V, W):
    out = [V]
    while det(V, W) > 1:
        Z = split(V, W)
        out.append(Z)
        V = Z
    out.append(W)
    return out

def in_cone(Vg, Wg, X):
    # X in closed cone spanned by Vg, Wg (det(Vg,Wg) > 0): det(Vg,X) >= 0 and det(X,Wg) >= 0
    return det(Vg, X) >= 0 and det(X, Wg) >= 0

def brute_returns(p, Vg, Wg):
    """all (q,k,t,b,e): qt - pk = 1, q+e = 4bk, (q,k),(p,t) in closed cone(Vg,Wg), all positive."""
    # (p,t) in cone: det(Vg,(p,t)) >= 0 and det((p,t),Wg) >= 0 ; slope p/t between the generators
    out = []
    # t range: t>0 with both dets >= 0 ; each det linear in t
    tmin = 1; tmax = 10 ** 9
    # det(Vg,(p,t)) = Vg0*t - Vg1*p >= 0  -> t >= Vg1*p/Vg0
    tmin = max(tmin, -(-Vg[1] * p // Vg[0]))
    # det((p,t),Wg) = p*Wg1 - t*Wg0 >= 0 -> t <= p*Wg1/Wg0
    tmax = min(tmax, p * Wg[1] // Wg[0])
    for t in range(tmin, tmax + 1):
        if gcd(p, t) != 1:
            continue
        k0 = (-pow(p, -1, t)) % t if t > 1 else 0
        if k0 == 0:
            k0 = t
        k = k0
        while k <= p * t + 1:      # k(4bt - p) = et + 1 <= pt + 1 forces k <= pt + 1
            q = (p * k + 1) // t
            check(q * t - p * k == 1, "det")
            if in_cone(Vg, Wg, (q, k)):
                for e in (1, p):
                    if (q + e) % (4 * k) == 0:
                        out.append((q, k, t, (q + e) // (4 * k), e))
            k += t
    return set(out)

def lemma_returns(p, Vg, Wg):
    """lem:marked-finite enumeration inside the cone with slope interval [beta, alpha]."""
    # slopes r/s of generators
    s1, s2 = Fraction(Vg[0], Vg[1]), Fraction(Wg[0], Wg[1])
    alpha, beta = max(s1, s2), min(s1, s2)
    out = set()
    tlo = -(-p * beta.denominator // beta.numerator) if True else 0
    from math import ceil, floor
    tlo = ceil(Fraction(p) / alpha); thi = floor(Fraction(p) / beta)
    for t in range(tlo, thi + 1):
        for e in (1, p):
            N = e * t + 1
            for k in divisors(N):
                delta = N // k
                if (delta + p) % (4 * t):
                    continue
                if not (beta <= Fraction(p * k + 1, t * k) <= alpha):
                    continue
                b = (p + delta) // (4 * t)
                q = 4 * b * k - e
                check(q == Fraction(p * k + 1, t), "q formula")
                out.add((q, k, t, b, e))
    return out

def witness(p, ret):
    q, k, t, b, e = ret
    return (b * k, b * t, p * b * k * t) if e == p else (b * t, p * b * k, p * b * k * t)

def norm_reps(n):
    return [(u, v) for v in range(1, isqrt(n // 2) + 1) for u in [isqrt(n - 2 * v * v)]
            if u > 0 and u * u + 2 * v * v == n and gcd(u, v) == 1]

# ------------------------------------------------------------ the p = 1201 example
p = 1201
v0, w0 = (7, 24), (31, 11)
check(7 ** 2 + 2 * 24 ** 2 == 1201 and 31 ** 2 + 2 * 11 ** 2 == 1203, "norms")
Delta = v0[0] * w0[1] - v0[1] * w0[0]; T = v0[0] * w0[0] + 2 * v0[1] * w0[1]
check((Delta, T, p + 1 - T, p + 1 + T) == (-667, 745, 457, 1947) and (p + 1 - T) * (p + 1 + T) == 1 + 2 * Delta ** 2, "Delta,T")
ch = chain((31, 11), (7, 24))
check(ch == [(31, 11), (14, 5), (11, 4), (8, 3), (5, 2), (2, 1), (1, 1), (1, 2), (1, 3), (3, 10), (5, 17), (7, 24)], f"chain {ch}")
M = ((23, 1201), (9, 470))
check(23 * 470 - 1201 * 9 == 1 and 23 + 1201 == 4 * 34 * 9, "tagged return")
leaves = list(zip(ch[:-1], ch[1:]))
L_of = [lf for lf in leaves if in_cone(lf[0], lf[1], (23, 9)) and in_cone(lf[0], lf[1], (1201, 470))]
check(L_of == [((8, 3), (5, 2))], f"leaf of tagged return {L_of}")
check(witness(1201, (23, 9, 470, 34, 1201)) == (306, 15980, 172727820), "witness 306")
check(Fraction(1, 306) + Fraction(1, 15980) + Fraction(1, 172727820) == Fraction(4, 1201), "witness identity")
# the empty unimodular cone ((24,35),(13,19))
check(det((24, 35), (13, 19)) == 1, "empty cone det")
check((821 * 7 + 331 * 31, 821 * 24 + 331 * 11) == (24 * 667, 35 * 667) and (446 * 7 + 179 * 31, 446 * 24 + 179 * 11) == (13 * 667, 19 * 667), "containment")
check(brute_returns(p, (24, 35), (13, 19)) == set(), "empty cone has no returns")
for t, k0, q in [(1752, 407, 279), (1753, 759, 520), (1754, 1237, 847), (1755, 434, 297)]:
    check((1201 * k0 + 1) == q * t and all((1201 * k + 1) % t for k in range(1, k0)), f"k0 row t={t}")
print("[B1] p=1201 example: norms, Delta, T, canonical chain (12 vectors), tagged return and its unique leaf "
      "C((8,3),(5,2)), witness (306,15980,172727820), empty cone data: all reproduce")

# ------------------------------------------------------------ all primes of the shape, below a bound
t0 = time.time()
tested = 0; totret = 0
for p in primerange(5, 1300):
    V = norm_reps(p); W = norm_reps(p + 2)
    if not V or not W:
        continue
    for v0 in V:
        for w0 in W:
            D0 = det(v0, w0)
            check(D0 != 0 and abs(D0) >= 2, "Delta >= 2")
            V0, W0 = (v0, w0) if D0 > 0 else (w0, v0)
            ch = chain(V0, W0)
            leaves = list(zip(ch[:-1], ch[1:]))
            check(len(leaves) <= abs(D0), "leaves <= D")
            check(all(det(x, y) == 1 for x, y in leaves), "unimodular leaves")
            check(max(x[0] for x in ch) < p, "first coordinates < p")
            parent = brute_returns(p, V0, W0)
            check(parent == lemma_returns(p, V0, W0), f"lem:marked-finite parent p={p}")
            union = []
            for lf in leaves:
                rs = brute_returns(p, lf[0], lf[1])
                check(rs == lemma_returns(p, lf[0], lf[1]), f"lem:marked-finite leaf p={p}")
                union.extend(rs)
            check(len(union) == len(set(union)) and set(union) == parent, f"disjoint union p={p}")
            for r in parent:
                x, y, z = witness(p, r)
                check(Fraction(1, x) + Fraction(1, y) + Fraction(1, z) == Fraction(4, p), "witness")
            tested += 1; totret += len(parent)
print(f"[B2] lem:split (unique r,E; Z positive primitive interior; dets; coordinate bound), lem:marked-finite "
      f"(= brute force on parent and every leaf), thm:orchard-partition (parent returns = disjoint union of leaf "
      f"returns) for all {tested} (p, v0, w0) with p < 1300 prime, p = u^2+2v^2, p+2 = x^2+2y^2 primitive; "
      f"{totret} returns, every one an ES witness ({time.time()-t0:.1f}s)")
print()
print("TOTAL FAILURES:", len(FAIL))
print(f"runtime {time.time()-T0:.1f}s")
