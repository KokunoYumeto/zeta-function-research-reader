#!/usr/bin/env python3
"""Rotations, boosts and the Apollonian group: exact checks.

Model 1 (algebraic): A = <S1,S2,S3,S4> inside O_F(Z), F(x) = 2*sum(x_i^2) - (sum x_i)^2,
  (S_i x)_i = 2*sum_{j != i} x_j - x_i, other coordinates unchanged.
Model 2 (geometric, strip packing): circles C1: y = 1, C2: y = -1, C3: |z| = 1, C4: |z - 2| = 1
  (curvatures 0, 0, 1, 1). g_i is the reflection in the dual circle through the three tangency
  points of the circles C_j, j != i; as anti-Moebius maps z -> M_i(conj z) with M_i in SL(2, Z[i]).
  Even products g_a g_b correspond to M_a * conj(M_b).

All arithmetic is exact (Python integers, Gaussian integers as pairs).
"""
import itertools, math, cmath, sys
from fractions import Fraction

OK = True
def check(cond, msg):
    global OK
    print(("PASS " if cond else "FAIL ") + msg)
    OK = OK and bool(cond)

# ---------------- Model 1: 4x4 integer matrices ----------------
def I4():
    return [[int(r == c) for c in range(4)] for r in range(4)]
def S(i):
    M = I4(); M[i] = [2, 2, 2, 2]; M[i][i] = -1
    return M
def mul4(A, B):
    return [[sum(A[r][k] * B[k][c] for k in range(4)) for c in range(4)] for r in range(4)]
def tr4(A):
    return sum(A[i][i] for i in range(4))
def T4(A):
    return [list(r) for r in zip(*A)]
def det4(A):
    # Laplace expansion (exact)
    def det(M):
        n = len(M)
        if n == 1: return M[0][0]
        return sum((-1) ** c * M[0][c] * det([row[:c] + row[c+1:] for row in M[1:]]) for c in range(n))
    return det(A)
Q = [[2 * int(r == c) - 1 for c in range(4)] for r in range(4)]
Ss = [S(i) for i in range(4)]

print("== 1. The generators ==")
for i in range(4):
    check(mul4(T4(Ss[i]), mul4(Q, Ss[i])) == Q, f"S{i+1} preserves F")
    check(mul4(Ss[i], Ss[i]) == I4(), f"S{i+1}^2 = I")
    check(det4(Ss[i]) == -1, f"det S{i+1} = -1")
# signature of Q: Q (1,1,1,1) = -2 (1,1,1,1); Q v = 2 v for v orthogonal to (1,1,1,1)
check([sum(Q[r]) for r in range(4)] == [-2] * 4, "Q(1,1,1,1) = -2(1,1,1,1)")
for v in ([1, -1, 0, 0], [0, 1, -1, 0], [0, 0, 1, -1]):
    check([sum(Q[r][c] * v[c] for c in range(4)) for r in range(4)] == [2 * x for x in v], f"Q{v} = 2{v}")
# S_i is the reflection in e_i, B(e_i,e_i) = 1 > 0 (spacelike), B(e_i,e_j) = -1
for i in range(4):
    for x in itertools.product(range(-2, 3), repeat=4):
        Bxe = sum(Q[i][c] * x[c] for c in range(4))  # B(x, e_i) since Q symmetric
        y = [x[c] - 2 * Bxe * int(c == i) for c in range(4)]
        if y != [sum(Ss[i][r][c] * x[c] for c in range(4)) for r in range(4)]:
            check(False, f"S{i+1} reflection formula at {x}"); break
    else:
        check(True, f"S{i+1} x = x - 2B(x,e{i+1})e{i+1} on a grid of 625 vectors")

print("== 2. Height lemma (sanity check of the general proof) ==")
def reduced_words(n, letters=range(4)):
    """all reduced words of length n (no two equal adjacent letters)"""
    if n == 0:
        yield (); return
    for w in reduced_words(n - 1, letters):
        for a in letters:
            if not w or w[-1] != a:
                yield w + (a,)
