#!/usr/bin/env python3
"""es50_checks.py -- independent checks for note 50_ (the owner's Erdos-Straus notes).

Written by claude-ab from the statements, not from the referee scripts.  Every certificate is
turned into an explicit triple (x, y, z) and tested exactly: 4xyz == p(xy + yz + zx).

Sections
  A  the support-zero core: no elementary j=1 certificate class contains a unit square
  B  quadratic-residue necessary conditions (eight shifts; p+5; visible-box shells)
  C  barriers (width-one versus group barrier; the example (433, 91))
  D  shell facts (non-coprime shells; R | p-1; the parity law for R | p^2-1)
  E  identities from the notes (29-channels; n = -c mod 4k-1 with c | k)
  F  locks and types (lock certificates for hard primes; Type II within R <= 107; complement squares)
Usage: python3 es50_checks.py [X]   (default X = 10**7)
"""
import sys, time, random
from math import gcd, isqrt
import numpy as np

X = int(float(sys.argv[1])) if len(sys.argv) > 1 else 10**7
T0 = time.time()
RESULTS = []
def check(label, name, ok, detail=""):
    RESULTS.append(ok)
    print(("PASS " if ok else "FAIL ") + label + " " + name + ("  [" + detail + "]" if detail else ""), flush=True)

# ---------------------------------------------------------------- sieve (smallest prime factor)
LIM = 3 * X + 64
spf = np.zeros(LIM + 1, dtype=np.int32)
for i in range(2, isqrt(LIM) + 1):
    if spf[i] == 0:
        blk = spf[i*i::i]
        blk[blk == 0] = i
        spf[i*i::i] = blk
z = np.nonzero(spf == 0)[0]
spf[z] = z
spf[0] = 0; spf[1] = 1
spf = spf.tolist()
def fac(n):
    f = {}
    while n > 1:
        q = spf[n]
        f[q] = f.get(q, 0) + 1
        n //= q
    return f
def isprime(n):
    return n >= 2 and spf[n] == n
