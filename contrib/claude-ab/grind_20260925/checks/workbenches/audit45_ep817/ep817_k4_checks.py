#!/usr/bin/env python3
"""Independent audit checks for the k=4 theorem of the Erdos Problem 817 workbench
(paper/ep817_k4_rate.tex) and for the ternary-variance refinement (EP-03).
Written for this audit from the written statements only; it does not import or
reuse any workbench code.  Exact integer / Fraction arithmetic throughout.

Sections
  A  bounded mod-19 kernel (Lemma mod-kernel)
  B  digit rigidity of D = {0,1,7,8,9,15,16} mod 19 (Proposition digit)
  C  carry-free lift: H(A_m) equals the digit language and is 4-AP-free, m<=4;
     heredity under deletion for all subsets of A_2, A_3
  D  structure lemmas on every admissible set in an exhaustive domain:
     relation splitting, disjoint minimal blocks, unique block decomposition,
     complete short kernel, ternary count |T(A)| = 3^t prod(3^m-2^m), block
     sizes >= 3, |T(A)| >= M_n >= 19^(n/3), the EP-03 polynomial factorisation
     and exact variance, and 19(M^2-1) <= 192 Q
  E  negative control: without the 4-AP-free hypothesis the conclusions fail
  F  the finite bounds against exact g_4(n) (values from the two C searches)
"""
import itertools, math, sys, time
from fractions import Fraction

t0 = time.time()
out = []
def say(*a):
    s = " ".join(str(x) for x in a)
    print(s); out.append(s)

def ap4_free(S):
    """S: set of ints. True iff no x,d!=0 with x,x+d,x+2d,x+3d in S."""
    v = sorted(S)
    for i in range(len(v)):
        for j in range(i + 1, len(v)):
            df = v[j] - v[i]
            if df % 3: continue
            d = df // 3
            if v[i] + d in S and v[i] + 2 * d in S:
                return False
    return True

def H(A):
    s = {0}
    for a in A:
        s |= {x + a for x in s}
    return s

# ---------------------------------------------------------------- A
cnt = 0; ok = True
for u, v, w in itertools.product(range(-2, 3), repeat=3):
    cnt += 1
    lhs = (u + 7 * v + 8 * w) % 19 == 0
    rhs = (u == v and w == -u)
    ok &= (lhs == rhs)
say(f"A. mod-19 kernel: {cnt} triples checked; kernel = t(1,1,-1), t in [-2,2]: {ok}")
assert ok and cnt == 125

# ---------------------------------------------------------------- B
D = sorted({(u + 7 * v + 8 * w) for u, v, w in itertools.product((0, 1), repeat=3)})
say(f"B. digit set D = {D} (7 values; 8 = 8 = 1+7 is the only collision)")
assert D == [0, 1, 7, 8, 9, 15, 16]
Dm = set(D)
bad = [(x, e) for x in range(19) for e in range(1, 19)
       if all((x + i * e) % 19 in Dm for i in range(4))]
say(f"   all 19*18 = {19*18} modular 4-APs with nonzero step: {len(bad)} lie in D")
assert not bad
quads = 0
for z in itertools.product(D, repeat=4):
    if (z[0] - 2 * z[1] + z[2]) % 19 == 0 and (z[1] - 2 * z[2] + z[3]) % 19 == 0:
        quads += 1
        assert z[0] == z[1] == z[2] == z[3]
say(f"   7^4 = {7**4} digit quadruples: {quads} have both second differences = 0 mod 19, all constant")
# stronger statement actually used by the Lean proof: second differences vanish mod 19 => equal

