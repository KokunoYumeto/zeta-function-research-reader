#!/usr/bin/env python3
"""Referee 23: independent checks of the Erdos-Straus passages of the workbench reader (Section 1).
Written from the definitions only; imports no workbench or author code.
"""
import sys, math, time
from sympy import primerange, factorint, isprime, divisors

t0 = time.time()
def say(tag, ok, msg=""):
    print(("[PASS] " if ok else "[FAIL] ") + tag + (": " + msg if msg else ""))
    sys.stdout.flush()

def all_solutions(p):
    """All (x,y,z), x<=y<=z, with 4/p = 1/x+1/y+1/z, via (Ry-S)(Rz-S)=S^2 at each x (x in (p/4, 3p/4])."""
    sols = []
    for x in range(p // 4 + 1, (3 * p) // 4 + 1):
        R = 4 * x - p
        S = p * x
        if R <= 0:
            continue
        S2 = S * S
        for d in divisors(S2):
            if d > S:
                break
            if (d + S) % R or (S2 // d + S) % R:
                continue
            y = (d + S) // R
            z = (S2 // d + S) // R
            if y >= x:
                sols.append((x, y, z))
    return sols

def brute_solutions(p):
    """Plain brute force with a y-loop (used for small p as a cross-check of all_solutions)."""
    from fractions import Fraction
    sols = []
    for x in range(1, 3 * p + 1):
        r = Fraction(4, p) - Fraction(1, x)
        if r <= 0:
            continue
        # y >= x, 1/y >= r/2  -> y <= 2/r ; 1/y < r -> y > 1/r
        ylo = max(x, int(1 / r) + 1)
        yhi = int(2 / r)
        for y in range(ylo, yhi + 1):
            s = r - Fraction(1, y)
            if s > 0 and s.numerator == 1 and s.denominator >= y:
                sols.append((x, y, s.denominator))
    return sols

# ---------------------------------------------------------------- Thm 1.1(a)
for p in primerange(3, 120):
    a = sorted(all_solutions(p)); b = sorted(brute_solutions(p))
    if a != b:
        say("solution enumerator agrees with y-loop brute force", False, str(p)); break
else:
    say("solution enumerator agrees with y-loop brute force for all odd primes < 120", True)

nsol = 0; bad = []; maxratio = {1: (0, None), 3: (0, None)}
nsol400 = 0
for p in primerange(3, 1500):
    for (x, y, z) in all_solutions(p):
        nsol += 1
        if p < 400: nsol400 += 1
        exc = (p % 4 == 3 and (x, y, z) == ((p + 1) // 2, (p + 1) // 2, p * (p + 1) // 4))
        if not ((2 * x < p and x < y) or exc):
            bad.append((p, x, y, z))
        if not exc:
            r = x / p
            if r > maxratio[p % 4][0]:
                maxratio[p % 4] = (r, (p, x, y, z))
say("Thm 1.1(a): every solution at an odd prime p < 1500 has x < p/2 and x < y, except ((p+1)/2,(p+1)/2,p(p+1)/4) at p = 3 mod 4",
    not bad, f"{nsol} solutions checked; {nsol400} of them at primes < 400 (reader: 2,259)")
print("   largest x/p over non-exceptional solutions: p=1 mod 4:", maxratio[1], "; p=3 mod 4:", maxratio[3])

# largest x/p restricted to larger primes (to see the trend)
for lo in (100, 500, 1000):
    best = (0, None)
    for p in primerange(lo, 1500):
        if p % 4 != 1: continue
        for (x, y, z) in all_solutions(p):
            if x / p > best[0]:
                best = (x / p, (p, x, y, z))
    print(f"   p = 1 mod 4, {lo} < p < 1500: largest x/p = {best[0]:.4f} at {best[1]}")

# ---------------------------------------------------------------- Thm 1.1(c) for every odd prime with the range (p/4, p/2)
def shell_occupied(p, a):
    R = 4 * a - p
    a2 = a * a
    for u in divisors(a2):
        if (4 * u + 1) % R == 0 or (u + a) % R == 0:
            return True
    return False
okc = True; cnt = 0
for p in primerange(3, 3000):
    solvable = len(all_solutions(p)) > 0 if p < 700 else True
    occ = any(shell_occupied(p, a) for a in range(p // 4 + 1, (p + 1) // 2) if 2 * a < p)
    cnt += 1
    if occ != solvable:
        okc = False; print("   mismatch", p)
say("Thm 1.1(c) with the range p/4 < a < p/2 holds for EVERY odd prime (p = 3 mod 4 included; a=(p+1)/4 has R=1 and is occupied)",
    okc, f"{cnt} odd primes < 3000")
okr1 = all(shell_occupied(p, (p + 1) // 4) and 4 * ((p + 1) // 4) - p == 1 and 2 * ((p + 1) // 4) < p
           for p in primerange(3, 20000) if p % 4 == 3)
say("for every prime p = 3 mod 4 below 20000, the shell a=(p+1)/4 lies in (p/4,p/2), has R=1 and is occupied", okr1)

# ---------------------------------------------------------------- Thm 1.1(b) counts
def EM(p, a):
    R = 4 * a - p
    a2 = a * a
    E = [u for u in divisors(a2) if (4 * u + 1) % R == 0]
    M = [u for u in divisors(a2) if (u + a) % R == 0]
    return E, M

def ordered_pairs(p, a):
    """ordered (y,z) with 1/a+1/y+1/z = 4/p, by brute force over y"""
    from fractions import Fraction
    r = Fraction(4, p) - Fraction(1, a)
    if r <= 0: return None
    out = []
    ylo = int(1 / r) + 1
    yhi = int(2 / r)
    for y in range(ylo, yhi + 1):
        s = r - Fraction(1, y)
        if s > 0 and s.numerator == 1:
            z = s.denominator
            out.append((y, z))
            if z != y: out.append((z, y))
    return out

n1 = n2 = 0; okb = True; fixed = 0
for p in primerange(3, 260):
    for a in range(p // 4 + 1, p):
        E, M = EM(p, a)
        op = ordered_pairs(p, a)
        n1 += 1
        if len(op) != 2 * len(E) + len(M): okb = False
        if any(y == z for (y, z) in op):
            fixed += 1
            if 4 * a - p != 1: okb = False
say("Thm 1.1(b) count 2|E|+|M| = #ordered pairs, p < 260 odd prime, p/4 < a < p", okb, f"{n1} pairs (reader: 4,726); y=z in {fixed} cases (reader: 29)")
okb2 = True
for p in primerange(3, 120):
    for a in range(p // 4 + 1, 3 * p + 1):
        if a % p == 0: continue
        E, M = EM(p, a)
        op = ordered_pairs(p, a)
        n2 += 1
        if len(op) != 2 * len(E) + len(M): okb2 = False
say("Thm 1.1(b) for p < 120, p/4 < a <= 3p, p not dividing a", okb2, f"{n2} pairs (reader: 4,303)")
# shells of p=1 mod 12 below 700 in the old range [3h+1,9h]
nsh = sum(6 * ((p - 1) // 12) for p in primerange(13, 700) if p % 12 == 1)
print(f"   shells a in [3h+1,9h] for primes p = 1 mod 12 below 700: {nsh} (reader: 4,398)")

# ---------------------------------------------------------------- Prop 1.2 at p = 5 mod 12  (the 'generalised' claim)
def prop12_prediction(a):
    f = factorint(a)
    P1 = 1; P2 = 1
    for l, v in f.items():
        if l % 3 == 1: P1 *= 2 * v + 1
        elif l % 3 == 2: P2 *= 2 * v + 1
    return P1, P2

fails = []; ok_corr = True; ok_1mod12 = True; nm5 = n1m = 0
for p in primerange(5, 30000):
    if p % 4 != 1: continue
    a = (p + 3) // 4
    E, M = EM(p, a)
    P1, P2 = prop12_prediction(a)
    target2 = sorted(u for u in divisors(a * a) if u % 3 == 2)
    if p % 12 == 1:
        n1m += 1
        if not (sorted(E) == sorted(M) == target2 and len(E) == P1 * (P2 - 1) // 2):
            ok_1mod12 = False
    else:
        nm5 += 1
        if not (sorted(E) == sorted(M) == target2 and len(E) == len(M) == P1 * (P2 - 1) // 2):
            fails.append(p)
        # corrected statement: E = {u = 2 mod 3}, M = {u = 1 mod 3}, |E| = P1(P2-1)/2, |M| = P1(P2+1)/2,
        # unordered solutions with least denominator a: P1(3P2-1)/4
        target1 = sorted(u for u in divisors(a * a) if u % 3 == 1)
        unordered = len(E) + len(M) // 2
        if not (sorted(E) == target2 and sorted(M) == target1 and len(E) == P1 * (P2 - 1) // 2
                and len(M) == P1 * (P2 + 1) // 2 and (P1 * (3 * P2 - 1)) % 4 == 0 and unordered == P1 * (3 * P2 - 1) // 4):
            ok_corr = False
say("Prop 1.2 exactly as stated, primes p = 1 mod 12 below 3e4", ok_1mod12, f"{n1m} primes")
say("Prop 1.2 exactly as stated (E_a = M_a = {u = 2 mod 3}, |E_a|=|M_a|=P1(P2-1)/2) at primes p = 5 mod 12 below 3e4 -- EXPECTED TO FAIL",
    not fails, f"fails at {len(fails)} of {nm5} primes, first {fails[:6]}")
p = 5; a = 2; E, M = EM(p, a); print(f"   counterexample p=5, a=2: E_a={E}, M_a={M}; Prop 1.2 predicts E_a=M_a={{2}}, |E_a|=|M_a|=1")
p = 17; a = 5; E, M = EM(p, a); print(f"   counterexample p=17, a=5: E_a={E}, M_a={M}; Prop 1.2 predicts E_a=M_a={{5}}, |E_a|=|M_a|=1")
say("corrected form at p = 5 mod 12: E_a={u|a^2: u=2 mod 3}, M_a={u: u=1 mod 3}, |E|=P1(P2-1)/2, |M|=P1(P2+1)/2, unordered P1(3P2-1)/4",
    ok_corr, f"{nm5} primes")
# direct count of unordered solutions with least denominator a at p=5 mod 12 (independent of E/M)
okdir = True
for p in primerange(5, 700):
    if p % 12 != 5: continue
    a = (p + 3) // 4
    P1, P2 = prop12_prediction(a)
    n = sum(1 for (x, y, z) in all_solutions(p) if x == a)
    if n != P1 * (3 * P2 - 1) // 4: okdir = False
    if n == 3 * P1 * (P2 - 1) // 4: okdir = False  # the stated count must differ
say("direct enumeration at p = 5 mod 12 below 700: #solutions with least denominator (p+3)/4 is P1(3P2-1)/4, never 3P1(P2-1)/4", okdir)

# ---------------------------------------------------------------- Prop 1.3 for every prime p = 1 mod 4
def prop13_pred(a):
    f = factorint(a)
    n3 = sum(v for l, v in f.items() if l % 7 == 3)
    n24 = sum(v for l, v in f.items() if l % 7 in (2, 4))
    has56 = any(l % 7 in (5, 6) for l in f)
    return has56 or n3 >= 3 or (n3 >= 1 and n24 >= 1)
ok13 = True; n13 = 0
for p in primerange(5, 30000):
    if p % 4 != 1: continue
    a = (p + 7) // 4
    n13 += 1
    E, M = EM(p, a)
    if (len(E) + len(M) > 0) != prop13_pred(a): ok13 = False
say("Prop 1.3 (occupancy criterion) at every prime p = 1 mod 4 below 3e4", ok13, f"{n13} primes")

# ---------------------------------------------------------------- Prop 1.4 survivors
surv = []; ok14 = True
for p in primerange(13, 10**6):
    if p % 12 != 1: continue
    a1 = (p + 3) // 4; a2 = (p + 7) // 4
    E1, M1 = EM(p, a1)
    if E1 or M1:
        continue
    E2, M2 = EM(p, a2)
    if E2 or M2:
        continue
    surv.append(p)
cls = sorted(set(p % 168 for p in surv))
print(f"   survivors of both first shells among p = 1 mod 12 below 1e6: {len(surv)} (reader: 989), first {surv[:3]}, classes mod 168: {cls}")
say("Prop 1.4: survivor count 989, first 1129,1201,2521, classes {1,25,121} mod 168", len(surv) == 989 and surv[:3] == [1129, 1201, 2521] and cls == [1, 25, 121])
# the characterisation itself
okchar = True
for p in primerange(13, 200000):
    if p % 12 != 1: continue
    a1 = (p + 3) // 4; a2 = (p + 7) // 4
    E1, M1 = EM(p, a1); E2, M2 = EM(p, a2)
    lhs = not (E1 or M1 or E2 or M2)
    rhs = (p % 24 == 1 and all(l % 3 == 1 for l in factorint(a1)) and all(l % 7 in (1, 2, 4) for l in factorint(a2)))
    if lhs != rhs: okchar = False
say("Prop 1.4 characterisation, all primes p = 1 mod 12 below 2e5", okchar)

# ---------------------------------------------------------------- Prop 1.5
from fractions import Fraction
fam = {}
ok15 = True; left = set(); ncov = 0
for p in primerange(25, 300000):
    if p % 24 != 1: continue
    if p % 7 == 3: A, B, R = 1, 2, 7
    elif p % 7 == 5: A, B, R = 2, 1, 7
    elif p % 7 == 6: A, B, R = 1, 1, 7
    elif p % 5 == 2: A, B, R = 1, 2, 15
    elif p % 5 == 3: A, B, R = 2, 1, 15
    else:
        left.add(p % 840); continue
    ncov += 1
    if (p + R) % (4 * A * B) or (A + p * B) % R: ok15 = False; continue
    D = (p + R) // (4 * A * B); C = (A + p * B) // R
    if Fraction(1, A * B * D) + Fraction(1, A * C * D) + Fraction(1, p * B * C * D) != Fraction(4, p): ok15 = False
units_sq = sorted(set((u * u) % 840 for u in range(840) if math.gcd(u, 840) == 1))
say("Prop 1.5: five identities hold with integral C, D at every covered prime p = 1 mod 24 < 3e5; the uncovered classes are the unit squares mod 840",
    ok15 and sorted(left) == units_sq, f"{ncov} primes covered; left classes {sorted(left)}; unit squares {units_sq}")

# ---------------------------------------------------------------- item 26 and item 3 data
p = 67369
print(f"   item 26: 67369 prime {isprime(67369)}, 67369 mod 24 = {67369 % 24}, 16849 = {factorint(16849)}, R(16849) = {4*16849-p}, R(16850) = {4*16850-p}")
print(f"   identity 16(4q^3+1)-(4q+1)(16q^2-4q+1): ", end="")
import sympy
q = sympy.symbols('q'); print(sympy.expand(16 * (4 * q**3 + 1) - (4 * q + 1) * (16 * q**2 - 4 * q + 1)))

# Pocklington (N-1 fully factored) -- own implementation
def pocklington_full(N, fac, maxw=100):
    """fac: dict prime->exp with prod = N-1. Returns dict prime->least witness, or None."""
    assert math.prod(q**e for q, e in fac.items()) == N - 1
    wit = {}
    for q in fac:
        for w in range(2, maxw):
            if pow(w, N - 1, N) != 1:
                return None  # N composite (Fermat witness)
            if math.gcd(pow(w, (N - 1) // q, N) - 1, N) == 1:
                wit[q] = w; break
        else:
            return None
    return wit
def trial_prime(n):
    if n < 2: return False
    i = 2
    while i * i <= n:
        if n % i == 0: return False
        i += 1
    return True
P = 7510085481569082811681
q1 = 15646011419935589191
q2 = 1482864185239
ok = True
ok &= (P - 1 == 2**5 * 3 * 5 * q1)
ok &= (q1 - 1 == 2 * 3 * 5 * 351707 * q2)
ok &= (q2 - 1 == 2 * 3 * 17**2 * 5051 * 169307)
leaves = [2, 3, 5, 17, 5051, 169307, 351707]
ok &= all(trial_prime(l) for l in leaves)
w2 = pocklington_full(q2, {2: 1, 3: 1, 17: 2, 5051: 1, 169307: 1})
w1 = pocklington_full(q1, {2: 1, 3: 1, 5: 1, 351707: 1, q2: 1})
w0 = pocklington_full(P, {2: 5, 3: 1, 5: 1, q1: 1})
ok &= all(w is not None for w in (w2, w1, w0))
maxw = max(max(w.values()) for w in (w2, w1, w0))
say("item 3: Pocklington chain proves 7510085481569082811681 prime (own implementation)", ok and maxw < 12,
    f"least witnesses: q2 {w2}; q1 {w1}; P {w0}; largest {maxw}")
print(f"elapsed {time.time()-t0:.1f}s")
