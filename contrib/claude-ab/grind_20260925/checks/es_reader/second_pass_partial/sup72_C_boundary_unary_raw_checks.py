#!/usr/bin/env python3
"""Independent checks: boundary_swap_completion.tex (4 theorems + R=7 companions),
unary_boolean_transport.tex (3), shared_variable_crt.tex (5), input_output_incidence.tex (1),
raw_scale_hit_incidence.tex (4).  Exact arithmetic; no workbench code imported."""
import random, time, itertools
from math import gcd
from fractions import Fraction
from sympy import isprime, factorint, divisors, primerange

random.seed(7)
T0 = time.time()
FAIL = []
def check(c, m):
    if not c:
        FAIL.append(m); print("FAIL:", m)
def lcm(a, b): return a // gcd(a, b) * b
def primes_1mod12(lo, hi): return [q for q in primerange(lo, hi) if q % 12 == 1]
def is_w(p, x, y, z): return Fraction(1, x) + Fraction(1, y) + Fraction(1, z) == Fraction(4, p)

# ============================================================ C1 boundary swap: four candidates
def T(rec, s, t, p, R):
    A, B, eps, D = rec
    al, be = (A, B) if s == 0 else (B, A)
    eta = eps ^ t
    C = Fraction(al + p ** (1 - eta) * be, R)
    return (al, be, eta, D), C

