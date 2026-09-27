#!/usr/bin/env python3
"""
Checks for note 11_, revision 2 (Lemma 11.2, Lemma 11.3, Example 11.5), claude-ab, model claude-opus-5-5 (Opus 5.5, max effort).

Lemma 11.2 (first negative coefficient).  M a multiplicative submonoid of the
positive integers, D_M(s) = sum_{m in M} m^{-s}, log D_M = sum_{n>=2} r_n n^{-s}.
If n0 is the smallest element of M with more than one factorization into atoms
of M, then r_n >= 0 for n < n0, and r_{n0} = 1 - j + eps, where j >= 2 is the
number of factorizations of n0 and eps = sum of 1/k over the factorizations of
n0 of the form u^k (u an atom).  In particular r_{n0} < 0.  For M = M_H
(congruence monoid), eps <= 1/2, hence r_{n0} <= -1/2.

Lemma 11.3 (half-factoriality).  M_H is half-factorial iff [G:H] <= 2.

Exact arithmetic throughout (fractions.Fraction, integers).
"""
from fractions import Fraction
from itertools import combinations
from math import gcd
import sys

# ---------------------------------------------------------------- helpers
def factorize(n):
    f, d = {}, 2
    while d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f

def divisors(n):
    ds = [1]
    for p, e in factorize(n).items():
        ds = [d * p ** k for d in ds for k in range(e + 1)]
    return sorted(ds)