def legendre(a, q):
    a %= q
    if a == 0: return 0
    return 1 if pow(a, (q - 1) // 2, q) == 1 else -1
def divisors_f(f):
    ds = [1]
    for q, e in f.items():
        ds = [d * q**k for d in ds for k in range(e + 1)]
    return ds
def is_solution(p, x, y, z):
    return x > 0 and y > 0 and z > 0 and 4 * x * y * z == p * (x * y + y * z + z * x)
def shell_solution(p, R, u, channel):
    """solution with x = a from the shell certificate: E (R | 4u+1) or M (R | u+a); u | a^2."""
    assert (p + R) % 4 == 0
    a = (p + R) // 4
    assert (a * a) % u == 0
    if channel == 'E':
        assert (4 * u + 1) % R == 0
        d = p * p * u
    else:
        assert (u + a) % R == 0
        d = p * u
    N = p * a
    assert (N + d) % R == 0 and (N + N * N // d) % R == 0
    return (a, (N + d) // R, (N + N * N // d) // R)

S840 = {1, 121, 169, 289, 361, 529}
P24 = [p for p in range(25, X, 24) if isprime(p)]          # primes p = 1 (mod 24), p < X
HARD = [p for p in P24 if p % 840 in S840]
print(f"# X = {X}: primes = 1 (mod 24): {len(P24)}; hard (mod 840 in S840): {len(HARD)}; sieve {time.time()-T0:.1f}s", flush=True)

# ================================================================ A. support-zero core
# A1: an elementary j=1 certificate class (R = 3 mod 4, u | m^2, n = -R mod 4m, n = -4u mod R, gcd(n,R)=1)
#     never contains a unit square modulo lcm(4m, R).  Exhaustive over small (R, m, u).
bad = 0; tested = 0
for R in range(3, 120, 4):
    for m in range(1, 60):
        if gcd(m, R) != 1: continue
        mod = 4 * m * R // gcd(4 * m, R)
        m2 = m * m
        us = [u for u in range(1, m2 + 1) if m2 % u == 0]
        squares = None
        for u in us:
            # class: n = -R (mod 4m), n = -4u (mod R)
            sols = [n for n in range(-R % (4 * m), mod, 4 * m) if (n + 4 * u) % R == 0 and gcd(n, mod) == 1]
            if not sols: continue
            if squares is None:
                squares = {(t * t) % mod for t in range(mod) if gcd(t, mod) == 1}
            tested += 1
            if any(n in squares for n in sols):
                bad += 1
check("A1", "no elementary j=1 certificate class contains a unit square (R<120, m<60)", bad == 0 and tested > 1000,
      f"{tested} classes, {bad} containing a square")

# A2: the support-zero core statement, one direction: a class that is a square mod 11, 19, 23 (and in S840)
#     lifts to squares modulo any P-smooth modulus (Hensel), so it meets no certificate class.
#     Spot check: every lift mod 9, 25, 49, 121, 16 of a unit square mod the prime (or 8) is a square.
ok = True
for q, k in ((3, 2), (5, 2), (7, 2), (11, 2), (19, 2), (23, 2)):
    qk = q**k
    sq = {(t * t) % qk for t in range(qk) if t % q}
    for r in range(1, q):
        if legendre(r, q) == 1:
            ok &= all(((r + q * j) % qk) in sq for j in range(q**(k - 1)))
sq16 = {(t * t) % 16 for t in range(1, 16, 2)}
ok &= all(x in sq16 for x in (1, 9))
check("A2", "Hensel: unit squares mod q (q = 3,5,7,11,19,23) and 1 mod 8 lift to squares mod q^2 and 16", ok)

# ================================================================ B. QR-type necessary conditions
# B1: the eight shifts (A1's Proposition 4.3, proved again here).  For every p = 1 (24), p < X, and every
#     odd prime q dividing a shift with (p/q) = -1, build the certificate and verify the triple.
def eight_shift_certificates(p):
    out = []
    for name, val in (("p+1", p + 1), ("p+2", p + 2), ("p+3", p + 3), ("p+4", p + 4),
                      ("p+7", p + 7), ("p+8", p + 8), ("2p+1", 2 * p + 1), ("3p+1", 3 * p + 1)):
        for q in fac(val):
            if q == 2 or legendre(p, q) != -1: continue
            if name in ("p+1", "p+4"):
                R = q
                if name == "p+1": out.append((name, q, shell_solution(p, R, (p + R) // 4, 'E')))
                else:              out.append((name, q, shell_solution(p, R, 1, 'M')))
            elif name in ("p+2", "p+8", "2p+1"):
                R = q if q % 8 == 7 else 3 * q
                a = (p + R) // 4
                if name == "p+2":  out.append((name, q, shell_solution(p, R, a // 2, 'E')))
                if name == "2p+1": out.append((name, q, shell_solution(p, R, 2 * a, 'E')))
                if name == "p+8":  out.append((name, q, shell_solution(p, R, 2, 'M')))
            elif name == "p+3":
                out.append((name, q, shell_solution(p, 3, q, 'E')))
            elif name == "p+7":
                a = (p + 7) // 4
                if q % 7 == 5:   out.append((name, q, shell_solution(p, 7, q, 'E')))
                elif q % 7 == 6: out.append((name, q, shell_solution(p, 7, a * q, 'M')))
                elif q % 7 == 3: out.append((name, q, shell_solution(p, 7, 2 * a * q, 'M')))
                else: raise AssertionError((p, q))
            elif name == "3p+1":
                N3 = (3 * p + 1) // 4
                h = N3 // q
                m = (h + 1) // 3
                R = (4 * q + 1) // 3
                assert N3 % q == 0 and (h + 1) % 3 == 0 and (4 * q + 1) % 3 == 0
                assert 4 * q * m - p == R
                out.append((name, q, shell_solution(p, R, q, 'E')))
    return out
t = time.time()
ncert = 0; nbad = 0; surv8 = []
for p in P24:
    cs = eight_shift_certificates(p)
    for name, q, (x, y, z) in cs:
        ncert += 1
        if not is_solution(p, x, y, z): nbad += 1
    if not cs: surv8.append(p)
check("B1", "eight shifts: every (shift, q) with (p/q) = -1 gives a verified solution, p = 1 (24), p < X",
      nbad == 0 and ncert > 0, f"{ncert} certificates, {nbad} bad, survivors of all eight: {len(surv8)}, {time.time()-t:.0f}s")
# B1b: survivors lie in S840 (they must, since the non-hard classes are solved by R = 3 or 7)
check("B1b", "every survivor of the eight shifts lies in a hard class mod 840", all(p % 840 in S840 for p in surv8),
      f"first survivors {surv8[:6]}")
# B1c: the shifts p+2, p+8, 2p+1 are not redundant: primes certified only by them
only = {"p+2": None, "p+8": None, "2p+1": None}
for p in P24:
    cs = eight_shift_certificates(p)
    names = {c[0] for c in cs}
    if len(names) == 1:
        n0 = next(iter(names))
        if n0 in only and only[n0] is None: only[n0] = p
    if all(v is not None for v in only.values()): break
check("B1c", "least p certified only by p+2, by p+8, by 2p+1", all(v is not None for v in only.values()), str(only))

# B2: p+5 on p = 9 (mod 40) (Theorem 4.1 of the referee pass C): the mu = 5 lock fires iff some prime
#     q | p+5 has (p/q) = -1; certificates verified.
def lock_a(p, mu, d):
    """lock (a): d odd, d | p+mu, d = -p (mod 4 mu): shell R = d, u = a/mu (E)."""
    return shell_solution(p, d, (p + d) // 4 // mu, 'E')
def lock_b(p, mu, h):
    """lock (b): h | N = (p+mu)/2, h = -1 (mod 4 mu): a = 2 mu e t, R = mu + 2e, u = mu^2 t (M)."""
    N = (p + mu) // 2
    e = N // h; t = (h + 1) // (4 * mu)
    a = 2 * mu * e * t; R = mu + 2 * e
    assert 4 * a - p == R
    return shell_solution(p, R, mu * mu * t, 'M')
def mu_lock(p, mu):
    N = (p + mu) // 2
    if (p + mu) % 2: return None
    f = fac(N)
    for d in sorted(divisors_f(f)):
        if d % 2 == 1 and (d + p) % (4 * mu) == 0 and d != p:
            return ('a', d, lock_a(p, mu, d))
        if (d + 1) % (4 * mu) == 0:
            return ('b', d, lock_b(p, mu, d))
    return None
viol = 0; ncert5 = 0; nbad5 = 0; n9 = 0
for p in range(9, X, 40):
    if not isprime(p): continue
    n9 += 1
    nr = any(legendre(p, q) == -1 for q in fac(p + 5) if q != 2 and q != 5)
    L = mu_lock(p, 5)
    if (L is not None) != nr: viol += 1
    if L is not None:
        ncert5 += 1
        if not is_solution(p, *L[2]): nbad5 += 1
check("B2", "p = 9 (mod 40): mu=5 lock fires <=> some q | p+5 has (p/q) = -1; certificates exact",
      viol == 0 and nbad5 == 0, f"{n9} primes, {viol} violations, {ncert5} certificates, {nbad5} bad")
# B2b: the same QR property on p = 121 (mod 840), and on p = 1, 361 (mod 840) with p = 4 (mod 9);
#      and its failure at p = 12601 (= 1 mod 840, p = 1 mod 9)
viol = 0; nclass = 0
for p in HARD:
    s = p % 840
    if s == 121 or (s in (1, 361) and p % 9 == 4):
        nclass += 1
        nr = any(legendre(p, q) == -1 for q in fac(p + 5) if q != 2 and q != 5)
        L = mu_lock(p, 5)
        if nr and L is None: viol += 1
        if L is not None and not is_solution(p, *L[2]): viol += 1
f12601 = fac(12601 + 5)
nr12601 = [q for q in f12601 if q != 2 and legendre(12601, q) == -1]
check("B2b", "p+5 QR property on 121 (840) and on 1, 361 (840) with p = 4 (9); fails at 12601",
      viol == 0 and isprime(12601) and nr12601 and mu_lock(12601, 5) is None,
      f"{nclass} primes checked; 12601+5 = {f12601}, non-residue factors {nr12601}")
# B2c: classes 169, 289, 529 are 9 (mod 40) classes (p = 4 mod 5), so B2 covers them
check("B2c", "169, 289, 529 are = 9 (mod 40); 121, 1, 361 are = 1 (mod 40)",
      all(s % 40 == 9 for s in (169, 289, 529)) and all(s % 40 == 1 for s in (121, 1, 361)))

# B3: the visible-box principle for prime shells R (referee pass C, Theorem 4.3), re-derived:
#     if the forced box of divisors of a^2 contains all squares mod R, then shell R is occupied iff
#     (p/R) = -1 or some prime q | p+R has (p/q) = -1.  Exact test on the good classes mod 10080.
def forced_box(c, R):
    lo = {}
    w = c + R
    v = 0
    while w % 2 == 0 and v < 12: w //= 2; v += 1
    t2 = v - 2
    if t2 > 0: lo[2] = min(t2, 3)                  # p mod 32 fixes v2(p+R) only up to 5
    if R != 3 and (c + R) % 3 == 0: lo[3] = 2 if (c + R) % 9 == 0 else 1
    for f in (5, 7):
        if R != f and (c + R) % f == 0: lo[f] = 1
    box = {1}
    for f, e in lo.items():
        box = {(b * pow(f, k, R)) % R for b in box for k in range(2 * e + 1)}
    return box
def occupied(p, R):
    a = (p + R) // 4
    if gcd(a, R) != 1: return False
    ds = divisors_f({q: 2 * e for q, e in fac(a).items()})
    tE = (-pow(4, -1, R)) % R; tM = (-a) % R
    for u in ds:
        r = u % R
        if r == tE: return ('E', u)
        if r == tM: return ('M', u)
    return False
classes10080 = [c for c in range(1, 10080, 24) if c % 840 in S840]
goodR = {}
for R in [q for q in range(3, 700) if isprime(q) and q % 4 == 3]:
    QR = {(i * i) % R for i in range(1, R)}
    g = [c for c in classes10080 if QR <= forced_box(c, R)]
    if g: goodR[R] = g
print("#   visible-box good prime shells (R: number of good classes mod 10080 out of 72):",
      {R: len(v) for R, v in goodR.items()}, flush=True)
viol = 0; ncert = 0; nbad = 0; tested = 0
for R, gl in goodR.items():
    gset = set(gl)
    for p in HARD:
        if p % 10080 not in gset or p == R: continue
        tested += 1
        crit = legendre(p, R) == -1 or any(legendre(p, q) == -1 for q in fac(p + R) if q != 2)
        oc = occupied(p, R)
        if bool(oc) != crit: viol += 1
        if oc:
            ncert += 1
            if not is_solution(p, *shell_solution(p, R, oc[1], oc[0])): nbad += 1
check("B3", "visible-box principle: occupied <=> (p/R) = -1 or NR factor of p+R, on the good classes",
      viol == 0 and nbad == 0 and set(goodR) >= {3, 7, 11, 19, 23, 31, 47, 59, 71, 311},
      f"good R: {sorted(goodR)}; {tested} (p,R) tests, {viol} violations, {ncert} certificates, {nbad} bad")

# B4: mu = 17 lock on its six classes mod 42840 (referee pass C, Theorem 4.2):
#     p = 361 or 529 (mod 840), p = 1 (mod 9), p mod 17 in {8, 15, 16}: lock fires <=> some q | p+17 has (p/q) = -1
viol = 0; n17 = 0; bad17 = 0
for p in HARD:
    if p % 840 in (361, 529) and p % 9 == 1 and p % 17 in (8, 15, 16):
        n17 += 1
        nr = any(legendre(p, q) == -1 for q in fac(p + 17) if q not in (2, 17))
        L = mu_lock(p, 17)
        if (L is not None) != nr: viol += 1
        if L is not None and not is_solution(p, *L[2]): bad17 += 1
check("B4", "mu = 17 lock on its six classes: fires <=> some q | p+17 has (p/q) = -1", viol == 0 and bad17 == 0 and n17 > 100,
      f"{n17} primes, {viol} violations, {bad17} bad certificates")
# B5: the record prime p* = 8803369 is certified by the new shifts p+2 (R = 223) and 2p+1 (R = 3*677 = 2031),
#     and by none of p+1, p+3, p+4, p+7 (its least occupied shell is R = 107)
cs = eight_shift_certificates(8803369)
names = sorted({c[0] for c in cs})
shells = sorted({4 * c[2][0] - 8803369 for c in cs})
check("B5", "p* = 8803369: certified exactly by the shifts p+2 and 2p+1", names == ["2p+1", "p+2"] and 223 in shells and 2031 in shells,
      f"shifts {names}, shells {shells}")

# ================================================================ C. barriers
def barrier_data(p, R):
    a = (p + R) // 4
    G = [x for x in range(1, R) if gcd(x, R) == 1]
    K = {1}
    frontier = [1]
    gens = [q % R for q in fac(a)]
    while frontier:
        nxt = []
        for k in frontier:
            for g in gens:
                y = (k * g) % R
                if y not in K: K.add(y); nxt.append(y)
        frontier = nxt
    width_one_kills = ((R - 1) not in K) and ((-4) % R not in K)
    K4 = set(K); frontier = list(K)
    while frontier:
        nxt = []
        for k in frontier:
            y = (k * 4) % R
            if y not in K4: K4.add(y); nxt.append(y)
        frontier = nxt
    group_kills = (R - 1) not in K4
    return width_one_kills, group_kills
w1, gb = barrier_data(433, 91)
check("C1", "(p, R) = (433, 91): width-one barrier kills, group barrier silent, shell empty",
      isprime(433) and w1 and not gb and not occupied(433, 91) and fac((433 + 91) // 4) == {131: 1})
# C2: width-one never wrong (it is a necessary condition) and separation count on p = 1 (24), p < 3000
sep = 0; wrong = 0
for p in [q for q in P24 if q < 3000]:
    for R in range(3, 3 * p, 4):
        if R % p == 0: continue
        oc = occupied(p, R)
        w1, gb = barrier_data(p, R)
        if oc and (w1 or gb): wrong += 1
        if w1 and not gb and not oc: sep += 1
check("C2", "width-one and group barriers are never violated; width-one strictly sharper (p = 1 (24) < 3000)",
      wrong == 0 and sep > 0, f"{sep} shells killed only by width-one")

# ================================================================ D. shell facts
# D1: non-coprime shell R = 7*73^2 at p = 73: a divisor d | N^2 with d = -N (mod R) exists, but no solution
p, R = 73, 7 * 73**2
a = (p + R) // 4; N = p * a; d = 4 * 73**3
brute = [(y, (N * y) // (R * y - N)) for y in range(N // R + 1, 2 * N // R + 1)
         if R * y - N > 0 and (N * y) % (R * y - N) == 0]
check("D1", "p = 73, R = 7*73^2: d = 4*73^3 divides N^2 and d = -N (mod R), yet 4/73 - 1/a has no 1/y+1/z",
      (N * N) % d == 0 and (d + N) % R == 0 and ((N + N * N // d) % R != 0) and brute == [],
      f"a = {a}, b = {(N + d)//R}, c = {(N + N*N//d)}/{R}")
# D2: R | p-1  =>  E_a = M_a ; D3: R | p^2-1 => |E_a| odd iff R | p+1  (all coprime shells, p = 1 (4) < 2000)
okE = True; okP = True; n1 = n2 = 0
for p in [q for q in range(5, 2000, 4) if isprime(q)]:
    for R in range(3, 3 * p, 4):
        if gcd(R, p) != 1: continue
        if (p * p - 1) % R: continue
        a = (p + R) // 4
        ds = divisors_f({q: 2 * e for q, e in fac(a).items()})
        E = {u for u in ds if (4 * u + 1) % R == 0}
        M = {u for u in ds if (u + a) % R == 0}
        if (p - 1) % R == 0:
            n1 += 1; okE &= (E == M)
        n2 += 1
        okP &= ((len(E) % 2 == 1) == ((p + 1) % R == 0))
check("D2", "R | p-1 implies E_a = M_a (coprime shells, p = 1 (4) < 2000)", okE, f"{n1} shells")
check("D3", "R | p^2-1 implies: |E_a| odd iff R | p+1", okP, f"{n2} shells")

# ================================================================ E. identities
# E1: the two 29-channels and the family n = -c (mod 4k-1), c | k:
#     4/n = 1/(kn) + 1/(k(n+c)/m) + 1/(kn(n+c)/(mc)),  m = 4k-1
bad = 0; n = 0
for nn in range(917, 10**6, 1276):
    x, y, zz = (nn + 11) // 4, (nn + 11) * (nn + 29) // 44, nn * (nn + 11) * (nn + 29) // 1276
    n += 1; bad += not is_solution(nn, x, y, zz)
for nn in range(1605, 10**6, 2204):
    x, y, zz = (nn + 19) // 4, (nn + 19) * (nn + 29) // 76, nn * (nn + 19) * (nn + 29) // 2204
    n += 1; bad += not is_solution(nn, x, y, zz)
check("E1", "n = 917 (1276) and n = 1605 (2204): the two 29-channel identities", bad == 0, f"{n} values of n < 10^6")
bad = 0; n = 0
for k in range(1, 40):
    m = 4 * k - 1
    for c in [c for c in range(1, k + 1) if k % c == 0]:
        for nn in range((-c) % m or m, 20000, m):
            if nn < 2: continue
            x, y, zz = k * nn, k * (nn + c) // m, k * nn * (nn + c) // (m * c)
            n += 1; bad += not is_solution(nn, x, y, zz)
check("E2", "family n = -c (mod 4k-1), c | k (contains n = 76 (mod 87): k = 22, c = 11)", bad == 0 and 87 == 4 * 22 - 1,
      f"{n} identities checked")
check("E3", "the class 917 (mod 1276) meets 76 (mod 87) exactly where n = 1 (mod 3)",
      all(((n % 87) == 76) == (n % 3 == 1) for n in range(917, 917 + 1276 * 60, 1276)))

# E4: the mu = 5, d = 31 lock channel: n = 429 (mod 620) gives 4/n = 1/a + 1/(as) + 5/(nas), a = (n+31)/4,
#     s = (n+5)/31; the class contains the prime 33289, which lies in the square core S840 x Q11 x Q19 x Q23
bad = 0; n = 0
for nn in range(429, 10**6, 620):
    a = (nn + 31) // 4; s_ = (nn + 5) // 31
    x, y, zz = a, a * s_, nn * a * s_ // 5
    n += 1; bad += not ((nn * a * s_) % 5 == 0 and is_solution(nn, x, y, zz))
p0 = 33289
incore = p0 % 840 in S840 and all(legendre(p0, q) == 1 for q in (11, 19, 23))
check("E4", "n = 429 (mod 620): mu=5, d=31 lock identity; contains the prime 33289 of the square core",
      bad == 0 and isprime(p0) and p0 % 620 == 429 and incore, f"{n} values of n < 10^6")
# E5: the owner's full-lock identity: the numerator is ps + p + mu (not ps + p + mu*s):
#     with s = (p+mu)/d:  p*s + p + mu = (p+mu)(p+d)/d  (identity in p for fixed d, mu)
from fractions import Fraction as Fr
ok = all(Fr(pp * Fr(pp + mu, d) + pp + mu) == Fr((pp + mu) * (pp + d), d) for pp in range(1, 60) for mu in (1, 3, 5, 29) for d in (3, 7, 11))
ok2 = any(Fr(pp * Fr(pp + mu, d) + pp + mu * Fr(pp + mu, d)) != Fr((pp + mu) * (pp + d), d) for pp in range(1, 60) for mu in (3, 5) for d in (7, 11))
check("E5", "full-lock numerator: ps+p+mu = (p+mu)(p+d)/d holds; the printed ps+p+mu*s does not", ok and ok2)
# E6: A_R(p) (ordered certificate count of shell R) is not a function of p mod 840: A_11 on p = 1 (mod 840)
def cert_count(p, R):
    a = (p + R) // 4
    if gcd(a, R) != 1: return None
    ds = divisors_f({q: 2 * e for q, e in fac(a).items()})
    E = sum(1 for u in ds if (4 * u + 1) % R == 0); M = sum(1 for u in ds if (u + a) % R == 0)
    return 2 * E + M
vals = sorted({cert_count(p, 11) for p in HARD if p % 840 == 1 and p < 20000})
check("E6", "A_11(p) takes several values on primes p = 1 (mod 840) below 20000", len(vals) >= 3, f"values {vals}")

# ================================================================ F. locks and types
# F1: every hard prime p < X has a lock certificate (lock (a) or (b)) for some odd mu
t = time.time()
nolock = []; maxR = 0
for p in HARD:
    found = None
    for mu in range(1, 4001, 2):
        L = mu_lock(p, mu)
        if L:
            found = (mu, L); break
    if not found:
        nolock.append(p); continue
    x, y, zz = found[1][2]
    if not is_solution(p, x, y, zz): nolock.append(p)
    maxR = max(maxR, 4 * x - p)
check("F1", "every hard prime p < X has a verified lock certificate (odd mu <= 4000)", not nolock,
      f"{len(HARD)} primes; failures {nolock[:5]}; largest shell among the certificates found (least mu first) {maxR}; {time.time()-t:.0f}s")
# F2: every p = 1 (24), p < X has an M-channel (Type II) certificate with R <= 107; p* is the only one needing 107
t = time.time()
need = {}
failsF2 = []
for p in P24:
    got = None
    for R in range(3, 108, 4):
        a = (p + R) // 4
        if gcd(a, R) != 1: continue
        ds = divisors_f({q: 2 * e for q, e in fac(a).items()})
        tM = (-a) % R
        for u in ds:
            if u % R == tM:
                got = (R, u); break
        if got: break
    if got is None:
        failsF2.append(p)
    else:
        if not is_solution(p, *shell_solution(p, got[0], got[1], 'M')): failsF2.append(p)
        need[got[0]] = need.get(got[0], []) + [p]
check("F2", "every p = 1 (24), p < X, has a verified Type II (M-channel) solution with R <= 107",
      not failsF2, f"failures {failsF2[:5]}; primes needing R = 107: {need.get(107, [])}; largest R used {max(need)}")
# F3: complement-square (M-channel with u = Q^2, Q | a, i.e. R | Q + a/Q): 97 is the least p = 1 (24) with none
def has_complement_square(p):
    for R in range(3, (p + 4) // 3 + 1, 4):
        a = (p + R) // 4
        if gcd(a, R) != 1: continue
        for Q in divisors_f(fac(a)):
            if (Q + a // Q) % R == 0:
                return (R, Q)
    return None
none24 = [p for p in P24 if p < 20000 and has_complement_square(p) is None]
nonehard = [p for p in none24 if p % 840 in S840]
check("F3", "complement-square certificates: least p = 1 (24) with none is 97; least hard one is 3361",
      none24[:1] == [97] and nonehard[:1] == [3361], f"none below 20000: {none24[:12]}...; hard: {nonehard[:5]}")

print(f"# total {len(RESULTS)} checks, {sum(RESULTS)} PASS, {len(RESULTS)-sum(RESULTS)} FAIL, {time.time()-T0:.0f}s")