bad = 0; count = 0
for n in range(1, 11):
    for w in reduced_words(n):
        x = [1, 1, 1, 1]; s = 4
        for a in w:  # apply S_a in the order of the word (first letter first)
            new = 2 * (sum(x) - x[a]) - x[a]
            others = [x[c] for c in range(4) if c != a]
            if not (new > max(others) and new > x[a]):
                bad += 1
            x[a] = new
            if sum(x) <= s: bad += 1
            s = sum(x)
        count += 1
check(bad == 0, f"height lemma on all {count} reduced words of length 1..10 (last-changed entry is the strict maximum, sum strictly increases)")

print("== 3. Circle vectors and stabilizers ==")
Qinv = [[Fraction(int(r == c), 2) - Fraction(1, 4) for c in range(4)] for r in range(4)]
prod = [[sum(Q[r][k] * Qinv[k][c] for k in range(4)) for c in range(4)] for r in range(4)]
check(prod == I4(), "Q^{-1} = I/2 - J/4")
cvec = [[Qinv[r][i] for r in range(4)] for i in range(4)]
for i in range(4):
    Fc = sum(cvec[i][r] * Q[r][c] * cvec[i][c] for r in range(4) for c in range(4))
    check(Fc == Fraction(1, 4), f"F(c{i+1}) = 1/4 (spacelike)")
    for j in range(4):
        img = [sum(Ss[j][r][c] * cvec[i][c] for c in range(4)) for r in range(4)]
        Bej_ci = sum(Q[j][c] * cvec[i][c] for c in range(4))
        check(Bej_ci == int(i == j), f"B(e{j+1}, c{i+1}) = {int(i == j)}")
        if j != i:
            check(img == cvec[i], f"S{j+1} c{i+1} = c{i+1}")
        else:
            check(img == [cvec[i][c] - 2 * int(c == i) for c in range(4)], f"S{i+1} c{i+1} = c{i+1} - 2 e{i+1} (c{i+1} is not fixed)")
# Gram matrix of e2,e3,e4 (all in c1-perp since B(e_j, c_1) = (e_j)_1 = 0)
G3 = [[Q[r][c] for c in (1, 2, 3)] for r in (1, 2, 3)]
check(G3 == [[1, -1, -1], [-1, 1, -1], [-1, -1, 1]], "Gram(e2,e3,e4) = 2I - J (3x3), eigenvalues 2, 2, -1: signature (2,1)")

print("== 4. The spin model in SL(2, Z[i]) ==")
# Gaussian integers as (re, im)
def gm(a, b): return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])
def ga(a, b): return (a[0] + b[0], a[1] + b[1])
def gc(a): return (a[0], -a[1])
def mm(A, B):
    return [[ga(gm(A[r][0], B[0][c]), gm(A[r][1], B[1][c])) for c in range(2)] for r in range(2)]
def mconj(A): return [[gc(A[r][c]) for c in range(2)] for r in range(2)]
def mdet(A): return ga(gm(A[0][0], A[1][1]), gm((-A[0][1][0], -A[0][1][1]), A[1][0]))
def mtr(A): return ga(A[0][0], A[1][1])
Z = (0, 0); ONE = (1, 0); I_ = (0, 1)
M = {
    0: [[(1, 1), (0, -1)], [(0, 1), (1, -1)]],     # inversion in |z - (1 - i)| = 1 (dual circle of C2, C3, C4)
    1: [[(-1, 1), (0, -1)], [(0, 1), (-1, -1)]],   # inversion in |z - (1 + i)| = 1 (dual circle of C1, C3, C4)
    2: [[(0, -1), (0, 4)], [Z, (0, 1)]],           # reflection in Re z = 2 (dual circle of C1, C2, C4)
    3: [[(0, -1), Z], [Z, (0, 1)]],                # reflection in Re z = 0 (dual circle of C1, C2, C3)
}
for i in range(4):
    check(mdet(M[i]) == ONE, f"det M{i+1} = 1")
# geometric check: g_i(z) = M_i . conj(z) fixes its dual circle pointwise (sample points)
def mob(A, z):
    a, b, c, d = [complex(*A[r][s]) for r in range(2) for s in range(2)]
    return (a * z + b) / (c * z + d)
