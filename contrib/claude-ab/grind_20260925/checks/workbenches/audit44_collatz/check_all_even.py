#!/usr/bin/env python3
"""Independent audit check of the all-even join extension
(collatz_reconstruction/research_program/all_even_join_extension_20260916/note.md).

Written from the note's statements only; imports nothing from the workbench.
T(n) = (3n+1)/2^v2(3n+1) on positive odd n.
"""
import sys, time, random
from fractions import Fraction
from math import floor, log

t0 = time.time()
def v2(x):
    return (x & -x).bit_length() - 1
def v3(x):
    assert x != 0
    k = 0
    while x % 3 == 0:
        x //= 3; k += 1
    return k
def T(n):
    x = 3 * n + 1
    return x >> v2(x)
def word(n, length):
    w = []
    for _ in range(length):
        x = 3 * n + 1; a = v2(x); w.append(a); n = x >> a
    return tuple(w), n
def path(n, length):
    vals = [n]
    for _ in range(length):
        n = T(n); vals.append(n)
    return vals

report = []
def ok(cond, msg):
    if not cond:
        print("FAIL:", msg); sys.exit(1)

# ---- Lemma 1: nu_3((2^e+2)/3) = nu_3(e-1) for even e ----
cnt = 0
for e in range(2, 4002, 2):
    h = (2 ** e + 2)
    ok(h % 3 == 0, "divisibility")
    h //= 3
    ok(h % 4 == 2, "h = 2 mod 4 at e=%d" % e)
    ok(v3(h) == v3(e - 1), "Lemma 1 at e=%d" % e)
    cnt += 1
report.append("Lemma 1 (nu3((2^e+2)/3)=nu3(e-1), h=2 mod 4): checked all even e in [2,4000]: %d cases PASS" % cnt)

# ---- Theorem 2 families ----
def amin(b, e, s):
    a = 1
    while 2 ** (a + e + 2 * b - s) >= 3 ** (a + b):
        a += 1
    return a
def family(b, e, s):
    h = (2 ** e + 2) // 3
    t = v3(h)
    a = amin(b, e, s)
    J = 2 ** (e + 2 * b - s); Q = 3 ** (a + b); K = 2 ** a * J
    d, r = ((4, 3) if s == 0 else (32, 27))
    # solve J n + h 3^b = 0 mod Q and n = r mod d by brute CRT over the d residues of n mod dQ
    res = (-h * 3 ** b * pow(J, -1, Q)) % Q
    n0 = None
    for k in range(d):
        c = res + k * Q
        if c % d == r:
            n0 = c; break
    if n0 == 0:
        n0 = d * Q
    m0 = (K * n0 + 2 ** a * h * 3 ** b) // Q - 1
    left = (1,) if s == 0 else (1, 2, 1)
    right = (1,) * a + (e,) + (2,) * (b - 1) + ((3,) if s == 0 else (1, 1, 3))
    return dict(b=b, e=e, s=s, h=h, t=t, a=a, J=J, Q=Q, K=K, d=d, r=r, n0=n0, m0=m0,
                left=left, right=right)

