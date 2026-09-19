"""Exact finite checks; M=sqrt(2*pi) is retained as a symbolic common factor."""
from fractions import Fraction as F
from math import factorial


def transpose(a):
    return [list(row) for row in zip(*a)]


def mm(a, b):
    return [[sum((x * y for x, y in zip(row, col)), F(0))
             for col in zip(*b)] for row in a]


def inv(a):
    n = len(a)
    aug = [[F(x) for x in row] + [F(i == j) for j in range(n)]
           for i, row in enumerate(a)]
    for k in range(n):
        pivot = next(i for i in range(k, n) if aug[i][k])
        aug[k], aug[pivot] = aug[pivot], aug[k]
        scale = aug[k][k]
        aug[k] = [x / scale for x in aug[k]]
        for i in range(n):
            if i != k:
                scale = aug[i][k]
                aug[i] = [x - scale * y for x, y in zip(aug[i], aug[k])]
    return [row[n:] for row in aug]


def psd_ldl(a):
    """Exact PSD test by rational Schur complements, including zero pivots."""
    b = [[F(x) for x in row] for row in a]
    n = len(b)
    assert b == transpose(b)
    pivots = []
    for k in range(n):
        pivot = b[k][k]
        assert pivot >= 0
        pivots.append(pivot)
        if pivot == 0:
            assert all(b[i][k] == 0 for i in range(k + 1, n))
            continue
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                b[i][j] -= b[i][k] * b[k][j] / pivot
    return pivots


def beta(n):
    return F(n * (2 * n - 1), 2)


def polynomial_rows(nmax):
    rows = [[F(1)], [F(0), F(1)]]
    for n in range(1, nmax):
        row = [F(0)] + rows[n]
        for j, x in enumerate(rows[n - 1]):
            row[j] -= beta(n) * x
        rows.append(row)
    return rows[:nmax + 1]


def moment_coefficients(kmax):
    # E_sigma[y^k] = M * coeff[p_0 in y^k], since the supplied p_n are orthogonal.
    vec = [F(1)]
    moments = [vec[0]]
    for _ in range(kmax):
        new = [F(0)] * (len(vec) + 1)
        for n, value in enumerate(vec):
            new[n + 1] += value
            if n:
                new[n - 1] += beta(n) * value
        vec = new
        moments.append(vec[0])
    return moments


MAX_N = 512
a = [F(1), F(1)]
g = [F(1), F(1, 2)]  # gamma_n = M * g[n], exactly.
for n in range(1, MAX_N):
    a.append(a[n] + beta(n) * a[n - 1])
    g.append(g[n] * F((n + 1) * (2 * n + 1), 2))
terms = [x * x / y for x, y in zip(a, g)]  # M * u_n^2.
totals = []
running = F(0)
for n, term in enumerate(terms):
    running += term
    totals.append(running)
    assert term <= (1 if n == 0 else 2)
    assert running <= 2 * n + 1
    if n >= 2:
        assert running <= F(18 * n + 9, 10)
    if n >= 3:
        assert term <= F(9, 5)
for n in range(1, MAX_N):
    assert F(2 * n, 1) - F(1, 2) > 0
    assert (2 * n - F(1, 2)) ** 2 - 4 * beta(n) == F(1, 4)