# ---------------------------------------------------------------- C
for m in range(1, 5):
    Am = [19 ** j * c for j in range(m) for c in (1, 7, 8)]
    assert len(set(Am)) == 3 * m and max(Am) == 8 * 19 ** (m - 1)
    Hm = H(Am)
    lang = {sum(d * 19 ** j for j, d in enumerate(ds)) for ds in itertools.product(D, repeat=m)}
    same = (Hm == lang)
    # bitset 4-AP test (fast for m=4)
    bits = 0
    for x in Hm: bits |= 1 << x
    top = max(Hm)
    free = all((bits & (bits >> d) & (bits >> (2 * d)) & (bits >> (3 * d))) == 0 for d in range(1, top // 3 + 1))
    say(f"C. m={m}: |A_m|={len(Am)}, max={max(Am)}=8*19^{m-1}, |H(A_m)|={len(Hm)}=7^{m}: {len(Hm)==7**m}, "
        f"H = digit language: {same}, 4-AP-free: {free}, max H={top} < 19^{m}: {top < 19**m}")
    assert same and free and len(Hm) == 7 ** m
for m in (2, 3):
    Am = [19 ** j * c for j in range(m) for c in (1, 7, 8)]
    allfree = all(ap4_free(H(B)) for r in range(len(Am) + 1) for B in itertools.combinations(Am, r))
    say(f"   all {2**len(Am)} subsets of A_{m} have 4-AP-free subset sums: {allfree}")
    assert allfree
# the 8-collision is real: 1+7 = 8, so H(A_m) has repeated sums (|H| = 7^m < 8^m)

# ---------------------------------------------------------------- D
def analyse(A, full_short_kernel=True):
    """Return dict of checks for admissible A (H(A) 4-AP-free)."""
    n = len(A)
    rel1 = [r for r in itertools.product((-1, 0, 1), repeat=n)
            if any(r) and sum(ri * ai for ri, ai in zip(r, A)) == 0]
    supp = {r: frozenset(i for i in range(n) if r[i]) for r in rel1}
    minimal = [r for r in rel1 if not any(supp[s] < supp[r] for s in rel1)]
    # Lemma disjoint: minimal r,s: disjoint supports or s = +-r
    for r in minimal:
        for s in minimal:
            if supp[r] & supp[s]:
                assert s == r or s == tuple(-x for x in r), (A, r, s)
    reps = []
    for r in minimal:
        if tuple(-x for x in r) not in reps: reps.append(r)
    blocks = [supp[r] for r in reps]
    assert all(len(b) >= 3 for b in blocks)
    for b1, b2 in itertools.combinations(blocks, 2): assert not (b1 & b2)
    covered = set().union(*blocks) if blocks else set()
    t_free = n - len(covered)
    # Lemma signed-decomp: every signed relation is a unique +-1/0 block sum
    for q in rel1:
        for i in range(n):
            if i not in covered: assert q[i] == 0
        for r, b in zip(reps, blocks):
            vals = {q[i] * r[i] for i in b}
            assert vals in ({0}, {1}, {-1}), (A, q, r)
    # Lemma split + short kernel on the whole box [-2,2]^n
    nrel2 = 0
    if full_short_kernel:
        for c in itertools.product(range(-2, 3), repeat=n):
            if sum(ci * ai for ci, ai in zip(c, A)) != 0: continue
            nrel2 += 1
            u = [ci if abs(ci) == 1 else 0 for ci in c]
            v = [ci // 2 if abs(ci) == 2 else 0 for ci in c]
            assert sum(x * a for x, a in zip(u, A)) == 0 and sum(x * a for x, a in zip(v, A)) == 0
            for i in range(n):
                if i not in covered: assert c[i] == 0
            for r, b in zip(reps, blocks):
                ts = {c[i] * r[i] for i in b}
                assert len(ts) == 1, (A, c, r)
    # ternary image and count formula
    T = {sum(x * a for x, a in zip(xs, A)) for xs in itertools.product((0, 1, 2), repeat=n)}
    pred = 3 ** t_free
    for b in blocks: pred *= 3 ** len(b) - 2 ** len(b)
    assert len(T) == pred, (A, len(T), pred)
    q, rr = divmod(n, 3); Mn = 19 ** q * 3 ** rr
    assert len(T) >= Mn and Mn ** 3 >= 19 ** n          # M >= M_n >= 19^(n/3)
    assert len(T) <= 2 * sum(A) + 1
    # EP-03: polynomial factorisation (coefficient map) and exact variance
    poly = {0: 1}
    def mul(p, qd):
        r = {}
        for e1, c1 in p.items():
            for e2, c2 in qd.items():
                r[e1 + e2] = r.get(e1 + e2, 0) + c1 * c2
        return {e: c for e, c in r.items() if c}
    for i in range(n):
        if i not in covered: poly = mul(poly, {0: 1, A[i]: 1, 2 * A[i]: 1})
    for r, b in zip(reps, blocks):
        full = {0: 1}; half = {0: 1}
        for i in b:
            full = mul(full, {0: 1, A[i]: 1, 2 * A[i]: 1}); half = mul(half, {0: 1, A[i]: 1})
        SB = sum(A[i] for i in b); assert SB % 2 == 0
        assert sum(A[i] for i in b if r[i] == 1) == SB // 2
        PB = dict(full)
        for e, c in half.items(): PB[e + SB // 2] = PB.get(e + SB // 2, 0) - c
        PB = {e: c for e, c in PB.items() if c}
        assert set(PB.values()) <= {1}
        poly = mul(poly, PB)
    assert set(poly.values()) <= {1} and set(poly) == T
    Mfr = Fraction(len(T)); mean = Fraction(sum(T), len(T)); S = sum(A)
    var = Fraction(sum(x * x for x in T), len(T)) - mean ** 2
    kappa = lambda m: Fraction(8 * 3 ** m - 3 * 2 ** m, 12 * (3 ** m - 2 ** m))
    pred_var = Fraction(2, 3) * sum(A[i] ** 2 for i in range(n) if i not in covered) + \
        sum(kappa(len(b)) * sum(A[i] ** 2 for i in b) for b in blocks)
    Q = sum(a * a for a in A)
    assert mean == S and var == pred_var and var <= Fraction(16, 19) * Q
    assert var >= Fraction(len(T) ** 2 - 1, 12) and 19 * (len(T) ** 2 - 1) <= 192 * Q
    return dict(blocks=[len(b) for b in blocks], t=t_free, T=len(T), nrel2=nrel2)

def admissible_sets(n, Nmax):
    """All n-subsets of [1,Nmax] with 4-AP-free H, by DFS with heredity pruning."""
    res = []
    def rec(prefix, Hs, start):
        if len(prefix) == n:
            res.append(tuple(prefix)); return
        for a in range(start, Nmax + 1):
            H2 = Hs | {x + a for x in Hs}
            if ap4_free(H2): rec(prefix + [a], H2, a + 1)
    rec([], {0}, 1)
    return res

domains = [(1, 30), (2, 30), (3, 40), (4, 40), (5, 48)]
from collections import Counter
for n, Nmax in domains:
    sets_ = admissible_sets(n, Nmax)
    shapes = Counter(); tot2 = 0
    for A in sets_:
        r = analyse(A, full_short_kernel=True)
        shapes[tuple(sorted(r["blocks"]))] += 1; tot2 += r["nrel2"]
    say(f"D. n={n}, all admissible n-subsets of [1,{Nmax}]: {len(sets_)} sets; all structure checks pass; "
        f"block-size patterns {dict(shapes)}; {tot2} relations in [-2,2]^n (zero vector included) checked")
# optimal sets from the exact search (n <= 6) and larger block sizes
extra = [(1,), (1, 3), (2, 3), (1, 4, 5), (1, 9, 13, 14), (3, 11, 13, 14), (1, 13, 35, 39, 40),
         (3, 26, 37, 39, 40), (2, 29, 45, 74, 77, 79), (1, 7, 8, 19, 133, 152),
         (1, 7, 8, 19, 133, 152, 361)]
for A in extra:
    if ap4_free(H(A)):
        r = analyse(A, full_short_kernel=(len(A) <= 7))
        say(f"   extra A={A}: admissible, blocks {r['blocks']}, free coords {r['t']}, |T|={r['T']}")
    else:
        say(f"   extra A={A}: NOT admissible (H has a 4-AP)")

# ---------------------------------------------------------------- E
say("E. negative controls (hypothesis H(A) 4-AP-free removed):")
for A in [(1, 2, 3), (1, 2, 4), (2, 3, 4, 5)]:
    n = len(A)
    T = {sum(x * a for x, a in zip(xs, A)) for xs in itertools.product((0, 1, 2), repeat=n)}
    q, rr = divmod(n, 3); Mn = 19 ** q * 3 ** rr
    say(f"   A={A}: H 4-AP-free={ap4_free(H(A))}, |T(A)|={len(T)}, M_n={Mn}: bound |T|>=M_n holds={len(T)>=Mn}")

# ---------------------------------------------------------------- F
g_exact = {1: 1, 2: 3, 3: 5, 4: 14, 5: 40, 6: 79}
if len(sys.argv) > 1:
    for kv in sys.argv[1:]:
        k, v = kv.split("="); g_exact[int(k)] = int(v)

def iroot3_19pow(n):  # 19^(n/3) as float for display only
    return 19 ** (n / 3)

def lower_paper(n):          # (19^(n/3)-1)/(2n): exact test N >= this  <=>  (2nN+1)^3 >= 19^n
    # smallest integer N with (2nN+1)^3 >= 19^n
    N = 0
    while (2 * n * N + 1) ** 3 < 19 ** n: N += 1
    return N
def lower_remark(n):         # ceil((19^(n/3)+n(n-1)-1)/(2n)) : smallest N with (2nN-n(n-1)+1)^3 >= 19^n
    N = 1
    while (2 * n * N - n * (n - 1) + 1) ** 3 < 19 ** n or 2 * n * N - n * (n - 1) + 1 < 0: N += 1
    return N
def lower_ep03_combined(n):  # EP-03 section 6: least N meeting all three integer constraints
    q, r = divmod(n, 3); Mn = 19 ** q * 3 ** r
    N = n
    while True:
        Qmax = n * N * N - n * (n - 1) * N + n * (n - 1) * (2 * n - 1) // 6
        if 2 * n * N >= Mn + n * (n - 1) - 1 and 192 * Qmax >= 19 * (Mn * Mn - 1):
            return N
        N += 1
def upper(n):
    return 8 * 19 ** ((n + 2) // 3 - 1)

say("F. finite bounds vs exact g_4(n)")
say("   n | paper lower | remark lower | EP-03 combined | exact g_4(n) | upper 8*19^(ceil(n/3)-1)")
for n in range(1, 13):
    ex = g_exact.get(n)
    lp, lr, lc, up = lower_paper(n), lower_remark(n), lower_ep03_combined(n), upper(n)
    if ex is not None:
        assert lp <= ex and lr <= ex and lc <= ex <= up
    say(f"   {n:2d} | {lp:11d} | {lr:12d} | {lc:14d} | {str(ex) if ex else '-':>12} | {up}")
say("   EP-03 table claims n=1..6: 1,3,5,11,27,49; n=9: 724; n=12: 11841; n=30: 352128817514")
claims = {1: 1, 2: 3, 3: 5, 4: 11, 5: 27, 6: 49, 9: 724, 12: 11841, 30: 352128817514}
mine = {n: lower_ep03_combined(n) if n < 20 else None for n in claims}
# n=30 needs a binary search
def lower_ep03_bs(n):
    q, r = divmod(n, 3); Mn = 19 ** q * 3 ** r
    def ok(N):
        Qmax = n * N * N - n * (n - 1) * N + n * (n - 1) * (2 * n - 1) // 6
        return N >= n and 2 * n * N >= Mn + n * (n - 1) - 1 and 192 * Qmax >= 19 * (Mn * Mn - 1)
    lo, hi = n, 10 ** 30
    while lo < hi:
        mid = (lo + hi) // 2
        if ok(mid): hi = mid
        else: lo = mid + 1
    return lo
mine[30] = lower_ep03_bs(30)
say(f"   recomputed: {mine}; agree: {all(mine[n]==claims[n] for n in claims)}")
# sqrt(n) gain: ratio of variance bound to interval bound
for n in (30, 60, 120, 300):
    q, r = divmod(n, 3); Mn = 19 ** q * 3 ** r
    ratio = math.sqrt(19 * (Mn * Mn - 1) / (192 * n)) / ((Mn - 1) / (2 * n))
    say(f"   n={n}: (variance bound)/(interval bound with M_n) = {ratio:.3f}; 2*sqrt(19/192)*sqrt(n) = {2*math.sqrt(19/192)*math.sqrt(n):.3f}")
# nth roots
for n in (6, 30, 300, 3000):
    lo = ((19 ** (n / 3) - 1) / (2 * n)) ** (1 / n) if n < 400 else math.exp((n / 3 * math.log(19) - math.log(2 * n)) / n)
    hi = math.exp((math.log(8) + ((n + 2) // 3 - 1) * math.log(19)) / n)
    say(f"   n={n}: lower^(1/n)={lo:.5f}, upper^(1/n)={hi:.5f}, 19^(1/3)={19**(1/3):.5f}")
say(f"done in {time.time()-t0:.1f}s")