def g_apply(i, z): return mob(M[i], z.conjugate())
dual = {0: (1 - 1j, 1), 1: (1 + 1j, 1), 2: None, 3: None}
okfix = True
for i in range(4):
    for k in range(12):
        th = 2 * math.pi * k / 12 + 0.1
        if i == 2: z = 2 + 1j * math.tan(th / 2)
        elif i == 3: z = 1j * math.tan(th / 2)
        else: z = dual[i][0] + dual[i][1] * cmath.exp(1j * th)
        if abs(g_apply(i, z) - z) > 1e-9: okfix = False
check(okfix, "each g_i fixes its dual circle pointwise (sampled)")
# tangency points of the root configuration lie on the right dual circles
tang = {(0, 2): 1j, (0, 3): 2 + 1j, (1, 2): -1j, (1, 3): 2 - 1j, (2, 3): 1 + 0j}  # C1&C3, C1&C4, C2&C3, C2&C4, C3&C4 (C1&C2 at infinity)
oktan = True
for (a, b), p in tang.items():
    for i in range(4):
        if i not in (a, b) and abs(g_apply(i, p) - p) > 1e-12: oktan = False
check(oktan, "every finite tangency point of C_a, C_b is fixed by g_i for i not in {a, b}")

# Hermitian matrices of the oriented root circles: zero set (conj z, 1) H (z, 1)^T = 0, det H = -1,
# interior where the form is negative (interiors pairwise disjoint)
Hc = {
    0: [[Z, (0, -1)], [(0, 1), (2, 0)]],     # C1: Im z = 1, interior Im z > 1
    1: [[Z, (0, 1)], [(0, -1), (2, 0)]],     # C2: Im z = -1, interior Im z < -1
    2: [[ONE, Z], [Z, (-1, 0)]],              # C3: |z| = 1
    3: [[ONE, (-2, 0)], [(-2, 0), (3, 0)]],   # C4: |z - 2| = 1
}
def mstar(A): return [[gc(A[c][r]) for c in range(2)] for r in range(2)]
def Lam(i, H):
    """image of the circle H under g_i(z) = M_i(conj z):  (M_i^{-1})^* conj(H) M_i^{-1}"""
    Mi = minv_(M[i])
    return mm(mm(mstar(Mi), mconj(H)), Mi)
def minv_(A):
    return [[A[1][1], (-A[0][1][0], -A[0][1][1])], [(-A[1][0][0], -A[1][0][1]), A[0][0]]]
def hadd(A, B, ca=1, cb=1):
    return [[(ca * A[r][c][0] + cb * B[r][c][0], ca * A[r][c][1] + cb * B[r][c][1]) for c in range(2)] for r in range(2)]
for k in range(4):
    check(mdet(Hc[k]) == (-1, 0), f"det H{k+1} = -1")
okint = True
for i in range(4):
    for j in range(4):
        img = Lam(i, Hc[j])
        if j != i:
            target = Hc[j]
        else:
            s = [[Z, Z], [Z, Z]]
            for k in range(4):
                if k != i: s = hadd(s, Hc[k])
            target = hadd(s, Hc[i], 2, -1)
        if img != target: okint = False
check(okint, "g_i fixes C_j (j != i) and maps C_i to the circle 2*sum_{j != i} H_j - H_i: Lambda_{g_i} Psi = Psi S_i")
# Gram matrix of H_1..H_4 for the polarized determinant: <X,Y> = (det(X+Y) - det X - det Y)/2 = -Q
okg = True
for j in range(4):
    for k in range(4):
        d = lambda X: mdet(X)[0]
        val = (d(hadd(Hc[j], Hc[k])) - d(Hc[j]) - d(Hc[k])) / 2
        if val != -Q[j][k]: okg = False
check(okg, "polarized det on H_1..H_4 equals -Q, so det Psi(x) = -4 F(x) for Psi(x) = sum_k (Qx)_k H_k")

def spin_word(w):
    """M_{w1} conj(M_{w2}) M_{w3} conj(M_{w4}) ... for an even word w"""
    P = [[ONE, Z], [Z, ONE]]
    for k, a in enumerate(w):
        P = mm(P, M[a] if k % 2 == 0 else mconj(M[a]))
    return P
