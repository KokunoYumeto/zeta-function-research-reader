#!/usr/bin/env python3
"""Quick independent checks: README items 2, 3, 8; results bench R02, R04, R05, R06, R08, R10;
X5, X6; ES-08 witness; ES-09 matrices, orbits and genus formulas; the classical mod-840 reduction.
My own code, exact arithmetic (cmath only for R02/X6 numerics)."""
import sys, time, itertools, cmath
from math import gcd, prod
from fractions import Fraction
import sympy as sp
from sympy import isprime, factorint, divisors, legendre_symbol, primerange

T0 = time.time()
def log(*a):
    print(*a); sys.stdout.flush()
def sigma(q): return 1 if q % 4 == 3 else 3
def gates(p, a, R):
    ds = divisors(a * a)
    return [u for u in ds if (4 * u + 1) % R == 0], [u for u in ds if (u + a) % R == 0], len(ds)

# ---- item 2: seven-vertex sink at p=2521
p = 2521; cyc = [11, 211, 683, 89, 17, 643, 113]
ok = True; allempty = True
for i, q in enumerate(cyc):
    A = (p + sigma(q) * q) // 4; R = sigma(q) * q
    nr = [r for r in factorint(A) if legendre_symbol(r, p) == -1]
    ok &= (p + R) % 4 == 0 and nr == [cyc[(i + 1) % 7]] and legendre_symbol(q, p) == -1
    E, M, nd = gates(p, A, R)
    allempty &= (not E and not M)
log(f"[item 2] p=2521 hard={p%840 in (1,121,169,289,361,529)}: canonical edges with a unique nonresidue factor around the 7-cycle: {ok}; both E/M gates empty at all 7 shells: {allempty}")
log("[item 2] p=2521 nevertheless has witnesses, e.g. shell a=636 (item 7): M-gate", (2521 + 4 * 8) % (4 * 636 - 2521) == 0)

# ---- item 3: constant-C6 triangle
p = 7510085481569082811681; tri = [31, 223, 307]
log(f"[item 3] p={p} prime (BPSW): {isprime(p)}, p mod 840 = {p % 840}")
ok = True; allempty = True; tot = 0
for i, q in enumerate(tri):
    A = (p + q) // 4
    f = factorint(A)
    nr = [r for r in f if legendre_symbol(r % p, p) == -1]
    ok &= q % 4 == 3 and (p + q) % 4 == 0 and nr == [tri[(i + 1) % 3]] and f[tri[(i + 1) % 3]] == 1
    E, M, nd = gates(p, A, q)
    tot += nd
    allempty &= (not E and not M)