npairs = 0; nfam = 0
for s in (0, 1):
    for b in range(1, 11):
        for e in range(2, 27, 2):
            f = family(b, e, s)
            nfam += 1
            ok(f['a'] >= e and f['a'] > f['t'], "a>=e, a>t_e")
            ok(f['a'] <= b + 2 * e - 2 * s, "bound (4)")
            ok(f['K'] < f['Q'], "K<Q")
            ok((f['K'] * f['n0'] + 2 ** f['a'] * f['h'] * 3 ** b) % f['Q'] == 0, "m0 integral")
            vs = list(range(0, 25)) + [random.randrange(10 ** 6) for _ in range(5)] + [10 ** 30 + 7]
            for v in vs:
                n = f['n0'] + f['d'] * f['Q'] * v
                m = f['m0'] + f['d'] * f['K'] * v
                wl, yl = word(n, len(f['left']))
                wr, yr = word(m, len(f['right']))
                ok(wl == f['left'], "left word exact (b,e,s,v)=%s" % ((b, e, s, v),))
                ok(wr == f['right'], "right word exact (b,e,s,v)=%s" % ((b, e, s, v),))
                ok(yl == yr, "common endpoint")
                ok(yl == ((3 * n + 1) // 2 if s == 0 else (27 * n + 23) // 16), "endpoint formula")
                ok(0 < m < n, "0<m<n")
                ok(v3(n) == b + f['t'], "nu3(n)=b+t_e")
                # identity (11): m = (K/Q) n + h (2/3)^a - 1
                ok(Fraction(m) == Fraction(f['K'], f['Q']) * n + f['h'] * Fraction(2, 3) ** f['a'] - 1, "identity (11)")
                npairs += 1
report.append("Theorem 2: %d families (s in {0,1}, b=1..10, even e=2..26), %d pairs incl. v up to 1e30: exact left/right words, common endpoint, 0<m<n, nu3(n)=b+t_e, identity (11): PASS" % (nfam, npairs))

# ---- Converse/completeness for small-modulus families by forward enumeration of m ----
def completeness(b, e, s, M):
    f = family(b, e, s)
    right = f['right']; L = len(right); found = 0
    step_n = f['d'] * f['Q']; step_m = f['d'] * f['K']
    for m in range(1, M, 2):
        w, y = word(m, L)
        if w != right:
            continue
        # recover n from y through the left word
        if s == 0:
            if (2 * y - 1) % 3: continue
            n = (2 * y - 1) // 3
        else:
            if (16 * y - 23) % 27: continue
            n = (16 * y - 23) // 27
        if n <= 0 or n % 2 == 0: continue
        if word(n, len(f['left']))[0] != f['left']: continue
        ok((n - f['n0']) % step_n == 0 and n >= f['n0'], "converse: n in progression")
        v = (n - f['n0']) // step_n
        ok(m == f['m0'] + step_m * v, "converse: same parameter for m")
        found += 1
    # forward: every progression member with m<M was found
    expected = 0 if f['m0'] >= M else (M - 1 - f['m0']) // step_m + 1
    ok(found == expected, "completeness count %d vs %d for %s" % (found, expected, (b, e, s)))
    return found
tot = 0; combos = []
for (b, e, s) in [(1, 2, 0), (2, 2, 0), (1, 4, 0), (1, 2, 1), (3, 2, 0), (1, 6, 0)]:
    c = completeness(b, e, s, 1 << 21)
    tot += c; combos.append(((b, e, s), c))
report.append("Converse (endpoint equality on positive sources gives exactly the progression): all odd m < 2^21 scanned for 6 families %s: PASS" % combos)

# ---- Theorem 3: finite search vs brute-force backward search ----
E_MAX = 60
def brute_templates(n):
    """All (s,b,e,a') with a right word 1^a',e,2^(b-1),tail whose endpoint equals the
    left endpoint of n, a' >= amin(b,e,s) (coefficient contracting), 0<m<n. Backward search,
    e up to E_MAX (far beyond k(n))."""
    out = set()
    for s in (0, 1):
        left = (1,) if s == 0 else (1, 2, 1)
        wl, y = word(n, len(left))
        if wl != left:
            continue
        # tail backward from y
        if (8 * y - 1) % 3: continue
        p = (8 * y - 1) // 3  # value before exponent-3 step
        if s == 1:
            if (2 * p - 1) % 3: continue
            p = (2 * p - 1) // 3
            if (2 * p - 1) % 3: continue
            p = (2 * p - 1) // 3
        u = p; b = 1
        while True:
            # u = value after the e-step, with b-1 twos following
            if u % 3 == 1:
                for e in range(2, E_MAX + 1, 2):
                    x = (2 ** e * u - 1) // 3  # integral since u=1 mod 3 and 2^e=1 mod 3
                    ap = 0
                    while (2 * x - 1) % 3 == 0:
                        x = (2 * x - 1) // 3; ap += 1
                        if ap >= amin(b, e, s) and 0 < x < n:
                            out.add((s, b, e, ap, x))
            if (4 * u - 1) % 3: break
            u = (4 * u - 1) // 3; b += 1
    return out

def note_templates(n):
    """Finite search as stated in Theorem 3 and (12)-(13) of the note (re-implemented)."""
    out = set()
    if n == 1: return out
    k = (n - 1).bit_length() - 2
    B = v3(n) if n % 3 == 0 else 0
    for e in range(2, k + 1, 2):
        h = (2 ** e + 2) // 3
        b = B - v3(e - 1)
        if b < 1: continue
        for s in (0, 1):
            f = family(b, e, s)
            if n % f['d'] != f['r']: continue
            if f['a'] > k: continue
            if (f['J'] * n + h * 3 ** b) % f['Q']: continue
            z = n // 3 ** b
            Z = f['J'] * z + h
            Amax = v3(Z)
            for ap in range(f['a'], Amax + 1):
                m = 2 ** ap * Z // 3 ** ap - 1
                out.add((s, b, e, ap, m))
            # adjacent sources: T(m_{a'+1}) = m_{a'}
            for ap in range(f['a'], Amax):
                ok(T(2 ** (ap + 1) * Z // 3 ** (ap + 1) - 1) == 2 ** ap * Z // 3 ** ap - 1, "T(m_{a'+1})=m_a'")
    return out

N3 = 400000
agree = 0; with_templates = 0; total_pairs = 0; maxe = 0
for n in range(3, N3, 2):
    A = brute_templates(n); Bn = note_templates(n)
    ok(A == Bn, "Theorem 3 mismatch at n=%d: brute %s note %s" % (n, sorted(A), sorted(Bn)))
    agree += 1
    if A:
        with_templates += 1; total_pairs += len(A)
        maxe = max(maxe, max(z[2] for z in A))
        for (s, b, e, ap, m) in A:
            k = (n - 1).bit_length() - 2
            ok(e <= ap <= k, "e<=a'<=k(n)")
report.append("Theorem 3 (finite membership search e<=k(n), b=nu3(n)-nu3(e-1), a<=a'<=A_max): identical to brute-force backward search with e<=%d on all odd n<%d (%d sources; %d have templates, %d template pairs; max e seen %d): PASS" % (E_MAX, N3, agree, with_templates, total_pairs, maxe))

# ---- Section 5: the e=8, b=2, s=0 family ----
f = family(2, 8, 0)
ok((f['h'], f['t'], f['a']) == (86, 0, 16), "h,t,a")
ok((f['n0'], f['d'] * f['Q'], f['m0'], f['d'] * f['K']) == (20241207, 1549681956, 14024703, 1073741824), "progression constants")
ok(T(20241207) == 30361811 and (3 * 1549681956) // 2 == 2324522934, "endpoint progression")
vals = path(14024703, 19)
ok(vals[-1] == 30361811, "right path endpoint")
ok(max(vals) == 9211998293, "peak 9,211,998,293 at v=0")
def R0(n):
    fl = 0; p = 1
    while p * 3 <= n: p *= 3; fl += 1
    return max(130 * (n + 1), (64 * n * 4 ** fl) // 3 ** fl + 21)
cntv = 0
for v in list(range(0, 3000)) + [random.randrange(10 ** 9) for _ in range(200)]:
    n = 20241207 + 1549681956 * v; m = 14024703 + 1073741824 * v
    pr = path(m, 19); pl = path(n, 1)
    ok(pr[-1] == pl[-1], "common endpoint v=%d" % v)
    ok(word(m, 19)[0] == (1,) * 16 + (8, 2, 3), "word v=%d" % v)
    ok(max(pr) == (4096 * n) // 9 + 85 and 9 * (max(pr) - 85) == 4096 * n, "peak formula")
    ok(max(pr + pl) <= R0(n), "budget R0 v=%d" % v)
    ok(n - m == 6216504 + 475940132 * v, "height difference")
    ok(v3(n) == 2, "ternary layer 2")
    cntv += 1
report.append("Section 5 family n=20241207+1549681956v, m=14024703+2^30 v: %d parameter values (v<3000 plus 200 random v<1e9): words (1) and (1^16,8,2,3), common endpoint, peak (4096/9)n+85 (9,211,998,293 at v=0), R0 budget, height difference, nu3(n)=2, clock 1-19=-18: PASS" % cntv)
# no incoming edge for sources divisible by 3
ok(all(((2 ** a * n - 1) % 3 != 0) for n in (20241207,) for a in range(1, 30)), "no predecessor")
# the e=4,b=1,s=1 family
f = family(1, 4, 1)
ok((f['n0'], f['d'] * f['Q'], f['m0'], f['d'] * f['K']) == (45243, 69984, 42367, 65536) and v3(45243) == 2, "e=4 family")
ok(word(45243, 3)[1] == 76349 and word(42367, len(f['right']))[1] == 76349, "e=4 endpoint")
report.append("e=4,b=1,sigma=1 family 45243+69984v -> 76349+118098v <- 42367+65536v, layer nu3=2: PASS")

# ---- R0 <= 64 n^{log_3 4} + 21 for n>=27 (spot check), R_* and K_* elementary inequalities ----
bad = [n for n in range(27, 200001, 2) if R0(n) > 64 * n ** (log(4) / log(3)) + 21 + 1e-6 * n]
ok(not bad, "R0 real-exponent bound")
report.append("R0(n) <= 64 n^(log_3 4)+21 for odd 27<=n<=200001: PASS (float check with tiny tolerance)")

# ---- Chain-homotopy identities (18) on a toy reduction using only the new templates ----
# D = Z[eps]/(eps^2) elements as (c0,c1); vectors as dict key->(c0,c1)
def mul(x, y): return (x[0] * y[0], x[0] * y[1] + x[1] * y[0])
def qp(k): return (1, k)
def add(u, v, c=(1, 0)):
    w = dict(u)
    for k, a in v.items():
        b = mul(c, a); o = w.get(k, (0, 0)); nv = (o[0] + b[0], o[1] + b[1])
        if nv == (0, 0): w.pop(k, None)
        else: w[k] = nv
    return w
def d_eps(u):  # edges E_n -> V_n - q V_T(n)
    out = {}
    for n, a in u.items():
        out = add(out, {n: a}); out = add(out, {T(n): mul((-1, -1), a)})
    return out
cache = {}
def resolve(n):
    if n in cache: return cache[n]
    A = note_templates(n)
    if not A:
        cache[n] = (n, 0, {}); return cache[n]
    s, b, e, ap, m = min(A, key=lambda z: (z[4], z[3]))
    left = (1,) if s == 0 else (1, 2, 1)
    right = (1,) * ap + (e,) + (2,) * (b - 1) + ((3,) if s == 0 else (1, 1, 3))
    def col(x, L):
        c = {}
        for i in range(L):
            c = add(c, {x: qp(i)}); x = T(x)
        return c
    j = len(left) - len(right)
    Bn = add(col(n, len(left)), col(m, len(right)), mul((-1, 0), qp(j)))
    ok(d_eps(Bn) == add({n: (1, 0)}, {m: (-1, -j)}), "identity (1) at n=%d" % n)
    r, k, h = resolve(m)
    H = add(Bn, h, qp(j))
    cache[n] = (r, j + k, H); return cache[n]
def Hmap(v):
    out = {}
    for n, a in v.items(): out = add(out, resolve(n)[2], a)
    return out
def Qmap(v):
    out = {}
    for n, a in v.items():
        r, k, _ = resolve(n); out = add(out, {r: mul(a, qp(k))})
    return out
def Fmap(u): return add(u, Hmap(d_eps(u)), (-1, 0))
nid = 0; nontriv = 0
for n in range(1, 60001, 2):
    V = {n: (1, 0)}
    r = resolve(n)
    if r[0] != n: nontriv += 1
    ok(d_eps(Hmap(V)) == add(V, Qmap(V), (-1, 0)), "d H = I - Q")
    ok(Qmap(Qmap(V)) == Qmap(V), "Q^2=Q"); ok(Hmap(Qmap(V)) == {}, "HQ=0")
    E = {n: (1, 0)}
    ok(d_eps(Fmap(E)) == Qmap(d_eps(E)), "dF = Qd"); ok(Fmap(Fmap(E)) == Fmap(E), "F^2=F")
    ok(Fmap(Hmap(V)) == {}, "FH=0")
    nid += 6
report.append("Identities (1) and (18) (d_eps H=I-Q, Q^2=Q, HQ=0, d_eps F=Q d_eps, F^2=F, FH=0) over Z[eps]/(eps^2) for a toy retraction using only all-even template moves, on basis vectors for all odd n<=60001 (%d non-root sources): %d identity checks PASS" % (nontriv, nid))

print("\n".join(report))
print("elapsed %.1fs" % (time.time() - t0))
