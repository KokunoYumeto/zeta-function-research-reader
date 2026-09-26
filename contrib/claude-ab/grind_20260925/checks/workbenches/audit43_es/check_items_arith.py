#!/usr/bin/env python3
"""Independent arithmetic checks for README items 4, 6, 7, 14, 21, 26
(erdos-straus-foundation @ d20b32e). My own code; exact integers except
the explicitly high-precision cosine sums in item 6 (mpmath, 60 digits).
"""
import sys, time, itertools
from math import gcd, isqrt, prod
from fractions import Fraction
from sympy import isprime, primerange, factorint, divisors, totient, legendre_symbol, jacobi_symbol
import mpmath

T0 = time.time()
def log(*a):
    print(*a); sys.stdout.flush()

HARD = {1, 121, 169, 289, 361, 529}
def hard(p): return p % 840 in HARD

N_SPF = 1_000_001
spf = list(range(N_SPF))
for i in range(2, isqrt(N_SPF) + 1):
    if spf[i] == i:
        for j in range(i * i, N_SPF, i):
            if spf[j] == j:
                spf[j] = i
def fac(n):
    if n < N_SPF:
        f = {}
        while n > 1:
            q = spf[n]; f[q] = f.get(q, 0) + 1; n //= q
        return f
    return factorint(n)
def divs_from(f):
    ds = [1]
    for q, e in f.items():
        ds = [d * q ** k for d in ds for k in range(e + 1)]
    return ds
def tau(f): return prod(e + 1 for e in f.values())

# =====================================================================
log("== ITEM 4: square-source closed sets (es-turn04-square-expansion) ==")
def sigma(q): return 1 if q % 4 == 3 else 3
cycles = {4201: [61, 137, 1153, 383, 191], 12601: [409, 3457, 5743, 2293, 487], 26209: [661, 881, 7213, 5981, 5519]}
exits = {4201: (61, 1462, 43), 12601: (409, 5911, 23), 26209: (661, 11014, 5507)}
for p, cyc in cycles.items():
    ok = hard(p) and isprime(p)
    for i, q in enumerate(cyc):
        nq = cyc[(i + 1) % len(cyc)]
        A1 = (p + sigma(q) * q) // 4
        ok &= isprime(q) and legendre_symbol(q, p) == -1 and (p + sigma(q) * q) % 4 == 0 and A1 % nq == 0
        ok &= 81 * sigma(q) * q >= 3 * p   # the height condition of thm:five
    q, A3, out = exits[p]
    ok &= (p + 9 * sigma(q) * q) == 4 * A3 and A3 % out == 0 and isprime(out) and legendre_symbol(out, p) == -1 and out not in cyc and A3 < p
    log(f"p={p}: cycle {cyc} canonical edges, types and multiplier-9 exit {out} | {A3}: {ok}")

def item4_graph(p):
    V = [q for q in primerange(3, p) if legendre_symbol(q, p) == -1]
    succ = {}
    for q in V:
        s = set()
        for t in (1, 3, 5, 7, 9):
            R = sigma(q) * q * t * t
            if R >= 3 * p: break
            A = (p + R) // 4
            assert (p + R) % 4 == 0 and legendre_symbol(A % p, p) == -1
            nr = [r for r in fac(A) if legendre_symbol(r, p) == -1]
            assert nr and all(r != q for r in nr)
            s.update(nr)
        succ[q] = s
    return V, succ
def min_closure(V, succ, cap=6):
    worst = cap
    for q in V:
        seen = {q}; stack = [q]
        while stack and len(seen) < cap:
            x = stack.pop()
            for y in succ[x]:
                if y not in seen:
                    seen.add(y); stack.append(y)
                    if len(seen) >= cap: break
        worst = min(worst, len(seen))
    return worst
LIM4 = 40000
hp = [p for p in primerange(1009, LIM4) if hard(p)]
bad = []
for p in hp:
    V, succ = item4_graph(p)
    if min_closure(V, succ) < 6:
        bad.append(p)