def local_data(x, inM):
    """Divisor-closed data at x: M-divisors, atoms among them, number of
    factorizations j(x) (multisets of atoms), set of lengths, and the exact
    formal-log coefficient r(x) = sum_k (-1)^{k+1}/k T_k(x)."""
    D = [d for d in divisors(x) if inM(d)]
    Dset = set(D)
    # atoms: d>1 in M with no factorization d = e*f, e,f in M\{1}
    atoms = []
    for d in D:
        if d == 1:
            continue
        if not any(d % e == 0 and (d // e) in Dset and e != 1 and e != d for e in D):
            atoms.append(d)
    # number of factorizations (multisets) and length sets: coin-change DP
    cnt = {d: 0 for d in D}; cnt[1] = 1
    L = {d: 0 for d in D}; L[1] = 1          # bitmask of lengths
    for u in atoms:
        for d in D:                           # ascending
            if d % u == 0 and (d // u) in Dset:
                cnt[d] += cnt[d // u]
                L[d] |= L[d // u] << 1
    # ordered k-tuples T_k(d) of elements of M\{1} with product d
    Dm = [d for d in D if d != 1]
    T = {d: 1 for d in Dm}                    # k = 1
    r = Fraction(0)
    k = 1
    while any(T.values()):
        r += Fraction((-1) ** (k + 1), k) * T.get(x, 0)
        T = {d: sum(T[d // e] for e in Dm if d % e == 0 and (d // e) in T and d // e != 1)
             for d in Dm}
        k += 1
    lengths = [i for i in range(L[x].bit_length()) if (L[x] >> i) & 1]
    return atoms, cnt[x], lengths, r

def pure_power_eps(x, atoms):
    eps = Fraction(0)
    for u in atoms:
        k, y = 0, x
        while y % u == 0:
            y //= u; k += 1
        if y == 1 and k >= 1:
            eps += Fraction(1, k)
    return eps

def global_scan(inM, N):
    """Smallest element n0 <= N with >= 2 factorizations (or None), and whether
    some element <= N has two different factorization lengths."""
    M = [n for n in range(1, N + 1) if inM(n)]
    Mset = set(M)
    isatom = {}
    # atoms: elements > 1 not a product of two smaller elements > 1
    prod_hit = bytearray(N + 1)
    Ms = [m for m in M if m > 1]
    for i, a in enumerate(Ms):
        if a * a > N:
            break
        for b in Ms[i:]:
            if a * b > N:
                break
            prod_hit[a * b] = 1
    atoms = [m for m in Ms if not prod_hit[m]]
    cnt = [0] * (N + 1); cnt[1] = 1
    L = [0] * (N + 1); L[1] = 1
    for u in atoms:
        for d in range(u, N + 1, u):
            if cnt[d // u]:
                cnt[d] += cnt[d // u]
                L[d] |= L[d // u] << 1
    n0 = next((n for n in M if cnt[n] >= 2), None)
    hf_witness = next((n for n in M if L[n] & (L[n] - 1)), None)
    return M, n0, hf_witness

def r_upto(M, n0):
    """Exact r_n for n in M, n <= n0, via the Omega-derivation recursion
    Omega(n) r_n = Omega(n) a_n - sum_{d|n,1<d<n} Omega(d) r_d a_{n/d}."""
    Mset = set(M)
    Om = {}
    def Omega(n):
        if n not in Om:
            Om[n] = sum(factorize(n).values())
        return Om[n]
    r = {}
    for n in M:
        if n == 1 or n > n0:
            continue
        s = Fraction(0)
        for d in divisors(n):
            if 1 < d < n and d in r and (n // d) in Mset:
                s += Omega(d) * r[d]
        r[n] = Fraction(Omega(n)) - s / 1
        r[n] = r[n] / Omega(n)
    return r

def units(q):
    return [a for a in range(1, q + 1) if gcd(a, q) == 1] if q > 1 else [1]

def subgroups(q):
    G = units(q)
    mod = q if q > 1 else 1
    subs = set()
    for size in range(0, 4):
        for gens in combinations(G, size):
            H = {1 % mod if mod > 1 else 1}
            H = {1 if q > 1 else 1}
            frontier = set(H)
            gens_ = list(gens)
            changed = True
            while changed:
                changed = False
                for h in list(H):
                    for g in gens_:
                        y = (h * g) % q if q > 1 else 1
                        if y == 0 and q > 1:
                            continue
                        if y not in H:
                            H.add(y); changed = True
            subs.add(frozenset(H))
    return G, sorted(subs, key=lambda s: (len(s), sorted(s)))


def is_prime(n):
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True

def smallest_prime_in_class(q, c):
    n = c if c > 1 else c + q
    while not is_prime(n):
        n += q
    return n

def local_lengths(x, inM):
    D = [d for d in divisors(x) if inM(d)]
    Dset = set(D)
    atoms = [d for d in D if d != 1 and not any(
        e != 1 and e != d and d % e == 0 and (d // e) in Dset for e in D)]
    L = {d: 0 for d in D}; L[1] = 1
    for u in atoms:
        for d in D:
            if d % u == 0 and (d // u) in Dset:
                L[d] |= L[d // u] << 1
    return [i for i in range(L[x].bit_length()) if (L[x] >> i) & 1]

def constructive_witness(q, G, H, inM):
    """Proof of Lemma 11.3, (=>): an element of order n >= 3 in G/H gives
    p^n p'^n = (p p')^n; otherwise G/H is elementary abelian of order >= 4 and
    (p r s)^2 = p^2 r^2 s^2."""
    best = None
    for g in G:
        n = next(k for k in range(1, len(G) + 1) if pow(g, k, q) in H)
        if n >= 3:
            p = smallest_prime_in_class(q, g)
            pp = smallest_prime_in_class(q, pow(g, -1, q))
            x = p ** n * pp ** n
            if best is None or x < best:
                best = x
    if best is None:
        for g in G:
            for h in G:
                if g in H or h in H or (g * h) % q in H or (g * h) % q == g or (g * h) % q == h:
                    continue
                # distinct nontrivial cosets gH, hH, ghH
                if any(((g * pow(h, -1, q)) % q) == t for t in H):
                    continue
                p = smallest_prime_in_class(q, g); r = smallest_prime_in_class(q, h)
                t = smallest_prime_in_class(q, (g * h) % q)
                x = (p * r * t) ** 2
                if best is None or x < best:
                    best = x
    return best, local_lengths(best, inM)

# ---------------------------------------------------------------- run
out = []
def say(*a):
    s = " ".join(str(x) for x in a)
    print(s); out.append(s)

N = int(sys.argv[1]) if len(sys.argv) > 1 else 12000
QMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 16
say(f"# first_negative_coefficient.py  N={N}  q<= {QMAX}")
bad = 0
for q in range(1, QMAX + 1):
    G, subs = subgroups(q)
    for H in subs:
        idx = len(G) // len(H)
        inM = (lambda n, q=q, H=H: n == 1 or (q == 1) or (gcd(n, q) == 1 and (n % q) in H))
        M, n0, hfw = global_scan(inM, N)
        tag = f"q={q:2d} |H|={len(H):2d} [G:H]={idx:2d} H={sorted(H) if len(H) <= 6 else '...'}"
        # Lemma 11.3 expectation
        hf_expected = idx <= 2
        if n0 is None:
            r = r_upto(M, min(N, 12000))
            neg = [n for n, v in r.items() if v < 0]
            ok = (not neg)
            say(tag, "| n0 > N | all r_n>=0 up to min(N,12000):", ok, "| free expected:", idx == 1)
            bad += (not ok)
        else:
            atoms, j, lens, rx = local_data(n0, inM)
            eps = pure_power_eps(n0, atoms)
            r = r_upto(M, n0)
            neg_before = [n for n, v in r.items() if v < 0 and n < n0]
            ok = (rx == 1 - j + eps) and rx < 0 and (r[n0] == rx) and not neg_before and idx >= 2
            if idx >= 2 and len(H) >= 1:
                ok = ok and eps <= Fraction(1, 2)
            say(tag, f"| n0={n0} j={j} eps={eps} r(n0)={rx} (=1-j+eps: {rx == 1 - j + eps})",
                f"| r_n>=0 before n0: {not neg_before} | ok: {ok}")
            bad += (not ok)
        # half-factoriality check
        if hf_expected:
            hf_ok = hfw is None
            say("      half-factorial expected; length-ambiguous element <= N:", hfw, "| ok:", hf_ok)
        else:
            if hfw is not None:
                hf_ok = True
                say("      not half-factorial expected; witness <= N:", hfw, "| ok: True")
            else:
                x, lens = constructive_witness(q, G, H, inM)
                hf_ok = len(lens) >= 2
                say(f"      not half-factorial expected; no witness <= N; constructive x = {x}: lengths {lens} | ok: {hf_ok}")
        bad += (hf_ok is False)

# constructive witnesses for [G:H] >= 3 at H = {1}, q = 5, 7, 8, 10, 12 (from the proof)
say("# constructive half-factoriality witnesses (proof of Lemma 11.3)")
def primes_in_class(q, c, count=2, start=2):
    res, n = [], start
    while len(res) < count:
        n += 1
        if all(n % p for p in range(2, int(n ** 0.5) + 1)) and n % q == c:
            res.append(n)
    return res
for q, c in [(5, 2), (7, 3), (10, 3), (12, 5)]:
    G = units(q)
    H = {1}
    order = next(k for k in range(1, 50) if pow(c, k, q) == 1)
    inM = (lambda n, q=q: n == 1 or (gcd(n, q) == 1 and n % q == 1))
    if order >= 3:
        p = primes_in_class(q, c, 1)[0]
        cinv = pow(c, -1, q)
        pp = primes_in_class(q, cinv, 1)[0]
        x = p ** order * pp ** order
        atoms, j, lens, rx = local_data(x, inM)
        say(f"q={q} c={c} ord={order}: x = {p}^{order}*{pp}^{order} = {x}: lengths {lens}")
    else:
        say(f"q={q} c={c} has order {order}")
# elementary abelian case q = 8 (G/H = (Z/2)^2) and q = 12 ((Z/2)^2)
for q, (c, d) in [(8, (3, 5)), (12, (5, 7))]:
    e = (c * d) % q
    p = primes_in_class(q, c, 1)[0]; r_ = primes_in_class(q, d, 1)[0]; s_ = primes_in_class(q, e, 1)[0]
    x = (p * r_ * s_) ** 2
    inM = (lambda n, q=q: n == 1 or (gcd(n, q) == 1 and n % q == 1))
    atoms, j, lens, rx = local_data(x, inM)
    say(f"q={q} classes {c},{d},{e}: x = ({p}*{r_}*{s_})^2 = {x}: lengths {lens}")

# non-congruence examples: exponent monoids {2^e : e in Lambda} and generated monoids
say("# other submonoids of (N, x)")
def gen_monoid(gens, N):
    S = {1}
    frontier = [1]
    while frontier:
        new = []
        for a in frontier:
            for g in gens:
                b = a * g
                if b <= N and b not in S:
                    S.add(b); new.append(b)
        frontier = new
    return S
for gens in [(4, 8), (8, 32), (4, 32), (2, 3), (6, 10, 15), (4, 6, 9), (4, 6), (8, 12, 18, 27), (9, 12, 16), (2, 9, 12)]:
    Nloc = 5000
    S = gen_monoid(gens, Nloc)
    inM = (lambda n, S=S: n in S)
    M, n0, hfw = global_scan(inM, Nloc)
    if n0 is None:
        r = r_upto(M, Nloc)
        say(f"<{gens}>: free up to {Nloc}; all r>=0: {all(v >= 0 for v in r.values())}")
        continue
    atoms, j, lens, rx = local_data(n0, inM)
    eps = pure_power_eps(n0, atoms)
    r = r_upto(M, n0)
    neg_before = [n for n, v in r.items() if v < 0 and n < n0]
    ok = (rx == 1 - j + eps) and rx < 0 and r[n0] == rx and not neg_before
    say(f"<{gens}>: n0={n0} j={j} eps={eps} r(n0)={rx} | r>=0 before n0: {not neg_before} | ok: {ok}")
    bad += (not ok)

# analytic scope remark: D for {2^e : e != 1} = (1 - x + x^2)/(1 - x), x = 2^{-s}
import cmath
for root in [cmath.exp(1j * cmath.pi / 3), cmath.exp(-1j * cmath.pi / 3)]:
    say(f"root x={root:.6f}: |x|={abs(root):.12f}  -> Re s = -log|x|/log 2 = {-cmath.log(abs(root)).real / cmath.log(2).real:.3e}")
say("TOTAL FAILURES:", bad)