nrec = 0
for p in primes_1mod12(13, 400):
    h = (p - 1) // 12
    for j in range(6 * h):
        a = 3 * h + j + 1; R = 4 * j + 3; S = p * a
        check(R == 4 * a - p, "R = 4j+3")
        for A in divisors(a):
            for B in divisors(a // A):
                D = a // (A * B)
                for eps in (0, 1):
                    X = (A, B, eps, D)
                    C = Fraction(A + p ** (1 - eps) * B, R)
                    orbit = set()
                    for s in (0, 1):
                        for t in (0, 1):
                            Y, Cst = T(X, s, t, p, R)
                            # involution and group law
                            Z, _ = T(Y, s, t, p, R)
                            check(Z == X, "T_{s,t} involution")
                            for s2 in (0, 1):
                                for t2 in (0, 1):
                                    check(T(Y, s2, t2, p, R)[0] == T(X, s ^ s2, t ^ t2, p, R)[0], "group law")
                            al, be, eta, _ = Y
                            x, y, z = a, p ** eta * al * Cst * D, p * be * Cst * D
                            check(1 / Fraction(x) + 1 / y + 1 / z == Fraction(4, p), "rational witness")
                            dy, dz = R * y - S, R * z - S
                            check(dy == p ** eta * al * al * D and dz == p ** (2 - eta) * be * be * D and dy * dz == S * S, "residuals")
                            orbit.add(Y)
                    check(len(orbit) == (4 if A != B else 2), "orbit size")
                    # raw scale correspondence
                    k = gcd(A, B); A0, B0, C0, D0 = A // k, B // k, C / k, k * k * D
                    check(C0 == Fraction(A0 + p ** (1 - eps) * B0, R), "C0")
                    check((C.denominator == 1) == (C0.denominator == 1), "integral locus = C0 integral")
                    # obstruction table on integral sources
                    if C.denominator == 1:
                        for (s, t) in [(0, 0), (1, 0), (0, 1), (1, 1)]:
                            (al, be, eta, _), Cst = T(X, s, t, p, R)
                            num = (al + p ** (1 - eta) * be) % R
                            if (s, t) == (0, 0) or ((s, t) == (1, 0) and eps == 1):
                                mult = 0
                            elif (s, t) == (1, 0):
                                mult = 1 - p * p
                            elif eps == 0:
                                mult = 1 - p
                            elif (s, t) == (0, 1):
                                mult = p - 1
                            else:
                                mult = -(p - 1)
                            check(num == (mult * B) % R, "table residue")
                            delta = R // gcd(R, mult)
                            check(Cst.denominator == delta, "table denominator of C")
                            y = p ** eta * al * Cst * D; z = p * be * Cst * D
                            check(y.denominator == delta and z.denominator == delta, "same denominator for y,z")
                    nrec += 1
print(f"[C1] thm:boundary-four-rational and thm:boundary-obstruction-fibres on all {nrec} raw records "
      f"(all shells of the primes p=1 mod 12 below 400): involutions, (Z/2)^2 law, orbit sizes, "
      f"rational witnesses, residuals d_y d_z = S^2, raw-scale integrality, obstruction residues and exact denominators: ok")

# ============================================================ C2 orbit-code and residual-3 global minimum
def hits(p, jmax):
    """all hits (A0,j,B0,eps) with coprime A0,B0, A0B0 | a, R | A0 + p^{1-eps} B0, 0 <= j < jmax."""
    h = (p - 1) // 12
    out = []
    for j in range(jmax):
        a = 3 * h + j + 1; R = 4 * j + 3
        for A0 in divisors(a):
            for B0 in divisors(a // A0):
                if gcd(A0, B0) != 1:
                    continue
                for eps in (0, 1):
                    if (A0 + p ** (1 - eps) * B0) % R == 0:
                        out.append((A0, j, B0, eps))
    return out

def code(rec, J, M):
    A0, j, B0, eps = rec
    Lam = 2 * J * M
    return (A0 - 1) * Lam + 2 * M * j + 2 * (B0 - 1) + eps

def decode(c, J, M):
    Lam = 2 * J * M
    A0 = 1 + c // Lam; r = c - (A0 - 1) * Lam; j = r // (2 * M); w = r - 2 * M * j
    return (A0, j, 1 + w // 2, w % 2)

t0 = time.time()
nprime = 0; rows = {"R|p-1": 0, "R|p^2-1 only": 0, "else eps=1": 0, "else eps=0": 0}
empty_r3 = 0
for p in primes_1mod12(13, 2500):
    h = (p - 1) // 12
    for (J, M) in [(3 * h, 6 * h), (6 * h, 9 * h)]:
        H = hits(p, J)
        codes = [code(x, J, M) for x in H]
        for x, c in zip(H, codes):
            check(decode(c, J, M) == x and 0 <= c < M * 2 * J * M, "code/decoder")
        # orbits: integral members of the four-candidate orbit
        Hs = set(H)
        for x in H:
            A0, j, B0, eps = x
            R = 4 * j + 3
            mem = {x}
            for (s, t) in [(1, 0), (0, 1), (1, 1)]:
                al, be = (A0, B0) if s == 0 else (B0, A0)
                eta = eps ^ t
                if (al + p ** (1 - eta) * be) % R == 0:
                    y = (al, j, be, eta)
                    check(y in Hs, "integral target is a hit")
                    check(code(y, J, M) - code(x, J, M) == s * (B0 - A0) * (2 * J * M - 2) + (eta - eps), "code difference")
                    mem.add(y)
            # table of integral members
            if (p - 1) % R == 0:
                exp = {(A0, j, B0, 0), (B0, j, A0, 0), (A0, j, B0, 1), (B0, j, A0, 1)}; key = "R|p-1"
                check(A0 != B0, "A != B on R | p-1")
            elif (p * p - 1) % R == 0:
                exp = {(A0, j, B0, eps), (B0, j, A0, eps)}; key = "R|p^2-1 only"
            elif eps == 1:
                exp = {(A0, j, B0, 1), (B0, j, A0, 1)}; key = "else eps=1"
            else:
                exp = {x}; key = "else eps=0"
            check(mem == exp, f"orbit table {p} {x}")
            rows[key] += 1
            mn = min(mem, key=lambda z: code(z, J, M))
            check(mn[0] == min(A0, B0) and mn[2] == max(A0, B0), "min member coordinates")
            if key == "R|p-1":
                check(mn[3] == 0, "min tag 0 on R|p-1")
        # global least hit lies among orbit minima, and the r3 theorem
        if H:
            gmin = min(H, key=lambda z: code(z, J, M))
        a3 = 3 * h + 1
        P2 = [l for l in factorint(a3) if l % 3 == 2]
        j0 = [x for x in H if x[1] == 0]
        if P2:
            ls = min(P2)
            check(gmin == (1, 0, ls, 0) and code(gmin, J, M) == 2 * (ls - 1), f"r3 global minimum p={p}")
            # boundary sources (m+1, 0, 1, 0)
            for x in j0:
                if x[2] == 1 and x[3] == 0 and x[0] > 1:
                    m = x[0] - 1
                    sw = (1, 0, m + 1, 0)
                    check(sw in Hs and code(sw, J, M) == 2 * m and 2 * (ls - 1) <= 2 * m, "boundary source")
                    check((2 * (ls - 1) == 2 * m) == (m + 1 == ls), "equality case")
        else:
            check(j0 == [], "r3 empty domain has no j=0 hit")
            empty_r3 += 1
    nprime += 1
print(f"[C2] thm:boundary-orbit-code and thm:boundary-r3-global-minimum, both radices, all {nprime} primes "
      f"p=1 mod 12 below 2500 (all hits enumerated by brute force): codes/decoder, code-difference formula, "
      f"integral orbit table (row counts {rows}), orbit minima, global least code = 2(l*-1) whenever P2(a3) "
      f"is nonempty, boundary-source inequality; {empty_r3} (prime, radix) cases with P2 empty and no j=0 hit "
      f"({time.time()-t0:.1f}s)")

# residual-seven companions at p = 373
p, a, R = 373, 95, 7
for (A, B, C, D) in [(19, 1, 56, 5), (5, 1, 54, 19)]:
    check(A * B * D == a and (A + p * B) == R * C, "373 record")
    Cs = Fraction(B + p * A, R)
    y, z = B * Cs * D, p * A * Cs * D
    check(Cs.denominator == 7 and y.denominator == 7 and z.denominator == 7 and is_w(p, a, y, z) if False else
          (Cs.denominator == 7 and y.denominator == 7 and z.denominator == 7 and Fraction(1, a) + 1 / y + 1 / z == Fraction(4, p)), "373 swap")
check(Fraction(1 + 373 * 19, 7) == Fraction(7088, 7) and 1 * Fraction(7088, 7) * 5 == Fraction(35440, 7) and 373 * 19 * Fraction(7088, 7) * 5 == Fraction(251163280, 7), "373 numbers 1")
check(Fraction(1 + 373 * 5, 7) == Fraction(1866, 7) and Fraction(1866, 7) * 19 == Fraction(35454, 7) and 373 * 5 * Fraction(1866, 7) * 19 == Fraction(66121710, 7), "373 numbers 2")
print("[C2] residual-seven companions at p=373: both same-tag swaps have exact denominator 7 and are rational witnesses: ok")

# ============================================================ C3 unary box and truth fibres
for p in primes_1mod12(13, 200):
    h = (p - 1) // 12
    J0, M0 = 6 * h, 9 * h
    Lam = 2 * J0 * M0
    img = set(); plus = 0; W1 = 0; Q = Fraction(0)
    for j in range(J0):
        a = 3 * h + j + 1; R = 4 * j + 3
        Ea = [u for u in divisors(a * a) if (4 * u + 1) % R == 0]
        Ma = [u for u in divisors(a * a) if (u + a) % R == 0]
        Q += len(Ea) + Fraction(len(Ma), 2)
        for eps in (0, 1):
            for u in divisors(a * a):
                g = gcd(a, u); A, B, D = a // g, u // g, g * g // u
                check(g * g % u == 0 and A * B * D == a and B * B * D == u, "chart")
                c = (A - 1) * Lam + 2 * M0 * j + 2 * (B - 1) + eps
                check(c not in img, "Theta injective")
                img.add(c)
                passing = (4 * u + p ** eps) % R == 0
                chi = (A + p ** (1 - eps) * B) % R == 0
                check(passing == chi, "B_p^+ = R | 4u + p^eps")
                check(passing == ((u in Ea) if eps == 0 else (u in Ma)), "E/M identification")
                if chi:
                    C = (A + p ** (1 - eps) * B) // R
                    y, z = p ** eps * A * C * D, p * B * C * D
                    check(is_w(p, a, y, z), "unary integer lift")
                    num, den = R * y - p * a, p * a
                    g2 = gcd(num, den)
                    check((num // g2, den // g2) == (A, p ** (1 - eps) * B), "inverse reduced pair")
                    W1 += 2 - eps
    # image = C_p^bud: all codes with AB | a and gcd(A,B) = 1
    bud = set()
    for j in range(J0):
        a = 3 * h + j + 1
        for A in divisors(a):
            for B in divisors(a // A):
                if gcd(A, B) == 1:
                    for eps in (0, 1):
                        bud.add((A - 1) * Lam + 2 * M0 * j + 2 * (B - 1) + eps)
    check(img == bud, "Theta onto C_p^bud")
    check(W1 == 2 * Q, "W_1 = 2 Q_p")
print("[C3] thm:unary-box (Theta bijective onto C_p^bud, gate equivalence, integer lift, inverse), "
      "W_1 = 2 Q_p (thm:unary-truth-fibres): all primes p=1 mod 12 below 200: ok")

# cor:actual-prime-truth-system on the full rectangle for p = 13, 37
for p in (13, 37):
    h = (p - 1) // 12; J0, M0 = 6 * h, 9 * h
    cnt = 0; Cmax = (p + 1) * M0 // 3
    for j in range(J0):
        a = 3 * h + j + 1; R = 4 * j + 3
        for A in range(1, M0 + 1):
            for B in range(1, M0 + 1):
                for eps in (0, 1):
                    Tn = A + (p + (1 - p) * eps) * B
                    phi = (a % (A * B) == 0) and all(not (A % d == 0 and B % d == 0) for d in range(2, M0 + 1)) and Tn % R == 0
                    chi = (a % (A * B) == 0) and gcd(A, B) == 1 and (A + p ** (1 - eps) * B) % R == 0
                    check(phi == chi, "Phi_ES = chi_p")
                    if phi:
                        C, D = Tn // R, a // (A * B)
                        check(1 <= D <= M0 and 1 <= C <= Cmax and B * B * D <= M0 * M0, "bounds")
                        y, z = p ** eps * A * C * D, p * B * C * D
                        check(max(y, z) <= p * M0 * M0 * Cmax, "y,z bound")
                        cnt += 1
print("[C3] cor:actual-prime-truth-system: Phi_ES truth set = chi_p hit set with the stated C, D, u, y, z bounds, "
      "full rectangles at p = 13 and 37: ok")

# ============================================================ C4 shared-variable CRT propositions
def merge(res, mod, b, n):
    g = gcd(mod, n)
    if (b - res) % g:
        return None
    if n // g > 1:
        h_ = (pow(mod // g, -1, n // g) * ((b - res) // g)) % (n // g)
    else:
        h_ = 0
    return res + mod * h_, mod * n // g

for _ in range(800):
    F = random.randint(1, 20)
    congs = [(random.randint(-9, 9), random.randint(-30, 30), random.randint(1, 40)) for _ in range(random.randint(0, 3))]
    ok = True; red = []
    for lam, beta, m in congs:
        g = gcd(lam, m)
        if beta % g:
            ok = False; break
        n = m // g
        ai = (pow(lam // g, -1, n) * (beta // g)) % n if n > 1 else 0
        red.append((ai, n))
    Mtot = 6 * F
    for _, n in red:
        Mtot = lcm(Mtot, n)
    brute = [X for X in range(0, Mtot) if X % (6 * F) == 0 and all((lam * X - beta) % m == 0 for lam, beta, m in congs)]
    if not ok:
        check(brute == [], "input-crt empty")
        continue
    pair_ok = all((ai - aj) % gcd(ni, nj) == 0 for ai, ni in red for aj, nj in red) and all(ai % gcd(6 * F, ni) == 0 for ai, ni in red)
    res, mod = 0, 6 * F
    for ai, ni in red:
        mm = merge(res, mod, ai, ni)
        if mm is None:
            res = None; break
        res, mod = mm
    check(pair_ok == (res is not None) == (len(brute) > 0), "pairwise tests suffice")
    if res is not None:
        check(brute == [res % mod] and 0 <= res < mod, "unique residue a in [0,M)")
print("[C4] prop:input-crt: pairwise compatibility tests <=> solvable; merged residue is the unique one in [0,M) (800 random systems): ok")

nseed = 0
for p in primes_1mod12(13, 300):
    h = (p - 1) // 12
    for a in range(3 * h + 1, 9 * h + 1):
        R = 4 * a - p
        for A in divisors(a):
            for B in divisors(a // A):
                if gcd(A, B) != 1:
                    continue
                for eps in (0, 1):
                    if (A + p ** (1 - eps) * B) % R:
                        continue
                    C = (A + p ** (1 - eps) * B) // R; Dp = a // (A * B)
                    check(4 * A * B * C * Dp == A + p ** (1 - eps) * B + p * C, "seed identity")
                    K0 = 4 * A * B * C; Th = C + (1 - eps) * B; Om = A + eps * B
                    g = gcd(K0, Th); m = K0 // g
                    for q in range(p - 300, p + 301):
                        check((Fraction(Om + q * Th, K0).denominator == 1) == ((q - p) % m == 0), "D_q integrality")
                    den = Fraction(A + B + C, 4 * A * B * C).denominator
                    check(den == m // gcd(m, p - 1) and den > 1, "den formula")
                    for Dd in ((12, 5, 7, 8, 9, 16, m, 2 * m) if m <= 3000 else ()):
                        d = gcd(Dd, m)
                        sols = [q for q in range(1, lcm(Dd, m) + 1) if q % Dd == 1 % Dd and (q - p) % m == 0]
                        check((len(sols) > 0) == ((p - 1) % d == 0), "output compatibility")
                        if sols:
                            q0 = 1 + Dd * ((pow(Dd // d, -1, m // d) * ((p - 1) // d)) % (m // d) if m // d > 1 else 0)
                            check(q0 % lcm(Dd, m) == sols[0] % lcm(Dd, m), "q0 formula")
                    # every prime q = p mod m, q = 1 mod 12, q > p: a witness with a_q in A_q
                    for q in primerange(p + 1, p + 2000):
                        if q % 12 == 1 and (q - p) % m == 0:
                            Dq = (Om + q * Th) // K0
                            aq, yq, zq = A * B * Dq, q ** eps * A * C * Dq, q * B * C * Dq
                            hq = (q - 1) // 12
                            check(is_w(q, aq, yq, zq) and 3 * hq + 1 <= aq <= 9 * hq, "transported witness")
                            check(4 * aq - q == Fraction(A + q ** (1 - eps) * B, C), "R_q formula")
                    nseed += 1
print(f"[C4] prop:output-crt (D_q integral iff q = p mod m; compatibility iff gcd(D,m) | p-1; q0 formula; "
      f"den((A+B+C)/4ABC) = m/gcd(m,p-1) > 1) and the witness/shell-interval part of thm:input-output-incidence "
      f"on all {nseed} coprime seeds at primes p=1 mod 12 below 300: ok")

# input-output example at p = 13
from math import factorial
F = factorial(13); Mm = 6 * F; X0 = 17 * Mm
check(F == 6227020800 and Mm == 37362124800 and X0 == 635156121600, "13! data")
check(X0 == 73 * 8700768789 + 3 and (X0 ** 4 - X0 ** 2 + 1) % 73 == 0, "73 | N(X0)")
check(Fraction(3 + 73, 8) == Fraction(19, 2), "D_73")
# prime divisors of N(X) = X^4 - X^2 + 1 are all = 1 mod 12 (a filter the theorem imposes explicitly)
bad = [(X, q) for X in range(1, 3000) for q in factorint(X ** 4 - X ** 2 + 1) if q % 12 != 1]
check(bad == [], "prime divisors of Phi_12")
print("[C4] input-output example at p=13 (X0 = 17*6*13!, 73 | N(X0), D_73 = 19/2) reproduces; every prime divisor "
      "of X^4 - X^2 + 1 for 1 <= X < 3000 is = 1 mod 12 (the q = 1 mod 12 filter is automatic)")

# ============================================================ C5 raw scale theorems
nraw = 0
for p in primes_1mod12(13, 250):
    h = (p - 1) // 12
    for a in range(3 * h + 1, 9 * h + 1):
        R = 4 * a - p
        for A in divisors(a):
            for B in divisors(a // A):
                D = a // (A * B)
                for eps in (0, 1):
                    if (A + p ** (1 - eps) * B) % R:
                        continue
                    C = (A + p ** (1 - eps) * B) // R
                    check(4 * A * B * C * D == A + p ** (1 - eps) * B + p * C, "raw equation")
                    k = gcd(A, B)
                    check(C % k == 0, "k | C")
                    A0, B0, C0, D0 = A // k, B // k, C // k, k * k * D
                    check(4 * A0 * B0 * C0 * D0 == A0 + p ** (1 - eps) * B0 + p * C0, "coprime equation")
                    u = B * B * D
                    check(u == B0 * B0 * D0 and gcd(a, u) == k * B * D == B0 * D0, "u and g_actual")
                    y, z = p ** eps * A * C * D, p * B * C * D
                    check((y, z) == (p ** eps * A0 * C0 * D0, p * B0 * C0 * D0), "same witness")
                    check(R * y - p * a == p ** eps * A * A * D and R * z - p * a == p ** (2 - eps) * B * B * D, "residuals")
                    nk = sum(1 for kk in divisors(D0) if D0 % (kk * kk) == 0)
                    fz = 1
                    for l, v in factorint(D0).items():
                        fz *= v // 2 + 1
                    check(nk == fz, "scale fibre count")
                    nraw += 1
print(f"[C5] thm:raw-scale-fibre on all {nraw} raw tuples at primes p=1 mod 12 below 250: ok")

nper = 0
for _ in range(3000):
    p = random.choice(primes_1mod12(13, 3000))
    h = (p - 1) // 12
    a = random.randint(3 * h + 1, 9 * h); R = 4 * a - p
    seeds = [(A0, B0, eps) for A0 in divisors(a) for B0 in divisors(a // A0) if gcd(A0, B0) == 1
             for eps in (0, 1) if (A0 + p ** (1 - eps) * B0) % R == 0]
    if not seeds:
        continue
    A0, B0, eps = random.choice(seeds)
    C0 = (A0 + p ** (1 - eps) * B0) // R; D0p = a // (A0 * B0)
    K0 = 4 * A0 * B0 * C0; Th = C0 + (1 - eps) * B0; Om = A0 + eps * B0
    g0 = gcd(K0, Th); m0 = K0 // g0; w = Th // g0
    for k in [kk for kk in divisors(D0p) if D0p % (kk * kk) == 0]:
        mk = k * k * K0 // gcd(k * k * K0, Th)
        check(Fraction(mk, m0) == Fraction(k * k, gcd(k * k, w)), "m_k/m_0")
        for q in range(p, p + 4 * mk + 1):
            Dk = Fraction(Om + q * Th, k * k * K0)
            check((Dk.denominator == 1) == ((q - p) % mk == 0), "D_k integrality")
        # first-half gate
        for q in [qq for qq in range(p, p + 3 * lcm(12, m0) + 1, lcm(12, m0))]:
            aq = Fraction(Om + q * Th, 4 * C0)
            check((2 * aq <= q - 1) == (q * (2 * C0 - Th) >= Om + 2 * C0), "first-half gate")
        nper += 1
print(f"[C5] thm:raw-scale-period (m_k/m_0 = k^2/gcd(k^2,w); D_k integral iff q = p mod m_k) and the first-half gate "
      f"equivalence of thm:raw-first-half-code on {nper} random (seed, k): ok")

# PCT radix change: c_F - c_H formula on all first-half hits
for p in primes_1mod12(13, 600):
    h = (p - 1) // 12
    JH, MH, JF, MF = 3 * h, 6 * h, 6 * h, 9 * h
    LH, LF = 2 * JH * MH, 2 * JF * MF
    check(LF == 3 * LH and LH == (p - 1) ** 2 // 4, "Lambda_F = 3 Lambda_H")
    for x in hits(p, JH):
        A0, j, B0, eps = x
        cH = (A0 - 1) * LH + (p - 1) * j + 2 * (B0 - 1) + eps
        cF = (A0 - 1) * LF + 2 * MF * j + 2 * (B0 - 1) + eps
        check(cH == code(x, JH, MH) and cF - cH == 2 * (A0 - 1) * LH + (p - 1) // 2 * j, "radix change")
    # least-hit selector: product formula equals least hit code
    H = hits(p, JH)
    cs = sorted(code(x, JH, MH) for x in H)
    check(cs[0] < MH * LH, "hit exists")
    for r0 in range(1, 4):
        check((min(x[0] for x in H) <= r0) == (cs[0] < r0 * LH), "first r0 layers criterion")
print("[C5] thm:raw-first-half-code: Lambda_F = 3 Lambda_H, c_F - c_H = 2(A-1)Lambda_H + (q-1)j/2 on every "
      "first-half hit, least-code layer criterion, primes p=1 mod 12 below 600: ok")

# fixtures at p = 13 and 61
check(4 * 2 * 1 * 5 * 2 == 80 == 2 + 13 + 13 * 5, "13 fixture")
check(decode(36, 6, 9) == (1, 2, 1, 0) and (1 + 13) % 11 != 0, "13 fixture decode")
check(4 * 2 * 4 * 2 * 2 == 128 == 2 + 4 + 61 * 2, "61 fixture")
check(Fraction(3 + 109, 8) == 14 and Fraction(3 + 157, 8) == 20 and Fraction(14, 4) == Fraction(7, 2) and 20 // 4 == 5, "61 fixture D values")
check(is_w(109, 28, 1526, 3052) and is_w(157, 40, 3140, 6280), "61 fixture witnesses")
print("[C5] fixtures p=13 (c_H=36, c_F=108, misread code 36 -> (1,2,1,0) fails) and p=61 (q=109: D_2 = 7/2; q=157: D_2 = 5) reproduce")

print()
print("TOTAL FAILURES:", len(FAIL))
print(f"runtime {time.time()-T0:.1f}s")