log(f"hard primes 1009<=p<{LIM4}: {len(hp)}; primes with a closed set of <=5 vertices under ports t in {{1,3,5,7,9}}: {bad} (theorem: none)")

# =====================================================================
log("\n== ITEM 6: complete-shell spectral bounds (es-turn06-full-shell) ==")
def shell_data(p, a):
    R = 4 * a - p
    fa = fac(a)
    ds = [d for d in divs_from(fa)] + [p * d for d in divs_from(fa)]
    c = {}
    for d in ds:
        g = d % R; c[g] = c.get(g, 0) + 1
    T = sum(c[g] * c.get((-g) % R, 0) for g in c)
    En = sum(v * v for v in c.values())
    return R, fa, ds, c, T, En
p = 944329
log("944329 hard:", hard(p), isprime(p), " 944329 mod 840 =", p % 840)
R, fa, ds, c, T, En = shell_data(p, 236094)
log(f"a=236094: R={R}, a={fa}, #divisors of pa={len(ds)}, T_a={T} (src 60), collision energy={En} (src 132), principal^2={len(ds)**2} (src 2304)")
# character coordinates: 5 generates U(47); chi(5)=zeta_23
ind = {}
x = 1
for k in range(46):
    ind[x] = k; x = x * 5 % 47
assert len(ind) == 46
C = [0] * 23
for d in ds:
    C[ind[d % 47] % 23] += 1
Q = [sum(C[i] * C[(i + j) % 23] for i in range(23)) for j in range(23)]
log("C coefficients:", C)
log("Q_0..Q_11:", Q[:12], "(src 192,187,176,159,138,116,92,70,50,33,21,14)")
mpmath.mp.dps = 60
def Qat(m):
    return mpmath.mpf(Q[0]) + 2 * sum(Q[j] * mpmath.cos(2 * mpmath.pi * m * j / 23) for j in range(1, 12))
q1, q2 = Qat(1), Qat(2)
log(f"Q(zeta)={mpmath.nstr(q1, 20)} (src in (1009,1010)); Q(zeta^2)={mpmath.nstr(q2, 20)} (src in (24,25))")
lb3 = (2 * q1 - 732) / 23; lb5 = (2 * (q1 + q2) - 732) / 23
log(f"three-mode bound {mpmath.nstr(lb3, 12)}, five-mode bound {mpmath.nstr(lb5, 12)} (>58, so T_a>=60 by 4|T_a); Q_0 = E + T: {Q[0] == En + T}")
Ls = Fraction(8 * tau(fa) ** 2, int(totient(47))) - En
log(f"principal-only L_a at R=47: {Ls} (src -732/23)")
R, fa, ds, c, T, En = shell_data(p, 236098)
B = sorted({pow(13, k, 63) * s % 63 for k in range(12) for s in (1, 62)})
cos = {}
for g, v in c.items():
    key = min((g * b) % 63 for b in B)
    cos[key] = cos.get(key, 0) + v
log(f"a=236098: R={R}, T_a={T} (src 8), energy={En} (src 16), B={B}, coset masses={sorted(cos.values(), reverse=True)} (src 8,8,0 with 3 cosets)")

