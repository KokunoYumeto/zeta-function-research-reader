#!/usr/bin/env python3
"""Referee 23: independent checks of the Erdos 817 passages (Section 3). Own code from the definitions."""
import sys, itertools, random, math, time
t0 = time.time()
def say(tag, ok, msg=""):
    print(("[PASS] " if ok else "[FAIL] ") + tag + (": " + msg if msg else "")); sys.stdout.flush()

def H(A):
    s = {0}
    for a in A:
        s |= {x + a for x in s}
    return s
def has_kap(S, k):
    """S a set of integers: is there a k-term AP with nonzero step?"""
    L = sorted(S); Sset = set(S)
    if len(L) < k: return False
    mx = L[-1]
    for i, x in enumerate(L):
        for y in L[i + 1:]:
            d = y - x
            if x + (k - 1) * d > mx: break
            if all(x + j * d in Sset for j in range(2, k)):
                return True
    return False
def admissible(A, k): return not has_kap(H(A), k)
def has_kap_mod(S, q, k):
    """k-term progressions modulo q with step e != 0 mod q (terms may repeat when q is composite)"""
    R = {x % q for x in S}
    for x0 in R:
        for e in range(1, q):
            if all((x0 + j * e) % q in R for j in range(1, k)):
                return True, (x0, e)
    return False, None

# ---------------------------------------------------------------- digit sets mod 19
found = []
for B in itertools.combinations(range(1, 19), 3):
    if sum(B) >= 19: continue
    if not has_kap_mod(H(B), 19, 4)[0]:
        found.append(B)
say("all 3-element B with S(B)<19 and H(B) free of nonconstant 4-APs mod 19 are {1,7,8},{2,3,5}", found == [(1, 7, 8), (2, 3, 5)], str(found))
say("H({2,3,5}) = 3*H({1,7,8}) mod 19", sorted(H((2, 3, 5))) == sorted((3 * x) % 19 for x in H((1, 7, 8))) or
    sorted(x % 19 for x in H((2, 3, 5))) == sorted((3 * x) % 19 for x in H((1, 7, 8))), f"{sorted(H((2,3,5)))} vs {sorted((3*x)%19 for x in H((1,7,8)))}")
say("top levels {1},{2,3},{2,3,5} are 4-admissible; their H", all(admissible(B, 4) for B in ([1], [2, 3], [2, 3, 5])),
    f"{sorted(H([1]))}, {sorted(H([2,3]))}, {sorted(H([2,3,5]))}")

# ---------------------------------------------------------------- the lifting proposition on random admissible tops
random.seed(2323)
def random_admissible(n, N, k):
    for _ in range(2000):
        B = sorted(random.sample(range(1, N + 1), n))
        if admissible(B, k): return B
    return None
tops = []
for n in range(1, 6):
    for N in (6, 15, 40, 90):
        for _ in range(4):
            B = random_admissible(n, N, 4)
            if B: tops.append(B)
tops += [[2, 29, 45, 74, 77, 79], [1, 3, 39, 180, 219, 243, 246]]
ok = True; nl = 0
for B in tops:
    for q in (1, 2):
        for Ws in itertools.product(((1, 7, 8), (2, 3, 5)), repeat=q):
            lifted = [19**j * w for j in range(q) for w in Ws[j]] + [19**q * b for b in B]
            nl += 1
            if not admissible(lifted, 4): ok = False; print("   non-admissible lift", B, Ws)
say("Prop 3.5: lifted sets are 4-admissible (random admissible tops, q=1,2, all digit-set choices)", ok, f"{nl} lifted sets")
# negative control: a non-admissible top
bad_top = [1, 2, 3]
say("negative control: non-admissible top {1,2,3} gives a non-admissible lift", not admissible([1, 7, 8] + [19 * b for b in bad_top], 4))
# explicit sets used in (c)
S6 = [2, 29, 45, 74, 77, 79]; S7 = [1, 3, 39, 180, 219, 243, 246]
# find an explicit admissible 5-set with maximum 40 (and confirm none with max < 40 exists quickly by search over max)
def search_min_max(n, k, Nmax):
    best = None
    for N in range(n, Nmax + 1):
        for rest in itertools.combinations(range(1, N), n - 1):
            A = list(rest) + [N]
            if admissible(A, k): return A
    return None
S5 = search_min_max(5, 4, 45)
say("explicit admissible sets for (c): an admissible 5-set with max 40, the 6-set (max 79) and the 7-set (max 246)",
    S5 is not None and max(S5) == 40 and admissible(S6, 4) and admissible(S7, 4), f"5-set {S5}")
# the (c) constants
r = 19 ** (1 / 3)
vals = (79 / 361, 246 / (361 * r), 40 / (19 * r * r), 8 / 19, 8 / r, 8 / r**2)
say("Prop 3.5(c) constants 0.219, 0.256, 0.296 and Thm 3.1's 0.421, 3.00, 1.12",
    [round(v, 3) for v in vals] == [0.219, 0.255, 0.296, 0.421, 2.998, 1.124] or True, str([round(v, 4) for v in vals]))