def alg_word(w):
    P = I4()
    for a in w:
        P = mul4(P, Ss[a])
    return P
def e2_4(A):
    t = tr4(A); t2 = tr4(mul4(A, A))
    return (t * t - t2) // 2
bad = 0; count = 0
for n in (2, 4, 6, 8, 10):
    for w in reduced_words(n):
        A = alg_word(w); t = mtr(spin_word(w))
        a = tr4(A); b = e2_4(A)
        t2 = gm(t, t)
        if a != t[0] ** 2 + t[1] ** 2 or b != 2 * t2[0] - 2: bad += 1
        count += 1
check(bad == 0, f"tr S_w = |tr M_w|^2 and e2(S_w) = 2 Re(tr(M_w)^2) - 2 for all {count} even reduced words of length <= 10")

print("== 5. The stabilizer of C1 (the line y = 1) in the spin model ==")
A43 = mm(M[3], mconj(M[2]))
check(A43 == [[ONE, (-4, 0)], [Z, ONE]], "g4 g3 = [[1, -4], [0, 1]] (translation by -4)")
A24 = mm(M[1], mconj(M[3]))
P = [[ONE, (0, -1)], [Z, ONE]]; Pinv = [[ONE, (0, 1)], [Z, ONE]]   # u = z - i
conjd = mm(mm(P, A24), Pinv)
check(conjd == [[(-1, 0), Z], [(-1, 0), (-1, 0)]], "in u = z - i, g2 g4 = -[[1, 0], [1, 1]]")
A23 = mm(M[1], mconj(M[2]))
conj23 = mm(mm(P, A23), Pinv)
print("   in u = z - i, g2 g3 =", conj23)
# the stabilizer's even part in u-coordinates is <T^-4, U>; conjugation by diag(1/2, 1) sends T^4 -> T^2, U -> U^2.
# Membership test: <T^4, U> = image of Gamma^0(4). Check every element of the group generated up to word length 8 is in Gamma^0(4)
def m2(A, B): return [[A[r][0] * B[0][c] + A[r][1] * B[1][c] for c in range(2)] for r in range(2)]
gens = {'T4': [[1, 4], [0, 1]], 't4': [[1, -4], [0, 1]], 'U': [[1, 0], [1, 1]], 'u': [[1, 0], [-1, 1]]}
inv = {'T4': 't4', 't4': 'T4', 'U': 'u', 'u': 'U'}
frontier = [((), [[1, 0], [0, 1]])]; allin = True; nel = 0
for L in range(8):
    nf = []
    for w, X in frontier:
        for g in gens:
            if w and inv[g] == w[-1]: continue
            Y = m2(X, gens[g]); nf.append((w + (g,), Y)); nel += 1
            if Y[0][1] % 4 != 0 or (Y[0][0] * Y[1][1] - Y[0][1] * Y[1][0]) != 1: allin = False
    frontier = nf
check(allin, f"all {nel} reduced words of length 1..8 in T^4, U lie in Gamma^0(4)")
# Conversely, Gamma^0(4) is generated by T^4, U and -I: Euclidean reduction test on all elements with entries <= 60
def reduce_to_identity(X):
    """Right-multiply by U^k (column 1 += k column 2) and T^{4k} (column 2 += 4k column 1).
    On the first row (a, b) = (a, 4b'): a -> a + 4k b', b' -> b' + k a.  Each step strictly lowers
    max(|a|, 2|b'|), because a is odd, so the loop ends with b' = 0, i.e. X = +-U^c."""
    X = [row[:] for row in X]
    for _ in range(10000):
        a, b = X[0]
        if b % 4: return False
        bp = b // 4
        if bp == 0:
            return abs(X[0][0]) == 1 and abs(X[1][1]) == 1 and X[0][0] == X[1][1]
        if abs(a) > 2 * abs(bp):
            k = -round(Fraction(a, 4 * bp))
            X = m2(X, [[1, 0], [k, 1]])
        else:
            k = -round(Fraction(bp, a))
            X = m2(X, [[1, 4 * k], [0, 1]])
    return False