log(f"[item 3] triangle 31->223->307->31: unique simple nonresidue successor at each vertex: {ok}; E/M empty at all three shells: {allempty}; divisor vectors examined: {tot} (src 1215)")
A9 = [(p + 9 * q) // 4 for q in tri]
log("[item 3] multiplier-9 sources have a nonresidue factor outside the triangle:",
    [any(legendre_symbol(r % p, p) == -1 and r not in tri for r in factorint(x)) for x in A9])

# ---- item 8: middle cutoff 4p >= 3t^2+6t-25 (p=1 mod 8) and hard version
viol = 0; nst = 0; eq = []
for p in primerange(17, 4000):
    if p % 8 != 1: continue
    hard = p % 840 in (1, 121, 169, 289, 361, 529)
    for a in range(p // 4 + 1, (p + 1) // 2):
        if not (p < 4 * a < 2 * p): continue
        R = 4 * a - p
        for u in divisors(a * a):
            if u < a and (u + a) % R == 0:
                g = gcd(a, u); h, r, s = g * g // u, u // g, a // g
                lam = (r + s) // R; j = h * r * lam; Q = 4 * j - 1; Aa = h * lam * lam
                nst += 1
                t = min(R, Q)
                if not (Fraction(p) == R * Q - Fraction((Q + 1) ** 2, 4 * Aa) and 4 * p >= 3 * t * t + 6 * t - 25): viol += 1
                if hard and not 4 * p >= 3 * t * t + 14 * t - 81: viol += 1
                if 4 * p == 3 * t * t + 6 * t - 25: eq.append(p)
log(f"[item 8] oriented middle states (u<a), p=1 mod 8 < 4000: {nst}; violations of p=RQ-(Q+1)^2/(4A), 4p>=3t^2+6t-25 (and hard 3t^2+14t-81): {viol}; equality primes: {sorted(set(eq))} (src 41)")

# ---- R02
z = cmath.exp(2j * cmath.pi / 6)
mins = min(abs(sum((1 if j == 3 else 0) * z ** (-m * j) for j in range(6)) + 2 * z ** (-m * ((3 - k) % 6))) for k in range(6) for m in range(6))
log(f"[R02] min over k,m of |Fourier value of delta_k| = {mins:.6f} (>0 means all nonzero; source: modulus of 1+2zeta^(-km) >= 1)")
# ---- R04
p, R = 8803369, 107; a = (p + R) // 4; b2, b3, b5 = 6, 21, 47176870
chk = [p % R, pow(b3, -1, R), b5 % R, p * a % R, b3 * b5 % R, a % R, (-b3 * b5) % R, 121 % R, pow(-b2 * b5, -1, R)]
log(f"[R04] p mod 107={chk[0]}, 21^-1={chk[1]}, b5={chk[2]}, pa={chk[3]}, b3b5={chk[4]}, a={chk[5]}, -b3b5={chk[6]}, 11^2={chk[7]}, (-b2b5)^-1={chk[8]} (src 51,51,35,35,93,93,14,14,27); (p+R)%4={(p+R)%4}; p prime: {isprime(p)}")
# ---- R05
def U(n):
    m = 3 * n + 1
    while m % 2 == 0: m //= 2
    return m
okR5 = all(3 * (4 * n + 1) + 1 == 4 * (3 * n + 1) for n in range(1, 2000))
okU = all(U(n) == U(4 ** j * n + (4 ** j - 1) // 3) for n in range(1, 4000, 2) for j in range(0, 8))
log(f"[R05] theta T = 4 theta: {okR5}; U(T^j n)=U(n) for odd n<4000, j<8: {okU}")
# ---- R06
Aset = {(35 * r + 11 * s + 33 * t) % 53 for r in range(-2, 3) for s in range(-2, 3) for t in range(-1, 2)}
Dset = set(range(53)) - Aset
DD = {(x - y) % 53 for x in Dset for y in Dset}
cover = {(x + 29) % 53 for x in Aset} | {(x + 23) % 53 for x in Aset}
log(f"[R06] |A|={len(Aset)}, D={sorted(Dset)} == {{23+42j}}: {Dset == {(23 + 42 * j) % 53 for j in range(10)}}, |D-D|={len(DD)}, 6 in D-D: {6 in DD}, (A+29)u(A+23)=C53: {len(cover) == 53}")
# ---- R08 with Lambda = A2 (Gram [[2,-1],[-1,2]]) and Lambda = Z^3
for G in (sp.Matrix([[2, -1], [-1, 2]]), sp.eye(3)):
    d = G.shape[0]
    Gl = sp.diag(G, G, G)
    I = sp.eye(d); Z0 = sp.zeros(d)
    Bd = sp.Matrix.hstack(I, I, I).T            # (x,x,x)
    Bk = sp.Matrix.hstack(sp.Matrix.vstack(I, -I, Z0), sp.Matrix.vstack(Z0, I, -I))   # g_i, P g_i
    GD = Bd.T * Gl * Bd; GK = Bk.T * Gl * Bk
    idx = abs(sp.Matrix.hstack(Bd, Bk).det())
    log(f"[R08] rank {d}: Gram(D)=3G {GD == 3*G}, Gram(K)=[[2G,-G],[-G,2G]] {GK == sp.Matrix(sp.BlockMatrix([[2*G, -G], [-G, 2*G]]))}, [L:D+K]={idx} == 3^d {idx == 3**d}")
# ---- R10
C2 = []
for bits in itertools.product((0, 1), repeat=4):
    if sum(bits) % 2 == 0:
        y = 0
        for i, b in enumerate(bits):
            if b: y ^= i
        C2.append((bits, y))
C3 = {tuple((i * x + j * yv) % 3 for x, yv in zip((1, 1, 1, 0), (1, 2, 0, 1))) for i in range(3) for j in range(3)}
H = {(tuple((3 * u_ + 2 * v_) % 6 for u_, v_ in zip(u, v)), y) for (u, y) in C2 for v in C3}
closed = all((tuple((a1 + a2) % 6 for a1, a2 in zip(k1, k2)), y1 ^ y2) in H for (k1, y1) in H for (k2, y2) in H)
qzero = all((sum(Fraction(5 * k * k, 6) for k in kk) + (1 if y else 0)) % 2 == 0 for kk, y in H)
costs = {}
for kk, y in H:
    cst = sum(Fraction(k * (6 - k), 6) for k in kk) + (1 if y else 0)
    costs[cst] = costs.get(cst, 0) + 1
log(f"[R10] |H|={len(H)}, subgroup: {closed}, q(H)=0 mod 2: {qzero}, cost multiplicities: {dict(sorted(costs.items()))} (src 0:1, 4:46, 6:25)")
# ---- X5, X6
log("[X5] powers of 289 mod 840:", [pow(289, k, 840) for k in range(6)], "(src 1,289,361,169,121,529; 289^3=169 != 839)")
import numpy as np
r_ = 6; Aab = [(a1, a2) for a1 in range(2) for a2 in range(3)]   # C2 x C3
basis = []
for a in Aab:
    for ch in Aab:
        W = np.zeros((r_, r_), dtype=complex)
        for xi, x in enumerate(Aab):
            val = cmath.exp(2j * cmath.pi * (ch[0] * x[0] / 2 + ch[1] * x[1] / 3))
            tgt = Aab.index(((a[0] + x[0]) % 2, (a[1] + x[1]) % 3))
            W[tgt, xi] = val
        basis.append(W.flatten())
Mx = np.array(basis)
log(f"[X6] Weyl operators on C[C2xC3]: rank of the 36 operators = {np.linalg.matrix_rank(Mx)} (expect 36); Gram = 6*I: {np.allclose(Mx.conj() @ Mx.T, 6 * np.eye(36))}")

# ---- ES-08 witness and ES-09 matrices / genus
p = 1201
log(f"[ES-08] 4/1201 = 1/310+1/1489240+1/9608: {Fraction(1,310)+Fraction(1,1489240)+Fraction(1,9608) == Fraction(4,1201)}; R=4*310-1201={4*310-1201}")
A1 = sp.Matrix([[1, 0, 0, 0], [6, 0, 1, 0], [-6, -1, -1, 0], [-2, 1, 0, 1]])
A2 = sp.Matrix([[1, 0, 0, 0], [0, 0, -1, 0], [-6, 1, 0, 0], [3, 0, 1, 1]])
Ai = sp.Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 1, 1, 0], [-1, 0, 0, 1]])
log(f"[ES-09] A1^3=I {A1**3 == sp.eye(4)}, A2^4=I {A2**4 == sp.eye(4)}, A1A2Ainf=I {A1*A2*Ai == sp.eye(4)}")
def perms(D):
    pts = [(x, y, z) for x in range(D) for y in range(D) for z in range(D)]
    idx = {v: i for i, v in enumerate(pts)}
    a1 = [idx[((6 + y) % D, (-6 - x - y) % D, (z - 2 + x) % D)] for (x, y, z) in pts]
    a2 = [idx[((-y) % D, (x - 6) % D, (z + 3 + y) % D)] for (x, y, z) in pts]
    ai = [idx[(x % D, (y + x) % D, (z - 1) % D)] for (x, y, z) in pts]
    return pts, a1, a2, ai
def cycles_in(perm, S):
    seen = set(); c = 0
    for s in S:
        if s in seen: continue
        c += 1; t = s
        while t not in seen:
            seen.add(t); t = perm[t]
    return c
res = []
for D in (1, 3, 5, 7, 9, 11, 13, 15):
    pts, a1, a2, ai = perms(D)
    n = len(pts)
    # check the monodromy relation on points: a1 a2 ainf = id (composition right to left as in source)
    comp_ok = all(a1[a2[ai[i]]] == i for i in range(n)) or all(ai[a2[a1[i]]] == i for i in range(n))
    # orbits
    seen = [False] * n; orbits = []
    for s in range(n):
        if seen[s]: continue
        orb = [s]; seen[s] = True; k = 0
        while k < len(orb):
            v = orb[k]; k += 1
            for pm in (a1, a2, ai):
                w = pm[v]
                if not seen[w]: seen[w] = True; orb.append(w)
        orbits.append(orb)
    gens = []
    for orb in orbits:
        S = set(orb)
        c1, c2, ci = cycles_in(a1, S), cycles_in(a2, S), cycles_in(ai, S)
        chi = c1 + c2 + ci - len(S)
        gens.append((len(S), Fraction(2 - chi, 2)))
    if D % 3:
        formula = [Fraction(5 * D**3 - 12 * D**2 - 17 * D + 24, 24)]
    else:
        formula = sorted([Fraction(5 * D**3 - 12 * D**2 - 81 * D + 216, 216), Fraction(5 * D**3 - 12 * D**2 - 9 * D + 27, 27)])
    res.append((D, comp_ok, sorted(gens), formula, sorted(g for _, g in gens) == formula))
for r in res:
    log(f"[ES-09] D={r[0]}: relation holds on points {r[1]}; orbits (size, genus) {[(s, str(g)) for s, g in r[2]]}; formula {[str(f) for f in r[3]]}; match {r[4]}")

# ---- classical mod-840 reduction via polynomial families
units = [c for c in range(840) if gcd(c, 840) == 1 and c % 24 == 1]
covered = {}
for A in range(1, 211):
    for B in range(1, 211):
        if 210 % (A * B): continue
        m = 4 * A * B
        # middle: R | A+B, p = -R mod 4AB
        for R in divisors(A + B):
            for c in units:
                if (c + R) % m == 0: covered.setdefault(c, ('M', A, B, R))
        # exterior: R | 840 odd, gcd(R, AB)=1, p=-R mod 4AB, p=-A/B mod R
        for R in divisors(105):
            if gcd(R, A * B) != 1: continue
            for c in units:
                if (c + R) % m == 0 and (c * B + A) % R == 0: covered.setdefault(c, ('E', A, B, R))
unc = sorted(set(units) - set(covered))
log(f"[840] classes c mod 840, gcd(c,840)=1, c=1 mod 24: {len(units)}; covered by a polynomial family with modulus | 840: {len(covered)}; uncovered: {unc} (squares mod 840: {sorted({x*x % 840 for x in range(840) if gcd(x,840)==1})})")
# sanity: each family identity on actual primes
bad = 0
for c, (ty, A, B, R) in covered.items():
    for p in [q for q in primerange(10000, 60000) if q % 840 == c][:5]:
        D = (p + R) // (4 * A * B)
        assert (p + R) % (4 * A * B) == 0
        if ty == 'M':
            C = (A + B) // R; t = (A * B * D, p * A * C * D, p * B * C * D)
        else:
            C = (A + p * B) // R; t = (A * B * D, A * C * D, p * B * C * D)
        if sum(Fraction(1, x) for x in t) != Fraction(4, p): bad += 1
log(f"[840] family identities fail on sample primes: {bad}")
log("time %.0fs" % (time.time() - T0))