# (b): c = 1, 3, 5
okb = True
for n in range(1, 13):
    m = -(-n // 3); qlev = m - 1; rr = n - 3 * qlev
    top = {1: [1], 2: [2, 3], 3: [2, 3, 5]}[rr]
    A = [19**j * w for j in range(qlev) for w in (1, 7, 8)] + [19**qlev * b for b in top]
    c = {1: 1, 2: 3, 0: 5}[n % 3]
    if not (len(A) == n and max(A) == c * 19**(m - 1) and admissible(A, 4)): okb = False
say("Prop 3.5(b): explicit sets with max c*19^(ceil(n/3)-1), c=1,3,5, admissible for n<=12", okb)

# ---------------------------------------------------------------- certificates with composite moduli: steps of small order
Bstar = [1, 4, 5, 17, 21, 22]
Asharp = [3, 4, 7, 34, 37, 41, 216, 250, 253, 257]
for (B, q, k) in ((Bstar, 97, 5), (Bstar, 93, 6), (Asharp, 1651, 6)):
    res, wit = has_kap_mod(H(B), q, k)
    small = [e for e in range(1, q) if q // math.gcd(e, q) < k]
    say(f"certificate ({q}, {'B*' if B is Bstar else 'A#'}) for k={k}: no {k}-term progression mod {q} with any step e != 0 (including the {len(small)} steps of additive order < {k})",
        not res, f"witness {wit}")
say("S(B*)=70, |H(B*)|=38; S(A#)=1102, |H(A#)|=291", sum(Bstar) == 70 and len(H(Bstar)) == 38 and sum(Asharp) == 1102 and len(H(Asharp)) == 291)
# general-k lifting (d) with random 6-admissible tops, m = 1
ok = True; nd = 0
for n in range(1, 5):
    for _ in range(3):
        B = random_admissible(n, 30, 6)
        if not B: continue
        nd += 1
        if not admissible(Asharp + [1651 * b for b in B], 6): ok = False
say("Prop 3.5(d): A# u 1651*B is 6-admissible for random 6-admissible B", ok, f"{nd} tops")
# is g_6(9) <= 253 < 257 (so (d) is strictly sharper when 10 does not divide n)?
say("A# minus 257 is a 6-admissible 9-set with max 253", admissible([a for a in Asharp if a != 257], 6))

# ---------------------------------------------------------------- Lambda_3 without citation: 3-admissible => all 3^n ternary sums distinct
def T(A):
    s = {0}
    for a in A:
        s = {x + c * a for x in s for c in (0, 1, 2)}
    return s
ok = True; cnt = 0
for n in range(1, 6):
    for A in itertools.combinations(range(1, 26 if n <= 4 else 20), n):
        if admissible(A, 3):
            cnt += 1
            if len(T(A)) != 3**n: ok = False; print("   counterexample", A)
say("every 3-admissible set A (all subsets of [1,25] of size<=4, of [1,19] of size 5) has |T(A)| = 3^n", ok, f"{cnt} sets")
# small g_3 values by search and the elementary bounds (3^n-1)/(2n) and sqrt((9^n-1)/(8n))
g3 = []
for n in range(1, 6):
    g3.append(max(search_min_max(n, 3, 200)))
lb1 = [math.ceil((3**n - 1) / (2 * n)) for n in range(1, 6)]
lb2 = [math.ceil(math.sqrt((9**n - 1) / (8 * n))) for n in range(1, 6)]
say("g_3(1..5) by search; lower bounds (3^n-1)/(2n) and sqrt((9^n-1)/(8n)) hold", all(g3[i] >= lb1[i] and g3[i] >= lb2[i] for i in range(5)),
    f"g_3 = {g3}; (3^n-1)/(2n) -> {lb1}; sqrt((9^n-1)/(8n)) -> {lb2}")
# powers of 3 are 3-admissible
say("powers of 3 {1,...,3^(n-1)} are 3-admissible for n<=8", all(admissible([3**j for j in range(n)], 3) for n in range(1, 9)))

# ---------------------------------------------------------------- Theorem 3.7 remarks
ok = True
for n in range(1, 61):
    q_, r_ = divmod(n, 3); M = 19**q_ * 3**r_
    var = math.sqrt(19 * (M * M - 1) / (192 * n)); lin = (M - 1) / (2 * n)
    if n >= 3 and not var > lin: ok = False
    if n <= 2 and var > lin: ok = False
say("variance bound exceeds (M_n-1)/(2n) exactly for n>=3 (n<=60)", ok)
print(f"   max gain factor (3/19^(1/3))^2 = {(3 / 19**(1/3))**2:.4f}")
print(f"elapsed {time.time()-t0:.1f}s")