p = 87481
log("87481:", hard(p), isprime(p))
occ = 0; posL = 0; nsh = 0; nonmult4 = 0
for a in range(p // 4 + 1, (p + 1) // 2):
    if 4 * a <= p or 2 * a >= p: continue
    R, fa, ds, c, T, En = shell_data(p, a)
    nsh += 1
    L = Fraction(8 * tau(fa) ** 2, int(totient(R))) - En
    if L > 0: posL += 1
    if T > 0: occ += 1
    if T % 4: nonmult4 += 1
log(f"p=87481: first-half shells={nsh} (src 21870); shells with L_a>0: {posL} (src 0); occupied shells (T_a>0): {occ} (src 34); T_a not divisible by 4: {nonmult4}")

# principal-only census on hard primes through 2*10^6
t6 = time.time()
Rlist = [R for R in range(3, 2_000_000, 4) if totient(R) < 960]
misses = []; nh = 0
for p in primerange(1009, 2_000_001):
    if not hard(p): continue
    nh += 1
    hit = False
    for R in Rlist:
        if R >= p: break
        a = (p + R) // 4
        fa = fac(a); ta = tau(fa)
        phi = int(totient(R))
        if phi >= 4 * ta: continue
        Rr, fa, ds, c, T, En = shell_data(p, a)
        if Fraction(8 * ta * ta, phi) - En > 0:
            hit = True; break
    if not hit: misses.append(p)
log(f"hard primes <=2e6: {nh} (src 4519); residuals with phi(R)<960: {len(Rlist)} (src 311, max {max(Rlist)}); principal-only misses: {misses} (src 87481,196561,944329,1915201); {time.time()-t6:.0f}s")

# =====================================================================
log("\n== ITEM 7: pointwise localization (es-turn06b) ==")
def nu(p):
    n = 2
    while legendre_symbol(n, p) != -1: n += 1
    return n
def mp_(p):
    m = 3
    while legendre_symbol(m % p, p) != -1: m += 4
    return m
ok = True
for p in primerange(17, 200000):
    if p % 8 != 1: continue
    n = nu(p)
    ok &= isprime(n) and n * n <= p and mp_(p) <= p - 2 * n
log("nu_p prime, nu_p^2<=p, m_p<=p-2nu_p for all primes p=1 mod 8 below 2e5:", ok)
stats = dict(M=0, E=0, Eend=0, eq_M5=0, eq_E6=0)
viol = []
for p in primerange(17, 6000):
    if p % 8 != 1: continue
    n = nu(p); m = mp_(p); J = (m + 1) // 4
    has3mod4 = any(q % 4 == 3 for q in fac(p + 1))
    for a in range(p // 4 + 1, (p + 1) // 2):
        if not (p < 4 * a and 2 * a < p): continue
        R = 4 * a - p
        for u in divs_from(fac(a * a)) if a * a < N_SPF else divisors(a * a):
            g = gcd(a, u); h, r, s = g * g // u, u // g, a // g
            if (p + 4 * u) % R == 0 and r < s:     # middle, ordered r<s
                stats['M'] += 1
                lam = (r + s) // R; j = h * r * lam; Qv = 4 * j - 1
                c1 = Qv * s == p * lam + r and Qv * R == p + 4 * h * r * r and Qv < p and legendre_symbol(Qv % p, p) == -1
                c2 = (4 * J - 1) * a <= J * (p + J)
                if (4 * J - 1) * a == J * (p + J): stats['eq_M5'] += 1
                if hard(p): c2 &= 11 * a <= 3 * (p + 3)
                if not (c1 and c2): viol.append(('M', p, a, u))
            if (4 * u + 1) % R == 0:                   # exterior
                stats['E'] += 1
                kap = (p * r + s) // R; delta = kap - r
                D = (r + kap) // s; Hh = h * delta * delta
                okE = (r + kap) % s == 0 and D == (4 * u + 1) // R and (Hh + 1) % D == 0 and delta > 0
                b = (Hh + 1) // D; gg = p - 2 * a
                okE &= s * D == 2 * r + delta and p == h * s * s * D - b and gg == h * s * delta - b
                okE &= Fraction(p) == 2 * gg + Fraction(gg * gg, b) + Fraction((gg + b) ** 2, b * Hh)
                okE &= legendre_symbol(h % p, p) == -1 and h >= n
                okE &= 2 * n * (p + 1) <= (2 * n + 1) * (gg + 1) ** 2
                if 2 * n * (p + 1) == (2 * n + 1) * (gg + 1) ** 2: stats['eq_E6'] += 1
                if not has3mod4:
                    stats['Eend'] += 1
                    okE &= 2 * n * (p + 2) < (n + 1) * (gg + 2) ** 2
                okE &= D <= ((p + 3) ** 2 + 4 * n) // (12 * n)
                if hard(p): okE &= 22 * (p + 1) <= 23 * (gg + 1) ** 2 and D <= ((p + 3) ** 2 + 44) // 132
                if not okE: viol.append(('E', p, a, u))
log(f"primes p=1 mod 8 below 6000: middle states (r<s)={stats['M']}, exterior states={stats['E']}, exterior states at primes with no 3 mod 4 factor of p+1={stats['Eend']}; equality cases (M5)={stats['eq_M5']}, (E6)={stats['eq_E6']}; violations: {viol[:5]} (count {len(viol)})")
for (p, a, u, trip) in [(1009, 276, 9, None), (1009, 253, 5819, None), (41, 18, 54, None), (2521, 636, 8, None)]:
    R = 4 * a - p
    log(f"  example p={p},a={a},u={u}: R={R}, E-gate {(4*u+1)%R==0}, M-gate {(p+4*u)%R==0}")
p = 2521
log("p=2521: nu,m =", nu(p), mp_(p), "; p^2+44 =", factorint(p * p + 44), "; divisors <p that are 31 mod 44:", [d for d in divisors(p * p + 44) if d < p and d % 44 == 31])

# =====================================================================
log("\n== ITEM 14: fixed-target cofactor capacity (es-turn07-capacity-completion) ==")
nbad = 0; nfin = 0; neq = 0; maxratio = 0
for t in range(1, 81):
    for j in range(1, 4001):
        h = 4 * j - 1
        if h <= t: continue
        A = [W for W in divisors(j * j) if W % h == t % h]
        can = [W for W in A if W == t]
        comp = [W for W in A if W == 4 * t * j]
        fin = [W for W in A if W != t and W != 4 * t * j]
        if bool(can) != (j * j % t == 0) or bool(comp) != (j % (4 * t) == 0): nbad += 1
        for W in fin:
            nfin += 1
            n_ = (W - t) // h; V = j * j // W; l = j - 4 * n_ * V
            w = Fraction(l * l, V)
            okf = (W - t) % h == 0 and l >= 1 and 4 * l + 2 <= t and w.denominator == 1 and n_ == Fraction(t - w, 4 * l + 1) and h <= t * t - 3 * t + 1
            if not okf: nbad += 1
            if h == t * t - 3 * t + 1:
                neq += 1
                if not (w == 1 and n_ == 1 and t == 4 * l + 2): nbad += 1
        if h > max(t, t * t - 3 * t + 1) and len(A) != (j * j % t == 0) + (j % (4 * t) == 0): nbad += 1
log(f"t<=80, j<=4000, h=4j-1>t: finite words={nfin}, equality cases h=t^2-3t+1: {neq}, violations of the classification/bound/count: {nbad}")
t, j = 289, 1224
log("t=289,j=1224: A =", [W for W in divisors(j * j) if W % (4 * j - 1) == t])
p = 825241; a, R, u, h, r, s, kap = 206321, 43, 2240439739, 19, 10859, 1, 208402140
okx = isprime(p) and hard(p) and 4 * a - p == R and (4 * u + 1) % R == 0 and a == h * r * s and u == h * r * r and kap == (p * r + s) // R and h - R == -24
log(f"example (17) p=825241: E state valid, alpha=h-R=-4*6: {okx}; capacity box of j=5 in class 6 mod 19: {[W for W in divisors(25) if W % 19 == 6]}")
ok19 = all((1447321 + 2131080 * n) % 840 == 1 for n in range(50))
p = 1447321 + 3 * 2131080
a, R, u, h, r = 1960155, 59, 89353665675, 43, 45585
okx = isprime(p) and p == 7840561 and 4 * a - p == R and (4 * u + 1) % R == 0 and a == h * r and u == h * r * r and h - R == -16
log(f"example (19): progression 1 mod 840: {ok19}; n=3 gives p={p} prime and valid E state with alpha=-16: {okx}; A_4(11) = {[W for W in divisors(121) if W % 43 == 4]}")

# =====================================================================
log("\n== ITEM 21: original-divisor descent, nine-word boundary (es-turn07-divisor-descent) ==")
def K_(n):
    return prod(q ** ((e + 1) // 2) for q, e in fac(n).items()) if n > 1 else 1
nsrc = 0; mism = 0; nine_fail = 0; other_empty = 0; other_src = 0; strict_fail = 0
for p in primerange(13, 2600):
    if p % 4 != 1: continue
    for a in range(p // 4 + 1, (p + 1) // 2):
        if not (p < 4 * a and 2 * a < p): continue
        R = 4 * a - p
        for u in divs_from(fac(a * a)):
            for ch, G in (('E', 4 * u + 1), ('M', p + 4 * u)):
                if (G * G) % R or G % R == 0: continue   # proper trace sources only
                nsrc += 1
                d = R // gcd(R, G); m = 4 * K_(u)
                formula = {k for k in divisors(R) if k % d == 0 and k % m == 1}
                brute = set()
                for k in divisors(R):
                    Rp = R // k
                    if (p + Rp) % 4: continue
                    ap = (p + Rp) // 4
                    if (ap * ap) % u == 0 and G % Rp == 0 and Rp % 4 == 3:
                        brute.add(k)
                if formula != brute: mism += 1
                if any(k == 1 for k in brute): strict_fail += 1
                if 36 % u == 0:
                    if not brute: nine_fail += 1
                else:
                    other_src += 1
                    if not brute: other_empty += 1
log(f"proper trace sources, primes p=1 mod 4 below 2600: {nsrc}; formula K != brute-force return set: {mism}; k=1 returns (should be none): {strict_fail}")
log(f"nine words u|36: sources without a return: {nine_fail} (theorem: 0); other words: {other_src} sources, {other_empty} without a return")
for (p, a, u, ch) in [(1009, 321, 9, 'M'), (1108801, 279295, 5, 'M'), (51361, 14845, 5, 'M')]:
    R = 4 * a - p; G = p + 4 * u if ch == 'M' else 4 * u + 1
    d = R // gcd(R, G); m = 4 * K_(u)
    log(f"  p={p},a={a},u={u},{ch}: R={R}, trace gate {(G*G)%R==0}, d={d}, K={sorted(k for k in divisors(R) if k % d == 0 and k % m == 1)}")

# =====================================================================
log("\n== ITEM 26: least prime 1 mod 24 with first trace shell below first full shell ==")
def first_shells(p):
    atr = afull = None
    a = p // 4 + 1
    while 2 * a < p and afull is None:
        R = 4 * a - p
        for u in divs_from(fac(a * a)) if a * a < N_SPF else divisors(a * a):
            for G in (4 * u + 1, p + 4 * u):
                if (G * G) % R == 0 and atr is None: atr = a
                if G % R == 0 and afull is None: afull = a
        a += 1
    return atr, afull
first = None; cnt = 0
for p in primerange(25, 67370):
    if p % 24 != 1: continue
    cnt += 1
    atr, afull = first_shells(p)
    if atr is not None and (afull is None or atr < afull):
        first = (p, atr, afull); break
log(f"primes 1 mod 24 scanned: {cnt} (src 817 through 67369); first with A_tr<A_full: {first} (src 67369, 16849, 16850)")
p, a = 67369, 16849; R = 4 * a - p
E = sorted(u for u in divisors(a * a) if ((4 * u + 1) ** 2) % R == 0)
M = sorted(u for u in divisors(a * a) if ((p + 4 * u) ** 2) % R == 0)
log(f"p=67369,a=16849,R={R}, a={factorint(a)}: E trace words {E}, M trace words {M} (src 29,83,488621,1398467 / 1421,4067,69803,199781)")
a = 16850; R = 4 * a - p
log(f"a=16850,R={R}: full E words {[u for u in divisors(a*a) if (4*u+1)%R==0]}, full M words {[u for u in divisors(a*a) if (p+4*u)%R==0]} (src E 674, 84250)")
log("time %.0fs" % (time.time() - T0))