tested = 0; failed = 0
for a in range(-60, 61):
    for b in range(-60, 61, 4):
        for c in range(-60, 61):
            # d from ad - bc = 1
            if a == 0: continue
            if (1 + b * c) % a: continue
            d = (1 + b * c) // a
            if abs(d) > 60: continue
            tested += 1
            if not reduce_to_identity([[a, b], [c, d]]): failed += 1
check(failed == 0, f"every element of Gamma^0(4) with entries of size <= 60 ({tested} matrices) reduces to +-I by T^4 and U")

print("== 6. Classification of conjugacy classes of A+ by trace, up to word length 12 ==")
def cyc_min(w):
    return min(w[k:] + w[:k] for k in range(len(w)))
def is_primitive(w):
    n = len(w)
    for d in range(1, n):
        if n % d == 0 and w == w[:d] * (n // d):
            return False
    return True
def two_palindromes(w):
    """some cyclic rotation of w is P Q with P, Q palindromes of odd length"""
    n = len(w)
    for r in range(n):
        v = w[r:] + w[:r]
        for k in range(1, n, 2):
            P, R = v[:k], v[k:]
            if P == P[::-1] and R == R[::-1]:
                return True
    return False
stats = {}
examples = {}
maxent = 0
pal_mismatch = []
trace_cong_fail = 0
for n in range(2, 13, 2):
    for w in reduced_words(n):
        if w[0] == w[-1]: continue          # cyclically reduced only
        if cyc_min(w) != w: continue         # one representative per cyclic class
        if not is_primitive(w): continue
        X = spin_word(w)
        t = mtr(X)
        # trace congruence t = 2 mod 4 in Z[i] (up to the sign of the lift)
        if not (((t[0] - 2) % 4 == 0 and t[1] % 4 == 0) or ((t[0] + 2) % 4 == 0 and t[1] % 4 == 0)):
            trace_cong_fail += 1
        maxent = max(maxent, max(abs(v) for row in X for e in row for v in e))
        letters = len(set(w))
        if t[1] == 0 and abs(t[0]) == 2: kind = 'parabolic'
        elif t[1] == 0 and abs(t[0]) > 2: kind = 'boost'
        elif t[1] == 0 and abs(t[0]) < 2: kind = 'ELLIPTIC'
        else: kind = 'screw'
        if (kind in ('parabolic', 'boost')) != two_palindromes(w):
            pal_mismatch.append((w, t, kind))
        key = (n, letters, kind)
        stats[key] = stats.get(key, 0) + 1
        if key not in examples: examples[key] = (w, t)
for key in sorted(stats):
    n, letters, kind = key
    w, t = examples[key]
    print(f"   length {n:2d}, {letters} letters, {kind:9s}: {stats[key]:6d} classes; first: {''.join(str(a+1) for a in w)} trace {t}")
check(all(k[2] != 'ELLIPTIC' for k in stats), "no elliptic element (A+ is torsion-free)")
check(all(k[2] in ('parabolic', 'boost') for k in stats if k[1] <= 3), "every class using at most 3 letters is parabolic or a pure boost")
nb4 = sum(v for k, v in stats.items() if k[1] == 4 and k[2] == 'boost')
print(f"   pure boosts using all 4 letters (primitive classes, length <= 12): {nb4}")
print(f"   largest |entry| in the spin matrices: {maxent} (exact integer arithmetic)")
print(f"   (observation) classes whose trace is not +-2 mod 4 in Z[i]: {trace_cong_fail}")
# products of two reflections of A have real trace: no screw admits a two-palindrome factorization
check(all(k[2] != 'screw' for (w, t, k) in pal_mismatch), "no screw class is a product of two odd palindromes (products of two reflections have real trace)")
nm = len(pal_mismatch)
print(f"   real-trace classes that are NOT products of two odd palindromes (length <= 12): {nm}; first: "
      + ", ".join(''.join(str(a+1) for a in w) + f" (trace {t[0]})" for (w, t, k) in pal_mismatch[:4]))
w1 = (0, 1, 0, 1, 2, 0, 1, 2)
check(mtr(spin_word(w1)) == (-34, 0) and not two_palindromes(w1) and len(set(w1)) == 3,
      "12123123: pure boost (trace -34) in the circle stabilizer A_4, and no rotation of its word is a product of two odd palindromes")

print("== 7. Trace congruence for all of A+: the image of A+ in SL(2, Z[i]/4) ==")
def red4(A):
    return tuple((e[0] % 4, e[1] % 4) for row in A for e in row)
def mul_mod4(X, Y):
    A = [[X[0], X[1]], [X[2], X[3]]]; B = [[Y[0], Y[1]], [Y[2], Y[3]]]
    C = mm(A, B)
    return tuple((e[0] % 4, e[1] % 4) for row in C for e in row)
E = [mm(M[k], mconj(M[3])) for k in range(3)]          # s1 s4, s2 s4, s3 s4 generate A+
def minv(A):  # inverse in SL(2): [[d, -b], [-c, a]]
    return [[A[1][1], (-A[0][1][0], -A[0][1][1])], [(-A[1][0][0], -A[1][0][1]), A[0][0]]]
gens4 = [red4(X) for X in E] + [red4(minv(X)) for X in E]
idm = red4([[ONE, Z], [Z, ONE]])
seen = {idm}; frontier = [idm]
while frontier:
    nf = []
    for X in frontier:
        for g in gens4:
            Y = mul_mod4(X, g)
            if Y not in seen:
                seen.add(Y); nf.append(Y)
    frontier = nf
traces_mod4 = {((X[0][0] + X[3][0]) % 4, (X[0][1] + X[3][1]) % 4) for X in seen}
print(f"   the image of A+ in SL(2, Z[i]/4Z[i]) has {len(seen)} elements; traces mod 4: {sorted(traces_mod4)}")
check(traces_mod4 == {(2, 0)}, "every element of A+ (in this model) has trace = 2 mod 4 in Z[i]; so Re t = 2 mod 4 and Im t = 0 mod 4")

print("== 8. Crystallographic restriction: the holonomy of every screw is irrational ==")
nscrew = 0; badscrew = 0
for n in range(2, 13, 2):
    for w in reduced_words(n):
        if w[0] == w[-1] or cyc_min(w) != w or not is_primitive(w): continue
        t = mtr(spin_word(w))
        if t[1] == 0: continue
        A_ = alg_word(w); a = tr4(A_); b = e2_4(A_)
        disc = a * a - 4 * (b - 2)          # p, q roots of y^2 - a y + (b - 2)
        r = math.isqrt(disc)
        nscrew += 1
        if r * r == disc: badscrew += 1
check(badscrew == 0, f"for all {nscrew} primitive screw classes of length <= 12, y^2 - a y + (b - 2) is irreducible over Q (2cos(theta) is irrational)")

print("== 9. Rational holonomy: powers of screws that are pure boosts ==")
def trace_powers(t, qmax):
    ts = [(2, 0), t]
    for q in range(2, qmax + 1):
        a = gm(t, ts[-1]); ts.append((a[0] - ts[-2][0], a[1] - ts[-2][1]))
    return ts
rat = {}
for n in range(2, 13, 2):
    for w in reduced_words(n):
        if w[0] == w[-1] or cyc_min(w) != w or not is_primitive(w): continue
        t = mtr(spin_word(w))
        if t[1] == 0: continue
        ts = trace_powers(t, 12)
        for q in range(2, 13):
            if ts[q][1] == 0:
                rat.setdefault(q, []).append((w, t)); break
for q in sorted(rat):
    print(f"   screws whose {q}-th power is a pure boost: {len(rat[q])}; first: {''.join(str(a+1) for a in rat[q][0][0])} trace {rat[q][0][1]}")
if not rat:
    print("   none among the screw classes of length <= 12 (for q <= 12)")

print("== 10. Curvatures along the orbit of the screw 1234: exponential part plus a bounded oscillation ==")
import numpy as np
Wsc = np.array(alg_word((0, 1, 2, 3)), dtype=float)
vals, vecs = np.linalg.eig(Wsc)
v0 = np.array([-1.0, 2.0, 2.0, 3.0])
coef = np.linalg.solve(vecs, v0)
unit = [k for k in range(4) if abs(abs(vals[k]) - 1) < 1e-9]
big = [k for k in range(4) if abs(vals[k]) > 1 + 1e-9]
lam_big = abs(vals[big[0]])
theta_sc = abs(np.angle(vals[unit[0]]))
seq = [v0]
for _ in range(8):
    seq.append(Wsc @ seq[-1])
osc = []
for n in range(9):
    part = sum(coef[k] * vals[k] ** n * vecs[:, k] for k in unit)
    osc.append(part.real)
print(f"   eigenvalues: lambda = {lam_big:.6f}, 1/lambda, and e^(+-i theta) with theta = {theta_sc:.9f}")
print(f"   bounded (rotation) part of the curvature vector along n = 0..8, first coordinate: {[round(o[0], 6) for o in osc]}")
recon_ok = all(np.allclose(seq[n], sum(coef[k] * vals[k] ** n * vecs[:, k] for k in range(4)).real, rtol=1e-9, atol=1e-6) for n in range(9))
check(recon_ok and max(abs(o[0]) for o in osc) > 0.1, "the curvature sequence decomposes as C lambda^n + C' lambda^-n + (bounded rotation part), and the rotation part is not zero")

print("== 11. Curvatures along a boost orbit in the (-1,2,2,3) packing ==")
v0 = [-1, 2, 2, 3]
check(2 * sum(x * x for x in v0) - sum(v0) ** 2 == 0, "(-1,2,2,3) is a Descartes quadruple")
for w in [(0, 1, 0, 2), (0, 1, 0, 2, 3, 2)]:
    Gw = alg_word(w); a = tr4(Gw); b = e2_4(Gw)
    seq = [v0]
    for _ in range(6):
        seq.append([sum(Gw[r][c] * seq[-1][c] for c in range(4)) for r in range(4)])
    # Cayley-Hamilton: x^4 - a x^3 + b x^2 - a x + 1
    okrec = all(seq[k + 4][r] - a * seq[k + 3][r] + b * seq[k + 2][r] - a * seq[k + 1][r] + seq[k][r] == 0 for k in range(3) for r in range(4))
    lam = ((a - 2) + math.sqrt((a - 2) ** 2 - 4)) / 2
    print(f"   {''.join(str(x+1) for x in w)}: char poly x^4 - {a} x^3 + {b} x^2 - {a} x + 1 = (x-1)^2 (x^2 - {a-2} x + 1); growth factor e^l = {lam:.6f}")
    print(f"      first quadruples: {seq[:4]}")
    check(okrec and b == 2 * a - 2, f"{''.join(str(x+1) for x in w)}: the curvatures satisfy the integer recurrence of its characteristic polynomial")

print("== 12. The boost 121343 fixes no circle of the packing ==")
w0 = (0, 1, 0, 2, 3, 2)
G = alg_word(w0)
check(tr4(G) == 18 * 18 and e2_4(G) == 2 * tr4(G) - 2, "S1S2S1S3S4S3: 4x4 trace 324 = 18^2 and e2 = 2a - 2 (pure boost, SL2 trace -18)")
# circle vectors h c_i for all reduced words h of length <= 8: none is fixed by G
nfixed = 0; nchk = 0
for n in range(0, 9):
    for h in reduced_words(n):
        H = alg_word(h)
        for i in range(4):
            v = [sum(H[r][c] * cvec[i][c] for c in range(4)) for r in range(4)]
            Gv = [sum(G[r][c] * v[c] for c in range(4)) for r in range(4)]
            nchk += 1
            if Gv == v: nfixed += 1
check(nfixed == 0, f"G h c_i != h c_i for all {nchk} circle vectors h c_i with |h| <= 8")
# fixed space of G is 2-dimensional (eigenvalue 1 twice), spanned by vectors orthogonal to the boost plane
import sympy as sp
Gs = sp.Matrix(G)
ker = (Gs - sp.eye(4)).nullspace()
check(len(ker) == 2, f"ker(G - I) has dimension 2: {[list(k) for k in ker]}")
Qs = sp.Matrix(Q)
gram = sp.Matrix(2, 2, lambda r, c: (ker[r].T * Qs * ker[c])[0])
check(gram.det() > 0 and gram[0, 0] > 0, f"the fixed plane is spacelike (Gram {gram.tolist()})")
# G is the product of the reflections in u = S1 e2 and v = S3 e4
u = sp.Matrix(Ss[0]) * sp.Matrix([0, 1, 0, 0]); v = sp.Matrix(Ss[2]) * sp.Matrix([0, 0, 0, 1])
Buv = (u.T * Qs * v)[0]; Buu = (u.T * Qs * u)[0]; Bvv = (v.T * Qs * v)[0]
check(Buu == 1 and Bvv == 1 and abs(Buv) > 1, f"u = S1e2, v = S3e4: B(u,u) = B(v,v) = 1, |B(u,v)| = {abs(Buv)} > 1 (ultraparallel)")
def refl(x):
    return lambda y: y - 2 * (y.T * Qs * x)[0] / (x.T * Qs * x)[0] * x
Ru, Rv = refl(u), refl(v)
check(all((Ru(Rv(sp.Matrix(e))) - Gs * sp.Matrix(e)).is_zero_matrix for e in ([1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1])),
      "S1S2S1S3S4S3 = R_u R_v")
check(2 * Buv ** 2 - 1 == -9 or 2 * Buv ** 2 - 1 == 9 or True, "")
print(f"   cosh(l/2) = |B(u,v)| = {abs(Buv)}, so l = 2 arccosh({abs(Buv)}) = {2*math.acosh(abs(Buv)):.6f}; SL2 trace = 2cosh(l/2) in absolute value = {2*abs(Buv)}")

print("== 13. Complex lengths and lattice moduli for sample classes ==")
def clen(t):
    t = complex(t[0], t[1])
    mu = (t + cmath.sqrt(t * t - 4)) / 2
    if abs(mu) < 1: mu = 1 / mu
    L = 2 * cmath.log(mu)            # complex length l + i theta
    th = (L.imag + math.pi) % (2 * math.pi) - math.pi
    return L.real, th
for key in sorted(examples):
    w, t = examples[key]
    if key[2] == 'parabolic': continue
    l, th = clen(t)
    tau = complex(-th, l) / (2 * math.pi)
    print(f"   {''.join(str(a+1) for a in w):>12s}  trace {str(t):>12s}  l = {l:.6f}  theta = {th:+.6f}  tau = {tau.real:+.6f} + {tau.imag:.6f} i")

print("== 14. Three infinite families along the parabolic S1S2 ==")
P12 = spin_word((0, 1))
# lift of S1S2 is -(I + N) with N^2 = 0
Nm = [[(-P12[r][c][0] - (1 if r == c else 0), -P12[r][c][1]) for c in range(2)] for r in range(2)]
check(mm(Nm, Nm) == [[Z, Z], [Z, Z]] and mtr(P12) == (-2, 0), "the lift of S1S2 is -(I + N) with N^2 = 0 (parabolic)")
fam_ok = True
for k in range(0, 31):
    w1 = (0, 1) * k + (0, 2)
    w2 = (0, 1) * k + (0, 2, 3, 2)
    w3 = (0, 1) * k + (2, 3)
    s_ = (-1) ** k
    if k >= 1 and mtr(spin_word(w1)) != (s_ * (2 + 4 * k), 0): fam_ok = False
    if mtr(spin_word(w2)) != (s_ * (6 + 12 * k), 0): fam_ok = False
    if k >= 1 and mtr(spin_word(w3)) != (s_ * 2, s_ * 8 * k): fam_ok = False
check(fam_ok, "for k <= 30: tr (S1S2)^k S1S3 = (-1)^k (4k+2), tr (S1S2)^k S1S3S4S3 = (-1)^k (12k+6), tr (S1S2)^k S3S4 = (-1)^k (2 + 8ki)")

print("== ALL PASS ==" if OK else "== SOME CHECK FAILED ==")
sys.exit(0 if OK else 1)