print(f"Exact recurrence and both all-degree inequalities checked for 0 <= N <= {MAX_N}.")
tau = [F(1)]
for m in range((MAX_N + 1) // 2):
    tau.append(tau[m] * (m + F(1, 2)) * (m + F(3, 4)) /
               ((m + 1) * (m + F(1, 4))))
for n in range(MAX_N + 1):
    assert totals[n] == (n + 1) * tau[(n + 1) // 2]
    if n:
        assert a[n] / a[n - 1] == (n if n % 2 else n - F(1, 2))
print(f"Exact closed kernel formula and alternating a_n ratios checked for 0 <= N <= {MAX_N}.")
print("n | a_n | gamma_n/M | M*u_n^2 | M*K_n(i,i)")
for n in range(9):
    print(f"{n} | {a[n]} | {g[n]} | {terms[n]} | {totals[n]}")

moments = moment_coefficients(20)
polys = polynomial_rows(10)
for n in range(11):
    r = [[moments[i + j] for j in range(n + 1)] for i in range(n + 1)]
    c = [row + [F(0)] * (n + 1 - len(row)) for row in polys[:n + 1]]
    norm_matrix = mm(mm(c, r), transpose(c))
    assert norm_matrix == [[g[i] if i == j else 0 for j in range(n + 1)]
                           for i in range(n + 1)]
    ri = inv(r)
    assert sum(ri[i][i] for i in range(n + 1)) <= totals[n]
    diff = [[totals[n] * (i == j) - ri[i][j] for j in range(n + 1)]
            for i in range(n + 1)]
    psd_ldl(diff)
print("Exact original-Gram norm, inverse-trace, and Loewner checks passed for 0 <= N <= 10.")
print("Moment coefficients through degree 8 (moments equal M times these):", moments[:9])

n = 4
r = [[moments[i + j] for j in range(n + 1)] for i in range(n + 1)]
ri = inv(r)
j = [[1, 0, 1, 0, 1], [0, 1, 1, 0, 0], [1, 0, 0, 2, 1]]
lam = [[1, 1, 0], [0, 1, 1]]
obs = mm(lam, j)
aat = mm(obs, transpose(obs))
aat_inv = inv(aat)
quotient = inv(mm(mm(obs, ri), transpose(obs)))  # Q = M * quotient.
comparison = [[quotient[i][k] - aat_inv[i][k] / totals[n]
               for k in range(2)] for i in range(2)]
pivots = psd_ldl(comparison)
print("Concrete Lambda J transport check, N=4:")
print("J =", j)
print("Lambda =", lam)
print("A =", obs)
print("A A* =", aat)
print("Q / M =", quotient)
print("Positive LDL pivots of Q/M - (M*K_4)^(-1)(A A*)^(-1):", pivots)

# Reference convolutions: original mass is M_k=(sqrt(2*pi))**k, never reset to 1.
for k in range(1, 13):
    alpha = F(k, 2)
    ak = [F(1), F(1)]
    gk = [F(1), alpha]  # gamma_n^[k] = M_k * gk[n].
    total = F(1) + 1 / alpha
    assert total <= 1 + max(F(1), 1 / alpha)
    for n in range(1, 128):
        ak.append(ak[n] + n * (n - 1 + alpha) * ak[n - 1])
        gk.append(gk[n] * (n + 1) * (n + alpha))
        term = ak[n + 1] ** 2 / gk[n + 1]
        total += term
        assert term <= max(F(1), 1 / alpha)
        assert total <= 1 + (n + 1) * max(F(1), 1 / alpha)
        assert (2 * n + alpha - 1) ** 2 - 4 * n * (n + alpha - 1) == (alpha - 1) ** 2
        if k == 2:
            assert term == 1
            assert total == n + 2
print("Reference convolution exact checks passed for 1 <= k <= 12, 0 <= N <= 128.")

# Exact rational/Gaussian-rational coefficient, determinant, and original-S jet tests.
import sympy as sp

cs = sp.Symbol("c", real=True)
for n in range(9):
    ts = sp.Matrix(n + 1, n + 1, lambda r, j:
                   sp.binomial(j, r) * cs ** (j - r) * sp.I ** r if r <= j else 0)
    tis = sp.Matrix(n + 1, n + 1, lambda r, j:
                    sp.binomial(j, r) * (-cs) ** (j - r) * sp.I ** (-j) if r <= j else 0)
    assert (ts * tis).applyfunc(sp.expand) == sp.eye(n + 1)
    assert ts.det() == sp.I ** (n * (n + 1) // 2)
print("Symbolic-c coefficient inverse and determinant phase checks passed for 0 <= N <= 8.")

n = 4
cs = sp.Rational(1, 2)
ts = sp.Matrix(n + 1, n + 1, lambda r, j:
               sp.binomial(j, r) * cs ** (j - r) * sp.I ** r if r <= j else 0)
jets = [(0, 0), (0, 1), (1, 0), (1, 1), (1, 2)]
js = sp.Matrix([[sp.factorial(j) / sp.factorial(j - d) * (cs + sp.I * y) ** (j - d)
                 if j >= d else 0 for j in range(n + 1)] for y, d in jets])
jy = sp.Matrix([[sp.factorial(j) / sp.factorial(j - d) * y ** (j - d)
                 if j >= d else 0 for j in range(n + 1)] for y, d in jets])
phase = sp.diag(*[sp.I ** d for _, d in jets])
assert (jy * ts - phase * js).applyfunc(sp.expand) == sp.zeros(n + 1)
assert sp.expand(js.det() - sp.I ** (n * (n + 1) // 2 - sum(d for _, d in jets)) * jy.det()) == 0
rs = sp.Matrix([[sp.Rational(moments[i + j].numerator, moments[i + j].denominator)
                 for j in range(n + 1)] for i in range(n + 1)])
hs = ts.H * rs * ts  # H_S = M * hs.
assert hs.det() == rs.det()
ls = sp.Matrix([[1, 2, 0, 1, 0], [0, 1, 1, 0, 2]])
as_original = ls * js
ay = (as_original * ts.inv()).applyfunc(sp.simplify)
assert (ay - ls * phase.inv() * jy).applyfunc(sp.simplify) == sp.zeros(2, n + 1)
q_original = (as_original * hs.inv() * as_original.H).inv().applyfunc(sp.simplify)
q_y = (ay * rs.inv() * ay.H).inv().applyfunc(sp.simplify)
assert q_original == q_y
geometry = (as_original * ts.inv() * ts.inv().H * as_original.H).applyfunc(sp.simplify)
assert geometry == (ay * ay.H).applyfunc(sp.simplify)
bound_coefficient = sp.Rational(totals[n].denominator, totals[n].numerator)
gap = (q_original - bound_coefficient * geometry.inv()).applyfunc(sp.simplify)
assert gap == gap.H
assert gap[0, 0] > 0 and gap[1, 1] > 0 and gap.det() > 0
print("Original S=1/2+i*y exact Gram, jets, determinant phase, quotient, and full-matrix bound passed (N=4).")
print("Jet derivative orders:", [d for _, d in jets])
print("det J_y =", jy.det(), "; det J_S =", js.det())
print("Q_S / M =", q_original)
print("A_S T^-1 T^{-*} A_S* =", geometry)
print("Exact positive gap diagonal and determinant:", gap[0, 0], gap[1, 1], sp.simplify(gap.det()))
